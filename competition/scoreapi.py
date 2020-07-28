import requests
import os
from datetime import datetime
from typing import List, Tuple

from competition.ranking import Ranking, Rank


class ScoreAPI:
    def __init__(self, url: str, encoding: str):
        self.url = url
        self.encoding = encoding
        self._http_headers = {
            'Cache-control': 'no-cache'
        }

    # Gets the scores from an HTTP server
    def get_scores(self) -> Tuple[datetime, Ranking]:
        r = self._http_get_scores()
        timestamp = self._parse_last_modified(r.headers['Last-Modified'])
        ranking = Ranking.parse_csv(r.text.splitlines())
        return timestamp, ranking

    # Parses the server response header 'Last-Modified' and returns a datetime
    def get_last_modified(self) -> datetime:
        try:
            r = self._http_get_scores()
            return self._parse_last_modified(r.headers['Last-Modified'])
        except:
            return datetime.now()

    def _parse_last_modified(self, t: str) -> datetime:
        # This assumes the Hour, Minute and Seconds are always in the same place
        return datetime.strptime(t[17:25], '%H:%M:%S')

    def _http_get_scores(self) -> requests.Response:
        r = requests.get(self.url, headers=self._http_headers)
        r.encoding = self.encoding
        return r


class FileScoreAPI(ScoreAPI):
    def __init__(self, url: str, encoding: str):
        super().__init__(url, encoding)
    
    # Gets the scores by parsing the file as csv
    def get_scores(self) -> Tuple[datetime, Ranking]:
        with open(self.url, 'r', encoding=self.encoding) as f:
            return datetime.now(), Ranking.parse_csv(f.readlines())

    # Reads the last modified time from the file system
    def get_last_modified(self) -> datetime:
        try:
            return datetime.fromtimestamp(os.path.getmtime(self.url))
        except:
            return datetime.now()
