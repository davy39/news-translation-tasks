---
title: We need a new document markup language — here is why
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-16T16:39:47.000Z'
originalURL: https://freecodecamp.org/news/we-need-a-new-document-markup-language-c22e0ec44e15
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ge4Z5bQFJwk5AUA8DjHgNQ.png
tags:
- name: documentation
  slug: documentation
- name: markup
  slug: markup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Christian Neumanns

  Introduction: What’s the Problem?

  There are many document markup languages available already. Wikipedia lists over
  70 variations in its List of document markup languages — among them HTML, Markdown,
  Docbook, Asciidoctor, reStruc...'
---

By Christian Neumanns

### Introduction: What’s the Problem?

There are many document markup languages available already. Wikipedia lists over 70 variations in its [List of document markup languages](https://en.wikipedia.org/wiki/List_of_document_markup_languages) — among them HTML, Markdown, Docbook, Asciidoctor, reStructuredText, etc.

Why, then, does the title of this article suggest we need _yet another one_???

What’s the problem?

There are two fundamental problems with the existing document markup languages: Either they are not easy to use, or they are not well suited to write complex documents, such as technical articles, user manuals, or books. An example of “not easy to use, but suited for complex documents” would be Docbook. An example of “easy to use, but not suited for complex documents” would be Markdown.

Of course, the above categorization is simplistic. But it should serve as a good starting point to get the gist of this article which aims to delineate the kind of problems that occur in practice. You’ll see many representative examples of markup code that illustrates what’s wrong, complemented by links to more information.

You’ll also discover a _new_ markup language. Lots of examples will demonstrate how a new syntax can lead to a language that is “easy to use and suited for complex documents”. A _proof-of-concept_ implementation is already available. More on this later.

### Preliminary Remarks

Please note:

* This article is about document markup languages used to write _text documents_, such as books and articles published on the net. There are other markup languages used to describe specific data, such as mathematical formulas, images, and geographic information, but these are out of scope of this article. However, some ideas presented in this article might be applied to other kinds of markup languages as well.
* This article focuses solely on the _syntax_ of markup languages. We will not discuss other aspects that are also important in the choice of a suitable markup language, such as: support on your OS, ease of installation and dependencies, the tool chain available to create final documents, the quality of documentation, price, customer/user support, etc.
* Readers of this article should have some basic experience with a markup language like HTML, Markdown, Asciidoctor, or similar.
* Readers not aware of the _many_ advantages of document markup languages might first want to read:  
[Advantages of Document Markup Languages vs WYSIWYG Editors](https://medium.freecodecamp.org/the-advantages-of-document-markup-languages-vs-wysiwyg-editors-829dc8362219) (Word Processors)

### Inconveniences / Part 1

Let us first consider some well-known markup languages and have a look at some inconveniences.

#### HTML

HTML is the language of the web. So, why not write everything in HTML? The reasons to discard this option are well known. Let’s quickly recapitulate them.

HTML is cumbersome to write. Nobody wants to write XML code by hand, although editors with HTML/XML support might help.

Some frequent writing tasks require non-trivial HTML code.

Suppose we want to display a horizontally centered image with a simple black border and a link. The HTML code an inexperienced user would expect to work could look like this:

```html
<img src="ball.png" align="center" border="yes" link="http://www.example.com/ball">
```

But the code he or she actually has to write is cumbersome and there are different ways to do it. Here is one way:

```html
<div style="text-align: center">
    <a href="http://www.example.com/ball">
        <img src="ball.png" style="border:1px solid black;">
    </a>
</div>
```

HTML lacks “productivity features for writers”, such as:

* Automatic generation of a table of contents, index, glossary, etc.
* Variables used to hold recurring values
* Splitting a document into different files

Other inconveniences will be shown later.

#### Markdown

[Markdown](https://en.wikipedia.org/wiki/Markdown) is a very popular, lightweight markup language. It is easy to learn and use, and well suited for short and simple texts, such as comments in forums, readme files, etc.

However, it suffers from the following problems that make it unsuitable for complex or big documents (e.g. technical articles, user manuals, and books):

* The original Markdown defined by John Gruber lacks many features expected by writers, such as tables (only embedded HTML tables are supported), automatic generation of table of contents, syntax highlighting, file splitting, etc.
* There is no unique, unambiguous specification for Markdown. Many flavors of Markdown exist, with different rules and different features supported. This leads to incompatibility issues when markup code is shared. [CommonMark](https://commonmark.org/) is an attempt to solve this problem. However, the specification is huge and not completed yet (at the time of writing, April 2019, version 0.28, dated 2017–08–01, is the latest one).
* Markdown has similar problems and limitations to those shown later in chapter “Inconveniences / Part 2”. These flaws can quickly become an annoyance when you use Markdown for anything else than short, simple texts.

Here is a list of articles with more information about Markdown’s shortcomings:

* [Why You Shouldn’t Use “Markdown” for Documentation](http://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/)
* [Sundown on Markdown?](https://www.red-gate.com/simple-talk/blogs/sundown-on-markdown/)
* [Why Markdown Is Not My Favourite Language](http://www.wilfred.me.uk/blog/2012/07/30/why-markdown-is-not-my-favourite-language/)

#### Docbook

[Docbook](https://docbook.org/) is an XML-based markup language that uses semantic tags to describe documents.

It has probably the most complete set of features among all markup languages. It has been used by many authors, is pre-installed on some Linux distributions, and is supported by many organizations and publishers. Docbook has been successfully used to create, publish, and print lots of big documents of all kinds.

But it has the following drawbacks:

It uses XML and a verbose syntax. Look at the following example, borrowed from [Wikipedia](https://en.wikipedia.org/wiki/DocBook):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<book xml:id="simple_book" xmlns="http://docbook.org/ns/docbook" version="5.0">
    <title>Very simple book</title>
    <chapter xml:id="chapter_1">
        <title>Chapter 1</title>
        <para>Hello world!</para>
        <para>I hope that your day is proceeding <emphasis>splendidly</emphasis>!</para>
    </chapter>
    <chapter xml:id="chapter_2">
        <title>Chapter 2</title>
        <para>Hello again, world!</para>
    </chapter>
</book>
```

Would you enjoy writing and maintaining such code?

Now compare the above code with the following one, written in a modern markup language like Asciidoctor:

```
= Very simple book

== Chapter 1

Hello world!

I hope that your day is proceeding _splendidly_!

== Chapter 2

Hello again, world!
```

Docbook is also complex, and therefore hard to learn and use.

Output produced by Docbook, especially HTML, looks old-fashioned (see examples on its website). Of course, presentation can be customized, but this is not an easy task.

#### LaTeX

[LaTeX](https://en.wikipedia.org/wiki/LaTeX) is a high-quality typesetting system. It is widely used in academia to create scientific documents. It is considered to be the best option for writing PDF documents containing lots of mathematic formulas and equations.

I never used LaTeX myself, because I don’t write scientific documents — just articles and books to be published on the web. Therefore, I don’t want to comment on it too much. However, it is important to mention it because of its popularity in academia.

LaTeX’s unique syntax seems verbose to me, and a bit complex. Here is an abbreviated example from [Wikipedia](https://en.wikipedia.org/wiki/LaTeX#Example):

```latex
\documentclass{article}
\usepackage{amsmath}
\title{\LaTeX}

\begin{document}
    \maketitle
    \LaTeX{} is a document preparation system ...
    
    % This is a comment
    \begin{align}
        E_0 &= mc^2 \\
        E &= \frac{mc^2}{\sqrt{1-\frac{v^2}{c^2}}}
    \end{align}  
\end{document}
```

The article [Conversion from (La)TeX to HTML](https://texfaq.org/FAQ-LaTeX2HTML) states that converting LaTeX math to HTML is “a challenge”.

Some markup languages allow LaTeX snippets to be embedded in their markup code, which can be very useful if you need the power of LaTeX for maths. There are other options to display maths on the web, such as [Mathjax](https://www.mathjax.org/) or [MathML](https://en.wikipedia.org/wiki/MathML) (an ISO standard and part of HTML5).

### Popular for Big Documents

A impressive number of markup languages have emerged. Many of them use a syntax similar to Markup, and are therefore easy to learn and use. Some have more features than Markdown and are even extensible. However, as soon as we start writing complex documents, corner-cases and limits diminish the initial joy of using them.

Two popular markup languages used for big documents are Asciidoctor (an improved version of [Asciidoc](https://en.wikipedia.org/wiki/AsciiDoc)), and [reStructuredText](https://en.wikipedia.org/wiki/ReStructuredText) (an improved version of StructuredText). We will have a look at them soon.

### Practical Markup Language (PML)

Before moving on to the most interesting part of this article, let me briefly introduce the new markup language I mentioned already in the introduction.

The language is called **_Practical_** _Markup Language (PML)_.

> “fitting the needs of a particular situation in a helpful way; helping to solve a problem or difficulty; effective or suitable”

> _— definition of ‘practical’ in the Cambridge Dictionary_

I started the [PML project](http://www.practical-programming.org/pml/index.html) a few months ago because I couldn’t find a markup language that was easy to use _and_ well suited for big, complex documents, such as a user manual.

In the next section we’ll look at examples of markup code written in PML, compared to code written in other languages. So let’s first mention two basic PML syntax rules needed to understand the upcoming examples.

A PML document is a tree of nodes (similar to an XML/XHTML document). Each node starts with a `{`, followed by a tag name. Each node ends with a `}`. A node can contain text or child nodes.

For example, here is a node containing text that will be rendered in italics:

```
{i bright}
```

This node starts with `{i` , and ends with `}`. `i` is the tag name. In this case `i` is an abbreviation for `italic`, which means that the node's content will be rendered in _italics_. The content of this node is the text `bright`. The above PML markup code will be rendered as:  
 _bright_

Some nodes have attributes, used to specify additional properties of the node (besides its tag name).

For example, the title of a chapter is defined with attribute `title`, as follows:

```
{chapter title=A Nice Surprise
    Once upon a time ...
}
```

There is not much more to say about the basic concept of PML syntax. For more insight, and a description of features not used in this article, please consult the [PML User Manual](http://www.practical-programming.org/pml/docs/User_Manual/PML_User_Manual.html).

You can download and play around with a free implementation of PML. But please note: PML is a _work in progress_. There are missing features, you might encounter bugs, and backwards compatibility is currently not guaranteed.

I use PML myself to write all my web documents, such as this article. For links to more real-life examples please visit the [FAQ](http://www.practical-programming.org/pml/about/faq.html#examples).

### Inconveniences / Part 2

I this section we’ll look at examples that reveal _some_ problems encountered with markup languages. This is by no means an exhaustive enumeration of all troubles and corner cases. The aim is to just show a few examples that demonstrate the kind of inconveniences and limits encountered in the real world.

For each example the markup code will be shown in [HTML](https://www.w3.org/TR/html/), [Asciidoctor](https://asciidoctor.org/), [reStructuredText](http://docutils.sourceforge.net/rst.html), and [PML](http://www.practical-programming.org/pml/).

If you want to try out some code, you can use the following online testers (no need to install anything on your PC):

* [HTML](https://www.w3schools.com/tryit/)
* [Asciidoctor](https://asciidoclive.com)
* [reStructuredText](http://rst.ninjs.org)

An online tester for PML is not yet available. You have to install PML on a Windows PC if you want to try it out.

### Font Styles

Font styles (_italic_, **bold**, `monospace`, etc.) are often used in all kinds of documents, so good support is essential.

But as we will see, surprises and limits can emerge, as soon as we have to deal with non-trivial cases. Let’s look at _some_ examples to illustrate this.

### Part of a Sentence in Italics

Suppose we want to write:  
 They called it _Harmonic States_, a good name.

This is a trivial case, and all languages support it.

**HTML**:

```
They called it <i>Harmonic States</i>, a good name.
```

**Asciidoctor**:

```
They called it _Harmonic States_, a good name.
```

**reStructuredText**:

```
They called it *Harmonic States*, a good name.
```

**PML**:

```
They called it {i Harmonic States}, a good name.
```

### Part of a Word in Italics

We want to write:  
 She _un_wrapped the challenge first.

**HTML**:

```
She <i>un</i>wrapped the challenge first.
```

**Asciidoctor**:

```
She __un__wrapped the challenge first.
```

Note that we have to use two underscores. Using a single underscore (as in the first example), would result in:  
 She _un_wrapped the challenge first.

**reStructuredText**:

```
She *un*\wrapped the challenge first.
```

Note that the letter w has to be escaped (preceded by a backslash) for reasons explained [here](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#character-level-inline-markup). If the letter is not escaped then a warning is displayed and the result is:  
 She *un*wrapped the challenge first.

**PML**:

```
She {i un}wrapped the challenge first.
```

### Text in Bold And Italic

We want to write:  
 They were all **_totally flabbergasted_**.

**HTML**:

```
They were all <b><i>totally flabbergasted</i></b>.
```

**Asciidoctor**:

```
They were all *_totally flabbergasted_*.
```

**reStructuredText:**

Combining bold and italic is not supported in reStructuredText, but there are some [complicated workarounds](https://stackoverflow.com/questions/11984652/bold-italic-in-restructuredtext).

**PML:**

```
They were all {b {i totally flabbergasted}}.
```

### Real-Life Example

Here is an example inspired by an Asciidoctor user who [asked](https://github.com/asciidoctor/asciidoctor/issues/2020) how to display:  
 **_id** _optional_.

Let’s make the exercise a little bit more interesting by also displaying:  
 __id_ **optional**.

**HTML**:

```
<b>_id</b> <i>optional</i>
<i>_id</i> <b>optional</b>
```

No surprise here. It just works as expected.

**Asciidoctor:**

Intuitive attempt:

```
*_id* _optional_
__id_ *optional*
```

The first line doesn’t work, it produces:  
 **_id_** __optional_

However, the second line works, which is a bit counterintuitive.

If normal text includes a character that is also used for markup (in our case the `_` preceding `id`), then the character must be escaped. This is a fundamental rule in pretty much all markup languages. For example in HTML a `&`lt; must be escaped wi`th &`lt;. Many languages (including Asciidoctor and PML) use a backslash prefix (e.`g.` \r) to escape. So let's rewrite the code:

```
*\_id* _optional_
_\_id_ *optional*
```

This doesn’t work in Asciidoctor. It produces  
 **_id** _optional_  
and  
\_id **optional**

Here is a correct version, as suggested in an answer to the user’s question:

```
*pass:[_]id* _optional_
_pass:[_]id_ *optional*
```

Another answer suggests this solution:

```
*_id* __optional__
___id__ *optional*
```

More edge case are documented in chapters [Unconstrained formatting edge cases](https://asciidoctor.org/docs/user-manual/#unconstrained-formatting-edge-cases) and [Escaping unconstrained quotes](https://asciidoctor.org/docs/user-manual/#escaping-unconstrained-quotes) of the Asciidoctor User Manual.

**reStructuredText:**

```
**_id** *optional*
*_id* **optional**
```

There is no problem here, because the character `_` is not used in reStructuredText to define markup.

However, suppose we wanted to write:  
 _*id*_ ***optional***.

Here is the code:

```
*\*id\** ***optional***
```

Note that the `*`s in `id` must be escaped, but the `*`s in `optional` don't need to be escaped.

**PML:**

```
{b _id} {i optional}
{i _id} {b optional}
```

### Nested Font Styles

Nested font styles of the same kind (e.g. `<i>...<i>..`.</i>...</i>) occur rarely in text written by humans, but they could be more or less frequent in auto-generated markup code. If they are not supported then the tool that generates the markup code becomes more complicated to implement, because it must track the font styles that are active already, in order to avoid nesting them.

So, how is this supported in the different languages?

**HTML:**

```
<i>This is <i>excellent</i&gt;, isn't it?</i>
```

No problem, it produces  
_This is excellent, isn’t it?_

**Asciidoctor:**

```
_This is _excellent_, isn't it?_
```

The above code is obviously ambiguous: Are the italics nested or do we want to italicize “This is “ and “, isn’t it?”. When I tested it, the result was neither of it:  
_This is _excellent_, isn’t it?_

As far as I now, Asciidoctor doesn’t support nested font styles of the same kind.

**reStructuredText:**

The reStructuredText specification [states](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#inline-markup): “Inline markup cannot be nested.” However, no error is displayed if it _is_ nested, and the result is unspecified.

**PML:**

```
{i This is {i excellent}, isn't it?}
```

Font styles of the same kind can be nested in PML. The above code results in:  
_This is excellent, isn’t it?_

### Nested Chapters

Suppose we are writing an article titled “New Awesome Product” that contains four chapters. The structure looks as follows:

```
New Awesome Product
    Introduction
    More features
    Faster
    Less resources
```

Later on we decide to insert chapter “Advantages” as a parent of the three last chapters. The structure now becomes:

```
New Awesome Product
    Introduction
    Advantages
        More features
        Faster
        Less resources
```

What are the _changes_ required in the markup code to pass from version 1 to version 2? Can we simply insert the code for a new chapter? Let’s see.

**HTML:**

![Image](https://cdn-media-1.freecodecamp.org/images/PoEYqgtazrmE2KEXHHEdSVyBd1XCISQurRxT)

Note: Code _changes_ are displayed in bold.

As shown above, besides inserting the new chapter, we have to change the markup for the three child chapters: `h2` must be changed to `h3`.

**Asciidoctor:**

![Image](https://cdn-media-1.freecodecamp.org/images/h6RYuEiJ5YHGqr6yjJ7UKEivRxOfhNKbc9Fs)

Again, we have to change the markup for the three child chapters: `==` must be changed to `===`

Note: The blank lines between the chapters are required, otherwise the document is not rendered correctly.

**reStructuredText:**

![Image](https://cdn-media-1.freecodecamp.org/images/iLno1NIDCRQW-AtE7E1R-Bp6lToSFfbQETlj)

The markup for the three child chapters must be changed: All occurrences of `=` must be changed to `-`

The non-trivial rules for reStructuredText’s sections can be looked up [here](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#sections).

**PML:**

![Image](https://cdn-media-1.freecodecamp.org/images/-z7E6Sv0f4-ZPQlj9ldRKMTiFLdzBjbjNCTF)

In PML, there is no need to change the code of the three child chapters.

**Bottom Line:**

In all languages, except PML, the markup code of all child chapters must be adapted if a parent chapter is inserted.

This is not a deal-breaker in case of small articles with few chapters. But image you are writing your next big article or book with lots of chapters and frequent changes. Now, the necessity to manually update child chapters can quickly turn into a daunting, boring, and error-prone task.

Note: Asciidoctor provides a `leveloffset` variable that can be used to change the level of chapters. This might be useful in some cases, but it also creates additional unneeded complexity, as can be seen [here](https://github.com/asciidoctor/asciidoctor/issues/530) and [here](https://github.com/asciidoctor/asciidoctor/issues/1616).

A more serious kind of problem can arise in the following situation: Imagine a set of different documents that share some common chapters. To avoid code duplication, the common chapters are stored in different files, and an `insert file` directive is used in the main documents. This works fine as long as the levels of all common chapters are the same in all documents. But troubles emerge if this is not the case.

It is also worth to mention that HTML, Asciidoctor and reStructuredText don’t protect us against wrong chapter hierarchies. For example, you don’t get a warning or error if a chapter of level 2 contains a direct child chapter of level 4.

In a language like PML, the above problems simply don’t exist, because the level is not specified in the markup code. All chapters (of any level) are defined with the same, unique syntax. The chapters’ tree structure (i.e. the level of each chapter) is automatically defined by the parser. And wrong hierarchies in the markup code, such as a missing `}` to close a chapter, are flagged by an error message.

### Lists

In Asciidoctor the kind of problems we have seen with chapter hierarchies can also arise with list hierarchies (e.g. lists that contain lists). The reason is the same as for chapters: [Asciidoctor lists](https://asciidoctor.org/docs/user-manual/#nested) use different markup code to explicitly specify the level of list items (`*` for level 1, `**` for level 2, etc.). Moreover, there are a number of complications you have to be aware of when working with [complex list content](https://asciidoctor.org/docs/user-manual/#complex-list-content).

In reStructuredText, [nested lists](https://stackoverflow.com/questions/5550089/how-to-create-a-nested-list-in-restructuredtext) are created using indentation and blank lines. This works fine for simple nested lists, but creates other problems in more complex cases (not discussed here). Using whitespace (e.g. blank lines and indentation) to define structure in markup code is a bad idea, as we’ll see soon.

In HTML and PML, the above problems don’t exist with lists because the syntax for parent- and child nodes is the same.

### Whitespace And Indentation

At first, using whitespace to define structure seams like a good idea. Look at the following example:

```
parent
    child 1
    child 2
```

The structure is very easy to read _and_ write. No noisy special markup characters are needed.

It is therefore tempting for markup language designers to use whitespace as a simple way to define structure. Unfortunately, this works well only for simple structures, and has other inconveniences we’ll see soon.

Therefore, a simple, but important rule must be applied in markup languages designed to work well with complex content:

> “Whitespace doesn’t change the structure or semantics of the document.”  
>   
> _— whitespace-insignificant-rule_

What does this mean?

First, let us define _whitespace_: Whitespace is any set of one or more consecutive spaces, tabs, new lines, and other Unicode characters that represent space.

In our context, the above rule means that:

Within text, a set of _several_ (i.e. more than one) whitespace characters is treated the same as a _single_ space character.

For example, this code:

```
a beautiful
    flower
```

… is identical to this one:

```
a beautiful flower
```

Between structural elements, a set of whitespace characters is insignificant.

For example, this code:

```
<table>

    <tr>
```

… is identical to this one:

```
<table><tr>
```

A special case of whitespace is _indentation_ (leading whitespace at the beginning of a line). The above rule implies that indentation is insignificant too. Indentation doesn’t change the result of the final document.

Applying the _whitespace-insignificant_ rule is important, because it leads to significant advantages:

* There is no need to learn, apply and worry about complex whitespace rules (see examples below).  
Violating the _whitespace-insignificant_ rule in a markup specification adds unneeded complexity, and can lead to markup code that is ugly, error-prone, and difficult to maintain, especially in the case of nested lists.
* Whitespace can freely be used by authors to format the markup code in a more understandable, presentable and attractive way (pretty printing). For example, lists (and lists of lists) can be indented to display their structure in a visually clear and maintainable way, without the risk of changing the underlying structure.
* Text blocks can be copy/pasted without the need to adapt whitespace.
* If shared text blocks (stored in different files) are imported into several documents with different structures, there is no risk of changing or breaking the structure.
* There is no unexpected or obscure behavior if the whitespace is not visible for human readers. Some examples:  
- a mixture of whitespace characters, such as spaces and tabs, especially when used to indent code  
- whitespace at the end of a line  
- whitespace in empty lines  
- visually impaired (blind) people who can’t read whitespace  
Note: To alleviate the pain, some editors provide a _display-whitespace_ mode.
* Tools that generate markup code, as well as markup parsers are generally easier to create.
* In some situations it is useful to reduce whitespace to a minimum (e.g. no new lines), in order to save storage space and improve performance.

If you want a few examples demonstrating the kind of technical problems that arise if whitespace is significant, you can read:

* [What are the downsides to whitespace indentation rather than requiring curly braces?](https://www.quora.com/What-are-the-downsides-to-whitespace-indentation-rather-than-requiring-curly-braces)
* [F# syntax: indentation and verbosity](https://fsharpforfunandprofit.com/posts/fsharp-syntax/)
* [Issue in nodeca/js-yaml](https://github.com/nodeca/js-yaml/issues/80)

So, how is whitespace handled in the languages we are discussing in this article?

**HTML:**

HTML applies the _whitespace-insignificant_ rule.

For a thorough explanation, look at this excellent article written by Patrick Brosset: [When does white space matter in HTML?](https://medium.com/@patrickbrosset/when-does-white-space-matter-in-html-b90e8a7cdd33).

**Asciidoctor:**

In Asciidoctor, whitespace is significant in some cases.

This can lead to surprising behavior and problems with no easy or no satisfying solution. Some examples can be seen [here](https://github.com/asciidoctor/asciidoctor/issues/686) and [here](https://github.com/asciidoctor/asciidoctor/issues/623).

**reStructuredText:**

reStructuredText has whitespace rules that are ‘a bit surprising’.

For example, writing `*very*` results in _very_ (text in italics, as expected). However, `* very*` results in * very* (no italics!), because of the whitespace preceding "very". To understand why, the answer might be found in chapter [Whitespace](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#whitespace) of the specification.

**PML:**

Similar to HTML, PML applies the _whitespace-insignificant_ rule.

There is one exception: For practical reasons, a blank line between two text blocks results in a paragraph break. This means that instead of writing:

```
{p text of paragraph 1}
{p text of paragraph 2}
```

… we can simply write:

```
text of paragraph 1

text of paragraph 2
```

Note: Sometimes, whitespace _is_ significant in text. For example whitespace must be preserved in source code examples. Or, in verbatim text, several consecutive spaces or new lines must be preserved in the final document. All languages support this. However, in reStructuredText it’s not always obvious how to it, as shown [here](https://stackoverflow.com/questions/51198270/how-do-i-create-a-new-line-with-restructuredtext).

### Other Inconveniences

As seen already, some markup languages systematically use opening and closing tags. An example would be `<`;i>`; an`d </i> in HTML. All XML-based languages, as well as PML belong to this class of languages.

Without digging into details, here are some drawbacks that can occur in languages that do _not_ (or not always) use pairs of distinct opening/closing tags (e.g. Markdown, Asciidoctor, and reStructuredText):

**Editor support**  
Creating good, reliable editor support is more difficult to develop. Examples of useful editor features are:

* syntax highlighting for markup code
* markup code completion
* visualizing pairs of block start/end marks (e.g. `{` and its corresponding `}`)
* block collapsing/expanding  
In the case of languages that use distinct opening/closing tags, the two last features work out-of-the-box in some editors. For example, PML uses `{` and `}` for node boundaries. This is also used in many programming languages (C, Java, Javascript, etc.) and therefore block features implemented for programming languages will also work for PML.

**Document validation**  
Fewer syntax and structure errors can be detected automatically. This can lead to more time spent on debugging documents. Or, even worse, there might be silently ignored errors that end up in wrong output (Did I really fail to spot the missing warning block on page 267 of my 310 pages book?).

**Parsers**  
It is more difficult to create parsers (i.e. programs that read markup code) that work well in all cases. If different parsers read the same markup code, there is an increased risk of getting different results for corner-cases.

**Auto-generated markup code**  
Tools that generate markup code programmatically are more difficult to create. For example, if whitespace is significant, or font styles cannot be nested, then additional state must be updated and tracked, in order to respect these rules.

### My Own Experience

When I started writing technical documents a few years ago, I used Docbook. It took me some time to learn it, but after that I never stumbled on anything I couldn’t do. Docbook is powerful. However, I disliked typing verbose XML code. I tried some XML editors, but gave up. Finally I just wrote complete text blocks unformatted in Notepad++, and then adorned the text with the necessary markup code. It was frustrating and time-consuming. Moreover, I couldn’t find a stylesheet that produced good-looking web documents, and I didn’t have the patience, motivation, and experience to fiddle around with big, complex CSS files and adapt them.

Later on I discovered Asciidoctor. What a relief. Everything was so much simpler and the web documents were beautiful, out of the box. Asciidoctor’s documentation is great, and I think the community is helpful and active. However, when I started to write more complex and bigger documents, I had to deal with problems similar to those described in the previous sections. At one point, I had to develop a specific pre- and post-processor to solve a problem for which I couldn’t find a solution in Asciidoctor/Gitbook.

An intriguing question emerged: “Why do these problems not exist in Docbook?”.

To make a long story short, I concluded that we need a new markup syntax. The key points to success would be:

* easy to learn: few, simple, consistent and predictable rules (no exceptions)
* easy to write and read
* well-structured documents with no ambiguities
* powerful enough to create big, complex documents without the need for “special rules, tricks, or workarounds”

After a period of investigating, pondering, programming, testing and improving, the [Practical Markup Language (PML)](http://www.practical-programming.org/pml/index.html) was born. Since then, I never looked back again. Today I write all my web documents in PML (including this article).

Of course, when I started to create PML, it was to cover my own needs. So, I am probably biased. Hopefully this article contains enough factual examples, but I encourage you to leave a comment if you see anything wrong, unfair, or missing. I appreciate constructive feedback of any kind, and I will update the article if needed.

### Conclusion

As demonstrated in this article, a good number of problems encountered with existing document markup languages vanish with the PML syntax.

Now we should come together to improve PML and make it more powerful, so that it covers more use cases and more people can benefit from it.

Please help to spread the word. Or try out PML and send feedback, so that we know what needs to be refined. Your voice counts!

The vision is to create the best possible document markup language and all necessary tools, so that writers can focus on writing and enjoy creating beautiful documents in a minimum of time — without worrying about unneeded complexity.

