---
title: CSS Pseudo-Classes – Comment la pseudo-classe :is fonctionne avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-02T22:04:37.000Z'
originalURL: https://freecodecamp.org/news/css-is-pseudo-class-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/1.-is.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: CSS Pseudo-Classes – Comment la pseudo-classe :is fonctionne avec des exemples
seo_desc: 'By Dillion Megida

  Pseudo-classes allow you to style an element in a specific state. There are many
  supported classes for states in CSS. In this article, I''ll explain how the :is
  pseudo-class works.

  This article is the first in a new series I''ll be wo...'
---

Par Dillion Megida

Les pseudo-classes vous permettent de styliser un élément dans un état spécifique. Il existe de nombreuses classes supportées pour les états en CSS. Dans cet article, je vais expliquer comment la pseudo-classe `:is` fonctionne.

Cet article est le premier d'une nouvelle série sur laquelle je travaillerai au cours des prochaines semaines et mois : **CSS Pseudo Classes Explained**. J'ai l'intention d'expliquer autant de pseudo-classes que possible, chaque article autonome traitant d'une pseudo-classe particulière.

J'ai [une playlist YouTube CSS Pseudo Classes Explained](https://www.youtube.com/playlist?list=PLLdz3KlabJv2sYL287Q_8lpy_jOgwQjN2) que vous pouvez consulter également.

Note : Les pseudo-classes sont différentes des pseudo-éléments. Les pseudo-classes s'appliquent à différents **états** des éléments, tandis que les pseudo-éléments s'appliquent à différentes **parties** d'un élément. 

Vous pouvez en apprendre davantage [sur les différences ici](https://dillionmegida.com/p/pseudo-elements-vs-pseudo-classes-in-css/).

Dans ce tutoriel, vous apprendrez toutes les bases de la pseudo-classe `:is`.

## Comment la pseudo-classe `:is` fonctionne

La pseudo-classe `:is` prend une liste d'arguments de sélecteurs et correspond à tous les éléments qui s'appliquent à n'importe quel sélecteur dans la liste. Voici la syntaxe :

```css
:is(selector1, selector2, selector3) {
  /* styles */
}
```

Vous spécifiez des sélecteurs de n'importe quel type, et tout élément dans le DOM qui "est" une correspondance pour l'un des sélecteurs sera sélectionné et stylisé.

J'ai un article sur [les types de sélecteurs en CSS](https://www.freecodecamp.org/news/how-to-select-elements-to-style-in-css/) que vous pouvez consulter pour voir les différents sélecteurs que vous pouvez utiliser avec la pseudo-classe `:is`. 

Le seul type de sélecteur que vous ne pouvez pas utiliser avec la classe est un **pseudo-élément**.

De plus, parce que j'aime avoir des versions vidéo de mes articles (pour ceux qui préfèrent/aimeraient regarder des vidéos), vous pouvez consulter la [version vidéo de la pseudo-classe :is sur YouTube](https://youtu.be/sDa4zDHv41Y).

Regardons quelques exemples de cette pseudo-classe.

### Exemples de la pseudo-classe `:is`

Regardez ce code CSS :

```css
:is(.selector1, #selector2, selector3, :selector4, [selector5]) {
  /* styles */
}
```

Dans la liste des arguments, nous avons les sélecteurs **selector1** `class`, **selector2** `id`, **selector3** `tag`, **selector4** `pseudo-class` et **selector5** `attribute`. Tous les éléments dans le DOM qui correspondent à au moins l'un de ces sélecteurs seront sélectionnés pour le style.

Regardons un exemple pratique.


```html
<section>
  <p>Paragraphe de section</p>
</section>

<div>
  <p>Paragraphe de div</p>
</div>

<article>
  <p>Paragraphe d'article</p>
</article>

<span>
  <p>Paragraphe de span</p>
</span>
```

Ici, nous avons un élément `section`, `div`, `article` et `span`. Chacun de ces éléments a un enfant `p`. Si nous voulions styliser tous les enfants `p` de ces éléments, nous pouvons avoir la déclaration de style suivante :

```css
section p,
div p,
article p,
span p {
  text-decoration: underline;
  color: red;
}
```

Résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-107.png)

Mais nous pouvons améliorer le CSS avec la pseudo-classe `:is`. Voici comment :

```css
:is(section, div, article, span) p {
  text-decoration: underline;
  color: red;
}
```

Cela nous donne le même résultat que ci-dessus. Mais qu'est-ce qui est différent ?

Dans la pseudo-classe `:is`, nous passons quatre sélecteurs : les noms de balises `selection`, `div`, `article` et `span`. En utilisant le [combinateur de descendants](https://www.freecodecamp.org/news/css-combinators-to-select-elements#1howtousethedescendantcombinator) (un caractère espace), nous sélectionnons les éléments de balise `p` qui sont des descendants de l'un des sélecteurs de la liste. Ce qui signifie que cette sélection sélectionnera :

* les descendants `p` de `section`
* les descendants `p` de `div`
* les descendants `p` de `article` et
* les descendants `p` de `span`

En utilisant la pseudo-classe `:is`, nous avons raccourci les sélecteurs d'éléments.

Regardons un autre exemple.

```html
<button class="active">Cliquez-moi</button>
```

Pour ce bouton, disons que vous voulez appliquer le même style lorsqu'il est en état de `hover` ou de `focus`, ou lorsqu'il a une classe `active`. Normalement, vous pouvez avoir le code suivant :

```css
button:hover,
button:focus,
button.active {
  background-color: black;
  color: white;
}
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-291.png)

Vous pouvez également améliorer cela avec la pseudo-classe `:is` :

```css
button:is(:hover, :focus, .active) {
  background-color: black;
  color: white;
}
```

Ici, vous voyez que nous ajoutons la pseudo-classe `:is` au `button`, et pour les sélecteurs, nous avons :
* la pseudo-classe `:hover`
* la pseudo-classe `:focus` et
* la classe `.active`

Cela correspondrait au bouton en conséquence.

## `:is` ne supporte pas les pseudo-éléments

Comme je l'ai mentionné précédemment, vous pouvez passer des sélecteurs de différents types comme arguments à la pseudo-classe `:is` à l'exception des pseudo-éléments.

Par exemple :

```css
:is(::after, ::selection) {
  /* styles */
}
```

Ici, nous passons les pseudo-éléments `::after` et [`::selection`](https://dillionmegida.com/p/css-selection-pseudo-element/) comme arguments pour la pseudo-classe `:is`. Une telle déclaration de style ne fonctionnera pas.

## Qu'est-ce qu'une liste de sélecteurs indulgente ?

Lorsque vous combinez plusieurs sélecteurs ensemble en CSS et que l'un de ces sélecteurs n'est pas supporté (ou est invalide), votre déclaration de style sera ignorée. Voici ce que je veux dire :

```css
.button, #box, invalid {
  /* styles */
}
```

Pour notre style ci-dessus, nous avons les sélecteurs **.button** `class`, **#box** `id`, et **invalid** `tag`. Les premier et deuxième sélecteurs sont valides, mais il n'y a pas de nom de balise comme **invalid**. Parce que le troisième n'est pas supporté, le style entier sera ignoré. 

Mais la pseudo-classe `:is` permet le concept de **liste de sélecteurs indulgente**. Cela signifie que si l'un des sélecteurs que vous passez comme argument n'est pas supporté, vous serez "pardonné". C'est-à-dire que les sélecteurs supportés seront appliqués et les éléments cibles stylisés en conséquence. Par exemple :

```css
button:is(:hover, :focuss, .active) {
  background-color: black;
  color: white;
}
```

Ici, nous passons la **:hover** `pseudo-classe`, **:focuss** `pseudo-classe`, et **.active** `class` pour nos styles. La pseudo-classe **:focuss** n'est pas supportée, mais au lieu que la déclaration de style entière soit ignorée, les sélecteurs **:hover** et **.active** seront toujours appliqués.

## Conclusion

Vous pouvez faire beaucoup de sélections avancées avec la pseudo-classe `:is`. Cette classe vous permet d'écrire des sélecteurs longs de manière plus courte et plus facile à lire.

Dans cet article, nous avons appris à propos de la pseudo-classe `:is`. À travers des exemples, nous avons vu comment elle fonctionne et comment elle améliore l'écriture du code CSS.

Gardez à l'esprit que cette pseudo-classe fonctionne de manière similaire à la pseudo-classe `:where`, avec une différence majeure. Je l'expliquerai dans un futur article sur la différence entre les pseudo-classes `:is` et `:where`.

Si vous avez aimé, n'hésitez pas à partager 😇