function feedbackvalidation(){
    var category= document.myform.category
    var name= document.myform.name
    var mobile= document.myform.mobile
    // var email= document.myform.email 
    // var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    var feedback=document.myform.feedback
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;


    if (category.value=='Select Category'){
        alert("Select Category")
        category.focus();
        return false;
    } 
    if (name.value=='' || name.value.length <6){
        alert("Name cannot be blank and should be more than 6 alphabets")
        name.focus();
        return false;
    } 
    if (mobile.value=='' || mobile.value.length !=10 ){
        alert("mobile number should be 10 digits and it should be a number")
        mobile.focus();
        return false;
    }
    // if(!email.value.match(mailformat)){
    //     alert("invalid email")
    //     email.focus();
    //     return false;
    // }
    if(feedback.value==''){
        alert("Please Give your Feedback")
        mobile.focus();
        return false;
    }
    return true;
    }