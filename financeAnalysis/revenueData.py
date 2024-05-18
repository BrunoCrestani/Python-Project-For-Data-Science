import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import warnings
warnings.filterwarnings("ignore")


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Pricce, Closing Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[reveneue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text = "Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text = "Revenue ($US Milions)", row=2, col=1)
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    fig.show()
     
#As a data scientist working for a hedge fund, 
# you will extract the profit data for Tesla and 
# GameStop and build a dashboard to compare the price 
# of the stock vs the profit for the hedge fund.

def getRevenue(ticker, url, dataframe):
    stock = yf.Ticker(ticker) 
    stock_data = stock.history(period="max")
    stock_data.reset_index(inplace=True)

    response = requests.get(url)
    html_data = response.text
    soup = BeautifulSoup(html_data, "html5lib")

    for row in soup.find("tbody").find_all("tr"):
        col = row.find_all("td")
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")

        dataframe.dropna(inplace=True)
        dataframe = dataframe[dataframe['Revenue'] != ""]
        dataframe = dataframe.append({"Date": date, "Revenue": revenue}, ignore_index=True)

    return dataframe

#TSLA
teslaUrl = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

tesla_revenue = getRevenue("TSLA", teslaUrl, tesla_revenue)

print ("Tesla Revenue:\n", tesla_revenue.tail(5))

#GME
gameStopUrl = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
gme_revenue = getRevenue("GME", gameStopUrl, gme_revenue)

print ("GameStop Revenue:\n", gme_revenue.tail(5))


