from django.db import models

#Contact Us Backend Start.
class ContactModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,help_text="Enter Username")
    email=models.EmailField(max_length=100,help_text="Enter Email")
    subject=models.CharField(max_length=100,help_text="Enter Subject")
    message=models.CharField(max_length=100,help_text="Enter Your Message")
    
    class Meta:
        db_table= "Contact_details"
    
    def __str__(self):
        return self.user_id+''+self.name
#Contact Us Backend End.

