---
title: Votre guide complet pour des images vraiment responsives
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T18:30:57.000Z'
originalURL: https://freecodecamp.org/news/your-complete-guide-to-truly-responsive-images
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/giraffe-NOT-responsive-image-medium.jpg
tags:
- name: Progressive Images
  slug: progressive-images
- name: 'image optimization '
  slug: image-optimization
- name: Image Placeholder
  slug: image-placeholder
- name: Responsive Image
  slug: responsive-image
seo_title: Votre guide complet pour des images vraiment responsives
seo_desc: 'By Dane Stevens


  There is a lot that goes into making a website responsive, and images are a major
  factor and can make or break your site. With that out of the way, let''s dig in:

  <img src="giraffe.jpg" />



  Whoa! That''s not quite right, let''s fix tha...'
---

Par Dane Stevens

![Images Responsives](https://cdn.tueri.io/274877906986/giraffe-family.jpg)

Il y a beaucoup à faire pour rendre un site web responsive, et les images sont un facteur majeur qui peut faire ou défaire votre site. Cela étant dit, plongeons dans le sujet :

```html
<img src="giraffe.jpg" />

```

![Girafe Non-Responsive](https://cdn.tueri.io/274877906980/giraffe-NOT-responsive-image.jpg?w=700&crop.width=700&h=467&crop.height=467&crop.x=1100&crop.y=700)

Whoa ! Ce n'est pas tout à fait correct, corrigeons cela.

## Images en pourcentage de largeur utilisant CSS

Par définition, un site responsive n'a pas de largeur fixe. Nous pouvons en tenir compte en définissant la largeur de notre image en pourcentages. Une largeur en pourcentage peut être définie directement sur l'image en utilisant du CSS en ligne ou définie globalement en utilisant une feuille de style CSS.

```html
<!-- CSS en ligne -->
<img src="giraffe.jpg" style="max-width: 100%;" />

```

```css
/* Feuille de style CSS globale */
imag {
    max-width: 100%;
}

```

Notre image définie à 100% de largeur maximale ressemble maintenant à ceci. N'hésitez pas à redimensionner la fenêtre de votre navigateur et à voir la largeur de l'image changer automatiquement.

![Girafe Complètement Responsive](https://cdn.tueri.io/274877906980/giraffe-NOT-responsive-image.jpg?w=700&h=467)

Génial ! Nos images sont maintenant responsives, mais ne nous emballons pas trop. Les largeurs en pourcentage CSS ont un inconvénient majeur : Ce panneau de lecture a une largeur maximale de 700 pixels et notre image fait 3742 pixels de large, soit 532% plus grande que ce dont nous avons besoin. Elle consomme également 1,55 Mo de bande passante.

### Donc l'image est énorme, quel est le problème ?

Sur une connexion internet ADSL standard, il faudra 2 secondes pour télécharger cette seule image.

Je vais supposer que vous avez plus d'une image sur votre site web. Si chaque image prend 2 secondes à télécharger, votre site sera très lent et votre classement dans les moteurs de recherche en prendra un coup.

### Comment pouvons-nous résoudre ce problème ?

Puisque nous n'avons besoin que d'une image de 700 pixels de large, ouvrons Photoshop et redimensionnons-la.

![Girafe Mangeant](https://cdn.tueri.io/274877906980/giraffe-NOT-responsive-image.jpg?w=700&h=467)

C'est mieux ! Notre image fait maintenant 700 pixels de large et pèse 264 Ko sans perte de qualité.

### Qu'en est-il des appareils mobiles ?

Excellente question ! Sur les appareils mobiles, 700 pixels peuvent être plus du double de ce dont vous avez besoin et 264 Ko sont encore lents sur une connexion internet mobile.

Et si nous pouvions afficher différentes tailles d'images pour différentes tailles d'appareils ?

Maintenant, vous réfléchissez !

## Différentes tailles d'images utilisant l'attribut srcset

Réduisons notre image originale et enregistrons-la en trois versions de 700 pixels, 480 pixels et 360 pixels. Nous les nommerons comme suit :

* giraffe-small.jpg - 360px @ 101 Ko
* giraffe-medium.jpg - 480px @ 151 Ko
* giraffe-large.jpg - 700px @ 264 Ko

![Petite, Moyenne et Grande Girafe](https://cdn.tueri.io/274877906987/giraffe-family.jpg)

Nous utiliserons l'attribut srcset pour informer le navigateur de nos différentes tailles d'images. Cela indique au navigateur que nous avons trois versions de cette image dans les tailles 360w, 480w et 700w. Le "w" dans ce cas est le même que "px".

```html
<img 
    style="max-width: 100%;"
    srcset="giraffe-small.jpg 360w, giraffe-medium.jpg 480w, giraffe-large.jpg 700w"
/>

```

Certains navigateurs plus anciens ignoreront l'attribut srcset. Nous pouvons utiliser l'attribut src comme solution de repli pour ces navigateurs.

```html
<img 
    style="max-width: 100%;"
    srcset="giraffe-small.jpg 360w, giraffe-medium.jpg 480w, giraffe-large.jpg 700w"
    src="giraffe-large.jpg"
/>

```

![Girafe Mangeant](https://cdn.tueri.io/274877906980/giraffe-NOT-responsive-image.jpg?w=700&h=467)

Génial ! Maintenant, nous économisons de la bande passante en livrant différentes images à différents appareils.

Cela va sans dire, mais vous savez ce que cela signifie, n'est-ce pas ? Vous devrez créer un minimum de trois versions de chaque image sur votre site. Si vous souhaitez prendre en charge les écrans hi-dpi ou rétina, vous aurez besoin de encore plus de variations. C'est une quantité incroyable de temps que personne n'a. De plus, si vous redessinez votre site à différents points de rupture, vous devrez tout refaire.

Chez Tueri, nous sommes aussi des développeurs et nous reconnaissons que votre temps est précieux. Dans la section suivante, je vais vous montrer comment nous avons résolu ce problème pour vous.

## Traitement d'images en temps réel avec [Tueri.io](https://tueri.io)

[Tueri.io](https://tueri.io) est une plateforme de traitement d'images en temps réel. Nous stockons, traitons et livrons votre image parfaitement dimensionnée pour chaque appareil.

### Voici ce que vous devez faire

1. Téléchargez votre image sur [Tueri.io](https://tueri.io)
2. Changez l'attribut `src` de l'image en `tueri-src`
3. Incluez [tueri.js](https://github.com/tueriapp/vanilla-tueri) dans votre code

```html
<img tueri-src="https://cdn.tueri.io/274877906982/giraffe-family.jpg"/>
<script src="tueri.js"></script>

```

![Famille de Girafes](https://cdn.tueri.io/274877906982/giraffe-family.jpg)

### C'est comme de la magie !

Oh, et nous faisons aussi :

* Des espaces réservés d'images de faible qualité
* Le chargement paresseux des images
* La compression d'images
* La conversion d'images

---

*Originalement publié sur [Tueri.io](https://tueri.io/blog/2019-03-27-your-complete-guide-to-truly-responsive-images/?utm_source=Freecodecamp&utm_medium=Post&utm_campaign=)*