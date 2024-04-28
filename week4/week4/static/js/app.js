function check() {
    if (document.getElementById("consent").checked) {
        return true;
    }else{
        alert("Please check the checkbox first");
        return false;
    }
}

function calc() {
    let input = parseFloat(document.getElementById("number_input").value);
    if (input>0) {
        window.location.href = `/square/${input}`;
        return false;
    }else{
        alert("Please enter a positive number");
        return false;
    }
}