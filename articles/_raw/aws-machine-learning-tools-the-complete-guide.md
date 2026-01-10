---
title: 'AWS Machine Learning Tools: The Complete Guide'
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-10-06T12:10:00.000Z'
originalURL: https://freecodecamp.org/news/aws-machine-learning-tools-the-complete-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/wall-7.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: framework
  slug: framework
- name: Machine Learning
  slug: machine-learning
- name: tools
  slug: tools
seo_title: null
seo_desc: 'In this article, we will take a look the machine learning tools offered
  by AWS. We''ll also understand the type of problems they try to solve for their
  customers.

  AWS Machine Learning comprises a rich set of tools that Amazon offers to help developers...'
---

In this article, we will take a look the machine learning tools offered by AWS. We'll also understand the type of problems they try to solve for their customers.

[AWS Machine Learning](https://aws.amazon.com/machine-learning/) comprises a rich set of tools that Amazon offers to help developers integrate machine learning models into their applications. 

AWS also offers pre-trained models for use cases including computer vision, recommendation engines, and language translation.

Amazon currently offers 15 machine learning services on its platform. In this article, we will take a look at each one of them so we can understand the type of problem they are trying to solve for their customers.

## SageMaker

[Amazon SageMaker](https://aws.amazon.com/sagemaker/) helps you to take your machine learning models from concept to production in a fraction of time compared to traditional code-based approaches. 

Sagemaker is a managed service and has the complete suite of tools you need to build, train, and deploy your machine learning models. They help you label your data, optimize your algorithms, and more. It's a complete solution for creating and deploying machine learning models.

SageMaker also has an autopilot option that will automatically process the data and run it through multiple algorithms. This helps developers find the best algorithm for their model without manually training and testing those models. 

Sagemaker also comes with an integrated IDE and a sharable Jupyter notebook that you can use to collaborate with your team.

## CodeGuru

[Amazon CodeGuru](https://aws.amazon.com/codeguru/) lets you automate your code reviews and performance optimizations for your application. 

It can find issues like [race conditions](https://searchstorage.techtarget.com/definition/race-condition), resource leaks, and wasted CPU cycles. This helps you produce higher quality code by providing specific recommendations based on code context.

Codeguru’s algorithms are trained with codebases from Amazon’s projects. Right now, CodeGuru supports only Java applications, but you can expect the functionality to extend to other languages in the near future.

## Comprehend

[Amazon Comprehend](https://aws.amazon.com/comprehend/) is a Natural Language Processing service from Amazon that uses machine learning to find valuable insights from textual data. 

Comprehend can work with unstructured data like product reviews, customer emails, twitter tweets, and so on to help you draw conclusions (like overall audience sentiment).

It's also a fully managed service, meaning you can use pre-trained models to work with your data. Comprehend also has an additional service called Amazon Comprehend Medical that lets you work with medical documents to analyze medical conditions and dosages.

## Forecast

[Amazon Forecast](https://aws.amazon.com/forecast/) is used to build time-series prediction models using your existing datasets. 

Forecast works great for use cases like predicting future business expenses, stock price prediction, and resource planning for organizations based on customer demand.

This service is also customizable and lets you build custom models on top of Amazon’s existing deep learning models. Like most machine learning tools in AWS, Forecast is also fully managed and can scale according to your business needs.

## Fraud Detector

[Amazon Fraud Detector](https://aws.amazon.com/fraud-detector/) is another fully managed service that helps you detect fake registrations and fraudulent transactions. 

Fraud detector can identify potentially fraudulent accounts and then helps you set up additional verification for those flagged accounts.

A fraud detector needs an existing dataset of labeled fraudulent transactions in order to train and understand the pattern of your customer behavior. It then uses this data to prevent further fraudulent transactions. 

You can also configure custom authentication rules for guest logins and product trials.

## Kendra

[Amazon Kendra](https://aws.amazon.com/kendra/) is an AI-powered enterprise search engine that will help you deliver highly accurate search results based on customer queries. 

You can use. Kendra to power search engines in your products that help your users find exactly what they're looking for.

Kendra can also be used to help customers find answers to specific problems while using your product without the need for additional customer support. 

Kendra also supports natural language questions, delivering an even smoother experience for your customers.

## Lex

[Amazon Lex](https://aws.amazon.com/lex/) lets you build conversational interfaces into your products. Lex offers [Natural Language Understanding (NLU)](https://en.wikipedia.org/wiki/Natural-language_understanding) models that can understand conversational input from users and perform the right actions.

Lex can be used as a replacement for manual customer support to help filter common queries, and it can answer them automatically. It is also a fully managed service that scales automatically and uses a pay-as-you-use model.

## Personalize

[Amazon Personalize](https://aws.amazon.com/personalize/) lets you create custom recommendations for your customers based on their usage patterns. 

While traditional recommendation engines can be used only to recommend products, Personalize lets you literally personalize every step of your customer’s user experience.

Personalize is a great tool to build product recommendations, custom search results based on queries and employ targeted marketing promotions.

## Polly

[Amazon Polly](https://aws.amazon.com/polly/) helps you build speech-enabled products for your customers. Polly provides lifelike voice outputs across a variety of languages including Chinese, Korean and Japanese.

Polly is powered by deep learning algorithms that mimic a conversational style interface that can be used in narrations, telephony applications, and other applications.

## Rekognition

[Amazon Rekognition](https://aws.amazon.com/rekognition/) is a computer vision solution from AWS that helps developers build applications that can recognize objects from images and videos. 

In addition to automatic object recognition, you can customize Rekognition to pick out specific objects and scenes based on your own requirements.

Rekognition can be used in use cases like identifying manufacturing defects in products, spotting unauthorized personnel in an organization, scanning for inappropriate content in movies, and so on. It can also be used to analyze player movements in games for post-game analysis.

## Textract

[Amazon Textract](https://aws.amazon.com/textract/) enables you to read data from scanned documents. The usual approach to digitizing paper documents is using manual data entry or [OCRs](https://en.wikipedia.org/wiki/Optical_character_recognition) with custom configurations. 

Textract makes it easier by automatically applying rules to documents and extracting valuable data along with components like forms and images within the document.

Textract is useful for processing loan applications, medical claims, and more. In addition to extracting data, these can be optimized for search using Textract. Documents that usually take months to process using manual methods can be processed in hours using AWS Textract.

## Transcribe

[Amazon Transcribe](https://aws.amazon.com/transcribe/) lets you build speech to text services in your application. Transcribe is useful in building medical transcription services, streaming audio, generating subtitles for video recordings, and more.

Transcribe can also be used to convert customer calls into text and analyze them for improved customer service. Cataloging audio archives is another use case for AWS transcribe.

## Translate

[Amazon Translate](https://aws.amazon.com/translate/) is a machine learning service similar to Google Translate. Translate can work with a variety of languages with high accuracy, which lets businesses customize their languages based on the the demographics of their audiences.

Translate is also designed to be more natural-sounding to customers since the context of the sentence is also taken into account. 

Translate is also highly customizable so it can help improve the accuracy of translation when working with your brand names and unique words related to your business.

## DeepLens

[Amazon DeepLens](https://aws.amazon.com/deeplens/) is a video camera with in-built deep learning capabilities that helps you build and test computer vision models in real-time. 

DeepLens is fully programmable and can be used to test models like live object recognition, classifying birds/ animals, face detection, and so on.

The product is designed for developers getting started in machine learning. It helps them get a grasp of how their models will work in the real world. 

DeepLens is also integrated with the AWS ecosystem and can be used with other AWS services like Lambda and Rekognition to extend its capabilities.

## DeepRacer

If you are a fan of self-driving cars, [AWS DeepRacer](https://aws.amazon.com/deepracer/) is a small autonomous race car designed by AWS that runs using machine learning. DeepRacer helps you test your reinforcement learning models using a physical track.

You can build reinforcement learning models using AWS SageMaker and test them instantly using DeepRacer. Amazon also gives you the opportunity to connect and compete with fellow racing enthusiasts by building virtual private race tracks.

## Summary

With a solution to almost every machine learning problem, Amazon Machine Learning offers a rich set of tools for machine learning engineers to work with. 

Amazon also adds new services every few months based on new use cases, making it one of the most dependable platforms where engineers can build AI solutions for their customers.

_Loved this article?_ [**_Join my Newsletter_**](http://tinyletter.com/manishmshiva) _and get a summary of my articles and videos every Monday._

