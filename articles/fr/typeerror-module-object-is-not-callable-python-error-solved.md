---
title: 'TypeError: module object is not callable [Erreur Python Résolue]'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-04T22:17:35.000Z'
originalURL: https://freecodecamp.org/news/typeerror-module-object-is-not-callable-python-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/brett-jordan-XWar9MbNGUY-unsplash--1-.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'TypeError: module object is not callable [Erreur Python Résolue]'
seo_desc: "In this article, we'll talk about the \"TypeError: 'module' object is not\
  \ callable\" error in Python. \nWe'll start by defining some of the keywords found\
  \ in the error message — module and callable. \nYou'll then see some examples that\
  \ raise the error, a..."
---

Dans cet article, nous allons parler de l'erreur "TypeError: 'module' object is not callable" en Python. 

Nous commencerons par définir certains des mots-clés trouvés dans le message d'erreur — `module` et `callable`. 

Vous verrez ensuite quelques exemples qui déclenchent l'erreur, et comment la corriger.

N'hésitez pas à sauter les deux prochaines sections si vous savez déjà ce que sont les modules et ce que signifie appeler une fonction ou une méthode. 

## Qu'est-ce qu'un Module en Programmation?

En programmation modulaire, les modules sont simplement des fichiers qui contiennent des fonctionnalités similaires nécessaires pour effectuer une certaine tâche. 

Les modules nous aident à séparer et à regrouper le code en fonction de la fonctionnalité. Par exemple, vous pourriez avoir un module appelé `math-ops.py` qui ne contiendra que du code lié aux opérations mathématiques. 

Cela rend le code plus facile à lire, à réutiliser et à comprendre. Pour utiliser un module dans une autre partie de votre base de code, vous devez l'importer pour accéder à toutes les fonctionnalités définies dans le module.

En Python, il existe de nombreux modules intégrés comme `os`, `math`, `time`, et ainsi de suite.

Voici un exemple qui montre comment utiliser le module `math` : 

```python
import math

print(math.sqrt(25))
//5.0
```

Comme vous pouvez le voir ci-dessus, la première chose que nous avons faite avant d'utiliser le module `math` a été de l'importer : `import math`.

Nous avons ensuite utilisé la méthode `sqrt` du module qui retourne la racine carrée d'un nombre : `math.sqrt(25)`.

Il nous a suffi de deux lignes de code pour obtenir la racine carrée de 25. En réalité, [le module `math` seul contient plus de 3500 lignes de code](https://github.com/python/cpython/blob/main/Modules/mathmodule.c). 

Cela devrait vous aider à comprendre ce qu'est un module et comment il fonctionne. Vous pouvez également créer vos propres modules (nous le ferons plus tard dans cet article).

## Que Signifie `callable` dans l'Erreur "TypeError: module object is not callable" ?

En Python et dans la plupart des langages de programmation, le verbe "call" est associé à l'exécution du code écrit dans une fonction ou une méthode. 

D'autres termes similaires souvent utilisés pour la même action sont "invoke" et "fire". 

Voici une fonction Python qui imprime "Smile!" sur la console :

```python
def smile():
    print("Smile!")
```

Si vous exécutez le code ci-dessus, rien ne sera imprimé sur la console car la fonction `smile` n'a pas encore été appelée, invoquée ou déclenchée. 

Pour exécuter la fonction, nous devons écrire le nom de la fonction suivi de parenthèses. C'est-à-dire :

```python
def smile():
    print("Smile!")
    
smile()
# Smile!
```

Sans les parenthèses, la fonction ne sera pas exécutée.

Maintenant, vous devriez comprendre ce que signifie le terme `callable` dans le message d'erreur : "TypeError: 'module' object is not callable". 

## Que Signifie l'Erreur "TypeError: module object is not callable" en Python ?

Les deux dernières sections nous ont aidés à comprendre certains des mots-clés trouvés dans le message d'erreur "TypeError: 'module' object is not callable". 

Pour faire simple, l'erreur "TypeError: 'module' object is not callable" signifie que les modules ne peuvent pas être appelés comme des fonctions ou des méthodes. 

## Comment Corriger l'Erreur "TypeError: module object is not callable" en Python

Il existe généralement deux façons de déclencher l'erreur "TypeError: 'module' object is not callable" : appeler un module intégré ou tiers, et appeler un module à la place d'une fonction. 

#### Exemple d'Erreur #1

```python
import math

print(math(25))
# TypeError: 'module' object is not callable

```

Dans l'exemple ci-dessus, nous avons appelé le module `math` (en utilisant des parenthèses `()`) et avons passé 25 comme paramètre en espérant effectuer une opération mathématique particulière : `math(25)`. Mais nous avons obtenu l'erreur.

Pour corriger cela, nous pouvons utiliser n'importe quelle méthode mathématique fournie par le module `math`. Nous utiliserons la méthode `sqrt` :

```python
import math

print(math.sqrt(25))
# 5.0
```

#### Exemple d'Erreur #2

Pour cet exemple, je vais créer un module pour calculer deux nombres :

```python
# add.py

def add(a,b):
    print(a+b)
    
```

Le nom du module ci-dessus est `add` qui peut être dérivé du nom de fichier **add.py**.

Importons la fonction `add()` du module `add` dans un autre fichier :

```python
# main.py
import add

add(2,3)
# TypeError: 'module' object is not callable
```

Vous devez vous demander pourquoi nous obtenons l'erreur alors que nous avons importé le module.

Eh bien, nous avons importé le module, pas la fonction. C'est pourquoi. 

Pour corriger cela, vous devez spécifier le nom de la fonction lors de l'importation du module :

```python
from add import add

add(2,3)
# 5
```

Nous sommes spécifiques : `from add import add`. Cela revient à dire : "du module add.py, importer la fonction `add`".

Vous pouvez maintenant utiliser la fonction `add()` dans le fichier **main.py**.

## Résumé

Dans cet article, nous avons parlé de l'erreur "TypeError: 'module' object is not callable" en Python. 

Cette erreur se produit principalement lorsque nous appelons ou invoquons un module comme s'il s'agissait d'une fonction ou d'une méthode. 

Nous avons commencé par discuter de ce qu'est un module en programmation, et de ce que signifie appeler une fonction — cela nous a aidés à comprendre ce qui cause l'erreur. 

Nous avons ensuite donné quelques exemples montrant l'erreur et comment la corriger. 

Bon codage !