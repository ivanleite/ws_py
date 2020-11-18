# importe de modulos necessarios
import pytesseract
import cv2

# leitura da imagem pelo openCV
path = '/home/imouraleite/workspace/python_ws/boot_camp_ws/teste/conceitos_basicos.jpg'
img = cv2.imread(path)
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
txt = pytesseract.image_to_string(img)

# passando o texto para um arquivo txt
with open('conceitos_basicos.txt', mode='w') as texto:
    texto.write(txt)
