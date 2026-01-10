---
title: What is Sentiment Analysis? A Complete Guide for Beginners
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-09-30T13:39:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-sentiment-analysis-a-complete-guide-to-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall-5.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Sentiment analysis
  slug: sentiment-analysis
seo_title: null
seo_desc: 'Sentiment analysis lets you analyze the sentiment behind a given piece
  of text. In this article, we will look at how it works along with a few practical
  applications.

  What is Sentiment Analysis?

  Sentiment analysis is a technique through which you can...'
---

Sentiment analysis lets you analyze the sentiment behind a given piece of text. In this article, we will look at how it works along with a few practical applications.

# What is Sentiment Analysis?

Sentiment analysis is a technique through which you can analyze a piece of text to determine the sentiment behind it. It combines machine learning and natural language processing (NLP) to achieve this. 

Using basic Sentiment analysis, a program can understand whether the sentiment behind a piece of text is positive, negative, or neutral.

It is a powerful technique in Artificial intelligence that has important business applications. 

For example, you can use sentiment analysis to analyze customer feedback. After collecting that feedback through various mediums like Twitter and Facebook, you can run sentiment analysis algorithms on those text snippets to understand your customers' attitude towards your product.

# How Sentiment Analysis Works

The simplest implementation of sentiment analysis is using a scored word list. 

For example, [AFINN](https://gist.githubusercontent.com/damianesteban/06e8be3225f641100126/raw/a51c27d4e9cc242f829d895e23b4435021ab55e5/afinn-111.txt) is a list of words scored with numbers between minus five and plus five. You can split a piece of text into individual words and compare them with the word list to come up with the final sentiment score.

Let's say we had the phrase, "I love cats, but I am **allergic** to them".

In the AFINN word list, you can find two words, “love” and “allergic” with their respective scores of +3 and -2. You can ignore the rest of the words (again, this is very basic sentiment analysis). 

By combining these two, you get a total score of +1. So you can classify this sentence as mildly positive.

There are complex implementations of sentiment analysis used in the industry today. Those algorithms can provide you with accurate scores for long pieces of text. Besides that, we have reinforcement learning models that keep getting better over time.

For complex models, you can use a combination of NLP and machine learning algorithms. There are three major types of algorithms used in sentiment analysis. Let's take a look at them.

## Automated Systems

Automatic approaches to sentiment analysis rely on machine learning models like clustering. 

Long pieces of text are fed into the classifier, and it returns the results as negative, neutral, or positive. Automatic systems are composed of two basic processes, which we'll look at now.

## Rule-based Systems

Unlike automated models, rule-based approaches are dependent on custom rules to classify data. Popular techniques include tokenization, parsing, stemming, and a few others. You can consider the example we looked at earlier to be a rule-based approach.

A good thing about rule-based systems is the ability to customize them. These algorithms can be tailor-made based on context by developing smarter rules.

Just keep in mind that you will have to regularly maintain these types of rule-based models to ensure consistent and improved results.

## Hybrid Systems

Hybrid techniques are the most modern, efficient, and widely-used approach for sentiment analysis. Well-designed hybrid systems can provide the benefits of both automatic and rule-based systems.

Hybrid models enjoy the power of machine learning along with the flexibility of customization. An example of a hybrid model would be a self-updating wordlist based on [Word2Vec](http://jalammar.github.io/illustrated-word2vec/). You can track these wordlists and update them based on your business needs.

# Use Cases for Sentiment Analysis

### Analyzing Customer Feedback

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-6.jpeg)

Customer feedback analysis is the most widespread application of sentiment analysis. Direct customer feedback is gold for businesses, especially startups. Accurate audience targeting is essential for the success of any type of business.

Well-made sentiment analysis algorithms can capture the core market sentiment towards a product. 

You can also extend this use case for smaller sub-sections, like analyzing product reviews on your Amazon store. The more customer-driven a company is, the better sentiment analysis can be of service.

### Campaign Monitoring

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-5.jpeg)

Manipulating voter emotions is a reality now, thanks to the [Cambridge Analytica Scandal](https://en.wikipedia.org/wiki/Facebook%E2%80%93Cambridge_Analytica_data_scandal).

Another use-case of sentiment analysis is a measure of influence. Taking the 2016 US Elections as an example, many polls concluded that Donald Trump was going to lose.

But experts had noted that people were generally disappointed with the current system. They backed their claims with strong evidence through sentiment analysis. 

I worked on a tool called Sentiments (Duh!) that monitored the US elections during my time as a Software Engineer at my former company. We noticed trends that pointed out that Mr. Trump was gaining strong traction with voters.

This should be evidence that the right data combined with AI can produce accurate results, even when it goes against popular opinion.

### Brand Monitoring

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-4.jpeg)

Brand monitoring is another great use-case for sentiment analysis. Companies can use sentiment analysis to check the social media sentiments around their brand from their audience.

KFC is a perfect example of a business that uses sentiment analysis to track, build, and enhance its brand. KFC’s social media campaigns are a great contributing factor to its success. They tailor their marketing campaigns to appeal to the young crowd and to be “present” in social media.

Tools like [Brandwatch](https://www.brandwatch.com/) can tell you if something negative about your brand is going viral. Other brands that use social media to promote a positive brand sentiment include Amazon, Netflix, and Dominoes.

### Stock Market Analysis

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-2.jpeg)

If you are a trader or an investor, you understand the impact news can have on the stock market. Whenever a major story breaks, it is bound to have a strong positive or negative impact on the stock market.

Sentiment analysis is a powerful tool for traders. You can analyze the market sentiment towards a stock in real-time, usually in a matter of minutes. This can help you plan your long or short positions for a particular stock.

Recently, Moderna announced the completion of phase I of its COVID-19 vaccine clinical trials. This news resulted in a strong rise in the stock price of Moderna. 

But today, Moderna’s stock stumbled after losing a patent. Using sentiment analysis, you can analyze these types of news in realtime and use them to influence your trading decisions.

### Compliance Monitoring

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-1.jpeg)

Regulatory and legal compliance can make or break large organizations. Often, these compliance documents are stashed into large websites like [Financial Conduct Authority](https://www.fca.org.uk/).

Large organizations spend a good chunk of their budgets on regulatory compliance. In these cases, traditional data analytics cannot offer a complete solution. 

Tools like [ScrapingHub](https://www.scrapinghub.com/) can help fetch documents from these websites. But companies need intelligent classification to find the right content among millions of web pages.

Sentiment analysis can make compliance monitoring easier and more cost-efficient. It can help build tagging engines, analyze changes over time, and provide a 24/7 watchdog for your organization.

# Conclusion

Sentiment analysis is a powerful tool that you can use to solve problems from brand influence to market monitoring. New tools are built around sentiment analysis to help businesses become more efficient.

And by the way, if you love Grammarly, you can go ahead and thank sentiment analysis.

_Loved this article?_ [**_Join my Newsletter_**](http://tinyletter.com/manishmshiva) _and get a summary of my articles and videos every Monday._


