---
title: Fonctions en Python – Expliqué avec des exemples de code
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-07-28T17:24:21.000Z'
originalURL: https://freecodecamp.org/news/functions-in-python-a-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/FUNCTIONS-IN-PYTHON.png
tags:
- name: Python
  slug: python
seo_title: Fonctions en Python – Expliqué avec des exemples de code
seo_desc: "In any programming language, functions facilitate code reusability. In\
  \ simple terms, when you want to do something repeatedly, you can define that something\
  \ as a function and call that function whenever you need to. \nIn this tutorial,\
  \ we shall learn ..."
---

Dans n'importe quel langage de programmation, les fonctions facilitent la _réutilisation du code_. En termes simples, lorsque vous voulez faire quelque chose de manière répétée, vous pouvez définir cette chose comme une fonction et appeler cette fonction chaque fois que vous en avez besoin. 

Dans ce tutoriel, nous allons apprendre à propos des fonctions définies par l'utilisateur en Python.

Lorsque vous avez commencé à coder en Python, vous avez probablement utilisé la fonction intégrée `print()` dans votre programme `Hello World!` 😀 et la fonction `input()` pour lire les entrées de l'utilisateur. 

Tant que vous savez comment _utiliser_ ces fonctions, vous n'avez pas à vous soucier de la manière dont elles ont été implémentées. 

En programmation, cela s'appelle l'_abstraction_. Cela vous permet d'utiliser des fonctions en les appelant avec les arguments requis, sans avoir à vous soucier de leur fonctionnement réel.

Il existe une multitude de fonctions intégrées en Python. Dans cet article, nous allons voir comment nous pouvons définir et utiliser nos propres fonctions. Commençons !

## Syntaxe des fonctions Python

L'extrait suivant montre la syntaxe générale pour définir une fonction en Python :

```python
def nom_de_la_fonction(paramètres):
    # Ce que la fonction fait va ici
    return résultat 
```

* Vous devez utiliser le mot-clé `def`, donner un nom à votre fonction, suivi d'une paire de parenthèses, et terminer la ligne par un deux-points (:). 
* Si votre fonction prend des arguments, les noms des arguments (paramètres) sont mentionnés à l'intérieur des parenthèses ouvrante et fermante.
* Veuillez noter que dans la _définition de la fonction_, les arguments que votre fonction consomme sont appelés _paramètres_.
* Lorsque vous appelez la fonction avec des valeurs spécifiques pour ces paramètres, ils sont appelés _arguments_ ou paramètres réels. Cela est dû au fait que les _arguments_ dans l'_appel de fonction_ sont les valeurs utilisées pour les paramètres de la fonction.
* Ensuite, vous commencez un bloc en retrait. C'est le corps de la fonction qui décrit ce que votre fonction fait.
* Il y a une instruction `return` qui retourne le résultat de l'opération sur les arguments. L'instruction `return` retourne le contrôle au point où la fonction a été appelée à l'origine.

Notez que les `arguments` et l'instruction `return` sont optionnels. Cela signifie que vous pourriez avoir une fonction qui ne prend _aucun argument_ et qui _ne retourne rien_. 😀

Essayons maintenant de comprendre les déclarations ci-dessus à l'aide d'exemples simples.

## Comment créer une fonction simple en Python

Créons maintenant une fonction simple en Python qui salue l'utilisateur, comme montré ci-dessous : 

```python
def ma_fonction():
  print("Bonjour ! J'espère que vous allez bien")


```

Comme vous pouvez le voir, la fonction `ma_fonction()` :

* ne prend aucun argument, 
* ne retourne rien, et
* imprime `"Bonjour ! J'espère que vous allez bien"` chaque fois qu'elle est _appelée_.

Notez que la définition de la fonction ci-dessus est inerte jusqu'à ce que la fonction soit déclenchée ou appelée. Allons-y et appelons la fonction `ma_fonction()` et vérifions la sortie.

```python
ma_fonction()

# Sortie
Bonjour ! J'espère que vous allez bien
```

## Comment créer une fonction avec des arguments en Python

Maintenant, nous allons modifier la fonction `ma_fonction()` pour inclure le `nom` et le `lieu` de l'utilisateur.

```python
def ma_fonction(nom,lieu):
  print(f"Bonjour {nom}! Êtes-vous de {lieu}?")
```

Nous pouvons maintenant appeler `ma_fonction()` en passant deux chaînes de caractères pour le `nom` et le `lieu` de l'utilisateur, comme montré ci-dessous.

```python
ma_fonction("Jane","Paris")

# Sortie
Bonjour Jane! Êtes-vous de Paris?
```

Que se passe-t-il si vous spécifiez d'abord le `lieu` puis le `nom` ? Trouvons-le.

```python
ma_fonction("Hawaii","Robert")

# Sortie
Bonjour Hawaii! Êtes-vous de Robert?
```

Nous obtenons `Bonjour Hawaii! Êtes-vous de Robert?` – et cela n'a pas de sens. 🤒 Qu'est-ce qui cause ce problème ? 

Les arguments dans l'appel de fonction sont des _arguments positionnels_. Cela signifie que le premier argument dans l'appel de fonction est utilisé comme valeur du premier paramètre (`nom`) et le deuxième argument dans l'appel de fonction est utilisé comme valeur du deuxième paramètre (`lieu`).

Voir l'extrait de code ci-dessous. Au lieu de spécifier uniquement les arguments, nous avons mentionné les paramètres et les valeurs qu'ils prennent. 

```python
ma_fonction(lieu="Hawaii",nom="Robert")

# Sortie
Bonjour Robert! Êtes-vous de Hawaii?
```

Ce sont des _arguments clés_. L'ordre des arguments dans l'appel de fonction n'a pas d'importance tant que les noms des paramètres sont corrects.

## Comment créer une fonction avec des arguments par défaut en Python

Et si nous avions certains paramètres qui prennent une valeur spécifique la plupart du temps lors des appels de fonction ? 

Ne pouvons-nous pas faire mieux que d'appeler la fonction avec la même valeur pour un paramètre particulier ? 

Oui, nous pouvons faire mieux, et c'est à cela que servent les `arguments par défaut` ! 😀

Créons une fonction `calcul_total()` qui nous aide à calculer et à imprimer le montant total à payer dans un restaurant. Étant donné un `montant_facture` et le pourcentage du `montant_facture` que vous choisissez de payer comme pourboire (`pourcentage_pourboire`), cette fonction calcule le montant total que vous devriez payer. 

Notez comment la définition de la fonction inclut la valeur par défaut du paramètre `pourcentage_pourboire` à utiliser lorsque l'utilisateur ne spécifie pas de pourcentage de pourboire.

Exécutez l'extrait de code ci-dessous.👍🏽 Vous avez maintenant votre fonction prête !

```python
def calcul_total(montant_facture,pourcentage_pourboire=10):
  total = montant_facture*(1 + 0.01*pourcentage_pourboire)
  total = round(total,2)
  print(f"Veuillez payer ${total}")
```

Appelons maintenant la fonction de différentes manières. L'extrait de code ci-dessous montre ce qui suit :

* Lorsque vous appelez la fonction `calcul_total` avec seulement le `montant_facture`, par défaut le pourcentage de pourboire de 10 est utilisé. 
* Lorsque vous spécifiez explicitement le pourcentage de pourboire, le pourcentage de pourboire mentionné dans l'appel de fonction est utilisé.

```python
# spécifier seulement montant_facture
# la valeur par défaut du pourcentage de pourboire est utilisée

 calcul_total(150)
 # Sortie
 Veuillez payer $165.0
 
 # spécifier à la fois montant_facture et un pourcentage de pourboire personnalisé
 # le pourcentage de pourboire spécifié dans l'appel de fonction est utilisé
 
 calcul_total(200,15)
 # Sortie
 Veuillez payer $230.0
 
 calcul_total(167,7.5)
 # Sortie
 Veuillez payer $179.53
 
```

## Comment créer une fonction qui retourne une valeur en Python

Jusqu'à présent, nous n'avons créé que des fonctions qui peuvent ou non prendre des arguments et ne retournent rien. Maintenant, créons une fonction simple qui retourne le volume d'un cuboïde donné la `longueur`, la `largeur` et la `hauteur`.

```python
def volume_du_cuboide(longueur,largeur,hauteur):
  return longueur*largeur*hauteur
  
  
```

Rappelons que le mot-clé `return` retourne le contrôle au point où la fonction a été appelée. L'appel de fonction est remplacé par la `valeur de retour` de la fonction. 

Appelons la fonction `volume_du_cuboide()` avec les arguments de dimension nécessaires, comme montré dans l'extrait de code ci-dessous. Notez comment nous utilisons la variable `volume` pour capturer la valeur retournée par la fonction.

```
volume = volume_du_cuboide(5.5,20,6)
print(f"Le volume du cuboïde est {volume} unités cubiques")

# Sortie
Le volume du cuboïde est 660.0 unités cubiques
```

## Comment créer une fonction qui retourne plusieurs valeurs en Python

Dans notre exemple précédent, la fonction `volume_du_cuboide()` retournait seulement une valeur, à savoir le volume d'un cuboïde donné ses dimensions. Voyons comment nous pouvons retourner plusieurs valeurs d'une fonction.

* Pour retourner plusieurs valeurs d'une fonction, il suffit de spécifier les valeurs à retourner, séparées par une virgule.
* Par défaut, la fonction retourne les valeurs sous forme de tuple. Si il y a `N` valeurs de retour, nous obtenons un `N`-tuple.

Créons une fonction simple `cube()` qui retourne le volume et la surface totale d'un cube, donnée la longueur de son côté.

```python
def cube(cote):
  volume = cote **3
  surface = 6 * (cote**2)
  return volume, surface
```

Pour vérifier qu'un tuple est retourné, collectons-le dans une variable `valeurs_retournees`, comme montré ci-dessous :

```
valeurs_retournees = cube(8)
print(valeurs_retournees)

# Sortie
(512, 384)
```

Maintenant, nous allons _dépaqueter le tuple_ et stocker les valeurs dans deux variables différentes.

```
volume, surface = cube(6.5)
print(f"Le volume du cube est {volume} unités cubiques et la surface totale est {surface} unités carrées")

# Sorties
Le volume du cube est 274.625 unités cubiques et la surface totale est 253.5 unités carrées
```

## Comment créer une fonction qui prend un nombre variable d'arguments en Python

Commençons par poser quelques questions :

* Que faire si nous ne connaissons pas le nombre exact d'arguments à l'avance ? 
* Pouvez-vous créer des fonctions qui fonctionnent avec un nombre variable d'arguments ?

La réponse est oui ! Et nous allons créer une telle fonction tout de suite.

Créons une fonction simple `ma_somme_var()` qui retourne la somme de tous les nombres passés en argument. Cependant, le nombre d'arguments pourrait être potentiellement différent chaque fois que nous appelons la fonction.

Remarquez comment la définition de la fonction a maintenant `*args` au lieu du simple nom du paramètre. Dans le corps de la fonction, nous parcourons `args` jusqu'à ce que nous ayons utilisé tous les arguments. La fonction `ma_somme_var` retourne la somme de tous les nombres passés en arguments.

```python
def ma_somme_var(*args):
  somme = 0
  for arg in args:
    somme += arg
  return somme
```

Appelons maintenant la fonction `ma_somme_var()` avec un nombre différent d'arguments chaque fois et vérifions rapidement si les réponses retournées sont correctes ! 🤒

```python
# Exemple 1 avec 4 nombres
somme = ma_somme_var(99,10,54,23)
print(f"Les nombres que vous avez additionnés donnent {somme}")
# Sortie
Les nombres que vous avez additionnés donnent 186

# Exemple 2 avec 3 nombres
somme = ma_somme_var(9,87,45)
print(f"Les nombres que vous avez additionnés donnent {somme}")
# Sortie
Les nombres que vous avez additionnés donnent 141

# Exemple 3 avec 6 nombres
somme = ma_somme_var(5,21,36,79,45,65)
print(f"Les nombres que vous avez additionnés donnent {somme}")
# Sortie
Les nombres que vous avez additionnés donnent 251
```

## ⏸ Un rapide récapitulatif

Faisons un rapide résumé de ce que nous avons couvert. Dans ce tutoriel, nous avons appris :

* comment définir des fonctions, 
* comment passer des arguments à une fonction, 
* comment créer des fonctions avec des arguments par défaut et un nombre variable d'arguments, et
* comment créer une fonction avec une ou plusieurs valeurs de retour.

J'espère que vous avez tous apprécié la lecture de cet article. Merci de votre lecture. Comme toujours, à la prochaine ! 😀