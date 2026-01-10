---
title: Comment j'ai ajouté le mode sombre à mon site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T15:47:25.000Z'
originalURL: https://freecodecamp.org/news/how-i-added-dark-mode-to-my-website-484bc3cb0318
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fTme9ip4kqGbZuHc.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment j'ai ajouté le mode sombre à mon site web
seo_desc: 'By Jonathan Sexton

  Same website, two different color schemes

  Last year I made it a point to redesign my website from scratch. I wanted something
  simple and minimalist looking that clearly stated what this was — a portfolio website.

  After I rebuilt my...'
---

Par Jonathan Sexton

#### Même site web, deux schémas de couleurs différents

L'année dernière, j'ai décidé de redessiner mon site web à partir de zéro. Je voulais quelque chose de simple et minimaliste qui indique clairement ce que c'était — un site web de portfolio.

Après avoir reconstruit mon site web de fond en comble, il semblait que partout où je me tournais, il y avait un autre article sur l'ajout d'un mode sombre à votre site web.

Au début, je ne pensais pas que cela ferait une si grande différence car, bien que j'aie une préférence pour les couleurs plus sombres, j'avais l'impression que mon site web était un bon équilibre entre des couleurs vives et amusantes et des polices plus sombres.

![Image](https://cdn-media-1.freecodecamp.org/images/0UKp9ooxLroDJHXifQ0UPa6JAZ2aczd0KtXw)

J'ai lu certains des articles que j'ai mentionnés précédemment et plus j'y pensais, plus je décidais de me lancer.

Je me suis inspiré de Flavio Copes qui a écrit un [article formidable](https://flaviocopes.com/dark-mode/) sur ce sujet précis. Contrairement à ce que Flavio a décidé de faire avec son site, je n'ai pas ajouté le choix de l'utilisateur au stockage local.

Cela est dû, en partie, aux différences entre nos sites. J'ai un site statique et il n'y a pas de redirections/pages séparées à part le blog qui est sur une plateforme différente, donc les utilisateurs ne rechargeront généralement pas la page. C'est une option intéressante et une que je pourrais ajouter plus tard.

D'accord, plongeons dans les détails de la façon dont j'ai accompli mon basculement en mode sombre.

### Le Code

Le code pour y parvenir était assez simple. J'ai pris la même approche que Flavio et j'ai ajouté les changements de style via CSS. J'ai dû prendre quelques étapes supplémentaires car j'ai une image sur ma page d'accueil.

![Image](https://cdn-media-1.freecodecamp.org/images/k3elVGlxhWNo9FKBbPzIdsfJ6MUBiMfFMPYy)

J'ai dû utiliser le drapeau **!important** sur certaines des règles car elles n'étaient pas appliquées correctement. C'était l'approche la plus facile à mettre en œuvre et je sais qu'il n'est pas conseillé d'utiliser ce drapeau, donc je chercherai une alternative dans un proche avenir.

Voici le JavaScript que j'ai utilisé pour faire fonctionner correctement mon interrupteur à bascule :

![Image](https://cdn-media-1.freecodecamp.org/images/uVO2mmQZyc5W7lzYqxb2fLIY5-OJeYGctlrH)

Je commence par sélectionner mon `div` avec un id de `light-dark-mode-container` et j'ajoute un [écouteur d'événement](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) à celui-ci.

Ensuite, je définis mes variables `everything`, qui sélectionne tout le contenu de la page, et `projectTiles` car cette classe appartient à un ensemble particulier de superpositions que je ne veux pas avoir un fond de couleur unie.

Ensuite, puisque j'utilise `[querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)` qui retourne une [NodeList](https://developer.mozilla.org/en-US/docs/Web/API/NodeList) statique, je parcourt tous les éléments des deux NodeLists et j'ajoute ou je retire complètement la classe `dark` des éléments retournés par la variable `projectTiles`.

Ce que j'obtiens, c'est un conteneur en haut de mon site web avec un interrupteur à bascule qui permet à l'utilisateur de basculer entre le mode clair et le mode sombre.

![Image](https://cdn-media-1.freecodecamp.org/images/8daEF9V6p0lk6rkCgsPced5rILn0wR95ms5x)
_Le produit final_

![Image](https://cdn-media-1.freecodecamp.org/images/OVHTig0pHG90YyP9FMF4E62xOgLCwHT5KEKo)
_L'écran suivant en mode sombre_

J'espère que vous avez apprécié cet article et peut-être que vous avez appris quelque chose aussi ! Si vous décidez de mettre en œuvre cela sur votre propre site web ou votre prochain projet, n'hésitez pas à le partager avec moi (laissez-moi un commentaire ou envoyez-moi un message sur [Twitter](https://twitter.com/jj_goose)). Je suis toujours heureux de voir le travail et les projets que les autres créent.

Cet article a été publié sur mon [blog](https://jonathansexton.me/blog) où j'écris des articles liés au développement web front-end. Je fais également des publications croisées sur [Dev.to](https://dev.to/jsgoose), donc si vous êtes sur cette plateforme, vous pouvez également trouver mon travail !

Pendant que vous y êtes, pourquoi ne pas vous inscrire à ma **Newsletter** ? Je promets de ne jamais spammer votre boîte de réception et vos informations ne seront pas partagées avec qui que ce soit d'autre.

Passez une journée formidable remplie d'amour, de joie et de codage !