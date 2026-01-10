---
title: Cleaning up Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T17:31:37.000Z'
originalURL: https://freecodecamp.org/news/cleaning-up-docker
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_C6BkVKRpoVK_Pq1TLqlSkQ-3.png
tags:
- name: command line
  slug: command-line
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Faizan Bashir

  With the passage of time running Docker in development, we tend to accumulate a
  lot of unused images. Sometimes for testing, research or just trying out fun new
  stuff. It''s always cool to run new software in containers, lights up new...'
---

By Faizan Bashir

With the passage of time running Docker in development, we tend to accumulate a lot of unused images. Sometimes for testing, research or just trying out fun new stuff. It's always cool to run new software in containers, lights up new possibilities for those of us interested in constantly learning new technologies. Downside is a lot of precious SSD memory occupied with rarely used or unused images, the worse thing is we hardly notice. But the guys at Docker Inc. have done a great task by keeping a track of all things Docker.

Say hello to the `system` command, part of the docker management commands and simply awesomeness. The `system` command provides info from disk usage to system-wide information, ain’t that cool.

### **Disk usage using** `**df**` **command:**

```
$ docker system df
```

Returns something like this,

```
TYPE              TOTAL     ACTIVE     SIZE         RECLAIMABLE
Images            35        6          8.332GB      7.364GB (88%)
Containers        12        12         417.6MB      0B (0%)
Local Volumes     67        2          2.828GB      2.828GB (100%)
Build Cache                            0B           0B
```

Notice the `Reclaimable` this is the size you can recover, it is calculated by subtracting the size of active images from the size of total images.

---

**Real time events using** `**events**` **command:**

```
$ docker system events
```

Returns the list of real time events from the server, based on Docker object types.

Formatting output

```
--format 'Type={{.Type}}  Status={{.Status}}  ID={{.ID}}'
```

or simply format the output as JSON

```
$ docker system events --format '{{json .}}'
```

---

**System-wide info using** `**info**` **command:**

Another cool command to get all the system related information is the `info` command. You will be amazed to see the amount of info you can get.

```
$ docker system info
```

---

**Remove unused data using** `**prune**` **command:**

Now that we have all the info we need, its cleanup time, but beware against using this command half asleep.

```
$ docker system prune
WARNING! This will remove:        
	- all stopped containers        
        - all networks not used by at least one container        
        - all dangling images        
        - all build cache
Are you sure you want to continue? [y/N]
```

Further we can remove exactly what we want, using any of the following commands, feast you eyes ladies and gents.

```
$ docker system prune -a --volumes
$ docker image prune
$ docker container prune
$ docker volume prune
$ docker network prune
```

All of the above commands will prompt for confirmation, so wash your face with cold water or take a shot of Espresso before issuing any of these ;).

