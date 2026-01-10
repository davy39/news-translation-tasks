---
title: Sous-chaîne Python – Comment découper une chaîne de caractères
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-27T15:24:00.000Z'
originalURL: https://freecodecamp.org/news/python-substring-how-to-slice-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pexels-hitesh-choudhary-7775640.jpg
tags:
- name: Python
  slug: python
seo_title: Sous-chaîne Python – Comment découper une chaîne de caractères
seo_desc: 'By Davis David

  In Python, a string is a sequence of characters that may contain special characters
  or alphanumeric characters.

  An example of a string is "we meet on Friday at 08:00 am". And you can access specific
  sub-parts of the string commonly kno...'
---

Par Davis David

En Python, une chaîne de caractères est une séquence de caractères qui peut contenir des caractères spéciaux ou alphanumériques.

Un exemple de chaîne est _"nous nous rencontrons vendredi à 08h00"_. Et vous pouvez accéder à des parties spécifiques de la chaîne, communément appelées sous-chaînes.

Nous pouvons définir une sous-chaîne comme une séquence de caractères au sein d'une chaîne. Dans l'exemple précédent, les sous-chaînes Python peuvent être "vendredi", "à", et "rencontrons", par exemple.

## Comment générer une sous-chaîne en Python

Python offre différentes méthodes pour générer une sous-chaîne, vérifier si une sous-chaîne est présente, obtenir l'index d'une sous-chaîne, et plus encore.

Vous pouvez extraire une sous-chaîne d'une chaîne en utilisant le découpage avec des indices comme suit :

`chaîne[début:fin:pas]`

* **début** - L'index de départ de la sous-chaîne.
* **fin** - L'index final de la sous-chaîne.
* **pas** - Un nombre spécifiant le pas du découpage. La valeur par défaut est 1.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image--2-.png)

Les indices peuvent être des nombres positifs ou négatifs. Les indices positifs commencent au début et vont jusqu'à la fin de la chaîne, tandis que les indices négatifs commencent à la fin et vont jusqu'au début de la chaîne.

Dans cet article, vous apprendrez à effectuer diverses opérations liées aux sous-chaînes en Python.

## Comment obtenir les premiers n caractères d'une chaîne en Python

Cet exemple vous montrera comment découper les 5 premiers caractères de la chaîne.

```python
chaîne = "bonjour le monde"
print(chaîne[:5])

```

Ici, vous définissez l'index de fin qui est 5. L'index de début est par défaut 0.

Le résultat est `'bonjo'`.

## Comment obtenir les caractères du milieu d'une chaîne via les sous-chaînes Python

Cet exemple vous montrera comment découper les caractères de l'index 3 à l'index 5 de la chaîne.

```python
chaîne = "bonjour le monde"
print(chaîne[3:5])

```

Le résultat est `'lo'`.

## Comment obtenir le dernier caractère d'une chaîne en Python

Pour obtenir le dernier caractère, utilisez l'index -1 (index négatif). Consultez l'exemple suivant :

```python
chaîne = "freecodecamp"
print(chaîne[-1])

```

Le résultat sera `'p'`.

## Comment obtenir les derniers n caractères d'une chaîne en Python

Dans cet exemple, vous allez découper les 4 derniers caractères de la chaîne. Ici, vous utilisez l'index négatif pour commencer le découpage à partir de la fin de la chaîne.

```python
chaîne = "freecodecamp"
print(chaîne[-4:])

```

Le résultat sera `'camp'`.

## Comment découper la chaîne avec des pas via les sous-chaînes Python

Vous pouvez découper la chaîne avec des pas après avoir indiqué un index de début et un index de fin. Par défaut, le pas est 1, mais dans l'exemple suivant, la taille du pas est 2.

```python
chaîne = "bienvenue chez freecodecamp"
print(chaîne[::2])

```

Le résultat sera `'bieucez rcedm'`.

## Comment vérifier si une sous-chaîne est présente dans une chaîne en Python

Parfois, vous souhaitez vérifier si une sous-chaîne est présente dans une chaîne. L'exemple suivant validera si la sous-chaîne 'code' est dans la chaîne :

```python
sous_chaîne = "code"
chaîne = "bienvenue chez freecodecamp"
print(sous_chaîne in chaîne)

```

Si elle est présente, elle retournera True, sinon False.

Ici, le résultat sera `True`.

## Une autre façon de vérifier si la sous-chaîne Python est présente dans la chaîne

Vous pouvez utiliser la méthode `find()` pour vérifier si une sous-chaîne est présente dans la chaîne.

Vérifions l'exemple suivant :

```python
sous_chaîne = "zz"
chaîne = "bonjour le monde"
print(chaîne.find(sous_chaîne))

```

Si elle est disponible, elle retourne l'index le plus à gauche de la sous-chaîne, sinon elle retourne -1 (ce qui signifie qu'elle n'est pas disponible).

Ici, le résultat est `-1`, ce qui signifie que **"zz"** n'est pas présent dans "bonjour le monde".

## Comment obtenir le caractère d'un index donné dans une chaîne en Python

Vous pouvez choisir de découper un caractère spécifique selon son numéro d'index.

```python
chaîne = "bonjour le monde"
print(chaîne[4])

```

Le résultat sera `'o'`.

## Comment créer une liste de sous-chaînes à partir d'une chaîne en Python

Vous pouvez utiliser la méthode **`split()`** pour créer une liste de sous-chaînes. Vérifions l'exemple suivant :

```python
chaîne = "bienvenue chez freecodecamp plateforme"
print(chaîne.split())

```

Le résultat sera `['bienvenue', 'chez', 'freecodecamp', 'plateforme']`

## Comment inverser une chaîne en Python avec des pas négatifs

Pour inverser la chaîne, le pas doit être une valeur négative, par exemple -1.

```python
chaîne = "bienvenue chez freecodecamp"
print(chaîne[::-1])

```

Le résultat est `'pmacedoceerf ot emoclew'`.

## Comment compter combien de fois une sous-chaîne est présente dans une chaîne en Python

Vous pouvez utiliser la méthode `count()` pour savoir combien de fois une sous-chaîne particulière est présente dans une chaîne.

```python
chaîne = "nous aurons une leçon de codage rapide cet après-midi"
print(chaîne.count('midi'))

```

Le résultat est 1.

## Réflexions finales sur les sous-chaînes Python

Félicitations 👏👏, vous êtes arrivé à la fin de cet article ! J'espère que vous avez appris quelque chose de nouveau sur les sous-chaînes Python.

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com).

Et vous pouvez lire plus d'articles comme celui-ci [ici](https://hackernoon.com/u/davisdavid?ref=hackernoon.com)