# Generated by Django 4.1.1 on 2022-09-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LinkedIn', '0014_alter_chat_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Comment Date'),
        ),
    ]
