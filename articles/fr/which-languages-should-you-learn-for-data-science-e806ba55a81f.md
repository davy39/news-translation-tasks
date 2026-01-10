---
title: Quelles langues devez-vous apprendre pour la science des données ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-31T16:07:30.000Z'
originalURL: https://freecodecamp.org/news/which-languages-should-you-learn-for-data-science-e806ba55a81f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gSxUa9oNaBk1QJf6eqQYeg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Java
  slug: java
- name: Julialang
  slug: julialang
- name: Matlab
  slug: matlab
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: R Programming
  slug: r-programming
- name: Scala
  slug: scala
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Quelles langues devez-vous apprendre pour la science des données ?
seo_desc: 'By Peter Gleeson

  Data science is an exciting field to work in, combining advanced statistical and
  quantitative skills with real-world programming ability. There are many potential
  programming languages that the aspiring data scientist might consider ...'
---

Par Peter Gleeson

La science des données est un domaine passionnant dans lequel travailler, combinant des compétences statistiques et quantitatives avancées avec une véritable capacité de programmation. Il existe de nombreux langages de programmation potentiels que l'aspirant scientifique des données pourrait envisager de maîtriser.

Bien qu'il n'y ait pas de réponse correcte, il y a plusieurs choses à prendre en considération. Votre succès en tant que scientifique des données dépendra de nombreux points, notamment :

**Spécificité**

En matière de science des données avancée, vous n'irez pas très loin en réinventant la roue à chaque fois. Apprenez à maîtriser les divers packages et modules proposés dans votre langage choisi. La mesure dans laquelle cela est possible dépend des packages spécifiques au domaine disponibles pour vous en premier lieu !

**Généralité**

Un scientifique des données de premier plan aura de bonnes compétences en programmation générale ainsi que la capacité à traiter des nombres. Une grande partie du travail quotidien en science des données tourne autour de la recherche et du traitement de données brutes ou du « nettoyage de données ». Pour cela, aucun package de machine learning sophistiqué ne sera d'une grande aide.

**Productivité**

Dans le monde souvent rapide de la science des données commerciale, il est important de faire le travail rapidement. Cependant, c'est ce qui permet à la dette technique de s'installer — et ce n'est qu'avec des pratiques sensées que cela peut être minimisé.

**Performance**

Dans certains cas, il est vital d'optimiser la performance de votre code, surtout lorsque vous traitez de grands volumes de données critiques. Les langages compilés sont généralement beaucoup plus rapides que les langages interprétés ; de même, les langages à typage statique sont considérablement plus fiables que ceux à typage dynamique. Le compromis évident est contre la productivité.

Dans une certaine mesure, ceux-ci peuvent être vus comme une paire d'axes (Généralité-Spécificité, Performance-Productivité). Chacun des langages ci-dessous se situe quelque part sur ces spectres.

Avec ces principes de base à l'esprit, examinons certains des langages les plus populaires utilisés en science des données. Ce qui suit est une combinaison de recherches et d'expériences personnelles de moi-même, d'amis et de collègues — mais ce n'est en aucun cas définitif ! Dans un ordre approximatif de popularité, voici :

### R

#### Ce que vous devez savoir

![Image](https://cdn-media-1.freecodecamp.org/images/bx3wt1sCBXSEUkiii81wH31gLcU0e3XiA6S7)

Sorti en 1995 comme descendant direct de l'ancien langage de programmation S, R n'a depuis cessé de se renforcer. Écrit en C, Fortran et en lui-même, le projet est actuellement soutenu par la [R Foundation for Statistical Computing](https://www.r-project.org/foundation/).

#### Licence

Gratuit !

#### Avantages

* Excellente gamme de packages de haute qualité, spécifiques au domaine et [open source](https://cran.r-project.org/). R dispose d'un package pour presque toutes les applications quantitatives et statistiques imaginables. Cela inclut les réseaux de neurones, la régression non linéaire, la phylogénétique, le traçage avancé et bien d'autres.
* L'installation de base comprend des fonctions et méthodes statistiques très complètes et intégrées. R gère également particulièrement bien l'algèbre matricielle.
* La visualisation de données est un point fort avec l'utilisation de bibliothèques telles que [ggplot2](http://ggplot2.org/).

#### Inconvénients

* Performance. Il n'y a pas deux façons de le dire, [R n'est pas un langage rapide](http://adv-r.had.co.nz/Performance.html).
* Spécificité du domaine. R est fantastique pour les statistiques et les objectifs de science des données. Mais moins pour la programmation générale.
* Particularités. R a quelques caractéristiques inhabituelles qui pourraient surprendre les programmeurs expérimentés avec d'autres langages. Par exemple : l'indexation à partir de 1, l'utilisation de plusieurs opérateurs d'affectation, des structures de données non conventionnelles.

#### Verdict — « brillant pour ce pour quoi il est conçu »

R est un langage puissant qui excelle dans une grande variété d'applications statistiques et de visualisation de données, et étant open source, il permet une communauté très active de contributeurs. Sa récente croissance en popularité témoigne de son efficacité dans ce qu'il fait.

### Python

#### Ce que vous devez savoir

![Image](https://cdn-media-1.freecodecamp.org/images/U0XPlJp-xNFQypL6euOVZKDgms1Rfk4Hiojy)

Guido van Rossum a introduit Python en 1991. Il est depuis devenu un langage généraliste extrêmement populaire, largement utilisé dans la communauté de la science des données. Les versions majeures sont actuellement [3.6](https://www.python.org/downloads/release/python-362/) et [2.7](https://www.python.org/download/releases/2.7/).

#### Licence

Gratuit !

#### Avantages

* Python est un langage de programmation généraliste très populaire et grand public. Il dispose d'une [large gamme de modules spécialisés](https://pypi.python.org/pypi) et d'un soutien communautaire. De nombreux services en ligne fournissent une API Python.
* Python est un langage facile à apprendre. La faible barrière à l'entrée en fait un langage idéal pour les débutants en programmation.
* Des packages tels que [pandas](http://pandas.pydata.org/), [scikit-learn](http://scikit-learn.org/stable/) et [Tensorflow](https://www.tensorflow.org/) font de Python une option solide pour les applications avancées de machine learning.

#### Inconvénients

* Sécurité des types : Python est un langage à typage dynamique, ce qui signifie que vous devez faire preuve de prudence. Des erreurs de type (comme passer une chaîne de caractères en argument à une méthode qui attend un entier) sont à prévoir de temps en temps.
* Pour des objectifs statistiques et d'analyse de données spécifiques, la vaste gamme de packages de R lui donne un léger avantage sur Python. Pour les langages généralistes, il existe des alternatives plus rapides et plus sûres que Python.

#### Verdict — « excellent polyvalent »

Python est un très bon choix de langage pour la science des données, et pas seulement au niveau débutant. Une grande partie du processus de science des données tourne autour du [processus ETL](https://en.wikipedia.org/wiki/Extract,_transform,_load) (extraction-transformation-chargement). Cela rend la généralité de Python idéale. Des bibliothèques comme Tensorflow de Google font de Python un langage très excitant pour travailler dans le machine learning.

### SQL

#### Ce que vous devez savoir

![Image](https://cdn-media-1.freecodecamp.org/images/1Dbg8u7RSmjx8l-Xv7DMDJpesKUYKEVASvP6)

[SQL](https://www.w3schools.com/sql/default.asp) (« Structured Query Language ») définit, gère et interroge les [bases de données relationnelles](https://en.wikipedia.org/wiki/Relational_database). Le langage est apparu en 1974 et a depuis subi de nombreuses implémentations, mais les principes de base restent les mêmes.

#### Licence

Variable — certaines implémentations sont gratuites, d'autres propriétaires

#### Avantages

* Très efficace pour interroger, mettre à jour et manipuler des bases de données relationnelles.
* La syntaxe déclarative rend SQL souvent très lisible. Il n'y a pas d'ambiguïté sur ce que `SELECT name FROM users WHERE age >` 18 est censé faire !
* SQL est très utilisé dans une gamme d'applications, ce qui en fait un langage très utile à connaître. Des modules tels que [SQLAlchemy](https://www.sqlalchemy.org/) rendent l'intégration de SQL avec d'autres langages simple.

#### Inconvénients

* Les capacités analytiques de SQL sont plutôt limitées — au-delà de l'agrégation et de la somme, du comptage et de la moyenne des données, vos options sont limitées.
* Pour les programmeurs venant d'un contexte impératif, la syntaxe déclarative de SQL peut présenter une courbe d'apprentissage.
* Il existe de nombreuses implémentations différentes de SQL telles que [PostgreSQL](https://www.postgresql.org/), [SQLite](https://www.sqlite.org/), [MariaDB](https://mariadb.org/). Elles sont toutes suffisamment différentes pour rendre l'interopérabilité quelque peu problématique.

#### Verdict — « intemporel et efficace »

SQL est plus utile comme langage de traitement de données que comme outil analytique avancé. Pourtant, une grande partie du processus de science des données repose sur l'ETL, et la longévité et l'efficacité de SQL prouvent qu'il s'agit d'un langage très utile pour le scientifique des données moderne à connaître.

### Java

#### Ce que vous devez savoir

![Image](https://cdn-media-1.freecodecamp.org/images/E2x8C0ZeF7QXqbkewzZdLlXojOkcMP16sayQ)

Java est un langage généraliste extrêmement populaire qui s'exécute sur la machine virtuelle Java (JVM). C'est un système informatique abstrait qui permet une portabilité transparente entre les plateformes. Actuellement soutenu par [Oracle Corporation](https://www.oracle.com/java/index.html).

#### Licence

Version 8 — Gratuit ! Les versions héritées sont propriétaires.

#### Avantages

* Ubiquité. De nombreux systèmes et applications modernes sont construits sur un backend Java. La capacité d'intégrer des méthodes de science des données directement dans la base de code existante est un atout puissant.
* Typage fort. Java ne fait pas de compromis en matière de sécurité des types. Pour les applications de big data critiques, cela est inestimable.
* Java est un langage généraliste, haute performance et compilé. Cela le rend adapté pour écrire un code de production ETL efficace et des algorithmes de machine learning intensifs en calcul.

#### Inconvénients

* Pour les analyses ad hoc et les applications statistiques plus dédiées, la verbosité de Java en fait un choix peu probable. Les langages de script à typage dynamique comme R et Python se prêtent à une productivité beaucoup plus grande.
* Comparé aux langages spécifiques à un domaine comme R, il n'existe pas un grand nombre de bibliothèques disponibles pour les méthodes statistiques avancées en Java.

#### Verdict — « un sérieux concurrent pour la science des données »

Il y a beaucoup à dire pour apprendre Java comme premier choix de langage pour la science des données. De nombreuses entreprises apprécieront la capacité d'intégrer de manière transparente le code de production de science des données directement dans leur base de code existante, et vous trouverez que les performances et la sécurité des types de Java sont de réels avantages.

Cependant, vous serez sans la gamme de packages spécifiques aux statistiques disponibles pour d'autres langages. Cela dit, définitivement un langage à considérer — surtout si vous connaissez déjà R et/ou Python.

### Scala

#### Ce que vous devez savoir

![Image](https://cdn-media-1.freecodecamp.org/images/ttyRkvz1Ye6LkeZdGzMZmesaG2BcvGZhFcmV)

Développé par Martin Odersky et sorti en 2004, [Scala](https://www.scala-lang.org/) est un langage qui s'exécute sur la JVM. C'est un langage multi-paradigme, permettant à la fois des approches orientées objet et fonctionnelles. Le framework de calcul en cluster [Apache Spark](https://spark.apache.org/) est écrit en Scala.

#### Licence

Gratuit !

#### Avantages

* Scala + Spark = Calcul en cluster haute performance. Scala est un choix idéal de langage pour ceux qui travaillent avec des ensembles de données de grand volume.
* Multi-paradigmatique : Les programmeurs Scala peuvent avoir le meilleur des deux mondes. Les paradigmes de programmation orientée objet et fonctionnelle sont disponibles pour eux.
* Scala est compilé en bytecode Java et s'exécute sur une JVM. Cela permet l'interopérabilité avec le langage Java lui-même, faisant de Scala un langage généraliste très puissant, tout en étant bien adapté pour la science des données.

#### Inconvénients

* Scala n'est pas un langage facile à prendre en main si vous débutez. Votre meilleur choix est de télécharger [sbt](http://www.scala-sbt.org/) et de configurer un IDE tel qu'Eclipse ou IntelliJ avec un plug-in spécifique à Scala.
* La syntaxe et le système de types sont souvent décrits comme complexes. Cela rend la courbe d'apprentissage raide pour ceux qui viennent de langages dynamiques comme Python.

#### Verdict — « parfait, pour des données suffisamment volumineuses »

Lorsque l'on utilise le calcul en cluster pour travailler avec le Big Data, alors Scala + Spark sont des solutions fantastiques. Si vous avez de l'expérience avec Java et d'autres langages à typage statique, vous apprécierez également ces caractéristiques de Scala.

Cependant, si votre application ne traite pas des volumes de données qui justifient la complexité supplémentaire de Scala, vous trouverez probablement que votre productivité est beaucoup plus élevée en utilisant d'autres langages comme R ou Python.

### Julia

#### Ce que vous devez savoir

![Image](https://cdn-media-1.freecodecamp.org/images/Ok4VqC5ra015oGgqPcuGvJ9cWBtBu5f0Zt-G)

Sorti il y a un peu plus de 5 ans, [Julia](https://julialang.org/) a marqué le monde du calcul numérique. Son profil a été élevé grâce à une adoption précoce par [plusieurs grandes organisations](https://juliacomputing.com/case-studies/), y compris de nombreuses dans le secteur financier.

#### Licence

Gratuit !

#### Avantages

* Julia est un langage compilé JIT (« just-in-time »), ce qui lui permet d'offrir de bonnes performances. Il offre également la simplicité, le typage dynamique et les capacités de script d'un langage interprété comme Python.
* Julia a été conçu à des fins d'analyse numérique. Il est également capable de programmation généraliste.
* Lisibilité. De nombreux utilisateurs du langage citent cela comme un avantage clé.

#### Inconvénients

* Maturité. En tant que nouveau langage, certains utilisateurs de Julia ont rencontré des instabilités lors de l'utilisation de packages. Mais le langage de base lui-même est apparemment suffisamment stable pour une utilisation en production.
* Le nombre limité de packages est une autre conséquence de la jeunesse du langage et de sa petite communauté de développement. Contrairement à R et Python bien établis, Julia n'a pas encore le choix de packages.

#### Verdict — « un langage pour l'avenir »

Le principal problème avec Julia est celui qui ne peut pas lui être reproché. En tant que langage récemment développé, il n'est pas aussi mature ou prêt pour la production que ses principales alternatives Python et R.

Mais, si vous êtes prêt à être patient, il y a toutes les raisons de prêter une attention particulière à l'évolution du langage dans les années à venir.

### MATLAB

#### Ce que vous devez savoir

![Image](https://cdn-media-1.freecodecamp.org/images/DI1Fj8dKXe484TVK6JSHSKeuYPPfE49rIwYI)

[MATLAB](https://in.mathworks.com/products/matlab.html) est un langage de calcul numérique établi utilisé dans le monde universitaire et industriel. Il est développé et licencié par MathWorks, une entreprise fondée en 1984 pour commercialiser le logiciel.

#### Licence

Propriétaire — le prix varie en fonction de votre cas d'utilisation

#### Avantages

* Conçu pour le calcul numérique. MATLAB est bien adapté pour les applications quantitatives avec des exigences mathématiques sophistiquées telles que le traitement du signal, les transformées de Fourier, l'algèbre matricielle et le traitement d'image.
* Visualisation de données. MATLAB dispose de grandes capacités de traçage intégrées.
* MATLAB est souvent enseigné dans le cadre de nombreux cours de premier cycle dans des matières quantitatives telles que la physique, l'ingénierie et les mathématiques appliquées. Par conséquent, il est largement utilisé dans ces domaines.

#### Inconvénients

* Licence propriétaire. Selon votre cas d'utilisation (académique, personnel ou entreprise), vous devrez peut-être payer pour une licence coûteuse. Il existe des alternatives gratuites telles que [Octave](https://www.gnu.org/software/octave/). C'est quelque chose à considérer sérieusement.
* MATLAB n'est pas un choix évident pour la programmation généraliste.

#### Verdict — « meilleur pour les applications mathématiquement intensives »

L'utilisation généralisée de MATLAB dans une gamme de domaines quantitatifs et numériques dans l'industrie et le milieu universitaire en fait une option sérieuse pour la science des données.

Le cas d'utilisation clair serait lorsque votre application ou votre rôle quotidien nécessite une fonctionnalité mathématique intensive et avancée. En effet, MATLAB a été spécifiquement conçu pour cela.

### Autres langages

Il existe d'autres langages grand public qui peuvent ou non intéresser les scientifiques des données. Cette section fournit un aperçu rapide... avec beaucoup de place pour le débat, bien sûr !

#### C++

[C++](https://isocpp.org/) n'est pas un choix courant pour la science des données, bien qu'il offre des performances ultra-rapides et une popularité grand public généralisée. La raison simple peut être une question de productivité contre performance.

Comme [un utilisateur de Quora le dit](https://www.quora.com/Why-dont-data-scientists-use-C-C%2B%2B/answer/Kevin-Lin?srid=hhtiJ) :

> _« Si vous écrivez du code pour faire une analyse ad hoc qui ne sera probablement exécutée qu'une seule fois, préféreriez-vous passer 30 minutes à écrire un programme qui s'exécutera en 10 secondes, ou 10 minutes à écrire un programme qui s'exécutera en 1 minute ? »_

Le gars a un point. Pourtant, pour des performances de niveau production sérieuses, C++ serait un excellent choix pour implémenter des algorithmes de machine learning optimisés à bas niveau.

**Verdict — « pas pour le travail quotidien, mais si la performance est critique... »**

#### JavaScript

Avec l'essor de [Node.js](https://nodejs.org/en/) ces dernières années, [JavaScript](https://en.wikipedia.org/wiki/JavaScript) est devenu de plus en plus un langage côté serveur sérieux. Cependant, son utilisation dans les domaines de la science des données et du machine learning a été limitée à ce jour (bien que vous puissiez consulter [brain.js](https://github.com/harthur/brain) et [synaptic.js](http://caza.la/synaptic/#/) !). Il souffre des inconvénients suivants :

* Arrivé tard dans le jeu (Node.js n'a que 8 ans !), ce qui signifie...
* Peu de bibliothèques et de modules pertinents pour la science des données sont disponibles. Cela signifie qu'il n'y a pas d'intérêt ou d'élan grand public réel.
* En termes de performance, Node.js est rapide. Mais JavaScript en tant que langage [n'est pas sans ses critiques](https://hackernoon.com/the-javascript-phenomenon-is-a-mass-psychosis-57adebb09359).

Les forces de Node résident dans l'I/O asynchrone, son utilisation généralisée et l'existence de [langages qui compilent en JavaScript](https://www.slant.co/topics/101/~best-languages-that-compile-to-javascript). Il est donc concevable qu'un framework utile pour la science des données et le traitement ETL en temps réel puisse se mettre en place.

La question clé est de savoir si cela offrirait quelque chose de différent de ce qui existe déjà.

**Verdict — « il y a beaucoup à faire avant que JavaScript puisse être considéré comme un langage sérieux pour la science des données »**

#### **Perl**

[Perl](https://www.perl.org/) est connu comme un « couteau suisse des langages de programmation », grâce à sa polyvalence en tant que langage de script généraliste. Il partage beaucoup de points communs avec Python, étant un langage de script à typage dynamique. Mais il n'a pas connu la popularité de Python dans le domaine de la science des données.

Cela est un peu surprenant, étant donné son utilisation dans des domaines quantitatifs tels que la [bioinformatique](https://en.wikipedia.org/wiki/BioPerl). Perl présente plusieurs inconvénients majeurs en matière de science des données. Il n'est pas particulièrement rapide, et sa syntaxe est [notoirement peu conviviale](https://en.wikipedia.org/wiki/Write-only_language). Il n'y a pas eu la même impulsion pour développer des bibliothèques spécifiques à la science des données. Et dans tout domaine, l'élan est clé.

**Verdict — « un langage de script généraliste utile, mais il n'offre aucun avantage réel pour votre CV en science des données »**

#### Ruby

[Ruby](https://www.ruby-lang.org/en/) est un autre langage généraliste, interprété et à typage dynamique. Pourtant, il n'a pas connu la même adoption pour la science des données que Python.

Cela peut sembler surprenant, mais est probablement le résultat de la domination de Python dans le milieu universitaire, et d'un effet de rétroaction positive. Plus les gens utilisent Python, plus de modules et de frameworks sont développés, et plus les gens se tourneront vers Python.

Le [projet SciRuby](http://sciruby.com/) existe pour apporter des fonctionnalités de calcul scientifique, telles que l'algèbre matricielle, à Ruby. Mais pour l'instant, Python mène toujours la danse.

**Verdict — « pas un choix évident pour la science des données, mais ne nuira pas au CV »**

### Conclusion

Voilà, vous avez un guide rapide sur les langages à considérer pour la science des données. La clé ici est de comprendre vos exigences d'utilisation en termes de généralité contre spécificité, ainsi que votre style de développement personnel préféré en termes de performance contre productivité.

J'utilise R, Python et SQL régulièrement, car mon rôle actuel se concentre principalement sur le développement de processus de pipeline de données et d'ETL existants. Ces langages offrent le bon équilibre entre généralité et productivité pour faire le travail, avec l'option d'utiliser les packages de statistiques plus avancés de R lorsque nécessaire.

Cependant — vous avez peut-être déjà une certaine expérience avec Java. Ou vous souhaitez utiliser Scala pour le big data. Ou peut-être êtes-vous impatient de vous impliquer dans le projet Julia.

Peut-être avez-vous appris MATLAB à l'université, ou souhaitez-vous donner une chance à SciRuby ? Peut-être avez-vous une suggestion complètement différente. Si c'est le cas, veuillez laisser une réponse ci-dessous — j'ai hâte d'avoir de vos nouvelles !

Merci d'avoir lu !