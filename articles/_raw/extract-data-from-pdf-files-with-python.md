---
title: How to Extract Data from PDF Files with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-06T17:51:46.000Z'
originalURL: https://freecodecamp.org/news/extract-data-from-pdf-files-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Extract-Data-from-PDF-Files-with-Python-1.png
tags:
- name: data analysis
  slug: data-analysis
- name: pdf
  slug: pdf
- name: Python
  slug: python
seo_title: null
seo_desc: "By Shittu Olumide\nData is present in all areas of the modern digital world,\
  \ and it takes many different forms. \nOne of the most common formats for data is\
  \ PDF. Invoices, reports, and other forms are frequently stored in Portable Document\
  \ Format (PDF)..."
---

By Shittu Olumide

Data is present in all areas of the modern digital world, and it takes many different forms. 

One of the most common formats for data is PDF. Invoices, reports, and other forms are frequently stored in Portable Document Format (PDF) files by businesses and institutions. 

It can be laborious and time-consuming to extract data from PDF files. Fortunately, for easy data extraction from PDF files, Python provides a variety of libraries. 

This tutorial will explain how to extract data from PDF files using Python. You'll learn how to install the necessary libraries and I'll provide examples of how to do so.

There are several Python libraries you can use to read and extract data from PDF files. These include PDFMiner, PyPDF2, PDFQuery and PyMuPDF. Here, we will use PDFQuery to read and extract data from multiple PDF files. 

## How to Use PDFQuery

PDFQuery is a Python library that provides an easy way to extract data from PDF files by using CSS-like selectors to locate elements in the document. 

It reads a PDF file as an object, converts the PDF object to an XML file, and accesses the desired information by its specific location inside of the PDF document.

Let's consider a short example to see how it works.

```py
from pdfquery import PDFQuery

pdf = PDFQuery('example.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)

```

In this code, we first create a PDFQuery object by passing the filename of the PDF file we want to extract data from. We then load the document into the object by calling the `load()` method.

Next, we use CSS-like selectors to locate the text elements in the PDF document. The `pq()` method is used to locate the elements, which returns a PyQuery object that represents the selected elements.

Finally, we extract the text from the elements by accessing the `text` attribute of each element and we store the extracted text in a list called `text`.

Let's consider another method we can use to read PDF files, extract some data elements, and create a structured dataset using PDFQuery. We will follow the following steps:

* Package installation.
* Import the libraries.
* Read and convert the PDF files.
* Access and extract the Data.

### Package installation

First, we need to install PDFQuery and also install Pandas for some analysis and data presentation.

```bash
pip install pdfquery
pip install pandas

```

### Import the libraries

```py
import pandas as pd
import pdfquery

```

We import the two libraries to be be able to use them in our project.

### Read and convert the PDF files

```py
#read the PDF
pdf = pdfquery.PDFQuery('customers.pdf')
pdf.load()


#convert the pdf to XML
pdf.tree.write('customers.xml', pretty_print = True)
pdf

```

We will read the pdf file into our project as an element object and load it. Convert the pdf object into an Extensible Markup Language (XML) file. This file contains the data and the metadata of a given PDF page.

The XML defines a set of rules for encoding PDF in a format that is readable by humans and machines. Looking at the XML file using a text editor, we can see where the data we want to extract is.

### Access and extract the Data

We can get the information we are trying to extract inside the `LTTextBoxHorizontal` tag, and we can see the metadata associated with it. 

The values inside the text box, [68.0, 231.57, 101.990, 234.893] in the XML fragment refers to `Left, Bottom, Right, Top` coordinates of the text box. You can think of this as the boundaries around the data we want to extract.

Let’s access and extract the customer name using the coordinates of the text box.

```py
# access the data using coordinates
customer_name = pdf.pq('LTTextLineHorizontal:in_bbox("68.0, 231.57, 101.990, 234.893")').text()

print(customer_name)

#output: Brandon James

```

And that's it, we are done! 

**Note**: Sometimes the data we want to extract is not in the exact same location in every file which can cause issues. Fortunately, PDFQuery can also query tags that contain a given string.

## Conclusion

Data extraction from PDF files is a crucial task because these files are frequently used for document storage and sharing. 

Python's PDFQuery is a potent tool for extracting data from PDF files. Anyone looking to extract data from PDF files will find PDFQuery to be a great option thanks to its simple syntax and comprehensive documentation. It is also open-source and can be modified to suit specific use cases.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

