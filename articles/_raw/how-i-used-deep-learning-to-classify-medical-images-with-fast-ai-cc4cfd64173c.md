---
title: How I used Deep Learning to classify medical images with Fast.ai
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T16:53:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-deep-learning-to-classify-medical-images-with-fast-ai-cc4cfd64173c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vyFlFjwlsfV7DX3kBDXJPQ.png
tags:
- name: AI
  slug: ai
- name: Deep Learning
  slug: deep-learning
- name: 'fastai, '
  slug: fastai
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By James Dietle

  Convolutional Neural Networks (CNNs) have rapidly advanced the last two years helping
  with medical image classification. How can we, even as hobbyists, take these recent
  advances and apply them to new datasets? We are going to walk th...'
---

By James Dietle

Convolutional Neural Networks (CNNs) have rapidly advanced the last two years helping with medical image classification. How can we, even as hobbyists, take these recent advances and apply them to new datasets? We are going to walk through the process, and it’s surprisingly more accessible than you think.

As our family moved to Omaha, my wife (who is in a fellowship for pediatric gastroenterology) came home and said she wanted to use image classification for her research.

Oh, I was soooo ready.

For over two years, I have been playing around with deep learning as a hobby. I even wrote several articles ([here](https://medium.com/@JamesDietle/part-of-the-fun-of-learning-data-science-is-seeing-how-quickly-it-can-relate-to-your-usual-roles-ceb7b0ff5f13) and [here](https://medium.com/@JamesDietle/9-months-in-the-hobby-of-deep-learning-d688cce4fa2e)). Now I had some direction on a problem. Unfortunately, I had no idea about anything in the gastrointestinal tract, and my wife hadn’t programmed since high school.

### **Start from the beginning**

My entire journey into deep learning has been through the [Fast.ai](https://www.fast.ai/) process. It started 2 years ago when I was trying to validate that all the “AI” and “Machine Learning” we were using in the security space wasn’t over-hyped or biased. It was, and we steered clear from those technologies. The most sobering fact was learning that being an expert in the field takes a little experimentation.

#### **Setup**

I have used Fast.ai for all the steps, and the newest version is making this more straightforward than ever. The ways to create your learning environment are proliferating rapidly. There are now docker images, Amazon amis, and services (like [Crestle](https://www.crestle.com/)) that make it easier than ever to set up.

Whether you are the greenest of coding beginners or experienced ninja, [start here](https://course.fast.ai/) on the Fast.ai website.

I opted to build my machine learning rig during a previous iteration of the course. However, it is not necessary, and I would recommend using another service instead. Choose the easiest route for you and start experimenting.

#### **Changes to Fast.ai with version 3**

I have taken the other iterations of Fast.ai, and after reviewing the newest course, I noticed how much more straightforward everything was in the notebook. Documentation and examples are everywhere.

Let’s dive into “[lesson1-pets](https://github.com/fastai/course-v3/blob/master/nbs/dl1/lesson1-pets.ipynb)”, and if you have setup Fast.ai feel free to follow along in your personal jupyter instance.

![Image](https://cdn-media-1.freecodecamp.org/images/u7vNdhatx2eygqg8w4IUCXuZGZuRHIx2y4f5)
_lesson1-pets from Fast.ai_

I prepared for the first lesson (typically defining between 2 classes — cats and dogs — as I had many times before. However, I saw this time that we were doing something much more complex regarding 33 breeds of cats and dogs using fewer lines of code.

**The CNN was up and learning in 7 lines of code!!**

That wasn’t the only significant change. Another huge stride was in showing errors. For example, we could quickly see a set of the top losses (items we confidently predicted wrong) and corresponding pet pictures from our dataset below.

![Image](https://cdn-media-1.freecodecamp.org/images/KWKmlZf52x6jVJPZDmtUMITcbqCbHl54Tjwh)
_Incorrect cat and dog breed predictions_

This function was pretty much a spot check for bad data. Ensuring a lion, tiger, or bear didn’t sneak into the set. We could also see if there were glaring errors that were obvious to us.

The confusion matrix was even more beneficial to me. It allowed me to look across the whole set for patterns in misclassification between the 33 breeds.

![Image](https://cdn-media-1.freecodecamp.org/images/sfF1pvbZpjjbu3n6GjRMuRaUbQxHAMg-jeTm)

Of the 33 breeds presented, we could see where our data diverged and ask ourselves if it made sense. A few breeds popped out in particular, and here are examples of the commonly confused images:

![Image](https://cdn-media-1.freecodecamp.org/images/59yz56xv0LGDuWt8T1iQuqWRP-lE74eJqUkK)
_Staffordshire terrier and American terrier._

![Image](https://cdn-media-1.freecodecamp.org/images/8vnEnaLgEN6Dm9I6AeIzYzxD3-4MbV36UYMt)
_Egyptian Mau and Bengal_

Not being a pet owner or enthusiast, I wouldn’t have be able to figure out these subtle details out about a breed’s subtle features. The model is doing a much better job than I would’ve been able to do! While I am certainly getting answers, I am also curious to find that missing feature or piece of data to improve the model.

There is an important caveat. We are now at the point where the model is _teaching_ us about the data. Sometimes we can get stuck in a mindset where the output is the end of the process. If we fall into that trap, we might miss a fantastic opportunity to create a positive feedback loop.

![Image](https://cdn-media-1.freecodecamp.org/images/2YFbSBKXrC8F4-AZn65WWIiJQ7rLnHkoAOBW)
_30-second powerpoint drawing_

Therefore, we are sitting a little wiser and little more confident in the 4th phase. Given this data, what decisions should I improve accuracy with?

* More training
* More images
* More powerful architecture

Trick question! I am going to look at a different dataset. Let’s get up and personal with endoscope images of people’s insides.

### **Get the dataset, see a whole lot of sh… stuff**

For anyone else interested in gastroenterology I recommend looking into [The Kvasir Dataset](https://datasets.simula.no/kvasir/#data-collection). A good description from their site is:

> the dataset containing images from inside the gastrointestinal (GI) tract. The collection of images are classified into three important anatomical landmarks and three clinically significant findings. In addition, it contains two categories of images related to endoscopic polyp removal. Sorting and annotation of the dataset is performed by medical doctors (experienced endoscopists)

There is also a [research paper](https://www.researchgate.net/publication/316215961_KVASIR_A_Multi-Class_Image_Dataset_for_Computer_Aided_Gastrointestinal_Disease_Detection) by experts (Pogorelov et al.) describing how they tackled the problem, which includes their findings.

Perfect, this is an excellent dataset to move from pets to people. Although a less cuddly dataset (that also includes stool samples) it is something exciting and complete.

As we download the data, the first thing we notice is that there are 8 classes in this dataset for us to classify instead of the 33 from before. However, it shouldn’t change any of our other operations.

![Image](https://cdn-media-1.freecodecamp.org/images/uo1ea2vqjqGnAJwIXtSBKnHIjWhRJrXi0LXx)

_Side Note: Originally, I spent a few hours scripting out how to move folders into validation folders, and spent some good time setting everything up. The scripting effort turned out to be a waste of time because there is already a simple function to create a validation set._

_The lesson is “if something is a pain, chances are someone from the Fast.ai community has already coded it for you.”_

### Diving into the notebook

_You can pick up my Jupyter notebook from [GitHub here](https://github.com/jamesdietle/fastaipart3/blob/master/Kvasir-Dataset2.ipynb)._

#### **Building for speed and experimentation**

As we start experimenting, it is crucial to get the framework correct. Try setting up the minimum needed to get it working that can scale up later. Make sure data is being taken in, processed, and provides outputs that make sense.

This means:

* Use smaller batches
* Use lower numbers of epochs
* Limit transforms

If a run is taking longer than 2 minutes, figure out a way to go faster. Once everything is in place, we can get crazy.

#### Data Handling

Data prioritization, organization, grooming, and handling is the most important aspect of deep learning. Here is a crude picture showing how data handling occurs, or you can read the [documentation](https://docs.fast.ai/basic_data.html).

![Image](https://cdn-media-1.freecodecamp.org/images/Ni-fwUCcGWDAXcUlCqgVl8Epvi13uUqUHVwl)

Therefore we need to do the same thing for the endoscope data, and it is one line of code.

![Image](https://cdn-media-1.freecodecamp.org/images/JtZ6HKXcNXHZbxTGaFNOaMEnI8zVSJeF4dgS)

Explaining the variables:

* Path points to our data (#1)
* The validation set at 20% to properly create dataloaders
* default transforms
* the image size set at 224

That’s it! The data block is all set up and ready for the next phase.

#### Resnet

We have data and we need to decide on an architecture. Nowadays Resnet is popularly used for image classification. It has a number after it which equates to the number of layers. Many [better articles](https://medium.com/@14prakash/understanding-and-implementing-architectures-of-resnet-and-resnext-for-state-of-the-art-image-cf51669e1624) exist [about Resnet](https://medium.com/@14prakash/image-classification-architectures-review-d8b95075998f), therefore, to simplify for this article:

> More layers = more accurate (Hooray!)

> More layers = more compute and time needed (Boo..)

Therefore Resnet34 has 34 layers of image finding goodness.

#### Ready? I’m ready!

With the structured data, architecture, and a default error metric we have everything we need for the learner to start fitting.

Let’s look at some code:

![Image](https://cdn-media-1.freecodecamp.org/images/Y-uV2EnLty823Yv1yMquSiR2aRgacmKyd1ck)

We see that after the cycles and 7 minutes we get to 87% accuracy. Not bad. Not bad at all.

Not being a doctor, I have a very untrained eye looking at these. I have no clue what to be looking for, categorization errors, or if the data is any good. So I went straight to the confusion matrix to see where mistakes were being made.

![Image](https://cdn-media-1.freecodecamp.org/images/EVJNURCQyxNtY8JnWDo7gQ-nbpxjG5P04ow2)

Of the 8 classes, 2 sets of 2 are often confused with each other. As a baseline, I could only see if they are dyed, polyps, or something else. So compared to my personal baseline of 30% accuracy, the machine is getting an amazing 87%.

After looking at the images from these 2 sets side by side, you can see why. (Since they are medical images, they might be NSFW and are present in the Jupyter notebook.)

1. The dyed sections are being confused with each other. This type of error can be expected. They are both blue and look very similar to each other.
2. Esophagitis is hard to tell from a normal Z-line. Perhaps esophagitis presents redder than Z-line? I’m not certain.

Regardless, everything seems great, and we need to step up our game.

### More layers, more images, more power!

Now that we see our super fast model working, let’s switch over to the powerhouse.

* I increased the size of the dataset from v1 to v2. The larger set doubles the number of images available from 4000 to 8000. _(Note: All examples in this article show v2.)_
* Transform everything that makes sense. There are lots of things you can tweak. We are going to go into more of this shortly.
* Since the images from the dataset are relatively large, I decided to try making the size bigger. Although this would be slower, I was curious if it would be better able to pick out little details. This hypothesis still requires some experimentation.
* More and more epochs.
* If you remember from before, Resnet50 would have more layers (be more accurate) but would require more compute time and therefore be slower. So we will change the model from Resnet34 to Resnet50.

#### **Transforms: Getting the most of an image**

Image transforms are a great way to improve accuracy. If we make random changes to an image (rotate, change color, flip, etc.) we can make it seem like we have more images to train from and we are less likely to overfit. Is it as good as getting more images? No, but it’s fast and cheap.

When choosing which transforms to use, we want something that makes sense. Here are some examples of normal transforms of the same image if we were looking at dog breeds. If any of these individually came into the dataset, we would think it makes sense. Putting in transforms we now we have 8 images instead for every 1.

![Image](https://cdn-media-1.freecodecamp.org/images/HnxacZmYHwcPPBgjOeLVLBh8YllnaULywJBn)

What if in the transformation madness we go too far? We could get the images below that are a little too extreme. We wouldn’t want to use many of these because they are not clear and do not correctly orient in a direction we would expect data to come in. While a dog could be tilted, it would never be upside down.

![Image](https://cdn-media-1.freecodecamp.org/images/MNijsrlyoAn6dSbT2SiepF27riQolrHI7LA3)

For the endoscope images, we are not as concerned about it being upside down or over tilted. An endoscope goes all over the place and can have a 360-degree rotation here, so I went wild with rotational transforms. Even a bit with the color as the lighting inside the body would be different. All of these seem to be in the realm of possibility.

![Image](https://cdn-media-1.freecodecamp.org/images/tpnXtApoMmk8rhYu71DdHORHiCP5oVwXHF9q)
_Example of dyed polyps_

_(Note: the green box denotes how far the scope traveled. Therefore, this technique might be cutting off the value that could have provided.)_

#### Reconstructing data and launching

Now we can see how to add transforms and how we would shift other variables for data:

![Image](https://cdn-media-1.freecodecamp.org/images/QUZEWFkUm8lcFXTCWXM58rplndCdQUW1A2M4)

Then we change the learner:

![Image](https://cdn-media-1.freecodecamp.org/images/jzQl2sQv19lAeWrUdY4B6UpXYbmo40tjy0mr)
_It really is that easy_

Then we are ready to fire!

![Image](https://cdn-media-1.freecodecamp.org/images/ApcLKcBsWNAF1Iz6Pw0cGx6sBVnc2tgB6NjK)

_Many epochs later…_

![Image](https://cdn-media-1.freecodecamp.org/images/qHbnsIFF1V209q1rVzFmzMZvE7Vz0EjN-oA4)
_Just worry about the number of the right here_

93% accurate! Not that bad, let’s look a the confusion matrix again.

![Image](https://cdn-media-1.freecodecamp.org/images/LfwbVbdB131A6yIuizYC2KpS02lZ1KqMJZx1)

It looks like the problem with dyed classification has gone away, but the esophagitis errors remain. In fact, the numbers of errors get worse in some of my iterations.

### Can this run in production?

Yes, there are instructions to quickly host this information as a web service. As long as the license isn’t up and you don’t mind waiting… you can try it on [Render right here](https://kvasir-demo.onrender.com/)!

![Image](https://cdn-media-1.freecodecamp.org/images/5YnqATL1HQXt7zcTcvCi2wEeXQxVLMrq43BH)

### Conclusion and Follow-up:

As you can see, it is straightforward to transfer the new course from Fast.ai to a different dataset. Much more accessible than ever before.

When going through testing, make sure you start with a fast concept to make sure everything is on the right path, then turn up the power later. Create a positive feedback loop to make sure you are both oriented correctly and as a mechanism to force you to learn more about the dataset. You will have a much richer experience in doing so.

Some observations on this dataset.

* I am trying to solve this problem wrong. I am using a single classifier when these slides have multiple classifications. I discovered this later while reading the research paper. _Don’t wait until the end to read papers!_
* As a multi-classification problem, I should be including bounding boxes for essential features.
* Classifications can benefit from a feature describing how far the endoscope is in the body. Significant landmarks in the body would help to classify the images. The small green box on the bottom left of the images is a map describing where the endoscope is and might be a useful feature to explore.
* If you haven’t seen the new fast.ai course take a look, it took me more time to write this post than it did to code the program, it was that simple.

**Resources**

* [Github Notebook](https://github.com/jamesdietle/fastaipart3/blob/master/Kvasir-Dataset2.ipynb)
* [Kvasir Dataset](https://datasets.simula.no/kvasir/#data-collection)
* [KVASIR: A Multi-Class Image Dataset for Computer Aided Gastrointestinal Disease Detection](https://www.researchgate.net/publication/316215961_KVASIR_A_Multi-Class_Image_Dataset_for_Computer_Aided_Gastrointestinal_Disease_Detection) (Pogorelov, Konstantin & Randel, Kristin & Griwodz, Carsten & de Lange, Thomas & Eskeland, Sigrun & Johansen, Dag & Spampinato, Conceo & Dang Nguyen, Duc Tien & Lux, Mathias & Schmidt, Peter & Riegler, Michael & Halvorsen)
* [FastAI](https://docs.fast.ai/)
* [PyTorch](https://pytorch.org/docs/master/)
* [Youtube video on this topic](https://youtu.be/GXuqT4uMKZk)

