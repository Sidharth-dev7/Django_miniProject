# Generated by Django 5.1.5 on 2025-02-10 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_registerr_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerr',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
