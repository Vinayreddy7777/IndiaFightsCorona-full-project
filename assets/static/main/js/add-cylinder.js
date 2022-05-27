function cylindervalidation(){
    var company_name= document.myform.companyname
    var distributor_name= document.myform.distributorname
    var location= document.myform.location
    var mobile= document.myform.mobile
    var category= document.myform.category
    var packages= document.myform.packages
    var cost= document.myform.cost
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;
    
    if (company_name.value=='' || company_name.value.length <6){
        alert("Company name cannot be blank and should be more than 6 alphabets")
        company_name.focus();
        return false;
    } 
    if (distributor_name.value=='' || distributor_name.value.length <6){
        alert("distributor name cannot be blank and should be full name")
        distributor_name.focus();
        return false;
    } 
    if (location.value==''){
        alert("location should not be empty")
        location.focus();
        return false;
    }   
    if (mobile.value=='' || mobile.value.length !=10 ){
        alert("mobile number should be 10 digits and it should be a number")
        mobile.focus();
        return false;
    }
    if (category.value=='Select Cylinder'){
        alert("Select One type of Cylinder")
        category.focus();
        return false;
    } 
    if (packages.value==''){
        alert("please enter number of packages available  and it should be a number")
        packages.focus();
        return false;
    }
    if (cost.value==''){
        alert("please enter cost and it should be a number")
        cost.focus();
        return false;
    }
    return true;
    }