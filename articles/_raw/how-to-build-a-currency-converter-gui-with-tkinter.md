---
title: How to Build a Currency Converter GUI with Tkinter
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-04-10T16:44:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-currency-converter-gui-with-tkinter
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/currency-converter.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Tkinter is a built-in Python library for creating graphical user interfaces\
  \ (GUIs). It provides a set of tools for building windows, frames, buttons, textboxes,\
  \ and other GUI elements. \nIt is easy to use and widely available, making it a\
  \ popular choi..."
---

Tkinter is a built-in Python library for creating graphical user interfaces (GUIs). It provides a set of tools for building windows, frames, buttons, textboxes, and other GUI elements. 

It is easy to use and widely available, making it a popular choice for building GUI applications in Python. It is also highly customizable, allowing developers to create unique and visually appealing user interfaces.

In this tutorial, you'll build a Currency Converter GUI application using Tkinter. Before you dive into the tutorial, it's worth noting that this is not the first time we're building a GUI application with Tkinter. In a previous tutorial, we built a [GUI Quiz App using Tkinter](https://blog.ashutoshkrris.in/how-to-build-a-gui-quiz-application-using-tkinter-and-open-trivia-db), and in another tutorial series, we built a [Password Manager](https://blog.ashutoshkrris.in/password-generator-using-python-and-tkinter-part-i). I encourage you to check out those tutorials as well.

Here's how your end result will look:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Converter.gif)

You can find the code for the tutorial in [this repository](https://github.com/ashutoshkrris/currency-converter-gui).

## Prerequisites

To follow along with this tutorial and build the application, you should have the following:

* Basic knowledge of the Python programming language
* Python 3.8+ installed on your system
* Familiarity with the [Tkinter](https://docs.python.org/3/library/tkinter.html) and [Requests](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python) libraries

## How to Set Up Your Virtual Environment

Before you start coding, you'll need to make sure you have all the necessary tools and libraries installed. To ensure that you have a clean and isolated environment, you'll create a virtual environment using `venv`.

Create a project directory and navigate to it in the terminal:

```bash
mkdir currency-converter
cd currency-converter
```

Create a virtual environment named `env` using the following command:

```bash
python -m venv env
```

Python now ships with the pre-installed `venv` library to create virtual environments.

Activate the virtual environment like this:

```bash
source env/bin/activate
```

Note: if you're on Windows, you'll need to use `source env/Scripts/activate` to activate the environment.

You should see `(env)` in your terminal prompt, indicating that the virtual environment has been activated.

### How to Install the Libraries

Now that you've created the virtual environment, you can install the following libraries:

* `requests`: The library helps you send requests on API endpoints.
* `python-decouple`: The library helps you read the values of environment variables.
* `pillow`: The library adds image processing capabilities to your Python interpreter.

To install the libraries, run the following command:

```bash
pip install requests python-decouple pillow
```

## How to Build the Currency Converter Utility Functions

In this section, you will start building the core functionality of our Currency Converter GUI. You will create two utility functions that will be used to convert currencies and retrieve currency codes from a JSON file.

To define the utility functions, you will create a new file called `utils.py` in the project. This file will contain all of your utility functions for the Currency Converter GUI.

### Utility Function to Get Currency Codes from the JSON File

This utility function will retrieve currency codes from a JSON file. This function will allow you to populate the GUI with a list of available currencies that the user can select from.

Create a `currency.json` file that includes the currency code and name of various currencies. The JSON file has the following structure:

```json
[
  { "AED": "United Arab Emirates Dirham" },
  { "AFN": "Afghan Afghani" },
  { "ALL": "Albanian Lek" },
  ...
]
```

You can obtain the content of the `currency.json` file from [this link](https://github.com/ashutoshkrris/currency-converter-gui/blob/main/currency.json) and copy it into the `currency.json` file in your project.

Add the following code to define the first utility function:

```python
import json

def get_currencies() -> list:
    currency_codes = []
    with open('currency.json') as f:
        currency_data = json.load(f)
        for currency in currency_data:
            code, _ = list(currency.items())[0]
            currency_codes.append(code)
    return sorted(currency_codes)
```

In the above code, you define a `get_currencies()` function that returns a list of currency codes. Inside the function, you create an empty list called `currency_codes` which you will use to store the currency codes. Then, you open the `currency.json` file in read mode and use the `json.load()` method to load the contents of the file into a Python dictionary called `currency_data`.

Next, you loop through each item in the `currency_data` dictionary using a `for` loop. Each item in the `currency_data` dictionary is a dictionary itself, with a single key-value pair representing a currency code and its name. Inside the `for` loop, you use the `list()` function to convert the key-value pair of each currency into a list. 

Since each dictionary contains only one key-value pair, we can use the `items()` method to convert the dictionary into a list of tuples containing the key-value pairs.

You then use [tuple unpacking](https://blog.ashutoshkrris.in/mastering-list-destructuring-and-packing-in-python-a-comprehensive-guide) to assign the first element of the list to the `code` variable and ignore the second element using `_`. 

Finally, you append the `code` variable, representing the currency code, to the `currency_codes` list. After looping through all the currencies in `currency_data`, you sort the `currency_codes` list in ascending order using the `sorted()` function and return it from the function.

If you call the function and print its result, you'll get the following output:

```bash
['ADA', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AVAX', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BNB', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DOT', 'DZD', 'EGP', 'ERN', 'ETB', 'ETH', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTC', 'LTL', 'LVL', 'LYD', 'MAD', 'MATIC', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'XRP', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']
```

### Utility Function to Convert Currencies

In order to build the currency converter, you need a utility function that can convert one currency to another. For this purpose, you'll use an external API to fetch the latest currency exchange value. While there are many currency exchange APIs available such as [API Forex](https://api.forex/), [Forex API](https://fxapi.com/), and so on, you're going to use the [Currency Conversion API](https://currencyapi.com/). 

You can integrate the API in your code either by using the `requests` module or its own `[currencyapi-python](https://github.com/everapihq/currencyapi-python)` library. As already mentioned, you'll use the `requests` module in this tutorial.

To use the API, you will need to sign up for an API key. You can sign up for a free account at [https://app.currencyapi.com/register](https://app.currencyapi.com/register). Once you have signed up, you can find your API key (highlighted in black) on the dashboard page.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-140705.png)

Create a `.env` file and add the following code to set the environment variable:

```
export API_KEY='your-api-key-here'
```

Copy your API Key from the dashboard and replace the `your-api-key-here` in the above file. Then run the following command to set the environment variables:

```bash
source .env
```

You then use the `python-decouple` library to read the API key values in the Python code. 

Next, in the same `utils.py` file, add the following code:

```python
import requests
from decouple import config


API_KEY = config('API_KEY')
API_ENDPOINT = 'https://api.currencyapi.com/v3/latest'

def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    query_params = {
        'apikey': API_KEY,
        'base_currency': from_currency,
        'currencies': to_currency
    }
    response = requests.get(API_ENDPOINT, params=query_params)
    currency_data = response.json()
    exchange_rate = currency_data['data'][to_currency]['value']
    exchanged_value = exchange_rate * amount
    return exchanged_value
```

The `convert_currency` function takes three arguments: `from_currency`, `to_currency`, and `amount`. `from_currency` and `to_currency` are the ISO currency codes for the currencies being converted and `amount` is the amount of the `from_currency` that you want to convert.

The function sends a GET request to the `API_ENDPOINT` URL with the `API_KEY`, `from_currency`, and `to_currency` as query parameters. The `requests.get()` function from the `requests` module is used to send the request and the `params` argument is used to pass the query parameters.

Once the response is received, we convert it into a Python dictionary using the `json()` method of the `response` object. A sample successful response looks like this:

```json
{
  "meta":{
    "last_updated_at":"2023-03-30T23:59:59Z"
  },
  "data":{
    "INR":{
      "code":"INR",
      "value":82.100841
    }
  }
}
```

You then extract the exchange rate from the response dictionary and calculate the exchanged value using the `amount` and `exchange_rate`. Finally, you return the exchanged value.

## How to Design the Currency Converter GUI with Tkinter

Now that you have the utility functions ready, you can design the GUI using Tkinter. Here's what the application will look like:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-203154.png)

The design includes a window of 300 X 320 size with a top frame and a main frame. The top frame contains the icon and title of the application. The main frame includes labels, combo boxes, entry widget, and button for currency conversion.

Let's build the application step by step. Create a `main.py` file in the project directory. First, import the necessary modules and functions, as well as define some color constants.

```python
from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

from utils import convert_currency, get_currencies

# Colors
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#333333"
BLUE_COLOR = "#0000FF"
```

### How to Create the Window

When creating a GUI app with Tkinter, the first step is to create a window with a specific size and title. In this case, the window size should be set to 300x320 and the title should be "Currency Converter". By default, the window background color is white, and it should not be resizable. Here's the code:

```python
# Window Configuration
window = Tk()
window.geometry("300x320")
window.title("Currency Converter")
window.configure(bg=WHITE_COLOR)
window.resizable(height=FALSE, width=FALSE)
```

### How to Create the Frames

As mentioned earlier, you need to create two frames – a top frame and a main frame. The top frame will contain the application icon and title, while the main frame will include essential widgets such as labels, entry widgets, combo boxes, and the conversion button. The following code accomplishes this:

```python
# Create top and main frames
top_frame = Frame(window, width=300, height=60, bg=BLUE_COLOR)
top_frame.grid(row=0, column=0)

main_frame = Frame(window, width=300, height=260, bg=WHITE_COLOR)
main_frame.grid(row=1, column=0)

```

Here, the `Frame()` function is used to create the two frames. The first argument is the parent window (which is `window` in this case), followed by the width, height and background color of the frames. You can then use the `grid()` method to place the frames in the window by specifying their row and column positions.

You place the `top_frame` widget in the first row and first column of the grid, while the `main_frame` widget in the second row and first column of the grid.

### How to Add Widgets in the Top Frame

Afterwards, you can create the widgets that belong to the top frame. The top frame should have an app icon and app title, as previously mentioned. You can obtain an icon from [Icons8](https://icons8.com/icons/set/exchange) (or from [here](https://github.com/ashutoshkrris/currency-converter-gui/blob/main/icon.png)) and save it in your project directory under the name `icon.png`.

```python
# Top Frame Widgets
icon_image = Image.open('icon.png')
icon_image = icon_image.resize((40, 40))
icon_image = ImageTk.PhotoImage(icon_image)
app_name_label = Label(top_frame, image=icon_image, compound=LEFT, text="Currency Converter", height=3, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=BLUE_COLOR, fg=WHITE_COLOR)
app_name_label.place(x=0, y=0)
```

The code first opens the image file `icon.png` using the PIL (Python Imaging Library) module's `Image` class. It then resizes the image to a size of 40x40 using the `resize()` method. Next, it converts the image to a format that can be displayed in the GUI using the `ImageTk` module's `PhotoImage` class.

The next line creates a `Label` widget that displays the app icon and title. You create the widget inside the top frame. The widget takes several parameters to configure its appearance.

The parameters include the following:

* the `image` of the app icon
* the `text` to be displayed ("Currency Converter")
* the `height` of the label (set to 3)
* padding on the left and top sides (set to 13 and 30, respectively)
* the anchor point of the label (set to the center) 
* the font style (`Arial 16 bold`)
* the background color (set to `BLUE_COLOR`)
* the foreground color (set to `WHITE_COLOR`)

Finally, we use the `place()` method to set the position of the label within the top frame. 

### How to Add Widgets in the Main Frame

As mentioned, the main frame will contain the essential widgets. Let's create them step by step.

The following code creates a Label widget named `result_label` inside the `main_frame` Frame. This label will display the result of the currency conversion. 

```python
result_label = Label(main_frame, text=" ", width=15, height=2, pady=7, padx=0, anchor=CENTER, font=('Ivy 16 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=SOLID)
result_label.place(x=50, y=10)
```

The label has text set to an empty string (" "), a width of 15, a height of 2 lines, and padding of 7 pixels on the y-axis and 0 pixels on the x-axis. The text will be centered using the `anchor=CENTER` option, and the font used is `Ivy 16 bold`. The background color of the label is set to white (`bg=WHITE_COLOR`), and the text color is black (`fg=BLACK_COLOR`). The `relief` option is set to SOLID to give the label a border. Finally, the label is placed at the coordinates (50, 10) using the `place()` method.

Next, in the application design, there are two labels – "From" and "To", each followed by a `ComboBox` below it.

```python
from_label = Label(main_frame, text="From", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
from_label.place(x=48, y=90)
from_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
from_combo['values'] = (get_currencies())
from_combo.current(0)
from_combo.place(x=50, y=115)


to_label = Label(main_frame, text="To", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
to_label.place(x=158, y=90)
to_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
to_combo['values'] = (get_currencies())
to_combo.current(1)
to_combo.place(x=160, y=115)
```

The first `Label` and `ComboBox` are for the currency to convert from. You create the label using the `Label()` function with the specified text, width, height, padding, font, and color settings. The Label is then placed in the main frame at the specified coordinates using the place() function. 

You then create a `ComboBox` using the `ttk.Combobox()` function with the specified width, font, and justification settings. The available values for the `ComboBox` are set using the `get_currencies()` function (imported from `utils.py`), and the default value is set to the first item in the list using the `current()` function. The `ComboBox` is also placed in the main frame at the specified coordinates using the `place()` function.

The second Label and ComboBox are for the currency to convert to. The Label and ComboBox are created and placed in a similar way to the first Label and ComboBox, with the only difference being the text and placement coordinates.

The last two widgets in the application design are the input field and the convert button. You can use the `Entry()` method to create the input field. It takes several parameters including `width`, `justify`, `font`, and `relief`. The created widget is then placed using the `place()` method with specific coordinates on the main frame.

Similarly, the convert button is created using the `Button()` method. It takes several parameters such as `text`, `width`, `height`, `bg`, `fg`, `font`, and `command`. The created button is then placed using the `place()` method with specific coordinates on the main frame.

Here's the code to create the input field and convert button:

```python
amount_entry = Entry(main_frame, width=22, justify=CENTER,
                    font=('Ivy 12 bold'), relief=SOLID)
amount_entry.place(x=50, y=155)

convert_button = Button(main_frame, text="Convert", width=19, padx=5,
                        height=1, bg=BLUE_COLOR, fg=WHITE_COLOR, font=('Ivy 12 bold'), command=convert)
convert_button.place(x=50, y=210)
```

The `command` parameter in the `convert_button` widget takes a function name. In this case, it's set to `convert`. But the `convert` function has not been defined yet. To define it, you can add the following code just before the window is defined:

```python
def convert():
    amount = float(amount_entry.get())
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    converted_amount = convert_currency(from_currency, to_currency, amount)

    result_label['text'] = f'{to_currency} {converted_amount:.2f}'
```

The `convert` function takes the user input from the `amount_entry` widget and the selected currencies from the `from_combo` and `to_combo` widgets, and passes them to the `convert_currency` function(imported from `utils.py`) to obtain the converted amount. It then sets the value of  `text` to the exchanged value in the `result_label` widget.

Finally, you call the `mainloop()` method at the end of the file. The method is responsible for running the application and continuously checking for user events, such as mouse clicks, keyboard inputs, and window resizing, and updating the window as necessary. 

Once the `mainloop()` method is called, the program enters into the event loop and starts waiting for user events. The window will remain open and active until the user closes the window or the program is terminated.

```python
# Mainloop
window.mainloop()
```

## Final Code

Here is the final code for the Currency Converter GUI application that you have been building. This code incorporates all the different components we have discussed so far, including creating frames, labels, combo boxes, entry fields, and buttons.

```python
from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

from utils import convert_currency, get_currencies

# Colors
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#333333"
BLUE_COLOR = "#0000FF"


def convert():
    amount = float(amount_entry.get())
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    converted_amount = convert_currency(from_currency, to_currency, amount)

    result_label['text'] = f'{to_currency} {converted_amount:.2f}'


# Window Configuration
window = Tk()
window.geometry("300x320")
window.title("Currency Converter")
window.configure(bg=WHITE_COLOR)
window.resizable(height=FALSE, width=FALSE)


# Frames
top_frame = Frame(window, width=300, height=60, bg=BLUE_COLOR)
top_frame.grid(row=0, column=0)

main_frame = Frame(window, width=300, height=260, bg=WHITE_COLOR)
main_frame.grid(row=1, column=0)


# Top Frame Widgets
icon_image = Image.open('icon.png')
icon_image = icon_image.resize((40, 40))
icon_image = ImageTk.PhotoImage(icon_image)
app_name_label = Label(top_frame, image=icon_image, compound=LEFT, text="Currency Converter", height=3, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=BLUE_COLOR, fg=WHITE_COLOR)
app_name_label.place(x=0, y=0)

# Main Frame Widgets
result_label = Label(main_frame, text=" ", width=15, height=2, pady=7, padx=0, anchor=CENTER, font=('Ivy 16 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=SOLID)
result_label.place(x=50, y=10)

from_label = Label(main_frame, text="From", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
from_label.place(x=48, y=90)
from_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
from_combo['values'] = (get_currencies())
from_combo.current(0)
from_combo.place(x=50, y=115)

to_label = Label(main_frame, text="To", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
to_label.place(x=158, y=90)
to_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
to_combo['values'] = (get_currencies())
to_combo.current(1)
to_combo.place(x=160, y=115)

amount_entry = Entry(main_frame, width=22, justify=CENTER,
                    font=('Ivy 12 bold'), relief=SOLID)
amount_entry.place(x=50, y=155)

convert_button = Button(main_frame, text="Convert", width=19, padx=5,
                        height=1, bg=BLUE_COLOR, fg=WHITE_COLOR, font=('Ivy 12 bold'), command=convert)
convert_button.place(x=50, y=210)

# Mainloop
window.mainloop()

```

You can finally run the application and start converting currencies!

## Conclusion

In this tutorial, you learned how to create a simple currency converter application using Python and Tkinter. We covered topics such as creating frames, labels, entry widgets, combo boxes, and buttons. You also created a function to convert currencies based on the user's input. 

There are several ways to improve this application. You can improve the user interface to look more attractive, add a feature to save the conversion history, and much more.

If you've followed along with this tutorial and built your own Currency Converter application, I encourage you to share your creation with the world! Take a screenshot or record a video of your application in action, and share it on Twitter. Be sure to tag me, [@ashutoshkrris](https://twitter.com/ashutoshkrris), so that I can see your work and share it with my followers.

I can't wait to see what you've created! Happy coding!

### Additional Resources

* [Github repository](https://github.com/ashutoshkrris/currency-converter-gui) for the tutorial
* [Create Graphic User Interfaces in Python Tutorial](https://www.youtube.com/watch?v=YXPyB4XeYLA)
* [How to interact with web services in Python](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python)
* [Currency Conversion API Documentation](https://currencyapi.com/docs)

