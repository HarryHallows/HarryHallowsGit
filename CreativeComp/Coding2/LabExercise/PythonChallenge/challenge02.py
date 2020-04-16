#After viewing page source there is displayed another encoded message full of different signs

import urllib.request
import re


#opening the link provided within the string statement "link here" then call read() function to read the page and decode() to decode the source

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

#we use the html comments to capture all of the text within the comment
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

print("".join(re.findall("[A-Za-z]", data)))

