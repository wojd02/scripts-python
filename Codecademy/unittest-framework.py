import unittest

def get_nearest_exit(row_number):
    if row_number < 15:
        location = 'front'
    elif row_number < 30:
        location = 'middle'
    else:
        location = 'back'
    return location

class NearestExitTests(unittest.TestCase):
    def test_row_1(self):
        self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
    def test_row_20(self):
        self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
    def test_row_40(self):
        self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')

#O unittest.main() está sendo chamado diretamente no final do script. Isso pode causar problemas se o script estiver sendo executado em um ambiente como um notebook Jupyter, um IDE (como o VS Code) por isso que só chamar o unittest.main() não vai funcionar.

#O argumento argv=['first-arg-is-ignored'] evita que unittest tente interpretar argumentos do sistema (como -f ou --ip) que podem existir em notebooks ou ambientes interativos.
#O argumento exit=False impede que o kernel do ambiente interativo seja finalizado após os testes.
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)