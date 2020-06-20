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










//----file input replacement to improve UI
filehandle = document.getElementById('myfile')
openexcel = document.querySelector('.openfilebtn')

openexcel.addEventListener('click', function () {
    filehandle.click();
})

var fileUpload = document.getElementById('myfile');

fileUpload.onchange = function (evt) {
    if (fileUpload.value != "") {
        if (typeof (FileReader) != "undefined") {
            document.querySelector('.filenamelabel').innerHTML = fileUpload.files[0].name;
        }
    }
};

//-----file input replacement end

//-----add contacts manually window
var modal = document.getElementById("myModal");
var manualadd = document.querySelector('.addbtn');
var mapform = document.querySelector('.mapForm');
var span = document.querySelector('.close');


manualadd.onclick = function () {
    mapform.style.display = "flex";
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
//------add contacts manually window end

//----simulating loading data to table

htmlcontent = `<div class="contactidH"><label>ID</label></div>
            <div class="nameH"><label>Name</label></div>
            <div class="firstNameH"><label>First Name</label></div>
            <div class="middleNameH"><label>Middle Name</label></div>
            <div class="lastNameH"><label>Last Name</label></div>`

document.querySelector('.tableheader').insertAdjacentHTML('beforeend', htmlcontent);

var i;
var htmlcontent;
for (i = 0; i < 50; i++) {
    htmlcontent = `<div class="entry">
            <div class="contactid"></div>
            <div class="name"></div>
            <div class="firstName">
            </div><div class="middleName">
            </div><div class="lastName"></div>
            </div>`

    document.querySelector('.resultSet').insertAdjacentHTML('beforeend', htmlcontent);
}

//simulating loading data to table end