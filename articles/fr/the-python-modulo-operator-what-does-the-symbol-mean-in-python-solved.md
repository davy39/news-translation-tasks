---
title: L'opérateur Modulo en Python - Que signifie le symbole % en Python ? (Résolu)
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-12-29T22:14:00.000Z'
originalURL: https://freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/python-modulo-image.jpg
tags:
- name: Python
  slug: python
seo_title: L'opérateur Modulo en Python - Que signifie le symbole % en Python ? (Résolu)
seo_desc: "When you see the % symbol, you may think \"percent\". But in Python, as\
  \ well as most other programming languages, it means something different. \nThe\
  \ % symbol in Python is called the Modulo Operator. It returns the remainder of\
  \ dividing the left hand op..."
---

Lorsque vous voyez le symbole %, vous pouvez penser "pour cent". Mais en Python, ainsi que dans la plupart des autres langages de programmation, il signifie quelque chose de différent. 

Le symbole `%` en Python est appelé l'opérateur Modulo. Il retourne le reste de la division de l'opérande de gauche par l'opérande de droite. Il est utilisé pour obtenir le reste d'un problème de division.

L'opérateur modulo est considéré comme une opération arithmétique, au même titre que `+`, `-`, `/`, `*`, `**`, `//`.

La syntaxe de base est :

```python
# a est divisé par b, et le reste est retourné
# a est divisé par b, et le reste est retourné
a % b
```

Dans l'exemple précédent, `a` est divisé par `b`, et le reste est retourné. Voyons un exemple avec des nombres.

```python
7 % 2
```

Le résultat de l'exemple précédent est **un**. Deux entre dans sept trois fois et il reste **un**.

Le diagramme ci-dessous montre une représentation visuelle de `7 / 2` et `7 % 2` (le "R" signifie "reste"). Le logo unique sur le côté droit (avec la flèche verte pointant dessus) est le reste du problème de division. C'est aussi la réponse à `7 % 2`.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-196.png)

Voici un autre exemple :

```python
3 % 4
```

Cela donnera **trois**. Quatre n'entre pas dans trois _aucune_ fois, donc le **trois** original reste. Le diagramme ci-dessous montre ce qui se passe. Rappelez-vous, l'opérateur modulo retourne le reste après avoir effectué la division. Le reste est trois.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-197.png)

### Exemple d'utilisation de l'opérateur Modulo

Une utilisation courante de l'opérateur Modulo est de trouver des nombres pairs ou impairs. Le code ci-dessous utilise l'opérateur modulo pour imprimer tous les nombres impairs entre 0 et 10.

```python
# Imprime tous les nombres impairs entre 1 et 9
for number in range(1, 10):
    if(number % 2 != 0):
        print(number)
```

Résultat :

```
1
3
5
7
9
```