---
title: Contexte d'exécution JavaScript – Comment JS fonctionne en coulisses
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-10T19:56:18.000Z'
originalURL: https://freecodecamp.org/news/execution-context-how-javascript-works-behind-the-scenes
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/header.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Contexte d'exécution JavaScript – Comment JS fonctionne en coulisses
seo_desc: 'By Victor Ikechukwu

  All JavaScript code needs to be hosted and run in some kind of environment. In most
  cases, that environment would be a web browser.

  For any piece of JavaScript code to be executed in a web browser, a lot of processes
  take place be...'
---

Par Victor Ikechukwu

Tout code JavaScript doit être hébergé et exécuté dans un environnement. Dans la plupart des cas, cet environnement est un navigateur web.

Pour qu'un code JavaScript soit exécuté dans un navigateur web, de nombreux processus se déroulent en coulisses. Dans cet article, nous allons examiner tout ce qui se passe en coulisses pour que le code JavaScript s'exécute dans un navigateur web.

Avant de plonger dans le sujet, voici quelques prérequis à connaître, car nous les utiliserons souvent dans cet article.

* **Analyseur syntaxique** : Un analyseur syntaxique est un programme qui lit votre code ligne par ligne. Il comprend comment le code correspond à la syntaxe définie par le langage de programmation et ce que le code est censé faire.
* **Moteur JavaScript** : Un moteur JavaScript est simplement un programme informatique qui reçoit le code source JavaScript et le compile en instructions binaires (code machine) qu'un CPU peut comprendre. Les moteurs JavaScript sont généralement développés par les éditeurs de navigateurs web, et chaque navigateur majeur en possède un. Parmi les exemples, on trouve le [moteur V8](https://v8.dev/) pour Google Chrome, [SpiderMonkey](https://firefox-source-docs.mozilla.org/js/index.html) pour Firefox, et [Chakra](https://en.wikipedia.org/wiki/Chakra_(JScript_engine)) pour Internet Explorer.
* **Déclarations de fonctions** : Ce sont des fonctions auxquelles un nom est assigné.

```javascript
function doSomething() { // ici "doSomething" est le nom de la fonction
  instructions; 
} 
```

* **Expressions de fonctions** : Ce sont des fonctions anonymes, c'est-à-dire des fonctions sans nom comme `js function () { instructions }`. Elles sont généralement utilisées dans des instructions, comme l'assignation d'une fonction à une variable. `let someValue = function () { instructions }`. 

Maintenant que nous avons clarifié ces points, plongeons dans le sujet.

## **Comment le code JavaScript est exécuté**

Pour ceux qui ne le savent pas, le navigateur ne comprend pas nativement le code JavaScript de haut niveau que nous écrivons dans nos applications. Il doit être converti dans un format que le navigateur et nos ordinateurs peuvent comprendre – le code machine.

Lors de la lecture du HTML, si le navigateur rencontre du code JavaScript à exécuter via une balise `<script>` ou un attribut contenant du code JavaScript comme `onClick`, il l'envoie à son moteur JavaScript.

Le moteur JavaScript du navigateur crée alors un environnement spécial pour gérer la transformation et l'exécution de ce code JavaScript. Cet environnement est connu sous le nom de **`Contexte d'exécution`**.

Le Contexte d'exécution contient le code qui est actuellement en cours d'exécution, ainsi que tout ce qui aide à son exécution.

Pendant l'exécution du Contexte d'exécution, le code spécifique est analysé par un analyseur, les variables et fonctions sont stockées en mémoire, le byte-code exécutable est généré, et le code est exécuté.

Il existe deux types de Contexte d'exécution en JavaScript :

* Contexte d'exécution global (GEC)
* Contexte d'exécution de fonction (FEC)

Examinons chacun d'eux en détail.

### **Contexte d'exécution global (GEC)**

Dès que le moteur JavaScript reçoit un fichier de script, il crée d'abord un Contexte d'exécution par défaut connu sous le nom de **`Contexte d'exécution global (GEC)`**.

Le GEC est le Contexte d'exécution de base/par défaut où tout le code JavaScript qui **n'est pas à l'intérieur d'une fonction** est exécuté.

> Pour chaque fichier JavaScript, il ne peut y avoir qu'un seul GEC.

### **Contexte d'exécution de fonction (FEC)**

Dès qu'une fonction est appelée, le moteur JavaScript crée un type différent de Contexte d'exécution connu sous le nom de Contexte d'exécution de fonction (FEC) au sein du GEC pour évaluer et exécuter le code à l'intérieur de cette fonction.

Puisque chaque appel de fonction obtient son propre FEC, il peut y avoir plus d'un FEC pendant l'exécution d'un script.

## **Comment les Contexte d'exécution sont créés ?**

Maintenant que nous savons ce que sont les Contexte d'exécution et les différents types disponibles, examinons comment ils sont créés.

La création d'un Contexte d'exécution (GEC ou FEC) se fait en deux phases :

1. Phase de création
2. Phase d'exécution

### Phase de création

Dans la phase de création, le Contexte d'exécution est d'abord associé à un Objet de Contexte d'exécution (ECO). L'Objet de Contexte d'exécution stocke de nombreuses données importantes que le code dans le Contexte d'exécution utilise pendant son exécution.

La phase de création se déroule en 3 étapes, au cours desquelles les propriétés de l'Objet de Contexte d'exécution sont définies et configurées. Ces étapes sont :

1. Création de l'Objet Variable (VO)
2. Création de la Chaîne de portée
3. Définition de la valeur du mot-clé `this`

Passons en revue chaque phase en détail.

### **Phase de création : Création de l'Objet Variable (VO)**

L'Objet Variable (VO) est un conteneur de type objet créé au sein d'un Contexte d'exécution. Il stocke les variables et les déclarations de fonctions définies au sein de ce Contexte d'exécution.

Dans le GEC, pour chaque variable déclarée avec le mot-clé `var`, une propriété est ajoutée à VO qui pointe vers cette variable et est définie sur 'undefined'.

De plus, pour chaque déclaration de fonction, une propriété est ajoutée à VO, pointant vers cette fonction, et cette propriété est stockée en mémoire. Cela signifie que toutes les déclarations de fonctions seront stockées et rendues accessibles à l'intérieur de VO, même avant que le code ne commence à s'exécuter.

Le FEC, en revanche, ne construit pas de VO. Il génère plutôt un objet de type tableau appelé objet 'argument', qui inclut tous les arguments fournis à la fonction. En savoir plus sur l'objet argument [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments).

Ce processus de stockage des variables et des déclarations de fonctions en mémoire avant l'exécution du code est connu sous le nom de **Hoisting**. Puisque c'est un concept important, nous en parlerons brièvement avant de passer à l'étape suivante.

### **Hoisting en JavaScript**

Les déclarations de fonctions et de variables sont hoistées en JavaScript. Cela signifie qu'elles sont stockées en mémoire de l'Objet Variable (VO) du Contexte d'exécution actuel et rendues disponibles au sein du Contexte d'exécution même avant le début de l'exécution du code.

#### **Hoisting de fonction**

Dans la plupart des scénarios de développement d'une application, les développeurs peuvent choisir de définir des fonctions en haut d'un script, et ne les appeler que plus tard dans le code, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/function-before-call.png)

Cependant, grâce au hoisting, l'inverse fonctionnera également. Nous pouvons appeler des fonctions d'abord, puis les définir plus tard dans le script.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/call-before-function.png)

Dans le code ci-dessus, la déclaration de la fonction `getAge` sera stockée en mémoire de VO, la rendant disponible pour une utilisation même avant qu'elle ne soit définie.

#### **Hoisting de variable**

Les variables initialisées avec le mot-clé `var` sont stockées en mémoire de l'Objet Variable (VO) du Contexte d'exécution actuel en tant que propriété, et initialisées avec la valeur `undefined`. Cela signifie que, contrairement aux fonctions, essayer d'accéder à la valeur de la variable avant qu'elle ne soit définie donnera `undefined`.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/log-before-variable.png)

#### **Règles de base du Hoisting**

Le hoisting ne fonctionne que pour les déclarations de fonctions, pas pour les expressions. Voici un exemple d'expression de fonction où l'exécution du code échouera.

```javascript
getAge(1990); 
var getAge = function (yearOfBirth) {
  console.log(new Date().getFullYear - yearOfBirth) 
};
```

L'exécution du code échoue, car avec les expressions de fonction, `getAge` sera hoisté en tant que variable et non en tant que fonction. Et avec le hoisting de variable, sa valeur sera définie sur `undefined`. C'est pourquoi nous obtenons l'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/getAge-error.png)

De plus, le hoisting de variable ne fonctionne pas pour les variables initialisées avec les mots-clés `let` ou `const`. Essayer d'accéder à une variable avant sa déclaration et d'utiliser les mots-clés `let` et `const` pour la déclarer plus tard entraînera une erreur `ReferenceError`. 

Dans ce cas, elles seront hoistées mais ne seront pas assignées avec la valeur par défaut `undefined`. `js console.log(name); let name = "Victor";` générera l'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/name-not-defined-error.png)

### **Phase de création : Création de la Chaîne de portée**

Après la création de l'Objet Variable (VO) vient la création de la Chaîne de portée en tant qu'étape suivante dans la phase de création d'un Contexte d'exécution.

La portée en JavaScript est un mécanisme qui détermine à quel point un morceau de code est accessible à d'autres parties de la base de code. La portée répond aux questions : d'où un morceau de code peut-il être accessible ? D'où ne peut-il pas être accessible ? Qu'est-ce qui peut y accéder, et qu'est-ce qui ne peut pas ?

Chaque Contexte d'exécution de fonction crée sa propre portée : l'espace/environnement où les variables et fonctions qu'il définit peuvent être accessibles via un processus appelé Scoping.

Cela signifie la position de quelque chose au sein d'une base de code, c'est-à-dire où un morceau de code est situé.

Lorsque qu'une fonction est définie dans une autre fonction, la fonction interne a accès au code défini dans celle de la fonction externe, et à celui de ses parents. Ce comportement est appelé **portée lexicale**.

Cependant, la fonction externe n'a pas accès au code à l'intérieur de la fonction interne.

Ce concept de portée soulève un phénomène associé en JavaScript appelé closures. Ce sont des fonctions internes qui ont toujours accès au code associé aux fonctions externes, même après que l'exécution des fonctions externes soit terminée. Vous pouvez en apprendre plus sur les closures [ici](https://www.freecodecamp.org/news/scope-and-closures-in-javascript/).

Regardons quelques exemples pour mieux comprendre :

![first-scope.png](https://www.freecodecamp.org/news/content/images/2022/02/first-scope.png)

* À droite se trouve la Portée Globale. C'est la portée par défaut créée lorsqu'un script `.js` est chargé et est accessible depuis toutes les fonctions dans tout le code.
* La boîte rouge est la portée de la fonction `first`, qui définit la variable `b = 'Hello!'` et la fonction `second`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/second-scope.png)

* En vert se trouve la portée de la fonction `second`. Il y a une instruction `console.log` qui doit imprimer les variables `a`, `b` et `c`.

Maintenant, les variables `a` et `b` ne sont pas définies dans la fonction `second`, seulement `c`. Cependant, grâce à la portée lexicale, elle a accès à la portée de la fonction dans laquelle elle se trouve et à celle de ses parents.

En exécutant le code, le moteur JS ne trouvera pas la variable `b` dans la portée de la fonction `second`. Il remonte donc dans la portée de ses parents, en commençant par la fonction `first`. Là, il trouve la variable `b = 'Hello'`. Il retourne à la fonction `second` et résout la variable `b` là-bas avec elle.

Même processus pour la variable `a`. Le moteur JS remonte à travers la portée de tous ses parents jusqu'à la portée du GEC, résolvant sa valeur dans la fonction `second`.

Cette idée du moteur JavaScript parcourant les portées des contextes d'exécution dans lesquels une fonction est définie afin de résoudre les variables et fonctions invoquées dans celles-ci est appelée la **chaîne de portée**.

![Chaîne de portée](https://www.freecodecamp.org/news/content/images/2022/02/scope-chain.png)

Ce n'est que lorsque le moteur JS ne peut pas résoudre une variable dans la chaîne de portée qu'il arrête l'exécution et génère une erreur.

Cependant, cela ne fonctionne pas dans l'autre sens. C'est-à-dire que la portée globale n'aura jamais accès aux variables de la fonction interne à moins qu'elles ne soient `retournées` par la fonction.

La chaîne de portée fonctionne comme un miroir sans tain. Vous pouvez voir l'extérieur, mais les gens de l'extérieur ne peuvent pas vous voir.

Et c'est pourquoi la flèche rouge dans l'image ci-dessus pointe vers le haut, car c'est la seule direction que prend la chaîne de portée.

### Phase de création : Définition de la valeur du mot-clé "this"

L'étape suivante et finale après la portée dans la phase de création d'un Contexte d'exécution est la définition de la valeur du mot-clé `this`.

Le mot-clé `this` en JavaScript fait référence à la portée à laquelle appartient un Contexte d'exécution.

Une fois la chaîne de portée créée, la valeur de `'this'` est initialisée par le moteur JS.

##### **`"this"` dans le Contexte Global**

Dans le GEC (en dehors de toute fonction et objet), `this` fait référence à l'objet global — qui est l'objet `window`.

Ainsi, les déclarations de fonctions et les variables initialisées avec le mot-clé `var` sont assignées en tant que propriétés et méthodes à l'objet global — l'objet `window`.

Cela signifie que déclarer des variables et des fonctions en dehors de toute fonction, comme ceci :

```javascript
var occupation = "Frontend Developer"; 

function addOne(x) { 
    console.log(x + 1) 
}
```

Est exactement la même chose que :

```javascript
window.occupation = "Frontend Developer"; 
window.addOne = (x) => { 
console.log(x + 1)
};
```

Les fonctions et variables dans le GEC sont attachées en tant que méthodes et propriétés à l'objet window. C'est pourquoi le snippet ci-dessous retournera vrai.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/variables-attached-as-properties-to-the-global-object.png)

##### **`"this"` dans les Fonctions**

Dans le cas du FEC, il ne crée pas l'objet `this`. Il obtient plutôt accès à celui de l'environnement dans lequel il est défini.

Ici, ce sera l'objet `window`, car la fonction est définie dans le GEC :

```javascript
var msg = "I will rule the world!"; 

function printMsg() { 
    console.log(this.msg); 
} 

printMsg(); // logs "I will rule the world!" to the console.
```

Dans les objets, le mot-clé `this` ne pointe pas vers le GEC, mais vers l'objet lui-même. Faire référence à `this` au sein d'un objet sera la même chose que :

`theObject.thePropertyOrMethodDefinedInIt;`

Considérez l'exemple de code ci-dessous :

```js
var msg = "I will rule the world!"; 
const Victor = {
    msg: "Victor will rule the world!", 
    printMsg() { console.log(this.msg) }, 
}; 

Victor.printMsg(); // logs "Victor will rule the world!" to the console.
```

Le code journalise `"Victor will rule the world!"` dans la console, et non `"I will rule the world!"` car dans ce cas, la valeur du mot-clé `this` auquel la fonction a accès est celle de l'objet dans lequel elle est définie, et non l'objet global.

Avec la valeur du mot-clé `this` définie, toutes les propriétés de l'Objet de Contexte d'exécution ont été définies. Cela marque la fin de la phase de création, et le moteur JS passe à la phase d'exécution.

### **La Phase d'exécution**

Enfin, juste après la phase de création d'un Contexte d'exécution vient la phase d'exécution. C'est l'étape où l'exécution réelle du code commence.

Jusqu'à ce point, le VO contenait des variables avec les valeurs `undefined`. Si le code est exécuté à ce stade, il est certain de retourner des erreurs, car nous ne pouvons pas travailler avec des valeurs indéfinies. 

À ce stade, le moteur JavaScript relit le code dans le Contexte d'exécution actuel, puis met à jour le VO avec les valeurs réelles de ces variables. Ensuite, le code est analysé par un analyseur, est transcrit en byte-code exécutable, et est finalement exécuté.

## **Pile d'exécution JavaScript**

La Pile d'exécution, également connue sous le nom de **Pile d'appels**, suit tous les Contexte d'exécution créés pendant le cycle de vie d'un script.

JavaScript est un langage à thread unique, ce qui signifie qu'il est capable d'exécuter une seule tâche à la fois. Ainsi, lorsque d'autres actions, fonctions et événements se produisent, un Contexte d'exécution est créé pour chacun de ces événements. En raison de la nature à thread unique de JavaScript, une pile de contextes d'exécution empilés à exécuter est créée, connue sous le nom de `Pile d'exécution`.

Lorsque les scripts se chargent dans le navigateur, le Contexte global est créé comme contexte par défaut où le moteur JS commence à exécuter le code et est placé au bas de la pile d'exécution.

Le moteur JS recherche ensuite les appels de fonction dans le code. Pour chaque appel de fonction, un nouveau FEC est créé pour cette fonction et est placé au-dessus du Contexte d'exécution actuellement en cours d'exécution.

Le Contexte d'exécution au sommet de la pile d'exécution devient le Contexte d'exécution actif et sera toujours exécuté en premier par le moteur JS.

Dès que l'exécution de tout le code au sein du Contexte d'exécution actif est terminée, le moteur JS retire ce contexte d'exécution de fonction particulier de la pile d'exécution, passe au suivant en dessous, et ainsi de suite.

Pour comprendre le processus de fonctionnement de la pile d'exécution, considérons l'exemple de code ci-dessous :

```javascript
var name = "Victor";

function first() {
  var a = "Hi!";
  second();
  console.log(`${a} ${name}`);
}

function second() {
  var b = "Hey!";
  third();
  console.log(`${b} ${name}`);
}

function third() {
  var c = "Hello!";
  console.log(`${c} ${name}`);
}

first();
```

Tout d'abord, le script est chargé dans le moteur JS.

Après cela, le moteur JS crée le GEC et le place à la base de la pile d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/global-context.png)

La variable `name` est définie en dehors de toute fonction, donc elle est dans le GEC et stockée dans son VO.

Le même processus se produit pour les fonctions `first`, `second` et `third`.

Ne soyez pas confus quant à la raison pour laquelle les fonctions sont encore dans le GEC. Rappelez-vous, le GEC est seulement pour le code JavaScript (variables et fonctions) qui **ne sont pas à l'intérieur d'une fonction**. Parce qu'elles n'ont pas été définies dans une fonction, les déclarations de fonctions sont dans le GEC. Cela a du sens maintenant 😃 ?

Lorsque le moteur JS rencontre l'appel de la fonction `first`, un nouveau FEC est créé pour elle. Ce nouveau contexte est placé au-dessus du contexte actuel, formant la soi-disant `Pile d'exécution`.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/execution-context-1.png)

Pendant la durée de l'appel de la fonction `first`, son Contexte d'exécution devient le contexte actif où le code JavaScript est d'abord exécuté.

Dans la fonction `first`, la variable `a = 'Hi!'` est stockée dans son FEC, et non dans le GEC.

Ensuite, la fonction `second` est appelée à l'intérieur de la fonction `first`.

L'exécution de la fonction `first` sera mise en pause en raison de la nature à thread unique de JavaScript. Elle doit attendre jusqu'à ce que son exécution, c'est-à-dire la fonction `second`, soit complète.

Encore une fois, le moteur JS configure un nouveau FEC pour la fonction `second` et le place au sommet de la pile, en faisant le contexte actif.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/execution-context-2.png)

La fonction `second` devient le contexte actif, la variable `b = 'Hey!';` est stockée dans son FEC, et la fonction `third` est invoquée à l'intérieur de la fonction `second`. Son FEC est créé et placé au sommet de la pile d'exécution.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/execution-context-3.png)

À l'intérieur de la fonction `third`, la variable `c = 'Hello!'` est stockée dans son FEC et le message `Hello! Victor` est journalisé dans la console.

Ainsi, la fonction a accompli toutes ses tâches et nous disons qu'elle `retourne`. Son FEC est retiré du sommet de la pile et le FEC de la fonction `second` qui a appelé la fonction `third` redevient le contexte actif.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/execution-context-2-1.png)

De retour dans la fonction `second`, le message `Hey! Victor` est journalisé dans la console. La fonction termine sa tâche, `retourne`, et son Contexte d'exécution est retiré de la pile d'appels.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/execution-context-1-1.png)

Lorsque la première fonction est complètement exécutée, la pile d'exécution de la première fonction est retirée de la pile. Ainsi, le contrôle revient au GEC du code.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/global-context-1.png)

Et enfin, lorsque l'exécution de l'ensemble du code est terminée, le moteur JS retire le GEC de la pile actuelle.

## **Contexte d'exécution global VS. Contexte d'exécution de fonction en JavaScript**

Puisque vous avez lu jusqu'à cette section, résumons les points clés entre le GEC et le FEC avec le tableau ci-dessous.

<table style="max-width: 700px; background-color: rgb(241, 241, 241); border-collapse: collapse; border-spacing: 0px; width: 700px; margin-bottom: 20px; color: rgb(51, 51, 51); font-family: source-code-pro, Consolas, monaco, monospace; font-size: 20.25px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><thead style="font-family: futura-pt, Helvetica, Arial, sans-serif; text-transform: uppercase; font-weight: bold; text-rendering: optimizelegibility; letter-spacing: 0.1em; font-size: 1em;"><tr><th style="padding: 8px; line-height: 20px; text-align: left; vertical-align: bottom; border-top: 0px; font-weight: bold;">CONTEXTE D'EXÉCUTION GLOBAL</th><th style="padding: 8px; line-height: 20px; text-align: left; vertical-align: bottom; border-top: 0px; font-weight: bold;">Contexte d'exécution de fonction</th></tr></thead><tbody><tr><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Crée un Objet Variable Global qui stocke les déclarations de fonctions et de variables.</td><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Ne crée pas d'Objet Variable Global. Crée plutôt un objet argument qui stocke tous les arguments passés à la fonction.</td></tr><tr><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Crée l'objet `this` qui stocke toutes les variables et fonctions dans la portée globale en tant que méthodes et propriétés.</td><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Ne crée pas l'objet `this`, mais a accès à celui de l'environnement dans lequel il est défini. Généralement l'objet `window`.</td></tr><tr><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Ne peut pas accéder au code des Contexte de Fonction définis en son sein</td><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Grâce à la portée, a accès au code (variables et fonctions) dans le contexte dans lequel il est défini et à celui de ses parents</td></tr><tr><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Configure l'espace mémoire pour les variables et fonctions définies globalement</td><td style="padding: 8px; line-height: 20px; text-align: left; vertical-align: top; border-top: 1px solid rgb(221, 221, 221);">Configure l'espace mémoire uniquement pour les variables et fonctions définies au sein de la fonction.</td></tr></tbody></table>

## **Conclusion**

Le Contexte d'exécution de JavaScript est la base pour comprendre correctement de nombreux autres concepts fondamentaux.

Le Contexte d'exécution (GEC et FEC), et la pile d'appels sont les processus effectués en coulisses par le moteur JS qui permettent à notre code de s'exécuter.

J'espère que vous avez maintenant une meilleure compréhension de l'ordre dans lequel vos fonctions/code s'exécutent et de la manière dont le moteur JavaScript les traite.

En tant que développeur, avoir une bonne compréhension de ces concepts vous aide à :

* Obtenir une compréhension décente des tenants et aboutissants du langage.
* Avoir une bonne maîtrise des concepts sous-jacents/centraux d'un langage.
* Écrire un code propre, maintenable et bien structuré, introduisant moins de bugs en production.

Tout cela fera de vous un meilleur développeur dans l'ensemble.

J'espère que vous avez trouvé cet article utile. N'hésitez pas à le partager avec vos amis et votre réseau, et n'hésitez pas à me connecter sur [Twitter](https://twitter.com/Victor_codejs) et mon [blog](https://vickyikechukwu.hashnode.dev/) où je partage une large gamme d'articles et de ressources éducatifs gratuits. Cela me motive vraiment à publier plus.

Merci d'avoir lu, et bon codage !