---
title: Apprendre les motifs avancés de React en développant un jeu avec animation
  de sprite
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-02T16:04:11.000Z'
originalURL: https://freecodecamp.org/news/learn-advanced-react-patterns-by-developing-a-game-with-sprite-animation-5dc072886975
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p6Q4wwQ2m1D_rGYvRBRPWg.png
tags:
- name: CSS
  slug: css
- name: Games
  slug: games
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Apprendre les motifs avancés de React en développant un jeu avec animation
  de sprite
seo_desc: 'By Pavel Vlasov

  Have you ever wanted to learn some advanced React patterns? Or build your own game
  engine? If at least one answer is yes, then this article is for you.

  In this tutorial, you’ll learn how to build basic sprite animation using React,
  st...'
---

Par Pavel Vlasov

Avez-vous déjà voulu apprendre quelques motifs avancés de React ? Ou construire votre propre moteur de jeu ? Si au moins une réponse est oui, alors cet article est pour vous.

Dans ce tutoriel, vous apprendrez comment construire une animation de sprite de base en utilisant [**React**](https://reactjs.org/), [styles-components](https://www.styled-components.com/), et **requestAnimationFrame**. À la fin, vous serez capable de créer des personnages comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ig-pwnKpjNtc2xaM0HMR6A.gif)

Vous pourriez me demander _pourquoi ne puis-je pas l'apprendre d'une autre manière_ ? Eh bien... Il y a trois raisons à cela :

![Image](https://cdn-media-1.freecodecamp.org/images/1*rBqlCIMpp_nQPy2EEpB0Hw.png)

Alors, commençons ! ?

### **Commençons par un peu de théorie**

Qu'est-ce qu'une animation de sprite ? [Wikipedia](https://en.wikipedia.org/wiki/Sprite_(computer_graphics)) dit que

> En infographie, un **sprite** est une image bitmap en deux dimensions qui est intégrée dans une scène plus grande.

Donc, fondamentalement, une animation de sprite est une image bitmap en deux dimensions qui change de manière répétée.

Un sprite est généralement représenté comme une image png avec différents états de l'animation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hbOGCHijQurkW40hwnocDw.png)
_Image bitmap_

Nous commencerons par créer un composant de tuile qui nous montrera une image à la fois et nous permettra de changer d'images avec la propriété **state** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fuAsHwFdlqR1qUw2b36GlA.gif)

En gros, nous devrons montrer une partie de l'image à la fois et cacher le reste. Assez simple.

### Tuile

Tout d'abord, nous créerons un composant conteneur pour créer la forme de notre cadre :

`width` et `height` représentent la taille de la tuile, et `scale` augmente la taille de l'image. `overflow: hidden` cachera la partie inutilisée de l'image et `transform-origin` permettra au conteneur de garder son haut et sa gauche identiques lorsque nous le mettrons à l'échelle.

Maintenant, nous devons ajuster la position de l'image intérieure. Nous utiliserons la propriété CSS `transform: translate` pour cela :

Maintenant, combinons tout cela dans le composant de tuile :

* La propriété `src` contient un lien vers l'image
* `tile` est l'objet avec les champs `width` et `height`, représente la taille de la tuile
* `state` index de l'image
* La propriété `scale` pour augmenter la taille de l'image (Par exemple, `scale = 2` est une image 2x)

À l'étape suivante, nous ajouterons un peu de mouvement à notre image.

### Sprite

Nous utiliserons **requestAnimationFrame** pour cela. Vous pourriez me demander pourquoi nous n'utilisons pas **setTimeout** ou **setInterval**. Le problème avec les timeouts est que le callback se déclenchera quelque part entre les images, ce qui peut entraîner une animation saccadée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2UnyL2Wr6r2OIDvogPpNLQ.png)
_requestAnimationFrame vs setInterval_

De plus, **requestAnimationFrame** nous permet de synchroniser les animations de différents objets à l'écran. Dans le jeu, vous en aurez beaucoup !

Mettons ensemble un composant Sprite :

Dans la fonction `animate`, nous devons changer l'`state` de l'image et demander une nouvelle image d'animation :

Nous utilisons la propriété `framesPerStep` pour contrôler le nombre d'états par image, afin que notre animation ne soit pas trop rapide.

### Et un pistolet ? ?

Maintenant, la seule chose que nous devons faire est de combiner notre sprite avec l'image du pistolet :

Et vous devriez obtenir le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mi4Xn8yPVYO7nDBf5TBXdg.gif)

La meilleure façon d'apprendre quelque chose est de le construire soi-même. Je vous encourage donc à utiliser ce [codesandbox](https://codesandbox.io/s/github/react-dev-camp/react-game-dev-course/tree/master/lessons/1_sprites/javascript?autoresize=1&hidenavigation=1) :

La version TypeScript est [disponible ici également](https://codesandbox.io/s/github/react-dev-camp/react-game-dev-course/tree/master/lessons/1_sprites/typescript).

En bonus, vous pouvez implémenter différentes animations en utilisant les fichiers du dossier assets.

Vous pouvez trouver le code source [ici](https://github.com/react-dev-camp/react-game-dev-course). J'ai utilisé des actifs de jeu créés par [finalbossblues](https://finalbossblues.itch.io/pixel-shooter-towers-asset-pack).

J'espère que vous avez apprécié l'article ! ?

Suivez-moi sur [Medium](https://medium.com/@pvlasov) et [Twitter](https://twitter.com/pvl4sov) pour obtenir plus de mises à jour sur les nouveaux articles. De plus, partagez cet article pour aider les autres à le connaître. Partager, c'est prendre soin ?

**Détruisez ce bouton d'applaudissements si vous en voulez plus.**

**Vous pouvez applaudir jusqu'à 50 fois !** ?

Quelques ressources supplémentaires sur le sujet :

[**Comprendre la méthode requestAnimationFrame() de JavaScript pour des animations fluides**](http://www.javascriptkit.com/javatutors/requestanimationframe.shtml)

[_requestAnimationFrame() est une méthode JavaScript pour créer des animations JavaScript plus fluides et moins gourmandes en ressources..._www.javascriptkit.com](http://www.javascriptkit.com/javatutors/requestanimationframe.shtml)

_Publié à l'origine sur [react.camp](http://react.camp/posts/advanced-react-patterns-game-engine-1-sprites/).