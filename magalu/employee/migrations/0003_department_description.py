# Generated by Django 2.2.1 on 2019-05-12 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190511_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]