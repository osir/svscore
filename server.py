#!/usr/bin/env python3

from datetime import datetime, timezone, timedelta

from flask import Flask
from flask import render_template
from flask import g
from competition.event import Event
from competition.ranking import Ranking, Rank
from competition.scoreapi import ScoreAPI, FileScoreAPI

app = Flask(__name__)
config_loaded = False
cache = (None, None)


@app.before_request
def init():
    global config_loaded
    app.config.from_pyfile('config.py')

    # Check config was loaded
    if not 'EVENT_NAME' in app.config:
        config_loaded = False
        return
    config_loaded = True

    if app.config['DEBUG_USE_FAKE_SERVER']:
        g.api = FileScoreAPI(app.config['DEBUG_FAKE_SERVER_PATH'], app.config['SCORING_SERVER_ENCODING'])
    else:
        g.api = ScoreAPI(app.config['SCORING_SERVER_URL'], app.config['SCORING_SERVER_ENCODING'])

    g.event = Event(app.config['EVENT_NAME'],
        app.config['EVENT_YEAR'],
        app.config['EVENT_ITERATION'],
        app.config['EVENT_ORGANISER'])


@app.route('/')
def route_home():
    err = None
    if not config_loaded:
        err = Exception('Could not load config')

    try:
        return render_ranking(err=err)
    except Exception as e:
        return render_ranking(e)


@app.route('/api/lastupdate')
def route_api_lastupdate():
    return g.api.get_last_modified().isoformat()


def render_ranking(err : Exception = None):
    global cache
    if err:
        # Show the cached version or the error if the cache is empty
        if len(cache) <= 0 or not cache[1]:
            return render_template('error.html', err=err)
        update_time = cache[0]
        update_time = datetime.now()
        ranking = cache[1]
    else:
        # Show the cached version or the error if the cache is empty
        try:
            update_time, ranking = g.api.get_scores()
            cache = (update_time, ranking)
        except Exception as e:
            return render_template('error.html', err=e)

    return render_template('ranking.html', ranking=ranking, update_time=update_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
