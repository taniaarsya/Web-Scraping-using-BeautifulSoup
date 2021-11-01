from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get ('https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('table',attrs={'class':'table table-striped text-sm text-lg-normal'})
print(table.prettify()[1:700])
table.find_all('th',attrs={'class':'font-semibold text-center'})

row_length = len(row)

temp = [] #initiating a list 

for i in range(1, row_length):
#insert the scrapping process here
    Date = table.find_all('th',attrs={'class':'font-semibold text-center'})[i].text
    Date = Date.strip()
    
    Market_Cap = table.find_all('td',attrs={'class':'text-center'})[4*i].text
    Market_Cap = Market_Cap.strip()
    
    Volume = table.find_all('td',attrs={'class':'text-center'})[4*i+1].text
    Volume = Volume.strip()
    
    Open = table.find_all('td',attrs={'class':'text-center'})[4*i+2].text
    Open = Open.strip()
    
    Close = table.find_all('td',attrs={'class':'text-center'})[4*i+3].text
    Close = Close.strip()
    
    temp.append((Date, Market_Cap, Volume, Open, Close))
    

temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns = ('Date', 'Market_Cap', 'Volume', 'Open', 'Close'))

#insert data wrangling here
df.dtypes
df['Market_Cap']=df['Market_Cap'].str.replace('$','')
df['Market_Cap']=df['Market_Cap'].str.replace(',','')

df['Volume']=df['Volume'].str.replace('$','')
df['Volume']=df['Volume'].str.replace(',','')

df['Open']=df['Open'].str.replace('$','')
df['Open']=df['Open'].str.replace(',','')

df['Close']=df['Close'].str.replace('$','')
df['Close']=df['Close'].str.replace(',','')
df['Close']=df['Close'].str.replace('N/A','0')

df['Date']=df['Date'].astype('datetime64')
df['Market_Cap']=df['Market_Cap'].astype('int64')
df['Volume']=df['Volume'].astype('int64')
df['Open']=df['Open'].astype('float64')
df['Close']=df['Close'].astype('float64')

df = df.set_index('Date')

df.sort_values('Volume', ascending=False)
df.plot()
df[['Open','Close']].plot()
#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{df["Market_Cap"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = ____.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)