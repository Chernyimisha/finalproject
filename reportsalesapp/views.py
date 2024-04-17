import openpyxl
import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from reportsalesapp import forms
from django.db.transaction import atomic
from django.core.files.temp import NamedTemporaryFile
from .utils import os_utils, openpyxl_utils
from .models import RealizationReport, RealizationReportDetail
from goodseller import settings
import logging
import zipfile

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'reportsalesapp/index.html')


def crud_report(request):
    return render(request, 'reportsalesapp/crud_report.html')


def crud_detail(request):
    return render(request, 'reportsalesapp/crud_detail.html')


def general_report(request):
    return render(request, 'reportsalesapp/general_report.html')


def upload_general_file_excel(request):
    if request.method == 'POST':
        form = forms.UploadGeneralFileExcelForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            fs = FileSystemStorage()
            fs.save(file.name, file)
            logger.info(f'Add general file: {file.name}.')
            return HttpResponse(f"Главный файл: {file.name} успешно добавлен.")
    else:
        form = forms.UploadGeneralFileExcelForm()
    return render(request, 'reportsalesapp/upload_file.html', {'form': form})


def delete_realization_detail(request):
    if request.method == 'POST':
        form = forms.RealizationReportDetailDelete(request.POST)
        if form.is_valid():
            realization_report = form.cleaned_data['realizationReport']
            detail = RealizationReportDetail.objects.filter(realizationReport=realization_report)
            detail.delete()
            logger.info(f'Удалена детализация к отчету: {realization_report.number}.')
            return HttpResponse(f"Детализация к отчету: {realization_report.number} успешно удалена.")
    else:
        form = forms.RealizationReportDetailDelete()
    return render(request, 'reportsalesapp/delete_detail.html', {'form': form})


def batch_bulk_create_detail(objects, batch_size):
    for i in range(0, len(objects), batch_size):
        RealizationReportDetail.objects.bulk_create(objects[i:i+batch_size])


def upload_realization_detail_excel(request):
    if request.method == 'POST':
        form = forms.RealizationReportDetailUploadFileExcelForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['files']
            report_numbers = {v for i in RealizationReport.objects.values('number') for v in i.values()}
            realization_reports = RealizationReport.objects.filter(realizationreportdetail__realizationReport__isnull=False).distinct()
            good_numbers = []
            bad_numbers = []
            other_numbers = []
            for file in files:
                lines = []
                report_number = int(os.path.splitext(file.name)[0].split(' ')[-1].strip('№'))
                if report_number in report_numbers:
                    realizationreport = RealizationReport.objects.filter(number=report_number).first()
                    if realizationreport not in realization_reports:
                        with NamedTemporaryFile(dir=settings.TEMPSTORAGE_ROOT) as tmp_zip, \
                                NamedTemporaryFile(dir=settings.TEMPSTORAGE_ROOT, mode='w+b') as tmp_xls:
                            for chunk in file.chunks():
                                tmp_zip.write(chunk)
                            with zipfile.ZipFile(tmp_zip) as zf:
                                for f in zf.infolist():
                                    if '0' in f.filename or 'weekly_report.xlsx' in f.filename:
                                        byte_text = zf.read(f)
                            tmp_xls.write(byte_text)
                            lines = openpyxl_utils.parsing_realization_report_detail(tmp_xls, realizationreport)
                        good_numbers.append(report_number)
                else:
                    bad_numbers.append(report_number)
                batch_bulk_create_detail(lines, 999)
                logger.info(f'File {file.name} processing successfully')
            context = {
                'good_numbers': good_numbers,
                'bad_numbers': bad_numbers,
            }
            return render(request, 'reportsalesapp/result_input_detail.html', context)
    else:
        form = forms.RealizationReportDetailUploadFileExcelForm()
    return render(request, 'reportsalesapp/upload_file.html', {'form': form})


def upload_realization_report_excel(request):
    """
    Функция-представление, обрабатывающая POST запрос, содержащий в себе форму с данными об экземпляре
    класса Сompany и файл-эксель с отчетами о реализации товаров за неделю. Функция в случае
    успешной валидации извлекает из формы данные о компании и наименование загруженного файла "file_name". Далее создается
    список "report_numbers" номеров отчетов, уже имеющихся в базе данных на момент загрузки новых. Номера должны быть строго
    уникальны, поэтому данный список поможет отсеять из вновь поступающих ненужные отчеты.
    Далее с помощью экземпляра "NamedTemporaryFile()" путем поэтапной записи "chunks" создается временный файл для помещения в него полученного
    из формы файла. Этот способ позволяет не сохранять в обычном виде загружаемый файл на сервере для его обработки.
    Через некоторое время файл автоматически удаляется из временного хранилища.
    После того как сформировался временный эксель файл он обрабатывается ("парсится") утилитой "parsing_realization_report(company, tmp, report_numbers)"
    из пользовательского модуля "openpyxl_utils", формируя список экземпляров "RealizationReport" для сохранения в БД.
    Далее с помощью метода "bulk_create" с параметром "reports" пакетно формируем записи в БД.
    Функция обеспечивает:
    - автоматическую загрузку данных в базу через "парсинг" эксель файла;
    - маппинг данных перед загрузкой (игнорирование имеющихся записей), проверка валидности;
    - пост-удаление загруженных файлов;
    - логгирование процесса;
    - оповещение пользователя о результатах обработки данных.
    :param request: Request object
    :return: render
    """
    if request.method == 'POST':
        form = forms.RealizationReportUploadFileExcelForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.cleaned_data['company']
            file_name = form.cleaned_data['file']
            report_numbers = {v for i in RealizationReport.objects.values('number') for v in i.values()}
            with NamedTemporaryFile(dir=settings.TEMPSTORAGE_ROOT) as tmp:
                for chunk in form.cleaned_data['file'].chunks():
                    tmp.write(chunk)
                reports = openpyxl_utils.parsing_realization_report(company, tmp, report_numbers)
            logger.info(f'File {file_name} uploaded successfully')
            RealizationReport.objects.bulk_create(reports)
            logger.info(f'File {file_name} processing successfully')
            return HttpResponse(f"{file_name} успешно сохранены.")
    else:
        form = forms.RealizationReportUploadFileExcelForm()
    return render(request, 'reportsalesapp/upload_file.html', {'form': form})

