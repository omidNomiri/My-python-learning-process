from actor import Actor

class Media(Actor):
    def __init__(self,name,director,IMDB_score,url,duration,genre,release_year,actor):
        super().__init__(actor)
        self.name = name
        self.director = director
        self.IMDB_score = IMDB_score
        self.url = url
        self.duration = duration
        self.genre = genre
        self.release_year = release_year
