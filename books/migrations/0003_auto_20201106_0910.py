# Generated by Django 3.1.3 on 2020-11-06 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('speciall_status', 'Can read all book')]},
        ),
    ]
