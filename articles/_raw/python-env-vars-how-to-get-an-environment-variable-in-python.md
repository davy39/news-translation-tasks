---
title: Python Env Vars – How to Get an Environment Variable in Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-10T21:39:01.000Z'
originalURL: https://freecodecamp.org/news/python-env-vars-how-to-get-an-environment-variable-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Shittu-Olumide-Python-Env-Vars---How-to-get-an-Environment-Variable-in-Python.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nEnvironment variables play a crucial role in Python\
  \ programming. They provide a way to store and access configuration values, system-specific\
  \ information, and sensitive data. \nIn this article, we will explore various methods\
  \ to retr..."
---

By Shittu Olumide

Environment variables play a crucial role in Python programming. They provide a way to store and access configuration values, system-specific information, and sensitive data. 

In this article, we will explore various methods to retrieve environment variables in Python and discuss best practices for handling and managing them effectively.

## What is an Environment Variable?

An environment variable is a named value that can affect the behavior of processes running on a computer system or operating system. It is a dynamic value that is stored in the environment and can be accessed by various programs or scripts running on the system.

Environment variables are typically set by the operating system or by the user and are accessible to all programs and processes running on the system. They provide a way to store configuration settings, system-specific information, or sensitive data without hardcoding them directly into the code. Instead, the code can retrieve the values from the environment variables, allowing for flexibility, security, and portability.

Environment variables are commonly used in software development to configure applications based on the specific environment in which they are deployed. For example, an application may use environment variables to store database connection strings, API keys, file paths, or other settings that can vary across different environments (like development, staging, or production).

In Python, you can access and manipulate environment variables using the `os` module. This module provides functions and dictionaries to interact with the operating system, including the ability to retrieve the values of environment variables, set new variables, or modify existing ones.

## How to Access Environment Variables: 

To access environment variables in Python, we can leverage the built-in `os` module, which provides functions for interacting with the operating system.

### How to use the os module:

First, we need to import the `os` module into our Python script:

```python
import os
```

The `os.environ` dictionary allows us to access all the environment variables set on our system. We can retrieve the value of a specific environment variable using its name as the key:

```python
# Retrieving the value of the "PATH" environment variable
path = os.environ["PATH"]
print(path)
```

### How to retrieve specific environment variables: 

To retrieve an environment variable without causing an error if it doesn't exist, we can use the `os.environ.get()` method. This method takes the variable name as an argument and returns its value. If the variable doesn't exist, it returns `None` or a specified default value:

```python
# Retrieving the value of an environment variable with a default value
database_url = os.environ.get("DATABASE_URL", "localhost:5432")
print(database_url)
```

### Example Use Cases:

Retrieving system-specific information:

* **Accessing the `PATH` environment variable**: The `PATH` variable contains a list of directories that the operating system searches when executing a command. Retrieving its value allows us to locate executables or scripts easily.
* **Retrieving the current user's home directory**: The `HOME` or `USERPROFILE` environment variables store the path to the current user's home directory, which is useful for accessing user-specific files and directories.

Handling sensitive information:

* **Using environment variables for API keys and passwords**: Storing sensitive data, such as API keys and passwords, as environment variables instead of hardcoding them in the code improves security. We can retrieve these values in our Python scripts using the aforementioned methods.
* **Securing sensitive data outside of code**: By storing sensitive information as environment variables, we can separate configuration from code. This allows us to share code publicly while keeping sensitive data private.

## How to Set Environment Variables: 

We can also set environment variables using the `os.environ` dictionary.

### How to use `os.environ`: 

To set a new environment variable, we assign a value to a key in the `os.environ` dictionary:

```python
# Setting a new environment variable
os.environ["API_KEY"] = "YOUR_API_KEY"
```

To modify an existing environment variable, we can simply reassign a new value to the key:

```python
# Modifying an existing environment variable
os.environ["DATABASE_URL"] = "new_database_url"
```

## Best Practices and Tips for Using Environment Variables:

* **Naming conventions for environment variables**: It is good practice to use uppercase letters and underscores to name environment variables, making them easily distinguishable from regular variables.
* **Handling platform-specific differences**: Keep in mind that environment variable names can differ across platforms. For example, the `HOME` variable is used in Unix-like systems, while `USERPROFILE` is used in Windows. Account for such differences when retrieving environment variables.
* **Documenting and managing environment variables**: Maintain documentation that lists all the required environment variables for your application, including their purpose and default values. Utilize tools like `.env` files to manage environment variables during local development.
* **Using a .env file for local development**: During local development, it's often convenient to use a `.env` file to store environment variables. This file contains key-value pairs in the format `KEY=VALUE`, with each variable on a new line. We can use libraries like `python-dotenv` to load the variables from the file into our Python script automatically.

## Conclusion

In this article, we have explored different methods to retrieve environment variables in Python. We have learned how to access them using the `os.environ` dictionary and retrieve specific variables with default values. We have also discussed example use cases, such as retrieving system-specific information and handling sensitive data securely.

We have seen how to set environment variables using the `os.environ` dictionary, both for creating new variables and modifying existing ones. Following best practices, such as using naming conventions, handling platform-specific differences, and documenting variables, is crucial for effective management.

By utilizing environment variables in Python, we can enhance the flexibility, security, and portability of our applications. Remember to follow best practices and incorporate environment variables as a fundamental part of your Python development workflow.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

