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

var name = 'SUNEIL STANLY'
document.querySelector('.namelabel').textContent = name.split(' ')[0];

document.querySelector('.emailid').textContent = 'suneil.stanly@gmail.com'

//---------------------------------- HEADER AND LEFT PANEL END ---------------------------------------

//---------------------------------------OPENING NEW PAGES--------------------------------------------

document.querySelector('.accountpagelink').onclick = function () {
    location.href = "account.html";
};

document.querySelector('.inboxbtn').onclick = function () {
    location.href = "mailbox.html";
};

document.querySelector('.unreadbtn').onclick = function () {
    location.href = "mailbox.html";
};

document.querySelector('.sentbtn').onclick = function () {
    location.href = "mailbox.html";
};

document.querySelector('.bouncedbtn').onclick = function () {
    location.href = "mailbox.html";
};

document.querySelector('.dashboardbtn').onclick = function () {
    location.href = "dashboard.html";
};

document.querySelector('.contactbtn').onclick = function () {
    location.href = "contacts.html";
};

document.querySelector('.groupbtn').onclick = function () {
    location.href = "groups.html";
};

document.querySelector('.campaignbtn').onclick = function () {
    location.href = "campaigns.html";
};

document.querySelector('.formbtn').onclick = function () {
    location.href = "forms.html";
};

document.querySelector('.templatebtn').onclick = function () {
    location.href = "templates.html";
};

document.querySelector('.statbtn').onclick = function () {
    location.href = "stats.html";
};