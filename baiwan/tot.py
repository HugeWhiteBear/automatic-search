from PIL import ImageGrab,Image
import pytesseract
import webbrowser

image_Q = ImageGrab.grab((120,250,670,350))
#image_A1 = ImageGrab.grab()
#image_A2 = ImageGrab.grab()
#image_A3 = ImageGrab.grab()

#杜甫和李白 (testing for screenshot)
image_Q.show()
#print(pytesseract.image_to_string(image_Q,lang='chi_sim'))
#example
#image_Q.save(r'C:\Users\77904\Desktop\1.jpg')
#imgQ = Image.open(r'C:\Users\77904\Desktop\1.jpg')
#imgQ.load()

#you have to install 'tesseract' on your computer
#https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows
#after that, pytesseract.py, change  tesseract_cmd = 'tesseract' into
#tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'  in case windows Error2

Q = pytesseract.image_to_string(image_Q,lang='chi_sim')
Q = Q.replace(' ','')
Q1 =''
for i in range(0,len(Q)):
    if Q[i] != '\"' and Q[i] != '.'and Q[i]!= '?'and Q[i]!='-':
        Q1 = Q1 + Q[i]


stringQ = 'https://www.google.com.sg/search?hl=cn&q=' + Q1
#stringA1 = 'https://www.google.com.sg/search?hl=cn&q=' + pytesseract.image_to_string(image_A1,lang='chi_sim')
#stringA2 = 'https://www.google.com.sg/search?hl=cn&q=' + pytesseract.image_to_string(image_A2,lang='chi_sim')
#stringA3 = 'https://www.google.com.sg/search?hl=cn&q=' + pytesseract.image_to_string(image_A3,lang='chi_sim')

#print(stringQ)
webbrowser.open(stringQ)
