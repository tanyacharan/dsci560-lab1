import requests
from bs4 import BeautifulSoup

#URL
url= "https://www.cnbc.com/world/?region=world"

#send request
response = requests.get(url)

#save raw html
raw_file = "../data/raw_data/web_data.html"
with open(raw_file, "w", encoding="utf-8") as p:
	p.write(response.text)
print("Web data saved here", raw_file)

soup= BeautifulSoup(response.text, "html.parser")

#print the title of the page so we can see what works
print("Page Title:", soup.title.string)
