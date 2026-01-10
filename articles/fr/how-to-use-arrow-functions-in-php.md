---
title: Comment utiliser les fonctions fléchées en PHP 7.4+
subtitle: ''
author: Montasser Mossallem
co_authors: []
series: null
date: '2025-05-08T18:33:42.174Z'
originalURL: https://freecodecamp.org/news/how-to-use-arrow-functions-in-php
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746354775446/092005ae-12bb-4be9-a72c-aacc5f044962.jpeg
tags:
- name: PHP
  slug: php
- name: Web Development
  slug: web-development
- name: web developers
  slug: web-developers
seo_title: Comment utiliser les fonctions fléchées en PHP 7.4+
seo_desc: 'Arrow functions were introduced in PHP 7.4 to allow devs to write short,
  anonymous functions. They offer a compact alternative to traditional closures, especially
  when the function body is small and focused.

  In this article, you will learn how to use...'
---

Les fonctions fléchées ont été introduites dans PHP 7.4 pour permettre aux développeurs d'écrire des fonctions courtes et anonymes. Elles offrent une alternative compacte aux fermetures traditionnelles, surtout lorsque le corps de la fonction est petit et ciblé.

Dans cet article, vous apprendrez comment utiliser la fonction fléchée en PHP avec des exemples. Vous apprendrez également la différence entre les fonctions fléchées et les fonctions anonymes.

## Table des matières

* [Prérequis](#prerequisites)
    
* [Comprendre les fonctions fléchées en PHP](#understand-the-arrow-functions-in-php)
    
* [La différence entre les fonctions fléchées et les fonctions anonymes en PHP](#the-difference-between-arrow-functions-and-anonymous-functions-in-php)
    
    * [1\. Syntaxe](#1-syntax)
        
    * [2\. Portée des variables (Portée lexicale)](#2-variable-scope-lexical-scope)
        
    * [3\. Lisibilité et brièveté](#3-readability-and-brevity)
        
* [Comment retourner des fonctions fléchées à partir d'autres fonctions](#how-to-return-arrow-functions-from-other-functions)
    
* [Comment utiliser les fonctions fléchées dans votre code ?](#how-to-use-arrow-functions-in-your-code)
    
    * [Utiliser la fonction fléchée avec `array_map()`](#use-the-arrow-function-within-array_map)
        
    * [Utiliser la fonction fléchée avec `array_filter()`](#use-the-arrow-function-with-array_filter)
        
    * [Utiliser la fonction fléchée avec `array_reduce()`](#use-the-arrow-function-with-array_reduce)
        
    * [Imbriquer les fonctions fléchées en PHP](#nest-arrow-functions-in-php)
        
* [Conclusion](#wrapping-up)
    

## Prérequis

Vous devez savoir comment écrire du code PHP de base, comme des fonctions, et être capable de travailler avec des tableaux. Assurez-vous d'utiliser PHP 7.4 ou une version plus récente, car les fonctions fléchées ne fonctionnent que dans cette version et au-delà.

## Comprendre les fonctions fléchées en PHP

La [fonction fléchée PHP](https://flatcoding.com/tutorials/php/arrow-functions/) est une syntaxe abrégée. Elle définit une fonction anonyme et est conçue pour des opérations et expressions simples.

Les fonctions fléchées en PHP sont mieux utilisées lorsque :

* Vous avez besoin d'un rappel rapide ou d'une fonction en ligne.
    
* La fonction retourne une seule expression.
    
* Vous voulez éviter les déclarations `use` répétitives.
    

La syntaxe de base d'une fonction fléchée est :

```php
fn(parameter_list) => expression;
```

* `fn` est le mot-clé qui définit la fonction fléchée.
    
* `parameter_list` est la liste des paramètres (similaire à une fonction normale).
    
* `=>` sépare la liste des paramètres de l'expression.
    
* `expression` est la valeur que la fonction retourne. Vous ne pouvez pas utiliser un bloc d'instructions ici – seule une seule expression est autorisée.
    

Les fonctions fléchées capturent automatiquement les variables de la portée. Elles n'ont pas besoin du mot-clé `use` comme montré ci-dessous :

```php
$var_name = 10; 
$func = function($n) use ( $var_name ) {
   return $n * $var_name;
}
```

Vous pouvez utiliser les variables dans la portée directement :

```php
$var_name = 10; 
$func = fn($n) => $n * $var_name;
```

Voici un exemple de portée lexicale :

```php
$multiplier = 3;
$multiply = fn($x) => $x * $multiplier;
echo $multiply(4); // Affiche : 12
```

La variable `$multiplier` est automatiquement capturée depuis la portée externe. Vous n'avez pas besoin d'utiliser `use($multiplier)` comme vous le feriez dans une fonction anonyme traditionnelle.

Règles clés de la syntaxe des fonctions fléchées :

* Utilisez toujours `fn`, pas `function`.
    
* Pas d'accolades ou de mot-clé `return` – juste une seule expression.
    
* Capture automatique des variables depuis la portée externe.
    
* Elle ne peut pas contenir plusieurs instructions ou structures de contrôle (comme `if`, `foreach`, etc.).
    

Passons à la section suivante pour examiner la différence entre les fonctions fléchées et les [fonctions anonymes en PHP](https://flatcoding.com/tutorials/php-programming/php-anonymous-functions/).

## La différence entre les fonctions fléchées et les fonctions anonymes en PHP

PHP prend en charge deux types de fonctions anonymes (c'est-à-dire des fonctions sans nom) :

* **Fonctions anonymes traditionnelles** sont définies par le mot-clé `function`
    
* **Fonctions fléchées** sont introduites dans PHP 7.4 avec le mot-clé `fn`
    

Les deux types peuvent être assignés à des variables et utilisés pour des rappels ou comme arguments de fonction. Ils servent des objectifs similaires, mais diffèrent en syntaxe et en gestion des variables externes.

Examinons leurs différences clés.

### 1\. Syntaxe

#### Fonction fléchée :

Les fonctions fléchées utilisent une expression sur une seule ligne sans accolades ni instruction `return`.

```php
$square = fn($n) => $n * $n;
```

La fonction fléchée l'assigne à la variable `$square`. La fonction prend un paramètre, `$n`, et retourne `$n * $n` (le carré de `$n`).

#### Fonction anonyme :

```php
$square = function($n) {
    return $n * $n;
};
```

Les fonctions anonymes utilisent un bloc de fonction complet et nécessitent un `return` explicite. Elles sont utilisées pour une logique multi-lignes ou un comportement complexe.

### 2\. Portée des variables (Portée lexicale)

Les fonctions fléchées capturent automatiquement les variables de la portée externe :

```php
$factor = 2;
$multiply = fn($x) => $x * $factor;
```

Les fonctions anonymes nécessitent que vous importiez manuellement les variables externes en utilisant `use` :

```php
$factor = 2;
$multiply = function($x) use ($factor) {
    return $x * $factor;
};
```

Vous ne pouvez pas utiliser la variable dans la portée au sein de la fonction anonyme à moins d'utiliser le mot-clé `use`.

### 3\. Lisibilité et brièveté

Les fonctions fléchées sont plus courtes. Elles vous aident à écrire des rappels petits et à expression unique :

```php
$numbers = [1, 2, 3];
$squares = array_map(fn($n) => $n * $n, $numbers);
```

Mais les fonctions anonymes sont meilleures lorsque :

* Le corps de la fonction a plusieurs lignes.
    
* Vous avez besoin d'une logique complexe ou de structures de contrôle.
    

**Voici un tableau qui montre les différences clés :**

| Fonctionnalité | Fonction fléchée | Fonction anonyme |
| --- | --- | --- |
| Introduite dans | PHP 7.4 | PHP 5.3 |
| Syntaxe | Courte, expression unique | Verbose, corps de fonction complet |
| Gestion de la portée | Automatique (lexicale) | Manuelle (mot-clé `use`) |
| Corps multi-lignes | Non autorisé | Autorisé |
| Mot-clé return | Non utilisé | Requis |

Passons à la section suivante pour comprendre comment retourner une fonction fléchée à partir d'une autre fonction.

## Comment retourner des fonctions fléchées à partir d'autres fonctions

Les fonctions sont des citoyens de première classe. Cela signifie que vous pouvez retourner une fonction à partir d'une autre fonction. Cela inclut les fonctions fléchées.

Vous pouvez définir et retourner une fonction fléchée à partir d'une fonction régulière comme ceci :

```php
function getMultiplier($factor) {
    return fn($x) => $x * $factor;
}

$double = getMultiplier(2);
echo $double(5); // Affiche : 10
```

Dans cet exemple :

* `getMultiplier()` retourne une fonction fléchée.
    
* La fonction fléchée capture `$factor` depuis la portée externe automatiquement (portée lexicale).
    
* La fonction retournée peut être stockée dans une variable et utilisée comme n'importe quel autre appelable.
    

Cela vous permet de générer de petites fonctions basées sur des paramètres et réduit la répétition de code.

Utilisez cette syntaxe lorsque vous avez besoin de construire un comportement dynamique – comme des filtres personnalisés ou des usines de fonctions.

Passons à la section suivante pour voir comment vous pouvez utiliser les fonctions fléchées dans votre code.

## Comment utiliser les fonctions fléchées dans votre code

### Utiliser la fonction fléchée avec `array_map()` :

`array_map()` vous permet de définir un rappel pour chaque élément d'un tableau. Il vous permet de définir le rappel directement au sein de l'appel de fonction.

Exemple :

```php
$numbers = [1, 2, 3, 4, 5];

$squares = array_map(fn($n) => $n * $n, $numbers);

print_r($squares);
// Affiche : [1, 4, 9, 16, 25]
```

La fonction fléchée `fn($n) => $n * $n` est exécutée pour chaque élément du tableau `$numbers`. Le résultat est un nouveau tableau de valeurs au carré.

### Utiliser la fonction fléchée avec `array_filter()`

`array_filter()` filtre les éléments d'un tableau avec un rappel. Les fonctions fléchées définissent une condition de filtre courte en ligne.

Exemple :

```php
$numbers = [1, 2, 3, 4, 5, 6];

$evenNumbers = array_filter($numbers, fn($n) => $n % 2 === 0);

print_r($evenNumbers);
// Affiche : [2, 4, 6]
```

Ici, la fonction fléchée vérifie si chaque nombre est pair. Le résultat est un tableau qui contient uniquement les nombres pairs.

### Utiliser la fonction fléchée avec `array_reduce()`

`array_reduce()` réduit un tableau à une seule valeur basée sur une fonction de rappel. Les fonctions fléchées aident à rendre le code compact.

Exemple :

```php
$numbers = [1, 2, 3, 4, 5];

$sum = array_reduce($numbers, fn($carry, $n) => $carry + $n, 0);

echo $sum; // Affiche : 15
```

La fonction fléchée additionne chaque nombre dans le tableau. `$carry` contient le total en cours et `$n` est le nombre actuel.

### Imbriquer les fonctions fléchées en PHP

Ici, la fonction interne effectue une opération et la fonction externe traite les résultats de la fonction interne.

```php
$numbers = [1, 2, 3, 4, 5];

$doubleAndSquare = array_map(
    fn($n) => fn($x) => ($x * 2) ** 2,  
    $numbers
);

$results = array_map(
    fn($fn) => $fn(3),  
    $doubleAndSquare
);

print_r($results);
// Affiche : [36, 36, 36, 36, 36]
```

Dans le code ci-dessus, le premier `array_map()` crée une liste de fonctions fléchées qui doublent puis élèvent au carré le nombre. Chaque élément dans le tableau `$numbers` est mappé à une fonction fléchée imbriquée.

Le second `array_map()` applique la fonction fléchée interne (qui double et élève au carré la valeur) au nombre `3`. Cela donne un tableau du même résultat.

## Conclusion

Dans cet article, vous avez appris les fonctionnalités de base et la syntaxe des fonctions fléchées. Cela vous montre leurs avantages par rapport aux fonctions anonymes.

Voici quelques points clés à retenir :

1. Les fonctions fléchées ont été introduites dans PHP 7.4. Elles vous fournissent une nouvelle syntaxe pour définir des fonctions anonymes avec un code plus simple.
    
2. Les fonctions fléchées sont un moyen plus court d'écrire des fonctions anonymes. Elles utilisent une ligne de code et n'ont pas besoin d'accolades ou du mot-clé `return`.
    
3. Les fonctions fléchées obtiennent automatiquement les variables de la portée. Cela vous permet d'utiliser une fonction fléchée comme rappel dans des fonctions comme `array_map()` ou `array_filter()`.
    

Ressources :

* [Documentation PHP sur les fonctions fléchées](https://www.php.net/manual/en/functions.arrow.php)
    
* [Blog Flatcoding](https://flatcoding.com/) où je publie de nombreux autres tutoriels