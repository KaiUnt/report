const eventsUrl = 'http://127.0.0.1:8000/events';
const generatePdfUrl = 'http://127.0.0.1:8000/generate_pdf';
const eventSearch = document.getElementById('eventSearch');
const eventList = document.getElementById('eventList');
const statusDiv = document.getElementById('status');

// Events laden und Suchfunktion aktivieren
async function loadEvents() {
    try {
        const response = await fetch(eventsUrl);
        if (!response.ok) throw new Error('Fehler beim Laden der Events.');
        
        const data = await response.json();
        const sortedEvents = data.events.sort((a, b) => new Date(a.date) - new Date(b.date));

        // Filterung aktivieren
        eventSearch.addEventListener('input', () => {
            const query = eventSearch.value.toLowerCase();
            const filteredEvents = sortedEvents.filter(event =>
                event.name.toLowerCase().includes(query) || event.date.includes(query)
            );
            renderEventList(filteredEvents);
        });
    } catch (error) {
        statusDiv.textContent = `Fehler: ${error.message}`;
    }
}

// Events rendern (mit Download-Button)
function renderEventList(events) {
    eventList.innerHTML = ''; // Alte Liste leeren
    if (events.length === 0) {
        eventList.innerHTML = '<li>Keine passenden Events gefunden.</li>';
        return;
    }

    events.forEach(event => {
        const listItem = document.createElement('li');
        listItem.className = 'event-container';

        // Event-Name
        const eventInfo = document.createElement('span');
        eventInfo.textContent = `${event.name} (${new Date(event.date).toLocaleDateString()})`;

        // Download-Button
        const downloadBtn = document.createElement('button');
        downloadBtn.textContent = 'Download Report';
        downloadBtn.addEventListener('click', () => generatePdf(event.id, downloadBtn));

        // Zusammenfügen
        listItem.appendChild(eventInfo);
        listItem.appendChild(downloadBtn);
        eventList.appendChild(listItem);
    });
}


// PDF generieren
async function generatePdf(eventId, button) {
    const originalText = button.textContent; // Ursprünglicher Button-Text speichern
    button.textContent = 'Lädt...';          // Button-Text ändern
    button.disabled = true;                  // Button deaktivieren

    try {
        statusDiv.textContent = '';          // Status leeren
        statusDiv.style.color = 'blue';
        statusDiv.textContent = 'PDF wird generiert... Bitte warten.';

        const response = await fetch(`${generatePdfUrl}?event_id=${eventId}`);
        if (!response.ok) throw new Error('Fehler beim Generieren der PDF.');

        // PDF herunterladen
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = `report_${eventId}.pdf`;
        link.click();
        URL.revokeObjectURL(url);

        statusDiv.style.color = 'green';
        statusDiv.textContent = 'PDF erfolgreich heruntergeladen!';
    } catch (error) {
        statusDiv.style.color = 'red';
        statusDiv.textContent = `Fehler: ${error.message}`;
    } finally {
        button.textContent = originalText; // Ursprünglichen Button-Text wiederherstellen
        button.disabled = false;           // Button aktivieren
    }
}

// Ladeindikator-Funktion hinzufügen
function showLoading(message) {
    statusDiv.textContent = message;  // Lade-Text anzeigen
    statusDiv.style.color = 'blue';
}

function hideLoading() {
    statusDiv.textContent = '';  // Lade-Text leeren
}

// Initialisierung
loadEvents();
