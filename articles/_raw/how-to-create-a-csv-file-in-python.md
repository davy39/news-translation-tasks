---
title: How to Create a CSV File Using Python
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
seo_title: null
seo_desc: 'CSV is an acronym for comma-separated values. It''s a file format that
  you can use to store tabular data, such as in a spreadsheet. You can also use it
  to store data from a tabular database.

  You can refer to each row in a CSV file as a data record. Ea...'
---

**CSV** is an acronym for comma-separated values. It's a file format that you can use to store tabular data, such as in a spreadsheet. You can also use it to store data from a tabular database.

You can refer to each row in a CSV file as a data record. Each data record consists of one or more fields, separated by commas.

This article shows you how to use the Python built-in module called **csv** to create CSV files. In order to fully comprehend this tutorial, you should have a good understanding of the fundamentals of the Python programming language.

The csv module has two classes that you can use in writing data to CSV. These classes are:

* the `csv.writer` class
    
* the `csv.DictWriter` class
    

## How to Create a CSV File Using the `csv.writer` Class

You can use the `csv.writer` class to write data into a CSV file. The class returns a writer object, which you can then use to convert data into delimited strings.

To ensure that the newline characters inside the quoted fields interpret correctly, open a CSV file object with **newline=''**.

The syntax for the **csv.writer** class is as follows:

```python
csv.writer(csvfile, dialect=’excel’, **fmtparams)
```

Now, let me walk you through the meaning of the different parameters used in the syntax.

1. The `csvfile` parameter represents the csvfile object with the `write()` method.
    
2. The optional `dialect` parameter represents the name of the dialect you can use in writing the CSV file.
    
3. The optional `fmtparams` parameter represents the formatting parameters that you can use to overwrite the parameters specified in the dialect.
    

The **csv.writer** class has two methods that you can use to write data to CSV files. The methods are as follows:

### The `writerow()` Method

The `writerow()` method takes in iterable data as its parameter and then writes the data to your CSV file in a single row. One popular usage of the **writerow()** method is using it to write the field row of your CSV file.

Now let me show you how you can use the **writerow()** method to write a single row into your CSV file.

In your code editor, create a file with the name [*profiles1.py*](http://profiles1.py). Then write the following code in the file:

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

The explanation for the code in `profiles1.py` is as follows:

1. Line one imports the Python *csv* module.
    
2. Line two is a blank line that separates the imported module from the rest of the code.
    
3. Line three of the code opens the CSV file in writing (w mode) with the help of the `open()` function.
    
4. Line four creates a CSV writer object by calling the writer() function and stores it in the `writer` variable.
    
5. Line five creates a variable named `fields`, which stores a list that consists of strings, each representing the title of a column in the CSV file.
    
6. Line six and below writes the field data and other data to CSV file by calling the **writerow()** method of the CSV writer object.
    

Once you are done, go to your command line terminal and navigate to the directory that has the Python file *profiles1.py*. Run the following command:

```sh
python profiles1.py
```

You should get a CSV file named *profiles1.csv* in your working directory with the following text in it:

```bash
name,age,country
Oladele Damilola,40,Nigeria
Alina Hricko,23,Ukraine
Isabel Walter,50,United Kingdom
```

### The `writerows()` Method

The **writerows()** method has similar usage to the writerow() method. The only difference is that while the writerow() method writes a single row to a CSV file, you can use the **writerows()** method to write multiple rows to a CSV file.

To see how the **writerows()** method works, create a file named *profiles2.py* in your working directory. Then write the following code in the file you created:

```python
import csv

with open('profiles2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    row_list = [
        ["name", "age", "country"], 
        ["Oladele Damilola", "40", "Nigeria"], 
        ["Alina Hricko", "23" "Ukraine"], 
        ["Isabel Walter", "50" "United Kingdom"],
    ]
    
    writer.writerows(row_list)
```

After writing the code in your profiles2.py file, go to your command line terminal and run the following command:

```sh
python profiles2.py
```

Now you should have a CSV file named *profiles2.csv* in your working directory. The file should have the data in the `row_list` variable.

## How to Create a CSV File Using the `csv.DictWriter` Class

You can use the `csv.DictWriter` class to write a CSV file from a dictionary. This is unlike the csv.writer Class, which writes to a CSV file from a list.

The syntax for the **csv.DictWriter** is as follows:

```python
class csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)
```

Now let me explain the meaning of the different parameters in the syntax:

1. The `csvfile` represents the file object with the `write()` method
    
2. The `fieldnames` parameter is a sequence of keys that identify the order in which Python passes the values in the dictionary.
    
3. The `restval` parameter is optional and it specifies the value to be written if the dictionary is missing a key in fieldnames.
    
4. The `extrasaction` parameter is optional and it specifies the action to take if a key is not found in fieldnames. Setting this parameter to `raise`, raises a *ValueError*.
    
5. The `dialect` parameter is optional and it represents the name of the dialect you want to use.
    

The **csv.DictWriter** class has two methods that you can use to write data to CSV files. The methods are as follows:

### The `writeheader()` Method

Use the **writeheader()** method to write the first row of your csv file using the pre-specified `fieldnames`.

To see how the the **writeheader()** method works, create a new file named *profiles3.py* in your working directory. Then write the following code in the *profles3.py* file using your code editor:

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

The explanation of the code in *profiles3.py* is as follows:

1. Line one imports the Python *csv* module.
    
2. Line two is a blank space that separates the Python csv module from the rest of the code.
    
3. Line three stores a list that contains three different dictionaries in a variable named `mydict`. The dictionaries have the data of different profiles in them.
    
4. Line seven stores strings, which represent the title of each column of the CSV file that you want to create in a variable named `fields`.
    
5. Line nine opens the *profiles3.csv* file in writing mode using `open()` function.
    
6. The `csv.DictWriter()` function in line ten creates the CSV dictionary writer object.
    
7. Line twelve passes the list of dictionaries to the `writer.writeheader()` function to write the pre-defined field names.
    

Once you are done writing the code, go to your command line terminal and navigate to the directory that has the python file *profiles3.py*. Run the following command:

```sh
python profiles3.py
```

Now, you should get a CSV file a named *profiles3.csv* in your working directory that has the following text in it:

```bash
name,age,country
```

### The `writerows()` Method

The **writerows()** method has a similar usage as the writeheader() method. You can use the method to write all the rows. The method writes only the values and not the keys.

To use the **writerows()** method, add this line of code to your code in *profiles3.py*:

```python
writer.writerows(mydict)
```

Now delete the *profiles3.csv* in your working directory and re-run the following command in your command line terminal:

```sh
python profiles3.py
```

You should now have a new CSV file named *profiles3.csv* in your working directory that has the following text in it:

```bash
name,age,country
Kelvin Gates,19,USA
Blessing Iroko,25,Nigeria
Idong Essien,42,Ghana
```

## Conclusion

Although CSV got its name from a **comma**, the comma is just a delimiter that separates the data.

You should know that a comma is a popular delimiter you will get in most CSV files. However, the delimiter could also be something else. For instance, you can use a semi-colon to separate the data instead of a comma.

If you like this tutorial, kindly [follow me on Twitter](https://twitter.com/activus_d) and give me a shout out.

### References and Further Reading

* [https://docs.python.org/3/library/csv.html?highlight=csv](https://docs.python.org/3/library/csv.html?highlight=csv)
