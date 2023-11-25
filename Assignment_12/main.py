from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from database import Database
from database import MOVIE_LIST

class Media_management:
    def __init__(self,id,name,score,duration):
        self.id = id
        self.name = name
        self.score = score
        self.duration = duration

    @staticmethod
    def show_menu():
        print("1.Add")
        print("2.Edit")
        print("3.Remove")
        print("4.Search")
        print("5.Search by time")
        print("6.Show movie info")
        print("7.Download")
        print("8.Exit")

    @staticmethod
    def add():
        choice = int(input("1.film 2.series 3.Documentary 4.clip \nwhat do you want add:"))
        name = str(input("Please enter your movie name: "))
        director = str(input("Please enter your director name: "))
        IMDB_score = float(input("Please enter IMDB score movie: "))
        url = str(input("Please enter your movie url: "))
        duration = int(input("Please enter your movie duration(enter minute): "))
        name_actor = str(input("Please separate the names with (,)\nPlease enter your movie actors: "))
        name_actor = list(name_actor.split(","))
        genre = str(input("Please separate the names with (,)\nPlease enter your movie genre: "))
        genre = list(genre.split(","))
        release_year = int(input("Please enter your movie release year: "))

        if choice == 1:
            new_movie = Film(name,director,IMDB_score,url,duration,name_actor,genre,release_year)

        elif choice == 2:
            episode = int(input("Please enter number of episode: "))
            new_movie = Series(name,director,IMDB_score,url,duration,name_actor,genre,release_year,episode)

        elif choice == 3:
            new_movie = Documentary(name,director,IMDB_score,url,duration,name_actor,genre,release_year)

        elif choice == 4:
            new_movie = Clip(name,director,IMDB_score,url,duration,name_actor,genre,release_year)

        else:
            print("We dont have another type of movie")
            return

        MOVIE_LIST.append(new_movie)
        print("movie add successful.")

    @staticmethod
    def edit():
        name = str(input("Please enter your movie want edit:"))
        for movie in MOVIE_LIST:
            if movie.name == name:
                if isinstance(movie, Series):
                    print(f"{movie.name}  {movie.director}  {movie.IMDB_score}  {movie.url}  {movie.duration}  {movie.casts}  {movie.genre}  {movie.release_year}  {movie.episode}")
                    edit_attribute = int(input("1.name  2.director  3.IMDB_score  4.url  5.duration  6.actors  7.genre  8.release_year  9.episode\nwhich you want:"))
                else:
                    print(f"{movie.name}  {movie.director}  {movie.IMDB_score}  {movie.url}  {movie.duration}  {movie.casts}  {movie.genre}  {movie.release_year}")
                    edit_attribute = int(input("1.name  2.director  3.IMDB_score  4.url  5.duration  6.actors  7.genre  8.release_year\nwhich you want:"))

                new_attribute = input("Please enter new value: ")
                if edit_attribute == 1:
                    movie.name = new_attribute
                elif edit_attribute == 2:
                    movie.director = new_attribute
                elif edit_attribute == 3:
                    movie.IMDB_score = float(new_attribute)
                elif edit_attribute == 4:
                    movie.url = new_attribute
                elif edit_attribute == 5:
                    movie.duration = int(new_attribute)
                elif edit_attribute == 6:
                    movie.actors = list(new_attribute.split(","))
                elif edit_attribute == 7:
                    movie.genre = list(new_attribute.split(","))
                elif edit_attribute == 8:
                    movie.release_year = int(new_attribute)
                elif edit_attribute == 9 and isinstance(movie, Series):
                    movie.episode = int(new_attribute)
                print("operation successful")
                return 
            else:
                print("We dont have this movie!")  

    @staticmethod
    def remove():
        global MOVIE_LIST
        name = str(input("Please enter your movie want remove:"))
        for movie in MOVIE_LIST:
            if movie.name == name:
                new_products = [movie for movie in MOVIE_LIST if movie.name != name]
                MOVIE_LIST = new_products
                print("operation successful")
                return
        else:
            print("We dont have this movie!")
            return

    @staticmethod
    def search():
        user_want = input("Please enter your movie name: ")
        for row in MOVIE_LIST:
            if row.name == user_want:
                if isinstance(row,Series):
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.casts}  {row.genre}  {row.release_year}  {row.episode}")
                    break
                else:
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.casts}  {row.genre}  {row.release_year}")
                    break
        else:
            print("We dont have this movie!")

    @staticmethod
    def search_by_time():
        user_time_a = int(input("Please enter your movie time zone(smaller time): ")) - 1
        user_time_b = int(input("Please enter your movie time zone(bigger time): ") ) + 1
        for row in MOVIE_LIST:
            if int(row.duration) >= user_time_a and int(row.duration) <= user_time_b:
                if isinstance(row,Series):
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.casts}  {row.genre}  {row.release_year}  {row.episode}")
                else:
                    print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.casts}  {row.genre}  {row.release_year}")

    @staticmethod
    def show_info():
        for row in MOVIE_LIST:

            if isinstance(row,Series):
                print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.casts}  {row.genre}  {row.release_year}  {row.episode}")
            else:
                print(f"{row.name}  {row.director}  {row.IMDB_score}  {row.url}  {row.duration}  {row.casts}  {row.genre}  {row.release_year}")

    def download(self):
        ...

print("Loading")
Database.read()
print("Loading complete")

while True:
    Media_management.show_menu()
    choice = int(input("what do yo want? "))

    if choice == 1:
        Media_management.add() 

    elif choice == 2:
        Media_management.edit()
        
    elif choice == 3:
        Media_management.remove()
    
    elif choice == 4:
        Media_management.search()

    elif choice == 5:
        Media_management.search_by_time()

    elif choice == 6:
        Media_management.show_info()

    elif choice == 7:
        Media_management.download()

    elif choice == 8:
        print("Thank you for choosing us")
        Database.write()
        exit(0)

    else:
        print("Enter number between 1 and 8")
