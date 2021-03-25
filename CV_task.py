''' Imoprt required python libraries'''
import re
import cv2
import pytesseract
from pytesseract import Output

'''use opencv cv image thresholding and grayscale functions to filter noise in images'''
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def thresholding(image):
    return cv2.threshold(image, 300, 200, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

path=r'/home/mewada/Downloads/k.jpg' #input image path

img = cv2.imread(path)
img = get_grayscale(img)
img = thresholding(img)
Data = pytesseract.image_to_data(img, output_type=Output.DICT)
keys = list(Data.keys())
date_pattern = '[A-Z][A-Z][A-Z][A-CF-HLJPT][A-Z][0-9\w][0-9][0-9][0-9][A-Z]' # PAN card pattern format
date_pattern_date = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$' # DOB pattern format

for j in Data['text']: #if the pattern and string matches in image print the string
    if re.match(date_pattern, j):
        print('PAN Number : '+j)
    if re.match(date_pattern_date,j):
        print('Date of Birth : '+j)

