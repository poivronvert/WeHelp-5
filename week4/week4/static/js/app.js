function check() {
    if (document.getElementById("consent").checked) {
        return true;
    }else{
        alert("Please check the checkbox first");
        return false;
    }
}