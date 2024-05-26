document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("upload-form").addEventListener("submit", async function(event) {
        event.preventDefault();

        let fileInput = document.getElementById("file-input");
        if (!fileInput.files[0]) {
            alert("Please select an image file.");
            return;
        }

        let formData = new FormData();
        formData.append("image", fileInput.files[0]);

        let response = await fetch("/api/upload/", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            alert("Failed to upload image. Please try again.");
            return;
        }

        let result = await response.json();
        displayResults(result);
    });

    function displayResults(result) {
        let resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = ""; // Clear previous results

        for (let key in result) {
            let colorDiv = document.createElement("div");
            colorDiv.className = "result-item";

            let colorName = document.createElement("span");
            colorName.textContent = `${key}: [${result[key][0]}, ${result[key][1]}, ${result[key][2]}]`;

            colorDiv.appendChild(colorName);
            resultsDiv.appendChild(colorDiv);
        }
    }
});
