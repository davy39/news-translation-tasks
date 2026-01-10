---
title: Le guide de préparation aux entretiens JavaScript – Sujets essentiels à connaître
  + Exemples de code
date: '2024-05-22T09:58:22.000Z'
author: Kunal Nalawade
authorURL: https://www.freecodecamp.org/news/author/kunal-nalawade-25/
originalURL: https://freecodecamp.org/news/js-interview-prep-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/JavaScript-Interview-Prep-Cover.png
tags:
- name: handbook
  slug: handbook
- name: JavaScript
  slug: javascript
seo_desc: 'JavaScript is a widely used language in web development and powers interactive
  features of virtually every website out there. JavaScript makes it possible to create
  dynamic web pages and is very versatile.

  JavaScript remains one of the most in-demand...'
---


JavaScript est un langage largement utilisé dans le développement web et alimente les fonctionnalités interactives de pratiquement tous les sites web actuels. JavaScript permet de créer des pages web dynamiques et s'avère très polyvalent.

<!-- more -->

JavaScript reste l'un des langages de programmation les plus demandés en 2024. De nombreuses entreprises recherchent une maîtrise de JavaScript et de l'un de ses frameworks comme Angular ou React. Si vous êtes un développeur web en herbe, comprendre ce que ces entreprises recherchent lors des entretiens est la clé pour débloquer de grandes opportunités.

Dans ce manuel, je vais approfondir plusieurs concepts essentiels de JavaScript que vous devez préparer avant de vous rendre à un entretien. Équipé des fondamentaux et des concepts suivants, vous vous positionnerez comme un candidat impressionnant dans le paysage du développement web.

## Table des matières

-   [Comment utiliser les mots-clés `var`, `let` et `const`.][1]
-   [Qu'est-ce que le Hoisting ?][2]
-   [Comment fonctionnent les closures ?][3]
-   [Comment implémenter le Debouncing.][4]
-   [Comment implémenter le Throttling.][5]
-   [Qu'est-ce que le Currying ?][6]
-   [Quelle est la différence entre `==` et `===` ?][7]
-   [Comment fonctionne le mot-clé `this` ?][8]
-   [Comment utiliser les méthodes `call`, `apply` et `bind`.][9]
-   [Que sont les prototypes et l'héritage prototypal ?][10]
-   [Comment utiliser l'opérateur Spread.][11]
-   [Comment fonctionne la déstructuration de tableaux et d'objets ?][12]
-   [Que sont les Promises ?][13]
-   [Comment utiliser les mots-clés `async` et `await`.][14]
-   [Qu'est-ce qu'une Event Loop ?][15]
-   [Comment fonctionne la propagation d'événements – Bubbling et Capturing.][16]
-   [Que sont les fonctions génératrices ?][17]
-   [Comment implémenter des polyfills pour `Array.map()`, `Array.reduce()` et `Array.filter()`][18]
-   [Réflexions supplémentaires][19]

## Comment utiliser les mots-clés `var`, `let` et `const`

En JavaScript, vous pouvez déclarer une variable de trois manières : en utilisant `var`, `let` et `const`. Il est essentiel de comprendre la différence entre ces trois-là.

Une variable `var` a une portée (scope) globale et au niveau de la fonction. Si la variable est déclarée globalement, elle est accessible partout, et si elle est déclarée à l'intérieur d'une fonction, elle est accessible partout dans cette fonction.

```javascript
var a=5
function fun() {
    var b=4
}

console.log(a) // 5
console.log(b) // throws ReferenceError
```

Une variable `let` a une portée au niveau du bloc. Cette variable, si elle est déclarée à l'intérieur d'un bloc, ne peut pas être consultée à l'extérieur de celui-ci. Par exemple :

```javascript
var a = 5;
if (a > 1) {
    var b = 6;
    let c = 7;
}
console.log(a); // prints 5
console.log(b); // prints 6
console.log(c); // throws ReferenceError
```

Ici, les variables `a` et `b` ont une portée globale, elles peuvent donc être consultées n'importe où. La variable `c` ne peut pas être consultée en dehors du bloc `if` car `let` n'a qu'une portée de niveau bloc.

`const` est utilisé pour déclarer une constante. Une fois qu'une variable est déclarée avec `const`, elle ne peut plus être modifiée.

```javascript
const x = 5;
x = 6; // Throws an error
```

Cependant, vous pouvez modifier les propriétés d'un objet ou les éléments d'un tableau.

```javascript
const obj = { name: 'kunal', age: 21 };
obj.name = 'alex';
console.log(obj); // { name: 'alex', age: 21 }

const arr = [1, 2, 3];
arr[1] = 4;
console.log(arr); // [ 1, 4, 3 ]
```

## Qu'est-ce que le Hoisting ?

Le Hoisting (remontée) fait référence au comportement par défaut de JavaScript qui déplace toutes les déclarations de variables et de fonctions vers le haut. Cela signifie que vous pouvez les utiliser avant qu'elles ne soient déclarées.

```javascript
x=5 
console.log(x) // prints 5 
var x               
```

Dans le code ci-dessus, JavaScript a déplacé la déclaration de la variable en haut du bloc de code. C'est-à-dire : c'est similaire à la déclaration de `x` à la première ligne.

Dans le cas des fonctions, les déclarations sont également déplacées vers le haut :

```javascript
function foo() {
    console.log("foo called");
}

foo(); // foo called
```

Cependant, cela ne fonctionne pas avec `let` et `const`.

```javascript
x = 5; // throws ReferenceError
let x;

fiz(); // throws ReferenceError
const fiz = () => { console.log("fiz called") };
```

## Comment fonctionnent les closures ?

Les closures (fermetures) sont un concept important en JavaScript. Lorsque vous avez une fonction à l'intérieur d'une autre fonction, la fonction interne a accès à toutes les variables de la fonction externe.

Mais lorsque cette fonction interne est renvoyée par la fonction externe, la fonction interne peut être appelée n'importe où en dehors de la fonction externe et elle peut toujours accéder à ces variables.

```javascript
function fun() {
    let count = 0;
    return () => {
        count++;
        console.log(count);
    };
}

const innerFun = fun();
innerFun(); // prints 1
innerFun(); // prints 2
innerFun(); // prints 3
```

Ici, `fun()` déclare et initialise une variable `count`. Ensuite, elle renvoie une fonction interne qui incrémente `count` avant de l'afficher. Maintenant, lorsque vous appelez `innerFun()` n'importe où en dehors de la méthode `fun()`, elle peut toujours accéder à `count` et l'incrémenter.

C'est le concept de closures. Vous pouvez en apprendre davantage sur les closures dans l'article suivant de [Matías Hernández][20].

[

Comment utiliser les closures en JavaScript – Guide pour débutants

Les closures sont un concept JavaScript déroutant à apprendre, car il est difficile de voir comment elles sont réellement utilisées. Contrairement à d'autres concepts tels que les fonctions, les variables et les objets, vous n'utilisez pas toujours les closures consciemment et directement...

![favicon](https://cdn.freecodecamp.org/universal/favicons/favicon.ico)Matías HernándezfreeCodeCamp.org

![English-Header-4](https://www.freecodecamp.org/news/content/images/2021/01/English-Header-4.png)

][21]

## Comment implémenter le Debouncing

Le debouncing est une technique qui retarde l'appel d'une fonction de quelques secondes et garantit qu'il y a toujours un délai entre l'appel de la fonction et son exécution.

Lorsque vous appelez une fonction, elle est exécutée après un délai. Cependant, si vous appelez à nouveau la fonction pendant ce délai, l'appel précédent est annulé et un nouveau minuteur est lancé. Le même processus se répète pour chaque appel de fonction ultérieur.

Voyons comment l'implémenter :

```javascript
function debounce(func, delay) {
    let timeout = null;
    return (...args) => {
        if (timeout) clearTimeout(timeout);
        timeout = setTimeout(() => {
            func(...args);
            timeout = null;
        }, delay);
    };
}
```

Le debouncing prend une fonction et un délai en paramètres, et renvoie une nouvelle fonction "debounced". Lorsque vous appelez la fonction debounced, elle s'exécutera après `delay` millisecondes. Si la fonction est appelée pendant ce laps de temps, elle annule l'appel précédent et attend à nouveau le `delay`.

Testons ce comportement :

```javascript
function fun(a, b) {
    console.log(`This is a function with arguments ${a} and ${b}`);
}

const debouncedFun = debounce(fun, 500);
debouncedFun(2, 3);
debouncedFun(2, 3);
debouncedFun(2, 3); // This is a function with arguments 2 and 3
```

Les deux premiers appels ne s'exécutent pas, tandis que le troisième s'exécute après 500 ms. Le debouncing utilise le concept de closures, il est donc important de les comprendre d'abord.

Le debouncing a de nombreuses applications, la plus populaire étant la fonctionnalité d'auto-complétion dans les barres de recherche. J'ai expliqué le debouncing en détail dans l'article suivant :

[

Le debouncing en JavaScript – Expliqué en construisant une fonctionnalité d'auto-complétion dans React

Salut les lecteurs, j'espère que vous allez bien ! Je suis de retour avec un autre tutoriel sur le développement web. Si vous êtes quelqu'un qui aime développer des applications web avec JavaScript et React, alors cet article est pour vous...

![favicon](https://cdn.freecodecamp.org/universal/favicons/favicon.ico)Kunal NalawadefreeCodeCamp.org

![photo-1550063873-ab792950096b](https://www.freecodecamp.org/news/content/images/2024/02/photo-1550063873-ab792950096b.jpeg)

][22]

## Comment implémenter le Throttling

Le throttling est une technique qui limite la fréquence à laquelle une fonction est appelée. Une fonction "throttled" s'exécute pour la première fois et ne peut être rappelée qu'après un certain délai. Si elle est appelée pendant le délai, rien ne se passe.

Voyons comment l'implémenter :

```javascript
function throttle(func, delay) {
    let timeout = null;
    return (...args) => {
        if (!timeout) {
            func(...args);
            timeout = setTimeout(() => {
                timeout = null;
            }, delay);
        }
    };
}
```

`throttle()` prend une fonction et un délai en paramètres, et renvoie une fonction throttled. Lorsque vous appelez la fonction throttled, elle s'exécute la première fois et lance un minuteur avec `delay`. Pendant ce temps, peu importe le nombre de fois que vous appelez la fonction throttled, elle ne s'exécutera pas.

Testons ce comportement :

```javascript
function fun(a, b) {
    console.log(`This is a function with arguments ${a} and ${b}`);
}

const throttledFun = throttle(fun, 500);

throttledFun(2, 3); // This is a function with arguments 2 and 3
throttledFun(2, 3);

setTimeout(() => {
    throttledFun(2, 3);
}, 300);

setTimeout(() => {
    throttledFun(2, 3); // This is a function with arguments 2 and 3
}, 600);
```

Ici, le premier appel s'exécute immédiatement, et pendant les 500 ms suivantes, aucun appel de fonction ne s'exécutera. Le dernier s'exécute car il est appelé après 500 ms.

Le throttling utilise également le concept de closures. J'ai expliqué le throttling en détail dans mon article, n'hésitez pas à le consulter :

[

Qu'est-ce que le Throttling en JavaScript ? Expliqué avec un cas d'utilisation simple en React

Bienvenue à nouveau, chers développeurs ! Aujourd'hui, nous plongeons une fois de plus dans JavaScript et le développement web pour apprendre le throttling. En tant que développeur, rendre votre site web convivial est important...

![favicon](https://cdn.freecodecamp.org/universal/favicons/favicon.ico)Kunal NalawadefreeCodeCamp.org

![throttling-image](https://www.freecodecamp.org/news/content/images/2024/04/throttling-image.jpeg)

][23]

## Qu'est-ce que le Currying ?

Le currying est une technique où une fonction avec plusieurs arguments est transformée en une séquence de fonctions, chaque fonction prenant un seul argument et renvoyant une autre fonction. Par exemple, considérons la fonction ci-dessous :

```javascript
function add(a, b, c) {
    return a + b + c;
}
```

Avec le currying, la fonction ci-dessus peut être écrite comme suit :

```javascript
function curryAdd(a) {
    return function(b) {
        return function(c) {
            return a + b + c;
        };
    };
}
```

Ici, chaque fonction à l'intérieur de `curryAdd` prend un argument et renvoie une autre fonction jusqu'à ce que tous les arguments soient collectés. `curryAdd` est également connue sous le nom de [fonction d'ordre supérieur][24].

Le currying vous permet de réutiliser des implémentations partielles d'une fonction. Au cas où vous n'auriez pas tous les arguments disponibles, vous pouvez fixer certains arguments de la fonction initialement et renvoyer une fonction réutilisable.

```javascript
// Fonction réutilisable
const addTwo = curryAdd(2);
console.log(addTwo); // prints the function

// Appel du résultat final
const result1 = addTwo(5)(10);
console.log(result1); // 17

const result2 = addTwo(3)(5);
console.log(result2); // 10
```

`addTwo` est une fonction réutilisable qui peut être utilisée plus tard, lorsque des arguments supplémentaires deviennent disponibles.

Ainsi, le currying améliore la modularité et la flexibilité du code avec l'application partielle de fonctions. Il vous permet également de créer des fonctions adaptées à des besoins spécifiques, comme on le voit dans l'exemple ci-dessus.

Le currying simplifie les fonctions complexes en les décomposant en parties plus simples et plus maniables. Cela conduit à un code plus propre et plus lisible.

## Quelle est la différence entre `==` et `===` ?

C'est très simple, mais c'est une question très couramment posée lors des entretiens.

```javascript
let a = 1;
let b = "1";

console.log(a == b); // true
console.log(a === b); // false
```

-   `==` compare uniquement la valeur de `a` et `b`,
-   `===` compare à la fois la valeur et le type de données de `a` et `b`.

## Comment fonctionne le mot-clé `this` ?

Le mot-clé `this` est l'objet auquel vous faites actuellement référence. Sa valeur est définie par le contexte dans lequel vous l'utilisez. Lorsqu'il est référencé globalement, `this` fait référence à l'objet [window][25].

```javascript
console.log(this) // prints window {}
```

`this` peut être utilisé pour accéder aux propriétés d'un objet.

```javascript
const obj = {
    name: 'kunal',
    age: 21,
    getInfo() {
        console.log(`Name: ${this.name}, Age: ${this.age}`);
    }
};

obj.getInfo();
```

Consultez la [documentation][26] pour en savoir plus sur le mot-clé `this`.

## Comment utiliser les méthodes `call`, `apply` et `bind`

Lorsque vous utilisez `this` à l'intérieur d'une fonction, sa valeur est définie sur l'objet sur lequel la fonction est appelée. Prenons un exemple :

```javascript
function getInfo() {
    console.log(`Name: ${this.name}, Age: ${this.age}`);
}
```

`call`, `apply` et `bind` sont utilisés pour définir la valeur du mot-clé `this` à l'intérieur d'une méthode.

### `call`

Pour appeler la fonction `getInfo()` sur un objet, utilisez la fonction `call`. Créons deux objets et appelons `getInfo()` sur ces objets.

```javascript
const ob1 = { name: 'alex', age: 25 };
const ob2 = { name: 'marcus', age: 23 };

getInfo.call(ob1); // Name: alex, Age: 25
getInfo.call(ob2); // Name: marcus, Age: 23
```

`call` définit la valeur du mot-clé `this` à l'intérieur d'une fonction.

### `apply`

La méthode `apply` est similaire à `call`, mais elle diffère par la manière dont vous passez les arguments. Considérons une fonction avec des arguments :

```javascript
function getInfo(a, b) {
    console.log(`Name: ${this.name}, Age: ${this.age}`);
    console.log(`Args: ${a} and ${b}`);
}

const obj = {
    name: 'alex',
    age: 25
};

getInfo.call(obj, 2, 3);
getInfo.apply(obj, [2, 3]);
```

### `bind`

`bind` est utilisé pour créer une nouvelle fonction dont le mot-clé `this` est défini sur un objet spécifique. Utilisons la fonction `getInfo` ci-dessus comme exemple.

```javascript
const obj = {
    name: 'alex',
    age: 25
};

const objGetInfo = getInfo.bind(obj, 2, 3);
objGetInfo();
```

Lorsque `bind` est appelé sur la fonction `getInfo()`, il renvoie une nouvelle fonction qui est liée à `obj`. Désormais, chaque fois que vous appelez la fonction `objGetInfo()`, le mot-clé `this` fait référence à `obj`.

Les trois méthodes sont similaires. C'est-à-dire qu'elles définissent la valeur du mot-clé `this`. Cependant, une différence clé de `bind` est qu'il renvoie une nouvelle fonction, tandis que `call` et `apply` appellent simplement la fonction.

## Que sont les prototypes et l'héritage prototypal ?

L'héritage est un concept de la programmation orientée objet qui permet à un objet d'hériter des propriétés et des méthodes d'un autre objet. Cependant, l'héritage fonctionne différemment en JavaScript.

En JavaScript, chaque objet possède une propriété qui le lie à un autre objet appelé prototype. Le prototype lui-même est un objet qui peut avoir son propre prototype, formant ainsi une chaîne de prototypes. Cette chaîne se termine lorsque nous atteignons un prototype égal à `null`.

Le prototype vous permet d'hériter des méthodes et des propriétés d'un autre objet. Lorsqu'une propriété n'existe pas sur un objet, JavaScript cherche dans son prototype et ainsi de suite jusqu'à ce qu'il atteigne la fin de la chaîne de prototypes.

Comprenons cela avec un exemple.

```javascript
let animal = {
    eats: true,
    walk() {
        console.log("Animal is walking");
    }
};

const rabbit = Object.create(animal);
rabbit.jumps = true;
rabbit.walk(); // Animal is walking
```

`Object.create` crée un nouvel objet `rabbit` avec son prototype défini sur `animal`. Vous pouvez également définir des propriétés supplémentaires pour le nouvel objet.

De plus, la méthode `walk()` n'existe pas sur `rabbit`, elle cherche donc dans le prototype de l'objet, `animal`. Cela signifie que l'objet `rabbit` a hérité des propriétés et des méthodes de l'objet `animal`.

Vous pouvez également utiliser la méthode ES6 `Object.setPrototypeOf` sur n'importe quel objet.

```javascript
const dog = {
    bark() {
        console.log("Dog barking");
    }
};

Object.setPrototypeOf(dog, animal);
console.log(dog.eats); // true
dog.walk(); // Animal is walking
```

Vous pouvez également utiliser une fonction comme constructeur et définir son prototype en utilisant la propriété `prototype`.

```javascript
function Animal(name) {
    this.name = name;
}

Animal.prototype.walk = function () {
    console.log(`${this.name} is walking`);
};

const dog = new Animal("Dog");
console.log(dog); // Animal { name: 'Dog' }
dog.walk(); // Dog is walking
```

Vous pouvez en apprendre davantage sur les prototypes et l'héritage en JavaScript dans l'article suivant de [Germán Cocca][27].

[

Prototypes et héritage en JavaScript – et pourquoi on dit que tout en JS est un objet

Salut tout le monde ! Dans ce court article, nous allons parler de l'héritage prototypal en JavaScript et de ses implications. Table des matières * Intro * Comment accéder aux propriétés et méthodes d'un prototype en JavaScript * La chaîne de prototypes...

![favicon](https://cdn.freecodecamp.org/universal/favicons/favicon.ico)Germán CoccafreeCodeCamp.org

![pexels-maor-attias-5192478](https://www.freecodecamp.org/news/content/images/2022/04/pexels-maor-attias-5192478.jpg)

][28]

## Comment utiliser l'opérateur Spread

L'opérateur spread (décomposition) est utilisé pour étaler le contenu d'un tableau ou d'un objet en éléments individuels ou pour collecter un ensemble d'éléments dans un seul objet. Il a les cas d'utilisation suivants :

L'opérateur spread peut être utilisé pour copier un tableau dans un nouveau :

```javascript
const arr1 = [2, 4, 5];
const arr2 = [...arr1];

console.log(arr1); // [2, 4, 5]
console.log(arr2); // [2, 4, 5]
console.log(arr1 == arr2); // false
```

`arr1` et `arr2` sont des objets complètement différents comme le montre l'opérateur d'égalité.

Vous pouvez également réutiliser les champs d'un objet lors de la création d'un nouvel objet :

```javascript
const obj1 = { name: 'kunal', age: 23 };
const obj2 = { ...obj1, gender: 'male', city: 'Mumbai' };

console.log(obj2); // { name: 'kunal', age: 23, gender: 'male', city: 'Mumbai' }
```

Vous pouvez collecter plusieurs arguments passés à une fonction dans un tableau.

```javascript
function fun1(...args) {
    console.log(args);
}

fun1(1, 2, 3, 4, 5); // [ 1, 2, 3, 4, 5 ]
```

Ou vous pouvez passer les éléments d'un tableau comme arguments individuels à une fonction.

```javascript
function fun2(a, b) {
    console.log(`${a} and ${b}`);
}

const numbers = [1, 2];
fun2(...numbers);
```

## Comment fonctionne la déstructuration de tableaux et d'objets ?

Similairement à l'opérateur spread, vous pouvez extraire les éléments d'un tableau ou d'un objet dans des variables individuelles.

```javascript
const arr = [1, 2, 3];
const [a, b, c] = arr;

console.log(a); // 1
console.log(b); // 2
console.log(c); // 3
```

C'est la même chose pour les objets :

```javascript
const obj = { name: 'kunal', age: 22, gender: 'male' };
const {name, age, gender} = obj;

console.log(name); // kunal
console.log(age); // 22
console.log(gender); // male
```

## Que sont les Promises ?

Les Promises (promesses) sont un concept très important en JavaScript, presque certain d'être abordé lors des entretiens. Les Promises sont utilisées pour les opérations asynchrones en JavaScript comme les timeouts ou les appels d'API.

Les Promises utilisent un objet [Promise][29] qui existe dans l'un des trois états suivants : en attente (pending), remplie (fulfilled/resolved) et rejetée (rejected). Lorsqu'une opération asynchrone se termine, une promesse peut être soit résolue (succès), soit rejetée (échec).

Prenons un exemple simple :

```javascript
function asyncOperation() {
    return new Promise((resolve, reject) => {
        const x = 1 + Math.random() * 10;
        if (x < 5) 
            resolve("Successful");
        else 
            reject("Error");
    });
}
```

La fonction ci-dessus renvoie une promesse qui effectue une opération asynchrone.

-   Si l'opération réussit, la méthode `resolve` est appelée pour indiquer que la promesse a été remplie.
-   Si l'opération échoue, la méthode `reject` est appelée pour indiquer que la promesse a été rejetée.

Dans cet exemple, ces méthodes sont appelées de manière aléatoire. Pour gérer cette promesse dans votre code, utilisez les méthodes `then` et `catch`.

```javascript
asyncOperation()
    .then((res) => {
        console.log(res);
    })
    .catch((err) => {
        console.log(err);
    });
```

-   La méthode `then` prend une fonction de rappel qui s'exécute si la promesse a été résolue. Elle prend un objet de réponse en argument qui est égal à l'objet que vous passez dans la méthode `resolve`.
-   La méthode `catch` prend une fonction de rappel qui s'exécute si la promesse a été rejetée et prend un objet d'erreur en argument qui est passé dans la méthode `reject`.

Le code ci-dessus affiche "Successful" ou "Error" de manière aléatoire.

En dehors des bases, l'objet Promise contient également des méthodes utiles qui fonctionnent avec plusieurs promesses : `[Promise.all()][30]`, `[Promise.any()][31]`, `[Promise.race()][32]`.

Lisez le tutoriel suivant pour en savoir plus sur les promesses en détail :

[

Tutoriel JavaScript Promise – Comment résoudre ou rejeter des promesses en JS

Les promesses sont des briques importantes pour les opérations asynchrones en JavaScript. Vous pensez peut-être que les promesses ne sont pas si faciles à comprendre, à apprendre et à manipuler. Et croyez-moi, vous n'êtes pas seul ! Les promesses sont un défi pour de nombreux développeurs web...

![favicon](https://cdn.freecodecamp.org/universal/favicons/favicon.ico)TAPAS ADHIKARYfreeCodeCamp.org

![cover-1](https://www.freecodecamp.org/news/content/images/2020/11/cover-1.png)

][33]

## Comment utiliser les mots-clés `async` et `await`

Le mot-clé `await` suspend l'exécution d'une fonction jusqu'à ce qu'une promesse soit résolue ou rejetée. `await` ne peut être utilisé qu'à l'intérieur d'une fonction `async`. Prenons un exemple :

```javascript
function dataPromise() {
    return new Promise(resolve => {
        setTimeout(() => resolve("Data retrieved"), 500);
    });
}

async function fetchData() {
    try {
        const res = await dataPromise();
        console.log(res); // Data retrieved (after 500ms)
    } catch(err) {
        console.log(err);
    }
}

fetchData();
```

Lorsque `dataPromise()` est appelée, l'exécution de la fonction s'interrompt pendant 500 ms. L'exécution continue après la résolution de la promesse. Pour gérer les erreurs, entourez le code d'un bloc `try-catch`.

Le mot-clé `await` facilite également le travail avec plusieurs promesses qui s'exécutent l'une après l'autre.

```javascript
function promise1() {
    return new Promise(resolve => {
        setTimeout(() => resolve("Promise 1 resolved"), 500);
    });
}

function promise2() {
    return new Promise(resolve => {
        setTimeout(() => resolve("Promise 2 resolved"), 300);
    });
}

async function fetchData() {
    try {
        const res1 = await promise1();
        console.log(res1); // Promise 1 resolved (after 500ms)
        const res2 = await promise2();
        console.log(res2); // Promise 2 resolved (after 300ms)
    } catch(err) {
        console.log(err);
    }
}

fetchData();
```

`async` et `await` facilitent le travail avec les promesses et rendent également votre code plus propre et plus lisible en supprimant l'imbrication dans le code.

## Qu'est-ce qu'une Event Loop ?

L'Event Loop (boucle d'événements) explique le mécanisme derrière les opérations asynchrones et la gestion des événements. C'est un concept crucial en JavaScript qui explique son modèle d'exécution et, par conséquent, l'une des questions les plus fréquemment posées lors des entretiens.

Plutôt que de fournir une brève explication, je pense que vous devriez l'apprendre en détail et le comprendre pleinement. Lisez la [documentation MDN][34] pour comprendre l'Event Loop en détail, à l'aide de diagrammes.

Si vous préférez les vidéos, vous pouvez également regarder la vidéo suivante de Philip Roberts :

<iframe width="356" height="200" src="https://www.youtube.com/embed/8aGhZQkoFbQ?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" title="What the heck is the event loop anyway? | Philip Roberts | JSConf EU" name="fitvid0"></iframe>

## Comment fonctionne la propagation d'événements – Bubbling et Capturing

La propagation d'événements a lieu lorsqu'un événement est capturé et géré par l'élément cible et tous ses ancêtres. Prenons l'exemple suivant :

```html
<body>
    <div id="box"> <button id="button">Click Me</button> </div>
    <script src="script.js"></script>
</body>
```

Lorsque vous cliquez sur le bouton, vous avez également cliqué sur l'élément `div` ainsi que sur le `body`. L'événement est propagé à travers l'arbre DOM. Ajoutons des gestionnaires à tous les éléments ci-dessus :

```javascript
document.body.addEventListener("click", () => {
    console.log("Body clicked");
});

document.getElementById("box").addEventListener("click", () => {
    console.log("div clicked");
});

document.getElementById("button").addEventListener("click", () => {
    console.log("Button clicked");
});
```

La propagation d'événements se produit de deux manières :

### Event Bubbling

Lorsque le bouton est cliqué, le gestionnaire d'événements du bouton est appelé en premier. Ensuite, l'événement remonte (bubbles up) dans l'arbre DOM et les gestionnaires d'événements des parents sont appelés séquentiellement, du parent immédiat jusqu'à l'ancêtre le plus élevé. C'est-à-dire : les éléments `div` et `body` respectivement.

![image-52](https://www.freecodecamp.org/news/content/images/2024/05/image-52.png)

Event Bubbling

### Event Capturing

Cela fonctionne de manière similaire à l'Event Bubbling, mais à l'inverse. L'événement est d'abord capturé par l'élément racine, puis descend dans l'arbre DOM jusqu'à l'élément cible.

Les gestionnaires d'événements sont appelés en séquence en partant de l'élément racine jusqu'à l'élément cible. Cela peut être réalisé en passant `true` comme troisième paramètre dans la fonction `addEventListener()`.

```javascript
document.body.addEventListener("click", () => {
    console.log("Body clicked");
}, true);
```

![image-53](https://www.freecodecamp.org/news/content/images/2024/05/image-53.png)

Event Capturing

Cependant, cela peut sembler contre-productif. Après tout, l'utilisateur veut seulement cliquer sur le bouton, il n'a aucune idée de la structure de l'arbre DOM. Donc, pour empêcher ce comportement, nous pouvons utiliser la méthode `stopPropagation()`.

```javascript
document.getElementById("button").addEventListener("click", (event) => {
    event.stopPropagation();
    console.log("Button clicked");
});
```

![image-54](https://www.freecodecamp.org/news/content/images/2024/05/image-54.png)

Propagation arrêtée

## Que sont les fonctions génératrices ?

Les fonctions génératrices sont un type spécial de fonctions qui peuvent suspendre leur exécution et la reprendre plus tard. Elles renvoient également une valeur chaque fois qu'elles suspendent leur exécution.

Les fonctions génératrices peuvent être utilisées pour renvoyer une séquence de valeurs de manière itérative, contrairement aux fonctions normales qui ne renvoient qu'une seule fois.

Voici un exemple basique d'une fonction génératrice :

```javascript
function* generatorFunction() {
    yield 1;
    yield 2;
}
```

Une fonction génératrice est déclarée avec `function*` et le mot-clé `yield` est utilisé pour suspendre l'exécution et renvoyer une valeur. La syntaxe ci-dessus crée un objet [GeneratorFunction][35].

```javascript
const gen = generatorFunction()
```

Cet objet utilise un [itérateur][36] pour exécuter une fonction génératrice. L'itérateur fournit une méthode `next()` qui exécute le corps de la fonction jusqu'à l'instruction `yield` suivante et renvoie un objet contenant la valeur générée et une propriété `done` (booléen), qui indique si la fonction génératrice a atteint sa fin.

Appelons la fonction génératrice :

```javascript
console.log(gen.next().value); // 1
console.log(gen.next()); // { value: 2, done: false }
console.log(gen.next()); // { value: undefined, done: true }
```

Ici, le premier appel à `next()` produit 1 et le second produit 2. Le dernier ne produit rien et définit le drapeau `done` à true car il n'y a plus d'instructions `yield`.

Vous pouvez également boucler sur une fonction génératrice en utilisant une boucle `for` :

```javascript
for(value of generatorFunction()) {
  console.log(value)
}
```

De cette façon, vous pouvez contrôler l'exécution d'une fonction génératrice en entrant et en sortant d'une fonction à tout moment.

## Comment implémenter des polyfills pour `Array.map()`, `Array.reduce()` et `Array.filter()`

JavaScript a beaucoup évolué depuis sa création. Plusieurs méthodes et constructions ont été ajoutées à JavaScript qui n'existaient pas auparavant. La plupart des navigateurs modernes utilisent les dernières versions de JavaScript.

Cependant, il existe plusieurs applications qui tournent encore sur d'anciens navigateurs utilisant des versions plus anciennes de JavaScript. Les méthodes de tableau comme `map`, `reduce` et `filter` peuvent ne pas être disponibles. Par conséquent, vous devrez peut-être fournir des polyfills pour ces méthodes.

Les polyfills sont des morceaux de code qui fournissent des fonctionnalités modernes aux anciens navigateurs qui ne les supportent pas. Cela garantit que votre code s'exécute de manière fluide sur différents navigateurs et versions.

La plupart des entreprises ont des sites web qui s'adressent encore à des utilisateurs et des systèmes fonctionnant sur de vieux navigateurs. Savoir écrire des polyfills pour les méthodes fréquemment utilisées est donc important.

Dans notre cas, nous allons écrire des polyfills pour les méthodes `Array.map`, `Array.reduce` et `Array.filter`. Cela signifie que nous allons écrire nos propres implémentations au lieu d'utiliser celles par défaut.

### `Array.map`

Cette méthode prend une fonction de rappel en paramètre, l'exécute sur chaque élément du tableau et renvoie un nouveau tableau modifié.

La fonction de rappel prend trois arguments : l'élément du tableau, l'index et le tableau lui-même. Les deux derniers arguments sont facultatifs.

```javascript
Array.prototype.map = function(callback) {
  var newArray = [];
  for (var i = 0; i < this.length; i++) {
    newArray.push(callback(this[i], i, this));
  }
  return newArray;
};
```

La logique est simple. Appelez la fonction pour chaque élément du tableau et ajoutez chaque valeur au nouveau tableau. Le mot-clé `this` est l'objet sur lequel vous appelez la fonction, dans ce cas, le tableau.

### `Array.filter`

Cette méthode prend également une fonction de rappel en paramètre. La fonction de rappel teste une condition sur chaque élément du tableau et renvoie une valeur booléenne. La méthode `filter` renvoie un nouveau tableau filtré contenant les éléments qui satisfont à la condition.

Cette fonction de rappel prend trois arguments : l'élément du tableau, l'index et le tableau lui-même. Les deux derniers arguments sont facultatifs.

```javascript
Array.prototype.filter = function(callback) {
  var filteredArr = [];
  for (var i = 0; i < this.length; i++) {
    var condition = callback(this[i], i, this);
    if (condition) {
      filteredArr.push(this[i]);
    }
  }
  return filteredArr;
};
```

Ici, utilisez la valeur booléenne renvoyée par la fonction de rappel pour ajouter des éléments au nouveau tableau.

### `Array.reduce`

Cette méthode prend une fonction de rappel et une valeur initiale en paramètres et réduit le tableau à une seule valeur. Cela se fait en exécutant la fonction sur l'accumulateur et la valeur actuelle et en stockant le résultat dans l'accumulateur.

La fonction de rappel prend quatre arguments : l'accumulateur, l'élément actuel, l'index et le tableau lui-même. Les deux derniers arguments sont facultatifs.

```javascript
Array.prototype.reduce = function(callback, initialValue) {
    var accumulator = initialValue;
    for (var i = 0; i < this.length; i++) {
        if (accumulator !== undefined) {
            accumulator = callback(accumulator, this[i], i, this);
        } else {
            accumulator = this[i];
        }
    }
    return accumulator;
};
```

Initialement, définissez l'accumulateur sur la valeur initiale. Exécutez la fonction de rappel pour chaque élément du tableau et stockez le résultat dans l'accumulateur. Si l'accumulateur est indéfini, définissez-le sur l'élément lui-même.

Testons ces méthodes :

```javascript
const arr = [1, 2, 3];
console.log(arr.map(ele => ele * 2)); // [ 2, 4, 6 ]
console.log(arr.filter(ele => ele < 2)); // [ 1 ]
console.log(arr.reduce((total, ele) => total + ele, 0)); // 6
```

**Remarque :** Avant d'ajouter un polyfill pour n'importe quelle propriété, vérifiez toujours si la propriété existe déjà sur le prototype de l'objet, sinon vous pourriez écraser le comportement existant. Par exemple :

```javascript
if (!Array.prototype.map)
```

## Réflexions supplémentaires

Avant de conclure, j'aimerais partager quelques réflexions supplémentaires. Réussir un entretien JavaScript ne consiste pas seulement à mémoriser des concepts. Assurez-vous de plonger profondément dans chaque sujet et de le comprendre parfaitement, y compris ses applications.

De plus, ne sous-estimez pas l'importance des compétences relationnelles comme la communication. Transmettre vos pensées clairement à l'interviewer est aussi important que de connaître votre sujet.

Lorsqu'on vous pose des questions sur l'un des concepts ci-dessus, commencez par expliquer brièvement le concept, puis utilisez un exemple pour une explication plus détaillée.

Expliquer avec des exemples est crucial pour répondre à toute question d'entretien. Cela permet aux interviewers de comprendre plus facilement votre processus de réflexion. Dans cet article, j'ai également suivi un modèle similaire en expliquant chaque concept.

Enfin, continuez à consulter ce manuel tout au long de votre préparation aux entretiens. N'hésitez pas à l'utiliser comme aide-mémoire. Si vous êtes un développeur expérimenté, ce manuel vous aidera également à revoir et à renforcer ces concepts.

## Conclusion

Les entretiens peuvent être assez effrayants et imprévisibles. Bien qu'il y ait une forte demande pour les compétences en JavaScript, la concurrence est tout aussi intense. Construire une base solide est crucial pour une préparation d'entretien réussie.

Dans ce manuel, j'ai souligné plusieurs sujets importants à préparer pour votre prochain entretien JavaScript et j'ai fourni des explications détaillées pour chaque concept. Bien que cette liste ne soit pas exhaustive, elle couvre plusieurs concepts critiques. Si vous pensez que j'ai oublié des sujets importants, n'hésitez pas à me le faire savoir.

Si vous ne parvenez pas à comprendre le contenu ou si vous trouvez l'explication insatisfaisante, commentez vos réflexions ci-dessous. Les nouvelles idées sont toujours les bienvenues ! N'hésitez pas à me contacter sur Twitter.

Bonne chance pour vos entretiens !!!

[1]: #heading-comment-utiliser-les-mots-cles-var-let-et-const
[2]: #heading-qu-est-ce-que-le-hoisting
[3]: #heading-comment-fonctionnent-les-closures
[4]: #heading-comment-implementer-le-debouncing
[5]: #heading-comment-implementer-le-throttling
[6]: #heading-qu-est-ce-que-le-currying
[7]: #heading-quelle-est-la-difference-entre-et
[8]: #heading-comment-fonctionne-le-mot-cle-this
[9]: #heading-comment-utiliser-les-methodes-call-apply-et-bind
[10]: #heading-que-sont-les-prototypes-et-l-heritage-prototypal
[11]: #heading-comment-utiliser-l-operateur-spread
[12]: #heading-comment-fonctionne-la-destructuration-de-tableaux-et-d-objets
[13]: #heading-que-sont-les-promises
[14]: #heading-comment-utiliser-les-mots-cles-async-et-await
[15]: #heading-qu-est-ce-qu-une-event-loop
[16]: #heading-comment-fonctionne-la-propagation-d-evenements-bubbling-et-capturing
[17]: #heading-que-sont-les-fonctions-generatrices
[18]: #heading-comment-implementer-des-polyfills-pour-array-map-array-reduce-et-array-filter
[19]: #heading-reflexions-supplementaires
[20]: https://www.freecodecamp.org/news/author/matias-hernandez/
[21]: https://www.freecodecamp.org/news/closures-in-javascript/
[22]: https://www.freecodecamp.org/news/deboucing-in-react-autocomplete-example/
[23]: https://www.freecodecamp.org/news/throttling-in-javascript/
[24]: https://www.freecodecamp.org/news/higher-order-functions-explained/
[25]: https://developer.mozilla.org/en-US/docs/Web/API/Window
[26]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this
[27]: https://www.freecodecamp.org/news/author/gercocca/
[28]: https://www.freecodecamp.org/news/prototypes-and-inheritance-in-javascript/
[29]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
[30]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
[31]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/any
[32]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race
[33]: https://www.freecodecamp.org/news/javascript-promise-tutorial-how-to-resolve-or-reject-promises-in-js/
[34]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop
[35]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction
[36]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#the_iterator_protocol