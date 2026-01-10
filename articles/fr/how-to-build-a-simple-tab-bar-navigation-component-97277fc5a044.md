---
title: Comment créer un composant de navigation à barres d'onglets simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-28T17:27:21.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-tab-bar-navigation-component-97277fc5a044
coverImage: https://cdn-media-1.freecodecamp.org/images/0*E5R1ZESIMi18_upW.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer un composant de navigation à barres d'onglets simple
seo_desc: 'By Florin Pop

  The theme for week #3 of my Weekly Coding Challenge is navigation! So let’s learn
  a bit more about it.

  Navigation

  A navigation component is crucial on a website because you want your users be able
  to easily navigate through your pages. ...'
---

Par Florin Pop

Le **thème** de la semaine #3 de mon [Défi de codage hebdomadaire](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) est la **navigation** ! Alors apprenons-en un peu plus à ce sujet.

### Navigation

Un composant de navigation est crucial sur un site web car vous voulez que vos utilisateurs puissent naviguer facilement à travers vos pages. Vous pouvez trouver un composant de navigation même sur des sites web à page unique qui permettra de sauter à une certaine section de la page. Donc, en tant que développeur, il est très utile de savoir comment construire ce type de composant.

Dans cet article, j'ai décidé de construire une [Navigation à barres d'onglets](https://codepen.io/FlorinPop17/full/qvyWxX/), mais vous pouvez construire n'importe quel type de navigation que vous voulez.

Je me suis inspiré de [ce](https://dribbble.com/shots/5925052-Google-Bottom-Bar-Navigation-Pattern) design réalisé par [Aurelien Salomon](https://dribbble.com/aureliensalomon). Voici à quoi ressemblera le résultat final de ce que nous allons construire :

%[https://codepen.io/FlorinPop17/pen/ZZajGB]

### Le HTML

La structure HTML va être simple. Nous aurons un `.tab-nav-container` et quatre `.tab` à l'intérieur :

```html
<div class="tab-nav-container">
    <div class="tab active purple">
        <i class="fas fa-home"></i>
        <p>Maison</p>
    </div>
    <div class="tab pink">
        <i class="far fa-heart"></i>
        <p>J'aime</p>
    </div>
    <div class="tab yellow">
        <i class="fas fa-search"></i>
        <p>Recherche</p>
    </div>
    <div class="tab teal">
        <i class="far fa-user"></i>
        <p>Profil</p>
    </div>
</div>
```

Comme vous pouvez le voir, chaque `.tab` a une icône (de [FontAwesome](https://fontawesome.con/)), le texte correspondant, et quelques classes supplémentaires qui seront utilisées pour donner à chaque onglet des propriétés spécifiques de `background-color` et `color`. De plus, la classe `.active`, qui sera utilisée pour styliser l'onglet actif. Assez basique, n'est-ce pas ? ?

### Le CSS

Tout d'abord, stylisons le `.tab-nav-container` :

**Note** : nous avons une largeur `fixed` sur le conteneur car nous ne voulons pas qu'il change de taille lorsque nous changeons l'onglet `.active` puisque chaque onglet peut avoir un texte qui est soit plus long soit plus court en taille (par exemple, Maison (5 lettres) vs Profil (6 lettres)).

Nous utilisons `flexbox` pour distribuer les `.tab` uniformément à l'intérieur du conteneur. Hormis cela, je crois que le CSS est assez explicite.

Ensuite... le style des `.tab` :

```css
.tab {
    background-color: #ffffff;
    border-radius: 50px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 20px;
    margin: 0 10px;
    transition: background 0.4s linear;
}

.tab i {
    font-size: 1.2em;
}

.tab p {
    font-weight: bold;
    overflow: hidden;
    max-width: 0;
}

.tab.active p {
    margin-left: 10px;
    max-width: 200px;
    transition: max-width 0.4s linear;
}

.tab.active.purple {
    background-color: rgba(91, 55, 183, 0.2);
    color: rgba(91, 55, 183, 1);
}

.tab.active.pink {
    background-color: rgba(201, 55, 157, 0.2);
    color: rgba(201, 55, 157, 1);
}

.tab.active.yellow {
    background-color: rgba(230, 169, 25, 0.2);
    color: rgba(230, 169, 25, 1);
}

.tab.active.teal {
    background-color: rgba(28, 150, 162, 0.2);
    color: rgba(28, 150, 162, 1);
}
```

Quelques points à noter ici :

1. Afin d'avoir une transition fluide lorsque nous changeons l'onglet `.active`, nous définissons une propriété `transition: background` pour la classe `.tab`.
2. Par défaut, la balise `p` à l'intérieur du `.tab` a une `max-width` de `0` et sa propriété `overflow` définie sur `hidden`. Cela est dû au fait que nous voulons afficher le texte uniquement lorsque le `.tab` est actif.
3. Nous utilisons les classes de couleur personnalisées (`.purple`, `.pink`, etc.) pour avoir différentes couleurs dans les onglets.

Assurons-nous qu'il a également une bonne apparence sur mobile :

```css
@media (max-width: 450px) {
    .tab-nav-container {
        padding: 20px;
        width: 350px;
    }

    .tab {
        padding: 0 10px;
        margin: 0;
    }

    .tab i {
        font-size: 1em;
    }
}
```

Comme vous pouvez le voir, nous réduisons le `.tab-nav-container` lorsque la largeur maximale de la fenêtre est de `450px` et nous réduisons également le padding pour le rendre plus petit.

### Le JavaScript

À la fin, en JS, nous devons nous assurer que lorsque l'utilisateur clique sur un autre `.tab`, la classe `.active` est ajoutée à celui-ci et retirée de l'onglet `.active` précédent :

```javascript
// Obtenir tous les onglets
const tabs = document.querySelectorAll('.tab');

tabs.forEach(clickedTab => {
    // Ajouter un écouteur d'événement onClick sur chaque onglet
    clickedTab.addEventListener('click', () => {
        // Retirer la classe active de tous les onglets (cela agit comme une "réinitialisation" complète)
        tabs.forEach(tab => {
            tab.classList.remove('active');
        });

        // Ajouter la classe active sur l'onglet cliqué
        clickedTab.classList.add('active');
    });
});
```

### Conclusion

Ce type de navigation à barres d'onglets est principalement utilisé sur les appareils mobiles, donc si vous voulez le réutiliser pour une application mobile, assurez-vous de positionner le conteneur en bas de l'écran (avec `position: fixed`) et de recalculer la largeur pour remplir toute la largeur de l'écran.

Dans l'exemple Codepen, nous changeons également la couleur de fond du corps lorsque l'on clique sur un autre onglet. Cela est juste pour des raisons visuelles et n'est pas exactement lié au thème de codage de cette semaine. Mais si vous voulez voir comment j'ai fait cela, consultez le code JS dans le [pen](https://codepen.io/FlorinPop17/pen/qvyWxX) (juste 2 lignes de code supplémentaires).

### Plus d'exemples pour ce défi de codage

Dans un [précédent](https://www.florin-pop.com/blog/2017/09/responsive-animated-navigation-menu) article, j'ai démontré comment construire un menu de navigation responsive. Vous pouvez également le consulter si vous voulez construire quelque chose de similaire.

De plus, si vous ne l'avez pas encore fait, assurez-vous de lire les "règles" du [Défi de codage hebdomadaire](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) si vous voulez participer au défi ! Et pourquoi ne le feriez-vous pas ? C'est une excellente façon d'améliorer vos compétences en codage ! ?

Bon codage ! ?

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/03/tab-bar-navigation/)._