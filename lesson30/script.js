function validateform(){
    var x = document.forms["myform"]["firstname"].value;
    if(x == ""){
        alert("Name is blank, please enter the name");
        return false;
    }
}
