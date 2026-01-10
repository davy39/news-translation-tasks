---
title: KeyError en Python – Comment corriger l'erreur de dictionnaire
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-07-07T19:33:31.000Z'
originalURL: https://freecodecamp.org/news/keyerror-in-python-how-to-fix-dictionary-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/brett-jordan-XWar9MbNGUY-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: KeyError en Python – Comment corriger l'erreur de dictionnaire
seo_desc: "When working with dictionaries in Python, a KeyError gets raised when you\
  \ try to access an item that doesn't exist in a Python dictionary.\nHere's a Python\
  \ dictionary called student:\nstudent = {\n  \"name\": \"John\",\n  \"course\":\
  \ \"Python\",\n}\n\nIn the dictio..."
---

Lorsque vous travaillez avec des dictionnaires en Python, une erreur KeyError est levée lorsque vous essayez d'accéder à un élément qui n'existe pas dans un dictionnaire Python.

Voici un dictionnaire Python appelé `student` :

```python
student = {
  "name": "John",
  "course": "Python",
}
```

Dans le dictionnaire ci-dessus, vous pouvez accéder au nom "John" en référençant sa clé – `name`. Voici comment :

```python
print(student["name"])
# John
```

Mais lorsque vous essayez d'accéder à une clé qui n'existe pas, vous obtenez une erreur KeyError. C'est-à-dire :

```python
student = {
  "name": "John",
  "course": "Python",
}

print(student["age"])
# ...KeyError: 'age'
```

C'est simple à corriger lorsque vous êtes celui qui écrit/test le code – vous pouvez soit vérifier les erreurs d'orthographe, soit utiliser une clé que vous savez exister dans le dictionnaire.

Mais dans les programmes où vous avez besoin d'une entrée utilisateur pour récupérer un élément particulier d'un dictionnaire, l'utilisateur peut ne pas connaître tous les éléments qui existent dans le dictionnaire.

Dans cet article, vous verrez comment corriger le KeyError dans les dictionnaires Python.

Nous parlerons des méthodes que vous pouvez utiliser pour vérifier si un élément existe dans un dictionnaire avant d'exécuter un programme, et que faire lorsque l'élément ne peut pas être trouvé.

## Comment corriger le KeyError du dictionnaire en Python

Les deux méthodes dont nous allons parler pour corriger l'exception KeyError en Python sont :

* Le mot-clé `in`.
* Le bloc `try except`.

Commençons.

### Comment corriger le KeyError en Python en utilisant le mot-clé `in`

Nous pouvons utiliser le mot-clé `in` pour vérifier si un élément existe dans un dictionnaire.

En utilisant une instruction `if...else`, nous retournons l'élément s'il existe ou retournons un message à l'utilisateur pour les informer que l'élément n'a pas pu être trouvé.

Voici un exemple :

```python
student = {
  "name": "John",
  "course": "Python",
  "age": 20
}

getStudentInfo = input("Quelle information sur l'étudiant voulez-vous ? ")

if getStudentInfo in student:
    print(f"La valeur pour votre demande est {student[getStudentInfo]}")
else:
	print(f"Il n'y a pas de paramètre avec la clé '{getStudentInfo}'. Essayez d'entrer name, course ou age.")
```

Essayons de comprendre le code ci-dessus en le décomposant.

Nous avons d'abord créé un dictionnaire appelé `student` qui avait trois éléments/clés – `name`, `course` et `age` :

```python
student = {
  "name": "John",
  "course": "Python",
  "age": 20
}

```

Ensuite, nous avons créé une fonction `input()` appelée `getStudentInfo` : `getStudentInfo = input("Quelle information sur l'étudiant voulez-vous ? ")`. Nous utiliserons la valeur de la fonction `input()` comme clé pour obtenir des éléments du dictionnaire.

Nous avons ensuite créé une instruction `if...else` pour vérifier si la valeur de la fonction `input()` correspond à une clé dans le dictionnaire :

```python
if getStudentInfo in student:
    print(f"La valeur pour votre demande est {student[getStudentInfo]}")
else:
	print(f"Il n'y a pas de paramètre avec la clé '{getStudentInfo}'. Essayez d'entrer name, course ou age.")
```

D'après l'instruction `if...else` ci-dessus, si la valeur de la fonction `input()` existe en tant qu'élément dans le dictionnaire, `print(f"La valeur pour votre demande est {student[getStudentInfo]}")` s'exécutera. `student[getStudentInfo]` désigne le dictionnaire `student` avec la valeur obtenue de la fonction `input()` agissant comme une clé.

Si la valeur de la fonction `input()` n'existe pas, alors `print(f"Il n'y a pas de paramètre avec la clé '{getStudentInfo}'. Essayez d'entrer name, course ou age.")` s'exécutera, indiquant à l'utilisateur que leur entrée est incorrecte, avec des suggestions des clés possibles qu'ils peuvent utiliser.

Allez-y et exécutez le code – entrez des clés correctes et incorrectes. Cela aidera à valider les explications ci-dessus.

### Comment corriger le KeyError en Python en utilisant un bloc `try except`

Dans un bloc `try except`, le bloc `try` vérifie les erreurs tandis que le bloc `except` gère toute erreur trouvée.

Voyons un exemple.

```python
student = {
  "name": "John",
  "course": "Python",
  "age": 20
}

getStudentInfo = input("Quelle information sur l'étudiant voulez-vous ? ")

try:
    print(f"La valeur pour votre demande est {student[getStudentInfo]}")
except KeyError:
    print(f"Il n'y a pas de paramètre avec la clé '{getStudentInfo}'. Essayez d'entrer name, course ou age.")
```

Tout comme nous l'avons fait dans la dernière section, nous avons créé le dictionnaire et une fonction `input()`.

Nous avons également créé différents messages pour les résultats que nous obtenons de la fonction `input()`.

Si aucune erreur n'est trouvée, seul le code dans le bloc `try` sera exécuté – cela retournera la valeur de la clé à partir de l'entrée de l'utilisateur.

Si une erreur est trouvée, le programme passera au bloc `except` qui indique à l'utilisateur que la clé n'existe pas tout en suggérant des clés possibles à utiliser.

## Résumé

Dans cet article, nous avons parlé du KeyError en Python. Cette erreur est levée lorsque nous essayons d'accéder à un élément qui n'existe pas dans un dictionnaire en Python.

Nous avons vu deux méthodes que nous pouvons utiliser pour corriger le problème.

Nous avons d'abord vu comment nous pouvons utiliser le mot-clé `in` pour vérifier si un élément existe avant d'exécuter le code.

Enfin, nous avons utilisé le bloc `try except` pour créer deux blocs de code – le bloc `try` s'exécute avec succès si l'élément existe tandis que le bloc `except` s'exécute si l'élément n'existe pas.

Bon codage !