# Generated by Django 3.1.5 on 2021-02-23 02:46

import core_fusion.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core_fusion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to=core_fusion.models.name_img, verbose_name='Imagem'),
        ),
    ]