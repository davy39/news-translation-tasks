---
title: Comment jouer et gagner au Sudoku - Utiliser les mathématiques et l'apprentissage
  automatique pour résoudre chaque énigme de Sudoku
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-10-04T21:45:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-play-and-win-sudoku-using-math-and-machine-learning-to-solve-every-sudoku-puzzle
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/relaxation-2040676_1920-1.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Python
  slug: python
seo_title: Comment jouer et gagner au Sudoku - Utiliser les mathématiques et l'apprentissage
  automatique pour résoudre chaque énigme de Sudoku
seo_desc: 'Sudoku (and its predecessors) has been played for over a hundred years.
  When it first came out people had to actually solve the puzzles using only their
  minds. Now we have computers! (Ok, so most people still just use their minds...)

  In this article,...'
---

Le Sudoku (et ses prédécesseurs) est joué depuis plus de cent ans. Lorsqu'il est sorti pour la première fois, les gens devaient résoudre les énigmes en utilisant uniquement leur esprit. Maintenant, nous avons des ordinateurs ! (D'accord, la plupart des gens utilisent encore leur esprit...)

Dans cet article, vous apprendrez à jouer et à gagner au Sudoku. Mais plus important encore, vous apprendrez à utiliser l'apprentissage automatique pour résoudre facilement chaque énigme de Sudoku. Qui a besoin de réfléchir quand on peut laisser l'ordinateur réfléchir à votre place ? 💡

Peter Norvig a développé un programme élégant utilisant Python pour gagner au Sudoku en utilisant la propagation de contraintes et la recherche. La solution de Norvig est considérée comme un classique et est souvent citée lorsque les gens développent leur propre code pour jouer au Sudoku. Après avoir passé en revue le Sudoku et quelques stratégies, je vais décomposer le code de Norvig étape par étape pour que vous puissiez comprendre comment il fonctionne.

## Qu'est-ce que le Sudoku ?

Le Sudoku est un puzzle de placement de nombres et il existe plusieurs types différents. Cet article traite du type le plus populaire.

L'objectif est de remplir une grille de 9x9 avec des chiffres (1-9) de sorte que chaque colonne, chaque ligne et chacun des neuf sous-grilles de 3x3 (également appelés boxes) contiennent chacun des chiffres de 1 à 9. Les puzzles commencent avec certains nombres déjà sur la grille et c'est à vous de remplir les autres nombres.

Dans l'image ci-dessous d'un jeu de Sudoku, le nombre qui devrait aller dans le carré surligné en bleu ne peut pas être dans l'un des carrés jaunes correspondant à la colonne, à la ligne et à la boîte de 3x3.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-216.png)

## Comment résoudre le Sudoku

Lors de la résolution d'un puzzle de Sudoku, vous devez constamment faire deux choses. La première chose à faire est d'éliminer les nombres des lignes, des colonnes et des boxes (sous-grilles de 3x3). La deuxième chose à faire est de chercher un seul candidat.

Dans l'exemple ci-dessous, les nombres possibles pour chaque carré sont notés en petite police. Les nombres possibles ont été déterminés en éliminant tous les chiffres qui apparaissent dans la même colonne, ligne ou boîte. La plupart des gens détermineront le nombre possible pour une boîte à la fois, au lieu de le faire pour toute la grille.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-212.png)

Après avoir éliminé les nombres, vous pouvez chercher des candidats uniques. Cela signifie trouver un carré qui ne peut être qu'un seul nombre possible. Dans l'exemple ci-dessous, les deux carrés surlignés en jaune doivent contenir **1** et **8** parce que tous les autres chiffres ont été éliminés puisqu'ils apparaissent déjà dans la colonne, la ligne ou la boîte du carré.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-213.png)

Maintenant que les deux carrés surlignés en jaune sont connus, cela élimine plus de possibilités des autres carrés. Maintenant, vous savez que le carré surligné en bleu doit être 7.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-217.png)

Si vous continuez à trouver les candidats uniques et à éliminer les options des autres carrés, vous atteindrez peut-être un point où il n'y a plus de candidats uniques.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-218.png)

À ce stade, vous pouvez chercher des solutions possibles pour les carrés où le nombre n'est que dans un seul carré dans une boîte, une ligne ou une colonne. Dans l'exemple ci-dessous, nous pouvons déterminer que la solution pour le carré surligné en bleu doit être 6 puisque le nombre 6 n'apparaît dans aucun autre carré de la boîte jaune.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-220.png)

Parfois, le plateau atteint un état où il semble que chaque carré non résolu pourrait potentiellement avoir plusieurs valeurs. Cela signifie qu'il y a plusieurs chemins que vous pourriez choisir et il n'est pas évident de savoir quel chemin mènera à la résolution du puzzle.

À ce stade, il est nécessaire d'essayer chaque option. Choisissez-en une et continuez à résoudre jusqu'à ce qu'il devienne clair que l'option que vous avez choisie ne peut pas être une solution. Vous devrez alors revenir en arrière et essayer une autre option.

Ce type de recherche peut être facilement effectué avec un ordinateur en utilisant un arbre de recherche binaire. Lorsqu'il y a l'option de deux nombres différents pour résoudre un carré, il est nécessaire de se ramifier en deux possibilités différentes. Un arbre de recherche binaire permettra à un algorithme de descendre une branche de choix, puis d'essayer une autre branche de choix.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-221.png)
_Représentation de l'arbre de recherche binaire_

Maintenant, nous allons voir le code Python qui peut résoudre les puzzles de Sudoku en utilisant une méthode similaire à celle qui vient d'être décrite.

## Le programme de Peter Norvig pour gagner au Sudoku

Peter Norvig a expliqué son approche pour résoudre le Sudoku et le code qu'il a utilisé dans son article [Résoudre chaque puzzle de Sudoku](http://www.norvig.com/sudoku.html).

Certains peuvent trouver son explication un peu difficile à suivre, surtout les débutants. Je vais décomposer les choses pour qu'il soit plus facile de comprendre comment fonctionne le code de Norvig.

Dans cet article, le code Python 2 de Norvig a été mis à jour vers Python 3. (Conversion Python 3 par [Naoki Shibuya](https://medium.com/activating-robotic-minds/peter-norvigs-sudoku-solver-25779bb349ce).) Je vais passer en revue le code quelques lignes à la fois, mais vous pouvez voir le code complet à la fin de cet article. Pour certaines personnes, il peut être utile de parcourir le code complet avant de continuer la lecture.

Tout d'abord, nous allons couvrir la configuration de base et la notation. Voici comment Norvig décrit la notation de base qu'il utilise dans son code :

> Un puzzle de Sudoku est une _**grille**_ de 81 carrés ; la majorité des passionnés étiquetent les colonnes de 1 à 9, les lignes de A à I, et appellent une collection de neuf carrés (colonne, ligne ou boîte) une _**unité**_ et les carrés qui partagent une unité les _**pairs**_.

Voici les noms des carrés :

```
 A1 A2 A3| A4 A5 A6| A7 A8 A9
 B1 B2 B3| B4 B5 B6| B7 B8 B9
 C1 C2 C3| C4 C5 C6| C7 C8 C9
---------+---------+---------
 D1 D2 D3| D4 D5 D6| D7 D8 D9
 E1 E2 E3| E4 E5 E6| E7 E8 E9
 F1 F2 F3| F4 F5 F6| F7 F8 F9
---------+---------+---------
 G1 G2 G3| G4 G5 G6| G7 G8 G9
 H1 H2 H3| H4 H5 H6| H7 H8 H9
 I1 I2 I3| I4 I5 I6| I7 I8 I9
```

Norvig définit les chiffres, les lignes et les colonnes comme des chaînes de caractères :

```python
digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
```

Vous remarquerez que `cols` est défini pour être égal à `digits`. Bien qu'ils aient la même valeur, ils représentent des choses différentes. La variable `digits` représente les chiffres qui vont dans un carré pour résoudre le puzzle. La variable `cols` représente les noms des colonnes de la grille.

Les carrés sont également définis comme des chaînes de caractères, mais les chaînes sont créées avec une fonction :

```python
def cross(A, B):
    "Produit cartésien des éléments dans A et des éléments dans B."
    return [a+b for a in A for b in B]

squares  = cross(rows, cols)
```

La partie de retour de la fonction `cross` (`[a+b for a in A for b in B]`) est simplement une manière élégante d'écrire ce code :

```python
squares = []
for a in rows:
    for b in cols:
        squares.append(a+b)
```

La variable `squares` est maintenant égale à une liste de tous les noms de carrés.

```python
['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
```

Chaque carré de la grille a 3 unités et 20 pairs. Les unités d'un carré sont la ligne, la colonne et la boîte dans lesquelles il apparaît. Les pairs d'un carré sont tous les autres carrés dans les unités. Par exemple, voici les unités et les pairs pour le carré C2 :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-222.png)

Toutes les unités pour chaque carré sont créées en utilisant la fonction `cross` avec le code suivant :

```python
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
```

En Python, un dictionnaire est une collection de paires clé-valeur. Les lignes de code suivantes créent des dictionnaires qui utilisent les noms des carrés comme clés et les trois unités ou les 20 pairs comme valeurs.

```python
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)
```

Maintenant, les 3 unités de 'C2' peuvent être accessibles avec `units['C2']` et donneront le résultat suivant :

```python
[['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
```

Ensuite, nous aurons besoin de deux représentations de la grille de jeu Sudoku complète. Un format textuel nommé `grid` sera l'état initial du puzzle. Une autre représentation de la grille sera également nécessaire pour décrire en interne l'état actuel d'un puzzle. Elle gardera une trace de toutes les valeurs possibles restantes pour chaque carré et sera nommée `values`.

Similaire à `units` et `peers`, `values` sera un dictionnaire avec des carrés comme clés. La valeur de chaque clé sera une chaîne de chiffres qui sont les chiffres possibles pour le carré. Si le chiffre était donné dans le puzzle ou a été trouvé, il n'y aura qu'un seul chiffre dans la clé. Par exemple, s'il y a une grille où A1 est 6 et A2 est vide, `values` ressemblerait à `{'A1': '6', 'A2': '123456789', ...}`.

## Fonctions Parse Grid et Grid Values

La fonction `parse_grid` (code ci-dessous) convertit la grille en un dictionnaire de valeurs possibles. La fonction `grid_values` extrait les valeurs importantes qui sont des chiffres, `0`, et `.`. Dans le dictionnaire `values`, les carrés sont les clés et les chiffres donnés dans la grille sont les valeurs.

Pour chaque carré avec une valeur donnée, la fonction `assign` est utilisée pour assigner la valeur au carré et éliminer la valeur des pairs. La fonction `assign` est couverte bientôt. Si quelque chose ne va pas, la fonction retourne False.

Voici le code pour les fonctions `parse_grid` et `grid_values`.

```python
def parse_grid(grid):
    """Convertir la grille en un dictionnaire de valeurs possibles, {square: digits}, ou
    retourner False si une contradiction est détectée."""
    ## Pour commencer, chaque carré peut être n'importe quel chiffre ; puis assigner les valeurs de la grille.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Échec si nous ne pouvons pas assigner d au carré s.)
    return values

def grid_values(grid):
    "Convertir la grille en un dictionnaire de {square: char} avec '0' ou '.' pour les vides."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))
```

## Propagation de contraintes

Les valeurs initiales pour les carrés seront soit des chiffres spécifiques (1-9), soit une valeur vide. Nous pouvons appliquer des contraintes à chaque carré et éliminer les valeurs qui sont impossibles. Norvig utilise deux stratégies pour aider à déterminer les valeurs correctes pour les carrés (qui correspondent aux stratégies ci-dessus) :

> _(1) Si un carré n'a qu'une seule valeur possible, alors éliminer cette valeur des pairs du carré._
> _(2) Si une unité n'a qu'un seul emplacement possible pour une valeur, alors placer la valeur là._

Un exemple de la première stratégie est que si nous savons que A1 a une valeur de 5, alors 5 peut être retiré de tous les 20 de ses pairs.

Voici un exemple de la deuxième stratégie : si l'on peut déterminer qu'aucun de A1 à A8 ne contient 9 comme valeur possible, alors nous pouvons être sûrs que A9 a une valeur de 9 puisque 9 doit apparaître quelque part dans l'unité.

Chaque fois qu'un carré est mis à jour, cela provoquera des mises à jour possibles de tous ses pairs. Ce processus continuera et est appelé **propagation de contraintes**.

## Fonction Assign

La fonction `assign(values, s, d)` est appelée à l'intérieur de la fonction `parse_grid`. Elle retourne les valeurs mises à jour. Elle accepte trois arguments : `values`, `s`, et `d`.

Rappelons que `values` est un dictionnaire qui associe chaque carré à toutes les valeurs de chiffres possibles pour ce carré. `s` est le carré auquel nous assignons une valeur et `d` est la valeur qui doit être assignée au carré. Au début, `d` provient du puzzle donné que nous résolvons.

Elle appelle la fonction `eliminate(values, s, d)` pour éliminer toutes les valeurs de s sauf d.

S'il y a une contradiction, comme deux carrés auxquels est assigné le même nombre, la fonction eliminate retournera False.

```python
def assign(values, s, d):
    """Éliminer toutes les autres valeurs (sauf d) de values[s] et propager.
    Retourner values, sauf retourner False si une contradiction est détectée."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
```

## Fonction Eliminate

Nous avons vu que la fonction `assign` appelle la fonction `eliminate`. La fonction eliminate est appelée comme ceci : `eliminate(values, s, d2) for d2 in other_values)`

La fonction `eliminate` éliminera les valeurs que nous savons ne pas pouvoir être une solution en utilisant les deux stratégies mentionnées ci-dessus. La première stratégie est que lorsqu'il n'y a qu'une seule valeur potentielle pour `s`, cette valeur est retirée des pairs de `s`. La deuxième stratégie est que lorsqu'il n'y a qu'un seul emplacement où une valeur `d` peut aller, cette valeur est retirée de tous les pairs.

Voici la fonction complète :

```python
def eliminate(values, s, d):
    """Éliminer d de values[s] ; propager lorsque les valeurs ou les emplacements <= 2.
    Retourner values, sauf retourner False si une contradiction est détectée."""
    if d not in values[s]:
        return values ## Déjà éliminé
    values[s] = values[s].replace(d,'')
    ## (1) Si un carré s est réduit à une valeur d2, alors éliminer d2 des pairs.
    if len(values[s]) == 0:
        return False ## Contradiction : dernière valeur retirée
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) Si une unité u est réduite à un seul emplacement pour une valeur d, alors la placer là.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction : aucun emplacement pour cette valeur
        elif len(dplaces) == 1:
        # d ne peut être qu'à un seul emplacement dans l'unité ; l'assigner là
            if not assign(values, dplaces[0], d):
                return False
    return values
```

## Fonction Display

La fonction `display` affichera le résultat après l'appel de `parse_grid`.

```python
def display(values):
    "Afficher ces valeurs sous forme de grille 2-D."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': 
            print(line)
    print()
```

Voici un exemple de ce à quoi ressemblera la grille après l'appel de la fonction display après avoir analysé une grille qui est un puzzle difficile.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-5.png)

Vous remarquerez que beaucoup de carrés ont plusieurs valeurs potentielles, tandis que certains sont complètement résolus. La grille ci-dessus est le résultat de l'application mécanique des deux stratégies ci-dessus. Mais comme vous pouvez le voir, ces stratégies seules ne suffisent pas à résoudre complètement le puzzle.

## Recherche

Il existe de nombreuses façons de résoudre un problème de Sudoku, mais certaines sont beaucoup plus efficaces que d'autres. Norvig suggère un type spécifique d'algorithme de recherche.

L'algorithme de recherche fait quelques choses. Tout d'abord, il s'assure qu'aucune solution ou contradiction n'a déjà été trouvée. Ensuite, il choisit un carré non rempli et considère toutes les valeurs qui sont encore possibles. Enfin, une par une, il essaie d'assigner chaque valeur au carré et recherche à partir de la position résultante.

L'ordre des variables est utilisé pour choisir quel carré commencer à explorer. Voici comment Norvig le décrit :

> nous utiliserons une heuristique courante appelée minimum de valeurs restantes, ce qui signifie que nous choisissons le (ou l'un des) carré avec le nombre minimum de valeurs possibles. Pourquoi ? Considérons grid2 ci-dessus. Supposons que nous choisissons B3 en premier. Il a 7 possibilités (1256789), donc nous nous attendons à nous tromper avec une probabilité de 6/7. Si au lieu de cela nous choisissons G2, qui n'a que 2 possibilités (89), nous nous attendons à nous tromper avec une probabilité de seulement 1/2. Ainsi, nous choisissons le carré avec le moins de possibilités et la meilleure chance de deviner correctement.

Les chiffres sont considérés dans l'ordre numérique.

Voici la fonction `search`, ainsi que la fonction `solve` qui analyse la grille initiale et appelle `search`.

```python
def solve(grid): return search(parse_grid(grid))

def search(values):
    "En utilisant la recherche en profondeur et la propagation, essayer toutes les valeurs possibles."
    if values is False:
        return False ## Échec précédent
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Résolu !
    ## Choisir le carré non rempli s avec le moins de possibilités
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
        for d in values[s])
```

Selon les règles du Sudoku, le puzzle est résolu lorsque chaque carré n'a qu'une seule valeur. La fonction `search` est appelée récursivement jusqu'à ce que le puzzle soit résolu. `values` est copié pour éviter la complexité.

Voici la fonction `some` utilisée pour vérifier si une tentative réussit à résoudre le puzzle.

```python
def some(seq):
    "Retourner un élément de seq qui est vrai."
    for e in seq:
        if e: return e
    return False
```

Ce code va maintenant résoudre chaque puzzle de Sudoku. Vous pouvez voir le code complet ci-dessous.

## Code complet du solveur de Sudoku

```python
def cross(A, B):
    "Produit cartésien des éléments dans A et des éléments dans B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

def parse_grid(grid):
    """Convertir la grille en un dictionnaire de valeurs possibles, {square: digits}, ou
    retourner False si une contradiction est détectée."""
    ## Pour commencer, chaque carré peut être n'importe quel chiffre ; puis assigner les valeurs de la grille.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Échec si nous ne pouvons pas assigner d au carré s.)
    return values

def grid_values(grid):
    "Convertir la grille en un dictionnaire de {square: char} avec '0' ou '.' pour les vides."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def assign(values, s, d):
    """Éliminer toutes les autres valeurs (sauf d) de values[s] et propager.
    Retourner values, sauf retourner False si une contradiction est détectée."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Éliminer d de values[s] ; propager lorsque les valeurs ou les emplacements <= 2.
    Retourner values, sauf retourner False si une contradiction est détectée."""
    if d not in values[s]:
        return values ## Déjà éliminé
    values[s] = values[s].replace(d,'')
    ## (1) Si un carré s est réduit à une valeur d2, alors éliminer d2 des pairs.
    if len(values[s]) == 0:
        return False ## Contradiction : dernière valeur retirée
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) Si une unité u est réduite à un seul emplacement pour une valeur d, alors la placer là.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction : aucun emplacement pour cette valeur
        elif len(dplaces) == 1:
            # d ne peut être qu'à un seul emplacement dans l'unité ; l'assigner là
            if not assign(values, dplaces[0], d):
                return False
    return values

def solve(grid): return search(parse_grid(grid))

def search(values):
    "En utilisant la recherche en profondeur et la propagation, essayer toutes les valeurs possibles."
    if values is False:
        return False ## Échec précédent
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Résolu !
    ## Choisir le carré non rempli s avec le moins de possibilités
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
        for d in values[s])

def some(seq):
    "Retourner un élément de seq qui est vrai."
    for e in seq:
        if e: return e
    return False
```