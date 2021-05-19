# Generated by Django 2.2.3 on 2019-12-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackageDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=50)),
                ('trip_date', models.DateField()),
                ('trip_price', models.DecimalField(decimal_places=2, default='0', max_digits=7)),
                ('offer', models.BooleanField(default=False)),
                ('trip_img', models.ImageField(blank=True, upload_to='uploadimage')),
                ('trip_from', models.CharField(default='Delhi', max_length=100)),
                ('trip_duration', models.CharField(blank=True, default=0, max_length=50)),
                ('trip_mode', models.CharField(blank=True, default='Train', max_length=20)),
                ('package_type', models.CharField(blank=True, choices=[('family', 'FAMILY'), ('luxary', 'LUXARY'), ('youth', 'YOUTH')], default='family', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(choices=[('family', 'FAMILY'), ('luxary', 'LUXARY'), ('youth', 'YOUTH')], default='family', max_length=32)),
                ('package_name', models.CharField(max_length=32)),
                ('package_date', models.DateField()),
                ('package_price', models.DecimalField(decimal_places=2, default='0', max_digits=7)),
                ('offer', models.BooleanField(default=False)),
                ('package_img', models.ImageField(upload_to='uploadimage')),
            ],
        ),
    ]