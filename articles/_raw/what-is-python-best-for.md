---
title: Python Use Cases – What is Python Best For?
subtitle: ''
author: Juan Cruz Martinez
co_authors: []
series: null
date: '2023-12-05T21:22:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-python-best-for
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/python-best-for.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Developers are often very passionate about their tech stack, and they'll\
  \ likely recommend it for anything. \nIt is very common to see devs on social media\
  \ sharing how you can build anything with JavaScript or how Python is great for\
  \ data scientists.\nA..."
---

Developers are often very passionate about their tech stack, and they'll likely recommend it for anything. 

It is very common to see devs on social media sharing how you can build anything with JavaScript or how Python is great for data scientists.

As a Python fanatic myself, I actually don't always use Python for my projects because Python doesn't excel at everything. So today, I want to share my thoughts about the main use cases in which Python shines.

## Scripting and Automation

It's never been easier to script and automate tasks thanks to the rise of no-code and tools like Apple's Shortcuts app. But even after integrating those into my day-to-day routine, there are many times when I still rely on Python to get things done.

I use Python in part because I'm already familiar with the language. Plus its simplicity and extensive library ecosystem help me get results quicker than with other programming languages.

Here are some of the tasks you can automate with Python along with some personal examples:

### File management

You can automate tasks like file organization, renaming, copying, and deletion using Python. 

I personally use Obsidian as my note-taking tool, where all my notes land in a dedicated "inbox" folder for processing. A Python script then reads the notes and moves each one to the appropriate folder based on their contents. 

The script sounds fancy, but it is pretty simple, as I already have a system in place.

Here is what my script for organizing notes looks like:

```python
import shutil
import os
import frontmatter

# List of frontmatter properties with folder destinations
frontmatter_to_dir = {
    'project': '1. Projects',
    'area': '2. Areas',
    'resource': '3. Resources',
}

def try_move_file(file, destination):
    print('- Moving file', file, "to", destination)
    try:
        shutil.move(file, destination)
    except Exception as err:
        print('-  - Project not found', err)


# Read all the files inside the "!inbox" directory
notes = os.listdir('!inbox')
for note in notes:
    note_path =  f"!inbox/{note}"
    # Read the file's frontmatter
    note_metadata = frontmatter.load(note_path)
    
    # Check if the file has a property to categorize this note,
    # for example: project, area, or resource
    for group, group_destination in frontmatter_to_dir.items():
        if group in note_metadata:
            # Try moving the file, it can be the case the project is
            # for example mispelled, in that case it won't do anything with the note
            try_move_file(note_path, f"{group_destination}/{note_metadata[group]}/{note}")
```

### Data processing

Python is in a unique position when it comes to data processing. Whether you are trying to process text, images, large data sets, or perform complex calculations, there are excellent Python libraries for all use cases. 

I usually create Python scripts to understand information. For example, I run a company with multiple SaaS products, and I have Python scripts to process statements and help me with the accounting.

### Extracting data from text files or web pages

You can use Python to extract data from websites, analyze web content, and gather information to send summaries or others. I used this until very recently to download RSS feeds from my favorite blogs and websites and create a one-email summary that I would then use to read the most interesting articles. I'm now using Readwise Reader for this purpose.

To showcase how to extract data from web pages using Python, I created a small script that would visit a site, parse it’s HTML and return information from elements in the DOM. In particular, it will visit a newspaper, find information about the exchange rate for the pair ARS/USD of the day, and print it on the screen. Great script for those living in Argentina.

```python
import requests
from bs4 import BeautifulSoup

# Load the newspapaer website to scrap information about the current exchange rate for USD/ARS
URL = 'https://www.lanacion.com.ar/'
page = requests.get(URL)

# Parse the HTML data
soup = BeautifulSoup(page.content, "html.parser")
# Use select to find an element in the DOM
# In our case, we need a span inside a link with a specific title
span = soup.select('a[title="Dólar blue"] span')[0]
price = span.get_text()
# In a real scenario, instead of simply printing the price,
# I'd for example, email me the results or do some other processing
print(price) # e.g. $930,00
```

### Sending emails

This is how my newsletter started: sending emails to subscribers through a Python script. Now, that's not scaling very well as I wanted fancier features, and I moved on to ConvertKit – but the Python script was good for being a free, smaller-scale solution.

Sending emails require access to an SMTP server, or similar service, in my case I was using a proprietary API to send those, Amazon SES, because when it comes to emailing in bulk, there are certain measures you want to take not to damage the score of your domain, or your emails will end up on the spam folder.

Here is how I was doing that:

```python
import boto3
import json

# All email addresses where store in s3
s3_bucket = ''
# Provide the path to your file in the S3 bucket
s3_key = 'mail_list/addresses.txt'

s3_client = boto3.client('s3')
# Retrieve the email ids from the file
s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
email_ids = s3_object['Body'].read().decode('utf-8').split('\n')

# Send email for each email ID
ses_client = boto3.client('ses')
for email_id in email_ids:
	email_id = email_id.strip() # Remove leading/trailing whitespace
	
	# Perform email sending operations using SES client
	response = ses_client.send_email(
		Source='<FromAddress>',
		Destination={'ToAddresses': [email_id]},
		Message={
			'Subject': {'Data': 'Your Subject'},
			'Body': {'Text': {'Data': 'Your Email Body'}}
		}
	)

print(f"Email sent to {email_id}. Message ID: {response['MessageId']}")
```

## Web Applications and APIs

It's true – you can't do web development just with Python. You'll still need HTML, CSS, and JavaScript. But when it comes to building backends for web applications, Python is a fantastic option. 

Thanks to popular Python frameworks like [Django](https://www.notion.so/Draft-Script-1d2f649493b04a0f84acc9dcc91f0c7a?pvs=21), [Flask](https://flask.palletsprojects.com/en/3.0.x/), and [FastAPI](https://fastapi.tiangolo.com/), it's very easy to start building your web applications and APIs.

In most products and applications I build, I use a combination of [NextJS](https://nextjs.org/) for the frontend, powered by a Python backend using FastAPI, and it's a killer combo. 

But I'm not alone in choosing Python to build web backends. Companies like Microsoft, Instagram, Pinterest, and the Washington Post use Python to serve millions of users.

## Data Analysis / Data Science / AI

Python is the undeniable leader in data science, artificial intelligence, and machine learning. This is in part thanks to its vast ecosystem of open-source libraries, like [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Tensorflow](https://www.tensorflow.org/), and [Python in Excel](https://techcommunity.microsoft.com/t5/excel-blog/announcing-python-in-excel-combining-the-power-of-python-and-the/ba-p/3893439) among others. This extensive toolkit empowers you to tackle virtually any challenge within these domains.

Are you performing complex statistical analysis? No problem, there's a library for that. Are you eager to start using state-of-the-art machine learning models? Python has you covered! Do you need a complex neural network? Of course, you can do that!

Python's vast ecosystem of libraries allows you to build what you need quickly, with libraries that are production-ready, fast, and efficient and that have high-quality APIs.

Here are some examples of related applications of Python for data science and AI:

* Time series analysis
* Data Visualization
* Sales predictions
* Language processing
* Sentiment analysis
* Recommendation systems (like music, videos, and so on)
* Classification
* Computer vision
* Self-driving cars
* and many more...

## Application Testing

Python's user-friendly syntax and readability make it an excellent choice for QA testers of all skill levels. Its straightforward structure and clear code organization facilitate rapid prototyping and implementation of test scripts.

Again, it's thanks to Python's rich ecosystem with libraries like Playwright and Selenium that Python is a great option for this category.

For web applications, QA engineers write test scripts that load the application in a headless browser, normally a QA or test environment, and perform a series of validations to determine that the application is correctly working.

For example, if you want to test a user’s list page, you can load the page, and querying DOM elements, you can validate that effectively the app is rendering results. Even more so, you can simulate keyboard strokes, clicks, complete forms, and much more with these tools.

Here is a same script that loads the [python.org](http://python.org/) website, performs a search, and validates that the result by comparing the resulting page against the `No results found` message.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set the driver to use Firefox, can also be Chrome, IE, and Remote
driver = webdriver.Firefox()
# Load the target website
driver.get("http://www.python.org")
# Validate that the page loaded by comparing the page title
assert "Python" in driver.title
# Find the search input element by name
elem = driver.find_element(By.NAME, "q")
# Empty it
elem.clear()
# Type `pycon`
elem.send_keys("pycon")
# Press an enter to trigger the search form
elem.send_keys(Keys.RETURN)
# Validate that the text `No results found.` is not present in the page
assert "No results found." not in driver.page_source
# Close the browser
driver.close()
```

## Conclusion

Python's versatility and extensive library ecosystem make it an excellent choice for various projects. Whether you need to automate tasks, process data, build web applications and APIs, perform data analysis and AI, or conduct application testing, Python has you covered.

Its simplicity, readability, and powerful libraries allow you to achieve results quickly and efficiently. So, next time you're considering a programming language for your project, consider Python's strengths in these areas.

Thanks for reading!

You can follow me ([@bajcmartinez](https://twitter.com/bajcmartinez)) along with [@jesstemporal](https://twitter.com/jesstemporal) on Twitter/X to learn more about Python and how to build secure Python applications. We're developer advocates at [Auth0 by Okta](https://auth0.com/) and regularly post content and live streams about Python.

