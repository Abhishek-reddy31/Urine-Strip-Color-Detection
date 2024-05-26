document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contact-form").addEventListener("submit", function(event) {
        event.preventDefault();
        
        
        alert("Thank you for your message. We will get back to you shortly.");
    });
});