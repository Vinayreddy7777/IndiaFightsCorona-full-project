from django.shortcuts import render, redirect
from hospitalapp.models import BedModel, VentilatorModel
from mainapp.models import ContactModel
from oxygensupplierapp.models import CylinderModel
from userapp.models import PlasmaDonorsModel, UsersFeedbackModel

#importing resources for messages.
from django.contrib import messages

#importing resources for search in search box.
from django.db.models import Q


def main_home(request):
    feedback= UsersFeedbackModel.objects.all()
    if request.method=="POST":
        return redirect('main_contact')
    return render(request,'main/main-index.html',{'f':feedback})

def main_about(request):
    if request.method=="POST":
        return redirect('main_contact')
    return render(request,'main/main-about.html')

def main_hospital_beds(request):
    beds= BedModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        beds=BedModel.objects.filter(Q(Bed_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(category__icontains=search) )
    return render(request,'main/main-hospital-beds.html',{'b': beds})

def main_ventilators(request):
    ventilators= VentilatorModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        ventilators=VentilatorModel.objects.filter(Q(Ventilator_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(ventilator_company__icontains=search) | Q(category__icontains=search))
    return render(request,'main/main-ventilators.html',{'v':ventilators})

def main_oxygen_cylinders(request):
    cylinders= CylinderModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        cylinders=CylinderModel.objects.filter(Q(cylinder_id__icontains=search) | Q(company_name__icontains=search) | Q(distributor_name__icontains=search) | Q(location__icontains=search) | Q(category__icontains=search))
    return render(request,'main/main-oxygen-cylinders.html',{'c':cylinders})

def main_plasma(request):
    plasma= PlasmaDonorsModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        plasma=PlasmaDonorsModel.objects.filter(Q(plasma_donor_id__icontains=search) | Q(plasma_donor_name__icontains=search) | Q(location__icontains=search) | Q(blood_group__icontains=search))
    return render(request,'main/main-plasma.html',{'p':plasma})

def main_ration_help(request):
    feedback= UsersFeedbackModel.objects.all()
    if request.method=="POST":
        return redirect('user_login')
    return render(request,'main/main-ration-help.html',{'f':feedback})

def main_contact(request):
    if request.method == "POST":
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')      
      
        user=ContactModel.objects.create(name=name,email=email,subject=subject,message=message)
        user.save()
        
        if user:    
            messages.success(request, "Sent Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
        
    return render(request,'main/main-contact.html')

def main_booking(request):
    return render(request,'main/booking.html')
