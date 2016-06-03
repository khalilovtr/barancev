import random


class Movie(object):

    def __init__(self, title="", year="", format="DVD"):
        self.title = title
        self.year = year
        self.format = format

    @classmethod
    def random(cls):
        from random import randint
        return cls(title="Фильм№ " + str(randint(0, 10000)),
                   year=str(randint(1950, 2016)),
                   duration=str(randint(10, 250)))


