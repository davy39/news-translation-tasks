---
title: What René Descartes can teach you about design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T18:59:27.000Z'
originalURL: https://freecodecamp.org/news/what-rene-descartes-can-teach-you-about-design-e0eace2ca268
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fVDFjkeeRS_wz1WpFX5Zrw.png
tags: []
seo_title: null
seo_desc: 'By Vishal Kumar

  Following on from How ancient mathematics can enrich your design skills


  _[vishalkumar.london](https://www.instagram.com/vishalkumar.london/" rel="noopener"
  target="blank" title=")


  I think, therefore I am.


  That is one of the most po...'
---

By Vishal Kumar

#### Following on from [How ancient mathematics can enrich your design skills](https://medium.freecodecamp.org/using-ancient-mathematics-to-enrich-your-design-skills-ac360a83d297)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fVDFjkeeRS_wz1WpFX5Zrw.png)
_[vishalkumar.london](https://www.instagram.com/vishalkumar.london/" rel="noopener" target="_blank" title=")_

> _I think, therefore I am._

That is one of the most popular phrases throughout the whole of European philosophy. It refers to human consciousness, cognition, and life.

That was a neat bit of knowledge. But you’re probably thinking, “what does that phrase have to do with **design,** and why should I care?”

It’s not so much the phrase, but the person behind it.

In this essay, I am going to unearth [René Descartes](https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes)’ knowledge of **algebraic geometry** (technically, [analytic geometry](https://en.wikipedia.org/wiki/Analytic_geometry)) via several mathematical and coding examples to explain why and how his insights are important for modern design.

As you scroll down, I hope my findings will help you _think_ differently about design!

### **Who was René Descartes?**

The famous French philosopher and mathematician who popularised the phrase, “_I think, therefore I am”,_ properly formalised this idea in his influential book, _Discourse on Method_, published in 1637.

Descartes was a fierce rationalist. He trusted in nothing more than the human mind and intellect to carry out reason and logic.

Yet most people don’t realise that in order to reason, Descartes would **frequently consult ancient Greek treaties on geometric proofs** by [Euclid](https://en.wikipedia.org/wiki/Euclid) (325 BC) and [Archimedes](https://en.wikipedia.org/wiki/Archimedes) (225 BC).

It is also less well-known that, as well as being a philosopher, Descartes was also one of the founders of **algebraic geometry.** He literally created the mathematical language which translates geometry into algebra, and the other way around.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LWz8NFZegrB2VgB6-Ib2xA@2x.png)
_1 [vishalkumar.london](https://www.instagram.com/vishalkumar.london/" rel="noopener" target="_blank" title=") — adapted from page 206, Book 3 of La Geometrie, René Descartes_

### La Geometrie (a bit of context)

> “The greatest single step ever made in the progress of the exact sciences”

Descartes admired pure geometry as an exercise in logic and induction, but grew frustrated with ancient Greek geometric proofs. With the renaissance of [algebra from the Islamic world in the 16th century](https://www.cambridge.org/core/books/cambridge-history-of-science/islamic-mathematics/4BF4D143150C0013552902EE270AF9C2/core-reader), Descartes sought to find a new language to express the relationship between algebra and geometry.

In a famous letter to Dutch philosopher Isaac Beeckman on March 26th 1619, Descartes announces his plan to advance an “entirely new science”.

Published as a sort-of appendix to 1637’s _Discourse on Method_, [_La Geometrie_](http://djm.cc/library/Geometry_of_Rene_Descartes_rev2.pdf) was Descartes’ new science. It was described by philosopher [John Stuart Mill](https://plato.stanford.edu/entries/mill/) as:

> “The greatest single step ever made in the progress of the exact sciences”

That’s a pretty big statement from one of the most influential philosophers of the 20th Century!

Mill wasn’t misguided with his judgement. Really, _La Geometrie_ was truly revolutionary. Descartes’ insights have created the bedrock of knowledge we all use today to perform basic mathematical tasks and calculations. Watch the wonderful video below by Sal Kahn to learn more.

So influential were Descartes’ ideas, the word “cartesian” takes his name — (Des) cartesian coordinates, cartesian equations, and so on.

Moreover, the syntax he invented in _La Geometrie_ was copied by Leibniz and adopted by Newton in the 17th century when both of them went on to create calculus!

![Image](https://cdn-media-1.freecodecamp.org/images/1*D7HJoCPQDb86XIV2VUvWcw@2x.png)
_Cartesian coordinate plane — [wikipedia](https://en.wikipedia.org/wiki/Cartesian_coordinate_system" rel="noopener" target="_blank" title=")_

### Why is _La Geometrie_ important for modern design?

Okay, so I hope I have convinced you that Descartes’ ideas were, and are, important. Now, let’s see some of those ideas applied to design.

Before you design anything, you should conceptually think about, understand, and visualise how the design would mathematically and geometrically be feasible.

Of course, there are [many design decisions to be made](https://medium.com/google-design/the-meaning-of-design-44f1a82129a8) — colour, depth, user experience… the list goes on. But, the core of any design starts with geometry, shapes, and forms... even a small scribble on a post-it note.

Humans tend to have a fairly intuitive understanding of geometry and shapes. For example, you know that in the below image there is a circle, a small equilateral triangle and four solid lines.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0DL--Bx114jYEbYVUdWGGA@2x.png)
_2 [vishalkumar.london](https://www.instagram.com/vishalkumar.london/" rel="noopener" target="_blank" title=") — adapted from page 61, Book 2 of La Geometrie, René Descartes_

Descartes’ insight comes from trying to express those shapes using algebra.

His method goes like this: first, he gives each point a letter — A, B, C, D, E, and so forth.

He then joins each point with a line or curve — for example, the line from C to B is expressed as CB. He then assigns another letter _y_ to that line. For example, CB = _y_.

These notational devices permitted him to describe an association of numbers to lengths of line segments that could be constructed with a straightedge and compass. This meant that he was able to create an algebraic equation using measurements and proportions which represented the shape.

Once you know how a shape (or a series of shapes) can be expressed using an algebraic equation, you then translate that equation on to a coordinate plane by coding the shape using a computer (you could also draw it by hand).

[Tyler Neylon](https://www.freecodecamp.org/news/what-rene-descartes-can-teach-you-about-design-e0eace2ca268/undefined)’s [wonderful article](https://medium.com/@tylerneylon/how-to-write-mathematics-on-medium-f89aa45c42a0) explains how he used equations and functions and then JavaScript to create the GIF below. The full code is [here](https://gist.github.com/tylerneylon/4d58806a2a00d6073733).

![Image](https://cdn-media-1.freecodecamp.org/images/1*w_1EysnL5ZWIHPX1fhTXhw@2x.gif)
_Taken from Tyler Neylon’s Medium post, [How to Write Mathematics on Medium](https://medium.com/@tylerneylon/how-to-write-mathematics-on-medium-f89aa45c42a0" rel="noopener" target="_blank" title=")_

### Mesolabe

Let’s explore Descartes’ insights a bit further.

The _mesolabe_ was a compass used by Descartes to find two mean proportionals between two given lines (**YX** and **YZ** below), required in solving the problem of the duplication of the cube.

Follow the steps below to see how Descartes created equations for the dotted lines without using any numbers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NJAKRWWkSxVd2BGfzg_POg@2x.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*bIzuDKWV6U_RriHwQGYDDA.gif)
_3 [Gridmath’s video on YouTube](https://www.instagram.com/vishalkumar.london/" rel="noopener" target="_blank" title="">vishalkumar.london </a>and a GIF of the mesolabe taken from <a href="https://www.youtube.com/watch?v=jhwRBoOK40E&amp;feature=youtu.be&amp;t=3m20s" rel="noopener" target="_blank" title=")_

To describe the dotted line **AD,** Descartes uses the following terminology:

**YA** = **YB** = _a_ ; **YC** = _x_ ; **CD** = _y_ ; **YD** = _z_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dO3ciu7EnI44vxO7Fk9FrQ@2x.png)

Using similar logic, Descartes concludes the below equations for **AF** and **AH**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bneQMewZhTUw9D-Ox_a4yQ@2x.png)

If you’re interested in the calculations behind the algebra and the equations above, especially **AF** and **AH**, I would advise watching Gridmath’s [video at 3m20s](https://youtu.be/jhwRBoOK40E?t=3m20s) to learn more.

### On the nature of curved lines

Throughout _La Geometrie,_ Descartes has a thorough discussion about how curved lines can be used to solve difficult problems:

> “We should always choose with care the simplest curve that can be used in the solution of a problem”

In fact, the _mesolabe_ was an instrument used to solve the famous Greek [Pappus problem](http://www.oxfordscholarship.com/view/10.1093/acprof:oso/9780198242505.001.0001/acprof-9780198242505-chapter-2). Put simply, the task is to identify a curve such that all the points on the curve satisfy a specified relation to the given ratio.

In the below images, we see formations of Descartes’ “geometrical calculus”. In particular, the image below, known as the **folium** (‘leaf’) **of Descartes,** contributed to the [genesis of calculus](https://en.wikipedia.org/wiki/Folium_of_Descartes). It has the equation:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zt-tT3sl_CvQW27rQBUkUg@2x.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PEC1YZjbUS_SDzKYVqOXJg@2x.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IytOIorZ2KpWDNZkAgMR8g.gif)
_Folium of Descartes (left) taken from [code from Fer](https://en.wikipedia.org/wiki/Folium_of_Descartes" rel="noopener" target="_blank" title="">wikipedia</a> and and an artwork of Folium of Descartes I created using an algorithm in p5js adopting <a href="https://www.openprocessing.org/user/74658" rel="noopener" target="_blank" title=")_

Curved lines, and therefore geometry, can be used to **solve a number of** extremely difficult **design problems in the modern day**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cx6n3UFfQJxT56p_CKlxXQ@2x.png)
_Foster and Partners design of Mexico City’s airport through geometric computation — [read the paper here](http://papers.cumincad.org/data/works/att/acadia17_620.pdf" rel="noopener" target="_blank" title=")._

[Foster and Partners](https://www.fosterandpartners.com/), an architectural firm, used **geometric computation and simulation** to [design Mexico City’s new airport](http://papers.cumincad.org/data/works/att/acadia17_620.pdf). Moreover, the algebraic structure of elliptic curves are being used to **design cutting-edge cryptography**, [Elliptic curve cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) ([Keeley Erhardt](https://www.freecodecamp.org/news/what-rene-descartes-can-teach-you-about-design-e0eace2ca268/undefined), thanks for the insight!)

### Conclusion

When Descartes was trying to _design_ a philosophical conceptualisation of the entire universe, he would refer to ancient geometric proofs to reason. As I have demonstrated in this essay, he used algebra as a tool to explain geometry, which helped him understand phenomena in the natural world.

I would like to highlight two major points made in this article:

1. Shapes and forms can be expressed on a coordinate plane using algebra and equations, which is important for design.
2. It is important to understand algebraic geometry, because when designing computationally or via an algorithm, you need to understand how to move the pixels on a screen geometrically using algebra.

I can’t emphasise enough how important it is to understand the underlying theory of a given subset of knowledge. Ancient mathematical theories have allowed me to explore and understand design at a much deeper level — I hope it has for you as well.

Thank you for reading!

#### Before you leave…

If you found this article helpful, hold down the? button and share the article on Facebook, Twitter or LinkedIn so that everyone can benefit from it too.

See more of Vishal’s work on [Instagram](https://www.instagram.com/vishalkumar.london/), [Facebook](https://www.facebook.com/vishalkumar.london/) or on his [website](https://vishalkumar.london/).

_“Curiosity is your greatest gift. Foster that curiosity and eternally remain curious”_ Kareem Dennis, 27th February 2018

