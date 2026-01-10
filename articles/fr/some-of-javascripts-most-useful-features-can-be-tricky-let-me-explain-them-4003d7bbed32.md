---
title: Symboles JavaScript, Itérateurs, Générateurs, Async/Await et Itérateurs Asynchrones
  — Tout Expliqué Simplement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-11T23:16:55.000Z'
originalURL: https://freecodecamp.org/news/some-of-javascripts-most-useful-features-can-be-tricky-let-me-explain-them-4003d7bbed32
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UovxjrPZdmpuy_P4w-5I5A.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Symboles JavaScript, Itérateurs, Générateurs, Async/Await et Itérateurs
  Asynchrones — Tout Expliqué Simplement
seo_desc: 'By rajaraodv

  Some JavaScript (ECMAScript) features are easier to understand than others. Generators
  look weird — like pointers in C/C++. Symbols manage to look like both primitives
  and objects at the same time.

  These features are all inter-related an...'
---

Par rajaraodv

Certaines fonctionnalités de JavaScript (ECMAScript) sont plus faciles à comprendre que d'autres. Les `Générateurs` semblent étranges — comme les pointeurs en C/C++. Les `Symboles` parviennent à ressembler à la fois à des primitives et à des objets.

**Toutes ces fonctionnalités sont inter-reliées et se construisent les unes sur les autres. Vous ne pouvez donc pas comprendre une chose sans comprendre l'autre.**

Dans cet article, je vais couvrir les `symboles`, les `symboles globaux`, les `itérateurs`, les `itérables`, les `générateurs`, `async/await` et les `itérateurs asynchrones`. **Je vais expliquer « pourquoi » ils existent en premier lieu et montrer comment ils fonctionnent avec quelques exemples utiles.**

> Il s'agit d'un sujet relativement avancé, mais ce n'est pas de la science-fiction. Cet article devrait vous donner une très bonne compréhension de tous ces concepts.

**D'accord, commençons.?**

![Image](https://cdn-media-1.freecodecamp.org/images/HBiVhsE9-rPJxFPNFdN5-5ZnnZSQmzN89X7H)

### Symboles

En ES2015, un nouveau (6ème) type de données appelé `symbole` a été créé.

#### POURQUOI?

Les trois principales raisons étaient :

#### Raison #1 — Ajouter de nouvelles fonctionnalités principales avec une compatibilité ascendante

Les développeurs JavaScript et le comité ECMAScript ([TC39](http://ecma-international.org/memento/TC39.htm)) avaient besoin d'un moyen d'ajouter de nouvelles propriétés d'objet sans casser les méthodes existantes comme les boucles `for in` ou les méthodes JavaScript comme `Object.keys`.

Par exemple, si j'ai un objet, `var myObject = {firstName:'raja', lastName:'rao'}` et si j'exécute `Object.keys(myObject)`, il retournera `[firstName, lastName]`.

Maintenant, si nous ajoutons une autre propriété, disons `newProperty` à `myObject`, et si vous exécutez `Object.keys(myObject)`, il **devrait** **toujours** retourner les anciennes valeurs (c'est-à-dire, d'une manière ou d'une autre, faire en sorte qu'il ignore la nouvelle propriété `newProperty`), et montrer simplement `[firstName, lastName]` — et non `[firstName, lastName, newProperty]`. Comment faire cela ?

Nous ne pouvions pas vraiment faire cela auparavant, donc un nouveau type de données appelé `Symboles` a été créé.

Si vous ajoutez `newProperty` en tant que symbole, alors `Object.keys(myObject)` ignorera cela (car il ne le connaît pas), et retournera toujours `[firstName, lastName]` !

#### Raison #2 — Éviter les collisions de noms

Ils voulaient également garder ces propriétés uniques. De cette façon, ils peuvent continuer à ajouter de nouvelles propriétés (et vous pouvez ajouter des propriétés d'objet) à l'objet global sans se soucier des collisions de noms.

Par exemple, supposons que vous avez un objet où vous ajoutez un `toUpperCase` personnalisé au `Array.prototype` global.

Maintenant, imaginez que vous chargez une autre bibliothèque (ou que ES2019 est sorti) et qu'elle avait une version différente de `Array.prototype.toUpperCase`. Alors votre fonction pourrait ne plus fonctionner à cause de la collision de noms.

![Image](https://cdn-media-1.freecodecamp.org/images/J6B2ibbhbGxk4KQq4j4CYL6zVTWXyXL6-B4o)

Alors, comment résoudre cette collision de noms que vous ne connaissez peut-être pas ? C'est là que les `Symboles` interviennent. Ils créent des valeurs uniques en interne qui vous permettent de créer des propriétés sans vous soucier des collisions de noms.

#### Raison #3 — Permettre des hooks aux méthodes principales via les Symboles « bien connus »

Supposons que vous voulez qu'une fonction principale, disons `String.prototype.search`, appelle votre fonction personnalisée. C'est-à-dire que `'somestring'.search(myObject);` devrait appeler la fonction de recherche de `myObject` et passer `'somestring'` comme paramètre ! Comment faire cela ?

C'est là qu'ES2015 a introduit un ensemble de symboles globaux appelés symboles « bien connus ». Et tant que **votre** objet a l'un de ces symboles comme propriété, vous pouvez rediriger les fonctions principales pour qu'elles appellent votre fonction !

Nous ne pouvons pas en parler beaucoup maintenant, donc je vais entrer dans tous les détails un peu plus tard dans cet article. Mais d'abord, apprenons comment les Symboles fonctionnent réellement.

#### Création de Symboles

Vous pouvez créer un symbole en appelant une fonction/objet global appelé `Symbol`. Cette fonction retourne une valeur de type de données `symbole`.

![Image](https://cdn-media-1.freecodecamp.org/images/clCoLqejtYU7HEECtCfze7I8Al5voKei--8-)

**Note :** Les symboles peuvent sembler des objets parce qu'ils ont des méthodes, mais ils n'en sont pas — ce sont des primitives. Vous pouvez les considérer comme des objets « spéciaux » qui ont certaines similitudes avec les objets réguliers, mais qui ne se comportent pas comme des objets réguliers.

Par exemple : Les symboles ont des méthodes comme les objets, mais contrairement aux objets, ils sont immuables et uniques.

#### Les symboles ne peuvent pas être créés par le mot-clé « new »

Parce que les symboles ne sont pas des objets et que le mot-clé `new` est censé retourner un objet, nous ne pouvons pas utiliser `new` pour retourner un type de données `symboles`.

```
var mySymbol = new Symbol(); // lance une erreur
```

#### Les symboles ont une « description »

Les symboles peuvent avoir une description — c'est juste pour des raisons de journalisation.

```
// la variable mySymbol contient maintenant une valeur « symbole » unique
// sa description est « some text »
const mySymbol = Symbol('some text');
```

#### Les symboles sont uniques

```
const mySymbol1 = Symbol('some text');
const mySymbol2 = Symbol('some text');
mySymbol1 == mySymbol2 // false
```

#### Les symboles se comportent comme un singleton si nous utilisons la méthode « Symbol.for »

Au lieu de créer un `symbole` via `Symbol()`, vous pouvez le créer via `Symbol.for(<clé>)`. Cela prend une « clé » (chaîne) pour créer un symbole. Et si un symbole avec cette clé existe déjà, il retourne simplement l'ancien symbole ! Il se comporte donc comme un singleton si nous utilisons la méthode `Symbol.for`.

```
var mySymbol1 = Symbol.for('some key'); // crée un nouveau symbole
var mySymbol2 = Symbol.for('some key'); // **retourne le même symbole
mySymbol1 == mySymbol2 // true
```

La vraie raison d'utiliser `.for` est de créer un symbole à un endroit et d'accéder au même symbole depuis un autre endroit.

**Attention :** `Symbol.for` rendra le symbole non unique dans le sens où vous finirez par écraser les valeurs si les **clés** sont les mêmes ! Essayez donc d'éviter cela si possible !

#### « Description » du symbole versus « clé »

Juste pour clarifier les choses, si vous n'utilisez pas `Symbol.for`, alors les symboles sont uniques. Cependant, si vous l'utilisez, alors si votre `clé` n'est pas unique, les symboles retournés ne seront pas non plus uniques.

![Image](https://cdn-media-1.freecodecamp.org/images/8zbLMllXK82Hk5TjWO0xZgSm8gWlTIp6QAKu)

#### Les symboles peuvent être une clé de propriété d'objet

C'est une chose très unique à propos des symboles — et aussi très déroutante. Bien qu'ils semblent être un objet, ils sont des primitives. Et nous pouvons attacher un symbole à un objet en tant que clé de propriété, tout comme une chaîne.

En fait, c'est l'une des principales façons d'utiliser les symboles — en tant que propriétés d'objet !

![Image](https://cdn-media-1.freecodecamp.org/images/R-dqw1eSSUtKqHL4rqpLOlPDtjTtpclIHSty)

**Note :** Les propriétés d'objet qui sont des symboles sont connues sous le nom de « propriétés clés ».

#### Opérateur crochets vs opérateur point

Vous ne pouvez pas utiliser un opérateur point car les opérateurs point ne fonctionnent que sur les propriétés de chaîne, vous devez donc utiliser un opérateur crochets.

![Image](https://cdn-media-1.freecodecamp.org/images/hfq5DSd88rGXqlUpyqsJn258KvQu3CD-LniM)

### 3 principales raisons d'utiliser les Symboles — un rappel

Revisitons les trois principales raisons maintenant que nous savons comment les symboles fonctionnent.

#### **Raison #1 — Les symboles sont invisibles pour les boucles et autres méthodes**

La boucle for-in dans l'exemple ci-dessous parcourt un objet `obj` mais elle ne connaît pas (ou ignore) `prop3` et `prop4` parce qu'ils sont des symboles.

![Image](https://cdn-media-1.freecodecamp.org/images/FO2t8FHLz9eRviM4xBs8wLk4SOxR1u7ne31x)

Ci-dessous un autre exemple où `Object.keys` et `Object.getOwnPropertyNames` ignorent les noms de propriétés qui sont des symboles.

![Image](https://cdn-media-1.freecodecamp.org/images/OpEPnJHKdDXt3332AS27me9YBMr3Tx6Efyj-)

#### **Raison #2 — Les symboles sont uniques**

Supposons que vous voulez une fonctionnalité appelée `Array.prototype.includes` sur l'objet global `Array`. Elle entrera en collision avec la méthode `includes` par défaut que JavaScript (ES2018) fournit. Comment l'ajouter sans collision ?

Tout d'abord, créez une variable avec le nom approprié `includes` et attribuez-lui un symbole. Ensuite, ajoutez cette variable (maintenant un symbole) au `Array` global en utilisant la notation crochets. Attribuez n'importe quelle fonction que vous voulez.

Enfin, appelez cette fonction en utilisant la notation crochets. Mais notez que vous devez passer le symbole réel dans les crochets comme : `arr[includes]()` et non comme une chaîne.

![Image](https://cdn-media-1.freecodecamp.org/images/lJo8y-zLg8TZtPXBfyVEmtJSJ3yb6gR7GFoO)

#### Raison #3. Symboles bien connus (c'est-à-dire symboles « globaux »)

Par défaut, JavaScript crée automatiquement un ensemble de variables de symboles et les attribue à l'objet global `Symbol` (oui, le même `Symbol()` que nous utilisons pour créer des symboles).

Dans ECMAScript 2015, ces symboles sont ensuite ajoutés aux méthodes principales telles que `String.prototype.search` et `String.prototype.replace` des objets principaux tels que les tableaux et les chaînes.

Quelques exemples de ces symboles sont : `Symbol.match`, `Symbol.replace`, `Symbol.search`, `Symbol.iterator` et `Symbol.split`.

Puisque ces symboles globaux sont globaux et exposés, nous pouvons faire en sorte que les méthodes principales appellent **nos** fonctions personnalisées au lieu des fonctions internes.

#### Un exemple : `_Symbol.search_`

Par exemple, la méthode publique `String.prototype.search` de l'objet String recherche une expression régulière ou une chaîne et retourne l'index si elle est trouvée.

![Image](https://cdn-media-1.freecodecamp.org/images/69xn6K7tJAA6eJeKkEi8n-bRebGfM7fphoRf)

En ES2015, il vérifie d'abord si la méthode `Symbol.search` est implémentée dans l'expression régulière de la requête (objet RegExp). Si c'est le cas, il appelle cette fonction et délègue le travail à celle-ci. Et les objets principaux comme RegExp implémentent le symbole `Symbol.search` qui fait réellement le travail.

#### Fonctionnement interne de Symbol.search (COMPORTEMENT PAR DÉFAUT)

1. Analyser `'rajarao'.search('rao');`
2. Convertir « rajarao » en objet String `new String('rajarao')`
3. Convertir « rao » en objet RegExp `new Regexp('rao')`
4. Appeler la méthode `search` de l'objet String « rajarao ».
5. La méthode `search` appelle internement la méthode `Symbol.search` sur l'objet « rao » (délègue la recherche à l'objet « rao ») et passe « rajarao ». Quelque chose comme ceci : `"rao"[Symbol.search]("rajarao")`
6. `"rao"[Symbol.search]("rajarao")` retourne le résultat de l'index comme `4` à la fonction `search` et finalement, `search` retourne `4` à notre code.

Le pseudo-code ci-dessous montre comment le code fonctionne internement :

![Image](https://cdn-media-1.freecodecamp.org/images/eRX3vzKog8jhzxjyMoOMxEyq4-OxrmrxPcYq)

Mais la beauté est que vous n'avez plus à passer RegExp. Vous pouvez passer n'importe quel objet personnalisé qui implémente `Symbol.search` et retourner ce que vous voulez et cela continuera à fonctionner.

Jetons un coup d'œil.

#### Personnalisation de la méthode String.search pour appeler notre fonction

L'exemple ci-dessous montre comment nous pouvons faire en sorte que `String.prototype.search` appelle la fonction de recherche de notre classe `Product` — grâce au symbole global `Symbol.search`.

![Image](https://cdn-media-1.freecodecamp.org/images/kcc8eq6pH5DRkxRTMDTIkCPJpnr4zgrWVESY)

#### Fonctionnement interne de Symbol.search (COMPORTEMENT PERSONNALISÉ)

1. Analyser `'barsoap'.search(soapObj);`
2. Convertir « barsoap » en objet String `new String('barsoap')`
3. Puisque `soapObj` est déjà un objet, ne pas faire de conversion
4. Appeler la méthode `search` de l'objet String « barsoap ».
5. La méthode `search` appelle internement la méthode `Symbol.search` sur l'objet « `soapObj` » (c'est-à-dire qu'elle délègue la recherche à l'objet « `soapObj` ») et passe « barsoap ». Quelque chose comme ceci : `soapObj[Symbol.search]('barsoap')`
6. `soapObj[Symbol.search]('barsoap')` retourne le résultat de l'index comme `FOUND` à la fonction `search` et finalement, `search` retourne `FOUND` à notre code.

Espérons que vous avez maintenant une bonne compréhension des Symboles.

D'accord, passons aux Itérateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/kEHK8PEgmOHaS6VUgG23msLpi8X8sMxPQsbV)

### Itérateurs et Itérables

#### POURQUOI?

Dans presque toutes nos applications, nous traitons constamment des listes de données et nous devons afficher ces données dans le navigateur ou l'application mobile. Typiquement, nous écrivons nos propres méthodes pour stocker et extraire ces données.

Mais le problème est que nous avons déjà des méthodes standard comme la boucle `for-of` et l'opérateur de propagation (`...`) pour extraire des collections de données à partir d'objets standard comme les tableaux, les chaînes et les maps. Pourquoi ne pouvons-nous pas utiliser ces méthodes standard pour notre objet également ?

Dans l'exemple ci-dessous, nous ne pouvons pas utiliser une boucle for-of ou un opérateur de propagation pour extraire des données de notre classe `Users`. Nous devons utiliser une méthode personnalisée `get`.

![Image](https://cdn-media-1.freecodecamp.org/images/0ZUUfwRblzYmzhfuh9ziyANRNRgzNefSRVQA)

Mais ne serait-il pas agréable de pouvoir utiliser ces méthodes existantes dans nos propres objets ? Pour y parvenir, nous devons avoir des règles que tous les développeurs peuvent suivre et rendre leurs objets compatibles avec les méthodes existantes.

Si elles suivent ces règles pour extraire des données de leurs objets, alors de tels objets sont appelés « itérables ».

Les règles sont :

1. L'objet/classe principal doit stocker certaines données.
2. L'objet/classe principal doit avoir le symbole global « bien connu » `symbol.iterator` comme propriété qui implémente une méthode spécifique selon les règles #3 à #6.
3. Cette méthode `symbol.iterator` doit retourner un autre objet — un objet « itérateur ».
4. Cet objet « itérateur » doit avoir une méthode appelée méthode `next`.
5. La méthode `next` doit avoir accès aux données stockées dans la règle #1.
6. Et si nous appelons `iteratorObj.next()`, elle doit retourner certaines données stockées de la règle #1 soit au format `{value:<stored data>, **done:** false}` si elle veut retourner plus de valeurs, soit au format `{**done:** true}` si elle ne veut pas retourner de données supplémentaires.

Si toutes ces 6 règles sont suivies, alors l'objet principal est appelé un « **itérable** » de la règle #1. L'objet qu'il retourne est appelé un « **itérateur** ».

Jetons un coup d'œil à la façon dont nous pouvons rendre notre objet `Users` et itérable :

![Image](https://cdn-media-1.freecodecamp.org/images/NCcsb6xvxscZ24U7swkutqwjjFfi4YYHECd-)
_Veuillez cliquer pour zoomer_

**Note importante** : Si nous passons un `itérable` (`allUsers`) à une boucle `for-of` ou à un opérateur de propagation, ils appellent internement `<itérable>[Symbol.iterator]()` pour obtenir l'itérateur (comme `allUsersIterator`) et utilisent ensuite l'itérateur pour extraire les données.

En quelque sorte, toutes ces règles sont là pour avoir une manière standard de retourner un objet `itérateur`.

![Image](https://cdn-media-1.freecodecamp.org/images/mPZxgsP8mMLNhJIqiXGF5yFPJ5fdmeJk9dyG)

### Fonctions génératrices

#### **POURQUOI?**

Il y a deux raisons principales :

1. fournir une abstraction de plus haut niveau aux itérables
2. Fournir de nouveaux flux de contrôle pour aider avec des choses comme « l'enfer des callbacks ».

Examinons-les en détail.

#### RAISON #1 — Un wrapper pour les itérables

Au lieu de rendre notre classe/objet un `itérable` en suivant toutes ces règles, nous pouvons simplement créer quelque chose appelé une méthode « Générateur » pour simplifier les choses.

Voici quelques-uns des principaux points concernant les générateurs :

1. Les méthodes génératrices ont une nouvelle syntaxe `*<monGénérateur>` à l'intérieur d'une classe, et les fonctions génératrices ont la syntaxe `function * monGénérateur(){}`.
2. L'appel des générateurs `monGénérateur()` retourne un objet `générateur` qui implémente également le protocole `iterator` (règles), donc nous pouvons utiliser cela comme une valeur de retour `iterator` prête à l'emploi.
3. Les générateurs utilisent une instruction spéciale `yield` pour retourner des données.
4. Les instructions `yield` gardent une trace des appels précédents et continuent simplement là où elles se sont arrêtées.
5. Si vous utilisez `yield` à l'intérieur d'une boucle, il ne s'exécutera qu'une fois chaque fois que nous appelons la méthode `next()` sur l'itérateur.

#### **Exemple 1 :**

Le code ci-dessous vous montre comment vous pouvez utiliser une méthode génératrice (`*getIterator()`) au lieu d'utiliser la méthode `Symbol.iterator` et d'implémenter la méthode `next` qui suit toutes les règles.

![Image](https://cdn-media-1.freecodecamp.org/images/pZfUjKv5veWYeQQ1zskNUzsL-mEJZ1cGrnko)
_Utilisation des générateurs à l'intérieur d'une classe_

#### **Exemple 2 :**

Vous pouvez simplifier encore plus. Faites d'une fonction un générateur (avec la syntaxe *), et utilisez `yield` pour retourner des valeurs une à la fois comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/nYHrw83GR5EF0jPwR3p-0bbkwmBXJuQJB8ER)
_Utilisation des générateurs directement en tant que fonctions_

**Note importante** : Bien que dans les exemples ci-dessus, j'utilise le mot « itérateur » pour représenter `allUsers`, c'est vraiment un objet `générateur`.

L'objet générateur a des méthodes comme `throw` et `return` en plus de la méthode `next` ! Mais à des fins pratiques, nous pouvons utiliser l'objet retourné simplement comme « itérateur ».

#### RAISON #2 — Fournir de meilleurs et nouveaux flux de contrôle

Aider à fournir de nouveaux flux de contrôle qui nous aident à écrire des programmes de nouvelles manières et à résoudre des problèmes comme « l'enfer des callbacks ».

Remarquez que contrairement à une fonction normale, la fonction génératrice peut `yield` (stocker l'`état` de la fonction et la valeur de `return`) et aussi être prête à prendre des valeurs d'entrée supplémentaires au point où elle a yield.

Dans l'image ci-dessous, chaque fois qu'elle voit `yield`, elle peut retourner la valeur. Vous pouvez utiliser `generator.next('some new value')` et passer la nouvelle valeur au point où elle a yield.

![Image](https://cdn-media-1.freecodecamp.org/images/y3hrnT63qXkWewIj4rWbfocef-Mu8TeY02gi)
_Fonction normale vs fonction génératrice_

L'exemple ci-dessous montre en termes plus concrets comment fonctionne le flux de contrôle :

![Image](https://cdn-media-1.freecodecamp.org/images/JlyaniqPAd5mszB37kq3YbGhELKpdbsTm11c)
_Flux de contrôle du générateur_

### Syntaxe et utilisation des générateurs

Les fonctions génératrices peuvent être utilisées de la manière suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/xNnkTFsqv23fBgya2lKmTyUb-COXeU4SCVIj)

#### **Nous pouvons avoir plus de code après « yield » (contrairement à l'instruction « return »)**

Tout comme le mot-clé `return`, le mot-clé `yield` retourne également la valeur — mais il nous permet d'avoir du code après le yield !

![Image](https://cdn-media-1.freecodecamp.org/images/w9dKtBLs7v3t5sLre8jpFmQ3TCgEWLTN99uj)

#### Vous pouvez avoir plusieurs yields

![Image](https://cdn-media-1.freecodecamp.org/images/RtoVwrmiWrKVGZOnXX5MEqedj2IqllxMmeZW)
_vous pouvez avoir plusieurs instructions yield_

#### Envoyer des valeurs dans les deux sens aux générateurs via la méthode « next »

La méthode `next` des itérateurs peut également passer des valeurs dans le générateur comme montré ci-dessous.

En fait, cette fonctionnalité permet aux générateurs d'éliminer « l'enfer des callbacks ». Vous en apprendrez plus à ce sujet dans un instant.

Cette fonctionnalité est également utilisée intensivement dans des bibliothèques comme [redux-saga](https://redux-saga.js.org/).

Dans l'exemple ci-dessous, nous appelons l'itérateur avec un appel `next()` vide pour obtenir la question. Ensuite, nous passons `23` comme valeur lorsque nous appelons `next(23)` la deuxième fois.

![Image](https://cdn-media-1.freecodecamp.org/images/aSFH1y8bOkNPhzJgN4KFZH3g5QGTxwGIifIs)
_Passer une valeur au générateur depuis l'extérieur via « next »_

#### Les générateurs aident à éliminer « l'enfer des callbacks »

Vous savez que nous tombons dans [l'enfer des callbacks](http://callbackhell.com/) si nous avons plusieurs appels asynchrones.

L'exemple ci-dessous montre comment des bibliothèques comme « [co](https://github.com/tj/co) » utilisent la fonctionnalité de générateur qui nous permet de passer une valeur via la méthode `next` pour nous aider à écrire du code asynchrone de manière synchrone.

Remarquez comment la fonction `co` passe le résultat de la promesse au générateur via `next(result)` dans l'étape #5 et l'étape #10.

![Image](https://cdn-media-1.freecodecamp.org/images/DJH7bZWmgDAmQMiecWmHXsPjKN9aiIzC0BGB)
_Explication étape par étape des bibliothèques comme « co » qui utilisent « next(<someval>) »_

D'accord, passons à async/await.

![Image](https://cdn-media-1.freecodecamp.org/images/q2ozY1fqYuvuRBnzmJZSxRDH4e1FTUhF254H)

### ASYNC/AWAIT

#### **POURQUOI?**

Comme vous l'avez vu précédemment, les générateurs peuvent aider à éliminer « l'enfer des callbacks », mais vous avez besoin d'une bibliothèque tierce comme `co` pour que cela se produise. Mais « l'enfer des callbacks » est un problème si important que le comité ECMAScript a décidé de créer un wrapper juste pour cet aspect des générateurs et a sorti les nouveaux mots-clés `async/await`.

Les différences entre les générateurs et Async/Await sont :

1. async/await utilise `await` au lieu de `yield`.
2. `await` ne fonctionne qu'avec les promesses.
3. Au lieu de `function*`, il utilise le mot-clé `async function`.

Ainsi, `async/await` est essentiellement un sous-ensemble des générateurs et a une nouvelle syntaxe sucrée.

Le mot-clé `async` indique au compilateur JavaScript de traiter la fonction différemment. Le compilateur met en pause chaque fois qu'il atteint le mot-clé `await` dans cette fonction. Il suppose que l'expression après `await` retourne une promesse et attend que la promesse soit résolue ou rejetée avant de continuer.

Dans l'exemple ci-dessous, la fonction `getAmount` appelle deux fonctions asynchrones `getUser` et `getBankBalance`. Nous pouvons faire cela dans une promesse, mais l'utilisation de `async await` est plus élégante et simple.

![Image](https://cdn-media-1.freecodecamp.org/images/3vUZj-y4RZb-LV2gDU2jNeL7n02zjUH9zbos)

![Image](https://cdn-media-1.freecodecamp.org/images/m9Ky899WlWX2Soj6vEleyTNOHt0LGVSEcZF7)

### ITÉRATEURS ASYNCHRONES

#### **POURQUOI?**

C'est un scénario assez courant où nous devons appeler des fonctions asynchrones dans une boucle. Ainsi, dans ES2018 (proposition finalisée), le comité TC39 a introduit un nouveau symbole `Symbol.asyncIterator` ainsi qu'une nouvelle construction `for-await-of` pour nous aider à boucler facilement sur des fonctions asynchrones.

La principale différence entre les objets itérateurs réguliers et les itérateurs asynchrones est la suivante :

#### **Objet itérateur**

1. La méthode `next()` de l'objet itérateur retourne une valeur comme `{value: 'some val', done: false}`
2. Utilisation : `iterator.next() //{value: 'some val', done: false}`

#### **Objet itérateur asynchrone**

1. La méthode next() de l'objet itérateur asynchrone **retourne une promesse** qui se résout plus tard en quelque chose comme `{value: 'some val', done: false}`
2. Utilisation : `iterator.next().then(({ value, done })=> {//{value: 'some val', done: false}}`

L'exemple ci-dessous montre comment fonctionne `for-await-of` et comment vous pouvez l'utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/vgX-wE-V4P3j1f6v6qQv4FERtQXZYAR7-9PC)
_for-await-of (ES2018)_

### RÉSUMÉ

**Symboles** — fournissent un type de données globalement unique. Vous les utilisez principalement comme propriétés d'objet pour ajouter de nouveaux comportements afin de ne pas casser les méthodes standard comme `Object.keys` et les boucles `for-in`.

**Symboles bien connus** — sont des symboles générés automatiquement par JavaScript et peuvent être utilisés pour implémenter des méthodes principales dans nos objets personnalisés.

**Itérables** — sont des objets qui stockent une collection de données et suivent des règles spécifiques afin que nous puissions utiliser la boucle standard `for-of` et les opérateurs de propagation `...` pour extraire des données de leur intérieur.

**Itérateurs** — sont retournés par les itérables et ont la méthode `next` — c'est ce qui extrait réellement les données d'un `itérable`.

**Générateurs** — fournissent une abstraction de plus haut niveau aux itérables. Ils fournissent également de nouveaux flux de contrôle qui peuvent résoudre des problèmes comme l'enfer des callbacks et fournir des blocs de construction pour des choses comme `Async/Await`.

**Async/Await** — fournit une abstraction de plus haut niveau aux générateurs afin de résoudre spécifiquement le problème de l'enfer des callbacks.

**Itérateurs asynchrones** — une toute nouvelle fonctionnalité de 2018 pour aider à boucler sur un tableau de fonctions asynchrones afin d'obtenir le résultat de chaque fonction asynchrone comme dans une boucle normale.

C'est à peu près tout !

### Lectures complémentaires

#### ECMAScript 2015+

1. [Voici des exemples de tout ce qui est nouveau dans ECMAScript 2016, 2017 et 2018](https://medium.freecodecamp.org/here-are-examples-of-everything-new-in-ecmascript-2016-2017-and-2018-d52fa3b5a70e)
2. [Découvrez ces conseils et astuces utiles pour ECMAScript 2015 (ES6)](https://medium.freecodecamp.org/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377)
3. [5 parties « mauvaises » de JavaScript qui sont corrigées dans ES6](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
4. [Est-ce que « Class » dans ES6 est la nouvelle partie « mauvaise » ?](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

Mes autres articles peuvent être trouvés [ici](https://medium.com/@rajaraodv/latest).

### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissements ? ci-dessous plusieurs fois pour montrer votre soutien ! f44ff44ff44f