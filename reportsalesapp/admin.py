from django.contrib import admin
from .models import RealizationReport, RealizationReportDetail


class RealizationReportAdmin(admin.ModelAdmin):
    list_display = ['company', 'number', 'date_from', 'date_to', 'create_dt', 'sales', 'transfer_for_goods',
                    'logistic', 'penalty', 'additional_payment', 'storage', 'acceptance', 'deduction',
                    'total', 'date_from', 'date_to', 'create_dt', 'sales', 'transfer_for_goods',
                    ]
    ordering = ['-date_to', '-company']


class RealizationReportDetailAdmin(admin.ModelAdmin):
    list_display = ['sale_dt', 'subject_name', 'sa_name', 'nm_id', 'doc_type_name', 'quantity', 'retail_amount',
                    'delivery_rub', 'ppvz_for_pay',
                    ]
    ordering = ['-sale_dt']

admin.site.register(RealizationReport, RealizationReportAdmin)
admin.site.register(RealizationReportDetail, RealizationReportDetailAdmin)
