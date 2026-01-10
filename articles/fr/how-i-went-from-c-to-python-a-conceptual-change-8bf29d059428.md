---
title: 'Comment je suis passé du C++ à Python : un changement conceptuel'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T00:03:41.000Z'
originalURL: https://freecodecamp.org/news/how-i-went-from-c-to-python-a-conceptual-change-8bf29d059428
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cJRAtfMPu_7QGFyq2n_FiQ.jpeg
tags:
- name: learning
  slug: learning
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'Comment je suis passé du C++ à Python : un changement conceptuel'
seo_desc: 'By asya f

  Introduction

  People say that coding in Python is so easy that even a 6 year old can do it. This
  was the thought that I had in mind when I started coding in Python at work. I had
  been a full-time software developer for 4 years at that time, ...'
---

Par asya f

### Introduction

Les gens disent que coder en Python est si facile qu'un enfant de 6 ans peut le faire. C'était la pensée que j'avais en tête lorsque j'ai commencé à coder en Python au travail. J'étais développeur logiciel à temps plein depuis 4 ans à cette époque, écrivant principalement en C++ sur Linux, en utilisant intensément la bibliothèque QT. Cependant, j'ai d'abord écrit du mauvais code Python.

Cela fait environ 3 ans que j'ai fait cette transition et je pense que c'est un bon moment pour résumer les progrès que j'ai réalisés pendant cette période. En regardant en arrière, je n'ai pas seulement changé mon langage de programmation principal, mais aussi mon environnement de travail et ma façon de penser le code.

Je ne vais pas entrer dans les détails et les différences entre C++ et Python, car il existe [de nombreuses ressources en ligne](https://www.educba.com/python-vs-c-plus-plus/), mais je vais plutôt décrire mon propre expérience. J'espère que cet article sera utile pour les personnes qui traversent la même transition que moi.

![Image](https://cdn-media-1.freecodecamp.org/images/gJvyoRQiZQyfjylGkcHimNA5Kef78j0DsMxB)
_Sauter de C++ à Python (Photo par [Unsplash](https://unsplash.com/photos/TZ-D7A7Oy0s?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Erik Dungan</a> sur <a href="https://unsplash.com/search/photos/deep-dive?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

### C++ est de la plongée, Python est du snorkeling

C++ ressemble à une plongée dans les mystères magiques de la mer - c'est beau, mais cela nécessite plus d'apprentissage et de pratique, et globalement, la distance que vous parcourez n'est pas si grande. Python ressemble un peu au snorkeling - vous voyez la beauté dès que vous mettez la tête dans l'eau, mais vous ne descendez pas beaucoup plus loin. Vous continuez à nager dans des eaux peu profondes et pouvez parcourir une longue distance facilement. À partir de cette description, il est clair que chacun de ces langages doit être utilisé au bon endroit et au bon moment.

#### Plonger dans C++ et survivre

C++ est plus strict et vous pénalise plus sévèrement pour vos erreurs. Ce n'est pas une session de codage efficace si vous n'avez pas obtenu une surprenante _erreur de segmentation_ au moins une fois. Par conséquent, cela nécessite une compréhension plus approfondie de l'ordinateur, du compilateur et du langage. Lorsque vous allez plus profond, vous pouvez vraiment voir et être impressionné par de belles choses, comme le processus de compilation et la gestion de la mémoire.

En tant que programmeur C++, je me souciais davantage des ajustements de syntaxe et des exemples bizarres. Je savais toujours où j'allouais de la mémoire et comment je la libérais. Les programmes que j'écrivais étaient plus autonomes car je préférais savoir ce qui se passait à l'intérieur de mon code. L'idée principale était que le code écrit par quelqu'un d'autre était moins fiable, plus sujet aux erreurs et pouvait faire exploser votre utilisation de la mémoire.

Mes principaux outils quotidiens étaient **Vim** avec de nombreux plugins pour écrire du code, **GDB** pour le débogage et **Valgrind** pour analyser mon utilisation de la mémoire et les erreurs. Je compilais avec **g++** et écrivais mes propres **Makefiles**. À l'époque, je ne sentais pas qu'un IDE me bénéficierait, mais plutôt qu'il ralentirait les choses et me ferait perdre le contact avec mon code. _En rétrospective, je m'appuyais fortement sur le compilateur pour trouver mes erreurs de type_.

![Image](https://cdn-media-1.freecodecamp.org/images/qq2GvVEIPB16B3NDqru9LJb-vhitY-Ofkzpo)
_Photo par [Unsplash](https://unsplash.com/photos/Td9FnTMHu0A?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jakob Boman</a> sur <a href="https://unsplash.com/search/photos/diving?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### Nager en eaux peu profondes en Python

L'une des premières choses que vous devez apprendre lorsque vous passez à Python est de savoir lâcher prise - vous ne savez pas ce qui se passe sous le capot, où la mémoire est allouée et libérée, et c'est OK. Vous êtes également encouragé à utiliser du code écrit par d'autres, emballé dans des bibliothèques, car cela vous fait gagner du temps et vous aide à coder plus rapidement. Cela ne signifie pas que vous devez écrire du code qui est lentement et repose sur des bibliothèques non maintenues et non fonctionnelles, mais l'accent est définitivement différent.

Lorsque j'ai commencé à coder en Python, j'ai d'abord écrit du code C++ en Python. Cela fonctionnait, mais je n'ai tiré aucun avantage du langage. Mon codage s'est amélioré lorsque j'ai commencé à écrire de manière plus "Pythonique" et à utiliser des bibliothèques, ainsi que des concepts plus avancés tels que les [générateurs](http://book.pythontips.com/en/latest/generators.html), les [décorateurs](http://book.pythontips.com/en/latest/decorators.html) et les [contexte](http://book.pythontips.com/en/latest/context_managers.html).

En tant que développeur Python, je tends à chercher d'abord la bibliothèque qui résout le problème en question. Python dispose d'un riche [écosystème de bibliothèques](https://pypi.org/) et d'une communauté qui le soutient. Il existe des bibliothèques pour faire pratiquement n'importe quoi. Voici quelques-unes que j'utilise quotidiennement : [**NumPy**](http://www.numpy.org/) pour les calculs numériques, [**OpenCV**](https://opencv.org/) pour la vision par ordinateur, [**json**](https://docs.python-guide.org/scenarios/json/) pour lire les fichiers json, [**SciPy**](https://www.scipy.org/scipylib/index.html) pour les calculs scientifiques, [**sqlite3**](https://docs.python.org/3.7/library/sqlite3.html) pour les bases de données.

Mon outil quotidien est **PyCharm** (oui, un IDE) avec le plugin **IdeaVim**. J'ai commencé à l'utiliser principalement en raison du fait que c'est un débogueur puissant, beaucoup plus convivial que le débogueur Python par défaut, **pdb**. J'utilise également **pip** pour installer les bibliothèques dont j'ai besoin. Je ne surveille plus mon utilisation de la mémoire sauf si je dois vraiment le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/RZNJFo27RiO1Azs7Mc-slNCDxvsWrV0A64He)
_Photo par [Unsplash](https://unsplash.com/photos/fYjIBVvUuRM?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Channey</a> sur <a href="https://unsplash.com/search/photos/snorkeling?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Quelques conseils pratiques

Si vous êtes un développeur C++ et que vous envisagez de commencer à coder en Python, voici mes conseils pour vous :

* **Débarrassez-vous des anciennes habitudes** — Arrêtez d'utiliser le compilateur C++ comme débogueur. Ne sur-optimisez pas l'utilisation de la mémoire. Évitez d'écrire du code de type C++. Et surtout, essayez de ne pas vous fier aux types.
* **Prenez de nouvelles habitudes** — Commencez à utiliser des bibliothèques. Écrivez du code Pythonique (mais sans en abuser). Gardez les choses lisibles. Utilisez des concepts plus complexes tels que les générateurs/décorateurs/contexte. Essayez PyCharm.
* **Utilisez des bibliothèques communes à C++ et Python** — Certaines bibliothèques C++, comme OpenCV et QT, ont une interface Python. Il est facile de commencer à utiliser la même bibliothèque en Python plutôt que d'apprendre une nouvelle bibliothèque à partir de zéro.
* **N'oubliez pas vos origines** — Parfois Python est tout simplement trop lent ou pas optimal pour la tâche. C'est là que vos connaissances en C++ interviennent. Il existe de nombreuses façons (**SIP**, **ctypes**, etc.) d'utiliser du code C++ à l'intérieur de Python.

### Conclusion

Peu importe ce que disent les autres, passer à un langage de programmation différent, surtout à un langage qui est fondamentalement différent de celui auquel vous êtes habitué, n'est pas facile. Prenez le temps d'apprendre, de creuser, de découvrir. Mais surtout, comprenez que ce n'est pas seulement le langage qui doit changer, mais aussi votre style de codage et votre méthodologie de travail.

Bonne chance !