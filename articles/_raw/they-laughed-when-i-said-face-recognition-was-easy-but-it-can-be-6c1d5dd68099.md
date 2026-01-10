---
title: They laughed when I said Face Recognition was easy. But it can be.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-29T17:55:45.000Z'
originalURL: https://freecodecamp.org/news/they-laughed-when-i-said-face-recognition-was-easy-but-it-can-be-6c1d5dd68099
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QhDzUIIwZVJBgaiKx4yBDA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
- name: TensorFlow
  slug: tensorflow
seo_title: null
seo_desc: 'By Tirmidzi Faizal Aflahi

  Maybe you have seen it before. Maybe some of you use a face unlock feature that
  some phones have. This technology called Face Recognition is simply amazing. But,
  do you think it is hard to make an application based on that t...'
---

By Tirmidzi Faizal Aflahi

Maybe you have seen it before. Maybe some of you use a **face unlock** feature that [some phones](https://www.theverge.com/circuitbreaker/2018/1/2/16840174/oneplus-5-face-unlock-oxygenos-open-beta) have. This technology called Face Recognition is simply amazing. But, do you think it is hard to make an application based on that technology? It is actually not that hard. You can even make it with **less than 10 lines of codes**! Seriously. Here is my Face Recognition Tensorflow tutorial, special for you.

### TL;DR

Here is the code, in case **_you don’t want to read_** the article. LOL.

```py
from easyfacenet.simple import facenet

images = ['images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg']
aligned = facenet.align_face(images)
comparisons = facenet.compare(aligned)

print("Is image 1 and 2 similar? ", bool(comparisons[0][1]))
print("Is image 1 and 3 similar? ", bool(comparisons[0][2]))
```

And it will output the following:

```
Is image 1 and 2 similar?  True
Is image 1 and 3 similar?  False
```

Wait, wait. No tensorflow? There is tensorflow of course. For this tutorial, I use an algorithm called [Facenet](https://github.com/davidsandberg/facenet) that was developed with tensorflow. And while it is easy enough for me to use Facenet out of the box while coding tensorflow syntax, I don’t think most of you would be comfortable with that.

So, I decided to create another interface on top of Facenet, which I called [**Easy Facenet**](https://pypi.org/project/easyfacenet/). To install the library, you can just type

```
pip install easyfacenet
```

And you are good to go!

The article should not end like this, should it? _Of course not_.

Let me explain to you, line by line, the tutorial. At the same time, we’ll cover how Face Recognition works in the first place.

### Face Recognition

![Image](https://cdn-media-1.freecodecamp.org/images/3DTIxnKPDarQyYXo88QGaPdggaYX85v6MyjF)
_Photo by [Unsplash](https://unsplash.com/photos/WiONHd_zYI4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Tianyi Ma</a> on <a href="https://unsplash.com/search/photos/macbook?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

So, how does Face Recognition work?

![Image](https://cdn-media-1.freecodecamp.org/images/xMHPbNlxw6NaWR4CtHNusWK1dR7bJXT7ov21)
_Courtesy of [OpenFace](http://cmusatyalab.github.io/openface/" rel="noopener" target="_blank" title=")_

As you can see from the picture above, the steps are like this:

1. Get an **input** image which should **contain a face**(s)
2. You need to find where exactly the face is and **put a bounding box around the face**
3. For consistency of the algorithm, you need to **transform the picture**, so that the position of mouth, nose, and eyes, are consistent for different pictures.
4. Then **crop it**
5. Input the cropped picture into the **Facenet algorithm,** which is a Deep Neural Network.
6. It will output a **vector representation** of that face. It was 128-dimensional vector back then, it is 512-dimensional right now.
7. Then you can do what you want with that representation. You can do **classification**, **clustering**, or just use a **similarity** **computation** between pictures.

Wow, that was a hell of a lot of stuff. Why is it so difficult? Well, basically you can group those 7 steps into 3 steps, which are,

1. **Alignment**, input an image and output the aligned cropped face
2. **Embedding**, input the face and output the representation
3. **Comparison**, compare those representations — are they similar or not?

Because it’s only 3 simple steps, the code should be as simple as that, shouldn’t it?

Yes, it can be, using **easyfacenet**.

### The simplest Face Recognition Tensorflow library available

Let’s break down the code bit by bit.

```py
from easyfacenet.simple import facenet
```

Import the _facenet_ file from a _simple_ module. There are three methods you can use inside the file. They are, **align_face**, **embedding**, and **compare**.

Easily, you can tell that each of these methods represents each step for Face Recognition.

```py
images = ['images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg']
```

Now we can define the images. What are those images? Well, _this_.

![Image](https://cdn-media-1.freecodecamp.org/images/NBYPXP4BP9RJC2p6HPWbrA-gqx58OyqqbSVZ)
_A picture of me (image1.jpg)_

And _this_.

![Image](https://cdn-media-1.freecodecamp.org/images/9Caduw4e7kq6XEEy2M3IqBWMzB5OoR0loQLh)
_Another picture of me (image2.jpg)_

And also _this_.

![Image](https://cdn-media-1.freecodecamp.org/images/1w9-X2Sxef4YMgYvsVNGf7OQRlCPzenTSXOO)
_My Lil’ bro (image3.jpg)_

We got the images. Now the real deal.

### Step 1. Alignment

```py
aligned = facenet.align_face(images)
```

The library will try to find the face inside the image and crop the face as well as [pre-whiten](https://github.com/davidsandberg/facenet/issues/433) the face. **Prewhitening** will make the training easier at training time, so in inference time, you will also need to prewhiten the image.

The prewhitened aligned face will look like this.

![Image](https://cdn-media-1.freecodecamp.org/images/CBCceYCyVyGh1er8p-Nl4mKgQxCIeVF49NwX)
_Image 1 to 3 from left to right_

Now, you are ready for the next step. Take a breather and chew slowly!

### Step 2. Embeddings

Wait, wait. I don’t see embeddings in the example above? Well, that’s because **the compare method already called embedding inside**. If you want to use embedding somehow, use this.

```py
embeddings = facenet.embedding(aligned)
```

The **embeddings** will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/FkVJ2zmPEJyxo2uTVrctJEFPbq8jIXTT1iNs)
_I don’t recommend you to look at the numbers_

### Step 3. Comparison

```py
comparisons = facenet.compare(aligned)
```

If you have 3 images, the **comparisons** variable will have 3 x 3 values. Which are **permutations** of each image compared to each other. In an example, if you want to get “**_is image 1 is similar to image 2?_**”, then

```py
print("Is image 1 and 2 similar? ", bool(comparisons[0][1]))
```

**_Is image 1 similar to image 3?_**

```py
print("Is image 1 and 3 similar? ", bool(comparisons[0][2]))
```

You didn’t forget already that the array is zero indexed, did you? Haha…

**And, that’s it**. You can get your comparison result just like that. The comparison technique I used is the **cosine similarity**. You can use any other similarity method you want. You can definitely use another method like clustering or classification. Something like the [Siamese Network](https://medium.com/@kuzuryu71/improving-siamese-network-performance-f7c2371bdc1e) is the thing you need to look for.

### What can you do next?

![Image](https://cdn-media-1.freecodecamp.org/images/61vE2pz5ezVb6SsLi3MzCzXg78COBEnKPi8j)
_Photo by [Unsplash](https://unsplash.com/photos/tMI2_-r5Nfo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Corinne Kutz</a> on <a href="https://unsplash.com/search/photos/macbook?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

As I have said, this is the **simplest Face Recognition Tensorflow library available.** Therefore you can start to do your thing as quickly as possible.

If you are the hacky one, you can explore the library and create the real Face Recognition Tensorflow code. Take a look at the code [here](https://github.com/taflahi/facenet/blob/master/simple/facenet.py) because that is the cornerstone of the library. Furthermore, extend the code or you can create your own functionality.

### Final Thoughts

If you want to know about the **paper** behind this amazing technology, you can look [here](https://arxiv.org/abs/1503.03832) as well as [here](http://www.robots.ox.ac.uk/~vgg/publications/2015/Parkhi15/parkhi15.pdf).

In conclusion, utilizing easyfacenet can help you tremendously in creating your face recognition project. Moreover, this Face Recognition library is **maintained** solely **by me.** It is easy for you if you want to ask for some kind of functionality.

As for the actual implementation for the other similarity method, I will bring you there in the next tutorial. Due to that reason, I will add the method exclusively inside the library.

Finally, if you want to read the original article, I originally published this on my blog post here at [thedatamage](https://thedatamage.com/face-recognition-tensorflow-tutorial/). Of course, you can read many more posts from me there.

