---
title: Python Break et Python Continue – Comment passer à l'itération suivante
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-14T13:55:01.000Z'
originalURL: https://freecodecamp.org/news/python-break-and-python-continue-how-to-skip-to-the-next-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/thisisengineering-raeng-uyfohHiTxho-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python Break et Python Continue – Comment passer à l'itération suivante
seo_desc: 'If you ever need to skip part of the current loop you are in or break out
  of the loop completely, then you can use the break and continue statements.

  In this article, I will cover how to use the break and continue statements in your
  Python code.

  How ...'
---

Si vous avez un jour besoin de sauter une partie de la boucle actuelle dans laquelle vous vous trouvez ou de sortir complètement de la boucle, vous pouvez utiliser les instructions `break` et `continue`.

Dans cet article, je vais expliquer comment utiliser les instructions `break` et `continue` dans votre code Python.

## Comment utiliser l'instruction break en Python

Vous pouvez utiliser l'instruction `break` si vous devez sortir d'une boucle `for` ou `while` et passer à la section de code suivante.

Dans ce premier exemple, nous avons une boucle `for` qui parcourt chaque lettre de freeCodeCamp.

```py
for letter in 'freeCodeCamp':
    print('lettre :', letter)
```

Voici ce qui est affiché dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.46.39-PM.png)

Si nous voulions arrêter notre boucle à la lettre « o », nous pouvons utiliser une instruction `if` suivie d'une instruction `break`.

```py
for letter in 'freeCodeCamp':
    if letter == "o":
        break
    print('lettre :', letter)
```

Voici ce qui est affiché dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.49.15-PM.png)

Dans l'exemple suivant, nous utilisons une boucle `while` pour incrémenter `num` tant que `num` est inférieur à 20.

```py
num = 5
while num < 20:
    print('Nombre actuel :', num)
    num = num + 1
```

Voici ce qui est affiché dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.54.17-PM.png)

Nous pourrions ajouter une condition à l'intérieur de notre boucle `while` indiquant que si `num` vaut 9, alors on sort de la boucle.

```py
num = 5
while num < 20:
    print('Nombre actuel :', num)
    num = num + 1
    if num == 9:
        break
```

Voici ce qui est affiché dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-7.55.38-PM.png)

## Comment utiliser l'instruction continue en Python

Vous pouvez utiliser l'instruction `continue` si vous devez ignorer l'itération actuelle d'une boucle `for` ou `while` et passer à l'itération suivante.

Dans cet exemple, nous bouclons sur une chaîne de caractères contenant mon nom.

```py
for letter in "Jessica":
```

À l'intérieur de la boucle `for`, nous avons une condition qui dit que si la lettre est « i », alors on ignore cette itération et on passe à la suivante.

```py
  if letter == "i":
        continue
```

Voici à quoi ressemble le code complet :

```py
for letter in "Jessica":
    if letter == "i":
        continue
    print(letter)
```

Voici ce qui est affiché dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-9.22.33-PM.png)

Vous devriez remarquer que la lettre « i » n'a pas été affichée dans la console et que l'instruction `continue` a sauté cette itération.

Dans l'exemple suivant, nous allons afficher des nombres par incréments de 10 à l'aide d'une boucle `while`. Nous allons ajouter une condition dans la boucle qui dit que si le nombre est 50, alors on ignore cette itération et on passe à la suivante.

```py
num = 10
while num < 100:
    num = num + 10
    if num == 50:
        continue
    print("Nombre actuel : ", num)
```

Voici ce qui est affiché dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-13-at-9.35.33-PM.png)

Comme vous pouvez le voir, le nombre 50 n'est pas affiché dans la console à cause de l'instruction `continue` à l'intérieur du bloc `if`.

## Conclusion

Les instructions `break` et `continue` en Python sont utilisées pour ignorer des parties de la boucle actuelle ou pour sortir complètement de la boucle.

L'instruction `break` peut être utilisée si vous devez sortir d'une boucle `for` ou `while` et passer à la section de code suivante.

L'instruction `continue` peut être utilisée si vous devez ignorer l'itération actuelle d'une boucle `for` ou `while` et passer à l'itération suivante.

J'espère que vous avez apprécié cet article et je vous souhaite bonne chance dans votre apprentissage de Python.