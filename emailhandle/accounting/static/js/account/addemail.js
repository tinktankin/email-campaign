
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



//---------------------------------- HEADER AND LEFT PANEL END ---------------------------------------

//---------------------------------------OPENING NEW PAGES--------------------------------------------

document.querySelector('.inboxbtn').onclick = function () {
    location.href = "http://localhost:8000/TinkComm/user/mailbox";
};
document.querySelector('.accountpagelink').onclick = function () {
    location.href = "http://localhost:8000/TinkComm/user/accountsetting/";
};

document.querySelector('.contactbtn').onclick = function () {
    location.href = "http://localhost:8000/TinkComm/user/contact";
};

document.querySelector('.dashboardbtn').onclick = function () {
    location.href = "http://localhost:8000/TinkComm/user/home/";
};
document.querySelector('.groupbtn').onclick = function () {
    location.href = "http://localhost:8000/TinkComm/user/groups/";
};
