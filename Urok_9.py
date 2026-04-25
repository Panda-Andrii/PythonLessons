import requests
from bs4 import BeautifulSoup

url = "https://uk.wikipedia.org/wiki/%D0%9A%D0%B8%D1%97%D0%B2"
headers = {"User-Agent": "Mozilla/5.0"}
resource = requests.get(url, headers=headers)
soup = BeautifulSoup(resource.text, "html.parser")
title = soup.find("h1").text
print("Назва статті:", title)

paragraph = soup.find("p").text
print(paragraph)

sections = soup.find_all("h2")
for s in sections:
    print(s.text)

links = soup.find_all("a")
print("Кількість посилань:", len(links))

for link in links:
    href = link.get("href")

    if href and href.startswith("/wiki/"):
        print("https://uk.wikipedia.org" + href)

images = soup.find_all("img")
for img in images[:5]:
    print(img.get("src"))