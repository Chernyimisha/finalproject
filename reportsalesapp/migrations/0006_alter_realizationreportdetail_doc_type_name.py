# Generated by Django 5.0.4 on 2024-04-14 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsalesapp', '0005_alter_realizationreportdetail_acceptance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizationreportdetail',
            name='doc_type_name',
            field=models.CharField(default=None, help_text='Тип документа', max_length=10, verbose_name='Тип документа'),
        ),
    ]
