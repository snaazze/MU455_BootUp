# Generated by Django 3.0.8 on 2020-07-30 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentiment',
            name='sentiment',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentiment',
            name='translated_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=5000),
            preserve_default=False,
        ),
    ]
