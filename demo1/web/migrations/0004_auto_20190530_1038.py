# Generated by Django 2.2.1 on 2019-05-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190530_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auto',
            field=models.CharField(default=None, max_length=20, verbose_name='作者'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='abs'),
        ),
    ]
