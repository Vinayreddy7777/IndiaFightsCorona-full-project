function ventilatorvalidation(){
    var hospital_name= document.myform.hospitalname
    var ventilator_company= document.myform.ventilatorcompany
    var location= document.myform.location
    var mobile= document.myform.mobile
    var category= document.myform.category
    var ventilators_available= document.myform.ventilatorsavailable
    var cost= document.myform.cost
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;
    
    if (hospital_name.value=='' || hospital_name.value.length <6){
        alert("Hospital name cannot be blank and should be more than 6 alphabets")
        hospital_name.focus();
        return false;
    } 
    if (ventilator_company.value=='' || ventilator_company.value.length <5){
        alert("Ventilator Company cannot be blank and should be more than 5 alphabets")
        ventilator_company.focus();
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
    if (category.value=='Select Ventilator'){
        alert("Select One type of Ventilator")
        category.focus();
        return false;
    } 
    if (ventilators_available.value==''){
        alert("please enter number of available ventilators and it should be a number")
        ventilators_available.focus();
        return false;
    }
    if (cost.value==''){
        alert("please enter cost and it should be a number")
        cost.focus();
        return false;
    }
    return true;
    }