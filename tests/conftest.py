from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director


from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO

# Создаем фикстуру с моком для DirectorDAO
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    john = Director(id=1, name="John")
    kate = Director(id=2, name="Kate")
    max = Director(id=3, name="Max")

    director_dao.get_one = MagicMock(return_value=john)
    director_dao.get_all = MagicMock(return_value=[john, kate, max])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao

#Создаем фикстуру с моком для GenreDAO
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre1 = Genre(id=1, name="Комедия")
    genre2 = Genre(id=2, name="Ужасы")
    genre3 = Genre(id=3, name="Драма")

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao

#Создаем фикстуру с моком для  MovieDAO
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie1 = Movie(id=1, title="Название 1", description="Описание 1",
                   trailer="Трейлер 1", year=2000, rating=8, genre_id=1,
                   director_id=1)
    movie2 = Movie(id=2, title="Название 2", description="Описание 2",
                   trailer="Трейлер 2", year=2001, rating=6,
                   genre_id=3, director_id=2)
    movie3 = Movie(id=3, title="Название 3", description="Описание 3",
                   trailer="Трейлер 3", year=2002, rating=4,
                   genre_id=8, director_id=5)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
