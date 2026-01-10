---
title: Comment passer de jQuery à Vanilla JavaScript avec Bootstrap 5
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-31T18:09:09.000Z'
originalURL: https://freecodecamp.org/news/bootstrap-5-vanilla-js-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/bootstrap-5-vanilla-js.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: Bootstrap 5
  slug: bootstrap-5
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: Tutorial
  slug: tutorial
seo_title: Comment passer de jQuery à Vanilla JavaScript avec Bootstrap 5
seo_desc: 'By Zoltán Szőgyényi

  Bootstrap 5 is a free and open-source CSS framework directed at responsive, mobile-first
  front-end web development.

  In case you didn''t know, Bootstrap 5 alpha has been officially launched. It has
  removed jQuery as a dependency, ha...'
---

Par Zoltán Szőgyényi

[Bootstrap 5](http://v5.getbootstrap.com/) est un framework CSS gratuit et open-source destiné au développement front-end responsive et mobile-first.

Au cas où vous ne le sauriez pas, [Bootstrap 5 alpha a été officiellement lancé](https://themesberg.com/blog/bootstrap/bootstrap-version-5-alpha-whats-new). Il a supprimé jQuery comme dépendance, a abandonné le support pour Internet Explorer 9 et 10, et apporte des mises à jour impressionnantes pour les fichiers Sass, le balisage, et une nouvelle API Utility.

Ce tutoriel vous montrera comment commencer à utiliser VanillaJS au lieu de jQuery lors de la construction de sites web en utilisant la dernière version de Bootstrap 5.

## Installation

Vous devrez inclure Bootstrap 5 dans votre projet. Il existe plusieurs façons de le faire, mais pour garder les choses simples, nous inclurons le framework via CDN.

Tout d'abord, créons une page `index.html` vide à l'intérieur d'un dossier de projet :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutoriel Bootstrap 5 Vanilla JS par Themesberg</title>
</head>
<body>
    
</body>
</html>
```

Incluez la feuille de style `bootstrap.min.css` avant la fin de votre balise `<head>` :

```html
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">
```

Ensuite, incluez la bibliothèque Popper.js et le fichier JavaScript principal de Bootstrap avant la fin de votre balise `<body>` :

```html
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js" integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/" crossorigin="anonymous"></script>
```

Curieux de savoir ce que signifient les attributs `integrity` et `crossorigin` ? Voici l'explication :

**Attribut Integrity** : permet au navigateur de vérifier la source du fichier pour s'assurer que le code n'est jamais chargé si la source a été manipulée.

**Attribut Crossorigin** : est présent lorsqu'une requête est chargée en utilisant 'CORS', ce qui est maintenant une exigence de la vérification SRI lorsqu'elle n'est pas chargée depuis la 'same-origin'.

Super ! Nous avons maintenant réussi à inclure la dernière version de Bootstrap dans notre projet. L'une des différences évidentes est que nous n'avons plus eu besoin de jQuery comme dépendance, **économisant environ 82,54 Ko** de bande passante si elle est minifiée.

## Passer de jQuery à Vanilla JS

Avant de commencer cette section, vous devez savoir qu'il est toujours possible d'utiliser Bootstrap 5 avec jQuery selon la [documentation officielle](https://v5.getbootstrap.com/docs/5.0/getting-started/javascript/#still-want-to-use-jquery-its-possible).

Nous recommandons d'utiliser Vanilla JavaScript si la seule raison pour laquelle vous avez utilisé jQuery était pour le sélecteur de requête, car vous pouvez faire la même chose avec `document.querySelector('#element')` comme si c'était `$('#element')`.

La première étape consiste à créer un fichier JavaScript et à l'inclure avant la fin de la balise body mais après les deux autres inclusions :

```html
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js" integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/" crossorigin="anonymous"></script>
<script src="js/app.js"></script>
```

Alors, quand avez-vous besoin d'utiliser JavaScript avec Bootstrap 5 ? Il existe certains composants dans le framework qui fonctionnent uniquement s'ils sont initialisés via JavaScript, tels que les tooltips, les popovers et les toasts.

De plus, avec des composants tels que les modals, les dropdowns et les carousels, vous pouvez vouloir les modifier de manière programmatique en fonction d'une action de l'utilisateur ou de la logique de l'application.

### Initialisation des tooltips via Vanilla JavaScript

Nous aimons tous les tooltips, mais ils ne fonctionnent pas à moins qu'ils ne soient initialisés via JavaScript. Commençons d'abord par créer un élément tooltip à l'intérieur de notre fichier `index.html` :

```html
<button id="tooltip" type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="top" title="Tooltip on top">
    Tooltip on top
</button>
```

Survoler le bouton ne montrera pas le tooltip, car par défaut, c'est une fonctionnalité optionnelle de Bootstrap et elle doit être initialisée manuellement en utilisant JavaScript. Si vous voulez le faire avec jQuery, voici à quoi cela ressemblerait :

```js
$('#tooltip').tooltip();
```

En utilisant Vanilla JS, vous devrez utiliser le code suivant pour activer le tooltip :

```js
var tooltipElement = document.getElementById('tooltip');
var tooltip = new bootstrap.Tooltip(tooltipElement);
```

Ce que fait le code ci-dessus, c'est qu'il sélectionne l'élément avec l'id unique "tooltip" et crée ensuite un objet tooltip Bootstrap. Vous pouvez ensuite l'utiliser pour manipuler l'état du tooltip, comme montrer ou cacher le tooltip de manière programmatique.

Voici un exemple de la façon dont vous pourriez le montrer/cacher via des méthodes :

```js
var showTooltip = true;
if (showTooltip) {
    tooltip.show();
} else {
    tooltip.hide();
}
```

Si vous souhaitez activer tous les tooltips, vous pourriez également utiliser le code suivant :

```js
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
});
```

Ce qui se passe ici, c'est que nous sélectionnons tous les éléments qui ont l'attribut et la valeur `data-toggle="tooltip"` et initialisons un objet tooltip pour chacun d'eux. Cela les sauvegarde également dans une variable tooltipList.

### Basculer la visibilité de vos éléments en utilisant les méthodes Collapse JavaScript

La fonctionnalité de collapse dans Bootstrap est un autre moyen très pratique de montrer et de cacher des éléments via des attributs de données ou JavaScript.

Voici un exemple de la façon dont nous pouvons montrer ou cacher une carte lorsqu'un certain bouton est cliqué. Commençons d'abord par créer le balisage HTML :

```html
<button id="toggleCardButton" type="button" class="btn btn-primary mb-2">Basculer la carte</button>
    <div id="card" class="card collapse show" style="width: 18rem;">
        <img src="https://dev-to-uploads.s3.amazonaws.com/i/rphqzfoh2cbz3zj8m8t1.png" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">Freecodecamp.org</h5>
            <p class="card-text">Ressource géniale pour apprendre la programmation.</p>
            <a href="#" class="btn btn-primary">Apprendre à coder gratuitement</a>
        </div>
    </div>
```

Nous avons donc créé un bouton avec l'id `toggleCardButton` et une carte avec l'id `card`. Commençons par sélectionner les deux éléments :

```js
var toggleButton = document.getElementById('toggleCardButton');
var card = document.getElementById('card');
```

Ensuite, nous devons créer un objet collapsable en utilisant l'élément de carte nouvellement sélectionné :

```js
var collapsableCard = new bootstrap.Collapse(card, {toggle: false});
```

Ce que fait le drapeau `toggle:false`, c'est qu'il garde l'élément visible après la création de l'objet. S'il n'est pas présent, il cacherait la carte par défaut.

Maintenant, nous devons ajouter un écouteur d'événement pour le bouton pour l'action de clic :

```js
toggleButton.addEventListener('click', function () {
    // faire quelque chose lorsque le bouton est cliqué
});
```

Et enfin, nous devons basculer la carte en utilisant l'objet collapsable que nous avons initialisé comme ceci :

```js
toggleButton.addEventListener('click', function () {
    collapsableCard.toggle();
});
```

C'est tout ! Maintenant, la carte sera affichée/masquée chaque fois que le bouton est cliqué. Bien sûr, tout cela aurait pu être fait en utilisant la [fonctionnalité des attributs de données](https://v5.getbootstrap.com/docs/5.0/components/collapse/#via-data-attributes) de Bootstrap, mais vous pouvez vouloir basculer certains éléments en fonction d'un appel API ou d'une logique dans votre application.

## Conclusion

Si vous avez suivi ce tutoriel, vous devriez maintenant être capable d'utiliser le framework CSS le plus populaire sans avoir besoin de jQuery dans votre projet. Cela vous permet **d'économiser jusqu'à 85 Ko de données** et rend votre site web plus rapide ! Félicitations 🎉

Si vous appréciez ce tutoriel et aimez utiliser Bootstrap comme framework CSS pour vos projets, je vous invite à consulter certains des thèmes, templates et UI Kits [Bootstrap gratuits et premium](https://themesberg.com/templates/bootstrap) que nous construisons chez Themesberg ❤️