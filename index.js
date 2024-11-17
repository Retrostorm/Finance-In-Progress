function toggleNavOn() {
  document.getElementById("nav-button-container").style.transform = "translateX(0)"
}

function toggleNavOff() {
  document.getElementById("nav-button-container").style.transform = "translateX(100%)"
}

addEventListener("resize", () => {
  if(window.innerWidth >= 750) {
    toggleNavOn()
  } else {
    toggleNavOff()
  }
});

function tr() {

}
