---
title: Exemples de Notation Big O – Complexité Temporelle et Efficacité des Algorithmes
  Expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T15:50:42.000Z'
originalURL: https://freecodecamp.org/news/big-o-notation-examples-time-complexity-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60625dd39618b008528a9495.jpg
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
seo_title: Exemples de Notation Big O – Complexité Temporelle et Efficacité des Algorithmes
  Expliquées
seo_desc: "By Jeremy L Thompson\nTime complexity analysis helps us determine how much\
  \ more time our algorithm needs to solve a bigger problem. \nIn this article, I\
  \ will explain what Big O notation means in time complexity analysis. We'll look\
  \ at three different a..."
---

Par Jeremy L Thompson

L'analyse de la complexité temporelle nous aide à déterminer combien de temps supplémentaire notre algorithme a besoin pour résoudre un problème plus grand.

Dans cet article, je vais expliquer ce que signifie la notation Big O dans l'analyse de la complexité temporelle. Nous examinerons trois algorithmes différents pour vérifier si un nombre est premier, et nous utiliserons la notation Big O pour analyser la complexité temporelle de ces algorithmes.

## Que signifie la Notation Big O ?

La notation Big O décrit comment le temps d'exécution estimé d'un algorithme augmente lorsque nous augmentons la taille du problème que nous résolvons.

Considérons quelques algorithmes hypothétiques pour trier une liste de nombres.

Si nous avons un algorithme `O(n)` pour trier une liste, la quantité de temps que nous prenons augmente linéairement à mesure que nous augmentons la taille de notre liste.

Une liste qui a 10 fois plus de nombres prendra environ 10 fois plus de temps à trier. Cela signifie que si le tri de `10` nombres nous prend `4` secondes, alors nous nous attendrions à ce que le tri d'une liste de `100` nombres nous prenne environ `40` secondes.

Si nous avons plutôt un algorithme `O(n²)` pour trier une liste, alors nous devrions nous attendre à ce que la quantité de temps que nous prenons augmente quadratiquement à mesure que nous augmentons la taille de notre liste.

Une liste qui a `10` fois plus de nombres prendra environ `100` fois plus de temps à trier ! Cela signifie que si le tri de `10` nombres nous prend `4` secondes, alors nous nous attendrions à ce que le tri d'une liste de `100` nombres nous prenne environ `400` secondes.

Les algorithmes les plus rapides pour trier une liste sont en fait `O(n log(n))`. Avec ces algorithmes, nous pouvons nous attendre à ce qu'une liste avec `10` fois plus de nombres prenne environ `23` fois plus de temps à trier.

En d'autres termes, si le tri de `10` nombres nous prend `4` secondes, alors nous nous attendrions à ce que le tri d'une liste de `100` nombres nous prenne environ `92` secondes.

## Exemple de Big O - Vérificateur de Nombres Premiers

Maintenant que nous savons ce que la notation Big O nous indique, examinons comment nous utilisons la notation Big O dans l'analyse de la complexité temporelle.

Dans cette section, nous examinerons trois algorithmes différents pour vérifier si un nombre est _premier_. Par définition d'un nombre _premier_, `num` est _premier_ si les seuls nombres qui divisent `num` de manière égale sont `1` et `num` lui-même.

### Algorithme 1 - Vérifier Tous les Diviseurs Possibles

Le plus simple algorithme auquel je puisse penser pour vérifier si un nombre est _premier_ est de vérifier s'il y a des diviseurs autres que `1` et `num` lui-même.

Dans la fonction `is_prime_all()` ci-dessous, j'essaie de diviser chaque nombre entre `1` et `num` par `num` et je vérifie s'il y a un reste.

J'ai écrit ce code en Rust afin de pouvoir utiliser [criterion](https://docs.rs/criterion) pour mesurer les performances d'exécution, mais l'analyse de la complexité temporelle avec la notation Big O fonctionne de la même manière avec tous les langages de programmation.

Si vous souhaitez exécuter criterion avec ce code sur votre ordinateur, vous pouvez trouver le code source Rust sur [GitHub](https://github.com/jeremylt/time_complexity).

```rust
pub fn is_prime_all(num: i64) -> bool {
    // Vérifier les diviseurs de num
    for i in 2..num {
        if num % i == 0 {
            // Tout diviseur autre que 1 ou num signifie que num n'est pas premier
            return false;
        }
    }
    // Aucun autre diviseur trouvé signifie que num est premier
    return true;
}

```

Nous devons vérifier `num - 2` nombres différents avec cet algorithme avant de pouvoir dire que `num` est premier, donc cet algorithme a une complexité temporelle de `O(num)` ou `O(n)`.

Vous avez probablement remarqué que nous avons supprimé le `-2` de notre notation Big O. Lorsque nous calculons la complexité temporelle en notation Big O pour un algorithme, nous ne nous intéressons qu'au plus grand facteur de `num` dans notre équation, donc tous les termes plus petits sont supprimés.

Lorsque j'ai testé ma fonction, il a fallu en moyenne `5,9` microsecondes à mon ordinateur pour vérifier que `1 789` est premier et en moyenne `60,0` microsecondes pour vérifier que `17 903` est premier.

Cela signifie qu'il faut environ `10` fois plus de temps pour vérifier un nombre qui est `10` fois plus grand, ce que nous attendions de notre analyse de complexité temporelle !

### Algorithme 2 - Vérifier la Moitié des Diviseurs Possibles

Nous pouvons améliorer notre algorithme. Si notre nombre, `num`, n'est pas divisible par `2`, alors nous savons aussi que notre nombre ne peut pas être divisible par `num/2` ou un nombre plus grand. Cela signifie que nous pouvons vérifier moins de nombres :

```rust
pub fn is_prime_half(num: i64) -> bool {
    // Vérifier les diviseurs de num
    for i in 2..num / 2 {
        if num % i == 0 {
            // Tout diviseur autre que 1 ou num signifie que num n'est pas premier
            return false;
        }
    }
    // Aucun autre diviseur trouvé signifie que num est premier
    return true;
}

```

Ce code prend deux fois moins de temps à s'exécuter. Sur mon ordinateur, il ne faut que `3,1` microsecondes pour vérifier que `1 789` est premier. Malheureusement, il faut `31,1` microsecondes pour vérifier que `17 903` est premier, ce qui signifie que la complexité temporelle de notre algorithme n'a pas changé !

Cela est dû au fait que notre plus grand facteur de `num` était le même dans la complexité temporelle de notre nouvel algorithme. Nous devons vérifier `num/2 - 1` valeurs, ce qui signifie que notre algorithme est toujours `O(n)`.

### Algorithme 3 - Vérifier Toutes les Paires de Diviseurs Possibles

Essayons un troisième algorithme et voyons si nous pouvons obtenir une complexité temporelle plus faible.

Pour cet algorithme, nous allons améliorer notre deuxième algorithme. Dans l'algorithme 2, nous utilisons le fait que si `2` n'est pas un diviseur de notre nombre, `num`, alors `num/2` ne peut pas non plus être un diviseur.

Mais ce n'est pas un tour spécial que nous pouvons seulement faire avec `2`. Si `3` n'est pas un diviseur de notre nombre, alors `num/3` ne peut pas non plus être un diviseur. Si `4` n'est pas un diviseur de notre nombre, alors `num/4` ne peut pas être un diviseur non plus.

Le plus grand nombre que nous devons vérifier est `√num`, car `√num * √num = num`.

```rust
pub fn is_prime_sqrt(num: i64) -> bool {
    // Vérifier les diviseurs de num
    for i in 2..=(num as f64).sqrt() as i64 {
        if num % i == 0 {
            // Tout diviseur autre que 1 ou num signifie que num n'est pas premier
            return false;
        }
    }
    // Aucun autre diviseur trouvé signifie que num est premier
    return true;
}

```

Nous ne vérifions que `√num - 1` nombres différents, donc cela signifie que notre complexité temporelle devrait être `O(√n)`. Lorsque je l'exécute sur mon ordinateur, je vois qu'il ne faut que `161,9` nanosecondes pour vérifier que `1 789` est premier et `555,0` nanosecondes pour vérifier que `17 903` est premier.

Cela signifie qu'il a fallu environ `3,4` fois plus de temps pour vérifier un nombre qui est `10` fois plus grand, et `√10 ≈ 3,2`. Notre analyse de complexité estime avec précision combien de temps il faut pour vérifier des nombres premiers plus grands avec cet algorithme.

## Résumé

L'analyse de la complexité temporelle nous aide à déterminer combien de temps supplémentaire notre algorithme a besoin pour résoudre un problème plus grand.

Nous avons examiné ce que signifie la notation Big O dans l'analyse de la complexité temporelle, et nous avons utilisé la notation Big O pour analyser la complexité temporelle de trois algorithmes de vérification de primalité.