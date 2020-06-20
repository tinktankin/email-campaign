//---------------------------------- HEADER AND LEFT PANEL START ---------------------------------------

var leftpanel = document.querySelector('.leftpanel');
var pagelinks = leftpanel.getElementsByClassName('pagelink');
for (var i = 0; i < pagelinks.length; i++) {
    pagelinks[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        if (current.length > 0) {
            current[0].className = current[0].className.replace(" active", "");
        }
        this.className += " active";
    });
};

document.querySelector('.namelabel').textContent = 'SUNEIL'
document.querySelector('.emailid').textContent = 'suniel.stanly@gmail.com'

//---------------------------------- HEADER AND LEFT PANEL END ---------------------------------------

//---------------------------------------OPENING NEW PAGES--------------------------------------------

document.querySelector('.inboxbtn').onclick = function () {
    location.href = "mailbox.html";
};

document.querySelector('.contactbtn').onclick = function () {
    location.href = "contacts.html";
};

document.querySelector('.dashboardbtn').onclick = function () {
    location.href = "dashboard.html";
};