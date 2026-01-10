---
title: How to Get Location Information of an IP Address Using Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-03-03T17:55:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-location-information-of-ip-address-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/location-ip.png
tags:
- name: api
  slug: api
- name: Python
  slug: python
seo_title: null
seo_desc: 'Sometimes you''ll need to know the location of an IP address, whether it''s
  your own or that of a site you''re using.

  One use-case for this is when you want to send login information to users for your
  website.

  In this article, we''re going to see how you...'
---

Sometimes you'll need to know the location of an IP address, whether it's your own or that of a site you're using.

One use-case for this is when you want to send login information to users for your website.

In this article, we're going to see how you can find the location of an IP address using Python.

# **Get your tools ready**

To accomplish this goal, we'll be using two APIs mentioned below:

1. [**ipify**](https://www.ipify.org/): This API will help us know the IP address from where the request is coming.
    
2. [**ipapi**](https://ipapi.co/): This API will help us fetch location information for a particular IP address.
    

To interact with these APIs, we'll be using the `**requests**` library in Python. If you're new to APIs, make sure you check out [this tutorial](https://ireadblog.com/posts/77/python-api-tutorial-how-to-interact-with-web-services) to learn about them.

You can install this library using the `pip` command like this:

```bash
$ pip install requests
```

Once the library is installed, we're good to go!

# **Get Location Information**

As we discussed, we'll first fetch our IP address from the first API. Then we'll make use of this IP address to fetch location information for this particular IP address. So, we'll have two functions:

```py
import requests


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


print(get_location())
```

In the above code, we have two functions – `**get_ip()**` and `**get_location()**`. Let's discuss each of them separately.

### `get_ip()` function

As per the [API documentation](https://www.ipify.org/) of ipify, we need to make a **GET** request on [`https://api.ipify.org?format=json`](https://api.ipify.org/?format=json) to get a JSON response that looks like this:

```json
{
  "ip": "117.214.109.137"
}
```

We store this response in a `response` variable which is nothing but a sort of [Python dictionary](https://ireadblog.com/posts/84/everything-you-need-to-know-about-python-dictionaries) with one key-value pair. So we returned the value of the key `**ip**` as `**response["ip"]**`.

### `get_location()` function

As per the [API documentation](https://ipapi.co/api/#introduction) of ipapi, we need to make a **GET** request on [`https://ipapi.co/{ip}/{format}/`](https://ipapi.co/%7Bip%7D/%7Bformat%7D/) to get location information for a particular IP address. `{ip}` is replaced by the IP address and `{format}` can be replaced with any of these – `json`, `jsonp`, `xml`, `csv`, `yaml`.

This function internally calls the `**get_ip()**` function to get the IP address and then makes a **GET** request on the URL with the IP address. This API returns a JSON response that looks like this:

```json
{
    "ip": "117.214.109.137",
    "version": "IPv4",
    "city": "Gaya",
    "region": "Bihar",
    "region_code": "BR",
    "country": "IN",
    "country_name": "India",
    "country_code": "IN",
    "country_code_iso3": "IND",
    "country_capital": "New Delhi",
    "country_tld": ".in",
    "continent_code": "AS",
    "in_eu": false,
    "postal": "823002",
    "latitude": 24.7935,
    "longitude": 85.012,
    "timezone": "Asia/Kolkata",
    "utc_offset": "+0530",
    "country_calling_code": "+91",
    "currency": "INR",
    "currency_name": "Rupee",
    "languages": "en-IN,hi,bn,te,mr,ta,ur,gu,kn,ml,or,pa,as,bh,sat,ks,ne,sd,kok,doi,mni,sit,sa,fr,lus,inc",
    "country_area": 3287590,
    "country_population": 1352617328,
    "asn": "AS9829",
    "org": "National Internet Backbone"
}
```

We get a whole lot of data in the response. You can use whatever works for you. For this tutorial, we'll just be using `**city**`, `**region**` and `country`. That's why we created a dictionary called `location_data` and stored all the data inside it and returned the same.

At last, we call the `**get_location()**` function and print the output. Our output will look like this:

```json
{
  "ip": "117.214.109.137", 
  "city": "Gaya", 
  "region": "Bihar", 
  "country": "India"
}
```

# **Conclusion**

In this article, we learned how we can interact with web services to get location information for a particular IP address.

Thanks for reading! For more such articles, checkout my blog, [iRead](https://ireadblog.com).
