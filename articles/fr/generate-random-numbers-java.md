---
title: Générateur de nombres aléatoires en Java – Comment générer des entiers avec
  Math Random
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-25T22:50:46.000Z'
originalURL: https://freecodecamp.org/news/generate-random-numbers-java
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Untitled-design--1-.png
tags:
- name: Java
  slug: java
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: random
  slug: random
seo_title: Générateur de nombres aléatoires en Java – Comment générer des entiers
  avec Math Random
seo_desc: "By Thanoshan MV\nComputer generated random numbers are divided into two\
  \ categories: true random numbers and pseudo-random numbers. \nTrue random numbers\
  \ are generated based on external factors. For example, generating randomness using\
  \ surrounding noise..."
---

Par Thanoshan MV

Les nombres aléatoires générés par ordinateur sont divisés en deux catégories : les vrais nombres aléatoires et les nombres pseudo-aléatoires. 

Les vrais nombres aléatoires sont générés en fonction de facteurs externes. Par exemple, générer de l'aléatoire en utilisant les bruits environnants. 

Mais générer de tels vrais nombres aléatoires est une tâche chronophage. Par conséquent, nous pouvons utiliser des nombres pseudo-aléatoires qui sont générés à l'aide d'un algorithme et d'une valeur de graine. 

Ces nombres pseudo-aléatoires sont suffisants pour la plupart des usages. Par exemple, vous pouvez les utiliser en cryptographie, dans la construction de jeux tels que les dés ou les cartes, et dans la génération de nombres OTP (mot de passe à usage unique). 

Dans cet article, nous allons apprendre comment générer des nombres pseudo-aléatoires en utilisant `Math.random()` en Java. 

## 1. Utiliser Math.random() pour générer des entiers

`Math.random()` retourne un nombre pseudo-aléatoire de type double, supérieur ou égal à zéro et inférieur à un. 

Essayons cela avec un peu de code :

```java
    public static void main(String[] args) {
        double randomNumber = Math.random();
        System.out.println(randomNumber);
    }
    // sortie #1 = 0.5600740702032417
    // sortie #2 = 0.04906751303932033
```

`randomNumber` nous donnera un nombre aléatoire différent à chaque exécution. 

Disons que nous voulons générer des nombres aléatoires dans une plage spécifiée, par exemple, de zéro à quatre. 

```java
    // générer des nombres aléatoires entre 0 et 4
    public static void main(String[] args) {
        // Math.random() génère un nombre aléatoire de 0.0 à 0.999
        // Ainsi, Math.random()*5 sera de 0.0 à 4.999
        double doubleRandomNumber = Math.random() * 5;
        System.out.println("doubleRandomNumber = " + doubleRandomNumber);
        // convertir le double en nombre entier
        int randomNumber = (int)doubleRandomNumber;
        System.out.println("randomNumber = " + randomNumber);
    }
    /* Sortie #1
    doubleRandomNumber = 2.431392914284627
    randomNumber = 2
    */
```

Lorsque nous convertissons un double en int, la valeur int conserve uniquement la partie entière. 

Par exemple, dans le code ci-dessus, `doubleRandomNumber` est `2.431392914284627`. La partie entière de `doubleRandomNumber` est `2` et la partie fractionnaire (nombres après la virgule) est `431392914284627`. Ainsi, `randomNumber` ne contiendra que la partie entière `2`. 

Vous pouvez en savoir plus sur la méthode `Math.random()` dans la [documentation Java](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html). 

Utiliser `Math.random()` n'est pas la seule façon de générer des nombres aléatoires en Java. Ensuite, nous verrons comment nous pouvons générer des nombres aléatoires en utilisant la classe Random. 

## 2. Utiliser la classe Random pour générer des entiers

Dans la classe Random, nous avons plusieurs méthodes d'instance qui fournissent des nombres aléatoires. Dans cette section, nous allons considérer deux méthodes d'instance, `nextInt(int bound)`, et `nextDouble()`. 

### Comment utiliser la méthode nextInt(int bound)

`nextInt(int bound)` retourne un nombre pseudo-aléatoire de type int, supérieur ou égal à zéro et inférieur à la valeur de bound. 

Le paramètre `bound` spécifie la plage. Par exemple, si nous spécifions le bound à 4, `nextInt(4)` retournera une valeur de type int, supérieure ou égale à zéro et inférieure à quatre. 0,1,2,3 sont les résultats possibles de `nextInt(4)`. 

Comme il s'agit d'une méthode d'instance, nous devons créer un objet random pour accéder à cette méthode. Essayons cela.

```java
    public static void main(String[] args) {
        // créer un objet Random
        Random random = new Random();
        // générer un nombre aléatoire de 0 à 3
        int number = random.nextInt(4);
        System.out.println(number);
    }
```

### Comment utiliser la méthode nextDouble()

Similaire à `Math.random()`, `nextDouble()` retourne un nombre pseudo-aléatoire de type double, supérieur ou égal à zéro et inférieur à un. 

```java
    public static void main(String[] args) {
        // créer un objet Random
        Random random = new Random();
        // génère un nombre aléatoire de 0.0 et inférieur à 1.0
        double number = random.nextDouble();
        System.out.println(number);
    }
```

Pour plus d'informations, vous pouvez lire la [documentation Java](https://docs.oracle.com/javase/8/docs/api/java/util/Random.html) de la classe random. 

## Alors, quelle méthode de nombre aléatoire devriez-vous utiliser ?

`[Math.random()](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#random--)` [utilise la classe random](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#random--). Si nous voulons uniquement des nombres pseudo-aléatoires de type double dans notre application, alors nous pouvons utiliser `Math.random()`. 

Sinon, nous pouvons utiliser la classe random car elle fournit diverses méthodes pour générer des nombres pseudo-aléatoires de différents types tels que `nextInt()`, `nextLong()`, `nextFloat()` et `nextDouble()`. 

Merci d'avoir lu.

Image par [Brett Jordan](https://unsplash.com/@brett_jordan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/random-numbers?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Vous pouvez me contacter sur [Medium](https://mvthanoshan.medium.com/).

**Bon codage !**