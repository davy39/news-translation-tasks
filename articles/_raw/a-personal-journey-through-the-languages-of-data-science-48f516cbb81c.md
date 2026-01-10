---
title: A personal journey through the languages of data science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T00:44:24.000Z'
originalURL: https://freecodecamp.org/news/a-personal-journey-through-the-languages-of-data-science-48f516cbb81c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U9aYgROZ2pa4Aa78VZL2Ww.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: programming languages
  slug: programming-languages
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Elena Nisioti

  One does not simply walk into TensorFlow.

  A PhD is a good opportunity for introspection. In fact, it is important to create
  opportunities for introspection no matter how busy or insignificant the present
  feels like.

  We should not reg...'
---

By Elena Nisioti

**One does not simply walk into TensorFlow.**

A PhD is a good opportunity for introspection. In fact, it is important to create opportunities for introspection no matter how busy or insignificant the present feels like.

We should not regard our past as an immature period, but as an unfolding story. A story of discoveries, mistakes, skills, and projects that are now part of our professional consciousness.

No matter how good a tutorial, detailed an article, or well-designed a library, it all comes down to personal assimilation when you learn a new tool. And what is this personal quality that shapes our receptive filters, so that one person’s favorite language is another person’s nightmare? (My personal nightmare is **actually doing my everyday programming in C.**)

The past. This is what this article is going to be about. An account of my attempts to use MATLAB, Weka, R, C++, and Python in my data science career.

Data science is a wide field, employing people from a huge variety of backgrounds, like economics, biology, and linguistics. Although data science emerged from a pure statistical background, it soon hijacked the field of computer science and is today a tool as versatile and essential as a calculator.

As a result, the palette of programming languages for data science kind of feels like the universe: a lifetime is not enough to explore it, and it is constantly expanding.

We know that there are trade-offs involved with the generality, power, and complexity of a language. Therefore, the popularity of a language should serve only as an indication of current trends, not a factor for determining your own choice. Ultimately, it’s a matter of application, experience, and taste.

### MATLAB

I was introduced into the world of machine learning through [an online course](https://www.coursera.org/learn/machine-learning) taught by Andrew Ng. I recommend it to this day to people looking for a smooth introduction into the admittedly scarily vast world of machine learning.

Although Python and R were much more popular at that time, Andrew chose MATLAB for the course’s assignments. Little did this bother me at that time, but it sure feels odd these days. Data science courses focus more on how to use a language (or a library) to do data analysis than how to do data analysis using a language.

In retrospect, I see that Andrew opted for a general-purpose language. One that his audience, consisting mostly of undergraduate computer scientists and engineers, was probably already familiar with. As the focus of the course was on implementing learning algorithms without the use of libraries, MATLAB was as good as any specialised language would be.

Although a fan of automated tools and handy libraries, I can’t emphasize enough the importance of the do-it-yourself attitude towards data science algorithms at the beginning of your path.

> I learned very early the difference between knowing the name of something and knowing something. — Richard Feynman

MATLAB does not lack the libraries to perform a wide selection of data analysis and machine learning tasks. I’m sure it is the preferred framework for people that swear by it, like signal processing and control engineers.

But it is not hard to trace why it did not conquer the field of data analysis, and me. It is a very expensive tool. Its free alternative, Octave, it is far less than being its equal. It could also be that I was never into languages that don’t start counting from zero.

![Image](https://cdn-media-1.freecodecamp.org/images/wBmD4fCLR6Mkl5LedyoauCvlnbbC8HVLEjiR)
_It doesn’t always have to crash._

### Weka

My experience with Weka was short-lived. We were introduced to it as an optional tool for an assignment for the Pattern Recognition course at my university.

Without any intention to underestimate the skills I acquired through this course, the most valuable lesson was this: the effect a GUI has on the data scientist is profound. Weka boasts about its ease of use and comprehensibility, providing the ability to train a machine learning model by loading a dataset and **simply pressing a button**. It is not hard to see the benefits of this approach. There is a global market desperate for prediction models and not enough experts to satisfy those needs.

Finding automated tools and using them to derive off-the-self solutions is a current research area, termed as [AutoML](http://www.ml4aad.org/automl/), but it took us some years, and failures, to realise that we need **a human in the loop**.

The illusion that we can produce good models for real problems without first having a good understanding of the data collapsed, with failures such as [MarketSwitch and KXEN](https://blog.datarobot.com/automated-machine-learning-short-history), in the late 90s. Automated tools can ease our work, discovering good parameterizations of the algorithms, useful pre-processing steps, and efficient testing pipelines. But they can’t substitute for the human expert, at least with our current level of expertise.

All in all, you should take responsibility for the models that you create.

> “Man,” I cried, “how ignorant art thou in thy pride of wisdom!” — Mary Wollstonecraft Shelley, Frankenstein

### R

I delved into the mysteries and wonders of R during my diploma thesis. You’ve probably heard that R is a special child in the family of data analysis languages. But a steep learning curve is an understatement for the feelings of self-doubt and utter disorientation I experienced at the beginning of the deployment.

Our goal was to create a software tool for the automated execution of machine learning experiments. R was more of a purpose than a means, as we wanted to conduct an extensive research on machine learning techniques by using the rich repository of R libraries.

Having to set up a whole framework, I wanted to make use of the wonders of object-oriented programming in my design. So, the first question I had to address was: does R support object-orientation? It does! In four different ways, actually. None of which directly matches the object-oriented programming I’d experienced in C++, Java, or Python.

The different ways came up gradually while the needs of the R community were still being discovered and methods to easily define and group functionalities were necessary. With no clear plan for the desired class qualities, it is not surprising that you now have the freedom (or should I say burden) to choose between S3, S4, reference, and R6 classes. There are quite a few [resources](https://www.cyclismo.org/tutorial/R/objectOriented.html) nowadays on this subject but, it suffices to say, if your project needs object-orientation, then R is probably not the language to go for.

After I settled for reference classes, I then began giving flesh to my software skeleton. I soon realised that R has apparently developed with — what I call — the [principle of most astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment). Specialising in data analysis, R has to offer lots of handy tools, such as the fancy data structures called data.frames, which elegantly capture the characteristics and needs of a dataset.

However, I remember some subtle technicalities in R that gave me nightmares back at the time. Five different assignment operators. All variables are weakly typed, unless they aren’t. RStudio, a free UI for R, throws a runtime error if a plot does not fit in its plane. Did someone mention namespaces?

People decide to name their SVM package “e1071” instead of something more intuitive, and that’s how you should load it. You want to perform the same operation, for example training, and different packages use different names for it. It’s a drag to have to read the manual of different packages to perform the same action. It also leads to lots of bugs, if you ignore the manuals because you assume consistency.

Up to this point, I’ve probably given the impression that I dislike R. But this is not the case. Although I would never attempt to build a framework from scratch in R again, the abundance of packages provided by the open source, heterogeneous R community can help you make visualisations and state-of-the-art pre-processing. This is cool for standalone experiments.

When it comes to machine learning, there is a remedy for the lack of compatibility between different packages. It is called [**caret**](http://topepo.github.io/caret/index.html) and is an attempt to provide common interfaces for pre-processing, training, and making predictions that support many useful packages, such as [**nnet**](https://cran.r-project.org/web/packages/nnet/index.html) for neural networks and svmRadial for support vector machines. Our [automl tool](https://github.com/issel-ml-squad/ads) would have been (much more of ) a mess, had we not exploited the usefulness of caret.

### C++

Now, why would you do data analysis in C++? Why would anyone do it?

Since a summer internship is my only experience in a non-academic workplace, I am not a guru of the psychology of a big company when choosing the tools of its employees. I suspect it was out of a combination of tradition and need for commercial, efficient-in-execution-time code.

Nevertheless, I decided to perform my experiments in R and, when the end of the internship approached, I could transfer my models and functions to C++. What could possibly go wrong?

I soon found out that it is not hard to impress people that do data analysis in C++ with fancy diagrams and impressive pre-processing techniques using R packages. Some of my coworkers even got interested in R and started experimenting with it, which kind of made me proud as I am generally bad at persuading people.

After I acquired satisfactory results, using simple R packages for PCA and support vector machines, I ventured into incorporating my models into the existing (and impressively bulky) C++ framework. The libsvm [package](http://ftp.auckland.ac.nz/software/CRAN/doc/packages/kernlab.pdf) seemed to be appropriate for my case, offering operations related to support vector machines.

Now, there’s quite a few options when you want to transfer machine learning models across languages, acting on different levels of the problem. Moving from simple to sophisticated, one can transfer the mathematical model, that is the parameterization of the algorithm, translate the model file across libraries, or use a package to interface across languages.

I found out the hard way that simply using the same parameterization is not enough. Although the family of algorithms remains the same — in my case, SVMs with a gaussian kernel — different implementations may adopt different mathematical models, thus requiring different sets of parameters. Even if models remain the same, implementation-specific factors can affect the performance of the model so drastically that different parameterization is required.

The most appropriate way seems to be [**rcpp**](https://cran.r-project.org/web/packages/Rcpp/index.html)_,_ a package that gracefully interfaces between existing C++ frameworks and R scripts. Compatibility among libraries of the two different languages is also supported by some packages, but is hardly ever the case. Sometimes retraining is the easiest and most trustworthy solution.

After this experience with the data scientific aspect of C++, I reconsidered my severe judgment on R’s slack attitude.

### Python

One of the first discussions with my current supervisor was:

-So, what language will you use for your future experiments?

-I think I’ll go for Python.

-So, you are experienced with Python?

-No, I’ve just been through a lot and I have a very good hunch about it.

Happy that my horrendously insufficient arguments persuaded him, I now enjoy the benefits of doing data analysis in Python. The ease of setting up experiments, appending functionality, and benefiting from rich libraries have really set my work forward. Although I largely write my own code, I have so far used **OpenAI gym** to define my own environment for reinforcement learning experiments, and **TensorForce**, a library that extends **TensorFlow** with a great selection of reinforcement learning algorithms.

Nevertheless, I won’t argue in favour of an unquestionable superiority of Python, as that would defeat my purpose. Programmers tend to solidify their beliefs into strong statements about languages. Probably forgetting that there can’t be **one language to rule them all.** If there were, it would have to be so general that it couldn’t be that effective.

So, next time you are in front of a new dataset, don’t be afraid to add another software arrow into your data science quiver. If all else fails, you will at least have something to complain about.

> Life can only be understood backwards; but it must be lived forwards — Søren Kierkegaard

