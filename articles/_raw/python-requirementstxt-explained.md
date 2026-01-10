---
title: Python Requirements.txt – How to Create and Pip Install Requirements.txt in
  Python
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2023-09-11T14:17:18.000Z'
originalURL: https://freecodecamp.org/news/python-requirementstxt-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/pexels-christina-morillo-1181671--1-.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'There are many Python packages we use to solve our coding problems daily.
  Take, for instance, the library "Beautiful Soup," – it doesn''t come with Python
  by default and needs to be installed separately.

  Many projects rely on libraries and other depen...'
---

There are many Python packages we use to solve our coding problems daily. Take, for instance, the library "Beautiful Soup," – it doesn't come with Python by default and needs to be installed separately.

Many projects rely on libraries and other dependencies, and installing each one can be tedious and time-consuming.

This is where a ‘requirements.txt’ file comes into play. requirements.txt is a file that contains a list of packages or libraries needed to work on a project that can all be installed with the file. It provides a consistent environment and makes collaboration easier.

## Format of a requirements.txt File

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-219.png align="left")

*Diagram showing a box containing requirements.txt and another box below it containing the text "package\_name == version"*

The above image shows a sample of a created requirements.txt file, containing a list of packages and versions of the installation.

## Key Terms

I've mentioned a few terms so far that you may not know. Here's what they mean, along with some other important terms you'll come across when working with requirements.txt:

* **Dependencies** are software components that a program needs to run correctly. They can be libraries, frameworks, or other programs.
    
* **Packages** are a way to group together related dependencies. They make it easier to install and manage dependencies.
    
* **Virtual Environments** is a directory that contains a copy of the Python interpreter and all of the packages that are required for a particular project.
    
* **Pip:** This is a package manager for Python. You can use Pip to install, uninstall, and manage Python packages.
    

## How to Create a requirements.txt File

To create a requirements file, you must set up your virtual environment. If you use Pycharm, there's a virtual environment already setup (.venv). But with Visual Studio code, you have to create [the virtual environment](https://code.visualstudio.com/docs/python/environments) yourself.

You can use your terminal or command prompt to create your requirements file. These are the steps to follow when creating the file:

First, open your terminal or command prompt. Then check to see if the file path shown is your working directory. Use the following command to do that:

```python
$ cd folder-name #cd - change directory
```

In the command above, replace ‘folder-name’ with the directory name you want to access.

![Image](https://lh4.googleusercontent.com/vgAz2y8K2iS5wT805qSCN4GhJSv4CDu_eY1_lD_xjetaHhqkNIIvZfCmlVBmBfYYw3PrEYlkq2lasDFsc3YhMtqxZwP4AVn3P70820VeUPdVZxVXU8Cw_UNqPhKnKn3fqpy1sgC5UY4urtfqj4VlYcg align="left")

*Diagram showing set project directory on command line*

Next, run this command:

```python
$ pip freeze > requirements.txt
```

And you'll see that the requirements file gets added

**Here's the output:**

![Image](https://www.freecodecamp.org/news/content/images/2023/09/requirementfile.png align="left")

*Diagram showing the newly created requirements file*

And here's your newly created requirements.txt file:

![Image](https://lh5.googleusercontent.com/1NEE23GJuy_i0qdANdi6twSQGnjfHrjVZ6LuUlENe57kqsMoUve3W0WcmxZLfY9JW04GrYZghVWFtY4_LnVU-isHVxv0ySpMCDQ5sYwhw2BhlQjCLbj2oa_v_nMIUgar2xayjkPRj6ogUARpZEYtKiA align="left")

*Diagram showing lists of packages in requirements file*

The image above shows the dependencies you can work with along with their versions.

## How to Work with a requirements.txt File

Now that we have the requirements file, you can see that it consists of a long list of different packages.

To work with the packages, you have to install them. You can do this by using the command prompt or terminal.

Type this command:

```python
pip install -r requirements.txt
```

It will look like this:

![Image](https://lh3.googleusercontent.com/7FDCFqn38aY2GFcoqtrKyy4Oyu_8cAPdJkOxbUIdZTfSalvufWIrbEehT61tgJxuhqiA0nINSfkyHcbE-H-H-hc77rY1zTkMQhyRijtWBOEqcaWZL7fnyNxRDO1hmKcagc9sYI4qijgj6Ut2lVY-zto align="left")

*Image showing installation of packages present in requirements.txt file*

Now that all the dependencies are installed, you can work with requirements.txt.

### Example of using requirements.txt

In this example, we will be working with two libraries, `beautifulsoup4` and `requests`, to return some information from a site.

![Image](https://lh6.googleusercontent.com/M5xLixBqsvL-vtUPFwEZq7NzB-jJDSpycapgv22OxtBKRFa9ysE0kIIPSG0mjltzfknNMdtlPYC8xDWwVnNyGiURQxHFJCrMI_Axexn7dKMRfVN4qUHLt0TEojj_pbLMW-cz_9wlrVw6VOOr8MaD-uQ align="left")

*Diagram showing the working libraries for this example in the requirements file*

In the image above, we see that the two libraries are present in the requirements.txt file and their version. Now we can work with the libraries because we installed them previously.

* Import the library BeautifulSoup from the package name bs4 (beautifulsoup4) and also import the library requests.
    

```python
from bs4 import BeautifulSoup
import requests
```

* To fetch information from the website URL, we use the `.get()` method to tap into the requests library.
    

```python
web_data = requests.get("https://www.lithuania.travel/en/category/what-is-lithuania", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
```

* Now that we have access to the the URL, the Beautiful Soup library accepts the `web_data` and returns all HTML contents present in it.
    

```python
soup = BeautifulSoup(web_data.content, features="html.parser")
```

* The final result I chose to return is elements with the
    
    tag in the first position \[0\].
    

```python
news_info = soup.findAll("p")[0]
print(news_info.text
```

Bringing it all together:

```python
from bs4 import BeautifulSoup
import requests
web_data = requests.get("https://www.lithuania.travel/en/category/what-is-lithuania", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
soup = BeautifulSoup(web_data.content, features="html.parser")
news_info = soup.findAll("p")[0]
print(news_info.text)
```

And here's the output:

![Image](https://lh4.googleusercontent.com/4H_qTUMuvWXNGMKpGrxHfVY6WaEntz51xZ936GwYWY6JRXILVPyd06spEt6emH0XKajK3Ov0qLixzgrqtEC5cIr-81UxyB61fTPPNhGcDc5eEhVoateHzmpAnvowdtbkqJgdz7IlpZ2aGtv9OWLCUCA align="left")

*Diagram showing code and result*

## Benefits of Using a requirements.txt File

* Managing dependencies: By listing the dependencies of your project in a requirements.txt file, you can easily see what packages are required and what versions they need to be.
    
* Sharing your project with others: If you share your project with others, you can include the requirements.txt file so that they can easily install the required packages. This can save them time and frustration and can help to ensure that everyone is using the same versions of the packages.
    

## Conclusion

In the article, we learned how to create a requirements.txt file and outlined the benefits of using it.

You should also try it out and work on a few projects with it. If you have any questions, you can reach out to me on [Twitter](https://twitter.com/HeritageAlabi1) 💙.
