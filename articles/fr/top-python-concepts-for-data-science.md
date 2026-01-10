---
title: Principaux concepts Python à connaître avant d'apprendre la science des données
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-08-24T17:53:30.000Z'
originalURL: https://freecodecamp.org/news/top-python-concepts-for-data-science
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/python-data-science-concepts.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: Principaux concepts Python à connaître avant d'apprendre la science des
  données
seo_desc: 'If you''re interested in learning data science, you''ve likely heard the
  buzzword "Python,". It''s a popular programming language often used in data science.

  But Python is a general-purpose programming language. This means that it''s not
  limited to data ...'
---

Si vous êtes intéressé par l'apprentissage de la science des données, vous avez probablement entendu le mot à la mode **"Python"**. C'est un langage de programmation populaire souvent utilisé en science des données.

Mais Python est un langage de programmation polyvalent. Cela signifie qu'il n'est pas limité à la science des données seule. Vous pouvez l'utiliser pour développer des applications web et mobiles, entre autres.

Ainsi, lors de l'apprentissage de Python pour la science des données, l'une des erreurs les plus courantes que font les débutants est de l'apprendre "incorrectement" — c'est-à-dire, ne pas apprendre Python en préparation pour la science des données. Cela peut entraîner une perte de temps et d'efforts.

Dans cet article, nous allons passer en revue les principaux concepts Python que vous devriez connaître avant de vous plonger dans la science des données. Maintenant, détendez-vous et suivez le guide car ce sera un voyage passionnant.

Pour avoir un aperçu rapide de ce que sera ce voyage, voici ce que nous allons couvrir :

* [Entiers et nombres à virgule flottante en Python](#heading-entiers-et-nombres-a-virgule-flottante-en-python)

* [Chaînes de caractères en Python](#heading-chaines-de-caracteres-en-python)

* [Valeurs booléennes en Python](#heading-valeurs-booleennes-en-python)

* [Opérateurs arithmétiques en Python](#heading-operateurs-arithmetiques-en-python)

* [Opérateur de comparaison en Python](#heading-operateur-de-comparaison-en-python)

* [Opérateurs logiques en Python](#heading-operateurs-logiques-en-python)

* [Opérateur d'appartenance en Python](#heading-operateur-dappartenance-en-python)

* [Formatage de chaînes f-string en Python](#heading-formatage-de-chaines-f-string-en-python)

* [Listes en Python](#heading-listes-en-python)

* [Tuples en Python](#heading-tuples-en-python)

* [Dictionnaires en Python](#heading-dictionnaires-en-python)

* [Fonction `Zip()` en Python](#heading-fonction-zip-en-python)

* [Fonction `Enumerate()` en Python](#heading-fonction-enumerate-en-python)

* [Fonction `Counter()` en Python](#heading-fonction-counter-en-python)

* [Instructions If-else en Python](#heading-instructions-if-else-en-python)

* [Fonction `Range()` en Python](#heading-fonction-range-en-python)

* [Compréhension de liste en Python](#heading-comprehension-de-liste-en-python)

* [Fonctions définies par l'utilisateur en Python](#heading-fonctions-definies-par-lutilisateur-en-python)

## Principaux concepts Python à connaître pour la science des données

### Pourquoi ces concepts sont importants à connaître

Pour être franc, ces concepts sont ce dont vous aurez besoin pour démarrer votre voyage en science des données lorsque vous souhaitez utiliser Python comme votre langage pour la science des données. Vous travaillerez avec eux dans votre travail quotidien en tant que scientifique des données, il est donc bon d'avoir une bonne maîtrise de leur fonctionnement.

### Entiers et nombres à virgule flottante en Python

Les nombres sont l'un des concepts les plus fondamentaux en science des données. Et Python contient des représentations (types de données) pour les différents types de nombres qui peuvent exister. Ceux-ci sont principalement classés en :

* Entiers : ce sont des nombres entiers qui sont soit positifs soit négatifs en Python. Les exemples incluent 200, -100, 67, et ainsi de suite.

* Nombres à virgule flottante : ce sont des valeurs décimales qui sont soit positives soit négatives. Les exemples incluent 200.65, -14.34, 53.0002, et ainsi de suite.

### Chaînes de caractères en Python

En Python, les chaînes de caractères contiennent des valeurs alphanumériques qui sont généralement enfermées dans des guillemets simples ou doubles.

Un exemple inclut `"FreeCodeCamp a beaucoup de ressources riches"`.

Python a beaucoup de méthodes que vous pouvez utiliser pour manipuler les chaînes de caractères. Par exemple, si vous souhaitez convertir une chaîne de caractères de majuscules en minuscules, vous pouvez utiliser la méthode `.lower()` en Python comme montré ci-dessous.

```python
string = "FREECODECAMP IS COOL"
print(string.lower())
>>> 'freecodecamp is cool'
```

Vous travaillez souvent avec des chaînes de caractères en science des données pour créer ou manipuler des données textuelles dans votre ensemble de données.

Pour en savoir plus sur les chaînes de caractères et leurs méthodes, [consultez ce manuel utile](https://www.freecodecamp.org/news/python-string-manipulation-handbook/).

### Valeurs booléennes en Python

Les valeurs booléennes sont également connues sous le nom de valeurs binaires. Ce sont des valeurs représentées par deux nombres. `True et False`, ou `0 et 1`.

### Opérateurs arithmétiques en Python

Vous utilisez les opérateurs arithmétiques pour effectuer des opérations mathématiques sur deux opérandes ou valeurs numériques. Ils incluent les suivants :

* Le symbole plus `+` représente l'addition.

* Le symbole tiret `-` représente la soustraction

* Le symbole astérisque `*` représente la multiplication.

* Le symbole barre oblique `/` représente la division.

* Le symbole pourcentage `%` est [utilisé pour exprimer le modulus](https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/)

* Le symbole double astérisque `**` représente un exposant.

* Le symbole double barre oblique `//` représente la division entière.

Les quatre premiers opérateurs sont assez simples car nous les utilisons au quotidien. Cependant, les suivants nécessitent un peu plus d'explications :

#### Qu'est-ce que l'opérateur modulus ?

L'opérateur modulus (`%`) retourne le reste lors de l'opération sur deux nombres distincts. Par exemple, 8 % 3 retournera 2 puisque 3 ne peut entrer dans 8 que deux fois, laissant un reste de 2.

#### Qu'est-ce que l'opérateur exponentiel ?

Vous utilisez l'opérateur exponentiel `**` pour élever un nombre à la puissance d'un autre. Par exemple, `2**3` est égal à 8, car 2 est élevé (ou multiplié par lui-même) trois fois : `2*2*2 = 8`

#### Qu'est-ce que l'opérateur de division entière ?

Vous utilisez l'opérateur de division entière `/` pour diviser. Mais contrairement aux autres opérateurs de division qui produisent un nombre décimal, la division entière retourne la partie entière de la division.

Par exemple, `5//2` donnera 2 (car 2 entre dans 5 deux fois de manière égale). La division entière n'approximera pas aussi bien.

#### Comment effectuer des opérations arithmétiques sur une chaîne de caractères

De plus, vous pouvez également effectuer des opérations arithmétiques sur une chaîne de caractères. L'addition et la multiplication sont deux opérations arithmétiques que vous pouvez effectuer sur une chaîne de caractères.

* Opérateur d'addition `+` : vous utilisez l'opérateur d'addition pour concaténer deux opérandes de chaîne ensemble (c'est-à-dire, vous joignez deux chaînes ensemble). Par exemple :

```python
"Folks" + "connect" 
>>> "Folksconnect"
```

* Opérateur de multiplication `*` : vous utilisez l'opérateur de multiplication pour répéter une chaîne de caractères (mais notez que l'un des opérandes doit être un nombre). Par exemple :

```python
2 * "Folks" 
>>> "FolksFolks"
```

### Opérateur de comparaison en Python

Vous utilisez les opérateurs de comparaison pour comparer deux opérandes. Lorsque les opérateurs de comparaison sont effectués sur deux opérandes, ils retournent une valeur booléenne de vrai ou faux. Les opérateurs de comparaison incluent :

* Signe supérieur à `>`

* Signe inférieur à `<`

* Signe égal `==`

* Signe différent `!=`

* Supérieur ou égal à `>=`

* Inférieur ou égal à `<=`

Voici quelques exemples : `2==2` donnera `True`. De même, `5>= 5` donnera `True` puisque 5 est également égal à 5.

### Opérateurs logiques en Python

Vous utilisez les opérateurs logiques pour combiner des instructions conditionnelles. Ils incluent `and`, `or` et `not`.

Par exemple, `4<5` et `3>2` retourneront `True`, car `4 <5` est une condition qui est vraie et `3 > 2` est une autre condition qui est également vraie. Donc `True` et `True` selon la porte logique donneront vrai.

Avant de continuer, je veux définir un terme que j'utiliserai principalement dans le reste de l'article — les itérables. Un itérable est essentiellement quelque chose qui consiste en une séquence de valeurs, par exemple des caractères, des nombres et ainsi de suite. Les itérables incluent les chaînes de caractères, les listes, les dictionnaires, les plages, les tuples, et ainsi de suite en Python.

### Opérateur d'appartenance en Python

Vous utilisez l'opération d'appartenance pour déterminer si une valeur appartient à une séquence/itérable. Une séquence peut être une chaîne de caractères, une liste de nombres, ou autre chose.

L'opérateur d'appartenance inclut l'opérateur `in` et l'opérateur `not in`.

Par exemple, disons que je veux vérifier si le caractère `b` est dans la chaîne de caractères `"What a time to be alive"` — je peux faire cela en tapant l'instruction suivante et le résultat sera une valeur booléenne.

```python
"b" in "what a time to be alive"


>>> True
```

Pour en savoir plus sur les opérateurs en Python, consultez [ces](https://www.freecodecamp.org/news/basic-operators-in-python-with-examples/) [articles](https://www.freecodecamp.org/news/operators-in-python-how-to-use-logical-operators-in-python/).

### Formatage de chaînes f-string en Python

Dans certains cas, vous pouvez vouloir insérer une valeur de variable dans une chaîne de caractères. Supposons que vous ne connaissez pas la valeur à l'avance mais que vous voulez qu'elle soit dans une chaîne de caractères. Le formatage de chaînes peut vous aider à y parvenir.

Il existe plusieurs façons de formater des chaînes de caractères en Python, mais nous allons nous concentrer sur l'une d'entre elles : le format f-littéral.

Regardons un exemple : j'ai deux variables, nom et âge, et je veux les inclure dans une chaîne de caractères puis imprimer toute la chaîne.

```python
age = 10
name = "Eagle"

string = f"Il y a certains oiseaux de proie comme {name} qui sont plus âgés que {age} ans."

print(string)

>>> Il y a certains oiseaux de proie comme Eagle qui sont plus âgés que 10 ans.
```

Donc, la première chose à faire est d'ajouter un f au début de la chaîne que vous souhaitez formater en utilisant le f-littéral. De plus, la variable que vous souhaitez formater doit être à l'intérieur d'accolades.

Pour en savoir plus sur le formatage de chaînes en utilisant les f-littéraux, consultez cet article de [Bala Priya qui l'explique](https://www.freecodecamp.org/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/). De plus, vous pouvez en savoir plus sur d'autres types de formatage de chaînes [ici](https://www.geeksforgeeks.org/string-formatting-in-python/).

### Listes en Python

Vous utilisez les listes pour stocker ou organiser des données dans un ordre séquentiel. Ces données peuvent être une chaîne de caractères, des nombres, ou des itérables comme une liste.

Une liste est également mutable, ce qui signifie qu'elle peut s'étendre et changer après que vous l'ayez déclarée (vous ajoutez de nouveaux éléments à celle-ci).

En Python, vous pouvez créer une liste avec des crochets et ensuite l'enregistrer dans une variable. Par exemple :

```python
lst_of_num = [2, 3, 4, 2].
```

Comme nous pouvons le voir, ce qui précède est une liste de nombres. La beauté d'une liste est qu'elle vous permet d'avoir des valeurs en double dans la liste. Comme mentionné précédemment, vous pouvez créer une liste de différents types de données, comme une liste de nombres, de chaînes de caractères et de listes.

```python
diverse_lst = [4, "Folks", ["2", 4, 6, 7]]
```

Pour accéder à un élément ou un élément de liste, vous utilisez l'indexation. En Python, le premier élément de tout itérable est toujours à la position d'index zéro. En d'autres termes, la position d'une liste commence par 0. Par exemple, les éléments de la variable `lst_of_number` dans l'index ou la position suivante.

```python
lst_of_num = [2, 3, 4, 2]. 

2 -- index ou position 0
3 -- index ou position 1
4 -- index ou position 2
2 -- index ou position 3
```

Vous pouvez accéder à un élément de liste en utilisant l'approche suivante :

`name_of_list[index ou position]`

Pour notre cas, si vous voulez accéder à l'élément à la 3ème position, vous pouvez le faire en tapant :

```python
print(lst_of_num[3])
>> 2
```

Les listes sont vos amies que vous utiliserez beaucoup en science des données. Vous en aurez besoin lorsque vous souhaitez avoir une séquence de valeurs dans un conteneur.

Pour apprendre à ajouter, supprimer ou mettre à jour une liste, consultez ce tutoriel utile de Ihechikara Vincent Abba sur [comment faire une liste en Python](https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/).

### Tuples en Python

Un tuple est un autre type de collection de données en Python. Vous l'utilisez également pour stocker et organiser des données sous la forme d'une liste.

La seule différence est qu'il est immutable, ce qui signifie qu'il ne peut pas s'étendre (vous ne pouvez pas ajouter de nouveaux éléments à celui-ci) comme une liste.

En Python, vous pouvez créer un tuple en utilisant des parenthèses.

```python
my_tuple = (2, 3, 5) # C'est un tuple de nombres.

Un tuple peut également contenir différents types de données :

diverse_tuple = (2, "Golang", [4, 5, 2], ("jour", "nuit"))
```

Pour accéder aux éléments d'un tuple, vous faites la même chose que pour une liste :

```python
my_tuple[2]
>>> 5
```

Lorsque vous avez besoin d'une collection Python à laquelle vous n'avez pas besoin d'ajouter de nouveaux éléments une fois qu'elle est créée, les tuples sont pratiques.

Si vous voulez en savoir plus sur les tuples, consultez cet [article](https://www.w3schools.com/python/python_tuples.asp). De plus, si vous voulez en savoir plus sur les différences entre les listes et les tuples, consultez [cet article utile de Dionysia Lemonaki qui l'explique](https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/).

### Dictionnaires en Python

Un dictionnaire est une collection Python qui stocke des données sous forme de paires clé-valeur. Vous pouvez créer un dictionnaire en utilisant des accolades. Les dictionnaires sont également mutables. Par exemple :

```python
my_dict = {"names":["Grace", "Dave", "Jack"], "scores":[45, 56, 70]}
```

La valeur avant la colonne est appelée la clé et ne peut contenir que des types de données immutables tels que des chaînes de caractères, des entiers ou des tuples. La valeur après la colonne est simplement appelée une valeur et peut contenir des types de données mutables et immutables comme des listes, des dictionnaires, et ainsi de suite.

Vous pouvez accéder aux valeurs d'un dictionnaire via les clés. Par exemple, disons que je veux obtenir le nom d'un étudiant à partir du dictionnaire ci-dessus. Je peux facilement le faire en utilisant les clés, comme ceci :

```python
print(my_dict["names"])
>>> ["Grace", "Dave", "Jack"]
```

Vous aurez souvent besoin de dictionnaires pour les tâches liées aux paires clé-valeur ou lorsque vous souhaitez transformer quelque chose en une série/dataframe dans Pandas (une bibliothèque avec laquelle vous travaillerez principalement pour la manipulation de données).

Pour en savoir plus sur les dictionnaires et comment ajouter, mettre à jour ou supprimer d'un dictionnaire, consultez [ce tutoriel utile de Dionysia Lemonaki qui les explique](https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/). Voici également un [article utile de Kolade Chris sur les dictionnaires](https://www.freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python/).

### Fonction `Zip()` en Python

Vous utilisez la fonction zip pour combiner deux itérables tels qu'une liste, un tuple, un dictionnaire, et ainsi de suite. Et chaque élément de chaque itérable est apparié ensemble.

En d'autres termes, le premier élément du premier itérable est apparié avec le premier élément du second itérable. Vous utilisez généralement la fonction zip pour fusionner deux listes ou tuples en un dictionnaire. Voyons comment cela se passe.

Disons que j'ai une liste qui contient le nom d'un étudiant et une autre liste qui contient le score de chaque étudiant. Maintenant, si je veux mapper le nom de chaque étudiant à son score respectif, je peux le faire en utilisant la fonction zip.

```python
name = ["Dave", "Jerry", "Sasha"]
score = [43, 56, 78]
result = zip(name, score)
```

Maintenant, nous avons terminé — mais si vous imprimez le résultat du code ci-dessus, c'est toujours un objet Iterator. La dernière chose que nous devons faire est d'utiliser une fonction dict — que vous utilisez pour convertir un itérable en un dictionnaire.

```python
print(dict(result)
>>> {"Dave":43, "Jerry":56, "Sasha":78}
```

Vous utiliserez souvent la fonction `zip()` pour joindre une liste en un dictionnaire en science des données.

Pour en savoir plus sur la fonction `zip()`, consultez ce tutoriel utile de Ihechikara Vincent Abba [ici](https://www.freecodecamp.org/news/python-zip-zip-function-in-python/).

### Fonction `Enumerate()` en Python

En Python, vous utilisez la fonction enumerate pour assigner ou apparier des valeurs d'index ou de position aux valeurs d'un itérable (rappelons que les valeurs d'index commencent à 0).

Une fois que ces valeurs d'index sont appariées aux valeurs de l'itérable, vous pouvez décider de les transformer en un dictionnaire où les valeurs d'index serviront maintenant de clé pour les valeurs de l'itérable.

Regardons un exemple pour voir comment cela fonctionne.

```python
lst = ["Free", "Code", "Camp"]
result = dict(enumerate(s))
print(result)
>>> {0: 'Free', 1: 'Code', 2: 'Camp', 3: 'Code'}
```

Vous utiliserez souvent la fonction `Enumerate()` pour assigner un index à une liste et ensuite la transformer en un dictionnaire.

### Fonction `Counter()` en Python

La fonction counter, comme son nom l'indique, vous permet de compter le nombre de fois où les valeurs d'un itérable se produisent.

La fonction counter produit un objet counter sous la forme d'un dictionnaire. Pour utiliser le counter(), nous devons l'importer depuis le module collection. Voyons comment cela fonctionne.

```python
from collections import Counter
lst = ["Free", "Code", "Camp", "Code", "Free"]
print(Counter(lst))
>>> Counter({'Free': 2, 'Code': 2, 'Camp': 1})
```

Vous utiliserez souvent la fonction `Counter` lors de l'exécution du traitement du langage naturel en science des données.

### Instructions If-else en Python

Vous utilisez les instructions if-else lorsque vous souhaitez exécuter une tâche basée sur une certaine condition. Dans la vie réelle, par exemple, si vous réussissez votre examen, vous serez promu. Mais si vous échouez, vous devrez le repasser afin d'être promu.

Il s'avère que ce type d'expression peut également être exécuté en Python en utilisant l'instruction if-else. Voici comment vous écrivez une instruction if else :

```python
if condition:
	execute statement
else:
	execute statement
```

Dans notre exemple d'examen, la condition pour l'expression ci-dessus est de savoir si vous réussissez ou non, et l'instruction exécutable est de savoir si vous réussissez ou non.

Maintenant, ce que fait l'expression ci-dessus est que si la condition est évaluée à vrai, l'instruction exécutable à l'intérieur du bloc if est exécutée. Si la condition n'est pas vraie, l'instruction exécutable à l'intérieur du bloc else est exécutée.

Passons en revue un exemple pour que nous puissions comprendre ce dont nous venons de parler.

Supposons que j'ai une liste de nombres comme `[4, 5, 6, 8, 10]`, et j'ai une variable `i` avec la valeur `6`. Maintenant, j'ai besoin d'écrire une instruction if-else qui imprimera si `i` est dans la liste ou non.

Comme vous pouvez vous y attendre, notre condition sera de savoir si `i` est dans la liste ou non, et notre instruction exécutable sera d'imprimer un message pour nous. Vous pouvez faire cela en utilisant le code fourni ci-dessus comme ceci :

```python
lst = [4, 5, 6, 8, 10]
i = 6

if i in lst:
	print("Oui 6 est présent dans la liste")
else:
	print("Non 6 n'est pas présent dans la liste")
    
>>> "Oui 6 est présent dans la liste"
```

Le `i in lst` est l'instruction conditionnelle qui évalue `True` ou `False`. Si `i` n'était pas présent dans la liste, alors l'instruction exécutable dans le bloc else serait imprimée.

Vous aurez souvent besoin d'instructions if-else pour effectuer des opérations conditionnelles en science des données.

Pour en savoir plus sur les instructions if-else, consultez cet article écrit par Dionysia Lemonaki qui [explique simplement les instructions if-else en Python](https://www.freecodecamp.org/news/python-else-if-statement-example/).

### Fonction `Range()` en Python

La fonction range, comme son nom l'indique, fournit une séquence de valeurs dans une plage spécifique lorsque cela est nécessaire. Elle fonctionne essentiellement comme ceci : (début, fin-1). C'est-à-dire qu'elle n'inclura pas la dernière valeur.

Donc, disons que je veux une liste de nombres allant de 2 à 10. Je peux facilement le faire avec la fonction range puis convertir le résultat en une liste au lieu de créer une liste et de taper ces éléments. Par exemple :

```python
# rappelez-vous que c'est fin-1 donc il affichera les valeurs de 2 à 10
no_range = range(2, 11)
print(list(no_range))
>>> [2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Vous aurez souvent besoin de la fonction `range()` lorsque vous avez besoin d'obtenir une liste de nombres avec une longue plage en science des données.

Pour en savoir plus sur la fonction range, consultez ce tutoriel utile de Bala Priya [ici](https://www.freecodecamp.org/news/python-range-function-explained-with-code-examples/).

### Boucles For en Python

L'instruction de boucle for vous permet de répéter une tâche un nombre de fois prédéfinies. La syntaxe d'une boucle for ressemble essentiellement à ceci :

```python
for i in iterable:
	execute statement
    
   
où i est une variable (vous pouvez changer son nom en ce que vous préférez) qui sert de place holder pour accéder à tous les éléments de l'itérable (par exemple dictionnaire, liste, chaîne, etc.)
```

Supposons que j'ai une liste contenant les noms de milliers d'étudiants et que je veux imprimer ces noms. Maintenant, au lieu de le faire manuellement (où j'accède aux noms dans la liste par indexation comme `print(names[10])` jusqu'au 1000ème élément), je peux facilement employer une boucle for puisque je veux effectuer la même tâche de manière répétée.

Par exemple :

```python
lst  = ["Free", "Code", "Camp", "is", "the", "best", "place", "to", "learn"]
for i in lst:
	print(i)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-123.png align="left")

Vous aurez souvent besoin de boucles for en science des données pour itérer à travers un itérable et effectuer certaines tâches.

Nous pouvons voir que la variable `i` sert de place holder pour accéder à chaque élément de la liste. Pour en savoir plus sur les boucles for et toutes leurs applications, consultez ce tutoriel utile de Kolade Chris [ici](https://www.freecodecamp.org/news/python-for-loop-example-how-to-write-loops-in-python/).

### Compréhension de liste en Python

Une compréhension de liste est une méthode simple de génération d'une nouvelle liste à partir d'un autre itérable en utilisant des opérations spécifiques.

Supposons que j'ai un tuple avec certaines valeurs et que je veux créer une nouvelle liste à partir de celui-ci qui ne contient que les valeurs du tuple qui peuvent être divisées par 3.

Une méthode consiste à créer une liste vide puis à utiliser une boucle for pour itérer à travers tous les éléments du tuple. Vous créez également une instruction if-else pour correspondre à la condition que vous souhaitez et ensuite ajouter les valeurs qui correspondent à cette condition à la liste vide que vous avez initialisée. Voici à quoi cela ressemble en code :

```python
my_tuple = (2, 3, 4, 6, 10, 12)
my_new_lst = []
for i in my_tuple:
	if i % 3 == 0:
    	my_new_lst.append(i)
print(my_new_lst)
>>> [3, 6, 12]
```

Je peux également le faire en utilisant la compréhension de liste en une seule ligne de code. Voyons comment cela se fait :

```python
my_tuple = (2, 3, 4, 6, 10, 12)

my_new_lst = [i for i in my_tuple if i % 3 == 0]
print(my_new_lst)

>>>[3, 6, 12]
```

Jusqu'à présent, nous avons vu que la compréhension de liste ressemble à la ligne de code ci-dessus.

Pour commencer, nous utilisons la boucle for pour itérer à travers le tuple, avec `i` agissant comme un place holder pour chaque élément du tuple. Maintenant, `i` sera évalué pour voir si la condition est remplie (c'est-à-dire pour chaque élément que `i` représente dans le tuple). Donc si la condition `i` est évaluée à vrai, `i` sera ajouté à la nouvelle liste créée.

Vous aurez souvent besoin de la compréhension de liste en science des données lorsque vous avez besoin d'une manière simple de créer une nouvelle liste à partir d'une liste existante.

Pour en savoir plus sur la compréhension de liste, consultez ce tutoriel utile de Dionysia Lemonaki [ici](https://www.freecodecamp.org/news/list-comprehension-in-python-with-code-examples/).

### Fonctions définies par l'utilisateur en Python

Définies par l'utilisateur signifie des fonctions que vous créez vous-même à partir de zéro.

Vous utilisez des fonctions pour modulariser ou regrouper une grande quantité de code en morceaux plus petits. Les fonctions sont utiles lorsque vous devez exécuter un ensemble de code de manière répétée. Au lieu de taper ce code encore et encore chaque fois que vous en avez besoin, vous pouvez facilement le modulariser en une fonction puis appeler la fonction (qui est simplement une instruction d'une ligne) chaque fois que vous en avez besoin.

En Python, vous créez une fonction de la manière suivante.

```python
def function_name(parameter1, parameter2, ....):
	
    //execute statement
    
    return value
```

* `Parameter` dans la fonction sert de place holder pour contenir toute valeur que vous souhaitez passer à l'intérieur de l'instruction exécutable de la fonction. Vous pouvez avoir plus d'un paramètre en fonction de ce que vous souhaitez réaliser.

* `Execute statement` signifie le code que vous souhaitez exécuter chaque fois que vous appelez la fonction.

* `return` est un mot-clé. Il n'est pas obligatoire pour une fonction de retourner une valeur. Vous pouvez décider de ne rien retourner.

Regardons un exemple de la façon d'écrire une fonction. Par exemple, supposons que vous voulez exécuter un code Python qui demande le nom et l'âge d'une personne. Vous voulez également créer une instruction conditionnelle qui imprime un message basé sur l'âge de la personne.

Maintenant, vous souhaitez exécuter ce code encore et encore car vous voulez l'essayer sur différentes personnes. Vous pouvez facilement écrire une fonction qui regroupera ce code en un morceau, que vous pourrez ensuite appeler chaque fois que vous en avez besoin.

```python
def print_func(person_name, person_age):
    if person_age > 10:
        print(f"Salut {person_name} tu as plus que ton âge dénaire et ton nom contient {len(person_name)} caractères.")
    else:
         print(f"Salut {person_name} tu es encore dans ton âge dénaire et ton nom contient {len(person_name)} caractères.")
```

Maintenant, passons en revue ce que nous avons ci-dessus. Nous avons créé une fonction nommée `print_func` qui nécessite deux paramètres que nous voulons lui passer : ils sont `person_name` et `person_age`.

De plus, l'instruction exécutable est l'instruction if-else que nous avons créée à l'intérieur, qui imprimera un message si l'âge d'une personne est supérieur à 10 et un autre message si ce n'est pas le cas.

Vous pouvez voir que nous utilisons le formatage de chaînes pour imprimer le nom de la personne et la longueur du nom de la personne. De plus, nous avons décidé de ne rien retourner puisque nous voulons simplement imprimer une valeur dans la console.

Maintenant, si vous souhaitez appeler cette fonction, vous l'appellerez avec son nom et les paramètres qu'elle nécessite. Dans notre cas, elle nécessite un nom et un âge.

```python
name = "Ibrahim"
age = 12
print_func(name, age)

>>> Salut Ibrahim tu as plus que ton âge dénaire et ton nom contient 7 caractères.
```

Vous aurez souvent besoin de fonctions pour modulariser votre code en science des données.

Pour en savoir plus sur la création de fonctions, consultez ce tutoriel utile sur les fonctions pour débutants de Bala Priya [ici](https://www.freecodecamp.org/news/functions-in-python-a-beginners-guide/). Consultez également celui de Dionysia Lemonaki sur la façon de déclarer et d'invoquer des fonctions avec des paramètres [ici](https://www.freecodecamp.org/news/python-function-examples-how-to-declare-and-invoke-with-parameters-2/).

## Conclusion

Nous sommes arrivés à la fin de ce long voyage. Vous vous demandez peut-être si vous devriez apprendre des sujets avancés comme la programmation orientée objet (POO), qui inclut des concepts comme les classes, avant d'apprendre la science des données.

Pour répondre directement à votre question, ce n'est pas nécessaire. La majorité de votre travail en science des données tournera autour de ces concepts que nous avons discutés dans ce tutoriel, et vous utiliserez principalement des fonctions pour modulariser votre code.

Néanmoins, à mesure que vos connaissances grandissent, il est utile d'apprendre la POO au cas où vous devriez contribuer à un projet open source.

Merci d'avoir pris le temps de lire cet article. J'espère que vous avez appris une chose ou deux.