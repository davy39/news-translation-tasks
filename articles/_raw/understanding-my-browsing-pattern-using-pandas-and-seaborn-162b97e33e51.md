---
title: Understanding my browsing pattern using Pandas and Seaborn
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-30T19:29:56.000Z'
originalURL: https://freecodecamp.org/news/understanding-my-browsing-pattern-using-pandas-and-seaborn-162b97e33e51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ag762hM4z29h33Pf_pkIWA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kartik Godawat


  By three methods we may learn wisdom. First, by reflection, which is noblest; Second,
  by imitation, which is easiest; and third by experience, which is the bitterest.
  — Confucius


  For the purpose of tracking the time I spend on a b...'
---

By Kartik Godawat

> By three methods we may learn wisdom. First, by reflection, which is noblest; Second, by imitation, which is easiest; and third by experience, which is the bitterest. — Confucius

For the purpose of tracking the time I spend on a browser, I use the [Limitless](https://chrome.google.com/webstore/detail/be-limitless/jdpnljppdhjpafeaokemhcggofohekbp?hl=en) extension on Chrome. While it gives me the time spent under categories, I thought it might be useful to inspect all my browsing data for the past year.

Here begins my quest to understand _all that there was_ in my browsing data.

In the process, I used Pandas and Seaborn. [Pandas](https://pandas.pydata.org/) is a python library for data manipulation and analysis. [Seaborn](https://seaborn.pydata.org) is built on top of matplotlib, which makes creating visualizations easier than ever.

#### Getting History Data

The first step in the process was to get all the browsing data for the past year. Google chrome stores the past 3 months of history on a device in SQLite format, but I ended up exporting my Google tracked data using [Google TakeOut](http://takeout.google.com). The exported json has my browsing history across all devices, including mobile.

The history stored by Chrome or tracked by Google does not give me the session information i.e. time spent on each tab. So my analysis is mainly focused on the number of visits and the time of visit rather than the session or the duration. A part of me is relieved actually, to know that Google is not tracking it _yet_.

Once the data was downloaded, I began by loading the data into a Pandas dataframe:

```
import pandas as pdwith open("BrowserHistory.json") as f:    data = json.loads(f.read())    df = pd.DataFrame(data["Browser History"])
```

```
# A possible param if differentiation is needed b/w different clientsdf.drop('client_id', axis=1, inplace=True)df.drop('favicon_url', axis=1, inplace=True)df.sample(1)
```

This is how the output looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/YA-NrAjL7fL7vNCLCI-qL2ljqXb7dfPBZTq2)

_page_transition:_ Contains info on the type of page open like reload, type & enter, link open etc. I was satisfied by filtering only on LINK and TYPED

```
df = df[(df['page_transition'] == "LINK") | (df['page_transition'] == "TYPED")]
```

#### Extracting/Extrapolating new columns(features):

To start off, I needed to break the time (in microseconds) to human-readable datetime format. Then I needed to derive features from it like hour, day, month, or day_of_week. From the URL field, extracting the top-level domain could be a useful field for analysis. So I used [tldextract](https://github.com/john-kurkowski/tldextract) to create a new domain column in the dataframe.

```
def convert_time(x):    return datetime.datetime.fromtimestamp(x/1000000)
```

```
days_arr = ["Mon","Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]def get_day_of_week(x):    return days_arr[x.weekday()]
```

```
def get_domain(x):    domain = tldextract.extract(x)[1]    sub_domain = tldextract.extract(x)[0]    if sub_domain == "mail":        return sub_domain + "." + domain    # Ugly hack to differentiate b/w drive.google.com and google.com    if domain == "google" and sub_domain=="www":        return "google_search"     return domain
```

```
# time_usec column is picked and for each row, convert_time(row) is called. The result is stored in the same dataframe under column dtdf['dt'] = df['time_usec'].apply(convert_time)...df['domain'] = df['url'].apply(get_domain)
```

Then I extrapolated the domain information to group well known domains into one or the other categories(buckets) defined by me:

```
def get_category(x):    if x in ["coursera", "kadenze", "fast", "kaggle", "freecodecamp"]:        return "Learning"    elif x in ["ycombinator", "medium", "hackernoon"]:        return "TechReads"    ...    else:        return "Other"
```

```
# Cluster popular domains into a categorydf['category'] = df['domain'].apply(get_category)
```

After all the operations, the dataframe now contains the following columns and basic analysis could begin.

**Available columns:** title,date,hour,month,is_secure,is_weekend,day_of_week,domain,category

### Exploring data and creating visualizations

#### Secure vs Insecure usage:

Once I have a dataframe with some numerical and categorical columns (month), creating a plot is super easy.

```
import seaborn as snssns.countplot(x="month", hue="is_secure", data=df)
```

![Image](https://cdn-media-1.freecodecamp.org/images/uegjuXfIh-7mrHWSIKdSoPeyOcNdtdai1YzK)
_Downward trend for http-only websites while surfing recently_

```
# Manual inspection, picking 50 random domains which were insecurerandom.sample(df[df["is_secure"] == "N"].domain.unique(), 50)
```

```
# To view data for such domainsdf[(df["domain"] == "mydomain") & (df["is_secure"] == "N")]["url"]
```

After looking at a couple of such visits, I ended up checking [this](http://www.girnationalpark.co.in/girsafari/) site. It **asks for Passport or Aadhar (India’s equivalent of SSN) number, along with email and mobile, while booking a jungle-safari, over HTTP.** I failed to notice it earlier! Final booking is handled through a separate and secure gateway. However, I still would feel much safer typing my demographics and passport details over HTTPS.

Instead of manually exploring rows, one stricter solution could be to add all such domains to an extension like [BlockSite](https://chrome.google.com/webstore/detail/block-site-website-blocke/eiimnmioipafcokbfikbljfdeojpcgbh?hl=en). They could be enabled as and when needed.

#### Weekday vs Weekend browser usage:

```
#is_weekend="Y" for saturday and sunday, "N" otherwisesns.countplot(x="hour", hue="is_weekend", data=df)
```

![Image](https://cdn-media-1.freecodecamp.org/images/GU7zJ5c5iZlF8uSdCFdkVb9BHVGH6H5WIIvL)
_Indicator that I sleep longer on weekends :P_

#### Browser usage over months:

To achieve this, I selected a subset of rows based on month’s condition and then grouped everything by the hour and date, to form a GitHub style heatmap viz.

```
from matplotlib import pyplot as plt
```

```
# Getting unique values after grouping by hour and datedf_new = df[(df["month"] >= 11)].groupby(["hour", "date"])["domain"].size()df_new = df_new.reset_index(name="count")
```

```
plt.figure(figsize = (16,5))
```

```
# Pivot the dataframe to create a [hour x date] matrix containing countssns.heatmap(df_new.pivot("hour", "date", "count"), annot=False, cmap="PuBuGn")
```

![Image](https://cdn-media-1.freecodecamp.org/images/MWUr2PnFaw8DdH6sH-daaQPSbPwA1Mi5ofwo)
_Vertically empty lines mean I was either on vacation or was not using Chrome browser._

The above code can easily be filtered. This can be done by adding more conditions to identify productive vs non-productive tab open timings and to view patterns over days. For example:

```
cat_arr = ["Shopping", "TravelBookings", "YouTube", "Social"]
```

```
df_new = df[(df["category"] in cat_arr)].groupby(["hour", "date"])["domain"].size()
```

#### Browser visits by day of week and hour:

I created another type of aggregated heatmap where I tried visualizing wrt hours and which day of the week it is.

```
df_heat = df.groupby(["hour", "day_of_week"])["domain"].size().reset_index()df_heat2 = df_heat.pivot("hour", "day_of_week", "domain")sns.heatmap(df_heat2[days_arr] , cmap="YlGnBu")
```

![Image](https://cdn-media-1.freecodecamp.org/images/md9YvYsDlyvOm-lt74KFkUSPoD8PBtpIjPQI)
_10–4 pm weekday productive hours with high browser visits on Thursday evenings_

One would expect post 5 pm Fridays through Monday morning to be of light usage. But what was interesting for me to reflect on was the light-colored areas on Wednesday evenings.

Now to use the custom categories that I manually bucketed the domains into. I generate the same heatmap again. But now with a condition on popular shopping sites. Note that the list is manually created by me based on my memory and random peeks into the unique domains I visited.

```
df_heat = df[df["category"] == "Shopping"].groupby(["hour", "day_of_week"])["category"].size().reset_index()
```

![Image](https://cdn-media-1.freecodecamp.org/images/9Nafi1Ehl3rFMRAL5cOhQy1oFhEXWjxxT0dF)

It’s good to have the satisfaction that I usually do not go on a shopping spree during office hours. However, the chart encouraged me to manually explore Thursday(20:00–21:00) and Friday(15:00–16:00, 00:00–01:00). At a higher level, I was very confident that I never shop during office timings. However, the heat-map shows some instances of such visits, shattering my illusions.

#### Most revisited stackoverflow questions:

A good friend once told me:

> Understanding stackoverflow usage helps you understand either your areas of improvements or configurations/syntax you ought to remember.

In any case, it’s good to have a cursory look at the most frequent visits for each month/quarter.

```
df_so = df[df["domain"] == "stackoverflow"].groupby(["url", "title"]).size()df_so = df_so.reset_index(name='count').sort_values('count',ascending=False)[["title", 'count']]
```

```
df_so.head(15)
```

![Image](https://cdn-media-1.freecodecamp.org/images/wIQT4eK6PSmKyUnpS7ytYzuuht482UI0GW1o)
_“Newest question” and None titled rows show there’s scope for data-preprocessing right in this context_

Maybe I should cache the page which shows me how to iterate over a Pandas dataframe!

Apart from stackoverflow, one of my most visited sites related to Pandas would be [Chris Albon’s notes on python and data-wrangling](https://chrisalbon.com/#python).

In general, it is very interesting to observe how your most-visited pages change theme over months. For example, they may move from simple questions to more complex, deeper ones. This is true as you build your understanding towards something new.

Lastly, just for fun, I ended up concatenating titles of all my stack-overflow searches for the past year. I then generated a decent looking [word-cloud](https://github.com/amueller/word_cloud) out of it.

![Image](https://cdn-media-1.freecodecamp.org/images/vJmTP5yIcxmdjD887Avv-9REXxDs8TIpoXPX)

Thank you very much for your time. If you enjoyed reading, please give me some claps so more people see the article. Thank you! And, until next time, have a great day :)

A working notebook is present on [GitHub](https://github.com/daerty0153/visualize-browser-history) with some more visualizations and some quick hacks around the data. Please do try it out with your own history dump and share interesting insights!

