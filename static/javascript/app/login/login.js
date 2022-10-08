let input_email = document.getElementById("login-user-email");
    let input_pwd1 = document.getElementById("login-user-password1");

    let progress_spinner = document.getElementById("progress-spinner");

    const STATE = {
        SHOW: true,
        HIDE: false
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
            }

            pushData(data);
        };

        let pushData = function (data) {
            $.ajax(
                {
                    url: "/user/login",
                    type: "POST",
                    data: JSON.stringify(data),
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    success: (response) => {
                        console.log(response);
                        setProgressState(STATE.HIDE);
                        if (response.status == 200) {
                            window.location = "/";
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

        if (value_email == "") {
            input_email.focus();
            return false;
        }

        if (value_password1 == "") {
            input_pwd1.focus();
            return false;
        }

        return true;
    }

    function setProgressState(state) {
        if (STATE.SHOW)
            progress_spinner.style.display = 'inline-block';
        else (STATE.HIDE)
        progress_spinner.style.display = 'none';
    }
