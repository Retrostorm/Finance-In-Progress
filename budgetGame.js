// Robert Palmer            11-16-24
// function to act as main function for the budget game

let month = 0;
let promptInMonth = 0;
const totalMonths = 5;
let funds = 1000;
const income = 13000;
const fixedExpenses = 1000;
let thisMonthsPrompts = [];
const situations = [{"Prompt1": {"Choice": "Feedback"}, "Prompt2": {"Choice": "Feedback"}}];
let feedback = []; 

function userInput(choice) {
    // This is the function called when a user gives input to a month / presses one of the buttons
    
    // Want new index of feedback to be last index + 1 / length of the array
    let newIndex = feedback.length;

    // Assign newIndex of feedback to the feedback associated with that month, the current prompt, and the user's choice
    // feedback[newIndex] = situations[month][thisMonthsPrompts[promptInMonth]][choice];
    feedback[newIndex] = situations[month][promptInMonth]["feedback"][choice]

    if (promptInMonth == 2) {
        nextMonth();
    } else {
        nextPrompt();
    }
}

function nextPrompt() {
    thisMonthsPrompts++;
    
    // Display stuff
}

function nextMonth() {
    month++;

    // Display the next months stuff
}
