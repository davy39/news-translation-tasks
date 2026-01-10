---
title: ES5 à ESNext — voici toutes les fonctionnalités ajoutées à JavaScript depuis
  2015
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2019-02-13T16:33:04.000Z'
originalURL: https://freecodecamp.org/news/es5-to-esnext-heres-every-feature-added-to-javascript-since-2015-d0c255e13c6e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QZppItKE3Sqdi3kZA-TNGQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: ES5 à ESNext — voici toutes les fonctionnalités ajoutées à JavaScript depuis
  2015
seo_desc: 'I wrote this article to help you move from pre-ES6 knowledge of JavaScript
  and get you quickly up to speed with the most recent advancements of the language.

  JavaScript today is in the privileged position to be the only language that can
  run natively...'
---

J'ai écrit cet article pour vous aider à passer d'une connaissance pré-ES6 de JavaScript et vous mettre rapidement à jour avec les avancées les plus récentes du langage.

JavaScript aujourd'hui est dans la position privilégiée d'être le seul langage qui peut s'exécuter nativement dans le navigateur, et il est hautement intégré et optimisé pour cela.

L'avenir de JavaScript sera brillant. Se tenir au courant des changements ne devrait pas être plus difficile qu'il ne l'est déjà, et mon objectif ici est de vous donner un aperçu rapide mais complet des nouvelles fonctionnalités disponibles pour nous.

**[Cliquez ici pour obtenir une version PDF / ePub / Mobi de cet article à lire hors ligne](https://flaviocopes.com/page/es5-to-esnext/)**

# Introduction à ECMAScript

Lorsque vous lisez à propos de JavaScript, vous verrez inévitablement l'un de ces termes : ES3, ES5, ES6, ES7, ES8, ES2015, ES2016, ES2017, ECMAScript 2017, ECMAScript 2016, ECMAScript 2015… que signifient-ils ?

Ils font tous référence à une **norme**, appelée ECMAScript.

ECMAScript est **la norme sur laquelle JavaScript est basé**, et il est souvent abrégé en **ES**.

Outre JavaScript, d'autres langues implémentent (ou ont implémenté) ECMAScript, notamment :

* _ActionScript_ (le langage de script Flash), qui perd en popularité depuis que Flash sera officiellement abandonné en 2020
* _JScript_ (le dialecte de script Microsoft), car à l'époque JavaScript était soutenu uniquement par Netscape et la guerre des navigateurs était à son apogée, Microsoft a dû construire sa propre version pour Internet Explorer

mais bien sûr JavaScript est l'**implémentation la plus populaire** et la plus largement utilisée de ES.

Pourquoi ce nom étrange ? `Ecma International` est une association de normes suisse qui est chargée de définir des normes internationales.

Lorsque JavaScript a été créé, il a été présenté par Netscape et Sun Microsystems à Ecma et ils lui ont donné le nom ECMA-262 alias **ECMAScript**.

[Ce communiqué de presse de Netscape et Sun Microsystems](https://web.archive.org/web/20070916144913/http://wp.netscape.com/newsref/pr/newsrelease67.html) (le créateur de Java) pourrait aider à comprendre le choix du nom, qui pourrait inclure des problèmes juridiques et de marque de Microsoft qui était dans le comité, [selon Wikipedia](https://en.wikipedia.org/wiki/ECMAScript).

Après IE9, Microsoft a arrêté de marquer son support ES dans les navigateurs comme JScript et a commencé à l'appeler JavaScript (au moins, je n'ai pas pu trouver de références à ce sujet).

Ainsi, à partir de 201x, le seul langage populaire supportant la spécification ECMAScript est JavaScript.

### Version actuelle d'ECMAScript

La version actuelle d'ECMAScript est **ES2018**.

Elle a été publiée en juin 2018.

### Qu'est-ce que TC39

TC39 est le comité qui fait évoluer JavaScript.

Les membres de TC39 sont des entreprises impliquées dans JavaScript et des fournisseurs de navigateurs, notamment Mozilla, Google, Facebook, Apple, Microsoft, Intel, PayPal, SalesForce et d'autres.

Chaque proposition de version standard doit passer par diverses étapes, [qui sont expliquées ici](https://tc39.github.io/process-document/).

### Versions d'ES

J'ai trouvé déroutant le fait que parfois une version d'ES est référencée par le numéro d'édition et parfois par l'année, et je suis confus par le fait que l'année soit par hasard -1 sur le numéro, ce qui ajoute à la confusion générale autour de JS/ES ?

Avant ES2015, les spécifications ECMAScript étaient communément appelées par leur édition. Ainsi, ES5 est le nom officiel de la mise à jour de la spécification ECMAScript publiée en 2009.

Pourquoi cela se produit-il ? Pendant le processus qui a conduit à ES2015, le nom a été changé de ES6 à ES2015, mais comme cela a été fait tardivement, les gens référaient toujours à ES6, et la communauté n'a pas abandonné la dénomination par édition — _le monde continue d'appeler les versions ES par numéro d'édition_.

Ce tableau devrait éclaircir un peu les choses :

![Image](https://cdn-media-1.freecodecamp.org/images/uBY4n5MuFWvc81VWSWVk2wc1ZYQ4MF1RM39A)

Plongeons dans les fonctionnalités spécifiques ajoutées à JavaScript depuis ES5. Commençons par les fonctionnalités d'ES2015.

## let et const

Jusqu'à ES2015, `var` était la seule construction disponible pour définir des variables.

```js
var a = 0
```

Si vous oubliez d'ajouter `var`, vous allez assigner une valeur à une variable non déclarée, et les résultats peuvent varier.

Dans les environnements modernes, avec le mode strict activé, vous obtiendrez une erreur. Dans les anciens environnements (ou avec le mode strict désactivé), cela initialisera la variable et l'assignera à l'objet global.

Si vous n'initialisez pas la variable lorsque vous la déclarez, elle aura la valeur `undefined` jusqu'à ce que vous lui assigniez une valeur.

```js
var a //typeof a === 'undefined'
```

Vous pouvez redéclarer la variable plusieurs fois, en l'écrasant :

```js
var a = 1
var a = 2
```

Vous pouvez également déclarer plusieurs variables en une seule fois dans la même instruction :

```js
var a = 1, b = 2
```

La **portée** est la portion de code où la variable est visible.

Une variable initialisée avec `var` en dehors de toute fonction est assignée à l'objet global, a une portée globale et est visible partout. Une variable initialisée avec `var` à l'intérieur d'une fonction est assignée à cette fonction, elle est locale et n'est visible qu'à l'intérieur, tout comme un paramètre de fonction.

Toute variable définie dans une fonction avec le même nom qu'une variable globale prend le pas sur la variable globale, l'ombrageant.

Il est important de comprendre qu'un bloc (identifié par une paire d'accolades) ne définit pas une nouvelle portée. Une nouvelle portée n'est créée que lorsqu'une fonction est créée, car `var` n'a pas de portée de bloc, mais une portée de fonction.

À l'intérieur d'une fonction, toute variable définie dans celle-ci est visible dans tout le code de la fonction, même si la variable est déclarée à la fin de la fonction, elle peut toujours être référencée au début, car JavaScript, avant d'exécuter le code, **déplace toutes les variables en haut** (quelque chose qui est appelé **hoisting**). Pour éviter la confusion, déclarez toujours les variables au début d'une fonction.

### Utilisation de `let`

`let` est une nouvelle fonctionnalité introduite dans ES2015 et c'est essentiellement une version de `var` avec une portée de bloc. Sa portée est limitée au bloc, à l'instruction ou à l'expression où elle est définie, et à tous les blocs internes contenus.

Les développeurs JavaScript modernes peuvent choisir d'utiliser uniquement `let` et d'abandonner complètement l'utilisation de `var`.

> _Si `let` semble un terme obscur, lisez simplement `let color = 'red'` comme_ que la couleur soit rouge _et tout devient beaucoup plus clair_

Définir `let` en dehors de toute fonction — contrairement à `var` — ne crée pas de variable globale.

### Utilisation de `const`

Les variables déclarées avec `var` ou `let` peuvent être modifiées plus tard dans le programme, et réassignées. Une fois qu'un `const` est initialisé, sa valeur ne peut plus jamais être changée, et il ne peut pas être réassigné à une valeur différente.

```js
const a = 'test'
```

Nous ne pouvons pas assigner un littéral différent à la `const` `a`. Nous pouvons cependant muter `a` si c'est un objet qui fournit des méthodes qui mutent son contenu.

`const` ne fournit pas l'immuabilité, il garantit simplement que la référence ne peut pas être changée.

`const` a une portée de bloc, comme `let`.

Les développeurs JavaScript modernes peuvent choisir d'utiliser toujours `const` pour les variables qui n'ont pas besoin d'être réassignées plus tard dans le programme, car nous devons toujours utiliser la construction la plus simple disponible pour éviter de faire des erreurs plus tard.

## Fonctions fléchées

Les fonctions fléchées, depuis leur introduction, ont changé à jamais l'apparence (et le fonctionnement) du code JavaScript.

À mon avis, ce changement a été si bien accueilli que l'on voit rarement l'utilisation du mot-clé `function` dans les bases de code modernes. Bien que celui-ci ait encore son utilité.

Visuellement, c'est un changement simple et bienvenu, qui vous permet d'écrire des fonctions avec une syntaxe plus courte, de :

```js
const myFunction = function() {
  //...
}
```

à

```js
const myFunction = () => {
  //...
}
```

Si le corps de la fonction ne contient qu'une seule instruction, vous pouvez omettre les accolades et tout écrire sur une seule ligne :

```js
const myFunction = () => doSomething()
```

Les paramètres sont passés entre les parenthèses :

```js
const myFunction = (param1, param2) => doSomething(param1, param2)
```

Si vous avez un (et un seul) paramètre, vous pouvez omettre complètement les parenthèses :

```js
const myFunction = param => doSomething(param)
```

Grâce à cette syntaxe courte, les fonctions fléchées **encouragent l'utilisation de petites fonctions**.

### Retour implicite

Les fonctions fléchées permettent d'avoir un retour implicite : les valeurs sont retournées sans avoir à utiliser le mot-clé `return`.

Cela fonctionne lorsqu'il y a une instruction sur une seule ligne dans le corps de la fonction :

```js
const myFunction = () => 'test'

myFunction() //'test'
```

Un autre exemple, lors du retour d'un objet, n'oubliez pas d'envelopper les accolades dans des parenthèses pour éviter qu'elles soient considérées comme les accolades du corps de la fonction :

```js
const myFunction = () => ({ value: 'test' })

myFunction() //{value: 'test'}
```

### Comment `this` fonctionne dans les fonctions fléchées

`this` est un concept qui peut être compliqué à comprendre, car il varie beaucoup en fonction du contexte et varie également en fonction du mode de JavaScript (_mode strict_ ou non).

Il est important de clarifier ce concept car les fonctions fléchées se comportent très différemment par rapport aux fonctions régulières.

Lorsque défini comme une méthode d'un objet, dans une fonction régulière `this` fait référence à l'objet, donc vous pouvez faire :

```js
const car = {
  model: 'Fiesta',
  manufacturer: 'Ford',
  fullName: function() {
    return `${this.manufacturer} ${this.model}`
  }
}
```

appeler `car.fullName()` retournera `"Ford Fiesta"`.

La portée de `this` avec les fonctions fléchées est **héritée** du contexte d'exécution. Une fonction fléchée ne lie pas `this` du tout, donc sa valeur sera recherchée dans la pile d'appels, donc dans ce code `car.fullName()` ne fonctionnera pas, et retournera la chaîne `"undefined undefined"` :

```js
const car = {
  model: 'Fiesta',
  manufacturer: 'Ford',
  fullName: () => {
    return `${this.manufacturer} ${this.model}`
  }
}
```

En raison de cela, les fonctions fléchées ne conviennent pas comme méthodes d'objet.

Les fonctions fléchées ne peuvent pas non plus être utilisées comme constructeurs, lors de l'instanciation d'un objet, une `TypeError` sera levée.

C'est là que les fonctions régulières doivent être utilisées à la place, **lorsqu'un contexte dynamique n'est pas nécessaire**.

Ceci est également un problème lors de la gestion des événements. Les écouteurs d'événements DOM définissent `this` comme étant l'élément cible, et si vous vous basez sur `this` dans un gestionnaire d'événements, une fonction régulière est nécessaire :

```js
const link = document.querySelector('#link')
link.addEventListener('click', () => {
  // this === window
})

const link = document.querySelector('#link')
link.addEventListener('click', function() {
  // this === link
})
```

## Classes

JavaScript a une manière assez inhabituelle d'implémenter l'héritage : l'héritage prototypal. [L'héritage prototypal](https://flaviocopes.com/javascript-prototypal-inheritance/), bien que, à mon avis, excellent, est différent de la plupart des autres langages de programmation populaires, qui implémentent l'héritage basé sur les classes.

Les personnes venant de Java ou Python ou d'autres langages avaient du mal à comprendre les intrications de l'héritage prototypal, donc le comité ECMAScript a décidé d'ajouter du sucre syntaxique par-dessus l'héritage prototypal afin qu'il ressemble à la manière dont l'héritage basé sur les classes fonctionne dans d'autres implémentations populaires.

Ceci est important : JavaScript sous le capot reste le même, et vous pouvez accéder au prototype d'un objet de la manière habituelle.

### Une définition de classe

Voici à quoi ressemble une classe.

```js
class Person {
  constructor(name) {
    this.name = name
  }
  
  hello() {
    return 'Hello, I am ' + this.name + '.'
  }
}
```

Une classe a un identifiant, que nous pouvons utiliser pour créer de nouveaux objets en utilisant `new ClassIdentifier()`.

Lorsque l'objet est initialisé, la méthode `constructor` est appelée, avec tous les paramètres passés.

Une classe a également autant de méthodes que nécessaire. Dans ce cas, `hello` est une méthode et peut être appelée sur tous les objets dérivés de cette classe :

```js
const flavio = new Person('Flavio')
flavio.hello()
```

### Héritage de classe

Une classe peut étendre une autre classe, et les objets initialisés en utilisant cette classe héritent de toutes les méthodes des deux classes.

Si la classe héritée a une méthode avec le même nom que l'une des classes plus haut dans la hiérarchie, la méthode la plus proche prend le pas :

```js
class Programmer extends Person {
  hello() {
    return super.hello() + ' I am a programmer.'
  }
}

const flavio = new Programmer('Flavio')
flavio.hello()
```

(le programme ci-dessus imprime « Hello, I am Flavio. I am a programmer. »)

Les classes n'ont pas de déclarations explicites de variables de classe, mais vous devez initialiser toute variable dans le constructeur.

À l'intérieur d'une classe, vous pouvez référencer la classe parente en appelant `super()`.

### Méthodes statiques

Normalement, les méthodes sont définies sur l'instance, et non sur la classe.

Les méthodes statiques sont exécutées sur la classe à la place :

```js
class Person {
  static genericHello() {
    return 'Hello'
  }
}

Person.genericHello() //Hello
```

### Méthodes privées

JavaScript n'a pas de moyen intégré pour définir des méthodes privées ou protégées.

Il existe des solutions de contournement, mais je ne les décrirai pas ici.

### Getters et setters

Vous pouvez ajouter des méthodes préfixées avec `get` ou `set` pour créer un getter et un setter, qui sont deux morceaux de code différents exécutés en fonction de ce que vous faites : accéder à la variable ou modifier sa valeur.

```js
class Person {
  constructor(name) {
    this._name = name
  }
  
  set name(value) {
    this._name = value
  }
  
  get name() {
    return this._name
  }
}
```

Si vous n'avez qu'un getter, la propriété ne peut pas être définie, et toute tentative de le faire sera ignorée :

```js
class Person {
  constructor(name) {
    this._name = name
  }
  
  get name() {
    return this._name
  }
}
```

Si vous n'avez qu'un setter, vous pouvez changer la valeur mais pas y accéder de l'extérieur :

```js
class Person {
  constructor(name) {
    this._name = name
  }
  
  set name(value) {
    this._name = value
  }
}
```

## Paramètres par défaut

Voici une fonction `doSomething` qui accepte `param1`.

```js
const doSomething = (param1) => {

}
```

Nous pouvons ajouter une valeur par défaut pour `param1` si la fonction est appelée sans spécifier de paramètre :

```js
const doSomething = (param1 = 'test') => {

}
```

Cela fonctionne également pour plusieurs paramètres, bien sûr :

```js
const doSomething = (param1 = 'test', param2 = 'test2') => {

}
```

Et si vous avez un objet unique avec des valeurs de paramètres ?

Il fut un temps, si nous devions passer un objet d'options à une fonction, afin d'avoir des valeurs par défaut de ces options si l'une d'entre elles n'était pas définie, vous deviez ajouter un peu de code à l'intérieur de la fonction :

```js
const colorize = (options) => {
  if (!options) {
    options = {}
  }
  
  const color = ('color' in options) ? options.color : 'yellow'
  ...
}
```

Avec la déstructuration, vous pouvez fournir des valeurs par défaut, ce qui simplifie beaucoup le code :

```js
const colorize = ({ color = 'yellow' }) => {
  ...
}
```

Si aucun objet n'est passé lors de l'appel de notre fonction `colorize`, de manière similaire, nous pouvons assigner un objet vide par défaut :

```js
const spin = ({ color = 'yellow' } = {}) => {
  ...
}
```

## Littéraux de gabarit

Les littéraux de gabarit permettent de travailler avec des chaînes de caractères de manière nouvelle par rapport à ES5 et versions antérieures.

La syntaxe, à première vue, est très simple, il suffit d'utiliser des backticks au lieu de guillemets simples ou doubles :

```js
const a_string = `something`
```

Ils sont uniques car ils offrent de nombreuses fonctionnalités que les chaînes de caractères normales construites avec des guillemets ne fournissent pas, en particulier :

* ils offrent une excellente syntaxe pour définir des chaînes de caractères multilingues
* ils fournissent un moyen facile d'interpoler des variables et des expressions dans des chaînes de caractères
* ils permettent de créer des DSL avec des balises de gabarit (DSL signifie langage spécifique de domaine, et il est utilisé par exemple dans React par Styled Components, pour définir le CSS pour un composant)

Plongeons dans chacun de ces points en détail.

### Chaînes de caractères multilingues

Avant ES6, pour créer une chaîne de caractères s'étendant sur deux lignes, vous deviez utiliser le caractère `\` à la fin d'une ligne :

```js
const string =
  'first part \
second part'
```

Cela permet de créer une chaîne de caractères sur 2 lignes, mais elle est rendue sur une seule ligne :

`first part second part`

Pour rendre la chaîne de caractères sur plusieurs lignes également, vous devez explicitement ajouter `\n` à la fin de chaque ligne, comme ceci :

```js
const string =
  'first line\n \
second line'
```

ou

```js
const string = 'first line\n' + 'second line'
```

Les littéraux de gabarit rendent les chaînes de caractères multilingues beaucoup plus simples.

Une fois qu'un littéral de gabarit est ouvert avec le backtick, vous appuyez simplement sur Entrée pour créer une nouvelle ligne, sans caractères spéciaux, et il est rendu tel quel :

```js
const string = `Hey
this

string
is awesome!`
```

Gardez à l'esprit que l'espace est significatif, donc faire ceci :

```js
const string = `First
                Second`
```

va créer une chaîne de caractères comme ceci :

```js
First
                Second
```

une manière facile de corriger ce problème est d'avoir une première ligne vide, et d'ajouter la méthode trim() juste après le backtick de fermeture, ce qui éliminera tout espace avant le premier caractère :

```js
const string = `
First
Second`.trim()
```

### Interpolation

Les littéraux de gabarit fournissent un moyen facile d'interpoler des variables et des expressions dans des chaînes de caractères.

Vous le faites en utilisant la syntaxe `${...}` :

```js
const var = 'test'
const string = `something ${var}` //something test
```

à l'intérieur des `${}` vous pouvez ajouter n'importe quoi, même des expressions :

```js
const string = `something ${1 + 2 + 3}`
const string2 = `something ${foo() ? 'x' : 'y'}`
```

### Balises de gabarit

Les gabarits balisés sont une fonctionnalité qui peut sembler moins utile au premier abord, mais ils sont en fait utilisés par de nombreuses bibliothèques populaires, comme Styled Components ou Apollo, la bibliothèque client/serveur GraphQL, il est donc essentiel de comprendre comment cela fonctionne.

Dans Styled Components, les balises de gabarit sont utilisées pour définir des chaînes CSS :

```js
const Button = styled.button`
  font-size: 1.5em;
  background-color: black;
  color: white;
`
```

Dans Apollo, les balises de gabarit sont utilisées pour définir un schéma de requête GraphQL :

```js
const query = gql`
  query {
    ...
  }
`
```

Les balises de gabarit `styled.button` et `gql` mises en évidence dans ces exemples sont simplement des **fonctions** :

```js
function gql(literals, ...expressions) {}
```

cette fonction retourne une chaîne de caractères, qui peut être le résultat de _n'importe quel_ type de calcul.

`literals` est un tableau contenant le contenu du littéral de gabarit tokenisé par les interpolations d'expressions.

`expressions` contient toutes les interpolations.

Si nous prenons un exemple ci-dessus :

```js
const string = `something ${1 + 2 + 3}`
```

`literals` est un tableau avec deux éléments. Le premier est `something`, la chaîne jusqu'à la première interpolation, et le second est une chaîne vide, l'espace entre la fin de la première interpolation (nous n'en avons qu'une) et la fin de la chaîne.

`expressions` dans ce cas est un tableau avec un seul élément, `6`.

Un exemple plus complexe est :

```js
const string = `something
another ${'x'}
new line ${1 + 2 + 3}
test`
```

dans ce cas `literals` est un tableau où le premier élément est :

```js
;`something
another `
```

le second est :

```
;`new line `
```

et le troisième est :

```js
;`
new line `
```

`expressions` dans ce cas est un tableau avec deux éléments, `x` et `6`.

La fonction à laquelle ces valeurs sont passées peut faire n'importe quoi avec elles, et c'est la puissance de ce type de fonctionnalité.

L'exemple le plus simple est de reproduire ce que fait l'interpolation de chaîne, en joignant `literals` et `expressions` :

```js
const interpolated = interpolate`I paid ${10}€`
```

et voici comment fonctionne `interpolate` :

```js
function interpolate(literals, ...expressions) {
  let string = ``
  for (const [i, val] of expressions) {
    string += literals[i] + val
  }
  string += literals[literals.length - 1]
  return string
}
```

## Affectations par décomposition

Étant donné un objet, vous pouvez extraire certaines valeurs et les mettre dans des variables nommées :

```js
const person = {
  firstName: 'Tom',
  lastName: 'Cruise',
  actor: true,
  age: 54, //inventé
}

const {firstName: name, age} = person
```

`name` et `age` contiennent les valeurs souhaitées.

La syntaxe fonctionne également sur les tableaux :

```js
const a = [1,2,3,4,5]
const [first, second] = a
```

Cette instruction crée 3 nouvelles variables en obtenant les éléments avec les index 0, 1, 4 du tableau `a` :

## Littéraux d'objets améliorés

```js
const [first, second, , , fifth] = a
```

Dans ES2015, les littéraux d'objets ont gagné des superpouvoirs.

### Syntaxe plus simple pour inclure des variables

Au lieu de faire

```js
const something = 'y'
const x = {
  something: something
}
```

tu peux faire

```js
const something = 'y'
const x = {
  something
}
```

### Prototype

Un prototype peut être spécifié avec

```js
const anObject = { y: 'y' }
const x = {
  __proto__: anObject
}
```

### super()

```js
const anObject = { y: 'y', test: () => 'zoo' }
const x = {
  __proto__: anObject,
  test() {
    return super.test() + 'x'
  }
}
x.test() //zoox
```

### Propriétés dynamiques

```js
const x = {
  ['a' + '_' + 'b']: 'z'
}
x.a_b //z
```

## Boucle for-of

ES5, en 2009, a introduit les boucles `forEach()`. Bien que pratiques, elles n'offraient aucun moyen de sortir de la boucle, comme le faisaient les boucles `for`.

ES2015 a introduit la boucle `**for-of**`, qui combine la concision de `forEach` avec la capacité de sortir de la boucle :

```js
//itérer sur la valeur
for (const v of ['a', 'b', 'c']) {
  console.log(v);
}

//obtenir l'index également, en utilisant `entries()`
for (const [i, v] of ['a', 'b', 'c'].entries()) {
  console.log(index) //index
  console.log(value) //value
}
```

Remarquez l'utilisation de `const`. Cette boucle crée une nouvelle portée à chaque itération, donc nous pouvons l'utiliser en toute sécurité au lieu de `let`.

La différence avec `for...in` est :

* `for...of` **itère sur les valeurs des propriétés**
* `for...in` **itère sur les noms des propriétés**

## Promesses

Une promesse est communément définie comme **un proxy pour une valeur qui deviendra éventuellement disponible**.

Les promesses sont un moyen de gérer le code asynchrone, sans écrire trop de callbacks dans votre code.

Les **fonctions asynchrones** utilisent l'API des promesses comme leur bloc de construction, donc les comprendre est fondamental même si dans le code plus récent vous utiliserez probablement des fonctions asynchrones au lieu de promesses.

### Comment fonctionnent les promesses, en bref

Une fois qu'une promesse a été appelée, elle commence dans un **état en attente**. Cela signifie que la fonction appelante continue l'exécution, tandis qu'elle attend que la promesse effectue son propre traitement, et donne un retour à la fonction appelante.

À ce stade, la fonction appelante attend qu'elle retourne la promesse dans un **état résolu**, ou dans un **état rejeté**, mais comme vous le savez [JavaScript](https://flaviocopes.com/javascript/) est asynchrone, donc _la fonction continue son exécution pendant que la promesse fait son travail_.

### Quelles API JS utilisent les promesses ?

En plus de votre propre code et du code de bibliothèque, les promesses sont utilisées par les API Web modernes standard telles que :

* l'API Battery
* l'API [Fetch](https://flaviocopes.com/fetch-api/)
* les [Service Workers](https://flaviocopes.com/service-workers/)

Il est peu probable que dans le JavaScript moderne vous vous retrouviez à _ne pas_ utiliser les promesses, alors commençons à plonger directement dans celles-ci.

### Créer une promesse

L'API Promise expose un constructeur Promise, que vous initialisez en utilisant `new Promise()` :

```js
let done = true

const isItDoneYet = new Promise((resolve, reject) => {
  if (done) {
    const workDone = 'Here is the thing I built'
    resolve(workDone)
  } else {
    const why = 'Still working on something else'
    reject(why)
  }
})
```

Comme vous pouvez le voir, la promesse vérifie la constante globale `done`, et si elle est vraie, nous retournons une promesse résolue, sinon une promesse rejetée.

En utilisant `resolve` et `reject`, nous pouvons communiquer une valeur en retour, dans le cas ci-dessus, nous retournons simplement une chaîne, mais cela pourrait être un objet également.

### Consommer une promesse

Dans la dernière section, nous avons introduit comment une promesse est créée.

Maintenant, voyons comment la promesse peut être _consommée_ ou utilisée.

```js
const isItDoneYet = new Promise()
//...

const checkIfItsDone = () => {
  isItDoneYet
    .then(ok => {
      console.log(ok)
    })
    .catch(err => {
      console.error(err)
    })
}
```

L'exécution de `checkIfItsDone()` exécutera la promesse `isItDoneYet()` et attendra qu'elle se résolve, en utilisant le callback `then`, et s'il y a une erreur, elle la gérera dans le callback `catch`.

### Chaînage de promesses

Une promesse peut être retournée à une autre promesse, créant une chaîne de promesses.

Un excellent exemple de chaînage de promesses est donné par l'API [Fetch](https://flaviocopes.com/fetch-api), une couche au-dessus de l'API XMLHttpRequest, que nous pouvons utiliser pour obtenir une ressource et mettre en file d'attente une chaîne de promesses à exécuter lorsque la ressource est récupérée.

L'API Fetch est un mécanisme basé sur les promesses, et l'appel à `fetch()` est équivalent à définir notre propre promesse en utilisant `new Promise()`.

### Exemple de chaînage de promesses

```js
const status = response => {
  if (response.status >= 200 && response.status < 300) {
    return Promise.resolve(response)
  }
  return Promise.reject(new Error(response.statusText))
}

const json = response => response.json()

fetch('/todos.json')
  .then(status)
  .then(json)
  .then(data => {
    console.log('Request succeeded with JSON response', data)
  })
  .catch(error => {
    console.log('Request failed', error)
  })
```

Dans cet exemple, nous appelons `fetch()` pour obtenir une liste d'éléments TODO à partir du fichier `todos.json` trouvé à la racine du domaine, et nous créons une chaîne de promesses.

L'exécution de `fetch()` retourne une [réponse](https://fetch.spec.whatwg.org/#concept-response), qui a de nombreuses propriétés, et parmi celles-ci nous référençons :

* `status`, une valeur numérique représentant le code d'état HTTP
* `statusText`, un message d'état, qui est `OK` si la requête a réussi

`response` a également une méthode `json()`, qui retourne une promesse qui se résoudra avec le contenu du corps traité et transformé en JSON.

Étant donné ces prémisses, voici ce qui se passe : la première promesse de la chaîne est une fonction que nous avons définie, appelée `status()`, qui vérifie l'état de la réponse et si ce n'est pas une réponse de succès (entre 200 et 299), elle rejette la promesse.

Cette opération fera sauter toutes les promesses enchaînées listées et passera directement à l'instruction `catch()` en bas, enregistrant le texte `Request failed` ainsi que le message d'erreur.

Si cela réussit, elle appelle la fonction json() que nous avons définie. Puisque la promesse précédente, lorsqu'elle est réussie, a retourné l'objet `response`, nous l'obtenons comme entrée de la deuxième promesse.

Dans ce cas, nous retournons les données JSON traitées, donc la troisième promesse reçoit le JSON directement :

```js
.then((data) => {
  console.log('Request succeeded with JSON response', data)
})
```

et nous l'enregistrons dans la console.

### Gestion des erreurs

Dans l'exemple ci-dessus, dans la section précédente, nous avions un `catch` qui était ajouté à la chaîne de promesses.

Lorsque quelque chose dans la chaîne de promesses échoue et lève une erreur ou rejette la promesse, le contrôle passe à l'instruction `catch()` la plus proche dans la chaîne.

```js
new Promise((resolve, reject) => {
  throw new Error('Error')
}).catch(err => {
  console.error(err)
})

// ou

new Promise((resolve, reject) => {
  reject('Error')
}).catch(err => {
  console.error(err)
})
```

### Erreurs en cascade

Si à l'intérieur du `catch()` vous levez une erreur, vous pouvez ajouter un second `catch()` pour la gérer, et ainsi de suite.

```js
new Promise((resolve, reject) => {
  throw new Error('Error')
})
  .catch(err => {
    throw new Error('Error')
  })
  .catch(err => {
    console.error(err)
  })
```

### Orchestration des promesses

#### `Promise.all()`

Si vous devez synchroniser différentes promesses, `Promise.all()` vous aide à définir une liste de promesses, et à exécuter quelque chose lorsqu'elles sont toutes résolues.

Exemple :

```js
const f1 = fetch('/something.json')
const f2 = fetch('/something2.json')

Promise.all([f1, f2])
  .then(res => {
    console.log('Array of results', res)
  })
  .catch(err => {
    console.error(err)
  })
```

La syntaxe d'affectation par décomposition ES2015 vous permet également de faire

```js
Promise.all([f1, f2]).then(([res1, res2]) => {
  console.log('Results', res1, res2)
})
```

Vous n'êtes pas limité à utiliser `fetch` bien sûr, **toute promesse est bonne à prendre**.

#### `Promise.race()`

`Promise.race()` s'exécute dès qu'une des promesses que vous lui passez est résolue, et elle exécute le callback attaché une seule fois avec le résultat de la première promesse résolue.

Exemple :

```js
const promiseOne = new Promise((resolve, reject) => {
  setTimeout(resolve, 500, 'one')
})
const promiseTwo = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'two')
})

Promise.race([promiseOne, promiseTwo]).then(result => {
  console.log(result) // 'two'
})
```

## Modules

ES Modules est la norme ECMAScript pour travailler avec des modules.

Alors que Node.js utilise la norme CommonJS depuis des années, le navigateur n'a jamais eu de système de modules, car toute décision majeure telle qu'un système de modules doit d'abord être standardisée par ECMAScript puis implémentée par le navigateur.

Ce processus de standardisation s'est achevé avec ES2015 et les navigateurs ont commencé à implémenter cette norme en essayant de garder tout bien aligné, en travaillant tous de la même manière, et maintenant les ES Modules sont supportés dans Chrome, Safari, Edge et Firefox (depuis la version 60).

Les modules sont très cool, car ils vous permettent d'encapsuler toutes sortes de fonctionnalités, et d'exposer cette fonctionnalité à d'autres fichiers JavaScript, comme des bibliothèques.

### La syntaxe des ES Modules

La syntaxe pour importer un module est :

```js
import package from 'module-name'
```

tandis que CommonJS utilise

```js
const package = require('module-name')
```

Un module est un fichier JavaScript qui **exporte** une ou plusieurs valeurs (objets, fonctions ou variables), en utilisant le mot-clé `export`. Par exemple, ce module exporte une fonction qui retourne une chaîne en majuscules :

> _uppercase.js_

```js
export default str => str.toUpperCase()
```

Dans cet exemple, le module définit une seule **exportation par défaut**, donc il peut s'agir d'une fonction anonyme. Sinon, il aurait besoin d'un nom pour le distinguer des autres exportations.

Maintenant, **n'importe quel autre module JavaScript** peut importer la fonctionnalité offerte par uppercase.js en l'important.

Une page HTML peut ajouter un module en utilisant une balise `<script>` avec l'attribut spécial `type="module"` :

```js
<script type="module" src="index.js"></script>
```

> _Note : cette importation de module se comporte comme un chargement de script `defer`. Voir [charger efficacement JavaScript avec defer et async](https://flaviocopes.com/javascript-async-defer/)_

Il est important de noter que tout script chargé avec `type="module"` est chargé en mode strict.

Dans cet exemple, le module `uppercase.js` définit une **exportation par défaut**, donc lorsque nous l'importons, nous pouvons lui assigner un nom de notre choix :

```js
import toUpperCase from './uppercase.js'
```

et nous pouvons l'utiliser :

```js
toUpperCase('test') //'TEST'
```

Vous pouvez également utiliser un chemin absolu pour l'importation du module, pour référencer des modules définis sur un autre domaine :

```js
import toUpperCase from 'https://flavio-es-modules-example.glitch.me/uppercase.js'
```

Cette syntaxe d'importation est également valide :

```js
import { toUpperCase } from '/uppercase.js'
import { toUpperCase } from '../uppercase.js'
```

Ceci ne l'est pas :

```js
import { toUpperCase } from 'uppercase.js'
import { toUpperCase } from 'utils/uppercase.js'
```

C'est soit absolu, soit il a un `./` ou `/` avant le nom.

### Autres options d'import/export

Nous avons vu cet exemple ci-dessus :

```js
export default str => str.toUpperCase()
```

Cela crée une exportation par défaut. Dans un fichier, vous pouvez cependant exporter plus d'une chose, en utilisant cette syntaxe :

```js
const a = 1
const b = 2
const c = 3

export { a, b, c }
```

Un autre module peut importer toutes ces exportations en utilisant

```js
import * from 'module'
```

Vous pouvez importer seulement quelques-unes de ces exportations, en utilisant l'affectation par décomposition :

```js
import { a } from 'module'
import { a, b } from 'module'
```

Vous pouvez renommer n'importe quelle importation, pour plus de commodité, en utilisant `as` :

```js
import { a, b as two } from 'module'
```

Vous pouvez importer l'exportation par défaut, et toute exportation non par défaut par nom, comme dans cette importation React courante :

```js
import React, { Component } from 'react'
```

Vous pouvez voir un exemple de ES Modules ici : [https://glitch.com/edit/#!/flavio-es-modules-example?path=index.html](https://glitch.com/edit/#!/flavio-es-modules-example?path=index.html)

### CORS

Les modules sont récupérés en utilisant CORS. Cela signifie que si vous référencez des scripts d'autres domaines, ils doivent avoir un en-tête CORS valide qui permet le chargement inter-sites (comme `Access-Control-Allow-Origin: *`)

#### Et pour les navigateurs qui ne supportent pas les modules ?

Utilisez une combinaison de `type="module"` et `nomodule` :

```js
<script type="module" src="module.js"></script>
<script nomodule src="fallback.js"></script>
```

### Conclusion sur les modules

Les ES Modules sont l'une des plus grandes fonctionnalités introduites dans les navigateurs modernes. Ils font partie d'ES6 mais le chemin pour les implémenter a été long.

Nous pouvons maintenant les utiliser ! Mais nous devons aussi nous rappeler que le fait d'avoir plus de quelques modules aura un impact sur les performances de nos pages, car c'est une étape supplémentaire que le navigateur doit effectuer à l'exécution.

Webpack sera probablement encore un acteur majeur même si les ES Modules arrivent dans le navigateur, mais avoir une telle fonctionnalité directement intégrée dans le langage est énorme pour une unification de la façon dont les modules fonctionnent côté client et sur Node.js également.

## Nouvelles méthodes de chaîne de caractères

Toute valeur de chaîne de caractères a obtenu de nouvelles méthodes d'instance :

* `repeat()`
* `codePointAt()`

### repeat()

Répète les chaînes de caractères pour le nombre de fois spécifié :

```js
'Ho'.repeat(3) //'HoHoHo'
```

Retourne une chaîne vide s'il n'y a pas de paramètre, ou si le paramètre est `0`. Si le paramètre est négatif, vous obtiendrez une RangeError.

### codePointAt()

Cette méthode peut être utilisée pour gérer les caractères Unicode qui ne peuvent pas être représentés par une seule unité Unicode de 16 bits, mais qui en nécessitent 2.

En utilisant `charCodeAt()`, vous devez récupérer le premier et le second, et les combiner. En utilisant `codePointAt()`, vous obtenez le caractère entier en un seul appel.

Par exemple, ce caractère chinois "?" est composé de 2 parties UTF-16 (Unicode) :

```js
"?".charCodeAt(0).toString(16) //d842
"?".charCodeAt(1).toString(16) //dfb7
```

Si vous créez un nouveau caractère en combinant ces caractères unicode :

```js
"\ud842\udfb7" //"?"
```

Vous pouvez obtenir le même résultat avec `codePointAt()` :

```js
"?".codePointAt(0) //20bb7
```

Si vous créez un nouveau caractère en combinant ces caractères unicode :

```js
"\u{20bb7}" //"?"
```

Plus d'informations sur Unicode et son utilisation dans mon [guide Unicode](https://flaviocopes.com/unicode/).

## Nouvelles méthodes d'objet

ES2015 a introduit plusieurs méthodes statiques sous l'espace de noms Object :

* `Object.is()` détermine si deux valeurs sont la même valeur
* `Object.assign()` utilisé pour copier superficiellement un objet
* `Object.setPrototypeOf` définit un prototype d'objet

### Object.is()

Cette méthode vise à aider à comparer des valeurs.

Utilisation :

```js
Object.is(a, b)
```

Le résultat est toujours `false` sauf si :

* `a` et `b` sont le même objet exact
* `a` et `b` sont des chaînes égales (les chaînes sont égales lorsqu'elles sont composées des mêmes caractères)
* `a` et `b` sont des nombres égaux (les nombres sont égaux lorsque leur valeur est égale)
* `a` et `b` sont tous deux `undefined`, tous deux `null`, tous deux `NaN`, tous deux `true` ou tous deux `false`

`0` et `-0` sont des valeurs différentes en JavaScript, alors faites attention à ce cas spécial (convertissez tout en `+0` en utilisant l'opérateur unaire `+` avant de comparer, par exemple).

### Object.assign()

Introduit dans `ES2015`, cette méthode copie toutes les **propriétés propres énumérables** d'un ou plusieurs objets dans un autre.

Son cas d'utilisation principal est de créer une copie superficielle d'un objet.

```js
const copied = Object.assign({}, original)
```

Étant une copie superficielle, les valeurs sont clonées, et les références d'objets sont copiées (pas les objets eux-mêmes), donc si vous modifiez une propriété d'objet dans l'objet original, celle-ci est également modifiée dans l'objet copié, puisque l'objet interne référencé est le même :

```js
const original = {
  name: 'Fiesta',
  car: {
    color: 'blue'
  }
}

const copied = Object.assign({}, original)

original.name = 'Focus'
original.car.color = 'yellow'

copied.name //Fiesta
copied.car.color //yellow
```

J'ai mentionné "un ou plusieurs" :

```js
const wisePerson = {
  isWise: true
}
const foolishPerson = {
  isFoolish: true
}
const wiseAndFoolishPerson = Object.assign({}, wisePerson, foolishPerson)

console.log(wiseAndFoolishPerson) //{ isWise: true, isFoolish: true }
```

### Object.setPrototypeOf()

Définir le prototype d'un objet. Accepte deux arguments : l'objet et le prototype.

Utilisation :

```js
Object.setPrototypeOf(object, prototype)
```

Exemple :

```js
const animal = {
  isAnimal: true
}
const mammal = {
  isMammal: true
}

mammal.__proto__ = animal
mammal.isAnimal //true

const dog = Object.create(animal)

dog.isAnimal  //true
console.log(dog.isMammal)  //undefined

Object.setPrototypeOf(dog, mammal)

dog.isAnimal //true
dog.isMammal //true
```

### L'opérateur de propagation

Vous pouvez développer un tableau, un objet ou une chaîne de caractères en utilisant l'opérateur de propagation `...`

Commençons par un exemple de tableau. Étant donné

```js
const a = [1, 2, 3]
```

tu peux créer un nouveau tableau en utilisant

```js
const b = [...a, 4, 5, 6]
```

Tu peux aussi créer une copie d'un tableau en utilisant

```js
const c = [...a]
```

Cela fonctionne également pour les objets. Clone un objet avec :

```js
const newObj = { ...oldObj }
```

En utilisant des chaînes de caractères, l'opérateur de propagation crée un tableau avec chaque caractère de la chaîne :

```js
const hey = 'hey'
const arrayized = [...hey] // ['h', 'e', 'y']
```

Cet opérateur a quelques applications assez utiles. La plus importante est la capacité d'utiliser un tableau comme argument de fonction de manière très simple :

(Auparavant, vous pouviez faire cela en utilisant `f.apply(null, a)` mais ce n'est pas aussi agréable et lisible.)

L'**élément rest** est utile lors de la **décomposition de tableau** :

```js
const numbers = [1, 2, 3, 4, 5]
[first, second, ...others] = numbers
```

et **éléments de propagation** :

```js
const numbers = [1, 2, 3, 4, 5]
const sum = (a, b, c, d, e) => a + b + c + d + e
const sum = sum(...numbers)
```

ES2018 introduit les propriétés rest, qui sont les mêmes mais pour les objets.

**Propriétés rest** :

```js
const { first, second, ...others } = {
  first: 1,
  second: 2,
  third: 3,
  fourth: 4,
  fifth: 5
}

first // 1
second // 2
others // { third: 3, fourth: 4, fifth: 5 }
```

**Les propriétés de propagation** nous permettent de créer un nouvel objet en combinant les propriétés de l'objet passé après l'opérateur de propagation :

```js
const items = { first, second, ...others }
items //{ first: 1, second: 2, third: 3, fourth: 4, fifth: 5 }
```

## Set

Une structure de données Set nous permet d'ajouter des données à un conteneur.

Un Set est une collection d'objets ou de types primitifs (chaînes de caractères, nombres ou booléens), et vous pouvez le considérer comme une Map où les valeurs sont utilisées comme clés de map, avec la valeur de la map étant toujours un booléen vrai.

### Initialiser un Set

Un Set est initialisé en appelant :

```js
const s = new Set()
```

### Ajouter des éléments à un Set

Vous pouvez ajouter des éléments au Set en utilisant la méthode `add` :

```js
s.add('one')
s.add('two')
```

Un set ne stocke que des éléments uniques, donc appeler `s.add('one')` plusieurs fois n'ajoutera pas de nouveaux éléments.

Vous ne pouvez pas ajouter plusieurs éléments à un set en même temps. Vous devez appeler `add()` plusieurs fois.

### Vérifier si un élément est dans le set

Une fois qu'un élément est dans le set, nous pouvons vérifier si le set le contient :

```js
s.has('one') //true
s.has('three') //false
```

### Supprimer un élément d'un Set par clé

Utilisez la méthode `delete()` :

```js
s.delete('one')
```

### Déterminer le nombre d'éléments dans un Set

Utilisez la propriété `size` :

```js
s.size
```

### Supprimer tous les éléments d'un Set

Utilisez la méthode `clear()` :

```js
s.clear()
```

### Itérer les éléments dans un Set

Utilisez les méthodes `keys()` ou `values()` — elles sont équivalentes :

```js
for (const k of s.keys()) {
  console.log(k)
}

for (const k of s.values()) {
  console.log(k)
}
```

La méthode `entries()` retourne un itérateur, que vous pouvez utiliser comme ceci :

```js
const i = s.entries()
console.log(i.next())
```

appeler `i.next()` retournera chaque élément sous forme d'objet `{ value, done = false }` jusqu'à ce que l'itérateur se termine, moment auquel `done` est `true`.

Vous pouvez également utiliser la méthode forEach() sur le set :

```js
s.forEach(v => console.log(v))
```

ou vous pouvez simplement utiliser le set dans une boucle for..of :

```js
for (const k of s) {
  console.log(k)
}
```

### Initialiser un Set avec des valeurs

Vous pouvez initialiser un Set avec un ensemble de valeurs :

```js
const s = new Set([1, 2, 3, 4])
```

### Convertir les clés du Set en un tableau

```js
const a = [...s.keys()]

// ou

const a = [...s.values()]
```

### Un WeakSet

Un WeakSet est un type spécial de Set.

Dans un Set, les éléments ne sont jamais collectés par le garbage collector. Un WeakSet, en revanche, permet à tous ses éléments d'être librement collectés par le garbage collector. Chaque clé d'un WeakSet est un objet. Lorsque la référence à cet objet est perdue, la valeur peut être collectée par le garbage collector.

Voici les principales différences :

1. vous ne pouvez pas itérer sur le WeakSet
2. vous ne pouvez pas supprimer tous les éléments d'un WeakSet
3. vous ne pouvez pas vérifier sa taille

Un WeakSet est généralement utilisé par le code au niveau du framework, et n'expose que ces méthodes :

* add()
* has()
* delete()

## Map

Une structure de données Map nous permet d'associer des données à une clé.

### Avant ES6

Avant son introduction, les gens utilisaient généralement des objets comme des maps, en associant un objet ou une valeur à une valeur de clé spécifique :

```js
const car = {}
car['color'] = 'red'
car.owner = 'Flavio'
console.log(car['color']) //red
console.log(car.color) //red
console.log(car.owner) //Flavio
console.log(car['owner']) //Flavio
```

### Entrée de la Map

ES6 a introduit la structure de données Map, nous fournissant un outil approprié pour gérer ce type d'organisation de données.

Une Map est initialisée en appelant :

```js
const m = new Map()
```

### Ajouter des éléments à une Map

Vous pouvez ajouter des éléments à la map en utilisant la méthode `set` :

```js
m.set('color', 'red')
m.set('age', 2)
```

### Obtenir un élément d'une map par clé

Et vous pouvez obtenir des éléments d'une map en utilisant `get` :

```js
const color = m.get('color')
const age = m.get('age')
```

### Supprimer un élément d'une map par clé

Utilisez la méthode `delete()` :

```js
m.delete('color')
```

### Supprimer tous les éléments d'une map

Utilisez la méthode `clear()` :

```js
m.clear()
```

### Vérifier si une map contient un élément par clé

Utilisez la méthode `has()` :

```js
const hasColor = m.has('color')
```

### Trouver le nombre d'éléments dans une map

Utilisez la propriété `size` :

```js
const size = m.size
```

### Initialiser une map avec des valeurs

Vous pouvez initialiser une map avec un ensemble de valeurs :

```js
const m = new Map([['color', 'red'], ['owner', 'Flavio'], ['age', 2]])
```

### Clés de la map

Tout comme n'importe quelle valeur (objet, tableau, chaîne, nombre) peut être utilisée comme valeur de l'entrée clé-valeur d'un élément de map, **n'importe quelle valeur peut être utilisée comme clé**, même des objets.

Si vous essayez d'obtenir une clé inexistante en utilisant `get()` à partir d'une map, elle retournera `undefined`.

### Situations étranges que vous ne trouverez presque jamais dans la vie réelle

```js
const m = new Map()
m.set(NaN, 'test')
m.get(NaN) //test

const m = new Map()
m.set(+0, 'test')
m.get(-0) //test
```

### Itérer sur les clés de la map

Map offre la méthode `keys()` que nous pouvons utiliser pour itérer sur toutes les clés :

```js
for (const k of m.keys()) {
  console.log(k)
}
```

### Itérer sur les valeurs de la map

L'objet Map offre la méthode `values()` que nous pouvons utiliser pour itérer sur toutes les valeurs :

```js
for (const v of m.values()) {
  console.log(v)
}
```

### Itérer sur les paires clé-valeur de la map

L'objet Map offre la méthode `entries()` que nous pouvons utiliser pour itérer sur toutes les valeurs :

```js
for (const [k, v] of m.entries()) {
  console.log(k, v)
}
```

ce qui peut être simplifié en

```js
for (const [k, v] of m) {
  console.log(k, v)
}
```

### Convertir les clés de la map en un tableau

```js
const a = [...m.keys()]
```

### Convertir les valeurs de la map en un tableau

```js
const a = [...m.values()]
```

## WeakMap

Une WeakMap est un type spécial de map.

Dans un objet map, les éléments ne sont jamais collectés par le garbage collector. Une WeakMap, en revanche, permet à tous ses éléments d'être librement collectés par le garbage collector. Chaque clé d'une WeakMap est un objet. Lorsque la référence à cet objet est perdue, la valeur peut être collectée par le garbage collector.

Voici les principales différences :

1. vous ne pouvez pas itérer sur les clés ou les valeurs (ou les paires clé-valeur) d'une WeakMap
2. vous ne pouvez pas supprimer tous les éléments d'une WeakMap
3. vous ne pouvez pas vérifier sa taille

Une WeakMap expose ces méthodes, qui sont équivalentes à celles de Map :

* `get(k)`
* `set(k, v)`
* `has(k)`
* `delete(k)`

Les cas d'utilisation d'une WeakMap sont moins évidents que ceux d'une Map, et vous ne trouverez peut-être jamais le besoin de les utiliser, mais essentiellement elle peut être utilisée pour construire un cache sensible à la mémoire qui n'est pas susceptible d'interférer avec la collecte des déchets, ou pour une encapsulation soigneuse et la dissimulation d'informations.

## Générateurs

Les générateurs sont une sorte spéciale de fonction avec la capacité de se mettre en pause, et de reprendre plus tard, permettant à d'autres codes de s'exécuter entre-temps.

Voir le guide complet des générateurs JavaScript pour une explication détaillée du sujet.

Le code décide qu'il doit attendre, donc il laisse d'autres codes "dans la file d'attente" s'exécuter, et garde le droit de reprendre ses opérations "lorsque la chose qu'il attend" est terminée.

Tout cela est fait avec un seul mot-clé simple : `yield`. Lorsque qu'un générateur contient ce mot-clé, l'exécution est suspendue.

Un générateur peut contenir plusieurs mots-clés `yield`, suspendant ainsi son exécution plusieurs fois, et il est identifié par le mot-clé `*function`, qui ne doit pas être confondu avec l'opérateur de déréférencement de pointeur utilisé dans les langages de programmation de bas niveau tels que C, C++ ou Go.

Les générateurs permettent de nouveaux paradigmes de programmation en JavaScript, permettant :

* une communication bidirectionnelle pendant l'exécution d'un générateur
* des boucles while de longue durée qui ne gèlent pas votre programme

Voici un exemple de générateur qui explique comment tout cela fonctionne.

```js
function *calculator(input) {
    var doubleThat = 2 * (yield (input / 2))
    var another = yield (doubleThat)
    return (input * doubleThat * another)
}
```

Nous l'initialisons avec

```js
const calc = calculator(10)
```

Puis nous démarrons l'itérateur sur notre générateur :

```js
calc.next()
```

Cette première itération démarre l'itérateur. Le code retourne cet objet :

```js
{
  done: false
  value: 5
}
```

Ce qui se passe est : le code exécute la fonction, avec `input = 10` comme il a été passé dans le constructeur du générateur. Il s'exécute jusqu'à ce qu'il atteigne le `yield`, et retourne le contenu de `yield` : `input / 2 = 5`. Donc nous avons obtenu une valeur de 5, et l'indication que l'itération n'est pas terminée (la fonction est simplement en pause).

Dans la deuxième itération, nous passons la valeur `7` :

```js
calc.next(7)
```

et ce que nous avons obtenu en retour est :

```js
{
  done: false
  value: 14
}
```

`7` a été placé comme valeur de `doubleThat`. Important : vous pourriez lire comme si `input / 2` était l'argument, mais ce n'est que la valeur de retour de la première itération. Nous sautons cela maintenant, et utilisons la nouvelle valeur d'entrée, `7`, et la multiplions par 2.

Nous atteignons ensuite le deuxième yield, et celui-ci retourne `doubleThat`, donc la valeur retournée est `14`.

Dans l'itération suivante, et dernière, nous passons 100

```js
calc.next(100)
```

et en retour nous avons obtenu

```js
{
  done: true
  value: 14000
}
```

Comme l'itération est terminée (plus de mots-clés yield trouvés) et nous retournons simplement `(input * doubleThat * another)` qui équivaut à `10 * 14 * 100`.

---

Ce sont les fonctionnalités introduites dans ES2015. Plongeons maintenant dans ES2016 qui est beaucoup plus petit en termes de portée.

---

## Array.prototype.includes()

Cette fonctionnalité introduit une syntaxe plus lisible pour vérifier si un tableau contient un élément.

Avec ES6 et les versions antérieures, pour vérifier si un tableau contenait un élément, vous deviez utiliser `indexOf`, qui vérifie l'index dans le tableau, et retourne `-1` si l'élément n'est pas présent.

Puisque `-1` est évalué comme une valeur vraie, vous ne pouviez **pas** faire par exemple

```js
if (![1,2].indexOf(3)) {
  console.log('Not found')
}
```

Avec cette fonctionnalité introduite dans ES7, nous pouvons faire

```js
if (![1,2].includes(3)) {
  console.log('Not found')
}
```

# Opérateur d'exponentiation

L'opérateur d'exponentiation `**` est l'équivalent de `Math.pow()`, mais intégré dans le langage au lieu d'être une fonction de bibliothèque.

```js
Math.pow(4, 2) == 4 ** 2
```

Cette fonctionnalité est une belle addition pour les applications JS intensives en mathématiques.

L'opérateur `**` est standardisé dans de nombreux langages, y compris Python, Ruby, MATLAB, Lua, Perl et bien d'autres.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_ta8eBjBIGeJucahugjlopg.png)

---

Ce sont les fonctionnalités introduites en 2016. Plongeons maintenant dans 2017

---

# Remplissage de chaîne

Le but du remplissage de chaîne est d'**ajouter des caractères à une chaîne**, afin qu'elle **atteigne une longueur spécifique**.

ES2017 introduit deux méthodes `String` : `padStart()` et `padEnd()`.

```js
padStart(targetLength [, padString])
padEnd(targetLength [, padString])
```

Exemple d'utilisation :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_dn9xi0ABHBNXUClPtUMPEg.png)

## Object.values()

Cette méthode retourne un tableau contenant toutes les valeurs des propriétés propres de l'objet.

Utilisation :

```js
const person = { name: 'Fred', age: 87 }
Object.values(person) // ['Fred', 87]
```

`Object.values()` fonctionne également avec les tableaux :

```js
const people = ['Fred', 'Tony']
Object.values(people) // ['Fred', 'Tony']
```

## Object.entries()

Cette méthode retourne un tableau contenant toutes les propriétés propres de l'objet, sous forme de tableau de paires `[key, value]`.

Utilisation :

```js
const person = { name: 'Fred', age: 87 }
Object.entries(person) // [['name', 'Fred'], ['age', 87]]
```

`Object.entries()` fonctionne également avec les tableaux :

```js
const people = ['Fred', 'Tony']Object.entries(people) // [['0', 'Fred'], ['1', 'Tony']]
```

## Object.getOwnPropertyDescriptors()

Cette méthode retourne tous les descripteurs de propriétés propres (non héritées) d'un objet.

Tout objet en JavaScript a un ensemble de propriétés, et chacune de ces propriétés a un descripteur.

Un descripteur est un ensemble d'attributs d'une propriété, et il est composé d'un sous-ensemble des éléments suivants :

* **value** : la valeur de la propriété
* **writable** : vrai si la propriété peut être modifiée
* **get** : une fonction getter pour la propriété, appelée lorsque la propriété est lue
* **set** : une fonction setter pour la propriété, appelée lorsque la propriété est définie à une valeur
* **configurable** : si faux, la propriété ne peut pas être supprimée ni aucun attribut ne peut être modifié, sauf sa valeur
* **enumerable** : vrai si la propriété est énumérable

`Object.getOwnPropertyDescriptors(obj)` accepte un objet, et retourne un objet avec l'ensemble des descripteurs.

### En quoi est-ce utile ?

ES6 nous a donné `Object.assign()`, qui copie toutes les propriétés propres énumérables d'un ou plusieurs objets, et retourne un nouvel objet.

Cependant, il y a un problème avec cela, car il ne copie pas correctement les propriétés avec des attributs non par défaut.

Si un objet, par exemple, n'a qu'un setter, il n'est pas correctement copié dans un nouvel objet, en utilisant `Object.assign()`.

Par exemple avec

```js
const person1 = {
    set name(newName) {
        console.log(newName)
    }
}
```

Cela ne fonctionnera pas :

```js
const person2 = {}
Object.assign(person2, person1)
```

Mais cela fonctionnera :

```js
const person3 = {}Object.defineProperties(person3,  Object.getOwnPropertyDescriptors(person1))
```

Comme vous pouvez le voir avec un simple test de console :

```js
person1.name = 'x'
"x"

person2.name = 'x'

person3.name = 'x'
"x"
```

`person2` manque le setter, il n'a pas été copié.

La même limitation s'applique pour le clonage superficiel d'objets avec **Object.create()**.

## Virgules finales

Cette fonctionnalité permet d'avoir des virgules finales dans les déclarations de fonctions, et dans les appels de fonctions :

```js
const doSomething = (var1, var2,) => {
  //...
}

doSomething('test2', 'test2',)
```

Ce changement encouragera les développeurs à arrêter l'habitude laide de la "virgule au début de la ligne".

## Fonctions asynchrones

JavaScript a évolué en très peu de temps des callbacks aux promesses (ES2015), et depuis ES2017, JavaScript asynchrone est encore plus simple avec la syntaxe async/await.

Les fonctions asynchrones sont une combinaison de promesses et de générateurs, et essentiellement, elles sont une abstraction de plus haut niveau sur les promesses. Laissez-moi répéter : **async/await est construit sur les promesses**.

### Pourquoi async/await a-t-il été introduit ?

Ils réduisent le code répétitif autour des promesses, et la limitation "ne pas rompre la chaîne" de l'enchaînement des promesses.

Lorsque les promesses ont été introduites dans ES2015, elles étaient destinées à résoudre un problème avec le code asynchrone, et elles l'ont fait, mais au cours des 2 années qui ont séparé ES2015 et ES2017, il était clair que _les promesses ne pouvaient pas être la solution finale_.

Les promesses ont été introduites pour résoudre le célèbre problème de _l'enfer des callbacks_, mais elles ont introduit leur propre complexité, et une complexité syntaxique.

Elles étaient de bonnes primitives autour desquelles une meilleure syntaxe pouvait être exposée aux développeurs, donc lorsque le moment était venu, nous avons obtenu les **fonctions asynchrones**.

Elles font en sorte que le code semble synchrone, mais il est asynchrone et non bloquant en arrière-plan.

### Comment cela fonctionne

Une fonction asynchrone retourne une promesse, comme dans cet exemple :

```js
const doSomethingAsync = () => {
  return new Promise(resolve => {
    setTimeout(() => resolve('I did something'), 3000)
  })
}
```

Lorsque vous voulez **appeler** cette fonction, vous préfixez avec `await`, et **le code appelant s'arrêtera jusqu'à ce que la promesse soit résolue ou rejetée**. Une mise en garde : la fonction cliente doit être définie comme `async`. Voici un exemple :

```js
const doSomething = async () => {
  console.log(await doSomethingAsync())
}
```

### Un exemple rapide

Voici un exemple simple d'async/await utilisé pour exécuter une fonction de manière asynchrone :

```js
const doSomethingAsync = () => {
  return new Promise(resolve => {
    setTimeout(() => resolve('I did something'), 3000)
  })
}

const doSomething = async () => {
  console.log(await doSomethingAsync())
}

console.log('Before')
doSomething()
console.log('After')
```

Le code ci-dessus imprimera ce qui suit dans la console du navigateur :

```js
Before
After
I did something //after 3s
```

### Tout est promis

Préfixer le mot-clé `async` à n'importe quelle fonction signifie que la fonction retournera une promesse.

Même si elle ne le fait pas explicitement, elle le fera en interne.

C'est pourquoi ce code est valide :

```js
const aFunction = async () => {
  return 'test'
}

aFunction().then(alert) // Cela alertera 'test'
```

et c'est la même chose que :

```js
const aFunction = async () => {
  return Promise.resolve('test')
}

aFunction().then(alert) // Cela alertera 'test'
```

### Le code est beaucoup plus simple à lire

Comme vous pouvez le voir dans l'exemple ci-dessus, notre code semble très simple. Comparez-le au code utilisant des promesses simples, avec des chaînes et des fonctions de rappel.

Et ceci est un exemple très simple, les principaux avantages apparaîtront lorsque le code sera beaucoup plus complexe.

Par exemple, voici comment vous obtiendriez une ressource JSON, et la parseriez, en utilisant des promesses :

```js
const getFirstUserData = () => {
  return fetch('/users.json') // obtenir la liste des utilisateurs
    .then(response => response.json()) // parser JSON
    .then(users => users[0]) // choisir le premier utilisateur
    .then(user => fetch(`/users/${user.name}`)) // obtenir les données de l'utilisateur
    .then(userResponse => response.json()) // parser JSON
}

getFirstUserData()
```

Et voici la même fonctionnalité fournie en utilisant await/async :

```js
const getFirstUserData = async () => {
  const response = await fetch('/users.json') // obtenir la liste des utilisateurs
  const users = await response.json() // parser JSON
  const user = users[0] // choisir le premier utilisateur
  const userResponse = await fetch(`/users/${user.name}`) // obtenir les données de l'utilisateur
  const userData = await user.json() // parser JSON
  return userData
}

getFirstUserData()
```

### Plusieurs fonctions asynchrones en série

Les fonctions asynchrones peuvent être enchaînées très facilement, et la syntaxe est beaucoup plus lisible qu'avec les promesses simples :

```js
const promiseToDoSomething = () => {
  return new Promise(resolve => {
    setTimeout(() => resolve('I did something'), 10000)
  })
}

const watchOverSomeoneDoingSomething = async () => {
  const something = await promiseToDoSomething()
  return something + ' and I watched'
}

const watchOverSomeoneWatchingSomeoneDoingSomething = async () => {
  const something = await watchOverSomeoneDoingSomething()
  return something + ' and I watched as well'
}

watchOverSomeoneWatchingSomeoneDoingSomething().then(res => {
  console.log(res)
})
```

Imprimera :

```js
I did something and I watched and I watched as well
```

### Débogage plus facile

Le débogage des promesses est difficile car le débogueur ne passera pas sur le code asynchrone.

Async/await rend cela très facile car pour le compilateur, c'est comme du code synchrone.

## Mémoire partagée et atomiques

Les WebWorkers sont utilisés pour créer des programmes multithreads dans le navigateur.

Ils offrent un protocole de messagerie via des événements. Depuis ES2017, vous pouvez créer un tableau de mémoire partagée entre les web workers et leur créateur, en utilisant un `SharedArrayBuffer`.

Puisqu'il est inconnu combien de temps l'écriture dans une portion de mémoire partagée prend pour se propager, **Atomics** est un moyen de garantir que lors de la lecture d'une valeur, toute opération d'écriture est terminée.

Tout détail supplémentaire sur ce sujet [peut être trouvé dans la proposition de spécification](https://github.com/tc39/ecmascript_sharedmem/blob/master/TUTORIAL.md), qui a depuis été implémentée.

---

C'était ES2017. Laissez-moi maintenant vous présenter les fonctionnalités d'ES2018

---

## Propriétés Rest/Spread

ES2015 a introduit le concept d'un **élément rest** lors de la manipulation de la **décomposition de tableau** :

```js
const numbers = [1, 2, 3, 4, 5]
[first, second, ...others] = numbers
```

et **éléments de propagation** :

```js
const numbers = [1, 2, 3, 4, 5]
const sum = (a, b, c, d, e) => a + b + c + d + e
const sum = sum(...numbers)
```

ES2018 introduit la même chose mais pour les objets.

**Propriétés rest** :

```js
const { first, second, ...others } = { first: 1, second: 2, third: 3, fourth: 4, fifth: 5 }

first // 1
second // 2
others // { third: 3, fourth: 4, fifth: 5 }
```

**Les propriétés de propagation** permettent de créer un nouvel objet en combinant les propriétés de l'objet passé après l'opérateur de propagation :

```js
const items = { first, second, ...others }
items //{ first: 1, second: 2, third: 3, fourth: 4, fifth: 5 }
```

## Itération asynchrone

La nouvelle construction `for-await-of` vous permet d'utiliser un objet itérable asynchrone comme itération de boucle :

```js
for await (const line of readLines(filePath)) {
  console.log(line)
}
```

Puisque cela utilise `await`, vous ne pouvez l'utiliser qu'à l'intérieur des fonctions `async`, comme un `await` normal.

## Promise.prototype.finally()

Lorsque qu'une promesse est remplie, elle appelle les méthodes `then()` avec succès, l'une après l'autre.

Si quelque chose échoue pendant ce processus, les méthodes `then()` sont sautées et la méthode `catch()` est exécutée.

`finally()` vous permet d'exécuter du code indépendamment de l'exécution réussie ou non de la promesse :

```js
fetch('file.json')
  .then(data => data.json())
  .catch(error => console.error(error))
  .finally(() => console.log('finished'))
```

## Améliorations des expressions régulières

ES2018 a introduit un certain nombre d'améliorations concernant les expressions régulières. Je recommande mon tutoriel sur elles, disponible à [https://flaviocopes.com/javascript-regular-expressions/](https://flaviocopes.com/javascript-regular-expressions/).

Voici les ajouts spécifiques à ES2018.

### Assertions de rétrovisée des RegExp : faire correspondre une chaîne en fonction de ce qui la précède

Ceci est une anticipation : vous utilisez `?=` pour faire correspondre une chaîne qui est suivie d'une sous-chaîne spécifique :

```js
/Roger(?=Waters)/

/Roger(?= Waters)/.test('Roger is my dog') //false
/Roger(?= Waters)/.test('Roger is my dog and Roger Waters is a famous musician') //true
```

`?!` effectue l'opération inverse, en faisant correspondre si une chaîne n'est **pas** suivie d'une sous-chaîne spécifique :

```js
/Roger(?!Waters)/

/Roger(?! Waters)/.test('Roger is my dog') //true
/Roger(?! Waters)/.test('Roger Waters is a famous musician') //false
```

Les anticipations utilisent le symbole `?=`. Elles étaient déjà disponibles.

**Les rétrovisées**, une nouvelle fonctionnalité, utilisent `?<=`.

```js
/(?<=Roger) Waters/

/(?<=Roger) Waters/.test('Pink Waters is my dog') //false
/(?<=Roger) Waters/.test('Roger is my dog and Roger Waters is a famous musician') //true
```

Une rétrovisée est niée en utilisant `?<!` :

```js
/(?<!Roger) Waters/

/(?<!Roger) Waters/.test('Pink Waters is my dog') //true
/(?<!Roger) Waters/.test('Roger is my dog and Roger Waters is a famous musician') //false
```

### Échappements de propriétés Unicode \p{...} et \P{...}

Dans un motif d'expression régulière, vous pouvez utiliser `\d` pour faire correspondre n'importe quel chiffre, `\s` pour faire correspondre n'importe quel caractère qui n'est pas un espace blanc, `\w` pour faire correspondre n'importe quel caractère alphanumérique, et ainsi de suite.

Cette nouvelle fonctionnalité étend ce concept à tous les caractères Unicode en introduisant `\p{}` et sa négation `\P{}`.

Tout caractère Unicode a un ensemble de propriétés. Par exemple, `Script` détermine la famille de langues, `ASCII` est un booléen qui est vrai pour les caractères ASCII, et ainsi de suite. Vous pouvez mettre cette propriété dans les parenthèses du graphe, et l'expression régulière vérifiera si elle est vraie :

```js
/^\p{ASCII}+$/u.test('abc')   //✅
/^\p{ASCII}+$/u.test('ABC@')  //✅
/^\p{ASCII}+$/u.test('ABC?') //❌
```

`ASCII_Hex_Digit` est une autre propriété booléenne, qui vérifie si la chaîne ne contient que des chiffres hexadécimaux valides :

```js
/^\p{ASCII_Hex_Digit}+$/u.test('0123456789ABCDEF') //✅
/^\p{ASCII_Hex_Digit}+$/u.test('h')                //❌
```

Il existe de nombreuses autres propriétés booléennes, que vous vérifiez simplement en ajoutant leur nom dans les parenthèses du graphe, y compris `Uppercase`, `Lowercase`, `White_Space`, `Alphabetic`, `Emoji` et plus encore :

```js
/^\p{Lowercase}$/u.test('h') //✅
/^\p{Uppercase}$/u.test('H') //✅

/^\p{Emoji}+$/u.test('H')   //❌
/^\p{Emoji}+$/u.test('??') //✅
```

En plus de ces propriétés binaires, vous pouvez vérifier l'une des propriétés des caractères Unicode pour faire correspondre une valeur spécifique. Dans cet exemple, je vérifie si la chaîne est écrite en alphabet grec ou latin :

```js
/^\p{Script=Greek}+$/u.test('ελληνικά') //✅
/^\p{Script=Latin}+$/u.test('hey') //✅
```

Lisez plus sur toutes les propriétés que vous pouvez utiliser [directement sur la proposition](https://github.com/tc39/proposal-regexp-unicode-property-escapes).

### Groupes de capture nommés

Dans ES2018, un groupe de capture peut être assigné à un nom, plutôt que d'être simplement assigné à un emplacement dans le tableau de résultats :

```js
const re = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/
const result = re.exec('2015-01-02')

// result.groups.year === '2015';
// result.groups.month === '01';
// result.groups.day === '02';
```

### Le drapeau s pour les expressions régulières

Le drapeau `s`, abréviation de _single line_, fait en sorte que le `.` corresponde également aux caractères de nouvelle ligne. Sans lui, le point correspond aux caractères réguliers mais pas à la nouvelle ligne :

```js
/hi.welcome/.test('hi\nwelcome') // false
/hi.welcome/s.test('hi\nwelcome') // true
```

---

## ESNext

Qu'est-ce qui suit ? ESNext.

ESNext est un nom qui indique toujours la prochaine version de JavaScript.

La version actuelle d'ECMAScript est **ES2018**. Elle a été publiée en juin 2018.

Historiquement, les éditions de JavaScript ont été standardisées pendant l'été, donc nous pouvons nous attendre à ce que **ECMAScript 2019** soit publié à l'été 2019.

Ainsi, au moment de l'écriture, ES2018 a été publié, et **ESNext est ES2019**

Les propositions pour la norme ECMAScript sont organisées en étapes. Les étapes 1 à 3 sont un incubateur de nouvelles fonctionnalités, et les fonctionnalités atteignant l'étape 4 sont finalisées dans le cadre de la nouvelle norme.

Au moment de l'écriture, nous avons un certain nombre de fonctionnalités à l'**étape 4**. Je vais les présenter dans cette section. Les dernières versions des principaux navigateurs devraient déjà implémenter la plupart de celles-ci.

Certains de ces changements sont principalement pour un usage interne, mais il est également bon de savoir ce qui se passe.

Il y a d'autres fonctionnalités à l'étape 3, qui pourraient être promues à l'étape 4 dans les prochains mois, et vous pouvez les consulter sur ce dépôt GitHub : [https://github.com/tc39/proposals](https://github.com/tc39/proposals).

## Array.prototype.{flat,flatMap}

`flat()` est une nouvelle méthode d'instance de tableau qui peut créer un tableau unidimensionnel à partir d'un tableau multidimensionnel.

Exemple :

```js
['Dog', ['Sheep', 'Wolf']].flat()
//[ 'Dog', 'Sheep', 'Wolf' ]
```

Par défaut, il ne "platise" qu'à un niveau, mais vous pouvez ajouter un paramètre pour définir le nombre de niveaux auxquels vous souhaitez platiser le tableau. Définissez-le sur `Infinity` pour avoir des niveaux illimités :

```js
['Dog', ['Sheep', ['Wolf']]].flat()
//[ 'Dog', 'Sheep', [ 'Wolf' ] ]

['Dog', ['Sheep', ['Wolf']]].flat(2)
//[ 'Dog', 'Sheep', 'Wolf' ]

['Dog', ['Sheep', ['Wolf']]].flat(Infinity)
//[ 'Dog', 'Sheep', 'Wolf' ]
```

Si vous êtes familier avec la méthode JavaScript `map()` d'un tableau, vous savez que vous pouvez exécuter une fonction sur chaque élément d'un tableau.

`flatMap()` est une nouvelle méthode d'instance de tableau qui combine `flat()` avec `map()`. Elle est utile lorsque vous appelez une fonction qui retourne un tableau dans le callback de map(), mais vous voulez que votre tableau résultant soit plat :

```js
['My dog', 'is awesome'].map(words => words.split(' '))
//[ [ 'My', 'dog' ], [ 'is', 'awesome' ] ]

['My dog', 'is awesome'].flatMap(words => words.split(' '))
//[ 'My', 'dog', 'is', 'awesome' ]
```

### Liaison de capture optionnelle

Parfois, nous n'avons pas besoin d'avoir un paramètre lié au bloc catch d'un try/catch.

Nous devions auparavant faire :

```js
try {
  //...
} catch (e) {
  //gérer l'erreur
}
```

Même si nous n'avions jamais besoin d'utiliser `e` pour analyser l'erreur. Nous pouvons maintenant simplement l'omettre :

```js
try {
  //...
} catch {
  //gérer l'erreur
}
```

## Object.fromEntries()

Les objets ont une méthode `entries()`, depuis ES2017.

Elle retourne un tableau contenant toutes les propriétés propres de l'objet, sous forme de tableau de paires `[key, value]` :

```js
const person = { name: 'Fred', age: 87 }
Object.entries(person) // [['name', 'Fred'], ['age', 87]]
```

ES2019 introduit une nouvelle méthode `Object.fromEntries()`, qui peut créer un nouvel objet à partir d'un tel tableau de propriétés :

```js
const person = { name: 'Fred', age: 87 }
const entries = Object.entries(person)
const newPerson = Object.fromEntries(entries)

person !== newPerson //true 
```

## String.prototype.{trimStart,trimEnd}

Cette fonctionnalité fait partie de v8/Chrome depuis presque un an maintenant, et elle va être standardisée dans ES2019.

## `trimStart()`

Retourne une nouvelle chaîne avec les espaces blancs supprimés du début de la chaîne originale

```js
'Testing'.trimStart() //'Testing'
' Testing'.trimStart() //'Testing'
' Testing '.trimStart() //'Testing '
'Testing'.trimStart() //'Testing'
```

## `trimEnd()`

Retourne une nouvelle chaîne avec les espaces blancs supprimés de la fin de la chaîne originale

```js
'Testing'.trimEnd() //'Testing'
' Testing'.trimEnd() //' Testing'
' Testing '.trimEnd() //' Testing'
'Testing '.trimEnd() //'Testing'
```

## Symbol.prototype.description

Vous pouvez maintenant récupérer la description d'un symbole en accédant à sa propriété `description` au lieu d'avoir à utiliser la méthode `toString()` :

```js
const testSymbol = Symbol('Test')
testSymbol.description // 'Test'
```

## Améliorations JSON

Avant ce changement, les symboles de séparateur de ligne (\u2028) et de séparateur de paragraphe (\u2029) n'étaient pas autorisés dans les chaînes analysées en tant que JSON.

En utilisant JSON.parse(), ces caractères entraînaient une `SyntaxError`, mais maintenant ils sont analysés correctement, comme défini par la norme JSON.

### JSON.stringify() bien formé

Corrige la sortie de `JSON.stringify()` lorsqu'elle traite les points de code UTF-8 de substitution (U+D800 à U+DFFF).

Avant ce changement, l'appel de `JSON.stringify()` retournait un caractère Unicode mal formé (un "").

Maintenant, ces points de code de substitution peuvent être représentés en toute sécurité sous forme de chaînes à l'aide de `JSON.stringify()`, et transformés en leur représentation d'origine à l'aide de `JSON.parse()`.

## Function.prototype.toString()

Les fonctions ont toujours eu une méthode d'instance appelée `toString()` qui retourne une chaîne contenant le code de la fonction.

ES2019 a introduit un changement dans la valeur de retour pour éviter de supprimer les commentaires et autres caractères comme les espaces blancs, représentant exactement la fonction telle qu'elle a été définie.

Si auparavant nous avions

```js
function /* this is bar */ bar () {}
```

Le comportement était le suivant :

```js
bar.toString() //'function bar() {}
```

maintenant le nouveau comportement est :

```js
bar.toString(); // 'function /* this is bar */ bar () {}'
```

---

En conclusion, j'espère que cet article vous a aidé à vous mettre à jour sur certaines des dernières additions à JavaScript, et les nouvelles fonctionnalités que nous verrons en 2019.

[**Cliquez ici pour obtenir une version PDF / ePub / Mobi de cet article à lire hors ligne**](https://flaviocopes.com/page/es5-to-esnext)

Flavio