let about = document.getElementById('about')
let privacy = document.getElementById('privacy')
let closePopup = document.querySelectorAll('.closePopup')
let submitBtn = document.getElementById('submit')
let files;

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

let dropArea = document.getElementById('drop-area');

// Prevent default behavior for drop events
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight the drop area when a file is dragged over
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

// Remove highlight when the file is not being dragged over
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight() {
    dropArea.classList.add('highlight');
}

function unhighlight() {
    dropArea.classList.remove('highlight');
}
let fileInput = document.getElementById('resumeInput');
function handleDrop(e) {

    files = e.dataTransfer.files;

    // Update the file input with the dropped files
    fileInput.files = files;

    // Perform any additional actions you need with the dropped files
    console.log('Files dropped:', files);

    // Reset the highlight
    dropArea.classList.remove('highlight');
    return files
}

// Handle file selection using the file input
function handleFileSelect() {
    files = fileInput.files;

    // Perform any actions you need with the selected files
    console.log('Files selected:', files);
    return files;
}

function removeFile(){
    fileInput.value = '';
    fileInput.dispatchEvent(new Event('input'));
    return;
}

submitBtn.addEventListener('click', function () {
    // Check that file-type user has uploaded is supported (.pdf, .docx, .doc, .txt)
    if (files && files.length > 0) {
        let supportedTypes = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'];
        
        if (!supportedTypes.includes(files[0].type)) {
            alert(`Only PDF, DOC, DOCX, and TXT supported. You uploaded ${files[0].type}`);
            removeFile();
        } else {
            alert('submitted!')
            removeFile();
        }} 
    else {
        // Handle case when no file is selected
        alert('No file selected');
    }
});

let removeFileBtn = document.getElementById('removeFile');
removeFileBtn.addEventListener('click', removeFile);