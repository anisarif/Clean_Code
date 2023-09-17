import unittest
from format_movies import format_movies
class TestFormatMovies(unittest.TestCase):
    def test_director_is_john_carpenter(self):
        # arrange
        movie = {
            "title": "Halloween",
            "director": "John Carpenter",
            "release_year": 1978,
            "classifications": ["horror"],
            "rotten_tomatoes_review": 90,
            "box_office": {
                "domestic": "$70,000,000",
                "international": "$35,000,000"
            }
        }
        data = [movie]

        # act
        result = format_movies(data)

        # assert
        self.assertEqual(result[0]['review'], 95)

    def test_movie_is_horror(self):
        # arrange
        movie = {
            "title": "Halloween",
            "director": "John Carpenter",
            "release_year": 1978,
            "classifications": ["horror"],
            "rotten_tomatoes_review": 90,
            "box_office": {
                "domestic": "$70,000,000",
                "international": "$35,000,000"
            }
        }
        data = [movie]

        # act
        result = format_movies(data)

        # assert
        self.assertEqual(result[0]['rating'], 'R')

    def test_movie_is_thriller(self):
        # arrange
        movie = {
            "title": "The Silence of the Lambs",
            "director": "Jonathan Demme",
            "release_year": 1991,
            "classifications": ["thriller"],
            "rotten_tomatoes_review": 95,
            "box_office": {
                "domestic": "$130,700,000",
                "international": "$272,700,000"
            }
        }
        data = [movie]

        # act
        result = format_movies(data)

        # assert
        self.assertEqual(result[0]['rating'], 'PG-13')

    def test_box_office_in_dollars(self):
        # arrange
        movie = {
            "title": "Jurassic Park",
            "director": "Steven Spielberg",
            "release_year": 1993,
            "classifications": ["sci-fi", "adventure"],
            "rotten_tomatoes_review": 92,
            "box_office": {
                "domestic": "$357,067,947",
                "international": "$914,691,118"
            }
        }
        data = [movie]

        # act
        result = format_movies(data)

        # assert
        self.assertEqual(result[0]['box_office'], '1,271,759,065 - $')
if __name__ == '__main__':
    unittest.main()
