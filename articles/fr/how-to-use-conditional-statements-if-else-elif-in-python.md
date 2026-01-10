---
title: Comment utiliser les instructions conditionnelles en Python – Exemples de if,
  else et elif
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-07T16:03:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-conditional-statements-if-else-elif-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Conditional.JPG
tags:
- name: Conditionals
  slug: conditionals
- name: Python
  slug: python
seo_title: Comment utiliser les instructions conditionnelles en Python – Exemples
  de if, else et elif
seo_desc: 'Conditional statements are an essential part of programming in Python.
  They allow you to make decisions based on the values of variables or the result
  of comparisons.

  In this article, we''ll explore how to use if, else, and elif statements in Python,
  ...'
---

Les instructions conditionnelles sont une partie essentielle de la programmation en Python. Elles vous permettent de prendre des décisions basées sur les valeurs des variables ou le résultat de comparaisons.

Dans cet article, nous explorerons comment utiliser les instructions if, else et elif en Python, ainsi que quelques exemples de leur utilisation en pratique.

## Comment utiliser l'instruction `if` en Python

L'instruction `if` vous permet d'exécuter un bloc de code si une certaine condition est vraie. Voici la syntaxe de base :

```python
if condition:
    # code à exécuter si la condition est vraie
```

La condition peut être n'importe quelle expression qui évalue à une valeur booléenne (True ou False). Si la condition est True, le bloc de code indenté sous l'instruction if sera exécuté. Si la condition est False, le bloc de code sera ignoré.

Voici un exemple de comment utiliser une instruction `if` pour vérifier si un nombre est positif :

```python
num = 5

if num > 0:
    print("Le nombre est positif.")
```

Sortie :

```python
Le nombre est positif.
```

Dans cet exemple, nous utilisons l'opérateur `>` pour comparer la valeur de `num` à 0. Si `num` est supérieur à 0, le bloc de code indenté sous l'instruction `if` sera exécuté, et le message "Le nombre est positif." sera affiché.

## Comment utiliser l'instruction `else` en Python

L'instruction `else` vous permet d'exécuter un bloc de code différent si la condition `if` est False. Voici la syntaxe de base :

```python
if condition:
    # code à exécuter si la condition est vraie
else:
    # code à exécuter si la condition est fausse
```

Si la condition est True, le bloc de code indenté sous l'instruction `if` sera exécuté, et le bloc de code indenté sous l'instruction `else` sera ignoré.

Si la condition est False, le bloc de code indenté sous l'instruction `else` sera exécuté, et le bloc de code indenté sous l'instruction `if` sera ignoré.

Voici un exemple de comment utiliser une instruction `if-else` pour vérifier si un nombre est positif ou négatif :

```python
num = -5

if num > 0:
    print("Le nombre est positif.")
else:
    print("Le nombre est négatif.")
```

Sortie :

```python
Le nombre est négatif.
```

Dans cet exemple, nous utilisons une instruction `if-else` pour vérifier si `num` est supérieur à 0. Si c'est le cas, le message "Le nombre est positif." est affiché. Si ce n'est pas le cas (c'est-à-dire, si num est négatif ou zéro), le message "Le nombre est négatif." est affiché.

## Comment utiliser l'instruction `elif` en Python

L'instruction `elif` vous permet de vérifier plusieurs conditions en séquence, et d'exécuter différents blocs de code en fonction de la condition qui est vraie. Voici la syntaxe de base :

```python
if condition1:
    # code à exécuter si condition1 est vraie
elif condition2:
    # code à exécuter si condition1 est fausse et condition2 est vraie
elif condition3:
    # code à exécuter si condition1 et condition2 sont fausses, et condition3 est vraie
else:
    # code à exécuter si toutes les conditions sont fausses
```

L'instruction `elif` est une abréviation de "else if", et peut être utilisée plusieurs fois pour vérifier des conditions supplémentaires.

Voici un exemple de comment utiliser une instruction `if-elif-else` pour vérifier si un nombre est positif, négatif ou zéro :

```python
num = 0

if num > 0:
    print("Le nombre est positif.")
elif num < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est zéro.")
```

## Cas d'utilisation des instructions conditionnelles

### Exemple 1 : Vérifier si un nombre est pair ou impair.

```python
num = 4

if num % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")
```

Sortie :

```python
Le nombre est pair.
```

Dans cet exemple, nous utilisons l'opérateur modulus (%) pour vérifier si `num` est divisible par 2.

Si le reste de num divisé par 2 est 0, la condition num % 2 == 0 est True, et le bloc de code indenté sous l'instruction `if` sera exécuté. Il affichera le message "Le nombre est pair."

Si le reste n'est pas 0, la condition est False, et le bloc de code indenté sous l'instruction `else` sera exécuté, affichant le message "Le nombre est impair."

### Exemple 2 : Attribuer une note en lettre basée sur un score numérique

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Votre note est :", grade)
```

Sortie :

```python
Votre note est : B
```

Dans cet exemple, nous utilisons une instruction `if-elif-else` pour attribuer une note en lettre basée sur un score numérique.

L'instruction `if` vérifie si le score est supérieur ou égal à 90. Si c'est le cas, la note est définie à "A". Si ce n'est pas le cas, la première instruction `elif` vérifie si le score est supérieur ou égal à 80. Si c'est le cas, la note est définie à "B". Si ce n'est pas le cas, la deuxième instruction `elif` vérifie si le score est supérieur ou égal à 70, et ainsi de suite. Si aucune des conditions n'est remplie, l'instruction `else` attribue la note "F".

### Exemple 3 : Vérifier si une année est bissextile

```python
year = 2000

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "est une année bissextile.")
        else:
            print(year, "n'est pas une année bissextile.")
    else:
        print(year, "est une année bissextile.")
else:
    print(year, "n'est pas une année bissextile.")
```

Sortie :

```python
2000 est une année bissextile.
```

Dans cet exemple, nous utilisons des instructions `if` imbriquées pour vérifier si une année est bissextile. Une année est bissextile si elle est divisible par 4, sauf pour les années qui sont divisibles par 100 mais pas par 400.

L'instruction `if` externe vérifie si year est divisible par 4. Si c'est le cas, l'instruction `if` interne vérifie si elle est également divisible par 100. Si c'est le cas, l'instruction `if` la plus interne vérifie si elle est divisible par 400. Si c'est le cas, le bloc de code indenté sous cette instruction sera exécuté, affichant le message "est une année bissextile."

Si ce n'est pas le cas, le bloc de code indenté sous l'instruction `else` à l'intérieur de l'instruction `if` interne sera exécuté, affichant le message "n'est pas une année bissextile.".

Si l'année n'est pas divisible par 4, le bloc de code indenté sous l'instruction `else` de l'instruction `if` externe sera exécuté, affichant le message "n'est pas une année bissextile."

### Exemple 4 : Vérifier si une chaîne contient un certain caractère

```python
string = "hello, world"
char = "w"

if char in string:
    print("La chaîne contient le caractère", char)
else:
    print("La chaîne ne contient pas le caractère", char)
```

**Résultat :**

```python
La chaîne contient le caractère w
```

Dans cet exemple, nous utilisons l'opérateur `in` pour vérifier si le caractère `char` est présent dans la chaîne string. Si c'est le cas, la condition `char` in string est True, et le bloc de code indenté sous l'instruction `if` sera exécuté, affichant le message "La chaîne contient le caractère" suivi du caractère lui-même.

Si `char` n'est pas présent dans string, la condition est False, et le bloc de code indenté sous l'instruction `else` sera exécuté, affichant le message "La chaîne ne contient pas le caractère" suivi du caractère lui-même.

## Conclusion

Les instructions conditionnelles (if, else et elif) sont des constructions de programmation fondamentales qui vous permettent de contrôler le flux de votre programme en fonction des conditions que vous spécifiez. Elles fournissent un moyen de prendre des décisions dans votre programme et d'exécuter différents codes en fonction de ces décisions.

Dans cet article, nous avons vu plusieurs exemples de comment utiliser ces instructions en Python, y compris la vérification si un nombre est pair ou impair, l'attribution d'une note en lettre basée sur un score numérique, la vérification si une année est bissextile et la vérification si une chaîne contient un certain caractère.

En maîtrisant ces instructions, vous pouvez créer des programmes plus puissants et polyvalents capables de gérer une plus grande variété de tâches et de scénarios.

Il est important de garder à l'esprit que l'indentation correcte est cruciale lors de l'utilisation des instructions conditionnelles en Python, car elle détermine quel bloc de code est exécuté en fonction de la condition.

Avec de la pratique, vous deviendrez compétent dans l'utilisation de ces instructions pour créer des programmes Python plus complexes et efficaces.

Restons en contact sur [Twitter](https://twitter.com/Olujerry19) et [Linkedin](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).