# Generated by Django 3.0.3 on 2020-11-22 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashionote', '0002_remove_brand_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='star',
        ),
    ]
