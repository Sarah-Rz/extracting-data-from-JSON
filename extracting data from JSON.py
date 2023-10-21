import urllib.request, urllib.parse, urllib.error
import json

# prompt for a URL using Urllib
url = input('Enter -')
fhand = urllib.request.urlopen(url).read()
data = fhand.decode()

# extracting data from Json
info = json.loads(data)

sum = 0

# parse and extract the comment counts from the JSON data (http://py4e-data.dr-chuck.net/comments_1862743.json)
for item in info["comments"]:

#compute the sum of the numbers in the file 
        sum = float(item['count']) + sum

print(sum)
