from media import Media

class Series(Media):
    def __init__(self,name,director,IMDB_score,url,duration,casts,genre,release_year,episode):
        super().__init__(name,director,IMDB_score,url,duration,casts,genre,release_year)
        self.episode = episode
