// Access skillsData passed from results.html
console.log('Skills data in results.js:', skillsData);

// Dynamically generate cards
const skillsContainer = document.getElementById('skillsContainer');
if (skillsData && skillsData.skills) {
    const skills = skillsData.skills;
    for (const skillName in skills) {
        if (skills.hasOwnProperty(skillName)) {
            const skillInfo = skills[skillName];
            const cardHTML = `
                <div class="card">
                    <div class="card-body">
                        <h3 class="card-title">${skillInfo.name}</h3>
                        <h5 class="card-symbol">${skillInfo.symbol}</h5>
                        <div class="card-info">
                        <p class="card-text">${skillInfo.definition}</p>
                        </d
                    </div>
                </div>
            `;
            skillsContainer.innerHTML += cardHTML; // Append card to container
        }
    }
} else {
    console.error('Skills data not available or invalid format');
}

function resetSkills() {
    fetch('/reset-skills', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Show reset message
        location.reload();   // Reload the page after reset
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error resetting skills data');
    });
}
