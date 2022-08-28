# Generated by Django 4.1 on 2022-08-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobportal',
            name='address',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobportal',
            name='place',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobportal',
            name='discriptions',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
