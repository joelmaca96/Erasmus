# Generated by Django 2.0.6 on 2018-06-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180626_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='Subimg1',
            field=models.ImageField(default=1, upload_to='Places'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lugar',
            name='Subimg2',
            field=models.ImageField(default=1, upload_to='Places'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lugar',
            name='Subimg3',
            field=models.ImageField(default=1, upload_to='Places'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lugar',
            name='Subimg4',
            field=models.ImageField(default=1, upload_to='Places'),
            preserve_default=False,
        ),
    ]
