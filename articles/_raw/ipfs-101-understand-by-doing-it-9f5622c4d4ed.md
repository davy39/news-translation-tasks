---
title: 'Learn by doing: a nice and easy intro to the Inter Planetary File System'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-21T09:44:26.000Z'
originalURL: https://freecodecamp.org/news/ipfs-101-understand-by-doing-it-9f5622c4d4ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IbSEzAzdoh3aOvsG0fyiGA.png
tags:
- name: code
  slug: code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Niharika Singh

  Primer on IPFS

  IPFS is short for Inter Planetary File System. It is a peer-to-peer, distributed
  file system to make the web faster, safer, and more open. To shift from the present
  version of the web to a distributed version of the w...'
---

By Niharika Singh

### Primer on IPFS

IPFS is short for Inter Planetary File System. It is a peer-to-peer, distributed file system to make the [web faster, safer, and more open.](https://ipfs.io/) To shift from the present version of the web to a distributed version of the web, we need the IPFS. Essentially, the aim is to replace HTTP.

**There are NO centralised servers. Everything is decentralised.** Let’s see how this works by doing it.

_I wrote an article about how IPFS uses MerkleDAG, which can be found [here](https://hackernoon.com/ipfs-and-merkle-forest-a6b7f15f3537)._

### STEP 1: Install IPFS

IPFS alpha version is written in GoLang. You’ll need to download it for your platform from [this link](https://ipfs.io/docs/install/).

To check that you’ve successfully installed IPFS, open the command console and enter the following command.

```
$ ipfs help
```

If you see something which starts like this:

```
USAGE
```

```
ipfs - Global p2p merkle-dag filesystem.
```

```
ipfs [--config=<config> | -c] [--debug=<debug> | -D] [--help=<help>] [-h=<h>] [--local=<local> | -L] [--api=<api>] <command> ...
```

Then you’re good to go!

![Image](https://cdn-media-1.freecodecamp.org/images/yDjQnIwZUm2seDD83k1bYg9Gd6yEK4Ak7fWQ)

### Step 2: Initialize IPFS Node

To initialize your local machine as an IPFS node, run the following command:

```
$ ipfs init
```

This command initializes IPFS configuration files and generates a new keypair using 2048 bit-RSA. This will produce your **peer identity** as an output.

You’ll see something like this:

```
initializing IPFS node at /Users/niharikasingh/.ipfs
```

```
generating 2048-bit RSA keypair...done
```

```
peer identity: QmTo1oMgGEH6Ym3H1xF55U7q4bexd5288YmEJjubDqVmKn
```

```
to get started, enter:
```

```
ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme
```

**You’ll have a different peer identity than mine.**

Now run the following command to see the hello message:

```
$ ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme
```

You’ll see a result that looks something like this:

```
Hello and Welcome to IPFS!
```

```
██╗██████╗ ███████╗███████╗
```

```
██║██╔══██╗██╔════╝██╔════╝
```

```
██║██████╔╝█████╗  ███████╗
```

```
██║██╔═══╝ ██╔══╝  ╚════██║
```

```
██║██║     ██║     ███████║
```

```
╚═╝╚═╝     ╚═╝     ╚══════╝
```

```
If you're seeing this, you have successfully installed
```

```
IPFS and are now interfacing with the ipfs merkledag!
```

```
-------------------------------------------------------
```

```
| Warning:                                              |
```

```
|   This is alpha software. Use at your own discretion! |
```

```
|   Much is missing or lacking polish. There are bugs.  |
```

```
|   Not yet secure. Read the security notes for more.   |
```

```
-------------------------------------------------------
```

```
Check out some of the other files in this directory:
```

```
./about
```

```
./help
```

```
./quick-start     <-- usage examples
```

```
./readme          <-- this file
```

```
./security-notes
```

**Voilà!**

### Step 3: Add some files to IPFS

Create a demo folder anywhere on your machine and throw in a couple of files. Any type of files: images, videos, music…literally anything. You can even add another folder within this folder.

![Image](https://cdn-media-1.freecodecamp.org/images/U1AAtYHLUIf2v6R6zKfdkx6ruHdul0tIQuuA)
_This is what my demo folder looks like._

Suppose the folder is named **“test-ipfs”.** So to push these files, first navigate into this folder on your command line and then run the following command:

```
$ ipfs add -r .
```

This command adds all files/directories present in the folder to IPFS recursively to create the IPFS MerkleDAG. You can even add a single file by using the following command: `$ ipfs add <filename.extensi`on>

This creates the following output:

```
added QmSTuTEThyESvDgmYdao2HK6kurXe2pqjA1KHPD8wSHVy7 test-ipfs/donut.jpeg
```

```
added QmSR9MJ5resQLjwqy7kEVVKJwTvDG53Npt9i1c6jZeZDtW test-ipfs/purse.jpeg
```

```
added QmUNLLsPACCz1vLxQVkXqqLX5R1X345qqfHbsf67hvA3Nn test-ipfs/folder1
```

```
added QmaKZ3dnc9ejBdGgEDCRtsLFNRxcY67HLjk6gXUnk9sdM9 test-ipfs
```

You’ll notice this long thing is the unique hash of that particular file. All the files and directories, as well as the parent folder, will have their unique hash.

```
$ ipfs ls QmaKZ3dnc9ejBdGgEDCRtsLFNRxcY67HLjk6gXUnk9sdM9
```

This works **exactly** like the UNIX file system. The expected output will show the following:

```
QmSTuTEThyESvDgmYdao2HK6kurXe2pqjA1KHPD8wSHVy7 219859 donut.jpeg
```

```
QmUNLLsPACCz1vLxQVkXqqLX5R1X345qqfHbsf67hvA3Nn 4      folder1/
```

```
QmSR9MJ5resQLjwqy7kEVVKJwTvDG53Npt9i1c6jZeZDtW 110254 purse.jpeg
```

The file size is shown at the end of the hash string. For example, 219859 is the file size of donut.jpeg.

### Step 4: Access files online

To access files online, first we’ve got to connect our node to the IPFS network. To do that, we’ve got to run the IPFS daemon.

```
$ ipfs daemon
```

This will produce the following output:

```
Initializing daemon...
```

```
Successfully raised file descriptor limit to 2048.
```

```
Swarm listening on /ip4/127.0.0.1/tcp/4001
```

```
Swarm listening on /ip4/169.254.100.132/tcp/4001
```

```
Swarm listening on /ip4/192.168.1.3/tcp/4001
```

```
Swarm listening on /ip6/::1/tcp/4001
```

```
Swarm listening on /p2p-circuit/ipfs/QmTo1oMgGEH6Ym3H1xF55U7q4bexd5288YmEJjubDqVmKn
```

```
Swarm announcing /ip4/127.0.0.1/tcp/4001
```

```
Swarm announcing /ip4/169.254.100.132/tcp/4001
```

```
Swarm announcing /ip4/192.168.1.3/tcp/4001
```

```
Swarm announcing /ip6/::1/tcp/4001
```

```
API server listening on /ip4/127.0.0.1/tcp/5001
```

```
Gateway (readonly) server listening on /ip4/127.0.0.1/tcp/8080
```

```
Daemon is ready
```

Now that you’ve pushed the files to IPFS, let’s see how can you access them.

```
localhost:8080/ipfs/hashOfTheFileYouWantToOpen
```

Suppose I wish to open purse.jpeg. I’ll copy the hash of purse.jpeg and hit the browser with the above syntax.

![Image](https://cdn-media-1.freecodecamp.org/images/KadAfb5SZMNkJwsx-DuPTFqgTlWwCWQTLcNj)

Likewise, you can even hear your music, video, and so on.

You can even access your content using the IPFS gateway:

```
gateway.ipfs.io/ipfs/hashOfTheFile
```

![Image](https://cdn-media-1.freecodecamp.org/images/odk2-x4N9Ae1PD05hO9-695FG6dVTP9wTfuQ)

![Image](https://cdn-media-1.freecodecamp.org/images/GvoWuiYohw98UJYL9EHpEHFU367obEpLsg8Z)

**You’re about to see real magic now!**

Point your browser to:

```
127.0.0.1:5001/webui
```

You’ll see this screen:

![Image](https://cdn-media-1.freecodecamp.org/images/QCO1qZsohtn6LiKPOV3ombnRFCbf-2Sp1lqL)

Feel free to play around.

**Connections:** Will show you your peers all over the world.

![Image](https://cdn-media-1.freecodecamp.org/images/9LrR9rpOaxqh2BAIk4Tm65Of5Hr3dOiWUH7r)
_How cool is that!_

**Files:** You can push files using the webUI.

![Image](https://cdn-media-1.freecodecamp.org/images/azl0Ef-ZLdXN5k9m-FK-ikvKAiUENjGgHY8Z)

**DAG:** Will show you the MerkleDAG and show related info about the file when its hash is entered.

![Image](https://cdn-media-1.freecodecamp.org/images/ZYgOHsZByxyGx5SnbCfL1AYJtuXaxX8SV28n)

**Config:** This will show you configurations about your own machine.

![Image](https://cdn-media-1.freecodecamp.org/images/zkgoHOaUu5GHtvWGHgxkKzPI459R3acpblV3)

### Step 5: Access files from your peers

IPFS promises that there is no central server that is giving you the files. So what if I tell you that you can stream video from my laptop also even if IPFS daemon isn’t running on my computer?

I’ve uploaded Katy Perry’s Roar video online. You can access it from me rather than hitting YouTube.

Go to:

```
localhost:8080/ipfs/QmWPCbXCK4NGXKac1QoKHdW7Qqud481T5FLHzu7RnSRDGR/
```

And **enjoy**!

You’ll be streaming this video on IPFS.

You can even use VLC Media Player for this.

URL used:

```
http://localhost:8080/ipfs/QmWPCbXCK4NGXKac1QoKHdW7Qqud481T5FLHzu7RnSRDGR/Katy%20Perry%20-%20Roar%20%28Official%29.mp4
```

![Image](https://cdn-media-1.freecodecamp.org/images/5qSQK6IMz3JUD5gVYINaK7soOWmMxMPXVSwv)

![Image](https://cdn-media-1.freecodecamp.org/images/kZNXalAycR1zhatzYGMkZzWcViABcSRdN9f7)

Feel free to play around with IPFS. This was a very brief overview. But I hope you got a basic idea about what IPFS is!

