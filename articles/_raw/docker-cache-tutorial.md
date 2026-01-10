---
title: Docker Cache – How to Do a Clean Image Rebuild and Clear Docker's Cache
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-28T18:51:57.000Z'
originalURL: https://freecodecamp.org/news/docker-cache-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/docker-cache-guide.png
tags:
- name: cache
  slug: cache
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: null
seo_desc: "By Sebastian Sigl\nContainers enable you to package your application in\
  \ a portable way that can run in many environments. The most popular container platform\
  \ is Docker. \nThis tutorial will explain how to use the Docker build cache to your\
  \ advantage.\nD..."
---

By Sebastian Sigl

Containers enable you to package your application in a portable way that can run in many environments. The most popular container platform is [Docker](https://www.docker.com/). 

This tutorial will explain how to use the Docker build cache to your advantage.

## Docker Build Cache

Building images should be fast, efficient, and reliable. The concept of Docker images comes with immutable layers. Every command you execute results in a new layer that contains the changes compared to the previous layer. 

All previously built layers are cached and can be reused. But, if your installation depends on external resources, the Docker cache can cause issues.

## How to Leverage the Docker Build Cache

To understand Docker build-cache issues, let’s build a simple custom [nginx](https://nginx.org/en/) Docker application. Before you build the image, create a Dockerfile that updates libraries and adds a custom startpage:

```dockerfile
FROM nginx:1.21.6

# Update all packages
RUN apt-get update && apt-get -y upgrade

# Use a custom startpage
RUN echo '<html><bod>My Custom Startpage</body></html>' > /usr/share/nginx/html/index.html
```

You can now build the Docker image:

```shell
$  docker build -t my-custom-nginx .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e12...  5.8s
=> [2/3] RUN apt-get update && apt-get -y upgrade           3.6s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...        0.2s

=> exporting to image                                       0.1s
=> exporting layers                                         0.1s
=> writing image                                            0.0s
=> naming to docker.io/library/my-custom-nginx

[+] Building 11.3s (7/7) FINISHED
```

In this example, I removed some output for readability. If you build the image the first time, you see that it takes quite some time, in my case `11.3s`. 

One long executing step is `apt-get update && apt-get -y upgrade` depending on how many dependencies are updated and how fast your internet speed is. It checks for package updates on the operation system and installs them if available.

Now, you execute it again, and you benefit from the Docker build cache:

```shell
$ docker build -t my-custom-nginx .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e1211ac1…   0.0s
=> CACHED [2/3] RUN apt-get update && apt-get -y upgrade        0.0s
=> CACHED [3/3] RUN echo '<html><bod>My Custom Startpage...     0.0s

=> exporting to image                                           0.0s
=> exporting layers                                             0.0s
=> writing image                                                0.0s
=> naming to docker.io/library/my-custom-nginx

Building 1.1s (7/7) FINISHED
```

This time, the image build is very fast because it can reuse all previously built images. When you customize your startpage in the Dockerfile, you see how the caching behavior is affected:

```dockerfile
FROM nginx:1.21.6

# Update all packages
RUN apt-get update && apt-get -y upgrade

# Use a custom startpage
RUN echo '<html><bod>New Startpage</body></html>' > /usr/share/nginx/html/index.html
```

Now, build the image again:

```shell
$ docker build -t my-custom-nginx .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e1211ac1…   0.0s
=> CACHED [2/3] RUN apt-get update && apt-get -y upgrade        0.0s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...            0.2s

=> exporting to image                                           0.0s
=> exporting layers                                             0.0s
=> writing image                                                0.0s
=> naming to docker.io/library/my-custom-nginx

Building 2.1s (7/7) FINISHED
```

This time it only rebuilt the last layer because it recognized that the `RUN` command had changed. But, it reused the intense 2nd build step and did not update operation system dependencies.

The caching behavior is intelligent. Once 1 step needs to rebuild, every subsequent step is built again. Therefore, it’s good to put frequently changing parts at the end of a `Dockerfile` to reuse previous build layers.

Still, maybe you want to force a rebuild of a cached layer to force a package update. Forcing a rebuild can be necessary because you want to keep your application safe and use the newest updates when available.

## How to Use the Docker Build `--no-cache` Option

There can be different reasons for disabling the build-cache. You can rebuild the image from the base image without using cached layers by using the `--no-cache` option.

```shell
$ docker build -t my-custom-nginx .

=> CACHED [1/3] FROM docker.io/library/nginx:1.21.6@sha256:...  0.0s
=> [2/3] RUN apt-get update && apt-get -y upgrade               3.5s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...            0.2s

=> exporting to image                                           0.1s
=> exporting layers                                             0.0s
=> writing image                                                0.0s
=> naming to docker.io/library/my-custom-nginx

Building 5.5s (7/7) FINISHED
```

New layers were constructed and used. The `docker build` runs both commands this time, which comes with an all-or-nothing approach. Either you provide the `--no-cache` option that executes all commands, or you will cache as much as possible.

## How to Use Docker Arguments for Cache-Busting

Another option allows providing a little starting point in the Dockerfile. You need to edit your Dockerfile like this:

```dockerfile
FROM nginx:1.21.6

# Update all packages
RUN apt-get update && apt-get -y upgrade

# Custom cache invalidation
ARG CACHEBUST=1

# Use a custom startpage
RUN echo '<html><bod>New Startpage</body></html>' > /usr/share/nginx/html/index.html
```

You add a `CACHEBUST` argument to your Dockerfile at the location you want to enforce a rebuild. Now, you can build the Docker image and provide an always different value that causes all following commands to rerun:

```shell
$ docker build -t my-custom-nginx --build-arg CACHEBUST=$(date +%s) .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e1211ac1...    0.0s
=> CACHED [2/3] RUN apt-get update && apt-get -y upgrade           0.0s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...               0.3s

=> exporting to image                                              0.0s
=> exporting layers                                                0.0s
=> writing image                                                   0.0s
=> naming to docker.io/library/my-custom-nginx

Building 1.0s (7/7) FINISHED
```

By providing `--build-arg CACHEBUST=$(date +%s)`, you set the parameter to an always different value that causes all following layers to rebuild.

## Summary

Docker’s build-cache is a handy feature. It speeds up Docker builds due to reusing previously created layers. 

You can use the  `--no-cache` option to disable caching or use a custom Docker build argument to enforce rebuilding from a certain step.

Understanding the Docker build cache is powerful and will make you more efficient in building your Docker container.

I hope you enjoyed this article.

If you liked it and feel the need to give me a round of applause or just want to get in touch, [follow me on Twitter](https://twitter.com/sesigl).

I work at eBay Kleinanzeigen, one of the world’s biggest classified companies. By the way, [we are hiring](http://ebay-kleinanzeigen.de/careers)!

## References

* [Docker arg instruction](https://www.geeksforgeeks.org/docker-arg-instruction/)
* [Stackoverflow: Disable Cache for specific RUN commands](https://stackoverflow.com/questions/35134713/disable-cache-for-specific-run-commands)
* [Baeldung: How the Docker Build Cache Works and When Not to Use it](https://www.baeldung.com/linux/docker-build-cache)

