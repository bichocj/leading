# Generated by Django 2.0.2 on 2018-11-16 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='code',
            new_name='leadgen_id',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='code',
            new_name='page_id',
        ),
    ]