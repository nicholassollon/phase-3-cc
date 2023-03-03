class Movie:

    all = []

    def __init__(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception(
                "Titles must be of string type and at least 1 char.")

        self.reviews = []
        self.reviewers = []
        Movie.add_movie(self)

    # title property goes here!
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception(
                "Titles must be of string type and at least 1 char.")

    def average_rating(self):
        average = 0
        for review in self.reviews:
            average += review
        return average/len(self.reviews)

    @classmethod
    def highest_rated(cls):
        highest = cls.all[0]
        for movie in cls.all:
            if highest.average_rating() < movie.average_rating():
                highest = movie
        return highest

    @classmethod
    def add_review(cls, review):
        cls.reviews.append(review)

    @classmethod
    def add_movie(cls, movie):
        cls.all.append(movie)
