---
title: Boucle For en Java + Exemple de Syntaxe de Boucle forEach
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-07T15:08:46.000Z'
originalURL: https://freecodecamp.org/news/for-loop-in-java-foreach-loop-syntax-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/loop.jpg
tags:
- name: Java
  slug: java
- name: Loops
  slug: loops
seo_title: Boucle For en Java + Exemple de Syntaxe de Boucle forEach
seo_desc: 'A loop in programming is a sequence of instructions that run continuously
  until a certain condition is met.

  In this article, we will learn about the for and forEach loops in Java.

  Syntax for a for loop in Java

  Here is the syntax for creating a for lo...'
---

Une boucle en programmation est une séquence d'instructions qui s'exécutent en continu jusqu'à ce qu'une certaine condition soit remplie.

Dans cet article, nous allons apprendre les boucles `for` et `forEach` en Java.

## Syntaxe pour une boucle `for` en Java

Voici la syntaxe pour créer une boucle `for` :

```java
for (initialisation; condition; incrément/décrément) {
   // code à exécuter
}
```

Décomposons certains des mots-clés ci-dessus.

**for** spécifie que nous allons créer une boucle. Il est suivi de parenthèses contenant tout ce qui est nécessaire pour que notre boucle fonctionne.

**initialisation** définit une variable initiale comme point de départ de la boucle, généralement un entier (nombre entier).

**condition** spécifie le nombre de fois où la boucle doit s'exécuter.

**incrément/décrément** augmente/diminue la valeur de la variable initiale à chaque fois que la boucle s'exécute. À mesure que l'incrément/décrément se produit, la valeur de la variable tend vers la **condition** spécifiée.

Notez que chaque mot-clé est séparé par un point-virgule (;).

Voici quelques exemples :

```java
for(int x = 1; x <=5; x++) {
  System.out.println(x);
}

/*
1
2
3
4
5
*/
```

Dans l'exemple ci-dessus, la variable initiale est `x` avec une valeur de 1. La boucle continuera à s'exécuter tant que la valeur de `x` est inférieure ou égale à 5 – c'est la condition. `x++` augmente la valeur de `x` après chaque exécution.

Nous avons ensuite imprimé la valeur de `x` qui s'arrête après 5 parce que la condition a été remplie. Incrémenter à 6 est impossible parce que cela est supérieur et non égal à 5.

Dans l'exemple suivant, nous allons utiliser la boucle `for` pour imprimer toutes les valeurs d'un tableau.

```java
int[] randomNumbers = {2, 5, 4, 7};
for (int i = 0; i < randomNumbers.length; i++) {
  System.out.println(randomNumbers[i]);
}

// 2
// 5
// 4
// 7
```

Cela est presque identique au dernier exemple. Ici, nous avons utilisé la longueur du tableau comme condition et la valeur de la variable initiale comme zéro parce que le numéro d'index du premier élément d'un tableau est zéro.

## Syntaxe pour une boucle `forEach` en Java

Vous utilisez une boucle `forEach` spécifiquement pour parcourir les éléments d'un tableau. Voici à quoi ressemble la syntaxe :

```java
for (dataType variableName : arrayName) {
  // code à exécuter
}
```

Vous remarquerez que la syntaxe ici est plus courte que celle de la boucle `for`. La boucle `forEach` commence également par le mot-clé **for**.

Au lieu d'initialiser une variable avec une valeur, nous spécifions d'abord le **type de données** (celui-ci doit correspondre au type de données du tableau). Cela est suivi par le **nom de notre variable** et le **nom du tableau** séparés par un deux-points.

Voici un exemple pour vous aider à mieux comprendre la syntaxe :

```java
int[] randomNumbers = {2, 5, 4, 7};
for (int x : randomNumbers) {
  System.out.println(x + 1);
}

/*
3
6
5
8
*/
```

Dans cet exemple, nous avons parcouru chaque élément et augmenté leur valeur initiale de 1.

Par défaut, la boucle s'arrêtera une fois qu'elle aura parcouru tous les éléments du tableau. Cela signifie que nous ne sommes pas obligés de passer une valeur à notre variable ou de spécifier une condition pour terminer la boucle.

## Conclusion

Dans cet article, nous avons appris ce que sont les boucles ainsi que la syntaxe pour créer une boucle `for` et `forEach` en Java. Nous avons également vu quelques exemples qui nous ont aidés à comprendre quand et comment les utiliser.

Bon codage !