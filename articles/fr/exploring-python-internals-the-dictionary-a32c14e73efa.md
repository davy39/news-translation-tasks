---
title: 'Améliorez vos compétences Python : Examen du Dictionnaire'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T16:44:08.000Z'
originalURL: https://freecodecamp.org/news/exploring-python-internals-the-dictionary-a32c14e73efa
coverImage: https://cdn-media-1.freecodecamp.org/images/0*f5Lr7gbwGVVbvsCN
tags:
- name: coding
  slug: coding
- name: data structures
  slug: data-structures
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'Améliorez vos compétences Python : Examen du Dictionnaire'
seo_desc: 'By Adam Goldschmidt


  a hash table (hash map) is a data structure that implements an associative array
  abstract data type, a structure that can map keys to values.


  If it smells like a Python dict, feels like a dict, and looks like one… well, it
  must ...'
---

Par Adam Goldschmidt

> _une table de hachage (hash map) est une structure de données qui implémente un type de données abstrait de tableau associatif, une structure qui peut mapper des clés à des valeurs._

Si cela ressemble à un `dict` Python, se comporte comme un `dict` et a l'air d'un `dict`... eh bien, cela doit être un `dict`. Absolument ! Oh, et un `set` aussi...

#### Huh?

Les dictionnaires et les ensembles en Python sont implémentés en utilisant une table de hachage. Cela peut sembler intimidant au premier abord, mais en approfondissant, tout devrait devenir clair.

![Image](https://cdn-media-1.freecodecamp.org/images/0*yHSWDgnvYXPmAA0Z)

### Objectif

Tout au long de cet article, nous allons découvrir comment un `dict` est implémenté en Python, et nous allons construire notre propre implémentation (simplifiée). L'article est divisé en trois parties, et la construction de notre dictionnaire personnalisé a lieu dans les deux premières :

1. Comprendre ce que sont les tables de hachage et comment les utiliser
2. Plonger dans le code source de Python pour mieux comprendre comment les dictionnaires sont implémentés
3. Explorer les différences entre le dictionnaire et d'autres structures de données telles que les listes et les ensembles

### Qu'est-ce qu'une table de hachage ?

Une table de hachage est une structure conçue pour stocker une liste de paires clé-valeur, sans compromettre la vitesse et l'efficacité de la manipulation et de la recherche dans la structure.

L'efficacité de la table de hachage provient de la **fonction de hachage** — une fonction qui calcule l'index de la paire clé-valeur — Ce qui signifie que nous pouvons rapidement insérer, rechercher et supprimer des éléments puisque nous connaissons leur index dans le tableau mémoire.

La complexité commence lorsque deux de nos clés ont le même hachage. Ce scénario est appelé une _collision de hachage_. Il existe de nombreuses façons de gérer une collision, mais nous ne couvrirons que la méthode de Python. Nous n'irons pas trop loin dans notre explication des tables de hachage pour garder cet article accessible aux débutants et centré sur Python.

Assurons-nous d'avoir bien compris le concept des tables de hachage avant de continuer. Nous allons commencer par créer les squelettes de notre `dict` personnalisé très (très) simple, composé uniquement de méthodes d'insertion et de recherche, en utilisant certaines des [méthodes dunder](https://docs.python.org/3.6/reference/datamodel.html#object.__getitem__) de Python. Nous devrons initialiser la table de hachage avec une liste de taille spécifique, et activer la notation par crochets ([]) pour celle-ci :

Maintenant, notre liste de table de hachage doit contenir des structures spécifiques, chacune contenant une clé, une valeur et un hachage :

#### Exemple de base

Une petite entreprise avec 10 employés souhaite conserver des enregistrements contenant les jours de maladie restants de leurs employés. Nous pouvons utiliser la fonction de hachage suivante, afin que tout puisse tenir dans le tableau mémoire :

`longueur du nom de l'employé % TABLE_SIZE`

Définissons notre fonction de hachage dans la classe Entry :

Maintenant, nous pouvons initialiser un tableau de 10 éléments dans notre table :

Attendez ! Réfléchissons-y. Nous allons probablement rencontrer des collisions de hachage. Si nous n'avons que 10 éléments, il sera beaucoup plus difficile pour nous de trouver un espace libre après une collision. Décidons que notre table aura le double de la taille — 20 éléments ! Cela sera utile à l'avenir, je vous le promets.

Pour insérer rapidement chaque employé, nous allons suivre la logique :

```
array[longueur du nom de l'employé % 20] = employee_remaining_sick_days
```

Ainsi, notre méthode d'insertion ressemblera à ce qui suit (sans gestion des collisions de hachage pour l'instant) :

Pour la recherche, nous faisons essentiellement la même chose :

```
array[longueur du prénom de l'employé % 20] 
```

Nous n'avons pas encore terminé !

### Gestion des collisions par Python

Python utilise une méthode appelée Adressage Ouvert pour gérer les collisions. Il redimensionne également les tables de hachage lorsqu'elles atteignent une certaine taille, mais nous n'aborderons pas cet aspect. Définition de l'Adressage Ouvert de [Wikipedia](https://en.wikipedia.org/wiki/Hash_table#Open_addressing) :

> _Dans une autre stratégie, appelée adressage ouvert, tous les enregistrements d'entrée sont stockés dans le tableau de compartiments lui-même. Lorsqu'une nouvelle entrée doit être insérée, les compartiments sont examinés, en commençant par l'emplacement haché et en procédant dans une séquence de sondage, jusqu'à ce qu'un emplacement inoccupé soit trouvé. Lors de la recherche d'une entrée, les compartiments sont scannés dans la même séquence, jusqu'à ce que soit l'enregistrement cible soit trouvé, soit un emplacement de tableau inutilisé soit trouvé, ce qui indique qu'il n'y a pas une telle clé dans la table._

Examinons le processus de récupération d'une valeur par `key`, en regardant le [code source](https://github.com/python/cpython/blob/master/Objects/dictobject.c#L745) de Python (écrit en C) :

1. Calculer le hachage de `key`
2. Calculer l'`index` de l'élément par `hash & mask` où `mask = HASH_TABLE_SIZE-1` (en termes simples - prendre les N derniers bits des bits de hachage) :

```
i = (size_t)hash & mask;
```

3. Si vide, retourner `DKIX_EMPTY` qui se traduit éventuellement par une `KeyError` :

```
if (ix == DKIX_EMPTY) {   *value_addr = NULL;   return ix;}
```

4. Si non vide, comparer les clés & hachages et définir l'adresse `value_addr` à l'adresse de la valeur réelle si égale :

```
if (ep->me_key == key) {    *value_addr = ep->me_value;    return ix;}
```

et :

```
if (dk == mp->ma_keys && ep->me_key == startkey) {    if (cmp > 0) {        *value_addr = ep->me_value;        return ix;    }}
```

5. Si non égal, utiliser différents bits du hachage (algorithme expliqué [ici](https://github.com/python/cpython/blob/master/Objects/dictobject.c#L135)) et revenir à l'étape 3 :

```
perturb >>= PERTURB_SHIFT;i = (i*5 + perturb + 1) & mask;
```

Voici un diagramme pour illustrer le processus entier :

![Image](https://cdn-media-1.freecodecamp.org/images/0*T4NeGGFsTXLjqdfh.jpg)

Le processus d'insertion est assez similaire — si l'emplacement trouvé est vide, l'entrée est insérée, s'il n'est pas vide, nous comparons la clé et le hachage — si égal, nous remplaçons la valeur, et si non, nous continuons notre quête de trouver un nouvel emplacement avec l'algorithme `perturb`.

#### Emprunter des idées à Python

Nous pouvons emprunter l'idée de Python de comparer à la fois les clés et les hachages de chaque entrée à notre objet d'entrée (en remplaçant la méthode précédente) :

Notre table de hachage n'a toujours aucune gestion des collisions — implémentons-en une ! Comme nous l'avons vu précédemment, Python le fait en comparant les entrées puis en changeant le masque des bits, mais nous allons le faire en utilisant une méthode appelée sondage linéaire (qui est une forme d'adressage ouvert, expliqué ci-dessus) :

> Lorsque la [fonction de hachage](https://en.wikipedia.org/wiki/Hash_function) provoque une collision en mappant une nouvelle clé à une cellule de la table de hachage qui est déjà occupée par une autre clé, le sondage linéaire recherche dans la table l'emplacement libre suivant le plus proche et insère la nouvelle clé là.

Donc, ce que nous allons faire, c'est avancer jusqu'à ce que nous trouvions un espace libre. Si vous vous souvenez, nous avons implémenté notre table avec le double de la taille (20 éléments et non 10) — **C'est là que cela devient utile**. Lorsque nous avançons, notre recherche d'un espace libre sera beaucoup plus rapide car il y a plus de place !

Mais nous avons un problème. Que se passe-t-il si quelqu'un d'astucieux essaie d'insérer le 11ème élément ? Nous devons lever une erreur (nous ne traiterons pas du redimensionnement de la table dans cet article). Nous pouvons garder un compteur des entrées remplies dans notre table :

Maintenant, implémentons la même chose dans notre méthode de recherche :

**Le code complet peut être trouvé [ici](https://gist.github.com/AdamGold/f2107afeec2a4788fb6e79a3ceeae32d).**

Maintenant, l'entreprise peut stocker en toute sécurité les jours de maladie pour chaque employé :

### Ensemble Python

En revenant au début de l'article, `set` et `dict` en Python sont implémentés de manière très similaire, avec `set` utilisant uniquement `key` et `hash` à l'intérieur de chaque enregistrement, comme on peut le voir dans [le code source](https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Include/setobject.h#L26) :

```
typedef struct {    PyObject *key;    Py_hash_t hash; /* Cached hash code of the key */} setentry;
```

Contrairement à `[dict](https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Objects/dict-common.h#L4)`, qui contient une valeur :

```
typedef struct {    /* Cached hash code of me_key. */    Py_hash_t me_hash;    PyObject *me_key;    PyObject *me_value; /* This field is only meaningful for combined tables */} PyDictKeyEntry;
```

### Performance et Ordre

#### Comparaison de temps

Je pense qu'il est maintenant clair qu'un `dict` est beaucoup plus rapide qu'une `list` (et prend beaucoup plus d'espace mémoire), en termes de recherche, d'insertion (à un endroit spécifique) et de suppression. Validons cette hypothèse avec un peu de code (j'exécute le code sur un MacBook Pro 2017) :

Et voici le code de test (une fois pour le `dict` et une fois pour la `list`, en remplaçant `d`) :

Les résultats sont, eh bien, assez ce à quoi nous nous attendions...

`dict` : `0.015382766723632812` secondes

`list` : `55.5544171333313` secondes

![Image](https://cdn-media-1.freecodecamp.org/images/0*smRKnPDQhelVdzwY.gif)

#### L'ordre dépend de l'ordre d'insertion

L'ordre du dictionnaire dépend de l'historique des insertions. Si nous insérons une entrée avec un hachage spécifique, et ensuite une entrée avec le même hachage, la deuxième entrée va se retrouver à un endroit différent de celui où elle serait si nous l'avions insérée en premier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*yWESkOAPo0LVNxto.png)

### Avant de partir...

Merci d'avoir lu ! Vous pouvez me suivre sur [Medium](https://medium.com/@adamgoldschmidt) pour plus d'articles comme celui-ci, ou sur [GitHub](https://github.com/AdamGold) pour découvrir des repos intéressants :)

Si vous avez aimé cet article, n'hésitez pas à appuyer longuement sur le bouton d'applaudissements ? pour aider les autres à le trouver. Plus vous appuyez longtemps, plus vous donnez d'applaudissements !

Et n'hésitez pas à partager vos pensées dans les commentaires ci-dessous, ou à me corriger si j'ai fait une erreur.

### Ressources supplémentaires

1. [Hash Crash: The Basics of Hash Tables](https://medium.com/@bartobri/hash-crash-the-basics-of-hash-tables-bef82a8ea550)
2. [The Mighty Dictionary](https://pyvideo.org/pycon-us-2010/the-mighty-dictionary-55.html)
3. [Introduction to Algorithms](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844)