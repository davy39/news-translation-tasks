---
title: 'Docker Remove Image: How to Delete Docker Images Explained with Examples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-22T21:45:00.000Z'
originalURL: https://freecodecamp.org/news/docker-remove-image-how-to-delete-docker-images-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/DockerErase3.png
tags:
- name: Docker best practices
  slug: docker-best-practices
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'By Marcelo Costa

  We live in an era where storage is becoming cheaper everyday. We can just send everything
  to the cloud and pay almost nothing.

  So why would we need to worry about deleting Docker images?

  First of all, there are still some mission cri...'
---

By Marcelo Costa

We live in an era where storage is becoming cheaper everyday. We can just send everything to the cloud and pay almost nothing.

So why would we need to worry about deleting Docker images?

First of all, there are still some mission critical workloads that can't be moved to the cloud, especially those in heavily regulated industries like law or healthcare.  
  
But to better answer that question, I would say that we as developers often find ourselves out of space on our local machines.

 Let's do a quick analysis of this [StackOverflow public dataset](https://cloud.google.com/blog/products/gcp/google-bigquery-public-datasets-now-include-stack-overflow-q-a) to explore that further:

```sql
SELECT tag,
       title,
       answer_count,
       favorite_count,
       score,
       view_count VIEWS
FROM
  (SELECT title,
          answer_count,
          favorite_count,
          view_count,
          score,
          SPLIT(tags, '|') tags
   FROM `bigquery-public-data.stackoverflow.posts_questions` 
         posts_questions), UNNEST(tags) tag
WHERE tag = 'docker'
  AND title LIKE '%space left%'
ORDER BY VIEWS DESC
```

**Query Results:**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-21-at-2.11.43-PM.png)

So it does't happen just with me, right? Look at how many views we have on those StackOverflow posts. If you are wondering, the number is **465687** views for posts matching the search query.

Luckily for us, today we are going to see some **easy-to-use** examples on how to delete our dangling and unused docker images to help ourselves out. 

## What are dangling and unused Docker images?

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/07/hanging3.png" alt="drawing" width="300">
</div>

What is the difference between dangling and unused images, you might ask?

A dangling image means that you've created a new build of the image but haven't given it a new name. Think about those old, forgotten images that no one knows what to do with anymore – those are "dangling images". 

They are left untagged and display `<none>` on their name when you run `docker images`.

On the other hand, an unused image means that it has not been assigned or is not being used in a container. 

For example, when running `docker ps -a` – it will list all your currently running containers plus exited containers. Any images being used inside any of containers are shown as "used images", and any others are unused.

## Delete Docker Images

Now let's see some examples of how to delete Docker images.

### Our case study

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/07/busyCat.png" alt="drawing" width="300">
</div>

The Busy Cat Corp is a fictional company that captures cat behavior data, and provides recommendations to cat owners on how to make their pets busier and happier.  
  
All their workloads are containerized, and they use the following database images:  
[cassandra](https://hub.docker.com/_/cassandra), [postgres](https://hub.docker.com/_/postgres), [mysql](https://hub.docker.com/_/mysql) and [mongo](https://hub.docker.com/_/mongo).

Their developers are constantly running out of space on their machines, and they are top users of StackOverflow – aren't we all?  
  
So they asked us for some quick examples of how to delete some images and get their space back.

First let's take a look at the machine of one of their developers.

```bash
docker images
```

**Output**

```bash
REPOSITORY  TAG          IMAGE ID            CREATED              SIZE
<none>       <none>      9c872a6119cc        About a minute ago   384MB
mysql        latest      5ac22cccc3ae        43 hours ago         544MB
cassandra    3           9fab0c92a93d        4 days ago           384MB
adoptopenjdk 8-jre...    2bf0172ac69b        4 days ago           210MB
mongo        latest      6d11486a97a7        2 weeks ago          388MB
postgres     latest      b97bae343e06        6 weeks ago          313MB
```

That's cool, they have all the images from their workloads downloaded. But look at the disk space – it's more than **2GB**! Let's see what we can do for them.

### Delete Docker dangling images

We'll start by looking for dangling images.

```
docker images -qf "dangling=true"
```

**Output**

```bash
REPOSITORY  TAG          IMAGE ID            CREATED              SIZE
<none>       <none>      9c872a6119cc        About a minute ago   384MB
```

We have one, so we are going to clear it up.

**Delete the dangling image**

```
docker rmi $(docker images -qf "dangling=true")

```

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/flamenco-done.png" alt="drawing" width="300">
</div>

### Delete Docker unused images

Next we are looking for unused images.

```
docker ps -a
```

**Output**

```bash
CONTAINER ID  IMAGE   CREATED           NAMES
b6387b343b81  mysql   16 minutes ago    some-mysql
```

We only have one container running the  `mysql`  image, so all the other images are unused. 

So that we don't have to do it manually, we can put together a script that shows all of the unused images to verify them.

```bash
# Get all the images currently in use
USED_IMAGES=($( \
    docker ps -a --format '{{.Image}}' | \
    sort -u | \
    uniq | \
    awk -F ':' '$2{print $1":"$2}!$2{print $1":latest"}' \
))

# Get all the images currently available
ALL_IMAGES=($( \
    docker images --format '{{.Repository}}:{{.Tag}}' | \
    sort -u \
))

# Print the unused images
for i in "${ALL_IMAGES[@]}"; do
    UNUSED=true
    for j in "${USED_IMAGES[@]}"; do
        if [[ "$i" == "$j" ]]; then
            UNUSED=false
        fi
    done
    if [[ "$UNUSED" == true ]]; then
        echo "$i is not being used."
    fi
done
```

**Output**

```bash
adoptopenjdk:8-jre-hotspot-bionic is not being used.
cassandra:3 is not being used.
mongo:latest is not being used.
postgres:latest is not being used.
```

Then it deletes the unused images.

```
# Get all the images currently in use
USED_IMAGES=($( \
    docker ps -a --format '{{.Image}}' | \
    sort -u | \
    uniq | \
    awk -F ':' '$2{print $1":"$2}!$2{print $1":latest"}' \
))

# Get all the images currently available
ALL_IMAGES=($( \
    docker images --format '{{.Repository}}:{{.Tag}}' | \
    sort -u \
))

# Remove the unused images
for i in "${ALL_IMAGES[@]}"; do
    UNUSED=true
    for j in "${USED_IMAGES[@]}"; do
        if [[ "$i" == "$j" ]]; then
            UNUSED=false
        fi
    done
    if [[ "$UNUSED" == true ]]; then
        docker rmi "$i"
    fi
done
```

After deleting both dangling and unused images we can look at what we have left.

```bash
docker images
```

**Output**

```bash
REPOSITORY  TAG          IMAGE ID            CREATED              SIZE
mysql        latest      5ac22cccc3ae        43 hours ago         544MB
```

So we only have the `mysql`  image remaining, that's great!

<div style="margin-right: auto;" markdown="1">
<img src="https://www.freecodecamp.org/news/content/images/2020/06/flamenco-done.png" alt="drawing" width="300">
</div>

### Delete all obsolete Docker images with prune

Those commands sound great, but a second developer said they didn't care about the differences between dangling and unused images. 

All they wanted was to clear obsolete images and get their disk space back.

> Personally this is what I usually do.

So we can just use Docker's prune commands.

```
# First delete all stopped containers
docker container prune

# Then delete both dangling and unused images
docker image prune --all
```

This will delete both unused and dangling images. Or in other words images without at least one container associated with them. 

Note: this is why we needed to first delete the stopped containers in the code above.

## **Wrapping **up****

In this article we saw how to delete Docker Images, and we used a fictional company to explain it with some easy-to-use examples.

It's important to point out that you shouldn't use Docker to keep a history of your old images. For a developer environment that's fine, and you can even automate the image clean up workload if you have to deal with a lot of them. 

But for a production workload, you should be using a Container Registry solution to handle your Docker images. 

There are many Container Registry solutions out there, like Google Cloud Platform with [Artifact Registry](https://cloud.google.com/artifact-registry) and Docker Enterprise with [Docker Trusted Registry](https://docs.mirantis.com/docker-enterprise/v3.0/dockeree-products/dtr.html). And if you are in the open source world, you can just use [Docker Hub](https://hub.docker.com/) :).  
  
Thanks for reading!

* Illustrations from [Icons8](https://icons8.com/)

If you found this helpful, or wish to challenge or extend anything raised here, feel free to contact me on [Twitter](https://twitter.com/mesmacosta) or [Linkedin](https://www.linkedin.com/in/mesmacosta). Let's connect!

