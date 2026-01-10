---
title: Contexte d'exécution JavaScript – Comment JS fonctionne en coulisses
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-22T17:50:05.000Z'
originalURL: https://freecodecamp.org/news/how-javascript-works-behind-the-scene-javascript-execution-context
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Dark-Blue-Illustrated-Techno-Daily-Smore-Header--1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Contexte d'exécution JavaScript – Comment JS fonctionne en coulisses
seo_desc: 'By Rwitesh Bera

  Have you ever wondered how JavaScript works behind the scenes? It''s actually quite
  fascinating! And that''s what you''ll learn about here.

  JavaScript is a single-threaded interpreted language. Every browser has its own
  JavaScript engine...'
---

Par Rwitesh Bera

Vous êtes-vous déjà demandé comment JavaScript fonctionne en coulisses ? C'est en fait assez fascinant ! Et c'est ce que vous allez apprendre ici.

JavaScript est un langage interprété à thread unique. Chaque navigateur a son propre moteur JavaScript. Google Chrome a le moteur V8, Mozilla Firefox a SpiderMonkey, et ainsi de suite. Ils sont tous utilisés pour le même objectif, car les navigateurs ne peuvent pas comprendre directement le code JavaScript. 

Regardons un exemple pour en apprendre davantage :

```js
var n = 5;

function square(n) {
  var ans = n * n;
  return ans;
}

var square1 = square(n);
var square2 = square(8);  

console.log(square1)
console.log(square2)
```

Dans le code ci-dessus,

1. n est initialisé et se voit attribuer une valeur de 5
2. Nous avons défini une fonction `square()` qui accepte un argument n et retourne le carré de n.
3. Nous appelons la fonction `square()` et stockons la valeur retournée dans la variable `square1`.
4. Nous appelons la fonction `square()` et stockons la valeur retournée dans la variable `square2`.
5. Enfin, il affiche à la fois `square1` et `square2`

En coulisses, JavaScript fait tant de choses. Comprenons tout cela.

## Qu'est-ce que le Contexte d'Exécution ?

Lorsque le moteur JavaScript analyse un fichier de script, il crée un environnement appelé **Contexte d'Exécution** qui gère l'ensemble de la transformation et de l'exécution du code. 

Pendant l'exécution du contexte, l'analyseur parse le code source et alloue de la mémoire pour les variables et les fonctions. Le code source est généré et exécuté.

Il existe deux types de contextes d'exécution : **global** et **fonction**. Le contexte d'exécution global est créé lorsqu'un script JavaScript commence à s'exécuter pour la première fois, et il représente la portée globale en JavaScript. Un contexte d'exécution de fonction est créé chaque fois qu'une fonction est appelée, représentant la portée locale de la fonction.

### Phases du Contexte d'Exécution JavaScript

Il y a deux phases du contexte d'exécution JavaScript :

1. **Phase de création** : Dans cette phase, le moteur JavaScript crée le contexte d'exécution et configure l'environnement du script. Il détermine les valeurs des variables et des fonctions et configure la chaîne de portée pour le contexte d'exécution.
2. **Phase d'exécution** : Dans cette phase, le moteur JavaScript exécute le code dans le contexte d'exécution. Il traite les instructions ou expressions dans le script et évalue les appels de fonction.

Tout en JS se passe à l'intérieur de ce contexte d'exécution. Il est divisé en deux composants. L'un est la mémoire et l'autre est le code. Il est important de se rappeler que ces phases et composants sont applicables aux contextes d'exécution globaux et fonctionnels.

### Phase de Création

![Image](https://www.freecodecamp.org/news/content/images/2022/12/1.png)
_Contexte d'Exécution_

Prenons cet exemple simple une fois de plus :

```js
var n = 5;

function square(n) {
  var ans = n * n;
  return ans;
}

var square1 = square(n);
var square2 = square(8);  

console.log(square1)
console.log(square2)
```

Au tout début, le moteur JavaScript exécute l'ensemble du code source, crée un contexte d'exécution global, puis fait les choses suivantes :

1. Crée un objet global qui est **window** dans le navigateur et **global** dans NodeJs.
2. Configure une mémoire pour stocker les variables et les fonctions.
3. Stocke les variables avec des valeurs comme undefined et les références de fonction.

Cela s'appelle la phase de création. Voici un diagramme pour aider à l'expliquer :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/untitled-2.png)
_Phase de Création dans le Contexte d'Exécution_

Après cette phase de création, le contexte d'exécution passera à la phase d'exécution du code.

### Phase d'Exécution

Maintenant, dans cette phase, il commence à parcourir l'ensemble du code ligne par ligne de haut en bas. Dès qu'il rencontre **n = 5**, il attribue la valeur 5 à 'n' en mémoire. Jusqu'à présent, la valeur de 'n' était undefined par défaut. 

Ensuite, nous arrivons à la fonction 'square'. Comme la fonction a été allouée en mémoire, il passe directement à la ligne **var square1 = square(n);**. square() sera invoquée et JavaScript créera une fois de plus un nouveau contexte d'exécution de fonction.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/untitled-3-1.png)
_Phase d'Exécution du Code_

Une fois le calcul terminé, il attribue la valeur du carré dans la variable 'ans' qui était undefined auparavant. La fonction retournera la valeur, et le contexte d'exécution de la fonction sera détruit.

La valeur retournée par square() sera attribuée à square1. Cela se produit également pour square2. Une fois l'exécution complète du code terminée, le contexte global ressemblera à ceci et sera également détruit.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/untitled-4.png)

## Qu'est-ce que la Pile d'Appels ?

Pour garder une trace de tous les contextes, y compris les contextes globaux et fonctionnels, le moteur JavaScript utilise une **pile d'appels**. Une pile d'appels est également connue sous le nom de 'Pile de Contexte d'Exécution', 'Pile d'Exécution', ou 'Pile Machine'.

Elle utilise le principe LIFO (Last-In-First-Out). Lorsque le moteur commence à exécuter le script, il crée un contexte global et le pousse sur la pile. Chaque fois qu'une fonction est invoquée, de manière similaire, le moteur JS crée un contexte de pile de fonction pour la fonction et le pousse au sommet de la pile d'appels et commence à l'exécuter. 

Lorsque l'exécution de la fonction actuelle est terminée, le moteur JavaScript supprimera automatiquement le contexte de la pile d'appels et reviendra à son parent. 

Regardons l'exemple suivant :

```js
function funcA(m,n) {
    return m * n;
}

function funcB(m,n) {
    return funcA(m,n);
}

function getResult(num1, num2) {
    return funcB(num1, num2)
}

var res = getResult(5,6);

console.log(res); // 30
```

Dans cet exemple, le moteur JS crée un contexte d'exécution global qui entre dans la phase de création. 

Tout d'abord, il alloue de la mémoire pour `funcA`, `funcB`, la fonction `getResult`, et la variable `res`. Ensuite, il invoque `getResult()`, qui sera poussé sur la pile d'appels.

Ensuite, `getResult()` appellera `funcB()`. À ce moment-là, le contexte de `funcB` sera stocké au sommet de la pile. Ensuite, il commencera à s'exécuter et appellera une autre fonction `funcA()`. De manière similaire, le contexte de `funcA` sera poussé.  

Une fois l'exécution de chaque fonction terminée, elle sera retirée de la pile d'appels. L'image suivante décrit l'ensemble du processus d'exécution :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/5.png)
_Pile d'Appels_

La pile d'appels a une taille fixe qui dépend du système ou du navigateur. Si le nombre de contextes dépasse la limite, une erreur de dépassement de pile se produira. Cela arrive avec une fonction récursive qui n'a pas de condition de base.

```js
function display() {
    display();
}

display();
```

```bash
C:\Users\rwiteshbera\Desktop\Javascript\n.js:2
    display();
    ^
RangeError: Maximum call stack size exceeded

```

## Conclusion

En conclusion, le contexte d'exécution JavaScript est une partie cruciale pour comprendre comment JavaScript fonctionne en coulisses. Il détermine l'environnement dans lequel le code est exécuté et quelles variables et fonctions sont disponibles à utiliser. 

La phase de création inclut la création des contextes d'exécution globaux et de fonction, la création de la chaîne de portée, et l'allocation de mémoire pour les variables et les fonctions. Pendant la phase d'exécution, le moteur JavaScript exécute le code ligne par ligne. Cela inclut l'évaluation et l'exécution des instructions.

J'espère que vous avez trouvé ce tutoriel utile et informatif. Si vous avez aimé le lire, je vous encourage à le partager avec vos amis et followers sur les réseaux sociaux. 

N'oubliez pas de me suivre également sur [Twitter](https://twitter.com/RwiteshBera) pour plus de mises à jour sur la programmation et la technologie. Merci pour votre lecture !