import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#define the ticker symbol
tickerSymbol = 'HER.MI'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='max',interval='1wk')

#see your data
tickerDf['Close'].plot(title="HER.MI's stock price")
plt.show()

#write file
tickerDf=tickerDf.sort_values(by='Date',ascending=False)
tickerDf.to_csv('result.csv',index=True,sep=';')