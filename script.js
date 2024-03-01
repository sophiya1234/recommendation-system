function getRecommendation() {
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;

    // Make a GET request to your Python backend
    fetch(`/recommendation?age=${age}&gender=${gender}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Process the response from the backend
            updateInterface(data);
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function updateInterface(data) {
    const recommendationDiv = document.getElementById('recommendation');
    recommendationDiv.innerText = data.recommendation;
}
