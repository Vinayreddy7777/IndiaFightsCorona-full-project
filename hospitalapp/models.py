from django.db import models

#Hospital Registration Backend Start.
class HospitalRegistrationModel(models.Model):
    hospital_id=models.AutoField(primary_key=True)
    hospital_name=models.CharField(max_length=100,help_text="Enter Supplier Name")
    mobile=models.BigIntegerField(help_text="Enter Mobile Number")
    email=models.EmailField(max_length=100,help_text="Enter Email")
    location=models.CharField(max_length=100,help_text="Enter Location")
    hospital_address=models.CharField(max_length=100,help_text="Enter Hospital Address")
    password=models.CharField(max_length=100,help_text="Enter Password")
    status=models.CharField(default='pending',max_length=100,null=True)

    class Meta:
        db_table= "hospital_reg_details"
    
    def __str__(self):
        return self.hospital_id+''+self.hospital_name
#Hospital Registration Backend End.


#Hospital Add Bed Backend Start.
class BedModel(models.Model):
    Bed_id=models.AutoField(primary_key=True)
    hospital_id=models.IntegerField(null=True,blank=True)
    hospital_name=models.CharField(max_length=100,help_text="Enter Hospital Name")
    location=models.CharField(max_length=100,help_text="Enter Location")
    mobile=models.BigIntegerField(help_text="Enter Mobile Number")
    category=models.CharField(max_length=100,help_text="Select Category",)
    beds_available=models.IntegerField(help_text="No-of Beds Available")
    cost=models.IntegerField(help_text="Enter Cost")
    details=models.TextField(max_length=100,help_text="Enter Additional Details", null=True)
    
    class Meta:
        db_table= "Bed_details"
    
    def __str__(self):
        return self.Bed_id+' '+self.hospital_name
#Hospital Add Bed Backend End.



#Hospital Add Ventilator Backend Start.
class VentilatorModel(models.Model):
    Ventilator_id=models.AutoField(primary_key=True)
    hospital_name=models.CharField(max_length=100,help_text="Enter Hospital Name")
    ventilator_company=models.CharField(max_length=100,help_text="Enter Ventilator Company")
    location=models.CharField(max_length=100,help_text="Enter Location")
    mobile=models.BigIntegerField(help_text="Enter Mobile Number")
    category=models.CharField(max_length=100,help_text="Select Category")
    ventilators_available=models.IntegerField(help_text="No-of Ventilators Available")
    cost=models.IntegerField(help_text="Enter Cost")
    details=models.TextField(max_length=100,help_text="Enter Additional Details", null=True)
    
    class Meta:
        db_table= "Ventilator_details"
    
    def __str__(self):
        return self.Ventilator_id+' '+self.hospital_name
#Hospital Add Ventilator Backend End.

