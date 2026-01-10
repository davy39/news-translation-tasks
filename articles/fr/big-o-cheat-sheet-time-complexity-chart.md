---
title: Aide-mémoire Big O – Tableau de complexité temporelle
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-10-05T15:00:53.000Z'
originalURL: https://freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/cover-template--12-.png
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
seo_title: Aide-mémoire Big O – Tableau de complexité temporelle
seo_desc: 'An algorithm is a set of well-defined instructions for solving a specific
  problem. You can solve these problems in various ways.

  This means that the method you use to arrive at the same solution may differ from
  mine, but we should both get the same r...'
---

Un algorithme est un ensemble d'instructions bien définies pour résoudre un problème spécifique. Vous pouvez résoudre ces problèmes de diverses manières.

Cela signifie que la méthode que vous utilisez pour arriver à la même solution peut différer de la mienne, mais nous devrions tous deux obtenir le même résultat.

Comme il existe plusieurs façons de résoudre un problème, il doit y avoir un moyen d'évaluer ces solutions ou algorithmes en termes de performance et d'efficacité (le temps qu'il faudra à votre algorithme pour s'exécuter et la quantité totale de mémoire qu'il consommera).

C'est essentiel pour les programmeurs afin de s'assurer que leurs applications fonctionnent correctement et pour les aider à écrire du code propre.

C'est là que la notation Big O entre en scène. La notation Big O est une mesure permettant de déterminer l'efficacité d'un algorithme. Elle vous permet d'estimer combien de temps votre code s'exécutera sur différents ensembles d'entrées et de mesurer l'efficacité avec laquelle votre code s'adapte à mesure que la taille de votre entrée augmente.

## Qu'est-ce que le Big O ?

Le Big O, également connu sous le nom de notation Big O, représente la complexité d'un algorithme dans le pire des cas. Il utilise des termes algébriques pour décrire la complexité d'un algorithme.

Le Big O définit le temps d'exécution requis pour exécuter un algorithme en identifiant comment les performances de votre algorithme changeront à mesure que la taille de l'entrée augmente. Mais il ne vous dit pas à quelle vitesse le temps d'exécution de votre algorithme s'écoule.

La notation Big O mesure l'efficacité et la performance de votre algorithme en utilisant la complexité temporelle et spatiale.

### Qu'est-ce que la complexité temporelle et spatiale ?

L'un des principaux facteurs sous-jacents affectant les performances et l'efficacité de votre programme est le matériel, le système d'exploitation et le processeur que vous utilisez.

Mais vous ne tenez pas compte de cela lorsque vous analysez les performances d'un algorithme. Au lieu de cela, ce qui importe, c'est la complexité temporelle et spatiale en tant que fonction de la taille de l'entrée.

La complexité temporelle d'un algorithme spécifie le temps qu'il faudra pour exécuter un algorithme **en fonction de la taille de son entrée**. De même, la complexité spatiale d'un algorithme spécifie la quantité totale d'espace ou de mémoire requise pour exécuter un algorithme **en fonction de la taille de l'entrée**.

Nous nous concentrerons sur la complexité temporelle dans ce guide. Il s'agira d'un aide-mémoire approfondi pour vous aider à comprendre comment calculer la complexité temporelle de n'importe quel algorithme.

### Pourquoi la complexité temporelle est-elle une fonction de la taille de l'entrée ?

Pour parfaitement saisir le concept de « en fonction de la taille de l'entrée », imaginez que vous avez un algorithme qui calcule la somme des nombres en fonction de votre entrée. Si votre entrée est 4, il ajoutera 1+2+3+4 pour afficher 10 ; si votre entrée est 5, il affichera 15 (c'est-à-dire 1+2+3+4+5).

```js
const calculateSum = (input) => {
  let sum = 0;
  for (let i = 0; i <= input; i++) {
    sum += i;
  }
  return sum;
};
```

Dans le code ci-dessus, nous avons trois instructions :

![](https://paper-attachments.dropbox.com/s_2D428973624E7FC84C7D69D11421DE762BEA6B6F3361231FCDCAE0425D14526F_1664881245657_Untitled.drawio+16.png align="left")

En regardant l'image ci-dessus, nous n'avons que trois instructions. Pourtant, parce qu'il y a une boucle, la deuxième instruction sera exécutée en fonction de la taille de l'entrée, donc si l'entrée est quatre, la deuxième instruction (instruction 2) sera exécutée quatre fois, ce qui signifie que l'algorithme entier s'exécutera six (4 + 2) fois.

En termes clairs, l'algorithme s'exécutera **entrée + 2** fois, où l'entrée peut être n'importe quel nombre. Cela montre qu'**il est exprimé en termes d'entrée. En d'autres termes, c'est une fonction de la taille de l'entrée**.

En Big O, il existe six principaux types de complexités (temporelle et spatiale) :

* Constante : O(1)
    
* Temps linéaire : O(n)
    
* Temps logarithmique : O(n log n)
    
* Temps quadratique : O(n^2)
    
* Temps exponentiel : O(2^n)
    
* Temps factoriel : O(n!)
    

Avant d'examiner des exemples pour chaque complexité temporelle, comprenons le tableau de complexité temporelle Big O.

## Tableau de complexité Big O

Le tableau Big O, également connu sous le nom de graphique Big O, est une notation asymptotique utilisée pour exprimer la complexité d'un algorithme ou sa performance en fonction de la taille de l'entrée.

Cela aide les programmeurs à identifier et à comprendre pleinement le scénario du pire cas ainsi que le temps d'exécution ou la mémoire requis par un algorithme.

Le [graphique suivant](bigocheatsheet.com) illustre la complexité Big O :

![Image de bigocheatsheet.com](https://paper-attachments.dropbox.com/s_2D428973624E7FC84C7D69D11421DE762BEA6B6F3361231FCDCAE0425D14526F_1664885448372_Untitled.drawio+17.png align="left")

Le tableau Big O ci-dessus montre que O(1), qui correspond à une complexité temporelle constante, est le meilleur. Cela implique que votre algorithme ne traite qu'une seule instruction sans aucune itération. Ensuite, il y a O(log n), qui est bon, et d'autres comme lui, comme indiqué ci-dessous :

* **O(1)** - Excellent/Meilleur
    
* **O(log n)** - Bon
    
* **O(n)** - Passable
    
* **O(n log n)** - Mauvais
    
* **O(n^2)**, **O(2^n)** et **O(n!)** - Horrible/Pire
    

Vous comprenez maintenant les diverses complexités temporelles, et vous pouvez reconnaître les meilleures, les bonnes et les passables, ainsi que les mauvaises et les pires (évitez toujours les mauvaises et les pires complexités temporelles).

La question suivante qui vient à l'esprit est de savoir comment savoir quel algorithme a quelle complexité temporelle, étant donné que ceci est censé être un aide-mémoire 😂.

* Lorsque votre calcul ne dépend pas de la taille de l'entrée, il s'agit d'une complexité temporelle constante (O(1)).
    
* Lorsque la taille de l'entrée est réduite de moitié, peut-être lors d'une itération, de la gestion d'une [récursion](https://joelolawanle.com/posts/recursion-in-javascript-explained-for-beginners), ou autre, il s'agit d'une complexité temporelle logarithmique (O(log n)).
    
* Lorsque vous avez une seule boucle dans votre algorithme, il s'agit d'une complexité temporelle linéaire (O(n)).
    
* Lorsque vous avez des boucles imbriquées dans votre algorithme, c'est-à-dire une boucle dans une boucle, il s'agit d'une complexité temporelle quadratique (O(n^2)).
    
* Lorsque le taux de croissance double à chaque ajout à l'entrée, il s'agit d'une complexité temporelle exponentielle (O(2^n)).
    

Commençons par décrire chaque complexité temporelle avec des exemples. Il est important de noter que j'utiliserai JavaScript dans les exemples de ce guide, mais le langage de programmation n'est pas important tant que vous comprenez le concept et chaque complexité temporelle.

## Exemples de complexité temporelle Big O

### Temps constant : O(1)

Lorsque votre algorithme ne dépend pas de la taille de l'entrée n, on dit qu'il a une complexité temporelle constante d'ordre O(1). Cela signifie que le temps d'exécution sera toujours le même, quelle que soit la taille de l'entrée.

Par exemple, si un algorithme doit retourner le premier élément d'un tableau. Même si le tableau contient 1 million d'éléments, la complexité temporelle sera constante si vous utilisez cette approche :

```js
const firstElement = (array) => {
  return array[0];
};

let score = [12, 55, 67, 94, 22];
console.log(firstElement(score)); // 12
```

La fonction ci-dessus ne nécessitera qu'une seule étape d'exécution, ce qui signifie que la fonction est en temps constant avec une complexité temporelle O(1).

Mais comme je l'ai dit plus tôt, il existe plusieurs façons de parvenir à une solution en programmation. Un autre programmeur pourrait décider de parcourir d'abord le tableau avant de retourner le premier élément :

```js
const firstElement = (array) => {
  for (let i = 0; i < array.length; i++) {
    return array[0];
  }
};

let score = [12, 55, 67, 94, 22];
console.log(firstElement(score)); // 12
```

Ceci n'est qu'un exemple – il est probable que personne ne ferait cela. Mais s'il y a une boucle, ce n'est plus un temps constant mais maintenant un temps linéaire avec une complexité temporelle O(n).

### Temps linéaire : O(n)

Vous obtenez une complexité temporelle linéaire lorsque le temps d'exécution d'un algorithme augmente linéairement avec la taille de l'entrée. Cela signifie que lorsqu'une fonction possède une itération qui parcourt une taille d'entrée n, on dit qu'elle a une complexité temporelle d'ordre O(n).

Par exemple, si un algorithme doit retourner la factorielle de n'importe quel nombre saisi. Cela signifie que si vous saisissez 5, vous devez boucler et multiplier 1 par 2 par 3 par 4 et par 5, puis afficher 120 :

```js
const calcFactorial = (n) => {
  let factorial = 1;
  for (let i = 2; i <= n; i++) {
    factorial = factorial * i;
  }
  return factorial;
};

console.log(calcFactorial(5)); // 120
```

Le fait que le temps d'exécution dépende de la taille de l'entrée signifie que la complexité temporelle est linéaire avec l'ordre O(n).

### Temps logarithmique : O(log n)

Ceci est similaire à la complexité temporelle linéaire, sauf que le temps d'exécution ne dépend pas de la taille de l'entrée mais plutôt de la moitié de la taille de l'entrée. Lorsque la taille de l'entrée diminue à chaque itération ou étape, on dit qu'un algorithme a une complexité temporelle logarithmique.

Cette méthode est la deuxième meilleure car votre programme s'exécute pour la moitié de la taille de l'entrée plutôt que pour la taille totale. Après tout, la taille de l'entrée diminue à chaque itération.

Un excellent exemple est celui des fonctions de recherche dichotomique (binary search), qui divisent votre tableau trié en fonction de la valeur cible.

Par exemple, supposons que vous utilisiez un algorithme de recherche dichotomique pour trouver l'index d'un élément donné dans un tableau :

```js
const binarySearch = (array, target) => {
  let firstIndex = 0;
  let lastIndex = array.length - 1;
  while (firstIndex <= lastIndex) {
    let middleIndex = Math.floor((firstIndex + lastIndex) / 2);

    if (array[middleIndex] === target) {
      return middleIndex;
    }

    if (array[middleIndex] > target) {
      lastIndex = middleIndex - 1;
    } else {
      firstIndex = middleIndex + 1;
    }
  }
  return -1;
};

let score = [12, 22, 45, 67, 96];
console.log(binarySearch(score, 96));
```

Dans le code ci-dessus, puisqu'il s'agit d'une recherche dichotomique, vous obtenez d'abord l'index du milieu de votre tableau, vous le comparez à la valeur cible et vous retournez l'index du milieu s'il est égal. Sinon, vous devez vérifier si la valeur cible est supérieure ou inférieure à la valeur du milieu pour ajuster le premier et le dernier index, réduisant ainsi la taille de l'entrée de moitié.

Parce qu'à chaque itération la taille de l'entrée diminue de moitié, la complexité temporelle est logarithmique avec l'ordre O(log n).

### Temps quadratique : O(n^2)

Lorsque vous effectuez une itération imbriquée, c'est-à-dire une boucle dans une boucle, la complexité temporelle est quadratique, ce qui est horrible.

Une façon parfaite d'expliquer cela serait d'avoir un tableau de n éléments. La boucle externe s'exécutera n fois, et la boucle interne s'exécutera n fois pour chaque itération de la boucle externe, ce qui donnera un total de n^2 affichages. Si le tableau contient dix éléments, dix s'afficheront 100 fois (10^2).

Voici un exemple de [Jared Nielsen](https://jarednielsen.com/big-o-quadratic-time-complexity/), où vous comparez chaque élément d'un tableau pour afficher l'index lorsque deux éléments sont similaires :

```js
const matchElements = (array) => {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      if (i !== j && array[i] === array[j]) {
        return `Match trouvé à ${i} et ${j}`;
      }
    }
  }
  return "Aucun match trouvé 😟";
};

const fruit = ["🍓", "🍐", "🍊", "🍌", "🍍", "🍑", "🍎", "🍈", "🍊", "🍇"];
console.log(matchElements(fruit)); // "Match trouvé à 2 et 8"
```

Dans l'exemple ci-dessus, il y a une boucle imbriquée, ce qui signifie que la complexité temporelle est quadratique avec l'ordre O(n^2).

### Temps exponentiel : O(2^n)

Vous obtenez une complexité temporelle exponentielle lorsque le taux de croissance double à chaque ajout à l'entrée (n), souvent en itérant à travers tous les sous-ensembles des éléments d'entrée. Chaque fois qu'une unité d'entrée augmente de 1, le nombre d'opérations exécutées est doublé.

La suite de Fibonacci récursive est un bon exemple. Supposons qu'on vous donne un nombre et que vous vouliez trouver le n-ième élément de la suite de Fibonacci.

La suite de Fibonacci est une suite mathématique dans laquelle chaque nombre est la somme des deux nombres précédents, où 0 et 1 sont les deux premiers nombres. Le troisième nombre de la suite est 1, le quatrième est 2, le cinquième est 3, et ainsi de suite... (0, 1, 1, 2, 3, 5, 8, 13, …).

Cela signifie que si vous passez 6, alors le 6ème élément de la suite de Fibonacci serait 8 :

```js
const recursiveFibonacci = (n) => {
  if (n < 2) {
    return n;
  }
  return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
};

console.log(recursiveFibonacci(6)); // 8
```

Dans le code ci-dessus, l'algorithme spécifie un taux de croissance qui double chaque fois que l'ensemble de données d'entrée est augmenté. Cela signifie que la complexité temporelle est exponentielle avec un ordre O(2^n).

## Conclusion

Dans ce guide, vous avez appris ce qu'est la complexité temporelle, comment la performance est déterminée à l'aide de la notation Big O, et les diverses complexités temporelles qui existent avec des exemples.

Vous pouvez en apprendre davantage via le [curriculum sur les algorithmes et les structures de données JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp.

Bon apprentissage !

Vous pouvez accéder à plus de 200 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.