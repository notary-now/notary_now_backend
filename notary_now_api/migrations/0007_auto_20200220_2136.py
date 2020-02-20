# Generated by Django 3.0.3 on 2020-02-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notary_now_api', '0006_notary_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(),
        ),
    ]
