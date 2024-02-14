# DEtect Text from image with pytesseract and turtle for printing the output  
import pyttsx3
import cv2
import pytesseract
from PIL import Image as ima
import turtle
engine=pyttsx3.init()

win=turtle.Screen()
win.setup(800,800)
win.bgcolor("black")
win.title("Text_Reconition")
w=turtle.Turtle()
w.pencolor("green")
w.hideturtle()

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

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
          w.write(text[:-1],align="right",font=("Arial",15,"bold"))
          
          print(text[:-1])
          
    tesseract()    
      

    
   
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def saved_image(): # taken saved image as an input 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    myconfig=r"--psm 12 --oem 3"

    text=pytesseract.image_to_string(ima.open("img4.jpg"),config=myconfig)
    w.write(text,align="center",font=("Arial",10,"bold")) 
    engine.say("printing the output ")                                                        #printing the output 
    print(text[:-1])
    img=cv2.imread("img4.jpg") #seting path
    height, width, _=img.shape
    boxes=pytesseract.image_to_boxes(img,config=myconfig)
    for box in boxes.splitlines():
       box=box.split(" ")
       img=cv2.rectangle(img,(int(box[1]),height-int(box[2])),(int(box[3]),height-int(box[4])),(100,0,0),2)
    engine.say(text[:-1])
    engine.say("your output is ready")
    cv2.imshow("img",img)
    cv2.waitKey(0)    


if __name__ == "__main__":
      
    print("Enter the mode :\n\t1.Saved_Image\n\t2.Live_Image")
    w.write("Enter the mode :\n\t1.Saved_Image\n\t2.Live_Image",font=("sanserif",25,"bold"))
    opt=win.numinput("Geting input","Enter your option!",0,minval=1,maxval=2)
    opt=int(input())
    w.clear()
    if(opt==2):
        engine.say("you selected option 2") 
        print("you selected option 2")
        saved_image()
        
    elif(opt==1):
         engine.say("you selected option 1")
         print("you selected option 1")
         inpcam()  
       
         
    else:
        engine.say("Enter a correct option")
        print("Enter a correct option:")    
        
    


    