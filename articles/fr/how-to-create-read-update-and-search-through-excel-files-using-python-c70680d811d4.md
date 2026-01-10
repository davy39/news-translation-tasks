---
title: Comment créer, lire, mettre à jour et rechercher dans des fichiers Excel en
  utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T10:35:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-read-update-and-search-through-excel-files-using-python-c70680d811d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*REWATbNLWv5uvpB0UKedEQ.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment créer, lire, mettre à jour et rechercher dans des fichiers Excel
  en utilisant Python
seo_desc: 'By Goran Aviani

  This article will show in detail how to work with Excel files and how to modify
  specific data with Python.

  First we will learn how to work with CSV files by reading, writing and updating
  them. Then we will take a look how to read file...'
---

Par Goran Aviani

Cet article montrera en détail comment travailler avec des fichiers Excel et comment modifier des données spécifiques avec Python.

Tout d'abord, nous apprendrons comment travailler avec des fichiers CSV en les lisant, en les écrivant et en les mettant à jour. Ensuite, nous verrons comment lire des fichiers, les filtrer par feuilles, rechercher des lignes/colonnes et mettre à jour des cellules de fichiers xlsx.

Commençons par le format de tableur le plus simple : le CSV.

### Partie 1 — Le fichier CSV

Un fichier CSV est un fichier de valeurs séparées par des virgules, où les données en texte brut sont affichées dans un format tabulaire. Ils peuvent être utilisés avec n'importe quel programme de tableur, tel que Microsoft Office Excel, Google Spreadsheets ou LibreOffice Calc.

Les fichiers CSV ne sont pas comme les autres fichiers de tableur, car ils ne permettent pas de sauvegarder des cellules, des colonnes, des lignes ou des formules. Leur limitation est qu'ils permettent également une seule feuille par fichier. Mon plan pour cette première partie de l'article est de vous montrer comment créer des fichiers CSV en utilisant Python 3 et le module de bibliothèque standard CSV.

Ce tutoriel se terminera avec deux dépôts GitHub et une application web en direct qui utilise effectivement le code de la deuxième partie de ce tutoriel (mais mis à jour et modifié pour un but spécifique).

### Écrire dans des fichiers CSV

Tout d'abord, ouvrez un nouveau fichier Python et importez le module CSV de Python.

```
import csv
```

#### Module CSV

Le module CSV inclut toutes les méthodes nécessaires intégrées. Celles-ci incluent :

* csv.reader
* csv.writer
* csv.DictReader
* csv.DictWriter
* et autres

Dans ce guide, nous allons nous concentrer sur les méthodes writer, DictWriter et DictReader. Celles-ci vous permettent de modifier, de manipuler et de manipuler les données stockées dans un fichier CSV.

Dans la première étape, nous devons définir le nom du fichier et l'enregistrer comme une variable. Nous devrions faire de même avec l'en-tête et les informations de données.

```py
filename = "imdb_top_4.csv"
header = ("Rank", "Rating", "Title")
data = [
(1, 9.2, "The Shawshank Redemption(1994)"),
(2, 9.2, "The Godfather(1972)"),
(3, 9, "The Godfather: Part II(1974)"),
(4, 8.9, "Pulp Fiction(1994)")
]
```

Maintenant, nous devons créer une fonction nommée _writer_ qui prendra trois paramètres : _header_, _data_ et _filename_.

```py
def writer(header, data, filename):
  pass
```

L'étape suivante consiste à modifier la fonction _writer_ pour qu'elle crée un fichier contenant les données des variables _header_ et _data_. Cela se fait en écrivant la première ligne de la variable _header_, puis en écrivant quatre lignes de la variable _data_ (il y a quatre lignes car il y a quatre tuples à l'intérieur de la liste).

```py
def writer(header, data, filename):
  with open (filename, "w", newline = "") as csvfile:
    movies = csv.writer(csvfile)
    movies.writerow(header)
    for x in data:
      movies.writerow(x)
```

> La [documentation officielle de Python](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters) décrit comment fonctionne la méthode csv.writer. Je vous suggère fortement de prendre une minute pour la lire.

**Et voilà !** Vous avez créé votre premier fichier CSV nommé imdb_top_4.csv. Ouvrez ce fichier avec votre application de tableur préférée et vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DuYsqu8EFzU15u_0HgNDKg.png)
_Utilisation de LibreOffice Calc pour voir le résultat._

Le résultat pourrait être écrit comme ceci si vous choisissez d'ouvrir le fichier dans une autre application :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q0U_MBj6mr3ekidC299lbQ.png)
_Utilisation de SublimeText pour voir le résultat._

### Mettre à jour les fichiers CSV

Pour mettre à jour ce fichier, vous devez créer une nouvelle fonction nommée _updater_ qui ne prendra qu'un seul paramètre appelé _filename_.

```py
def updater(filename):
    with open(filename, newline= "") as file:
        readData = [row for row in csv.DictReader(file)]
        # print(readData)
        readData[0]['Rating'] = '9.4'
        # print(readData)

    readHeader = readData[0].keys()
    writer(readHeader, readData, filename, "update")
```

Cette fonction ouvre d'abord le fichier défini dans la variable _filename_, puis sauvegarde toutes les données qu'elle lit depuis le fichier dans une variable nommée _readData_. La deuxième étape consiste à coder en dur la nouvelle valeur et à la placer à la place de l'ancienne dans la position _readData[0]['Rating']_.

La dernière étape de la fonction consiste à appeler la fonction _writer_ en ajoutant un nouveau paramètre _update_ qui indiquera à la fonction que vous effectuez une mise à jour.

> csv.DictReader est expliqué plus en détail dans la documentation officielle de Python [ici](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters).

Pour que _writer_ fonctionne avec un nouveau paramètre, vous devez ajouter un nouveau paramètre partout où _writer_ est défini. Retournez à l'endroit où vous avez appelé pour la première fois la fonction _writer_ et ajoutez "write" comme nouveau paramètre :

```py
writer(header, data, filename, "write")
```

Juste en dessous de l'appel de la fonction writer, appelez _updater_ et passez le paramètre _filename_ :

```py
writer(header, data, filename, "write")
updater(filename)
```

Maintenant, vous devez modifier la fonction _writer_ pour qu'elle prenne un nouveau paramètre nommé _option_ :

```py
def writer(header, data, filename, option):
```

Désormais, nous nous attendons à recevoir deux options différentes pour la fonction _writer_ (_write_ et _update_). Pour cette raison, nous devons ajouter deux instructions if pour prendre en charge cette nouvelle fonctionnalité. La première partie de la fonction sous "if option == "write" :" vous est déjà connue. Vous devez simplement ajouter la section de code "elif option == "update" :" et la partie _else_ telles qu'elles sont écrites ci-dessous :

```py
def writer(header, data, filename, option):
        with open (filename, "w", newline = "") as csvfile:
            if option == "write":

                movies = csv.writer(csvfile)
                movies.writerow(header)
                for x in data:
                    movies.writerow(x)
            elif option == "update":
                writer = csv.DictWriter(csvfile, fieldnames = header)
                writer.writeheader()
                writer.writerows(data)
            else:
                print("Option is not known")
```

**Bravo !** Vous avez terminé !

Maintenant, votre code devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*vPoREgLGJU8VmB5k)
_Le code._

Vous pouvez également trouver le code ici :

[https://github.com/GoranAviani/CSV-Viewer-and-Editor](https://github.com/GoranAviani/CSV-Viewer-and-Editor)

Dans la première partie de cet article, nous avons vu comment travailler avec des fichiers CSV. Nous avons créé et mis à jour un tel fichier.

### Partie 2 — Le fichier xlsx

Pendant plusieurs week-ends, j'ai travaillé sur ce projet. J'ai commencé à travailler dessus parce qu'il y avait un besoin pour ce type de solution dans mon entreprise. Ma première idée était de construire cette solution directement dans le système de mon entreprise, mais alors je n'aurais rien à écrire, hein ?

J'ai construit cette solution en utilisant Python 3 et la bibliothèque _openpyxl_. La raison pour laquelle j'ai choisi _openpyxl_ est qu'elle représente une solution complète pour créer des feuilles de calcul, les charger, les mettre à jour, les renommer et les supprimer. Elle permet également de lire ou d'écrire dans des lignes et des colonnes, de fusionner ou de séparer des cellules ou de créer des graphiques Excel Python, etc.

### Terminologie et informations de base d'Openpyxl

* Workbook est le nom d'un fichier Excel dans Openpyxl.
* Un workbook se compose de feuilles (par défaut, 1 feuille). Les feuilles sont référencées par leurs noms.
* Une feuille se compose de lignes (lignes horizontales) commençant par le numéro 1 et de colonnes (lignes verticales) commençant par la lettre A.
* Les lignes et les colonnes forment une grille et créent des cellules qui peuvent contenir des données (valeur numérique ou chaîne) ou des formules.

> Openpyxl est bien documenté et je vous conseille de jeter un œil [ici](https://openpyxl.readthedocs.io/en/stable/).

La première étape consiste à ouvrir votre environnement Python et à installer _openpyxl_ dans votre terminal :

```
pip install openpyxl
```

Ensuite, importez _openpyxl_ dans votre projet, puis chargez un workbook dans la variable _theFile_.

```py
import openpyxl

theFile = openpyxl.load_workbook('Customers1.xlsx')
print(theFile.sheetnames)
currentSheet = theFile['customers 1']
print(currentSheet['B4'].value)
```

Comme vous pouvez le voir, ce code imprime toutes les feuilles par leurs noms. Il sélectionne ensuite la feuille nommée "customers 1" et la sauvegarde dans une variable _currentSheet_. Dans la dernière ligne, le code imprime la valeur située dans la position B4 de la feuille "customers 1".

Ce code fonctionne comme il se doit, mais il est très codé en dur. Pour le rendre plus dynamique, nous allons écrire un code qui :

* _Lit le fichier_
* _Obtient tous les noms de feuilles_
* _Parcourt toutes les feuilles_
* _Dans la dernière étape, le code imprime les valeurs situées dans les champs B4 de chaque feuille trouvée dans le workbook._

```py
import openpyxl

theFile = openpyxl.load_workbook('Customers1.xlsx')
allSheetNames = theFile.sheetnames

print("All sheet names {} " .format(theFile.sheetnames))


for x in allSheetNames:
    print("Current sheet name is {}" .format(x))
    currentSheet = theFile[x]
    print(currentSheet['B4'].value)
```

C'est mieux que avant, mais c'est toujours une solution codée en dur et elle suppose toujours que la valeur que vous recherchez se trouve dans la cellule B4, ce qui est simplement ridicule :)

Je m'attends à ce que votre projet ait besoin de rechercher dans toutes les feuilles du fichier Excel une valeur spécifique. Pour ce faire, nous allons ajouter une boucle for supplémentaire dans la plage "ABCDEF" et simplement imprimer les noms de cellules et leurs valeurs.

```py
import openpyxl

theFile = openpyxl.load_workbook('Customers1.xlsx')
allSheetNames = theFile.sheetnames

print("All sheet names {} " .format(theFile.sheetnames))


for sheet in allSheetNames:
    print("Current sheet name is {}" .format(sheet))
    currentSheet = theFile[sheet]
    # print(currentSheet['B4'].value)

    #print max numbers of wors and colums for each sheet
    #print(currentSheet.max_row)
    #print(currentSheet.max_column)

    for row in range(1, currentSheet.max_row + 1):
        #print(row)
        for column in "ABCDEF":  # Here you can add or reduce the columns
            cell_name = "{}{}".format(column, row)
            #print(cell_name)
            print("cell position {} has value {}".format(cell_name, currentSheet[cell_name].value))
```

Nous avons fait cela en introduisant la boucle "for row in range..". La plage de la boucle for est définie de la cellule de la ligne 1 au nombre maximum de lignes de la feuille. La deuxième boucle for recherche dans les noms de colonnes prédéfinis "ABCDEF". Dans la deuxième boucle, nous afficherons la position complète de la cellule (nom de la colonne et numéro de la ligne) et une valeur.

Cependant, dans cet article, ma tâche est de trouver une colonne spécifique nommée "telephone" puis de parcourir toutes les lignes de cette colonne. Pour ce faire, nous devons modifier le code comme ci-dessous.

```py
import openpyxl

theFile = openpyxl.load_workbook('Customers1.xlsx')
allSheetNames = theFile.sheetnames

print("All sheet names {} " .format(theFile.sheetnames))


def find_specific_cell():
    for row in range(1, currentSheet.max_row + 1):
        for column in "ABCDEFGHIJKL":  # Here you can add or reduce the columns
            cell_name = "{}{}".format(column, row)
            if currentSheet[cell_name].value == "telephone":
                #print("{1} cell is located on {0}" .format(cell_name, currentSheet[cell_name].value))
                print("cell position {} has value {}".format(cell_name, currentSheet[cell_name].value))
                return cell_name

for sheet in allSheetNames:
    print("Current sheet name is {}" .format(sheet))
    currentSheet = theFile[sheet]
```

Ce code modifié parcourt toutes les cellules de chaque feuille, et comme avant, la plage de lignes est dynamique et la plage de colonnes est spécifique. Le code parcourt les cellules et recherche une cellule qui contient le texte "telephone". Une fois que le code trouve la cellule spécifique, il notifie l'utilisateur dans quelle cellule le texte est situé. Le code fait cela pour chaque cellule à l'intérieur de toutes les feuilles qui sont dans le fichier Excel.

L'étape suivante consiste à parcourir toutes les lignes de cette colonne spécifique et à imprimer les valeurs.

```py
import openpyxl

theFile = openpyxl.load_workbook('Customers1.xlsx')
allSheetNames = theFile.sheetnames

print("All sheet names {} " .format(theFile.sheetnames))


def find_specific_cell():
    for row in range(1, currentSheet.max_row + 1):
        for column in "ABCDEFGHIJKL":  # Here you can add or reduce the columns
            cell_name = "{}{}".format(column, row)
            if currentSheet[cell_name].value == "telephone":
                #print("{1} cell is located on {0}" .format(cell_name, currentSheet[cell_name].value))
                print("cell position {} has value {}".format(cell_name, currentSheet[cell_name].value))
                return cell_name

def get_column_letter(specificCellLetter):
    letter = specificCellLetter[0:-1]
    print(letter)
    return letter

def get_all_values_by_cell_letter(letter):
    for row in range(1, currentSheet.max_row + 1):
        for column in letter:
            cell_name = "{}{}".format(column, row)
            #print(cell_name)
            print("cell position {} has value {}".format(cell_name, currentSheet[cell_name].value))



for sheet in allSheetNames:
    print("Current sheet name is {}" .format(sheet))
    currentSheet = theFile[sheet]
    specificCellLetter = (find_specific_cell())
    letter = get_column_letter(specificCellLetter)

    get_all_values_by_cell_letter(letter)

```

Cela est fait en ajoutant une fonction nommée _get_column_letter_ qui trouve une lettre de colonne. Après avoir trouvé la lettre de la colonne, nous parcourons toutes les lignes de cette colonne spécifique. Cela est fait avec la fonction _get_all_values_by_cell_letter_ qui imprimera toutes les valeurs de ces cellules.

### Conclusion

**Bra gjort !** Il y a beaucoup de choses que vous pouvez faire après cela. Mon plan était de construire une application en ligne qui standardiserait tous les numéros de téléphone suédois pris à partir d'une boîte de texte et offrirait aux utilisateurs la possibilité de simplement copier les résultats à partir de la même boîte de texte. La deuxième étape de mon plan était d'étendre la fonctionnalité de l'application web pour prendre en charge le téléchargement de fichiers Excel, le traitement des numéros de téléphone à l'intérieur de ces fichiers (les standardiser à un format suédois) et offrir les fichiers traités aux utilisateurs.

J'ai accompli ces deux tâches et vous pouvez les voir en direct dans la page Outils de mon site _Incodaq.com_ :

> [https://tools.incodaq.com/](https://tools.incodaq.com/)

De plus, le code de la deuxième partie de cet article est disponible sur GitHub :

> [https://github.com/GoranAviani/Manipulate-Excel-spreadsheets](https://github.com/GoranAviani/Manipulate-Excel-spreadsheets)

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci sur mon profil Medium : [https://medium.com/@goranaviani](https://medium.com/@goranaviani) et d'autres choses amusantes que je construis sur ma page GitHub : [https://github.com/GoranAviani](https://github.com/GoranAviani)