import zipfile, re

zipp = zipfile.ZipFile("channel.zip")

# h1: start from number 90052 h2: answer is inside the zip
print(zipp.read("readme.txt").decode("utf-8"))

num = '90052'

comments = []

while True:
    content = zipp.read(num + ".txt").decode("utf-8")
    comments.append(zipp.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)
#This is a small miss direction using the word "Hockey will lead you to a hint stating "it's in the air. look at the letters"
#zip files may contain comments and they can be accessed by zip.comment
print("".join(comments))