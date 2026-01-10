---
title: Dictionnaire Python – Comment effectuer des opérations CRUD sur les dictionnaires
  en Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-01-11T19:05:01.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-python-dictionaries
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/dictionary.png
tags:
- name: crud
  slug: crud
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Dictionnaire Python – Comment effectuer des opérations CRUD sur les dictionnaires
  en Python
seo_desc: "One of the most important composite data types in Python is the dictionary.\
  \ It's a collection you use to store data in {key:value} pairs. \nDictionaries are\
  \ ordered and mutable, and they cannot store duplicate data. Just keep in mind that\
  \ before Pytho..."
---

L'un des types de données composites les plus importants en Python est le dictionnaire. Il s'agit d'une collection que vous utilisez pour stocker des données sous forme de paires `{clé:valeur}`.

Les dictionnaires sont ordonnés et mutables, et ils ne peuvent pas stocker de données en double. Gardez simplement à l'esprit qu'avant Python 3.6, les dictionnaires étaient non ordonnés.

Très bien, plongeons-nous et apprenons-en plus sur leur fonctionnement.

## Comment créer un dictionnaire en Python

Comme nous le savons, un dictionnaire est composé d'une collection de paires `{clé:valeur}`. Un deux-points (`:`) sépare chaque clé de sa valeur associée.

Nous pouvons définir un dictionnaire en enfermant une liste séparée par des virgules de paires clé-valeur dans des accolades (`{}`).

```python
mon_dict = {
    "Nom": "Ashutosh Krishna",
    "Rôle": 23,
    "Matières": ["OS", "CN", "DBMS"]
}
```

Dans l'exemple ci-dessus, `Nom`, `Rôle` et `Matières` sont les clés du dictionnaire `mon_dict`. `Ashutosh Krishna`, `23` et `["OS", "CN", "DBMS"]` sont leurs valeurs respectives.

Nous pouvons également déclarer un dictionnaire en utilisant la fonction intégrée `dict()` comme ceci :

```python
mon_dict = dict({
    "Nom": "Ashutosh Krishna",
    "Rôle": 23,
    "Matières": ["OS", "CN", "DBMS"]
})

```

Une liste de tuples fonctionne bien pour cela :

```python
mon_dict = dict([
    ("Nom", "Ashutosh Krishna"), 
    ("Rôle", 23),
    ("Matières", ["OS", "CN", "DBMS"])
])

```

Ils peuvent également être spécifiés comme arguments de mots-clés.

```python
mon_dict = dict(
    Nom="Ashutosh Krishna", 
    Rôle=23, 
    Matières=["OS", "CN", "DBMS"]
)

```

## Comment accéder aux valeurs d'un dictionnaire en Python

Vous ne pouvez pas accéder aux valeurs d'un dictionnaire en utilisant l'index.

```python
mon_dict = {
    "Nom": "Ashutosh Krishna",
    "Rôle": 23,
    "Matières": ["OS", "CN", "DBMS"]
}

print(mon_dict[1])

```

Si vous essayez de faire cela, cela générera une erreur **KeyError** comme ceci :

```bash
Traceback (most recent call last):
  File "C:\Users\ashut\Desktop\Test\hello\test.py", line 7, in <module>
    print(mon_dict[1])
KeyError: 1
```

Remarquez que l'exception s'appelle KeyError. Cela signifie-t-il que les valeurs du dictionnaire peuvent être accessibles en utilisant les clés ? Oui, vous avez raison !

Vous pouvez obtenir une valeur d'un dictionnaire en spécifiant sa clé correspondante entre crochets (`[]`).

```repl
>>> mon_dict['Nom']          
'Ashutosh Krishna'
>>> mon_dict['Matières'] 
['OS', 'CN', 'DBMS']
```

Si une clé n'existe pas dans le dictionnaire, nous obtenons une exception KeyError comme nous l'avons vu ci-dessus.

```repl
>>> mon_dict['Collège']  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Collège'
```

Mais nous pouvons également éviter cette erreur en utilisant la fonction `get()`.

```repl
>>> mon_dict.get('Collège')
>>> 
```

Si la clé existe dans le dictionnaire, elle récupérera la valeur correspondante. Mais si elle n'existe pas, elle ne générera pas d'erreur.

## Comment mettre à jour un dictionnaire en Python

Les dictionnaires sont mutables, ce qui signifie qu'ils peuvent être modifiés. Nous pouvons ajouter une nouvelle paire `{clé:valeur}` ou modifier celles existantes.

Ajouter un nouvel élément dans le dictionnaire est assez facile en utilisant l'opérateur d'affectation, comme ceci :

```repl
>>> mon_dict['Collège'] = 'NSEC'
>>> mon_dict                    
{'Nom': 'Ashutosh Krishna', 'Rôle': 23, 'Matières': ['OS', 'CN', 'DBMS'], 'Collège': 'NSEC'}
```

Si la clé est déjà présente dans le dictionnaire, elle mettra à jour la valeur de cette clé.

```repl
>>> mon_dict['Rôle'] = 35
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Rôle': 35, 'Matières': ['OS', 'CN', 'DBMS'], 'Collège': 'NSEC'}
```

### Comment mettre à jour un dictionnaire en utilisant la méthode update()

Nous pouvons également mettre à jour le dictionnaire en utilisant la méthode intégrée `update()` comme ceci :

```repl
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Rôle': 35, 'Matières': ['OS', 'CN', 'DBMS'], 'Collège': 'NSEC'}
>>> autre_dict = {'Branche': 'IT'}
>>> mon_dict.update(autre_dict)
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Rôle': 35, 'Matières': ['OS', 'CN', 'DBMS'], 'Collège': 'NSEC', 'Branche': 'IT'}
>>>
```

La méthode `update()` prend soit un dictionnaire, soit un objet itérable de paires clé/valeur (généralement des tuples).

```repl
>>> mon_dict.update(Branche='CSE') 
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Rôle': 35, 'Matières': ['OS', 'CN', 'DBMS'], 'Collège': 'NSEC', 'Branche': 'CSE'}
```

## Comment supprimer des éléments d'un dictionnaire en Python

Il existe plusieurs façons de supprimer des éléments d'un dictionnaire Python.

### Comment supprimer des éléments d'un dictionnaire avec la méthode `pop()`

Nous pouvons supprimer un élément particulier dans un dictionnaire en utilisant la méthode `pop()`. Cette méthode supprime un élément avec la `clé` fournie et retourne la `valeur`.

```repl
>>> rôle = mon_dict.pop('Rôle') 
>>> rôle
35
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Matières': ['OS', 'CN', 'DBMS'], 'Collège': 'NSEC', 'Branche': 'CSE'}
```

### Comment supprimer un élément d'un dictionnaire avec la méthode `popitem()`

La méthode `popitem()` supprime la dernière paire clé-valeur et la retourne sous forme de tuple :

```repl
>>> mon_dict.popitem()
('Branche', 'CSE')
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Matières': ['OS', 'CN', 'DBMS'], 'Collège': 'NSEC'}
```

### Comment supprimer un élément d'un dictionnaire avec le mot-clé `del`

Vous pouvez utiliser le mot-clé `del` pour supprimer une paire `{clé:valeur}` particulière ou même le dictionnaire entier.

```repl
>>> del mon_dict['Matières'] 
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Collège': 'NSEC'}
>>> del mon_dict
>>> mon_dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mon_dict' is not defined
```

### Comment supprimer un élément d'un dictionnaire avec la méthode `clear()`

La méthode `clear` efface toutes les paires `{clé:valeur}` du dictionnaire.

```repl
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Rôle': 23, 'Matières': ['OS', 'CN', 'DBMS']}
>>> mon_dict.clear()
>>> mon_dict
{}
```

Remarquez qu'après l'appel de la méthode `clear()`, l'impression du dictionnaire ne génère pas d'erreur car la méthode `clear()` ne supprime pas le dictionnaire. Mais le mot-clé `del` supprime également le dictionnaire. C'est pourquoi nous obtenons une erreur NameError dans ce cas.

## Opérateurs et fonctions intégrées des dictionnaires

Parlons de deux opérateurs et fonctions intégrées importants que nous pouvons utiliser avec les dictionnaires.

### Fonction `len()`

La fonction `len()` retourne le nombre de paires clé-valeur dans un dictionnaire :

```repl
>>> mon_dict
{'Nom': 'Ashutosh Krishna', 'Rôle': 23, 'Matières': ['OS', 'CN', 'DBMS']}
>>> len(mon_dict)
3
```

### Fonction `sorted()`

La fonction `sorted()` trie les éléments d'un itérable donné dans un ordre spécifique (ascendant ou descendant) et le retourne sous forme de liste.

```repl
>>> sorted(mon_dict)
['Nom', 'Rôle', 'Matières']
```

### Opérateur `in`

Vous pouvez utiliser l'opérateur `in` pour vérifier si une clé est présente dans le dictionnaire ou non.

```repl
>>> 'Rôle' in mon_dict
True
>>> 'Collège' in mon_dict
False
```

## Méthodes intégrées des dictionnaires

Il existe diverses méthodes intégrées disponibles dans un dictionnaire Python. Nous en avons discuté quelques-unes précédemment telles que `clear()`, `pop()` et `popitem()`. Voyons quelques autres méthodes également.

<table border="0" style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px !important; margin-left: 0px; padding: 0px; box-sizing: border-box; border-collapse: collapse; width: 728px; white-space: pre-wrap; background-color: rgb(248, 250, 255); border: none; color: rgb(37, 38, 94); font-family: euclid_circular_a, arial, &quot;source sans pro&quot;, &quot;helvetica neue&quot;, helvetica, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><tbody style="margin: 0px; padding: 0px; box-sizing: border-box; border-top: 1px solid rgb(204, 204, 204);"><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><th style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); text-align: left; min-width: 100px; font-weight: 400;">Méthode</th><th style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); text-align: left; min-width: 100px; font-weight: 400;">Description</th></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">clear()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Supprime tous les éléments du dictionnaire.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">copy()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Retourne une copie superficielle du dictionnaire.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">fromkeys(seq[, v])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Retourne un nouveau dictionnaire avec des clés de <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">seq</var> et une valeur égale à <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">v</var> (par défaut <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">None</code>).</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">get(key[,d])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Retourne la valeur de la <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var>. Si la <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> n'existe pas, retourne <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> (par défaut <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">None</code>).</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">items()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Retourne un nouvel objet des éléments du dictionnaire au format (clé, valeur).</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">keys()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Retourne un nouvel objet des clés du dictionnaire.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">pop(key[,d])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Supprime l'élément avec la <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> et retourne sa valeur ou <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> si <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> n'est pas trouvé. Si <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> n'est pas fourni et que la <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> n'est pas trouvée, elle lève une erreur <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">KeyError</code>.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">popitem()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Supprime et retourne un élément arbitraire (<strong style="margin: 0px; padding: 0px; box-sizing: border-box; font-weight: bolder;">clé, valeur</strong>). Lève une erreur <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">KeyError</code> si le dictionnaire est vide.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">setdefault(key[,d])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Retourne la valeur correspondante si la <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> est dans le dictionnaire. Si ce n'est pas le cas, insère la <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">key</var> avec une valeur de <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> et retourne <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">d</var> (par défaut <code style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; font-size: 14px; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; display: inline-block; line-height: 20px;">None</code>).</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">update([other])</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 1px solid rgba(0, 0, 0, 0.1); min-width: 100px; color: rgba(37, 38, 94, 0.7);">Met à jour le dictionnaire avec les paires clé/valeur de <var style="margin: 0px 2px; padding: 0px 4px; box-sizing: border-box; border: 1px solid rgb(211, 220, 230); border-radius: 4px; font-style: normal; font-family: &quot;droid sans mono&quot;, inconsolata, menlo, consolas, &quot;bitstream vera sans mono&quot;, courier, monospace; display: inline-block; font-size: 14px; line-height: 20px;">other</var>, écrasant les clés existantes.</td></tr><tr style="margin: 0px; padding: 0px; box-sizing: border-box;"><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 0px; min-width: 100px; color: rgba(37, 38, 94, 0.7);">values()</td><td style="margin: 0px; padding: 12px 24px; box-sizing: border-box; border-bottom: 0px; min-width: 100px; color: rgba(37, 38, 94, 0.7);">Retourne un nouvel objet des valeurs du dictionnaire</td></tr></tbody></table>

## Comment parcourir un dictionnaire

Par défaut, lorsque nous utilisons une boucle for pour parcourir un dictionnaire, nous obtenons les clés :

```python
mon_dict = {
    "Nom": "Ashutosh Krishna",
    "Rôle": 23,
    "Matières": ["OS", "CN", "DBMS"]
}

for item in mon_dict:
    print(item)
```

Sortie :

```bash
Nom
Rôle
Matières
```

Nous pouvons également parcourir un dictionnaire de les manières suivantes :

### Comment parcourir un dictionnaire en utilisant la méthode `items()`

Lorsque nous utilisons la méthode `items()` pour parcourir un dictionnaire, elle retourne un tuple de clé et de valeur à chaque itération. Ainsi, nous pouvons obtenir directement la clé et la valeur dans ce cas :

```python
mon_dict = {
    "Nom": "Ashutosh Krishna",
    "Rôle": 23,
    "Matières": ["OS", "CN", "DBMS"]
}

for key, value in mon_dict.items():
    print(key, value)

```

Sortie :

```bash
Nom Ashutosh Krishna
Rôle 23
Matières ['OS', 'CN', 'DBMS']
```

### Comment parcourir un dictionnaire en utilisant `keys()`

Dans ce cas, nous obtenons la clé à chaque itération.

```python
mon_dict = {
    "Nom": "Ashutosh Krishna",
    "Rôle": 23,
    "Matières": ["OS", "CN", "DBMS"]
}

for key in mon_dict.keys():
    print(key)

```

Sortie :

```bash
Nom
Rôle
Matières
```

### Comment parcourir un dictionnaire en utilisant `values()`

Dans ce cas, nous obtenons les valeurs du dictionnaire directement.

```python
mon_dict = {
    "Nom": "Ashutosh Krishna",
    "Rôle": 23,
    "Matières": ["OS", "CN", "DBMS"]
}

for value in mon_dict.values():
    print(value)

```

Sortie :

```bash
Ashutosh Krishna
23
['OS', 'CN', 'DBMS']
```

## Comment fusionner des dictionnaires en Python

Nous devons souvent fusionner des dictionnaires en Python. J'ai écrit un article séparé sur ce sujet, que vous pouvez lire [ici](https://iread.ga/posts/76/how-to-merge-dictionaries-in-python).

## Conclusion

Dans cet article, nous avons appris ce que sont les dictionnaires Python et comment effectuer des opérations CRUD sur eux. Nous avons également vu plusieurs méthodes et fonctions associées.

J'espère que vous avez apprécié – et merci pour la lecture !

<a class="cta-button" href="https://newsletter.ashutoshkrris.tk" target="_blank">S'abonner à ma newsletter</a>