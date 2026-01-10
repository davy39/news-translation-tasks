---
title: Exemple de commentaire JSON — Comment commenter dans les fichiers JSON
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-26T14:56:30.000Z'
originalURL: https://freecodecamp.org/news/json-comment-example-how-to-comment-in-json-files
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/abstract-art-blur-bright-373543.jpg
tags:
- name: data
  slug: data
- name: json
  slug: json
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
seo_title: Exemple de commentaire JSON — Comment commenter dans les fichiers JSON
seo_desc: 'By Amy Haddad

  If you’re having trouble adding comments to your JSON file, there’s a good reason:
  JSON doesn’t support comments.

  “I removed comments from JSON because I saw people were using them to hold parsing
  directives, a practice which would have...'
---

Par Amy Haddad

Si vous avez des difficultés à ajouter des commentaires à votre fichier JSON, il y a une bonne raison : JSON ne supporte pas les commentaires.

« J'ai supprimé les commentaires de JSON parce que je voyais que les gens les utilisaient pour contenir des directives d'analyse, une pratique qui aurait détruit l'interopérabilité », écrit [Douglas Crockford](https://web.archive.org/web/20150105080225if_/https://plus.google.com/+DouglasCrockfordEsq/posts/RK8qyGVaGSr), qui a popularisé ce format de données basé sur du texte.

Cependant, il existe une solution de contournement. Et c'est ce dont parle cet article : comment ajouter des commentaires à votre fichier JSON.

## Ajouter des données comme commentaires

Une façon de contourner le problème des commentaires est d'ajouter des données à votre fichier JSON qui fonctionnent comme des commentaires.

Passons par un exemple, en commençant par ces informations dans notre fichier JSON :

```json
{
   "sport": "basketball",
   "coach": "Joe Smith",
   "wins": 15,
   "losses": 5
}
```

Maintenant, ajoutons une autre paire clé-valeur pour servir de commentaire, que vous pouvez voir dans la première ligne du code ci-dessous :

```json
{
   "_comment1": "ceci est mon commentaire",
   "sport": "basketball",
   "coach": "Joe Smith",
   "wins": 15,
   "losses": 5
}
```

Voici un autre exemple. Cette fois, nous utilisons deux tirets bas au début et à la fin de la clé :

```json
 "__comment2__": "ceci est un autre commentaire",
```

Les tirets bas aident à différencier le commentaire du reste des données dans notre fichier.

### Un mot de prudence

Il y a un détail important à garder à l'esprit.

Les commentaires que nous avons ajoutés à notre fichier JSON sont inclus dans l'objet JSON. En d'autres termes, les commentaires sont traités comme des données.

Voici ce que nous voulons dire.

Voici le code dans notre fichier, **`data.json`** :

```json
{
   "_comment1": "ceci est mon commentaire",
   "sport": "basketball",
   "coach": "Joe Smith",
   "wins": 15,
   "losses": 5
}
```

Maintenant, nous allons lire ces données depuis le fichier, `read_comments.py` :

```python
import json
with open("data.json", mode="r") as j_object:
   data = json.load(j_object)
print(data)
```

Le résultat inclut notre commentaire :

```json
{'_comment1': 'ceci est mon commentaire', 'sport': 'basketball', 'coach': 'Joe Smith', 'wins': 15, 'losses': 5}
```

Nous pouvons même extraire la valeur du commentaire de l'objet JSON : `ceci est mon commentaire` :

```python
import json
 
with open("data.json", mode="r") as j_object:
   data = json.load(j_object)
   print(data["_comment1"])
```

Gardez à l'esprit que le commentaire n'est un commentaire que pour le développeur, et non pour l'ordinateur.

### Un type différent de commentaire

Cette pratique de commentaire JSON est différente des commentaires dans les langages de programmation, comme Python, qui sont généralement ignorés lorsque le programme s'exécute.

```python
# Voici mon commentaire
word = "house"
for letter in word:
   print(letter)
```

Lorsque nous exécutons le programme Python ci-dessus, nous obtenons les lettres du mot, « house ». Mais nous ne voyons pas le commentaire. Il est ignoré.

## Options de commentaire

[JSMin](https://www.crockford.com/jsmin.html) est une autre option à considérer.

C'est un outil qui supprime les espaces blancs supplémentaires et les commentaires des fichiers JavaScript. Mais il fonctionne également sur les fichiers JSON. JSMin supprime les commentaires des fichiers JSON avant qu'ils ne soient analysés.

Il existe donc des options pour commenter dans les fichiers JSON. Bien que ce ne soient pas des solutions parfaites, il existe au moins des moyens d'inclure la documentation dont vous avez besoin lorsque vous en avez besoin.

_Je parle de l'apprentissage de la programmation et des meilleures façons de s'y prendre (_[amymhaddad.com](https://amymhaddad.com/)).