---
title: 'Le guide ultime de Python : comment passer de débutant à pro'
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2020-05-01T16:47:40.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-python-from-beginner-to-intermediate-to-pro
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/The-Ultimate-Guide-To-Python-1.png
tags:
- name: 100Days100Projects
  slug: 100days100projects
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: 'Le guide ultime de Python : comment passer de débutant à pro'
seo_desc: 'If you have an interest in Data Science, Web Development, Robotics, or
  IoT you must learn Python. Python has become the fastest-growing programming language
  due to its heavy usage and wide range of applications.

  For a beginner or a person from a non-...'
---

Si vous vous intéressez à la science des données, au développement web, à la robotique ou à l'IoT, vous devez apprendre Python. Python est devenu le langage de programmation à la croissance la plus rapide en raison de son utilisation intensive et de sa large gamme d'applications.

Pour un débutant ou une personne issue d'un milieu non technique, apprendre Python est un bon choix. La syntaxe est comme parler et écrire en anglais simple. Par exemple, considérons cette syntaxe qui montre sa ressemblance avec la langue anglaise.

```python
print("Hello folks")
```

Nous utiliserons `Python3` dans ce tutoriel car il est largement utilisé. La plupart des frameworks et bibliothèques de Python supportent cette version.

> **Note :** Toute version supérieure à 3.5.2 supporte la plupart des bibliothèques et frameworks.

## Index :

1. [Introduction](#heading-introduction)
    
2. [Installation](#installation-)
    
3. [Shell Python](#heading-python-shell)
    
4. [Commentaire](#comment-)
    
5. [Print](#heading-print)
    
6. [Indentation](#heading-indentation)
    
7. [Variables](#heading-variables)
    
8. [Opérateurs](#heading-operators)
    
9. [Instructions conditionnelles](#heading-conditional-statements)
    
10. [Boucles For](#heading-for-loops)
    
11. [Boucles While](#heading-while-loops)
    
12. [Entrée utilisateur](#heading-user-input)
    
13. [Transtypage](#heading-typecasting)
    
14. [Dictionnaires](#heading-dictionaries)
    
15. [Listes](#heading-lists)
    
16. [Tuples](#heading-tuples)
    
17. [Ensembles](#heading-sets)
    
18. [Fonctions et arguments](#heading-functions-and-arguments)
    
19. [Args](#heading-args)
    
20. [Arguments de mot-clé](#heading-keyword-arguments)
    
21. [Arguments par défaut](#heading-default-argument)
    
22. [Kwargs](#heading-kwargs)
    
23. [Portée](#heading-scope)
    
24. [Instruction Return](#heading-return-statement)
    
25. [Expression Lambda](#heading-lambda-expression)
    
26. [Compréhension de liste](#heading-list-comprehension)
    
27. [Concepts POO](#oops-concepts-)
    
28. [Classes](#heading-classes)
    
29. [Méthodes](#heading-methods)
    
30. [Objets](#heading-objects)
    
31. [Constructeur](#heading-constructor)
    
32. [Attribut d'instance](#heading-instance-attributes)
    
33. [Attributs de classe](#heading-class-attributes)
    
34. [Self](#heading-self)
    
35. [Héritage](#heading-inheritance)
    
36. [Super](#heading-super)
    
37. [Héritage multiple](#heading-multiple-inheritance)
    
38. [Polymorphisme](#heading-polymorphism)
    
39. [Encapsulation](#heading-encapsulation)
    
40. [Décorateurs](#heading-decorator)
    
41. [Exceptions](#heading-exceptions)
    
42. [Import de package](#heading-package-import)
    
43. [Gestion JSON](#heading-json-handling)
    

**Note :** Le début de ce guide est destiné aux débutants. Si vous avez une expérience intermédiaire en Python, n'hésitez pas à passer à la section suivante en utilisant les liens ci-dessus.

## **Introduction** :

Selon l'[octoverse](https://octoverse.github.com/#top-languages) de Github, Python est le deuxième langage le plus utilisé par les développeurs en 2019.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-29-at-6.53.10-PM.png align="left")

*Graphique Octoverse de l'évolution des langages*

Avant d'apprendre un langage, il est utile de savoir comment ce langage est apparu. Eh bien, Python a été développé par [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum), un programmeur néerlandais, et a été publié en 1991.

Python est un langage interprété. Il utilise l'interpréteur [CPython](https://en.wikipedia.org/wiki/CPython) pour compiler le code Python en byte code. Pour un débutant, vous n'avez pas besoin de connaître beaucoup de choses sur CPython, mais vous devez être conscient de comment Python fonctionne en interne.

La philosophie derrière Python est que le code doit être lisible. Il y parvient avec l'aide de l'indentation. Il supporte de nombreux paradigmes de programmation comme la programmation fonctionnelle et orientée objet. Vous comprendrez mieux ces concepts au fur et à mesure de votre lecture.

La question de base que la plupart des débutants ont en tête est de savoir ce qu'un langage peut faire. Voici quelques cas d'utilisation de Python :

* Développement côté serveur (Django, Flask)
    
* Science des données (Pytorch, Tensor-flow)
    
* Analyse de données / Visualisation (Matplotlib)
    
* Scripting (Beautiful Soup)
    
* Développement embarqué
    

> **Note :** Je ne recommande aucun des frameworks ou bibliothèques mentionnés ci-dessus en particulier. Ils sont populaires et largement utilisés dans leurs domaines respectifs.

## Installation

La première étape pour apprendre un langage de programmation est de l'installer. Python est fourni avec la plupart des systèmes d'exploitation de nos jours. Utilisez la commande suivante dans votre terminal pour vérifier si Python est disponible :

```shell
python3 --version
```

Vous verrez la sortie suivante :

```shell
Python 3.7.0
```

Notez que votre version de Python peut être différente. Si vous avez Python installé et que la version est supérieure à 3.5.2, vous pouvez sauter cette section.

Pour ceux qui n'ont pas Python installé, suivez les étapes ci-dessous :

* [Utilisateur Windows](#heading-windows-user)
    
* [Utilisateur Mac](#heading-mac-user)
    
* [Utilisateur Linux](#heading-linux-user)
    

### Utilisateur Windows :

* Allez sur le [site officiel de Python](https://www.python.org/downloads/).
    
* Cliquez sur le bouton de téléchargement (Télécharger Python 3.8.2) \[ **Note :** La version peut différer en fonction de quand vous lisez cet article \]
    
* Allez dans le chemin où le package est téléchargé et double-cliquez sur l'installateur.
    
* Cochez la case indiquant "Ajouter Python 3.x à PATH" puis cliquez sur "Installer maintenant".
    
* Une fois terminé, vous recevrez une invite indiquant que "L'installation a réussi". Vérifiez à nouveau si Python est configuré correctement en utilisant la commande ci-dessus.
    
* Pour confirmer si Python est installé et configuré correctement, utilisez la commande `python3 --version`.
    

### Utilisateur Mac :

* Installez d'abord [xcode](https://apps.apple.com/in/app/xcode/id497799835?mt=12) depuis l'app store.
    
* Si vous souhaitez installer Xcode en utilisant le terminal, utilisez la commande suivante :
    

```shell
xcode-select --install
```

* Après cela, nous utiliserons le gestionnaire de paquets brew pour installer Python. Pour installer et configurer [brew](https://brew.sh/), utilisez la commande suivante :
    

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

* Une fois la configuration de brew terminée, utilisez la commande suivante pour mettre à jour les paquets obsolètes :
    

```shell
brew update
```

* Utilisez la commande suivante pour installer Python :
    

```shell
brew install python3
```

* Pour confirmer si Python est installé et configuré correctement, utilisez la commande `python3 --version`.
    

### Utilisateur Linux :

* Pour installer Python en utilisant `apt`, utilisez la commande suivante :
    

```shell
sudo apt install python3
```

* Pour installer Python en utilisant `yum`, utilisez la commande suivante :
    

```shell
sudo yum install python3
```

* Pour confirmer si Python est installé et configuré correctement, utilisez la commande `python3 --version`.
    

## Shell Python :

Le shell est l'un des outils les plus utiles que vous rencontrerez. Le shell Python nous donne le pouvoir de tester rapidement n'importe quel concept avant de l'intégrer dans notre application.

Allez dans le terminal ou l'invite de commande. Entrez la commande `python3` et vous obtiendrez la sortie suivante :

```shell
[1;32m[0m[1;32m[0m[0;32mPython 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Dans ce tutoriel, nous apprendrons certains concepts à l'aide du shell python3 que vous pouvez voir ci-dessus. À partir de maintenant, chaque fois que je mentionne **aller dans le shell Python**, cela signifie que vous devez utiliser la commande `python3`.

Pour apprendre les concepts restants, nous créerons un fichier appelé "testing" avec l'extension `.py`. Pour exécuter ce fichier, nous utiliserons la commande suivante :

```shell
python3 testing.py
```

Allons dans le shell Python. Tapez `10 + 12` après le marqueur `>>>`. Vous obtiendrez la sortie 22 :

```python
>>> 10 + 12
22
```

## Commentaires :

Les commentaires facilitent l'écriture de code car ils nous aident (et aident les autres) à comprendre pourquoi un morceau de code particulier a été écrit. Une autre chose géniale à propos des commentaires est qu'ils aident à améliorer la lisibilité du code.

```python
# Stay Safe
```

Lorsque vous ajoutez la syntaxe ci-dessus, l'interpréteur Python comprend que c'est un commentaire. Tout ce qui suit `#` n'est pas exécuté.

Vous vous demandez peut-être pourquoi vous devriez utiliser des commentaires. Imaginez que vous êtes un développeur et que vous avez été affecté à un énorme projet. Le projet compte plus de mille lignes de code. Pour comprendre comment tout fonctionne, vous devrez passer ligne par ligne et lire tout le code.

Quelle est la meilleure solution ? Ah-ha ! Les commentaires. Les commentaires nous aident à comprendre pourquoi un morceau de code particulier a été écrit et ce qu'il retourne ou fait. Considérez cela comme une documentation pour chaque morceau de code.

## Print :

Outre les outils de débogage de l'éditeur, la chose qui aide le plus souvent les développeurs à résoudre les problèmes est une instruction print. L'instruction print est l'une des syntaxes les plus sous-estimées de toute la programmation.

Alors, comment aide-t-elle à déboguer un problème ? Eh bien, imaginez que vous avez un module et que vous souhaitez vérifier le flux d'exécution pour le comprendre ou le déboguer. Il y a deux options. Soit vous pouvez utiliser un débogueur, soit ajouter une instruction print.

Il n'est pas toujours possible d'utiliser un débogueur. Par exemple, si vous utilisez le shell Python, alors un débogueur n'est pas disponible. Dans un tel scénario, print nous aide. Un autre scénario est lorsque votre application est en cours d'exécution. Vous pouvez ajouter une instruction print qui s'affichera dans les logs de votre application et les surveiller en temps réel.

Python fournit une méthode print intégrée avec la syntaxe suivante :

```python
print("Stay safe...")
```

## Indentation :

Une autre partie intéressante de ce langage est l'indentation. Pourquoi ? Eh bien, la réponse est simple : cela rend le code lisible et bien formaté. Il est obligatoire en Python de suivre les règles d'indentation. Si une indentation correcte n'est pas suivie, vous obtiendrez l'erreur suivante :

```python
IndentationError: unexpected indent
```

Voyez-vous, même les erreurs en Python sont si lisibles et faciles à comprendre. Au début, vous pourriez être ennuyé par l'obligation d'indentation. Mais avec le temps, vous comprendrez que l'indentation est l'amie du développeur.

## **Variables** :

Comme le nom l'indique, une variable est quelque chose qui peut changer. Une variable est un moyen de se référer à un emplacement mémoire utilisé par un programme informatique.

Eh bien, dans la plupart des langages de programmation, vous devez assigner le type à une variable. Mais en Python, vous n'en avez pas besoin. Par exemple, pour déclarer un entier en C, la syntaxe suivante est utilisée : `int num = 5;`. En Python, c'est `num = 5`.

Allez dans le shell Python et effectuez l'opération étape par étape :

* `Integer` : Valeurs numériques qui peuvent être positives, négatives ou nulles sans point décimal.
    

```python
>>> num = 5
>>> print(num)
5
>>> type(num)
<class 'int'>
```

Comme vous pouvez le voir ici, nous avons déclaré une variable `num` et assigné 5 comme valeur. La méthode intégrée `type` de Python peut être utilisée pour vérifier le type de variable. Lorsque nous vérifions le type de `num`, nous voyons la sortie `<class 'int'>`. Pour l'instant, concentrez-vous simplement sur le `int` dans cette sortie. `int` représente un entier.

* `Float` : Similaire à un entier mais avec une légère différence — les floats sont une valeur numérique avec une décimale.
    

```python
>>> num = 5.0
>>> print(num)
5.0
>>> type(num)
<class 'float'>
```

Ici, nous avons assigné un nombre avec une seule décimale à `num`. Lorsque nous vérifions le type de `num`, nous pouvons voir qu'il est `float`.

* `String` : Une formation de caractères ou d'entiers. Ils peuvent être représentés en utilisant des guillemets doubles ou simples.
    

```python
>>> greet = "Hello user"
>>> print(greet)
Hello user
>>> type(greet)
<class 'str'>
```

Ici, nous avons assigné une chaîne à `greet`. Le type de greet est une chaîne comme vous pouvez le voir à partir de la sortie.

* `Boolean` : Un opérateur binaire avec une valeur Vrai ou Faux.
    

```python
>>> is_available = True
>>> print(is_available)
True
>>> type(is_available)
<class 'bool'>
```

Ici, nous avons assigné une valeur True à `is_available`. Le type de cette variable est booléen. Vous ne pouvez assigner que **True** ou **False**. Souvenez-vous que **T** et **F** doivent être en majuscules ou cela donnera une erreur comme suit :

```shell
>>> is_available = true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
```

* `NoneType` : Cela est utilisé lorsque nous n'avons pas la valeur de la variable.
    

```python
>>> num = None
>>> print(num)
None
>>> type(num)
<class 'NoneType'>
```

## Opérateurs :

Jetez un coup d'œil à l'image ci-dessous pour voir tous les opérateurs arithmétiques disponibles en Python :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-30-at-12.28.55-PM.png align="left")

*Tableau des opérateurs*

Passons en revue les opérateurs un par un.

### Opérateurs arithmétiques

Cela inclut l'addition, la soustraction, la suppression, l'exponentiation, le modulo et la division entière. Ainsi que la syntaxe abrégée pour certains opérateurs.

Tout d'abord, nous allons déclarer deux variables, `a` et `b`.

```python
>>> a = 6 # Assignment
>>> b = 2
```

Essayons nos opérations arithmétiques de base :

```python
>>> a + b # Addition
8
>>> a - b # Subtraction
4
>>> a * b # Multiplication
12
>>> a / b # Division
3.0
>>> a ** b # Exponentiation
36
```

Pour tester d'autres opérations arithmétiques, changeons la valeur de `a` et `b`.

```python
>>> a = 7
>>> b = 3
>>> a % b # Modulus
1
>>> a // b # Floor division
2
```

Les opérations arithmétiques abrégées sont également disponibles en Python. Reportez-vous à l'image ci-dessus pour les tester. Pour imprimer la sortie des opérations abrégées, utilisez l'instruction `print`.

### Opérateurs de comparaison

Cela inclut égal à, supérieur à et inférieur à.

```python
>>> a = 5 # Assign
>>> b = 2 # Assign
>>> a > b # Greater than
True
>>> a < b # less then
False
>>> a == b # Equal to
False
>>> a >= 5 # Greater than or equal to
True
>>> b <= 1 # Less than or equal to
False
```

### Opérateurs logiques

Ces opérateurs incluent not, and, & or.

```python
>>> a = 10
>>> b = 2
>>> a == 2 and b == 10 # and
False
>>> a == 10 or b == 10 # or
True
>>> not(a == 10) # not
False
>>> not(a == 2)
True
```

## Instructions conditionnelles :

Comme le nom le suggère, les instructions conditionnelles sont utilisées pour évaluer si une condition est vraie ou fausse.

De nombreuses fois, lorsque vous développez une application, vous devez vérifier une certaine condition et faire différentes choses en fonction du résultat. Dans de tels scénarios, les instructions conditionnelles sont utiles. Si, elif et else sont les instructions conditionnelles utilisées en Python.

Nous pouvons comparer des variables, vérifier si la variable a une valeur ou si c'est un booléen, puis vérifier si c'est vrai ou faux. Allez dans le shell Python et effectuez l'opération étape par étape :

**Condition Numéro 1 :** Nous avons un entier et 3 conditions ici. La première est la condition `if`. Elle vérifie si le nombre est égal à 10.

La deuxième est la condition `elif`. Ici, nous vérifions si le nombre est inférieur à 10.

La dernière condition est `else`. Cette condition s'exécute lorsque aucune des conditions ci-dessus ne correspond.

```python
>>> number = 5
>>> if number == 10:
...     print("Number is 10")
... elif number < 10:
...     print("Number is less than 10")
... else:
...     print("Number is more than 10")
...
```

Sortie :

```shell
Number is less than 10
```

**Note :** Il n'est pas obligatoire de vérifier que deux conditions sont égales dans la condition `if`. Vous pouvez le faire dans le `elif` également.

**Condition Numéro 2 :** Nous avons un booléen et 2 conditions ici. Avez-vous remarqué comment nous vérifions si la condition est vraie ? Si `is_available`, alors imprimer "Yes it is available", sinon imprimer "Not available".

```python
>>> is_available = True
>>> if is_available:
...     print("Yes it is available")
... else:
...     print("Not available")
...
```

Sortie :

```shell
Yes it is available
```

**Condition Numéro 3 :** Ici, nous avons inversé la condition numéro 2 à l'aide de l'opérateur not.

```python
>>> is_available = True
>>> if not is_available:
...     print("Not available")
... else:
...     print("Yes it is available")
...
```

Sortie :

```shell
Yes it is available
```

**Condition Numéro 4 :** Ici, nous déclarons les données comme None et vérifions si les données sont disponibles ou non.

```python
>>> data = None
>>> if data:
...     print("data is not none")
... else:
...     print("data is none")
...
```

Sortie :

```shell
data is none
```

**Condition Numéro 5 :** Vous pouvez également utiliser un if en ligne en Python. La syntaxe pour y parvenir est la suivante :

```python
>>> num_a = 10
>>> num_b = 5
>>> if num_a > num_b: print("num_a is greater than num_b")
...
```

Sortie :

```shell
num_a is greater than num_b
```

**Condition Numéro 6 :** Vous pouvez également utiliser un if else en ligne en Python. La syntaxe pour y parvenir est la suivante :

```python
expression_if_true if condition else expression_if_false
```

Exemple :

```python
>>> num = 5
>>> print("Number is five") if num == 5 else print("Number is not five")
```

Sortie :

```shell
Number is five
```

**Condition Numéro 7 :** Vous pouvez également utiliser des instructions if-else imbriquées. La syntaxe pour y parvenir est la suivante :

```python
>>> num = 25
>>> if num > 10:
...     print("Number is greater than 10")
...     if num > 20:
...             print("Number is greater than 20")
...     if num > 30:
...             print("Number is greater than 30")
... else:
...     print("Number is smaller than 10")
...
```

Sortie :

```shell
Number is greater than 10
Number is greater than 20
```

**Condition Numéro 8 :** Vous pouvez également utiliser l'opérateur `and` dans une instruction conditionnelle. Il indique que si la condition1 et la condition2 sont toutes deux vraies, alors exécutez-la.

```python
>>> num = 10
>>> if num > 5 and num < 15:
...     print(num)
... else:
...     print("Number may be small than 5 or larger than 15")
...
```

Sortie :

```shell
10
```

Comme notre nombre est entre 5 et 15, nous obtenons la sortie 10.

**Condition Numéro 9 :** Vous pouvez également utiliser l'opérateur `or` dans une instruction conditionnelle. Il indique que si soit la condition1 soit la condition2 est vraie, alors exécutez-la.

```python
>>> num = 10
>>> if num > 5 or num < 7:
...     print(num)
...
```

Sortie :

```shell
10
```

Êtes-vous confus parce que la valeur de `num` est 10 et notre deuxième condition indique que `num` est inférieur à 7 ? Alors pourquoi obtenons-nous la sortie 10 ? C'est à cause de la condition `or`. Comme l'une des conditions correspond, elle l'exécutera.

## Boucles For :

Une autre méthode utile dans n'importe quel langage de programmation est un itérateur. Si vous devez implémenter quelque chose plusieurs fois, que ferez-vous ?

```python
print("Hello")
print("Hello")
print("Hello")
```

Eh bien, c'est une façon de le faire. Mais imaginez que vous devez le faire cent ou mille fois. Eh bien, c'est beaucoup d'instructions print que nous devons écrire. Il y a une meilleure façon appelée itérateurs ou boucles. Nous pouvons utiliser soit une boucle `for` soit une boucle `while`.

Ici, nous utilisons la méthode range. Elle spécifie la plage jusqu'à laquelle la boucle doit être répétée. Par défaut, le point de départ est 0.

```python
>>> for i in range(3):
...     print("Hello")
...
```

Sortie :

```shell
Hello
Hello
Hello
```

Vous pouvez également spécifier la plage de cette manière `range(1,3)`.

```python
>>> for i in range(1,3):
...     print("Hello")
...
```

Sortie :

```shell
Hello
Hello
```

"Hello" n'est imprimé que deux fois car nous avons spécifié la plage ici. Pensez à la plage comme `Nombre à droite - Nombre à gauche`.

Eh bien, vous pouvez également ajouter une instruction else dans la boucle for.

```python
>>> for i in range(3):
...     print("Hello")
... else:
...     print("Terminé")
```

Sortie :

```shell
Hello
Hello
Hello
Terminé
```

Comme vous pouvez le voir, notre boucle s'est exécutée 3 fois (3 - 0) et une fois cela fait, elle a exécuté l'instruction else.

Nous pouvons également imbriquer une boucle for dans une autre boucle for.

```python
>>> for i in range(3):
...     for j in range(2):
...             print("Boucle intérieure")
...     print("Boucle extérieure")
...
```

Sortie :

```shell
Boucle intérieure
Boucle intérieure
Boucle extérieure
Boucle intérieure
Boucle intérieure
Boucle extérieure
Boucle intérieure
Boucle intérieure
Boucle extérieure
```

Comme vous pouvez le voir, l'instruction print de la boucle intérieure s'est exécutée deux fois. Après cela, l'instruction print de la boucle extérieure s'est exécutée. Ensuite, la boucle intérieure s'est exécutée deux fois. Alors, que se passe-t-il ici ? Si vous êtes confus, alors considérez ceci pour le résoudre :

* Notre interpréteur vient et voit qu'il y a une boucle `for`. Il redescend et vérifie qu'il y a une autre boucle `for`.

* Donc maintenant, il exécutera la boucle `for` intérieure deux fois et sortira. Une fois terminé, il sait que la boucle for extérieure lui a ordonné de répéter deux fois de plus.

* Il recommence et voit la boucle for intérieure et répète.

Eh bien, vous pouvez également choisir de passer une certaine condition de boucle `for`. Que signifie passer ici ? Eh bien, chaque fois que cette boucle for se produira et que l'interpréteur verra l'instruction `pass`, il ne l'exécutera pas et passera à la ligne suivante.

```python
>>> for i in range(3):
...     pass
...
```

Vous n'obtiendrez aucune sortie sur le shell.

## Boucles While :

Un autre itérateur disponible en Python est la boucle `while`. Nous pouvons obtenir certains des mêmes résultats avec l'aide d'une boucle `while` que nous avons obtenus avec la boucle `for`.

```python
>>> i = 0
>>> while i < 5:
...     print("Nombre", i)
...     i += 1
...
```

Sortie :

```shell
Nombre 0
Nombre 1
Nombre 2
Nombre 3
Nombre 4
```

Rappelez-vous que chaque fois que vous utilisez une boucle while, il est important que vous ajoutiez une instruction d'incrémentation ou une instruction qui mettra fin à la boucle while à un moment donné. Sinon, la boucle while s'exécutera indéfiniment.

Une autre option est d'ajouter une instruction `break` dans une boucle `while`. Cela cassera la boucle.

```python
>>> i = 0
>>> while i < 5:
...     if i == 4:
...             break
...     print("Nombre", i)
...     i += 1
...
```

Sortie :

```shell
Nombre 0
Nombre 1
Nombre 2
Nombre 3
```

Ici, nous cassons la boucle `while` si nous trouvons que la valeur de `i` est 4.

Une autre option est d'ajouter une instruction `else` dans la boucle `while`. L'instruction sera exécutée après que la boucle while soit terminée.

```python
>>> i = 0
>>> while i < 5:
...     print("Nombre", i)
...     i += 1
... else:
...     print("Le nombre est supérieur à 4")
...
```

Sortie :

```shell
Nombre 0
Nombre 1
Nombre 2
Nombre 3
Nombre 4
Le nombre est supérieur à 4
```

L'instruction `continue` peut être utilisée pour sauter l'exécution actuelle et passer à la suivante.

```python
>>> i = 0
>>> while i < 6:
...     i += 1
...     if i == 2:
...             continue
...     print("nombre", i)
...
```

Sortie :

```shell
nombre 1
nombre 3
nombre 4
nombre 5
nombre 6
```

## Saisie utilisateur :

Imaginez que vous construisez une application en ligne de commande. Maintenant, vous devez prendre la saisie de l'utilisateur et agir en conséquence. Pour cela, vous pouvez utiliser la méthode intégrée `input` de Python.

La syntaxe pour y parvenir est la suivante :

```python
variable = input(".....")
```

Exemple :

```python
>>> name = input("Entrez votre nom : ")
Entrez votre nom : Sharvin
```

Lorsque vous utilisez la méthode `input` et appuyez sur entrée, vous serez invité avec le texte que vous entrez dans la méthode `input`. Vérifions si notre affectation fonctionne ou non :

```python
>>> print(name)
Sharvin
```

Le voilà ! Il fonctionne parfaitement. Ici, `Sharvin` est de type string.

```python
>>> type(name)
<class 'str'>
```

Essayons un autre exemple où nous attribuerons un entier plutôt qu'une chaîne et vérifierons le type.

```python
>>> date = input("Date d'aujourd'hui : ")
Date d'aujourd'hui : 12
>>> type(date)
<class 'str'>
```

Êtes-vous confus ? Nous avons entré un entier 12 et il nous donne toujours son type comme une chaîne. Ce n'est pas un bug. C'est ainsi que l'entrée est censée fonctionner. Pour convertir la chaîne en entier, nous utiliserons le transtypage.

## Transtypage :

Nous avons vu que la méthode `input` retourne une chaîne pour l'entier également. Maintenant, si nous voulons comparer cette sortie avec un autre entier, nous avons besoin d'un moyen de la convertir en entier.

```python
>>> date_to_int = int(date)
>>> type(date_to_int)
<class 'int'>
```

Ici, nous avons pris la date que nous avons déclarée ci-dessus dans la section Saisie utilisateur et l'avons convertie en entier en utilisant la méthode intégrée `int` de Python. Cela s'appelle le transtypage.

En gros, vous pouvez effectuer les conversions suivantes à l'aide du transtypage :

* entier en chaîne : `str()`

* chaîne en entier : `int()`

* entier en flottant : `float()`

> Note : La conversion de flottant en entier est également possible.

```python
>>> type(date)
<class 'str'>

# Conversion de chaîne en flottant
>>> date_to_float = float(date)
>>> type(date_to_float)
<class 'float'>

# Conversion de flottant en chaîne
>>> date_to_string = str(date_to_float)
>>> type(date_to_string)
<class 'str'>

# Conversion de flottant en entier
>>> date_to_int = int(date_to_float)
>>> type(date_to_int)
<class 'int'>
```

## Dictionnaires :

Imaginez que vous voulez stocker certains détails utilisateur. Alors, comment pouvez-vous stocker ces détails ? Oui, nous pouvons utiliser des variables pour les stocker comme suit :

```python
>>> fname = "Sharvin"
>>> lname = "Shah"
>>> profession = "Développeur"
```

Pour accéder à cette valeur, nous pouvons faire ce qui suit :

```python
>>> print(fname)
Sharvin
```

Mais est-ce une manière élégante et optimisée d'y accéder ? La réponse est non. Pour la rendre plus conviviale, stockons les données dans un dictionnaire clé-valeur.

Qu'est-ce qu'un dictionnaire ? Un dictionnaire est une collection qui est non ordonnée et mutable (c'est-à-dire qu'elle peut être mise à jour).

Voici le format du dictionnaire :

```json
data = {
	"key" : "value"
}
```

Comprenons mieux le dictionnaire à l'aide d'un exemple :

```python
>>> user_details = {
...     "fname": "Sharvin",
...     "lname": "Shah",
...     "profession": "Développeur"
... }
```

### Comment accéder à une valeur dans un dictionnaire

Nous pouvons accéder à la valeur à l'intérieur d'un dictionnaire de deux manières. Nous allons examiner les deux et ensuite les déboguer pour trouver laquelle est la meilleure.

Méthode 1 : Pour accéder à la valeur de la clé `fname` du dictionnaire `user_details`, nous pouvons utiliser la syntaxe suivante :

```python
>>> user_details["fname"]
'Sharvin'
```

Méthode 2 : Nous pouvons également accéder à la valeur de la clé `fname` du dictionnaire `user_details` en utilisant `get`.

```python
>>> user_details.get("fname")
'Sharvin'
```

Je sais que la méthode 1 semble plus facile à comprendre. Le problème avec elle se pose lorsque nous essayons d'accéder aux données qui ne sont pas disponibles dans notre dictionnaire.

```python
>>> user_details["age"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
```

Nous obtenons une KeyError qui indique que la clé n'est pas disponible. Essayons le même scénario avec la méthode 2.

```python
>>> user_details.get("age")
```

Nous n'obtenons rien d'imprimé dans notre console. Déboguons cela pour savoir pourquoi cela s'est produit. Attribuons une variable age à notre opération `get` et nous l'imprimerons dans notre console.

```python
>>> age = user_details.get("age")
>>> print(age)
None
```

Donc, lorsque `get` ne trouve pas la clé, il définit la valeur à None. À cause de cela, nous n'obtenons aucune erreur. Maintenant, vous vous demandez peut-être laquelle est la bonne. La plupart du temps, l'utilisation de la méthode 2 a plus de sens, mais pour certaines conditions de vérification strictes, nous devons utiliser la méthode 1.

### Comment vérifier si une clé existe

Vous vous demandez peut-être comment vérifier si le dictionnaire contient une clé particulière ou non. Python fournit la méthode intégrée `keys()` pour résoudre ce problème.

```python
>>> if "age" in user_details.keys():
...     print("Oui, elle est présente")
... else:
...     print("Non présente")
...
```

Nous obtiendrons la sortie suivante :

```shell
Non présente
```

Que se passe-t-il si nous voulons vérifier si le dictionnaire est vide ou non ? Pour comprendre cela, déclarons un dictionnaire vide comme suit :

```python
>>> user_details = {}
```

Lorsque nous utilisons if-else sur un dictionnaire directement, il retourne vrai si des données sont présentes ou faux si vide.

```python
>>> if user_details:
...     print("Non vide")
... else:
...     print("Vide")
...
```

Sortie :

```shell
Vide
```

Nous pouvons également utiliser la méthode intégrée `bool` de Python pour vérifier si le dictionnaire est vide ou non. Rappelez-vous que bool retourne False si le dictionnaire est vide et True s'il est rempli.

```python
>>> bool(user_details)
False

>>> user_details = {
...     "fname" : "Sharvin"
... }
>>> bool(user_details)
True
```

### Comment mettre à jour la valeur d'une clé existante

Maintenant que nous savons comment obtenir une clé particulière et vérifier si elle existe, comment la mettons-nous à jour dans le dictionnaire ?

Déclarons un dictionnaire comme suit :

```python
>>> user_details = {
...     "fname":"Sharvin",
...     "lname": "Shah",
...     "profession": "Développeur"
... }
```

Pour mettre à jour la valeur, utilisez la syntaxe suivante :

```python
>>> user_details["profession"] = "Développeur de logiciels"
>>> print(user_details)
{'fname': 'Sharvin', 'lname': 'Shah', 'profession': 'Développeur de logiciels'}
```

La mise à jour d'une valeur de clé dans un dictionnaire est la même que l'attribution d'une valeur à la variable.

### Comment ajouter une paire clé-valeur

La question suivante est comment ajouter une nouvelle valeur au dictionnaire ? Ajoutons une clé `age` avec une valeur de 100.

```python
>>> user_details["age"] = "100"
>>> print(user_details)
{'fname': 'Sharvin', 'lname': 'Shah', 'profession': 'Développeur de logiciels', 'age': '100'}
```

Comme vous pouvez le voir, une nouvelle paire clé-valeur est ajoutée dans notre dictionnaire.

### Comment supprimer une paire clé-valeur

Pour supprimer une paire clé-valeur du dictionnaire, Python fournit une méthode intégrée appelée `pop`.

```python
>>> user_details.pop("age")
'100'

>>> print(user_details)
{'fname': 'Sharvin', 'lname': 'Shah', 'profession': 'Développeur de logiciels'}
```

Cela supprime la paire clé-valeur `age` du dictionnaire `user_details`. Nous pouvons également utiliser un opérateur `del` pour supprimer la valeur.

```python
>>> del user_details["age"]

>>> print(user_details)
{'fname': 'Sharvin', 'lname': 'Shah', 'profession': 'Développeur de logiciels'}
```

La méthode `del` peut également être utilisée pour **supprimer complètement le dictionnaire**. Utilisez la syntaxe suivante pour supprimer complètement le dictionnaire `del user_details`.

### Comment copier un dictionnaire

Un dictionnaire ne peut pas être copié de manière traditionnelle. Par exemple, vous ne pouvez pas copier la valeur de `dictA` vers `dictB` comme suit :

```python
dictA = dictB
```

Pour copier les valeurs, vous devez utiliser la méthode `copy`.

```python
>>> dictB = user_details.copy()

>>> print(dictB)
{'fname': 'Sharvin', 'lname': 'Shah', 'profession': 'Développeur de logiciels'}
```

## Listes :

Imaginez que vous avez un ensemble de données qui n'est pas étiqueté. En d'autres termes, chaque élément de données n'a pas de clé qui le définit. Alors, comment allez-vous le stocker ? Les listes viennent à la rescousse. Elles sont définies comme suit :

```python
data = [ 1, 5, "xyz", True ]
```

Une liste est une collection de données aléatoires, ordonnées et mutables (c'est-à-dire qu'elle peut être mise à jour).

### Comment accéder aux éléments de la liste

Essayons d'accéder au premier élément :

```python
>>> data[1]
5
```

Attendez, que s'est-il passé ici ? Nous essayons d'accéder au premier élément mais nous obtenons le deuxième élément. Pourquoi ?

L'indexation de la liste commence à zéro. Alors, que veux-je dire par là ? L'indexation de la position des éléments commence à zéro. La syntaxe pour accéder à un élément est la suivante :

```python
list[position_in_list]
```

Pour accéder au premier élément, nous devons y accéder comme suit :

```python
>>> data[0]
1
```

Vous pouvez également spécifier une plage pour accéder à l'élément entre ces positions.

```python
>>> data[2:4]
['xyz', True]
```

Ici, la première valeur représente le début tandis que la dernière valeur représente la position jusqu'à laquelle nous voulons la valeur.

### Comment ajouter un élément à une liste

Pour ajouter un élément dans la liste, nous devons utiliser la méthode append fournie par Python.

```python
>>> data.append("Hello")

>>> data
[1, 5, 'abc', True, 'Hello']
```

### Comment changer la valeur d'un élément

Pour changer la valeur d'un élément, utilisez la syntaxe suivante :

```python
>>> data[2] = "abc"

>>> data
[1, 5, 'abc', True]
```

### Comment supprimer un élément d'une liste

Pour supprimer un élément d'une liste, nous pouvons utiliser la méthode intégrée `remove` de Python.

```python
>>> data.remove("Hello")
>>> data
[1, 5, 'abc', True]
```

### Comment parcourir une liste

Nous pouvons également parcourir la liste pour trouver un certain élément et opérer dessus.

```python
>>> for i in data:
...     print(i)
...
```

Sortie :

```shell
1
5
abc
True
```

### Comment vérifier si un élément existe ou non

Pour vérifier si un élément particulier existe ou non dans la liste, nous pouvons utiliser la boucle if comme suit :

```python
>>> if 'abc' in data:
...     print("yess..")
...
yess..
```

### Comment copier les données d'une liste

Pour copier les données d'une liste vers une autre, nous devons utiliser la méthode `copy`.

```python
>>> List2 = data.copy()
>>> List2
[1, 5, 'abc', True]
```

### Comment vérifier la longueur d'une liste

Nous pouvons également vérifier la longueur de la liste en utilisant la méthode intégrée `len` de Python.

```python
>>> len(data)
4
```

### Comment joindre deux listes

Pour joindre deux listes, nous pouvons utiliser l'opérateur `+`.

```python
>>> list1 = [1, 4, 6, "hello"]
>>> list2 = [2, 8, "bye"]
>>> list1 + list2
[1, 4, 6, 'hello', 2, 8, 'bye']
```

Que se passe-t-il si nous essayons d'accéder à une position d'élément qui n'est pas disponible dans la liste ? Nous obtenons une `erreur d'index de liste hors de portée` dans une telle condition.

```python
>>> list1[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

## Tuples :

Le tuple est un type de données qui est ordonné et immutable (c'est-à-dire que les données ne peuvent pas être changées).

Créons un tuple :

```python
>>> data = ( 1, 3 , 5, "bye")
>>> data
(1, 3, 5, 'bye')
```

### Comment accéder à un élément de tuple

Nous pouvons accéder aux éléments dans le tuple de la même manière que nous y accédons dans une liste :

```python
>>> data[3]
'bye'
```

Nous pouvons accéder à la plage d'index comme suit :

```python
>>> data[2:4]
(5, 'bye')
```

### Comment changer la valeur d'un tuple

Si vous pensez attendre — comment pouvons-nous changer la valeur d'un tuple, alors vous avez raison mon ami. Nous ne pouvons pas changer la valeur d'un tuple car il est immutable. Nous obtenons l'erreur suivante si nous essayons de changer la valeur d'un tuple :

```python
>>> data[1] = 8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Il existe une solution de contournement pour changer la valeur d'un tuple :

```python
>>> data = ( 1, 3 , 5, "bye")
>>> data_two = list(data) # Convertir les données en liste
>>> data_two[1] = 8 # Mettre à jour la valeur car la liste est mutable
>>> data = tuple(data_two) # Convertir à nouveau en tuple
>>> data
(1, 8, 5, 'bye')
```

Toutes les autres méthodes que nous avons vues dans la liste sont également applicables au tuple.

**\[ Note: Une fois qu'un tuple est créé, une nouvelle valeur ne peut pas être ajoutée. \]**.

## Ensembles :

Les ensembles sont un autre type de données en Python qui sont non ordonnés et non indexés. Les ensembles sont déclarés comme suit :

```python
>>> data = { "hello", "bye", 10, 15 }
>>> data
{10, 15, 'hello', 'bye'}
```

### Comment accéder à une valeur

Comme les ensembles sont non indexés, nous ne pouvons pas accéder directement à la valeur dans un ensemble. Ainsi, pour accéder à la valeur dans l'ensemble, vous devez utiliser une boucle for.

```python
>>> for i in data:
...     print(i)
...

10
15
hello
bye
```

### Comment changer une valeur

Une fois l'ensemble créé, les valeurs ne peuvent pas être changées.

### Comment ajouter un élément

Pour ajouter un élément à l'ensemble, Python fournit une méthode intégrée appelée `add`.

```python
>>> data.add("test")
>>> data
{10, 'bye', 'hello', 15, 'test'}
```

### Comment vérifier la longueur

Pour vérifier la longueur de l'ensemble, nous utilisons la méthode `len`.

```python
>>> len(data)
5
```

### Comment supprimer un élément

Pour supprimer un élément, utilisez la méthode `remove` :

```python
>>> data.remove("test")
>>> data
{10, 'bye', 'hello', 15}
```

## Fonctions et arguments :

Les fonctions sont un moyen pratique de déclarer une opération que nous voulons effectuer. Avec l'aide des fonctions, vous pouvez séparer la logique selon l'opération.

Les fonctions sont un bloc de code qui nous aide dans la réutilisabilité de la logique répétitive. Les fonctions peuvent être à la fois intégrées et définies par l'utilisateur.

Pour déclarer une fonction, nous utilisons le mot-clé `def`. Voici la syntaxe des fonctions :

```python
>>> def hello_world():
...     print("Hello world")
...
```

Ici, nous déclarons une fonction qui, lorsqu'elle est appelée, imprime une instruction "Hello world". Pour appeler une fonction, nous utilisons la syntaxe suivante :

```python
>>> hello_world()
```

Nous obtiendrons la sortie suivante :

```shell
Hello world
```

Rappelez-vous que les parenthèses `()` dans un appel de fonction signifie l'exécuter. Retirez ces parenthèses et essayez l'appel à nouveau.

```python
>>> hello_world
```

Vous obtiendrez la sortie suivante :

```shell
<function hello_world at 0x1083eb510>
```

Lorsque nous retirons les parenthèses de l'appel de fonction, cela nous donne une référence de fonction. Ici, comme vous pouvez le voir, la référence de `function hello_world` pointe vers cette adresse mémoire `0x1083eb510`.

Imaginez que vous devez effectuer une opération d'addition. Vous pouvez le faire en déclarant `a` et `b` puis en effectuant l'addition.

```python
>>> a = 5
>>> b = 10
>>> a + b
15
```

C'est une façon de procéder. Mais maintenant, imaginez que la valeur de `a` et `b` a changé et que vous devez le faire à nouveau.

```python
>>> a = 5
>>> b = 10
>>> a + b
15
>>> a = 2
>>> b = 11
>>> a + b
13
```

Cela semble encore faisable. Maintenant, imaginez que nous devons ajouter un ensemble de deux nombres cent fois. Les nombres dans l'ensemble sont différents pour chaque calcul. C'est beaucoup à faire. Ne vous inquiétez pas — nous avons une fonction à notre disposition pour résoudre ce problème.

```python
>>> def add(a,b):
...     print(a+b)
...
```

Ici, nous ajoutons `a` et `b` comme argument obligatoire à la fonction `add`. Pour appeler cette fonction, nous utiliserons la syntaxe suivante :

```python
>>> add(10,5)
```

Sortie :

```shell
15
```

Voyez comme il est facile de définir une fonction et de l'utiliser ? Alors, que se passe-t-il si nous ne passons pas d'argument ?

```python
>>> add()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 2 required positional arguments: 'a' and 'b'
```

Python lance une TypeError et nous informe que la fonction nécessite deux arguments.

Pouvez-vous deviner ce qui se passera si nous passons un troisième argument ?

```python
>>> add(10,5,1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() takes 2 positional arguments but 3 were given
```

Eh bien, Python nous informera que nous avons passé 3 arguments mais qu'il n'y a que 2 arguments positionnels.

Alors, que pouvons-nous faire lorsque nous ne savons pas combien d'arguments une fonction peut prendre ? Pour résoudre ce problème, nous utilisons args et kwargs.

## Args :

Lorsque vous ne savez pas combien d'arguments seront passés à la fonction, utilisez args et kwargs (kwargs sont discutés ci-dessous).

Pour passer n nombre d'arguments à une fonction, nous utilisons args. Nous ajoutons un `*` devant l'argument.

> N'oubliez pas que lorsque vous ajoutez un `*` devant, vous recevrez un tuple d'arguments.

```python
>>> def add(*num):
...     print(num)
...
```

Ici, `*num` est une instance de args. Maintenant, lorsque nous appelons la fonction `add`, nous pouvons passer n nombre d'arguments et cela ne lèvera pas de `TypeError`.

```python
>>> add(1,2,3)
(1, 2, 3)

>>> add(1,2,3,4)
(1, 2, 3, 4)
```

Maintenant, pour effectuer l'opération d'addition, nous utiliserons la fonction intégrée `sum` de Python.

```python
>>> def add(*num):
...     print(sum(num))
...
```

Maintenant, lorsque nous appelons la fonction add, nous obtiendrons la sortie suivante :

```python
>>> add(1,2,3) # Appel de fonction
6
>>> add(1,2,3,4) # Appel de fonction
10
```

## Arguments nommés :

Il arrive que nous ne connaissions pas l'ordre des arguments qui seront passés à notre fonction lorsqu'elle est appelée. Dans un tel scénario, nous utilisons des arguments nommés car vous pouvez les passer dans n'importe quel ordre dans votre appel et notre fonction connaîtra la valeur. Regardez cet exemple :

```python
>>> def user_details(username, age):
...     print("Username is", username)
...     print("Age is", age)
...
```

Appelons cette fonction comme suit :

```python
>>> user_details("Sharvin", 100)
```

Nous obtiendrons la sortie suivante :

```shell
Username is Sharvin
Age is 100
```

Cela semble correct, mais imaginez si nous appelions notre fonction de cette manière :

```python
>>> user_details(100, "Sharvin")
```

Nous obtiendrons la sortie suivante :

```shell
Username is 100
Age is Sharvin
```

Cela ne semble pas correct. Ce qui s'est passé, c'est que `username` a pris la valeur de 100 tandis que `age` a pris la valeur de "Sharvin". Dans des scénarios comme celui-ci où nous ne connaissons pas l'ordre des arguments, nous pouvons utiliser des arguments nommés lors de l'appel de la fonction :

```python
>>> user_details(age=100, username="Sharvin")
```

Sortie :

```shell
Username is Sharvin
Age is 100
```

## Argument par défaut :

Supposons qu'il y ait une condition où nous ne sommes pas sûrs qu'un argument particulier recevra une valeur ou non lorsque la fonction est appelée. Dans un tel scénario, nous pouvons utiliser des arguments par défaut comme suit :

```python
>>> def user_details(username, age = None):
...     print("Username is", username)
...     print("Age is", age)
...
```

Ici, nous attribuons `None` à notre argument age. Si nous ne passons pas de second argument lors de l'appel de la fonction, il prendra None comme valeur par défaut.

Appelons la fonction :

```python
>>> user_details("Sharvin")
```

Sortie :

```shell
Username is Sharvin
Age is None
```

Si nous passons le second argument, il remplacera None et l'utilisera comme valeur.

```python
>>> user_details("Sharvin", 200)
Username is Sharvin
Age is 200
```

Mais que se passera-t-il si nous attribuons le premier argument dans notre fonction comme argument par défaut et le second comme argument obligatoire ? Allez dans la console Python et essayez ceci :

```python
>>> def user_details(username=None, age):
...     print("Username is", username)
...     print("Age is", age)
...
```

Vous obtiendrez l'erreur suivante :

```shell
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```

> **À retenir :** Tous les arguments obligatoires doivent être déclarés en premier et ensuite les arguments par défaut doivent être déclarés.

## Kwargs :

Il peut y avoir une situation où vous ne savez pas combien d'arguments nommés seront passés dans la fonction. Dans un tel scénario, nous pouvons utiliser Kwargs.

Pour utiliser kwargs, nous mettons `**` devant l'argument.

> **À retenir :** Lorsque vous ajoutez un `**` devant, vous recevrez un dictionnaire d'arguments.

Comprenons cela par un exemple. Nous allons déclarer une fonction qui accepte username comme argument avec `**` devant.

```python
>>> def user(**username):
...     print(username)
...
```

Lorsque nous appelons la fonction `user` comme suit, nous recevrons un dictionnaire.

```python
>>> user(username1="xyz",username2="abc")
```

Sortie :

```shell
{'username1': 'xyz', 'username2': 'abc'}
```

Alors, que se passe-t-il ici ? Cela semble identique à args, n'est-ce pas ?

Non, ce n'est pas le cas. Dans args, vous ne pouvez pas accéder à une valeur particulière par son nom car elle est sous la forme d'un tuple. Ici, nous obtenons les données sous la forme d'un dictionnaire, donc nous pouvons facilement accéder à la valeur.

Considérons cet exemple :

```python
>>> def user(**user_details):
...     print(user_details['username'])
...
```

Appelons notre fonction :

```python
>>> user(username="Sharvin",age="1000")
```

Et vous obtiendrez la sortie suivante :

```shell
Sharvin
```

## Portée :

Une portée définit où une variable ou une fonction est disponible. Il existe deux types de portée en Python : globale et locale.

### Portée globale

Une variable ou une fonction créée dans le corps principal du code Python est appelée une variable ou une fonction globale et fait partie de la portée globale. Par exemple :

```python
>>> greet = "Hello world"
>>> def testing():
...     print(greet)
...
>>> testing()
Hello world
```

Ici, la variable `greet` est disponible globalement car elle est déclarée dans le corps du programme.

### Portée locale

Une variable ou une fonction créée à l'intérieur d'une fonction est appelée une variable ou une fonction locale et fait partie de la portée locale :

```python
>>> def testing():
...     greet = "Hello world"
...     print(greet)
...
>>> testing()
Hello world
```

Ici, `greet` est créée à l'intérieur de la fonction testing et n'est disponible que là. Essayons d'y accéder dans notre corps principal et voyons ce qui se passe :

```python
>>> print(greet)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'greet' is not defined
```

**À retenir :** Redémarrez la console Python en appuyant sur ctrl + d et relancez le shell en utilisant la commande `python3` avant de tester le code ci-dessus. Le premier exemple vous fait déclarer la variable `greet` dans la portée globale, ce qui signifie qu'elle sera toujours disponible en mémoire lorsque vous exécuterez le deuxième exemple.

Comme `greet` n'est pas disponible globalement, nous obtenons l'erreur qu'elle n'est pas définie.

## Instruction return :

Jusqu'à présent, nos fonctions sont assez simples. Elles reçoivent des données, les traitent et les impriment. Mais dans le monde réel, vous avez besoin qu'une fonction retourne une sortie afin qu'elle puisse être utilisée dans différentes opérations.

Pour y parvenir, des instructions return sont utilisées. N'oubliez pas que les instructions return ne font partie que des fonctions et des méthodes. La syntaxe de l'instruction return est assez facile.

```python
>>> def add(a, b):
...     return a + b
...
>>> add(1,3)
4
```

Au lieu d'imprimer notre addition, nous retournons la sortie. La valeur de la sortie retournée peut également être stockée dans une variable.

```python
>>> sum = add(5,10)
>>> print(sum)
15
```

## Expression lambda :

Considérons une situation où vous ne voulez pas effectuer beaucoup de calculs dans une fonction. Dans un tel scénario, écrire une fonction complète n'a pas de sens. Pour résoudre cela, nous utilisons une expression lambda ou une fonction lambda.

Alors, qu'est-ce qu'une expression lambda ? C'est une fonction anonyme et elles sont limitées à une seule expression. L'expression lambda peut prendre n nombre d'arguments.

La syntaxe de l'expression lambda est :

```python
variable = lambda arguments: operation
```

Comprenons cela mieux par un exemple :

```python
>>> sum = lambda a: a + 10
```

Ici, nous avons déclaré une variable `sum` que nous utilisons pour appeler la fonction lambda. `a` représente l'argument qui est passé à cette fonction.

Appelons notre fonction :

```python
>>> x(5)
15
```

## Compréhension de liste :

Considérons une situation où vous voulez une liste de carrés. Normalement, vous déclarerez une liste `squares` et ensuite dans une boucle for, vous mettrez au carré les nombres.

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Cela est faisable, mais nous pouvons y parvenir en une seule ligne avec l'aide de la compréhension de liste.

Il y a deux façons d'y parvenir. Comprenons les deux.

```python
>>> squares = list(map(lambda x: x**2, range(10)))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Ici, nous utilisons le constructeur `list` pour construire une liste et à l'intérieur de celle-ci, une fonction lambda qui met au carré le nombre. Une autre façon d'obtenir le même résultat est la suivante :

```python
>>> squares = list(x**2 for x in range(10))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Je préfère cette façon car elle est plus concise et plus facile à comprendre.

Et si nous avons une condition où nous voulons un ensemble de deux nombres qui sont identiques ? Eh bien, nous devons écrire deux boucles for et une boucle if.

Voyons à quoi cela ressemblera :

```python
>>> num_list = []
>>> for i in range(10):
...     for j in range(10):
...             if i == j:
...                     num_list.append((i,j))
...
>>> num_list
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
```

C'est beaucoup de travail. Et en termes de lisibilité, c'est difficile à comprendre.

Utilisons la compréhension de liste pour obtenir le même résultat.

```python
>>> num_list = list((i,j) for i in range(10) for j in range(10) if i == j)

>>> num_list
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
```

Voyez comme il est facile d'obtenir la même sortie en une seule expression ? Eh bien, c'est la puissance de la compréhension de liste.

## Concepts de la POO :

Python est un langage de programmation multi-paradigme. Cela signifie que Python peut utiliser différentes approches pour résoudre un problème. L'un des paradigmes est la programmation procédurale ou fonctionnelle. Elle structure le code comme une recette – un ensemble d'étapes sous forme de fonctions et de blocs de code.

Une autre approche pour résoudre le problème est de créer des classes et des objets. Cela est connu sous le nom de programmation orientée objet. Un objet est une collection de données (variables) et de méthodes qui agissent sur ces données. Et les classes sont un plan pour chaque objet.

L'important à comprendre en programmation orientée objet est que les objets sont au centre du paradigme – ils représentent non seulement les données mais aussi la structure du programme.

Vous pouvez choisir le paradigme qui convient le mieux au problème à résoudre, mélanger différents paradigmes dans un programme, et/ou passer d'un paradigme à un autre à mesure que votre programme évolue.

### Avantages de la programmation orientée objet

* **Héritage :** C'est l'un des concepts les plus utiles en POO. Il spécifie que l'objet enfant aura toutes les propriétés et comportements de l'objet parent. Ainsi, l'héritage nous permet de définir une classe qui hérite de toutes les méthodes et propriétés d'une autre classe.

* **Polymorphisme :** Pour comprendre le polymorphisme, divisons le mot en deux parties. La première partie "poly" signifie plusieurs et "morph" signifie former ou façonner. Ainsi, le polymorphisme signifie qu'une tâche peut être effectuée de nombreuses manières différentes.

Par exemple, vous avez une classe `animal`, et tous les animaux parlent. Mais ils parlent différemment. Ici, le comportement "parler" est polymorphe et dépend de l'animal. Ainsi, le concept abstrait "animal" ne "parle" pas réellement, mais des animaux spécifiques (comme les chiens et les chats) ont une implémentation concrète de l'action "parler".

Le polymorphisme signifie que le même nom de fonction ou de méthode est utilisé pour différents types.

* **Encapsulation :** En programmation orientée objet, vous pouvez restreindre l'accès aux méthodes et variables – nous pouvons rendre les méthodes et variables privées. Cela peut empêcher les données d'être modifiées par accident et est connu sous le nom d'encapsulation.

Tout d'abord, nous comprendrons les classes, les objets et les constructeurs. Ensuite, après cela, nous examinerons à nouveau les propriétés ci-dessus. Si vous connaissez déjà les classes, les objets et les constructeurs, n'hésitez pas à passer à la section suivante.

## Classes :

Il existe des structures de données primitives disponibles en Python, par exemple, les nombres, les chaînes et les listes. Celles-ci peuvent toutes être utilisées pour des représentations simples comme le nom, le lieu, le coût, etc.

Mais que faire si nous avons des données plus complexes ? S'il y a un motif dans la répétition des propriétés de ces données, que pouvons-nous faire ?

Supposons que nous avons 100 animaux différents. Chaque animal a un nom, un âge, des pattes, etc. Que faire si nous voulons ajouter d'autres propriétés à chaque animal, ou si un autre animal est ajouté à cette liste ? Pour gérer un scénario aussi complexe, nous avons besoin de classes.

Selon la documentation officielle de [Python](https://docs.python.org/3/tutorial/classes.html) :

> Les classes fournissent un moyen de regrouper des données et des fonctionnalités. La création d'une nouvelle classe crée un nouveau type d'objet, permettant de créer de nouvelles instances de ce type.

Chaque instance de classe peut avoir des attributs attachés pour maintenir son état. Les instances de classe peuvent également avoir des méthodes (définies par sa classe) pour modifier son état.

Syntaxe de la classe :

```python
class ClassName:

    <expression-1>
    .
    .
    .
    <expression-N>
```

Nous utilisons le mot-clé `class` pour définir une classe. Nous allons définir une `class Car`.

```python
class Car:
    pass
```

## Méthodes :

Les méthodes ressemblent aux fonctions. La seule différence est que les méthodes dépendent d'un objet. Une fonction peut être invoquée par son nom tandis que les méthodes doivent être invoquées en utilisant leur référence de classe. Elles sont définies à l'intérieur de la classe.

Dans notre exemple, créons deux méthodes. L'une est un moteur et l'autre est une roue. Ces deux méthodes définissent les parties disponibles dans notre voiture.

Le programme ci-dessous nous donnera une meilleure idée des classes :

```python
>>> class Car:
...     def engine(self):
...             print("Engine")
...

>>> Car().engine()
Engine
```

Ici, nous appelons la méthode `engine` en utilisant la référence `Car()`.

Pour résumer, la classe fournit un plan de ce qui doit être défini mais elle ne fournit aucun contenu réel. La classe `Car` ci-dessus définit le moteur mais elle ne précisera pas ce qu'est le moteur d'une voiture spécifique. C'est spécifié par l'objet.

## Objets :

L'objet est une instance de la classe. Considérons l'exemple ci-dessus d'une voiture. Ici, Car est notre `class` et `toyota` est l'`object` de la voiture. Nous pouvons créer plusieurs copies de l'objet. Chaque objet doit être défini en utilisant la classe.

La syntaxe pour créer un objet est :

```python
toyota = Car()
```

Considérons notre exemple `Car` pour mieux comprendre les objets :

```python
class Car:

    def engine(self):
        print("Engine")

    def wheel(self):
        print("Wheel")

toyota = Car()
```

Le `toyota = Car()` ci-dessus est un **objet de classe**. Les objets de classe supportent deux types d'opérations : les références d'attributs et l'instanciation.

L'instanciation de classe utilise la notation de fonction. L'opération d'instanciation ("appeler" un objet de classe) crée un objet vide.

Maintenant, nous pouvons appeler différentes méthodes de notre classe `Car` en utilisant l'objet `toyota` que nous avons créé. Appelons les méthodes `engine` et `wheel`.

Ouvrez votre éditeur et créez un fichier nommé `mycar.py`. Dans ce fichier, copiez le code ci-dessous :

```python
class Car:

    def engine(self):
        print("Engine")

    def wheel(self):
        print("Wheel")

if __name__ == "__main__":
    toyota = Car()
    toyota.engine()
    toyota.wheel()
```

Enregistrez le code ci-dessus. Maintenant, examinons de plus près notre programme.

Ici, nous créons un objet `toyota` à l'aide de la classe `Car`. Le `toyota.engine()` est un objet méthode. Que se passe-t-il exactement lorsque l'objet méthode est appelé ?

Dans l'appel `toyota.engine()`, il ne prend aucun argument, mais si vous regardez la déclaration de la méthode, vous pouvez voir qu'elle prend un argument `self`.

Vous pouvez être confus quant à la raison pour laquelle cela ne lève pas d'erreur. Eh bien, chaque fois que nous utilisons un objet méthode, l'appel `toyota.engine()` est converti en `Car.engine(toyota)`. Nous comprendrons mieux le self dans la section à venir.

Exécutez le programme en utilisant la commande suivante.

```shell
python mycar.py
```

Vous obtiendrez la sortie suivante :

```shell
Engine
Wheel
```

## Constructeur :

La méthode `__init__` est la méthode constructeur en Python. La méthode constructeur est utilisée pour initialiser les données.

Allez dans la console Python et entrez cet exemple :

```python
>>> class Car():
...     def __init__(self):
...             print("Hello I am the constructor method.")
...
```

Lorsque nous appelons notre classe, nous obtiendrons la sortie suivante :

```python
>>> toyota = Car()
Hello I am the constructor method.
```

**Note :** Vous n'aurez jamais à appeler la méthode **init**() – elle est appelée automatiquement lorsque vous créez une instance de classe.

## Attributs d'instance :

Toutes les classes ont des objets et tous les objets ont des attributs. Les attributs sont les propriétés. Nous utilisons la méthode `__init__()` pour spécifier l'attribut initial d'un objet.

Considérons notre exemple de voiture :

```python
class Car():
    def __init__(self, model): 
        self.model = model  #attribut d'instance
```

Dans notre exemple, chaque `Car()` a un modèle spécifique. Ainsi, les attributs d'instance sont des données uniques à chaque instance.

## Attributs de classe :

Nous avons vu que les attributs d'instance sont spécifiques à chaque objet, mais les attributs de classe sont les mêmes pour toutes les instances. Regardons l'exemple de la voiture à l'aide des attributs de classe.

```python
class Car():

    no_of_wheels = 4 #attribut de classe
```

Ainsi, chaque voiture peut avoir des modèles différents, mais toutes les voitures auront seulement 4 roues.

## Self :

Maintenant, comprenons ce que signifie `self` et comment nous l'utilisons en programmation orientée objet. `self` représente l'instance d'une classe. En utilisant le mot-clé `self`, nous pouvons accéder aux données initialisées dans le constructeur et les méthodes d'une classe.

Regardons un exemple de la façon dont `self` peut être utilisé. Créons une méthode nommée `brand` sous notre classe `Car`.

À l'intérieur de cette méthode `__init__`, nous passerons un modèle en passant le nom du modèle de notre voiture lorsque nous instancions notre objet. Ce nom peut être accédé n'importe où dans la classe, par exemple `self.model` dans notre cas.

Allez dans le fichier nommé `mycar.py` et remplacez l'ancien code par ce code :

```python
class Car(): 

  def __init__(self, model): 
    self.model = model
  		
  def brand(self): 
    print("The brand is", self.model)  

if __name__ == "__main__":
  car = Car("Bmw")
  car.brand()
```

Maintenant, lorsque nous exécutons notre programme ci-dessus en utilisant la commande suivante :

```shell
python mycar.py
```

Nous obtiendrons la sortie suivante :

```shell
The brand is Bmw
```

**Note :** `self` est une convention et non un vrai mot-clé Python. `self` est un argument dans une méthode et nous pouvons utiliser un autre nom à sa place. Mais il est recommandé d'utiliser `self` car cela augmente la lisibilité de votre code.

## Héritage :

L'héritage fait référence à une classe qui hérite des propriétés d'une autre classe.

La classe à partir de laquelle les propriétés sont héritées est appelée la classe de base. La classe qui hérite des propriétés d'une autre classe est appelée la classe dérivée.

L'héritage peut être défini comme une relation parent-enfant. L'enfant hérite des propriétés du parent. Ainsi, l'enfant devient une classe dérivée tandis que le parent est une classe de base. Ici, le terme propriété fait référence aux attributs et méthodes.

La syntaxe pour une définition de classe dérivée ressemble à ceci :

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Il est important de noter que les classes enfants remplacent ou étendent les attributs et comportements des méthodes de la classe parente. Cela signifie que les classes enfants héritent de tous les attributs et comportements de leurs parents – mais elles sont également capables de spécifier un comportement différent à suivre.
Le type de classe le plus basique est un objet, dont toutes les autres classes héritent généralement comme parent. Modifions notre exemple précédent pour comprendre comment fonctionne l'héritage.

Nous allons créer une classe de base nommée `vehicle` :

```python
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name
```

Nous avons créé une classe `Vehicle` et instancié un constructeur avec `self.name` que nous utilisons dans la méthode `getName`. Chaque fois que cette méthode sera appelée, elle retournera le `name` qui a été passé lors de l'instanciation d'un objet pour cette classe.

Maintenant, créons une classe enfant `Car` :

```python
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

class Car(Vehicle):
  pass
```

`Car` est une classe enfant de `Vehicle`. Elle hérite de toutes les méthodes et attributs de la classe parente.

Maintenant, utilisons les méthodes et attributs de la classe `Vehicle` dans notre classe enfant `Car`.

```python
class Vehicle:

    def __init__(self, name, color='silver'):
        self.name = name
        self.color = color
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

class Car(Vehicle):
  pass

audi = Car("Audi r8")
print("The name of our car is", audi.get_name(), "and color is", audi.get_color())
```

Comprenons ce que nous avons fait ici.

Nous avons déclaré une classe nommée `Vehicle` avec un constructeur qui prend le nom comme argument tandis que la couleur a un argument par défaut.

Nous avons deux méthodes à l'intérieur. `get_name` retourne le nom tandis que `get_color` retourne la couleur. Nous avons instancié un objet et passé le nom de la voiture.

Une chose que vous remarquerez ici, c'est que nous utilisons les méthodes de la classe de base dans notre déclaration de classe enfant.

Exécutez le programme ci-dessus en utilisant la commande suivante :

```shell
python mycar.py
```

Sortie :

```python
The name of our car is Audi r8 and color is silver
```

Nous pouvons également remplacer une méthode ou un attribut parent. Dans l'exemple ci-dessus, nous avons défini la couleur de notre véhicule comme argentée. Mais que faire si la couleur de notre voiture est noire ?

Maintenant, pour chaque classe enfant, nous ne pouvons pas apporter de modifications dans la classe parente. C'est là qu'intervient la fonctionnalité de remplacement.

```python
class Vehicle:

    def __init__(self, name, color='silver'):
        self.name = name
        self.color = color
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

class Car(Vehicle):

    def get_color(self):
        self.color = 'black'
        return self.color

audi = Car("Audi r8")
print("The name of our car is", audi.get_name(), "and color is", audi.get_color()
```

Comme vous pouvez le voir dans le programme ci-dessus, je n'ai pas instancié de constructeur. La raison en est que notre classe enfant `Car` utilise uniquement les attributs de la classe `Vehicle` et qu'elle les hérite déjà. Donc dans un tel scénario, il n'est pas nécessaire de réinstancier ces attributs.

Maintenant, lorsque nous exécutons le programme ci-dessus, nous obtiendrons la sortie suivante :

```shell
The name of our car is Audi r8 and color is black
```

## Super :

`super()` retourne un objet temporaire de la superclasse qui permet ensuite d'appeler les méthodes de cette superclasse.

L'appel des méthodes précédemment construites avec `super()` nous évite de devoir réécrire ces méthodes dans notre sous-classe, et nous permet de remplacer les superclasses avec des modifications de code minimales. Ainsi, `super` étend la fonctionnalité de la méthode héritée.

Étendons notre exemple de voiture en utilisant `super()`. Nous allons instancier un constructeur avec `brand_name` et `color` dans la classe parente, `Vehicle`. Maintenant, nous allons appeler ce constructeur depuis notre classe enfant (`Car`) en utilisant `super`. Nous allons créer une méthode `get_description` qui retourne `self.model` de la classe `Car` et `self.brand_name`, `self.color` de la classe `Vehicle`.

```python
class Vehicle:
 
    def __init__(self, brand_name, color):
        self.brand_name = brand_name
        self.color = color
 
    def get_brand_name(self):
        return self.brand_name
 
class Car(Vehicle):
 
    def __init__(self, brand_name, model, color):  
        super().__init__(brand_name, color)       
        self.model = model
 
    def get_description(self):
        return "Car Name: " + self.get_brand_name() + self.model + " Color:" + self.color
 
c = Car("Audi ",  "r8", " Red")
print("Car description:", c.get_description())
print("Brand name:", c.get_brand_name())
```

Lorsque nous exécutons le programme ci-dessus, nous obtenons la sortie suivante :

```shell
Car description: Car Name: Audi r8 Color: Red
Brand name: Audi
```

## Héritage multiple :

Lorsque une classe hérite des méthodes et attributs de plusieurs classes parentes, on parle alors d'héritage multiple. Cela nous permet d'utiliser les propriétés de plusieurs classes de base ou classes parentes dans une classe dérivée ou enfant.

La syntaxe générale de l'héritage multiple est la suivante :

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Étendons notre exemple de véhicule en utilisant la propriété d'héritage multiple. Dans cet exemple, nous allons créer 3 classes, à savoir `Vehicle`, `Cost` et `Car`.

Les classes `Vehicle` et `Cost` seront les classes parentes. Une classe `Vehicle` représente la propriété générale tandis que la classe `Cost` représente son prix.

Comme `Car` a une propriété générale et un coût, elle aura deux classes parentes. Ainsi, nous hériterons de plusieurs classes parentes.

```python
class Vehicle:

    def __init__(self, brand_name):
        self.brand_name = brand_name
    
    def get_brand_name(self):
        return self.brand_name


class Cost:		

    def __init__(self, cost):
        self.cost = cost
    
    def get_cost(self):
        return self.cost

 
class Car(Vehicle, Cost):	

    def __init__(self, brand_name, model, cost): 
        self.model = model 
        Vehicle.__init__(self, brand_name) 
        Cost.__init__(self, cost) 

    def get_description(self):
        return self.get_brand_name() + self.model + " is the car " + "and it's cost is " + self.get_cost()
		
c = Car("Audi ",  "r8", "2 cr")
print("Car description:", c.get_description())
```

Ici, vous trouverez une chose dans le programme ci-dessus qui est différente de tous les autres programmes de ce tutoriel. J'ai utilisé `Vehicle.__init__(self, brand_name)` dans le constructeur de la classe `Car`. C'est une façon d'appeler les attributs de la classe parente. Une autre façon est `super` que j'ai expliqué ci-dessus.

Lorsque nous exécutons le programme ci-dessus, nous obtiendrons la sortie suivante :

```python
Car description: Audi r8 is the car and it's cost is 2 cr
```

Bien qu'il puisse être utilisé efficacement, l'héritage multiple doit être fait avec soin afin que nos programmes ne deviennent pas ambigus et difficiles à comprendre pour les autres programmeurs.

## Polymorphisme :

Le mot polymorphisme signifie avoir plusieurs formes. En programmation, le polymorphisme signifie qu'un même nom de fonction (mais avec des signatures différentes) est utilisé pour différents types.

Étendons notre programme de voiture en utilisant le polymorphisme. Nous allons créer deux classes, `Car` et `Bike`. Les deux classes ont une méthode ou fonction commune, mais elles impriment des données différentes. Le programme est assez explicite :

```python
class Car: 

    def company(self): 
        print("Car belongs to Audi company.")
   
    def model(self): 
        print("The Model is R8.") 
   
    def color(self): 
        print("The color is silver.") 
   
class Bike: 

    def company(self): 
        print("Bike belongs to pulsar company.") 
   
    def model(self): 
        print("The Model is dominar.") 
   
    def color(self): 
        print("The color is black.") 
  
def func(obj): 
    obj.company() 
    obj.model() 
    obj.color() 
   
car = Car() 
bike = Bike() 
   
func(car) 
func(bike)
```

Lorsque nous exécutons le code ci-dessus, nous obtenons la sortie suivante :

```shell
Car belongs to Audi company.
The Model is R8.
The color is silver.
Bike belongs to pulsar company.
The Model is dominar.
The color is black.
```

## Encapsulation :

Dans la plupart des programmations orientées objet, nous pouvons restreindre l'accès aux méthodes et variables. Cela peut empêcher les données d'être modifiées par accident et est connu sous le nom d'encapsulation.

Utilisons l'encapsulation dans notre exemple de voiture. Maintenant, imaginez que nous avons un moteur super secret. Dans le premier exemple, nous allons cacher notre moteur en utilisant une **variable privée**. Dans le deuxième exemple, nous allons cacher notre moteur en utilisant une **méthode privée**.

**Exemple 1 :**

```python
class Car:

  def __init__(self): 
    self.brand_name = 'Audi '
    self.model = 'r8'
    self.__engine = '5.2 L V10'
    
  def get_description(self):
        return self.brand_name + self.model + " is the car"
  
c = Car()
print(c.get_description)
print(c.__engine)
```

Dans cet exemple, `self.__engine` est un attribut privé. Lorsque nous exécutons ce programme, nous obtenons la sortie suivante.

```shell
Audi r8 is the car
AttributeError: 'Car' object has no attribute '__engine'
```

Nous obtenons une erreur indiquant que l'objet `Car` n'a pas d'attribut `__engine` car c'est un objet privé.

**Exemple 2 :**

Nous pouvons également définir une méthode privée en ajoutant `__` devant le nom de la méthode. Voici un exemple de la façon dont nous pouvons définir une méthode privée.

```python
class Car:

  def __init__(self):
      self.brand_name = 'Audi '
      self.model = 'r8'

  def __engine(self):
      return '5.2 L V10'

  def get_description(self):
      return self.brand_name + self.model + " is the car"
    
    
c = Car()
print(c.get_description())
print(c.__engine())
```

Dans cet exemple, `def __engine(self)` est une méthode privée. Lorsque nous exécutons ce programme, nous obtenons la sortie suivante.

```shell
Audi r8 is the car
AttributeError: 'Car' object has no attribute '__engine'
```

Maintenant, supposons que nous voulons accéder à l'attribut ou à la méthode privée, nous pouvons le faire de la manière suivante :

```python
class Car:

  def __init__(self):
      self.brand_name = 'Audi '
      self.model = 'r8'
      self.__engine_name = '5.2 L V10'

  def __engine(self):
      return '5.2 L V10'

  def get_description(self):
      return self.brand_name + self.model + " is the car"
    
    
c = Car()
print(c.get_description())
print("Accessing Private Method: ", c._Car__engine()) 
print("Accessing Private variable: ", c._Car__engine_name)
```

La sortie du programme suivant est :

```shell
Audi r8 is the car
Accessing Private Method:  5.2 L V10
Accessing Private variable:  5.2 L V10
```

L'encapsulation vous donne plus de contrôle sur le degré de couplage dans votre code. Elle permet à une classe de changer son implémentation sans affecter d'autres parties du code.

## Décorateur :

Imaginez que vous devez étendre la fonctionnalité de plusieurs fonctions. Comment allez-vous faire cela ?

Eh bien, une façon est de faire des appels fonctionnels et dans cette fonction, vous pouvez le gérer. Faire des changements dans 30 à 40 appels de fonction et se souvenir où placer l'appel est une tâche fastidieuse. Mais la manière plus élégante fournie par Python est avec les décorateurs.

Qu'est-ce qu'un décorateur ? Un décorateur est une fonction qui prend une fonction et étend sa fonctionnalité sans la modifier explicitement. Eh bien, je comprends si vous êtes encore confus sur ce que sont les décorateurs. Ne vous inquiétez pas – nous avons un outil nommé exemple pour l'expliquer.

Essayons un exemple pour comprendre le décorateur. Il y a deux façons d'écrire un décorateur.

### Méthode 1

Nous déclarons une fonction décorateur et dans les arguments de la fonction, nous attendons que la fonction soit passée comme argument. À l'intérieur, nous écrivons une fonction wrapper où les opérations sont effectuées et elle est retournée.

```python
>>> def my_decorator(func):
...     def wrapper():
...             print("Line Number 1")
...             func()
...             print("Line Number 3")
...     return wrapper
...
>>> def say_hello():
...     print("Hello I am line Number 2")
...
```

Pour appeler la fonction, nous assignons le décorateur avec `say_hello` comme argument.

```python
>>> say_hello = my_decorator(say_hello)
```

Nous pouvons également vérifier la référence en utilisant `say_hello`. Nous obtiendrons la sortie qui nous indique qu'elle a été enveloppée par la fonction `my_decorator`.

```python
<function my_decorator.<locals>.wrapper at 0x10dc84598>
```

Appelons notre fonction `say_hello` :

```python
>>> say_hello()
Line Number 1
Hello I am line Number 2
Line Number 3
```

Voyez la magie, la ligne "Hello I am line Number 2" s'imprime entre la ligne 1 et 3 car l'appel de fonction s'exécute là.

La méthode 1 est maladroite, et à cause de cela, beaucoup de gens préfèrent une approche différente.

### Méthode 2

Ici, notre déclaration de décorateur reste la même, mais nous changeons la façon dont l'appel est assigné à ce décorateur. Quelle que soit la fonction qui nécessite ce décorateur, elle s'enveloppe elle-même avec `@decorator_name`.

```python
>>> def my_decorator(func):
...     def wrapper():
...             print("Line Number 1")
...             func()
...             print("Line Number 3")
...     return wrapper
...
>>> @my_decorator
... def say_hello():
...     print("Hello I am line Number 2")
...
>>> say_hello()
```

La sortie est la même :

```shell
Line Number 1
Hello I am line Number 2
Line Number 3
```

Un décorateur est un outil puissant et il est utilisé dans les scénarios de développement suivants d'une application :

* Configuration du logger

* Configuration de la configuration

* Configuration de la capture d'erreurs

* Extension de la fonctionnalité commune pour toutes les fonctions et classes

## Exceptions :

Lorsque nous apprenions diverses syntaxes, nous avons rencontré diverses erreurs. Ces erreurs se sont produites à cause de la syntaxe. Mais dans une application réelle, les erreurs (ou communément appelées bugs) ne se produisent pas seulement à cause de problèmes de syntaxe, mais aussi à cause d'erreurs réseau ou d'autres causes.

Pour gérer ces problèmes, nous utilisons Try - Except. Dans le bloc `try`, nous écrivons l'expression que nous voulons exécuter, tandis que dans le bloc `except`, nous capturons l'erreur. Le bloc Try-Except ressemble à ceci :

```python
try:
	expression
except:
	catch error
```

Comprenons cela avec un exemple :

```python
>>> try:
...     print(value)
... except:
...     print("Something went wrong")
...
```

Ici, nous essayons d'imprimer la variable value, mais elle n'est pas définie. Donc nous obtenons la sortie suivante :

```shell
Something went wrong
```

Vous pensez peut-être que la ligne "something went wrong" n'est pas très utile. Alors, comment pouvons-nous savoir ce qui n'a pas fonctionné ici ?

Nous pouvons imprimer l'exception et l'utiliser pour découvrir ce qui n'a pas fonctionné. Testons cela dans notre exemple :

```python
>>> try:
...     print(value)
... except Exception as e:
...     print(e)
...
```

Et le résultat est :

```shell
name 'value' is not defined
```

Waouh ! C'est magique. Il me notifie que 'value' n'est pas défini.

Python fournit également un outil nommé `raise`. Supposons que vous ne voulez pas qu'une certaine condition se produise et si elle se produit, vous voulez la lever. Dans une telle condition, vous pouvez utiliser `raise`. Considérez l'exemple ci-dessous :

```python
>>> i = 5
>>> if i < 6:
...     raise Exception("Number below 6 are not allowed")
...
```

La sortie que nous obtenons est la suivante :

```shell
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
Exception: Number below 6 are not allowed
```

Il existe de nombreux sous-types d'exceptions, donc je vous recommande de consulter la [Documentation Python](https://docs.python.org/3/tutorial/errors.html#errors-and-exceptions) pour les comprendre.

## Importation de packages :

Vous avez appris les bases de Python et vous êtes maintenant prêt à construire des applications géniales. Mais attendez – nous manquons encore quelques sujets importants.

Sans l'importation de packages, vous serez obligé d'écrire tout dans un seul fichier. Imaginez le désordre que cela sera.

Créez deux fichiers nommés `main.py` et `hello.py`. Rappelez-vous que les deux fichiers doivent être dans le même répertoire.

Sous `hello.py`, copiez-collez le code suivant :

```python
def say_hello():
    print("Hello world")
```

Sous `main.py`, copiez-collez le code suivant :

```python
import hello

if __name__ == "__main__":
    hello.say_hello()
```

Dans `hello.py`, nous avons déclaré une fonction `say_hello()` qui imprime "Hello world". Dans `main.py`, vous verrez une instruction d'importation. Nous importons le module hello et appelons la fonction `say_hello()` de ce module.

Exécutez notre programme en utilisant la commande suivante :

```shell
[0;34m[0m python main.py
```

Sortie :

```shell
Hello world
```

Maintenant, comprenons comment importer un module qui se trouve dans un autre répertoire.

Créons un répertoire nommé "data" et déplaçons notre `hello.py` à l'intérieur de ce répertoire.

Allez dans `main.py` et changez l'instruction d'importation précédente.

```python
from data import hello

if __name__ == "__main__":
    hello.say_hello()
```

Il y a deux façons d'importer depuis un répertoire.

* Méthode 1 : `from data import hello`

* Méthode 2 : `import data.hello`

Je préfère la méthode 1 pour sa lisibilité. Vous pouvez choisir la méthode qui vous semble la meilleure.

Exécutons notre application en utilisant la commande suivante :

```shell
[0;34m[0m python main.py
```

Et une erreur se produit. Attendez, pourquoi cela s'est-il produit ? Nous avons tout fait correctement. Passons en revue l'erreur :

```shell
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from data import hello
ImportError: No module named data
```

Eh bien, Python nous dit qu'il ne reconnaît pas un module nommé data. Pour résoudre ce problème, créez un `__init__.py` à l'intérieur du répertoire data. Laissez le fichier vide et exécutez le programme à nouveau et vous obtiendrez la sortie suivante :

```shell
Hello world
```

Eh bien, Python ne traite pas par défaut un répertoire comme un module. Pour informer Python de traiter un répertoire comme un module, `__init__.py` est requis.

## Gestion du JSON :

Si vous avez déjà travaillé avec le développement web ou le développement d'applications, vous savez peut-être que tous les appels d'API se font au format JSON. Bien que le JSON ressemble à un dictionnaire en Python, rappelez-vous qu'il est très différent.

Pour gérer le JSON, Python fournit un package intégré `json`. Pour utiliser ce package, nous devons l'importer comme suit :

```python
import json
```

Cette bibliothèque fournit deux méthodes qui nous aident à gérer le JSON. Comprenons-les une par une.

### JSON loads :

Si vous avez une chaîne JSON et que vous souhaitez la convertir en dictionnaire, vous devez utiliser la méthode `loads`. Allez dans le shell Python et copiez-collez le code suivant :

```python
>>> import json
>>> json_string = '{ "user_name":"Sharvin", "age":1000}' #JSON String
>>> type(json_string)
<class 'str'>
>>> data = json.loads(json_string)
>>> type(data)
<class 'dict'>
>>> data
{'user_name': 'Sharvin', 'age': 1000}
```

### JSON dumps :

Maintenant, convertissons nos données au format de chaîne JSON en utilisant la méthode `dumps`.

```python
>>> jsonString = json.dumps(data)
>>> type(jsonString)
<class 'str'>
>>> jsonString
'{"user_name": "Sharvin", "age": 1000}'
```

Pour en savoir plus sur la manipulation du JSON, consultez la [Documentation Python](https://docs.python.org/3/library/json.html).

## C'est tout !

Et nous avons terminé ! J'espère que vous comprenez maintenant les bases de Python. Félicitations ! C'est une énorme réalisation.

Les commentaires sont les bienvenus. De plus, si vous souhaitez apprendre un autre sujet, vous pouvez tweeter le nom du sujet sur Twitter et inclure mon handle Twitter. \[ **@sharvinshah26** \]