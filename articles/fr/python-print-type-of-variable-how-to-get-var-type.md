---
title: "Python : Afficher le type d'une variable – Comment obtenir le type d'une variable"
date: 2024-10-18T11:20:41.093Z
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://www.freecodecamp.org/news/python-print-type-of-variable-how-to-get-var-type/
posteditor: ""
proofreader: ""
---

Si vous débutez en Python, vous familiariser avec tous ses différents types de données peut être déroutant au début. Après tout, le langage en met beaucoup à votre disposition.

<!-- more -->

Dans cet article, je vais vous montrer comment obtenir le type de diverses structures de données en Python en les assignant à une variable, puis en affichant le type dans la console avec la fonction `print()`.

## Comment afficher le type d'une variable en Python

Pour obtenir le type d'une variable en Python, vous pouvez utiliser la fonction intégrée `type()`.

La syntaxe de base ressemble à ceci :

```
type(variableName)
```

En Python, tout est un objet. Ainsi, lorsque vous utilisez la fonction `type()` pour afficher le type de la valeur stockée dans une variable dans la console, elle renvoie le type de classe de l'objet.

Par exemple, si le type est une chaîne de caractères et que vous utilisez `type()` dessus, vous obtiendrez `<class 'str'>` comme résultat.

Pour vous montrer la fonction `type()` en action, je vais déclarer quelques variables et leur assigner les différents types de données en Python.

```
name = "freeCodeCamp"

score = 99.99

lessons =  ["RWD", "JavaScript", "Databases", "Python"]

person = {
    "firstName": "John",
    "lastName": "Doe",
    "age": 28
}

langs = ("Python", "JavaScript", "Golang")

basics = {"HTML", "CSS", "JavaScript"}
```

Je vais ensuite afficher les types dans la console en enveloppant quelques chaînes de caractères et la fonction `type()` avec `print()`.

```
print("The variable, name is of type:", type(name))
print("The variable, score is of type:", type(score))
print("The variable, lessons is of type:", type(lessons))
print("The variable, person is of type:", type(person))
print("The variable, langs is of type:", type(langs))
print("The variable, basics is of type:", type(basics))
```

**Voici les sorties :**

```
# Outputs:
# The variable, name is of type:  <class 'str'>
# The variable, score is of type: <class 'float'>  
# The variable, lessons is of type:  <class 'list'>
# {The variable, person is of type:  <class 'dict'> 
# The variable, langs is of type:  <class 'tuple'> 
# The variable, basics is of type:  <class 'set'>
```

## Conclusion

La fonction `type()` est une fonction intégrée précieuse de Python avec laquelle vous pouvez obtenir le type de données d'une variable.

Si vous êtes débutant, vous devriez vous épargner la peine de mémoriser les types de données en utilisant la fonction `type()` pour afficher le type d'une variable dans la console. Cela vous fera gagner du temps.

Vous pouvez également utiliser la fonction `type()` pour le débogage car, en Python, les variables ne sont pas déclarées avec des types de données. Ainsi, la fonction `type()` a été intégrée au langage pour vous permettre de vérifier les types de données des variables.

Merci de votre lecture.
