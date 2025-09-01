import csv
from bs4 import BeautifulSoup

#load the saved html here
raw_file = "../data/raw_data/web_data.html"
with open(raw_file, "r", encoding="utf-8") as p:
	html = p.read()
soup=BeautifulSoup(html, "html.parser")

print("here we are getting fields from web_data.html")

#this part will get the market banner data
market_data = []
market_cards = soup.find_all("div", class_="MarketCard-container")

for card in market_cards:
	symbol = card.find("span", class_="MarketCard-symbol")
	position = card.find("span", class_="MarketCard-stockPosition")
	change =  card.find("span", class_="MarketCard-changesPct")

	if symbol and position and change:
		market_data.append([
			symbol.get_text(strip=True),
			position.get_text(strip=True),
			change.get_text(strip=True)
		])
print(f"extracted {len(market_data)} market entries")

#save the data to csv
market_file = "../data/processed_data/market_data.csv"
with open(market_file, "w", newline="", encoding="utf-8") as p:
	writer= csv.writer(p)
	writer.writerow(["Symbol", "StockPosition", "ChangePct"])
	writer.writerows(market_data)
print("Market data saved to", market_file)

#now get the news data
news_data = []
news_items = soup.find_all("div", class_="LatestNews-container")
for thing in news_items:
	timestamp = thing.find("time", class_="LatestNews-timestamp")
	headline = thing.find("a", class_="LatestNews-headline")
	if timestamp and headline:
		news_data.append([
			timestamp.get_text(strip=True),
			headline.get_text(strip=True),
			headline["href"]
		])
print(f"Extracted {len(news_data)} news entries.")

#save the news data to csv
news_file = "../data/processed_data/news_data.csv"
with open(news_file, "w", newline="", encoding="utf-8") as p:
	writer= csv.writer(p)
	writer.writerow(["Timestamp", "Title", "Link"])
	writer.writerows(news_data)
print("news data saved to", news_file)
