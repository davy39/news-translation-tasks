---
title: Comment formater une chaîne de caractères en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-10T17:19:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/How-To-Format-A-String-in-python.jpg
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Comment formater une chaîne de caractères en Python
seo_desc: "By Suchin Ravi\nFormatting a string is something you'll do all the time\
  \ when you're coding in Python. For every variable, tuple, and dictionary and the\
  \ logic that we define, we eventually have to either print or display it in some\
  \ form. \nAnd each of t..."
---

Par Suchin Ravi

Le formatage d'une chaîne de caractères est une opération que vous effectuerez constamment lorsque vous coderez en Python. Pour chaque variable, tuple, dictionnaire et la logique que nous définissons, nous devons finalement soit les imprimer, soit les afficher sous une certaine forme.

Et chacun de ces éléments, sans exception, nécessite que nous formations la sortie requise en une chaîne de caractères avant de pouvoir enfin l'imprimer ou utiliser la fonction pertinente pour afficher la chaîne en Python.

Vous avez peut-être déjà utilisé la fonction `str` et travaillé avec des littéraux de chaîne, mais il y a de nombreuses fois où nous avons besoin de quelque chose de plus. Avec cela à l'esprit, examinons comment nous pouvons formater des chaînes en utilisant différentes techniques de Python3.

# Comment formater une chaîne de caractères en utilisant la concaténation : print('Hello'+name)

Il s'agit de la technique la plus simple – et donc la plus facile – pour commencer. C'est aussi la manière que je préfère pour enseigner à quelqu'un qui vient de commencer à coder.

L'utilisation des portions dans l'ordre littéral et des opérateurs '+' rend cela facile à comprendre sans aucune connaissance préalable en codage.

```python
name = 'YoungWonks'
year = 2014

string = 'Hello, ' + name
print(string)

string = name + ' was started in ' + str(year)
print(string)
```

Voici le résultat :

```bash
Hello, YoungWonks 
YoungWonks was started in 2014
```

L'exemple ci-dessus montre comment nous pouvons joindre des variables en utilisant l'opérateur d'addition pour créer une chaîne formatée. La chose à garder à l'esprit ici est que nous devrons convertir toutes les variables en chaînes. Ici, la variable name est déjà une chaîne et year est un entier.

# Comment formater une chaîne de caractères à l'ancienne : print 'Hello %s' % name

Cette approche était plus souvent utilisée dans Python2, lorsque le langage était encore jeune et en évolution. C'est une technique facile à comprendre pour les codeurs expérimentés qui viennent d'un arrière-plan de programmation C.

Ici, comme vous pouvez le voir dans le code ci-dessous, nous définissons le placeholder avec le type de données spécifié et les argument(s) à la fin de l'instruction. Cela ressemble au langage C (et à d'autres langages aussi).

```python
name = 'YoungWonks'
year = 2014

string = 'Hello, %s ' % name
print(string)

string = '%s was started in %d' % (name, year)
print(string)
```

Et voici le résultat :

```bash
Hello, YoungWonks 
YoungWonks was started in 2014
```

Dans l'exemple ci-dessus, nous définissons les variables que nous voulons formater dans les chaînes. Ensuite, nous créons la chaîne avec les placeholders pour les variables.

Gardez à l'esprit que les placeholders doivent correspondre aux types des variables correspondantes. Nous pouvons lier les variables réelles aux placeholders en utilisant le symbole % à la fin de l'instruction.

# Comment formater une chaîne de caractères en utilisant Format : ''.format()

Il s'agit d'une technique que de nombreux programmeurs Python considèrent comme un bol d'air frais, car elle simplifie les choses pour vous.

Elle a été introduite dans les premières versions de Python3. Essentiellement, la nouvelle syntaxe a supprimé les symboles '%' et a plutôt fourni `.format()` en tant que méthode de chaîne, qui accepte des arguments positionnels pour les substitutions décrites dans les accolades.

Nous pouvons également spécifier des arguments de mot-clé ici, bien que cela puisse sembler un peu verbeux à certains moments.

Il y a plus que vous pouvez faire avec la méthode `str.format`, comme spécifier la précision, l'arrondi et le remplissage avec des zéros. Pour les besoins de cet article, nous nous concentrerons uniquement sur l'utilisation de base.

```python
name = 'YoungWonks'
year = 2014

string = '{} was started in {}'.format(name, year)
print(string)

string = '{0} was started in {1}'.format(name, year)
print(string)

yw = {'name': 'YoungWonks', 'year': 2014}
string = "{name} was started in {year}.".format(name=yw['name'], year=yw['year'])
print(string)
```

Voici le résultat :

```bash
YoungWonks was started in 2014
YoungWonks was started in 2014
YoungWonks was started in 2014
```

Dans l'exemple ci-dessus, nous créons les variables à formater dans la chaîne. Ensuite, sous la forme la plus simple, nous pouvons utiliser {} comme placeholders pour les variables à utiliser. Nous appliquons ensuite la méthode `.format()` à la chaîne et spécifions les variables comme un ensemble ordonné de paramètres.

La deuxième partie de l'exemple utilise les indices des paramètres ordonnés dans les placeholders.

La troisième partie de l'exemple nous montre également comment utiliser un dictionnaire dans le formatage de la chaîne tout en utilisant des paramètres nommés dans la méthode .format.

# Comment formater une chaîne de caractères en utilisant les F Strings : f'hello {name}'

Aussi abrégé en format string, les f strings sont la technique la plus récente que Python3 supporte désormais, donc elles sont adoptées rapidement.

Les f strings abordent la verbosité de la technique `.format()` et fournissent un moyen court de faire la même chose en ajoutant la lettre f comme préfixe à la chaîne. Cette méthode semble avoir le meilleur des deux techniques :

1. L'ordre littéral de la concaténation
2. La modularité de la méthode `.format()`

Grâce à ces avantages, de plus en plus de développeurs semblent l'utiliser. Je pense que cela est également plus simple pour les étudiants à apprendre, et plus facile à adopter si vous êtes encore nouveau dans le codage.

```python
name = 'YoungWonks'
year = 2014
string = f'{name} was started in {year}'
print(string)

string = f'{name} was started in {2013 + 1}.'
print(string)

yw = {'name': 'YoungWonks', 'year': 2014}
string = f"{yw['name']} was started in {yw['year']}."
print(string)
```

```bash
YoungWonks was started in 2014 
YoungWonks was started in 2014.
YoungWonks was started in 2014.
```

Comme vous l'avez peut-être remarqué, l'exemple ci-dessus est similaire à la méthode `.format()`. Ici, nous utilisons les {} pour les placeholders dans les chaînes, mais nous spécifions également les variables directement dans le placeholder.

Cette méthode prend effet lorsque nous utilisons la lettre minuscule `f` au début de la chaîne. Vous pouvez également utiliser cette méthode avec d'autres types de données tels que les dictionnaires.

# Devons-nous connaître et utiliser toutes ces méthodes de formatage de chaînes ?

Toutes ces connaissances sont pertinentes lorsque vous apprenez Python. Même si vous n'utiliserez pas souvent l'ancien style de formatage de chaînes, il existe certains forums plus anciens, des posts Stack Overflow, et de nombreuses bibliothèques d'apprentissage automatique plus anciennes qui utilisent encore ces anciens styles.

Pour cette raison, il est bon de les connaître afin de pouvoir reconnaître ce qui se passe et potentiellement déboguer un problème.

Parmi les trois autres méthodes que nous avons discutées ici, vous pouvez utiliser n'importe laquelle d'entre elles pour formater vos chaînes en Python. Choisissez simplement celle qui fonctionne le mieux en fonction du contexte et même de votre humeur ce jour-là !

Le `+` est utile lorsque vous travaillez avec des instructions rapides et simples. Vous pouvez également l'utiliser pour créer des états de débogage lors du développement d'un projet simple.

Par exemple, si nous devions créer un simple jeu de devinette de nombres, nous pourrions utiliser l'opérateur `+` comme montré ci-dessous :

```python
import random
random_number = random.randint(1,100)
user_guess = None
while True:
	print('Please guess the number between 1 and 100 : ')
    user_guess = int(input())
    if user_guess == random_number:
    	print('Correct!')
    else:
    	print("Try Again!")
        
    #prints for debugging
    print("Random Number: "+ str(random_number))
    print("User Guess: "+ str(user_guess))
```

Les instructions de débogage utilisées dans le code ci-dessus ne resteront pas dans votre code final. (Vous ne voudriez pas donner le nombre à deviner, n'est-ce pas ?) Vous pouvez donc utiliser l'approche de concaténation dans vos impressions lors du développement de votre code.

Lorsque vous ajoutez des instructions de journalisation, vous pouvez préférer les méthodes `.format()` ou `f string` car elles rendront vos instructions plus modulaires. Il sera également plus facile de spécifier la précision/le formatage pour le type de données lui-même.

# Existe-t-il d'autres techniques de formatage de chaînes en Python ?

Oui ! Les chaînes de modèle sont une telle technique qui sont fournies en tant que classe dans le module string de la bibliothèque standard de Python. Elle est importée en tant que module et la méthode `.substitute()` est utilisée pour remplacer les placeholders.

Cela dit, je n'ai jamais eu à utiliser cela dans mes expériences de codage jusqu'à présent et je n'en ai appris que lors de la recherche pour ce blog.

# Conclusion

Le formatage des chaînes de caractères en Python est un outil important au quotidien pour un programmeur Python à connaître. Chaque langage de codage semble formater les chaînes de manière similaire. C'est aussi une partie très importante de la raison pour laquelle nous utilisons des langages de script.

Parmi ces différentes manières de formater les chaînes, il semble que la méthode `f string` soit là pour rester, ainsi que `.format()` et la concaténation. Nous pourrions voir la syntaxe Python2 s'estomper à mesure que la plupart des bibliothèques héritées commencent à supporter Python3.

Voici une [fiche de référence utile](https://www.youngwonks.com/resources/python-cheatsheet) qui contient plus de syntaxe Python de base et également quelques méthodes de chaîne pour votre référence.

# Formatage des chaînes dans d'autres langages

Les autres langages de programmation semblent suivre une syntaxe similaire en ce qui concerne la précision et la représentation, et reposent sur des substitutions de variables. Mais ils diffèrent dans la manière dont ils sortent les chaînes formatées vers la console.

C++ est l'exception visible ici avec la méthode `cout` de la bibliothèque standard. Java, fidèle à sa nature, utilise `System.out.println()`, tandis que JavaScript utilise `console.log()`. Vous trouverez une méthode comparable pour chaque langage.

_Suchin Ravi est un éducateur et technologue, et enseigne l'informatique chez YoungWonks. Il travaille en tant que développeur logiciel principal chez Wonksknow LLC._