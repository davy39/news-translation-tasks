---
title: Think you need a Dashboard? You should build a Notebook instead.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T21:46:25.000Z'
originalURL: https://freecodecamp.org/news/think-you-need-a-dashboard-you-should-build-a-notebook-instead-33104d913f95
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iOUCCgSxZ8pwih2L
tags:
- name: analytics
  slug: analytics
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mahdi Karabiben

  After first establishing themselves as a key component of the standard Business
  Intelligence model during the first years of the millennium, dashboards were rapidly
  adopted by most companies as the go-to tool to present data-driven...'
---

By Mahdi Karabiben

After first establishing themselves as a key component of the standard Business Intelligence model during the first years of the millennium, dashboards were rapidly adopted by most companies as the go-to tool to present data-driven insights and indicators.

When Hadoop was introduced afterwards in 2007, its launch was followed by a set of Big Data technologies that radically changed how things are done behind the curtains. They allowed parallelism on a previously unimaginable scale. These changes were, for a long period, limited to data storage and data processing. Changing the way the end users accessed data felt like an unnecessary step, because dashboards were still doing a fine job.

In a Big Data era that completely changed how companies process their data, dashboards managed to remain the _de facto_ standard for making sense of the mind-boggling amounts of data being produced on a daily basis. Most companies offering dashboarding solutions rapidly adapted their products to Big Data technologies. They also offered connectors that allowed dashboards to remain the undisputed go-to tool when it comes to understanding data.

But with continuous changes and improvements to the standard Big Data technologies happening at a staggering pace, maybe it’s time to update the _Big Data User Experience_?

### The problem with dashboards: you’re always one step behind

When they started being integrated into technology stacks at the turn of the century, dashboards answered to a clear and coherent need: presenting KPIs and data-driven insights that offer answers to established questions. They were the portal to the company’s data, and allowed people with multiple roles and needs to understand what the data has to say. In essence, dashboards were first introduced to democratize **data discovery**.

But at the turn of the century, data flows were very structured, the data didn’t have that much to say, and the range of questions to ask it was limited.

That no longer is the case. With the exponential growth of the data being produced daily, the value of this new black gold reaches new highs every day. The volumes of data available for exploitation in this Big Data era don’t just offer answers to a specific set of questions. They offer you questions you still haven’t thought about asking yet. This led to the rise of **data exploration**, with data scientists trying to extract as much value from data as possible.

Relying on dashboards to visualize and extract value from your data means that you have to use another technology (usually **notebooks**) to explore it and decide what gets to be accessible through your dashboards. Such a mechanism means that the dashboard comes always at a second phase of extracting value from data. In this era where the amounts of data available allow for an infinite number of possibilities when it comes to data exploration, no dashboard could be enough to extract all of the value your data offers.

Working with this two-step mechanism means that collaboration between different roles remains limited. This is because the data architectures become too complex due to the number of technologies used by the different data specialists.

This chain of people using different technologies for different needs means that in order to add certain insights to a dashboard, a data analyst needs to wait for a data scientist to work on the data via a notebook. In turn the data scientist may need to wait for a data engineer to offer the data in a certain structure through a script. And remember — throughout this whole time-consuming process, the value of the data keeps decreasing.

Multiple dashboard-providers have tried to integrate data exploration capabilities within their platforms, with Tableau notably offering [an impressive Spark connector](https://onlinehelp.tableau.com/current/pro/desktop/en-us/examples_sparksql.htm) that allows you to run Spark SQL jobs directly from your dashboard. Still, the capabilities remain limited and the interactivity is only partial, which leaves the end-user always one step behind.

Whether you’re using Kibana, Tableau, or Qlikview, your dashboard can offer valuable insights regarding your data. The problem with such technologies is that they were built with data discovery in mind. And because of that they neglect one key element made possible on a massive scale in this Big Data era: **data exploration**.

As data flows keep growing exponentially, dedicating the main portal to your data merely to insights means that you’re only reading the first page of a very interesting book.

### Notebooks, and how they take interactivity to a completely new level

As mentioned above, notebooks have been the standard tool for data exploration for the past few years. Since the release of [project Jupyter](https://jupyter.org/) in 2014, and through the set of functionalities it offered on top of what was already available via IPython, notebooks attracted data scientists as an ideal data exploration tool thanks mainly to one key concept: **interactivity**.

Thanks to kernels (within the Jupyter ecosystem) and interpreters (within Apache Zeppelin), notebooks let you explore your data through a multitude of Big Data processing technologies. They then offer immediate access to the data via built-in visualization modules and output mechanisms. Gathering both of these capabilities into the same tool is the key to using such tool for both data discovery and exploration.

Notebooks are not only a tool that allows for direct access to data, they do so while maintaining complete interactivity. They completely blur the line that separates data scientists and data analysts and allow people with these two roles to collaborate together seamlessly.

This works perfectly thanks to the powerful protocol that notebooks rely on and to their main building block, cells (paragraphs in Zeppelin). By offering multiple cell types (for code and text), notebooks allow for efficient collaboration.

To show their efficiency compared to dashboards, let’s go back to the scenario we talked about earlier. In a notebook-based architecture, when a data analyst needs certain insights within a notebook, the data engineer can add a code cell within which they manipulate the data through the adequate data processing technology. Then the data scientist uses this data in another code cell to extract the desired information and offer the output to the data analyst. This all happens without any of these three data specialists leaving the notebook.

In an era where Fast Data is the norm, extracting value from your data through a structured pipeline using different tools for each step is no longer a sustainable pattern. The data that comes through an unstructured real-time data flow may offer valuable insights when used for batch processes. But it offers even more value when it’s progressively analyzed via near-real-time processing and interactive dashboards (i.e. notebooks) that offer complete access to the raw data and sophisticated visualizations.

