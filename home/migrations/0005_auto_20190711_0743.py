# Generated by Django 2.2 on 2019-07-11 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190707_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='guides',
            name='album_logo',
            field=models.FileField(default=24, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guides',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
