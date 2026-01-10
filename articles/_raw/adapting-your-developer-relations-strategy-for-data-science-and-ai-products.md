---
title: How to adapt your developer relations strategy for data science and AI products
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-20T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/adapting-your-developer-relations-strategy-for-data-science-and-ai-products
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0c4740569d1a4ca4aa1.jpg
tags:
- name: AI
  slug: ai
- name: Data Science
  slug: data-science
seo_title: null
seo_desc: 'By David Nugent

  The global market for artificial intelligence products is supposed to grow roughly
  10 times by 2025 to almost $120 billion, according to market research firm Tractica.
  Many companies are attempting to capture that market, including IB...'
---

By David Nugent

The global market for artificial intelligence products is supposed to grow roughly 10 times by 2025 to almost $120 billion, according to market research firm Tractica. Many companies are attempting to capture that market, including IBM with its Watson [suite of developer tools](https://www.ibm.com/watson/developer/?cm_mmc=OSocial_Blog-_-Developer_IBM+Developer-_-WW_WW-_-OInfluencer-Dev-DN-container-devrel&cm_mmca1=000037FD&cm_mmca2=10010797). 

I spoke to my colleague Upkar Lidder about how to adapt a developer-relations strategy to current and future generations of developer-facing AI products.

![Upkar speaking](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/speaker.jpg)

Upkar Lidder is a full-stack developer and data wrangler with a decade of development experience in a variety of roles. He speaks at various conferences and participates in local tech groups and meetups. Upkar went to graduate school in Canada and currently resides in the United States.

### Q: You’ve worked with developers working on all kinds of AI projects, from simple 101-style tutorials to customers implementing huge systems. How does AI development differ from more conventional programming?

There’s a lot of learning, trial, and experimentation with AI and machine learning. The goals for AI projects may be vague: “reduce the number of customer complaints,” for example.

By comparison, classical software development user requirements may  look like “give me a dialog box with a button on it” — specific and well-defined. Of course, there is a lot of user research and design that goes into the software spec to get to that point, and as a developer, you work to that spec. On the contrary, as a data scientist, you may only be pointed to an unstructured data set, then the real fun starts: You start exploring it! I love the data-wrangling aspect of AI development. You can get into a Jupyter Notebook and start exploring specific outliers, shapes of data, types of data, and see how the data looks through different visual representations.

Then you make decisions. What do I do with the missing values? How is that going to affect my projected outcome? Even in these first two stages, there are a lot of unknowns. In software development many programmers walk a well-worn path which their colleagues and predecessors have paved since decades. In data science, you have an exploratory period where you try to find a path to take. Once you’re done cleaning and transforming, you choose an appropriate modeling technique and proceed with your analysis. A lot of that exploration is brute force. XKCD has my favorite cartoon on data science.

![data science cartoon](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/cartoon.jpg)

Like I said, some of data science is just brute force. Even with helper libraries and frameworks, you have to sketch out an educated starting point yourself and let the library do much of the rest on its own. Afterward, you’ll analyze how the results compare with your other benchmark algorithms and repeat the procedure.

### Q: This raises the question: How do you explain your project and model to non-technical users?

It’s a great question: how well do you want to be able to explain your thought process and decisions to business users? Some models like decision trees are easy to explain, whereas something built with neural networks or ensemble models, your models can get more complicated and harder to explain. Compare this to traditional software development: except for some tricky bugs, problems of explanation like that just don’t happen.

Now with the more advanced systems like [AutoAI](https://www.ibm.com/cloud/watson-studio/autoai?cm_mmc=OSocial_Blog-_-Developer_IBM+Developer-_-WW_WW-_-OInfluencer-Dev-DN-ai-devrel-upkar&cm_mmca1=000037FD&cm_mmca2=10010797), you give the data to the system, and it will take care of more of the heavy lifting on your behalf. For example, I’m working with some data scientists on a project analyzing NPS scores for some internal departments. We’re building a system where, as a support call is going on, the system can identify red flags in the call that show it “going downhill” and alert a manager while the call is still in process. We have access to data points such as call length, customer tier, and sentiment analysis, so we can use this data to automatically flag issues before they explode. Interestingly, we tried running AutoAI on the data — the data scientists didn’t like it! The main issue is that it can be a bit of a “black box,” and the scientists wanted to be able to explain how they reached their conclusions.

In the annual data science survey, one of the biggest gaps in data science is skillsets. So, on the one hand, we need black box systems like this where you don’t have to have a Ph.D. in math to understand why the system works; it will do feature engineering, [Hyperparameter optimization](https://en.wikipedia.org/wiki/Hyperparameter_optimization) — at the same time, the data scientists are not fully trusting it.

![People listening](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/listening.jpg)

### Q: You’ve been working at IBM for a few years. What did you do before you got into AI, and how did you make the switch?

I joined through the support group at IBM, so I’d get calls from clients around the world with issues and try to help them out. I was Level 2-3, so the problems would be escalated to me. So the customers were already angry by the time they talked to me! In a lot of ways, I feel that the beginning role was similar to what I do now. I talk with developers and try to figure out how to help them, even though I approach that from an education perspective more than support. Then I was a Java developer, building products with Eclipse. From there I went to a client-facing technical role working on client projects, so very different from product development. From there I became a functional lead, which is essentially a project management role. I had a team of developers that I’d work with to scope solutions and ensure they were delivered on time. After two years of that, I moved into DevRel.

Before working in developer relations, I would enjoy mentoring coding school and bootcamp students on the side; so when this developer-relations job came up I thought, “Wow, it would be great to do that as a job and get paid for it!”

![IBM booth](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/ibmbooth.jpg)

### Q: You’ve previously advocated for products and technologies like APIs and serverless architecture. What new tactics have you developed to talk about AI and machine learning?

With AI/ML, you have to _do_ — less talking, more _doing_.  For other software development topics like serverless, you can have a longer lecture and then get into a demo. With AI/ML, there’s an emphasis on experimentation. You have to get your hands dirty or it won’t work. I love Jupyter Notebook because you can do something, see the causation, see the result, and only then think about why.

I feel like there’s more abstract theory, math, and intuition behind data science. You can always memorize a formula, but to be able to get an intuition about something, that is ideal. And that comes from experimentation. Through visualization and plotting, you can understand the math behind the different data science concepts. Contrast that with something more DevOps-oriented — it’s a different approach. So in data science and AI developer relations, you have to make sure the attendees are doing something and engaged. Otherwise you lose them very fast — because there’s math involved!

One of the things that’s worked for me is to put a lot of time into my workshops, explaining every step in great detail. In my slides, I’ll use arrows, annotated rectangles, and the like to ensure that the students are able to follow along easily and naturally. When I teach Jupyter Notebooks, I craft half-baked solutions, where I build out a solution that works to a certain point and then the next two cells would be questions: find the frequency of the data we just queried. You can do a demo, where you do and they watch, then you can do a follow-along, where you both do at the same time, and finally, you walk through an exercise method, where they do the work first. The last two are most useful for data science concepts.

![Speaking](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/speech.jpg)

### Q: Let’s talk more about hands-on workshops. We find ourselves doing more and more workshops at IBM. What best practices can you share?

The top five things that work for me in workshops:

* Prerequisites — Get workshop attendees to complete some prerequisites before the workshop. If you have special codes for attendees to use, distribute them ahead of time. When they check in at registration, the first thing you do is add the code to upgrade their account. A lot of time in workshops is wasted on setting up; the speaker spends the first 10 minutes saying “Hey, follow me.” Avoid this if possible by preparing beforehand. And of course, as much as you try, it’s impossible to get everybody set up before you start; you’ll have to cater to these users before you start your presentation.
* Step-by-step instructions — Even if the attendees have no issues following along, have a backup plan with slide numbers that they can go back to and follow. Who reads the book that comes with the vacuum cleaner? Nobody, but you may need to consult it later if you have issues.
* Have the final solution ready — If you’re using GitHub, have different branches for the different steps; if users are less technical or need to skip a section, they can check out that branch and still be able to keep up with the workshop. This type of content takes time to develop.
* Stretch goals — You’ll get an audience of all backgrounds and experiences, and it’s important to cater to all of them (to the extent possible). You’ll either lose the beginners — it’s important not to lose them because it may be their first time doing something — but you don’t want to lose the intermediate and advanced users either, and this is where stretch goals are important.
* Resources — Tell your students where to go and what to do next, outside of the logistics of the workshops. Make sure you have assistants during the sessions as a resource also.

### Q: Who would you like to call out in the developer-relations world for doing a good job or stretching the boundaries of developer relations?

Fortunately, the DevRel world is filled with people I look up to! Some of the names that come to mind are:

* Josh Gordon, Google, @random_forests
* Paige Bailey, Google, @DynamicWebPaige
* James Thomas, IBM, @thomasj
* Gabriela de Queiroz, IBM, @gdequeiroz
* Vijay Bommireddipalli, IBM, @vjbytes
* Renee M. P. Teate, Heliocampus, @BecomingDataSci

![game](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/game.jpg)

## Next steps

* Follow [Upkar on Twitter](https://twitter.com/lidderupk)
* Listen to one of Upkar’s talks at the [IBM Developer SF meetup](https://www.meetup.com/IBM-Developer-SF-Bay-Area-Meetup/)

