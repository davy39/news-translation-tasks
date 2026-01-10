---
title: AI in Google Sheets – How to Use GPT Copilot
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-06-12T22:10:01.000Z'
originalURL: https://freecodecamp.org/news/ai-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/ai-in-google-sheets-thumb.jpg
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'It seems to be the year of AI. And my favorite tool, Google Sheets, is
  not to be left out of the fun. 🎉


  Coefficient produced a Google sheets extension with the ability to use OpenAI''s
  GPT models from within a spreadsheet. It’s called GPT Copilot an...'
---

It seems to be the year of AI. And my favorite tool, Google Sheets, is not to be left out of the fun. 🎉

![Image](https://www.freecodecamp.org/news/content/images/2023/06/giphy.gif)

[Coefficient](https://coefficient.io/gpt-google-sheets) produced a Google sheets extension with the ability to use OpenAI's GPT models from within a spreadsheet. It’s called GPT Copilot and it’s available to try for free. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.00.44-PM.png)
_screenshot of Coefficient's GPT in Sheets page_

I have been putting off looking into this tool for quite some time, though I've been following Coefficient's Google Sheets work for a while now.

To be honest, I'd gotten a little tired of all the AI talk and was wary of yet another effort in that realm. Do I really need to use AI in spreadsheets? 

🤷Yes and no.

## Video Example

I made a quick video walking through a handful of the GPTx functions, and I'll detail all of them in the article below. If you have a sec, check out the 2.5 min video and give it a 👍.

%[https://youtu.be/HaKYyPLaOFA]

The extension is pretty cool.

AI is not some thing that is going to do all of my work for me. But it is a pretty powerful tool with which I can do work faster, more efficiently, and in some cases get some unique inspiration from.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/potential.gif)
_gif of ted lasso saying, smells like potential_

## GPT Copilot Functions

In the GPT Copilot extension on Google Sheets, we are given a list of several built-in `GPTX` functions we can now use directly in the sheet itself. 

[Here](https://docs.google.com/spreadsheets/d/1CaLdC22IS_9K42ycwkyYlnsCSGsEpyJtedPWXxn5poI/edit#rangeid=903106705) is a document with all the functions listed out, and we'll go through each below.

And [here's the spreadsheet](https://docs.google.com/spreadsheets/d/10suhdcRdi5NI_PCGO0VK1TXiLIGdy44T8R3zL9938So/edit?usp=sharing) I used for all my samples and the video. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.12.07-PM.png)

The first function, `=GPTX(prompt)` simply lets us generate text using Open AI's GPT model.

I used this to generate a subject line for an email below. This generic `GPTX` function can be used to query ChatAI's model for anything you can think of: 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-113.png)
_Screenshot of GPTX() function_

Then we get `**=GPTX_LIST(prompt)**` which lets us generate a list of values in the same way. 

This is similar to the first example, but the list of items will appear in separate cells so it's handy if you want...say, the top 10 video games by sales in Korea:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-114.png)
_Screenshot of GPTX_LIST() function_

`**=GPTX_EDIT(text,[task])**` was useful as I went through and created email body messages based on a prompt that I fed into the function. So it lets us perform a task or transformation on an input text.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.14.09-PM.png)
_screenshot of GPTX_EDIT function_

`**GPTX_MAP(search_keys, inputs)**` performs a fuzzy search, given a list of search keys in the list of input values, and then outputs the most similar search for each input value.

If we have a list of games and platform companies, it can map the company values to the correct game:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-124.png)
_Screenshot of GPTX_MAP()_

`**GPTX_FILL(text, [task])**` fills in missing information in the table based on example rows.

This will let you feed it some example data and have GPTX fill in the rest:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-115.png)
_Screenshot of GPTX_FILL_

`**GPTX_TABLE(prompt, [header_row])**` generates a table of values. This one was particularly cool because you can give it a real query to get data from, or have it fill out a table with dummy data.

Here we can pull in some population info on the top 5 cities in Tennessee: 😀

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-116.png)
_Screenshot of GPTX_TABLE()_

`**GPTX_FORMAT(text, language)**` converts input values into the specified format. 

`**GPTX_TAG(text, tags)**` does what it sounds like: it applies one or more tags matching a piece text.

If you have a list of movies, and a list of genres, you can tag them here. Interestingly:

1. GPT doesn't seem to have a sense of humor as it didn't classify Waterworld as a flop.
2. It also won't blindly fill in genres that are missing from the list (Goldeneye and Seven)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/flop.png)
_Screenshot of GPTX_TAG()_

Another cautionary tale, though...when I added crime to see if it would fill in Seven's blank, it actually came back with different answers on some of the others...and left off Casper and Jumanji this time. So, while nothing is really tagged incorrectly, it does have varying results. 

In this case, it does behave like a human, in a way. You'll get different people answering this type of tagging question in different ways too. 🤷‍♂️

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2.png)

`**GPTX_CLASSIFY(text, labels)**`, in the same way, classifies text given a set of labels or categories.

`**GPTX_EXTRACT(text, info_to_extract)**` extracts the desired information from the input text. So if you have an address in a cell, it can extract the city name from the address.

> Caution though; I encountered several instances while writing these GPTX functions where I got #ERROR!s and had to refresh the page, close it and reopen, or simply wait a while...

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-118.png)

`**GPTX_SUMMARIZE(text, language)**` summarizes the input text according to the given format.

I tried to be clever here. I pasted the first chapter of The Great Gatsby into a cell. Pretty quickly got a "too large" error 😂)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-119.png)
_screenshot of GPTX_Summarize error_

But! Reducing down to the first 726 words was sufficient to have it actually summarize the beginning of this awesome novel:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-121.png)
_Screenshot of GPTX_SUMMARIZE() summarizing the start of The Great Gatsby_

`**GPTX_TRANSLATE(text, language)**` translates the input text into the specified language.

This one's straightfoward and not incredibly useful for my spreadsheets...but nonetheless, it's pretty neat:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-122.png)
_Screenshot of GPTX_TRANSLATE()_

`**GPTX_CONVERT(text, format)**` converts the input text into the specified structured format.

`**GPTX_CODE(task, language)**`generates code in a specified language, which performs the specified task. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.21.54-PM.png)

`GPTX_CODE()` was really neat. I also see the most chances for problems here because novices will be tempted to blindly use code not knowing how or if it works.

This seems most beneficial as a helper for when I know how the code should work, but can prompt for the basic skeleton instead of needing to search for methods on my own.

## Limits to GPT Copilot

Are there limits to the number of prompts you can feed these functions? Yes. Of course there are. 😆

To stay free, you get 10,000 executions. Monthly plans start at 100,000 executions per month.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.33.46-PM.png)
_screenshot from the Coefficient GPT CopilotFAQ_

## What I Think

I walk through some real basic stuff that I could have generated on my own in the [example video](https://youtu.be/HaKYyPLaOFA) that I encourage you to watch. But I do see the potential for this to be a very helpful tool as the ecosystem matures.

Insofar as dummy data is concerned, it is really helpful to just generate stuff in a spreadsheet quickly.

And it works great to fill in the blanks where you previously might do a little bit more manual labor, extracting values, formatting things, classifying things, and so on.

In addition to these built-in functions, the Coefficient add-on also contains a pivot builder, a formula builder, and a chart builder tool.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.25.26-PM.png)
_screenshot of Coefficient's extension_

These allow you to feed a prompt into the extension based on the data in your spreadsheet, and it will generate either a pivot table, a formula, or a chart.

These are kind of crutches for doing some pretty basic operations in Google Sheets. But they do have an interesting utility and are pretty reliable when you give well-written prompts to them.

## Wrapping Up

🤔 AI tools can be a big time sink. It's pretty easy to spend more time getting mediocre results from them than it would have taken to do things manually.

But, that's part of the learning curve for any toolkit. Upfront investments can certainly pay off in the long run. I'll keep using these tools to hopefully make better spreadsheets more efficiently.

❓What do you think? Is this another example of over-engineering simple things? Or is it the next big thing in Google Sheets?

Come join the conversation on my YouTube channel: [https://www.youtube.com/@eamonncottrell?sub_confirmation=1](https://www.youtube.com/@eamonncottrell?sub_confirmation=1)

Or my LinkedIn: [https://www.linkedin.com/in/eamonncottrell/](https://www.linkedin.com/in/eamonncottrell/)

Have a great one! 👋

