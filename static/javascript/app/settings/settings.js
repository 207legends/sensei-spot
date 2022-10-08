let input_name = document.getElementById("settings-user-name");
let input_username = document.getElementById("settings-user-username");
let input_email = document.getElementById("settings-user-email");
let input_dob = document.getElementById("settings-user-dob");
let input_pincode = document.getElementById("settings-user-pincode");
let select_country = document.getElementById("settings-user-country");
let select_state = document.getElementById("settings-user-state");
let select_city = document.getElementById("settings-user-city");
let input_address1 = document.getElementById("settings-user-address1");
let input_address2 = document.getElementById("settings-user-address2");
let input_address3 = document.getElementById("settings-user-address3");
let input_landmark = document.getElementById("settings-user-landmark");

let progress_spinner = document.getElementById("progress-spinner");

function checkEmailFormat() {
    let value = input_email.value;
    let pattern = CONSTANTS.REGEX.EMAIL;

    let message = "";

    if (pattern.test(value) == false) {
        message = `<span>Email is not in correct format</span>`;
    }

    setFeedback(FEEDBACKS.EMAIL, message);
}

function submitData() {
    let isFormValid = checkForm();

    if (!isFormValid) {
        return;
    }

    setProgressState(STATE.SHOW);

    let createDataToPush = function () {
        let data = {                        
            name: "",
            username: "",
            email : "",
            dob: "",
            pincode: "",
            country: "",
            state: "",
            city: "",
            address1: "",
            address2: "",
            address3: "",
            landmark: ""
        }

        pushData(data);
    };

    let pushData = function (data) {
        $.ajax(
            {
                url: "/user/settings",
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
