---
title: Comment créer une barre de menu coulissante en utilisant HTML, CSS et JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-18T17:15:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-sliding-menu-bar-using-html-css-and-javascript-669f0c1c37a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x_Hcn2GhZZoiwhWBSnVGTA.jpeg
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment créer une barre de menu coulissante en utilisant HTML, CSS et JavaScript
seo_desc: 'By Supriya Shashivasan

  A menu is what you look for when you land at a website. It has options and gives
  you access to everything the website has to offer you. You would definitely say
  it is an important part of a website, right?

  My friend Girish pati...'
---

Par Supriya Shashivasan

Un menu est ce que vous cherchez lorsque vous arrivez sur un site web. Il comporte des options et vous donne accès à tout ce que le site a à vous offrir. Vous diriez définitivement que c'est une partie importante d'un site web, n'est-ce pas ?

Mon ami [Girish patil](https://www.freecodecamp.org/news/how-to-build-a-sliding-menu-bar-using-html-css-and-javascript-669f0c1c37a7/undefined) et moi avons lancé une newsletter bihebdomadaire pour les développeurs front-end ce mois-ci. La première newsletter présente les barres de menu coulissantes, et me voilà donc en train d'écrire sur la façon dont nous l'avons construite.

Avant de commencer, procurez-vous un conteneur pour l'ensemble de votre page web et concevez la largeur et la hauteur selon vos besoins. Maintenant, à l'intérieur du conteneur, vous devez placer un menu coulissant. Dans cet article, nous expliquerons comment créer un menu coulissant à gauche.

### Commençons

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Jjz_X5KuI7U3Qs-lyKFSw.gif)
_Inspiration !!!! ;)_

Le code HTML pour le curseur est donné ci-dessous. Il s'agit d'une version de base.

```
<div class="slider-container">
```

```
<a href="#" class="slider-trigger">   Cliquez ici   </a>
```

```
<div class="slider-parent">    <h1>Curseur</h1>    <a href="https:/twitter.com/giyaletter">Twitter</a> <br>    <a href="https:/twitter.com/s_omeal">@Supriya</a> <br>    <a href="https:/twitter.com/g__patil">@Girish</a> <br>   </div>
```

```
</div>
```

Une **balise d'ancrage** est utilisée pour ouvrir le menu lorsqu'on clique dessus. C'est ce qui déclenche l'ouverture du menu, donc vous pouvez voir pourquoi il est appelé **slider-trigger**. Le composant de menu est ce qui se trouve dans la classe **slider-parent**.

Maintenant, concevez la barre de menu en CSS. Portez une attention particulière aux détails de conception.

```
.slider-container {  position: relative; }  .slider-container .slider-parent {    height: 70vh;    max-width: 250px;    width: 100%;    background: #6C7A89;    position: absolute;    left: -250px;    top: 50px;    visibility: hidden;    opacity: 0;    pointer-events: none;    transition: .2s all linear; }   .slider-container .slider-parent.active {      visibility: visible;      pointer-events: inherit;      transition: .2s all ease-in-out;      opacity: 1;      left: 0; }
```

Décomposons maintenant l'extrait ci-dessus et discutons de son fonctionnement.

**Maxwidth** définit la largeur maximale que la div peut occuper. Dans une fenêtre plus petite, elle peut occuper moins de 250px. La div occupe 250px lorsque la fenêtre est étirée au maximum sur l'écran.

Parfois, l'utilisateur peut regarder le site web sur un écran beaucoup plus petit, donc nous voulons que notre div se redimensionne en conséquence.

Passons maintenant à la raison pour laquelle **left : -250px ?** Cela est fait pour obtenir cette action de glissement fluide pour le menu. Remarquez que la valeur pour left est négative, ce qui nous indique que le menu commence à 250px à gauche de la position de départ (qui est 0). Donc, il n'est actuellement pas dans la zone visible.

Nous ne voulons pas que le menu coulissant soit visible du tout, c'est pourquoi nous ajoutons **opacity** et rendons sa **visibility hidden**. Tout le monde aime l'animation, et cela donne une sensation visuelle intéressante. Cette animation peut être réalisée en utilisant le composant **transition**.

#### YAYYY! Le curseur de base est terminé!

![Image](https://cdn-media-1.freecodecamp.org/images/1*UJtn-JxIMOnn6D6jLGqFgw.gif)
_Je suis sûre que vous danserez mieux :P_

Maintenant que le curseur de base est terminé, comprenons ce qui se passe lorsque la barre du curseur est active — c'est-à-dire lorsque la balise d'ancrage qui ouvre la barre de menu est cliquée.

Concentrez-vous sur la classe **active** dans le code CSS donné ci-dessus. Remarquez que les valeurs pour **opacity** et visibility sont changées. Ce changement est fait pour rendre le curseur (qui était précédemment caché) visible sur l'écran.

De plus, vous pourriez vous demander : pourquoi est-ce maintenant **left : 0 ?** Auparavant, le curseur était hors de l'écran. Maintenant que nous voulons que le menu commence du côté gauche de l'écran, nous changeons la valeur de left à 0.

OH! L'animation! Ajoutez à nouveau le composant **transition** afin que lorsque le curseur est actif, il apparaisse en douceur depuis la gauche.

C'est fait! Vous avez conçu les composants, donc quelle est la prochaine étape? JavaScript! Cela mettra tout cela en action.

### Ajout de JavaScript

```
var sliderTrigger = document.getElementsByClassName("slider-trigger")[0];var slider = document.getElementsByClassName('slider-parent')[0];
```

```
sliderTrigger.addEventListener( "click" , function(el){
```

```
if(slider.classList.contains("active")){  slider.classList.remove("active"); }else{  slider.classList.add("active"); }
```

```
});
```

Examinons comment JavaScript enveloppe tout et fait fonctionner le curseur. Nous voulons que le curseur s'ouvre lorsque la balise d'ancrage **slider-trigger** est cliquée. Nous obtenons donc cet élément dans une variable **sliderTrigger**. Plus tard, nous obtenons l'élément curseur entier dans la variable **slider**. Maintenant, nous ajoutons un écouteur d'événement qui implémente une fonction lorsque l'élément **sliderTrigger** est cliqué.

```
sliderTrigger.addEventListener( "click" , function(el) {} );
```

La fonction qui est écrite contrôle la mécanique de l'ouverture et de la fermeture de la barre de menu coulissante. Rappelez-vous que nous avions une classe **slider-parent** active et normale.

L'astuce que nous implémentons ici est d'ajouter la classe active lorsque l'élément **sliderTrigger** est cliqué, et de supprimer la classe active lorsque le même élément est cliqué à nouveau. Pour ce faire, nous utilisons le code donné ci-dessous, pour vérifier si la variable contient la classe active.

```
slider.classList.contains("active")
```

Si la valeur est vraie, nous supprimons la classe active de la liste. Que se passe-t-il alors? La barre de menu coulissante se ferme. Si la valeur est fausse, nous ajoutons la classe active à la liste de classes. Maintenant, que se passe-t-il? Oui, la barre de menu coulissante est affichée. C'est aussi simple que cela.

```
slider.classList.add("active")
```

```
slider.classList.remove("active")
```

### Voilà, c'est fait!! Regardez qui applaudit ;)

![Image](https://cdn-media-1.freecodecamp.org/images/1*FPKDw_SRNiaOfjL1fPBBRg.gif)

Le fonctionnement du même code est montré ci-dessous dans le CodePen.

Bien que ce soit un exemple de base, j'envoie des exemples de barres de menu coulissantes plus complexes et de différents types dans ma newsletter.

[Dépôt Github de Giyaletter](https://github.com/girishpatil/giya)

Compte Twitter: [Supriya S](https://twitter.com/s_omeal) et [Girish Patil](https://twitter.com/theevilhead)

Merci. Bon codage :)

Découvrez nos produits:

[paybackhub.com](http://paybackhub.com) et [certhive.com](http://certhive.com)