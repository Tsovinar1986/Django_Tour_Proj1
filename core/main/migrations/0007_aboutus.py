# Generated by Django 3.2.5 on 2022-05-25 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_fligths_flights'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='about ouw company what we giva and what we have')),
                ('img', models.ImageField(upload_to='media', verbose_name='Images of us or travel places')),
            ],
            options={
                'verbose_name': 'about us',
                'verbose_name_plural': 'about our traveling types',
            },
        ),
    ]
