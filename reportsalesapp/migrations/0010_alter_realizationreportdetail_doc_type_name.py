# Generated by Django 5.0.4 on 2024-04-14 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsalesapp', '0009_alter_realizationreportdetail_doc_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizationreportdetail',
            name='doc_type_name',
            field=models.CharField(blank=True, default=None, help_text='Тип документа', max_length=10, null=True, verbose_name='Тип документа'),
        ),
    ]