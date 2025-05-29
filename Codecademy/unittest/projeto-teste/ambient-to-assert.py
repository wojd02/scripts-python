import unittest
import login_database


class db():
    users = [{'user': 'jonatan','password': '%13q002G'},
        {'user': 'admin','password': '@157796%'},
        {'user': 'Kara_wire','password': '53MN23*!'}
        ]
user = login_database.login('admin', '@157796%')
session = login_database.check_in.check_in_user_data(user)
connection_db_user = login_database.check_in.connect_db(session)
search = login_database.check_in.search_db(session)
print()

class testing_code(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        login_database.ambient.create_ambient()
    
    def test_user_data(self, connection = bool):
        connection = session
        self.assertTrue(connection)

    @classmethod
    def tearDownClass(cls):
        login_database.ambient.close_ambient()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

usu = 'Kara_wire'
sen = '53MN23*!'
for c in db.users:
    if c['user'] == usu and c['password'] == sen:
        print(f'Bem-vindo(a) {usu}, seu login foi efetuado com sucesso!')
        break
else:
    print('ERROR! Sua combinação de login não foi encontrada, verifique usuário e senha e tente novamente!')

def add_user(user = str, password = str):
    return {'user': user, 'password': password}
adicionar = add_user('Maria', '@jsoOw02')
db.users.append(adicionar)
print(db.users)
#amanhã tentar armazenar o banco de dados em um txt ou fazer uma tabela