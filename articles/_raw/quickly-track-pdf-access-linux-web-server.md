---
title: How to Quickly Track PDF Access on a Linux Web Server
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-12-02T17:17:52.000Z'
originalURL: https://freecodecamp.org/news/quickly-track-pdf-access-linux-web-server
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/calculator.jpg
tags:
- name: analytics
  slug: analytics
- name: Google Analytics
  slug: google-analytics
- name: Linux
  slug: linux
- name: metrics
  slug: metrics
- name: pdf
  slug: pdf
seo_title: null
seo_desc: 'Is it possible to track how many times your website''s users click to download
  binary files like PDFs or JPGs? Yes it is possible. Is it easy? I didn''t originally
  think so. I was wrong.

  The story began while I was optimizing a landing page on my Boots...'
---

Is it possible to track how many times your website's users click to download binary files like PDFs or JPGs? Yes it is possible. Is it easy? I didn't originally think so. I was wrong.

The story began while I was optimizing a landing page on my [Bootstrap IT website](https://bootstrap-it.com/davidclinton/keeping-up) for my new book, _Keeping Up: Backgrounders to all the big technology trends you can't afford to miss_. 

I wanted to provide access to the PDF file of a sample chapter from the book. But I also wanted some way to know how many people actually downloaded it.

Now let's take a step back. [Google Analytics](https://analytics.google.com/analytics/web/) is a free service that uses code snippets inserted into your HTML files to collect and display data on how often your files were accessed. 

The magic - and problem - of Google Analytics is in just how much information about your users can be revealed. I discussed some of the privacy concerns involved with the service in the Keeping Up book. I also mentioned how I feel at least a bit guilty for using the service myself on my own sites.

At any rate, all by itself, Google Analytics isn't able to tell you much about how your web-based PDFs are being used. Of course, there are tricks for getting around the problem. 

Traditional approaches include setting up the [Google Tag Manager](https://marketingplatform.google.com/about/tag-manager/), customizing the syntax of the request URLs you use or, if your site uses WordPress software, working with the [Monster Insights plugin](https://www.monsterinsights.com/). Each of those can work, but will require a fairly steep learning curve.

But I'm a Linux sysadmin. And, as I never fail to remind the people around me, the best sysadmins are lazy. Learning curve? That sounds suspiciously like work. Not gonna happen on my watch.

So here's the deal. My web server, obviously, runs Linux. And, under the hood, HTTP traffic is handled by Apache. That means that everything happening to and on my websites is going to be logged by Apache. 

Everything. All it'll take to give me what I need to know about what my PDF sample chapter has been up to, is a single line of Bash run from my local workstation:

```
echo "cd /var/log/apache2 && grep -nr KeepingUpSampleChapter" \
   | ssh -i PrivateKey.pem LoginName@bootstrap-it.com

```

Let's break that down. The first of the two commands in quotation marks (`cd /var/log/apache2`) will move us to the /var/log/apache2/ directory on the Linux server where Apache writes its logs. That's not rocket science.

There are going to be multiple files of interest in that directory. That's because messages relevant to regular access and errors are saved to different files, and because file rotation policies mean that there could be more than one version of either of those files, too. So I'll use `grep` to search all the uncompressed files for the `KeepingUpSampleChapter` string. `KeepingUpSampleChapter` is, of course, part of the filename of the PDF.

I then pipe that command to SSH, which will connect to my remote server and execute the command. Here's what a single entry would look like from a successful run (I've removed the requester's IP address out of privacy concerns):

```
other_vhosts_access.log.1:12200:bootstrap-it.com:443 <requester's IP Address> - - [01/Dec/2020:16:39:36 -0500] "GET /davidclinton/KeepingUpSampleChapter.pdf?pdf=SamplePDF HTTP/1.1" 200 65146 "https://bootstrap-it.com/davidclinton/keeping-up/" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"

```

We can see:

* The log file where the entry appeared (`other_vhosts_access.log.1`)
* The requester's IP address (redacted)
* The timestamp telling us exactly when the file was accessed
* The relative location of the file on the server file system (`/davidclinton/KeepingUpSampleChapter.pdf`)
* The URL from which the request was made (`https://bootstrap-it.com/davidclinton/keeping-up/`)
* And the browser the user was running

That's a lot of information. If we're just curious about how many _times_ the file was downloaded, we can simply pipe the output to the `wc` command that will tell us three things about the output: the number of lines, words, and characters it contained. That command would look like this:

```
echo "cd /var/log/apache2 && grep -nr KeepingUpSampleChapter | wc" \
   | ssh -i PrivateKey.pem LoginName@bootstrap-it.com

```

There is one possible limitation with this method. If your website is busy, the log files will roll over frequently, often more than once a day. By default, after the first rollover, the files are compressed using the `gz` algorithm, which can't be read by `grep`.

The `zgrep` command won't have any trouble handling such files, but the process could end up taking a very long time. You might consider writing a simple custom script to decompress each `gz` file and then run regular `grep` against its contents. That'll be your project.

_There's much more administration goodness in the form of books, courses, and articles available at my [bootstrap-it.com](https://bootstrap-it.com/davidclinton)._

