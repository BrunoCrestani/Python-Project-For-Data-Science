import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html'

data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

title = soup.title

print(title)

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    open_price = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    volume = col[6].text

    amazon_data = amazon_data.append({"Date": date, "Open": open_price, "High": high, "Low": low, "Close": close, "Volume": volume}, ignore_index=True)

print(amazon_data.tail())
