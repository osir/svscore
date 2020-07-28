import csv
from typing import List

class Ranking:
    def __init__(self):
        self.entries: List[Rank] = []

    @staticmethod
    def parse_csv(lines: List[str]):
        ranking = Ranking()
        reader = csv.reader(lines, dialect='excel')
        for row in reader:
            try:
                ranking.entries.append(Rank.from_csv(row))
            except:
                continue
        return ranking


class Rank:
    def __init__(self, pos: int, competitor: str, year: int, category: str, town: str, association: str, weapon_type: str, score: float):
        if score < 0:
            raise AttributeError('Position < 0 not allowed')
        self.position: int = pos
        self.competitor: str = competitor
        self.year: int = year
        self.category: str = category
        self.town: str = town
        self.association: str = association
        self.weapon_type: str = weapon_type
        if score < 0:
            raise AttributeError('Score < 0 not allowed')
        self.score: float = score


    @staticmethod
    def from_csv(line: List[str]):
        if not len(line) == 7:
            raise IndexError('CSV does not have 7 fields')

        pos = int(line[0], 10)
        competitor = line[1]

        year_cat = line[2].split(' ')
        year = int(year_cat[0], 10)
        category = year_cat[1]

        town_assoc = line[3].split(', ')
        town = town_assoc[0]
        assoc = town_assoc[1]

        weapon = line[4]
        score = float(line[5])

        return Rank(pos, competitor, year, category, town, assoc, weapon, score)
