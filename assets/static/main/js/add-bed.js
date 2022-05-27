function bedvalidation(){
    var hospital_name= document.myform.hospitalname
    var location= document.myform.location
    var mobile= document.myform.mobile
    var category= document.myform.category
    var beds_available= document.myform.bedsavailable
    var cost= document.myform.cost
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;
    
    if (hospital_name.value=='' || hospital_name.value.length <6){
        alert("Hospital name cannot be blank and should be more than 6 alphabets")
        hospital_name.focus();
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
    if (category.value=='Select Bed'){
        alert("Select One type of Bed")
        category.focus();
        return false;
    } 
    if (beds_available.value==''){
        alert("please enter number of available beds and it should be a number")
        beds_available.focus();
        return false;
    }
    if (cost.value==''){
        alert("please enter cost and it should be a number")
        cost.focus();
        return false;
    }
    return true;
    }