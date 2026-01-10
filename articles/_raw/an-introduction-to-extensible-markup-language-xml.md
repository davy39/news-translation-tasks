---
title: An Introduction to Extensible Markup Language (XML)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-extensible-markup-language-xml
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d1f740569d1a4ca3600.jpg
tags:
- name: markup
  slug: markup
- name: toothbrush
  slug: toothbrush
- name: xml
  slug: xml
seo_title: null
seo_desc: "XML stands for eXtensible Markup Language. It is extensible, because unlike\
  \ HTML, it does not use a predefined set of tags for identifying structural components.\
  \ Instead, it provides a mechanism for users to define tags themselves. \nXML was\
  \ designed ..."
---

XML stands for eXtensible Markup Language. It is extensible, because unlike HTML, it does not use a predefined set of tags for identifying structural components. Instead, it provides a mechanism for users to define tags themselves. 

XML was designed to simplify data sharing and data transport, and focuses on structuring that information in a logical way.

## **Syntax of XML**

The syntax for XML is very straight forward and quite easy to learn. 

XML documents must contain one root element that is the parent of all other elements:

```text
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```

Above syntax shows the root element which is necessary while creating an XML code.

But the root element can be called anything. For example:

```text
<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
```

In the code above `<note>` is the root element.

Advantages of using XML:

* Simplicity - XML documents are ordinary text files that can be created and edited with any text editor.
* Vendor independence
* Platform independence
* Extensive infrastructure

Disadvantages of using XML:

* Verbose and cumbersome syntax
* Highly inefficient storage

