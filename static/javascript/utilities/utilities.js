function hide(id) {
    let e = document.getElementById(id);
    e.style.display = 'none';
}

function show(id) {
    let e = document.getElementById(id);
    e.style.display = 'block';
}

function setTitleForHeadingWithUnderline(title) {
    document.getElementById("heading-title").innerHTML = title;
}