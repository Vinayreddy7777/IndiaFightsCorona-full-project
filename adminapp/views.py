from turtle import color
from django.shortcuts import render,redirect,get_object_or_404
from hospitalapp.models import BedModel, HospitalRegistrationModel, VentilatorModel
from mainapp.models import ContactModel
from userapp.models import PlasmaDonorsModel, RationDonorsModel, UserRegistrationModel, UsersFeedbackModel, UserRequestModel
from oxygensupplierapp.models import O2supplierRegistrationModel, CylinderModel
#importing for email
from django.core.mail import EmailMultiAlternatives
from IndiaFightsCorona.settings import DEFAULT_FROM_EMAIL

#importing resources for messages.
from django.contrib import messages

#importing resources for search in search box.
from django.db.models import Q

#Admin Login Backend Start.
def admin_login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')         
               
        if name =='admin' and password =='admin':     
            messages.success(request,'Login Successfull')
            return redirect('admin_dashboard')
        else:        
            messages.error(request, "Invalid Login") 
    return render(request,'admin/admin-login.html')
#Admin Login Backend end.



def admin_dashboard(request):
    Hospitals=HospitalRegistrationModel.objects.count()
    O2suppliers=O2supplierRegistrationModel.objects.count()
    Users=UserRegistrationModel.objects.count()
    Hospital_beds=BedModel.objects.count()
    O2cylinders=CylinderModel.objects.count()
    Ventilators=VentilatorModel.objects.count()
    
    return render(request,'admin/admin-dashboard.html',{'Hospitals':Hospitals,'O2suppliers':O2suppliers,'Users':Users,'Hospital_beds':Hospital_beds,'O2cylinders':O2cylinders,'Ventilators':Ventilators})

def admin_view_hospitals(request):
    hospitals = HospitalRegistrationModel.objects.all()
    
    if request.method=="POST":
        search=request.POST.get("search")
        hospitals=HospitalRegistrationModel.objects.filter(Q(hospital_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(status__icontains=search) )
        
    return render(request,'admin/admin-view-hospitals.html',{'h': hospitals})


#Admin View Hospitals Update Backend Start.  
def accept_hospitals(request,id):
    accept=get_object_or_404(HospitalRegistrationModel,hospital_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    
    
    #email code
    html_content = "<br/><p>Hello<strong>"+' '+str(accept.hospital_name) +"</strong>We are from IndiaFightsCorona Services, Your Registration has been successfully <strong>Accepted</strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Connection Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent Successfully")
    return redirect('admin_view_hospitals')

def reject_hospitals(request,id):
    reject=get_object_or_404(HospitalRegistrationModel,hospital_id=id)
    reject.status='Rejected'
    reject.save(update_fields=['status'])
    reject.save()
    
    #email code
    html_content = "<br/><p>Hello<strong>"+' '+str(reject.hospital_name) +"</strong>We are from IndiaFightsCorona Services, Your Registration has been successfully <strong>Rejected</strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [reject.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Connection Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent Successfully")
    return redirect('admin_view_hospitals')
#Admin  View Hospitals Update Backend End.
    
def admin_view_hospital_beds(request):
    beds= BedModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        beds=BedModel.objects.filter(Q(Bed_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(category__icontains=search) )
    return render(request,'admin/admin-view-hospital-beds.html',{'b': beds})

def admin_view_ventilators(request):
    ventilators= VentilatorModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        ventilators=VentilatorModel.objects.filter(Q(Ventilator_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(ventilator_company__icontains=search) | Q(category__icontains=search))
    return render(request,'admin/admin-view-hospital-ventilators.html',{'v':ventilators})

def admin_view_plasma(request):
    plasma= PlasmaDonorsModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        plasma=PlasmaDonorsModel.objects.filter(Q(plasma_donor_id__icontains=search) | Q(plasma_donor_name__icontains=search) | Q(location__icontains=search) | Q(blood_group__icontains=search) | Q(date__icontains=search))

    return render(request,'admin/admin-view-hospital-plasma.html',{'p': plasma})

# def admin_users_request_plasma(request):
#     request_plasma= UserRegistrationModel.objects.all()
#     return render(request,'admin/admin-users-request-plasma.html',{'p': request_plasma})

def admin_view_ration(request):
    ration= RationDonorsModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        ration=RationDonorsModel.objects.filter(Q(ration_donor_id__icontains=search) | Q(ration_donor_name__icontains=search) | Q(location__icontains=search) | Q(who_you_are__icontains=search)| Q(date__icontains=search) )
    return render(request,'admin/admin-view-hospital-ration.html',{'r': ration})

# def admin_users_request_ration(request):
#     request_ration= UserRegistrationModel.objects.all()
#     return render(request,'admin/admin-users-request-ration.html',{'r': request_ration})

def admin_view_o2_suppliers(request):
    suppliers= O2supplierRegistrationModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        suppliers=O2supplierRegistrationModel.objects.filter(Q(supp_id__icontains=search) | Q(supp_name__icontains=search) | Q(status__icontains=search) )
    return render(request,'admin/admin-view-oxygen-suppliers.html',{'s': suppliers})

#Admin View O2supplier Update Backend Start. 
def accept_o2supplier(request,id):
    accept=get_object_or_404(O2supplierRegistrationModel,supp_id=id)
    accept.status='Accepted'
    accept.save(update_fields=['status'])
    accept.save()
    
    #email code
    html_content = "<br/><p>Hello<strong>"+' '+str(accept.supp_name) +"</strong>We are from IndiaFightsCorona Services, Your Registration has been successfully <strong>Accepted</strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Connection Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent Successfully")
    return redirect('admin_view_o2_suppliers')

def reject_o2supplier(request,id):
    reject=get_object_or_404(O2supplierRegistrationModel,supp_id=id)
    reject.status='Rejected'
    reject.save(update_fields=['status'])
    reject.save()
    
    #email code
    html_content = "<br/><p>Hello<strong>"+' '+str(reject.supp_name) +"</strong>We are from IndiaFightsCorona Services, Your Registration has been successfully <strong>Rejectted</strong></p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [reject.email]
    # if send_mail(subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("Connection Status", html_content, from_mail, to_mail)
    msg.attach_alternative(html_content, "text/html")
    if msg.send():
        print("Sent Successfully")
    return redirect('admin_view_o2_suppliers')
#Admin View O2supplier Update Backend Start. 

def admin_view_o2_cylinders(request):
    cylinders= CylinderModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        cylinders=CylinderModel.objects.filter(Q(cylinder_id__icontains=search) | Q(company_name__icontains=search) | Q(distributor_name__icontains=search) | Q(location__icontains=search)| Q(category__icontains=search)| Q(date__icontains=search) )
    return render(request,'admin/admin-view-oxygen-cylinders.html',{'c': cylinders})

def admin_view_users(request):
    users= UserRegistrationModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        users=UserRegistrationModel.objects.filter(Q(user_id__icontains=search) | Q(username__icontains=search) | Q(location__icontains=search) | Q(pin__icontains=search) )
    return render(request,'admin/admin-view-users.html',{'u': users})

def admin_view_help_requests(request):
    help_request= UserRequestModel.objects.all()
    a=UserRequestModel.objects.filter(requesting_for='Plasma').count()
    b=UserRequestModel.objects.filter(requesting_for='Ration').count()
    if request.method=="POST":
        search=request.POST.get("search")
        help_request=UserRequestModel.objects.filter(Q(request_id__icontains=search) | Q(name__icontains=search) | Q(location__icontains=search) | Q(pin__icontains=search)| Q(requesting_for__icontains=search)| Q(date_time__icontains=search) )
    return render(request,'admin/admin-view-help-details.html',{'r': help_request,'a':a,'b':b})

def admin_view_feedback(request):
    feedback= UsersFeedbackModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        feedback=UsersFeedbackModel.objects.filter(Q(hospital_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(status__icontains=search) )
    return render(request,'admin/admin-view-feedback.html',{'d':feedback})


def admin_contact_us(request): 
    contact_us= ContactModel.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        contact_us=ContactModel.objects.filter(Q(user_id__icontains=search) | Q(name__icontains=search) | Q(subject__icontains=search))       
    return render(request,'admin/admin-contact-us.html',{'c':contact_us})


