---
title: How I used Python to help me chose an organisation for Google Summer of Code
  ‘19
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T16:59:38.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-python-to-help-me-chose-an-organisation-for-google-summer-of-code-19-75078de13194
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ucoUbiOID-texxFdJ8v2jw.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: gsoc
  slug: gsoc
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Vaibhav Gupta

  In this tutorial, I’ll be using python to scrape data from the Google Summer of
  Code (GSoC) archive about the participating organizations from the year 2009.

  My Motivation Behind This Project

  While I was scrolling through the huge li...'
---

By Vaibhav Gupta

In this tutorial, I’ll be using python to scrape data from the Google Summer of Code (GSoC) archive about the participating organizations from the year 2009.

### My Motivation Behind This Project

While I was scrolling through the huge list of organisations that participated in GSoC’18, I realised that exploring an organisation is a repetitive task - choose one, explore its projects, check that if it has participated in previous years or not. But, there are 200+ organizations, and going through them all would take a whole lot of time. So, being a lazy person, I decided to use python to ease my work

### Requirements

* _Python (I’ll be using python3.6, because f-strings are awesome ?)_
* _Pipenv (for virtual environment)_
* _requests (for fetching the web page)_
* _Beautiful Soup 4 (for extracting data from the web pages)_

### Building Our Script

These are the web pages which we are going to scrape:

1. For the years 2009–2015: [Link](https://www.google-melange.com/archive/gsoc)
2. For the years 2015–2018: [Link](https://summerofcode.withgoogle.com/archive/)

### Coding Part

![Image](https://cdn-media-1.freecodecamp.org/images/1*u5vEWeGuTXMWZiQQz8PbqQ.gif)
_[GIF from Giphy](https://giphy.com/gifs/nascar-owen-wilson-daytona-500-xTiN0GMUaOI726QYZa" rel="noopener" target="_blank" title=")_

#### Step 1: Setting up the virtual environment and installing the dependencies

_virtualenv_ can be used to create a virtual environment, but I would recommend using _Pipenv_ because it minimizes the work and supports _Pipfile_ and _Pipfile.lock_.

Make a new folder and enter the following series of commands in the terminal:

```
pip install pipenv
```

Then create a virtual environment and install all the dependencies with just a single command (Pipenv rocks ?):

```
pipenv install requests beautifulsoup4 --three
```

The above command will perform the following tasks:

* Create a virtual environment (for python3).
* Install _requests_ and b_eautifulsoup4._
* Create `Pipfile` and `Pipfile.lock` in the same folder.

Now, activate the virtual environment:

```
pipenv shell
```

Notice the name of the folder before `$` upon activation like this:

```
(gsoc19) $
```

#### Step 2: Scraping data for the years 2009–2015

Open any code editor and make a new python file (I will name it `2009–2015.py`). The webpage contains the links for the list of organizations of each year. First, write a utility function in a separate file `utils.py` which will GET any webpage for us and will raise an `Exception` if there’s a connection error.

Now, get the link of the web page which contains the list of organizations for each year.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pyKlRbBI5wfHuxFmSxoWjQ.png)
_Webpage preview_

For that, create a function `get_year_with_link`. Before writing the function, we need to inspect this webpage a little. Right-click on any year and click on _Inspect_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4qOIYUKISEcOIPcshCZ8KQ.png)

Note that there’s a `<`ul> tag, and inside it, ther`e ar`e <li> tags, each of which `conta`ins a <span&g`t; tag with class mdl-list__it`em-primary-content, inside of which is our link and year. Also, notice that this pattern is the same for each year. We want to grab that data.

The tasks performed by this function are in this order:

1. Get the `MAIN_PAGE`, raise an exception if there’s a connection error.
2. If the response code is `200 OK`, parse the fetched webpage with BeautifulSoup. And if the response code is something else, exit the program.
3. Find all the `<`li> tags with `class mdl-list__item mdl-list__item — on`e-line and store the returned li`st in ye`ars_li.
4. Initialize an empty `years_dict` dictionary.
5. Start iterating over the `years_li` list.
6. Get the year text (2009, 2010, 2011,…), remove all `\n`, and store it in the `year`.
7. Get the relative link of each year (/archive/gsoc/2015, /archive/gsoc/2016,…) and store it in the `relative_link`.
8. Convert the `relative_link` into the full link by combining it with the `HOME_PAGE` link and store it in `full_link`.
9. Add this data to the `year_dict` dictionary with the year as key and `full_link` as its value.
10. Repeat this for all years.

This will give us a dictionary with years as keys and their links as values in this format:

```
{  ...  '2009': 'https://www.google-melange.com/archive/gsoc/2009',  '2010': 'https://www.google-melange.com/archive/gsoc/2010',  ...}
```

Now, we want to visit these links and get the name of every organization with their links from these pages. Right-click on any org name and click on _Inspect_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ISaEmvazH3dr8Knfe3MtqA.png)

Note that there’s a `<`ul> tag with `class md`l-list, whic`h ha`s <li> tags `with class mdl-list__item mdl-list__ite`m — one-line. Inside of each `th`ere’s an <a> tag which has the link and the organization’s name. We want to grab that. For that, let’s create `another function get_organizatio`ns_list_with_links, which takes the links of web pages which contains the organizations' list for each year (wh`ich we scraped in` get_year_with_link).

The tasks performed by this function are in this order:

1. Get the org list page, ([https://www.google-melange.com/archive/gsoc/2015](https://www.google-melange.com/archive/gsoc/2015), [https://www.google-melange.com/archive/gsoc/201](https://www.google-melange.com/archive/gsoc/2015)6, ….), raise an exception if there’s a connection error.
2. If the response code is `200 OK`, parse the fetched webpage with BeautifulSoup. And if the response code is something else, exit the program.
3. Find all the `<`li> tags with `class mdl-list__item mdl-list__item — on`e-line and store the returned li`st in o`rgs_li.
4. Initialize an empty `orgs_dict` dictionary.
5. Start iterating over the `orgs_li` list.
6. Get the org name, remove all `\n`, and store it in the `org_name` .
7. Get the relative link of each org (/archive/gsoc/2015/orgs/n52, /archive/gsoc/2015/orgs/beagleboard,…) and store it in the `relative_link`.
8. Convert the `relative_link` into the full link by combining it with the `HOME_PAGE` link and store it in `full_link`.
9. Add this data to the `orgs_dict` with the `org_name` as key and `full_link` as its value.
10. Repeat this for all the organizations for a particular year.

This will give us a dictionary with organizations’ names as keys and their links as values, like this:

```
{  ...  'ASCEND': 'https://www.google-melange.com/archive/gsoc/2015/orgs/ascend',
```

```
'Apache Software Foundation': 'https://www.google-melange.com/archive/gsoc/2015/orgs/apache',  ...}
```

Moving ahead, we want to visit these links and get the title, description, and link of each project of each org for each year (?). Right-click on any project’s title and click on I_nspect._

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sb8nG8HeNSqrwUVG5BTiAQ.png)

Again, the same pattern. There’s a `<`ul> tag with `class md`l-list which contain`s th`e <li> tags `with class mdl-list__item mdl-list__ite`m — two-line, inside of which `there`’s an <span> `whi`ch contains an <a> tag containing our project’s `name.` Also, there’s a`n <span> tag with` class mdl-list__item-sub-title containing the project’s description`. For that, create a` function get_org_projects_info to get this task done.

The tasks performed by this function are in this order:

1. Get the org’s description page, ([https://www.google-melange.com/archive/gsoc/2015/orgs/ascend](https://www.google-melange.com/archive/gsoc/2015/orgs/ascend), [https://www.google-melange.com/archive/gsoc/2015/orgs/apache](https://www.google-melange.com/archive/gsoc/2015/orgs/apache), ….), raise an exception if there’s a connection error.
2. If the response code is `200 OK`, parse the fetched webpage with BeautifulSoup. And if the response code is something else, exit the program.
3. Find all the `<`li> tags with class equ`al to mdl-list__item mdl-list__item — tw`o-line and store the returned li`st in proje`cts_li.
4. Initialize an empty `projects_info` list.
5. Start iterating over the `projects_li` list.
6. Initialize an empty dictionary `proj_info` in each loop.
7. Get the project’s title, remove all `\n`, and store it in the `proj_title` .
8. Get the relative link of each project ([https://www.google-melange.com/archive/gsoc/2015/orgs/apache/projects/djkevincr.html](https://www.google-melange.com/archive/gsoc/2015/orgs/apache/projects/djkevincr.html), ….) and store it in the `proj_relative_link`.
9. Convert the `proj_relative_link` into the full link by combining it with the `HOME_PAGE` link and store it in `proj_full_link`.
10. Store the project’s title, description and link in the `proj_info` dictionary and append this dictionary to the `projects_info` list.

This will give us a list containing dictionaries with the project’s data.

```
[  ...  {    'title': 'Project Title 1',    'description': 'Project Description 1',    'link': 'http://project-1-link.com/',  },  {    'title': 'Project Title 2',    'description': 'Project Description 2',    'link': 'http://project-2-link.com/',  }  ...]
```

#### Step 3: Implementing the main function

Let’s see the code first:

The tasks performed by this function are in this order:

1. We want to have a `final_dict` dictionary so that we can save it as `.json` file.
2. Then, we call our function `get_year_with_link()`, which will return a dictionary with years as keys and links to the list of organizations as values and store it in `year_with_link`.
3. We iterate over the dictionary `year_with_link`.
4. For each year, we call the function `get_organizations_list_with_links()` with the link for it as the parameter, which will return a dictionary with organizations’ name as keys and links to the webpage containing information about them as values. We store the returning value in `final_dict`, with `year` as keys.
5. Then we iterate over each org for each year.
6. For each org, we call the function `get_org_projects_info()` with the link for the org as parameter, which will return a list of dictionaries containing each projects’ information.
7. We store that data in the `final_dict`.
8. After the loop is over, we will have a `final_dict` dictionary as follows:

```
{    "2009": {        "Org 1": [            {                "title": "Project - 1",                "description": "Project-1-Description",                "link": "http://project-1-link.com/"            },            {                "title": "Project - 2",                "description": "Project-2-Description",                "link": "http://project-2-link.com/"            }        ],        "Org 2": [            {                "title": "Project - 1",                "description": "Project-1-Description",                "link": "http://project-1-link.com/"            },            {                "title": "Project - 2",                "description": "Project-2-Description",                "link": "http://project-2-link.com/"            }        ]    },    "2010": {        ...    }}
```

9. Then we will save it as a `json` file with `json.dumps` .? ?

#### Next Steps

Data for the years 2016–2018 can be scraped in a similar manner. And then python (or any suitable language) can be used to analyze the data. Or, a web app can be made. In fact, I have already made my version of a webapp using _Django_, _Django REST Framework_ and _ReactJS_. **Here is the link for the same:** [https://gsoc-data-analyzer.netlify.com/](https://gsoc-data-analyzer.netlify.com/)

> All the code for this tutorial is available on my [github](https://github.com/dojutsu-user/GSoC-Data-Analyser).

### Improvements

The running time of the script can be improved by using Multithreading. Currently, it fetches one link at one time, it can be made to fetch multiple links simultaneously.

### About Me

Hi there.

I am **Vaibhav Gupta**, an undergrad student at **Indian Institute of Information Technology, Lucknow**. I love Python and JS.

See my [portfolio](https://dojutsu-user.github.io/) or find me on [Facebook](https://www.facebook.com/vaib79), [LinkedIn](https://www.linkedin.com/in/vaibhavgupta79/) or [Github](https://github.com/dojutsu-user).

