class Viewer:

    all_users = set()

    def __init__(self, username):
        user_check = False
        if type(username) == str:
            if len(username) > 5 and len(username) < 17:
                for user in Viewer.all_users:
                    if user == username:
                        user_check = False
                        raise Exception("User already exists.")
            else:
                raise Exception("Username must be 6-16 characters.")
            if not user_check:
                self._username = username
                Viewer.all_users.add(username)
        else:
            raise Exception("Usernames must be of String class")
        self.reviews = []
        self.reviewed_movies = []

    # username property goes here!

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        user_check = False
        if type(username) == str:
            if len(username) > 5 and len(username) < 17:
                for user in Viewer.all_users:
                    if user == username:
                        user_check = False
                        raise Exception("User already exists.")
            else:
                raise Exception("Username must be 6-16 characters.")
            if not user_check:
                self._username = username
                Viewer.all_users.add(username)
        else:
            raise Exception("Usernames must be of String class")

    def reviewed_movie(self, movie):
        for reviewed in self.reviewed_movies:
            if (reviewed == movie):
                return True
        return False

    def rate_movie(self, movie, rating):
        from lib.Review import Review
        if movie in self.reviewed_movies:
            for review in self.reviews:
                if review.viewer.username == self.username:
                    review.rating = rating
        else:
            self.reviews.append(Review(self, movie, rating))
