---
title: La coercition de type en JavaScript expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T19:29:59.000Z'
originalURL: https://freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7awmfn1lq2McPz8ggapndw.png
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La coercition de type en JavaScript expliquée
seo_desc: 'By Alexey Samoshkin

  Know your engines


  Weird things can happen in JavaScript

  [Edit 2/5/2018]: This post is now available in Russian. Claps to Serj Bulavyk for
  his efforts.

  Type coercion is the process of converting value from one type to another (suc...'
---

Par Alexey Samoshkin

#### Connaître vos moteurs

![Image](https://cdn-media-1.freecodecamp.org/images/1*7awmfn1lq2McPz8ggapndw.png)
_Des choses étranges peuvent arriver en JavaScript_

**[Modification 2/5/2018]** : Cet article est maintenant [disponible en russe](https://medium.com/@sergeybulavyk/%D0%BF%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%82%D0%B8%D0%BF%D0%BE%D0%B2-%D0%B2-javascript-35a15ddfc333). Applaudissements à [Serj Bulavyk](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/undefined) pour ses efforts.

La **coercition de type** est le processus de conversion d'une valeur d'un type à un autre (comme une chaîne en nombre, un objet en booléen, etc.). Tout type, qu'il soit primitif ou un objet, est un sujet valide pour la coercition de type. Pour rappel, les primitives sont : number, string, boolean, null, undefined + Symbol (ajouté dans ES6).

Comme exemple de coercition de type en pratique, regardez le [Tableau de comparaison JavaScript](https://dorey.github.io/JavaScript-Equality-Table/), qui montre comment l'opérateur d'égalité souple `==` se comporte pour différents types `a` et `b`. Cette matrice semble effrayante en raison de la coercition de type implicite que l'opérateur `==` effectue, et il est à peine possible de se souvenir de toutes ces combinaisons. Et vous n'avez pas à le faire — il suffit d'apprendre les principes sous-jacents de la coercition de type.

Cet article approfondit le fonctionnement de la coercition de type en JavaScript et vous armera des connaissances essentielles pour que vous puissiez expliquer en toute confiance ce que les expressions suivantes calculent. À la fin de l'article, je montrerai les réponses et les expliquerai.

```
true + false
12 / "6"
"number" + 15 + 3
15 + 3 + "number"
[1] > null
"foo" + + "bar"
'true' == true
false == 'false'
null == ''
!!"false" == !!"true"
['x'] == 'x'
[] + null + 1
[1,2,3] == [1,2,3]
{}+[]+{}+[1]
!+[]+[]+![]
new Date(0) - 0
new Date(0) + 0
```

Oui, cette liste est remplie de choses assez stupides que vous pouvez faire en tant que développeur. Dans 90 % des cas d'utilisation, il est préférable d'éviter la coercition de type implicite. Considérez cette liste comme un exercice d'apprentissage pour tester vos connaissances sur le fonctionnement de la coercition de type. Si vous vous ennuyez, vous pouvez trouver plus d'exemples sur [wtfjs.com](https://wtfjs.com/).

Au fait, parfois vous pourriez rencontrer de telles questions lors d'un entretien pour un poste de développeur JavaScript. Alors, continuez à lire 😉

### Coercition implicite vs. explicite

La coercition de type peut être explicite ou implicite.

Lorsque le développeur exprime l'intention de convertir entre les types en écrivant le code approprié, comme `Number(value)`, cela s'appelle **coercition de type explicite** (ou casting de type).

Puisque JavaScript est un langage faiblement typé, les valeurs peuvent également être converties automatiquement entre différents types, et cela s'appelle **coercition de type implicite**. Cela se produit généralement lorsque vous appliquez des opérateurs à des valeurs de différents types, comme `1 == null`, `2/'5'`, `null + new Date()`, ou cela peut être déclenché par le contexte environnant, comme avec `if (value) {...}`, où `value` est coercé en booléen.

Un opérateur qui ne déclenche pas de coercition de type implicite est `===`, qui est appelé l'opérateur d'égalité stricte. L'opérateur d'égalité souple `==`, en revanche, effectue à la fois la comparaison et la coercition de type si nécessaire.

La coercition de type implicite est une épée à double tranchant : c'est une grande source de frustration et de défauts, mais aussi un mécanisme utile qui nous permet d'écrire moins de code sans perdre la lisibilité.

### Trois types de conversion

La première règle à connaître est qu'il n'existe que trois types de conversion en JavaScript :

* en chaîne de caractères
* en booléen
* en nombre

Deuxièmement, la logique de conversion pour les primitives et les objets fonctionne différemment, mais les primitives et les objets ne peuvent être convertis que de ces trois manières.

Commençons d'abord par les primitives.

### Conversion en chaîne de caractères

Pour convertir explicitement des valeurs en chaîne de caractères, appliquez la fonction `String()`. La coercition implicite est déclenchée par l'opérateur binaire `+`, lorsqu'un opérande est une chaîne de caractères :

```
String(123) // explicite
123 + ''    // implicite
```

Toutes les valeurs primitives sont converties en chaînes de caractères naturellement comme vous pourriez vous y attendre :

```
String(123)                   // '123'
String(-12.3)                 // '-12.3'
String(null)                  // 'null'
String(undefined)             // 'undefined'
String(true)                  // 'true'
String(false)                 // 'false'
```

La conversion de Symbol est un peu délicate, car elle ne peut être convertie que de manière explicite, mais pas implicite. [Lire plus](https://leanpub.com/understandinges6/read/#leanpub-auto-symbol-coercion) sur les règles de coercition de `Symbol`.

```
String(Symbol('my symbol'))   // 'Symbol(my symbol)'
'' + Symbol('my symbol')      // TypeError est lancé
```

### Conversion en booléen

Pour convertir explicitement une valeur en booléen, appliquez la fonction `Boolean()`. La conversion implicite se produit dans un contexte logique ou est déclenchée par des opérateurs logiques (`||` `&&` `!`).

```
Boolean(2)          // explicite
if (2) { ... }      // implicite en raison du contexte logique
!!2                 // implicite en raison de l'opérateur logique
2 || 'hello'        // implicite en raison de l'opérateur logique
```

**Note** : Les opérateurs logiques tels que `||` et `&&` effectuent des conversions booléennes en interne, mais [retournent en réalité la valeur des opérandes originaux](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators#Logical_operators), même s'ils ne sont pas booléens.

```
// retourne le nombre 123, au lieu de retourner true
// 'hello' et 123 sont toujours coercés en booléen en interne pour calculer l'expression
let x = 'hello' && 123;   // x === 123
```

Dès qu'il n'y a que 2 résultats possibles pour la conversion booléenne : `true` ou `false`, il est plus facile de se souvenir de la liste des valeurs falsy.

```
Boolean('')           // false
Boolean(0)            // false     
Boolean(-0)           // false
Boolean(NaN)          // false
Boolean(null)         // false
Boolean(undefined)    // false
Boolean(false)        // false
```

Toute valeur qui n'est pas dans la liste est convertie en `true`, y compris les objets, fonctions, `Array`, `Date`, types définis par l'utilisateur, etc. Les Symboles sont des valeurs truthy. Les objets vides et les tableaux sont également des valeurs truthy :

```
Boolean({})             // true
Boolean([])             // true
Boolean(Symbol())       // true
!!Symbol()              // true
Boolean(function() {})  // true
```

### Conversion numérique

Pour une conversion explicite, appliquez simplement la fonction `Number()`, comme vous l'avez fait avec `Boolean()` et `String()`.

La conversion implicite est délicate, car elle est déclenchée dans plus de cas :

* opérateurs de comparaison (`>`, `<`, `<=`,`>=`)
* opérateurs bit à bit (`|` `&` `^` `~`)
* opérateurs arithmétiques (`-` `+` `*` `/` `%`). Notez que le `+` binaire ne déclenche pas de conversion numérique lorsqu'un opérande est une chaîne de caractères.
* opérateur unaire `+`
* opérateur d'égalité souple `==` (incl. `!=`). Notez que `==` ne déclenche pas de conversion numérique lorsque les deux opérandes sont des chaînes de caractères.

```
Number('123')   // explicite
+'123'          // implicite
123 != '456'    // implicite
4 > '5'         // implicite
5/null          // implicite
true | 0        // implicite
```

Voici comment les valeurs primitives sont converties en nombres :

```
Number(null)                   // 0
Number(undefined)              // NaN
Number(true)                   // 1
Number(false)                  // 0
Number(" 12 ")                 // 12
Number("-12.34")               // -12.34
Number("\n")                   // 0
Number(" 12s ")                // NaN
Number(123)                    // 123
```

Lors de la conversion d'une chaîne de caractères en nombre, le moteur supprime d'abord les espaces, les caractères `\n`, `\t` en début et en fin, retournant `NaN` si la chaîne rognée ne représente pas un nombre valide. Si la chaîne est vide, elle retourne `0`.

`null` et `undefined` sont traités différemment : `null` devient `0`, tandis que `undefined` devient `NaN`.

Les Symboles ne peuvent pas être convertis en nombre, ni explicitement ni implicitement. De plus, une `TypeError` est lancée, au lieu d'une conversion silencieuse en `NaN`, comme cela se produit pour `undefined`. Voir plus sur les règles de conversion des Symboles sur [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#Symbol_type_conversions).

```
Number(Symbol('my symbol'))    // TypeError est lancée
+Symbol('123')                 // TypeError est lancée
```

Il y a deux **règles spéciales** à retenir :

1. Lorsque vous appliquez `==` à `null` ou `undefined`, la conversion numérique ne se produit pas. `null` est égal uniquement à `null` ou `undefined`, et n'est pas égal à autre chose.

```
null == 0               // false, null n'est pas converti en 0
null == null            // true
undefined == undefined  // true
null == undefined       // true
```

2. NaN n'est égal à rien, même à lui-même :

```
if (value !== value) { console.log("nous traitons avec NaN ici") }
```

### Coercition de type pour les objets

Jusqu'à présent, nous avons examiné la coercition de type pour les valeurs primitives. Ce n'est pas très excitant.

En ce qui concerne les objets et lorsque le moteur rencontre une expression comme `[1] + [2,3]`, il doit d'abord convertir un objet en une valeur primitive, qui est ensuite convertie en type final. Et il y a toujours seulement trois types de conversion : numérique, chaîne de caractères et booléen.

Le cas le plus simple est la conversion booléenne : toute valeur non primitive est toujours coercée en `true`, peu importe si un objet ou un tableau est vide ou non.

Les objets sont convertis en primitives via la méthode interne `[[ToPrimitive]]`, qui est responsable à la fois de la conversion numérique et en chaîne de caractères.

Voici une pseudo-implémentation de la méthode `[[ToPrimitive]]` :

`[[ToPrimitive]]` est passé avec une valeur d'entrée et un type de conversion préféré : `Number` ou `String`. `preferredType` est facultatif.

Les conversions numérique et en chaîne de caractères utilisent deux méthodes de l'objet d'entrée : `valueOf` et `toString`. Ces deux méthodes sont déclarées sur `Object.prototype` et sont donc disponibles pour tous les types dérivés, tels que `Date`, `Array`, etc.

En général, l'algorithme est le suivant :

1. Si l'entrée est déjà une primitive, ne rien faire et la retourner.

2. Appeler `input.toString()`, si le résultat est une primitive, la retourner.

3. Appeler `input.valueOf()`, si le résultat est une primitive, la retourner.

4. Si ni `input.toString()` ni `input.valueOf()` ne donnent une primitive, lancer `TypeError`.

La conversion numérique appelle d'abord `valueOf` (3) avec un repli sur `toString` (2). La conversion en chaîne de caractères fait l'inverse : `toString` (2) suivi de `valueOf` (3).

La plupart des types intégrés n'ont pas de `valueOf`, ou ont un `valueOf` qui retourne l'objet lui-même, donc il est ignoré car ce n'est pas une primitive. C'est pourquoi les conversions numérique et en chaîne de caractères peuvent fonctionner de la même manière — les deux finissent par appeler `toString()`.

Différents opérateurs peuvent déclencher une conversion numérique ou en chaîne de caractères avec l'aide du paramètre `preferredType`. Mais il y a deux exceptions : l'égalité souple `==` et les opérateurs binaires `+` déclenchent des modes de conversion par défaut (`preferredType` n'est pas spécifié, ou est égal à `default`). Dans ce cas, la plupart des types intégrés supposent une conversion numérique par défaut, sauf `Date` qui effectue une conversion en chaîne de caractères.

Voici un exemple de comportement de conversion de `Date` :

Vous pouvez remplacer les méthodes `toString()` et `valueOf()` par défaut pour vous brancher sur la logique de conversion objet-vers-primitive.

Remarquez comment `obj + ''` retourne `'101'` en tant que chaîne de caractères. L'opérateur `+` déclenche un mode de conversion par défaut, et comme dit précédemment, `Object` suppose une conversion numérique par défaut, utilisant ainsi la méthode `valueOf()` en premier au lieu de `toString()`.

### Méthode ES6 Symbol.toPrimitive

Dans ES5, vous pouvez vous brancher sur la logique de conversion objet-vers-primitive en remplaçant les méthodes `toString` et `valueOf`.

Dans ES6, vous pouvez aller plus loin et remplacer complètement la routine interne `[[ToPrimitive]]` en implémentant la méthode `[Symbol.toPrimitive]` sur un objet.

### Exemples

Armés de la théorie, revenons maintenant à nos exemples :

```
true + false             // 1
12 / "6"                 // 2
"number" + 15 + 3        // 'number153'
15 + 3 + "number"        // '18number'
[1] > null               // true
"foo" + + "bar"          // 'fooNaN'
'true' == true           // false
false == 'false'         // false
null == ''               // false
!!"false" == !!"true"    // true
['x'] == 'x'             // true 
[] + null + 1            // 'null1'
[1,2,3] == [1,2,3]       // false
{}+[]+{}+[1]             // '0[object Object]1'
!+[]+[]+![]              // 'truefalse'
new Date(0) - 0          // 0
new Date(0) + 0          // 'Thu Jan 01 1970 02:00:00(EET)0'
```

Ci-dessous, vous pouvez trouver une explication pour chaque expression.

L'opérateur binaire `+` déclenche une conversion numérique pour `true` et `false`

```
true + false
==> 1 + 0
==> 1
```

L'opérateur de division arithmétique `/` déclenche une conversion numérique pour la chaîne `'6'` :

```
12 / '6'
==> 12 / 6
==>> 2
```

L'opérateur `+` a une associativité de gauche à droite, donc l'expression `"number" + 15` s'exécute en premier. Puisqu'un opérande est une chaîne de caractères, l'opérateur `+` déclenche une conversion en chaîne de caractères pour le nombre `15`. À la deuxième étape, l'expression `"number15" + 3` est évaluée de manière similaire.

```
"number" + 15 + 3 
==> "number15" + 3 
==> "number153"
```

L'expression `15 + 3` est évaluée en premier. Pas besoin de coercition du tout, puisque les deux opérandes sont des nombres. À la deuxième étape, l'expression `18 + 'number'` est évaluée, et puisque un opérande est une chaîne de caractères, elle déclenche une conversion en chaîne de caractères.

```
15 + 3 + "number" 
==> 18 + "number" 
==> "18number"
```

L'opérateur de comparaison `>` déclenche une conversion numérique pour `[1]` et `null`.

```
[1] > null
==> '1' > 0
==> 1 > 0
==> true
```

L'opérateur unaire `+` a une priorité plus élevée que l'opérateur binaire `+`. Donc l'expression `+'bar'` est évaluée en premier. Le plus unaire déclenche une conversion numérique pour la chaîne `'bar'`. Puisque la chaîne ne représente pas un nombre valide, le résultat est `NaN`. À la deuxième étape, l'expression `'foo' + NaN` est évaluée.

```
"foo" + + "bar" 
==> "foo" + (+"bar") 
==> "foo" + NaN 
==> "fooNaN"
```

L'opérateur `==` déclenche une conversion numérique, la chaîne `'true'` est convertie en NaN, le booléen `true` est converti en 1.

```
'true' == true
==> NaN == 1
==> false

false == 'false'   
==> 0 == NaN
==> false
```

`==` déclenche généralement une conversion numérique, mais ce n'est pas le cas avec `null`. `null` est égal uniquement à `null` ou `undefined`, et n'est pas égal à autre chose.

```
null == ''
==> false
```

L'opérateur `!!` convertit les chaînes `'true'` et `'false'` en booléen `true`, puisque ce sont des chaînes non vides. Ensuite, `==` vérifie simplement l'égalité de deux booléens `true` sans aucune coercition.

```
!!"false" == !!"true"  
==> true == true
==> true
```

L'opérateur `==` déclenche une conversion numérique pour un tableau. La méthode `valueOf()` du tableau retourne le tableau lui-même, et est ignorée car ce n'est pas une primitive. La méthode `toString()` du tableau convertit `['x']` en simple chaîne de caractères `'x'`.

```
['x'] == 'x'  
==> 'x' == 'x'
==>  true
```

L'opérateur `+` déclenche une conversion numérique pour `[]`. La méthode `valueOf()` du tableau est ignorée, car elle retourne le tableau lui-même, qui est non primitif. La méthode `toString` du tableau retourne une chaîne vide.

À la deuxième étape, l'expression `'' + null + 1` est évaluée.

```
[] + null + 1  
==>  '' + null + 1  
==>  'null' + 1  
==> 'null1'
```

Les opérateurs logiques `||` et `&&` coercissent les opérandes en booléen, mais retournent les opérandes originaux (non booléens). `0` est falsy, tandis que `'0'` est truthy, car c'est une chaîne non vide. `{}` objet vide est également truthy.

```
0 || "0" && {}  
==>  (0 || "0") && {}
==> (false || true) && true  // en interne
==> "0" && {}
==> true && true             // en interne
==> {}
```

Aucune coercition n'est nécessaire car les deux opérandes sont du même type. Puisque `==` vérifie l'identité de l'objet (et non l'égalité de l'objet) et que les deux tableaux sont deux instances différentes, le résultat est `false`.

```
[1,2,3] == [1,2,3]
==>  false
```

Tous les opérandes sont des valeurs non primitives, donc `+` commence par le plus à gauche en déclenchant une conversion numérique. Les méthodes `valueOf` des `Object` et des `Array` retournent l'objet lui-même, donc il est ignoré. `toString()` est utilisé comme solution de repli. Le truc ici est que le premier `{}` n'est pas considéré comme un littéral d'objet, mais plutôt comme une déclaration d'instruction de bloc, donc il est ignoré. L'évaluation commence avec l'expression `+[]` suivante, qui est convertie en une chaîne vide via la méthode `toString()` puis en `0`.

```
{}+[]+{}+[1]
==> +[]+{}+[1]
==> 0 + {} + [1]
==> 0 + '[object Object]' + [1]
==> '0[object Object]' + [1]
==> '0[object Object]' + '1'
==> '0[object Object]1'
```

Celui-ci est mieux expliqué étape par étape selon la priorité des opérateurs.

```
!+[]+[]+![]  
==> (!+[]) + [] + (![])
==> !0 + [] + false
==> true + [] + false
==> true + '' + false
==> 'truefalse'
```

L'opérateur `-` déclenche une conversion numérique pour `Date`. `Date.valueOf()` retourne le nombre de millisecondes depuis l'époque Unix.

```
new Date(0) - 0
==> 0 - 0
==> 0
```

L'opérateur `+` déclenche une conversion par défaut. Date suppose une conversion en chaîne de caractères comme conversion par défaut, donc la méthode `toString()` est utilisée, plutôt que `valueOf()`.

```
new Date(0) + 0
==> 'Thu Jan 01 1970 02:00:00 GMT+0200 (EET)' + 0
==> 'Thu Jan 01 1970 02:00:00 GMT+0200 (EET)0'
```

### Ressources

Je tiens vraiment à recommander l'excellent livre « [Understanding ES6](https://leanpub.com/understandinges6) » écrit par [Nicholas C. Zakas](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/undefined). C'est une excellente ressource d'apprentissage pour ES6, pas trop de haut niveau, et ne creuse pas trop dans les détails internes.

Et voici un bon livre sur ES5 uniquement - [SpeakingJS](http://speakingjs.com/) écrit par [Axel Rauschmayer](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/undefined).

(**Russe**) Современный учебник Javascript — [https://learn.javascript.ru/](https://learn.javascript.ru/). En particulier, [ces](https://learn.javascript.ru/object-conversion) [deux](https://learn.javascript.ru/types-conversion) pages sur la coercition de type.

Tableau de comparaison JavaScript — [https://dorey.github.io/JavaScript-Equality-Table/](https://dorey.github.io/JavaScript-Equality-Table/)

wtfjs — un petit blog de code sur ce langage que nous aimons malgré tout ce qu'il nous donne à détester — [https://wtfjs.com/](https://wtfjs.com/)