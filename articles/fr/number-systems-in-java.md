---
title: Comment fonctionnent les systèmes de numération en Java – Décimal, Binaire,
  Octal et Hexadécimal expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-11T21:54:41.000Z'
originalURL: https://freecodecamp.org/news/number-systems-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/number-systems.jpg
tags:
- name: Java
  slug: java
seo_title: Comment fonctionnent les systèmes de numération en Java – Décimal, Binaire,
  Octal et Hexadécimal expliqués
seo_desc: "By Mikael Lassa\nKnowing how to work with numbers is essential in programming.\
  \ Java supports four number systems that are used for various purposes – the decimal,\
  \ binary, octal, and hexadecimal systems. \nUnderstanding what these number systems\
  \ are and..."
---

Par Mikael Lassa

Savoir travailler avec les nombres est essentiel en programmation. Java supporte quatre systèmes de numération utilisés pour diverses fins – les systèmes décimal, binaire, octal et hexadécimal.

Comprendre ce que sont ces systèmes de numération et quand les utiliser est une compétence importante pour tout programmeur Java.

## Comment fonctionne le système de numération décimal

Le système de numération décimal est le système de numération le plus largement utilisé en Java. C'est aussi probablement le plus facile à comprendre, car nous l'utilisons couramment dans la vie quotidienne. Il s'agit d'un système en base 10 qui utilise dix chiffres (0-9) pour représenter les nombres.

En termes plus techniques, la documentation Java d'Oracle définit un littéral entier comme un nombre représenté par une séquence de chiffres ASCII de 0 à 9. Lorsqu'il est suffixé par le caractère ASCII L ou l, le nombre est de type `long`. ([Source : Documentation Java d'Oracle](https://docs.oracle.com/javase/specs/jls/se12/html/jls-3.html#jls-DecimalIntegerLiteral))

Pour rappel, `int` et `long` sont deux des types de données primitifs en Java. Un `int` est un entier 32 bits représentant des valeurs allant de -2 147 483 648 à 2 147 483 647. Un `long` est un entier 64 bits qui peut contenir des valeurs considérablement plus grandes, à savoir de -9 223 372 036 854 775 808 à 9 223 372 036 854 775 807.

Les cas d'utilisation du système de numération décimal en Java sont naturellement nombreux. Il est couramment utilisé dans de nombreuses applications pour gérer des valeurs numériques telles que les devises, les prix et autres données financières, ou différents types de quantités et de mesures (longueur, temps, etc.). Il est également utilisé pour la plupart des types de calculs arithmétiques, ainsi que pour compter et indexer des éléments dans des tableaux ou des listes.

Voici quelques exemples simples :

```java
int decimalInt = 15;
long decimalLong = 400L;
```

## Comment fonctionne le système de numération binaire

Le système de numération binaire est un système en base 2 qui utilise deux chiffres (0 et 1) pour représenter les nombres. Les ordinateurs sont conçus pour traiter les entrées sous forme de nombres binaires, car ils peuvent facilement représenter deux états (par exemple, marche/arrêt) et peuvent être combinés pour effectuer des opérations plus complexes.

En Java, les nombres binaires peuvent être utilisés pour des tâches de programmation de bas niveau, où il peut être nécessaire de fonctionner plus près du fonctionnement interne de la machine.

Les nombres binaires sont également utiles pour les opérations logiques bit à bit, telles que `AND`, `OR` et `NOT`. Ces opérations peuvent être effectuées rapidement et efficacement dans le processeur d'un ordinateur à l'aide de circuits logiques numériques simples.

Pour déclarer un nombre binaire en Java, vous pouvez utiliser le préfixe `0b` ou `0B` suivi des chiffres binaires. Par exemple :

```java
int binaryInt = 0b1010; 
long binaryLong = 0B1010L;
```

## Comment fonctionne le système de numération octal

Le système de numération octal est un système en base 8 qui utilise huit chiffres (0-7) pour représenter les nombres. Les nombres octaux ne sont peut-être pas aussi largement utilisés que les autres systèmes décrits dans cet article, mais ils trouvent leurs domaines d'application distincts.

Dans les systèmes d'exploitation basés sur Unix, par exemple, les permissions de fichiers sont représentées à l'aide de nombres octaux. Cela signifie que, lorsque vous travaillez avec des permissions de fichiers en Java, vous devrez peut-être utiliser des nombres octaux pour définir les permissions d'un fichier.

Pour déclarer un nombre octal en Java, vous utilisez le chiffre `0` comme préfixe, suivi des chiffres octaux. Par exemple :

```java
int octalInt = 0273;
long octalLong = 0273L;
```

## Comment fonctionne le système de numération hexadécimal

Le système de numération hexadécimal est un système en base 16 qui utilise un total de 16 caractères, c'est-à-dire dix chiffres (0-9) et six lettres (A-F), pour représenter les nombres. Les lettres représentent les nombres 10 à 15.

Les avantages de l'utilisation du système hexadécimal sont évidents chaque fois que vous avez besoin d'une manière plus concise de représenter les nombres – par exemple, lorsque vous traitez des tâches de programmation de bas niveau.

Les adresses mémoire de l'ordinateur et les codes de couleur sont en effet souvent représentés par des nombres hexadécimaux, car les représentations binaires correspondantes seraient considérablement plus difficiles à lire pour les humains.

Pour déclarer un nombre hexadécimal en Java, vous utilisez `0x` ou `0X` comme préfixe, suivi des chiffres. Par exemple :

```java
int hexInt = 0x10e; 
long hexLong = 0XABC1;
```

## Comment convertir entre les systèmes de numération

Il existe plusieurs raisons pour lesquelles vous pourriez avoir besoin de convertir entre différents systèmes de numération. Lorsque vous travaillez avec la programmation de bas niveau, par exemple, vous pourriez avoir besoin de convertir entre les nombres décimaux et binaires ou hexadécimaux pour pouvoir définir des configurations.

Une méthode courante pour traduire différents systèmes de numération en système décimal consiste à multiplier chaque chiffre, en commençant par la droite, par la puissance correspondante du nombre de base, qui est 2 pour les nombres binaires, 8 pour les nombres octaux, et ainsi de suite.

Par exemple, pour convertir des nombres octaux en système décimal, vous pouvez calculer le produit de chaque chiffre, en commençant par le chiffre le plus à droite, par la puissance correspondante du nombre 8. La formule peut être représentée comme suit, où `digit0` est le chiffre le plus à droite :

```
(digit0 x 8^0) + (digit1 x 8^1) + (digit2 x 8^2) + ... + (digitn x 8^n) 
```

Sur la base de cette formule, le nombre octal `0273` se convertit en 187 : en commençant par la droite, le chiffre 3 est multiplié par 8 à la puissance 0, puis le chiffre 7 est multiplié par 8 à la puissance 1, et ainsi de suite.

```
  (3 x 8^0) + (7 x 8^1) + (2 x 8^2)
= 3 + 56 + 128
= 187
```

Un concept similaire s'applique aux nombres hexadécimaux, en utilisant la base 16 pour le calcul. Par exemple, le nombre hexadécimal `0xABC1` peut être converti en 43969 comme suit :

```
 (1 x 16^0) + (C x 16^1) + (B x 16^2) + (A x 16^3) 
= 1 + 192 + 2816 + 40960       
= 43969
```

Java fournit des méthodes pour convertir des nombres d'un système de numération à un autre. Ces méthodes sont disponibles dans les classes enveloppes `Integer` et `Long`.

Pour convertir un nombre décimal en une chaîne représentant son équivalent binaire, octal ou hexadécimal, vous pouvez utiliser les méthodes suivantes :

```java
int decimalNumber = 165;

String binaryNumber = Integer.toBinaryString(decimalNumber); //10100101
String octalNumber = Integer.toOctalString(decimalNumber);  //245
String hexNumber = Integer.toHexString(decimalNumber);  //a5
```

Pour effectuer la conversion inverse, la méthode `parseInt` dispose d'une implémentation utile qui prend deux arguments : la chaîne à analyser et la base, qui sera 2 pour les nombres binaires, 8 pour les octaux et 16 pour les hexadécimaux.

```java
String binaryNumber = "1010";
int decimalFromBinary = Integer.parseInt(binaryNumber, 2);

String octalNumber = "10";
int decimalFromOctal = Integer.parseInt(octalNumber, 8);

String hexNumber = "A";
int decimalFromHex = Integer.parseInt(hexNumber, 16);
```

## Conclusion

Ce guide a couvert les quatre systèmes de numération supportés en Java : décimal, binaire, octal et hexadécimal. Il a également décrit quelques moyens simples de déclarer et de convertir des nombres entre différents systèmes de numération.

Avoir une compréhension de ces concepts est important pour tout programmeur Java, car cela permet de mettre en œuvre une manipulation et un calcul de données plus flexibles et efficaces en fonction des exigences spécifiques du projet.

Si vous souhaitez lire d'autres articles, vous êtes les bienvenus pour consulter mon [blog](https://medium.com/@mikael.lassa).