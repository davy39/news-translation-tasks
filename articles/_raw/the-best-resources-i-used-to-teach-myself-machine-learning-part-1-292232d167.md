---
title: The Best Resources I Used to Teach Myself Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-12T19:39:11.000Z'
originalURL: https://freecodecamp.org/news/the-best-resources-i-used-to-teach-myself-machine-learning-part-1-292232d167
coverImage: https://cdn-media-1.freecodecamp.org/images/1*92h6Lg1Bu1F9QqoVNrkLdQ.jpeg
tags:
- name: AI
  slug: ai
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Gwendolyn Faraday


  The field of machine learning is becoming more and more mainstream every year. With
  this growth come many libraries and tools to abstract away some of the most difficult
  concepts to implement for people starting out.

  Most people...'
---

By Gwendolyn Faraday

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-57.png)

The field of machine learning is becoming more and more mainstream every year. With this growth come many libraries and tools to abstract away some of the most difficult concepts to implement for people starting out.

Most people will say you need a higher level degree in ML to work in the industry. If you love working with data and practical math, then I would say this is not true. I did not graduate college with a Machine Learning or data degree yet I am working with ML right now at a startup. I want to share what I used to learn and how I got here in hopes that it will help someone else.

### Getting Started

I knew Python already when I started, but, if you don’t, I recommend learning basic and intermediate Python first. The language is pretty easy to learn compared to others. Python is also home to the largest data science/ML community so there are tons of tools to help as you learn.

[Learn Python: freeCodeCamp Python Crash Course](https://www.youtube.com/watch?v=rfscVS0vtbw)

With that out of the way, the first thing you should do is download “The Machine Learning Podcast” by OCDevel ([overcast.fm](https://overcast.fm/itunes1204521130/machine-learning-guide), [iTunes](https://itunes.apple.com/us/podcast/machine-learning-guide/id1204521130)) into your favorite podcast app. Listen to the first 10–15 episodes. They are very good at giving an overview of the machine learning ecosystem and there are also recommended resources which are linked on the [OCDevel site](http://ocdevel.com/mlg).

### Tooling

Anaconda & Jupyter Notebook — These are a must for ML & data science. Follow the [instructions here](https://jupyter.org/install) to install and set them up.

[Visual Studio Code](https://code.visualstudio.com/) with [Python Plugin](https://code.visualstudio.com/docs/languages/python) — I never thought I would be recommending a Microsoft product, but I am honestly impressed with their open source commitment lately. This is now my favorite code editor, even for doing some things in Python — like debugging code.

[Kaggle.com](https://www.kaggle.com/) is the best place to find datasets when you are starting out. Go ahead and sign up for an account and poke around the site. You will notice that there are many competitions for people of all experience levels and even tutorials to go with them (like [this beginner-friendly one](https://www.kaggle.com/c/titanic#tutorials) about the Titanic). These datasets will be very helpful to practice with while you are learning Python libraries.

### Python Libraries

Next, it’s important to learn the common Python libraries for working with data: Numpy, Matplotlib, Pandas, Scikit-Learn, etc. I recommend starting with [this course from datacamp](https://campus.datacamp.com/courses/intro-to-python-for-data-science). It goes over some basics which you can skip or use for review and the Numpy section is a good intro.

Pandas is a must learn but also takes a little while to grasp since it does so many things. It’s built on top of Numpy and is used for cleaning, preparing, and analyzing data. It also has built-in tools for things like visualization. I used a lot of resources to learn Pandas and practice with it. Here are a few:

1. [Learn Pandas on Kaggle](https://www.kaggle.com/learn/pandas)
2. [Learn Pandas Video Course](https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y) | [Notebook for Course](https://nbviewer.jupyter.org/github/justmarkham/pandas-videos/blob/master/pandas.ipynb)
3. Jupyter Notebook Extra Examples: [Basics](https://nbviewer.jupyter.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section2_1-Introduction-to-Pandas.ipynb) | [Plotting with Matplotlib & Pandas](https://nbviewer.jupyter.org/github/fonnesbeck/Bios8366/blob/master/notebooks/Section0_2-Plotting-and-Visualization.ipynb) | [And Many More](https://github.com/fonnesbeck/Bios8366/tree/master/notebooks)

After Pandas comes Scikit-Learn. This is where things start to be applied more to actual machine learning algorithms. Scikit-Learn is a scientific Python library for machine learning.

The best resource I found for this so far is the book “[Hands on Machine Learning with Scikit-Learn and Tensorflow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291/ref=sr_1_4)”. I think it does a very good job of teaching you step-by-step with practical examples. The first half is about Scikit-Learn, so I did that part first and then came back to the Tensorflow portion.

There are many other Python libraries like Keras and PyTorch, but I will get into those later. This is already a lot to learn :)

### Shallow Learning

This is the first step into machine learning. Scikit-Learn has shallow learning functions like linear regression built into the library. The Scikit-Learn book that I mention above teaches about many types of common machine learning algorithms and lets you practice with hands on examples.

While that’s good, I still found it useful to also go through Andrew Ng’s Machine Learning course from Stanford. [It’s available to be audited for free on Coursera](https://www.coursera.org/learn/machine-learning#syllabus) (there is a podcast for this course on iTunes, but it’s a little hard to follow and well over a decade old). The quality of instruction is amazing and it’s one of the most recommended resources online (it’s not the easiest to get through which is why I recommend it down here).

Start going through the Andrew Ng course slowly and don’t get frustrated if you don’t understand something. I had to put it down and pick it up several times. I also took Matlab in college, which is the language he uses in the course, so I didn’t have trouble with that part. But if you want to use Python instead, you can find [the examples translated online](https://github.com/kaleko/CourseraML).

### Math :)

Yes, math is necessary. However, I don’t feel like an intense, math-first approach is best way to learn; it’s intimidating for many people. As OCDevel suggests in his podcast (linked above), spend most of your time learning practical machine learning and maybe 15–20% studying the math.

I think the first step here is to learn/brush up on statistics. It can be easier to digest and be both a lot fun and practical. After statistics, you will definitely need to learn a bit of linear algebra and some calculus to really know what’s going on in deep learning. This will take some time, but here are some of the resources that I recommend for this.

**Statistics Resources:**

1. I think the statistics courses on Udacity are quite good. You can start with [this one](https://www.udacity.com/course/intro-to-statistics--st101) and then explore the other ones they offer.
2. I loved the book, “[Naked Statistics](https://www.amazon.com/Naked-Statistics-Stripping-Dread-Data/dp/039334777X/ref=sr_1_1)”. It’s full of practical examples and enjoyable to read.
3. It’s also useful to understand Bayesian statistics and how it differs Frequentist and Classical models. [This coursera course](https://www.coursera.org/learn/bayesian-statistics) does a great job explaining these concepts — there is also a [part 2 of the course here](https://www.coursera.org/learn/mcmc-bayesian-statistics).

**Linear Algebra Resources:**

1. The book, “[Linear Algebra, Step by Step](https://www.amazon.com/Linear-Algebra-Step-Kuldeep-Singh/dp/0199654441/ref=sr_1_7)” is excellent. It’s like a high school/college textbook but well written and easy to follow. There are also plenty of exercises for each chapter with answers in the back.
2. [Essence of Linear Algebra video series](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) — The math explanations by 3blue1brown are amazing. I highly recommend his math content.
3. There is an overview of linear algebra in the Andrew Ng course as well but I think the two resources I list above are a bit easier to use for learning the subject.

**Calculus Resources:**

I had taken a few years of Calculus before, but I still needed to brush up quite a bit. I picked up a used textbook for Calc. 1 at a local bookstore to start. Here are some online resources that helped me as well.

1. [Essence of Calculus video series](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
2. [Understanding Calculus](https://www.thegreatcoursesplus.com/understanding-calculus) from The Great Courses Plus

**Other Helpful Math:**

1. [Mathematical Decision Making](https://www.thegreatcoursesplus.com/mathematical-decision-making-predictive-models-and-optimization) from The Great Courses Plus

### Deep Learning

After learning some math and the basics of data science and machine learning, it’s time to jump into more algorithms and neural networks.

You probably got a taste of deep learning already with some of the resources I mentioned in part 1, but here are some really good resources to introduce you to neural networks anyhow. At least they will be a good review and fill in some gaps for you.

1. [3blue1brown’s Series Explaining Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
2. [Deeplizard’s Intro to Deep Learning Playlist](https://www.youtube.com/watch?v=gZmobeGL0Yg&list=PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU)

While you are working through the Andrew Ng Stanford course, I recommend checking out fast.ai. They have several high quality, practical video courses that can really help to learn and cement these concepts. The first is [Practical Deep Learning for Coders](http://course.fast.ai/) and second — just released — is [Cutting Edge Deep Learning For Coders, Part 2](http://course.fast.ai/part2.html). I picked up so many things from watching and re-watching some of these videos. Another amazing feature of fast.ai is [the community forum](https://forums.fast.ai/); probably one of the most active AI forums online.

### Deep Learning Libraries in Python

I think it’s a good idea to learn a little bit from all three of these libraries. Keras is a good place to start as it’s API is made to be simpler and more intuitive. Right now, I use almost entirely PyTorch, which is my personal favorite, but they all have pro’s and con’s. Thus it’s good to be able to which one to choose in different situations.

**Keras**

* [Deeplizard Keras Playlist](https://www.youtube.com/watch?v=RznKVRTFkBY&list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL) — This channel has some seriously good explanations and examples. You can following along with the videos for free, or have access to the code notebooks as well by [subscribing on Patreon](https://www.patreon.com/deeplizard) at the $3 (USD) tier.
* I also found the [documentation for Keras](https://keras.io/) to be quite good
* Datacamp has many well-written tutorials for ML and Keras like [this one](https://www.datacamp.com/community/tutorials/deep-learning-python)

**Tensorflow**

* The Tensorflow section of book, “[Hands on Machine Learning with Scikit-Learn and Tensorflow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291/ref=sr_1_4)” (mentioned above also)
* [Deeplizard Tensorflow Series](https://www.youtube.com/watch?v=HEQDRWMK6yY&list=PLZbbT5o_s2xr83l8w44N_g3pygvajLrJ-)

**PyTorch**

* [Deeplizard Pytorch Series](https://www.youtube.com/watch?v=v5cngxo4mIg&list=PLZbbT5o_s2xrfNyHZsM6ufI0iZENK9xgG)
* [Udacity Pytorch Bootcamp](https://www.udacity.com/course/deep-learning-pytorch--ud188) — I’m currently taking Udacity’s Deep Reinforcement Learning nanodegree and I thought their PyTorch section earlier in the course was very good. They are about to launch it for free to the public! [Here are some of their PyTorch notebooks on Github](https://github.com/udacity/DL_PyTorch).
* [Fast.ai](http://www.fast.ai/) is also built with PyTorch — You will be learning this library some if you go through their courses.

### Blogs & Research Papers

I have found it very helpful to read current research as I learn. There are plenty of resources that help making complicated concepts, and the math behind them, easier to digest. These papers are also a lot more fun to read then you may realize.

1. [fast.ai blog](http://www.fast.ai/topics/)
2. [Distill .pub](https://distill.pub/) — Machine Learning Research explained clearly
3. [Two Minute Papers](https://www.youtube.com/user/keeroyz) — Short video breakdowns of AI and other research papers
4. [Arvix Sanity](http://www.arxiv-sanity.com/) — More intuitive tool to search through, sort, and save research papers
5. [Deep Learning Papers Roadmap](https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap)
6. [Machine Learning Subreddit](https://www.reddit.com/r/MachineLearning/) — They have ‘what are you reading’ threads discussing research papers
7. [Arxiv Insights](https://www.youtube.com/channel/UCNIkB2IeJ-6AmZv7bQ1oBYg) — This channel has some great breakdowns of AI research papers

### Audio-supplementary Education

1. [The Data Skeptic](https://dataskeptic.com/podcast/) — They have a lot of good shorter episodes, called [mini]s where they cover machine learning concepts
2. [Software Engineering Daily Machine Learning](https://itunes.apple.com/us/podcast/machine-learning-software-engineering-daily/id1230807136?mt=2)
3. [OCDevel Machine Learning Podcast](https://itunes.apple.com/us/podcast/machine-learning-guide/id1204521130) — I already mentioned this one, but I’m listing it again just in case you missed it

### Additional Learning Resources

* [Neural Networks and Deep Learning E-book](http://neuralnetworksanddeeplearning.com/)
* [Machine Learning Yearning](https://www.deeplearning.ai/machine-learning-yearning/) (free draft) by Andrew Ng

### The End

Please clap if this was helpful :)

Social Media: [@gwen_faraday](https://twitter.com/gwen_faraday)

_If you know of any other resources that are good, or see that I am missing something, please leave links in the comments. Thank you._

