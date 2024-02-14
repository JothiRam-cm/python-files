import pytesseract
import PIL.Image
import cv2
import pyttsx3
eng=pyttsx3.init()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
myconfig=r"--psm 12 --oem 3"

text=pytesseract.image_to_string(PIL.Image.open("img3.jpg"),config=myconfig)
output = ""

output = output + text
     
print(output)
img=cv2.imread("img3.jpg")
height, width, _=img.shape
boxes=pytesseract.image_to_boxes(img,config=myconfig)
for box in boxes.splitlines():
    box=box.split(" ")
    img=cv2.rectangle(img,(int(box[1]),height-int(box[2])),(int(box[3]),height-int(box[4])),(100,0,0),2)
    
cv2.imshow("img",img)
cv2.waitKey(0)    
