# Generated by Django 2.2 on 2020-11-27 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0004_auto_20201127_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]
