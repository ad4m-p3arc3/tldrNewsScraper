from bs4 import BeautifulSoup
import requests

url = "https://tldr.tech/tech/2023-06-01"

contents = requests.get(url)

soup = BeautifulSoup(contents.text, "html.parser")

for script in soup(["script", "style"]):
    script.extract()    # rip it out

text = soup.get_text()

print(text)