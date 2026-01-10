---
title: Une introduction à la syntaxe de décomposition en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-03T21:16:09.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-spread-syntax-in-javascript-fba39595922c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*wYWeW6thQtSGbuS5
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction à la syntaxe de décomposition en JavaScript
seo_desc: 'By Ashay Mandwarya ?️??

  What is it and why do we need it?


  _Photo by [Unsplash](https://unsplash.com/@thesollers?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Anton Darius | @theSollers on <a href="https://unsplash.co...'
---

Par Ashay Mandwarya 👨🏽‍💻

#### Qu'est-ce que c'est et pourquoi en avons-nous besoin ?

![Image](https://cdn-media-1.freecodecamp.org/images/kpPvb3XGdd7Dt04-ad26LV1wNB-YWlD5Uljn)
_Photo par [Unsplash](https://unsplash.com/@thesollers?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Anton Darius | @theSollers</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

La syntaxe de décomposition a été introduite dans la spécification ES6 de JavaScript. Elle s'est depuis avérée être un élément de code précieux, rendant le code propre et facile à comprendre.

MDN définit **…** comme :

> La **syntaxe de décomposition** permet à un itérable tel qu'une expression de tableau ou une chaîne d'être développé dans des endroits où zéro ou plusieurs arguments (pour les appels de fonction) ou éléments (pour les littéraux de tableau) sont attendus, ou une expression d'objet d'être développée dans des endroits où zéro ou plusieurs paires clé-valeur (pour les littéraux d'objet) sont attendues.

Nous sommes tous d'accord pour dire que la définition ci-dessus est complexe et que nous n'avons pas compris un mot de ce qu'elle essaie de dire. Alors commençons par les bases de la syntaxe de décomposition.

* L'opérateur de décomposition est simplement 3 points `...`
* Il peut être utilisé sur des itérables comme un tableau ou une chaîne.
* Il développe un itérable en ses éléments individuels
* Il peut fournir un appel de fonction avec un tableau (ou tout autre itérable) où 0 ou plusieurs arguments étaient attendus.

**Exemple**

L'extrait suivant contient une fonction appelée sum qui attend 3 arguments x, y et z. Nous avons un tableau avec 3 éléments, et nous voulons passer les éléments du tableau comme arguments de la fonction.

![Image](https://cdn-media-1.freecodecamp.org/images/3hR85inZDEf6pPSrvHNxh6nBWCtiyzMLDTCu)

Avant l'introduction de l'opérateur de décomposition, cela se faisait via la fonction apply.

Après l'introduction de l'opérateur de décomposition, cela pouvait être fait très simplement :

![Image](https://cdn-media-1.freecodecamp.org/images/GOyLsS18ND0S5WdIYUueFVTr5w5n7chDfOg4)

Comme on peut le voir dans l'extrait ci-dessus avec l'opérateur de décomposition, nous n'avons pas à utiliser la fonction apply. Cela nous évite d'écrire plus de code.

L'exemple ci-dessus donne une idée très sommaire et brève de l'opérateur de décomposition. D'abord, approfondissons les détails à ce sujet, puis nous verrons plus d'exemples.

### Syntaxe

L'opérateur de décomposition peut être utilisé de nombreuses manières et dans divers scénarios tels que

* **À l'intérieur des appels de fonction**

![Image](https://cdn-media-1.freecodecamp.org/images/GBky3Srjrr4UtzdstTzJLa1jYs95mZhfZMCT)

Lorsque utilisé dans le scénario ci-dessus, le `…` est appelé le paramètre rest. Nous verrons des exemples liés à cela dans la section exemples.

* **Création/Extension d'un tableau/itérable :**

![Image](https://cdn-media-1.freecodecamp.org/images/plbemKpJR4jYL1RxOpQykp6DLOwKRgU0zAIK)

### Exemples

* **En tant que rest**

… est utilisé comme argument pour une fonction variadique. Une fonction variadique est une fonction qui peut avoir un nombre variable de paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/E65KbaqcTyzOKHExPf06s1PxCeNN5ecEg9qQ)

Ici, lorsque nous retournons args, nous voyons que nous obtenons notre tableau que nous avons passé en tant que valeurs séparées dans l'appel. Cela montre que l'opérateur rest fonctionne exactement à l'opposé de la syntaxe de décomposition. L'un développe et l'autre condense la valeur.

Une autre chose à noter est qu'il n'y a pas de nombre spécifique de paramètres mentionné dans la définition de la fonction. Cela signifie qu'en utilisant … la fonction peut avoir n nombre d'arguments. Nous n'avons pas besoin de spécifier les paramètres à l'avance.

C'est particulièrement une manière très flexible de recevoir des arguments pour une fonction pour laquelle le nombre spécifique d'arguments n'est pas déterminé comme les fonctions Math.max et Math.min. Ce sont des fonctions variadiques car le nombre d'entrées peut être infini pour elles.

Revenons à l'exemple, pour obtenir la somme de tous les arguments

![Image](https://cdn-media-1.freecodecamp.org/images/GGxZLLfTPqmxmoz4UWDs9QC0gcPwfTY79mRb)

Nous devons itérer le tableau et ajouter tous les éléments individuels pour produire le résultat.

* **Pousser des éléments dans un tableau**

La fonction push() est utilisée pour pousser des éléments dans un tableau. La limitation avec push est que nous devons pousser les éléments un par un (push(1,2,3)). Si un tableau dont les éléments doivent être insérés dans le tableau en utilisant push, nous obtiendrons un tableau multidimensionnel, ce que nous n'avons pas demandé.

![Image](https://cdn-media-1.freecodecamp.org/images/jDIOeXcE5FWI28Pd3ZvA2glor-bky4ULBLRn)

Encore une fois, apply vient à la rescousse

![Image](https://cdn-media-1.freecodecamp.org/images/A8ehvgpbQXdo5QjrEV01luli6oiXLS2RGv12)

Comme nous pouvons le voir, l'utilisation de apply ne semble pas très élégante et nous avons besoin d'une syntaxe simple et petite pour le faire. Utilisons la décomposition …

![Image](https://cdn-media-1.freecodecamp.org/images/7mVMylAGnatsCSTGdBWyn5Fo2oZ70UWUNwLW)

Élégant !

* **Copier un tableau**

![Image](https://cdn-media-1.freecodecamp.org/images/PjvE5dPbLmi1dK0UDrBH95ads1-wlP-ADGMN)

Simple !

Le même résultat peut être produit en utilisant un objet

![Image](https://cdn-media-1.freecodecamp.org/images/YYlEmAxXhv2fZ0C0ROiBC74mbRP1mWesgHI5)

* **Concaténer 2 tableaux**

La concaténation est faite en utilisant la fonction concat

![Image](https://cdn-media-1.freecodecamp.org/images/WlYNJfs0jB6Hw4Y3VttUHTn8lI6S5FDiiidQ)

Le même résultat peut être obtenu en utilisant l'opérateur …

![Image](https://cdn-media-1.freecodecamp.org/images/eSN8Hm-y7BbaBtEXHU9k5SfMHbeK8IyPO3hQ)

* **Convertir une chaîne en tableau**

Cela peut être fait en utilisant à la fois la fonction split et l'opérateur …

![Image](https://cdn-media-1.freecodecamp.org/images/vHzSvkmtOb1eLW8XuoLhVOtsEYP4-ZuVFa1-)

![Image](https://cdn-media-1.freecodecamp.org/images/0hJH3tYjZ96gDMlAVioIG9hoK4p1Zo-RVCEv)

* **Utilisation dans les fonctions max et min**

L'extrait suivant tente de trouver l'élément maximum dans le tableau, donc nous passons le tableau entier dans la fonction mais nous obtenons le résultat comme NaN

![Image](https://cdn-media-1.freecodecamp.org/images/rGe20ar6559QFEyd1NzdUF8S-2Z2VqR6S13p)

Nous pouvons utiliser apply, mais comme vu dans les exemples précédents, je déteste l'utiliser

![Image](https://cdn-media-1.freecodecamp.org/images/4318SrchWxeR0K2k9GTS45C0DH1i0I5ZqUBy)

Même chose pour min

![Image](https://cdn-media-1.freecodecamp.org/images/SnMeVaTIwhsxcJYIzHn34touLSHHJaODLhJO)

### Conclusion

Nous avons vu de nombreuses situations où l'opérateur de décomposition s'avère utile et réduit notre code tout en le rendant super facile à comprendre.

Si vous aimez cela, applaudissez 👏 et suivez 🚀 pour plus.

![Image](https://cdn-media-1.freecodecamp.org/images/QM0OaPVNzU78PsxECtJR-DrVQBUFaXN15dT7)
_Google_