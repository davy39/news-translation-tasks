---
title: Comment créer un menu coulissant réactif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-14T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-responsive-sliding-menu-97b90852a455
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_qfdprsLd9bgo4VB1gTWyA.gif
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer un menu coulissant réactif
seo_desc: 'By Prashant Yadav

  I run a blog named learnersbucket.com where I write about ES6, Data structures,
  and Algorithms to help others crack coding interviews. Follow me on Twitter for
  regular updates.

  When I was designing my blog with a mobile-first approa...'
---

Par Prashant Yadav

Je tiens un blog nommé [learnersbucket.com](https://learnersbucket.com/) où j'écris sur [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), [Data structures](https://learnersbucket.com/tutorials/topics/data-structures/), et [Algorithms](https://learnersbucket.com/examples/topics/algorithms/) pour aider les autres à réussir les entretiens de codage. Suivez-moi sur [Twitter](https://twitter.com/LearnersBucket) pour des mises à jour régulières.

Lorsque je concevais mon blog avec une approche mobile-first, j'ai décidé de garder mon menu de navigation latéral séparé en bas à droite. Il n'y a pas besoin d'en-tête fixe et l'utilisateur peut tout lire en pleine hauteur.

Voici à quoi ressemble la version simple de mon menu mobile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_qfdprsLd9bgo4VB1gTWyA.gif)
_Menu de Navigation Latéral Coulissant_

Voici comment vous pouvez créer votre propre menu de navigation latéral réactif.

### Aperçu

Avant de passer à la conception du menu, imaginons quels composants nous avons besoin.

* Un bouton hamburger ? qui affichera/masquera le menu coulissant.
* Une animation sur le bouton hamburger pour représenter l'état actuel du menu.
* Un menu de navigation latéral.

Comme le menu de navigation latéral basculera au clic du menu hamburger, nous pouvons les regrouper dans un seul conteneur.

### Dépendances

J'aime utiliser jQuery pour la manipulation du [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) car cela réduit la quantité de code que je dois écrire.

### Bouton hamburger

#### Structure HTML

Il existe une astuce simple pour créer un menu hamburger.

Nous allons utiliser un `<div>` avec une classe `.hamburger` pour créer l'enveloppe du bouton hamburger. Ensuite, nous placerons trois `<span>` pour créer les couches du hamburger.

### Conception du bouton hamburger

Maintenant que la structure HTML de notre bouton est prête, nous devons la concevoir pour qu'elle ressemble à un hamburger. Lors de la conception, nous devons garder à l'esprit que nous devons fournir l'animation pour l'ouverture et la fermeture lorsque l'utilisateur clique dessus.

Comme nous créons un bouton hamburger de dimension fixe, nous allons fournir des dimensions fixes à l'enveloppe.

* Nous avons créé un parent fixe `.hamburger{position:fixed}` pour le placer où nous voulons sur l'écran.
* Ensuite, nous avons conçu tous les `<span>` comme de petites boîtes rectangulaires avec `position:absolute`.
* Comme nous devons montrer trois bandes différentes, nous avons changé la position supérieure du 2ème span `.hamburger > span:nth-child(2){ top: 16px; }` et du 3ème span `.hamburger > span:nth-child(3){ top: 27px; }`.
* Nous avons également fourni `transition: all .25s ease-in-out;` à tous les spans pour que le changement de leurs propriétés soit fluide.

### Ouverture et fermeture du bouton hamburger avec jQuery

Chaque fois que le bouton hamburger est cliqué, il basculera une classe `open`. Nous pouvons maintenant utiliser cette classe pour ajouter l'effet d'ouverture et de fermeture.

`.hamburger.open > span:nth-child(2){ transform: translateX(-100%); opacity: 0;}` fera glisser la bande du milieu du hamburger vers la gauche et la rendra transparente.

`.hamburger.open > span:nth-child(1){ transform: rotateZ(45deg); top:16px; }` et `.hamburger.open > span:nth-child(2){ transform: rotateZ(-45deg); top:16px; }` amèneront le premier et le dernier span à la même position supérieure et les feront tourner pour former un X.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wV23krL_L1ewHBrk.gif)
_Bouton Hamburger_

Félicitations 💡 nous avons notre bouton hamburger 🍔 prêt, alors créons maintenant la navigation latérale.

### Menu de navigation latéral réactif

#### Structure HTML

Nous allons créer un menu de navigation simple.

Nous avons utilisé un élément `nav` pour créer le menu de navigation et placé les liens dans `ul`.

### Conception du menu de navigation

J'ai créé un menu latéral plein écran, vous pouvez changer les dimensions selon vos besoins. Nous utilisons le sélecteur `>` pour éviter d'écraser le style d'autres éléments.

Maintenant que nous avons notre menu de navigation et notre bouton hamburger prêts, nous pouvons les envelopper dans un conteneur pour les rendre fonctionnels.

### Menu de navigation coulissant

#### Structure HTML

Nous avons placé le bouton hamburger et le menu de navigation à l'intérieur de l'enveloppe `.mobile-menu`.

### Conception du menu de navigation coulissant

Nous avons mis à jour la conception en fournissant certaines propriétés du `.hamburger` à `.mobile-menu` pour le rendre fixe et avons rendu `.hamburger` relatif pour garder la conception des `<span>` identique.

Comme il peut y avoir plusieurs `nav`, nous avons mis à jour tous les sélecteurs `.mobile-menu > nav` pour nous assurer que nous pointons uniquement vers les éléments requis.

### Rendre le menu latéral fonctionnel avec jQuery

Nous ajoutons maintenant notre classe `.open` à `.mobile-menu` afin de pouvoir gérer à la fois le bouton hamburger et le menu coulissant avec un seul changement.

Notre CSS pour l'animation est également mis à jour en conséquence.

Bien joué 🎉 nous avons couvert tout.

Consultez la démonstration fonctionnelle ici

### Conclusion

Cet article concernait un menu coulissant simple. J'ai essayé de le décomposer en différents composants afin que vous puissiez les utiliser indépendamment.

Merci d'avoir eu la patience de lire ceci. Si vous avez appris quelque chose de nouveau aujourd'hui, donnez quelques 👏. Partagez-le également avec vos amis afin qu'ils puissent apprendre quelque chose de nouveau aussi.

C'est tout, suivez-moi sur [Twitter](https://twitter.com/LearnersBucket) pour le partage de connaissances. J'écris sur [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), Nodejs, [Data structures](https://learnersbucket.com/tutorials/topics/data-structures/) et [Algorithms](https://learnersbucket.com/examples/topics/algorithms/) et le développement web full stack avec JavaScript.

_Publié à l'origine sur [learnersbucket.com](https://learnersbucket.com/examples/html/how-to-create-responsive-sidebar-menu/) le 14 avril 2019._