from django.db import models
from mainapp.models import Company


class RealizationReport(models.Model):
    number = models.PositiveBigIntegerField(verbose_name='№ отчета', help_text='Номер отчёта', blank=False, unique=True)
    date_from = models.DateTimeField(verbose_name='Дата начала', help_text='Дата начала отчётного периода', blank=False)
    date_to = models.DateTimeField(verbose_name='Дата конца', help_text='Дата конца отчётного периода', blank=False)
    create_dt = models.DateTimeField(verbose_name='Дата формирования', help_text='Дата формирования отчёта', blank=False)
    sales = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Продажа', help_text='Выручка с учетом возвратов')
    transfer_for_goods = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='К перечислению за товар', help_text='Выручка за вычетом комиссии')
    logistic = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость логистики')
    penalty_logistic = models.IntegerField(verbose_name='Штраф. Повышенная логистика согласно коэффициенту по обмерам')
    penalty_other = models.IntegerField(verbose_name='Другие виды штрафов')
    penalty = models.IntegerField(verbose_name='Общая сумма штрафов')
    additional_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Доплаты')
    storage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость хранения')
    acceptance = models.IntegerField(verbose_name='Стоимость платной приемки')
    deduction = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Прочие удержания/выплаты')
    total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Итого к оплате')
    currency = models.CharField(max_length=5, verbose_name='Валюта')
    company = models.ForeignKey(Company, on_delete=models.PROTECT, blank=False)

    class Meta:
        ordering = ["-create_dt", 'company']

    def __str__(self):
        return f'{self.number}, {self.date_from}, {self.date_to} {self.company}'


class RealizationReportDetail(models.Model):
    realizationReport = models.ForeignKey(RealizationReport, on_delete=models.CASCADE, blank=False)
    gi_id = models.PositiveIntegerField(verbose_name='Номер поставки', help_text='Номер поставки')
    subject_name = models.CharField(default='', max_length=150, verbose_name='Предмет', help_text='Предмет')
    nm_id = models.PositiveIntegerField(verbose_name='Код номенклатуры', help_text='Артикул WB')
    brand_name = models.CharField(default='', max_length=50, verbose_name='Бренд', help_text='Бренд')
    sa_name = models.CharField(default='', max_length=150, verbose_name='Артикул поставщика', help_text='Артикул продавца')
    ts_name = models.CharField(default='', max_length=15, verbose_name='Размер', help_text='Размер')
    barcode = models.CharField(default='', max_length=15, verbose_name='Баркод', help_text='Баркод')
    doc_type_name = models.CharField(default='', max_length=10, verbose_name='Тип документа', help_text='Тип документа')
    quantity = models.PositiveSmallIntegerField(verbose_name='Кол-во', help_text='Количество')
    retail_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена розничная', help_text='Цена розничная')
    retail_amount = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Вайлдберриз реализовал Товар (Пр)', help_text='Сумма продаж (возвратов)')
    office_name = models.CharField(default='', max_length=50, verbose_name='Склад', help_text='Склад')
    supplier_oper_name = models.CharField(default='', max_length=50, verbose_name='Обоснование для оплаты', help_text='Обоснование для оплаты')
    order_dt = models.DateField(verbose_name='Дата заказа покупателем', help_text='Дата заказа')
    sale_dt = models.DateField(verbose_name='Дата продажи', help_text='Дата продажи')
    shk_id = models.PositiveBigIntegerField(verbose_name='ШК', help_text='Штрих-код')
    delivery_amount = models.PositiveSmallIntegerField(verbose_name='Количество доставок', help_text='Количество доставок')
    return_amount = models.PositiveSmallIntegerField(verbose_name='Количество возврата', help_text='Количество возвратов')
    delivery_rub = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Услуги по доставке товара покупателю', help_text='Стоимость логистики')
    gi_box_type_name = models.CharField(default='', max_length=15, verbose_name='Тип коробов', help_text='Тип коробов')
    ppvz_for_pay = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='К перечислению Продавцу за реализованный Товар',
                                       help_text='К перечислению продавцу за реализованный товар')
    site_country = models.CharField(default='', max_length=30, verbose_name='Страна', help_text='Страна продажи')
    penalty = models.PositiveIntegerField(verbose_name='Общая сумма штрафов', help_text='Штрафы')
    additional_payment = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Доплаты', help_text='Доплаты')
    storage_fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Хранение', help_text='Стоимость хранения', null=True, blank=True)
    deduction = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Удержания', help_text='Прочие удержания/выплаты', null=True, blank=True)
    acceptance = models.IntegerField(verbose_name='Платная приемка', help_text='Стоимость платной приёмки', null=True, blank=True)

    def __str__(self):
        return f'{self.sa_name}, артикул: {self.nm_id}, баркод: {self.shk_id}, хранение: {self.storage_fee}'

