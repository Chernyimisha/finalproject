# Generated by Django 5.0.4 on 2024-04-14 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportsalesapp', '0003_rename_realizationreport_id_realizationreport_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realizationreportdetail',
            name='rrd_id',
        ),
    ]