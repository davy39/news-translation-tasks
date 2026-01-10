---
title: Une introduction aux animations Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T19:43:41.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-web-animations-86f45de2a871
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ez-Q3W-m0iDOFJyExQJMdw.jpeg
tags:
- name: animation
  slug: animation
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Une introduction aux animations Web
seo_desc: 'By CodeDraken

  In this introduction to web animations article, we will cover basic CSS animations
  using pseudo-classes, transitions, and transformations.

  If you’re unsure why you should use CSS animations then take a look at these articles.

  Some basic...'
---

Par CodeDraken

Dans cet article d'introduction aux animations Web, nous aborderons les animations CSS de base en utilisant les **pseudo-classes**, les **transitions** et les **transformations**.

Si vous n'êtes pas sûr de pourquoi vous devriez utiliser les animations CSS, jetez un œil à [ces](https://developers.google.com/web/fundamentals/design-and-ux/animations/css-vs-javascript) [articles](https://medium.com/bridge-collection/improve-the-payment-experience-with-animations-3d1b0a9b810e).

Un exemple de code basique (et très laid (pour l'instant)) pour cet article sera disponible sur CodePen :

### Déclenchement

Avant de plonger dans quelques animations, réfléchissons à la manière dont elles vont être activées. La plupart de nos animations ne s'exécuteront pas immédiatement lorsque la page se charge. Plus couramment, *elles seront déclenchées* par un changement de classe (via JavaScript) ou en utilisant des pseudo-classes.

#### Pseudo Foo

Voici quelques [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) qui sont le plus couramment utilisées pour les animations.

[**:hover**](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover)
La pseudo-classe hover est déclenchée lorsque vous *survolez la cible* avec la souris. Dans cet exemple, nous définissons le `<p>` pour qu'il change sa couleur en bleu lorsqu'il est survolé. Il retrouvera sa couleur d'origine après que la souris ne soit plus dessus.

```
<style> #hover-example:hover {  color: blue;  cursor: pointer; }</style>
```

```
<p id="hover-example">Exemple de survol</p>
```

[**:focus**](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus)

> « La pseudo-classe :focus CSS représente un élément (comme une entrée de formulaire) qui a reçu le focus. » — MDN

(um… n'est-ce pas comme utiliser un mot pour se définir lui-même ??)

Focus est principalement utilisé pour les entrées et les boutons lorsqu'ils sont sélectionnés/activés — c'est-à-dire, *lorsque vous cliquez sur une entrée ou que vous y accédez par tabulation*. Dans cet exemple, cliquer ou accéder par tabulation à l'entrée provoquera un changement de largeur et de couleur de fond. Cliquer en dehors de celle-ci la ramènera à sa taille (et couleur) d'origine.

```
<style> input:focus {  background-color: #f4f4f4;  width: 50vw; }</style>
```

```
<input type="text">
```

[**:active**](https://developer.mozilla.org/en-US/docs/Web/CSS/:active)
Active semble similaire à focus, mais il est généralement *déclenché pendant une fraction de seconde*. Le premier cas d'utilisation qui vient à l'esprit sont les ancres (liens). Dans cet exemple, nous faisons en sorte que tout élément avec la classe `activate` change pendant qu'il est cliqué (c'est-à-dire, pendant qu'il est actif).

```
<style> .activate:active {  background-color: orange; }</style>
```

```
<p class="activate">Cliquez sur moi !</p><div class="activate">Activez-moi !</div><button class="activate">Maintenez-moi !</button>
```

### [Transformations](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

> « La propriété CSS transform vous permet de faire pivoter, redimensionner, incliner ou translater un élément donné. » — MDN

Transform est l'endroit où vous faites passer vos animations CSS au niveau supérieur. Il existe 21 fonctions ou plus que vous pouvez utiliser avec transform, mais nous n'en couvrirons pas toutes dans cet article.

#### Translation (x, y)

Translater signifie que vous déplacez quelque chose. Dans l'exemple ci-dessous, nous déplaçons tout élément ayant la classe `translate` de `10rem` sur l'axe X et de `5rem` sur l'axe Y. (Si vous n'êtes pas familier avec rem, vous pouvez également utiliser des pixels.)

Il s'agit de la fonction raccourcie qui combine X et Y, mais vous pouvez utiliser `translateX` ou `translateY` si vous préférez.

```
<style> .translate {  transform: translate(10rem, 5rem) }</style>
```

#### Mise à l'échelle (x, y)

Similaire à `translate`, scale dispose également de `scaleX`, `scaleY` et d'une fonction raccourcie `scale`. Utilisez scale pour *changer la taille de quelque chose*. Dans l'exemple ci-dessous, les éléments avec la classe `scale` sont réduits à la moitié de leur taille.

```
<style> .scale {  transform: scale(0.5); }</style>
```

#### [Transform-origin](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin) (x, y, z)

Transform-origin est une propriété importante lors de la gestion des animations, en particulier des rotations. C'est un peu étrange et difficile à expliquer avec des mots, et je vous suggère fortement de consulter la documentation MDN pour celle-ci si vous n'êtes pas déjà familier avec le changement d'origines (comme dans Photoshop). La documentation le décrit le mieux :

> « L'origine de la transformation est le point autour duquel une transformation est appliquée » — MDN

Imaginez une roue :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ez-Q3W-m0iDOFJyExQJMdw.jpeg)
*grande roue de Unsplash*

Lorsque la roue tourne, elle pivote autour de ce point central. Mais imaginez maintenant que ce point central soit déplacé, disons, vers le coin supérieur gauche. Maintenant, la roue tourne autour de ce nouveau point, offrant ainsi une expérience très différente. Ce point central est similaire à l'origine. Voir le [CodePen](https://codepen.io/CodeDraken/pen/OwOLrW) pour un exemple interactif.

#### Rotation (angle)

Rotate fait exactement ce qu'il dit faire. Vous pouvez spécifier n'importe quel angle, négatif, positif, n'importe quel nombre et il le fera tourner autant. Il existe quelques valeurs différentes que vous pouvez utiliser (deg, rad, grad) — [voir plus de types de valeurs sur MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/angle).

### Rendre les choses fluides

En utilisant les [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions), nous pouvons lisser les choses et contrôler le flux de nos animations.

Les transitions sont comme des interpolations ou un *contrôle de vitesse* pour notre animation. Elles peuvent prendre 4 arguments, et je vais détailler chacun d'eux.

#### [transition-property](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-property)

La propriété de transition est *ce que vous animez*. Cela peut être la couleur, la taille, une transformation, etc. Vous pourriez également dire `all` pour tout transitionner, mais vous devriez éviter de le faire et être plus spécifique.

Il existe une [longue liste de propriétés](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties) que vous pouvez animer sur MDN. Vous devriez éviter d'animer quoi que ce soit qui n'est pas dans la liste.

`transition-property: all;`

#### [transition-duration](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-duration)

Il s'agit de *la durée pendant laquelle l'animation mettra pour se terminer*. Utilisez des secondes ou des millisecondes.

`transition-duration: 2s;`

#### [transition-timing-function](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-timing-function)

C'est là que cela devient plus complexe. La fonction de temporisation de transition est une *courbe d'accélération qui décrit comment l'animation se déroule*. Jetez un œil à [ces](http://cubic-bezier.com/#.17,.67,.83,.67) [sites](https://easings.net/) pour voir à quoi ressemble cette courbe et comment elle affecte l'animation.

Vous pouvez la faire démarrer en douceur puis terminer en douceur, démarrer lentement puis terminer rapidement, ou avoir un flux plus complexe avec des parties lentes et rapides. Il existe de nombreuses façons de faire évoluer votre animation.

Heureusement, il existe des valeurs prédéfinies que nous pouvons utiliser :

```
easeease-inease-outease-in-outlinearstep-startstep-end
```

Vous devrez jouer un peu avec elles pour trouver celle qui convient à votre animation.

Parfois, nous devrons créer les nôtres en utilisant `cubic-bezier` (ou [utiliser une bibliothèque](https://daneden.github.io/animate.css/)). Pour cela, je vous suggère de trouver un outil en ligne (voir les liens ci-dessus) ou d'utiliser les outils de développement de votre navigateur pour en créer un.

`transition-timing-function: cubic-bezier(.29, 1.01, 1, -0.68);`

#### [transition-delay](https://developer.mozilla.org/en-US/docs/Web/CSS/transition-delay)

Il s'agit peut-être de la valeur la plus simple. Transition-delay est le temps qu'il *attendra avant de commencer l'effet*. Utilisez des secondes ou des millisecondes.

`transition-delay: 500ms;`

#### [Transition](https://developer.mozilla.org/en-US/docs/Web/CSS/transition) (propriété, durée, temporisation, délai)

Vous l'avez deviné, il s'agit du *raccourci* pour combiner toutes les fonctions ci-dessus.

Voici à quoi cela ressemble avec une transition :

`transition: background 1s ease-in-out 0.5s;`

Pour plusieurs, vous devez les ajouter à la même transition séparées par des virgules.

```
transition: background 1s ease-in-out 0.5s,width 2s ease-in,height 1.5s;
```

### En conclusion

C'est tout ce dont vous avez besoin pour commencer à créer des sites Web interactifs. Allez pratiquer ce que vous avez appris, et une fois que vous aurez maîtrisé les sujets abordés ici, vous pourrez passer à des animations plus avancées.

Dans le prochain article (ou deux), je parlerai des images clés, des transformations 3D, des performances, des animations JavaScript, et plus encore.

Merci d'avoir lu ! Si vous avez des questions, des commentaires ou des critiques, veuillez laisser un commentaire ci-dessous et je répondrai dès que possible.