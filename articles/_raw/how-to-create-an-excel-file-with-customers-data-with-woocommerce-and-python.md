---
title: How to Create an Excel File that Pulls Customer Data with WooCommerce and Python
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2021-10-08T15:15:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-excel-file-with-customers-data-with-woocommerce-and-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/cover-1.jpg
tags:
- name: ecommerce
  slug: ecommerce
- name: excel
  slug: excel
- name: Python
  slug: python
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: '“Hey, could you please send me our customers'' emails? We’re about to launch
  a new marketing campaign and…we need them ASAP.”

  If you work in the Web department on a corporate level, you''ve probably heard this
  sentence hundreds of times. So, today I wa...'
---

“Hey, could you please send me our customers' emails? We’re about to launch a new marketing campaign and…we need them ASAP.”

If you work in the Web department on a corporate level, you've probably heard this sentence hundreds of times. So, today I want to share how I solved this issue for a company I worked at.

## What Was the Request?

We had an e-commerce app built with WooCommerce, that got thousands of orders every day worldwide. To register, users had to add their first name, last name, and email address. 

Our marketing department asked my team to provide them with the email address and first names of all our customers to launch a new campaign. 

I expected them to ask for a CSV file to upload contacts massively to their marketing platform. Instead, they told me they needed an Excel file since they had to edit it before going ahead with the campaign launch. 

Once they assigned me the Jira issue, I was ready to start.

## Analyzing the Problem

WooCommerce provides users with the export functionality to get customers' data but it doesn’t generate an Excel file. It generates a CSV or an XML file.

When you work with a tool like WordPress, the first option you think about is using a plugin and get what you need. 

I found a few options on the WordPress plugin directory, but there is a lot to consider every time you install a new plugin in your instance. You have to think about maintenance costs (consider every time a developer works on it, they log hours that affect your budget), security vulnerabilities, and – last but not the least – purchase approval can take a long time.  

I also considered a second option: downloading the CSV via the user interface and turning it into an Excel file by using one of the thousand services you can find online. 

But using third parties services could break critical security and privacy policies and the final result is not always reliable. So I decided to go no further in this direction.

In the end, I thought developing a script was the best and fastest option to solve this task.  

WordPress provides developers with APIs. Many other plugins from the WordPress system provide APIs as well, and WooCommerce is not an exception. The [documentation](https://docs.woocommerce.com/document/woocommerce-rest-api/) is robust and it offers links to libraries for the most used languages such as Node.js, Python, PHP, and Ruby.

I decided to go with Python and use this technology to develop a script that generates an Excel file with the following structure:

* Two columns: first name and email
* One row per customer

I chose Python for several reasons: there are hundreds of libraries that can help you get get the job done, it is flexible, and it is very useful when it comes to handling data.

I also decided to use Pandas and Openpyxl to handle data and create the Excel file.

## Before coding, let’s get what we need

To work with the WooCommerce API, I need to generate the APIs keys to work with. You can get more info on WooCommerce official [documentation](https://docs.woocommerce.com/document/woocommerce-rest-api/). 

First, you need to log into your WooCommerce instance, and then go to WooCommerce > Settings > Advanced > REST API.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/0-1.png)

Then I'll give it a brief description, choose the user I want to generate the API for, choose the permissions granted (Read/Write or both), and then hit “Generate API key”.

Next, I’ll get the Consumer Key and the Consumer Secret:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/screencapture-marcoventuritest-it-wooTest-wp-admin-admin-php-2021-10-06-17_19_38.png)

## How to Prepare the Environment

The very first thing I did was add the necessary libraries to develop my script. I started with the Python library for WooCommerce. To install it, I ran this command:

```python
pip install woocommerce
```

Good. Now I'll go ahead and install Pandas, a data analysis and manipulation tool for Python:

```python
pip install pandas
```

After that, I installed Openpyxl, a Python library to read and write Excel files:

```python
pip install openpyxl
```

## Let’s code

I made the API call using the API function provided by the WooCommerce Python library and I stored it in a variable. Then I passed the function the base URL of my WooCommerce website, the consumer key, the consumer secret, and the version.

```python
wcdata = API(
    url='<BASE_URL>',
    consumer_key='ck_XXXXXXXXXXXXXXXXXXXX',
    consumer_secret='cs_XXXXXXXXXXXXXXXXXXXX',
    version='wc/v3'
)
```

Then I used the GET function to call the "customers" endpoint and I created locally a JSON file (“contacts.json”) with the data I got from the endpoint I called right before:

```python
newJson = wcdata.get('customers').json()
with open('contacts.json', 'w') as f:
    json.dump(newJson, f, ensure_ascii=False, indent=4)
```

I converted it to a Pandas object and stored it in the "df_json" variable:

```python
df_json = pd.read_json('contacts.json')
```

I used the `to_excel()` function to turn the object into an Excel file. I passed the function three arguments:

* The name of the file I was about to create
* The index, set to “false” since I didn't want the record id to be printed on my file
* The columns I wanted to print on my file (first_name and email)

```python
df_json.to_excel('customers_contacts.xlsx', index=False, columns=('first_name', 'email'))
```

I ran the script and I got this:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/6bis.png)

That’s it. This is how I created an Excel file with customers' emails and first names with WooCommerce APIs and Python in less than 20 lines of code. 

Of course, it is a script you can run via the command line when needed or you can also automate it to regularly generate reports about the e-commerce you and your team are running.

## Final thoughts

I also wanted to share some other content I found on the web while studying to develop this script. 

The first one is a Stack Overflow [question](https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file). It helped me optimize my code while creating the JSON file. I really appreciated the chosen question, especially when it suggested how you can write a "nicer" JSON file on a modern system. 

The second one is about Pandas. If you write Python code, one day or another, you'll have to deal with data and their manipulation. This [article](https://www.marsja.se/how-to-convert-json-to-excel-python-pandas/) by Erik Marsja explains really well how you can convert your JSON file to Excel with Pandas. It provides readers with several tips on how they can use this powerful library to display the data they want in an efficient and effective way.

Feel free to share this post if you found it useful! You can also find the full code on this Github [repo](https://github.com/mventuri/-woocommerce-to-excel-python).


