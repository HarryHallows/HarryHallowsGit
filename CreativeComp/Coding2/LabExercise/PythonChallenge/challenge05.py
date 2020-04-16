from urllib.request import urlopen
import pickle


# Normally plain text can be encoded as utf-8 or some other form, once we call .decode() it will reveal it self
url = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")#.read()

#url.decode()

#As hinted by pronouncing "peak hell", let's use pickle to deserialize it:
data = pickle.load(url)

for line in data:
    print("".join([k * v for k, v in line]))