# Generated by Django 2.0.2 on 2018-11-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='telephone'),
        ),
    ]
