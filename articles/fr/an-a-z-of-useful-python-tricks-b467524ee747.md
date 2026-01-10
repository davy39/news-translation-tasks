---
title: Un A-Z des astuces Python utiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-28T16:13:34.000Z'
originalURL: https://freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747
coverImage: https://cdn-media-1.freecodecamp.org/images/0*omyr-SRrpmo80-28
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Un A-Z des astuces Python utiles
seo_desc: 'By Peter Gleeson

  Python is one of the world’s most popular, in-demand programming languages. This
  is for many reasons:


  it’s easy to learn

  it’s super versatile

  it has a huge range of modules and libraries


  I use Python daily as an integral part of my...'
---

Par Peter Gleeson

Python est l'un des langages de programmation les plus populaires et demandés au monde. Cela pour plusieurs raisons :

* il est facile à apprendre
* il est super polyvalent
* il dispose d'une énorme gamme de modules et de bibliothèques

J'utilise Python quotidiennement dans le cadre de mon travail de data scientist. En cours de route, j'ai appris quelques astuces et conseils utiles.

Ici, j'en ai partagé certains dans un format A-Z.

La plupart de ces "astuces" sont des choses que j'ai utilisées ou découvertes au cours de mon travail quotidien. Certaines, je les ai trouvées en parcourant la [documentation de la bibliothèque standard Python](https://docs.python.org/3/library/index.html). Quelques autres, je les ai trouvées en cherchant dans [PyPi](https://pypi.org/search/).

Cependant, à qui le mérite revient-il ? J'en ai découvert quatre ou cinq sur [awesome-python.com](https://awesome-python.com/). Il s'agit d'une liste curatée de centaines d'outils et de modules Python intéressants. Cela vaut la peine d'être parcouru pour s'inspirer !

#### all ou any

L'une des nombreuses raisons pour lesquelles Python est un langage si populaire est qu'il est lisible et expressif.

On plaisante souvent en disant que Python est du "[pseudocode exécutable](https://www.artima.com/intv/tippingP.html)". Mais lorsque vous pouvez écrire du code comme ceci, il est difficile d'argumenter autrement :

```python
x = [True, True, False]
if any(x):
    print("Au moins un True")
if all(x):
    print("Pas un seul False")
if any(x) and not all(x):    
    print("Au moins un True et un False")
```

#### bashplotlib

Vous voulez tracer des graphiques dans la console ?

```
$ pip install bashplotlib
```

Vous pouvez avoir des graphiques dans la console.

#### collections

Python dispose de certains types de données par défaut, mais parfois ils ne se comportent pas exactement comme vous le souhaitez.

Heureusement, la bibliothèque standard Python offre [le module collections](https://docs.python.org/3/library/collections.html). Ce module pratique vous fournit des types de données supplémentaires.

```python
from collections import OrderedDict, Counter

# Se souvient de l'ordre dans lequel les clés sont ajoutées !
x = OrderedDict(a=1, b=2, c=3)

# Compte la fréquence de chaque caractère
y = Counter("Hello World!")


```

#### dir

Vous vous êtes déjà demandé comment vous pouvez regarder à l'intérieur d'un objet Python et voir quels attributs il possède ? Bien sûr que oui.

Depuis la ligne de commande :

```
>>> dir()
>>> dir("Hello World")
>>> dir(dir)
```

Cela peut être une fonctionnalité très utile lorsque vous exécutez Python de manière interactive, et pour explorer dynamiquement les objets et modules avec lesquels vous travaillez.

Lisez plus [ici](https://docs.python.org/3/library/functions.html#dir).

#### emoji

Oui, [vraiment](https://pypi.org/project/emoji/).

```
$ pip install emoji
```

Ne faites pas semblant que vous ne allez pas l'essayer...

```python
from emoji import emojize
print(emojize(":thumbs_up:"))
```

👍

#### from __future__ import

L'une des conséquences de la popularité de Python est qu'il y a toujours de nouvelles versions en développement. De nouvelles versions signifient de nouvelles fonctionnalités — à moins que votre version ne soit obsolète.

Ne craignez rien, cependant. Le [module __future__](https://docs.python.org/2/library/__future__.html) vous permet d'importer des fonctionnalités des versions futures de Python. C'est littéralement comme voyager dans le temps, ou de la magie, ou quelque chose comme ça.

```python
from __future__ import print_function
print("Hello World!")
```

Pourquoi ne pas essayer [d'importer des accolades](https://stackoverflow.com/questions/17811855/syntax-error-not-a-chance) ?

#### geopy

La géographie peut être un terrain difficile pour les programmeurs à naviguer (ha, un jeu de mots !). Mais [le module geopy](https://geopy.readthedocs.io/en/latest/) le rend déconcertant de facilité.

```
$ pip install geopy
```

Il fonctionne en abstraisant les API d'une gamme de différents services de géocodage. Il vous permet d'obtenir l'adresse complète d'un lieu, la latitude, la longitude, et même l'altitude.

Il y a aussi une classe de distance utile. Elle calcule la distance entre deux lieux dans votre unité de mesure favorite.

```python
from geopy import GoogleV3

place = "221b Baker Street, London"
location = GoogleV3().geocode(place)
print(location.address)
print(location.location)
```

#### howdoi

Bloqué sur un problème de codage et vous ne vous souvenez plus de cette solution que vous avez vue auparavant ? Besoin de vérifier StackOverflow, mais vous ne voulez pas quitter le terminal ?

Alors vous avez besoin [de cet outil utile en ligne de commande](https://github.com/gleitz/howdoi).

```
$ pip install howdoi
```

Posez-lui n'importe quelle question que vous avez, et il fera de son mieux pour retourner une réponse.

```
$ howdoi vertical align css
$ howdoi for loop in java
$ howdoi undo commits in git
```

Soyez conscient cependant — il extrait le code des meilleures réponses de StackOverflow. Il ne donne peut-être pas toujours les informations les plus utiles...

```
$ howdoi exit vim
```

#### inspect

Le [module inspect](https://docs.python.org/3/library/inspect.html) de Python est idéal pour comprendre ce qui se passe en coulisses. Vous pouvez même appeler ses méthodes sur lui-même !

L'exemple de code ci-dessous utilise `inspect.getsource()` pour imprimer son propre code source. Il utilise également `inspect.getmodule()` pour imprimer le module dans lequel il a été défini.

La dernière ligne de code imprime son propre numéro de ligne.

```python
import inspect

print(inspect.getsource(inspect.getsource))
print(inspect.getmodule(inspect.getmodule))
print(inspect.currentframe().f_lineno)
```

Bien sûr, au-delà de ces utilisations triviales, le module inspect peut s'avérer utile pour comprendre ce que fait votre code. Vous pouvez également l'utiliser pour écrire du code auto-documenté.

#### Jedi

La bibliothèque Jedi est une bibliothèque d'autocomplétion et d'analyse de code. Elle rend l'écriture de code plus rapide et plus productive.

Sauf si vous développez votre propre IDE, vous serez probablement le plus intéressé par [l'utilisation de Jedi en tant que plugin d'éditeur](https://jedi.readthedocs.io/en/latest/docs/usage.html). Heureusement, il y en a déjà beaucoup disponibles !

Vous utilisez peut-être déjà Jedi, cependant. Le projet IPython utilise Jedi pour sa fonctionnalité d'autocomplétion de code.

#### **kwargs

Lors de l'apprentissage de n'importe quel langage, il y a de nombreuses étapes importantes en cours de route. Avec Python, comprendre la syntaxe mystérieuse `**kwargs` compte probablement comme l'une d'entre elles.

Le double astérisque devant un objet dictionnaire vous permet de passer le contenu de ce dictionnaire en tant qu'[arguments nommés à une fonction](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments).

Les clés du dictionnaire sont les noms des arguments, et les valeurs sont les valeurs passées à la fonction. Vous n'avez même pas besoin de l'appeler `kwargs` !

```python
dictionary = {"a": 1, "b": 2}

def someFunction(a, b):
    print(a + b)
    return
    
# ces lignes font la même chose :
someFunction(**dictionary)
someFunction(a=1, b=2)
```

Cela est utile lorsque vous souhaitez écrire des fonctions qui peuvent gérer des arguments nommés non définis à l'avance.

#### List comprehensions

L'une de mes choses préférées concernant la programmation en Python sont ses [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

Ces expressions permettent d'écrire du code très propre qui se lit presque comme du langage naturel.

Vous pouvez lire plus sur la façon de les utiliser [ici](https://www.learnpython.org/en/List_Comprehensions).

```python
numbers = [1,2,3,4,5,6,7]
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]

cities = ['London', 'Dublin', 'Oslo']

def visit(city):
    print("Welcome to "+city)
for city in cities:
    visit(city)
```

#### map

Python supporte la programmation fonctionnelle à travers un certain nombre de fonctionnalités intégrées. L'une des plus utiles est la fonction `map()` — surtout en combinaison avec [les fonctions lambda](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions).

```python
x = [1, 2, 3]
y = map(lambda x : x + 1 , x)
# imprime [2,3,4]
print(list(y))
```

Dans l'exemple ci-dessus, `map()` applique une simple fonction lambda à chaque élément dans `x`. Elle retourne un objet map, qui peut être converti en un objet itérable tel qu'une liste ou un tuple.

#### newspaper3k

Si vous ne l'avez pas encore vu, alors préparez-vous à être impressionné par [le module newspaper de Python](https://pypi.org/project/newspaper3k/).

Il vous permet de récupérer des articles de presse et des métadonnées associées à partir d'une gamme de publications internationales de premier plan. Vous pouvez récupérer des images, du texte et des noms d'auteurs.

Il dispose même de certaines [fonctionnalités NLP intégrées](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#performing-nlp-on-an-article).

Ainsi, si vous pensiez utiliser BeautifulSoup ou une autre bibliothèque de webscraping DIY pour votre prochain projet, économisez-vous du temps et des efforts et faites `$ pip install newspaper3k` à la place.

#### Operator overloading

Python fournit un support pour [la surcharge d'opérateurs](https://docs.python.org/3/reference/datamodel.html#special-method-names), ce qui est l'un de ces termes qui vous font sonner comme un vrai scientifique informatique.

C'est en fait un concept simple. Vous vous êtes déjà demandé pourquoi Python vous permet d'utiliser l'opérateur `+` pour ajouter des nombres et aussi pour concaténer des chaînes ? C'est la surcharge d'opérateurs en action.

Vous pouvez définir des objets qui utilisent les symboles d'opérateurs standard de Python de leur propre manière spécifique. Cela vous permet de les utiliser dans des contextes pertinents pour les objets avec lesquels vous travaillez.

```python
class Thing:
    def __init__(self, value):
        self.__value = value
    def __gt__(self, other):
        return self.__value > other.__value
    def __lt__(self, other):
        return self.__value < other.__value

something = Thing(100)
nothing = Thing(0)

# True
something > nothing

# False
something < nothing

# Error
something + nothing
```

#### pprint

La fonction `print` par défaut de Python fait son travail. Mais essayez d'imprimer un objet grand et imbriqué, et le résultat est plutôt laid.

Voici où intervient le [module pretty-print de la bibliothèque standard](https://docs.python.org/3/library/pprint.html). Cela imprime des objets structurés complexes dans un format facile à lire.

Un must pour tout développeur Python qui travaille avec des structures de données non triviales.

```python
import requests
import pprint

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
pprint.pprint(users)
```

#### Queue

Python supporte le multithreading, et cela est facilité par le module Queue de la bibliothèque standard.

Ce module vous permet de mettre en œuvre des structures de données de file d'attente. Ce sont des structures de données qui vous permettent d'ajouter et de récupérer des entrées selon une règle spécifique.

Les files d'attente "premier entré, premier sorti" (ou FIFO) vous permettent de récupérer des objets dans l'ordre où ils ont été ajoutés. Les files d'attente "dernier entré, premier sorti" (LIFO) vous permettent d'accéder aux objets ajoutés le plus récemment en premier.

Enfin, les files d'attente prioritaires vous permettent de récupérer des objets selon l'ordre dans lequel ils sont triés.

[Voici un exemple de la façon d'utiliser les files d'attente](https://www.tutorialspoint.com/python3/python_multithreading.htm) pour la programmation multithread en Python.

#### __repr__

Lors de la définition d'une classe ou d'un objet en Python, il est utile de fournir une manière "officielle" de représenter cet objet sous forme de chaîne. Par exemple :

```
>>> file = open('file.txt', 'r')
>>> print(file)
<open file 'file.txt', mode 'r' at 0x10d30aaf0>
```

Cela facilite grandement le débogage du code. Ajoutez-le à vos définitions de classe comme ci-dessous :

```python
class someClass:
    def __repr__(self):
        return "<some description here>"
        
someInstance = someClass()

# imprime <some description here>
print(someInstance)
```

#### sh

Python fait un excellent langage de script. Parfois, l'utilisation des bibliothèques standard os et subprocess peut être un peu fastidieuse.

La [bibliothèque sh](http://amoffat.github.io/sh/) offre une alternative pratique.

Elle vous permet d'appeler n'importe quel programme comme s'il s'agissait d'une fonction ordinaire — utile pour automatiser les flux de travail et les tâches, tout cela depuis Python.

```python
import sh
sh.pwd()
sh.mkdir('new_folder')
sh.touch('new_file.txt')
sh.whoami()
sh.echo('This is great!')
```

#### Type hints

Python est un langage à typage dynamique. Vous n'avez pas besoin de spécifier les types de données lorsque vous définissez des variables, des fonctions, des classes, etc.

Cela permet des temps de développement rapides. Cependant, il y a peu de choses plus ennuyeuses qu'une erreur d'exécution causée par un simple problème de typage.

[Depuis Python 3.5](https://docs.python.org/3/library/typing.html), vous avez la possibilité de fournir des indications de type lors de la définition de fonctions.

```
def addTwo(x : Int) -> Int:    return x + 2
```

Vous pouvez également définir des alias de type :

```
from typing import List
```

```
Vector = List[float]
Matrix = List[Vector]
```

```python
def addMatrix(a : Matrix, b : Matrix) -> Matrix:
    result = []
    for i,row in enumerate(a):
        result_row =[]
        for j, col in enumerate(row):
            result_row += [a[i][j] + b[i][j]]
        result += [result_row]
    return result

x = [[1.0, 0.0], [0.0, 1.0]]
y = [[2.0, 1.0], [0.0, -2.0]]
z = addMatrix(x, y)
```

Bien que non obligatoires, les annotations de type peuvent rendre votre code plus facile à comprendre.

Elles vous permettent également d'utiliser des outils de vérification de type pour attraper ces erreurs de type avant l'exécution. Probablement utile si vous travaillez sur des projets grands et complexes !

#### uuid

Une manière rapide et facile de générer des identifiants universellement uniques (ou "UUID") est à travers le [module uuid de la bibliothèque standard Python](https://docs.python.org/3/library/uuid.html).

```python
import uuid

user_id = uuid.uuid4()
print(user_id)
```

Cela crée un nombre aléatoire de 128 bits qui sera presque certainement unique.

En fait, il y a plus de 2¹²² UUID possibles qui peuvent être générés. Cela représente plus de cinq undécillions (ou 5 000 000 000 000 000 000 000 000 000 000 000 000).

La probabilité de trouver des doublons dans un ensemble donné est extrêmement faible. Même avec un billion d'UUID, la probabilité qu'un doublon existe est bien inférieure à une sur un milliard.

Pas mal pour deux lignes de code.

#### Virtual environments

C'est probablement ma chose préférée de Python.

Il y a de fortes chances que vous travailliez sur plusieurs projets Python en même temps. Malheureusement, parfois deux projets dépendront de différentes versions de la même dépendance. Laquelle installez-vous sur votre système ?

Heureusement, le [support de Python pour les environnements virtuels](https://docs.python.org/3/tutorial/venv.html) vous permet d'avoir le meilleur des deux mondes. Depuis la ligne de commande :

```
python -m venv my-project
source my-project/bin/activate
pip install all-the-modules 
```

Maintenant, vous pouvez avoir des versions et des installations autonomes de Python fonctionnant sur la même machine. Résolu !

#### wikipedia

Wikipedia dispose d'une excellente API qui permet aux utilisateurs un accès programmatique à un corpus inégalé de connaissances et d'informations complètement gratuites.

Le [module wikipedia](https://wikipedia.readthedocs.io/en/latest/quickstart.html) rend l'accès à cette API presque embarrassant de commodité.

```python
import wikipedia

result = wikipedia.page('freeCodeCamp')
print(result.summary)

for link in result.links:
    print(link)
```

Comme le site réel, le module prend en charge plusieurs langues, la désambiguïsation des pages, la récupération de pages aléatoires, et dispose même d'une méthode `donate()`.

#### xkcd

L'humour est une caractéristique clé du langage Python — après tout, il est nommé d'après l'émission de sketchs comiques britannique [Monty Python's Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus). Une grande partie de la documentation officielle de Python fait référence aux sketchs les plus célèbres de l'émission.

Le sens de l'humour ne se limite pas aux docs, cependant. Essayez d'exécuter la ligne ci-dessous :

```
import antigravity
```

Ne changez jamais, Python. Ne changez jamais.

#### YAML

YAML signifie "[YAML Ain't Markup Language](http://yaml.org/)". Il s'agit d'un langage de formatage de données, et est un sur-ensemble de JSON.

Contrairement à JSON, il peut stocker des objets plus complexes et faire référence à ses propres éléments. Vous pouvez également écrire des commentaires, ce qui le rend particulièrement adapté à l'écriture de fichiers de configuration.

Le [module PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) vous permet d'utiliser YAML avec Python. Installez avec :

```
$ pip install pyyaml
```

Et importez ensuite dans vos projets :

```
import yaml
```

PyYAML vous permet de stocker des objets Python de n'importe quel type de données, et des instances de n'importe quelle classe définie par l'utilisateur également.

#### zip

Une dernière astuce pour vous, et elle est vraiment cool. Vous avez déjà eu besoin de former un dictionnaire à partir de deux listes ?

```python
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))
```

La fonction intégrée `zip()` prend un certain nombre d'objets itérables et retourne une liste de tuples. Chaque tuple regroupe les éléments des objets d'entrée par leur index positionnel.

Vous pouvez également "dézipper" des objets en appelant `*zip()` sur eux.

#### Merci d'avoir lu !

Alors voilà, un A-Z des astuces Python — espérons que vous avez trouvé quelque chose d'utile pour votre prochain projet.

Python est un langage très diversifié et bien développé, donc il y a forcément de nombreuses fonctionnalités que je n'ai pas encore incluses.

Veuillez partager vos propres astuces Python préférées en laissant une réponse ci-dessous !