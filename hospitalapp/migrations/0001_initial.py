# Generated by Django 4.0.2 on 2022-03-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedModel',
            fields=[
                ('Bed_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_id', models.IntegerField(blank=True, null=True)),
                ('hospital_name', models.CharField(help_text='Enter Hospital Name', max_length=100)),
                ('location', models.CharField(help_text='Enter Location', max_length=100)),
                ('mobile', models.BigIntegerField(help_text='Enter Mobile Number')),
                ('category', models.CharField(help_text='Select Category', max_length=100)),
                ('beds_available', models.IntegerField(help_text='No-of Beds Available')),
                ('cost', models.IntegerField(help_text='Enter Cost')),
                ('details', models.TextField(help_text='Enter Additional Details', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Bed_details',
            },
        ),
        migrations.CreateModel(
            name='HospitalRegistrationModel',
            fields=[
                ('hospital_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(help_text='Enter Supplier Name', max_length=100)),
                ('mobile', models.BigIntegerField(help_text='Enter Mobile Number')),
                ('email', models.EmailField(help_text='Enter Email', max_length=100)),
                ('location', models.CharField(help_text='Enter Location', max_length=100)),
                ('hospital_address', models.CharField(help_text='Enter Hospital Address', max_length=100)),
                ('password', models.CharField(help_text='Enter Password', max_length=100)),
                ('status', models.CharField(default='pending', max_length=100, null=True)),
            ],
            options={
                'db_table': 'hospital_reg_details',
            },
        ),
        migrations.CreateModel(
            name='VentilatorModel',
            fields=[
                ('Ventilator_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(help_text='Enter Hospital Name', max_length=100)),
                ('ventilator_company', models.CharField(help_text='Enter Ventilator Company', max_length=100)),
                ('location', models.CharField(help_text='Enter Location', max_length=100)),
                ('mobile', models.BigIntegerField(help_text='Enter Mobile Number')),
                ('category', models.CharField(help_text='Select Category', max_length=100)),
                ('ventilators_available', models.IntegerField(help_text='No-of Ventilators Available')),
                ('cost', models.IntegerField(help_text='Enter Cost')),
                ('details', models.TextField(help_text='Enter Additional Details', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Ventilator_details',
            },
        ),
    ]