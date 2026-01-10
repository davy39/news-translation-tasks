---
title: Exemple JavaScript String.Replace() avec RegEx
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-20T20:31:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-replace-example-with-regex
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c982a740569d1a4ca1884.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Regex
  slug: regex
- name: Web Development
  slug: web-development
seo_title: Exemple JavaScript String.Replace() avec RegEx
seo_desc: 'By Dillion Megida

  Regular Expressions (also called RegEx or RegExp) are a powerful way to analyze
  text. With RegEx, you can match strings at points that match specific characters
  (for example, JavaScript) or patterns (for example, NumberStringSymbol ...'
---

Par Dillion Megida

Les expressions régulières (également appelées RegEx ou RegExp) sont un moyen puissant d'analyser du texte. Avec RegEx, vous pouvez faire correspondre des chaînes à des points qui correspondent à des caractères spécifiques (par exemple, JavaScript) ou à des motifs (par exemple, NumberStringSymbol - 3a&).

La méthode `.replace` est utilisée sur les chaînes en JavaScript pour remplacer des parties de chaîne par des caractères. Elle est souvent utilisée comme suit :

```js
const str = 'JavaScript';
const newStr = str.replace("ava", "-");
console.log(newStr);
// J-Script
```

Comme vous pouvez le voir ci-dessus, la méthode replace accepte deux arguments : la chaîne à remplacer et par quoi la chaîne sera remplacée.

C'est là que **Regex** entre en jeu.

L'utilisation de `.replace` ci-dessus est limitée : les caractères à remplacer sont connus - "ava". Que faire si nous nous préoccupons d'un motif à la place ? Peut-être un nombre, deux lettres, et le mot "foo" ou trois symboles utilisés ensemble ?

La méthode `.replace` utilisée avec `RegEx` peut atteindre cet objectif. `RegEx` peut être utilisé efficacement pour recréer des motifs. Ainsi, en combinant cela avec `.replace`, nous pouvons remplacer des motifs et pas seulement des caractères exacts.

## Comment utiliser `RegEx` avec `.replace` en JavaScript

Pour utiliser RegEx, le premier argument de `replace` sera remplacé par la syntaxe regex, par exemple `/regex/`. Cette syntaxe sert de motif où toute partie de la chaîne qui correspondra sera remplacée par la nouvelle sous-chaîne.

Voici un exemple :

```js
// correspond à un nombre, quelques caractères et un autre nombre
const reg = /\d.*\d/
const str = "Java3foobar4Script"
const newStr = str.replace(reg, "-");
console.log(newStr);
// "Java-Script"
```

La chaîne `3foobar4` correspond au regex `/\d.*\d/`, donc elle est remplacée.

Que faire si nous voulions effectuer des remplacements à plusieurs endroits ?

`Regex` offre déjà cela avec le drapeau `g` (global), et le même peut être utilisé avec `replace`. Voici comment :

```js
const reg = /\d{3}/g
const str = "Java323Scr995ip4894545t";
const newStr = str.replace(reg, "");
console.log(newStr);
// JavaScrip5t
// 5 n'a pas passé le test :(
```

Le regex correspond aux parties de la chaîne qui sont exactement 3 chiffres consécutifs. `323` correspond, `995` correspond, `489` correspond, et `454` correspond. Mais le dernier `5` ne correspond pas au motif. 

Le résultat est que `JavaScrip5t` montre comment les motifs sont correctement correspondus et remplacés par la nouvelle sous-chaîne (une chaîne vide).

Le drapeau de casse - `i` peut également être utilisé. Cela signifie que vous pouvez remplacer des motifs insensibles à la casse. Voici comment il est utilisé :

```js
const reg1 = /\dA/
const reg2 = /\dA/i
const str = "Jav5ascript"
const newStr1 = str.replace(reg1, "--");
const newStr2 = str.replace(reg2, "--");
console.log(newStr1) // Jav5ascript
console.log(newStr2) // Jav--script
```

`..5a..` ne correspond pas à la première syntaxe car RegEx est par défaut sensible à la casse. Mais avec l'utilisation du drapeau `i`, comme vu dans la deuxième syntaxe, la chaîne est comme prévu - remplacée.

## Comment utiliser Split avec les expressions régulières

`split` utilise également `RegEx`. Ce qui signifie que vous pouvez diviser une chaîne non seulement à des sous-chaînes qui correspondent à des caractères exacts, mais aussi à des motifs.

Voici un rapide aperçu :

```js
const regex = /\d{2}a/;
const str = "Hello54 How 64aare you";
console.log(str.split(regex))
// ["Hello54 How ", "are you"]
```

La chaîne a été `split` à `64a` car cette sous-chaîne correspond au regex spécifié.

**Notez que** le drapeau global - `g` - dans `split` est sans importance, contrairement au drapeau `i` et aux autres drapeaux. Cela est dû au fait que `split` divise la chaîne aux plusieurs points où le regex correspond.

## Conclusion

`RegEx` rend le `replace` des chaînes en JavaScript plus efficace, puissant et amusant. 

Vous n'êtes pas seulement restreint à des caractères exacts mais à des motifs et à des remplacements multiples à la fois. Dans cet article, nous avons vu comment ils fonctionnent ensemble en utilisant quelques exemples.

À la vôtre pour RegEx ?