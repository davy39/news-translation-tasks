---
title: CSS display:none et visibility:hidden – Quelle est la différence ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-15T23:13:53.000Z'
originalURL: https://freecodecamp.org/news/css-display-none-and-visibility-hidden-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/11.-display-visibility-2.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: CSS display:none et visibility:hidden – Quelle est la différence ?
seo_desc: 'By Dillion Megida

  display:none and visibility:hidden are two style declarations you can use to hide
  elements on the screen with CSS. But what are the differences between them?

  When building applications, there are times that you want to hide elements...'
---

Par Dillion Megida

`display:none` et `visibility:hidden` sont deux déclarations de style que vous pouvez utiliser pour masquer des éléments à l'écran avec CSS. Mais quelles sont les différences entre eux ?

Lors de la création d'applications, il arrive que vous souhaitiez masquer des éléments visuellement (sans les supprimer du DOM, juste de l'écran). Vous pouvez le faire de différentes manières.

Deux approches courantes incluent l'utilisation de la propriété `display` avec une valeur **none** ou de la propriété `visibility` avec une valeur **hidden**.

Bien que les deux approches masquent l'élément visuellement, elles font en sorte que l'élément se comporte de manière différente. Je vais expliquer ces différences dans cet article.

Voici [la version vidéo](https://youtu.be/nMq3U65wAdQ) de cet article si vous êtes intéressé.

Voici l'exemple que j'utiliserai pour expliquer comment tout cela fonctionne :

Le HTML :

```html
<div class="container">
  <div class="block1"></div>
  <div class="block2"></div>
  <div class="block3"></div>
</div>
```

Et le CSS :

```css
.container {
  padding: 20px;
  width: max-content;
  display: flex;
  border: 1px solid black;
}

.block1,
.block2,
.block3 {
  height: 40px;
  width: 120px;
}

.block1 {
  background-color: rgb(224, 110, 49);
  margin-right: 20px;
}

.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
}

.block3 {
  background-color: rgb(12, 154, 142);
}
```

Nous avons une `div` avec une classe **container**. Cette `div` a trois enfants `div` avec des classes **block1**, **block2** et **block3**, respectivement. Nous avons spécifié quelques styles pour les `div`. Le premier enfant `div` est orange, le second est `blue`, et le troisième est `teal`.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-77.png)

## Comment utiliser `display: none` en CSS

La propriété `display` définit comment un élément est affiché (en **inline** ou **block**) et détermine également la disposition des enfants d'un élément (en **flex**, **grid**, etc.).

Avec une valeur **none** pour cette propriété, l'affichage de l'élément est désactivé. Cela signifie que l'élément – ainsi que ses enfants – ne sera pas affiché. Le document est rendu sans l'élément **comme s'il n'existait pas**.

Voyons maintenant comment fonctionne `display: none`. Voici un exemple avec ce style appliqué à l'élément **.block2** :

```css
.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  display: none;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-78.png)

Comme vous pouvez le voir ici, l'élément **.container** a réduit en largeur. C'est comme si l'élément **.block2** n'existait pas. Parce que nous avons utilisé `display:none` sur cet élément, il n'est pas rendu dans le document. Ainsi, son espace à l'écran devient vacant pour que d'autres éléments l'occupent.

Nous pouvons également tester cela en ajoutant `display:none` à l'élément **.block1** :

```css
.block1 {
  background-color: rgb(224, 110, 49);
  margin-right: 20px;
  display: none;
}

.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  display: none;
}
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-79.png)

Ici, vous voyez que **.block1** et **.block2** ne sont pas rendus, donc leurs espaces sont occupés.

## Comment utiliser `visibility: hidden` en CSS

La propriété `visibility`, comme son nom l'indique, spécifie si un élément est visible ou non. Cependant, cette propriété n'affecte pas la disposition de l'élément. C'est la principale différence par rapport à la propriété `layout`.

Avec une valeur **hidden** pour cette propriété, l'élément auquel elle est appliquée devient "invisible". L'espace requis par le modèle de boîte de l'élément reste, mais l'élément lui-même est masqué.

Voyons comment cette propriété s'applique à notre exemple ci-dessus. Voici le résultat de ce style appliqué à l'élément **.block2** :

```css
.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  visibility: hidden;
}
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-80.png)

Comme vous le remarquerez ici, contrairement à `display: none`, l'élément **.block2** est invisible, mais sa disposition reste intacte. En fait, la `margin-right` sur cet élément est toujours présente. Seul l'élément lui-même est masqué.

Ajoutons également ce style à **.block1** pour voir le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-81.png)

Maintenant, les deux éléments sont invisibles, mais ils sont toujours rendus dans le document, donc leur espace n'est pas vacant.

La prochaine chose à laquelle vous pourriez penser est : "quelle est la différence entre `visibility: hidden` et `opacity: 0` ?"

## `visibility: hidden` vs `opacity: 0`

Les deux styles semblent très similaires. Je peux vous le montrer en remplaçant `visibility:hidden` par `opacity:0` dans nos exemples ci-dessus :

```css
.block1 {
  background-color: rgb(224, 110, 49);
  margin-right: 20px;
  opacity: 0;
}

.block2 {
  background-color: rgb(77, 77, 234);
  margin-right: 20px;
  opacity: 0;
}
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-82.png)

Vous pouvez voir qu'il n'y a pas de différence visuelle entre ce résultat et le précédent. Mais il y a une différence dans le comportement des éléments.

Les éléments avec `visibility: hidden` sont **non interactifs**. Je ne sais pas si c'est le meilleur mot pour cela 😂 mais ce que je veux dire, c'est que les utilisateurs ne peuvent pas interagir (par exemple, en cliquant) avec de tels éléments. C'est parce que ces éléments sont effectivement invisibles.

Les éléments avec `opacity: 0`, en revanche, sont **interactifs** car ils sont en fait visibles, juste très transparents. La propriété `opacity` ne spécifie pas la visibilité d'un élément – elle ne spécifie que la transparence.

Nous pouvons vérifier cette différence avec un exemple. Supposons que l'élément **.block2** avait un attribut `onclick` comme ceci :

```html
<div class="block2" onclick="alert('hello')"></div>
```

Si vous utilisez `visibility:hidden` sur cet élément, cliquer sur l'espace où se trouve l'élément ne déclenchera rien. Mais si vous utilisez `opacity:0` sur cet élément, cliquer sur cet espace déclenchera la fenêtre contextuelle d'alerte affichant le texte "hello". Vous pouvez tester cela sur votre navigateur pour voir cela en direct.

## Cas d'utilisation pour `display:none` et `visibility:hidden`

Ces déclarations de style peuvent servir différents objectifs selon ce que vous souhaitez réaliser.

Dans mon expérience, j'utilise `display:none` lorsque je veux masquer quelque chose. Pensez à masquer une fenêtre contextuelle, un élément de liste de tâches dans l'interface utilisateur qui a été coché, ou la barre latérale dans une page.

Utiliser `visibility:hidden` pour ces éléments fait en sorte que leur espace soit conservé, et cela pourrait rendre une page étrange lorsqu'il y a un espace vide.

Les seules fois où j'utilise `visibility:hidden`, c'est lorsque je veux afficher une animation pendant que je "masque" ou "affiche" un élément. La propriété `display` n'anime pas entre les valeurs, mais la propriété `visibility` peut le faire. J'utilise `visibility` en combinaison avec `opacity` pour de telles animations de fondu en entrée et en sortie.

## Conclusion

En résumé, `display:none`, `visibility:hidden` et `opacity:0` peuvent être utilisés pour masquer des éléments visuellement, mais :

* `display:none` désactive la disposition des éléments, donc ils ne sont pas rendus
* `visibility:hidden` masque les éléments sans changer leur disposition
* `opacity:0` rend les éléments très transparents, mais les utilisateurs peuvent toujours interagir avec eux.

Si vous avez aimé cet article, veuillez le partager avec d'autres pour apprendre 😇