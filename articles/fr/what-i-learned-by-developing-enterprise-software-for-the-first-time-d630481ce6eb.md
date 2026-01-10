---
title: Ce que j'ai appris en développant des logiciels d'entreprise pour la première
  fois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-23T19:58:26.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-by-developing-enterprise-software-for-the-first-time-d630481ce6eb
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/1_B1ynrF6ECoTQyPmwWRAxag.jpeg
tags:
- name: Career
  slug: career
- name: software development
  slug: software-development
seo_title: Ce que j'ai appris en développant des logiciels d'entreprise pour la première
  fois
seo_desc: 'By David

  In this article, I’ll share ten lessons I learned from my first project as a self-taught
  software developer. I was working for a consulting company at the time, and my official
  title was Software Engineer. The project I worked on was a web a...'
---

Par David

Dans cet article, je partagerai dix leçons que j'ai apprises lors de mon premier projet en tant que développeur logiciel autodidacte. Je travaillais pour une société de conseil à l'époque, et mon titre officiel était Software Engineer. Le projet sur lequel j'ai travaillé était une application web pour le secteur public.

#### Leçon n°1 : apprenez l'architecture dès que possible

Au début, la partie la plus difficile a été de s'habituer à la quantité de code écrit. Il devait y avoir au moins un million de lignes de code au moment où j'ai commencé ! C'est devenu beaucoup plus facile après avoir découvert l'architecture que nous utilisions. Je me souviens avoir été confus à ce sujet à l'époque.

Ce n'est que lorsque j'ai suivi un cours intensif sur la [layered architecture](https://en.wikipedia.org/wiki/Multitier_architecture), proposé par l'entreprise, que j'ai vraiment compris comment naviguer dans la base de code. J'en avais reçu un bref aperçu à mes débuts, mais j'aurais aimé avoir une meilleure compréhension plus tôt.

#### Leçon n°2 : ne prenez pas de raccourcis avec l'architecture

À mi-parcours de mon temps sur le projet, nous avons ajouté beaucoup de nouvelles fonctionnalités. Nous avons pu en réaliser une partie avec des technologies plus récentes. Comme je ne comprenais toujours pas vraiment la valeur de l'architecture que nous utilisions, j'ai décidé de prendre des raccourcis. Cela a fini par coûter du temps et des ressources lorsque nous avons dû revenir en arrière pour corriger le tir.

#### Leçon n°3 : ne sous-estimez pas la valeur du contexte métier

Une partie importante du projet consiste à apprendre les exigences métier. J'ai complètement sous-estimé l'importance de cela pendant toute la durée du projet. Ce fut une erreur coûteuse. Si vous ne comprenez pas le contexte métier de votre travail, il est très facile de s'engager sur la mauvaise voie.

#### Leçon n°4 : ne sous-estimez pas la valeur d'être autodidacte

Ce projet m'a permis de gagner beaucoup de confiance en mes capacités de développeur. Je crois fermement que, si vous avez les bons outils, vous pouvez devenir un expert dans n'importe quel domaine.

Bien que je ne prétende pas être un expert, mon [matériel d'apprentissage autodidacte](http://learnitmyway.com/2016/11/11/learning-material-software-development/) était plus que suffisant pour me préparer à ce projet. Gardez à l'esprit — la liste était beaucoup plus courte quand j'ai commencé ! Cette révélation m'a inspiré à écrire [Est-ce que faire des études en valait la peine ?](http://learnitmyway.com/2016/10/12/was-studying-worth-it/)

#### Leçon n°5 : écrivez des tests rapides et supprimez ceux qui deviennent obsolètes

Notre projet comprenait de nombreux tests. Nous avions une suite de tests autonome qui exécutait des tests unitaires, des tests de persistance et des tests d'intégration. Les tests unitaires prenaient quelques minutes, mais l'ensemble prenait une heure entière ! J'ai réalisé que les tests rapides sont les meilleurs, et qu'il ne sert à rien de s'accrocher à de vieux tests devenus obsolètes.

#### Leçon n°6 : méfiez-vous des conséquences de committer moins souvent

Nous utilisions [Subversion](https://subversion.apache.org/) pour notre contrôle de version. Malheureusement, le code que nous committions était automatiquement envoyé dans le dépôt. Nous travaillions très rarement avec des branches, car le coût d'opportunité semblait trop élevé. Cela a conduit à committer du code moins souvent. J'essayais toujours de Commit fréquemment, mais il m'arrivait de casser le build — je ne pensais pas avoir besoin d'investir une heure pour lancer les tests localement.

#### Leçon n°7 : écrivez des tests fiables — et n'oubliez pas de les maintenir

En plus de cela, certains tests n'étaient pas toujours au vert. Ils fonctionnaient parfois, mais échouaient tout aussi souvent. Cela rendait le build rouge. En conséquence, je n'appréciais pas vraiment la valeur d'un build rouge. Parfois, le build restait rouge pendant des jours parce que personne n'avait remarqué qu'un autre test avait été cassé.

#### Leçon n°8 : revoyez le code dès que possible

En règle générale, nous avions un développeur qui écrivait le code et un autre qui le révisait. J'ai eu l'occasion de faire les deux. Souvent, je recevais une fonctionnalité à développer. Avant de la terminer, on me donnait quelque chose à réviser. Il pouvait s'écouler des jours avant que je ne trouve le temps de faire la revue.

Cela causait souvent des maux de tête, car le code que je révisais n'était plus le même que celui qui avait été développé. Le [Pair programming](https://en.wikipedia.org/wiki/Pair_programming) aurait permis d'éviter ce problème, mais ce n'était pas notre façon de travailler.

#### Leçon n°9 : le refactoring doit être accompagné de tests

Les tests n'ont été introduits que cinq ans après le début du projet. Avant cela, tous les tests étaient effectués manuellement. Cela signifiait qu'une grande partie de la base de code n'avait aucune couverture de test, ce qui est dangereux.

Personnellement, j'aime beaucoup l'idée d'appliquer la [boy scout rule](http://programmer.97things.oreilly.com/wiki/index.php/The_Boy_Scout_Rule) au code. J'avais naturellement tendance à beaucoup refactoriser. Mais comme nous n'avions pas de couverture de test pour tout ce que je refactorisais, j'introduisais parfois des défauts dans notre logiciel.

#### Leçon n°10 : le développement de logiciels est un compromis entre la valeur métier et l'excellence logicielle

Nous utilisions un [V-model](https://en.wikipedia.org/wiki/V-Model) pour le processus de développement logiciel. Cela incluait des délais pour le développement, les tests manuels et la mise en production du logiciel. Nous n'avions pas un temps illimité pour développer ou réviser le code que nous écrivions. Dans certains cas, je passais trop de temps à perfectionner le code, ce qui n'apportait pas toujours de valeur métier.

#### Dernières pensées

Ce projet a été une expérience d'apprentissage très précieuse pour moi. J'espère que vous avez également pu en tirer quelque chose. Faites-le moi savoir dans les commentaires ci-dessous si vous avez eu des expériences similaires ou contrastées !

---

**Avant de partir…** Merci d'avoir lu l'article ! J'écris sur mes expériences professionnelles et éducatives en tant que développeur logiciel autodidacte, alors n'hésitez pas à consulter [mon blog](https://www.learnitmyway.com/) ou à vous abonner à [ma newsletter](https://learnitmyway.com/newsletter) pour plus de contenu.

**Vous pourriez aussi aimer :**

* [Matériel d'apprentissage — développement logiciel](http://learnitmyway.com/2016/11/11/learning-material-software-development/) (mon parcours d'apprentissage commençant par l'introduction à l'informatique)
* [Tester Apollo Server avec Typescript](https://learnitmyway.com/apollo-server-testing/)
* [Est-ce que faire des études en valait la peine ?](http://learnitmyway.com/2016/10/12/was-studying-worth-it/)