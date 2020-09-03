import csv

from main import Movie
from main import Actor
from main import Genre
from main import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.dataset_of_movies = set()
        self.dataset_of_actors = set()
        self.dataset_of_directors = set()
        self.dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                actor = row['Actors']
                director = row['Director']
                genres = row['Genre']
                actorlist = actor.split(',')
                genrelist = genres.strip().split(',')
                for a in actorlist:
                    if a[0] == " ":
                        a = a[1:]
                    a = Actor(a)
                    if a not in self.dataset_of_actors:
                        self.dataset_of_actors.add(a)
                if director[0] == " ":
                    director = director[1:]
                director = Director(director)
                if director not in self.dataset_of_directors:
                    self.dataset_of_directors.add(director)
                for genre in genrelist:
                    if genre[0] == " ":
                        genre = genre[1:]
                    genre = Genre(genre)
                    if genre not in self.dataset_of_genres:
                        self.dataset_of_genres.add(genre)

                if title[0] == " ":
                    title = title[1:]
                self.dataset_of_movies.add(Movie(title,int(row['Year'])))
                release_year = int(row['Year'])
                print(f"Movie {index} with title: {title}, release year {release_year}")
                index += 1

filename = 'Data1000Movies.csv'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()

print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
all_directors_sorted = sorted(movie_file_reader.dataset_of_movies)
print(f'first 3 unique directors of sorted dataset: {all_directors_sorted[0:3]}')


