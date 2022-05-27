function rationvalidation(){
    var name= document.myform.name
    var mobile= document.myform.mobile
    var alternate_mobile= document.myform.alternatemobile
    var email= document.myform.email 
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    var location= document.myform.location
    var category= document.myform.whoareyou
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;
    
    if (name.value=='' || name.value.length <6){
        alert("Name cannot be blank and should be more than 6 alphabets")
        name.focus();
        return false;
    } 
    if (mobile.value=='' || mobile.value.length !=10 ){
        alert("mobile number should be 10 digits and it should be a number")
        mobile.focus();
        return false;
    }if (alternate_mobile.value=='' || alternate_mobile.value.length !=10 ){
        alert("alternate mobile number should be 10 digits and it should be a number")
        alternate_mobile.focus();
        return false;
    }
    if(!email.value.match(mailformat)){
        alert("invalid email")
        email.focus();
        return false;
    }
    if (location.value==''){
        alert("location should not be empty")
        location.focus();
        return false;
    }   
    
    if (category.value=='Select Who are You'){
        alert("Select Who are You")
        category.focus();
        return false;
    } 
    return true;
    }