---
title: Introduction à Deno – Guide pour débutants
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2022-09-09T22:50:17.000Z'
originalURL: https://freecodecamp.org/news/intro-to-deno
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-07-at-4.09.00-PM.png
tags:
- name: Deno
  slug: deno
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: TypeScript
  slug: typescript
seo_title: Introduction à Deno – Guide pour débutants
seo_desc: "What is Deno?\nDeno is a new JavaScript runtime. It was built by Ryan Dahl,\
  \ the creator of Node.js. \nDahl had a few things that he regretted doing with Node\
  \ and wanted to build a runtime that could solve those issues. Deno, like Node,\
  \ is built on the ..."
---

## Qu'est-ce que Deno ?

Deno est un nouvel environnement d'exécution JavaScript. Il a été créé par Ryan Dahl, le créateur de Node.js.

Dahl avait quelques regrets concernant Node et voulait créer un environnement d'exécution capable de résoudre ces problèmes. Deno, comme Node, est basé sur le moteur JavaScript V8 mais a été développé en utilisant Rust au lieu de C++.

L'un des principaux objectifs de Deno est de rapprocher le JavaScript côté serveur du JavaScript navigateur.

Si vous avez écrit du code à la fois pour Node et pour le navigateur, vous avez sûrement rencontré des différences dans les API utilisées dans ces espaces respectifs. Deno vise à avoir les mêmes API sur le serveur que celles que vous utiliseriez dans le navigateur. Nous examinerons plus en détail des exemples spécifiques de cela plus tard.

## Fonctionnalités clés de Deno

### Deno utilise TypeScript

L'une des fonctionnalités les plus marquantes de Deno est qu'il traite TypeScript comme un langage de première classe dès la sortie de la boîte. Cela signifie que vous pouvez exécuter ou utiliser TypeScript sans installer de packages externes ou tiers. Cela fonctionne simplement.

TypeScript est de plus en plus populaire dans le monde JavaScript, et de nombreux outils et entreprises poussent à son utilisation. Il est intéressant de voir une nouvelle technologie progressive comme TypeScript recevoir plus d'attention, et obtenir un statut de première classe dans un grand projet comme Deno est une avancée majeure.

### Deno est sécurisé par défaut

Deno est sécurisé par défaut. Cela signifie que, sauf si le script est _spécifiquement_ autorisé, il ne peut pas accéder aux fichiers système, à l'environnement (comme les variables d'environnement) ou au réseau.

Pour autoriser spécifiquement l'accès à ces fonctionnalités, vous devez passer le drapeau correspondant dans la commande CLI. Voici quelques-uns de ceux que vous utiliserez le plus :

* **Accès réseau** : `--allow-net`, vous pouvez également spécifier quelles URL le code est autorisé à accéder. Par exemple : `--allow-net=https://api.deepgram.com`
* **Accès aux fichiers** : `--allow-read`
* **Accès à l'environnement** : `--allow-env`

### Compatibilité navigateur de Deno

Comme je l'ai mentionné ci-dessus, Deno s'efforce d'avoir la même API que le navigateur. La plus grande de ces API, à mon avis, est la prise en charge de l'[API fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

De nos jours, dans la plupart du JavaScript que j'écris, j'utilise l'API `fetch`. Pouvoir utiliser la même syntaxe dans mon code côté serveur facilite grandement la productivité et réduit la charge de changement de contexte.

## Gestionnaire de packages

Deno n'a pas de registre de gestionnaire de packages. Node utilise `npm` pour charger des packages tiers dans votre projet, mais Deno charge les modules via des URL.

Je dois avouer que j'étais un peu confus au début. Ayant "grandit" avec Node et npm, il m'était étrange de ne pas avoir une sorte de gestionnaire de packages ou de fichier `package.json`.

Au lieu de ce registre centralisé, Deno permet aux développeurs de packages d'héberger leur code où ils le souhaitent. Si le code est hébergé sur GitHub, vous pouvez enregistrer votre module sur leur [service d'hébergement](https://deno.land/x) où il est mis en cache. Cela facilite la recherche et l'utilisation du module par les développeurs.

## Modules ES

Deno utilise également les Modules ES et ne prend pas en charge la syntaxe `require()`. Encore une fois, la plupart du JavaScript que j'écris ces jours-ci utilise des fonctionnalités modernes comme celle-ci, donc il est agréable de ne pas avoir à se soucier de s'assurer que j'utilise la syntaxe correcte en fonction de l'environnement pour lequel je code.

## Bibliothèque standard

Deno est livré avec une [bibliothèque standard](https://deno.land/std@0.138.0) qui contient des fonctionnalités auditées par l'équipe Deno. Cela rend vraiment facile de commencer à utiliser Deno.

Il n'est pas nécessaire de chercher des packages tiers pour faire des choses assez basiques qui sont nécessaires dans le code côté serveur. En tant que développeur, il est rassurant de savoir que le code que j'utilise est officiellement supporté et approuvé par l'équipe Deno.

### Module de test

L'un des modules inclus dans la bibliothèque standard est le [module de test](https://deno.land/std@0.109.0/testing). Ce module facilite l'écriture de tests dans Deno et les rendra plus cohérents entre les projets.

Cela peut ne pas être un avantage pour tout le monde, surtout si certains ont des opinions fortes sur les bibliothèques de test. Personnellement, je l'aime beaucoup. À mesure que Deno continue de grandir, la cohérence entre les projets facilitera la maintenance du code et le changement de projets.

## Deno vs Node

La plus grande question entourant Deno est de savoir comment il se compare à Node.

Deno offre clairement certains avantages par rapport à Node. Être sécurisé par défaut est définitivement une fonctionnalité attrayante, et les développeurs verront le support intégré de TypeScript comme un grand avantage.

D'un autre côté, Node possède une communauté très riche avec un écosystème établi et des packages tiers qui facilitent la mise en route. Avec [l'annonce que Deno prendra en charge _la plupart_ des packages npm](https://deno.com/blog/v1.25#experimental-npm-support), je peux voir les gens passer à Deno plus tôt que tard.

Deno a également récemment lancé [Deno Deploy](https://deno.com/deploy) en bêta publique. Cela permettra aux utilisateurs de déployer rapidement du code JavaScript à la périphérie. Ce service pourrait donner à l'entreprise Deno un avantage (jeu de mots intended) au fil du temps et faire croître la base d'utilisateurs.

## Conclusion

L'expérience que j'ai eue avec Deno au cours des derniers mois a été très amusante. J'ai apprécié travailler avec et je suis excité de voir ce que l'avenir lui réserve.

Au cours des prochaines semaines, j'écrirai plusieurs articles approfondissant le monde de Deno.