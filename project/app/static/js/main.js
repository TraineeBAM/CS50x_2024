let about = document.getElementById('about')
let privacy = document.getElementById('privacy')
let closePopup = document.querySelectorAll('.closePopup')

about.addEventListener('click', function() {
    aboutInfo.style.display='block';
})

privacy.addEventListener('click', function() {
    privacyInfo.style.display='block';
})

closePopup.forEach(function(closePopup) {
    closePopup.addEventListener('click', function() {
        aboutInfo.style.display = 'none';
        privacyInfo.style.display = 'none';
    });
});