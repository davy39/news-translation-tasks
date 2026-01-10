---
title: How to Automate Your Business Strategy with Python and APIs
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2022-12-06T18:11:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-e-commerce-operations-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-1.png
tags:
- name: api
  slug: api
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: null
seo_desc: "When you work in e-commerce operations, you'll have to perform many tasks\
  \ daily to implement your company's business strategies. \nBut these often repetitive\
  \ tasks can be time-consuming and leave room for errors. Some of these errors can\
  \ cost your com..."
---

When you work in e-commerce operations, you'll have to perform many tasks daily to implement your company's business strategies. 

But these often repetitive tasks can be time-consuming and leave room for errors. Some of these errors can cost your company money, reputation, and time. 

Luckily, Python and APIs can help you prevent such mistakes as well as save time and money. Your team can then invest that time and money in other activities like developing new strategies or methods to be more efficient.

## You May Have Heard of APIs Before 

If you work in the tech industry, you've likely heard of APIs at least once in your life. If you have never heard of it, don't worry – I'll give you a brief explanation here.

**"API"** stands for **Application Programming Interface**. They help services or applications communicate with each other. 

Just to give you an example, if you are a frontend developer you'll be asked to call a backend service via its API to retrieve the information you want to print on the screen. This is how the backend and the frontend send and receive data. When you call an API you get a JSON or XML file as a response.

APIs can be also **"RESTful"**, which stands for **Representational State Transfer**. Rest is a set of architectural constraints that help you design efficient and safe APIs. 

If you'd like to know more about REST APIs, I recommend that you [read this article by Ihechikara](https://www.freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners/) here on freeCodeCamp's publication.

## How Can APIs Help You Get Work Done?

As I said, APIs are about exchanging information. Even if you're not developing a frontend application, you can retrieve the data you need and manipulate or handle them to get the information you need. Then you can ask another service to perform the action you want it to perform.

I'll give you an everyday-life example to show you how you can use APIs to automate tasks to help implement your business strategy.

### API Use Case Example

Let's say our company sells umbrellas and we want to update our price list according to the weather of the city where our store is located. When it rains, we want the umbrellas' price to be raised, while we want it to decrease when the weather is good. In any other case, we want to leave the price as it is.

Of course, this is an over-simplified scenario, but I think it is a good fit to show how powerful APIs can be to help you automate your business strategies online.

Without any automation, you would have to check the weather forecasts every day and manually update the item's price. As I said at the beginning of this article, this type of manual process can be time-consuming and leave room for errors. Also, don't forget you would need somebody to perform these tasks 365 days a year.

Thankfully, we can automate this process. This is what we need:

* Python (3.10 and above)
* A CMS/e-commerce exposing APIs (I'm using Woocommerce for this tutorial)
* Weather forecast APIs

### How to Use Python and APIs to Automate Updates

We'll implement a batch written in Python – that executes every 24 hours – to update the price of the umbrellas according to the response of a weather forecast API we call.

Let's dive into the script and analyze it step by step. 

First of all, I declare environment variables. This is the list:

```python
API_BASEURL #The baseurl of the weather forecast service I'm calling

API_CITY #The city I want to get weather information about

API_COUNTRY #The country where API_CITY is located 

API_KEY # The secret Key I must pass to retrieve the weather information

CONSUMER_KEY #The key I need to work with Woocommerce APIs 

CONSUMER_SECRET #The secret I need to work with Woocommerce APIs

DOMAIN #The domain of my ecommerce
```

Then, I start importing the libraries I need:

```python
import os
from dotenv import load_dotenv
```

I import **os** and I also import **load_dotenv** to work with environment variables.

Then I import requests and JSON to handle the API's response.

```python
import requests
import json
```

Then I import the API module from Woocommerce Python library. You can find more information in its rich [documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/?python#libraries-and-tools).

```python
from woocommerce import API
```

Once I imported all the libraries and modules I need, I'll instantiate the variables I'll use on my script:

```python
load_dotenv()
product_to_sell_id = "1736" #The Id related to umbrellas in my e-commerce
raised_price = "12" #The price I want to set when it rains
lowered_price = "8" #The price I want to set when weather is good
regular_price = "10" #The regular price of the item 
```

Then I declare the **changePrice** function:

```python
def changePrice(price, idProduct):

    wcapi = API(
        url= os.getenv('DOMAIN'), 
        consumer_key= os.getenv('CONSUMER_KEY'), 
        consumer_secret= os.getenv('CONSUMER_SECRET'), 
        wp_api=True, 
        version="wc/v3" 
    )

    data = {
        "regular_price": price
    }

    wcapi.put("products/" + idProduct, data).json()
    
    print("New price set to " + data["regular_price"])
```

The function has two arguments: the price I want to set (price) and the id of the product I want to update (idProduct).

Inside the function I store in the **wcapi** variable the API method with the information I need to reach my e-commerce (baseurl, consumer key, and secret).

I store in the **data** variable the payload I want to pass: I want to update the value of the key "regular_price" with the value of the argument "price".

After that, I update the e-commerce database with the PUT method by passing the path of the product I want to update (it's a concatenation of the string "products/" and the value of the argument "idProduct") and the data variable value.

In the end, I print a success message.

Once the **changePrice** function is ready, I need to define a new one to make the script work. But before we go ahead, we need to see the data we get from our API call.

The JSON file we get back as a response returns a lot of information. But, as I said at the beginning, we just want to know what the weather is like. 

We get this data with the "code" key. Every weather status is associated with a number. In our case, we focus on these two codes: 

```python
502 #rainy
800 #sunny
```

Now that we have what we need, we define the **getWeather** function:

```python
def getWeather():

    url = os.getenv('API_BASEURL')

    headers = {
    "Accept": "application/json"
    }
    
    payload = {
    "key": os.getenv('API_KEY'),
    "city": os.getenv('API_CITY'),
    "country": os.getenv('API_COUNTRY')
    }
    

    response = requests.request(
    "GET",
    url,
    params=payload,
    headers=headers  
    )

    data = response.text

    parse_json = json.loads(data)

    get_parse_result = parse_json["data"][0]["weather"]["code"]
    
    match get_parse_result:
        case 502:
            changePrice(raised_price, product_to_sell_id)

        case 800:
            changePrice(lowered_price, product_to_sell_id)

        case _:
            changePrice(regular_price, product_to_sell_id)
```

In the **url** variable we define the base URL of the API we're calling. In the payload variable I pass our secret key, the city, and the country I want to get the weather about.

I perform my GET request by passing the URL, payload, and headers. Once I get the response, I parse it, and implement a switch statement with 3 cases:

* **get_parse_result** equals 502: we call the changePrice function passing as first argument the raised_price variable to increase the product price
* **get_parse_result** equals 800: we call the changePrice function passing as first argument the lowered_price variable to decrease the product price
* **get_parse_result** has a different value: we call the changePrice function passing as first argument the regular_price variable to keep the product price as it is

A the end of the script, I call the getWeather function:

```python
getWeather()

```

And there you go – the prices will be automatically updated thanks to a little code.

## Wrapping Up

So, this is just a quick example of how you can use APIs to automate your business strategies, save time, and avoid mistakes that can cost your company money. 

It's a pretty basic example but I think it shows the potential of APIs and their benefits. Here you can find my [repo](https://github.com/mventuri/automate-ecom-prices) with the full script.

