---
title: How I analyzed DVD rental data with SQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-20T21:53:13.000Z'
originalURL: https://freecodecamp.org/news/project-1-analyzing-dvd-rentals-with-sql-fd12dd674a64
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zGw3_fh6s09rpS3ZCxDYDQ.jpeg
tags:
- name: analytics
  slug: analytics
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Okoh Anita

  Introduction

  I recently completed some training in Data Foundation facilitated by Bertelsmann’s
  School of Data Science (in partnership with Udacity). For a personal project, I
  decided to analyze the database for a DVD rental company we ...'
---

By Okoh Anita

#### Introduction

I recently completed some training in Data Foundation facilitated by Bertelsmann’s School of Data Science (in partnership with Udacity). For a personal project, I decided to analyze the database for a DVD rental company we will call **Rent A Film**. Let’s take a look at a case study detailing my process and output.

#### Data-set

I began by taking a look at the database. The database **DvdRental** has 15 tables. Below are the different tables and a brief description of them.

* actor — contains actors data including first name and last name.
* film — contains films data such as title, release year, length, rating, etc.
* film_actor — contains the relationships between films and actors.
* category — contains film’s categories data.
* film_category — containing the relationships between films and categories.
* store — contains the store data including manager staff and address.
* inventory — stores inventory data.
* rental — stores rental data.
* payment — stores customer’s payments.
* staff — stores staff data.
* customer — stores customer’s data.
* address — stores address data for staff and customers
* city — stores the city names.
* country — stores the country names.

_Note: I analyzed this database using PostgreSQL. You can get details to install PostgreSQL [here](http://www.postgresqltutorial.com/install-postgresql/) and download the DVD rental database [here](http://www.postgresqltutorial.com/postgresql-sample-database/)._

#### Objective & Goals

In this project, I’ll aim to answer the following questions:

1. What are the top and least rented (in-demand) genres and what are their total sales?
2. Can we know how many distinct users have rented each genre?
3. What is the average rental rate for each genre? (from the highest to the lowest)
4. How many rented films were returned late, early, and on time?
5. In which countries does **Rent A Film** have a presence and what is the customer base in each country? What are the total sales in each country? (from most to least)
6. Who are the top 5 customers per total sales and can we get their details just in case **Rent A Film** wants to reward them?

Before getting started with analyses, I first tried understanding the ERM (Entity Relationship Model) of this database also known as Schema. Here is the Schema below:

![Image](https://cdn-media-1.freecodecamp.org/images/Re5gkP7yWnJhl7p84eVLeVRxixkh9Po284s0)
_[DVD RENTAL SCHEMA](http://www.postgresqltutorial.com/postgresql-sample-database/" rel="noopener" target="_blank" title=")_

You can view my code on my GitHub profile [here](https://github.com/anitaokoh/DVD-RENTAL).

#### Analysis

To answer the first question **_“_What are the top and least rented (in-demand) genres and what are what are their total sales?”**, I first identified with tables I would need to Join, which are:

> **Category >film_Category >film>inventory>rental >cu**stomer >payment

Below is the query I used to extract to answer the question:

![Image](https://cdn-media-1.freecodecamp.org/images/7-yaKfFB753y7H0NeIdgYtR6c-WMlrjSJJ9d)

![Image](https://cdn-media-1.freecodecamp.org/images/ooD0kn6JsTwZ9XfabDd8nIfsaYHY0eiOAjGz)

**Insights**

From the above table, we can draw 3 major insights:

* **Rent A Film** has 16 available genres
* The sports category seems to be the most rented genre in terms of the number of times being rented, and it also has the highest total sales in terms of money.
* The music category is the least rented genre in terms of the number of times being rented and has the lowest total sales in terms of money

**Question 2: Can we know how many distinct users have rented each genre? In short, yes we can.**

The tables to join are as follows:

> **Category > film_Category > film > inventory > renta**l > customer

Below is my query for this question:

![Image](https://cdn-media-1.freecodecamp.org/images/8MxaJS0364pwezbp8P-RXTjQ6nLBnqjgiq9v)

![Image](https://cdn-media-1.freecodecamp.org/images/TK2anW8Y-xEhWWToXXcEVVvraLIL5vkiElfp)

**Insights**

I wanted to know how many distinct customers rented each of the genres. One fascinating thing from the query is that although the music genre has the least total rented record, it does not have the least number of distinct customers who rented the genre. The travel genre holds that record.

By taking a step back and connecting the insights derived from question 1 and 2, we can say that the travel genre was re-rented more times than the music genre.

And of course, the sports genre has the highest number of distinct customers who rented the genre.

**Question 3: What is the Average rental rate for each genre?** (from the highest to the lowest)

The tables to join are as follows:

> **Category > film_Category >**; film

Below is my query for this question:

![Image](https://cdn-media-1.freecodecamp.org/images/wqh-5F-ZpUE1sd3FMMouuxnqpR683paYZtyv)

![Image](https://cdn-media-1.freecodecamp.org/images/jUeVY4Iomda2s1OfWaFqGqhmVPM8LTShibZf)

**Insights**

I went ahead to see if the number of times a category has been rented has anything to do the average rental rate of each genre. From the above table, we can easily conclude that average rental rate may not be a factor.

Although the game genre has the lowest average rental rate, it is one of the top five most rented genre. Surprisingly, the Music genre is not the most expensive — Action is, even though the action genre is one of the most rented genres.

We can safely say that most of the customers are lovers of sport-related movies and are least interested in musical movies.

**Question 4: How many rented films were returned late, early and on time?**

The tables to join are as follows:

> **film > inventory >** rental

![Image](https://cdn-media-1.freecodecamp.org/images/Wk0iyxP6WpwbQLGhZNpz09J38baFiMYMvWDz)

![Image](https://cdn-media-1.freecodecamp.org/images/xe6Cg0xlQER5aZZRc0dAyp-B76gf73MHQZew)

**Insights**

The return status of movies is arguably is one the most important aspects to monitor in a DVD rental business. From the above query, 48% of the movies are returned earlier than the due date while 41% of the movies are returned late and 11% arrive on time.

There could be a number of factors for why this could be happening, like the shipping distance of these movies from stores which could be totally out of the control of the customers and so on. _We would need to dive deeper into the data to get the gist of the issue._

However, it is wise to note that a significant percentage of movies are returned late. Introducing a penalty fee for late arrival could be an extra source of income and in turn, discourage late returns.

But such a decision can only make sense if we know why the issue is occurring.

**Question 5: In which countries do Rent A Film have a presence in and what is the customer base in each country? What are the total sales in each country?** (From most to least)

The tables to join are as follows:

> **Country > City > Address > customer** > payment

See query below:

![Image](https://cdn-media-1.freecodecamp.org/images/oZfnuGxi1ZsB-TJqS0kTx41mVm1CfOKtvaQD)

![Image](https://cdn-media-1.freecodecamp.org/images/OzlVEmkcz3STrKZ30ZCsPr4gqExcRwjK8DpR)

![Image](https://cdn-media-1.freecodecamp.org/images/G0YGu2nLvUDUe1c-79i5od9yK10gBAH77O6m)

![Image](https://cdn-media-1.freecodecamp.org/images/PhqJRtlIpMfwnnq-qDgd5bX9tohNREX0cNDw)

![Image](https://cdn-media-1.freecodecamp.org/images/ZspQd77D0ahbHZzApXfj-OfsDecw4YJWsUxd)

![Image](https://cdn-media-1.freecodecamp.org/images/bumlck68X66y7788-8f-oIqbGkAQzbxIpIqI)

![Image](https://cdn-media-1.freecodecamp.org/images/GdsPzZEkcaRbpLW7E5rDwL5u5bNLv09fNsep)

![Image](https://cdn-media-1.freecodecamp.org/images/bHNQ8hWQvkNTeTJ0Oza9K1MWzaNBkO7495a-)

**Insights**

**Rent A Film** has a presence in 108 countries with India having the highest customer base of 60 customers and the largest total sales in terms of money. Afghanistan has the smallest total sales in terms of money, even though it is not the only country with the smallest customer base of 1 customer

**Question 6: Who are the top 5 customers per total sales and can we get their detail just in case Rent A Film wants to reward them?**

The tables to join are as follows:

> **Country > City > Address > customer** > payment

See query below:

![Image](https://cdn-media-1.freecodecamp.org/images/h6oSZOmqcmAkrA9WS0hu0DLdo6Oo9UdZUWbc)

![Image](https://cdn-media-1.freecodecamp.org/images/ivEIz9TpgeeJF5Yc0Cd6gbRZTA5KyN-tYh3S)

**Insights**

Assuming we wish to reward or send physical gifts to the top customers, the above table shows their full names, addresses, email etc.

This information can be sent to the marketing team of the company in order to use their domain knowledge to decide how to reward them.

### Conclusion

In this project, we analyzed data from a DVD rental company we decided to call **‘Rent A Film’** to find insights about the customers and their preference. We got 3 major conclusions:

1. The company has sport-loving customers and they would be advisable to stock more sport-related films to increase total sales compared to music-related movies. It would be a good idea to increase the average rental rate of sport genre films since it is not a major factor in renting for the customers. This, in turn, increases total revenue. However further analysis needs to be done to conclude on this.
2. There is potential to have an extra source of revenue through a fee on late film returns.
3. **Rent A Film** has a presence in 108 countries with India been the largest market in people and revenue. Additionally, 20% of the countries they have presence in contribute to 80% of the total customer base.

_P.S Like me, anyone can learn to be a data analyst and if you want to be notified on my next project or updates on my learning, feel free to sign up to my [newsletter](https://goo.gl/forms/aEbTwhSXRDAUa5tr1)_

