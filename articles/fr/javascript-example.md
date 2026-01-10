---
title: Les meilleurs exemples JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-21T17:38:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f25740569d1a4ca4102.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Les meilleurs exemples JavaScript
seo_desc: 'JavaScript is the most widely used scripting language on earth. Here are
  some examples of key syntax patterns in JavaScript.

  Argument Example

  The arguments object is an array-like object (in that the structure of the object
  is similar to that of an a...'
---

JavaScript est le langage de script le plus largement utilisé sur terre. Voici quelques exemples de modèles de syntaxe clés en JavaScript.

## Exemple d'argument

L'objet arguments est un **objet de type tableau** _(en ce sens que la structure de l'objet est similaire à celle d'un tableau ; cependant, il ne doit pas être considéré comme un tableau car il a toute la fonctionnalité d'un objet)_ qui stocke tous les arguments que vous avez passés à une fonction et est propre à cette fonction en particulier. 

Si vous passiez 3 arguments à une fonction, disons `storeNames()`, ces 3 arguments seraient stockés à l'intérieur d'un objet appelé **arguments** et cela ressemblerait à ceci lorsque nous passons les arguments `storeNames("Mulder", "Scully", "Alex Krycek")` à notre fonction :

* Tout d'abord, nous déclarons une fonction et la faisons retourner l'objet arguments.
* Ensuite, lorsque nous exécutons cette fonction avec **n arguments**, 3 dans ce cas, elle nous retournera l'objet et il **ressemblera** à un tableau. Nous pouvons le convertir en tableau, mais nous en parlerons plus tard...

```javascript
function storeNames() { return arguments; }
```

```javascript
// Si nous exécutons la ligne suivante dans la console :
storeNames("Mulder", "Scully", "Alex Kryceck");
// La sortie sera { '0': 'Mulder', '1': 'Scully', '2': 'Alex Kryceck' }
```

## **Traiter comme un tableau**

Vous pouvez invoquer des arguments en utilisant `arguments[n]` (où _n_ est l'index de l'argument dans l'objet de type tableau). Mais si vous voulez l'utiliser comme un tableau pour des fins d'itération ou pour appliquer des méthodes de tableau, vous devez _le convertir en tableau_ en déclarant une variable et en utilisant la méthode Array.prototype.slice.call (car _arguments_ n'est pas un tableau) :

```javascript
var args = Array.prototype.slice.call(arguments);

// ou la méthode ES6 :
var args = Array.from(arguments)
```

Puisque **slice()** a deux paramètres (le paramètre **end** est optionnel). Vous pouvez saisir une certaine portion des arguments en spécifiant le début et la fin de votre portion (utiliser la méthode _slice.call()_ rend ces deux paramètres optionnels, pas seulement _end_). Consultez le code suivant :

```javascript
function getGrades() {
    var args = Array.prototype.slice.call(arguments, 1, 3);
    return args;
}

// Affichons cela !
console.log(getGrades(90, 100, 75, 40, 89, 95));

// LA SORTIE DOIT ÊTRE : //
// [100, 75] <- Pourquoi ? Parce qu'il a commencé à l'index 1 et s'est arrêté à l'index 3
// donc, l'index 3 (40) n'a pas été pris en considération.
//
// Si nous supprimons le paramètre '3', laissant juste (arguments, 1) nous obtiendrions
// chaque argument à partir de l'index 1 : [100, 75, 40, 89, 95].
```

### **Problèmes d'optimisation avec Array.slice()**

Il y a un petit problème : il n'est pas recommandé d'utiliser slice dans l'objet arguments (pour des raisons d'optimisation)...

**Important** : Vous ne devriez pas utiliser slice sur les arguments car cela empêche les optimisations dans les moteurs JavaScript (V8 par exemple). Au lieu de cela, essayez de construire un nouveau tableau en itérant à travers l'objet arguments.

Alors, quelle autre méthode est disponible pour convertir _arguments_ en tableau ? Je recommande la boucle for (pas la boucle for-in). Vous pouvez le faire comme ceci :

```javascript
var args = []; // Tableau vide, au début.
for (var i = 0; i < arguments.length; i++) {
    args.push(arguments[i])
} // Maintenant 'args' est un tableau qui contient vos arguments.
```

Pour plus d'informations sur les problèmes d'optimisation : [Optimization Killers: Managing Arguments](https://github.com/petkaantonov/bluebird/wiki/Optimization-killers#3-managing-arguments)

### **Paramètre rest ES6 comme moyen de contourner l'objet arguments**

En ES2015/ES6, il est possible d'utiliser le paramètre rest (`...`) au lieu de l'objet arguments dans la plupart des cas. Supposons que nous avons la fonction suivante (non-ES6) :

```text
function getIntoAnArgument() {
    var args = arguments.slice();
    args.forEach(function(arg) {
        console.log(arg);
    });
}
```

Cette fonction peut être remplacée en ES6 par :

```text
function getIntoAnArgument(...args) {
    args.forEach(arg => console.log(arg));
}
```

Notez que nous avons également utilisé une fonction fléchée pour raccourcir le rappel forEach !

L'objet arguments n'est pas disponible à l'intérieur du corps d'une fonction fléchée.

Le paramètre rest doit toujours venir comme dernier argument dans votre définition de fonction.  
`function getIntoAnArgument(arg1, arg2, arg3, ...restOfArgs /* aucun autre argument autorisé ici */) { // corps de la fonction }`

## Exemple d'opération arithmétique

JavaScript fournit à l'utilisateur cinq opérateurs arithmétiques : `+`, `-`, `*`, `/` et `%`. Les opérateurs sont pour l'addition, la soustraction, la multiplication, la division et le reste, respectivement.

## **Addition**

**Syntaxe**

`a + b`

**Utilisation**

```text
2 + 3          // retourne 5
true + 2       // interprète true comme 1 et retourne 3
false + 5      // interprète false comme 0 et retourne 5
true + "bar"   // concatène la valeur booléenne et retourne "truebar"
5 + "foo"      // concatène la chaîne et le nombre et retourne "5foo"
"foo" + "bar"  // concatène les chaînes et retourne "foobar"
```

_Astuce :_ Il y a un opérateur [incrément](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Increment_() pratique qui est un excellent raccourci lorsque vous ajoutez des nombres par 1.

## **Soustraction**

**Syntaxe**

`a - b`

**Utilisation**

```text
2 - 3      // retourne -1
3 - 2      // retourne 1
false - 5  // interprète false comme 0 et retourne -5
true + 3   // interprète true comme 1 et retourne 4
5 + "foo"  // retourne NaN (Not a Number)
```

_Astuce :_ Il y a un opérateur [décrément](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Decrement_(--) pratique qui est un excellent raccourci lorsque vous soustrayez des nombres par 1.

## **Multiplication**

**Syntaxe**

`a * b`

**Utilisation**

```text
2 * 3                // retourne 6
3 * -2               // retourne -6
false * 5            // interprète false comme 0 et retourne 0
true * 3             // interprète true comme 1 et retourne 3
5 * "foo"            // retourne NaN (Not a Number)
Infinity * 0         // retourne NaN
Infinity * Infinity  // retourne Infinity
```

_Astuce :_ Lors de la réalisation de calculs, il est possible d'utiliser des parenthèses pour prioriser les nombres qui doivent être multipliés ensemble.

## **Division**

**Syntaxe**

`a / b`

**Utilisation**

```text
3 / 2                // retourne 1.5
3.0 / 2/0            // retourne 1.5
3 / 0                // retourne Infinity
3.0 / 0.0            // retourne Infinity
-3 / 0               // retourne -Infinity
false / 5            // interprète false comme 0 et retourne 0
true / 2             // interprète true comme 1 et retourne 0.5
5 + "foo"            // retourne NaN (Not a Number)
Infinity / Infinity  // retourne NaN
```

## **Reste**

**Syntaxe**

`a % b`

**Utilisation**

```text
3 % 2          // retourne 1
true % 5       // interprète true comme 1 et retourne 1
false % 4      // interprète false comme 0 et retourne 0
3 % "bar"      // retourne NaN
```

## **Incrément**

**Syntaxe**

`a++ ou ++a`

**Utilisation** 

```js
// Postfix 
x = 3; // déclarer une variable 
y = x++; // y = 4, x = 3 

// Préfix 
var a = 2; 
b = ++a; // a = 3, b = 3
```

## **Décrément**

**Syntaxe**

`a-- ou --a`

**Utilisation** 

```js
// Postfix 
x = 3; // déclarer une variable 
y = x--; // y = 3, x = 3 

// Préfix 
var a = 2; 
b = --a; // a = 1, b = 1
```

_Important :_ Comme vous pouvez le voir, vous **ne pouvez pas** effectuer d'opérations sur `Infinity`.

### Exemple de fonction fléchée

Les fonctions fléchées sont une nouvelle syntaxe ES6 pour écrire des expressions de fonction JavaScript. La syntaxe plus courte économise du temps, ainsi que simplifie la portée de la fonction.

## **Qu'est-ce que les fonctions fléchées ?**

Une expression de fonction fléchée est une syntaxe plus concise pour écrire des expressions de fonction en utilisant un jeton de "flèche grasse" (`=>`).

### **La syntaxe de base**

Voici un exemple de base d'une fonction fléchée :

```javascript
// Syntaxe ES5
var multiply = function(x, y) {
  return x * y;
};

// Fonction fléchée ES6
var multiply = (x, y) => { return x * y; };

// Ou encore plus simple
var multiply = (x, y) => x * y;    
```

Vous n'avez plus besoin des mots-clés `function` et `return`, ni même des accolades.

### **Un `this` simplifié**

Avant les fonctions fléchées, les nouvelles fonctions définissaient leur propre valeur `this`. Pour utiliser `this` à l'intérieur d'une expression de fonction traditionnelle, nous devons écrire un contournement comme suit :

```javascript
// Syntaxe ES5
function Person() {
  // nous assignons `this` à `self` pour pouvoir l'utiliser plus tard
  var self = this;
  self.age = 0;

  setInterval(function growUp() {
    // `self` fait référence à l'objet attendu
    self.age++;
  }, 1000);
}
```

Une fonction fléchée ne définit pas sa propre valeur `this`, elle hérite de `this` de la fonction englobante :

```javascript
// Syntaxe ES6
function Person(){
  this.age = 0;

  setInterval(() => {
    // `this` fait maintenant référence à l'objet Person, brillant !
    this.age++;
  }, 1000);
}

var p = new Person();
```

## Opérateurs d'assignation

## Exemple d'opérateur d'assignation

Les opérateurs d'assignation, comme leur nom l'indique, assignent (ou réassignent) des valeurs à une variable. Bien qu'il existe plusieurs variations des opérateurs d'assignation, ils s'appuient tous sur l'opérateur d'assignation de base.

Syntaxe = **y;DescriptionNecessityxVariableRequired=Assignment operatorRequiredyValue to assign to variableRequired**

## **Exemples**

```text
let initialVar = 5;   // L'initialisation de la variable nécessite l'utilisation d'un opérateur d'assignation

let newVar = 5;
newVar = 6;   // Les valeurs des variables peuvent être modifiées en utilisant un opérateur d'assignation
```

## **Variations**

Les autres opérateurs d'assignation sont un raccourci pour effectuer une opération en utilisant la variable (indiquée par x ci-dessus) et la valeur (indiquée par y ci-dessus) puis en assignant le résultat à la variable elle-même.

Par exemple, voici la syntaxe pour l'opérateur d'addition et d'assignation :

```text
x += y;
```

Cela revient à appliquer l'opérateur d'addition et à réassigner la somme à la variable d'origine (c'est-à-dire x), ce qui peut être exprimé par le code suivant :

```text
x = x + y;
```

Pour illustrer cela avec des valeurs réelles, voici un autre exemple d'utilisation de l'opérateur d'addition et d'assignation :

```text
let myVar = 5;   // valeur de myVar : 5
myVar += 7;   // valeur de myVar : 12 = 5 + 7
```

### Liste complète des opérateurs d'assignation de JavaScript

Opérateur | Syntaxe | Version longue  
------------------------------- | --------- | -------------  
Assignment | x = y | x = y  
Addition assignment | x += y | x = x + y  
Subtraction assignment | x -= y | x = x - y  
Multiplication assignment | x *= y | x = x * y  
Division assignment | x /= y | x = x / y  
Remainder assignment | x %= y | x = x % y  
Exponentiation assignment | x **= y | x = x ** y  
Left shift assignment | x <<= y | x = x << y  
Right shift assignment | x >>= y | x = x >> y  
Unsigned right shift assignment | x >>>= y | x = x >>> y  
Bitwise AND assignment | x &= y | x = x & y  
Bitwise XOR assignment | x ^= y | x = x ^ y  
Bitwise OR assignment | x |= y | x = x | y

## **Exemple de booléen**

Les booléens sont un type de données primitif couramment utilisé dans les langages de programmation informatique. Par définition, un booléen a deux valeurs possibles : `true` ou `false`.

En JavaScript, il y a souvent une coercition de type implicite vers un booléen. Si, par exemple, vous avez une instruction if qui vérifie une certaine expression, cette expression sera coercée en un booléen :

```javascript
var a = 'a string';
if (a) {
  console.log(a); // logs 'a string'
}
```

Il n'y a que quelques valeurs qui seront coercées en false :

* false (pas vraiment coercé, car il est déjà false)
* null
* undefined
* NaN
* 0
* "" (chaîne vide)

Toutes les autres valeurs seront coercées en true. Lorsqu'une valeur est coercée en un booléen, nous l'appelons aussi soit 'falsy' soit 'truthy'.

Une façon dont la coercition de type est utilisée est avec l'utilisation des opérateurs ou (`||`) et et (`&&`) :

```javascript
var a = 'word';
var b = false;
var c = true;
var d = 0
var e = 1
var f = 2
var g = null

console.log(a || b); // 'word'
console.log(c || a); // true
console.log(b || a); // 'word'
console.log(e || f); // 1
console.log(f || e); // 2
console.log(d || g); // null
console.log(g || d); // 0
console.log(a && c); // true
console.log(c && a); // 'word'
```

Comme vous pouvez le voir, l'opérateur _ou_ vérifie le premier opérande. Si celui-ci est vrai ou truthy, il le retourne immédiatement (c'est pourquoi nous obtenons 'word' dans le premier cas & true dans le deuxième cas). Si ce n'est pas vrai ou truthy, il retourne le deuxième opérande (c'est pourquoi nous obtenons 'word' dans le troisième cas).

Avec l'opérateur et, cela fonctionne de manière similaire, mais pour que 'et' soit vrai, les deux opérandes doivent être truthy. Il retournera donc toujours le deuxième opérande si les deux sont vrais/truthy, sinon il retournera false. C'est pourquoi dans le quatrième cas nous obtenons true et dans le dernier cas nous obtenons 'word'.

## **L'objet Boolean**

Il existe également un objet natif JavaScript `Boolean` qui enveloppe une valeur et convertit le premier paramètre en une valeur booléenne. Si une valeur est omise ou falsy -0, -0, `null`, `false`, `NaN`, `undefined`, ou une chaîne vide (`""`) - la valeur de l'objet est false. Passez toutes les autres valeurs, y compris la chaîne `"false"`, et la valeur de l'objet est définie sur true.

Notez que les valeurs booléennes primitives (`true` et `false`) sont différentes de celles de l'objet Boolean.

### Plus de détails

Rappelez-vous que tout objet, dont la valeur n'est pas `undefined` ou `null`, évalue à true s'il est utilisé dans une instruction conditionnelle. Par exemple, même si cet objet `Boolean` est explicitement défini sur false, il évalue à true et le code est exécuté :

```javascript
var greeting = new Boolean(false);
if (greeting) {
  console.log("Hello world");
}

// Hello world
```

Cela ne s'applique pas aux primitives booléennes :

```javascript
var greeting = false;
if (greeting) {
  console.log("Hello world"); // le code ne s'exécutera pas
}
```

Pour convertir une valeur non booléenne en booléenne, utilisez `Boolean` comme une fonction plutôt que comme un objet : 

```javascript
var x = Boolean(expression);     // utilisation préférée en tant que fonction
var x = new Boolean(expression); // ne faites pas cela
```

## Fonctions de rappel

Cette section donne une brève introduction au concept et à l'utilisation des fonctions de rappel en JavaScript.

### Les fonctions sont des objets

La première chose que nous devons savoir est qu'en JavaScript, les fonctions sont des objets de première classe. En tant que telles, nous pouvons travailler avec elles de la même manière que nous travaillons avec d'autres objets, comme les assigner à des variables et les passer comme arguments dans d'autres fonctions. Cela est important, car c'est cette dernière technique qui nous permet d'étendre la fonctionnalité dans nos applications.

## **Exemple de fonction de rappel**

Une **fonction de rappel** est une fonction qui est passée _en tant qu'argument_ à une autre fonction, pour être "rappelée" plus tard. 

Une fonction qui accepte d'autres fonctions comme arguments est appelée une **fonction d'ordre supérieur**, qui contient la logique pour _quand_ la fonction de rappel est exécutée. C'est la combinaison de ces deux éléments qui nous permet d'étendre notre fonctionnalité.

Pour illustrer les rappels, commençons par un exemple simple :

```javascript
function createQuote(quote, callback){ 
  var myQuote = "Comme je le dis toujours, " + quote;
  callback(myQuote); // 2
}

function logQuote(quote){
  console.log(quote);
}

createQuote("mangez vos légumes !", logQuote); // 1

// Résultat dans la console : 
// Comme je le dis toujours, mangez vos légumes !
```

Dans l'exemple ci-dessus, `createQuote` est la fonction d'ordre supérieur, qui accepte deux arguments, le second étant le rappel. La fonction `logQuote` est utilisée pour passer en tant que notre fonction de rappel. Lorsque nous exécutons la fonction `createQuote` _(1)_, notez que nous n'ajoutons _pas_ de parenthèses à `logQuote` lorsque nous la passons en tant qu'argument. Cela est dû au fait que nous ne voulons pas exécuter notre fonction de rappel immédiatement, nous voulons simplement passer la définition de la fonction à la fonction d'ordre supérieur afin qu'elle puisse être exécutée plus tard.

De plus, nous devons nous assurer que si la fonction de rappel que nous passons attend des arguments, nous fournissons ces arguments lors de l'exécution du rappel _(2)_. Dans l'exemple ci-dessus, ce serait l'instruction `callback(myQuote);` , puisque nous savons que `logQuote` attend qu'une citation soit passée.

De plus, nous pouvons passer des fonctions anonymes en tant que rappels. L'appel suivant à `createQuote` aurait le même résultat que l'exemple ci-dessus :

```javascript
createQuote("mangez vos légumes !", function(quote){ 
  console.log(quote); 
});
```

Incidemment, vous n'avez pas _besoin_ d'utiliser le mot "callback" comme nom de votre argument. JavaScript doit simplement savoir que c'est le nom correct de l'argument. Basé sur l'exemple ci-dessus, la fonction suivante se comportera de la même manière.

```javascript
function createQuote(quote, functionToCall) { 
  var myQuote = "Comme je le dis toujours, " + quote;
  functionToCall(myQuote);
}
```

## **Pourquoi utiliser les rappels ?**

La plupart du temps, nous créons des programmes et des applications qui fonctionnent de manière **synchrone**. En d'autres termes, certaines de nos opérations ne sont démarrées qu'après que les précédentes ont été complétées. 

Souvent, lorsque nous demandons des données à d'autres sources, comme une API externe, nous ne savons pas toujours _quand_ nos données seront servies. Dans ces cas, nous voulons attendre la réponse, mais nous ne voulons pas toujours que notre application entière s'arrête pendant que nos données sont récupérées. Ces situations sont celles où les fonctions de rappel sont utiles.

Prenons un exemple qui simule une requête à un serveur :

```javascript
function serverRequest(query, callback){
  setTimeout(function(){
    var response = query + "full!";
    callback(response);
  },5000);
}

function getResults(results){
  console.log("Réponse du serveur : " + results);
}

serverRequest("Le verre est à moitié ", getResults);

// Résultat dans la console après un délai de 5 secondes :
// Réponse du serveur : Le verre est à moitié plein !
```

Dans l'exemple ci-dessus, nous faisons une requête simulée à un serveur. Après 5 secondes, la réponse est modifiée puis notre fonction de rappel `getResults` est exécutée. Pour voir cela en action, vous pouvez copier/coller le code ci-dessus dans l'outil de développement de votre navigateur et l'exécuter.

De plus, si vous êtes déjà familier avec `setTimeout`, alors vous avez utilisé des fonctions de rappel tout au long. La fonction anonyme passée en argument dans l'appel de la fonction `setTimeout` de l'exemple ci-dessus est également un rappel ! Donc le rappel original de l'exemple est en fait exécuté par un autre rappel. Faites attention à ne pas imbriquer trop de rappels si vous pouvez l'éviter, car cela peut conduire à ce que l'on appelle "l'enfer des rappels" ! Comme le nom l'indique, ce n'est pas un plaisir à gérer.

## **Exemple de classe JavaScript**

JavaScript n'a pas le concept de classes de manière inhérente.

Mais nous pourrions simuler les fonctionnalités d'une classe en tirant parti de la nature prototypale de JavaScript.

Cette section suppose que vous avez une compréhension de base des [prototypes](https://guide.freecodecamp.org/javascript/prototypes).

Pour plus de clarté, supposons que nous voulons créer une classe qui peut faire ce qui suit

```javascript
var p = new Person('James','Bond'); // créer une nouvelle instance de la classe Person
	p.log() // Output: 'I am James Bond' // Accéder à une fonction dans la classe
	// Utiliser des setters et getters 
	p.profession = 'spy'
	p.profession // output: James bond is a spy
```

### **Utilisation du mot-clé class**

Comme dans tout autre langage de programmation, vous pouvez maintenant utiliser le mot-clé `class` pour créer une classe.

Cela n'est pas supporté dans les anciens navigateurs et a été introduit dans ECMAScript 2015.

`class` est juste un sucre syntaxique sur le modèle d'héritage basé sur les prototypes existant de JavaScript.

En général, les programmeurs utilisent les méthodes suivantes pour créer une classe en JavaScript.

### **Utilisation de méthodes ajoutées aux prototypes :**

Ici, toutes les méthodes sont ajoutées au prototype

```javascript
function Person(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
}

Person.prototype.log = function() {
    console.log('I am', this._firstName, this._lastName);
}

// Cette ligne ajoute des getters et setters pour l'objet profession. Notez que généralement vous pourriez simplement écrire vos propres fonctions get et set comme la méthode 'log' ci-dessus.
// Puisque dans cet exemple nous essayons d'imiter la classe ci-dessus, nous essayons d'utiliser les propriétés getters et setters fournies par JavaScript
Object.defineProperty(Person.prototype, 'profession', {
    set: function(val) {
        this._profession = val;
    },
    get: function() {
        console.log(this._firstName, this._lastName, 'is a', this._profession);
    }
})
```

Vous pourriez également écrire des méthodes de prototype sur la fonction `Person` comme ci-dessous :

```javascript
Person.prototype = {
    log: function() {
        console.log('I am ', this._firstName, this._lastName);
    }
    set profession(val) {
        this._profession = val;
    }

    get profession() {
        console.log(this._firstName, this._lastName, 'is a', this._profession);
    }

}
```

### **Utilisation de méthodes ajoutées en interne**

Ici, les méthodes sont ajoutées en interne au lieu du prototype :

```javascript
function Person(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;

    this.log = function() {
        console.log('I am ', this._firstName, this._lastName);
    }

    Object.defineProperty(this, 'profession', {
        set: function(val) {
            this._profession = val;
        },
        get: function() {
            console.log(this._firstName, this._lastName, 'is a', this._profession);
        }
    })
}
```

### **Masquer les détails dans les classes avec des symboles**

Le plus souvent, certaines propriétés et méthodes doivent être cachées pour empêcher l'accès depuis l'extérieur de la fonction. 

Avec les classes, pour obtenir cette fonctionnalité, une façon de le faire est d'utiliser des symboles. Le symbole est un nouveau type intégré de JavaScript, qui peut être invoqué pour donner une nouvelle valeur de symbole. Chaque symbole est unique et peut être utilisé comme clé sur un objet. 

Un cas d'utilisation des symboles est que vous pouvez ajouter quelque chose à un objet que vous ne possédez peut-être pas, et vous ne voulez peut-être pas entrer en collision avec d'autres clés de l'objet. Par conséquent, créer un nouveau symbole et l'ajouter comme propriété à cet objet en utilisant un symbole est le plus sûr. De plus, lorsqu'une valeur de symbole est ajoutée à un objet, personne d'autre ne saura comment l'obtenir.

```javascript
class Person {
    constructor(firstName, lastName) {
        this._firstName = firstName;
        this._lastName = lastName;
    }

    log() {
        console.log('I am', this._firstName, this._lastName);
    }

    // setters
    set profession(val) {
        this._profession = val;
    }
    // getters
    get profession() {
        console.log(this._firstName, this._lastName, 'is a', this._profession);
    }
// Avec le code ci-dessus, même si nous pouvons accéder aux propriétés en dehors de la fonction pour changer leur contenu, que se passe-t-il si nous ne voulons pas cela.
// Les symboles viennent à la rescousse.
let s_firstname  = new Symbol();

class Person {
    constructor(firstName, lastName) {
        this[s_firstName] = firstName;
        this._lastName = lastName;
    }

    log() {
        console.log('I am', this._firstName, this._lastName);
    }

    // setters
    set profession(val) {
        this._profession = val;
    }
    // getters
    get profession() {
        console.log(this[s_firstName], this._lastName, 'is a', this._profession);
    }
```

### Exemple de fermeture JavaScript

Une fermeture est la combinaison d'une fonction et de l'environnement lexical (portée) dans lequel cette fonction a été déclarée. Les fermetures sont une propriété fondamentale et puissante de Javascript. Cette section discute du 'comment' et du 'pourquoi' des fermetures :

### **Exemple**

```js
// nous avons une fonction externe nommée walk et une fonction interne nommée fly

function walk (){
  
  var dist = '1780 feet';
  
  function fly(){
    console.log('At '+dist);
  }
  
  return fly;
}

var flyFunc = walk(); // appeler walk retourne la fonction fly qui est assignée à flyFunc
// vous pourriez vous attendre à ce que, une fois la fonction walk ci-dessus exécutée
// vous pourriez penser que JavaScript s'est débarrassé de la variable 'dist'

flyFunc(); // Logs out 'At 1780 feet'
// mais vous pouvez toujours utiliser la fonction comme ci-dessus 
// c'est le pouvoir des fermetures
```

### **Un autre exemple**

```js
function by(propName) {
    return function(a, b) {
        return a[propName] - b[propName];
    }
}

const person1 = {name: 'joe', height: 72};
const person2 = {name: 'rob', height: 70};
const person3 = {name: 'nicholas', height: 66};

const arr_ = [person1, person2, person3];

const arr_sorted = arr_.sort(by('height')); // [ { name: 'nicholas', height: 66 }, { name: 'rob', height: 70 },{ name: 'joe', height: 72 } ]
```

La fermeture 'se souvient' de l'environnement dans lequel elle a été créée. Cet environnement consiste en toutes les variables locales qui étaient dans la portée au moment où la fermeture a été créée.

```js
function outside(num) {
  var rememberedVar = num; // Dans cet exemple, rememberedVar est l'environnement lexical que la fermeture 'se souvient'
  return function inside() { // C'est la fonction dont la fermeture 'se souvient'
    console.log(rememberedVar)
  }
}

var remember1 = outside(7); // remember1 est maintenant une fermeture qui contient rememberedVar = 7 dans son environnement lexical, et // la fonction 'inside'
var remember2 = outside(9); // remember2 est maintenant une fermeture qui contient rememberedVar = 9 dans son environnement lexical, et // la fonction 'inside'

remember1(); // Cela exécute maintenant la fonction 'inside' qui console.log(rememberedVar) => 7
remember2(); // Cela exécute maintenant la fonction 'inside' qui console.log(rememberedVar) => 9 
```

Les fermetures sont utiles car elles vous permettent de 'vous souvenir' de données et ensuite de manipuler ces données à travers des fonctions retournées. Cela permet à Javascript d'émuler des méthodes privées que l'on trouve dans d'autres langages de programmation. Les méthodes privées sont utiles pour restreindre l'accès au code ainsi que pour gérer votre espace de noms global.

### **Variables et méthodes privées**

Les fermetures peuvent également être utilisées pour encapsuler des données/méthodes privées. Jetez un œil à cet exemple :

```javascript
const bankAccount = (initialBalance) => {
  const balance = initialBalance;

  return {
    getBalance: function() {
      return balance;
    },
    deposit: function(amount) {
      balance += amount;
      return balance;
    },
  };
};

const account = bankAccount(100);

account.getBalance(); // 100
account.deposit(10); // 110
```

Dans cet exemple, nous ne pourrons pas accéder à `balance` depuis n'importe où en dehors de la fonction `bankAccount`, ce qui signifie que nous venons de créer une variable privée. 

Où est la fermeture ? Eh bien, réfléchissez à ce que `bankAccount()` retourne. Il retourne en fait un objet avec un tas de fonctions à l'intérieur, et pourtant lorsque nous appelons `account.getBalance()`, la fonction est capable de "se souvenir" de sa référence initiale à `balance`. 

C'est le pouvoir de la fermeture, où une fonction "se souvient" de sa portée lexicale (portée de compilation), même lorsque la fonction est exécutée en dehors de cette portée lexicale.

### Émuler des variables à portée de bloc

Javascript n'avait pas de concept de variables à portée de bloc. Cela signifie que lors de la définition d'une variable à l'intérieur d'une boucle for, par exemple, cette variable était visible depuis l'extérieur de la boucle for également. Alors, comment les fermetures peuvent-elles nous aider à résoudre ce problème ? Regardons cela.

```javascript
    var funcs = [];
    
    for(var i = 0; i < 3; i++){
        funcs[i] = function(){
            console.log('My value is ' + i);  // créer trois fonctions différentes avec différentes valeurs de paramètre.
        }
    }
    
    for(var j = 0; j < 3; j++){
        funcs[j]();             // My value is 3
                                // My value is 3
                                // My value is 3
    }
```

Puisque la variable i n'a pas de portée de bloc, sa valeur dans les trois fonctions a été mise à jour avec le compteur de boucle et a créé des valeurs malveillantes. Les fermetures peuvent nous aider à résoudre ce problème en créant une capture de l'environnement dans lequel la fonction se trouvait lorsqu'elle a été créée, préservant ainsi son état.

```javascript
    var funcs = [];
    
    var createFunction = function(val){
	    return function() {console.log("My value: " + val);};
    }

    for (var i = 0; i < 3; i++) {
        funcs[i] = createFunction(i);
    }
    for (var j = 0; j < 3; j++) {
        funcs[j]();                 // My value is 0
                                    // My value is 1
                                    // My value is 2
    }
```

Les versions ultérieures de Javascript (ES6+) ont un nouveau mot-clé appelé let qui peut être utilisé pour donner à la variable une portée de bloc. Il existe également de nombreuses fonctions (forEach) et des bibliothèques entières (lodash.js) qui sont dédiées à la résolution de tels problèmes comme ceux expliqués ci-dessus. Ils peuvent certainement augmenter votre productivité, cependant, il reste extrêmement important d'avoir des connaissances sur tous ces problèmes lorsque vous essayez de créer quelque chose de grand.

Les fermetures ont de nombreuses applications spéciales qui sont utiles lors de la création de grands programmes Javascript.

1. Émuler des variables privées ou l'encapsulation
2. Faire des appels côté serveur asynchrones
3. Créer une variable à portée de bloc.

### Émuler des variables privées

Contrairement à de nombreux autres langages, Javascript n'a pas de mécanisme qui vous permet de créer des variables d'instance encapsulées dans un objet. Avoir des variables d'instance publiques peut causer beaucoup de problèmes lors de la construction de programmes de taille moyenne à grande. Cependant, avec les fermetures, ce problème peut être atténué.

Comme dans l'exemple précédent, vous pouvez construire des fonctions qui retournent des littéraux d'objet avec des méthodes qui ont accès aux variables locales de l'objet sans les exposer. Ainsi, les rendant effectivement privées.

Les fermetures peuvent également vous aider à gérer votre espace de noms global pour éviter les collisions avec des données partagées globalement. Habituellement, toutes les variables globales sont partagées entre tous les scripts de votre projet, ce qui vous causera définitivement beaucoup de problèmes lors de la construction de programmes de taille moyenne à grande. 

C'est pourquoi les auteurs de bibliothèques et de modules utilisent des fermetures pour cacher les méthodes et les données d'un module entier. Cela s'appelle le modèle de module, il utilise une expression de fonction immédiatement invoquée qui exporte uniquement certaines fonctionnalités vers le monde extérieur, réduisant ainsi considérablement le nombre de références globales.

Voici un court exemple de squelette de module.

```javascript
var myModule = (function() = {
    let privateVariable = 'I am a private variable';
    
    let method1 = function(){ console.log('I am method 1'); };
    let method2 = function(){ console.log('I am method 2, ', privateVariable); };
    
    return {
        method1: method1,
        method2: method2
    }
}());

myModule.method1(); // I am method 1
myModule.method2(); // I am method 2, I am a private variable
```

Les fermetures sont utiles pour capturer de nouvelles instances de variables privées contenues dans l'environnement 'mémorisé', et ces variables ne peuvent être accessibles que par la fonction ou les méthodes retournées.

### Exemple de commentaire JavaScript

Les programmeurs utilisent des commentaires pour ajouter des indices, des notes, des suggestions ou des avertissements à leur code source ; ils n'ont aucun effet sur la sortie réelle du code. Les commentaires peuvent être très utiles pour expliquer l'intention de ce que votre code fait ou devrait faire.

Il est toujours une bonne pratique, lorsque vous commencez, de commenter plus souvent qu'autrement, car cela peut aider ceux qui lisent votre code à comprendre ce que votre code entend faire exactement.

JavaScript a deux façons d'assigner des commentaires dans son code.

La première façon est le commentaire `//` ; tout le texte suivant `//` sur la même ligne devient un commentaire. Par exemple :

```javascript
function hello() {
  // Ceci est un commentaire JavaScript sur une ligne
  console.log("Hello world!");
}
hello();
```

La deuxième façon est le commentaire `/* */`, qui peut être utilisé pour les commentaires sur une seule ligne et sur plusieurs lignes. Par exemple :

```javascript
function hello() {
  /* Ceci est un commentaire JavaScript sur une ligne */
  console.log("Hello world!");
}
hello();
```

```javascript
function hello() {
  /* Ce commentaire s'étend sur plusieurs lignes. Remarquez
     que nous n'avons pas besoin de terminer le commentaire avant d'avoir fini. */
  console.log("Hello world!");
}
hello();
```

Vous pouvez également empêcher l'exécution de code JavaScript en commentant simplement les lignes de code comme ceci :

```javascript
function hello() {
  /*console.log("Hello world!");*/
}
hello();
```

#### **Plus d'informations :**

[Comment écrire des commentaires en JavaScript](https://www.digitalocean.com/community/tutorials/how-to-write-comments-in-javascript)

### **De nombreux IDE viennent avec un raccourci clavier pour commenter des lignes.**

1. Surbrillance du texte à commenter
2. Mac : Appuyez sur Command (Touche Apple) & "/"
3. Windows : Appuyez sur Control & "/"
4. Vous pouvez également décommenter du code en effectuant les mêmes étapes

Un raccourci pour commenter une section de JavaScript dans de nombreux éditeurs de code est de surligner les lignes de code que vous souhaitez commenter, puis d'appuyer sur `Cmd/Ctrl + /`.

Les commentaires sont également très utiles pour les tests de code, car vous pouvez empêcher une certaine ligne/bloc de code de s'exécuter :

```javascript
function hello() {
  // L'instruction ci-dessous ne sera pas exécutée
  // console.log('hi')
  }
hello();
```

```text
function hello() {
  // Les instructions ci-dessous ne seront pas exécutées
  /*
  console.log('hi');
  console.log('code-test');
  */
}
hello();
```

## Exemple d'opérateur de comparaison JavaScript

JavaScript possède à la fois des comparaisons **strictes** et des comparaisons **avec conversion de type**.

* La comparaison stricte (`===`) n'évalue à vrai que si les deux opérandes sont du même type.
* La comparaison abstraite (`==`) tente de convertir les deux opérandes au même type avant de les comparer.
* Avec les comparaisons abstraites relationnelles (`<=`), les deux opérandes sont convertis en primitives, puis au même type avant la comparaison.
* Les chaînes sont comparées en utilisant les valeurs Unicode basées sur l'ordre standard.

## **Caractéristiques des comparaisons :**

* Deux chaînes sont considérées comme strictement égales lorsqu'elles ont les caractères dans la même séquence et la même longueur.
* Deux nombres sont considérés comme strictement égaux lorsqu'ils sont tous deux du type nombre et sont numériquement égaux. Cela signifie que `0` et `-0` sont strictement égaux puisqu'ils évaluent tous deux à `0`. Notez que `NaN` est une valeur spéciale et n'est égale à rien, y compris `NaN`.
* Deux opérandes booléens sont considérés comme strictement égaux si les deux sont `true` ou `false`.
* Deux objets ne sont jamais considérés comme égaux dans les comparaisons strictes ou abstraites.
* Les expressions qui comparent des objets ne sont considérées comme vraies que si les opérandes référencent tous deux la même instance exacte de l'objet.
* Null et undefined sont tous deux considérés comme strictement égaux à eux-mêmes (`null === null`) et abstraitement égaux l'un à l'autre (`null == undefined`)

## **Opérateurs d'égalité**

### **Égalité (==)**

L'opérateur d'égalité convertit d'abord les opérandes qui ne sont pas du même type, puis les compare strictement l'un à l'autre.

#### **Syntaxe**

```text
 x == y
```

#### **Exemples**

```text
 1   ==  1        // true
"1"  ==  1        // true
 1   == '1'       // true
 0   == false     // true
 0   == null      // false

 0   == undefined   // false
 null  == undefined // true
```

### **Inégalité (!=)**

L'opérateur d'inégalité évalue à vrai si les deux opérandes ne sont pas égaux. Si les opérandes ne sont pas du même type, il essaiera de les convertir au même type avant de faire la comparaison.

#### **Syntaxe**

```text
x != y
```

#### **Exemples**

```text
1 !=   2     // true
1 !=  "1"    // false
1 !=  '1'    // false
1 !=  true   // false
0 !=  false  // false
```

### **Identité / égalité stricte (===)**

L'opérateur d'identité ou d'égalité stricte retourne vrai si les deux opérandes sont strictement égaux en termes de valeur et de type. Contrairement à l'opérateur d'égalité (`==`), il ne tentera pas de convertir les opérandes au même type.

#### **Syntaxe**

```text
x === y
```

#### **Exemples**

```text
3 === 3   // true
3 === '3' // false
```

### **Non-identité / inégalité stricte (!==)**

L'opérateur de non-identité ou d'inégalité stricte retourne vrai si les deux opérandes ne sont pas strictement égaux en termes de valeur ou de type.

#### **Syntaxe**

```text
x !== y
```

#### **Exemples**

```text
3 !== '3' // true
4 !== 3   // true
```

## **Opérateurs relationnels**

### **Opérateur supérieur à (>)**

L'opérateur supérieur à retourne vrai si l'opérande de gauche est supérieur à celui de droite.

#### **Syntaxe**

```text
x > y
```

#### **Exemples**

```text
4 > 3 // true
```

### **Opérateur supérieur ou égal à (>=)**

L'opérateur supérieur ou égal à retourne vrai si l'opérande de gauche est supérieur ou égal à celui de droite.

#### **Syntaxe**

```text
x >= y
```

#### **Exemples**

```text
4 >= 3 // true
3 >= 3 // true
```

### **Opérateur inférieur à (<)**

L'opérateur inférieur à retourne vrai si l'opérande de gauche est inférieur à celui de droite.

#### **Syntaxe**

```text
x < y
```

#### **Exemples**

```text
3 < 4 // true
```

### **Opérateur inférieur ou égal à (<=)**

L'opérateur inférieur ou égal à retourne vrai si l'opérande de gauche est inférieur ou égal à celui de droite.

#### **Syntaxe**

```text
x <= y
```

#### **Exemples**

```text
3 <= 4 // true
```

## **Exemple de validation de formulaire JavaScript**

La validation de formulaire se faisait autrefois sur le serveur, après que le client avait entré toutes les données nécessaires et avait ensuite appuyé sur le bouton Soumettre. Si les données entrées par un client étaient incorrectes ou simplement manquantes, le serveur devait renvoyer toutes les données au client et demander que le formulaire soit renvoyé avec les informations correctes. C'était un processus vraiment long qui mettait beaucoup de charge sur le serveur.

JavaScript fournit un moyen de valider les données du formulaire sur l'ordinateur du client avant de les envoyer au serveur web. La validation de formulaire effectue généralement deux fonctions :

### **Validation de base**

Tout d'abord, le formulaire doit être vérifié pour s'assurer que tous les champs obligatoires sont remplis. Il suffit de parcourir chaque champ du formulaire pour vérifier les données.

### **Validation du format des données**

Deuxièmement, les données entrées doivent être vérifiées pour leur forme et leur valeur correctes. Votre code doit inclure une logique appropriée pour tester l'exactitude des données.

#### **Exemple :**

```html
<html>
   
   <head>
      <title>Validation de formulaire</title>
      
      <script type="text/javascript">
         <!--
            // Le code de validation du formulaire viendra ici.
         //-->
      </script>
      
   </head>
   
   <body>
      <form action="/cgi-bin/test.cgi" name="myForm" onsubmit="return(validate());">
         <table cellspacing="2" cellpadding="2" border="1">
            
            <tr>
               <td align="right">Nom</td>
               <td><input type="text" name="Name" /></td>
            </tr>
            
            <tr>
               <td align="right">EMail</td>
               <td><input type="text" name="EMail" /></td>
            </tr>
            
            <tr>
               <td align="right">Code postal</td>
               <td><input type="text" name="Zip" /></td>
            </tr>
            
            <tr>
               <td align="right">Pays</td>
               <td>
                  <select name="Country">
                     <option value="-1" selected>[choisissez le vôtre]</option>
                     <option value="1">USA</option>
                     <option value="2">UK</option>
                     <option value="3">INDE</option>
                  </select>
               </td>
            </tr>
            
            <tr>
               <td align="right"></td>
               <td><input type="submit" value="Submit" /></td>
            </tr>
            
         </table>
      </form>
      
   </body>
</html>
```

#### **Sortie**

Jetez un œil [ici](https://liveweave.com/LP9eOP).

### **Validation de formulaire de base**

Commençons par voir comment faire une validation de formulaire de base. Dans le formulaire ci-dessus, nous appelons validate() pour valider les données lorsque l'événement onsubmit se produit. Le code suivant montre l'implémentation de cette fonction `validate()`.

```html
<script type="text/javascript">
   // Le code de validation du formulaire viendra ici.
   function validate()
      {
      
         if( document.myForm.Name.value == "" )
         {
            alert( "Veuillez fournir votre nom !" );
            document.myForm.Name.focus() ;
            return false;
         }
         
         if( document.myForm.EMail.value == "" )
         {
            alert( "Veuillez fournir votre Email !" );
            document.myForm.EMail.focus() ;
            return false;
         }
         
         if( document.myForm.Zip.value == "" ||
         isNaN( document.myForm.Zip.value ) ||
         document.myForm.Zip.value.length != 5 )
         {
            alert( "Veuillez fournir un code postal au format #####." );
            document.myForm.Zip.focus() ;
            return false;
         }
         
         if( document.myForm.Country.value == "-1" )
         {
            alert( "Veuillez fournir votre pays !" );
            return false;
         }
         return( true );
      }
</script>
```

#### **Sortie**

Jetez un œil [ici](https://liveweave.com/pCPTnP).

### **Validation du format des données**

Maintenant, nous allons voir comment nous pouvons valider les données de notre formulaire saisies avant de les soumettre au serveur web.

L'exemple suivant montre comment valider une adresse e-mail saisie. Une adresse e-mail doit contenir au moins un signe '@' et un point (.). De plus, le '@' ne doit pas être le premier caractère de l'adresse e-mail, et le dernier point doit être au moins un caractère après le signe '@'.

#### **Exemple :**

```html
<script type="text/javascript">
    function validateEmail()
      {
         var emailID = document.myForm.EMail.value;
         atpos = emailID.indexOf("@");
         dotpos = emailID.lastIndexOf(".");
         
         if (atpos < 1 || ( dotpos - atpos < 2 )) 
         {
            alert("Veuillez entrer un identifiant de messagerie correct")
            document.myForm.EMail.focus() ;
            return false;
         }
         return( true );
      }
</script>
```

#### **Sortie**

Jetez un œil [ici](https://liveweave.com/nznVs6).

### **Contraintes de formulaire HTML5**

Certaines des contraintes HTML5 couramment utilisées pour `<input>` sont l'attribut `type` (par exemple, `type="password"`), `maxlength`, `required` et `disabled`. Une contrainte moins couramment utilisée est l'attribut `pattern` qui prend une expression régulière JavaScript.

## Exemple d'instruction if JavaScript

L'instruction `if` exécute une instruction si une condition spécifiée est `true`. Si la condition est `false`, une autre instruction peut être exécutée en utilisant l'instruction `else`.

**Note :** L'instruction `else` est facultative.

```javascript
if (condition)
    /* faire quelque chose */
else
    /* faire autre chose */
```

Plusieurs instructions `if...else` peuvent être enchaînées pour créer une clause `else if`. Cela spécifie une nouvelle condition à tester et peut être répété pour tester plusieurs conditions, en vérifiant jusqu'à ce qu'une instruction vraie soit présentée pour être exécutée.

```javascript
if (condition1)
    /* faire quelque chose */
else if (condition2)
    /* faire autre chose */
else if (condition3)
    /* faire autre chose */
else
    /* instruction finale */
```

**Note :** Si vous voulez exécuter plus d'une instruction dans la partie `if`, `else` ou `else if`, des accolades sont requises autour des instructions :

```javascript
if (condition) {
    /* faire */
    /* quelque chose */
    /* avec plusieurs instructions */
} else {
    /* faire quelque chose */
    /* else */
}
```

[Lien MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) | [Lien MSDN](https://msdn.microsoft.com/en-us/library/85yyde5c.aspx)

## **Exemples**

**Utilisation de** `if...else` :

```javascript
    // Si x=5 z=7 et q=42. Si x n'est pas 5 alors z=19.
    if (x == 5) {
      z = 7;
      q = 42
    else
      z = 19;
```

**Utilisation de** `else if` :

```javascript
if (x < 10)
    return "Petit nombre";
else if (x < 50)
    return "Nombre moyen";
else if (x < 100)
    return "Grand nombre";
else {
    flag = 1;
    return "Nombre invalide";
}
```

## Exemple de prototype JavaScript

JavaScript est un langage basé sur les prototypes, donc comprendre l'objet prototype est l'un des concepts les plus importants que les praticiens de JavaScript doivent connaître. 

Cette section vous donnera un bref aperçu de l'objet Prototype à travers divers exemples. Avant de lire cette partie, vous devrez avoir une compréhension de base de la [référence `this` en JavaScript](https://www.freecodecamp.org/news/the-complete-guide-to-this-in-javascript/).

### **Objet prototype**

Pour plus de clarté, examinons l'exemple suivant :

```javascript
function Point2D(x, y) {
  this.x = x;
  this.y = y;
}
```

Lorsque la fonction `Point2D` est déclarée, une propriété par défaut nommée `prototype` sera créée pour elle (notez que, en JavaScript, une fonction est aussi un objet). 

La propriété `prototype` est un objet qui contient une propriété `constructor` et sa valeur est la fonction `Point2D` : `Point2D.prototype.constructor = Point2D`. Et lorsque vous appelez `Point2D` avec le mot-clé `new`, _les objets nouvellement créés hériteront de toutes les propriétés de_ `Point2D.prototype`. 

Pour vérifier cela, vous pouvez ajouter une méthode nommée `move` dans `Point2D.prototype` comme suit :

```javascript
Point2D.prototype.move = function(dx, dy) {
  this.x += dx;
  this.y += dy;
}

var p1 = new Point2D(1, 2);
p1.move(3, 4);
console.log(p1.x); // 4
console.log(p1.y); // 6
```

Le `Point2D.prototype` est appelé **objet prototype** ou **prototype** de l'objet `p1` et pour tout autre objet créé avec la syntaxe `new Point2D(...)`. Vous pouvez ajouter plus de propriétés à l'objet `Point2D.prototype` comme vous le souhaitez. Le modèle courant est de déclarer des méthodes à `Point2D.prototype` et les autres propriétés seront déclarées dans la fonction constructeur.

Les objets intégrés en JavaScript sont construits de manière similaire. Par exemple :

* Le prototype des objets créés avec `new Object()` ou la syntaxe `{}` est `Object.prototype`.
* Le prototype des tableaux créés avec `new Array()` ou la syntaxe `[]` est `Array.prototype`.
* Et ainsi de suite avec d'autres objets intégrés tels que `Date` et `RegExp`.

`Object.prototype` est hérité par tous les objets et il n'a pas de prototype (son prototype est `null`).

### **Chaîne de prototypes**

Le mécanisme de la chaîne de prototypes est simple : lorsque vous accédez à une propriété `p` sur l'objet `obj`, le moteur JavaScript recherchera cette propriété à l'intérieur de l'objet `obj`. Si le moteur ne parvient pas à la trouver, il continue la recherche dans le prototype de l'objet `obj` et ainsi de suite jusqu'à atteindre `Object.prototype`. Si, après la fin de la recherche, rien n'a été trouvé, le résultat sera `undefined`. Par exemple :

```javascript
var obj1 = {
  a: 1,
  b: 2
};

var obj2 = Object.create(obj1);
obj2.a = 2;

console.log(obj2.a); // 2
console.log(obj2.b); // 2
console.log(obj2.c); // undefined
```

Dans l'extrait de code ci-dessus, l'instruction `var obj2 = Object.create(obj1)` créera l'objet `obj2` avec le prototype `obj1`. En d'autres termes, `obj1` devient le prototype de `obj2` au lieu de `Object.prototype` par défaut. Comme vous pouvez le voir, `b` n'est pas une propriété de `obj2` ; vous pouvez toujours y accéder via la chaîne de prototypes. Pour la propriété `c`, cependant, vous obtenez une valeur `undefined` car elle ne peut pas être trouvée dans `obj1` et `Object.prototype`.

### **Classes**

En ES2016, nous pouvons maintenant utiliser le mot-clé `Class` ainsi que les méthodes mentionnées ci-dessus pour manipuler `prototype`. La `Class` JavaScript plaît aux développeurs issus de milieux OOP, mais elle fait essentiellement la même chose que ci-dessus.

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height
    this.width = width
  }

  get area() {
    return this.calcArea()
  }

  calcArea() {
    return this.height * this.width
  }
}

const square = new Rectangle(10, 10)

console.log(square.area) // 100
```

Cela revient essentiellement à :

```javascript
function Rectangle(height, width) {
  this.height = height
  this.width = width
}

Rectangle.prototype.calcArea = function calcArea() {
  return this.height * this.width
}
```

Les méthodes `getter` et `setter` dans les classes lient une propriété d'objet à une fonction qui sera appelée lorsque cette propriété est recherchée. Ce n'est qu'un sucre syntaxique pour faciliter la recherche ou la définition de propriétés.

## Exemple de portée JavaScript

Si vous avez programmé en JavaScript pendant un certain temps, vous avez sans doute rencontré un concept connu sous le nom de `scope`. Qu'est-ce que `scope` ? Pourquoi devriez-vous prendre le temps de l'apprendre ?

En termes de programmeur, `scope` est le **contexte d'exécution actuel**. Confus ? Regardons le morceau de code suivant :

```text
var foo = 'Salut, je suis foo !';

var baz = function () {
  var bar = 'Salut, je suis bar aussi !';
    console.log(foo);
}

baz(); // Salut, je suis foo !
console.log(bar); // ReferenceError...
```

C'est un exemple simple, mais il illustre bien ce que l'on appelle la _portée lexicale_. JavaScript, et presque tous les autres langages de programmation, ont une _portée lexicale_. Il existe un autre type de portée connu sous le nom de _portée dynamique_, mais nous n'en discuterons pas.

Maintenant, le terme _portée lexicale_ semble sophistiqué, mais comme vous le verrez, il est en réalité très simple en principe. Dans une portée lexicale, il existe deux types de portées : la _portée globale_ et une _portée locale_.

Avant que vous ne tapiez la première ligne de code dans votre programme, une _portée globale_ est créée pour vous. Cela contient toutes les variables que vous déclarez dans votre programme **en dehors de toute fonction**.

Dans l'exemple ci-dessus, la variable `foo` est dans la portée globale du programme, tandis que la variable `bar` est déclarée à l'intérieur d'une fonction et est donc **dans la portée locale de cette fonction**.

Décortiquons l'exemple ligne par ligne. Bien que vous puissiez être confus à ce stade, je vous promets que vous aurez une bien meilleure compréhension d'ici la fin de votre lecture.

À la ligne 1, nous déclarons la variable `foo`. Rien de trop sophistiqué ici. Appelons cela une référence côté gauche (LHS) à `foo`, car nous attribuons une valeur à `foo` et elle est du côté gauche du signe `égal`.

À la ligne 3, nous déclarons une fonction et l'attribuons à la variable `baz`. C'est une autre référence LHS à `baz`. Nous attribuons une valeur à celle-ci (rappelons-nous, les fonctions sont aussi des valeurs !). Cette fonction est ensuite appelée à la ligne 8. C'est une référence RHS, ou une référence côté droit à `baz`. Nous récupérons la valeur de `baz`, qui dans ce cas est une fonction, puis nous l'invoquons. 

Une autre référence RHS à `baz` serait si nous attribuions sa valeur à une autre variable, par exemple `foo = baz`. Ce serait une référence LHS à `foo` et une référence RHS à `baz`.

Les références LHS et RHS peuvent sembler confuses, mais elles sont importantes pour discuter de la portée. Pensez-y de cette manière : une référence LHS attribue une valeur à la variable, tandis qu'une référence RHS récupère la valeur de la variable. Ce sont simplement des moyens plus courts et plus pratiques de dire 'récupérer la valeur' et 'attribuer une valeur'.

Décortiquons maintenant ce qui se passe à l'intérieur de la fonction elle-même.

Lorsque le compilateur compile le code à l'intérieur d'une fonction, il entre dans la **portée locale** de la fonction.

À la ligne 4, la variable `bar` est déclarée. C'est une référence LHS à `bar`. À la ligne suivante, nous avons une référence RHS à `foo` à l'intérieur de `console.log()`. Rappelez-vous, nous récupérons la valeur de `foo` puis la passons comme argument à la méthode `console.log()`.

Lorsque nous avons une référence RHS à `foo`, le compilateur recherche la déclaration de la variable `foo`. Le compilateur ne la trouve pas dans la fonction elle-même, ou dans la **portée locale de la fonction**, donc il **monte d'un niveau : à la portée globale**.

À ce stade, vous pensez probablement que la portée a quelque chose à voir avec les variables. C'est correct. Une portée peut être considérée comme un conteneur pour les variables. Toutes les variables créées dans une portée locale ne sont accessibles que dans cette portée locale. Cependant, toutes les portées locales peuvent accéder à la portée globale. (Je sais que vous êtes probablement encore plus confus maintenant, mais restez avec moi pour quelques paragraphes de plus).

Donc, le compilateur monte à la portée globale pour trouver une référence LHS à la variable `foo`. Il en trouve une à la ligne 1, donc il récupère la valeur de la référence LHS, qui est une chaîne : `'Salut, je suis foo !'`. Cette chaîne est envoyée à la méthode `console.log()`, et affichée dans la console.

Le compilateur a terminé l'exécution du code à l'intérieur de la fonction, donc nous revenons à la ligne 9. À la ligne 9, nous avons une référence RHS pour la variable `bar`.

Maintenant, `bar` a été déclarée dans la portée locale de `baz`, mais il y a une référence RHS pour `bar` dans la portée globale. Puisqu'il n'y a pas de référence LHS pour `bar` dans la portée globale, le compilateur ne peut pas trouver de valeur pour `bar` et lance une ReferenceError.

Mais, vous pourriez demander, si la fonction peut chercher à l'extérieur d'elle-même pour les variables, ou si une portée locale peut jeter un coup d'œil dans la portée globale pour trouver des références LHS, pourquoi la portée globale ne peut-elle pas jeter un coup d'œil dans une portée locale ? Eh bien, c'est ainsi que fonctionne la portée lexicale !

```text
... // portée globale
var baz = function() {
  ... // portée de baz
}
... /// portée globale
```

C'est le même code que ci-dessus qui illustre la portée. Cela forme une sorte de hiérarchie qui remonte à la portée globale :

`baz -> global`.

Donc, si une référence RHS pour une variable à l'intérieur de la portée de `baz` peut être satisfaite par une référence LHS pour cette variable dans la portée globale. Mais l'inverse n'est **pas vrai**.

Et si nous avions une autre fonction à l'intérieur de `baz` ?

```text
... // portée globale
var baz = function() {
  ... // portée de baz

  var bar = function() {
     ... // portée de bar.
  }

}
... /// portée globale
```

Dans ce cas, la hiérarchie ou la **chaîne de portée** ressemblerait à ceci :

`bar -> baz -> global`

Toute référence RHS à l'intérieur de la portée locale de `bar` peut être satisfaite par des références LHS dans la portée globale ou la portée de `baz`, mais une référence RHS dans la portée de `baz` ne peut pas être satisfaite par une référence LHS dans la portée de `bar`.

**Vous ne pouvez parcourir une chaîne de portée que vers le bas, pas vers le haut.**

Il y a deux autres choses importantes que vous devez savoir sur les portées JavaScript.

1. Les portées sont déclarées par des fonctions, pas par des blocs.
2. Les fonctions peuvent être référencées vers l'avant, les variables ne le peuvent pas.

Observez (chaque commentaire décrit la portée à la ligne où il est écrit) :

```text
    // outer() est dans la portée ici car les fonctions peuvent être référencées vers l'avant
    
    function outer() {
    
        // seulement inner() est dans la portée ici
        // car seules les fonctions sont référencées vers l'avant
    
        var a = 1;
        
        // maintenant 'a' et inner() sont dans la portée
        
        function inner() {
            var b = 2
            
            if (a == 1) {
                var c = 3;
            }
            
            // 'c' est toujours dans la portée car JavaScript ne se soucie pas
            // de la fin du bloc 'if', seulement de la fonction inner()
        }
        
        // maintenant b et c sont hors de portée
        // a et inner() sont toujours dans la portée
        
    }
    
    // ici, seulement outer() est dans la portée
```

## Exemple de boucle For JavaScript

### **Syntaxe**

```javascript
for ([initialisation]); [condition]; [expression-finale]) {
   // instruction
}
```

L'instruction `for` de JavaScript se compose de trois expressions et d'une instruction :

* initialisation - Exécutée avant la première exécution de la boucle. Cette expression est couramment utilisée pour créer des compteurs. Les variables créées ici sont limitées à la boucle. Une fois que la boucle a terminé son exécution, elles sont détruites.
* condition - Expression qui est vérifiée avant l'exécution de chaque itération. Si elle est omise, cette expression est évaluée à true. Si elle est évaluée à true, l'instruction de la boucle est exécutée. Si elle est évaluée à false, la boucle s'arrête.
* expression-finale - Expression qui est exécutée après chaque itération. Généralement utilisée pour incrémenter un compteur. Mais elle peut aussi être utilisée pour décrémenter un compteur.
* instruction - Code à répéter dans la boucle

Chacune de ces trois expressions ou l'instruction peut être omise. Les boucles for sont couramment utilisées pour compter un certain nombre d'itérations afin de répéter une instruction. Utilisez une instruction `break` pour sortir de la boucle avant que l'expression de condition ne soit évaluée à false.

## **Pièges courants**

**Dépassement des limites d'un tableau**

Lors de l'indexation sur un tableau à plusieurs reprises, il est facile de dépasser les limites du tableau (ex. essayer de référencer le 4ème élément d'un tableau de 3 éléments).

```javascript
    // Cela provoquera une erreur.
    // Les limites du tableau seront dépassées.
    var arr = [ 1, 2, 3 ];
    for (var i = 0; i <= arr.length; i++) {
       console.log(arr[i]);
    }

    output:
    1
    2
    3
    undefined
```

Il y a deux façons de corriger ce code. Définissez la condition soit sur `i < arr.length` soit sur `i <= arr.length - 1`

### **Exemples**

Itérer à travers les entiers de 0 à 8

```javascript
for (var i = 0; i < 9; i++) {
   console.log(i);
}

output:
0
1
2
3
4
5
6
7
8
```

Sortir d'une boucle avant que l'expression de condition ne soit fausse

```javascript
for (var elephant = 1; elephant < 10; elephant+=2) {
    if (elephant === 7) {
        break;
    }
    console.info('elephant is ' + elephant);
}

output:
elephant is 1
elephant is 3
elephant is 5
```

## Exemple d'instruction Break JavaScript

L'instruction **break** termine la boucle, l'instruction `switch` ou l'instruction `label` en cours et transfère le contrôle du programme à l'instruction suivant l'instruction terminée.

```text
break;
```

Si l'instruction **break** est utilisée dans une instruction étiquetée, la syntaxe est la suivante :

```text
break labelName;
```

## **Exemples**

La fonction suivante a une instruction **break** qui termine la boucle `while` lorsque **i** est 3, puis retourne la valeur **3 * x**.

```text
function testBreak(x) {
  var i = 0;

  while (i < 6) {
    if (i == 3) {
      break;
    }
    i += 1;
  }

  return i * x;
}
```

Dans l'exemple suivant, le compteur est configuré pour compter de 1 à 99 ; cependant, l'instruction **break** termine la boucle après 14 comptes.

```text
for (var i = 1; i < 100; i++) {
  if (i == 15) {
    break;
  }
}
```

## Exemple de boucle do while JavaScript

La boucle `do...while` est étroitement liée à la boucle [`while`](http://forum.freecodecamp.com/t/javascript-while-loop/14668). Dans la boucle do while, la condition est vérifiée à la fin de la boucle.

Voici la **syntaxe** pour la boucle `do...while` :

## **Syntaxe :**

```text
 do {

   *Instruction(s);*

} while (*condition*);
```

**instruction(s) :** Une instruction qui est exécutée **au moins une fois** avant que la condition ou l'expression booléenne ne soit évaluée et est réexécutée chaque fois que la condition est évaluée à true.

**condition :** Ici, une condition est une [expression booléenne](https://www.freecodecamp.org/news/boolean-definition/). Si l'expression booléenne est évaluée à true, l'instruction est exécutée à nouveau. Lorsque l'expression booléenne est évaluée à false, la boucle se termine.

## **Exemple :**

```text
var i = 0;
do {
  i = i + 1;
  console.log(i);
} while (i < 5);

Sortie:
1
2
3
4
5
```

## Exemple de boucle For In JavaScript

L'instruction `for...in` itère sur les propriétés énumérables d'un objet, dans un ordre arbitraire. Pour chaque propriété distincte, des instructions peuvent être exécutées.

```text
for (variable in object) {
...
}
```

Obligatoire/FacultatifParamètreDescriptionObligatoireVariable: Un nom de propriété différent est assigné à la variable à chaque itération. FacultatifObject: un objet dont les propriétés énumérables sont itérées.

## **Exemples**

```text
// Initialiser l'objet.
a = { "a": "Athens", "b": "Belgrade", "c": "Cairo" }

// Itérer sur les propriétés.
var s = ""
for (var key in a) {
    s += key + ": " + a[key];
    s += "<br />";
    }
document.write (s);

// Sortie:
// a: Athens
// b: Belgrade
// c: Cairo

// Initialiser le tableau.
var arr = new Array("zero", "one", "two");

// Ajouter quelques propriétés expando au tableau.
arr["orange"] = "fruit";
arr["carrot"] = "vegetable";

// Itérer sur les propriétés et les éléments.
var s = "";
for (var key in arr) {
    s += key + ": " + arr[key];
    s += "<br />";
}

document.write (s);

// Sortie:
//   0: zero
//   1: one
//   2: two
//   orange: fruit
//   carrot: vegetable

// Méthode efficace pour obtenir les clés d'un objet en utilisant une expression dans les conditions de la boucle for-in
var myObj = {a: 1, b: 2, c:3}, myKeys = [], i=0;
for (myKeys[i++] in myObj);

document.write(myKeys);

//Sortie:
//   a
//   b
//   c
```

## Exemple de boucle For Of JavaScript

L'instruction `for...of` crée une boucle itérant sur des objets itérables (y compris Array, Map, Set, Arguments object et ainsi de suite), invoquant un crochet d'itération personnalisé avec des instructions à exécuter pour la valeur de chaque propriété distincte.

```javascript
    for (variable of object) {
        statement
    }
```

Description variable: À chaque itération, une valeur d'une propriété différente est assignée à la variable.object Object dont les propriétés énumérables sont itérées.

## **Exemples**

### **Array**

```javascript
    let arr = [ "fred", "tom", "bob" ];

    for (let i of arr) {
        console.log(i);
    }

    // Output:
    // fred
    // tom
    // bob
```

### **Map**

```javascript
    var m = new Map();
    m.set(1, "black");
    m.set(2, "red");

    for (var n of m) {
        console.log(n);
    }

    // Output:
    // 1,black
    // 2,red
```

### **Set**

```javascript
    var s = new Set();
    s.add(1);
    s.add("red");

    for (var n of s) {
        console.log(n);
    }

    // Output:
    // 1
    // red
```

### **Arguments object**

```javascript
    // votre navigateur doit supporter la boucle for..of
    // et les variables let-scoped dans les boucles for

    function displayArgumentsObject() {
        for (let n of arguments) {
            console.log(n);
        }
    }


    displayArgumentsObject(1, 'red');

    // Output:
    // 1
    // red
```

## Exemple de boucle While JavaScript

La boucle while commence par évaluer la condition. Si la condition est vraie, l'instruction (ou les instructions) est/sont exécutée(s). Si la condition est fausse, l'instruction (ou les instructions) n'est/sont pas exécutée(s). Après cela, la boucle while se termine.

Voici la **syntaxe** de la boucle while :

## **Syntaxe :**

```text
while (condition)

{

  statement(s);

}
```

_statement(s) :_ Une instruction qui est exécutée tant que la condition est évaluée à true.

_condition :_ Ici, la condition est une expression booléenne qui est évaluée avant chaque passage dans la boucle. Si cette condition est évaluée à true, statement(s) est/sont exécutée(s). Lorsque la condition est évaluée à false, l'exécution se poursuit avec l'instruction après la boucle while.

## **Exemple :**

```text
    var i = 1;
    while (i < 10) 
    {
      console.log(i);
       i++; // i=i+1 même chose
    }

    Output:
    1 
    2 
    3 
    4
    5
    6
    7
    8
    9
```