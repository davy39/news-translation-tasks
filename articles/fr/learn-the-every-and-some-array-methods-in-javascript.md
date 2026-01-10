---
title: Méthodes de tableau JavaScript – Comment utiliser every() et some() en JS
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2022-08-10T15:23:43.000Z'
originalURL: https://freecodecamp.org/news/learn-the-every-and-some-array-methods-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-1.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Méthodes de tableau JavaScript – Comment utiliser every() et some() en
  JS
seo_desc: 'In JavaScript, every and some help you test if something is true for every
  element or some elements of an array.

  In this article, I''ll show you how to use these helpful array methods.


  Table of Contents1How every() and some() Work – an Overview2Param...'
---

En JavaScript, `every` et `some` vous aident à tester si quelque chose est vrai pour tous les éléments ou certains éléments d'un tableau.

Dans cet article, je vais vous montrer comment utiliser ces méthodes de tableau utiles.

<!--
Generator: https://ashutoshbw.github.io/ftg/

## Comment `every()` et `some()` fonctionnent – un aperçu
## Paramètres de `every` et `some`
### `predicate`
### `thisArg` optionnel
## Cas particuliers pour `every` et `some`
### Que se passe-t-il lorsque `every` et `some` sont appelés sur un tableau vide ?
### Les éléments non existants sont ignorés
### Mutation du tableau dans le prédicat
## Un défi pour vous
-->
<div style="margin-bottom: 20px; font-size: 19px; font-family: Lato, sans-serif;"><h2 style="margin-bottom: 0px; margin-top: 20px; font-weight: normal; line-height: 50px;">Table des matières</h2><ul style="padding-left: 10px; padding-block: 8px; list-style-type: none; margin: 0px; border-block: 1px solid gray;"><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">1</span><a href="#comment-every-et-some-fonctionnent-un-aperçu">Comment <code>every()</code> et <code>some()</code> fonctionnent – un aperçu</a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2</span><a href="#paramètres-de-every-et-some">Paramètres de <code>every</code> et <code>some</code></a><ul style="list-style-type: none; margin: 0px; padding-left: 19.0243px;"><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.1</span><a href="#predicate"><code>predicate</code></a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.2</span><a href="#optional-thisarg"><code>thisArg</code> optionnel</a></li></ul></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3</span><a href="#cas-particuliers-pour-every-et-some">Cas particuliers pour <code>every</code> et <code>some</code></a><ul style="list-style-type: none; margin: 0px; padding-left: 19.0243px;"><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.1</span><a href="#quest-ce-qui-se-passe-lorsque-every-et-some-sont-appelés-sur-un-tableau-vide">Que se passe-t-il lorsque <code>every</code> et <code>some</code> sont appelés sur un tableau vide ?</a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.2</span><a href="#les-éléments-non-existants-sont-ignorés">Les éléments non existants sont ignorés</a></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.3</span><a href="#mutation-du-tableau-dans-le-prédicat">Mutation du tableau dans le prédicat</a></li></ul></li><li style="margin-block: 2px; padding: 0px;"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">4</span><a href="#un-défi-pour-vous">Un défi pour vous</a></li></ul><span style="font-size: 9px; float: right; line-height: 12px;"><a href="https://ashutoshbw.github.io/ftg/" target="_blank">Made with FTG</a></span></div>



<h2 id="comment-every-et-some-fonctionnent-un-aperçu"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">1</span>Comment <code>every()</code> et <code>some()</code> fonctionnent – un aperçu<a href="#comment-every-et-some-fonctionnent-un-aperçu" aria-label="Anchor link for: &quot;Comment every() et some() fonctionnent – un aperçu&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

Tout d'abord, nous avons besoin de données à tester. Pour simplifier, considérons un tableau de nombres :

```js
const nums = [34, 2, 48, 91, 12, 32];
```

Maintenant, disons que nous voulons tester si chaque nombre du tableau est inférieur à `100`. En utilisant `every`, nous pouvons facilement le tester comme ci-dessous :

```js
nums.every(n => n < 100);
// true
```

Court et simple ! Vous pouvez penser à ce qui se passe ici comme suit :

- `every` parcourt les éléments du tableau de gauche à droite.
  - Pour chaque itération, il appelle la fonction donnée avec l'élément courant du tableau comme premier argument.
  - La boucle continue jusqu'à ce que la fonction retourne une **[valeur fausse](https://www.ashutoshbiswas.dev/blog/truthy-and-falsy/)**. Et dans ce cas, `every` retourne `false` – sinon, il retourne `true`.


`some` fonctionne également de manière très similaire à `every` :
- `some` parcourt les éléments du tableau de gauche à droite.
  - Pour chaque itération, il appelle la fonction donnée avec l'élément courant du tableau comme premier argument.
  - La boucle continue jusqu'à ce que la fonction retourne une **[valeur vraie](https://www.ashutoshbiswas.dev/blog/truthy-and-falsy/)**. Et dans ce cas, `some` retourne `true` – sinon, il retourne `false`.

Maintenant, utilisons `some` pour tester si certains nombres du tableau sont impairs :

```js
nums.some(n => n % 2 == 1);
// true
```

C'est vraiment vrai ! `91` est impair.

Mais ce n'est pas la fin de l'histoire. Ces méthodes ont plus de profondeur. Creusons.

<h2 id="paramètres-de-every-et-some"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2</span>Paramètres de <code>every</code> et <code>some</code><a href="#paramètres-de-every-et-some" aria-label="Anchor link for: &quot;Paramètres de every et some&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

La manière d'utiliser les méthodes de tableau `every` et `some` est exactement la même. Elles ont le même ensemble de paramètres et ces paramètres signifient des choses identiques. Il est donc très facile de les apprendre en une seule fois.

Nous avons déjà travaillé avec le premier paramètre de ces méthodes qui est une fonction. Nous appelons cette fonction _predicate_.

> En informatique, un **[predicate](https://www.baeldung.com/cs/predicates)** est une fonction d'un ensemble de paramètres qui retourne un booléen comme réponse. JavaScript traite la fonction que nous donnons à `every`/`some` comme un _predicate_. Nous pouvons retourner n'importe quel type de valeur que nous souhaitons, mais celles-ci sont traitées comme un booléen, il est donc courant d'appeler cette fonction un prédicat.

Elles ont également un deuxième paramètre optionnel pour contrôler `this` à l'intérieur des prédicats non-fléchés. Nous l'appelons `thisArg`.

Vous pouvez donc appeler ces méthodes de la manière suivante :

```javascript
arr.every(predicate)
arr.every(predicate, thisArg)

arr.some(predicate)
arr.some(predicate, thisArg)
```

Voyons le `predicate` et le `thisArg` optionnel en détail ci-dessous.

<h3 id="predicate"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.1</span><code>predicate</code><a href="#predicate" aria-label="Anchor link for: &quot;predicate&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

Grâce au `predicate`, `every`/`some` nous donne non seulement accès à l'élément courant du tableau, mais aussi à son index et au tableau original via ses paramètres comme ci-dessous :

* **1er paramètre** : L'élément courant du tableau.
* **2ème paramètre** : L'index de l'élément courant.
* **3ème paramètre** : Le tableau lui-même sur lequel `every`/`some` est appelé.

Nous n'avons vu que le premier paramètre en action dans les exemples précédents. Attrapons l'index et le tableau en définissant deux paramètres supplémentaires. Cette fois, disons que nous avons des données de T-Shirt à tester pour voir si tous ont le logo `freeCodeCamp` :

```js
let tshirts = [
  { size: "S", color: "black", logo: "freeCodeCamp" },
  { size: "S", color: "white", logo: "freeCodeCamp" },
  { size: "S", color: "teal",  logo: "freeCodeCamp" },
  { size: "M", color: "black", logo: "freeCodeCamp" },
  { size: "M", color: "white", logo: "freeCodeCamp" },
  { size: "M", color: "teal",  logo: "freeCodeCamp" },
  { size: "L", color: "black", logo: "freeCodeCamp" },
  { size: "L", color: "white", logo: "freeCodeCamp" },
  { size: "L", color: "teal",  logo: "freeCodeCamp" },
];

tshirts.every((item, i, arr) => {
  console.log(i);
  console.log(arr);
  return item.logo == "freeCodeCamp";
})
```

Essayez cela dans votre console pour voir le résultat. Et n'oubliez pas de jouer aussi avec `some`.

<h3 id="optional-thisarg"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">2.2</span><code>thisArg</code> optionnel<a href="#optional-thisarg" aria-label="Anchor link for: &quot;Optional thisArg&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

Si dans un cas quelconque vous avez besoin d'avoir une valeur particulière de `this` à l'intérieur de votre prédicat, vous pouvez la définir avec `thisArg`. Notez que cela n'est applicable que pour les prédicats non-fléchés car les fonctions fléchées n'ont pas de liaisons `this`.

Si vous omettez cet argument, `this` à l'intérieur du prédicat (fonction non-fléchée) fonctionne comme d'habitude, c'est-à-dire :

* En mode strict, `this` est `undefined`.
* En mode non strict, `this` est l'**objet global** qui est `window` dans le navigateur et `global` dans Node.

Je ne peux pas penser à un bon cas d'utilisation de `thisArg`. Mais je pense qu'il est bon qu'il existe car maintenant vous avez le contrôle sur `this` à l'intérieur de votre prédicat. Donc même si un jour il y a un besoin pour cela, vous saurez qu'il y a un moyen.

Si vous avez de bonnes idées pour des utilisations de `thisArg`, faites-le moi savoir sur Twitter :)

<h2 id="cas-particuliers-pour-every-et-some"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3</span>Cas particuliers pour <code>every</code> et <code>some</code><a href="#cas-particuliers-pour-every-et-some" aria-label="Anchor link for: &quot;Cas particuliers pour every et some&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

<h3 id="quest-ce-qui-se-passe-lorsque-every-et-some-sont-appelés-sur-un-tableau-vide"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.1</span>Que se passe-t-il lorsque <code>every</code> et <code>some</code> sont appelés sur un tableau vide ?<a href="#quest-ce-qui-se-passe-lorsque-every-et-some-sont-appelés-sur-un-tableau-vide" aria-label="Anchor link for: &quot;Que se passe-t-il lorsque every et some sont appelés sur un tableau vide ?&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

Parfois, le tableau que vous voulez tester peut être vide. Par exemple, vous avez récupéré un tableau à partir d'une API et il peut avoir un nombre arbitraire d'éléments à différents moments, y compris zéro.

Pour le cas de `every`, une valeur de retour `true` peut signifier deux choses :

* Si le tableau a plus de zéro éléments, alors tous les éléments du tableau satisfont le prédicat.
* Le tableau n'a pas d'éléments.

Donc, si nous voulons, nous pouvons faire des choses folles à l'intérieur du prédicat comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/wth-what-the-hell-is-going-on.gif)

```js
const myCatsBankAccounts = [];
myCatsBankAccounts.every(account => account.balance > elonMusk.totalWealth)

```

Et obtenir toujours `true` comme valeur de retour !

Si le tableau est vide, JavaScript retourne directement `true` sans aucun appel au prédicat.

C'est parce qu'en logique, vous pouvez dire n'importe quoi sur les éléments d'un ensemble vide et cela est considéré comme vrai ou plus précisément [vrai de manière vide](https://en.wikipedia.org/wiki/Vacuous_truth). Une telle logique peut sembler absurde dans l'usage quotidien, mais c'est ainsi que la logique fonctionne. Lisez la page wiki liée ci-dessus pour en savoir plus.

Donc, si vous obtenez `true` comme valeur de retour de `every`, vous devez être conscient que le tableau pourrait être vide.

`some`, en revanche, retourne directement `false` sur les tableaux vides sans aucun appel à `predicate` et sans aucune bizarrerie.

<h3 id="les-éléments-non-existants-sont-ignorés"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.2</span>Les éléments non existants sont ignorés<a href="#les-éléments-non-existants-sont-ignorés" aria-label="Anchor link for: &quot;Les éléments non existants sont ignorés&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

Si votre tableau a des trous comme ci-dessous, ils sont ignorés par `every`/`some` :

```js
const myUntiddyArry = [1,,,3,,42];
```

<h3 id="mutation-du-tableau-dans-le-prédicat"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">3.3</span>Mutation du tableau dans le prédicat<a href="#mutation-du-tableau-dans-le-prédicat" aria-label="Anchor link for: &quot;Mutation du tableau dans le prédicat&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h3>

Je ne discuterai pas de ce cas ici, car la mutation du tableau original complique généralement les choses et laisse plus de place aux bugs.

Si vous en avez vraiment besoin ou si vous êtes intéressé, veuillez lire la note dans la [spécification](https://tc39.es/ecma262/multipage/indexed-collections.html#sec-array.prototype.every) pour plus de détails.

<h2 id="un-défi-pour-vous"><span style="margin-right: 8px; color: rgb(102, 166, 46); font-weight: bold; font-style: normal;">4</span>Un défi pour vous<a href="#un-défi-pour-vous" aria-label="Anchor link for: &quot;Un défi pour vous&quot;" style="color: rgb(208, 52, 52); padding-left: 8px; text-decoration: none;">#</a></h2>

Exprimez `every` avec `some` et `some` avec `every` en JavaScript.

J'espère que vous ressentirez également l'immense joie et émerveillement que j'ai eus lorsque j'ai découvert cette relation !

<details style="align-self: flex-start; margin: 1.5em 0 1.5em; width: 100%;">
  <summary>Solution</summary>
<p>Faisons cela étape par étape. D'abord, essayons d'exprimer <code>every</code> avec <code>some</code> :</p>
<ul>
<li>Pour chaque élément du tableau, le prédicat est vrai.</li>
<li>Il n'est pas vrai que pour certains éléments du tableau, le prédicat n'est pas vrai.</li>
</ul>
<p>Nous pouvons traduire cela en JavaScript comme ci-dessous :</p>
<pre style="min-width:0">const myEvery = (arr, predicate) => !arr.some(e => !predicate(e));
</pre>
<p>Maintenant, exprimons <code>some</code> avec <code>every</code>. C'est presque la même chose qu'avant. Juste <code>some</code> est remplacé par <code>every</code>. Essayez de comprendre ce qui se passe :</p>
<ul>
<li>Pour certains éléments du tableau, le prédicat est vrai.</li>
<li>Il n'est pas vrai que pour chaque élément du tableau, le prédicat n'est pas vrai.</li>
</ul>
<p>En JavaScript :</p>
<pre style="min-width:0">const mySome = (arr, predicate) => !arr.every(e => !predicate(e));
</pre>
<p>Notez que les implémentations ci-dessus fonctionnent également lorsque <code>arr</code> est vide. Et pour simplifier, j'ai exclu les autres paramètres du <code>predicate</code> et <code>thisArg</code>. Essayez d'ajouter ces détails vous-même, si vous êtes intéressé. Dans ce processus, vous pourriez apprendre une ou plusieurs choses !</p>
</details>

Merci d'avoir lu ! J'espère que cet article a été utile. Consultez mes autres articles [ici](https://www.freecodecamp.org/news/author/ashutoshbw/). Restons en contact sur [Twitter](https://twitter.com/ashutoshbw).