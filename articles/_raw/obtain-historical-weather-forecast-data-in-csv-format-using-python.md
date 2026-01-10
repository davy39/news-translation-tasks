---
title: Obtain Historical Weather Forecast data in CSV format using Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-09T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/obtain-historical-weather-forecast-data-in-csv-format-using-python
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca193740569d1a4ca4f62.jpg
tags:
- name: worldweatheronline
  slug: worldweatheronline
- name: api
  slug: api
- name: csv
  slug: csv
- name: dataframe
  slug: dataframe
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: weather
  slug: weather
seo_title: null
seo_desc: 'By Ekapope Viriyakovithya

  Recently, I worked on a machine learning project related to renewable energy, which
  required historical weather forecast data from multiple cities.

  Despite intense research, I had a hard time finding the good data source. Mo...'
---

By Ekapope Viriyakovithya

Recently, I worked on a machine learning project related to renewable energy, which required **historical weather forecast data from multiple cities**.

Despite intense research, I had a hard time finding the good data source. Most websites restrict the access to only past two weeks of historical data. If you need more, you need to pay. In my case, I needed five years of data — hourly historical forecast, which can be costly.

### **My requirements are...**

**1\. Free — at least during trial period**

No need to provide credit card info.

**2\. Flexible**

Flexible to change forecast interval, time periods, locations.

**3\. Reproducible**

Easy to reproduce and implement in the production phase.

In the end, I decided to use data from [World Weather Online](https://www.worldweatheronline.com/developer/api/historical-weather-api.aspx). This took me less than two minutes to subscribe free trial premium API — without filling credit card info. (500 free requests/key/day for 60 days, as of 30-May-2019).

![Image](https://cdn-media-1.freecodecamp.org/images/1*kVPI57az2iE7Kjni3AhxOw.png align="left")

[*https://www.worldweatheronline.com/developer/signup.aspx*](https://www.worldweatheronline.com/developer/signup.aspx)

You can try out requests in JSON or XML format [here](https://www.worldweatheronline.com/developer/premium-api-explorer.aspx). The result is nested JSON which needed a bit pre-processing work before feeding into ML models. Therefore, I wrote some [scripts](https://github.com/ekapope/WorldWeatherOnline) to parse them into pandas DataFrames and save as CSV for further use.

### Introducing wwo-hist package

This [wwo-hist package](https://pypi.org/project/wwo-hist/) is used to retrieve and parse historical weather data from [World Weather Online](https://www.worldweatheronline.com/developer/api/historical-weather-api.aspx) into pandas DataFrame and CSV file.

**Input:** api\_key, location\_list, start\_date, end\_date, frequency

**Output:** location\_name.csv

**Output column names:** date\_time, maxtempC, mintempC, totalSnow\_cm, sunHour, uvIndex, uvIndex, moon\_illumination, moonrise, moonset, sunrise, sunset, DewPointC, FeelsLikeC, HeatIndexC, WindChillC, WindGustKmph, cloudcover, humidity, precipMM, pressure, tempC, visibility, winddirDegree, windspeedKmph

#### Install and import the package:

```py
pip install wwo-hist
```

```py
# import the package and function
from wwo_hist import retrieve_hist_data

# set working directory to store output csv file(s)
import os
os.chdir(".\YOUR_PATH")
```

**Example code:**

Specify input parameters and call ***retrieve\_hist\_data()****.* Please visit [my github repo](https://github.com/ekapope/WorldWeatherOnline) for more info about parameters setup.

This will retrieve **3-hour interval** historical weather forecast data for **Singapore** and **California** from **11-Dec-2018** to **11-Mar-2019**, save output into hist\_weather\_data variable and **CSV** files.frequency = 3

```py
FREQUENCY = 3
START_DATE = '11-DEC-2018'
END_DATE = '11-MAR-2019'
API_KEY = 'YOUR_API_KEY'
LOCATION_LIST = ['singapore','california']

hist_weather_data = retrieve_hist_data(API_KEY,
                                LOCATION_LIST,
                                START_DATE,
                                END_DATE,
                                FREQUENCY,
                                location_label = False,
                                export_csv = True,
                                store_df = True)
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ga1fGBrxkoKgfzbu align="left")

*This is what you will see in your console.*

![Image](https://cdn-media-1.freecodecamp.org/images/1*0-UJ7XO4ZG76oDlVvHQNVA.png align="left")

*Result CSV(s) exported to your working directory.*

![Image](https://cdn-media-1.freecodecamp.org/images/0*gdtco3Zi0Kv03uz9 align="left")

*Check the CSV output.*

There you have it! The script detailed is also [documented on GitHub](https://github.com/ekapope/WorldWeatherOnline).

---

Thank you for reading. Please give it a try, and let me know your feedback! If you like what I did, consider following me on [GitHub](https://github.com/ekapope), [Medium](https://medium.com/@ekapope.v), and [Twitter](https://twitter.com/EkapopeV) to get more articles and tutorials on your feed.
