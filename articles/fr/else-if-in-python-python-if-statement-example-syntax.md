---
title: Else-If en Python – Syntaxe et exemples de l'instruction If en Python
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-22T20:41:35.000Z'
originalURL: https://freecodecamp.org/news/else-if-in-python-python-if-statement-example-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Copy-of-pip--4-.png
tags:
- name: Python
  slug: python
seo_title: Else-If en Python – Syntaxe et exemples de l'instruction If en Python
seo_desc: "When you're coding, you need to be able to check certain conditions and\
  \ change the control of the program execution accordingly. \nPython provides many\
  \ conditional statements for decision making, and if-else is one of them.\nIn this\
  \ blog post, we will ..."
---

Lorsque vous codez, vous devez être capable de vérifier certaines conditions et de modifier le contrôle de l'exécution du programme en conséquence. 

Python propose de nombreuses instructions conditionnelles pour la prise de décision, et `if-else` est l'une d'entre elles.

Dans cet article de blog, nous allons apprendre :

1. L'ordre d'exécution par défaut des instructions et comment nous pouvons le modifier.
2. Ce qu'est l'instruction `if-else` et sa syntaxe.
3. Comment gérer plusieurs conditions en utilisant `elif`.
4. Un exemple pratique d' `if-else` où nous écrirons un programme pour vérifier si un nombre est pair ou impair.

## Ordre séquentiel vs structure de contrôle en Python

Par défaut, l'exécution des instructions est séquentielle. L'**ordre séquentiel** signifie que les instructions sont exécutées l'une après l'autre dans l'ordre où elles sont écrites.

Voyons un exemple d'exécution séquentielle ci-dessous en calculant le taux horaire d'un travailleur :

```python
# Écrire un programme pour calculer le taux total

hours = input("entrez les heures : ")
rateperhr = 10
print("Votre taux total est", int(hours)*rateperhr)


```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-95.png)

Et si nous devions vérifier si le nombre d'heures dépasse 8 heures par jour et entre dans la limite des heures supplémentaires ? 

Ici, nous devons vérifier une condition et prendre la décision en conséquence. C'est là que les **structures de contrôle** interviennent. Une structure de contrôle redirige l'ordre d'exécution des instructions dans un programme.

En Python, nous pouvons utiliser les instructions `if`, `if-else`, `if-elif-else`, ou `switch` pour contrôler l'exécution du programme. Les boucles sont un autre moyen de contrôler le flux d'exécution. Dans ce blog, nous nous concentrerons principalement sur if-else et ses dérivés.

## Introduction à l'instruction if en Python

L'instruction `if` s'exécute sur la base d'une certaine condition si celle-ci est `true` (vraie). Si la condition est fausse, alors les instructions à l'extérieur du bloc `if` sont exécutées.

### Syntaxe de l'instruction `if` en Python :

```python
if <expression>:
    <statement>
```

Notez que le corps du bloc `if` est la séquence d'instructions indentée. Les deux points à la fin de l' `<expression>` indiquent le début de l'instruction `if`.

![Flux de l'instruction if](https://www.freecodecamp.org/news/content/images/2022/03/image-88.png)
_Flux de l'instruction `if`_

**Exemple :**

```python
if 10<20:
  print("Vrai, instruction à l'intérieur du 'if'")
  print("Toujours à l'intérieur du if")

print("Instruction à l'extérieur du 'if'")
```

**Sortie :**

![Exemple de l'instruction if](https://www.freecodecamp.org/news/content/images/2022/03/image-87.png)
_Exemple de l'instruction if_

### Instruction if-else en Python

Et si nous voulons faire quelque chose au cas où l'instruction `if` est fausse ? Nous pouvons le faire en ajoutant un bloc `else` supplémentaire.

Syntaxe de `if-else` :

```python
if <expression>:
    <statement>
    <statement>
else:
    <statement>
    <statement>
```

Dans l'instruction `if-else`, nous avons deux branches selon que l'instruction est vraie ou fausse. Le bloc `if` est exécuté si l'expression est vraie. Le bloc `else` est exécuté si l'expression est fausse. Vous voyez comment nous modifions la séquence d'exécution ? C'est possible grâce aux structures de contrôle.

## Flux de l'instruction if-else en Python

Nous pouvons résumer le flux des instructions `if-else` dans le diagramme suivant.

Tout d'abord, l'expression est évaluée. Si l'expression est vraie, les instructions à l'intérieur du `if` sont exécutées et le bloc `else` est ignoré. Si l'expression est fausse, c'est l'instruction du bloc `else` qui s'exécute.

![diagramme de flux if-else](https://www.freecodecamp.org/news/content/images/2022/03/image-89.png)
_diagramme de flux if-else_

### Exemple d'if-else en Python :

Comparons deux nombres pour trouver le plus grand.

```python
a = input("entrez un nombre : ")
b = input("entrez un autre nombre : ")

if a>b:
  print("Le premier nombre est le plus grand")
else:
  print("Le deuxième nombre est le plus grand")
```

**Sortie** :

![Exemple d'if-else](https://www.freecodecamp.org/news/content/images/2022/03/image-90.png)
_Exemple d'if-else_

## La clause elif en Python

L'instruction `elif` ajoute une autre branche de "décision" au `if-else`. Disons que vous voulez évaluer plusieurs expressions, vous pouvez alors utiliser `elif` comme suit :

```python
if <expression>:
    <statement(s)>
elif <expression>:
    <statement(s)>
elif <expression>:
    <statement(s)>
    .
    .
    .
else:
    <statement(s)>

```

Cela signifie que lorsque l'instruction `if` est fausse, l'expression `elif` suivante est vérifiée. Dès qu'une expression est vraie, le contrôle sort du bloc `if-else`.

Au plus, un seul bloc sera exécuté. Si `else` n'est pas spécifié et que toutes les instructions sont `false`, aucun des blocs ne sera exécuté.

**Voici un exemple :**

```python
if 51<5:
  print("Faux, instruction ignorée")
elif 0<5:
  print("vrai, bloc exécuté")
elif 0<3:
  print("vrai, mais le bloc ne s'exécutera pas")
else:
  print("Si tout échoue.")
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-91.png)

Notez que le deuxième `elif` ne s'est pas exécuté car le premier elif a été évalué comme `true`.

## Un exemple pratique d'if-else – le nombre est-il pair ou impair ?

Dans cet exemple, nous allons vérifier si un nombre est pair ou impair. Dans la logique, nous avons vérifié que si le modulo d'un nombre est zéro, il est pair. C'est parce que tous les nombres pairs, lorsqu'ils sont divisés par 2, ont un reste de `0`. Nous avons vérifié le modulo de `0` dans une instruction séparée, car la division par zéro donne une erreur de traceback.

```python
# Prendre l'entrée de l'utilisateur
inp_num = input("Entrez un nombre : ")

# Convertir la chaîne en entier
inp_num = int(inp_num)

if inp_num == 0:
  print(inp_num, "est Pair")
elif inp_num%2==0:
  print(inp_num, "est Pair")
else:
  print(inp_num, "est Impair")
```

**Sortie :**

Cas de test #1 :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-92.png)

Cas de test #2 :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-93.png)

Cas de test #3 :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-94.png)

## Conclusion

Dans ce tutoriel, nous avons appris comment nous pouvons contrôler le flux d'exécution en utilisant les instructions `if-else`. L'utilisation d'instructions conditionnelles nous aide à écrire des programmes significatifs. Ces instructions peuvent être imbriquées pour traiter des problèmes complexes.

Quelle est la chose que vous avez préférée apprendre dans ce tutoriel ? Dites-le-moi sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Crédits de l'image de la bannière : [Thinking vector created by storyset - www.freepik.com](https://www.freepik.com/vectors/thinking) & canva.com