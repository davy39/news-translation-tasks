---
title: 'Python Data Analysis: How to Visualize a Kaggle Dataset with Pandas, Matplotlib,
  and Seaborn'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-22T17:49:27.000Z'
originalURL: https://freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9822740569d1a4ca1855.jpg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: kaggle
  slug: kaggle
- name: Matplotlib
  slug: matplotlib
- name: pandas
  slug: pandas
seo_title: null
seo_desc: 'By Srijan

  The Indian Premier League or IPL is a T20 cricket tournament organized annually
  by the Board of Control for Cricket In India (BCCI). Eight city-based franchises
  compete with each other over 6 weeks to find the winner.

  In this article, I''m g...'
---

By Srijan

The **Indian Premier League** or IPL is a T20 cricket tournament organized annually by the Board of Control for Cricket In India (BCCI). Eight city-based franchises compete with each other over 6 weeks to find the winner.

In this article, I'm going to analyze data from the IPL's past seasons to see which teams have won the most games, how teams behave when winning a toss, who has the greatest legacy, and so on. 

I have done this analysis from a historical point of view, giving an overview of what has happened in the IPL over the years. I have used tools such as _Pandas_, _Matplotlib_ and _Seaborn_ along with _Pytho_n to give a visual as well as numeric representation of the data in front of us.

**Pandas** stands for _Python Data Analysis_ library. It is typically used for working with tabular data (similar to the data stored in a spreadsheet). Pandas provides helper functions to read data from various file formats like CSV, Excel spreadsheets, HTML tables, JSON, SQL and perform operations on them.

**Matplotlib** and **Seaborn** are two Python libraries that are used to produce plots. Matplotlib is generally used for plotting lines, pie charts, and bar graphs. 

Seaborn provides some more advanced visualization features with less syntax and more customizations. I switch back-and-forth between them during the analysis.

## Table of Contents

1. [Getting the Dataset](#heading-1-getting-the-dataset)
2. [Data Preparation and Cleaning](#heading-2-data-preparation-and-cleaning)
3. [Exploratory Analysis and Visualization](#heading-3-exploratory-analysis-and-visualization)
4. [Asking and Answering Questions](#asking-and-answering-questions)
5. [Inferences From the Analysis](#heading-5-inferences-from-the-analysis)
6. [Conclusion](#heading-6-conclusion)

## 1. Getting the Dataset

I downloaded the dataset from [Kaggle](https://www.kaggle.com/nowke9/ipldata). You will see there are two CSV (Comma Separated Value) files, matches.csv and deliveries.csv. I chose to do my analysis on matches.csv.

To find more interesting datasets, you can look at [this](https://jovian.ml/forum/t/recommended-datasets-for-course-project/11711) page.

## 2. Data Preparation and Cleaning

A dataset contains many columns and rows. It is always possible that certain rows have missing values or `NaN` for one or more columns. 

It is also possible that there might be certain columns or rows that you want to discard from your analysis. You can also combine two or more datasets for an in-depth analysis.

Cleaning the data involves making corrections to that data, leaving out unnecessary columns or rows, merging datasets, and so on.

Before taking these steps, I needed to install and import the tools (_libraries_) to be used during the analysis. I imported the libraries with different aliases such as `pd`, `plt` and `sns`.  I then set some basic styles for the plots.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=5" title="Jovian Viewer" height="308" width="800" frameborder="0" scrolling="auto"></iframe>

Notice the special command `%matplotlib inline`. It makes sure that plots are shown and embedded within the Jupyter notebook itself. Without this command, sometimes plots may show up in pop-up windows.

Using the `read_csv()` method from the _Pandas_ library, I loaded the _matches.csv_ file_._ 

Data from the file is read and stored in a `DataFrame` object - one of the core data structures in Pandas for storing and working with tabular data. I used the `_df` suffix in the variable names for data frames.

I used the name `matches_raw_df` for the data frame. This indicates that this is unprocessed data that I will clean, filter, and modify to prepare a data frame that's ready for analysis.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=9" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=10" title="Jovian Viewer" height="308" width="800" frameborder="0" scrolling="auto"></iframe>

Using the `shape` property of a `Dataframe` object, I found that the dataset contains 756 rows and 18 columns. To find the names of those columns I used the `columns` property. It returned a list of the columns in a data frame.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=11" title="Jovian Viewer" height="138" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=13" title="Jovian Viewer" height="222" width="800" frameborder="0" scrolling="auto"></iframe>

To get a summary of what the data frame contains, I used `info()`. This gives information about columns, number of non-null values in each column, their data type, and memory usage.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=15" title="Jovian Viewer" height="717" width="800" frameborder="0" scrolling="auto"></iframe>

Almost all columns except `umpire3` have no or very few null values. The presence of null values could result from a lack of information or an incorrect data entry. 

An interesting thing to observe is that, although there are no null values for the `result` column, there are some for `winner` and `player_of_match` columns. Let's find out why.

I first accessed the `result` column using _dot notation_ (`matches_raw_df.result`). Then I used `vaule_counts()` method on the `result` column.

`value_counts()` returns a _series_ which contains counts of unique values. Here, it tells us about the different values present in `result` and the total number for each of them.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=18" title="Jovian Viewer" height="218" width="800" frameborder="0" scrolling="auto"></iframe>

So, out of 756 matches (rows), 4 matches ended as _no result_. 

Cricket is an outdoor sport and unlike, say, football, play isn't possible when it's raining. It is very common to have matches abandoned due to incessant raining. Therefore, we have no winners or player of the match for these 4 matches.

For this analysis, the `umpire3` column isn't needed. So I removed the column using the `drop()` method by passing the column name and axis value. If you want to remove multiple columns, the column names are to be given in a list.

I assigned this **cleaned** data frame to `matches_df`. I used this data frame for further analysis.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=22" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=23" title="Jovian Viewer" height="308" width="800" frameborder="0" scrolling="auto"></iframe>

## 3. Exploratory Analysis and Visualization

Exploratory analysis involves performing operations on the dataset to understand the data and find patterns. It helps us make sense of the data we have. 

Visualization is the graphic representation of data. It involves producing charts that communicate those patterns among the represented data to viewers.

Now, let's take a look at the data I analyzed and what I learned in the process.

### Number of matches and teams

I tried to find the number of matches played in each season in the IPL from its inception to 2019.

Since I needed matches played each season, it made sense to group our data according to different seasons. Pandas has a `groupby()` method to achieve this, wherein I passed `season` as an argument.

Since an `id` is unique for each match (row), counting the number of ids for each season leads to what we want. I used the `count()` method on the `id` column to find the number of matches held each season. This series is assigned to the variable `matches_per_season`.

I then used the `barplot()` method from the Seaborn library to plot the series. The index of the series, that is the seasons, were given as the x-value while the values of those indices were given as y-values.

I used various `matpllotlib.pyplot` methods such as `figure()`, `xticks()` and `title()` to set the size of the plot, title of the plot, and so on. 

`figure` takes a parameter, `figsize`, which I set to `(12,6)`. Notice that the size was given as a tuple. To `xticks()`, I gave the `rotation` parameter a value of `75` to make it easier to read. 

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=30" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=31" title="Jovian Viewer" height="565" width="800" frameborder="0" scrolling="auto"></iframe>

Each season, almost 60 matches were played. However, we see a spike in the number of matches from 2011 to 2013. This is because two new franchises, the **Pune Warrior**s and **Kochi Tuskers Kerala**, were introduced, increasing the number of teams to 10.

However, Kochi was removed in the very next season, while the Pune Warriors were removed in 2013, bringing the number down to 8 from 2014 onwards.

Before the start of the 2016 season, two teams, the **Chennai Super Kings** and **Rajasthan Royals** were banned for two seasons. To make up for their absence, two new teams (the **Rising Pune Supergiants** and **Gujarat Lions**) entered the competition.

When the Chennai Super Kings and Rajasthan Royals returned, these two teams were removed from the competition.

### Analyzing the Toss results

One of the most significant events in any cricket match is the toss, which happens at the very start of a match. The toss winner can choose whether they want to bat first or second (fielding first). 

Let's see what the trend has been amongst the teams across different seasons.

Again I grouped the rows by season and then counted the different values of the `toss_decision` column by using `value_counts()`. 

Since a percentage gives a clearer picture, I divided the above result with `matches_per_season` and multiplied it by 100. This series was assigned to `toss_decision_percentage`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=35" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=36" title="Jovian Viewer" height="643" width="800" frameborder="0" scrolling="auto"></iframe>

Here, `toss_decision_percentage` is a series with _multi-index_. If we print the index of the series using the `index` property, we see it is of the form `(2008, 'bat'), (2008, 'field')` and so on. 

The series used both `season` and `toss_decision` as an index. But I only wanted the seasons to be an index. I used `unstack()` to achieve this. 

By using the `unstack()` method on the series, it converted the values of `toss_decision` (that is, `bat` and `field`) into separate columns.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/85&cellId=38" title="Jovian Viewer" height="490" width="800" frameborder="0" scrolling="auto"></iframe>

Next I used the `plot()` method from Matplotlib to represent these values as bar charts. `plot()` has a parameter `kind` which decides what type of plot to draw. The value was set to `bar`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/85&cellId=39" title="Jovian Viewer" height="484" width="800" frameborder="0" scrolling="auto"></iframe>

For 2008-2013, teams seemed to favour both batting first and second. For this period, teams chose to bat first more in 2009, 2010 and 2013. On the other hand, they chose fielding first more in 2008 and 2011. Things were even-steven in 2012.

This could be because IPL and T20 cricket in general was in its budding stages. So, teams were probably learning and trying to figure out which option would be more beneficial.

However, since 2014, teams have overwhelmingly chosen to bat second. Especially since 2016, teams have chosen to field first **more than 80%** of the time.

Batting first requires that the team gauge the conditions and the pitch and then set a target accordingly. Chasing is less complicated, as there is a fixed target to achieve. 

Conditions have also become more batsman-friendly and the skills of the batsmen have increased tremendously (_read more_ [_here_](https://www.espncricinfo.com/story/_/id/18568387/tim-wigmore-how-batting-second-become-more-fruitful-more-popular)).

### Number of Wins

We saw how teams in the recent past have chosen to bat second more than 4 out of 5 times. Did this decision transform the results? Let's see.

For `wins_batting_first`, the values of `win_by_wickets` has to be 0. Also, the `result` column should have a value of `normal` since tied matches also have win margins as 0. This condition was stored as `filter1`.

Similarly, for `wins_fielding_first`, the the value of `win_by_runs` has to be 0 and the `result` column should have a value of `normal`. This condition was stored as `filter1`.

In both the series, I used `count()` method on `winner` column to find the won matches in the filtered conditions. I divided the results with `matches_per_season` calculated earlier to give a better understanding.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/88&cellId=43" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/88&cellId=44" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/88&cellId=45" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/89&cellId=46" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>

To plot these two series together, I combined them using Pandas' `concat()` method. I passed the two series names as a list and set the value of `axis` as `1`. This gives us a new data frame which was stored as `combined_wins_df`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/89&cellId=47" title="Jovian Viewer" height="547" width="800" frameborder="0" scrolling="auto"></iframe>

Next I plotted `combined_wins_df` as a bar chart using `plot()`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=44" title="Jovian Viewer" height="484" width="800" frameborder="0" scrolling="auto"></iframe>

We saw earlier that for 2008-2013, teams faced a conundrum whether to bat first or field first. This is partially visible in the results as well. 

The wins from batting first are very close to that from fielding first. However, there is just one season where teams batting first won more, with things being equal in 2013.

Again, since 2014, things have been in favour of teams chasing except 2015. Leaving out 2015, things have been overwhelmingly in favour of teams fielding first.

So, teams choosing to field more have been justified in their decisions.

### Teams with "History"

In leagues across different sports, there is always talk about teams with "history" – teams that have played the most in the league and continue to do so. Let's find those teams in the IPL.

Now, between two teams A and B, it can be "A vs B" or "B vs A", depending on how the data entry has been done. So I decided to count the total number of different values for both the `team1` and `team2` columns using `value_counts()`. Then I added them together.

I sorted the results in descending order using the `sort_values()` method from Pandas. The `ascending` parameter was set to `False`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=48" title="Jovian Viewer" height="470" width="800" frameborder="0" scrolling="auto"></iframe>

Here, I used `sns.barplot()` to plot the graph.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=49" title="Jovian Viewer" height="451" width="800" frameborder="0" scrolling="auto"></iframe>

The **Mumbai Indians** have played the most matches. They are followed by the Royal Challengers Bangalore, Kolkata Knight Riders, Kings XI Punjab and Chennai Super Kings.

The Chennai Super Kings and Rajasthan Royals could have been higher had they not been banned.

You will see there are two teams from Delhi, the **Delhi Daredevils** and **Delhi Capitals**. This resulted from a change in ownership and then team name in 2018.

It's a similar story for the **Deccan Chargers** and **Sunrisers Hyderabad**, as the Deccan Chargers were removed from the IPL in 2013 and the Sunrisers came in their place.

Also, there are two teams with almost same name: the **Rising Pune Supergiants** and **Rising Pune Supergiant**. They are same team, and there was no change in ownership – it has more to do with superstitions.

In the 2016 season, the Rising Pune Supergiants finished 7th. The owners changed the captain for 2017 and also **dropped the 's'** from Supergiants. Well, it paid off as they finished as runner-up that season!

### Teams with "Legacy"

Now, teams may have a lot of history but it's their "legacy" – how often they win – that makes them popular and attracts new and neutral fans.

To find such teams, I simply used `value_counts()` on the `winner` column. This gives us the number of matches that each team has won.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=53" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=54" title="Jovian Viewer" height="433" width="800" frameborder="0" scrolling="auto"></iframe>

So Mumbai has the most wins. But a better metric to judge would be the win percentage. To find the win percentage, I divided `most_wins` by `total_matches_played` to find the `win_percentage` for each team.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=57" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=58" title="Jovian Viewer" height="444" width="800" frameborder="0" scrolling="auto"></iframe>

The Rising Pune Supergiant and Delhi Capitals have the highest win percentage. This is largely because they have played fewer matches compared to most teams. Especially Rising Pune Supergiant, which technically became a new team after dropping the 's'.

The Chennai Super Kings, despite playing two fewer seasons than the Mumbai Indians, had only 9 fewer victories. They, along with the Mumbai Indians, are the only two teams in the top 5 that were also part of the IPL in 2008.

**Chennai** and **Mumbai** are the teams with the most legacy.

## 4. Asking and Answering Questions from the Data

We've already gained some insights about the IPL by exploring various columns of our dataset. 

Let's ask some specific questions, and try to answer them using data frame operations and interesting visualizations.

### Q. Who has won the IPL tournament?

* Group the rows according to seasons using `groupby()`.
* Find the last match of each season, that is, the final using `tail()`. It returns the last n rows from a Dataframe object or series based on position.
* Sort the values per season using `sort_values()`.
* Count the different winners and the times they won using `value_counts()` on `winner`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=65" title="Jovian Viewer" height="134" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=66" title="Jovian Viewer" height="264" width="800" frameborder="0" scrolling="auto"></iframe>

Then I plotted the series `ipl_winners` using `sns.barplot()`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=67" title="Jovian Viewer" height="353" width="800" frameborder="0" scrolling="auto"></iframe>

Mumbai and Chennai, our _legacy_ teams, have won the IPL at least 3 times. The Sunrisers Hyderabad are the only team that joined the league later and won the trophy.

### Q. Which are the most and least consistent teams across all seasons?

* Created a data frame between different values of `winner` and `season` using `pd.crosstab()`.
* Plotted the data frame as a heatmap.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=71" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=72" title="Jovian Viewer" height="208" width="800" frameborder="0" scrolling="auto"></iframe>

`pd.crosstab()` gives a simple cross-tabulation of the `winner` and `season` columns. For each different value of `winner`, `pd.crosstab()` finds its frequency for each different value in `season`. 

Then I plotted  `matches_won_each_season` using `sns.heatmap()`. I passed the data frame `matches_won_each_season`, with `annot` as `True` to have the values shown as well. Here, the darker color indicates more matches won.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=73" title="Jovian Viewer" height="496" width="800" frameborder="0" scrolling="auto"></iframe>

The **Chennai Super Kings** have been the most consistent team, winning at least 8 matches in each of the seasons they have played. This is backed up by the fact that they are the **only** team to reach the playoffs stage every season.

At the other end of the spectrum are 3 teams, the **Delhi Daredevils**, **Kings XI Punjab** and **Rajasthan Royals**. All three of them have had two seasons where they performed really well. However, they have been pretty average during the other seasons.

### Q. What has been the biggest margin of victory in terms of runs in the IPL?

* Filter the data frame using the required condition.
* Sort the values in descending order using `sort_values()`.
* Find the biggest 10 victories in the list using the `head()` method. It works opposite to `tail()`, returning the first n rows.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=81" title="Jovian Viewer" height="134" width="800" frameborder="0" scrolling="auto"></iframe>

I plotted the filtered data frame `highest_wins_by_runs_df` using `sns.scatterplot()`. For the `x` parameter I used `season`, and I used `win_by_runs` as the `y` parameter. I made the size of the points bigger for the top 10 victories using the `s` parameter.

To put emphasis on the top 10 victories, I used a different color as well as annotated those data points using `plt.annotate()`. The first parameter is the text of the annotation. The position of the point to be annotated is given as a tuple.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=82" title="Jovian Viewer" height="501" width="800" frameborder="0" scrolling="auto"></iframe>

The biggest margin of victory by runs is **146 runs**. In 2017, the Mumbai Indians defeated the Delhi Daredevils by this margin. The Royal Challengers Bangalore have 3 victories amongst the top 5.

### Q. Mumbai and Chennai are the two most successful teams so far. Which team leads in the head-to-head record?

* Filter the data frame using the required condition to find the matches played between the two teams.
* Use the `value_counts()` on the `winner` column to find how many times each of the teams have won.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=105" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=108" title="Jovian Viewer" height="180" width="800" frameborder="0" scrolling="auto"></iframe>

I plotted the series `mivcsk` as a bar chart for a better visualization.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=109" title="Jovian Viewer" height="507" width="800" frameborder="0" scrolling="auto"></iframe>

MI have dominated CSK and are leading the head-to-head record 17-11. We can see their dominance especially in the 2019 season, where the MI defeated the CSK 4 out of 4 times they met, including the playoff and the final.

## 5. Inferences from the Analysis

We have drawn some interesting inferences and now know more about the IPL than when we started. Here's a summary of what we learned through our analysis:

* Almost 60 matches are played in every IPL season amongst 8 teams.
* There has been an attempt to expand the IPL to 10 teams but the 8 teams idea was brought back and has been continued since.
* For the first six seasons (2008-2013), teams were figuring out whether batting first or chasing would be better after winning the toss. This could be down to the fact that the IPL and T20 cricket were both in their early stages so teams were trying different strategies.
* But, since 2014, teams have preferred chasing, especially in the past 4 seasons (2016-2019) where teams have chosen to field more than 4 times out of 5. This is likely because having a set total to chase makes things simpler. This could also result from teams preferring to chase in ODIs as well.
* Though teams have overwhelmingly chosen to field first, the win percentage after choosing to bat or field is not that one-sided. However, their difference is on the rise.
* Mumbai Indians have played the most matches in the IPL. Due to the brief expansion, change of owners, and removal and banning of teams, there have been 15 teams who have played in the IPL.
* Chennai and Mumbai are the two teams with the highest win percentage. The fact that they are the only two teams that were part of the first season as well, in the top 5, shows their dominance.
* Mumbai Indians have the won the IPL 4 times, the most. They are followed by Chennai at 3 and Kolkata Knight Riders at 2. Sunrisers Hyderabad, Deccan Chargers and Rajasthan Royals complete the IPL Champions list, all winning once each.
* 146 runs is the largest margin of victory by runs. Mumbai Indians defeated Delhi Daredevils by this margin in 2017. The largest margin for victory by wickets is 10, which has been achieved many times.
* The two heavyweights, Mumbai and Chennai, have a head-to-head record in favour of Mumbai at 17-11. Mumbai have had the upper hand in the 2019 season every time they met, including the final.

## 6. Conclusion

In this article, we did a bunch of analysis and saw some interesting visualizations. However, this was just scratching the surface.

You can perform more interesting analysis on _matches.csv_ as a standalone data set. But combining _deliveries.csv_ with this dataset could lead to more in-depth analysis.

I did this data analysis and visualization as a project for the 6-week course [Data Analysis with Python: Zero to Pandas](https://www.freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn/zerotopandas.com). This course was conducted by [Jovian.ml](https://jovian.ml) in partnership with [freeCodeCamp.org](https://www.freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn/www.freecodecamp.org). Check out the project [here](https://jovian.ml/srijansrj5901/ipl-data-analysis).

Also, the IPL is on right now. Go watch it and enjoy!

