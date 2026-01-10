---
title: La technique des Fab Four pour créer des emails responsives sans Media Queries
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-11T18:34:38.000Z'
originalURL: https://freecodecamp.org/news/the-fab-four-technique-to-create-responsive-emails-without-media-queries-baf11fdfa848
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8MfWNObJP1mFnYJzKkdflQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: email
  slug: email
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: La technique des Fab Four pour créer des emails responsives sans Media
  Queries
seo_desc: 'By Rémi Parmentier

  I think I found a new way to create responsive emails, without media queries. The
  solution involves the CSS calc() function and the three width, min-width and max-width
  properties.

  Or as I like to call them all together: the Fab Fo...'
---

Par Rémi Parmentier

Je pense avoir trouvé une nouvelle façon de créer des emails responsives, sans media queries. La solution implique la fonction CSS _calc()_ et les trois propriétés _width_, _min-width_ et _max-width_.

Ou comme j'aime les appeler ensemble : les Fab Four (en CSS).

![Image](https://cdn-media-1.freecodecamp.org/images/1*8MfWNObJP1mFnYJzKkdflQ.png)
_calc() & width & min-width & max-width, aka Les Fab Four (en CSS)._

### Le problème

Créer des emails responsives est difficile, surtout depuis que les clients email sur mobile (comme Gmail, Yahoo ou Outlook.com) ne supportent pas les media queries. Une [approche hybride](http://labs.actionrocket.co/the-hybrid-coding-approach), une [stratégie Gmail first](https://julie.io/writing/gmail-first-strategy-for-responsive-emails/), ou [un email responsive sans media queries](http://webdesign.tutsplus.com/tutorials/creating-a-future-proof-responsive-email-without-media-queries--cms-23919) sont d'excellentes façons de s'adapter à cette situation.

Cette dernière approche a été ma préférée jusqu'à présent. La grande idée est d'avoir des colonnes en tant que _<div>_ avec une largeur fixe alignées _avec « display:inline-block »_. Une fois qu'un écran ne peut plus contenir deux blocs côte à côte, ils s'empileront naturellement l'un sous l'autre. Mais j'ai toujours eu un problème avec cela.

Une fois que tous les blocs sont empilés, ils ne prennent pas la pleine largeur de l'email.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ybAI7RS4xjmQY3Y_B4jUnw.png)
_Sans media queries, les colonnes peuvent s'empiler mais ne pas s'étendre en pleine largeur. [Illustration par Nicole Merlin](http://webdesign.tutsplus.com/tutorials/creating-a-future-proof-responsive-email-without-media-queries--cms-23919" rel="noopener" target="_blank" title=")._

Je cherche des moyens de résoudre ce problème depuis longtemps. Flexbox est un bon candidat, mais malheureusement [le support de Flexbox dans un email](https://medium.com/@hteumeuleu/using-flexbox-in-an-email-4b1aa7a69886#.83apq23wx) est désastreux.

### Une solution

#### _Rappel sur width, min-width et max-width_

En plus de la fonction _calc()_, la solution que j'ai trouvée implique ces trois propriétés CSS. Afin de comprendre pleinement comment cela fonctionne, voici un rappel de la manière dont _width_, _min-width_ et _max-width_ se comportent lorsqu'ils sont utilisés ensemble (comme [clairement résumé](http://goetter.tumblr.com/post/64119638003/quiz-parce-que-la-taille-%C3%A7a-compte) par le développeur front-end français Raphaël Goetter).

* Si la valeur de _width_ est supérieure à la valeur de _max-width_, _max-width_ l'emporte.
* Si la valeur de _min-width_ est supérieure aux valeurs de _width_ ou _max-width_, _min-width_ l'emporte.

Pouvez-vous deviner quelle serait la largeur d'une boîte avec les styles suivants ?

```
.box {    width:320px;    min-width:480px;    max-width:160px;}
```

_(Réponse : la boîte serait large de 480px.)_

#### Introduction à calc() et la formule magique

Sans plus attendre, voici un exemple des Fab Four pour créer deux colonnes qui s'empileront et s'étendront en dessous de 480px.

```
.block {    display:inline-block;    min-width:50%;    max-width:100%;    width:calc((480px — 100%) * 480);}
```

Décomposons cela pour chaque propriété _width_.

```
min-width:50%;
```

La propriété _min-width_ définit les largeurs de nos colonnes sur ce que nous pourrions appeler notre version desktop. Nous pouvons changer cette valeur pour ajouter plus de colonnes (par exemple, 25% pour une disposition à quatre colonnes), ou définir des colonnes avec des largeurs fixes en pixels.

```
max-width:100%;
```

La propriété _max-width_ définit les largeurs de nos colonnes sur ce que nous pourrions appeler notre version mobile. À 100%, chaque colonne s'étendra et s'adaptera à la pleine largeur de leur conteneur parent. Nous pouvons changer cette valeur pour garder des colonnes sur mobile (par exemple, 50% pour une disposition à deux colonnes).

```
width:calc((480px — 100%) * 480);
```

Grâce à la fonction _calc()_, la propriété _width_ est l'endroit où la magie opère. La valeur _480_ correspond à notre valeur de breakpoint souhaitée. Les 100% correspondent à la largeur du conteneur parent de nos colonnes. Le but de ce calcul est de créer une valeur plus grande que notre _max-width_ ou plus petite que notre _min-width_, afin que l'une de ces propriétés soit appliquée à la place.

Voici deux exemples.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zCzf5ZChfB1WB5FGULzpig.png)

Avec un parent de 500px, la largeur _calculée_ est égale à -9600px. Elle est plus petite que la min-width. Donc la min-width de 50% l'emporte. Ainsi nous avons une disposition à deux colonnes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PJANsECXH1VCJ5UxxaJ-5w.png)

Avec un parent de 400px, la largeur _calculée_ est égale à 38400px. Elle est plus grande que la min-width, mais la max-width est plus petite. Donc la max-width de 100% l'emporte. Ainsi nous avons une disposition à une colonne.

### Démo

Voici une démo de ce que cette technique peut faire.   
Vous pouvez [voir la démo complète en ligne ici](http://emails.hteumeuleu.fr/wp-content/uploads/2016/02/the-fab-four.html) (ou [sur Litmus Builder](https://litmus.com/builder/9c0fce1) ou [sur CodePen](http://codepen.io/hteumeuleu/pen/VaZgqg)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*YcVo7AGzJekmg5eupqLK0A.png)
_Illustrations par [Elias Stein](https://dribbble.com/shots/2012203-Paul-George" rel="noopener" target="_blank" title=")_

Et voici deux captures d'écran de cette démo dans Gmail, sur le webmail desktop et sur l'application mobile sous iOS. Même code, rendu différent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GUknMjQDihG2WkqHIEBBUA.png)
_La démo des Fab Four telle que vue sur le webmail desktop de Gmail et sur l'application iOS de Gmail._

Dans cette démo, j'ai défini quelques exemples de différentes grilles (avec deux, trois, quatre colonnes). La première grille, avec les images, est conçue pour passer de quatre colonnes sur desktop à deux colonnes sur mobile. Les autres grilles sont conçues pour s'étendre en pleine largeur sur mobile.

Aussi, remarquez comment le titre passe d'une position alignée à gauche sur desktop à une position centrée sur mobile. Cela est réalisé en donnant au titre une largeur fixe de 190px et un « margin:0 auto; » pour le centrer. Sur desktop, le conteneur parent du titre a une min-width de 190px appliquée, donc le logo reste à gauche. Sur mobile, le conteneur parent s'étend en pleine largeur, donc le logo devient centré.

Un grand avantage de cette technique est que, puisque tout est basé sur la largeur du parent de la grille, un email peut s'adapter même sur un webmail desktop. Par exemple, sur Outlook.com, peu importe si vous choisissez d'avoir le volet de lecture en bas ou à droite, l'email répondra correctement à la largeur du volet de lecture. Cela serait impossible à faire avec des media queries.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lbGOlHr5J-I2XSlbLrfQCg.png)
_Sur Outlook.com, l'email s'adapte aux différentes vues._

### Support

Dans les navigateurs, calc() est [bien supporté depuis IE9](http://caniuse.com/#search=calc()). Il s'avère que calc() a également un assez bon support dans les clients email. Il fonctionne dans Apple Mail (sur iOS et OS X), Thunderbird, Outlook (applications iOS et Android), Gmail (webmail, applications iOS et Android), AOL (webmail), et l'ancien Outlook.com (toujours présent en Europe).

#### L'ancien Outlook.com

Outlook.com a un petit problème, cependant. Le webmail filtrera chaque propriété avec un _calc()_ qui inclut des parenthèses. Cela signifie que « calc(480px - 100%) » est supporté, mais que « calc((480px - 100%) * 480) » ne l'est pas. Puisque ma formule initiale implique des parenthèses, nous devons la refactoriser pour éviter les parenthèses. Donc la formule pour supporter l'ancien Outlook.com ressemble à ceci.

```
width:calc(480px * 480 — 100% * 480);
```

#### Clients non supportés

Bien sûr, _calc()_ n'est pas supporté dans les anciens clients email comme Lotus Notes, ou le dernier Outlook pour Windows (utilisant le moteur de rendu HTML de Word). Il ne fonctionnera pas non plus sur Outlook Web App (à la fois Office 365 et le nouveau Outlook.com) et Yahoo (webmail, applications iOS et Android). Ces deux derniers supprimeront toute propriété impliquant un _calc()_.

#### Solutions de repli

Dans ces cas, je suggérerais de dupliquer toutes les propriétés impliquées avec des valeurs de largeur fixe pour les clients qui ne supportent pas _calc()_. Afin de cacher les Fab Four de ces clients, je conseille d'utiliser des fonctions _calc()_, même si ce n'est pas techniquement utile. Notre premier exemple ressemblerait à ceci.

```
.block {    display:inline-block;    min-width:240px;    width:50%;    max-width:100%;    min-width:calc(50%);    width:calc(480px * 480 — 100% * 480);}
```

#### Outlook Web App

Cependant, Outlook Web App (à la fois Office 365 et le nouveau Outlook.com) a un autre problème. Lorsqu'une fonction _calc()_ contient une multiplication (avec le caractère « * »), le nouveau Outlook.com et Office 365 supprimeront l'attribut de style _inline_ correspondant. Cela signifie que nous devons calculer les multiplications à la main et ne garder que la soustraction résultante. Voici à quoi ressemble le calcul final pour un breakpoint de 480px.

```
width:calc(230400px — 48000%);
```

#### Préfixes WebKit

Les anciennes versions d'Android (avant Android 5.0) ou d'iOS (avant iOS 7) nécessitent des préfixes _-webkit-_ pour fonctionner. Notre version finale ressemble à ceci.

```
.block {    display:inline-block;    min-width:240px;    width:50%;    max-width:100%;    min-width:-webkit-calc(50%);    min-width:calc(50%);    width:-webkit-calc(230400px — 48000%);    width:calc(230400px — 48000%);}
```

### Limites et réflexions finales

Comme tout dans le monde du développement d'emails, la technique des Fab Four n'est pas parfaite. Voici quelques limitations auxquelles je pense :

* Cela ne fonctionnera pas sur Yahoo. La version desktop de son webmail supporte les media queries, cependant. Nous pourrions donc améliorer un peu les choses en faisant une version mobile first de notre email, puis en l'améliorant sur desktop avec des media queries.
* Vous ne pouvez définir qu'un seul breakpoint. Cela ne pose peut-être pas de problème pour les emails, car les designs dépassent rarement 600px sur desktop et ne nécessitent pas plus d'un breakpoint pour s'adapter sur mobile.
* Vous ne pouvez que diminuer le nombre de colonnes d'une version desktop à une version mobile. Bien que cela arrive rarement, vous ne pourriez pas passer d'une disposition à quatre colonnes sur mobile à une disposition à une seule colonne sur desktop.
* La version finale du calcul (pour supporter l'ancien Outlook.com et se dégrader élégamment sur le nouveau) est difficile à lire. Utiliser un préprocesseur et un mixin pour générer toutes les propriétés requises pourrait être plus qu'utile.

Je pense toujours que cette technique sera très utile dans de nombreux cas, surtout pour les optimisations Gmail. Je suis sûr qu'il y a aussi des cas d'utilisation pour les sites web (comme les widgets, les publicités, etc.).

Et j'ai hâte de voir ce que cela vous inspirera pour créer.