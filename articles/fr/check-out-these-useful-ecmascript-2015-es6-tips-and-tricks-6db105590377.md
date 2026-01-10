---
title: Découvrez ces conseils et astuces utiles pour ECMAScript 2015 (ES6)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T11:21:58.000Z'
originalURL: https://freecodecamp.org/news/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W5vbBi1Nah40KGMRIE1GJw.jpeg
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
seo_title: Découvrez ces conseils et astuces utiles pour ECMAScript 2015 (ES6)
seo_desc: 'By rajaraodv

  EcmaScript 2015 (aka ES6) has been around for couple of years now, and various new
  features can be used in clever ways. I wanted to list and discuss some of them,
  since I think you’ll find them useful.

  If you know of other tips, please l...'
---

Par rajaraodv

EcmaScript 2015 (aka ES6) existe depuis quelques années maintenant, et diverses nouvelles fonctionnalités peuvent être utilisées de manière intelligente. Je voulais lister et discuter de certaines d'entre elles, car je pense que vous les trouverez utiles.

Si vous connaissez d'autres conseils, faites-le moi savoir dans les commentaires et je serai heureux de les ajouter.

### 1. Imposer des paramètres obligatoires

ES6 fournit des [valeurs de paramètre par défaut](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) qui vous permettent de définir une valeur par défaut à utiliser si la fonction est appelée sans ce paramètre.

Dans l'exemple suivant, nous définissons la fonction `required()` comme valeur par défaut pour les paramètres `a` et `b`. Cela signifie que si `a` ou `b` n'est pas passé, la fonction `required()` est appelée et vous obtiendrez une erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/3ub3TwVA-WD6loznXLRYjTa3Fh5ANEy1iWFf)

```
const required = () => {throw new Error('Paramètre manquant')};
```

```
//La fonction ci-dessous lancera une erreur si "a" ou "b" est manquant.const add = (a = required(), b = required()) => a + b;
```

```
add(1, 2) //3add(1) // Erreur: Paramètre manquant.
```

### 2. La puissante méthode "reduce"

La méthode [reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) des tableaux est extrêmement polyvalente. Elle est généralement utilisée pour convertir un tableau d'éléments en une seule valeur. **Mais vous pouvez faire beaucoup plus avec elle.**

> **?Astuce: La plupart de ces astuces reposent sur le fait que la valeur initiale soit un tableau ou un objet au lieu d'une simple valeur comme une chaîne ou une variable.**

**2.1 Utiliser reduce pour faire à la fois map et filter *simultanément***

Supposons que vous avez une situation où vous avez une liste d'éléments, et vous voulez mettre à jour chaque élément (c'est-à-dire [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)) et ensuite filtrer seulement quelques éléments (c'est-à-dire [filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)). Mais cela signifie que vous devrez parcourir la liste deux fois!

Dans l'exemple ci-dessous, nous voulons doubler la valeur des éléments du tableau et ensuite ne sélectionner que ceux qui sont supérieurs à 50. Remarquez comment nous pouvons utiliser la puissante méthode reduce pour doubler (map) et ensuite filtrer? C'est assez efficace.

![Image](https://cdn-media-1.freecodecamp.org/images/2RmGA5oaAU66UHEmGi1CuQcmjmxVptU6ODya)

```
const numbers = [10, 20, 30, 40];
```

```
const doubledOver50 = numbers.reduce((finalList, num) => {    num = num * 2; //double chaque nombre (c'est-à-dire map)    //filtrer les nombres > 50  if (num > 50) {    finalList.push(num);  }  return finalList;}, []);
```

```
doubledOver50; // [60, 80]
```

#### 2.2 Utiliser "reduce" au lieu de "map" ou "filter"

Si vous regardez attentivement l'exemple ci-dessus (de 2.1), vous saurez que reduce peut être utilisé pour filtrer ou mapper des éléments! **?**

#### **2.3 Utiliser reduce pour équilibrer les parenthèses**

Voici un autre exemple de la polyvalence de la fonction reduce. Étant donné une chaîne avec des parenthèses, nous voulons savoir si elles sont équilibrées, c'est-à-dire qu'il y a un nombre égal de "(" et ")", et que "(" est avant ")".

Nous pouvons facilement faire cela avec reduce comme montré ci-dessous. Nous tenons simplement une variable `counter` avec une valeur de départ de 0. Nous comptons vers le haut si nous rencontrons `(` et vers le bas si nous rencontrons `)`. Si elles sont équilibrées, alors nous devrions finir avec `0`.

![Image](https://cdn-media-1.freecodecamp.org/images/aDMvpuYoRuNYZQSNkSQRWFUSj7Ts4uYHvEqN)

```
//Retourne 0 si équilibré.const isParensBalanced = (str) => {  return str.split('').reduce((counter, char) => {    if(counter < 0) { //correspond à ")" avant "("      return counter;    } else if(char === '(') {      return ++counter;    } else if(char === ')') {      return --counter;    }  else { //correspond à un autre caractère      return counter;    }      }, 0); //<-- valeur de départ du compteur}
```

```
isParensBalanced('(())') // 0 <-- équilibréisParensBalanced('(asdfds)') //0 <-- équilibré
```

```
isParensBalanced('(()') // 1 <-- non équilibréisParensBalanced(')(') // -1 <-- non équilibré
```

#### 2.4 Compter les éléments dupliqués dans un tableau (Convertir un tableau → Objet)

Il arrive que vous souhaitiez compter les éléments dupliqués dans un tableau ou convertir un tableau en un objet. Vous pouvez utiliser reduce pour cela.

Dans l'exemple ci-dessous, nous voulons compter combien de voitures de chaque type existent et mettre ce chiffre dans un objet.

![Image](https://cdn-media-1.freecodecamp.org/images/S8-gsm9HsRWi0NuGzFUHlxZc2snesPCyRqif)

```
var cars = ['BMW','Benz', 'Benz', 'Tesla', 'BMW', 'Toyota'];
```

```
var carsObj = cars.reduce(function (obj, name) {    obj[name] = obj[name] ? ++obj[name] : 1;  return obj;}, {});
```

```
carsObj; // => { BMW: 2, Benz: 2, Tesla: 1, Toyota: 1 }
```

Il y a beaucoup plus de choses que vous pouvez faire en utilisant reduce, et je vous encourage à lire les exemples listés sur MDN [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce).

### **3. La destructuration d'objets**

#### 3.1 Supprimer les propriétés indésirables

Il arrive que vous souhaitiez supprimer des propriétés indésirables — peut-être parce qu'elles contiennent des informations sensibles ou sont simplement trop grandes. Au lieu de parcourir tout l'objet pour les supprimer, nous pouvons simplement extraire ces propriétés dans des variables et garder les utiles dans le paramètre ***rest***.

Dans l'exemple ci-dessous, nous voulons supprimer les propriétés `_internal` et `tooBig`. Nous pouvons les assigner aux variables `_internal` et `tooBig` et stocker le reste dans un paramètre ***rest*** `cleanObject` que nous pouvons utiliser plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/gks2CAUelU0bRtB4Qv6QCa36iwO6V-P5anql)

```
let {_internal, tooBig, ...cleanObject} = {el1: '1', _internal:"secret", tooBig:{}, el2: '2', el3: '3'};
```

```
console.log(cleanObject); // {el1: '1', el2: '2', el3: '3'}
```

#### **3.2 Déstructurer les objets imbriqués dans les paramètres de fonction**

Dans l'exemple ci-dessous, la propriété `engine` est un objet imbriqué de l'objet `car`. Si nous sommes intéressés par, disons, la propriété `vin` de `engine`, nous pouvons facilement la déstructurer comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/kKqMWgbJ4iHiiISlA5IBerbFpLfGPqDH0Cz7)

```
var car = {  model: 'bmw 2018',  engine: {    v6: true,    turbo: true,    vin: 12345  }}
```

```
const modelAndVIN = ({model, engine: {vin}}) => {  console.log(`model: ${model} vin: ${vin}`);}
```

```
modelAndVIN(car); // =&gt; model: bmw 2018  vin: 12345
```

#### 3.3 Fusionner des objets

ES6 vient avec un opérateur de propagation (dénoté par trois points). Il est généralement utilisé pour déconstruire les valeurs de tableau, mais vous pouvez l'utiliser sur les objets également.

Dans l'exemple suivant, nous utilisons l'opérateur de propagation pour propager dans un nouvel objet. Les clés de propriété dans le 2ème objet écraseront les clés de propriété dans le 1er objet.

Dans l'exemple ci-dessous, les clés de propriété `b et c` de `object2` écrasent celles de `object1`

![Image](https://cdn-media-1.freecodecamp.org/images/Ha7VjK0erZZBEhegOXkd7i0nwwSep-agomIf)

```
let object1 = { a:1, b:2,c:3 }let object2 = { b:30, c:40, d:50}let merged = {...object1, ...object2} //propager et réajouter dans mergedconsole.log(merged) // {a:1, b:30, c:40, d:50}
```

### 4. Les Sets

#### 4.1 Supprimer les doublons des tableaux en utilisant les Sets

Dans ES6, vous pouvez facilement supprimer les doublons en utilisant les Sets, car les Sets ne permettent de stocker que des valeurs uniques.

![Image](https://cdn-media-1.freecodecamp.org/images/c6-c8h6HRo2IhEO3K5eSUr0b3mKsGTz7bXnz)

```
let arr = [1, 1, 2, 2, 3, 3];let deduped = [...new Set(arr)] // [1, 2, 3]
```

#### 4.2 Utiliser les méthodes de tableau

Convertir les Sets en un tableau est aussi simple que d'utiliser un opérateur de propagation (`...`). Vous pouvez utiliser toutes les méthodes de tableau facilement sur les Sets également!

Supposons que nous avons un set comme montré ci-dessous et que nous voulons le `filtrer` pour ne contenir que les éléments supérieurs à 3.

![Image](https://cdn-media-1.freecodecamp.org/images/WOfyWUT3195DJtjn1-5kef5VbIyauIkjOFhh)

```
let mySet = new Set([1,2, 3, 4, 5]);
```

```
var filtered = [...mySet].filter((x) => x > 3) // [4, 5]
```

### 5. La destructuration de tableau

De nombreuses fois, votre fonction peut retourner plusieurs valeurs dans un tableau. Nous pouvons facilement les capturer en utilisant la destructuration de tableau.

#### 5.1 Échanger des valeurs

![Image](https://cdn-media-1.freecodecamp.org/images/LQyBnIxTXt0k8uFDx608soQwixZWdfhESS6F)

```
let param1 = 1;let param2 = 2;
```

```
//échanger et assigner les valeurs de param1 et param2[param1, param2] = [param2, param1];
```

```
console.log(param1) // 2console.log(param2) // 1
```

#### 5.2 Recevoir et assigner plusieurs valeurs d'une fonction

Dans l'exemple ci-dessous, nous récupérons un post à `/post` et les commentaires associés à `/comments`. Puisque nous utilisons `async / await`, la fonction retourne le résultat dans un tableau. En utilisant la destructuration de tableau, nous pouvons simplement assigner le résultat directement dans les variables correspondantes.

![Image](https://cdn-media-1.freecodecamp.org/images/c4x-m3Q161nVcfvPlNo1FEPH7AKmPYGNuzZI)

```
async function getFullPost(){  return await Promise.all([    fetch('/post'),    fetch('/comments')  ]);}
```

```
const [post, comments] = getFullPost();
```

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissements ? ci-dessous quelques fois pour montrer votre soutien! f44ff44ff44f ??

### Mes autres articles

[_https://medium.com/@rajaraodv/latest_](https://medium.com/@rajaraodv/latest)

#### ECMAScript 2015+

1. [_Exemples de tout ce qui est *NOUVEAU* dans ECMAScript 2016, 2017 et 2018_](https://medium.freecodecamp.org/here-are-examples-of-everything-new-in-ecmascript-2016-2017-and-2018-d52fa3b5a70e)
2. [_Découvrez ces conseils et astuces utiles pour ECMAScript 2015 (ES6)_](https://medium.freecodecamp.org/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377)
3. [_5 parties "mauvaises" de JavaScript qui sont corrigées dans ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
4. [_Est-ce que "Class" dans ES6 est la nouvelle partie "mauvaise"?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### Améliorations du Terminal

1. [_Comment personnaliser votre terminal - Un guide étape par étape avec des images_](https://medium.freecodecamp.org/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22)
2. [_Personnaliser votre terminal "ZSH" en sept étapes - Un guide visuel_](https://medium.freecodecamp.org/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38)

#### WWW

1. [_Une histoire fascinante et désordonnée du Web et de JavaScript_](https://medium.freecodecamp.org/a-fascinating-and-messy-history-of-the-web-and-javascript-video-8978dc7bda75)

#### Virtual DOM

1. [_Le fonctionnement interne du Virtual DOM_](https://medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf)

#### Performance de React

1. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)
2. [_Utiliser Preact au lieu de React_](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c#.7fzp0lyo3)

#### Programmation Fonctionnelle

1. [_JavaScript est Turing Complete - Expliqué_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Programmation Fonctionnelle en JS - Avec des exemples pratiques (Partie 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Programmation Fonctionnelle en JS - Avec des exemples pratiques (Partie 2)_](https://medium.freecodecamp.org/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e)
4. [_Pourquoi Redux a besoin que les reducers soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)

#### WebPack

1. [_Webpack - Les parties confuses_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(sous le capot)_
3. [_Webpack's HMR et React-Hot-Loader - Le manuel manquant_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Pourquoi Draft.js et pourquoi vous devriez contribuer_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_Comment Draft.js représente les données de texte riche_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React et Redux :

1. [_Guide étape par étape pour construire des applications React Redux_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_Un guide pour construire une application React Redux CRUD_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(application de 3 pages)_
3. [_Utiliser des Middlewares dans les applications React Redux_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Ajouter une validation de formulaire robuste aux applications React Redux_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Sécuriser les applications React Redux avec des tokens JWT_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Gérer les emails transactionnels dans les applications React Redux_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_L'anatomie d'une application React Redux_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)
8. [_Pourquoi Redux a besoin que les reducers soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)
9. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)