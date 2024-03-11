let incorrect = document.querySelectorAll('.incorrect');
let incorrectBtn = document.querySelectorAll('.incorrect>button')
incorrectBtn.forEach(function(element) {
    element.addEventListener('click', function() {
        element.style.backgroundColor = 'red';
        element.parentNode.innerHTML += `<p>Incorrect</p>`;
    });
})

let correct = document.querySelector('.correct');
let correctBtn = document.querySelector('.correct>button')
correctBtn.addEventListener('click', function(){
    correctBtn.style.backgroundColor = 'green';
    correct.innerHTML += `<p>Correct!</p>`;
})

let userInput = document.querySelector('#userInput');
let submitBtn = document.querySelector('#submitBtn');
let textGen = document.querySelector('#textGen');

submitBtn.addEventListener('click', function(event){
    textGen.innerHTML = '';
    let userInputValue = userInput.value.toLowerCase();
    if (userInputValue == 'ganymede'){
        userInput.style.backgroundColor = 'green';
        textGen.innerHTML += `<p>Ganymede is correct!</p>`;
    } else{
        userInput.style.backgroundColor = 'red';
        textGen.innerHTML += `<p>Incorrect</p>`
    }
})
