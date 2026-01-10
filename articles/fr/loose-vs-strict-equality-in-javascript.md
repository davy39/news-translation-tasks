---
title: Comment == est différent de === en JavaScript ? Égalité stricte vs. égalité
  souple expliquée
subtitle: ''
author: Sobit Prasad
co_authors: []
series: null
date: '2023-02-14T18:09:26.000Z'
originalURL: https://freecodecamp.org/news/loose-vs-strict-equality-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/shapes--1--1.png
tags:
- name: Equality
  slug: equality
- name: JavaScript
  slug: javascript
seo_title: Comment == est différent de === en JavaScript ? Égalité stricte vs. égalité
  souple expliquée
seo_desc: 'If you are reading this blog, you''re probably learning JavaScript – and
  that''s awesome.

  Double equals (==) and triple equals (===) in JavaScript often make beginners scratch
  their heads. This doesn''t mean that you should fear JavaScript, in fact jarg...'
---

Si vous lisez ce blog, vous apprenez probablement JavaScript – et c'est génial.

Les doubles égaux (==) et triples égaux (===) en JavaScript font souvent gratter la tête des débutants. Cela ne signifie pas que vous devriez craindre JavaScript, en fait, le jargon comme celui-ci rend JavaScript encore plus beau une fois que vous savez comment il fonctionne.

## Que sont `==` et `===` en JavaScript ?

Maintenant, une chose que nous devons retenir est que `==` et `===` sont tous deux utilisés pour des comparaisons et pour trouver le degré de similitude ou d'égalité entre les choses que nous comparons.

`==` et `===` retournent tous deux **true** s'ils trouvent une égalité et **false** sinon. Mais il y a un piège : `==` et `===` utilisent des critères différents pour mesurer le degré d'égalité.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/shapes--2-.png align="left")

Cela dit, comprenons comment `==` (double égal) est différent de `===` (triple égal) en utilisant différents exemples.

## Comment fonctionne Double Égal (==) – avec des exemples

Double égal (==) est souvent appelé "égalité souple" car il effectue une coercition de type avant de faire toute comparaison.

Cela signifie que si les types de données des opérandes que nous comparons sont différents, alors le moteur JavaScript convertit automatiquement l'un des opérandes pour qu'il soit du même type que l'autre afin de rendre la comparaison possible.

Comprenons avec l'aide d'un exemple.

```js
const a = 100;
const b = '100';

console.log(a == b) // true
```

Dans l'exemple ci-dessus, nous avons deux variables `a` et `b`. Le type de la variable `a` est `number` et le type de la variable `b` est `string`.

Maintenant, lorsque nous comparons les deux variables en utilisant double égal (`==`), nous obtenons `true` comme résultat.

C'est parce que le type de la variable `a` est converti en `string` avant de faire la comparaison.

Après la comparaison, la valeur est vérifiée dans les deux variables. Si elle est la même, nous obtiendrons `true`, et nous obtiendrons `false` sinon. Dans notre cas, c'est `true`.

**Il est important de noter que les valeurs réelles restent inchangées. Elles sont uniquement converties implicitement lors de la comparaison.**

### Règles pour la coercition de type

L'exemple ci-dessus est assez simple, n'est-ce pas ? Alors, testons-le à nouveau avec un autre exemple. Et après cela, nous explorerons les règles pour la coercition de type.

```js
const a = true;
const b = 'true';

console.log(a == b)
```

Maintenant, que pensez-vous que sera le résultat ? Si votre réponse était `true`, malheureusement ce n'est pas correct. Mais si vous avez compris que c'était `false`, alors félicitations.

Si votre réponse était fausse, ne vous inquiétez pas car nous allons apprendre quelques règles qui vous aideront à mieux comprendre.

Donc, voici les règles pour la coercition de type en JavaScript :

* Si l'un des opérandes est une `string`, l'autre opérande sera converti en `string`.

* Si l'un des opérandes est un `number`, l'autre opérande sera converti en `number`.

* Si l'un des opérandes est un `boolean`, il sera converti en `number` (`true` devient `1` et `false` devient `0`).

* Si l'un des opérandes est un `object` et l'autre est une valeur primitive, l'objet sera converti en une valeur primitive avant que la comparaison ne soit faite.

* Si l'un des opérandes est `null` ou `undefined`, l'autre doit également être `null` ou `undefined` pour retourner `true`. Sinon, il retournera `false`.

Maintenant, à partir du point trois, vous savez pourquoi notre réponse était `false` dans l'exemple ci-dessus.

C'est parce que la valeur de la variable `a` (`true`) est convertie en nombre avant la comparaison. Donc après la comparaison – où nous comparons maintenant 1 et `'true'` – nous obtenons `false` parce que les variables contiennent des valeurs différentes.

## Comment fonctionne Triple Égal (===) – avec des exemples

Triple égal (===), également appelé "égalité stricte", fonctionne de manière similaire à double égal (==), avec une différence importante : il ne convertit pas les types des opérandes avant de comparer.

Lors de la comparaison des variables, il vérifie d'abord si les types diffèrent. Si c'est le cas, il retourne `false`. Si les types correspondent, alors il vérifie la valeur. Si les valeurs sont les mêmes et ne sont pas des nombres, il retourne `true`.

Enfin, si les deux opérandes sont des nombres et ne sont pas `NaN`, et qu'ils ont la même valeur, alors il retourne `true`. Sinon, `false`.

Comprenons cela avec l'aide d'exemples :

```js
const a = 100;
const b = '100';

console.log(a === b);
```

Nous avons pris le même exemple que ci-dessus, mais au lieu de comparer avec double égal (==), nous comparons avec triple égal (===).

Donc, vous avez peut-être déjà deviné la réponse. Oui, c'est `false`, pourquoi ? Parce que le type de la variable `a` est number et le type de la variable `b` est string.

Lors de la comparaison, triple égal vérifie d'abord les types des opérandes – et ces types diffèrent dans cet exemple. Donc, il retourne `false`.

Regardons un autre exemple :

```js
const a = true;
const b = 1;

console.log(a === b);
```

Dans l'exemple ci-dessus, nous avons deux variables `a` et `b`. Le type de la variable `a` est boolean et le type de la variable `b` est number.

Donc, si nous comparons en utilisant triple égal (===), il retournera `false` – parce que, encore une fois, les variables ont des types différents.

## Conclusion

Les opérateurs `==` et `===` en JavaScript sont des opérateurs de comparaison que nous utilisons pour déterminer si deux valeurs sont égales ou non.

L'opérateur `==` effectue une comparaison d'égalité souple qui effectue une coercition de type si nécessaire pour rendre la comparaison possible.

L'opérateur `===`, en revanche, effectue une comparaison d'égalité stricte qui n'effectue pas de coercition de type et nécessite que les opérandes aient le même type (ainsi que la même valeur).

La coercition de type en JavaScript peut parfois conduire à des résultats inattendus, il est donc généralement recommandé d'utiliser l'opérateur d'égalité stricte `===` plutôt que l'opérateur d'égalité souple `==`.