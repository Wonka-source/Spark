# Generated by Django 3.2.17 on 2023-02-07 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spark', '0006_alter_event_optional_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='optional_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
