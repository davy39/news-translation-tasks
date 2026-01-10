---
title: Comment écrire du code facilement descriptible
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-10-02T20:34:23.000Z'
originalURL: https://freecodecamp.org/news/writing-describable-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/writing-describable-code.jpg
tags:
- name: Code Quality
  slug: code-quality
- name: software design
  slug: software-design
- name: software design patterns
  slug: software-design-patterns
seo_title: Comment écrire du code facilement descriptible
seo_desc: When code is not describable using words, most people have to do some mental
  mapping to turn it in to words. This wastes mental energy, and you run the risk
  of getting the mapping wrong. Different people will map to different words, which
  leads to co...
---

Lorsque le code ne peut pas être décrit avec des mots, la plupart des gens doivent faire un effort mental pour le traduire en mots. Cela gaspille de l'énergie mentale, et vous risquez de vous tromper dans la traduction. Différentes personnes traduiront en différents mots, ce qui entraîne de la confusion lors de la discussion sur le code. 

Ceci est généralement un terrain fertile pour les bugs nés de la mauvaise communication / incompréhension, et la correction de ces bugs introduit souvent de nouveaux bugs, pour les mêmes raisons. À la fin, cela devient un code que personne ne comprend vraiment ou ne veut toucher.

## Exemple de code indescriptible

Il est facile de penser que le code est déjà un langage écrit. S'il semble simple, il devrait être facile à lire, à parler et à écouter. Cependant, ce n'est pas toujours le cas.

Ci-dessous se trouve une solution courante pour décider si une année est bissextile.

```python
(divisibleBy(4) and not divisibleBy(100)) or divisibleBy(400)

```

Ce n'est pas un code excessivement compliqué. Il appelle une fonction 3 fois, a 3 opérateurs (and, or, not), et a deux niveaux d'imbrication.

Cependant, si vous prenez un moment pour essayer de décrire l'algorithme en mots, je pense que vous trouverez cela difficile.

Peut-être "Une année est bissextile si elle est divisible par 4 et non divisible par 100, ou divisible par 400" ?

Le problème avec cela est que le code a des parenthèses, mais les mots n'en ont pas. Ils ne peuvent donc pas décrire adéquatement la condition, et si "ou divisible par 400" s'applique à "divisible par 4" ou "non divisible par 400". Vous pourriez essayer de gesticuler ou de varier la longueur des pauses entre les déclarations, mais espérons qu'il est évident qu'il y a beaucoup de potentiel pour l'erreur.

## Refactorisation en code descriptible

Au lieu de cela, nous pouvons commencer par décrire la condition avec des mots, puis rendre les mots aussi clairs et concis que possible. Nous pourrions commencer par ceci :

"400 ans est un cas spécial. Si une année est divisible par 400, alors c'est une année bissextile. 100 ans est également un cas spécial. Si une année est divisible par 100, alors ce n'est pas une année bissextile, sauf si elle est également divisible par 400, le cas spécial de 400 ans prend la priorité. S'il n'y a pas de cas spéciaux, alors l'année est bissextile si elle est divisible par 4."

Ceci est clair, mais n'est pas concis, donc nous voudrions probablement le raccourcir un peu :

"Si une année est divisible par 400, alors c'est une année bissextile. Sinon, si elle est divisible par 100, alors c'est une année normale, sinon c'est une année bissextile si elle est divisible par 4."

Si nous transformons ces mots en code, nous obtenons probablement quelque chose comme ceci :

```python
	if divisbleBy(400):
		return LeapYear
	elif divisbleBy(100)
		return NormalYear
	elif divisbleBy(4):
		return LeapYear
	else:
		return NormalYear

```

## Conclusions

Le code difficile à comprendre est une occurrence quotidienne pour pratiquement tous les programmeurs. Nous pouvons nous aider nous-mêmes et nos collègues en écrivant du code qui est facile à décrire en mots.

Et la grande chose est que faire cela est en fait plus facile que d'écrire du code de n'importe quelle autre manière, car il n'y a pas de traduction mentale / d'effort mental gaspillé. Le seul "truc" est de décrire l'algorithme en mots, puis d'écrire le code pour correspondre aux mots.

Dans de nombreuses organisations, l'algorithme sera déjà décrit en mots, dans le cadre de tests d'acceptation ou de stories utilisateurs, ce qui améliorera encore la productivité.