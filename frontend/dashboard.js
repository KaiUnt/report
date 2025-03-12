// Global variables
let allAthletes = [];
let currentAthleteIndex = 0;
let eventName = "";

// Get event ID from URL
const urlParams = new URLSearchParams(window.location.search);
const eventId = urlParams.get('event_id');

// DOM Elements
const loadingSpinner = document.getElementById('loadingSpinner');
const profileContent = document.getElementById('profileContent');
const prevButton = document.getElementById('prevAthlete');
const nextButton = document.getElementById('nextAthlete');
const athleteCounter = document.getElementById('athleteCounter');
const eventNameElement = document.getElementById('eventName');

// Event listeners
document.addEventListener('DOMContentLoaded', init);
prevButton.addEventListener('click', showPreviousAthlete);
nextButton.addEventListener('click', showNextAthlete);

// Initialization function
async function init() {
    if (!eventId) {
        showError("No event ID provided");
        return;
    }
    
    try {
        await fetchAthleteData();
        updateNavigation();
        showAthlete(currentAthleteIndex);
    } catch (error) {
        showError("Failed to load athlete data: " + error.message);
    }
}

// Fetch athlete data from API
async function fetchAthleteData() {
    showLoading(true);
    
    try {
        const response = await fetch(`/api/athlete_data?event_id=${eventId}`);
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`API error (${response.status}): ${errorText}`);
        }
        
        const data = await response.json();
        allAthletes = data.athletes;
        eventName = data.event_name;
        
        // Update event name in header
        eventNameElement.textContent = eventName;
        
        if (allAthletes.length === 0) {
            throw new Error("No athletes found for this event");
        }
    } finally {
        showLoading(false);
    }
}

// Show loading spinner
function showLoading(isLoading) {
    loadingSpinner.style.display = isLoading ? 'block' : 'none';
    profileContent.style.display = isLoading ? 'none' : 'block';
}

// Show error message
function showError(message) {
    loadingSpinner.textContent = `Error: ${message}`;
    loadingSpinner.style.color = 'red';
    loadingSpinner.style.display = 'block';
    profileContent.style.display = 'none';
}

// Update navigation controls
function updateNavigation() {
    prevButton.disabled = currentAthleteIndex === 0;
    nextButton.disabled = currentAthleteIndex === allAthletes.length - 1;
    athleteCounter.textContent = `${currentAthleteIndex + 1} / ${allAthletes.length}`;
}

// Show previous athlete
function showPreviousAthlete() {
    if (currentAthleteIndex > 0) {
        currentAthleteIndex--;
        showAthlete(currentAthleteIndex);
        updateNavigation();
    }
}

// Show next athlete
function showNextAthlete() {
    if (currentAthleteIndex < allAthletes.length - 1) {
        currentAthleteIndex++;
        showAthlete(currentAthleteIndex);
        updateNavigation();
    }
}

// Calculate age from date of birth
function calculateAge(dob) {
    if (!dob) return null;
    
    const birthDate = new Date(dob);
    const today = new Date();
    
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    
    return age;
}

// Format date string
function formatDate(dateString) {
    if (!dateString) return "-";
    
    const date = new Date(dateString);
    return date.toLocaleDateString();
}

// Display athlete data
function showAthlete(index) {
    const athlete = allAthletes[index];
    if (!athlete) return;
    
    // Basic info
    document.getElementById('athleteName').textContent = athlete.name;
    document.getElementById('athleteBib').textContent = athlete.bib ? `BIB: #${athlete.bib}` : 'BIB: Not assigned';
    document.getElementById('athleteNationality').textContent = athlete.nationality ? `Nationality: ${athlete.nationality}` : 'Nationality: -';
    
    // Age
    const age = calculateAge(athlete.dob);
    document.getElementById('athleteAge').textContent = age ? `Age: ${age}` : 'Age: -';
    
    // Image
    const imageElement = document.getElementById('athleteImage');
    if (athlete.image) {
        imageElement.src = athlete.image;
        imageElement.alt = `Photo of ${athlete.name}`;
    } else {
        imageElement.src = 'placeholder.png'; // Make sure you have a placeholder image
        imageElement.alt = 'No photo available';
    }
    
    // Stats
    document.getElementById('totalEvents').textContent = athlete.stats.total_events || '0';
    document.getElementById('totalSeries').textContent = athlete.stats.total_series || '0';
    
    // Best results by points
    if (athlete.stats.best_result_by_points) {
        const bestPoints = athlete.stats.best_result_by_points;
        document.getElementById('bestResultByPoints').textContent = 
            `${bestPoints.points} points at ${bestPoints.event_name} (${formatDate(bestPoints.date)})`;
    } else {
        document.getElementById('bestResultByPoints').textContent = '-';
    }
    
    // Best results by rank
    if (athlete.stats.best_result_by_rank) {
        const bestRank = athlete.stats.best_result_by_rank;
        document.getElementById('bestResultByRank').textContent = 
            `${bestRank.place}. Place at ${bestRank.event_name} (${formatDate(bestRank.date)})`;
    } else {
        document.getElementById('bestResultByRank').textContent = '-';
    }
    
    // Oldest result
    if (athlete.stats.oldest_result) {
        const oldest = athlete.stats.oldest_result;
        document.getElementById('oldestResult').textContent = 
            `${oldest.event_name} (${formatDate(oldest.date)})`;
    } else {
        document.getElementById('oldestResult').textContent = '-';
    }
    
    // Best series
    if (athlete.stats.best_series) {
        const bestSeries = athlete.stats.best_series;
        document.getElementById('bestSeriesResult').textContent = 
            `${bestSeries.place}. Place in ${bestSeries.series_name}`;
    } else {
        document.getElementById('bestSeriesResult').textContent = '-';
    }
    
    // Pro stats
    if (athlete.stats.best_pro_series) {
        const bestProSeries = athlete.stats.best_pro_series;
        document.getElementById('bestProSeries').textContent = 
            `${bestProSeries.place}. Place in ${bestProSeries.series_name}`;
    } else {
        document.getElementById('bestProSeries').textContent = '-';
    }
    
    if (athlete.stats.best_pro_event) {
        const bestProEvent = athlete.stats.best_pro_event;
        document.getElementById('bestProEvent').textContent = 
            `${bestProEvent.points} points at ${bestProEvent.event_name}`;
    } else {
        document.getElementById('bestProEvent').textContent = '-';
    }
    
    // Challenger stats
    if (athlete.stats.best_challenger_series) {
        const bestChallengerSeries = athlete.stats.best_challenger_series;
        document.getElementById('bestChallengerSeries').textContent = 
            `${bestChallengerSeries.place}. Place in ${bestChallengerSeries.series_name}`;
    } else {
        document.getElementById('bestChallengerSeries').textContent = '-';
    }
    
    if (athlete.stats.best_challenger_event) {
        const bestChallengerEvent = athlete.stats.best_challenger_event;
        document.getElementById('bestChallengerEvent').textContent = 
            `${bestChallengerEvent.points} points at ${bestChallengerEvent.event_name}`;
    } else {
        document.getElementById('bestChallengerEvent').textContent = '-';
    }
    
    // Series results
    const seriesContainer = document.getElementById('seriesResultsContainer');
    seriesContainer.innerHTML = '';
    
    if (athlete.series_results && athlete.series_results.length > 0) {
        // Sort series by year (newest first)
        const sortedSeries = [...athlete.series_results].sort((a, b) => b.series_year - a.series_year);
        
        sortedSeries.forEach(series => {
            // Create series card
            const seriesCard = document.createElement('div');
            seriesCard.className = 'series-card';
            
            // Series header
            const seriesHeader = document.createElement('div');
            seriesHeader.className = 'series-header';
            seriesHeader.textContent = series.series_name;
            seriesCard.appendChild(seriesHeader);
            
            // Series info
            const seriesInfo = document.createElement('div');
            seriesInfo.className = 'series-info';
            seriesInfo.innerHTML = `
                <div><strong>Division:</strong> ${series.division_name || '-'}</div>
                <div><strong>Place:</strong> ${series.place || '-'}</div>
                <div><strong>Points:</strong> ${series.points || '-'}</div>
            `;
            seriesCard.appendChild(seriesInfo);
            
            // Events
            if (series.events && series.events.length > 0) {
                const eventList = document.createElement('div');
                eventList.className = 'event-list';
                
                // Sort events by place
                const sortedEvents = [...series.events].sort((a, b) => {
                    if (a.place === null || a.place === undefined) return 1;
                    if (b.place === null || b.place === undefined) return -1;
                    return a.place - b.place;
                });
                
                sortedEvents.forEach(event => {
                    const eventItem = document.createElement('div');
                    eventItem.className = 'event-item';
                    
                    const eventName = document.createElement('div');
                    eventName.className = 'event-name';
                    eventName.textContent =
                   eventItem.appendChild(eventName);
                   
                   const eventDate = document.createElement('div');
                   eventDate.className = 'event-date';
                   eventDate.textContent = formatDate(event.date);
                   eventItem.appendChild(eventDate);
                   
                   const eventPlace = document.createElement('div');
                   eventPlace.className = 'event-place';
                   eventPlace.textContent = event.place !== null ? `${event.place}.` : '-';
                   eventItem.appendChild(eventPlace);
                   
                   const eventPoints = document.createElement('div');
                   eventPoints.className = 'event-points';
                   eventPoints.textContent = event.points !== null ? event.points : '-';
                   eventItem.appendChild(eventPoints);
                   
                   eventList.appendChild(eventItem);
               });
               
               seriesCard.appendChild(eventList);
           }
           
           seriesContainer.appendChild(seriesCard);
       });
   } else {
       const noResults = document.createElement('p');
       noResults.textContent = 'No series results found.';
       noResults.style.textAlign = 'center';
       noResults.style.padding = '1rem';
       noResults.style.color = '#666';
       seriesContainer.appendChild(noResults);
   }
}