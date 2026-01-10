---
title: 'The Tar Command in Linux: Tar CVF and Tar XVF Explained with Example Commands'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-08-14T21:34:05.000Z'
originalURL: https://freecodecamp.org/news/tar-command-linux-tar-cvf-tar-xvf
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9938740569d1a4ca1e84.jpg
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "The name tar is, by most accounts, short for tape archive. The \"tapes\"\
  \ in question would be all those magnetic storage drives that were popular all the\
  \ way back in the 1950s. \nThat suggests that the tar tool might be a bit old and\
  \ past its prime. But..."
---

The name `tar` is, by most accounts, short for _tape archive_. The "tapes" in question would be all those magnetic storage drives that were popular all the way back in the 1950s. 

That suggests that the `tar` tool might be a bit old and past its prime. But the truth is that, over all the years and through all the seismic changes to the IT world, `tar` has lost none of its power and value.

In this article, based on content from my [Linux in Action book](https://www.amazon.com/gp/product/1617294934/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1617294934&linkCode=as2&tag=projemun-20&linkId=1a460c0cd9a39e01821133b90632cba8), I'm going to show you the basics of tar archive creation, compression, and restoration. Let's start at the beginning.

# Creating archives

This example will take all the files and directories within and below the current work directory and build an archive file that I’ve cleverly named `archivename.tar`. 

Here I use three arguments after the tar command: 

* the `c` tells tar to create a new archive,
* `v` sets the screen output to verbose so I’ll get updates, and 
* `f` points to the filename I’d like to give the archive. 

The `*` is what tells `tar` to include all files and local directories recursively.

```
$ tar cvf archivename.tar *
file1
file2
file3
directory1
directory1/morestuff
directory1/morestuff/file100
directory1/morestuff/file101

```

The tar command will never move or delete any of the original directories and files you feed it – it only makes archived copies. 

You should also note that using a dot (.) instead of an asterisk (*) in the previous command would include even hidden files (whose filenames begin with a dot) in the archive.

If you’re following along on your own computer (as you definitely should), then you’ll see a new file named archivename.tar. The .tar filename extension isn’t necessary, but it’s always a good idea to clearly communicate the purpose of a file in as many ways as possible.

Extracting your archive in order to restore the files is easy: Just use `xvf` instead of `cvf`. That, in the example, will save new copies of the original files and directories in the current location.

```
$ tar xvf archivename.tar
file1
file2
file3
directory1
directory1/morestuff
directory1/morestuff/file100
directory1/morestuff/file101

```

Of course, you can also have tar send your extracted files to some other place using the `-C` argument, followed by the target location:

```
$ tar xvf archivename.tar -C /home/mydata/oldfiles/

```

You won’t always want to include all the files within a directory tree in your archive. 

Suppose you’ve produced some videos, but they're currently kept in directories along with all kinds of graphic, audio, and text files (containing your notes). The only files you need to back up are the final video clips using the .mp4 filename extension. 

Here’s how to do that:

```
$ tar cvf archivename.tar *.mp4

```

That’s great. But those video files are enormous. Wouldn’t it be nice to make that archive a bit smaller using compression? 

Say no more! Just run the previous command with the `z` (zip) argument. That will tell the gzip program to compress the archive. 

If you want to follow convention, you can also add a `.gz` extension in addition to the `.tar` that’s already there. Remember: clarity.

Here’s how that would play out:

```
$ tar czvf archivename.tar.gz *.mp4

```

If you try this out on your own .mp4 files and then run ls -l on the directory containing the new archives, you may notice that the `.tar.gz` file isn’t all that much smaller than the `.tar` file, perhaps 10% or so. What’s with that? 

Well, the `.mp4` file format is itself compressed, so there’s a lot less room for gzip to do its stuff.

As tar is fully aware of its Linux environment, you can use it to select files and directories that live outside your current working directory. This example adds all the `.mp4` files in the `/home/myuser/Videos/` directory:

```
$ tar czvf archivename.tar.gz /home/myuser/Videos/*.mp4

```

Because archive files can get big, it might sometimes make sense to break them down into multiple smaller files, transfer them to their new home, and then re-create the original file at the other end. The split tool is made for this purpose.

In this example, `-b` tells Linux to split the archivename.tar.gz file into 1 GB-sized parts. The operation then names each of the parts—archivename.tar.gz.partaa, archivename.tar.gz.partab, archivename.tar.gz.partac, and so on:

```
$ split -b 1G archivename.tar.gz "archivename.tar.gz.part"

```

On the other side, you re-create the archive by reading each of the parts in sequence (cat archivename.tar.gz.part*), then redirect the output to a new file called archivename.tar.gz:

```
$ cat archivename.tar.gz.part* > archivename.tar.gz

```

# Streaming file system archives

Here’s where the good stuff starts. I’m going to show you how to create an archive image of a working Linux installation and stream it to a remote storage location — all within a single command. Here’s the command:

```
# tar czvf - --one-file-system / /usr /var \
  --exclude=/home/andy/ | ssh username@10.0.3.141 \
  "cat > /home/username/workstation-backup-Apr-10.tar.gz"

```

Rather than trying to explain all that right away, I’ll use smaller examples to explore it one piece at a time. 

Let’s create an archive of the contents of a directory called importantstuff that’s filled with, well, really important stuff:

```
$ tar czvf - importantstuff/ | ssh username@10.0.3.141 "cat > /home/username/myfiles.tar.gz"
importantstuff/filename1
importantstuff/filename2
[...]
username@10.0.3.141's password:

```

Let me explain that example. Rather than entering the archive name right after the command arguments (the way you’ve done until now), I used a dash (czvf -). 

The dash outputs data to standard output. It lets you push the archive filename details back to the end of the command and tells tar to expect the source content for the archive instead. 

I then piped (|) the unnamed, compressed archive to an ssh login on a remote server where I was asked for my password. 

The command enclosed in quotation marks then executed cat against the archive data stream, which wrote the stream contents to a file called myfiles.tar.gz in my home directory on the remote host.

One advantage of generating archives this way is that you avoid the overhead of a middle step. There’s no need to even temporarily save a copy of the archive on the local machine. Imagine backing up an installation that fills 110 GB of its 128 GB of available space. Where would the archive go?

That was just a directory of files. Suppose you need to back up an active Linux OS to a USB drive so you can move it over to a separate machine and drop it into that machine’s main drive. 

Assuming there’s already a fresh installation of the same Linux version on the second machine, the next copy/paste operation will generate an exact replica of the first.

> NOTE: This won’t work on a target drive that doesn’t already have a Linux file system installed. To handle that situation, you’ll need to use `dd`.

The next example creates a compressed archive on the USB drive known as `/dev/sdc1`. 

The `--one-file-system` argument excludes all data from any file system besides the current one. This means that pseudo partitions like `/sys/` and `/dev/` won’t be added to the archive. If there are other partitions that you want to include (as you’ll do for `/usr/` and `/var/` in this example), then they should be explicitly added. 

Finally, you can exclude data from the current file system using the `--exclude` argument:

```
# tar czvf /dev/sdc1/workstation-backup-Apr-10.tar.gz \
  --one-file-system \
  / /usr /var \
  --exclude=/home/andy/

```

Now let’s go back to that full-service command example. Using what you’ve already learned, archive all the important directories of a file system and copy the archive file to a USB drive. It should make sense to you now:

```
# tar czvf - --one-file-system / /usr /var \
  --exclude=/home/andy/ | ssh username@10.0.3.141 \
  "cat > /home/username/workstation-backup-Apr-10.tar.gz"

```

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com/)._

