---
title: How to Use Python to Build Your Own Web Scraper
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-07-10T13:11:06.000Z'
originalURL: https://freecodecamp.org/news/use-python-sdk-to-build-a-web-scraper
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/ilya-pavlov-OqtafYT5kTw-unsplash.jpg
tags:
- name: Python
  slug: python
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Jess Wilk

  What is Web scraping?

  Web scraping is a technique used to collect large amounts of data automatically
  using a programming script. This makes it useful for many professionals such as
  data analysts, market researchers, SEO specialists, bus...'
---

By Jess Wilk

## **What is Web scraping?**

Web scraping is a technique used to collect large amounts of data automatically using a programming script. This makes it useful for many professionals such as data analysts, market researchers, SEO specialists, business analysts, and academic researchers.

## **What You'll Learn Here**

Python provides two libraries, Requests and Beautiful Soup, that help you scrape websites more easily. The combined use of Python's Requests and Beautiful Soup can retrieve HTML content from a website and then parse it to extract the data you need. In this article, I'll show you how to use these libraries with an example.

By the end of this guide, you will be equipped to build your own Web Scraper and have a more profound understanding of working with a large amount of data and how to apply it to make data-driven decisions.

Please note that while a web scraper is a useful tool, make sure you're compliant with all legal guidelines. This involves respecting the website's `robots.txt` file and adhering to the terms of service so you avoid unauthorized data extraction. 

Also, before scraping, make sure that the scraping process does not harm the website's functionality or overload its servers. Finally, respect data privacy by not scraping personal or sensitive information without proper consent.

## **How Beautiful Soup and Python Requests Work Together**

Let’s understand the role of each library. 

The Python Requests library is responsible for fetching HTML content from the URL you provide in the script. Once it retrieves the content, it stores the data in a response object. 

Beautiful Soup then takes over, transforming the raw HTML from the Requests response into a structured format and parsing it. You can then scrape data from the parsed HTML by specifying attributes, allowing you to automate the collection of specific data from websites or repositories.

But this duo has its limitations. The Requests library can’t handle websites with dynamic JavaScript content. So you should use it primarily for sites that serve static content from servers. If you need to scrape a dynamically loaded site, you will have to use more advanced automation tools like Selenium.

## **How to Build a Web Scraper with Python** 

Now that we understand what Beautiful Soup and Python Requests can do, let’s discuss how we can scrape data using these tools.

In the following example, we’ll be scraping data from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/datasets). 

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXd2MTmii-KD8tu6AAeHhbr9Sb5vauq3jC3AcYc2Yvd4kcCQLdTdVrBqZuFOpF-vKQ3E012hV7W6bm0iOtqrCsvJx6xsT165mKqbKVC8Kf48ZxOMq-Joi7n2jDw6fl3AM4XLVBuikCJpXTIB6c6JriJtP9MQ?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Datasets at the UC Irvine Machine Learning Repository_

As you can see, it contains many datasets, and you can find further details about each dataset by going to a dedicated page for the dataset. You can access the dedicated page by clicking on the dataset name in the list above. 

Check out the image below to get an idea of the information provided for each dataset.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXcb7_BVgpIh1P931U-HHX6BKIPN1ODKRzc6WqjX-n77uA9Uvz_e80wqc2YtJx2-Rq3HzWKtlDE31gV-7jz0UASzKrhq86X45paNDkVVO5oNXeaRZ99vIs45g1TwMk54hpyEetzyuDjMgPYW4KKW-oPhKjh8?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Iris dataset_

The code we write below will go through each dataset, scrape the details, and save them to a CSV file.

### Prerequisites

To try out this tutorial, you need several prerequisites set up.

I am assuming you already have a Python installation on your machine. If not, please download the latest Python from the [official website](https://www.python.org/downloads/).

The Requests and Beautiful Soup libraries don't come with Python. You will have to install them separately. For this, you can use the pip package manager which is included by default with Python installation since Python 3.4.

You can use pip to install the Requests and Beautiful Soup libraries using the following commands:

```python
pip install requests
pip install beautifulsoup4
```

If they were successfully installed, now you are ready to start coding.

### Step 1: Import Necessary Libraries

First, import the necessary libraries: Requests for making HTTP requests, BeautifulSoup for parsing HTML content (if you don't already have it installed from the previous step), and CSV for saving the data.

```python
import requests
from bs4 import BeautifulSoup
import csv
```

### Step 2: Define the Base URL and CSV Headers

Set the base URL for the dataset listings and define the headers for the CSV file where the scraped data will be saved.

```python
def scrape_uci_datasets():
    base_url = "https://archive.ics.uci.edu/datasets"


    headers = [
        "Dataset Name", "Donated Date", "Description",
        "Dataset Characteristics", "Subject Area", "Associated Tasks",
        "Feature Type", "Instances", "Features"
    ]


    data = []

```

### Step 3: Create a Function to Scrape Dataset Details

Define a function `scrape_dataset_details` that takes the URL of an individual dataset page, retrieves the HTML content, parses it using BeautifulSoup, and extracts relevant information.

```python

    def scrape_dataset_details(dataset_url):
        response = requests.get(dataset_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_name = soup.find(
            'h1', class_='text-3xl font-semibold text-primary-content')
        dataset_name = dataset_name.text.strip() if dataset_name else "N/A"


        donated_date = soup.find('h2', class_='text-sm text-primary-content')
        donated_date = donated_date.text.strip().replace(
            'Donated on ', '') if donated_date else "N/A"


        description = soup.find('p', class_='svelte-17wf9gp')
        description = description.text.strip() if description else "N/A"


        details = soup.find_all('div', class_='col-span-4')


        dataset_characteristics = details[0].find('p').text.strip() if len(
            details) > 0 else "N/A"
        subject_area = details[1].find('p').text.strip() if len(
            details) > 1 else "N/A"
        associated_tasks = details[2].find('p').text.strip() if len(
            details) > 2 else "N/A"
        feature_type = details[3].find('p').text.strip() if len(
            details) > 3 else "N/A"
        instances = details[4].find('p').text.strip() if len(
            details) > 4 else "N/A"
        features = details[5].find('p').text.strip() if len(
            details) > 5 else "N/A"


        return [
            dataset_name, donated_date, description, dataset_characteristics,
            subject_area, associated_tasks, feature_type, instances, features
        ]

```

The `scrape_dataset_details` function retrieves the HTML content of a dataset page and parses it using BeautifulSoup. It extracts information by targeting specific HTML elements based on their tags and classes, such as dataset names, donation dates, and descriptions. 

The function uses methods like `find` and `find_all` to locate these elements and retrieve their text content, handling cases where elements might be missing by providing default values. 

This systematic approach ensures that the relevant details are accurately captured and returned in a structured format.

### Step 4: Create a Function to Scrape Dataset Listings

Define a function `scrape_datasets` that takes the URL of a page listing multiple datasets, retrieves the HTML content, and finds all dataset links. For each link, it calls `scrape_dataset_details` to get detailed information.

```python
    def scrape_datasets(page_url):
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_list = soup.find_all(
            'a', class_='link-hover link text-xl font-semibold')


        if not dataset_list:
            print("No dataset links found")
            return


        for dataset in dataset_list:
            dataset_link = "https://archive.ics.uci.edu" + dataset['href']
            print(f"Scraping details for {dataset.text.strip()}...")
            dataset_details = scrape_dataset_details(dataset_link)
            data.append(dataset_details)
```

### Step 5: Loop Through Pages Using Pagination Parameters

Implement a loop to navigate through the pages using pagination parameters. The loop continues until no new data is added, indicating that all pages have been scraped.

```python
    skip = 0
    take = 10
    while True:
        page_url = f"https://archive.ics.uci.edu/datasets?skip={skip}&take={take}&sort=desc&orderBy=NumHits&search="
        print(f"Scraping page: {page_url}")
        initial_data_count = len(data)
        scrape_datasets(page_url)
        if len(
                data
        ) == initial_data_count:  
            break
        skip += take
```

### Step 6: Save the Scraped Data to a CSV File

After scraping all the data, save it to a CSV file.

```python
    with open('uci_datasets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


    print("Scraping complete. Data saved to 'uci_datasets.csv'.")
```

### Step 7: Run the Scraping Function

Finally, call the `scrape_uci_datasets` function to start the scraping process.

```python
scrape_uci_datasets()
```

## **Full Code**

Here is the complete code for the web scraper:

```python
import requests
from bs4 import BeautifulSoup
import csv


def scrape_uci_datasets():
    base_url = "https://archive.ics.uci.edu/datasets"


    headers = [
        "Dataset Name", "Donated Date", "Description",
        "Dataset Characteristics", "Subject Area", "Associated Tasks",
        "Feature Type", "Instances", "Features"
    ]


    # List to store the scraped data
    data = []


    def scrape_dataset_details(dataset_url):
        response = requests.get(dataset_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_name = soup.find(
            'h1', class_='text-3xl font-semibold text-primary-content')
        dataset_name = dataset_name.text.strip() if dataset_name else "N/A"


        donated_date = soup.find('h2', class_='text-sm text-primary-content')
        donated_date = donated_date.text.strip().replace(
            'Donated on ', '') if donated_date else "N/A"


        description = soup.find('p', class_='svelte-17wf9gp')
        description = description.text.strip() if description else "N/A"


        details = soup.find_all('div', class_='col-span-4')


        dataset_characteristics = details[0].find('p').text.strip() if len(
            details) > 0 else "N/A"
        subject_area = details[1].find('p').text.strip() if len(
            details) > 1 else "N/A"
        associated_tasks = details[2].find('p').text.strip() if len(
            details) > 2 else "N/A"
        feature_type = details[3].find('p').text.strip() if len(
            details) > 3 else "N/A"
        instances = details[4].find('p').text.strip() if len(
            details) > 4 else "N/A"
        features = details[5].find('p').text.strip() if len(
            details) > 5 else "N/A"


        return [
            dataset_name, donated_date, description, dataset_characteristics,
            subject_area, associated_tasks, feature_type, instances, features
        ]


    def scrape_datasets(page_url):
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')


        dataset_list = soup.find_all(
            'a', class_='link-hover link text-xl font-semibold')


        if not dataset_list:
            print("No dataset links found")
            return


        for dataset in dataset_list:
            dataset_link = "https://archive.ics.uci.edu" + dataset['href']
            print(f"Scraping details for {dataset.text.strip()}...")
            dataset_details = scrape_dataset_details(dataset_link)
            data.append(dataset_details)


    # Loop through the pages using the pagination parameters
    skip = 0
    take = 10
    while True:
        page_url = f"https://archive.ics.uci.edu/datasets?skip={skip}&take={take}&sort=desc&orderBy=NumHits&search="
        print(f"Scraping page: {page_url}")
        initial_data_count = len(data)
        scrape_datasets(page_url)
        if len(
                data
        ) == initial_data_count: 
            break
        skip += take


    with open('uci_datasets.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


    print("Scraping complete. Data saved to 'uci_datasets.csv'.")


scrape_uci_datasets()

```

Once you run the script, it will run for a while until the terminal says “No dataset links found”, followed by “Scraping complete. Data saved to 'uci_datasets.csv'”, indicating that the scraped data has been saved in a CSV file.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXdRUvJJsu32oaxdattur__98CEF9GvqQMDTDQzpqS-NW3I2-haF5tfWH_mIBFwEhAqLhUhURVKCNFJE-b1bRzeZtz2oApWePqLZqWahKT0uhoXN0Ok7JJQnWN32dWQOHclZ2y9hg2MdqvoLDhToy-gCj9o?key=f_hrU3B_rjNJFpKZiiV3Pw)

To view the scraped data, open the 'uci_datasets.csv', you should be able to see the data organized by Dataset Name, Donated Date, Description, Characteristics, Subject Area, and so on.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXd1ZkPzSyPxZ3KsZklCPPcruSll4xUBxm3KiNdageDzHK-wbTxG7v8HLFpoJ-gMvIpdKPxzoshzRlmNjiPeVcbvse14gdGFHu7Wm89UgTACtImpToHOkqcU29S6s31CzC_T20h1bUO4w0D9sLFC_5Tmy3o?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Data organized by Dataset Name, Donated Date, Description, Characteristics, Subject Area, and so on._

You can have a better view of the data if you open the file via Excel.

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXfdmf621HGzQNHCdgxTJ6cvl2YEpuAq5hfvqpE9KrbZ8kDkGo6R3YIYpCFMmNoY8z29YEfcesZap9hpxiLc3fwHEyzLdo6dNQGNExRdam3t3taUebgKL_ocDFXyo2KhhMTpGDod2sUQI5miEUp_UCyNPZo?key=f_hrU3B_rjNJFpKZiiV3Pw)
_Data organized in Excel file_

By following the logic mentioned in this article, you can scrape many sites. All you need to do is start from the base URL, figure out how to navigate through the list, and go to the dedicated page for each list item. Then, identify suitable page elements like IDs and classes where you can isolate and extract the data you want. 

You also need to understand the logic behind pagination. Most often, pagination makes slight changes to the URL, which you can use to loop from one page to another. 

Finally, you can write the data to a CSV file, which is suitable for storing and as input for visualization.

## **Conclusion**

Using Python along with Requests and Beautiful Soup allows you to create fully functional web scrapers to extract data from websites. While this functionality can be highly advantageous for data-driven decision-making, it is important to keep ethical and legal considerations in mind.

Once you become familiar with the methods used in this script, you can explore techniques like proxy management and data persistence. You can also familiarize yourself with other libraries like Scrapy, Selenium, and Puppeteer to fulfill your data collection needs. 

Thank you for reading! I'm Jess, and I'm an expert at Hyperskill. You can check out my **Python** developer course on the platform.

