class Review:

    def __init__(self, viewer, movie, rating):
        self._viewer = viewer
        self._movie = movie
        if type(rating) == int:
            if rating < 6 and rating > 0:
                self._rating = rating
            else:
                raise Exception("Rating must be between 1-5")
        else:
            raise Exception("Rating must be an integer")

        self.add_viewer_to_movie()
        self.add_movie_to_viewer()
        self.add_review_to_viewer()
        self.add_viewer_to_movie()

    # properties

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer must be of class Viewer")

    @property
    def movie(self):
        return self._movie

    @movie.setter
    def movie(self, movie):
        import Movie
        if isinstance(movie, Movie):
            self._movie = movie
            Movie.add_review(self)
        else:
            raise Exception("Movie must be of class Movie")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if type(rating) == int:
            if rating < 6 and rating > 0:
                self._rating = rating
            else:
                raise Exception("Rating must be between 1-5")
        else:
            raise Exception("Rating must be an integer")

    def add_viewer_to_movie(self):
        if self._viewer not in self._movie.reviewers:
            self._movie.reviewers.append(self._viewer)

    def add_movie_to_viewer(self):
        if self._movie not in self._viewer.reviewed_movies:
            self._viewer.reviewed_movies.append(self._movie)

    def add_review_to_movie(self):
        self._movie.reviews.append(self)

    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)
