import film as Film
import series as Series
import documentary as Documentary
import clip as Clip
import actor as Actor
import database as DB
import media as Media

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
        print("8.Exit")

    @staticmethod
    def add():
        choice = int(input("1.film 2.series 3.Documentary 4.clip \nwhat do you want add:"))
        name = str(input("Please enter your movie name: "))
        director = str(input("Please enter your director name: "))
        IMDB_score = float(input("Please enter IMDB score movie: "))
        url = str(input("Please enter your movie url: "))
        duration = int(input("Please enter your movie duration(enter minute): "))
        name_actor = str(input("Please enter your movie actors: "))
        genre = str(input("Please enter your movie genre: "))
        release_year = int(input("Please enter your movie release year: "))

        if choice == 1:
            new_movie = Film(name,director,IMDB_score,url,duration,genre,release_year)
            DB.MOVIE_LIST.append(new_movie)
        
        elif choice == 2:
            episode = int(input("Please enter number of episode: "))
            new_movie = Series(name,director,IMDB_score,url,duration,genre,release_year,episode)
            DB.MOVIE_LIST.append(new_movie)

        elif choice == 3:
            new_movie = Documentary(name,director,IMDB_score,url,duration,genre,release_year)
            DB.MOVIE_LIST.append(new_movie)

        elif choice == 4:
            new_movie = Clip(name,director,IMDB_score,url,duration,genre,release_year)
            DB.MOVIE_LIST.append(new_movie)

        PRODUCTS.append(new_movie)
        print("movie add successful.")

    def edit(self):
        choice = int(input("you want change witch one?(1.name_2.price_3.storage): "))
        if choice == 1:
            for row in PRODUCTS:
                print(row["name"],"\t",row["price"],"\t",row["storage"])
            select = input("select your product name: ")
            for row in PRODUCTS:
                if row["name"] == select:
                    new_product = input("New name: ")
                    row["name"] = new_product
            print("product edit operation success.")
        if choice == 2:
            for row in PRODUCTS:
                print(row["name"],"\t",row["price"],"\t",row["storage"])
            select = input("select your product name: ")
            for row in PRODUCTS:
                if row["name"] == select:
                    new_product = input("New price: ")
                    row["price"] = new_product
            print("product edit operation success.")
        if choice == 3:
            for row in PRODUCTS:
                print(row["name"],"\t",row["price"],"\t",row["storage"])
            select = input("select your product name: ")
            for row in PRODUCTS:
                if row["name"] == select:
                    new_product = input("New storage: ")
                    row["storage"] = new_product
            print("product edit operation success.")

    def remove(self):
        global PRODUCTS
        code = int(input("Please enter your product id: "))
        new_products = [row for row in PRODUCTS if row['code'] != code]
        PRODUCTS = new_products
        print("Remove successful.")

    def search(self):
        user_search = input("Please enter your product id or name: ")
        for product in PRODUCTS:
            if product["code"]==user_search or product["name"]==user_search:
                print(product["code"],"\t",product["name"],"\t",product["price"])
                break
        else:
            print("We dont have any product with this code or name.")

    def show_info(self):
        ...

    def download(self):
        ...

Media_management.show_menu()
choice = int(input("what do yo want? "))

if choice == 1:
    Media_management.add() 