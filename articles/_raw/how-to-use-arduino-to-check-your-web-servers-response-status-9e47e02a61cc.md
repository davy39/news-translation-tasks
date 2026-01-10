---
title: How to use Arduino to check your web server’s response status
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T21:13:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-arduino-to-check-your-web-servers-response-status-9e47e02a61cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bQ91iaTCYt1SEHw-S3Rmxg.jpeg
tags:
- name: arduino
  slug: arduino
- name: Electronics
  slug: electronics
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Harshita Arora

  Last year, I created Crypto Price Tracker (an app which was acquired by Redwood
  City Ventures this year). A back end member of my team had been using an Arduino
  setup to check web server response statuses continuously to get updates...'
---

By Harshita Arora

Last year, I created [Crypto Price Tracker](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8) (an app which was acquired by Redwood City Ventures this year). A back end member of my team had been using an Arduino setup to check web server response statuses continuously to get updates all the time. I found that setup to be pretty useful and interesting.

I researched about it and recreated the setup for myself. In this article, I’ll show you how you can build it yourself, too.

#### Things that you need:

1. [Arduino Uno](https://store.arduino.cc/usa/arduino-uno-rev3)
2. [Ethernet Shield for Arduino](http://a.co/d/cLNijNF) (to connect the Arduino to the Internet)
3. Ethernet Cable
4. A/B Type USB 2.0 Cable (Power cable for Arduino)
5. Male-to-Male Jumper Cables (x2)
6. Breadboard
7. LED (x1, any color)
8. Resistor (x1, >100 ohms works)

#### Setting It Up

1. Mount/Insert the Ethernet shield on the Arduino.
2. Insert the positive (longer) end of the LED into the breadboard slot 6a and the negative (shorter) end into slot 5a.
3. Insert one end of the **resistor** into the breadboard slot 1b and the other into slot 5b.
4. Insert one end of the **first** jumper cable into the breadboard slot 1e. Insert the other end into the GND slot of the Ethernet shield.
5. Insert one end of the **second** jumper cable into the breadboard slot 6e. Insert the other end into pin slot 2 of the Ethernet shield.
6. Connect the **Ethernet** cable from your router to your Ethernet shield.

This is what my setup looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qbA3umNhKDiZy1bBrQZy1g.jpeg)

7. Open a command line interface on your machine and check and note your default gateway. This can be done using `ipconfig` command on Windows or the `netstat -nr | grep default` command on Linux/Mac.

8. Download and install the Arduino IDE if you haven’t already.

9. Open the IDE and go to Files `-&`gt; Exampl`es` -> Eth`er`net -> WebClientRepeating. You should see the following code:

10. Edit the **line 37** to be an IP address in the range (1–254) of your default gateway IP. So for example, if my default gateway is 10.0.0.1, then I can use an IP address from 10.0.0.2 to 10.0.0.254. It is, however, important to make sure that the IP that you’re using doesn’t conflict with any other IP addresses on your network.

For this example, I changed the line of code to be:

`**IPAddress ip(10, 0, 0, 2);**`

11. Change the DNS in **line 40** to be **8.8.8.8** (this is the Google Public DNS and is just something I prefer, you may use a DNS that you prefer).

For this example, I changed the line of code to be:

`**IPAddress myDns(8, 8, 8, 8);**`

12. Change the URL in **line 45** to a URL matching your web server. If you would like to use an IP address instead, then comment **line 45** and uncomment **line 46**. Since I am using a web server that I’m hosting locally, for this example, I will use an IP address.

For this example, I changed the line of code to be:

`//char server[] = “[www.arduino.cc](http://www.arduino.cc)";`  
`IPAddress server(127,0,0,1);`

Note that the port or the path here is not important yet. Just the IP Address  
is needed. If you would like to change the port that is used for the GET  
request, you may change it on **line 94**.

For this example, I have hosted my local webserver on port 3000. Thus, I will change the code in **line 94** to something like this:

`if (client.connect(server, 3000)) {`

13. Edit the **GET** request that is pre-written in **lines 97 - 100** to follow this pattern:

`client.println(“GET /path_to_url HTTP/1.1”);`  
`client.println(“Host: 127.0.0.1”);`  
`client.println(“Connection: close”);`  
`client.println();`

14. We can now start programming the behaviour of the LED depending on the web server status and response. To do this, we must first declare the pin we’re using for the LED on our Ethernet shield.

Add the following line of code after the first two **include** statements of the program:

`int LED = 2;`

15. Add the following lines of code at the beginning of the _setup()_ function.

`pinMode(LED, OUTPUT);`

`digitalWrite(LED, LOW); //program starts with the LED turned off`

16. Add the following line of code after the GET request line that we previously edited:

`digitalWrite(LED, LOW);`

17. Finally, add this line of code at the beginning of the **else** statement of the same conditional:

`digitalWrite(LED, HIGH);`

And voilà, you’re done!

Upload the program to your Arduino. Open the serial monitor from the top right part of the IDE and watch the response. If your server doesn’t respond, the LED glows, if it does, the LED stays off :)

You can check out my final code [here](https://gist.github.com/harshitaarora/1e096fe2ba7915964742e3f324f15184).

#### Checking Response

If you would also like to **validate** the response that you receive from your  
web server, then you may add them inside the following conditional of the  
program.

`if (client.available()) {`  
`char c = client.read();`  
`Serial.write(c);`  
`}`

The variable **c** is where the response is stored.  
You could check it like this:

`if (client.available()) {`

`char c = client.read();`  
`if(c == “arduino is great”){`  
 `digitalWrite(LED, LOW); //correct response`  
`}`  
`else{`  
`digitalWrite(LED, HIGH); //wrong response`  
`}`  
`Serial.write(c);`  
`}`

Do note that, if you’re trying to do this, then it’s best to get rid of the  
digitalWrite statement after the GET request. Depending on your response,  
you may also have to parse JSON values. There are several ways to do this  
and plenty of tutorials/articles around for it too! Make sure to check them  
out!

Have fun! Feel free to email me at `harshita (at) harshitaapps.com` for any questions, feedback, or ideas!

Make sure to check out [Crypto Price Tracker](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8) app if you’re interested/invested in cryptocurrencies! :)

