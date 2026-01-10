---
title: Comment travailler avec les Data Frames et les fichiers CSV dans R — Une introduction
  détaillée avec des exemples
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2020-06-21T13:57:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-data-frames-and-csv-files-in-r
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Data-frames-and-CSV-files.png
tags: []
seo_title: Comment travailler avec les Data Frames et les fichiers CSV dans R — Une
  introduction détaillée avec des exemples
seo_desc: 'Welcome! If you want to start diving into data science and statistics,
  then data frames, CSV files, and R will be essential tools for you. Let''s see how
  you can use their amazing capabilities.

  In this article, you will learn:


  What CSV files are and ...'
---

**Bienvenue !** Si vous souhaitez vous lancer dans la science des données et les statistiques, alors les data frames, les fichiers CSV et R seront des outils essentiels pour vous. Voyons comment vous pouvez utiliser leurs capacités incroyables.

**Dans cet article, vous apprendrez :**

* Ce que sont les fichiers CSV et à quoi ils servent.
* Comment créer des fichiers CSV en utilisant Google Sheets.
* Comment lire des fichiers CSV dans R.
* Ce que sont les Data Frames et à quoi ils servent.
* Comment accéder aux éléments d'un data frame.
* Comment modifier un data frame.
* Comment ajouter et supprimer des lignes et des colonnes.

Nous utiliserons RStudio, un IDE (Integrated Development Environment) open-source pour exécuter les exemples.

**Commençons ! ✨**

## 📝 Introduction aux fichiers CSV

Les fichiers CSV (Comma-separated Values) peuvent être considérés comme l'un des éléments de base de l'analyse de données car ils sont utilisés pour stocker des données représentées sous la forme d'un tableau. 

Dans ce fichier, les valeurs sont séparées par des virgules pour représenter les différentes colonnes du tableau, comme dans cet exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-153.png)
_Fichier CSV_

Nous allons générer ce fichier en utilisant Google Sheets.

## 📝 Comment créer un fichier CSV en utilisant Google Sheets

Créons votre premier fichier CSV en utilisant Google Sheets.

**Étape 1 :** Allez sur le [site web de Google Sheets](https://www.google.com/sheets/about/) et cliquez sur "Go to Google Sheets" : 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-227.png)

**💡 Astuce :** Vous pouvez accéder à Google Sheets en cliquant sur le bouton situé en haut à droite de la page d'accueil de Google :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-228.png)

Si nous zoomons, nous voyons le bouton "Sheets" :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-156.png)

💡 **Astuce :** Pour utiliser Google Sheets, vous devez avoir un compte Gmail. Alternativement, vous pouvez créer un fichier CSV en utilisant MS Excel ou un autre éditeur de feuilles de calcul.

Vous verrez ce panneau :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-157.png)

**Étape 2 :** Créez une feuille de calcul vierge en cliquant sur le bouton "+".

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-158.png)

Vous avez maintenant une nouvelle feuille de calcul vide :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-159.png)

**Étape 3 :** Changez le nom de la feuille de calcul en `students_data`. Nous aurons besoin d'utiliser le nom du fichier pour travailler avec les data frames. Écrivez le nouveau nom et cliquez sur Entrée pour confirmer le changement.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-162.png)

**Étape 4 :** Dans la première ligne de la feuille de calcul, écrivez les titres des colonnes.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-160.png)

Lorsque vous importez un fichier CSV dans R, les titres des colonnes sont appelés **variables**. Nous allons définir six variables : `first_name`, `last_name`, `age`, `num_siblings`, `num_pets`, et `eye_color`, comme vous pouvez le voir juste ici :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-163.png)

💡 **Astuce :** Remarquez que les noms sont écrits en minuscules et que les mots sont séparés par un trait de soulignement. Ce n'est pas obligatoire, mais puisque vous devrez accéder à ces noms dans R, il est très courant d'utiliser ce format. 

**Étape 5 :** Entrez les données pour chacune des colonnes. 

Lorsque vous lisez le fichier dans R, chaque ligne est appelée une **observation**, et elle correspond aux données recueillies auprès d'un individu, d'un animal, d'un objet ou d'une entité.

Dans ce cas, chaque ligne correspond aux données d'un étudiant :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-164.png)

**Étape 6 :** Téléchargez le fichier CSV en cliquant sur `Fichier -> Télécharger -> Valeurs séparées par des virgules`, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-165.png)

**Étape 7 :** Renommez le fichier CSV. Vous devrez supprimer "Sheet1" du nom par défaut car Google Sheet l'ajoutera automatiquement au nom du fichier. 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-169.png)

Excellent travail ! Maintenant, vous avez votre fichier CSV et il est temps de commencer à travailler avec lui dans R. 

## 📝 Comment lire un fichier CSV dans R

Dans RStudio, la première étape avant de lire un fichier CSV est de s'assurer que votre répertoire de travail actuel est le répertoire où se trouve le fichier CSV. 

💡 **Astuce :** Si ce n'est pas le cas, vous devrez utiliser le chemin complet vers le fichier.

### Changer le répertoire de travail actuel

Vous pouvez changer votre répertoire de travail actuel dans ce panneau :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-172.png)

Si nous zoomons, vous pouvez voir le chemin actuel (1) et sélectionner le nouveau en cliquant sur le bouton ellipsis (`...`) à droite (2) :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-171.png)

💡 **Astuce :** Vous pouvez également vérifier votre répertoire de travail actuel avec `getwd()` dans la console interactive. 

Ensuite, cliquez sur "Plus" et "Définir comme répertoire de travail". 

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-175.png)

### Lire le fichier CSV

Une fois que vous avez configuré votre répertoire de travail actuel, vous pouvez lire le fichier CSV avec cette commande :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-176.png)

En code R, nous avons ceci :

```r
> students_data <- read.csv("students_data.csv")
```

💡 **Astuce :** Nous l'assignons à la variable `students_data` pour accéder aux données du fichier CSV avec cette variable. Dans R, nous pouvons séparer les mots en utilisant des points `.`, des traits de soulignement `_`, `UpperCamelCase`, ou `lowerCamelCase`.

Après avoir exécuté cette commande, vous verrez ceci dans le panneau en haut à droite :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-177.png)

Maintenant, vous avez une variable définie dans l'environnement ! Voyons ce que sont les data frames et comment ils sont étroitement liés aux fichiers CSV.

## 📝 Introduction aux Data Frames

Les data frames sont le format numérique standard utilisé pour stocker des données statistiques sous la forme d'un tableau. **Lorsque vous lisez un fichier CSV dans R, un data frame est généré**. 

Nous pouvons confirmer cela en vérifiant le type de la variable avec la fonction `class` :

```r
> class(students_data)
[1] "data.frame"
```

Cela a du sens, n'est-ce pas ? Les fichiers CSV contiennent des données représentées sous la forme d'un tableau et les data frames représentent ces données tabulaires dans votre code, ils sont donc profondément connectés.

Si vous entrez cette variable dans la console interactive, vous verrez le contenu du fichier CSV :

```r
> students_data
  first_name last_name age num_siblings num_pets eye_color
1      Emily    Dawson  15            2        5      BLUE
2       Rose Patterson  14            5        0     GREEN
3  Alexander     Smith  16            0        2     BROWN
4       Nora    Navona  16            4       10     GREEN
5       Gino      Sand  17            3        8      BLUE
```

### Plus d'informations sur le Data Frame

Vous avez plusieurs alternatives différentes pour voir le nombre de variables et d'observations du data frame :

* Votre première option est de regarder le panneau en haut à droite qui montre les variables actuellement définies dans l'environnement. Ce data frame a 5 observations (lignes) et 6 variables (colonnes) :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-178.png)

* Une autre alternative est d'utiliser les fonctions `nrow` et `ncol` dans la console interactive ou dans votre programme, en passant le data frame comme argument. Nous obtenons les mêmes résultats : 5 lignes et 6 colonnes.

```r
> nrow(students_data)
[1] 5
> ncol(students_data)
[1] 6
```

* Vous pouvez également voir plus d'informations sur le data frame en utilisant la fonction `str` : 

```r
> str(students_data)
'data.frame':	5 obs. of  6 variables:
 $ first_name  : Factor w/ 5 levels "Alexander","Emily",..: 2 5 1 4 3
 $ last_name   : Factor w/ 5 levels "Dawson","Navona",..: 1 3 5 2 4
 $ age         : int  15 14 16 16 17
 $ num_siblings: int  2 5 0 4 3
 $ num_pets    : int  5 0 2 10 8
 $ eye_color   : Factor w/ 3 levels "BLUE","BROWN",..: 1 3 2 3 1
```

Cette fonction (appliquée à un data frame) vous indique :

* Le nombre d'observations (lignes).
* Le nombre de variables (colonnes).
* Les noms des variables.
* Les types de données des variables.
* Plus d'informations sur les variables.

Vous pouvez voir que cette fonction est vraiment utile lorsque vous voulez en savoir plus sur les données avec lesquelles vous travaillez. 

💡 **Astuce :** Dans R, un "Factor" est une variable qualitative, c'est-à-dire une variable dont les valeurs représentent des catégories. Par exemple, `eye_color` a les valeurs `"BLUE"`, `"BROWN"`, `"GREEN"` qui sont des catégories, donc comme vous pouvez le voir dans la sortie de `str` ci-dessus, cette variable est automatiquement définie comme un "factor" lorsque le fichier CSV est lu dans R.

## 📝 Data Frames : Opérations et Fonctions Clés

Maintenant, vous savez comment voir plus d'informations sur le data frame. Mais la magie des data frames réside dans les capacités et fonctionnalités incroyables qu'ils offrent, alors voyons cela plus en détail. 

### Comment accéder à une valeur d'un Data Frame

Les data frames sont comme des matrices, donc vous pouvez accéder à des valeurs individuelles en utilisant deux indices entourés de crochets et séparés par une virgule pour indiquer quelles lignes et quelles colonnes vous souhaitez inclure dans le résultat, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-181.png)

Par exemple, si nous voulons accéder à la valeur de `eye_color` (colonne 6) du quatrième étudiant dans les données (ligne 4) :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-182.png)

Nous devons utiliser cette commande :

```r
> students_data[4, 6]
```

💡 **Astuce :** Dans R, les indices commencent à `1` et la première ligne avec les noms des variables n'est pas comptée.

Voici la sortie :

```r
[1] GREEN
Levels: BLUE BROWN GREEN
```

Vous pouvez voir que la valeur est `"GREEN"`. Les variables de type "factor" ont des "levels" qui représentent les différentes catégories ou valeurs qu'elles peuvent prendre. Cette sortie nous indique les niveaux de la variable `eye_color`.

### Comment accéder aux lignes et colonnes d'un Data Frame

Nous pouvons également utiliser cette syntaxe pour accéder à une plage de lignes et de colonnes afin d'obtenir une portion de la matrice originale, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-179.png)

Par exemple, si nous voulons obtenir l'âge et le nombre de frères et sœurs des troisième, quatrième et cinquième étudiants de la liste, nous utiliserions :

```r
> students_data[3:5, 3:4]

  age num_siblings
3  16            0
4  16            4
5  17            3
```

**💡 Astuce :** La syntaxe de base pour définir un intervalle dans R est `<start>:<end>`. Notez que ces indices sont inclusifs, donc les troisième et cinquième éléments sont inclus dans l'exemple ci-dessus lorsque nous écrivons `3:5`. 

Si nous voulons obtenir toutes les lignes ou colonnes, nous omettons simplement l'intervalle et incluons la virgule, comme ceci :

```r
> students_data[3:5,]

  first_name last_name age num_siblings num_pets eye_color
3  Alexander     Smith  16            0        2     BROWN
4       Nora    Navona  16            4       10     GREEN
5       Gino      Sand  17            3        8      BLUE
```

Nous n'avons pas inclus d'intervalle pour les colonnes après la virgule dans `students_data[3:5,]`, donc nous obtenons toutes les colonnes du data frame pour les trois lignes que nous avons spécifiées.

De même, nous pouvons obtenir toutes les lignes pour une plage spécifique de colonnes si nous omettons les lignes :

```r
> students_data[, 1:3]

  first_name last_name age
1      Emily    Dawson  15
2       Rose Patterson  14
3  Alexander     Smith  16
4       Nora    Navona  16
5       Gino      Sand  17
```

**💡 Astuce :** Notez que vous devez toujours inclure la virgule dans les deux cas.

### Comment accéder à une colonne

Il existe trois façons d'accéder à une colonne entière :

* **Option #1 :** pour accéder à une colonne et la retourner sous forme de data frame, vous pouvez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-184.png)

Par exemple :

```r
> students_data["first_name"]

  first_name
1      Emily
2       Rose
3  Alexander
4       Nora
5       Gino
```

* **Option #2 :** pour obtenir une colonne sous forme de vecteur (séquence), vous pouvez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-185.png)

**💡 Astuce :** Remarquez l'utilisation du symbole `$`.

Par exemple :

```python
> students_data$first_name

[1] Emily     Rose      Alexander Nora      Gino     
Levels: Alexander Emily Gino Nora Rose
```

* **Option #3 :** Vous pouvez également utiliser cette syntaxe pour obtenir la colonne sous forme de vecteur (voir ci-dessous). Cela est équivalent à la syntaxe précédente :

```r
> students_data[["first_name"]]

[1] Emily     Rose      Alexander Nora      Gino     
Levels: Alexander Emily Gino Nora Rose
```

### Comment filtrer les lignes d'un Data Frame

Vous pouvez filtrer les lignes d'un data frame pour obtenir une portion de la matrice qui répond à certaines conditions. 

Pour cela, nous utilisons cette syntaxe, en passant la condition comme premier élément entre crochets, puis une virgule, et enfin en laissant le deuxième élément vide.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-190.png)

Par exemple, pour obtenir toutes les lignes pour lesquelles `students_data$age > 16`, nous utiliserions :

```r
> students_data[students_data$age > 16,]

  first_name last_name age num_siblings num_pets eye_color
5       Gino      Sand  17            3        8      BLUE
```

Nous obtenons un data frame avec les lignes qui répondent à cette condition.

### Filtrer les lignes et choisir les colonnes

Vous pouvez combiner cette condition avec une plage de colonnes :

```r
> students_data[students_data$age > 16, 3:6]

  age num_siblings num_pets eye_color
5  17            3        8      BLUE
```

Nous obtenons les lignes qui répondent à la condition et les colonnes dans la plage `3:6`. 

## 📝 Comment modifier les Data Frames

Vous pouvez modifier des valeurs individuelles d'un data frame, ajouter des colonnes, ajouter des lignes et les supprimer. **Voyons comment vous pouvez faire cela !**

### Comment changer une valeur

Pour changer une valeur individuelle du data frame, vous devez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-191.png)

Par exemple, si nous voulons changer la valeur qui se trouve actuellement à la ligne 4 et à la colonne 6, indiquée en bleu ici :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-182.png)

Nous devons utiliser cette ligne de code :

```
students_data[4, 6] <- "BROWN"
```

**💡 Astuce :** Vous pouvez également utiliser `=` comme opérateur d'assignation.

Voici la sortie. La valeur a été changée avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-193.png)

**💡 Astuce :** Rappelez-vous que la première ligne du fichier CSV n'est pas comptée comme la première ligne car elle contient les noms des variables. 

### Comment ajouter des lignes à un Data Frame

Pour ajouter une ligne à un data frame, vous devez utiliser la fonction `rbind` :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-194.png)

Cette fonction prend deux arguments :

* Le data frame que vous souhaitez modifier.
* Une liste avec les données de la nouvelle ligne. Pour créer la liste, vous pouvez utiliser la fonction `list()` avec chaque valeur séparée par une virgule.

Voici un exemple :

```r
> rbind(students_data, list("William", "Smith", 14, 7, 3, "BROWN"))
```

La sortie est :

```r
  first_name last_name age num_siblings num_pets eye_color
1      Emily    Dawson  15            2        5      BLUE
2       Rose Patterson  14            5        0     GREEN
3  Alexander     Smith  16            0        2     BROWN
4       Nora    Navona  16            4       10     BROWN
5       Gino      Sand  17            3        8      BLUE
6       <NA>     Smith  14            7        3     BROWN
```

**Mais attendez !** Un message d'avertissement a été affiché :

```r
Warning message:
In `[<-.factor`(`*tmp*`, ri, value = "William") :
  invalid factor level, NA generated
```

Et remarquez la première valeur de la sixième ligne, c'est `<NA>` :

```python
6       <NA>     Smith  14            7        3     BROWN
```

Cela s'est produit parce que la variable `first_name` a été automatiquement définie comme un facteur lorsque nous avons lu le fichier CSV et les facteurs ont des "catégories" (niveaux) fixes. 

Vous ne pouvez pas ajouter un nouveau niveau (valeur - `"William"`) à cette variable sauf si vous lisez le fichier CSV avec la valeur `FALSE` pour le paramètre `stringsAsFactors`, comme montré ci-dessous :

```r
> students_data <- read.csv("students_data.csv", stringsAsFactors = FALSE)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-196.png)

Maintenant, si nous essayons d'ajouter cette ligne, le data frame est modifié avec succès.

```r
> students_data <- rbind(students_data, list("William", "Smith", 14, 7, 3, "BROWN"))
> students_data

  first_name last_name age num_siblings num_pets eye_color
1      Emily    Dawson  15            2        5      BLUE
2       Rose Patterson  14            5        0     GREEN
3  Alexander     Smith  16            0        2     BROWN
4       Nora    Navona  16            4       10     GREEN
5       Gino      Sand  17            3        8      BLUE
6    William     Smith  14            7        3     BROWN
```

**💡 Astuce :** Notez que si vous relisez le fichier CSV et l'assignez à la même variable, toutes les modifications apportées précédemment seront supprimées et vous verrez le data frame original. Vous devez ajouter cet argument à la première ligne de code qui lit le fichier CSV et ensuite apporter des modifications.

### Comment ajouter des colonnes à un Data Frame

Ajouter des colonnes à un data frame est beaucoup plus simple. Vous devez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-197.png)

Par exemple :

```r
> students_data$GPA <- c(4.0, 3.5, 3.2, 3.15, 2.9, 3.0)
```

**💡 Astuce :** Le nombre d'éléments doit être égal au nombre de lignes du data frame.

La sortie montre le data frame avec la nouvelle colonne GPA :

```r
> students_data

  first_name last_name age num_siblings num_pets eye_color  GPA
1      Emily    Dawson  15            2        5      BLUE 4.00
2       Rose Patterson  14            5        0     GREEN 3.50
3  Alexander     Smith  16            0        2     BROWN 3.20
4       Nora    Navona  16            4       10     GREEN 3.15
5       Gino      Sand  17            3        8      BLUE 2.90
6    William     Smith  14            7        3     BROWN 3.00
```

### Comment supprimer des colonnes

Pour supprimer des colonnes d'un data frame, vous devez utiliser cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-198.png)

Lorsque vous attribuez la valeur Null à une colonne, cette colonne est automatiquement supprimée du data frame. 

Par exemple, pour supprimer la colonne `age`, nous utilisons : 

```r
> students_data$age <- NULL
```

La sortie est :

```r
> students_data

  first_name last_name num_siblings num_pets eye_color  GPA
1      Emily    Dawson            2        5      BLUE 4.00
2       Rose Patterson            5        0     GREEN 3.50
3  Alexander     Smith            0        2     BROWN 3.20
4       Nora    Navona            4       10     GREEN 3.15
5       Gino      Sand            3        8      BLUE 2.90
6    William     Smith            7        3     BROWN 3.00
```

### Comment supprimer des lignes

Pour supprimer des lignes d'un data frame, vous pouvez utiliser des indices et des plages. Par exemple, pour supprimer la première ligne d'un data frame :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-200.png)

Le `[-1,]` prend une portion du data frame qui n'inclut pas la première ligne. Ensuite, cette portion est assignée à la même variable.

Si nous avons ce data frame et que nous voulons supprimer la première ligne :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-230.png)

La sortie est un data frame qui n'inclut pas la première ligne :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-231.png)

En général, pour supprimer une ligne spécifique, vous devez utiliser cette syntaxe où `<row_num>` est la ligne que vous souhaitez supprimer :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-229.png)

**💡 Astuce :** Remarquez le signe `-` avant le numéro de ligne.

Par exemple, si nous voulons supprimer la ligne 4 de ce data frame :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-232.png)

La sortie est :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-233.png)

Comme vous pouvez le voir, la ligne 4 a été supprimée avec succès.

## 📝 En résumé

* Les fichiers CSV sont des fichiers de valeurs séparées par des virgules utilisés pour représenter des données sous la forme d'un tableau. Ces fichiers peuvent être lus en utilisant R et RStudio.
* Les data frames sont utilisés dans R pour représenter des données tabulaires. Lorsque vous lisez un fichier CSV, un data frame est créé pour stocker les données. 
* Vous pouvez accéder et modifier les valeurs, les lignes et les colonnes d'un data frame.

J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile. Maintenant, vous pouvez travailler avec des data frames et des fichiers CSV dans R.

**Si vous avez aimé cet article, envisagez de** [**vous inscrire à mon nouveau cours en ligne** **"Introduction à la statistique dans R - Une approche pratique**](https://www.udemy.com/course/descriptive-statistics-using-r-a-practical-introduction/?referralCode=F5AC93170862ED00BF67)**"**