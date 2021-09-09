import unittest
from models import movie

Movie = movie.Movie

class MovieTest(unittest.TestCase):
    """
    Test class to test the behavior of movie class.
    This is by testing wether objects are actual instances of the class
    """

    def setUp(self):
        """
        Set up method that will be run before every test.
        """
        self.new_movie = Movie(1234, 'Python Must Be Crazy', 'A thrilling new Python Series',
                               'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

if __name__ == '__main__':
    unittest.main()