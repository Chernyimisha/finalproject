from django import forms
from mainapp.models import Company
from .models import RealizationReport, RealizationReportDetail
import os


class RealizationReportUploadFileExcelForm(forms.Form):
    company = forms.ModelChoiceField(label="Выберите фирму", queryset=Company.objects.all())
    file = forms.FileField(label="Выберите файл .xlsx")

    def clean_file(self):
        file = self.cleaned_data['file']
        if os.path.splitext(file.name)[1].lower().rfind('xl') == -1:
            raise forms.ValidationError('Неверный формат файла. Выберите excel-файл!')
        return file


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        for file in data:
            if os.path.splitext(file.name)[1].lower().rfind('zip') == -1:
                raise forms.ValidationError('Неверный формат файла. Выберите zip-файлы!')
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class RealizationReportDetailUploadFileExcelForm(forms.Form):
    files = MultipleFileField(label="Выберите один или несколько файлов .zip")


class RealizationReportDetailDelete(forms.Form):
    realizationReport = forms.ModelChoiceField(label="Выберите отчет",
                                               queryset=RealizationReport.objects.filter(realizationreportdetail__realizationReport__isnull=False).distinct())


class UploadGeneralFileExcelForm(forms.Form):
    file = forms.FileField(label="Загрузите файл Вайлдберриз.xlsx", required=False)

    def clean_file(self):
        file = self.cleaned_data['file']
        if os.path.splitext(file.name)[-1].lower().rfind('xl') == -1:
            raise forms.ValidationError('Неверный формат файла. Выберите excel-файл!')
        return file
