import pyodbc
import sqlite3
import pandas as pd

# Verificar os drivers disponíveis
print("Drivers disponíveis:", pyodbc.drivers())

# CONEXÃO COM O SQLITE USANDO PYODBC
try:
    dados_conexao = (
        "Driver={SQLite3 ODBC Driver};"
        "Server=localhost;"
        "Database=salarios.sqlite;"
    )
    conexao_odbc = pyodbc.connect(dados_conexao)
    print('Conexão ODBC bem-sucedida')

    cursor_odbc = conexao_odbc.cursor()

    # Ler os primeiros 10 valores da tabela Salaries
    cursor_odbc.execute("SELECT * FROM Salaries")
    valores = cursor_odbc.fetchall()
    print(valores[:10])

    # Inserir novo álbum (se a tabela existir)
    try:
        cursor_odbc.execute("""
        INSERT INTO albums (Title, ArtistId)
        VALUES ('Juan Rock', 4)
        """)
        conexao_odbc.commit()
        print("Inserção realizada com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

    # Fechar conexão ODBC
    cursor_odbc.close()
    conexao_odbc.close()

except Exception as e:
    print(f"Erro na conexão ODBC: {e}")

print('-' * 80)

# CONEXÃO COM SQLITE3
try:
    conexao_sqlite = sqlite3.connect('chinook.db')
    cursor_sqlite = conexao_sqlite.cursor()

    # Ler clientes do banco
    tabela_clientes = pd.read_sql("SELECT * FROM customers", conexao_sqlite)
    print(tabela_clientes.head())  # Exibir apenas as primeiras linhas

    # Obter os nomes das colunas
    cursor_sqlite.execute("SELECT * FROM customers")
    descricao = cursor_sqlite.description
    colunas = [tupla[0] for tupla in descricao]
    valores = cursor_sqlite.fetchall()

    # Criar DataFrame com os dados obtidos
    tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas)
    print(tabela_clientes.head())

    # Atualizar email de um cliente
    try:
        cursor_sqlite.execute("""
        UPDATE customers 
        SET Email = "juanmurta@gmail.com" 
        WHERE Email = "luisg@embraer.com.br"
        """)
        conexao_sqlite.commit()
        print("Email atualizado com sucesso.")

    except Exception as e:
        print(f"Erro ao atualizar: {e}")

    # Deletar um álbum (se existir)
    try:
        cursor_sqlite.execute("DELETE FROM albums WHERE AlbumId=2")
        conexao_sqlite.commit()
        print("Álbum deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar: {e}")

    # Fechar conexão SQLite
    cursor_sqlite.close()
    conexao_sqlite.close()

except Exception as e:
    print(f"Erro na conexão SQLite: {e}")
