# Generated by Django 2.0.6 on 2018-07-02 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_remove_restaurante_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Restaurante', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Restaurante', to='blog.Lugar'),
        ),
    ]