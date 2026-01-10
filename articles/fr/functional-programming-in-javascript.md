---
title: Qu'est-ce que la programmation fonctionnelle ? Un guide JavaScript pour débutants
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2020-11-17T21:06:24.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Functional-code.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que la programmation fonctionnelle ? Un guide JavaScript pour
  débutants
seo_desc: 'JavaScript is a multi-paradigm language and can be written following different
  programming paradigms. A programming paradigm is essentially a bunch of rules that
  you follow when writing code.

  These paradigms exist because they solve problems that pro...'
---

JavaScript est un langage multi-paradigme et peut être écrit en suivant différents paradigmes de programmation. Un paradigme de programmation est essentiellement un ensemble de règles que vous suivez lors de l'écriture de code.

Ces paradigmes existent parce qu'ils résolvent des problèmes auxquels les programmeurs sont confrontés, et ils ont leurs propres règles et instructions pour vous aider à écrire un meilleur code.

Chaque paradigme vous aide à résoudre un problème spécifique. Il est donc utile d'avoir un aperçu de chacun d'eux. Nous allons couvrir la programmation fonctionnelle ici.

À la fin de cet article, vous trouverez des ressources que vous pouvez utiliser pour aller plus loin si vous avez apprécié cette introduction. 

Il y a aussi un glossaire GitHub qui vous aidera à décoder certains des jargons utilisés en programmation fonctionnelle. 

Enfin, vous trouverez un endroit pour mettre les mains dans le code avec des exemples pratiques et un dépôt GitHub rempli de ressources que vous pouvez utiliser pour en apprendre davantage. Alors, plongeons-nous dans le sujet.

## Paradigmes de programmation déclarative vs impérative

Un exemple de ces paradigmes dont j'ai parlé au début est la programmation orientée objet. Un autre est la programmation fonctionnelle.

Alors, qu'est-ce que la programmation fonctionnelle exactement ? 

La programmation fonctionnelle est un sous-paradigme du paradigme de **programmation déclarative**, avec ses propres règles à suivre lors de l'écriture de code.

### Qu'est-ce que le paradigme de programmation déclarative ?

Si vous codez dans un langage qui suit le paradigme déclaratif, vous écrivez du code qui spécifie **ce que vous voulez faire, sans dire comment.**

Un exemple super simple de cela est soit SQL soit HTML :

```sql
SELECT * FROM customers
```

```html
<div></div>
```

Dans les exemples de code ci-dessus, vous n'implémentez pas le `SELECT` ou comment rendre un `div`. Vous dites simplement à l'ordinateur _ce qu'il doit faire_, sans le _comment_.

De ce paradigme, il existe des sous-paradigmes tels que la **programmation fonctionnelle**. Plus d'informations à ce sujet ci-dessous.

### Qu'est-ce que le paradigme de programmation impérative ?

Si vous codez dans un langage qui suit le paradigme impératif/procédural, vous écrivez du code qui dit **comment faire quelque chose.**

Par exemple, si vous faites quelque chose comme ci-dessous :

```javascript
for (let i = 0; i < arr.length; i++) {
     increment += arr[i];
}
```

Vous dites à l'ordinateur exactement quoi faire. Parcourez le tableau appelé `arr`, puis `incrémentez` chacun des éléments du tableau.

### Programmation déclarative vs impérative

Vous pouvez écrire JavaScript dans le **paradigme déclaratif** ou le **paradigme impératif**. C'est ce que les gens veulent dire lorsqu'ils disent que c'est un langage multi-paradigme. C'est juste que le code fonctionnel suit le **paradigme déclaratif**. 

Si cela vous aide à vous souvenir, un exemple de commande déclarative serait de demander à l'ordinateur de vous faire une tasse de thé (je ne me soucie pas de la manière dont vous le faites, apportez-moi simplement du thé).

Tandis qu'impérativement, vous devriez dire :

* Allez dans la cuisine.
* S'il y a une bouilloire dans la pièce, et qu'elle a assez d'eau pour une tasse de thé, allumez la bouilloire.
* S'il y a une bouilloire dans la pièce, et qu'elle n'a pas assez d'eau pour une tasse de thé, remplissez la bouilloire avec assez d'eau pour une tasse de thé, puis allumez la bouilloire.
* _Et ainsi de suite_

### Alors, qu'est-ce que la programmation fonctionnelle ?

Alors, que signifie cela pour le code fonctionnel ?

Parce que c'est un sous-paradigme du **paradigme déclaratif**, cela affecte la manière dont vous écrivez le code fonctionnel. Cela conduit généralement à moins de code, car JavaScript a déjà beaucoup de fonctions intégrées dont vous avez couramment besoin. C'est l'une des raisons pour lesquelles les gens aiment le code fonctionnel. 

Cela vous permet également d'abstraire beaucoup (vous n'avez pas besoin de comprendre en profondeur comment quelque chose est fait), vous appelez simplement une fonction qui le fait pour vous.

Et quelles sont les règles qui mènent au code fonctionnel ?

La programmation fonctionnelle peut être simplement expliquée en suivant ces 2 lois dans votre code :

1. **Vous architectez votre logiciel à partir de fonctions pures et isolées**
2. **Vous évitez la mutabilité et les effets secondaires**

Approfondissons cela.

## 1. Architectez votre logiciel à partir de fonctions pures et isolées

Commençons par le début, 

Le code fonctionnel utilise largement quelques choses :

### Fonctions pures

La même entrée donne toujours la même sortie (**idempotence**), et n'a pas d'effets secondaires. 

Une **fonction idempotente** est une fonction qui, lorsque vous réappliquez les résultats à cette fonction à nouveau, ne produit pas un résultat différent.

```javascript
/// Exemple de quelques utilisations de Math.abs
Math.abs('-1');     // 1
Math.abs(-1);       // 1
Math.abs(null);     // 0


Math.abs(Math.abs(Math.abs('-1')));           // Retourne toujours 1
Math.abs(Math.abs(Math.abs(Math.abs('-1')))); // Retourne toujours 1
```

Les effets secondaires se produisent lorsque votre code interagit avec (lit ou écrit dans) un état mutable externe. 

L'état mutable externe est littéralement tout ce qui se trouve en dehors de la fonction et qui changerait les données dans votre programme. Définir une fonction ? Définir un booléen sur un objet ? Supprimer des propriétés sur un objet ? Tous les changements d'état en dehors de votre fonction.

```javascript
function setAvailability(){
	available = true;
}
```

### Fonctions isolées

Il n'y a pas de dépendance à l'état du programme, ce qui inclut les variables globales sujettes à changement. 

Nous en discuterons plus en détail, mais tout ce dont vous avez besoin doit être passé à la fonction en tant qu'argument. Cela rend vos dépendances (les choses dont la fonction a besoin pour faire son travail) beaucoup plus claires à voir, et plus découvrables.

Ok, alors pourquoi faites-vous les choses de cette manière ?

Je sais que cela semble être beaucoup de restrictions qui rendent votre code inutilement difficile. Mais ce ne sont pas des restrictions, ce sont des directives qui essaient de vous empêcher de tomber dans des schémas qui mènent couramment à des bugs.

Lorsque vous ne changez pas l'exécution de votre code, en bifurquant votre code avec des `if` basés sur l'état des `Boolean`, étant définis par plusieurs endroits dans votre code, vous rendez le code plus prévisible et il est plus facile de raisonner sur ce qui se passe.

Lorsque vous suivez le paradigme fonctionnel, vous constaterez que l'ordre d'exécution de votre code n'a pas autant d'importance. 

Cela a plusieurs avantages - l'un étant, par exemple, que pour reproduire un bug, vous n'avez pas besoin de savoir exactement quel était l'état de chaque `Boolean` et `Object` avant d'exécuter vos fonctions. Tant que vous avez une pile d'appels (vous savez quelle fonction est en cours d'exécution/a été exécutée avant vous), elle peut reproduire les bugs et les résoudre plus facilement.

### Réutilisabilité grâce aux fonctions d'ordre supérieur

Les fonctions qui peuvent être assignées à une variable, passées dans une autre fonction, ou retournées par une autre fonction comme n'importe quelle autre valeur normale, sont appelées **fonctions de première classe**. 

En JavaScript, toutes les fonctions sont des fonctions de première classe. Les fonctions qui ont un statut de première classe nous permettent de créer des **fonctions d'ordre supérieur**.

Une **fonction d'ordre supérieur** est une fonction qui prend une fonction comme argument, retourne une fonction, ou les deux ! Vous pouvez utiliser des fonctions d'ordre supérieur pour éviter de vous répéter dans votre code.

Quelque chose comme ceci :

```js
// Voici un exemple non fonctionnel
const ages = [12,32,32,53]
for (var i=0; i < ages.length; i++) {
    finalAge += ages[i];
}

// Voici un exemple fonctionnel
const ages = [12,32,32,53]
const totalAge = ages.reduce( function(firstAge, secondAge){
    return firstAge + secondAge;
})


```

Les fonctions JavaScript intégrées `Array` `.map`, `.reduce`, et `.filter` acceptent toutes une fonction. Elles sont d'excellents exemples de **fonctions d'ordre supérieur**, car elles itèrent sur un tableau et appellent la fonction qu'elles ont reçue pour chaque élément du tableau.

Vous pourriez donc faire :

```js
// Voici un exemple de chaque
const array = [1, 2, 3];

const mappedArray = array.map(function(element){
    return element + 1;
});
// mappedArray est [2, 3, 4]

const reduced = array.reduce(function(firstElement, secondElement){
	return firstElement + secondElement;
});
// reduced est 6

const filteredArray = array.filter(function(element){
    return element !== 1;
});
// filteredArray est [2, 3]
```

Passer les résultats de fonctions dans d'autres fonctions, ou même passer les fonctions elles-mêmes, est extrêmement courant dans le code fonctionnel. J'ai inclus cette brève explication en raison de la fréquence à laquelle elle est utilisée.

Ces fonctions sont également souvent utilisées car elles ne changent pas la fonction sous-jacente (pas de changement d'état) mais opèrent sur une copie du `array`.

## 2. Éviter la mutabilité et les effets secondaires

La deuxième règle est d'éviter la mutabilité - nous en avons brièvement parlé plus tôt, lorsque nous avons parlé de limiter les changements à l'état mutable externe - et les effets secondaires.

Mais ici, nous allons approfondir. En gros, cela se résume à ceci : ne changez pas les choses ! Une fois que vous l'avez fait, il est **immuable** (inchangé au fil du temps).

```js
var ages = [12,32,32,53]
ages[1] = 12;  // non !
ages = [];     // non !
ages.push("2") // non !
```

Si quelque chose doit changer pour vos structures de données, faites des changements sur une copie.

```js
const ages = [12,32,32,53]
const newAges = ages.map(function (age){
    if (age == 12) { return 20; }
    else { return age; }
})
```

Pouvez-vous voir que j'ai fait une copie avec mes changements nécessaires ?

Cet élément est répété encore et encore. Ne changez pas l'état ! 

Si nous suivons cette règle, nous utiliserons largement `const` pour savoir que les choses ne changeront pas. Mais cela doit aller plus loin. Que pensez-vous de ce qui suit ?

```js
const changingObject = {
    willChange: 10
}

changingObject.willChange = 10;  // non !
delete obj.willChange            // non !

```

Les propriétés de `changingObject` doivent être complètement verrouillées. `const` ne vous protégera que de l'initialisation sur la variable.

```js
const obj = Object.freeze({
    cantChange: 'Locked' }) // La fonction `freeze` impose l'immuabilité.

obj.cantChange = 0      // Ne change pas l'objet !
delete obj.cantChange   // Ne change pas l'objet !
obj.addProp = "Gotcha!" // Ne change pas l'objet !
```

Si nous ne pouvons pas changer l'état des variables globales, alors nous devons nous assurer :

* Nous déclarons les arguments de fonction - tout calcul à l'intérieur d'une fonction dépend uniquement des arguments, et non de tout objet ou variable global.
* Nous ne modifions pas une variable ou un objet - créez de nouvelles variables et objets et retournez-les si nécessaire à partir d'une fonction.

### Rendez votre code référentiellement transparent

Lorsque vous suivez la règle de ne jamais changer l'état, votre code devient **référentiellement transparent**. C'est-à-dire que vos appels de fonction peuvent être remplacés par les valeurs qu'ils représentent sans affecter le résultat.

En tant qu'exemple simple pour vérifier si votre code est **référentiellement transparent**, regardez l'extrait de code ci-dessous :

```js
const greetAuthor = function(){
    return 'Hi Kealan'
}
```

Vous devriez pouvoir simplement remplacer cet appel de fonction par la `string` qu'il retourne, et n'avoir aucun problème. 

La programmation fonctionnelle avec des expressions référentiellement transparentes vous fait commencer à penser à votre code différemment si vous êtes habitué à l'**orientation objet**.

Mais pourquoi ?

Parce qu'au lieu d'objets et d'états mutables dans votre code, vous commencez à avoir des fonctions pures, sans changement d'état. Vous comprenez très clairement ce que vous attendez de votre fonction pour qu'elle retourne (car elle ne change jamais, alors qu'elle pourrait normalement retourner différents types de données en fonction de l'état en dehors de la fonction).

Cela peut vous aider à mieux comprendre le flux, à comprendre ce qu'une fonction fait simplement en la parcourant, et à être plus rigoureux avec les responsabilités de chaque fonction pour obtenir de meilleurs systèmes découplés.

Vous pouvez en apprendre davantage sur la transparence référentielle [ici](https://medium.com/@olxc/referential-transparency-93352c2dd713).

### Ne pas itérer

Espérons que, si vous avez prêté attention jusqu'à présent, vous voyez que nous ne changeons pas d'état. Donc, pour être clair, les boucles `for` sont exclues :

```js
for(let i = 0; i < arr.length; i++) {
    total += arr[i];
}
```

Parce que nous changeons l'état d'une variable. Utilisez plutôt la fonction d'ordre supérieur `map`.

## Plus de fonctionnalités de la programmation fonctionnelle

J'espère qu'à ce stade, vous avez une bonne vue d'ensemble de ce qu'est et n'est pas le code fonctionnel. Mais il y a quelques concepts finaux utilisés largement dans le code fonctionnel que nous devons couvrir. 

Dans tout le code fonctionnel que j'ai lu, ces concepts et outils sont les plus utilisés, et nous devons les couvrir pour obtenir nos connaissances de base.

Alors, c'est parti.

## Récursivité en programmation fonctionnelle

Il est possible en JavaScript d'appeler une fonction à partir de la fonction elle-même.

Ce que nous pourrions toujours faire :

```javascript
function recurse(){
    recurse();
}
```

Le problème avec cela est que ce n'est pas utile. Cela s'exécutera éventuellement jusqu'à ce qu'il fasse planter votre navigateur. Mais l'idée de la récursivité est qu'une fonction s'appelle elle-même à partir de son corps de fonction. Alors, regardons un exemple plus utile :

```js
function recurse(start, end){
    if (start == end) {
        console.log(end)
        return;
    } else {
        console.log(start)
        return recurse(start+1, end)
    }
}

recurse(1, 10);
// 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

Cet extrait de code comptera à partir de l'argument `start` jusqu'à l'argument `end`. Et il le fait en appelant sa propre fonction à nouveau.

L'ordre de cela ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-135.png)
_Un exemple de pile d'appels pour cette fonction récursive._

Ajoutez un débogueur à l'intérieur des blocs if pour suivre cela si cela n'a pas de sens pour vous. La récursivité est un outil que vous pouvez utiliser pour itérer en programmation fonctionnelle.

Qu'est-ce qui rend le premier exemple et le deuxième exemple différents ? Le deuxième a ce que nous appelons **"un cas de base"**. Un cas de base permet à la fonction de finalement arrêter de s'appeler elle-même à l'infini. Lorsque `start` est égal à `end`, nous pouvons arrêter la récursivité. Comme nous savons que nous avons compté jusqu'à la toute fin de notre boucle.

Mais chaque appel des fonctions appelle à nouveau sa propre fonction, et ajoute à l'argument de la fonction.

L'exemple de code que je viens d'inclure pour l'exemple de comptage n'est pas une **fonction pure**. Pourquoi ?

Parce que la `console` est un état ! Et nous avons enregistré des `string` dessus. 

Cela a été une brève introduction à la récursivité, mais n'hésitez pas à aller ici pour en apprendre davantage [ici](https://javascript.info/recursion).

### Pourquoi utiliser la récursivité ?

La récursivité nous permet d'arrêter de muter les variables d'état, pour commencer.

Il existe également certaines structures de données (structures d'arbres) qui sont plus efficaces lorsqu'elles sont résolues avec la récursivité. Elles nécessitent généralement moins de code, donc certains codeurs aiment la lisibilité de la récursivité. 

## Currying en programmation fonctionnelle

Le currying est un autre outil largement utilisé dans le code fonctionnel. L'**arité** d'une fonction fait référence au nombre d'arguments qu'elle reçoit.

```js
// Parlons arité
function arity2(arg1, arg2){}             // La fonction a une arité de 2
function arity0(){}                       // La fonction a une arité de 0
function arity2(arg1, arg2, arg3, arg4){} // La fonction a une arité de 4
```

  
**Curryfier** une fonction transforme une fonction qui a une arité de plus de 1, en 1. Elle le fait en retournant une fonction interne pour prendre l'argument suivant. Voici un exemple :

```js
function add(firstNum, secondNum){
	return firstNum + secondNum;
}

// Curryfions cette fonction

function curryAdd(firstNum){
	return function(secondNum){
            return firstNum + secondNum;
    }
}
```

  
Essentiellement, il restructure une fonction pour qu'elle prenne un argument, mais elle retourne ensuite une autre fonction pour prendre l'argument suivant, autant de fois que nécessaire. 

### Pourquoi utiliser le currying ?

Le grand avantage du currying est lorsque vous devez réutiliser la même fonction plusieurs fois mais ne changer qu'un (ou moins) des paramètres. Vous pouvez donc sauvegarder le premier appel de fonction, quelque chose comme ceci :

```js
function curryAdd(firstNum){
	return function(secondNum){
            return firstNum + secondNum;
    }
}

let add10 = curryAdd(10);
add10(2); // Retourne 12

let add20 = curryAdd(20);
add20(2); // Retourne 22
```

Le currying peut également rendre votre code plus facile à refactoriser. Vous n'avez pas à changer plusieurs endroits où vous passez les mauvais arguments de fonction - juste l'un d'eux, où vous avez lié le premier appel de fonction à l'argument incorrect.

C'est également utile si vous ne pouvez pas fournir tous les arguments à une fonction en une seule fois. Vous pouvez simplement retourner la première fonction pour appeler la fonction interne lorsque vous avez tous les arguments plus tard. 

## Application partielle en programmation fonctionnelle

De manière similaire, l'application partielle signifie que vous appliquez quelques arguments à une fonction à la fois et retournez une autre fonction qui est appliquée à plus d'arguments. Voici le meilleur exemple que j'ai trouvé dans la documentation MDN :

```javascript
const module = {
  height: 42,
  getComputedHeight: function(height) {
    return this.height + height;
  }
};

const unboundGetComputedHeight = module.getComputedHeight;
console.log(unboundGetComputedHeight(32)); // La fonction est invoquée dans le scope global
// sortie : NaN
// Sortie NaN car this.height est indéfini (dans le scope de window) donc fait 
// undefined + 32 qui retourne NaN

const boundGetComputedHeight = unboundGetComputedHeight.bind(module);
console.log(boundGetComputedHeight(32));
// sortie attendue : 74
```

`bind` est le meilleur exemple d'une application partielle. Pourquoi ?

Parce que nous retournons une fonction interne qui est assignée à `boundGetComputedHeight` qui est appelée, avec le scope `this` correctement configuré et un nouvel argument passé plus tard. Nous n'avons pas assigné tous les arguments à la fois, mais nous avons plutôt retourné une fonction pour accepter le reste des arguments.

### Pourquoi utiliser l'application partielle ?

Vous pouvez utiliser l'application partielle chaque fois que vous ne pouvez pas passer tous vos arguments à la fois, mais pouvez retourner des `function`s à partir de fonctions d'ordre supérieur pour traiter le reste des arguments.

## Composition de fonctions en programmation fonctionnelle

Le dernier sujet que je pense être fondamental pour le code fonctionnel est la **composition de fonctions**.

La **composition de fonctions** nous permet de prendre deux fonctions ou plus et de les transformer en une seule fonction qui fait exactement ce que les deux fonctions (ou plus) font.

```javascript
// Si nous avons ces deux fonctions

function add10(num) {
	return num + 10;
}
function add100(num) {
    return num + 100;
}

// Nous pouvons composer ces deux fonctions en =>
function composed(num){
	return add10(add100(num));
}

composed(1) // Retourne 111
```

Vous pouvez aller plus loin et créer des fonctions pour composer un nombre quelconque de fonctions d'arité multiple ensemble si vous en avez besoin pour votre cas d'utilisation.

### Pourquoi utiliser la composition de fonctions ?

La composition vous permet de structurer votre code à partir de fonctions réutilisables, pour éviter de vous répéter. Vous pouvez commencer à traiter les fonctions comme de petits blocs de construction que vous pouvez combiner pour obtenir une sortie plus complexe. 

Celles-ci deviennent alors les "unités" ou la puissance de calcul dans vos programmes. Ce sont beaucoup de petites fonctions qui fonctionnent de manière générique, toutes composées en fonctions plus grandes pour faire le "vrai" travail. 

C'est une manière puissante d'architecturer votre code, et cela vous empêche de créer d'énormes fonctions copiées et collées avec de minuscules différences entre elles. 

Cela peut également vous aider à tester lorsque votre code n'est pas étroitement couplé. Et cela rend votre code plus réutilisable. Vous pouvez simplement changer la composition de vos fonctions ou ajouter plus de petites fonctions dans la composition, plutôt que d'avoir tout le code copié et collé dans toute la base de code (pour lorsque vous avez besoin qu'il fasse quelque chose de similaire mais pas tout à fait la même chose qu'une autre fonction).

L'exemple ci-dessous est rendu trivial pour vous aider à comprendre, mais j'espère que vous voyez la puissance de la **composition de fonctions**.

```javascript
/// Voici un exemple où nous devons copier et coller
function add50(num) {
	return num + 50;
}

// Ok. Maintenant nous devons ajouter 30. Mais nous avons toujours besoin d'ajouter 50 ailleurs
// Donc nous avons besoin d'une nouvelle fonction
function add30(num){
	return num + 30;
}

// Ugh, changement d'entreprise à nouveau
function add20(num){
	return num + 20;
}

// Chaque fois que nous devons changer la fonction même légèrement. Nous avons besoin d'une nouvelle fonction

// Utilisons la composition

// Notre petite fonction pure réutilisable
function add10(num){
	return num + 10;
}

function add50Composed(num){
	return add10(add10(add10(add10(addNum(num)))));
}

function add30Composed(num){
	return add10(add10(add10(num)));
}

function add20Composed(num){
	return add10(add10(num));
}
```

Voyez-vous comment nous avons composé de nouvelles fonctions à partir de fonctions pures plus petites ?

## Conclusion

Cet article a couvert beaucoup de choses. Mais j'espère qu'il a expliqué le code fonctionnel simplement, ainsi que certains des motifs répétitifs que vous verrez encore et encore, dans le code fonctionnel et même non fonctionnel.

Le code fonctionnel n'est pas nécessairement le meilleur, et le code orienté objet non plus. Le code fonctionnel est généralement utilisé pour des problèmes plus mathématiques comme l'analyse de données. Il est également très utile pour les systèmes en temps réel à haute disponibilité, comme les choses écrites en Erlang (un langage fonctionnel). Mais cela dépend vraiment du problème.

Je publie mes articles sur [Twitter](https://twitter.com/kealanparr). Si vous avez apprécié cet article, vous pouvez en lire plus là-bas.

## Comment en apprendre davantage

Commencez [ici](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/functional-programming/learn-about-functional-programming), avec l'introduction de freeCodeCamp à la programmation fonctionnelle avec JavaScript.

Regardez [ici](https://github.com/xgrommx/awesome-functional-programming#javascript) pour quelques bibliothèques que vous pouvez inclure et avec lesquelles jouer, pour vraiment maîtriser la programmation fonctionnelle.

Parcourez [ceci](https://github.com/leandrotk/functional-programming-learning-path) bon aperçu de nombreux concepts fonctionnels.

Enfin, [voici](https://github.com/hemanth/functional-programming-jargon) un excellent glossaire de termes fonctionnels qui brise le jargon.