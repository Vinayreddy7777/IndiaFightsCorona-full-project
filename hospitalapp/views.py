from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from hospitalapp.models import HospitalRegistrationModel, BedModel, VentilatorModel

#importing resources for messages.
from django.contrib import messages

#importing resources for search in search box.
from django.db.models import Q



#Hospital Login Backend Start.
def hospital_login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password") 
        try:  
            check=HospitalRegistrationModel.objects.get(email=email,password=password)  
            request.session["hospital"]=check.hospital_id
            status=check.status
            if status=="Accepted":
                messages.success(request,'Login Successful')
                return redirect('hospital_dashboard')
            elif status=="Rejected":
                messages.error(request,'Your Request has been Rejected, So you cannot Login')  
            elif status=="pending":
                messages.info(request,'Your Status is Pending, You Cannot Login Now')  
        except:
            messages.warning(request,'Invalid Login')  

    return render(request,'hospital/hospital-login.html')
#Hospital Login Backend End.


#Hospital Registration Backend Start.
def hospital_registration(request):
    if request.method == "POST":
        hospital_name = request.POST.get('hospitalname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        location = request.POST.get('location')
        hospital_address = request.POST.get('hospitaladdress')
        password = request.POST.get('password')
        
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
        
        if HospitalRegistrationModel.objects.filter(email=email).exists():
            messages.error(request, "Email already exist")   
                 
        else:
            User=HospitalRegistrationModel.objects.create(hospital_name=hospital_name,mobile=mobile,email=email,location=location,hospital_address=hospital_address,password=password)
            User.save()
            messages.success(request, "Account created successful")


        # messages.error(request, "Error. Message not sent.")
        
        
        
    return render(request,'hospital/hospital-registration.html')
#Hospital Registration Backend End.

def hospital_dashboard(request):
    if 'hospital' in request.session:
        # current_user = request.session['hospital']
        print(request.session["hospital"])
        Hospital_beds=BedModel.objects.count()
        Ventilators=VentilatorModel.objects.count()
        Hospitals=HospitalRegistrationModel.objects.count()
        return render(request,'hospital/hospital-dashboard.html',{'Hospital_beds':Hospital_beds,'Ventilators':Ventilators,'Hospitals':Hospitals})
    else:
        return redirect('hospital_login')
    
    return render(request,'hospital/hospital-dashboard.html',{'Hospital_beds':Hospital_beds,'Ventilators':Ventilators,'Hospitals':Hospitals})

#Hospital Add Bed Backend Start.
def hospital_add_bed(request):
    if request.method == "POST":
        hospital_id = request.session["hospital"]
        hospital_name = request.POST.get('hospitalname')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        category = request.POST.get('category')
        beds_available = request.POST.get('bedsavailable')
        cost = request.POST.get('cost')
        details = request.POST.get('details')
        
        user=BedModel.objects.create(hospital_id=hospital_id,hospital_name=hospital_name,location=location,mobile=mobile,category=category,beds_available=beds_available,cost=cost,details=details)
        user.save()
        if user:    
            messages.success(request, "Bed Updated Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
    return render(request,'hospital/hospital-add-bed-details.html')
#Hospital Add Bed Backend End.


#Hospital View Beds Backend Start.
def hospital_view_beds(request):
    hosp_id = request.session["hospital"]
    beds= BedModel.objects.filter(hospital_id=hosp_id)
    
    if request.method=="POST":
        search=request.POST.get("search")
        beds=BedModel.objects.filter(Q(Bed_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(category__icontains=search) )
    return render(request,'hospital/hospital-view-bed-details.html',{'b':beds})
#Hospital View Beds Backend End.

    
#Hospital Edit Bed Backend Start.
def hospital_edit_bed(request,id):
    edit=BedModel.objects.filter(Bed_id=id) 
    obj = get_object_or_404(BedModel,Bed_id=id)
    if request.method =="POST":
        hospital_name = request.POST.get('hospitalname')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        category = request.POST.get('category')
        beds_available = request.POST.get('bedsavailable')
        cost = request.POST.get('cost')
        details = request.POST.get('details') 

        obj.hospital_name=hospital_name
        obj.location=location
        obj.mobile=mobile
        obj.category=category
        obj.beds_available=beds_available
        obj.cost=cost
        obj.details=details
        
        obj.save()
        
        if obj:    
            messages.success(request, "Bed Updated Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
            
    return render(request,'hospital/hospital-edit-bed-details.html',{'e':edit})
#Hospital Edit Bed Backend End.

#Hospital Delete Bed Backend Start.
def delete_bed(request,id):
    c = BedModel.objects.filter(Bed_id=id)
    c.delete()
    return redirect('hospital_view_beds')
#Hospital Delete Bed Backend End.



#Hospital Add Ventilator Backend Start.
def hospital_add_ventilator(request):
    if request.method == "POST": 
        hospital_name = request.POST.get('hospitalname')
        ventilator_company = request.POST.get('ventilatorcompany')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        category = request.POST.get('category')
        ventilators_available = request.POST.get('ventilatorsavailable')
        cost = request.POST.get('cost')
        details = request.POST.get('details')
        VentilatorModel.objects.create(hospital_name=hospital_name,ventilator_company=ventilator_company,location=location,mobile=mobile,category=category,ventilators_available=ventilators_available,cost=cost,details=details)
    return render(request,'hospital/hospital-add-ventilators.html')
#Hospital Add Ventilator Backend End.


#Hospital View Ventilators Backend Start.
def hospital_view_ventilators(request):
    ventilators= VentilatorModel.objects.all()
    
    if request.method=="POST":
        search=request.POST.get("search")
        ventilators=VentilatorModel.objects.filter(Q(Ventilator_id__icontains=search) | Q(hospital_name__icontains=search) | Q(location__icontains=search) | Q(ventilator_company__icontains=search) | Q(category__icontains=search))
    return render(request,'hospital/hospital-view-ventilators.html',{'v':ventilators})
#Hospital View Ventilators Backend End.


#Hospital Edit Ventilator Backend Start.
def hospital_edit_ventilator(request,id):
    edit=VentilatorModel.objects.filter(Ventilator_id=id) 
    obj = get_object_or_404(VentilatorModel,Ventilator_id=id)
    if request.method =="POST":
        hospital_name = request.POST.get('hospitalname')
        ventilator_company = request.POST.get('ventilatorcompany')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        category = request.POST.get('category')
        ventilators_available = request.POST.get('ventilators_available')
        cost = request.POST.get('cost')
        details = request.POST.get('details') 

        obj.hospital_name=hospital_name
        obj.ventilator_company=ventilator_company
        obj.location=location
        obj.mobile=mobile
        obj.category=category
        obj.ventilators_available=ventilators_available
        obj.cost=cost
        obj.details=details
        
        obj.save()
        
        if obj:    
            messages.success(request, "Ventilator Updated Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
            
    return render(request,'hospital/hospital-edit-ventilators.html',{'e':edit})
#Hospital Edit Ventilator Backend End.

#Hospital Delete Ventilator Backend Start.
def delete_ventilator(request,id):
    c = VentilatorModel.objects.filter(Ventilator_id=id)
    c.delete()
    return redirect('hospital_view_ventilators')
#Hospital Delete Ventilator Backend End.

def hospital_logout(request):
    try:       
        del request.session['hospital']
    except:       
        return redirect('hospital_login')
    
    return render(request, 'main/main-index.html')



