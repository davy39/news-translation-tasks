---
title: Le Manuel d'Exemples de Code Python – Exemples de Programmes Python Simples
  pour Débutants
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-05-04T17:20:38.000Z'
originalURL: https://freecodecamp.org/news/python-code-examples-simple-python-program-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Python-Code-Examples-Handbook-Mockup.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: handbook
  slug: handbook
- name: Python
  slug: python
seo_title: Le Manuel d'Exemples de Code Python – Exemples de Programmes Python Simples
  pour Débutants
seo_desc: 'Python is a high-level, general purpose, interpreted programming language.
  It''s well-known for being very easy to learn yet powerful, and it has many uses
  in many different fields.

  If you''re someone trying to get started with Python, it''s easy to get...'
---

Python est un langage de programmation interprété, de haut niveau et à usage général. Il est bien connu pour être très facile à apprendre tout en étant puissant, et il a de nombreuses utilisations dans de nombreux domaines différents.

Si vous êtes quelqu'un qui essaie de commencer avec Python, il est facile de se perdre parmi toutes les excellentes ressources d'apprentissage sur Internet.

Maintenant, cet article n'essaie pas d'être une autre tête dans cette foule. Plutôt, ici je vais vous introduire aux bases de Python et je vais vous orienter dans la bonne direction.

Dans cet article, je vais vous introduire aux fondamentaux du langage de programmation Python avec l'aide d'une tonne d'exemples de code. Je vais les expliquer en détail et inclure des liens pour une étude plus approfondie.

Une fois que je vous aurai introduit au langage à un niveau de base, je vous suggérerai quelques excellentes ressources d'apprentissage et expliquerai comment en tirer le meilleur parti.

Bien que j'expliquerai les exemples de code en détail, je suppose que vous êtes familier avec les concepts de programmation courants tels que les expressions, les instructions, les variables, les fonctions, et ainsi de suite. Donc je ne passerai pas de temps à expliquer ces concepts de programmation en détail – plutôt je me concentrerai sur la manière de Python de les implémenter/utiliser.

Sans plus tarder, plongeons-nous dedans !

## Table des Matières

* [Aperçu de Haut Niveau de Python](#heading-aperçu-de-haut-niveau-de-python)
* [Comment Écrire Bonjour, le Monde ! en Python](#heading-comment-écrire-bonjour-le-monde-en-python)
* [Variables en Python](#heading-variables-en-python)
* [Types de Données en Python](#heading-types-de-données-en-python)
* [Comment Écrire des Commentaires en Python](#heading-comment-écrire-des-commentaires-en-python)
* [Chaînes de Caractères en Python](#heading-chaînes-de-caractères-en-python)
* [Nombres en Python](#heading-nombres-en-python)
* [Comment Gérer l'Entrée Utilisateur en Python](#heading-comment-gérer-lentrée-utilisateur-en-python)
* [if-else-elif en Python](#heading-if-else-elif-en-python)
* [match-case en Python](#heading-match-case-en-python)
* [Listes et Tuples en Python](#heading-listes-et-tuples-en-python)
* [Boucles en Python](#heading-boucles-en-python)
* [Dictionnaires en Python](#heading-dictionnaires-en-python)
* [Fonctions en Python](#heading-fonctions-en-python)
* [Ressources d'Apprentissage Python Supplémentaires](#heading-ressources-dapprentissage-python-supplémentaires)
* [Conclusion](#heading-conclusion)

## Aperçu de Haut Niveau de Python

Avant de me lancer dans le codage, vous devrez avoir Python installé et prêt à fonctionner sur votre système. Selon le système que vous utilisez – Windows, macOS ou Linux – le processus d'installation sera différent.

Si vous êtes sous Windows, mon collègue auteur de freeCodeCamp [Md. Fahim Bin Amin](https://www.freecodecamp.org/news/author/fahimbinamin/) a écrit un excellent guide sur [Comment Installer Python sur Windows](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/). Un autre auteur [Dillion Megida](https://www.freecodecamp.org/news/author/dillionmegida/) a écrit un autre excellent article sur [Comment Installer Python 3 sur Mac](https://www.freecodecamp.org/news/how-to-install-python-3-on-mac-and-update-the-python-version-macos-homebrew-command-guide/).

Certaines plateformes, comme certaines des distributions Linux modernes, viennent avec une version assez à jour de Python préinstallée. Donc si vous êtes sous Linux, exécutez la commande suivante pour vérifier votre version de Python :

```shell
python3 --version
```

Avoir n'importe quelle version de Python 3 installée sur votre système suffira. En plus de Python, vous aurez également besoin d'un éditeur de code ou d'un IDE bien adapté pour écrire du code Python.

Dans mon article [Python IDE – Meilleurs IDE et Éditeurs pour Python](https://www.freecodecamp.org/news/python-ide-best-ides-and-editors-for-python/) j'ai listé trois des meilleurs éditeurs de code et IDE que vous pouvez utiliser pour écrire du code Python.

Donc si vous avez Python et un éditeur de code ou un IDE prêt à fonctionner, passons à l'écriture de votre premier morceau de code Python.

### Comment Écrire Bonjour, le Monde ! en Python

Quelque part dans votre ordinateur, créez un nouveau fichier nommé `program.py` et mettez le code suivant dedans :

```python
print('Bonjour, le Monde !')
```

Pour exécuter ce code, ouvrez votre terminal dans le répertoire où vous avez mis le fichier `program.py` et exécutez la commande suivante :

```shell
# sur Windows et macOS
python program.py

# sur Linux
python3 program.py
```

La sortie du code sera ce que vous avez passé comme paramètre de la fonction `print()`, qui dans le cas de cet extrait de code est :

```shell
Bonjour, le Monde !
```

Comme vous l'avez peut-être déjà deviné, `print()` est une fonction intégrée de Python qui imprime ce que vous lui donnez sur la console. La fonction peut imprimer des chaînes de caractères, des nombres, des expressions – plus ou moins tout ce que vous pouvez lui lancer.

```python
print('Bonjour, le Monde !')
print(100)
print(5 + 5)
```

La première instruction imprime la chaîne de caractères `Bonjour, le Monde !` comme avant. La deuxième imprime un nombre et la troisième imprime le résultat de l'expression `5 + 5` :

```shell
Bonjour, le Monde !
100
10
```

Une chose que vous avez peut-être remarquée ou non est que les trois instructions print ont été sorties sur trois lignes séparées. Alors que dans d'autres langages comme C/C++/C#/Java, vous devez ajouter explicitement un caractère de nouvelle ligne.

Il s'avère que `print()` fonctionne comme un caractère de nouvelle ligne par défaut et vous pouvez remplacer ce comportement par défaut comme suit :

```python
print('Bonjour, le Monde !', end=' | ')
print(100, end=' | ')
print(5 + 5)
```

Maintenant, la sortie du programme sera :

```shell
Bonjour, le Monde ! | 100 | 10
```

Ce qui signifie que toute chaîne de caractères que vous passez comme valeur du paramètre `end` sera utilisée comme caractère de terminaison de la ligne imprimée.

Ici, j'ai utilisé `|` comme caractère de terminaison des deux premières instructions. Cependant, j'ai utilisé le caractère de nouvelle ligne par défaut comme caractère de terminaison de la dernière instruction.

Vous pouvez en apprendre plus sur la fonction `print()` en jouant avec ou en lisant la [documentation officielle](https://docs.python.org/3/library/functions.html#print) sur la fonction.

### Variables en Python

Pour déclarer une variable en Python, vous commencez par écrire le nom de la variable, puis un signe égal, suivi de la valeur de la variable :

```python
nom = 'Farhan'

print('Mon nom est ' + nom)
```

La sortie de ce code sera :

```shell
Mon nom est Farhan
```

Comme vous pouvez le voir, il n'y a pas de mot-clé spécial pour déclarer une variable. Python est assez intelligent pour obtenir le type de la variable à partir de la valeur que vous attribuez.

Dans l'exemple ci-dessus, la variable `nom` contient la chaîne de caractères `Farhan`. Puisque le mot `Farhan` est entre guillemets, Python traitera cette variable comme une chaîne de caractères.

En Python, vous pouvez concaténer deux chaînes de caractères en utilisant le signe plus. C'est ce que nous avons fait dans l'instruction `print()` ci-dessus. Mais si vous changez le code comme suit :

```python
nom = 'Farhan'
âge = 27

print('Mon nom est ' + nom)
print('Jai ' + âge + ' ans')
```

Et essayez d'exécuter ce programme, vous rencontrerez le problème suivant :

```shell
Mon nom est Farhan
Traceback (most recent call last):
  File "C:\Users\shovi\repos\python-playground\hello-world.py", line 5, in <module>
    print('Jai ' + âge + ' ans')
TypeError: can only concatenate str (not "int") to str
```

Comme vous pouvez le voir, les chaînes de caractères ne peuvent être concaténées qu'avec des chaînes de caractères, et la variable `âge` est un entier. Il existe une meilleure façon d'intégrer des variables dans des instructions de chaîne de caractères.

```python
nom = 'Farhan'
âge = 27

print(f'Mon nom est {nom}')
print(f'Jai {âge} ans')
```

J'espère que vous avez remarqué le `f` au début des chaînes de caractères à l'intérieur des instructions `print()`. Ce `f` transforme les chaînes de caractères en f-strings. Ces chaînes de caractères sont évaluées à l'exécution, donc à l'intérieur d'une f-string, vous pouvez mettre n'importe quelle instruction Python valide entre accolades. Cela rend l'intégration de variables ou même de logique simple dans des chaînes de caractères très facile.

Vous pouvez redéclarer vos variables n'importe où dans le programme. Vous pouvez même changer leurs types si vous le souhaitez.

```python
a = 'ceci est une chaîne de caractères'

a = 10

print(a)
```

Ceci est un programme complètement valide et la valeur de `a` sera imprimée comme `10` puisque vous avez remplacé la valeur initiale à la deuxième ligne.

### Types de Données en Python

En Python, il y a quatre principaux types littéraux dont vous devez être conscient :

| Type           | Exemple        |
| -------------- | -------------- |
| Entier         | 1              |
| Nombre à virgule flottante | 2.0            |
| Booléen        | True           |
| Chaîne de caractères         | 'freeCodeCamp' |

Les entiers et les nombres à virgule flottante sont auto-explicatifs. Un booléen peut être soit `vrai` soit `faux`, et les chaînes de caractères en Python peuvent être enfermées soit dans des guillemets simples soit dans des guillemets doubles. Je préfère utiliser des guillemets simples. Vous pouvez utiliser celui que vous préférez mais essayez de ne pas mélanger les deux types de guillemets ensemble.

### Commentaires en Python

Les commentaires en Python commencent par un symbole dièse :

```python
# ceci est un commentaire
```

Les commentaires écrits en utilisant un dièse ne peuvent être que sur une seule ligne. Si vous voulez écrire un commentaire sur plusieurs lignes en Python, vous devrez utiliser des guillemets comme suit :

```python
'''ceci est un commentaire
 qui continue
 et continue
 et continue...'''
```

Commenter votre code selon les besoins est une bonne façon de le documenter. Mais assurez-vous de ne pas ajouter de commentaires là où le code peut être facilement compris en le regardant simplement.

### Chaînes de Caractères en Python

Les chaînes de caractères en Python sont des collections ordonnées de caractères Unicode. Les chaînes de caractères ne peuvent pas être modifiées à l'exécution. Vous avez déjà vu comment déclarer une chaîne de caractères. Dans cette section, vous apprendrez les opérations courantes sur les chaînes de caractères.

Dans une chaîne de caractères, chaque caractère aura un index. Et comme les tableaux, les index des chaînes de caractères commencent à zéro.

```python
nom = 'Farhan'

# F -> 0
# a -> 1
# r -> 2
# h -> 3
# a -> 4
# n -> 5
```

Ces caractères peuvent être accessibles en utilisant ces index comme suit :

```python
nom = 'Farhan'

print(nom[0])
print(nom[1])
print(nom[2])
print(nom[3])
print(nom[4])
print(nom[5])
```

La sortie de ce programme sera comme suit :

```shell
F
a
r
h
a
n
```

Une autre chose amusante que vous pouvez faire en utilisant ces index est le découpage. Supposons que vous voulez prendre une partie d'une chaîne de caractères.

```python
nom = 'Farhan'

print(nom[0:3])
```

La sortie de ce programme sera :

```shell
Far
```

Dans cet exemple, `nom[0:3]` signifie imprimer en commençant par l'index `0` jusqu'à l'index `3`. Maintenant, vous pouvez penser que `h` est à l'index `3` et vous aurez raison à ce sujet. Mais le truc avec le découpage est qu'il n'inclut pas le caractère à l'index de fin.

Si vous souhaitez en apprendre plus sur le découpage, il y a un article intitulé [Comment Sous-chaîner une Chaîne de Caractères en Python](https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/) que vous pourriez trouver utile.

Vous pouvez utiliser la fonction `len()` pour déterminer la longueur d'une chaîne de caractères comme suit :

```python
nom = 'Farhan'

print(len(nom))
```

La sortie de ce programme sera `6` puisque il y a six caractères dans la chaîne de caractères.

Python a une tonne de méthodes de chaîne de caractères, mais démontrer chacune d'entre elles n'est pas possible ici donc je vais démontrer certaines des plus courantes.

La première méthode est `capitalize()`. Cette méthode retourne une copie de la chaîne de caractères donnée avec son premier caractère en majuscule et le reste en minuscules.

```python
print('python est génial'.capitalize())
```

La sortie de ce code sera `Python est génial`. Si vous voulez convertir toute la phrase en majuscules, il y a la méthode `upper()` :

```python
print('python est génial'.upper())
```

La sortie de ce code sera `PYTHON EST GÉNIAL`. Vous pouvez faire l'inverse en utilisant la méthode `lower()` :

```python
print('PYTHON EST GÉNIAL'.lower())
```

La sortie de ce code sera `python est génial`. Il y a les méthodes `isupper()` et `islower()` pour vérifier si une chaîne de caractères est en majuscules ou en minuscules.

```python
print('PYTHON EST GÉNIAL'.islower())
print('PYTHON EST GÉNIAL'.isupper())
```

La sortie de ce code sera comme suit :

```shell
False
True
```

Si vous voulez remplacer toutes les occurrences d'une sous-chaîne dans une chaîne de caractères, vous pouvez le faire en utilisant la méthode `replace()` :

```python
print('python est génial'.replace('python', 'freeCodeCamp'))
```

Ce code remplacera toutes les occurrences de `python` par `freeCodeCamp` dans la chaîne de caractères donnée.

Enfin, il y a les méthodes `split()` et `join()`. La première divise une chaîne de caractères en une liste :

```python
print('python est génial'.split(' '))
```

La méthode prend un délimiteur pour diviser la chaîne de caractères. Ici, j'ai utilisé l'espace comme délimiteur. La sortie de ce code sera `['python', 'est', 'génial']`. C'est une liste. Nous n'avons pas encore couvert les listes mais nous le ferons bientôt. Pour l'instant, comprenez qu'elles sont comme des tableaux.

Vous pouvez produire une nouvelle chaîne de caractères en utilisant les éléments d'un itérable, c'est-à-dire une liste, en utilisant la méthode `join()` :

```python
print(' '.join(['python', 'est', 'génial']))
```

J'ai appelé la méthode `join()` sur un espace donc le résultat de ce code sera une chaîne de caractères jointe en utilisant des espaces entre eux comme suit :

```python
python est génial
```

Si vous voulez en apprendre plus sur toutes les méthodes de chaîne de caractères en Python, n'hésitez pas à consulter la [documentation officielle](https://docs.python.org/3/library/stdtypes.html#string-methods).

### Nombres en Python

Les nombres en Python peuvent être de types entier, à virgule flottante et complexe. Dans cet article, je ne discuterai que des opérations liées aux nombres réels – c'est-à-dire les entiers et les nombres à virgule flottante.

Vous pouvez effectuer des opérations d'addition, de soustraction, de multiplication et de division en utilisant des entiers et des nombres à virgule flottante comme dans n'importe quel autre langage de programmation :

```python
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
```

La sortie de cet extrait de code sera comme suit :

```shell
15
5
50
2.0
```

Une chose à garder à l'esprit est que même si vous effectuez une opération de division entre deux entiers, le résultat sera toujours un nombre à virgule flottante. Si vous voulez que le résultat soit un entier, vous pouvez le faire comme suit :

```python
a = 10
b = 5

print(a//b)
```

Cette fois, le résultat sera un entier. Soyez prudent, si il y a des nombres après la virgule, ils seront tronqués.

Si vous souhaitez en apprendre plus sur les types numériques en Python, n'hésitez pas à consulter la [documentation officielle](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

### Comment Gérer l'Entrée Utilisateur en Python

Pour prendre une entrée de l'utilisateur, il y a la fonction `input()`.

```python
nom = input('Quel est votre nom ? ')

print(f'Votre nom est {nom}')
```

La sortie de ce programme sera comme suit :

```shell
Quel est votre nom ? Farhan
Votre nom est Farhan
```

La fonction `input()` enregistre l'entrée de l'utilisateur comme une chaîne de caractères même si l'utilisateur entre un nombre. Donc si vous prenez un nombre comme entrée de l'utilisateur, assurez-vous de le convertir au type de données approprié.

### if-elif-else en Python

Comme tout autre langage de programmation, Python a les instructions habituelles `if-elif-else`.

```python
a = float(input('Premier : '))
b = float(input('Second : '))
op = input('Opération (sum/sub/mul/div) : ')

if op == 'sum':
    print(f'a + b = {a+b}')
elif op == 'sub':
    print(f'a - b = {a-b}')
elif op == 'mul':
    print(f'a * b = {a*b}')
elif op == 'div':
    print(f'a / b = {a/b}')
else:
    print('Opération Invalide !')

```

Ceci est un programme de calculatrice très simple. Selon l'opération que vous choisissez, la calculatrice effectuera l'une des opérations mentionnées.

En Python, les blocs de code tels que le bloc `if` ou le bloc `elif` ou le bloc `else` commencent par le mot-clé et un deux-points.

L'indentation est cruciale en Python et si vous indentiez le code dans un bloc de code de manière inappropriée, le code échouera à s'exécuter.

### match-case en Python

En Python, un `match-case` est équivalent à une instruction `switch-case` dans d'autres langages de programmation. Le programme de calculatrice mentionné précédemment peut être réécrit en utilisant `match-case` comme suit :

```python
a = float(input('Premier : '))
b = float(input('Second : '))
op = input('Opération (sum/sub/mul/div) : ')

match op:
    case 'sum':
        print(f'a + b = {a+b}')
    case 'sub':
        print(f'a - b = {a-b}')
    case 'mul':
        print(f'a * b = {a*b}')
    case 'div':
        print(f'a / b = {a/b}')
    case _:
        print('Opération Invalide !')

```

Encore une fois, selon la valeur de `op`, l'un des cas sera exécuté. Si l'entrée de l'utilisateur ne correspond à aucun des cas, alors l'action générique `_` aura lieu.

Gardez à l'esprit que `match-case` est disponible uniquement sur Python 3.10 et les versions ultérieures. Donc si vous utilisez une version plus ancienne, vous n'aurez peut-être pas cette instruction.

### Listes et Tuples en Python

Les listes en Python sont une séquence de valeurs. Vous pouvez modifier les listes à l'exécution. Vous pouvez créer une liste comme suit :

```python
voyelles = ['a', 'e', 'i', 'o', 'u']

print(voyelles)
```

La sortie de ce programme sera `['a', 'e', 'i', 'o', 'u']`. Comme les chaînes de caractères, chaque élément dans une liste Python a un index et ces index commencent à zéro.

```python
voyelles = ['a', 'e', 'i', 'o', 'u']

print(voyelles[0])
print(voyelles[1])
print(voyelles[2])
print(voyelles[3])
print(voyelles[4])
```

Comme les chaînes de caractères, vous pouvez effectuer un découpage sur les listes également et la syntaxe pour découper une liste est la même que pour une chaîne de caractères.

Les listes en Python ont un tas de méthodes utiles. Pour ajouter de nouveaux éléments à une liste, il y a les méthodes `append()`, `extend()`, et `insert()`.

La méthode `append()` ajoute un nouvel élément à la liste et la méthode `extend()` ajoute plusieurs éléments :

```python
voyelles = ['a', 'e']

voyelles.append('i')
voyelles.extend(['o', 'u'])

print(voyelles)
```

La méthode `insert()`, en revanche, insère un élément à un index donné dans la liste :

```python
voyelles = ['a', 'i', 'o', 'u']

voyelles.insert(1, 'e')

print(voyelles)
```

La méthode `pop()` retire le dernier élément de la liste :

```python
voyelles = ['a', 'e', 'i', 'o', 'u']

élément_retiré = voyelles.pop()

print(élément_retiré)
print(voyelles)
```

La sortie de cet extrait de code sera :

```shell
u
['a', 'e', 'i', 'o']
```

La méthode `remove()` peut retirer un élément donné de la liste :

```python
voyelles = ['a', 'e', 'i', 'o', 'u']

voyelles.remove('e')

print(voyelles)
```

Cela supprimera le `e` de la liste des voyelles.

Enfin, il y a la méthode `clear()` qui retire tous les éléments de la liste.

Il y a aussi la méthode `sort()` :

```python
voyelles = ['u', 'e', 'a', 'o', 'i']

voyelles.sort()

print(voyelles)
```

La méthode `sort()` trie la liste par ordre croissant. Cette méthode trie la liste en place. Cela signifie qu'elle ne retourne pas une nouvelle liste, et trie plutôt la liste originale.

Si vous voulez inverser la liste à la place, il y a la méthode `reverse()` :

```python
voyelles = ['u', 'e', 'a', 'o', 'i']

voyelles.reverse()

print(voyelles)
```

C'est aussi une méthode en place comme sort. C'est juste l'inverse (sans jeu de mots) de la méthode sort. Vous pouvez en apprendre plus sur les listes à partir de la [documentation officielle](https://docs.python.org/3/tutorial/datastructures.html).

Il y a aussi un type de séquence immutable appelé tuple en Python. Les tuples sont assez similaires aux listes mais vous ne pouvez pas modifier un tuple.

```python
voyelles = ('a', 'e', 'i', 'o', 'u')

print(voyelles)
```

La sortie de ce code sera `('a', 'e', 'i', 'o', 'u')`. Il n'y a pas beaucoup de méthodes pour les tuples. Si vous voulez en apprendre plus sur les tuples, consultez la [documentation officielle](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences).

### Boucles en Python

Vous pouvez utiliser des boucles en Python pour itérer sur un type de séquence comme une liste.

```python
voyelles = ['a', 'e', 'i', 'o', 'u']

for lettre in voyelles:
    print(lettre.upper())
```

Il y a aussi la boucle `while` mais puisque la boucle `for` est celle que vous utiliserez principalement, je ne passerai pas de temps à expliquer les boucles `while`.

### Dictionnaires en Python

Supposons que je vous ai donné la ligne "the quick brown fox jumped over the lazy dog" et que je vous demande de compter le nombre d'occurrences pour chaque lettre. Vous pouvez faire cela facilement en utilisant une table de hachage.

Une table de hachage est une collection de paires clé-valeur.

```
{
    clé_1: valeur_1,
    clé_2: valeur_2,
    clé_3: valeur_3,
    clé_4: valeur_4,
    clé_5: valeur_5,
}
```

Pour effectuer la tâche que je vous ai donnée précédemment, vous pouvez écrire le code suivant :

```python
phrase = 'the quick brown fox jumped over the lazy dog'

enregistrement = {}

for lettre in phrase:
    if lettre in enregistrement:
        enregistrement[lettre] += 1
    else:
        enregistrement[lettre] = 1

print(enregistrement)
```

La sortie de ce code sera comme suit :

```shell
{'t': 2, 'h': 2, 'e': 4, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 'd': 2, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'g': 1}
```

Ceci est un dictionnaire. Chaque lettre est une clé et leur nombre d'occurrences est la valeur. Dans l'extrait de code, vous déclarez un dictionnaire à la deuxième ligne. [Estefania Cassingena Navone](https://www.freecodecamp.org/news/author/estefaniacn/) a écrit un article intitulé [Python Dictionaries 101: A Detailed Visual Introduction](https://www.freecodecamp.org/news/python-dictionaries-detailed-visual-introduction/) que vous pouvez consulter pour en apprendre plus sur les dictionnaires.

### Fonctions en Python

Le dernier concept que je vais discuter est les fonctions. Les fonctions en programmation sont des morceaux de code qui effectuent une certaine tâche.

En Python, vous pouvez déclarer une fonction en utilisant le mot-clé `def` suivi de la signature de la fonction :

```python
def somme(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

a = float(input('Premier : '))
b = float(input('Second : '))
op = input('Opération (sum/sub/mul/div) : ')

if op == 'sum':
    print(f'a + b = {somme(a, b)}')
elif op == 'sub':
    print(f'a - b = {soustraction(a, b)}')
elif op == 'mul':
    print(f'a * b = {multiplication(a, b)}')
elif op == 'div':
    print(f'a / b = {division(a, b)}')
else:
    print('Opération Invalide !')

```

C'est le même programme de calculatrice que précédemment, mais maintenant les opérations sont écrites dans des fonctions séparées.

Pour en apprendre plus sur les fonctions, vous pouvez lire cet article : [Functions in Python – Explained with Code Examples](https://www.freecodecamp.org/news/functions-in-python-a-beginners-guide/) par [Bala Priya C](https://www.freecodecamp.org/news/author/bala-priya/).

Il y a beaucoup d'autres concepts que vous devez apprendre si vous voulez devenir un excellent programmeur Python. C'est ce dont traite la section suivante.

## Ressources d'Apprentissage Python Supplémentaires

Maintenant que vous avez une compréhension de base du langage de programmation Python, je vais vous suggérer quelques ressources d'apprentissage de haute qualité pour continuer votre parcours d'apprentissage.

### Apprendre Python en 4 Heures

%[https://youtu.be/rfscVS0vtbw]

La première ressource de la liste est une vidéo sur la chaîne YouTube freeCodeCamp créée par Girrafe Academy.

L'instructeur a créé plusieurs cours sur la chaîne et est connu pour faire des vidéos concises.

La vidéo couvre la plupart des concepts importants de Python en 4 heures. L'instructeur réalise également des projets simples en cours de route.

### Python pour Tout le Monde

%[https://youtu.be/8DvywoWv6fI]

Un autre cours Python convivial pour les débutants sur la chaîne YouTube freeCodeCamp est Python pour Tout le Monde. Ce qui rend ce cours spécial est qu'il ne s'adresse pas seulement aux débutants en Python mais aussi aux personnes qui essaient de commencer avec la programmation en général.

Le cours dure un peu plus de 13 heures et est enseigné par Charles R. Severance alias Dr. Chuck. Il a écrit certains des cours les plus incroyables sur Internet.

Si vous êtes assez patient pour suivre un cours de 13 heures, Python pour Tout le Monde est l'un des meilleurs cours Python en ligne.

### 12 Projets Python pour Débutants

%[https://youtu.be/8ext9G7xspg]

Si vous préférez une approche basée sur des projets, alors ce cours de 3 heures par Kylie Ying est fortement recommandé.

Kylie est un membre de l'équipe freeCodeCamp et sait ce qu'elle fait. Dans ce cours, vous apprendrez à faire 12 projets Python conviviaux pour débutants avec des niveaux de complexité croissants.

### Apprendre Python en Construisant 5 Jeux

%[https://youtu.be/XGf2GcyHPhc]

Si vous êtes passionné par les jeux et que vous voulez apprendre Python en construisant des jeux classiques, alors ce cours devrait vous convenir.

L'instructeur de ce cours est Christian Thompson, un programmeur Python expérimenté. Si vous êtes familier avec un autre langage de programmation ou si vous apprenez bien en vous lançant dans des projets, plongez-vous dedans.

### Python Intermédiaire

%[https://youtu.be/HGOBQPFzWKo]

Si vous avez terminé votre premier cours Python et que vous avez appris tous les concepts fondamentaux et que vous cherchez maintenant la prochaine étape logique, alors ne cherchez pas plus loin.

Patrick Loeber a produit ce cours de 6 heures sur Python intermédiaire où vous apprendrez un bon nombre de concepts généralement non trouvés dans les cours Python pour débutants.

### Programmation Orientée Objet avec Python

%[https://youtu.be/Ej_02ICOIgs]

Si vous avez du mal à comprendre la programmation orientée objet en général, ce cours vous enseignera la programmation orientée objet avec Python en 2 heures.

Le cours inclut des tonnes d'exemples de code et couvre tous les concepts importants concernant la programmation orientée objet avec Python. Je suggérerais ce cours juste après avoir terminé votre cours de base.

### Python pour la Science des Données

%[https://youtu.be/LHBE6Q9XlzI]

Ceci est un cours un peu spécialisé. Si vous pensez vous lancer dans la science des données et que vous voulez apprendre tout ce qui est nécessaire en Python pour la science des données, alors ce cours vous aidera grandement.

Ne pensez pas que ce cours est rapide. En un peu plus de 12 heures, ce cours vous enseignera les concepts de programmation Python et une série d'outils essentiels pour la science des données en détail.

### Structures de Données et Algorithmes en Python

%[https://youtu.be/pkYVOmU3MgA]

Avoir une compréhension des structures de données et des algorithmes est essentiel pour devenir un développeur logiciel efficace.

Dans ce cours de 12,5 heures de Jovian, vous apprendrez les structures de données et les algorithmes importants avec des exemples de code en détail. Peu importe ce que vous prévoyez de faire avec Python ensuite, je recommande vivement ce cours.

## Conclusion

Je voudrais vous remercier du fond du cœur pour le temps que vous avez passé à lire cet article.

Bien que j'aie listé autant de bonnes ressources que possible, la [chaîne YouTube freeCodeCamp](https://www.youtube.com/c/Freecodecamp/search?query=python) est remplie d'excellentes ressources d'apprentissage Python.

J'ai aussi un blog personnel où j'écris sur des sujets technologiques aléatoires, donc si vous êtes intéressé par quelque chose comme ça, consultez [https://farhan.dev](https://farhan.dev). Si vous avez des questions ou êtes confus à propos de quelque chose – ou si vous voulez simplement entrer en contact – je suis disponible sur [Twitter](https://twitter.com/frhnhsin) et [LinkedIn](https://www.linkedin.com/in/farhanhasin/).