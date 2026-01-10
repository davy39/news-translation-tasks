---
title: How to Predict Rent and Optimize Your Lease Duration So You Can Save Money
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-11T01:45:26.000Z'
originalURL: https://freecodecamp.org/news/https-medium-freecodecamp-org-how-to-predict-rent-and-select-the-best-lease-duration-to-save-money-5cf35145d398
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XkBmEX4MUwXSb8eo98TsXg.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Real Estate
  slug: real-estate
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Zhen Liu

  In my last post, we talked about how to pick the best month to sign the lease based
  on seasonality. Now, how long should you sign the lease for when facing different
  options like 12-month, 15-month, 18-month or longer? Is there any strate...'
---

By Zhen Liu

In my [last post](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a), we talked about how to pick the best month to sign the lease based on seasonality. Now, how long should you sign the lease for when facing different options like 12-month, 15-month, 18-month or longer? Is there any strategy in selecting the best option to save money?

To analyze this, I modelled 353 cities’ rent data from [Zillow](https://www.zillow.com/research/data/#other-metrics) (one-bedroom, city-level data). In this article, I will show you how to make time series predictions, and which cities are predicted to increase the most in rent!

#### First, how does lease duration help you save money?

As shown below, you can save money by signing a longer lease if you predict the rent will increase in your city. If the monthly rent increases $100 in the next year, you’ll save $1,200 by signing a 2-year lease, then renew it year-by-year.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7bY_4ic8FMaImPsaRZz8Sg.png)

#### How do you predict if rent will increase?

We observed that rent is an additive time series with a combination of seasonality, trend and some random noise.

Additive model: Y(t) =Seasonality(t) + Trend(t) + Randomness(t)

We can decompose a time series into the right hand side of the equation above by applying R’s `stl()` function (stl stands for "seasonal and trend decomposition using locally weighted scatterplot smoothing”).

```
# Decompose the additive time seriesdecomposed_rent <- stl(rent.series, s.window="periodic") #periodic means the seasonality factor is same for every year
```

```
# Extract the components from time seriesseasonal   <- decomposed_rent$time.series[,1]trend	   <- decomposed_rent$time.series[,2]random     <- decomposed_rent$time.series[,3]
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*pOSifCkvyN2LLvesF_A8sg.png)
_The plot of the decomposed time series of rent verified that the components are additive, where rent = Seasonality + Trend + Randomness_

You can simply apply the `st()` function in R on the time series format of rent data to predict rent in the next 2 years.

```
# Forecast rent for the next 24 months with 95% Confidence Intervalfore_rent<-stlf(rent.series, s.window="period",h=24, level = 95) 
```

#### Which cities have the predicted increase of rent?

_*How to read the plots: The **light green** **band** area after 2018 is the 95% Confidence Interval of the rent prediction. The **text in purple** tells you how much you can save if you sign a 2-year rent vs 1-year rent, according to the purple rectangular area outlined. I used_ `ggplot2` _for all the plots._

### 1. Bay Area

![Image](https://cdn-media-1.freecodecamp.org/images/1*xx2OynsXjT9euYGLOzCNRQ.png)

Sunnyvale’s predicted monthly rent increase is the greatest among all 246 cities I analyzed, which is $165 (comparing 2018–01’s rent to the predicted rent in 2019–01). So signing a 2-year lease in 2018 Jan can save you 165*12= **$ 1980** on the second year; signing a 18-month lease can save 165*6 = **$990**. Given the seasonality effect in Sunnyvale, you should also try to avoid renewing the lease around July.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ks6lXmPRK_jsaQk00T7DJg.png)

### 2.Denver

![Image](https://cdn-media-1.freecodecamp.org/images/1*gLXQKu8gp8aOfSApU5_mwA.png)

### 3.Southern California

![Image](https://cdn-media-1.freecodecamp.org/images/1*T7QFELfN2wQSe_ghzijkYg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*m0gtYNI_qtSWXpZshROYJA.png)

### 4. Seattle Area

![Image](https://cdn-media-1.freecodecamp.org/images/1*pL4yYcZbfdXY3PiyrKdhdQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2CgkcLhr-MrvsitBFP3DiQ.png)

### 5. Florida

![Image](https://cdn-media-1.freecodecamp.org/images/1*wsEj6o6zivPOBleX_rbD4w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZxAlZ9_lZQfQ88_Vma1qLw.png)

### 6. Texas

![Image](https://cdn-media-1.freecodecamp.org/images/1*kzDwYdn4AjTvjFAd66USoQ.png)

For the 11 cities above, if a 2-year lease isn’t an option, 18-months can still save a lot compared to an yearly updated increasing rent.

Which other cities show a huge leap in rent? I plotted the 20 cities total (including the cities mentioned above) to show you a comparison of rent as well as the increase of rent among more cities.

The **_length of line segment_** of each city is the increase of the rent where the red dot is the rent in 2018–01 and the green is the predicted rent in 2019 -01.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZfRNJEjyDvOiPfxWatzEsw.png)

From the plot above, Lakewood (Denver Metro in CO) and El Cajon (San Diego Metro in CA)’s rents are not that high among the 20 cities, but the “step” of increase is bigger compared to other cities with similar range of rent.

The cities with rent >$2000 and significant predicted increase are all in CA (Top 4 of the plot). The rent there is already expensive, and they are getting more expensive, faster.

Among the top 20, there are 8 in CA, 6 in FL, 2 in WA, 2 in TX, 1 in NY and 1 in CO.

#### Are there any cities that don’t show much trend in rent?

![Image](https://cdn-media-1.freecodecamp.org/images/1*HPApNP5vlsnuecn8ldeukQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*mcw3q3DVsto1ZhDBLbW4tQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*v1rbNlgNjuLOPv1uJ6I6Bg.png)

For the cities above, there’s no predicted increase. So for cities with very significant seasonality effect like Boston and Wilmington, it doesn’t really matter **_how long_** you sign the lease; but **_which month_** you sign.

The month with the highest rent in Boston is November, while it’s April in Wilmington.

If you are curious about what are other cities like this, read more about cities with seasonality in my [_last post_](https://medium.freecodecamp.org/how-to-analyze-seasonality-and-trends-to-save-money-on-your-apartment-lease-714d1d82771a)_!_

_Find the R code for time series models and visualization with ggplot2 [here](https://github.com/zhendata/Medium_Posts/blob/master/Rent%20Prediction_zhendata.R)._

Give me a few claps and follow me here if you find it helpful!

