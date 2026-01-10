---
title: Cours accéléré de Python pour les non-programmeurs Python - Comment commencer
  rapidement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T14:44:27.000Z'
originalURL: https://freecodecamp.org/news/python-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Python-language.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: beginners guide
  slug: beginners-guide
- name: code newbie
  slug: code-newbie
- name: coding
  slug: coding
- name: Python
  slug: python
- name: Python 3
  slug: python3
- name: Tutorial
  slug: tutorial
seo_title: Cours accéléré de Python pour les non-programmeurs Python - Comment commencer
  rapidement
seo_desc: 'By Srebalaji Thirumalai

  This article is for people who already have experience in programming and want to
  learn Python quickly.

  I created this resource out of frustration when I couldn''t find an online course
  or any other resource that taught Python ...'
---

Par Srebalaji Thirumalai

Cet article s'adresse aux personnes qui ont déjà de l'expérience en programmation et qui souhaitent apprendre Python rapidement.

J'ai créé cette ressource par frustration lorsque je n'ai pas pu trouver un cours en ligne ou toute autre ressource qui enseignait Python aux programmeurs qui connaissaient déjà d'autres langages de programmation.

Dans ce cours, je vais couvrir toutes les bases de Python (des leçons approfondies seront ajoutées plus tard) afin que vous puissiez commencer avec le langage très rapidement.

## Table des matières

* Installation de l'environnement
* Hello World
* Chaînes de caractères
* Nombres
* Float
* Bool
* Liste
* Tuple
* Sets
* Dictionnaire
* if..else
* Boucles
* Fonctions
* Classes
* Modules
* Valeurs Truthy et Falsy
* Gestion des exceptions

## Installation de l'environnement

Pour commencer, installez Python 3. Je recommande d'utiliser VSCode comme éditeur. Il dispose de nombreuses extensions à configurer afin que vous puissiez configurer votre environnement en quelques minutes seulement.

## Hello world

```
print("Hello world")

```

Si vous connaissez déjà les bases de la programmation, vous savez probablement comment exécuter ce programme :P. Enregistrez le programme avec l'extension `.py`. Ensuite, exécutez `python hello.py` ou `python3 hello.py`.

Dans ce tutoriel, nous allons suivre `python3`. `python2` sera abandonné en 2020. Je pense donc qu'il est bon d'utiliser la dernière version.

## Variables et types de données

Les variables peuvent contenir des lettres, des nombres et des traits de soulignement.

### Chaînes de caractères

```python
# Ceci est un commentaire en Python
msg_from_computer = "Hello" # Chaîne de caractères
another_msg ='Hello in single quote' # Ceci est également une chaîne de caractères.

print(msg_from_computer + " World..!")

# Type retournera le type de données.
print(type(msg_from_computer)) # <type 'str'>. Nous verrons l'explication de ceci plus tard.

```

### Nombres

```python
2
2 * 3
2 ** 7
(2 + 3) * 4

```

### Floats

```python
2.7

0.1 + 0.2 # 0.3
2 * 0.1 # 0.2

```

Faites attention à la concaténation :

```python
count = 5

print("I need" + count + "chocolates") # Cette ligne générera une erreur. Comme count est un entier, vous devez le convertir en chaîne de caractères.

print("I need" + str(count) + "chocolates") # Cela fonctionnera

```

### Bool

```python
True # La première lettre est en majuscule

False

bool("some value") # Retourne True

bool("") # Retourne False

bool(1) # Retourne True


```

### Liste

Les listes sont essentiellement comme des tableaux. Dans le monde Python, on les appelle `List`. Et elles sont ordonnées.

```python
numbers = ["one", "two", "three"]

numbers[0] # one

numbers[-1] # three. C'est génial. Si nous passons une valeur négative, Python commencera par la fin.

numbers[-2] # two

len(numbers) # 3. Cela retourne simplement la longueur

numbers.append("four") # Append ajoutera l'élément à la fin. ["one", "two", "three", "four"]

numbers.insert(1, "wrong_one") # Insert insérera la valeur particulière à la position appropriée. ["one", "wrong_one", "two", "three", "four"]

# Supprimer une valeur est un peu étrange
del numbers[1] # Supprimera la valeur à la position appropriée. "one", "two", "three", "four"]

# Pop vous aidera à supprimer le dernier élément d'un tableau
popped_element = numbers.pop()

print(popped_element) # four
print(numbers) # ["one", "two", "three"]

# Supprimer des éléments par valeur
numbers.remove("two") # ["one", "three"]. Cela supprimera uniquement la première occurrence d'un tableau.

# Tri
alpha = ["z", "c", "a"]
alpha.sort()
print(alpha) # ["a", "c", "z"] Le tri est permanent. maintenant `alpha` est trié de manière permanente

alpha.sort(reverse=True)
print(alpha) #["z", "c" , "a"] Tri inverse.

alpha = ["z", "c", "a"]
print(sorted(alpha)) # ["a", "c", "z"] Cela retournera simplement le tableau trié. Il ne sauvegardera pas le tableau trié dans la variable elle-même.

print(alpha) # ["z", "c", "a"] Comme vous pouvez le voir, il n'est pas trié

# Inverser un tableau
nums = [10, 1, 5]
nums.reverse()
print(nums) # [5, 1, 10] Cela inverse simplement un tableau. Cela signifie qu'il lit depuis la fin. Ce n'est pas un tri. Cela change simplement l'ordre chronologique.

# Découper des éléments
alpha = ['a', 'b', 'c', 'd', 'e']
alpha[1:3] # ['b', 'c']. Le premier élément est l'index de départ. Et Python s'arrête à l'élément avant le deuxième index.
alpha[2:5] # ['c', 'd', 'e']

alpha[:4] # [ 'a', 'b', 'c', 'd'] Dans ce cas, le premier index n'est pas présent, donc Python commence depuis le début.

alpha[:3] # ['a', 'b', 'c']

alpha[3:] # ['d', 'e'] Dans ce cas, le dernier index n'est pas présent. Il parcourt donc jusqu'à la fin de la liste.

alpha[:] # ['a', 'b', 'c', 'd', 'e'] Il n'y a pas d'index de début ou de fin. Vous savez donc ce qui se passe. Et cela vous aide à copier l'ensemble du tableau. Je pense que je n'ai pas besoin d'expliquer que si vous copiez le tableau, alors tout changement dans le tableau original n'affectera pas le tableau copié.

another_alpha = alpha # Cela ne copie pas le tableau. Tout changement dans alpha affectera également another_alpha.

```

### Tuples

Les tuples sont comme des listes mais ils sont **immuables**. Cela signifie que vous ne pouvez pas les ajouter ou les mettre à jour. Vous pouvez simplement lire les éléments. Et rappelez-vous, comme les listes, les tuples sont également séquentiels.

```python
nums = (1, 2, 3)

print(nums) # (1, 2, 3)

print(nums[0]) # 1

print(len(nums)) # 3

empty_tuple = () # tuple vide. La longueur est zéro.

num = (1, ) # Notez la virgule finale. Lors de la définition d'un seul élément dans le tuple, pensez à ajouter une virgule finale.

num = (1)
print(type(num)) # <type 'int'> Il ne retournera pas un tuple. Parce qu'il n'y a pas de virgule finale.

# Créer un nouveau tuple à partir du tuple existant
nums = (1, 2, 3)
char = ('a', )
new_tuple = nums + char
print(new_tuple) # (1, 2, 3, 'a')

```

### Sets

Les sets sont des collections non ordonnées sans éléments dupliqués.

```python
alpha = {'a', 'b', 'c', 'a'}

print(alpha) # set(['a', 'c', 'b']) Comme vous pouvez le voir, les doublons sont supprimés dans les sets. Et la sortie n'est pas ordonnée.

# Accéder aux éléments dans un set
# Vous ne pouvez pas accéder par index car les sets sont non ordonnés. Vous pouvez y accéder uniquement par boucle. Ne vous inquiétez pas pour la boucle for, nous l'approfondirons dans la section suivante.
for ele in alpha:
  print(ele)

# Pour ajouter un élément au set
alpha.add('s')

# add peut être utilisé pour insérer un seul élément. Si vous voulez plusieurs éléments, alors update sera pratique
alpha.update(['a', 'x', 'z']) # set(['a', 'c', 'b', 'x', 'z']) Souvenez-vous que les doublons sont supprimés.

# Longueur de alpha
len(alpha) # 5

# Supprimer l'élément du set
alpha.remove('a')
alpha.discard('a') # Il est plus sûr d'utiliser discard que remove. Discard ne générera jamais d'erreur même si l'élément n'est pas présent dans le set, mais remove le fera.


```

### Dictionnaires

Les dictionnaires sont des mappages clé-valeur en Python. Ils sont non ordonnés.

```python
user = {'id': 1, 'name': 'John wick', 'email': 'john@gmail.com'}

user['id'] # 1
user['name'] # John wick

# Longueur du dictionnaire
len(user) # 3

# Ajouter une nouvelle paire clé-valeur
user['age'] = 35

# Pour obtenir toutes les clés
keys = user.keys() # ['id', 'name', 'email', 'age']. Cela retournera une liste.

# Pour obtenir toutes les valeurs
values = user.values() # [1, 'John wick', 'john@gmail.com']

# Pour supprimer une clé
del user['age']

# Exemple de dictionnaire imbriqué.
user = {
  'id': 1,
  'name': 'John wick',
  'cars': ['audi', 'bmw', 'tesla'],
  'projects': [
    {
      'id': 10,
      'name': 'Project 1'
    },
    {
      'id': 11,
      'name': 'Project 2'
    }
  ]
}

# Nous verrons comment parcourir le dictionnaire dans la section de la boucle for.

```

## if..else

Vous savez probablement déjà comment fonctionne l'instruction `if..else`. Mais voyons un exemple ici :

```python
a = 5
b = 10

# Voyez l'indentation. Les indentations sont très importantes en Python. Python générera une erreur si les indentations ne sont pas correctes.
if a == 5:
  print('Awesome')

# and est équivalent à && 
if a == 5 and b == 10:
  print('A est cinq et b est dix')

# instruction if else. C'est la même chose que dans la plupart des langages.
if a == 5:
  print('A est cinq')
elif a == 6:
  print('A est six')
elif a == 7:
  print('A est sept')
else:
  print('A est un nombre quelconque')

# or est équivalent à ||
if a < 6 or a == 10:
  print('A doit être inférieur à 6 ou doit être égal à dix')

# not est équivalent à !
if not a == 10:
  print('A n'est pas égal à 10')

# C'est la notation abrégée de l'instruction if.
if a == 5: print('A est cinq')

# Notation abrégée pour l'instruction if-else.
print('A est cinq') if a == 5 else print('A n'est pas cinq')

```

## Boucles

Python a deux types de boucles :

1. For
2. While

### Boucles while

```python
# La boucle while suivante imprime jusqu'à 5. Souvenez-vous de l'indentation.
i = 0
while i <= 5:
  print(i)
  i += 1

# Utilisation de break ou continue dans une boucle while
i = 0
while i <= 5:
  print(i)
  i += 1
  if i == 2:
    break # Vous pouvez essayer d'utiliser continue ici

# Voici la partie intéressante. La boucle while a une partie else. La partie else s'exécutera une fois que toute la boucle sera terminée.
i = 10
while i <= 15:
  print(i)
  i += 1
else:
  print('Terminé')

# Sortie
10
11
12
13
14
15
Terminé

# Mais si vous utilisez break dans la boucle, alors Python sortira de toute la boucle et n'exécutera pas la partie else.
i = 10
while i <= 15:
  print(i)
  i += 1
  if i == 13:
    break
else:
  print('Terminé')

# Sortie
10
11
12

```

### Boucles for

```python
# Les boucles for comme for(i=0; i<5; i++) ne sont pas principalement utilisées en Python. Au lieu de cela, Python insiste sur l'itération sur les éléments

arr = ['a', 'b', 'c', 'd', 'e']
for ele in arr: # Imprime chaque élément d'un tableau
  print(ele)

word = "python"
for char in word: # Imprime chaque caractère du mot
  print(char)

# Vous pouvez utiliser break, continue et la partie else dans une boucle for également.

# En parlant des boucles for, j'ai remarqué que la plupart des ressources ont également mentionné la fonction range(). (Nous traiterons des fonctions dans la partie suivante de cet article.)

# La fonction range() génère une séquence de nombres.

# range(start, stop, step)
# start - optionnel, le nombre de départ. Par défaut est 0. Ce nombre est inclus dans la séquence
# stop - obligatoire, le nombre de fin. Ce nombre est exclu de la séquence
# step - optionnel, incréments par. Par défaut est 1.

range(3) # Ce code génère une séquence de 0 à 2.
range(1, 4) # Ce code génère une séquence de 1 à 3.
range(1, 8, 2) # Ce code génère une séquence avec 1, 3, 5, 7

for ele in range(3): # Imprime de 0 à 2. 
  print(ele)

# Dans l'exemple ci-dessous, vous pouvez voir que j'ai utilisé range pour itérer à travers un tableau avec un index.
for index in range(0, len(arr)):
  print(arr[index])

dict = {'name': 'John wick'}

# Vous pouvez itérer à travers un dictionnaire. items() retournera à la fois les clés et les valeurs. Vous pouvez également utiliser keys() et values() si nécessaire. 
for key, value in dict.items():
  print(key + " est " + value)

# Vous pouvez également utiliser une fonction intégrée enumerate(). enumurate() retournera un tuple avec un index. Il est principalement utilisé pour ajouter un compteur aux objets itérables en Python.
for index, value in enumerate(arr):
  print(value + " est présent à " + str(index))

```

## Fonctions

```python
def prints_hello_world():
  print('Hello world from Python')

prints_hello_world()

# Instruction return
def prints_something(something):
  return something + ' from Python'

print(prints_something('Hello world'))

# Si vous passez un nombre incorrect d'arguments comme deux ou trois arguments à cette fonction, alors Python générera une erreur.
print(prints_something())

# Paramètre par défaut. Je pense que c'est courant dans la plupart des langages maintenant.
def prints_something(something = 'Hello world'):
  print(something + ' from Python')

# arguments de mot-clé. Vous pouvez passer explicitement quel paramètre doit être apparié. De cette manière, vous n'avez pas à envoyer les arguments dans l'ordre, il suffit de mentionner explicitement le nom du paramètre.
def movie_info(title, director_name, ratings):
  print(title + " - " + director_name + " - " + ratings)

movie_info(ratings='9/10', director_name='David Fincher', title='Fight Club')


# Nombre arbitraire d'arguments
# Parfois, vous ne savez pas combien d'arguments sont passés. Dans ce cas, vous devez demander à Python d'accepter autant d'arguments que possible.

def languages(*names):
  print(names) # ('Python', 'Ruby', 'JavaScript', 'Go'). C'est un tuple.
  return 'Vous avez mentionné '+ str(len(names))+ ' langages'

print(languages('Python', 'Ruby', 'JavaScript', 'Go')) # Vous avez mentionné 4 langages

def languages(fav_language, *names):
  print(names) # ('Ruby', 'JavaScript', 'Go')
  return 'Mon langage préféré est ' + fav_language+ '. Et je prévois d'apprendre les autres '+ str(len(names))+ ' langages aussi'

print(languages('Python', 'Ruby', 'JavaScript', 'Go')) # Mon langage préféré est Python. Et je prévois d'apprendre les autres 3 langages aussi


# Arguments de mot-clé arbitraires
# Ces types d'arguments sont utiles lorsque vous ne savez pas quel type de paramètres sont passés. Dans le cas précédent, c'est utile lorsque vous ne savez pas combien de paramètres sont passés, mais dans ce cas, vous ne savez pas quel type d'informations sera passé.

def user_info(**info):
  print(info) # {'id': 1, 'name': 'Srebalaji', 'fav_language': ['Python', 'Ruby']} C'est un dictionnaire

# Les arguments de mot-clé arbitraires s'attendront toujours à mentionner les paramètres explicitement
user_info(id=1, name='Srebalaji', fav_language=['Python', 'Ruby'])

# Le code ci-dessous générera une erreur. Il n'y a pas d'arguments de mot-clé.
user_info(1, 'Srebalaji')

def user_info(id, name, **info):
  print(info) # {'fav_language': ['Python', 'Ruby'], 'twitter_handle': '@srebalaji'}

user_info(1, 'Srebalaji', fav_language=['Python', 'Ruby'], twitter_handle='@srebalaji')


```

## Classes

```python
# Python est un langage à usage général et également orienté objet.

# C'est une convention que le nom de la classe commence par une majuscule. Mais Python ne génère aucune erreur si vous ne la suivez pas.
class Animal():
  # C'est le constructeur.
  # Comme vous pouvez le voir dans chaque méthode de la classe, j'ai passé 'self' comme premier paramètre. Le premier paramètre est toujours censé être l'instance actuelle de la classe et il est obligatoire de passer l'instance dans le premier paramètre. Et vous pouvez nommer cette variable comme vous le souhaitez.
  def __init__(self, name): 
    self.name = name

  def eat(self):
    print(self.name +' mange')

  def sleep(self):
    print(self.name+' dort')

# Initialisation d'une classe
dog = Animal('harry')
dog.eat()

print(dog.name) # Comme vous pouvez le voir, l'attribut 'name' est également disponible en public. 

# Il peut même être modifié.
dog.name = 'Rosie'
print(dog.name) # 'Rosie'

# Techniquement, il n'y a aucun moyen de rendre les attributs privés en Python. Mais il existe certaines techniques que les développeurs Python utilisent. Je vais essayer d'en lister quelques-unes.

# Attributs protégés.
# Ces attributs ne peuvent être accessibles qu'au sein de la classe et également par la sous-classe.

class Person():
  # Vous pouvez voir que j'ai utilisé un nom différent pour le premier paramètre.
  def __init__(my_instance, name):
    # L'attribut 'name' est protégé.
    my_instance._name = name

  def reads(my_instance):
    print(my_instance._name + ' lit')

  def writes(my_object):
    print(my_object._name + ' écrit')


person1 = Person('Ram')

person1.reads()

# Mais le pire, c'est que l'instance de la classe peut toujours y accéder et le changer :P

print(person1._name) # 'Ram'

person1._name = 'Je peux encore changer.'
print(person1._name) # Je peux encore changer

# Protégé peut être utile parfois. Voyons comment fonctionnent les attributs privés. Cela peut être un sauveur de vie parfois.

class Person():
  def __init__(self, name):
    # L'attribut 'name' est privé.
    self.__name = name

  def reads(self):
    print(self.__name + ' lit')

  def writes(self):
    print(self.__name + ' écrit')
  
  # C'est une méthode privée. Cela ne peut pas être accessible en dehors de la classe.
  def __some_helper_method():
      print('Une méthode d'aide.')


person1 = Person('Ram')
person1.reads() # Ram lit

print(person1.name) # Générera une erreur. L'objet 'Person' n'a pas d'attribut 'name'

print(person1.__name) # Générera une erreur. L'objet 'Person' n'a pas d'attribut '__name'

# Les attributs privés ne peuvent être accessibles qu'au sein de la classe. C'est donc sûr. Mais il y a encore un piège :P

print(person1._Person__name) # Ram.

# Vous pouvez même changer la valeur
person1._Person__name = 'Hari'

print(person1._Person__name) # Hari.

# Mais chaque développeur sait que l'accès et la modification des attributs privés est une mauvaise pratique. Et Python n'a pas vraiment de restriction claire pour l'éviter. Vous devez donc faire confiance à vos pairs sur ce point.

# Héritage

class Animal():
  def __init__(self, name):
    self.name = name

  def eat(self):
    print('Animal mange')

  def sleep(self):
    print('Animal dort')

# Dog est une sous-classe de Animal
class Dog(Animal):
  def __init__(self, name):
    self.name = name

  def eat(self):
    print('Dog mange')


dog1 = Dog('harry')
dog1.eat() # Dog mange
dog1.sleep() # Animal dort

```

## Modules

```python
# Les modules nous aident à organiser le code en Python. Vous pouvez diviser le code en différents fichiers et dossiers et y accéder lorsque vous le souhaitez.

# Considérez le fichier ci-dessous. Il contient deux fonctions.
# calculations.py

def add(a, b):
  return a + b

def substract(a, b):
  return a - b

# considérons un autre fichier que nous considérons comme un fichier principal.
# main.py
import calculations

calculations.add(5, 10) # 15
calculations.substract(10, 3) # 7

# Dans l'exemple ci-dessus, vous avez importé le fichier et avez accédé aux fonctions de celui-ci.

# Il existe d'autres moyens d'importer.

# Vous pouvez changer le nom de la méthode si vous le souhaitez
import calculations as calc
calc.add(5, 10) # 15

# Vous pouvez importer des fonctions spécifiques dont vous avez besoin.
# Vous pouvez accéder à la fonction directement. Vous ne voulez pas mentionner le module.
from calculations import add
add(5, 10) # 15

# Vous pouvez également importer plusieurs fonctions
from calculations import add, multiple, divide

# Vous pouvez importer toutes les fonctions
from calculations import *
add(10, 15)
multiple(4, 5)
divide(10, 3)

# Cela fonctionnera également pour les classes et les variables.

```

## Valeurs Truthy et Falsy

```python
# Selon la documentation Python, tout objet peut être testé comme truthy ou falsy.

# Voici les valeurs Truthy
True
2 # Toute valeur numérique autre que 0
[1] # liste non vide
{'a': 1} # dictionnaire non vide
'a' # chaîne de caractères non vide
{'a'} # Set non vide

# Voici les valeurs Falsy
False
None
0 
0.0
[] # liste vide
{} # dictionnaire vide
() # tuple vide
"" # chaîne de caractères vide
range(0) # set vide

# Vous pouvez évaluer tout objet en booléen en utilisant
bool(any_object) # retourne True ou False

```

## Gestion des exceptions

```python
# Le code qui peut générer des exceptions peut être enveloppé dans l'instruction 'try'. 'except' gérera cette exception.
try:
  some_error_raised
except:
  print('Exception gérée')

# Chaque exception en Python héritera de la classe 'exception'. 

# Dans l'exemple ci-dessous, vous pouvez voir que 'NameError' est la classe d'exception dérivée de la classe principale 'Exception'.
try:
  some_error_raised
except Exception as e:
  print('Exception levée')
  print(e.__class__) # <class 'NameError'>

# Le bloc 'else' s'exécutera si le code dans le bloc 'try' n'a levé aucune exception. Cela sera utile dans de nombreuses situations.

try:
  some_error_raised
except:
  print('Exception gérée')
else:
  print('Aucune erreur levée. Vous pouvez reprendre votre opération ici') # ce code s'exécutera si aucune erreur n'est levée dans le bloc 'try'

# bloc final
# Le code dans le bloc 'finally' s'exécutera peu importe si l'exception est levée ou non.
try:
  some_error_raised
except Exception as e:
  print('Exception levée')
else:
  print('Cela s'exécutera si aucune erreur n'est levée dans try')
finally:
  print('Ce code s'exécutera que le code ait une erreur ou non.')


# Levez votre propre exception. Vous pouvez également créer votre propre classe d'exception héritée de la classe Exception.
try:
  raise ZeroDivisionError # Classe d'exception intégrée de Python
except Exception as e:
  print(e.__class__) # <class 'ZeroDivisionError'>

# Attrapez une exception spécifique.
try:
  raise ZeroDivisionError # Classe d'exception intégrée de Python
except TypeError as e:
  print('Seule l'exception d'erreur de type est capturée')
except ZeroDivisionError as e:
  print('Seule l'exception de division par zéro est capturée')
except Exception as e:
  print('Autres exceptions')

```

Merci d'avoir lu :)

Publié à l'origine dans ce dépôt Github : [Python crash course](https://github.com/srebalaji/python-crash-course)