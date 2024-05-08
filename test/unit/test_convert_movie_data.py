

from unittest import TestCase
from rag_pipeline.utility.movie_data import process_movie_data


class TestDEUtility(TestCase):

    def test_one_movie_data_processing(self):
        
        known_types = [
            "Action",
            "Adult",
            "Adventure",
            "Animation",
            "Biography",
            "Comedy",
            "Crime",
            "Documentary",
            "Drama",
            "Family",
            "Fantasy",
            "Game-Show",
            "History",
            "Horror",
            "Lifestyle",
            "Music",
            "Musical",
            "Mystery",
            "New",
            "Reality-TV",
            "Romance",
            "Sci-Fi",
            "Short",
            "Sport",
            "Talk-Show",
            "Thriller",
            "War",
            "Western"
        ]
        movie_data = [
            '"a title" (2013)',
            " A plot line. This can be multiple sentences ",
        ] + ["0"] * len(known_types)

        movie_data[2+4] = "1"
        expected_processed_data = {
            "content": "A plot line. This can be multiple sentences",
            "meta": {
                "title": '"a title" (2013)',
                "movie_types": "Biography"
            }
        }

        actual_processed_data = process_movie_data(movie_data, known_types)

        self.assertDictEqual(expected_processed_data, actual_processed_data)