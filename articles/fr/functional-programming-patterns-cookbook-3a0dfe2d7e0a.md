---
title: 'Patterns de Programmation Fonctionnelle : Un Cookbook'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T10:00:47.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-patterns-cookbook-3a0dfe2d7e0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wnKmEBrlwH3uDZ_c6su12w.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'Par Karthik Iyengar. Cet article s''adresse à un public qui passe des bibliothèques fonctionnelles comme ramda à l''utilisation de Types de Données Algébriques. Nous utilisons l''excellente bibliothèque crocks...'
---

Par Karthik Iyengar

Cet article s'adresse à un public qui passe de bibliothèques fonctionnelles comme `ramda` à l'utilisation de Types de Données Algébriques (ADTs). Nous utilisons l'excellente bibliothèque `[crocks](https://evilsoft.github.io/crocks/?source=post_page---------------------------)` pour nos ADTs et nos helpers, bien que ces concepts puissent s'appliquer à d'autres également. Nous nous concentrerons sur la démonstration d'applications pratiques et de patterns sans trop nous attarder sur la théorie.

#### Executer des fonctions dangereuses en toute securite

Supposons que nous ayons une situation où nous voulons utiliser une fonction appelée `darken` provenant d'une bibliothèque tierce. `darken` prend un multiplicateur, une couleur et renvoie une nuance plus sombre de cette couleur.

```js
// darken :: Number -> String -> String
darken(0.1)("gray")
//=> "#343434"
```

C'est assez pratique pour nos besoins en CSS. Mais il s'avère que la fonction n'est pas aussi innocente qu'elle en a l'air. `darken` lève des erreurs (throws errors) lorsqu'elle reçoit des arguments inattendus !

```js
darken(0.1)(null)
=> // Error: Passed an incorrect argument to a color function, please pass a string representation of a color.
// (Erreur : Argument incorrect passé à une fonction de couleur, veuillez passer une représentation de couleur sous forme de chaîne.)
```

C'est, bien sûr, très utile pour le débogage — mais nous ne voudrions pas que notre application plante juste parce que nous n'avons pas pu dériver une couleur. C'est ici que `tryCatch` vient à la rescousse.

```js
import { darken } from "polished"
import { tryCatch, compose, either, constant, identity, curry } from "crocks"

// safeDarken :: Number -> String -> String
const safeDarken = curry(n =>
  compose(
    either(constant("inherit"), identity),
    tryCatch(darken(n))
  )
)
```

`tryCatch` exécute la fonction fournie à l'intérieur d'un bloc try-catch et renvoie un Type Somme (Sum Type) appelé `Result`. En essence, un Type Somme est fondamentalement un type "ou". Cela signifie que le `Result` peut être soit un `Ok` si une opération réussit, _ou_ un `Error` en cas d'échec. D'autres exemples de Types Somme incluent `Maybe`, `Either`, `Async` et ainsi de suite. Le helper point-free `either` extrait la valeur de la boîte `Result` et renvoie la valeur CSS par défaut `inherit` si les choses se sont mal passées ou la couleur assombrie si tout s'est bien passé.

```js
safeDarken(0.5)(null)
//=> inherit

safeDarken(0.25)('green')
//=> '#004d00'
```

#### Imposer des types a laide des helpers Maybe

Avec JavaScript, nous rencontrons souvent des cas où nos fonctions explosent parce que nous attendons un type de données particulier, mais que nous en recevons un autre à la place. `crocks` fournit les fonctions `safe`, `safeAfter` et `safeLift` qui nous permettent d'exécuter du code de manière plus prévisible en utilisant le type `Maybe`. Regardons comment convertir des chaînes camelCase en Title Case.

```js
import { safeAfter, safeLift, isArray, isString, map, compose, option } from "crocks"

// match :: Regex -> String -> Maybe [String]
const match = regex => safeAfter(isArray, str => str.match(regex))

// join :: String -> [String] -> String
const join = separator => array => array.join(separator)

// upperFirst :: String -> String
const upperFirst = x =>
  x.charAt(0)
    .toUpperCase()
    .concat(x.slice(1).toLowerCase())

// uncamelize :: String -> Maybe String
const uncamelize = safeLift(isString, compose(
  option(""),
  map(compose(join(" "), map(upperFirst))),
  match(/(((^[a-z]|[A-Z])[a-z]*)|[0-9]+)/g),
))

uncamelize("rockTheCamel")
//=> Just "Rock The Camel"

uncamelize({})
//=> Nothing
```

Nous avons créé une fonction helper `match` qui utilise `safeAfter` pour lisser le comportement de `String.prototype.match` qui renvoie `undefined` s'il n'y a pas de correspondance. Le prédicat `isArray` garantit que nous recevons un `Nothing` si aucune correspondance n'est trouvée, et un `Just [String]` en cas de correspondances. `safeAfter` est idéal pour exécuter des fonctions existantes ou tierces de manière fiable et sécurisée.

(Conseil : `safeAfter` fonctionne très bien avec les fonctions `ramda` qui renvoient `a | undefined`.)

Notre fonction `uncamelize` est exécutée avec `safeLift(isString)`, ce qui signifie qu'elle ne s'exécutera que lorsque l'entrée renvoie true pour le prédicat `isString`.

En plus de cela, crocks fournit également les helpers `prop` et `propPath` qui vous permettent d'extraire des propriétés d'objets (`Object`) et de tableaux (`Array`).

```js
import { prop, propPath, map, compose } from "crocks"

const goodObject = {
  name: "Bob",
  bankBalance: 7999,
  address: {
    city: "Auckland",
    country: "New Zealand",
  },
}

prop("name")(goodObject)
//=> Just "Bob"
propPath(["address", "city"])(goodObject)
//=> Just "Auckland"

// getBankBalance :: Object -> Maybe String
const getBankBalance = compose(
  map(balance => balance.toFixed(2)),
  prop("bankBalance")
)

getBankBalance(goodObject)
//=> Just '7999.00'
getBankBalance({})
//=> Nothing
```

C'est super, surtout si nous traitons des données provenant d'effets de bord qui ne sont pas sous notre contrôle, comme des réponses d'API. Mais que se passe-t-il si les développeurs de l'API décident soudainement de gérer le formatage de leur côté ?

```js
const badObject = { 
  name: "Rambo",
  bankBalance: "100.00",
  address: {
    city: "Hope",
    country: "USA"
  }
}

getBankBalance(badObject) // TypeError: balance.toFixed is not a function :-(
```

Erreurs d'exécution ! Nous avons essayé d'invoquer la méthode `toFixed` sur une chaîne (`String`), ce qui n'existe pas vraiment. Nous devons nous assurer que `bankBalance` est réellement un nombre (`Number`) avant d'y invoquer `toFixed`. Essayons de résoudre cela avec notre helper `safe`.

```js
import { prop, propPath, compose, map, chain, safe, isNumber } from "crocks"

// getBankBalance :: Object -> Maybe String
const getBankBalance = compose(
  map(balance => balance.toFixed(2)),
  chain(safe(isNumber)),
  prop("bankBalance")
)

getBankBalance(badObject) //=> Nothing
getBankBalance(goodObject) //=> Just '7999.00'
```

Nous redirigeons les résultats de la fonction `prop` vers notre fonction `safe(isNumber)` qui renvoie également un `Maybe`, selon que le résultat de `prop` satisfait le prédicat. Le pipeline ci-dessus garantit que le dernier `map` qui contient le `toFixed` ne sera appelé que lorsque `bankBalance` est un `Number`.

Si vous devez gérer beaucoup de cas similaires, il serait judicieux d'extraire ce pattern sous forme de helper :

```js
import { Maybe, ifElse, prop, chain, curry, compose, isNumber } from "crocks"

const { of, zero } = Maybe

// propIf :: (a -> Boolean) -> [String | Number] -> Maybe a
const propIf = curry((fn, path) =>
  compose(
    chain(ifElse(fn, of, zero)),
    prop(path)
  )
)

propIf(isNumber, "age", goodObject) 
//=> Just 7999
propIf(isNumber, "age", badObject) 
//=> Nothing
```

#### Utiliser des Applicatifs pour garder les fonctions propres

Souvent, nous nous retrouvons dans des situations où nous voudrions utiliser une fonction existante avec des valeurs enveloppées dans un conteneur. Essayons de concevoir une fonction `add` sécurisée qui n'autorise que les nombres, en utilisant les concepts de la section précédente. Voici notre première tentative.

```js
import { Maybe, safe, isNumber } from "crocks"

// safeNumber :: a -> Maybe a
const safeNumber = safe(isNumber)

// add :: a -> b -> Maybe Number
const add = (a, b) => {
  const maybeA = safeNumber(a)
  const maybeB = safeNumber(b)
  
  return maybeA.chain(
    valA => maybeB.map(valB => valA + valB)
  )
}

add(1, 2)
//=> Just 3

add(1, {})
//=> Nothing
```

Cela fait exactement ce dont nous avons besoin, mais notre fonction `add` n'est plus un simple `a + b`. Elle doit d'abord élever nos valeurs dans des `Maybe`, puis y accéder pour obtenir les valeurs, et enfin renvoyer le résultat. Nous devons trouver un moyen de préserver la fonctionnalité principale de notre fonction `add` tout en lui permettant de fonctionner avec des valeurs contenues dans des ADTs ! C'est ici que les Foncteurs Applicatifs deviennent utiles.

Un Foncteur Applicatif est comme un foncteur régulier, mais en plus de `map`, il implémente également deux méthodes supplémentaires :

```
of :: Applicative f => a -> f a
```

La méthode `of` est un constructeur totalement simple, et elle place n'importe quelle valeur que vous lui donnez dans notre type de données. On l'appelle aussi `pure` dans d'autres langages.

```js
Maybe.of(null)
//=> Just null

Const.of(42)
//=> Const 42
```

Et voici où réside tout l'intérêt — la méthode `ap` :

```
ap :: Apply f => f a ~> f (a -> b) -> f b
```

La signature ressemble beaucoup à celle de `map`, la seule différence étant que notre fonction `a -> b` est également enveloppée dans un `f`. Voyons cela en action.

```js
import { Maybe, safe, isNumber } from "crocks"

// safeNumber :: a -> Maybe a
const safeNumber = safe(isNumber)

// add :: a -> b -> c
const add = a => b => a + b 

// add :: a -> b -> Maybe Number
const safeAdd = (a, b) => Maybe.of(add)
  .ap(safeNumber(a))
  .ap(safeNumber(b))

safeAdd(1, 2)
//=> Just 3

safeAdd(1, "danger")
//=> Nothing
```

Nous élevons d'abord notre fonction `add` curryfiée dans un `Maybe`, puis nous lui appliquons `Maybe a` et `Maybe b`. Nous avons utilisé `map` jusqu'à présent pour accéder à la valeur à l'intérieur d'un conteneur et `ap` n'est pas différent. En interne, il utilise `map` sur `safeNumber(a)` pour accéder à `a` et l'appliquer à `add`. Cela donne un `Maybe` qui contient une fonction `add` partiellement appliquée. Nous répétons le même processus avec `safeNumber(b)` pour exécuter notre fonction `add`, ce qui donne un `Just` du résultat si `a` et `b` sont tous deux valides, ou un `Nothing` sinon.

Crocks nous fournit également les helpers `liftA2` et `liftN` pour exprimer le même concept de manière pointfree. Voici un exemple simple :

```js
liftA2(add)(Maybe(1))(Maybe(2))
//=> Just 3
```

Nous utiliserons ce helper de manière intensive dans la section `Exprimer le parallélisme`.

Conseil : Puisque nous avons observé qu'`ap` utilise `map` pour accéder aux valeurs, nous pouvons faire des choses sympas comme générer un produit cartésien à partir de deux listes.

```js
import { List, Maybe, Pair, liftA2 } from "crocks"

const names = List(["Henry", "George", "Bono"])
const hobbies = List(["Music", "Football"])

List(name => hobby => Pair(name, hobby))
  .ap(names)
  .ap(hobbies)
// => List [ Pair( "Henry", "Music" ), Pair( "Henry", "Football" ), 
// Pair( "George", "Music" ), Pair( "George", "Football" ), 
// Pair( "Bono", "Music" ), Pair( "Bono", "Football" ) ]
```

#### Utiliser Async pour une gestion derreurs previsible

`crocks` fournit le type de données `Async` qui nous permet de construire des calculs asynchrones paresseux. Pour en savoir plus, vous pouvez consulter la documentation officielle détaillée [ici](https://evilsoft.github.io/crocks/docs/crocks/Async.html?source=post_page---------------------------). Cette section vise à fournir des exemples de la façon dont nous pouvons utiliser `Async` pour améliorer la qualité de nos rapports d'erreurs et rendre notre code résilient.

Souvent, nous rencontrons des cas où nous voulons faire des appels d'API qui dépendent les uns des autres. Ici, l'endpoint `getUser` renvoie une entité utilisateur de GitHub et la réponse contient beaucoup d'URLs intégrées pour les dépôts, les étoiles, les favoris, etc. Nous allons voir comment concevoir ce cas d'utilisation en utilisant `Async`.

```js
import { Async, prop, compose, chain,  safe, isString, maybeToAsync } from "crocks"

const { fromPromise } = Async

// userPromise :: String -> Promise User Error
const userPromise = user => fetch(`https://api.github.com/users/${user}`)
  .then(res => res.json())

// resourcePromise :: String -> Promise Resource Error
const resourcePromise = url => fetch(url)
  .then(res => res.json())

// getUser :: String -> Async User Error
const getUser = compose(
  chain(fromPromise(userPromise)),
  maybeToAsync('getUser attend une chaîne de caractères'),
  safe(isString)
)

// getResource :: String -> Object -> Async Resource Error
const getResource = path => user => {
  if (!isString(path)) {
    return Async.Rejected("getResource attend une chaîne de caractères")
  }
  return maybeToAsync("Erreur : Réponse utilisateur malformée reçue", prop(path, user))
    .chain(fromPromise(resourcePromise))
}

// logError :: (...a) -> IO()
const logError = (...args) => console.log("Erreur : ", ...args)

// logResponse :: (...a) -> IO()
const logSuccess = (...args) => console.log("Succès : ", ...args)

getUser("octocat")
  .chain(getResource("repos_url"))
  .fork(logError, logSuccess)
//=> Success: { ...response }

getUser(null)
  .chain(getResource("repos_url"))
  .fork(logError, logSuccess)
//=> Error: The user must be as string

getUser("octocat")
  .chain(getResource(null))
  .fork(logError, logSuccess)
//=> Error: getResource expects a string

getUser("octocat")
  .chain(getResource("unknown_path_here"))
  .fork(logError, logSuccess)
//=> Error: Malformed user response received
```

L'utilisation de la transformation `maybeToAsync` nous permet d'utiliser toutes les fonctionnalités de sécurité que nous obtenons en utilisant `Maybe` et de les intégrer à nos flux `Async`. Nous pouvons maintenant signaler les erreurs d'entrée et d'autres erreurs dans le cadre de nos flux `Async`.

#### Utiliser efficacement les Monoides

Nous avons déjà utilisé des Monoïdes en effectuant des opérations telles que la concaténation de chaînes (`String`) ou de tableaux (`Array`) et l'addition de nombres en JavaScript natif. C'est simplement un type de données qui nous offre les méthodes suivantes.

```
concat :: Monoid m => m a -> m a -> m a
```

`concat` nous permet de combiner deux Monoïdes du même type ensemble avec une opération spécifiée à l'avance.

```
empty :: Monoid m => () => m a
```

La méthode `empty` nous fournit un élément d'identité qui, lorsqu'il est concaténé avec d'autres Monoïdes du même type, renverrait le même élément. Voici de quoi je parle.

```js
import { Sum } from "crocks"

Sum.empty()
//=> Sum 0

Sum(10)
  .concat(Sum.empty())
//=> Sum 10

Sum(10)
  .concat(Sum(32))
//=> Sum 42
```

En soi, cela ne semble pas très utile, mais `crocks` fournit des Monoïdes supplémentaires ainsi que des helpers `mconcat`, `mreduce`, `mconcatMap` et `mreduceMap`.

```js
import { Sum, mconcat, mreduce, mconcatMap, mreduceMap } from "crocks"

const array = [1, 3, 5, 7, 9]

const inc = x => x + 1

mconcat(Sum, array)
//=> Sum 25

mreduce(Sum, array)
//=> 25

mconcatMap(Sum, inc, array)
//=> Sum 30

mreduceMap(Sum, inc, array)
//=> 30
```

Les méthodes `mconcat` et `mreduce` prennent un Monoïde et une liste d'éléments et appliquent `concat` à tous leurs éléments. La seule différence entre elles est que `mconcat` renvoie une instance du Monoïde tandis que `mreduce` renvoie la valeur brute. Les helpers `mconcatMap` et `mreduceMap` fonctionnent de la même manière, sauf qu'ils acceptent une fonction supplémentaire utilisée pour mapper chaque élément avant d'appeler `concat`.

Regardons un autre exemple de Monoïde de `crocks`, le Monoïde `First`. Lors de la concaténation, `First` renverra toujours la première valeur non vide.

```js
import { First, Maybe } from "crocks"

First(Maybe.zero())
  .concat(First(Maybe.zero()))
  .concat(First(Maybe.of(5)))
//=> First (Just 5)

First(Maybe.of(5))
  .concat(First(Maybe.zero()))
  .concat(First(Maybe.of(10)))
//=> First (Just 5)
```

En utilisant la puissance de `First`, essayons de créer une fonction qui tente d'obtenir la première propriété disponible sur un objet.

```js
import { curry, First, mreduceMap, flip, prop, compose } from "crocks"

/** tryProps -> a -> [String] -> Object -> b */
const tryProps = flip(object => 
  mreduceMap(
    First, 
    flip(prop, object),
  )
)
 
const a = {
  x: 5,
  z: 10,
  m: 15,
  g: 12
}

tryProps(["a", "y", "b", "g"], a)
//=> Just 12

tryProps(["a", "b", "c"], a)
//=> Nothing

tryProps(["a", "z", "c"], a)
//=> Just 10
```

Plutôt soigné ! Voici un autre exemple qui tente de créer un formateur au mieux lorsqu'il reçoit différents types de valeurs.

```js

import { 
  applyTo, mreduceMap, isString, isEmpty, mreduce, First, not, isNumber, chain
  compose, safe, and, constant, Maybe, map, equals, ifElse, isBoolean, option,
} from "crocks";

// isDate :: a -> Boolean
const isDate = x => x instanceof Date;

// lte :: Number -> Number -> Boolean
const lte = x => y => y <= x;

// formatBoolean :: a -> Maybe String
const formatBoolean = compose(
  map(ifElse(equals(true), constant("Yes"), constant("No"))),
  safe(isBoolean)
);

// formatNumber :: a -> Maybe String
const formatNumber = compose(
  map(n => n.toFixed(2)),
  safe(isNumber)
);

// formatPercentage :: a -> Maybe String
const formatPercentage = compose(
  map(n => n + "%"),
  safe(and(isNumber, lte(100)))
);

// formatDate :: a -> Maybe String
const formatDate = compose(
  map(d => d.toISOString().slice(0, 10)),
  safe(isDate)
);

// formatString :: a -> Maybe String
const formatString = safe(isString)

// autoFormat :: a -> Maybe String
const autoFormat = value =>
  mreduceMap(First, applyTo(value), [
    formatBoolean,
    formatPercentage,
    formatNumber,
    formatDate,
    formatString
  ]);

autoFormat(true)
//=> Just "Yes"

autoFormat(10.02)
//=> Just "10%"

autoFormat(255)
//=> Just "255.00"

autoFormat(new Date())
//=> Just "2019-01-14"

autoFormat("YOLO!")
//=> Just "YOLO!"

autoFormat(null)
//=> Nothing
```

#### Exprimer le paralle lisme en style Pointfree

Nous pourrions rencontrer des cas où nous voulons effectuer plusieurs opérations sur une seule donnée et combiner les résultats d'une certaine manière. `crocks` nous fournit deux méthodes pour y parvenir. Le premier pattern exploite les Types Produits (Product Types) `Pair` et `Tuple`. Regardons un petit exemple où nous avons un objet qui ressemble à ceci :

```
{ ids: [11233, 12351, 16312], rejections: [11233] }
```

Nous aimerions écrire une fonction qui accepte cet objet et renvoie un tableau (`Array`) d'`ids` excluant ceux rejetés. Notre première tentative en JavaScript natif ressemblerait à ceci :

```js
const getIds = (object) => object.ids.filter(x => object.rejections.includes(x))
```

Cela fonctionne bien sûr, mais cela exploserait au cas où l'une des propriétés serait malformée ou non définie. Faisons en sorte que `getIds` renvoie un `Maybe` à la place. Nous utilisons le helper `fanout` qui accepte deux fonctions, les exécute sur la même entrée et renvoie une `Pair` de résultats.

```js
import { prop, compose, equals, filter, fanout, merge, liftA2 } from "crocks"

/**
 * object :: Record
 * Record :: {
 *  ids: [Number]
 *  rejection: [Number]
 * }
 **/
const object = { ids: [11233, 12351, 16312], rejections: [11233] }

// excludes :: [a] -> [b] -> Boolean
const excludes = x => y => !x.includes(y)

// difference :: [a] -> [a] -> [a]
const difference = compose(filter, excludes)

// getIds :: Record -> Maybe [Number]
const getIds = compose(
  merge(liftA2(difference)),
  fanout(prop("rejections"), prop("ids"))
)

getIds(object)
//=> Just [ 12351, 16312 ]

getIds({ something: [], else: 5 })
//=> Nothing
```

L'un des principaux avantages de l'approche pointfree est qu'elle nous encourage à diviser notre logique en petits morceaux. Nous avons maintenant le helper réutilisable `difference` (avec `liftA2`, comme vu précédemment) que nous pouvons utiliser pour fusionner (`merge`) les deux moitiés de la `Pair` ensemble.

La deuxième méthode consisterait à utiliser le combinateur `converge` pour obtenir des résultats similaires. `converge` prend trois fonctions et une valeur d'entrée. Il applique ensuite l'entrée aux deuxième et troisième fonctions et redirige les résultats des deux vers la première. Utilisons-le pour créer une fonction qui normalise un tableau d'objets en fonction de leurs `id`. Nous utiliserons le Monoïde `Assign` qui nous permet de combiner des objets ensemble.

```js
import {
  mreduceMap, applyTo, option, identity, objOf, map,
  converge, compose, Assign, isString, constant
} from "crocks"
import propIf from "./propIf"

// normalize :: String -> [Object] -> Object
const normalize = mreduceMap(
  Assign,
  converge(
    applyTo,
    identity,
    compose(
      option(constant({})),
      map(objOf),
      propIf(isString, "id")
    )
  )
)

normalize([{ id: "1", name: "Kerninghan" }, { id: "2", name: "Stallman" }])
//=> { 1: { id: '1', name: 'Kerninghan' }, 2: { id: '2', name: 'Stallman' } }

normalize([{ id: null}, { id: "1", name: "Knuth" }, { totally: "unexpected" }])
//=> { 1: { id: '1', name: 'Knuth' } }
```

#### Utiliser Traverse et Sequence pour garantir lintegrite des donnees

Nous avons vu comment utiliser `Maybe` et consorts pour nous assurer que nous travaillons toujours avec les types attendus. Mais que se passe-t-il lorsque nous travaillons avec un type qui contient d'autres valeurs, comme un tableau (`Array`) ou une liste (`List`) par exemple ? Regardons une fonction simple qui nous donne la longueur totale de toutes les chaînes contenues dans un tableau.

```js
import { compose, safe, isArray, reduce, map } from "crocks"

// sum :: [Number] -> Number
const sum = reduce((a, b) => a + b, 0)

// length :: [a] -> Number
const length = x => x.length;

// totalLength :: [String] -> Maybe Number 
const totalLength = compose(
  map(sum),
  map(map(length)),
  safe(isArray)
)

const goodInput = ["is", "this", "the", "real", "life?"]
totalLength(goodInput)
//=> Just 18

const badInput = { message: "muhuhahhahahaha!"}
totalLength(badInput)
//=> Nothing
```

C'est bien. Nous nous sommes assurés que notre fonction renvoie toujours un `Nothing` si elle ne reçoit pas un tableau. Est-ce suffisant pour autant ?

```js
totalLength(["stairway", "to", undefined])
//=> TypeError: x is undefined
```

Pas vraiment. Notre fonction ne garantit pas que le contenu de la liste ne nous réserve pas de surprises. L'une des façons de résoudre ce problème serait de définir une fonction `safeLength` qui ne fonctionne qu'avec des chaînes de caractères :

```js
// safeLength :: a -> Maybe Number 
const safeLength = safeLift(isString, length)
```

Si nous utilisons `safeLength` au lieu de `length` comme fonction de mapping, nous recevrions un `[Maybe Number]` au lieu d'un `[Number]` et nous ne pourrions plus utiliser notre fonction `sum`. C'est ici que `sequence` devient utile.

```js
import { sequence, Maybe, Identity } from "crocks"

sequence(Maybe, Identity(Maybe.of(1)))
//=> Just Identity 1

sequence(Array, Identity([1,2,3]))
//=> [ Identity 1, Identity 2, Identity 3 ]

sequence(Maybe, [Maybe.of(4), Maybe.of(2)])
//=> Just [ 4, 2 ]

sequence(Maybe, [Maybe.of(4), Maybe.zero()])
//=> Nothing
```

`sequence` aide à échanger le type interne avec le type externe tout en effectuant un certain `effet`, étant donné que le type interne est un Applicatif. Le `sequence` sur `Identity` est assez simple — il fait juste un `map` sur le type interne et renvoie le contenu enveloppé dans un conteneur `Identity`. Pour `List` et `Array`, `sequence` utilise `reduce` sur la liste pour combiner son contenu à l'aide d'`ap` et `concat`. Voyons cela en action dans notre implémentation refactorisée de `totalLength`.

```js
// totalLength :: [String] -> Maybe Number 
const totalLength = compose(
  map(sum),
  chain(sequence(Maybe)),
  map(map(safeLength)),
  safe(isArray)
)

const goodString = ["is", "this", "the", "real", "life?"]
totalLength(goodString)
//=> Just 18

totalLength(["stairway", "to", undefined])
//=> Nothing
```

Super ! Nous avons construit un `totalLength` complètement blindé. Ce pattern de mapper sur quelque chose de `a -> m b` puis d'utiliser `sequence` est si courant que nous avons un autre helper appelé `traverse` qui effectue les deux opérations ensemble. Voyons comment nous pouvons utiliser `traverse` au lieu de `sequence` dans l'exemple ci-dessus.

```js
// totalLengthT :: [String] -> Maybe Number 
const totalLengthT = compose(
  map(sum),
  chain(traverse(Maybe, safeLength)),
  safe(isArray)
)
```

Et voilà ! Cela fonctionne exactement de la même manière. Si on y réfléchit bien, notre opérateur `sequence` est fondamentalement un `traverse` avec un `identity` comme fonction de mapping.

Remarque : Comme nous ne pouvons pas inférer le type interne en JavaScript, nous devons explicitement fournir le constructeur de type comme premier argument de `traverse` et `sequence`.

Il est facile de voir à quel point `sequence` et `traverse` sont inestimables pour valider des données. Essayons de créer un validateur générique qui prend un schéma et valide un objet d'entrée. Nous utiliserons le type `Result`, qui accepte un Semigroupe sur le côté gauche nous permettant de collecter des erreurs. Un Semigroupe est similaire à un Monoïde et définit une méthode `concat` — mais contrairement au Monoïde, il ne nécessite pas la présence de la méthode `empty`. Nous introduisons également la fonction de transformation `maybeToResult` ci-dessous, qui nous aidera à interagir entre `Maybe` et `Result`.

```js

import {
  Result, isString, map, merge, constant, bimap, flip, propOr, identity, 
  toPairs, safe, maybeToResult, traverse, and, isNumber, compose
} from "crocks"

// length :: [a] -> Int
const length = x => x.length

// gte :: Number -> a -> Result String a
const gte = x => y => y >= x

// lte :: Number -> a -> Result String a
const lte = x => y => y <= x

// isValidName :: a -> Result String a
const isValidName = compose(
  maybeToResult("attendu : une chaîne de moins de 20 caractères"),
  safe(and(compose(lte(20), length), isString))
)

// isAdult :: a -> Result String a
const isAdult = compose(
  maybeToResult("attendu : une valeur supérieure à 18"),
  safe(and(isNumber, gte(18)))
)

/**
 *  schema :: Schema
 *  Schema :: {
 *    [string]: a -> Result String a
 *  }
 * */
const schema = {
  name: isValidName,
  age: isAdult,
}

// makeValidator :: Schema -> Object -> Result [String] Object
const makeValidator = flip(object =>
  compose(
    map(constant(object)),
    traverse(Result, merge((key, validator) =>
        compose(
          bimap(error => [`${key}: ${error}`], identity),
          validator,
          propOr(undefined, key)
        )(object)
      )
    ),
    toPairs
  )
)

// validate :: Object -> Result [String] Object
const validate = makeValidator(schema)

validate(({
  name: "Car",
  age: 21,
}))
//=> Ok { name: "Car", age: 21 }

validate(({
  name: 7,
  age: "Old",
}))
//=>  Err [ "name: attendu : une chaîne de moins de 20 caractères", "age: attendu : une valeur supérieure à 18" ]
```

Comme nous avons inversé (`flip`) la fonction `makeValidator` pour la rendre plus adaptée à la curryfication, notre chaîne `compose` reçoit d'abord le schéma contre lequel nous devons valider. Nous divisons d'abord le schéma en paires (`Pair`) clé-valeur et passons la valeur de chaque propriété à sa fonction de validation correspondante. Au cas où la fonction échouerait, nous utilisons `bimap` pour mapper sur l'erreur, lui ajouter plus d'informations et la renvoyer sous la forme d'un tableau (`Array`) singleton. `traverse` concaténera (`concat`) ensuite toutes les erreurs si elles existent, ou renverra l'objet original s'il est valide. Nous aurions également pu renvoyer une `String` au lieu d'un `Array`, mais un `Array` est bien plus pratique.

_Merci à [Ian Hofmann-Hicks,](https://www.freecodecamp.org/news/functional-programming-patterns-cookbook-3a0dfe2d7e0a/undefined) [Sinisa Louc](https://www.freecodecamp.org/news/functional-programming-patterns-cookbook-3a0dfe2d7e0a/undefined) et [Dale Francis](https://github.com/dalefrancis88) pour leurs contributions à ce post._