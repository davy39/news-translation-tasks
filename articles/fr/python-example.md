---
title: Exemples Python – Structures de données, algorithmes, exemples de code de syntaxe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-31T22:22:00.000Z'
originalURL: https://freecodecamp.org/news/python-example
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e5a740569d1a4ca3ca7.jpg
tags:
- name: Python
  slug: python
seo_title: Exemples Python – Structures de données, algorithmes, exemples de code
  de syntaxe
seo_desc: 'Python is a general purpose programming language which is dynamically typed,
  interpreted, and known for its easy readability with great design principles.

  freeCodeCamp has one of the most popular courses on Python. It''s completely free.
  You can watch...'
---

Python est un langage de programmation généraliste qui est typé dynamiquement, interprété et connu pour sa lisibilité facile avec de grands principes de conception.

freeCodeCamp possède l'un des cours les plus populaires sur Python. Il est complètement gratuit. Vous pouvez [le regarder sur YouTube ici](https://www.youtube.com/watch?v=rfscVS0vtbw).

![Image](https://img.youtube.com/vi/rfscVS0vtbw/maxresdefault.jpg)

# Exemple de structures de données Python

Certaines informations générales sur les nombres à virgule flottante et leur fonctionnement en Python peuvent être trouvées [ici](https://docs.python.org/3/tutorial/floatingpoint.html).

Presque toutes les implémentations de Python suivent la spécification IEEE 754 : Standard pour l'arithmétique binaire en virgule flottante. Plus d'informations sur le [site IEEE](https://en.wikipedia.org/wiki/IEEE_754).

Les objets flottants peuvent être créés en utilisant des [littéraux à virgule flottante](https://docs.python.org/3/reference/lexical_analysis.html#floating-point-literals) :

```text
>>> 3.14
3.14
>>> 314\.    # Zéro(s) final(s) non requis.
314.0
>>> .314    # Zéro(s) initial(s) non requis.
0.314
>>> 3e0
3.0
>>> 3E0     # 'e' ou 'E' peut être utilisé.
3.0
>>> 3e1     # Valeur positive après e déplace la décimale vers la droite.
30.0
>>> 3e-1    # Valeur négative après e déplace la décimale vers la gauche.
0.3
>>> 3.14e+2 # '+' n'est pas requis mais peut être utilisé pour la partie exposant.
314.0
```

Les littéraux numériques ne contiennent pas de signe, cependant la création d'objets flottants négatifs est possible en préfixant avec un opérateur unaire `-` (moins) sans espace avant le littéral :

```
>>> -3.141592653589793
-3.141592653589793
>>> type(-3.141592653589793)
<class 'float'>
```

De même, les objets flottants positifs peuvent être préfixés avec un opérateur unaire `+` (plus) sans espace avant le littéral. Habituellement, `+` est omis :

```text
>>> +3.141592653589793
3.141592653589793
```

Notez que les zéros initiaux et finaux sont valides pour les littéraux à virgule flottante.

De même, les objets flottants positifs peuvent être préfixés avec un opérateur unaire `+` (plus) sans espace avant le littéral. Habituellement, `+` est omis :

```text
>>> +3.141592653589793
3.141592653589793
```

Notez que les zéros initiaux et finaux sont valides pour les littéraux à virgule flottante.

```text
>>> 0.0
0.0
>>> 00.00
0.0
>>> 00100.00100
100.001
>>> 001e0010      # Même que 1e10
10000000000.0
```

Le [constructeur `float`](https://docs.python.org/3/library/functions.html#float) est une autre façon de créer des objets `float`.

La création d'objets `float` avec des littéraux à virgule flottante est préférée lorsque cela est possible :

```
>>> a = 3.14         # Préférer le littéral à virgule flottante lorsque cela est possible.
>>> type(a)
<class 'float'>
>>> b = int(3.14)    # Fonctionne mais inutile.
>>> type(b)
<class 'float'>
```

Cependant, le constructeur float permet de créer des objets float à partir d'autres types de nombres :

```
>>> a = 4
>>> type(a)
<class 'int'>
>>> print(a)
4
>>> b = float(4)
>>> type(b)
<class 'float'>
>>> print(b)
4.0
>>> float(400000000000000000000000000000000)
4e+32
>>> float(.00000000000000000000000000000004)
4e-32
>>> float(True)
1.0
>>> float(False)
0.0
```

Le constructeur `float` créera également des objets `float` à partir de chaînes qui représentent des littéraux numériques :

```
>>> float('1')
1.0
>>> float('.1')
0.1
>>> float('3.')
3.0
>>> float('1e-3')
0.001
>>> float('3.14')
3.14
>>> float('-.15e-2')
-0.0015
```

Le constructeur `float` peut également être utilisé pour créer des représentations numériques de `NaN` (Not a Number), `infinity` négatif et `infinity` (notez que les chaînes pour ceux-ci sont insensibles à la casse) :

```
>>> float('nan')
nan
>>> float('inf')
inf
>>> float('-inf')
-inf
>>> float('infinity')
inf
>>> float('-infinity')
-inf
```

### Nombres complexes

Les nombres complexes ont une partie réelle et une partie imaginaire, chacune représentée par un nombre à virgule flottante.

La partie imaginaire d'un nombre complexe peut être créée en utilisant un littéral imaginaire, ce qui donne un nombre complexe avec une partie réelle de `0.0` :

```python
>>> a = 3.5j
>>> type(a)
<class 'complex'>
>>> print(a)
3.5j
>>> a.real
0.0
>>> a.imag
3.5
```

Aucun littéral n'existe pour créer un nombre complexe avec des parties réelle et imaginaire non nulles. Pour créer un nombre complexe avec une partie réelle non nulle, ajoutez un littéral imaginaire à un nombre à virgule flottante :

```python
>>> a = 1.1 + 3.5j
>>> type(a)
<class 'complex'>
>>> print(a)
(1.1+3.5j)
>>> a.real
1.1
>>> a.imag
3.5
```

Ou utilisez le [constructeur complex](https://docs.python.org/3/library/functions.html#complex).

```python
class complex([real[, imag]])
```

Les arguments utilisés pour appeler le constructeur complex peuvent être de type numérique (y compris `complex`) pour l'un ou l'autre paramètre :

```python
>>> complex(1, 1)
(1+1j)
>>> complex(1j, 1j)
(-1+1j)
>>> complex(1.1, 3.5)
(1.1+3.5j)
>>> complex(1.1)
(1.1+0j)
>>> complex(0, 3.5)
3.5j
```

Une `string` peut également être utilisée comme argument. Aucun deuxième argument n'est autorisé si une chaîne est utilisée comme argument

```python
>>> complex("1.1+3.5j")
(1.1+3.5j)
```

# Exemple de booléens Python

`bool()` est une fonction intégrée dans Python 3. Cette fonction retourne une valeur booléenne, c'est-à-dire Vrai ou Faux. Elle prend un argument, `x`.

## **Arguments**

Elle prend un argument, `x`. `x` est converti en utilisant la procédure standard de [Test de Vérité](https://docs.python.org/3/library/stdtypes.html#truth).

## **Valeur de retour**

Si `x` est faux ou omis, cela retourne `False` ; sinon, cela retourne `True`.

## **Exemple de code**

```
print(bool(4 > 2)) # Retourne True car 4 est supérieur à 2
print(bool(4 < 2)) # Retourne False car 4 n'est pas inférieur à 2
print(bool(4 == 4)) # Retourne True car 4 est égal à 4
print(bool(4 != 4)) # Retourne False car 4 est égal à 4 donc l'inégalité ne tient pas
print(bool(4)) # Retourne True car 4 est une valeur non nulle
print(bool(-4)) # Retourne True car -4 est une valeur non nulle
print(bool(0)) # Retourne False car c'est une valeur nulle
print(bool('dskl')) # Retourne True car la chaîne est une valeur non nulle
print(bool([1, 2, 3])) # Retourne True car la liste est une valeur non nulle
print(bool((2,3,4))) # Retourne True car le tuple est une valeur non nulle
print(bool([])) # Retourne False car la liste est vide et égale à 0 selon le test de valeur de vérité
```

# Exemple d'opérateurs booléens Python

[`and`](https://docs.python.org/3/reference/expressions.html#and), [`or`](https://docs.python.org/3/reference/expressions.html#or), [`not`](https://docs.python.org/3/reference/expressions.html#not)

[Docs Python - Opérations booléennes](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

Ce sont les opérations booléennes, classées par priorité ascendante :

OpérationRésultatNotes x or y si x est faux, alors y, sinon x (1) x and y si x est faux, alors x, sinon y (2) not x si x est faux, alors True, sinon False (3).

**Notes :**

1. Il s'agit d'un opérateur de court-circuit, il n'évalue donc le deuxième argument que si le premier est False.
2. Il s'agit d'un opérateur de court-circuit, il n'évalue donc le deuxième argument que si le premier est True.
3. not a une priorité inférieure aux opérateurs non booléens, donc not a == b est interprété comme not (a == b), et a == not b est une erreur de syntaxe.

## **Exemples :**

### **`not` :**

```
>>> not True
False
>>> not False
True
```

### **`and` :**

```
>>> True and False    # Court-circuité au premier argument.
False
>>> False and True    # Le deuxième argument est évalué.
False
>>> True and True     # Le deuxième argument est évalué.
True
```

### **`or` :**

```
>>> True or False    # Court-circuité au premier argument.
True
>>> False or True    # Le deuxième argument est évalué.
True
>>> False or False   # Le deuxième argument est évalué.
False
```

# Exemple de constantes Python

Trois constantes intégrées couramment utilisées :

* `True` : La valeur vraie du type _bool_. Les affectations à `True` lèvent une _SyntaxError_.
* `False` : La valeur fausse du type _bool_. Les affectations à `False` lèvent une _SyntaxError_.
* `None` : La seule valeur du type _NoneType_. None est fréquemment utilisé pour représenter l'absence de valeur, comme lorsque les arguments par défaut ne sont pas passés à une fonction. Les affectations à `None` lèvent une _SyntaxError_.

Autres constantes intégrées :

* `NotImplemented` : Valeur spéciale qui doit être retournée par les méthodes spéciales binaires, telles que `__eg__()`, `__add__()`, `__rsub__()`, etc.) pour indiquer que l'opération n'est pas implémentée par rapport à l'autre type.
* `Ellipsis` : Valeur spéciale utilisée principalement en conjonction avec la syntaxe de découpage étendue pour les types de données conteneurs définis par l'utilisateur.
* `__debug__` : True si Python n'a pas été démarré avec une option -o.

Constantes ajoutées par le module site. Le module site (qui est importé automatiquement pendant le démarrage, sauf si l'option de ligne de commande -S est donnée) ajoute plusieurs constantes à l'espace de noms intégré. Elles sont utiles pour l'interpréteur de shell interactif et ne doivent pas être utilisées dans les programmes.

Objets qui, lorsqu'ils sont imprimés, impriment un message comme « Utilisez quit() ou Ctrl-D (c'est-à-dire EOF) pour quitter », et lorsqu'ils sont appelés, lèvent SystemExit avec le code de sortie spécifié :

* quit(code=None)
* exit(code=None)

Objets qui, lorsqu'ils sont imprimés, impriment un message comme « Tapez license() pour voir le texte complet de la licence », et lorsqu'ils sont appelés, affichent le texte correspondant de manière paginée (un écran à la fois) :

* copyright
* license
* credits

# Exemple d'appel de fonction Python

Une instruction de définition de fonction n'exécute pas la fonction. L'exécution (l'appel) d'une fonction se fait en utilisant le nom de la fonction suivi de parenthèses contenant les arguments requis (le cas échéant).

```
>>> def say_hello():
...     print('Hello')
...
>>> say_hello()
Hello
```

L'exécution d'une fonction introduit une nouvelle table des symboles utilisée pour les variables locales de la fonction. Plus précisément, toutes les affectations de variables dans une fonction stockent la valeur dans la table des symboles locale. 

D'autre part, les références de variables cherchent d'abord dans la table des symboles locale, puis dans les tables des symboles locales des fonctions englobantes, puis dans la table des symboles globale, et enfin dans la table des noms intégrés. Ainsi, les variables globales ne peuvent pas être directement affectées à une valeur au sein d'une fonction (sauf si elles sont nommées dans une instruction globale), bien qu'elles puissent être référencées.

```
>>> a = 1
>>> b = 10
>>> def fn():
...     print(a)    # a local n'est pas assigné, pas de fonction englobante, a global référencé.
...     b = 20      # b local est assigné dans la table des symboles locale pour la fonction.
...     print(b)    # b local est référencé.
...
>>> fn()
1
20
>>> b               # b global n'est pas changé par l'appel de fonction.
10
```

Les paramètres réels (arguments) d'un appel de fonction sont introduits dans la table des symboles locale de la fonction appelée lorsqu'elle est appelée. De cette manière, les arguments sont passés en utilisant l'appel par valeur (où la valeur est toujours une référence d'objet, pas la valeur de l'objet). Lorsqu'une fonction appelle une autre fonction, une nouvelle table des symboles locale est créée pour cet appel.

```
>>> def greet(s):
...     s = "Hello " + s    # s dans la table des symboles locale est réassigné.
...     print(s)
...
>>> person = "Bob"
>>> greet(person)
Hello Bob
>>> person                  # person utilisé pour appeler reste lié à l'objet original, 'Bob'.
'Bob'
```

Les arguments utilisés pour appeler une fonction ne peuvent pas être réassignés par la fonction, mais les arguments qui référencent des objets mutables peuvent avoir leurs valeurs changées :

```
>>> def fn(arg):
...     arg.append(1)
...
>>> a = [1, 2, 3]
>>> fn(a)
>>> a
[1, 2, 3, 1]
```

# Exemple de classe Python

Les classes fournissent un moyen de regrouper des données et des fonctionnalités ensemble. La création d'une nouvelle classe crée un nouveau type d'objet, permettant de créer de nouvelles instances de ce type. Chaque instance de classe peut avoir des attributs attachés pour maintenir son état. Les instances de classe peuvent également avoir des méthodes (définies par sa classe) pour modifier son état.

Comparé à d'autres langages de programmation, le mécanisme de classe de Python ajoute des classes avec un minimum de nouvelle syntaxe et sémantique. C'est un mélange des mécanismes de classe trouvés en C++. 

Les classes Python fournissent toutes les fonctionnalités standard de la programmation orientée objet : le mécanisme d'héritage de classe permet plusieurs classes de base, une classe dérivée peut remplacer n'importe quelle méthode de sa classe de base ou de ses classes de base, et une méthode peut appeler la méthode d'une classe de base avec le même nom. 

Les objets peuvent contenir des quantités et des types de données arbitraires. Comme c'est vrai pour les modules, les classes participent à la nature dynamique de Python : elles sont créées à l'exécution et peuvent être modifiées davantage après la création.

#### **Syntaxe de définition de classe :**

La forme la plus simple de définition de classe ressemble à ceci :

```python
class ClassName:
    <statement-1>
        ...
        ...
        ...
    <statement-N>
```

#### **Objets de classe :**

Les objets de classe supportent deux types d'opérations : les références d'attributs et l'instanciation.

Les références d'attributs utilisent la syntaxe standard utilisée pour toutes les références d'attributs en Python : `obj.name`. Les noms d'attributs valides sont tous les noms qui étaient dans l'espace de noms de la classe lorsque l'objet de classe a été créé. Donc, si la définition de classe ressemblait à ceci :

```python
class MyClass:
    """ Un exemple simple de classe """
    i = 12345

    def f(self):
        return 'hello world'
```

Alors `MyClass.i` et `MyClass.f` sont des références d'attributs valides, retournant respectivement un entier et un objet fonction. Les attributs de classe peuvent également être assignés, donc vous pouvez changer la valeur de `MyClass.i` par assignation. `__doc__` est également un attribut valide, retournant la docstring appartenant à la classe : `"Un exemple simple de classe"`.

L'instanciation de classe utilise la notation de fonction. Faites simplement semblant que l'objet de classe est une fonction sans paramètre qui retourne une nouvelle instance de la classe. Par exemple (en supposant la classe ci-dessus) :

```python
x = MyClass()
```

Crée une nouvelle instance de la classe et assigne cet objet à la variable locale x.

L'opération d'instanciation (« appel » d'un objet de classe) crée un objet vide. De nombreuses classes aiment créer des objets avec des instances personnalisées pour un état initial spécifique. Par conséquent, une classe peut définir une méthode spéciale nommée **init**(), comme ceci :

```python
def __init__(self):
    self.data = []
```

Lorsque une classe définit une méthode `__init__()`, l'instanciation de la classe appelle automatiquement `__init__()` pour la nouvelle instance de classe créée. Donc dans cet exemple, une nouvelle instance initialisée peut être obtenue par :

```python
x = MyClass()
```

Bien sûr, la méthode `__init__()` peut avoir des arguments pour une plus grande flexibilité. Dans ce cas, les arguments donnés à l'opérateur d'instanciation de classe sont transmis à `__init__()`. Par exemple,

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
              ...

x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

# Exemple de blocs de code et d'indentation Python

Il est généralement bon de ne pas mélanger les tabulations et les espaces lors de la programmation en Python. Faire cela peut éventuellement causer une `TabError`, et votre programme plantera. Soyez cohérent lorsque vous codez - choisissez soit d'indenter en utilisant des tabulations ou des espaces et suivez votre convention choisie dans tout votre programme.

#### **Blocs de code et indentation**

L'une des caractéristiques les plus distinctives de Python est son utilisation de l'indentation pour marquer les blocs de code. Considérez l'instruction if de notre programme simple de vérification de mot de passe :

```python
if pwd == 'apple':
    print('Connexion en cours ...')
else:
    print('Mot de passe incorrect.')

print('Tout est fait !')
```

Les lignes print('Connexion en cours ...') et print('Mot de passe incorrect.') sont deux blocs de code séparés. Ceux-ci se trouvent être d'une seule ligne, mais Python vous permet d'écrire des blocs de code composés de n'importe quel nombre d'instructions.

Pour indiquer un bloc de code en Python, vous devez indenter chaque ligne du bloc du même montant. Les deux blocs de code dans notre exemple d'instruction if sont tous deux indentés de quatre espaces, ce qui est une quantité typique d'indentation pour Python.

Dans la plupart des autres langages de programmation, l'indentation est utilisée uniquement pour aider à rendre le code plus joli. Mais en Python, elle est requise pour indiquer à quel bloc de code une instruction appartient. Par exemple, le dernier print('Tout est fait !') n'est pas indenté, et n'est donc pas partie de l'else-block.

Les programmeurs familiers avec d'autres langages sont souvent irrités à l'idée que l'indentation compte : de nombreux programmeurs aiment la liberté de formater leur code comme ils le souhaitent. Cependant, les règles d'indentation de Python sont assez simples, et la plupart des programmeurs utilisent déjà l'indentation pour rendre leur code lisible. Python va simplement plus loin et donne un sens à l'indentation.

#### **Instructions If/elif**

Une instruction if/elif est une instruction if généralisée avec plus d'une condition. Elle est utilisée pour prendre des décisions complexes. Par exemple, supposons qu'une compagnie aérienne a les tarifs de billet "enfant" suivants : les enfants de 2 ans ou moins volent gratuitement, les enfants de plus de 2 ans mais de moins de 13 ans paient un tarif enfant réduit, et toute personne de 13 ans ou plus paie un tarif adulte régulier. Le programme suivant détermine combien un passager doit payer :

```python
# airfare.py
age = int(input('Quel âge avez-vous ? '))
if age <= 2:
    print(' gratuit')
elif 2 < age < 13:
    print(' tarif enfant')
else:
    print('tarif adulte')
```

Après que Python obtient l'âge de l'utilisateur, il entre dans l'instruction if/elif et vérifie chaque condition l'une après l'autre dans l'ordre où elles sont données. 

Ainsi, il vérifie d'abord si l'âge est inférieur à 2, et si c'est le cas, il indique que le vol est gratuit et saute hors de la condition elif. Si l'âge n'est pas inférieur à 2, alors il vérifie la condition elif suivante pour voir si l'âge est compris entre 2 et 13. Si c'est le cas, il imprime le message approprié et saute hors de l'instruction if/elif. Si ni la condition if ni la condition elif n'est vraie, alors il exécute le code dans le bloc else.

#### **Expressions conditionnelles**

Python a un autre opérateur logique que certains programmeurs aiment (et d'autres non !). C'est essentiellement une notation abrégée pour les instructions if qui peut être utilisée directement dans les expressions. Considérez ce code :

```python
food = input("Quel est votre aliment préféré ? ")
reply = 'beurk' if food == 'lamb' else 'yum'
```

L'expression du côté droit de = dans la deuxième ligne est appelée une expression conditionnelle, et elle évalue soit 'beurk' soit 'yum'. C'est équivalent à ce qui suit :

```python
food = input("Quel est votre aliment préféré ? ")
if food == 'lamb':
   reply = 'beurk'
else:
   reply = 'yum'
```

Les expressions conditionnelles sont généralement plus courtes que les instructions if/else correspondantes, bien que pas aussi flexibles ou faciles à lire. En général, vous devriez les utiliser lorsqu'elles simplifient votre code.

## Exemple d'opérateur de comparaison Python

Il y a huit opérations de comparaison en Python. Elles ont toutes la même priorité (qui est plus élevée que celle des opérations booléennes). Les comparaisons peuvent être enchaînées arbitrairement ; par exemple, `x < y <= z` est équivalent à `x < y and y <= z`, sauf que `y` est évalué une seule fois (mais dans les deux cas `z` n'est pas évalué du tout lorsque `x < y` est trouvé faux).

Ce qui suit résume les opérations de comparaison :

| Opération | Signification| 
| --- | ---|
| `<` | strictement inférieur à |
| `<=` | inférieur ou égal à |
| `>` | strictement supérieur à | 
| `>=` | supérieur ou égal à |
| `==` | égal à |
| `!=` | différent de | 
| `is` | identité d'objet | 
| `is not` | identité d'objet niée |

Les objets de types différents, sauf les différents types numériques, ne sont jamais égaux. De plus, certains types (par exemple, les objets fonction) ne supportent qu'une notion dégénérée de comparaison où deux objets quelconques de ce type sont inégaux. Les opérateurs `<`, `<=`, `>` et `>=` lèveront une exception `TypeError` lors de la comparaison d'un nombre complexe avec un autre type numérique intégré, lorsque les objets sont de types différents qui ne peuvent pas être comparés, ou dans d'autres cas où il n'y a pas d'ordre défini.

Les instances non identiques d'une classe sont normalement comparées comme non égales sauf si la classe définit la méthode `__eq__()`.

Les instances d'une classe ne peuvent pas être ordonnées par rapport à d'autres instances de la même classe, ou à d'autres types d'objet, sauf si la classe définit suffisamment des méthodes `__lt__()`, `__le__()`, `__gt__()`, et `__ge__()` (en général, `__lt__()` et `__eq__()` sont suffisantes, si vous voulez les significations conventionnelles des opérateurs de comparaison).

Le comportement des opérateurs `is` et `is not` ne peut pas être personnalisé ; de plus, ils peuvent être appliqués à n'importe quel couple d'objets et ne lèvent jamais d'exception.

Nous pouvons également enchaîner les opérateurs `<` et `>`. Par exemple, `3 < 4 < 5` retournera `True`, mais `3 < 4 > 5` ne le fera pas. Nous pouvons également enchaîner l'opérateur d'égalité. Par exemple, `3 == 3 < 5` retournera `True` mais `3 == 5 < 5` ne le fera pas.

### **Comparaisons d'égalité - is vs ==**

En Python, il y a deux opérateurs de comparaison qui nous permettent de vérifier si deux objets sont égaux. L'opérateur `is` et l'opérateur `==`. Cependant, il y a une différence clé entre eux !

La différence clé entre is et == peut être résumée comme suit :

* `is` est utilisé pour comparer **l'identité**
* `==` est utilisé pour comparer **l'égalité**

## **Exemple**

Tout d'abord, créez une liste en Python.

```python
myListA = [1,2,3]
```

Ensuite, créez une copie de cette liste.

```python
myListB = myListA
```

Si nous utilisons l'opérateur == ou l'opérateur is, les deux donneront un résultat **True**.

```python
>>> myListA == myListB # les deux listes contiennent des éléments similaires
True
>>> myListB is myListA # myListB contient les mêmes éléments
True
```

C'est parce que myListA et myListB pointent tous deux vers la même variable de liste, que j'ai définie au début de mon programme Python. Les deux listes sont exactement les mêmes, à la fois en identité et en contenu.

Cependant, que se passe-t-il si je crée maintenant une nouvelle liste ?

```python
myListC = [1,2,3]
```

L'exécution de l'opérateur `==` montre toujours que les deux listes sont les mêmes, en termes de contenu.

```python
>>> myListA == myListC
True
```

Cependant, l'exécution de l'opérateur `is` produira maintenant une sortie `False`. C'est parce que myListA et myListC sont deux variables différentes, malgré le fait qu'elles contiennent les mêmes données. Même si elles ont l'air identiques, elles sont **différentes**.

```python
>>> myListA is myListC
False # les deux listes ont des références différentes
```

Pour résumer :

* Une expression `is` renvoie `True` si les deux variables pointent vers la même référence
* Une expression `==` renvoie `True` si les deux variables contiennent les mêmes données

# Exemple de dictionnaire Python

Un dictionnaire (a.k.a dict) en Python est un type de données intégré qui peut être utilisé pour stocker des paires **`clé-valeur`**. Cela vous permet de traiter un **`dict`** comme s'il s'agissait d'une _base de données_ pour stocker et organiser des données.

La chose spéciale à propos des dictionnaires est la manière dont ils sont implémentés. La structure de type table de hachage facilite la vérification de l'existence - ce qui signifie que nous pouvons facilement déterminer si une clé spécifique est présente dans le dictionnaire sans avoir besoin d'examiner chaque élément. L'interpréteur Python peut simplement aller à l'emplacement de la clé et vérifier si la clé est là.

Les dictionnaires peuvent utiliser presque tous les types de données arbitraires, comme des chaînes, des entiers, etc., pour les clés. Cependant, les valeurs qui ne sont pas hachables, c'est-à-dire les valeurs contenant des listes, des dictionnaires ou d'autres types mutables (qui sont comparés par valeur plutôt que par identité d'objet) ne peuvent pas être utilisées comme clés. Les types numériques utilisés pour les clés obéissent aux règles normales de comparaison numérique : si deux nombres sont égaux (comme `1` et `1.0`), ils peuvent être utilisés de manière interchangeable pour indexer la même entrée de dictionnaire. (Notez cependant que, comme les ordinateurs stockent les nombres à virgule flottante sous forme d'approximations, il est généralement déconseillé de les utiliser comme clés de dictionnaire.)

Une exigence très importante d'un dictionnaire est que les clés **doivent** être uniques.

Pour créer un dictionnaire vide, utilisez simplement une paire d'accolades :

```py
    >>> teams = {}
    >>> type(teams)
    >>> <class 'dict'>
```

Pour créer un dictionnaire non vide avec certaines valeurs initiales, placez une liste séparée par des virgules de paires clé-valeur :

```python
    >>> teams = {'barcelona': 1875, 'chelsea': 1910}
    >>> teams
    {'barcelona': 1875, 'chelsea': 1910}
```

Il est facile d'ajouter des paires clé-valeur à un dictionnaire existant :

```python
    >>> teams['santos'] = 1787
    >>> teams
    {'chelsea': 1910, 'barcelona': 1875, 'santos': 1787} # Remarquez l'ordre - Les dictionnaires sont non ordonnés !
    >>> # extraction de la valeur - Il suffit de fournir la clé
    ...
    >>> teams['barcelona']
    1875
```

L'opérateur **`del`** est utilisé pour supprimer une paire clé-valeur du dictionnaire. Dans les scénarios où une clé déjà utilisée est à nouveau utilisée pour stocker des valeurs, l'ancienne valeur associée à cette clé est complètement perdue. De plus, gardez à l'esprit qu'il est erroné d'extraire la valeur en utilisant une clé inexistante.

```
    >>> del teams['santos']
    >>> teams
    {'chelsea': 1910, 'barcelona': 1875}
    >>> teams['chelsea'] = 2017 # écrasement    
    >>> teams
    {'chelsea': 2017, 'barcelona': 1875}
```

Le mot-clé **`in`** peut être utilisé pour vérifier si une clé existe dans le dictionnaire ou non :

```python
    >>> 'sanots' in teams
    False    
    >>> 'barcelona' in teams
    True
    >>> 'chelsea' not in teams
    False
```

**`keys`** est une méthode intégrée qui peut être utilisée pour obtenir les clés d'un dictionnaire donné. Pour extraire les clés présentes dans un dictionnaire sous forme de listes :

```python
    >>> club_names = list(teams.keys())    
    >>> club_names
    ['chelsea', 'barcelona']
```

Une autre façon de créer un dictionnaire est d'utiliser la méthode **`dict()`** :

```python
    >>> players = dict( [('messi','argentina'), ('ronaldo','portugal'), ('kaka','brazil')] ) # séquence de paires clé-valeur est passée  
    >>> players
    {'ronaldo': 'portugal', 'kaka': 'brazil', 'messi': 'argentina'}
    >>> 
    >>> # Si les clés sont des chaînes simples, il est plus facile de spécifier les paires en utilisant des arguments mots-clés
    ...
    >>> dict( totti = 38, zidane = 43 )
    {'zidane': 43, 'totti': 38}
```

Les compréhensions de dictionnaires peuvent également être utilisées pour créer des dictionnaires à partir d'expressions de clés et de valeurs arbitraires :

```python
    >>> {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}
```

**Boucle dans un dictionnaire**  
Pour simplement boucler sur les clés dans le dictionnaire, plutôt que sur les clés et les valeurs :

```python
    >>> d = {'x': 1, 'y': 2, 'z': 3} 
    >>> for key in d:
    ...     print(key) # faire quelque chose
    ...
    x
    y
    z
```

Pour boucler à la fois sur la clé et la valeur, vous pouvez utiliser ce qui suit :  
Pour Python 2.x :

```
    >>> for key, item in d.iteritems():
    ...     print items
    ...
    1
    2
    3
```

Utilisez **`items()`** pour Python 3.x :

```python
    >>> for key, item in d.items():
    ...     print(key, items)
    ...
    x 1
    y 2
    z 3
```

# Exemple d'objets Python

En Python, tout est un _objet_.

Les _objets_ représentent un regroupement logique d'attributs. Les attributs sont des données et/ou des fonctions. Lorsqu'un objet est créé en Python, il est créé avec une _identité_, un _type_ et une _valeur_.

Dans d'autres langages, les _primitives_ sont des _valeurs_ qui n'ont pas de _propriétés_ (attributs). Par exemple, en JavaScript, `undefined`, `null`, `boolean`, `string`, `number` et `symbol` (nouveau dans ECMAScript 2015) sont des primitives.

En Python, il n'y a pas de primitives. `None`, les _booléens_, les _chaînes_, les _nombres_ et même les _fonctions_ sont tous des _objets_, quel que soit leur mode de création.

Nous pouvons démontrer cela en utilisant certaines fonctions intégrées :

* [`id`](https://docs.python.org/3/library/functions.html#id)
* [`type`](https://docs.python.org/3/library/functions.html#type)
* [`dir`](https://docs.python.org/3/library/functions.html#dir)
* [`issubclass`](https://docs.python.org/3/library/functions.html#issubclass)

Les constantes intégrées `None`, `True` et `False` sont des _objets_ :

Nous testons l'objet `None` ici.

```
>>> id(None)
4550218168
>>> type(None)
<class 'NoneType'>
>>> dir(None)
[__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> issubclass(type(None), object)
True
```

Ensuite, inspectons `True`.

```py
>>> id(True)
4550117616
>>> type(True)
<class 'bool'>
>>> dir(True)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> issubclass(type(True), object)
True
```

Pas de raison de laisser `False` de côté !

```py
>>> id(False)
4550117584
>>> type(False)
<class 'bool'>
>>> dir(False)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> issubclass(type(False), object)
True
```

Les _chaînes_, même lorsqu'elles sont créées par des littéraux de chaîne, sont également des _objets_.

```py
>>> id("Hello campers!")
4570186864
>>> type('Hello campers!')
<class 'str'>
>>> dir("Hello campers!")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> issubclass(type('Hello campers!'), object)
True
```

Même chose avec les _nombres_.

```py
>>> id(42)
4550495728
>>> type(42)
<class 'int'>
>>> dir(42)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> issubclass(type(42), object)
True
```

## **Les fonctions sont aussi des objets**

En Python, les fonctions sont des objets de première classe.

Les _fonctions_ en Python sont également des _objets_, créées avec une _identité_, un _type_ et une _valeur_. Elles aussi peuvent être passées dans d'autres _fonctions_ :

```py
>>> id(dir)
4568035688
>>> type(dir)
<class 'builtin_function_or_method'>
>>> dir(dir)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
>>> issubclass(type(dir), object)
True
```

Il est également possible de lier des fonctions à un nom et d'appeler la fonction liée en utilisant ce nom :

```py
>>> a = dir
>>> print(a)
<built-in function dir>
>>> a(a)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
```

## Liaison de nom et alias de fonctions

Lorsque vous définissez une fonction en Python, ce nom de fonction est introduit dans la table des symboles actuelle. La valeur du nom de la fonction a alors un type qui est reconnu comme une fonction définie par l'utilisateur par l'interpréteur :

```py
>>> something = 1
>>> type(something)
<type 'int'>

>>> def something():
...     pass
...
>>> type(something)
<type 'function'>

>>> something = []
>>> type(something)
<type 'list'>
```

La valeur de la fonction peut ensuite être assignée à un autre nom. Après avoir été réassignée, elle peut toujours être utilisée comme une fonction. Utilisez cette méthode pour renommer vos fonctions :

```py
>>> def something(n):
...     print(n)
...
>>> type(something)
<type 'function'>

>>> s = something
>>> s(100)
100
```

# Tuples Python

Un tuple est une séquence d'objets Python. Les tuples sont immuables, ce qui signifie qu'ils ne peuvent pas être modifiés après leur création, contrairement aux listes.

**Création :**

Un tuple vide est créé en utilisant une paire de parenthèses, `()` :

```py
    >>> empty_tuple = ()
    >>> print(empty_tuple)
    ()
    >>> type(empty_tuple)
    <class 'tuple'>
    >>> len(empty_tuple)
    0
```

Un `tuple` avec des éléments est créé en séparant les éléments avec des virgules (les parenthèses entourantes, `()`, sont facultatives avec exceptions) :

```py
    >>> tuple_1 = 1, 2, 3       # Créer un tuple sans parenthèses.
    >>> print(tuple_1)
    (1, 2, 3)
    >>> type(tuple_1)
    <class 'tuple'>
    >>> len(tuple_1)
    3
    >>> tuple_2 = (1, 2, 3)     # Créer un tuple avec parenthèses.
    >>> print(tuple_2)
    (1, 2, 3)
    >>> tuple_3 = 1, 2, 3,      # Virgule finale facultative.
    >>> print(tuple_3)
    (1, 2, 3)
    >>> tuple_4 = (1, 2, 3,)    # Virgule finale dans les parenthèses également facultative.
    >>> print(tuple_4)
    (1, 2, 3)
```

Un `tuple` avec un seul élément doit avoir la virgule finale (avec ou sans parenthèses) :

```
>>> not_tuple = (2)    # Pas de virgule finale fait que ceci n'est pas un tuple.
>>> print(not_tuple)
2
>>> type(not_tuple)
<class 'int'>
>>> a_tuple = (2,)     # Tuple à un seul élément. Nécessite une virgule finale.
>>> print(a_tuple)
(2,)
>>> type(a_tuple)
<class 'tuple'>
>>> len(a_tuple)
1
>>> also_tuple = 2,    # Parentheses omises. Nécessite une virgule finale.
>>> print(also_tuple)
(2,)
>>> type(also_tuple)
<class 'tuple'>
```

Les parenthèses sont requises dans les cas d'ambiguïté (si le tuple fait partie d'une expression plus grande) :

Notez que c'est en fait la virgule qui fait un tuple, pas les parenthèses. Les parenthèses sont facultatives, sauf dans le cas du tuple vide, ou lorsqu'elles sont nécessaires pour éviter l'ambiguïté syntaxique. 

Par exemple, `f(a, b, c)` est un appel de fonction avec trois arguments, tandis que `f((a, b, c))` est un appel de fonction avec un 3-tuple comme argument unique.

```py
    >>> print(1,2,3,4,)          # Appelle print avec 4 arguments : 1, 2, 3, et 4
    1 2 3 4
    >>> print((1,2,3,4,))        # Appelle print avec 1 argument : (1, 2, 3, 4,)
    (1, 2, 3, 4)
    >>> 1, 2, 3 == (1, 2, 3)     # Équivalent à 1, 2, (3 == (1, 2, 3))
    (1, 2, False)
    >>> (1, 2, 3) == (1, 2, 3)   # Utilisez des parenthèses entourantes en cas d'ambiguïté.
    True
```

Un `tuple` peut également être créé avec le constructeur `tuple` :

```py
    >>> empty_tuple = tuple()
    >>> print(empty_tuple)
    ()
    >>> tuple_from_list = tuple([1,2,3,4])
    >>> print(tuple_from_list)
    (1, 2, 3, 4)
    >>> tuple_from_string = tuple("Hello campers!")
    >>> print(tuple_from_string)
    ('H', 'e', 'l', 'l', 'o', ' ', 'c', 'a', 'm', 'p', 'e', 'r', 's', '!')
    >>> a_tuple = 1, 2, 3
    >>> b_tuple = tuple(a_tuple)    # Si le constructeur est appelé avec un tuple pour
    l'itérable,
    >>> a_tuple is b_tuple          # l'argument tuple est retourné.
    True
```

**Accès aux éléments d'un `tuple` :**

Les éléments des `tuples` sont accessibles et indexés de la même manière que les `listes`.

```py
>>> my_tuple = 1, 2, 9, 16, 25
>>> print(my_tuple)
(1, 2, 9, 16, 25)
```

_Indexation à partir de zéro_

```py
    >>> my_tuple[0]
    1
    >>> my_tuple[1]
    2
    >>> my_tuple[2]
    9
```

_Indexation circulaire_

```py
    >>> my_tuple[-1]
    25
    >>> my_tuple[-2]
    16
```

**Empaquetage et dépaquetage :**

L'instruction `t = 12345, 54321, 'hello!'` est un exemple d'empaquetage de tuple : les valeurs `12345`, `54321` et `'hello!'` sont empaquetées ensemble dans un tuple. L'opération inverse est également possible :

```shell
    >>> x, y, z = t
```

Cela s'appelle, de manière appropriée, le dépaquetage de séquence et fonctionne pour toute séquence du côté droit. Le dépaquetage de séquence nécessite qu'il y ait autant de variables du côté gauche du signe égal qu'il y a d'éléments dans la séquence. Notez que l'affectation multiple est en réalité simplement une combinaison d'empaquetage de tuple et de dépaquetage de séquence.

```py
    >>> t = 1, 2, 3    # Empaquetage de tuple.
    >>> print(t)
    (1, 2, 3)
    >>> a, b, c = t    # Dépaquetage de séquence.
    >>> print(a)
    1
    >>> print(b)
    2
    >>> print(c)
    3
    >>> d, e, f = 4, 5, 6    # L'affectation multiple combine l'empaquetage et le dépaquetage.
    >>> print(d)
    4
    >>> print(e)
    5
    >>> print(f)
    6
    >>> a, b = 1, 2, 3       # L'affectation multiple nécessite que chaque variable (droite)
    ait un élément correspondant (gauche).
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: trop de valeurs à dépaqueter (attendu 2)
```

**Immuable :**

Les `tuples` sont des conteneurs immuables, garantissant **quels** objets ils contiennent ne changeront pas. Cela ne garantit **pas** que les objets qu'ils contiennent ne changeront pas :

```shell
    >>> a_list = []
    >>> a_tuple = (a_list,)    # Un tuple (immuable) avec un élément de liste (mutable).
    >>> print(a_tuple)
    ([],)

    >>> a_list.append("Hello campers!")
    >>> print(a_tuple)         # L'élément de l'immuable est muté.
    (['Hello campers!'],)
```

**Utilisations :**

Les fonctions ne peuvent retourner qu'une seule valeur, cependant, un `tuple` hétérogène peut être utilisé pour retourner plusieurs valeurs d'une fonction. Un exemple est la fonction intégrée `enumerate` qui retourne un itérable de `tuples` hétérogènes :

```py
    >>> greeting = ["Hello", "campers!"]
    >>> enumerator = enumerate(greeting)
    >>> enumerator.next()
    >>> enumerator.__next__()
    (0, 'Hello')
    >>> enumerator.__next__()
    (1, 'campers!')
```

# Exemple d'instruction de boucle For Python

Python utilise une boucle for pour itérer sur une liste d'éléments. Cela diffère de C ou Java, qui utilisent la boucle for pour modifier une valeur par étapes et accéder à quelque chose comme un tableau en utilisant cette valeur.

Les boucles For itèrent sur des structures de données basées sur des collections comme les listes, les tuples et les dictionnaires.

La syntaxe de base est :

```python
for value in list_of_values:
  # utiliser la valeur à l'intérieur de ce bloc
```

En général, vous pouvez utiliser n'importe quoi comme valeur d'itérateur, où les entrées de l'itérable peuvent être assignées. Par exemple, vous pouvez dépaqueter des tuples à partir d'une liste de tuples :

```python
list_of_tuples = [(1,2), (3,4)]

for a, b in list_of_tuples:
  print("a:", a, "b:", b)
```

D'autre part, vous pouvez boucler sur n'importe quoi qui est itérable. Vous pouvez appeler une fonction ou utiliser un littéral de liste.

```python
for person in load_persons():
  print("Le nom est:", person.name)
```

```python
for character in ["P", "y", "t", "h", "o", "n"]:
  print("Donnez-moi un '{}'!".format(character))
```

Quelques façons d'utiliser les boucles For :

**Itérer sur la fonction range()**

```python
for i in range(10):
    print(i)
```

Plutôt que d'être une fonction, range est en fait un type de séquence immuable. La sortie contiendra des résultats de la borne inférieure, c'est-à-dire 0 à la borne supérieure, c'est-à-dire 10, mais en excluant 10. Par défaut, la borne inférieure ou l'index de départ est défini à zéro. Sortie :

```text
>
0
1
2
3
4
5
6
7
8
9
>
```

De plus, on peut spécifier la borne inférieure de la séquence et même le pas de la séquence en ajoutant un deuxième et un troisième paramètre.

```py
for i in range(4,10,2): #De 4 à 9 en utilisant un pas de deux
    print(i)
```

Sortie :

```py
>
4
6
8
>
```

**Fonction xrange()**

Pour la plupart, xrange et range sont exactement les mêmes en termes de fonctionnalité. Ils fournissent tous deux un moyen de générer une liste d'entiers pour que vous puissiez l'utiliser comme bon vous semble. La seule différence est que range retourne un objet liste Python et xrange retourne un objet xrange. Cela signifie que xrange ne génère pas réellement une liste statique au moment de l'exécution comme le fait range. Il crée les valeurs au fur et à mesure que vous en avez besoin avec une technique spéciale appelée yield. Cette technique est utilisée avec un type d'objet connu sous le nom de générateurs.

Une autre chose à ajouter. Dans Python 3.x, la fonction xrange n'existe plus. La fonction range fait maintenant ce que xrange fait dans Python 2.x

**Itérer sur les valeurs dans une liste ou un tuple**

```python
A = ["hello", 1, 65, "thank you", [2, 3]]
for value in A:
    print(value)
```

Sortie :

```text
>
hello
1
65
thank you
[2, 3]
>
```

**Itérer sur les clés dans un dictionnaire (aka hashmap)**

```python
fruits_to_colors = {"apple": "#ff0000",
                    "lemon": "#ffff00",
                    "orange": "#ffa500"}

for key in fruits_to_colors:
    print(key, fruits_to_colors[key])
```

Sortie :

```text
>
apple #ff0000
lemon #ffff00
orange #ffa500
>
```

**Itérer sur deux listes de même taille dans une seule boucle avec la fonction zip()**

```python
A = ["a", "b", "c"]
B = ["a", "d", "e"]

for a, b in zip(A, B):
  print a, b, a == b
  
```

Sortie :

```text
>
a a True
b d False
c e False
>
```

**Itérer sur une liste et obtenir l'index correspondant avec la fonction enumerate()**

```python
A = ["this", "is", "something", "fun"]

for index,word in enumerate(A):
    print(index, word)
```

Sortie :

```text
>
0 this
1 is
2 something
3 fun
>
```

Un cas d'utilisation courant est l'itération sur un dictionnaire :

```python
for name, phonenumber in contacts.items():
  print(name, "is reachable under", phonenumber)
```

Si vous avez absolument besoin d'accéder à l'index actuel de votre itération, ne pas utiliser `range(len(iterable))` ! C'est une très mauvaise pratique et vous obtiendrez beaucoup de rires de la part des développeurs Python seniors. Utilisez plutôt la fonction intégrée `enumerate()` :

```python
for index, item in enumerate(shopping_basket):
  print("Item", index, "is a", item)
```

**Instructions for/else** Python vous permet d'utiliser else avec les boucles for, le cas else est exécuté lorsque aucune des conditions dans le corps de la boucle n'a été satisfaite. Pour utiliser else, nous devons utiliser l'instruction `break` afin de pouvoir sortir de la boucle lorsque la condition est satisfaite. Si nous ne sortons pas, alors la partie else sera exécutée.



```python
week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
today = 'Saturday'
for day in week_days:
  if day == today:
    print('today is a week day')
    break
else:
  print('today is not a week day')
```

Dans le cas ci-dessus, la sortie sera `today is not a week day` puisque le break dans la boucle ne sera jamais exécuté.

**Itérer sur une liste en utilisant une fonction de boucle en ligne**

Nous pourrions également itérer en ligne en utilisant Python. Par exemple, si nous devons mettre en majuscules tous les mots d'une liste à partir d'une liste, nous pourrions simplement faire ce qui suit :

```python
A = ["this", "is", "awesome", "shinning", "star"]

UPPERCASE = [word.upper() for word in A]
print (UPPERCASE)
```

Sortie :

```text
>
['THIS', 'IS', 'AWESOME', 'SHINNING', 'STAR']
```

# Exemple de fonction Python

Une fonction vous permet de définir un bloc de code réutilisable qui peut être exécuté plusieurs fois dans votre programme.

Les fonctions vous permettent de créer des solutions plus modulaires et [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) à des problèmes complexes.

Alors que Python fournit déjà de nombreuses fonctions intégrées telles que `print()` et `len()`, vous pouvez également définir vos propres fonctions à utiliser dans vos projets.

L'un des grands avantages de l'utilisation de fonctions dans votre code est qu'il réduit le nombre total de lignes de code dans votre projet.

### **Syntaxe**

En Python, une définition de fonction a les caractéristiques suivantes :

1. Le mot-clé `def`
2. un nom de fonction
3. des parenthèses(), et à l'intérieur des parenthèses des paramètres d'entrée, bien que les paramètres d'entrée soient facultatifs.
4. un deux-points :
5. un bloc de code à exécuter
6. une instruction de retour (facultative)

```python
# une fonction sans paramètres ou valeurs retournées
def sayHello():
  print("Hello!")

sayHello()  # appelle la fonction, 'Hello!' est imprimé sur la console

# une fonction avec un paramètre
def helloWithName(name):
  print("Hello " + name + "!")

helloWithName("Ada")  # appelle la fonction, 'Hello Ada!' est imprimé sur la console

# une fonction avec plusieurs paramètres avec une instruction de retour
def multiply(val1, val2):
  return val1 * val2

multiply(3, 5)  # imprime 15 sur la console
```

Les fonctions sont des blocs de code qui peuvent être réutilisés simplement en appelant la fonction. Cela permet une réutilisation de code simple et élégante sans réécrire explicitement des sections de code. Cela rend le code plus lisible, plus facile à déboguer et limite les erreurs de frappe.

Les fonctions en Python sont créées en utilisant le mot-clé `def`, suivi d'un nom de fonction et des paramètres de fonction à l'intérieur des parenthèses.

Une fonction retourne toujours une valeur. Le mot-clé `return` est utilisé par la fonction pour retourner une valeur. Si vous ne voulez pas retourner de valeur, la valeur par défaut `None` sera retournée.

Le nom de la fonction est utilisé pour appeler la fonction, en passant les paramètres nécessaires à l'intérieur des parenthèses.



```python
# ceci est une fonction de somme de base
def sum(a, b):
  return a + b

result = sum(1, 2)
# result = 3
```

Vous pouvez définir des valeurs par défaut pour les paramètres, et ainsi Python interprétera que la valeur de ce paramètre est celle par défaut si aucune n'est donnée.

```python
def sum(a, b=3):
  return a + b

result = sum(1)
# result = 4
```

Vous pouvez passer les paramètres dans l'ordre que vous souhaitez, en utilisant le nom du paramètre.

```python
result = sum(b=2, a=2)
# result = 4
```

Cependant, il n'est pas possible de passer un argument mot-clé avant un argument non mot-clé.

```python
result = sum(3, b=2)
#result = 5
result2 = sum(b=2, 3)
#Lèvera une SyntaxError
```

Les fonctions sont également des objets, vous pouvez donc les assigner à une variable et utiliser cette variable comme une fonction.

```python
s = sum
result = s(1, 2)
# result = 3
```

### **Notes**

Si une définition de fonction inclut des paramètres, vous devez fournir le même nombre de paramètres lorsque vous appelez la fonction.

```python
print(multiply(3))  # TypeError: multiply() prend exactement 2 arguments (0 donné)

print(multiply('a', 5))  # 'aaaaa' imprimé sur la console

print(multiply('a', 'b'))  # TypeError: Python ne peut pas multiplier deux chaînes
```

Le bloc de code que la fonction exécutera inclut toutes les instructions indentées dans la fonction.

```python
def myFunc():
print('ceci sera imprimé')
print('ceci aussi')

x = 7
# l'affectation de x ne fait pas partie de la fonction puisqu'elle n'est pas indentée
```

Les variables définies dans une fonction n'existent que dans le cadre de cette fonction.

```python
def double(num):
x = num * 2
return x

print(x)  # erreur - x n'est pas défini
print(double(4))  # imprime 8
```

Python interprète le bloc de fonction uniquement lorsque la fonction est appelée et non lorsque la fonction est définie. Ainsi, même si le bloc de définition de la fonction contient une sorte d'erreur, l'interpréteur Python ne la signalera que lorsque la fonction sera appelée.

# Exemple de générateur Python

Les générateurs sont un type spécial de fonction qui vous permet de retourner des valeurs sans terminer une fonction. Ils le font en utilisant le mot-clé `yield`. Similaire à `return`, l'expression `yield` retournera une valeur à l'appelant. La différence clé entre les deux est que `yield` suspendra la fonction, permettant à d'autres valeurs d'être retournées à l'avenir.

Les générateurs sont itérables, ils peuvent donc être utilisés proprement avec des boucles for ou tout autre chose qui itère.



```python
def my_generator():
    yield 'hello'
    yield 'world'
    yield '!'

for item in my_generator():
    print(item)

# sortie:
# hello
# world
# !
```

Comme d'autres itérateurs, les générateurs peuvent être passés à la fonction `next` pour récupérer l'élément suivant. Lorsqu'un générateur n'a plus de valeurs à retourner, une erreur `StopIteration` est levée.

```python
g = my_generator()
print(next(g))
# 'hello'
print(next(g))
# 'world'
print(next(g))
# '!'
print(next(g))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
```

Les générateurs sont particulièrement utiles lorsque vous devez créer un grand ensemble de valeurs mais que vous n'avez pas besoin de les garder toutes en mémoire en même temps. Par exemple, si vous devez imprimer le premier million de nombres de Fibonacci, vous retourneriez généralement une liste d'un million de valeurs et itéreriez sur la liste pour imprimer chaque valeur. Cependant, avec un générateur, vous pouvez retourner chaque valeur une à la fois :

```python
def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fib(1000000):
    print(x)
```

# Exemple d'itérateur Python

Python supporte un concept d'itération sur des conteneurs. Cela est implémenté en utilisant deux méthodes distinctes ; celles-ci sont utilisées pour permettre aux classes définies par l'utilisateur de supporter l'itération.

[Docs Python - Types d'itérateurs](https://docs.python.org/3/library/stdtypes.html#iterator-types)

L'itération est le processus de répétition programmatique d'une étape un nombre donné de fois. Un programmeur peut utiliser l'itération pour effectuer la même opération sur chaque élément d'une collection de données, par exemple imprimer chaque élément d'une liste.

* Les objets peuvent implémenter une méthode `__iter__()` qui retourne un objet itérateur pour supporter l'itération.

Les objets itérateurs doivent implémenter :

* `__iter__()` : retourne l'objet itérateur.
* `__next__()` : retourne le prochain objet du conteneur. iterator_object = 'abc'.**iter**_() print(iteratorobject) print(id(iterator_object)) print(id(iterator_object.**iter**())) # Retourne l'itérateur lui-même. print(iterator_object.**next**_()) # Retourne le 1er objet et avance l'itérateur. print(iteratorobject.**next**()) # Retourne le 2ème objet et avance l'itérateur. print(iterator_object.**next**_()) # Retourne le 3ème objet et avance l'itérateur. print(iteratorobject.**next**()) # Lève une exception StopIteration.

Sortie :

```text
<str_iterator object at 0x102e196a0>
4343305888
4343305888
a
b
c
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-1-d466eea8c1b0> in <module>()
      6 print(iterator_object.__next__())     # Retourne le 2ème objet et avance l'itérateur.
      7 print(iterator_object.__next__())     # Retourne le 3ème objet et avance l'itérateur.
----> 8 print(iterator_object.__next__())     # Lève une exception StopIteration.

StopIteration:
```

# **Opérateur ternaire en Python Exemple**

Les opérations ternaires en Python, souvent également appelées expressions conditionnelles, permettent au programmeur d'effectuer une évaluation et de retourner une valeur basée sur la vérité de la condition donnée.

L'opérateur ternaire diffère d'une structure `if`, `else`, `elif` standard en ce sens qu'il n'est pas une structure de contrôle de flux, et se comporte davantage comme d'autres opérateurs tels que `==` ou `!=` dans le langage Python.

### **Exemple**

Dans cet exemple, la chaîne `Even` est retournée si la variable `val` est paire, sinon la chaîne `Odd` est retournée. La chaîne retournée est ensuite assignée à la variable `is_even` et imprimée sur la console.

#### **Entrée**

```python
for val in range(1, 11):
    is_even = "Even" if val % 2 == 0 else "Odd"
    print(val, is_even, sep=' = ')
```

#### **Sortie**

```text
1 = Odd
2 = Even
3 = Odd
4 = Even
5 = Odd
6 = Even
7 = Odd
8 = Even
9 = Odd
10 = Even
```

# Exemple d'instruction de boucle While Python

Python utilise la boucle `while` de manière similaire à d'autres langages populaires. La boucle `while` évalue une condition puis exécute un bloc de code si la condition est vraie. Le bloc de code s'exécute de manière répétée jusqu'à ce que la condition devienne fausse.

La syntaxe de base est :

```python
counter = 0
while counter < 10:
   # Exécute le bloc de code ici tant que
   # counter est inférieur à 10
```

Un exemple est montré ci-dessous :

```python
days = 0    
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
while days < 7:
   print("Today is " + week[days])
   days += 1
```

Sortie :



```text
Today is Monday
Today is Tuesday
Today is Wednesday
Today is Thursday
Today is Friday
Today is Saturday
Today is Sunday
```

Explication ligne par ligne du code ci-dessus :

1. la variable days est définie à une valeur de 0.
2. une variable week est assignée à une liste contenant tous les jours de la semaine.
3. la boucle while commence
4. le bloc de code sera exécuté jusqu'à ce que la condition retourne true.
5. la condition est days<7 ce qui signifie approximativement exécuter la boucle while jusqu'à ce que la variable days soit inférieure à 7
6. Donc lorsque days=7 la boucle while arrête de s'exécuter.
7. la variable days est mise à jour à chaque itération.
8. Lorsque la boucle while s'exécute pour la première fois, la ligne Today is Monday est imprimée sur la console et la variable days devient égale à 1.
9. Puisque la variable days est égale à 1 ce qui est inférieur à 7, la boucle while est exécutée à nouveau.
10. Cela continue encore et encore et lorsque la console imprime Today is Sunday la variable days est maintenant égale à 7 et la boucle while arrête de s'exécuter.

## f-strings en Python

Dans la version 3.6 de Python, une nouvelle méthode de formatage de chaînes a été implémentée. La nouvelle méthode est appelée interpolation de chaînes littérales (bien que communément appelée f-string).

L'utilisation de f-string permet au programmeur d'insérer dynamiquement une variable dans une chaîne de manière propre et concise. En plus d'insérer des variables dans une chaîne, cette fonctionnalité offre également la possibilité au programmeur d'évaluer des expressions, de joindre le contenu d'une collection, et même d'invoquer des fonctions au sein de la f-string.

Pour effectuer ces comportements dynamiques au sein d'une f-string, nous les enveloppons à l'intérieur d'accolades dans la chaîne, et nous ajoutons un f minuscule au début de la chaîne (avant la guillemet ouvrant.

### **Exemples**

Insertion dynamique d'une variable dans une chaîne à l'exécution :

```python
name = 'Jon Snow'
greeting = f'Hello! {name}'
print(greeting)
```

Évaluation d'une expression dans une chaîne :

```python
val1 = 2
val2 = 3
expr = f'The sum of {val1} + {val2} is {val1 + val2}'
print(expr)
```

Appel d'une fonction et insertion de la sortie dans une chaîne :

```python
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

func = f'The sum of 3 + 5 is {sum(3, 5)}'
print(func)
```

Jointure du contenu d'une collection dans une chaîne :

```python
fruits = ['Apple', 'Banana', 'Pear']

list_str = f'List of fruits: {", ".join(fruits)}'
print(list_str)
```

# Comment installer Python 3

Vous pouvez télécharger Python à partir de ce lien officiel [lien](https://www.python.org/downloads/). En fonction de votre système d'exploitation (Windows ou Linux ou OSX), vous pourriez vouloir installer Python 3 en suivant [ces instructions](http://docs.python-guide.org/en/latest/starting/installation/).

## **Utilisation des environnements virtuels**

Il est toujours une bonne idée de [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) votre installation Python et de la garder séparée de votre _Python système_. Le _Python système_ est le chemin vers l'interpréteur Python, qui est utilisé par d'autres modules installés avec votre système d'exploitation.

Il n'est **pas sûr** d'installer des frameworks ou des bibliothèques Python Web directement en utilisant le _Python système_. Au lieu de cela, vous pouvez utiliser [Virtualenv](https://virtualenv.readthedocs.org/en/latest/) pour créer et lancer un processus Python séparé lorsque vous développez des applications Python.

### **Virtualenvwrapper**

Le [module Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) facilite la gestion et le sandboxing de plusieurs environnements Python sandboxés sur une seule machine, sans corrompre aucun module ou service écrit en Python et utilisé par votre machine.

Bien sûr, la plupart des environnements de développement hébergés dans le cloud tels que [Nitrous](https://www.nitrous.io/) ou [Cloud9](https://c9.io/) viennent également avec ceux-ci préinstallés et prêts pour que vous commenciez à coder ! Vous pouvez rapidement choisir une boîte à partir de votre tableau de bord et commencer à coder après avoir activé un environnement Python 3.

Dans [Cloud9](https://c9.io/), vous devez sélectionner la boîte Django lors de la création d'un nouvel environnement de développement.

Quelques exemples de commandes shell suivent. Si vous souhaitez copier-coller, notez que le signe `$` est un raccourci pour l'invite de terminal, il ne fait pas partie de la commande. Mon invite de terminal ressemble à ceci :

```text
alayek:~/workspace (master) $
```

Et, un `ls` ressemblerait à

```text
alayek:~/workspace (master) $ ls
```

Mais, en l'écrivant dans cette documentation, je l'écrirais comme

```text
$ ls
```

Revenant à notre discussion, vous pouvez créer un sandbox Python 3 incluant l'interpréteur sur Cloud9 en exécutant sur votre terminal cloud :

```text
$ mkvirtualenv py3 --python=/usr/bin/python3
```

Vous devez l'exécuter une seule fois après avoir créé une nouvelle boîte pour votre projet. Une fois exécutée, cette commande créera un nouvel environnement virtuel sandboxé prêt à être utilisé, nommé `py3`.

Pour voir les environnements virtuels disponibles, vous pouvez utiliser

```text
$ workon
```

Pour activer `py3`, vous pouvez utiliser la commande `workon` avec le nom de l'environnement :

```text
$ workon py3
```

Les trois commandes de terminal ci-dessus fonctionneraient également sur des machines locales Linux ou des machines OSX. Ce sont des commandes [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/#introduction) ; donc si vous prévoyez de les utiliser, assurez-vous d'avoir ce module installé et ajouté à la variable `PATH`.

Si vous êtes à l'intérieur d'un environnement virtuel ; vous pouvez facilement le découvrir en vérifiant votre invite de terminal. Le nom de l'environnement sera clairement affiché dans votre invite de terminal.

Par exemple, lorsque je suis à l'intérieur de l'environnement `py3`, je verrai ceci comme mon invite de terminal :

```text
(py3)alayek:~/workspace (master) $
```

Remarquez le `(py3)` entre parenthèses ! Si pour une raison quelconque vous ne voyez pas cela, même si vous êtes à l'intérieur d'un environnement virtuel ; vous pouvez essayer de faire l'une des choses [mentionnées ici](http://stackoverflow.com/questions/1871549/python-determine-if-running-inside-virtualenv).

Pour sortir d'un environnement virtuel ou pour le désactiver - utilisez cette commande :

```text
$ deactivate
```

Encore une fois, cela fonctionne uniquement avec le module virtualenvwrapper.

### **Pipenv**

Une alternative à l'utilisation de virtualenvwrapper est [Pipenv](https://docs.pipenv.org/). Il crée automatiquement des environnements virtuels pour vos projets et maintient un fichier `Pipfile` qui contient les dépendances. L'utilisation de Pipenv signifie que vous n'avez plus besoin d'utiliser pip et virtualenv séparément, ou de gérer votre propre fichier `requirements.txt`. Pour ceux qui sont familiers avec JavaScript, Pipenv est similaire à l'utilisation d'un outil de packaging comme `npm`.

Pour commencer avec Pipenv, vous pouvez suivre ce guide très détaillé [guide](https://docs.pipenv.org/install.html#installing-pipenv). Pipenv facilite la [spécification de la version de Python](https://docs.pipenv.org/basics.html#specifying-versions-of-python) que vous souhaitez utiliser pour chaque projet, [importer](https://docs.pipenv.org/basics.html#importing-from-requirements-txt) à partir d'un fichier `requirements.txt` existant et [grapher](https://docs.pipenv.org/#pipenv-graph) vos dépendances.