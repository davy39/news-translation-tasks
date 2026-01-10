---
title: nth-child() vs nth-of-type() Sélecteurs en CSS – Quelle est la Différence ?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2024-01-31T18:33:32.000Z'
originalURL: https://freecodecamp.org/news/nth-child-vs-nth-of-type-selector-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/nth-child-vs-nth-of-type-css-selector-freecodecamp-featured-codesweetly.jpg
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: Web Development
  slug: web-development
seo_title: nth-child() vs nth-of-type() Sélecteurs en CSS – Quelle est la Différence
  ?
seo_desc: 'The :nth-child() and :nth-of-type() CSS selectors select items from a group
  of HTML elements. But they work in different ways.

  Here is the main distinction between them:


  nth-child() selects its items from any group of elements. nth-of-type() selects...'
---

Les sélecteurs CSS `:nth-child()` et `:nth-of-type()` sélectionnent des éléments à partir d'un groupe d'éléments HTML. Mais ils fonctionnent de manières différentes.

Voici la principale distinction entre eux :

![nth-child vs nth-of-type selector in CSS](https://www.freecodecamp.org/news/content/images/2024/01/nth-child-vs-nth-of-type-selector-in-css-codesweetly.png)
_nth-child() sélectionne ses éléments à partir de n'importe quel groupe d'éléments. nth-of-type() sélectionne ses éléments à partir d'un type spécifié d'élément._

* `:nth-child()` sélectionne des éléments à partir d'un groupe général d'éléments. Par exemple, sélectionner un nœud `<p>` à partir d'un groupe mixte qui inclut `<h1>`, `<div>`, et `<section>`.
* `:nth-of-type()` sélectionne des éléments à partir d'un groupe spécifié d'éléments. Par exemple, sélectionner un nœud `<p>` à partir d'un groupe de frères `<p>`.

Cet article utilise des exemples pour vous montrer exactement comment les deux sélecteurs fonctionnent en CSS afin que vous puissiez comprendre leurs similitudes et différences.

## Table des Matières

1. [Qu'est-ce que le sélecteur CSS :nth-child() ?](#heading-quest-ce-que-le-selecteur-css-nth-child)
   - [Syntaxe du sélecteur CSS :nth-child()](#heading-syntaxe-du-selecteur-css-nth-child)
   - [Exemples du sélecteur CSS :nth-child()](#heading-exemples-du-selecteur-css-nth-child)
2. [Qu'est-ce que le sélecteur CSS :nth-of-type() ?](#heading-quest-ce-que-le-selecteur-css-nth-of-type)
   - [Syntaxe du sélecteur CSS :nth-of-type()](#heading-syntaxe-du-selecteur-css-nth-of-type)
   - [Exemples du sélecteur CSS :nth-of-type()](#heading-exemples-du-selecteur-css-nth-of-type)
3. [Aperçu](#heading-aperçu)

Alors, sans plus tarder, commençons avec le sélecteur `:nth-child()`.

## Qu'est-ce que le sélecteur CSS `:nth-child()` ?

Le sélecteur CSS `:nth-child()` sélectionne un ou plusieurs éléments enfants parmi leurs frères directs, indépendamment des types de nœuds.

### Syntaxe du sélecteur CSS `:nth-child()`

Le sélecteur CSS `:nth-child()` accepte un seul argument. Voici la syntaxe :

```css
html-element:nth-child(valeur) {
  déclarations de style
}
```

L'argument `valeur` peut être l'un des suivants :

1. Un nombre : Par exemple, utiliser `3` représente le troisième enfant.
2. Le mot-clé `even` ou `odd` : Nous l'utilisons pour représenter les enfants pairs ou impairs.
3. La formule `An+B` : Nous l'utilisons pour exprimer une série de nombres. Par exemple, `2n+3` exprime ces nombres : `[(2x0)+3]`, `[(2x1)+3]`, `[(2x2)+3]`, `[(2x3)+3]`, et ainsi de suite.

Notez ce qui suit :

- `:nth-child()` est un sélecteur de [pseudo-classe](https://codesweetly.com/css-pseudo-selectors#what-is-a-css-pseudo-class-selector) CSS.
- Le sélecteur `:nth-child()` fonctionne uniquement sur les frères directs.
- Dans la formule `An+B`,
  - `A` est une valeur [entière](https://codesweetly.com/web-tech-terms-i#integer) de votre choix.
  - `n` est le multiplicateur qui augmente automatiquement à partir de zéro (`0`).
  - `+` (ou `-`) est l'opérateur d'addition (ou de soustraction).
  - `B` est une valeur de décalage optionnelle pour augmenter (ou diminuer) le résultat dérivé après avoir multiplié `A` et `n`.

### Exemples du sélecteur CSS `:nth-child()`

Voici des exemples de la façon d'utiliser le sélecteur de pseudo-classe CSS `:nth-child()`.

#### Appliquer DeepPink à l'élément `<p>` qui est le troisième enfant de son élément parent

Le sélecteur `:nth-child()` ci-dessous sélectionne l'élément `<p>` qui est le troisième enfant de son élément parent.

```css
p:nth-child(3) {
  color: DeepPink;
}

```

Si l'extrait ci-dessous est le document HTML pour le [jeu de règles CSS](https://codesweetly.com/css-ruleset) ci-dessus, les navigateurs appliqueront `DeepPink` au deuxième élément `<p>` uniquement.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<p>Second paragraph element</p>
<h2>First heading 2 element</h2>
<p>Third paragraph element</p>
<h3>First heading 3 element</h3>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-3c8dkj)

Le sélecteur `:nth-child()` fonctionne uniquement sur les frères directs. Par exemple, vous pouvez réécrire l'extrait HTML ci-dessus pour inclure des éléments imbriqués comme suit :

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p>Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's third paragraph element</p>
    <p>Article's fourth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's fifth paragraph element</p>
  <p>Article's sixth paragraph element</p>
</article>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-harjmu)

Le sélecteur `p:nth-child(3)` appliquera `DeepPink` uniquement au quatrième nœud `<p>` car il est le troisième enfant de son élément parent.

#### Appliquer DeepPink à chaque enfant impair qui est un nœud `<p>`

Le sélecteur `:nth-child()` ci-dessous sélectionne chaque élément enfant impair qui est un nœud `<p>`.

```css
p:nth-child(odd) {
  color: DeepPink;
}

```

**Note :** `1` est la position d'[index](https://codesweetly.com/web-tech-terms-i#index) du premier élément enfant.

En supposant que l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, les navigateurs appliqueront `DeepPink` au quatrième élément `<p>` uniquement.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<h2>First heading 2 element</h2>
<p>Second paragraph element</p>
<h3>First heading 3 element</h3>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-p2tsnq)

#### Appliquer `DeepPink` à chaque enfant pair qui est un nœud `<p>`

Le sélecteur `:nth-child()` ci-dessous sélectionne chaque élément enfant pair qui est un nœud `<p>`.

```css
p:nth-child(even) {
  color: DeepPink;
}

```

**Note :** `1` est la position d'index du premier élément enfant.

En supposant que l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, les navigateurs appliqueront `DeepPink` aux premier, deuxième, quatrième et sixième éléments `<p>`.

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p>Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <p>Article's third paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-c9bvm5)

#### Appliquer DeepPink au troisième élément enfant, septième, onzième, et ainsi de suite qui est un nœud `<p>`

Le sélecteur `:nth-child()` ci-dessous sélectionne chaque élément enfant `<p>` dont l'index est un multiple de deux (`2`) avec un décalage de trois (`+3`).

**Note :** `1` est la position d'index du premier élément enfant.

```css
p:nth-child(2n+3) {
  color: DeepPink;
}

```

**Quiz Amusant :** Si l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, lesquels des éléments le navigateur stylisera-t-il ?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<div><p>Fifth paragraph element</p></div>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<div><p>Nineth paragraph element</p></div>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-ri4zjg)

#### Appliquer DeepPink au premier enfant, troisième, cinquième, et ainsi de suite qui est un nœud `<p>`

Le sélecteur `:nth-child()` ci-dessous sélectionne chaque élément enfant `<p>` dont l'index est un multiple de deux (`2`) avec un décalage de moins trois (`-3`).

**Note :** `1` est la position d'index du premier élément enfant.

```css
p:nth-child(2n-3) {
  color: DeepPink;
}

```

**Quiz Amusant :** Si l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, lesquels des éléments le navigateur stylisera-t-il ?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<div><p>Fifth paragraph element</p></div>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<div><p>Nineth paragraph element</p></div>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-jc7gyl)

#### Appliquer DeepPink aux nœuds `<p>` qui sont l'un des trois premiers enfants de leur parent

Le sélecteur `:nth-child()` ci-dessous applique DeepPink aux nœuds `<p>` s'ils sont l'un des trois premiers éléments de leur parent.

```css
p:nth-child(-n+3) {
  color: DeepPink;
}

```

**Quiz Amusant :** Si l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, lesquels des éléments le navigateur stylisera-t-il ?

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p>Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <p>Article's third paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-rjuvvs)

Notez que :

- `1` est la position d'index du premier élément enfant.
- La syntaxe `-n+3` sélectionne toujours les trois premiers enfants car :
  - `-1 + 3 = 2`
  - `-2 + 3 = 1`
  - `-3 + 3 = 0`


Maintenant que nous savons comment fonctionne le sélecteur CSS `:nth-child()`, discutons de `:nth-of-type()` afin que nous puissions voir la différence.

## Qu'est-ce que le sélecteur CSS `:nth-of-type()` ?

Le sélecteur CSS `:nth-of-type()` sélectionne un ou plusieurs éléments enfants parmi leurs frères directs du même type de nœud.

### Syntaxe du sélecteur CSS `:nth-of-type()`

Le sélecteur CSS `:nth-of-type()` accepte un seul argument. Voici la syntaxe :

```css
html-element:nth-of-type(valeur) {
  déclarations de style
}

```

L'argument `valeur` peut être l'un des suivants :

1. Un nombre : Par exemple, utiliser `3` représente le troisième type d'élément.
2. Le mot-clé `even` ou `odd` : Nous l'utilisons pour représenter les types d'éléments pairs ou impairs.
3. La formule `An+B` : Nous l'utilisons pour exprimer une série de nombres. Par exemple, `2n+3` exprime ces nombres : `[(2x0)+3]`, `[(2x1)+3]`, `[(2x2)+3]`, `[(2x3)+3]`, et ainsi de suite.

Notez ce qui suit :

- `:nth-of-type()` est un sélecteur de [pseudo-classe](https://codesweetly.com/css-pseudo-selectors#what-is-a-css-pseudo-class-selector) CSS.
- Le sélecteur `:nth-of-type()` fonctionne uniquement sur les frères directs.
- Dans la formule `An+B`,
  - `A` est une valeur [entière](https://codesweetly.com/web-tech-terms-i#integer) de votre choix.
  - `n` est le multiplicateur qui augmente automatiquement à partir de zéro (`0`).
  - `+` (ou `-`) est l'opérateur d'addition (ou de soustraction).
  - `B` est une valeur de décalage optionnelle pour augmenter (ou diminuer) le résultat dérivé après avoir multiplié `A` et `n`.

### Exemples du sélecteur CSS `:nth-of-type()`

Voici des exemples de la façon d'utiliser le sélecteur de pseudo-classe CSS `:nth-of-type()`.

#### Appliquer DeepPink au troisième type d'élément `<p>`

Le sélecteur `:nth-of-type()` ci-dessous sélectionne le troisième élément `<p>` parmi ses frères du même type de nœud.

```css
p:nth-of-type(3) {
  color: DeepPink;
}

```

En supposant que l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, les navigateurs appliqueront `DeepPink` au troisième élément `<p>` uniquement.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<p>Second paragraph element</p>
<h2>First heading 2 element</h2>
<p>Third paragraph element</p>
<h3>First heading 3 element</h3>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-txtema)

Le sélecteur `:nth-of-type()` fonctionne uniquement sur les frères directs. Par exemple, vous pouvez réécrire l'extrait HTML ci-dessus pour inclure des éléments imbriqués comme suit :

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p> Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's third paragraph element</p>
    <p>Article's fourth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's fifth paragraph element</p>
  <p>Article's sixth paragraph element</p>
</article>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-hv18yl)

Le sélecteur `p:nth-of-type(3)` appliquera `DeepPink` uniquement au cinquième nœud `<p>` car il est le troisième type `<p>` de son élément parent.

Par conséquent, si vous ajoutez un nœud `<p>` supplémentaire à l'élément `<section>`, le sélecteur `p:nth-of-type(3)` appliquera `DeepPink` aux cinquième et sixième éléments `<p>`.

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p> Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's third paragraph element</p>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-ydvfhw)

#### Appliquer DeepPink à chaque type d'élément `<p>` impair

Le sélecteur `:nth-of-type()` ci-dessous sélectionne chaque élément enfant `<p>` avec un [index](https://codesweetly.com/web-tech-terms-i#index) impair.

```css
p:nth-of-type(odd) {
  color: DeepPink;
}

```

**Note :** `1` est la position d'index du premier élément enfant.

En supposant que l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, les navigateurs appliqueront `DeepPink` aux premier et troisième éléments `<p>`.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<h2>First heading 2 element</h2>
<p>Second paragraph element</p>
<h3>First heading 3 element</h3>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-uhbpyv)

#### Appliquer DeepPink à chaque type d'élément `<p>` pair

Le sélecteur `:nth-of-type()` ci-dessous sélectionne chaque élément enfant `<p>` avec un index pair.

```css
p:nth-of-type(even) {
  color: DeepPink;
}

```

**Note :** `1` est la position d'index du premier élément enfant.

En supposant que l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, les navigateurs appliqueront `DeepPink` aux deuxième, cinquième et sixième éléments `<p>`.

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p> Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <p>Article's third paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-ueawgj)

**Note :** Les navigateurs appliqueront `DeepPink` au cinquième paragraphe car il est le deuxième nœud `<p>` de l'élément `<section>`.

#### Appliquer DeepPink au troisième type d'élément `<p>`, cinquième, septième, et ainsi de suite

Le sélecteur `:nth-of-type()` ci-dessous sélectionne chaque élément enfant `<p>` dont l'index est un multiple de deux (`2`) avec un décalage de trois (`+3`).

**Note :** `1` est la position d'index du premier élément enfant.

```css
p:nth-of-type(2n+3) {
  color: DeepPink;
}

```

**Quiz Amusant :** Si l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, lesquels des éléments le navigateur stylisera-t-il ?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<p>Nineth paragraph element</p>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-mbfvqr)

#### Appliquer DeepPink au premier type d'élément `<p>`, troisième, cinquième, et ainsi de suite

Le sélecteur `:nth-of-type()` ci-dessous sélectionne chaque élément enfant `<p>` dont l'index est un multiple de deux (`2`) avec un décalage de moins trois (`-3`).

**Note :** `1` est la position d'index du premier élément enfant.

```css
p:nth-of-type(2n-3) {
  color: DeepPink;
}

```

**Quiz Amusant :** Si l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, lesquels des éléments le navigateur stylisera-t-il ?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<p>Nineth paragraph element</p>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-inivqw)

#### Appliquer DeepPink aux trois premiers types d'éléments `<p>`

Le sélecteur `:nth-of-type()` ci-dessous applique `DeepPink` aux trois premiers éléments enfants `<p>`.

```css
p:nth-of-type(-n+3) {
  color: DeepPink;
}

```

**Quiz Amusant :** Si l'extrait ci-dessous est le document HTML pour le jeu de règles CSS ci-dessus, lesquels des éléments le navigateur stylisera-t-il ?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<p>Nineth paragraph element</p>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Essayez de le modifier**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-akcgtf)

**Note :**

- `1` est la position d'index du premier élément enfant.
- La syntaxe `-n+3` sélectionne toujours les trois premiers éléments enfants `<p>` car :
  - `-1 + 3 = 2`
  - `-2 + 3 = 1`
  - `-3 + 3 = 0`

## Aperçu

Dans cet article, nous avons discuté des similitudes et des différences entre les sélecteurs CSS `:nth-child()` et `:nth-of-type()`. Nous avons également utilisé des exemples pour voir comment ils fonctionnent.

Merci d'avoir lu !

### Et voici une ressource utile sur React.JS :

J'ai écrit un livre sur la [Création de Paquets NPM](https://amzn.to/48NjBdY) !

C'est un guide convivial pour débutants afin de maîtriser l'art de créer, tester et publier des bibliothèques NPM dans l'écosystème React et JavaScript.

Il utilise un projet évolutif pour expliquer les fondamentaux de la construction et de la gestion de paquets NPM à partir de zéro.

[![Creating NPM Package ReactJS book is now available at Amazon](https://www.freecodecamp.org/news/content/images/2024/01/creating-npm-package-reactjs-book-codesweetly.png)](https://amzn.to/48NjBdY)