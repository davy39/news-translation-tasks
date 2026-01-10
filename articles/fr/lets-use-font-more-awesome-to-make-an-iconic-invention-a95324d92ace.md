---
title: Font (More) Awesome — une invention iconique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-08T07:31:19.000Z'
originalURL: https://freecodecamp.org/news/lets-use-font-more-awesome-to-make-an-iconic-invention-a95324d92ace
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cPpBR06SrC96_qi9Bw5Pmw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Font (More) Awesome — une invention iconique
seo_desc: 'By Pubudu Dodangoda

  Whether you are building a website, a mobile app, or even a standalone app, there
  are few things you can never escape. The proper use of graphics and icons is one
  such basic need. Fancy icons are just as important as alignments an...'
---

Par Pubudu Dodangoda

Que vous construisiez un site web, une application mobile ou même une application autonome, il y a quelques choses dont vous ne pouvez jamais vous échapper. L'utilisation appropriée des graphiques et des icônes est l'un de ces besoins de base. Les icônes fantaisistes sont tout aussi importantes que les alignements et les combinaisons de couleurs. C'est parce qu'une seule icône peut exprimer ce que cent mots peuvent dire !

Bien qu'il existe de nombreuses façons d'ajouter des icônes à un site web, la méthode la plus populaire consiste à utiliser Font Awesome. Une fois que vous avez effectué les configurations requises, l'ajout d'une icône est aussi simple que ceci :

```
<i class="fa fa-bell"></i>
```

Pourtant, il existe des situations où l'ensemble d'icônes fourni par Font Awesome est insuffisant. Par exemple, j'ai récemment voulu utiliser les logos de Facebook, Twitter et Airbnb sur un site web. Et cela m'a surpris — l'icône Airbnb n'était pas incluse dans Font Awesome. En fait, la communauté avait demandé l'icône Airbnb il y a environ **3 ans**. Pourtant, l'icône n'est toujours pas dans l'ensemble officiel d'icônes.

De plus, si vous voulez une icône personnalisée qui n'est pas très populaire, le moyen le moins complexe de l'ajouter est d'utiliser une balise `img`. C'est trop de travail par rapport à l'utilisation de Font Awesome. D'un autre côté, les développeurs de Font Awesome ne peuvent pas répondre à toutes les demandes d'icônes, pratiquement parlant.

J'ai donc cherché un moyen facile d'obtenir les icônes dont j'avais besoin, sans dépendre d'un tiers. Heureusement, j'ai trouvé un outil appelé [Calligraphr](https://www.calligraphr.com/). Je vais maintenant expliquer comment j'ai utilisé cet outil, quelques connaissances en CSS et quelques autres astuces simples pour pouvoir faire ce qui suit dans mon code :

```
<i class="fa fa-troll"/><i class="fa fa-like-a-boss"/><i class="fa fa-lol"/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/06GY02wLrvOJ37HhebA2R9Jb7c5ceMs-avez)

Plutôt cool, non ? Alors **construisons Font More Awesome !**

### Création d'une police

La première étape de notre voyage est de créer la police Font More Awesome en utilisant [les instructions sur leur site web](https://www.calligraphr.com/en/webapp/app_home/?/). La première étape consiste à télécharger le modèle. Voici un exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/xvjYDSmV1iYpfqMQtNBhcrOlAaYQUR6hOb3X)
_Modèle Calligraphr_

Maintenant, ce que nous devons faire, c'est remplir ces cases avec les icônes souhaitées. Vous pouvez soit imprimer et dessiner les icônes à la main, soit utiliser un outil comme Adobe Photoshop ou GIMP pour utiliser des images téléchargées depuis Internet.

Après avoir rempli le modèle, il ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/T9jAuPS950YFzb61zATJA0iucZjDz1b4pMKU)

La prochaine chose que vous devez faire est assez simple. Il suffit de télécharger le modèle rempli sur le site web de Calligraphr et de cliquer sur le bouton « build font » — et BOOM ! Votre police personnalisée sera téléchargée. Appelons-la `FontMoreAwesome.otf`

Si vous vous demandez quel genre de magie vient de se produire, cela s'appelle la [vectorisation](https://en.wikipedia.org/wiki/Image_tracing) ou le traçage d'image. En raison de l'algorithme de traçage sous-jacent, vous pourriez remarquer de légères différences entre l'image utilisée et l'icône réelle créée. Mais, une fois les images converties en vecteur, elles peuvent être redimensionnées sans perdre en qualité.

### Intégration avec Font Awesome

Bien sûr, vous pouvez traiter le nouveau fichier de police comme un ensemble d'icônes séparé. Mais ne serait-ce pas cool si nous pouvions étendre la police Font Awesome elle-même ? Faisons-le !

Une chose que vous devez comprendre ici est que nous allons hériter des règles CSS définies par le fichier CSS de Font Awesome. Par exemple, il contiendra une entrée comme suit :

```
.fa {  display: inline-block;  font: normal normal normal 14px/1 FontAwesome;  font-size: inherit;  text-rendering: auto;  -webkit-font-smoothing: antialiased;  -moz-osx-font-smoothing: grayscale;}
```

Cela signifie que lorsque nous définissons un élément d'icône comme suit, il héritera des styles tels que `display`, `font-size` et `text-rendering` de ce qui précède.

```
<i class="fa fa-troll"/>
```

Maintenant, définissons notre fichier CSS personnalisé. Appelons le fichier `font-more-awesome.css`

La première entrée de ce fichier doit être la déclaration font-face. Cela peut être fait comme suit. Pas de gros problème. Juste un peu de CSS de base.

```
@font-face {    font-family: 'FontMoreAwesome';    src: url('../fonts/FontMoreAwesome.otf');    font-weight: normal;    font-style: normal;}
```

Ensuite, nous pouvons facilement définir les icônes personnalisées que nous voulons comme ceci :

```
.fa-troll:before {    font-family: FontMoreAwesome;    content: "A";}.fa-lol:before {    font-family: FontMoreAwesome;    content: "B";}.fa-like-a-boss:before {    font-family: FontMoreAwesome;    content: "C";}
```

Notez ici que nous définissons les icônes comme des pseudo-éléments en utilisant le sélecteur `before`. De cette façon, nous pouvons injecter le contenu que nous voulons dans l'élément qui utilise ces classes.

Dans la police FontMoreAwesome que nous avons créée, « A », « B » et « C » sont représentés par les icônes pour Troll, Lol et Like-a-boss respectivement. Ce n'est pas la meilleure façon de procéder, cependant.

Font Awesome utilise la zone d'usage privé Unicode (PUA) pour s'assurer que les lecteurs d'écran ne lisent pas des caractères aléatoires qui représentent des icônes.

Mais pour notre exemple, nous allons nous en tenir aux lettres de l'alphabet anglais pour garder l'histoire simple.

Une autre chose à noter dans l'exemple ci-dessus est que nous remplaçons la font-family définie par Font Awesome tout en injectant du contenu personnalisé.

### Utilisons Font More Awesome

La dernière étape consiste à charger ce fichier CSS dans le fichier index.html, ce qui est assez facile.

```
<link href="css/font-more-awesome.css" rel="stylesheet">
```

Maintenant, vous pouvez utiliser ces icônes comme n'importe quelle autre icône `fa`. Par exemple, l'icône suivante sera grande et tournera.

```
<i class="fa fa-troll fa-spin fa-lg"/>
```

### Avez-vous aimé cette histoire ? Alors il y a une petite chose que vous pourriez faire...

![Image](https://cdn-media-1.freecodecamp.org/images/bD2IJyIxD9odMO7kgFmvcbVVQPDaCUceF69M)