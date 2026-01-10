---
title: Les listes en Python – Un guide complet
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-06-03T18:42:20.000Z'
originalURL: https://freecodecamp.org/news/lists-in-python-comprehensive-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/PYTHON-LISTS.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: Les listes en Python – Un guide complet
seo_desc: "Let’s suppose you’re planning to visit your neighborhood store to stock\
  \ up on essentials. What is the first thing you’d do? \nHave the answer already?\
  \ Yes, you'd probably write down a shopping list! Python also has a built-in data\
  \ structure called Lis..."
---

Supposons que vous prévoyez de visiter votre magasin de quartier pour faire le plein d'essentiels. Quelle est la première chose que vous feriez ?

Avez-vous déjà la réponse ? Oui, vous écrivriez probablement une liste de courses ! Python dispose également d'une structure de données intégrée appelée `List` qui est très similaire à votre liste de courses.

Cet article est un tutoriel convivial pour les débutants sur les listes Python. Au cours des prochaines minutes, nous allons découvrir les listes et couvrir certaines des opérations les plus courantes telles que le découpage des listes et leur modification à l'aide des méthodes de liste.

Alors, allons-y et apprenons-en plus sur les listes Python et voyons comment elles sont analogues à notre liste de courses.

> Entrons et faisons les courses ensemble !

## Comment fonctionnent les listes en Python

Il est tout à fait naturel d'écrire les articles d'une liste de courses les uns en dessous des autres. Pour que Python reconnaisse notre liste, nous devons enfermer tous les éléments de la liste entre crochets `([ ])`, les éléments étant _séparés par des virgules_.

Voici un exemple où nous créons une liste avec 6 articles que nous aimerions acheter.

```python
liste_de_courses = ['pommes','stylos','biscuits à l'avoine','bloc-notes','brosses','peinture']

```

## Mutabilité des listes en Python

De la même manière que nous pouvons toujours modifier notre liste de courses en réorganisant les articles – faire des choses comme remplacer `biscuits à l'avoine` par notre `bonbon` préféré, par exemple – nous pouvons faire de même avec les listes Python.

Pour cette raison, les listes sont **mutables**. Voici comment nous pouvons remplacer `biscuits à l'avoine` par `bonbon` dans notre liste.

```python
liste_de_courses[2] = 'bonbon'
print(liste_de_courses)
# Sortie
>> ['pommes', 'stylos', 'bonbon', 'bloc-notes', 'brosses', 'peinture']
```

### Indexation dans les listes Python

Avez-vous remarqué que `biscuits à l'avoine` est le troisième élément de la liste, mais est à l'index `2` ? Eh bien, c'est à cause de l'**indexation à zéro**. En Python, l'**`index`** est essentiellement un _décalage par rapport au début de la liste_.

> C'est pourquoi le premier élément est à l'index `0` (aucun décalage), le deuxième élément est à l'index `1`, et ainsi de suite. En général, si la liste a n éléments, le dernier élément est à l'index `(n-1)`.

Si nous essayons d'accéder à un élément à un index invalide, nous obtiendrons une `IndexError`.

Dans notre exemple, notre liste de courses a 6 éléments (la plage d'index va de 0 à 5). Comme le montre l'extrait de code ci-dessous, si nous essayons d'accéder à un élément à `index = 6`, nous obtiendrions une erreur car il n'y a pas d'élément à l'index `6`.

```python
print(liste_de_courses[6])
# Sortie
>> --------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-21-a9f3b9517136> in <module>()
----> 1 liste_de_courses[6]

IndexError: list index out of range
```

D'autre part, nous pouvons également utiliser l'**indexation négative**. Le _dernier élément_ est à l'index `-1`, l'_avant-dernier élément_ est à l'index `-2` et ainsi de suite.

```python
print(liste_de_courses[-1])
# Sortie
>> peinture
```

Tout comme notre liste de courses pourrait contenir des articles de n'importe quel type tels que des fruits, des légumes, des sucreries et plus encore, une liste Python pourrait également contenir des _articles de n'importe quel type_.

Cela dit, il est tout à fait normal qu'une liste contienne une autre petite liste comme l'un de ses éléments. Ce processus est appelé imbrication et de telles listes sont appelées listes imbriquées.

Voici un exemple où notre liste de courses contient deux listes plus petites.
 `ma_liste_imbriquée = [['pomme','banane'],['peinture','brosses']]`

## Comment parcourir les listes en Python

Il est assez courant de parcourir notre `liste_de_courses` pour vérifier si nous avons acheté tout ce dont nous avons besoin. Cela s'appelle parcourir la liste.

En Python, vous pouvez le faire en utilisant des boucles et l'opérateur `in`.

```python
for article in liste_de_courses:
  print(article)
# Sortie 
pommes
stylos
bonbon
bloc-notes
brosses
peinture
```

Si nous devions effectuer certaines opérations sur la liste, il est recommandé d'utiliser `range` pour obtenir un ensemble d'index que nous pouvons ensuite parcourir.

## Comment découper les listes en Python

Et si nous étions intéressés à ne regarder qu'un sous-ensemble de notre `liste_de_courses` ? Cela nécessiterait de découper la liste et de récupérer un sous-ensemble d'articles.

Voici un modèle général : `nom_liste[index_début:index_fin +1]`. Essayons maintenant de l'analyser.

* Si nous avons besoin d'une partie de la liste jusqu'à `index_fin`, spécifiez `index_fin + 1` lors de la spécification des index de début et de fin.
* L'`index_début` par défaut est `0`, et l'`index_fin` par défaut est l'index du dernier élément de la liste.
* Si nous ne spécifions pas l'`index_début`, la partie commence à partir du premier élément de la liste.
* Si nous ne spécifions pas l'`index_fin`, la partie s'étend jusqu'au dernier élément de la liste.
* Si nous ne spécifions pas ces deux index, alors la partie retournée est la liste entière.

L'extrait de code suivant illustre cela.

```python
print(liste_de_courses[2:])
# Sortie
>> ['bonbon', 'bloc-notes', 'brosses', 'peinture']

print(liste_de_courses[:2])
# Sortie
>> ['pommes', 'stylos']

print(liste_de_courses[:])
# Sortie
>> ['pommes', 'stylos', 'bonbon', 'bloc-notes', 'brosses', 'peinture']
```

## Comment opérer sur les listes en Python

Vous pouvez appliquer des fonctions intégrées courantes telles que `len()`, `min()` et `max()` sur les listes pour obtenir la longueur de la liste, l'élément minimum et l'élément maximum, respectivement.

Comme notre `liste_de_courses` ne contient que des chaînes de caractères, `min()` retourne la chaîne qui apparaît en premier lorsque la liste est triée lexicographiquement. `max()` retourne la chaîne qui apparaît en dernier.

Vous pouvez voir l'extrait de code pour cette section ci-dessous.

```python
print(len(liste_de_courses))
>> 6

print(max(liste_de_courses))
>> stylos

print(min(liste_de_courses))
>> pommes
```

Nous pouvons créer une nouvelle liste en concaténant des listes existantes, tout comme nous pouvons toujours assembler deux petites listes de courses pour créer une nouvelle liste.

```python
liste_2 = liste_de_courses + ['nouilles','amandes']
print(liste_2)

>> ['pommes', 'stylos', 'bonbon', 'bloc-notes', 'brosses', 'peinture', 'nouilles', 'amandes']
```

## Méthodes de liste Python

En plus des fonctions intégrées qui peuvent opérer sur les listes, Python dispose de plusieurs méthodes de liste qui nous aident à effectuer des opérations utiles sur les listes.

Considérons notre `liste_de_courses`. Quelles sont les opérations courantes que nous effectuerions probablement sur notre liste ? Listons-en quelques-unes :

* Ajouter un ou plusieurs éléments à notre `liste_de_courses`
* Supprimer un ou plusieurs éléments de notre `liste_de_courses`
* Réorganiser les éléments de notre `liste_de_courses`

### Comment ajouter des éléments à une liste en Python

Nous pouvons ajouter des éléments, un à la fois, à la fin de la liste en utilisant la méthode `append()`. Ajoutons `raisins` à notre `liste_de_courses`.

```python
liste_de_courses.append('raisins')
print(liste_de_courses)

>> ['pommes', 'stylos', 'bonbon', 'bloc-notes', 'brosses', 'peinture', 'raisins']
```

Et si nous avions une autre liste (ou tout autre itérable) que nous voulions ajouter à une liste existante ? Au lieu d'ajouter les éléments de la nouvelle liste un par un, nous pourrions utiliser la méthode `extend()` pour ajouter la liste entière à la première liste comme montré ci-dessous.

```python
liste_de_courses.extend(['barres protéinées','fromage'])
print(liste_de_courses)

>> ['pommes', 'stylos', 'bonbon', 'bloc-notes', 'brosses', 'peinture', 'raisins', 'barres protéinées', 'fromage']
```

**Note** : Il existe une différence inhérente entre les méthodes de liste `append()` et `extend()` et l'opérateur '+' pour concaténer deux listes.

Alors que l'opérateur '+' crée une nouvelle liste en combinant les listes que nous spécifions comme opérandes, les méthodes `append()` et `extend()` modifient la liste sur laquelle elles sont appelées (invoquées) et ne retournent pas une nouvelle liste.

### Comment supprimer des éléments d'une liste en Python

Nous pouvons supprimer des éléments d'une liste, soit un seul élément soit un groupe, en utilisant les méthodes suivantes.

La méthode `pop()` retourne le dernier élément de la liste et le supprime également, comme montré ci-dessous. `fromage` était le dernier élément de la liste, et il est maintenant supprimé.

```python
dernier_element = liste_de_courses.pop()
print(liste_de_courses)
print(dernier_element)
# Sortie
>> ['pommes', 'stylos', 'bonbon', 'bloc-notes', 'brosses', 'peinture', 'raisins', 'barres protéinées']
>> fromage
```

Si nous voulons supprimer un élément à un index particulier, nous pouvons spécifier l'`index` comme argument de `pop()`.

```python
pas_besoin = liste_de_courses.pop(2)
print(pas_besoin)
# Sortie
>> bonbon
```

Si nous n'avons pas besoin d'accéder à la valeur de l'élément de liste supprimé, nous pouvons choisir d'utiliser la fonction `del` à la place.

Nous pouvons supprimer un élément à un index particulier en spécifiant cet index, ou nous pouvons supprimer tous les éléments d'une partie de liste en découpant la liste comme expliqué dans la section précédente.

```python
del liste_de_courses[1]
print(liste_de_courses)
# Sortie
>> ['pommes', 'bloc-notes', 'brosses', 'peinture', 'raisins', 'barres protéinées']
```

Supposons que nous connaissons l'article que nous n'avons plus besoin d'acheter mais que nous ne savons pas à quel index se trouve l'article. Dans ces cas, nous pouvons utiliser la méthode `remove()` pour supprimer un article par son nom.

Dans notre exemple, l'article à l'index `1` dans notre copie la plus récente est `stylos`. Si nous ne connaissions pas l'index de `stylos`, nous pourrions écrire `liste_de_courses.remove('stylos')` pour effectuer la même tâche que dans l'extrait de code ci-dessus.

Pour supprimer tous les éléments d'une liste, nous pouvons utiliser `nom_liste.clear()`.

**Note** : Si nous essayons de supprimer un élément qui n'existe pas dans la liste, nous obtiendrions une `ValueError`.

## Comment trier une liste en Python

Nous pouvons choisir de trier notre `liste_de_courses` en appelant la méthode `sort()`. Comme notre liste ne contient que des chaînes de caractères, `sort()` triera notre liste par ordre alphabétique. Si nous avons une liste de nombres, les éléments seront triés par ordre croissant par défaut.

Si vous souhaitez trier par ordre décroissant, définissez l'argument optionnel `reverse = True`.

**Note** : L'appel de la méthode `sort()` modifie la liste existante et ne crée pas de nouvelle liste. Si vous souhaitez avoir une nouvelle liste triée tout en conservant la liste existante telle quelle, utilisez plutôt la méthode `sorted()`.

```python
liste_de_courses.sort()
print(liste_de_courses)
# Sortie
>> ['pommes', 'brosses', 'raisins', 'bloc-notes', 'peinture', 'barres protéinées']
```

Une autre méthode utile est `count` que vous pouvez utiliser pour vérifier combien de fois un article spécifique apparaît dans notre liste. `nom_liste.count(elt)` retourne le nombre de fois où `elt` apparaît dans la liste `nom_liste`.

## Récapitulatif

⏸ Il est maintenant temps pour un rapide récapitulatif. Regardez l'image ci-dessous et vérifiez si vous êtes capable de vous rappeler ce que nous avons lu jusqu'à présent.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/lists-recap.png)

📌 Voici une autre feuille de référence utile que j'ai préparée pour les méthodes de liste que vous pourriez enregistrer pour votre référence.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/lmcc.png)

À bientôt dans un autre article sur Python.👋 En attendant, bon apprentissage et bon codage !

### Références

[1] [Python for Everybody](https://www.freecodecamp.org/learn/scientific-computing-with-python/) sur freeCodeCamp

[2] [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)