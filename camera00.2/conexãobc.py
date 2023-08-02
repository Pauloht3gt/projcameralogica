import mysql.connector

# Conectando ao banco de dados
cnx = mysql.connector.connect(user='root', password='3306', host='localhost', database='pit')
cursor = cnx.cursor()

# Lendo a imagem do arquivo
with open("C:\Users\paulo\OneDrive\Área de Trabalho\paulo 2ªinf\daniel\camera00.2\paulohh.jpeg", 'rb') as arquivo:
    imagem = arquivo.read()

# Inserindo a imagem na tabela
query = "INSERT INTO imagens (nome, imagem, tipo) VALUES (%s, %s, %s)"
valores = ('imagem1', imagem, 'jpg')
cursor.execute(query, valores)
cnx.commit()

# Fechando a conexão
cursor.close()
cnx.close()