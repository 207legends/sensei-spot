window.onload = onBodyLoad;

function setOfferOfDayModal(state) {
    let s = state == true ? 'show' : 'hide';
    $('#modal-offer-of-day').modal(s)
}

function hideTopAnnouncement() {
    hide('top-announcement-container');
}

function onBodyLoad() {
    //setTheme();
    setOfferOfDayModal(CONSTANTS.OFFER_OF_DAY.STATE);
}

function setTheme() {
    let themeSheet = document.getElementById("stylesheet-theme");

    let currentTheme = localStorage.getItem("current-theme");
    if (currentTheme != null) {
        themeSheet.href = `/static/css/main-${currentTheme}.css`;
    }
    else {
        currentTheme = "light";
        themeSheet.href = `/static/css/main-${currentTheme}.css`;
    }
}

function swtichTheme() {
    let newThemeValue = document.getElementById("checkbox-theme").checked ? "dark" : "light";
    console.log(newThemeValue);

    localStorage.setItem("current-theme", newThemeValue);

    setTheme();
}

window.onscroll = () => {
    if (document.body.scrollTop > 100) {
        document.getElementById("btn-scroll-to-top").style.display = "block";
    }
    else {
        document.getElementById("btn-scroll-to-top").style.display = "none";
    }
}