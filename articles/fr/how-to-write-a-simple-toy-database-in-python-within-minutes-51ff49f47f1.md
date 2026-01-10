---
title: Comment écrire une base de données jouet simple en Python en quelques minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T23:33:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yp-GUhlz1nZTRbkW-ye2HA.jpeg
tags:
- name: database
  slug: database
- name: json
  slug: json
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment écrire une base de données jouet simple en Python en quelques minutes
seo_desc: 'By Palash Bauri

  MySQL, PostgreSQL, Oracle, Redis, and many more, you just name it — databases are
  a really important piece of technology in the progress of human civilization. Today
  we can see how valuable data are, and so keeping them safe and stabl...'
---

Par Palash Bauri

MySQL, PostgreSQL, Oracle, Redis, et bien d'autres, vous n'avez qu'à les nommer — les bases de données sont un élément vraiment important de la technologie dans le progrès de la civilisation humaine. Aujourd'hui, nous pouvons voir à quel point les **données** sont précieuses, et c'est là que la base de données entre en jeu pour les garder en sécurité et stables !

Nous pouvons donc voir à quel point les bases de données sont importantes. Depuis un certain temps, je pensais créer ma propre base de données jouet juste pour comprendre, jouer et expérimenter avec. Comme l'a dit [**Richard Feynman**](https://en.wikipedia.org/wiki/Richard_Feynman) :

> **_Ce que je ne peux pas créer, je ne comprends pas._**

Alors, sans plus attendre, passons à la partie amusante : le codage.

### Commençons à coder...

Pour cette base de données jouet, nous utiliserons **Python** (mon préféré ❤️). J'ai nommé cette base de données **FooBarDB** (je n'ai pas trouvé d'autre nom ?), mais vous pouvez l'appeler comme vous voulez !

Alors, commençons par importer quelques bibliothèques Python nécessaires qui sont déjà disponibles dans la bibliothèque standard de Python :

```python
import json
import os
```

Oui, nous avons seulement besoin de ces deux bibliothèques ! Nous avons besoin de `json` car notre base de données sera basée sur JSON, et `os` pour certaines opérations liées aux chemins.

Maintenant, définissons la classe principale `FoobarDB` avec quelques fonctions assez basiques, que je vais expliquer ci-dessous.

```python
class FoobarDB(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dumpdb(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False
```

Ici, nous avons défini notre classe principale avec une fonction `__init__`. Lorsque nous créons une base de données Foobar, nous devons simplement passer l'emplacement de la base de données. Dans la première fonction `__init__`, nous prenons le paramètre location et remplaçons `~` ou `~user` par le répertoire personnel de l'utilisateur pour qu'il fonctionne comme prévu. Enfin, nous le plaçons dans la variable `self.location` pour y accéder plus tard dans les fonctions de la même classe. À la fin, nous appelons la fonction `load` en passant `self.location` comme argument.

```python
. . . .
    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True
. . . .
```

Dans la fonction `load` suivante, nous prenons l'emplacement de la base de données comme paramètre. Ensuite, nous vérifions si la base de données existe ou non. Si elle existe, nous la chargeons avec la fonction `_load()` (expliquée ci-dessous). Sinon, nous créons un objet JSON vide en mémoire. Enfin, nous retournons vrai en cas de succès.

```python
. . . . 

    def _load(self):
        self.db = json.load(open(self.location, "r"))
. . . .
```

Dans la fonction `_load`, nous ouvrons simplement le fichier de la base de données à partir de l'emplacement stocké dans `self.location`. Ensuite, nous le transformons en un objet JSON et le chargeons dans la variable `self.db`.

```py
. . . .
    def dumpdb(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False

. . . .
```

Et enfin, la fonction `dumpdb` : son nom indique ce qu'elle fait. Elle prend la base de données en mémoire (en fait un objet JSON) à partir de la variable `self.db` et l'enregistre dans le fichier de la base de données ! Elle retourne **True** si l'enregistrement est réussi, sinon elle retourne **False.**

### Rendre cela un peu plus utilisable... ?

Attendez une minute ! ? Une base de données est inutile si elle ne peut pas stocker et récupérer des données, n'est-ce pas ? Allons-y et ajoutons-les aussi...

```py
. . . .
    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Erreur lors de l'enregistrement des valeurs dans la base de données : " + str(e))
            return False

    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            print("Aucune valeur trouvée pour " + str(key))  
            return False

    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True
. . . .
```

La fonction `set` est utilisée pour ajouter des données à la base de données. Comme notre base de données est une base de données simple basée sur des paires clé-valeur, nous prendrons uniquement une `clé` et une `valeur` comme arguments.

Tout d'abord, nous essaierons d'ajouter la clé et la valeur à la base de données, puis nous enregistrerons la base de données. Si tout se passe bien, elle retournera True. Sinon, elle affichera un message d'erreur et retournera False. (Nous ne voulons pas qu'elle plante et efface nos données à chaque fois qu'une erreur se produit ?).

```py
. . . .
    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            return False
. . . .
```

`get` est une fonction simple, nous prenons `key` comme argument et essayons de retourner la valeur liée à la clé à partir de la base de données. Sinon, False est retourné avec un message.

```py
. . . .
    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

. . . .
```

La fonction `delete` est utilisée pour supprimer une clé ainsi que sa valeur de la base de données. Tout d'abord, nous nous assurons que la clé est présente dans la base de données. Si ce n'est pas le cas, nous retournons False. Sinon, nous supprimons la clé avec le `del` intégré qui supprime automatiquement la valeur de la clé. Ensuite, nous enregistrons la base de données et elle retourne false.

Maintenant, vous pourriez penser, que faire si j'ai créé une grande base de données et que je veux la réinitialiser ? En théorie, nous pouvons utiliser `delete` — mais ce n'est pas pratique, et c'est aussi très chronophage ! ⏳ Alors nous pouvons créer une fonction pour effectuer cette tâche...

```py
. . . . 

    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True
. . . .
```

Voici la fonction pour réinitialiser la base de données, `resetdb` ! C'est si simple : d'abord, ce que nous faisons, c'est réassigner notre base de données en mémoire avec un objet JSON vide et nous l'enregistrons simplement ! Et c'est tout ! Notre base de données est maintenant à nouveau propre.

### Enfin... ?

C'est tout, les amis ! Nous avons créé notre propre **base de données jouet** ! ?? En fait, Fo**obarDB** est juste une simple démonstration d'une base de données. C'est comme un jouet DIY bon marché : vous pouvez l'améliorer de la manière que vous voulez. Vous pouvez également ajouter de nombreuses autres fonctions selon vos besoins.

Le code source complet est ici ? [bauripalash/foobardb](https://github.com/bauripalash/foobardb)

J'espère que vous avez apprécié ! Faites-moi part de vos suggestions, idées ou erreurs que j'ai commises dans les commentaires ci-dessous ! ?

Suivez/mentionnez-moi sur les réseaux sociaux ? F[acebook,](https://facebook.com/bauripalash) T[witter,](https://twitter.com/bauripalash) I[nstagram](https://instagram.com/bauripalash)

Merci ! À bientôt !

---
Si vous aimez mon travail (mes articles, histoires, logiciels, recherches et bien plus encore), envisagez de [m'offrir un café ☕](https://www.buymeacoffee.com/palash) ?