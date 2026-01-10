---
title: Comment créer de superbes transitions de page dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-11T17:50:09.000Z'
originalURL: https://freecodecamp.org/news/beautiful-page-transitions-in-angular
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/SF.jpeg
tags:
- name: Angular
  slug: angular
- name: animations
  slug: animations
- name: Web Design
  slug: web-design
seo_title: Comment créer de superbes transitions de page dans Angular
seo_desc: 'By Arjav Dave

  In today’s world, just having a website is not enough. The website needs to have
  a clean UI and it needs to be intuitive. And most importantly, it needs to have
  some sort of interactive element.

  Interactivity keeps users glued to your s...'
---

Par Arjav Dave

Dans le monde d'aujourd'hui, avoir un simple site web ne suffit plus. Le site doit avoir une interface utilisateur (UI) propre et être intuitif. Et surtout, il doit comporter un élément interactif.

L'interactivité permet de retenir les utilisateurs sur votre site plus longtemps. Par conséquent, cela augmente les chances que les utilisateurs deviennent des clients. De plus, un temps d'interaction plus long entraîne un taux de rebond plus faible et un meilleur classement dans les moteurs de recherche.

L'une des formes d'interaction les plus courantes et les plus basiques se produit lorsqu'un utilisateur fait défiler (scroll) votre site web. Mais ne serait-ce pas assez ennuyeux si l'utilisateur continuait à faire défiler votre longue page statique ?

Dans ce tutoriel, nous allons examiner trois animations de base que vous pouvez implémenter au défilement. Les animations de parallaxe (parallax), de fondu (fade) et de glissement (slide) sont les animations les plus populaires utilisées par les développeurs pour rendre le défilement plus amusant. Voyons comment nous pouvons les construire pour nos sites.

Avant d'aller plus loin, voici les résultats finaux :

![Animation de parallaxe](https://www.freecodecamp.org/news/content/images/2021/05/1_Ywqe-PW3A-V8B5mvJmlpVg.gif)
_Parallaxe ([Voir la démo](https://animations-demo-ffcb4.web.app/parallax\" class=\"cd il\" rel=\"noopener\" style=\"box-sizing: inherit; color: inherit; text-decoration: underline; -webkit-tap-highlight-color: transparent;))_

![Animation de fondu](https://www.freecodecamp.org/news/content/images/2021/05/1_cZYvFm4F9EZXCyfpv1Rnwg.gif)
_Fondu ([Voir la démo](https://animations-demo-ffcb4.web.app/fade\" class=\"cd il\" rel=\"noopener\" style=\"box-sizing: inherit; color: inherit; text-decoration: underline; -webkit-tap-highlight-color: transparent;))_

![Animation de glissement](https://www.freecodecamp.org/news/content/images/2021/05/1_-thdCqzqVWw9o0oTk-lN0g.gif)
_Glissement ([Voir la démo](https://animations-demo-ffcb4.web.app/slide\" class=\"cd il\" rel=\"noopener\" style=\"box-sizing: inherit; color: inherit; text-decoration: underline; -webkit-tap-highlight-color: transparent;))_

# Configuration du projet

## Prérequis

Nous utiliserons Angular 11 pour créer notre projet. Et nous utiliserons VS Code comme IDE.

Pour construire les animations, nous allons utiliser la fabuleuse [Green Sock Animation Platform (gsap)](https://greensock.com/gsap/). C'est l'une des meilleures bibliothèques d'animation JavaScript du marché.

## Créer le projet

Créez un projet Angular en saisissant la commande ci-dessous. _Assurez-vous d'activer le routage_ lorsqu'on vous le demande.

```
ng new animations --style css
code animations
```

Cela créera un nouveau projet nommé _animations_ avec le format de style CSS. Ensuite, il ouvrira le projet dans VS Code.

Maintenant, installons gsap. Dans votre terminal VS Code, entrez la commande ci-dessous :

```
npm install --save gsap @types/gsap
```

Cela installera la bibliothèque gsap et les fichiers de typage via `@types/gsap`.

Enfin, créons trois composants. Entrez les commandes ci-dessous :

```
ng g c parallax
ng g c fade
ng g c slide
```

## Comment configurer les routes

Créons trois routes distinctes : `/parallax`, `/fade`, et `/scroll`. Ouvrez votre `app-routing.module.ts` et ajoutez les routes comme ci-dessous :

<script src=\"https://gist.github.com/shenanigan/a48aa865eb07ae94044e5e4c29ddaf9a.js\"></script>

# Comment créer une animation de parallaxe

Puisque nous avons maintenant configuré le projet, commençons par l'animation de parallaxe.

Lorsque vous créez des animations de page, vous utilisez généralement des sections. Alors, ouvrez votre fichier `parallax.component.html` et collez le code ci-dessous :

<script src=\"https://gist.github.com/shenanigan/9441fd03f71c4b2569c7d47aedc13b9d.js\"></script>

Ajoutons un peu de style à ces sections. Comme nous allons utiliser des sections dans les trois composants, nous ajouterons le style au fichier commun `styles.css`.

Ouvrez votre fichier `styles.css` et collez le CSS ci-dessous :

<script src=\"https://gist.github.com/shenanigan/dca657f450b032f5fc59a61f286f169d.js\"></script>

Dans le code ci-dessus, nous rendons la hauteur et la largeur de la section égales à la hauteur et à la largeur de la fenêtre d'affichage (viewport). Deuxièmement, nous alignons le contenu au centre de la section. Enfin, nous définissons le style de police pour l'affichage du texte.

Comme la classe `bg` utilisée dans `parallax.component.html` est spécifique à la parallaxe, nous définirons ses propriétés dans `parallax.component.css`. Ouvrez ce fichier et collez le CSS ci-dessous :

<script src=\"https://gist.github.com/shenanigan/af0cd6f8452fef800e511aa22a0d9790.js\"></script>

Pour configurer l'animation de parallaxe, nous devons ajouter du code TypeScript. Ouvrez donc votre fichier `parallax.component.ts` et ajoutez le code ci-dessous dans votre fonction `ngOnInit` :

<script src=\"https://gist.github.com/shenanigan/d5cf12a6dd47f7fbef4f26f346f12312.js\"></script>

J'ai ajouté des commentaires en ligne pour vous aider à comprendre le code. Envoyez-moi un message si vous avez besoin d'explications supplémentaires.

Enfin, ajoutez les imports ci-dessous en haut de votre fichier TS afin de ne pas avoir d'erreurs au moment de la compilation :

```
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/all';
```

C'est tout ! Vous pouvez maintenant visiter [http://localhost:4200/parallax](http://localhost:4200/parallax) pour voir la magnifique animation.

# Comment créer une animation de fondu

Pour l'animation de fondu, ouvrez le fichier `fade.component.html` et collez le code HTML ci-dessous :

<script src=\"https://gist.github.com/shenanigan/d7cea722e1f9a7ce73143810bb6e894f.js\"></script>

Dans le `fade.component.css`, collez le CSS ci-dessous :

<script src=\"https://gist.github.com/shenanigan/f8d15983a7a263af72f2b2addf71f151.js\"></script>

Nous n'allons afficher qu'une seule section à la fois. Nous allons donc masquer toutes les sections sauf la première. De plus, comme nous ne déplaçons pas les sections avec le défilement, nous marquerons leur position comme fixe.

Ajoutons le code d'animation pour rendre les autres sections visibles au défilement. Ouvrez le fichier `fade.component.ts` et collez le code suivant :

<script src=\"https://gist.github.com/shenanigan/0fadba01528dc3e0d3636522a5f13adc.js\"></script>

J'ai ajouté des commentaires en ligne afin de rendre le code explicite. Pour toute précision, n'hésitez pas à me le faire savoir.

Visitez [http://localhost:4200/fade](http://localhost:4200/parallax) pour voir l'animation de fondu fluide pendant que vous défilez.

# Comment créer une animation de glissement

C'est généralement la plus facile à comprendre et à mettre en œuvre.

Ouvrez votre fichier `slide.component.html` et collez le code ci-dessous. C'est similaire à `fade.component.html`, sauf que la classe est supprimée de la première section.

<script src=\"https://gist.github.com/shenanigan/6a68e1b4cc35ba04809fa6d118bf098c.js\"></script>

Nous n'avons pas besoin d'ajouter de CSS.

Ensuite, ouvrez le fichier `slide.component.ts` et ajoutez le code ci-dessous :

<script src=\"https://gist.github.com/shenanigan/f958d7d662ffe821e3c0431bfb5b27bf.js\"></script>

Encore une fois, j'ai ajouté les commentaires en ligne pour une meilleure compréhension du code. Pour toute question, contactez-moi.

Ouvrez [http://localhost:4200/slide](http://localhost:4200/slide) pour voir une animation de glissement fascinante pendant que vous défilez.

# Conclusion

Les animations ajoutent beaucoup de valeur à votre site et aident à maintenir l'engagement de vos utilisateurs. Comme pour toute chose, n'en abusez pas et utilisez les animations avec modération. N'encombrez pas et ne gâchez pas le site web avec des images lourdes et des animations farfelues. Keep It Simple & Keep It Subtle (KIS & KIS).

Dans ce tutoriel, nous avons vu comment ajouter des animations simples de parallaxe, de fondu et de glissement pour les sections de page.

Enfin, un grand merci à [Lorem Picsum](https://picsum.photos/) pour avoir fourni de si belles photos.

Si vous avez aimé cet article, vous aimerez peut-être aussi les articles ci-dessous :

* [Modules de chargement différé (Lazy Loading) dans Angular](https://betterprogramming.pub/lazy-loading-in-angular-a-beginners-guide-c09d09738d08)
* [.NET 5 : Comment authentifier et autoriser correctement les API](https://itnext.io/net-5-how-to-authenticate-authorise-apis-correctly-34b09d132d84)
* [Apprendre le TDD avec des tests d'intégration dans .NET 5.0](https://itnext.io/learn-tdd-with-integration-tests-in-net-5-0-937f126e7220)

_Note : Vous pouvez trouver l'intégralité du projet_ [_sur GitHub_](https://github.com/shenanigan/animations-demo)_._