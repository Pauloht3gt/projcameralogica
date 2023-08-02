import cv2
import face_recognition as fr
from PIL import Image

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow('video da webcam', frame)
        tempotecla = cv2.waitKey(5)
        if tempotecla == 27: # ESC
            break
cv2.imwrite('fotoImagem.png', frame)

webcam.release ()
cv2.destroyAllWindows()

img01 = fr.load_image_file('paulohh.jpeg')
img01 = cv2.cvtColor(img01,cv2.COLOR_BGR2RGB)
img02 = fr.load_image_file('fotoImagem.png')
img02 = cv2.cvtColor(img02,cv2.COLOR_BGR2RGB)

faceLoc = fr.face_locations(img01)[0]
cv2.rectangle(img01,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,255,0),2)
encode01 = fr.face_encodings(img01)[0]
encode02 = fr.face_encodings(img02)[0]

comparacao = fr.compare_faces([encode01],encode02)
distancia = fr.face_distance([encode02],encode02)

print(comparacao,distancia)
cv2.imshow('paulo',img01)
cv2.imshow('paulo02',img02)
cv2.waitKey(0)



def image_to_binary(image_path):
    # Abrir a imagem
    image = Image.open("C:\Users\paulo\OneDrive\Área de Trabalho\paulo 2ªinf\daniel\camera00.2\paulohh.jpeg")

    # Converter a imagem para escala de cinza (opcional)
    image = image.convert('L')

    # Obter os pixels da imagem
    pixels = image.load()

    # Definir uma função para converter um valor de pixel em binário
    def pixel_to_binary(pixel):
        # Verificar se o pixel é branco ou preto
        if pixel > 128:
            return '1'  # Pixel branco
        else:
            return '0'  # Pixel preto

    # Converter cada pixel em binário
    binary_string = ''
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            binary_string += pixel_to_binary(pixel)

    return binary_string

# Caminho da imagem
image_path = 'caminho/para/a/imagem.png'

# Converter a imagem para binário
binary_number = image_to_binary(image_path)

# Imprimir o número binário
print(binary_number)



























# webcam = cv2.VideoCapture(0)

# if webcam.isOpened():
#     validacao, frame = webcam.read()

#     while validacao:
#         validacao, frame = webcam.read()
#         cv2.imshow('video da webcam', frame)
#         tempotecla = cv2.waitKey(5)
#         if tempotecla == 27: # ESC
#             break
# cv2.imwrite('fotoImagem.png', frame)

# webcam.release ()
# cv2.destroyAllWindows()

# img01 = fr.load_image_file('Rafael.jpg')
# img01 = cv2.cvtColor(img01,cv2.COLOR_BGR2RGB)
# img02 = fr.load_image_file('fotoImagem.png')
# img02 = cv2.cvtColor(img02,cv2.COLOR_BGR2RGB)

# faceLoc = fr.face_locations(img01)[0]
# cv2.rectangle(img01,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(0,255,0),2)
# encode01 = fr.face_encodings(img01)[0]
# encode02 = fr.face_encodings(img02)[0]

# comparacao = fr.compare_faces([encode01],encode02)
# distancia = fr.face_distance([encode02],encode02)

# print(comparacao,distancia)
# cv2.imshow('paulo',img01)
# cv2.imshow('paulo02',img02)
# cv2.waitKey(0)