# Generated by Django 2.2.12 on 2020-05-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchquery',
            name='total_results',
            field=models.IntegerField(default=0, null=True, verbose_name='Total results'),
        ),
    ]