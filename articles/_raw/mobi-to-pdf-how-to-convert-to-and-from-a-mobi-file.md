---
title: Mobi to PDF – How to Convert a Mobi File Extension In Browser or From the Command
  Line
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-01T02:05:00.000Z'
originalURL: https://freecodecamp.org/news/mobi-to-pdf-how-to-convert-to-and-from-a-mobi-file
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9872740569d1a4ca1a19.jpg
tags:
- name: ebook
  slug: ebook
- name: pdf
  slug: pdf
seo_title: null
seo_desc: If you've bought a book online recently, or downloaded a free public domain
  book at a site like Project Guttenberg, there's a good chance that it's a .mobi
  file. But you probably weren't able to open it because you didn't have the right
  software inst...
---

If you've bought a book online recently, or downloaded a free public domain book at a site like [Project Guttenberg](https://www.gutenberg.org/), there's a good chance that it's a `.mobi` file. But you probably weren't able to open it because you didn't have the right software installed.

In this article, you'll learn what `.mobi` files are and how to convert to and from the `.mobi` format for easier reading between devices.

## What's a `.mobi` file?

`.mobi` files are an eBook file format created by the company Mobipocket for their Mobipocket Reader software.

Amazon bought Mobipocket in 2005, and based the Kindle eBook reader's file formats (`.azw` and `.azw3`) on the `.mobi` format. Because of this, it's possible to read most `.mobi` files on Kindle devices.

## How to open a `.mobi` file

There are a number of ways to open `.mobi` eBooks. Some common suggestions include [Calibre](https://calibre-ebook.com/), [FBReader](https://fbreader.org/), and the official [Kindle app](https://www.amazon.com/b/ref=ruby_redirect?ie=UTF8&node=16571048011).

Of these, both Calibre and FBReader are available for Windows, macOS, Linux. On top of this, FBReader is also available for Android and iOS.

## How to convert a `.mobi` file

Converting `.mobi` eBooks into other formats is really straightforward, both online and locally.

### How to Convert to or from a `.mobi` file online

There are a number of sites like [docspal](https://www.docspal.com/) that let you upload a `.mobi` file, and select a format to convert it to like PDF. Once it's finished with the conversion, you can download the new file.

To convert a `.mobi` file into a PDF, go to the site and upload the file:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-43.png)

Next, select the file type you want to convert the `.mobi` file to from the dropdown on the right:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-44.png)

Finally, click the "Convert" button and download the converted file.

This also works if you want to convert a PDF file to `.mobi` – upload the PDF file, select `.mobi` from the dropdown on the right, and click the "Convert" button. 

### How to Convert to or from a `.mobi` file locally on your computer

While converting `.mobi` files to and from other formats on your local machine is a bit more involved, Calibre makes it easy.

To convert a `.mobi` file into a PDF, first, [download](https://calibre-ebook.com/download) and install Calibre for your operating system.

Then, open Calibre, click "Add books" in the top right corner, and select your eBook:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-45.png)
_Selecting a `.mobi` eBook in Linux Mint_

Next, select the eBook in your Calibre library and click the "Convert books" button in the menu at the top.

In the "Convert books" menu, select PDF from the "Output format" dropdown in the top right corner:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-47.png)

Finally, click the "OK" button in the lower right corner.

Once the conversion is finished, your new PDF file will be in the `/Calibre Library/[Book author]/` directory.

To convert a PDF to a `.mobi` file in Calibre, first add the PDF file, click "Convert books", select `.mobi` from the "Output format" dropdown, then click the "OK" button.

### How to Convert to or from a `.mobi` file from the command line

If you want a faster way to convert files to and from the `.mobi` format, Calibre includes a neat little command line tool, `ebook-convert`.

**Note:** These instructions were written for Linux, but should also apply to macOS and possibly Windows with [WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/install-win10) configured.

To convert a `.mobi` file to PDF, open up a terminal and `cd` into the directory with the eBook file:

```bash
cd ~/Documents/ebooks
```

Then, run the `ebook-convert` command with the following options:

```bash
ebook-convert <from_file>.<from_format> <to_file>.<to_format>
```

For example:

```bash
ebook-convert pride-and-prejudice.mobi pride-and-prejudice.pdf
```

Going from PDF to `.mobi` is just as easy:

```bash
ebook-convert pride-and-prejudice.pdf pride-and-prejudice.mobi
```

## The end

While `.mobi` files are an older format, they're still well supported and can be converted to other file formats easily. Whether you convert the files online or locally is up to you.

However you decide to convert your eBook files, stay safe and read a good book.

