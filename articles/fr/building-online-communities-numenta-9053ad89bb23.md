---
title: 'Construction de communautés en ligne : Numenta'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-11T11:22:30.000Z'
originalURL: https://freecodecamp.org/news/building-online-communities-numenta-9053ad89bb23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dxRIVyhf8oU4jwe16F12Uw.png
tags:
- name: brain
  slug: brain
- name: Machine Learning
  slug: machine-learning
- name: open source
  slug: open-source
seo_title: 'Construction de communautés en ligne : Numenta'
seo_desc: 'By Gitter

  We caught up with Matt Taylor from Numenta — an organization whose mission is to
  lead a new era of machine intelligence and build computer systems around the principles
  of the brain. Matt shared his thoughts and insights on the open source ...'
---

Par Gitter

_Nous avons discuté avec [Matt Taylor](https://twitter.com/rhyolight) de [Numenta](http://numenta.com/) — une organisation dont la mission est de diriger une nouvelle ère d'intelligence machine et de construire des systèmes informatiques autour des principes du cerveau. Matt a partagé ses pensées et ses perspectives sur la communauté open source autour de leurs projets passionnants. Découvrez ce qu'il dit et consultez le canal communautaire [Numenta](https://gitter.im/numenta/public) sur [Gitter](http://gitter.im)._

**Parlez-nous un peu de vous et de la communauté Numenta. Comment tout a commencé ?**

Je suis le _Porte-drapeau de la Communauté Open Source_ pour Numenta (auto-proclamé ?). Numenta existe depuis plus de 10 ans, principalement en tant qu'organisation de recherche et développement. Notre double mission est de **comprendre les principes de fonctionnement du néocortex** et de **construire des systèmes informatiques basés sur ces principes.** Ce sont des objectifs assez ambitieux, ce qui explique pourquoi une petite "startup" comme la nôtre existe depuis si longtemps !

Une fois que nous avions établi certains algorithmes fondamentaux basés sur le néocortex qui semblaient réellement fonctionner, nous avons ouvert notre code source sous la licence AGPLv3 dans l'intention de le monétiser éventuellement en licenciant notre technologie. Cette technologie s'appelle **Hierarchical Temporal Memory (HTM)**, et nous avons plusieurs implémentations logicielles dans différents environnements au sein de notre base de code communautaire. Les plus populaires d'entre elles sont [**NuPIC**](https://github.com/numenta/nupic) (Numenta Platform for Intelligent Computing), qui est une base de code Python / C++, et [**HTM.Java**](https://github.com/numenta/htm.java) pour la JVM. Il existe également une implémentation Clojure créée par la communauté qui est encore dans un état de "recherche".

**Quels sont les principaux sujets discutés dans le canal Numenta ?**

La plupart des discussions portent sur la théorie HTM et les détails techniques de nos implémentations open source HTM. HTM est un sujet profond, donc beaucoup de gens viennent avec des questions sur le pooling spatial, l'algorithme de mémoire temporelle ou les classificateurs. Il semble toujours y avoir quelqu'un pour répondre à leurs questions si je ne suis pas là, ce qui est génial. C'est bien d'avoir quelques experts dédiés qui fréquentent le canal pour engager les gens et construire des relations même quand je ne suis pas là.

Nous discutons également du développement en cours des bases de code, des problèmes qui sont résolus et des rapports de bugs. Il y a aussi une bonne dose de support technique où nous aidons les gens à se lancer avec NuPIC et HTM.Java.

Et comme nous avons une communauté si amicale et diverse, nous avons de nombreuses discussions hors sujet et futiles simplement pour nous divertir. Je pense que la dernière portait sur les [Kanji](https://en.wikipedia.org/wiki/Kanji) ou les [vélos couchés](http://m5ligfietsen.nl/site/EN/Models/M-Racer).

**Quels sont les objectifs communs que vous avez en tant que communauté ?**

Je pense qu'il y a deux objectifs communs dans notre communauté. Le premier est de **construire des applications cool en utilisant la technologie HTM** qui existe dans les logiciels aujourd'hui. Le second est de **continuer à faire évoluer la théorie HTM** afin que davantage de caractéristiques du néocortex et de l'intelligence générale puissent être ajoutées au logiciel au fil du temps. Nous modélisons actuellement une couche d'une région du cortex, jusqu'à 65 000 neurones environ, mais les développements futurs de HTM construiront des hiérarchies de ces régions ainsi qu'ajouteront plus de couches aux régions pour soutenir les développements à venir comme l'intégration sensorimotrice, le feedback et l'attention. L'avenir de cette technologie est très prometteur, étant donné que nous pouvons faire des choses intéressantes avec un ensemble si limité de neurones aujourd'hui.

**Quels sont les facteurs les plus importants que vous avez pris en compte lors de la création et de la maintenance de la communauté ? Quels facteurs contribuent au succès de votre communauté ?**

Deux choses : _la transparence_ et _l'inclusion_.

Numenta et moi avons commencé à construire cette communauté lorsque nous avons **ouvert notre code source en juin 2013**. Dès le début, nous avons mis l'accent sur la transparence. Depuis le jour où j'ai commencé en tant que Porte-drapeau de la Communauté OS chez Numenta, je m'efforce de garantir que nous, en tant qu'entreprise, soyons très ouverts sur notre technologie et nos projets futurs. Nous organisons régulièrement des [HTM Hackers' Hangouts](https://www.youtube.com/playlist?list=PL3yXMgtrZmDogxgQa_dKsuWj-0Wi_UZlJ) en ligne où n'importe qui dans notre communauté peut rejoindre et discuter en vidéo avec les ingénieurs de Numenta. Nous organisons également des [Office Hours](https://www.youtube.com/watch?v=MWBFw4WoZxA&list=PL3yXMgtrZmDqsqo6hytKjhrkfFNEYDqfn) en ligne avec notre fondateur **Jeff Hawkins** et le VP de la Recherche **Subutai Ahmad** tous les quelques mois, permettant aux gens de leur poser des questions directement. Tout cela est publié sur notre [chaîne YouTube](http://www.youtube.com/channel/UC8-ttzWLgXZOGuhUyrPlUuA). Nous avons même rendu notre [code de recherche open source](http://numenta.com/blog/increasing-research-transparency.html), afin que tout le monde puisse voir exactement sur quels algorithmes nous travaillons avant qu'ils ne deviennent grand public.

Beaucoup de personnes de tous horizons s'intéressent au développement des technologies de calcul cognitif comme HTM, donc nous avons un mélange sain de personnalités diverses dans notre communauté. J'ai donc essayé dès le début de rendre notre travail aussi accessible et abordable que possible, permettant aux profanes de s'impliquer de manière que d'autres projets très techniques ne peuvent pas. Nous avons des opportunités pour les membres de la communauté d'aider avec la documentation, les rapports de bugs, la relecture, etc. Ce n'est pas seulement pour les scientifiques et les ingénieurs. Nous avons des personnes de tous horizons : des lycéens, des octogénaires, des neuroscientifiques, des ingénieurs informatiques, des professeurs, des étudiants, des philosophes, etc. Je veux rendre notre communauté attrayante pour tout le monde.

**Quels sont les principaux défis que vous rencontrez lors de la gestion de la communauté ?**

Il peut être difficile de reconnaître sur quoi travaillent différentes personnes et d'où elles viennent. Notre communauté voit beaucoup de nouveaux visages, et certains d'entre eux sont brillants et font des choses vraiment intéressantes. Mais il est parfois difficile de savoir qui travaille sur quoi.

La technologie HTM a une courbe d'apprentissage abrupte, et elle est encore très nouvelle. Le logiciel lui-même peut être difficile à installer sur tous les systèmes d'exploitation (Python avec des extensions C++ ?). Nous avons beaucoup de gens dans notre communauté qui apprennent à programmer _juste pour pouvoir travailler avec les HTM_. L'un de mes principaux défis est de rendre notre technologie et notre pile technologique plus accessibles. Nous avons parcouru un long chemin depuis que nous avons commencé en 2013, mais il y a toujours plus à faire ! Je produis actuellement une série de vidéos YouTube appelée [HTM School](https://www.youtube.com/playlist?list=PL3yXMgtrZmDqhsFQzwUC9V8MeeVOQ7eZ9) pour aider à éduquer les gens sur les concepts HTM dès le début. J'espère que des choses comme cela m'aideront à répondre aux questions sur nos listes de diffusion concernant la théorie HTM. Et oh, au fait, la façon dont les vidéos YouTube s'intègrent dans Gitter est géniale ! ?

**Comment encouragez-vous l'engagement et la contribution des participants à la communauté ?**

Si quelqu'un veut travailler sur du code, nous avons une [pile de problèmes pour débutants](https://github.com/numenta/nupic/labels/newbie) qui sont assez non menaçants, bien qu'il serait utile de connaître un peu Python. Nous avons également des personnes qui écrivent des traductions de nos livres blancs, ce qui est très utile pour éduquer dans d'autres langues.

Je **ne décourage jamais les gens fous**. Nous n'avons pas découvert toutes les façons d'encoder différentes données en SDR pour que les HTM les consomment, donc j'attends juste que quelqu'un construise quelque chose qui me souffle. Je pense que le meilleur moyen d'accélérer cela est de partager des idées et d'encourager les gens à construire des choses étranges et intéressantes. Il y a beaucoup de personnes très créatives dans notre communauté. Certains pourraient les appeler fous, mais je sais qu'un certain pourcentage d'entre eux sont des **purs génies**.

**Sur la base de votre expérience, pensez-vous que les communautés open source ont changé et évolué au fil des années ? Si oui, comment ?**

Je pense que la communication en face à face est très importante pour les personnes actives dans la communauté. Votre visage contient beaucoup d'informations qui augmentent la communication vocale. Plus les gens se voient, plus ils se sentent proches. L'émergence de meilleurs outils de vidéoconférence a rendu beaucoup plus facile le maintien de la cohésion d'une communauté. Nous publions des réunions en ligne régulières où n'importe qui dans la communauté peut rejoindre et exprimer ses opinions et idées. Tout cela est publié sur notre chaîne YouTube, et je peux voir à quel point les gens sont engagés par le nombre de vues qu'ils obtiennent. Avoir la capacité de réunir les gens dans une conversation comme celle-ci et de publier l'ensemble en direct sur Internet est incroyable. C'est très cool de rencontrer quelqu'un lors d'un événement et de le reconnaître grâce aux réunions YouTube !

Gitter a également été très utile, surtout la façon dont il se connecte directement à toutes nos bases de code OS et nous donne un espace pour discuter du code de manière beaucoup plus personnelle qu'un problème Github.

**Quel conseil donneriez-vous à quelqu'un qui veut créer une communauté open source en ligne à partir de zéro ?**

Soit être un extraverti, soit être très bon pour faire semblant d'être un extraverti. ?