function myfunction() {
    var inpobj = document.getElementById('id1');

    if (!inpobj.checkValidity()) {
        document.getElementById("id2").innerHTML = inpobj.validationMessage;
    } else {
        document.getElementById("id2").innerHTML = "Input is ok";
    }
}
