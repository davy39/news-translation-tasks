---
title: Une introduction rapide à Material Design avec Materialize
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-07T10:32:52.000Z'
originalURL: https://freecodecamp.org/news/an-quick-introduction-to-material-design-using-materialize-8a9b223c64f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Jie55HRpeCmZpmldgrL2eQ.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Une introduction rapide à Material Design avec Materialize
seo_desc: "By Arun \nWhat is Material Design?\nMaterial Design is a design language\
  \ created by Google. According to material.io, Material Design aims to combine:\n\
  \n…classic principles of good design with the innovation and possibility of technology\
  \ and science. It..."
---

Par Arun 

### Qu'est-ce que Material Design ?

Material Design est un langage de conception créé par Google. Selon [material.io](https://material.io/guidelines/), Material Design vise à combiner :

> …les principes classiques du bon design avec l'innovation et les possibilités de la technologie et de la science. Il vise à développer un système sous-jacent unique qui permet une expérience unifiée sur toutes les plateformes et tailles d'appareils. Les préceptes mobiles sont fondamentaux, mais le tactile, la voix, la souris et le clavier sont tous des méthodes d'entrée de première classe.

### Pourquoi utiliser Material Design ?

Material Design offre une expérience utilisateur fluide sur tous les appareils. Les transitions et animations réactives, ainsi que les effets de remplissage et de profondeur tels que les ombres et les éclairs, le rendent élégant et convivial. Google utilise Material Design sur presque toutes ses applications (comme Keep et Calendar).

### Comment utiliser Material Design dans vos applications web ?

Materialize est une bibliothèque de composants front-end réactive similaire à Bootstrap. Elle offre tout ce que Bootstrap propose, mais la différence est que Materialize suit les principes de Material Design. Voici un exemple de modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/SBQOXxPhVSVVscU7xlE7KLgSGkL55iHM6Jdr)

### Voici une liste des fonctionnalités offertes par Materialize :

* Grille
* Tableaux
* Badges, boutons, fil d'Ariane
* Cartes, puces, collections
* Pied de page, formulaires
* Barre de navigation
* Et bien plus encore !

### Comment commencer

Contrairement à Bootstrap, Materialize ne nécessite pas popper.js. Il nécessite uniquement jQuery. Voici tout ce dont vous avez besoin pour commencer. Ajoutez ceci à votre HTML et vous serez prêt à partir !

```html
<!-- CSS compilé et minifié -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
<!-- jQuery compilé et minifié -->
<script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
<!-- JavaScript compilé et minifié -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
```

### [Couleurs](http://materializecss.com/color.html)

Avec Materialize, vous pouvez changer la couleur de n'importe quel élément HTML en lui donnant simplement un nom de classe de la couleur souhaitée. Par exemple, si vous voulez donner à votre balise de paragraphe la couleur rouge, vous faites ce qui suit :

```
<p class="red">Lorem Ipsum</p>
```

De plus, vous pouvez également éclaircir ou assombrir une couleur en lui donnant un autre nom de classe `lighten-1` ou `darken-1`. Par exemple, `<h1 class="blue lighten-1">Sample Text</h1>. Le 1 peut être remplacé par des nombres jusqu'à 5 pour éclaircir et jusqu'à 4 pour assombrir. Des nombres plus élevés appliqueront des teintes plus claires ou plus foncées de la couleur.

### [Boutons](http://materializecss.com/buttons.html)

Pour Materialize un bouton, donnez-lui simplement le nom de classe `btn`. Vous pouvez également ajouter une animation sympa en lui donnant une autre classe `waves-effect`. Si vous avez besoin d'un bouton plus grand, la classe `btn-large` peut être utilisée. Par exemple :

```html
<button class="btn">
  Cliquez
</button> <!-- Bouton Materialized sans animation de clic -->
<button class="btn waves-effect">
  Cliquez
</button> <!-- Bouton Materialized avec animation de clic -->
<button class="btn-large">
  Cliquez
</button> <!-- Grand Bouton -->
```

### [Ombre](http://materializecss.com/shadow.html)

> Dans le Material Design, tout devrait avoir une certaine profondeur z qui détermine à quel point l'élément est surélevé ou proche de la page.

Pour appliquer un effet d'ombre à un élément, la classe `z-depth-2` peut être utilisée (2 peut être remplacé par des nombres de 1 à 5). Par exemple :

```html
<div class="z-depth-2"><!-- Contenu vraiment cool --></div>

```

### Conclusion

Je n'ai fait qu'effleurer la surface ici. Il y a beaucoup plus disponible dans Materialize (comme les transitions, les cartes, le carrousel et les modales). Vous pouvez apprendre à utiliser tous les composants à partir de la [documentation](http://materializecss.com/getting-started.html). Les noms de classe sont très simples et la grille est vraiment utile pour créer rapidement des colonnes réactives. Je vous souhaite bonne chance !