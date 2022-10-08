let input_email = document.getElementById("signup-user-email");
let input_pwd1 = document.getElementById("signup-user-password1");
let input_pwd2 = document.getElementById("signup-user-password2");
let select_role = document.getElementById("signup-user-role");
let checkbox_agree = document.getElementById("signup-user-agree")

let progress_spinner = document.getElementById("progress-spinner");
const STATE = {
    SHOW: true,
    HIDE: false
}

const FEEDBACKS = {
    EMAIL: "fb-email",
    PASSWORD1: "fb-password1",
    PASSWORD2: "fb-password2",
    TERMS: "fb-terms"
}

function checkEmailFormat() {
    let value = input_email.value;
    let pattern = CONSTANTS.REGEX.EMAIL;

    let message = "";

    if (pattern.test(value) == false) {
        message = `<span>Email is not in correct format</span>`;
    }

    setFeedback(FEEDBACKS.EMAIL, message);

}

function checkPasswordFormat() {
    let value = input_pwd1.value;
    let pattern = CONSTANTS.REGEX.PASSWORD;
    let message = "";

    if (pattern.test(value) == false) {
        message = `
            Password must contain 
            <ul>
                <li>1 capital alphabet</li>
                <li>1 small albhabet</li>
                <li>1 numeric digit</li>
                <li>8 or more characters</li>
            </ul>
            `;
    }

    setFeedback(FEEDBACKS.PASSWORD1, message);
}

function checkConfirmPassword() {
    let value1 = input_pwd1.value;
    let value2 = input_pwd2.value;
    let message = ""

    if (value1 != value2) {
        message = `
            <span>Password is not same</span>
            `;
    }

    setFeedback(FEEDBACKS.PASSWORD2, message);
}

function submitData() {
    let isFormValid = checkForm();

    if (!isFormValid) {
        return;
    }

    setProgressState(STATE.SHOW);

    let createDataToPush = function () {
        let data = {
            email: input_email.value,
            password: input_pwd1.value,
            role: select_role.value
        }

        pushData(data);
    };

    let pushData = function (data) {
        $.ajax(
            {
                url: "/user/signup",
                type: "POST",
                data: JSON.stringify(data),
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                success: (response) => {
                    console.log(response);
                    setProgressState(STATE.HIDE);
                    if (response.status == 200) {
                        window.location = "/user/login";
                    }
                    else if (response.status == 401) {
                        document.getElementById("error-message").innerHTML = response.message;
                        document.getElementById("error-dialog").style.display = "block";
                    }

                },
                error: (error) => {
                    setProgressState(STATE.HIDE);
                }
            }
        )
    }

    createDataToPush();
}

function checkForm() {
    let value_email = input_email.value;
    let value_password1 = input_pwd1.value;
    let value_password2 = input_pwd2.value;
    let message = "";

    if (value_email == "") {
        message = "Field is empty";
        setFeedback(FEEDBACKS.EMAIL, message);
        return false;
    }
    if (CONSTANTS.REGEX.EMAIL.test(value_email) == false) {
        message = `<span>Email is not in correct format</span>`;
        setFeedback(FEEDBACKS.EMAIL, message);
        return false;
    }

    if (value_password1 == "") {
        message = "Field is empty";
        setFeedback(FEEDBACKS.PASSWORD1, message);
        return false;
    }
    if (CONSTANTS.REGEX.PASSWORD.test(value_password1) == false) {
        message = `
            Password must contain 
            <ul>
                <li>1 capital alphabet</li>
                <li>1 small albhabet</li>
                <li>1 numeric digit</li>
                <li>8 or more characters</li>
            </ul>
            `;
        setFeedback(FEEDBACKS.PASSWORD1, message);
        return false;
    }

    if (value_password2 == "") {
        message = "Field is empty";
        setFeedback(FEEDBACKS.PASSWORD2, message);
        return false;
    }
    if (value_password1 != value_password2) {
        message = `
            <span>Password is not same</span>
            `;
        setFeedback(FEEDBACKS.PASSWORD2, message);
        return false;
    }

    if (checkbox_agree.checked == false) {
        message = `Terms and conditions not agreed`;
        setFeedback(FEEDBACKS.TERMS, message);
        return false;
    }

    return true;
}

function setFeedback(id, message) {
    document.getElementById(id).innerHTML = message;
}

function setProgressState(state) {
    if (STATE.SHOW)
        progress_spinner.style.display = 'inline-block';
    else (STATE.HIDE)
    progress_spinner.style.display = 'none';
}