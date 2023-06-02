from bs4 import BeautifulSoup
import requests
from datetime import date, timedelta

today = str(date.today() - timedelta(days=1))
print(today)
x = 0
url = "https://tldr.tech/tech/"

url = url + today

print(url)
contents = requests.get(url)

soup = BeautifulSoup(contents.text, "html.parser")

for script in soup(["script", "style"]):
    script.extract()    # rip it out

text = soup.get_text()

print(text)