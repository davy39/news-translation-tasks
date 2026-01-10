---
title: A quick guide to understanding incentive stock options
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T22:36:24.000Z'
originalURL: https://freecodecamp.org/news/understanding-incentive-stock-options-ec4c0dc1498f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7OMEduetLbgtrrUyDiKlAA.png
tags:
- name: Stock Options
  slug: stock-options
- name: engineering
  slug: engineering
- name: jobs
  slug: jobs
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Katie Siegel

  This article is a non-official resource on evaluating startup stock packages. Keep
  in mind that I am not a CPA or a lawyer, so this information has been cobbled together
  from my own memory, experiences as a software engineer, and cach...'
---

By Katie Siegel

This article is a non-official resource on evaluating startup stock packages. Keep in mind that I am not a CPA or a lawyer, so this information has been cobbled together from my own memory, experiences as a software engineer, and cache of internet articles.

There are three main types of stock options:

* ISOs, or incentive stock options,
* NSOs, or non-qualified stock options,
* and RSUs, or restricted stock units.

ISOs tend to be awarded by smaller startups, and companies transition into awarding RSUs as they grow in size and valuation. Typically, stock packages transition from ISOs to RSUs when a company raises Series D funding or exceeds a ~$1B valuation, and ISOs become too expensive for employees to purchase. This blog post only deals with ISOs.

Stock options allow you to purchase shares in a company. You can purchase shares at the **strike price**, which is a price decided by a third party accounting firm, approved by the board, and assigned to you after you join the company. There is also a fair market value (FMV) associated with each share — this a value higher than your strike price that was decided the last time the company was externally valued (e.g. a funding round, though some companies will also regularly update their FMV even if they aren’t actively fundraising).

### Initial questions to ask

To value your stock options, you should ask the following questions:

**“What is my strike price per share?”**

If you are evaluating a stock package before joining a company, keep in mind that your strike price is decided after you join, so it may be higher than the current strike price per share. Your strike price could change if the company raises another round of funding or gets a 409a valuation before you join.

**“What is the total number of shares for the company?”**

This number helps you understand the percentage of the company you will own — your shares divided by the total number of shares.

**“Does the company offer early exercise?”**

This means that you can purchase your options before you vest them (but also before you know if your company will be successful). Most startups offer early exercise. Early exercising your options helps you avoid alternative minimum tax (covered below), and helps you avoid short term federal capital gains tax.

**“Does the company offer 83(b) election?”**

If you can early exercise, the answer to this question is yes. An 83(b) election is a way to inform the company and the IRS that you’ve exercised your options. You must submit an 83(b) to reap the tax benefits of early exercise.

**“How long after leaving the company do I have to exercise my shares?”**

This is the time window after which you lose the ability to purchase your stock options after leaving the company. For pre-series D startups, this window is typically 90 days. Many later-stage startups offer a 7 year exercise window, because it usually costs tens of thousands to fully exercise your options, and employees might not be able to afford the sum of money.

### What else you need to know

The company must be able to answer the above five questions, or it is a huge red flag. This holds for any company, no matter how small.

Once you have the answer to the questions above, you can calculate the value of your options package and answer the following questions:

**“How much do I have to pay to exercise my options?”**

Multiply the number of shares by the current strike price per share. This is a good estimate of the amount you’ll have to pay, but the real amount will probably be slightly higher. If the company raises money between the time you sign your offer and the time you join, the amount might be much higher.

Keep in mind that you are spending liquid money to purchase illiquid stock, and that companies often provide a deadline of 90 days after termination of employment to buy stock options. So, if the amount you have to spend to purchase your stock is overwhelming, you may be unable to afford purchasing your options until your company has a liquidity event. This is the “golden handcuffs” problem — a financial weight tying you to working at the company for longer than you might otherwise want.

**“How much is my equity package worth?”**

Multiply the number of shares by the current fair market value per share. In general, this is the amount your options are “worth,” but there are a few factors that might push that number higher. If the startup raised money a while ago, has grown in headcount, and/or has increased revenue, the startup’s options are worth more than just after the most recent raise.

However, keep in mind that you have to pay a certain amount of money to get your options, so subtract this purchasing cost in your calculations. Also, keep in mind that all startups bear some amount of risk; your stock options could end up being worthless if the startup folds or has an underwhelming exit.

### Dealing with taxes

**“How much will I have to pay in taxes when I exercise my options?”**

For ISOs, the two main taxes you should consider are capital gains and AMT.

#### Capital gains tax

If you hold your stock for at least a year after exercising, you will pay long term capital gains on the amount your stock appreciated from the purchase price, **when you sell that stock**. For engineers, this long term capital gains rate will be 15–20%, compared to the much higher short term capital gains rate, which is equal to your income tax rate. You only have to pay short term capital gains tax on your stock options if you hold them for less than a year or if you were awarded NSOs.

#### AMT

You will be assigned a strike price when joining the company. Let’s call this “strike price A”. Throughout the company’s lifetime, the strike price will gradually rise. At some point, you will decide to exercise some options; let’s call the strike price at this point “strike price B.” From these two numbers, we can calculate the net value you’re gaining by exercising:

> net stock increase =

> (strike price B — strike price A) * # of shares

From that amount, you can calculate your AMT (alternative minimum tax), which is 26–28% of that net value amount. However, some income is exempt from AMT, which for a single person, is typically $70.3k for taxpayers filing individually or $109.4k for taxpayers filing jointly. (If you make over $500k per year, some exemptions may not apply). So, the real AMT formula is:

> AMT =

> (net stock increase+other income — exemption)*AMT rate

If your calculated AMT is less than your federal income tax, **you do not pay any AMT.** If it is larger than your federal income tax, you pay the amount that it exceeds your federal income tax, on top of paying your federal income tax. So, if your calculated AMT is $50k and you paid $35k in federal income tax, you owe the government $15k for the difference between the two amounts.

All in all, unless you buy options netting you a profit exceeding $200k in a given year, you’re unlikely to run into AMT.

**“Should I early exercise my options?”**

The answer to this question depends on your own personal finances. Only early exercise with a sum of money that you are prepared to lose entirely. If you can tolerate a loss of a few tens of thousands of dollars, there are several tax benefits, including not having to worry about AMT.

If you’re concerned about the financial risk of early exercising, you can choose to purchase a subset of your shares. An accountant can help you determine a way to exercise shares over time, while staying well below the threshold that would trigger AMT.

### Wrapping up

All in all, if you are confused about your equity packages, talk to a CPA! Spending a few hundred dollars to avoid an unnecessary tax bill totaling tens of thousands may be worthwhile. In the meantime, I’ll leave you with some additional resources:

* [Calculating AMT in 2018 (and how it is different from 2017)](https://www.fool.com/taxes/2018/02/05/how-the-alternative-minimum-tax-is-changing-in-201.aspx)
* [Long term vs. short term capital gains tax](https://www.investopedia.com/articles/personal-finance/101515/comparing-longterm-vs-shortterm-capital-gain-tax-rates.asp)
* [Stock options and AMT](https://www.nceo.org/articles/stock-options-alternative-minimum-tax-amt)
* [Wealthfront blog post](https://blog.wealthfront.com/improving-tax-results-stock-option-restricted-stock-grant/)
* [Front’s compensation and equity calculator](https://comp.data.frontapp.com/)

