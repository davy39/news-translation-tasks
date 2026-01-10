---
title: Types de sélecteurs CSS – Comment sélectionner des éléments à styliser en CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-19T22:01:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-select-elements-to-style-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/css-selector-types.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: style
  slug: style
seo_title: Types de sélecteurs CSS – Comment sélectionner des éléments à styliser
  en CSS
seo_desc: "By Dillion Megida\nWhen you want to style an element with CSS, you first\
  \ have to \"select\" it. In this article, I'll show you seven (7) ways in which\
  \ you can do that.\nHere's the syntax for styling elements in CSS:\nselector {\n\
  \  /* styles here */\n}\n\nYou ..."
---

Par Dillion Megida

Lorsque vous souhaitez styliser un élément avec CSS, vous devez d'abord le "sélectionner". Dans cet article, je vais vous montrer sept (7) façons de le faire.

Voici la syntaxe pour styliser des éléments en CSS :

```css
sélecteur {
  /* styles ici */
}
```

Vous avez le sélecteur qui "cible" le ou les éléments que vous souhaitez styliser, puis vous avez une accolade ouvrante. Après l'accolade, vous avez vos styles utilisant différentes propriétés CSS, et vous la fermez avec une accolade fermante.

Il existe de nombreuses façons de cibler des éléments. Vous pouvez appeler ces méthodes **Types de Sélecteurs**.

Voici une vidéo avec des exemples sur les [Façons de sélectionner des éléments à styliser en CSS](https://www.youtube.com/watch?v=0yysG5U_2i8) si vous préférez cela.

Voici sept types de sélecteurs en CSS.

## 1. Comment utiliser le Sélecteur Universel (*) en CSS

Le Sélecteur Universel, **astérisque** (*), vous permet de sélectionner TOUS les éléments de n'importe quel type pour les styliser. Voici un exemple :

```css
* {
  border: 1px solid black;
}
```

Supposons que nous utilisions ce style pour le HTML suivant :

```html
<body>
    <h1>Styles CSS</h1>
    <p>Comment appliquer des styles</p>
    <div>
        <img width="20px" height="20px" src="https://www.freecodecamp.org/news/content/images/size/w150/2022/03/deee.jpg" />
    </div>
</body>
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image--3-.png)

Vous pouvez voir que les éléments `body`, `h1`, `p`, `div` et `img` ont tous une `border` de **1px solid black** parce que nous avons utilisé le sélecteur universel.

## 2. Comment styliser des éléments par nom de balise en CSS

Vous pouvez également sélectionner des éléments pour les styliser en utilisant leurs noms de balise. Voici un exemple :

```css
p {
  color: red;
}

img {
  width: 100px;
  height: 100px;
}
```

Ces déclarations de style appliquent une `color` **red** à tous les éléments `p` et une `width` et `height` de **200px** à tous les éléments `img`.

Voici comment le style ci-dessus fonctionne avec ce HTML :

```html
<span>Je suis un span</span>
<p>Il y a un span au-dessus de moi</p>
<img src="https://www.freecodecamp.org/news/content/images/size/w150/2022/03/deee.jpg" />
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-383.png)

Vous pouvez voir que le `span` n'est pas stylisé – seuls le `img` et le `p` le sont.

## 3. Comment styliser des classes en CSS

Les éléments acceptent différents attributs (également appelés propriétés), y compris les classes. Vous pouvez cibler un élément en fonction de la classe que vous avez spécifiée dessus. Voici un exemple :

```html
<div class="container">
    <h2>Bonjour</h2>
</div>

<div>
    <h2>Comment allez-vous</h2>
</div>
```

Il y a deux `div` ici, mais un seul a un attribut de classe avec la valeur **container**. Vous pouvez styliser celui avec la classe en utilisant un **point** (**.**) puis la classe comme ceci :

```css
div {
  border: 1px solid purple;
}

.container {
  border-width: 20px;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image--5-.png)

Dans le CSS, nous avons spécifié que tous les éléments `div` doivent avoir une `border` de **1px solid purple**. Mais pour l'élément avec une classe **container**, vous pouvez voir dans le résultat qu'il a une `border-width` de 20px.

## 4. Comment styliser des identifiants en CSS

Similaire à l'attribut `class`, vous pouvez spécifier un `id` sur un élément que vous pouvez cibler depuis CSS pour le styliser.

Voici un exemple :

```html
<div class="container">
    <h2>Bonjour</h2>
</div>

<div id="container">
    <h2>Comment allez-vous</h2>
</div>
```

Vous pouvez cibler l'élément `id` ici en utilisant un **dièse** (**#**) puis l'id comme ceci :

```css
#container {
  border-left: 10px solid blue;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-385.png)

En utilisant l'élément (qu'il s'agisse d'un `div`, `p`, ou de n'importe quel type) avec l'`id` **container**, nous avons appliqué des styles uniquement au deuxième élément `div`.

Contrairement aux classes, cependant, les `id` doivent être **uniques**. Deux éléments ou plus ne peuvent pas avoir le même `id`, car cela causerait des comportements inattendus.

## 5. Comment styliser d'autres attributs en CSS

Nous avons vu comment cibler les attributs `class` et `id`. Et si vous vouliez cibler d'autres attributs ? Eh bien, vous pouvez le faire en utilisant des **crochets** (**[attr]**). Comment cela fonctionne-t-il ?

Voyons un exemple :

```html
<a href="#">
    Un lien
</a>

<p href="https://google.com">
    Un paragraphe lien
</p>
```

Dans cet exemple, nous avons deux éléments : une balise `a` et une balise `p`. Pour styliser les deux éléments, vous pouvez utiliser leurs noms de balise directement :

```css
p, a {
  color: red;
}
```

La virgule vous permet d'appliquer des styles à plusieurs sélecteurs à la fois.

Mais une autre façon de styliser les deux éléments est d'utiliser leurs attributs. Ils ont tous les deux un attribut `href`.

Gardez simplement à l'esprit que l'attribut `href` n'est pas supporté dans les balises `p` cependant. Je l'utilise simplement pour illustrer un exemple.

Voici comment vous pouvez utiliser l'attribut `href` pour styliser les deux éléments :

```css
[href] {
  color: red;
}
```

Ce CSS correspondra à tous les éléments avec l'attribut `href`.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-386.png)

Les deux éléments ont l'attribut `href` et sont donc sélectionnés pour nos styles. Ici, nous avons utilisé l'attribut `href` sans valeur. Vous pouvez également spécifier une valeur pour être précis sur votre cible comme ceci :

```css
[href="#"] {
  color: red;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-387.png)

Seule la balise `a` a l'attribut `href` avec la valeur **#**, donc c'est le seul élément qui correspond à nos styles, comme vous pouvez le voir sur l'image ci-dessus.

## 6. Comment utiliser les Pseudo-Classes en CSS

Les pseudo-classes sont des types de sélecteurs qui vous permettent de sélectionner des éléments dans un état particulier. Pour en nommer quelques-unes, voici quelques états supportés :

* `hover` (lorsque la souris survole un élément)
* `disabled` (lorsqu'un élément tel qu'une entrée ou un bouton est désactivé)
* `required` (lorsqu'un élément de formulaire est requis)

Et bien d'autres que vous pouvez trouver dans la [Documentation MDN sur les Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes).

Vous pouvez appliquer des styles lorsque les éléments sont dans ces états. Vous sélectionnez l'état en utilisant un **deux-points** (**:**) suivi de l'état. Voici un exemple :

```html
<!DOCTYPE html>
<button>
    Survolez-moi
</button>
```

La ligne `<!DOCTYPE html>` est importante pour spécifier qu'il s'agit de HTML5 afin que les pseudo-classes puissent fonctionner.

Et voici le CSS :

```css
:hover {
  background-color: black;
  color: white;
}
```

Ce CSS appliquerait ces styles à n'importe quel élément que vous survolez. Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-388.png)

L'image de gauche est sans l'état de survol. À droite, vous pouvez voir les styles appliqués au `body` et au `button` parce que nous les survolons.

En survolant le `button`, vous survolez également le `body` parce que le `button` est un enfant du `body`.

## 7. Comment utiliser le Sélecteur de Pseudo-Éléments en CSS

Les pseudo-éléments (différents des Pseudo-Classes) sont utilisés pour sélectionner une "partie spécifique d'un élément". Pas l'élément entier – juste une partie. Et vous pouvez également les utiliser pour ajouter des éléments pseudo (artificiels) à un élément existant.

Voici un article détaillé sur les [Pseudo-éléments vs Pseudo-classes en CSS](https://dillionmegida.com/p/pseudo-elements-vs-pseudo-classes-in-css/)

Voici quelques sélecteurs de pseudo-éléments supportés :

* `selection` : la partie surlignée d'un élément
* `first-line` : la première ligne d'un paragraphe
* `placeholder` : le texte de l'espace réservé d'un élément d'entrée

Et bien d'autres que vous pouvez trouver dans la [Documentation MDN sur les Pseudo-éléments](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements).

Pour appliquer des styles en utilisant un sélecteur de pseudo-élément, vous utilisez **deux deux-points** (**::**) suivis du pseudo-élément. Voici un exemple :

```html
<!DOCTYPE html>
<input placeholder="Entrez un texte" />
```

Et voici le CSS pour ce HTML :

```css
input {
  color: blue;
}

::placeholder {
  color: red;
  font-style: italic;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-389.png)

Le sélecteur de pseudo-élément `::placeholder` style la "partie espace réservé" de tous les éléments de formulaire. Comme vous pouvez le voir dans l'exemple ci-dessus, l'élément `input` lui-même a un style `color` de **blue**, mais la partie espace réservé a un style différent.

## Conclusion

Dans cet article, je vous ai montré sept façons de cibler les éléments que vous souhaitez styliser. Nous avons vu :

* le sélecteur universel, pour sélectionner tous les éléments
* les noms de balise pour sélectionner les éléments qui correspondent à un nom de balise
* les classes pour sélectionner les éléments avec un attribut de classe
* les identifiants pour sélectionner un élément avec un attribut d'identifiant
* les attributs pour sélectionner les éléments qui ont un attribut avec ou sans une valeur spécifiée
* les pseudo-classes pour sélectionner les éléments dans un état spécifique
* les pseudo-éléments pour sélectionner des parties spécifiques d'un élément

Vous pouvez également combiner ces sélecteurs pour être plus précis sur l'élément que vous souhaitez cibler. Vous le faites en utilisant des **Combinateurs**.

Les combinateurs vous permettent d'utiliser plusieurs sélecteurs pour cibler des éléments en fonction de la relation entre les éléments qui correspondent aux sélecteurs. Voici un [article que j'ai écrit sur les combinateurs si vous voulez en savoir plus](https://www.freecodecamp.org/news/css-combinators-to-select-elements/).

Pour vous donner un aperçu rapide – les combinateurs sont utilisés entre plusieurs types de sélecteurs, et ils vous permettent de styliser des éléments en fonction de la relation qu'ils ont avec d'autres éléments.

Merci d'avoir lu !