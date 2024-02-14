import cv2
import pytesseract
from PIL import Image as ima
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def saved_image(): # taken saved image as an input 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    myconfig=r"--psm 12 --oem 3"

    text=pytesseract.image_to_string(ima.open("img4.jpg"),config=myconfig)                                                        #printing the output 
    print(text[:-1])
    img=cv2.imread("img4.jpg") #seting path
    height, width, _=img.shape
    boxes=pytesseract.image_to_boxes(img,config=myconfig)
    for box in boxes.splitlines():
       box=box.split(" ")
       img=cv2.rectangle(img,(int(box[1]),height-int(box[2])),(int(box[3]),height-int(box[4])),(100,0,0),2)
    cv2.imshow("img",img)
    cv2.waitKey(0)    
saved_image() 
    
