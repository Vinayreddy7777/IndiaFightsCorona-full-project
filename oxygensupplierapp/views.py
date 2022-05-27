from struct import pack
from django.shortcuts import render, redirect, get_object_or_404
from oxygensupplierapp.models import O2supplierRegistrationModel, CylinderModel

#importing resources for messages.
from django.contrib import messages

#Oxygensupplier Login Backend Start.
def oxygensupplier_login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")       
        try:
            check=O2supplierRegistrationModel.objects.get(email=email,password=password)
            request.session["supp_id"]=check.supp_id
            status=check.status
            if status=="Accepted":
                messages.success(request,'Login Successful')
                return redirect('oxygensupplier_dashboard')
            elif status=="Rejected":
                messages.error(request,'Your Request has been Rejected, So you cannot Login')  
            elif status=="pending":
                messages.info(request,'Your Status is Pending, You Cannot Login Now')  
        except:
            messages.warning(request,'Invalid Login')  
                
    return render(request,'oxygensuppliers/oxygensuppliers-login.html')
#Oxygensupplier Login Backend End.

#Oxygensupplier Registration Backend Start.
def oxygensupplier_registration(request):
    if request.method == "POST":
        supp_name = request.POST.get('suppliername')
        mobile = request.POST.get('mobile')
        alternate_mobile = request.POST.get('alternatemobile')
        email = request.POST.get('email')
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
        
        if O2supplierRegistrationModel.objects.filter(email=email).exists():
            messages.error (request, "Email already exist")   
                 
        else:
            User=O2supplierRegistrationModel.objects.create(supp_name=supp_name,mobile=mobile,alternate_mobile=alternate_mobile,email=email,password=password)
            User.save()
            messages.success(request, "Account created successful")


        # messages.error(request, "Error. Message not sent.")

    return render(request,'oxygensuppliers/oxygensuppliers-registration.html')
#Oxygensupplier Registration Backend End.



def oxygensupplier_dashboard(request):
    a=CylinderModel.objects.filter(category='Small').count()
    b=CylinderModel.objects.filter(category='Medium').count()
    c=CylinderModel.objects.filter(category='Large').count()
    return render(request,'oxygensuppliers/oxygensuppliers-dashboard.html',{'a':a,'b':b,'c':c})

def oxygensupplier_add_o2cylinder(request):
    if request.method == "POST":
        
        company_name = request.POST.get('companyname')
        distributor_name = request.POST.get('distributorname')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        category = request.POST.get('category')
        packages = request.POST.get('packages')
        cost = request.POST.get('cost')
        details = request.POST.get('details')
        
        
        user=CylinderModel.objects.create(company_name=company_name,distributor_name=distributor_name,location=location,mobile=mobile,category=category,packages=packages,cost=cost,details=details)
        user.save()
        
        if user:    
            messages.success(request, "Cylinder Added Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")
            
    return render(request,'oxygensuppliers/oxygensuppliers-add-oxygen-cylinder-details.html')

def oxygensupplier_view_o2cylinder(request):
    cylinder= CylinderModel.objects.all()
    return render(request,'oxygensuppliers/oxygensuppliers-view-oxygen-cylinder-details.html',{'d':cylinder})

def oxygensupplier_edit_o2cylinder(request, id):
    edit=CylinderModel.objects.filter(cylinder_id=id) 
    obj = get_object_or_404(CylinderModel,cylinder_id=id)
    if request.method =="POST":
        company_name = request.POST.get('companyname')
        distributor_name = request.POST.get('distributorname')
        location = request.POST.get('location')
        mobile = request.POST.get('mobile')
        category = request.POST.get('category')
        packages = request.POST.get('packages')
        cost = request.POST.get('cost')
        details = request.POST.get('details') 

        obj.company_name=company_name
        obj.distributor_name=distributor_name
        obj.location=location
        obj.mobile=mobile
        obj.category=category
        obj.packages=packages
        obj.cost=cost
        obj.details=details
        
        # obj.save(update_fields=["company_name,distributor_name,location,mobile,category,packages,cost,details"])
        obj.save()
        
        if obj:    
            messages.success(request, "Cylinder Updated Successfully")
        else:
            messages.error(request, "Something Wrong, Please try again.")

    return render(request,'oxygensuppliers/oxygensuppliers-edit-oxygen-cylinder-details.html',{'e':edit})


def delete_o2cylinder(request,id):
    c = CylinderModel.objects.filter(cylinder_id=id)
    c.delete()
    return redirect('oxygensupplier_view_o2cylinder')



