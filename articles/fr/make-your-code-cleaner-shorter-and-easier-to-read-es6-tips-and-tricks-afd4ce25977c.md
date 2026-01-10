---
title: Astuces et conseils ES6 pour rendre votre code plus propre, plus court et plus
  facile à lire !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-22T15:37:51.000Z'
originalURL: https://freecodecamp.org/news/make-your-code-cleaner-shorter-and-easier-to-read-es6-tips-and-tricks-afd4ce25977c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2VqxkdyNCmWa8ojZZIoQOg.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Astuces et conseils ES6 pour rendre votre code plus propre, plus court
  et plus facile à lire !
seo_desc: 'By Sam Williams

  Template literals

  Template literals make working with strings so much easier than before. They''re
  started with a back tick, and can have variables inserted using ${variable}. Compare
  these two lines of code:

  var fName = ''Peter'', sName...'
---

Par Sam Williams

### Littéraux de gabarit

Les littéraux de gabarit rendent le travail avec les chaînes de caractères beaucoup plus facile qu'avant. Ils commencent par une backtick, et peuvent contenir des variables insérées en utilisant `${variable}`. Comparez ces deux lignes de code :

```
var fName = 'Peter', sName = 'Smith', age = 43, job= 'photographer';var a = 'Hi, I\'m ' + fName + ' ' + sName + ', I\'m ' + age + ' and work as a ' + job + '.';var b = `Hi, I'm ${ fName } ${ sName }, I'm ${ age } and work as a ${ job }.`;
```

Cela simplifie grandement la vie et rend le code plus facile à lire. Vous pouvez mettre n'importe quoi à l'intérieur des accolades : variables, équations ou appels de fonction. Je vais utiliser ces exemples tout au long de cet article.

### Portée de bloc de syntaxe

JavaScript a toujours été limité par les fonctions, c'est pourquoi il était devenu courant d'envelopper l'ensemble d'un fichier JavaScript dans une expression de fonction invoquée immédiatement vide (IIFE). Cela est fait pour isoler toutes les variables du fichier, afin qu'il n'y ait pas de conflits de variables.

Maintenant, nous avons la portée de bloc et deux nouvelles déclarations de variables qui sont liées à un bloc.

### Déclaration 'Let'

Cela est similaire à `var` mais présente quelques différences notables. Parce qu'il est limité à un bloc, une nouvelle variable avec le même nom peut être déclarée sans affecter les variables externes.

```
var a = 'car' ;{    let a = 5;    console.log(a) // 5}console.log(a) // car
```

Parce qu'il est lié à une portée de bloc, il résout cette question classique d'entretien : 
"quel est le résultat, et comment le faire fonctionner comme prévu ?"

```
for (var i = 1; i < 5; i++){    setTimeout(() => { console.log(i); }, 1000);}
```

Dans ce cas, il affiche "5 5 5 5 5" parce que la variable `i` change à chaque itération.

Si vous remplacez `var` par `let`, tout change. Maintenant, chaque boucle crée une nouvelle portée de bloc avec la valeur de i liée à cette boucle. C'est comme si vous aviez écrit :

```
{let i = 1; setTimeout(() => { console.log(i) }, 1000)} {let i = 2; setTimeout(() => { console.log(i) }, 1000)} {let i = 3; setTimeout(() => { console.log(i) }, 1000)} {let i = 4; setTimeout(() => { console.log(i) }, 1000)} {let i = 5; setTimeout(() => { console.log(i) }, 1000)} 
```

Une autre différence entre `var` et `let` est que `let` n'est pas hissé comme `var`.

```
{     console.log(a); // undefined    console.log(b); // ReferenceError    var a = 'car';    let b = 5;}
```

En raison de sa portée plus stricte et de son comportement plus prévisible, certaines personnes ont dit que vous devriez utiliser `let` au lieu de `var`, sauf lorsque vous avez spécifiquement besoin du hissing ou de la portée plus lâche de la déclaration `var`.

### Const

Si vous vouliez déclarer une variable constante en JavaScript auparavant, il était courant de nommer la variable en majuscules. Cependant, cela ne sécurisait pas la variable — cela indiquait simplement aux autres développeurs qu'il s'agissait d'une constante et qu'elle ne devait pas être modifiée.

Maintenant, nous avons la déclaration `const`.

```
{    const c = "tree";    console.log(c);  // tree    c = 46;  // TypeError! }
```

`const` ne rend pas la variable immuable, il verrouille simplement son assignation. Si vous avez une assignation complexe (objet ou tableau), la valeur peut encore être modifiée.

```
{    const d = [1, 2, 3, 4];    const dave = { name: 'David Jones', age: 32};    d.push(5);     dave.job = "salesman";    console.log(d);  // [1, 2, 3, 4, 5]    console.log(dave);  // { age: 32, job: "salesman", name: 'David Jones'}}
```

### Problème avec les fonctions de portée de bloc

Les déclarations de fonctions sont maintenant spécifiées pour être liées à la portée de bloc.

```
{    bar(); // fonctionne    function bar() { /* faire quelque chose */ }}bar();  // ne fonctionne pas
```

Le problème survient lorsque vous déclarez une fonction à l'intérieur d'une instruction `if`.

Considérez ceci :

```
if ( something) {    function baz() { console.log('I passed') }} else {    function baz() { console.log('I didn\'t pass') } } baz();
```

Avant ES6, les deux déclarations de fonction auraient été hissées et le résultat aurait été `'I didn\'t pass'` peu importe ce que `something` était.   
Maintenant, nous obtenons `'ReferenceError'`, car `baz` est toujours lié par la portée de bloc.

### Spread

ES6 introduit l'opérateur `...`, qui est appelé l'opérateur de spread. Il a deux utilisations principales : étendre un tableau ou un objet dans un nouveau tableau ou objet, et joindre plusieurs paramètres dans un tableau.

Le premier cas d'utilisation est celui que vous rencontrerez probablement le plus, alors nous allons le voir en premier.

```
let a = [3, 4, 5];let b = [1, 2, ...a, 6];console.log(b);  // [1, 2, 3, 4, 5, 6]
```

Cela peut être très utile pour passer un ensemble de variables à une fonction à partir d'un tableau.

```
function foo(a, b, c) { console.log(`a=${a}, b=${b}, c=${c}`)} let data = [5, 15, 2];foo( ...data); // a=5, b=15, c=2
```

Un objet peut également être étendu, en insérant chaque paire clé-valeur dans le nouvel objet. (L'étalement d'objet est en fait à l'étape 4 de la proposition et sera officiellement dans ES2018. Il n'est pris en charge que par Chrome 60 ou ultérieur, Firefox 55 ou ultérieur, et Node 6.4.0 ou ultérieur)

```
let car = { type: 'vehicle ', wheels: 4};let fordGt = { make: 'Ford', ...car, model: 'GT'};console.log(fordGt); // {make: 'Ford', model: 'GT', type: 'vehicle', wheels: 4}
```

Une autre caractéristique de l'opérateur de spread est qu'il crée un nouveau tableau ou objet. L'exemple ci-dessous crée un nouveau tableau pour `b`, mais `c` fait simplement référence au même tableau.

```
let a = [1, 2, 3];let b = [ ...a ];let c = a;b.push(4);console.log(a);  // [1, 2, 3]console.log(b);  // [1, 2, 3, 4] référençant différents tableauxc.push(5);console.log(a);  // [1, 2, 3, 5] console.log(c);  // [1, 2, 3, 5] référençant le même tableau
```

Le deuxième cas d'utilisation consiste à regrouper des variables dans un tableau. Cela est très utile lorsque vous ne savez pas combien de variables sont passées à une fonction.

```
function foo(...args) {    console.log(args); } foo( 'car', 54, 'tree');  //  [ 'car', 54, 'tree' ] 
```

### Paramètres par défaut

Les fonctions peuvent maintenant être définies avec des paramètres par défaut. Les valeurs manquantes ou indéfinies sont initialisées avec la valeur par défaut. Faites simplement attention — car les valeurs null et false sont coercées à 0.

```
function foo( a = 5, b = 10) {    console.log( a + b);} foo();  // 15foo( 7, 12 );  // 19foo( undefined, 8 ); // 13foo( 8 ); // 18foo( null ); // 10 car null est coercé à 0
```

Les valeurs par défaut peuvent être plus que de simples valeurs — elles peuvent également être des expressions ou des fonctions.

```
function foo( a ) { return a * 4; }function bar( x = 2, y = x + 4, z = foo(x)) {    console.log([ x, y, z ]);}bar();  // [ 2, 6, 8 ]bar( 1, 2, 3 ); //[ 1, 2, 3 ] bar( 10, undefined, 3 );  // [ 10, 14, 3 ]
```

### Déstructuration

La déstructuration est le processus de décomposition du tableau ou de l'objet du côté gauche du signe égal. Le tableau ou l'objet peut provenir d'une variable, d'une fonction ou d'une équation.

```
let [ a, b, c ] = [ 6, 2, 9];console.log(`a=${a}, b=${b}, c=${c}`); //a=6, b=2, c=9
```

```
function foo() { return ['car', 'dog', 6 ]; } let [ x, y, z ] = foo();console.log(`x=${x}, y=${y}, z=${z}`);  // x=car, y=dog, z=6
```

Avec la déstructuration d'objet, les clés de l'objet peuvent être listées à l'intérieur des accolades pour extraire cette paire clé-valeur.

```
function bar() { return {a: 1, b: 2, c: 3}; }let { a, c } = bar();console.log(a); // 1console.log(c); // 3console.log(b); // undefined
```

Parfois, vous voulez extraire les valeurs mais les assigner à une nouvelle variable. Cela se fait en utilisant une paire 'clé: variable' à gauche du signe égal.

```
function baz() {     return {        x: 'car',        y: 'London',        z: { name: 'John', age: 21}    }; }let { x: vehicle, y: city, z: { name: driver } } = baz();
```

```
console.log(    `I'm going to ${city} with ${driver} in their ${vehicle}.`); // I'm going to London with John in their car. 
```

Une autre chose que la déstructuration d'objet permet est d'assigner une valeur à plusieurs variables.

```
let { x: first, x: second } = { x: 4 };console.log( first, second ); // 4, 4
```

### Littéraux d'objet et paramètres concis

Lorsque vous créez un littéral d'objet à partir de variables, ES6 vous permet d'omettre la clé si elle est identique au nom de la variable.

```
let a = 4, b = 7;let c = { a: a, b: b };let concise = { a, b };console.log(c, concise) // {a: 4, b: 7}, {a: 4, b: 7}
```

Cela peut également être utilisé en combinaison avec la déstructuration pour rendre votre code beaucoup plus simple et plus propre.

```
function foo() {    return {        name: 'Anna',         age: 56,       job: { company: 'Tesco', title: 'Manager' }    };} 
```

```
// pré ES6let a = foo(), name = a.name, age = a.age, company = a.job.company;
```

```
// ES6 déstructuration et paramètres concis let { name, age, job: {company}} = foo();
```

Il peut également être utilisé pour déstructurer les objets passés dans les fonctions. Les méthodes 1 et 2 sont la façon dont vous l'auriez fait avant ES6, et la méthode 3 utilise la déstructuration et les paramètres concis.

```
let person = {    name: 'Anna',     age: 56,    job: { company: 'Tesco', title: 'Manager' }};
```

```
// méthode 1function old1( person) {    var yearOfBirth = 2018 - person.age;    console.log( `${ person.name } works at ${ person.job.company } and was born in ${ yearOfBirth }.`);}
```

```
// méthode 2function old1( person) {    var age = person.age,        yearOfBirth = 2018 - age,         name = person.name,        company = person.job.company;    console.log( `${ name } works at ${ company } and was born in ${ yearOfBirth }.`);} 
```

```
// méthode 3function es6({ age, name, job: {company}}) {    var yearOfBirth = 2018 - age;    console.log( `${ name } works at ${ company } and was born in ${ yearOfBirth }.`);} 
```

En utilisant ES6, nous pouvons extraire `age`, `name` et `company` sans déclaration de variable supplémentaire.

### Noms de propriétés dynamiques

ES6 ajoute la possibilité de créer ou d'ajouter des propriétés avec des clés assignées dynamiquement.

```
let  city= 'sheffield_';let a = {    [ city + 'population' ]: 350000};a[ city + 'county' ] = 'South Yorkshire';console.log(a); // {sheffield_population: 350000, sheffield_county: 'South Yorkshire' }
```

### Fonctions fléchées

Les fonctions fléchées ont deux aspects principaux : leur structure et leur liaison `this`.

Elles peuvent avoir une structure beaucoup plus simple que les fonctions traditionnelles car elles n'ont pas besoin du mot clé `function`, et elles retournent automatiquement ce qui suit la flèche.

```
var foo = function( a, b ) {    return a * b;} 
```

```
let bar = ( a, b ) => a * b;
```

Si la fonction nécessite plus qu'un simple calcul, des accolades peuvent être utilisées et la fonction retourne ce qui est retourné par la portée de bloc.

```
let baz = ( c, d ) => {    let length = c.length + d.toString().length;    let e = c.join(', ');    return `${e} and there is a total length of  ${length}`;}
```

L'un des endroits les plus utiles pour les fonctions fléchées est dans les fonctions de tableau comme `.map`, `.forEach` ou `.sort`.

```
let arr = [ 5, 6, 7, 8, 'a' ];let b = arr.map( item => item + 3 );console.log(b); // [ 8, 9, 10, 11, 'a3' ]
```

En plus d'avoir une syntaxe plus courte, cela résout également les problèmes qui survenaient souvent autour du comportement de liaison `this`. La solution avec les fonctions pré-ES6 était de stocker la référence `this`, souvent en tant que variable `self`.

```
var clickController = {    doSomething: function (..) {        var self = this;        btn.addEventListener(            'click',             function() { self.doSomething(..) },             false       );   } };
```

Cela devait être fait parce que la liaison `this` est dynamique. Cela signifie que le `this` à l'intérieur de l'écouteur d'événement et le `this` à l'intérieur de `doSomething` ne font pas référence à la même chose.

À l'intérieur des fonctions fléchées, la liaison `this` est lexicale, pas dynamique. C'était la principale caractéristique de conception de la fonction fléchée.

Bien que la liaison lexicale `this` puisse être géniale, parfois ce n'est pas ce qui est souhaité.

```
let a = {    oneThing: ( a ) => {         let b = a * 2;         this.otherThing(b);    },     otherThing: ( b ) => {....} };
```

```
a.oneThing(6);
```

Lorsque nous utilisons `a.oneThing(6)`, la référence `this.otherThing( b )` échoue car `this` ne pointe pas vers l'objet `a`, mais vers la portée environnante. Si vous réécrivez du code hérité en utilisant la syntaxe ES6, c'est quelque chose à surveiller.

### Boucles `for ... of`

ES6 ajoute un moyen d'itérer sur chacune des valeurs d'un tableau. Cela est différent de la boucle `for ... in` existante qui itère sur la clé/l'index.

```
let a = ['a', 'b', 'c', 'd' ];// ES6 for ( var val of a ) {    console.log( val );} // "a" "b" "c" "d"// pré-ES6 for ( var idx in a ) {    console.log( idx );}  // 0 1 2 3
```

L'utilisation de la nouvelle boucle `for ... of` évite d'ajouter un `let val = a[idx]` à l'intérieur de chaque boucle.

Les tableaux, les chaînes de caractères, les générateurs et les collections sont tous itérables en JavaScript standard. Les objets simples ne peuvent normalement pas être itérés, sauf si vous avez défini un itérateur pour eux.

### Littéraux numériques

Le code ES5 gérait bien les formats de nombres décimaux et hexadécimaux, mais le format octal n'était pas spécifié. En fait, il était activement interdit en mode strict.

ES6 a ajouté un nouveau format, en ajoutant un `o` après le `0` initial pour déclarer le nombre en octal. Ils ont également ajouté un format binaire.

```
Number( 29 )  // 29Number( 035 ) // 35 dans l'ancien format octal. Number( 0o35 ) // 29 dans le nouveau format octal Number( 0x1d ) // 29 en hexadécimal Number( 0b11101 ) // 29 en binaire
```

### Et bien plus encore...

Il y a beaucoup, beaucoup plus que ES6 nous offre pour rendre notre code plus propre, plus court, plus facile à lire et plus robuste. Je vise à écrire une continuation de cet article couvrant les parties moins connues de ES6.

Si vous ne pouvez pas attendre aussi longtemps, lisez le livre [You Don't Know JS book on ES6](https://github.com/getify/You-Dont-Know-JS/blob/master/es6%20%26%20beyond/ch2.md) de Kyle Simpson, ou consultez ce [site web brillant](http://es6-features.org/#Constants) !

Voulez-vous devenir développeur et obtenir votre premier emploi dans le logiciel ? Téléchargez les [7 étapes pour devenir développeur et obtenir votre premier emploi](https://mailchi.mp/4e8890d8138a/completecoding).

> SUIVANT - Comment sécuriser l'emploi de vos rêves. Maîtrisez le processus d'entretien

Si vous avez aimé cela et que vous l'avez trouvé utile, montrez votre soutien en applaudissant et abonnez-vous pour obtenir plus d'articles comme celui-ci !

![Image](https://cdn-media-1.freecodecamp.org/images/YteINwvwgVVGxTMs5umIsksyix1ILkn-W0dD)

![Image](https://cdn-media-1.freecodecamp.org/images/w12a6mIA8-w7GgPNcl2wD7rHCVlNKVYHpuEB)

![Image](https://cdn-media-1.freecodecamp.org/images/bs1er3gxQhRoQ1WIfxT6fZLLBUFNIdAR9ER5)