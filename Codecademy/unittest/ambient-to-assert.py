import unittest
class wifi:
    def connect():
        print('checking network connection')
    
    def end():
        print('ending network connection')

class login:
    def __init__(self, user, password):
        self._user = user
        self._password = password  

class check_in(login):
    def check_in_user_data(self):
        user_in_db = self._user
        password_in_db = self._password
        user_db = 'admin'
        password_db = '@157796%'
        if password_in_db == password_db and user_in_db == user_db:
            return True
        else:
            return False                        
    
    def connect_db(connection = bool):
        if connection == True:
            print('LOADING....')
            print('connecting to database...')
        else:
            print('ERROR, please check your password')
    
    def search_db(connection = bool):
        if connection is True:
            print('Searching your data in our Data Base')
        else:
            print('ACCESS DENIED!')

class ambient:
    def create_ambient():
        wifi.connect()
        print('Creating a safe ambient...')
    
    def close_ambient():
        print('Closing the ambient...')
        wifi.end()

user = login('admin', '@157796%')
session = check_in.check_in_user_data(user)
connection_db_user = check_in.connect_db(session)
search = check_in.search_db(session)
print()
class testing_code(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        ambient.create_ambient()
    
    def test_user_data(self, connection = bool):
        connection = session
        self.assertTrue(connection)

    @classmethod
    def tearDownClass(cls):
        ambient.close_ambient()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)