#!/usr/bin/env python3
import ipdb;
from lib.Movie import Movie
from lib.Viewer import Viewer
from lib.Review import Review

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###


    viewer = Viewer(username="luckier_the_cat")
    movie = Movie("The Bourne Identity")
    viewer.rate_movie(movie, 3)




# DO NOT REMOVE THIS
    ipdb.set_trace()
