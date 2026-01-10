---
title: The easy way to set up Docker on a Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-28T16:25:05.000Z'
originalURL: https://freecodecamp.org/news/the-easy-way-to-set-up-docker-on-a-raspberry-pi-7d24ced073ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SlD_OCnoe1dvKRij1whLIw.png
tags:
- name: Docker
  slug: docker
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ryan Gordon

  Docker is a very useful tool for running containerized versions of popular applications
  (such as databases) or setting up some IoT service on an internet-connected device.

  But installing Docker can sometimes be a hassle if it needs to ...'
---

By Ryan Gordon

Docker is a very useful tool for running containerized versions of popular applications (such as databases) or setting up some IoT service on an internet-connected device.

But installing Docker can sometimes be a hassle if it needs to be done a number of times across different computers. The silver lining, however, is that there is a handy trick hidden away in the Docker docs detailing how to install Docker with just two lines in the terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/furVV9L-htV7JcYivVuH9OFp17YIHkfqzKeX)

Yes, you heard right! With just two lines you can load and install Docker.

Installing Docker can be handled by a bash script which will automate the entire installation. Docker provides such a script at `get.docker.com` . The first command will be consuming this URL, looking for a file called `get-docker.sh` . Once gotten, we just run the script. The two commands can be chained together to form a statement like:

```
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

Now you have Docker installed, and the installation only took two lines.

As you just saw, the two commands above are chained together using the ‘&&’ operator. This means that the commands will run one after the other, but can be typed on the same line.

One small issue, though, is that you might experience difficulty running Docker commands without sudo. This can be fixed, but it’ll take a few more lines.

### How to set up Docker to run without using sudo all the time

I discovered this solution on [AskUbuntu](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo) after encountering the problem. Let’s go through it now.

#### There are 3 steps:

1. Add the Docker group if it doesn’t already exist:

```
sudo groupadd docker
```

2. Add the connected user “$USER” to the docker group. Change the user name to match your preferred user if you do not want to use your current user:

```
sudo gpasswd -a $USER docker
```

3. From here you have two options: either logout and then log back in, or run `newgrp docker` for the changes to take effect.

You should now be able to run Docker without sudo. To test, try this:

```
docker run hello-world
```

If it worked, you should see a lovely message from Docker:

![Image](https://cdn-media-1.freecodecamp.org/images/TAfV1RgUTurTJwxhQcKjGkMoNF6xbN7hxuek)

Again, all credit for this solution goes to this great [AskUbuntu](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo) answer I found. Without typing sudo all the time, commands will be much easier to work with.

### But wait, there’s more!

What if you want docker-compose also? You could try and install the docker-compose source similarly to how we installed Docker. One interesting approach I found on the Google Cloud Engines docs is that you can actually run docker-compose as a container itself!

Doing so means you have a disposable installation of docker-compose which will be used to compose your services. At any point, you can throw it away and repeat the steps for a fresh docker-compose.

First step will be running docker-compose as a container and giving it access to volumes.

```
docker run \    -v /var/run/docker.sock:/var/run/docker.sock \    -v "$PWD:/rootfs/$PWD" \    -w="/rootfs/$PWD" \    docker/compose:1.13.0 up
```

Next, make an alias to docker compose:

```
echo alias docker-compose="'"'docker run \    -v /var/run/docker.sock:/var/run/docker.sock \    -v "$PWD:/rootfs/$PWD" \    -w="/rootfs/$PWD" \    docker/compose:1.13.0'"'" >> ~/.bashrc
```

Then reload bash:

```
source ~/.bashrc
```

Now you have full access to docker-compose. The alias defined above means that rather than having to type out docker commands when you want to use the compose container, you can just use ‘docker-compose’ as you normally would.

### Important Notice about Docker on RPi

Raspberry Pi’s use ARM archetecture, and as a result wont be compatible with all containers out of the box. Images will need to be built from an ARM base image.

You can see this in action by running a containerized Redis instance on a Raspberry Pi (which is quite relevant to an upcoming series I’m writing). Doing so will require working with a base image. Provided we use an ARM-compatible image, no problems should arise. The issue is finding a well-maintained one.

If you enjoyed this article, give it a clap.

I have other posts on my page related to Microservices, Ionic, and more.

