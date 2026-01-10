---
title: Une introduction simple au framework jQuery Mobile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-02T16:49:43.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-jquery-mobile-framework
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99e8740569d1a4ca225a.jpg
tags:
- name: jQuery
  slug: jquery
- name: mobile app development
  slug: mobile-app-development
seo_title: Une introduction simple au framework jQuery Mobile
seo_desc: "By Alfrick Opidi\nWhen the world discovered the web, things were unexciting\
  \ and lifeless. For example, building a simple image mouseover application required\
  \ several lines of code, and couldn't work on some platforms. \nBut things got better\
  \ when jQuer..."
---

Par Alfrick Opidi

Lorsque le monde a découvert le web, les choses étaient peu excitantes et sans vie. Par exemple, la création d'une application simple de survol de souris sur une image nécessitait plusieurs lignes de code et ne fonctionnait pas sur certaines plateformes. 

Mais les choses se sont améliorées avec l'introduction de jQuery, car il a permis aux développeurs de créer des applications JavaScript impressionnantes qui pouvaient fonctionner confortablement dans divers environnements.

Après cela, l'équipe jQuery a élevé les choses d'un cran en développant jQuery UI, ce qui a permis aux développeurs de créer des applications web esthétiques sur le noyau jQuery existant. 

Mieux encore, en 2010, jQuery Mobile a été introduit, ce qui a rendu le développement beaucoup meilleur et plus efficace.

Conçu avec une orientation vers les téléphones mobiles, [jQuery Mobile](http://jquerymobile.com/) est un framework unifié et efficace qui offre des composants UI, des transitions de données et d'autres fonctionnalités passionnantes. 

jQuery Mobile tire parti des fonctionnalités de HTML5, CSS3, jQuery, ainsi que de jQuery UI dans un seul framework qui permet aux développeurs d'atteindre une cohérence sur différentes plateformes et appareils.

## Fonctionnalités de base de jQuery Mobile

### 1. Grande simplicité et facilité d'utilisation

Le framework jQuery Mobile est simple et flexible. Puisque l'interface de configuration du framework est pilotée par le balisage, les développeurs peuvent facilement construire leurs interfaces d'application de base complètes en HTML, avec un minimum ou pas de code JavaScript. 

Les tâches complexes nécessitant plusieurs lignes de code JavaScript, telles que les appels Ajax et la manipulation du DOM, peuvent être facilement réalisées avec quelques [lignes de code](https://www.freecodecamp.org/news/long-code-vs-short-code/) dans jQuery Mobile.

Par exemple, si nous voulons qu'un utilisateur clique et masque du texte après qu'une page a été créée dans le DOM, mais avant que l'amélioration ne soit complète, nous pouvons simplement utiliser le gestionnaire d'événements **pagecreate**. C'est quelque chose qui nécessiterait plusieurs lignes de code pour être accompli sans jQuery Mobile. 

```javascript
$(document).on("pagecreate","#mypagetest",function(){
  $("span").on("click",function(){
    $(this).hide();
  });                       
});
```

Dans le code ci-dessus, le paramètre **#mypagetest** fait référence à l'id de la page qui spécifie l'événement de la page. De plus, la méthode **on()** est utilisée pour attacher les gestionnaires d'événements.

De plus, sa simplicité permet aux développeurs de diviser leurs applications en plusieurs pages. Avec le framework, les développeurs peuvent "écrire moins, et faire plus".

### 2. Amélioration progressive et dégradation élégante

L'[amélioration progressive](https://www.gov.uk/service-manual/technology/using-progressive-enhancement) et la dégradation élégante sont des fonctionnalités clés qui propulsent l'agilité de jQuery Mobile. Elles lui permettent de supporter à la fois les appareils haut de gamme et moins capables (par exemple, ceux qui manquent de support JavaScript).

Le framework permet aux développeurs de construire des applications qui peuvent être accessibles par le plus grand nombre de navigateurs et d'appareils, qu'il s'agisse d'Internet Explorer 6 ou du dernier Android ou iPhone.

jQuery Mobile donne également aux développeurs la capacité de rendre le contenu de base (tel que construit) sur des appareils basiques. Et les plateformes et navigateurs plus sophistiqués seront de plus en plus enrichis en utilisant des JavaScript et CSS supplémentaires, liés externement.

### 3. Support des entrées conviviales

Lors du développement avec jQuery Mobile, les développeurs peuvent inclure une [API](https://blog.api.rakuten.net/what-is-an-api/) simple pour supporter les entrées tactiles, souris et curseur. Plusieurs types d'éléments de formulaire faciles à styliser et adaptés au tactile sont également inclus dans le framework.

Les exemples incluent des ensembles de cases à cocher et de boutons radio, des curseurs, des filtres de recherche et des éléments de sélection de menu. De plus, chacun des éléments de formulaire inclut une version alternative 'mini', qui peut être facilement incorporée dans les pages web mobiles.

Par exemple, voici comment créer un bouton de case à cocher en utilisant jQuery Mobile. Remarquez que l'attribut **data-mini="true"** est ajouté pour créer une version mini du bouton. 

```html
<form>
    <input type="checkbox" name="checkbox-mini-0" id="my-checkbox" data-mini="true">
    <label for="checkbox-mini-0">Cliquez ici pour accepter</label>
</form>
```

Au-delà de tout cela, pour garantir que l'expérience utilisateur est optimisée sur les appareils mobiles, le framework dispose d'un système de navigation riche basé sur Ajax qui permet des transitions de page animées de manière transparente.

Avec les événements de transition de jQuery Mobile, vous pouvez animer la transition de la page active actuelle vers la nouvelle page. 

Par exemple, vous pouvez utiliser l'événement **pagebeforeshow** (déclenché sur la page "à") et l'événement **pagebeforehide** (déclenché sur la page "de") lors de la transition d'une page à l'autre. Les deux événements sont déclenchés avant que l'animation de transition ne commence.

Voyons comment ils peuvent être appliqués : 

```javascript
$(document).on("pagebeforeshow","#myfirstpage",function(){ 
    
    // Lorsque vous entrez dans myfirstpage
    
  alert("myfirstpage est sur le point d'apparaître");
    
});

$(document).on("pagebeforehide","#myfirstpage",function(){ 
    
    // Lorsque vous quittez myfirstpage
    
  alert("myfirstpage est sur le point de disparaître");
});
```

### 4. Accessibilité

Outre ses capacités multiplateformes, jQuery pour mobile a été créé avec une forte considération pour l'accessibilité. 

Le framework est livré avec le support des Applications Internet Riches Accessibles (WAI-ARIA) pour aider les personnes handicapées utilisant des lecteurs d'écran et d'autres technologies d'assistance à accéder facilement aux pages web.

### 5. Taille légère

La taille légère de jQuery Mobile (environ 40 Ko lorsqu'il est minifié) ajoute à sa rapidité. De plus, le fait qu'il utilise un minimum de dépendances d'images accélère également considérablement ses capacités.

### 6. Thèmes et widgets UI

jQuery Mobile dispose d'un système de thèmes intégré qui permet aux développeurs de déterminer leur propre style d'application. Avec le jQuery Mobile Themeroller, les développeurs peuvent personnaliser efficacement leurs applications pour les adapter à leurs couleurs, goûts et préférences.

Le framework est également livré avec divers widgets innovants et multiplateformes qui permettent aux développeurs de créer des applications mieux personnalisées. 

Certains des widgets disponibles sont les barres d'outils persistantes, les boutons, les dialogues et le widget popup couramment utilisé.

### 7. Réactivité

La réactivité complète du framework permet aux mêmes bases de code sous-jacentes de s'adapter confortablement à différents types d'écrans, des appareils mobiles aux écrans de taille bureau.

## Structure de page de base de jQuery Mobile

La structure de jQuery Mobile comprend tous les composants UI et attributs nécessaires pour créer des applications et sites web mobiles conviviaux et riches en fonctionnalités de tous types — qu'ils soient basiques ou avancés.

Vous pouvez utiliser jQuery Mobile pour créer des pages web, divers types de vues de liste, des barres d'outils, une large gamme d'éléments de formulaire et de boutons, des dialogues, ainsi que d'autres fonctionnalités.

Importamment, puisque jQuery Mobile est créé sur le noyau jQuery, il permet aux développeurs de tirer parti du code jQuery UI et d'accéder à des installations clés. Celles-ci incluent des animations et effets d'image robustes pour les pages web, la manipulation du DOM, la gestion des événements et Ajax pour la communication avec le serveur.

Prenons un aperçu de l'apparence du code de développement jQuery Mobile.

Par exemple, en cette période de pandémie de COVID-19 où la plupart des gens travaillent depuis chez eux ou depuis des [espaces de coworking](https://novelcoworking.com/locations/ohio/cincinnati/hooper-building/), créons une simple page web qui démontre quelques erreurs de gestion d'équipe que les gens commettent.

Voici le code :

```html
<!DOCTYPE html>
<html>

<head>
  <title>Exemple jQuery Mobile</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" />
  <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
  <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
</head>

<body>
  <div data-role="page" date-theme="c">
    <div data-role="header">
      <h1>Exemple fCC jQuery Mobile</h1>
    </div>
    <div data-role="content">
      <p>Erreurs de gestion d'équipe en télétravail COVID-19 à éviter</p>
    </div>
    <p>
    <ul data-role="listview" data-inset="true" data-filter="true"></ul>
    </p>
    <p>
    <ul>
      <li><a href="#">Utiliser des outils inutiles</a></li>
      <li><a href="#">Négliger les évaluations d'équipe</a></li>
      <li><a href="#">Micromanagement</a></li>
      <li><a href="#">Embaucher trop rapidement</a></li>
      <li><a href="#">Ne pas avoir de plans de secours</a></li>
    </ul>
    </p>
    <div data-role="footer">
      <h4>alfrickopidi.com, 2020 - Copyright</h4>
    </div>
  </div>
</body>

</html>
```

Voici le résultat lorsque les lignes de code jQuery Mobile ci-dessus sont ouvertes sur un navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image1.png)

Notamment, lorsque la taille du navigateur est réduite ou augmentée, la taille des éléments de la liste s'ajuste également de manière appropriée. Par conséquent, la page web peut être facilement accessible sur divers appareils avec différentes résolutions d'écran sans se soucier du manque de cohérence. La taille des éléments changera en conséquence pour s'adapter au type d'appareil.

Comme vous pouvez le voir dans l'exemple de code ci-dessus, le document est un simple HTML5 qui inclut les trois éléments suivants :

* Fichiers du CSS jQuery Mobile (jquery.mobile-1.4.5.min.css)
* Fichiers du dépôt jQuery (jquery-1.11.1.min.js)
* Fichiers du dépôt jQuery Mobile (jquery.mobile-1.4.5.min.js)

Ces fichiers sont directement liés au CDN jQuery. Une autre alternative est de se rendre sur la [page de téléchargement](http://jquerymobile.com/download/) pour obtenir ces fichiers et les héberger sur un serveur privé.

Importamment, l'inclusion de la balise méta "viewport" lors du développement avec jQuery Mobile indique aux appareils que la largeur de la page et la largeur de l'écran de l'appareil sont équivalentes (width=device-width).

La balise indique également au navigateur de zoomer à 100 pour cent (scale=1). Si l'échelle est modifiée à 2, par exemple, le navigateur zoome la page web de 50 pour cent.

Un examen plus approfondi du code révèle certains attributs "_data-" étranges dispersés dans celui-ci. Il s'agit d'une fonctionnalité améliorée de HTML5 qui permet aux développeurs de transmettre des données organisées à travers une application — par exemple, l'attribut _data-role="header"_ définit la section d'en-tête de la page web.

L'exemple ci-dessus ne fait qu'effleurer la surface des choses que les développeurs peuvent réaliser en utilisant jQuery Mobile. La [documentation](https://demos.jquerymobile.com/1.4.5/) du framework est facile à suivre et décrit ses nombreuses fonctionnalités, y compris la liaison de pages, l'incorporation de transitions de page animées et la conception de boutons.

## Conclusion

jQuery pour mobile est un framework riche en ressources, construit avec les capacités de jQuery, HTML5 et CSS pour gérer efficacement certains problèmes de compatibilité multiplateforme, multidevice et multinavigateur.

Le framework offre de grandes opportunités pour créer des applications mobiles et web puissantes, entièrement réactives et prêtes pour l'avenir.

Allez-vous l'essayer ?