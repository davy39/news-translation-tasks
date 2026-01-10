---
title: How to make your own Python dev-server with Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T17:10:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-own-python-dev-server-with-raspberry-pi-37651156379f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ylvkldd2jkFaSSpn8MdVTQ.png
tags:
- name: Python
  slug: python
- name: Raspberry Pi
  slug: raspberry-pi
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Karan Asher

  In simple terms, Raspberry Pi is a super cheap ($40) Linux based computer. That’s
  it. Seriously.

  It can do whatever you can imagine a normal Linux computer can do, such as browse
  the web, write code, edit documents, and connect to I/O ...'
---

By Karan Asher

_In simple terms, Raspberry Pi is a super cheap ($40) Linux based computer. That’s it. Seriously._

It can do whatever you can imagine a normal Linux computer can do, such as browse the web, write code, edit documents, and connect to I/O devices such a thumb drive, mouse, keyboard, etc. This tutorial will be focused on learning how to make your own Python dev-server with Raspberry Pi.

### Step 0. Define the goal

Before we begin, it is important to understand what is it that we are trying to build. By the end of the tutorial, you will be able to run a basic website (using [Flask](http://flask.pocoo.org/)) off of a Raspberry Pi on your local home network.

The goal of this tutorial is to demonstrate how a Pi can be used as a dev-server, more specifically, the example will be to host a simple website (using [Flask](http://flask.pocoo.org/)).

### Step 1. State the assumptions

Here are some assumptions that this tutorial will make:

1. You already have a Raspberry Pi set up with Raspbian OS. [Here](https://www.raspberrypi.org/documentation/setup/) is a useful setup guide if you need one.
2. The Pi is connected to your home WiFi (and that you know the Pi’s IP address).
3. You will not require a screen going forward. assuming points 1 and 2 are complete.

We will use [VS Code](https://code.visualstudio.com/) with the [Remote VSCode](https://marketplace.visualstudio.com/items?itemName=rafaelmaiolla.remote-vscode) extension to remotely create and edit files on the Pi. I definitely recommend that you use these two to follow along. Also, these will make working with remote files a lot easier, so that’s a plus.

### Step 2. Find the Pi’s IP address

First, connect the Pi to a power supply, and ensure that it is correctly booted up and connected to the WiFi/Ethernet (basically, it needs to have an internet connection).

We will use ssh to connect to and communicate with the Pi. To do that remotely using a laptop, you need to know its IP address. This can be easily obtained using your ISP’s admin portal (usually available at [http://192.168.0.1](http://192.168.0.1). Please note that this could be different for different ISPs.)

Usually, you should have your Pi connected to an address which may look similar to ‘192.168.0.12.’ Again, this will be different for different people. So please use the IP address that you found for your Pi in the admin portal. Going forward, this tutorial will use 192.168.0.12 as the Pi’s IP address.

### Step 3. Connect to the Pi using ssh

Open VS Code and its built-in terminal window on your laptop. Connect to the Pi with an IP address of 192.188.0.12 using the following ssh command:

> _ssh -R 52698:localhost:52698 pi@192.168.0.12_

The above command will set up a 2-way communication channel between your laptop and the Pi. If this is the first time you are connecting to the Pi, use raspberry as the password. You may be prompted to change your default password. It is highly recommended that you do so.

![Image](https://cdn-media-1.freecodecamp.org/images/k-iRsowxI6mnJfpiWmQPGkQOiaRQ8OE50gpg)
_Terminal window after successfully connecting to the pi_

### Step 4. Create a project directory

You should now be in the home directory of the Pi. Let’s create a directory for the website we wish to build. Use the following command to create the directory:

> _mkdir MyFlaskWebsite_

Use the ‘ls’ command to verify that you can indeed see a new folder named MyFlaskWebsite.

![Image](https://cdn-media-1.freecodecamp.org/images/cUhjzjTdVOTdFCANjEYrStpwuNoy4YsKWTZj)
_Create and verify the project directory_

### Step 5. Install Flask

We will use [Flask](http://flask.pocoo.org/) to create a simple website. [Flask](http://flask.pocoo.org/) is a Python based micro web framework. It uses [Jinja](http://jinja.pocoo.org/) (Python based template engine) as its template engine which makes it very usable and powerful. Use the following command to install flask on the Pi:

> _sudo apt-get install python3-flask_

![Image](https://cdn-media-1.freecodecamp.org/images/JBEt1A3RTqaIUErc0sevCZjxpZMppU1qTCjA)
_Install flask_

### Step 6. Write some basic code

Now that Flask is installed, we can start creating files and writing some code. First, navigate to your newly created project directory (from step 4) by using the following command:

> _cd MyFlaskWebsite_

All project files and folders will reside inside this ‘MyFlaskWebsite’ directory. Now, create your first code file (app.py) using the following command:

> _touch app.py_

On checking the directory using the ‘ls’ command, you should be able to see this newly created file.

![Image](https://cdn-media-1.freecodecamp.org/images/Ad9fp3IFU8Q2TtuKgRC3f3-dInXyaEQ-6NZH)
_Navigate to project directory and create a new file_

Now, press F1 and choose ‘Remote Start Server.’ This should allow you to remotely edit files on the Pi using your laptop.

![Image](https://cdn-media-1.freecodecamp.org/images/UB9XT8GkO3T49BOvUd6iAX6yn2iAbHiqKbqi)
_Start the remote server_

Next, use the following command to start editing the newly created app.py file. It might take a few seconds but the empty file should then be visible in the window right above.

> _rmate app.py_

![Image](https://cdn-media-1.freecodecamp.org/images/O4Ybu5hVBCof4wGQ8q4z5c4MEA5zvNgBzkXv)
_Start editing the file remotely_

Type out the code shown in the below picture. Here, we have defined a route to the home page of the website which should display ‘This is my flask website and it is so cool.’ Note that setting the host to 0.0.0.0 allows this website to be accessible by all devices connected to the same network.

![Image](https://cdn-media-1.freecodecamp.org/images/oyV0xCTNN59M32nPsaqLs5oCB8IwBNfgqiWC)
_Create a basic website_

Save the file and use the following command to run the website on the Pi server:

> _python3 app.py_

![Image](https://cdn-media-1.freecodecamp.org/images/V1gtV9AL1LrQnyZaQhq-5zk7eCuvaNMrmsWw)
_Run the website_

On receiving the above success message, open a new browser window on any device within your network and type out the Pi’s IP address (in this case, it is 192.168.0.12) followed by the port the dev-server is running on (5000.) So the complete address will be [http://192.168.0.12:5000/](http://192.168.0.12:5000/)

You should see the text ‘This is my flask website and it is so cool.’ on the webpage.

![Image](https://cdn-media-1.freecodecamp.org/images/3OunjfD19vW0jkUprzpCRgxftK3PU1cWf2mT)
_Check the webpage in a browser_

This confirms that your dev-server is active and is running the website you just created.

### Step 7. Add more routes

Currently, the code consists of only 1 route which is the home page of the website. Add another route by typing out the following code. Note that you can dynamically make changes while the dev-server is running. It will automatically capture the delta (code change) and run a revised version once you refresh your browser window.

![Image](https://cdn-media-1.freecodecamp.org/images/wFupha2dFoFLYbsxCjKwMHjnTXmD5YKLwuMu)
_Add a meow route_

To check whether or not the new route works as expected, go to [http://192.168.0.12:5000/meow](http://192.168.0.12:5000/meow) and the webpage should ‘MEOW’ at you.

![Image](https://cdn-media-1.freecodecamp.org/images/I-YacWJFs3S2wcDN2pVniaEwwkZj8B0XCZUN)
_Verify that the new route works as expected_

### Step 8. Add structure to your code

Now, adding more routes is cool but having the all the code in just 1 app.py file is not how a website should be structured. Usually, we would have a folder with HTML templates, a folder with static CSS files and another one for JS files. Let’s add these folders and move the code in appropriate folders to structure out code better. Use the following commands to create these directories:

> _mkdir templates_

> _mkdir static_

Use the ‘ls’ command to verify that these folders have been created.

![Image](https://cdn-media-1.freecodecamp.org/images/MfI2Gvi6kC0WFxxxRkS9Jn4HYdu8KWF56teL)
_Add structure to your code_

Now, let’s create an HTML file for the homepage. Use the following commands to navigate to the templates directory. Then, create a new file named index.html and use rmate to edit the same:

> _cd templates_

> _touch index.html_

> _rmate index.html_

![Image](https://cdn-media-1.freecodecamp.org/images/C7xLB4tDdW3twueajM9Elzh5LxD169l6DAuw)

Write some basic HTML code for the homepage inside index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/nLyBtnwKxFGqhx9d52DxFMj6mBE2u9gq-qXP)
_HTML code for the homepage_

Make the following changes in app.py to use the index.html file. The below code will search for a file named index.html in the templates directory by default.

![Image](https://cdn-media-1.freecodecamp.org/images/lfuYCPtema6YCe4t1y7pCj8yxOZXPYGtzx8I)
_Use the new index.html file and render it using app.py_

Navigate back to the project directory and run the website again.

![Image](https://cdn-media-1.freecodecamp.org/images/xnv7ptoeZLKzqOmUNfLBhZPgubKooaWj-D3-)

Go back to the home page and you should see the content you put inside of index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/Lh1CRnj7mtlxmzyDPFjALEBRYAC0CvzcwyDn)

Now add some styling by creating ‘main.css’ inside the static directory. As always, use the ‘cd’ command to change the directory, ‘touch’ command to create a new file, and ‘rmate’ command to edit the same file.

![Image](https://cdn-media-1.freecodecamp.org/images/SNa8U2sOoIrMN6tuAsBmtbHFUX43Vfgfc05J)
_Create the css file_

Add some styling to the h4 tag. Note that we currently have 1 h4 tag in index.html which the css is supposed to modify.

![Image](https://cdn-media-1.freecodecamp.org/images/MUCDIINplzZwjSTrm-1fBkev15z0q7Juku3n)
_Some css code_

As always, test your changes by using the following command:

> _python3 app.py_

![Image](https://cdn-media-1.freecodecamp.org/images/zY2hMd8vwNjCYVsVs-DyfY7rkBOur3IC66DS)

Notice how the text within the h4 tag gets colored according to the CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/VElytx48rZcyMNhmx3xUt6pf4PVjM3RZrmct)

### Step 9. Take advantage of Jinja

[Jinja](http://jinja.pocoo.org/) in a Python based template engine which adds a lot of powerful features to webpages. Although this tutorial is not focused on learning Jinja, let’s just look at a simple example of how Jinja can be useful.

Let’s just create a list of fruits in app.py and pass it as a parameter to index.html. We will then have index.html display that list on the webpage. Make the following changes in app.py and index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/Klh2Cgj-O8v8H4fYR8Jv00o-QiemELP-iH9t)
_Pass the my_list as a parameter to index.html_

![Image](https://cdn-media-1.freecodecamp.org/images/k3KZzf3MzBJCxvljXa0RoQKYzRPfc5kGl8JR)
_Display my_list on the webpage_

Refresh your webpage and you should see the list of fruits on screen.

![Image](https://cdn-media-1.freecodecamp.org/images/o8hYHuUKS47d9bESOKFOhiUs1FR8JTKuL3MY)

This speaks to how powerful and useful Jinja can be. For more info on Jinja, please refer to [this](http://jinja.pocoo.org/).

### Step 10. Next steps

Now that you have a fully functional Python dev-server, the possibilities going forward are practically infinite. Here are a few useful next steps that you may consider for your project:

1. Currently, the Pi is accessible only through the devices within your personal network. To expose the Pi to the outside world (access it through any device outside your personal network), you need something known as port forwarding. Basically, you need a domain name and a static IP address which is permanently assigned to the Pi. More info [here](https://www.raspberrypi.org/documentation/remote-access/access-over-Internet/README.md) and [here](https://maker.pro/raspberry-pi/projects/raspberry-pi-web-server).
2. Most applications will require a database for basic CRUD operations. Python supports SQlite right out of the box. Learn how to use SQlite with Flask [here](http://flask.pocoo.org/docs/1.0/patterns/sqlite3/) and [here](https://www.tutorialspoint.com/flask/flask_sqlite.htm).
3. [Here’s a cool Raspberry Pi starter kit on Amazon](https://www.amazon.com/CanaKit-Raspberry-Starter-Premium-Black/dp/B07BCC8PK7/ref=sr_1_1_sspa?ie=UTF8&qid=1536006349&sr=8-1-spons&keywords=raspberry+pi+canakit&psc=1). The neat thing about this is that it has everything you need to get started and saves you the effort of searching individual items yourself.
4. Since you are not using a screen, it is important that you use the shutdown command for the Pi using the terminal. This ensures that the Pi and the SD card are not damaged:

> _sudo shutdown -h now_

#UntilNextTime.

