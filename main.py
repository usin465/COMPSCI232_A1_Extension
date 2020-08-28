import datetime;
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, obj):
        if self.__director_full_name == obj.__director_full_name:
            return True
        else:
            return False

    def __lt__(self, obj):
        return (self.__director_full_name < obj.__director_full_name)

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:

    def __init__(self, genre: str):
        if genre == "" or type(genre) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre.strip()

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __lt__(self, obj):
        return (self.__genre_name < obj.__genre_name)

    def __eq__(self, obj):
        return (self.__genre_name == obj.__genre_name)

    def __hash__(self):
        return hash(self.__genre_name)


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__actor_colleagues = list()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, obj):
        if self.__actor_full_name == obj.__actor_full_name:
            return True
        else:
            return False

    def __lt__(self, obj):
        return (self.__actor_full_name < obj.__actor_full_name)

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if colleague not in self.__actor_colleagues:
            self.__actor_colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__actor_colleagues:
            return True
        else:
            return False


class Movie:
    def __init__(self, t: str, year: int):
        if t == "" or type(t) is not str:
            self.__title = None
        else:
            self.__title = t.strip()
        if year >= 1900:
            self.__release_year = year
        else:
            self.__release_year = None
        self.__description = None
        self.__director = None
        self.__actors = list()
        self.__genres = list()
        self.__runtime_minutes = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, t):
        if t == "" or type(t) is not str:
            self.__title = None
        else:
            self.__title = t.strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, d):
        if d == "" or type(d) is not str:
            self.__description = None
        else:
            self.__description = d.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, dire=Director):
        self.__director = dire

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, ac_list):
        self.__actors = ac_list

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, ac_list):
        self.__genres = ac_list

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, mins: int):
        if mins >= 0:
            self.__runtime_minutes = mins
        else:
            raise ValueError

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, obj):
        return (self.__title, self.__release_year) == (obj.__title, obj.__release_year)

    def __lt__(self, obj):
        return (self.__title, self.__release_year) < (obj.__title, obj.__release_year)

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    def add_actor(self, ac):
        if ac not in self.__actors:
            self.__actors.append(ac)

    def remove_actor(self, ac):
        if ac in self.__actors:
            self.__actors.remove(ac)

    def add_genre(self, g):
        if g not in self.__genres:
            self.__genres.append(g)

    def remove_genre(self, g):
        if g in self.__genres:
            self.__genres.remove(g)


class Review:
    def __init__(self,m : Movie, r: str, rate : int):
        self.__movie = m
        self.__review_text = r
        self.__rating = None
        if rate > 0 and rate <= 10:
            self.__rating = rate
        self.__timestamp = datetime.datetime.now().timestamp()

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        readable = datetime.datetime.fromtimestamp(self.__timestamp).isoformat()
        return readable
    def __repr__(self):
        return f"{self.__movie}"

    def __eq__(self, other):
        return (self.__timestamp,self.__review_text,self.__movie, self.__rating) == (other.__timestamp,other.__review_text,other.__movie,other.__rating)


class User:
    def __init__(self, user:str,passw:str):
        if user == "" or type(user) is not str:
            self.__user_name = None
        else:
            user.strip()
            self.__user_name = user.lower()
        self.__password = passw
        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self,news:str):
        self.__user_name = news

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, newp:str):
        self.__password = newp

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, a_list):
        self.__watched_movies = a_list

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, a_list):
        self.__reviews = a_list

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self,newt):
        if newt >= 0:
            self.__time_spent_watching_movies_minutes = newt

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self,movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self,review):
        self.__reviews.append(review)

    def __eq__(self, other):
        return self.__user_name == other.__user_name



class WatchList:

    def __init__(self):
        self.__watch_list = list()
        self.__index = -1

    def add_movie(self, movie:Movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie:Movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index:int):
        if index < len(self.__watch_list):
            return self.__watch_list[index]
        else:
            return None
    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if self.__watch_list == []:
            return None
        else:
            return self.__watch_list[0]

    def __iter__(self):
        return self


    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__watch_list):
            self.__index = -1
            raise StopIteration
        else:
            return self.__watch_list[self.__index]

watchlist2 = WatchList()
watchlist2.add_movie(Movie("Ice Age", 2002))
watchlist2.add_movie(Movie("Ice Age", 2002))
print(watchlist2.size())

watchlist2 = WatchList()
print(watchlist2.first_movie_in_watchlist())

watchlist2 = WatchList()
watchlist2.add_movie(Movie("Moana", 2016))
watchlist2.add_movie(Movie("Ice Age", 2002))
watchlist2.add_movie(Movie("Guardians of the Galaxy", 2012))
watchlist2.remove_movie(Movie("Moana",2016))
print(watchlist2.select_movie_to_watch(50))

watchlist2 = WatchList()
watchlist2.add_movie(Movie("Moana", 2016))
watchlist2.add_movie(Movie("Ice Age", 2002))
watchlist2.add_movie(Movie("Guardians of the Galaxy", 2012))
watchlist2.remove_movie(Movie("Moana",2016))
print(watchlist2.select_movie_to_watch(1))
watchlist2.remove_movie(Movie("folens,",1990))

watchlist2 = WatchList()
watchlist2.add_movie(Movie("Moana", 2016))
watchlist2.add_movie(Movie("Ice Age", 2002))
watchlist2.add_movie(Movie("Guardians of the Galaxy", 2012))
watchlist2.remove_movie(Movie("Moana",2016))
print(watchlist2.select_movie_to_watch(1))

watchlist2 = WatchList()
watchlist2.add_movie(Movie("Moana", 2016))
watchlist2.add_movie(Movie("Ice Age", 2002))
watchlist2.add_movie(Movie("Guardians of the Galaxy", 2012))
watchlist2.remove_movie(Movie("Moana",2016))
for item in watchlist2:
    print(item)

watchlist2 = WatchList()
watchlist2.add_movie(Movie("Moana", 2016))
watchlist2.add_movie(Movie("Ice Age", 2002))
watchlist2.add_movie(Movie("Guardians of the Galaxy", 2012))
watchlist2.remove_movie(Movie("Moana",2016))
print(f"Size of watchlist: {watchlist2.size()}")

watchlist2 = WatchList()
watchlist2.add_movie(Movie("Moana", 2016))
watchlist2.add_movie(Movie("Ice Age", 2002))
watchlist2.add_movie(Movie("Guardians of the Galaxy", 2012))
print(f"Size of watchlist: {watchlist2.size()}")

watchlist = WatchList()
print(f"Size of watchlist: {watchlist.size()}")
watchlist.add_movie(Movie("Moana", 2016))
watchlist.add_movie(Movie("Ice Age", 2002))
watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
print(watchlist.first_movie_in_watchlist())






