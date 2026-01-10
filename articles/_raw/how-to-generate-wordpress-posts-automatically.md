---
title: How to Generate WordPress Posts Automatically with Python
subtitle: ''
author: Marco Venturi
co_authors: []
series: null
date: '2022-08-22T20:55:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-wordpress-posts-automatically
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/-.png
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: 'If you run a website, you are aware of the importance of content. It''s
  important for your web presence, to help you be recognized as a leader in your field,
  to improve your SEO ranking, to increase your audience, and more.

  WordPress is one of the mos...'
---

If you run a website, you are aware of the importance of content. It's important for your web presence, to help you be recognized as a leader in your field, to improve your SEO ranking, to increase your audience, and more.

WordPress is one of the most popular and widely-used tools to create blogs, e-commerce platforms, and websites.

In this article, I'll show you how to create content automatically and push it to your WordPress website with Python. 

This is how it works:

* We'll get content from our source (for example, another website we run)
* We'll translate it into our language
* We'll choose a featured image already available on our website and finally publish it to our WordPress instance as a post.

The script we're about to develop can be useful if you want to create content in another language in a quick way to expand your audience. 

Let's say you have a webzine with content written in English and you want Spanish-speaking users to start reading your posts. You can create a new blog and run your script to get your posts translated into Spanish and ready to read by your users.

## Let's Get Started 

This is the script we'll develop by the end of this article:

```python
import requests
import json
import random
from googletrans import Translator
from requests.auth import HTTPBasicAuth

def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
    response_API = requests.get(sourceURL)
    data = response_API.text
    parse_json = json.loads(data)
    get_article_title = parse_json['title']
    get_article_content = parse_json['body']
    image_list = ["1689","1594","1612"]

    translator = Translator()

    title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
    title_translation_text = title_translation.text 

    content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
    content_translation_text = content_translation.text 

    random_image_list = random.choice(image_list)
 
    WP_url = wpBaseURL + "/wp-json/wp/v2/posts"

    auth = HTTPBasicAuth(<USERNAME>, <PASSWORD>)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps({ 
        "status":postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
        "featured_media": random_image_list
    })

    response = requests.request(
    "POST",
    WP_url,
    data=payload,
    headers=headers,
    auth=auth
    )

    print(response)
    print(random_image_list)


post_creator("https://jsonplaceholder.typicode.com/posts/5", "<BASE_URL>", "la", "en", "publish")
```

We'll break it into single parts and see, step by step, what we need to do. 

Before that, we need to go to the dashboard of our WordPress website and create a new application password. We'll use it to build our basic authentication when pushing posts to our website. 

If you've never done it before, you can check WordPress official [documentation](https://make.wordpress.org/core/2020/11/05/application-passwords-integration-guide/) on how to do it. Once you'll create it, you'll see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/0-2.png)

Don't forget to save it, this is the only chance to get it!

## Time to Code

Let's start checking out our code from the libraries we need. We'll use the googletrans library to translate our content with Google translate APIs. So, from the command line, I move to my project directory and type:

```python
pip install googletrans
```

You could encounter this error when you run the script:

```cmd
AttributeError: 'NoneType' object has no attribute 'group'
```

If you see this message error, you should install this version:

```cmd
pip install googletrans==4.0.0-rc1

```

I found it on [this](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group) StackOverflow article. If you want to know more about it, just have a look!

## How to Get the Content Translated

Once we install googletrans, we define a new function and call it "post_creator":

```python
def post_creator(sourceURL, wpBaseURL, sourceLang, targetLang, postStatus):
```

We pass this function five arguments:

* `sourceURL`: the URL of the website you get content from
* `wpBaseURL`: the URL of your new website where you want to import translated content
* `sourceLang`: the original language of the content
* `targetLang`: the language you want your content to be translated into
* `postStatus`: the status of your WordPress post: for example "draft", "published", and so on.

Inside the function, we declare six variables. Let's see them.

We use the GET method to call an API to get the content we want to translate: 

```python
response_API = requests.get(sourceURL)
```

Then we store in the "data" variable the text of the request:

```python
data = response_API.text
```

We parse the JSON with the ".loads()" method to convert it into a Python dictionary:

```python
parse_json = json.loads(data)

```

Then we store the value of the JSON key "title":

```python
get_article_title = parse_json['title']

```

We do the same with the "body" key:

```python
get_article_content = parse_json['body']

```

Finally, we store in a variable a list where we have the IDs of the media we want to use as "featured image": 

```python
image_list = ["1689","1594","1612"]

```

After we created the above variables, we instantiate Translator():

```python
translator = Translator()
```

Now we can start translating content. We translate the title of the article we got from the previous API call and store it in the "title_translation" variable. We then get its text and store it in the "title_translation_text" variable:

```python
title_translation = translator.translate(get_article_title, src=sourceLang, dest=targetLang)
title_translation_text = title_translation.text 
```

We do the same with the content of the article:

```python
content_translation = translator.translate(get_article_content, src=sourceLang, dest=targetLang)
content_translation_text = content_translation.text 
```

We get a random image from the image IDs list we created before. Images must be already available in our WordPress instance. Then we pick one just by specifying its ID:

```python
random_image_list = random.choice(image_list)
```

## How to Create Our WordPress Blog Post

Now we set things up to push the content we have to our WordPress website. First, we store the URL we're calling to push the content in a variable: 

```python
WP_url = wpBaseUrl + "/wp-json/wp/v2/posts"

```

We store in a variable the credentials for our basic authentication: the username and the application password we created before. We use "HTTPBasicAuth" to handle our authentication:

```python
auth = HTTPBasicAuth(<USERNAME>, <PASSWORD>)
```

We store in a variable the headers we want to pass. We set the output type to JSON and indicate that the request body format is JSON:

```python
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
```

Time to define the payload. We use the dumps() function to convert the Python object we created into a JSON string and then we pass the data we need to create the blog post: 

```python
payload = json.dumps({ 
        "status":postStatus,
        "title": title_translation_text,
        "content": content_translation_text,
        "featured_media": random_image_list
    })
```

Then we use the request() method to make our API call:

```python
response = requests.request(
    "POST",
    WP_url,
    data=payload,
    headers=headers,
    auth=auth
    )
```

At the end of the function, we print the response of the POST call and the ID of the media we'll use as the featured image:

```python
print(response)
print(random_image_list)
```

Once we've completed our function, it's time to call it and pass the correct arguments:

```python
post_creator("https://jsonplaceholder.typicode.com/posts/5", <BASEURL>, "la", "en", "publish")
```

* `https://jsonplaceholder.typicode.com/posts/5`: the URL we call to get the content we want to translate
* `<BASEURL>`: the base URL of our WordPress website
* `la`: the language code of the content we get from our API call. In this case, it is "Lorem Ipsum" content, so we set it to Latin
* `en`: the language code we want to translate our content into. We set it to English.
* `publish`: the status of the WordPress post we are creating

If we run the script via the command line, we see this message:

```cmd
<Response [201]> 
1594
```

And if you visit the website, you can see the post:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/1-1.png)

Just to give you a complete overview, this is the JSON we got content from:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/2.png)

## Final Thoughts

In this article, we saw how to automate posts in a few lines of code with Python. It can be run as a batch or when necessary. 

Content is always a key point when you manage a website. I hope this article will help you translate content quickly and grow your audience even faster. [Here](https://github.com/mventuri/python-wordpress-blog-post) you can find the repo on GitHub. 

Enjoy and keep coding! :) 


