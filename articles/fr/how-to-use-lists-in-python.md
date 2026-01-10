---
title: Comment utiliser les listes en Python – Expliqué avec des exemples de code
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-03-01T20:02:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-lists-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-2-.png
tags:
- name: Python
  slug: python
seo_title: Comment utiliser les listes en Python – Expliqué avec des exemples de code
seo_desc: "In Python, lists are a cornerstones of data organization and manipulation\
  \ – so I think they deserve a thorough exploration. \nThis article delves into how\
  \ to create and manipulate lists in Python, some advanced functionalities, and some\
  \ practical appl..."
---

En Python, les listes sont un pilier de l'organisation et de la manipulation des données – elles méritent donc une exploration approfondie.

Cet article examine comment créer et manipuler des listes en Python, certaines fonctionnalités avancées et quelques applications pratiques des listes.

Vous pouvez obtenir tout le code source à partir de [ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/python/python-list/main.py).

## Table des matières

* [Qu'est-ce qu'une liste en Python](#heading-quest-ce-quune-liste-en-python) ?
* [Comment créer une liste en Python](#heading-comment-creer-une-liste-en-python)
* [Comment accéder aux éléments d'une liste en Python](#heading-comment-acceder-aux-elements-dune-liste-en-python)
* [Opérations et méthodes de liste](#heading-operations-et-methodes-de-liste)
* [Concepts avancés de liste](#heading-concepts-avances-de-liste)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'une liste en Python ?

Imaginez que vous préparez une grande aventure, en remplissant votre sac à dos fidèle. Dans votre sac, vous avez différents compartiments où vous pouvez ranger vos affaires – certains compartiments pour les vêtements, d'autres pour les collations, et peut-être même une poche cachée pour vos trésors les plus précieux.

Maintenant, pensez aux listes Python comme votre sac à dos numérique. Une liste Python est comme un conteneur polyvalent, mais au lieu de compartiments, elle contient diverses informations appelées "éléments". Ces éléments peuvent être n'importe quoi : des nombres, des mots, même d'autres listes ! Tout comme votre sac à dos, vous pouvez réorganiser, ajouter, supprimer ou mettre à jour ces éléments selon vos besoins.

Par exemple, supposons que vous planifiez un voyage à l'épicerie. Vous pouvez créer une liste Python appelée `grocery_list` pour garder une trace de tous les articles que vous devez acheter. Chaque article, tel que "pommes", "bananes" ou "lait", est comme un élément de votre liste.

Voici à quoi pourrait ressembler une simple liste de courses en Python :

```python
liste_de_courses = ["pommes", "bananes", "lait"]
```

Une liste Python est une collection ordonnée, dynamique et mutable d'éléments enfermés dans des crochets `[]`.

Ces éléments, appelés articles ou valeurs, peuvent être de différents types de données – nombres, chaînes de caractères, booléens, et même d'autres listes (créant des structures imbriquées).

Avec cette liste, vous pouvez facilement vérifier ce que vous devez acheter, ajouter de nouveaux articles au fur et à mesure que vous vous en souvenez, ou supprimer des articles au fur et à mesure que vous les obtenez ou si vous changez d'avis.

La beauté des listes Python réside dans leur flexibilité et leur commodité. Que vous organisiez des données, gériez des tâches ou résolviez des problèmes complexes, les listes offrent un moyen puissant de stocker et de manipuler des informations dans vos programmes Python. Tout comme votre sac à dos fidèle vous aide à rester organisé lors de vos aventures, les listes Python aident à garder votre code propre et efficace.

## Comment créer une liste en Python

Créer des listes en Python est aussi polyvalent que d'organiser vos affaires dans différents compartiments de votre sac à dos. Selon ce que vous emballez, vous pourriez choisir d'arranger vos articles différemment pour une meilleure organisation et accessibilité.

### Liste sur une seule ligne

Pensez à cela comme à jeter vos collations préférées dans votre sac à dos pour un voyage rapide. Lorsque vous êtes pressé et que vous devez attraper vos essentiels rapidement, une liste sur une seule ligne est la solution. Elle est concise et efficace, parfaite lorsque vous avez une courte liste d'articles à retenir.

```python
fruits = ["pomme", "banane", "cerise"]

```

### Liste sur plusieurs lignes pour la lisibilité

Imaginez que vous faites vos bagages pour un long voyage et que vous voulez vous assurer que tout s'ajuste parfaitement dans votre sac à dos. Tout comme plier soigneusement vos vêtements pour maximiser l'espace, une liste sur plusieurs lignes assure la clarté et l'organisation, surtout pour les listes plus longues.

```python
nombres = [
    1,
    2,
    3,
    4,
    5,
]

```

### Liste de types de données mixtes

Parfois, vos aventures nécessitent d'emballer une variété d'articles – collations, gadgets, et peut-être même un bon livre. De même, une liste de types de données mixtes accueille différents types de données, vous permettant de stocker une gamme diversifiée d'informations dans une seule liste.

```python
liste_mixte = ["bonjour", 3.14, True]

```

En comprenant quand utiliser chaque type de liste, vous pouvez organiser vos données efficacement, rendant vos programmes Python plus faciles à lire et à maintenir. Tout comme faire vos bagages pour différents voyages, choisir le bon type de liste vous assure d'être bien préparé pour toute aventure de codage.

## Comment accéder aux éléments d'une liste en Python

Imaginez que vous avez une rangée de bocaux, chacun contenant un type différent de bonbons. Vous voulez prendre un bonbon spécifique dans l'un des bocaux. Comment faites-vous ? Vous regardez les étiquettes sur les bocaux pour trouver celui que vous voulez, n'est-ce pas ?

Dans les listes Python, chaque élément est comme un bonbon dans un bocal, et l'étiquette sur le bocal est similaire à ce que nous appelons un "index".

### Comment fonctionnent les indices

Un index est comme l'étiquette sur chaque bocal. Il nous indique la position d'un élément dans la liste. Mais voici le truc : en Python, nous commençons à compter à partir de 0, et non de 1. Ainsi, les éléments d'une liste Python sont étiquetés en commençant par 0, puis 1, 2, et ainsi de suite.

### Comment accéder aux éléments d'une liste

Pour prendre le bonbon d'un bocal spécifique, vous regardez l'étiquette et choisissez le bon. De même, pour obtenir un élément d'une liste, vous utilisez son index. Voici comment faire en Python :

```python
# Supposons que nous avons une liste de fruits
fruits = ["pomme", "banane", "cerise"]

# Pour accéder au premier fruit (pomme), qui est à l'index 0
premier_fruit = fruits[0]
print(premier_fruit)  # Sortie : pomme

# Pour accéder au deuxième fruit (banane), qui est à l'index 1
deuxieme_fruit = fruits[1]
print(deuxieme_fruit)  # Sortie : banane

```

En utilisant l'index à l'intérieur de crochets après le nom de la liste, Python nous aide à récupérer l'élément stocké à cette position.

Savoir comment accéder aux éléments d'une liste est super pratique ! C'est comme avoir une carte magique qui vous guide directement vers le bonbon que vous voulez.

Vous pouvez utiliser cette compétence chaque fois que vous devez travailler avec des morceaux spécifiques de données dans votre programme. Que vous comptiez des bonbons, gériez des scores dans un jeu, ou organisiez une liste de noms d'amis, comprendre comment accéder aux éléments par leurs indices est la clé pour débloquer tout le potentiel des listes Python.

## Opérations et méthodes de liste

### Comment modifier une liste

Contrairement aux chaînes de caractères, les listes sont mutables. Cela signifie que vous pouvez changer leur contenu après les avoir créées.

Imaginez que votre liste est comme un livre de recettes, où vous pouvez ajouter, supprimer ou réorganiser des ingrédients comme vous le souhaitez. Voici les méthodes clés pour modifier les listes :

#### Ajouter un élément

Ajoute un élément à la fin de la liste, comme ajouter un nouvel ingrédient à la fin de votre recette.

Voici la syntaxe : `nom_de_la_liste.append(élément)`

Et voici un exemple de code :

```python
fruits.append("orange")
# Explication : Nous ajoutons "orange" à la fin de la liste 'fruits'.
# Résultat : fruits sera maintenant ["pomme", "banane", "cerise", "orange"]

```

#### Insérer un élément

Insère un élément à un index spécifique, en décalant les éléments existants si nécessaire, similaire à l'ajout d'un nouvel ingrédient à une étape spécifique de votre recette.

Voici la syntaxe : `nom_de_la_liste.insert(index, élément)`

Et voici un exemple de code :

```python
fruits.insert(1, "raisin")
# Explication : Nous ajoutons "raisin" à l'index 1 dans la liste 'fruits', en décalant les autres éléments si nécessaire.
# Résultat : fruits sera maintenant ["pomme", "raisin", "banane", "cerise", "orange"]

```

#### Supprimer un élément

Supprime la première occurrence d'un élément spécifique, tout comme supprimer un ingrédient dont vous n'avez plus besoin de votre recette.

Voici la syntaxe : `nom_de_la_liste.remove(élément)`

Et voici un exemple de code :

```python
fruits.remove("banane")
# Explication : Nous supprimons la première occurrence de "banane" de la liste 'fruits'.
# Résultat : fruits sera maintenant ["pomme", "raisin", "cerise", "orange"]

```

#### Retirer un élément

Supprime et retourne l'élément à l'index donné, similaire à retirer un ingrédient d'une étape spécifique de votre recette.

Voici la syntaxe : `nom_de_la_liste.pop(index)`

Et voici un exemple de code :

```python
élément_supprimé = fruits.pop(1)
# Explication : Nous supprimons l'élément à l'index 1 ("raisin") de la liste 'fruits' et le stockons dans 'élément_supprimé'.
# Résultat : élément_supprimé sera "raisin", fruits sera maintenant ["pomme", "cerise", "orange"]

```

#### Étendre une liste

Étend la liste en ajoutant tous les éléments d'un itérable, comme ajouter plus d'ingrédients à votre recette à partir d'une autre recette.

Voici la syntaxe : `nom_de_la_liste.extend(itérable)`

Et voici un exemple de code :

```python
plus_de_fruits = ["mangue", "ananas"]
fruits.extend(plus_de_fruits)
# Explication : Nous ajoutons tous les fruits de 'plus_de_fruits' à la fin de la liste 'fruits'.
# Résultat : fruits sera maintenant ["pomme", "cerise", "orange", "mangue", "ananas"]

```

### Comment découper une liste

Découper une liste est comme couper un gâteau en tranches parfaitement dimensionnées. Tout comme vous choisissez où commencer à couper, où terminer, et quelle épaisseur chaque tranche doit avoir, découper une liste vous permet d'extraire des portions spécifiques de données de votre liste.

Imaginez que vous avez un délicieux gâteau, tout juste sorti du four. Vous êtes chargé de le couper en tranches pour vos invités. Voici comment découper une liste se rapporte à couper un gâteau :

#### Points de début et de fin

* **Index de début :** C'est là où vous commencez à couper le gâteau. Si vous commencez à la première couche du gâteau, vous pourriez commencer au bord même. Lorsque vous choisissez un index de début, vous pouvez en choisir n'importe quel - il n'a pas besoin d'être le premier.
* **Index de fin :** C'est là où vous arrêtez de couper le gâteau. Si vous arrêtez à la troisième couche, vous ne couperez pas au-delà de ce point.

#### Épaisseur de la tranche (Étape)

* Tout comme vous pouvez couper des tranches de gâteau plus épaisses ou plus fines, dans le découpage d'une liste, vous pouvez décider combien d'éléments inclure dans chaque tranche.

Voici la syntaxe pour découper :

```python
nom_de_la_liste[index_de_debut:index_de_fin:pas]

```

Et voici un exemple de code pour vous montrer comment cela fonctionne :

```python
# Supposons que nous avons une liste de couches de gâteau
couches_de_gateau = ["chocolat", "vanille", "fraise", "citron", "red velvet"]

# Découper les couches de gâteau
tranche_de_gateau = couches_de_gateau[1:4:2]
# Explication : Nous découpons 'couches_de_gateau' en commençant par l'index 1 (vanille) jusqu'à l'index 4 (citron),
#             et en sélectionnant chaque deuxième élément.
# Résultat : tranche_de_gateau sera ["vanille", "citron"]

```

* **Index de début 1 (vanille) :** C'est là où nous commençons à couper le gâteau.
* **Index de fin 4 (citron) :** Nous arrêtons de couper à cette couche, mais nous n'incluons pas le citron.
* **Pas de 2 :** Nous sautons chaque autre couche entre la vanille et le citron.
* **Résultat :** Nous obtenons une tranche contenant uniquement les couches de vanille et de citron.

En découpant des listes, vous pouvez extraire des sections spécifiques de données adaptées à vos besoins, tout comme couper des tranches de gâteau pour répondre aux préférences de vos invités.

#### Méthodes courantes de liste

##### Longueur

Retourne la longueur (nombre d'éléments) de la liste, similaire à compter le nombre d'ingrédients dans votre recette.

Voici la syntaxe : `len(nom_de_la_liste)`

Et voici un exemple de code :

```python
longueur = len(fruits)
# Explication : Nous trouvons le nombre d'éléments dans la liste 'fruits'.
# Résultat : longueur sera 5

```

##### Trier

Trie la liste en place, comme arranger vos ingrédients par ordre alphabétique dans votre recette.

Voici la syntaxe : `nom_de_la_liste.sort()`

Et voici un exemple de code :

```python
fruits.sort()
# Explication : Nous trions les éléments de 'fruits' par ordre croissant.
# Résultat : fruits sera maintenant ["pomme", "cerise", "mangue", "orange", "ananas"]

```

##### Trié

Retourne une nouvelle liste triée sans modifier la liste originale, similaire à faire une copie de votre recette avec les ingrédients arrangés différemment.

Voici la syntaxe : `sorted(nom_de_la_liste)`

Et voici un exemple de code :

```python
nombres_tries = sorted(nombres)
# Explication : Nous créons une nouvelle liste 'nombres_tries' avec les éléments de 'nombres' triés.
# Résultat : nombres_tries sera [1, 2, 3, 4, 5], 'nombres' reste inchangé

```

Le tri personnalisé dans les listes Python vous permet de trier les éléments en fonction de critères autres que leur ordre naturel. Cela est réalisé en utilisant le paramètre optionnel `key`, qui spécifie une fonction à appeler sur chaque élément avant le tri. Voici une explication :

#### Tri personnalisé et la fonction Key

Imaginez que vous avez une collection de fiches de recettes, chacune avec une liste d'ingrédients. Maintenant, au lieu de trier ces fiches de recettes par ordre alphabétique selon leurs titres, vous voulez les trier en fonction du nombre d'ingrédients que chaque recette nécessite. C'est là que le tri personnalisé avec la fonction key entre en jeu.

Voici la syntaxe pour faire cela :

```python
nom_de_la_liste.sort(key=fonction)
liste_triee = sorted(nom_de_la_liste, key=fonction)

```

Maintenant, regardons un exemple :

Supposons que nous avons une liste de fiches de recettes, où chaque fiche est un tuple contenant le nom de la recette et le nombre d'ingrédients requis :

```python
recettes = [("Tarte aux pommes", 9), ("Gâteau au chocolat", 7), ("Salade", 4), ("Crêpes", 6)]

```

Si nous voulons trier ces fiches de recettes en fonction du nombre d'ingrédients requis, nous pouvons utiliser une fonction de tri personnalisée :

```python
# Définir une fonction pour extraire le nombre d'ingrédients de chaque tuple de recette
def obtenir_nombre_ingrédients(recette):
    return recette[1]

# Trier les recettes en fonction du nombre d'ingrédients
recettes.sort(key=obtenir_nombre_ingrédients)

# Résultat : recettes sera [("Salade", 4), ("Crêpes", 6), ("Gâteau au chocolat", 7), ("Tarte aux pommes", 9)]

```

* Nous définissons une fonction `obtenir_nombre_ingrédients` qui prend un tuple de recette en entrée et retourne le deuxième élément du tuple (le nombre d'ingrédients).
* Nous utilisons ensuite cette fonction comme paramètre `key` dans la méthode `sort`. Python appellera cette fonction sur chaque tuple de recette et utilisera les valeurs retournées pour le tri.
* En conséquence, les recettes sont triées en fonction du nombre d'ingrédients requis, du plus petit au plus grand.

Le tri personnalisé avec la fonction key vous permet de trier les listes en fonction de critères complexes, tels que les attributs d'objets ou les valeurs calculées, vous offrant une plus grande flexibilité dans l'organisation de vos données.

##### Inverser

Inverse l'ordre des éléments en place, comme retourner votre recette à l'envers.

Voici la syntaxe : `nom_de_la_liste.reverse()`

Et voici un exemple :

```python
fruits.reverse()
# Explication : Nous inversons l'ordre des éléments dans la liste 'fruits'.
# Résultat : fruits sera maintenant ["ananas", "orange", "mangue", "cerise", "pomme"]

```

##### Index

Retourne le premier index d'un élément donné, similaire à trouver le numéro de page où un ingrédient est listé dans votre livre de recettes.

Voici la syntaxe : `nom_de_la_liste.index(élément)`

Et voici un exemple :

```python
index_de_cerise = fruits.index("cerise")
# Explication : Nous trouvons l'index de la première occurrence de "cerise" dans la liste 'fruits'.
# Résultat : index_de_cerise sera 3

```

##### Vérifier l'existence d'un élément

Vérifie si un élément existe dans la liste, comme vérifier si un ingrédient est listé dans votre recette.

Voici la syntaxe : `élément in nom_de_la_liste`

Et voici un exemple :

```python
est_pomme_présente = "pomme" in fruits
# Explication : Nous vérifions si "pomme" existe dans la liste 'fruits'.
# Résultat : est_pomme_présente sera True

```

##### Compter les occurrences

Retourne le nombre de fois qu'un élément spécifique apparaît dans la liste, similaire à compter combien de fois un ingrédient est utilisé dans votre recette.

Voici la syntaxe : `nom_de_la_liste.count(élément)`

Et voici un exemple :

```python
compte_de_orange = fruits.count("orange")
# Explication : Nous comptons le nombre de fois que "orange" apparaît dans la liste 'fruits'.
# Résultat : compte_de_orange sera 1

```

## Concepts avancés de liste

### Compréhension de liste

En ce qui concerne le travail avec les listes en Python, il existe un outil puissant à votre disposition appelé compréhension de liste. Cette syntaxe concise vous permet de générer des listes basées sur des itérables existants avec facilité, rendant votre code plus lisible et efficace.

La compréhension de liste offre un moyen concis de créer des listes en appliquant une expression à chaque élément d'un itérable existant, éventuellement avec des conditions de filtrage.

#### Exemple 1 : Générer les carrés des nombres

Dans une approche traditionnelle, vous pourriez initialiser une liste vide, parcourir une plage de nombres, calculer le carré de chaque nombre et l'ajouter à la liste. Avec la compréhension de liste, vous obtenez le même résultat en une seule ligne, en itérant sur la plage de nombres et en créant directement la liste des carrés.

```python
# Approche traditionnelle :
carrés = []
for x in range(5):
    carrés.append(x**2)

# Explication :
# Dans l'approche traditionnelle, nous initialisons une liste vide 'carrés'.
# Nous parcourons ensuite les nombres de 0 à 4 en utilisant la fonction range().
# Pour chaque nombre 'x', nous calculons son carré (x**2) et l'ajoutons à la liste 'carrés'.

# Compréhension de liste :
carrés = [x**2 for x in range(5)]

# Explication :
# Avec la compréhension de liste, nous obtenons le même résultat en une seule ligne.
# Nous utilisons une syntaxe compacte pour itérer sur les nombres de 0 à 4 et calculer leurs carrés directement,
# créant la liste 'carrés' en une seule fois.

```

#### Exemple 2 : Générer des nombres pairs

De même, lors de la génération d'une liste de nombres pairs, vous pouvez utiliser une syntaxe compacte avec la compréhension de liste pour itérer sur une plage de nombres et inclure uniquement ceux qui sont divisibles par 2, éliminant ainsi le besoin de déclarations conditionnelles supplémentaires.

```python
# Approche traditionnelle :
nombres_pairs = []
for x in range(10):
    if x % 2 == 0:
        nombres_pairs.append(x)

# Explication :
# Dans l'approche traditionnelle, nous initialisons une liste vide 'nombres_pairs'.
# Nous parcourons ensuite les nombres de 0 à 9 en utilisant la fonction range().
# Pour chaque nombre 'x', nous vérifions s'il est pair (divisible par 2), et si c'est le cas, nous l'ajoutons à la liste 'nombres_pairs'.

# Compréhension de liste :
nombres_pairs = [x for x in range(10) if x % 2 == 0]

# Explication :
# Avec la compréhension de liste, nous obtenons le même résultat de manière plus concise.
# Nous utilisons une syntaxe compacte pour itérer sur les nombres de 0 à 9 et inclure uniquement ceux qui sont pairs,
# créant directement la liste 'nombres_pairs' en une seule ligne.

```

#### Exemple 3 : Générer une liste de chaînes de caractères

La compréhension de liste n'est pas limitée aux opérations numériques. Vous pouvez également l'appliquer pour manipuler des chaînes de caractères. Par exemple, convertir une liste de noms en majuscules peut être réalisé en une seule ligne, rendant votre code plus concis et lisible.

```python
# Approche traditionnelle :
noms = ['Alice', 'Bob', 'Charlie']
noms_majuscules = []
for nom in noms:
    noms_majuscules.append(nom.upper())

# Explication :
# Dans l'approche traditionnelle, nous initialisons une liste vide 'noms_majuscules'.
# Nous parcourons ensuite chaque nom dans la liste 'noms'.
# Pour chaque nom, nous le convertissons en majuscules en utilisant la méthode upper() et ajoutons le résultat à 'noms_majuscules'.

# Compréhension de liste :
noms_majuscules = [nom.upper() for nom in noms]

# Explication :
# Avec la compréhension de liste, nous obtenons le même résultat de manière plus succincte.
# Nous utilisons une syntaxe compacte pour itérer sur chaque nom dans la liste 'noms',
# en appliquant la méthode upper() pour convertir chaque nom en majuscules,
# créant directement la liste 'noms_majuscules' en une seule ligne.

```

#### Exemple 4 : Générer une liste de tuples

Les boucles imbriquées sont couramment utilisées pour générer des combinaisons d'éléments, telles que des paires de nombres. Avec la compréhension de liste, vous pouvez rationaliser ce processus en utilisant des boucles imbriquées directement dans la syntaxe de compréhension, créant des tuples de combinaisons sans effort.

```python
# Approche traditionnelle :
paires = []
for x in range(3):
    for y in range(2):
        paires.append((x, y))

# Explication :
# Dans l'approche traditionnelle, nous initialisons une liste vide 'paires'.
# Nous utilisons ensuite des boucles imbriquées pour itérer sur chaque combinaison possible de valeurs x et y.
# Pour chaque combinaison, nous créons un tuple (x, y) et l'ajoutons à la liste 'paires'.

# Compréhension de liste :
paires = [(x, y) for x in range(3) for y in range(2)]

# Explication :
# Avec la compréhension de liste, nous obtenons le même résultat de manière plus compacte.
# Nous utilisons une syntaxe compacte avec des boucles imbriquées pour itérer sur chaque combinaison possible de valeurs x et y,
# créant directement la liste 'paires' contenant des tuples en une seule ligne.

```

#### Exemple 5 : Générer une liste de combinaisons

La compréhension de liste permet également d'inclure des expressions conditionnelles, vous permettant de filtrer certaines combinaisons en fonction de critères spécifiques. Cette flexibilité en fait un outil polyvalent pour diverses tâches de génération de listes.

```python
# Approche traditionnelle :
combinaisons = []
for x in range(1, 4):
    for y in range(1, 4):
        if x != y:
            combinaisons.append((x, y))

# Explication :
# Dans l'approche traditionnelle, nous initialisons une liste vide 'combinaisons'.
# Nous utilisons ensuite des boucles imbriquées pour itérer sur chaque combinaison possible de valeurs x et y.
# Pour chaque combinaison où x n'est pas égal à y, nous créons un tuple (x, y) et l'ajoutons à la liste 'combinaisons'.

# Compréhension de liste :
combinaisons = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]

# Explication :
# Avec la compréhension de liste, nous obtenons le même résultat de manière plus succincte.
# Nous utilisons une syntaxe compacte avec des boucles imbriquées et une expression conditionnelle pour itérer sur chaque combinaison possible de valeurs x et y,
# en incluant uniquement celles où x n'est pas égal à y,
# créant directement la liste 'combinaisons' contenant des tuples en une seule ligne.

```

### Listes imbriquées

Les listes en Python peuvent contenir d'autres listes, créant ainsi des structures multidimensionnelles. Cette fonctionnalité est utile pour représenter des matrices, des tableaux ou des structures de données hiérarchiques. Explorons comment travailler avec des listes imbriquées :

#### Comment créer une liste imbriquée

```python
liste_imbriquée = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

```

Dans cet exemple, nous définissons une liste imbriquée `liste_imbriquée` contenant trois listes internes, chacune représentant une ligne dans une matrice.

#### Comment accéder aux éléments dans les listes imbriquées

Pour accéder aux éléments dans une liste imbriquée, vous utilisez plusieurs indices, chaque indice représentant la position de l'élément dans la liste interne respective. Par exemple :

```python
print(liste_imbriquée[0][1])  # Sortie : 2

```

Ce code accède à l'élément à la ligne 0 et à la colonne 1 de la liste imbriquée, donnant la valeur `2`.

#### Comment itérer sur les listes imbriquées

Vous pouvez itérer sur une liste imbriquée en utilisant des boucles imbriquées, avec une boucle externe itérant sur chaque liste interne et une boucle interne itérant sur chaque élément dans cette liste interne. Par exemple :

```python
for sous_liste in liste_imbriquée:
    for élément in sous_liste:
        print(élément)

```

Ce code itère sur chaque sous-liste dans la `liste_imbriquée` puis itère sur chaque élément dans cette sous-liste, imprimant chaque élément individuellement.

##### Exemple 1 : Somme des éléments dans une liste imbriquée

```python
somme_totale = 0
for sous_liste in liste_imbriquée:
    for élément in sous_liste:
        somme_totale += élément
print("Somme totale :", somme_totale)

```

Dans cet exemple, nous itérons sur chaque sous-liste et chaque élément dans la sous-liste, en additionnant tous les éléments de la liste imbriquée.

##### Exemple 2 : Trouver la valeur maximale dans une liste imbriquée

```python
valeur_max = float('-inf')  # Initialiser avec moins l'infini
for sous_liste in liste_imbriquée:
    for élément in sous_liste:
        if élément > valeur_max:
            valeur_max = élément
print("Valeur maximale :", valeur_max)

```

Dans cet exemple, nous trouvons la valeur maximale dans la liste imbriquée en itérant sur chaque sous-liste et chaque élément dans la sous-liste, en mettant à jour la variable `valeur_max` si une valeur plus grande est rencontrée.

## Conclusion

Dans cet article, nous avons exploré les aspects fondamentaux, les opérations et les fonctionnalités avancées des listes Python. Vous devriez maintenant avoir une base solide pour tirer parti de cette structure de données polyvalente de manière efficace dans divers scénarios de programmation.

Si vous avez des commentaires, envoyez-moi un message direct sur [Twitter](https://twitter.com/introvertedbot) ou [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).