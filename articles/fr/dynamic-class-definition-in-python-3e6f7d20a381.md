---
title: Définition dynamique de classe en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T17:49:19.000Z'
originalURL: https://freecodecamp.org/news/dynamic-class-definition-in-python-3e6f7d20a381
coverImage: https://cdn-media-1.freecodecamp.org/images/0*bJlMQkXW7FOfL5CL
tags:
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Définition dynamique de classe en Python
seo_desc: 'By Peter Gleeson

  Here’s a neat Python trick you might just find useful one day. Let’s look at how
  you can dynamically define classes, and create instances of them as required.

  This trick makes use of Python’s object oriented programming (OOP) capabil...'
---

Par Peter Gleeson

Voici un truc Python astucieux qui pourrait vous être utile un jour. Examinons comment vous pouvez définir dynamiquement des classes et créer des instances selon vos besoins.

Ce truc utilise les capacités de programmation orientée objet (POO) de Python, nous allons donc les passer en revue d'abord.

### Classes et objets

Python est un langage orienté objet, ce qui signifie qu'il vous permet d'écrire du code dans le [paradigme orienté objet](https://guide.freecodecamp.org/design-patterns/object-oriented-programming/).

Le concept clé de ce paradigme de programmation est les classes. En Python, celles-ci sont utilisées pour créer des objets qui peuvent avoir des attributs.

Les objets sont des instances spécifiques d'une classe. Une classe est essentiellement un plan de ce qu'est un objet et de la manière dont il devrait se comporter.

Les classes sont définies avec deux types d'attributs :

* [Attributs de données](https://docs.python.org/3/tutorial/classes.html#instance-objects) — variables disponibles pour une instance donnée de cette classe
* [Méthodes](https://docs.python.org/3/tutorial/classes.html#method-objects) — fonctions disponibles pour une instance de cette classe

L'exemple classique de POO implique généralement différents types d'animaux ou de nourriture. Ici, j'ai opté pour un thème plus pratique avec une simple visualisation de données.

Tout d'abord, définissez la classe `BarChart`.

```python
class BarChart:
	def __init__(self, title, data):
    	self.title = title
    	self.data = data
   	def plot(self):
    	print("\n"+self.title)
        for k in self.data.keys():
        	print("-"*self.data[k]+" "+k)
```

La méthode `__init__` vous permet de définir des attributs lors de l'instanciation. C'est-à-dire, lorsque vous créez une nouvelle instance de `BarChart`, vous pouvez passer des arguments qui fournissent le titre et les données du graphique.

Cette classe possède également une méthode `plot()`. Celle-ci imprime un graphique à barres très basique dans la console lorsqu'elle est appelée. Elle pourrait faire des choses plus intéressantes dans une application réelle.

Ensuite, instanciez une instance de `BarChart` :

```python
data = {"a":4, "b":7, "c":8}bar = BarChart("A Simple Chart", data)
```

Vous pouvez maintenant utiliser l'objet `bar` dans le reste de votre code :

```python
bar.data['d'] = bar.plot()
```

```
A Simple Chart
---- a
------- b
-------- c
----- d
```

C'est génial, car cela vous permet de définir une classe et de créer des instances dynamiquement. Vous pouvez créer des instances d'autres graphiques à barres en une seule ligne de code.

```python
new_data = {"x":1, "y":2, "z":3}
bar2 = BarChart("Another Chart", new_data)
bar2.plot()
```

```
Another Chart
- x
-- y
--- z
```

Supposons que vous souhaitiez définir plusieurs classes de graphiques. [L'héritage](https://docs.python.org/3.7/tutorial/classes.html#inheritance) vous permet de définir des classes qui "héritent" des propriétés des classes de base.

Par exemple, vous pourriez définir une classe de base `Chart`. Ensuite, vous pouvez définir des classes dérivées qui héritent de la base.

```python
class Chart:
	def __init__(self, title, data):
    	self.title = title
        self.data = data
    def plot(self):
    	pass
```

```python
class BarChart(Chart):
	def plot(self):
    	print("\n"+self.title)
        for k in self.data.keys():
        	print("-"*self.data[k]+" "+k)
```

```python
class Scatter(Chart):
	def plot(self):
    	points = zip(data['x'],data['y'])
        y = max(self.data['y'])+1
        x = max(self.data['x'])+1
        print("\n"+self.title)
        for i in range(y,-1,-1):
        	line = str(i)+"|"
            for j in range(x):
            	if (j,i) in points:
                	line += "X"
                else:
                	line += " "
            print(line)
```

Ici, la classe `Chart` est une classe de base. Les classes `BarChart` et `Scatter` héritent de la méthode `__init__()` de `Chart`. Mais elles ont leurs propres méthodes `plot()` qui remplacent celle définie dans `Chart`_._

Vous pouvez maintenant créer des objets de graphique en nuage de points également.

```python
data = {'x':[1,2,4,5], 'y':[1,2,3,4]}
scatter = Scatter('Scatter Chart', data)
scatter.plot()
```

```
Scatter Chart
4|     X
3|	  X 
2|  X
1| X
0|
```

Cette approche vous permet d'écrire un code plus abstrait, donnant à votre application une plus grande flexibilité. Avoir des plans pour créer d'innombrables variations du même objet général vous évitera de répéter inutilement des lignes de code. Cela peut également rendre le code de votre application plus facile à comprendre.

Vous pouvez également importer des classes dans des projets futurs, si vous souhaitez les réutiliser plus tard.

### Méthodes de fabrication

Parfois, vous ne connaîtrez pas la classe spécifique que vous souhaitez implémenter avant l'exécution. Par exemple, peut-être que les objets que vous créez dépendront de l'entrée de l'utilisateur, ou des résultats d'un autre processus avec un résultat variable.

Les [méthodes de fabrication](https://en.wikipedia.org/wiki/Factory_method_pattern) offrent une solution. Ce sont des méthodes qui prennent une liste dynamique d'arguments et retournent un objet. Les arguments fournis déterminent la classe de l'objet qui est retourné.

Un exemple simple est illustré ci-dessous. Cette méthode de fabrication peut retourner soit un objet de graphique à barres, soit un objet de graphique en nuage de points, selon l'argument `style` qu'elle reçoit. Une méthode de fabrication plus intelligente pourrait même deviner la meilleure classe à utiliser, en examinant la structure de l'argument `data`.

```python
def chart_factory(title, data, style):
	if style == "bar":
    	return BarChart(title, data)
    if style == "scatter":
    	return Scatter(title, data)
    else:
    	raise Exception("Unrecognized chart style.")
        
    
```

```python
chart = chart_factory("New Chart", data, "bar")
chart.plot()
```

Les méthodes de fabrication sont idéales lorsque vous savez à l'avance quelles classes vous souhaitez retourner et les conditions dans lesquelles elles sont retournées.

Mais que faire si vous ne savez même pas cela à l'avance ?

### Définitions dynamiques

Python vous permet de définir des classes dynamiquement et de créer des objets avec elles selon vos besoins.

Pourquoi pourriez-vous vouloir faire cela ? La réponse courte est encore plus d'abstraction.

Admettons que le besoin d'écrire du code à ce niveau d'abstraction est généralement rare. Comme toujours en programmation, vous devriez considérer s'il existe une solution plus simple.

Cependant, il peut y avoir des moments où il s'avère vraiment utile de définir des classes dynamiquement. Nous allons couvrir un cas d'utilisation possible ci-dessous.

Vous êtes peut-être familier avec la fonction `type()` de Python. Avec un argument, elle retourne simplement le "type" de l'objet de l'argument.

```python
type(1) # <type 'int'>
type('hello') # <type 'str'>
type(True) # <type 'bool'>
```

Mais, avec trois arguments, `type()` retourne un tout nouvel [objet de type](https://docs.python.org/3/library/stdtypes.html#bltin-type-objects). Cela est [équivalent à définir une nouvelle classe](https://docs.python.org/3/library/functions.html#type).

```
NewClass = type('NewClass', (object,), {})
```

* Le premier argument est une chaîne qui donne un nom à la nouvelle classe
* Le suivant est un tuple, qui contient toutes les classes de base dont la nouvelle classe devrait hériter
* Le dernier argument est un dictionnaire d'attributs spécifiques à cette classe

Quand pourriez-vous avoir besoin d'utiliser quelque chose d'aussi abstrait que cela ? Considérez l'exemple suivant.

[Flask Table](https://flask-table.readthedocs.io/en/stable/#flask-table) est une bibliothèque Python qui génère de la syntaxe pour les tableaux HTML. Elle peut être installée via le gestionnaire de paquets pip.

Vous pouvez utiliser Flask Table pour définir des classes pour chaque tableau que vous souhaitez générer. Vous définissez une classe qui hérite d'une classe de base `Table`. Ses attributs sont des objets de colonne, qui sont des instances de la classe `Col`.

```python
from flask_table import Table, Col
class MonthlyDownloads(Table):
	month = Col('Month')
    downloads = Col('Downloads')
    
data = [{'month':'Jun', 'downloads':700},
		{'month':'Jul', 'downloads':900},
        {'month':'Aug', 'downloads':1600},
        {'month':'Sep', 'downloads':1900},
        {'month':'Oct', 'downloads':2200}]
        
table = MonthlyDownloads(data)print(table.__html__())
```

Vous créez ensuite une instance de la classe, en passant les données que vous souhaitez afficher. La méthode `__html__()` génère le HTML requis.

Maintenant, supposons que vous développez un outil qui utilise Flask Table pour générer des tableaux HTML basés sur un fichier de configuration fourni par l'utilisateur. Vous ne savez pas à l'avance combien de colonnes l'utilisateur souhaite définir — cela pourrait être une, cela pourrait être cent ! Comment votre code peut-il définir la bonne classe pour le travail ?

La définition dynamique de classe est utile ici. Pour chaque classe que vous souhaitez définir, vous pouvez construire dynamiquement le dictionnaire `attributes`.

Supposons que votre configuration utilisateur soit un fichier CSV, avec la structure suivante :

```
Table1, column1, column2, column3
Table2, column1
Table3, column1, column2
```

Vous pourriez lire le fichier CSV ligne par ligne, en utilisant le premier élément de chaque ligne comme nom de chaque classe de tableau. Les éléments restants de cette ligne seraient utilisés pour définir des objets `Col` pour cette classe de tableau. Ceux-ci sont ajoutés à un dictionnaire `attributes`, qui est construit de manière itérative.

```
for row in csv_file:
	attributes = {}
    for column in row[1:]:
    	attributes[column] = Col(column)
        globals()[row[0]] = type(row[0], (Table,), attributes)
```

Le code ci-dessus définit des classes pour chacun des tableaux dans le fichier de configuration CSV. Chaque classe est ajoutée au dictionnaire `globals`.

Bien sûr, ceci est un exemple relativement trivial. FlaskTable est capable de générer des tableaux beaucoup plus sophistiqués. Un cas d'utilisation réel en ferait mieux usage ! Mais, espérons-le, vous avez vu comment la définition dynamique de classe pourrait s'avérer utile dans certains contextes.

### Maintenant vous savez...

Si vous êtes nouveau en Python, il vaut la peine de se familiariser avec les classes et les objets dès que possible. Essayez de les implémenter dans votre prochain projet d'apprentissage. Ou, [parcourez des projets open source sur Github](https://github.com/trending/python) pour voir comment d'autres développeurs les utilisent.

Pour ceux qui ont un peu plus d'expérience, il peut être très gratifiant d'apprendre comment les choses fonctionnent "derrière les scènes". Parcourir [la documentation officielle](https://docs.python.org/3/) peut être éclairant !

Avez-vous déjà trouvé un cas d'utilisation pour la définition dynamique de classe en Python ? Si oui, ce serait génial de le partager dans les réponses ci-dessous.