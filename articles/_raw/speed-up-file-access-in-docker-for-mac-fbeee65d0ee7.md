---
title: How to speed up shared file access in Docker for Mac
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-17T21:41:52.000Z'
originalURL: https://freecodecamp.org/news/speed-up-file-access-in-docker-for-mac-fbeee65d0ee7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pH318KUH_V10gogDY13Nog.jpeg
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
seo_desc: 'By Sebastian Sigl

  Docker just released a native MacOS runtime environment to run containers on Macs
  with ease. They fixed many issues, but the bitter truth is they missed something
  important. The read and write access for mounted volumes is terrible....'
---

By Sebastian Sigl

[Docker](https://www.docker.com/) just released a native MacOS runtime environment to run containers on Macs with ease. They fixed many issues, but the bitter truth is they missed something important. The read and write access for mounted volumes is terrible.

### Benchmarks

We can spin up a container and write to a mounted volume by executing the following commands:

1. Start a container
2. Mount the current directory
3. Write random data to a file in this directory

```
docker run --rm -it -v "$(PWD):/pwd" -w /pwd alpine time dd if=/dev/zero of=speedtest bs=1024 count=100000
```

Let’s compare the results of Windows, Cent OS and Mac OS:

### Windows 10

```
100000+0 records in
100000+0 records out
real    0m 0.29s
user    0m 0.03s
sys     0m 0.21s
```

### Cent OS

```
100000+0 records in
100000+0 records out
real    0m 0.21s
user    0m 0.02s
sys     0m 0.14s
```

### Mac OS

```
100000+0 records in
100000+0 records out
real 0m 19.32s
user 0m 0.42s
sys 0m 1.46s
```

So the winner is…. 19 seconds for writing. For reading it is quiet similar. When you develop a big dockerized application then you are in a bad spot. Usually you would work on your source code and expect no slowdowns for building. But the bitter truth is it will take ages.

This [GitHub issue](https://github.com/docker/for-mac/issues/77) tracks the current state. There is a lot of hate so better listen to the “members” instead of reading all the frustrations.

@dsheetz from the Docker for Mac team nailed the issue:

> Perhaps the most important thing to understand is that **shared file system performance is multi-dimensional**. This means that, depending on your workload, you may experience exceptional, adequate, or poor performance with `osxfs`, the file system server in Docker for Mac. File system APIs are very wide (20-40 message types) with many intricate semantics involving on-disk state, in-memory cache state, and concurrent access by multiple processes. Additionally, `osxfs` integrates a mapping between OS X's _FSEvents_ API and Linux's _inotify_ API which is implemented inside of the file system itself complicating matters further (cache behavior in particular).

> At the highest level, there are two dimensions to file system performance: _throughput_ (read/write IO) and _latency_ (roundtrip time). In a traditional file system on a modern SSD, applications can generally expect throughput of a few GB/s. With large sequential IO operations, `osxfs` can achieve throughput of around 250 MB/s which, while not native speed, will not be the bottleneck for most applications which perform acceptably on HDDs.

> _Latency_ is the time it takes for a file system system call to complete. For instance, the time between a thread issuing _write_ in a container and resuming with the number of bytes written. With a classical block-based file system, this latency is typically under 10μs (microseconds). With `osxfs`, latency is presently around 200μs for most operations or 20x slower. For workloads which demand many sequential roundtrips, this results in significant observable slow down. To reduce the latency, we need to shorten the data path from a Linux system call to OS X and back again. This requires tuning _each component_ in the data path in turn -- some of which require significant engineering effort. Even if we achieve a huge latency reduction of 100μs/roundtrip, we will still "only" see a doubling of performance. This is typical of performance engineering, which requires significant effort to analyze slowdowns and develop optimized components.

Many people created workarounds with different approaches. Some of them use nfs, Docker in Docker, Unison 2 way sync or rsync. I tried some solutions but non of them worked for my docker container that contains a big Java monolith. Either they install extra tools like vagrant to reduce the pain. Vagrant uses nfs but this is still slow compared to native write and read performance. Or they are unreliable, hard to setup and hard to maintain.

I made a step back and thought about the root issue again. A very good approach is [docker-sync](https://github.com/EugenMayer/docker-sync). It’s a ruby application with a lot of options. One very mature option is file synchronisation based upon rsync.

### Rsync

Rsync initial release was in 1996 (20 years ago). It’s used for transferring files across computer systems. One important use case is 1-way synchronization.

Sounds good…, right ?

Docker-sync supports rsync for synchronization. In the beginning it worked but a few days later I got some connection issues between my host and my container.

Do you know the feeling when you want to fix something but it feels so far away? You realise you don’t understand what’s happing behind the scenes.

The rsync approach sounds right. It tackles the root of the issue: operating on mounted files right now is damn slow.

I tried other solutions but without real success.

### Build a custom image

So let’s try to get our hands dirty. You start a rsync server in the container and connect to it using rsync. This approach works for many years for other use-cases.

Let’s setup a docker Centos 6 container with an installed and configured rsync service.

1. The Dockerfile

```
FROM centos:6
# install rsync
RUN yum update -y
RUN yum -y install rsync xinetd
# configure rsync
ADD ./rsyncd.conf /root/
RUN sed -i 's/disable[[:space:]]*=[[:space:]]*yes/disable = no/g' /etc/xinetd.d/rsync # enable rsync
RUN cp /root/rsyncd.conf /etc/rsyncd.conf
RUN /etc/rc.d/init.d/xinetd start
RUN chkconfig xinetd on
# create the dir that will be synced
RUN mkdir /home/share
# just to keep the container running
CMD /etc/rc.d/init.d/xinetd start && tail -f /dev/null
```

2. Build the container within the repository directory.

```
docker build . -t docker-rsync
```

3. Start the container and map the rsync server port to a specific host port.

```
docker run -p 10873:873 docker-rsync
```

Now we need to sync our share directory and sync any changes again as soon as anything changes. Rsync will only sync changes after an initial sync.

```
# initial sync
rsync -avP ./share --delete rsync://localhost:10873/example/
# sync on change
fswatch -0 ./share | xargs -0 -n 1 -I {} rsync -avP ./share --delete rsync://localhost:10873/example/
```

Fswatch utilizes rsync to talk to the container as soon as something changes. We do not use any kind of docker volume mounting. Hence all file operations will stay in the container and will be fast. Whenever we change something rsync transfers it to the container using . For sure you can use all rsync features like delete rules or exclude patterns.

If we change something (it does not matter if it’s a small project or a huge one) then we see something like

```
2 files to consider
share/helloWorld.txt
           5 100%    0.00kB/s    0:00:00 (xfer#1, to-check=0/2)
sent 159 bytes  received 44 bytes  406.00 bytes/sec
total size is 5  speedup is 0.02
```

0.02 seconds, great !

Fswatch uses file system events on Mac OS. Thus is still very fast and you can event tweak it. For example by excluding build related directories like _target_ or _node_modules_.

Sources are available on [GitHub](https://github.com/Journerist/docker-rsync-example).

For small projects the bad performance is not a critical issue. For huge application rsync is our hero. Good old tools, and still reliable and important.

Especially for all guys who love Mac OS and need to use a VM know the pain. Issues like the command key mapping are annoying. Either you map it to the Windows key or in the end you don’t use it anymore. So on Mac OS you use cmd+c to copy something and in your container you use control. For sure you can also map your host control to command but then you have again other issues. Everything is better when you can work in Mac OS instead of in a virtual machine as a mac user.

I hope you enjoyed the article. If you like it and feel the need for a round of applause, [follow me on Twitter](https://twitter.com/sesigl).  I work at eBay Kleinanzeigen, one of the biggest classified companies globally. By the way, [we are hiring](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen)!

Happy coding :)

