---
title: 'Tutoriel Bootstrap : Apprenez à créer votre premier site avec Bootstrap 4'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-04T09:56:29.000Z'
originalURL: https://freecodecamp.org/news/building-your-first-bootstrap-4-0-site-b54bbff6bc55
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kEPuAx-hfMY6IYJRryX_Hg.png
tags:
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: 'Tutoriel Bootstrap : Apprenez à créer votre premier site avec Bootstrap
  4'
seo_desc: 'By Per Harald Borgen

  A quick tutorial to get you up to speed with the latest version of Bootstrap.


  In my opinion, the best way to learn a new technology is often to start building
  stuff from day one. This gives a sense of meaning to the learning pro...'
---

Par Per Harald Borgen

#### Un tutoriel rapide pour vous familiariser avec la dernière version de Bootstrap.

![Image](https://cdn-media-1.freecodecamp.org/images/Z4irOKS7b5aR5aWnh4yuB3Yme-IU9BM0vraJ)

À mon avis, la meilleure façon d'apprendre une nouvelle technologie est souvent de commencer à construire des choses dès le premier jour. Cela donne un sens au processus d'apprentissage. De plus, c'est gratifiant de voir un produit apparaître devant vous alors que vous vous battez à travers le matériel.

Donc dans cet article, je vais vous guider à travers la création d'un site web simple en utilisant Bootstrap 4.0 tout en mettant en lumière les nouvelles fonctionnalités les plus importantes de la bibliothèque.

Si vous voulez apprendre correctement Bootstrap 4.0, consultez [ce cours gratuit sur Scrimba !](https://scrimba.com/g/gbootstrap4?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_tutorial_article)

![Cliquez sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*urFRJZAIpDzoefSXnvCWhw.png)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/gbootstrap4?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbootstrap4_tutorial_article)_

Maintenant, commençons.

### Ce que nous allons construire

Nous allons construire un site web de portfolio de base. Bien qu'il soit simple, il contient plusieurs concepts de base que vous devrez apprendre pour utiliser correctement Bootstrap 4.0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kEPuAx-hfMY6IYJRryX_Hg.png)

Si vous voulez jouer avec le code, consultez [ce terrain de jeu Scrimba](https://scrimba.com/c/cbGBwUb?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_tutorial_article). N'hésitez pas à l'utiliser comme référence si vous ne comprenez pas quelque chose dans l'article et que vous avez besoin d'expérimenter par vous-même.

### La barre de navigation

Commençons par la barre de navigation. Dans Bootstrap 4.0, ils ont simplifié les barres de navigation, car elles nécessitent un peu moins de balisage maintenant. Voici ce dont nous avons besoin pour créer la barre de navigation la plus simple possible :

```html
<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Mon portfolio</a>
</nav>
```

Mon portfolio

Ce qui donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6pEAqF3q0nsD3bM38_pLQ.png)

La classe `bg-light` rend l'arrière-plan gris clair tandis que la classe `navbar-light` donne au texte une couleur foncée. Par défaut, la couleur du texte dans les barres de navigation est bleue, cependant, je pense qu'elle est plus belle avec la classe `navbar-light`.

Ajoutons du contenu à notre barre de navigation, au même niveau que la balise d'ancrage de la marque :

```html
<ul class="navbar-nav">  
  <li class="navbar-item">  
    <a href="#" class="nav-link">Page d'accueil</a>  
  </li>  
  <li class="navbar-item">  
    <a href="#" class="nav-link">Blog</a>  
  </li>  
  <li class="navbar-item">  
    <a href="#" class="nav-link">À propos</a>  
  </li>  
  <li class="navbar-item">  
    <a href="#" class="nav-link">Contactez-nous</a>  
  </li>  
</ul>

```

Les trois classes à remarquer ici sont `navbar-nav`, `navbar-link` et `navbar-item`. Ensemble, elles construisent les options de navigation comme vous le souhaitez.

Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fpG4uxcu7-iKPpTHBcNCeA.png)

Cependant, nous devons maintenant la rendre réactive, car nous voulons que nos options de navigation se replient en une icône de hamburger sur les petits écrans. Pour y parvenir, nous devons faire deux choses :

1. Dire à Bootstrap à quel point les options de navigation doivent se casser pour se replier en un hamburger
2. Créer le balisage pour le hamburger

Pour la rendre réactive, nous allons ajouter la classe `navbar-expand-md` à l'élément `nav` lui-même :

```html
<nav class="navbar navbar-light bg-light `**navbar-expand-md**`">  
...  
</nav

```

Cela indique à Bootstrap que nous voulons que les options de la barre de navigation basculent entre les états développé et replié au point d'arrêt `md`, qui est à `768px`.

Nous devons également envelopper nos options de navigation dans une div (avec les deux classes `collapse` et `navbar-collapse`) qui indique à Bootstrap que c'est la partie que nous voulons replier.

```html
<div class="collapse navbar-collapse" id="navbarNav">  
  <ul class="navbar-nav">  
  ...   
  </ul>  
</div>

```

L'id `navbarNav` est pour connecter cet élément avec l'attribut `data-target` dans l'icône du hamburger, que nous allons créer comme ceci :

```html
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">  
  <span class="navbar-toggler-icon"></span>  
</button>
```

Nous avons maintenant une belle barre de navigation, qui se replie et se déploie à notre point d'arrêt choisi :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1dn65y8seTpzTi1EV6EaVw.gif)

### Jumbotron

L'étape suivante est de créer quelque chose qui accueille nos utilisateurs sur le site web en dessous de la barre de navigation. Pour cela, nous allons utiliser le composant [jumbotron](https://getbootstrap.com/docs/4.0/components/jumbotron/). C'est super simple :
```html
<div class="jumbotron jumbotron-fluid">  
  <div class="container">  
  <h1 class="display-3">Bienvenue sur mon site web</h1>  
  <p class="lead">Je suis un développeur et designer. Consultez mon portfolio ci-dessous</p>  
</div>

```

Ce qui donne le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*6gtZU68RZIRChydZ7_nNxg.png)

Les classes `display-3` et `lead` sont des classes de typographie, qui rendent le texte un peu plus opinionné et mieux présenté à mon avis. Vous pouvez en lire plus sur [la typographie dans Bootstrap 4.0 ici.](http://When%20you%20need%20a%20heading%20to%20stand%20out,%20consider%20using%20a%20display%20heading%E2%80%94a%20larger,%20slightly%20more%20opinionated%20heading%20style.)

### Le contenu principal — Grille et cartes

En dessous de notre jumbotron, nous allons ajouter le contenu principal de notre site web, qui consistera en quatre cartes. Une [carte](https://getbootstrap.com/docs/4.0/components/card/) est un tout nouveau composant de Bootstrap 4.0, et elle remplace les panneaux, les puits et les miniatures de Bootstrap 3.0.

Commençons par voir ce que nous voulons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*atNp4J0OetHwEbTx0w0Twg.png)

#### Création de la grille

Pour les faire apparaître correctement comme ceci, et pour également s'assurer qu'elles fonctionnent bien de manière réactive, nous devons envelopper les cartes dans une grille. La grille est l'un des éléments principaux de Bootstrap, et de nombreux développeurs utilisent la bibliothèque uniquement à cause de la grille.

Nous allons commencer par créer une grille très simple sans contenu. Dans Bootstrap, vous créez toujours des lignes en premier, puis vous enveloppez des colonnes à l'intérieur des lignes. Par défaut, la grille peut être divisée en 12 colonnes en largeur.

Au-dessus du point d'arrêt `sm`, nous voulons que chacune des cartes prenne la moitié de la largeur, donc nous donnerons aux colonnes une classe `col-sm-6`. Lorsque l'écran atteint le point d'arrêt `lg`, nous voulons quatre cartes en largeur, donc nous ferons `col-lg-3`.

```html
<div class="container">  
  <div class="row">  
    <div class="col-sm-6 col-lg-3">colonne</div>  
    <div class="col-sm-6 col-lg-3">colonne</div>  
    <div class="col-sm-6 col-lg-3">colonne</div>  
    <div class="col-sm-6 col-lg-3">colonne</div>  
  </div>  
</div>

```

Cela donne la disposition réactive suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*cFB-CAHtMUqhu4C1P8Vcdw.gif)

#### Création des cartes

Maintenant, nous devons simplement remplacer le texte des colonnes par un composant de carte. Voici le balisage pour notre carte :

```html
<div class="card">  
  <img class="card-img-top" alt="Image d'en-tête de la carte" src="img1.png">  
  <div class="card-body">  
    <h5 class="card-title">Projet 1</h5>  
    <p class="card-text">Un projet génial</p>  
    <a href="#" class="btn btn-info">Voir le projet</a>  
  </div>  
</div>

```

Pour transformer une `div` en carte, nous ajouterons simplement la classe `card`. Si nous voulons qu'une image apparaisse dans l'en-tête de la carte, nous ajouterons `card-img-top`. Pour le reste du contenu, nous utiliserons les classes `card-body`, `card-title`, et `card-text`.

Un problème, cependant, est que cette disposition ne sera pas belle lorsque la grille aura plusieurs lignes. Comme vous pouvez le voir, nous devons ajouter un peu d'espacement entre les lignes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q6VaR_rIriYA3ct6putJPQ.png)

Cela vous présentera un nouveau concept d'espacement dans Bootstrap 4.0, où vous pouvez ajouter des classes pour définir le remplissage et la marge. Nous ajouterons simplement la classe `mt-3` aux `div` de carte.

```html
<div class="card mt-3">  
...  
</div>

```

Le `mt` signifie `margin-top`, et le 3 est un nombre sur une échelle de 1 à 5, où 5 est le plus grand. Vous pouvez également faire, par exemple, `pb-4`, qui définirait le `padding-bottom` à 4. Vous avez probablement compris le principe maintenant. Une fois que nous avons ajouté cela, nous avons une belle grille avec des cartes sur notre site web.

### Formulaire de contact

Enfin, ajoutons également un formulaire de contact. Il s'agira simplement d'une nouvelle ligne dans notre grille. Cette fois, nous utiliserons également la classe `offset`, car nous ne voulons pas qu'elle soit en pleine largeur, du moins pas au-dessus du point d'arrêt `md`.

Donc, à partir de `md` et au-dessus, nous lui donnerons une largeur de six colonnes, et un décalage de trois :

```html
<div class="row mt-5">  
  <div class="col-sm-12 **col-md-6 offset-md-3**">  
    <h3>Contactez-nous !</h3>  
    _...le formulaire va ici..._  
  </div>  
</div>

```

Maintenant, regardons le code pour le formulaire lui-même :

```html
<form>  
  <div class="form-group">  
    <input type="text" class="form-control" id="email" placeholder="Votre email..">  
  </div>  
  <div class="form-group">  
    <textarea class="form-control" placeholder="Votre message..">              
    </textarea>  
  </div>  
  <button type="submit" class="btn btn-primary">Envoyer</button></form>

```

Les contrôles — comme `<input>` et `<textarea>` — sont stylisés avec la classe `form-control`. Ils lui donnent l'apparence d'un formulaire Bootstrap classique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3yIL5iR0__uNFnHkXgSivw.png)

Et c'est tout ! Vous avez maintenant créé votre tout premier site web avec Bootstrap 4.0. Si vous voulez apprendre correctement la bibliothèque, assurez-vous de consulter notre [cours gratuit sur Scrimba.](https://scrimba.com/g/gbootstrap4?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_tutorial_article)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le cofondateur de [Scrimba](https://scrimba.com) — la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gbootstrap4_tutorial_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gbootstrap4_tutorial_article)_