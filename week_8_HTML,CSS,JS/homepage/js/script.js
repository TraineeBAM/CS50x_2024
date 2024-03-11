let submitBtn = document.getElementById('submit_btn');
let form = document.getElementById('form');
let popup = document.getElementById('popup')
let closePopup = document.getElementById('closePopup')

form.addEventListener('submit', (event) => {
    event.preventDefault()

    if (form.checkValidity()){
        popup.style.display='block';
        form.reset();
    }
})

closePopup.addEventListener('click', function (){
    popup.style.display='none';
})