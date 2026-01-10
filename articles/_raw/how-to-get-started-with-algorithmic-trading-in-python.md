---
title: How to Get Started with Algorithmic Trading in Python
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-01-04T17:56:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-algorithmic-trading-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Fashion-Beauty-Lifestyle-Youtube-Channel-Art--2-.png
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: null
seo_desc: 'When I was working as a Systems Development Engineer at an Investment Management
  firm, I learned that to succeed in quantitative finance you need to be good with
  mathematics, programming, and data analysis.

  Algorithmic or Quantitative trading can be ...'
---

When I was working as a Systems Development Engineer at an Investment Management firm, I learned that to succeed in quantitative finance you need to be good with mathematics, programming, and data analysis.

[Algorithmic or Quantitative trading](https://www.freecodecamp.org/news/algorithmic-trading-in-python/) can be defined as the process of designing and developing statistical and mathematical trading strategies. It is an extremely sophisticated area of finance.

**So, the question is how do you get started with Algorithmic Trading?**

I am going to walk you through five essential topics that you should study in order to pave your way into this fascinating world of trading.

I personally prefer Python as it offers the right degree of customization, ease and speed of development, testing frameworks, and execution speed. Because of this, all these topics are focused on [**Python for Trading**](https://medium.com/datadriveninvestor/getting-starting-with-algorithmic-trading-with-python-1ae169cc1705).

## 1\. Learn [Python Programming](https://www.freecodecamp.org/learn/)

In order to have a flourishing career in Data Science in general, you need solid fundamentals. Whichever language you choose, you should thoroughly understand certain topics in that language.

Here’s what you should look to master in the Python ecosystem for data science:

* [**Environment Setup**](https://towardsdatascience.com/ideal-python-environment-setup-for-data-science-cdb03a447de8) — this includes creating a virtual environment, installing required packages, and [working with Jupyter notebook](https://towardsdatascience.com/the-complete-guide-to-jupyter-notebooks-for-data-science-8ff3591f69a4)s or Google colabs.
    
* **Data Structures** — some of the most important pythonic data structures are lists, dictionaries, NumPy arrays, tuples, and sets. I’ve collected a [few examples](https://medium.com/p/python-fundamentals-for-data-science-6c7f9901e1c8) in the linked article for you to learn these.
    
* **Object-Oriented Programming —** As a quant analyst, you should make sure you are good at writing well-structured code with proper classes defined. You must learn to use objects and their methods while using external packages like Pandas, NumPy, SciPy, and so on.
    

The freeCodeCamp curriculum also offers a certification in [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-course/) to help you get started with the basics.

## Learn How to Crunch Financial Data

Data analysis is a crucial part of finance. Besides learning to handle dataframes using Pandas, there are a few specific topics that you should pay attention to while dealing with trading data.

### How to exploring data using Pandas

One of the most important packages in the Python data science stack is undoubtedly Pandas. You can accomplish almost all major tasks using the functions defined in the package.

Focus on creating dataframes, filtering (`loc`, `iloc`, `query`), descriptive statistics (summary), join/merge, grouping, and subsetting.

### How to deal with time-series data

Trading data is all about time-series analysis. You should learn to resample or reindex the data to change the frequency of the data, from minutes to hours or from the end of day OHLC data to end of week data.

For example, you can convert 1-minute time series into 3-minute time series data using the resample function:

```python
df_3min = df_1min.resample('3Min', label='left').agg({'OPEN': 'first', 'HIGH': 'max', 'LOW': 'min', 'CLOSE': 'last'})
```

## 3\. How to Write Fundamental Trading Algorithms

A career in quantitative finance requires a solid understanding of statistical hypothesis testing and mathematics. A good grip over concepts like multivariate calculus, linear algebra, probability theory will help you lay a good foundation for designing and writing algorithms.

You can start by calculating moving averages on stock pricing data, writing simple algorithmic strategies like moving average crossover or mean reversion strategy and learning about relative strength trading.

After taking this small yet significant leap of practicing and understanding how basic statistical algorithms work, you can look into the more sophisticated areas of machine learning techniques. These require a deeper understanding of statistics and mathematics.

Here are two books you can start with:

* [Quantitative Trading: How to build your own Algorithmic Trading Business](http://www.amazon.com/gp/product/0470284889/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470284889&linkCode=as2&tag=quant0f-20) —By Dr. Ernest Chan
    
* Book on [Algorithmic Trading and DMA](http://www.amazon.com/gp/product/0956399207/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0956399207&linkCode=as2&tag=quant0f-20) — By Barry Johnson
    

And here are a couple courses that will help you get started with Python for Trading and that cover most of the topics that I’ve captured here:

* [Python for Trading by Multi Commodity Exchange offered by Quantra](https://quantra.quantinsti.com/course/python-for-trading?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=python_finance_article)
    
* [Algorithmic Trading with Python](https://www.freecodecamp.org/news/algorithmic-trading-using-python-course/) – a free 4-hour course from Nick McCullum on the freeCodeCam YouTube channel
    

You can get 10% off the Quantra course by using my code **HARSHIT10.**

## 4\. Learn About Backtesting

Once you are done coding your trading strategy, you can’t simply put it to the test in the live market with actual capital, right?

The next step is to expose this strategy to a stream of historical trading data, which would generate trading signals. The carried out trades would then accrue an associated profit or loss (P&L) and the accumulation of all the trades would give you the total P&L. This is called backtesting.

Backtesting requires you to be well-versed in many areas, like mathematics, statistics, software engineering, and market microstructure. Here are some concepts you should learn to get a decent understanding of backtesting:

* You can start by understanding technical indicators. Explore the Python package called TA\_Lib to use these indicators.
    
* Employ momentum indicators like parabolic SAR, and try to calculate the transaction cost and slippage.
    
* Learn to plot cumulative strategy returns and study the overall performance of the strategy.
    
* A very important concept that affects the performance of the backtest is bias. You should learn about optimization bias, look-ahead bias, psychological tolerance, and survivorship bias.
    

## 5\. Performance Metrics — How to Evaluate Trading Strategies

It’s important for you to be able to explain your strategy concisely. If you don’t understand your strategy, chances are on any external modification of regulation or regime shift, your strategy will start behaving abnormally.

Once you understand the strategy confidently, the following performance metrics can help you learn how good or bad the strategy actually is:

* **Sharpe Ratio** — heuristically characterises the risk/reward ratio of the strategy. It quantifies the return you can accrue for the level of volatility undergone by the equity curve.
    
* **Volatility** — quantifies the “risk” related to the strategy. The Sharpe ratio also embodies this characteristic. Higher volatility of an underlying asset often leads to higher risk in the equity curve and that results in smaller Sharpe ratios.
    
* **Maximum Drawdown** — the largest overall peak-to-trough percentage drop on the equity curve of the strategy. Maximum drawdowns are often studied in conjunction with momentum strategies as they suffer from them. Learn to calculate it using the `numpy` library.
    
* **Capacity/Liquidity** — determines the scalability of the strategy to further capital. Many funds and investment management firms suffer from these capacity issues when strategies increase in capital allocation.
    
* **CAGR —** measures the average rate of a strategy’s growth over a period of time. It is calculated by the formula: (cumulative strategy returns)^(252/number of trading days) — 1
    

## Further Resources

This article served as a suggested curriculum to help you get started with algorithmic trading. It is a good list of concepts to master.

Now, the question is what resources can help you get up to speed with these topics?

Here are a few classic books and useful courses with assignments and exercises that I found helpful:

* **\[Course\]** [**Python for Trading Course by Multi Commodity Exchange offered by Quantra**](https://quantra.quantinsti.com/course/python-for-trading?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=python_finance_article) **\[PromoCode: HARSHIT10\]**
    
* **\[Book\]** [**Quantitative Trading: How to Build Your Own Algorithmic Trading Business**](http://www.amazon.com/gp/product/0470284889/ref=as_li_tf_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470284889&linkCode=as2&tag=quant0f-20) **— Ernest Chan**
    
* **\[Course\]** [**Dr. Ernest Chan’s trading courses on the Quantra Platform**](https://quantra.quantinsti.com/courses?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=python_finance_article)
    
* **\[Book\]** [**Python for Finance — Yves Hilpisch**](https://www.amazon.in/Python-Finance-Yves-Hilpisch/dp/1491945281)
    
* **\[Journals\]:** [arXiv](http://arxiv.org/archive/q-fin), [Wiley’s Mathematical finance](http://onlinelibrary.wiley.com/journal/10.1111/%28ISSN%291467-9965), [computational finance](http://www.risk.net/type/journal/source/journal-of-computational-finance).
    

### [Data Science with Harshit](https://www.youtube.com/c/DataSciencewithHarshit?sub_confirmation=1)

%[https://www.youtube.com/watch?v=yapSsspJzAw&t] 

With this channel, I am planning to roll out a couple of [series covering the entire data science space](https://towardsdatascience.com/hitchhikers-guide-to-learning-data-science-2cc3d963b1a2?source=---------8------------------). Here is why you should be subscribing to the [channel](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ):

* This series would cover all the required/demanded quality tutorials on each of the topics and subtopics like [Python fundamentals for Data Science](https://towardsdatascience.com/python-fundamentals-for-data-science-6c7f9901e1c8?source=---------5------------------).
    
* Explained [Mathematics and derivations](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea?source=---------9------------------) of why we do what we do in ML and Deep Learning.
    
* [Podcasts with Data Scientists and Engineers](https://www.youtube.com/watch?v=a2pkZCleJwM&t=2s) at Google, Microsoft, Amazon, etc, and CEOs of big data-driven companies.
    
* [Projects and instructions](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb?source=---------2------------------) to implement the topics learned so far. Learn about new certifications, Bootcamp, and resources to crack those certifications like this [**TensorFlow Developer Certificate Exam by Google.**](https://youtu.be/yapSsspJzAw)
    

If this tutorial was helpful, you should check out my data science and machine learning courses on [Wiplane Academy](https://www.wiplane.com/). They are comprehensive yet compact and helps you build a solid foundation of work to showcase.
