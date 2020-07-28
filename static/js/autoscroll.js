// Settings
let interval = 0
let distance = 0
let waitTop = 0
let waitBottom = 0

// Globals
let scrollOptions = { behavior: 'smooth' }
let scrolling = false
let lastUpdate = null

/*
 * Keyboard shortcuts:
 * P - Pause/Continue autoscroll
 * R - Refresh Page
 * T - Go to top and stop there
 */
document.addEventListener('keyup', (e) => {
    if (e.code === 'KeyP') {
        toggleScroll()
        e.preventDefault()
    }
    if (e.code === 'KeyR') {
        location = location // reloads the page
        e.preventDefault()
    }
    if (e.code === 'KeyT') {
        stopScroll()
        window.scrollTo(0, 0)
        e.preventDefault()
    }
    // else let the browser handle the key normally
});

// Set all the settings and start scrolling
const initScroll = (ms, px, top, bottom) => {
    interval = ms
    distance = px
    waitTop = top
    waitBottom = bottom
    lastUpdate = Date.now()
    startScroll()
}

// Wait and continue scrolling from top
const startScroll = () => {
    scrolling = true
    window.scrollTo(0, 0)
    setTimeout(() => {
        continueScroll()
    }, waitTop);
}

let i
// Starts a new interval and continues scrolling from current position
const continueScroll = () => {
    scrolling = true
    i = setInterval(() => {
        if (window.scrollY >= window.scrollMaxY) {
            // Stop loop (interval)
            clearInterval(i)
            // Wait and start again
            setTimeout(() => {
                checkForUpdates()
                startScroll()
            }, waitBottom)
        }

        window.scrollBy(0, distance)
    }, interval)
}

// Stop scrolling at the current position and stay there
const stopScroll = () => {
    clearInterval(i)
    i = null
    scrolling = false
}

// Toggles scrolling
const toggleScroll = () => {
    console.log(scrolling)
    if (scrolling) {
        stopScroll()
    } else {
        continueScroll()
    }
}

// Checks the server and reloads if there are new scores
const checkForUpdates = () => {
    let xhr = new XMLHttpRequest()
    xhr.open('GET', '/api/lastupdate', true)
    xhr.onreadystatechange = () => {
        // If request is done, compare dates
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (new Date(lastUpdate) < new Date(xhr.response)) {
                // Server is newer, refresh
                location = location
            }
        }
    }
    xhr.send()
}
