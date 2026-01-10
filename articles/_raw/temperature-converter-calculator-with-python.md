---
title: How to Build a Temperature Converter Calculator with Python
subtitle: ''
author: David Fagbuyiro
co_authors: []
series: null
date: '2023-03-13T23:00:14.000Z'
originalURL: https://freecodecamp.org/news/temperature-converter-calculator-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-maksim-goncharenok-5995230.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Temperature conversion is a fundamental topic in physics and engineering.
  It''s also important in many disciplines for research and various applications.

  For example, temperature measurements are critical for effective data analysis and
  interpretation...'
---

Temperature conversion is a fundamental topic in physics and engineering. It's also important in many disciplines for research and various applications.

For example, temperature measurements are critical for effective data analysis and interpretation in everything from weather forecasting to material research. As a result, having an effective and easy-to-use temperature converter calculator is critical for both professionals and students. 

In this tutorial, we'll look at how to create a temperature converter calculator in Python. Python is a popular programming language with a large community and many helpful libraries, making it an excellent choice for creating a temperature converter calculator.

You will learn how to make a powerful and effective temperature conversion calculator that can convert between multiple temperature scales such as Celsius, Fahrenheit, and Kelvin by following the step-by-step directions in this tutorial.

### Requirements:

To follow along with this tutorial, you will need to have Python installed on your computer. You can download the latest version of Python from the official website.

We will also be using the Python standard library, which should be included with your Python installation.

## How to Build the Temperature Converter Calculator

The first step in creating our temperature converter calculator is to define the temperature scales that we want to convert between. 

In this example, we will be converting between Celsius, Fahrenheit, and Kelvin. We will create a dictionary that maps each temperature scale to a unique identifier.

```python
TEMPERATURE_SCALES = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K'
}
```

Next, we will define a function to convert a temperature from one scale to another. This function will take as input the temperature value, the input temperature scale, and the output temperature scale. It will then use the appropriate conversion formula to convert the temperature to the desired scale.

```python
def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else:
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32) / 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5 / 9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9 / 5 - 459.67
        else:
            return value
    else:
        return value
```

Now that we have our conversion function, we can create the main program. We will use a while loop to repeatedly prompt the user for input until they choose to quit. 

For each conversion, we will prompt the user for the input temperature value, the input temperature scale, and the output temperature scale. We will then call our conversion function to convert the temperature and print the result.

```python
while True:
    # Prompt the user for input
    print('Enter the input temperature value:')
    value = float(input())
    print('Enter the input temperature scale (C, F, or K):')
    input_scale = input().upper()
    print('Enter the output temperature scale (C, F, or K):')
    output_scale = input().upper()

    # Convert the temperature and print the result
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

    # Prompt the user to continue or quit
    print('Enter q to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'q':
        break
```

When you run the program, you will see the following output:

```python
Enter the input temperature value:

```

You can then enter the input temperature value, the input temperature scale (C, F, or K), and the output temperature scale (C, F, or K). The program will then convert the temperature and print the result. You can continue to convert temperatures until you choose to quit by entering 'q'.

This is the output of the above code:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-133.png)

## Conclusion

In this article, we have demonstrated how to create a temperature converter calculator using Python. With just a few lines of code, we can build a robust and efficient temperature converter that can convert between Celsius, Fahrenheit, and Kelvin.

