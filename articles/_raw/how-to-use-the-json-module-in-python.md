---
title: How to Use the JSON Module in Python – A Beginner's Guide
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-06-05T22:51:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-json-module-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/json-module.png
tags:
- name: json
  slug: json
- name: Python
  slug: python
seo_title: null
seo_desc: "JSON (JavaScript Object Notation) is a popular, lightweight data interchange\
  \ standard. It represents data structures made up of key-value pairs that's quite\
  \ straightforward and human-readable. \nJSON has become the industry standard for\
  \ data interchan..."
---

JSON (JavaScript Object Notation) is a popular, lightweight data interchange standard. It represents data structures made up of key-value pairs that's quite straightforward and human-readable. 

JSON has become the industry standard for data interchange between online services. And it's widely utilized in modern programming languages, including Python.

JSON data is frequently expressed as nested dictionaries, lists, and scalar values such as texts, numbers, booleans, and null. It is named JSON because it closely mimics the syntax used in JavaScript objects.

In this tutorial, you will explore the JSON module in Python and learn how to effectively work with JSON data.

## Python's Built-in JSON Module

JSON plays an important role in Python programming because it allows efficient data serialization and deserialization. It enables Python programs to effortlessly communicate with web services, exchange data, and store structured information. 

Developers can use JSON to seamlessly link their Python programs with a variety of APIs, databases, and external systems that use JSON for data representation.

If you're looking to learn how to interact with web services using Python, check out [my tutorial on the requests module](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python).

The built-in JSON module in Python provides a powerful set of methods and classes that make working with JSON data simple. Developers can use it to encode Python objects into JSON strings and decode JSON strings back into Python objects.

## How to Store JSON Data in a File

When working with JSON data in Python, you'll often need to save the data or share it with others. Storing JSON data in a file enables quick retrieval and data persistence. 

In this section, you'll learn how to use Python's `json.dump()` function to save JSON data to a file. This process involves serializing the JSON data and saving it to a file, which you can subsequently read and use as needed.

### The `json.dump()` function

The `json.dump()` function in Python allows you to store JSON data directly into a file. This function takes two parameters: the data to be serialized and the file object where the data will be written.

To write JSON data to a file, you need to follow a few steps. First, you need to open a file in write mode, specifying the file path. Then, you can use the `json.dump()` function to serialize the data and write it to the file. Finally, you need to close the file to ensure that all the data is properly saved.

Let's learn how to store data in a file using the horoscope API response as an example.

Assume you have made a GET request to the following URL: [https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today](https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today), which provides the daily horoscope for the Capricorn sign.

```python
import requests
import json

# Make the GET request to the horoscope API
response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()  # Convert the response to JSON

# Store the JSON data in a file
with open("horoscope_data.json", "w") as file:
    json.dump(data, file)

print("Data stored successfully!")
```

In the code above, you use the `requests` library to make a GET request to the [Horoscope API](https://blog.ashutoshkrris.in/how-to-create-a-horoscope-api-with-beautiful-soup-and-flask). You then extract the JSON data from the response using the `.json()` method. Finally, you open a file named `horoscope_data.json` in write mode using the `with` statement, and you use `json.dump()` to store the data in the file.

Check out [this tutorial](https://blog.ashutoshkrris.in/how-to-know-your-horoscope-using-python) to learn how to find out your horoscope using Python.

If you open the `horoscope_data.json` file, you'll see contents similar to below:

```json
{
  "data": {
    "date": "Jun 3, 2023",
    "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
  },
  "status": 200,
  "success": true
}
```

## How to Retrieve Data from a JSON File

You'll often need to read data from a JSON file. For example, you may need to read configuration settings from a JSON file. Python's JSON module provides the `json.load()` function, which allows you to read and deserialize JSON data from a file. 

In this section, you will learn how to use the `json.load()` function to retrieve JSON data from a file and work with it in your Python programs.

### The `json.load()` function

The `json.load()` function accepts a file object as an argument and returns deserialized JSON data in the form of Python objects such as dictionaries, lists, strings, numbers, booleans, and null values.

To read JSON data from a file, you need to open the file in read mode, extract the data using the `json.load()` function, and store it in a variable for further processing. It's important to ensure that the file being read contains valid JSON data – otherwise, it may raise an exception.

Let's see how you can retrieve the data from the previously created `horoscope_data.json` file:

```python
import json

# Retrieve JSON data from the file
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

# Access and process the retrieved JSON data
date = data["data"]["date"]
horoscope_data = data["data"]["horoscope_data"]

# Print the retrieved data
print(f"Horoscope for date {date}: {horoscope_data}")
```

In the code above, you open the file `horoscope_data.json` in read mode using the `with` statement. You then use the `json.load()` function to deserialize the JSON data from the file into the data variable. Finally, you access specific fields of the JSON data (e.g., "date" and "horoscope_data") and process them as needed.

## How to Format the JSON Output

When you read data from a JSON file and print it, the output is displayed as a single line, which may not resemble the structured format of JSON.

```python
import json

# Retrieve JSON data from the file
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

print(data)
```

Output:

```bash
{'data': {'date': 'Jun 3, 2023', 'horoscope_data': 'The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up.'}, 'status': 200, 'success': True}
```

### The `json.dumps()` function

The JSON module provides you with a `json.dumps()` function to serialize Python objects into a JSON formatted string. It provides various options for customization, including formatting the output to make it more human-readable.

The `json.dumps()` function provides several [options](https://docs.python.org/3/library/json.html#json.dumps) to customize the output. The most commonly used is the `indent` which allows you to specify the number of spaces used for indentation.

```python
import json

# Retrieve JSON data from the file
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

# Format the data
formatted_data = json.dumps(data, indent=2)

print(formatted_data)
```

Output:

```bash
{
  "data": {
    "date": "Jun 3, 2023",
    "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
  },
  "status": 200,
  "success": true
}
```

As you can see, the JSON data is now formatted with proper indentation, enhancing its readability. This technique can be applied to any JSON data, allowing you to present JSON output in a more organized and visually appealing way.

## The `json.tool` Command Line Tool

Python's JSON module provides a convenient command line tool called `json.tool` that allows you to format and pretty-print JSON data directly from the command line. It is a useful utility for quickly visualizing the structure and contents of JSON data in a more readable and organized format.

To use `json.tool`, you can execute the following command in your command-line interface:

```bash
python -m json.tool <input_file> <output_file>
```

where:

* `python -m json.tool` invokes the `json.tool` module using the Python interpreter.
* `<input_file>` represents the path to the JSON file you want to format.
* `<output_file>` is an optional argument that specifies the file to which you want to save the formatted JSON output. If not provided, the formatted output will be displayed on the console.

Let's say you have a `horoscope_data.json` file with the following contents:

```json
{
  "data": {
    "date": "Jun 3, 2023",
    "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
  },
  "status": 200,
  "success": true
}
```

Notice that the above JSON file has an indentation of two spaces.

To pretty-print this JSON file using `json.tool`, you can execute the following command:

```bash
python -m json.tool horoscope_data.json
```

The output will be:

```json
{
    "data": {
        "date": "Jun 3, 2023",
        "horoscope_data": "The forecast today is stormy. You may have sensed that there was some tension clouding the conversation at home. Resentments were left unsaid and subtle power games were played without resolution. Today, Capricorn, it all becomes too unbearable for you. Regardless of the risks involved, you will take measures to clear things up."
    },
    "status": 200,
    "success": true
}
```

As you can see in the example, executing the `json.tool` module with the input file path formats the JSON data and displays the formatted output on the console.

You can also redirect the formatted output to an output file by specifying the output file name as the second argument:

```bash
python -m json.tool horoscope_data.json formatted_data.json
```

This command formats the JSON data from `horoscope_data.json` and saves the formatted output to `formatted_data.json`.

## JSON Encoding Custom Objects

The JSON module in Python allows you to encode and decode custom objects by using JSON encoder and decoder classes. You can define custom serialization and deserialization logic for your objects using these classes.

`JSONEncoder` class allows you to customize the encoding process. To define how your custom object should be encoded into JSON format, you can extend the `JSONEncoder` and change its `default` method.

Here's an example of how you can extend the `JSONEncoder` class and customize the encoding process for a custom object:

```python
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)


# Create a custom object
person = Person("Ashutosh Krishna", 23)

# Encode the custom object using the custom encoder
json_str = json.dumps(person, cls=PersonEncoder)

# Print the encoded JSON string
print(json_str)
```

In this example, you define a custom class `Person` with `name` and `age` attributes. You then create a subclass of `JSONEncoder` called `PersonEncoder` and override its `default` method. Within the `default` method, you check if the object being encoded is an instance of `Person`. If it is, you provide a JSON-serializable representation of the object by returning a dictionary containing the `name` and `age` attributes. If the object is not of type `Person`, you call the `default` method of the superclass to handle other types.

By using `json.dumps` and specifying the `cls` parameter as your custom encoder class `PersonEncoder`, you can encode the `person` object into a JSON string. The output will be:

```bash
{"name": "Ashutosh Krishna", "age": 23}
```

Similarly, you can specify custom decoding logic in the JSON decoder class, `JSONDecoder`. To define how JSON data should be decoded into your custom object, extend the `JSONDecoder` and override its `object_hook` function.

## How to Create JSON from a Python Dictionary

You can use the `json.dumps()` function provided by the JSON module to create JSON from a [Python dictionary](https://blog.ashutoshkrris.in/everything-you-need-to-know-about-python-dictionaries). This function takes a Python object, typically a dictionary, and converts it into a JSON string representation.

```python
import json

# Python dictionary
data = {
    "name": "Ashutosh Krishna",
    "age": 23,
    "email": "ashutosh@example.com"
}

# Convert dictionary to JSON string
json_str = json.dumps(data)

# Print the JSON string
print(json_str)
```

In this example, you have a Python dictionary `data` representing some data. By calling `json.dumps(data)`, you convert the dictionary into a JSON string. The output will be:

```bash
{"name": "Ashutosh Krishna", "age": 23, "email": "ashutosh@example.com"}
```

## How to Create a Python Dictionary from JSON

To create a Python dictionary from JSON data, you can use the `json.loads()` function provided by the JSON module. This function takes a JSON string and converts it into a corresponding Python object, typically a dictionary.

```python
import json

# JSON string
json_str = '{"name": "Ashutosh Krishna", "age": 23, "email": "ashutosh@example.com"}'

# Convert JSON string to Python dictionary
data = json.loads(json_str)

# Access the dictionary values
print(data["name"])
print(data["age"])
print(data["email"])
```

In this example, you have a JSON string `json_str` representing some data. By calling `json.loads(json_str)`, you convert the JSON string into a Python dictionary. You can then access the values in the dictionary using their respective keys.

The output will be:

```bash
Ashutosh Krishna
23
ashutosh@example.com
```

## Wrapping Up

Understanding the Python JSON module is necessary for working with JSON data because it is widely used for data exchange and storage in a variety of applications. 

You can efficiently handle JSON data, interface with APIs, and deal with configuration files if you learn how to use the JSON module.


