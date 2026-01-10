---
title: Sentiment Analysis Using Laravel and the Google Natural Language API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T11:02:55.000Z'
originalURL: https://freecodecamp.org/news/sentiment-analysis-using-laravel-and-the-google-natural-language-api-acb70871698a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TdiVdPnYkvgl3qWnLGgOcg.jpeg
tags:
- name: Laravel
  slug: laravel
- name: nlp
  slug: nlp
- name: PHP
  slug: php
- name: Sentiment analysis
  slug: sentiment-analysis
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Darren Chowles

  Write your own sentiment checker in 5 minutes.


  Sentiment Analysis is the process of determining whether a piece of text is positive,
  negative, or neutral.

  Real world applications for Sentiment Analysis

  The goal of this article is t...'
---

By Darren Chowles

#### Write your own sentiment checker in 5 minutes.

![Image](https://cdn-media-1.freecodecamp.org/images/W-RZSezYMfrCrFNASW1qeHGAc8tHm8epzb9F)

Sentiment Analysis is the process of determining whether a piece of text is positive, negative, or neutral.

### Real world applications for Sentiment Analysis

The goal of this article is to get you up and running using the Google Natural Language API with Laravel. You’ll be using this API to perform sentiment analysis on text.

Using these techniques, you can build some great functionality into existing applications. Some ideas include:

* detecting sentiment in comments or reviews
* forecasting market movements based on social media activity
* ascertaining the effectiveness of a marketing campaign by observing sentiment before and after

### Interpreting Sentiment Analysis values

The Google API takes the provided text, analyzes it, and determines the prevailing emotional opinion. It determines whether the writing is positive, negative, or neutral.

The sentiment is represented by numerical **score** and **magnitude** values.

* The **score** ranges between -1.0 (negative) and 1.0 (positive).
* The **magnitude** indicates the strength of emotion (both positive and negative). The range spans from 0.0 to infinity. The **magnitude** is not normalized, so longer passages of text will always have a larger **magnitude**.

![Image](https://cdn-media-1.freecodecamp.org/images/okN8PYIoQbHRpiBvsV2A1QCDW3rlkUJMyk6H)
_The values above are guides only, and you’ll need to adjust according to your specific environment._

### Google Cloud Platform setup

The first step involves creating a new project in the Google Cloud Platform console.

Head over to the dashboard and [create a new project](https://console.cloud.google.com/projectcreate).

![Image](https://cdn-media-1.freecodecamp.org/images/z6371dAtV-MSOkaUJgZaEJvCvlB5pykD3OUq)

Once your project is created, keep the **Project ID** handy.

![Image](https://cdn-media-1.freecodecamp.org/images/ssGnt0a3bKIaNyCRIwJcbaSD7iaAuKrMUSGP)

* Once you have your project, go to the [Create service account key](https://console.cloud.google.com/apis/credentials/serviceaccountkey) page.
* Ensure your Sample project is selected at the top.
* Under **Service account**, select **New service account**.
* Enter a name in the **Service account name** field.
* Under **Role**, select **Project** &g**t; Ow**ner.
* Finally, click **Create** to have the JSON credentials file downloaded automatically.

![Image](https://cdn-media-1.freecodecamp.org/images/IbX4pzWkQIl9XCtFFizscV2S4zRXvQCohCRP)

You may also need to enable the Cloud Natural Language API via the [API Library](https://console.developers.google.com/apis/library/language.googleapis.com) section.

![Image](https://cdn-media-1.freecodecamp.org/images/ZSc4dpY-9xCA4MM7q7WrYcQV-mFqndbkFEiA)

### Laravel project setup

The next step involves setting up a new Laravel project. If you already have an existing Laravel project, you can skip this step.

I’m using Laravel 5.5 LTS for this article. In the command line, run the following Composer command to create a new project (you can also use the [Laravel installer](https://laravel.com/docs/5.5#installing-laravel)):

```
composer create-project --prefer-dist laravel/laravel sample "5.5.*"
```

If you used Composer, rename the **.env.example** file to **.env** and run the following command afterwards to set the application key:

```
php artisan key:generate
```

### Add the Google “cloud-language” package

Run the following command to add the Google Cloud Natural Language package to your project:

```
composer require google/cloud-language
```

You may go ahead and place the downloaded JSON credentials file in your application root (NOT in your public directory). Feel free to rename it. Never commit this file to your code repo — the same goes for any sensitive settings. One option is to add it to the server manually after initial deployment.

### The main event: adding the actual code to your project

I’ll be adding the following route to my **routes/web.php** file:

```
<?php 
```

```
Route::get('/', 'SampleController@sentiment');
```

I’ve created a simple controller to house the code. I’ll be adding all the code within the controller. In a production application, I strongly suggest using separate service classes for any business logic. This way controllers are lean and stick to their original intention: controlling the input/output.

We’ll start with a simple controller, adding a `use` statement to include the Google Cloud `ServiceBuilder` class:

```
<?php
```

```
namespace App\Http\Controllers;
```

```
use Google\Cloud\Core\ServiceBuilder;
```

```
class SampleController extends Controller{    public function sentiment()    {        // Code will be added here    }}
```

The first thing we’ll do is create an instance of the `ServiceBuilder` class so we can specify our Project ID and JSON credentials.

```
$cloud = new ServiceBuilder([    'keyFilePath' => base_path('gc.json'),    'projectId' => 'sample-207012']);
```

You specify the location of the JSON file using the `keyFilePath` option. I’ve used the Laravel [base_path()](https://laravel.com/docs/5.5/helpers#method-base-path) helper to refer to the fully qualified app root path.

The next option is the `projectId`. This is the value you grabbed when you created the project in the GCP console.

Next, we’ll create an instance of the `LanguageClient` class. The `ServiceBuilder` class makes it easy by exposing various factory methods which grant access to services in the API.

```
$language = $cloud->language();
```

Now that we have an instance of the class, we can start making use of the Natural Language API. We’ll declare a variable with some text, analyze the sentiment, and output the results:

```
// The text to analyse$text = 'I hate this - why did they not make provisions?';
```

```
// Detect the sentiment of the text$annotation = $language->analyzeSentiment($text);$sentiment = $annotation->sentiment();
```

```
echo 'Sentiment Score: ' . $sentiment['score'] . ', Magnitude: ' . $sentiment['magnitude'];
```

And that’s all there is to it!

![Image](https://cdn-media-1.freecodecamp.org/images/savaV9K6VqBmJIvC8kMz97tdvMFa4NpX7jRs)
_Output for the code above._

Here is the final controller class code:

```
<?php
```

```
namespace App\Http\Controllers;
```

```
use Google\Cloud\Core\ServiceBuilder;
```

```
class SampleController extends Controller{    public function sentiment()    {        $cloud = new ServiceBuilder([            'keyFilePath' => base_path('gc.json'),            'projectId' => 'sample-207012'        ]);
```

```
        $language = $cloud->language();
```

```
        // The text to analyse        $text = 'I hate this - why did they not make provisions?';
```

```
        // Detect the sentiment of the text        $annotation = $language->analyzeSentiment($text);        $sentiment = $annotation->sentiment();
```

```
        echo 'Sentiment Score: ' . $sentiment['score'] . ', Magnitude: ' . $sentiment['magnitude'];    }}
```

### Conclusion

We’ve only scratched the surface of what the Google Natural Language API has to offer. Once you’ve come to grips with this, I suggest checking out the following additional services available in this API:

* **Entity Analysis**: analyze entities like landmarks and public figures.
* **Content Classification**: analyze text and return a list of categories that apply to the content.

If you have any questions — please feel free to make contact!

_Originally published at [www.chowles.com](https://www.chowles.com/sentiment-analysis-using-laravel-and-google-natural-language-api/) on June 13, 2018._

