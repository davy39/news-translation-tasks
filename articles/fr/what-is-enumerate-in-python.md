---
title: Qu'est-ce que enumerate() en Python ? Exemple d'énumération
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-22T15:56:07.000Z'
originalURL: https://freecodecamp.org/news/what-is-enumerate-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-yan-krukov-8612931.jpg
tags:
- name: Python
  slug: python
seo_title: Qu'est-ce que enumerate() en Python ? Exemple d'énumération
seo_desc: "By Suchandra Datta\nThe enumerate() function is one of the built-in functions\
  \ in Python. It provides a handy way to access each item in an iterable, along with\
  \ a count value that specifies the order in which the item was accessed. \nIn this\
  \ article you..."
---

Par Suchandra Datta

La fonction `enumerate()` est l'une des fonctions intégrées en Python. Elle offre un moyen pratique d'accéder à chaque élément d'un itérable, ainsi qu'à une valeur de compteur qui spécifie l'ordre dans lequel l'élément a été accessible. 

Dans cet article, vous apprendrez tout ce dont vous avez besoin pour commencer à utiliser `enumerate()` dans votre code. Plus précisément, nous explorerons :

* Quand utiliser enumerate
* La syntaxe de `enumerate()` et les arguments d'entrée
* Différentes façons d'invoquer `enumerate()` en utilisant des itérables intégrés
* Comment invoquer `enumerate()` en utilisant un itérable personnalisé
* Comment utiliser `enumerate()` dans une boucle for

Commençons.

## Quand utiliser Enumerate ?

Prenons un exemple. Supposons que nous avons une liste de noms d'étudiants :

```python
noms = ["Wednesday", "Enid", "Rowan", "Bianca"]
```

Nous voulons créer une liste de tuples, où chaque élément de tuple contient un numéro d'identification d'étudiant et le nom de l'étudiant comme ceci :

```python
[(0, 'Wednesday'), (1, 'Enid'), (2, 'Rowan'), (3, 'Bianca')]
```

L'identifiant de l'étudiant est l'index du nom de l'étudiant dans la liste des noms. Ainsi, dans le tuple (3, 'Bianca'), l'étudiante Bianca a un identifiant de 3 puisque Bianca est à l'index 3 dans la liste des noms. De même, dans (0, 'Wednesday'), l'étudiante Wednesday a un identifiant de 0 puisque elle est à l'index 0 dans la liste des noms.

Chaque fois que nous rencontrons des situations où nous voulons utiliser un élément de liste ainsi que l'index de cet élément de liste ensemble, nous utilisons `enumerate()`. `enumerate()` suivra automatiquement l'ordre dans lequel les éléments sont accessibles, ce qui nous donne la valeur de l'index sans avoir besoin de maintenir une variable d'index séparée.

Voici comment nous pouvons créer la liste de tuples d'identifiants et de noms d'étudiants en utilisant `enumerate()` :

```python
list(enumerate(noms))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-119.png)

Examinons de plus près la syntaxe de cette fonction.

## Syntaxe de enumerate() et arguments d'entrée

Tout d'abord, examinons **`enumerate(iterable, start=0)`.**

Enumerate nécessite seulement deux arguments d'entrée :

* Un itérable, tel qu'une liste, un tuple, une chaîne, un dictionnaire ou tout objet qui a les méthodes `__next__` et `__iter__` définies (ce qui signifie qu'il supporte l'itération). Cet argument est obligatoire.
* Une valeur de départ pour le compteur, qui par défaut est zéro

`enumerate()` retournera un objet enumerate qui contient essentiellement une liste de tuples. Chaque tuple contient un élément de l'itérable et la valeur de compteur de l'élément.

Pour plus de détails sur les arguments d'entrée et les variations, vous pouvez consulter la documentation [ici](https://docs.python.org/3/library/functions.html#enumerate).

Nous pouvons appeler enumerate comme ceci :

```python
enumerate(noms)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-109.png)

La sortie `<enumerate at 0x1d02258>` est l'objet enumerate. Pour voir les éléments de l'énumération, nous pouvons utiliser une liste comme ceci :

```python
list(enumerate(noms))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-120.png)

Nous obtenons une liste de tuples. Chaque tuple est de la forme (compteur, élément de la liste des noms) avec la valeur de départ par défaut de zéro, donc le compteur commence à zéro. 

Le 1er élément de la liste des noms et le compteur = 0 forment le 1er tuple. Le deuxième élément de la liste des noms et le compteur = 1 forment le deuxième tuple. De même, le 4ème élément de la liste des noms et le compteur = 3 forment le dernier tuple. 

## Comment invoquer `enumerate()` en utilisant des itérables intégrés

Il existe différentes façons d'invoquer `enumerate()`, telles que :

* Invoquer `enumerate()` avec une valeur de départ spécifique
* Invoquer `enumerate()` et convertir la sortie en une liste, un tuple ou un dictionnaire
* Invoquer `enumerate()` avec un dictionnaire en entrée

Examinons chacun de ces cas avec des exemples.

### Comment invoquer `enumerate()` avec une valeur de départ spécifique

Vous voudrez utiliser cette option lorsque vous avez une exigence que les valeurs d'index doivent commencer à partir d'une valeur spécifique. Par exemple, pour cette liste de noms d'étudiants :

```python
noms = ["Wednesday", "Enid", "Rowan", "Bianca"]
```

Nous voulons une liste d'identifiants et de noms d'étudiants avec la restriction que les identifiants doivent commencer à 1. Dans ce cas, nous pouvons invoquer enumerate avec un paramètre de départ comme ceci :

```python
list(enumerate(noms, start=1))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-121.png)

Maintenant, la valeur de compteur retournée par enumerate commence à 1 et non à zéro comme dans la sortie précédente. Si nous avons une restriction que les identifiants d'étudiants doivent commencer à 100, alors nous pouvons obtenir la sortie souhaitée en faisant simplement start=100 :

```python
list(enumerate(noms, start=100))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-122.png)

### Comment invoquer `enumerate()` et convertir la sortie en une liste, un tuple ou un dictionnaire

Nous pouvons convertir la sortie de l'énumération en une liste, un tuple ou un dictionnaire en appelant le constructeur correspondant de ce type.

Pour obtenir une liste, nous utilisons cette syntaxe :

```python
list(enumerate(noms))
```

Pour un tuple, nous utilisons cette syntaxe :

```python
tuple(enumerate(noms))
```

Remarquez comment les sorties se ressemblent presque, sauf que les tuples du premier sont enfermés dans `[ ]`, signifiant qu'il s'agit d'une liste de tuples. Dans le second, ils sont enfermés dans `( )` signifiant qu'il s'agit d'un tuple de tuples :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-123.png)

Pour un dictionnaire, utilisez le constructeur comme ceci :

```python
dict(enumerate(noms))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-124.png)

### Comment invoquer `enumerate()` avec un dictionnaire en entrée

La manière par défaut dont enumerate traite les dictionnaires est un peu différente de la manière dont il fonctionne avec les listes ou les tuples. 

Les dictionnaires sont un type de mappage avec une paire clé-valeur, et `enumerate()` n'itère que sur les clés et non sur les valeurs par défaut.

Par exemple,

```python
noms_et_pouvoirs_speciaux = {"Wednesday":"psychic", "Enid":"werewolf", "Tyler":"normie"}
print(tuple(enumerate(noms_et_pouvoirs_speciaux)))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-112.png)

Enumerate ne considère que les clés du dictionnaire et retourne la valeur de compteur. Ce n'est pas utile lorsque nous voulons un index pour la clé et la valeur. 

Nous pouvons énumérer à la fois les clés et les valeurs comme ceci :

```python
noms_et_pouvoirs_speciaux = {"Wednesday":"psychic", "Enid":"werewolf", "Tyler":"normie"}
print(tuple(enumerate(noms_et_pouvoirs_speciaux.items())))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-113.png)

## Comment invoquer `enumerate()` en utilisant un itérable personnalisé

Nous pouvons souvent rencontrer des situations où nous devons maintenir une collection d'objets définis par l'utilisateur et itérer sur cette collection. Tout objet est un itérable s'il a les méthodes `__iter__` et `__next__` définies. 

Dans cette section, nous apprendrons comment créer notre propre itérable et ensuite utiliser enumerate avec lui.

Disons que nous voulons suivre quels étudiants fréquentent une école fictive appelée Nevermore Academy en quelle année. Nous créons une classe Student pour représenter chaque étudiant et une classe Nevermore pour représenter l'école. 

Nous voulons effectuer la même tâche que précédemment : créer une liste de tuples avec l'identifiant de l'étudiant et le nom de l'étudiant. Mais maintenant, au lieu d'une liste, nous devons traiter avec une liste d'objets stockés dans une variable d'instance d'un objet de type Nevermore. 

Voici la définition de la classe Student. Pour chaque étudiant, nous avons deux variables d'instance - le nom de l'étudiant et le pouvoir spécial de l'étudiant.

```python
#Créer une classe Student qui a des variables d'instance - nom de l'étudiant, pouvoir de l'étudiant
class Student:
    def __init__(self, name, power):
        self.name=name
        self.power=power
```

Maintenant, créons quelques objets Student :

```python
student_1 = Student("Rowan","telekinesis")
student_2 = Student("Enid", "werewolf")
student_3 = Student("Wednesday", "psychic")
student_4 = Student("Bianca","siren")
```

Ensuite, définissons la classe Nevermore. Elle a 3 variables d'instance pour stocker l'année, la liste des objets Student qui fréquentent Nevermore pour cette année, et une variable d'index i. Cette variable sera utilisée pour l'itération dans la méthode `__next__`.

Le constructeur ressemble à ceci :

```python
class Nevermore:
    def __init__(self, year):
        self.year=year
        self.students=[]
        #Cette variable sera l'index utilisant lequel nous retournerons des valeurs du tableau students dans la méthode __next__
        self.i=-1
```

Ajoutons une méthode d'instance utilisant laquelle la variable d'instance `students` sera peuplée :

```python
 def add(self, Student):
        self.students.append(Student)
```

Elle prend en entrée un objet Student et l'ajoute à la liste.

Ensuite, nous définissons les méthodes dont nous avons besoin pour en faire un itérable :

```python
def __iter__(self):
        return self
    
def __next__(self):
        self.i = self.i + 1
        if self.i < len(self.students):
            return self.students[self.i].name
        else:
            raise StopIteration
```

Enumerate accédera aux éléments de l'itérable en fonction de ce que la méthode `__next__` retourne. 

Dans `__next__`, nous parcourons la liste en utilisant la variable d'instance i comme index. Tant que l'index est valide, nous retournons le nom de l'objet Student dans le tableau students. 

Une fois que nous avons parcouru tous les étudiants, nous levons une exception StopIteration, qui est une méthode standard pour signifier la fin de l'itération.

Voici la définition complète de la classe :

```python
#Créer une classe qui contient l'année de promotion et une liste d'objets étudiants
class Nevermore:
    def __init__(self, year):
        self.year=year
        self.students=[]
        #Cette variable sera l'index utilisant lequel nous retournerons des valeurs du tableau students dans la méthode __next__
        self.i=-1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.i = self.i + 1
        if self.i < len(self.students):
            return self.students[self.i].name
        else:
            raise StopIteration
    def add(self, Student):
        self.students.append(Student)
```

Créons un objet Nevermore pour l'année 2022 :

```python
promotion = Nevermore("2022")
```

Et maintenant, ajoutons quelques étudiants à la promotion 2022 :

```python
promotion.add(student_1)    
promotion.add(student_2)
promotion.add(student_3)
promotion.add(student_4)
```

`promotion` est maintenant notre objet personnalisé qui a des variables d'instance - année, une chaîne, et students, une liste d'objets Student. Nous invoquons maintenant enumerate comme ceci :

```python
print(list(enumerate(promotion)))
```

Nous obtiendrons la sortie comme ceci, où nous avons le compteur dans lequel l'objet étudiant est accessible, qui est notre identifiant d'étudiant et le nom de l'étudiant. Nous avons ajouté Rowan en premier à la liste donc la valeur du compteur est 0. Nous avons ajouté Enid en second donc la valeur du compteur est 1, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-125.png)

## Comment utiliser `enumerate()` dans une boucle for

Dans nos applications, nous pourrions vouloir utiliser la sortie de enumerate pour un traitement ultérieur, comme obtenir l'identifiant et le nom de l'étudiant et utiliser ensuite cette valeur pour accéder à une autre structure de données. La manière la plus courante d'utiliser `enumerate()` est à travers une boucle for.

Nous pouvons déballer la sortie de l'énumération dans une boucle for comme ceci :

```python
noms = ["Wednesday", "Enid", "Rowan", "Bianca"]
for student_id, name in enumerate(noms):
    print("student_id = {}\tstudent name = {}".format(student_id, name))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-126.png)

`enumerate()` retourne un tuple pour chaque élément de l'itérable. La première valeur dans le tuple est la valeur de compteur que nous stockons dans la variable de boucle for `student_id`. La deuxième valeur dans le tuple est l'élément de la liste que nous stockons dans la variable de boucle for `name`. 

Nous pourrions avoir un dataframe où, correspondant à chaque étudiant, nous avons certaines autres informations comme les activités extrascolaires. Nous définissons l'index à `student_id` afin que nous puissions accéder à n'importe quelle ligne dans le `df` en utilisant la valeur `student_id` avec la méthode `df.loc`

```python
import pandas as pd

df = pd.DataFrame(data=[[3, "Choir"], [2, "NA"], [0, "Bee keeping"], [1, "Blogging"]], \
                  columns=["student_id", "extra_curricular"])
df = df.set_index("student_id")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-129.png)

En utilisant l'identifiant et le nom de l'étudiant de l'énumération, nous pouvons accéder au dataframe comme ceci :

```python
for student_id, name in enumerate(noms):
    print("student_id = {}\tstudent name = {} \nExtra currcilar = {}\n".format(student_id, name, df.loc[student_id]["extra_curricular"]))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-128.png)

## Conclusion

Dans cet article, nous avons appris la méthode enumerate et quand l'utiliser. Nous avons examiné un exemple où il est utile d'avoir des valeurs d'index ainsi que des éléments itérables ensemble, les arguments d'entrée de `enumerate`, comment l'invoquer en utilisant des listes, des dictionnaires, des objets personnalisés, et comment l'utiliser dans une boucle for. 

J'espère que cela vous a aidé dans votre codage Python et je vous souhaite tout le meilleur dans votre parcours d'apprentissage de Python.