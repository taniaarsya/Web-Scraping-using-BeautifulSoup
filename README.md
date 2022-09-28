# Web-Scrapping using Beautifulsoup

At this module we will learn on how do simple web scrapping using beautiful soup. Web scrapping is one of a method that we can use to colleting the data from internet. At this particular module, we will try to scrap Indonesian inflation rate from pusatdata.kontan.co.id, it's one of data center from indonesian economic newspaper that provide couple of useful financial information. To do this we will only use a couple default library from python and BeautifulSoup.

This module is made as easy and simple as possible which can be used for new developer to learn how to webscrapping using Beautiful Soup. But to do webscrapping you will need a bit of knowlage in html which I'll also try to help to explain what you needed at this module, but it is always better if you understand a bit what in html first. You can read it quickly at beautifulsoup documentation. It explain what is html and what beautiful soup exactly do at it landing page.
(https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Webscrapping with Beautiful Soup"). We will also make use of the simple flask dashboard to display our scraps and visualizations.

## Dependencies

Actually to follow this module you only need to install beautifulsoup4 with pip install beautifulsoup4 and you are good to go. But here some libraries that needed to be installed first that I use at this module :

- beautifulSoup4
- pandas
- flask
- matplotlib

What is BeautifulSoup
Beautiful Soup is a Python library for pulling data out of HTML and XML files. Beautiful Soup 3 only works on Python 2.x, but Beautiful Soup 4 also works on Python 3.x. Beautiful Soup 4 is faster, has more features, and works with third-party parsers like lxml and html5lib.

Since beautifulsoup used to pull the data out of a HTML, so first we need to pull out the html first. How we do it? We will use default library request.

So all this code is doing is sending a GET request to spesific address we give. This is the same type of request your browser sent to view this page, but the only difference is that Requests can't actually render the HTML, so instead you will just get the raw HTML and the other response information.

how to install requirements.txt in the following way :

```python
pip install -r requirements.txt
```

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrap the data  & Extracting the right information (5 points)
- Creating data frame & Data wrangling (5 points)
- Creating a tidy python notebook as a report. (2 points)
- Implement it on flask dashboard (2 points)


## What You Need to Do

* Please try to scrape the questions below using `beautiful soup` in your notebook first.
* You can clone this repo.
* Please open the notebook template on this capstone and fill it in according to the instructions. Make sure you provide the analysis needed on the notebook.
* The files in this repo are skeletons that can be used to create a simple flask dashboard.
* Please fill in the blanks.
* Fill in the `scrap` function with the scraping process that you have done in the notebook.

```python
table = soup.find(___)
tr = table.find_all(___)
```

* Fill in this section to save the scrap that has been made into a dataframe.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* Finally, you can use the `scrap` function by filling in the following section with a web link that has been scraped.

```python
df = scrap(___) #insert url here
```

*  can also play with the UI on `index.html` which can follow the comments to see which parts can be changed. 

### The Final Mission

Pada captsone kali ini, bisa memilih salah satu soal ini untuk dikerjakan.

1. (Easy) Data Volume Penjualan Ethereum dari `https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel`

   * Dari halaman tersebut carilah `Date`, dan `Volume`.
   * Buat lah plot pergerakan volume perdagangan dari Ethereum. 

2. (Medium) Data kurs US Dollar ke rupiah dari `https://www.exchange-rates.org/history/IDR/USD/T`

    * Dari halaman tersebut carilah `harga harian`, dan `tanggal`
    * Bualah plot pergerakan kurs USD 
    
3. (Hard) Data film yang rilis di tahun 2021 dari `https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31`

    * Dari Halaman tersebut carilah `judul` , `imdb rating` , `metascore`, dan `votes`
    * Buatlah plot dari 7 film paling populer di tahun 2021.


Happy learning! 
