
class Event:
    def __init__(self, name: str, year: int, iteration: int, organisation: str):
        self.name = name
        self.year = year
        self.iteration = iteration
        self.organisation = organisation

    def get_fullname(self):
        if self.iteration:
            return f'{self.iteration}. {self.name} {self.year} - {self.organisation}'
        else:
            return f'{self.name} {self.year} - {self.organisation}'
