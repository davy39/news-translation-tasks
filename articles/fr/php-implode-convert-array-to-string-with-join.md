---
title: PHP Implode – Convertir un tableau en chaîne de caractères avec Join
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-10-06T16:14:10.000Z'
originalURL: https://freecodecamp.org/news/php-implode-convert-array-to-string-with-join
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/implode.png
tags:
- name: arrays
  slug: arrays
- name: PHP
  slug: php
seo_title: PHP Implode – Convertir un tableau en chaîne de caractères avec Join
seo_desc: "In PHP, the implode() function is a built-in function that takes an array\
  \ and converts it to a string. implode() doesn’t modify the original array. \nIt\
  \ doesn’t matter whether the array is an indexed or associative array. Once you\
  \ pass in the array to..."
---

En PHP, la fonction `implode()` est une fonction intégrée qui prend un tableau et le convertit en une chaîne de caractères. `implode()` ne modifie pas le tableau d'origine.

Peu importe que le tableau soit un tableau indexé ou associatif. Une fois que vous passez le tableau à `implode()`, il joint toutes les valeurs en une chaîne.

## Syntaxe de `implode()` en PHP
`implode()` prend deux valeurs en paramètres – le séparateur et le tableau que vous souhaitez convertir en chaîne.

Le séparateur peut être n'importe quel caractère ou une chaîne vide. Il est valide tant que vous le spécifiez entre guillemets. Si vous ne passez pas le séparateur, `implode()` fonctionne toujours. Le tableau, quant à lui, peut être un tableau associatif ou un tableau indexé.

NB : `implode()` ne fonctionne pas avec les tableaux imbriqués.

La syntaxe complète d'un `implode()` ressemble à ceci :

```js
implode(" ", $array);
```

Dans la syntaxe ci-dessus, un espace vide (" ") est le séparateur, et `$array` est le tableau.

## Exemples d'implode avec un tableau indexé
En PHP, un tableau indexé est exactement ce qu'il semble être – chaque valeur du tableau possède un index qui lui est automatiquement attribué. Vous pouvez également attribuer les index si vous le souhaitez.

Voici un exemple du fonctionnement de `implode()` avec un tableau indexé :

```js
<?php
$langs = array("PHP", "JavaScript", "Python", "C++", "Ruby"); 

$newLangs = implode($langs);
// Puisque nous affichons une chaîne, nous pouvons utiliser echo pour afficher le résultat dans le navigateur
echo $newLangs;
?>
```

![ss1-2](https://www.freecodecamp.org/news/content/images/2022/10/ss1-2.png) 

Notez que je n'ai pas passé de séparateur et `implode()` fonctionne toujours très bien.
Dans l'exemple ci-dessous, j'ai passé un espace vide, une virgule et un trait d'union comme séparateurs :

```js
<?php
$langs = array("PHP", "JavaScript", "Python", "C++", "Ruby"); 

$newLangsSpace = implode(" ", $langs);
$newLangsComma = implode(", ", $langs);
$newLangsHyphen = implode("-", $langs);

// Puisque nous affichons une chaîne, nous pouvons utiliser echo pour afficher le résultat dans le navigateur
echo $newLangsSpace."<br>"."<br>";
echo $newLangsComma."<br>"."<br>";
echo $newLangsHyphen ."<br>";
?>
```

![ss2-2](https://www.freecodecamp.org/news/content/images/2022/10/ss2-2.png) 

Vous pouvez voir qu'il est préférable de spécifier un séparateur pour bien voir les valeurs.

## Exemples d'implode avec un tableau associatif
Vous définissez un index nommé avec un tableau associatif. Voyons comment `implode()` fonctionne avec les tableaux associatifs.

```js
<?php
$person = [
    'first_name' => "Kolade",
    'last_name' => "Chris",
    'likes' => "football and Pro-wrestling",
    'email' => "kolade@gmail.com",
];
// Ce n'est pas mon e-mail. Ne vous donnez pas la peine de m'envoyer un message.

$newPerson = implode(" ", $person);
echo $newPerson."<br>";
?>
```

![ss3-2](https://www.freecodecamp.org/news/content/images/2022/10/ss3-2.png) 

Vous pouvez voir que les index n'ont pas été affichés. Pour afficher également les index, vous devez attacher le tableau à la méthode `array_keys()` lors de l'affichage du tableau :

```js
<?php
$person = [
    'first_name' => "Kolade",
    'last_name' => "Chris",
    'likes' => "football and Pro-wrestling",
    'email' => "kolade@gmail.com",
];
// Ce n'est pas mon e-mail. Ne vous donnez pas la peine de m'envoyer un message.

$newPersonValues = implode(", ", $person)."<br>";
$newPersonKeys = implode(", ", array_keys($person));

echo $newPersonKeys."<br>"; 
echo $newPersonValues;
?>
```

![ss4-2](https://www.freecodecamp.org/news/content/images/2022/10/ss4-2.png) 

Pour prouver que le tableau d'origine n'est jamais modifié, j'afficherai le tableau à côté des variables implosées :

```js
<?php
$person = [
    'first_name' => "Kolade",
    'last_name' => "Chris",
    'likes' => "football and Pro-wrestling",
    'email' => "kolade@gmail.com",
];
// Ce n'est pas mon e-mail. Ne vous donnez pas la peine de m'envoyer un message.

$newPersonValues = implode(", ", $person)."<br>";
$newPersonKeys = implode(", ", array_keys($person));

echo $newPersonKeys."<br>"; 
echo $newPersonValues."<br>";

print_r($person);
?>
```

Vous pouvez utiliser l'extension Chrome PHP View pour formater votre tableau affiché afin qu'il soit plus lisible :

![phpViewer](https://www.freecodecamp.org/news/content/images/2022/10/phpViewer.png) 

## Dernières réflexions
Dans cet article, vous avez découvert la fonction `implode()` en PHP et son fonctionnement. Nous avons également vu comment la fonction `implode()` fonctionne avec les tableaux indexés et associatifs, à l'aide d'exemples.

N'oubliez pas que `implode()` ne fonctionne pas avec les tableaux imbriqués (tableaux multidimensionnels). En fait, je peux le prouver :

```js
<?php
$persons = array (
  array("Kolade", 22, 03),
  array("Yemi", 15, 12),
  array("Cook", 07, 01),
  array("Oliver", 19, 01)
);

$newPersons = implode($persons);
print_r($newPersons);
?>
```

![ss6-2](https://www.freecodecamp.org/news/content/images/2022/10/ss6-2.png) 

Cela ne fonctionne pas ainsi car `implode()` ne fonctionne qu'avec des tableaux plats (`[ ]`) au lieu de tableaux multidimensionnels (`[ [ ] ]`). Implode examine le premier tableau, et une fois qu'il voit que le premier tableau contient plusieurs tableaux, il renvoie une erreur.

Merci de votre lecture.