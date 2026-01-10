---
title: PHP Explode – Comment diviser une chaîne en un tableau
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-17T17:19:46.000Z'
originalURL: https://freecodecamp.org/news/php-explode-how-to-split-a-string-into-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/explode.png
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: PHP Explode – Comment diviser une chaîne en un tableau
seo_desc: 'The PHP explode() function converts a string to an array. Each of the characters
  in the string is given an index that starts from 0. Like the built-in implode()
  function, the explode function does not modify the data (string).

  Syntax of the explode()...'
---

La fonction PHP `explode()` convertit une chaîne en un tableau. Chaque caractère de la chaîne reçoit un index commençant à 0. Comme la fonction intégrée `implode()`, la fonction explode ne modifie pas les données (chaîne).

### Syntaxe de la fonction `explode()`

La fonction `explode()` prend trois paramètres :
- le séparateur
- la chaîne à convertir en tableau
- et la limite

La syntaxe complète est la suivante :
```js
explode(séparateur, chaîne, limite)
```

Contrairement à `implode()` qui fonctionne même si le séparateur n'est pas fourni, la fonction `explode()` ne fonctionnera pas sans le séparateur. Ainsi, tout comme la chaîne divisée en un tableau, le séparateur est requis. Vous pouvez utiliser le paramètre limite pour spécifier le nombre de tableaux attendus. Il est facultatif.

## Exemples de `implode()`

Supposons que j'ai la chaîne "Hello World". Si la chaîne est passée dans une fonction `explode()`, `Hello` prend un index de 0 dans le tableau, et `World` prend un index de 1. N'oubliez pas que les tableaux utilisent un indexage basé sur zéro.

```js
$str = "Hello world";
$newStr = explode(" ", $str);

// Nous imprimons un tableau, donc nous pouvons utiliser print_r()
print_r($newStr); 
```

![ss1-3](https://www.freecodecamp.org/news/content/images/2022/10/ss1-3.png)

Si vous spécifiez une limite dans la fonction `explode()`, le(s) index ne dépassera(ont) pas ce nombre. Par exemple, si vous spécifiez 2, toutes les chaînes s'afficheront, mais l'index ne dépassera pas 2.

```js
$str = "CSS, HTML, PHP, Java, JavaScript";
$newStr = explode(" ", $str, 2);

// Nous imprimons un tableau, donc nous pouvons utiliser print_r()
print_r($newStr); 
```

![ss2-3](https://www.freecodecamp.org/news/content/images/2022/10/ss2-3.png) 

Vous pouvez voir que le premier élément prend un index de 0 et le reste des éléments séparés par des virgules prend 1. L'index n'est pas supérieur à la limite de 2 spécifiée.

La fonction `explode()` recherche les espaces dans la chaîne pour diviser la chaîne en un tableau. Si vous tapez deux mots différents ensemble, ils sont traités comme un seul :

```js
$str = "CSS HTMLPHP Java JavaScript";
$newStr = explode( " ", $str);

// Nous imprimons un tableau, donc nous pouvons utiliser print_r()
print_r($newStr); 
```
![ss5-2](https://www.freecodecamp.org/news/content/images/2022/10/ss5-2.png)

Vous pouvez voir que HTML et PHP ont été imprimés ensemble car il n'y avait pas d'espace entre eux.

## Conclusion
Cet article vous a montré comment utiliser la fonction `explode()` en PHP. 

Notez que contrairement à `implode()` qui fonctionne sans le séparateur, le séparateur est très important dans `explode()`. Si vous ne spécifiez pas de séparateur, `explode()` ne fonctionnera pas comme prévu.

```js
$str = "CSS, HTML, PHP, Java, JavaScript";
$newStr = explode($str, 2);

// Nous imprimons un tableau, donc nous pouvons utiliser print_r()
print_r($newStr); 
```

![ss3-3](https://www.freecodecamp.org/news/content/images/2022/10/ss3-3.png)

Et si vous laissez le séparateur comme une chaîne vide, vous obtenez une erreur :

![ss4-3](https://www.freecodecamp.org/news/content/images/2022/10/ss4-3.png) 
 
Merci d'avoir lu.