import pyodbc
import sqlite3
import pandas as pd
print(pyodbc.drivers())

# CONEXÃO USANDO PYODBC
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
            "Server=localhost;"
            "Database=salarios.sqlite;")

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem sucedida')


cursor = conexao.cursor()
cursor.execute("SELECT * FROM Salaries")
valores = cursor.fetchall()
print(valores[:10])


cursor.execute("""
INSERT INTO albums (Title, ArtistId)
VALUES
('Juan Rock', 4)
""")
cursor.commit()


print('-' * 80)
# CONEXÃO USANDO SQLITE3
conexao = sqlite3.connect('chinook.db')

tabela_clientes = pd.read_sql("SELECT * FROM customers", conexao)
print(tabela_clientes)


cursor.execute("SELECT * FROM customers")

valores = cursor.fetchall()
descricao = cursor.description
cursor.close()

# PEGAR O NOME DOS CAMPOS DA TABELA
colunas = [tupla[0] for tupla in descricao]
print(colunas)

# CRIANDO UMA TABELA COM OS DADOS DO BANCO
tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas)
print(tabela_clientes)

cursor.execute('''
UPDATE customers SET Email="juanmurta@gmail.com" WHERE Email="luisg@embraer.com.br"
''') # executar o comando SQL
cursor.commit()  # perpetuar no banco as alterações

cursor.execute('''
DELETE FROM albums WHERE AlbumId=2
''')
cursor.commit()

conexao.close()
cursor.close()