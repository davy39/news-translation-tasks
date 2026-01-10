---
title: 'La distribution t : un concept statistique clé découvert par une brasserie
  de bière'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T20:42:20.000Z'
originalURL: https://freecodecamp.org/news/the-t-distribution-a-key-statistical-concept-discovered-by-a-beer-brewery-dbfdc693184
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ooxuSXzQoLp1CzVpcaP2Gw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: learning
  slug: learning
- name: life
  slug: life
- name: Mathematics
  slug: mathematics
- name: technology
  slug: technology
seo_title: 'La distribution t : un concept statistique clé découvert par une brasserie
  de bière'
seo_desc: 'By Kirill Dubovikov

  In this post we will look at two probability distributions you will encounter almost
  each time you do data science, statistics, or machine learning.

  Gaussian distribution

  Imagine that we are doing a research on the height of vario...'
---

Par Kirill Dubovikov

Dans cet article, nous allons examiner deux distributions de probabilité que vous rencontrerez presque à chaque fois que vous ferez de la science des données, des statistiques ou de l'apprentissage automatique.

### Distribution gaussienne

Imaginez que nous menons une recherche sur la taille de diverses personnes dans une ville. Nous descendons dans la rue et mesurons un groupe de personnes au hasard. (Certaines d'entre elles ont trouvé cela assez étrange et voulaient appeler la police, mais voyons, c'est pour la science !)

Maintenant, nous décidons qu'une [Analyse Exploratoire des Données](https://en.wikipedia.org/wiki/Exploratory_data_analysis) ne ferait pas de mal. Mais le logiciel statistique comme R n'est pas disponible pour le moment, alors nous faisons simplement un histogramme des personnes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5gf9Vel8pV2kuwZgWpQHZg.jpeg)
_Quand vous n'avez pas de logiciel statistique sous la main…_

Que voyons-nous ici ? Ahh, la célèbre courbe en cloche. Il s'agit probablement de la distribution de probabilité la plus importante que vous rencontrerez jamais. Grâce au [Théorème Central Limite](https://en.wikipedia.org/wiki/Central_limit_theorem), la distribution gaussienne est présente dans de nombreux phénomènes du monde réel. Elle est si courante que les gens l'appellent simplement une **distribution normale**.

Le Théorème Central Limite stipule que la moyenne arithmétique d'un nombre suffisamment grand de variables aléatoires indépendantes sera normalement distribuée. Ces variables aléatoires peuvent avoir n'importe quelle distribution initialement. Mais lorsque nous mesurons quelque chose qui est représenté par leur somme, nous finirons éventuellement (à mesure que le nombre d'échantillons tend vers ∞) par obtenir un processus normalement distribué.

La fonction de densité de probabilité de la distribution gaussienne est écrite ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mZXFcXjoX-hGcIVq8Rjfag@2x.png)

Cette formule peut sembler un peu intimidante, mais elle est pratique à utiliser mathématiquement. Si vous êtes intéressé par la manière dont elle peut être dérivée, vous pouvez [lire comment ici](http://courses.ncssm.edu/math/Talks/PDFS/normal.pdf). Comme vous pouvez le voir, cette distribution a deux paramètres :

* µ (moyenne)
* σ (écart-type).

La moyenne µ contrôle la [valeur attendue](https://en.wikipedia.org/wiki/Expected_value) (où la plupart des valeurs iront) d'une variable aléatoire normalement distribuée. La variance σ² contrôle la dispersion ou la variété des valeurs possibles sous la distribution.

Le concept de distribution normale a une immense valeur en apprentissage automatique. Une grande variété d'algorithmes d'apprentissage automatique l'utilisent extensivement :

* Les modèles linéaires supposent que les erreurs sont normalement distribuées
* Les processus gaussiens supposent que toutes les valeurs d'une fonction sous le modèle sont distribuées normalement
* Les mélanges gaussiens vous permettent de modéliser des distributions complexes et de construire des classificateurs sur la base de modèles de mélange
* La distribution normale apparaît comme l'un des principaux composants dans les Autoencodeurs Variationnels

Voici une démonstration interactive de la distribution gaussienne.

### La distribution t de Student

![Image](https://cdn-media-1.freecodecamp.org/images/1*wqw17kqJXeunz7cBdk8sUQ.jpeg)

Que se passe-t-il si nous voulons modéliser nos données avec une distribution gaussienne, mais que la variance σ² nous est inconnue ? Ce problème se pose lorsque les tailles d'échantillon sont petites et que l'écart-type (σ) ne peut pas être estimé avec précision.

William Gosset a abordé ce problème tout en travaillant à la brasserie Guinness. Il a trouvé empiriquement une formule pour une variable aléatoire **t-distribuée**.

Tout d'abord, supposons que nous avons des valeurs x, …, xn qui ont été échantillonnées à partir d'une certaine distribution normale N(µ, σ²).

Nous ne connaissons pas la vraie variance, mais nous pouvons l'estimer en calculant la moyenne et la variance de l'échantillon :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Fzr4BLa0YDiDI4kMIjZOkw@2x.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*sACHMWdisU0nU2e2xPIZeg@2x.png)

Alors la variable aléatoire

![Image](https://cdn-media-1.freecodecamp.org/images/1*frSLeAx5ObJWzD3L6a7Szw@2x.png)

aura une distribution t avec n-1 degrés de liberté, où n est le nombre d'échantillons.

Cette formule peut ressembler à la transformation de la distribution Normale en Normale Standard (un raccourci pour la distribution Normale avec une moyenne nulle et une variance unitaire) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TE3StAIUL1TEoxhbKzAiqw@2x.png)

Nous ne connaissons pas la vraie variance de la population, nous devons donc substituer l'estimation de l'écart-type de l'échantillon à la vraie valeur.

Cette distribution est à la base de la méthode scientifique, appelée le **test t**. Cela a été utilisé chez Guinness pour mesurer la qualité de leur bière.

William Gosset a publié ce résultat sous le pseudonyme Student. Guinness avait peur que ses concurrents découvrent que le test t était utilisé pour contrôler la qualité de leur produit.

Les découvertes de Gosset ont ensuite été formalisées par le célèbre statisticien Ronald Fisher. Fisher est considéré comme l'auteur de l'approche fréquentiste des statistiques.

Maintenant, vient la partie amusante ! Vous pouvez jouer avec la distribution t ci-dessous :

Comme vous pouvez le voir, la distribution t approche la normale standard lorsque les degrés de liberté sont grands. Cela se produit parce que la moyenne de l'échantillon approche la vraie moyenne à mesure que le nombre d'échantillons approche l'infini. Les "queues épaisses" de la distribution t compensent l'incertitude lorsque nous travaillons avec de petits échantillons.

Un lecteur intéressé pourrait demander : "Alors, quelle est la fonction de densité de probabilité de la distribution t ? Comment pouvons-nous la dériver ?" Il s'avère que ce n'est pas si facile en termes de mathématiques, mais l'idée centrale est facile à saisir.

Supposons que nous soyons intéressés par l'obtention de la fonction de densité de probabilité d'une variable normale X ~ N(0, σ). Mais sans dépendance directe de l'écart-type σ.

Intuitivement, pour se débarrasser de σ, nous devons faire quelques hypothèses. Traitions σ comme une variable aléatoire elle-même, et supposons qu'elle suit une [distribution Gamma](https://en.wikipedia.org/wiki/Gamma_distribution) (il s'agit d'une distribution très générale qui a de nombreuses utilisations en statistiques bayésiennes).

De cette manière, nous pouvons dire que X est un mélange de deux distributions de probabilité continues : Normale et Gamma. Ensuite, nous intégrons σ et arrivons à la formule de la fonction de densité de probabilité pour la distribution t.

Vous pouvez voir des preuves plus formelles [ici](https://probabilityandstats.wordpress.com/tag/students-t-distribution/) et [ici](https://www.statlect.com/probability-distributions/student-t-distribution).

### Conclusion

Les distributions gaussiennes et les distributions de Student sont certaines des distributions de probabilité continues les plus importantes en statistiques et en apprentissage automatique.

La distribution t peut être utilisée comme un substitut à la distribution gaussienne lorsque la variance de la population est inconnue, ou lorsque la taille de l'échantillon est petite. Les deux sont étroitement liées l'une à l'autre de manière stricte et formelle.

Merci d'avoir lu mon article ! J'espère qu'il vous a aidé à apprendre quelque chose de nouveau ou à rafraîchir vos connaissances existantes.