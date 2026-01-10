---
title: Public APIs Developers Can Use in Their Projects
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2023-03-02T00:28:23.000Z'
originalURL: https://freecodecamp.org/news/public-apis-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/api-cover.jpg
tags:
- name: api
  slug: api
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "A public API, also known as an external API, is a type of application programming\
  \ interface that allows developers to access specific features and data of a software\
  \ application or service. \nIt is \"public\" in the sense that it is made available\
  \ to th..."
---

A public API, also known as an external API, is a type of application programming interface that allows developers to access specific features and data of a software application or service. 

It is "public" in the sense that it is made available to third-party developers and is not limited to internal use by the organization that created the API. 

Public APIs are made available to anyone who wants to use them and typically do not need any special permission or authentication to access them. Developers can use public APIs to build new applications, enhance existing ones, or integrate different software systems.

In this article, we will be discussing the types of public APIs, their benefit to developers, and public APIs that you can use in your projects.

## Types of Public APIs

There are different types of APIs that developers can use to access data and features provided by online services. It's like borrowing someone's tool to help you do your job more easily.

Here are the main types:

### Representational State Transfer (REST) APIs

These are very popular and easy-to-use APIs which use _HTTP_ requests to get or change data. An example is the Twitter API and some of the ones mentioned in this article.

### Simple Object Access Protocol (SOAP) APIs

These APIs are more complex but have superpowers for security and advanced features. These web-based APIs use the XML data format to exchange data between applications. A popular example is Amazon Web Services (AWS) API.

### GraphQL

This API can be more efficient and save you time by giving you only the data you need. You can use the GraphQL API to request only the names and descriptions of a user's repositories, rather than getting all of the repository data at once. 

This makes it easier to work with large amounts of data and can help improve the performance of the application. An example is GitHub's GraphQL API.

### Webhooks

These are like a hotline that lets you know when important things happen. An example would be real-time notifications about social media updates. You can also use webhooks to notify an application when a user makes a purchase.

### Websockets

This API allows two-way communication between a client and a server in real time. They are commonly used for applications that need real-time updates. A common example would be chat applications or online games.

## Benefits of Public APIs for Developers

I've already alluded to some of the benefits of working with Public APIs. But now let me spell out why they're so useful in a bit more detail.

### Access to existing functionality

Public APIs provide developers with access to existing functionality and data that they can use to create new applications. This can save developers time and resources – they do not need to build everything from scratch.

### Improved integration and user experience

Public APIs speed up the development process of web applications and also enable integration between different systems.

You can use public APIs to create integrations between different applications and services. This can improve the user experience by making it easier to use different products together seamlessly.

### Improved efficiency

Public APIs can help developers create applications more efficiently by allowing them to focus on the specific functionality they want to build, rather than having to worry about the underlying technology.

### Increased functionality

By using public APIs, developers can add new functionality to their applications without having to build it themselves. This can enable them to create more complex and innovative applications.

## Challenges with Using Public APIs

As helpful as public APIs are, there are some challenges that go along with using them. Here's a few things to keep in mind:

1. **Data privacy and security concerns:** Public APIs may expose sensitive data and require authentication measures to ensure that data is not accessed by unauthorized parties.
2. **Documentation:** Some public APIs may have incomplete or poorly written documentation, which can make it difficult for developers to understand how to use the API.
3. **Compatibility:** Some public APIs may not be compatible with the programming language or framework that a developer is using, which can make it difficult to integrate the API with their application.
4. **Rate Limits**: Many public APIs have rate limits, which restrict the number of requests a developer can make in a given period. If the rate limit is exceeded, the API may return errors or stop working altogether.

## How to Choose a Public API for Your Project

When you're ready to choose a public API to work with, there are some things to keep in mind. These tips will help you choose one that's right for your needs, and help you avoid some of the challenges we just discussed.

### Availability and Reliability

To make sure you pick the best API for your project, make sure you verify its availability and reliability. 

Seek out APIs that provide assurances of high uptime and have a proven record of reliable availability. Also take into account whether the API has usage restrictions or if there are any costs associated with it.

### Documentation and Support

Choose APIs that have proper documentation and support. This will help you understand how to use them and resolve any technical problems. Look out for clear, detailed documentation that can promptly address your concerns or inquiries.

### Security and Privacy

Consider the security and privacy of your project and data, which could be crucial. Search for APIs with strong security measures, like encryption and authentication, and that have transparent privacy policies that ensure the protection of user data. Choose APIs based on the sensitivity of your project and data.

### Project Requirements

When selecting an API, think about what you want to achieve with your project and what features you require from the API. For instance, if you intend to integrate social media, use a social media API like Twitter or Facebook.

### Reviews and Feedback

Check out feedback and reviews from other developers who have used the API you are considering. Reviews can provide insight into the strengths and limitations of the API, as well as any potential problems that other developers have faced.

## Common Public APIs Used by Developers

If you want some ideas of helpful public APIs you can use, you're in luck. I've compiled a list here to get you started, containing some of the most popular public APIs out there that can add a lot to your projects.

### [JSONPlaceholder](https://jsonplaceholder.typicode.com/) API

This is a website that helps developers test their programs before using a real one. It lets you create, change, and delete fake data using HTTP requests. 

This fake data can be adjusted to fit your needs and comes in different forms like JSON, CSV, and YAML. This site helps you make sure your code works correctly and create demos for others to see.

### Weather APIs

Weather APIs, such as [**OpenWeatherMap**](https://openweathermap.org/) and [**Weather Underground**](https://www.wunderground.com/), let you incorporate real-time, historical, and forecast weather data into your applications. 

These APIs offer a comprehensive array of weather information, including current temperature, wind speed, direction, humidity, atmospheric pressure, and precipitation. 

The only obstacle is that users must obtain a key. But they provide free or affordable access to their data for non-commercial use and small-scale projects.

### News APIs

News APIs like the [**New York Times API**](https://developer.nytimes.com/apis) provides access to news articles and media content for developers. You can use them to retrieve articles, images, videos, and other media types and are commonly used to build news aggregators and search engines. 

The New York Times API is frequently used to create personalized news feeds and applications that analyze news content for trends.

### Book APIs

These provide access to data and information about books such as their titles, authors, genres, ISBNs, publication dates, cover images, and descriptions. Examples are the [**Google Books API**](https://developers.google.com/books) and [**Open Library API**](https://openlibrary.org/developers/api)**.**

### Movie APIs

A movie API provides access to a database of movie information, including details on movie titles, release dates, genres, ratings, cast members, and more. It also supports the search and filtering of movies based on various criteria. 

Examples are [**The Movie Database (TMDb) API**](https://developers.themoviedb.org/3/getting-started/introduction)**,** [**IMDb API**](https://developer.imdb.com/)**,** and [**Rotten Tomatoes API**](https://rapidapi.com/collection/rotten-tomatoes-api)**.**

### Meals and Drink APIs

This API provides access to information about food and beverages. [**TheMealDB API**](https://www.themealdb.com/api.php) and [**Spoonacular API**](https://spoonacular.com/food-api) are examples of APIs that offer access to food and beverage-related data, including details on their names, ingredients, nutritional information, recipes, and images. The [**Cocktail DB API**](https://www.thecocktaildb.com/api.php) is an API that specializes in drinks and cocktails.

### YouTube API

This API helps developers do many things, like finding videos, getting information about them, handling user accounts, adding or changing videos, getting comments and analytics, and more. 

This API is usually used in apps that show videos or work with YouTube. An example of a YouTube API is the [**YouTube Data API**](https://developers.google.com/youtube/v3).

### Google Search API

The Google Search API is a tool that allows you to access and integrate Google's search engine results into your applications. It provides a range of functionalities such as searching for web pages, images, videos, news articles, and more. 

With this API, you can create customized search experiences for your users, as well as extract and analyze search data. But it's important to note that as of September 2021, Google has deprecated the Google Search API and replaced it with the [**Custom Search JSON API.**](https://developers.google.com/custom-search/v1/introduction)

### eCommerce API

These APIs help developers integrate eCommerce platforms into their applications. They allow you to manage product catalogs, process orders, and payments, and create online stores and shopping apps. 

Popular examples of eCommerce APIs include [**Shopify API**](https://shopify.dev/docs/api), [**WooCommerce API**](https://woocommerce.com/document/woocommerce-rest-api/), and [**Magento API**](https://www.cloudways.com/blog/magento-2-rest-api/#:~:text=The%20Magento%20API%20allows%20the,responses%20for%20creating%20the%20integration.).

### Dog APIs

This API is for dog lovers and provides your with access to a database of information and media related to dogs. 

It includes functionalities such as retrieving dog breed information, images, random dog images, and more. 

You can use this API to create various dog-related applications such as dog breed identification, dog image galleries, and dog training apps. An example includes [**Dog API**](https://thedogapi.com/) and [**Dog CEO API**](https://dog.ceo/dog-api/).

### [The Cat API](https://thecatapi.com/)

This is a web-based API that provides developers with access to a large collection of cat images and information, including breed, temperament, and more. 

The API is free to use for non-commercial purposes, with some limitations on the number of requests that can be made per day. 

### Dictionary API 

This API allows you to access dictionary data and integrate it into your applications. It provides functionalities such as word definitions, synonyms, antonyms, translations, and more. 

With this API, you can create language-related applications such as word games, language-learning apps, and translation tools. 

Examples of dictionary APIs include [**Merriam-Webster Dictionary API**](https://dictionaryapi.com/) and [**Oxford Dictionary API**](https://developer.oxforddictionaries.com/). These APIs provide developers with a vast collection of word-related data that you can use to create various language-related applications.

### Sports APIs

Sports APIs give you access to lots of information about sports like player and team stats, schedules, and game results. 

With these APIs, you can make apps that show users live updates about games, scores, and other sports news. Some examples of sports APIs are [**Sportradar API,**](https://developer.sportradar.com/docs/read/Home) [**Api-Sport**](https://api-sports.io/)**s,** and the [**NFL API**](https://developer.nfl.com/get-started/overview).

### Quotes API

Quote APIs give you access to a collection of famous quotes, sayings, and phrases from various authors, celebrities, and historical figures. 

These APIs allow your to retrieve quotes and display them in your applications or websites, and they often include features for searching and filtering quotes based on different criteria, such as author, category, or keyword. Examples of quotes APIs include the [**Quotes Free API**](https://zenquotes.io/)**.**

### Joke API

This is a type of public API that provides you with access to various types of jokes, including puns, one-liners, and more. 

These APIs are often used to build applications that can generate random jokes or display jokes based on specific categories or themes. They can also be used to add humor to existing applications or to create standalone joke-related apps. Examples of joke APIs include the [**JokeAPI**](https://sv443.net/jokeapi/v2/) and [**DadJokes**](https://dadjokes.io/).

### [National Park Service (NPS) API](https://www.nps.gov/subjects/developer/api-documentation.htm)

This is a free public API that lets developers get lots of information about the national parks in the United States. This includes details about where the parks are, what's in them, and events happening there. The API also has data on animals, plants, and other natural things found in the parks. 

Anyone can use the API if they sign up for a free key, and it doesn't cost any money. But there are limits on how much data you can request each day to make sure it works well for everyone.

### [Giphy SDK API](https://developers.giphy.com/docs/sdk)

The Giphy SDK (software development kit ) API provides access to a vast library of GIFs and stickers, as well as tools for searching, filtering, and organizing content. It allows you to add animated GIFs and other types of short-form content to your apps, websites, and other digital products.

### [Rest Countries API](https://restcountries.com/)

This API provides information about countries and territories around the world, including their names, capital cities, currencies, languages, and more.

### Gallery API

This API gives you access to and displays collections of images or other media. Here are a few examples: [**Unsplash API**](https://unsplash.com/developers)**,** [**Flickr API**](https://www.flickr.com/services/api/)**,** [**Getty Images API**](https://developers.gettyimages.com/)**,** and [**Pexels API**](https://www.pexels.com/api/)**.**

### [Health API ( specifically Covid-19 API)](https://covid19api.com/)

This is a free API for developers, and you can use it to build COVID-19-related applications, services, and visualizations. 

Developers can use these APIs to get the latest data on COVID-19 cases, deaths, and recoveries, and use this data to inform their applications and services.

## Conclusion

Public APIs provide developers with access to pre-built functionality, data, and services, allowing them to integrate these capabilities into their applications without having to build them from scratch. 

This can save you time and resources, enabling you to focus on building unique features and functionality that set your applications apart.

In this article, we covered some public APIs, but there are many more available, covering a wide range of functionality and data types. You should carefully consider your project requirements and choose the APIs that best meet your needs.

**You can read about more public APIs in this guide to** [**35+ Free Public APIs to Improve Productivity**](https://blog.idrisolubisi.com/35-free-public-apis-to-improve-productivity).

If you enjoyed this article, consider sharing it to help other developers.

You could also visit [**my blog**](https://ijaycent.hashnode.dev/) to read more articles from me, and you can connect with me on [**Twitter**](https://twitter.com/ijaydimples) and [**LinkedIn**](https://www.linkedin.com/in/ijeoma-igboagu/).

Thanks for reading💖

