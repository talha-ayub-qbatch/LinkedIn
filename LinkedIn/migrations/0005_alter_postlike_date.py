# Generated by Django 4.1.1 on 2022-09-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkedIn', '0004_postlike_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
