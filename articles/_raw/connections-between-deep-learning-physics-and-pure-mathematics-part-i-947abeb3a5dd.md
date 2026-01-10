---
title: Connections between Neural Networks and Pure Mathematics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-12T08:23:21.000Z'
originalURL: https://freecodecamp.org/news/connections-between-deep-learning-physics-and-pure-mathematics-part-i-947abeb3a5dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GJj62r8BX02Sx0I26O3DUA.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: Mathematics
  slug: mathematics
- name: 'Science '
  slug: science
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Marco Tavora

  How an esoteric theorem gives important clues about the power of Artificial Neural
  Networks

  Nowadays, artificial intelligence is present in almost every part of our lives.
  Smartphones, social media feeds, recommendation engines, onlin...'
---

By Marco Tavora

#### How an esoteric theorem gives important clues about the power of Artificial Neural Networks

Nowadays, artificial intelligence is present in almost every part of our lives. Smartphones, social media feeds, recommendation engines, online ad networks, and navigation tools are examples of AI-based applications that affect us on a daily basis.

Deep learning has been systematically improving the state of the art in areas such as speech recognition, autonomous driving, machine translation, and visual object recognition. However, the reasons why deep learning works so spectacularly well are not yet fully understood.

### Hints from Mathematics

[Paul Dirac](https://en.wikipedia.org/wiki/Paul_Dirac), one of the fathers of quantum mechanics and arguably the greatest English physicist since [Sir Isaac Newton](https://www.westminster-abbey.org/abbey-commemorations/commemorations/sir-isaac-newton/), once remarked that progress in physics using the “[method of mathematical reason](http://www.damtp.cam.ac.uk/events/strings02/dirac/speach.html)” would

> “…enable[s] one to infer results about experiments that have not been performed. There is no logical reason why the […] method should be possible at all, but one has found in practice that it does work and meets with reasonable success. This must be ascribed to some mathematical quality in Nature, a quality which the casual observer of Nature would not suspect, but which nevertheless plays an important role in Nature’s scheme.”

> — Paul Dirac, 1939

![Image](https://cdn-media-1.freecodecamp.org/images/5ZKarm0xndzz384YDVedKxTTau618wLukOBK)
_Portrait of Paul Dirac is at the peak of his powers (Wikimedia Commons)._

There are many examples in history where purely abstract mathematical concepts eventually led to powerful applications way beyond the context in which they were developed. This article is about one of those examples.

Though I’ve been working with machine learning for a few years now, I’m a [theoretical physicist](https://scholar.google.com/citations?user=SaB1GO0AAAAJ&hl=en) by training, and I have a soft spot for pure mathematics. Lately, I have been particularly interested in the connections between deep learning, pure mathematics, and physics.

This article provides examples of powerful techniques from a branch of mathematics called [mathematical analysis](https://en.wikipedia.org/wiki/Real_analysis). My goal is to use rigorous mathematical results to try to “justify”, at least in some respects, why deep learning methods work so surprisingly well.

![Image](https://cdn-media-1.freecodecamp.org/images/Iwu2ZtCJlo0yRbVQjxfldXmO1tZx9O4P19BZ)
_Abstract representation of a neural network ([source](https://www.shutterstock.com/g/ktsdesign" rel="noopener" target="_blank" title="))._

### A Beautiful Theorem

In this section, I will argue that one of the reasons why artificial neural networks are so powerful is intimately related to the mathematical form of the output of its neurons.

![Image](https://cdn-media-1.freecodecamp.org/images/yDxrc-KkYWRqxhJNWZF85398nV8fMrOCjjAc)
_A manuscript by Albert Einstein ([source](http://www.alberteinstein.info/manuscripts.html" rel="noopener" target="_blank" title="))._

I will justify this bold claim using a celebrated theorem originally proved by two Russian mathematicians in the late 50s, the so-called [Kolmogorov-Arnold representation theorem](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Arnold_representation_theorem).

![Image](https://cdn-media-1.freecodecamp.org/images/FZ9m54A8ujLhtGC5Q5Ek45M3j7sPYdzzKqXi)
_The mathematicians Andrei Kolmogorov (left) and Vladimir Arnold (right)._

#### Hilbert’s 13th problem

In 1900, [David Hilbert](https://en.wikipedia.org/wiki/David_Hilbert), one of the most influential mathematicians of the 20th century, presented a famous [collection of problems](https://en.wikipedia.org/wiki/Hilbert%27s_problems) that effectively set the course of the 20th-century mathematics research.

The Kolmogorov–Arnold representation theorem is related to one of the celebrated [Hilbert problems](https://en.wikipedia.org/wiki/Hilbert%27s_problems), all of which hugely influenced 20th-century mathematics.

#### Closing in on the connection with neural networks

A generalization of one of these problems, the [13th](https://en.wikipedia.org/wiki/Hilbert%27s_thirteenth_problem) problem specifically, considers the possibility that a function of _n_ variables can be expressed as a combination of sums and compositions of just two functions of a single variable which are denoted by Φ and _ϕ_.

More concretely:

![Image](https://cdn-media-1.freecodecamp.org/images/5ciEd-xaR7lp3US513Jo20KsVnwtor2qBeWU)
_Kolmogorov-Arnold representation theorem_

Here, _η_ and the λs are real numbers. It should be noted that these two univariate functions are Φ and _ϕ_ can have a highly complicated (fractal) structure.

Three articles, by Kolmogorov (1957), Arnold (1958) and [Sprecher](http://www.ams.org/journals/tran/1965-115-00/S0002-9947-1965-0210852-X/S0002-9947-1965-0210852-X.pdf) (1965) provided a proof that there must exist such representation. This result is rather unexpected since according to it, the bewildering complexity of multivariate functions can be “translated” into trivial operations of univariate functions, such as additions and function compositions.

### Now what?

If you got this far (and I would be thrilled if you did), you are probably wondering: how could an esoteric theorem from the 50s and 60s be even remotely related to cutting-edge algorithms such as artificial neural networks?

### A Quick Reminder of Neural Networks Activations

The expressions computed at each node of a neural network are compositions of other functions, in this case, the so-called activation functions. The degree of complexity of such compositions depends on the depth of the hidden layer containing the node. For example, a node in the second hidden layer performs the following computation:

![Image](https://cdn-media-1.freecodecamp.org/images/L8v4n0-Pw16u8yIcdkQXoTADtSM5zyWJJQfr)
_Computation performed by the k-th hidden unit in the second hidden layer._

Where the _w_s are the weights, and the _b_s are the biases. The similarity with the multivariate function _f_ shown a few paragraphs above is evident!

Let us quickly write down a function in Python only for forward-propagation which outputs the calculations performed by the neurons. The code for the function below has the following steps:

* **First line**: the first activation function _ϕ_ acts on the first linear step given by:

```
x0.dot(w1) + b1
```

where `x0` is the input vector.

* **Second line: t**he second activation function acts on the second linear step

```
y1.dot(w2) + b2
```

* **Third line:** a [softmax function](https://en.wikipedia.org/wiki/Softmax_function#Neural_networks) is used in the final layer of the neural network, acting on the third linear step

```
y2.dot(w3) + b3
```

The full function is:

```
def forward_propagation(w1, b1, w2, b2, w3, b3, x0):        y1 = phi(x0.dot(w1) + b1)    y2 = phi(y1.dot(w2) + b2)    y3 = softmax(y2.dot(w3) + b3)        return y1, y2, y3
```

To compare this with our expression above we write:

```
y2 = phi(phi(x0.dot(w1) + b1).dot(w2) + b2)
```

The correspondence can be made more clear:

![Image](https://cdn-media-1.freecodecamp.org/images/T77L1UoWBNfvewKPTmoAzGReC54fhnp0eKzV)

### A Connection Between Two Worlds

We, therefore, conclude that the result proved by Kolmogorov, Arnold, and Sprecher implies that neural networks, whose output is nothing but the repeated composition of functions, are extremely powerful objects, which can represent any multivariate function or equivalently almost any process in nature. This partly explains why neural networks work so well in so many fields. In other words, the generalization power of neural networks is, at least in part, a consequence of the Kolmogorov-Arnold representation theorem.

As pointed out by [Giuseppe Carleo](https://indico.math.cnrs.fr/event/2435/), the generalization power of forming functions of functions of functions _ad_ nauseam was, in a way, “discovered independently also by nature” since neural networks, which work as shown above doing precisely that, are a simplified way to describe how our brains work.

Thanks a lot for reading! Constructive criticism and feedback are always welcome!

My [Github](https://github.com/marcotav) and my website [www.marcotavora.me](https://marcotavora.me/) have some other interesting stuff both about data science and physics.

There is a lot more to come, stay tuned!

