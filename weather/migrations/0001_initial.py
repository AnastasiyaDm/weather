from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(default='city_name', max_length=100)),
                ('cord_lon', models.CharField(default='cord_lon', max_length=100)),
                ('cord_lat', models.CharField(default='cord_lat', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_main', models.TextField()),
                ('weather_description', models.TextField()),
                ('temp', models.CharField(default='temp', max_length=100)),
                ('date_time', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.City')),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_main', models.TextField()),
                ('weather_description', models.TextField()),
                ('temp', models.CharField(default='temp', max_length=100)),
                ('date_time', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.City')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='weather',
            unique_together={('city', 'date_time')},
        ),
        migrations.AlterUniqueTogether(
            name='forecast',
            unique_together={('city', 'date_time')},
        ),
    ]