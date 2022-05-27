from django.forms import HiddenInput
from django.shortcuts import render,redirect
from userapp.models import UserRegistrationModel, PlasmaDonorsModel, RationDonorsModel, UsersFeedbackModel, UserRequestModel
from hospitalapp.models import BedModel, VentilatorModel
from oxygensupplierapp.models import CylinderModel

#importing resources for messages.
from django.contrib import messages


import re

#User Login Backend Start.
def user_login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            check=UserRegistrationModel.objects.get(email=email,password=password)
            request.session["user_id"]=check.user_id
            messages.success(request,'Login Successful')
            return redirect('user_home')
        except:
            messages.error(request, "Invalid Login") 
    return render(request,'user/user-login.html')
#User Login Backend End.

#User Registration Backend Start.
def user_registration(request):
    if request.method == "POST" and request.FILES["photo"]:
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        location = request.POST.get('location')
        pin = request.POST.get('pin')
        password = request.POST.get('password')
        profile_image = request.FILES['photo']
        
        # if len(username) < 5:
        #     messages.error (request, "user name must be 10 characters")
        # # elif not username.isalpha():
        # #     messages.error (request, "username should only contain letters")
        # elif len(mobile)!=10:
        #     messages.error (request,"mobile number should be ten digits")
        # elif len(password) < 8:
        #     messages.error (request, "Make sure your password is atleast 8 letters")
        # elif re.search('[0-9]', password) is None:
        #     messages.error (request, "Make sure your password has a number in it")
        # elif re.search('[A-Z]',password) is None:
        #     messages.error (request, "Make sure your password has a capital letter in it")
        
        if UserRegistrationModel.objects.filter(email=email).exists():
            messages.error (request, "Email already exist")   
                 
        else:
            User=UserRegistrationModel.objects.create(username=username,mobile=mobile,email=email,location=location,pin=pin,password=password,profile_image=profile_image)
            User.save()
        
            messages.success(request, "Account created successful")


        # messages.error(request, "Error. Message not sent.")
        
    return render(request,'user/user-registration.html')
#User Registration Backend End.


def user_home(request):
    feedback= UsersFeedbackModel.objects.all()
    return render(request,'user/user-dashboard.html',{'f':feedback})

def user_donate_plasma(request):
    if request.method == "POST":
        plasma_donor_name=request.POST.get('name')
        donor_contact_number=request.POST.get('mobile')
        donor_alternate_number=request.POST.get('alternatemobile')
        email=request.POST.get('email')
        location=request.POST.get('location')
        blood_group=request.POST.get('bloodgroup')
        desc=request.POST.get('description')

        user=PlasmaDonorsModel.objects.create(plasma_donor_name=plasma_donor_name,donor_contact_number=donor_contact_number,donor_alternate_number=donor_alternate_number,email=email,location=location,blood_group=blood_group,desc=desc)
        user.save()       
        
        if user:    
            messages.success(request, "Donated Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")

    return render(request,'user/user-donate-plasma.html')

def user_donate_ration(request):
    if request.method == "POST":
        ration_donor_name=request.POST.get('name')
        donor_contact_number=request.POST.get('mobile')
        donor_alternate_number=request.POST.get('alternatemobile')
        email=request.POST.get('email')
        location=request.POST.get('location')
        who_you_are=request.POST.get('whoareyou')
        desc=request.POST.get('description')

        user=RationDonorsModel.objects.create(ration_donor_name=ration_donor_name,donor_contact_number=donor_contact_number,donor_alternate_number=donor_alternate_number,email=email,location=location,who_you_are=who_you_are,desc=desc)
        user.save()
        
        if user:    
            messages.success(request, "Donated Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
            
    return render(request,'user/user-donate-ration.html')

def user_request_help(request):
    if request.method == "POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        alternate_mobile=request.POST.get('alternatemobile')
        email=request.POST.get('email')
        location=request.POST.get('location')
        pin=request.POST.get('pin')
        requesting_for=request.POST.get('requestingfor')
        message=request.POST.get('message')

        user=UserRequestModel.objects.create(name=name,mobile=mobile,alternate_mobile=alternate_mobile,email=email,location=location,pin=pin,requesting_for=requesting_for,message=message)
        user.save()
        
        if user:    
            messages.success(request, "Requested Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
            
    return render(request,'user/user-request-help.html')

def user_feedback(request):
    user_id = request.session["user_id"]
    if request.method == "POST":
        category=request.POST.get('category')
        user_name=request.POST.get('name')
        user_number=request.POST.get('mobile')
        user_email=request.POST.get('email')
        user_details = UserRegistrationModel.objects.get(user_id=user_id)
        user_photo=user_details.profile_image
        feedback=request.POST.get('feedback')      

        user=UsersFeedbackModel.objects.create(category=category,user_name=user_name,user_number=user_number,user_email=user_email,feedback=feedback,user_photo=user_photo)
        user.save()
        
        if user:    
            messages.success(request, "Submitted Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
    return render(request,'user/user-feedback.html')


def user_hospital_beds(request):
    beds= BedModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        beds=BedModel.objects.filter(Q(Bed_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(category__icontains=search) )
    return render(request,'user/user-hospital-beds.html',{'b': beds})

def user_ventilators(request):
    ventilators= VentilatorModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        ventilators=VentilatorModel.objects.filter(Q(Ventilator_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(ventilator_company__icontains=search) | Q(category__icontains=search))
    return render(request,'user/user-ventilators.html',{'v':ventilators})

def user_oxy_cylinders(request):
    cylinders= CylinderModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        cylinders=CylinderModel.objects.filter(Q(cylinder_id__icontains=search) | Q(company_name__icontains=search) | Q(distributor_name__icontains=search) | Q(location__icontains=search) | Q(category__icontains=search))
    return render(request,'user/user-oxy-cylinders.html',{'c':cylinders})



