# Generated by Django 2.2 on 2019-07-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('experience', models.TextField()),
                ('area', models.TextField()),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
