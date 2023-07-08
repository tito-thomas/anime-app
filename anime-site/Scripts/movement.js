
/*function homeNavStyling() {
    const navbar = document.querySelector("#mynav")
    navbar.style.transition = "0.4s"
    if (window.scrollY != 0) {
        navbar.style.backgroundColor = "rgb(3 36 86)"
    }
    else {
        navbar.style.backgroundColor = "transparent"
    }
}*/

if (document.URL.includes("Welcome")) {
    //stop buttons from redirecting
    const selections = document.querySelector(".qbuttons");
    selections.addEventListener("click", function (event) {
        event.preventDefault();

    });
}


function checkLoggedIn() {

    var url = document.URL.split('/')
    //Check if user is logged in
    if (document.URL.includes("Welcome") || document.URL.includes("Dashboard")) {
        const navbar = document.querySelector("#mynav")
        navbar.style.display = "flex"
        if (document.URL.includes("Welcome")){
            navbar.style.backgroundColor = "#0e113a"
        }
        else { navbar.style.backgroundColor = "rgb(128 195 132)"}
        //window.addEventListener("scroll", homeNavStyling)
        return true;
    }

}

checkLoggedIn()

let counter = 1;

const next = document.querySelectorAll(".next-button");

let pos = -1500;


next.forEach(function (e) { 
    e.addEventListener("click", function () {
        //const next = document.querySelector("#next-button");
        const slide = document.querySelector(".all-questions");
        const images = document.querySelectorAll(".question-group");
        //subtract distance we moved initally in css }
        if (counter == 2) {back.style.display = "flex";}
        if (counter == 1) { next[1].style.display = "flex"; }
        if (counter == 5) { next[1].style.display = "none"; }

        if (e == next[0]) {pos += 640;}
        else { pos += 600;}
        
        //if we're end the end hide the next button
        if (counter == images.length - 1) {
            //counter = 0;
            //next.style.display = "none";
            //think of translate values as coordinates not the amount that it moves the element
        }

        slide.style.transition = "transform 0.4s ease-in-out";
        slide.style.transform = "translateX(" + -pos + "px)";
        counter++;
        console.log(counter);

    });
});


//let backcounter = 1;
const back = document.querySelector("#back-button");
back.addEventListener("click", function () {
    const slide = document.querySelector(".all-questions");
    const images = document.querySelectorAll(".question-group");
    next[1].style.display = "flex";
    //subtract distance we moved initally in css }

    pos -= 600;
    //if we're end the end hide the next button
    if (counter == 3) {
        back.style.display = "none";
        //think of translate values as coordinates not the amount that it moves the element
    }
    //else {
        slide.style.transition = "transform 0.4s ease-in-out";
        slide.style.transform = "translateX(" + -pos + "px)";
        counter--;
        console.log(counter);
    //}
});