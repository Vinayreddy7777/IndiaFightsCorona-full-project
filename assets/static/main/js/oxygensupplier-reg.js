function validation(){
    var suppliername= document.myform.suppliername
    var mobile= document.myform.mobile
    var alternatemobile= document.myform.alternatemobile
    var email= document.myform.email 
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    var password=document.myform.password
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;
    
    if (suppliername.value=='' || suppliername.value.length <6){
        alert(" supplier name should be more than 6 alphabets")
        username.focus();
        return false;
    }    
    if (mobile.value=='' || mobile.value.length !=10 ){
        alert("mobile number should be 10 digits")
        mobile.focus();
        return false;
    }
    if (alternatemobile.value=='' || alternatemobile.value.length !=10 ){
        alert("mobile number should be 10 digits")
        alternatemobile.focus();
        return false;
    }
    if(!email.value.match(mailformat)){
        alert("invalid email")
        email.focus();
        return false;
    }
    if (password.value==''){
        alert("password should not be empty")
        password.focus();
        return false;
    }
    if (!letter.test(password.value)) {
        alert("Please make sure password includes a lowercase letter.")
           return false;
        }
    if (!number.test(password.value)) {
        alert("Please make sure Password Includes a Digit")
           return false;
        }
    if (!upper.test(password.value)) {
        alert("Please make sure password includes an uppercase letter.");
           return false;
        }
    return true;
    }