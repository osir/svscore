### EVENT ###

EVENT_NAME = 'Schiessen'
EVENT_YEAR = 2020
EVENT_ITERATION = 1
EVENT_ORGANISER = 'Verein'


### INTERFACE ###

# Offset from UTC in hours, no sign is equivalent to '+', examples: +2, 3, -1
TIME_UTC_OFFSET = 2

# How many decimal places to display on the scoreboard (can be 0)
SCORE_DECIMALS = 0

# How long to wait between intervals
SCROLL_INTERVAL_MS = 20
# How many pixels every interval the scoreboard should scroll down
SCROLL_DISTANCE_PX = 1
# How long to wait at the top of the page before starting to scroll
SCROLL_WAIT_TOP_S = 6
# How long to wait at the bottom of the page before jumping to top
SCROLL_WAIT_BOTTOM_S = 3


### SERVER ###

# URL of the scoring server, including scheme (e.g. 'http://')
SCORING_SERVER_URL = 'https://scoring.server/scores.csv'
# Encoding of the file the scoring server sends
SCORING_SERVER_ENCODING = 'utf-16'


### DEBUG ###

# Whether or not to use a local file instead of the scoring server
DEBUG_USE_FAKE_SERVER = False
# The location of the file to be used instead of contacting the scoring server
DEBUG_FAKE_SERVER_PATH = '/tmp/fake-scores.txt'
