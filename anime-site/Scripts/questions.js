

const buttons1 = document.querySelectorAll("#group1 button")
const hiddeninput1 = document.querySelector("#v1")
let value1 = "";
var selected1 = {};
var prev1;
buttons1.forEach(function (i) {
    i.addEventListener("click", function (){
        value1 = i.value;
        console.log("click");
        hiddeninput1.value = value1;

        //Any new selection, highlight new button, declour previous
        if ((selected1[i.value] == 0 || !(i.value in selected1)) & prev1 != null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected1[i.value] = 1;

            prev1.style.backgroundColor = "#F0F0F0";
            prev1.style.color = "black";
            selected1[prev1.value] = 0;
            prev1 = i
        }
       //First time selection - change colour
        else if (selected1[i.value] == 0 || !(i.value in selected1) & prev1 == null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected1[i.value] = 1;
            prev1 = i
        }
            
    })
})



const buttons2 = document.querySelectorAll("#group2 button")
const hiddeninput2 = document.querySelector("#v2")
let value2 = "";
var selected2 = {};
var prev2;
buttons2.forEach(function (i) {
    i.addEventListener("click", function () {
        value2 = i.value;
        hiddeninput2.value = value2;

        //Any new selection, highlight new button, declour previous
        if ((selected2[i.value] == 0 || !(i.value in selected2)) & prev2 != null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected2[i.value] = 1;

            prev2.style.backgroundColor = "#F0F0F0";
            prev2.style.color = "black";
            selected2[prev1.value] = 0;
            prev2 = i
        }
        //First time selection - change colour
        else if (selected2[i.value] == 0 || !(i.value in selected2) & prev2 == null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected2[i.value] = 1;
            prev2 = i
        }
    })
})



const buttons3 = document.querySelectorAll("#group3 button")
const hiddeninput3 = document.querySelector("#v3")
let value3 = "";
var selected3 = {};
var prev3;
buttons3.forEach(function (i) {
    i.addEventListener("click", function () {
        value3 = i.value;
        hiddeninput3.value = value3;

        //Any new selection, highlight new button, declour previous
        if ((selected3[i.value] == 0 || !(i.value in selected3)) & prev3 != null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected3[i.value] = 1;

            prev3.style.backgroundColor = "#F0F0F0";
            prev3.style.color = "black";
            selected3[prev3.value] = 0;
            prev3 = i
        }
        //First time selection - change colour
        else if (selected3[i.value] == 0 || !(i.value in selected3) & prev3 == null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected3[i.value] = 1;
            prev3 = i
        }
    })
})



const buttons4 = document.querySelectorAll("#group4 button")
const hiddeninput4 = document.querySelector("#v4")
let value4 = "";
var selected4 = {};
var prev4;
buttons4.forEach(function (i) {
    i.addEventListener("click", function () {
        value4 = i.value;
        hiddeninput4.value = value4;

        //Any new selection, highlight new button, declour previous
        if ((selected4[i.value] == 0 || !(i.value in selected4)) & prev4 != null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected4[i.value] = 1;

            prev4.style.backgroundColor = "#F0F0F0";
            prev4.style.color = "black";
            selected4[prev4.value] = 0;
            prev4 = i
        }
        //First time selection - change colour
        else if (selected4[i.value] == 0 || !(i.value in selected4) & prev4 == null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected4[i.value] = 1;
            prev4 = i
        }
    })
})


const buttons5 = document.querySelectorAll("#group5 button")
const hiddeninput5 = document.querySelector("#v5")
let value5 = "";
var selected5 = {};
var prev5;
buttons5.forEach(function (i) {
    i.addEventListener("click", function () {
        value5 = i.value;
        hiddeninput5.value = value5;

        //Any new selection, highlight new button, declour previous
        if ((selected5[i.value] == 0 || !(i.value in selected5)) & prev5 != null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected5[i.value] = 1;

            prev5.style.backgroundColor = "#F0F0F0";
            prev5.style.color = "black";
            selected5[prev5.value] = 0;
            prev5 = i
        }
        //First time selection - change colour
        else if (selected5[i.value] == 0 || !(i.value in selected5) & prev5 == null) {
            i.style.backgroundColor = "rgb(79 91 255)";
            i.style.color = "white";
            selected5[i.value] = 1;
            prev5 = i
        }
    })
})
