from django.contrib import admin
from .models import Company, Individ, Employe, APIKey, APIUrl


class IndividAdmin(admin.ModelAdmin):
    list_display = ['family', 'name', 'surname', 'email', 'phone', 'registration_date', 'status']
    ordering = ['-registration_date']


class EmployedAdmin(admin.ModelAdmin):
    list_display = ['jobtitle', 'individ', 'salary', 'startjob', 'status']
    ordering = ['startjob']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['longname', 'inn', 'ogrn', 'registration_date', 'director', 'status']
    ordering = ['-registration_date']


class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['description', 'company', 'lastusage']
    ordering = ['-description']


class APIUrlAdmin(admin.ModelAdmin):
    list_display = ['description', 'url', 'request', 'validity']
    ordering = ['-description']


admin.site.register(Individ, IndividAdmin)
admin.site.register(Employe, EmployedAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(APIKey, APIKeyAdmin)
admin.site.register(APIUrl, APIUrlAdmin)


