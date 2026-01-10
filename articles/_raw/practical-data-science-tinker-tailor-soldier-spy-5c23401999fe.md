---
title: 'Practical data science: tinker, tailor, soldier, spy'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T20:39:33.000Z'
originalURL: https://freecodecamp.org/news/practical-data-science-tinker-tailor-soldier-spy-5c23401999fe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UITRP8PyvgZFeUdu.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: statistics
  slug: statistics
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Michelle Jones

  I came to data science and statistics as a failure. After finishing my master’s
  degree in psychology I applied for about 30 psychology-related jobs without success.
  I didn’t even make it to the interview stage. I then saw a job adve...'
---

By Michelle Jones

I came to data science and statistics as a failure. After finishing my master’s degree in psychology I applied for about 30 psychology-related jobs without success. I didn’t even make it to the interview stage. I then saw a job advertisement for a research officer, and that started a 21-year career as an applied statistician in government. Along the way, I completed a postgraduate qualification in statistics.

**My coding history**

My first code was in SPSS PC version 5.0 for my master’s thesis. Back in 1995, when I was writing my thesis, user interfaces for statistical software were very simple. I used the menu system to create the first set of code I needed. Next, I copy-pasted that code for the next lot of analyzes on other variables, only changing the parts relating to the variable names.

![Image](https://cdn-media-1.freecodecamp.org/images/g8klZsrmqlbBjDEAGQPpzpfl6WiNVNO2estK)
_At least it wasn’t punch cards. [Image credit](https://en.wikipedia.org/wiki/Fortran#/media/File:FortranCardPROJ039.agr.jpg" rel="noopener" target="_blank" title=")._

Working with the code directly gave me an understanding of how code worked: commands, command options, and end-of-line markers. It made me think hard about which options I wanted in the analysis because I typed them in. This is the way I was introduced to coding. It was also faster than using the menu system.

At roughly the same time I had a gentle introduction to SAS, version 6, to help a professor with his data analysis. The code had been written, and I was only modifying it to update the analysis. This version of SAS only had a program editor, and I read many hard-copy SAS user guides. This was my introduction to coding without a menu system, and I made many mistakes starting out. My special skill was failing to close quote marks for strings.

From here, I spent the next 21 years using statistical software in various roles across government. I’ve used SPSS, SAS, R, and Stata. I’ve learned VBA, which I have mainly used for Excel, and also for Access. For my Ph.D., which is my current focus, I’m using R, VBA, Java, and Latex.

**Tinker**

The main role of a data scientist is to tinker with things. About 90% of my time has been spent in transforming data into a suitable format to analyze. Sometimes this is a simple but time-consuming task, for example matching data between multiple data warehouse extracts because a fourth normal form is not useful for data analysis. Sometimes the transformations can be simple and quick. One example is changing data from wide format to long format, or vice versa, due to data structure assumptions in the software.

More complicated tinkering includes the recoding of detailed data to a less detailed format that is useful to analysis. For example, there are many different ways that people answer “Other” response options in surveys, but these all need to be coded for analysis.

![Image](https://cdn-media-1.freecodecamp.org/images/De8REfoHLkzHG7MMwwtj9dyBs-xOc75An1O0)
_Sometimes it’s important to compare apples and oranges, and sometimes we just want to know about fruit. [Image credit](https://www.flickr.com/photos/microassist/7268711202" rel="noopener" target="_blank" title=")._

**Tailor**

The largest influence on how you will code in an organization is the culture. The culture controls what software is used, what software can be introduced, and how your code will interact with other staff. Sometimes your co-workers will want reports. Sometimes your co-workers are subject matter experts and will help you recode. Sometimes you need to produce a coding solution for co-workers to use. You may be one of many staff who uses software to do analysis.

You must tailor your solutions to meet these needs. Analyzing data for reports is your standard data scientist task, and can be done with any statistical software. You are the only person using the software, and the coding complications are only visible to you. Your restriction is the software available to use.

Working with co-workers to tailor data is also easy to do. One example is recoding open-ended responses into aggregate categories for analysis. I tend to use Excel for this, as most organizations have this software and all staff can access it, but any software that can handle rows of data is useful. After discussing the problem and solution with the co-workers, I dump the data into a single column in Excel, with a title row, and pass it over.

Sometimes the need to tailor data is not obvious until a first analysis is done. One variable may be collected using a relatively small number of subcategories. For example, relationship status, and you find that the results for one subcategory will be within the margin of error. You may wish to recode your data so that this subcategory is merged with another, logical, subcategory. This new, combined, subcategory will be renamed to something more suitable, reflecting the new content.

Tailoring code for colleagues to use can be easy. If your co-workers use the same statistical software, providing code for that software with comments and instructions may be all that is required. Frequently staff doesn’t have statistical software and just require a solution in software that they use. That software is likely to be Excel. Your task can range from checking formulas to providing a VBA macro in a macro-enabled Excel workbook.

**Soldier**

Most staff do not understand what you do. They see what you produce, but they have no knowledge and no interest in how you do it. As I said earlier, about 90% of your role is grunt-work, as data rarely arrive in a form suitable for analysis. If it does, another data scientist has done the grunt-work for you.

Other grunt-work is trying to get code to work, and perhaps implementing a different solution. For example, I once made the mistake of trying to use a for-next loop in R on a couple of million records. This is before I discovered that R uses vectorization, which made the solution a one-liner.

![Image](https://cdn-media-1.freecodecamp.org/images/AYhLKyuSxS27hish2bD4UhlqPhYg-wEF7b3C)
_The data fairy who actually does all of the hard work for me. [Image credit](https://pixabay.com/en/angel-feathers-female-magic-wand-1298818/" rel="noopener" target="_blank" title=")._

**Spy**

Make sure you know what your co-worker client wants before you start anything, especially anything that will take a lot of time. People can be non-specific, for example simply saying they need a report.

You use the tricks of a spy. How will the report be used? Do they need detailed analyzes or just high-level ones? For example, do you analyze by sex and age separately, but not by sex and age combined? Do people want a breakdown of the data? Use a table. Do people want a broad-brush picture? Use a graph. If the report is long, what should each chapter focus on? What analyzes are best suited to the report? What types of conclusions does the co-worker want to be emphasized?

**Tips**

Save interim datasets, don’t overwrite them. If I’m reading in from another file type, for example, .csv, I always save the newly imported dataset. I do my data manipulations on that dataset but save to different dataset. This way, when manipulations go wrong (and they will), you don’t need to bring the data in from scratch again. If something is weird in the analysis results, for example, there is a category that is blank, you can see if the problem is with the original data or something you did.

Remember to comment your code, and code for clarity and not always efficiency. Many times I have had to go back to code written 6 months, 1 year, 2 years before and work out what I did and why I did it that way.

When dealing with many lines of code, I use comment heading blocks to section code. This is useful when you only need to run part of the code again, and you are trying to find the code you need to re-run.

When working with large amounts of code that are used to write chapters in a report, I separate each chapter’s analyzes into different code files. Each code file has the relevant chapter number in the filename.

Assume that no one will peer review your work. Before analysis, check the data to make sure it is reasonable. I use frequency tables for this. These are a quick way to see if there are unexpected categories or categories that contain too little data to accurately report on.

**Finally**

As a data scientist, you are the software expert. You may advise on what software should be used, in light of organizational needs and funds. You may need to do, or help with, formal staff training. You are likely to be the one phoned and emailed when people have problems using the software. You will have a lot of interaction with the ICT department.

**Some examples of my work**

Chapter four of [this report](http://www.police.govt.nz/about-us/publication/pursuits-the-case-for-change) on police pursuits. I used SAS.

Working paper on the [gender pay gap](http://www.ssc.govt.nz/wp15) in the New Zealand public service, one of my most cited publications. The data were analyzed using SPSS.

My only sole-author [published article](http://onlinelibrary.wiley.com/doi/10.1111/nbu.12075/abstract) (behind paywall), and that used other people’s data. I only used Excel.

A published article (not behind paywall) where I had [fun with graphs](https://www.sciencedirect.com/science/article/pii/S0273230016302276?via%3Dihub#fig1), these were done in R. I sketched these out on paper before coding them.

This [study and report](http://www.foodstandards.gov.au/publications/Pages/consumerlabelsurvey2015.aspx) took over 2 years. Most of the analysis was performed in Stata, supplemented by R for the decision tree analyzes. The graphs were produced in Excel, using results from Stata.

