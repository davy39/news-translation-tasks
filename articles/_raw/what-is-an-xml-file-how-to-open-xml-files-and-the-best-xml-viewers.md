---
title: What is an XML File? How to Open XML Files and the Best XML Viewers
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-09-10T17:25:27.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-xml-file-how-to-open-xml-files-and-the-best-xml-viewers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98bf740569d1a4ca1bd4.jpg
tags:
- name: xml
  slug: xml
seo_title: null
seo_desc: 'If you''ve ever seen the .xml extension in your downloads folder and wondered
  what that is, you''re not alone.

  Keep reading to learn what and XML file is, and how to open it both locally on your
  computer and in online editors.

  What''s an XML file?

  XML s...'
---

If you've ever seen the `.xml` extension in your downloads folder and wondered what that is, you're not alone.

Keep reading to learn what and XML file is, and how to open it both locally on your computer and in online editors.

## What's an XML file?

XML stands for Extensible Markup Language and was created by the [W3C](https://www.w3.org/) (World Wide Web Consortium) in the 90s.

Though XML, like HTML, is a human readable markup language, they serve very different purposes. HTML describes the structure of a web page and its content, and XML describes the structure of data.

XML provides programs, and more importantly, programmers, a standard, widely accepted format to transmit data across different systems. In that way, XML has more in common with JSON than it does with HTML.

While XML is no longer the preferred method for organizing and transmitting data, it still has its place. XML is still used in many legacy systems, and both RSS and SVG are both based on the XML format.

Here's a simple example of an XML file and how it's used to structure data:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<fcc_merch>
   <item>
      <name>Triblend T-shirt</name>
      <price>$24.99</price>
      <description>Represent the freeCodeCamp community with pride in this jet-black Triblend T-shirt featuring the iconic "bonfire function call" logo.</description>
   </item>
   <item>
      <name>Cotton-Poly Pullover Hoodie</name>
      <price>$49.99</price>
      <description>Stay toasty and dress like a developer with this jet-black cotton-poly pullover hoodie.</description>
   </item>
   <item>
      <name>Ceramic Coffee Mug</name>
      <price>$14.99</price>
      <description>Toast to the developer community with your very own freeCodeCamp Bonfire Function Call mug.</description>
   </item>
</fcc_merch>
```

## How to open an XML file locally

Back to your downloads folder and that file with the `.xml` extension.

If you ever need to open an XML file, you have a lot of options. The big question is whether you need to edit the data in the XML file, or just view it.

### View an XML file in a browser

If all you need to do is view the data in an XML file, you're in luck. Just about every browser can open an XML file.

In Chrome, just open a new tab and drag the XML file over. Alternatively, right click on the XML file and hover over "Open with" then click "Chrome".

When you do, the file will open in a new tab. 

Here's what the `fcc-merch.xml` file looks like in Chrome:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-26.png)

**Note:** Instructions for your operating system may differ slightly.

### Edit an XML file in a text editor

If you need to edit an XML file locally, or you prefer to view it outside of the browser, the best way to do that is in a text editor.

You have a lot of options depending on your operating system. Here are some common recommendations:

**Windows:**

* [Notepad++](https://notepad-plus-plus.org/)

**Mac/Linux/Windows:**

* [VSCode](https://code.visualstudio.com/)
* [Atom](https://atom.io/)
* [Sublime Text](https://www.sublimetext.com/)

Note that VSCode, Atom, and Sublime Text are pretty heavy programs, especially if all you want to do is edit an XML file. Mac and Linux users may have access to other lightweight text editors like gedit or Leafpad that can open and edit XML files.

If you want to learn how to code, then by all means, try out one of the editors listed above.

Once you've download an editor, you can open the XML file from the editor's GUI like you would any other file.

Here's the same `fcc-merch.xml` file in VSCode:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-27.png)

## How to open an XML file online

Opening an XML file online is easy, and the best online XML viewers also function as editors and formatters.

Here are some of the most popular online XML viewers/editors:

* [Code Beautify](https://codebeautify.org/xmlviewer)
* [JSON Formatter](https://jsonformatter.org/xml-viewer)
* [Tutorialspoint](https://www.tutorialspoint.com/online_xml_editor.htm)

Each one works similarly, allowing you to either upload the XML file from your computer or copy and paste it into the editor on the left:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-24.png)
_Code Beautify's XML viewer/editor_

Once you load your XML, you can click "Tree View" to make it easier to see the hierarchy of your data and how different fields are nested:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-33.png)

 Just make any edits you need to in the editor on the left. Then when you're done, just click "Download" to download a copy of your edited file.

Note that your downloaded copy may have a different name like `codebeautify.xml`. Just rename the file before you attach it to an email, upload it, or whatever it is you need to do.

## In summary

The XML format has a long and storied history.

Even though XML files are quite dense compared to modern solutions for data transmission like JSON, it doesn't hurt to know how to open and edit them. Fortunately you've got a lot of options on your local machine and online.

Hope this helps the next time you need to open up or edit an XML file.

Stay safe and happy coding.

