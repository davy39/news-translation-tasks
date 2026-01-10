---
title: Comment (et pourquoi) intégrer les concepts de domaine dans le code
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-11-12T07:48:19.000Z'
originalURL: https://freecodecamp.org/news/embedding-domain-concepts-in-code
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/2015-Gran-Paradiso-007.JPG
tags:
- name: Quality Software
  slug: quality-software
- name: Code Quality
  slug: code-quality
- name: '#Domain-Driven-Design'
  slug: domain-driven-design
- name: software design
  slug: software-design
- name: software development
  slug: software-development
seo_title: Comment (et pourquoi) intégrer les concepts de domaine dans le code
seo_desc: Code should clearly reflect the problem it’s solving, and thus openly expose
  that problem’s domain. Embedding domain concepts in code requires thought and skill,
  and doesn't drop out automatically from TDD. However, it is a necessary step on
  the road...
---

Le code doit clairement refléter le problème qu'il résout, et ainsi exposer ouvertement le domaine de ce problème. Intégrer les concepts de domaine dans le code nécessite de la réflexion et des compétences, et ne découle pas automatiquement du TDD. Cependant, c'est une étape nécessaire pour écrire un code facilement compréhensible.

J'étais récemment à une rencontre sur l'artisanat logiciel, où nous avons formé des paires pour résoudre un Berlin Clock Kata simplifié. Une Berlin Clock affiche l'heure à l'aide de rangées de lumières clignotantes, que vous pouvez voir ci-dessous (bien que dans le kata, nous avons simplement produit une représentation textuelle, et les lumières d'une rangée sont toutes de la même couleur).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/berlin-clock-2.gif)

## Solution initiale pilotée par les tests

La plupart des paires ont utilisé le TDD de l'intérieur vers l'extérieur, et il y avait beaucoup de solutions qui ressemblaient à ceci (code complet [disponible sur GitHub](https://github.com/ceddlyburge/berlin-clock-initial-tdd-solution/blob/master/BerlinClock.py)).

```python
def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

	return [
		seconds_row_lights(seconds % 2)
		, five_hours_row_lights(hours)
		, single_hours_row_lights(hours % 5)
		, five_minutes_row_lights(minutes)
		, single_minutes_row_lights(minutes % 5)
	]

def five_hours_row_lights(hours):
    lights_on = hours // 5
    lights_in_row = 4
    return lights_for_row("R", lights_on, lights_in_row)
	
# ...

```

Ce type de solution découle naturellement de l'application du TDD de l'intérieur vers l'extérieur au problème. Vous écrivez quelques tests pour la rangée des secondes, puis quelques tests pour la rangée des cinq heures, et ainsi de suite, puis vous assemblez le tout et faites un peu de refactoring. Cette solution expose certains des concepts de domaine à première vue :

* Il y a 5 rangées
* Il y a une rangée pour les secondes, 2 rangées pour les heures et 2 rangées pour les minutes

D'autres concepts sont disponibles après un peu de recherche, mais ne sont pas immédiatement évidents. Les rangées sont composées de lumières qui peuvent être allumées (ou présumément éteintes), et le nombre de lumières allumées est une indication de l'heure.

Cependant, certaines parties importantes du problème ne sont pas exposées. Et puisque je ne l'ai pas encore expliqué, vous ne savez probablement pas exactement comment fonctionne la Berlin Clock.

## Élever les concepts

Pour améliorer cela, nous pouvons rapprocher certains des détails qui sont enterrés dans les fonctions auxiliaires (comme `get_five_hours`) vers le haut du fichier. Cela vous amène à quelque chose comme ce qui suit (code complet [disponible sur GitHub](https://github.com/ceddlyburge/berlin-clock-elevated-concepts/blob/master/BerlinClock.py)), bien que l'inconvénient soit que cela casse presque tous les tests. Les solutions comme celle-ci sont plus rares sur GitHub, mais existent.

```python
def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

	single_seconds = seconds_row_lights(seconds % 2)
    five_hours = row_lights(
		light_colour="R",
		lights_on=hours // 5,
		lights_in_row=4)
    single_hours = row_lights(
		light_colour="R",
		lights_on=hours % 5,
		lights_in_row=4)
    five_minutes = row_lights(
		light_colour="Y",
		lights_on=minutes // 5,
		lights_in_row=11)
    single_minutes = row_lights(
		light_colour="Y",
		lights_on=minutes % 5,
		lights_in_row=4)

	return [
		single_seconds,
		five_hours,
		single_hours,
		five_minutes,
		single_minutes
	]

# ...

```

Cela améliore les concepts qui sont maintenant exposés à première vue :

* Il y a 5 rangées
* La rangée des secondes est un cas spécial
* Il y a 2 rangées pour les heures et 2 rangées pour les minutes
* Les rangées utilisent des lumières de différentes couleurs
* Les rangées ont un nombre différent de lumières

C'est assez bien, et c'est déjà mieux que la plupart des solutions existantes. Cependant, il reste un peu mystérieux comment les rangées sont liées entre elles (il y a 2 rangées pour afficher les heures et les minutes, donc présumément elles sont liées). Il n'est pas non plus évident quelle quantité de temps chaque lumière représente.

## Nommer les concepts implicites

Pour l'instant, certains des concepts (comme la quantité de temps que chaque lumière représente) sont implicites dans le code. Les rendre explicites, et les nommer, nous force à les comprendre et à intégrer cette compréhension dans le code.

Afin de rendre explicite la quantité de temps que chaque lumière représente, il semble sensé de passer une valeur `time_per_light` à `row_lights`. Cela signifie que nous devons pousser le calcul de `lights_on` dans `row_lights`.

Cela rend à son tour évident qu'il existe deux types de rangées : l'une liée au quotient (`\\`) de la valeur temporelle, et l'autre liée au reste / modulus (`%`). Si nous regardons le cas du quotient, nous voyons que le deuxième paramètre de l'opération est le `time_per_light`, qui est 5 dans les deux cas (5 heures dans un cas et 5 minutes dans l'autre).

Cela nous permet d'écrire ces rangées comme ceci :

```python
five_hour_row = row_lights(
	time_per_light=5,
	value=hours, 
	light_colour="R",
	lights_in_row=4)

```

Si nous tournons maintenant notre attention vers le cas du reste, nous réalisons que `time_per_light` est toujours singulier (une heure ou une minute), car il comble les lacunes dans le cas du quotient.

Par exemple, la rangée des cinq heures peut représenter 0, 5, 10, 15 ou 20 heures, mais rien entre les deux. Pour représenter n'importe quelle heure, il doit y avoir une autre rangée pour représenter +1, +2, +3 et +4. Cela signifie que cette rangée doit avoir exactement 4 lumières, et que chaque lumière doit représenter 1 heure.

Cela implique que le cas du reste dépend du quotient, que la plupart des gens décriraient comme une relation parent/enfant.

Avec cette connaissance en main, nous pouvons maintenant créer une fonction pour les rangées de reste enfant, et la solution ressemble maintenant à ceci (code complet [sur GitHub](https://github.com/ceddlyburge/berlin-clock)) :

```python
def berlin_clock_time(julian_time):
    hours, minutes, seconds = list(map(int, julian_time.split(":")))

	return [
		seconds_row_lights(
			seconds % 2),
		parent_row_lights(
			time_per_light=5,
			value=hours, 
			light_colour="R",
			lights_in_row=4),
		child_remainder_row_lights(
			parent_time_per_light=5,
			value=hours,
			light_colour="R"),
		parent_row_lights(
			time_per_light=5,
			value=minutes, 
			light_colour="Y",
			lights_in_row=11),
		child_remainder_row_lights(
			parent_time_per_light=5,
			light_colour="Y",
			value=minutes)
	]

# ...

```

Un rapide coup d'œil à ce code révèle maintenant presque tous les concepts de domaine :

* La première rangée représente les secondes et est un cas spécial
* Sur la deuxième rangée, chaque lumière "R" représente 5 heures
* La troisième rangée montre le reste de la deuxième
* Sur la quatrième rangée, chaque lumière "Y" représente 5 heures
* La cinquième rangée montre le reste de la quatrième

Cela a nécessité une certaine réflexion, ce qui nous aura coûté un peu de temps / d'argent. Mais nous avons augmenté notre compréhension du problème en le faisant, et surtout, nous avons intégré cette connaissance dans le code. Cela signifie que la prochaine personne à lire le code n'aura pas à faire cela, ce qui économisera du temps / de l'argent. Puisque nous passons environ 10 fois plus de temps à lire du code qu'à l'écrire, cela est probablement une entreprise qui en vaut la peine.

Intégrer cette compréhension a également rendu plus difficile pour les futurs programmeurs de faire des erreurs. Par exemple, le concept de rangées parent/enfant n'existait pas dans les exemples précédents, et il serait facile de les mal assortir. Maintenant, le concept est clair, et les valeurs sont principalement calculées pour vous. Il est également plus facile de refactoriser pour supporter de nouvelles variantes d'horloge, par exemple où les lumières de la première rangée d'heures représentent 6 heures.

## Jusqu'où faut-il aller ?

Il y a des choses que nous pouvons faire pour aller plus loin. Par exemple, le `parent_time_per_light` d'une rangée enfant doit correspondre au `time_per_light` de son parent, et il n'y a rien qui impose cela. Il y a également une relation entre `time_per_light` et `lights_in_row` pour les rangées parent, et encore une fois, elle n'est pas imposée.

Cependant, pour l'instant, nous ne sommes tenus de supporter qu'une seule variante d'horloge, donc celles-ci ne valent probablement pas la peine d'être faites. Lorsqu'un changement est requis pour le code, nous devrions refactoriser de sorte que le changement soit facile (ce qui peut être difficile) et ensuite faire le changement facile.

## Conclusions

Intégrer les concepts de domaine dans le code nécessite de la réflexion et des compétences, et le TDD ne le fera pas nécessairement pour vous. Cela prend plus de temps qu'une solution naïve, mais rend le code plus facile à comprendre, et économisera très probablement du temps à moyen terme. Le temps, c'est de l'argent, et trouver le bon équilibre entre dépenser du temps maintenant et en économiser plus tard est également une compétence importante pour un programmeur professionnel.