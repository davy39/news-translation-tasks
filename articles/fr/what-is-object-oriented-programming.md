---
title: Signification de la POO – Qu'est-ce que la Programmation Orientée Objet ?
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2022-09-06T17:15:18.000Z'
originalURL: https://freecodecamp.org/news/what-is-object-oriented-programming
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/OOP--1-.png
tags:
- name: object oriented
  slug: object-oriented
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Signification de la POO – Qu'est-ce que la Programmation Orientée Objet
  ?
seo_desc: 'In today''s technology driven society, computer programming knowledge is
  in high demand. And as a developer, you''ll need to know various programming languages.

  Over the past few decades, many programming languages have risen in popularity.
  You can see...'
---

Dans la société actuelle, où la technologie joue un rôle central, les connaissances en programmation informatique sont très demandées. Et en tant que développeur, vous devrez maîtriser divers langages de programmation.

Au cours des dernières décennies, de nombreux langages de programmation ont gagné en popularité. Vous pouvez voir comment les langages populaires sont classés dans ce tableau de classement en temps réel [ici](https://www.tiobe.com/tiobe-index//).

Alors que de nouveaux langages sont créés, les langages existants sont constamment mis à jour pour les améliorer.

Bien que la plupart des langages de programmation présentent certaines similitudes, chacun a des règles et des méthodes spécifiques qui le rendent unique.

Un concept commun à de nombreux langages de programmation est la **Programmation Orientée Objet**.

Lorsque j'ai rencontré ce terme pour la première fois, il était un peu confus. Il m'a fallu un certain temps pour vraiment comprendre son importance en programmation. Mais cela a également été une opportunité pour moi d'apprendre ses concepts clés et de savoir à quel point il est important pour la carrière d'un développeur et pour résoudre des défis.

Dans cet article, nous allons aborder la Programmation Orientée Objet (POO) dans son ensemble, sans nous appuyer sur un langage particulier. Vous apprendrez ce que c'est, pourquoi c'est si populaire en tant que paradigme de programmation, sa structure, son fonctionnement, ses principes, et plus encore.

Commençons.

# Qu'est-ce que la Programmation Orientée Objet ?

Si vous deviez effectuer une recherche rapide sur Internet pour savoir ce qu'est la programmation orientée objet, vous trouveriez que la POO est définie comme un paradigme de programmation qui repose sur le concept de classes et d'objets.

Maintenant, pour un débutant, cela peut être un peu confus – mais pas besoin de s'inquiéter. Je vais essayer de l'expliquer de la manière la plus simple possible, comme le dit la célèbre phrase "Expliquez-le-moi comme si j'avais 5 ans".

Voici un bref aperçu de ce que vous pouvez réaliser avec la POO : vous pouvez l'utiliser pour structurer un programme logiciel en blocs de code simples et réutilisables (dans ce cas, généralement appelés classes), que vous utilisez ensuite pour créer des instances individuelles des objets.

Alors, trouvons une définition plus simple de la programmation orientée objet et en apprenons davantage à son sujet.

## Expliquer la POO comme si j'avais 5 ans

Le terme "orienté objet" est une combinaison de deux termes, objet et orienté.

La signification dictionnaire d'un objet est "une entité qui existe dans le monde réel", et orienté signifie "intéressé par un type particulier de chose ou d'entité".

En termes simples, la POO est un modèle de programmation qui est construit autour d'objets ou d'entités, donc on l'appelle programmation orientée objet.

Pour mieux comprendre le concept, examinons des programmes logiciels couramment utilisés : Un bon exemple pour expliquer cela serait l'utilisation d'une imprimante lorsque vous imprimez un document.

La première étape consiste à initier l'action en cliquant sur la commande d'impression ou en utilisant des raccourcis clavier. Ensuite, vous devez sélectionner votre imprimante. Ensuite, vous attendrez une réponse vous indiquant si le document a été imprimé ou non.

Derrière ce que nous ne pouvons pas voir, la commande sur laquelle vous avez cliqué interagit avec un objet (imprimante) pour accomplir la tâche d'impression.

Peut-être vous demandez-vous, comment la POO est-elle devenue si populaire ?

# Comment la POO est devenue populaire

Les concepts de la POO ont commencé à émerger dans les années 60 avec un langage de programmation appelé [Simula](https://en.wikipedia.org/wiki/Simula). Même si à l'époque, les développeurs n'ont pas complètement adopté les premières avancées des langages POO, les méthodologies ont continué à évoluer.

Avance rapide jusqu'aux années 80, et un éditorial écrit par David Robinson a été l'une des premières introductions à la POO, car de nombreux développeurs ne savaient pas qu'elle existait.

À cette époque, des langages comme C++ et Eiffel étaient devenus plus populaires et grand public parmi les programmeurs informatiques. La reconnaissance a continué à croître pendant les années 90, et avec l'arrivée de Java, la POO a attiré un grand nombre d'adeptes.

En 2002, en conjonction avec la sortie du .NET Framework, Microsoft a introduit un tout nouveau langage POO appelé C# – qui est souvent décrit comme le langage de programmation le plus puissant.

Il est intéressant de noter que, des générations plus tard, le concept d'organisation de votre code en objets significatifs qui modélisent les parties de votre problème continue de déconcerter les programmeurs.

Beaucoup de personnes qui n'ont aucune idée de comment fonctionne un ordinateur trouvent le concept de programmation orientée objet assez naturel. En revanche, beaucoup de personnes qui ont de l'expérience avec les ordinateurs pensent initialement qu'il y a quelque chose d'étrange dans les systèmes orientés objet.

# Structure de la POO

![Image](https://www.freecodecamp.org/news/content/images/2022/09/OOP.png)

Imaginez que vous gérez une animalerie, avec de nombreuses races différentes et que vous devez suivre les noms, l'âge, les jours de présence et autres détails courants de maintenance. Comment concevriez-vous un logiciel réutilisable pour gérer cela ?

Gardez à l'esprit que nous avons de nombreuses races, donc écrire du code pour chacune serait fastidieux. Mais nous pouvons regrouper les informations connexes ensemble afin de produire un code plus court et plus réutilisable.

C'est là que les blocs de construction entrent en jeu pour nous aider à faire cela en utilisant des **Classes, Objets, Méthodes** et **Attributs**.

Plongeons-nous et comprenons ce que sont exactement ces blocs de construction :

* **Classes** - ce sont des types de données définis par l'utilisateur qui servent de plan pour les objets, les attributs et les méthodes.

* **Objets** - Ce sont des instances d'une classe avec des données spécifiquement définies. Lorsque une classe est définie initialement, la description est le seul objet qui est défini.

* **Méthodes** - Ce sont des fonctions qui sont définies à l'intérieur d'une classe et qui décrivent le comportement d'un objet. Elles sont utiles pour la réutilisabilité ou pour garder la fonctionnalité encapsulée dans un objet à la fois. La réutilisabilité du code est un grand avantage lors du débogage.

* **Attributs** - Ceux-ci sont définis dans le modèle de classe et représentent l'état d'un objet. Les objets contiennent des données stockées dans le champ d'attribut.

# Principes de la POO

![POO](https://www.freecodecamp.org/news/content/images/2021/10/Creative-Business-Template-Presentation--2-.png)

Afin de savoir comment écrire un bon code POO, nous devons comprendre les 4 piliers de la POO auxquels nous devons adhérer :

* Encapsulation
* Abstraction
* Héritage
* Polymorphisme

Plongeons-nous et comprenons mieux ce que chacun de ces termes signifie exactement.

## Encapsulation

C'est le concept qui lie les données ensemble. Les fonctions manipulent les informations et les gardent en sécurité. Aucun accès direct n'est accordé aux informations si elles sont cachées. Si vous souhaitez accéder aux informations, vous devez interagir avec l'article responsable des informations.

Si vous travaillez dans une entreprise, il est probable que vous ayez eu une expérience avec l'encapsulation.

Pensez à un département des ressources humaines. Les membres du personnel des ressources humaines encapsulent (cachent) les données sur les employés. Ils déterminent comment ces données seront utilisées et manipulées. Toute demande de données sur les travailleurs ou demande de mise à jour des informations doit passer par eux.

En encapsulant les données, vous rendez les informations de votre système plus sûres et plus fiables. Vous êtes également en mesure de surveiller comment les informations sont accessibles et quelles opérations sont effectuées sur elles. Cela facilite la maintenance du programme et simplifie le processus de débogage.

## Abstraction

L'abstraction fait référence à l'utilisation de classes simples pour représenter la complexité. Basiquement, nous utilisons l'abstraction pour gérer la complexité en permettant à l'utilisateur de ne voir que les informations pertinentes et utiles.

Un bon exemple pour expliquer cela est la conduite d'une voiture automatique. Lorsque vous avez une voiture automatique et que vous voulez aller du point A au point B, tout ce que vous avez à faire est de lui donner la destination et de démarrer la voiture. Ensuite, elle vous conduira à votre destination.

Ce que vous n'avez pas besoin de savoir, c'est comment la voiture est fabriquée, comment elle prend et suit correctement les instructions, comment la voiture filtre différentes options pour trouver le meilleur itinéraire, et ainsi de suite.

Le même concept est appliqué lors de la construction d'applications POO. Vous faites cela en cachant les détails qui ne sont pas nécessaires pour que l'utilisateur les voie. L'abstraction facilite les choses et vous permet de gérer vos projets en petites parties gérables.

## Héritage

L'héritage permet aux classes d'hériter des caractéristiques d'autres classes. Par exemple, vous pourriez classer tous les chats ensemble comme ayant certaines caractéristiques communes, comme avoir quatre pattes. Leurs races les classent ensuite en sous-groupes avec des attributs communs, comme la taille et la couleur.

Vous utilisez l'héritage en POO pour classer les objets dans vos programmes selon des caractéristiques et des performances communes. Cela facilite le travail avec les objets et la programmation, car cela vous permet de mélanger des caractéristiques générales dans un objet parent et d'hériter de ces caractéristiques dans les objets enfants.

Par exemple, vous définirez un objet employé qui définit toutes les caractéristiques générales des employés dans votre entreprise.

Vous pourrez ensuite définir un objet manager qui hérite des caractéristiques de l'objet employé mais ajoute également des caractéristiques uniques aux managers dans votre entreprise. L'objet manager reflétera automatiquement tout changement dans la mise en œuvre de l'objet employé.

## Polymorphisme

C'est la capacité de deux objets différents à répondre à une seule forme. Le programme déterminera quel usage est critique pour chaque exécution de la chose à partir de la classe parente, ce qui réduit la duplication de code. Il permet également à différents types d'objets d'interagir avec la même interface.

## Exemples de langages POO

La technologie et les langages de programmation évoluent constamment. Nous avons vu l'essor de nombreux langages sous la catégorie POO, mais **Simula** est crédité comme étant le premier langage POO.

Les langages de programmation considérés comme purs POO traitent tout comme des objets, tandis que les autres sont conçus principalement avec un certain processus procédural.

*Exemples de langages POO :*
* Scala
* Emerald
* Ruby
* JADE
* Java
* Python
* C++
* JavaScript
* Visual Basic .NET
* PHP

Et bien d'autres.

## Avantages de la POO

Dans les années 70 et 80, les langages de programmation procéduraux comme C et Pascal étaient largement utilisés pour développer des systèmes logiciels orientés business. Mais à mesure que les programmes exécutaient des fonctionnalités commerciales plus complexes et interagissaient avec d'autres systèmes, les lacunes de la méthodologie de programmation structurée ont commencé à apparaître.

En raison de cela, de nombreux développeurs de logiciels se sont tournés vers les méthodologies et les langages de programmation orientés objet pour résoudre les problèmes rencontrés. Les avantages de l'utilisation de ces langages incluaient les éléments suivants :

* **Réutilisabilité du code** - grâce à l'héritage, vous pouvez réutiliser le code. Cela signifie qu'une équipe n'a pas à écrire le même code plusieurs fois.

* Meilleure intégration avec les systèmes d'exploitation modernes.

* **Productivité améliorée** - les développeurs peuvent construire de nouveaux programmes facilement et rapidement grâce à l'utilisation de plusieurs bibliothèques.

* Le polymorphisme permet à une seule fonction de s'adapter à la classe dans laquelle elle est placée.

* Facile à mettre à niveau, et les programmeurs peuvent également implémenter des fonctionnalités système indépendamment.

* Grâce à l'**Encapsulation**, les objets peuvent être autonomes. Cela facilite également le dépannage et la collaboration sur le développement.

* En utilisant l'encapsulation et l'abstraction, le code complexe est caché, la maintenance du logiciel est plus facile et les protocoles Internet sont protégés.

## Conclusion

Aujourd'hui, la plupart des langages permettent aux développeurs de mélanger les paradigmes de programmation. Cela est souvent dû au fait qu'ils seront utilisés pour diverses méthodes de programmation.

Par exemple, prenons JavaScript – vous pouvez l'utiliser pour la POO et la programmation fonctionnelle. Lorsque vous codez en JavaScript orienté objet, vous devez réfléchir attentivement à la structure du programme et planifier dès le début du codage. Vous pourriez le faire en voyant comment vous pourrez décomposer les nécessités en classes simples et réutilisables qui seront utilisées comme plan pour les instances d'objets.

Les développeurs travaillant avec la POO s'accordent généralement à dire que, en général, son utilisation permet de meilleures structures de données et une réutilisabilité du code. Cela fait gagner du temps à long terme.