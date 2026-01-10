---
title: How to Save a Base64 String as a PDF File on the Client Side in JavaScript
subtitle: ''
author: Vikram Aruchamy
co_authors: []
series: null
date: '2023-02-27T18:20:44.000Z'
originalURL: https://freecodecamp.org/news/save-a-base64-string-as-pdf-on-client-side-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/How-to-check-if-a-String-is-URL-in-Javascript.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Base64 strings represent binary objects in textual format. They are designed
  to transmit binary data between channels that only support a textual format.

  Sometimes, you might receive PDF files from various services as a Base64 string,
  and you may nee...'
---

Base64 strings represent binary objects in textual format. They are designed to transmit binary data between channels that only support a textual format.

Sometimes, you might receive PDF files from various services as a Base64 string, and you may need to convert them to a PDF file on the client side after receiving the response.

This tutorial teaches you how to save a Base64 string as a PDF on the client side in JavaScript.

## Base64 String Format

[Base64 strings](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs) are in text format, and they have a metadata prefix on them.

**Here's the syntax:**

```
data:[<mediatype>][;base64],<data>

```

Where,

* `data` is a common prefix
* `Mediatype` is a [Mimetype](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) string that represents the type of the file
* `Base64` shows that the string is a Base64 string

Let's look at an example:

```
data:application/pdf;base64,<Base64 String>

```

The above string represents a Base64 string of a PDF file.

Base64 strings are also known as [DataURLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs). Data URLs are URLs that are prefixed with the `data:` scheme to allow users to embed files inline in the `HTML` document.

To convert a PDF file into a Base64 string, you can use the [online Base64 Encoder tool](https://www.base64encode.pro/). You can upload the file and click _Encode_. It’ll return a text file that contains the base64 equivalent string of the PDF file.

Now let's use the output string and [convert the Base64 string into a PDF file](https://www.base64decode.pro/blog/how-to-convert-a-base64-string-to-a-file-in-java-with-examples/) format on the client side using JavaScript.

## How to Create a User Interface with HTML

For this demonstration, let's create a simple UI in HTML. Our UI will have:

* A `text area` that accepts a Base64 string in the text box
* A `Button`, with a click event, that converts the Base64 string available in the text area into a PDF format and downloads it automatically.

Here's the code to do that:

```
<label for="Base64StringTxtBox">Base64 String</label>

<textarea id="Base64StringTxtBox" name="Base64Text" rows="4" cols="50">

</textarea>

<button type="Convert" onclick="downloadAsPDF()">Convert to PDF</button>

```

## How to Use the Anchor Tag

To convert the Base64 string into a PDF file, you'll need to do the following:

* Get the Base64 string from the Textarea
* Create an [Anchor](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a) element in the HTML element
* Assign the Base64 string to the `href` attribute of the anchor element
* Assign a filename to the `download` attribute. The [download](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attr-download) instructs the browser to treat the linked URL as a download option. When the anchor link is clicked, the target specified in the `href` attribute is downloaded with the filename.

Let's look at an example:

The following JavaScript code downloads the Base64 string as a PDF file:

```
function downloadAsPDF(pdf) {

  var base64String = document.getElementById("Base64StringTxtBox").value;
  
  const downloadLink = document.createElement("a");
  
  downloadLink.href = base64String;
  
  downloadLink.download = "convertedPDFFile.pdf";
  
  downloadLink.click();
}

```

## How to Handle Base64 Strings without Metadata

In some cases, a base64 strings might not have a metadata prefix. The user might receive just the Base64 data as a response.

Each file type has a common prefix in the Base64 string. For example,

* A JPG file Base64 string starts with `/9j`
* A PDF file Base64 string starts with  `JVB`
* A PNG file Base64 string starts with `iVB`

The Stackoverflow answer [here](https://stackoverflow.com/a/58158656/8510024) explains more in detail about finding the Mime type from the Base64 string without metadata.

Now let's learn how to download Base64 string without metadata as a PDF file.

* Check if the Base64 starts with `JVB`, append the metadata `data:application/pdf;base64,` to the existing Base64 string, and download it using the anchor tag.
* Check if the Base64 string starts with the `Data:` prefix. If yes, directly download the file using the anchor tag.
* If the string doesn’t have the prefix `data:` or `JVB`, then it is not a valid PDF file Base64 string. Alert the user with an appropriate error message.

Let's look at an example.

The following code demonstrates how to validate the Base64 string before downloading it as a PDF file.

```
function downloadAsPDF(pdf) {

  var base64String = document.getElementById("Base64StringTxtBox").value;

  if (base64String.startsWith("JVB")) {
    base64String = "data:application/pdf;base64," + base64String;
    downloadFileObject(base64String);
  } else if (base64String.startsWith("data:application/pdf;base64")) {
    downloadFileObject(base64String);
  } else {
    alert("Not a valid Base64 PDF string. Please check");
  }

}

function downloadFileObject(base64String) {
  const linkSource = base64String;
  const downloadLink = document.createElement("a");
  const fileName = "convertedPDFFile.pdf";
  downloadLink.href = linkSource;
  downloadLink.download = fileName;
  downloadLink.click();
}

```

## How to Use the Online Base64 Decode Tool

You can also use the [Online Base64 Decode tool](https://www.base64decode.pro/) to convert the Base64 String into a PDF file. You can add the Base64 string in a text file and upload it to the online tool. It’ll convert the file and download it.

### JSfiddle Link

The above two tutorials are available in the following JSfiddle links:

* Example 1 – [Download the Base64 string with the Meta Data prefix](https://jsfiddle.net/jsowl/yxbts6ap/4/)
* Example 2 – [Download the Base64 string without the Meta Data prefix](https://jsfiddle.net/jsowl/vmu5t80b/9/)

## Conclusion

To summarise, in this tutorial you have learned what Base64 strings are, how to convert a Base64 string to a file, and then download it on the client side using JavaScript. 

You’ve also learned about the Metadata prefixes of the Base64 strings.

