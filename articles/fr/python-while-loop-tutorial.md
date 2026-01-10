---
title: Tutoriel sur les boucles While en Python – Exemples de syntaxe While True et
  boucles infinies
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-11-13T15:54:56.000Z'
originalURL: https://freecodecamp.org/news/python-while-loop-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/While-loops-image-1.png
tags:
- name: Python
  slug: python
seo_title: Tutoriel sur les boucles While en Python – Exemples de syntaxe While True
  et boucles infinies
seo_desc: "Welcome! If you want to learn how to work with while loops in Python, then\
  \ this article is for you. \nWhile loops are very powerful programming structures\
  \ that you can use in your programs to repeat a sequence of statements. \nIn this\
  \ article, you will..."
---

Bienvenue ! Si vous souhaitez apprendre à travailler avec les boucles while en Python, alors cet article est fait pour vous. 

Les boucles while sont des structures de programmation très puissantes que vous pouvez utiliser dans vos programmes pour répéter une séquence d'instructions. 

**Dans cet article, vous apprendrez :**

* Ce que sont les boucles while.
* À quoi elles servent.
* Quand elles doivent être utilisées.
* Comment elles fonctionnent en coulisses.
* Comment écrire une boucle while en Python.
* Ce que sont les boucles infinies et comment les interrompre.
* À quoi sert `while True` et sa syntaxe générale.
* Comment utiliser une instruction `break` pour arrêter une boucle while.

Vous apprendrez comment les boucles while fonctionnent en coulisses avec des exemples, des tableaux et des diagrammes.

Êtes-vous prêt ? Commençons. 🔍

## 🔹 Objectif et cas d'utilisation des boucles While

Commençons par l'objectif des boucles while. À quoi servent-elles ?

Elles sont utilisées pour répéter une séquence d'instructions un nombre inconnu de fois. Ce type de boucle s'exécute **tant que** une condition donnée est `True` et ne s'arrête que lorsque la condition devient `False`.

Lorsque nous écrivons une boucle while, nous ne définissons pas explicitement combien d'itérations seront effectuées, nous écrivons seulement la condition qui doit être `True` pour continuer le processus et `False` pour l'arrêter.

**💡 Conseil :** si la condition de la boucle while n'évalue jamais `False`, alors nous aurons une boucle infinie, qui est une boucle qui ne s'arrête jamais (en théorie) sans intervention externe. 

**Voici quelques exemples de cas d'utilisation réels des boucles while :**

* **Saisie utilisateur :** Lorsque nous demandons une saisie utilisateur, nous devons vérifier si la valeur entrée est valide. Nous ne pouvons pas savoir à l'avance combien de fois l'utilisateur entrera une saisie invalide avant que le programme ne puisse continuer. Par conséquent, une boucle while serait parfaite pour ce scénario.
* **Recherche :** rechercher un élément dans une structure de données est un autre cas d'utilisation parfait pour une boucle while car nous ne pouvons pas savoir à l'avance combien d'itérations seront nécessaires pour trouver la valeur cible. Par exemple, l'algorithme de recherche binaire peut être implémenté en utilisant une boucle while.
* **Jeux :** Dans un jeu, une boucle while pourrait être utilisée pour maintenir la logique principale du jeu en cours jusqu'à ce que le joueur perde ou que le jeu se termine. Nous ne pouvons pas savoir à l'avance quand cela se produira, donc c'est un autre scénario parfait pour une boucle while. 

## 🔹 Fonctionnement des boucles While

Maintenant que vous savez à quoi servent les boucles while, voyons leur logique principale et comment elles fonctionnent en coulisses. Voici un diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-24.png)
_Boucle While_

**Décortiquons cela plus en détail :**

* Le processus commence lorsqu'une boucle while est rencontrée pendant l'exécution du programme.
* La condition est évaluée pour vérifier si elle est `True` ou `False`. 
* Si la condition est `True`, les instructions appartenant à la boucle sont exécutées. 
* La condition de la boucle while est vérifiée à nouveau. 
* Si la condition évalue à nouveau `True`, la séquence d'instructions s'exécute à nouveau et le processus est répété.
* Lorsque la condition évalue `False`, la boucle s'arrête et le programme continue au-delà de la boucle.

L'une des caractéristiques les plus importantes des boucles while est que les variables utilisées dans la condition de la boucle ne sont pas mises à jour automatiquement. Nous devons mettre à jour leurs valeurs explicitement avec notre code pour nous assurer que la boucle s'arrêtera éventuellement lorsque la condition évaluera `False`.

## 🔹 Syntaxe générale des boucles While

Très bien. Maintenant que vous savez comment fonctionnent les boucles while, plongeons dans le code et voyons comment vous pouvez écrire une boucle while en Python. Voici la syntaxe de base :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-105.png)
_Boucle While (Syntaxe)_

**Voici les principaux éléments (dans l'ordre) :**

* Le mot-clé `while` (suivi d'un espace).
* Une condition pour déterminer si la boucle continuera à s'exécuter ou non en fonction de sa valeur de vérité (`True` ou `False`).
* Un deux-points (`:`) à la fin de la première ligne.
* La séquence d'instructions qui sera répétée. Ce bloc de code est appelé le "corps" de la boucle et il doit être indenté. Si une instruction n'est pas indentée, elle ne sera pas considérée comme faisant partie de la boucle (veuillez voir le diagramme ci-dessous). 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-7.png)

**💡 Conseil :** Le [guide de style Python](https://www.python.org/dev/peps/pep-0008/#indentation) (PEP 8) recommande d'utiliser 4 espaces par niveau d'indentation. Les tabulations ne doivent être utilisées que pour rester cohérent avec le code qui est déjà indenté avec des tabulations.

## 🔹 Exemples de boucles While

Maintenant que vous savez comment fonctionnent les boucles while et comment les écrire en Python, voyons comment elles fonctionnent en coulisses avec quelques exemples.

### Fonctionnement d'une boucle While de base

Voici une boucle while de base qui imprime la valeur de `i` **tant que** `i` est inférieur à 8 (`i < 8`) :

```python
i = 4

while i < 8:
    print(i)
    i += 1
```

Si nous exécutons le code, nous voyons cette sortie :

```
4
5
6
7
```

Voyons ce qui se passe en coulisses lorsque le code s'exécute :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-16.png)

* **Itération 1 :** initialement, la valeur de `i` est 4, donc la condition `i < 8` évalue `True` et la boucle commence à s'exécuter. La valeur de `i` est imprimée (4) et cette valeur est incrémentée de 1. La boucle recommence. 
* **Itération 2 :** maintenant la valeur de `i` est 5, donc la condition `i < 8` évalue `True`. Le corps de la boucle s'exécute, la valeur de `i` est imprimée (5) et cette valeur `i` est incrémentée de 1. La boucle recommence.
* **Itérations 3 et 4 :** Le même processus est répété pour les troisième et quatrième itérations, donc les entiers 6 et 7 sont imprimés.
* Avant de commencer la cinquième itération, la valeur de `i` est `8`. Maintenant la condition de la boucle while `i < 8` évalue `False` et la boucle s'arrête immédiatement.

💡 **Conseil :** Si la condition de la boucle while est `False` avant de commencer la première itération, la boucle while ne démarrera même pas.

### Saisie utilisateur en utilisant une boucle While

Voyons maintenant un exemple de boucle while dans un programme qui prend une saisie utilisateur. Nous utiliserons la fonction `input()` pour demander à l'utilisateur d'entrer un entier et cet entier ne sera ajouté à la liste que s'il est pair. 

Voici le code :

```python
# Définir la liste
nums = []

# La boucle s'exécutera tant que la longueur de la
# liste nums est inférieure à 4
while len(nums) < 4:
    # Demander une saisie utilisateur et la stocker dans une variable en tant qu'entier.
    user_input = int(input("Entrez un entier : "))
    # Si la saisie est un nombre pair, l'ajouter à la liste
    if user_input % 2 == 0:
        nums.append(user_input)
```

La condition de la boucle est `len(nums) < 4`, donc la boucle s'exécutera tant que la longueur de la liste `nums` est strictement inférieure à 4.

**Analysons ce programme ligne par ligne :**

* Nous commençons par définir une liste vide et l'assigner à une variable appelée `nums`.

```python
nums = []
```

* Ensuite, nous définissons une boucle while qui s'exécutera tant que `len(nums) < 4`.

```python
while len(nums) < 4:
```

* Nous demandons une saisie utilisateur avec la fonction `input()` et la stockons dans la variable `user_input`.

```python
user_input = int(input("Entrez un entier : "))
```

**💡 Conseil :** Nous devons convertir (caster) la valeur entrée par l'utilisateur en entier en utilisant la fonction `int()` avant de l'assigner à la variable car la fonction `input()` retourne une chaîne de caractères ([source](https://docs.python.org/3/library/functions.html#input)).

* Nous vérifions si cette valeur est paire ou impaire. 

```python
if user_input % 2 == 0:
```

* Si elle est paire, nous l'ajoutons à la liste `nums`. 

```python
nums.append(user_input)
```

* Sinon, si elle est impaire, la boucle recommence et la condition est vérifiée pour déterminer si la boucle doit continuer ou non.

Si nous exécutons ce code avec une saisie utilisateur personnalisée, nous obtenons la sortie suivante :

```python
Entrez un entier : 3
Entrez un entier : 4    
Entrez un entier : 2    
Entrez un entier : 1
Entrez un entier : 7
Entrez un entier : 6    
Entrez un entier : 3
Entrez un entier : 4    
```

Ce tableau résume ce qui se passe en coulisses lorsque le code s'exécute :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-86.png)

💡 **Conseil :** La valeur initiale de `len(nums)` est `0` car la liste est initialement vide. La dernière colonne du tableau montre la longueur de la liste à la fin de l'itération actuelle. Cette valeur est utilisée pour vérifier la condition avant que la prochaine itération ne commence. 

Comme vous pouvez le voir dans le tableau, l'utilisateur entre des entiers pairs lors des deuxième, troisième, sixième et huitième itérations et ces valeurs sont ajoutées à la liste `nums`. 

Avant qu'une "neuvième" itération ne commence, la condition est vérifiée à nouveau mais maintenant elle évalue `False` car la liste `nums` a quatre éléments (longueur 4), donc la boucle s'arrête. 

Si nous vérifions la valeur de la liste `nums` lorsque le processus est terminé, nous voyons ceci :

```python
>>> nums
[4, 2, 6, 4]
```

Exactement ce à quoi nous nous attendions, la boucle while s'est arrêtée lorsque la condition `len(nums) < 4` a évalué `False`.

Maintenant que vous savez comment les boucles while fonctionnent en coulisses et que vous avez vu quelques exemples pratiques, plongeons dans un élément clé des boucles while : la condition. 

## 🔹 Conseils pour la condition dans les boucles While

Avant de commencer à travailler avec les boucles while, vous devez savoir que la condition de la boucle joue un rôle central dans la fonctionnalité et la sortie d'une boucle while. 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-25.png)

Vous devez être très prudent avec l'opérateur de comparaison que vous choisissez car c'est une source très courante de bugs. 

Par exemple, les erreurs courantes incluent :

* Utiliser `<` (inférieur à) au lieu de `<=` (inférieur ou égal à) (ou vice versa).
* Utiliser `>` (supérieur à) au lieu de `>=` (supérieur ou égal à) (ou vice versa).  

Cela peut affecter le nombre d'itérations de la boucle et même sa sortie. 

Voyons un exemple :

Si nous écrivons cette boucle while avec la condition `i < 9` :

```python
i = 6

while i < 9:
    print(i)
    i += 1

```

Nous voyons cette sortie lorsque le code s'exécute :

```python
6
7
8
```

La boucle effectue trois itérations et s'arrête lorsque `i` est égal à `9`.

Ce tableau illustre ce qui se passe en coulisses lorsque le code s'exécute :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-20.png)

* Avant la première itération de la boucle, la valeur de `i` est 6, donc la condition `i < 9` est `True` et la boucle commence à s'exécuter. La valeur de `i` est imprimée et ensuite elle est incrémentée de 1. 
* Dans la deuxième itération de la boucle, la valeur de `i` est 7, donc la condition `i < 9` est `True`. Le corps de la boucle s'exécute, la valeur de `i` est imprimée, et ensuite elle est incrémentée de 1. 
* Dans la troisième itération de la boucle, la valeur de `i` est 8, donc la condition `i < 9` est `True`. Le corps de la boucle s'exécute, la valeur de `i` est imprimée, et ensuite elle est incrémentée de 1. 
* La condition est vérifiée à nouveau avant qu'une quatrième itération ne commence, mais maintenant la valeur de `i` est 9, donc `i < 9` est `False` et la boucle s'arrête. 

Dans ce cas, nous avons utilisé `<` comme opérateur de comparaison dans la condition, mais que pensez-vous qu'il se passera si nous utilisons `<=` à la place ?

```python
i = 6

while i <= 9:
    print(i)
    i += 1
```

Nous voyons cette sortie :

```python
6
7
8
9
```

La boucle effectue une itération de plus car nous utilisons maintenant l'opérateur "inférieur ou égal à" `<=` , donc la condition est toujours `True` lorsque `i` est égal à `9`.

Ce tableau illustre ce qui se passe en coulisses :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-21.png)

Quatre itérations sont effectuées. La condition est vérifiée à nouveau avant de commencer une "cinquième" itération. À ce stade, la valeur de `i` est `10`, donc la condition `i <= 9` est `False` et la boucle s'arrête. 

## 🔹 Boucles While infinies

Maintenant que vous savez comment fonctionnent les boucles while, mais que pensez-vous qu'il se passera si la condition de la boucle while n'évalue jamais `False` ? 

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-109.png)

### Qu'est-ce que les boucles While infinies ?

Rappelez-vous que les boucles while ne mettent pas à jour les variables automatiquement (nous sommes responsables de le faire explicitement avec notre code). Il n'y a donc aucune garantie que la boucle s'arrêtera à moins que nous écrivions le code nécessaire pour rendre la condition `False` à un moment donné pendant l'exécution de la boucle. 

Si nous ne le faisons pas et que la condition évalue toujours `True`, alors nous aurons une **boucle infinie**, qui est une boucle while qui s'exécute indéfiniment (en théorie).

Les boucles infinies sont généralement le résultat d'un bug, mais elles peuvent également être causées intentionnellement lorsque nous voulons répéter une séquence d'instructions indéfiniment jusqu'à ce qu'une instruction `break` soit trouvée. 

Voyons ces deux types de boucles infinies dans les exemples ci-dessous. 

💡 **Conseil :** Un bug est une erreur dans le programme qui provoque des résultats incorrects ou inattendus. 

### Exemple de boucle infinie

Voici un exemple de boucle infinie non intentionnelle causée par un bug dans le programme :

```python
# Définir une variable
i = 5

# Exécuter cette boucle tant que i est inférieur à 15
while i < 15:
    # Imprimer un message
    print("Bonjour le monde !")
    
```

Analysez ce code un instant. 

Ne remarquez-vous pas quelque chose de manquant dans le corps de la boucle ? 

C'est exact ! 

La valeur de la variable `i` n'est jamais mise à jour (elle est toujours `5`). Par conséquent, la condition `i < 15` est toujours `True` et la boucle ne s'arrête jamais. 

Si nous exécutons ce code, la sortie sera une séquence "infinie" de messages `Bonjour le monde !` car le corps de la boucle `print("Bonjour le monde !")` s'exécutera indéfiniment. 

```python
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
Bonjour le monde !
.
.
.
# Continue indéfiniment
```

Pour arrêter le programme, nous devrons interrompre la boucle manuellement en appuyant sur `CTRL + C`.

Lorsque nous le faisons, nous verrons une erreur `KeyboardInterrupt` similaire à celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-116.png)

Pour corriger cette boucle, nous devrons mettre à jour la valeur de `i` dans le corps de la boucle pour nous assurer que la condition `i < 15` évaluera éventuellement `False`. 

Voici une solution possible, en incrémentant la valeur de `i` de 2 à chaque itération :

```python
i = 5

while i < 15:
    print("Bonjour le monde !")
    # Mettre à jour la valeur de i
    i += 2
```

Très bien. Maintenant que vous savez comment corriger les boucles infinies causées par un bug. Vous devez simplement écrire du code pour garantir que la condition évaluera éventuellement `False`. 

Commençons à plonger dans les boucles infinies intentionnelles et comment elles fonctionnent. 

## 🔹 Comment créer une boucle infinie avec While True

Nous pouvons générer une boucle infinie intentionnellement en utilisant `while True`. Dans ce cas, la boucle s'exécutera indéfiniment jusqu'à ce que le processus soit arrêté par une intervention externe (`CTRL + C`) ou lorsqu'une instruction `break` est trouvée (vous en apprendrez plus sur `break` dans un instant).

Voici la syntaxe de base :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-35.png)

Au lieu d'écrire une condition après le mot-clé `while`, nous écrivons simplement la valeur de vérité directement pour indiquer que la condition sera toujours `True`.

Voici un exemple :

```python
>>> while True:
	print(0)

	
0
0
0
0
0
0
0
0
0
0
0
0
0
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    print(0)
KeyboardInterrupt
```

La boucle s'exécute jusqu'à ce que `CTRL + C` soit pressé, mais Python dispose également d'une instruction `break` que nous pouvons utiliser directement dans notre code pour arrêter ce type de boucle.

### L'instruction `break`

Cette instruction est utilisée pour arrêter une boucle immédiatement. Vous devez la considérer comme un panneau "stop" rouge que vous pouvez utiliser dans votre code pour avoir plus de contrôle sur le comportement de la boucle.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-110.png)

Selon la [Documentation Python](https://docs.python.org/3/tutorial/controlflow.html?highlight=break#break-and-continue-statements-and-else-clauses-on-loops) :

> L'instruction [`break`](https://docs.python.org/3/reference/simple_stmts.html#break), comme en C, sort de la boucle [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) ou [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) la plus imbriquée.

Ce diagramme illustre la logique de base de l'instruction `break` :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-111.png)
_L'instruction `break`_

**Voici la logique de base de l'instruction `break` :**

* La boucle while ne commence que si la condition évalue `True`. 
* Si une instruction `break` est trouvée à un moment donné pendant l'exécution de la boucle, la boucle s'arrête immédiatement.
* Sinon, si `break` n'est pas trouvé, la boucle continue son exécution normale et s'arrête lorsque la condition évalue `False`. 

Nous pouvons utiliser `break` pour arrêter une boucle while lorsqu'une condition est remplie à un point particulier de son exécution, donc vous la trouverez généralement au sein d'une instruction conditionnelle, comme ceci :

```
while True:
    # Code
    if <condition>:
    	break
    # Code
```

Cela arrête la boucle immédiatement si la condition est `True`.

💡 **Conseil :** Vous pouvez (en théorie) écrire une instruction `break` n'importe où dans le corps de la boucle. Elle n'a pas nécessairement à faire partie d'une conditionnelle, mais nous l'utilisons couramment pour arrêter la boucle lorsqu'une condition donnée est `True`.

Voici un exemple de `break` dans une boucle `while True` :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-41.png)

**Voyons cela plus en détail :**

La première ligne définit une boucle `while True` qui s'exécutera indéfiniment jusqu'à ce qu'une instruction `break` soit trouvée (ou jusqu'à ce qu'elle soit interrompue avec `CTRL + C`).

```python
while True:
```

La deuxième ligne demande une saisie utilisateur. Cette saisie est convertie en entier et assignée à la variable `user_input`. 

```
user_input = int(input("Entrez un entier : "))
```

La troisième ligne vérifie si la saisie est impaire. 

```
if user_input % 2 != 0:
```

Si c'est le cas, le message `Ce nombre est impair` est imprimé et l'instruction `break` arrête la boucle immédiatement.

```
print("Ce nombre est impair")
break
```

Sinon, si la saisie est paire, le message `Ce nombre est pair` est imprimé et la boucle recommence.

```
print("Ce nombre est pair")
```

La boucle s'exécutera indéfiniment jusqu'à ce qu'un entier impair soit entré car c'est la seule façon dont l'instruction `break` sera trouvée. 

Voici un exemple avec une saisie utilisateur personnalisée :

```python
Entrez un entier : 4
Ce nombre est pair
Entrez un entier : 6
Ce nombre est pair
Entrez un entier : 8
Ce nombre est pair
Entrez un entier : 3
Ce nombre est impair
>>> 
```

## 🔹 En résumé

* Les boucles while sont des structures de programmation utilisées pour répéter une séquence d'instructions tant qu'une condition est `True`. Elles s'arrêtent lorsque la condition évalue `False`. 
* Lorsque vous écrivez une boucle while, vous devez apporter les mises à jour nécessaires dans votre code pour vous assurer que la boucle s'arrêtera éventuellement.
* Une boucle infinie est une boucle qui s'exécute indéfiniment et ne s'arrête qu'avec une intervention externe ou lorsqu'une instruction `break` est trouvée. 
* Vous pouvez arrêter une boucle infinie avec `CTRL + C`.
* Vous pouvez générer une boucle infinie intentionnellement avec `while True`.
* L'instruction `break` peut être utilisée pour arrêter une boucle while immédiatement. 

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant que vous savez comment travailler avec les boucles While en Python. 

Suivez-moi sur Twitter [@EstefaniaCassN](https://twitter.com/EstefaniaCassN) et si vous voulez en apprendre plus sur ce sujet, consultez mon cours en ligne [Python Loops and Looping Techniques: Beginner to Advanced](https://www.udemy.com/course/python-loops-and-looping-techniques-beginner-to-advanced/?referralCode=EEABE054BAB98C00CC8E).