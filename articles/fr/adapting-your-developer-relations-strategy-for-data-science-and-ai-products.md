---
title: Comment adapter votre stratégie de relations avec les développeurs pour les
  produits de data science et d'IA
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-20T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/adapting-your-developer-relations-strategy-for-data-science-and-ai-products
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0c4740569d1a4ca4aa1.jpg
tags:
- name: AI
  slug: ai
- name: Data Science
  slug: data-science
seo_title: Comment adapter votre stratégie de relations avec les développeurs pour
  les produits de data science et d'IA
seo_desc: 'By David Nugent

  The global market for artificial intelligence products is supposed to grow roughly
  10 times by 2025 to almost $120 billion, according to market research firm Tractica.
  Many companies are attempting to capture that market, including IB...'
---

Par David Nugent

Le marché mondial des produits d'intelligence artificielle devrait croître d'environ 10 fois d'ici 2025 pour atteindre près de 120 milliards de dollars, selon le cabinet d'études de marché Tractica. De nombreuses entreprises tentent de capturer ce marché, y compris IBM avec sa suite d'outils de développement Watson [suite d'outils de développement](https://www.ibm.com/watson/developer/?cm_mmc=OSocial_Blog-_-Developer_IBM+Developer-_-WW_WW-_-OInfluencer-Dev-DN-container-devrel&cm_mmca1=000037FD&cm_mmca2=10010797). 

J'ai parlé à mon collègue Upkar Lidder de la manière d'adapter une stratégie de relations avec les développeurs aux générations actuelles et futures de produits d'IA destinés aux développeurs.

![Upkar speaking](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/speaker.jpg)

Upkar Lidder est un développeur full-stack et un data wrangler avec une décennie d'expérience de développement dans divers rôles. Il parle lors de diverses conférences et participe à des groupes technologiques locaux et à des meetups. Upkar a fait ses études supérieures au Canada et réside actuellement aux États-Unis.

### Q : Vous avez travaillé avec des développeurs travaillant sur tous types de projets d'IA, des tutoriels simples de style 101 aux clients mettant en œuvre des systèmes énormes. En quoi le développement de l'IA diffère-t-il de la programmation plus conventionnelle ?

Il y a beaucoup d'apprentissage, d'essais et d'expérimentation avec l'IA et le machine learning. Les objectifs des projets d'IA peuvent être vagues : « réduire le nombre de plaintes des clients », par exemple.

En comparaison, les exigences des utilisateurs en développement logiciel classique peuvent ressembler à « donnez-moi une boîte de dialogue avec un bouton dessus » — spécifiques et bien définies. Bien sûr, il y a beaucoup de recherche utilisateur et de design qui vont dans les spécifications logicielles pour en arriver là, et en tant que développeur, vous travaillez selon ces spécifications. Au contraire, en tant que data scientist, on peut vous pointer vers un ensemble de données non structurées, puis le vrai plaisir commence : vous commencez à l'explorer ! J'adore l'aspect data-wrangling du développement de l'IA. Vous pouvez entrer dans un Jupyter Notebook et commencer à explorer des valeurs aberrantes spécifiques, des formes de données, des types de données, et voir comment les données apparaissent à travers différentes représentations visuelles.

Ensuite, vous prenez des décisions. Que faire avec les valeurs manquantes ? Comment cela va-t-il affecter mon résultat projeté ? Même dans ces deux premières étapes, il y a beaucoup d'inconnues. En développement logiciel, de nombreux programmeurs suivent un chemin bien tracé que leurs collègues et prédécesseurs ont pavé depuis des décennies. En data science, vous avez une période exploratoire où vous essayez de trouver un chemin à prendre. Une fois que vous avez terminé le nettoyage et la transformation, vous choisissez une technique de modélisation appropriée et poursuivez votre analyse. Beaucoup de cette exploration est brute force. XKCD a ma bande dessinée préférée sur la data science.

![data science cartoon](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/cartoon.jpg)

Comme je l'ai dit, une partie de la data science est simplement brute force. Même avec des bibliothèques et des frameworks d'aide, vous devez esquisser vous-même un point de départ éduqué et laisser la bibliothèque faire beaucoup du reste par elle-même. Ensuite, vous analyserez comment les résultats se comparent à vos autres algorithmes de référence et répéterez la procédure.

### Q : Cela soulève la question : Comment expliquez-vous votre projet et votre modèle aux utilisateurs non techniques ?

C'est une excellente question : à quel point voulez-vous être capable d'expliquer votre processus de pensée et vos décisions aux utilisateurs métiers ? Certains modèles comme les arbres de décision sont faciles à expliquer, alors que quelque chose construit avec des réseaux de neurones ou des modèles d'ensemble, vos modèles peuvent devenir plus compliqués et plus difficiles à expliquer. Comparez cela au développement logiciel traditionnel : sauf pour quelques bugs délicats, des problèmes d'explication comme celui-ci ne se produisent tout simplement pas.

Maintenant, avec les systèmes plus avancés comme [AutoAI](https://www.ibm.com/cloud/watson-studio/autoai?cm_mmc=OSocial_Blog-_-Developer_IBM+Developer-_-WW_WW-_-OInfluencer-Dev-DN-ai-devrel-upkar&cm_mmca1=000037FD&cm_mmca2=10010797), vous donnez les données au système, et il prendra en charge plus de travail lourd pour vous. Par exemple, je travaille avec certains data scientists sur un projet analysant les scores NPS pour certains départements internes. Nous construisons un système où, lors d'un appel de support, le système peut identifier des drapeaux rouges dans l'appel qui montrent qu'il « va mal » et alerter un manager pendant que l'appel est encore en cours. Nous avons accès à des points de données tels que la durée de l'appel, le niveau du client et l'analyse des sentiments, donc nous pouvons utiliser ces données pour signaler automatiquement les problèmes avant qu'ils n'explosent. Intéressamment, nous avons essayé d'exécuter AutoAI sur les données — les data scientists ne l'ont pas aimé ! Le principal problème est qu'il peut être un peu une « boîte noire », et les scientifiques voulaient pouvoir expliquer comment ils sont arrivés à leurs conclusions.

Dans l'enquête annuelle sur la data science, l'un des plus grands écarts en data science est les compétences. Donc, d'une part, nous avons besoin de systèmes de boîte noire comme celui-ci où vous n'avez pas besoin d'avoir un doctorat en mathématiques pour comprendre pourquoi le système fonctionne ; il effectuera l'ingénierie des caractéristiques, l'[optimisation des hyperparamètres](https://en.wikipedia.org/wiki/Hyperparameter_optimization) — en même temps, les data scientists ne lui font pas entièrement confiance.

![People listening](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/listening.jpg)

### Q : Vous travaillez chez IBM depuis quelques années. Que faisiez-vous avant de vous lancer dans l'IA, et comment avez-vous fait la transition ?

J'ai rejoint le groupe de support chez IBM, donc je recevais des appels de clients du monde entier avec des problèmes et j'essayais de les aider. J'étais de niveau 2-3, donc les problèmes m'étaient escaladés. Donc les clients étaient déjà en colère quand ils me parlaient ! À bien des égards, je pense que le rôle initial était similaire à ce que je fais maintenant. Je parle avec les développeurs et j'essaie de comprendre comment les aider, même si je m'approche de cela d'un point de vue éducatif plus que de support. Ensuite, j'étais développeur Java, construisant des produits avec Eclipse. De là, je suis passé à un rôle technique orienté client travaillant sur des projets clients, très différent du développement de produits. De là, je suis devenu un responsable fonctionnel, ce qui est essentiellement un rôle de gestion de projet. J'avais une équipe de développeurs avec laquelle je travaillais pour définir des solutions et m'assurer qu'elles étaient livrées à temps. Après deux ans de cela, je suis passé dans le DevRel.

Avant de travailler dans les relations avec les développeurs, j'aimais encadrer des étudiants de coding school et de bootcamp à côté ; donc quand ce travail de relations avec les développeurs est apparu, j'ai pensé, « Wow, ce serait génial de faire cela comme travail et d'être payé pour cela ! »

![IBM booth](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/ibmbooth.jpg)

### Q : Vous avez précédemment défendu des produits et des technologies comme les APIs et l'architecture serverless. Quelles nouvelles tactiques avez-vous développées pour parler de l'IA et du machine learning ?

Avec l'IA/ML, vous devez _faire_ — moins parler, plus _faire_. Pour d'autres sujets de développement logiciel comme le serverless, vous pouvez avoir une conférence plus longue et ensuite passer à une démonstration. Avec l'IA/ML, il y a un accent sur l'expérimentation. Vous devez mettre les mains dans le cambouis ou cela ne fonctionnera pas. J'adore Jupyter Notebook car vous pouvez faire quelque chose, voir la causalité, voir le résultat, et seulement ensuite réfléchir au pourquoi.

J'ai l'impression qu'il y a plus de théorie abstraite, de mathématiques et d'intuition derrière la data science. Vous pouvez toujours mémoriser une formule, mais pour pouvoir avoir une intuition sur quelque chose, c'est idéal. Et cela vient de l'expérimentation. Grâce à la visualisation et au traçage, vous pouvez comprendre les mathématiques derrière les différents concepts de data science. Comparez cela avec quelque chose de plus orienté DevOps — c'est une approche différente. Donc, dans les relations avec les développeurs en data science et en IA, vous devez vous assurer que les participants font quelque chose et sont engagés. Sinon, vous les perdez très vite — parce qu'il y a des mathématiques impliquées !

L'une des choses qui a fonctionné pour moi est de consacrer beaucoup de temps à mes ateliers, en expliquant chaque étape en détail. Dans mes diapositives, j'utilise des flèches, des rectangles annotés et autres pour m'assurer que les étudiants peuvent suivre facilement et naturellement. Lorsque j'enseigne Jupyter Notebooks, je crée des solutions à moitié cuites, où je construis une solution qui fonctionne jusqu'à un certain point et ensuite les deux cellules suivantes seraient des questions : trouver la fréquence des données que nous venons d'interroger. Vous pouvez faire une démonstration, où vous faites et ils regardent, puis vous pouvez faire un suivi, où vous faites tous les deux en même temps, et enfin, vous passez par une méthode d'exercice, où ils font le travail en premier. Les deux dernières sont les plus utiles pour les concepts de data science.

![Speaking](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/speech.jpg)

### Q : Parlons davantage des ateliers pratiques. Nous nous retrouvons à faire de plus en plus d'ateliers chez IBM. Quelles sont les meilleures pratiques que vous pouvez partager ?

Les cinq choses qui fonctionnent le mieux pour moi dans les ateliers :

* Prérequis — Faites en sorte que les participants à l'atelier complètent certains prérequis avant l'atelier. Si vous avez des codes spéciaux pour les participants, distribuez-les à l'avance. Lorsqu'ils s'enregistrent à l'accueil, la première chose à faire est d'ajouter le code pour mettre à niveau leur compte. Beaucoup de temps dans les ateliers est perdu à la configuration ; l'orateur passe les 10 premières minutes à dire « Hé, suivez-moi. » Évitez cela si possible en préparant à l'avance. Et bien sûr, aussi bien que vous essayiez, il est impossible de faire en sorte que tout le monde soit configuré avant de commencer ; vous devrez vous occuper de ces utilisateurs avant de commencer votre présentation.
* Instructions étape par étape — Même si les participants n'ont aucun problème à suivre, avez un plan de secours avec des numéros de diapositives auxquels ils peuvent revenir et suivre. Qui lit le livre qui accompagne l'aspirateur ? Personne, mais vous pourriez avoir besoin de le consulter plus tard si vous avez des problèmes.
* Avoir la solution finale prête — Si vous utilisez GitHub, avez différentes branches pour les différentes étapes ; si les utilisateurs sont moins techniques ou doivent sauter une section, ils peuvent consulter cette branche et toujours pouvoir suivre l'atelier. Ce type de contenu prend du temps à développer.
* Objectifs étendus — Vous aurez un public de tous horizons et expériences, et il est important de répondre à tous (dans la mesure du possible). Vous perdrez soit les débutants — il est important de ne pas les perdre car ce pourrait être leur première fois de faire quelque chose — mais vous ne voulez pas perdre les utilisateurs intermédiaires et avancés non plus, et c'est là que les objectifs étendus sont importants.
* Ressources — Dites à vos étudiants où aller et quoi faire ensuite, en dehors de la logistique des ateliers. Assurez-vous d'avoir des assistants pendant les sessions comme ressource également.

### Q : Qui aimeriez-vous mentionner dans le monde des relations avec les développeurs pour avoir fait du bon travail ou repoussé les limites des relations avec les développeurs ?

Heureusement, le monde du DevRel est rempli de personnes que j'admire ! Certains des noms qui me viennent à l'esprit sont :

* Josh Gordon, Google, @random_forests
* Paige Bailey, Google, @DynamicWebPaige
* James Thomas, IBM, @thomasj
* Gabriela de Queiroz, IBM, @gdequeiroz
* Vijay Bommireddipalli, IBM, @vjbytes
* Renee M. P. Teate, Heliocampus, @BecomingDataSci

![game](https://developer.ibm.com/developer/blogs/adapting-your-devrel-strategy-for-data-science-and-ai-products/images/game.jpg)

## Prochaines étapes

* Suivez [Upkar sur Twitter](https://twitter.com/lidderupk)
* Écoutez l'une des conférences d'Upkar lors du [IBM Developer SF meetup](https://www.meetup.com/IBM-Developer-SF-Bay-Area-Meetup/)