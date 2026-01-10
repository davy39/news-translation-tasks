---
title: Apprendre la programmation Python – Tout ce que vous devez savoir (Livre gratuit)
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2022-10-27T16:38:20.000Z'
originalURL: https://freecodecamp.org/news/learn-python-book
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-christina-morillo-1181359--4-.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: book
  slug: book
- name: Python
  slug: python
seo_title: Apprendre la programmation Python – Tout ce que vous devez savoir (Livre
  gratuit)
seo_desc: 'Python is one of the most popular programming languages in the world today.
  It was created in 1991 by Guido van Rossum.

  According to van Rossum, Python is a:


  “high-level programming language, and its core design philosophy is all about code
  readabil...'
---

Python est l'un des langages de programmation les plus populaires au monde aujourd'hui. Il a été créé en 1991 par Guido van Rossum.

Selon van Rossum, Python est un :

> « langage de programmation de haut niveau, et sa philosophie de conception principale est centrée sur la lisibilité du code et une syntaxe qui permet aux programmeurs d'exprimer des concepts en quelques lignes de code. »

## Avantages d'apprendre Python

Python est l'un des langages les plus faciles que vous pouvez apprendre et utiliser. Vous pouvez l'utiliser pour le développement de logiciels, le côté serveur du développement web, l'apprentissage automatique, les mathématiques, et tout type de script auquel vous pouvez penser.

Le bon côté de Python est qu'il est largement utilisé et accepté par de nombreuses entreprises et institutions académiques. Cela en fait un très bon choix, surtout si vous commencez tout juste votre parcours en codage.

Python dispose également d'une grande communauté de développeurs qui l'utilisent et sont prêts à vous aider si vous êtes bloqué ou avez des questions. Cette communauté a déjà publié de nombreuses bibliothèques open source que vous pouvez commencer à utiliser. Ils les améliorent également activement.

La syntaxe de Python est assez similaire à celle de la langue anglaise, ce qui la rend plus facile à comprendre et à utiliser de manière assez intuitive.

Python fonctionne sur un système d'interpréteur, ce qui signifie que vous n'avez pas à attendre qu'un compilateur compile le code et puis l'exécute. Vous pouvez plutôt construire des prototypes rapidement.

Il fonctionne également sur différentes plateformes, telles que Windows, Linux, Mac, Raspberry Pi, et ainsi de suite.

Vous voyez donc – c'est un excellent langage de programmation, que vous débutiez ou que vous cherchiez à ajouter un autre outil utile à votre kit.

Voici ce que nous allons couvrir dans ce livre :

## Table des matières

* [Bases de Python](#heading-installation)

* [Opérateurs en Python](#heading-operateurs-en-python)

* [Types de données en Python](#heading-types-de-donnees-en-python)

* [Tuples en Python](#heading-tuples-en-python)

* [Dictionnaires en Python](#heading-dictionnaires-en-python-structures-de-donnees-cle-valeur)

* [Ensembles en Python](#heading-ensembles-en-python)

* [Conversions de types en Python](#heading-conversions-de-types-en-python)

* [Contrôle de flux en Python](#heading-controle-de-flux-en-python)

* [Fonctions en Python](#heading-fonctions-en-python)

* [Programmation orientée objet en Python](#heading-programmation-orientee-objet-en-python)

* [Importation en Python](#heading-importation-en-python)

* [Comment gérer les exceptions en Python](#heading-comment-gerer-les-exceptions-en-python)

* [Saisie utilisateur en Python](#heading-saisie-utilisateur-en-python)

* [Obtenez la version PDF du livre](#heading-obtenez-le-livre-en-pdf)

# Bases de Python

## Indentation en Python

Comparé à d'autres langages, Python accorde une importance spéciale à l'indentation.

Dans d'autres langages de programmation, les espaces blancs et les indentations ne sont utilisés que pour rendre le code plus lisible et plus joli. Mais en Python, ils représentent un sous-bloc de code.

Le code suivant ne va pas fonctionner, car la deuxième ligne n'est pas correctement indentée :

```python
if 100 > 10:
  print("100 est plus grand que 10")
```

Pour qu'il fonctionne correctement, l'indentation doit ressembler à ce qui suit :

```python
if 100 > 10:
    print("100 est plus grand que 10")
```

Cela peut sembler difficile à comprendre, mais vous pouvez utiliser un éditeur de code qui met en évidence de telles erreurs de syntaxe de manière assez vivante. De plus, plus vous écrivez de code Python, plus il devient facile pour vous de considérer de telles indentations comme une seconde nature.

Python utilise quatre espaces pour une indentation correcte par défaut.

## Commentaires en Python

Nous utilisons les commentaires pour spécifier des parties du programme qui doivent être simplement ignorées et non exécutées par l'interpréteur Python. Cela signifie que tout ce qui est écrit à l'intérieur d'un commentaire n'est pas pris en compte du tout et vous pouvez écrire dans n'importe quelle langue que vous voulez, y compris votre propre langue maternelle.

En Python, vous commencez un commentaire avec le symbole *#* devant la ligne :

```python
# Ceci est un commentaire en Python
```

Vous pouvez également inclure des commentaires plus étendus sur plusieurs lignes en utilisant des guillemets triples :

```python
"""
Ceci est un commentaire en Python.
Ici, nous tapons dans une autre ligne et nous sommes toujours dans le même bloc de commentaire.

Dans la ligne précédente, nous avons un espace, car il est permis d'avoir des espaces à l'intérieur des commentaires.

Terminons ce commentaire ici.
"""
```

## Méthode print() en Python

Nous allons utiliser la méthode `print()` car elle nous aide à voir les résultats dans la console.

Vous n'avez pas besoin de savoir comment elle fonctionne en coulisses ou même savoir ce qu'est une méthode pour l'instant. Considérez-la simplement comme un moyen pour nous d'afficher les résultats de notre code dans la console.

# Opérateurs en Python

## Opérateurs arithmétiques en Python

Même si vous pouvez simplement sortir votre téléphone de votre poche et faire quelques calculs, vous devriez également vous habituer à implémenter quelques opérateurs arithmétiques en Python.

Lorsque nous voulons ajouter deux nombres, nous utilisons le signe plus, comme en mathématiques :

```python
print(50 + 4)  # 54
```

De même, pour la soustraction, nous utilisons le signe moins :

```python
print(50 - 4)  # 46
```

Pour la multiplication, nous utilisons l'étoile ou l'astérisque :

```python
print(50 * 4)  # 200
```

Lorsque nous faisons des divisions, nous utilisons le signe de la barre oblique :

```python
print(50 / 4)  # 12.5
print(8 / 4)  # 2.0
```

Cela donne des nombres à virgule flottante. Si nous voulons obtenir uniquement le nombre entier lors de la division (également connu sous le nom de division entière), nous devons utiliser le double signe de fraction :

```python
print(50 // 4)  # 12
print(8 / 4)  # 2
```

Nous pouvons également trouver le reste d'un nombre divisé par un autre nombre en utilisant le signe de pourcentage `%`.

```python
print(50 % 4)  # 2
```

Cette opération peut être utile, notamment dans les cas où nous voulons vérifier si un nombre est impair ou pair. Un nombre est impair si, lorsqu'il est divisé par 2, le reste est 1. Sinon, il est pair.

Voici une illustration :

```python
print(50 % 2)  # 0
# Puisque le reste est 0, ce nombre est pair

print(51 % 2)  # 1
# Puisque le reste est 1, ce nombre est impair
```

Lorsque nous voulons élever un nombre à une puissance spécifique, nous devons utiliser le double signe étoile :

```python
print(2 ** 3)  # 8
# C'est une façon abrégée d'écrire 2 * 2 * 2

print(5 ** 4)  # 625
# C'est une façon abrégée d'écrire 5 * 5 * 5 * 5
```

## Opérateurs d'affectation en Python

Vous utilisez ces opérateurs pour affecter des valeurs aux variables.

Lorsque nous déclarons une variable, nous utilisons le signe égal :

```python
nom = "Fatos"
age = 28
```

Nous pouvons également déclarer plusieurs variables sur la même ligne :

```python
nom, age, lieu = "Fatos", 28, "Europe"
```

Nous pouvons utiliser cela comme un moyen d'échanger également des valeurs entre des variables. Par exemple, supposons que nous avons deux variables `a` et `b` et que nous voulons échanger leurs valeurs.

Une façon logique de faire cela serait d'introduire une troisième variable qui sert de variable temporaire :

```python
a, b = 1, 2

print(a)  # 1
print(b)  # 2

c = a
a = b
b = c

print(a)  # 2
print(b)  # 1
```

Nous pouvons faire cela en une seule ligne de la manière suivante :

```python
a, b = 1, 2

print(a)  # 1
print(b)  # 2

b, a = a, b

print(a)  # 2
print(b)  # 1
```

Nous pouvons également fusionner les opérateurs d'affectation avec les opérateurs arithmétiques.

Voyons comment nous pouvons faire cela pour l'addition d'abord.

Supposons que nous avons les variables suivantes :

```python
somme_totale = 20

somme_actuelle = 10
```

Maintenant, nous voulons ajouter la valeur de `somme_actuelle` à `somme_totale`. Pour cela, nous devons écrire ce qui suit :

```python
somme_totale = somme_totale + somme_actuelle

print(somme_totale)  # 30
```

Cela peut ne pas sembler exact, puisque le côté droit n'est pas égal au côté gauche. Cependant, dans ce cas, nous faisons simplement une affectation et non une comparaison des deux côtés de l'équation.

Pour faire cela rapidement, nous pouvons utiliser la forme suivante :

```python
somme_totale += somme_actuelle

print(somme_totale)  # 30
```

Cela est équivalent à l'instruction précédente.

De même, nous pouvons faire de même avec d'autres opérateurs arithmétiques :

Soustraction :

```python
resultat = 3
nombre = 4

resultat -= nombre  # Cela est égal à resultat = resultat - nombre

print(resultat)  # -1
```

Multiplication :

```python
produit = 3
nombre = 4

produit *= nombre  # Cela est égal à produit = produit * nombre

print(produit)  # 12
```

Division :

```python
resultat = 8
nombre = 4

resultat /= nombre  # Cela est égal à resultat = resultat / nombre

print(resultat)  # 2.0
```

Opérateur modulo :

```python
resultat = 8
nombre = 4

resultat %= nombre  # Cela est égal à resultat = resultat % nombre

print(resultat)  # 0
```

Opérateur de puissance :

```python
resultat = 2
nombre = 4

resultat **= nombre  # Cela est égal à resultat = resultat ** nombre

print(resultat)  # 16
```

## Opérateurs de comparaison en Python

Vous avez probablement appris à faire des comparaisons de base de nombres à l'école, comme vérifier si un nombre spécifique est plus grand qu'un autre nombre, ou s'ils sont égaux.

Nous pouvons utiliser presque les mêmes opérateurs en Python pour faire de telles comparaisons.

Voyons-les en action.

### Opérateurs d'égalité

Vous pouvez vérifier si deux nombres sont égaux en utilisant l'opérateur `==` :

```python
print(2 == 3)  # False
```

La dernière expression évalue à False puisque `2` n'est pas égal à `3`.

Il y a un autre opérateur que vous pouvez utiliser pour vérifier si 2 nombres ne sont pas égaux. C'est un opérateur que vous n'avez peut-être pas vu dans vos cours de mathématiques écrit exactement de cette manière. C'est l'opérateur `!=`.

Faisons une comparaison pour voir si `2` n'est pas égal à `3` :

```python
print(2 != 3)  # True
```

Cette expression évalue à True puisque `2` n'est effectivement pas égal à `3`.

### Opérateurs d'inégalité

Maintenant, nous allons voir comment vérifier si un nombre est plus grand qu'un autre nombre :

```python
print(2 > 3)  # False
```

C'est quelque chose que vous devriez déjà savoir de vos cours de mathématiques.

Lorsque vous essayez de vérifier si un nombre est supérieur ou égal à un autre nombre, nous devons utiliser cet opérateur `>=` :

```python
print(2 >= 3)  # False
```

De même, pour vérifier si un nombre est inférieur ou égal à un autre, nous avons :

```python
print(2 < 3)  # True
print(2 <= 3)  # True
```

### Opérateurs logiques

En mathématiques au lycée, vous avez peut-être appris les opérateurs logiques tels que `and` et `or`.

En bref, pour qu'une expression évalue à True lorsque vous utilisez `and`, les deux déclarations doivent être vraies. En Python, nous l'implémentons en utilisant `and` :

```python
print(5 > 0 and 3 < 5)  # True
```

Cet exemple va évaluer à True puisque `5` est supérieur à `0`, ce qui évalue à True, et `3` est inférieur à `5`, ce qui évalue également à True. De cela, nous obtenons True et True, ce qui évalue à True.

Prenons un exemple où une expression `and` va évaluer à `False` :

```python
print(2 > 5 and 0 > -1)  # False
```

`2` n'est pas supérieur à `5`, donc la déclaration du côté gauche va évaluer à False. Peu importe ce qu'il y a du côté droit, nous allons obtenir l'expression entière égale à `False`, puisque False et toute autre valeur (comme True) vont aboutir à False.

Lorsque vous avez des déclarations où au moins l'une d'entre elles doit évaluer à True, alors nous devons utiliser l'opérateur `or` :

```python
print(2 > 5 or 0 > -1)  # True
```

Cela va évaluer à True puisque la déclaration du côté droit évalue à True – donc au moins l'une d'entre elles est vraie.

Si les deux déclarations sont False, alors `or` aboutit à `False` à la fin :

```python
print(2 < 0 or 0 > 1)  # False
```

Cela est False puisque 0 n'est pas supérieur à 2 et aussi 0 n'est pas supérieur à 1. Donc l'expression entière est False.

# Types de données en Python

## Variables en Python

Vous pouvez penser aux variables comme les éléments de base de tout programme informatique que vous pourriez écrire.

Vous pouvez utiliser des variables pour stocker des valeurs et ensuite les réutiliser autant de fois que vous le souhaitez. Le moment où vous voulez changer une valeur, vous pouvez simplement la changer à un seul endroit et cette nouvelle valeur que vous venez de changer va être reflétée partout ailleurs où cette variable est utilisée.

Chaque variable en Python est un objet.

Une variable est créée au moment où elle est initialisée avec une valeur.

Voici les règles générales pour les variables Python :

* Un nom de variable doit commencer par une lettre ou le caractère de soulignement. Il ne peut pas commencer par un nombre.

* Un nom de variable ne peut contenir que des caractères alphanumériques et des soulignements (A-z, 0-9, et \_ ).

* Les noms de variables sont sensibles à la casse, ce qui signifie que `height`, `Height`, et `HEIGHT` sont toutes des variables différentes.

Définissons notre première variable :

```python
age = 28
```

Dans cet exemple, nous initialisons une variable avec le nom *age* et lui attribuons la valeur 28.

Nous pouvons définir d'autres variables avec elle, comme :

```python
age = 28
salaire = 10000
```

Nous pouvons utiliser à peu près n'importe quel nom que nous voulons, mais il est préférable d'utiliser des noms que vous et vos collègues qui travaillent avec vous pouvez comprendre.

Nous avons d'autres types de variables en Python, tels que les nombres à virgule flottante, les chaînes de caractères et les valeurs booléennes. Nous pouvons même créer nos propres types personnalisés.

Voyons un exemple de variable qui contient un nombre à virgule flottante :

```python
taille = 3.5
```

Comme vous pouvez le voir, cette initialisation est assez similaire à celles où nous avions des nombres entiers. Ici, nous changeons simplement la valeur à droite. L'interpréteur Python est assez intelligent pour savoir que nous traitons avec un autre type de variable, à savoir un type de variable à virgule flottante.

Voyons un exemple de chaîne de caractères :

```python
lecteur = "Fatos"
```

Nous plaçons les valeurs de chaîne soit entre guillemets doubles, soit entre guillemets simples pour spécifier la valeur que nous voulons stocker dans les variables de chaîne.

Lorsque nous voulons stocker des valeurs booléennes, nous devons utiliser des mots réservés, à savoir, *True* et *False*.

```python
texte_visible = False
```

Nous pouvons également avoir une valeur booléenne stockée lorsque nous avons des expressions qui résultent en une valeur booléenne, par exemple, lorsque nous comparons un nombre avec un autre nombre, comme :

```python
est_plus_grand = 5 > 6
```

Cette variable va être initialisée avec la valeur *False* puisque 5 est inférieur à 6.

## Nombres en Python

Nous avons trois types numériques en Python : les entiers, les flottants et les nombres complexes.

### Entiers

Les entiers représentent des nombres entiers qui peuvent être à la fois positifs et négatifs et ne contiennent aucune partie décimale.

Voici quelques exemples d'entiers : `1`, `3000`, `-31234`, et ainsi de suite.

Lorsque nous additionnons, soustrayons ou multiplions deux entiers, nous obtenons un entier comme résultat à la fin.

```python
print(3 + 5)  # 8
print(3 - 5)  # -2
print(3 * 5)  # 15
```

Ce sont tous des entiers.

Cela inclut également les cas où nous élevons un nombre à une puissance :

```python
resultat = 3 ** 4  # Cela est similaire à multiplier 3 * 3 * 3 * 3 dans lequel cas, nous multiplions des entiers ensemble
print(resultat)  # 81
```

Lorsque nous voulons diviser deux entiers, nous allons obtenir un nombre à virgule flottante.

### Booléens

Le type booléen représente les valeurs de vérité, True et False. Vous avez appris l'explication de ce type dans la section *Nombres*, puisque les booléens sont effectivement des sous-types du type entier.

Plus spécifiquement, presque toujours une valeur False peut être considérée comme un `0`, tandis qu'une valeur True peut être considérée comme un `1`.

Ainsi, nous pouvons également effectuer des opérations arithmétiques avec eux :

```python
print(True * 5)  # 5
print(False * 500)  # 0, puisque False est égal à 0
```

L'exception pour ces représentations entières des valeurs booléennes est lorsque ces valeurs sont des chaînes de caractères telles que "False" et "True".

### Flottants

Les nombres à virgule flottante sont des nombres qui contiennent la partie décimale, tels que `-3.14`, `12.031`, `9.3124`, et ainsi de suite.

Nous pouvons également convertir en nombres à virgule flottante en utilisant la fonction `float()` :

```python
dix = float(10)

print(dix)  # 10.0
```

Lorsque nous additionnons, soustrayons ou divisons deux nombres à virgule flottante, ou un nombre à virgule flottante et un entier, nous obtenons un nombre à virgule flottante comme résultat à la fin :

```python
print(3.4 * 2)  # 6.8
print(3.4 + 2)  # 5.4
print(3.4 - 2)  # 1.4
print(2.1 * 3.4)  # 7.14
```

### Nombres complexes

Les nombres complexes ont à la fois la partie réelle et la partie *imaginaire* que nous écrivons de la manière suivante :

```python
nombre_complexe = 1 + 5j

print(nombre_complexe)  # (1+5j)
```

## Chaînes de caractères en Python

Les chaînes de caractères représentent des caractères qui sont enfermés entre guillemets simples ou doubles. Les deux sont traités de la même manière :

```python
nom = "Fatos"  # Guillemets doubles

nom = 'Fatos'  # Guillemets simples
```

Si nous voulons inclure une citation à l'intérieur d'une chaîne de caractères, nous devons indiquer à Python qu'il ne doit pas fermer la chaîne mais simplement échapper cette citation :

```python
salutation = 'Bonjour. Je\'m bien.'  # Nous avons échappé l'apostrophe dans Je'm.

salutation_guillemets_doubles = "Bonjour. Je'm bien."  # Lorsque nous utilisons des guillemets doubles, nous n'avons pas besoin d'échapper l'apostrophe
```

Lorsque nous voulons inclure une nouvelle ligne dans une chaîne de caractères, nous pouvons inclure le caractère spécial `\n` :

```python
ma_chaine = "Je veux continuer \n à la ligne suivante"

print(ma_chaine) 
# Je veux continuer 
# à la ligne suivante
```

Puisque les chaînes de caractères sont des tableaux de caractères, nous pouvons indexer des caractères spécifiques en utilisant des index. Les index commencent à 0 et vont jusqu'à la longueur de la chaîne moins 1.

Nous excluons l'index qui est égal à la longueur de la chaîne puisque nous commençons l'indexation à partir de 0 et non de 1.

Voici un exemple :

```python
chaine = "Mot"
```

Dans cet exemple, si nous devions sélectionner des caractères individuels de la chaîne, ils se dérouleraient comme suit :

```python
chaine = "Mot"

print(chaine[0])  # M
print(chaine[1])  # o
print(chaine[2])  # t
```

Nous pouvons utiliser des index négatifs également, ce qui signifie que nous commençons par la fin de la chaîne avec `-1`. Nous ne pouvons pas utiliser `0` pour indexer à partir de la fin d'une chaîne, puisque `-0 = 0` :

```python
print(chaine[-1])  # t
print(chaine[-2])  # o
print(chaine[-3])  # M
```

Nous pouvons également faire du découpage et inclure seulement une portion de la chaîne et non la chaîne entière. Par exemple, si nous voulons obtenir des caractères qui commencent à un index spécifique jusqu'à un index spécifique, nous devons l'écrire de la manière suivante : `chaine[index_debut:index_fin]`, en excluant le caractère à l'index `index_fin` :

```python
chaine = "Mot"

print(chaine[0:3])  # Mot
```

Si nous voulons commencer à partir d'un index spécifique et continuer à obtenir tous les caractères restants de la chaîne jusqu'à la fin, nous pouvons omettre de spécifier l'index de fin, comme suit :

```python
chaine = "Mot"

print(chaine[2:])  # ot
```

Si nous voulons commencer à partir de 0 et aller jusqu'à un index spécifique, nous pouvons simplement spécifier l'index de fin :

```python
chaine = "Mot"

print(chaine[:2])  # Mo
```

Cela signifie que la valeur de `chaine` est égale à `chaine[:2]` (en excluant le caractère à la position 2) + `chaine[2:]`.

Notez que les chaînes de caractères en Python sont immuables. Cela signifie qu'une fois qu'un objet chaîne a été créé, il ne peut pas être modifié, comme essayer de changer un caractère dans une chaîne.

À titre d'illustration, supposons que nous voulons changer le premier caractère de la chaîne, à savoir remplacer `M` par `A` de la manière suivante :

```python
chaine = "Mot"
chaine[0] = "A"
```

Maintenant, si nous essayons d'imprimer `chaine`, nous obtiendrons une erreur comme suit :

```python
# TypeError: l'objet 'str' ne supporte pas l'affectation d'élément
```

Si nous avons besoin d'une nouvelle chaîne, nous devons simplement en créer une nouvelle.

### Opérateurs de chaîne

Nous pouvons concaténer des chaînes en utilisant l'opérateur `+` :

```python
premier = "Premier"
deuxieme = "Deuxieme"

version_concatenee = premier + " " + deuxieme

print(version_concatenee)  # Premier Deuxieme
```

Nous pouvons utiliser l'opérateur de multiplication `*` avec des chaînes et des nombres.

Vous pouvez utiliser cela pour répéter la chaîne autant de fois. Par exemple, si nous voulons répéter une chaîne 5 fois, mais que nous ne voulons pas l'écrire manuellement cinq fois, nous pouvons simplement la multiplier par le nombre 5 :

```python
chaine = "Abc"

version_repetee = chaine * 5

print(version_repetee)  # AbcAbcAbcAbcAbc
```

### Méthodes intégrées des chaînes

Il existe quelques méthodes intégrées des chaînes que nous pouvons utiliser et qui peuvent nous faciliter la manipulation de celles-ci.

#### Méthode `len()`

`len()` est une méthode que nous pouvons utiliser pour obtenir la longueur d'une chaîne :

```python
phrase = "Je vais bien."

print(len(phrase))  # 12
```

#### Méthode `replace()`

Nous pouvons utiliser `replace()` pour remplacer un caractère ou une sous-chaîne d'une chaîne par un autre caractère ou une autre sous-chaîne :

```python
chaine = "Abc"

version_modifiee = chaine.replace("A", "Z")

print(version_modifiee)  # Zbc
```

#### Méthode `strip()`

`strip()` supprime les espaces blancs qui peuvent se trouver au début ou à la fin d'une chaîne :

```python
chaine = " Salut "

print(chaine.strip())  # Salut
```

#### Méthode `split()`

Nous pouvons utiliser `split()` pour convertir une chaîne en un tableau de sous-chaînes basé sur un motif spécifique qui est mentionné comme séparateur.

Par exemple, supposons que nous voulons enregistrer tous les mots d'une phrase dans un tableau de mots. Ces mots sont séparés par des espaces blancs, donc nous devons faire la division basée sur cela :

```python
phrase = "Ceci est une phrase qui est déclarée ici"

print(phrase.split(" ")) 
# ['Ceci', 'est', 'une', 'phrase', 'qui', 'est', 'déclarée', 'ici']
```

#### Méthode `join()`

`join()` est l'inverse de `split()` : à partir d'un tableau de chaînes, il retourne une chaîne. Le processus de concaténation est supposé se faire avec un séparateur spécifié entre chaque élément du tableau qui, à la fin, résulte en une seule chaîne concaténée :

```python
mots = ["chat", "chien", "lapin"]

print(" - ".join(mots))  # chat - chien - lapin
```

#### Méthode `count()`

Nous pouvons utiliser `count()` pour compter le nombre de fois qu'un caractère ou une sous-chaîne apparaît dans une chaîne :

```python
chaine = "Salut"
 
print(chaine.count("h"))  # 1, puisque c'est sensible à la casse et 'h' n'est pas égal à 'H'

print(chaine.count("e"))  # 2

print(chaine.count("Hi"))  # 1

print(chaine.count("Salut"))  # 1
```

#### Méthode `find()`

`find()` nous permet de trouver un caractère ou une sous-chaîne dans une chaîne et retourne l'index de celui-ci. Dans le cas où il ne le trouve pas, il retournera simplement `-1` :

```python
chaine = "Salut"

print(chaine.find("3"))  # -1

print(chaine.find("e"))  # 5

print(chaine.find("Hi"))  # 0

print(chaine.find("Salut"))  # 0
```

#### `lower()`

`lower()` convertit tous les caractères d'une chaîne en minuscules :

```python
chaine = "Salut"

print(chaine.lower())  # salut
```

#### `upper()`

`upper()` convertit tous les caractères d'une chaîne en majuscules :

```python
chaine = "Salut"

print(chaine.upper())  # SALUT
```

#### Méthode `capitalize()`

Nous pouvons utiliser `capitalize()` pour convertir le premier caractère d'une chaîne en majuscule :

```python
chaine = "salut"

print(chaine.capitalize())  # Salut
```

#### Méthode `title()`

`title()` convertit les caractères de début de chaque mot (séquences séparées par des espaces blancs) d'une chaîne en majuscules :

```python
chaine = "salut"

print(chaine.title())  # Salut
```

#### Méthode `isupper()`

`isupper()` est une méthode que nous pouvons utiliser pour vérifier si tous les caractères d'une chaîne sont en majuscules :

```python
chaine = "êtes-vous ICI"
une_autre_chaine = "OUI"

print(chaine.isupper())  # False
print(une_autre_chaine.isupper())  # True
```

#### Méthode `islower()`

`islower()` vérifie de manière similaire si tous les caractères sont en minuscules :

```python
chaine = "êtes-vous ICI"
une_autre_chaine = "non"

print(chaine.islower())  # False
print(une_autre_chaine.islower())  # True
```

#### Méthode `isalpha()`

`isalpha()` retourne True si tous les caractères d'une chaîne sont des lettres de l'alphabet :

```python
chaine = "A1"
une_autre_chaine = "aA"

print(chaine.isalpha())  # False, puisque elle contient 1
print(une_autre_chaine.isalpha())  # True puisque à la fois `a` et `A` sont des lettres de l'alphabet
```

#### Méthode `isdecimal()`

`isdecimal()` retourne True si tous les caractères d'une chaîne sont des nombres :

```python
chaine = "A1"
une_autre_chaine = "3.31"
encore_une_autre_chaine = "3431"

print(chaine.isdecimal())  # False, puisque elle contient 'A'
print(une_autre_chaine.isdecimal())  # False, puisque elle contient '.'
print(encore_une_autre_chaine.isdecimal())  # True, puisque elle contient uniquement des nombres
```

### Formatage de chaînes

Le formatage d'une chaîne peut être assez utile puisque vous pouvez l'utiliser assez fréquemment, quel que soit le type de projet ou de script sur lequel vous travaillez.

Illustrons d'abord pourquoi nous avons besoin de formatage et incluons l'interpolation de chaînes.

Imaginez que je veux développer un logiciel qui salue les gens au moment où ils arrivent, comme :

```python
salutation = "Bonjour Fatos."
```

Cela semble bien maintenant, mais je ne suis pas la seule personne qui l'utilise, n'est-ce pas ?

Je ne suis qu'une des personnes qui a la chance de l'utiliser.

Maintenant, si quelqu'un vient et s'inscrit, je vais devoir utiliser leurs propres noms, comme :

```python
salutation = "Bonjour Besart."
```

C'est juste mon premier utilisateur réel qui s'inscrit. Je ne me compte pas moi-même.

Maintenant, imaginons que j'ai de la chance et que le deuxième utilisateur arrive également un vendredi matin et que notre application doit afficher :

```python
salutation = "Bonjour Betim."
```

Comme vous pouvez le voir, nous arrivons quelque part d'un point de vue commercial puisque deux nouveaux utilisateurs viennent d'arriver, mais ce n'est pas une implémentation évolutive. Nous écrivons une expression `salutation` très statique.

Vous devriez déjà vous souvenir que nous allons mentionner quelque chose que j'ai introduit au début.

Oui, nous allons devoir utiliser des variables et inclure une variable à côté de la chaîne, comme suit :

```python
salutation = "Bonjour " + prenom
```

C'est beaucoup plus flexible.

C'est une façon de faire cela.

Une autre façon de faire cela est d'utiliser une méthode appelée `format()`.

Nous pouvons utiliser des accolades pour spécifier les endroits où nous voulons mettre des valeurs dynamiques, comme suit :

```python
salutation = "Bonjour {}. Aujourd'hui, nous sommes le {}.".format("Fatos", "Vendredi")
```

Cela va maintenant mettre le premier paramètre de la méthode `format()` à l'intérieur des premières accolades, qui dans notre cas est `Fatos`. Ensuite, dans la deuxième occurrence des accolades, il va mettre le deuxième paramètre de la méthode `format()`.

Si nous essayons d'imprimer la valeur de la chaîne, nous devrions obtenir ce qui suit :

```python
print(salutation)
# Bonjour Fatos. Aujourd'hui, nous sommes le Vendredi.
```

Nous pouvons spécifier des paramètres avec des index à l'intérieur des accolades comme suit qui peuvent ensuite être utilisés :

```python
salutation = "Aujourd'hui, nous sommes le {1}. Passez une bonne journée {0}.".format("Fatos", "Vendredi")

print(salutation)
# salutation = "Aujourd'hui, nous sommes le {1}. Passez une bonne journée {0}.".format("Fatos", "Vendredi")
```

Nous pouvons également spécifier des paramètres à l'intérieur de la méthode `format()` et utiliser ces mots spécifiques à l'intérieur des accolades comme référence :

```python
salutation = "Aujourd'hui, nous sommes le {jour_de_la_semaine}. Passez une bonne journée {prenom}.".format(prenom="Fatos",
                                                                              jour_de_la_semaine="Vendredi")
print(salutation)  # Aujourd'hui, nous sommes le Vendredi. Passez une bonne journée Fatos.
```

Nous pouvons combiner les deux types d'arguments dans un seul exemple, comme suit :

```python
courte_bio = 'Mon nom est {nom}. Mon nom de famille est {0}. J\'adore {passion}. J\'aime jouer à {1}.'.format(
    'Morina',
    'Basketball',
    nom='Fatos',
    passion='Programmation'
)

print(courte_bio)
# Mon nom est Fatos. Mon nom de famille est Morina. J'adore la programmation. J'aime jouer au basketball.
```

Comme vous pouvez le voir, l'utilisation d'arguments nommés par opposition à des arguments positionnels peut être moins sujette aux erreurs, puisque leur ordre dans la méthode `format()` n'a pas d'importance.

Nous pouvons également utiliser une autre façon de formater les chaînes qui consiste à commencer une chaîne par `f` ou `F` avant les guillemets d'ouverture ou les guillemets triples et à inclure les noms des variables que nous voulons voir incluses à la fin :

```python
prenom = "Fatos"
jour_de_la_semaine = "Vendredi"
continent = "Europe"

salutation = f'Bonjour {prenom}. Aujourd\'hui, nous sommes le {jour_de_la_semaine}'

print(salutation)  # Bonjour Fatos. Aujourd'hui, nous sommes le Vendredi.
```

Voici un autre exemple où nous utilisons un guillemet triple après le `F` :

```python
continent = "Europe"

je_suis_ici = F'''Je suis en {continent}'''

print(je_suis_ici)  # Je suis en Europe
```

## Listes en Python

Si vous regardez une étagère à livres, vous pouvez voir que les livres sont empilés et placés étroitement les uns à côté des autres. Vous pouvez voir qu'il y a de nombreux exemples de collecte et de structuration d'éléments de quelque manière que ce soit.

Cela est également assez important en programmation informatique. Nous ne pouvons pas simplement continuer à déclarer d'innombrables variables et les gérer aussi facilement.

Disons que nous avons une classe d'étudiants et que nous voulons enregistrer leurs noms. Nous pouvons commencer à enregistrer leurs noms selon la manière dont ils sont positionnés dans la salle de classe :

```python
premier = "Albert"
deuxieme = "Besart"
troisieme = "Fisnik"
quatrieme = "Festim"
cinquieme = "Gazmend"
```

La liste peut continuer, ce qui rendra assez difficile pour nous de suivre tous.

Il existe heureusement une manière plus facile pour nous de mettre ceux-ci dans une collection en Python appelée une liste.

Créons une liste appelée *étudiants* et stockons dans cette liste tous les noms déclarés dans le bloc de code précédent :

```python
étudiants = ["Albert", "Besart", "Fisnik", "Festim", "Gazmend"]
```

C'est plus joli, n'est-ce pas ?

De plus, cette façon, il est plus facile pour nous de gérer et aussi de manipuler les éléments dans la liste.

Vous pouvez penser que, "Eh bien, c'était plus facile pour moi de simplement appeler *premier* et obtenir la valeur stockée là. Maintenant, il est impossible d'obtenir une valeur de cette nouvelle liste, appelée *étudiants*".

Si nous ne pouvions pas lire et utiliser ces éléments que nous venons de stocker dans une liste, cela la rendrait moins utile.

Heureusement, les listes ont des index, qui commencent à 0. Cela signifie que si nous voulons obtenir le premier élément d'une liste, nous devons utiliser l'index 0 et non l'index 1 comme vous pourriez le penser.

Dans l'exemple ci-dessus, les éléments de la liste ont ces index correspondants :

```python
étudiants = ["Albert", "Besart", "Fisnik", "Festim", "Gazmend"]
# Index 0, 1, 2, 3, 4
```

Maintenant, si nous voulons obtenir le premier élément, nous écrivons simplement :

```python
étudiants[0]
```

Si nous voulons obtenir le deuxième élément, nous écrivons simplement :

```python
étudiants[1]
```

Comme vous pouvez probablement le voir, nous devons simplement écrire le nom de la liste et également l'index correspondant de l'élément que nous voulons obtenir entre crochets.

Cette liste n'est, bien sûr, pas statique. Nous pouvons ajouter des éléments à celle-ci, comme lorsqu'un nouvel étudiant rejoint la classe.

Ajoutons un nouvel élément dans la liste *étudiants* avec la valeur *Besfort* :

```python
étudiants.append("Besfort")
```

Nous pouvons également changer la valeur d'un élément existant. Pour cela, nous devons simplement réinitialiser cet élément spécifique de la liste avec une nouvelle valeur.

Par exemple, changeons le nom du premier étudiant :

```python
étudiants[0] = "Besim"
```

Les listes peuvent contenir différents types de variables, par exemple, nous pouvons avoir une chaîne qui contient des entiers, des nombres à virgule flottante et des chaînes :

```python
liste_combinee = [3.14, "Un élément", 1, "Un autre élément ici"]
```

### Découpage

De manière similaire aux chaînes, les listes peuvent également être découpées, ce qui, en résultat, retourne une nouvelle liste. Cela signifie que la liste originale reste inchangée.

Voyons comment nous pouvons obtenir les trois premiers éléments d'une liste en utilisant le découpage :

```python
ma_liste = [1, 2, 3, 4, 5]

print(ma_liste[0:3])  # [1, 2, 3]
```

Comme vous pouvez le voir, nous avons spécifié 0 comme index de départ et 3 comme index où le découpage doit s'arrêter, en excluant l'élément à l'index de fin.

Si nous voulons simplement commencer à partir d'un index et obtenir tous les éléments restants dans la liste, ce qui signifie que l'index de fin doit être le dernier index, alors nous pouvons omettre et ne pas avoir à écrire le dernier index du tout :

```python
ma_liste = [1, 2, 3, 4, 5]

print(ma_liste[3:])  # [4, 5]
```

De même, si nous voulons commencer à partir du début de la liste et faire le découpage jusqu'à un index spécifique, alors nous pouvons omettre d'écrire l'index 0 entièrement, puisque Python est assez intelligent pour l'inférer :

```python
ma_liste = [1, 2, 3, 4, 5]

print(ma_liste[:3])  # [1, 2, 3]
```

Les chaînes en Python sont immuables, tandis que les listes sont mutables, ce qui signifie que nous pouvons modifier le contenu des listes après les avoir déclarées.

À titre d'illustration, supposons que nous voulons changer le premier caractère de la chaîne, à savoir remplacer `S` par `B` de la manière suivante :

```python
chaine = "Chaine"
chaine[0] = "B"
```

Maintenant, si nous essayons d'imprimer `chaine`, nous obtiendrons une erreur comme suit :

```python
# TypeError: l'objet 'str' ne supporte pas l'affectation d'élément
```

Maintenant, si nous avons une liste et que nous voulons modifier son premier élément, alors nous pouvons le faire avec succès :

```python
ma_liste = ["a", "b", "c", "d", "e"]

ma_liste[0] = 50

print(ma_liste)  # [50, 'b', 'c', 'd', 'e']
```

Nous pouvons étendre une liste en la concaténant avec une autre liste en utilisant l'opérateur `+` :

```python
première_liste = [1, 2, 3]

deuxième_liste = [4, 5]

première_liste = première_liste + deuxième_liste 

print(première_liste)  # [1, 2, 3, 4, 5]
```

### Comment imbriquer une liste à l'intérieur d'une autre liste

Nous pouvons imbriquer une liste à l'intérieur d'une autre liste comme ceci :

```python
points_math = [30, "Math"]

points_physique = [53, "Physique"]

matières = [points_math, points_physique]

print(matières)  # [[30, 'Math'], [53, 'Physique']]
```

Ces listes n'ont même pas besoin d'avoir la même longueur.

Pour accéder aux éléments d'une liste qui se trouve à l'intérieur d'une liste, nous devons utiliser des index doubles.

Voyons comment nous pouvons accéder à l'élément `points_math` à l'intérieur de la liste `matières`. Puisque `points_math` est un élément dans la liste `matières` positionné à l'index 0, nous devons simplement faire ce qui suit :

```python
print(matières[0])  # [30, 'Math']
```

Maintenant, supposons que nous voulons accéder à `Math` à l'intérieur de la liste `matières`. Puisque `Math` est à l'index `1`, nous allons devoir utiliser les index doubles suivants :

```python
print(matières[0][1])  # 'Math'
```

### Méthodes de liste

`len()` est une méthode que vous pouvez utiliser pour trouver la longueur d'une liste :

```python
ma_liste = ["a", "b", 1, 3]

print(len(ma_liste))  # 4
```

#### Comment ajouter des éléments à une liste

Nous pouvons également étendre les listes en ajoutant de nouveaux éléments, ou nous pouvons également supprimer des éléments.

Nous pouvons ajouter de nouveaux éléments à la fin d'une liste en utilisant la méthode `append()` :

```python
ma_liste = ["a", "b", "c"]

ma_liste.append("Nouvel élément")

ma_liste.append("Encore un nouvel élément")

print(ma_liste) 
# ['a', 'b', 'c', 'Nouvel élément', 'Encore un nouvel élément']
```

Si nous voulons ajouter des éléments à des index spécifiques dans une liste, nous pouvons utiliser la méthode `insert()`. Nous spécifions l'index dans le premier argument et l'élément que nous voulons ajouter dans la liste comme deuxième argument :

```python
ma_liste = ["a", "b"]

ma_liste.insert(1, "z")

print(ma_liste)  # ['a', 'z', 'b']
```

#### Comment supprimer des éléments d'une liste

Nous pouvons supprimer des éléments de listes en utilisant la méthode `pop()`, qui supprime le dernier élément de la liste :

```python
ma_liste = [1, 2, 3, 4, 5]

ma_liste.pop()  # supprime 5 de la liste

print(ma_liste)  # [1, 2, 3, 4]

ma_liste.pop()  # supprime 4 de la liste

print(ma_liste)  # [1, 2, 3]
```

Nous pouvons également spécifier l'index d'un élément dans la liste qui indique quel élément de la liste nous devons supprimer :

```python
ma_liste = [1, 2, 3, 4, 5]

ma_liste.pop(0)  # Supprime l'élément à l'index 0

print(ma_liste)  # [2, 3, 4, 5]
```

Nous pouvons également supprimer des éléments de listes en utilisant l'instruction `del` et en spécifiant ensuite la valeur de l'élément que nous voulons supprimer :

```python
ma_liste = [1, 2, 3, 4, 1]

del ma_liste[0]  # Supprime l'élément ma_liste[0]

print(ma_liste)  # [2, 3, 4, 5]
```

Nous pouvons également supprimer des tranches de listes en utilisant `del` :

```python
ma_liste = [1, 2, 3, 4, 1]

del ma_liste[0:3]  # Supprime les éléments : ma_liste[0], ma_liste[1], ma_liste[2]

print(ma_liste)  # [4, 1]
```

Nous pouvons faire cela en utilisant `remove()` :

```python
ma_liste = [1, 2, 3, 4]

ma_liste.remove(3) 

print(ma_liste)  # [1, 2, 4]
```

`reverse()` nous permet d'inverser les éléments d'une liste. C'est assez simple et direct :

```python
ma_liste = [1, 2, 3, 4]

ma_liste.reverse()

print(ma_liste)  # [4, 3, 2, 1]
```

#### Recherche d'index

Obtenir des éléments d'une liste en utilisant des index est simple. Trouver des index d'éléments d'une liste est également facile. Nous devons simplement utiliser la méthode `index()` et mentionner l'élément que nous voulons trouver à l'intérieur d'une liste :

```python
ma_liste = ["Fatos", "Morina", "Python", "Logiciel"]

print(ma_liste.index("Python"))  # 2
```

### Appartenance

Cela est assez intuitif et lié à la vie réelle : nous pouvons nous demander si quelque chose fait partie de quelque chose ou non.

Mon téléphone est-il dans ma poche ou mon sac ?

L'e-mail de mon collègue est-il inclus dans le CC ?

Mon ami est-il dans ce café ?

En Python, si nous voulons vérifier si une valeur fait partie de quelque chose, nous pouvons utiliser l'opérateur `in` :

```python
ma_liste = [1, 2, 3]  # C'est une liste

print(1 in ma_liste)  # True
```

Puisque 1 est inclus dans le tableau `[1, 2, 3]`, l'expression évalue à True.

Nous pouvons également l'utiliser non seulement avec des tableaux de nombres, mais aussi avec des tableaux de caractères :

```python
voyelles = ['a', 'i', 'o', 'u']
print('y' in voyelles)  # False
```

Puisque `y` n'est pas une voyelle et n'est pas inclus dans le tableau déclaré, l'expression dans la deuxième ligne du précédent extrait de code va résulter en False.

De même, nous pouvons également vérifier si quelque chose n'est pas inclus en utilisant `not in` :

```python
nombres_impairs = [1, 3, 5, 7]
print(2 not in nombres_impairs)  # True
```

Puisque 2 n'est pas inclus dans le tableau, l'expression va évaluer à True.

### Comment trier les éléments d'une liste

Trier les éléments d'une liste est quelque chose que vous pouvez avoir besoin de faire de temps en temps. `sort()` est une méthode intégrée qui vous permet de trier les éléments d'une liste par ordre croissant alphabétique ou numérique :

```python
ma_liste = [3, 1, 2, 4, 5, 0]

ma_liste.sort()

print(ma_liste)  # [0, 1, 2, 3, 4, 5]

liste_alphabetique = ['a', 'c', 'b', 'z', 'e', 'd']

liste_alphabetique.sort()

print(liste_alphabetique)  # ['a', 'b', 'c', 'd', 'e', 'z']
```

Il existe d'autres méthodes de listes que nous n'avons pas incluses ici.

### Compréhension de liste

La compréhension de liste représente une manière concise dans laquelle nous utilisons une boucle `for` pour créer une nouvelle liste à partir d'une liste existante. Le résultat est toujours une nouvelle liste à la fin.

Commençons par un exemple où nous voulons multiplier chaque nombre d'une liste par 10 et sauvegarder ce résultat dans une nouvelle liste. D'abord, faisons cela sans utiliser la compréhension de liste :

```python
nombres = [2, 4, 6, 8]  # Liste complète

nombres_dix_fois = []  # Liste vide

for nombre in nombres:
    nombre = nombre * 10  # Multiplier chaque nombre par 10
    nombres_dix_fois.append(nombre)  # Ajouter ce nouveau nombre dans la nouvelle liste
    
print(nombres_dix_fois)  # [20, 40, 60, 80]
```

Nous pouvons implémenter cela en utilisant la compréhension de liste de la manière suivante :

```python
nombres = [2, 4, 6, 8]  # Liste complète

nombres_dix_fois = [nombre * 10 for nombre in nombres]  # Compréhension de liste

print(nombres_dix_fois)  # [20, 40, 60, 80]
```

Nous pouvons également inclure des conditions lors de ces compréhensions de liste.

Supposons que nous voulons sauvegarder une liste de nombres positifs.

Avant d'écrire la manière dont nous implémenterions cela en utilisant la compréhension de liste, écrivons une manière dans laquelle nous créerions une liste de seulement des nombres qui sont supérieurs à 0 dans une autre liste et augmenterions ces nombres positifs de 100 :

```python
nombres_positifs = []  # Liste vide

nombres = [-1, 0, 1, -2, -3, -4, 3, 2]  # Liste complète

for nombre in nombres:
    if nombre > 0:  # Si le nombre actuel est supérieur à 0
        nombres_positifs.append(nombre + 100)  # ajouter ce nombre à l'intérieur de la liste nombres_positifs

        
print(nombres_positifs)  # [101, 103, 102]
```

Nous pouvons faire de même en utilisant la compréhension de liste :

```python
nombres = [-1, 0, 1, -2, -3, -4, 3, 2]  # Liste complète

nombres_positifs = [nombre + 100 for nombre in nombres if nombre > 0]  # Compréhension de liste

print(nombres_positifs)  # [101, 103, 102]
```

Comme vous pouvez le voir, cela est beaucoup plus court et devrait prendre moins de temps à écrire.

Nous pouvons également utiliser la compréhension de liste avec plusieurs listes.

Prenons un exemple où nous voulons ajouter chaque élément d'une liste avec chaque élément d'une autre liste :

```python
première_liste = [1, 2, 3]
deuxième_liste = [50]

double_listes = [premier_élément +
                deuxième_élément for premier_élément in première_liste for deuxième_élément in deuxième_liste]

print(double_listes)  # [51, 52, 53]
```

À la fin, nous allons obtenir une liste résultante qui a le même nombre d'éléments que la liste avec la longueur la plus longue.

## Tuples en Python

Les tuples sont des collections qui sont ordonnées et immuables, ce qui signifie que leur contenu ne peut pas être modifié. Ils sont ordonnés et nous pouvons accéder à leurs éléments en utilisant des index.

Commençons avec notre premier tuple :

```python
véhicules = ("Ordinateur", "Smartphone", "Montre intelligente", "Tablette")

print(véhicules)

# ('Ordinateur', 'Smartphone', 'Montre intelligente', 'Tablette')
```

Toutes les opérations d'indexation et de découpage que nous avons vues dans la section sur les listes s'appliquent également aux tuples :

```python
print(len(véhicules))  # 4

print(véhicules[3])  # Tablette

print(véhicules[:3])  # ('Ordinateur', 'Smartphone', 'Montre intelligente')
```

Vous pouvez trouver l'index d'un élément à l'intérieur d'un tuple en utilisant la méthode `index()` :

```python
print(véhicules.index('tablette'))  # 3
```

Nous pouvons également concaténer ou fusionner deux tuples en utilisant l'opérateur `+` :

```python
sciences_naturelles = ('Chimie', 'Astronomie',
                    'Science de la Terre', 'Physique', 'Biologie')

sciences_sociales = ('Anthropologie', 'Archéologie', 'Économie', 'Géographie',
                   'Histoire', 'Droit', 'Linguistique', 'Politique', 'Psychologie', 'Sociologie')

sciences = sciences_naturelles + sciences_sociales

print(sciences)
# ('Chimie', 'Astronomie', 'Science de la Terre', 'Physique', 'Biologie', 'Anthropologie', 'Archéologie', 'Économie', 'Géographie', 'Histoire', 'Droit', 'Linguistique', 'Politique', 'Psychologie', 'Sociologie')
```

### Vérification d'appartenance

Nous pouvons vérifier si un élément fait partie d'un tuple en utilisant les opérateurs `in` et `not in` tout comme avec les listes :

```python
véhicules = ('Voiture', 'Vélo', 'Avion')

print('Moto' in véhicules)  # False, puisque Moto n'est pas inclus dans véhicules

print('Train' not in véhicules)  # True, puisque Train n'est pas inclus dans véhicules
```

### Comment imbriquer deux tuples

Au lieu de fusionner, nous pouvons également imbriquer des tuples dans un seul tuple en utilisant des tuples que nous voulons imbriquer à l'intérieur des parenthèses :

```python
sciences_naturelles = ('Chimie', 'Astronomie',
                    'Science de la Terre', 'Physique', 'Biologie')

sciences_sociales = ('Anthropologie', 'Archéologie', 'Économie', 'Géographie',
                   'Histoire', 'Droit', 'Linguistique', 'Politique', 'Psychologie', 'Sociologie')

sciences = (sciences_naturelles, sciences_sociales)

print(sciences)
# (('Chimie', 'Astronomie', 'Science de la Terre', 'Physique', 'Biologie'), ('Anthropologie', 'Archéologie', 'Économie', 'Géographie', 'Histoire', 'Droit', 'Linguistique', 'Politique', 'Psychologie', 'Sociologie'))
```

### Immuabilité

Puisque les tuples sont immuables, nous ne pouvons pas les modifier après les avoir créés. Cela signifie que nous ne pouvons pas ajouter ou supprimer des éléments, ou ajouter un tuple à un autre tuple.

Nous ne pouvons même pas modifier les éléments existants dans un tuple. Si nous essayons de modifier un élément dans un tuple, nous allons rencontrer un problème comme suit :

```python
véhicules = ('Voiture', 'Vélo', 'Avion')

véhicules[0] = 'Camion'

print(véhicules)
# TypeError: l'objet 'tuple' ne supporte pas l'affectation d'élément
```

## Dictionnaires en Python – Structures de données clé-valeur

Comme nous l'avons vu précédemment, les éléments dans les listes sont associés à des index que nous pouvons utiliser pour référencer ces éléments.

Il existe une autre structure de données en Python qui nous permet de spécifier nos propres index personnalisés et pas seulement des nombres. Ceux-ci sont appelés dictionnaires, et ils sont similaires aux dictionnaires que nous utilisons pour trouver la signification des mots que nous ne comprenons pas.

Supposons que vous essayez d'apprendre l'allemand et qu'il y a un nouveau mot que vous n'avez pas eu la chance d'apprendre auparavant et que vous venez de voir sur un marché : *Wasser*.

Maintenant, vous pouvez prendre votre téléphone et vérifier sa signification correspondante en anglais en utilisant Google Translate ou toute autre application de votre choix. Mais si vous deviez utiliser un dictionnaire physique, vous devriez trouver ce mot en allant à cette page spécifique et vérifier sa signification qui se trouve juste à côté. La référence ou la clé pour la signification de ce mot serait le terme *Wasser*.

Maintenant, si nous voulons implémenter cela en Python, nous ne devrions pas utiliser des listes qui n'ont que des index sous forme de nombres. Nous devrions utiliser des dictionnaires à la place.

Pour les dictionnaires, nous utilisons des accolades et avons chaque élément qui a deux parties : la clé et la valeur.

Dans notre exemple précédent, la clé était le mot allemand, tandis que la valeur était sa traduction en anglais, comme vous pouvez le voir dans l'exemple suivant :

```python
traduction_allemand_anglais = {
    "Wasser": "Eau",
    "Brot": "Pain",
    "Milch": "Lait"
}
```

Maintenant, lorsque nous voulons accéder à des éléments spécifiques dans le dictionnaire, nous utilisons simplement les clés. Par exemple, supposons que nous voulons obtenir la signification du mot *Brot* en anglais. Pour cela, nous pouvons simplement référencer cet élément en utilisant cette clé :

```python
traduction_brot = traduction_allemand_anglais["Brot"]
print(traduction_brot)  # Pain
```

Lorsque nous imprimons la valeur que nous obtenons, nous allons obtenir la traduction en anglais.

De même, nous pouvons obtenir la traduction anglaise du mot *Milch* en obtenant la valeur de l'élément qui a *Milch* comme clé :

```python
traduction_milch = traduction_allemand_anglais["Milch"]
print(traduction_milch)  # Lait
```

Nous pouvons également obtenir la valeur d'un élément dans un dictionnaire en utilisant `get()` et en spécifiant la clé de l'élément que nous voulons obtenir :

```python
traduction_allemand_anglais.get("Wasser")
```

Les clés et les valeurs peuvent être de n'importe quel type de données.

Les dictionnaires peuvent avoir des valeurs en double, mais toutes les clés doivent être uniques. Jetez un coup d'œil à cet exemple pour voir ce que je veux dire :

```python
mon_dictionnaire = dict([
  ('a', 1),
  ('b', 1),
  ('c', 2)
])
```

Nous pouvons créer des dictionnaires en utilisant `dict()` :

```python
mots = dict([
    ('abandonner', 'renoncer à quelqu\'un ou quelque chose sur le terrain'),
    ('abaisser', 'abaisser en rang, fonction ou estime'),
    ('confondre', 'détruire la possession de soi ou la confiance en soi')
])

print(mots)
# {'abandonner': 'renoncer à quelqu\'un ou quelque chose sur le terrain', 'abaisser': 'abaisser en rang, fonction ou estime', 'confondre': 'détruire la possession de soi ou la confiance en soi'}
```

### Comment ajouter de nouvelles valeurs à un dictionnaire

Nous pouvons ajouter de nouvelles valeurs à l'intérieur des dictionnaires en spécifiant une nouvelle clé et une valeur correspondante. Ensuite, Python va créer un nouvel élément à l'intérieur de ce dictionnaire :

```python
mots = {
    'a': 'alpha',
    'b': 'bêta',
    'd': 'delta',
}

mots['g'] = 'gamma'

print(mots)
# {'a': 'alpha', 'b': 'bêta', 'd': 'delta', 'g': 'gamma'}
```

Si nous spécifions la clé d'un élément qui fait déjà partie du dictionnaire, cet élément va être modifié :

```python
mots = {
    'a': 'alpha',
    'b': 'bêta',
    'd': 'delta',
}

mots['b'] = 'bravo'


print(mots)
# {'a': 'alpha', 'b': 'bravo', 'd': 'delta'}
```

### Comment supprimer des éléments d'un dictionnaire

Si nous voulons supprimer des éléments d'un dictionnaire, nous pouvons utiliser la méthode `pop()` et également spécifier la clé de l'élément que nous voulons supprimer :

```python
mots = {
    'a': 'alpha',
    'b': 'bêta',
    'd': 'delta',
}

mots.pop('a')

print(mots)  # {'b': 'bêta', 'd': 'delta'}
```

Nous pouvons également supprimer des valeurs en utilisant `popitem()` qui supprime la dernière paire clé-valeur insérée à partir de Python 3.7. Dans les versions antérieures, il supprime une paire aléatoire :

```python
mots = {
    'a': 'alpha',
    'b': 'bêta',
    'd': 'delta',
}

mots['g'] = 'gamma'

mots.popitem()

print(mots) 
# {'a': 'alpha', 'b': 'bêta', 'd': 'delta'}
```

Il existe une autre façon de supprimer des éléments, à savoir en utilisant l'instruction `del` :

```python
mots = {
    'a': 'alpha',
    'b': 'bêta',
    'd': 'delta',
}

del mots['b']

print(mots)  # {'a': 'alpha', 'd': 'delta'}
```

### Comment obtenir la longueur d'un dictionnaire

Nous pouvons obtenir la longueur d'un dictionnaire en utilisant `len()` tout comme avec les listes et les tuples :

```python
mots = {
    'a': 'alpha',
    'b': 'bêta',
    'd': 'delta',
}

print(len(mots))  # 3
```

### Appartenance

Si nous voulons vérifier si une clé fait déjà partie d'un dictionnaire afin d'éviter de l'écraser, nous pouvons utiliser les opérateurs `in` et `not in` tout comme avec les listes et les tuples :

```python
mots = {
    'a': 'alpha',
    'b': 'bêta',
    'd': 'delta',
}

print('a' in mots)  # True
print('z' not in mots)  # True
```

### Compréhension

Nous pouvons utiliser la compréhension tout comme avec les listes pour créer des dictionnaires de manière rapide.

Pour nous aider avec cela, nous allons avoir besoin d'utiliser une méthode appelée `items()` qui convertit un dictionnaire en une liste de tuples. L'élément à l'index 0 est une clé, tandis qu'à la position avec l'index 1, nous avons une valeur.

Voyons d'abord la méthode `items()` en action :

```python
points = {
    'Festim': 50,
    'Zgjim': 89,
    'Durim': 73
}

éléments = points.items()

print(éléments) # dict_items([('Festim', 50), ('Zgjim', 89), ('Durim', 73)])
```

Maintenant, créons un nouveau dictionnaire à partir de ce dictionnaire existant `points` en utilisant la compréhension.

Nous pouvons supposer qu'un professeur est de bonne humeur et suffisamment généreux pour récompenser chaque étudiant avec un bonus de `10` points. Nous voulons ajouter ces nouveaux points à chaque étudiant en sauvegardant ces nouveaux points dans un nouveau dictionnaire :

```python
points = {
    'Festim': 50,
    'Zgjim': 89,
    'Durim': 73
}

éléments = points.items()

points_modifiés = {clé: valeur + 10 for (clé, valeur) in éléments}

print(points_modifiés)  # {'Festim': 60, 'Zgjim': 99, 'Durim': 83}
```

## Ensembles en Python

Les ensembles sont des collections non ordonnées et non indexées de données. Puisque les éléments dans les ensembles ne sont pas ordonnés, nous ne pouvons pas accéder aux éléments en utilisant des index ou en utilisant la méthode `get()`.

Nous pouvons ajouter des tuples, mais nous ne pouvons pas ajouter des dictionnaires ou des listes dans un ensemble.

Nous ne pouvons pas ajouter d'éléments en double dans les ensembles. Cela signifie que lorsque nous voulons supprimer des éléments en double d'un autre type de collection, nous pouvons utiliser cette unicité dans les ensembles.

Commençons par créer notre premier ensemble en utilisant des accolades comme suit :

```python
premier_ensemble = {1, 2, 3}
```

Nous pouvons également créer des ensembles en utilisant le constructeur `set()` :

```python
ensemble_vide = set()  # Ensemble vide

premier_ensemble = set((1, 2, 3))  # Nous convertissons un tuple en un ensemble
```

Comme toutes les structures de données, nous pouvons trouver la longueur d'un ensemble en utilisant la méthode `len()` :

```python
print(len(premier_ensemble))  # 3
```

### Comment ajouter des éléments à un ensemble

Nous pouvons ajouter un élément dans un ensemble en utilisant la méthode `add()` :

```python
mon_ensemble = {1, 2, 3}

mon_ensemble.add(4)

print(mon_ensemble)  # {1, 2, 3, 4}
```

Si nous voulons ajouter plus d'un élément, alors nous devons utiliser la méthode `update()`. Nous utilisons comme entrée pour cette méthode une liste, un tuple, une chaîne ou un autre ensemble :

```python
mon_ensemble = {1, 2, 3}

mon_ensemble.update([4, 5, 6])

print(mon_ensemble)  # {1, 2, 3, 4, 5, 6}

mon_ensemble.update("ABC")

print(mon_ensemble)  # {1, 2, 3, 4, 5, 6, 'A', 'C', 'B'}
```

### Comment supprimer des éléments d'un ensemble

Si nous voulons supprimer des éléments d'ensembles, nous pouvons utiliser les méthodes `discard()` ou `remove()` :

```python
mon_ensemble = {1, 2, 3}

mon_ensemble.remove(2)

print(mon_ensemble)  # {1, 3}
```

Si nous essayons de supprimer un élément qui ne fait pas partie de l'ensemble en utilisant `remove()`, alors nous allons obtenir une erreur :

```python
mon_ensemble = {1, 2, 3}

mon_ensemble.remove(4)

print(mon_ensemble)  # KeyError: 4
```

Pour éviter de telles erreurs lors de la suppression d'éléments d'ensembles, nous pouvons utiliser la méthode `discard()` :

```python
mon_ensemble = {1, 2, 3}

mon_ensemble.discard(4)

print(mon_ensemble)  # {1, 2, 3}
```

### Opérations de théorie des ensembles

Si vous vous souvenez des leçons de mathématiques du lycée, vous devriez déjà connaître l'union, l'intersection et la différence entre deux ensembles d'éléments. Ces opérations sont également prises en charge pour les ensembles en Python.

#### Union

L'union représente la collection de tous les éléments uniques des deux ensembles. Nous pouvons trouver l'union de deux ensembles en utilisant l'opérateur pipe `|` ou la méthode `union()` :

```python
premier_ensemble = {1, 2}
deuxieme_ensemble = {2, 3, 4}

ensemble_union = premier_ensemble.union(deuxieme_ensemble)

print(ensemble_union)  # {1, 2, 3, 4}
```

#### Intersection

L'intersection représente la collection qui contient les éléments qui sont dans les deux ensembles. Nous pouvons la trouver en utilisant l'opérateur `&` ou la méthode `intersection()` :

```python
premier_ensemble = {1, 2}
deuxieme_ensemble = {2, 3, 4}

ensemble_intersection = premier_ensemble.intersection(deuxieme_ensemble)

print(ensemble_union)  # {2}
```

#### Différence

La différence entre deux ensembles représente la collection qui contient uniquement les éléments qui sont dans le premier ensemble, mais pas dans le second. Nous pouvons trouver la différence entre deux ensembles en utilisant l'opérateur `-` ou la méthode `difference()`

```python
premier_ensemble = {1, 2}
deuxieme_ensemble = {2, 3, 4}

ensemble_difference = premier_ensemble.difference(deuxieme_ensemble)

print(ensemble_difference)  # {1}
```

Comme vous pouvez probablement vous en souvenir du lycée, l'ordre des ensembles lorsque nous trouvons la différence de deux ensembles compte, ce qui n'est pas le cas avec l'union et l'intersection.

Cela est similaire à l'arithmétique, où `3 - 4` n'est pas égal à `4 - 3` :

```python
premier_ensemble = {1, 2}
deuxieme_ensemble = {2, 3, 4}

premier_ensemble_difference = premier_ensemble.difference(deuxieme_ensemble)

print(premier_ensemble_difference)  # {1}

deuxieme_ensemble_difference = deuxieme_ensemble.difference(premier_ensemble)

print(deuxieme_ensemble_difference)  # {3, 4}
```

# Conversions de types en Python

## Conversions entre types primitifs

Python est un langage de programmation orienté objet. C'est pourquoi il utilise des fonctions constructrices de classes pour effectuer des conversions d'un type à un autre.

### Méthode `int()`

`int()` est une méthode que vous utilisez pour convertir un littéral entier, un littéral flottant (en l'arrondissant à son nombre entier précédent, c'est-à-dire 3.1 à 3), ou un littéral de chaîne (à condition que la chaîne représente un littéral int ou float) :

```python
trois = int(3)  # conversion d'un littéral entier en un entier
print(trois)  # 3

quatre = int(4.8)  # conversion d'un nombre flottant en son entier le plus proche précédent
print(quatre)  # 4

cinq = int('5')  # conversion d'une chaîne en un entier
print(cinq)  # 5
```

### Méthode `float()`

`float()` est utilisé de manière similaire pour créer des nombres flottants à partir d'un entier, d'un flottant ou d'un littéral de chaîne (à condition que la chaîne représente un littéral `int` ou `float`) :

```python
littéral_int = float(5)
print(littéral_int)  # 5.0

littéral_float = float(1.618)
print(littéral_float)  # 1.618

chaîne_int = float("40")
print(chaîne_int)  # 40.0

chaîne_float = float("37.2")
print(chaîne_float)  # 37.2
```

### Méthode `str()`

Nous pouvons utiliser `str()` pour créer des chaînes à partir de chaînes, de littéraux entiers, de littéraux flottants et de nombreux autres types de données :

```python
int_en_chaine = str(3)
print(int_en_chaine)  # '3'

float_en_chaine = str(3.14)
print(float_en_chaine)  # '3.14'

chaine_en_chaine = str('bonjour')
print(chaine_en_chaine)  # 'bonjour'
```

## Autres conversions

Pour convertir d'un type de structure de données à un autre type, nous faisons ce qui suit :

```markdown
type_destination(type_entrée)
```

Commençons avec des types spécifiques, afin que cela devienne beaucoup plus clair.

### Conversions en listes

Nous pouvons convertir un ensemble, un tuple ou un dictionnaire en une liste en utilisant le constructeur `list()`.

```python
livres_tuple = ('Livre 1', 'Livre 2', 'Livre 3')
tuple_en_liste = list(livres_tuple)  # Conversion de tuple en liste
print(tuple_en_liste)  # ['Livre 1', 'Livre 2', 'Livre 3']


livres_ensemble = {'Livre 1', 'Livre 2', 'Livre 3'}
ensemble_en_liste = list(livres_ensemble)  # Conversion d'ensemble en liste
print(ensemble_en_liste)  # ['Livre 1', 'Livre 2', 'Livre 3']
```

Lors de la conversion d'un dictionnaire en une liste, seules ses clés vont être incluses dans la liste :

```python
livres_dict = {'1': 'Livre 1', '2': 'Livre 2', '3': 'Livre 3'}
dict_en_liste = list(livres_dict)  # Conversion de dict en liste
print(dict_en_liste)  # ['1', '2', '3']
```

Si nous voulons conserver à la fois les clés et les valeurs d'un dictionnaire, nous devons utiliser la méthode `items()` pour le convertir d'abord en une liste de tuples où chaque tuple est une clé et une valeur :

```python
livres_dict = {'1': 'Livre 1', '2': 'Livre 2', '3': 'Livre 3'}

dict_en_liste = list(livres_dict.items())  # Conversion de dict en liste

print(dict_en_liste)
# [('1', 'Livre 1'), ('2', 'Livre 2'), ('3', 'Livre 3')]
```

### Conversions en tuples

Toutes les structures de données peuvent être converties en un tuple en utilisant la méthode de constructeur `tuple()`, y compris un dictionnaire. Dans ce cas, nous obtenons un tuple avec les clés du dictionnaire :

```python
livres_liste = ['Livre 1', 'Livre 2', 'Livre 3']
liste_en_tuple = tuple(livres_liste)  # Conversion de liste en tuple
print(liste_en_tuple)  # ('Livre 1', 'Livre 2', 'Livre 3')


livres_ensemble = {'Livre 1', 'Livre 2', 'Livre 3'}
ensemble_en_tuple = tuple(livres_ensemble)  # Conversion d'ensemble en tuple
print(ensemble_en_tuple)  # ('Livre 1', 'Livre 2', 'Livre 3')


livres_dict = {'1': 'Livre 1', '2': 'Livre 2', '3': 'Livre 3'}
dict_en_tuple = tuple(livres_dict)  # Conversion de dict en tuple
print(dict_en_tuple)  # ('1', '2', '3')
```

### Conversions en ensembles

De même, toutes les structures de données peuvent être converties en un ensemble en utilisant la méthode de constructeur `set()`, y compris un dictionnaire. Dans ce cas, nous obtenons un ensemble avec les clés du dictionnaire :

```python
livres_liste = ['Livre 1', 'Livre 2', 'Livre 3']
liste_en_ensemble = set(livres_liste)  # Conversion de liste en ensemble
print(liste_en_ensemble)  # {'Livre 2', 'Livre 3', 'Livre 1'}


livres_tuple = ('Livre 1', 'Livre 2', 'Livre 3')
tuple_en_ensemble = set(livres_tuple)  # Conversion de tuple en ensemble
print(tuple_en_ensemble)  # {'Livre 2', 'Livre 3', 'Livre 1'}


livres_dict = {'1': 'Livre 1', '2': 'Livre 2', '3': 'Livre 3'}
dict_en_ensemble = set(livres_dict)  # Conversion de dict en ensemble
print(dict_en_ensemble)  # {'1', '3', '2'}
```

### Conversions en dictionnaires

Les conversions en dictionnaires ne peuvent pas être faites avec n'importe quel type d'ensembles, de listes ou de tuples, puisque les dictionnaires représentent des structures de données où chaque élément contient à la fois une clé et une valeur.

La conversion d'une liste ou d'un tuple en un dictionnaire peut être faite si chaque élément d'une liste est également une liste avec deux éléments, ou un tuple avec deux éléments.

```python
livres_tuple_liste = [(1, 'Livre 1'), (2, 'Livre 2'), (3, 'Livre 3')]
tuple_liste_en_dictionnaire = dict(livres_tuple_liste)  # Conversion de liste en dict
print(tuple_liste_en_dictionnaire)  # {1: 'Livre 1', 2: 'Livre 2', 3: 'Livre 3'}

livres_liste_liste = [[1, 'Livre 1'], [2, 'Livre 2'], [3, 'Livre 3']]
tuple_liste_en_dictionnaire = dict(livres_liste_liste)  # Conversion de liste en dict
print(tuple_liste_en_dictionnaire)  # {1: 'Livre 1', 2: 'Livre 2', 3: 'Livre 3'}


livres_tuple_liste = ([1, 'Livre 1'], [2, 'Livre 2'], [3, 'Livre 3'])
tuple_liste_en_ensemble = dict(livres_tuple_liste)  # Conversion de tuple en ensemble
print(tuple_liste_en_ensemble)  # {'Livre 2', 'Livre 3', 'Livre 1'}

livres_liste_liste = ([1, 'Livre 1'], [2, 'Livre 2'], [3, 'Livre 3'])
liste_liste_en_ensemble = dict(livres_liste_liste)  # Conversion de liste en ensemble
print(liste_liste_en_ensemble)  # {'Livre 2', 'Livre 3', 'Livre 1'}
```

Dans le cas où nous voulons convertir un ensemble en un dictionnaire, nous devons avoir chaque élément comme un tuple de longueur 2.

```python
livres_tuple_ensemble = {('1', 'Livre 1'), ('2', 'Livre 2'), ('3', 'Livre 3')}
tuple_ensemble_en_dict = dict(livres_tuple_ensemble)  # Conversion de dict en ensemble
print(tuple_ensemble_en_dict)  # {'1', '3', '2'}
```

Si nous essayons de faire une conversion d'un ensemble qui a chaque élément comme une liste de longueur 2 en un dictionnaire, nous allons obtenir une erreur :

```python
livres_liste_ensemble = {['1', 'Livre 1'], ['2', 'Livre 2'], ['3', 'Livre 3']}
liste_ensemble_en_dict = dict(livres_liste_ensemble)  # Conversion de dict en ensemble
print(liste_ensemble_en_dict)  # {'1', '3', '2'}
```

Après avoir exécuté le dernier bloc de code, nous allons obtenir une erreur :

```python
TypeError: type non hachable : 'list'
```

## Conclusion sur les types de données

En conclusion, Python dispose d'une variété de types de données que vous pouvez utiliser pour stocker des données. Ces types de données sont importants à connaître afin que vous puissiez choisir celui qui convient à vos besoins.

Assurez-vous d'utiliser le bon type de données pour la tâche qui se présente à vous afin d'éviter les erreurs et d'optimiser les performances.

# Contrôle de flux en Python

### Instructions conditionnelles

Lorsque vous réfléchissez aux façons dont nous pensons et communiquons également les uns avec les autres, vous pouvez avoir l'impression que nous utilisons effectivement toujours des conditions.

* Si c'est 8 heures, je prends le bus et je vais travailler.

* Si j'ai faim, je mange.

* Si cet article est bon marché, je peux me le permettre.

C'est aussi quelque chose que vous pouvez faire en programmation. Nous pouvons utiliser des conditions pour contrôler le flux de l'exécution.

Pour cela, nous utilisons le terme réservé *if* et une expression qui évalue à une valeur True ou False. Nous pouvons ensuite également utiliser une instruction *else* où nous voulons que le flux continue dans les cas où la condition *if* n'est pas remplie.

Pour faciliter la compréhension, supposons que nous avons un exemple où nous voulons vérifier si un nombre est positif :

```python
if nombre > 0:
    print("Le nombre donné est positif")
else:
    print("Le nombre donné n'est pas positif")
```

Si nous avions *nombre = 2* : nous entrerions dans la branche *if* et exécuterions la commande utilisée pour imprimer le texte suivant dans la console :

```bash
Le nombre donné est positif
```

Si nous avions un autre nombre, comme -1, nous verrions dans la console le message suivant être imprimé :

```python
Le nombre donné n'est pas positif
```

Nous pouvons également ajouter des conditions supplémentaires – et pas seulement 2 comme ci-dessus – en utilisant *elif* qui est évalué lorsque l'expression *if* n'est pas évaluée.

Voyons un exemple pour faciliter la compréhension :

```python
if nombre > 0:
    print("Le nombre donné est positif")
elif nombre == 0:
    print("Le nombre donné est 0")
else:
    print("Le nombre donné est négatif")
```

Maintenant, si nous avions *nombre = 0*, la première condition ne sera pas remplie, puisque la valeur n'est pas supérieure à 0. Comme vous pouvez le deviner, puisque le nombre donné est égal à 0, nous allons voir le message suivant imprimé dans la console :

```bash
Le nombre donné est 0
```

Dans les cas où la valeur est négative, notre programme va passer les deux premières conditions puisqu'elles ne sont pas satisfaites et sauter dans la branche *else* et imprimer le message suivant dans la console :

```bash
Le nombre donné est négatif
```

### Boucle / Itérateur

La boucle représente la capacité du programme à exécuter un ensemble d'instructions encore et encore jusqu'à ce qu'une certaine condition soit remplie. Nous pouvons le faire avec *while* et *for*.

Voyons d'abord l'itération avec *for*.

#### Boucle for en Python

Cette boucle est simple et assez directe. Tout ce que vous avez à faire est de spécifier un état de départ et de mentionner la plage dans laquelle elle doit itérer, comme vous pouvez le voir dans l'exemple suivant :

```python
for nombre in range(1, 7):
    print(nombre)
```

Dans cet exemple, nous itérons de 1 à 7 et imprimons chaque nombre (de 1 à 7 en excluant 7) dans la console.

Nous pouvons changer à la fois les nombres de début et de fin dans la plage comme nous le voulons. De cette façon, nous pouvons être assez flexibles en fonction de nos scénarios spécifiques.

#### Boucle while en Python

Décrivons maintenant les itérations avec *while*. C'est aussi une autre façon de faire des itérations qui est également assez directe et intuitive.

Ici, nous devons spécifier une condition de départ avant le bloc *while* et également mettre à jour la condition en conséquence.

La boucle **while** a besoin d'une « **condition de boucle** ». Si elle reste True, elle continue à itérer. Dans cet exemple, lorsque `num` est `11`, la **condition de boucle** est égale à `False`.

```python
nombre = 1

while nombre < 7:
    print(nombre)
    nombre += 1  # Cette partie est nécessaire pour nous à ajouter afin que l'itération ne dure pas éternellement
```

Ce bloc *while* va imprimer les mêmes déclarations que le code que nous avons utilisé avec le bloc *for*.

#### Itération : Parcourir les structures de données

Maintenant que nous avons couvert à la fois l'itération et les listes, nous pouvons sauter dans les façons de parcourir les listes.

Nous ne stockons pas simplement des choses dans des structures de données et les laissons là pendant des années. Nous devons être capables d'utiliser ces éléments dans différents scénarios.

Prenons notre liste d'étudiants d'avant :

```python
étudiants = ["Albert", "Besart", "Fisnik", "Festim", "Gazmend"]
```

Maintenant, pour parcourir la liste, nous pouvons simplement taper :

```python
for étudiant in étudiants:
    print(étudiant)
```

Oui, c'est aussi simple. Nous parcourons chaque élément de la liste et imprimons leurs valeurs.

Nous pouvons faire cela pour les dictionnaires également. Mais puisque les éléments dans les dictionnaires ont 2 parties (clé et valeur), nous devons spécifier à la fois la clé et la valeur comme suit :

```python
traduction_allemand_anglais = {
    "Wasser": "Eau",
    "Brot": "Pain",
    "Milch": "Lait"
}

for clé, valeur in traduction_allemand_anglais:
    print("Le mot allemand " + clé + " signifie " + valeur + " en anglais")
```

Nous pouvons également obtenir uniquement les clés des éléments du dictionnaire :

```python
for clé in traduction_allemand_anglais:
    print(clé)
```

Notez que *clé* et *valeur* sont simplement des noms de variables que nous avons choisis pour illustrer l'itération. Mais nous pouvons utiliser n'importe quel nom que nous voulons pour nos variables, comme dans l'exemple suivant :

```python
for mot_allemand, traduction_anglaise in traduction_allemand_anglais:
    print("Le mot allemand " + mot_allemand + " signifie " + traduction_anglaise + " en anglais")
```

Cette itération va imprimer la même chose dans la console que le bloc de code avant le dernier.

Nous pouvons également avoir des boucles for imbriquées. Par exemple, disons que nous voulons parcourir une liste de nombres et trouver une somme de chaque élément avec chaque autre élément d'une liste. Nous pouvons faire cela en utilisant des boucles `for` imbriquées :

```python
nombres = [1, 2, 3]
somme_des_nombres = []  # Liste vide

for premier_nombre in nombres:
    for deuxième_nombre in nombres:  # Parcourir la liste et ajouter les nombres
        somme_actuelle = premier_nombre + deuxième_nombre
        # ajouter le premier_nombre actuel de la première_liste au deuxième_nombre de la deuxième_liste
        somme_des_nombres.append(somme_actuelle)


print(somme_des_nombres)
# [2, 3, 4, 3, 4, 5, 4, 5, 6]
```

#### Comment arrêter une boucle for

Parfois, nous pouvons avoir besoin de sortir d'une boucle `for` avant qu'elle n'atteigne la fin. Cela peut être le cas lorsqu'une condition a été remplie ou que nous avons trouvé ce que nous cherchions et qu'il n'est pas nécessaire de continuer plus loin.

Dans ces situations, nous pouvons utiliser `break` pour arrêter toute autre itération de la boucle `for`.

Supposons que nous voulons vérifier s'il y a un nombre négatif dans une liste. Dans le cas où nous trouvons ce nombre, nous arrêtons de le chercher.

Implémentons cela en utilisant `break` :

```python
ma_liste = [1, 2, -3, 4, 0]

for élément in ma_liste:
    print("Nombre actuel : ", élément)
    if élément < 0:
        print("Nous venons de trouver un nombre négatif")
        break

# Nombre actuel :  1
# Nombre actuel :  2
# Nombre actuel :  -3
# Nous venons de trouver un nombre négatif
```

Comme nous pouvons le voir, le moment où nous atteignons -3, nous sortons de la boucle `for` et nous arrêtons.

#### Comment sauter une itération

Il peut également y avoir des cas où nous voulons sauter certaines itérations car nous ne nous y intéressons pas et qu'elles n'ont pas autant d'importance. Nous pouvons faire cela en utilisant `continue` qui empêche l'exécution du code en dessous dans ce bloc de code et déplace la procédure d'exécution vers l'itération suivante :

```python
ma_somme = 0
ma_liste = [1, 2, -3, 4, 0]

for élément in ma_liste:
    if élément < 0:  # Ne pas inclure les nombres négatifs dans la somme
        continue
    ma_somme += élément

print(ma_somme)  # 7
```

`pass` est une instruction que nous pouvons utiliser pour nous aider lorsque nous sommes sur le point d'implémenter une méthode ou autre chose mais que nous ne l'avons pas encore fait et que nous ne voulons pas obtenir d'erreurs.

Cela nous aide à exécuter le programme même si certaines parties du code sont manquantes :

```python
ma_liste = [1, 2, 3]

for élément in ma_liste:
    pass  # Ne rien faire
```

## Conclusion sur les instructions conditionnelles

En conclusion, Python offre des instructions conditionnelles pour vous aider à contrôler le flux de votre programme.

L'instruction `if` vous permet d'exécuter un bloc de code uniquement si une certaine condition est remplie. L'instruction `elif` vous permet d'exécuter un bloc de code uniquement si une autre condition est remplie. Et l'instruction `else` vous permet d'exécuter un bloc de code uniquement si aucune autre condition n'est remplie.

Ces instructions sont très utiles pour contrôler le flux de votre programme.

# Fonctions en Python

Il existe de nombreux cas où nous devons utiliser le même bloc de code encore et encore. Notre première supposition serait de l'écrire autant de fois que nous le voulons.

Objectivement, cela fonctionne, mais la vérité est que c'est une très mauvaise pratique. Nous faisons un travail répétitif qui peut être assez ennuyeux et qui est également sujet à plus d'erreurs que nous pourrions négliger.

C'est la raison pour laquelle nous devons commencer à utiliser des blocs de code que nous pouvons définir une fois et ensuite utiliser ce même code ailleurs.

Pensez simplement à cela dans la vie réelle : Vous voyez une vidéo YouTube qui a été enregistrée et téléchargée sur YouTube une fois. Elle va ensuite être regardée par de nombreuses autres personnes, mais la vidéo reste la même que celle qui a été téléchargée initialement.

En d'autres termes, nous utilisons des méthodes comme représentant un ensemble d'instructions de codage qui sont ensuite censées être appelées ailleurs dans le code et que nous n'avons pas à écrire de manière répétée.

Dans les cas où nous voulons modifier cette méthode, nous la changeons simplement à l'endroit où elle a été déclarée initialement et les autres endroits où elle est appelée n'ont rien à faire.

Pour définir une méthode en Python, nous commençons par utiliser le mot-clé `def`, puis le nom de la fonction et ensuite une liste d'arguments que nous prévoyons d'utiliser. Après cela, nous devons commencer à écrire le corps de la méthode dans une nouvelle ligne après une indentation.

```python
def additionner(premier_nombre, deuxième_nombre):
    notre_somme = premier_nombre + deuxième_nombre
    return notre_somme
```

Comme vous pouvez le voir à partir de la coloration syntaxique, `def` et `return` sont des mots-clés en Python que vous ne pouvez pas utiliser pour nommer vos variables.

Maintenant, partout où nous voulons que cette `addition()` soit appelée, nous pouvons simplement l'appeler là et ne pas avoir à nous soucier de l'implémenter entièrement.

Puisque nous avons défini cette méthode, nous pouvons l'appeler de la manière suivante :

```python
résultat = additionner(1, 5)

print(résultat)  # 6
```

Vous pourriez penser que c'est une méthode si simple et commencer à demander, pourquoi nous nous embêtons même à écrire une méthode pour cela ?

Vous avez raison. C'était une méthode très simple juste pour vous introduire à la façon dont nous pouvons implémenter des fonctions.

Écrivons une fonction qui trouve la somme des nombres qui sont entre deux nombres spécifiés :

```python
def somme_dans_plage(nombre_debut, nombre_fin):
    résultat = 0
    
    while nombre_debut < nombre_fin:
        résultat = résultat + nombre_debut
        nombre_debut = nombre_debut + 1
        
    return résultat
```

C'est maintenant un ensemble d'instructions que vous pouvez appeler à d'autres endroits et que vous n'avez pas à réécrire entièrement.

```python
résultat = somme_dans_plage(1, 5)

print(résultat)  # 10
```

Notez que les fonctions définissent une portée, ce qui signifie que les variables qui sont définies dans cette portée ne sont pas accessibles en dehors de celle-ci.

Par exemple, nous ne pouvons pas accéder à la variable nommée `produit` en dehors de la portée de la fonction :

```python
def multiplier_dans_plage(nombre_debut, nombre_fin):
    produit = 1
    while nombre_debut < nombre_fin:
        produit = produit * nombre_debut
        nombre_debut = nombre_debut + 1
    return produit
```

`produit` est accessible uniquement à l'intérieur du corps de cette méthode.

## Arguments par défaut dans les fonctions

Lorsque nous appelons des fonctions, nous pouvons rendre certains des arguments optionnels en écrivant une valeur initiale pour eux dans l'en-tête de la fonction.

Prenons un exemple où nous obtenons le prénom d'un utilisateur comme argument requis et laissons le deuxième argument optionnel.

```python
def obtenir_utilisateur(prenom, nom=""):
    return f"Salut {prenom} {nom}"
```

Nous allons maintenant appeler cette fonction avec les deux arguments :

```python
utilisateur = obtenir_utilisateur("Durim", "Gashi")

print(utilisateur)  # Salut Durim Gashi
```

Nous pouvons maintenant appeler cette même fonction même si le deuxième argument n'est pas spécifié :

```python
utilisateur = obtenir_utilisateur("Durim")

print(utilisateur)  # Salut Durim
```

## Liste d'arguments de mots-clés

Nous pouvons définir les arguments des fonctions comme des mots-clés :

```python
# Le premier argument est requis. Les deux autres sont optionnels
def obtenir_utilisateur(numéro, prenom='', nom=''):
    return f"Salut {prenom} {nom}"
```

Maintenant, nous pouvons appeler cette fonction en écrivant des arguments comme des mots-clés :

```python
utilisateur = obtenir_utilisateur(1, nom="Gashi")

print(utilisateur)  # Salut  Gashi
```

Comme vous pouvez le voir, nous pouvons omettre `prenom` puisqu'il n'est pas requis. Nous pouvons également changer l'ordre des arguments lors de l'appel de la fonction et cela fonctionnera toujours de la même manière :

```python
utilisateur = obtenir_utilisateur(1, nom="Gashi", prenom='Durim')

print(utilisateur)  # Salut Durim Gashi
```

## Cycle de vie des données

Les variables qui sont déclarées à l'intérieur d'une fonction ne peuvent pas être accessibles à l'extérieur de celle-ci. Elles sont isolées.

Voyons un exemple pour illustrer cela :

```python
def compter():
    compte = 0  # Cela n'est pas accessible à l'extérieur de la fonction.


compter()

print(compte)  # Cela va générer une erreur lors de l'exécution, puisque compte est seulement déclaré à l'intérieur de la fonction et n'est pas accessible à l'extérieur de celle-ci
```

De même, nous ne pouvons pas changer les variables à l'intérieur des fonctions qui ont été déclarées à l'extérieur des fonctions et qui ne sont pas passées comme arguments :

```python
compte = 3331


def compter():
    compte = 0  # C'est une nouvelle variable


compter()

print(compte)  # 3331
# Cela est déclaré à l'extérieur de la fonction et n'a pas été changé
```

## Comment modifier les données à l'intérieur des fonctions

Nous pouvons modifier les données mutables qui sont passées à travers une fonction comme arguments. Les données mutables représentent des données que nous pouvons modifier même après qu'elles ont été déclarées. Les listes, par exemple, sont des données mutables.

```python
noms = ["betim", "durim", "gezim"]


def capitaliser_noms(liste_actuelle):

    for i in range(len(liste_actuelle)):
        liste_actuelle[i] = liste_actuelle[i].capitalize()

    print("À l'intérieur de la fonction :", liste_actuelle)

    return liste_actuelle


capitaliser_noms(noms)  # À l'intérieur de la fonction : ['Betim', 'Durim', 'Gezim']

print("À l'extérieur de la fonction :", noms)  # À l'extérieur de la fonction : ['Betim', 'Durim', 'Gezim']
```

Dans le cas de données immuables, nous ne pouvons modifier la variable qu'à l'intérieur d'une fonction, mais la valeur réelle à l'extérieur de cette fonction va rester inchangée. Les données immuables sont les chaînes de caractères et les nombres :

```python
nom = "Betim"


def dire_bonjour(param_actuel):
    param_actuel = param_actuel + " Gashi"
    nom = param_actuel  # nom est une variable locale
    print("Valeur à l'intérieur de la fonction :", nom)
    return param_actuel


dire_bonjour(nom)  # Valeur à l'intérieur de la fonction : Betim Gashi

print("Valeur à l'extérieur de la fonction :", nom)  # Valeur à l'extérieur de la fonction : Betim
```

Si nous voulons vraiment mettre à jour les variables immuables à travers une fonction, nous pouvons assigner une valeur de retour d'une fonction à la variable immuable :

```python
nom = "Betim"


def dire_bonjour(param_actuel):
    param_actuel = param_actuel + " Gashi"
    nom = param_actuel  # nom est une variable locale
    print("Valeur à l'intérieur de la fonction", nom)
    return param_actuel


# Ici, nous assignons la valeur de nom au param_actuel qui est retourné par la fonction
nom = dire_bonjour(nom)  # Valeur à l'intérieur de la fonction Betim Gashi

# Valeur à l'extérieur de la fonction : Betim Gashi
print("Valeur à l'extérieur de la fonction :", nom)
```

## Fonctions Lambda

Les fonctions Lambda sont des fonctions anonymes que nous pouvons utiliser pour retourner une sortie. Nous pouvons écrire des fonctions lambda en utilisant le modèle de syntaxe suivant :

```python
lambda paramètres : expression
```

L'expression ne peut être écrite que sur une seule ligne.

Commençons à illustrer ces fonctions anonymes en utilisant quelques exemples.

Nous allons commencer par une fonction qui multiplie chaque entrée par 10 :

```python
dix_fois = lambda nombre : nombre * 10

print(dix_fois(10))  # 100
```

Écrivons un autre exemple dans lequel nous vérifions si l'argument donné est positif ou non :

```python
est_positif =  lambda a : f'{a} est positif' if a > 0 else f'{a} n\'est pas positif'


print(est_positif(3))  # 3 est positif

print(est_positif(-1))  # -1 n'est pas positif
```

Notez que nous ne pouvons pas utiliser la clause `if` sans la clause `else` à l'intérieur d'une fonction lambda.

À ce stade, vous pouvez vous demander, pourquoi avons-nous besoin d'utiliser des fonctions lambda, puisque elles semblent être presque les mêmes que les autres fonctions ?

Nous pouvons voir cela illustré dans la section suivante.

### Fonctions comme arguments de fonctions

Jusqu'à présent, nous avons vu des façons d'appeler des fonctions en utilisant des nombres et des chaînes. Nous pouvons en fait appeler des fonctions avec n'importe quel type d'objet Python.

Nous pouvons même fournir une fonction entière comme argument d'une fonction, ce qui peut fournir un niveau d'abstraction qui peut être assez utile.

Voyons un exemple où nous voulons faire quelques conversions d'une unité à une autre :

```python
def convertir_en_metres(pieds):
    return pieds * 0.3048


def convertir_en_pieds(metres):
    return metres / 0.3048


def convertir_en_milles(kilometres):
    return kilometres / 1.609344


def convertir_en_kilometres(milles):
    return milles * 1.609344
```

Maintenant, nous pouvons créer une fonction générale et passer une autre fonction comme argument :

```python
def conversion(operation, argument):
    return operation(argument)
```

Nous pouvons maintenant appeler `conversion()` comme ceci :

```python
resultat = conversion(convertir_en_milles, 10)

print(resultat)  # 6.2137119223733395
```

Comme vous pouvez le voir, nous avons écrit `convertir_en_milles` comme paramètre de la fonction `conversion()`. Nous pouvons utiliser d'autres fonctions déjà définies comme cela :

```python
resultat = conversion(convertir_en_pieds, 310)

print(resultat)  # 1017.0603674540682
```

Nous pouvons maintenant utiliser des lambdas et rendre ce type d'abstraction beaucoup plus simple.

Au lieu d'écrire ces quatre fonctions, nous pouvons simplement écrire une fonction lambda concise et l'utiliser comme paramètre lors de l'appel de la fonction `conversion()` :

```python
def conversion(operation, argument):
    return operation(argument)


resultat = conversion(lambda kilometres: kilometres / 1.609344, 10)

print(resultat)  # 6.2137119223733395
```

Cela est bien sûr plus simple.

Utilisons quelques autres exemples avec des fonctions intégrées.

#### Fonction `map()`

map() est une fonction intégrée qui crée un nouvel objet en obtenant des résultats en appelant une fonction sur chaque élément d'une liste existante :

```python
map(nom_de_la_fonction, ma_liste)
```

Voyons un exemple d'écriture d'une fonction lambda comme fonction d'une map.

Triplons chaque nombre dans une liste en utilisant la compréhension de liste :

```python
ma_liste = [1, 2, 3, 4]

liste_triple = [x * 3 for x in ma_liste]

print(liste_triple)  # [3, 6, 9, 12]
```

Nous pouvons implémenter cela en utilisant une fonction `map()` et une fonction lambda :

```python
ma_liste = [1, 2, 3, 4]

liste_triple = map(lambda x: x * 3, ma_liste)

print(liste_triple)  # [3, 6, 9, 12]
```

Cela crée une nouvelle liste. L'ancienne liste n'est pas modifiée.

#### Fonction `filter()`

C'est une autre fonction intégrée que nous pouvons utiliser pour filtrer les éléments d'une liste qui satisfont une condition.

Filtrons d'abord les éléments négatifs d'une liste en utilisant la compréhension de liste :

```python
ma_liste = [3, -1, 2, 0, 14]

liste_non_négative = [x for x in ma_liste if x >= 0]

print(liste_non_négative)  # [3, 2, 0, 14]
```

Maintenant, nous allons filtrer les éléments en utilisant `filter()` et une fonction lambda. Cette fonction retourne un objet que nous pouvons convertir en une liste en utilisant `list()` :

```python
ma_liste = [3, -1, 2, 0, 14]

objet_filtre_non_négatif = filter(lambda x: x >= 0, ma_liste)

liste_non_négative = list(objet_filtre_non_négatif)

print(liste_non_négative)  # [3, 2, 0, 14]
```

Vous devriez maintenant comprendre comment vous pouvez appeler des fonctions avec d'autres fonctions comme arguments et pourquoi les lambdas sont utiles et importants.

## Décorateurs en Python

Un décorateur représente une fonction qui accepte une autre fonction comme argument.

Nous pouvons le considérer comme un moyen dynamique de changer la façon dont une fonction, une méthode ou une classe se comporte sans avoir à utiliser de sous-classes.

Une fois qu'une fonction est passée comme argument à un décorateur, elle sera modifiée puis retournée comme une nouvelle fonction.

Commençons par une fonction de base que nous voulons décorer :

```python
def inverser_liste(liste_entrée):
    return liste_entrée[::-1]
```

Dans cet exemple, nous retournons simplement une liste inversée.

Nous pouvons également écrire une fonction qui accepte une autre fonction comme argument :

```python
def inverser_liste(liste_entrée):
    return liste_entrée[::-1]


def inverser_liste_entrée(autre_fonction, liste_entrée):
    # nous déléguons l'exécution à autre_fonction() 
    return autre_fonction(liste_entrée)


résultat = inverser_liste_entrée(inverser_liste, [1, 2, 3])

print(résultat)  # [3, 2, 1]
```

Nous pouvons également imbriquer une fonction à l'intérieur d'une autre fonction :

```python
def inverser_liste_entrée(liste_entrée):
    # inverser_liste() est maintenant une fonction locale qui n'est pas accessible de l'extérieur
    def inverser_liste(autre_liste):
        return autre_liste[::-1]

    résultat = inverser_liste(liste_entrée)
    return résultat               # Retourner le résultat de la fonction locale


résultat = inverser_liste_entrée([1, 2, 3])
print(résultat)  # [3, 2, 1]
```

Dans cet exemple, `inverser_liste()` est maintenant une fonction locale et ne peut pas être appelée en dehors de la portée de la fonction `inverser_liste_entrée()`.

Maintenant, nous pouvons écrire notre premier décorateur :

```python
def décorateur_inverser_liste(fonction_entrée):
    def enveloppe_fonction():
        résultat_retourné = fonction_entrée()
        liste_inversée = résultat_retourné[::-1]
        return liste_inversée

    return enveloppe_fonction
```

`décorateur_inverser_liste()` est une fonction décoratrice qui prend en entrée une autre fonction. Pour l'appeler, nous devons écrire une autre fonction :

```python
# Fonction que nous voulons décorer
def obtenir_liste():
    return [1, 2, 3, 4, 5]
```

Maintenant, nous pouvons appeler le décorateur avec notre nouvelle fonction comme argument :

```python
décorateur = décorateur_inverser_liste(obtenir_liste)  # Cela retourne une référence à la fonction

résultat_du_décorateur = décorateur()  # Ici, nous appelons la fonction réelle en utilisant des parenthèses

# Nous pouvons maintenant imprimer le résultat dans la console
print(résultat_du_décorateur)  # [5, 4, 3, 2, 1]
```

Voici l'exemple complet :

```python
def décorateur_inverser_liste(fonction_entrée):
    def enveloppe_fonction():
        résultat_retourné = fonction_entrée()
        liste_inversée = résultat_retourné[::-1]
        return liste_inversée

    return enveloppe_fonction

# Fonction que nous voulons décorer
def obtenir_liste():
    return [1, 2, 3, 4, 5]


# Cela retourne une référence à la fonction
décorateur = décorateur_inverser_liste(obtenir_liste)

# Ici, nous appelons la fonction réelle en utilisant des parenthèses
résultat_du_décorateur = décorateur()

# Nous pouvons maintenant imprimer le résultat dans la console
print(résultat_du_décorateur)  # [5, 4, 3, 2, 1]
```

Nous pouvons également appeler un décorateur en utilisant des annotations. Pour cela, nous utilisons le signe `@` avant le nom du décorateur que nous voulons appeler et le plaçons juste au-dessus du nom de la fonction :

```python
# Fonction que nous voulons décorer
@décorateur_inverser_liste  # L'annotation de la fonction décoratrice
def obtenir_liste():
    return [1, 2, 3, 4, 5]
```

Maintenant, nous pouvons simplement appeler la fonction `obtenir_liste()` et le décorateur va être appliqué :

```python
résultat_du_décorateur = obtenir_liste()

print(résultat_du_décorateur)  # [5, 4, 3, 2, 1]
```

### Comment empiler des décorateurs

Nous pouvons également utiliser plus d'un décorateur pour une seule fonction. Leur ordre d'exécution commence de haut en bas, ce qui signifie que le décorateur qui a été défini en premier est appliqué en premier, puis le deuxième, et ainsi de suite.

Faisons une simple expérience et appliquons le même décorateur que nous avons défini dans la section précédente deux fois.

Commençons par comprendre ce que cela signifie.

Nous appelons d'abord le décorateur pour inverser une liste :

`[1, 2, 3, 4, 5]` en `[5, 4, 3, 2, 1]`

Ensuite, nous l'appliquons à nouveau, mais maintenant avec le résultat retourné de l'appel précédent du décorateur :

`[5, 4, 3, 2, 1]` => `[1, 2, 3, 4, 5]`

En d'autres termes, inverser une liste puis inverser à nouveau cette liste inversée va retourner l'ordre original de la liste.

Voyons cela avec des décorateurs :

```python
@décorateur_inverser_liste
@décorateur_inverser_liste
def obtenir_liste():
    return [1, 2, 3, 4, 5]


résultat = obtenir_liste()

print(résultat)  # [1, 2, 3, 4, 5]
```

Je vais expliquer cela avec un autre exemple.

Implémentons un autre décorateur qui ne retourne que les nombres supérieurs à 1. Nous voulons ensuite inverser cette liste retournée avec notre décorateur existant.

```python
def décorateur_nombres_positifs(liste_entrée):
    def enveloppe_fonction():
        # Obtenir uniquement les nombres supérieurs à 0
        nombres = [nombre for nombre in liste_entrée() if nombre > 0]
        return nombres

    return enveloppe_fonction
```

Maintenant, nous pouvons appeler ce décorateur et l'autre décorateur que nous avons implémenté :

```python
@décorateur_nombres_positifs
@décorateur_inverser_liste
def obtenir_liste():
    return [1, -2, 3, -4, 5, -6, 7, -8, 9]


résultat = obtenir_liste()
print(résultat)  # [9, 7, 5, 3, 1]
```

Voici l'exemple complet :

```python
def décorateur_inverser_liste(fonction_entrée):
    def enveloppe_fonction():
        résultat_retourné = fonction_entrée()
        liste_inversée = résultat_retourné[::-1]  # Inverser la liste
        return liste_inversée

    return enveloppe_fonction


# Premier décorateur
def décorateur_nombres_positifs(liste_entrée):
    def enveloppe_fonction():
        # Obtenir uniquement les nombres supérieurs à 0
        nombres = [nombre for nombre in liste_entrée() if nombre > 0]
        return nombres

    return enveloppe_fonction

# Fonction que nous voulons décorer


@décorateur_nombres_positifs
@décorateur_inverser_liste
def obtenir_liste():
    return [1, -2, 3, -4, 5, -6, 7, -8, 9]


résultat = obtenir_liste()
print(résultat)  # [9, 7, 5, 3, 1]
```

### Comment passer des arguments aux fonctions décoratrices

Nous pouvons également passer des arguments aux fonctions décoratrices :

```python
def décorateur_additionner_nombres(fonction_entrée):
    def enveloppe_fonction(a, b):
        résultat = 'La somme de {} et {} est {}'.format(
            a, b, fonction_entrée(a, b))  # appel de la fonction d'entrée avec des arguments
        return résultat
    return enveloppe_fonction


@décorateur_additionner_nombres
def additionner_nombres(a, b):
    return a + b


print(additionner_nombres(1, 2))  # La somme de 1 et 2 est 3
```

#### Décorateurs intégrés

Python est livré avec plusieurs décorateurs intégrés, tels que `@classmethod`, `@staticmethod`, `@property`, et ainsi de suite. Nous couvrirons ceux-ci dans le prochain chapitre.

## Conclusion sur les fonctions

Python est un excellent langage pour écrire des fonctions car elles sont faciles à écrire.

Les fonctions lambda sont un excellent moyen de créer de petites fonctions concises en Python. Elles sont parfaites lorsque vous n'avez pas besoin d'une fonction complète, ou lorsque vous voulez simplement tester un extrait de code.

Les décorateurs Python sont un excellent moyen d'améliorer la lisibilité et la maintenabilité du code. Ils vous permettent de modulariser votre code et de le rendre plus organisé. Vous pouvez également les utiliser pour effectuer diverses tâches telles que la journalisation, la gestion des exceptions et les tests. Donc, si vous cherchez un moyen de nettoyer votre code Python, envisagez d'utiliser des décorateurs.

# Programmation orientée objet en Python

Si vous allez acheter un cookie dans un magasin local, vous allez obtenir une version du cookie qui a été produite en de nombreuses autres copies.

Il y a un emporte-pièce à cookie dans une usine qui a été utilisé pour produire un grand nombre de cookies qui sont ensuite distribués dans différents magasins où ces cookies sont ensuite servis aux clients finaux.

Nous pouvons penser à cet emporte-pièce comme un plan qui a été conçu une fois et est utilisé de nombreuses fois par la suite. Nous utilisons également ce type de plan en programmation informatique.

Un plan qui est utilisé pour créer d'innombrables autres copies est appelé une **classe**. Nous pouvons penser à une classe comme une classe appelée **Cookie**, **Factory**, **Building**, **Book**, **Pencil**, et ainsi de suite. Nous pouvons utiliser la classe de **cookie** comme un plan pour créer autant d'instances que nous voulons, que nous appelons des objets.

En d'autres termes, les plans sont des classes qui sont utilisées comme *emporte-pièces*, tandis que les cookies qui sont servis dans différents magasins sont des *objets*.

La **programmation orientée objet** représente une façon d'organiser un programme en utilisant des classes et des objets. Nous utilisons des classes pour créer des objets. Les objets interagissent les uns avec les autres.

Nous n'utilisons pas exactement le même plan pour chaque objet qui existe. Il y a un plan pour produire des livres, un autre pour produire des crayons, et ainsi de suite. Nous devons les catégoriser en fonction de leurs attributs et de leurs fonctionnalités.

Un objet créé à partir de la classe Crayon peut avoir un type de couleur, un fabricant, une épaisseur spécifique, et ainsi de suite. Ce sont les **attributs**. Un objet *crayon* peut également *écrire*, ce qui représente sa fonctionnalité, ou sa **méthode**.

Nous utilisons des classes et des objets dans différents langages de programmation, y compris Python.

Voyons à quoi ressemble une classe *Bicycle* très basique en Python :

```python
class Bicycle:
    pass
```

Nous avons utilisé le mot-clé *class* pour indiquer que nous allons commencer à écrire une classe, puis nous tapons le nom de la classe.

Nous avons ajouté le `pass` car nous ne voulons pas que l'interpréteur Python nous crie dessus en lançant des erreurs pour ne pas continuer à écrire la partie restante du code qui appartient à cette classe.

Maintenant, si nous voulons créer de nouveaux objets à partir de cette classe *Bicycle*, nous pouvons simplement écrire le nom de l'objet (qui peut être n'importe quel nom de variable que vous voulez) et l'initialiser avec la méthode constructeur *Bicycle()* qui est utilisée pour créer de nouveaux objets :

```python
favorite_bike = Bicycle()
```

Dans ce cas, *favorite_bike* est un objet qui est créé à partir de la classe *Bicycle*. Il obtient toutes les fonctionnalités et attributs de la classe Bicycle.

Nous pouvons enrichir notre classe *Bicycle* et inclure des attributs supplémentaires afin que nous puissions avoir des *bikes* personnalisés, adaptés à nos besoins.

Pour cela, nous pouvons définir une méthode constructeur appelée *init* comme suit :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike):
        self.manufacturer = manufacturer
        self.color = color
        self.is_mountain_bike = is_mountain_bike
```

Notez l'utilisation des traits de soulignement avant et après le nom `init` de la méthode. Ils représentent des indicateurs pour l'interpréteur Python pour traiter cette méthode comme une méthode spéciale.

C'est une méthode qui ne retourne rien. C'est une bonne pratique de la définir comme la première méthode de la classe, afin que les autres développeurs puissent également la voir à une ligne spécifique.

Maintenant, si nous voulons créer de nouveaux objets en utilisant ce plan de vélos, nous pouvons simplement écrire :

```python
bike = Bicycle("Connondale", "grey", True)
```

Nous avons fourni nos paramètres personnalisés pour ce vélo et les passons à la méthode constructeur. Ensuite, nous obtenons un nouveau vélo avec ces attributs spécifiques en retour. Comme vous pouvez probablement le dire, nous créons un vélo de montagne gris de la marque `Connondale`.

Nous pouvons également créer des objets à partir de classes en utilisant des arguments optionnels comme suit :

```python
class Bicycle:
    # Tous les attributs suivants sont optionnels
    def __init__(self, manufacturer=None, color='grey', is_mountain_bike=False):
        self.manufacturer = manufacturer
        self.color = color
        self.is_mountain_bike = is_mountain_bike
```

Maintenant, nous venons de créer cet objet avec ces attributs, qui ne sont actuellement pas accessibles en dehors de la portée de la classe.

Cela signifie que nous avons créé ce nouvel objet à partir de la classe *Bicycle*, mais ses attributs correspondants ne sont pas accessibles. Pour y accéder, nous pouvons implémenter des méthodes qui nous aident à y accéder.

Pour cela, nous allons définir des `getters` et des `setters`, qui représentent des méthodes que nous utilisons pour obtenir et définir les valeurs des attributs des objets. Nous allons utiliser une annotation appelée `@property` pour nous aider avec cela.

Voyons cela avec du code :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike):
        self._manufacturer = manufacturer
        self._color = color
        self._is_mountain_bike = is_mountain_bike

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer


bike = Bicycle("Connondale", "Grey", True)

print(bike.manufacturer)  # Connondale
```

Nous pouvons écrire des getters et des setters pour tous les attributs de la classe :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike):
        self._manufacturer = manufacturer
        self._color = color
        self._is_mountain_bike = is_mountain_bike

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def is_mountain_bike(self):
        return self._is_mountain_bike

    @is_mountain_bike.setter
    def is_mountain_bike(self, is_mountain_bike):
        self.is_mountain_bike = is_mountain_bike

bike = Bicycle("Connondale", "Grey", True)
```

Maintenant que nous les avons définis, nous pouvons appeler ces méthodes getters comme des attributs :

```python
print(bike.manufacturer)  # Connondale
print(bike.color)  # Grey
print(bike.is_mountain_bike)  # True
```

Nous pouvons également modifier la valeur que nous avons initialement utilisée pour n'importe quel attribut en tapant simplement le nom de l'objet et l'attribut où nous voulons changer le contenu :

```python
bike.is_mountain_bike = False
bike.color = "Blue"
bike.manufacturer = "Trek"
```

Nos classes peuvent également avoir d'autres méthodes ainsi que des getters et des setters.

Définissons une méthode à l'intérieur de la classe Bicycle que nous pouvons ensuite appeler à partir de n'importe quel objet que nous avons créé à partir de cette classe :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike):
        self._manufacturer = manufacturer
        self._color = color
        self._is_mountain_bike = is_mountain_bike

    def get_description(self):
        desc = "This is a " + self._color + " bike of the brand " + self._manufacturer
        return desc
```

Nous avons créé une méthode très simple dans laquelle nous préparons une chaîne comme résultat à partir des attributs de l'objet que nous créons. Nous pouvons ensuite appeler cette méthode comme n'importe quelle autre méthode.

Voyons cela en action :

```python
bike = Bicycle("Connondale", "Grey", True)

print(bike.get_description())  # This is a Grey bike of the brand Connondale
```

## Méthodes en Python

Les méthodes sont similaires aux fonctions, que nous avons couvertes ci-dessus.

En résumé, nous regroupons quelques instructions dans un bloc de code appelé méthode. Là, nous effectuons certaines opérations que nous nous attendons à faire plus d'une fois et que nous ne voulons pas écrire encore et encore. À la fin, nous pouvons ne pas retourner de résultat du tout.

Il existe trois types de méthodes en Python :

* méthodes d'instance

* méthodes de classe

* méthodes statiques

Parlons brièvement de la structure globale des méthodes, puis plongeons un peu plus dans le détail pour chaque type de méthode.

#### Paramètres

Les paramètres d'une méthode nous permettent de transmettre des valeurs dynamiques qui peuvent ensuite être prises en compte lors de l'exécution des instructions qui sont à l'intérieur de la méthode.

L'instruction `return` représente l'instruction qui sera la dernière à être exécutée dans cette méthode. C'est un indicateur pour l'interpréteur Python d'arrêter l'exécution de toute autre ligne et de retourner une valeur.

#### L'argument self

Le premier argument d'une méthode en Python est `self`, qui est également l'une des différences entre une méthode et une fonction. Il représente une référence à l'objet auquel il appartient. Si nous ne le spécifions pas comme premier argument de la méthode lors de sa déclaration, le premier argument est alors traité comme une référence à l'objet.

Nous l'écrivons uniquement lorsque nous déclarons la méthode, mais nous n'avons pas besoin de l'inclure lorsque nous invoquons cette méthode particulière en utilisant un objet comme appelant.

Il n'est pas requis que nous le nommions `self`, mais c'est une convention largement pratiquée par les développeurs écrivant du code Python dans le monde entier.

Définissons une méthode d'instance à l'intérieur de la classe `Bicycle` que nous pouvons ensuite appeler à partir de n'importe quel objet que nous avons créé à partir de cette classe :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike):
        self._manufacturer = manufacturer
        self._color = color
        self._is_mountain_bike = is_mountain_bike

    def get_description(self):
        desc = "This is a " + self._color + " bike of the brand " + self._manufacturer
        return desc
```

Nous avons créé une méthode très simple dans laquelle nous préparons une chaîne comme résultat à partir des attributs de l'objet que nous créons. Nous pouvons ensuite appeler cette méthode comme n'importe quelle autre méthode :

```python
bike = Bicycle("Connondale", "Grey", True)

print(bike.get_description())  # This is a Grey bike of the brand Connondale
# Nous ne passons aucun argument lors de l'appel de la méthode get_description() puisque nous n'avons pas besoin d'inclure self du tout
```

### Méthodes de classe

Nous avons couvert les méthodes d'instance jusqu'à présent. Ce sont des méthodes que nous pouvons appeler avec des objets.

Les méthodes de classe sont des méthodes que nous pouvons appeler en utilisant des noms de classe et auxquelles nous pouvons accéder sans avoir besoin de créer un nouvel objet du tout.

Puisqu'il s'agit d'un type spécifique de méthode, nous devons indiquer à l'interpréteur Python qu'elle est en fait différente. Nous faisons cela en apportant une modification à la syntaxe.

Nous utilisons l'annotation `@classmethod` au-dessus d'une méthode de classe et `cls` similaire à l'utilisation de `self` pour les méthodes d'instance. `cls` est simplement une manière conventionnelle de se référer à la classe qui appelle la méthode – vous n'avez pas à utiliser ce nom.

Déclarons notre première méthode de classe :

```python
class Article:
    blog = 'https://www.python.org/'

    # la méthode init est appelée lorsqu'une instance de la classe est créée
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def get_blog(cls):
        return cls.blog
```

Maintenant, appelons cette méthode de classe que nous venons de déclarer :

```python
print(Article.get_blog())  # https://www.python.org/
```

Notez que nous n'avons pas eu à écrire d'argument lors de l'appel de la méthode `get_blog()`. D'autre part, lorsque nous déclarons des méthodes et des méthodes d'instance, nous devons toujours inclure au moins un argument.

### Méthodes statiques

Ce sont des méthodes qui n'ont pas de relations directes avec les variables de classe ou les variables d'instance. Vous pouvez les considérer comme des fonctions utilitaires qui sont censées nous aider à faire quelque chose avec les arguments qui sont passés lors de leur appel.

Nous pouvons les appeler en utilisant à la fois le nom de la classe et un objet créé par cette classe où cette méthode est déclarée. Cela signifie qu'elles n'ont pas besoin d'avoir leur premier argument lié à l'objet ou à la classe qui les appelle (comme c'était le cas avec l'utilisation des paramètres `self` pour les méthodes d'instance et `cls` pour les méthodes de classe).

Il n'y a pas de limite au nombre d'arguments que nous pouvons utiliser pour les appeler.

Pour la créer, nous devons utiliser l'annotation `@staticmethod`.

Créons une méthode statique :

```python
class Article:
    blog = 'https://www.python.org/'

    # la méthode init est appelée lorsqu'une instance de la classe est créée
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def get_blog(cls):
        return cls.blog

    @staticmethod
    def print_creation_date(date):
        print(f'Le blog a été créé le {date}')


article = Article('Premier Article', 'Ceci est le premier article')

# Appel de la méthode statique en utilisant l'objet
article.print_creation_date('2022-07-18')  # Le blog a été créé le 2022-07-18

# Appel de la méthode statique en utilisant le nom de la classe
Article.print_creation_date('2022-07-21')  # Le blog a été créé le 2022-07-21
```

Les méthodes statiques ne peuvent pas modifier les attributs de classe ou d'instance. Elles sont censées être comme des fonctions utilitaires.

Si nous essayons de changer une classe, nous allons obtenir des erreurs :

```python
class Article:
    blog = 'https://www.python.org/'

    # la méthode init est appelée lorsqu'une instance de la classe est créée
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def get_blog(cls):
        return cls.blog

    @staticmethod
    def set_title(self, date):
        self.title = 'Un titre aléatoire'
```

Si nous essayons d'appeler cette méthode statique maintenant, nous allons obtenir une erreur :

```python
# Appel de la méthode statique en utilisant le nom de la classe
Article.set_title('2022-07-21')
```

```python
TypeError: set_title() manque 1 argument positionnel requis : 'date'
```

C'est parce que les méthodes statiques n'ont aucune référence à `self` car elles ne sont pas directement liées aux objets ou aux classes et donc elles ne peuvent pas modifier les attributs.

### Modificateur d'accès

Lors de la création de classes, nous pouvons restreindre l'accès à certains attributs et méthodes afin qu'ils ne soient pas accessibles aussi facilement.

Nous avons les modificateurs d'accès `public` et `private`.

Voyons comment les deux fonctionnent.

#### Attributs publics

Les attributs publics sont ceux qui sont accessibles à la fois à l'intérieur et à l'extérieur de la classe.

Par défaut, tous les attributs et méthodes sont publics en Python. Si nous voulons qu'ils soient privés, nous devons le spécifier.

Voyons un exemple d'attributs publics :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike):
        self.manufacturer = manufacturer
        self.color = color
        self.is_mountain_bike = is_mountain_bike

    def get_manufacturer(self):
        return self.manufacturer
```

Dans le bloc de code précédent, `color` et `get_manufacturer()` sont accessibles à l'extérieur de la classe puisqu'ils sont `public` et peuvent être accessibles à la fois à l'intérieur et à l'extérieur de la classe :

```python
bike = Bicycle("Connondale", "Grey", True)

print(bike.color)  # Grey
print(bike.get_manufacturer())  # Connondale
```

#### Attributs privés

Les attributs privés peuvent être accessibles directement uniquement à l'intérieur de la classe.

Nous pouvons rendre les propriétés des attributs en utilisant le double soulignement, comme vous pouvez le voir dans l'exemple suivant :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike, old):
        self.manufacturer = manufacturer
        self.color = color
        self.is_mountain_bike = is_mountain_bike
        self.__old = old  # C'est une propriété privée
```

Maintenant, si nous essayons d'accéder à `__old`, nous allons obtenir une erreur :

```python
bike = Bicycle("Connondale", "Grey", True, False)

print(bike.__old)  # AttributeError: l'objet 'Bicycle' n'a pas d'attribut '__old'
```

Voyons maintenant un exemple où nous déclarons des méthodes privées en utilisant le double soulignement devant le nom de la méthode que nous voulons rendre privée :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike, old):
        self.manufacturer = manufacturer
        self.color = color
        self.is_mountain_bike = is_mountain_bike
        self.__old = old  # C'est une propriété privée

    def __get_old(self):  # C'est une méthode privée
        return self.__old
```

Maintenant, si nous voulons appeler cette méthode privée depuis l'extérieur de la classe, une erreur va être lancée :

```python
bike = Bicycle("Connondale", "Grey", True, False)

print(bike.__get_old())  # AttributeError: l'objet 'Bicycle' n'a pas d'attribut '__get_old'
```

Il n'est pas courant d'avoir des variables privées en Python. Cependant, les développeurs peuvent trouver nécessaire de restreindre l'accès afin que des variables spécifiques ne soient pas accessibles et modifiées de manière négligente.

## Comment masquer des informations en Python

Lorsque vous sortez et utilisez une machine à café, vous n'êtes pas censé connaître tous les détails techniques qui se cachent derrière cette machine.

C'est la même chose avec votre voiture. Lorsque vous vous asseyez sur votre siège de conducteur, vous n'analysez pas et ne comprenez pas tous les détails de chaque partie de la voiture. Vous avez une idée de base à leur sujet, mais à part cela, vous vous concentrez simplement sur la conduite.

C'est une sorte de restriction d'accès pour les personnes extérieures, afin qu'elles n'aient pas à se soucier des détails exacts qui se passent à l'intérieur.

Nous pouvons faire cela en Python également.

Nous avons vu jusqu'à présent les blocs de base de la programmation orientée objet, tels que les classes et les objets.

Les classes sont des plans qui sont utilisés pour créer des instances appelées objets. Nous pouvons utiliser des objets de différentes classes pour interagir les uns avec les autres et construire un programme robuste.

Lorsque nous travaillons sur nos propres programmes, nous pouvons ne pas vouloir que tout le monde sache tous les détails que nos classes ont. Nous pouvons donc limiter l'accès à ceux-ci, afin que certains attributs soient moins susceptibles d'être accessibles involontairement et modifiés de manière incorrecte.

Pour nous aider avec cela, nous masquons des parties d'une classe et fournissons simplement une interface qui a moins de détails sur le fonctionnement interne de notre classe.

Nous pouvons masquer les données de deux manières :

1. Encapsulation

2. Abstraction

Commençons par l'encapsulation.

### Qu'est-ce que l'encapsulation ?

L'encapsulation n'est pas quelque chose de spécial et unique pour Python. D'autres langages de programmation l'utilisent également.

En résumé, nous pouvons la définir comme la liaison des données et des méthodes dans une classe. Nous utilisons ensuite cette classe pour créer des objets.

Nous encapsulons les classes en utilisant des modificateurs d'accès `private` qui peuvent ensuite restreindre l'accès direct à de tels attributs. Cela peut restreindre le contrôle.

Nous devons ensuite écrire des méthodes publiques qui peuvent fournir un accès au monde extérieur.

Ces méthodes sont appelées `getters` et `setters`.

Une méthode **getter** est une méthode que nous utilisons pour obtenir la valeur d'un attribut.

Un **setter** est une méthode que nous utilisons pour définir la valeur d'un attribut.

Définissons d'abord une méthode `getter` et une méthode `setter` que nous pouvons utiliser pour obtenir des valeurs :

```python
class Smartphone:
    def __init__(self, type=None):  # définition de l'initialiseur pour le cas sans argument
        self.__type = type  # définition du type ici au début lorsque l'objet est créé

    def set_type(self, value):
        self.__type = value

    def get_type(self):
        return (self.__type)
```

Maintenant, utilisons cette classe pour définir le type et également obtenir le type :

```python
smartphone = Smartphone('iPhone')  # nous définissons le type en utilisant la méthode constructeur

# obtenir la valeur du type
print(smartphone.get_type())   # iPhone

# Changer la valeur du type
smartphone.set_type('Samsung')  

# obtenir la nouvelle valeur du type
print(smartphone.get_type())    # Samsung
```

Ce que nous avons fait jusqu'à présent est de définir et également de lire la valeur d'un attribut privé d'un objet créé à partir de la classe `Smartphone`.

Nous pouvons également définir des `getters` et des `setters` en utilisant l'annotation `@property`.

Voyons cela avec du code :

```python
class Bicycle:
    def __init__(self, manufacturer, color):
        self._manufacturer = manufacturer
        self._color = color

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


bike = Bicycle("Connondale", "Grey")
```

Maintenant que nous les avons définis, nous pouvons appeler ces méthodes getters comme des attributs :

```python
print(bike.manufacturer)  # Connondale
print(bike.color)  # Grey
```

Nous pouvons également modifier la valeur que nous avons initialement utilisée pour n'importe quel attribut en tapant simplement le nom de l'objet et l'attribut que nous voulons modifier :

```python
bike.is_mountain_bike = False
bike.color = "Blue"
```

Nos classes peuvent également avoir d'autres méthodes ainsi que des getters et des setters.

Définissons une méthode à l'intérieur de la classe Bicycle que nous pouvons ensuite appeler à partir de n'importe quel objet que nous avons créé à partir de cette classe :

```python
class Bicycle:
    def __init__(self, manufacturer, color, is_mountain_bike):
        self._manufacturer = manufacturer
        self._color = color
        self._is_mountain_bike = is_mountain_bike

    def get_description(self):
        desc = "This is a " + self._color + " bike of the brand " + self._manufacturer
        return desc
```

Nous avons créé une méthode très simple dans laquelle nous préparons une chaîne comme résultat à partir des attributs de l'objet que nous créons. Nous pouvons ensuite appeler cette méthode comme n'importe quelle autre méthode.

Voyons cela en action :

```python
bike = Bicycle("Connondale", "Grey", True)

print(bike.get_description())  # This is a Grey bike of the brand Connondale
```

#### Mais pourquoi avons-nous besoin de l'encapsulation ?

Cela semble assez prometteur et élégant, mais vous ne l'avez peut-être pas encore tout à fait compris. Vous pourriez avoir besoin de raisons supplémentaires pour comprendre pourquoi vous avez besoin de ce type de masquage.

Pour illustrer cela, prenons une autre classe, où nous avons un attribut privé appelé `salary`. Supposons que nous ne nous soucions pas de l'encapsulation et que nous essayons simplement de construire une classe rapidement et de l'utiliser dans notre projet pour notre client comptable.

Supposons que nous avons la classe suivante :

```python
class Employee:
    def __init__(self, name=None, email=None, salary=None):
        self.name = name
        self.email = email
        self.salary = salary
```

Maintenant, créons un nouvel objet `employee` et initialisons ses attributs en conséquence :

```python
# Nous créons un objet
betim = Employee('Betim', 'betim@company.com', 5000)

print(betim.salary)  # 5000
```

Puisque `salary` n'est pas protégé de quelque manière que ce soit, nous pouvons définir un nouveau salaire pour cet nouvel objet sans aucun problème :

```python
betim.salary = 25000

print(betim.salary)  # 25000
```

Comme nous pouvons le voir, cette personne a obtenu cinq fois le salaire qu'elle recevait auparavant sans passer par aucun type d'évaluation ou d'entretien. En fait, cela s'est produit en quelques secondes. Cela va probablement peser lourdement sur le budget de l'entreprise.

Nous ne voulons pas faire cela. Nous voulons restreindre l'accès à l'attribut `salary` afin qu'il ne soit pas appelé d'autres endroits. Nous pouvons faire cela en utilisant le double soulignement avant le nom de l'attribut comme vous pouvez le voir ci-dessous :

```python
class Employee:
    def __init__(self, name=None, email=None, salary=None):
        self.__name = name
        self.__email = email
        self.__salary = salary
```

Créons un nouvel objet :

```python
# Nous créons un objet
betim = Employee('Betim', 'betim@company.com', 1000)
```

Maintenant, si nous essayons d'accéder à ses attributs, nous ne pouvons pas le faire, puisque ce sont des attributs privés :

```python
print(betim.salary)  # 1000
```

Tenter d'accéder à l'un des attributs sera suivi d'une erreur :

```python
AttributeError: l'objet 'Employee' n'a pas d'attribut 'salary'
```

Nous pouvons simplement implémenter une méthode qui retourne les attributs mais nous ne fournissons aucun moyen pour quelqu'un d'augmenter son salaire de manière furtive :

```python
class Employee:
    def __init__(self, name=None, email=None, salary=None):
        self.__name = name
        self.__email = email
        self.__salary = salary

    def get_info(self):
        return self.__name, self.__email, self.__salary
```

Maintenant, nous pouvons accéder aux informations des objets créés par cette classe :

```python
# Nous créons un objet
betim = Employee('Betim', 'betim@company.com', '5000')

print(betim.get_info())  # ('Betim', 'betim@company.com', '5000')
```

En résumé, l'encapsulation nous aide à protéger les propriétés des objets et à y accéder de manière contrôlée.

## Héritage en Python

Dans la vie réelle, nous pouvons partager de nombreuses caractéristiques avec d'autres êtres humains.

Nous avons tous besoin de manger de la nourriture, de boire de l'eau, de travailler, de dormir, de bouger, et ainsi de suite. Ces comportements et caractéristiques, ainsi que beaucoup d'autres, sont partagés par des milliards de personnes dans le monde entier.

Ils ne sont pas quelque chose d'unique que seule notre génération possède. Ces traits existent depuis aussi longtemps que les humains existent.

Cela va également durer pour les générations futures.

Nous pouvons également avoir certaines caractéristiques partagées entre les objets et les classes que nous implémentons nous-mêmes en programmation informatique en utilisant l'**héritage**. Cela inclut à la fois les attributs et les méthodes.

Imaginons que nous avons une classe appelée `Book`. Elle devrait contenir un titre, un auteur, un nombre de pages, une catégorie, un ISBN, et ainsi de suite. Nous allons garder notre classe simple et utiliser seulement deux attributs :

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_short_book_paragraph(self):
        short_paragraph = "This is a short paragraph of the book."
        return short_paragraph
```

Maintenant, nous pouvons créer un objet à partir de cette classe et y accéder :

```python
first_book = Book("Atomic Habits", "James Clear")

print(first_book.title)  # Atomic Habits
print(first_book.author)  # James Clear
print(first_book.get_short_book_paragraph())  # This is a short paragraph of the book.
```

Créons maintenant une sous-classe de la classe `Book` qui hérite des attributs et des méthodes de la classe `Book`, mais qui a également une méthode supplémentaire appelée `get_book_description()` :

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def get_short_book_paragraph(self):
        short_paragraph = "This is a short paragraph of the book."
        return short_paragraph

    
class BookDetails(Book):
    def __init__(self, title, author):
        Book.__init__(self, title, author)
        # Ici, nous appelons le constructeur de la classe parente Book

    def get_book_details(self):
        description = "Title: " + self.title + ". "
        description += "Author: " + self.author
        return description
```

Notez la syntaxe dans laquelle nous disons à Python que `BookDetails` est une sous-classe de la classe `Book` :

```python
class BookDetails(Book):
```

Si nous essayons d'accéder à cette nouvelle méthode à partir d'objets de la classe `Book`, nous allons obtenir une erreur :

```python
first_book = Book("Atomic Habits", "James Clear")

print(first_book.get_book_details())
# AttributeError: l'objet 'Book' n'a pas d'attribut 'get_book_details'
```

Cela se produit parce que cette méthode `get_book_details()` ne peut être accessible qu'à partir d'objets de `BookDetails` :

```python
first_book_details = BookDetails("Atomic Habits", "James Clear")

print(first_book_details.get_book_details())
# Title: Atomic Habits. Author: James Clear
```

Nous pouvons, cependant, accéder à n'importe quelle méthode qui est définie dans la classe parente, qui dans notre cas est la classe `Book` :

```python
first_book_details = BookDetails("Atomic Habits", "James Clear")

print(first_book_details.get_short_book_paragraph())
# This is a short paragraph of the book.
```

Dans les classes précédentes, `Book` est considérée comme une classe parente ou une superclasse, tandis que `BookDetails` est considérée comme une classe enfant, ou une sous-classe.

### Fonction `super()`

Il existe une fonction spéciale appelée `super()` que nous pouvons utiliser à partir d'une classe enfant pour faire référence à sa classe parente sans écrire le nom exact de la classe parente.

Nous l'utilisons avec les initialiseurs, ou lors de l'appel des propriétés ou méthodes des classes parentes.

Voyons les trois illustrés avec des exemples.

#### Comment utiliser `super()` avec les initialiseurs

Nous pouvons utiliser `super()` à l'intérieur de la méthode constructeur de la sous-classe et même appeler le constructeur de la super classe :

```python
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)  # appel du constructeur de la classe parente
        self.health = 100  # initialisation d'un nouvel attribut qui n'est pas dans la classe parente
```

Nous pouvons également remplacer `super()` par le nom de la classe parente, ce qui va fonctionner de la même manière :

```python
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(name, age)  # appel du constructeur de la classe parente
        self.health = 100  # initialisation d'un nouvel attribut qui n'est pas dans la classe parente
```

Même en changeant l'ordre des lignes à l'intérieur du constructeur de l'enfant ne causera aucune erreur du tout.

#### Comment utiliser `super()` avec les propriétés de classe de la classe parente

Nous pouvons utiliser `super()` pour accéder aux propriétés de classe de la classe parente, ce qui peut être utile surtout lorsque la classe parente et la classe enfant utilisent le même nom pour un attribut.

Pour voir cela en action, supposons que nous avons un attribut de classe appelé `name` qui est présent à la fois dans la classe parente et la classe enfant. Nous voulons accéder à cette variable à partir de la classe parente et de la classe enfant.

Pour cela, nous devons simplement écrire `super()` puis le nom de la variable :

```python
class Producer:  # classe parente
    name = 'Samsung'


class Seller(Producer):  # classe enfant
    name = 'Amazon'

    def get_product_details(self):
        # Appel de la variable de la classe parente
        print("Producer:", super().name)

        # Appel de la variable de la classe enfant
        print("Seller:", self.name)
```

Maintenant, si nous appelons la méthode `get_product_details()`, nous allons obtenir ce qui suit imprimé dans la console :

```python
seller = Seller()

seller.get_product_details()

# Producer: Samsung
# Seller: Amazon
```

#### Comment utiliser `super()` avec les méthodes de la classe parente

Nous pouvons appeler de manière similaire les méthodes de la classe parente en utilisant `super()`.

```python
class Producer:  # classe parente
    name = 'Samsung'

    def get_details(self):
        return f'Producer name: {self.name}'


class Seller(Producer):  # classe enfant
    name = 'Amazon'

    def get_details(self):
        # Appel de la méthode de la classe parente
        print(super().get_details())

        # Appel de la variable de la classe enfant
        print(f'Seller name: {self.name}')


seller = Seller()
seller.get_details()

# Producer name: Amazon
# Seller name: Amazon
```

C'est tout ce que vous devez savoir sur `super()`.

### Types d'héritage

Nous pouvons avoir différents types d'héritage en fonction de la relation des classes parentes et des classes enfants :

1. Simple

2. Multiniveau

3. Hiérarchique

4. Multiple

5. Hybride

##### 1. Héritage simple

Nous pouvons avoir une classe qui hérite uniquement d'une autre classe :

```python
class Animal:
    def __init__(self):
        self.health = 100

    def get_health(self):
        return self.health


class Cat(Animal):
    def __init__(self, name):
        super().__init__()
        self.health = 150
        self.name = name

    def move(self):
        print("Cat is moving")

cat = Cat("Cat")

# Appel de la méthode de la classe parente
print(cat.get_health())  # 150

# Appel de la méthode de la classe enfant
cat.move()  # Cat is moving
```

##### 2. Héritage multiniveau

C'est un autre type d'héritage où une classe hérite d'une autre classe qui hérite d'une autre classe : la classe A hérite de la classe B qui hérite de la classe C.

Implémentons cela en Python :

```python
class Creature:
    def __init__(self, alive):
        self.alive = alive

    def is_it_alive(self):
        return self.alive


class Animal(Creature):
    def __init__(self):
        super().__init__(True)
        self.health = 100

    def get_health(self):
        return self.health


class Cat(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def move(self):
        print("Cat is moving")


cat = Cat("Cat")

# Appel de la méthode de la classe parente de la classe parente
print(cat.is_it_alive())

# Appel de la méthode de la classe parente
print(cat.get_health())  # 150

# Appel de la méthode de la classe enfant
cat.move()  # Cat is moving
```

##### 3. Héritage hiérarchique

Lorsque nous dérivons plusieurs classes enfants de la même classe parente, nous avons alors un héritage hiérarchique. Ces classes enfants héritent de la classe parente :

```python
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return self.x, self.y


class Continent(Location):
    pass


class Country(Location):
    pass


continent = Continent(0, 0)
print(continent.get_location())  # (0, 0)

country = Country(10, 30)
print(country.get_location())  # (10, 30)
```

##### 4. Héritage multiple

Nous pouvons avoir un autre type d'héritage, à savoir l'héritage multiple qui peut nous aider à hériter de plus d'une classe en même temps.

Supposons que nous avons une classe appelée `Date` et une autre appelée `Time`.

Nous pouvons alors implémenter une autre classe qui hérite des deux classes :

```python
class Date:
    date = '2022-07-23'  # Date codée en dur

    def get_date(self):
        return self.date


class Time:
    time = '20:20:20'  # Heure codée en dur

    def get_time(self):
        return self.time


class DateTime(Date, Time):  # Héritage des deux
    def get_date_time(self):
        return self.get_date() + ' ' + self.get_time()  # obtenir des méthodes de ses classes parentes


date_time = DateTime()
print(date_time.get_date_time())  # 2022-07-23 20:20:20
```

##### 5. Héritage hybride

L'héritage hybride est une combinaison d'héritage multiple et multiniveau :

```python
class Vehicle:
    def print_vehicle(self):
        print('Vehicle')


class Car(Vehicle):
    def print_car(self):
        print('Car')


class Ferrari(Car):
    def print_ferrari(self):
        print('Ferrari')


class Driver(Ferrari, Car):
    def print_driver(self):
        print('Driver')
```

Maintenant, si nous créons un objet à partir de la classe `Driver`, nous pouvons appeler toutes les méthodes de toutes les classes :

```python
driver = Driver()

# Appel de toutes les méthodes de la sous-classe
driver.print_vehicle()  # Vehicle
driver.print_car()  # Car
driver.print_ferrari()  # Ferrari
driver.print_driver()  # Driver
```

## Polymorphisme en Python

C'est un autre concept important de la programmation orientée objet qui fait référence à la possibilité d'un objet de se comporter comme différentes formes et d'appeler différents comportements.

Un exemple de fonction intégrée qui utilise le polymorphisme est la méthode `len()` qui peut être utilisée à la fois pour les chaînes et les listes :

```python
print(len('Python'))  # 6

print(len([2, 3, -43]))  # 3
```

Nous pouvons prendre un autre exemple avec une classe appelée `House`. Nous pouvons avoir différentes sous-classes qui héritent des méthodes et des attributs de cette superclasse, à savoir des classes telles que `Condo`, `Apartment`, `SingleFamilyHouse`, `MultiFamilyHouse`, et ainsi de suite.

Supposons que nous voulons implémenter une méthode dans la classe `House` qui est censée obtenir la superficie.

Chaque type de résidence a une taille différente, donc chacune des sous-classes doit avoir des implémentations différentes.

Maintenant, nous pouvons définir des méthodes dans des sous-classes telles que :

* `getAreaOfCondo()`

* `getAreaOfApartment()`

* `getAreaOfSingleFamilyHouse()`

* `getAreaOfMultiFamilyHouse()`

Cela nous obligerait à nous souvenir des noms de chaque sous-classe, ce qui peut être fastidieux et également sujet à des erreurs lorsque nous les appelons.

Heureusement, il existe une méthode plus simple que nous pouvons utiliser qui provient du polymorphisme.

Nous pouvons avoir du polymorphisme en utilisant à la fois des méthodes et de l'héritage.

Voyons d'abord comment nous pouvons implémenter le polymorphisme en utilisant des méthodes.

### Polymorphisme utilisant des méthodes

Supposons que nous avons deux classes, à savoir `Condo` et `Apartment`. Toutes deux ont la méthode `get_area()` qui retourne une valeur.

Chacune d'entre elles aura une implémentation personnalisée.

Maintenant, la méthode que nous allons appeler dépend du type de classe de l'objet :

```python
class Condo:
    def __init__(self, area):
        self.area = area

    def get_area(self):
        return self.area


class Apartment:
    def __init__(self, area):
        self.area = area

    def get_area(self):
        return self.area
```

Créons deux objets à partir de ces classes :

```python
condo = Condo(100)

apartment = Apartment(200)
```

Maintenant, nous pouvons mettre les deux dans une liste et appeler la même méthode pour les deux objets :

```python
places_to_live = [condo, apartment]

for place in places_to_live:
    print(place.get_area())  # même méthode pour les deux objets
```

Après avoir exécuté cela, nous allons voir ce qui suit dans la console :

```bash
# 100
# 200
```

C'est ainsi que vous implémentez le polymorphisme avec des méthodes.

### Polymorphisme avec héritage

Nous pouvons non seulement appeler une méthode d'une superclasse. Nous pouvons également utiliser le même nom mais avoir une implémentation différente pour chaque sous-classe.

Définissons d'abord une superclasse :

```python
class House:
    def __init__(self, area):
        self.area = area

    def get_price(self):
        pass
```

Ensuite, nous implémenterons les sous-classes `Condo` et `Apartment` de la superclasse `House` :

```python
class House:
    def __init__(self, area):
        self.area = area

    def get_price(self):
        pass


class Condo(House):
    def __init__(self, area):
        self.area = area

    def get_price(self):
        return self.area * 100 


class Apartment(House):
    def __init__(self, area):
        self.area = area

    def get_price(self):
        return self.area * 300
```

Comme nous pouvons le voir, les deux sous-classes ont la méthode `get_price()` mais des implémentations différentes.

Nous pouvons maintenant créer de nouveaux objets à partir des sous-classes et appeler cette méthode qui va se *polymorpher* en fonction de l'objet qui l'appelle :

```python
condo = Condo(100)

apartment = Apartment(200)

places_to_live = [condo, apartment]

for place in places_to_live:
    print(place.get_price())
```

Après avoir exécuté cela, nous allons voir ce qui suit dans la console :

```bash
# 10000
# 60000
```

C'est un autre exemple de polymorphisme où nous avons une implémentation spécifique d'une méthode qui a le même nom.

# Importation en Python

L'un des principaux avantages de l'utilisation d'un langage populaire comme Python est son grand nombre de bibliothèques que vous pouvez utiliser et dont vous pouvez bénéficier.

De nombreux développeurs à travers le monde sont généreux avec leur temps et leurs connaissances et publient beaucoup de bibliothèques vraiment utiles. Ces bibliothèques peuvent nous faire gagner beaucoup de temps, tant dans notre travail professionnel que dans nos projets personnels que nous pouvons faire pour le plaisir.

Voici quelques modules avec des méthodes très utiles que vous pouvez immédiatement commencer à utiliser dans vos projets :

* `time` : Accès et conversions de temps

* `csv` : Lecture et écriture de fichiers CSV

* `math` : Fonctions mathématiques

* `email` : Créer, envoyer et traiter des emails

* `urllib` : Travailler avec des URLs

Pour importer un ou plusieurs modules, nous devons simplement écrire `import` puis le nom des modules que nous voulons importer.

Importons notre premier module :

```python
import os
```

Maintenant, importons plusieurs modules à la fois :

```python
import os, numbers, math
```

Une fois que nous avons importé un module, nous pouvons commencer à utiliser les méthodes qui s'y trouvent.

```python
import math

print(math.sqrt(81))  # 9.0
```

Nous pouvons également utiliser de nouveaux noms pour nos modules importés en spécifiant un alias pour eux `as alias` où `alias` est n'importe quel nom de variable que vous voulez :

```python
import math as math_module_that_i_just_imported

result = math_module_that_i_just_imported.sqrt(4)

print(result)  # 2.0
```

## Comment limiter ce que nous voulons importer

Il arrive que nous ne voulions pas importer un package entier avec toutes ses méthodes. Cela est dû au fait que nous voulons éviter de remplacer les méthodes ou les variables qui se trouvent dans le module par celles que nous voulons implémenter nous-mêmes.

Nous pouvons spécifier les parties que nous voulons importer en utilisant la forme suivante :

```python
from module import function
```

Prenons un exemple d'importation uniquement de la fonction racine carrée du module `math` :

```python
from math import sqrt

print(sqrt(100))  # 10.0
```

## Problèmes avec l'importation de tout depuis un module

Nous pouvons également importer tout depuis un module, ce qui peut s'avérer problématique. Illustrons cela avec un exemple.

Supposons que nous voulons importer tout ce qui est inclus dans le module `math`. Nous pouvons faire cela en utilisant l'astérisque comme ceci :

```python
from math import *  # L'astérisque est un indicateur pour inclure tout lors de l'importation
```

Maintenant, supposons que nous voulons déclarer une variable appelée `sqrt` :

```python
sqrt = 25
```

Lorsque nous essayons d'appeler la fonction `sqrt()` du module math, nous allons obtenir une erreur, puisque l'interpréteur va appeler la dernière variable `sqrt` que nous venons de déclarer dans le bloc de code précédent :

```python
print(sqrt(100))
```

```python
TypeError: l'objet 'float' n'est pas appelable
```

# Comment gérer les exceptions en Python

Lorsque nous implémentons des scripts Python ou faisons tout type d'implémentation, nous allons obtenir de nombreuses erreurs qui sont lancées même lorsque la syntaxe est correcte.

Ces types d'erreurs qui se produisent pendant l'exécution sont appelées exceptions.

Nous n'avons effectivement pas à nous rendre et à ne rien faire à leur sujet. Nous pouvons écrire des gestionnaires qui sont là pour faire quelque chose afin que l'exécution du programme ne s'arrête pas.

## Exceptions courantes en Python

Voici quelques-unes des exceptions les plus courantes qui se produisent en Python avec des définitions tirées de la [documentation Python](https://docs.python.org/3/library/exceptions.html) :

* **Exception** – Il s'agit d'une classe qui est une superclasse de la plupart des autres types d'exceptions qui se produisent.

* **NameError** – Levée lorsqu'un nom local ou global n'est pas trouvé.

* **AttributeError** – Levée lorsqu'une référence ou une affectation d'attribut échoue.

* **SyntaxError** – Levée lorsque l'analyseur rencontre une erreur de syntaxe.

* **TypeError** – Levée lorsqu'une opération ou une fonction est appliquée à un objet de type inapproprié. La valeur associée est une chaîne donnant des détails sur l'inadéquation de type.

* **ZeroDivisionError** – Levée lorsque le deuxième argument d'une opération de division ou de modulo est zéro.

* **IOError** – Levée lorsqu'une opération d'E/S (comme une instruction print, la fonction intégrée open() ou une méthode d'un objet fichier) échoue pour une raison liée à l'E/S, par exemple, « fichier non trouvé » ou « disque plein ».

* **ImportError** – Levée lorsqu'une instruction import échoue à trouver la définition du module ou lorsqu'un **from … import** échoue à trouver un nom qui doit être importé.

* **IndexError** – Levée lorsqu'un indice de séquence est hors de portée.

* **KeyError** – Levée lorsqu'une clé de mappage (dictionnaire) n'est pas trouvée dans l'ensemble des clés existantes.

* **ValueError** – Levée lorsqu'une opération ou une fonction intégrée reçoit un argument qui a le bon type mais une valeur inappropriée, et que la situation n'est pas décrite par une exception plus précise telle que IndexError.

Il existe de nombreux autres types d'erreurs, mais vous n'avez pas vraiment besoin de les connaître maintenant. Il est également très peu probable que vous voyiez tous les types d'erreurs tout le temps.

Vous pouvez voir plus de types d'exceptions dans la [documentation Python](https://docs.python.org/3/library/exceptions.html).

## Comment gérer les exceptions en Python

Commençons par un exemple très simple et écrivons un programme qui génère une erreur intentionnellement afin que nous puissions ensuite la corriger.

Nous allons faire une division par zéro, ce que vous avez probablement vu à l'école :

```python
print(5 / 0)
```

Si nous essayons d'exécuter cela, nous allons être accueillis avec l'erreur suivante dans la console :

```python
ZeroDivisionError: division par zéro
```

Si nous devions avoir de telles occurrences à l'intérieur d'un programme Python de quelque nature que ce soit, nous devrions attraper et envelopper cette erreur à l'intérieur d'un bloc `try/except`.

Nous devons écrire à l'intérieur du bloc `try` la partie du code que nous prévoyons va générer des erreurs. Nous attrapons ensuite ces types d'erreurs à l'intérieur du bloc `except` en spécifiant également le type d'erreur que nous prévoyons se produire.

Voyons le premier exemple.

Voyons comment nous pouvons gérer cette erreur afin que nous soyons également informés qu'une telle erreur s'est produite :

```python
try:
    5 / 0
except ZeroDivisionError:
    print('Vous ne pouvez pas diviser par 0 mon ami !')
```

Comme vous pouvez le voir, nous imprimons un message dans la console une fois que nous avons atteint la partie où une division par 0 se produit.

Nous pouvons également omettre la partie `ZeroDivisionError` complètement :

```python
try:
    5 / 0
except:
    print('Vous ne pouvez pas diviser par 0 mon ami !')
```

Cependant, cela n'est pas recommandé, car nous attrapons tous les types d'erreurs dans un seul bloc `except` et nous ne sommes pas sûrs du type d'erreurs qui sont attrapées (ce qui serait assez utile pour nous).

Continuons avec un autre type d'erreur.

Maintenant, nous allons essayer d'utiliser une variable qui n'est pas définie du tout :

```python
name = 'User'

try:
    person = name + surname  # surname n'est pas déclaré
except NameError:
    print('Une variable n\'est pas définie')
```

Dans l'exemple précédent, nous avons utilisé la variable `surname` avant de la déclarer, donc une `NameError` va être lancée.

Continuons avec un autre exemple qui peut être assez courant.

Lorsque nous utilisons des listes, il peut être une erreur courante d'utiliser un index qui est hors de portée. Cela signifie que l'index que nous avons utilisé est plus grand ou plus petit que la plage des index des éléments de cette liste.

Illustrons cela avec un exemple, où une `IndexError` va être lancée :

```python
ma_liste = [1, 2, 3, 4]

try:
	print(ma_liste[5])
    # Cette liste n'a que 4 éléments, donc ses index vont de 0 à 3
except IndexError:
    print('Vous avez utilisé un index qui est hors de portée')
```

Nous pouvons également utiliser un seul bloc `try` avec plusieurs erreurs `except` :

```python
ma_liste = [1, 2, 3, 4]

try:
    print(ma_liste[5])
    # Cette liste n'a que 4 éléments, donc ses index vont de 0 à 3
except NameError:
    print('Vous avez utilisé une valeur invalide')
except ZeroDivisionError:
    print('Vous ne pouvez pas diviser par zéro')
except IndexError:
    print('Vous avez utilisé un index qui est hors de portée')
```

Dans l'exemple précédent, nous essayons d'abord d'attraper s'il y a une variable utilisée mais non déclarée. Si cette erreur se produit, alors ce bloc `except` va prendre le contrôle du flux d'exécution. Ce flux d'exécution va s'arrêter là.

Ensuite, nous essayons de vérifier si nous divisons par zéro. Si cette erreur est lancée, alors ce bloc `except` va prendre le contrôle de l'exécution et tout ce qui est à l'intérieur va être exécuté. De même, nous continuons avec le reste des erreurs déclarées.

Nous pouvons également mettre plus d'une erreur entre parenthèses pour attraper plusieurs exceptions. Mais cela ne va pas être utile pour nous, puisque nous ne savons pas quelle erreur spécifique a été lancée. En d'autres termes, la méthode suivante fonctionne, mais elle n'est pas recommandée :

```python
ma_liste = [1, 2, 3, 4]

try:
    print(ma_liste[5])
    # Cette liste n'a que 4 éléments, donc ses index vont de 0 à 3
except (NameError, ZeroDivisionError, IndexError):
    print('Une NameError, ZeroDivisionError ou IndexError s\'est produite')
```

#### Le mot-clé `finally`

Après que `try` et `except` soient passés, il y a un autre bloc que nous pouvons déclarer et exécuter. Ce bloc commence par le mot-clé `finally` et il est exécuté peu importe si une erreur est lancée ou non :

```python
ma_liste = ['a', 'b']

try:
    print(ma_liste[0])
except IndexError:
    print('Une IndexError s\'est produite')
finally:
    print('Le programme se termine. Cela va être exécuté.')
```

Si nous exécutons le bloc de code précédent, nous allons voir ce qui suit dans la console :

```python
Le programme se termine. Cela va être exécuté.
```

Nous écrivons généralement du code que nous voulons comme nettoyage à l'intérieur du bloc `finally`. Cela inclut des choses comme la fermeture d'un fichier, l'arrêt d'une connexion avec une base de données, la sortie complète du programme, et ainsi de suite.

#### try, else, except

Nous pouvons écrire des instructions à l'intérieur de `try` et `except`, mais nous pouvons également utiliser un bloc `else` où nous pouvons écrire du code que nous voulons être exécuté s'il n'y a pas d'erreurs lancées :

```python
ma_liste = ['a', 'b']

try:
    print(ma_liste[0])
except IndexError:
    print('Une IndexError s\'est produite')
else:
    print('Aucune erreur ne s\'est produite. Félicitations !')
```

Si nous exécutons le code ci-dessus, nous allons obtenir ce qui suit imprimé dans la console :

```python
Aucune erreur ne s'est produite. Félicitations !
```

### Conclusion sur les exceptions

Espérons que vous comprenez maintenant les exceptions et les différentes façons dont vous pouvez les gérer. Si vous les gérez correctement, il ne devrait pas y avoir d'interruptions soudaines qui font échouer votre programme de manière inattendue.

# Saisie utilisateur en Python

Lorsque vous souhaitez développer un programme interactif et obtenir une entrée utilisateur dans la ligne de commande, vous pouvez appeler une fonction appelée `input()`.

C'est très simple et tout ce que vous avez à faire est de déclarer une variable où vous souhaitez enregistrer la valeur que l'utilisateur tape :

```python
user_input = input("Veuillez taper votre nom.")
```

Nous pouvons ensuite utiliser cette valeur et l'imprimer :

```python
print(f'Bonjour {user_input}. Heureux de vous avoir ici')
```

# Conclusion

Ce livre représente ma tentative de rendre l'apprentissage des bases de Python rapide et facile pour vous. Il y a beaucoup d'autres choses à savoir sur Python que je n'ai pas couvertes dans ce livre, mais nous allons nous arrêter ici.

J'espère que cela sera une référence utile pour vous.

Maintenant que vous avez eu l'occasion d'apprendre à écrire en Python, allez-y et faites un impact positif avec vos lignes de code.

## Obtenez le livre en PDF

Vous pouvez lire ce livre en PDF en le téléchargeant [ici](https://fatosmorina.gumroad.com/l/pythonprogramming).