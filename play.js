function nextCard() {
  document.querySelector(".card:nth-child(1)").style.transform = "translateY(-200%)"
  document.querySelector(".card:nth-child(1)").style.opacity = ".8"
  setTimeout(() => {
    document.querySelector(".card:nth-child(1)").remove()
  }, 500);  
}

var randWT = (Math.floor(Math.random() * 3) + 1)
document.querySelector(".card:nth-child(1)").innerHTML = `<img src="/docs/w2-${randWT}.svg" />`
