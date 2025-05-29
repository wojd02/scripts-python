import unittest
import login_database

user = login_database.login('jonatan', '%13q002G')
session = login_database.check_in.check_in_user_data(user)
connection_db_user = login_database.check_in.connect_db(session)
search = login_database.check_in.search_db(session)
print()

class testing_code(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        login_database.ambient.create_ambient()
    @unittest.skipUnless(session, 'usuário não permitido, permitido, executando testes')
    def test_user_data(self, connection = bool):
        connection = session
        self.assertTrue(connection)

    @classmethod
    def tearDownClass(cls):
        login_database.ambient.close_ambient()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

client = login_database.search_account_in_db('admin', '@157796%')


#adicionar = login_database.add_user('Maria', '@jsoOw02')
#db.users.append(adicionar)
#print(db.users)
#amanhã tentar armazenar o banco de dados em um txt ou fazer uma tabela