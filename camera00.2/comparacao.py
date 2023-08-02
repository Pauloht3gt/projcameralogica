import cv2
import imagehash
import sqlite3

def compare_images(photo_path, threshold=10):
    # Calcular o hash da imagem a ser inserida
    new_photo_hash = imagehash.average_hash(Image.open(photo_path))
    
    # Abrir conexão com o banco de dados
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        # Recuperar todas as fotos do banco de dados
        cursor.execute("SELECT nome, dados FROM fotos")
        rows = cursor.fetchall()
        
        # Comparar o hash da nova foto com as existentes no banco de dados
        for row in rows:
            existing_photo_hash = imagehash.hex_to_hash(row[0])  # Supondo que o hash esteja armazenado como uma string
            difference = new_photo_hash - existing_photo_hash
            if difference <= threshold:
                print("A foto já existe no banco de dados.")
                return
        
        # Se a foto não existir, inseri-la no banco de dados
        with open(photo_path, 'rb') as photo_file:
            photo_data = photo_file.read()

        cursor.execute("INSERT INTO fotos (nome, dados) VALUES (?, ?)",
                       (str(new_photo_hash), sqlite3.Binary(photo_data)))
        
        # Salvar as alterações no banco de dados
        conn.commit()
        print("Foto inserida com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao inserir a foto:", e)
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

# Exemplo de uso
compare_images('caminho/para/foto.jpg')
