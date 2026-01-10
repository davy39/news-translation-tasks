---
title: Comment implémenter le défilement horizontal en utilisant Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T04:36:23.000Z'
originalURL: https://freecodecamp.org/news/horizontal-scrolling-using-flexbox-f9d16817f742
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8MiXDWg3C4evyq1WtRWTcw.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment implémenter le défilement horizontal en utilisant Flexbox
seo_desc: 'Horizontal scrolling using Flexbox

  If you create websites, chances are you have been asked to create a horizontal scrolling
  component. It is extremely easy to implement this using just a few lines of Flexbox.
  Let me show you how.

  Project Layout

  We ne...'
---

![Image](https://cdn-media-1.freecodecamp.org/images/4d5EkVE0IxLXQkRlSL3MOAYRnKtvmaqpqR2M)
_Défilement horizontal en utilisant Flexbox_

Si vous créez des sites web, il est probable que vous ayez été invité à créer un composant de défilement horizontal. Il est extrêmement facile de l'implémenter en utilisant seulement quelques lignes de Flexbox. Laissez-moi vous montrer comment.

#### Mise en page du projet

Nous devons créer un conteneur qui contiendra toutes les images que nous voulons faire défiler. Voici le code :

```html
<div class="container">
  <img src="images/bhutan1.jpg" alt="Bhutan" />
  <img src="images/bhutan2.jpg" alt="Bhutan" />
  <img src="images/bhutan3.jpg" alt="Bhutan" />
  <img src="images/bhutan4.jpg" alt="Bhutan" />
  <img src="images/bhutan5.jpg" alt="Bhutan" />
  <img src="images/bhutan6.jpg" alt="Bhutan" />
  <img src="images/bhutan7.jpg" alt="Bhutan" />
</div>

```

#### Stylisation du projet

L'étape suivante consiste à ajouter un style pour que le conteneur fasse défiler horizontalement. Pour cela, je fais en sorte que le conteneur s'affiche en tant que Flexbox. De plus, je définis la valeur overflow-x sur auto. Voici le style :

```css
.container {
  display: flex;
  overflow-x: auto;
}

```

Voici à quoi ressemble le défilement horizontal :

![Image](https://cdn-media-1.freecodecamp.org/images/OtTK-LibpJ6mcBOeHSmI2wIcXrlzMzzw5VND)
_La version initiale de notre défilement horizontal_

Cela répond à notre exigence d'une zone de défilement horizontal. Je ne suis pas satisfait de son apparence. Il y a trois choses que je veux changer :

* Ajouter un espace blanc entre les images
* Supprimer la barre de défilement horizontale
* Placer le défilement au milieu de l'écran

Les images se touchent. Ajoutons un peu d'espace blanc entre elles. Voici le CSS pour cela :

```css
.container img {
  margin-right: 15px;
}

```

Ensuite, je veux me débarrasser de la barre de défilement horizontale, ce que je peux faire avec ce code :

```css
.container::-webkit-scrollbar {
  display: none;
}

```

Le dernier changement que je veux apporter est de centrer la zone de défilement au milieu de l'écran. Par défaut, la hauteur du html est la hauteur des éléments. Je dois faire en sorte que la hauteur soit de 100 % de la fenêtre. Flexbox fournit un moyen de centrer les éléments avec le paramètre align-items. Pour utiliser cette fonctionnalité, je vais convertir le `body` pour qu'il s'affiche en tant que Flexbox. Voici le code que je vais ajouter pour le body :

```css
body {
  display: flex;
  align-items: center;
  height: 100vh;
}

```

Avec ces changements, voici à quoi ressemble notre zone de défilement horizontal final.

![Image](https://cdn-media-1.freecodecamp.org/images/qJCD4OP64IdYdHTGPKnFVBKhFLrkiIWDrKSe)

### Conclusion

Il est très facile de créer une zone de défilement horizontal en utilisant Flexbox. Merci d'avoir lu.

Voici quelques articles supplémentaires que vous pourriez aimer lire :

[**Voici 5 mises en page que vous pouvez réaliser avec FlexBox**](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)
[_La disposition flexible CSS — Flexbox — offre une solution simple aux problèmes de conception et de mise en page que les concepteurs et…_hackernoon.com](https://hackernoon.com/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d)

[**Pensez en dehors de la boîte avec la propriété CSS shape-outside**](https://hackernoon.com/mastering-css-series-shape-outside-44d626270b25)
[_CSS est basé sur un modèle de boîte. Si vous avez une image qui est un cercle autour duquel vous voulez envelopper du texte, il enveloppera…_hackernoon.com](https://hackernoon.com/mastering-css-series-shape-outside-44d626270b25)

[**Apprenez la propriété CSS border-radius en construisant une calculatrice**](https://medium.freecodecamp.org/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d)
[_Avez-vous déjà vu un bouton sur une page web qui a des bords arrondis ? Avez-vous déjà vu une image qui s'adapte dans un…_medium.freecodecamp.org](https://medium.freecodecamp.org/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d)