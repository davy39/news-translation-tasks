---
title: 'Typeerror: int object is not callable – Comment le corriger en Python'
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-18T14:10:48.000Z'
originalURL: https://freecodecamp.org/news/typeerror-int-object-is-not-callable-how-to-fix-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/typeerror.png
tags:
- name: error
  slug: error
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: 'Typeerror: int object is not callable – Comment le corriger en Python'
seo_desc: "In Python, a “Typeerror” occurs when you use different data types in an\
  \ operation. \nFor example, if you attempt to divide an integer (number) by a string,\
  \ it leads to a typeerror because an integer data type is not the same as a string.\
  \ \nOne of those..."
---

En Python, une « Typeerror » se produit lorsque vous utilisez différents types de données dans une opération. 

Par exemple, si vous essayez de diviser un entier (nombre) par une chaîne de caractères, cela conduit à une `typeerror` car un type de données entier n'est pas le même qu'une chaîne de caractères. 

L'une de ces erreurs de type est l'erreur « int object is not callable ».

L'erreur « int object is not callable » se produit lorsque vous déclarez une variable et que vous la nommez avec un nom de fonction intégrée tel que `int()`, `sum()`, `max()`, et autres.

L'erreur se produit également lorsque vous n'indiquez pas d'opérateur arithmétique lors de l'exécution d'une opération mathématique.

Dans cet article, je vais vous montrer comment l'erreur se produit et ce que vous pouvez faire pour la corriger.

## Comment corriger `Typeerror: int object is not callable` dans les noms de fonctions intégrées
Si vous utilisez un nom de fonction intégrée comme variable et que vous l'appelez comme une fonction, vous obtiendrez l'erreur « int object is not callable ».

Par exemple, le code ci-dessous tente de calculer le total des âges de certains enfants avec la fonction intégrée `sum()` de Python. Le code a abouti à une erreur car le même `sum` a déjà été utilisé comme nom de variable :
```py
kid_ages = [2, 7, 5, 6, 3]

sum = 0
sum = sum(kid_ages)
print(sum)
```
Un autre exemple ci-dessous montre comment j'ai essayé d'obtenir le plus âgé parmi ces enfants avec la fonction `max()`, mais j'avais déjà déclaré une variable `max` :
```py
kid_ages = [2, 7, 5, 6, 3]

max = 0
max = max(kid_ages)
print(max)
```

Les deux exemples de code ont conduit à cette erreur dans le terminal :
![error](https://www.freecodecamp.org/news/content/images/2022/07/error.png)

Pour corriger le problème, vous devez changer le nom de la variable que vous avez nommée comme une fonction intégrée afin que le code puisse s'exécuter avec succès :
```py
kid_ages = [2, 7, 5, 6, 3]

sum_of_ages = 0
sum = sum(kid_ages)
print(sum)

# Output: 23
```
```py
kid_ages = [2, 7, 5, 6, 3]

max_of_ages = 0
max = max(kid_ages)
print(max)

# Output: 7
```

Si vous supprimez les variables personnalisées, votre code s'exécutera toujours comme prévu :
```py
kid_ages = [2, 7, 5, 6, 3]

sum = sum(kid_ages)
print(sum)

# Output: 23
```

```py
kid_ages = [2, 7, 5, 6, 3]

max = max(kid_ages)
print(max)

# Output: 7
```

## Comment corriger `Typeerror: int object is not callable` dans les calculs mathématiques

En mathématiques, si vous faites quelque chose comme 4(2+3), vous obtiendrez la bonne réponse qui est 20. Mais en Python, cela conduirait à l'erreur `Typeerror: int object is not callable`.
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/07/ss2-2.png)

Pour corriger cette erreur, vous devez indiquer à Python que vous souhaitez multiplier le nombre à l'extérieur des parenthèses par la somme des nombres à l'intérieur des parenthèses. 

Pour ce faire, vous spécifiez un signe de multiplication (*) avant la parenthèse ouvrante :
```py
print(4*(2+3))

#Output: 20
```

Python vous permet de spécifier n'importe quel signe arithmétique avant la parenthèse ouvrante. 

Vous pouvez donc effectuer d'autres calculs là aussi :
```py
print(4+(2+3))

# Output: 9
```
```py
print(4-(2+3))

# Output: -1
```

```py
print(4/(2+3))

# Output: 0.8
```

## Réflexions finales

La `Typeerror: int object is not callable` est une erreur de débutant en Python que vous pouvez éviter de manière simple.

Comme montré dans cet article, vous pouvez éviter l'erreur en n'utilisant pas un nom de fonction intégrée comme identifiant de variable et en spécifiant les signes arithmétiques là où c'est nécessaire.

Merci d'avoir lu.