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
var balance = wtWages[randWT - 1];

// This variable represents costs accrued due to using a credit card, this is displayed at end
var creditCardBill = 0;

// Data structure for data of cards
// Individual items are for choice 0 or choice 1
// First array in each element holds what change takes place, second is value of that change
const cards = [
    [["nothing", "nothing"], [0, 0], "Context Here for W2"],
    [["balance", "nothing"], [-690, 0], ""],
    [["balance", "nothing"], [-2800, 0], ""],
    [["balance", "balance"], [0, 500], ""], 
    [["balance", "credit"], [-75, 75], ""],
    [["balance", "nothing"], [-68, 0], ""],
];

function userChoice(cardNum, choice) {
    // When passing cardNum, note that the first card will have an index of 1, but will be stored at index 0 in cards
    let card = cards[cardNum - 1];

    if (card[0][choice] == "balance") {
        balance += card[1][choice];
        console.log(balance);
    } else if (card[0][choice] == "credit") {
        creditCardBill += card[1][choice];
    }

    nextCard();
}


function openFullscreen(elem) {
    if (document.fullscreenElement) {
        document.exitFullscreen()
    } else if (document.querySelector("body").requestFullscreen) {
        document.querySelector("body").requestFullscreen();
    } else if (document.querySelector("body").webkitRequestFullscreen) { /* Safari */
        document.querySelector("body").webkitRequestFullscreen();
    } else if (document.querySelector("body").msRequestFullscreen) { /* IE11 */
        document.querySelector("body").msRequestFullscreen();
    }
  }
