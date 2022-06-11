# Generated by Django 3.2.5 on 2022-05-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_index_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='stays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Hotel name')),
                ('img', models.ImageField(upload_to='media', verbose_name='Hotel image')),
                ('price', models.IntegerField(verbose_name='hotel one nigth price')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
        ),
    ]
