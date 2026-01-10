---
title: "xor.py \x13 Comment fonctionne l'opérateur XOR en Python"
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-05-08T16:35:55.000Z'
originalURL: https://freecodecamp.org/news/xor-py-how-the-python-xor-operator-works
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/xor-in-python.png
tags:
- name: Python
  slug: python
seo_title: "xor.py \x13 Comment fonctionne l'opérateur XOR en Python"
seo_desc: "You can use bitwise operators in Python to perform different operations\
  \ on the individual bits of an integer. \nThere are different bitwise operators\
  \ like the bitwise AND (&), bitwise OR (|), bitwise XOR (^), and so on. \nIn this\
  \ article, we'll focus o..."
---

Vous pouvez utiliser des opérateurs bit à bit en Python pour effectuer différentes opérations sur les bits individuels d'un entier. 

Il existe différents opérateurs bit à bit comme le ET bit à bit (`&`), le OU bit à bit (`|`), le XOR bit à bit (`^`), et ainsi de suite. 

Dans cet article, nous nous concentrerons sur l'opérateur XOR bit à bit (`^`). Vous apprendrez son mode de fonctionnement ainsi que quelques exemples pratiques. 

## Comment fonctionne l'opérateur XOR en Python

L'opérateur XOR convertit d'abord les entiers impliqués dans l'opération en leur format binaire. L'opérateur évalue ensuite les bits correspondants des valeurs binaires.

Lorsque deux bits sont évalués, la valeur retournée dépendra des bits. Si les deux bits sont 0, 0 est retourné. Si les deux bits sont 1, 0 est retourné. Si l'un des bits est 1 tandis que l'autre est 0, alors 1 sera retourné. 

Ainsi, l'opérateur XOR ne retournera 1 que lorsque deux bits ont des valeurs différentes. C'est-à-dire : 

0 ^ 0 = 0.   
1 ^ 1 = 0.  
1 ^ 0 = 1.  
0 ^ 1 = 1.

Après avoir évalué tous les bits correspondants, la valeur binaire résultante sera retournée en base 10. 

Ne vous inquiétez pas si les explications ci-dessus semblent confuses  les exemples dans la section suivante devraient simplifier le fonctionnement de l'opérateur XOR.

## Exemple d'opérateur XOR en Python

Dans cette section, vous verrez des exemples de code qui montrent comment fonctionne l'opérateur XOR bit à bit. 

```python
x = 12
y = 10

print(x ^ y)
# 6
```

Dans le code ci-dessus, nous avons créé deux variables `x` et `y` avec 12 et 10 comme valeurs respectives. 

En utilisant l'opérateur XOR  `x ^ y`  nous avons obtenu 6 comme résultat. 

Décomposons le code pour voir comment nous avons obtenu une valeur de 6 à partir de l'opération.

### Étape #1 - Conversion en valeurs binaires

Nous avons commencé avec deux valeurs (12 et 10) :

```python
x = 12
y = 10
```

Ces valeurs doivent être converties en leur format binaire par l'opérateur XOR avant que les opérations ne commencent. 

La valeur binaire de 12 est 1100 tandis que la valeur binaire de 10 est 1010. 

### Étape #2 - Évaluation des bits correspondants

Maintenant que les valeurs ont été converties en leurs formats binaires, la prochaine chose que fait l'opérateur XOR est de comparer les bits correspondants. 

Ainsi, le premier bit de 1100 sera comparé au premier bit de 1010. Le deuxième bit des deux valeurs binaires sera comparé ensuite. Cette comparaison se poursuivra jusqu'à ce qu'il n'y ait plus de bits à comparer. 

Rappelons que nous avons discuté de la manière dont l'opérateur XOR retourne une valeur de chaque comparaison : 

0 ^ 0 = 0.   
1 ^ 1 = 0.  
1 ^ 0 = 1.  
0 ^ 1 = 1.

En utilisant la logique ci-dessus, comparons les bits des deux opérandes  1100 et 1010. Nous les désignerons comme opérande A et B, respectivement.

Valeur du premier bit de l'opérande A = 1. Valeur du premier bit de l'opérande B = 1.   
1 ^ 1 = 0. 

Valeur du deuxième bit de l'opérande A = 1. Valeur du deuxième bit de l'opérande B = 0.   
1 ^ 0 = 1. 

Valeur du troisième bit de l'opérande A = 0. Valeur du troisième bit de l'opérande B = 1.   
0 ^ 1 = 1. 

Valeur du quatrième bit de l'opérande A = 0. Valeur du quatrième bit de l'opérande B = 0.   
0 ^ 0 = 0. 

Lorsque nous collectons les valeurs résultantes de chaque comparaison, nous obtenons 0110 qui est le même que 6 en base 10. 

Les comparaisons de bits ci-dessus expliquent comment le code de la section précédente a retourné une valeur de 6. C'est-à-dire :

```python
x = 12
y = 10

print(x ^ y)
# 6
```

## Résumé

Dans cet article, nous avons parlé des opérateurs bit à bit en Python. Ils sont utilisés pour effectuer des opérations impliquant les bits individuels des entiers. 

Nous avons parlé de l'opérateur XOR bit à bit (`^`) qui convertit les entiers en leur format binaire, puis compare leurs valeurs de bits correspondantes. 

Nous avons vu un exemple qui montrait comment l'opérateur XOR fonctionne sous le capot. 

Bonne programmation ! Vous pouvez en apprendre plus sur Python sur [mon blog](https://ihechikara.com/).