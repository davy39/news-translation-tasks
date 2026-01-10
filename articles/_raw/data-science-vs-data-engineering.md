---
title: The Difference Between Data Science and Data Engineering
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-21T22:54:32.000Z'
originalURL: https://freecodecamp.org/news/data-science-vs-data-engineering
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-markus-spiske-177598--1-.jpg
tags:
- name: data-engineering
  slug: data-engineering
- name: Data Science
  slug: data-science
seo_title: null
seo_desc: "By Edem Gold\nI recently became very interested in Data Science and Data\
  \ Engineering, especially how they compare and complement each other. \nI initially\
  \ assumed Data Engineering was a subset of Data Science. But after extensive research\
  \ I found out j..."
---

By Edem Gold

I recently became very interested in Data Science and Data Engineering, especially how they compare and complement each other. 

I initially assumed Data Engineering was a subset of Data Science. But after extensive research I found out just how much the two fields differ.

In this article, I'll discuss the differences between Data Science and Data Engineering and the main tasks of each field.

> "Data is the new oil. It’s valuable, but if unrefined it cannot really be used." – Clive Humby

## What Do We Mean by Data?

To fully understand the relationship between Data Science and Data Engineering, you have to understand the one thing that links them both: data.

Data is a word that has become commonplace in today's society, with so many reports of [data leaks](https://www.statista.com/statistics/1307426/number-of-data-breaches-worldwide),[the innapropriate collection of data by big tech companies](https://www.security.org/resources/data-tech-companies-have/), and so on.

Data refers to information that is collected and stored in a format that can be processed by a computer. It can be in various forms such as numbers, text, images, and videos, and it can be collected, stored, and analyzed to extract insights and inform decisions.

**Now why do so many companies want data and what's so special about it?**

Data is important to companies because it allows them to make informed decisions about their operations and strategies. By analyzing data, companies can gain insights into the behaviour of their users. Then, they can use the insights they get from their users to make their products way more efficient, desireable, and useful.

Data scientists and engineers are the people responsible for collecting the data, making it useful, analysing it, gaining insights and trends from it. They also pass on the information they've mined to management in order to permit informed decision making. Now let's see how they differ.

## What is Data Science?

Data Science was named the _The Sexiest Job of the 21st Century_ by the [Harvard Business Review](https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century), and its claim to the title is arguably legitimate.

Data Science is the process of using scientific methods, algorithms, and systems to analyse and extract value from data.

In other words, the data scientist is the individual responsible for gaining insights from data and making abstract mathematical models from the data in order to enable prediction.

Now let's look at the data engineer.

## What is Data Engineering?

Data Engineering is the process of designing, constructing, and maintaining the pipelines and infrastructure that collect, store, process and analyze data.

The Data Engineer is the individual who's responsible for ensuring that the data required by Data Scientists is available in the correct and accurate format.

Data is infuriatingly complex and disordered when it is collected. In order for Data Scientists to efficiently gain insights from it, the data needs to be pre-processed. 

Then, once insights have been made, Data Scientists formulate an abstract mathematical model from the data, commonly known as a [Machine Learning Model](https://learn.microsoft.com/en-us/windows/ai/windows-ml/what-is-a-machine-learning-model). This abstraction needs to be post-processed in order to be deployed and integrated into the product. 

All these tasks are performed by data engineers.

## The Relationship Between Data Scientists and the Data Engineers – Explained with an Analogy

Imagine you placed a bet with a friend on the outcome of a football game. But you wanted to cut out the luck factor that is always so present in uninformed guesses. This way you can be extremely sure that your team wins the game and you win the bet.

A data engineer would collect the data on the two teams involved in the bet. They'd consider data points such as _number of games won, possession rate per game, and results of previous clashes between the two teams_. Then they'd create an ETL pipeline where the data would be collected, cleaned, and stored for the data scientist.

The Data Scientist would then perform something called _Predictive Analysis_ using Machine Learning. This means that the data scientist would feed the data prepared by the data engineer into an algorithm that would then generate a mathematical abstraction called a _Machine Learning model_. 

Then the Machine learning model would predict the team expected to win the bet. And just like that your guess becomes less of guess and more of a data-informed decision.

## Summary

As you can hopefully see from this description of Data Scientists and Engineers, a Data Scientist is similar to a star football player and the Data Engineer like the player's very talented coach who keeps them fit and provides them with tactics to win a game.

