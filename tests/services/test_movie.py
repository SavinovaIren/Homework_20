import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all()
        assert len(movie) > 0

    def test_create(self):
        movie_d = {"id": 2, "name": "Oleg"}
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_update(self):
        movie = self.movie_service.update(1)
        assert movie is not None

    def test_delete(self):
        movie = self.movie_service.delete(1)
        assert movie is None