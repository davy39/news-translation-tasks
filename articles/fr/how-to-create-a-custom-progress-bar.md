---
title: Comment créer une barre de progression personnalisée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-13T04:02:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-custom-progress-bar
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/how-to-create-a-custom-progress-bar.png
tags:
- name: WeeklyCodingChallenge
  slug: weeklycodingchallenge
- name: coding challenge
  slug: coding-challenge
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: progress bar
  slug: progress-bar
seo_title: Comment créer une barre de progression personnalisée
seo_desc: 'By Florin Pop

  Originally published on www.florin-pop.com

  The theme for week #14 of the Weekly Coding Challenge is:

  Progress Bar

  A progress bar is used to show how far a user action is still in process until it''s
  completed. A good example is a downloa...'
---

Par Florin Pop

*Originalement publié sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/06/how-to-create-a-custom-progress-bar/)*

Le **thème** pour la semaine #14 du [Défi de codage hebdomadaire](https://florin-pop.com/blog/2019/03/weekly-coding-challenge/) est :

## Barre de progression

Une barre de progression est utilisée pour montrer à quel point une action de l'utilisateur est encore en cours jusqu'à ce qu'elle soit terminée. Un bon exemple est une barre de progression de téléchargement qui vous montre combien du fichier est déjà téléchargé (ou cela pourrait aussi être une barre de progression de téléversement si vous téléversez des fichiers ?).

Dans cet article, nous allons construire ce type de [Barre de progression](https://codepen.io/FlorinPop17/full/jjPWbv/) :

%[https://codepen.io/FlorinPop17/pen/jjPWbv/]

## Le HTML

Pour la structure HTML, nous avons besoin de deux choses :

1. un _conteneur_ qui affichera la longueur totale (100%) de la barre de progression - `.progress-bar`
2. l'élément de progression réel qui suivra essentiellement la progression actuelle (par exemple, 20%) - `.progress`

```html
<div class="progress-bar">
    <div data-size="20" class="progress"></div>
</div>
```

Comme vous pouvez le voir, la div `.progress` a un attribut `data-size`. Cela sera utilisé en **JavaScript** pour définir la `width` de la progression. Vous verrez dans un instant ce que je veux dire, mais d'abord, stylisons ces deux éléments. ?

## Le CSS

```css
.progress-bar {
    background-color: #fefefe;
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    margin: 15px;
    height: 30px;
    width: 500px;
    max-width: 100%;
}

.progress {
    background: #ad5389;
    background: -webkit-linear-gradient(to bottom, #3c1053, #ad5389);
    background: linear-gradient(to bottom, #3c1053, #ad5389);
    border-radius: 3px;
    height: 30px;
    width: 0;
    transition: width 0.5s ease-in;
}
```

Quelques points à noter concernant le CSS ci-dessus :

1. les deux éléments sont des rectangles qui ont la même hauteur (`30px`) et le même `border-radius`
2. initialement, la largeur de `.progress` est définie sur `0` et nous mettrons cela à jour dans le code **JavaScript** ci-dessous
3. également, `.progress` a un beau `linear-gradient` de [uiGradients](https://uigradients.com/)
4. la `transition` ajoutée à `.progress` est utilisée pour créer une belle animation lorsque la valeur de son attribut `data-size` est modifiée dynamiquement

## Le JavaScript

Pour cela, nous devons parcourir tous les éléments `.progress` (dans notre exemple, il n'y en a qu'un seul, mais vous pouvez en ajouter plusieurs dans une application) pour obtenir leur valeur `data-set` et la définir comme leur largeur. Nous utiliserons le pourcentage (`%`) dans ce cas.

```js
const progress_bars = document.querySelectorAll('.progress');

progress_bars.forEach(bar => {
    const { size } = bar.dataset;
    bar.style.width = `${size}%`;
});
```

Nous utilisons un peu de [Destructuration d'objet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

`const { size } = bar.dataset`

est la même chose que :

`const size = bar.dataset.size`

mais vous le saviez peut-être déjà ?.

## Conclusion

Il y a plusieurs choses que vous pourriez faire pour améliorer ce composant. Certaines d'entre elles sont :

1. Ajouter plusieurs variantes de couleur via différentes _classes_
2. Ajouter la valeur en pourcentage
3. Le faire animer dynamiquement en changeant la valeur de la taille.

J'espère que vous avez apprécié et assurez-vous de partager avec moi ce que vous créez !

Bon codage ! ?