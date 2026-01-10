---
title: Comment écrire une bonne documentation
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-12-21T21:00:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-good-documentation
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/cover-1.png
tags:
- name: docs
  slug: docs
- name: documentation
  slug: documentation
- name: Infrastructure as code
  slug: infrastructure-as-code
seo_title: Comment écrire une bonne documentation
seo_desc: 'In this article, I''ll discuss the secret to never forgetting how your
  project works, in three steps.

  If you’ve ever half-written a software project before taking a few days off, this
  is the article you’ll discover you needed when you reopen that IDE....'
---

Dans cet article, je vais discuter du secret pour ne jamais oublier comment fonctionne votre projet, en trois étapes.

Si vous avez déjà écrit à moitié un projet logiciel avant de prendre quelques jours de congé, cet article est celui que vous découvrirez avoir besoin lorsque vous rouvrirez cet IDE.

![Votre projet le vendredi (un puzzle terminé) vs le lundi (un tas de pièces de puzzle) comic](https://www.freecodecamp.org/news/content/images/2020/12/friday-monday.png)
_Ne vous inquiétez pas, tout se remettra en place d'ici vendredi... (Comic par l'auteur)_

Dans les équipes technologiques que je dirige, nous faisons un effort constant pour documenter toutes les choses. La documentation vit aux côtés du code en tant que joueur à part entière.

Cela aide à garantir que personne n'a besoin de faire des suppositions sur le fonctionnement de quelque chose, ou de convoquer de longues réunions pour acquérir des connaissances de travail sur une fonctionnalité. Une bonne documentation nous fait gagner beaucoup de temps et d'ennuis.

Cela dit, et contrairement à la croyance populaire, la documentation logicielle la plus précieuse n'est pas principalement écrite pour les autres. Comme je l'ai dit dans ce tweet bien reçu :

> Le secret d'une bonne documentation est de l'écrire pendant que vous écrivez le code. Vous êtes votre premier public. Expliquez ce que vous faites à vous-même. Votre futur vous remerciera !

> — Victoria Drake [24 novembre 2020](https://twitter.com/victoriadotdev/status/1331262801797652483?ref_src=twsrc%5Etfw)

Voici trois étapes concrètes que vous pouvez suivre pour écrire une bonne documentation avant qu'il ne soit trop tard.

## 1. Commencez avec des notes précises

Alors que vous travaillez sur des idées dans le code, assurez-vous de ne pas oublier rapidement les détails importants en commençant par des notes précises. Bien que vous voudrez expliquer les choses à vous-même sous forme longue plus tard, des notes courtes suffiront à capturer les détails sans interrompre le flux de votre session de codage.

Gardez un document ouvert à côté de votre code et notez des choses comme les commandes, les décisions et les sources que vous utilisez. Cela peut inclure :

* Les commandes du terminal que vous avez tapées
* Pourquoi vous avez choisi une méthode particulière plutôt qu'une autre
* Les liens que vous avez visités pour obtenir de l'aide ou de l'_inspiration_ de copie-collage
* L'ordre dans lequel vous avez fait les choses

Ne vous inquiétez pas des phrases complètes à ce stade. Assurez-vous simplement de capturer avec précision le contexte, les extraits de code pertinents et les URL utiles. Il peut également être utile d'activer toute option d'enregistrement automatique disponible.

## 2. Expliquez les décisions en forme longue

Le moment idéal pour aborder cette étape est lorsque vous faites une pause dans le codage, mais avant de complètement passer à autre chose sur ce que vous travaillez actuellement.

Vous voulez vous assurer que le contexte, les idées et les décisions sont encore frais dans votre esprit lorsque vous les expliquez à vous-même.

Passez en revue les notes courtes que vous avez prises et commencez à les développer en écriture conversationnelle. Soyez votre propre canard en plastique. Décrivez ce que vous faites comme si vous l'enseigniez à quelqu'un d'autre. Vous pourriez aborder des sujets tels que :

* Décisions qui semblent étranges : « Je ferais normalement cela de cette manière, mais j'ai choisi de faire quelque chose de différent parce que... »
* Les défis que vous avez rencontrés et comment vous les avez surmontés
* Décisions architecturales qui soutiennent vos objectifs de projet

En restez aux points principaux. L'écriture en forme longue ne signifie pas que vous serez payé au mot ! Utilisez simplement des phrases complètes et écrivez comme si vous expliquiez votre projet à un collègue. Après tout, vous expliquez à votre futur vous.

## 3. Ne négligez pas les connaissances préalables

Cette étape est mieux faite après une longue pause déjeuner, ou même le lendemain (mais probablement pas deux jours après). Relisez votre document et comblez les lacunes qui deviennent apparentes après avoir mis une certaine distance entre vous et le projet.

Prenez soin de remplir ou au moins de lier les connaissances préalables, surtout si vous utilisez fréquemment différents langages ou outils. Même une action aussi petite que de coller un lien vers la documentation de l'API que vous avez utilisée peut économiser des heures de recherche future.

Écrivez ou liez les README, les étapes d'installation et les problèmes de support pertinents. Pour les actions en ligne de commande fréquemment effectuées, vous pouvez utiliser un [Makefile auto-documenté](https://victoria.dev/blog/how-to-create-a-self-documenting-makefile/) pour éviter d'avoir à utiliser `man` pour les tâches courantes chaque fois que vous revenez à un projet.

Il est facile d'oublier les détails de support même après une courte pause de votre projet. Capturez tout ce que vous avez trouvé utile cette fois-ci.

## Documenter toutes les choses !

La prochaine fois que vous vous surprenez à penser : « Je suis sûr que je me souviendrai de cette partie, pas besoin de l'écrire », rappelez-vous simplement de cet emoji : 🧑‍🔧

Les projets logiciels sont composés de bien plus que de leur code. Pour mieux préparer votre futur vous à réussir, documentez toutes les choses ! Qu'il s'agisse d'un processus que vous avez établi, d'une Infrastructure as Code, ou d'une idée de feuille de route future fugace — écrivez-le ! Votre futur vous remerciera pour cela.

Si vous avez aimé cet article, j'adorerais le savoir. Rejoignez les milliers de personnes qui apprennent avec moi sur [victoria.dev](https://victoria.dev/) ! Visitez et abonnez-vous pour en savoir plus sur la construction de votre pile de compétences en codage.