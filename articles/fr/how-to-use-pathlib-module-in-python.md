---
title: Python Path – Comment utiliser le module Pathlib avec des exemples
subtitle: ''
author: Rochdi Khalid
co_authors: []
series: null
date: '2022-05-10T13:59:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-pathlib-module-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pathlib-cover-freecodecamp.jpg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: Python Path – Comment utiliser le module Pathlib avec des exemples
seo_desc: "Each operating system has different rules for constructing file paths.\
  \ For example, Linux uses forward slashes for paths, while Windows uses backslashes.\
  \ \nThis small difference can cause issues if you are working on a project and you\
  \ want other devel..."
---

Chaque système d'exploitation a des règles différentes pour construire les chemins de fichiers. Par exemple, Linux utilise des barres obliques pour les chemins, tandis que Windows utilise des barres obliques inverses. 

Cette petite différence peut causer des problèmes si vous travaillez sur un projet et que vous souhaitez que d'autres développeurs, provenant de différents systèmes d'exploitation, étendent votre code. 

Heureusement, si vous codez en Python, le module Pathlib fait le travail difficile en vous permettant de vous assurer que vos chemins de fichiers fonctionnent de la même manière sur différents systèmes d'exploitation. De plus, il fournit des fonctionnalités et des opérations pour vous aider à gagner du temps lors de la manipulation de chemins.

## Prérequis

Pathlib est inclus par défaut avec Python >= 3.4. Cependant, si vous utilisez une version de Python inférieure à 3.4, vous n'aurez pas accès à ce module.

## Comment fonctionne Pathlib ?

Pour comprendre comment vous pouvez construire un chemin de base en utilisant Pathlib, créons un nouveau fichier Python appelé `example.py` et plaçons-le dans un répertoire particulier.

Ouvrez le fichier et tapez le contenu suivant :

```python
import pathlib

p = pathlib.Path(__file__)
print(p)

```

Dans cet exemple, nous importons le module Pathlib. Ensuite, nous créons une nouvelle variable appelée `p` pour stocker le chemin. Ici, nous utilisons l'objet Path de Pathlib avec une variable intégrée en Python appelée **__file__** pour faire référence au chemin du fichier dans lequel nous écrivons actuellement `example.py`.

Si nous imprimons `p`, nous obtiendrons le chemin du fichier dans lequel nous nous trouvons actuellement :

```
/home/rochdikhalid/dev/src/package/example.py
```

Comme montré ci-dessus, Pathlib crée un chemin vers ce fichier en plaçant ce script particulier dans un objet Path. Pathlib contient de nombreux objets tels que `PosixPath()` et `PurePath()`, que nous apprendrons à connaître plus en détail dans les sections suivantes.

Avant de nous lancer dans cela, Pathlib divise les chemins du système de fichiers en deux classes différentes qui représentent deux types d'objets de chemin : **Pure Path** et **Concrete Path**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/pathlib-diagram.png)
_Classes PurePath()_

Le chemin pur fournit des utilitaires pour gérer et manipuler votre chemin de fichier sans effectuer d'opérations d'écriture, tandis que le chemin concret vous permet de manipuler et d'effectuer des opérations d'écriture sur votre chemin de fichier. 

En d'autres termes, un chemin concret est une sous-classe d'un chemin pur. Il hérite des manipulations de la classe parente et ajoute des opérations d'entrée/sortie qui effectuent des appels système.

## Chemins purs en Python

Les chemins purs manipulent un chemin de fichier sur votre machine même s'il appartient à un système d'exploitation différent. 

Par exemple, supposons que vous êtes sur Linux et que vous souhaitez utiliser un chemin de fichier Windows. Ici, les objets de classe de chemin pur vous aideront à faire fonctionner le chemin sur votre machine avec quelques opérations de base comme la création de chemins enfants ou l'accès à des parties individuelles d'un chemin. 

Mais les chemins purs ne pourront pas imiter certaines autres opérations comme la création d'un répertoire ou d'un fichier car vous n'êtes pas réellement dans ce système d'exploitation.

### Comment utiliser les chemins purs

Comme vous pouvez le voir dans le diagramme ci-dessus, les chemins purs se composent de trois classes qui gèrent tout chemin de système de fichiers sur votre machine :

**PurePath()** est le nœud racine qui fournit des opérations de gestion à chaque objet de chemin dans Pathlib. 

Lorsque vous instanciez `PurePath()`, il crée deux classes pour gérer les chemins Windows et non-Windows. `PurePath()` crée un objet de chemin générique "chemin agnostique", indépendamment du système d'exploitation sur lequel vous exécutez.

```python
In [*]: pathlib.PurePath('setup.py')                                            
Out[*]: PurePosixPath('setup.py')

```

PurePath() dans l'exemple ci-dessus crée un `PurePosixPath()` parce que nous supposons que nous exécutons sur une machine Linux. Mais si vous l'instanciez sur Windows, vous obtiendrez quelque chose comme `PureWindowsPath('setup.py')`.

**PurePosixPath()** est le nœud enfant de PurePath() implémenté pour les chemins de système de fichiers non-Windows.

```python
In [*]: pathlib.PurePosixPath('setup.py')                                            
Out[*]: PurePosixPath('setup.py')

```

Vous n'obtiendrez aucune erreur si vous instanciez `PurePosixPath()` sur Windows car cette classe ne fait tout simplement pas d'appels système.

**PureWindowsPath()** est le nœud enfant de PurePath() implémenté pour les chemins de système de fichiers Windows.

```python
In [*]: pathlib.PureWindowsPath('setup.py')                                     
Out[*]: PureWindowsPath('setup.py')

```

La même chose s'applique à `PureWindowsPath()` puisque cette classe ne fournit pas d'appels système, donc l'instancier ne soulèvera aucune erreur pour les autres systèmes d'exploitation.

### Propriétés des chemins purs

Chaque sous-classe dans **`PurePath()`** fournit les propriétés suivantes :

**PurePath().parent** sort le parent du chemin :

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').parent                     
Out[*]: PurePosixPath('/src/goo/scripts')

```

Dans l'exemple ci-dessus, nous utilisons la propriété `.parent` pour obtenir le chemin du parent logique de `**main.py**`.

**PurePath().parents[]** sort les ancêtres du chemin :

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
		p.parents[0]               
Out[*]: PurePosixPath('/src/goo/scripts')

In [*]: p.parents[1]                
Out[*]: PurePosixPath('/src/goo')

```

Vous devez toujours spécifier l'index de l'ancêtre dans les crochets comme montré ci-dessus. Dans Python 3.10 et au-dessus, vous pouvez utiliser des tranches et des valeurs d'index négatives.

**PurePath().name** fournit le nom du dernier composant de votre chemin :

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').name                      
Out[*]: 'main.py'

```

Dans cet exemple, le composant final du chemin est `main.py`. Donc, la propriété `.name` sort le nom du fichier `main.py` qui est **main** avec son suffixe **.py**.

D'autre part, **PurePath().suffix** fournit l'extension du fichier du dernier composant de votre chemin :

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').suffix                    
Out[*]: '.py'

```

Comparé à la propriété `.name`, la propriété `.suffix` sort l'extension du fichier et exclut le nom du fichier.

**PurePath().stem** sort uniquement le nom du composant final de votre chemin sans le suffixe :

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').stem                      
Out[*]: 'main'

```

Comme montré ci-dessus, la propriété `.stem` exclut le suffixe du composant final `main.py` et fournit uniquement le nom du fichier.

### Méthodes des chemins purs

Chaque sous-classe de `PurePath()` fournit les méthodes suivantes :

**PurePath().is_absolute()** vérifie si votre chemin est absolu ou non :

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.is_absolute()

Out[*]: True

In [*]: o = pathlib.PurePath('scripts/main.py')
        o.is_absolute()

Out[*]: False

```

Notez que le chemin absolu se compose d'une racine et d'un nom de lecteur. Dans ce cas, `PurePath()` ne nous permet pas de connaître le nom du lecteur. 

Si vous utilisez `PureWindowsPath()`, vous pouvez représenter un chemin absolu qui contient un nom de lecteur comme `PureWindowsPath('c:/Program Files')`.

**PurePath().is_relative()** vérifie si le chemin appartient à l'autre chemin donné ou non :

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.is_relative_to('/src')

Out[*]: True

In [*]: p.is_relative_to('/data')

Out[*]: False

```

Dans cet exemple, le chemin donné `/src` fait partie ou appartient au chemin `p`, tandis que l'autre chemin donné `/data` retourne `False` car il n'a pas de relation relative avec le chemin `p`.

**PurePath().joinpath()** concatène le chemin avec les arguments donnés (chemins enfants) :

```python
In [*]: p = pathlib.PurePath('/src/goo')
        p.joinpath('scripts', 'main.py')

Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

Notez qu'il n'est pas nécessaire d'ajouter des barres obliques dans vos arguments donnés, car la méthode `.joinpath()` gère cela pour vous.

**PurePath().match()** vérifie si le chemin correspond à un motif donné :

```python
In [*]: pathlib.PurePath('/src/goo/scripts/main.py').match('*.py')
Out[*]: True

In [*]: pathlib.PurePath('/src/goo/scripts/main.py').match('goo/*.py')
Out[*]: True

In [*]: pathlib.PurePath('src/goo/scripts/main.py').match('/*.py')
Out[*]: False

```

Sur la base des exemples ci-dessus, le motif doit correspondre au chemin. Si le motif donné est absolu, le chemin doit également être absolu.

**PurePath().with_name()** change le nom du composant final avec son suffixe :

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.with_name('app.js')
Out[*]: PurePosixPath('/src/goo/scripts/app.js')

In [*]: p
Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

La méthode `.with_name()` ne change pas le nom du dernier composant de manière permanente. De plus, si le chemin donné ne contient pas de nom, une erreur se produit comme mentionné dans la [documentation officielle](https://docs.python.org/3/library/pathlib.html#methods-and-properties).

**PurePath().with_stem()** change uniquement le nom du composant final du chemin :

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.with_stem('app.py')
Out[*]: PurePosixPath('/src/goo/scripts/app.py')

In [*]: p
Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

Cela est similaire à la méthode `.with_name()`. La méthode `.with_stem()` change le nom du dernier composant temporairement. De plus, si le chemin donné ne contient pas de nom, une erreur se produira.

**PurePath().with_suffix()** change temporairement le suffixe ou l'extension du composant final de votre chemin :   

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main.py')
        p.with_suffix('.js')
Out[*]: PurePosixPath('/src/goo/scripts/main.js')

```

Si le nom du chemin donné ne contient pas de suffixe, la méthode `.with_suffix()` ajoute le suffixe pour vous :

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main')
        p.with_suffix('.py')
Out[*]: PurePosixPath('/src/goo/scripts/main.py')

```

Mais, si nous n'incluons pas le suffixe et que nous gardons l'argument vide `''`, le suffixe actuel sera supprimé.

```python
In [*]: p = pathlib.PurePath('/src/goo/scripts/main')
        p.with_suffix('')
Out[*]: PurePosixPath('/src/goo/scripts/main')

```

Certaines méthodes comme `.with_stem()`, et `.is_relative_to()` ont été ajoutées récemment à Python 3.9 et au-dessus. Donc, si vous appelez ces méthodes en utilisant Python 3.8 ou inférieur, une erreur d'attribut est soulevée.

## Chemins concrets en Python

Les chemins concrets vous permettent de gérer, manipuler et effectuer des opérations d'écriture sur différents chemins de système de fichiers. 

En d'autres termes, ce type d'objet de chemin vous aide à créer, par exemple, un nouveau fichier, un nouveau répertoire, et à effectuer d'autres opérations d'entrée/sortie sans être dans ce système d'exploitation.

### Comment utiliser les chemins concrets

Les chemins concrets gèrent tout chemin de système de fichiers et effectuent des appels système sur votre machine. Ces objets de chemin sont les chemins enfants des chemins purs et se composent de trois sous-classes comme les chemins purs :

**Path()** est le nœud enfant de `PurePath()`, il fournit des opérations de gestion avec la capacité d'effectuer des opérations d'écriture sur votre chemin. 

Lorsque vous instanciez `Path()`, il crée deux classes pour gérer les chemins Windows et non-Windows. Comme `PurePath()`, `Path()` crée également un objet de chemin générique "chemin agnostique", indépendamment du système d'exploitation sur lequel vous exécutez.

```python
In [*]: pathlib.Path('setup.py')                                            
Out[*]: PosixPath('setup.py')

```

`Path()` dans l'exemple ci-dessus crée un `PosixPath()` parce que nous supposons que nous exécutons sur une machine Linux. Mais si vous l'instanciez sur Windows, vous obtiendrez quelque chose comme `WindowsPath('setup.py')`

**PosixPath()** est le nœud enfant de `Path()` et `PurePosixPath()`, implémenté pour gérer et manipuler les chemins de système de fichiers non-Windows.

```python
In [*]: pathlib.PosixPath('setup.py')                                            
Out[*]: PosixPath('setup.py')

```

Vous obtiendrez une erreur si vous instanciez `PosixPath()` sur une machine Windows car vous ne pouvez pas faire d'appels système tout en exécutant sur un système d'exploitation différent.

**WindowsPath()** est le nœud enfant de `Path()` et `PureWindowsPath()` implémenté pour les chemins de système de fichiers Windows.

```python
In [*]: pathlib.WindowsPath('setup.py')                                     
Out[*]: WindowsPath('setup.py')

```

La même chose s'applique à `WindowsPath()` puisque vous exécutez sur un système d'exploitation différent – donc l'instancier soulèvera une erreur.

### Propriétés des chemins concrets

Puisque le chemin concret est la sous-classe du chemin pur, vous pouvez tout faire avec les chemins concrets en utilisant les propriétés de `PurePath()`. Cela signifie que nous pouvons utiliser, par exemple, la propriété `.with_suffix` pour ajouter un suffixe à un chemin concret :

```python
In [*]: p = pathlib.Path('/src/goo/scripts/main')
        p.with_suffix('.py')
Out[*]: PosixPath('/src/goo/scripts/main.py')

```

Ou, vous pouvez vérifier si un chemin donné est relatif au chemin original :

```python
In [*]: p = pathlib.Path('/src/goo/scripts/main.py')
        p.is_relative_to('/src')

Out[*]: True

```

N'oubliez pas que les chemins concrets héritent des opérations de gestion des chemins purs et ajoutent des opérations d'écriture qui effectuent des appels système et des configurations d'entrée/sortie.

### Méthodes des chemins concrets

Chaque sous-classe de `Path()` fournit les méthodes suivantes pour gérer les chemins et effectuer des appels système :

**Path().iterdir()** retourne le contenu d'un répertoire. Supposons que nous avons le dossier suivant qui contient les fichiers suivants :

```
data
	population.json
	density.json
	temperature.yml
	stats.md
	details.txt

```

Pour retourner le contenu du répertoire `/data`, vous pouvez utiliser la méthode `.iterdir()` ici :

```python
In [*]: p = pathlib.Path('/data')

        for child in p.iterdir():
        	print(child)

Out[*]: PosixPath('/data/population.json')
         PosixPath('/data/density.json')
         PosixPath('/data/temprature.yml')
         PosixPath('/data/stats.md')
         PosixPath('/data/details.txt')

```

La méthode `.iterdir()` crée un itérateur qui liste les fichiers de manière aléatoire.

**Path().exists()** vérifie si le fichier/répertoire existe dans un chemin courant. Utilisons le répertoire de l'exemple précédent (notre répertoire courant est `/data`) :

```python
In [*]: p = pathlib.Path('density.json').exists()
        p
Out[*]: True

```

La méthode **.exists()** retourne `True` car le fichier donné existe dans le répertoire `data`. La méthode retourne `False` si le fichier n'existe pas.

```python
In [*]: p = pathlib.Path('aliens.py').exists()
        p
Out[*]: False

```

La même chose s'applique aux répertoires, la méthode retourne `True` si le répertoire donné existe et retourne `False` s'il n'existe pas.

**Path().mkdir()** crée un nouveau répertoire à un chemin donné :

```python
In [*]: p = pathlib.Path('data')
        directory = pathlib.Path('data/secrets')
        directory.exists()
Out[*]: False

In [*]: directory.mkdir(parents = False, exist_ok = False)
        directory.exists()
Out[*]: True

```

Selon la documentation officielle, la méthode `.mkdir()` prend trois arguments. Nous nous concentrerons uniquement pour le moment sur `parents` et `exist_ok`. 

Les deux arguments sont définis sur `False` par défaut. Le `parent` soulève une erreur FileNotFound en cas de parent manquant, tandis que `exist_ok` soulève une erreur FileExists si le répertoire donné existe déjà.

Dans l'exemple ci-dessus, vous pouvez définir les arguments sur `True` pour ignorer les erreurs mentionnées et mettre à jour le répertoire.

Nous pouvons également créer un nouveau fichier à un chemin donné en utilisant la méthode `Path().touch()` :

```python
In [*]: file = pathlib.Path('data/secrets/secret_one.md')
        file.exists()
Out[*]: False

In [*]: file.touch(exist_ok = False)
        file.exists()
Out[*]: True

```

La même logique s'applique à la méthode `.touch()`. Ici, `exist_ok` peut être défini sur `True` pour ignorer l'erreur FileExists et mettre à jour le fichier.

**Path().rename()** renomme le fichier/répertoire à un chemin donné. Prenons un exemple en utilisant notre répertoire `/data` :

```python
In [*]: p = pathlib.Path('density.json')
        n = pathlib.Path('density_2100.json')
        p.rename(n)
Out[*]: PosixPath('density_2100.json')

```

Si vous attribuez un fichier non existant à la méthode, elle soulève une erreur FileNotFound. La même chose s'applique aux répertoires.

**Path().read_text()** retourne le contenu d'un fichier au format chaîne :

```python
In [*]: p = pathlib.Path('info.txt')
        p.read_text()

Out[*]: 'some text added'

```

De plus, vous pouvez utiliser la méthode `**write_text()**` pour écrire un contenu dans un fichier :

```python
In [*]: p = pathlib.Path('file.txt')
        p.write_text('we are building an empire')

Out[*]: 'we are building an empire'

```

Notez que la méthode **`.write_text()`** a été ajoutée à Python 3.5 et a été mise à jour récemment dans Python 3.10 pour avoir certains paramètres supplémentaires.

## Note importante

Vous pourriez vous demander pourquoi vous devez utiliser les chemins de système de fichiers Windows – car chaque package devrait être compatible avec d'autres systèmes d'exploitation, pas seulement Windows. 

Vous avez raison si le but est de faire un chemin agnostique OS. Mais, parfois nous ne pouvons pas faire cela en raison de certains paramètres qui sont uniques aux systèmes Windows ou Posix. C'est pourquoi ces objets sont disponibles pour aider les développeurs à gérer ces cas d'utilisation. 

Certains packages ciblent des problèmes présents uniquement dans l'écosystème Windows, et Python accommode ces cas d'utilisation dans cette bibliothèque.

## Et ensuite ?

Espérons que ce tutoriel vous aide à apprendre comment et pourquoi utiliser Pathlib et comment il est utile pour gérer et manipuler les chemins de système de fichiers. 

Il serait génial de jouer avec ce que vous avez appris et de transformer les choses en un vrai projet. Si vous avez des questions, n'hésitez pas à me contacter à tout moment sur [LinkedIn](https://www.linkedin.com/in/rochdi-khalid/). 

De plus, vous pouvez jeter un coup d'œil à ma chaîne sur [YouTube](https://www.youtube.com/channel/UCF8iZXSsjgc8kE8hITp5rdQ) où je partage des vidéos sur ce que j'apprends et construis avec du code.

À bientôt dans le prochain tutoriel, et continuez à avancer !

### Références

Il y a beaucoup à savoir. Dans cet article de blog, j'ai couvert les bases dont vous avez besoin pour utiliser Pathlib dans votre projet. 

La documentation officielle met en avant plus de méthodes et de propriétés que vous pouvez appliquer à vos chemins de système de fichiers :

* [Pathlib — Chemins de système de fichiers orientés objet](https://docs.python.org/3/library/pathlib.html)