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










//---------------------------------- SIMULATING BACKEND INTERACTION START -----------------------------------
var dummyData = [
    {From:'Naman', Email:'naman@gmail.com', Subject:'Database deployed on the cloud', Date:'9: 23 PM | June 12, 2020'},
    {From:'Hritik', Email:'hritik@gmail.com', Subject:'Task updated on Trello', Date:'3: 23 PM | June 12, 2020'},
    {From:'Anurag', Email:'anurag@outlook.com', Subject:'Grant access to Github', Date:'10: 31 AM | June 12, 2020'},
    {From:'Ashay', Email:'ashay@outlook.com', Subject:'Read receipts solution found', Date:'12: 11 PM | June 11, 2020'},
    {From:'Tushar', Email:'tushar@gmail.com', Subject:'imaplib done and dusted', Date:'6: 13 PM | June 10, 2020'},
    {From:'Naman', Email:'naman@gmail.com', Subject:'Database deployed on the cloud', Date:'9: 23 PM | June 12, 2020'},
    {From:'Hritik', Email:'hritik@gmail.com', Subject:'Task updated on Trello', Date:'3: 23 PM | June 12, 2020'},
    {From:'Anurag', Email:'anurag@outlook.com', Subject:'Grant access to Github', Date:'10: 31 AM | June 12, 2020'},
    {From:'Ashay', Email:'ashay@outlook.com', Subject:'Read receipts solution found', Date:'12: 11 PM | June 11, 2020'},
    {From:'Tushar', Email:'tushar@gmail.com', Subject:'imaplib done and dusted', Date:'6: 13 PM | June 10, 2020'},
];

var htmlcontent;
var totalmails = 10;
var llimit = 1;
var ulimit = llimit + dummyData.length - 1;
document.querySelector('.numemails').textContent = String(llimit) + '-' + String(ulimit) + ' of ' + String(totalmails);


for (var j = 0; j < dummyData.length; j++) {
    htmlcontent = `
            <div class="messagebox">
                <div class="div1"><label></label></div>
                <div class="div2"><label></label></div>
                <div class="div3"><hr class="hr2"></div>
                <div class="div4"><label>SUBJECT</label></div>
                <div class="div5"><label></label></div>
                <div class="div6"><label></label></div>
                <div class="div7"><button><i class="far fa-eye" aria-hidden="true"></i></button></div>
                <div class="div8"><button><i class="far fa-trash-alt" aria-hidden="true"></i></button></div>
            </div>
            `
    document.querySelector('.rightbox').insertAdjacentHTML('beforeend', htmlcontent);
    msgbox = document.querySelector('.rightbox').lastElementChild;
    msgbox.querySelector('.div1').firstElementChild.innerHTML = dummyData[j].From;
    msgbox.querySelector('.div2').firstElementChild.innerHTML = dummyData[j].Email;
    msgbox.querySelector('.div5').firstElementChild.innerHTML = dummyData[j].Subject;
    msgbox.querySelector('.div6').firstElementChild.innerHTML = dummyData[j].Date;
}
//---------------------------------- SIMULATING BACKEND INTERACTION END -----------------------------------

//---------------------------------- FRONTEND INTERACTION START -------------------------------------------


//---------------------------------- FRONTEND INTERACTION END -------------------------------------------