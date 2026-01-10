---
title: TypeError String Indices Must be Integers Python Error [Résolu]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-07T23:28:09.000Z'
originalURL: https://freecodecamp.org/news/typeerror-string-indices-must-be-integers-javascript-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pakata-goh-RDolnHtjVCY-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: TypeError String Indices Must be Integers Python Error [Résolu]
seo_desc: 'If you try to access values from a dictionary or iterable object using
  the string value instead of the integer value then you will receive the following
  error message:

  TypeError: string indices must be integers

  In this article, I will show you exampl...'
---

Si vous essayez d'accéder à des valeurs d'un dictionnaire ou d'un objet itérable en utilisant la valeur de chaîne au lieu de la valeur entière, vous recevrez le message d'erreur suivant :

```
TypeError: string indices must be integers
```

Dans cet article, je vais vous montrer des exemples de raisons pour lesquelles vous pourriez recevoir ce message d'erreur et comment le corriger.

## Comment accéder aux valeurs d'une liste en Python

Dans cet exemple, nous avons la liste suivante d'instruments de musique :

```py
instruments = ['flute', 'trumpet', 'oboe', 'percussion', 'guitar']
```

Si nous voulions accéder au troisième instrument de la liste, nous utiliserions la valeur d'index numérique 2 :

```py
instruments[2]
```

La ligne de code suivante afficherait correctement le résultat `oboe` :

```py
instruments = ['flute', 'trumpet', 'oboe', 'percussion', 'guitar']
print(instruments[2])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-11.41.54-PM.png)

Si j'essayais d'accéder à cette même liste mais que j'utilisais l'index de chaîne `'oboe'`, cela entraînerait un message d'erreur :

```py
instruments = ['flute', 'trumpet', 'oboe', 'percussion', 'guitar']
print(instruments['oboe'])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-11.43.28-PM.png)

Si vous rencontrez ce message d'erreur, vérifiez que vous utilisez la valeur d'index numérique pour accéder aux éléments au lieu d'une valeur de chaîne.

## Comment accéder aux valeurs d'un dictionnaire en Python

Modifions notre exemple précédent pour créer un dictionnaire d'instruments et de quantités.

```py
instruments = {
    'flute': 2,
    'trumpet': 5,
    'oboe': 1,
    'percussion': 4,
    'guitar': 9
}
```

Si nous voulions afficher toutes les valeurs de notre dictionnaire `instruments`, nous pourrions utiliser une boucle avec la méthode `.values()`.

```py
for quantity in instruments.values():
    print(quantity)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-06-at-11.59.57-PM.png)

Si nous supprimions la méthode `.values()` et que nous essayions d'accéder aux valeurs en utilisant des indices de chaîne, nous recevrions le message d'erreur suivant :

```py
for quantity in instruments:
    print(quantity['flute'])
    print(quantity['trumpet'])
    print(quantity['oboe'])
    print(quantity['percussion'])
    print(quantity['guitar'])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-07-at-12.15.23-AM.png)

Si vous affichez `quantity`, vous verrez que c'est une chaîne.

```py
for quantity in instruments:
    print(quantity)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-07-at-12.22.50-AM.png)

Si vous essayez d'écrire `quantity['flute']`, cela se traduit par `'flute'['flute']` ce qui n'a pas de sens en Python.

La façon de résoudre cela serait de référencer notre dictionnaire `instruments` au lieu d'utiliser `quantity`.

Le code suivant refactorisé produirait les résultats corrects :

```py
instruments = {
    'flute': 2,
    'trumpet': 5,
    'oboe': 1,
    'percussion': 4,
    'guitar': 9
}

print(instruments['flute'])
print(instruments['trumpet'])
print(instruments['oboe'])
print(instruments['percussion'])
print(instruments['guitar'])
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-07-at-12.19.21-AM.png)

J'espère que vous avez apprécié cet article et bonne chance dans votre parcours Python.