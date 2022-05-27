from django.db import models
from datetime import datetime

# Create your models here.

class O2supplierRegistrationModel(models.Model):
    supp_id=models.AutoField(primary_key=True)
    supp_name=models.CharField(max_length=100,help_text="Enter Supplier Name")
    mobile=models.BigIntegerField(help_text="Enter Mobile Number", null=True)
    alternate_mobile=models.BigIntegerField(help_text="Enter Alternate Number", null=True)
    email=models.EmailField(max_length=100,help_text="Enter Email")
    password=models.CharField(max_length=100,help_text="Enter Password")
    status=models.CharField(default='pending',max_length=100,null=True)

    class Meta:
        db_table= "supp_reg_details"
    
    def __str__(self):
        return self.supp_id+' '+self.supp_name


class CylinderModel(models.Model):
    cylinder_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=100, null=True, help_text="Enter Company Name")
    distributor_name=models.CharField(max_length=100, null=True, help_text="Enter Distributor Name")
    location=models.CharField(max_length=100, null=True, help_text="Enter Location")
    mobile=models.BigIntegerField(null=True)
    category=models.CharField(max_length=100, null=True, help_text="Select Category")
    packages=models.CharField(max_length=100, help_text="Enter Package's" )
    cost=models.IntegerField(null=True)
    details=models.TextField()
    date=models.DateTimeField(default=datetime.now())


    class Meta:
        db_table= "cylinder_details"
    
    def __str__(self):
        return self.company_name
