---
title: Comment utiliser la bibliothèque Polars en Python pour l'analyse de données
author: Sara Jadhav
date: '2025-12-10T18:14:34.788Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-polars-library-in-python-for-data-analysis
description: 'Dans cet article, je vais vous donner une introduction accessible aux
  débutants à la bibliothèque Polars en Python.

  Polars est une bibliothèque open-source, écrite à l''origine en Rust, qui facilite
  la manipulation de données (data wrangling) en Python. La syntaxe de Polars est
  très similaire à celle de Pandas...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765325732081/94ab547b-fdaf-41bb-ae60-ad03be31211a.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
- name: python beginner
  slug: python-beginner
- name: Polars
  slug: polars
- name: Programming Blogs
  slug: programming-blogs
- name: dataset
  slug: dataset
- name: dataframe
  slug: dataframe
seo_desc: 'In this article, I’ll give you a beginner-friendly introduction to the
  Polars library in Python.

  Polars is an open-source library, originally written in Rust, which makes data wrangling
  easier in Python. The syntax of Polars is very similar to Pandas...'
---


Dans cet article, je vais vous donner une introduction accessible aux débutants à la bibliothèque Polars en Python.

Polars est une bibliothèque open-source, écrite à l'origine en Rust, qui facilite la manipulation de données en Python. La syntaxe de Polars est très similaire à celle de Pandas ; ainsi, si vous avez déjà travaillé avec Pandas ou la bibliothèque PySpark, l'utilisation de Polars devrait être un jeu d'enfant.

Polars excelle par sa rapidité d'exécution. Elle est également économe en mémoire et vous aide à optimiser votre code grâce au parallélisme. Elle vous permet aussi de convertir des données depuis et vers diverses bibliothèques comme NumPy, Pandas, et d'autres.

Dans ce tutoriel, nous allons découvrir la bibliothèque Polars en partant de zéro, de l'installation et l'importation de la bibliothèque sur le système jusqu'à la manipulation de données dans un jeu de données à l'aide de cette bibliothèque.

Tout d'abord, nous examinerons les fonctions de base de Polars. Nous écrirons également du code pratique, ce qui vous aidera à appliquer ce que vous avez appris. Enfin, nous travaillerons avec un exemple de jeu de données pour consolider d'autres concepts clés de Polars. Plongeons dans le vif du sujet.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Installation et importation de la bibliothèque Polars](#heading-installation-et-importation-de-la-bibliotheque-polars)
    
* [Qu'est-ce qu'une Series ?](#heading-qu-est-ce-qu-une-series)
    
* [Qu'est-ce qu'un DataFrame ?](#heading-qu-est-ce-qu-un-dataframe)
    
* [Comment lire des fichiers CSV avec Polars](#heading-comment-lire-des-fichiers-csv-avec-polars)
    
* [Autres fonctions importantes](#heading-autres-fonctions-importantes)
    
* [Résumé](#heading-resume)
    

## Prérequis

Même si ce tutoriel est accessible aux débutants, posséder des connaissances de base dans les domaines suivants vous aidera à mieux comprendre cet article :

* Syntaxe de base de Python
    
* Structures de données
    
* Capacité à importer des bibliothèques et connaissance de l'utilisation des fonctions et méthodes
    
* Les bases de NumPy et Pandas seront utiles (mais pas indispensables).
    

Maintenant que vous connaissez les prérequis nécessaires pour suivre, commençons notre tutoriel.

## Installation et importation de la bibliothèque Polars

Pour installer la bibliothèque Polars, vous pouvez utiliser la commande suivante dans votre terminal :

`pip install polars`

Cela fonctionne si vous avez déjà le gestionnaire de paquets pip sur votre système. Si vous êtes dans un environnement conda, vous pouvez utiliser ceci :

`conda install -c conda-forge polars`

Cependant, je recommande vivement d'utiliser le gestionnaire de paquets pip pour éviter divers désagréments.

Importons Polars dans notre programme. Nous suivrons le même processus que pour l'importation d'autres bibliothèques en Python :

```python
import polars as pl # pl est un alias conventionnel
```

Lors de la création d'un objet Polars avec des données, il est important de connaître la taille de nos données. Polars a la capacité de gérer 2³² lignes dans un DataFrame. Pour charger plus de données, utilisez la commande suivante pour installer la bibliothèque Polars :

`pip install polars[rt64]`

Si vous souhaitez utiliser la bibliothèque Polars immédiatement sans l'installer sur votre système, l'utilisation d'un notebook Google Colab est la meilleure option. Dans Google Colab, vous pouvez directement importer et commencer à utiliser Polars dans votre programme. J'utiliserai Google Colab pour ce tutoriel.

## Qu'est-ce qu'une Series ?

Une Series est un élément fondamental d'un DataFrame. C'est une structure de données unidimensionnelle que vous pouvez corréler à une « liste » en Python ou à un « tableau 1D » dans NumPy. Mais la différence entre une Series et un tableau 1D est que la première est étiquetée alors que le second ne l'est pas. Plusieurs Series se rejoignent pour former un DataFrame.

Nous pouvons créer une Series avec des données homogènes ainsi qu'avec des données hétérogènes.

### Création d'une Series avec des données homogènes

Dans une Series, le type de données de tous les éléments doit être le même. Si ce n'est pas le cas, une erreur est générée.

La syntaxe pour définir une Series Polars est la suivante :

`nom_var = pl.Series("nom_colonne", [valeurs])`

Le code suivant montre un exemple de définition d'une Series homogène en Python :

```python
import polars as pl
series_homo = pl.Series("Numbers", ['One', 'Two', 'Three', 'Four', 'Five'])
print(series_homo)
```

**Sortie :**

```plaintext
shape: (5,)
Series: 'Numbers' [str]
[
	"One"
	"Two"
	"Three"
	"Four"
	"Five"
]
```

Dans le code ci-dessus, nous avons d'abord importé la bibliothèque Polars en utilisant l'alias `pl`. L'utilisation d'alias est un choix personnel, mais `pl` est conventionnel (comme `np` pour NumPy et `pd` pour Pandas). L'avantage d'utiliser des alias conventionnels est que lorsque vous transmettez le code à quelqu'un d'autre, il lui est facile de s'y retrouver.

Ensuite, nous avons utilisé la fonction `pl.Series()` pour créer un objet Series Polars. Comme premier paramètre, nous avons passé l'étiquette de notre Series (`Numbers` dans ce cas). Ensuite, nous avons passé les valeurs à stocker sous forme de liste. N'oubliez pas que la liste de valeurs que nous passons agit comme un seul argument. Enfin, nous avons affiché notre Series.

Nous pouvons voir que la sortie nous renseigne sur les dimensions de l'objet Polars ainsi que sur le type de données de la Series. La forme (lignes, colonnes) nous indique le nombre de lignes et de colonnes présentes dans l'objet Polars.

Nous pouvons trouver le type de données d'une Series homogène explicitement en utilisant la méthode `dtype`.

```python
print(series_homo.dtype)
```

**Sortie :**

```plaintext
String
```

### Création d'une Series avec des données hétérogènes

Des données hétérogènes signifient que le type de données de tous les éléments n'est pas le même. La syntaxe pour définir une Series avec des données hétérogènes est la suivante :

`nom_var = pl.Series("nom_colonne", [valeurs], strict=False)`

Vous vous demandez probablement, d'après ce que j'ai dit plus haut : comment pouvons-nous avoir une Series avec des données hétérogènes ? Eh bien, une chose à noter est qu'une Series est toujours homogène quel que soit le type de données qui lui est fourni. Je vais vous expliquer cela — regardons d'abord ce code :

```python
import polars as pl

series_hetero = pl.Series("Numbers", [1, "Two", 3, "Four"], strict=False)
print(series_hetero)
```

**Sortie :**

```plaintext
shape: (4,)
Series: 'Numbers' [str]
[
	"1"
	"Two"
	"3"
	"Four"
]
```

Ici, nous avons créé un objet Series à l'aide de la fonction `pl.Series()`, nous l'avons étiqueté et nous avons passé les valeurs souhaitées.

Mais vous remarquerez que nous avons fourni des données hétérogènes (des données qui n'ont pas le même type) à la fonction. Habituellement, cela génère une erreur. Mais comme nous avons défini le paramètre `strict` sur False, la fonction devient plus souple avec le schéma de la Series. (Le schéma est simplement le type de données attendu pour les valeurs à enregistrer dans la Series.)

Si aucun schéma particulier n'est défini pour une Series recevant des données hétérogènes, `pl.Series()` définit le schéma sur `pl.Utf8` (type de données chaîne de caractères). Vous pouvez voir cette correction automatique du schéma dans l'exemple ci-dessus. Cela empêche le programme de planter, car un type de données chaîne peut comprendre des caractères, des chiffres ainsi que des symboles.

De plus, nous pouvons voir que le type de données de tous les éléments est le même (`pl.Utf8`). Cela signifie que la Series est homogène, même si nous y avons mis des données hétérogènes.

Si nous définissons un schéma pour la Series, la bibliothèque Polars convertit tous les enregistrements — qui présentent un type de données différent du schéma défini — en objets nuls. Cela devrait être clair dans l'exemple suivant :

```python
import polars as pl
# définition du schéma comme Entier 32 bits
series = pl.Series("ints", [1, -2, 3, 4, 5, 'Thirteen', 'Fourteen'], dtype=pl.Int32, strict=False)
print(series)
```

**Sortie :**

```plaintext
shape: (7,)
Series: 'ints' [i32]
[
	1
	-2
	3
	4
	5
	null
	null
]
```

Ici, nous pouvons voir que les deux dernières entités étaient des chaînes de caractères (`String`), mais comme nous avons défini le schéma sur `Integer`, elles ont été transformées en enregistrements nuls (`null`).

Ainsi, comme vous pouvez le voir, la souplesse du programme dépend du fait que vous définissiez le paramètre `strict` sur True ou False. Si nous le définissons sur True, nous imposons strictement le schéma aux données. En cas de non-respect du schéma, le programme lève une exception. D'un autre côté, si nous définissons le paramètre `strict` sur False, la Series préserve tout de même sa nature homogène en transformant les éléments non conformes au schéma en valeurs nulles.

Maintenant que vous comprenez le fonctionnement des Series, nous sommes prêts à passer aux DataFrames.

## Qu'est-ce qu'un DataFrame ?

Un DataFrame est une structure de données bidimensionnelle que vous pouvez utiliser pour stocker un grand nombre de paramètres liés aux données collectées. Il est également utile pour analyser ces données. Un DataFrame n'est rien d'autre qu'une collection de plusieurs Series, chacune étiquetée différemment pour stocker différents aspects des données.

Voici la syntaxe pour créer un objet DataFrame Polars :

`nom_var = pl.DataFrame({paires clé: valeur}, schema)`

L'exemple suivant vous montre comment définir un objet DataFrame en Python :

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
print(df)
```

**Sortie :**

```plaintext
shape: (10, 3)
┌────────┬─────────────┬─────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 │
│ ---    ┆ ---         ┆ ---         │
│ u32    ┆ f64         ┆ f64         │
╞════════╪═════════════╪═════════════╡
│ 1      ┆ 0.0         ┆ 0.0         │
│ 2      ┆ 0.693147    ┆ 0.30103     │
│ 3      ┆ 1.098612    ┆ 0.477121    │
│ 4      ┆ 1.386294    ┆ 0.60206     │
│ 5      ┆ 1.609438    ┆ 0.69897     │
│ 6      ┆ 1.791759    ┆ 0.778151    │
│ 7      ┆ 1.94591     ┆ 0.845098    │
│ 8      ┆ 2.079442    ┆ 0.90309     │
│ 9      ┆ 2.197225    ┆ 0.954243    │
│ 10     ┆ 2.302585    ┆ 1.0         │
└────────┴─────────────┴─────────────┘
```

Ci-dessus, nous avons créé un objet DataFrame Polars avec la fonction `pl.DataFrame()`. Dans la fonction, nous avons créé un dictionnaire comme argument pour passer les valeurs du DataFrame.

Dans le dictionnaire, chaque paire clé-valeur représente une Series. Chaque clé représente l'étiquette de la Series, tandis que sa valeur représente les données de la Series. Les valeurs sont passées sous forme de liste car chaque clé ne peut correspondre qu'à une seule valeur.

Ensuite, nous avons défini le schéma pour le DataFrame. Là encore, le schéma est un dictionnaire, où chaque paire clé-valeur correspond au schéma de la Series. Dans le schéma, chaque clé représente l'étiquette de la Series (pour mapper le schéma à la bonne Series) et sa valeur représente le type de données.

Dans la sortie, nous pouvons voir que nous avons obtenu un tableau clair représentant nos données. Les étiquettes sont proprement séparées des données et, en dessous d'elles, leur schéma est également représenté.

### Qu'est-ce qu'un schéma ?

Un schéma fait référence à la définition du type de données de la Series. Nous fixons un type de données particulier à la Series homogène pour éviter de se retrouver avec des données mixtes.

Par exemple, dans le code ci-dessus, nous avons défini le type de données de la colonne `Number` sur `Unsigned Integer - 32 bit (pl.UInt32)` car nous ne voulons pas mettre d'entiers négatifs dans notre fonction logarithme NumPy.

Maintenant, si nous voulons masquer le type de données (qui est écrit sous chaque étiquette), nous pouvons utiliser la fonction suivante :

```python
pl.Config.set_tbl_hide_column_data_types(active=True)
```

### Les fonctions head, tail et glimpse

Les fonctions `head()`, `tail()` et `glimpse()` sont utilisées pour jeter un coup d'œil rapide aux données en examinant certains enregistrements (lignes). Elles sont particulièrement utiles pour les grands jeux de données afin de voir quelles colonnes sont présentes, quel type de données se trouve dans chaque colonne, etc.

La fonction `head()` affiche le nombre de lignes spécifié (passé en argument) depuis le haut du DataFrame. Si aucun argument n'est passé, elle affiche les cinq premières lignes du DataFrame.

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
pl.Config.set_tbl_hide_column_data_types(active=True)
print(df.head(3))
```

**Sortie :**

```plaintext
shape: (3, 3)
┌────────┬─────────────┬─────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 │
╞════════╪═════════════╪═════════════╡
│ 1      ┆ 0.0         ┆ 0.0         │
│ 2      ┆ 0.693147    ┆ 0.30103     │
│ 3      ┆ 1.098612    ┆ 0.477121    │
└────────┴─────────────┴─────────────┘
```

Dans cet exemple, nous avons utilisé le même DataFrame que celui que nous venons de créer. Ensuite, nous avons utilisé la fonction `head()` pour afficher les trois premières lignes. Vous remarquerez peut-être aussi que la représentation du schéma sous les noms de colonnes a disparu. C'est parce que nous avons utilisé `pl.Config.set_tbl_hide_column_data_types(active=True)`.

La fonction `glimpse()` présente les données de manière concise et horizontale (les lignes sont représentées comme des colonnes et les colonnes comme des lignes) pour une meilleure lisibilité.

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
pl.Config.set_tbl_hide_column_data_types(active=True)
print(df.glimpse())
```

**Sortie :**

```plaintext
Rows: 10
Columns: 3
$ Number      <u32> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
$ Natural Log <f64> 0.0, 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 1.791759469228055, 1.9459101490553132, 2.0794415416798357, 2.1972245773362196, 2.302585092994046
$ Log Base 10 <f64> 0.0, 0.3010299956639812, 0.47712125471966244, 0.6020599913279624, 0.6989700043360189, 0.7781512503836436, 0.8450980400142568, 0.9030899869919435, 0.9542425094393249, 1.0

None
```

Ici, nous avons utilisé la fonction `glimpse()` sur notre DataFrame `df`. Nous pouvons voir la sortie comme notre DataFrame transposé. De plus, `None` est renvoyé. C'est parce que, par défaut, `glimpse()` définit son paramètre `return_as_string` sur `None`. Pour le changer en chaîne de caractères, nous pouvons définir le paramètre `return_as_string` sur True. L'exemple suivant montre comment faire :

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
pl.Config.set_tbl_hide_column_data_types(active=True)
print(f'Returned as String: \n{df.glimpse(return_as_string=True)}')
```

**Sortie :**

```plaintext
Returned as String: 
Rows: 10
Columns: 3
$ Number      <u32> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
$ Natural Log <f64> 0.0, 0.6931471805599453, 1.0986122886681098, 1.3862943611198906, 1.6094379124341003, 1.791759469228055, 1.9459101490553132, 2.0794415416798357, 2.1972245773362196, 2.302585092994046
$ Log Base 10 <f64> 0.0, 0.3010299956639812, 0.47712125471966244, 0.6020599913279624, 0.6989700043360189, 0.7781512503836436, 0.8450980400142568, 0.9030899869919435, 0.9542425094393249, 1.0
```

Dans le code ci-dessus, nous pouvons voir que le DataFrame est renvoyé sous forme de chaîne et que `None` n'est pas renvoyé.

Enfin, la fonction `tail()` affiche le nombre de lignes spécifié depuis le bas du jeu de données. Lorsqu'aucun argument n'est passé, elle affiche les 5 dernières lignes par défaut.

C'est utile pour vérifier si nos données ont été complètement chargées. Vérifier les premiers enregistrements avec `head()` et les derniers avec `tail()` garantit que les données sont correctement et totalement chargées.

De plus, nous pouvons vérifier s'il y a des enregistrements vides à la fin du jeu de données. Avoir des enregistrements vides à la fin peut être fatal dans certains cas. Par exemple, si vous devez entraîner un modèle de Machine Learning sur un jeu de données et que vous le divisez statiquement en jeux de test et d'entraînement, les lignes vides à la fin vont causer un problème. Ainsi, vérifier nos données au préalable est une bonne pratique, et ces fonctions nous y aident.

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
pl.Config.set_tbl_hide_column_data_types(active=True)
print(df.tail(3))
```

**Sortie :**

```plaintext
shape: (3, 3)
┌────────┬─────────────┬─────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 │
╞════════╪═════════════╪═════════════╡
│ 8      ┆ 2.079442    ┆ 0.90309     │
│ 9      ┆ 2.197225    ┆ 0.954243    │
│ 10     ┆ 2.302585    ┆ 1.0         │
└────────┴─────────────┴─────────────┘
```

Dans le code ci-dessus, nous avons utilisé la fonction `tail()` sur le jeu de données et passé '3' comme argument. Ainsi, notre programme a renvoyé les trois dernières lignes.

### La fonction sample

La fonction `sample()` renvoie un nombre donné de lignes aléatoires dans un ordre aléatoire par rapport à leur occurrence dans le DataFrame. Cela permet d'éviter un échantillonnage biaisé des données.

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
pl.Config.set_tbl_hide_column_data_types(active=True)
print(df.sample(3))
```

**Sortie :**

```plaintext
shape: (3, 3)
┌────────┬─────────────┬─────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 │
╞════════╪═════════════╪═════════════╡
│ 6      ┆ 1.791759    ┆ 0.778151    │
│ 5      ┆ 1.609438    ┆ 0.69897     │
│ 10     ┆ 2.302585    ┆ 1.0         │
└────────┴─────────────┴─────────────┘
```

Nous pouvons voir dans la sortie que nous avons obtenu des lignes de données aléatoires dans un ordre aléatoire (la ligne 5 vient avant la ligne 6 dans le DataFrame, pourtant par échantillonnage, nous avons obtenu la ligne 5 après la ligne 6). L'échantillonnage est une bonne pratique car il aide à éviter le surapprentissage (overfitting) en Machine Learning dans certains cas et nous donne une idée générale de l'ensemble du jeu de données.

### Concaténation de deux DataFrames

En résumé, « concaténer » signifie simplement « lier ». Ajouter ou lier un jeu de données à un autre — essentiellement, les empiler l'un sur l'autre — revient à concaténer les deux jeux de données.

Par exemple, dans le DataFrame précédent, nous avions des nombres de 1 à 10 et leurs logarithmes. Maintenant, si nous voulons aller de 1 à 20, nous devons concaténer un autre jeu de données contenant les nombres de 11 à 20 au premier.

Le code suivant montre comment cela fonctionne :

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
pl.Config.set_tbl_hide_column_data_types(active=True)

# nouveau jeu de données créé pour la concaténation
df1 = pl.DataFrame({
    "Number" : [x for x in range(11, 21)],
    "Log Base 10" : [np.log10(x) for x in range(11,21)],
    "Natural Log" : [np.log(x) for x in range(11, 21)]
}, schema=schema)

print(pl.concat([df, df1], how='vertical')) # concaténation des deux jeux de données
```

**Sortie :**

```plaintext
shape: (20, 3)
┌────────┬─────────────┬─────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 │
╞════════╪═════════════╪═════════════╡
│ 1      ┆ 0.0         ┆ 0.0         │
│ 2      ┆ 0.693147    ┆ 0.30103     │
│ 3      ┆ 1.098612    ┆ 0.477121    │
│ 4      ┆ 1.386294    ┆ 0.60206     │
│ 5      ┆ 1.609438    ┆ 0.69897     │
│ …      ┆ …           ┆ …           │
│ 16     ┆ 2.772589    ┆ 1.20412     │
│ 17     ┆ 2.833213    ┆ 1.230449    │
│ 18     ┆ 2.890372    ┆ 1.255273    │
│ 19     ┆ 2.944439    ┆ 1.278754    │
│ 20     ┆ 2.995732    ┆ 1.30103     │
└────────┴─────────────┴─────────────┘
```

Dans ce code, nous avons d'abord créé le DataFrame `df`. Ensuite, nous avons créé un autre DataFrame `df1`. Enfin, nous avons utilisé `pl.concat()` pour concaténer les DataFrames.

Le premier argument que nous avons passé est la liste des DataFrames à lier. Le paramètre `how` définit la manière de concaténer. « Vertical » dans ce contexte signifie que nous lions les DataFrames verticalement (en ajoutant plus de lignes).

Le point important à noter ici est que l'incompatibilité de schéma peut lever une exception. Si les DataFrames à concaténer ont des schémas différents, il y aura un problème d'incompatibilité. Il est donc préférable de garder les schémas des deux jeux de données identiques.

Ici, nous avons introduit une variable nommée `schema` contenant le paramètre de schéma du DataFrame et nous l'avons appliquée aux deux DataFrames pour éviter toute incompatibilité.

De plus, la concaténation se produit dans l'ordre des arguments passés. Par exemple, dans le code ci-dessus, `df` apparaît avant `df1`, donc dans le DataFrame lié, `df` apparaît en premier, puis `df1`. Si nous avions changé la séquence des valeurs, le DataFrame concaténé commencerait par `df1` puis `df`.

Le code suivant explique cela :

```python
import polars as pl
import numpy as np

schema = {"Number": pl.UInt32, "Natural Log": None, "Log Base 10": None}

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
pl.Config.set_tbl_hide_column_data_types(active=True)

# nouveau jeu de données créé pour la concaténation
df1 = pl.DataFrame({
    "Number" : [x for x in range(11, 21)],
    "Log Base 10" : [np.log10(x) for x in range(11,21)],
    "Natural Log" : [np.log(x) for x in range(11, 21)]
}, schema=schema)

print(pl.concat([df1, df], how='vertical')) # séquence changée de [df,df1] à [df1, df]
```

**Sortie :**

```plaintext
shape: (20, 3)
┌────────┬─────────────┬─────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 │
╞════════╪═════════════╪═════════════╡
│ 11     ┆ 2.397895    ┆ 1.041393    │
│ 12     ┆ 2.484907    ┆ 1.079181    │
│ 13     ┆ 2.564949    ┆ 1.113943    │
│ 14     ┆ 2.639057    ┆ 1.146128    │
│ 15     ┆ 2.70805     ┆ 1.176091    │
│ …      ┆ …           ┆ …           │
│ 6      ┆ 1.791759    ┆ 0.778151    │
│ 7      ┆ 1.94591     ┆ 0.845098    │
│ 8      ┆ 2.079442    ┆ 0.90309     │
│ 9      ┆ 2.197225    ┆ 0.954243    │
│ 10     ┆ 2.302585    ┆ 1.0         │
└────────┴─────────────┴─────────────┘
```

Ici, nous pouvons voir que `df1` apparaît en premier, puis `df` (contrairement à l'exemple précédent). Ainsi, la séquence des valeurs est importante.

### Comment joindre deux DataFrames

**Joindre** des jeux de données et **concaténer** des jeux de données sont deux concepts différents. Alors que concaténer signifie « lier » deux jeux de données séparés, [joindre](https://www.freecodecamp.org/news/understanding-sql-joins/) fait référence à la combinaison de jeux de données sur la base d'une colonne partagée (une clé).  
L'ordinateur fait correspondre les lignes des deux jeux de données là où les valeurs des clés sont identiques.

Dans le jeu de données 'df' précédent, nous allons ajouter une nouvelle colonne en joignant le jeu de données 'df' avec un autre DataFrame.

```python
# nouveau dataframe
new_col = pl.DataFrame({
    "Number" : [x for x in range(1, 11)],
    "Log Base 2" : [np.log2(x) for x in range(1, 11)]
})

new_data = df.join(new_col, on="Number", how="left") # Les deux ont une colonne identique pour mapper les valeurs

print(new_data.head())
```

**Sortie :**

```plaintext
shape: (5, 4)
┌────────┬─────────────┬─────────────┬────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 ┆ Log Base 2 │
╞════════╪═════════════╪═════════════╪════════════╡
│ 1      ┆ 0.0         ┆ 0.0         ┆ 0.0        │
│ 2      ┆ 0.693147    ┆ 0.30103     ┆ 1.0        │
│ 3      ┆ 1.098612    ┆ 0.477121    ┆ 1.584963   │
│ 4      ┆ 1.386294    ┆ 0.60206     ┆ 2.0        │
│ 5      ┆ 1.609438    ┆ 0.69897     ┆ 2.321928   │
└────────┴─────────────┴─────────────┴────────────┘
```

Dans cet exemple, nous avons utilisé la fonction join sur `df` et passé `new_col` comme argument. C'est pourquoi les colonnes de `df` apparaissent avant la colonne du jeu de données `new_col`. Le paramètre `on` doit recevoir le nom d'une colonne sur la base de laquelle les deux jeux de données doivent être joints.

Ici, nous avons d'abord mappé les éléments de la colonne `Number` et ses lignes correspondantes, puis joint les DataFrames en conséquence.

Si nous avions utilisé la fonction `join()` sur le DataFrame `new_col`, les colonnes de `df` apparaîtraient après la colonne de `new_col`. Le code suivant clarifiera cela :

```python
# nouveau dataframe
new_col = pl.DataFrame({
    "Number" : [x for x in range(1, 11)],
    "Log Base 2" : [np.log2(x) for x in range(1, 11)]
})

new_data = new_col.join(df, on="Number", how="left") # df passé comme argument

print(new_data.head())
```

**Sortie :**

```plaintext
shape: (5, 4)
┌────────┬────────────┬─────────────┬─────────────┐
│ Number ┆ Log Base 2 ┆ Natural Log ┆ Log Base 10 │
╞════════╪════════════╪═════════════╪═════════════╡
│ 1      ┆ 0.0        ┆ 0.0         ┆ 0.0         │
│ 2      ┆ 1.0        ┆ 0.693147    ┆ 0.30103     │
│ 3      ┆ 1.584963   ┆ 1.098612    ┆ 0.477121    │
│ 4      ┆ 2.0        ┆ 1.386294    ┆ 0.60206     │
│ 5      ┆ 2.321928   ┆ 1.609438    ┆ 0.69897     │
└────────┴────────────┴─────────────┴─────────────┘
```

Vous pouvez remarquer que la colonne 'Log Base 2' apparaît avant les autres colonnes (contrairement à l'exemple précédent). Ce changement est donc significatif.

### Comment utiliser la fonction `with_columns()`

La fonction `with_columns()` nous permet d'apporter des modifications à une colonne et de l'afficher comme une nouvelle colonne aux côtés des colonnes existantes du jeu de données original. C'est similaire à la fonction `join()`.

L'exemple suivant clarifiera cela :

```python
import polars as pl
import numpy as np

df = pl.DataFrame(
    {
        "Number" : np.arange(1, 11),
        "Natural Log" : [np.log(x) for x in range(1,11)],
        'Log Base 10' : [np.log10(x) for x in range(1,11)]
        },
    schema=schema
    )
new_data = df.with_columns((np.log2(pl.col("Number"))).alias("Log Base 2"))

print(new_data.head())
```

**Sortie :**

```plaintext
shape: (5, 4)
┌────────┬─────────────┬─────────────┬────────────┐
│ Number ┆ Natural Log ┆ Log Base 10 ┆ Log Base 2 │
╞════════╪═════════════╪═════════════╪════════════╡
│ 1      ┆ 0.0         ┆ 0.0         ┆ 0.0        │
│ 2      ┆ 0.693147    ┆ 0.30103     ┆ 1.0        │
│ 3      ┆ 1.098612    ┆ 0.477121    ┆ 1.584963   │
│ 4      ┆ 1.386294    ┆ 0.60206     ┆ 2.0        │
│ 5      ┆ 1.609438    ┆ 0.69897     ┆ 2.321928   │
└────────┴─────────────┴─────────────┴────────────┘
```

Dans cet exemple, nous avons un DataFrame `df`. Pour y ajouter une colonne, nous utilisons la fonction `with_columns()`. Dans cette fonction, nous avons sélectionné la colonne nommée 'Number' à l'aide de la fonction `pl.col()` et l'avons placée à l'intérieur de `np.log2()` pour obtenir la valeur du logarithme en base 2 pour chaque enregistrement. Enfin, pour étiqueter la nouvelle colonne, nous avons utilisé la fonction `alias()`, avec l'étiquette passée en argument.

Maintenant que nous connaissons les bases des DataFrames, voyons comment travailler avec des fichiers CSV.

## Comment lire des fichiers CSV avec Polars

Lire des fichiers CSV avec Polars est extrêmement similaire à la manière dont cela fonctionne avec Pandas. Pour ce tutoriel, j'utiliserai le jeu de données Titanic. Voici le [lien vers le jeu de données](https://www.kaggle.com/datasets/yasserh/titanic-dataset?select=Titanic-Dataset.csv) pour que vous puissiez le télécharger. Dans cette partie du tutoriel, nous parlerons principalement de la sélection de colonnes (utile pour la sélection de caractéristiques) et du filtrage des données.

Voici la syntaxe pour lire un fichier CSV :

`nom_var = pl.read_csv("chemin_jeu_de_donnees")`

Exemple de code :

```python
import polars as pl

data = pl.read_csv("/titanic_dataset.csv")
print(data.head())
```

**Sortie :**

```plaintext
shape: (5, 12)
┌─────────────┬──────────┬────────┬─────────────────────┬───┬─────────┬─────────┬───────┬──────────┐
│ PassengerId ┆ Survived ┆ Pclass ┆ Name                ┆ … ┆ Ticket  ┆ Fare    ┆ Cabin ┆ Embarked │
╞═════════════╪══════════╪════════╪═════════════════════╪═══╪═════════╪═════════╪═══════╪══════════╡
│ 892         ┆ 0        ┆ 3      ┆ Kelly, Mr. James    ┆ … ┆ 330911  ┆ 7.8292  ┆ null  ┆ Q        │
│ 893         ┆ 1        ┆ 3      ┆ Wilkes, Mrs. James  ┆ … ┆ 363272  ┆ 7.0     ┆ null  ┆ S        │
│             ┆          ┆        ┆ (Ellen Need…        ┆   ┆         ┆         ┆       ┆          │
│ 894         ┆ 0        ┆ 2      ┆ Myles, Mr. Thomas   ┆ … ┆ 240276  ┆ 9.6875  ┆ null  ┆ Q        │
│             ┆          ┆        ┆ Francis             ┆   ┆         ┆         ┆       ┆          │
│ 895         ┆ 0        ┆ 3      ┆ Wirz, Mr. Albert    ┆ … ┆ 315154  ┆ 8.6625  ┆ null  ┆ S        │
│ 896         ┆ 1        ┆ 3      ┆ Hirvonen, Mrs.      ┆ … ┆ 3101298 ┆ 12.2875 ┆ null  ┆ S        │
│             ┆          ┆        ┆ Alexander (Helg…    ┆   ┆         ┆         ┆       ┆          │
└─────────────┴──────────┴────────┴─────────────────────┴───┴─────────┴─────────┴───────┴──────────┘
```

Nous pouvons obtenir l'analyse statistique des données en utilisant la fonction `describe()`.

```python
print(data.describe())
```

**Sortie :**

```plaintext
shape: (9, 13)
┌────────────┬─────────────┬──────────┬──────────┬───┬─────────────┬───────────┬───────┬──────────┐
│ statistic  ┆ PassengerId ┆ Survived ┆ Pclass   ┆ … ┆ Ticket      ┆ Fare      ┆ Cabin ┆ Embarked │
╞════════════╪═════════════╪══════════╪══════════╪═══╪═════════════╪═══════════╪═══════╪══════════╡
│ count      ┆ 418.0       ┆ 418.0    ┆ 418.0    ┆ … ┆ 418         ┆ 417.0     ┆ 91    ┆ 418      │
│ null_count ┆ 0.0         ┆ 0.0      ┆ 0.0      ┆ … ┆ 0           ┆ 1.0       ┆ 327   ┆ 0        │
│ mean       ┆ 1100.5      ┆ 0.363636 ┆ 2.26555  ┆ … ┆ null        ┆ 35.627188 ┆ null  ┆ null     │
│ std        ┆ 120.810458  ┆ 0.481622 ┆ 0.841838 ┆ … ┆ null        ┆ 55.907576 ┆ null  ┆ null     │
│ min        ┆ 892.0       ┆ 0.0      ┆ 1.0      ┆ … ┆ 110469      ┆ 0.0       ┆ A11   ┆ C        │
│ 25%        ┆ 996.0       ┆ 0.0      ┆ 1.0      ┆ … ┆ null        ┆ 7.8958    ┆ null  ┆ null     │
│ 50%        ┆ 1101.0      ┆ 0.0      ┆ 3.0      ┆ … ┆ null        ┆ 14.4542   ┆ null  ┆ null     │
│ 75%        ┆ 1205.0      ┆ 1.0      ┆ 3.0      ┆ … ┆ null        ┆ 31.5      ┆ null  ┆ null     │
│ max        ┆ 1309.0      ┆ 1.0      ┆ 3.0      ┆ … ┆ W.E.P. 5734 ┆ 512.3292  ┆ G6    ┆ S        │
└────────────┴─────────────┴──────────┴──────────┴───┴─────────────┴───────────┴───────┴──────────┘
```

### Comment sélectionner des colonnes dans le jeu de données

Nous allons maintenant apprendre à sélectionner certaines colonnes du jeu de données et à les transformer en un nouveau DataFrame. Cela peut être utile si nous voulons entraîner un modèle de Machine Learning basé uniquement sur certaines colonnes et non sur l'ensemble du jeu de données (c'est-à-dire en utilisant la sélection de caractéristiques).

Regardons d'abord le code ci-dessous :

```python
new_df = data.select(
    pl.col("Survived"),
    pl.col("Name"),
    pl.col("Age"),
    pl.col("Sex")
)

print(new_df.head())
```

**Sortie :**

```plaintext
shape: (5, 4)
┌──────────┬─────────────────────────────────┬──────┬────────┐
│ Survived ┆ Name                            ┆ Age  ┆ Sex    │
╞══════════╪═════════════════════════════════╪══════╪════════╡
│ 0        ┆ Kelly, Mr. James                ┆ 34.5 ┆ male   │
│ 1        ┆ Wilkes, Mrs. James (Ellen Need… ┆ 47.0 ┆ female │
│ 0        ┆ Myles, Mr. Thomas Francis       ┆ 62.0 ┆ male   │
│ 0        ┆ Wirz, Mr. Albert                ┆ 27.0 ┆ male   │
│ 1        ┆ Hirvonen, Mrs. Alexander (Helg… ┆ 22.0 ┆ female │
└──────────┴─────────────────────────────────┴──────┴────────┘
```

Dans le code ci-dessus, nous avons sélectionné quatre colonnes à l'aide des fonctions `select()` et `pl.col()` du jeu de données Titanic et les avons transformées en un nouveau DataFrame appelé `new_df`.

Maintenant, nous pouvons filtrer ces données comme nous le souhaitons. Créons un nouveau DataFrame en filtrant uniquement les passagers survivants du jeu de données :

```python
survived_data = data.select(
    pl.col("Survived"),
    pl.col("Name"),
    pl.col("Age"),
    pl.col("Sex")
).filter(pl.col("Survived")==1)

print(survived_data.head())
```

**Sortie :**

```plaintext
shape: (5, 4)
┌──────────┬─────────────────────────────────┬──────┬────────┐
│ Survived ┆ Name                            ┆ Age  ┆ Sex    │
╞══════════╪═════════════════════════════════╪══════╪════════╡
│ 1        ┆ Wilkes, Mrs. James (Ellen Need… ┆ 47.0 ┆ female │
│ 1        ┆ Hirvonen, Mrs. Alexander (Helg… ┆ 22.0 ┆ female │
│ 1        ┆ Connolly, Miss. Kate            ┆ 30.0 ┆ female │
│ 1        ┆ Abrahim, Mrs. Joseph (Sophie H… ┆ 18.0 ┆ female │
│ 1        ┆ Snyder, Mrs. John Pillsbury (N… ┆ 23.0 ┆ female │
└──────────┴─────────────────────────────────┴──────┴────────┘
```

Dans le code ci-dessus, nous avons utilisé la fonction `filter()`. Cette fonction nous aide à rassembler les données qui répondent à une condition donnée. Dans l'exemple ci-dessus, nous avons ajouté la condition suivante : « Chaque élément de la colonne nommée 'Survived' doit être égal à 1 ». Ainsi, nous avons obtenu les données requises.

## Autres fonctions importantes

### Comment afficher le nom des colonnes d'un jeu de données

Vous pouvez afficher les noms des colonnes en utilisant la méthode `columns`. Le code suivant montre comment utiliser la méthode columns :

```python
print(data.columns) # data --> Jeu de données Titanic
```

**Sortie :**

> \['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'\]

### Comment indexer un jeu de données

Indexer un jeu de données signifie ajouter une colonne d'index au jeu de données existant. Cela peut s'avérer utile pour suivre les lignes du jeu de données.

Nous pouvons indexer le jeu de données à l'aide de la fonction `with_row_index()`. À l'intérieur de cette fonction, nous pouvons passer un argument pour nommer cette nouvelle colonne d'index. Si nous ne passons aucun argument, le nom de la colonne d'index est défini sur 'index' par défaut.

```python
data = pl.read_csv("/titanic_dataset.csv").with_row_index('#') # nommer la colonne d'index '#'
print(data.head())
```

**Sortie :**

```plaintext
shape: (5, 13)
┌─────┬─────────────┬──────────┬────────┬───┬─────────┬─────────┬───────┬──────────┐
│ #   ┆ PassengerId ┆ Survived ┆ Pclass ┆ … ┆ Ticket  ┆ Fare    ┆ Cabin ┆ Embarked │
│ --- ┆ ---         ┆ ---      ┆ ---    ┆   ┆ ---     ┆ ---     ┆ ---   ┆ ---      │
│ u32 ┆ i64         ┆ i64      ┆ i64    ┆   ┆ str     ┆ f64     ┆ str   ┆ str      │
╞═════╪═════════════╪══════════╪════════╪═══╪═════════╪═════════╪═══════╪══════════╡
│ 0   ┆ 892         ┆ 0        ┆ 3      ┆ … ┆ 330911  ┆ 7.8292  ┆ null  ┆ Q        │
│ 1   ┆ 893         ┆ 1        ┆ 3      ┆ … ┆ 363272  ┆ 7.0     ┆ null  ┆ S        │
│ 2   ┆ 894         ┆ 0        ┆ 2      ┆ … ┆ 240276  ┆ 9.6875  ┆ null  ┆ Q        │
│ 3   ┆ 895         ┆ 0        ┆ 3      ┆ … ┆ 315154  ┆ 8.6625  ┆ null  ┆ S        │
│ 4   ┆ 896         ┆ 1        ┆ 3      ┆ … ┆ 3101298 ┆ 12.2875 ┆ null  ┆ S        │
└─────┴─────────────┴──────────┴────────┴───┴─────────┴─────────┴───────┴──────────┘
```

### Comment renommer des colonnes dans le jeu de données

Enfin, pour renommer des colonnes dans le jeu de données, nous utilisons la fonction `rename()`.

```python
data = pl.read_csv("/titanic_dataset.csv").with_row_index('#').rename({'PassengerId':'renamed_col'})
print(data.head())
```

**Sortie :**

```plaintext
shape: (5, 13)
┌─────┬─────────────┬──────────┬────────┬───┬─────────┬─────────┬───────┬──────────┐
│ #   ┆ renamed_col ┆ Survived ┆ Pclass ┆ … ┆ Ticket  ┆ Fare    ┆ Cabin ┆ Embarked │
│ --- ┆ ---         ┆ ---      ┆ ---    ┆   ┆ ---     ┆ ---     ┆ ---   ┆ ---      │
│ u32 ┆ i64         ┆ i64      ┆ i64    ┆   ┆ str     ┆ f64     ┆ str   ┆ str      │
╞═════╪═════════════╪══════════╪════════╪═══╪═════════╪═════════╪═══════╪══════════╡
│ 0   ┆ 892         ┆ 0        ┆ 3      ┆ … ┆ 330911  ┆ 7.8292  ┆ null  ┆ Q        │
│ 1   ┆ 893         ┆ 1        ┆ 3      ┆ … ┆ 363272  ┆ 7.0     ┆ null  ┆ S        │
│ 2   ┆ 894         ┆ 0        ┆ 2      ┆ … ┆ 240276  ┆ 9.6875  ┆ null  ┆ Q        │
│ 3   ┆ 895         ┆ 0        ┆ 3      ┆ … ┆ 315154  ┆ 8.6625  ┆ null  ┆ S        │
│ 4   ┆ 896         ┆ 1        ┆ 3      ┆ … ┆ 3101298 ┆ 12.2875 ┆ null  ┆ S        │
└─────┴─────────────┴──────────┴────────┴───┴─────────┴─────────┴───────┴──────────┘
```

Dans l'exemple ci-dessus, nous avons renommé la colonne nommée 'PassengerId' en 'renamed\_col'.

## Résumé

Vous savez maintenant comment travailler avec la bibliothèque Python Polars pour analyser vos données plus efficacement.

Dans cet article, vous avez appris :

* Ce qu'est Polars et comment l'installer
    
* Comment définir des Series et des DataFrames dans Polars
    
* Différentes fonctions pour manipuler les DataFrames
    
* Comment lire et travailler avec des fichiers CSV dans Polars
    

Merci de m'avoir lue, et bonne manipulation de données !