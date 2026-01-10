---
title: Variables Globales en Python – Comment Définir une Variable Globale Exemple
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-05-12T18:46:34.000Z'
originalURL: https://freecodecamp.org/news/python-global-variables-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/fernando-cferdophotography-tNDYN8jWyfM-unsplash.jpg
tags:
- name: Python
  slug: python
- name: variables
  slug: variables
seo_title: Variables Globales en Python – Comment Définir une Variable Globale Exemple
seo_desc: 'In this article, you will learn the basics of global variables.

  To begin with, you will learn how to declare variables in Python and what the term
  ''variable scope'' actually means.

  Then, you will learn the differences between local and global variable...'
---

Dans cet article, vous apprendrez les bases des variables globales.

Pour commencer, vous apprendrez comment déclarer des variables en Python et ce que le terme 'portée des variables' signifie réellement.

Ensuite, vous apprendrez les différences entre les variables locales et globales et comprendrez comment définir des variables globales et comment utiliser le mot-clé `global`.

Voici ce que nous allons couvrir :

1. [Une introduction aux variables en Python](#introduction)
    1. [Portée des variables expliquée](#portee)
2. [Comment créer des variables avec une portée locale](#locale)
3. [Comment créer des variables avec une portée globale](#globale)
    1. [Le mot-clé `global`](#mot-cle)

## Que sont les Variables en Python et Comment les Créer ? Une Introduction pour Débutants <a name="introduction"></a>

Vous pouvez penser aux variables comme des **conteneurs de stockage**.

Ce sont des conteneurs de stockage pour contenir des données, des informations et des valeurs que vous souhaitez enregistrer dans la mémoire de l'ordinateur. Vous pouvez ensuite les référencer ou même les manipuler à un moment donné tout au long de la vie du programme.

Une variable a un nom **symbolique**, et vous pouvez penser à ce nom comme à l'**étiquette** sur le conteneur de stockage qui agit comme son identifiant.

Le nom de la variable sera une référence et un pointeur vers les données stockées à l'intérieur. Ainsi, il n'est pas nécessaire de se souvenir des détails de vos données et informations – vous devez simplement référencer le nom de la variable qui contient ces données et informations.

Lorsqu'on donne un nom à une variable, assurez-vous qu'il est descriptif des données qu'elle contient. Les noms de variables doivent être clairs et facilement compréhensibles à la fois pour vous-même à l'avenir et pour les autres développeurs avec lesquels vous pourriez travailler.

Maintenant, voyons comment créer réellement une variable en Python.

Lors de la déclaration de variables en Python, vous n'avez pas besoin de spécifier leur type de données.

Par exemple, dans le langage de programmation C, vous devez mentionner explicitement le type de données que la variable contiendra.

Ainsi, si vous vouliez stocker votre âge qui est un entier, ou de type `int`, voici ce que vous devriez faire en C :

```c
#include <stdio.h>
 
int main(void)
{
  int age = 28;
  // 'int' est le type de données
  // 'age' est le nom 
  // 'age' est capable de contenir des valeurs entières
  // nombres entiers positifs/négatifs ou 0
  // '=' est l'opérateur d'affectation
  // '28' est la valeur
}
```

Cependant, voici comment vous écriviez ce qui précède en Python :

```python
age = 28

#'age' est le nom de la variable, ou identifiant
# '=' est l'opérateur d'affectation
#'28' est la valeur assignée à la variable, donc '28' est la valeur de 'age'
```
Le nom de la variable est toujours du côté gauche, et la valeur que vous souhaitez assigner va du côté droit après l'opérateur d'affectation.
    
Gardez à l'esprit que vous pouvez changer les valeurs des variables tout au long de la vie d'un programme :

```python
my_age = 28

print(f"Mon âge en 2022 est {my_age}.")

my_age = 29

print(f"Mon âge en 2023 sera {my_age}.")

#output

#Mon âge en 2022 est 28.
#Mon âge en 2023 sera 29.
```

Vous gardez le même nom de variable, `my_age`, mais vous ne changez que la valeur de `28` à `29`.

### Que Signifie la Portée des Variables en Python ? <a name="portee"></a>

La portée des variables fait référence aux parties et aux limites d'un programme Python où une variable est disponible, accessible et visible.

Il existe quatre types de portée pour les variables Python, également connus sous le nom de **règle LEGB** :

- **L**ocale,
- **E**nclosing,
- **G**lobale,
- **B**uilt-in.

Pour le reste de cet article, vous vous concentrerez sur l'apprentissage de la création de variables avec une portée globale, et vous comprendrez la différence entre les portées des variables locales et globales.

## Comment Créer des Variables avec une Portée Locale en Python <a name="locale"></a>

Les variables définies à l'intérieur du corps d'une fonction ont une *portée locale*, ce qui signifie qu'elles sont accessibles uniquement au sein de cette fonction particulière. En d'autres termes, elles sont 'locales' à cette fonction.

Vous ne pouvez accéder à une variable locale qu'en appelant la fonction.

```python
def learn_to_code():
    #créer une variable locale
    coding_website = "freeCodeCamp"
    print(f"Le meilleur endroit pour apprendre à coder est avec {coding_website} !")

#appeler la fonction
learn_to_code()


#output

#Le meilleur endroit pour apprendre à coder est avec freeCodeCamp!
```

Regardez ce qui se passe lorsque j'essaie d'accéder à cette variable avec une portée locale depuis l'extérieur du corps de la fonction :

```python
def learn_to_code():
    #créer une variable locale
    coding_website = "freeCodeCamp"
    print(f"Le meilleur endroit pour apprendre à coder est avec {coding_website} !")

#essayer d'imprimer la variable locale 'coding_website' depuis l'extérieur de la fonction
print(coding_website)

#output

#NameError: name 'coding_website' is not defined
```

Cela lève une `NameError` car elle n'est pas 'visible' dans le reste du programme. Elle est seulement 'visible' au sein de la fonction où elle a été définie.

## Comment Créer des Variables avec une Portée Globale en Python <a name="globale"></a>

Lorsque vous définissez une variable *à l'extérieur* d'une fonction, comme en haut du fichier, elle a une portée globale et elle est connue comme une variable globale.

Une variable globale est accessible depuis n'importe quel endroit dans le programme.

Vous pouvez l'utiliser à l'intérieur du corps d'une fonction, ainsi que l'accéder depuis l'extérieur d'une fonction :

```python
#créer une variable globale
coding_website = "freeCodeCamp"

def learn_to_code():
    #accéder à la variable 'coding_website' à l'intérieur de la fonction
    print(f"Le meilleur endroit pour apprendre à coder est avec {coding_website} !")

#appeler la fonction
learn_to_code()

#accéder à la variable 'coding_website' depuis l'extérieur de la fonction
print(coding_website)

#output

#Le meilleur endroit pour apprendre à coder est avec freeCodeCamp!
#freeCodeCamp
```

Que se passe-t-il lorsqu'il y a une variable globale et une variable locale, et qu'elles ont toutes les deux le même nom ?

```python
#variable globale
city = "Athens"

def travel_plans():
    #variable locale avec le même nom que la variable globale
    city = "London"
    print(f"Je veux visiter {city} l'année prochaine !")

#appeler la fonction - cela affichera la valeur de la variable locale
travel_plans()

#référencer la variable globale - cela affichera la valeur de la variable globale
print(f"Je veux visiter {city} l'année prochaine !")

#output

#Je veux visiter London l'année prochaine!
#Je veux visiter Athens l'année prochaine!
```

Dans l'exemple ci-dessus, peut-être que vous ne vous attendiez pas à cette sortie spécifique.

Peut-être pensiez-vous que la valeur de `city` changerait lorsque je lui ai assigné une valeur différente à l'intérieur de la fonction.

Peut-être vous attendiez-vous à ce que lorsque j'ai référencé la variable globale avec la ligne `print(f"Je veux visiter {city} l'année prochaine!")`, la sortie serait `#Je veux visiter London l'année prochaine!` au lieu de `#Je veux visiter Athens l'année prochaine!`.

Cependant, lorsque la fonction a été appelée, elle a imprimé la valeur de la variable locale.

Ensuite, lorsque j'ai référencé la variable globale à l'extérieur de la fonction, la valeur assignée à la variable globale a été imprimée.

Elles n'ont pas interféré l'une avec l'autre.

Cela dit, utiliser le même nom de variable pour les variables globales et locales n'est pas considéré comme une bonne pratique. Assurez-vous que vos variables n'ont pas le même nom, car vous pourriez obtenir des résultats confus lorsque vous exécutez votre programme.

### Comment Utiliser le Mot-Clé `global` en Python <a name="mot-cle"></a>

Que se passe-t-il si vous avez une variable globale mais que vous souhaitez changer sa valeur à l'intérieur d'une fonction ?

Regardez ce qui se passe lorsque j'essaie de faire cela :

```python
#variable globale
city = "Athens"

def travel_plans():
    #Tout d'abord, c'est comme lorsque j'ai essayé d'accéder à la variable globale définie à l'extérieur de la fonction.
    # Cela fonctionne bien seul, comme vous l'avez vu précédemment.
    print(f"Je veux visiter {city} l'année prochaine !")

    #Cependant, lorsque j'essaie ensuite de réassigner une valeur différente à la variable globale 'city' depuis l'intérieur de la fonction,
    #après avoir essayé de l'imprimer,
    #cela lèvera une erreur
    city = "London"
    print(f"Je veux visiter {city} l'année prochaine !")

#appeler la fonction
travel_plans()

#output

#UnboundLocalError: local variable 'city' referenced before assignment
```

Par défaut, Python pense que vous voulez utiliser une variable locale à l'intérieur d'une fonction.

Ainsi, lorsque j'essaie d'abord d'imprimer la valeur de la variable et *ensuite* de réassigner une valeur à la variable à laquelle j'essaie d'accéder, Python est confus.

La façon de changer la valeur d'une variable globale à l'intérieur d'une fonction est d'utiliser le mot-clé `global` :

```python
#variable globale
city = "Athens"

#imprimer la valeur de la variable globale
print(f"Je veux visiter {city} l'année prochaine !")

def travel_plans():
    global city
    #imprimer la valeur initiale de la variable globale
    print(f"Je veux visiter {city} l'année prochaine !")
    #assigner une valeur différente à la variable globale depuis l'intérieur de la fonction
    city = "London"
    #imprimer la nouvelle valeur
    print(f"Je veux visiter {city} l'année prochaine !")

#appeler la fonction
travel_plans()

#imprimer la valeur de la variable globale
print(f"Je veux visiter {city} l'année prochaine !")
```

Utilisez le mot-clé `global` avant de le référencer dans la fonction, sinon vous obtiendrez l'erreur suivante : `SyntaxError: name 'city' is used prior to global declaration`.

Plus tôt, vous avez vu que vous ne pouviez pas accéder aux variables créées à l'intérieur des fonctions puisqu'elles ont une portée locale.

Le mot-clé `global` change la visibilité des variables déclarées à l'intérieur des fonctions.

```python
def learn_to_code():
   global coding_website
   coding_website = "freeCodeCamp"
   print(f"Le meilleur endroit pour apprendre à coder est avec {coding_website} !")

#appeler la fonction
learn_to_code()

#accéder à la variable depuis l'intérieur de la fonction
print(coding_website)

#output

#Le meilleur endroit pour apprendre à coder est avec freeCodeCamp!
#freeCodeCamp
```

## Conclusion

Et voilà ! Vous connaissez maintenant les bases des variables globales en Python et pouvez distinguer les différences entre les variables locales et globales.

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !