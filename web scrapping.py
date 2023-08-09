# Web Scrapping :)
# pip install beautifulsoup4
# pip install requests
import requests
from bs4 import BeautifulSoup
#url = "https://www.indiatoday.in/"
url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/points-table-standings"
response = requests.get(url)
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
#print(type(soup), id(soup))
#print(soup.prettify())
teams = soup.find_all('span', class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
wins = soup.find_all('td', class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max")
#tags = soup.find_all("h3")
for team in teams:
    title = team.text.strip()
    print(title)

for win in wins:
    num = win.text.strip()
    print(num)

# tags = soup.find_all("div", class_)
# for tag in tags:
#     print("~~~~~~~~~~~~~~~~~~~~~")
#     print(tag.text)
#     print("~~~~~~~~~~~~~~~~~~~~~")