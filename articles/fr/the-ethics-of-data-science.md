---
title: Éthique de la Science des Données – Ce qui peut mal tourner et comment l'éviter
subtitle: ''
author: Kylie Ying
co_authors: []
series: null
date: '2021-09-16T15:17:13.000Z'
originalURL: https://freecodecamp.org/news/the-ethics-of-data-science
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/data-science-ethics-101.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: ethics
  slug: ethics
seo_title: Éthique de la Science des Données – Ce qui peut mal tourner et comment
  l'éviter
seo_desc: 'Data science models are all around you.

  They could impact your admission to a school, whether you get hired (or fired),
  your work schedule, whom you date, whether you get a loan, what ads are shown to
  you, what social media posts you see, and so on.

  ...'
---

Les modèles de science des données sont partout autour de vous.

Ils peuvent influencer votre admission dans une école, si vous êtes embauché (ou licencié), votre horaire de travail, avec qui vous sortez, si vous obtenez un prêt, quelles publicités vous sont montrées, quels posts sur les réseaux sociaux vous voyez, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Slide3.jpeg)

J'ai créé une présentation discutant de l'éthique derrière la science des données, de l'acquisition des données à la modélisation et aux algorithmes.

Dans ce cours, je discute de ce qui pourrait mal tourner d'un point de vue moral, de ce qui a mal tourné dans le passé, et des directives que la communauté informatique a créées pour combattre les conduites non éthiques.

Ce contenu est adapté de [OpenDS4All](https://github.com/odpi/OpenDS4All/tree/master/opends4all-resources). OpenDS4All est un projet créé pour accélérer la création de programmes de science des données dans les institutions académiques.

OpenDS4All tente de fournir une combinaison de cours magistraux, d'activités de récitation ou de classe inversée, et de devoirs pratiques pour dispenser une éducation en science des données et en ingénierie des données.

Maintenant, explorons comment l'éthique joue un rôle dans l'acquisition moderne de données et les algorithmes.

Pour une plongée approfondie dans l'éthique de la science des données, vous pouvez regarder la présentation ici. Si vous voulez brièvement en apprendre plus sur l'éthique en science des données et comprendre de quoi parle la présentation, continuez à lire.

%[https://www.youtube.com/watch?v=WU7McTUumxU]

## Pourquoi devrions-nous nous soucier de l'éthique dans la technologie ?

**"Un grand pouvoir implique de grandes responsabilités"**. Ah, le principe de Peter Parker. La science des données a maintenant tant d'influence sur la vie des gens. Un bon scientifique des données doit comprendre les problèmes éthiques entourant les données qu'il obtient ou utilise, les algorithmes qu'il emploie, et leur impact sur les personnes.

Les gens font la bonne chose pour quelques raisons différentes. L'éthique entre en jeu ici. L'éthique est un ensemble de règles que nous suivons tous volontairement parce que cela rend le monde meilleur pour nous tous.

Cependant, parfois, il n'est pas clair sur le moment ce qu'est la bonne chose à faire. Parfois, cela n'est évident qu'avec le recul. Cependant, ces expériences et conséquences sont ce qui façonne notre compréhension et nos attentes pour l'avenir.

## Éthique et Données

Les données sont constamment collectées à notre sujet. Les caméras sont partout. Les téléphones portables rapportent les localisations. Les réseaux sociaux suivent nos clics.

### Consentement éclairé

Dans la recherche sur les sujets humains, il y a une notion de consentement éclairé. Nous comprenons ce qui est fait, nous consentons volontairement à l'expérience, et nous avons le droit de retirer notre consentement à tout moment.

Cependant, cela est plus vague dans la "conduite ordinaire des affaires", comme les tests A/B. Par exemple, Facebook peut effectuer ces tests tout le temps sans consentement explicite ou même sans connaissance !

Dans la vidéo, je discute d'une expérience de manipulation de l'humeur faite par Facebook en 2012 et d'une expérience "L'Amour est aveugle" faite par OKCupid en 2015.

Le consentement éclairé est souvent enterré dans les petits caractères et beaucoup d'entre nous ne lisons pas nécessairement ces longues conditions générales. De plus, il est difficile de contrôler comment les données sont utilisées à l'avenir et comment elles sont contrôlées.

De plus, les grands ensembles de données sont parfois très vagues sur la manière dont ils sont protégés. Par exemple, Wikipedia, Yelp, Rotten Tomatoes, un ensemble de données cliniques, les données d'une entreprise, votre séquence génétique...

### Vie privée

Il y a aussi une préoccupation concernant la vie privée. La vie privée est un besoin humain fondamental. La perte de vie privée se produit lorsqu'il y a une perte de contrôle sur les données personnelles. Dans la vidéo, je discute d'une controverse de 2016 chez OKCupid où les données de profil des utilisateurs ont été publiées.

Dans certains cas, même lorsque les informations identifiables sont supprimées des données – comme le nom, le numéro de téléphone, l'adresse, etc. – cela peut ne pas être suffisant pour protéger les identités des individus.

Il y a eu de nombreux cas de désanonymisation, où les utilisateurs d'AOL sont identifiés sur la base de l'historique de recherche, ou les dossiers médicaux des gens sont identifiés sur la base du code postal, de la date de naissance et du sexe.

À partir de ces préoccupations concernant la sécurité des données publiées, le concept de "vie privée différentielle" est entré en jeu. Essentiellement, l'objectif est de fournir autant d'informations statistiques que possible tout en garantissant l'anonymat de l'individu contributeur.

## Éthique et Algorithmes

Un algorithme ne peut pas être neutre. Un algorithme encode naturellement les biais que nous lui fournissons. Par exemple, nos données d'entraînement peuvent ne pas représenter l'ensemble de la population. La population passée peut ne pas représenter la population future.

**Il est possible d'obtenir des résultats "mauvais" à partir de données "bonnes".**

### Erreurs courantes des algorithmes

Il peut y avoir des attributs corrélés qui interfèrent. Dans la vidéo, je discute d'un exemple où Staples tentait de battre ses concurrents, mais a fini par offrir des deals moins chers aux quartiers plus aisés.

De plus, les résultats peuvent parfois être présentés de manière trompeuse. Dans l'exemple ci-dessous, nous pouvons voir comment les mêmes données avec différents axes y peuvent mener à des conclusions différentes :

![Image](https://lh6.googleusercontent.com/rDNiax3IOShWDaOt5qDoKQFEi1UON7sQtoqkIZC63mpyJWTK8T9SskSyXTxSDKVQ2caps-AiYgTNq7hp4ZVF0nRWf65kt_nYIgnGlrX9_7yj2SVrEGkRfubO7Ws3kdD6HCByyTuOQU8=s0)

Il est également possible de p-hacker pour trouver des motifs dans les données qui peuvent être présentés comme statistiquement significatifs. Mais en réalité, vous avez peut-être simplement effectué de nombreux tests statistiques sur de nombreuses expériences et n'avez rapporté que ceux avec des résultats significatifs.

Si vous faites une infinité d'expériences, il est certain qu'il y en aura une qui reviendra avec des résultats significatifs juste par hasard.

### FAT* – Équité, Responsabilité, Transparence

Dans la communauté informatique, un domaine de recherche important qui a émergé est FAT* (Fairness, Accountability, Transparency). Cela implique de déterminer des décisions équitables selon nos notions de justice sociale, l'utilisation éthique des données, et des décisions interprétables issues de l'apprentissage automatique.

[Voici](https://geomblog.github.io/fairness) une bonne ressource pour en apprendre plus en profondeur.

L'équité est un sujet à la mode en informatique théorique en ce moment. Il existe deux types de discrimination qui peuvent se produire : la discrimination d'un individu et la discrimination dans le résultat global.

La discrimination d'un individu peut se produire lorsqu'un individu du groupe cible est traité différemment d'un individu par ailleurs identique n'appartenant pas au groupe cible.

La discrimination dans le résultat global peut se produire lorsque le pourcentage de réussite du groupe cible peut différer par rapport à celui de la population générale.

[Voici](https://www.quantamagazine.org/making-algorithms-fair-an-interview-with-cynthia-dwork-20161123) une excellente ressource pour une discussion plus approfondie.

Dans la vidéo, je discute du rôle controversé des algorithmes dans le prononcé des peines et la libération conditionnelle. Ces algorithmes semblent montrer des disparités raciales en faveur des accusés blancs et en défaveur des accusés noirs.

![Image](https://lh6.googleusercontent.com/tDiLKliZzV-rDY88tsmW3Cafd97o1oNG2FTHhFIzPgHEfLIzODgcjEp0Nwt8O0y7EeoVB4Mwzdn_5WSlOUUesrDTLrIKASQBFpBBqB5MrtbDD3HEUjYhXUcPfmMetLFf15i0SWQVxCw=s0)

En plus d'être équitables, nous voulons également que nos algorithmes soient reproductibles. En général, "transparence" signifie une transparence totale. L'ensemble du pipeline de collecte de données, de données brutes et d'analyses de recherche devrait être mis à disposition, contribuant ainsi à une reproductibilité potentielle.

Cependant, parfois les données ne peuvent pas être partagées, et les algorithmes peuvent être assez complexes et difficiles à comprendre, surtout s'ils sont des algorithmes de boîte noire.

Pour aider à résoudre ce problème, les principes "FAIR" – trouvables, accessibles, interopérables, réutilisables – ont été proposés. Consultez cet [article](https://www.nature.com/articles/sdata201618) pour en savoir plus.

## Voulez-vous en savoir plus ?

En résumé, les codes de conduite pour la recherche sont assez bien compris. En général, les expériences veulent obtenir un consentement éclairé, protéger la vie privée des sujets et maintenir la confidentialité des données collectées tout en minimisant les dommages.

Inversement, le concept de ce qui est équitable est légèrement plus subtil. Parfois, il n'est pas nécessairement clair ce qui constitue exactement un traitement équitable d'un groupe d'un point de vue quantitatif.

Il peut y avoir un compromis entre l'optimisation des résultats et l'évitement de la discrimination contre un groupe. Cependant, la communauté informatique a activement établi des directives pour aider à protéger les individus, les données et les modèles.

Voulez-vous en savoir plus ? Regardez la présentation pour plonger dans les nuances de l'éthique en science des données !

%[https://www.youtube.com/watch?v=WU7McTUumxU]

Merci à [OpenDS4All](https://github.com/odpi/OpenDS4All/tree/master/opends4all-resources) !