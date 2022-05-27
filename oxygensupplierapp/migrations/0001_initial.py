# Generated by Django 4.0.2 on 2022-03-24 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CylinderModel',
            fields=[
                ('cylinder_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(help_text='Enter Company Name', max_length=100, null=True)),
                ('distributor_name', models.CharField(help_text='Enter Distributor Name', max_length=100, null=True)),
                ('location', models.CharField(help_text='Enter Location', max_length=100, null=True)),
                ('mobile', models.BigIntegerField(null=True)),
                ('category', models.CharField(help_text='Select Category', max_length=100, null=True)),
                ('packages', models.CharField(help_text="Enter Package's", max_length=100)),
                ('cost', models.IntegerField(null=True)),
                ('details', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 24, 11, 55, 44, 308462))),
            ],
            options={
                'db_table': 'cylinder_details',
            },
        ),
        migrations.CreateModel(
            name='O2supplierRegistrationModel',
            fields=[
                ('supp_id', models.AutoField(primary_key=True, serialize=False)),
                ('supp_name', models.CharField(help_text='Enter Supplier Name', max_length=100)),
                ('mobile', models.BigIntegerField(help_text='Enter Mobile Number', null=True)),
                ('alternate_mobile', models.BigIntegerField(help_text='Enter Alternate Number', null=True)),
                ('email', models.EmailField(help_text='Enter Email', max_length=100)),
                ('password', models.CharField(help_text='Enter Password', max_length=100)),
                ('status', models.CharField(default='pending', max_length=100, null=True)),
            ],
            options={
                'db_table': 'supp_reg_details',
            },
        ),
    ]
