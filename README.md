# Automatic-Search
This small program is used for some money-earning, ask and answer app.
For several reasons, we cannot run it in cmd or separately in current version.

To use this program, two libraries needed are 'Pillow',which substitites for 'PIL' - Python Image Library in Python3.X, and 'pytesseract'.
Also, the Optical Character Recognition in this program is based on Google Tesseract-OCR. It can be download at
https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows

In case of " WindowsError: [Error 2] The system cannot find the file specified ", find ‘pytesseract.py’, open it and change " tesseract_cmd = 'tesseract' " into " tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' ". (It depends on where you install Tesseract-OCR)

Then you need to connect your phone with your computer and project your phone screen on the computer. Make sure the position matchs the code. You can test with the code in #block.

For more functions, such as combining the question with the answers, using the code in #block.
