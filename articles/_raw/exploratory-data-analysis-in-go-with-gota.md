---
title: Data Analysis in Go – How to Use the Gota Package
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
seo_title: null
seo_desc: 'By Ukeje Chukwuemeriwo Goodness

  Data analysis is the process of filtering, manipulating, and processing raw data
  and datasets to get insights from them.

  Python and R are usually the go-to languages for data analysis. But these days Go
  is becoming mor...'
---

By Ukeje Chukwuemeriwo Goodness

Data analysis is the process of filtering, manipulating, and processing raw data and datasets to get insights from them.

Python and R are usually the go-to languages for data analysis. But these days Go is becoming more and more popular for this purpose.

In this tutorial, we will be going over Gota, a data analysis package in Go, and its core functions and uses.

## What is Gota?

Gota is a Series, DataFrame and data wrangling module for the Go programming language.

Gota is similar to the Pandas library in Python and is built to interface with [Gonum](https://www.gonum.org/), a scientific computing package in Go, just like Pandas and Numpy.

The Gota module makes data wrangling (transforming and manipulating) operations in Go very easy. It works with Go inbuilt data types and various file formats like JSON, CSV, and HTML.

Here are some prerequisites:

* Some knowledge of the terminal for your system
* Some knowledge of Go and functional programming
* A recent version of Go (I use Go 1.17.6, but you can use a different version)
* A text editor like VS Code or a specialized IDE like Goland

And here's what we'll cover:

* Gota Series
* Gota Dataframes
* Reading files as DataFrames
* Operations on Gota DataFrames
* Exporting and saving files

## How to Get Started with Gota

First, create a new directory and navigate to it in your terminal.

For this tutorial, I created a new directory called `gota-tutorial`.

For Linux or Mac:

```
mkdir gota-tutorial
cd gota-tutorial
```

In your new directory, create a file named `main.go`.

Then in the `main.go` file, add the following code:

```go
package main

import (
	"fmt"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
)

func main() {
	// Future code will go here
}

```

Note that all of the future code in this tutorial will go inside the body of the `main` function.

Next, run the following command in your terminal to initialize a module and enable dependency tracking. This is a simple example, so the module name / path will just be called `example/gota-tutorial`:

```
go mod init example/gota-tutorial
```

You should see the following output:

```
go: creating new go.mod: module example/gota-tutorial
go: to add module requirements and sums:
        go mod tidy
```

And you should see a new `go.mod` file in your project's directory.

Finally, run `go mod tidy` to add the module requirements and sums, or, in other words, install everything you need to run Gota:

```
go mod tidy
```

After running that command, you should see a new `go.sum` file. So your directory should now have a `main.go` file, along with the automatically generated `go.mod` and `go.sum` files.

You can read more about dependency tracking in this [official getting started guide](https://go.dev/doc/tutorial/getting-started#install).

## Basic Gota Concepts

![Image](https://www.freecodecamp.org/news/content/images/2022/04/dataframe.png)

Let's learn some Gota basics before diving in.

A **Dataset** is a collection of data, tabular or otherwise.

**Dataframes** are data structures that organize data into two-dimensional (rows and columns) tables, usually for the purpose of analysis.

A **Series** is a collection of one-dimensional data belonging to a DataFrame.

Note that `df`, and variations like `dogsDf`, are the variable names of the DataFrame object used as an example throughout this article.

## What are Gota Series?

Gota Series are created using the `series.New()` method on compound data types, like slices and maps.

For slices, `series.New()` takes in three arguments: it takes in the slice, the Series type (type of elements to be contained in the Series), and a column name.

```go
series.New([]string{"z", "y", "d", "e"}, series.String, "col")

```

Series can also be made from maps by initializing the keys to be of type `series` and using the `.Type` method to insert Series types.

```go
a := map[string]series.Type{
	"A": series.String,
	"D": series.Bool,
}

```

These slices can be passed into DataFrames for further manipulation and operations.

Note that, if you'd like to see the output for the code above, that you'll need to comment out `"github.com/go-gota/gota/dataframe"`, and use `fmt.Println()`, similar to this:

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

Then you can see both Series in the console after running your code by entering the `go run .` command in the terminal.

**Output:**

```
[z y d e]
map[A:string D:bool]
```

## What are Gota DataFrames?

DataFrame functions are contained in the Gota `dataframe` submodule.

DataFrames are data structures of other data structures. Essentially, they format the data into two-dimensional tables so you can manipulate those data. So to use DataFrames, we read other data structures and data types.

We will be reading Series, structs, JSON, and CSV files in this tutorial.

## How to Convert a Series into a DataFrame Object

You can convert a Series or a set of Series into a DataFrame object using the `dataframe.New()` method. It takes in the Series or set of Series as arguments:

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

Note that `"github.com/go-gota/gota/dataframe"` has been uncommented in the code above.

**Output**:

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

## DataFrame of Structs Types

You can use structs to create DataFrames:

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

You do this by creating a slice of instances of the struct type and creating DataFrames using the `dataframe.LoadStructs` method which takes in the slice.

Also, note that `"github.com/go-gota/gota/series"` was commented out.

**Output**:

```go
[4x4] DataFrame

    Name     Color    Height Vaccinated
 0: Buster   Black    56     false
 1: Jake     White    61     false
 2: Bingo    Brown    50     true
 3: Gray     Cream    68     false
    <string> <string> <int>  <bool>
```

## How to Query DataFrames in Gota

When we have a DataFrame object, we can query it for information about the composition of the DataFrame using various methods.

* `df.Dims()` → Outputs the dimensions of the DataFrame object
* `df.Types()` → Outputs the datatypes that constitute the DataFrame
* `df.Names()` → Outputs the column names of the DataFrame
* `df.Nrow()` → Outputs the number of rows
* `df.Ncol()` → Outputs the number of columns

Here's what those looks like using the `dogsDf` example from before:

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

**Output:**

```
4 4
[string string int bool]
[Name Color Height Vaccinated]
4
4
```

## How to Query Columns

There are many methods that come with a Gota DataFrame column that help with querying column values.

Once you select a column with `df.Col("column_name")`, you can use some of the following methods:

* `col.IsNaN()` → Checks if it's a null column
* `col.Mean()` → Returns the mean (average) value of the column
* `col.Copy()` → Creates a new copy of the column
* `col.HasNaN()` → Checks if there’s a null value in the column
* `col.Records()` → returns the values in the column

Here's what those looks like using the `dogsDf` example from before:

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

	col := dogsDf.Col("Height") // Selects a column
	fmt.Println(col.IsNaN())
	fmt.Println(col.Mean())
	fmt.Println(col.Copy())
	fmt.Println(col.HasNaN())
	fmt.Println(col.Records())
}

```

**Output:**

```
[false false false false]
58.75
[56 61 50 68]
false
[56 61 50 68]
```

## How to Convert JSON and CSV Strings into DataFrame Objects

JSON and CSV strings can be passed to `dataframe.ReadJSON()` and `dataframe.ReadCSV()` respectively.

### How to Convert JSON Strings into DataFrames

The JSON string variable is passed as an argument into `dataframe.ReadJSON()` using `strings.NewReader()` which returns a buffered JSON string.

Import the `"strings"` package along with `"github.com/go-gota/gota/dataframe"`, and optionally, `"fmt"`.

Then in your `main` function, include a JSON string, read it with `strings.NewReader()`, and pass that to `dataframe.ReadJSON()`:

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

**Output:**

```
[2x4] DataFrame

    Age   Favorite Color Height(ft) Name
 0: 44    Red            6.700000   John
 1: 40    Blue           5.700000   Mary
    <int> <string>       <float>    <string>
```

### How to Convert CSV Strings into DataFrames

Here is a similar example, but with a CSV string.

This time, read the CSV string with `strings.NewReader()`, and pass that to `dataframe.ReadCSV()`:

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

**Output**:

```
[2x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: John     44    Red            6.700000
 1: Mary     40    Blue           5.700000
    <string> <int> <string>       <float>
```

### How to Convert CSV Files into DataFrames

Say you have some CSV in a separate file named `stats.csv` with the following:

```markdown
Name,Age,Favorite Color,Height(ft)
John,44,Red,6.7
Mary,40,Blue,5.7
Esther,35,Black,4.9
Jason,36,Green,5.2

```

You can read your CSV file with `os.Open()`, which takes the file name as an argument.

The `defer` and `.Close()` pattern helps to close the file once the program finishes running to prevent data loss.

First, import `"log"` and `"os"` along with `"github.com/go-gota/gota/dataframe"` and `"fmt"`.

Then, read the file with `os.Open()`, use the `defer` and `.Close()` pattern, and add in some simple error logging:

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

**Output:**

```
[4x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: John     44    Red            6.700000
 1: Mary     40    Blue           5.700000
 2: Esther   35    Black          4.900000
 3: Jason    36    Green          5.200000
    <string> <int> <string>       <float>
```

### How to Convert JSON Files into DataFrames

Reading a separate JSON file and converting it into a DataFrame is very similar.

Say you have a `stats.json` file this time:

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

But this time, you need to use `dataframe.ReadJSON()` instead:

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

**Output:**

```
[4x4] DataFrame

    Age   Favorite Color Height(ft) Name
 0: 44    Red            6.700000   John
 1: 40    Blue           5.700000   Mary
 2: 35    Black          4.900000   Esther
 3: 40    Green          5.200000   Mary
    <int> <string>       <float>    <string>
```

## Gota Dataframe Operations

Now that you know the basics of working with DataFrames and Series, and how to populate both with data, we'll take a look at more ways to wrangle that data with DataFrames.

### How to Select Rows in Gota

You can select rows using the `.Subset()` method of the DataFrame object.

`df.Subset()` takes in a slice of two integers that depict the number of rows that should be selected:

```go
// This selects the first two rows of the DataFrame
rows := df.Subset([]int{0, 2})

```

Here's the full code building off the CSV file example above:

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

	// This selects the first two rows of the DataFrame
	rows := df.Subset([]int{0, 2})

	fmt.Println(rows)
}

```

**Output:**

```
[2x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: John     44    Red            6.700000
 1: Esther   35    Black          4.900000
    <string> <int> <string>       <float>
```

### How to Select Columns in Gota

Use the `.Select()` method to select columns of a DataFrame.

`df.Select()` takes in a slice of two integers that depict how many columns should be selected:

```go
// This selects the first two columns of a DataFrame
columns := df.Select([]int{0, 2})

```

You can also select columns by index (column names) by passing a slice of strings:

```go
// This selects columns of a DataFrame by name
columns := df.Select([]string{"Name", "Favorite Color"})

```

Here is the full code using the CSV file example from earlier showing both methods of selecting columns:

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

	// This selects the first two columns of a DataFrame
	firstTwoColumns := df.Select([]int{0, 2})

	// This selects columns of a DataFrame by name
	namedColumns := df.Select([]string{"Name", "Favorite Color"})

	fmt.Println(firstTwoColumns)
	fmt.Println(namedColumns)
}

```

**Output:**

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

### How to Update DataFrames in Gota

Use the `.Set()` method of the DataFrame object to update entries.

`df.Set()` takes in a slice of integers specifying the limit of rows to be updated, and a `dataframe.LoadRecords()` function, which takes in a two-dimensional slice of the type to be passed in:

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

Note that the `df.Set()` method modifies the 

Again, building off of the CSV file example from earlier, here's how you can update entries in a DataFrame:

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

**Output**:

```
[4x4] DataFrame

    Name     Age   Favorite Color Height(ft)
 0: Jesse    34    Indigo         3.500000
 1: Mary     40    Blue           5.700000
 2: Esther   35    Black          4.900000
 3: Peter    33    Violet         3.300000
    <string> <int> <string>       <float>
```

### How to Filter Values in Gota

Use the `.Filter()` method on the DataFrame object to filter out values.

This takes in `dataframe.F`, which you pass a struct literal to.

The struct literal takes in a column name, `Colname`, a comparator, `Comparator`, and a value, `Comparando`, which is the value you want to filter out of the DataFrame.

**Comparators:**

* `series.Eq` → Equal to =
* `series.Neq` → Not Equal to ≠
* `series.Greater` → Greater than >
* `series.GreaterEq` → Greater than or Equal to ≥
* `series.Less` → Less than <
* `series.LessEq` → Less than or Equal to ≤
* `series.In` → Is contained In

In this example, we use the dataframe object from the Series to the dataframe section above.

Using some different example code from earlier in the tutorial, here's a simple example of the `.Filter()` method:

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

	// Filter out b from the column named alphas
	fil := df.Filter(
		dataframe.F{Colname: "alphas", Comparator: series.Eq, Comparando: "b"},
	)

	fmt.Println(fil)
}

```

**Output:**

```markdown
[1x4] DataFrame

    alphas   numbers alnums   state
 0: b        4       b2       false
    <string> <int>   <string> <bool>
```

### How to Sort a Dataframe in Gota

To sort a DataFrame, use the `.Arrange()` method of the DataFrame object.

The `df.Arrange()` method takes in `dataframe.Sort()` or `dataframe.RevSort()`, which sorts in ascending or descending order respectively. It also takes in the name of the column to be sorted as a string.

**How to Sort in Ascending Order:**

Here's a snippet showing how to use the `df.Arrange()` method to sort in ascending order:

```go
sorted := df.Arrange(
	dataframe.Sort("numbers"),
)
```

**How to Sort in Descending Order:**

This snippet shows you how to sort in descending order:

```go
sorted := df.Arrange(
	dataframe.RevSort("numbers"),
)
```

And here's the full code using an example from earlier in the tutorial showing how to sort in both ascending and descending order:

```go
// Continue from How to Sort a Dataframe in Gota

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

**Output:**

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

### How to Categorize Data in Gota

You can use the `.GroupBy()` method of the DataFrame object to categorize data based on specific columns.

To use the `df.GroupBy()` method, just pass in the column names you want to group together:

```go
categorize := df.GroupBy("Name", "Age")
```

Again, building off of the CSV file example from earlier, here's how you can update entries in a DataFrame:

Again, using the CSV file example from earlier, here's how you can use `df.GroupBy()` to categorize or group data by columns:

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

### How to Join DataFrames in Gota

Joins are a combination of DataFrames. Joining DataFrames with Gota works just like in SQL (Structured Query Language).

**Types of Joins:**

* Inner join → `df.InnerJoin()` returns a DataFrame of matching values in both tables
* Left join → `df.LeftJoin()` matches similarities in the right DataFrame to the left DataFrame
* Right join → `df.RightJoin()` matches similarities in the left DataFrame to the right DataFrame
* Outer join → `df.OuterJoin()` returns all values of the DataFrame

Here's the basic syntax for joining DataFrames objects:

```go
joinVariableName := df.joinType(otherDataframe, joinKey)

```

The Join key is the column of the DataFrame object where the join is to be executed.

Note that `joinKey` is a string of the column of the DataFrame object where the join should be executed.

Here's some code showing how to do a left join:

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

**Output:**

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

### How to Apply Functions to a DataFrame in Gota

To apply functions to columns and rows of a DataFrame, use the `.Capply()` and `.Rapply()` methods on the DataFrame object, respectively.

These take in the function to be applied on the column or row:

```go
df.Capply(function)
df.Rapply(function)

```

Here's a full example that shows a simple DataFrame created from a single Series. In it, the `.Capply()` and `.Rapply()` methods are used to apply a function to calculate the mean of a column:

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

### How to Use Describe on a DataFrame in Gota

Use `.Describe()` on a DataFrame object to return descriptive statistics on the values of the DataFrame:

```go
description := df.Describe()

```

And here's a full example:

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

**Output:**

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

## How to Export DataFrames (Writing Files in Go)

Once you're finished manipulating your data, you can use the `.WriteCSV()` and `.WriteJSON()` methods to export your data as a CSV or JSON file.

### How to Export DataFrames as a CSV File

To export your data as a CSV file, just use the `.WriteCSV()` method on the DataFrame object you want to export as a CSV file.

First, use the `os` package to create a file, then pass that file to the `df.WriteCSV()` method to export your DataFrame as a CSV:

```go
file, err := os.Create("output.csv")
if err != nil {
	log.Fatal(err)
}

df.WriteCSV(file)

```

Here's a full example that shows building a DataFrame from a CSV string, updating the DataFrame, and exporting the updated DataFrame as a CSV file:

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

And the following CSV will be should be written to `output.csv`:

```
Name,Age,Favorite Color,Height(ft)
Jesse,34,Indigo,3.500000
Mary,40,Blue,5.700000
Peter,33,Violet,3.300000

```

### How to Export DataFrames as a JSON File

Exporting your data as a JSON file is very similar, and just uses the `.WriteJSON()` method on the DataFrame object you want to export.

Here's a full example:

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

And you should now have a file named `output.json` with the following JSON array:

```json
[{"Age":34,"Favorite Color":"Indigo","Height(ft)":3.5,"Name":"Jesse"},{"Age":40,"Favorite Color":"Blue","Height(ft)":5.7,"Name":"Mary"},{"Age":33,"Favorite Color":"Violet","Height(ft)":3.3,"Name":"Peter"}]

```

## Conclusion

In this tutorial, you have learned how to perform data analysis in Go. You've also learned about the Gota package's various functions.

It's still a good idea to primarily use Python and R for data analysis as they are considered the industry standard. But Gota is useful for applications requiring speed and homogeneity.

Check out the [Gota documentation](https://pkg.go.dev/github.com/go-gota/gota/dataframe) to learn more or contribute to the project.

Have fun coding and exploring!

