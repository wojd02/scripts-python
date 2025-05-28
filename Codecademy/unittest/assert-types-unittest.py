#TIPOS DE TESTES DO UNITTEST
import unittest
def get_daily_movie():
    print('Retrieving the movie set to play on today\'s flight...')
    return 'Parasite'
def get_licensed_movies():
    print('Retrieving the list of licensed movies from the database...')
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies
def get_wifi_status():
    print('Checking WiFi signal...')
    print('WiFi is inactive')
    return False
def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 40

def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.99999999
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = get_daily_movie()
    licensed_movies = get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies) # Verifica se o primeiro argumento esta no segundo argumento(lista)


  def test_wifi_status(self):
    wifi_enabled = get_wifi_status()
    self.assertTrue(wifi_enabled) # Verifica se o argumento tem o valor de True
  
  def test_maximum_display_brightness(self):
    brightness = get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400) # Verifica se os dois argumentos são quase iguais(arredonda a diferença em 7 casas decimais e teria que dar zero para retornar true)
  
  def test_device_temperature(self):
    device_temp = get_device_temp()
    self.assertLess(device_temp, 35) # Verifica se o primeiro valor é menor que o segundo

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)