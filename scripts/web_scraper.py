import requests
from bs4 import BeautifulSoup

#URL
url= "https://www.cnbc.com/world/?region=world"

#browser
headers = {
	"User-Agent": (
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
		"AppleWebKit/537.36 (KHTML, like Gecko) "
		"Chrome/119.0.0.0 Safari/537.36"
	),
	"Accept-Language": "en-US,en;q=0.9",
}

#send request
response = requests.get(url, headers=headers)
print("status:", response.status_code)

#save raw html
if response.status_code == 200:
	raw_file = "../data/raw_data/web_data.html"
	with open(raw_file, "w", encoding="utf-8") as p:
		p.write(response.text)
	print("Web data saved here", raw_file)
else:
	print("Failed to get page, status:", response.status_code)

soup= BeautifulSoup(response.text, "html.parser")

#print the title of the page so we can see what works
print("Page Title:", soup.title.string)
