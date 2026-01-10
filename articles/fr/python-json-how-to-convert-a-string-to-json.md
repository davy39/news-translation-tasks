---
title: Python JSON – Comment convertir une chaîne de caractères en JSON
date: '2021-11-09T16:38:47.000Z'
author: Dionysia Lemonaki
authorURL: https://www.freecodecamp.org/news/author/dionysialemonaki/
originalURL: https://freecodecamp.org/news/python-json-how-to-convert-a-string-to-json
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/nordwood-themes-bJjsKbToY34-unsplash.jpg
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_desc: "In this tutorial you'll learn the basics of JSON – what it is, where it\
  \ is most commonly used, and its syntax.\nYou'll also see how to convert a string\
  \ to JSON in Python.\nLet's get started!\nWhat is JSON?\nJSON stands for JavaScript\
  \ Object Notation. \nIt..."
---


Dans ce tutoriel, vous apprendrez les bases du JSON – ce que c'est, où il est le plus couramment utilisé et sa syntaxe.

<!-- more -->

Vous verrez également comment convertir une chaîne de caractères en JSON en Python.

Commençons !

## Qu'est-ce que le JSON ?

JSON signifie JavaScript Object Notation.

C'est un format de données utilisé pour stocker et transférer des informations pour les applications web.

Le JSON a été inspiré par le langage de programmation JavaScript, mais il n'est pas lié à un seul langage.

La plupart des langages de programmation modernes disposent de bibliothèques pour analyser et générer des données JSON.

### Où le JSON est-il utilisé ?

Le JSON est principalement utilisé pour envoyer et recevoir des données entre un serveur et un client, où le client est une page web ou une application web.

C'est un format beaucoup plus robuste à utiliser pendant le cycle requête-réponse que les applications web utilisent lors de la connexion via un réseau. Cela se compare au format XML, plus complexe et moins compact, qui était le format de prédilection il y a quelques années.

### Syntaxe JSON de base

En JSON, les données sont écrites sous forme de paires clé-valeur, comme ceci :

```
"first_name": "Katie"
```

Les données sont entourées de guillemets doubles et la paire clé-valeur est séparée par deux-points.

Il peut y avoir plus d'une paire clé-valeur et chacune est séparée par une virgule :

```
"first_name": "Katie", "last_name": "Rodgers"
```

L'exemple ci-dessus montrait un _objet_, une collection de plusieurs paires clé-valeur.

Les objets sont à l'intérieur d'accolades :

```
{
    "first_name": "Katie",  
    "last_name": "Rodgers"
}
```

Vous pouvez également créer des tableaux (arrays), une liste ordonnée de valeurs, avec JSON. Dans ce cas, les tableaux sont contenus à l'intérieur de crochets :

```
[
  { 

    "first_name": "Katie",  
    "last_name": "Rodgers"
  },

  { 

    "first_name": "Naomi",  
    "last_name": "Green"
  },
]

// or:


{
 "employee": [
     { 
    "first_name": "Katie",  
    "last_name": "Rodgers"
  },

  { 
    "first_name": "Naomi",  
    "last_name": "Green"
  },
 ]
}

//this created an 'employee' object that has 2 records.
// It defines the first name and last name of an employee
```

## Comment travailler avec des données JSON en Python

### Inclure le module JSON pour Python

Pour utiliser JSON avec Python, vous devrez d'abord inclure le module `json` en haut de votre fichier Python. Celui-ci est intégré à Python et fait partie de la bibliothèque standard.

Ainsi, supposons que vous ayez un fichier nommé `demo.py`. En haut, vous ajouteriez la ligne suivante :

```
import json
```

### Utiliser la fonction `json.loads()`

Si vous avez des données sous forme de chaîne JSON dans votre programme comme ceci :

```
#include json library
import json

#json string data
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

#check data type with type() method
print(type(employee_string))

#output
#<class 'str'>
```

vous pouvez les transformer en JSON en Python en utilisant la fonction `json.loads()`.

La fonction `json.loads()` accepte en entrée une chaîne de caractères valide et la convertit en un dictionnaire Python.

Ce processus est appelé _désérialisation_ – l'action de convertir une chaîne de caractères en un objet.

```
#include json library
import json

#json string data
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

#check data type with type() method
print(type(employee_string))

#convert string to  object
json_object = json.loads(employee_string)

#check new data type
print(type(json_object))

#output
#<class 'dict'>
```

Vous pouvez ensuite accéder à chaque élément individuellement, comme vous le feriez en utilisant un dictionnaire Python :

```
#include json library
import json

#json string data
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

#check data type with type() method
print(type(employee_string))

#convert string to  object
json_object = json.loads(employee_string)

#check new data type
print(type(json_object))

#output
#<class 'dict'>

#access first_name in dictionary
print(json_object["first_name"])

#output
#Michael
```

Prenons un autre exemple :

1) Prenez des données de chaîne JSON :

```
import json

#json string
employees_string = '''
{
    "employees": [
       {
           "first_name": "Michael", 
           "last_name": "Rodgers", 
           "department": "Marketing"
        },
       {
           "first_name": "Michelle", 
           "last_name": "Williams", 
           "department": "Engineering"
        }
    ]
}
'''

#check data type using the type() method
print(type(employees_string))

#output
#<class 'str'>
```

2) Utilisez la fonction `json.loads()` pour convertir une chaîne en un objet :

```
import json

emoloyees_string = '''
{
    "employees" : [
       {
           "first_name": "Michael", 
           "last_name": "Rodgers", 
           "department": "Marketing"
        },
       {
           "first_name": "Michelle", 
           "last_name": "Williams", 
           "department": "Engineering"
        }
    ]
}
'''

data = json.loads(employees_string)

print(type(data))
#output
#<class 'dict'>
```

3) Accédez aux données :

```
import json

employees_string = '''
{
    "employees" : [
       {
           "first_name": "Michael", 
           "last_name": "Rodgers", 
           "department": "Marketing"

        },
       {
           "first_name": "Michelle", 
           "last_name": "Williams", 
           "department": "Engineering"
        }
    ]
}
'''

data = json.loads(employees_string)

print(type(data))
#output
#<class 'dict'>

#access first_name
for employee in data["employees"]: 
    print(employee["first_name"])

#output
#Michael
#Michelle
```

## Conclusion

Et voilà – vous connaissez maintenant les bases de l'utilisation du JSON en Python.

Si vous voulez en savoir plus sur Python, freeCodeCamp propose une [Certification Python][1] qui vous emmène des fondamentaux tels que les variables, les boucles et les fonctions vers des concepts plus avancés comme les structures de données. À la fin, vous construirez également 5 projets.

Merci de votre lecture et bon apprentissage !

[1]: https://www.freecodecamp.org/learn/scientific-computing-with-python/