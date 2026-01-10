---
title: How to install TensorFlow and Keras using Anaconda Navigator — without the
  command line
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-24T10:15:00.000Z'
originalURL: https://freecodecamp.org/news/install-tensorflow-and-keras-using-anaconda-navigator-without-command-line
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca140740569d1a4ca4d8c.jpg
tags:
- name: anaconda
  slug: anaconda
- name: keras
  slug: keras
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By Ekapope Viriyakovithya

  Say no to pip install in the command line! Here''s an alternative way to install
  TensorFlow on your local machine in 3 steps.


  _Photo by [Unsplash](https://unsplash.com/@kowalikus?utm_source=ghost&utm_medium=referral&utm_camp...'
---

By Ekapope Viriyakovithya

Say no to pip install in the command line! Here's an alternative way to install TensorFlow on your local machine in 3 steps.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-239.png)
_Photo by [Unsplash](https://unsplash.com/@kowalikus?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Krzysztof Kowalik</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

# Why am I writing this?

I played around with pip install with multiple configurations for several hours, trying to figure how to properly set my python environment for TensorFlow and Keras.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-31.png)
_why is tensorflow so hard to install — 600k+ results_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-32.png)
_unable to install tensorflow on windows site:stackoverflow.com — 26k+ results_

# Just before I gave up, I found this…

_“[One key benefit of installing TensorFlow using conda rather than pip is a result of the conda package management system. When TensorFlow is installed using conda, conda installs all the necessary and compatible dependencies for the packages as well.](https://www.anaconda.com/tensorflow-in-anaconda/?source=post_page---------------------------) _”__

This article will walk you through the process how to install TensorFlow and Keras by using the GUI version of Anaconda. I assume you have downloaded and installed [Anaconda Navigator](https://www.anaconda.com/distribution/?source=post_page---------------------------) already.

# Let’s get started!

1. Launch Anaconda Navigator. Go to the Environments tab and click ‘Create’.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-33.png)
_Go to ‘Environments tab’, click ‘Create’_

2. Input a new environment name - I put ‘tensorflow_env’. **Make sure to select Python 3.6 here!** Then ‘Create’, this may take few minutes.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-34.png)
_make sure to select Python 3.6_

3. In your new ‘tensorflow_env’ environment, select ‘Not installed’, and type in ‘tensorflow’. Then, tick ‘tensorflow’ and ‘Apply’. The pop-up window will appear, go ahead and apply. This may take several minutes.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-35.png)

Do the same for ‘keras’.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-36.png)

Check your installation by importing the packages. If everything is okay, the command will return nothing. If the installation was unsuccessful, you will get an error.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-37.png)
_no error pop up — Yeah!_

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-38.png)
_You can also try with Spyder._

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-39.png)
_no error pop up — Yeah!_

And…Ta-da! It’s done! You can follow [this article](https://towardsdatascience.com/how-to-build-a-neural-network-with-keras-e8faa33d0ae4?source=post_page---------------------------) to test your newly installed packages :)

---

Thank you for reading. Please give it a try, and let me know your feedback!

Consider following me on [GitHub](https://github.com/ekapope?source=post_page---------------------------), [Medium](https://medium.com/@ekapope.v?source=post_page---------------------------), and [Twitter](https://twitter.com/EkapopeV?source=post_page---------------------------) to get more articles and tutorials on your feed if you like what I did. :)

