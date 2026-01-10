---
title: How to generate a GitHub markdown file from Microsoft Word using TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T00:48:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-a-github-markdown-file-from-microsoft-word-using-typescript-a8976ea958c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*85IJbXqoCZIBLjS3oyQ1YA.jpeg
tags:
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Manish Bansal

  What? Why would one want to generate an MD file from a Microsoft word document?
  If that’s the first thought you had after reading this title, then let me give you
  a strong use case.

  Consider a situation where you are using Git or any...'
---

By Manish Bansal

What? Why would one want to generate an MD file from a Microsoft word document? If that’s the first thought you had after reading this title, then let me give you a strong use case.

Consider a situation where you are using Git or any other version control system (VCS) for your project’s sources as well as its artifacts. Now, like most projects, you decide to use Microsoft word for documentation and check it into Git. Again, multiple team members edit the same document. After editing, they check-in the document into the repository.

Now, Git will be able to maintain the history of your document. How will you be able to look at the changes that have been made to the document since you last checked it in? Yes, you can use Microsoft word’s track change mode, but isn’t that messy? Or for heaven’s sake, will you be able to use Git diff utility to check the differences quickly? I would say, no.

Then what is the solution? Should you stop using Microsoft Word for documentation? Or should you switch to some other VCS?

I would say neither. How about you maintain your documentation in Microsoft word? Then change it into a markdown (MD) file (in layman terms, a text file) during the build phase and check in? If that solution excites you, then keep reading.

But before jumping right into conversion, let me first tell you what exactly is a markdown file.

### What is a markdown or an MD file?

Markdown is a syntax language aiming for easy reading and writing structured text. Further, it is easy to learn, and it only requires a text editor to create a document.

Now, there are multiple implementations of the language (like [GFM](https://github.github.com/gfm/) aka Github flavored Markdown). Each of these implementations has their own improvements and features that are not necessarily compatible with each other.

Each implementation supports various common features like paragraphs, blockquotes, headings, and lists. This helps in maintaining text in a structured manner like Microsoft Word. But, instead of using internal binary codes, MD files use plain text characters for these features. This makes an MD file a text file but not a binary file like a docx file.

For example, in GitHub’s markdown flavor, here are the various features and ways of representing them in the form of text compared to a word document.

![Image](https://cdn-media-1.freecodecamp.org/images/EmrHeOtVuSp1R-hU7j6UqWwzB9r7DhCjGY0Y)

For the detailed advantages of MD files over word documents, you can also refer to [this](https://hackernoon.com/say-yes-to-markdown-no-to-ms-word-be4692e7a8cd) article.

### OK! I am convinced. Show me the code.

Disclaimer: This project is inspired by TypeScript source code. While browsing it, I found this idea of converting a word document to an MD file. You can see its source code [here](https://github.com/manishbansal8843/TypeScript/blob/1b880f8ad445c778911a71b8cdec94ae885299bf/scripts/word2md.ts#L407).

For simplicity, I have removed a few sections of code in my repository. The original code was meant to convert TypeScript specification documentation to an MD file. This file contains lots of customized styles. So, once you are done with this article, you can very much go through TypeScript converter code and appreciate it’s abilities to perform more complex conversions.

The complete code mentioned in this article can be referred to [here](https://github.com/manishbansal8843/word2mdconverter). The whole code can be divided into 3 sections:

1. Gulp Configurations.
2. CScript execution.
3. TypeScript main function

As stated earlier, you can convert a word document to a MD file during the build phase. This can be done by any task runner. Here, I have chosen gulp.

In Gulp configurations, I have defined 3 tasks. First one is to clean the build directory which is pretty standard. Second is to compile the TypeScript code. And the last one is to call the CScript for executing the JavaScript.

### What is CScript?

CScript.exe (present in C:\Windows\System32) is a console-based executable for the scripting host that are used to run the scripts. It can interpret scripting languages like VB Script or JavaScript. Similarly, we have WScript but it is used for windows applications. In this, the console is not attached. So if you have a requirement of creating a console based application, we can use CScript.

Now, in our project, the main job of CScript is to provide a run-time environment to our script i.e. JavaScript. Now, you must be thinking, why haven’t I used node instead of CScript to run my JavaScript.

Both provide a run-time environment for a JavaScript. CScript provides inherent support for windows component object model technique. So if you try to run this script via Node, you will get an error like this.

> var fileStream = new ActiveXObject(“ADODB.Stream”);

> ReferenceError: ActiveXObject is not defined

**Now, what is a component object model technique?**

Component object model is a technology developed by Microsoft. It is not a language but a binary standard. As per the definition,

> The Microsoft Component Object Model ([COM](https://docs.microsoft.com/en-us/windows/desktop/com/the-component-object-model)) is a platform-independent, distributed, object-oriented system for creating binary software components that can interact. COM is the foundation technology for Microsoft’s OLE (compound documents), ActiveX (Internet-enabled components), as well as others.

In layman terms, COM objects are interfaces to the various runtime objects. (That’s why the definition has a term called “binary software components”). It is not a language, but a technique which is programming language agnostic.

The only language requirement for COM is that code is generated in a language that can create structures of pointers. Either explicitly or implicitly, call functions through pointers. Object-oriented languages such as C++ and Smalltalk provide programming mechanisms that simplify the implementation of COM objects

After that, we can use any other language like Java, VB or JavaScript to interact with those COM objects. This will further give us access to runtime applications. In our case, to Microsoft word applications.

**So, are you saying we cannot use Node at all here?**

No, that is not true. We can use Node also instead of CScript. But to support COM, we will need to install another package called win32com for COM support. Details can be found [here](https://helloacm.com/using-com-object-in-nodejs/).

### Final code

Now, in order to interact with word application, various APIs have been used. And since we are using the COM object model, I referred to the [word object model](https://docs.microsoft.com/en-us/visualstudio/vsto/word-object-model-overview?view=vs-2017).

Word provides hundreds of objects with which you can interact. These objects are organized in a hierarchy that closely follows the user interface. At the top of the hierarchy is the Application object. This object represents the current instance of Word. The Application object contains the Document, Selection, Bookmark, and Range objects. Each of these objects has many methods and properties that you can access to manipulate and interact with the object.

Now, in our script, we have first created a word application object by using ActiveXObject. Once the application object is obtained, the document object is created by passing the name of the document (obtained from command line arguments of cscript calling).

Now, this represents the active object of the actual document. This object is capable of parsing as well as manipulating the word document. However, in our use case, we only need to parse the document and write a text file.

This code is very generic, which is used to convert very basic features of a word document like cross-references, lists, subscript texts, bold and italic characters etc. into GFM format. However, you can write your own code converting your customized styles of the word document into the desired format.

You can find the actual typescript code [here](https://github.com/manishbansal8843/word2mdconverter/blob/master/src/word2mdconverter.ts). The code is quite easy to read. Below are few major highlights of it:

1. [First](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L357), a document object is passed to convertDocumentToMarkdown function which returns the text to be written in an MD file.
2. Further, in convertDocumentToMarkdown, methods and properties of the document object are called to find and replace relevant word features with the corresponding GFM language syntax. E.g. first, subscript and bold & italic texts are searched. After that, the text is replaced by GFM specific code. And finally, the word styles are removed. All this is done [here](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L332-L334).
3. After this, cross-references are [replaced](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L336-L338). However, this is tricky. First, the toggleShowCodes function is called. This has a similar impact as alt+F9 in a word document. This replaces all the cross-references in a document with the code. After that, find and replace method is called to find and replace all cross-references with GFM style. Here, “19 REF” is passed as an argument to a function. This is a standard search criterion for finding all cross-references in a word document. At last, after replacing, again the toggleShowCodes function is called to bring back the document to its original form.
4. At last, the writeDocument function is called which does the main job. It reads the document paragraph by paragraph and then, using switch case, looks for the styles of the paragraphs (like if it’s a heading or a table or a list paragraph or an image). Now, depending on the found style, the desired text is written in the MD file.

**A word or two on embedding images:** Embedding images into an MD file is a bit tricky.

First, you need to store the images on your git repository. Then the link has to be given in the MD file for embedding in it. The syntax is ![alt text](path/in/the/repository/image1.jpg).

Now, in order to auto-generate this link for an image while converting word into an MD file, hidden text is created (just after the image without any space) with content as the link itself. And then in the [code](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L258-L263), this hidden text is stripped off and inserted into the MD file.

Now, you might find the actual code to do all this stuff very tedious, but this is all as per the [API](https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word._document?view=word-pia) exposed by the Word application. So do not worry about that. You can definitely refer my code or TypeScript’s original code. Both will be a good starter for your next project.

Oh wait!! That is it. You made it till the end ?. Well, then ? Congratulations! ? And, If you liked this article, please hit that clap ? button below. It would mean a lot to me and it will help other people see the story. Cheers! ?

