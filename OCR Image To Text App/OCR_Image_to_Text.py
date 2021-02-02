'''
step1. GoTo Command Prompt and install pytesseract package using command 'pip install pytesseract'
step2. Goto this link - https://github.com/ub-mannheim/tesseract/wiki and download
'tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit) resp.' setup and Install it on your machine.
step3. Change the Image path in the below code.
After that run the below code
'''

import pytesseract  # Importing the package installed in step1.
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/gsc-30431/AppData/Local/Tesseract-OCR/tesseract.exe"
# Provide the path of tesseract.exe file which was installed in step2

def convert():
    img = Image.open('C:/Users/gsc-30431/PycharmProjects/test1.py/Python_Projects/OCR_Img_to_Text/img5.jpg')  # Update Image Path Here!
    # Provite the path of Image which is to be converted into text
    text = pytesseract.image_to_string(img)
    print(text)

convert()
