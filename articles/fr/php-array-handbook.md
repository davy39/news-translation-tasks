---
title: Guide complet des tableaux en PHP – Comment créer, manipuler et parcourir des
  tableaux
date: '2024-05-08T22:25:55.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/php-array-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/PHP-Array-Handbook-Cover-1.png
tags:
- name: arrays
  slug: arrays
- name: handbook
  slug: handbook
- name: PHP
  slug: php
seo_desc: In every programming language, arrays provide a flexible option to store
  more than one data type in a single variable. They are one of the most versatile
  data structures in the programming world, which is one reason a lot of external
  data and many AP...
---


Dans chaque langage de programmation, les tableaux offrent une option flexible pour stocker plusieurs types de données dans une seule variable. Ils constituent l'une des structures de données les plus polyvalentes du monde de la programmation, ce qui explique pourquoi de nombreuses données externes et de nombreuses API sont transmises sous forme de tableaux.

<!-- more -->

Lorsque vous créez un tableau en PHP, vous voudrez pouvoir l'utiliser. Pour ce faire, vous devez le manipuler ou le parcourir. PHP fournit plusieurs fonctions intégrées pour manipuler les tableaux et plusieurs façons de les parcourir.

Comprendre et utiliser ces fonctions intégrées et ces boucles est essentiel pour une manipulation efficace des tableaux. Grâce à elles, vous gagnerez du temps, écrirez un code plus propre et deviendrez un développeur PHP plus efficace.

Notez que ceci est la première partie d'une série de deux articles. La deuxième partie se concentrera sur l'utilisation de MongoDB en PHP en reconstruisant le projet "Football Team Cards". Les footballeurs proviendront d'une base de données MongoDB Atlas. Nous les récupérerons ensuite sous forme de tableaux pour les afficher sur la page.

## Ce que nous allons aborder

-   [Comment créer des tableaux en PHP][1]
    -   [Comment créer des tableaux avec la fonction array()][2]
    -   [Comment créer des tableaux avec la syntaxe des crochets][3]
-   [Comment afficher des tableaux en PHP][4]
    -   [Comment afficher un tableau avec la fonction `print_r()`][5]
    -   [Comment afficher un tableau avec la fonction var\_dump()][6]
-   [Fonctions de tableaux PHP][7]
    -   [La fonction de tableau `count()`][8]
    -   [La fonction de tableau `array_push()`][9]
    -   [La fonction `array_pop()`][10]
    -   [La fonction `array_shift()`][11]
    -   [La fonction `array_unshift()`][12]
    -   [La fonction `array_splice()`][13]
    -   [La fonction `array_keys()`][14]
    -   [La fonction `array_values()`][15]
    -   [La fonction `array_reduce()`][16]
    -   [La fonction `sort()`][17]
    -   [La fonction `rsort()`][18]
    -   [La fonction `array_replace()`][19]
    -   [La fonction `array_reverse()`][20]
    -   [La fonction `array_slice()`][21]
    -   [La fonction `array_sum()`][22]
    -   [La fonction `array_merge()`][23]
    -   [La fonction `array_filter()`][24]
    -   [La fonction `array_map()`][25]
    -   [La fonction `array_search()`][26]
    -   [La fonction `array_column()`][27]
    -   [La fonction `in_array()`][28]
-   [Comment parcourir des tableaux en PHP][29]
    -   [Comment parcourir un tableau indexé][30]
    -   [Comment parcourir un tableau associatif][31]
    -   [Comment parcourir un tableau à l'intérieur d'un template HTML][32]
-   [Conclusion][33]

## Comment créer des tableaux en PHP

En PHP, les tableaux existent sous 3 formes :

-   **indexé** – un tableau classique avec des index prédéfinis
-   **multidimensionnel** – un tableau contenant d'autres tableaux
-   **associatif** – un tableau avec des index sous forme de chaînes de caractères (clés)

Il existe deux façons de créer l'une de ces 3 formes de tableaux en PHP. Vous pouvez soit utiliser la fonction `array()`, soit la syntaxe des crochets (`[ ]`).

### Comment créer des tableaux avec la fonction array()

Pour créer un tableau PHP avec la fonction `array()`, il suffit de passer les éléments dans la fonction.

Voici le principe :

-   un **tableau classique** est créé avec la fonction `array()` en passant les éléments directement dans la fonction
-   un **tableau multidimensionnel** est créé avec la fonction `array()` en imbriquant une ou plusieurs fonctions `array()` à l'intérieur d'une fonction `array()`
-   un **tableau associatif** est créé avec la fonction `array()` en séparant la clé et les valeurs par une flèche grasse (`=>`) et en séparant chaque entrée par une virgule

Voici des exemples de chacun d'eux en code :

```
// tableau classique avec la fonction array
$myFruitsArr1 = array("Apple", "Banana", "Cashew", "Mango");


// tableau multidimensionnel avec la fonction array
$myFruitsArr2 = array(
 array("Apple", "Avocado", "Apricot"),
 array("Banana", "Blackeberry", "Babaco"),
 array("Cashew", "Cherry", "Canary melon"),
 array("Mango", "Melon", "Miracle fruit"),
);


// tableau associatif avec la fonction array
$myFruitsArr3 = array(
 "fruit 1" => "Apple",
 "fruit 2" => "Banana",
 "fruit 3" => "Cashew",
 "fruit 4" => "Mango",
);
```

### Comment créer des tableaux avec la syntaxe des crochets

La syntaxe des crochets est la méthode la plus courante pour créer un tableau en PHP (ainsi qu'en JavaScript).

Pour créer un tableau avec la syntaxe des crochets, remplacez chaque occurrence de `array()` par des crochets ouvrants et fermants :

```
// tableau classique avec la syntaxe des crochets
$myFruitsArr1 = ["Apple", "Banana", "Cashew", "Mango"];


// tableau multidimensionnel avec la syntaxe des crochets
$myFruitsArr2 = [
 ["Apple", "Avocado", "Apricot"],
 ["Banana", "Blackeberry", "Babaco"],
 ["Cashew", "Cherry", "Canary melon"],
 ["Mango", "Melon", "Miracle fruit"],
];


// tableau associatif avec la syntaxe des crochets
$myFruitsArr3 = [
 "fruit 1" => "Apple",
 "fruit 2" => "Banana",
 "fruit 3" => "Cashew",
 "fruit 4" => "Mango",
];
```

## Comment afficher des tableaux en PHP

La plupart du temps, vous pourriez avoir besoin d'afficher un tableau à des fins de débogage ou de visualisation. PHP fournit l'instruction `echo`, ainsi que les fonctions `print_r()` et `var_dump()` pour afficher des données.

`echo` n'affiche pas un tableau correctement car il est destiné à l'affichage de chaînes de caractères, d'entiers et de flottants. Vous devriez utiliser `print_r()` et `var_dump()` pour afficher des tableaux à la place.

### Comment afficher un tableau avec la fonction `print_r()`

La fonction `print_r()` affiche des informations structurées sur une variable dans un format lisible par l'homme.

`print_r()` est particulièrement utile pour afficher et inspecter le contenu de structures de données complexes comme les tableaux et les objets. Vous l'utilisez en lui passant l'identifiant du tableau :

```
print_r($myFruitsArr1);
print_r($myFruitsArr2);
print_r($myFruitsArr3);
```

Même si le tableau ou l'objet possède des éléments imbriqués, `print_r()` parcourra l'intégralité du tableau ou de l'objet et affichera le contenu sans oublier aucun élément.

Voici à quoi ressemblent chacun des 3 types de tableaux lorsque vous les affichez avec la fonction `print_r()` :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image6-1.png) _Exemples de tableaux classiques, multidimensionnels et associatifs._

### Comment afficher un tableau avec la fonction `var_dump()`

La fonction `var_dump()` vous permet d'afficher un tableau ou une variable comme la fonction `print_r()`. Ce qu'elle fait différemment, c'est qu'elle affiche le type de données de ce que vous imprimez, y compris pour chaque élément du tableau.

Voici comment utiliser la fonction `var_dump()` :

```
var_dump($myFruitsArr1);
var_dump($myFruitsArr2);
var_dump($myFruitsArr3);
```

Et voici à quoi ressemblent chacun des 3 types de tableaux lorsque vous les affichez avec la fonction `var_dump()` :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image3.png) _Tableaux classiques, multidimensionnels et associatifs affichés avec var_dump()_

## Fonctions de tableaux PHP

PHP propose une riche variété de fonctions de tableaux. Elles vous permettent d'effectuer un large éventail d'opérations, de la manipulation de base au traitement de données avancé.

Il existe plus de 70 fonctions de tableaux que vous pouvez utiliser en PHP, nous ne pourrons donc pas toutes les couvrir dans ce guide.

Voici celles que nous allons aborder :

-   `count()`
-   `array_push()`
-   `array_pop()`
-   `array_shift()`
-   `array_unshift()`
-   `array_splice()`
-   `array_keys()`
-   `array_values()`
-   `array_reduce()`
-   `sort()`
-   `rsort()`
-   `array_replace()`
-   `array_reverse()`
-   `array_slice()`
-   `array_sum()`
-   `array_merge()`
-   `array_filter()`
-   `array_map()`
-   `array_search()`
-   `array_column()`
-   `in_array()`

### La fonction de tableau `count()`

La fonction `count()` fait ce que son nom indique : elle parcourt un tableau, compte les éléments et renvoie un entier représentant la longueur du tableau.

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
echo count($myFruitsArr); // 4
```

`count()` peut être utile si vous voulez effectuer une action basée sur la longueur d'un tableau particulier :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];


if (count($myFruitsArr) === 4) {
 echo "Il y a assez de fruits";
} else {
 echo "Il n'y a pas assez de fruits";
}


// Il y a assez de fruits
```

Parce que `count()` obtient la longueur d'un tableau, elle est couramment utilisée dans les boucles :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];


for ($i = 0; $i < count($myFruitsArr); $i++) {
 echo $myFruitsArr[$i] . "<br>";
}


/*
Sortie :


Apple
Banana
Cashew
Mango
*/
```

### La fonction de tableau `array_push()`

`array_push()` "pousse" un élément à la fin du tableau. C'est-à-dire qu'elle ajoute un élément spécifié après le dernier élément du tableau. Cela signifie qu'elle modifie le tableau original.

`array_push` prend un argument `array` obligatoire et l'élément que vous souhaitez ajouter au tableau existant :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];


array_push($myFruitsArr, "Avocado");
print_r($myFruitsArr); // Array ( [0] => Apple [1] => Banana [2] => Cashew [3] => Mango [4] => Avocado )
```

Vous pouvez afficher la balise `<pre>` pour mieux formater le tableau résultant :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];


array_push($myFruitsArr, "Avocado");
echo "<pre>";
var_dump($myFruitsArr);
echo "<pre>";


/*
Sortie :


array(5) {
 [0]=>
 string(5) "Apple"
 [1]=>
 string(6) "Banana"
 [2]=>
 string(6) "Cashew"
 [3]=>
 string(5) "Mango"
 [4]=>
 string(7) "Avocado"
}
*/
```

Vous pouvez également ajouter deux éléments ou plus :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];


array_push($myFruitsArr, "Avocado", "Pineapple");
echo "<pre>";
var_dump($myFruitsArr);
echo "<pre>";


/*
Sortie :


array(6) {
 [0]=>
 string(5) "Apple"
 [1]=>
 string(6) "Banana"
 [2]=>
 string(6) "Cashew"
 [3]=>
 string(5) "Mango"
 [4]=>
 string(7) "Avocado"
 [5]=>
 string(9) "Pineapple"
}
*/
```

### La fonction `array_pop()`

`array_pop()` fait le contraire de ce que fait `array_push()` – **elle supprime un élément de la fin du tableau**. Cela signifie qu'elle peut être utile dans les structures de données de type pile (stack).

Pour utiliser la fonction `array_pop()`, il vous suffit de passer le tableau duquel vous voulez supprimer l'élément :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
array_pop($myFruitsArr);


echo "<pre>";
var_dump($myFruitsArr);
echo "<pre>";


/*
Mango a disparu :


array(3) {
 [0]=>
 string(5) "Apple"
 [1]=>
 string(6) "Banana"
 [2]=>
 string(6) "Cashew"
}
*/
```

Vous pouvez afficher l'élément supprimé car `array_pop()` modifie le tableau original et retourne la valeur supprimée :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
$poppedElem = array_pop($myFruitsArr);


echo $poppedElem; // Mango
```

### La fonction `array_shift()`

`array_shift()` est similaire à `array_pop`, mais elle supprime le premier élément d'un tableau et non le dernier. Elle est donc utile dans les structures de données de type file (queue).

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
array_shift($myFruitsArr);
var_dump($myFruitsArr);


/*
Apple a disparu :


array(3) {
 [0]=>
 string(6) "Banana"
 [1]=>
 string(6) "Cashew"
 [2]=>
 string(5) "Mango"
}
*/
```

Parce que la fonction `array_shift()` modifie le tableau original, elle réindexe les éléments :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];


echo "avant shift : ";
var_dump($myFruitsArr);


echo "<br>";


echo "après shift : ";
array_shift($myFruitsArr);
var_dump($myFruitsArr);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image5.png) _Avant et après l'utilisation de la fonction shift()_

`array_shift()` retourne également l'élément supprimé :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
$shiftedElem = array_shift($myFruitsArr);

echo $shiftedElem; // Apple
```

### La fonction `array_unshift()`

La fonction `array_unshift()` ajoute un ou plusieurs éléments au début d'un tableau. Elle modifie le tableau original en insérant les nouveaux éléments au début et en réindexant les éléments existants.

Elle prend comme arguments le tableau auquel vous voulez ajouter des éléments et l'élément que vous voulez ajouter.

Voici un exemple :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
array_unshift($myFruitsArr, "Avocado");

var_dump($myFruitsArr);

/*
array(5) {
 [0]=>
 string(7) "Avocado"
 [1]=>
 string(5) "Apple"
 [2]=>
 string(6) "Banana"
 [3]=>
 string(6) "Cashew"
 [4]=>
 string(5) "Mango"
}
*/
```

### La fonction `array_splice()`

La méthode `array_splice()` supprime un élément d'un tableau et le remplace par le remplacement spécifié. `array_splice()` modifie le tableau original et retourne les éléments supprimés.

`array_splice()` prend jusqu'à 4 arguments, comme vous pouvez le voir dans sa syntaxe de base ci-dessous :

```
array_splice(array, startingIndex, length, replacement)
```

-   `array` est le tableau sur lequel vous utilisez la fonction `array_splice()`
-   `startingIndex` est la position où vous voulez commencer à supprimer l'élément ou les éléments dans le tableau. Si vous spécifiez `0`, cela supprimera le premier élément.
-   `length` est la longueur de la découpe. Par exemple, si vous spécifiez `2`, deux éléments seront supprimés à partir de l'index `startingIndex` spécifié.
-   `replacement` est l'élément qui remplacera l'élément à supprimer. Il peut s'agir d'un seul élément ou d'un autre tableau.

Voici un exemple avec un tableau et un remplacement par une chaîne de caractères :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
$splicedItem = array_splice($myFruitsArr, 1, 1, "Avocado");

var_dump($myFruitsArr);

/*
Sortie :

array(4) {
 [0]=>
 string(5) "Apple"
 [1]=>
 string(7) "Avocado"
 [2]=>
 string(6) "Cashew"
 [3]=>
 string(5) "Mango"
}
*/
echo "<br>";

var_dump($splicedItem);

/*
Sortie :
array(1) {
 [0]=>
 string(6) "Banana"
}
*/
```

Voici un autre exemple avec un tableau comme remplacement :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
$splicedItem = array_splice($myFruitsArr, 1, 1, array("Avocado", "Apricot", "Abiu"));

var_dump($myFruitsArr);
/*
Sortie :

array(6) {
 [0]=>
 string(5) "Apple"
 [1]=>
 string(7) "Avocado"
 [2]=>
 string(7) "Apricot"
 [3]=>
 string(4) "Abiu"
 [4]=>
 string(6) "Cashew"
 [5]=>
 string(5) "Mango"
}
*/

var_dump($splicedItem);
/*
Sortie :

array(1) {
 [0]=>
 string(6) "Banana"
}
*/
```

### La fonction `array_keys()`

Il y a deux composants dans chaque tableau : les clés et les valeurs. Pour un tableau classique, les clés sont les index numériques. Pour un tableau associatif, les clés sont les indices textuels spécifiés pour chaque élément.

La fonction `array_keys` extrait les clés des éléments d'un tableau.

Si le tableau est un tableau classique, elle liste les indices du tableau comme clés :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
$myFruitsArrKeys = array_keys($myFruitsArr);

print_r($myFruitsArrKeys);
/*
Sortie :

Array
(
   [0] => 0
   [1] => 1
   [2] => 2
   [3] => 3
)
*/
```

Si le tableau est un tableau associatif, elle liste les clés que vous avez spécifiées pour chaque élément :

```
$myFruitsWithColors = [
 "apple" => "red",
 "banana" => "yellow",
 "orange" => "orange",
 "grape" => "purple",
 "watermelon" => "green",
];

$myFruitsWithColorsKeys = array_keys($myFruitsWithColors);

print_r($myFruitsWithColorsKeys);
/*
Sortie :

Array
(
   [0] => apple
   [1] => banana
   [2] => orange
   [3] => grape
   [4] => watermelon
)
*/
```

`array_keys()` peut accepter un deuxième argument. Il s'agit généralement d'une valeur présente dans le tableau.

Si vous spécifiez une valeur en deuxième argument, `array_keys()` renverra uniquement la clé correspondant à cette valeur :

```
$myFruitsWithColors = [
 "apple" => "red",
 "banana" => "yellow",
 "orange" => "orange",
 "grape" => "purple",
 "watermelon" => "green",
];

$myFruitsWithColorsKeys = array_keys($myFruitsWithColors, "orange");

print_r($myFruitsWithColorsKeys);
/*
Sortie :

Array
(
   [0] => orange
)
*/
```

### La fonction `array_values()`

La fonction `array_values()` extrait l'autre partie d'un tableau – les valeurs.

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
$myFruitsArrValues = array_values($myFruitsArr);

print_r($myFruitsArrValues);

/*
Sortie :
Array
(
   [0] => Apple
   [1] => Banana
   [2] => Cashew
   [3] => Mango
)
*/
```

Le résultat de `array_values()` ressemble à ce qui se passe lorsque vous affichez un tableau classique avec la fonction `print_r()`, mais ce n'est pas tout à fait la même chose. En réalité, elle réassigne des indices numériques à ces valeurs extraites.

Un exemple avec un tableau associatif rendra cela plus clair :

```
$myFruitsWithColors = [
 "apple" => "red",
 "banana" => "yellow",
 "orange" => "orange",
 "grape" => "purple",
 "watermelon" => "green",
];

$myFruitsWithColorsValues = array_values($myFruitsWithColors);
print_r($myFruitsWithColorsValues);

/*
Sortie :

Array
(
   [0] => red
   [1] => yellow
   [2] => orange
   [3] => purple
   [4] => green
)
*/
```

### La fonction `array_reduce()`

La fonction `array_reduce()` est utilisée pour "réduire" un tableau à une seule valeur en appliquant une fonction de rappel (callback) à chaque élément du tableau. Elle fonctionne comme la méthode `reduce()` des tableaux en JavaScript.

`array_reduce()` itère à travers le tableau et exécute la fonction de rappel sur chaque élément, accumulant un résultat unique.

Cela signifie que vous pouvez l'utiliser pour l'agrégation et le calcul de données, comme le calcul de la valeur totale des articles dans un panier d'achat.

`array_reduce()` prend 2 arguments obligatoires et 1 argument optionnel. Voici la syntaxe :

```
array_reduce(arraytoReduce, callbackFunction, initialValue)
```

-   `arrayToReduce` est le tableau sur lequel vous utilisez `reduce`
-   `callbackFunction` est la fonction qui va "réduire" les éléments du tableau en une seule valeur
-   `initialValue` est optionnel. Il spécifie la valeur initiale de l'accumulateur. S'il est fourni, il sera utilisé comme valeur initiale pour le premier appel à la fonction de rappel. Sinon, le premier élément du tableau sera utilisé comme valeur initiale de l'accumulateur.

`array_reduce()` est généralement utilisée avec des nombres :

```
$myNumbers = [5, 89, 19, 10, 49];

$total = array_reduce($myNumbers, function ($carry, $item) {
 return $carry + $item;
}, 0);

echo $total; // 172
```

Vous pouvez extraire cette fonction de rappel dans une fonction séparée et la passer en argument de la fonction `array_reduce()` :

```
$myNumbers = [5, 89, 19, 10, 49];


function addNums($carry, $item)
{
 return $carry + $item;
}

$total = array_reduce($myNumbers, 'addNums', 0);

echo $total; // 172
```

`array_reduce()` fonctionne également avec des chaînes de caractères :

```
$words = ["Hello", "camper!", "How", "are", "you", "today?"];

// Utilisation de array_reduce pour concaténer toutes les chaînes
$result = array_reduce($words, function ($carry, $item) {
 return $carry . " " . $item;
}, "");

echo $result; //  Hello camper! How are you today?
```

### La fonction `sort()`

La fonction `sort()` prend un tableau et le trie par ordre croissant en fonction des valeurs de ses éléments. Elle modifie le tableau original en réorganisant ses éléments.

Si vous avez des données dans un tableau que vous souhaitez organiser par ordre croissant, la fonction `sort()` est parfaite pour cela.

```
$myNums = [4, 2, 1, 3, 5];
sort($myNums);

print_r($myNums);

/*
Sortie :

Array
(
   [0] => 1
   [1] => 2
   [2] => 3
   [3] => 4
   [4] => 5
)
*/
```

### La fonction `rsort()`

La fonction `rsort()` est similaire à `sort()`, mais elle trie le tableau par ordre décroissant au lieu de l'ordre croissant.

```
$myNums = array(4, 2, 1, 3, 5);
rsort($myNums);

/*
Sortie :

Array
(
   [0] => 5
   [1] => 4
   [2] => 3
   [3] => 2
   [4] => 1
)
*/

print_r($myNums);
```

### La fonction `array_replace()`

La fonction `array_replace()` est utilisée pour remplacer les valeurs du premier tableau par les valeurs d'un tableau fourni. Elle est idéale pour mettre à jour des données.

`array_replace()` prend deux arguments – le tableau que vous voulez remplacer et le nouveau tableau.

```
$myNamesArr1 = ["Zen", "Kay", "Luger"];
$myNamesArr2 = ["Yuan", "Jay", "John"];

$replaceRes = array_replace($myNamesArr1, $myNamesArr2);

print_r($replaceRes);

/*
Sortie :
Array
(
   [0] => Yuan
   [1] => Jay
   [2] => John
)
*/
```

Si vous ne fournissez pas de deuxième valeur, elle renvoie le seul argument que vous fournissez :

```
$myNamesArr1 = ["Zen", "Kay", "Luger"];
$myNamesArr2 = ["Yuan", "Jay", "John"];

$replaceRes = array_replace($myNamesArr1);

print_r($replaceRes);

/*
Sortie :
Array
(
   [0] => Zen
   [1] => Kay
   [2] => Luger
)
*/
```

Si vous passez trois tableaux ou plus en arguments, le dernier argument sera le remplacement pour le premier, et non le deuxième :

```
$myNamesArr1 = ["Zen", "Kay", "Luger"];
$myNamesArr2 = ["Yuan", "Jay", "John"];
$myNamesArr3 = ["Eddy", "White", "Jane"];


$replaceRes = array_replace($myNamesArr1, $myNamesArr2, $myNamesArr3);

print_r($replaceRes);

/*
Sortie :
Array
(
   [0] => Eddy
   [1] => White
   [2] => Jane
)
*/
```

Vous pouvez également remplacer sélectivement un élément à un index particulier :

```
$myFruitsArr1 = ["a" => "apple", "b" => "banana", "c" => "cherry"];
$myFruitsArr2 = array("b" => "blueberry", "c" => "cranberry");
$replaceRes = array_replace($myFruitsArr1, $myFruitsArr2);

print_r($replaceRes);

/*
Sortie :
Array
(
   [a] => apple
   [b] => blueberry
   [c] => cranberry
)
*/
```

### La fonction `array_reverse()`

La fonction `array_reverse()` est utilisée pour inverser l'ordre des éléments d'un tableau. Elle crée un nouveau tableau avec les éléments dans l'ordre inverse.

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango"];
$reversedArr = array_reverse($myFruitsArr);

print_r($reversedArr);

/*
Sortie :

Array
(
   [0] => Mango
   [1] => Cashew
   [2] => Banana
   [3] => Apple
)
*/
```

Si vous vous souvenez du fonctionnement de la fonction `rsort()`, c'est très similaire à `array_reverse()`. La seule différence est que `rsort()` modifie le tableau original, alors que `array_reverse()` ne le fait pas.

### La fonction `array_slice()`

Si vous voulez extraire une partie particulière d'un tableau et la renvoyer sous la forme d'un tableau séparé, `array_slice()` est la fonction idéale.

`array_slice()` vous permet de spécifier l'index de début, la longueur de la tranche et si vous souhaitez préserver les clés du tableau original. Voici la syntaxe de base :

```
array_slice(arrayToSlice, startIndex, length, preserve)
```

-   `arrayToSlice` est le tableau sur lequel vous voulez utiliser `array_slice()`
-   `startIndex` est l'index à partir duquel vous voulez commencer la découpe
-   `length` est la longueur de la découpe dans le `arrayToSlice`. C'est optionnel.
-   `preserve` spécifie si vous voulez que les index du tableau changent ou non. C'est un booléen.

L'exemple ci-dessous commence la découpe à partir du deuxième élément du tableau, ce qui signifie qu'il laissera de côté le premier élément et renverra les autres :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango", "Avocado", "Pineapple"];
$slicedArr = array_slice($myFruitsArr, 1);

print_r($slicedArr);

/*
Sortie :

Array
(
   [0] => Banana
   [1] => Cashew
   [2] => Mango
   [3] => Avocado
   [4] => Pineapple
)
*/
```

N'oubliez pas que vous pouvez spécifier le nombre d'éléments que vous voulez extraire en spécifiant un troisième argument optionnel :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango", "Avocado", "Pineapple"];
$slicedArr = array_slice($myFruitsArr, 1, 3);

print_r($slicedArr);

/*
Sortie :

Array
(
   [0] => Banana
   [1] => Cashew
   [2] => Mango
)
*/
```

Si vous voulez préserver les index, vous pouvez spécifier un quatrième argument booléen optionnel à `true` :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango", "Avocado", "Pineapple"];
$slicedArr = array_slice($myFruitsArr, 1, 3, true);

print_r($slicedArr);

/*
Sortie :

Array
(
   [1] => Banana
   [2] => Cashew
   [3] => Mango
)
*/
```

### La fonction `array_sum()`

`array_sum()` additionne toutes les valeurs numériques d'un tableau et renvoie le résultat. Le seul paramètre qu'elle prend est le tableau contenant les valeurs numériques.

```
$myNums = [5, 6, 9, 20, 1];

$total = array_sum($myNums);
echo $total; // 41
```

Si elle est utilisée sur un tableau contenant des chaînes de caractères, `array_sum()` génère l'erreur `Warning: array_sum(): Addition is not supported on type string in /location/index.php on line #` :

```
$myFruitsArr = ["Apple", "Banana", "Cashew", "Mango", "Avocado", "Pineapple"];
$total = array_sum($myFruitsArr);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image2.png) _Erreur de la fonction sum()_

### La fonction `array_merge()`

`array_merge()` fusionne deux ou plusieurs tableaux. Cela signifie qu'elle est idéale pour combiner plusieurs tableaux en un seul grand tableau.

```
$array1 = [1, 2, 3];
$array2 = [4, 5, 6, 7, 8];

$result = array_merge($array1, $array2);

print_r($result);
/*
Sortie :


Array
(
   [0] => 1
   [1] => 2
   [2] => 3
   [3] => 4
   [4] => 5
   [5] => 6
   [6] => 7
   [7] => 8
)
*/
```

Vous pouvez également utiliser `array_merge()` sur des tableaux associatifs :

```
$array1 = [
 'fname' => 'John',
 'sex' => 'male',
];


$array2 = [
 'lname' => 'Doe',
 'favColor' => 'red',
];

$result = array_merge($array1, $array2);
print_r($result);

/*
Sortie :

Array
(
   [fname] => John
   [sex] => male
   [lname] => Doe
   [favColor] => red
)
*/
```

Si les tableaux contiennent des clés identiques, la dernière écrase la ou les précédentes dans le résultat :

```
$array1 = [
 'fname' => 'John',
 'sex' => 'male',
];


$array2 = [
 'fname' => 'Jane',
 'favColor' => 'red',
];

$result = array_merge($array1, $array2);
print_r($result);

/*
Sortie :

Array
(
   [fname] => Jane
   [sex] => male
   [favColor] => red
)
*/
```

Si un seul tableau est passé à `array_merge()` et que les clés ne sont pas des entiers séquentiels commençant par 0, mais plutôt une séquence comme `3`, `7`, `8`, le tableau résultant verra ses clés réindexées en commençant par `0` :

```
$myArray = [3 => 'Barn', 7 => 'Silo', 8 => 'Tank'];
$res = array_merge($myArray);

print_r($res);

/*
Array
(
   [0] => Barn
   [1] => Silo
   [2] => Tank
)
*/
```

### La fonction `array_filter()`

La fonction `array_filter()` "filtre" les éléments d'un tableau sur la base d'une fonction de rappel que vous lui passez. Vous pouvez l'utiliser pour supprimer les éléments inutiles d'un tableau.

Si la fonction de rappel renvoie `true` pour un élément du tableau, cet élément est inclus dans le tableau résultant, sinon il est exclu.

`array_filter()` prend jusqu'à 3 arguments. La syntaxe de base ressemble à ceci :

```
array_filter(arrayToFilter, callbackFunction, flag)
```

-   `arrayToFilter` est le tableau que vous voulez filtrer. C'est un argument obligatoire.
-   `callbackFunction` est la fonction de rappel que vous voulez appliquer à chaque élément du tableau. Si elle n'est pas fournie, tous les éléments évalués à `true` seront inclus dans le résultat.
-   `flag` spécifie si les clés du tableau seront préservées ou réindexées. Les valeurs possibles sont `ARRAY_FILTER_USE_KEY`, `ARRAY_FILTER_USE_BOTH`, et `ARRAY_FILTER_USE_BOTH`.

Voici un exemple qui récupère les nombres pairs d'un tableau de nombres :

```
$array = [76, 11, 12, 22, 13, 43, 54];
$getEvenNums = array_filter($array, function ($value) {
 return $value % 2 == 0;
});


print_r($getEvenNums);


/*
Array
(
   [0] => 76
   [2] => 12
   [3] => 22
   [6] => 54
)
*/
```

Voici un exemple plus complexe pour obtenir toutes les personnes dont le prénom est "John" dans un tableau associatif multidimensionnel :

```
$persons = [
 ['first' => 'John', 'last' => 'Doe'],
 ['first' => 'Janet', 'last' => 'Jackson'],
 ['first' => 'John', 'last' => 'Smith'],
 ['first' => 'Jane', 'last' => 'Doe'],
 ['first' => 'David', 'last' => 'Lee'],
 ['first' => 'John', 'last' => 'Olga']
];


$personsWithJohnFirstnames = array_filter($persons, function ($person) {
 return $person['first'] === "John";
});

print_r($personsWithJohnFirstnames);

/*
Sortie :

Array
(
   [0] => Array
       (
           [first] => John
           [last] => Doe
       )

   [2] => Array
       (
           [first] => John
           [last] => Smith
       )

   [5] => Array
       (
           [first] => John
           [last] => Olga
       )

)
*/
```

N'oubliez pas que si vous passez le tableau comme seul argument, le tableau résultant contiendra chaque élément qui s'évalue à `true` :

```
$array = [9, 4, 10, 0, 3];
$result = array_filter($array);


print_r($result);


/*
Sortie :


Array
(
   [0] => 9
   [1] => 4
   [2] => 10
   [4] => 3
)
*/
```

### La fonction `array_map()`

La fonction `array_map()` transforme tous les éléments d'un tableau sur la base d'une fonction de rappel qui lui est passée. Elle renvoie ensuite un nouveau tableau contenant les éléments transformés.

Vous pouvez considérer `array_map()` comme un moyen plus pratique de "boucler" sur un tableau, même si techniquement ce n'est pas une boucle.

`array_map()` prend deux paramètres obligatoires – la fonction de rappel et le tableau que vous voulez transformer.

Voici un exemple dans lequel tous les nombres d'un tableau sont mis au carré :

```
$numbers = [5, 8, 3, 4];

$squaredNumbers = array_map(function ($num) {
 return $num * $num;
}, $numbers);

print_r($squaredNumbers);

/*
Sortie :

Array
(
   [0] => 25
   [1] => 64
   [2] => 9
   [3] => 16
)
*/
```

Vous pouvez également extraire la fonction de rappel dans une fonction séparée et la transmettre :

```
function squareNums($num)
{
 return $num * $num;
}

$numbers = [5, 8, 3, 4];
$squaredNumbers = array_map('squareNums', $numbers);

print_r($squaredNumbers);

/*
Sortie :

Array
(
   [0] => 25
   [1] => 64
   [2] => 9
   [3] => 16
)
*/
```

Vous pouvez également utiliser la fonction `array_map()` sur un tableau de chaînes de caractères. L'exemple ci-dessous convertit tous les fruits du tableau `$fruitsArr` en majuscules :

```
$fruitsArr = ['mango', 'apple', 'orange', 'strawberry'];

function toUpperCase($str)
{
 return strtoupper($str);
}

$uppercasedFruits = array_map('toUpperCase', $fruitsArr);

print_r($uppercasedFruits);

/*
Sortie :

Array
(
   [0] => MANGO
   [1] => APPLE
   [2] => ORANGE
   [3] => STRAWBERRY
)
*/
```

Voici un exemple utilisant un tableau associatif où toutes les valeurs sont préfixées par `prefix_` :

```
$fruitsArr = [
 'fruit1' => 'mango',
 'fruit2' => 'banana',
 'fruit3' => 'orange',
];


function addPrefixToFruits($fruit)
{
 return 'prefix_' . $fruit;
}

$prefixedFruits = array_map('addPrefixToFruits', $fruitsArr);

print_r($prefixedFruits);

/*
Sortie :

Array
(
   [fruit1] => prefix_mango
   [fruit2] => prefix_banana
   [fruit3] => prefix_orange
)
*/
```

> **Note** : Si vous vous demandez quelle est la différence entre `array_map()` et `array_filter()`, retenez que **`array_map()` transforme tous les éléments du tableau sur la base d'une fonction de rappel**. En revanche, **`array_filter()` renvoie tout élément du tableau qui correspond (retourne true) à la fonction de rappel qui lui est passée**.

### La fonction `array_search()`

La fonction `array_search()` est utilisée pour rechercher une valeur donnée dans un tableau. Si la valeur est trouvée, elle renvoie la clé de la valeur, sinon elle ne renvoie rien.

`array_search()` prend jusqu'à 3 arguments. Voici la syntaxe :

```
array_search(valueToSearch, arrayToSearch, strict)
```

-   `valueToSearch` est la valeur que vous recherchez
-   `arrayToSearch` est le tableau dans lequel vous voulez effectuer la recherche
-   `strict` est un argument booléen optionnel qui détermine si un opérateur de comparaison stricte doit être utilisé dans la recherche. Par défaut, il est à `false`. S'il est réglé sur `true`, il recherchera des éléments identiques dans le tableau. Par exemple, il fera la distinction entre `"1"` et `1`.

Voici un exemple qui vérifie la présence de l'élément `Cashew` dans un tableau de fruits :

```
$myFruitsArr = [
 "fruit1" => "Apple",
 "fruit2" => "Banana",
 "fruit3" => "Cashew",
 "fruit4" => "Mango",
 "fruit5" => "Avocado",
 "fruit6" => "Pineapple"
];

$checkForCashew = array_search('Cashew', $myFruitsArr);

echo $checkForCashew; // fruit3
```

Et si vous l'utilisez sur un tableau classique, elle renverra toujours l'index du tableau, qui est la clé sous-jacente :

```
$myFruitsArr = [
 "Apple",
 "Banana",
 "Cashew",
 "Mango",
 "Avocado",
 "Pineapple"
];


$CheckForCashew = array_search('Cashew', $myFruitsArr);


echo $CheckForCashew; // 2
```

### La fonction `array_column()`

La fonction `array_column()` extrait une seule colonne de valeurs d'un tableau multidimensionnel. Elle renvoie un tableau contenant les valeurs d'une colonne spécifiée du tableau d'entrée.

Cela signifie que `array_column` est utile lorsque vous voulez créer un tableau à partir d'une colonne d'un tableau existant.

`array_column()` prend jusqu'à 3 arguments. Voici la syntaxe :

```
array_column(parentArray, columKey, indexKey)
```

-   `parentArray` : généralement un tableau multidimensionnel, c'est le tableau dont on veut extraire la colonne de valeurs
-   `columnKey` : la clé ou l'index de la colonne dont on veut extraire les valeurs. Il peut s'agir d'un index entier ou d'une clé de type chaîne représentant le nom de la colonne.
-   `indexKey` (optionnel) : la colonne à utiliser comme index pour le tableau retourné. S'il est omis ou défini sur null, des index numériques sont utilisés.

L'exemple ci-dessous utilise la clé "name" du tableau pour créer un nouveau tableau :

```
$pupils = [
 ["id" => 1, "name" => "John", "score" => 90],
 ["id" => 2, "name" => "Jane", "score" => 79],
 ["id" => 3, "name" => "Will", "score" => 83],
 ["id" => 4, "name" => "Jill", "score" => 92],
 ["id" => 5, "name" => "steven", "score" => 100],
];

$arrayFromNameColumn = array_column($pupils, 'name');

print_r($arrayFromNameColumn);

/*
Sortie :

Array
(
   [0] => John
   [1] => Jane
   [2] => Will
   [3] => Jill
   [4] => steven
)
*/
```

N'oubliez pas que vous pouvez passer une autre clé du tableau pour faire de ses valeurs les index du tableau résultant. J'utiliserai l'id pour cela :

```
$pupils = [
 ["id" => 1, "name" => "John", "score" => 90],
 ["id" => 2, "name" => "Jane", "score" => 79],
 ["id" => 3, "name" => "Will", "score" => 83],
 ["id" => 4, "name" => "Jill", "score" => 92],
 ["id" => 5, "name" => "steven", "score" => 100],
];

$arrayFromNameColumn = array_column($pupils, "name", "id");

print_r($arrayFromNameColumn);

/*
Sortie :



Array
(
   [1] => John
   [2] => Jane
   [3] => Will
   [4] => Jill
   [5] => steven
)
*/
```

### La fonction `in_array()`

`in_array()` est utilisée pour vérifier si un élément particulier se trouve dans un tableau. Elle prend deux paramètres obligatoires et un paramètre optionnel.

Voici la syntaxe :

```
in_array(itemToSearch, arrayToSearchThrough, strict)
```

-   `itemToSearch` est l'élément que vous recherchez. C'est obligatoire.
-   `arrayToSearchThrough` est le tableau dans lequel vous voulez chercher `itemToSearch`. C'est également obligatoire.
-   `strict` est une valeur booléenne qui vous permet de spécifier si vous voulez que la recherche soit effectuée avec une comparaison lâche (`==`) ou une comparaison stricte (`===`). La valeur par défaut est `false`.

Voici la fonction `in_array()` en action :

```
$myFruitsArr1 = ["Apple", "Banana", "Cashew", "Mango"];
var_dump(in_array("Banana", $myFruitsArr1)); // bool(true)
var_dump(in_array("banana", $myFruitsArr1)); // bool(false)
```

Comme le résultat de `in_array()` est un booléen, elle est couramment utilisée dans les conditions :

```
$myFruitsArr1 = ["Apple", "Banana", "Cashew", "Mango"];


if (in_array("Banana", $myFruitsArr1)) {
 echo "Banana est dans le tableau"; // Banana est dans le tableau
} else {
 echo "Banana n'est pas dans le tableau";
}
```

## Comment parcourir des tableaux en PHP

PHP fournit la boucle traditionnelle `for` pour itérer à travers les tableaux indexés et associatifs. Vous pouvez également utiliser une fonction `forEach()` plus propre pour le même but.

### Comment parcourir un tableau indexé

Voici la syntaxe de base pour parcourir un tableau avec une boucle `for` :

```
for ($i=0; $i < count($arr); $i++) {
 # faire quelque chose avec $arr ...
}
```

Et voici celle de `foreach()` :

```
foreach ($arrs as $arr) {
 # faire quelque chose avec $arr
}
```

Voici un exemple utilisant la boucle `for` pour parcourir un tableau de chaînes de caractères :

```
$retiredBallers = ["Pele", "Maradona", "Zidane", "Lampard", "Okocha"];

for ($i = 0; $i < count($retiredBallers); $i++) {
 echo $retiredBallers[$i] . "<br>";
}

/*
Sortie :

Pele
Maradona
Zidane
Lampard
Okocha
*/
```

Vous pouvez parcourir des nombres de la même manière :

```
for ($i = 0; $i < count($myNums); $i++) {
 echo $myNums[$i] . "<br>";
}

/*
Sortie :

45
8
90
2
5
*/
```

Vous pouvez également afficher l'index de chaque élément du tableau :

```
for ($i = 0; $i < count($myNums); $i++) {
 echo $myNums[$i] . " est à l'index " . $i . "<br>";
}

/*
Sortie :

45 est à l'index 0
8 est à l'index 1
90 est à l'index 2
2 est à l'index 3
5 est à l'index 4
*/
```

N'oubliez pas que vous pouvez utiliser `foreach` pour parcourir n'importe quel tableau également :

```
foreach ($retiredBallers as $retiredBaller) {
 echo $retiredBaller . "<br>";
}


/*
Pele
Maradona
Zidane
Lampard
Okocha
*/
```

Vous pouvez obtenir l'index de cette façon aussi :

```
foreach ($retiredBallers as $key => $retiredBaller) {
 echo $retiredBaller . " est à l'index " . $key . "<br>";
}


/*
Pele est à l'index 0
Maradona est à l'index 1
Zidane est à l'index 2
Lampard est à l'index 3
Okocha est à l'index 4
*/
```

### Comment parcourir un tableau associatif

Un tableau associatif peut être complexe avec des éléments imbriqués profondément. Vous devez donc extraire ce que vous voulez au lieu de tout afficher.

Voici comment j'ai obtenu le nom et le pays de certains footballeurs retraités à partir d'un tableau `$retiredFootballers` :

```
$retiredFootballers = [
 [
   "name" => "Pele",
   "position" => "Forward",
   "country" => "Brazil",
   "club" => "Santos"
 ],


 [
   "name" => "Diego Maradona",
   "position" => "Attacking Midfielder",
   "country" => "Argentina",
   "club" => "Napoli"
 ],


 [
   "name" => "Zinedine Zidane",
   "position" => "Midfielder",
   "country" => "France",
   "club" => "Real Madrid"
 ],


 [
   "name" => "Ronaldinho",
   "position" => "Attacking Midfielder",
   "country" => "Brazil",
   "club" => "Barcelona"
 ],


 [
   "name" => "David Beckham",
   "position" => "Midfielder",
   "country" => "England",
   "club" => "Manchester United"
 ],
 [
   "name" => "Jay-Jay Okocha",
   "position" => "Midfielder",
   "country" => "Nigeria",
   "club" => "Bolton Wanderers"
 ]
];


for ($i = 0; $i < count($retiredFootballers); $i++) {
 echo $retiredFootballers[$i]["name"] . " vient de " . $retiredFootballers[$i]["country"] . "<br>";
 echo "<hr>";
}
```

Faire la même chose avec `foreach()` est plus propre car vous n'avez pas besoin d'une variable `$i` :

```
foreach ($retiredFootballers as $retiredFootballer) {
 echo $retiredFootballer["name"] . " vient de " . $retiredFootballer["country"] . "<br>";
 echo "<hr>";
}
```

### Comment parcourir un tableau à l'intérieur d'un template HTML

Tout code HTML dans votre fichier PHP constitue le template de ce fichier PHP. Cela signifie que vous pouvez effectuer le bouclage à l'intérieur du HTML, car vous pouvez écrire du PHP à l'intérieur de ce HTML.

Voici comment vous pouvez faire cela :

```
<?php
$retiredBallers = ["Pele", "Maradona", "Zidane", "Lampard", "Okocha"];
?>

<h1 class="text-center mt-3 bd-highlight">Parcourir des tableaux en PHP</h1>

 <h2 class="mx-5 mt-5">Quelques footballeurs retraités</h2>

 <ul class="list-group mx-5" style="width: 25%;">
   <!-- La boucle -->
   <?php for ($i = 0; $i < count($retiredBallers); $i++) : ?>
     <li class="list-group-item"> <?= $retiredBallers[$i] ?> </li>
   <?php endfor; ?>
 </ul>
```

Vous pouvez faire la même chose avec `foreach()` :

```
<?php
$retiredBallers = ["Pele", "Maradona", "Zidane", "Lampard", "Okocha"];
?>

<h1 class="text-center mt-3 bd-highlight">Parcourir des tableaux en PHP</h1>

 <h2 class="mx-5 mt-5">Quelques footballeurs retraités</h2>


 <ul class="list-group mx-5" style="width: 25%;">
   <!-- La boucle -->
   <?php foreach ($retiredBallers as $retiredBaller) : ?>
     <li class="list-group-item"> <?= $retiredBaller ?> </li>
   <?php endforeach; ?>
 </ul>
```

Voici à quoi cela ressemble dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image4.png) _Parcourir des tableaux à l'aide de la boucle for PHP à l'intérieur du HTML_

Utilisons également `foreach()` pour afficher le tableau associatif `$retiredFootballers` :

```
<h1 class="text-center mt-3 bd-highlight">Parcourir des tableaux en PHP</h1>


 <h2 class="mx-5 mt-5">Quelques footballeurs retraités</h2>


 <ul class="list-group mx-5" style="width: 25%;">
   <!-- La boucle -->
   <?php foreach ($retiredFootballers as $retiredFootballer) : ?>
     <li class="list-group-item"> <?= $retiredFootballer["name"] . " vient de " . $retiredFootballer["country"] ?> </li>
   <?php endforeach; ?>
 </ul>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image1.png) _Parcourir des tableaux à l'aide de la fonction foreach PHP à l'intérieur du HTML_

## Conclusion

Apprendre à travailler avec les tableaux est une étape fondamentale vers la maîtrise de PHP et du développement web. C'est pourquoi ce guide vous a présenté les diverses capacités des tableaux PHP, de la création à la manipulation et au parcours.

Vous devriez maintenant être confiant dans l'utilisation des tableaux pour gérer efficacement les données en PHP, qu'il s'agisse de listes simples avec des tableaux indexés, ou de structures complexes avec des tableaux associatifs et multidimensionnels.

Pour la suite, je vous encourage à expérimenter diverses fonctions de tableaux pour améliorer votre code et relever différents défis de programmation. Envisagez également d'explorer les tableaux multidimensionnels et associatifs pour des scénarios de données plus complexes.

À mesure que vous progresserez avec les tableaux PHP, leur intégration avec les opérations de base de données pourra encore améliorer vos applications web, alors gardez un œil sur le deuxième article de cette série.

Bon code !

[1]: #heading-comment-creer-des-tableaux-en-php
[2]: #heading-comment-creer-des-tableaux-avec-la-fonction-array
[3]: #heading-comment-creer-des-tableaux-avec-la-syntaxe-des-crochets
[4]: #heading-comment-afficher-des-tableaux-en-php
[5]: #heading-comment-afficher-un-tableau-avec-la-fonction-print-r
[6]: #heading-comment-afficher-un-tableau-avec-la-fonction-var-dump
[7]: #heading-fonctions-de-tableaux-php
[8]: #heading-la-fonction-de-tableau-count
[9]: #heading-la-fonction-de-tableau-array-push
[10]: #heading-la-fonction-arraypop
[11]: #heading-la-fonction-arrayshift
[12]: #heading-la-fonction-arrayunshift
[13]: #heading-la-fonction-arraysplice
[14]: #heading-la-fonction-arraykeys
[15]: #heading-la-fonction-arrayvalues
[16]: #heading-la-fonction-arrayreduce
[17]: #heading-la-fonction-sort
[18]: #heading-la-fonction-rsort
[19]: #heading-la-fonction-arrayreplace
[20]: #heading-la-fonction-arrayreverse
[21]: #heading-la-fonction-arrayslice
[22]: #heading-la-fonction-arraysum
[23]: #heading-la-fonction-arraymerge
[24]: #heading-la-fonction-arrayfilter
[25]: #heading-la-fonction-arraymap
[26]: #heading-la-fonction-arraysearch
[27]: #heading-la-fonction-arraycolumn
[28]: #heading-la-fonction-inarray
[29]: #heading-comment-parcourir-des-tableaux-en-php
[30]: #heading-comment-parcourir-un-tableau-indexe
[31]: #heading-comment-parcourir-un-tableau-associatif
[32]: #heading-comment-parcourir-un-tableau-a-l-interieur-du-template-html
[33]: #heading-conclusion