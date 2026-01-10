---
title: Un voyage personnel à travers les langages de la science des données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T00:44:24.000Z'
originalURL: https://freecodecamp.org/news/a-personal-journey-through-the-languages-of-data-science-48f516cbb81c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U9aYgROZ2pa4Aa78VZL2Ww.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: programming languages
  slug: programming-languages
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un voyage personnel à travers les langages de la science des données
seo_desc: 'By Elena Nisioti

  One does not simply walk into TensorFlow.

  A PhD is a good opportunity for introspection. In fact, it is important to create
  opportunities for introspection no matter how busy or insignificant the present
  feels like.

  We should not reg...'
---

Par Elena Nisioti

**On ne se lance pas simplement dans TensorFlow.**

Un doctorat est une bonne opportunité pour l'introspection. En fait, il est important de créer des opportunités pour l'introspection, peu importe à quel point le présent semble occupé ou insignifiant.

Nous ne devrions pas considérer notre passé comme une période immature, mais comme une histoire qui se déroule. Une histoire de découvertes, d'erreurs, de compétences et de projets qui font maintenant partie de notre conscience professionnelle.

Peu importe la qualité d'un tutoriel, la précision d'un article ou la conception d'une bibliothèque, tout se résume à l'assimilation personnelle lorsque vous apprenez un nouvel outil. Et quelle est cette qualité personnelle qui façonne nos filtres réceptifs, de sorte que le langage préféré d'une personne est le cauchemar d'une autre ? (Mon cauchemar personnel est **de faire ma programmation quotidienne en C.**)

Le passé. C'est de cela que cet article va parler. Un récit de mes tentatives d'utilisation de MATLAB, Weka, R, C++ et Python dans ma carrière en science des données.

La science des données est un domaine vaste, employant des personnes issues d'une grande variété de milieux, comme l'économie, la biologie et la linguistique. Bien que la science des données soit issue d'un contexte purement statistique, elle a rapidement détourné le domaine de l'informatique et est aujourd'hui un outil aussi polyvalent et essentiel qu'une calculatrice.

En conséquence, la palette des langages de programmation pour la science des données ressemble un peu à l'univers : une vie ne suffit pas pour l'explorer, et il est en constante expansion.

Nous savons qu'il y a des compromis impliqués avec la généralité, la puissance et la complexité d'un langage. Par conséquent, la popularité d'un langage ne devrait servir que d'indication des tendances actuelles, et non de facteur pour déterminer votre propre choix. En fin de compte, c'est une question d'application, d'expérience et de goût.

### MATLAB

J'ai été initiée au monde de l'apprentissage automatique grâce à [un cours en ligne](https://www.coursera.org/learn/machine-learning) enseigné par Andrew Ng. Je le recommande encore aujourd'hui aux personnes cherchant une introduction en douceur dans le monde admettons effrayant de l'apprentissage automatique.

Bien que Python et R étaient beaucoup plus populaires à cette époque, Andrew a choisi MATLAB pour les devoirs du cours. Cela ne me dérangeait guère à l'époque, mais cela semble étrange ces jours-ci. Les cours de science des données se concentrent davantage sur la manière d'utiliser un langage (ou une bibliothèque) pour faire de l'analyse de données que sur la manière de faire de l'analyse de données en utilisant un langage.

En rétrospective, je vois qu'Andrew a opté pour un langage généraliste. Un langage que son public, composé principalement d'étudiants en informatique et en ingénierie, connaissait probablement déjà. Comme l'objectif du cours était de mettre en œuvre des algorithmes d'apprentissage sans utiliser de bibliothèques, MATLAB était aussi bon que n'importe quel langage spécialisé.

Bien que fan d'outils automatisés et de bibliothèques pratiques, je ne peux pas insister assez sur l'importance de l'attitude "faites-le vous-même" envers les algorithmes de science des données au début de votre parcours.

> J'ai très tôt appris la différence entre connaître le nom de quelque chose et connaître quelque chose. — Richard Feynman

MATLAB ne manque pas de bibliothèques pour effectuer une large sélection de tâches d'analyse de données et d'apprentissage automatique. Je suis sûre que c'est le framework préféré des personnes qui en sont adeptes, comme les ingénieurs en traitement du signal et en contrôle.

Mais il n'est pas difficile de comprendre pourquoi il n'a pas conquis le domaine de l'analyse de données, et moi. C'est un outil très coûteux. Son alternative gratuite, Octave, est loin d'être son égale. Il se pourrait aussi que je n'ai jamais été fan des langages qui ne commencent pas à compter à partir de zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/wBmD4fCLR6Mkl5LedyoauCvlnbbC8HVLEjiR)
_Cela ne doit pas toujours planter._

### Weka

Mon expérience avec Weka a été de courte durée. Nous l'avons découvert comme un outil optionnel pour un devoir du cours de Reconnaissance de Formes à mon université.

Sans aucune intention de sous-estimer les compétences que j'ai acquises grâce à ce cours, la leçon la plus précieuse a été celle-ci : l'effet qu'une interface graphique a sur le scientifique des données est profond. Weka se vante de sa facilité d'utilisation et de sa compréhensibilité, offrant la possibilité d'entraîner un modèle d'apprentissage automatique en chargeant un ensemble de données et **en appuyant simplement sur un bouton**. Il n'est pas difficile de voir les avantages de cette approche. Il existe un marché mondial désespéré pour des modèles de prédiction et pas assez d'experts pour satisfaire ces besoins.

Trouver des outils automatisés et les utiliser pour dériver des solutions prêtes à l'emploi est un domaine de recherche actuel, appelé [AutoML](http://www.ml4aad.org/automl/), mais il nous a fallu quelques années, et des échecs, pour réaliser que nous avons besoin **d'un humain dans la boucle**.

L'illusion que nous pouvons produire de bons modèles pour des problèmes réels sans d'abord avoir une bonne compréhension des données s'est effondrée, avec des échecs tels que [MarketSwitch et KXEN](https://blog.datarobot.com/automated-machine-learning-short-history), à la fin des années 90. Les outils automatisés peuvent faciliter notre travail, en découvrant de bonnes paramétrisations des algorithmes, des étapes de pré-traitement utiles et des pipelines de test efficaces. Mais ils ne peuvent pas remplacer l'expert humain, du moins avec notre niveau actuel d'expertise.

En fin de compte, vous devez prendre la responsabilité des modèles que vous créez.

> « Homme, » m'écriai-je, « que tu es ignorant dans ta fierté de sagesse ! » — Mary Wollstonecraft Shelley, Frankenstein

### R

Je me suis plongée dans les mystères et les merveilles de R pendant mon mémoire de diplôme. Vous avez probablement entendu dire que R est un enfant spécial dans la famille des langages d'analyse de données. Mais une courbe d'apprentissage abrupte est un euphémisme pour les sentiments de doute de soi et de désorientation totale que j'ai éprouvés au début du déploiement.

Notre objectif était de créer un outil logiciel pour l'exécution automatisée d'expériences d'apprentissage automatique. R était plus un but qu'un moyen, car nous voulions mener une recherche approfondie sur les techniques d'apprentissage automatique en utilisant le riche dépôt de bibliothèques R.

Devant mettre en place un framework complet, je voulais utiliser les merveilles de la programmation orientée objet dans ma conception. Donc, la première question que j'ai dû aborder était : R supporte-t-il l'orientation objet ? Oui ! En fait, de quatre manières différentes. Aucune ne correspond directement à la programmation orientée objet que j'avais expérimentée en C++, Java ou Python.

Les différentes manières sont apparues progressivement alors que les besoins de la communauté R étaient encore en cours de découverte et que des méthodes pour définir et regrouper facilement des fonctionnalités étaient nécessaires. Sans plan clair pour les qualités de classe souhaitées, il n'est pas surprenant que vous ayez maintenant la liberté (ou devrais-je dire le fardeau) de choisir entre les classes S3, S4, référence et R6. Il existe aujourd'hui quelques [ressources](https://www.cyclismo.org/tutorial/R/objectOriented.html) sur ce sujet, mais il suffit de dire que si votre projet nécessite une orientation objet, alors R n'est probablement pas le langage à choisir.

Après m'être décidée pour les classes de référence, j'ai commencé à donner vie à mon squelette logiciel. J'ai rapidement réalisé que R s'est apparemment développé avec — ce que j'appelle — le [principe de la plus grande surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment). Spécialisé dans l'analyse de données, R doit offrir de nombreux outils pratiques, tels que les structures de données élégantes appelées data.frames, qui capturent élégamment les caractéristiques et les besoins d'un ensemble de données.

Cependant, je me souviens de certaines subtilités techniques dans R qui m'ont donné des cauchemars à l'époque. Cinq opérateurs d'assignation différents. Toutes les variables sont faiblement typées, sauf si elles ne le sont pas. RStudio, une interface utilisateur gratuite pour R, génère une erreur d'exécution si un graphique ne tient pas dans son plan. Quelqu'un a mentionné les espaces de noms ?

Les gens décident de nommer leur package SVM "e1071" au lieu de quelque chose de plus intuitif, et c'est ainsi que vous devez le charger. Vous voulez effectuer la même opération, par exemple l'entraînement, et différents packages utilisent différents noms pour cela. C'est fastidieux de devoir lire le manuel de différents packages pour effectuer la même action. Cela conduit également à de nombreux bugs, si vous ignorez les manuels parce que vous supposez une cohérence.

Jusqu'à ce point, j'ai probablement donné l'impression que je n'aime pas R. Mais ce n'est pas le cas. Bien que je ne tenterais plus jamais de construire un framework à partir de zéro en R, l'abondance de packages fournie par la communauté R open source et hétéroclite peut vous aider à faire des visualisations et un pré-traitement de pointe. C'est cool pour les expériences autonomes.

En ce qui concerne l'apprentissage automatique, il existe un remède au manque de compatibilité entre différents packages. Il s'appelle [**caret**](http://topepo.github.io/caret/index.html) et est une tentative de fournir des interfaces communes pour le pré-traitement, l'entraînement et la réalisation de prédictions qui supportent de nombreux packages utiles, tels que [**nnet**](https://cran.r-project.org/web/packages/nnet/index.html) pour les réseaux de neurones et svmRadial pour les machines à vecteurs de support. Notre [outil automl](https://github.com/issel-ml-squad/ads) aurait été (beaucoup plus) un désordre, si nous n'avions pas exploité l'utilité de caret.

### C++

Maintenant, pourquoi feriez-vous de l'analyse de données en C++ ? Pourquoi quelqu'un le ferait-il ?

Puisqu'un stage d'été est ma seule expérience dans un lieu de travail non académique, je ne suis pas une experte de la psychologie d'une grande entreprise lorsqu'il s'agit de choisir les outils de ses employés. Je suppose que c'était une combinaison de tradition et de besoin de code commercial, efficace en temps d'exécution.

Néanmoins, j'ai décidé de réaliser mes expériences en R et, lorsque la fin du stage approchait, je pourrais transférer mes modèles et fonctions en C++. Qu'est-ce qui pourrait mal se passer ?

J'ai rapidement découvert qu'il n'est pas difficile d'impressionner les personnes qui font de l'analyse de données en C++ avec des diagrammes élégants et des techniques de pré-traitement impressionnantes utilisant des packages R. Certains de mes collègues se sont même intéressés à R et ont commencé à expérimenter avec, ce qui m'a rendu plutôt fière car je suis généralement mauvaise pour persuader les gens.

Après avoir obtenu des résultats satisfaisants, en utilisant des packages R simples pour l'ACP et les machines à vecteurs de support, je me suis lancée dans l'incorporation de mes modèles dans le framework C++ existant (et impressionnamment volumineux). Le package libsvm [package](http://ftp.auckland.ac.nz/software/CRAN/doc/packages/kernlab.pdf) semblait être approprié pour mon cas, offrant des opérations liées aux machines à vecteurs de support.

Maintenant, il y a plusieurs options lorsque vous voulez transférer des modèles d'apprentissage automatique entre des langages, agissant à différents niveaux du problème. En allant du simple au sophistiqué, on peut transférer le modèle mathématique, c'est-à-dire la paramétrisation de l'algorithme, traduire le fichier de modèle entre les bibliothèques, ou utiliser un package pour interfacer entre les langages.

J'ai appris à mes dépens que simplement utiliser la même paramétrisation n'est pas suffisant. Bien que la famille d'algorithmes reste la même — dans mon cas, les SVM avec un noyau gaussien — différentes implémentations peuvent adopter différents modèles mathématiques, nécessitant ainsi différents ensembles de paramètres. Même si les modèles restent les mêmes, des facteurs spécifiques à l'implémentation peuvent affecter les performances du modèle de manière si drastique que différentes paramétrisations sont nécessaires.

La manière la plus appropriée semble être [**rcpp**](https://cran.r-project.org/web/packages/Rcpp/index.html), un package qui interface élégamment entre les frameworks C++ existants et les scripts R. La compatibilité entre les bibliothèques des deux langages différents est également supportée par certains packages, mais c'est rarement le cas. Parfois, le réentraînement est la solution la plus facile et la plus fiable.

Après cette expérience avec l'aspect scientifique des données de C++, j'ai reconsidéré mon jugement sévère sur l'attitude laxiste de R.

### Python

L'une des premières discussions avec mon superviseur actuel a été :

-Alors, quel langage allez-vous utiliser pour vos futures expériences ?

-Je pense que je vais opter pour Python.

-Alors, vous êtes expérimentée avec Python ?

-Non, j'ai juste traversé beaucoup de choses et j'ai un très bon pressentiment à ce sujet.

Heureuse que mes arguments horriblement insuffisants l'aient persuadé, je profite maintenant des avantages de faire de l'analyse de données en Python. La facilité de mise en place des expériences, l'ajout de fonctionnalités et le bénéfice de bibliothèques riches ont vraiment fait avancer mon travail. Bien que j'écrive largement mon propre code, j'ai jusqu'à présent utilisé **OpenAI gym** pour définir mon propre environnement pour les expériences d'apprentissage par renforcement, et **TensorForce**, une bibliothèque qui étend **TensorFlow** avec une grande sélection d'algorithmes d'apprentissage par renforcement.

Néanmoins, je ne plaiderai pas en faveur d'une supériorité incontestable de Python, car cela irait à l'encontre de mon propos. Les programmeurs ont tendance à solidifier leurs croyances en des déclarations fortes sur les langages. Probablement en oubliant qu'il ne peut pas y avoir **un langage pour les gouverner tous**. S'il y en avait un, il devrait être si général qu'il ne pourrait pas être si efficace.

Alors, la prochaine fois que vous serez face à un nouvel ensemble de données, n'ayez pas peur d'ajouter une autre flèche logicielle à votre carquois de science des données. Si tout le reste échoue, vous aurez au moins quelque chose à critiquer.

> La vie ne peut être comprise qu'en regardant en arrière ; mais elle doit être vécue en regardant vers l'avant — Søren Kierkegaard