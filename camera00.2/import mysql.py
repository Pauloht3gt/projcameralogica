# import mysql.connector

# con = mysql.connector.connect(host='localhost',database='pit',user='root',password='')

# if con.is_connected():
   # db_info = con.get_server_info()
   # print("Conectado ao servidor mysql versão ",db_info)
   # cursor = con.cursor()
   # cursor.execute("select database();")
   # linha = cursor.fetchone()
   # print("Conectado ao banco de dados",linha)

# if con.is_connected():
  #  cursor.close()
   # con.close()
   # print("Conexão ao mysql foi encerrada")












import mysql.connector
from mysql.connector import Error
# Inserir registros em um banco de dados MYSQL

try: 
    con = mysql.connector.connect(host='localhost',database='pit',user='root',password='')

    inserir_foto = """INSERT INTO paulo_fotos
                        (Nome, Foto)
                        VALUES
                        (1, 'paulin',)
                    """
    cursor = con.cursor()
    cursor.execute(inserir_foto)
    con.commit()
    print(cursor.rowcount, "Registros inseridos na tabela!")
    cursor.close()

except Error as erro:
    print("Falha ao enserir dados no MYSQL: {}" .format(erro))

finally: 
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão MYSQL finalizada!")