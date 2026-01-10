---
title: How to Create Stunning QR Codes with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-21T15:40:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-stunning-qr-codes-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/How-to-create-stunning-QR-codes-with-python-1.png
tags:
- name: Python
  slug: python
- name: qr code
  slug: qr-code
seo_title: null
seo_desc: "By Shittu Olumide\nA quick response (QR) code is a barcode that a digital\
  \ device can easily scan. It encodes data as a series of pixels in a square grid.\
  \ \nTracking information about supply chains using QR codes is very useful in marketing\
  \ and advertis..."
---

By Shittu Olumide

A quick response (QR) code is a barcode that a digital device can easily scan. It encodes data as a series of pixels in a square grid. 

Tracking information about supply chains using QR codes is very useful in marketing and advertising campaigns.

The International Organization for Standardization certified QR codes as a global standard in 2000. They are an improvement over the previous uni-dimensional barcodes (ISO).

QR codes were developed in the 1990s to provide more information than a regular barcode. They were created by Denso Wave, a Toyota affiliate, to monitor the production of vehicles. 

In contrast to barcodes, which need a beam of light to bounce off the parallel lines, QR codes may be scanned digitally by devices like smartphones.

QR codes are used in cryptocurrency systems to enable digital payments, such as when displaying a Bitcoin address. QR codes are also often used to communicate site URLs to mobile devices. 

In this article, we will use the `segno` library to create beautiful QR codes that perform so many functions. 

## What is Segno?

[Segno](https://pypi.org/project/segno/0.1.5/#:~:text=Segno%20%E2%80%93%20Python%20QR%20Code%20and,Codes%20with%20nearly%20no%20effort.) is an open-source QR code generator that lets you create both regular and micro QR codes with very little effort. It also doesn't have any dependencies. 

Segno offers a few serialization types like SVG, EPS, PNG, PDF, and text output. None of these serializers calls on an external library. Through a plugin design, Segno offers other serialization types. PyPy and Python versions 2.6 to 3.4 were used for testing.

### How to Install Segno

Just like every other Python library, you can install Segno via pip.

```py
pip install segno

```

## How to Create a QR Code

So, using the `.make()` method, let's start by making the most basic QR code possible. Since the content is so brief, Segno automatically generates a fun-sized "micro QR" code, which carries raw data and that you can copy or transfer.

```py
import segno

price_tag = segno.make("Hello World")
price_tag.save("hello-world.png")

```

The QR code is generated and saved into our project directory.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Price-Tag.png)
_hello-world.png_

We can add a border to the QR code to make it look more attractive. You can do this by adding the `border` parameter to the `.save()` method.

```py
import segno
qrcode = segno.make('Vampire Blues')
qrcode.save('vampire-blues.png', border=5)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/vampire-blues.png)
_output: vapire-blues.png_

The QR codes that we have been creating have been very small. We can make them look bigger by adding the scale parameter like this:

```py
import segno
qrcode = segno.make_qr('Welcome')
qrcode.save('welcome.png', scale=10)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/welcome.png)
_welcome.png_

### How to Create Colorful QR Codes

We can also create some colorful QR codes with Segno – they are really beautiful. This is possible with the help of many serializers which accept the parameters dark and light to specify the color of the dark modules and light modules.

Here are a couple examples to give you an idea of what's possible:

```py
import segno
qrcode = segno.make("Green ave, Kingston")
qrcode.save('address.png', dark='darkred', light='lightblue', scale=10)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/address.png)
_address.png_

```py
import segno
qrcode = segno.make("Green ave, Kingston")
# Dark modules with alpha transparency
qrcode.save('address2.png', dark='#0000ffcc', scale=10)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/address2.png)
_address2.png_

```py
import segno
micro_qrcode = segno.make('Rain', error='q')
micro_qrcode.save('rain.png', dark='darkblue', data_dark='steelblue', scale=5)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/rain.png)
_rain.png_

## How to Save QR Codes in Different Formats

Segno give us the flexibility to save our generated QR codes in different file formats such as `.svg`, `.png`, `.eps`, and `.pdf`.

Here's how you would do that:

```py
import segno
qrcode = segno.make('Beatles')
qrcode.save('Beatles.svg')
qrcode.save('Beatles.png')
qrcode.save('Beatles.eps')

```

## Use Cases for QR Codes with Examples

### How to Make a QR Code for URL Sharing

We can easily generate a QR code that links to a URL. This lets us get online content by using the same technique with a little bigger payload.

We will create a QR code that links to my YouTube channel (Velcast Podcast), and then we will save it.

Here's the code for that:

```py
import segno

video = segno.make('https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A')
video.save('Video.png', dark="yellow", light="#323524", scale=5)

```

And the result:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Video.png)
_video.png_

### How to Make a QR Code for a WiFi Configuration

We can also use the Segmo library to create a QR code for wifi configuration. The `segno.helpers` module offers factory methods to generate standard QR codes for encoding geographic coordinates, `vCards` and `MeCards`, `WIFI setups`, and `EPC QR Codes`. 

The error correction level "L" is utilized in creating QR codes. If possible, we will apply the higher error correction level without altering the QR Code version.

The density of the QR code picture decreases with decreasing error correction level, which enhances minimum printing size. The more damage it can withstand before losing its ability to be read, the greater the error correction level.

The optimal balance between density and toughness for general marketing use is Level L or Level M. In industrial settings where maintaining a clean or undamaged QR code may be difficult, Level Q and Level H are the best options.

```py
from segno import helpers

qrcode = helpers.make_wifi(ssid='MyWifi', password='1234567890', security='WPA')
qrcode.designator
'3-M'
qrcode.save('wifi-access.png', scale=10)

```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/wifi-access.png)
_wifi-access.png_

We can also do this code this way:

```py
import segno
wifi_settings = {    
    ssid='(Wifi Name)',    
    password='(Wifi Password)',    
    security='WPA',
    }
wifi = segno.helpers.make_wifi(**wifi_settings)
wifi.save("Wifi.png", dark="yellow", light="#323524", scale=8)

```

We can use either of the two options for the code. They result in the same thing but represent different styles of writing and presentation.

Common use cases of using QR codes for wifi access include:

* Instead of giving consumers unique access codes, businesses may use QR codes to offer free WiFi access. Customers only need to scan the code to have access.
* Families can use it to grant visitors access to their internet at home.

### How to Encode Contact Details in QR Codes

We can also store contact details in a QR code. We just need to make use of the `helpers.make_mecard()` method and we can pass in the contact details. It's also important to note that we can pass in a list to the method.

Let's look at an example:

```py
from segno import helpers
qrcode = helpers.make_mecard(name='Shittu Olumide', email='me@example.com', phone='+123456789')
qrcode.designator
'3-L'
# Some params accept multiple values, like email, phone, url
qrcode = helpers.make_mecard(name='Shittu Olumide', 
                             email=('me@example.com', 'email@example.com'),
                             url=['http://www.example.com', 'https://example.come/~olu'])
qrcode.save('mycontact.png', scale=5)

```

Segno also allows you to perform the following actions:

* **segno.helpers.make_geo**: Launch the built-in mapping program at a certain Latitude and Longitude.
* **segno.helpers.make_email**: Send a message using a preset topic and body. Excellent for activating any number of potential activities from a mail server, like subscribing to newsletters, registering your arrival somewhere, and more.
* **segno.helpers.make_epc_qr**: Initiate an electronic payment.

### QR code use cases

Now that you've learned how to create QR codes, here are some of their applications in businesses and in our daily lives:

* Digital payments.
* Sharing business information.
* Sharing personal contact information.
* QR code menus in restaurants.
* Facilitating WiFi authentication.

And many more.

## Conclusion

Hopefully, this short article has whetted your appetite and inspires you to employ QR codes in your work and personal projects. 

By developing some eye-catching, functioning QR codes in this article, we tested the Segno Python module. You can read the official [documentation](https://segno.readthedocs.io/en/latest/) to learn more about the library.

