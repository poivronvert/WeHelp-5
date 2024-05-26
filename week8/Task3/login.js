let passwordInput = document.getElementById('passwordInput').value;
let regex = /^(?=.*[A-Za-z])(?=.*\\d)(?=.*[@#$%])[A-Za-z\\d@#$%]{4,8}$/;
let alertMsg='密碼必須包含4到8個字符，並且只能包含英文字母、數字和以下特殊字符之一：@#$%'

document.getElementById('submit').addEventListener('click', function() {
    if (!regex.test(passwordInput)) {
        alert(alertMsg);
    }
});