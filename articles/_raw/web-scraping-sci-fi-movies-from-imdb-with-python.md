---
title: Web Scraping in Python – How to Scrape Sci-Fi Movies from IMDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-09T19:50:10.000Z'
originalURL: https://freecodecamp.org/news/web-scraping-sci-fi-movies-from-imdb-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-pixabay-270348--1-.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: "By Riley Predum\nHave you ever struggled to find a dataset for your data\
  \ science project? If you're like I am, the answer is yes. \nLuckily, there are\
  \ many free datasets available – but sometimes you want something more specific\
  \ or bespoke. For that, w..."
---

By Riley Predum

Have you ever struggled to find a dataset for your data science project? If you're like I am, the answer is yes. 

Luckily, there are many free datasets available – but sometimes you want something more specific or bespoke. For that, web scraping is a good skill to have in your toolbox to pull data off your favorite website.

## What’s Covered in this Article?

This article has a Python script you can use to scrape the data on sci-fi movies (or whatever genre you choose!) from the [IMDB](https://www.imdb.com/) website. It can then write these data to a dataframe for further exploration. 

I will conclude this article with a bit of exploratory data analysis (EDA). Through this, you will see what further data science projects are possible for you to try.

_Disclaimer: while web scraping is a great way of programmatically pulling data off of websites, please do so responsibly. My script uses the sleep function, for example, to slow down the pull requests intentionally, so as not to overload IMDB's servers. Some websites frown upon the use of web scrapers, so use it wisely._

## Web Scraping and Data Cleaning Script

Let’s get to the scraping script and get that running. The script pulls in movie titles, years, ratings (PG-13, R, and so on), genres, runtimes, reviews, and votes for each movie. You can choose how many pages you want to scrape based on your data needs. 

_Note: it will take longer the more pages you select. It takes 40 min to scrape 200 webpages using the [Google Colab Notebook](https://colab.research.google.com/drive/11avx1TqYw_2sb5tUNi0ZO4ABRc50LNxK?usp=sharing)._

For those of you who have not tried it before, Google Colab is a cloud-based [Jupyter Notebook](https://realpython.com/jupyter-notebook-introduction/#:~:text=The%20Jupyter%20Notebook%20is%20an,the%20people%20at%20Project%20Jupyter.) style Python development tool that lives in the Google app suite. You can use it out of the box with many of the packages already installed that are common in data science. 

Below is an image of the Colab workspace and its layout:

![Image](https://lh4.googleusercontent.com/R9sAuHzGHrEvRK_hiAWsy4W41W72et6clD38gIYeAA6AtA32e97xxw0W5ub_96xmgSMTDB2VjRK-gz_YgYtZoV1YyCHjKftaB7-HD2NQ7qt_8hcdnDfqaibp0ONwPr9-4zO5gv3FuXdxiOMsN6eF8bA)
_Introducing the Google Colab user interface_

With that, let’s dive in! First things first, you should always import your packages as their own cell. If you forget a package you can re-run just that cell. This cuts down on development time. 

Note: some of these packages need `pip install package_name` to be run to install them first. If you choose to run the code locally using something like a Jupyter Notebook you'll need to do that. If you want to get up and running quickly, you can use the Google Colab notebook. This has all these installed by default.

```python
from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns
```

## How to Do the Web Scraping

You can run the following code which does the actual web scraping. It will pull all the columns mentioned above into arrays and populate them one movie at a time, one page at a time. 

There are also some data cleaning steps I have added and documented in this code as well. I removed parentheses from string data mentioning the year of the film for example. I then converted those to integers. Things like this make exploratory data analysis and modeling easier.

Note that I use the sleep function to avoid being restricted by IMDB when it comes to cycling through their web pages too quickly.

```python
# Note this takes about 40 min to run if np.arange is set to 9951 as the stopping point.

pages = np.arange(1, 9951, 50) # Last time I tried, I could only go to 10000 items because after that the URI has no discernable pattern to combat webcrawlers; I just did 4 pages for demonstration purposes. You can increase this for your own projects.
headers = {'Accept-Language': 'en-US,en;q=0.8'} # If this is not specified, the default language is Mandarin

#initialize empty lists to store the variables scraped
titles = []
years = []
ratings = []
genres = []
runtimes = []
imdb_ratings = []
imdb_ratings_standardized = []
metascores = []
votes = []

for page in pages:
  
   #get request for sci-fi
   response = get("https://www.imdb.com/search/title?genres=sci-fi&"
                  + "start="
                  + str(page)
                  + "&explore=title_type,genres&ref_=adv_prv", headers=headers)
  
   sleep(randint(8,15))
   
   #throw warning for status codes that are not 200
   if response.status_code != 200:
       warn('Request: {}; Status code: {}'.format(requests, response.status_code))

   #parse the content of current iteration of request
   page_html = BeautifulSoup(response.text, 'html.parser')
      
   movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
  
   #extract the 50 movies for that page
   for container in movie_containers:

       #conditional for all with metascore
       if container.find('div', class_ = 'ratings-metascore') is not None:

           #title
           title = container.h3.a.text
           titles.append(title)

           if container.h3.find('span', class_= 'lister-item-year text-muted unbold') is not None:
            
             #year released
             year = container.h3.find('span', class_= 'lister-item-year text-muted unbold').text # remove the parentheses around the year and make it an integer
             years.append(year)

           else:
             years.append(None) # each of the additional if clauses are to handle type None data, replacing it with an empty string so the arrays are of the same length at the end of the scraping

           if container.p.find('span', class_ = 'certificate') is not None:
            
             #rating
             rating = container.p.find('span', class_= 'certificate').text
             ratings.append(rating)

           else:
             ratings.append("")

           if container.p.find('span', class_ = 'genre') is not None:
            
             #genre
             genre = container.p.find('span', class_ = 'genre').text.replace("\n", "").rstrip().split(',') # remove the whitespace character, strip, and split to create an array of genres
             genres.append(genre)
          
           else:
             genres.append("")

           if container.p.find('span', class_ = 'runtime') is not None:

             #runtime
             time = int(container.p.find('span', class_ = 'runtime').text.replace(" min", "")) # remove the minute word from the runtime and make it an integer
             runtimes.append(time)

           else:
             runtimes.append(None)

           if float(container.strong.text) is not None:

             #IMDB ratings
             imdb = float(container.strong.text) # non-standardized variable
             imdb_ratings.append(imdb)

           else:
             imdb_ratings.append(None)

           if container.find('span', class_ = 'metascore').text is not None:

             #Metascore
             m_score = int(container.find('span', class_ = 'metascore').text) # make it an integer
             metascores.append(m_score)

           else:
             metascores.append(None)

           if container.find('span', attrs = {'name':'nv'})['data-value'] is not None:

             #Number of votes
             vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
             votes.append(vote)

           else:
               votes.append(None)

           else:
               votes.append(None)
```

Pandas dataframes take as input arrays of data for each of their columns in key:value pairs. I did a couple extra data cleaning steps here to finalize the data cleaning. 

After you run the following cell, you should have a dataframe with the data you scraped.

```python
sci_fi_df = pd.DataFrame({'movie': titles,
                      'year': years,
                      'rating': ratings,
                      'genre': genres,
                      'runtime_min': runtimes,
                      'imdb': imdb_ratings,
                      'metascore': metascores,
                      'votes': votes}
                      )

sci_fi_df.loc[:, 'year'] = sci_fi_df['year'].str[-5:-1] # two more data transformations after scraping
# Drop 'ovie' bug
# Make year an int
sci_fi_df['n_imdb'] = sci_fi_df['imdb'] * 10
final_df = sci_fi_df.loc[sci_fi_df['year'] != 'ovie'] # One small issue with the scrape on these two movies so just dropping those ones.
final_df.loc[:, 'year'] = pd.to_numeric(final_df['year'])
```

## Exploratory Data Analysis

Now that you have the data, one of the first things you might want to do is learn more about it at a high level. The following commands are a useful first look at any data and we’ll use them next:

```python
final_df.head()
```

This command shows you the first 5 rows of your dataframe. It helps you see that nothing looks weird and everything is ready for analysis. You can see the output here:

![Image](https://lh3.googleusercontent.com/TCYKlpEKIJOVJIAtIGN4wzDhCySaYIXI9cyBizZxR3XHsAQO_YH9mh626hCq8fdItaAF0N0cxSs1PP1eYujRsOt8HgeXtcC3hff-y0Jl4tvN__itH97iXqb6DrN6wJrngdsNaKQTQag5StHfOIcy5A0)
_The first five rows of data outputted using the `final_df.head()` command_

```python
final_df.describe()
```

This command will provide you with the mean, standard deviation, and other summaries. Count can show you if there are any null values in some of the columns which is useful information to know. The year column, for example, shows you the range of movies scraped – from 1927 to 2022. 

You can see the output below and inspect the others:

![Image](https://lh6.googleusercontent.com/Zeo_Y8ipyIejyYIBa2Aaocz4obHNlMVU76YTylZGl_wpRovYVFNS4e0m1DYAwkcqhpoYikJFL_dSgZSH-qoghJM3VMXESMUykrfs1e3JuXRkrp9iEZhPPnqGvsSamdYQe6Noz0Q0OA-Wen616-pmbDQ)
_Running `final_df.describe()` produces summary statistics showing the number of data points, averages, standard deviations, and more._

```python
final_df.info()
```

This command lets you know the data types you are working with in each of your columns. 

As a data scientist, this information can be helpful to you. Certain functions and methods need certain data types. You can also ensure that your underlying data types are in a format that makes sense for what they are. 

For example: a 5 star rating should be a float or int (if decimals are not allowed). It should not be a string since it's a number. Here’s a summary of what the data format was for each variable after the scraping:

![Image](https://lh3.googleusercontent.com/PT7Fa9XFYErtorVw6bNxw7Q1mI-p2_hlKgTbTs90RRpALPDlqd95F_EOwCQ7cV2cDymqZ-mXIa_0blqxxJ5wZ8Bznzd0iFyTB6kFroIUK2DJNzfRZgwgsRHr0pjDyE1ZUrQILf-22w856OoufnnKmRI)
_Running `final_df.info()` results in showing you how many values you have in each column and what their data types are._

The next command to learn more about your variables produces a heatmap. The heatmap shows the correlation between all your quantitative variables. This is a quick way to assess relationships that may exist between variables. I like to see the coefficients rather than trying to decipher the color code, so I use the `annot=True` argument.

```python
sns.heatmap(final_df.corr(), annot=True);
```

The command above produces the following visualization using the Seaborn data visualization package:

![Image](https://lh3.googleusercontent.com/niHLKP7bps1EpZ_39u5k3dPDF0Xuz8Zuhal8Bbc8wtImKUv50M_7fEH65rCAkrTglGtZTJpZ2sRfIE0E6Kjn9m_CYGkRct83_3wWzVp0rnHA8nh5UuveFO0OqtjVfoOzMsKGq0lZ2uxw66Lp4g69aMo)
_A heatmap of correlations after running `sns.heatmap(final_df.corr(), annot=True);`_

You can see that the strongest correlation is between the IMDB score and the metascore. This is not surprising since it's likely that two movie rating systems rate similarly.

The next strongest correlation you can see is between the IMDB rating and the number of votes. This is interesting because as the number of votes increases, you have a more representative sample of the population rating. It's strange to see that there is a weak association between the two, though.

The number of votes roughly increases as the runtime increases as well.

You can also see a slight negative association between IMDB or metascore and the year the movie came out. We’ll look at this shortly.

You can check out some of these relationships visually via a scatter plot with this code:

```python
x = final_df['n_imdb']
y = final_df['votes']
plt.scatter(x, y, alpha=0.5) # s= is size var, c= is color var
plt.xlabel("IMDB Rating Standardized")
plt.ylabel("Number of Votes")
plt.title("Number of Votes vs. IMDB Rating")
plt.ticklabel_format(style='plain')
plt.show()
```

This results in this visualization:

![Image](https://lh3.googleusercontent.com/vvqxh5VwbHPoypyGlNBstgZW8puVWKa5m_hl6MYB_r78OfRC7TWBx9jxjf8PFflJO93hq83ZdIqX97uq6C_WjlZV5jorCDgtU3U3_dESuUgsStfLEgkeiikHTq2noabW_tPJQRRGpFrVmQ90gja4xAo)
_IMDB Ratings vs. the Number of Votes_

The association above shows some outliers. Generally, we see a greater number of votes on movies that have an IMDB rating of 85 or more. There are fewer reviews on movies with a rating of 75 or less. 

Drawing these boxes around the data can show you what I mean. There's roughly two groupings of different magnitudes:

![Image](https://lh6.googleusercontent.com/QEUbjZrtSiLCbdcXIR1MN0MKvcCZgVxeW2sPzMo4KL36pjCQq87rkRdgKKwK2yWSh2Uz0HMoIckyOa0qcNX4hCQok_kuuyqq4PddFHVuC5Tzyg9-WdZobdZgWfOpW1PnKWFKfQLaDAEDXoDHfiuU5mY)
_Two Core Groups in the Data_

Another thing that might be interesting to see is how many movies of each rating there are. This can show you where Sci-Fi tends to land in the ratings data. Use this code to get a bar chart of the ratings:

```python
ax = final_df['rating'].value_counts().plot(kind='bar',
                                   figsize=(14,8),
                                   title="Number of Movies by Rating")
ax.set_xlabel("Rating")
ax.set_ylabel("Number of Movies")
ax.plot();
```

That code results in this chart which shows us that R and PG-13 make up the majority of these Sci-Fi movies on IMDB.

![Image](https://lh3.googleusercontent.com/7896rs2HtqgI4nIPyI-vUU5w43C3_Dcuyc_DdjUOudq76aIHstBINNVf5e0-1G3MUZzFgKDzK_2Jhsnno5swbXIoZwMuxqg1icY8aPbxWjOsCIm3BB9lObzY7HiDSAhmLTfcpfi2HWdW4VoUjBcnbrk)
_Number of Movies by Rating_

I did see that there were a few movies rated as “Approved” and was curious what that was. You can filter down the dataframe with this code to drill down into that:

```python
final_df[final_df['rating'] == 'Approved']
```

This revealed that most of these movies were made before the 80s:

![Image](https://lh3.googleusercontent.com/OIxMNDTgcXcPo_Wy8N7miq44OOAai4o-A8upYa1pNbqWjDVzPduRxNcMgUPuG9-OFyNd1AFgwWeq_o4E3Kv9pXy8xVSH7p6ZZi9uoOy78dBFK0LjvDnN9k7WYDTiZYxwpVgCiqXokWLPuMo746jvWMo)
_All Rating "Approved" Movies_

I went to the MPAA website and there was no mention of them on their ratings information page. It must have been phased out at some point.

You could also check out if any years or decades outperformed others on reviews. I took the average metascore by year and plotted that with the following code to explore further:

```python
# What are the average metascores by year?
final_df.groupby('year')['metascore'].mean().plot(kind='bar', figsize=(16,8), title="Avg. Metascore by Year", xlabel="Year", ylabel="Avg. Metascore")
plt.xticks(rotation=90)
plt.plot();
```

This results in the following chart:

![Image](https://lh5.googleusercontent.com/BTwJBQhq0zBTr5UH5J3n7CSR6k3Ft8l9GBQ_czZRlu_LO192AXd0G_ozwXzsb6pctS-8lHCvgVLx6VZ7hWH-trp8C4oFAPCGufh2gq-F2WV96u90xt05KqUGYCqSFpmXxPEsFKSZQceglNItwChRnfE)
_Avg. Metascore by Movie Year_

Now I’m not saying I know why, but there is a gradual, mild decline as you progress through history in the average metascore variable. It seems that ratings have leveled out around 55-60 in the last couple decades. This might be because we have more data on newer movies or newer movies tend to get reviewed more.

```python
final_df['year'].value_counts().plot(kind='bar', figsize=[20,9])
```

Run the above code and you will see that the 1927 movie only had a sample of 1 review. That score is then biased and over-inflated. You will see too that the more recent movies are better represented in reviews as I suspected:

![Image](https://lh6.googleusercontent.com/d2C-t1DLqSjRY8DpeoudyBNHG4SevXCZXFK4xoaw3QHpj_j4qnEf479Tn7wNyBqOwKAzR5GVidaRZ79XB5Eo36msA8LRBxNaJu_9Xk1VKE5oeo2Pue1TLnbjMX3y48Gc5xfOBnlZ1x9rdTktI_N2Bpg)
_Number of Movies by Year_

## Data Science Project Ideas to Take This Further

You have textual, categorical, and numeric variables here. There are a few options you could try to explore more.

One thing you could do is use Natural Language Process (NLP) to see if there are any naming conventions to movie ratings, or within the world of Sci-Fi (or if you chose to do a different genre, whatever genre you chose!). 

You could change the web scraping code to pull in many more genres too. With that you could create a new inter-genre database to see if there are naming conventions by genre.

You could then try to predict the genre based on the name of the movie. You could also try to predict the IMDB rating based on the genre or year the movie came out. The latter idea would work better in the last few decades since most observations are there.

I hope this tutorial sparked curiosity in you about the world of data science and what's possible! 

You’ll find in exploratory data analysis that there are always more questions to ask. Working with that constraint is about prioritizing based on business goal(s). It’s important to start with those objectives up front or you could be in the data weeds exploring forever.

If the field of data science is interesting to you and you want to expand your skillset and enter into it professionally, consider checking out Springboard’s [Data Science Career Track](https://www.springboard.com/courses/data-science-career-track/). In this course, Springboard guides you through all of the key concepts in depth with a 1:1 expert mentor paired with you to support you on your journey.

I've written other articles that frame data science projects in relation to business problems and walk through technical approaches to solving them on my [Medium](https://medium.com/@rileypredum). Check those out if you are interested!

Happy coding!

Riley

