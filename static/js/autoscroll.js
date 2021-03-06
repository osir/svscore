// Globals
let timeout = null
let lastUpdate = null
let paused = false

// Config
let scrollDistance
let intervalDelay
let topDelay
let bottomDelay


const startScroll = (intervalDelayMs, scrollDistancePx, topDelayS, bottomDelayS) => {
    log('Initializing scrolling')

    // Scroll to top
    window.scrollTo(0, 0)

    // Setup globals
    lastUpdate = Date()

    // Setup shortcuts
    document.addEventListener('keyup', shortcutHandler)

    // Set config variables
    intervalDelay = intervalDelayMs
    scrollDistance = scrollDistancePx
    topDelay = topDelayS
    bottomDelay = bottomDelayS

    log('[cfg] Interval delay: ' + intervalDelay + 'ms')
    log('[cfg] Scroll distance: ' + intervalDelay + 'px')
    log('[cfg] Top waiting: ' + topDelay + 's')
    log('[cfg] Bottom waiting: ' + bottomDelay + 's')

    // Start the main interval (async)
    setInterval(mainInterval, intervalDelay)

    log('Initialization complete, mainInterval started')
    let s = ((calcMaxScroll() / scrollDistance) * 20) / 1000
    log('Estimated scroll time: ' + s + ' seconds (' + (s/60).toFixed(1) + 'min)')
}


/*
 * Keyboard shortcuts:
 * P - Pause/Continue autoscroll
 * R - Refresh Page
 * T - Go to top and stop there
 */
const shortcutHandler = (e) => {
    log('Key pressed: ' + e.code)
    if (e.code === 'KeyP') {
        paused = !paused
        e.preventDefault()
    }
    if (e.code === 'KeyR') {
        location = location // reloads the page
        e.preventDefault()
    }
    if (e.code === 'KeyT') {
        // Warning: possible race condition
        // since mainInterval is async, it might move one pixel after jumping to top
        paused = true
        window.scrollTo(0, 0)
        e.preventDefault()
    }
    // else let the browser handle the key normally
}


const mainInterval = () => {
    let pos = window.scrollY

    // If at the top, wait before scrolling
    if (pos === 0) {
        // If it isn't set yet, set the timeout to some seconds in the future
        if (timeout === null) {
            log('Entered top, waiting for timeout: ' + topDelay)
            timeout = new Date()
            timeout.setSeconds(timeout.getSeconds() + topDelay)
        }
        // If the current time has passed the timeout, start scrolling
        if (new Date() > timeout) {
            log('Timeout reached, starting to scroll')
            timeout = null
            window.scrollBy(0, scrollDistance)
        }

    // If the bottom was reached, wait before resetting and check for an update
    } else if (pos >= calcMaxScroll()) {
        // If it isn't set ye, wait before resetting and check for an updatee
        if (timeout === null) {
            log('Entered bottom, waiting for timeout: ' + bottomDelay)
            timeout = new Date()
            timeout.setSeconds(timeout.getSeconds() + bottomDelay)
            // Start checking for updates
            checkForUpdates()
        }
        // If the current time has passed the timeout, reset to the top
        if (timeout < new Date()) {
            if (!paused) {
                timeout = null
                window.scrollTo(0, 0)
            }
        }

    // Otherwise scroll normally
    } else {
        if (!paused) {
            window.scrollBy(0, scrollDistance)
        }
    }
}


// Returns the lowest scrollable coordinate of the window
// by subtracting the browser window's height from the element's height
const calcMaxScroll = () => document.body.scrollHeight - window.innerHeight


// Checks the server and reloads if there are new scores
const checkForUpdates = () => {
    log('Started checking for update')
    let xhr = new XMLHttpRequest()
    xhr.open('GET', '/api/lastupdate', true)
    xhr.onreadystatechange = () => {
        // If request is done, compare dates
        if (xhr.readyState === 4 && xhr.status === 200) {
            log('Response: ' + xhr.response)
            log('Response: ' + new Date(xhr.response))
            log('Last update: ' + lastUpdate)
            if (lastUpdate < new Date(xhr.response)) {
                log('Server is newer, reloading...')
                location = location
            } else {
                log('Nothing to update')
            }
        }
    }
    log('Sending request')
    xhr.send()
}


const log = (msg) => {
    let d = new Date()
    let t = d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds()
    console.log(t + ' ' + msg)
}
