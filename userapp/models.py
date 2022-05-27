from django.db import models
from datetime import datetime


# Create your models here.
class UserRegistrationModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,help_text="Enter Username")
    mobile=models.BigIntegerField(help_text="Enter Mobile Number")
    email=models.EmailField(max_length=100,help_text="Enter Email")
    location=models.CharField(max_length=100,help_text="Enter Location")
    pin=models.IntegerField(help_text="Enter Mobile Number")
    password=models.CharField(max_length=100,help_text="Enter Password")
    profile_image=models.ImageField(upload_to='images/', null=True)

    
    class Meta:
        db_table= "user_reg_details"
    
    def __str__(self):
        return self.user_id+' '+self.username


class PlasmaDonorsModel(models.Model):
    plasma_donor_id=models.AutoField(primary_key=True)
    plasma_donor_name=models.CharField(max_length=100, null=True, help_text="Enter Your Name")
    donor_contact_number=models.BigIntegerField(null=True)
    donor_alternate_number=models.BigIntegerField(null=True)
    email=models.CharField(max_length=100, null=True, help_text="Enter Your Email")
    location=models.CharField(max_length=100, null=True, help_text="Enter Your Location")
    blood_group=models.CharField(max_length=100, help_text="Select Your Blood Group" )
    desc=models.TextField()
    date=models.DateTimeField(default=datetime.now())

    class Meta:
        db_table= "plasma_donors"
    
    def __str__(self):
        return self.donor_id+''+self.donor_name

    
class RationDonorsModel(models.Model):
    ration_donor_id=models.AutoField(primary_key=True)
    ration_donor_name=models.CharField(max_length=100, null=True, help_text="Enter Your Name")
    donor_contact_number=models.BigIntegerField(null=True)
    donor_alternate_number=models.BigIntegerField(null=True)
    email=models.CharField(max_length=100, null=True, help_text="Enter Your Email")
    location=models.CharField(max_length=100, null=True, help_text="Enter Your Location")
    who_you_are=models.CharField(max_length=100, help_text="Select Who You are" )
    desc=models.TextField()
    date=models.DateTimeField(default=datetime.now())

    class Meta:
        db_table= "ration_donors"
    
    def __str__(self):
        return self.donor_id+''+self.donor_name
    
    


class UserRequestModel(models.Model):
    request_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=True, help_text="Enter Your Name")
    mobile=models.BigIntegerField(null=True)
    alternate_mobile=models.BigIntegerField(null=True)
    email=models.CharField(max_length=100, null=True, help_text="Enter Your Email")
    location=models.CharField(max_length=100, null=True, help_text="Enter Your Location")
    pin=models.IntegerField(null=True)
    requesting_for=models.CharField(max_length=100, help_text="Select What you are Requesting for?" )
    message=models.TextField()
    date_time=models.DateTimeField(default=datetime.now())

    class Meta:
        db_table= "users_request"
    
    def __str__(self):
        return self.request_id+' '+self.name
    

class UsersFeedbackModel(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=100, help_text="Select Your Category" )
    user_name=models.CharField(max_length=100, null=True, help_text="Enter Your Name")
    user_number=models.BigIntegerField(null=True)
    user_email=models.CharField(max_length=100, help_text="Enter Your Email")
    feedback=models.TextField()
    user_photo=models.CharField(null=True,blank=True,max_length=200)
    date=models.DateTimeField(default=datetime.now())

    class Meta:
        db_table= "users_feedback"
    
    def __str__(self):
        return self.category+' '+self.user_name




