---
title: Comment choisir entre les bibliothèques open source en utilisant la popularité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T21:40:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-between-open-source-libraries-using-popularity-c71677785542
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aRTxvJrpsNRfsacu_sThaA.gif
tags:
- name: coding
  slug: coding
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment choisir entre les bibliothèques open source en utilisant la popularité
seo_desc: 'By Ashish Singal

  Through my career as a product manager, I’ve worked closely with engineers to build
  many technology products (and even hacked some together myself).

  When developing technology products, one of the most critical choices we can make
  is...'
---

Par Ashish Singal

Au cours de ma [carrière](https://www.linkedin.com/in/ashishsingal/) en tant que chef de produit, j'ai travaillé en étroite collaboration avec des ingénieurs pour construire de nombreux produits technologiques (et même en bricoler certains [moi-même](https://medium.com/@ashishsingal1/introducing-betalyzer-a-fintech-tutorial-110ac9abda58)).

Lors du développement de produits technologiques, l'un des choix les plus critiques que nous pouvons faire est entre des ensembles concurrents de bibliothèques et de frameworks. Un ingrédient clé est la **popularité relative**, pour plusieurs raisons :

1. **Indicateur du meilleur**. Surtout dans l'open source, le « marché » est assez efficace. Les développeurs se tournent généralement vers les meilleures technologies et votent avec leurs pieds.
2. **Aide**. Bien que la documentation formelle soit extrêmement importante, les questions sur Stack Overflow et les tutoriels Medium sont parfois encore plus bénéfiques pour progresser dans la courbe d'apprentissage et pour déboguer. Les extraits de code et les conseils des praticiens augmentent considérablement la vitesse de développement et l'impact.
3. **Talent**. Plus une bibliothèque est populaire, plus vous aurez de chances de trouver des personnes qui savent l'utiliser pour vous aider à construire votre produit.
4. **Améliorations futures**. Une base d'utilisateurs et une communauté dynamiques garantissent le développement continu du projet à l'avenir, réduisant ainsi les risques qu'il devienne obsolète.

#### Indicateurs de popularité

Il existe plusieurs moyens de mesurer la popularité des bibliothèques OS :

1. [Questions sur Stack Overflow](http://stackoverflow.com)
2. [Étoiles sur Github](https://github.com/)
3. [Google Trends](https://trends.google.com/trends/?geo=US)

[StackShare](https://stackshare.io) mérite également une mention honorable ici comme un bon moyen de trouver des outils populaires.

#### Évaluer la dynamique

Cependant, ces mesures nécessitent une composante temporelle. Sans prendre en compte la dynamique des métriques, les mesures ci-dessus sont purement rétrospectives — elles aident à informer sur ce qui **était** la meilleure technologie, et non sur ce qui **est** ou ce qui **sera**.

![Image](https://cdn-media-1.freecodecamp.org/images/rGSnxIgdwWGMlYKSkEAHsWC071BMJjfzRtKm)
_La dynamique nous aide à regarder vers l'avenir plutôt que vers le passé_

Par conséquent, plus souvent, lors de l'évaluation de bibliothèques concurrentes, je regarde souvent des graphiques de ces statistiques au fil du temps. Il existe plusieurs applications qui nous permettent de le faire :

1. [**Stack Overflow Trends**](http://sotagtrends.com/). Outil [open source](https://github.com/robianmcd/tag-trends) par [Rob McDiarmid](https://www.linkedin.com/in/rob-mcdiarmid-b56930140/). Également directement depuis [Stack Overflow](https://insights.stackoverflow.com/trends).
2. [**Github Star History**](https://timqian.com/star-history/). Des outils similaires incluent [StarTrack](https://seladb.github.io/StarTrack-js/), [Stargraph](https://stargraph.co/), et [ce projet](https://stars.przemeknowak.com/). Malheureusement, la plupart utilisent l'API Github pour cela, qui semble être assez peu fiable et boguée.
3. [**Google Trends**](https://trends.google.com/trends/?geo=US), bien sûr, fonctionne directement, mais semble quelque peu plus erratique et moins informatif que les deux autres mesures.

Google Cloud a également rendu les données de [Stack Overflow](https://console.cloud.google.com/marketplace/details/stack-exchange/stack-overflow?filter=solution-type:dataset&q=stack%20overflow&id=46a148ff-896d-444c-b08d-360169911f59) et de [Github](https://console.cloud.google.com/marketplace/details/github/github-repos?filter=solution-type:dataset&q=github&id=46ee22ab-2ca4-4750-81a7-3ee0f0150dcb) disponibles dans le cadre de leur programme [Public Datasets](https://cloud.google.com/public-datasets/). Et voici un [article](https://towardsdatascience.com/these-are-the-real-stack-overflow-trends-use-the-pageviews-c439903cd1a) qui explore certaines informations de Stack Overflow.

#### Exemple : Flask versus Django

Flask et Django sont deux frameworks populaires pour les applications web Python avec lesquels j'ai personnellement beaucoup d'expérience. Flask est plus léger et plus flexible, tandis que Django a beaucoup plus de fonctionnalités intégrées et est plus riche en fonctionnalités.

Voyons comment ceux-ci se classent en utilisant nos méthodologies ci-dessus :

1. **Étoiles sur Github** : [Django](https://github.com/django/django) compte actuellement 40k étoiles sur Github tandis que [Flask](https://github.com/pallets/flask) en compte 42k — ils sont au coude à coude. J'ai essayé plusieurs des trackers d'historique Github, mais ils ont tous expiré pour moi.
2. **Stack Overflow** : [Django](https://stackoverflow.com/questions/tagged/django) compte 191k questions, tandis que [Flask](https://stackoverflow.com/questions/tagged/flask) en compte 26k. La tendance montre que Flask rattrape son retard, mais il a encore un long chemin à parcourir.
3. **Google Trends** : Selon Google Trends, Django est actuellement environ deux fois plus populaire que Flask.

![Image](https://cdn-media-1.freecodecamp.org/images/CBZQzcNTdVcxYMvy7DrK0trRPjyrvAxMwErI)
_Questions posées sur Stack Overflow par mois : Flask vs Django_

![Image](https://cdn-media-1.freecodecamp.org/images/4jadhf1FU1Jm6a5A2vevtekWtlcWMaUc3Fsj)
_Popularité des recherches Google Trends : Flask vs Django_

**Notez** bien sûr que la popularité relative n'est qu'un facteur parmi d'autres dans le choix entre les bibliothèques. Entre Flask et Django, par exemple, j'ai tendance à choisir Flask pour le prototypage rapide ainsi que lorsque je développe une application non traditionnelle et que j'ai besoin d'une grande flexibilité. J'ai tendance à choisir Django lorsque je souhaite une fonctionnalité prête à l'emploi pour des choses comme les comptes utilisateurs, l'administration et l'ORM intégré.

![Image](https://cdn-media-1.freecodecamp.org/images/2tSeX16wBNz2R5HWtcHemR0I1Vhuya83NznB)
_Oui, la popularité compte !_

J'espère que cela aide ! Merci d'avoir lu.