---
title: Comment créer des animations CSS personnalisées avec des exemples
subtitle: ''
author: Eric Hu
co_authors: []
series: null
date: '2024-01-09T21:59:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-custom-css-animations
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/cover.png
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
seo_title: Comment créer des animations CSS personnalisées avec des exemples
seo_desc: 'Animations are a crucial component of modern web design. They enable you
  to create dynamic and engaging web elements that attract more customers and drive
  more sales.

  In this article, we will discuss how to create cool custom animations using CSS.

  Pr...'
---

Les animations sont un composant crucial de la conception web moderne. Elles vous permettent de créer des éléments web dynamiques et engageants qui attirent plus de clients et génèrent plus de ventes.

Dans cet article, nous allons discuter de la manière de créer des animations personnalisées cool en utilisant CSS.

## Prérequis

Avant de continuer avec cet article, assurez-vous d'avoir des connaissances de base en HTML et CSS. 

Je supposerai que vous êtes familier avec les [sélecteurs CSS](https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/), la définition de la [taille](https://www.w3schools.com/css/css_dimension.asp) et de la [couleur](https://www.w3schools.com/css/css_colors.asp) des éléments, le [positionnement des éléments](https://www.ericsdevblog.com/courses/html-css/4/), l'[ajustement de l'opacité](https://www.freecodecamp.org/news/css-opacity/), et la [transformation des éléments](https://www.freecodecamp.org/news/complete-guide-to-css-transform-functions-and-properties/).

## Comment créer votre première animation CSS

Commençons par préparer un élément HTML.

```html
<body>
  <div class="square"></div>
</body>

```

```css
.square {
  width: 100px;
  height: 100px;
  background-color: purple;

  /* Centrer l'élément */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

```

Les lignes 7 à 10 démontrent une méthode couramment utilisée pour [centrer un élément en utilisant CSS](https://www.ericsdevblog.com/posts/how-to-center-a-div-in-css/). Voici le résultat du code ci-dessus :

![square center](https://www.freecodecamp.org/news/content/images/2024/01/square-center.png)
_Carré centré_

Avant de commencer à créer l'animation, vous devez d'abord réfléchir à l'effet que vous souhaitez obtenir. 

Par exemple, pour ce tutoriel, je veux créer un effet de rebond pour le carré. Cela signifie que je dois créer une animation basée sur la propriété `top` afin que le carré puisse monter et descendre.

```css
@keyframes bounce {
  0% {
    top: 90%;
  }
  100% {
    top: 10%;
  }
}

```

Pour définir une animation, vous devez utiliser la règle `@keyframes`, qui vous permet de définir des images clés dans le processus d'animation. 

Les images clés sont définies avec des valeurs en pourcentage, commençant par `0%` et se terminant par `100%`. Par exemple, dans notre exemple, l'animation commencera par `top: 90%;`, et se terminera par `top: 10%;`, et après cela, elle reviendra à `50%`.

Et, bien sûr, vous devez lier l'animation `bounce` avec le carré (`animation-name`) et également indiquer au navigateur combien de temps vous souhaitez que cette animation dure (`animation-duration`). Voici comment faire :

```css
.square {
  . . .
  animation-name: bounce;
  animation-duration: 2s;
}

```

![square moves up](https://www.freecodecamp.org/news/content/images/2024/01/bounce-1.gif)
_Un carré qui monte_

## Comment ajouter plusieurs images clés

Mais comme vous pouvez le voir, le carré commence par le bas, monte en haut, et revient ensuite au centre. Ce n'est pas exactement un effet de rebond. Alors, comment faire pour que le carré redescende ?

Pour cela, vous pouvez configurer une troisième image clé comme ceci :

```css
@keyframes bounce {
  0% {
    top: 90%;
  }
  50% {
    top: 10%;
  }
  100% {
    top: 90%;
  }
}

```

De cette manière, le carré commencera par le bas (`top: 90%;`), montera en haut (`top: 10%;`), et redescendra (`top: 90%;`).

![square moves up and then down](https://www.freecodecamp.org/news/content/images/2024/01/bounce-2.gif)
_Le carré monte puis redescend_

## Comment créer une animation répétitive

Il y a un problème qui doit encore être résolu. L'animation ne se joue qu'une seule fois. En pratique, vous pourriez vouloir que votre animation se répète plusieurs fois pour créer l'effet que le carré rebondit réellement. 

Au lieu de créer plus d'images clés, ce qui n'est pas facile, vous pouvez définir une propriété `animation-iteration-count` et spécifier le nombre de fois que vous voulez que l'animation se répète.

```css
.square {
  . . .
  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: 5;
}

```

![repeat animation 5 times](https://www.freecodecamp.org/news/content/images/2024/01/bounce-3.gif)
_Le carré monte et descend cinq fois_

Et si vous voulez que l'animation dure indéfiniment, spécifiez simplement `infinite`.

```css
.square {
  . . .
  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

```

## Comment utiliser une fonction de timing pour une animation plus fluide

Enfin, l'effet de rebond a commencé à fonctionner, mais il y a encore place à l'amélioration. Le mouvement du carré semble un peu peu naturel. L'effet de rebond serait meilleur si vous pouviez lisser le mouvement.

Cela peut être réalisé avec une fonction de timing. Par défaut, le navigateur supposera une fonction de timing `linear`, ce qui signifie que l'animation aura une vitesse constante du début à la fin. Mais vous pouvez changer cela en utilisant la propriété `animation-timing-function`, comme ceci :

```css
.square {
  . . .
  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-timing-function: ease-in-out;
}

```

En spécifiant `ease-in-out`, vous dites au navigateur de commencer l'animation lentement et de la terminer progressivement. En conséquence, l'animation entière sera beaucoup plus fluide.

![ease in out](https://www.freecodecamp.org/news/content/images/2024/01/bounce-4.gif)
_`ease-in-out` rendant le mouvement du carré fluide_

### La courbe de Bézier cubique

La valeur `ease-in-out` représente en réalité une équation mathématique appelée [Cubic Bezier](https://www.w3schools.com/cssref/func_cubic-bezier.php). Je vous épargnerai les définitions mathématiques complexes, et vous devez seulement savoir que la fonction définit une courbe avec quatre points de contrôle. 

[cubic-bezier.com](https://cubic-bezier.com/) est un outil en ligne qui vous permet de personnaliser la courbe en déplaçant simplement les points de contrôle.

![cubic bezier](https://www.freecodecamp.org/news/content/images/2024/01/cubic-bezier.png)
_Une courbe de Bézier cubique_

Les points contrôlent la forme de la courbe, et la pente de la courbe contrôle ensuite la vitesse de l'animation. Par exemple, le graphique ci-dessus indique que l'animation commencera lentement, accélérera, puis se terminera en douceur.

```css
.square {
  . . .
  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-timing-function: cubic-bezier(0.17, 0.67, 0.8, 0.36);
}

```

Dans la plupart des cas, vous n'avez pas à définir une courbe de Bézier cubique personnalisée. Il existe plusieurs courbes prédéfinies qui devraient suffire pour la plupart des cas d'utilisation.

`ease` représente la courbe `cubic-bezier(0.25, 0.1, 0.25, 1)`. L'animation commencera par accélérer lentement puis décélérera pour s'arrêter.

![ease](https://www.freecodecamp.org/news/content/images/2024/01/ease.png)
_Courbe de Bézier cubique pour ease_

`ease-in` représente la courbe `cubic-bezier(0.42, 0, 1, 1)`. L'animation commencera en douceur puis s'arrêtera plutôt brusquement.

![ease in](https://www.freecodecamp.org/news/content/images/2024/01/ease-in.png)
_Courbe de Bézier cubique pour ease-in_

`ease-out` représente la courbe `cubic-bezier(0, 0, 0.58, 1)`. L'animation commencera brusquement puis ralentira pour s'arrêter en douceur.

![ease out](https://www.freecodecamp.org/news/content/images/2024/01/ease-out.png)
_Courbe de Bézier cubique pour ease-out_

`ease-in-out` représente la courbe `cubic-bezier(0.42, 0, 0.58, 1)`. L'animation sera fluide aux deux extrémités.

![ease in out](https://www.freecodecamp.org/news/content/images/2024/01/ease-in-out.png)
_Courbe de Bézier cubique pour ease-in-out_

### La fonction `steps()`

Outre la courbe fluide, vous pouvez également spécifier une fonction de pas. La fonction `steps()` prend deux arguments. Le premier spécifie le nombre de pas, et le second définit le point auquel le changement se produit dans le pas, soit au début soit à la fin.

```css
.square {
  . . .
  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-timing-function: steps(5, start);
}

```

Dans ce cas, l'animation sera divisée en cinq étapes, et pour chaque étape, le changement se produira au début de l'étape.

![5 steps](https://www.freecodecamp.org/news/content/images/2024/01/bounce-5.gif)
_Une démonstration de la fonction steps_

Il existe également deux raccourcis disponibles pour la fonction `steps()`. `step-start` correspond à `steps(1, start)`, et `step-end` correspond à `steps(1, end)`.

## Comment combiner plusieurs animations

Jusqu'à présent, nous avons couvert tous les fondamentaux que vous devez comprendre pour créer des animations CSS. Et maintenant, il est temps de devenir plus créatif.

Nos exemples précédents se sont tous concentrés sur le changement de la propriété `top` afin de créer l'effet de rebond. Vous pouvez, en fait, combiner plusieurs propriétés en une seule animation. Par exemple, vous pouvez créer un effet de pulsation en changeant la forme et l'opacité de l'élément ensemble.

```css
@keyframes pulse {
  0% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
    opacity: 0.7;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
}

```

```css
.ball {
  width: 100px;
  height: 100px;
  background-color: purple;
  border-radius: 50%;

  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  animation: pulse 2s ease-in-out infinite;
}

```

Notez également que les propriétés d'animation peuvent être combinées en un raccourci, `animation`.

![pulse](https://www.freecodecamp.org/news/content/images/2024/01/pulse.gif)
_L'animation d'effet de pulsation_

## Autres propriétés liées aux animations

Outre les propriétés d'animation que nous avons discutées jusqu'à présent, il existe certaines propriétés diverses dont nous devrions parler. Elles peuvent également être utiles parfois. 

Tout d'abord, il y a la propriété `animation-direction`, qui définit comment l'animation sera jouée. La propriété accepte quatre valeurs différentes :

* `normal` : L'animation est jouée vers l'avant.
* `reverse` : L'animation est jouée vers l'arrière.
* `alternate` : L'animation est jouée vers l'avant d'abord, puis vers l'arrière. Cela ne fonctionne que lorsque `animation-iteration-count` est supérieur à 1.
* `alternate-reverse` : L'animation est jouée vers l'arrière d'abord, puis vers l'avant.

Par défaut, l'animation commencera à jouer immédiatement après le chargement de la page. Mais vous pouvez changer cela avec la propriété `animation-delay`, qui spécifie combien de temps vous souhaitez attendre avant que l'animation ne commence.

Enfin, la propriété `animation-fill-mode` détermine comment l'élément sera affiché avant et après que l'animation soit jouée. Par défaut, l'élément ne conservera aucun style de l'animation. Après l'arrêt de l'animation, l'élément reviendra à la normale.

Lorsque `animation-fill-mode` est défini sur `forwards`, l'élément conservera les styles de la dernière image clé de l'animation après que l'animation soit jouée.

Lorsque défini sur `backwards`, l'élément prendra les styles de la première image clé de l'animation dès que l'animation est jouée.

Lorsque défini sur `both`, l'élément conservera les styles de la première image clé avant que l'animation ne commence (se comporte comme `backwards`), et il conservera également les styles de la dernière image clé après que l'animation soit terminée (comme `forwards`).

## Conclusion

Ce tutoriel a couvert tout ce que vous devez savoir pour commencer à créer des animations CSS en utilisant la règle `@keyframes`.

```css
@keyframes pulse {
  0% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
    opacity: 0.7;
  }
  100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
}

```

Nous avons également passé en revue plusieurs propriétés CSS liées aux animations :

* `animation-duration` : Définit la durée de l'animation.
* `animation-iteration-count` : Définit le nombre de fois que l'animation se répète.
* `animation-timing-function` : Spécifie la fonction de timing, qui contrôle la vitesse à laquelle l'animation est jouée.
* `animation-direction` : La direction dans laquelle l'animation est jouée.
* `animation-delay` : Le délai avant que l'animation ne commence.
* `animation-fill-mode` : Si les styles de l'animation doivent être conservés après sa fin.

Pour des lectures supplémentaires sur HTML et CSS, consultez cette série de cours -> [HTML & CSS: A Practical Guide](https://www.ericsdevblog.com/courses/html-css/).