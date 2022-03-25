function load(dst, src) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        document.getElementById(dst).innerHTML = this.responseText;
    };
    xhttp.open("GET", src, true);
    xhttp.send();
}