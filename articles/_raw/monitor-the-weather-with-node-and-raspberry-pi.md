---
title: How to Use Node, a Raspberry Pi, and an LCD Screen to Monitor the Weather
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-30T18:34:14.000Z'
originalURL: https://freecodecamp.org/news/monitor-the-weather-with-node-and-raspberry-pi
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vinicius-amnx-amano-ALpEkP29Eys-unsplash.jpg
tags:
- name: hardware
  slug: hardware
- name: projects
  slug: projects
- name: Raspberry Pi
  slug: raspberry-pi
- name: smart home
  slug: smart-home
seo_title: null
seo_desc: "By Stan Georgian\nOver the last few years, smart home devices have gone\
  \ from less than 300,000 back in 2015 up to almost 1.2 billion in 2020. And they’re\
  \ expected to grow to 1.5 billion by 2021. \nSo it's likely you have at least some\
  \ smart devices in ..."
---

By Stan Georgian

Over the last few years, smart home devices have gone from less than 300,000 back in 2015 up to almost 1.2 billion in 2020. And they’re expected to grow to [1.5 billion by 2021](https://www.omdia.com/resources/product-content/how-the-smart-home-will-develop-by-2021). 

So it's likely you have at least some smart devices in your home, given that the average will reach 8.7 smart devices per home by 2021.

As developers, we have some advantage in this domain, since we can build our own smart home devices.

It’s not only the devices that have experienced rapid development. The development boards used for them have started to become more and more commercial and accessible. 

In this article, we will see how we can use a Raspberry Pi, an LCD screen, and a few lines of code to monitor the weather outside or for a specific location.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/ezgif-6-8af115ff0d25.gif)

Because this is a Do It Yourself (DIY) project, there are some prerequisites that we need for this device.

## Prerequisites

* Raspberry Pi 3 (or higher)
* LCD Screen
* Connection Wires
* Potentiometer (Optional)
* Breadboard (Optional)

# How to Build It

As soon as we have everything we need we can start. Let's take it step by step.

## Step I - Base Configuration

The first step consists of the basic setup and a verification of all the components.

For this demo, we will use the ClimaCell Weather API as a weather data provider, as they have a large number of indicators, including air quality indicators, for us to use.

To use their API we must open an account on their platform and get an API key, which we’ll use to sign our requests.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/bQHbP2FU.png)
_ClimaCell API Limit_

The account is free to open and it comes with a 100-hour limit of API calls, which is more than enough for our project.

As soon as we have this API key, we can move to the hardware configuration and connect the LCD screen to our Raspberry Pi. You should turn the Raspberry Pi off while you make the wire connection.

The pin layout for Raspberry Pi 3 can be seen in the next image.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/emiVLiHU.png)
_Raspberry Pi 3 Pins_

The wire connection between the LCD and the development board is the following:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/WWjB6lbg.png)
_Connection between Raspberry PI and LCD_

This hardware connection will make the LCD screen be on full brightness and full contrast. The brightness level is not a problem, but contrast is because we won’t be able to see the characters on the screen. 

That’s why we need to introduce at least one potentiometer with which to set the contrast level.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/DFu8N63z.png)
_Schematic_

At this point, we can turn on our Raspberry Pi and we should see the LCD screen alive. With the help of variable resistance we should be able to control the contrast.

## Step II - Project Configuration

As a programming language, we’ll use [NodeJS](https://nodejs.org/en/) to write the code. If you don’t already have NodeJS installed on your Raspberry then you can follow these [simple instructions](https://www.instructables.com/id/Install-Nodejs-and-Npm-on-Raspberry-Pi/).

In a new folder, run the command `npm init -y` to set up a new npm package, followed by the command `npm install lcd node-fetch` to install these 2 necessary dependencies.  


* `lcd` will be used to communicate with the LCD Screen
* `node-fetch`  will be used to make [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) requests to ClimaCell API.

We said that we need an API key to communicate with the weather data provider. You place your secret API key directly in the main code, or you can create a `config.json` file in which you can place this key and any other code-related configuration you may have.

`config.json`

```javascript
{  "cc_key": "<your_ClimaCell_API_key>"}
```

Lastly, let’s create the main file of our project and include all these things we talked about.

```javascript
// * Dependencies
const Lcd = require("lcd");
const fs = require("fs");
const fetch = require("node-fetch");

// * Globals
const { cc_key } = JSON.parse(fs.readFileSync("./config.json"));

```

## Step III - The LCD

Writing on the screen is a piece of cake using the lcd module. This library acts as a layer of abstraction over how we communicate with the device. In this way we don’t need to micro-manage each command individually.

The entire code for our LCD screen is the following:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/MidH14Tk.png)
_[RAW](https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&amp;t=seti&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=const%2520lcd%2520%253D%2520new%2520Lcd(%257B%2520rs%253A%252026%252C%2520e%253A%252019%252C%2520data%253A%2520%255B13%252C%25206%252C%25205%252C%252011%255D%252C%2520cols%253A%252016%252C%2520rows%253A%25202%2520%257D)%253B%250A%250A%250Afunction%2520writeToLcd(col%252C%2520row%252C%2520data)%2520%257B%250A%2520%2520return%2520new%2520Promise((resolve%252C%2520reject)%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520lcd.setCursor(col%252C%2520row)%253B%250A%2520%2520%2520%2520lcd.print(data%252C%2520(err)%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520%2520%2520if%2520(err)%2520%257B%250A%2520%2520%2520%2520%2520%2520%2520%2520reject()%253B%250A%2520%2520%2520%2520%2520%2520%257D%250A%2520%2520%2520%2520%2520%2520resolve()%253B%250A%2520%2520%2520%2520%257D)%253B%250A%2520%2520%257D)%253B%250A%257D)_

The first step was to create a new `lcd` object and to pass as argument the pins we’ve used.

The keys `cols` and `rows` represent the number of columns and rows of our LCD display. 16x2 is the one I used in this example. If your LCD has just 8 columns and 1 row, then replace 16 and 2 with your values.

To write something on the display we need to use these two methods successively:

* lcd.setCursor() - selecting the position from which to start writing
* lcd.print()

At the same time, we wrapped these two functions in a promise to make use of `async/away` keywords.

At this point, you can use this function and print something on your display. `writeToLcd(0,0,'Hello World')` should print the message `Hello World` on the first row starting from the first column.

## Step IV - The Weather Data

The next step is to get the weather data and print it on the display.

ClimaCell provides a lot of weather data information, but also air quality and pollen, fire and other information. The data is vast, but keep in mind that your LCD screen only has 16 columns and 2 rows – that’s just 32 characters.

If you want to display more types of data and this limit is too small for you, then you can use a scroll effect.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/81w9nkUg.gif)

For this demo we’ll keep it simple and we’ll print on the LCD screen the following data:

* current date (hour, minutes, seconds)
* temperature
* precipitation intensity

![Image](https://www.freecodecamp.org/news/content/images/2020/06/zj8FQisB.png)
_[RAW](https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&amp;t=seti&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=async%2520function%2520getWeatherData(apiKey%252C%2520lat%252C%2520lon)%2520%257B%250A%2520%2520const%2520url%2520%253D%2520%2560https%253A%252F%252Fapi.climacell.co%252Fv3%252Fweather%252Frealtime%253Flat%253D%2524%257Blat%257D%2526lon%253D%2524%257Blon%257D%2526unit_system%253Dsi%2526fields%253Dtemp%2526fields%253Dprecipitation%2526apikey%253D%2524%257BapiKey%257D%2560%253B%250A%250A%2520%2520const%2520res%2520%253D%2520await%2520fetch(url)%253B%250A%2520%2520const%2520data%2520%253D%2520await%2520res.json()%253B%250A%2520%2520return%2520data%253B%250A%257D%250A%250Aasync%2520function%2520printWeatherData()%2520%257B%250A%2520%2520const%2520%257B%2520temp%252C%2520precipitation%2520%257D%2520%253D%2520await%2520getWeatherData(cc_key%252C%252045.658%252C%252025.6012)%253B%250A%250A%2520%2520%252F%252F%2520*%2520first%2520row%250A%2520%2520await%2520writeToLcd(0%252C%25200%252C%2520Math.round(temp.value)%2520%252B%2520temp.units)%253B%250A%250A%2520%2520%252F%252F%2520*%2520second%2520row%250A%2520%2520const%2520precipitationMessage%2520%253D%250A%2520%2520%2520%2520%2522Precip.%253A%2520%2522%2520%252B%2520precipitation.value%2520%252B%2520precipitation.units%253B%250A%2520%2520await%2520writeToLcd(0%252C%25201%252C%2520precipitationMessage)%253B%250A%257D)_

To get data from ClimaCell for a specific location, then you need to send its geographical coordinates, latitude and longitude.

To find your city’s coordinates, you can use a free tool like [latlong.net](https://www.latlong.net/place/new-york-city-ny-usa-1848.html) and then you can save them in `config.json` file along with your API key, or you can write them directly in the code.

At this point the data format returned by the API call is the following:

```javascript
{
  lat: 45.658,
  lon: 25.6012,
  temp: { value: 17.56, units: 'C' },
  precipitation: { value: 0.3478, units: 'mm/hr' },
  observation_time: { value: '2020-06-22T16:30:22.941Z' }
}
```

We can deconstruct this object and get the temp and the precipitation values and print them on the first and second row.

## Step V - Wrap it Up

All we need to do now is to write the logic for our script, and update the LCD screen when new data arrives.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/oeM4lSfQ.png)
_[RAW](https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&amp;t=seti&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=async%2520function%2520main()%2520%257B%250A%2520%2520await%2520printWeatherData()%253B%250A%250A%2520%2520setInterval(()%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520printWeatherData()%253B%250A%2520%2520%257D%252C%25205%2520*%252060%2520*%25201000)%253B%250A%250A%2520%2520setInterval(async%2520()%2520%253D%253E%2520%257B%250A%2520%2520%2520%2520await%2520writeToLcd(8%252C%25200%252C%2520new%2520Date().toISOString().substring(11%252C%252019))%253B%250A%2520%2520%257D%252C%25201000)%253B%250A%257D%250A%250Alcd.on(%2522ready%2522%252C%2520main)%253B%250A%250A%252F%252F%2520*%2520If%2520ctrl%252Bc%2520is%2520hit%252C%2520free%2520resources%2520and%2520exit.%250Aprocess.on(%2522SIGINT%2522%252C%2520(_)%2520%253D%253E%2520%257B%250A%2520%2520lcd.close()%253B%250A%2520%2520process.exit()%253B%250A%257D)%253B)_

The weather data is updated every 5 minutes. But because we have a limit of 100 API Calls / Hour imposed by ClimaCell, we can go even further and update the weather data each minute.

For the current date, we have two options: 

* we can use the property `observation_time` and display the date at which the data was received, or 
* we can make a real clock and display the current time.

I chose the second option, but feel free to do it as you please.

To print the time in the upper right corner, we must first calculate the starting column so that the text fits snugly. For this we can use the next formula `total columns number` minus `text to display length`

The date has 8 characters and because he has 16 columns, we must start from column number 8.

The LCD setting is asynchronous, so we must use the method `lcd.on()` provided by the related library, so we know when the LCD has been initialized and is ready to be used.

Another best practice in embedded systems is to close and free the resources that you use. That’s why we use the `SIGNINT` event to close the LCD screen when the program is stopped. Other events like this one include:  


* `SIGUSR1` and `SIGUSR2` - to catch "kill pid” like nodemon restart
* `uncaughtException` - to catch uncaught exceptions

## Step VI - Run it Forever

The script is complete and at this point we can run our program. We just have one more thing we must do before we can finish. 

At this point you’re probably connected to your Raspberry Pi using SSH or directly with an HDMI cable and a monitor. No matter what, when you close your terminal the program will stop. 

At the same time if you power off your device and after some time or immediately power it on again, the script will not start and you’ll have to do it manually.

To solve this problem, we can use a process manager like [pm2](https://www.npmjs.com/package/pm2).

Here are the steps:  


1. `sudo npm install pm2 -g` - install pm2
2. `sudo pm2 startup` - create a startup script for pm2 manager
3. `pm2 start index.js` - start an application
4. `pm2 save` - save your process list across server restart

Now you can reboot your board and the script will start automatically when the device is ready.

# Conclusion

From this point you can customize your new device however you want. If you find this weather data important for you (or any other data from ClimaCell, like air pollution, pollen, fire index or road risk), you can create a custom case to put the Raspberry Pi and the LCD display in it. Then after you added a battery you can place the device in your house.

[Raspberry Pi](https://www.raspberrypi.org/) is like a personal computer, so you can do much more on it than you would normally do on a microcontroller like [Arduino](https://www.arduino.cc/). Because of this, it's easy to combine it with other devices you have in your house.

