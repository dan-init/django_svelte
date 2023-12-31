# Generated by Django 4.2.4 on 2023-08-03 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Drivetrace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivetrace_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=255)),
                ('test_datetime', models.DateTimeField()),
                ('cell', models.CharField(max_length=5)),
                ('iwr', models.IntegerField()),
                ('rmsse', models.IntegerField()),
                ('total_co', models.IntegerField()),
                ('total_co2', models.IntegerField()),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cdt_app.driver')),
                ('drivetrace', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cdt_app.drivetrace')),
                ('engineer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cdt_app.engineer')),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cdt_app.vehicle')),
            ],
        ),
    ]
