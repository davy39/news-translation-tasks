---
title: Comment j'ai construit un portail RH sur Angular 4 et Magento
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-23T09:59:14.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-an-online-hrm-management-portal-on-angular-4-magento
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/background-close-up-computer-2740956-1.jpg
tags:
- name: Angular
  slug: angular
- name: Angular
  slug: angularjs
- name: app development
  slug: app-development
- name: Magento
  slug: magento
- name: PHP
  slug: php
- name: software development
  slug: software-development
seo_title: Comment j'ai construit un portail RH sur Angular 4 et Magento
seo_desc: "By Shifa Martin\nSometimes trying a new technology mashup works wonders.\
  \ Both Magento 2 + Angular 4 are very commonly talked about, and many consider them\
  \ to be the future of the development industry. \nFor example, I recently used Magento\
  \ + Angular 4 ..."
---

Par Shifa Martin

Parfois, essayer un nouveau mélange de technologies fait des miracles. Magento 2 + Angular 4 sont très souvent mentionnés, et beaucoup les considèrent comme l'avenir de l'industrie du développement. 

Par exemple, j'ai récemment utilisé Magento + Angular 4 pour construire un [portail de gestion des ressources humaines](https://www.valuecoders.com/case-studies/hr-management-portal) super-efficace.

## Apprendre avec les meilleurs exemples

L'une des fonctionnalités les plus recherchées d'un portail RH est « gérer des exigences diverses rapidement ». Cela signifie que le département des ressources humaines a besoin d'un logiciel pour gérer l'ensemble du cycle de vie de la performance des employés et d'autres activités RH en un clic. Par exemple, gérer l'intégration des employés, les évaluations de performance, la formation et le développement, la gestion des congés, la gestion des griefs, les processus disciplinaires, etc. Ensuite, ils examinent le résultat final.

> Le portail RH que j'ai construit est un logiciel de gestion en ligne intuitif qui a rapporté jusqu'à 90 pour cent de meilleure performance que d'autres outils. Cependant, il souffrait de nombreux défis tels que la vitesse du logiciel, la qualité de la sortie et la promptitude. 

### Défis

Un utilisateur entre généralement de nombreuses détails en combinaisons et fait un va-et-vient entre l'étape 1 et l'étape 2. Chaque fois que l'utilisateur passe d'un onglet à l'autre, toutes les détails de l'employé sont rechargées. Cela est ennuyeux et le risque d'abandon de l'utilisateur est élevé.

Le prototype d'un tel portail RH indépendant fonctionnait très bien. Cependant, le développer était une tâche complexe. Nos développeurs ont dû faire fonctionner AngularJS et Magento (PHP) ensemble en dernier recours. 

Mon entreprise [ValueCoders, société de développement logiciel](https://www.valuecoders.com/), qui est un leader mondial dans les solutions IT et logicielles, dispose de sa propre équipe de développement qui a travaillé d'arrache-pied sur ce portail RH. 

## Pourquoi Magento avec Angular 4 pour le portail RH ?

Avant de venir nous voir, notre client avait déjà reçu des offres de différentes agences de développement. Et, en tant que service amical, mon équipe a été chargée d'examiner toutes ces idées pour leur portail RH. Mais, j'ai été surpris de voir que l'une d'entre elles n'avait envoyé qu'une seule chose : elles allaient construire le portail RH avec le framework basé sur TypeScript, Angular. 

Et ce n'était pas tout. Ils avaient même essayé de cacher le fait que cette technologie n'était pas suffisante pour construire le portail RH. Au lieu de cela, ils ont promu leur marque et ont également proposé un prix qui ne justifiait pas la création d'un portail RH en ligne avec des propositions de haute qualité. 

**Le cœur du problème est de savoir pourquoi nous avons utilisé Magento avec AngularJS pour le portail RH.**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/giphy--1--1.gif)

Sans aucun doute, Magento est l'un des systèmes CMS open-source les plus populaires écrits en PHP, ce qui justifie que chaque e-portail doit être unique. Avec ses fonctionnalités prêtes à l'emploi, son architecture open-source et son API REST, Magento offre une capacité inégalée pour personnaliser et intégrer des tiers à votre application, que vous ne pouviez que rêver. 

Cependant, la montée de la connectivité internet, des smartphones et des tablettes a directement affecté le marché des CMS e-commerce. Aujourd'hui, les clients ne s'attendent pas seulement à ce qu'un e-portail ou un portail RH soit unique, mais ils veulent aussi qu'il fonctionne rapidement et de manière transparente. Dans une tentative d'apporter une sensation native au site web, le plus grand avantage d'un framework JavaScript MVC comme AngularJS. Certains le louent comme l'avenir de l'industrie du développement e-commerce et d'autres l'appellent un gadget à la mode.

Avoir un framework MVC signifie que les clients peuvent naviguer à travers le portail RH de page en page ou de vue en vue et non comme un livre. Cela signifie qu'au lieu de rafraîchir toute la page web, l'utilisateur navigue vers une page interne et seule la section pertinente sera mise à jour. Le résultat est un portail RH à chargement ultra-rapide car les pages internes du site web ne se chargent jamais. 

Expliquer l'intégralité d'AngularJS et de Magento dépasse le cadre de cet article, mais nous allons examiner des extraits de code rapides pour un guide complet sur le tutoriel HRM.

Avant de passer à des détails plus techniques, une brève introduction du type de portail RH avec lequel nous avons traité ici semble appropriée.

## Fonctionnalités du portail RH

![Image](https://www.freecodecamp.org/news/content/images/2019/10/5d55e5d304e085e83b57aeda747ee0eb.jpg)

Le client est la principale plateforme HRIS d'Australie qui gère l'ensemble du cycle de vie des employés en un clic. Ils aident à centraliser les activités RH et à améliorer l'efficacité de votre entreprise avec de nombreuses fonctionnalités géniales.

Après quelques discussions avec le client, quelques spécifications ont été cristallisées :

* Développer un portail RH pour gérer et faciliter toutes les fonctions du département des ressources humaines dans les entreprises qui traitent la paie, la performance, la gestion des employés, le recrutement, la formation, etc.
* Le côté client doit être solide et capable de gérer des exigences diverses rapidement.
* Développer un portail RH qui offre une manière intelligente de gérer le HRM et d'économiser à la fois de l'argent et du temps.
* Aucune perte de qualité du site web.

Ce sont des fonctionnalités assez bonnes pour un portail RH. C'est exactement ce que notre client veut de nous avec un nouveau mélange de technologies. Donc, si vous voulez connaître le résultat final, voici un aperçu du codage sur Angular 4 pour le portail RH.

C'est ce que j'ai essayé de faire. Et j'ai fait un coup de maître. Maintenant que j'ai couvert toutes les choses contextuelles, je peux enfin vous emmener vers des choses plus techniques.  

Voici l'une des fonctionnalités du portail RH qui est la structuration organisationnelle ou le treemapping, où un utilisateur peut vérifier les détails complets d'un employé en entrant l'identifiant de l'employé, le nom, le département ou le type d'opérations. Cet outil vous donne une méthode pour afficher des données hiérarchiques en utilisant des figures imbriquées et en un seul clic sur la touche Entrée.

### Codons avec Angular 4 :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/coding-1.png)
_Codage sur Angular 4 pour l'organigramme/détails des employés_

![Image](https://www.freecodecamp.org/news/content/images/2019/10/coding-on-angular.png)
_Codage sur Angular 4 pour l'organigramme/détails des employés_

> Après avoir préparé la base du portail RH en utilisant Angular 4, l'un des premiers défis était d'ajouter des fonctionnalités dans un environnement de développement différent.

### Voici une autre illustration avec les codes PHP : 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/happyHr1-php-1-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Happyhr2-php-2-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/php-new-01-2.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/php-new-02-2.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/php-new-03-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/php-new-04-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/php-new-05.png)

En considérant les exemples ci-dessus, espérons que cela fera économiser à quelqu'un là-bas une quantité raisonnable de temps et d'efforts passés dans le codage pour obtenir ce type de portail RH prêt pour votre entreprise. 

## Pour résumer mon expérience

Ce projet de portail RH m'a appris l'intégration continue, le déploiement et la surveillance de la solution logicielle avant de la soumettre à une nouvelle version dans les magasins d'applications. Cependant, quelques choses simples que je considère encore comme nécessaires :

* L'entreprise cliente veut toujours automatiser tout ce qui peut être automatisé. Cela n'est possible qu'avec une équipe de développeurs. J'étais donc déterminé à embaucher des développeurs Angular qui ont une expérience souhaitable dans l'industrie et peuvent rendre le processus de développement aussi facile que possible.
* Si une chose est sûre dans le développement de votre portail RH, c'est que vous prendrez l'aide de développeurs dédiés avant de commencer le processus de développement réel de l'application/web.     

Admettons que la technologie est en constante évolution et loin d'être parfaite. Mais moi et de nombreux autres développeurs n'hésiterions pas à les utiliser encore et encore. Comme toujours, si vous cherchez de l'aide pour le développement de portails RH, n'hésitez pas à [nous contacter](https://www.valuecoders.com/contact). 

Et, si vous cherchez des [développeurs Angular expérimentés](https://www.valuecoders.com/hire-developers/hire-angularjs-developers), des [développeurs Magento](https://www.valuecoders.com/hire-developers/hire-magento-developers) et que vous êtes intéressé à les embaucher pour votre prochain projet de portail RH, l'équipe de développement logiciel de ValueCoders est là pour vous aider ! 	 

> Connectez-vous avec moi sur Twitter pour plus de mises à jour sur les futurs articles/tutoriels : [https://twitter.com/ValueCoders](https://twitter.com/ValueCoders)