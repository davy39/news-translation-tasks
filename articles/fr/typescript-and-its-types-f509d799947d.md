---
title: Un tour rapide mais approfondi de TypeScript et de ses types
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T15:01:01.000Z'
originalURL: https://freecodecamp.org/news/typescript-and-its-types-f509d799947d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ug5XILnTeW5IJ7HUOAprkw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Un tour rapide mais approfondi de TypeScript et de ses types
seo_desc: 'By David Piepgrass

  Union types, generics, JSX, type system loopholes and more!


  _Photo by [Unsplash](https://unsplash.com/photos/sGlwpgB7ENM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">L...'
---

Par David Piepgrass

#### Types d'union, génériques, JSX, failles du système de types et plus encore !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ug5XILnTeW5IJ7HUOAprkw.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/sGlwpgB7ENM?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Luis Villasmil</a> sur <a href="https://unsplash.com/search/photos/types?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Ce tour rapide de TypeScript s'adresse principalement aux personnes ayant une certaine expérience avec JavaScript.

Je vais également expliquer quelques faits surprenants sur JavaScript, au cas où vous n'auriez étudié que quelque chose de vaguement similaire, comme Java ou C#. Si vous souhaitez savoir comment configurer un projet TypeScript, consultez mon [article précédent](https://medium.freecodecamp.org/how-to-set-up-a-typescript-project-67b427114884).

TypeScript est basé sur JavaScript. Le compilateur TypeScript (ou d'autres outils basés sur celui-ci, comme `ts-node` ou `ts-jest`) traduit TypeScript en JavaScript normal simplement en supprimant toutes les informations de type.

Parallèlement à ce processus, une vérification de type est effectuée afin de découvrir des **erreurs de type** — des erreurs que vous avez commises et qui ont quelque chose à voir avec les types. Bien sûr, occasionnellement, il se plaint également des choses que vous avez faites intentionnellement mais qui ont nevertheless enfreint les règles de TypeScript.

### Types

Les types peuvent être attachés aux variables avec un deux-points (:) dans leur définition, comme ceci :

```
let z: number = 26;
```

Cependant, vous n'avez souvent pas besoin d'**écrire** le type. Par exemple, si vous écrivez :

```
let z = 26;
```

TypeScript **infère** que z est un nombre. Donc si vous écrivez :

```
let z = 26;z = "Not a number";
```

Vous obtiendrez une erreur sur la deuxième ligne. TypeScript a initialement adopté une faille : toute variable peut être `null` ou `undefined` :

```
z = null;      // Autorisé !z = undefined; // Autorisé ! 
```

Si vous êtes nouveau dans JavaScript, vous vous demandez probablement ce que sont `null` et `undefined`, ou [pourquoi ils sont deux choses différentes](https://stackoverflow.com/questions/5076944/what-is-the-difference-between-null-and-undefined-in-javascript).

Eh bien, j'ai promis de vous parler de **TypeScript** et `null`/`undefined` sont des **choses JavaScript**. Ha !

Personnellement, je n'utilise pas beaucoup `null`. Je trouve pratique d'utiliser `undefined` de manière cohérente pour éviter de m'inquiéter de la distinction. `undefined` est la valeur par défaut des nouvelles variables et des paramètres de fonction qui n'ont pas été fournis par l'appelant. C'est la valeur que vous obtenez si vous lisez une propriété qui n'existe pas sur un objet. En revanche, JavaScript lui-même utilise rarement `null`, donc si vous ne l'utilisez pas vous-même, vous ne le rencontrerez pas très souvent. Je suis sûr que certaines personnes font le contraire et préfèrent `null`.

Quoi qu'il en soit, certaines personnes — y compris moi — sont d'avis que permettre à **toutes** les variables d'être `null`/`undefined` était une mauvaise idée. Donc TypeScript 2.0 [vous permet de retirer cette permission](https://blog.mariusschulz.com/2016/09/27/typescript-2-0-non-nullable-types) avec l'option de compilateur `"strictNullChecks": true` dans "tsconfig.json". Vous pouvez utiliser `"strict": true` pour une vérification de type maximale. Au lieu de cela, vous écririez :

```
let z: number | null = 26;
```

si vous **voulez** que `z` puisse potentiellement être `null` (| signifie "ou").

#### Types d'union

TypeScript a la capacité de comprendre les variables qui peuvent avoir plusieurs types. Par exemple, voici un code JavaScript normal :

Ceci est autorisé dans TypeScript par défaut, car `var y` (par lui-même) donne à `y` un type de `any`, signifiant n'importe quoi. Donc nous pouvons assigner n'importe quoi, par exemple une valeur ou un objet, à `y`. Nous pouvons certainement le définir comme une chaîne, ou un nombre, ou un tableau de deux choses. `any` est un type spécial — il signifie "cette valeur ou variable devrait se comporter comme une valeur ou une variable JavaScript et, par conséquent, ne pas me donner d'erreurs de type."

Je recommande l'option de compilateur `"strict": true`. Mais, dans ce mode, TypeScript n'autorise pas `var y` — il nécessite `var y: any` à la place.

Cependant, TypeScript nous permet d'être plus spécifiques en disant :

```
var y: string | number;
```

Cela signifie "la variable y est une chaîne ou un nombre". Si `y` est créé de cette manière, en utilisant l'exemple ci-dessus, la partie `if-else` est autorisée. Mais l'autre partie qui dit `y = [y, y]` n'est pas autorisée, car `[y, y]` n'est ni une chaîne ni un nombre. `y` est un tableau de type `number[] | string[]`. Cette fonctionnalité, dans laquelle une variable peut avoir l'un des deux (ou plus) types, est appelée **types d'union** et elle est souvent utile.

**Astuce :** Pour vous aider à apprendre TypeScript, il peut être utile de [faire des expériences dans le playground](http://www.typescriptlang.org/play/).  
   
Pour vous aider à en apprendre davantage sur **JavaScript**, appuyez sur F12 dans Chrome, Firefox ou Edge et cherchez la Console. Dans la console, vous pouvez écrire du code JavaScript, pour découvrir ce que fait un petit morceau de JavaScript et si vous l'écrivez correctement :

![Image](https://cdn-media-1.freecodecamp.org/images/0*vecftDpvTNmd-nJt.png)

Cette console est fantastique car vous pouvez l'utiliser pour effectuer des expériences dans _n'importe quel_ onglet du navigateur — même celui-ci ! Puisque TypeScript est simplement JavaScript avec une vérification de type statique, vous pouvez utiliser la console pour vous aider à apprendre la partie de TypeScript qui _n'a pas_ de types statiques. Dans votre fichier TypeScript, vous pouvez appeler `console.log(something)` pour imprimer des choses dans la console du navigateur. Dans certains navigateurs, `log` peut afficher des objets complexes. Par exemple, essayez d'écrire `console.log({name:"Steve", age:37, favoriteNumbers:[7, 666, -1]})` :

![Image](https://cdn-media-1.freecodecamp.org/images/0*6l1UncVlSmswuaAO.png)

### Classes

Comme vous le savez, les classes sont des ensembles de fonctions et de variables qui peuvent être instanciées en plusieurs objets. Les fonctions à l'intérieur des classes peuvent faire référence à d'autres fonctions et variables à l'intérieur de la classe, mais en JavaScript et TypeScript, vous devez utiliser le préfixe `this.` Une classe JavaScript typique pourrait ressembler à ceci :

La sortie de la console est :

```
The big box is 10000 times larger than the small oneThe zero-size box has an area of 0.
```

JavaScript est un peu pointilleux. Lorsque vous créez une fonction en dehors d'une classe, elle a le mot `function` devant elle. Mais, lorsque vous créez une fonction à l'intérieur d'une `class`, il est **interdit** d'avoir le mot `function` devant elle.

Les fonctions et les méthodes sont la même chose, sauf que les méthodes dans les classes ont accès à `this` — une référence à l'objet courant, sauf pour les méthodes `static`. Les méthodes `static` sont appelées sur la `class`, `Box.ZeroSize` dans cet exemple, donc elles n'ont pas d'« objet courant ». (Eh bien, en fait, l'objet courant de `ZeroSize` est la fonction constructeur `Box`, qui n'est _pas_ une instance de `Box`.)

Contrairement à JavaScript, les classes TypeScript permettent les déclarations de variables, telles que `width` et `height` dans cet exemple :

Pour plus de commodité, TypeScript vous permet de définir un constructeur et les variables qu'il initialise en même temps. Donc au lieu de

```
  width: number;  height: number;  constructor(width: number, height: number) {    this.width = width;    this.height = height;  }
```

you pouvez simplement écrire

```
constructor(public width: number, public height: number) {}
```

Au fait, pour tous les développeurs C# qui lisent ceci, cela fonctionne exactement comme mon [système LeMP](http://ecsharp.net/lemp/) pour C#.

Contrairement à JavaScript, TypeScript a des variables et fonctions `private` (et `protected`) qui sont inaccessibles en dehors de la classe :

Les variables `private` vous permettent de marquer clairement les parties d'une classe comme "internes". Les utilisateurs de la classe ne peuvent pas modifier ou lire celles-ci.

### Interfaces

Les interfaces sont un moyen de décrire les "formes" des objets. Voici un exemple :

`IBox` fait référence à toute classe qui a une propriété `width` et `height` qui sont des nombres lisibles. `IArea` fait référence à tout ce qui a une propriété `area` lisible. La classe `Box` satisfait ces deux exigences. La fonction `get area()` est considérée comme une propriété, car elle est appelée sans les parenthèses `()`. Donc je pourrais écrire :

```
let a: IBox = new Box(10,100);  // OKlet b: IArea = new Box(10,100); // OK
```

Les interfaces dans TypeScript fonctionnent comme les interfaces dans le langage de programmation Go, et non comme les interfaces en Java et C#. C'est une bonne chose. Cela signifie que les classes **n'ont pas** à dire explicitement qu'elles implémentent une interface. `Box` implémente `IBox` et `IArea` sans le dire.

Cela signifie que nous pouvons définir des interfaces pour des types qui n'étaient pas initialement conçus pour une interface particulière. Par exemple, mon package [BTree](https://www.npmjs.com/package/sorted-btree) définit une interface `IMap<Key,V`al> qui représente un dictionnaire de paires clé-valeur. La nouvelle classe Map intégrée dans ES6 respecte également cette interface, donc vous pouvez `put` une Map dans une variable IMap. Donc, par exemple, vous pouvez écrire une fonction avec un paramètre IMap, et vous pouvez passer une Map ou un BTree à la fonction, et la fonction n'a pas besoin de savoir ou de se soucier du type qu'elle a reçu.

`readonly` signifie que nous pouvons lire, mais pas changer :

```
console.log(`The box is ${a.width} by ${a.height}.`); // OKa.width = 2; /* ERR: Cannot assign to 'width' because it is a                      constant or a read-only property. */
```

TypeScript n'exige pas `readonly` pour la compatibilité des interfaces. Par exemple, TypeScript accepte ce code même s'il ne fonctionne pas :

```
interface IArea {  area: number; // area is not readonly, so it can be changed}
```

```
let ia: IArea = new Box(10,100);ia.area = 5; // Accepted by TypeScript, but causes a runtime error
```

Je pense que c'est un bug dans TypeScript.

TypeScript a également un concept de parties optionnelles d'une interface :

```
interface Person {  readonly name: string;  readonly age: number;  readonly spouse?: Person;}
```

Par exemple, nous pouvons écrire `let p: Person = {name:'John Doe', age:37}`. Puisque `p` est une `Person`, nous pouvons plus tard faire référence à `p.spouse`. Cela est égal à `undefined` dans ce cas, mais pourrait être une `Person` si un objet différent lui était assigné qui a un `spouse`.

Cependant, si vous utilisez `p = {name:'Chad', age:19, spouse:'Jennifer'}` avec le mauvais type de données pour `spouse`, TypeScript répond que `Type string is not assignable to type Person _|_ undefined`_._

### Types d'intersection

Les types d'intersection sont les cousins moins connus des types d'union. Un type d'union comme `A | B` signifie qu'une valeur peut être **soit** un A ou un B, mais pas les deux. Un type d'intersection comme `A & B` signifie qu'une valeur est à la fois A et B en même temps. Par exemple, cette `box` est à la fois `IBox` et `IArea`, donc elle a toutes les propriétés des deux interfaces :

```
let box: IBox & IArea = new Box(5, 7);
```

Si vous mélangez les types d'union et d'intersection, vous pouvez utiliser des parenthèses pour changer le sens :

```
// soit un Date&IArea ou IBox&IArealet box1: (Date | IBox) & IArea = new Box(5, 7);// soit un Date ou un IBox&IArealet box2: Date | (IBox & IArea) = new Box(5, 7);
```

`&` a une priorité plus élevée que `|`, donc `A & B | C` signifie `(A & B) | C`.

### Types structurels

Dans certains autres langages de programmation, chaque type a un nom, comme `string` ou `double` ou `Component`. Dans TypeScript, de nombreux types ont des noms mais, plus fondamentalement, la plupart des types sont définis par leur structure. En d'autres termes, le nom du type, s'il en a un, n'est pas important pour le système de types. Voici un exemple où les variables ont un type structurel :

```
var book1 = { title: "Adventures of Tom Sawyer",       year:1876 };var book2 = { title: "Adventures of Huckleberry Finn", year:1884 };
```

Si vous passez votre souris sur `book1` dans VS Code, son type est décrit comme `{ title: string; year: number; }`. Il s'agit d'un type **structurel** : un type défini entièrement par le fait qu'il a une propriété appelée `title` qui est une `string`, et une autre propriété appelée `year` qui est un `number`. Ainsi, `book1` et `book2` ont le même type, et vous pouvez assigner l'un à l'autre, ou à un livre différent.

```
book1 = book2; // allowedbook2 = { year: 1995, title: "Vertical Run" }; // allowed
```

En général, vous pouvez assigner une valeur avec "plus de choses" à une variable dont le type inclut "moins de choses", mais pas l'inverse :

```
var book3 = { title: "The Duplicate",               author: "William Sleator", year:1988 };var book4 = { title: "The Boy Who Reversed Himself" };book1 = book3; // allowedbool1 = bool4; /* NOT allowed. Here is the error message:    Type '{ title: string; }' is not assignable to type     '{ title: string; year: number; }'. Property 'year'     is missing in type '{ title: string; }'.  */ 
```

En outre, si nous avons une interface comme celle-ci :

```
interface Book {  title: string;  author?: string;  year: number;}
```

Alors nous pouvons assigner n'importe quelle valeur `Book` à `book1` ou `book2`. Mais `author` est requis dans `book3` et `Book` peut ne pas contenir d'auteur. Nous pouvons assigner n'importe laquelle des variables de livre à une nouvelle variable de type `Book`, sauf `book4`, bien sûr.

Clairement, les types structurels sont fantastiques. Cela est évident après avoir passé quelques années à utiliser des langages sans eux. Par exemple, imaginez si deux personnes, Alfred et Barbara, écrivent différents modules `A` et `B`. Ils traitent tous deux des points en utilisant des coordonnées X-Y. Donc chaque module contient une interface `Point` :

```
interface Point {    x: number;    y: number;}
```

De nombreux langages utilisent des types **nominaux** au lieu de types structurels. Dans ces langages, `A.Point` est considéré comme un type complètement différent de `B.Point` même s'ils sont identiques. Donc tout point produit par `A` ne peut pas être utilisé par `B` et vice versa. Cela peut être frustrant, alors prenez un moment pour célébrer avec moi la merveille de la typographie structurelle de TypeScript.

Les types structurels peuvent être écrits soit avec des points-virgules, soit avec des virgules, par exemple `{ x: number, y: number }` et `{ x: number; y: number; }` sont identiques.

### Typage basé sur le flux et le point d'exclamation

Si `s` est une chaîne, vous pourriez écrire `s.match(_/[0-9]+/_)` pour trouver le premier groupe de chiffres dans cette chaîne. `/[0-9]+/` est un `RegExp` — un objet qui peut être utilisé pour rechercher des chaînes en utilisant des [Expressions Régulières](https://en.wikipedia.org/wiki/Regular_expression). Les expressions régulières sont un système de correspondance de chaînes pris en charge par de nombreux langages de programmation, y compris JavaScript.

`match` retourne un tableau de chaînes, ou `null` si le `RegExp` n'a pas correspondu à la chaîne. Par exemple, si `s = "I have 10 cats and 2 dogs"` alors `s.match(/[0-9]+/)` retourne `["10"]`, mais si `s = "I have ten velociraptors and a weevil"` alors `match` retourne `null`.

Si vous cherchiez des chiffres dans une chaîne, vous voudriez que votre code se comporte différemment selon que la chaîne contient des chiffres ou non, n'est-ce pas ? Donc vous utiliseriez une instruction `if` :

```
var found: string[]|null = s.match(/[0-9]+/);if (found) {  console.log("The string has a number in it: " + found[0]);} else {  console.log("The string lacks digits.");}
```

Comme vous le savez probablement, `if (found)` signifie "si found est truthy". Cela signifie essentiellement `if (found != null && found != 0 && found != false)`.

Si vous ne vérifiez pas si `found !== null`, TypeScript vous donnera une erreur :

```
var found = s.match(/[0-9]+/);console.log("The string has a number in it: " + found[0]);           // Error: Object is possibly 'null'  ^^^^^
```

Alors pourquoi **ne** recevez-vous pas d'erreur lorsque vous utilisez l'instruction `if` ? C'est la magie du typage basé sur le flux de TypeScript.

Dans la première branche de l'instruction `if`, TypeScript sait que `found` **ne peut pas** être null, et donc le type de `found` **change dans ce bloc** pour exclure `null`. Ainsi, son type devient `string[]`. De même, à l'intérieur du bloc `else {...}`, TypeScript sait que `found` **ne peut pas** être `string[]`, donc `string[]` est exclu et le type de `found` devient `null` dans cette région.

Mais TypeScript a un opérateur `!` qui est utilisé pour éviter certains messages d'erreur. Il signifie "écoute, compilateur, je sais que tu penses que cette variable pourrait être `null` ou `undefined`, mais je te promets qu'elle ne l'est pas. Donc si `found` a le type `string[]|null`, alors `found!` a le type `string[]`."

Si vous êtes sûr que `s` contient des chiffres, vous pouvez utiliser `!` pour éviter le message d'erreur :

```
var found = s.match(/[0-9]+/);console.log("The string has a number in it: " + found![0]);
```

Le système de typage basé sur le flux de TypeScript prend en charge les opérateurs `typeof` et `instanceof`, ainsi que les opérateurs de comparaison ordinaires. Si vous commencez avec une variable qui pourrait avoir plusieurs types, vous pouvez utiliser l'un de ces opérateurs pour affiner le type :

**Note :** JavaScript distingue les types **primitifs** et **boxed primitive**, qui sont des objets. Par exemple, `"yarn"` est un primitif, et son type est `string`. Cependant, il existe également un type de chaîne **boxed** appelé `String` avec un S majuscule, qui est rarement utilisé. Vous pouvez créer un `String` en écrivant `new String("yarn")`. La chose à garder à l'esprit est que ce sont des types totalement différents.

`"yarn" instanceof String` est `false` : `"yarn"` est un `string`, pas un `String` !

`"yarn" instanceof string` n'est **pas** faux. Au lieu de cela, c'est une expression totalement illégale — le côté droit de `instanceof` doit être une **fonction constructeur** et `string` n'a pas de constructeur.

JavaScript fournit deux opérateurs différents pour tester les types de primitifs et d'objets (non-primitifs) :

* `[instanceof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof)` vérifie la [chaîne de prototypes](https://medium.freecodecamp.org/prototype-in-js-busted-5547ec68872) pour découvrir si une valeur est un certain type d'objet.
* `[typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)` vérifie si quelque chose est un primitif et, si oui, de quel type.

Comme vous pouvez le voir dans le code ci-dessus, `instanceof` est un opérateur binaire qui retourne un booléen, tandis que `typeof` est un opérateur unaire qui retourne une chaîne. Par exemple, `typeof "yarn"` retourne `"string"` et `typeof 12345` retourne `"number"`. Les types primitifs sont `number`, `boolean`, `string`, `symbol`, `undefined`, et `null`. Tout ce qui n'est pas un primitif est un `Object`, y compris les fonctions.

Mais `typeof` traite les fonctions de manière spéciale. Par exemple, `typeof Math.sqrt === "function"`, et `Math.sqrt instanceof Object === true`. Les Symbols sont nouveaux dans ES6 et, bien que `null` soit un primitif, `typeof null === "object"` [est une erreur](http://2ality.com/2013/10/typeof-null.html).

Comme vous pouvez le voir dans l'exemple ci-dessus, TypeScript comprend également `Array.isArray` comme un moyen de détecter un tableau. Cependant, certaines autres méthodes de détection de types en JavaScript ne sont pas prises en charge :

* `if (thing.unshift)` est parfois utilisé pour distinguer les chaînes des autres choses, car presque rien sauf les chaînes n'ont une méthode `unshift`. Cela n'est pas pris en charge dans TypeScript car il ne vous permet pas de lire une propriété qui peut ne pas exister.
* `if (thing.hasOwnProperty("unshift"))` n'est pas reconnu comme un test de type.
* `if (thing.constructor === String)` n'est pas reconnu comme un test de type. En JavaScript, la lecture d'une propriété telle que `constructor` promeut `thing` au statut Boxed, donc même si `thing` est une _chaîne primitive_, son `.constructor` sera _non-primitive_.
* `if ("unshift" in thing)` ne fonctionne pas. "Le côté droit d'une expression 'in' doit être de type 'any', un type d'objet ou un paramètre de type." (`in` doit être évité de toute façon car il est lent.)

### Alias de types

L'instruction `type` crée un nouveau nom pour un type. Par exemple, après avoir écrit :

```
type num = number;
```

Vous pouvez utiliser `num` comme synonyme de `number`. `type` est similaire à `interface` puisque vous pouvez écrire quelque chose comme ceci...

```
type Point = {    x: number;    y: number;}
```

...au lieu de `interface Point {...}`. Cependant, seules les interfaces supportent **l'héritage**. Par exemple, je peux créer une nouvelle interface qui est **comme** `Point` mais qui a également un nouveau membre `z`, comme ceci :

```
interface Point3D extends Point {    z: number;}
```

Vous ne pouvez pas faire d'héritage avec `type`. Cependant, si `Point` était défini avec `type`, vous êtes toujours autorisé à l'étendre avec une `interface`.

### Types de fonctions

En JavaScript, vous pouvez passer des fonctions à d'autres fonctions, comme ceci :

```
function doubler(x) { return x*2; }function squarer(x) { return x*x; }function experimenter(func){  console.log(`When I send 5 to my function, I get ${func(5)}.`);}experimenter(doubler);experimenter(squarer);
```

Sortie :

```
When I send 5 to my function, I get 10.When I send 5 to my function, I get 25.
```

En TypeScript, vous devez normalement écrire les types des arguments de fonction — vous devez savoir comment exprimer le type de `func`. Comme vous pouvez le voir ici, son type devrait être quelque chose comme `(param: number) => num`ber :

```
function doubler(x: number) { return x*2; }function squarer(x: number) { return x*x; }function experimenter(func: (param: number) =&gt; number){  console.log(`When I send 5 to my function, I get ${func(5)}.`);}experimenter(doubler);experimenter(squarer);
```

TypeScript vous oblige à donner un **nom** au paramètre de `func`, mais il n'a pas d'importance quel est ce nom. J'aurais pu l'appeler `x`, ou `Wednesday`, ou `myFavoriteSwearWord` et cela n'aurait fait aucune différence. Mais ne pensez même pas à l'appeler `asshat`. Le compilateur ne s'en souciera pas, mais qu'en est-il de votre patron ? Mieux vaut prévenir que guérir, c'est tout ce que je peux dire.

En JavaScript, tout ce qui est à l'intérieur d'un objet est une propriété — une sorte de variable — et cela inclut les fonctions. Par conséquent, ces deux interfaces signifient la même chose :

```
interface Thing1 {  func: (param: number) =&gt; number;}interface Thing2 {  func(param: number): number;}
```

Et donc ce code est autorisé :

```
class Thing {  func(x: number) { return x * x * x; }}let t1: Thing1 = new Thing();let t2: Thing2 = t1; 
```

Cela vous semble-t-il étrange que TypeScript exige `:` avant le type de retour d'une fonction "normale" mais qu'il exige `=&`gt; avant le type de retour d'une variable de fonction ? En tout cas, c'est comme ça.

### Génériques, dates et autres

#### Dates

Supposons que j'écrive une fonction qui garantit qu'une valeur est un tableau, comme ceci :

```
function asArray(v: any): any[] {  // return v if it is an array, otherwise return [v]  return (Array.isArray(v) ? v : [v]);}
```

La fonction `asArray` fonctionne, mais elle perd des informations de type. Par exemple, que se passe-t-il si cette fonction l'appelle ?

```
/** Prints one or more dates to the console */function printDates(dates: Date|Date[]) {  for (let date of asArray(dates)) {      // SUPER BUGGY!      var year = date.getYear();      var month = date.getMonth() + 1;      var day = date.getDay();      console.log(`${year}/${month}/${day}`);  }}
```

Le compilateur TypeScript accepte ce code, mais il contient deux bugs. Le code a correctement ajouté `1` au mois, car `getMonth()` retourne 0 pour janvier et 11 pour décembre. Mais le code pour obtenir l'`year` et le `day` sont tous deux incorrects. Puisque `asArray` retourne `any[]`, la vérification de type et IntelliSense — qui auraient pu attraper ces bugs — sont désactivés sur `date`. Ces bugs auraient pu être évités si `asArray` était générique :

```
function asArray<T>(v: T | T[]): T[] {  return Array.isArray(v) ? v : [v];}
```

Cette version de `asArray` fait la même chose, mais elle a un **paramètre de type**, que j'ai décidé d'appeler `T`, pour permettre une vérification de type améliorée. Le paramètre de type peut être n'importe quel type, donc il est similaire à `any`. Mais il permet à la fonction de décrire la **relation** entre le paramètre `v` et la valeur de retour.

Plus précisément, il dit que `v` et la valeur de retour ont, eh bien, des types similaires. Lorsque vous appelez `asArray`, le compilateur TypeScript trouve une valeur de `T` qui permet à l'appel d'avoir du sens. Par exemple, si vous appelez `asArray(42)`, le compilateur choisit `T=number` car il est possible d'utiliser 42 comme argument pour `asArray(v: number|number[]): number[]`. Après avoir choisi `T=number`, TypeScript réalise que `asArray` retourne un tableau de nombres.

Dans `printDates`, nous avons appelé `asArray(dates)` et le compilateur comprend que `T=Date` fonctionne le mieux dans cette situation. Après avoir choisi `T=Date`, TypeScript réalise que `asArray` retourne un tableau de `Date`. Par conséquent, la variable `date` a le type `Date`, et il trouve alors le premier bug : `date.getYear` n'existe pas ! Eh bien, en fait, il existe, mais il a été déprécié en raison de son comportement — il retourne le nombre d'années depuis 1900 — 118 en 2018. Au lieu de cela, vous devriez appeler `getFullYear`.

TypeScript lui-même ne remarque pas le deuxième bug. Mais, lorsque vous tapez `date.getDay`, VS Code vous informera dans une petite boîte contextuelle que cette fonction "Gets the day of the week, using local time". Le jour de la semaine ? Vous devez **plaisanter** !

Grâce aux génériques et à VS Code, nous corrigeons notre code pour appeler `date.getDate` à la place. Cela ne retourne **pas** la date sans une heure qui y est attachée, mais plutôt le **jour du mois en cours**. Contrairement au mois, le jour ne commence **pas** à compter à partir de zéro.

```
/** Prints one or more dates to the console */function printDates(dates: Date|Date[]) {  for (let date of asArray(dates)) {      var year = date.getFullYear();      var month = date.getMonth() + 1;      var day = date.getDate();      console.log(`${year}/${month}/${day}`);  }}
```

Une bonne chose à propos de `Date` est qu'ils sont normalement stockés en UTC — fuseau horaire universel, ou GMT. Cela signifie que si l'utilisateur change le fuseau horaire sur son ordinateur, les objets `Date` dans votre programme continuent de représenter le même **point dans le temps**, mais la chaîne retournée par `.toString()` change. Habituellement, c'est ce que vous voulez, surtout en JavaScript où vous pouvez avoir du code client et serveur s'exécutant dans différents fuseaux horaires.

#### Génériques

Un exemple avancé de génériques apparaît dans mon [module simplertime](https://www.npmjs.com/package/simplertime). Dans ce cas, j'avais une fonction `timeToString` qui acceptait une liste d'options de formatage comme ceci :

```
export interface TimeFormatOptions {  /** If true, a 24-hour clock is used and AM/PM is hidden */  use24hourTime?: boolean;  /** Whether to include seconds in the output (null causes seconds   *  to be shown only if seconds or milliseconds are nonzero) */  showSeconds?: boolean|null;  ...}
```

```
export function timeToString(time: Date|number,                              opt?: TimeFormatOptions): string {  ...}
```

Le mot-clé `export` est utilisé pour partager du code avec d'autres fichiers sources. Par exemple, vous pouvez importer `timeToString` dans votre propre code en utilisant `import {timeToString} from 'simplertime'` (après l'installation avec `npm i simplertime` bien sûr). Si vous souhaitez importer des choses depuis un fichier différent dans le **même dossier**, ajoutez un préfixe `./` au nom du fichier, par exemple `import * as stuff from './mystuff'`.

Les génériques peuvent également être utilisés sur les classes et les interfaces. Par exemple, JavaScript a un type `Set` pour contenir une collection non ordonnée de valeurs. Nous pourrions l'utiliser comme ceci :

```
var primes = new Set([2, 3, 5, 7]);for (var i = 0; i < 10; i++)  console.log(`Is the number ${i} prime? ${primes.has(i)}`);
```

En TypeScript, cependant, `Set` a un paramètre de type, `Set<`;T>, signifiant que tous les éléments dans le set ont le type T. Dans ce code, TypeScript infère `que T=`number, donc si vous `écrivez primes.add("he`llo!") vous obtiendrez une erreur de type. Si vous voulez **réellement** créer un set qui peut contenir à la fois des chaînes et des nombres, vous pouvez le faire comme ceci :

```
var primes = new Set&lt;string|number>([2, 3, 5, 7]); 
```

Vous pouvez également créer vos propres types génériques. Par exemple, j'ai créé une structure de données [B+ Tree](https://en.wikipedia.org/wiki/B%2B_tree) appelée `[BTree<K,](https://github.com/qwertie/btree-typescript)` V>, qui est une collection de paires clé-valeur, triées par clé, qui prend en charge le clonage rapide. Elle a deux paramètres de type, K (une clé) et V (une valeur) et sa définition ressemble à peu près à **ci-dessous**. Note : les corps de fonction ont été omis car je veux juste vous montrer à quoi ressemble une classe générique :

### Littéraux comme types

Vous vous souvenez de l'erreur lorsque vous écrivez ceci ?

```
let z = 26;z = "Zed";
```

Le message d'erreur semble un peu étrange :

```
Type '"Zed"' is not assignable to type 'number'
```

Pourquoi dit-il que `"Zed"` est un "type", au lieu d'une "valeur" ou d'une "chaîne" ? Pour comprendre cela, il est nécessaire de comprendre que TypeScript a la capacité de traiter les valeurs comme des types. `"Zed"` est une `string`, bien sûr, mais c'est plus que cela — il a **un autre type en même temps**, un type plus spécifique appelé `"Zed"` qui représente la _valeur_ `"Zed"`. Nous pouvons même créer une variable avec ce type :

```
let zed: "Zed" = "Zed";
```

Maintenant, nous avons créé une variable complètement inutile appelée `zed`. Nous pouvons définir cette variable sur `"Zed"`, mais rien d'autre :

```
zed = "Zed"; // OKzed = "ZED"; // Error: Type '"ZED"' is not assignable to type '"Zed"'.
```

Par défaut, nous pouvons définir `zed` sur `null` et `undefined`. Heureusement, avec l'option `"strictNullChecks": true`, nous pouvons fermer cette faille afin que cette variable ne soit jamais autre chose que "Zed". Merci Dieu pour cela, c'est tout ce que je peux dire.

Alors, à quoi servent ces types littéraux ? Eh bien, parfois une fonction n'autorise que certaines chaînes particulières. Par exemple, imaginez si vous avez une fonction qui vous permet de `turn("left")` ou `turn("right")` mais rien d'autre. Cette fonction pourrait être déclarée avec un type littéral :

```
function turn(direction: "left"|"right") {  }
```

### Tableaux de longueur fixe

Voici une autre énigme pour vous : quelle est la différence entre les types `number[]` et `[number]` ? Le premier est un tableau de nombres, le second est un tableau qui contient un seul élément, qui est un nombre.

De même, `[string,number]` désigne un tableau de longueur 2 avec le premier élément étant une chaîne et le second étant un nombre. De plus, le tableau a une propriété `length: 2`, c'est-à-dire que son **type** est `2`, et non pas simplement `number`. Ces tableaux de longueur fixe sont appelés types de tuples.

### Génériques avancés

Alors, vous vous souvenez du module `simplertime` dont je parlais ? Il exporte également un objet `defaultTimeFormat` qui contient les valeurs par défaut pour les options de formatage de `timeToString`. Je voulais définir une fonction spéciale qui me permettrait d'écrire des choses comme `get(options, 'use24hourTime')` pour récupérer la valeur de `options.use24hourTime` si elle existe et `defaultTimeFormat.use24hourTime` si elle n'existe pas.

Dans de nombreux langages, il est impossible d'écrire une fonction comme celle-ci, mais c'est possible dans les langages "dynamiques" comme JavaScript. Voici à quoi ressemblerait la fonction `get` en JavaScript :

```
function get(opt, name) {  if (opt === undefined || opt[name] === undefined)    return defaultTimeFormat[name]  return opt[name];}
```

En JavaScript et TypeScript, `thing.property` peut être écrit comme `thing["property"]` et, si la propriété n'existe pas, le résultat est `undefined`. Mais dans la version avec crochets, nous pouvons utiliser une **variable**, de sorte que la question "quelle propriété utilisons-nous ?" peut être répondue par du code situé ailleurs.

Traduire cela en TypeScript est possible avec une fonctionnalité appelée `keyof`, mais c'est **très** délicat. Voici la traduction :

```
function get<;K extends keyof TimeFormatOptions>(         opt: TimeFormatOptions|undefined, name: K):          TimeFormatOptions[K]{  if (opt === undefined || opt[name] === undefined)    return defaultTimeFormat[name]  return opt[name];}
```

Ici, la variable de type `K` a une **contrainte** attachée à elle, `K extends keyof TimeFormatOptions`. Voici comment cela fonctionne :

1. `keyof X` transforme les propriétés de `X` en un type d'union des noms des propriétés. Par exemple, étant donné l'interface `Book` précédente, `keyof Book` signifie `"title" | "author" | "age"`. De même, `keyof TimeFormatOptions` est l'un des noms de propriété dans `TimeFormatOptions`.
2. La contrainte "extends", `X extends Y`, signifie que "X doit être Y, ou un sous-type de Y". Par exemple, `X extends Object` signifie que `X` doit être un type d'`Object`, ce qui signifie qu'il peut être un tableau ou une `Date` ou même une fonction, tous considérés comme des Objects, mais il ne peut pas être une `string` ou un `number` ou un `boolean`. De même, `X extends Point` signifie que `X` est `Point` ou un type _plus spécifique_ que `Point`, comme `Point3D`.
3. Que signifierait `B extends keyof Book` ? Cela signifierait que `B` est un **sous-type** de `"title" | "author" | "age"`. Et, rappelez-vous, nous parlons de **types** ici, **pas** de valeurs. Le littéral de chaîne `"title"` a la valeur `"title"` mais il a aussi le type `"title"`, qui est un concept différent. Le type est géré par le système de types TypeScript, et la valeur est gérée par JavaScript. Le type `"title"` n'existe plus lorsque le programme est en cours d'exécution, mais la valeur `"title"` existe toujours. Maintenant, `B` peut être assigné à des types comme `"title"` ou `"title" | "age"`, car chaque valeur de type `"title" | "age"` (ou `"title"`) peut être assignée à une variable de type `keyof Book`. Cependant, `B` ne peut pas être `string`, car certaines chaînes ne sont pas "title", "author", ou "age".
4. De même, `K` est contraint d'avoir un sous-type de `keyof TimeFormatOptions`, comme `"use24hourTime"`.
5. Le type `X[Y]` signifie "le type de la propriété Y de X, où Y est un littéral numérique ou de chaîne". Par exemple, le _type_ `Book["author"]` est `string | undefined`.

En mettant tout cela ensemble, lorsque j'écris `get(options, 'use24hourTime')`, le compilateur décide que `K='use24hourTime'`. Par conséquent, le paramètre `name` a le type `"use24hourTime"` et le type de retour est `TimeFormatOptions["use24hourTime"]`, ce qui signifie `boolean | undefined`.

### Failles dans le système de types

Puisque TypeScript est construit sur JavaScript, il accepte certaines failles dans son système de types pour diverses raisons. Plus tôt, nous avons vu l'une de ces failles, le fait que ce code est légal :

```
class Box {  constructor(public width: number, public height: number) {}  get area() { return this.width*this.height; }}
```

```
interface IArea {  area: number; // area is not readonly}
```

```
let ia: IArea = new Box(10,100);ia.area = 5; // Accepted by TypeScript, but causes a runtime error
```

Voici quelques autres failles intéressantes :

#### Vous pouvez assigner une classe dérivée à une classe de base

Un `Date` est un type d'`Object`, donc naturellement vous pouvez écrire :

```
var d: Object = new Date();
```

Il est donc logique que nous puissions également assigner cette interface `D` à cette interface `O`, n'est-ce pas ?

```
interface D { date: Date }interface O { date: Object }var de: D = { date: new Date() };    // okay...var oh: O = de;                      // makes sense...oh.date = { date: {wait:"what?"} }   // wait, what?
```

Eh bien, non, pas vraiment, car TypeScript croit maintenant que `de.date` est un `Date` alors qu'il s'agit en réalité d'un `Object`.

#### Vous pouvez assigner [A,B] à (A|B)[]

Il est logique qu'un tableau de deux éléments, un `A` suivi d'un `B`, soit également un tableau de `A|B`, n'est-ce pas ? En fait, non, pas vraiment :

```
var array1: [number,string] = [5,"five"];var array2: (number|string)[] = array1;   // makes sense...array2[0] = "string!";                    // wait, what?
```

TypeScript croit maintenant que `array1[0]` est un `number` alors qu'il s'agit en réalité d'une `string`. C'est un exemple d'un problème plus général, que les tableaux sont traités comme covariants mais qu'ils **ne sont pas** vraiment covariants car ils sont modifiables.

#### Tableaux ? Il y a des dragons.

En mode `strict` recommandé, vous ne pouvez pas mettre `null` ou `undefined` dans des tableaux de nombres...

```
var a = [1,2,3];a[3] = undefined; // 'undefined' is not assignable to type 'number'
```

Donc cela signifie que lorsque nous obtenons une valeur d'un tableau de nombres, c'est un nombre, n'est-ce pas ? En fait, non, pas vraiment :

```
var array = [1,2,3];var n = array[4];
```

TypeScript croit maintenant que `n` est un `number` alors qu'il s'agit en réalité de `undefined`.

Une faille plus évidente est que vous pouvez allouer un tableau dimensionné de nombres... sans aucun nombre dedans :

```
var array = new Array<number>(2); // array of two "numbers"var n:number = array[0];
```

#### Les paramètres de fonction sont bivariants lors de la substitution

Contrairement à d'autres langages avec typage statique, TypeScript permet la substitution avec des paramètres covariants. **Paramètre covariant** signifie que, lorsque la classe devient plus spécifique (A à B), le paramètre devient également plus spécifique (Object à Date) :

```
class A {    method(value: Object) { }}
```

```
class B extends A {    method(value: Date) { console.log(value.getFullYear()); }}
```

```
var a:A = new B();a.method({}); // Calls B.method, which has a runtime error
```

Cela n'est pas sûr, mais étrangement, c'est autorisé. En revanche, il est (relativement) sûr de substituer avec des **paramètres contravariants**, comme ceci :

```
class A {    method(value: Date) { }}class B extends A {    method(value: Object) { console.log(value instanceof Date); }}
```

Les types de retour covariants sont également sûrs :

```
class A {    method(): Object { return {} }}class B extends A {    method(): Date { return new Date(); }}
```

TypeScript rejette à juste titre les types de retour contravariants :

```
class A {    method(): Date { return new Date(); }}class B extends A {    // Property 'method' in type 'B' is not assignable to     // the same property in base type 'A'.    //   Type '() => Object' is not assignable to type '() => Date'    //     Type 'Object' is not assignable to type 'Date'    method(): Object { return {} }}
```

#### Les classes se prennent pour des interfaces (mais elles ne le sont pas)

TypeScript vous permet de traiter une classe comme si c'était une interface. Par exemple, ceci est légal :

```
class Class {  content: string = "";}
```

```
var stuff: Class = {content:"stuff"};
```

Stuff n'est pas une vraie `Class`, mais TypeScript pense que c'en est une, ce qui peut causer une erreur de type `TypeError` à l'exécution si vous utilisez `instanceof Class` ailleurs dans le programme :

```
function typeTest(x: Class|Date) {  if (x instanceof Class)    console.log("The class's content is " + x.content);  else    console.log("It's a Date in the year " + x.getFullYear());}
```

```
typeTest(stuff);
```

#### `_this_` n'est pas nécessairement ce que vous pensez

`this` est une faille de JavaScript, pas de TypeScript. Chaque fois qu'une fonction utilise `this`, elle pourrait accéder à un objet complètement inattendu, avec un type différent de ce que vous pensez :

```
class Time {  constructor(public hours: number, public minutes: number) { }  toDate(day: Date) {    var clone = new Date(day);    clone.setHours(this.hours, this.minutes);    return clone;  }}
```

```
// Call toDate() with this=12345Time.prototype.toDate.call(12345, new Date());
```

Le seul péché de TypeScript est qu'il n'essayera pas de vous empêcher de faire cela.

En parlant de `this`, une chose que les développeurs JavaScript devraient savoir est que les **fonctions fléchées** comme `x =>` x+1 fonctionnent légèrement différemment des fonctions anonymes comme `function(x) {return x`+1}.

Les fonctions **fléchées** héritent de la valeur de `this` de la fonction externe dans laquelle elles se trouvent. Les fonctions **normales** reçoivent une nouvelle valeur de `this` de l'appelant. Donc, si `f` est une fonction fléchée, `f.call(12345, x)` ne change pas `this`, donc c'est comme appeler `f(x)`. C'est généralement une bonne chose, mais si vous écrivez :

`var obj = { x: 5, f: () => this.`x }

Vous devriez réaliser que `obj.f()` ne retourne **pas** `obj.x`.

#### Leçons

Pour éviter ces failles, vous devez :

* **Ne pas** traiter un **objet** comme un type "baser" (par exemple, ne traitez pas `D` comme un `O`) sauf si vous êtes sûr que le type baser ne sera pas modifié d'une manière qui pourrait violer le système de types.
* **Ne pas** traiter un **tableau** comme un type "baser" (par exemple, ne traitez pas `D[]` comme `O[]`, ou `[A,B]` comme `(A|B)[]`) sauf si vous êtes sûr que le type baser ne sera pas modifié d'une manière qui pourrait violer le système de types.
* Faites attention à ne pas laisser de "trous" avec des valeurs indéfinies dans vos tableaux.
* Faites attention à ne pas utiliser d'index de tableau hors limites.
* **Ne pas** substituer une méthode de classe de base avec des paramètres covariants.
* **Évitez** de traiter une classe `K` comme si c'était une interface, sauf si vous êtes sûr qu'aucun code ne vérifiera jamais le type avec `instanceof`.
* **Évitez** d'utiliser `.call(...)` et soyez prudent avec la manière dont vous gérez les références aux fonctions.

TypeScript avait en fait [plus](https://github.com/Microsoft/TypeScript/issues/9765) [de failles](https://github.com/Microsoft/TypeScript/issues/3410#issuecomment-111646030) dans le passé, qui sont maintenant comblées.

### JSX

React a introduit le concept de code JSX. Ou peut-être que [Hyperscript](https://github.com/hyperhype/hyperscript) l'a introduit et React a copié l'idée peu après. Dans tous les cas, JSX **ressemble** à du code HTML/XML. Mais vous ne créez pas d'éléments DOM, vous créez de vieux objets JavaScript ordinaires, que nous appelons un "DOM virtuel". Par exemple, `<img src={imageUrl`}/> signifie en réalité React.createElement("img", { src: image`Url }) dans un fichier .jsx ou .tsx.

Si JSX est une chose React, pourquoi en parle-je dans la section TypeScript ? Parce que le support pour JSX est intégré dans le compilateur TypeScript. Pour obtenir le support JSX dans n'importe quel fichier TypeScript, vous devez simplement changer l'extension du fichier de `.ts` à `.tsx`.

JSX peut être utilisé aux mêmes endroits que les expressions normales : vous pouvez passer du code JSX à une fonction...

```
ReactDOM.render(<h1>I'm JSX code!</h1>, document.body);
```

vous pouvez le stocker dans une variable...

```
let variable = <h1>I'm JSX code!</h1>;
```

et vous pouvez le retourner d'une fonction...

```
return <h1>I'm JSX code!</h1>;
```

Parce que `<h1>I'm JSX code`!</h1> signifie en réalité React.createElement("h1", null, "I'm` JSX code!").

Il est important de savoir si une balise JSX commence par une lettre majuscule — elle est traduite en TypeScript (ou JavaScript) **différemment** si c'est le cas. Par exemple :

* `<div class="foo`"/> `signifie React.createElement('div', {"class":"`foo"}), mais
* `<Div class="foo`"/> `signifie React.createElement(Div, {"class":"`foo"}) (sans guillemets autour de Div).

Conseils pour utiliser JSX :

* JSX est similaire à XML, donc toutes les balises doivent être fermées : écrivez `<b`r/>`, pas <br>.
* JSX ne prend en charge que les attributs de chaîne et les expressions JavaScript. Lorsque vous écrivez des attributs numériques en TypeScript, utilisez `<input type="number" min={0} max={100`}/>, car m`ax=100 est une erreur de syntaxe et max`="100" est une erreur de type.
* Dans React/Preact, vous pouvez utiliser un tableau d'éléments à tout endroit où une liste d'enfants est attendue. Par exemple, au lieu de `return <p>Ann<br/>Bob`<br/>Cam&l`t;/p>, vous pouvez écrire let x = [<br/>, 'Bob', &`lt;br/>]; return <p>Ann{x}Cam</p>. Cela a le même effet car React/Preact "aplatit" les tableaux dans la liste des enfants.
* Dans React, l'attribut `class` n'est pas pris en charge pour une raison quelconque. Utilisez `className` à la place.
* JSX lui-même ne prend pas en charge les propriétés ou enfants optionnels. Par exemple, supposons que vous écriviez `<Foo prop={`x}> mais vous voulez omettre la prop lorsque `x est indéfini. Eh bien, JSX lui-même ne prend pas en charge quelque chose comme cela. Cependant, la plupart des composants traitent une propriété indéfinie de la même manière qu'une propriété manquante, donc cela fonctionne généralement de toute façon. JSX ne prend pas en charge les enfants optionnels non plus, mais vous pouvez obtenir le même effet avec un tableau vide : car les tableaux sont "effondrés" par React/Pr`eact, <Foo>`{ [] }</Foo> a le même effet que <Foo></F`oo>. <Foo>{undefined}</Foo> n'a pas cet effet `(vous vous retrouvez avec un seul enfant égal à undefined.)
* Si vous avez un objet comme `obj = {a:1, b:2}` et que vous souhaitez utiliser toutes les propriétés de l'objet comme propriétés d'un Composant, vous pouvez écrire `<Component {...obj`}/>. Les points sont toujours requis ; <Componen`t {obj}/> n'est pas autorisé.

En haut du fichier, le pragma `@jsx` peut contrôler la fonction "factory" qui est appelée pour traduire les éléments JSX. Par exemple, si vous utilisez `/** @jsx h */` alors `<b>th`is</b> se traduit par h('b', n`ull, "this") `au lieu de React.createElement('b', n`ull, "this"). Certaines applications Preact utilisent ce pragma (h est la fonction preact pour créer des éléments), mais vous n'aurez pas besoin de l'utiliser dans ce tutoriel (c`reateElement est un `s`ynonyme de h). De plus, dans "tsconfig.json", vous pouvez obtenir le même `effet avec "jsxF`actory": `"h" dans les com`pilerOptions.

### Voir aussi

[TypeScript evolution](https://blog.mariusschulz.com/series/typescript-evolution) explique les dernières fonctionnalités de TypeScript en détail. Vous pourriez également aimer voir [Advanced Types](https://www.typescriptlang.org/docs/handbook/advanced-types.html) dans le manuel de TypeScript.

### Avant de partir...

Si vous avez aimé cet article, n'oubliez pas d'applaudir ou de tweeter ! Et si vous souhaitez apprendre React, continuez avec mon [prochain article](http://typescript-react-primer.loyc.net/tutorial-5.html).