---
title: REST API cURL Post Request via Construct 3 GameDev Tool & AJAX Module
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-23T02:25:54.000Z'
originalURL: https://freecodecamp.org/news/rest-api-curl-post-request-via-construct-3-gamedev-tool-ajax-module
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/c3-woo-wp-banner.jpg
tags:
- name: construct 3
  slug: construct-3
- name: Ajax
  slug: ajax
- name: curl
  slug: curl
- name: json
  slug: json
- name: REST API
  slug: rest-api
- name: woocommerce
  slug: woocommerce
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: 'By Andreas Lopez

  Hello FreeCodeCamp Reader Community! This Tutorial is made as a little thought experiment
  but might have some merit for the one or other person.


  Please keep in mind that this plugin is making an example by adding a product via
  Const...'
---

By Andreas Lopez

Hello FreeCodeCamp Reader Community! This Tutorial is made as a little thought experiment but might have some merit for the one or other person.

> Please keep in mind that this plugin is making an example by adding a product via Construct 3 Forms + REST API cURL Request to an existing WordPress + WooCommerce installation.

The principles still are valid for other purposes you might have with the REST API, and I included the .c3p on the bottom of this tutorial. There are more elegant ways about feeding the arrays of information to the application, but this is a quick demo as proof-of-concept that I put together within 2 hours and felt like sharing it due to the lack of API and AJAX information for Construct 3.

**Here is the entire code in a single screenshot:**

![Image](https://www.freecodecamp.org/news/content/images/2019/06/c3-api-example.jpg)
_Construct 3 Source Code Screenshot_

# The Code Broken Down once we click on 'Create Product' button
* productjson is an obligatory text field outside of the viewport on the layout.
* productjson contains our entire payload data pre-formatted as json to allow the REST API to work properly.
* The payload contains dynamically created content which are the forms in the layout such as product name, sku, price, etc.
* The AJAX module that I renamed AJAX_Data will set the Request_Header to "Content-Type" with the value of "application/json", because the REST API via cURL request will utilize JSON.
* The next AJAX_Data with the 'Post to URL' request will be our actual API request.
* The Tag is merely a name which can be utilized for example to return the values of the request, in the example of my project - as debugging information.
* The URL will start with your domain, i.e. 'https://www.example.com' The next part of the URL is the API request you would like to make, in our example as per WooCommerce documentation to add a product we need '/wp-json/wc/v3/products?'
* Last but not least for the URL we need the consumer key and secret in this manner: 'consumer_key=<consumer_key>&consumer_secret=<consumer_secret>'
* The full URL looks like this: "https://www.example.com/wp-json/wc/v3/products?consumer_key=<consumer_key>&consumer_secret=<consumer_secret>"
* Next up is the Data. This is simple since we already have made a text box for this exact purpose. Simply refer to it here, in my example the Data will be 'productjson.Text'.
* And at the very end, what type of Request. Since we are creating a product we will need 'POST', if we were to retrieve a product we would want a 'GET' request, see the respective documentation of the API you are using.

### .c3p File Download:

[https://drive.google.com/open?id=16DKq5RJD5tCw57oZPruGk_mtTIAe-Um9](https://drive.google.com/open?id=16DKq5RJD5tCw57oZPruGk_mtTIAe-Um9%5B/url%5D)

# Requirements for my .c3p example
* WordPress Installation with WooCommerce installed
* REST API enabled and issued a consumer secret & key
* Replace my API secret and key example in the code
* Uploaded an image in the media gallery within WordPress
* Created a Product Category within WordPress/WooCommerce

If you need a free WordPress environment to play around with, I used [https://pantheon.io](https://pantheon.io), under the free plan you can get 2 sandbox sites. Just make sure to install the WP-CORS plugin first and set allowed sites to '*' as seen in their documentation here:  
[https://pantheon.io/docs/platform-considerations/#cors](https://pantheon.io/docs/platform-considerations/#cors%5B/url%5D)

[https://wordpress.org/plugins/wp-cors/](https://wordpress.org/plugins/wp-cors/%5B/url%5D)

### API Source Information & Relevant C3 Documentation:

[WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs)  
[Construct 3 AJAX Documentation](https://www.construct.net/en/make-games/manuals/construct-3/plugin-reference/ajax)  
[JSON Validator tool to verify if your JSON is properly formatted.](https://jsonlint.com/)  
[Original Tutorial I wrote on Construct.net](https://www.construct.net/en/tutorials/rest-api-curl-post-request-2245)

