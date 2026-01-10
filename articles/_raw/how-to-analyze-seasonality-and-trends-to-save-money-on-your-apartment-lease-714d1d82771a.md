---
title: How to Analyze Rental Seasonality and Trend to Save Money on Your Lease
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T10:04:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ltPh1YrsG8dK9VnnM9-rzg.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Real Estate
  slug: real-estate
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Zhen Liu

  When I was looking for a new apartment to rent, I started to wonder: is there any
  seasonality impact? Is there a month when the rent is lowest so I can save money
  when I start my lease?

  To tackle this question, I used Zillow’s public data...'
---

By Zhen Liu

When I was looking for a new apartment to rent, I started to wonder: is there any seasonality impact? Is there a month when the rent is lowest so I can save money when I start my lease?

To tackle this question, I used Zillow’s public data [here](https://www.zillow.com/research/data/#other-metrics). I analyzed their one-bedroom rental data from January, 2011 to September, 2017 for the top 100 US cities ranked by size.

**The short answer is YES**. You can save from **$1000 to $2000** if you pick the right month to start renting in certain cities. By simply fitting a linear regression model using time and month to estimate rent, I found some interesting seasonality patterns for a few cities.

**Methodology:**

On the high level, **rent = trend + seasonality**. I fit a linear regression model for each city to breakdown trend and seasonality (using a cycle of 12 months).

Model: estimated rent(for a specific month)=t+t²+m1+m2+m3+…+m12

Variables: **t** and **t²** are continuous variables to estimate trend; t is the count of months from the beginning month in a city. I added t² to adjust for quadratic trend, and you’ll see some clear curves in the plot of Philadelphia below.

**m1**, **m2**, … , **m12** are binary variables (0 or 1) that indicate to which month one data point (rent) belongs. Each rent data point can only be assigned one of the monthly variable (as 1). The rest will be 0.

After fitting the model above for all cities, I counted how many months’ coefficients were statistically significantly higher than the month estimated to have the lowest rent. I considered cities with a count ≥3 to have a potentially large seasonality effect.

Then I examined the the overall model fitting to filter out cities with a lot of noise, and came up with a final list of the six most representative cities.

Now I’m going to show you these cities so you can see the sweetest month for you to start renting. I plotted the simulated rent against the actual rent below. You can see the pure seasonal difference (adjusted by each city’s trend) for each month on the lower right corner. Here’s how to read the plots:

**Black line**: actual rent data

**Green line**: simulated rent by regression model given month and year

**Green bar plot on the right corner**: pure seasonal effect estimated by model

**Grey line**: estimated trend by regression model

**Seasonal gap**: highest rent minus lowest rent (the difference estimated between the highest and lowest point from the regression model without trend effect)

**Numerical labels**: represent the months estimated to have highest (red) and lowest (blue) rent

#### Six Cities with Significant Seasonality Effect

You’ll definitely save money if you start renting on a “low” month in these cities.

1. **Boston**

If you start renting in June, you’ll save about **$2484** a year (207*12) compared to starting a lease in November. The grey line shows a slight trend in Boston, but it’s not very significant compared to the strong seasonal factor.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O7j2jme7i-NfCwiCaqclOw.png)

2. **Minneapolis**

There is a slight upward trend, but the seasonality effect is more significant than the trend. Your yearly savings, if renting from December, can be as high as **$1896** (158*12). In reality, this number is likely to be slightly lower, because the upward trend tends to shrink the difference a bit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g-LTRX9KAENiS9i1VdJong.png)

**3. Philadelphia**

After the regression model’s adjustment for the curve-shaped trend, the estimated yearly saving on rent is **$1404** (117*12). This number is greater during the period with a downward trend: you can see that the distance between January and May’s rent is stretched further prior to 2014. The estimated savings are smaller when the overall rent increased during recent years.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nFFdZPnBAU-WfZBgX8zBCg.png)

**4. Chicago**

The overall trend in Chicago is actually the opposite of Philadelphia’s — it went up and then down. But the seasonality effect is still significant after adjusting for trend. The estimated yearly saving is **$1248** (104*12). If the downward trend continues, the saving will be greater — the rent distance between November and April is stretched further as plotted in recent years.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ODN13xjLVsENCt9WM0EJdQ.png)

**5. Columbus**

There is a noticeable upward trend in Columbus’s rent, but the seasonality effect is also quite significant. The estimated yearly savings are smaller after adjusting the pure seasonal gap ($89) by the upward trend, so you’d save around **$720** (60*12). But you should still consider starting your lease in November and avoiding August.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uJ7DZrhZbn5PgxIoU-LDVA.png)

**6. Woodbridge**

If you start renting in December, you’ll save about **$948** (79*12) a year compared to renting from July. The trend isn’t very significant here, so it’s still seasonality that drives the rent price in Woodbridge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R08gdHIMwHRp8-AeYTZsrg.png)

**What about Seattle, the city where I live?**

The seasonality effect also exists in Seattle, and it shows significance in the regression model. However, the trend is so big that the seasonality almost doesn’t matter.

Even so, understanding the seasonality for cities like Seattle can be helpful. While you might not able to negotiate the rent down that much in a less busy season, you could ask that the application fee be waived or something like that.

My current apartment waived mine when I started my lease in January — December has the lowest rent, followed by January. But they might not offer this perk in the busiest months with higher rents, like May and June.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g-Odn1rQgGeAIrfq8bgbIw.png)

Another city where the trend outweighs the seasonality is Omaha.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5SWacHouHqUv5kro3ONA_A.png)

Knowing your city’s seasonality in rent can help you save thousands if you know the pattern. I did my analysis and plots using R, but you can simply plot your city’s data in Excel if you just want to see if there are any noticeable trend and seasonality. Using open source data to hack your life decisions and save money is actually pretty simple.

#### Now, how long should you sign your lease?

Say you are offered a few different options for the length of your lease. Usually it’s nine months to 18 months. Do you know what’s the best length to choose when you sign your lease? There is actually another trick to save money when you pick the duration, and I’ll show you the trick and the math behind it in my next post.

Give me a few claps and share this with friends who might find it useful!

**_You can find my code [here](https://github.com/zhendata/Rent_Seasonality/blob/master/rent_seasonality_zhendata.R)_**.

