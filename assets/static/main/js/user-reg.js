function validation(){
    var username= document.myform.username
    var mobile= document.myform.mobile
    var email= document.myform.email 
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    var location= document.myform.location
    var pin= document.myform.pin
    var password=document.myform.password
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;
    var image=document.myform.photo
    
    if (username.value=='' || username.value.length <6){
        alert(" username should be more than 6 alphabets")
        username.focus();
        return false;
    }    
    if (mobile.value=='' || mobile.value.length !=10 ){
        alert("mobile number should be 10 digits")
        mobile.focus();
        return false;
    }
    if(!email.value.match(mailformat)){
        alert("invalid email")
        email.focus();
        return false;
    }
    if (location.value==''){
        alert("location should not be empty")
        user_name.focus();
        return false;
    }
    if (pin.value=='' || pin.value.length !=6 ){
        alert("pincode should be 6 digits")
        pin.focus();
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
    if (image.value.length==''){
        alert("please upload your profile image");
        return false;
    }
    return true;
    }