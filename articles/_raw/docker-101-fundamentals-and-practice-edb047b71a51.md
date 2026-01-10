---
title: 'Docker 101: Fundamentals and Practice'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-14T22:54:17.000Z'
originalURL: https://freecodecamp.org/news/docker-101-fundamentals-and-practice-edb047b71a51
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mgaoUlIJzr502lhY.jpg
tags:
- name: Docker
  slug: docker
- name: nginx
  slug: nginx
- name: Productivity
  slug: productivity
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Guilherme Pejon

  If you''re tired of hearing your coworkers praise Docker and its benefits at every
  chance they get, or you''re tired of nodding your head and walking away every time
  you find yourself in one of these conversations, you''ve come to the...'
---

By Guilherme Pejon

If you're tired of hearing your coworkers praise Docker and its benefits at every chance they get, or you're tired of nodding your head and walking away every time you find yourself in one of these conversations, you've come to the right place.

Also, if you are looking for a new excuse to wander off without getting fired, keep reading and you'll thank me later.

![Image](https://cdn-media-1.freecodecamp.org/images/GXyh0RbblBFolxVst-ZN6DWd3CnUk5aREezM)
_Source: [developermemes](http://www.developermemes.com" rel="noopener" target="_blank" title=")_

### Docker

Here's Docker's definition, according to [Wikipedia](https://en.wikipedia.org/wiki/Docker_(software)):

> Docker is a computer program that performs operating-system-level virtualization.

Pretty simple, right? Well, not exactly. Alright, here's my definition of what docker is:

> Docker is a platform for creating and running **containers** from **images**.

Still lost? No worries, that's because you probably don't know what **containers** or **images** are.

**Images** are single files containing all the dependencies and configurations required to run a program, while **containers** are the instances of those images. Let's go ahead and see an example of that in practice to make things clearer.

> **Important note:** Before you continue, make sure you [install docker](https://docs.docker.com/install/) using the recommended steps for your operating system.

### Part 1. "Hello, World!" from a Python image

Let's say you don't have Python installed in your machine — or at least not the latest version - and you need python to print "Hello, World!" in your terminal. What do you do? You use docker!

Go ahead and run the following command:

```
docker run --rm -it python:3 python
```

Don't worry, I'll explain that command in a second, but right now you are probably seeing something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/i7DalGXQXEQYdUQS2FMMsn0x62Kz1KSq8Igx)
_It might take a few moments for this command to run for the first time_

That means we are currently inside a **docker container** created from a python 3 **docker image,** running the `python` command. To finish off the example, type `print("Hello, World!")` and watch as the magic happens.

![Image](https://cdn-media-1.freecodecamp.org/images/A-pKIHg3d-pdx9vDt50v3bmW6z0JTTde5X-P)
_A "Hello, World!". Much wow!_

Alright, you did it, but before you start patting yourself on the back, let's take a step back and understand how that worked.

#### **Breaking it down**

Let's start from the beginning. The `docker run` command is docker's standard tool to help you start and run your containers.

The `--rm` flag is there to tell the Docker Daemon to clean up the container and remove the file system after the container exits. This helps you save disk space after running short-lived containers like this one, that we only started to print "Hello, World!".

The `-t (or --tty)` flag tells Docker to allocate a virtual terminal session within the container. This is commonly used with the `-i (or --interactive)` option, which keeps STDIN open even if running in detached mode (more about that later).

> **Note:** Don't worry too much about these definitions right now. Just know that you will use the`-it` flag anytime you want to type some commands on your container.

Lastly, `python:3` is the base image we used for this container. Right now, this image comes with python version 3.7.3 installed, among other things. Now, you might be wondering where did this image came from, and what's inside of it. You can find the answers to both of these questions right [here](https://hub.docker.com/_/python/), along with all the other python images we could have used for this example.

Last but not least, `python` was the command we told Docker to execute inside our `python:3` image, which started a python shell and allowed our `print("Hello, World!")` call to work.

#### One more thing

To exit python and terminate our container, you can use CTRL/CMD + D or `exit()`. Go ahead and do that right now. After that, try to execute our `docker run` command again and you'll see something a little bit different, and a lot faster.

![Image](https://cdn-media-1.freecodecamp.org/images/PjuutqjPnUNWh3q5mgQjJ0hs9qEqfPgJAlG1)
_Much faster. Wow!_

That's because we already downloaded the `python:3` image, so our container starts a lot faster now.

### Part 2. Automated "Hello World!" from a Python image

What's better than writing "Hello, World!" in your terminal once? You got it, writing it twice!

Since we cannot wait to see "Hello, World!" printed in our terminal again, and we don't want to go through the hustle of opening up python and typing `print` again, let's go ahead and automate that process a little bit. Start by creating a `hello.py` file anywhere you'd like.

```
# hello.py
```

```
print("Hello, World!")
```

Next, go ahead and run the following command from that same folder.

```
docker run --rm -it -v $(pwd):/src python:3 python /src/hello.py
```

This is the result we are looking for:

![Image](https://cdn-media-1.freecodecamp.org/images/NEXiMrDxjadvG2DEDuGRSXg05HsDuqA5QAju)
_Great! YAHW (Yet Another "Hello World!")_

> **Note:** I used `ls` before the command to show you that I was in the same folder that I created the `hello.py` file in.

As we did earlier, let's take a step back and understand how that worked.

#### Breaking it down

We are pretty much running the same command we ran in the last section, apart from two things.

The `-v $(pwd):/src` option tells the Docker Daemon to start up a **volume i**n our container**.** Volumes are the best way to persist data in Docker. In this example, we are telling Docker that we want the current directory - retrieved from `$(pwd)` - to be added to our container in the folder `/src`.

> **Note:** You can use any other name or folder that you want, not only `/src`

If you want to check that `/src/hello.py` actually exists inside our container, you can change the end of our command from `python hello.py` to `bash`. This will open an interactive shell inside our container, and you can use it just like you would expect.

![Image](https://cdn-media-1.freecodecamp.org/images/IbjkecLbC0HhtIFcvHz7IYEEubn05ZU1Gnkt)
_Isn't that crazy?_

> **Note:** We can only use `bash` here because it comes pre-installed in the `python:3` image. Some images are so simple that they don't even have `bash`. That doesn't mean you can't use it, but you'll have to install it yourself if you want it.

The last bit of our command is the `python /src/hello.py` instruction. By running it, we are telling our container to look inside its `/src` folder and execute the `hello.py` file using `python`.

Maybe you can already see the wonders you can do with this power, but I'll highlight it for you anyway. Using what we just learned, we can pretty much run **any code** from **any language** inside **any computer** without having to install **any dependencies** at the host machine - except for Docker, of course. That's a lot of **bold text** for one sentence, so make sure you read that twice!

### Part 3. Easiest "Hello, World!" possible from a Python image using Dockerfile

Are you tired of saying hello to our beautiful planet, yet? That's a shame, cause we are gonna do it again!

The last command we learned was a little bit verbose, and I can already see myself getting tired of typing all of that code every time I wanna say "Hello, World!" Let's automate things a little bit further now. Create a file named `Dockerfile` and add the following content to it:

```
# Dockerfile
```

```
FROM python:3
```

```
WORKDIR /src/app
```

```
COPY . .
```

```
CMD [ "python", "./hello.py" ]
```

Now run this command in the same folder you created the `Dockerfile`:

```
docker build -t hello .
```

All that's left to do now is to go crazy using this code:

```
docker run hello
```

![Image](https://cdn-media-1.freecodecamp.org/images/xkJM8U1zy7RgVHoFgMXr1ZbRxRmynsDIz1Jr)
_Note that you don’t even need to be in the same folder anymore_

You already know how it is. Let's take a moment to understand how a Dockerfile works now.

#### Breaking it down

Starting with our Dockerfile, the first line `FROM python:3` is telling Docker to start everything with the base image we are already familiar with, `python:3`.

The second line, `WORKDIR /src/app`, sets the working directory inside our container. This is for some instructions that we'll execute later, like `CMD` or `COPY`. You can see the rest of the supported instructions for `WORKDIR` right [here](https://docs.docker.com/engine/reference/builder/#workdir).

The third line, `COPY . .` is basically telling Docker to copy everything from our current folder (first `.`), and paste it on `/src/app` (second `.`). The paste location was set with the `WORKDIR` command right above it.

> **Note:** We could achieve the same results by removing the `WORKDIR` instruction and replacing the `COPY . .` instruction with `COPY . /src/app`. In that case, we would also need to change the last instruction, `CMD ["python", "./hello.py"]` to `CMD ["python", "/src/app/hello.py"]`.

Finally, the last line `CMD ["python", "./hello.py"]` is providing the default command for our container. It's essentially saying that every time we `run` a container from this configuration, it should run `python ./hello.py`. Keep in mind that we are implicitly running `/src/app/hello.py` instead of only `hello.py`, since that's what where we pointed our `WORKDIR` to.

> **Note:** The `CMD` command can be overwritten at runtime. For instance, if you want to run `bash` instead, you would do `docker run hello bash` after building the container.

With our Dockerfile finished, we go ahead and start our `build` process. The `docker build -t hello .` command reads all the configuration we added to our Dockerfile and creates a **docker image** from it. That's right, just like the `python:3` image we've been using for this entire article. The `.` at the end tells Docker that we want to run a Dockerfile at our current location, and the `-t hello` option gives this image the name `hello`, so we can easily reference it at runtime.

After all of that, all we need to do is run the usual `docker run` instruction, but this time with the `hello` image name at the end of the line. That will start a container from the image we recently built and finally print the good ol' "Hello, World!" in our terminal.

#### Extending our base image

What do we do if we need some dependency to run our code that does not come pre-installed with our base image? To solve that problem, docker has the `RUN` [instruction](https://docs.docker.com/engine/reference/builder/#run).

Following our python example, if we needed the `numpy` library to run our code, we could add the `RUN` instruction right after our `FROM` command.

```
# Dockerfile
```

```
FROM python:3
```

```
# NEW LINERUN pip3 install numpy
```

```
WORKDIR /src/app
```

```
COPY . .
```

```
CMD [ "python", "./hello.py" ]
```

The `RUN` instruction basically gives a command to be executed by the container's terminal. That way, since our base image already comes with `pip3` installed, we can use `pip3 install numpy`.

> **Note:** For a real python app, you would probably add all the dependencies you need to a `requirements.txt` file, copy it over to the container, and then update the `RUN` instruction to `RUN pip3 install -r requirements.txt`.

### Part 4. "Hello, World!" from a Nginx image using a long-lived detached container

I know you are probably tired of hearing me say it, but I have one more "Hello" to say before I go. Let's go ahead and use our newly acquired docker power to create a simple long-lived container, instead of these short-lived ones we've been using so far.

Create an `index.html` file in a new folder with the following content.

```
# index.html
```

```
<h1>Hello, World!</h1>
```

Now, let's create a new Dockerfile in the same folder.

```
# Dockerfile
```

```
FROM nginx:alpine
```

```
WORKDIR /usr/share/nginx/html
```

```
COPY . .
```

Build the image and give it the name `simple_nginx`, like we previously did.

```
docker build -t simple_nginx .
```

Lastly, let's run our newly created image with the following command:

```
docker run --rm -d -p 8080:80 simple_nginx
```

You might be thinking that nothing happened because you are back to your terminal, but let's take a closer look with the `docker ps` command.

![Image](https://cdn-media-1.freecodecamp.org/images/dc8GKlsLJ6mKsn7r-6Z6LQQIlKoy9kjUhvxO)
_I had to crop the output, but you’ll see a few other columns there_

The `docker ps` command shows all the running containers in your machine. As you can see in the image above, I have a container named `simple_nginx` running in my machine right now. Let's open up a web browser and see if `nginx` is doing its job by accessing `localhost:8080`.

![Image](https://cdn-media-1.freecodecamp.org/images/BuDs3TFSrsnUeN3VggrmWNi3GjKTdL5WnQTx)
_Hurray! (this is the last time, I promise)_

Everything seems to be working as expected, and we are serving a static page through the `nginx` running inside our container. Let's take a moment to understand how we accomplished that.

#### Breaking it down

I'm going to skip the Dockerfile explanation because we already learned those commands in the last section. The only "new" thing in that configuration is the `nginx:alpine` image, which you can read more about it [here](https://hub.docker.com/_/nginx).

Apart from what is new, this configuration works because `nginx` uses the `usr/share/nginx/html` folder to search for an `index.html` file and start serving it, so since we named our file `index.html` and configured the `WORKDIR` to be `usr/share/nginx/html`, this setup will work right out of the box.

The `build` command is exactly like the one we used in the last section as well, we are only using the Dockerfile configuration to build an image with a certain name.

Now for the fun part, the `docker run --rm -d -p 8080:80 simple_nginx` instruction. Here we have two new flags. The first one is the detached (`-d`) flag, which means that we want to run this container in the background, and that's why we are back at our terminal right after using the `docker run` command, even though our container is still running.

The second new flag is the `-p 8080:80` option. As you might have guessed, this is the `port` flag, and it's basically mapping the port `8080` from our local machine to the port `80` inside our container. You could have used any other port instead of `8080`, but you cannot change the port `80` without adding an additional setting to the `nginx` image, since `80` is the standard port the `nginx` image exposes.

> **Note:** If you want to stop a detached container like this one, you can use the `docker ps` command to get the **container's name** (not image), and then use the `docker stop` instruction with the desired container's name at the end of the line.

### Part 5. The end

That's it! If you are still reading this, you have all the basics to start using Docker today on your personal projects or daily work.

Let me know what you thought about this article in the comments, and I'll make sure to write a follow-up article covering more advanced topics like `docker-compose` somewhere in the near future.

If you have any questions, please let me know.

Cheers!

