---
title: Comment trouver rapidement les problèmes de type dans votre code Python avec
  Pytype
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:50:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-quickly-find-type-issues-in-your-python-code-with-pytype-c022782f61c3
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/python-1.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment trouver rapidement les problèmes de type dans votre code Python
  avec Pytype
seo_desc: 'By Ehud Tamir

  TL;DR — If you’re working on a large Python project or just like to keep your code-base
  tidy and neat, Pytype is the tool for you.

  Python is a great programming language for prototyping and scripting. The concise
  syntax, flexible type s...'
---

Par Ehud Tamir

**TL;DR —** Si vous travaillez sur un grand projet Python ou si vous aimez simplement garder votre base de code propre et ordonnée, [Pytype](https://github.com/google/pytype) est l'outil qu'il vous faut.

Python est un excellent langage de programmation pour le prototypage et le scripting. La syntaxe concise, le système de types flexible et la nature interprétée nous permettent d'essayer rapidement une idée, de la modifier et de réessayer.

Lorsque les projets Python **grandissent**, la flexibilité qui était autrefois un atout pour la vitesse devient un fardeau pour la vitesse de développement. Alors que des développeurs supplémentaires rejoignent le projet et que plus de code est écrit, le manque d'informations de type rend le code plus difficile à lire et à comprendre. Sans un système de vérification de type, les erreurs sont faciles à commettre et difficiles à détecter.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/python.jpeg)
_CC BY 2.5, [https://commons.wikimedia.org/w/index.php?curid=648709](https://commons.wikimedia.org/w/index.php?curid=648709)_

[**Pytype**](https://github.com/google/pytype) à la rescousse ! Pytype est un outil open-source pour la vérification de type et l'inférence de type en Python. Et il fonctionne directement — il suffit de l'installer et de l'exécuter !

Pytype va...

1. Inférer statiquement les informations de type et vérifier votre code pour les erreurs de type.
2. Valider les annotations de type PEP 484 dans votre code pour la cohérence.
3. Réintégrer les informations de type inférées dans votre code, **si vous le souhaitez**.

Si vous êtes convaincu, allez-y et visitez [Pytype](https://github.com/google/pytype) pour les instructions d'installation et d'utilisation. Ci-dessous, je présente quelques exemples d'utilisation intéressants !

### Exemple #1 : Inférence et vérification de type

C'est le scénario le plus courant. Vous avez écrit du code et vous voulez vérifier que vous n'avez pas fait d'erreurs. Considérez cette fonction :

```py
import re

def GetUsername(email_address):
  match = re.match(r'([^@]+)@example\.com', email_address)
  return match.group(1)
```

Assez simple. Elle extrait la partie d'une adresse e-mail avant le @ en utilisant une expression régulière, et la retourne. Avez-vous remarqué le bug ?

Voyons ce qui se passe lorsque nous utilisons `pytype` pour le vérifier :

```py
% pytype get_username.py
Analyzing 1 sources with 0 dependencies
File "/.../get_username.py", 
line 5, in GetUsername: No attribute 'group' on None [attribute-error]
  In Optional[Match[str]]
```

Pytype nous dit que `group` n'est pas un appel de fonction valide sur `match`. Oh ! `re.match()` retourne `None` lorsqu'aucun match n'est trouvé. En effet, dans ces cas, `match.group(1)` va lever une exception.

Corrigeons le bug, en faisant en sorte que la fonction retourne None pour une adresse e-mail invalide :

```py
import re
def GetUsername(email_address):
  match = re.match(r'([^@]+)@example\.com', email_address)
  
if match is None:
    return None
  return match.group(1)  # <-- Ici, match ne peut pas être None
```

Maintenant, lorsque nous relançons `pytype`, l'erreur a disparu. Pytype infère que si le code après le **if** est exécuté, match est garanti de ne pas être `None`.

### Exemple #2 : Validation des annotations de type

En Python 3, vous pouvez annoter les types ([PEP 484](https://www.python.org/dev/peps/pep-0484)) de votre code pour aider les outils de vérification de type **et les autres développeurs** à comprendre votre intention. Pytype est capable d'alerter lorsque vos annotations de type contiennent des erreurs :

```py
import re
from typing import Match

def GetEmailMatch(email) -> Match:
  return re.match(r'([^@]+)@example\.com', email)
```

Utilisons `pytype` pour vérifier cet extrait de code :

```py
% pytype example.py
Analyzing 1 sources with 0 dependencies
File "/.../example.py", line 5, in GetEmailMatch: 
bad option in return type [bad-return-type]
  Expected: Match
  Actually returned: None
```

Pytype nous dit que `GetEmailMatch` peut retourner `None`, mais nous avons annoté son type de retour comme `Match`. Pour corriger cela, nous pouvons utiliser l'annotation de type `Optional` du module typing :

```py
import re
from typing import Match, Optional

def GetEmailMatch(email) -> Optional[Match]:
  return re.match(r'([^@]+)@example\.com', email)
```

`Optional` signifie que la valeur de retour peut être un objet `Match` ou `None`.

### Exemple #3 : Réintégration des informations de type inférées

Pour vous aider à adopter les annotations de type, Pytype peut les ajouter dans le code pour vous. Regardons cet extrait de code :

```py
import re
  
def GetEmailMatch(email):
  return re.match(r'([^@]+)@example\.com', email)

def GetUsername(email_address):
  match = GetEmailMatch(email_address)
  if match is None:
    return None
  return match.group(1)
```

Pour ajouter des annotations de type à ce code, nous exécutons d'abord `pytype` sur le fichier. `pytype` sauvegarde les informations de type inférées dans un fichier `.pyi`. Ensuite, nous pouvons exécuter `merge-pyi` pour réintégrer les annotations de type dans le code :

```
% pytype email.py
% merge-pyi -i email.py pytype_output/email.pyi
```

Et voilà !

```py
import re
from typing import Match
from typing import Optional

def GetEmailMatch(email) -> Optional[Match[str]]:
  return re.match(r'([^@]+)@example\.com', email)

def GetUsername(email_address) -> Optional[str]:
  match = GetEmailMatch(email_address)
  if match is None:
    return None
  return match.group(1)
```

Les annotations de type, y compris les instructions `import`, sont maintenant dans le fichier source.

Pour plus d'exemples d'utilisation et d'instructions d'installation, veuillez visiter [Pytype sur GitHub](https://github.com/google/pytype).

Merci d'avoir lu !