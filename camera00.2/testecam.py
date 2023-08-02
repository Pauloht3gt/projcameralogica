import mysql.connector

#Conexão ao Banco
cnx = mysql.connector.connect(user="cadastro", password="3306", host="localhost", database="cadastro")
cursor= cnx.cursor()

#Leitor de Img
with open("C:\Users\paulo\OneDrive\Área de Trabalho\paulo 2ªinf\daniel\camera00.2\paulohh.jpeg", "rb") as arquivo:
        imagem = arquivo.read()

#Inserindo Imagem na tabela
query = "INSERT INTO imagens (nome, imagem, tipo) VALUES (%s, %s, %s)"
valores = ("pauzin", imagem, "jpg")
cursor.execute(query, valores)
cnx.commit()

#Fechando a conexão
cursor.close()
cnx.close()
