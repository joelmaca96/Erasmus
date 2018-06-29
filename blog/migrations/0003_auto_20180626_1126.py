# Generated by Django 2.0.6 on 2018-06-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_lugar_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tema',
            old_name='Lugar',
            new_name='ciudad',
        ),
        migrations.RenameField(
            model_name='tema',
            old_name='starter',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='tema',
            old_name='subject',
            new_name='direccion',
        ),
        migrations.AddField(
            model_name='lugar',
            name='country',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tema',
            name='message',
            field=models.TextField(default=1, max_length=4000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tema',
            name='tema',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
