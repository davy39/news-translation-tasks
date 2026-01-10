---
title: Comment créer un Kit UI de Boutons
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T17:27:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-buttons-ui-kit-fdd354ee0815
coverImage: https://cdn-media-1.freecodecamp.org/images/0*eUqmaII3aMOcV9hw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
seo_title: Comment créer un Kit UI de Boutons
seo_desc: 'By Florin Pop

  The theme for week #6 of the Weekly Coding Challenge is:

  Buttons

  “A button? ?” you might ask… Yes! A button! ?

  “But why?”

  Because a button is one of the building blocks of any website/web application. Whether
  you are on Facebook or Twit...'
---

Par Florin Pop

Le **thème** pour la semaine #6 du [Défi de Codage Hebdomadaire](https://www.florin-pop.com/blog/2019/03/weekly-coding-challenge/) est :

### Boutons

« Un bouton ? ? » pourriez-vous demander… Oui ! Un bouton ! ?

« Mais pourquoi ? »

Parce qu'un bouton est l'un des éléments de base de tout site web ou application web. Que vous soyez sur Facebook, Twitter ou Google, etc., vous trouverez toujours un bouton qui vous permet d'interagir avec l'application d'une manière ou d'une autre. Cette semaine, nous allons donc créer des boutons — beaucoup de boutons !

Si vous souhaitez participer au Défi, n'hésitez pas à créer tout type de boutons : des boutons **3D**, des boutons avec **effet de vague**, des boutons **animés**, etc. — le ciel est la limite ?. **Soyez créatif !** Vous savez à quel point j'apprécie la créativité ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*2aQjTjjd0_RMJpFR.gif)

Dans cet article, nous allons créer plusieurs boutons et les regrouper dans un [Kit UI de Boutons](https://codepen.io/FlorinPop17/full/MRbOMJ) :

Avant de passer à la partie implémentation, examinons les différents états dans lesquels un bouton peut se trouver :

1. État **par défaut**
2. État **survol** — lorsque la souris est au-dessus du bouton
3. État **actif** — lorsque le bouton est pressé
4. État **focus** — lorsque le bouton est mis en évidence. Autorisé sur les éléments qui acceptent les événements clavier. Cela est utilisé pour guider les utilisateurs qui n'utilisent que le clavier lors de leur navigation dans l'application.
5. État **désactivé**

Nous devons styliser les boutons pour couvrir tous ces états.

De plus, nous aurons trois types de boutons différents : `primary`, `secondary` et `tertiary`, ainsi que deux tailles supplémentaires : `large` et `small`.

### Le HTML

```html
<div>
    <h4>Primary</h4>
    <button class="btn btn-primary">Default</button>
    <button class="btn btn-primary btn-hover">Hover</button>
    <button class="btn btn-primary" disabled>Disabled</button>
    <button class="btn btn-primary btn-large">Large</button>
    <button class="btn btn-primary btn-small">Small</button>

    <h4>Secondary</h4>
    <button class="btn btn-secondary">Default</button>
    <button class="btn btn-secondary btn-hover">Hover</button>
    <button class="btn btn-secondary" disabled>Disabled</button>
    <button class="btn btn-secondary btn-large">Large</button>
    <button class="btn btn-secondary btn-small">Small</button>

    <h4>Tertiary</h4>
    <button class="btn btn-tertiary">Default</button>
    <button class="btn btn-tertiary btn-hover">Hover</button>
    <button class="btn btn-tertiary" disabled>Disabled</button>
    <button class="btn btn-tertiary btn-large">Large</button>
    <button class="btn btn-tertiary btn-small">Small</button>
</div>
```

Nous utilisons des classes pour différencier les différents types de boutons.

### Le CSS

`.btn` est la classe principale utilisée par tous nos boutons :

```css
.btn {
    border-radius: 2px;
    border: 1px solid;
    color: #ffffff;
    cursor: pointer;
    font-family: 'Open Sans', sans-serif;
    font-size: 14px;
    padding: 8px 24px;
}
```

☝️ Un peu de style général pour le rendre plus beau que la version par défaut. ?

Ensuite, nous avons les différents états :

```css
.btn-hover,
.btn:hover {
    opacity: 0.9;
}

.btn:disabled {
    background-color: transparent;
    cursor: not-allowed;
    opacity: 0.7;
}

.btn:active {
    opacity: 1;
}

.btn:focus {
    outline: 0;
}
```

Pour avoir une différence entre les états, nous pouvons jouer avec la propriété `opacity`.

Initialement, le bouton a une `opacity: 1` et nous réduisons légèrement cette `opacity` lorsque nous survolons le bouton, puis un peu plus lorsque le bouton est `disabled`. Lorsque nous cliquons sur le bouton, nous rétablissons l'opacité à 1 pour un bel effet.

Pour l'état `focus`, nous supprimons la propriété `outline` par défaut et nous ajoutons une propriété `box-shadow` à la place, mais nous le ferons séparément pour chaque type de bouton car la couleur change en fonction de la classe (voir ci-dessous).

Les couleurs individuelles sont définies pour les classes `.btn-primary`, `.btn-secondary` et `.btn-tertiary` :

```css
.btn-primary {
    border-color: var(--primary-color);
    background-color: var(--primary-color);
}

.btn-primary:disabled {
    color: var(--primary-color);
}

.btn-primary:focus {
    box-shadow: 0 0 5px var(--primary-color);
}

.btn-secondary {
    border-color: var(--secondary-color);
    background-color: var(--secondary-color);
}

.btn-secondary:disabled {
    color: var(--secondary-color);
}

.btn-secondary:focus {
    box-shadow: 0 0 5px var(--secondary-color);
}

.btn-tertiary {
    border-color: var(--tertiary-color);
    background-color: var(--tertiary-color);
}

.btn-tertiary:disabled {
    color: var(--tertiary-color);
}

.btn-tertiary:focus {
    box-shadow: 0 0 5px var(--tertiary-color);
}
```

Comme vous pouvez le voir, nous utilisons la méthode des [variables CSS](https://www.w3schools.com/css/css3_variables.asp) pour définir la même couleur sur différentes propriétés. Mais pour que cela fonctionne, nous devons déclarer les variables de couleur sur `:root` comme suit :

```css
:root {
    --primary-color: #3457dc;
    --secondary-color: #ea4d67;
    --tertiary-color: #ea674d;
}
```

Notez qu'il est bon de déclarer `:root` en haut du fichier CSS.

Enfin, ajoutons les deux tailles supplémentaires, les classes `.btn-large` et `.btn-small` :

```css
.btn-large {
    font-size: 16px;
    padding: 12px 36px;
}

.btn-small {
    font-size: 12px;
    padding: 4px 12px;
}
```

### Conclusion

Vous voyez comme il est facile de créer un _Kit UI de Boutons_ ? ?

En tant que **fonctionnalités bonus**, vous pouvez ajouter un `effet de vague` aux boutons via **JavaScript**. Je l'ai fait dans un article précédent — vous pouvez le consulter en cliquant [ici](https://www.florin-pop.com/blog/2017/09/button-ripple-effect) !

J'espère que vous avez aimé ce défi et j'ai hâte de voir ce que vous allez créer !

Bon codage ! ?

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/04/buttons-ui-kit/)._