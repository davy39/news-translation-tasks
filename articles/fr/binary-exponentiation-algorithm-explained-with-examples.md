---
title: Algorithme d'Exponentiation Binaire – Expliqué avec des Exemples Pratiques
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-10-14T19:40:15.140Z'
originalURL: https://freecodecamp.org/news/binary-exponentiation-algorithm-explained-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728672475917/5eeec863-5481-42d8-8b1f-9c92915f570f.png
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: Competitive programming
  slug: competitive-programming
- name: MathJax
  slug: mathjax
seo_title: Algorithme d'Exponentiation Binaire – Expliqué avec des Exemples Pratiques
seo_desc: Binary exponentiation, also known as exponentiation by squaring, is a powerful
  algorithm used to efficiently calculate large powers of numbers. This technique
  is particularly useful in various fields of computer science, including cryptography,
  compe...
---

L'exponentiation binaire, également connue sous le nom d'exponentiation par carrés, est un algorithme puissant utilisé pour calculer efficacement de grandes puissances de nombres. Cette technique est particulièrement utile dans divers domaines de l'informatique, notamment la cryptographie, la programmation compétitive et les graphiques informatiques.

Dans cet article, nous allons explorer le concept d'exponentiation binaire, comprendre son fonctionnement et l'implémenter en code.

## Qu'est-ce que l'Exponentiation Binaire ?

L'exponentiation binaire est une méthode pour calculer \\(a^n\\) (a élevé à la puissance n) en utilisant uniquement des multiplications, au lieu des \\(O(n)\\) multiplications naïves.

Cette amélioration significative de l'efficacité permet de calculer des puissances extrêmement grandes rapidement, même en utilisant l'arithmétique modulaire.

## Comment Fonctionne l'Exponentiation Binaire

L'idée clé derrière l'exponentiation binaire est de décomposer l'exposant en sa représentation binaire et d'utiliser les propriétés des exposants pour simplifier le calcul.

Décomposons cela étape par étape :

1. Convertir l'exposant `n` en sa représentation binaire.

2. Initialiser le résultat à 1 et la base à `a`.

3. Parcourir chaque bit de la représentation binaire de `n` de droite à gauche : (a). Si le bit actuel est 1, multiplier le résultat par la base actuelle. (b). Élever la base au carré (la multiplier par elle-même).

4. Retourner le résultat final.

Par exemple, calculons \\(3^{13}\\) :

1. Convertir 13 en binaire : \\(13_{10} = 1101_2\\)

2. Initialiser résultat = 1, base = 3

3. Parcourir les bits :

    * Bit 1 : résultat = \\(1 * 3 = 3\\)*, base =* \\(3 * 3 = 9\\)

    * Bit 0 : résultat = 3, base = \\(9 * 9 = 81\\)

    * Bit 1 : résultat = \\(3 * 81 = 243\\)*, base =* \\(81 * 81 = 6561\\)

    * Bit 1 : résultat = \\(243 * 6561 = 1,594,323\\)

Ainsi, \\(3^{13} = 1,594,323.\\)

## Pourquoi l'Exponentiation Binaire est Efficace

L'efficacité de l'exponentiation binaire provient de deux facteurs principaux :

1. **Nombre réduit de multiplications** : Au lieu d'effectuer `n-1` multiplications comme dans l'approche naïve, nous n'effectuons que \\(O(log n)\\) multiplications. Cela est dû au fait que nous décomposons essentiellement le problème en sous-problèmes plus petits basés sur la représentation binaire de l'exposant.

2. **Réutilisation des calculs précédents** : En élevant la base au carré à chaque étape, nous réutilisons les résultats des calculs précédents, ce qui réduit considérablement le nombre total d'opérations nécessaires.

Pour illustrer cette efficacité, considérons le calcul de \\(a^{1000000}\\). L'approche naïve nécessiterait 999,999 multiplications, tandis que l'exponentiation binaire ne nécessiterait qu'environ 20 multiplications (car \\(\log_2(1000000) \approx 20\\)).

## Implémentation de l'Algorithme

Implémentons l'algorithme d'exponentiation binaire en Python :

```python
def binary_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        # Si le bit actuel est 1, multiplier le résultat par la base actuelle
        if exponent & 1:
            result *= base
        # Élever la base au carré
        base *= base
        # Passer au bit suivant
        exponent >>= 1
    return result

# Exemple d'utilisation
print(binary_exponentiation(3, 13))  # Sortie : 1594323
```

Décomposons l'algorithme :

1. Nous initialisons `result` à 1, qui est l'identité pour la multiplication.

2. Nous utilisons une boucle while pour itérer jusqu'à ce que l'exposant devienne 0.

3. Nous vérifions si le bit le moins significatif de l'exposant est 1 en utilisant l'opérateur bitwise AND `&`. Si c'est le cas, nous multiplions le résultat par la base actuelle.

4. Nous élevons la base au carré en la multipliant par elle-même.

5. Nous utilisons l'opérateur de décalage à droite `>>=` pour passer au bit suivant de l'exposant.

6. Enfin, nous retournons le résultat.

### Analyse de la Complexité Temporelle

La complexité temporelle de l'exponentiation binaire est \\(O(log n)\\), où `n` est l'exposant. Cela est dû au fait que :

1. Le nombre de bits dans la représentation binaire de `n` est \\(\lfloor \log_2 n\rfloor + 1\\).

2. Nous effectuons au plus deux multiplications par bit (une pour élever la base au carré, et potentiellement une pour mettre à jour le résultat).

Par conséquent, le nombre total de multiplications est au plus \\(2(\lfloor \log_2 n \rfloor + 1)\\), ce qui se simplifie en \\(O(\log n)\\).

## Exemples de Problèmes et Solutions

Examinons quelques problèmes algorithmiques que vous pouvez résoudre efficacement en utilisant l'exponentiation binaire, avec des explications détaillées des solutions et comment nous en sommes arrivés à utiliser l'exponentiation binaire.

### Problème 1 : Exponentiation Modulaire

**Problème** : Calculer \\(3^{1000000} \bmod 1000000007\\).

**Approche** :

1. Nous reconnaissons que ce problème implique un exposant très grand (1000000), ce qui serait impraticable à calculer en utilisant l'exponentiation naïve.

2. Nous remarquons également que nous devons trouver le résultat modulo un grand nombre premier (1000000007).

3. Cette combinaison d'un grand exposant et de l'arithmétique modulaire est un indicateur clair que nous devons utiliser l'exponentiation binaire modulaire.

**Solution** : Nous allons modifier notre fonction d'exponentiation binaire pour inclure l'arithmétique modulaire :

```python
def mod_binary_exponentiation(base, exponent, mod):
    result = 1
    base %= mod
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent >>= 1
    return result

print(mod_binary_exponentiation(3, 1000000, 1000000007))  # Sortie : 624098969
```

**Explication** :

1. Nous initialisons `result` à 1 et définissons `base` à `base % mod` pour gérer les cas où la base initiale est plus grande que le module.

2. La boucle principale fonctionne de manière similaire à l'algorithme d'exponentiation binaire original, mais avec deux différences clés :

    a. Lorsque nous mettons à jour `result`, nous effectuons `(result * base) % mod`. Cela garantit que `result` ne dépasse jamais `mod`, empêchant le débordement d'entier et maintenant le résultat modulaire correct.

    b. Lorsque nous élevons `base` au carré, nous effectuons `(base * base) % mod` pour la même raison.

3. Les opérations bitwise (`exponent & 1` et `exponent >>= 1`) fonctionnent exactement comme dans l'algorithme original, nous permettant de traiter la représentation binaire de l'exposant efficacement.

4. En appliquant l'opération modulo à chaque étape, nous nous assurons que tous les résultats intermédiaires restent dans la plage \[0, mod-1\]. Cela est possible grâce aux propriétés de l'arithmétique modulaire :

    $$(a\u22c5b)modm=((amodm)\u22c5(bmodm))modm$$

Ce problème serait impossible à résoudre avec l'exponentiation naïve en raison du résultat énorme, mais l'exponentiation binaire modulaire le rend traitable en gardant tous les résultats intermédiaires gérables.

### Problème 2 : Exponentiation de Matrices

**Problème** : Étant donné une matrice 2x2 A, calculer An où n = 1000000.

**Approche** :

1. Nous observons que nous devons élever une matrice à une puissance très grande (1000000).

2. La multiplication de matrices est associative, ce qui nous permet d'utiliser le même principe que l'exponentiation binaire pour les nombres.

3. Nous reconnaissons que c'est un scénario parfait pour appliquer l'exponentiation binaire aux matrices.

**Solution** : Nous pouvons utiliser l'exponentiation binaire sur les matrices. Voici une implémentation Python avec des explications :

```python
import numpy as np

def matrix_multiply(A, B, mod):
    return np.array([[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
                     [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]])

def matrix_power(A, n, mod):
    result = np.eye(2, dtype=int)
    while n > 0:
        if n & 1:
            result = matrix_multiply(result, A, mod)
        A = matrix_multiply(A, A, mod)
        n >>= 1
    return result

A = np.array([[1, 1], [1, 0]])
n = 1000000
mod = 1000000007

result = matrix_power(A, n, mod)
print(result)  # Sortie : [[690749268 297612485]
                #         [297612485 393136783]]
```

**Explication** :

1. `matrix_multiply(A, B, mod)` :

    * Cette fonction effectue la multiplication de matrices de deux matrices 2x2, A et B.

    * Chaque élément de la matrice résultante est calculé en utilisant la formule standard de multiplication de matrices, suivie d'une opération modulo pour garder les valeurs gérables.

2. `matrix_power(A, n, mod)` :

    * Cette fonction implémente l'exponentiation binaire pour les matrices.

    * Nous commençons avec `result` comme la matrice identité 2x2 (créée en utilisant `np.eye(2, dtype=int)`).

    * La boucle principale suit le même schéma que l'exponentiation binaire scalaire : a. Si le bit actuel de n est 1, nous multiplions `result` par le `A` actuel. b. Nous élevons `A` au carré (en le multipliant par lui-même). c. Nous décalons n à droite pour passer au bit suivant.

    * Toutes les multiplications de matrices sont effectuées en utilisant notre fonction `matrix_multiply`, qui incorpore l'arithmétique modulaire.

Cette technique d'exponentiation de matrices est particulièrement puissante pour résoudre les relations de récurrence linéaires en temps logarithmique, comme démontré ici avec la suite de Fibonacci.

## Problèmes Pratiques

Voici quelques problèmes à résoudre en utilisant l'exponentiation binaire :

1. **Exponentiation Modulaire** : Calculer \\(7^{1234567} \bmod 1000000009\\). (Indice : Utilisez la fonction `mod_binary_exponentiation` du Problème 1 dans les exemples.)

2. **Dernier Chiffre** : Trouver le dernier chiffre de . (Indice : Observez le motif des derniers chiffres des puissances de 2 et utilisez l'exponentiation binaire avec modulo 10.)

3. **Tour de Puissances** : Calculer les trois derniers chiffres de \\(2^{2^{20}}\\). (Indice : Utilisez la propriété de l'arithmétique modulaire que \\(a^b \bmod m = a^{b \bmod \phi(m)} \bmod m\\) où \\(\phi\\) est la fonction indicatrice d'Euler. Vous devrez d'abord calculer \\(2^{20} \bmod \phi(1000)\\).)

4. **Chaînes de Matrices** : Étant donné une matrice 2x2 A = \[\[1, 2\], \[3, 4\]\], calculer les deux derniers chiffres de la somme de tous les éléments dans \\(A^{1000000}\\). (Indice : Utilisez l'exponentiation de matrices comme dans le Problème 2 des exemples, mais ne gardez trace que des deux derniers chiffres de chaque élément. Vous devrez faire la somme des éléments après l'exponentiation finale.)

5. **Suite de Fibonacci** : Trouver le 1000000ème nombre de Fibonacci modulo 1000000007. (Indice : Utilisez la forme matricielle de la suite de Fibonacci (\[\[1, 1\], \[1, 0\]\]) et appliquez l'exponentiation de matrices comme montré dans le Problème 2 des exemples.)

## Conclusion

L'exponentiation binaire est une technique puissante qui peut être appliquée à une large gamme de problèmes impliquant de grands exposants. Comme nous l'avons vu dans les exemples et les problèmes pratiques, elle est particulièrement utile en arithmétique modulaire, en opérations matricielles et en résolution de relations de récurrence.

En pratiquant ces problèmes, vous acquerrez une compréhension plus profonde de la manière d'appliquer l'exponentiation binaire dans divers scénarios. N'oubliez pas que la clé est de reconnaître quand un problème implique l'élévation de quelque chose à une grande puissance, qu'il s'agisse d'un nombre, d'une matrice ou même d'une structure plus complexe.

Si vous avez trouvé cette explication de l'algorithme d'exponentiation binaire utile, vous pourriez également apprécier des tutoriels et concepts de programmation plus approfondis que je couvre sur mon [blog](https://blog.theenthusiast.dev).