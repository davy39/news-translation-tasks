---
title: Analyse de données en Go – Comment utiliser le package Gota
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-25T20:52:01.000Z'
originalURL: https://freecodecamp.org/news/exploratory-data-analysis-in-go-with-gota
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Exodus-Of-Decentralized-Internet.png
tags:
- name: data analysis
  slug: data-analysis
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Analyse de données en Go – Comment utiliser le package Gota
seo_desc: 'By Ukeje Chukwuemeriwo Goodness

  Data analysis is the process of filtering, manipulating, and processing raw data
  and datasets to get insights from them.

  Python and R are usually the go-to languages for data analysis. But these days Go
  is becoming mor...'
---

Par Ukeje Chukwuemeriwo Goodness

L'analyse de données est le processus de filtrage, de manipulation et de traitement de données brutes et de jeux de données pour en tirer des informations.

Python et R sont généralement les langages de prédilection pour l'analyse de données. Mais de nos jours, Go devient de plus en plus populaire à cette fin.

Dans ce tutoriel, nous allons passer en revue Gota, un package d'analyse de données en Go, ainsi que ses fonctions et utilisations principales.

## Qu'est-ce que Gota ?

Gota est un module Series, DataFrame et de manipulation de données pour le langage de programmation Go.

Gota est similaire à la bibliothèque Pandas en Python et est conçu pour s'interfacer avec [Gonum](https://www.gonum.org/), un package de calcul scientifique en Go, tout comme Pandas et Numpy.

Le module Gota rend les opérations de manipulation de données (transformation et manipulation) en Go très faciles. Il fonctionne avec les types de données intégrés de Go et divers formats de fichiers comme JSON, CSV et HTML.

Voici quelques prérequis :

* Quelques connaissances du terminal pour votre système
* Quelques connaissances de Go et de la programmation fonctionnelle
* Une version récente de Go (j'utilise Go 1.17.6, mais vous pouvez utiliser une version différente)
* Un éditeur de texte comme VS Code ou un IDE spécialisé comme Goland

Et voici ce que nous allons couvrir :

* Gota Series
* Gota Dataframes
* Lire des fichiers en tant que DataFrames
* Opérations sur les DataFrames Gota
* Exportation et sauvegarde de fichiers

## Comment commencer avec Gota

Tout d'abord, créez un nouveau répertoire et naviguez jusqu'à lui dans votre terminal.

Pour ce tutoriel, j'ai créé un nouveau répertoire appelé `gota-tutorial`.

Pour Linux ou Mac :

```
mkdir gota-tutorial
cd gota-tutorial
```

Dans votre nouveau répertoire, créez un fichier nommé `main.go`.

Ensuite, dans le fichier `main.go`, ajoutez le code suivant :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	// Le code futur ira ici
}

```

Notez que tout le code futur de ce tutoriel ira à l'intérieur du corps de la fonction `main`.

Ensuite, exécutez la commande suivante dans votre terminal pour initialiser un module et activer le suivi des dépendances. C'est un exemple simple, donc le nom/chemin du module sera simplement appelé `example/gota-tutorial` :

```
go mod init example/gota-tutorial
```

Vous devriez voir la sortie suivante :

```
go: création d'un nouveau go.mod : module example/gota-tutorial
go: pour ajouter les exigences du module et les sommes :
        go mod tidy
```

Et vous devriez voir un nouveau fichier `go.mod` dans le répertoire de votre projet.

Enfin, exécutez `go mod tidy` pour ajouter les exigences du module et les sommes, ou, en d'autres termes, installer tout ce dont vous avez besoin pour exécuter Gota :

```
go mod tidy
```

Après avoir exécuté cette commande, vous devriez voir un nouveau fichier `go.sum`. Ainsi, votre répertoire devrait maintenant contenir un fichier `main.go`, ainsi que les fichiers `go.mod` et `go.sum` générés automatiquement.

Vous pouvez en savoir plus sur le suivi des dépendances dans ce [guide officiel de démarrage](https://go.dev/doc/tutorial/getting-started#install).

## Concepts de base de Gota

![Image](https://www.freecodecamp.org/news/content/images/2022/04/dataframe.png)

Apprenons quelques bases de Gota avant de plonger.

Un **Dataset** est une collection de données, tabulaires ou non.

Les **Dataframes** sont des structures de données qui organisent les données en tableaux à deux dimensions (lignes et colonnes), généralement à des fins d'analyse.

Une **Series** est une collection de données unidimensionnelles appartenant à un DataFrame.

Notez que `df`, et ses variations comme `dogsDf`, sont les noms de variables de l'objet DataFrame utilisés comme exemple tout au long de cet article.

## Qu'est-ce que les Series Gota ?

Les Series Gota sont créées en utilisant la méthode `series.New()` sur des types de données composés, comme les slices et les maps.

Pour les slices, `series.New()` prend trois arguments : elle prend la slice, le type de Series (type d'éléments à contenir dans la Series), et un nom de colonne.

```go
series.New([]string{"z", "y", "d", "e"}, series.String, "col")

```

Les Series peuvent également être créées à partir de maps en initialisant les clés pour qu'elles soient de type `series` et en utilisant la méthode `.Type` pour insérer des types de Series.

```go
a := map[string]series.Type{
	"A": series.String,
	"D": series.Bool,
}

```

Ces slices peuvent être passées dans des DataFrames pour une manipulation et des opérations supplémentaires.

Notez que, si vous souhaitez voir la sortie pour le code ci-dessus, vous devrez commenter `"github.com/go-gota/gota/dataframe"`, et utiliser `fmt.Println()`, similaire à ceci :

```go
package main

import (
	"fmt"
	// "github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	fmt.Println(series.New([]string{"z", "y", "d", "e"}, series.String, "col"))
	
	a := map[string]series.Type{
		"A": series.String,
		"D": series.Bool,
	}

	fmt.Println(a)
}
```

Ensuite, vous pouvez voir les deux Series dans la console après avoir exécuté votre code en entrant la commande `go run .` dans le terminal.

**Sortie :**

```
[z y d e]
map[A:string D:bool]
```

## Qu'est-ce que les DataFrames Gota ?

Les fonctions DataFrame sont contenues dans le sous-module `dataframe` de Gota.

Les DataFrames sont des structures de données d'autres structures de données. Essentiellement, ils formatent les données en tableaux à deux dimensions afin que vous puissiez manipuler ces données. Donc, pour utiliser les DataFrames, nous lisons d'autres structures de données et types de données.

Nous allons lire des Series, des structs, des JSON et des fichiers CSV dans ce tutoriel.

## Comment convertir une Series en un objet DataFrame

Vous pouvez convertir une Series ou un ensemble de Series en un objet DataFrame en utilisant la méthode `dataframe.New()`. Elle prend en argument la Series ou l'ensemble de Series :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	df := dataframe.New(
		series.New([]string{"a", "b", "c", "d", "e"}, series.String, "alphas"),
		series.New([]int{5, 4, 2, 3, 1}, series.Int, "numbers"),
		series.New([]string{"a1", "b2", "c3", "d4", "e5"}, series.String, "alnums"),
		series.New([]bool{true, false, true, true, false}, series.Bool, "state"),
	)

	fmt.Println(df)
}

```

Notez que `"github.com/go-gota/gota/dataframe"` a été décommenté dans le code ci-dessus.

**Sortie :**

```
[5x4] DataFrame

    alphas   numbers alnums   state
 0: a        5       a1       true
 1: b        4       b2       false
 2: c        2       c3       true
 3: d        3       d4       true
 4: e        1       e5       false
    <string> <int>   <string> <bool>
```

## DataFrame de types Structs

Vous pouvez utiliser des structs pour créer des DataFrames :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	// "github.com/go-gota/gota/series"
)

func main() {
	type Dog struct {
		Name       string
		Color      string
		Height     int
		Vaccinated bool
	}

	dogs := []Dog{
		{"Buster", "Black", 56, false},
		{"Jake", "White", 61, false},
		{"Bingo", "Brown", 50, true},
		{"Gray", "Cream", 68, false},
	}

	dogsDf := dataframe.LoadStructs(dogs)
	
    fmt.Println(dogsDf)
}

```

Vous faites cela en créant une slice d'instances du type struct et en créant des DataFrames en utilisant la méthode `dataframe.LoadStructs` qui prend en argument la slice.

Notez également que `"github.com/go-gota/gota/series"` a été commenté.

**Sortie :**

```go
[4x4] DataFrame

    Name     Color    Height Vaccinated
 0: Buster   Black    56     false
 1: Jake     White    61     false
 2: Bingo    Brown    50     true
 3: Gray     Cream    68     false
    <string> <string> <int>  <bool>
```

## Comment interroger les DataFrames dans Gota

Lorsque nous avons un objet DataFrame, nous pouvons l'interroger pour obtenir des informations sur la composition du DataFrame en utilisant diverses méthodes.

* `df.Dims()` → Affiche les dimensions de l'objet DataFrame
* `df.Types()` → Affiche les types de données qui constituent le DataFrame
* `df.Names()` → Affiche les noms des colonnes du DataFrame
* `df.Nrow()` → Affiche le nombre de lignes
* `df.Ncol()` → Affiche le nombre de colonnes

Voici à quoi cela ressemble en utilisant l'exemple `dogsDf` précédent :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
)

func main() {
	type Dog struct {
		Name       string
		Color      string
		Height     int
		Vaccinated bool
	}

	dogs := []Dog{
		{"Buster", "Black", 56, false},
		{"Jake", "White", 61, false},
		{"Bingo", "Brown", 50, true},
		{"Gray", "Cream", 68, false},
	}

	dogsDf := dataframe.LoadStructs(dogs)
	
	fmt.Println(dogsDf.Dims())
	fmt.Println(dogsDf.Types())
	fmt.Println(dogsDf.Names())
	fmt.Println(dogsDf.Nrow())
	fmt.Println(dogsDf.Ncol())
}

```

**Sortie :**

```
4 4
[string string int bool]
[Name Color Height Vaccinated]
4
4
```

## Comment interroger les colonnes

Il existe de nombreuses méthodes qui accompagnent une colonne de DataFrame Gota et qui aident à interroger les valeurs des colonnes.

Une fois que vous avez sélectionné une colonne avec `df.Col("column_name")`, vous pouvez utiliser certaines des méthodes suivantes :

* `col.IsNaN()` → Vérifie si c'est une colonne nulle
* `col.Mean()` → Retourne la valeur moyenne (moyenne) de la colonne
* `col.Copy()` → Crée une nouvelle copie de la colonne
* `col.HasNaN()` → Vérifie s'il y a une valeur nulle dans la colonne
* `col.Records()` → retourne les valeurs dans la colonne

Voici à quoi cela ressemble en utilisant l'exemple `dogsDf` précédent :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
)

func main() {
	type Dog struct {
		Name       string
		Color      string
		Height     int
		Vaccinated bool
	}

	dogs := []Dog{
		{"Buster", "Black", 56, false},
		{"Jake", "White", 61, false},
		{"Bingo", "Brown", 50, true},
		{"Gray", "Cream", 68, false},
	}

	dogsDf := dataframe.LoadStructs(dogs)

	col := dogsDf.Col("Height") // Sélectionne une colonne
	fmt.Println(col.IsNaN())
	fmt.Println(col.Mean())
	fmt.Println(col.Copy())
	fmt.Println(col.HasNaN())
	fmt.Println(col.Records())
}

```

**Sortie :**

```
[false false false false]
58.75
[56 61 50 68]
false
[56 61 50 68]
```

## Comment convertir des chaînes JSON et CSV en objets DataFrame

Les chaînes JSON et CSV peuvent être passées à `dataframe.ReadJSON()` et `dataframe.ReadCSV()` respectivement.

### Comment convertir des chaînes JSON en DataFrames

La variable de chaîne JSON est passée en argument à `dataframe.ReadJSON()` en utilisant `strings.NewReader()` qui retourne une chaîne JSON tamponnée.

Importez le package `"strings"` ainsi que `"github.com/go-gota/gota/dataframe"`, et optionnellement, `"fmt"`.

Ensuite, dans votre fonction `main`, incluez une chaîne JSON, lisez-la avec `strings.NewReader()`, et passez cela à `dataframe.ReadJSON()` :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"strings"
)

func main() {
	jsonString := `[
  {
    "Name": "John",
    "Age": 44,
    "Favorite Color": "Red",
    "Height(ft)": 6.7
  },
  {
    "Name": "Mary",
    "Age": 40,
    "Favorite Color": "Blue",
    "Height(ft)": 5.7
  }
]`

	jsonDf := dataframe.ReadJSON(strings.NewReader(jsonString))
	fmt.Println(jsonDf)
}

```

**Sortie :**

```
[2x4] DataFrame

    Age   Favorite Color Height(ft) Name
 0: 44    Red            6.700000   John
 1: 40    Blue           5.700000   Mary
    <int> <string>       <float>    <string>
```

### Comment convertir des chaînes CSV en DataFrames

Voici un exemple similaire, mais avec une chaîne CSV.

Cette fois, lisez la chaîne CSV avec `strings.NewReader()`, et passez cela à `dataframe.ReadCSV()` :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"strings"
)

func main() {
	csvString := `
Name,Age,Favorite Color,Height(ft)
John,44,Red,6.7
Mary,40,Blue,5.7`

	csvDf := dataframe.ReadCSV(strings.NewReader(csvString))
	fmt.Println(csvDf)
}

```

**Sortie :**

```
[2x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: John     44    Red            6.700000
 1: Mary     40    Blue           5.700000
    <string> <int> <string>       <float>
```

### Comment convertir des fichiers CSV en DataFrames

Supposons que vous avez un CSV dans un fichier séparé nommé `stats.csv` avec le contenu suivant :

```markdown
Name,Age,Favorite Color,Height(ft)
John,44,Red,6.7
Mary,40,Blue,5.7
Esther,35,Black,4.9
Jason,36,Green,5.2

```

Vous pouvez lire votre fichier CSV avec `os.Open()`, qui prend le nom du fichier comme argument.

Le motif `defer` et `.Close()` aide à fermer le fichier une fois que le programme a fini de s'exécuter pour prévenir la perte de données.

Tout d'abord, importez `"log"` et `"os"` ainsi que `"github.com/go-gota/gota/dataframe"` et `"fmt"`.

Ensuite, lisez le fichier avec `os.Open()`, utilisez le motif `defer` et `.Close()`, et ajoutez un simple journal d'erreurs :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
)

func main() {
	file, err := os.Open("stats.csv")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	df := dataframe.ReadCSV(file)

	fmt.Println(df)
}

```

**Sortie :**

```
[4x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: John     44    Red            6.700000
 1: Mary     40    Blue           5.700000
 2: Esther   35    Black          4.900000
 3: Jason    36    Green          5.200000
    <string> <int> <string>       <float>
```

### Comment convertir des fichiers JSON en DataFrames

Lire un fichier JSON séparé et le convertir en DataFrame est très similaire.

Supposons que vous avez un fichier `stats.json` cette fois :

```json
[
  {
    "Name": "John",
    "Age": 44,
    "Favorite Color": "Red",
    "Height(ft)": 6.7
  },
  {
    "Name": "Mary",
    "Age": 40,
    "Favorite Color": "Blue",
    "Height(ft)": 5.7
  },
  {
    "Name": "Esther",
    "Age": 35,
    "Favorite Color": "Black",
    "Height(ft)": 4.9
  },
  {
    "Name": "Mary",
    "Age": 40,
    "Favorite Color": "Green",
    "Height(ft)": 5.2
  }
]

```

Mais cette fois, vous devez utiliser `dataframe.ReadJSON()` à la place :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
)

func main() {
	file, err := os.Open("stats.json")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	df := dataframe.ReadJSON(file)

	fmt.Println(df)
}

```

**Sortie :**

```
[4x4] DataFrame

    Age   Favorite Color Height(ft) Name
 0: 44    Red            6.700000   John
 1: 40    Blue           5.700000   Mary
 2: 35    Black          4.900000   Esther
 3: 40    Green          5.200000   Mary
    <int> <string>       <float>    <string>
```

## Opérations sur les DataFrames Gota

Maintenant que vous connaissez les bases de l'utilisation des DataFrames et des Series, et comment les remplir avec des données, nous allons examiner d'autres façons de manipuler ces données avec les DataFrames.

### Comment sélectionner des lignes dans Gota

Vous pouvez sélectionner des lignes en utilisant la méthode `.Subset()` de l'objet DataFrame.

`df.Subset()` prend en argument une slice de deux entiers qui dépeignent le nombre de lignes qui doivent être sélectionnées :

```go
// Cela sélectionne les deux premières lignes du DataFrame
rows := df.Subset([]int{0, 2})

```

Voici le code complet basé sur l'exemple de fichier CSV ci-dessus :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
)

func main() {
	file, err := os.Open("stats.csv")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	df := dataframe.ReadCSV(file)

	// Cela sélectionne les deux premières lignes du DataFrame
	rows := df.Subset([]int{0, 2})

	fmt.Println(rows)
}

```

**Sortie :**

```
[2x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: John     44    Red            6.700000
 1: Esther   35    Black          4.900000
    <string> <int> <string>       <float>
```

### Comment sélectionner des colonnes dans Gota

Utilisez la méthode `.Select()` pour sélectionner les colonnes d'un DataFrame.

`df.Select()` prend en argument une slice de deux entiers qui dépeignent combien de colonnes doivent être sélectionnées :

```go
// Cela sélectionne les deux premières colonnes d'un DataFrame
columns := df.Select([]int{0, 2})

```

Vous pouvez également sélectionner des colonnes par index (noms de colonnes) en passant une slice de chaînes :

```go
// Cela sélectionne les colonnes d'un DataFrame par nom
columns := df.Select([]string{"Name", "Favorite Color"})

```

Voici le code complet utilisant l'exemple de fichier CSV précédent montrant les deux méthodes de sélection de colonnes :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
)

func main() {
	file, err := os.Open("stats.csv")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	df := dataframe.ReadCSV(file)

	// Cela sélectionne les deux premières colonnes d'un DataFrame
	firstTwoColumns := df.Select([]int{0, 2})

	// Cela sélectionne les colonnes d'un DataFrame par nom
	namedColumns := df.Select([]string{"Name", "Favorite Color"})

	fmt.Println(firstTwoColumns)
	fmt.Println(namedColumns)
}

```

**Sortie :**

```
[4x2] DataFrame

    Name     Favorite Color
 0: John     Red
 1: Mary     Blue
 2: Esther   Black
 3: Jason    Green
    <string> <string>

[4x2] DataFrame

    Name     Favorite Color
 0: John     Red
 1: Mary     Blue
 2: Esther   Black
 3: Jason    Green
    <string> <string>
```

### Comment mettre à jour les DataFrames dans Gota

Utilisez la méthode `.Set()` de l'objet DataFrame pour mettre à jour les entrées.

`df.Set()` prend en argument une slice d'entiers spécifiant la limite des lignes à mettre à jour, et une fonction `dataframe.LoadRecords()`, qui prend en argument une slice à deux dimensions du type à passer :

```go
updatedDf := df.Set(
	[]int{0, 3},
	dataframe.LoadRecords(
		[][]string{
			[]string{"Jenny", "23", "Purple", "2.2"},
			[]string{"Jesse", "34", "Indigo", "3.5"},
			[]string{"Peter", "33", "Violet", "3.3"},
		},
	),
)
```

Notez que la méthode `df.Set()` modifie le DataFrame.

Encore une fois, en s'appuyant sur l'exemple de fichier CSV précédent, voici comment vous pouvez mettre à jour les entrées dans un DataFrame :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
)

func main() {
	file, err := os.Open("stats.csv")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	df := dataframe.ReadCSV(file)

	updatedDf := df.Set(
		[]int{0, 3},
		dataframe.LoadRecords(
			[][]string{
				[]string{"Jenny", "23", "Purple", "2.2"},
				[]string{"Jesse", "34", "Indigo", "3.5"},
				[]string{"Peter", "33", "Violet", "3.3"},
			},
		),
	)

	fmt.Println(updatedDf)
}

```

**Sortie :**

```
[4x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: Jesse    34    Indigo         3.500000
 1: Mary     40    Blue           5.700000
 2: Esther   35    Black          4.900000
 3: Peter    33    Violet         3.300000
    <string> <int> <string>       <float>
```

### Comment filtrer les valeurs dans Gota

Utilisez la méthode `.Filter()` sur l'objet DataFrame pour filtrer les valeurs.

Cela prend en argument `dataframe.F`, auquel vous passez un littéral de struct.

Le littéral de struct prend en argument un nom de colonne, `Colname`, un comparateur, `Comparator`, et une valeur, `Comparando`, qui est la valeur que vous souhaitez filtrer dans le DataFrame.

**Comparateurs :**

* `series.Eq` → Égal à =
* `series.Neq` → Non égal à ≠
* `series.Greater` → Supérieur à >
* `series.GreaterEq` → Supérieur ou égal à ≥
* `series.Less` → Inférieur à <
* `series.LessEq` → Inférieur ou égal à ≤
* `series.In` → Est contenu dans

Dans cet exemple, nous utilisons l'objet dataframe de la section Series vers le dataframe ci-dessus.

En utilisant un exemple de code différent de celui du début du tutoriel, voici un exemple simple de la méthode `.Filter()` :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	df := dataframe.New(
		series.New([]string{"a", "b", "c", "d", "e"}, series.String, "alphas"),
		series.New([]int{5, 4, 2, 3, 1}, series.Int, "numbers"),
		series.New([]string{"a1", "b2", "c3", "d4", "e5"}, series.String, "alnums"),
		series.New([]bool{true, false, true, true, false}, series.Bool, "state"),
	)

	// Filtrer b de la colonne nommée alphas
	fil := df.Filter(
		dataframe.F{Colname: "alphas", Comparator: series.Eq, Comparando: "b"},
	)

	fmt.Println(fil)
}

```

**Sortie :**

```markdown
[1x4] DataFrame

    alphas   numbers alnums   state
 0: b        4       b2       false
    <string> <int>   <string> <bool>
```

### Comment trier un DataFrame dans Gota

Pour trier un DataFrame, utilisez la méthode `.Arrange()` de l'objet DataFrame.

La méthode `df.Arrange()` prend en argument `dataframe.Sort()` ou `dataframe.RevSort()`, qui trient respectivement par ordre croissant ou décroissant. Elle prend également le nom de la colonne à trier sous forme de chaîne.

**Comment trier par ordre croissant :**

Voici un extrait montrant comment utiliser la méthode `df.Arrange()` pour trier par ordre croissant :

```go
sorted := df.Arrange(
	dataframe.Sort("numbers"),
)
```

**Comment trier par ordre décroissant :**

Cet extrait montre comment trier par ordre décroissant :

```go
sorted := df.Arrange(
	dataframe.RevSort("numbers"),
)
```

Et voici le code complet utilisant un exemple du début du tutoriel montrant comment trier par ordre croissant et décroissant :

```go
// Suite de Comment trier un DataFrame dans Gota

package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	df := dataframe.New(
		series.New([]string{"a", "b", "c", "d", "e"}, series.String, "alphas"),
		series.New([]int{5, 4, 2, 3, 1}, series.Int, "numbers"),
		series.New([]string{"a1", "b2", "c3", "d4", "e5"}, series.String, "alnums"),
		series.New([]bool{true, false, true, true, false}, series.Bool, "state"),
	)

	sortedAscending := df.Arrange(
		dataframe.Sort("numbers"),
	)

	fmt.Println(sorted)
}

```

**Sortie :**

```
[5x4] DataFrame

    alphas   numbers alnums   state
 0: e        1       e5       false
 1: c        2       c3       true
 2: d        3       d4       true
 3: b        4       b2       false
 4: a        5       a1       true
    <string> <int>   <string> <bool>

[5x4] DataFrame

    alphas   numbers alnums   state
 0: a        5       a1       true
 1: b        4       b2       false
 2: d        3       d4       true
 3: c        2       c3       true
 4: e        1       e5       false
    <string> <int>   <string> <bool>
```

### Comment catégoriser les données dans Gota

Vous pouvez utiliser la méthode `.GroupBy()` de l'objet DataFrame pour catégoriser les données en fonction de colonnes spécifiques.

Pour utiliser la méthode `df.GroupBy()`, passez simplement les noms des colonnes que vous souhaitez regrouper :

```go
categorize := df.GroupBy("Name", "Age")
```

Encore une fois, en s'appuyant sur l'exemple de fichier CSV précédent, voici comment vous pouvez mettre à jour les entrées dans un DataFrame :

Encore une fois, en utilisant l'exemple de fichier CSV précédent, voici comment vous pouvez utiliser `df.GroupBy()` pour catégoriser ou regrouper les données par colonnes :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
)

func main() {
	file, err := os.Open("stats.csv")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	df := dataframe.ReadCSV(file)

	categorize := df.GroupBy("Name", "Age")

	fmt.Println(categorize)
}

```

### Comment joindre des DataFrames dans Gota

Les jointures sont une combinaison de DataFrames. Joindre des DataFrames avec Gota fonctionne exactement comme en SQL (Structured Query Language).

**Types de jointures :**

* Jointure interne → `df.InnerJoin()` retourne un DataFrame des valeurs correspondantes dans les deux tables
* Jointure gauche → `df.LeftJoin()` fait correspondre les similitudes dans le DataFrame de droite au DataFrame de gauche
* Jointure droite → `df.RightJoin()` fait correspondre les similitudes dans le DataFrame de gauche au DataFrame de droite
* Jointure externe → `df.OuterJoin()` retourne toutes les valeurs du DataFrame

Voici la syntaxe de base pour joindre des objets DataFrames :

```go
joinVariableName := df.joinType(otherDataframe, joinKey)

```

La clé de jointure est la colonne de l'objet DataFrame où la jointure doit être exécutée.

Notez que `joinKey` est une chaîne de la colonne de l'objet DataFrame où la jointure doit être exécutée.

Voici un exemple de code montrant comment faire une jointure gauche :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	dfA := dataframe.New(
		series.New([]string{"a", "b", "c", "d", "e"}, series.String, "alphas"),
		series.New([]int{5, 4, 2, 3, 1}, series.Int, "numbers"),
		series.New([]string{"a1", "b2", "c3", "d4", "e5"}, series.String, "alnums"),
		series.New([]bool{true, false, true, true, false}, series.Bool, "state"),
	)
	dfB := dataframe.New(
		series.New([]string{"f", "g", "h", "i", "j"}, series.String, "alphas"),
		series.New([]int{1, 2, 3, 4, 5}, series.Int, "numbers"),
		series.New([]string{"f6", "g7", "h8", "i9", "j10"}, series.String, "alnums"),
		series.New([]bool{false, true, false, false, true}, series.Bool, "state"),
	)

	leftJoin := dfA.RightJoin(dfB, "state")

	fmt.Println(leftJoin)
}

```

**Sortie :**

```
[12x7] DataFrame

    state  alphas_0 numbers_0 alnums_0 alphas_1 numbers_1 alnums_1
 0: false  b        4         b2       f        1         f6
 1: false  e        1         e5       f        1         f6
 2: true   a        5         a1       g        2         g7
 3: true   c        2         c3       g        2         g7
 4: true   d        3         d4       g        2         g7
 5: false  b        4         b2       h        3         h8
 6: false  e        1         e5       h        3         h8
 7: false  b        4         b2       i        4         i9
 8: false  e        1         e5       i        4         i9
 9: true   a        5         a1       j        5         j10
    ...    ...      ...       ...      ...      ...       ...
    <bool> <string> <int>     <string> <string> <int>     <string>
```

### Comment appliquer des fonctions à un DataFrame dans Gota

Pour appliquer des fonctions aux colonnes et aux lignes d'un DataFrame, utilisez les méthodes `.Capply()` et `.Rapply()` sur l'objet DataFrame, respectivement.

Celles-ci prennent en argument la fonction à appliquer sur la colonne ou la ligne :

```go
df.Capply(function)
df.Rapply(function)

```

Voici un exemple complet qui montre un DataFrame simple créé à partir d'une seule Series. Dans cet exemple, les méthodes `.Capply()` et `.Rapply()` sont utilisées pour appliquer une fonction afin de calculer la moyenne d'une colonne :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	df := dataframe.New(
		series.New([]int{95, 74, 59, 82, 87}, series.Int, "score"),
	)

	mean := func(s series.Series) series.Series {
		floats := s.Float()
		sum := 0.0
		for _, f := range floats {
			sum += f
		}
		return series.Floats(sum / float64(len(floats)))
	}

	meanScore := df.Capply(mean)

	fmt.Println(meanScore)
}

```

### Comment utiliser Describe sur un DataFrame dans Gota

Utilisez `.Describe()` sur un objet DataFrame pour retourner des statistiques descriptives sur les valeurs du DataFrame :

```go
description := df.Describe()

```

Et voici un exemple complet :

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	df := dataframe.New(
		series.New([]string{"a", "b", "c", "d", "e"}, series.String, "alphas"),
		series.New([]int{5, 4, 2, 3, 1}, series.Int, "numbers"),
		series.New([]string{"a1", "b2", "c3", "d4", "e5"}, series.String, "alnums"),
		series.New([]bool{true, false, true, true, false}, series.Bool, "state"),
	)

	description := df.Describe()

	fmt.Println(description)
}

```

**Sortie :**

```markdown
[8x5] DataFrame

    column   alphas   numbers  alnums   state
 0: mean     -        3.000000 -        0.600000
 1: median   -        3.000000 -        NaN
 2: stddev   -        1.581139 -        0.547723
 3: min      a        1.000000 a1       0.000000
 4: 25%      -        2.000000 -        0.000000
 5: 50%      -        3.000000 -        1.000000
 6: 75%      -        4.000000 -        1.000000
 7: max      e        5.000000 e5       1.000000
    <string> <string> <float>  <string> <float>
```

## Comment exporter des DataFrames (Écrire des fichiers en Go)

Une fois que vous avez terminé de manipuler vos données, vous pouvez utiliser les méthodes `.WriteCSV()` et `.WriteJSON()` pour exporter vos données sous forme de fichier CSV ou JSON.

### Comment exporter des DataFrames en tant que fichier CSV

Pour exporter vos données en tant que fichier CSV, utilisez simplement la méthode `.WriteCSV()` sur l'objet DataFrame que vous souhaitez exporter en tant que fichier CSV.

Tout d'abord, utilisez le package `os` pour créer un fichier, puis passez ce fichier à la méthode `df.WriteCSV()` pour exporter votre DataFrame en tant que CSV :

```go
file, err := os.Create("output.csv")
if err != nil {
	log.Fatal(err)
}

df.WriteCSV(file)

```

Voici un exemple complet qui montre la construction d'un DataFrame à partir d'une chaîne CSV, la mise à jour du DataFrame, et l'exportation du DataFrame mis à jour en tant que fichier CSV :

```go
package main

import (
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
	"strings"
)

func main() {
	csvString := `
Name,Age,Favorite Color,Height(ft)
John,44,Red,6.7
Mary,40,Blue,5.7
Paul,27,green,5.6`

	df := dataframe.ReadCSV(strings.NewReader(csvString))

	updatedDf := df.Set(
		[]int{0, 2},
		dataframe.LoadRecords(
			[][]string{
				[]string{"Jenny", "23", "Purple", "2.2"},
				[]string{"Jesse", "34", "Indigo", "3.5"},
				[]string{"Peter", "33", "Violet", "3.3"},
			},
		),
	)

	file, err := os.Create("output.csv")
	if err != nil {
		log.Fatal(err)
	}

	updatedDf.WriteCSV(file)
}

```

Et le CSV suivant devrait être écrit dans `output.csv` :

```
Name,Age,Favorite Color,Height(ft)
Jesse,34,Indigo,3.500000
Mary,40,Blue,5.700000
Peter,33,Violet,3.300000

```

### Comment exporter des DataFrames en tant que fichier JSON

Exporter vos données en tant que fichier JSON est très similaire, et utilise simplement la méthode `.WriteJSON()` sur l'objet DataFrame que vous souhaitez exporter.

Voici un exemple complet :

```go
package main

import (
	"github.com/go-gota/gota/dataframe"
	"log"
	"os"
	"strings"
)

func main() {
	csvString := `
Name,Age,Favorite Color,Height(ft)
John,44,Red,6.7
Mary,40,Blue,5.7
Paul,27,green,5.6`

	df := dataframe.ReadCSV(strings.NewReader(csvString))

	updatedDf := df.Set(
		[]int{0, 2},
		dataframe.LoadRecords(
			[][]string{
				[]string{"Jenny", "23", "Purple", "2.2"},
				[]string{"Jesse", "34", "Indigo", "3.5"},
				[]string{"Peter", "33", "Violet", "3.3"},
			},
		),
	)

	file, err := os.Create("output.json")
	if err != nil {
		log.Fatal(err)
	}

	updatedDf.WriteJSON(file)
}

```

Et vous devriez maintenant avoir un fichier nommé `output.json` avec le tableau JSON suivant :

```json
[{"Age":34,"Favorite Color":"Indigo","Height(ft)":3.5,"Name":"Jesse"},{"Age":40,"Favorite Color":"Blue","Height(ft)":5.7,"Name":"Mary"},{"Age":33,"Favorite Color":"Violet","Height(ft)":3.3,"Name":"Peter"}]

```

## Conclusion

Dans ce tutoriel, vous avez appris comment effectuer l'analyse de données en Go. Vous avez également appris les différentes fonctions du package Gota.

Il est toujours judicieux d'utiliser principalement Python et R pour l'analyse de données, car ils sont considérés comme la norme de l'industrie. Mais Gota est utile pour les applications nécessitant rapidité et homogénéité.

Consultez la [documentation Gota](https://pkg.go.dev/github.com/go-gota/gota/dataframe) pour en savoir plus ou contribuer au projet.

Amusez-vous à coder et à explorer !