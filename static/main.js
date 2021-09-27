$(function () {
    let passwordInputButton1 = $("#password1")
    let signupPasswordInput1 = document.querySelector('input[type="password"]#id_password1')
    let eyeButton1 = $("#eye_password1")
    eyeButton1.addClass('fa-eye')
    passwordInputButton1.click(function () {
        if (signupPasswordInput1.type === "password") {
            signupPasswordInput1.type = "text"
            eyeButton1.removeClass('fa-eye')
            eyeButton1.addClass('fa-eye-slash')
        } else {
            signupPasswordInput1.type = "password"
            eyeButton1.addClass('fa-eye')
            eyeButton1.removeClass('fa-eye-slash')
        }
    });

    let eyeButton2 = $("#eye_password2")
    eyeButton2.addClass('fa-eye')
    let passwordInputButton2 = $("#password2");
    let signupPasswordInput2 = document.querySelector('input[type="password"]#id_password2')
    passwordInputButton2.click(function () {
        if (signupPasswordInput2.type === "password") {
            signupPasswordInput2.type = "text"
            eyeButton2.removeClass('fa-eye')
            eyeButton2.addClass('fa-eye-slash')
        } else {
            signupPasswordInput2.type = "password"
            eyeButton2.addClass('fa-eye')
            eyeButton2.removeClass('fa-eye-slash')
        }
    });

    let eyeButton = $("#eye_password")
    eyeButton.addClass('fa-eye')
    let passwordInputButton = $("#password");
    let signupPasswordInput = document.querySelector('input[type="password"]#id_password')
    passwordInputButton.click(function () {
        if (signupPasswordInput.type === "password") {
            signupPasswordInput.type = "text"
            eyeButton.removeClass('fa-eye')
            eyeButton.addClass('fa-eye-slash')
        } else {
            signupPasswordInput.type = "password"
            eyeButton.addClass('fa-eye')
            eyeButton.removeClass('fa-eye-slash')
        }
    });
});