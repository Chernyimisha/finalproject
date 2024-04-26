from django.contrib import admin
from django.shortcuts import HttpResponse
from .models import RealizationReport, RealizationReportDetail
from .utils import query_utils, mapping_utils, input_data_general_report_utils


@admin.action(description='Пометить как отраженный в Главной книге')
def reset_status_true(modeladmin, request, queryset):
    fields = ['nm_id', 'sa_name', 'quantity', 'doc_type_name', 'retail_amount',
              'delivery_rub', 'ppvz_for_pay']
    for report in queryset:
        query = query_utils.get_details_period(report, fields=fields)
        set_nm_id = mapping_utils.add_set_nm_id(query)
        mapping_data = mapping_utils.aggregation_by_item(query, set_nm_id)
        try:
            mapping_utils.control_method(report, mapping_data)
        except Exception as e:
            return HttpResponse(f"Oops, something went wrong: {e}")
        print("input")
        input_data_general_report_utils.input_data_general_report(mapping_data)
        if not input_data_general_report_utils.control_data(mapping_data):
            input_data_general_report_utils.input_data_general_report(mapping_data, firstiteration=False)
    queryset.update(status=True)


@admin.action(description='Пометить как НЕотраженный в в Главной книге')
def reset_status_false(modeladmin, request, queryset):
    queryset.update(status=False)


class RealizationReportAdmin(admin.ModelAdmin):
    list_display = ['status', 'company', 'number', 'date_from', 'date_to', 'create_dt', 'sales', 'transfer_for_goods',
                    'logistic', 'penalty', 'additional_payment', 'storage', 'acceptance', 'deduction',
                    'total', 'date_from', 'date_to', 'create_dt', 'sales', 'transfer_for_goods',
                    ]
    ordering = ['-date_to', '-company']
    actions = [reset_status_true, reset_status_false]


class RealizationReportDetailAdmin(admin.ModelAdmin):
    list_display = ['sale_dt', 'subject_name', 'sa_name', 'nm_id', 'doc_type_name', 'quantity', 'retail_amount',
                    'delivery_rub', 'ppvz_for_pay',
                    ]
    ordering = ['-sale_dt']

admin.site.register(RealizationReport, RealizationReportAdmin)
admin.site.register(RealizationReportDetail, RealizationReportDetailAdmin)
