---
title: How to Use Selenium and Python to Scrape Websites More Effectively
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-11T22:53:43.000Z'
originalURL: https://freecodecamp.org/news/improve-web-scraping-with-selenium
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/web-scraping-articl-image.jpg
tags:
- name: Python
  slug: python
- name: selenium
  slug: selenium
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Otávio Simões Silveira

  When you''re scraping data from the web with Python, Selenium will often come up
  as an helpful tool to use. It was originally designed for automated testing, but
  its scraping capabilities are impressive, too.

  This is because ...'
---

By Otávio Simões Silveira

When you're scraping data from the web with Python, Selenium will often come up as an helpful tool to use. It was originally designed for automated testing, but its scraping capabilities are impressive, too.

This is because Selenium can do things that other libraries or frameworks often can't when collecting data: accessing JavaScript-rendered content and interacting with the page in basically any way you want.

This article is about the second capability – interacting with the page however you want. It will cover three helpful topics to give you more options when you're interact with a website in order to access its content. 

And although this article focuses on web scraping, that’s only one use case for these tips as you can implement them for any tasks where Selenium is useful.

Before we start, an important disclaimer: before beginning to scrape any website, make sure to check if the website allows you to do so. Also, it's a good practice to configure your scraper in order not to overload the website's server as we don't intend to cause any harm. 

Scraping is fun and a great way to gather data, but it needs to be done in a correct legal, manner.

## How to Mark Check Boxes

The process of scraping data doesn't involve only scraping the data. Sometimes you need to navigate through the website to get to where the data is. And when going through the website, you may need to fill out some forms, click on one or two buttons, and mark a check box, for example.

Marking a check box may seem like a very simple action, but it can be a little tricky. That’s because you might think that all you need to do is to locate the element using its Xpath and then use the `click` method to click on it.

And, yes, depending on the website that may be the case – but it’s not a rule. For most websites, Selenium won’t recognize a checkbox as a clickable button. So when you try to click on it, an exception will be raised.

The workaround for this is to locate the element and use an ActionChains object to move the cursor to the check box and then click on it. This is the code to do that:

```python
check_box = driver.find_element_by_xpath('Xpath')

actions = webdriver.ActionChains(driver)
actions.move_to_element_with_offset(check_box, -5, 5).perform()
actions.click().perform()
```

The `move_to_element_with_offset` method will move the mouse by an offset of a specific element on the page, relative to its top-left corner. You need to inform the element and the distance you want the cursor to move away from the top-left corner.

The goal is to have the cursor around the middle of the check box. To find the appropriate distance for the move, execute the code with the `size` attribute of the element before running the complete code.

```python
check_box = driver.find_element_by_xpath('Xpath')
print(check_box.size)
```

The output should look like this:

`{'height': 10, 'width': 10}`

And then, after the cursor has been moved, you just need to perform a click and the check box will be marked.

## How to Handle Frames

You may have found yourself in a situation where you just cannot make Selenium find a particular element on a webpage. No matter how you try to do it – by using the Xpath, or the class name, or whatever – you keep getting errors. 

So you check over and over for errors in the code but everything seems to be just fine. So what’s wrong?

Actually, nothing is wrong. The data you want to collect or the element you want to interact with is just in another frame on the page. We use HTML frames to divide the page into sections that each load a different part of the content.

To fix the problem, you only need to switch to the correct frame before you try to interact with the page again. If you know the name of the frame, just do this:

```python
driver.switch_to.frame('mainIframe')
```

You can also use the index of the frame to make the switch:

```python
driver.switch_to.frame(0)
```

But if you don’t know the name of the frame or how many frames there are on the page, the solution is to find all the frames on the page and then print the name of each one of them. This is how it would work:

```
frames = driver.find_elements_by_tag_name('iframe')
for frame in frames:
   print(frame.get_attribute('name'))

```

To find out how many frames are on the page, just print the length of the `frames` object.

```python
print(len(frames))
```

And now you are free to interact with the page and collect the data you need.

## How to Switch Tabs

Another common situation you might face when navigating through a website to collect data is that a button automatically opens a new tag. When this happens, it’s important to know how to go from tab to tab in order to get the data you need.

Fortunately, handling tabs with Selenium is not a complex process. Actually, it’s somewhat similar to handling frames.

You can use a more rustic approach using two objects: one contains the current tab and another one contains all the tabs. Then you just have to iterate over the second one and the iterator is different from the current tab you just switch from.

```python
current_tab = driver.current_window_handle

all_tabs = driver.window_handles
for tab in all_tabs:
   if tab!= current_tab:
       driver.switch_to.window(tab)
```

But if you have more than two tabs and want to be able to access any one of them anytime you need, there's a more elegant approach – and you’ll only need to keep track of the order in which the tabs are opened.

For this approach, you don't need to know the current tab. This is because you can switch tabs just by selecting the corresponding index of the tab you want to move to in the object with all the tabs.

```python
driver.switch_to.window(all_tabs[i])
```

If you want to go through all the tabs at once and perform actions and collect data from each one of them, you can easily iterate over all the tabs, too.

```python
all_tabs = driver.window_handles
for tab in all_tabs:
   driver.switch_to.window(tab)
```

However, if you’re opening more tabs to scrape data and you have a lot of links to scrape, you should be aware that you're making considerably more requests to the website than usual. This is because for each link, you’re opening two or three new tabs. 

In this case, you’ll also want to insert some random pauses in your code in order not to overload the server. You'll also want to take advantage of a proxy provider, like [Infatica](https://infatica.io/) (a company that's committed to sharing information through articles like this one) to make sure your code will keep running as long as there are pages left to scrape. 

This also makes sure that you’re not getting blocked, and that you and your connection are protected.

## Conclusion

I hope these Selenium tips will help you use it and scrape more effectively. There's much more you can do, but I wanted to keep this relatively short.

If you’re interested in more content like this or if you have a question, a suggestion, or just want to be in touch, feel free to reach out. Maybe there’s a second part coming soon!

