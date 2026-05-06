import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com/page/{}/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

total_count = 0  # total quotes counter

with open("quotes.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])

    for i in range(1, 4):
        url = base_url.format(i)
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        print(f"Page {i} scraped successfully")

        for quote in quotes:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            writer.writerow([text, author])
            total_count += 1

print("\nTotal Quotes Scraped:", total_count)
print("Scraping completed successfully!")