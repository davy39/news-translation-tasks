---
title: How to SSH into a Docker Container – Secure Shell vs Docker Attach
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-24T19:47:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-ssh-into-a-docker-container-secure-shell-vs-docker-attach
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/ssh-into-docker-container-image-1.png
tags:
- name: Docker
  slug: docker
- name: ssh
  slug: ssh
seo_title: null
seo_desc: "By Sebastian Sigl\nContainers are the bread and butter for running applications\
  \ today. And the most popular container technology is called Docker. \nKnowing how\
  \ to SSH into a container is essential to using, debugging, and operating containers\
  \ on your ..."
---

By Sebastian Sigl

Containers are the bread and butter for running applications today. And the most popular container technology is called [Docker](https://www.docker.com/). 

Knowing how to SSH into a container is essential to using, debugging, and operating containers on your local operating system or remote setup. 

This article will describe different methods for doing so along with their constraints.

## Method 1 – Attach to a Running Container using `docker exec`

The most common and helpful command for getting a shell in a container is `docker exec -it`. It runs a new command in the container, which allows you to start a new interactive shell:

```sh
# start a container
$ docker run --name nginx --rm -p 8080:80  -d nginx

# create and connect to a bash shell in the container
$ docker exec -it nginx bash

root@a84ad71521b1:/#
```

You can exit the current shell by pressing `control + d` or typing `exit`.

It works because:

* `docker exec` runs a new command,
* `-i` adds a stdin stream,
* `-t` adds a terminal driver,
* `-it` combines `-i` and `-t`, which allows you to interact with the process.

‌‌It can happen that your container does not have bash installed. In case you can not start bash, you can try starting a `sh`-shell:

```sh
docker exec -it nginx sh
```

‌‌Also, there might not be a shell installed in the container. Therefore, there is no way to get a shell in that container in a plain docker Universum and you can not start any shell.‌‌

Depending on your container orchestration tool, you might still be able to access the container. For example, [distroless containers](https://github.com/GoogleContainerTools/distroless) are getting more popular to reduce the footprint of the container. If you use Kubernetes, an [ephemeral container](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) feature allows you to debug containers without a shell as well as crashed containers.

## Method 2 – Attach to a Running Container using `docker attach`

> The `docker attach` command attaches your terminal’s standard input, output, and error to a running container using the container’s id or name. (Source [docker.com](https://docs.docker.com/engine/reference/commandline/attach/))

In practice, this means everything you enter gets forwarded to the container, and everything that is printed will be shown in your console.

Now, you attach to the running container:

```sh
$ docker attach nginx                              

172.17.0.1 - - [18/Mar/2022:08:37:14 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36" "-"

```

While running this, you can open [http://localhost:8080](http://localhost:8080). Because the container prints access logs on each page opened, you will see the output in your terminal.

Additionally, input is forwarded as well to the container. So if you press `control + c`, which triggers a kill signal, your container will shut down.

```sh
$ docker attach nginx                              
172.17.0.1 - - [18/Mar/2022:08:37:14 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36" "-"
^[[A^C2022/03/18 08:39:50 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/03/18 08:39:50 [notice] 32#32: exiting

```

Detaching can be tricky because `control + c` is also used for detaching. To be able to detach without stopping the container, you can attach to the container by disabling forwarding signals:

```sh
# start the container again
docker run --name nginx --rm -p 8080:80  -d nginx

# attach with proxying signals
docker attach --sig-proxy=false nginx
```

## Conclusion

To connect to a container using plain docker commands, you can use `docker exec` and `docker attach`.

`docker exec` is a lot more popular because you can run a new command that allows you to spawn a new shell. You can check processes, files and operate like in your local environment.

`docker attach` is more restricted because it attaches your terminal’s standard input, output, and error to the main process of a running container.

I hope you enjoyed the article.

If you liked it and felt the need to give me a round of applause or just want to get in touch, [follow me on Twitter](https://twitter.com/sesigl).

I work at eBay Kleinanzeigen, one of the world’s biggest classified companies. By the way, [we are hiring](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen)!

### References

* [How to SSH into a Running Docker Container and Run Commands](https://phoenixnap.com/kb/how-to-ssh-into-docker-container)
* [How to Detach From a Docker Container Without Stopping It](https://www.cloudsavvyit.com/14226/how-to-detach-from-a-docker-container-without-stopping-it/#:~:text=Docker%20supports%20a%20keyboard%20combination,alive%2C%20keeping%20your%20container%20running.)
* [Docker attach documentation](https://docs.docker.com/engine/reference/commandline/attach/)
* [Docker exec documentation](https://docs.docker.com/engine/reference/commandline/exec/)

