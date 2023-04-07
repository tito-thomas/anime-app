
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


function checkLoggedIn() {

    var url = document.URL.split('/')
    //Check if user is logged in
    if (document.URL.includes("Dashboard")) {
        const navbar = document.querySelector("#mynav")
        navbar.style.display = "flex"
        navbar.style.backgroundColor = "#0e113a"

        //window.addEventListener("scroll", homeNavStyling)
    }

}

checkLoggedIn()