import urllib.request
import re

#similar process to the previous challenge 
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

#print(data)

#print(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data))


print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))