---
title: Attributs Python – Exemples d'attributs de classe et d'instance
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-12T02:17:19.000Z'
originalURL: https://freecodecamp.org/news/python-attributes-class-and-instance-attribute-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pyAttributes.jpg
tags:
- name: Python
  slug: python
seo_title: Attributs Python – Exemples d'attributs de classe et d'instance
seo_desc: 'When creating a class in Python, you''ll usually create attributes that
  may be shared across every object of a class or attributes that will be unique to
  each object of the class.

  In this article, we''ll see the difference between class attributes and ...'
---

Lorsque vous créez une `class` en Python, vous créerez généralement des attributs qui peuvent être partagés entre tous les objets d'une classe ou des attributs qui seront uniques à chaque objet de la classe.

Dans cet article, nous verrons la différence entre les attributs de classe et les attributs d'instance en Python avec des exemples.

Avant cela, voyons comment créer une classe en Python.

## Comment créer une classe en Python

Pour créer une classe en Python, nous utilisons le mot-clé `class` suivi du nom de la classe. Voici un exemple :

```python
class Student:
    name = "Jane"
    course = "JavaScript"
```

Dans le code ci-dessus, nous avons créé une classe appelée `Student` avec une propriété `name` et `course`. Maintenant, créons de nouveaux objets à partir de cette classe.

```python
class Student:
    name = "Jane"
    course = "JavaScript"
    
Student1 = Student()

print(Student1.name)
# Jane
```

Nous avons créé un nouvel objet appelé `Student1` à partir de la classe `Student`.

Lorsque nous avons imprimé `Student1.name`, nous avons obtenu "Jane" affiché dans la console. Rappelez-vous que la valeur de Jane était stockée dans une variable dans la classe originale créée.

Ces variables `name` et `course` sont en fait des attributs de classe. Nous verrons plus d'exemples dans la section suivante pour vous aider à mieux comprendre.

## Attributs de classe et d'instance en Python

Pour donner une définition de base des deux termes, les **attributs de classe** sont des variables de classe qui sont héritées par chaque objet d'une classe. La valeur des attributs de classe reste la même pour chaque nouvel objet.

Comme vous le verrez dans les exemples de cette section, les attributs de classe sont définis en dehors de la fonction `__init__()`.

D'autre part, les **attributs d'instance**, qui sont définis dans la fonction `__init__()`, sont des variables de classe qui nous permettent de définir différentes valeurs pour chaque objet d'une classe.

Voici un exemple :

```python
class Student:
    school = "freeCodeCamp.org"
    
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John

```

Dans le code ci-dessus, nous avons créé une variable dans la classe `Student` appelée `school`.

Nous avons créé deux autres variables mais dans la fonction `__init__()` – `name` et `course` – que nous avons initialisées en utilisant le paramètre `self`.

Le premier paramètre dans une fonction `__init__()` est utilisé pour initialiser d'autres paramètres lors de la création de variables dans la fonction. Vous pouvez l'appeler comme vous voulez – par convention, `self` est principalement utilisé.

La variable `school` agit comme un attribut de classe tandis que `name` et `course` sont des attributs d'instance. Décomposons l'exemple ci-dessus pour expliquer les attributs d'instance.

```python
Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John
```

Nous avons créé deux objets à partir de la classe `Student` – `Student1` et `Student2`. Chacun de ces objets, par défaut, aura toutes les variables créées dans la classe. Mais chaque objet est capable d'avoir sa propre variable `name` et `course` parce qu'elles ont été créées dans la fonction `__init__()`.

Maintenant, imprimons la variable `school` pour chaque objet et voyons ce qui se passe.

```python
print(Student1.school) # freeCodeCamp.org
print(Student2.school) # freeCodeCamp.org
```

Les deux nous ont donné la même valeur parce que la variable `school` est un attribut de classe.

## Conclusion

Dans cet article, nous avons vu comment créer une classe en Python et les différences entre les attributs de classe et d'instance.

En résumé, les **attributs de classe** restent les mêmes pour chaque objet et sont définis en dehors de la fonction `__init__()`. Les **attributs d'instance** sont quelque peu dynamiques car ils peuvent avoir différentes valeurs dans chaque objet.

Les **attributs d'instance** sont définis dans la fonction `__init__()`.

Bon codage !