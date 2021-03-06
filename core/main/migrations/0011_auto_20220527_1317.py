# Generated by Django 3.2.5 on 2022-05-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_booking_productfortours'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='The service type name')),
                ('describe', models.TextField(verbose_name='Service describe')),
                ('img', models.ImageField(upload_to='media', verbose_name='Image of type')),
            ],
            options={
                'verbose_name': 'Type of service',
                'verbose_name_plural': 'Types of the services',
            },
        ),
        migrations.CreateModel(
            name='TourPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Travel place name')),
                ('describe', models.TextField(max_length=1000, verbose_name='Travel place decsribtion')),
                ('img', models.ImageField(upload_to='media', verbose_name='Travel place image')),
                ('price', models.IntegerField(verbose_name='Travel place price')),
                ('in_page', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Tour place',
                'verbose_name_plural': 'Tour places',
            },
        ),
        migrations.RenameModel(
            old_name='Booking',
            new_name='BookingStayPlace',
        ),
        migrations.DeleteModel(
            name='aboutus',
        ),
        migrations.DeleteModel(
            name='blog',
        ),
        migrations.DeleteModel(
            name='flights',
        ),
        migrations.DeleteModel(
            name='stays',
        ),
        migrations.AlterField(
            model_name='touridea',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Travel place price'),
        ),
    ]
