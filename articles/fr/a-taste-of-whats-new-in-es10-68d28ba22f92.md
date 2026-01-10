---
title: Un aperçu des nouveautés d'ES10
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T17:06:20.000Z'
originalURL: https://freecodecamp.org/news/a-taste-of-whats-new-in-es10-68d28ba22f92
coverImage: https://cdn-media-1.freecodecamp.org/images/0*DiulTq2UG0G7_Jrf
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un aperçu des nouveautés d'ES10
seo_desc: 'By Ashay Mandwarya ?️??

  Every year, a new version of ECMAScript is released with the proposals which are
  officially ready for distribution to devs and users alike. This article will be
  discussing the latest iteration of the language, and what new fea...'
---

Par Ashay Mandwarya 👨🏽‍💻

Chaque année, une nouvelle version d'ECMAScript est publiée avec les propositions qui sont officiellement prêtes pour la distribution aux développeurs et aux utilisateurs. Cet article discutera de la dernière itération du langage et des nouvelles fonctionnalités qu'elle apporte.

**ES10/ES2019** a apporté de grandes améliorations dans cette mise à jour. Il introduit des fonctions et des méthodes qui permettront aux développeurs d'écrire moins de code et de faire un travail plus productif.

**Commençons sans plus tarder.**

### flat()

flat() est une méthode utilisée pour aplatir un tableau. Il existe certaines situations où les éléments d'un tableau sont eux-mêmes des tableaux. Ces types de tableaux sont appelés tableaux imbriqués.

Normalement, pour les désimbriquer (aplatir), nous devions utiliser la récursivité. Maintenant, avec l'introduction de flat(), cela peut être fait en une seule ligne. Pour information, un tableau aplati est un tableau de profondeur 0. flat() prend un argument, un nombre qui représente la profondeur. La profondeur est le niveau d'imbrication à l'intérieur d'un tableau. Voyons un exemple expliquant l'imbrication et la profondeur.

![Image](https://cdn-media-1.freecodecamp.org/images/QUDBVgv-56mkzLWlS5yz04WXxldztqBFW5Ob)
_Un tableau de profondeur 3_

Le tableau ci-dessus est un tableau de profondeur 3. C'est un tableau à l'intérieur d'un tableau, à l'intérieur d'un tableau, à l'intérieur d'un tableau 🤯. Généralement, en JavaScript, un tableau peut avoir une profondeur infinie ou jusqu'à ce que vous manquez de mémoire. Supposons qu'un tableau ait une profondeur d'imbrication de 3 et que nous l'aplatissions seulement jusqu'à une profondeur de 2, alors il y aura encore un tableau imbriqué à l'intérieur du tableau principal.

#### **Syntaxe**

![Image](https://cdn-media-1.freecodecamp.org/images/7PGK5m4DnlCd5ba8m8ScN8PI1omeKLB91OS5)

#### **Retourne**

Il retourne un tableau aplati.

#### Exemple

![Image](https://cdn-media-1.freecodecamp.org/images/ATwKx7nwYwfJ3Pr1bntIsdYSk7QKsg-dMmTr)

Le tableau imbriqué de profondeur 3 est aplati en utilisant flat avec une profondeur de 3.

Si nous mettons la profondeur à 2, nous obtenons ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Q6EA0RBJSfec7TcQ7oIZks09NOudcEQ6J86w)

Nous pouvons voir qu'il reste encore un tableau non aplati dans la sortie.

### **flatMap()**

flatMap() est utilisé pour aplatir un tableau imbriqué et pour modifier les valeurs selon une fonction comme une fonction map(). Cette fonction travaille sur un tableau et prend une fonction de rappel comme argument. La fonction de rappel dicte comment le tableau doit être aplati. Elle fonctionne comme un map, mais en plus, elle l'aplatit également. Si vous voulez en savoir plus sur les maps, consultez [cet](https://hackernoon.com/map-filter-reduce-ebbed4be4201) article.

flatMap() peut être utilisé pour aplatir un tableau de profondeur 1 seulement, car en interne, il appelle une fonction map suivie d'une fonction flat avec une profondeur de 1.

#### **Syntaxe**

![Image](https://cdn-media-1.freecodecamp.org/images/-JLMPV4UYEggPQoN6iU6LnN2unU0SlrparOw)

#### **Retourne**

Un tableau aplati avec des valeurs manipulées grâce à la fonction de rappel qui lui est fournie. Tout comme un map.

**map()**+**flat()**=&**gt;flatma**p()

#### Exemple

![Image](https://cdn-media-1.freecodecamp.org/images/CCBG2KFQbF63sdLnICx4jf7A8iAOA30QHvpJ)

Dans cet exemple, map et flatMap sont montrés l'un après l'autre pour montrer la différence entre les deux fonctions. map() retourne un tableau de tableaux qui contenaient les valeurs, tandis que la sortie de flatMap() était la même que map, en plus de l'aplatissement du tableau.

### Object.fromEntries()

Une autre fonction très utile. Object.fromEntries est utilisé pour former des objets à partir d'une paire clé-valeur fournie. Il prend une liste de paires clé-valeur et retourne un objet dont les propriétés sont données par les entrées. Il fonctionne comme l'inverse de **Object.entries()**.

#### **Paramètres**

Il prend n'importe quel itérable, c'est-à-dire un tableau.

#### **Retourne**

Il retourne un objet avec les paires clé-valeur données.

#### **Exemple**

![Image](https://cdn-media-1.freecodecamp.org/images/OL255RjE690hCSdMN9hq567NXpI6zR4GXioW)

Nous pouvons voir que lorsque nous avons fourni une map (qui stocke des valeurs en paires) à la fonction fromEntries(), nous obtenons un objet avec les paires clé-valeur respectives comme dans la map.

### trimStart()

La méthode trimStart() supprime les espaces blancs au début d'une chaîne. trimLeft() est un alias de cette méthode.

#### **Syntaxe**

![Image](https://cdn-media-1.freecodecamp.org/images/xyYdL1RkMnebTKlvSkqFuSfcom7TyS7OsI1i)

#### **Retourne**

Elle retourne une chaîne avec les espaces blancs au début supprimés.

#### **Exemple**

![Image](https://cdn-media-1.freecodecamp.org/images/8syOWHSR0HNlxxwrpzB53SyUcoZcyDdu88Kt)

Nous pouvons clairement voir les espaces blancs supprimés dans la sortie.

### trimEnd()

La méthode trimEnd() supprime les espaces blancs à la fin d'une chaîne. trimRight() est un alias de cette méthode.

#### **Syntaxe**

![Image](https://cdn-media-1.freecodecamp.org/images/H15TWnL1dwUbOWTyiNWvy7NrohUHI9rah1PL)

#### **Retourne**

Elle retourne une chaîne avec tous les espaces supprimés à la fin.

#### **Exemple**

![Image](https://cdn-media-1.freecodecamp.org/images/D-VXK9s3JgxhALJPet71YfkS-iLfMsb2Tomh)

Nous pouvons clairement voir que les espaces à la fin sont supprimés.

### **Changements dans la liaison catch**

Jusqu'à ES10, nous étions obligés par la syntaxe de lier une variable d'exception pour la clause catch, que ce soit nécessaire ou non. De nombreuses fois, on peut remarquer que le bloc catch est simplement redondant. La proposition ES10 nous permet de simplement omettre la variable, nous donnant une chose de moins à laquelle penser.

#### **Exemple**

![Image](https://cdn-media-1.freecodecamp.org/images/8Ljl779UXBNH5uwn2GdtB0xzbQlrSyCjppkZ)

Dans l'exemple ci-dessus, nous pouvons voir qu'aucune variable n'est à fournir à catch pour qu'il s'exécute.

### Description du Symbole

Lorsque nous créons un Symbole en JS, il est possible de spécifier une description qui peut être utilisée pour le débogage plus tard. Le processus de récupération de cette description est un peu fastidieux. Nous devons reconstruire le Symbole à nouveau et avec l'aide de la méthode toString() pour accéder à la description.

ES10 ajoute une nouvelle propriété en lecture seule appelée description, qui retourne la description du Symbole.

#### **Exemple**

![Image](https://cdn-media-1.freecodecamp.org/images/Tb8bH2d2Bpv0UiowLyz1JS06GJ6HwXPCHqbh)

Nous pouvons voir que nous obtenons directement la description en utilisant la propriété .description du Symbole.

### Conclusion

Ce sont quelques-unes des fonctionnalités qui vont être introduites dans la norme ES10 actuelle. J'espère que vous avez apprécié l'article ! Merci pour la lecture.

![Image](https://cdn-media-1.freecodecamp.org/images/pZsQZzx0nRyznNDnWEa2-9xpJ0d93RF5mExF)
_Google