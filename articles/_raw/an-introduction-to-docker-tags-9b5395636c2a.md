---
title: A quick introduction to Docker tags
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T18:22:09.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-docker-tags-9b5395636c2a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*KBn45TeUMJZSbz9n.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shubheksha Jalan

  If you’ve worked with Docker even for a little while, I bet you’ve come across tags.
  They often look like “my_image_name:1” where the part after the colon is known as
  a tag. The tag is not always specified when tagging images, but...'
---

By Shubheksha Jalan

If you’ve worked with Docker even for a little while, I bet you’ve come across tags. They often look like “my_image_name:1” where the part after the colon is known as a tag. The tag is not always specified when tagging images, but we’ll get to the bottom of that later.

Ever since I started using Docker, I’ve been very confused about tags. The documentation doesn’t explain them very well, and there really aren’t any thorough explanations on the topic. That’s why I decided to write this post.

### What are Docker tags?

So, what exactly are Docker tags? In simple words, Docker tags convey useful information about a specific image version/variant. They are aliases to the ID of your image which often look like this: `f1477ec11d12`. It’s just a way of referring to your image. A good analogy is how Git tags refer to a particular commit in your history.

The two most common cases where tags come into play are:

1. When building an image, we use the following command:

```
docker build -t username/image_name:tag_name .
```

Let’s try to unpack what this command does for a bit. We tell the Docker daemon to fetch the Docker file present in the current directory (that’s what the `.` at the end does). Next, we tell the Docker daemon to build the image and give it the specified tag. If you run `docker images`, you should see an image whose repository is `username/image_name` and tag is `tag_name`.

`username/image_name` is not a mandatory format for specifying the name of the image. It’s just a useful convention to avoid tagging your image again when you need to push it to a registry.

Your image can be named anything you want. For the public Docker registry, you’re restricted to a two level hierarchy while naming images. For example, your image cannot have the name `a/b/c:1.` This restriction usually doesn’t exist in private registries. As stated before, it’s not mandatory to specify a `tag_name.` We’ll see what happens in that case soon.

2. Explicitly tagging an image through the `tag` command.

```
docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
```

This command just creates an alias (a reference) by the name of the `TARGET_IMAGE` that refers to the `SOURCE_IMAGE.` That’s all it does. It’s like assigning an existing image another name to refer to it. Notice how the tag is specified as optional here as well, by the `[:TAG]` .

### What happens when you don’t specify a tag?

Alright, now let’s uncover what happens when you don’t specify a tag while tagging an image. This is where the `latest` tag comes into the picture. Whenever an image is tagged without an explicit tag, it’s given the `latest` tag by default. It’s an unfortunate naming choice that causes a lot of confusion. But I like to think of it as the **default tag** that’s given to images when you don’t specify one.

A lot of confusion around `latest` is caused due to the expectation that it’s the latest version of the image, especially in Dockerfiles. Let’s consider the various scenarios with an example:

#### Scenario 1:

Suppose the following statement is present in our Dockerfile:

```
FROM debian
```

Since we didn’t specify any tag, Docker will add the `latest` tag and try to pull the image `debian:latest` .

#### Scenario 2:

```
FROM debian:9.3
```

Since the tag is explicitly mentioned here, Docker will pull the Debian image tagged 9.3

Another thing to keep in mind is that there is no rule which states that an image needs to have just one tag. An image can have multiple tags and they’re usually used to specify major and minor versions. For example, consider this:

![Image](https://cdn-media-1.freecodecamp.org/images/bOvBoIYQodn8oPnc9D39cLmXRwp4i-vcgIUc)
_[Docker Hub page for Debian](https://hub.docker.com/r/library/debian/" rel="noopener" target="_blank" title=")_

At the time of writing this post, the `latest` tag for the Debian image points to the `9.3` release **and** the `9` release. This will most likely change in the future whenever the major or minor version is bumped for the image.

Please note that tags being used for semantic versioning is a convention that’s followed, but tags weren’t designed _just_ for that purpose.

### In conclusion, latest is not a special tag

The main takeaway from what we’ve covered so far is that **latest is just like any other tag**. The onus is on the developer to tag the images properly such that `latest` always points to the latest stable release of the image.

Hence, we don’t explicitly specify a tag in our Dockerfiles when pulling images, since we might end up with a completely different version of the base image than what we had used before. There is no guarantees about whether it’ll be a major bump or minor bump. Even an old release can be tagged as `latest`.

P.S. If you found any misconceptions/errors in the post, please feel free to tweet to me [@ScribbingOn](https://twitter.com/ScribblingOn).

Thanks to [Jérôme Petazzoni](https://twitter.com/jpetazzo) for helping me make sense of some of this.

