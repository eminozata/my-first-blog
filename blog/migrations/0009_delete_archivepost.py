# Generated by Django 3.2.6 on 2021-10-02 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_archivepost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArchivePost',
        ),
    ]