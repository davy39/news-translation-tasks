---
title: How  to rock your next time series forecasting project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-29T15:43:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-rock-your-next-time-series-forecasting-project-3930d589f704
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UAOHYeh9LCDFdNvAUSHDDg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Productivity
  slug: productivity
- name: project management
  slug: project-management
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kirill Dubovikov

  Time series forecasting is a task of great importance. It has a wide variety of
  applications ranging from sales forecasting to anomaly detection in complex manufacturing
  processes.

  Yet, it is quite different from traditional machi...'
---

By Kirill Dubovikov

Time series forecasting is a task of great importance. It has a wide variety of applications ranging from sales forecasting to anomaly detection in complex manufacturing processes.

Yet, it is quite different from traditional machine learning methods.

Forecasting projects have many caveats you should be aware of to succeed in the task at hand. In this article we will explore key points that will help you to finish the task successfully. Read on to find out the ones you miss out.

### Research your methods

![Image](https://cdn-media-1.freecodecamp.org/images/bAd0qz2jSIO2atDsxIZnx2-8ABNd0QBnMhRy)

It is crucial to study your problem in detail and plan before committing actions that will affect the success of your project.

#### 1. Study your theory

Before taking on a modeling project, make sure that you understand the theory if you haven’t already. [Forecasting: Principles and Practice](https://otexts.org/fpp2/) is a very solid resource that can outline the basics in a practical and concise way.

#### 2. Study the domain

Before discussing any project details, make sure that you understand the basics. Learn as much as you can about the business domain in which you will operate. Google can help you get started. Understand key definitions and common business models. Without this step, you may end up doing months worth of work for nothing. You do not want to fail because you solved a problem that does not make business sense.

#### 3. Study the problem

The first thing you should do in any data science project is to study the problem. And I do not mean talking with your client for 15 minutes and writing out an initial understanding. You should question everything and be skeptical (in a good sense).

Remember, that data science is a relatively new field in the world of practical applications. This means that **your client’s vision may be incomplete**. To help them you should understand their business and their problem as deep as you can.

Work with requirements, digest them word-by-word and feel the problem at hand. Then try to understand the business behind the problem.

Is it sound from the economy standpoint? What is the end goal of your client? It may not be direct profits, but there must be a goal. Does solving the problem your client asks for really helps to achieve this goal?

If not, try to figure out what can be changed together with your customer. Do not fear to ask questions — project success depends on them.

### Finding the right data

![Image](https://cdn-media-1.freecodecamp.org/images/xdrYcaR9HaaKK5l1eVc2Lb1b1W1fvSg2N2fP)
_Photo by Franki Chamaki on Unsplash_

At this point we should have a good understanding of our problem and domain. Next, we will look into the importance of researching and questioning the data.

#### 4. Think about metrics and evaluation

Next, you should think about evaluation. And I am not talking about model validation, but an evaluation that makes sense to the client. Often, they won’t come up with ready to use business metric, that’s your responsibility to work with them on it. In the end, you should have a solid mathematical definition of how your forecasts affect the end goal of the project.

And please do not try to use conventional data science validation metrics such as MAPE, MAE, RMSE as the main project metric. They are fine metrics for validation purposes, though they still can fail you pretty bad in a business context.

For example, take that we have some sales data for different items. The client asked us to estimate future sales over the two-month horizon. In addition, she gave us historical data on current sales forecasting strategy (e.g. done by analysts by hand).

For example, your new fancy deep learning model destroys existing strategy by 30% difference in MAPE. You may deploy it to production and fail miserably for the following reasons:

* Your model **undersells** frequently compared to the current strategy. The error can be small and do not affect MAPE by much, but business-wise 4% undersells compared to their current approach can be a disaster
* Your model cuts possible oversales by a large margin. In many cases, this would not impress the client. In the end, they even can ask you to use the upper confidence interval to cut the risks of underselling
* MAPE (chosen metric) does not make sense to the client and is hard to understand by people that will read the report

Always make sure that you have a sound model evaluation strategy. It is your safety belt, and it is better to have one rather than not, isn’t it?

#### 5. Look at your data

Do your Exploratory Data Analysis (EDA) homework. It may be very seductive to skip this part. “We’ll do this later, for sure! I’ll just look at how some models perform”. That’s what you may think. [Eat your frogs first](https://www.fastcompany.com/1592454/work-smart-do-your-worst-task-first-or-eat-live-frog-every-morning). Draw plots, seek outliers, check for strange patterns. If you have many time series, look at their sums if it makes sense to do so.

Communicate all findings to the client. If anything in the data is not understandable and clear then that should be figured out as soon as possible.

You may have bugs in the code, or your framework may have bugs too, or perhaps the client’s data exporting pipeline may also be buggy. Double check the date parsing. Always deliberately state date format for your framework. For example, Python’s pandas library can silently fail you when parsing dates in different locales.

Even if you won’t find any bugs, your client may be surprised by your findings. Unusual seasonal patterns and anomaly findings can provide tremendous value too. Your customer may not be aware of these because they did not look at the data the way you do.

#### 6. Look at your data AGAIN

Do more EDA. I can’t emphasize how important this is.

#### 7. Write tests for data loading and preprocessing

Write automated tests for your data pipeline. Tests will pay you off and save you time later.

#### 8. Ponder on business metrics

Are your business metrics defined? Your customer has agreed on them and every piece is crystal clear to them? Do you have functions to calculate them implemented and properly tested? If not, then it is time to stop and do this part.

If you will continue hoping that MAPE or RMSE will make it up for a business metric you may end up in trouble. It will make your reports hard to understand and increase your chances of solving the wrong task.

### Simplicity is the key

![Image](https://cdn-media-1.freecodecamp.org/images/N9U43H8K8z0a0ULimWe9r9xD2duqeNcpT4BZ)

At last, let us not forget about simplicity. The last five points explore the value behind simple things: simple models, double checks and communication.

#### 9. Start with the mean

Before going full-machine learning, check how simple models work, like predicting the mean average. No, really.

Some examples:

* Predicting running mean for the last N weeks
* Predicting running quantiles
* Predicting Exponentially Weighted Average
* Using heuristic rules for holidays and regular events. A mean with a multiplier can work wonders on the New Year

This will give you a solid baseline. It may be hard to believe, but in some cases, you may even find that is is the best possible solution. For this exact reason, we have created an entire module devoted to heuristic rules and simple statistical models in our forecasting framework.

#### 10. Choose the right model

Finally, the fun part. Try out as many models as you can afford. Do an initial test on a wide range of models, filter them and tune the best one or two.

Be wary of non-functional requirements. Always measure the time required for fitting the model. Your task may have limitations that will affect your choice:

* Running time, especially if you have tens of thousands of time series to make forecasts for
* Available computational resources

#### 11. Measure performance

Calculate your business and technical metrics using time series cross-validation. Use as many folds as you can to get accurate estimates. Research your findings if you see anything unusual. Extremely good performance? Extremely bad performance? Those are often the signs of caution.

#### 12. Check everything again

Check yourself. Check your client. Write some tests if possible.

#### 13. Prepare reports and communicate clearly

Now is the time to communicate and present your findings and results. Research consumers of your results. Do they know about machine learning or time series forecasting? Are they proficient in computer science? If they are, this part may be easy.

If not, try to use fancy statistics and machine learning thesaurus as little as you can. Prepare clear definitions if you can’t go without complex terms. Use plots with titles, legends and axis names. The end goal is to communicate your results as clear as it is possible. No one will be able to use your results if they won’t understand them. And no one will be able to spot a mistake if you will hide behind complex descriptions and cryptic formulas.

### General guidance for the course of the entire project

* Communicate more. I can’t emphasize this more. In the end, communication is likely to be more important than your entire 100-model ensemble powerhouse
* Get rid of complex thesaurus
* Dive into the business

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/3LazLBqqRo0kgvWhmL6YbUn7N4ohhQiyrbry)

We have explored some key points that will help to to succeed in a time series forecasting project. Some of them may seem intuitive and you may think that you’ll never make these mistakes, but be sure to check yourself. Often, the easiest thing to fail in is the most obvious one.

Please, s[hare the article](https://ctt.ac/79dT2) if it helped you. Also, consider giving it it some claps ? .

Follow me on ? T[witter](https://twitter.com/kdubovikov) ,?Me[dium a](https://medium.com/@dubovikov.kirill)nd ??‍?Linke[dIn.](https://www.linkedin.com/in/kirill-dubovikov-2a20b154/)

