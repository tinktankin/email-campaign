//---------------------------------------OTHER--------------------------------------------

//----file input replacement to improve UI
filehandle = document.getElementById('id_profile')
openexcel = document.querySelector('.openfilebtn')

openexcel.addEventListener('click', function () {
    filehandle.click();
})

var fileUpload = document.getElementById('id_profile');

fileUpload.onchange = function (evt) {
    if (fileUpload.value != "") {
        if (typeof (FileReader) != "undefined") {
            document.querySelector('.filenamelabel').innerHTML = fileUpload.files[0].name;
        }
    }
};



//--------------------------load manage email---------------------------

//------------------------load personal details------------------------------------


