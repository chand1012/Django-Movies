from movies.util.fake_model import FakeMovie

def parse_movies(x: list[tuple]) -> list[FakeMovie]:
    final = []
    for item in x:
        final.append(FakeMovie(item[0], item[1], item[2], item[3]))
    return final
