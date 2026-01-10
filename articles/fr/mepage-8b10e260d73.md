---
title: MePage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-08T08:50:43.000Z'
originalURL: https://freecodecamp.org/news/mepage-8b10e260d73
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6z_QTQc5m385kAYhsjlt2w.jpeg
tags:
- name: CSS
  slug: css
- name: marketing
  slug: marketing
- name: portfolio
  slug: portfolio
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: MePage
seo_desc: 'By Divya Mistry

  A Single-page Destination on the Web

  After going through some front-end development tutorials on Free Code Camp, I decided
  to try my hands at this simple Zipline challenge of creating a portfolio page. I’ll
  refer to this single-page d...'
---

Par Divya Mistry

#### Une destination monopage sur le Web

Après avoir suivi quelques tutoriels de développement front-end sur [Free Code Camp](https://www.freecodecamp.org/news/mepage-8b10e260d73/undefined), j'ai décidé de tenter ma chance avec ce simple [défi Zipline](http://www.freecodecamp.com/challenges/zipline-build-a-personal-portfolio-webpage) de création d'une page portfolio. Je vais appeler cette destination monopage un _MePage_ pour les besoins de cet article.

Nous allons procéder en deux étapes. D'abord, nous allons créer une page en utilisant [CodePen](http://codepen.io/) pour itérer notre design et le code, puis, optionnellement, nous allons la [pousser](https://help.github.com/articles/pushing-to-a-remote/) vers [Github Pages](https://pages.github.com) lorsque nous serons satisfaits des résultats. Gardez à l'esprit que tout cela peut être fait indépendamment de Codepen et de Github Pages.

Cela dit, c'est parti.

### CodePen

![Image](https://cdn-media-1.freecodecamp.org/images/1*fjd-3vkg7STzTTAUM5DNqw.png)
_page d'accueil de codepen.io_

CodePen offre un moyen facile de tester vos idées de développement front-end. Vous pouvez créer un ensemble de pages web pour apprendre et/ou montrer vos compétences en développement web, et les partager avec le monde. Nous allons l'utiliser pour construire un site personnel monopage (c'est-à-dire un _MePage_) où le visiteur peut en apprendre davantage sur vous, votre présence sur les réseaux sociaux et obtenir vos coordonnées.

Étape 1 : Créez un [+Nouveau Pen](http://codepen.io/pen/).

Étape 2 : Dans la boîte HTML, écrivez ce qui suit. Cela montre la structure générale du MePage.

```
<body>  <!-- barre de navigation -->  <!-- texte d'en-tête -->  <!-- icônes sociales -->  <!-- citation inspirante -->  <!-- à propos de moi -->  <!-- contactez-moi --></body>
```

Étape 3 : Nous allons utiliser Bootstrap pour notre site. Incluons cela pour notre usage. Cliquez sur l'icône d'engrenage dans le coin supérieur gauche du bloc CSS. Dans la fenêtre des paramètres CSS, cliquez sur le menu déroulant Ajout rapide et sélectionnez Bootstrap.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o4wtaxwaN7_MdL2LUdjNZw.png)
_Ajouter Bootstrap en utilisant l'ajout rapide dans les paramètres CSS_

Tant que nous y sommes, ajoutons également les bibliothèques jQuery et Bootstrap JavaScript pour aider à l'interactivité de la barre de navigation basée sur le menu. Pour ce faire, allez à la page des paramètres JavaScript et ajoutez rapidement les bibliothèques jQuery et Bootstrap.

Maintenant, nous commençons à remplir les différentes parties de la page.

Étape 4 : Créons d'abord la barre de navigation. Nous allons utiliser la barre de navigation [fixed-top](http://getbootstrap.com/examples/navbar-fixed-top/) de Bootstrap pour cela.

_Bien que ce ne soit pas nécessaire, vous pouvez lire les détails techniques sur la barre de navigation Bootstrap [ici](http://getbootstrap.com/components/#navbar). Cela vous aidera à personnaliser la barre de navigation plus tard._

* Créez un élément <nav> et un conteneur <div> dans le <body>. C'est là que le contenu de la barre de navigation ira.

```
<!-- barre de navigation -->  <nav class="navbar navbar-default navbar-fixed-top">    <div class="container">      <!-- contenu de la navigation -->      <!-- Ajoutez le prochain morceau de code ici -->    </div>  </nav>
```

* Nous pouvons également utiliser le design réactif pour le menu de navigation lorsque la page web est consultée sur des écrans plus petits. Le code suivant affichera le contenu des éléments de navigation dans un menu pliable sur les petits écrans. Nous allons également afficher un nom de marque ou un logo. J'ai choisi de garder mon propre nom comme nom de marque ici.

```
<div class="navbar-header">  <button type="button" class="navbar-toggle collapsed"            data-toggle="collapse" data-target="#navbar"            aria-expanded="false" aria-controls="navbar">
```

```
    <!-- ajoutez le bouton bascule avec 3 lignes/bars horizontales -->    <span class="sr-only">Basculer la navigation</span>    <span class="icon-bar"></span>    <span class="icon-bar"></span>    <span class="icon-bar"></span>  </button>  <a class="navbar-brand" href="#">Divya Mistry</a></div><!-- Ajoutez le prochain morceau de code ici -->
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*qKoRflAv-BX7nfxjkSjeiw.png)
_Barre de navigation commençant à prendre forme._

* Ensuite, nous choisissons les éléments de navigation pour la barre de navigation. Pour cet exercice, nous allons créer un lien _Accueil_ pour sauter à la vue par défaut, un lien _À propos_ pour sauter à la section « à propos de moi », et un lien _Contact_ pour sauter aux informations de contact. Ceux-ci pourraient tous être des pages différentes ; cependant, nous allons utiliser la magie des signets dans la page et Bootstrap pour garder tout dans une seule page et sauter autour des sections pertinentes. Ajoutez le code suivant où indiqué dans le morceau de code précédent.

```
<div class="navbar-collapse collapse" id="navbar">  <!-- ajoutez des éléments à la barre de navigation -->  <ul class="nav navbar-nav navbar-right">    <li><a href="#">Accueil</a></li>    <li><a href="#apropos">À propos</a></li>    <li><a href="#contact">Contact</a></li>  </ul></div><!-- Ajoutez le prochain morceau de code ici -->
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHDcqdUOcjNnh-u2cLIBrQ.png)
_Barre de navigation prête._

Nous avons terminé avec la barre de navigation maintenant. Vous remarquerez que nous avons ancré les liens _À propos_ et _Contact_ aux références #apropos et #contact, mais ils ne font rien si vous cliquez sur le lien. Créons ceux-ci avec une structure de base de notre page.

```
<div class="container">  <div class="row text-center">    <!-- texte d'en-tête -->    <!-- AJOUTEZ le morceau de code du texte d'en-tête ICI -->    <!-- icônes sociales -->    <!-- AJOUTEZ le morceau de code des boutons sociaux ICI -->    <!-- citation inspirante -->    <!-- AJOUTEZ le morceau de code de la citation inspirante ICI -->  </div>  <div class="row text-center" id="apropos">    <!-- à propos de moi -->    <!-- AJOUTEZ le morceau de code du texte À propos ICI -->  </div>  <div class="row text-center" id="contact">    <!-- contactez-moi -->    <!-- AJOUTEZ le morceau de code du texte Contact ICI -->  </div></div>
```

Commençons à remplir les différentes sections. Ajoutez les lignes de code suivantes où indiqué avec les commentaires <!_-- AJOUTEZ le 20	4 ICI -_-> dans le code HTML ci-dessus.

* Texte d'en-tête

```
<div class="col-xs-12">  <!-- titre du nom -->  <h1>Divya Mistry</h1>  <h4>Je *vais* vous bioinformatiser</h1>  <hr></div>
```

* Icônes sociales

```
<div class="col-xs-12">  <!-- boutons sociaux -->  <a class="btn btn-default" href="https://twitter.com/divyamistry" target="_blank">Twitter</a>  <a class="btn btn-default" href="https://linkedin.com/in/divyamistry" target="_blank">LinkedIn</a>  <a class="btn btn-default" href="https://github.com/divyamistry" target="_blank">Github</a></div>
```

* Citation inspirante

```
<div class="col-xs-12">  <blockquote class="blockquote-reverse my-quote">    <p>Le fou pense qu'il est sage, mais l'homme sage sait qu'il est un fou.</p>    <footer>William Shakespeare dans <cite title="India">Comme il vous plaira</cite></footer>  </blockquote></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*vDRQEOqSDYC9NhmgYlGdZw.png)
_Contenu de la section principale de la page._

Vous remarquerez qu'une partie du titre est coupée et que la citation ne semble pas très proéminente ou alignée. Nous allons corriger cela dans une minute. Continuons à ajouter les détails aux sections restantes de la page.

* Section À propos de moi. Nous allons ajouter une description sur le côté gauche et une photographie sur le côté droit.

```
<div class="col-xs-6"> <!-- À propos de moi - description -->  <p class="lead">Consommateur et producteur de trucs scientifiques.</p>  <p>Je suis étudiant en bioinformatique et biologie computationnelle. J'aime rendre la science plus facile à utiliser et à comprendre. Quand je ne suis pas au labo/bureau, je suis à la maison à écouter des airs de Bollywood.</p></div><div class="col-xs-6"> <!-- À propos de moi - photo -->  <img class="img-rounded" height="250px" alt="Visage de Divya" src="https://lh3.googleusercontent.com/kQABk1XZ1HLRrtfkZA9tZH8WDmLgDqWIG44v-IVASL65N1hWX30"></div>
```

* Contactez-moi

```
<div class="col-xs-6"> <!-- photo contactez-moi -->  <img class="img-rounded" src="https://openclipart.org/image/150px/svg_to_png/98293/1290715998.png" alt="Contactez-moi"></div><div class="col-xs-6"> <!-- texte contactez-moi -->  <address>    <strong>Divya Mistry</strong><br>    Mon adresse<br>    Unité 001<br>    Ames, IA 50011<br>    <abbr title="Numéro de téléphone">515-555-0144</abbr>  </address></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*hwSjqh2su5swE8sduMLk7A.png)
_Tout le contenu ajouté. Nous devons encore corriger l'espacement._

* Pied de page. _Ah ! Je vous laisse cela comme exercice. Essayez de lire la documentation Bootstrap et créez votre propre pied de page. Voici une idée : ajoutez un simple élément <d_iv> et fournissez votre propre note de copyright._

Étape 5 : Modifions l'espacement et l'apparence pour rendre la page plus propre. Nous allons maintenant passer au CSS.

* Abaissez le corps de sorte que le contenu ne soit pas caché derrière la barre de navigation. Bootstrap [recommande environ 70px](http://getbootstrap.com/components/#navbar-fixed-top) pour cela. J'aime utiliser les unités [em](https://en.wikipedia.org/wiki/Em_%28typography%29) pour [plusieurs raisons](http://www.w3.org/Style/Examples/007/units.en.html#font-size).

```
/* Abaissez le texte principal sous la barre de navigation */body { padding-top: 3em; }
```

* Pour l'instant, toutes les sections sont trop proches les unes des autres. Séparons-les pour donner beaucoup d'espacement entre elles. Vous pouvez jouer avec ce remplissage selon vos préférences. Je préfère environ une taille verticale typique d'écran d'ordinateur portable de 768px.

```
/* chaque ligne doit être un grand écran en soi */.row { height: 768px; }
```

* Rendons la citation de Shakespeare beaucoup plus proéminente à l'écran.

```
/* Espacement au-dessus de la citation */.my-quote { margin-top: 5em; }
```

```
/* Police, taille et couleur du texte de la citation */.my-quote>p {   font-family: "Lora", serif;   font-size: 3em;   color: #aaa;}
```

```
/* Taille et couleur de la police de l'attribution de la citation */.my-quote>footer { font-size: 1em; color: #bbb; }
```

Vous remarquerez que j'ai choisi la famille de polices [Lora](https://www.google.com/fonts/specimen/Lora) pour ma citation. Cette police est disponible via Google Fonts. Pour l'utiliser, tout ce que vous avez à faire est d'aller dans vos paramètres HTML (cliquez sur l'icône d'engrenage dans le coin supérieur gauche de l'éditeur HTML) et ajoutez la ligne suivante dans la zone de texte **Stuff for <he**ad>.

```
<link href='https://fonts.googleapis.com/css?family=Lora:400italic' rel='stylesheet' type='text/css'>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*uNnc8LmFoEwkVtP005lDmQ.png)
_Ajout de la feuille de style Google Fonts à &lt;head&gt;._

* Enfin, donnons à chaque section d'information un peu d'espace de remplissage en haut afin que lorsque nous y sautons, la barre de navigation ne cache pas le contenu.

```
/* pour chaque section de la page */#apropos { padding-top: 6em; }#contact { padding-top: 6em; }
```

_Notez que ce remplissage est nécessaire malgré le remplissage de l'élément <body>, car les ancres de signets en ligne sont référencées au haut de la vue du port d'affichage de la fenêtre du navigateur où <body> commence, et non par rapport à l'endroit où le contenu à l'intérieur de la section du corps commence._

![Image](https://cdn-media-1.freecodecamp.org/images/1*-o-kQB6Nr13Ha-yKJgiROg.png)
_CSS mis à jour pour corriger l'espacement et les alignements._

Étape 6 : Effectuez toutes les modifications CSS que vous souhaitez pour le pied de page. J'ai décidé de présenter un texte légèrement plus petit.

Voici mon [CodePen résultant](http://codepen.io/anon/pen/wKYqMW) basé sur cet exercice. Vous pouvez ajouter des images de fond au corps et à toutes les sections pour lui donner un [effet visuel agréable](http://codepen.io/ThiagoFerreir4/full/eNMxEp).

### Pages Github

![Image](https://cdn-media-1.freecodecamp.org/images/1*UP16Y8izJ8IASnBfd-ZG-g.png)

Github offre un excellent moyen d'[héberger des pages statiques](https://pages.github.com/) pour vous-même et pour vos projets. J'ai décidé de créer une [page utilisateur Github](http://divyamistry.github.io/) en utilisant les résultats de cet exercice. Le code est disponible dans [ce dépôt](https://github.com/divyamistry/divyamistry.github.io). N'hésitez pas à forker le dépôt.

_Il existe plusieurs bons tutoriels pour vous apprendre comment fonctionne Github. Si vous n'êtes pas familier avec [git](https://www.atlassian.com/git/) et [Github](https://try.github.io/levels/1/challenges/1), essayez-les. C'est une compétence qui vaut la peine d'être apprise._

![Image](https://cdn-media-1.freecodecamp.org/images/1*eAdEAIWlpYgrfTXUuaOqIg.png)
_Ma page Github utilisant ce tutoriel._

### Mots de la fin

J'espère que vous avez aimé cet exercice et que vous avez pu créer votre propre MePage. Commentez ici avec votre URL CodePen ou Github pour montrer vos résultats. Si vous avez modifié cela et créé votre propre version d'une MePage géniale, partagez-la également. J'adorerais voir cela. Et enfin, si vous voulez rester en contact, [@divyamistry](https://twitter.com/divyamistry) est un excellent moyen de crier.