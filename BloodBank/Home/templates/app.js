// This file will handle form submissions and any dynamic content
document.getElementById('donorForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Donor registered successfully!');
});

document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const city = document.getElementById('searchCity').value;
    const bloodType = document.getElementById('searchBloodType').value;

    // Here you would typically fetch results from a server or database
    document.getElementById('results').innerHTML = `<p>Searching for donors with blood type ${bloodType} in ${city}...</p>`;
});

document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Message sent successfully!');
});
function updateClock() {
    const clockElement = document.getElementById('clock');
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    clockElement.textContent = `${hours}:${minutes}:${seconds}`;
}

setInterval(updateClock, 1000); // Update the clock every second
updateClock(); // Initial call to display clock immediately



