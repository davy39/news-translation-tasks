---
title: Supprimer une colonne de Dataframe dans Pandas – Comment supprimer des colonnes
  des Dataframes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-27T18:03:48.000Z'
originalURL: https://freecodecamp.org/news/dataframe-drop-column-in-pandas-how-to-remove-columns-from-dataframes
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Dataframe-Drop-Column-in-Pandas
seo_title: Supprimer une colonne de Dataframe dans Pandas – Comment supprimer des
  colonnes des Dataframes
---

How-to-Remove-Columns-from-Dataframes.png
tags:
- name: Science des données
  slug: science-des-donnees
- name: pandas
  slug: pandas
- name: Python
  slug: python
seo_title: null
seo_desc: 'Par Shittu Olumide

  Dans Pandas, vous aurez parfois besoin de supprimer des colonnes d''un DataFrame pour diverses
  raisons, telles que le nettoyage des données, la réduction de l''utilisation de la mémoire ou la simplification de l''analyse.
  Dans cet article, je vais vous montrer comment faire.

  Je commencerai par présent...'
---

Par Shittu Olumide

Dans Pandas, vous aurez parfois besoin de supprimer des colonnes d'un DataFrame pour diverses raisons, telles que le nettoyage des données, la réduction de l'utilisation de la mémoire ou la simplification de l'analyse. Et dans cet article, je vais vous montrer comment faire.

Je commencerai par présenter la méthode `.drop()`, qui est la principale méthode pour supprimer des colonnes dans Pandas. Nous passerons en revue la syntaxe et les paramètres de la méthode `.drop()`, y compris comment spécifier les colonnes à supprimer et comment contrôler si le DataFrame original est modifié sur place ou si un nouveau DataFrame est renvoyé.

Ensuite, je fournirai un exemple d'utilisation de la méthode `.drop()` pour supprimer des colonnes d'un DataFrame.

## Comment utiliser la méthode `.drop()` dans Pandas

La méthode `.drop()` est une fonction intégrée dans Pandas qui vous permet de supprimer une ou plusieurs lignes ou colonnes d'un DataFrame. Elle renvoie un nouveau DataFrame avec les lignes ou colonnes spécifiées supprimées et ne modifie pas le DataFrame original sur place, à moins que vous ne définissiez le paramètre `inplace` sur `True`.

La syntaxe pour utiliser la méthode `.drop()` est la suivante :

```py
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')

```

Ici, `DataFrame` fait référence au DataFrame Pandas dont vous souhaitez supprimer des lignes ou des colonnes. Les paramètres que vous pouvez utiliser avec la méthode `.drop()` incluent :

* `labels` : Ce paramètre spécifie les étiquettes ou les indices des lignes ou des colonnes à supprimer. Vous pouvez passer soit une seule étiquette ou un seul indice, soit une liste d'étiquettes ou d'indices.
* `axis` : Ce paramètre spécifie s'il faut supprimer des lignes ou des colonnes. Par défaut, il est défini sur `0`, ce qui signifie que les lignes sont supprimées. Si vous souhaitez supprimer des colonnes, réglez-le sur `1`.
* `index` et `columns` : Ces paramètres sont des alternatives au paramètre `labels` et spécifient respectivement les étiquettes ou les indices des lignes ou des colonnes à supprimer.
* `level` : Ce paramètre est utilisé pour supprimer un niveau spécifique d'un index hiérarchique.
* `inplace` : Ce paramètre est une valeur booléenne qui détermine s'il faut modifier le DataFrame original sur place. Par défaut, il est défini sur `False`.
* `errors` : Ce paramètre spécifie comment gérer les erreurs si la ou les étiquettes ou indices spécifiés ne sont pas trouvés dans le DataFrame. Par défaut, il est défini sur `raise`, ce qui signifie qu'une `KeyError` est levée. Les autres options sont `ignore` et `warn`, qui ignoreront ou afficheront respectivement un avertissement lorsque l'étiquette/l'indice n'est pas trouvé.

## Comment supprimer une seule colonne d'un Dataframe dans Pandas

Commençons doucement en apprenant d'abord comment supprimer une seule colonne d'un Dataframe avant de passer à la suppression de plusieurs colonnes.

Exemple de code :

```py
import pandas as pd

# créer un exemple de dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'gender': ['F', 'M', 'M']
        }
df = pd.DataFrame(data)

# afficher le dataframe original
print('DataFrame original :\n', df)

# supprimer la colonne 'gender'
df = df.drop(columns=['gender'])

# afficher le dataframe modifié
print('DataFrame modifié :\n', df)

```

Sortie :

```bash
Original DataFrame:
       name  age gender
0    Alice   25      F
1      Bob   30      M
2  Charlie   35      M

Modified DataFrame:
       name  age
0    Alice   25
1      Bob   30
2  Charlie   35

```

### Explication du code :

Dans l'exemple ci-dessus, nous avons d'abord créé un DataFrame d'exemple avec trois colonnes – `name`, `age` et `gender`. Nous avons ensuite utilisé la méthode `.drop()` avec le paramètre `columns` pour supprimer la colonne `gender`. Le DataFrame résultant ne contient plus que les colonnes `name` et `age`.

Il est important de noter que la méthode `.drop()` ne modifie pas le DataFrame original sur place. Au lieu de cela, elle renvoie un nouveau DataFrame avec la ou les colonnes spécifiées supprimées. Si vous souhaitez modifier le DataFrame original, vous devez réassigner le résultat de la méthode `.drop()` à la variable d'origine, comme nous l'avons fait dans l'exemple ci-dessus.

En plus du paramètre `columns`, la méthode `.drop()` possède également un certain nombre d'autres paramètres optionnels que vous pouvez utiliser pour contrôler la suppression des colonnes.

Par exemple, vous pouvez utiliser le paramètre `inplace` pour modifier le DataFrame original sur place au lieu de renvoyer un nouveau DataFrame. Vous pouvez également utiliser le paramètre `axis` pour supprimer des colonnes par index plutôt que par nom.

## Comment supprimer plusieurs colonnes d'un Dataframe dans Pandas

Dans cette section, nous allons supprimer plusieurs colonnes de notre dataframe. Cette approche est similaire à la suppression d'une seule colonne du dataframe.

Pour supprimer deux colonnes ou plus d'un DataFrame à l'aide de la méthode `.drop()` dans Pandas, nous pouvons passer une liste de noms de colonnes au paramètre `columns` de la méthode.

### Exemple de code :

```py
import pandas as pd

# créer un exemple de dataframe
data = {'name': ['John', 'Mary', 'Peter'],
        'age': [30, 25, 35],
        'gender': ['Male', 'Female', 'Male'],
        'city': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# supprimer les colonnes 'gender' et 'city'
df.drop(columns=['gender', 'city'], inplace=True)

# imprimer le dataframe modifié
print(df)

```

Sortie :

```bash
    name  age
0   John   30
1   Mary   25
2  Peter   35

```

### Explication du code :

Dans cet exemple, nous créons d'abord un DataFrame d'exemple avec quatre colonnes – `name`, `age`, `gender` et `city`. Ensuite, nous utilisons la méthode `.drop()` pour supprimer les colonnes `gender` et `city` en passant une liste de leurs noms au paramètre `columns`. Enfin, nous définissons le paramètre `inplace` sur `True` pour modifier le DataFrame original et nous imprimons le DataFrame modifié.

Notez que vous pouvez également supprimer des colonnes par leurs indices en passant une liste d'indices au paramètre `columns`. Par exemple, pour supprimer la deuxième et la troisième colonne, vous pouvez utiliser :

```py
df.drop(columns=df.columns[1:3], inplace=True)

```

Cela supprimera les colonnes avec les indices 1 et 2 (c'est-à-dire les colonnes `age` et `gender` dans cet exemple).

## Conclusion

J'espère que cet article sera une ressource utile pour toute personne travaillant avec des DataFrames Pandas qui a besoin de supprimer des colonnes de manière efficace et efficiente.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !