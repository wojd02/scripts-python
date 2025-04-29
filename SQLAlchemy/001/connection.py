from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:my_pw@localhost:3308/cinema')

conn = engine.connect()
response = conn.exec_driver_sql('SELECT * FROM filmes;')

for row in response:
    print(row)
