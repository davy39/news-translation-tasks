---
title: Comment fonctionne array.prototype.map()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-27T23:12:55.000Z'
originalURL: https://freecodecamp.org/news/how-array-prototype-map-works-b6b69379c3af
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sxqOoI2RvGq8n7MYwoWX-w.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment fonctionne array.prototype.map()
seo_desc: 'By Pradeep Pothineni

  JavaScript is an ubiquitous language now. Once confined to client side usage, now
  you can find it on servers in many flavors. As JavaScript grew, so did its arsenal
  of functions that users can use. Most times you are content usin...'
---

Par Pradeep Pothineni

JavaScript est désormais un langage omniprésent. Autrefois confiné à une utilisation côté client, on le trouve maintenant sur les serveurs sous de nombreuses formes. À mesure que JavaScript a évolué, son arsenal de fonctions utilisables par les développeurs a également grandi. La plupart du temps, vous êtes satisfait d'utiliser ces méthodes et vous ne souhaiterez que rarement franchir cette étape supplémentaire pour comprendre ce qui se passe réellement sous le capot.

Sur cette note, franchissons aujourd'hui cette étape supplémentaire et explorons une fonction très populaire : `**Array.prototype.map()**`_._

![Image](https://cdn-media-1.freecodecamp.org/images/1*sxqOoI2RvGq8n7MYwoWX-w.jpeg)

_Avertissement_ : Je n'expliquerai pas comment utiliser `**map()**` — l'exemple ci-dessous l'illustre, ou vous pouvez trouver de nombreux exemples en cherchant sur Google. Au lieu de cela, plongeons dans la manière dont map est réellement implémenté en coulisses.

La méthode `**map()**` crée un nouveau tableau avec le résultat de l'appel d'une fonction fournie sur chaque élément du tableau appelant.

Exemple :

```js
var array1 = [1, 4, 9, 16];
// passer une fonction à map
const map1 = array1.map(x => x * 2);

console.log(map1);
// sortie attendue : Array [2, 8, 18, 32]
```

#### **Implémentation**

Prenons l'implémentation directement de la source et essayons de la disséquer. Ci-dessous se trouve le polyfill MDN. Prenez le temps de comprendre le code, copiez-le et exécutez-le sur votre machine. Si vous êtes un développeur JavaScript débutant ou intermédiaire, vous rencontrerez sûrement au moins quelques questions.

```js
/* Implémentation de Array.prototype.map */
Array.prototype.map = function (callback/*, thisArg*/) {
    var T, A, k;
    if (this == null) {
        throw new TypeError('this est null ou non défini');
    }
    var O = Object(this);
    var len = O.length >>> 0;
    if (typeof callback !== 'function') {
        throw new TypeError(callback + ' n\'est pas une fonction');
    }
    if (arguments.length > 1) { 
        T = arguments[1];
    }
    A = new Array(len);
    k = 0;
    while (k < len) {
        var kValue, mappedValue;
        if (k in O) {
            kValue = O[k];
            mappedValue = callback.call(T, kValue, k, O);            
            A[k] = mappedValue;
        }
        k++;
    }
    return A;
};
```

J'ai mis en évidence quelques questions courantes qui pourraient surgir dans les commentaires du code ci-dessous.

```js
/* Implémentation de Array.prototype.map */
Array.prototype.map = function (callback/*, thisArg*/) {
    var T, A, k;
    if (this == null) {
        throw new TypeError('this est null ou non défini');
    }
    var O = Object(this);
    var len = O.length >>> 0;// QUESTION 1 : Quel est l'intérêt de cette ligne de code ?
    if (typeof callback !== 'function') {
        throw new TypeError(callback + ' n\'est pas une fonction');
    }
    if (arguments.length > 1) { 
        T = arguments[1];
    }
    //  QUESTION 2 : Quel est l'intérêt de la condition if et pourquoi assignons-nous T=arguments[1] ?
    A = new Array(len);
    k = 0;
    while (k < len) {
        var kValue, mappedValue;
        if (k in O) {
            kValue = O[k];
            mappedValue = callback.call(T, kValue, k, O); 
            // QUESTION 3 : pourquoi passons-nous T, k et O alors que tout ce dont vous avez besoin est kValue ?
            A[k] = mappedValue;
        }
        k++;
    }
    return A;
};
```

Répondons à chacune d'entre elles en commençant par le bas.

**QUESTION 3 : Pourquoi passons-nous T, k et O alors que tout ce dont vous avez besoin est kValue ?**

```js
mappedValue = callback.call(T, kValue, k, O);
```

C'est la plus simple des trois questions, c'est pourquoi je l'ai choisie pour commencer. Dans la plupart des cas, passer la **kValue** à la **callback** serait suffisant, mais :

* Et si vous avez un cas d'utilisation où vous devez effectuer une opération uniquement sur un élément sur deux ? Eh bien, vous avez besoin d'un index qui est **(k)**.
* De même, il pourrait y avoir d'autres cas d'utilisation où vous avez besoin du tableau **(O)** lui-même pour qu'il soit disponible dans la callback.
* Pourquoi **T** ? Pour l'instant, sachez simplement que **T** est transmis pour maintenir le contexte. Vous comprendrez mieux cela une fois que vous aurez terminé avec la question 2.

**QUESTION 2 : Quel est l'intérêt de la condition if et pourquoi assignons-nous T=arguments[1] ?**

```js
if (arguments.length > 1) {   T = arguments[1];    }
```

La fonction map dans l'implémentation ci-dessus a deux arguments : la **callback** et le **thisArg** optionnel. La callback est un argument obligatoire tandis que **thisArg** est optionnel.

On peut passer ce qui devrait être la valeur **"this"** à l'intérieur de la **callback** en fournissant le deuxième argument optionnel. C'est pourquoi le code vérifie s'il y a plus d'un argument et assigne le deuxième argument optionnel à une variable qui peut être transmise à la callback.

Pour mieux illustrer, supposons que vous avez une exigence fictive où vous devez retourner le _nombre/2_ s'il est divisible par 2, et s'il n'est pas divisible par 2, vous devez retourner le nom d'utilisateur de la personne appelante. Le code ci-dessous illustre comment vous pouvez faire cela :

```js
const myObj = { user: "John Smith" }
var x = [10, 7];
let output = x.map(function (n) {
  if (n % 2 == 0) {
    return n / 2;
  } else {
    return this.user
  }
}, myObj) // myObj est le deuxième argument optionnel arguments[1]

console.log(output); // [5,'John Smith']
// si vous exécutez le programme sans fournir myObj, ce serait // indéfini car il ne peut pas accéder aux valeurs de myObj
console.log(output); // [ 5, undefined ]
```

**QUESTION 1 : Quel est l'intérêt de cette ligne de code ?**

```js
var len = O.length >>> 0
```

Celle-ci m'a pris un certain temps à comprendre. Il se passe beaucoup de choses dans cette ligne de code. En JavaScript, vous avez la possibilité de redéfinir le **"this"** dans une fonction en invoquant la méthode en utilisant **call_._** Vous pouvez le faire en utilisant **bind** ou **apply** également, mais pour cette discussion, restons avec **call.**

```js
const anotherObject={length:{}} 
const myObj = { user: "John Smith" }
var x = [10, 7];
let output = x.map.call(anotherObject,function (n) {
  if (n % 2 == 0) {return n / 2;}
  else 
  {return this.user}
}, myObj)
```

Lorsque vous invoquez en utilisant **call,** le premier paramètre serait le contexte dans lequel la fonction map s'exécute. En envoyant le paramètre, vous écrasez le **"this"** à l'intérieur de map avec le **"this"** de anotherObject.

Si vous observez, la propriété **length** de anotherObject est un objet vide et non un entier. Si vous utilisez simplement **O.length au lieu de O.length>>>0**, cela entraînerait une valeur indéfinie. En décalant à zéro, vous convertissez en réalité toutes les fractions et les non-entiers en un entier. Dans ce cas, le résultat serait coercé à 0.

La plupart des cas d'utilisation n'auront pas besoin de cette vérification, mais il pourrait y avoir un cas limite où ce type de scénario doit être géré. Les bons programmeurs qui ont conçu la spécification ont vraiment tout pensé ! En parlant de la spécification, vous pouvez en fait trouver la spécification sur la manière dont chaque fonction doit être implémentée dans Ecmascript ici :

[**Spécification du langage ECMAScript - ÉDITION ECMA-262 5.1**](https://www.ecma-international.org/ecma-262/5.1/#sec-15.4.4.19)  
[_Ce document et ses éventuelles traductions peuvent être copiés et fournis à d'autres, et des œuvres dérivées qui commentent_](https://www.ecma-international.org/ecma-262/5.1/#sec-15.4.4.19)  
[www.ecma-international.org](https://www.ecma-international.org/ecma-262/5.1/#sec-15.4.4.19)

La spécification (**étape 3**) indique clairement que la longueur doit être un entier non signé sur 32 bits. C'est la raison pour laquelle nous effectuons un décalage de remplissage à zéro pour nous assurer que la longueur est un entier, car map lui-même n'exige pas que la valeur **this** soit un objet Array.

C'est tout !

Je tiens à remercier quelques personnes que je n'ai jamais rencontrées, mais qui ont eu la gentillesse de prendre le temps (sur des forums Internet) et de m'aider à comprendre quelques nuances.

[Salathiel Genese](https://github.com/SalathielGenese), [Jordan Harband](https://twitter.com/ljharb) — merci !

Note : Si vous êtes bloqué sur une autre ligne de code, n'hésitez pas à la mettre dans les commentaires et je ferai de mon mieux pour clarifier.

Merci pour votre temps et bon codage !