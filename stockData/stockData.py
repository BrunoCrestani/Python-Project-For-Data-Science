import pandas as pd
import requests
from bs4 import BeautifulSoup

# Ignore all warnings
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'

data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    open_price = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    volume = col[6].text

    netflix_data = netflix_data.append({"Date": date, "Open": open_price, "High": high, "Low": low, "Close": close, "Volume": volume}, ignore_index=True)

print(netflix_data.head())
