---
title: How to Learn Machine Learning – Tips and Resources to Learn ML the Practical
  Way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T17:28:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-machine-learning-practical-tips-and-resources
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Article-Visual-Template.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: null
seo_desc: "By Yacine Mahdid\nA lot of people want to learn machine learning these\
  \ days. But the daunting bottom-up curriculum that most ML teachers propose is enough\
  \ discourage a lot of newcomers. \nIn this tutorial I flip the curriculum upside\
  \ down and will outl..."
---

By Yacine Mahdid

A lot of people want to learn machine learning these days. But the daunting bottom-up curriculum that most ML teachers propose is enough discourage a lot of newcomers. 

In this tutorial I flip the curriculum upside down and will outline what I think is the fastest and easiest way to get a solid grasp of ML.

### Table of Contents

The curriculum I propose here is a looping multi-step step process that goes like this:

* **[Step 0: Immerse yourself in the Machine Learning field](#heading-step-0-immerse-yourself-in-the-machine-learning-field)**
* **[Step 1: Study one project that looks like your endgame](#heading-step-1-study-one-project-that-looks-like-your-endgame)**
* **[Step 2: Learn the programming language](#heading-step-2-learn-the-programming-language)**
* **[Step 3: Learn the libraries from top to bottom](#heading-step-3-learn-the-libraries-from-top-to-bottom)**
* **[Step 4: Do one project that you're passionate about in max one month](#heading-step-4-do-one-project-youre-passionate-about-in-max-one-month)**
* **[Step 5: Identify one gap in your knowledge and learn about it](#heading-step-5-identify-one-gap-in-your-knowledge-and-learn-about-it)**
* **[Step 6: Repeat steps 0 to 5](#heading-step-6-repeat-steps-0-to-5)** 

This is a looping learning plan because the 6th step is actually a GOTO to Step 0!

As a disclaimer, this curriculum might strange to you. But I've battle tested it when I was teaching machine learning to undergraduates at McGill University. 

I tried many iteration of this curriculum, starting with the theoretically superior bottom-up approach. But from experience, this pragmatic top-down approach is what gives the best results. 

One common critique I get is that people not starting with the basics, like statistics or linear algebra, will have a poor understanding of machine learning and they will not know what they are doing when modeling. 

In theory, yes, this is true and this is why I started teaching ML with the bottom up approach. In practice, this has never been the case.

What actually ended up happening was that because the students knew how to do the high level modeling, they were much more inclined to delve into the low level stuff on their own as they saw the direct benefit it would bring to their higher level skills. 

This context that they were able to set for themselves wouldn't have been there if they'd started from the bottom – and this is where I believe most teachers lose their students.

All that being said, let's jump into the actual learning plan! 🚀🚀🚀

## Step 0: Immerse Yourself in the Machine Learning Field

The very first part of learning anything is to take some time t0 understand where _things end_ and where your interest lies. 

This will have two main benefits:

* Knowing the size of the field will allow you to know you are not missing out on something, so it will increase your focus.
* It will be easier to draw a path in your mental model if you know what the landscape you are strolling in looks like.

![sheep grazing, with mighty himalayas as backdrop](https://images.unsplash.com/photo-1565618408142-2b7446ec7c5a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDE2fHxzaGVlcHxlbnwwfHx8fDE2MjQxMjA0Njg&ixlib=rb-1.2.1&q=80&w=2000)
_Imagine that you are a sheep in a pasture. It's important that you know where the boundaries are and where the grass taste better : Photo by [Unsplash](https://unsplash.com/@aranya00?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">ARANYA KAR</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

In order to immerse yourself properly in the field and hone your learning plan, you should answer these three questions in order:

* **What can you do with Machine Learning?**
* **What do you want to do with Machine Learning?**
* **How do you do that specific thing?**

These questions will allow you to zone into something very specific and manageable to learn, while also allowing you to see the bigger picture.

Let's look at each of these questions in a bit more detail.

### What can you do with Machine Learning? 

This questions is very broad and will change month over month. The great thing with this curriculum is that at every pass through the steps you will spend some time learning about what is possible in the field. 

This will allow you to refine your mental model of Machine Learning. So if you don't have a 100% accurate picture of what is possible in your first pass, it's not a big deal. Approximate understanding is better than none.

![Image](https://images.unsplash.com/photo-1519904981063-b0cf448d479e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDR8fGhpZ2h8ZW58MHx8fHwxNjI0MTIxNzYy&ixlib=rb-1.2.1&q=80&w=2000)
_Think of this question as climbing a foggy mountain and taking note of the landscape down below: Photo by [Unsplash](https://unsplash.com/@lux17?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Lucas Clara</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Here is a brief overview of what you can do with machine learning, from the technical to the practical applications.

#### Technical Machine Learning Topics

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-22.png)
_Classification task using SVM_

* **Supervised Learning:** This type of learning involves giving input and labeled output to a model to train it. Once the training is done, you should technically be able to give it an input and it will generate the right output. 
* **Unsupervised Learning:** This learning involves input without output. You ask the model to make sense of the patterns in the data.
* **Reinforcement Learning:** This ML setup involves an agent, an environment, actions the agent can do, and rewards. It kind of looks like how you would train a dog with treats.
* **Online Learning:** This type of learning can be both supervised and unsupervised. The particularity is that the model can be updated "Online" as the stream of data comes in.
* **Transfer Learning:** This type of learning is when you use an already trained model as the starting point for a different learning task. This greatly speeds up the learning of the second task.
* **Ensemble Learning:** This ML technique involves putting multiple trained predictors together (one after the other or by taking a vote of the output) and using this ensemble of predictors as the final predictor.

There are many more flavors of machine learning, but these are a good starting point.

#### Common Machine Learning Models

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-23.png)
_[One of the most complicated types of model called a Deep Neural Network](https://github.com/ashishpatel26/Tools-to-Design-or-Visualize-Architecture-of-Neural-Network)._

* **Linear Regression:** This is the good ol' `y = ax + b` formula which actually works quite well for a lot of problems. This should be the starting point for most analysis.
* **Logistic Regression:** This is a type of model that models the probability of a class or multiple classes. Even though it has regression in the name it's a classification model.
* **Decision Tree:** The decision tree model creates a tree of  'decisions' or formulae, which when followed lead to the desired output. These types of models are important because they are easy to understand and inspect once trained.
* **Support Vector Machine (SVM):** Think of this model as constructing a plane that separate two class with maximum width in between. It's a bit more complicated than that, but imagine a line with a thickness and you are half-way there.
* **Naive Bayes:** These types of classifiers use Bayes' Theorem which assumes that all features are independent from each other. This is rarely the case, though, this is why it's called naïve. It does work surprisingly well in practice even when that assumption doesn't hold.
* **k-nearest neighbors:** This type of classifier doesn't require training, it simply memorizes all of the elements in the dataset. It can then give you an output based on the distance of the input with the other point in the dataset.
* **K-Means:** This unsupervised model will, given a number of clusters, figure out which points belong to which cluster. It will do this by repeatedly modifying the centroid of each cluster until it converges to something stable.
* **Random Forest:** This is an ensemble technique which uses a lot of very simple decision tree classifiers. The output of the model is the class output by the most decision trees.
* **Dimensionality Reduction Algorithms:** There are a wide-variety of dimensionality reduction algorithms, principal components analysis being one of them. The gist of all these algorithms is that they can create a mapping from the dataset with lots of dimensions (features) to a representation with fewer. When it maps to 2 or 3 dimensions it allows us to visualize a high dimensional dataset in 2D or 3D.
* **XGBoost:** This model is a regularized gradient boosted model. In a nutshell, it has weak learners setup in series instead of in parallel (like random forest). It's a very good model and is usually a top performer in machine learning competitions.
* **Deep Neural Network:** These types of models are a whole field of their own. Basically they are weak predictors put both in series and in parallel. These models are able to construct a hierarchical representation of the data which yield great results. They are notoriously finicky (to say the least) to train because of their high capacity. There are lots of architectures that are possible for these models, like CNNs and Transformers.

There are a lot of machine learning models out there. But thankfully you don't need to know all of them to be proficient in machine learning. 

Actually if you know **Linear Regression**, **SVM**, **XGBoost** and some form of **Deep Neural Network** you are good to go for most problems. But learning how the model learns gives you more mental flexibility and allows you to think differently about problems.

#### Common Applications of Machine Learning

This is one area where things will change drastically from month to month. Basically in any field where you have data being collected you can throw ML into the mix. 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-24.png)
_[Type of ML application called image segmentation](https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/) (useful for self-driven cars)._

The point here is that the breadth and depth of the application of ML is ever expanding. So don't fret too much if you think you have only a superficial understanding of what is possible.

* **Computer Vision:** Machine Learning (and Deep Learning more particularly) are currently at a point where they're pretty good at anything to do with images and recognizing objects. There are also generative kinds of analysis you can do where the Neural Network are able to generate an image using specific architectural tricks (GAN or Neural Style Transfer, for instance).
* **Natural Language Processing (NLP):** This includes quite a lot of sub topics like: answering questions, translation, classifying documents or text generation.
* **Medical Diagnosis:** When you're dealing with medical images, it's pretty common to use computer vision techniques to analyze them. But medical diagnosis can also include readings that are not image-based like concentration of a certain hormone in a blood sample.
* **Bioinformatics:** This is a very broad field overlapping with many other techniques. In general, bioinformatics uses machine learning techniques to deal with bio-data and their analysis. Here you can think of protein folding as one type of task in bioinformatics that relies heavily on machine learning.
* **Outlier Detection:** Recognizing when something is part of a category or when it's so far off from the bulk of the data that it must be an outlier is a very important exercise in many fields.
* **Weather Forecasting:** Anything really having to do with massive amount of data points over time will be a good candidate for applying machine learning. Weather forecasting is one kind of problem in which there are lots of data available throughout time. 

This list could go on for a while. The point here is to make a good map of what is possible so that you feel grounded in the next phase of your learning journey.

### What do you want to do with Machine Learning? 

This questions is the most important one. You won't be able to meaningfully do everything in Machine Learning (or any other field). You have to be very selective about what you think is a good use of your time and what is not.

One way of making this choice is to rank your interests in descending order. 

![Work day](https://images.unsplash.com/photo-1517817748493-49ec54a32465?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDV8fG5vdGVzfGVufDB8fHx8MTYyNDEyNDA4OQ&ixlib=rb-1.2.1&q=80&w=2000)
_Take a good old pen and paper and rank these learning topics 👺: Photo by [Unsplash](https://unsplash.com/@adolfofelix?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Adolfo Félix</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Then just select your top-most interest and pin it somewhere you can see it. This is what you will be learning and nothing else until your rankings change. 

And keep in mind that you can definitely change your interests. If you are very interested in a specific topic but, after learning about it more, it's not as interesting anymore, then it's OK to ditch the topic and take up another one. That's the whole reason you do this first planning step.

Here, if there are many subjects that interest you, I strongly advise that you still commit to only one for a cycle. All subjects interconnect in some way. Going deep into a topic will allow you to see these connections. Jumping superficially from topic to topic will not.

If I was to learn something new right now in my 100th pass through this learning curriculum I would dive into **Graph Neural Networks** and their application in **Supply Chain Management**.

### How do you do that specific thing?

Now that you know what interests you and where it lies with respect to the general context, spend some time understanding how are people doing it. 

![Image](https://images.unsplash.com/photo-1606857521015-7f9fcf423740?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDV8fG9mZmljZXxlbnwwfHx8fDE2MjQxMjQ1ODc&ixlib=rb-1.2.1&q=80&w=2000)
_What are they using, what is their setup? Photo by [Unsplash](https://unsplash.com/@israelandrxde?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Israel Andrade</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Spending time understanding what you will be spending weeks (or longer) studying is very important. Being able to gain context to ground what you will be learning and knowing what you don't need to know about will save you lots of time and energy.

It will also help you understand what you don't really need to focus your energy on. For example, if you find that most people aren't using HTML, CSS, and JavaScript in their everyday ML work, don't focus on these technologies.

In terms of what people use in ML, there is a wide range of programming languages and tools depending on the application. You have tools in C++, Java, Lua, Swift, JavaScript, Python, R, Julia, MATLAB, Rust...and the list goes on and on.

But the density of practitioners are quite clustered around Python and its package ecosystem. Python is a relatively easy to grasp programming language with a thriving ecosystem. This means that people who want to build machine-learning tools more likely to develop those tools with a Python interface. 

The actual tools are aren't usually developed in pure Python, though, because the language is quite slow. But since they have a direct interface to Python the user won't know that it's actually a C++ library wrapped in Python. 

If you didn't get that last part it's all right. Just keep in mind that Python + libraries in Python are a very safe bet to learn.

#### Tools to Use for Machine Learning

The usual suspects for tools to learn for ML are the following:

* [**Python**](https://www.python.org/) for high level programming
* [**Pandas**](https://pandas.pydata.org/) for dataset manipulation
* [**Numpy**](https://numpy.org/) for numerical computing on CPU
* [**Scikit-learn**](https://scikit-learn.org/stable/) for non-deep learning machine learning models
* [**Tensorflow**](https://www.tensorflow.org/) or [**Pytorch**](https://pytorch.org/) for Deep Learning machine learning models
* Higher level wrapper Deep Learning libraries like [**Keras**](https://keras.io/) and [**fast.ai**](https://www.fast.ai/)
* Basics of [**Git**](https://git-scm.com/) for working on your project
* [**Jupyter Notebook**](https://jupyter.org/) or [**Google Colab**](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjxoMiDw7jxAhWVK80KHUXiCTYQFjAAegQIBxAD&url=https%3A%2F%2Fresearch.google.com%2Fcolaboratory%2F&usg=AOvVaw38J01zt_Dlb6pQ1fe6FGrI) for code experimentation

There are many more tools that you can use, [like a looooot more](https://github.com/josephmisiti/awesome-machine-learning#python)! Be aware of them, but don't stress too much that you are not up on the very latest library. The technologies mentioned above are good enough for most projects. 

But there are some libraries that you might need to add to your stack because they are specialized for your domain of study.

In my case, to study **Graph Neural Networks** and their application in **Supply Chain Management**, it seems like all of these packages are alright. Still, there are more specialized packages in Pytorch like the [Pytorch geometri](https://github.com/rusty1s/pytorch_geometric)c library which would speed up my development of Graph Neural Networks. 

So my stack would look like this: 

**Python + Pandas + Pytorch + Pytorch geometric +  Git + Colab** 

I know that this stack is good for my use-case since I studied how people where developing in that specific sub field and this is what they're using.

## Step 1: Study One Project that Looks Like Your Endgame

Now that you know exactly what you want to do and you have a rough idea of how you'll do that specific thing, it's time to get more specific.

The best way to learn deeply about how to do something is to watch an actual expert work. You can look at this as an asynchronous apprenticeship.

![Broadcast engineers work in studio](https://images.unsplash.com/photo-1581092922699-2766a7278454?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDd8fGFwcHJlbnRpY2V8ZW58MHx8fHwxNjI1NTAwMzcy&ixlib=rb-1.2.1&q=80&w=2000)
_You and your mentor figuring out what all the blinking lights are for: Photo by [Unsplash](https://unsplash.com/@thisisengineering?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">ThisisEngineering RAEng</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Being able to see the end result of where you want to be in action will give you more context to ground your learning than any theory.

So to do this, the best way is to hop on GitHub or Kaggle and check out public projects. Review a few of them until you find one that resonates with you. 

This could be a full blown library, a simple analysis, or a production ready AI. Whatever it is, find a few of them and then select the one project that interests you the most.

Once you have that project, do take some time to run through the documentation, the structure of the codebase, and the code. You will likely be lost. Especially if you don't know much about how to code. But this is a positive feeling when learning something new!

Take some notes about repeated patterns that you are seeing, interesting bits that you understand, or topics you don't really understand. Bookmark this project and go back to it when you have moved along your learning path.

A good place to start looking is [this list on GitHub](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code). However, just searching around on [Kaggle](https://www.kaggle.com/) or GitHub for keywords that relate to your interests with machine learning will do the trick.

For my specific learning plan, a good simple project is this one from [Thomas Kipf](https://github.com/tkipf/pygcn). It is simple enough that I can walk through it and understand what is happening at each section, while at the same time learn the basics of the structure.

## Step 2: Learn the Programming Language

Now that you have a very clear picture of where you need to go and what you need to learn, it's time to understand the code.

The code will most likely be Python-based, but depending on what you want to learn and what project you bookmarked you might get into Julia, C++, Java or others. 

Whatever language it is, you should take some time to learn the basics in order to understand how to cobble together scripts.

A very good course to learn enough Python in order to be functional is [freeCodeCamp's Scientific Computing with Python course](https://www.freecodecamp.org/learn/scientific-computing-with-python/) or [Kaggle's very short Python course](https://www.kaggle.com/learn/python). 

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Capture.PNG)
_Highly recommend this one from freeCodeCamp!_

You don't need to understand 100% of how the language works. Each pass through this curriculum, spend a bit of time refining your knowledge of the programming language you choose so the learning will be iterative.

In my case for my learning plan, the freeCodeCamp course would do the trick.

## Step 3: Learn the Libraries from Top to Bottom

One thing that I often see in machine learning curricula is that they start implementing some of the algorithms from scratch after learning the basics of ML. 

While I believe this is a great project to do on its own, I don't think that this should be the main focus early on in your path to learning machine learning.

The main reason is that almost no one is implementing algorithms from scratch, except the people making the packages devs are using. Even then, they often rely on other packages made by linear-algebra folks to do much of the low level work.

All of this to say that although having a strong understanding of how things work under the hood is a net positive, but I don't think it should be an early goal.

What I strongly advise at this point is to learn the highest level library in the programming language you choose which will get you to the end results. Learn how to use that super high level package enough to make something that works. 

You'll definitely lack understanding as to why something is working or not at this point, but it doesn't matter too much.

What matters is being able to get your hands moving with the tools that experts actually use day-to-day. Once you kinda understood what the high level library is doing you should move on to a slightly lower level one. 

Make sure you don't go too deep into learning the library, though (if you are at the [LAPACK](http://www.netlib.org/lapack/) level while reading about Fortran, you've gone too far!!).

For my project, the main library I need to learn is Pytorch or its higher lever wrapper, so [a practical course by fast.ai](https://course.fast.ai/) would do the trick.

## Step 4: Do One Project You're Passionate About in Max One Month

Now comes the actual part where the most learning will happen. At this point you should have the bare-minimum knowledge to duck-tape together a project that has minimal usefulness. 

Just a note – if you feel totally confident going into the project you are planning, you haven't moved fast enough through steps 0 to 3.

Think about something in your area of interest that you would really want to create and develop. Don't go too crazy on the project, though, as it should take between 1 week and 1 month max to complete. 

**Put that date in your calendar with a notification.** Having a time-bounded project is both motivating and just stressful enough that you will get it done.

The idea here is to struggle enough on a small-ish project to understand where your major knowledge gaps are and to experience what an actual machine learning developer experiences. 

By going free-form without the harness of a course or a book you will be able to do the actual parts of an ML project that are hard:

* Plan, scope, and track your ML project's progress
* Read documentation online about libraries
* Read StackOverflow, GitHub threads, a random engineer's blog post and cryptic help forum about that one bug 👺.
* Build your project in a sub-optimal way and improve it over time.
* Debug overfitting, underfitting, and generalization issues.

To pick a project that interests you, I suggest doing these three small exercises:

* Think deeply about what interests you currently 
* Look at a list of project ideas
* Take a look at open datasets

By doing a mix of these three things, you will be able to form more context about what is possible. You'll also to mix-and-match your interests to make something truly your own.

This [list on Github](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) should be a very good spot to get some inspiration about a mini-project to do. You can then combine that with [Google Dataset Search engine](https://datasetsearch.research.google.com/) in order to find some data that match your project.

⚠️ Don't underestimate the importance of data. ⚠️  
Even if you have very good ideas, if there is no data available it will severely hinder your progress. 

For my interests, I have found this neat dataset about a [Mining Company's Global Supply Chain](https://figshare.com/articles/dataset/Mining_Company_s_Global_Supply_Chain_Logistics_Data_for_a_Medium_Size_Excavator_Extended_Dataset/2749120/1) with quite enough data to make something out of it. My project will be about modeling the data as a graph and using Graph Neural Networks to infer sale prices of an excavator that is the central topic of this dataset.

## Step 5: Identify One Gap in Your Knowledge and Learn About it

At this point you've spent some time crafting your project and you are actually impressed by how far you've gotten with it. It's probably nowhere near what you had in mind, though, and you've encountered countless issues in your path. 

Now, you are realizing how little you actually know and that there are some part of your knowledge that you really need to patch up.

![Living the best times of their lives.](https://images.unsplash.com/photo-1573269354259-8c108692afa1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDE1fHxzdW4lMjBwZW9wbGV8ZW58MHx8fHwxNjI1NTAwODU0&ixlib=rb-1.2.1&q=80&w=2000)
_You rejoicing in your newfound ignorance! Congrats 👏 : Photo by [Unsplash](https://unsplash.com/@daniel_joshua_?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Daniel Joshua</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

This is great! Make a list of all the gaps that you saw along the way and rank them in order of your estimated priority. This might be hard for you, since everything will look very important at this point. But doing the exercise of making a conscious decision about what to learn next is almost as valuable as the learning itself.

Now comes the strange part: eliminate everything from your list and only learn the most important piece of knowledge.

When I say eliminate, I mean it. Delete everything but the first one. When you do another pass in this loop, your estimate of what to learn next will be mostly wrong and you will be missing other more critical bits of knowledge that you didn't know about.

Now that you have only one item left to learn, give yourself between 1 day to 1 week to learn about this particular topic. This may seem very short, but what you really want here is to get just deep enough in the knowledge to be functional for your next round of learning. 

![Designer sketching Wireframes](https://images.unsplash.com/photo-1434030216411-0b793f4b4173?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDJ8fGxlYXJuaW5nfGVufDB8fHx8MTYyNDEyNzY5NA&ixlib=rb-1.2.1&q=80&w=2000)
_Study that one little bit of knowledge very hard for a short period of time: Photo by [Unsplash](https://unsplash.com/@craftedbygc?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Green Chameleon</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

In practice, what might happen is that you get deep enough into this topic to notice how it links to other important topics (like probability, statistics, or even the god-forsaken-linear-algebra). 

Take a hard look at these links, follow them if you feel like it, and reinforce your mental model of machine learning in order to make it more accurate.

## Step 6: Repeat Steps 0 to 5

Your first pass through this pipeline will likely be so-so at best. But you will have learned much more in a very short period of time than anything you would have achieved with the bottom up approach.

The value you will get out of this method increases quite rapidly through each pass of the pipeline. Each round will be easier and you will get a clearer picture of the field.

This methodology is based on the lean methodology that I learned to apply at my [startup](https://axya.co/en/) with great success. Doing multiple iterations on the topic you are optimizing for is the fastest way to get to your goal.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-168.png)
_Three step lean cycle, image taken from [here](https://www.calltheone.com/en/consultants/build-measure-learn-cycle-lean-startup)._

Within the year you might be able to stack 12 pass through this pipeline, which means 12 machine learning projects and a very hands-on comprehension of the field.

This method will make you both highly hirable and will give you the tools you need to improve yourself, all on your own.

Also, as a side note for people that are already familiar with machine learning, **this is gradient descent**. You are literally doing gradient descent on the "learning machine-learning" problem by doing some small step in the cost plane of your ignorance. 

You are even doing a variant of gradient descent which looks ahead in the cost plane and is able to slow down (spend more time on a project or learning concept) or speed up (skip when the topic is not that relevant for your understanding). This is [Nesterov-accelerated gradient](https://youtu.be/6FrBXv9OcqE) in a nutshell 😄 (lol sorry for that bit)!

![Image](https://www.freecodecamp.org/news/content/images/2021/06/maxresdefault.jpg)
_This is you in your cost plane of machine learning ignorance going waaaaaay down._

## Summary and Conclusion

In summary you should:

1. Figure out what the ML field looks like and make a mental map of it.
2. Find a cool project that you would like to do and study it.
3. Learn the required programming language.
4. Learn enough libraries to be able to do something useful.
5. Do a project for [1 week, 1 month].
6. Learn about one thing that you saw as a big gap in your knowledge.
7. And reiterate!

I hope this was useful, don't hesitate to reach out to me via [LinkedIn](https://www.linkedin.com/in/yacine-mahdid-809425163/) if you have strong opinions about this process. Also, if you want to learn more about a specific machine learning topic, take a look at my [Youtube channel](https://www.youtube.com/channel/UCts-XMcexTiPSR8QbyRGFxA).

Have a great one 👋

# Useful Machine Learning Resources

In this section I'll share a collection of learning resources I recommend for people wanting to get started learning. This is not an exhaustive list, but it will be a good starting point for people wanting to get a good first mental model of Machine Learning.

## Machine Learning Books

### The Elements of Statistical Learning By Astie et al.

A classic in the machine learning community, highly recommend spending time with this book over and over again.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-26.png)
_Great introductory book!_

### Artificial Intelligence, A Modern Approach (3rd Edition)

This will give you a good overview about the broader field of artificial intelligence which doesn't necessarily include machine learning.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-27.png)
_This book ties the whole AI/ML/DL field together quite nicely_

### The Deep Learning Book

Big classic in the deep learning field, it's surprisingly a very approachable book if you have some background in linear algebra (there is a primer at the beginning).

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-29.png)
_The cover is very neat as it was generated by a Deep Neural Network_

### Python Data Science Handbook: Essential Tools for Working with Data

Really great book to be able to upgrade your data science skill in Pandas and Numpy. This will make your code much more compact, efficient, and readable.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-30.png)
_Keep it close to your desk and do the exercises_

### Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems

If you had one book to go through to get up and running it would be this one. Very thorough and hands-on.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-31.png)
_Take either the HD lizard or the grayscale one, both are very solid!_

### Deep Learning with Pytorch

I love this book because you get a direct insight by the creators of Pytorch about their philosophy (and there are some neat neuroscience examples in there which I'm always happy to see).

![Image](https://www.freecodecamp.org/news/content/images/2021/07/71sXWAx3ktL.jpg)
_The visuals for this one are very well done, especially the tensors part._

## Machine Learning Blogs

### Machine Learning Mastery

If you do end up googling a lot of stuff on a project (like any human being) you will quite repeatedly end up at this blog post: [machinelearningmastery](https://machinelearningmastery.com).

It's quite well written and the SEO this person was able to get out of the website for ML related topics is quite amazing.

### Analytics Vidhya

The second blog you will most likely find on Google search is this one, [analyticsvidhya](https://www.analyticsvidhya.com). It might look a bit more spammy than the previous one but there is still lots of great content in there.

### Distill

Very neat visually rich _journal_ for machine learning topics: [distill.pub](https://distill.pub/)

It seems that they are taking a one year hiatus though because the whole team burned out, but nevertheless there's high quality ML content in there.

## Machine Learning Community

### r/MachineLearning

[Great community](https://www.reddit.com/r/MachineLearning/) to get the very latest development in machine learning and/or to get a hot take on current events in the ML community.

It shares high quality content, and by lurking in there for a while will get you a sense of what others in the field think.

It also generates good learning gems such as [this one](https://www.reddit.com/r/MachineLearning/comments/5z8110/d_a_super_harsh_guide_to_machine_learning/):

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Capture-1.PNG)
_This is very blunt, but still relevant._

### r/LearnMachineLearning

This is an [excellent community for newcomers](https://www.reddit.com/r/learnmachinelearning/) to ask questions, post your projects, or get some inspiration from the work of others.

## Machine Learning Events

### MAIN (Montreal AI and Neuroscience) Conference

I'm biased over here because this is a conference that joins two of my interests: Neuroscience and Machine Learning: [2020 link](https://www.main2020.org/) & [Youtube video](https://www.youtube.com/channel/UCddp3o-ctW8rmYtfdDfVUkA)

Also, since it's hosted in Montreal and I live nearby I can usually hop in there to check what are the latest advancements in Computational Neuroscience.

### NeurIPS (Neural Information Processing Systems) Conference

This one is the [mythical machine learning conference](https://nips.cc/) on neural networks.

It kind of became overcrowded in the recent years up to the point that its usefulness as been put into question. Still, if you can't attend, checking what the researchers that get accepted to it work on is a good idea.

There are [a lot more out there](https://www.guide2research.com/topconf/machine-learning) and it's a great idea to go to conferences from time to time in order to see really cutting edge research. It can be a bit overwhelming, but it's a great learning experience.

## Online Machine Learning Courses

### Fast AI

If I had one online course to recommend it would be [this one from FastAI](https://course.fast.ai/#How-do-I-get-started?).

It actually embodies this pragmatic-straight-to-the-action approach I've wrote about in this blog post + the teacher is highly entertaining. 

### Andrew Ng ML (of course)

If I had a second one to recommend I'll go with [Andrew Ng's course on machine learning](https://www.coursera.org/learn/machine-learning).

### freeCodeCamp's Machine Learning and Data Analysis YouTube Courses

freeCodeCamp has a bunch of great Machine Learning and Data Analysis courses on their YouTube channel, like:

* [Python for Bioinformatics](https://www.freecodecamp.org/news/python-for-bioinformatics-use-machine-learning-and-data-analysis-for-drug-discovery/)
* [Python and scikit-learn Crash Course](https://www.freecodecamp.org/news/learn-scikit-learn/)
* [Dive into Deep Learning](https://www.freecodecamp.org/news/learn-deep-learning-from-the-president-of-kaggle/)
* [How to Analyze Data with Python, Pandas, and NumPy](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/)
* [Deep learning with PyTorch](https://www.freecodecamp.org/news/free-deep-learning-with-pytorch-live-course/)
* And of course, [Python for Everybody from Dr. Chuck](https://www.freecodecamp.org/news/python-for-everybody/)

There's lots more where those came from – just head over to freeCodeCamp's YouTube channel and search for what you want to learn.

