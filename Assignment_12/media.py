class Media:
    def __init__(self,name,director,IMDB_score,url,duration,casts,genre,release_year):
        self.name = name
        self.director = director
        self.IMDB_score = IMDB_score
        self.url = url
        self.duration = duration
        self.casts = [casts]
        self.genre = [genre]
        self.release_year = release_year
