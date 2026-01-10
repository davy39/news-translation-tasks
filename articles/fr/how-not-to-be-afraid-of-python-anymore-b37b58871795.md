---
title: Comment ne plus avoir peur de Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T22:03:21.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-python-anymore-b37b58871795
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YOVsFZ95l6WcVFXf
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment ne plus avoir peur de Python
seo_desc: 'By Neil Kakkar

  A dive into the language reference documentation

  For the first year or two when I started coding, I thought learning a language was
  all about learning the syntax. So, that’s all I did.

  Needless to say, I didn’t turn into a great develo...'
---

Par Neil Kakkar

#### Une plongée dans la documentation de référence du langage

Pendant la première année ou les deux premières années où j'ai commencé à coder, je pensais que apprendre un langage consistait uniquement à apprendre la syntaxe. C'est donc tout ce que j'ai fait.

Inutile de dire que je ne suis pas devenu un grand développeur. J'étais bloqué. Puis, un beau jour, tout s'est éclairci. J'ai réalisé que je faisais cela de travers. Apprendre la syntaxe devrait être le cadet de mes soucis. Ce qui compte, c'est tout le reste concernant le langage. Qu'est-ce que tout cela exactement ? Lisez la suite.

Cet article est divisé en trois parties principales : Le Modèle de Données, le Modèle d'Exécution et l'Analyse Lexicale.

Cet article est plus une plongée dans le fonctionnement des choses dans l'univers Python — en contraste avec comment apprendre Python. Vous trouverez de nombreuses sources d'apprentissage en ligne.

Ce que je n'ai pas trouvé en ligne, c'est une source unique des 'gotchas' courants en Python. Une source expliquant comment le langage fonctionne. Cela tente de résoudre ce problème. Je pense avoir échoué, il y a tellement à dire !

Tout ici provient de la documentation officielle. Je l'ai condensée — aux points importants, réorganisé les choses et ajouté mes exemples. Tous les liens pointent vers la documentation.

Sans plus attendre, c'est parti.

### Modèle de Données

#### Objets, valeurs et types

Les [Objets](https://docs.python.org/3.7/reference/datamodel.html#objects-values-and-types) sont l'abstraction de Python pour les données.

Chaque objet a son `identité` unique fixe, un `type` fixe et une `valeur`.

'Fixe' signifie que l'`identité` et le `type` d'un `Objet` ne peuvent jamais changer.

La `valeur` peut changer. Les objets dont la valeur peut changer sont appelés **mutables** tandis que les objets dont la valeur ne peut pas changer sont appelés **immuables**.

La mutabilité est déterminée par le `type` :

* Les Nombres, les Chaînes de caractères et les Tuples sont immuables
* Les Listes et les Dictionnaires sont mutables

L'identité des objets peut être comparée via l'opérateur `is`.

`id()` retourne l'`identité`

`type()` retourne le `type`

> Note : La valeur d'un objet conteneur immuable qui contient une référence à un objet mutable peut changer lorsque la valeur de ce dernier est modifiée. Cependant, le conteneur est toujours considéré comme immuable, car la collection d'objets qu'il contient ne peut pas être modifiée. Ainsi, l'immuabilité n'est pas strictement la même chose que d'avoir une valeur inchangée.

Cette note m'a fait tourner la tête les deux premières fois que je l'ai lue.

Traduction simple : L'immuabilité n'est pas la même chose qu'une valeur inchangée. Dans l'exemple ci-dessous, le `tuple` est `immuable`, tandis que sa `valeur` continue de changer (à mesure que la `liste` change).

Exemple :

```python
>>> t = ("a", [1]) # un tuple de chaîne et de liste
>>> id(t)
4372661064
>>> t
('a', [1])
>>> type(t)
<class 'tuple'>
>>> t[1]
[1]
>>> t[1].append(2)
>>> t
('a', [1, 2])
>>> id(t)
4372661064
>>> type(t)
<class 'tuple'>
```

Le tuple est immuable, même s'il contient un objet mutable, une liste.

Comparez cela à une chaîne de caractères, où la modification du tableau existant change l'objet (puisque les chaînes sont immuables).

```py
>>> x = "abc"
>>> id(x)
4371437472
>>> x += "d"
>>> x
'abcd'
>>> id(x)
4373053712
```

Ici, le nom, `x` est lié à un autre objet de type chaîne. Cela change également son id.

L'objet original, étant immuable, reste immuable. La liaison est expliquée plus en détail ci-dessous, ce qui devrait clarifier les choses.

#### Types intégrés

Python vient avec plusieurs [types intégrés](https://docs.python.org/3.7/reference/datamodel.html#the-standard-type-hierarchy) :

#### None

Le type est représenté par un seul objet, donc une seule valeur. Le seul objet avec `type = NoneType`

```py
>>> type(None)
<class 'NoneType'>
```

#### Nombres

Ceci est une collection de classes de base abstraites utilisées pour représenter des nombres. Elles ne peuvent pas être instanciées, et `int`, `float` héritent de `numbers.Number`.

Elles sont créées par des littéraux numériques et des opérations arithmétiques. Les objets retournés sont immuables, comme nous l'avons vu. La liste suivante d'exemples rendra cela clair :

```py
>>> a = 3 + 4
>>> type(a)
<class 'int'>
>>> isinstance(a, numbers.Number)
True
>>> isinstance(a, numbers.Integral)
True
>>> isinstance(3.14 + 2j, numbers.Real)
False
>>> isinstance(3.14 + 2j, numbers.Complex)
True
```

#### Séquences

Celles-ci représentent des ensembles ordonnés finis indexés par des entiers non négatifs. Tout comme un tableau dans d'autres langages.

`len()` retourne la longueur des séquences. Lorsque la longueur est `n`, l'ensemble d'index a des éléments de `0...n-1`. Ensuite, le ième élément est sélectionné par `seq[i-1]`.

Pour une séquence `l`, vous pouvez sélectionner des éléments entre les index en utilisant le slicing : `l[i:j]`.

Il existe deux types de séquences : mutables et immuables.

* Les séquences immuables incluent : les chaînes de caractères, les tuples et les bytes.
* Les séquences mutables incluent : les listes et les tableaux d'octets

#### Ensembles

Celles-ci représentent des ensembles non ordonnés, finis d'objets uniques et immuables. Ils ne peuvent pas être indexés, mais peuvent être itérés. `len()` retourne toujours le nombre d'éléments dans l'ensemble.

Il existe deux types d'ensembles : mutables et immuables.

* Un ensemble mutable est créé par `set()`.
* Un ensemble immuable est créé par `frozenset()`.

#### Mappages

#### Dictionnaire

Celles-ci représentent des ensembles finis d'objets indexés par des valeurs presque arbitraires. Les clés ne peuvent pas être des objets mutables. Cela inclut les listes, les autres dictionnaires et les autres objets qui sont comparés par valeur, et non par identité d'objet.

Cela signifie qu'un `frozenset` peut également être une clé de dictionnaire !

#### **Modules**

Un objet module est une unité organisationnelle de base en Python. L'espace de noms est implémenté sous forme de dictionnaire. Les références d'attributs sont des recherches dans ce dictionnaire.

Pour un module `m`, le dictionnaire est en lecture seule, accessible par `m.__dict__`.

C'est un dictionnaire régulier, donc vous pouvez ajouter des clés !

Voici un exemple, avec le [Zen de Python](https://www.python.org/dev/peps/pep-0020/) :

Nous ajoutons notre fonction personnalisée, `figure()` au module `this`.

```
>>> import this as t
>>> t.__dict__
{'__name__': 'this', '__doc__': None, '__package__': '',
.....
.....
's': "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna
vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!",
'd': {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 
'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'},
'c': 97,
'i': 25
}
>>> def figure():
...   print("Can you figure out the Zen of Python?")
... 
>>> t.fig = figure
>>> t.fig()
Can you figure out the Zen of Python?
>>> t.__dict__
{'__name__': 'this', '__doc__': None, '__package__': '',
.....
.....
's': "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna
vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!",
'd': {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 
'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'},
'c': 97,
'i': 25
'fig': <function figure at 0x109872620>
}
>>> print("".join([t.d.get(c, c) for c in t.s]))
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Pas très utile non plus, mais bon à savoir.

#### Surcharge des opérateurs

Python permet la [surcharge des opérateurs](https://docs.python.org/3.7/reference/datamodel.html#special-method-names).

Les classes ont des noms de fonctions spéciaux — des méthodes qu'elles peuvent implémenter pour utiliser les opérateurs définis par Python. Cela inclut le slicing, les opérations arithmétiques et l'indexation.

Par exemple, `__getitem__()` fait référence à l'indexation. Ainsi, `x[i]` est équivalent à `type(x).__getitem__(x,i)`.

Ainsi, pour utiliser l'opérateur `[]` sur une classe `someClass` : vous devez définir `__getitem__()` dans `someClass`.

```py
>>> class operatorTest(object):
...     vals = [1,2,3,4]
...     def __getitem__(self, i):
...         return self.vals[i]
... 
>>> x = operatorTest()
>>> x[2]
3
>>> x.__getitem__(2)
3
>>> type(x)
<class '__main__.OperatorTest'>
>>> type(x).__getitem__(x,2)
3
>>> OperatorTest.__getitem__(x,2)
3
```

Confus quant à la raison pour laquelle tous sont équivalents ? C'est pour la partie suivante — où nous couvrons les définitions de classes et de fonctions.

De même, la [fonction](https://docs.python.org/3.7/reference/datamodel.html#object.__str__) `__str__()` détermine la sortie lorsque la méthode `str()` est appelée sur un objet de votre classe.

Pour les opérations de comparaison, les noms de fonctions spéciaux sont :

* `object.__lt__(self, other)` pour `<` (« inférieur à »)
* `object.__le__(self, other)` pour `≤` (« inférieur ou égal à »)
* `object.__eq__(self, other)` pour `==` (« égal à »)
* `object.__ne__(self, other)` pour `!=` (« différent de »)
* `object.__gt__(self, other)` pour `>` (« supérieur à »)
* `object.__ge__(self, other)` pour `≥` (« supérieur ou égal à »)

Ainsi, par exemple, `x < y` est appelé comme `x.__lt__`(y)

Il existe également des [fonctions spéciales pour les opérations arithmétiques](https://docs.python.org/3.7/reference/datamodel.html#emulating-numeric-types), comme `object.__add__(self, other)`.

Par exemple, `x+y` est appelé comme `x.__add__(y)`

Une autre [fonction](https://docs.python.org/3.7/reference/datamodel.html#object.__iter__) intéressante est `__iter__()`.

Vous appelez cette méthode lorsque vous avez besoin d'un itérateur pour un conteneur. Elle retourne un [nouvel objet itérateur](https://docs.python.org/3.7/library/stdtypes.html#iterator-types) qui peut itérer sur tous les objets dans le conteneur.

Pour les mappages, il devrait itérer sur les clés du conteneur.

L'objet itérateur lui-même supporte deux méthodes :

* `iterator.__iter__()` : Retourne l'objet lui-même.

Cela rend les `itérateurs` et les `conteneurs` équivalents.

Cela permet à l'itérateur et aux conteneurs d'être utilisés dans les instructions `for` et `in`.

* `iterator.__next__()` : Retourne l'élément suivant du conteneur. S'il n'y a plus d'éléments, lève l'exception `StopIteration`.

```py
class IterableObject(object):    # La classe de l'objet itérateur
     vals = []
     it = 0
     def __init__(self, val):
         self.vals = val
         it = 0
 
     def __iter__(self):
         return self
 
     def __next__(self):
         if self.it < len(self.vals):
             index = self.it
             self.it += 1
             return self.vals[index]
         raise StopIteration
 
 class IterableClass(object):    # La classe du conteneur
       vals = [1,2,3,4]
 
       def __iter__(self):
         return iterableObject(self.vals)
>>> iter_object_example = IterableObject([1,2,3])
>>> for val in iter_object_example:
...   print(val)
... 
1
2
3
>>> iter_container_example = IterableClass()
>>> for val in iter_container_example:
...  print(val)
... 
1
2
3
4
```

Chouette, non ? Il existe également un équivalent direct en JavaScript.

Les [Gestionnaires de Contexte](https://docs.python.org/3.7/reference/datamodel.html#with-statement-context-managers) sont également implémentés via la surcharge des opérateurs.

`with open(filename, 'r') as f`

`open(filename, 'r')` est un objet gestionnaire de contexte qui implémente

`object.__enter__(self)` et

`object.__exit__(self, exc_type, exc_value, traceback)`   
Les trois paramètres ci-dessus sont nuls lorsque l'erreur est `None`.

```py
class MyContextManager(object):
    def __init__(self, some_stuff):
        self.object_to_manage = some_stuff
    def __enter__(self):
        print("Entering context management")
        return self.object_to_manage # peut faire quelques transformations aussi
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Successfully exited")
            # Autres choses à fermer
>>> with MyContextManager("file") as f:
...     print(f)
... 
Entering context management
file
Successfully exited
```

Ce n'est pas utile — mais cela fait passer le message. Est-ce que cela le rend utile quand même ?

![Image](https://cdn-media-1.freecodecamp.org/images/vJ7yWCli55L8Sn1i-cnzBNyjXJm8quKKcPRq)
_[Philosoraptor](https://www.google.co.uk/search?q=Philosoraptor" rel="noopener" target="_blank" title=")_

### Modèle d'Exécution

Un bloc est un morceau de code exécuté comme une unité dans un cadre d'exécution.

Exemples de blocs incluent :

* Modules, qui sont des blocs de niveau supérieur
* Corps de fonction
* Définition de classe
* Mais PAS les boucles `for` et autres structures de contrôle

Rappelez-vous comment tout est un `objet` en Python ?

Eh bien, vous avez des `noms` liés à ces `objets`. Ces `noms` sont ce que vous considérez comme des variables.

```py
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

La liaison de noms, ou l'assignation, se produit dans un bloc.

Exemples de liaison de noms — ceux-ci sont intuitifs :

* Les paramètres des fonctions sont liés aux noms définis dans la fonction
* Les instructions d'importation lient le nom du module
* Les définitions de classe et de fonction lient le nom aux objets de classe / fonction
* Gestionnaires de contexte : `with ... as f` : f est la liaison de nom à l'objet `...`

Les noms liés à un bloc sont locaux à ce bloc. Cela signifie que les variables globales sont simplement des noms liés au module.

Les variables utilisées dans un bloc sans y être définies sont des variables libres.

Les portées définissent la visibilité d'un nom dans un bloc. La portée d'une variable inclut le bloc dans lequel elle est définie, ainsi que tous les blocs contenus dans le bloc de définition.

Rappelez-vous comment les boucles for ne sont pas des blocs ? C'est pourquoi les variables d'itération définies dans la boucle sont accessibles après la boucle, contrairement à C++ et JavaScript.

```py
>>> for i in range(5):
...   x = 2*i
...   print(x, i)
... 
0 0
2 1
4 2
6 3
8 4
>>> print(x, i)    # en dehors de la boucle ! x a été défini à l'intérieur.
8 4
```

Lorsque un nom est utilisé dans un bloc, il est résolu en utilisant la portée englobante la plus proche.

> Note : Si une opération de liaison de nom se produit quelque part dans un bloc de code, toutes les utilisations du nom dans le bloc sont traitées comme des références au bloc actuel. Cela peut entraîner des erreurs lorsqu'un nom est utilisé dans un bloc avant d'être lié.

Par exemple :

```
>>> name = "outer_scope"
>>> def foo():
...     name = "inner_function" if name == "outer_scope" \
                else "not_inner_function"
... 
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'name' referenced before assignment
```

C'est une traceback merveilleuse, qui devrait maintenant avoir du sens.

Nous avons le bloc de niveau supérieur, le module — dans lequel il y a un autre bloc, la fonction. Chaque liaison à l'intérieur de la fonction a la fonction comme portée de niveau supérieur !

Ainsi, lorsque vous liez le nom `name` à l'objet `"inner_function"` : avant la liaison, vous vérifiez sa valeur. La règle dit que vous ne pouvez pas le référencer avant la liaison. Exactement la raison de l'`UnboundLocalError`.

![Image](https://cdn-media-1.freecodecamp.org/images/3vBeauEpskRngPsPSWn2ww0KsgA3mNCGGzjl)
_Pas ce type de **Modèle d'Exécution** ? [Source](https://myanimelist.net/featured/1195/Top_25_Badass_Anime_Warrior_Girls" rel="noopener" target="_blank" title=")_

### Analyse Lexicale

Python vous permet d'utiliser des [jonctions de ligne](https://docs.python.org/3.7/reference/lexical_analysis.html#explicit-line-joining). Pour continuer explicitement les lignes, utilisez un antislash.

Les commentaires ne sont pas autorisés après les jonctions de ligne.

```py
if a < 10 and b < 10 \ # Commentaire entraîne SyntaxError
and c < 10: # Commentaire OK
    return True
else:
    return False
```

Implicitement, la jonction de ligne se produit d'elle-même lorsque les éléments sont à l'intérieur d'accolades. Les commentaires sont autorisés ici.

```py
month_names = ['Januari', 'Februari', 'Maart',      # Ce sont les
               'April',   'Mei',      'Juni',       # noms néerlandais
               'Juli',    'Augustus', 'September',  # pour les mois
               'Oktober', 'November', 'December']   # de l'année
```

#### Indentation

Le nombre d'espaces / tabulations dans l'[indentation](https://docs.python.org/3.7/reference/lexical_analysis.html#indentation) n'a pas d'importance, tant qu'il augmente pour les choses qui doivent être indentées. La première ligne ne doit pas être indentée.

La règle des quatre espaces est une convention définie par [PEP 8: Style Guide](https://www.python.org/dev/peps/pep-0008/#string-quotes). C'est une bonne pratique de la suivre.

```py
# Calculer la liste de toutes les permutations de l.
def perm(l):
        # L'indentation des commentaires est ignorée
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]     # Niveau d'indentation choisi
             p = perm(s)             # Doit être au même niveau que ci-dessus
             for x in p:
              r.append(l[i:i+1] + x) # Un espace OK
    return r
```

Il y a aussi quelques identifiants réservés.

* `_` pour l'import : les fonctions / variables commençant par `_` ne sont pas importées.
* `__*__` pour les noms définis par le système, définis par l'implémentation : nous en avons vu quelques-uns. (`__str__()`, `__iter__()`, `__add__()`)

Python offre également une [concatenation implicite de littéraux de chaîne](https://docs.python.org/3.7/reference/lexical_analysis.html#string-literal-concatenation)

```py
>>> def name():
...   return "Neil" "Kakkar"
...
>>> name()
'Neil Kakkar'
```

#### Chaînes de Format

Le [formatage de chaînes](https://docs.python.org/3.7/reference/lexical_analysis.html#formatted-string-literals) est un outil utile en Python.

Les chaînes peuvent avoir `{ expr }` dans le littéral de chaîne où `expr` est une expression. L'évaluation de l'expression est substituée en place.

Les conversions peuvent être spécifiées pour convertir le résultat avant le formatage.

`!r` appelle `repr()`, `!s` appelle `str()` et `!a` appelle `ascii()`

```py
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}."  # repr() est équiv. à !r
"He said his name is 'Fred'."
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # champs imbriqués
'result:      12.35'
# Cela revient au même que "{decf:10.4f}".format(decf=float(value))
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}"  # utilisant le spécificateur de format de date
'January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}"  # utilisant le spécificateur de format hexadécimal
'0x400'
```

C'est une syntaxe plus propre que l'utilisation de `[str.format()](https://docs.python.org/3.7/library/stdtypes.html#str.format)`

### Résumé

Avec cela, nous avons couvert les principaux piliers de Python. Le modèle de données objet, le modèle d'exécution avec ses portées et ses blocs et quelques éléments sur les chaînes. Connaître tout cela vous place devant chaque développeur qui ne connaît que la syntaxe. C'est un nombre plus élevé que vous ne le pensez.

Autres articles de cette série :

* [Comment ne plus avoir peur de Vim](https://medium.freecodecamp.org/how-not-to-be-afraid-of-vim-anymore-ec0b7264b0ae)
* [Comment ne plus avoir peur de GIT](https://medium.freecodecamp.org/how-not-to-be-afraid-of-git-anymore-fe1da7415286)

Vous avez aimé cela ? [Ne manquez plus un article — abonnez-vous à ma liste de diffusion !](http://neilkakkar.com/subscribe/)