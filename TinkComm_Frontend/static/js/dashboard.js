//---------------------------------- HEADER AND LEFT PANEL START ---------------------------------------

var pagelinks = document.querySelector('.leftpanel').getElementsByClassName('pagelink');
for (var i = 0; i < pagelinks.length; i++) {
    pagelinks[i].addEventListener("click", function () {
        var current = document.querySelector('.leftpanel').getElementsByClassName("active");
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
    {Group:'Technical', Subject:'Deploy application on AWS', Date:'9: 23 PM | June 12, 2020', Read:3},
    {Group:'Technical', Subject:'Distribute marketing materials', Date:'8: 23 PM | June 10, 2020', Read:9},
    {Group:'Technical', Subject:'Deploy application on Azure', Date:'8: 23 PM | June 9, 2020', Read:12},
    {Group:'Technical', Subject:'Start Digital Marketing', Date:'8: 23 PM | June 8, 2020', Read:6},
    {Group:'Technical', Subject:'Deploy application on Azure', Date:'8: 23 PM | June 9, 2020', Read:12},
    {Group:'Technical', Subject:'Start Digital Marketing', Date:'8: 23 PM | June 8, 2020', Read:6}
];

var lastData = [
    {Group:'Technical', Subject:'Deploy application on AWS', Date:'9: 23 PM | June 12, 2020'},
    {Group:'Promotion', Subject:'Distribute marketing materials', Date:'8: 23 PM | June 10, 2020'},
    {Group:'Management', Subject:'Hiring postponed', Date:'8: 23 PM | June 10, 2020'}
]

var mailboxcontent;

for (var j = 0; j < lastData.length; j++) {
    mailboxcontent = `
            <div class="groupbox">
                <div class="gbdiv1"><label></label></div>
                <div class="gbdiv2"><hr class="hr2"></div>
                <div class="gbdiv3"><label></label></div>
                <div class="gbdiv4"><label></label></div>
            </div>
            `
    document.querySelector('.grouplist').insertAdjacentHTML('beforeend', mailboxcontent);
    grpbox = document.querySelector('.grouplist').lastElementChild;
    grpbox.querySelector('.gbdiv1').firstElementChild.innerHTML = lastData[j].Group;
    grpbox.querySelector('.gbdiv3').firstElementChild.innerHTML = lastData[j].Subject;
    grpbox.querySelector('.gbdiv4').firstElementChild.innerHTML = lastData[j].Date;
}

var historyboxcontent;

for (var j = 0; j < dummyData.length; j++) {
    historyboxcontent = `
            <div class="messagebox">
                <div class="mbdiv1"><label>You</label></div>
                <div class="mbdiv2">
                    <div><label>SUBJECT</label></div>
                    <label class="subjecthistory">Deploy the application on AWS</label>
                </div>
                <div class="mbdiv3"><button class="viewmailbtn"><i class="fas fa-external-link-alt"></i></button></div>
                <div class="mbdiv4"><hr class="hr2"></div>
                <div class="mbdiv5">
                    <label class="datehistory">9: 23 PM | June 12, 2020</label>
                    <button class="seenbtn">SEEN BY 2</button>
                </div>
            </div>
            `
    document.querySelector('.mailhistory').insertAdjacentHTML('beforeend', historyboxcontent);
    msgbox = document.querySelector('.mailhistory').lastElementChild;
    msgbox.querySelector('.subjecthistory').innerHTML = dummyData[j].Subject;
    msgbox.querySelector('.datehistory').innerHTML = dummyData[j].Date;
    msgbox.querySelector('.seenbtn').innerHTML = 'SEEN BY ' + String(dummyData[j].Read);
}

//---------------------------------- SIMULATING BACKEND INTERACTION END -----------------------------------

//---------------------------------- FRONT END INTERACTIONS START-------------------------------------

var tablist = document.querySelector('.mailtabs').getElementsByClassName('tablist');
for (var i = 0; i < tablist.length; i++) {
    tablist[i].addEventListener("click", function () {
        var current = document.querySelector('.mailtabs').getElementsByClassName("active");
        if (current.length > 0) {
            current[0].className = current[0].className.replace(" active", "");
        }
        this.className += " active";
    });
};

var groupboxes = document.querySelector('.grouplist').getElementsByClassName('groupbox');
for (var i = 0; i < groupboxes.length; i++) {
    groupboxes[i].addEventListener("click", function () {
        var current = document.querySelector('.grouplist').getElementsByClassName("groupbox active");
        if (current.length > 0) {
            current[0].className = current[0].className.replace(" active", "");
        }
        this.className += " active";
    });
};


//---------------------------------- FRONT END INTERACTIONS END-------------------------------------