---
title: Docker Data Containers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T18:05:19.000Z'
originalURL: https://freecodecamp.org/news/docker-data-containers
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_AUiK5PwnsPG_xaT9jcVoSA-2.jpeg
tags:
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
seo_title: null
seo_desc: 'By Faizan Bashir

  There is more than one way to manage data in Docker container. Say hello to the
  Data Containers.

  Simply put data containers are containers whose job is just to store/manage data.

  Similar to other containers they are managed by the ho...'
---

By Faizan Bashir

There is more than one way to manage data in Docker container. Say hello to the Data Containers.

Simply put data containers are containers whose job is just to store/manage data.

Similar to other containers they are managed by the host system. However, they don’t show up when you perform a `docker ps` command.

To create a Data Container we first create a container with a well-known name for future reference. We use _busybox_ as the base as it’s small and lightweight in case we want to explore and move the container to another host.

When creating the container, we also provide a volume `-v` option to define where other containers will be reading/writing data.

```
$ docker create -v /config --name dataContainer busybox
```

With the container in place, we can now copy files from our local client directory into the container.

To copy files into a container you use the command `docker cp`. The following command will copy the _config.conf_ file into the _config_ directory of _dataContainer_.

```
$ docker cp config.conf dataContainer:/config/
```

Now our Data Container has our config, we can reference the container when we launch dependent containers requiring the configuration file.

Using the magical `--volumes-from <container>` option we can use the mount volumes from other containers inside the container being launched. In this case, we’ll launch an Ubuntu container which has reference to our Data Container. When we list the config directory, it will show the files from the attached container.

```
$ docker run --volumes-from dataContainer ubuntu ls/config
```

If a _/config_ directory already existed then, the volumes-from would override and be the directory used. You can map multiple volumes to a container.

---

### **Import and Export Container data**

Data can be imported and exported from a container, using the `docker export` command.

We can move the Data Container to another machine simply by exporting it to a .tar file.

```
$ docker export dataContainer > dataContainer.tar
```

Likewise we can import the Data Container back into Docker.

```
$ docker import dataContainer.tar
```


