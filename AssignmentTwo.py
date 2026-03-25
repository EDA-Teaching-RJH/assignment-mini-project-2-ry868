#Movie database 
import re
import csv

class Movie:
    def __init__ (self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating

    def __str__ (self):
        return f"{self.title} ({self.year}) - {self.genre}, Rating: {self.rating}"
        #returns all details of the movie

class MovieDatabase:
    def __init__ (self):
        self.movies = []
        #list of movies

    #viewing all movies currently in the database
    def view_movies(self):
       if not self.movies:
           print("No movies in database")
           return
       for movie in self.movies:
           print(movie)

    #adding movies with all its details then checking if valid
    def add_movie(self, movie):
        self.movies.append(movie)
        #allows for you to add movies

    #search a movie by either naming the title or using a word
    def search_movie(self, term):
        matches = []
        for movie in self.movies:
            if re.search(term, movie.title, re.IGNORECASE):
                matches.append(movie)
        if matches:
            for movie in matches:
                print(movie)
        else:
            print("No matching terms")

    #View list of movies by rating, using lambda to take the movies and return the sorted ratings 
    def sort_rating(self):
        sorted_ratings = sorted(self.movies, key=lambda movie: movie.rating, reverse=True)
        for ratings in sorted_ratings:
            print(ratings)
    
    #load files from the csv
    def load_file(self, csvfile):
        with open(csvfile, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.movies.append(Movie(*row))

    #saves new movies to csv
    def save_to_file(self, csvfile):
        with open(csvfile, "w", newline="") as f:
            writer = csv.writer(f)
            for movie in self.movies:
                writer.writerow([movie.title, movie.year, movie.genre, movie.rating]) 

#This section is to be able to validate data (year, genre, rating)
def valid_year(year):
    if re.search(r"^\d{4}$", year):
        return True
    return False

validGenres = ["Action",
               "Adventure",
               "Animation",
               "Comedy",
               "Crime",
               "Drama",
               "Fantasy",
               "Horror",
               "Mystery",
               "Psychological Drama",
               "Romance",
               "Sci-Fi",
               "Thriller"]

#Using REGEX so that it only allows any letter including a hyphen then returns to validGenre to check 
def valid_genre(genre):
    if not re.search(r"^[a-zA-Z\- ]+$", genre):
        return False
    return genre.title() in validGenres

#Using REGEX making it only allow 10 or any number with a decimal and the question mark making it optional
def valid_rating(rating):
    if re.search(r"^(10|[0-9](\.[0-9])?)$", rating):
        return True
    else:
        return False

#Main menu 
def menu():

    #Set class as one variable to store and manage movies
    mdb = MovieDatabase()
    mdb.load_file("movies.csv")

    while True:
        print("""
        Movie database: 
        1. View Movies
        2. Add Movie
        3. Search Movie
        4. Sort by Rating
        5. Save and Exit
        6. Exit without Saving""")

        select = input("\nSelect Option: ")

        if select == "1":
            mdb.view_movies()

        elif select == "2":
            title = input("Movie title: ").strip().title()
            year = input("Year: ")
            if not valid_year(year):
                print("Invalid Year inputted")
                continue

            genre = input("Genre: ").strip().title()
            if not valid_genre(genre):
                print("Invalid genre")
                print("Valid genres: ")
                for genres in validGenres:
                    print(genres)
                continue

            rating = input("Rating: ")
            if not valid_rating(rating):
              print("Invalid rating")
              continue

            movie = Movie(title, year, genre, rating)
            print("Movie successfully added")
            mdb.add_movie(movie)

        elif select == "3":
            term = input("Search by term: ")
            mdb.search_movie(term)

        elif select == "4":
            mdb.sort_rating()

        elif select == "5":
            mdb.save_to_file("movies.csv")
            print("Database saved")
            break

        elif select == "6":
            break
        
        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()