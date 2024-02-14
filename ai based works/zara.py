import pyttsx3
import pytesseract
from PIL import Image as ima
import cv2
import turtle




#myconfig = r"--psm 6 --oem 3"

#text=pytesseract.image_to_string(PIL.Image.open(""),config=myconfig)
#qsprint(text)



def inpcam():
    camera=cv2.VideoCapture(0)
    while True:
       ret,Image=camera.read()
       if not ret:
            break
       gray_frame = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
       cv2.imshow('Text detection',Image)
       if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg',gray_frame)
        break
    camera.release()
    cv2.destroyAllWindows()

    def tesseract():
          #path_to_tesseract='C:\Program Files\Tesseract-OCR\tessdata.exe'
          imagpath='test1.jpg'
          pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  
          text=pytesseract.image_to_string(ima.open(imagpath))
          src=turtle.Screen()
          src.setup(500,500)
          src.title("text_regonitation")
          src.bgcolor("black")
          w=turtle.Turtle()
          w.speed("fastest")
          w.pencolor("green")
          w.write(text,align="right",font=("Arial",15,"bold"))
          
          print(text[:-1])
          
    tesseract()    
inpcam()        
