---
title: How to Code a Scraping Bot with Selenium and Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-12T18:37:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-scraping-bot-with-selenium-and-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5ffd8f3b75d5f706921cc190.jpg
tags:
- name: Python
  slug: python
- name: selenium
  slug: selenium
- name: Tutorial
  slug: tutorial
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: "By Otávio Simões Silveira\nSelenium is a tool designed to help you run\
  \ automated tests in web applications. It is available in several different programming\
  \ languages. \nAlthough it’s not its main purpose, Selenium is also used in Python\
  \ for web scrapi..."
---

By Otávio Simões Silveira

Selenium is a tool designed to help you run automated tests in web applications. It is available in several different programming languages. 

Although it’s not its main purpose, Selenium is also used in Python for web scraping, because it can access JavaScript-rendered content (which regular scraping tools like BeautifulSoup can’t do).

Selenium is also useful when you need to interact with the page somehow before collecting the data, such as clicking buttons or filling out fields. This is the use case that will be covered in this article. 

As an example, we’ll scrape investing.com to extract historical data of dollar exchange rates against one or more currencies.

If you search the web, you can find APIs and Python packages that make it much easier to gather financial data (instead of scraping it manually). However, the idea here is to explore how Selenium can help you with general data extraction.

## The Website We're Going to Scrape

First, we need to understand the website. [This site](https://investing.com/currencies/usd-eur-historical-data) contains the historical data for the exchange rate of the dollar against the euro.

On this page, you can see a table with the data and the option to set the date range we want. That’s what we’re going to use. 

To see the data for other currencies against the dollar, just replace “_eur_” with the other currency code in the URL.

Also, this assumes that you’ll only want the currency's exchange rate against the dollar. If that’s not the case, just replace the “usd” in the URL.

## The Scraper's Code

We’ll start with the imports, and we don’t need much. Let's import some useful items from Selenium: the `sleep` function to insert some pauses in the code, and Pandas to manipulate the date when necessary.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
```

Next, we’ll write a function to scrape the data. The function will receive:

* A list of currency codes
* A start date
* An end date
* A boolean informing if we want to export the data as a _.csv_ file. I’ll use False as the default.

Also, as the idea here is to build a scraper capable of gathering data about multiple currencies, we’ll also initialize an empty list to store the data from each currency.

```python
def get_currencies(currencies, start, end, export_csv=False):
    frames = []
```

As the function now has a list of currencies, you’ll probably imagine that we’ll iterate over this list and get the data currency by currency. That’s precisely the plan.

So for each currency in the currencies list, we’ll create a URL, instantiate a driver object, and use it to get the page. Then we’ll maximize the window, but that’s only visible if you keep `option.headless` as False. Otherwise, Selenium will do all the work without showing you anything.

```python
for currency in currencies:
    my_url = f'https://br.investing.com/currencies/usd-{currency.lower()}-historical-data'
    option = Options()
    option.headless = False
    driver = webdriver.Chrome(options=option)
    driver.get(my_url)
    driver.maximize_window()
```

We’re already looking at the historical data at this point, and we could just get the table with the data. However, by default, we only see the data for about the last 20 days. We want to get this data for any time period. 

For this, we’ll use some interesting Selenium functionalities to interact with the website. This is when Selenium shines!

What we’ll do here is click on the dates and fill the Start Date and End Date fields with the dates we want and hit Apply. 

For this, we’ll use `WebDriverWait`, `ExpectedConditions`, and `By` to make sure the web driver will wait for the elements we want to interact with to be clickable. 

This is important because if the diver tries to interact with something before it becomes clickable, an exception will be raised.

The waiting time will be twenty seconds, but it’s up to you to set it as you find appropriate. First, let’s select the date button by its Xpath and then click on it.

```python
date_button = WebDriverWait(driver, 20).until(
              EC.element_to_be_clickable((By.XPATH,
              "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span")))

date_button.click()
```

Now, we need to fill the Start Date field. Let’s first select it and then use `clear` to delete the default date and `send_keys` to fill it with the date we want.

```python
start_bar = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, 
	        "/html/body/div[7]/div[1]/input[1]")))

start_bar.clear()
start_bar.send_keys(start) 
```

And now we repeat the process for the End Date field.

```python
end_bar = WebDriverWait(driver, 20).until(
          EC.element_to_be_clickable((By.XPATH, 
          "/html/body/div[7]/div[1]/input[2]")))

end_bar.clear()
end_bar.send_keys(end)
```

With this done, we’ll select the Apply button and click on it. Then we use `sleep` to pause the code for a few seconds and make sure the new page is fully loaded.

```python
apply_button = WebDriverWait(driver, 20).until(
	           EC.element_to_be_clickable((By.XPATH,  
               "/html/body/div[7]/div[5]/a")))

apply_button.click()
sleep(5)
```

If you had `option.headless` as False, you’ll see this entire process happening in front of you as if somebody was actually clicking on the page. When Selenium clicks on Apply, you’ll see the table reloading to show the data for the time period you specified.

We now use the `pandas.read_html` function to select all the tables on the page. This function will receive the page’s source code. Finally, we can quit the driver.

```python
dataframes = pd.read_html(driver.page_source)
driver.quit()
print(f'{currency} scraped.')
```

## How to Handle Exceptions in Selenium

The process of collecting the data is done. But we need to consider that Selenium can sometimes be a little unstable and could eventually fail to load the page at some point during all the actions we’re performing here.

To prevent that, we’ll have the entire code inside a `try` clause that will be inside an infinity loop. Once Selenium manages to collect the data as I described above, the loop will be broken. But every time it finds a problem, an `expect` clause will be activated. 

In this scenario the code will:

* Quit the driver – it’s always important to do this so we don’t end up with dozens of memory consuming web drivers running
* Print a message indicating the error
* Sleep for thirty seconds
* Go to the start of the loop once more

This process will be repeated until the data for each currency is properly collected. And this is the code for all this:

```python
 for currency in currencies:
        while True:
            try:
                # Opening the connection and grabbing the page
                my_url = f'https://br.investing.com/currencies/usd-{currency.lower()}-historical-data'
                option = Options()
                option.headless = False
                driver = webdriver.Chrome(options=option)
                driver.get(my_url)
                driver.maximize_window()
                   
                # Clicking on the date button
                date_button = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[5]/section/div[8]/div[3]/div/div[2]/span")))
                
                date_button.click()
                
                # Sending the start date
                start_bar = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[7]/div[1]/input[1]")))
                            
                start_bar.clear()
                start_bar.send_keys(start)

                # Sending the end date
                end_bar = WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                            "/html/body/div[7]/div[1]/input[2]")))
                            
                end_bar.clear()
                end_bar.send_keys(end)
               
                # Clicking on the apply button
                apply_button = WebDriverWait(driver,20).until(
                		EC.element_to_be_clickable((By.XPATH,
                		"/html/body/div[7]/div[5]/a")))
                
                apply_button.click()
                sleep(5)
                
                # Getting the tables on the page and quiting
                dataframes = pd.read_html(driver.page_source)
                driver.quit()
                print(f'{currency} scraped.')
                break
            
            except:
                driver.quit()
                print(f'Failed to scrape {currency}. Trying again in 30 seconds.')
                sleep(30)
                continue

```

One last step, though. If you recall, what we have so far is a list containing all the tables on the page stored as DataFrames. We need to select the one table that contains the historical data we want.

For each DataFrame in this dataframes list, we’ll check if the name of its columns matches what we expect. If they do, then that’s our frame and we break the loop. And now we’re finally ready to append this DataFrame to the list that was initialized in the beginning.

```python
for dataframe in dataframes:
    if dataframe.columns.tolist() == ['Date', 'Price', 'Open', 'High', 'Low', 'Change%']:
        df = dataframe
        break

frames.append(df)
```

And yes, if the `export_csv` parameter was set to True, we would need to export a _.csv_ file. But that’s far from being an issue as the `DataFrame.to_csv` method can easily get this done. 

And then we can just wrap this function up by returning the list of DataFrames. This last step is done after the looping through the currencies list is over, of course.

```python
if export_csv:
        df.to_csv('currency.csv', index=False)
        print(f'{currency}.csv exported.')

# Outside of the loop
return frames
```

And that’s it! Here’s the complete code for these two last steps combined:

```python
		# Selecting the correct table            
        for dataframe in dataframes:
            if dataframe.columns.tolist() == ['Date', 'Price', 'Open', 'High', 'Low', 'Change%']:
                df = dataframe
                break
        frames.append(df)

        # Exporting the .csv file
        if export_csv:
            df.to_csv('currency.csv', index=False)
            print(f'{currency}.csv exported.')
                  
  return frames
```

## Next Steps and Wrapping Up

So far this code gets the historical data of the exchange rate of a list of currencies against the dollar and returns a list of DataFrames and several _.csv_ files.

But there’s always room for improvement. With a few more lines of code, it’s not hard to make the function return and export a single DataFrame containing the data for every currency in the list. 

Another suggestion is to write an `update` function using the same Selenium functionalities that receive an existing dataframe and update the historical data to the present date.

Besides, the exact same logic used to scrape the currencies can be used to scrape stocks, indices, commodities, futures, and much more. There are so many pages you can scrape.

However, if that’s the goal, then it’s important to insert more pauses in the code to avoid overloading the server. You should also take advantage of a proxy provider, such as [Infatica](https://infatica.io/), to make sure your code will keep running as long as there are pages left to scrape and that you and your connection are protected.

Finally, Selenium can be useful in several other situations such as signing in to websites, filling out forms, selecting items in a dropdown list, and much more. Of course, it’s not the only solution for such problems, but it can definitely be useful depending on the use case.

I hope you’ve enjoyed this article and that it has helped you out. If you have a question or a suggestion, feel free to [be in touch](https://www.linkedin.com/in/otavioss28/).

  

