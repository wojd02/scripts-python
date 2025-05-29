class wifi:
    def connect():
        print('checking network connection')
    def end():
        print('ending network connection')

class login:
    def __init__(self, user, password):
        self._user = user
        self._password = password  

class db():
    users = [{'user': 'jonatan','password': '%13q002G'},
        {'user': 'admin','password': '@157796%'},
        {'user': 'Kara_wire','password': '53MN23*!'}
        ]
    

def add_user(user = str, password = str): #código básico para adicionar um usuario na lista, mas n serve para o que preciso :(
    return {'user': user, 'password': password}

def search_account_in_db(user, password):
        for c in db.users:
            if c['user'] == user and c['password'] == password:
                print(f'Bem-vindo(a) {user}, seu login foi efetuado com sucesso!')
                break
        else:
            print('ERROR! Sua combinação de login não foi encontrada, verifique usuário e senha e tente novamente!')

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
