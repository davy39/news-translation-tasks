---
title: I Built A Jupyter Notebook That Will Analyze Cryptocurrency Portfolios For
  You
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-20T10:35:13.000Z'
originalURL: https://freecodecamp.org/news/i-built-a-jupyter-notebook-that-will-analyze-cryptocurrency-portfolios-for-you-bdaba618aeca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yclB_TfehNu8DxAADDBzXg.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Cryptocurrency
  slug: cryptocurrency
- name: data scientist
  slug: data-scientist
- name: Investing
  slug: investing
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Grant Bartel

  The amount of engagement in the crypto investment space needs no introduction. With
  market caps, volumes, and public awareness on the rise, I thought I’d put together
  a simple Jupyter notebook to get a clearer and broader viewpoint in...'
---

By Grant Bartel

The amount of engagement in the crypto investment space needs no introduction. With [market caps, volumes, and public awareness on the rise](http://www.ibtimes.co.uk/year-cryptocurrencies-became-mainstream-1654616), I thought I’d put together a simple Jupyter notebook to get a clearer and broader viewpoint into the investment activities within my own crypto portfolio.

TL;DR [here’s the code](https://github.com/grantathon/crypto_portfolio_analysis) ;)

### Why Should We Analyze Our Portfolios?

Because we’re definitely missing important details about our investments by only looking at the total value of our (potentially fat) wallets — even though I enjoy looking at Blockfolio from time to time. Because seeing our Ripple go to the moon and overshadow the rest of our investments is likely increasing our financial risk substantially. Because we all want our money to grow, but achieving this by picking a diverse set of cryptos is easier and safer than picking a moonshot that could end up a dud (and make us broke).

And let’s face it, the market gains are just too big for us to be left in the dark on the true characteristics of our investment portfolios.

### Important Portfolio Characteristics

Now there are several characteristics of our portfolio that we should take a good look at, including return **and** risk. But a lot of the time we’re fixated on one and not the other.

We can look at return in several ways: the amount of money we’ve made from the beginning to the current date, the average rate of money we’ve made over specific time periods (e.g., annual returns), how much better our investments did when compared to several characteristics of a benchmark (e.g., [alpha](https://www.investopedia.com/terms/a/alpha.asp)), and even the annual compound rate it would have taken to get to our current investment based on our starting point (i.e., [CAGR](https://en.wikipedia.org/wiki/Compound_annual_growth_rate)).

As important, if not more, is how we look at risk and its effect on return. I don’t know about you, but I want to make sure I’m making a good return based on an amount of risk I feel comfortable with. If we take on a huge amount of risk to make one particular return when we could have taken much less risk to make that very same return, the path to take for a more **efficient investment** is clear.

This is where understanding volatility, correlations, and risk-adjusted returns come into play by computing statistics such as standard deviation of returns (or volatility), [beta](https://www.investopedia.com/terms/b/beta.asp), the [Sharpe ratio](https://en.wikipedia.org/wiki/Sharpe_ratio), and the [Sortino ratio](https://en.wikipedia.org/wiki/Sortino_ratio).

And while we can compute all the statistics under the sun to measure our portfolio’s performance, it doesn’t do much good if we don’t include a reference point to see how well we’re doing in comparison. This is called a [benchmark](https://www.investopedia.com/terms/b/benchmark.asp), and we’ll be using the golden boy of cryptocurrencies: Bitcoin.

### Notebook Walk-Through

So I don’t want to display a bunch of code here because I think you should go through the notebook yourself and get a feel for things. Don’t be afraid, the notebook includes some clear explanations and the code is commented! It’ll also help in better understanding this post. If you want, clone [the repo](https://github.com/grantathon/crypto_portfolio_analysis) and give it a whirl first. However, I will show you results through some statistics and nice visualizations.

To start, we need to create a tradesheet that emulates how we invested our portfolio. The one below is included in [the repo](https://github.com/grantathon/crypto_portfolio_analysis). These are actually the same cryptos I invested in and the times I bought and sold them up until now, but the amount of money and the allocations (i.e., the amount I bought and sold) are not ;)

![Image](https://cdn-media-1.freecodecamp.org/images/XzoSg0XtQ6s8pL4cdk3sKG-k381rkitWdTtr)

You can think of the tradesheet as our **investment strategy**. These are the trades we decided to take based on our wizardry powers or what an algorithm told us.

![Image](https://cdn-media-1.freecodecamp.org/images/sikS8FYcWs5FmvVcfZY2naHH5UxGyMPDn3PJ)
_Source: [Playstarbound](https://community.playstarbound.com/threads/glitch-ship-ai-feedback.80652/page-11" rel="noopener" target="_blank" title=")_

Along with the tradesheet, we also need historical market data. I chose to go with something simple: download some CSVs from [CoinGecko](https://www.coingecko.com/) and throw them into a data folder. Pulling data from an API would be better though!

Now we want to run a backtest on our investment strategy. Simply put, running a backtest allows us to go back in time to our first trade, walk forward in time, and simulate the trading activity that occurred in our portfolio up until today. A backtester can be very sophisticated and can be used in a lot of different scenarios (to the finance geeks: pun intended), but in our case it’s rather straightforward.

![Image](https://cdn-media-1.freecodecamp.org/images/I05CqzVIRz3ccjLIjcy85QUBz5apBZ4xWAcG)

Based on the statistics above, it’s clear that our portfolio did fairly well when compared to our benchmark. The returns are better, volatility is only slightly worse, and our beta is surprisingly below 100%. And look at that alpha!

OK. Numbers are nice, but I want to see some charts.

![Image](https://cdn-media-1.freecodecamp.org/images/pnWUDH7fXvwbY-DlQ2wiYuK1inrGjP4P9vnY)

Well that’s intimidating. The above chart shows how the USD value of our portfolio evolved over time including all of our cash flows (i.e., deposits and withdrawals). While it’s nice to visualize this, it’s hard to get a clear idea of how our portfolio did in true performance when cash flows are included. For example, if I deposited $1 million (I wish), the portfolio would appear to have a HUGE spike!

![Image](https://cdn-media-1.freecodecamp.org/images/aI9DYZ7J2guZE1BcBaJ04dLfbPDaavgNcBPm)

Now that’s better. By removing the daily returns when cash flows were witnessed, we have a more accurate representation of the true performance of our portfolio. Fortunately, we have a very small number of cash flows, so this method is acceptable. As you can see, it took us some time to catch up to Bitcoin, but it did and eventually surpassed it (thanks [Golem](https://golem.network/) and [NEO](https://neo.org/)).

![Image](https://cdn-media-1.freecodecamp.org/images/H5PJZhnLSD23zJVoy7jFUAO8vDDzNGesxa3c)

Actually, you can see that after the crazy Bitcoin, Ethereum, and Litecoin boom (aka the Coinbase boom), our portfolio became more diversified. This surely had a lot to do with the dampening of the upcoming Bitcoin drawdowns and the likely larger returns experienced among the newly added assets.

![Image](https://cdn-media-1.freecodecamp.org/images/jD3HVn19ylfyNF6clE3QMxThd9ZbX6Q0WGVH)

Well there you have it. Clearly, our portfolio experienced much less volatility (i.e., risk) after diversifying. Diversification (and luck) for the win!

![Image](https://cdn-media-1.freecodecamp.org/images/BcXX6mRbl6s-S5cUvheXUxWzYQNLcNAbIQbd)

For me, this is the most interesting plot. This is a matrix that represents the correlations between all of the assets in our portfolio. While a lot of assets had a [medium to high correlation](https://statistics.laerd.com/statistical-guides/pearson-correlation-coefficient-statistical-guide.php) with one another, [Bitcoin Cash](https://www.bitcoincash.org/) had a very low correlation to every single asset. You can even see that it was negatively correlated with [OmiseGO](https://omisego.network/)! Correlations do change over time, but it’s nonetheless interesting to see these types of relationships within our portfolio.

Again, go ahead and clone [the repo](https://github.com/grantathon/crypto_portfolio_analysis) and play around a bit so you can understand in more detail how we went about analyzing our portfolio. You can even add your own tradesheet to get a glimpse into yours. And if you find bugs, let me know!

### Summing It All Up

I hope you’ve gained a better appreciation for why it’s important to look at your portfolio through various lenses. It’s hard to get a clear understanding from just visualizing asset price movements, especially with all that’s been going on lately in the crypto space. Also, it’s not always clear how much risk we’re taking on over time, and how those risks will evolve when we invest.

What is clear is that diversification in such a market is important, because none of us knows where this market is going. With that in mind, best to keep an eye on your ship while weathering the storms and HODL.

By the way, none of this should be treated as investment advice and same goes for the code. Whichever investments you pursue are purely at your own discretion.

Full disclosure: At the time of writing this article I was invested in BCH, BTC, ETH, GNT, LTC, NEO, and OMG.

_I’m Grant and I’m a freelance SEO and content professional. If you’re looking to grow your brand's organic search traffic, I can help with your [fintech SEO](https://www.writefintech.com/). Cheers!_

