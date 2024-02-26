const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

let currentDate = new Date();
let currentMonth = currentDate.getMonth();
let currentYear = currentDate.getFullYear();

// Object to store events
const events = {};

function renderCalendar() {
    const monthYearElement = document.getElementById('monthYear');
    const datesElement = document.getElementById('dates');

    monthYearElement.textContent = `${months[currentMonth]} ${currentYear}`;

    const firstDay = new Date(currentYear, currentMonth, 1);
    const lastDay = new Date(currentYear, currentMonth + 1, 0);

    let html = '';
    for (let i = 1; i <= lastDay.getDate(); i++) {
        const date = new Date(currentYear, currentMonth, i);
        const classes = date.getMonth() === currentMonth ? 'date current-month' : 'date';

        // Check if there's an event for the date
        const eventCount = events[date.toISOString()] ? events[date.toISOString()].length : 0;

        html += `<div class="${classes}" onclick="showEvents('${date.toISOString()}')">
                    <span>${i}</span>
                    ${eventCount > 0 ? `<div class="event-count">${eventCount}</div>` : ''}
                </div>`;
    }

    datesElement.innerHTML = html;
}

function showEvents(dateISO) {
    const date = new Date(dateISO);
    const dateString = date.toDateString();
    const eventList = events[dateISO] || [];

    let eventText = `<h3>${dateString}</h3>`;
    eventText += `<ul>`;
    eventList.forEach(event => {
        eventText += `<li>${event}</li>`;
    });
    eventText += `</ul>`;

    const eventModal = document.createElement('div');
    eventModal.className = 'event-modal';
    eventModal.innerHTML = eventText;

    document.body.appendChild(eventModal);
}

function addEvent() {
    const eventDate = document.getElementById('eventDate').value;
    const eventText = document.getElementById('eventText').value;

    if (eventDate && eventText) {
        if (!events[eventDate]) {
            events[eventDate] = [];
        }
        events[eventDate].push(eventText);

        renderCalendar();
    }

    // Close the modal
    closeModal();
}

function closeModal() {
    const eventModal = document.querySelector('.event-modal');
    if (eventModal) {
        eventModal.remove();
    }
}

document.addEventListener('DOMContentLoaded', renderCalendar);
