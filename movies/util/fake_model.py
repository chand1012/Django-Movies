class FakeMovie:
    movie_id: int
    title: str
    release_date: str
    imdb_id: str

    def __init__(self, movie_id: int, title: str, release_date: str, imdb_id: str):
        self.movie_id = movie_id
        self.title = title
        self.release_date = release_date
        self.imdb_id = imdb_id
