function nextCard() {
    document.querySelector(".card:nth-child(1)").style.transform = "translateY(-200%)";
    document.querySelector(".card:nth-child(1)").style.opacity = ".8";
    setTimeout(() => {
      document.querySelector(".card:nth-child(1)").remove()
    }, 500);  
  }

var randWT = (Math.floor(Math.random() * 3) + 1);
document.querySelector(".card:nth-child(1)").innerHTML = `<img src="/docs/w2-${randWT}.svg" />`;

const wtWages = [2468.54, 64543.84, 13458.21];
var balance = wtWages[randWt - 1];

// This variable represents costs accrued due to using a credit card, this is displayed at end
var creditCardBill = 0;

const cards = {1: "AAAAAAAAAA"}

function userChoice(cardNum) {

}

function balanceChange(change) {
    // change is either positive for saving or negative for spending
    balance += change;
}
