---
title: Les transitions CSS expliquées
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2017-12-22T02:36:13.000Z'
originalURL: https://freecodecamp.org/news/css-transitions-explained-d67ab9a02049
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dtrF5zNPuHvPlUSY.png
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: transitions
  slug: transitions
seo_title: Les transitions CSS expliquées
seo_desc: 'The simplest (and most straightforward) way to animate your components
  is through CSS Transitions. In this article, you’ll learn how CSS Transitions work,
  and how to make animations with it.

  A transition occurs when a CSS property changes from one va...'
---

La manière la plus simple (et la plus directe) d'animer vos composants est d'utiliser les transitions CSS. Dans cet article, vous apprendrez comment fonctionnent les transitions CSS et comment créer des animations avec elles.

Une transition se produit lorsqu'une propriété CSS passe d'une valeur à une autre sur une certaine durée.

Vous pouvez créer des transitions CSS avec la propriété `transition` :

```css
.selector { 
  transition: property duration transition-timing-function delay; 
}
```

La propriété `transition` est un raccourci pour quatre propriétés CSS : `transition-property`, `transition-duration`, `transition-timing-function` et `transition-delay`.

```css
.selector { 
  transition-property: property; 
  transition-duration: duration; 
  transition-timing-function: timing-function; 
  transition-delay: delay 
      
  /* La propriété transition est le raccourci pour les quatre propriétés ci-dessus */ 
  transition: property duration timing-function delay; 
}
```

`transition-property` fait référence à la propriété CSS que vous souhaitez transitionner. Elle est requise dans le raccourci `transition`.

`transition-duration` fait référence à la durée de la transition. Combien de temps voulez-vous que la transition dure ? Cette valeur s'écrit en secondes avec le suffixe `s` (comme `3s`). Elle est également requise dans le raccourci `transition`.

`transition-timing-function` fait référence à la manière dont la transition se produit. Vous en apprendrez plus à ce sujet plus tard.

`transition-delay` fait référence au temps que vous souhaitez attendre avant de commencer la transition. Cette valeur s'écrit en secondes avec le suffixe `s` (comme `3s`). `transition-delay` est optionnel dans le raccourci `transition`.

### Déclenchement des transitions

Vous pouvez déclencher des transitions CSS directement avec des pseudo-classes comme `:hover` (s'active lorsque la souris passe sur un élément), `:focus` (s'active lorsqu'un utilisateur accède à un élément via la touche tabulation, ou lorsqu'il clique dans un champ de saisie), ou `:active` (s'active lorsque l'utilisateur clique sur l'élément).

```css
/* création de transitions directement en CSS */ 
.button { 
  background-color: #33ae74; 
  transition: background-color 0.5s ease-out; 
} 

.button:hover { 
  background-color: #1ce; 
}
```

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="CSS Transition" src="//codepen.io/zellwk/embed/Qqzzxd/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href='https://codepen.io/zellwk/pen/Qqzzxd/'>CSS Transition</a> par Zell Liew
  (<a href='https://codepen.io/zellwk'>@zellwk</a>) sur <a href='https://codepen.io'>CodePen</a>.
</iframe>

Vous pouvez également déclencher des transitions CSS via JavaScript en ajoutant ou en supprimant une classe.

```css
/* CSS */
.button { 
  background-color: #33ae74; 
  transition: background-color 0.5s ease-out; 
} 

.button.is-active { color: #1ce; }

// JavaScript
const button = document.querySelector('.button') button.addEventListener('click', _ => button.classList.toggle('is-active'))
```

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="CSS Transition with JavaScript" src="//codepen.io/zellwk/embed/GMPPBg/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href='https://codepen.io/zellwk/pen/GMPPBg/'>CSS Transition with JavaScript</a> par Zell Liew
  (<a href='https://codepen.io/zellwk'>@zellwk</a>) sur <a href='https://codepen.io'>CodePen</a>.
</iframe>

### Comprendre transition-timing-function

La propriété `transition-timing-function` régit la manière dont une transition se produit. Toutes les transitions ont une valeur par défaut de `linear`, ce qui signifie que la propriété change de manière uniforme jusqu'à la fin de la transition.

```css
.selector { 
  transition: transform 1s linear; 
  
  /* OU */ 
  transition-property: transform; 
  transition-duration: 1s; 
  transition-timing-function: linear; 
}
```

Le fait est que peu de choses se déplacent de manière linéaire dans la vie. Ce n'est pas ainsi que les objets réels bougent. Parfois, nous accélérons ; parfois, nous ralentissons. La propriété `transition-timing-function` vous permet de capturer tout cela.

Imaginez-vous en train de lancer une balle de tennis dans un champ libre. La balle quitte votre main avec une vitesse maximale. À mesure qu'elle avance, elle perd de l'énergie, elle ralentit et finit par s'arrêter. C'est ce qu'on appelle `ease-out`. Il existe une fonction de timing pour cela.

```css
.selector { 
  transition-timing-function: ease-out; 
}
```

Maintenant, imaginez que vous êtes dans une voiture. Elle est à l'arrêt. Lorsque vous démarrez la voiture, elle accélère et se dirige vers sa vitesse de pointe. C'est ce qu'on appelle `ease-in`. Il existe également une fonction de timing pour cela.

```css
.selector { 
  transition-timing-function: ease-in; 
}
```

Puisque vous avez `ease-in` et `ease-out`, il existe également une fonction de timing qui combine les deux, `ease-in-out`. (Je déconseille d'utiliser `ease-in-out` dans vos transitions à moins qu'elles ne durent plus d'une seconde. Rien ne s'accélère et ne se ralentit en moins d'une seconde. Cela semble tout simplement bizarre.)

```css
.selector { 
  transition-timing-function: ease-in-out; 
}
```

Consultez ce Pen pour une démonstration des fonctions de timing que vous avez apprises jusqu'à présent :

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="CSS Transition Timing Functions (no cubic)" src="//codepen.io/zellwk/embed/Oxrqpo/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href='https://codepen.io/zellwk/pen/Oxrqpo/'>CSS Transition Timing Functions (no cubic)</a> par Zell Liew
  (<a href='https://codepen.io/zellwk'>@zellwk</a>) sur <a href='https://codepen.io'>CodePen</a>.
</iframe>

Enfin, si aucun des choix ci-dessus ne vous convient, vous pouvez créer votre propre fonction de timing avec `cubic-bezier`.

### Créer votre propre fonction de timing avec cubic-bezier

Une courbe de Bézier cubique (`cubic-bezier`) est un ensemble de quatre valeurs qui déterminent votre `transition-timing-function`. Cela ressemble à ceci :

```css
.selector { 
  transition-timing-function: cubic-bezier(x1, y1, x2, y2); 
}
```

Ne vous inquiétez pas pour les valeurs `x1`, `y1`, `x2` et `y2`. Vous ne créerez jamais de courbes cubic-bezier en écrivant les chiffres vous-même (à moins que vous ne sachiez déjà ce qu'ils signifient et que vous ajustiez votre fonction de timing pour atteindre la perfection).

Vous pouvez compter sur les outils de développement de Chrome et Firefox pour vous aider à créer vos courbes. Pour les utiliser, ajoutez une `transition-timing-function` à un élément, puis ouvrez les outils de développement et cliquez sur la fonction de timing.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dtrF5zNPuHvPlUSY.png)

Voir le Pen [CSS Transition Timing Functions](https://codepen.io/zellwk/pen/gGZqNo/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

Approfondir la création de vos propres courbes de Bézier pour vos animations dépasse le cadre de l'article d'aujourd'hui. Si cela vous intéresse, vous pouvez trouver plus d'informations sur les courbes cubic-bezier dans « [Understanding CSS Timing Functions](https://www.smashingmagazine.com/2014/04/understanding-css-timing-functions/) » par [Stephen Greig](https://twitter.com/Stephen_Greig).

### Transitionner deux propriétés ou plus

Vous pouvez transitionner deux (ou plus) propriétés CSS en les séparant par une virgule dans votre propriété `transition` ou `transition-property`.

Vous pouvez faire de même avec la durée, les fonctions de timing et les délais. Si les valeurs sont les mêmes, vous n'avez besoin d'en spécifier qu'une seule.

```css
.selector { 
  transition: background-color 1s ease-out, color 1s ease-out; 
  
  /* OU */  
  transition-property: background, color; 
  transition-duration: 1s; 
  transition-timing-function: ease-out; 
}
```

Vous pourriez être tenté de transitionner chaque propriété CSS avec `all`. Ne faites jamais cela. C'est mauvais pour les performances. Spécifiez toujours la propriété que vous essayez de transitionner.

```css
/* NE FAITES JAMAIS CELA */ 
.selector { 
  transition-property: all;
} 

/* FAITES TOUJOURS CECI */ 
.selector { 
  transition-property: background-color, color, transform; 
}
```

### Transition d'entrée vs transition de sortie

Parfois, vous voulez que les propriétés transitent différemment à l'entrée et à la sortie. Vous voulez que la durée, la fonction de timing ou le délai soient différents.

Pour ce faire, vous écrivez un autre ensemble de propriétés `transition-`.

```css
.button { 
  background-color: #33ae74; 
  transition: background-color 0.5s ease-out; 
} 

.button:hover { 
  background-color: #1ce; 
  transition-duration: 2s; 
}
```

Lorsque vous écrivez des propriétés de transition dans la (pseudo) classe de déclenchement, celles-ci écrasent les propriétés de transition d'origine que vous avez définies dans la classe de base.

Ainsi, dans l'exemple ci-dessus, lorsque vous survolez le bouton, la couleur d'arrière-plan met 2 secondes pour passer de `#33ae74` à `#1ce`.

Lorsque vous quittez le survol du bouton, la couleur d'arrière-plan ne met que 0,5s pour revenir à `#1ce` car la `transition-duration` de 2s n'existe plus.

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="Transition CSS (vitesses de transition différentes à l'entrée et à la sortie)" src="//codepen.io/zellwk/embed/GOLLyR/?height=265&theme-id=0&default-tab=css,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href='https://codepen.io/zellwk/pen/GOLLyR/'>CSS Transition (vitesses de transition différentes à l'entrée et à la sortie)</a> par Zell Liew
  (<a href='https://codepen.io/zellwk'>@zellwk</a>) sur <a href='https://codepen.io'>CodePen</a>.
</iframe>

### Conclusion

Les transitions CSS sont le moyen le plus simple de réaliser des animations. Vous pouvez créer des transitions soit avec le raccourci `transition`, soit avec les propriétés `transition-` individuelles.

Pour créer une transition, vous écrasez une propriété dans une classe (ou pseudo-classe), et vous spécifiez la propriété à animer dans `transition` ou `transition-property`.

N'oubliez pas de modifier votre `transition-timing-function` pour que votre animation paraisse plus réelle !

Si vous avez aimé cet article, vous adorerez [Learn JavaScript](https://zellwk.com/learnjs/) — un cours qui vous aide à apprendre à **construire de réels composants de zéro** avec JavaScript.

(Oh, au fait, si vous avez aimé cet article, j'apprécierais que vous puissiez le [partager](http://twitter.com/share?text=CSS%20Transitions%20explained%20by%20%40zellwk%20?%20&url=https://zellwk.com/blog/css-transitions/&hashtags=). )

_Publié initialement sur [zellwk.com](https://zellwk.com/blog/css-transitions/)._