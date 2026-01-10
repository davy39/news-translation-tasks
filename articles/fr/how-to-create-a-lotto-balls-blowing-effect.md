---
title: Comment créer un effet de souffle d'air avec JavaScript
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2020-07-02T15:36:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-lotto-balls-blowing-effect
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/ball-blower-image.png
tags:
- name: animations
  slug: animations
- name: JavaScript
  slug: javascript
seo_title: Comment créer un effet de souffle d'air avec JavaScript
seo_desc: Have you ever wondered how you can create a realistic air blowing effect
  with JavaScript? Like the one shown on the evening TV shows, where multiple balls
  are being mixed up in a sphere-like object by leveraging air pressure? If you want
  to find out ...
---

Vous vous êtes déjà demandé comment créer un effet réaliste de souffle d'air avec JavaScript ? Comme celui montré dans les émissions de télévision du soir, où plusieurs balles sont mélangées dans un objet en forme de sphère en utilisant la pression de l'air ? Si vous voulez savoir comment c'est fait, continuez à lire.

✨ Si vous voulez sauter la lecture et passer directement au code, vous le trouverez [ici](https://github.com/mihailgaberov/bingo-blower). J'ai également déployé une [démo en direct ici](https://tender-hoover-fdc559.netlify.app/). ✨

## Recherche

Récemment, j'ai décidé de rénover quelque chose d'ancien que j'ai fait il y a 4 ans pour [un projet à moi](https://github.com/mihailgaberov/bingo/). Voici à quoi cela ressemblait :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-242.png align="left")

*Souffleur de Bingo*

À l'époque, j'avais choisi d'utiliser une bibliothèque appelée [Paperjs](http://paperjs.org/). À l'époque, cette bibliothèque m'avait permis de créer quelque chose de très proche de ce que je voulais réaliser.

Il s'avère qu'il existe aujourd'hui beaucoup plus de bibliothèques JavaScript qui permettent de faire des animations avec ou sans physique.

Avant de faire mon choix final, que vous verrez ci-dessous, j'ai joué avec [Anime.js](https://animejs.com/), [Velocity.js](http://velocityjs.org/), [Popmotion](https://popmotion.io/pure/), [Three.js](https://threejs.org/), [GreenSock JS](https://greensock.com/gsap/), [Mo.js](https://mojs.github.io/) et [Matter.js](https://brm.io/matter-js/). Chacune d'entre elles a ses avantages et ses inconvénients, et comme pour tout le reste, votre choix dépend des besoins spécifiques que vous pourriez avoir. J'ai choisi Matter.js.

## Découvrez Matter.js

Matter.js est un moteur de physique 2D pour corps rigides en JavaScript. Cela semble complexe, mais ce n'est pas le cas. Ce que cela signifie réellement, c'est que cette bibliothèque contient tout ce dont nous avons besoin pour créer des animations physiques 2D réalistes avec JavaScript.

Pour des informations détaillées sur ce que Matter.js a à offrir, vous pouvez consulter leur [documentation](https://brm.io/matter-js/docs/). Dans notre cas, nous tirerons principalement parti du [module Body](https://brm.io/matter-js/docs/classes/Body.html) et des fonctionnalités qu'il offre. Voyons comment dans la section suivante.

## Balles et Tube

Le composant "tube" est simple. Ce n'est qu'une [image](https://github.com/mihailgaberov/bingo-blower/blob/master/static/images/blower.png) d'arrière-plan que j'utilise pour créer l'illusion que les balles volent à l'intérieur d'un objet en verre en forme de sphère.

La partie intéressante est le code pour créer les animations et détecter les collisions entre les balles et les murs. Mais allons-y étape par étape.

Comme je l'ai dit, le "tube" est une image d'arrière-plan que j'ai ajoutée via la simple propriété CSS [background](https://developer.mozilla.org/en-US/docs/Web/CSS/background). Regardons les balles elles-mêmes. Pour elles, j'avais deux choix : essayer de dessiner des cercles sur une toile et les faire ressembler à des balles ou utiliser des images simples. J'ai choisi la deuxième option, car je voulais avoir une vue plus réaliste des balles.

Ainsi, avec l'aide d'un programme de traitement graphique, un ami a créé [75 images](https://github.com/mihailgaberov/bingo-blower/tree/master/static/images) pour moi, une pour chaque balle.

Ayant tous les éléments dont nous avons besoin, nous sommes maintenant prêts à approfondir et à implémenter une physique avec Matter.js.

## Implémenter, tester, implémenter, tester

Avant de passer à l'animation elle-même, nous devons mentionner quelques éléments spécifiques à Matter.js. Lors de la création d'animations avec cette bibliothèque, nous devons définir, au minimum :

* [Matter.Engine](https://brm.io/matter-js/docs/classes/Engine.html) - c'est le contrôleur qui gère les mises à jour de la simulation du monde.

* [Matter.World](https://brm.io/matter-js/docs/classes/World.html) - contient des méthodes pour créer et manipuler le composite du monde.

* [Matter.Render](https://brm.io/matter-js/docs/classes/Render.html) - ce module est un simple moteur de rendu basé sur la toile HTML5 pour visualiser les instances de `Matter.Engine`.

Dans notre exemple, nous allons également utiliser :

* [Matter.Bodies](https://brm.io/matter-js/docs/classes/Bodies.html) pour créer les différentes parties de la scène (les balles, le cercle de délimitation invisible).

* [Matter.Body](https://brm.io/matter-js/docs/classes/Body.html) pour appliquer des forces aux corps et ainsi créer une simulation physique réaliste d'un souffleur.

* [Matter.Runner](https://brm.io/matter-js/docs/classes/Runner.html) pour exécuter le tout.

* [Matter.Events](https://brm.io/matter-js/docs/classes/Events.html) nous donne la possibilité d'avoir des écouteurs pour différents événements qui pourraient se produire pendant l'animation. Dans ce cas spécifique, nous l'utilisons pour écouter l'événement 'tick', qui se produit à chaque tick de rendu. Dans la fonction de gestion des événements, nous effectuons notre vérification pour savoir quand les balles entrent en collision avec les murs et nous appliquons les forces pertinentes pour créer un effet de rebond. Nous retardons l'écoute de cet événement avec un délai de 3 secondes, afin de pouvoir avoir un effet plus proche de celui d'une loterie. Imaginez une sphère où les balles commencent à bouger lorsque, par exemple, un bouton est pressé.

## Essayer et Jouer

Au début de cet article, j'ai posté le lien vers le [dépôt GitHub](https://github.com/mihailgaberov/bingo-blower) avec le code et les éléments qu'il contient. Si vous voulez jouer davantage, vous pouvez facilement le consulter et essayer différentes modifications. Vous pourriez vouloir jouer avec les forces appliquées, ou la taille des balles, et ainsi de suite.

Il y a beaucoup de place pour l'expérimentation lorsque nous parlons de physique. Et c'est toujours amusant, surtout lorsque nous ajoutons des animations à l'image.

## Conclusion

Il s'avère que [Matter.js](https://brm.io/matter-js/index.html) est une excellente bibliothèque pour faire des animations 2D réalistes soutenues par les lois de la physique. Bien sûr, il existe d'autres options parmi lesquelles vous pouvez choisir, mais comme je l'ai dit, c'est une question de choix et de besoins du projet.

Je recommanderais personnellement au moins d'essayer et de voir par vous-même. Pour quelqu'un avec une expérience Flash ou similaire, Matter.js est définitivement facile à prendre en main. Et si vous êtes suffisamment obstiné pour continuer à essayer différents paramètres, vous pourriez obtenir des résultats incroyables.

## Ressources

https://brm.io/matter-js/ - Le site web de la bibliothèque
[https://burakkanber.com/blog/modeling-physics-in-javascript-introduction/](https://burakkanber.com/blog/modeling-physics-in-javascript-introduction/) - des articles intéressants et bien expliqués liés à la physique en JavaScript
[https://spicyyoghurt.com/tutorials/html5-javascript-game-development/collision-detection-physics/](https://spicyyoghurt.com/tutorials/html5-javascript-game-development/collision-detection-physics/) - tutoriel sur la détection des collisions
[https://codepen.io/AlexRA96/full/egaxVV](https://codepen.io/AlexRA96/full/egaxVV) - exemple de balle rebondissante
[https://codepen.io/Shokeen/pen/WjKmMG?editors=1010](https://codepen.io/Shokeen/pen/WjKmMG?editors=1010) - exemple codepen avec application de forces
[https://code.tutsplus.com/tutorials/getting-started-with-matterjs-body-module--cms-28835](https://code.tutsplus.com/tutorials/getting-started-with-matterjs-body-module--cms-28835) - tutoriel pour débutants pour commencer avec Matter.js
[https://codepen.io/jh3y/pen/gOPmMyO?editors=0110](https://codepen.io/jh3y/pen/gOPmMyO?editors=0110) - un autre exemple cool avec des ours qui tombent
[https://codepen.io/danielgivens/pen/geKrRx](https://codepen.io/danielgivens/pen/geKrRx) - un exemple encore plus cool avec une horloge circulaire et des particules à l'intérieur
[https://codepen.io/dotcli/pen/NEXrQe](https://codepen.io/dotcli/pen/NEXrQe) - un autre exemple de limites circulaires et de particules (chaussettes !) à l'intérieur