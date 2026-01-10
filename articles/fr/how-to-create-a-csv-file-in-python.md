---
title: Comment créer un fichier CSV en utilisant Python
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2023-03-01T00:43:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-csv-file-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/csv-article-cover-image-2.png
tags:
- name: csv
  slug: csv
- name: Python
  slug: python
seo_title: Comment créer un fichier CSV en utilisant Python
seo_desc: 'CSV is an acronym for comma-separated values. It''s a file format that
  you can use to store tabular data, such as in a spreadsheet. You can also use it
  to store data from a tabular database.

  You can refer to each row in a CSV file as a data record. Ea...'
---

**CSV** est l'acronyme de "comma-separated values" (valeurs séparées par des virgules). C'est un format de fichier que vous pouvez utiliser pour stocker des données tabulaires, comme dans une feuille de calcul. Vous pouvez également l'utiliser pour stocker des données provenant d'une base de données tabulaire.

Vous pouvez vous référer à chaque ligne d'un fichier CSV comme un enregistrement de données. Chaque enregistrement de données se compose d'un ou plusieurs champs, séparés par des virgules.

Cet article vous montre comment utiliser le module intégré de Python appelé **csv** pour créer des fichiers CSV. Afin de comprendre pleinement ce tutoriel, vous devez avoir une bonne compréhension des fondamentaux du langage de programmation Python.

Le module csv dispose de deux classes que vous pouvez utiliser pour écrire des données dans un fichier CSV. Ces classes sont :

* la classe `csv.writer`

* la classe `csv.DictWriter`

## Comment créer un fichier CSV en utilisant la classe `csv.writer`

Vous pouvez utiliser la classe `csv.writer` pour écrire des données dans un fichier CSV. La classe retourne un objet writer, que vous pouvez ensuite utiliser pour convertir des données en chaînes délimitées.

Pour vous assurer que les caractères de nouvelle ligne à l'intérieur des champs cités sont interprétés correctement, ouvrez un objet de fichier CSV avec **newline=''**.

La syntaxe de la classe **csv.writer** est la suivante :

```python
csv.writer(csvfile, dialect='excel', **fmtparams)
```

Maintenant, laissez-moi vous expliquer la signification des différents paramètres utilisés dans la syntaxe.

1. Le paramètre `csvfile` représente l'objet csvfile avec la méthode `write()`.

2. Le paramètre optionnel `dialect` représente le nom du dialecte que vous pouvez utiliser pour écrire le fichier CSV.

3. Le paramètre optionnel `fmtparams` représente les paramètres de formatage que vous pouvez utiliser pour écraser les paramètres spécifiés dans le dialecte.

La classe **csv.writer** dispose de deux méthodes que vous pouvez utiliser pour écrire des données dans des fichiers CSV. Les méthodes sont les suivantes :

### La méthode `writerow()`

La méthode `writerow()` prend des données itérables comme paramètre et écrit ensuite les données dans votre fichier CSV en une seule ligne. Une utilisation populaire de la méthode **writerow()** consiste à l'utiliser pour écrire la ligne de champ de votre fichier CSV.

Maintenant, laissez-moi vous montrer comment vous pouvez utiliser la méthode **writerow()** pour écrire une seule ligne dans votre fichier CSV.

Dans votre éditeur de code, créez un fichier avec le nom [*profiles1.py*](http://profiles1.py). Ensuite, écrivez le code suivant dans le fichier :

```python
import csv

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "age", "country"]
    
    writer.writerow(field)
    writer.writerow(["Oladele Damilola", "40", "Nigeria"])
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "United Kingdom"])
```

L'explication du code dans `profiles1.py` est la suivante :

1. La ligne un importe le module *csv* de Python.

2. La ligne deux est une ligne vide qui sépare le module importé du reste du code.

3. La ligne trois du code ouvre le fichier CSV en mode écriture (mode w) avec l'aide de la fonction `open()`.

4. La ligne quatre crée un objet writer CSV en appelant la fonction writer() et le stocke dans la variable `writer`.

5. La ligne cinq crée une variable nommée `fields`, qui stocke une liste composée de chaînes, chacune représentant le titre d'une colonne dans le fichier CSV.

6. La ligne six et suivantes écrit les données de champ et autres données dans le fichier CSV en appelant la méthode **writerow()** de l'objet writer CSV.

Une fois que vous avez terminé, allez dans votre terminal de ligne de commande et naviguez jusqu'au répertoire qui contient le fichier Python *profiles1.py*. Exécutez la commande suivante :

```sh
python profiles1.py
```

Vous devriez obtenir un fichier CSV nommé *profiles1.csv* dans votre répertoire de travail avec le texte suivant :

```bash
name,age,country
Oladele Damilola,40,Nigeria
Alina Hricko,23,Ukraine
Isabel Walter,50,United Kingdom
```

### La méthode `writerows()`

La méthode **writerows()** a une utilisation similaire à la méthode writerow(). La seule différence est que tandis que la méthode writerow() écrit une seule ligne dans un fichier CSV, vous pouvez utiliser la méthode **writerows()** pour écrire plusieurs lignes dans un fichier CSV.

Pour voir comment fonctionne la méthode **writerows()**, créez un fichier nommé *profiles2.py* dans votre répertoire de travail. Ensuite, écrivez le code suivant dans le fichier que vous avez créé :

```python
import csv

with open('profiles2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    row_list = [
        ["name", "age", "country"], 
        ["Oladele Damilola", "40", "Nigeria"], 
        ["Alina Hricko", "23", "Ukraine"], 
        ["Isabel Walter", "50", "United Kingdom"],
    ]
    
    writer.writerows(row_list)
```

Après avoir écrit le code dans votre fichier profiles2.py, allez dans votre terminal de ligne de commande et exécutez la commande suivante :

```sh
python profiles2.py
```

Maintenant, vous devriez avoir un fichier CSV nommé *profiles2.csv* dans votre répertoire de travail. Le fichier devrait contenir les données de la variable `row_list`.

## Comment créer un fichier CSV en utilisant la classe `csv.DictWriter`

Vous pouvez utiliser la classe `csv.DictWriter` pour écrire un fichier CSV à partir d'un dictionnaire. Cela diffère de la classe csv.writer, qui écrit dans un fichier CSV à partir d'une liste.

La syntaxe de **csv.DictWriter** est la suivante :

```python
class csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
```

Maintenant, laissez-moi vous expliquer la signification des différents paramètres de la syntaxe :

1. Le paramètre `csvfile` représente l'objet fichier avec la méthode `write()`.

2. Le paramètre `fieldnames` est une séquence de clés qui identifie l'ordre dans lequel Python passe les valeurs dans le dictionnaire.

3. Le paramètre `restval` est optionnel et spécifie la valeur à écrire si le dictionnaire manque d'une clé dans fieldnames.

4. Le paramètre `extrasaction` est optionnel et spécifie l'action à entreprendre si une clé n'est pas trouvée dans fieldnames. Définir ce paramètre sur `raise` lève une *ValueError*.

5. Le paramètre `dialect` est optionnel et représente le nom du dialecte que vous souhaitez utiliser.

La classe **csv.DictWriter** dispose de deux méthodes que vous pouvez utiliser pour écrire des données dans des fichiers CSV. Les méthodes sont les suivantes :

### La méthode `writeheader()`

Utilisez la méthode **writeheader()** pour écrire la première ligne de votre fichier csv en utilisant les `fieldnames` pré-spécifiés.

Pour voir comment fonctionne la méthode **writeheader()**, créez un nouveau fichier nommé *profiles3.py* dans votre répertoire de travail. Ensuite, écrivez le code suivant dans le fichier *profles3.py* en utilisant votre éditeur de code :

```python
import csv 

mydict =[{'name': 'Kelvin Gates', 'age': '19', 'country': 'USA'}, 
         {'name': 'Blessing Iroko', 'age': '25', 'country': 'Nigeria'}, 
         {'name': 'Idong Essien', 'age': '42', 'country': 'Ghana'}]
         
fields = ['name', 'age', 'country'] 

with open('profiles3.csv', 'w', newline='') as file: 
    writer = csv.DictWriter(file, fieldnames = fields)
    
    writer.writeheader()
```

L'explication du code dans *profiles3.py* est la suivante :

1. La ligne un importe le module *csv* de Python.

2. La ligne deux est un espace vide qui sépare le module csv de Python du reste du code.

3. La ligne trois stocke une liste contenant trois dictionnaires différents dans une variable nommée `mydict`. Les dictionnaires contiennent les données de différents profils.

4. La ligne sept stocke des chaînes, qui représentent le titre de chaque colonne du fichier CSV que vous souhaitez créer dans une variable nommée `fields`.

5. La ligne neuf ouvre le fichier *profiles3.csv* en mode écriture en utilisant la fonction `open()`.

6. La fonction `csv.DictWriter()` de la ligne dix crée l'objet writer de dictionnaire CSV.

7. La ligne douze passe la liste des dictionnaires à la fonction `writer.writeheader()` pour écrire les noms de champs pré-définis.

Une fois que vous avez terminé d'écrire le code, allez dans votre terminal de ligne de commande et naviguez jusqu'au répertoire qui contient le fichier python *profiles3.py*. Exécutez la commande suivante :

```sh
python profiles3.py
```

Maintenant, vous devriez obtenir un fichier CSV nommé *profiles3.csv* dans votre répertoire de travail qui contient le texte suivant :

```bash
name,age,country
```

### La méthode `writerows()`

La méthode **writerows()** a une utilisation similaire à la méthode writeheader(). Vous pouvez utiliser la méthode pour écrire toutes les lignes. La méthode écrit uniquement les valeurs et non les clés.

Pour utiliser la méthode **writerows()**, ajoutez cette ligne de code à votre code dans *profiles3.py* :

```python
writer.writerows(mydict)
```

Maintenant, supprimez le fichier *profiles3.csv* dans votre répertoire de travail et ré-exécutez la commande suivante dans votre terminal de ligne de commande :

```sh
python profiles3.py
```

Vous devriez maintenant avoir un nouveau fichier CSV nommé *profiles3.csv* dans votre répertoire de travail qui contient le texte suivant :

```bash
name,age,country
Kelvin Gates,19,USA
Blessing Iroko,25,Nigeria
Idong Essien,42,Ghana
```

## Conclusion

Bien que CSV tire son nom de la **virgule**, la virgule n'est qu'un délimiteur qui sépare les données.

Vous devez savoir qu'une virgule est un délimiteur populaire que vous trouverez dans la plupart des fichiers CSV. Cependant, le délimiteur pourrait également être autre chose. Par exemple, vous pouvez utiliser un point-virgule pour séparer les données au lieu d'une virgule.

Si vous aimez ce tutoriel, n'hésitez pas à [me suivre sur Twitter](https://twitter.com/activus_d) et à me faire un petit coucou.

### Références et lectures complémentaires

* [https://docs.python.org/3/library/csv.html?highlight=csv](https://docs.python.org/3/library/csv.html?highlight=csv)