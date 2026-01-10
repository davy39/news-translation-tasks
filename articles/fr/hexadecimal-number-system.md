---
title: Le système de numération hexadécimal expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-09T23:13:00.000Z'
originalURL: https://freecodecamp.org/news/hexadecimal-number-system
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/malte-bickel-rGYdVCMQBCY-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Le système de numération hexadécimal expliqué
seo_desc: 'Hexadecimal numbers, often shortened to “hex numbers” or “hex”, are numbers
  represented in base 16 as opposed to base 10 that we use for everyday arithmetic
  and counting.

  In practical terms, this means that each column of a number written in hexadeci...'
---

Les nombres hexadécimaux, souvent abrégés en "nombres hex" ou "hex", sont des nombres représentés en base 16, contrairement à la base 10 que nous utilisons pour l'arithmétique et le comptage quotidiens.

En termes pratiques, cela signifie que chaque colonne d'un nombre écrit en hexadécimal peut représenter jusqu'à 16 valeurs.

Les chiffres en hexadécimal utilisent les symboles standard 0, 1, 2, 3, 4, 5, 6, 7, 8 et 9 pour représenter les valeurs correspondantes, et utilisent les six premières lettres de l'alphabet pour représenter les valeurs 10 à 15 (ex. : A, B, C, D, E, F).

En programmation, nous préfixons les constantes hexadécimales avec `0x`, avec quelques exceptions.

### **Exemples et explication**

```text
0x1        ==        1
0xF        ==        15
0xFF       ==        255
0xFFF      ==        4095
0x1000     ==        4096
```

Dans le système standard en base 10, chaque colonne représente des puissances croissantes de 10, tandis qu'en base 16, chaque colonne représente des puissances croissantes de 16.

Comme on peut le voir dans l'exemple de tableau ci-dessus, avec un seul chiffre hexadécimal, nous pouvons représenter des nombres allant jusqu'à 15 inclus. Ajoutez une autre colonne et nous pouvons représenter des nombres jusqu'à 255, 4095 avec une autre colonne, et ainsi de suite.

## **Utilisations de l'hexadécimal en programmation bas niveau**

L'hexadécimal a d'abord trouvé son utilité en informatique comme une fonctionnalité de commodité.

Les données dans nos ordinateurs ont une unité de stockage commune la plus petite, l'octet. Chaque octet contient 8 bits et peut stocker un nombre compris entre 0 et 255 inclus.

L'hexadécimal a l'avantage d'être concis et d'avoir des limites bien définies.

Un seul octet est toujours représenté par deux chiffres hexadécimaux de 0x00 à 0xFF, ce dernier étant la valeur maximale par octet de 255.

La concision et la nature alignée sur les octets des nombres hexadécimaux en font un choix populaire pour les ingénieurs logiciels travaillant sur des bases de code de bas niveau ou des logiciels embarqués.

## **Utilisations des nombres hexadécimaux en JavaScript**

JavaScript prend en charge l'utilisation de la notation hexadécimale à la place de tout entier, mais pas des décimaux.

Par exemple, le nombre 2514 en hexadécimal est 0x9D2, mais il n'existe aucun moyen pris en charge par le langage pour représenter 25,14 comme un nombre hexadécimal.

L'utilisation de l'hexadécimal dans votre code est un choix personnel et stylistique, et n'a aucun effet sur la logique sous-jacente que votre code implémente.

## **Utilisations des nombres hexadécimaux en CSS**

CSS utilise depuis longtemps la notation hexadécimale pour représenter les valeurs de couleur. Considérez le sélecteur suivant :

```css
.my-container {
    background-color: #112233;
    color: #FFFFFF;
}
```

La valeur de `background-color` est en fait trois octets hexadécimaux.

Le processeur CSS traite ces derniers comme trois octets individuels, représentant le Rouge, le Vert et le Bleu.

Dans notre exemple, 11 correspond à la composante de couleur Rouge, 22 correspond à la composante de couleur Verte, et 33 à la composante de couleur Bleue.

Il n'existe actuellement aucun moyen en CSS3 de définir une couleur avec une composante alpha en utilisant l'hexadécimal. Le projet de CSS4<sup>1</sup> inclut une proposition pour permettre un octet supplémentaire afin de spécifier les valeurs alpha.

Pour l'instant, l'utilisation de la fonction standard `rgba()` est la méthode recommandée pour ajouter une valeur alpha à vos couleurs.