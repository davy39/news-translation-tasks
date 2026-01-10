---
title: Les Fermetures en JavaScript Expliquées avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-18T23:14:00.000Z'
originalURL: https://freecodecamp.org/news/closures-in-javascript-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c82740569d1a4ca32a5.jpg
tags:
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Les Fermetures en JavaScript Expliquées avec des Exemples
seo_desc: 'What are Closures?

  A closure is the combination of a function and the lexical environment (scope) within
  which that function was declared. Closures are a fundamental and powerful property
  of Javascript. This article discusses the ‘how’ and ‘why’ abou...'
---

# **Qu'est-ce que les Fermetures ?**

Une fermeture (closure) est la combinaison d'une fonction et de l'environnement lexical (portée) dans lequel cette fonction a été déclarée. Les fermetures sont une propriété fondamentale et puissante de JavaScript. Cet article discute du "comment" et du "pourquoi" des fermetures :

### **Exemple**

```js
// nous avons une fonction externe nommée walk et une fonction interne nommée fly

function walk() {

  var dist = '1780 feet';

  function fly() {
    console.log('At ' + dist);
  }

  return fly;
}

var flyFunc = walk(); // appeler walk retourne la fonction fly qui est assignée à flyFunc
// vous pourriez penser que une fois la fonction walk exécutée
// vous pourriez penser que JavaScript a supprimé la variable 'dist'

flyFunc(); // Affiche 'At 1780 feet'
// mais vous pouvez toujours utiliser la fonction comme ci-dessus
// c'est la puissance des fermetures
```

### **Un Autre Exemple**

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

La fermeture "se souvient" de l'environnement dans lequel elle a été créée. Cet environnement consiste en toutes les variables locales qui étaient dans la portée au moment où la fermeture a été créée.

```js
function outside(num) {
  var rememberedVar = num; // Dans cet exemple, rememberedVar est l'environnement lexical que la fermeture "se souvient"
  return function inside() { // C'est la fonction que la fermeture "se souvient"
    console.log(rememberedVar)
  }
}

var remember1 = outside(7); // remember1 est maintenant une fermeture qui contient rememberedVar = 7 dans son environnement lexical, et // la fonction 'inside'
var remember2 = outside(9); // remember2 est maintenant une fermeture qui contient rememberedVar = 9 dans son environnement lexical, et // la fonction 'inside'

remember1(); // Cela exécute maintenant la fonction 'inside' qui console.log(rememberedVar) => 7
remember2(); // Cela exécute maintenant la fonction 'inside' qui console.log(rememberedVar) => 9
```

Les fermetures sont utiles car elles vous permettent de "vous souvenir" de données et ensuite de manipuler ces données à travers des fonctions retournées. Cela permet à JavaScript d'émuler des méthodes privées que l'on trouve dans d'autres langages de programmation. Les méthodes privées sont utiles pour restreindre l'accès au code ainsi que pour gérer votre espace de noms global.

## Variables et méthodes privées

Les fermetures peuvent également être utilisées pour encapsuler des données/méthodes privées. Regardez cet exemple :

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

Dans cet exemple, nous ne pourrons pas accéder à `balance` depuis l'extérieur de la fonction `bankAccount`, ce qui signifie que nous avons créé une variable privée. Où est la fermeture ? Eh bien, réfléchissez à ce que `bankAccount()` retourne. Elle retourne en fait un objet avec un ensemble de fonctions à l'intérieur, et pourtant, lorsque nous appelons `account.getBalance()`, la fonction est capable de "se souvenir" de sa référence initiale à `balance`. C'est la puissance de la fermeture, où une fonction "se souvient" de sa portée lexicale (portée de compilation), même lorsque la fonction est exécutée en dehors de cette portée lexicale.

### Émuler des variables à portée de bloc.

JavaScript n'avait pas de concept de variables à portée de bloc. Cela signifie que lors de la définition d'une variable à l'intérieur d'une boucle for, par exemple, cette variable est visible depuis l'extérieur de la boucle for également. Alors, comment les fermetures peuvent-elles nous aider à résoudre ce problème ? Regardons cela.

```javascript
    var funcs = [];
    
    for(var i = 0; i < 3; i++){
        funcs[i] = function(){
            console.log('My value is ' + i);  // création de trois fonctions différentes avec différentes valeurs de paramètre.
        }
    }
    
    for(var j = 0; j < 3; j++){
        funcs[j]();             // My value is 3
                                // My value is 3
                                // My value is 3
    }
```

Puisque la variable i n'a pas de portée de bloc, sa valeur dans les trois fonctions a été mise à jour avec le compteur de boucle et a créé des valeurs erronées. Les fermetures peuvent nous aider à résoudre ce problème en créant une capture de l'environnement dans lequel la fonction se trouvait lorsqu'elle a été créée, préservant ainsi son état.

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

Les versions récentes de JavaScript ES6+ ont un nouveau mot-clé appelé let qui peut être utilisé pour donner à la variable une portée de bloc. Il existe également de nombreuses fonctions (forEach) et des bibliothèques entières (lodash.js) qui sont dédiées à résoudre de tels problèmes comme ceux expliqués ci-dessus. Elles peuvent certainement augmenter votre productivité, cependant, il reste extrêmement important d'avoir des connaissances sur tous ces problèmes lorsque vous essayez de créer quelque chose de grand.

Les fermetures ont de nombreuses applications spéciales qui sont utiles lors de la création de grands programmes JavaScript.

1. Émuler des variables privées ou l'encapsulation
2. Faire des appels asynchrones côté serveur
3. Créer une variable à portée de bloc.

### Émuler des variables privées.

Contrairement à de nombreux autres langages, JavaScript ne dispose pas d'un mécanisme qui vous permet de créer des variables d'instance encapsulées dans un objet. Avoir des variables d'instance publiques peut causer beaucoup de problèmes lors de la création de programmes de taille moyenne à grande. Cependant, avec les fermetures, ce problème peut être atténué.

Comme dans l'exemple précédent, vous pouvez créer des fonctions qui retournent des littéraux d'objet avec des méthodes qui ont accès aux variables locales de l'objet sans les exposer. Ainsi, les rendant effectivement privées.

Les fermetures peuvent également vous aider à gérer votre espace de noms global pour éviter les collisions avec des données partagées globalement. Habituellement, toutes les variables globales sont partagées entre tous les scripts de votre projet, ce qui vous causera certainement beaucoup de problèmes lors de la création de programmes de taille moyenne à grande. C'est pourquoi les auteurs de bibliothèques et de modules utilisent des fermetures pour masquer les méthodes et les données d'un module entier. Cela s'appelle le modèle de module, il utilise une expression de fonction immédiatement invoquée qui exporte uniquement certaines fonctionnalités vers le monde extérieur, réduisant ainsi considérablement le nombre de références globales.

Voici un court exemple de squelette de module.

```javascript
var myModule = (function() {
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

Les fermetures sont utiles pour capturer de nouvelles instances de variables privées contenues dans l'environnement "souvenu", et ces variables ne peuvent être accessibles que par la fonction ou les méthodes retournées.

## Vecteurs

Un vecteur est peut-être le type de collection le plus simple en Clojure. Vous pouvez le considérer comme un tableau en JavaScript. Définissons un vecteur simple :

```text
def a-vector [1 2 3 4 5]
;; Alternativement, utilisez la fonction vector:
def another-vector (vector 1 2 3 4 5)
;; Vous pouvez utiliser des virgules pour séparer les éléments, puisque Clojure les traite comme des espaces.
def comma-vector [1, 2, 3, 4, 5]
```

Vous verrez qu'il utilise des crochets, tout comme un tableau en JS. Puisque Clojure, comme JS, est typé dynamiquement, les vecteurs peuvent contenir des éléments de n'importe quel type, y compris d'autres vecteurs.

```text
def mixed-type-vector [1 "foo" :bar ["spam" 22] #"^baz$"]
```

### Ajouter des éléments à un vecteur

Vous pouvez ajouter des éléments à un vecteur en utilisant `conj`. Vous pouvez également préfixer une liste en utilisant `into`, mais notez que `into` est destiné à fusionner deux vecteurs, donc ses deux arguments doivent être des vecteurs, et l'utilisation de `into` est plus lente que l'utilisation de `conj`.

```text
(time (conj [1 2] 3))
; => "Elapsed time: 0.032206 msecs"
;    [1 2 3]
(time (into [1] [2 3]))
; => "Elapsed time: 0.078499 msecs"
;    [1 2 3]
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[IDEOne it!](https://ideone.com/wBSUEd)

### Récupérer des éléments d'un vecteur

Vous pouvez récupérer des éléments d'un vecteur en utilisant `get`. Cela équivaut à utiliser la notation entre crochets pour accéder aux éléments d'un tableau dans de nombreux langages impératifs. Les éléments d'un vecteur sont indexés à partir de 0, en comptant à partir de la gauche.

```text
var arr = [1, 2, 3, 4, 5];
arr[0];
// => 1
```

En Clojure, cela s'écrirait comme suit :

```text
def a-vector [1 2 3 4 5]
(get a-vector 0)
; => 1
```

Vous pouvez également donner à `get` une valeur par défaut, si vous lui donnez un index qui n'est pas dans le tableau.

```text
;; la liste n'a pas 2147483647 éléments, donc elle retournera une chaîne à la place.
(get a-vector 2147483646 "sorry, not found!")
; => "sorry, not found!"
```

### Convertir d'autres collections en vecteurs

Les structures de données non vectorielles peuvent être converties en vecteurs en utilisant la fonction `vec`. Avec les tables de hachage, cela produit un vecteur 2D contenant des paires de clés et de valeurs.

```text
(vec '(1 2 3 4 5))
; => [1 2 3 4 5]
(vec {:jack "black" :barry "white"})
; => [[:jack "black"] [:barry "white"]]
```

### Quand utiliser un vecteur ?

Un vecteur doit être utilisé dans presque tous les cas si vous avez besoin d'une collection, car ils ont les temps d'accès aléatoires les plus courts, ce qui facilite la récupération d'éléments d'un vecteur. Notez que les vecteurs sont ordonnés. Si l'ordre n'a pas d'importance, il peut être préférable d'utiliser un ensemble. Notez également que les vecteurs sont conçus pour ajouter des éléments ; si vous devez préfixer des éléments, vous pourriez vouloir utiliser une liste.

## Plus d'informations sur les Fermetures :

* [Apprendre les fermetures JavaScript en six minutes](https://www.freecodecamp.org/news/learn-javascript-closures-in-n-minutes/)
* [Un guide de base sur les fermetures en JavaScript](https://www.freecodecamp.org/news/a-basic-guide-to-closures-in-javascript-9fc8b7e3463e/)
* [Découvrez la puissance des fermetures dans VueJS](https://www.freecodecamp.org/news/closures-vuejs-higher-order-functions-emojipicker-f10d3c249a12/)
* [Les fermetures JavaScript expliquées en envoyant un colis](https://www.freecodecamp.org/news/javascript-closures-explained-by-mailing-a-package-4f23e9885039/)