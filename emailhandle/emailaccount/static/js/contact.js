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


//---------------------------------- HEADER AND LEFT PANEL END ---------------------------------------










//----file input replacement to improve UI
filehandle = document.getElementById('id_myfile')
openexcel = document.querySelector('.openfilebtn')

openexcel.addEventListener('click', function () {
    filehandle.click();
})

var fileUpload = document.getElementById('id_myfile');

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


//simulating loading data to table end
