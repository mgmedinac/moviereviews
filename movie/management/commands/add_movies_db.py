from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help='load movies from movie_descriptions.json into the Movie model'

    def handle(self,*age, **kwargs):
        #construct the full path to the JSON file
        #recuerde que la consola está ubicada en la carpeta DjangoprojectBase.
        #El path del archivo movie_descriptions con respecto a DjangoProjectBase sería la carpeta anteriro
        json_file_path= 'movie/management/commands/movies.json'

        #load data from JSON file
        with open(json_file_path,'r')as file:
            movies = json.load(file)

        #add products to the database:

        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title= movie['title']).first()#se asegura que la pelicula no exista en la base de datos 
            if not exist:
                Movie.objects.create(title = movie['title'],
                                     image = 'movie/image/default.jpg',
                                     genre = movie ['genre'],
                                     year = movie ['year'])
   