---
title: Comment et pourquoi utiliser la programmation fonctionnelle en JavaScript moderne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T16:21:17.000Z'
originalURL: https://freecodecamp.org/news/how-and-why-to-use-functional-programming-in-modern-javascript-fda2df86ad1b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*lT-xzWoNJwX_yPIi
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Comment et pourquoi utiliser la programmation fonctionnelle en JavaScript
  moderne
seo_desc: 'By PALAKOLLU SRI MANIKANTA

  In this article, you will get a deep understanding of functional programming and
  its benefits.

  Introduction To Functional Programming

  Functional programming (FP) is a type of paradigm or pattern in computer science.
  Everyth...'
---

Par PALAKOLLU SRI MANIKANTA

Dans cet article, vous obtiendrez une compréhension approfondie de la programmation fonctionnelle et de ses avantages.

## Introduction à la programmation fonctionnelle

La programmation fonctionnelle (FP) est un type de paradigme ou de modèle en informatique. Tout est fait à l'aide de fonctions en FP et les blocs de construction de base sont uniquement des fonctions.

Les langages de programmation qui supportent purement la programmation fonctionnelle sont —

1. Haskell
2. Closure
3. Scala
4. SQL

Certains des langages de programmation qui supportent la programmation fonctionnelle ainsi que d'autres paradigmes de programmation sont —

1. Python
2. Javascript
3. C++
4. Ruby

Puisque le nom dit fonctionnel, la plupart des programmeurs pensent aux fonctions mathématiques. Ce n'est pas le cas avec FP. Ce n'est qu'une abstraction pour résoudre des problèmes complexes du monde réel de manière facile et efficace.

Avant l'ère de la programmation orientée objet, l'industrie du logiciel dépendait entièrement de la programmation fonctionnelle. Ce paradigme a dominé l'industrie du logiciel pendant quelques décennies. Il y a quelques problèmes avec la programmation fonctionnelle, et c'est pourquoi ils sont passés au paradigme orienté objet. Les problèmes avec FP seront discutés plus tard dans cet article.

C'est tout pour l'introduction à la programmation fonctionnelle. Maintenant, tout d'abord, nous devons apprendre ce qu'est une fonction.

### Fonctions

Avant de révéler la définition réelle, je veux expliquer une situation pour savoir où utiliser réellement FP. Supposons que vous écrivez du code pour construire une application. Dans votre parcours de développement, vous voulez réutiliser le code de quelques lignes (100) à différents endroits. Pour votre application, les fonctions sont utiles. Nous pouvons écrire des fonctions à un endroit et nous pourrons accéder à ces fonctions de n'importe où dans le programme. La programmation fonctionnelle a les caractéristiques suivantes —

1. Réduit la redondance du code.
2. Améliore la modularité.
3. Nous aide à résoudre des problèmes complexes.
4. Augmente la maintenabilité.

**Regardons la définition réelle d'une fonction :**

> Une fonction est un bloc de code spécifié qui est utilisé pour effectuer une tâche spécifique dans le programme.

Les types de fonctions les plus populaires sont —

1. Fonctions générales
2. Fonctions fléchées
3. Fonctions anonymes

### Fonctions générales

Les fonctions générales ne sont rien d'autre que les fonctions qui sont assez souvent utilisées par le programmeur pour effectuer une tâche spécifique. La syntaxe pour déclarer une fonction générale en Javascript est :

```
function functionName(parameters) {  // code à exécuter}
```

**function —** C'est un mot-clé nécessaire pour déclarer une fonction.

**functionName —** Il peut être nommé en fonction du travail de la fonction.

**parameters —** Nous pouvons passer n'importe quel nombre de paramètres à une fonction.

> Les fonctions déclarées ne sont pas exécutées immédiatement. Elles sont « sauvegardées pour une utilisation ultérieure » et seront exécutées plus tard, lorsqu'elles sont invoquées (appelées).

Nous devons appeler la fonction lorsque nous voulons exécuter ce morceau de code qui est retourné dans une fonction.

Les fonctions générales sont classées comme suit —

### Fonctions sans argument

Nous n'avons pas besoin de passer d'arguments à la fonction.

```
// Déclaration de la fonction
```

```
function sayHello(){   alert('Bonjour...!');}
```

```
// Appel de la fonction
sayHello()
```

Lorsque nous appelons la fonction sayHello(), elle produira le message d'alerte Bonjour.

### Fonctions avec arguments

Dans ce type de fonctions, nous passerons des arguments.

**Exemple**

```
// Déclaration d'une fonction
```

```
function add(num1, num2){   return num1 + num2;}
```

```
// Appel de la fonction
```

```
var result = add(7, 11);
```

```
console.log(result);
```

Les arguments qui sont passés lors de la déclaration d'une fonction, c'est-à-dire (num1, num2), sont appelés **Paramètres Formels**.

Les arguments qui sont passés lors de l'appel d'une fonction, c'est-à-dire (7, 11), sont appelés **Paramètres Réels**.

Une fonction retourne généralement une valeur, et pour retourner cette valeur, nous devons utiliser le mot-clé **return**. Lorsqu'une fonction retourne une valeur, cela signifie qu'elle n'imprime aucune sortie pour nous, elle retourne simplement la sortie finale. C'est notre responsabilité d'imprimer ce résultat. Dans le programme ci-dessus, la fonction retourne la valeur et je passe cette valeur à une variable nommée 'result'. Maintenant, la fonction passera le résultat à la variable 'result'.

## La particularité des fonctions JavaScript

Si vous passez plus d'arguments que le nombre déclaré, vous n'obtiendrez aucune erreur. Mais dans d'autres langages de programmation comme Python, C, C++, Java, etc., nous obtiendrons une erreur. JavaScript considérera en fonction de leurs besoins.

**Exemple**

```
// Appel de la fonction avec plus d'arguments que le nombre déclaré
```

```
var result1 = add(2, 4, 6);console.log(result1);
```

```
var result2 = add(2);console.log(result2);
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/ucOi2Z4tT9lDi5N0PgIHbaJ2NfDSuNIJVBSE)
_Sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

Si vous passez moins d'arguments que le nombre déclaré, vous n'obtiendrez également aucune erreur. Mais nous ne pouvons pas prédire la sortie du programme car, en fonction de la fonctionnalité de votre fonction, la sortie sera produite.

### Fonction à arguments variables

Le plus grand avantage des fonctions JavaScript est que nous pouvons passer n'importe quel nombre d'arguments à la fonction. Cette fonctionnalité aide les développeurs à travailler de manière plus efficace et cohérente.

**Exemple**

```
// Création d'une fonction pour calculer la somme de tous les nombres d'arguments
```

```
function sumAll(){
```

```
let sum = 0;
```

```
for(let i=0;i<arguments.length;i++){      sum = sum + arguments[i];}
```

```
return sum;
```

```
}
```

```
// Appel de la fonction sumAll
```

```
sumAll();
```

```
sumAll(1,2,3,12,134,3234,4233,12,3243);
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/eDW47gBu-rgnJm0QmZ9ZSNp14AUPkvNa4ngl)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

C'est tout sur les fonctions générales qui sont utilisées pour effectuer notre tâche complexe de manière simple. Maintenant, discutons de certaines fonctions avancées introduites dans ES6 appelées **Fonctions Fléchées**.

### Fonctions Fléchées

Une **expression de fonction fléchée** est une alternative syntaxiquement compacte à une expression de fonction régulière. Elle n'a pas ses propres liaisons avec les mots-clés **this**, **super**, **arguments** ou **new.target**. Les expressions de fonction fléchée ne conviennent pas comme méthodes. Elles ne peuvent pas être utilisées comme constructeurs.

> L'une des fonctionnalités les plus appréciées dans Es6 sont les fonctions fléchées. Cette fonction fléchée aide les développeurs à gagner du temps et à simplifier la portée des fonctions.

La syntaxe pour la fonction fléchée est :

```
const functionName = (parameters) => {  // code à exécuter}
```

```
           (OU)
```

```
var functionName = (parameters) => {  // code à exécuter}
```

```
           (OU)
```

```
let functionName = (parameters) => {  // code à exécuter}
```

### Exemples de Fonctions Fléchées

**Exemple 1**

Création d'une fonction fléchée pour dire un message de bienvenue aux utilisateurs.

```
// Création d'une fonction de bienvenue
```

```
let sayHello = () => {   return 'Bienvenue dans le monde JavaScript...!';}
```

```
// Appel de la fonction
```

```
console.log(sayHello())
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/-1hdRxk3qIX0X72UJBI1q1osAgnaMi4VZvQs)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

**Exemple 2**

Dans cet exemple, nous créons une fonction fléchée pour générer le plus grand de tous les nombres qui sont passés en argument.

```
let maxNumber = (a,b,c,d) => {
```

```
   if(a > b && a > c && a > d)       return a;   else if(b > a && b > c && b>d)       return b;   else if(c > a && c > b && c > d)       return c;   else       return d;}
```

```
// Appel de la fonction
```

```
console.log(maxNumber(1,2,4,3));
```

**Sortie :**

![Image](https://cdn-media-1.freecodecamp.org/images/3t84j6xz-SQsRP9s1QoahCDkob9ppNniDtJo)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

### Combinaison d'arguments variables avec des fonctions fléchées

Puisque nous travaillons avec une fonction fléchée, elle ne supporte pas le tableau d'arguments par défaut comme une fonction générale. C'est notre responsabilité de déclarer explicitement qu'elle supporte un nombre variable d'arguments.

**Exemple 3**

```
let varArgSum = (...args) => {   let sum = 0;
```

```
 for(let i=0;i<args.length;i++){      sum = sum + args[i];}
```

```
return sum;
```

```
}
```

```
// Appel de la fonction
```

```
console.log(varArgSum());
```

```
console.log(varArgSum(1,2,3,4,5,6,7,8,9,10));
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/ckNYIRsu7dpCk6iBb26AuqZMGYpa9DePLxSl)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

C'est ainsi que nous pouvons combiner un nombre variable d'arguments avec des fonctions fléchées. Maintenant, discutons des fonctions anonymes en JavaScript.

### Fonctions Anonymes

Une fonction anonyme est simplement une fonction sans nom. Le but d'utiliser une fonction anonyme est d'effectuer une certaine tâche et cette tâche n'est plus requise pour le programme. Généralement, les fonctions anonymes sont déclarées dynamiquement à l'exécution.

> Les fonctions anonymes sont appelées une seule fois dans un programme.

**Exemple :**

```
// Travailler avec une fonction anonyme
```

```
var a = 10;  // Variable de portée globale.
```

```
// création d'une fonction(function() {
```

```
  console.log("Bienvenue dans le monde des fonctions anonymes");
```

```
  var b = 20;  // b est une variable de portée locale.
```

```
  var c = a+b; // c est une variable de portée locale    //a peut être utilisé car il est dans la portée globale
```

```
  console.log("L'addition de deux nombres est : "+c);})();
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/mgfAMM-0fwKX62MXgUouc2Bt--zpNHAlaiJh)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

C'est le concept des fonctions anonymes. Je pense que je l'ai expliqué de manière simple et facile.

### Fonctions d'Ordre Supérieur

Une fonction d'ordre supérieur est une fonction qui prend des fonctions comme argument ou qui retourne une autre fonction comme résultat.

Le meilleur exemple de fonctions d'ordre supérieur en JavaScript est celui de Array.map(), Array.reduce(), Array.filter().

**Exemple 1 : Array.map()**

```
// travailler avec Array.map()
```

```
let myNumberArray = [4,9,16,25,36,49];
```

```
let mySquareRootArray = myNumberArray.map(Math.sqrt);
```

```
console.log(mySquareRootArray);
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/KPgAtGbvzMd4ZEiHjTXcwzMH4Lo5xfLXDVd1)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

**Exemple 2 : Array.reduce()**

```
// travailler avec Array.reduce()
```

```
let someRandomNumbers = [24,1,23,78,93,47,86];
```

```
function getSum(total, num){  return total + num;}
```

```
let newReducedResult = someRandomNumbers.reduce(getSum);
```

```
console.log(newReducedResult);
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/HnU0h9I7jXXzPkUsuClW6Pdajb47mUjK7PZz)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

**Exemple 3 : Array.filter()**

```
// Travailler avec array filter
```

```
let ages = [12,24,43,57,18,90,43,36,92,11,3,4,8,9,9,15,16,14];
```

```
function rightToVote(age){   return age >= 18;}
```

```
let votersArray = ages.filter(rightToVote);
```

```
console.log(votersArray);
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/FPNv0puZjLOD1z0KapHXstBPF8iR1KmKkpN4)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

### Récursivité

C'est l'un des sujets clés de la programmation fonctionnelle. Le processus dans lequel une fonction s'appelle directement ou indirectement est appelé une fonction récursive. Ce concept de récursivité est assez utile pour résoudre des problèmes algorithmiques comme les Tours de Hanoï, Pré-Ordres, Post-Ordres, In-Ordres, et certains problèmes de parcours de graphes.

**Exemple**

Discutons d'un exemple célèbre : trouver la factorielle d'un nombre en utilisant la récursivité. Cela peut être fait en appelant la fonction directement depuis le programme de manière répétée. La logique du programme est

> factorielle(n) = factorielle(n) * factorielle(n - 1) * factorielle(n - 2) * factorielle(n - 3) * ….. * factorielle(n - n);

```
// Trouver la factorielle d'un nombre en utilisant la récursivité
```

```
function factorial(num){  if(num == 0)        return 1;  else        return num * factorial(num - 1);
```

```
}
```

```
// appel de la fonction
```

```
console.log(factorial(3));
```

```
console.log(factorial(7));
```

```
console.log(factorial(0));
```

**Sortie**

![Image](https://cdn-media-1.freecodecamp.org/images/7YUVGyUrWQcqnG8dUZ5BnfbXmqT1SvzAyVeI)
_Partie sortie et exécution du programme ci-dessus dans la console JavaScript de Chrome._

## Caractéristiques de la programmation fonctionnelle

L'objectif de tout langage FP est de mimiquer l'utilisation des concepts mathématiques. Cependant, le processus de base de calcul est différent en programmation fonctionnelle. Les principales caractéristiques de la programmation fonctionnelle sont :

**Les données sont immuables :** Les données qui sont présentes à l'intérieur des fonctions sont immuables. En programmation fonctionnelle, nous pouvons facilement créer une nouvelle structure de données mais nous ne pouvons pas modifier celle existante.

**Maintenabilité :** La programmation fonctionnelle offre une grande maintenabilité pour les développeurs et les programmeurs. Nous n'avons pas à nous soucier des changements qui sont accidentellement faits en dehors de la fonction donnée.

**Modularité :** C'est l'une des caractéristiques les plus importantes de la programmation fonctionnelle. Cela nous aide à décomposer un grand projet en modules plus simples. Ces modules peuvent être testés séparément, ce qui vous aide à réduire le temps passé sur les tests unitaires et le débogage.

## Avantages de la programmation fonctionnelle

1. Elle nous aide à résoudre les problèmes de manière efficace et plus simple.
2. Elle améliore la modularité.
3. Elle nous permet d'implémenter le lambda calcul dans notre programme pour résoudre des problèmes complexes.
4. Certains langages de programmation supportent les fonctions imbriquées, ce qui améliore la maintenabilité du code.
5. Elle réduit les problèmes complexes en morceaux simples.
6. Elle améliore la productivité du développeur.
7. Elle nous aide à déboguer le code rapidement.

## Inconvénients de la programmation fonctionnelle

1. Pour les débutants, c'est difficile à comprendre. Ce n'est donc pas une approche de paradigme adaptée aux nouveaux programmeurs.
2. La maintenance est difficile pendant la phase de codage lorsque la taille du projet est grande.
3. La réutilisabilité en programmation fonctionnelle est une tâche délicate pour les développeurs.

## Conclusion

Pour certains, cela peut être un tout nouveau paradigme de programmation. J'espère que vous lui donnerez une chance dans votre parcours de programmation. Je pense que vous trouverez vos programmes plus faciles à lire et à déboguer.

Ce concept de programmation fonctionnelle peut être délicat et difficile pour vous. Même si vous êtes débutant, cela deviendra éventuellement plus facile. Ensuite, vous pourrez profiter des fonctionnalités de la programmation fonctionnelle.

**Si vous avez aimé cet article, partagez-le avec vos amis.**

**Bonjour les gens occupés, j'espère que vous vous êtes amusés à lire cet article, et j'espère que vous avez appris beaucoup ici ! C'était ma tentative de partager ce que j'apprends.**

**J'espère que vous avez vu quelque chose d'utile pour vous ici. Et à la prochaine fois !**

**Amusez-vous bien ! Continuez à apprendre de nouvelles choses et à coder pour résoudre des problèmes.**

**Consultez mon [Twitter](https://twitter.com/Sri_Programmer), [Github](https://github.com/srimani-programmer), et [Facebook](https://www.facebook.com/srimani.programmer).**