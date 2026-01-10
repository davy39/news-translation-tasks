---
title: Python Requests – How to Interact with Web Services using Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2021-12-13T23:03:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-interact-with-web-services-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Black-Moon-Blog-Banner--2-.png
tags:
- name: api
  slug: api
- name: http
  slug: http
- name: Python
  slug: python
- name: REST API
  slug: rest-api
seo_title: null
seo_desc: An API, or Application Programming Interface, facilitates communication
  between two pieces of software. It lets you retrieve and send data using code. We
  mostly commonly use APIs to retrieve data, and that will be the focus of this beginner-friendly
  ...
---

An API, or **Application Programming Interface**, facilitates communication between two pieces of software. It lets you retrieve and send data using code. We mostly commonly use APIs to retrieve data, and that will be the focus of this beginner-friendly tutorial.

When we want to receive data from an API, we need to make a **request**. Requests are used all over the web. For instance, when you visited this blog post, your web browser made a request to the freeCodeCamp web server, which responded with the content of this web page.

![Image](https://res.cloudinary.com/dlomjljb6/image/upload/v1/media/blog/uploads/2021/06/04/api-request_rlwgao)

API requests work in exactly the same way – you make a request to an API server for data, and it responds to your request.

## Different HTTP Methods and Status Codes

There are various HTTP methods for [REST APIs](https://www.ibm.com/cloud/learn/rest-apis). These methods tell the API what operations need to be performed on the data. While there are many HTTP methods, the five methods listed below are the most commonly used with REST APIs:

<table class="table table-hover" style="box-sizing: border-box; border-collapse: collapse; width: 690px; margin-bottom: 1.125rem; color: rgb(34, 34, 34); font-family: &quot;source sans pro&quot;, -apple-system, BlinkMacSystemFont, &quot;segoe ui&quot;, Roboto, &quot;helvetica neue&quot;, Arial, sans-serif, &quot;apple color emoji&quot;, &quot;segoe ui emoji&quot;, &quot;segoe ui symbol&quot;; font-size: 18px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><thead style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><th style="box-sizing: border-box; text-align: -webkit-match-parent; padding: 0.75rem; vertical-align: bottom; border-top: 1px solid rgb(222, 226, 230); border-bottom: 2px solid rgb(222, 226, 230);">HTTP method</th><th style="box-sizing: border-box; text-align: -webkit-match-parent; padding: 0.75rem; vertical-align: bottom; border-top: 1px solid rgb(222, 226, 230); border-bottom: 2px solid rgb(222, 226, 230);">Description</th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">GET</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Retrieve existing data</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">POST</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Add new data</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">PUT</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Update existing data</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">PATCH</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Partially update existing data</td></tr><tr style="box-sizing: border-box; color: rgb(34, 34, 34); background-color: rgba(0, 0, 0, 0.075);"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">DELETE</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Delete data</td></tr></tbody></table>

Once a REST API receives and processes an HTTP request, it returns a response with a HTTP status code. This status code provides information about the response and helps the client application know what kind of response it is.

Status codes are numbered based on the category of the result:

<table class="table table-hover" style="box-sizing: border-box; border-collapse: collapse; width: 690px; margin-bottom: 1.125rem; color: rgb(34, 34, 34);"><thead style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><th style="box-sizing: border-box; text-align: -webkit-match-parent; padding: 0.75rem; vertical-align: bottom; border-top: 1px solid rgb(222, 226, 230); border-bottom: 2px solid rgb(222, 226, 230);">Code range</th><th style="box-sizing: border-box; text-align: -webkit-match-parent; padding: 0.75rem; vertical-align: bottom; border-top: 1px solid rgb(222, 226, 230); border-bottom: 2px solid rgb(222, 226, 230);">Category</th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">1xx</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Informational response</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">2xx</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Successful operation</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">3xx</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Redirection</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">4xx</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Client error</td></tr><tr style="box-sizing: border-box; color: rgb(34, 34, 34); background-color: rgba(0, 0, 0, 0.075);"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">5xx</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Server error</td></tr></tbody></table>

You can learn more about HTTP status codes from the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

## API Endpoints

API Endpoints are the public URLs exposed by the server that a client application uses to access resources and data. 

For the sake of this tutorial, we'll be using the [Fake Store REST API](https://fakestoreapi.com/). More specifically, we'll be using the below endpoints:

<table class="table table-hover" style="box-sizing: border-box; border-collapse: collapse; width: 690px; margin-bottom: 1.125rem; color: rgb(34, 34, 34); font-family: &quot;source sans pro&quot;, -apple-system, BlinkMacSystemFont, &quot;segoe ui&quot;, Roboto, &quot;helvetica neue&quot;, Arial, sans-serif, &quot;apple color emoji&quot;, &quot;segoe ui emoji&quot;, &quot;segoe ui symbol&quot;; font-size: 18px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><thead style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><th style="box-sizing: border-box; text-align: -webkit-match-parent; padding: 0.75rem; vertical-align: bottom; border-top: 1px solid rgb(222, 226, 230); border-bottom: 2px solid rgb(222, 226, 230);">HTTP method</th><th style="box-sizing: border-box; text-align: -webkit-match-parent; padding: 0.75rem; vertical-align: bottom; border-top: 1px solid rgb(222, 226, 230); border-bottom: 2px solid rgb(222, 226, 230);">API endpoint</th><th style="box-sizing: border-box; text-align: -webkit-match-parent; padding: 0.75rem; vertical-align: bottom; border-top: 1px solid rgb(222, 226, 230); border-bottom: 2px solid rgb(222, 226, 230);">Description</th></tr></thead><tbody style="box-sizing: border-box;"><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">GET</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">/products</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Get a list of products.</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">GET</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">/products?limit=x</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Get only 5 products.</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">GET</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">/products/&lt;product_id&gt;</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Get a single product.</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">POST</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">/products</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Create a new product.</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">PUT</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">/products/&lt;product_id&gt;</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Update a product.</td></tr><tr style="box-sizing: border-box;"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">PATCH</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">/products/&lt;product_id&gt;</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Partially update a product.</td></tr><tr style="box-sizing: border-box; color: rgb(34, 34, 34); background-color: rgba(0, 0, 0, 0.075);"><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">DELETE</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);"><code style="box-sizing: border-box; font-family: SFMono-Regular, Menlo, Monaco, Consolas, &quot;liberation mono&quot;, &quot;courier new&quot;, monospace; font-size: 14.85px; color: rgb(34, 34, 34); overflow-wrap: break-word; white-space: nowrap;">/products/&lt;product_id&gt;</code></td><td style="box-sizing: border-box; padding: 0.75rem; vertical-align: top; border-top: 1px solid rgb(222, 226, 230);">Delete a product.</td></tr></tbody></table>

Each of the endpoints above performs a different action based on the HTTP method. For each API URL, the base URL is: `https://fakestoreapi.com`. We'll explore them one after another. 

But first we need to install an external library to consume these APIs. Most Python developers use the `requests` library to interact with web services. You can install this library using the `pip` command like this:

```bash
$ pip install requests
```

Once the library is installed, we're good to go!

## How to Make a GET Request

This is one of the most common HTTP request methods you'll come across. It is a **read-only** operation which allows you to retrieve data from the API. 

Let's try out the GET request on the first endpoint we mentioned above that responds with a list of products.

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products")
print(response.json())

```

The above script uses the `requests.get()` method to send a GET request on the API endpoint `/products`. It responds with a list of all the products. We then call `.json()` to view the JSON response, which looks like this:

```json
[
    {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
        "rating": {
            "rate": 3.9,
            "count": 120
        }
    },
    {
        "id": 2,
        "title": "Mens Casual Premium Slim Fit T-Shirts ",
        "price": 22.3,
        "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
        "rating": {
            "rate": 4.1,
            "count": 259
        }
    },
    {
        "id": 3,
        "title": "Mens Cotton Jacket",
        "price": 55.99,
        "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg",
        "rating": {
            "rate": 4.7,
            "count": 500
        }
    },
    {
        "id": 4,
        "title": "Mens Casual Slim Fit",
        "price": 15.99,
        "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg",
        "rating": {
            "rate": 2.1,
            "count": 430
        }
    },
    {
        "id": 5,
        "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        "price": 695,
        "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
        "category": "jewelery",
        "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg",
        "rating": {
            "rate": 4.6,
            "count": 400
        }
    },
    {
        "id": 6,
        "title": "Solid Gold Petite Micropave ",
        "price": 168,
        "description": "Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.",
        "category": "jewelery",
        "image": "https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg",
        "rating": {
            "rate": 3.9,
            "count": 70
        }
    },
    {
        "id": 7,
        "title": "White Gold Plated Princess",
        "price": 9.99,
        "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
        "category": "jewelery",
        "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg",
        "rating": {
            "rate": 3,
            "count": 400
        }
    },
    {
        "id": 8,
        "title": "Pierced Owl Rose Gold Plated Stainless Steel Double",
        "price": 10.99,
        "description": "Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel",
        "category": "jewelery",
        "image": "https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg",
        "rating": {
            "rate": 1.9,
            "count": 100
        }
    },
    {
        "id": 9,
        "title": "WD 2TB Elements Portable External Hard Drive - USB 3.0 ",
        "price": 64,
        "description": "USB 3.0 and USB 2.0 Compatibility Fast data transfers Improve PC Performance High Capacity; Compatibility Formatted NTFS for Windows 10, Windows 8.1, Windows 7; Reformatting may be required for other operating systems; Compatibility may vary depending on user’s hardware configuration and operating system",
        "category": "electronics",
        "image": "https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_.jpg",
        "rating": {
            "rate": 3.3,
            "count": 203
        }
    },
    {
        "id": 10,
        "title": "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
        "price": 109,
        "description": "Easy upgrade for faster boot up, shutdown, application load and response (As compared to 5400 RPM SATA 2.5” hard drive; Based on published specifications and internal benchmarking tests using PCMark vantage scores) Boosts burst write performance, making it ideal for typical PC workloads The perfect balance of performance and reliability Read/write speeds of up to 535MB/s/450MB/s (Based on internal testing; Performance may vary depending upon drive capacity, host device, OS and application.)",
        "category": "electronics",
        "image": "https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_.jpg",
        "rating": {
            "rate": 2.9,
            "count": 470
        }
    },
    {
        "id": 11,
        "title": "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
        "price": 109,
        "description": "3D NAND flash are applied to deliver high transfer speeds Remarkable transfer speeds that enable faster bootup and improved overall system performance. The advanced SLC Cache Technology allows performance boost and longer lifespan 7mm slim design suitable for Ultrabooks and Ultra-slim notebooks. Supports TRIM command, Garbage Collection technology, RAID, and ECC (Error Checking & Correction) to provide the optimized performance and enhanced reliability.",
        "category": "electronics",
        "image": "https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_.jpg",
        "rating": {
            "rate": 4.8,
            "count": 319
        }
    },
    {
        "id": 12,
        "title": "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
        "price": 114,
        "description": "Expand your PS4 gaming experience, Play anywhere Fast and easy, setup Sleek design with high capacity, 3-year manufacturer's limited warranty",
        "category": "electronics",
        "image": "https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_.jpg",
        "rating": {
            "rate": 4.8,
            "count": 400
        }
    },
    {
        "id": 13,
        "title": "Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin",
        "price": 599,
        "description": "21. 5 inches Full HD (1920 x 1080) widescreen IPS display And Radeon free Sync technology. No compatibility for VESA Mount Refresh Rate: 75Hz - Using HDMI port Zero-frame design | ultra-thin | 4ms response time | IPS panel Aspect ratio - 16: 9. Color Supported - 16. 7 million colors. Brightness - 250 nit Tilt angle -5 degree to 15 degree. Horizontal viewing angle-178 degree. Vertical viewing angle-178 degree 75 hertz",
        "category": "electronics",
        "image": "https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg",
        "rating": {
            "rate": 2.9,
            "count": 250
        }
    },
    {
        "id": 14,
        "title": "Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED ",
        "price": 999.99,
        "description": "49 INCH SUPER ULTRAWIDE 32:9 CURVED GAMING MONITOR with dual 27 inch screen side by side QUANTUM DOT (QLED) TECHNOLOGY, HDR support and factory calibration provides stunningly realistic and accurate color and contrast 144HZ HIGH REFRESH RATE and 1ms ultra fast response time work to eliminate motion blur, ghosting, and reduce input lag",
        "category": "electronics",
        "image": "https://fakestoreapi.com/img/81Zt42ioCgL._AC_SX679_.jpg",
        "rating": {
            "rate": 2.2,
            "count": 140
        }
    },
    {
        "id": 15,
        "title": "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats",
        "price": 56.99,
        "description": "Note:The Jackets is US standard size, Please choose size as your usual wear Material: 100% Polyester; Detachable Liner Fabric: Warm Fleece. Detachable Functional Liner: Skin Friendly, Lightweigt and Warm.Stand Collar Liner jacket, keep you warm in cold weather. Zippered Pockets: 2 Zippered Hand Pockets, 2 Zippered Pockets on Chest (enough to keep cards or keys)and 1 Hidden Pocket Inside.Zippered Hand Pockets and Hidden Pocket keep your things secure. Humanized Design: Adjustable and Detachable Hood and Adjustable cuff to prevent the wind and water,for a comfortable fit. 3 in 1 Detachable Design provide more convenience, you can separate the coat and inner as needed, or wear it together. It is suitable for different season and help you adapt to different climates",
        "category": "women's clothing",
        "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg",
        "rating": {
            "rate": 2.6,
            "count": 235
        }
    },
    {
        "id": 16,
        "title": "Lock and Love Women's Removable Hooded Faux Leather Moto Biker Jacket",
        "price": 29.95,
        "description": "100% POLYURETHANE(shell) 100% POLYESTER(lining) 75% POLYESTER 25% COTTON (SWEATER), Faux leather material for style and comfort / 2 pockets of front, 2-For-One Hooded denim style faux leather jacket, Button detail on waist / Detail stitching at sides, HAND WASH ONLY / DO NOT BLEACH / LINE DRY / DO NOT IRON",
        "category": "women's clothing",
        "image": "https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg",
        "rating": {
            "rate": 2.9,
            "count": 340
        }
    },
    {
        "id": 17,
        "title": "Rain Jacket Women Windbreaker Striped Climbing Raincoats",
        "price": 39.99,
        "description": "Lightweight perfet for trip or casual wear---Long sleeve with hooded, adjustable drawstring waist design. Button and zipper front closure raincoat, fully stripes Lined and The Raincoat has 2 side pockets are a good size to hold all kinds of things, it covers the hips, and the hood is generous but doesn't overdo it.Attached Cotton Lined Hood with Adjustable Drawstrings give it a real styled look.",
        "category": "women's clothing",
        "image": "https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2.jpg",
        "rating": {
            "rate": 3.8,
            "count": 679
        }
    },
    {
        "id": 18,
        "title": "MBJ Women's Solid Short Sleeve Boat Neck V ",
        "price": 9.85,
        "description": "95% RAYON 5% SPANDEX, Made in USA or Imported, Do Not Bleach, Lightweight fabric with great stretch for comfort, Ribbed on sleeves and neckline / Double stitching on bottom hem",
        "category": "women's clothing",
        "image": "https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_.jpg",
        "rating": {
            "rate": 4.7,
            "count": 130
        }
    },
    {
        "id": 19,
        "title": "Opna Women's Short Sleeve Moisture",
        "price": 7.95,
        "description": "100% Polyester, Machine wash, 100% cationic polyester interlock, Machine Wash & Pre Shrunk for a Great Fit, Lightweight, roomy and highly breathable with moisture wicking fabric which helps to keep moisture away, Soft Lightweight Fabric with comfortable V-neck collar and a slimmer fit, delivers a sleek, more feminine silhouette and Added Comfort",
        "category": "women's clothing",
        "image": "https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg",
        "rating": {
            "rate": 4.5,
            "count": 146
        }
    },
    {
        "id": 20,
        "title": "DANVOUY Womens T Shirt Casual Cotton Short",
        "price": 12.99,
        "description": "95%Cotton,5%Spandex, Features: Casual, Short Sleeve, Letter Print,V-Neck,Fashion Tees, The fabric is soft and has some stretch., Occasion: Casual/Office/Beach/School/Home/Street. Season: Spring,Summer,Autumn,Winter.",
        "category": "women's clothing",
        "image": "https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_.jpg",
        "rating": {
            "rate": 3.6,
            "count": 145
        }
    }
]
```

If you look closely, the JSON response looks like list of Python dictionaries. JSON is a very popular data interchange format for REST APIs.

You can also print other attributes related to the response such as the status code.

```python
print(response.status_code)

# OUTPUT
>>> 200
```

As we know, status code 200 means a success response. 

Since the `/products` endpoint returns a lot of data, let's limit this data to just 3 products. 

To do this, we have an endpoint `/products?limit=x` where x is a positive integer. The `limit` is called query parameter. Let's see how we can add this query parameter in the request.

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

response = requests.get(f"{BASE_URL}/products", params=query_params)
print(response.json())

```

The `requests.get()` method takes a parameter called `params` where we can specify our query parameters in the form of a Python dictionary. Thus, we have created a dictionary called `query_params` and passed `limit` as the key and `3` as the value. We then passed this `query_params` in the `requests.get()`. The output now looks like this:

```json
[
  {
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    "rating": { "rate": 3.9, "count": 120 }
  },
  {
    "id": 2,
    "title": "Mens Casual Premium Slim Fit T-Shirts ",
    "price": 22.3,
    "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg",
    "rating": { "rate": 4.1, "count": 259 }
  },
  {
    "id": 3,
    "title": "Mens Cotton Jacket",
    "price": 55.99,
    "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg",
    "rating": { "rate": 4.7, "count": 500 }
  }
]

```

Now we have the response data limited to just 3 products. Let's try to get only one product with the `id` 18.

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products/18")
print(response)
```

Since we have an endpoint `/products/<product_id>`, we can pass the `id` 18 in the API URL and make a GET request on it. The response looks like this:

```json
{
    "id": 18,
    "title": "MBJ Women's Solid Short Sleeve Boat Neck V ",
    "price": 9.85,
    "description": "95% RAYON 5% SPANDEX, Made in USA or Imported, Do Not Bleach, Lightweight fabric with great stretch for comfort, Ribbed on sleeves and neckline / Double stitching on bottom hem",
    "category": "women's clothing",
    "image": "https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_.jpg",
    "rating": {
        "rate": 4.7,
        "count": 130
    }
}
```

## How to Make a POST Request

We use the POST request to add new data to the REST API. The data is sent to the server in JSON format which looks like a Python dictionary. According to the Fake Store API documentation, a product has the following attributes: `title`, `price`, `description`, `image` and `category`. So, a new product looks like this:

```python
new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}
```

We can send a POST request using the `requests.post()` method like this:

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json())
```

In the `requests.post()` method, we can pass JSON data using the `json` argument. Using the `json` argument automatically sets the `Content-Type` to `Application/JSON` in the request header. 

Once we make a POST request on the `/products` endpoint, we get a product object with the `id` in the response. The response looks like this:

```json
{
  "_id": "61b45067e087f30012c45a45",
  "id": 21,
  "title": "test product",
  "price": 13.5,
  "description": "lorem ipsum set",
  "image": "https://i.pravatar.cc",
  "category": "electronic"
}

```

If we don't use the `json` argument, we have to make the POST request like this:

```python
import requests
import json

BASE_URL = 'https://fakestoreapi.com'

new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(f"{BASE_URL}/products", data=json.dumps(new_product), headers=headers)
print(response.json())

```

In this case where we use the `data` argument instead of `json`, we need to set the `Content-Type` to `application/json` in the header explicitly. While in the case of the `json` argument, we don't need to serialize the data – but we need to serialize the data using `json.dumps()` in this case.

## How to Make a PUT Request

We often need to update existing data in the API. Using the PUT request, we can update the complete data. This means that when we make a PUT request, it replaces the old data with the new data.

In the POST request, we had created a new product whose `id` was 21. Let's update the old product with a new product by making a PUT request on the `products/<product_id>` endpoint.

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

updated_product = {
    "title": 'updated_product',
    "category": 'clothing'
}

response = requests.put(f"{BASE_URL}/products/21", json=updated_product)
print(response.json())

```

When we make the PUT request with the `updated_product` using the `requests.put()` method, it responds with the following JSON data:

```json
{
  "id": "21",
  "title": "updated_product",
  "category": "clothing"
}
```

Notice that the old product has been completely replaced with the updated product.

## How to Make a PATCH Request

Sometime, we do not need to replace the old data completely. Rather we wish to modify only certain fields. In that case, we use the PATCH request. 

Let's update the category of the product back from **clothing** to **electronic** by making a PATCH request on the `products/<product_id>` endpoint.

```python
import requests

BASE_URL = 'https://fakestoreapi.com'

updated_product = {
    "category": 'electronic'
}

response = requests.patch(f"{BASE_URL}/products/21", json=updated_product)
print(response.json())
```

In this case, we use the `requests.patch()` method which returns a response like this:

```json
{
  "id": "21",
  "title": "updated_product",
  "category": "electronic"
}
```

Notice that this time the entire data has not changed – only the category field has been updated.

## How to Make a DELETE Request

As the name suggests, if you wish to delete a resource from the API, you can use a DELETE request. Let's delete this product with the `id` 21.

```python
import requests

BASE_URL = 'https://fakestoreapi.com'


response = requests.delete(f"{BASE_URL}/products/21")
print(response.json())
```

The `requests.delete()` method helps us make a DELETE request on the `/products/<product_id>` endpoint.

## Wrapping Up

In this tutorial, we learned how we can interact with web services using an awesome tool called **requests** in Python.

I hope you enjoyed it – and thanks for reading!

