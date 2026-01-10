---
title: Python Program Examples – Simple Code Examples for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-17T17:09:25.000Z'
originalURL: https://freecodecamp.org/news/python-program-examples-simple-code-examples-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/python-program-examples-image.png
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: null
seo_desc: 'By Shittu Olumide

  Mark Twain said that the secret of getting ahead is getting started. Programming
  can seem daunting for beginners, but the best way to get started is to dive right
  in and start writing code.

  Simple code examples are a great way for b...'
---

By Shittu Olumide

Mark Twain said that the secret of getting ahead is getting started. Programming can seem daunting for beginners, but the best way to get started is to dive right in and start writing code.

Simple code examples are a great way for beginners to get their feet wet and learn the basics of programming. In this article, I will provide a series of simple code examples that are perfect for Python beginners. 

These examples cover a range of programming concepts and will help you develop a solid foundation in programming. Whether you're new to programming or just looking to brush up on your skills, these code examples will help you get started on your coding journey.

If you need to learn some Python basics, I've added some helpful resources at the end of this tutorial.

## How to Build a Number Guessing Game in Python

In this project, you will create a simple number guessing game that allows the user to guess a random number between 1 and 100. The program will give hints to the user after each guess, indicating whether their guess was too high or too low, until the user guesses the correct number.

**Code**:

```py
import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

```

**Explanation**:

* Start by importing the `random` module, which will allow you to generate a random number.
* Generate a random number between 1 and 100 using the `randint()` function from the `random` module, and assign it to a variable.
* Create a loop that allows the user to guess the number until they guess correctly. Inside the loop, prompt the user to enter their guess using the `input()` function, and convert their input to an integer using the `int()` function.
* Add a conditional statement inside the loop that checks whether the user's guess is correct, too high, or too low. If the guess is correct, print a congratulatory message and break out of the loop. If the guess is too high or too low, print a hint message to help the user guess the number correctly.
* Run the program and play the number guessing game!

## How to Build a Simple Password Generator in Python

A password generator, as the name implies, generates a random password of a particular length using different combination of characters, and special characters.

**Code**:

```py
import random
import string

def generate_password(length):
    """This function generates a random password
    of a given length using a combination of
    uppercase letters, lowercase letters,
    digits, and special characters"""
    
    # Define a string containing all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password using a random selection of characters
    password = "".join(random.choice(all_chars) for i in range(length))
    
    return password

# Test the function by generating a password of length 10
password = generate_password(10)
print(password)

```

**Explanation**:

* We import the `random` and `string` modules which we use to generate random values and work with strings, respectively.
* Next, we define a function called `generate_password` that takes a single parameter `length`, which specifies the length of the password that needs to be generated.
* Inside the function, we define a string called `all_chars` which contains all possible characters that can be used to generate the password. We use the `string.ascii_letters`, `string.digits`, and `string.punctuation` constants to create this string.
* We then use list comprehension to generate a list of `length` random characters from the `all_chars` string using the `random.choice()` function. Finally, we join these characters together into a single string using the `"".join()` function and return the result.
* To test the function, we call it with an argument of 10 to generate a password of length 10 and print the result.

Note that this is a very simple password generator and may not be suitable for use in real-world scenarios where security is a concern.

## How to Build a Password Checker in Python

We will build a password checker in this section. Its job is to check if a password is strong enough based on some of the criteria we set. It'll print an error if any of the password criteria isn't met.

**Code**:

```py
# Define a function to check if the password is strong enough
def password_checker(password):
    # Define the criteria for a strong password
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"
    
    # Check the length of the password
    if len(password) < min_length:
        print("Password is too short!")
        return False
    
    # Check if the password contains an uppercase letter, lowercase letter, digit, and special character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True
    
    # Print an error message for each missing criteria
    if not has_uppercase:
        print("Password must contain at least one uppercase letter!")
        return False
    if not has_lowercase:
        print("Password must contain at least one lowercase letter!")
        return False
    if not has_digit:
        print("Password must contain at least one digit!")
        return False
    if not has_special_char:
        print("Password must contain at least one special character!")
        return False
    
    # If all criteria are met, print a success message
    print("Password is strong!")
    return True

# Prompt the user to enter a password and check if it meets the criteria
password = input("Enter a password: ")
password_checker(password)

```

**Explanation**:

* In this code, we define a function called `password_checker()` that takes a password as an argument and checks if it meets certain criteria for strength.
* We first define the criteria for a strong password – a minimum length of 8 characters, at least one uppercase letter, one lowercase letter, one digit, and one special character.
* We then check the length of the password and whether it contains the required types of characters using a for loop that iterates through each character in the password.
* If the password fails to meet any of the criteria, we print an error message and return `False` to indicate that the password is not strong enough. Otherwise, we print a success message and return `True`.
* Finally, we prompt the user to enter a password using the `input()` function and pass it to the `password_checker()` function to check if it meets the criteria.

## How to Build a Web Scraper in Python

A web scraper scrapes/gets data from webpages and saves it in any format we want, either .csv or .txt. We will build a simple web scraper in this section using a Python library called Beautiful Soup.

**Code**:

```py
import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage you want to scrape
url = 'https://www.example.com'

# Send an HTTP request to the URL and retrieve the HTML content
response = requests.get(url)

# Create a BeautifulSoup object that parses the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the webpage
links = soup.find_all('a')

# Print the text and href attribute of each link
for link in links:
    print(link.get('href'), link.text)

```

**Explanation**:

* In this code, we first import the `requests` and `BeautifulSoup` modules which are used to make HTTP requests and parse HTML content, respectively.
* Next, we set the URL of the webpage that we want to scrape in a variable called `url`.
* We then use the `requests.get()` function to send an HTTP GET request to the URL and retrieve the HTML content of the webpage as a response.
* We create a `BeautifulSoup` object called `soup` that parses the HTML content of the response using the `html.parser` parser.
* We then use the `soup.find_all()` method to find all the links on the webpage and store them in a variable called `links`.
* Finally, we use a for loop to iterate through each link in `links` and print the text and href attribute of each link using the `link.get()` method.

## How to Build a Currency Converter in Python

A currency converter is a program that helps users convert the value of one currency into another currency. You can use it for a variety of purposes, such as calculating the cost of international purchases, estimating travel expenses, or analyzing financial data.

Note: we will use the ExchangeRate-API to get the exchange rate data, which is a free and open-source API for currency exchange rates. But there are other APIs available that may have different usage limits or requirements.

**Code**:

```py
# Import the necessary modules
import requests

# Define a function to convert currencies
def currency_converter(amount, from_currency, to_currency):
    # Set the API endpoint for currency conversion
    api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint)
    
    # Get the JSON data from the response
    data = response.json()
    
    # Extract the exchange rate for the target currency
    exchange_rate = data["rates"][to_currency]
    
    # Calculate the converted amount
    converted_amount = amount * exchange_rate
    
    # Return the converted amount
    return converted_amount

# Prompt the user to enter the amount, source currency, and target currency
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency code: ").upper()
to_currency = input("Enter the target currency code: ").upper()

# Convert the currency and print the result
result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")

```

**Explanation**:

* In this code, we define a function called `currency_converter()` that takes an amount, source currency code, and target currency code as arguments and returns the converted amount.
* We first set the API endpoint for currency conversion using the `from_currency` parameter and the `requests` module to send a GET request to the endpoint.
* We then extract the exchange rate for the target currency from the JSON data returned by the API using the `to_currency` parameter and calculate the converted amount by multiplying the exchange rate with the `amount` parameter.
* Finally, we prompt the user to enter the `amount`, `from_currency`, and `to_currency` using the `input()` function and pass them to the `currency_converter()` function to convert the currency. The converted amount is then printed using string formatting.

## Conclusion

All these projects are very simple and easy to build. If you really want to improve your Python skills, I'd advise you to take the code, modify and edit it, and build upon it. You can turn many of these simple projects into much more complex applications if you want.

If you need to learn some Python basics, check out these helpful resources:

* [How to build your first Python project – YouTube course](https://www.youtube.com/watch?v=_ZqAVck-WeM)
* [Python for Everybody – full university course from Dr. Chuck](https://www.youtube.com/watch?v=8DvywoWv6fI)
* [Learn Python for beginners – free courses](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/)
* freeCodeCamp's [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) and [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) certifications

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

