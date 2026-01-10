---
title: 'How to set up Docker and Windows Subsystem for Linux: A Love Story. ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T17:13:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-docker-and-windows-subsystem-for-linux-a-love-story-35c856968991
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nKPs7NaTWQnJpNSU
tags:
- name: Docker
  slug: docker
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Piotr Gaczkowski

  Do you sometimes feel you’re a beautiful princess turned by an evil wizard into
  a frog? Like you don’t belong? I do. I’m a UNIX guy scared to leave the cozy command
  line. My terminal is my castle. But there are times when I’m forc...'
---

By Piotr Gaczkowski

Do you sometimes feel you’re a beautiful princess turned by an evil wizard into a frog? Like you don’t belong? I do. I’m a UNIX guy scared to leave the cozy command line. My terminal is my castle. But there are times when I’m forced to use Microsoft Windows and I have learned a few tricks on how to cope with that.

For my daily terminal needs, I have installed Windows Subsystem for Linux along with the Ubuntu distribution. On top of that, I have a Linuxbrew installation which helps me manage any third-party apps I may need. This combination works surprisingly well! I have a nifty symbolic link to access all my “external” (that is Windows-hosted) data: `ln -s ~/external /mnt/c/Users/DoomHammer` and most of the needs are fulfilled this way. That is, unless I need to use Docker.

### What’s so Special About Docker?

Unlike most applications I typically use every day, Docker is a system application. This means its rooted deep into the system and requires an actual daemon to run on the host machine. And by the host machine, I mean native Microsoft Windows in that case.

Does it mean you can’t use Docker from inside WSL? Not necessarily. But you need to flex your muscles a bit more to get there. First of all, you need to install Docker for Windows. There’s Docker Enterprise Editions for Windows Server 2016 (and up) and there’s Community Edition for Windows 10 Professional or Enterprise. And I was stuck at Windows 10 Home Edition.

### Getting Docker on Windows 10 Home

It seems getting Docker to run on Windows 10 Home Edition is a bit more tricky. Docker Community Edition requires Hyper-V support which is unavailable on Home Edition. This means I needed to dig out [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/), an older distribution which relied on Docker Machine and Virtualbox. But after installation, Virtualbox greeted me with a prompt saying it’s impossible to run virtualization.

As it turned out, I had the virtualization setting turned off in BIOS. Apparently for security reasons. I turned it on, opened Virtualbox again and… the same. This made me worried a bit. After a bit of Web crawling, I found the advice to check `systeminfo`. Well, it clearly showed *some* hypervisor is running. But not Virtualbox and most certainly not Hyper-V, right?

To my surprise, it was Hyper-V all along. It seems Home Edition lacks the userland tools to actually **use** Hyper-V but it doesn’t mean that the Hypervisor itself wasn’t running. Thankfully, turning it off was just a `bcdedit /set hypervisorlaunchtype off` away. After I rebooted the machine Virtualbox was eager to work. Cool, score for me!

### Docker and WSL, Best Friends Forever?

Having a working Virtualbox I opened Docker Quickstart Terminal. On the first run, it creates a Docker Machine (that’s why it needs Virtualbox) to act as a host for all the containers. I typed `docker run --rm hello-world` and watched the progress bar as Docker downloaded the appropriate image for me. Another score!

Now, instead of the `cmd.exe` I’d like to use Docker from the comfort of my WSL. How do I do that? Fortunately, WSL has access to native Windows binaries. This means I can run `docker-machine.exe ls` to see the machine created by Docker Toolbox. It should be right there named simply `default`. If the state is anything else than “Running” you can start it with `docker-machine.exe start`. Each time you want to run Docher Machine remember that unlike in `cmd.exe` the extension (`.exe`) is mandatory.

Normally we would call `docker-machine.exe env` to set the environment variables.

Unfortunately it outputs the variables in a format understood by `cmd.exe`, not by any Bourne-compatible shell like bash or zsh. But we can change this behavior with `docker-machine.exe env --shell sh`.

Hmm, almost there. But there’s one thing left hanging. The certificate path is written as a Windows path. How to translate into something WSL understands? [For some time now](https://github.com/MicrosoftDocs/WSL/releases/tag/17046), WSL features a nice utility called `wslpath`. Thanks to this tool we can call `export DOCKER_CERT_PATH=$(wslpath $DOCKER_CERT_PATH)` and we're **almost** ready.

We still need the userland tools. So, using your favorite package manager install both the Docker Engine and Docker Compose. For me this means `brew install docker docker-compose`. After that a `docker run --rm hello-world` should yield exactly the same results as it did in a Docker Toolbox terminal. Congratulations!

### Is That All?

No, of course not. You may quickly notice that bind-mount does not work correctly. That’s because the Docker daemon expects proper Windows paths, and WSL paths sadly cannot be translated automatically. But there are a few hacks we can use to improve the situation.

Now, which hack you need depends of the version you are running. Hitting Win+R and typing `winver` you should see a dialog that says something around the lines:

> Microsoft Windows  
> Version 18.03 (OS Build 17133.73)

If it’s actually 18.03 or newer you can edit `/etc/wsl.conf` to look like this:

```
[automount]
root = /
options = "metadata"
```

It means WSL would mount the C: drive under `/c/` instead of the usual `/mnt/c`. Why is this important? Well, it’s important because that’s what Docker daemon expects of Windows paths. By the way: after you save the file, you need to re-login for the changes to take effect.

**Warning**! If you happen to use [wsl-terminal](https://github.com/goreliu/wsl-terminal) this change will break it. Use the next method in such a case.

Another approach if you don’t want to re-login or if you’re stuck with an older version is to bind mount one mountpoint to the other like this:

```
sudo mkdir /c
sudo mount --bind /mnt/c /c
```

Quicker, but only available as long as you are logged in. You’ll have to repeat this the next time you reboot your machine or add it to your shell runtime configuration (like `~/.bashrc` or `~/.zshrc`). That’s because `/etc/fstab` does not work as expected on WSL.

As you may have noticed, this means you are now able to run Docker with mounts, but only if your volumes are within the Windows filesystem. Since command line `docker` expects absolute paths this should be no big deal, but with Docker Compose you have to be extra careful. It allows to use relative paths and this way everything that starts with `./` won’t work.

If you absolutely insist on mounting WSL’s filesystem with Docker you can try replacing all those `./` with `/c/Users/$USERNAME/AppData/Local/lxss` along with the project’s `$PWD`. In this case `$USERNAME` does not mean your WSL username, but you Windows one.

I thought it’d be clever to write a wrapper around Docker Compose to make it change the working directory into this `lxss` but unfortunately WSL has no rights to access it. And rightfully so, I think!

### One Last Wall

We can run Docker and we can bind data directories. What else can we want? Maybe working port-forwarding? Unlike with Native solutions, using Docker through Docker Machine requires to call every service on `$(docker-machine ip):$PORT` instead of the usual `localhost:$PORT`. There is a way around it, albeit not a very elegant one:

```sh
#!/bin/sh

# This script uses Virtualbox Port Forwarding to make all Docker services
# available on Windows host under `localhost`

VBXMGMT=/c/Program\ Files/Oracle/VirtualBox/VBoxManage.exe

# List all the running container ids
docker ps -q | while read -r i; do
  # List all the ports bound by this container<Paste>
  for port in $(docker port "$i" | cut -d'-' -f1); do
    port_num=$(echo "${port}" | cut -d'/' -f1)
    port_type=$(echo "${port}" | cut -d'/' -f2)
    echo "Create rule natpf1 for ${port_type} port ${port_num}"
    "$VBXMGMT" controlvm "default" natpf1 "${port_type}-port${port_num},${port_type},,${port_num},,${port_num}"
  done
done
```

I believe you can write a wrapper around Docker to perform this dance each time you run a new container. I admit I haven’t tested it that way, as most of the time I’m satisfied with forwarding a single port.

I hope this will make your work with Docker on WSL much more pleasant. It certainly did this for me!

### Bibliography

I wouldn’t have written this article if it wasn’t for the fine people who shared their knowledge. Every time I stumbled over some obstacle I could search for the existing solutions. Below, a list of articles and posts that helped me write this guide:

[**Setting Up Docker for Windows and WSL to Work Flawlessly**](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)  
[_With a couple of tweaks the WSL (Windows Subsystem for Linux, also known as Bash for Windows) can be used with Docker…_nickjanetakis.com](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)[**How to access linux/Ubuntu files from Windows 10 WSL?**](https://superuser.com/a/1110976)  
[_Super User is a question and answer site for computer enthusiasts and power users. Join them; it only takes a minute…_superuser.com](https://superuser.com/a/1110976)[**Port forwarding in docker-machine?**](https://stackoverflow.com/questions/32174560/port-forwarding-in-docker-machine)  
[_You can still access the VBoxmanage.exe command from the VirtualBox used by docker machine: VBoxManage controlvm…_stackoverflow.com](https://stackoverflow.com/questions/32174560/port-forwarding-in-docker-machine)

