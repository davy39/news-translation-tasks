---
title: Que peut-on exactement faire avec Python ? Voici les 3 principales applications
  de Python.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-15T02:04:10.000Z'
originalURL: https://freecodecamp.org/news/what-can-you-do-with-python-the-3-main-applications-518db9a68a78
coverImage: https://cdn-media-1.freecodecamp.org/images/0*lBhKdwfBlmWAPQFd
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: Que peut-on exactement faire avec Python ? Voici les 3 principales applications
  de Python.
seo_desc: 'By YK Sugi

  If you’re thinking of learning Python — or if you recently started learning it —
  you may be asking yourself:


  “What exactly can I use Python for?”


  Well that’s a tricky question to answer, because there are so many applications
  for Python....'
---

Par YK Sugi

Si vous pensez apprendre Python — ou si vous avez récemment commencé à l'apprendre — vous vous demandez peut-être :

> **« À quoi puis-je exactement utiliser Python ? »**

Eh bien, c'est une question difficile à répondre, car il existe de nombreuses applications pour Python.

Mais avec le temps, j'ai observé qu'il existe 3 applications principales populaires pour Python :

* Développement Web
* Science des données — incluant l'apprentissage automatique, l'analyse de données et la visualisation de données
* Scripting

Parlons de chacune d'elles à tour de rôle.

### **Développement Web**

Les frameworks web basés sur Python comme **Django** et **Flask** sont récemment devenus très populaires pour le développement web.

Ces frameworks web vous aident à créer du code côté serveur (code backend) en Python. C'est le code qui s'exécute sur votre serveur, par opposition aux appareils et navigateurs des utilisateurs (code front-end). Si vous n'êtes pas familier avec la différence entre le code backend et le code front-end, veuillez consulter ma note de bas de page ci-dessous.

#### **Mais attendez, pourquoi ai-je besoin d'un framework web ?**

C'est parce qu'un framework web facilite la création de la logique backend commune. Cela inclut la mise en correspondance de différentes URL avec des morceaux de code Python, la gestion des bases de données et la génération de fichiers HTML que les utilisateurs voient sur leurs navigateurs.

#### **Quel framework web Python devrais-je utiliser ?**

Django et Flask sont deux des frameworks web Python les plus populaires. Je vous recommande d'utiliser l'un d'eux si vous débutez.

#### **Quelle est la différence entre Django et Flask ?**

Il y a un [excellent article](https://www.codementor.io/garethdwyer/flask-vs-django-why-flask-might-be-better-4xs7mdf8v) sur ce sujet par Gareth Dwyer, alors laissez-moi le citer ici :

**_<début de citation>_**

Contrastes principaux :

* Flask offre simplicité, flexibilité et contrôle fin. Il est non opinionné (il vous laisse décider comment vous voulez implémenter les choses).
* Django offre une expérience tout-en-un : vous obtenez un panneau d'administration, des interfaces de base de données, un [ORM (mappage objet-relationnel)](https://stackoverflow.com/questions/1279613/what-is-an-orm-and-where-can-i-learn-more-about-it), et une structure de répertoire pour vos applications et projets dès le départ.

Vous devriez probablement choisir :

* Flask, si vous êtes concentré sur l'expérience et les opportunités d'apprentissage, ou si vous voulez plus de contrôle sur les composants à utiliser (comme les bases de données que vous voulez utiliser et comment vous voulez interagir avec elles).
* Django, si vous êtes concentré sur le produit final. Surtout si vous travaillez sur une application simple comme un site d'actualités, une boutique en ligne ou un blog, et que vous voulez qu'il y ait toujours une seule façon évidente de faire les choses.

**_</fin de citation>_**

En d'autres termes, si vous êtes débutant, Flask est probablement un meilleur choix car il a moins de composants à gérer. De plus, Flask est un meilleur choix si vous voulez plus de personnalisation.

D'un autre côté, si vous cherchez à construire quelque chose de simple, Django vous permettra probablement d'y parvenir plus rapidement.

Maintenant, si vous cherchez à apprendre Django, je recommande le livre appelé Django pour les débutants. Vous pouvez le trouver [ici](http://csdojo.io/dj).

Vous pouvez également trouver les chapitres d'exemple gratuits de ce livre [ici](https://djangoforbeginners.com/).

D'accord, passons au sujet suivant !

### **Science des données — incluant l'apprentissage automatique, l'analyse de données et la visualisation de données**

#### **Tout d'abord, revoyons ce qu'est l'apprentissage automatique.**

Je pense que la meilleure façon d'expliquer ce qu'est l'apprentissage automatique est de vous donner un exemple simple.

Supposons que vous voulez développer un programme qui détecte automatiquement ce qu'il y a dans une image.

Donc, étant donné cette image ci-dessous (Image 1), vous voulez que votre programme reconnaisse qu'il s'agit d'un chien.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Mbj3L2cl0zzT2A0L)
_Image 1_

Étant donné cette autre image ci-dessous (Image 2), vous voulez que votre programme reconnaisse qu'il s'agit d'une table.

![Image](https://cdn-media-1.freecodecamp.org/images/0*gxTn_CbMyCcQ1NFV)
_Image 2_

Vous pourriez dire, eh bien, je peux simplement écrire du code pour faire cela. Par exemple, peut-être que s'il y a beaucoup de pixels marron clair dans l'image, alors nous pouvons dire que c'est un chien.

Ou peut-être, vous pouvez trouver comment détecter les bords dans une image. Ensuite, vous pourriez dire, s'il y a beaucoup de bords droits, alors c'est une table.

Cependant, ce type d'approche devient rapidement compliqué. Et si un chien blanc apparaît dans l'image sans poils marron ? Et si l'image ne montre que les parties rondes de la table ?

**C'est là que l'apprentissage automatique intervient.**

L'apprentissage automatique met généralement en œuvre un algorithme qui détecte automatiquement un motif dans l'entrée donnée.

Vous pouvez donner, par exemple, 1 000 images de chiens et 1 000 images de tables à un algorithme d'apprentissage automatique. Ensuite, il apprendra la différence entre un chien et une table. Lorsque vous lui donnerez une nouvelle image d'un chien ou d'une table, il sera capable de reconnaître laquelle c'est.

Je pense que cela ressemble un peu à la façon dont un bébé apprend de nouvelles choses. Comment un bébé apprend-il qu'une chose ressemble à un chien et une autre à une table ? Probablement à partir d'une série d'exemples.

Vous ne dites probablement pas explicitement à un bébé, « Si quelque chose est poilu et a des poils marron clair, alors c'est probablement un chien. »

Vous diriez probablement simplement, « C'est un chien. Cela aussi est un chien. Et cela est une table. Cela aussi est une table. »

Les algorithmes d'apprentissage automatique fonctionnent de la même manière.

Vous pouvez appliquer la même idée à :

* les systèmes de recommandation (pensez à YouTube, Amazon et Netflix)
* la reconnaissance faciale
* la reconnaissance vocale

parmi d'autres applications.

Les algorithmes d'apprentissage automatique populaires que vous avez peut-être entendus incluent :

* Réseaux de neurones
* Apprentissage profond
* Machines à vecteurs de support
* Forêt aléatoire

Vous pouvez utiliser l'un des algorithmes ci-dessus pour résoudre le problème d'étiquetage d'images que j'ai expliqué précédemment.

#### **Python pour l'apprentissage automatique**

Il existe des bibliothèques et frameworks populaires d'apprentissage automatique pour Python.

Deux des plus populaires sont **scikit-learn** et **TensorFlow**.

* scikit-learn vient avec certains des algorithmes d'apprentissage automatique les plus populaires intégrés. J'en ai mentionné certains ci-dessus.
* TensorFlow est plus une bibliothèque de bas niveau qui vous permet de construire des algorithmes d'apprentissage automatique personnalisés.

Si vous débutez avec un projet d'apprentissage automatique, je vous recommande de commencer par scikit-learn. Si vous commencez à rencontrer des problèmes d'efficacité, alors je commencerais à explorer TensorFlow.

#### **Comment devrais-je apprendre l'apprentissage automatique ?**

Pour apprendre les fondamentaux de l'apprentissage automatique, je recommande soit le cours d'apprentissage automatique de [Stanford](https://www.coursera.org/learn/machine-learning) soit celui de [Caltech](https://work.caltech.edu/telecourse.html).

Veuillez noter que vous avez besoin de connaissances de base en calcul et en algèbre linéaire pour comprendre certains des matériaux dans ces cours.

Ensuite, je pratiquerais ce que vous avez appris dans l'un de ces cours avec [Kaggle](https://www.kaggle.com/). C'est un site où les gens concourent pour construire le meilleur algorithme d'apprentissage automatique pour un problème donné. Ils ont également de bons tutoriels pour les débutants.

### **Qu'en est-il de l'analyse de données et de la visualisation de données ?**

Pour vous aider à comprendre à quoi cela pourrait ressembler, laissez-moi vous donner un exemple simple ici.

Supposons que vous travaillez pour une entreprise qui vend des produits en ligne.

Ensuite, en tant qu'analyste de données, vous pourriez tracer un graphique à barres comme celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*62T-rtheKPehgZdPTEpKww.png)
_Graphique à barres 1 — généré avec Python_

À partir de ce graphique, nous pouvons voir que les hommes ont acheté plus de 400 unités de ce produit et les femmes environ 350 unités de ce produit ce dimanche particulier.

En tant qu'analyste de données, vous pourriez proposer quelques explications possibles pour cette différence.

Une explication possible évidente est que ce produit est plus populaire auprès des hommes que des femmes. Une autre explication possible pourrait être que la taille de l'échantillon est trop petite et que cette différence a été causée simplement par hasard. Et une autre explication possible pourrait être que les hommes tendent à acheter ce produit davantage seulement le dimanche pour une raison quelconque.

Pour comprendre laquelle de ces explications est correcte, vous pourriez tracer un autre graphique comme celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VgNfqK5XxNfHxx6S4VFCjQ.png)
_Graphique linéaire 1 — généré avec Python_

Au lieu de montrer les données pour le dimanche seulement, nous regardons les données pour une semaine complète. Comme vous pouvez le voir, à partir de ce graphique, nous pouvons voir que cette différence est assez constante sur différents jours.

À partir de cette petite analyse, vous pourriez conclure que l'explication la plus convaincante pour cette différence est que ce produit est simplement plus populaire auprès des hommes que des femmes.

D'un autre côté, que se passe-t-il si vous voyez un graphique comme celui-ci à la place ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*dMpu_fd-THNXRJhHIq2O3g.png)
_Graphique linéaire 2 — également généré avec Python_

Alors, qu'est-ce qui explique la différence du dimanche ?

Vous pourriez dire, peut-être que les hommes tendent à acheter davantage ce produit seulement le dimanche pour une raison quelconque. Ou peut-être que c'était simplement une coïncidence que les hommes en aient acheté davantage ce dimanche-là.

Donc, voici un exemple simplifié de ce à quoi pourrait ressembler l'analyse de données dans le monde réel.

Le travail d'analyse de données que j'ai fait lorsque je travaillais chez Google et Microsoft était très similaire à cet exemple — seulement plus complexe. J'ai en fait utilisé Python chez Google pour ce type d'analyse, tandis que j'ai utilisé JavaScript chez Microsoft.

J'ai utilisé SQL dans les deux entreprises pour extraire des données de nos bases de données. Ensuite, j'utilisais soit Python et Matplotlib (chez Google) soit JavaScript et D3.js (chez Microsoft) pour visualiser et analyser ces données.

#### **Analyse de données / visualisation avec Python**

L'une des bibliothèques les plus populaires pour la visualisation de données est [Matplotlib](https://matplotlib.org/).

C'est une bonne bibliothèque pour commencer car :

* Elle est facile à prendre en main
* Certaines autres bibliothèques comme [seaborn](https://seaborn.pydata.org/) sont basées sur elle. Donc, apprendre Matplotlib vous aidera à apprendre ces autres bibliothèques plus tard.

**Comment devrais-je apprendre l'analyse de données / visualisation avec Python ?**

Vous devriez d'abord apprendre les fondamentaux de l'analyse de données et de la visualisation. Lorsque j'ai cherché de bonnes ressources pour cela en ligne, je n'en ai pas trouvé. Donc, j'ai fini par faire une vidéo YouTube sur ce sujet :

J'ai également fini par faire un [cours complet sur ce sujet sur Pluralsight](https://goo.gl/fZ5oVX), que vous pouvez suivre gratuitement en vous inscrivant à leur essai gratuit de 10 jours.

Je recommande les deux.

Après avoir appris les fondamentaux de l'analyse de données et de la visualisation, apprendre les fondamentaux de la statistique sur des sites comme Coursera et Khan Academy sera également utile.

### **Scripting**

#### **Qu'est-ce que le scripting ?**

Le scripting fait généralement référence à l'écriture de petits programmes conçus pour automatiser des tâches simples.

Alors, laissez-moi vous donner un exemple de mon expérience personnelle ici.

Je travaillais autrefois dans une petite startup au Japon où nous avions un système de support par e-mail. C'était un système pour nous permettre de répondre aux questions que les clients nous envoyaient par e-mail.

Lorsque je travaillais là-bas, j'avais la tâche de compter le nombre d'e-mails contenant certains mots-clés afin que nous puissions analyser les e-mails que nous recevions.

Nous aurions pu le faire manuellement, mais au lieu de cela, j'ai écrit un simple programme / un simple script pour automatiser cette tâche.

En fait, nous utilisions Ruby pour cela à l'époque, mais Python est également un bon langage pour ce type de tâche. Python est adapté à ce type de tâche principalement parce qu'il a une syntaxe relativement simple et est facile à écrire. Il est également rapide d'écrire quelque chose de petit avec et de le tester.

### **Qu'en est-il des applications embarquées ?**

Je ne suis pas un expert en applications embarquées, mais je sais que Python fonctionne avec Raspberry Pi. Cela semble être une application populaire parmi les amateurs de matériel.

### **Qu'en est-il du gaming ?**

Vous pourriez utiliser la bibliothèque appelée PyGame pour développer des jeux, mais ce n'est pas le moteur de jeu le plus populaire. Vous pourriez l'utiliser pour construire un projet de loisir, mais personnellement, je ne le choisirais pas si vous êtes sérieux au sujet du développement de jeux.

Plutôt, je recommande de commencer avec Unity avec C#, qui est l'un des moteurs de jeu les plus populaires. Il vous permet de construire un jeu pour de nombreuses plateformes, y compris Mac, Windows, iOS et Android.

### **Qu'en est-il des applications de bureau ?**

Vous pourriez en créer une avec Python en utilisant Tkinter, mais cela ne semble pas être le choix le plus populaire non plus.

Au lieu de cela, il semble que des langages comme [Java, C# et C++](https://www.quora.com/What-is-the-best-programming-language-to-develop-a-desktop-application-It-should-be-cross-platform-free-easy-to-learn-and-have-a-good-community) soient plus populaires pour cela.

Récemment, certaines entreprises ont commencé à utiliser JavaScript pour créer des applications de bureau également.

[Par exemple, l'application de bureau de Slack a été construite avec quelque chose appelé Electron](https://slack.engineering/building-hybrid-applications-with-electron-dc67686de5fb). Il vous permet de construire des applications de bureau avec JavaScript.

Personnellement, si je construisais une application de bureau, j'opterais pour une option JavaScript. Cela vous permet de réutiliser une partie du code d'une version web si vous en avez une.

Cependant, je ne suis pas non plus un expert en applications de bureau, alors s'il vous plaît faites-moi savoir dans un commentaire si vous êtes en désaccord ou d'accord avec moi sur ce point.

### **Python 3 ou Python 2 ?**

Je recommande Python 3 car il est plus moderne et c'est une option plus populaire à ce stade.

### **Note de bas de page : Une note sur le code backend vs le code front-end (au cas où vous ne seriez pas familier avec les termes) :**

Supposons que vous voulez créer quelque chose comme Instagram.

Alors, vous devriez créer du code front-end pour chaque type d'appareil que vous voulez supporter.

Vous pourriez utiliser, par exemple :

* Swift pour iOS
* Java pour Android
* JavaScript pour les navigateurs web

Chaque ensemble de code s'exécutera sur chaque type d'appareil / navigateur. Ce sera l'ensemble de code qui déterminera à quoi ressemblera la disposition de l'application, à quoi ressembleront les boutons lorsque vous cliquerez dessus, etc.

Cependant, vous aurez toujours besoin de la capacité de stocker les informations et les photos des utilisateurs. Vous voudrez les stocker sur votre serveur et pas seulement sur les appareils de vos utilisateurs afin que les abonnés de chaque utilisateur puissent voir ses photos.

C'est là que le code backend / code côté serveur intervient. Vous devrez écrire du code backend pour faire des choses comme :

* Garder une trace de qui suit qui
* Compresser les photos pour qu'elles ne prennent pas autant d'espace de stockage
* Recommander des photos et de nouveaux comptes à chaque utilisateur dans la fonctionnalité _découverte_

Donc, c'est la différence entre le code backend et le code front-end.

D'ailleurs, Python n'est pas le seul bon choix pour écrire du code backend / côté serveur. Il existe de nombreuses autres options populaires, y compris Node.js, qui est basé sur JavaScript.

### Vous avez aimé cet article ? Alors, vous pourriez aussi aimer ma chaîne YouTube.

J'ai une chaîne YouTube d'éducation à la programmation appelée [CS Dojo](https://www.youtube.com/csdojo) avec plus de 440 000 abonnés, où je produis plus de contenu comme cet article.

Par exemple, vous pourriez aimer ces vidéos :

#### En tout cas, merci beaucoup d'avoir lu mon article !