# Generated by Django 3.2.17 on 2023-02-07 00:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_spark', '0005_alter_event_optional_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='optional_end_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]