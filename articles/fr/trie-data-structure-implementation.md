---
title: Implémentation de la Structure de Données Trie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-05T23:29:00.000Z'
originalURL: https://freecodecamp.org/news/trie-data-structure-implementation
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cc2740569d1a4ca3403.jpg
tags:
- name: data structures
  slug: data-structures
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Implémentation de la Structure de Données Trie
seo_desc: 'Introduction

  The word trie is an inflix of the word “retrieval”, because the trie can find a
  single word in a dictionary with only a prefix of the word.

  Trie is an efficient data retrieval data structure. Using trie, search complexities
  can be brough...'
---

## **Introduction**

Le mot trie est un infixe du mot « **retrie**val », car le trie peut trouver un seul mot dans un dictionnaire avec seulement un préfixe du mot.

Trie est une structure de données efficace pour la récupération de données. En utilisant trie, les complexités de recherche peuvent être réduites à une limite optimale, c'est-à-dire la longueur de la chaîne.

Il s'agit d'une structure d'arbre multi-voies utile pour stocker des chaînes sur un alphabet, lorsque nous les stockons. Elle a été utilisée pour stocker de grands dictionnaires d'anglais, par exemple, des mots dans des programmes de vérification orthographique. Cependant, la pénalité sur les tries est les exigences de stockage.

## **Qu'est-ce qu'un trie ?**

Un trie est une structure de données de type arbre qui stocke des chaînes et vous aide à trouver les données associées à cette chaîne en utilisant le préfixe de la chaîne.

Par exemple, disons que vous prévoyez de construire un dictionnaire pour stocker des chaînes avec leurs significations. Vous devez vous demander pourquoi je ne peux pas simplement utiliser une table de hachage pour obtenir l'information.

Oui, vous pouvez obtenir des informations en utilisant une table de hachage, mais les [tables de hachage](https://www.freecodecamp.org/news/hash-tables/) ne peuvent trouver des données que lorsque la chaîne correspond exactement à celle que nous avons ajoutée. Mais le trie nous donnera la capacité de trouver des chaînes avec des préfixes communs, un caractère manquant, etc., en moins de temps, par rapport à une table de hachage.

Un trie ressemble généralement à ceci,

![Trie](https://discourse-user-assets.s3.amazonaws.com/original/2X/c/c43e222a6f9152512d73f97b8117db5c074bbc8e.png)

Ceci est une image d'un Trie, qui stocke les mots {assoc, algo, all, also, tree, trie}.

## **Comment implémenter un trie**

Implémentons un trie en python, pour stocker des mots avec leurs significations à partir d'un dictionnaire anglais.

```text
ALPHABET_SIZE = 26 # Pour l'anglais

class TrieNode:
	def __init__(self):
		self.edges = [None]*(ALPHABET_SIZE) # Chaque index correspondant à chaque caractère.
		self.meaning = None # Signification du mot.
		self.ends_here = False # Nous indique si le mot se termine ici.
```

Comme vous pouvez le voir, les arêtes sont de longueur 26, chaque index correspondant à chaque caractère de l'alphabet. 'A' correspond à 0, 'B' à 1, 'C' à 2 … 'Z' à l'index 25. Si le caractère que vous cherchez pointe vers `None`, cela implique que le mot n'est pas dans le trie.

Un Trie typique doit implémenter au moins ces deux fonctions :

* `add_word(word,meaning)`
* `search_word(word)`
* `delete_word(word)`

De plus, on peut aussi ajouter quelque chose comme

* `get_all_words()`
* `get_all_words_with_prefix(prefix)`

## Ajout d'un mot au trie

```text
	def add_word(self,word,meaning):
		if len(word)==0:
			self.ends_here = True # Parce que nous avons atteint la fin du mot
			self.meaning = meaning # Ajout de la signification à ce nœud
			return
		ch = word[0] # Premier caractère
		# Valeur ASCII du premier caractère (moins) la valeur ASCII de 'a'-> le premier caractère de notre ALPHABET nous donne l'index de l'arête que nous devons rechercher.
		index = ord(ch) - ord('a')
		if self.edges[index] == None:
			# Cela implique qu'il n'y a pas encore de préfixe avec ce caractère.
			new_node = TrieNode()
			self.edges[index] = new_node

		self.edges[index].add(word[1:],meaning) # Ajout du reste du mot
```

## Récupération des données

```text
	def search_word(self,word):
		if len(word)==0:
			if self.ends_here:
				return True
			else:
				return "Le mot n'existe pas dans le Trie"
		ch = word[0]
		index = ord(ch)-ord('a')
		if self.edge[index]== None:
			return False
		else:
			return self.edge[index].search_word(word[1:])
```

La fonction `search_word` nous indiquera si le mot existe dans le Trie ou non. Puisque le nôtre est un dictionnaire, nous devons également récupérer la signification, déclarons maintenant une fonction pour cela.

```text
	def get_meaning(self,word):
		if len(word)==0 :
			if self.ends_here:
				return self.meaning
			else:
				return "Le mot n'existe pas dans le Trie"
		ch = word[0]
		index = ord(ch) - ord('a')
		if self.edges[index] == None:
			return "Le mot n'existe pas dans le Trie"
		else:
			return self.edges[index].get_meaning(word[1:])
```

## Suppression des données

En supprimant des données, vous devez simplement changer la variable `ends_here` en `False`. Cela n'altère pas les préfixes, mais supprime tout de même la signification et l'existence du mot du trie.

```text
	def delete_word(self,word):
		if len(word)==0:
			if self.ends_here:
				self.ends_here = False
				self.meaning = None
				return "Supprimé"
			else:
				return "Le mot n'existe pas dans le Trie"
		ch = word[0]
		index = ord(ch) - ord('a')
		if self.edges[index] == None:
			return "Le mot n'existe pas dans le Trie"
		else:
			return self.edges[index].delete_word(word[1:])
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le Code](https://repl.it/CWbr)