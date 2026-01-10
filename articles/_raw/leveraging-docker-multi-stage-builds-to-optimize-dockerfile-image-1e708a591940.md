---
title: How to leverage Docker multi-stage builds to optimize your dockerfiles and
  images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T09:49:14.000Z'
originalURL: https://freecodecamp.org/news/leveraging-docker-multi-stage-builds-to-optimize-dockerfile-image-1e708a591940
coverImage: https://cdn-media-1.freecodecamp.org/images/0*htBXuMZ5x0KT1gwv
tags:
- name: best practices
  slug: best-practices
- name: Docker
  slug: docker
- name: optimization
  slug: optimization
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kumar Rishav

  Multi-stage builds are a new feature requiring Docker 17.05 or higher on the daemon
  and client. They’re useful in building complex/multi step images while keeping them
  easy to read and maintain.

  Keeping the image size down is one of t...'
---

By Kumar Rishav

Multi-stage builds are a new feature requiring Docker 17.05 or higher on the daemon and client. They’re useful in building complex/multi step images while keeping them easy to read and maintain.

Keeping the image size down is one of the challenging tasks while building the image. Each instruction in the Dockerfile adds a layer to the image. Also, you need to remember to clean up any dependencies/artifactories you don’t need later. Before, you might have used shell scripts to keep layers light as much as possible. But using shell tricks to write a really efficient Dockerfile is a painful task.

### What exactly are Multi-Stage Builds?

In simple terms: you can use the end result (for ex: binary/executable file) of one stage into another stage without worrying about dependencies used to build that binary/executable file.

### How does it work?

With Multi-stage builds, you can have multiple `FROM` statement in a single Dockerfile. Each `FROM` statement contributes to one stage. The first stage starts from the number `0`.

```
FROM mhart/alpine-node:10  #stage 0
```

```
.......
```

```
FROM alpine:3.7 #stage 1
```

Here, the order of stages matters as the first stage will always be `0`. Another way is to give a name to the `stage` by using `AS`. In that case you don't have to worry about order.

```
FROM mhart/alpine-node:10 AS nodebuilder
```

```
.......
```

```
FROM alpine:3.7 AS builder
```

### Demonstrating Multi-Stage Builds

Tested Infrastructure: [Play with Docker](https://labs.play-with-docker.com)

For demonstration purposes, let us consider a simple nodejs app and build a binary out of it. When you execute this binary, it will call a [NASA api](https://api.nasa.gov/api.html) which returns some interesting facts about today’s date.

#### Before: docker images

![Image](https://cdn-media-1.freecodecamp.org/images/y9julNFQgoTabMcNhHLskgKl3tqEB7DAZW5w)
_before:docker_images_

Currently we have two images which I pulled from [dockerhub](https://hub.docker.com/):

* `alpine (**~4Mb**)` - Lightest version of linux os
* `alpine-node (**~70Mb**)` - alpine + Node/Npm and other dependencies.

#### File structure

![Image](https://cdn-media-1.freecodecamp.org/images/V18qYpT2DGm6u5DqAqib6rbSEddTVX02k7KP)

`**Dockerfile**`**:**

* **On stage 0** (alias: `builder`), we have a `alpine-node` OS which has `node` and `npm` built in it. Its size is `**~70Mb**`. This stage will create a binary (named `nasa` : _Line 6_) in the current `WORKDIR` i.e `app/`.
* **On stage 1**, we have `alpine` OS. After that, we install some necessary dependencies. In `Line 14`, we copied `nasa` binary from the previous stage (`builder`) to the current stage. So, we just copied the binary and leave all heavy `alpine-node` OS and other dependencies like `npm` ([node package manager](https://www.npmjs.com/)) etc behind, as the binary already has the required dependencies (like nodejs) built into it.

`**app/**` **:**

* It's just a simple node application. It does a `https` call and fetches data using the NASA api. It has `index.js` and `package.json`. I have used `[pkg](https://www.npmjs.com/package/pkg)` to build the node binary. Here is the app’s [code](https://gist.github.com/kumarrishav/36596fc94fe282d9e8dc26707fbdb7df).

#### After: docker images

![Image](https://cdn-media-1.freecodecamp.org/images/d0rZnHfp2mOtWo8w8biOGMozjv9OGIOtSPPG)
_after: docker images_

**multistage:1.0.0** (`56b102754f6d`) is the final required image which we built. Its size is `**~45Mb**`. **Almost 1/4th** of the intermediate image (`13bac50ebc1a`) built on stage 0 and **almost half** of the `alpine-node` image.

So, this was a simple example to showcase the multi-stage builds feature. For images having multiple steps (like 10–15 FROM statement), you will find this feature very useful.

#### Use an external image as a “stage”

When using multi-stage builds, you are not limited to copying from stages you created earlier in your Dockerfile. You can use the `COPY --from` instruction to copy from a separate image, either using the local image name, a tag available locally or on a Docker registry, or a tag ID.

`COPY --from=sampleapp:latest home/user/app/config.json app/config.json`

**Thank you.**

_Thanks [Ajeet](https://twitter.com/ajeetsraina) for reviewing the blog._

_Originally posted at [collabnix](http://collabnix.com/): [https://lnkd.in/fJaC6gp](https://lnkd.in/fJaC6gp)._

