---
title: Comment faire une temporisation en Python avec la fonction sleep()
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-08T20:07:00.000Z'
originalURL: https://freecodecamp.org/news/time-delay-python-sleep-function
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e0d740569d1a4ca3b11.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Comment faire une temporisation en Python avec la fonction sleep()
seo_desc: 'There are times when you want your program to run immediately. But there
  are also some times when you want to delay the execution of certain pieces of code.

  That''s where Python''s time module comes in. time is part of Python''s standard
  library, and co...'
---

Il arrive que vous souhaitiez que votre programme s'exécute immédiatement. Mais il arrive aussi que vous souhaitiez retarder l'exécution de certaines parties du code.

C'est là qu'intervient le module `time` de Python. `time` fait partie de la bibliothèque standard de Python et contient la fonction utile `sleep()` qui suspend ou met en pause un programme pendant un nombre donné de secondes :

```text
import time

print('s'exécute immédiatement')

for letter in 'bonjour, monde !':
    time.sleep(2)  # pause de 2 secondes entre chaque print
    print(letter)
```

**Sortie :**

```
s'exécute immédiatement
b # chaque caractère imprimé après un délai de deux secondes
o
n
j
o
u
r
,

m
o
n
d
e

!
```

Des nombres à virgule flottante peuvent être donnés comme argument à `sleep()` pour des temps de pause plus précis. Par exemple, le code suivant retardera chaque instruction `print()` d'une demi-seconde, soit 500 ms :

```py
import time

for letter in 'les flottants marchent aussi':
  time.sleep(0.5) # ajoute un délai de 500 ms
  print(letter)
```

**Sortie :**

```
l # chaque caractère imprimé après un délai de 500 ms
e
s

f
l
o
t
t
a
n
t
s

m
a
r
c
h
e
n
t

a
u
s
s
i
```

Parfois, vous pourriez avoir besoin de retarder pour des incréments de temps connus et différents. Dans ce cas, vous pouvez parcourir une liste de différentes périodes de délai avec une boucle `for` :

```py
import time

for i in [.5, 1, 2, 3, 4]:
  time.sleep(i)
  print(f"Délai de {i} secondes")
```

**Sortie :**

```
Délai de 0.5 secondes
Délai de 1 secondes
Délai de 2 secondes
Délai de 3 secondes
Délai de 4 secondes
```

Comme vous pouvez l'imaginer, il y a beaucoup de choses que vous pouvez faire avec la fonction `sleep()`. Alors allez-y et essayez-la dans vos propres programmes – pas besoin de dormir dessus !

#### **Plus d'informations :**

Documentation du module [time](https://docs.python.org/3/library/time.html#time.sleep) sur la fonction sleep.

## Plus de tutoriels Python :

[Les meilleurs tutoriels Python](https://www.freecodecamp.org/news/best-python-tutorial/)

[Les meilleurs exemples de code Python](https://www.freecodecamp.org/news/python-example/)

[Python pour tous par Dr. Chuck](https://www.freecodecamp.org/news/python-for-everybody/)