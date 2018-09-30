# Generated by Django 2.1.1 on 2018-09-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='modify_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modify Date'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='NAME'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='NAME'),
        ),
    ]