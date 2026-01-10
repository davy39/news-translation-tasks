---
title: Qu'est-ce qu'une Table de Hachage ? Complexité Temporelle et Exemple Two Sum
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2024-01-25T17:02:13.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-hash-map
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/joan-gamell-ZS67i1HLllo-unsplash.jpg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: Hash tables
  slug: hash-tables
- name: Mapping
  slug: mapping
seo_title: Qu'est-ce qu'une Table de Hachage ? Complexité Temporelle et Exemple Two
  Sum
seo_desc: 'A hash table or hash map, is a data structure that helps with mapping keys
  to values for highly efficient operations like the lookup, insertion and deletion
  operations.

  In this tutorial, you''ll learn the following:


  Constant and linear time complexit...'
---

Une table de hachage ou carte de hachage, est une structure de données qui aide à mapper des clés à des valeurs pour des opérations hautement efficaces comme la recherche, l'insertion et la suppression.

Dans ce tutoriel, vous apprendrez les points suivants :

* Complexité temporelle constante et linéaire.
* Pourquoi utiliser une table de hachage ?
* Choses à considérer lors de l'écriture de fonctions de hachage.
* Comment résoudre le problème Two Sum en PHP et JavaScript.

## Qu'est-ce que la Complexité Temporelle Constante - O(1) ?

O(1) indique que le temps d'exécution d'un algorithme est constant, indépendamment de la taille de l'entrée. 

Cela implique que la performance de l'algorithme n'est pas dépendante de la taille de l'entrée. Un exemple est l'accès à un index d'un tableau.

```php
<?php

function constantTimeAlgorithm($arr) 
{
    
    echo $arr[0] . PHP_EOL;
}
```

Voici un exemple non-code pour illustrer le concept de complexité temporelle constante :

Imaginez envoyer un fichier par une compagnie aérienne à votre ami, et la compagnie aérienne a une politique où ils facturent en fonction du poids du colis.

Maintenant, que votre fichier pèse 2 grammes ou 20 kilogrammes, le temps de traitement de la compagnie aérienne reste constant. Cela signifie que le temps qu'il faut à la compagnie aérienne pour traiter votre colis ne dépend pas du poids du fichier – il est toujours le même. 

En d'autres termes, le temps de traitement est constant indépendamment de la taille du fichier.

## Qu'est-ce que la Complexité Temporelle Linéaire - O(n) ?

O(n) indique que le temps d'exécution d'un algorithme croît linéairement avec la taille de l'entrée. 

La performance de l'algorithme est directement proportionnelle à la taille de l'entrée. Un exemple est le parcours d'une boucle `for` et l'impression des éléments.

```php
<?php

function linearTimeAlgorithm($arr) 
{
    foreach ($arr as $element) {
        echo $element . PHP_EOL;
    }
}

```

Voici un exemple non-code pour illustrer le concept de complexité temporelle linéaire :

Considérez l'utilisation d'un service de transfert électronique pour envoyer un fichier à votre ami. Dans ce scénario, le temps nécessaire pour transférer le fichier augmente linéairement avec la taille du fichier. 

Par exemple, si cela prend 1 minute pour transférer un fichier de 100 Mo, cela prendrait environ 100 minutes pour transférer un fichier de 10 Go en utilisant le même service. 

Cette relation linéaire entre la taille du fichier et le temps nécessaire pour le transférer reflète la complexité temporelle linéaire. Le temps pris pour transférer le fichier augmente proportionnellement ou linéairement avec la taille de l'entrée ou du fichier.

## Pourquoi utiliser une Table de Hachage ?

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-108.png)
_Illustration de comment fonctionne une table de hachage_

Une table de hachage est une implémentation concrète du type de données abstrait connu sous le nom de tableau associatif. 

Dans une table de hachage, les clés sont hachées pour déterminer l'index où les valeurs correspondantes seront stockées, permettant une récupération et un stockage efficaces des paires clé-valeur. 

Cette implémentation fournit généralement des temps d'accès rapides pour des opérations comme l'insertion, la suppression et la recherche de valeurs basées sur leurs clés associées. 

Dans des langages comme PHP ou JavaScript, lorsque vous utilisez un tableau associatif, vous utilisez essentiellement une table de hachage. Leurs tableaux associatifs sont implémentés en utilisant des tables de hachage en coulisses. 

Vous pouvez utiliser des chaînes de caractères, des entiers ou d'autres types de données comme clés, et le mécanisme de hachage interne du langage mappe efficacement ces clés à leurs valeurs correspondantes. De plus, JavaScript fournit l'objet `Map` pour des fonctionnalités de table de hachage plus avancées.

### Complexité Temporelle et Spatiale pour une Table de Hachage

La complexité temporelle et spatiale pour une table de hachage (ou table de hachage) n'est pas nécessairement O(n) pour toutes les opérations. La complexité temporelle typique et souhaitée pour les opérations de base comme l'insertion, la recherche et la suppression dans une table de hachage bien conçue est O(1) en moyenne. 

Voici une ventilation de la complexité temporelle et spatiale pour une table de hachage :

#### Complexité Temporelle :

Cas Moyen :

* Insertion (moyenne) : O(1)
* Recherche (moyenne) : O(1)
* Suppression (moyenne) : O(1)

Pire Cas :

* Insertion (pire) : O(n), où n est la taille de la table de hachage. Cela se produit lorsqu'il y a de nombreuses collisions de hachage, conduisant à un sondage linéaire ou à d'autres stratégies de résolution de collisions qui peuvent impliquer de parcourir toute la table de hachage.
* Recherche et Suppression (pire) : O(n), pour la même raison que l'insertion.

#### Complexité Spatiale :

* La complexité spatiale est généralement O(n). Où n est le nombre de paires clé-valeur stockées dans la table de hachage. Chaque paire clé-valeur occupe un espace constant, et l'espace requis croît linéairement avec le nombre d'éléments.

Dans l'analyse des algorithmes, la notation O(1) et O(n) représentent les bornes supérieures de la complexité temporelle d'un algorithme, où n est la taille de l'entrée.

#### Opérations

1. **Insertion :** La paire clé-valeur est hachée, et l'index résultant est utilisé pour stocker la valeur dans l'emplacement correspondant. Si une collision se produit, la stratégie de résolution de collision est appliquée.
2. **Suppression :** La clé est hachée pour trouver l'index, et l'élément à cet index est supprimé. La résolution de collision peut être nécessaire.
3. **Recherche :** La clé est hachée pour trouver l'index, et la valeur à cet index est retournée. La résolution de collision peut être appliquée si nécessaire.

## Choses à considérer lors de la création de tables de hachage

Lors de la création de tables de hachage, il y a plusieurs considérations importantes pour assurer l'efficacité, y compris le calcul rapide des codes de hachage et des stratégies efficaces de résolution de collisions.

### Calcul rapide

Les codes de hachage doivent être calculés rapidement pour assurer des opérations d'insertion, de recherche et de suppression efficaces. Une bonne fonction de hachage contribue à la vitesse de calcul du code de hachage.

### Éviter les collisions

Une collision se produit lorsque deux clés ou plus produisent le même code de hachage. En d'autres termes, plusieurs clés mappent au même index de tableau.

## Comment gérer les collisions

Les tables de hachage utilisent des techniques de résolution de collisions pour gérer les collisions. Les stratégies courantes incluent :

#### Chaînage

Pour gérer plusieurs valeurs avec le même code de hachage, le chaînage implique de stocker une liste liée ou une autre structure de données à chaque index de tableau. Si une collision se produit, la nouvelle paire clé-valeur est ajoutée à la liste liée à l'index pertinent.

#### Adressage ouvert

Lorsque une collision se produit dans une table de hachage, une technique appelée adressage ouvert est employée pour la résoudre en cherchant l'espace ouvert suivant. 

Tout ce qu'elle fait est de chercher dans le tableau l'emplacement vide suivant où la combinaison clé-valeur peut être placée. Des méthodes incluant le double hachage, le sondage quadratique et le sondage linéaire sont appliquées.

**Sondage Linéaire :** Dans le sondage linéaire, l'algorithme se déplace linéairement à l'index suivant dans le tableau afin de trouver l'emplacement ouvert suivant lorsqu'une collision se produit.

**Sondage Quadratique :** Dans cette méthode, un algorithme emploie une fonction quadratique pour trouver l'emplacement suivant qui devient disponible.

**Double Hachage :** Dans le double hachage, l'algorithme calcule la taille du pas entre les sondages en utilisant une fonction de hachage secondaire.

Afin de réduire la possibilité de collisions, une bonne fonction de hachage doit générer des codes de hachage distincts pour diverses entrées. En s'assurant que les codes de hachage sont uniformément distribués dans la plage des valeurs potentielles, les collisions peuvent être évitées.

## Comment résoudre le problème Two Sum

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-117.png)
_Problème Two Sum_

Le problème Two Sum implique de trouver toutes les paires d'éléments dans un tableau qui s'additionnent pour donner une valeur cible spécifique. Maintenant, regardons l'énoncé du problème.

### Énoncé du problème

Étant donné un tableau d'entiers `nums` et un entier `target`, retourner les indices des deux nombres tels qu'ils s'additionnent pour donner le `target`.

_Exemple 1 :_

**Entrée :** nums = [3,2,4, 8], target = 12

**Sortie :** [2, 3]

_Exemple 2 :_

**Entrée :** nums = [5,5], target = 10 

**Sortie :** [0,1]

### Solution

Pour résoudre le problème Two Sum, nous pouvons utiliser une table de hachage. L'idée est de parcourir le tableau `nums` et, pour chaque élément, vérifier si le complément (la différence entre la cible et l'élément actuel) est déjà dans la table de hachage. Si c'est le cas, nous avons trouvé une paire d'indices dont les éléments s'additionnent pour donner la cible.

Voici les étapes à suivre :

1. Pour contenir les éléments et leurs indices respectifs, créer une table de hachage vide lors de l'initialisation.
2. Parcourir le tableau de `nums`.
3. Faire le calcul du complément (cible - élément actuel) pour chaque élément.
4. Vérifier si le complément a déjà été ajouté à la table de hachage. Si oui, retourner l'index actuel et l'index stocké dans la table de hachage pour le complément.
5. Si le complément n'est pas dans la table de hachage, stocker l'élément actuel et son index dans la table de hachage.
6. Si aucune paire n'est trouvée lors du parcours, cela implique qu'il n'y a pas de solution.

##### Solution de code PHP

```php
<?php

function twoSum($nums, $target) {
    $hashTable = [];

    foreach ($nums as $i => $num) {
        $complement = $target - $num;

        if (array_key_exists($complement, $hashTable)) {
        
            // Trouvé la paire, retourner les indices
            return [$hashTable[$complement], $i];
        }

        // Stocker l'élément actuel dans la table de hachage
        $hashTable[$num] = $i;
    }

    // Aucune solution trouvée
    return [];
}

// Exemple d'utilisation :
$nums = [2, 7, 11, 5, 15, 30];
$target = 12;
$result = twoSum($nums, $target);

echo "Indices des deux nombres : [" . implode(", ", $result) . "]";

```

##### Solution de code JavaScript utilisant la fonction `map`

```javascript
function twoSum(nums, target) {
    const hashTable = new Map();

    for (const [index, num] of nums.entries()) {
        const complement = target - num;

        // Vérifier si le complément est dans la Map
        if (hashTable.has(complement)) {
        
            // Trouvé la paire, retourner les indices
            return [hashTable.get(complement), index];
        }

        // Stocker le nombre actuel et son index dans la Map
        hashTable.set(num, index);
    }

    // Aucune solution trouvée
    return [];
}

// Exemple d'utilisation :
const nums = [2, 7, 11, 5, 15, 30];
const target = 12;
const result = twoSum(nums, target);

console.log(`Indices des deux nombres qui s'additionnent pour donner ${target} : [${result.join(', ')}]`);

```

Cette approche a une complexité temporelle de O(n) car nous parcourons le tableau une fois. La complexité spatiale est également O(n) en raison du stockage des éléments dans la table de hachage.

## Ressources

1. [Table de hachage de Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
2. [Tables de hachage en Python](https://www.youtube.com/watch?v=RcZsTI5h0kg)

## Conclusion

Dans cet article, vous avez appris les tables de hachage, les choses à considérer lors de l'écriture de fonctions de hachage et un problème réel qui implique de résoudre le problème Two Sum.

Continuez à apprendre, et bon codage !

Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/suleolanrewaju/) et [Twitter](https://twitter.com/bigdevlarry).