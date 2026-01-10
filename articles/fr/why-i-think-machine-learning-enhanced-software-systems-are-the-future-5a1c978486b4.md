---
title: Pourquoi je pense que les systèmes logiciels améliorés par l'apprentissage
  automatique sont l'avenir.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-26T10:10:28.000Z'
originalURL: https://freecodecamp.org/news/why-i-think-machine-learning-enhanced-software-systems-are-the-future-5a1c978486b4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OOWSoWHeQ5kyJ4N0P2ptNA.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi je pense que les systèmes logiciels améliorés par l'apprentissage
  automatique sont l'avenir.
seo_desc: 'By Rodrigo Araújo

  I have been brewing the idea of using machine learning to improve software systems
  since 2016. It was pretty vague and broad, without an actionable plan. I just had
  the intuition — the software configuration and tuning, especially a...'
---

Par Rodrigo Araújo

J'ai mûri l'idée d'utiliser l'apprentissage automatique pour améliorer les systèmes logiciels depuis 2016. C'était assez vague et large, sans plan d'action concret. J'avais juste l'intuition — la configuration et le réglage des logiciels, surtout après l'adoption des microservices, devenaient trop complexes.

#### La complexité croissante de la configuration et du réglage des systèmes

Si vous avez assez d'expérience dans l'industrie du logiciel, il est très probable que vous ayez rencontré un problème de configuration ou de réglage.

Les problèmes de configuration et de réglage sont assez courants et peuvent entraîner des pannes vraiment graves. Ils se produisent souvent lorsque :

1. Certaines parties du système sont mal ou incorrectement configurées, ou
2. Une configuration qui fonctionnait auparavant ne fonctionne plus parce que le contexte du système a changé.

Pensez au nombre de réplicas de base de données et à leurs schémas d'écriture. Ou dans Postgresql, pensez au nombre de tampons partagés, à la taille du cache efficace, et à la taille minimale et maximale du wal.

Si mal configuré dès le départ, cela ne fonctionnera pas dans le contexte donné, c'est simple. Ce qui est plus intéressant, cependant, c'est que si c'est _correctement_ configuré, cela peut fonctionner à un moment donné. Mais à mesure que le contexte change — charge de travail du système, utilisation des ressources du système, architecture globale du système — le système se comportera mal. Ou, pire encore, une panne pourrait se produire.

Cela conduira, inévitablement, à des opérations effectuées manuellement et à la création d'heuristiques. En d'autres termes, cela conduira à :

> Oh, nous devrions définir X à A, lorsque la charge de travail est T, mais il devrait être A+10 lorsque la charge de travail est T+100 et que nous avons une utilisation des ressources du système supérieure à 80%... Je suppose. Ou peut-être mettons simplement une file d'attente devant ce composant, les files d'attente résolvent tout, n'est-ce pas ?

Maintenant, multipliez ce scénario par des dizaines ou des centaines de services. Réfléchissez une seconde à la charge cognitive résultant de ces configurations.

Ce n'est pas une préoccupation nouvelle. En 2003, Ganek et Corbi [ont discuté](http://ieeexplore.ieee.org/document/5386835/?reload=true) de la nécessité de l'informatique autonome pour gérer la complexité de la gestion des systèmes logiciels. Ils ont noté que la gestion des systèmes complexes était devenue trop coûteuse, laborieuse et sujette aux erreurs en raison de la pression que ressentaient les ingénieurs lors de leur maintenance. Cela a augmenté le potentiel de pannes de système avec un impact concurrent sur les affaires.

Même de nos jours, la plupart des configurations et des réglages des systèmes sont effectués manuellement, souvent en temps réel, ce qui est connu pour être une pratique très chronophage et risquée. Consultez ces deux liens ([ici](https://link.springer.com/book/10.1007/978-3-642-35813-5) et [ici](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.90.8651&rep=rep1&type=pdf)) pour en savoir plus.

![Image](https://cdn-media-1.freecodecamp.org/images/2BvlZ15KllBuRhMqHbyNH8wDeyBvJfZKZuw-)

#### Le besoin d'informatique autonome

La plupart des décisions de configuration et de réglage du système sont prises en fonction du contexte — il existe de nombreuses variables différentes telles que la charge de travail, le nombre d'instances de certains services, l'utilisation des ressources, et plus encore. Alors pourquoi ne pas déléguer ces tâches à quelque chose qui excelle exactement dans cela ? _L'apprentissage automatique semble être un outil réalisable pour le travail._

Après avoir commencé mon master à l'Université de la Colombie-Britannique, j'ai continué à travailler sur cette idée. Cela semblait intéressant bien que assez étrange, et parfois, peu pratique et impossible à mettre en œuvre.

À ma grande surprise, j'ai réalisé que je n'étais pas seul. Certaines personnes très intéressantes travaillaient sur ces idées — donc ce n'est peut-être pas si étrange, peu pratique et impossible.

Récemment, Jeff Dean — un homme que j'admire beaucoup — [a donné une conférence au NIPS 2017 sur l'apprentissage automatique pour les systèmes](https://news.ycombinator.com/item?id=15892956), où il a déclaré :

> L'apprentissage devrait être utilisé dans tous nos systèmes informatiques. Le code système traditionnel de bas niveau (systèmes d'exploitation, compilateurs, systèmes de stockage) n'utilise pas largement l'apprentissage automatique aujourd'hui. Cela devrait changer !

> Les systèmes informatiques sont remplis d'heuristiques : compilateurs, code de mise en réseau, systèmes d'exploitation. Les heuristiques doivent bien fonctionner « en général ». [Elles] ne s'adaptent généralement pas au modèle réel d'utilisation et ne tiennent pas compte du contexte disponible

> L'apprentissage au cœur de tous nos systèmes informatiques les rendra meilleurs/plus adaptatifs.

J'étais en admiration totale lorsque j'ai lu cela. L'un des ingénieurs que j'admire le plus parlait des mêmes idées que celles auxquelles je pensais et sur lesquelles je travaillais.

Cela m'a conduit à penser que ce n'est pas seulement intéressant mais **naturel de penser à améliorer les systèmes logiciels avec l'apprentissage automatique.** Dans toute la pile logicielle, nous avons de nombreuses heuristiques qui, bien qu'elles fonctionnent bien, pourraient être améliorées par l'apprentissage automatique.

Est-ce un défi et potentiellement risqué ? Oui, très certainement. Surtout étant donné que l'interprétabilité, apparemment, est devenue un objectif secondaire dans la communauté de l'apprentissage automatique. Comment pouvons-nous interpréter et expliquer les décisions prises par les réseaux de neurones ?

Cependant, cela dit, ces obstacles ne devraient pas entraver le progrès scientifique et technologique. [Oui, nous devrions remettre en question les anciens paradigmes](https://arxiv.org/pdf/1712.01208.pdf) et essayer d'améliorer les choses.

![Image](https://cdn-media-1.freecodecamp.org/images/HCfR4tFFH5qucVzcmyk7jobtJHlmPimQ14QU)

#### Vers des systèmes logiciels améliorés par l'apprentissage automatique

Comme l'a souligné Jeff Dean : nous devons trouver des moyens **pratiques** de rendre les systèmes conscients des données. Nous avons besoin de systèmes qui collectent des métriques et des métadonnées sur eux-mêmes. Pour y parvenir, nous pourrions apprendre une ou deux choses des idées de l'observabilité et de l'instrumentation des systèmes. Nous instrumentons les systèmes depuis des décennies, et les données sont déjà là.

Nous devons également trouver des moyens **pratiques** et **propres** d'**intégrer** des composants d'apprentissage automatique dans les systèmes logiciels, faisant de l'apprentissage un citoyen de première classe dans le système. Cela conduira à des **systèmes qui apprennent à s'améliorer eux-mêmes**, battant les heuristiques et les opérations effectuées manuellement. Réfléchissez à cela pendant une seconde. Cela semble cool _et_ réalisable.

J'ajouterais également que nous avons besoin de moyens **pratiques** et **propres** pour propager les décisions prises par les modèles appris au reste du système. Cela permettrait au système d'avoir des capacités auto-adaptatives. Ici, nous pourrions apprendre quelque chose de la communauté de la théorie du contrôle.

L'idée générale est assez simple : faire apprendre à un système son comportement en entraînant un modèle sur son contexte. Ensuite, lui permettre de changer ses structures et ses configurations afin d'optimiser pour un certain scénario. Maintenant, mettez en œuvre cette idée de manière à ce qu'il soit possible de l'intégrer dans de nombreux types de systèmes.

#### Résumé

Les questions les plus intéressantes que j'ai en tête sont :

1. L'auto-adaptation par des modèles appris peut-elle conduire à des systèmes logiciels plus stables, plus rapides et plus sûrs ? Peut-elle réduire le besoin de configurer et de régler manuellement les systèmes, permettant aux ingénieurs de se concentrer sur des tâches plus importantes ?
2. Cela peut-il être facilement intégré dans les systèmes logiciels, nécessitant seulement de petits changements dans la base de code ?
3. Cela peut-il fonctionner avec peu de surcharge ?

Il est important de noter que cela **ne** remplacerait pas les bons ingénieurs, mais libérerait plutôt les capacités cognitives des ingénieurs pour se concentrer sur ce qui compte.

[Je crois sincèrement que cela deviendra une tendance dans les prochaines années](http://www.sysml.cc/). Je travaille moi-même sur ces idées dans le cadre de mes études de troisième cycle, et je publierai les résultats de mes recherches, alors [restez à l'écoute](https://twitter.com/digorithm).