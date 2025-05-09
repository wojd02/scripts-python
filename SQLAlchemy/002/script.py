from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy import ForeignKey

#criando o banco de dados
db = create_engine("sqlite:///SQLAlchemy/002/banco.db")

#session é utilizado para fazer entradas de dados no BD
Session = sessionmaker(bind=db)
session = Session()

#Criando as tabelas
base = declarative_base()

class Usuario(base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    status = Column("status", Boolean)

    def __init__(self, nome, email, senha, status=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.status = status

class Livro(base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column("titulo", String)
    qtd_pags = Column("qtd_pags", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtd_pags, dono):
        self.titulo = titulo
        self.qtd_pags = qtd_pags
        self.dono = dono

base.metadata.create_all(bind=db)
#CRUD(create, read, update and delete) cadastrando dados

#READ
usuario_procura = session.query(Usuario).filter_by(id="1").first()
print(usuario_procura.nome)
print(usuario_procura.email)
print(usuario_procura.senha)
print(usuario_procura.status)

#CREATE
#usuario = Usuario(nome = "Cara", email="caradbh@gmail.com", senha="androidslives22")
#session.add(usuario)
#session.commit()

#livro = Livro(titulo = 'A casa negra', qtd_pags= '690', dono=usuario_cara.id)
#session.add(livro)
#session.commit()

#UPDATE
#usuario_procura.nome = 'Ana Clara'
#session.add(usuario_procura)
#session.commit()

#DELETE
#session.delete(usuario_procura)
#session.commit()

