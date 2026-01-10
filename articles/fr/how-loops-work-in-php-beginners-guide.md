---
title: 'Comment fonctionnent les boucles en PHP : Un guide complet pour débutants'
subtitle: ''
author: Montasser Mossallem
co_authors: []
series: null
date: '2025-06-18T22:08:57.415Z'
originalURL: https://freecodecamp.org/news/how-loops-work-in-php-beginners-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750178963918/bf8c63b9-9624-4cb0-bd31-10ffbdbe67f6.jpeg
tags:
- name: PHP
  slug: php
- name: PHP7
  slug: php7
- name: php8
  slug: php8
- name: PHPUnit
  slug: phpunit
- name: PhpStorm
  slug: phpstorm
seo_title: 'Comment fonctionnent les boucles en PHP : Un guide complet pour débutants'
seo_desc: 'PHP loops help you repeat a block of code based on a condition. You can
  use them to work through arrays or repeat actions. You can also use them to skip
  steps based on logic.

  In this article, you will learn how PHP loops work and when to use each typ...'
---

Les boucles PHP vous aident à répéter un bloc de code en fonction d'une condition. Vous pouvez les utiliser pour parcourir des tableaux ou répéter des actions. Vous pouvez également les utiliser pour sauter des étapes en fonction de la logique.

Dans cet article, vous apprendrez comment fonctionnent les boucles PHP et quand utiliser chaque type.

## Table des matières

* [Comprendre comment fonctionnent les boucles en PHP](#heading-comprendre-comment-fonctionnent-les-boucles-en-php)
    
* [La boucle `while` en PHP](#heading-la-boucle-while-en-php)
    
* [La boucle `do...while` en PHP](#heading-la-boucle-do-while-en-php)
    
* [La boucle `for` en PHP](#heading-la-boucle-for-en-php)
    
* [La boucle `foreach` en PHP](#heading-la-boucle-foreach-en-php)
    
* [Utiliser l'instruction `break`](#heading-utiliser-linstruction-break)
    
* [Utiliser l'instruction `continue`](#heading-utiliser-linstruction-continue)
    
* [Remplacer les boucles par `array_map()` en PHP](#heading-remplacer-les-boucles-par-array_map-en-php)
    
* [Comprendre les boucles imbriquées](#heading-comprendre-les-boucles-imbriquees)
    
* [Conclusion](#heading-conclusion)
    

Commençons.

## Comprendre comment fonctionnent les boucles en PHP

Une boucle permet à PHP d'exécuter le même ensemble d'instructions plusieurs fois. Elle vérifie une certaine condition avant chaque exécution. Ensuite, le code s'exécute à nouveau si la condition est vraie et s'arrête si la condition est fausse.

![Diagramme montrant comment fonctionnent les boucles en PHP](https://cdn.hashnode.com/res/hashnode/image/upload/v1749910672507/5a4f946c-bbe8-407d-bfd0-c524d7fef9e0.png align="center")

Les boucles aident à réduire le code répété. Vous pouvez traiter des éléments dans une liste ou vérifier des valeurs. Les boucles vous permettent d'écrire un bloc de code une fois et de l'exécuter plusieurs fois.

PHP fournit quatre types principaux de boucles :

* while
    
* do...while
    
* for
    
* foreach
    

Examinons chacun d'eux en détail.

## La boucle `while` en PHP

La boucle while vérifie si la condition est vraie avant d'exécuter le bloc de code. Si la condition est vraie, elle exécute le bloc. Ensuite, elle vérifie à nouveau. La boucle se répète jusqu'à ce que la condition devienne fausse.

Voici la syntaxe :

```plaintext
while (condition) {
  // bloc de code
}
```

Voici un exemple :

```php
$count = 1;
while ($count <= 3) {
  echo "Count: $count\n";
  $count++;
}
```

Cette boucle commence avec `$count = 1`. Elle imprime la valeur et ajoute 1 à chaque fois. Elle s'arrête lorsque `$count` devient 4.

Cela donne cette sortie :

```plaintext
Count: 1
Count: 2
Count: 3
```

Voici un autre exemple :

```php
$index = 0;
$names = ['Tom', 'Anna', 'Joe'];
while ($index < count($names)) {
  echo $names[$index] . "\n";
  $index++;
}
```

Cette boucle imprime chaque nom du tableau. Elle utilise l'index pour parcourir la liste.

Sortie :

```plaintext
Tom
Anna
Joe
```

Alors, **quand devez-vous utiliser une boucle** `while`**?**

Utilisez une boucle `while` lorsque vous voulez vérifier la condition avant d'exécuter le code. Ce type convient le mieux lorsque la boucle ne doit pas s'exécuter du tout si la condition est fausse dès le début.

Voici un exemple :

Vous demandez à un utilisateur d'entrer un nombre. Vous ne voulez exécuter votre boucle que si le nombre est positif.

```php
$number = getUserInput();

while ($number > 0) {
  echo "You entered: $number\n";
  $number = getUserInput();
}
```

Si le premier nombre est zéro ou négatif, la boucle sera ignorée. Cela a du sens ici - vous ne voulez que la boucle s'exécute pour les nombres valides.

Vous apprendrez comment fonctionne la boucle `do while` en PHP dans la partie suivante.

## La boucle `do...while` en PHP

La boucle `do...while` exécute le bloc de code une fois, puis vérifie la condition. Elle s'exécute toujours au moins une fois.

```plaintext
do {
  // bloc de code
} while (condition);
```

Exemple :

```php
$start = 5;
do {
  echo "Start: $start\n";
  $start++;
} while ($start < 8);
```

Cette boucle imprime les nombres de 5 à 7. Elle vérifie la condition après l'exécution du bloc.

Sortie :

```plaintext
Start: 5
Start: 6
Start: 7
```

Voici un autre exemple :

```php
$retry = 0;
do {
  echo "Attempt $retry\n";
  $retry++;
} while ($retry < 1);
```

Le code s'exécute une fois, même si la condition est fausse au début. Sortie :

```plaintext
Attempt 0
```

Utilisez une boucle `do...while` lorsque vous voulez que le code s'exécute au moins une fois. Cela a du sens lorsque la première étape doit se produire avant de vérifier la condition.

Voici un exemple :

Vous voulez montrer un menu à l'utilisateur au moins une fois. Ensuite, vous continuez à le montrer jusqu'à ce qu'ils choisissent de quitter.

```php
do {
  $option = showMenuAndGetChoice();
} while ($option != "exit");
```

Le menu apparaît une fois quoi qu'il arrive. Si l'utilisateur tape "exit" immédiatement, la boucle s'arrête après une exécution.

Passons à la section suivante pour examiner la boucle la plus courante en PHP, qui est la boucle for.

## La boucle `for` en PHP

La boucle `for` fonctionne lorsque vous savez combien de fois vous voulez que la boucle s'exécute. Elle vous donne un moyen propre de définir un compteur, de vérifier une condition et de mettre à jour le compteur - tout en une seule ligne. Cela rend la boucle facile à lire et à contrôler.

La boucle a trois parties à l'intérieur des parenthèses :

1. **Début** - Cela configure la boucle. Vous définissez généralement un compteur ici, comme `$i = 0`.
    
2. **Condition** - La boucle s'exécute tant que cette partie est vraie. Dès qu'elle devient fausse, la boucle s'arrête.
    
3. **Étape** - Cela met à jour le compteur après chaque exécution de la boucle. Vous pouvez augmenter ou diminuer la valeur ici.
    

Voici la structure :

```plaintext
for (début; condition; étape) {
  // bloc de code
}
```

Voici un exemple :

```php
for ($i = 1; $i <= 3; $i++) {
  echo "Number: $i\n";
}
```

Voici ce qui se passe :

* `$i = 1` définit la valeur de départ.
    
* La condition `$i <= 3` vérifie si la boucle doit s'exécuter.
    
* Si la condition est vraie, le code à l'intérieur s'exécute.
    
* Ensuite, `$i++` augmente le compteur de 1.
    
* La boucle se répète jusqu'à ce que `$i` devienne supérieur à 3.
    

Voici la sortie :

```plaintext
Number: 1
Number: 2
Number: 3
```

Voici un autre exemple :

```php
for ($i = 2; $i <= 6; $i += 2) {
  echo "$i is even\n";
}
```

L'étape ici est `$i += 2`, et non pas seulement `$i++`. Cela ajoute 2 à `$i` après chaque exécution au lieu de 1. Ainsi, les valeurs passent de 2 à 4 à 6. C'est ainsi que vous contrôlez le rythme de la boucle.

Voici la sortie :

```plaintext
2 is even
4 is even
6 is even
```

Vous utilisez une boucle `for` lorsque :

* Vous savez exactement combien de fois vous devez exécuter le code
    
* Vous travaillez avec un compteur qui augmente ou diminue
    
* Vous parcourez une plage, comme les nombres de 1 à 10
    
* Vous voulez garder toute la configuration de la boucle en un seul endroit
    

Dans la section suivante, vous apprendrez à propos d'une autre boucle appelée `foreach`. Continuons.

## La boucle `foreach` en PHP

La boucle [foreach de PHP](https://flatcoding.com/tutorials/php/foreach-loop-in-php/) est conçue pour fonctionner avec des tableaux. Elle vous permet de parcourir chaque élément du tableau, un à la fois. Vous n'avez pas besoin de compteur, et vous n'avez pas besoin de vérifier la taille - PHP gère cette partie pour vous.

Il existe deux façons d'utiliser `foreach`, et les deux fonctionnent uniquement avec des tableaux ou des objets qui se comportent comme des tableaux :

* Parcourir uniquement les valeurs
    
* Parcourir les clés et les valeurs
    

Examinons chacune d'elles.

**Parcourir uniquement les valeurs** : cette version vous donne une valeur du tableau à chaque exécution :

```php
$colors = ['red', 'green', 'blue'];

foreach ($colors as $color) {
  echo "$color\n";
}
```

Ici, le tableau a trois valeurs. La boucle vous en donne une à la fois. Vous n'obtenez pas la position ou l'index - juste la valeur.

Voici la sortie :

```plaintext
red  
green  
blue
```

**Parcourir les clés et les valeurs** : Cette version vous donne à la fois la clé et la valeur pour chaque élément du tableau.

Voici un exemple :

```php
$person = ['name' => 'Alice', 'age' => 30, 'city' => 'Cape Town'];

foreach ($person as $key => $value) {
  echo "$key: $value\n";
}
```

Ici, `$key` contient chaque index ou nom, et `$value` contient ce qui est stocké à cette clé.

Voici la sortie :

```php
name: Alice  
age: 30  
city: Cape Town
```

Ce format aide lorsque vous voulez étiqueter des données, travailler avec à la fois le nom et la valeur, ou construire quelque chose comme un formulaire ou un rapport.

Rappelez-vous que `foreach` fonctionne uniquement avec des tableaux ou des objets qui se comportent comme des tableaux (tels que des objets qui implémentent `Traversable`). Vous ne pouvez pas l'utiliser avec une simple chaîne ou un nombre.

Si vous essayez ceci :

```php
foreach (123 as $item) {
  echo $item;
}
```

Vous obtenez une erreur. PHP attend quelque chose qui contient plusieurs éléments, comme un tableau ou un objet itérable.

Vous pouvez quitter la boucle avec une instruction `break` basée sur une condition ou une expression. Passons à la partie suivante pour voir comment nous pouvons faire cela.

## Comment utiliser l'instruction `break` en PHP

L'instruction [break](https://flatcoding.com/tutorials/php/php-break-exit-php-loop/) en PHP termine la boucle immédiatement, même si sa condition reste vraie. Voici sa syntaxe :

```plaintext
break;
```

Voici un exemple :

```php
for ($i = 1; $i <= 5; $i++) {
  if ($i === 3) {
    break;
  }
  echo "$i\n";
}
```

Cette boucle s'arrête lorsque `$i` devient 3. Sortie :

```plaintext
1
2
```

Ce code PHP utilise une boucle `for` pour compter de 1 à 5. Il inclut une condition qui arrête la boucle tôt avec `break`. Si `$i` est égal à 3, la boucle se termine.

Sinon, il imprime la valeur de `$i`. La sortie est 1 et 2, et la boucle se termine avant d'atteindre 3.

Voici quelques raisons courantes d'utiliser l'instruction `break` :

* Lorsque vous trouvez ce que vous cherchez
    
* Si vous voulez sortir sur une certaine condition
    
* À l'intérieur d'un menu ou d'une boucle d'entrée utilisateur
    
* Dans les instructions `switch`
    

PHP exécutera tout le code après la première correspondance si vous n'utilisez pas `break`. Cela peut causer des bugs.

Dans la section suivante, vous verrez comment sauter des parties d'une boucle lorsque certaines conditions sont vraies.

## Comment utiliser l'instruction `continue`

L'instruction [continue de PHP](https://flatcoding.com/tutorials/php/php-continue-statement/) saute le reste de la boucle pour l'étape actuelle. Voici sa syntaxe :

```php
continue;
```

Voici un exemple :

```php
for ($i = 1; $i <= 4; $i++) {
  if ($i === 2) {
    continue;
  }
  echo "$i\n";
}
```

Cette boucle n'imprime pas 2 et passe à la valeur suivante. Sortie :

```plaintext
1
3
4
```

Alors, **pourquoi voudriez-vous sauter une partie d'une boucle avec** `continue`**?**

Vous utilisez l'instruction `continue` en PHP lorsque vous voulez sauter le reste du bloc de boucle actuel et passer à l'élément suivant. Cela aide lorsque vous devez éviter certaines étapes dans une boucle en fonction d'une condition.

Vous pouvez utiliser `continue` dans une boucle `foreach`, `for` ou `while`. Si une valeur ne correspond pas à ce dont vous avez besoin, vous la sautez et continuez. Vous n'arrêtez pas la boucle - vous sautez seulement l'exécution actuelle.

**Alors, pourquoi voudriez-vous éviter les boucles dans certains cas ?**

Les boucles vous donnent un contrôle total, mais elles peuvent entraîner du désordre. Vous répétez la même logique encore et encore. Cela rend le code plus difficile à lire. Vous risquez également des bugs si vous oubliez de mettre à jour un compteur ou de sortir au bon moment.

Si tout ce que vous voulez est d'appliquer une action à chaque élément d'un tableau, une boucle peut sembler trop. Vous n'avez pas besoin d'un contrôle total - juste d'un moyen propre de mapper les valeurs. C'est là qu'une fonction intégrée comme `array_map` a plus de sens.

Dans la partie suivante, vous verrez comment `array_map` remplace une boucle lorsque vous voulez un moyen de changer chaque élément d'un tableau.

## Comment remplacer les boucles par `array_map()` en PHP

La fonction [array_map](https://flatcoding.com/tutorials/php/array_map/) de PHP vous aide à éviter les boucles répétitives. Elle applique une [fonction de rappel](https://www.freecodecamp.org/news/how-to-use-arrow-functions-in-php/) à chaque élément d'un ou plusieurs tableaux et retourne un nouveau tableau avec les résultats.

```php
$numbers = [1, 2, 3, 4];
$doubled = array_map(fn($n) => $n * 2, $numbers);
print_r($doubled);
```

La sortie :

```plaintext
[2, 4, 6, 8]
```

Cela fait la même chose qu'une boucle `foreach` où vous multipliez chaque nombre par 2 et stockez le résultat. Mais avec `array_map`, la logique reste en un seul endroit.

Vous passez la fonction et le tableau comme arguments. C'est ce que les gens veulent dire par un "style fonctionnel" - vous utilisez des outils intégrés qui se concentrent sur l'entrée et la sortie, pas sur les étapes ou les compteurs.

Vous obtenez le même résultat, mais le code est plus court à lire. Vous évitez également les effets secondaires puisque `array_map` retourne un nouveau tableau sans changer l'original.

Dans la section suivante, vous comprendrez comment fonctionnent les boucles imbriquées.

## Comment fonctionnent les boucles imbriquées en PHP

Une boucle imbriquée signifie qu'une boucle se trouve à l'intérieur d'une autre. La boucle externe contrôle le cycle principal tandis que la boucle interne s'exécute complètement chaque fois que la boucle externe s'exécute une fois.

Ainsi, si la boucle externe s'exécute deux fois et que la boucle interne s'exécute trois fois à chaque cycle, la boucle interne s'exécute six fois au total.

Par exemple :

```php
for ($i = 1; $i <= 2; $i++) {
  for ($j = 1; $j <= 3; $j++) {
    echo "i=$i, j=$j\n";
  }
}
```

Voici comment cela fonctionne :

* La boucle externe utilise `$i`. Elle commence à 1 et s'exécute tant que `$i <= 2`.
    
* Cela signifie que la boucle externe s'exécute deux fois : une fois pour `$i = 1` et une fois pour `$i = 2`.
    
* À l'intérieur de celle-ci, la boucle interne utilise `$j`. Elle commence à 1 et s'exécute tant que `$j <= 3`.
    
* Ainsi, pour chaque fois que la boucle externe s'exécute, la boucle interne s'exécute trois fois : pour `$j = 1`, `$j = 2`, et `$j = 3`.
    

Sortie :

```plaintext
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
```

Alors, **comment utilisez-vous les boucles imbriquées avec des tableaux ?**

Vous pouvez également utiliser des boucles imbriquées pour lire un tableau à deux dimensions. Voici un exemple utilisant une matrice :

```php
$matrix = [
  [1, 2],
  [3, 4]
];

foreach ($matrix as $row) {
  foreach ($row as $cell) {
    echo "$cell ";
  }
  echo "\n";
}
```

Dans ce cas :

* Le `foreach` externe obtient chaque ligne de la matrice.
    
* Chaque `$row` est un tableau : d'abord `[1, 2]`, puis `[3, 4]`.
    
* Le `foreach` interne parcourt chaque valeur à l'intérieur de la ligne.
    

Ainsi, la sortie est :

```plaintext
1 2
3 4
```

Vous pouvez utiliser des boucles imbriquées lorsque vous devez gérer une grille ou une matrice. Cela fonctionne également lorsque vous voulez regrouper des valeurs.

**Quand devez-vous utiliser des boucles imbriquées, et quand ne devez-vous pas ?**

Vous pourriez avoir :

* Des lignes et des colonnes dans une matrice
    
* Une liste de commandes, chacune avec des articles
    
* Des catégories, chacune avec des sous-catégories
    

Chaque fois que vous devez parcourir un groupe qui se trouve à l'intérieur d'un autre groupe, les boucles imbriquées aident. Elles vous permettent de parcourir les deux niveaux étape par étape.

Par exemple, si vous avez des produits regroupés par type, vous pouvez utiliser une boucle externe pour les types et une boucle interne pour chaque produit à l'intérieur.

Mais les boucles imbriquées ont aussi des limites. Si les deux boucles s'exécutent de nombreuses fois, votre code ralentit rapidement. Une boucle à l'intérieur d'une boucle signifie que le nombre total d'étapes augmente rapidement.

Si la boucle externe s'exécute 100 fois et que la boucle interne s'exécute 100 fois, cela fait 10 000 étapes. Cela peut entraîner des temps de chargement longs ou même geler le serveur avec de grands ensembles de données.

Les boucles imbriquées résolvent de vrais problèmes, mais assurez-vous de les utiliser uniquement lorsqu'elles conviennent. Toutes les tâches n'en ont pas besoin. Si vous pouvez résoudre le même problème avec une seule boucle et des données claires, c'est souvent mieux.

## Conclusion

Les boucles vous aident à répéter des tâches en PHP. Vous pouvez utiliser while, for, ou même foreach en fonction de vos besoins. Utilisez break pour arrêter tôt. Utilisez continue pour sauter des étapes. Utilisez des boucles imbriquées si vous travaillez avec des grilles ou des données groupées.

Maintenant, espérons que vous comprenez comment fonctionne chaque [boucle PHP](https://flatcoding.com/tutorials/php/php-loop-with-loops-examples/) en fonction de ces exemples et cas d'utilisation clairs.