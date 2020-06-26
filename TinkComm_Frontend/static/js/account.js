
//---------------------------------------OTHER--------------------------------------------

//----file input replacement to improve UI
filehandle = document.getElementById('myphoto')
openexcel = document.querySelector('.openfilebtn')

openexcel.addEventListener('click', function () {
    filehandle.click();
})

var fileUpload = document.getElementById('myphoto');

fileUpload.onchange = function (evt) {
    if (fileUpload.value != "") {
        if (typeof (FileReader) != "undefined") {
            document.querySelector('.filenamelabel').innerHTML = fileUpload.files[0].name;
        }
    }
};



//--------------------------load manage email---------------------------
var dummyData = [
    {emailid:'suneil.stanly@gmail.com'},
    {emailid:'suneils008@outlook.com'},
    {emailid:'stan@tinktank.com'},
];

var i;
var htmlcontent = `<div class="singleemailid">
                        <label></label>
                        <div>
                            <button class="makedefaultbtn">MAKE DEFAULT</button>
                            <button class="removebtn">REMOVE</button>
                        </div>
                    </div>`

var selectmenucontent;

for (i = 0; i < dummyData.length; i++) {
    document.querySelector('.manageemail').insertAdjacentHTML('beforeend', htmlcontent);
    emailidbox = document.querySelector('.manageemail').lastElementChild;
    emailidbox.firstElementChild.innerHTML = dummyData[i].emailid;

    selectmenucontent = `<option value="${dummyData[i].emailid}">${dummyData[i].emailid}</option>`
    document.querySelector('#selectemailid').insertAdjacentHTML('beforeend', selectmenucontent);
    }

//------------------------load personal details------------------------------------

document.querySelector('.userimage').src = 'static/images/userimage.svg';
document.querySelector('.completenamelabel').innerHTML = 'Suneil Stanly';
document.querySelector('.usernamelabel').innerHTML = 'suneil.stanly.009';
document.querySelector('.accountemaillabel').innerHTML = 'suneil.stanly@gmail.com';
document.querySelector('.defaultemaillabel').innerHTML = 'suneil.stanly@gmail.com';