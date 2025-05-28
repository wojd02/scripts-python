import unittest
def get_daily_movies():
    print('Retrieving the movie set to play on today\'s flight...')
    return ['Parasite', 'Nomadland', 'Roma', 'Black Widow', 'Spiral']


def get_licensed_movies():
    print('Retrieving the list of licenses movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movies = get_daily_movies()
    licensed_movies = get_licensed_movies()

    # Write your code below:
    for movie in daily_movies:
      print(movie)
      with self.subTest(movie): # subTest() vai fazer com que cada iteração do loop seja um teste único. E não vai parar no primeiro erro que ocorrer.
        self.assertIn(movie, licensed_movies)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)