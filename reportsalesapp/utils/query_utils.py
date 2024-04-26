from reportsalesapp.models import RealizationReportDetail, RealizationReport


def get_details_period(report: RealizationReport, **kwargs):
    if 'fields' in kwargs and ('date_from' in kwargs and 'date_to' in kwargs):
        query = RealizationReportDetail.objects.filter(
            realizationReport=report,
            sale_dt__gte=kwargs['date_from'],
            sale_dt__lte=kwargs['date_to'],
        ).values(*kwargs['fields'])
    elif 'date_from' in kwargs and 'date_to' in kwargs:
        query = RealizationReportDetail.objects.filter(
            realizationReport=report,
            sale_dt__gte=kwargs['date_from'],
            sale_dt__lte=kwargs['date_to'])
    elif 'fields' in kwargs:
        query = RealizationReportDetail.objects.filter(
            realizationReport=report,
        ).values(*kwargs['fields'])
    else:
        query = RealizationReportDetail.objects.filter(
            realizationReport=report)
    return query








