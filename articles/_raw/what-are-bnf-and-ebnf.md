---
title: What are BNF and EBNF in Programming?
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2023-07-17T17:26:21.000Z'
originalURL: https://freecodecamp.org/news/what-are-bnf-and-ebnf
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/ryan-wallace-azA1hLbjBBo-unsplash.jpg
tags:
- name: programming languages
  slug: programming-languages
- name: syntax
  slug: syntax
seo_title: null
seo_desc: 'As programmers, we communicate with computers through many languages: Python,
  JavaScript, SQL, C... you name it. But do you know how the creators of these languages
  precisely describe their syntax to us, leaving no room for doubt?

  They could''ve relie...'
---

As programmers, we communicate with computers through many languages: Python, JavaScript, SQL, C... you name it. But do you know how the creators of these languages precisely describe their syntax to us, leaving no room for doubt?

They could've relied on plain English, but that would not be a good solution because of the potential verbosity and ambiguity. So they used specially designed languages for it. 

In this article, you'll learn about two of these widely used languages: BNF and EBNF.

Another fascinating aspect of these special languages or notations is that you can write the grammar of your own language using them and give it as input to some magical computer programs called "parser generators". These can output other programs capable of parsing any text according to the grammar you used. How amazing is that? 

This feature can save you a lot of time since manually writing such programs is challenging and time-consuming.

Before learning (E)BNF, it's helpful to be able to distinguish between syntax and semantics. So let's start from there.

## Syntax vs Semantics in Programming Languages

Syntax refers to the structure of the elements of a language based on its type. On the other hand, semantics are all about the meaning.

Something written syntactically correctly in a language can be completely meaningless. And no text can be meaningful if its syntax is incorrect.

Two of the most famous sentences regarding syntax and semantics are [composed by Noam Chomsky](https://en.wikipedia.org/wiki/Colorless_green_ideas_sleep_furiously):

1. Colorless green ideas sleep furiously.
2. Furiously sleep ideas green colorless.

The first sentence's syntax is correct but it's meaningless. And since the second one is syntactically wrong, it is far from being meaningful.

The same is true for programming languages too. Let's look at the following two JavaScript code snippets to see what I mean.

The following code is syntactically correct but semantically wrong because it's not possible to reassign something to a constant variable:

```js
const name = "Palash";
name = "Akash";

```

The following is syntactically incorrect and thus does not even have any chance to be semantically correct.

```js
"Palash" = const name;
"Akash" = name;

```

You check the syntax of your JavaScript code online with a tool like the [Esprima Syntax Validator](https://esprima.org/demo/validate.html).

There are two more concepts you need to understand before learning to read BNF/EBNF.

## Terminals and Non-Terminals

BNF/EBNF is usually used to specify the grammar of a language. Grammar is a set of _rules_ (also called _production rules_). Here language refers to nothing but a set of strings that are valid according to the rules of its grammar.

A BNF/EBNF grammar description is an unordered list of rules. _Rules_ are used to define _symbols_ with the help of other symbols.

You can think of _symbols_ as the building blocks of grammar. There are two kinds of symbols:

* **Terminal (or Terminal symbol)**: Terminals are strings written within quotes. They are meant to be used as they are. Nothing is hidden behind them. For example `"freeCodeCamp"` or `"firefly"`.
* **Non-terminal (or Non-terminal symbol)**: Sometimes we need a name to refer to something else. These are called _non-terminals_. In BNF, _non-terminal_ names are written within angle brackets (for example `<statement>`), while in EBNF they don't usually use brackets (for example `statement`).

The whole language is derived from a single _non-terminal_ symbol. This is called the **start** or **root** **symbol** of the grammar. By convention, it is written as the first non-terminal in the BNF/EBNF grammar description.

Finally, you are ready to learn BNF. It's easier than you might think it is.

## What is BNF?

BNF stands for **B**ackus–**N**aur **F**orm which resulted primarily from the contributions of [John Backus](https://en.wikipedia.org/wiki/John_Backus) and [Peter Naur](https://en.wikipedia.org/wiki/Peter_Naur).

The syntax of BNF/EBNF is so simple that many people adopted their styles. So in different places, you will most likely see different styles. If the syntax is different from conventional ones, that's usually documented there. In this article I will use one particular style, just to keep things simple.

Below is an example of a simple _production rule_ in BNF:

```bnf
<something> ::= "content" 

```

Each rule in BNF (also in ENBF) has three parts:

* **Left-hand side**: Here we write a non-terminal to define it. In the above example, it is `<something>`.
* **`::=`**: This character group separates the **Left hand side** from **Right hand side**. Read this symbol as "is defined as".
* **Right-hand side**: The definition of the non-terminal specified on the right-hand side. In the above example, it's `"content"`.

The above `<something>` is just one thing fixed thing. Let's now see all the ways you can compose a _non-terminal_.

### How to compose a non-terminal

BNF offers two methods to us:

* Sequencing
* Choice

You can just write a combination of one or more terminals or non-terminals in a sequence and the result is their concatenation, with non-terminals being replaced by their content. For example, you can express your breakfast in the following ways:

```bnf
<breakfast> ::= <drink> " and biscuit"
<drink> ::= "tea"

```

It means the only option for breakfast for you is `"tea and biscuit"`. Note that here, the order of symbols is important.

Let's say someday you want to drink coffee instead of tea. In this case, you can express your possible breakfast items like below:

```bnf
<breakfast> ::= <drink> " and biscuit"
<drink> ::= "tea" | "coffee"

```

The `|` operator indicates that the parts separated by it are choices. Which means the non-terminal on the left can be any such part. Here the order is _unimportant_, that is there is no difference between `"tea" | "coffee` and `"coffee" | "tea"`.

That is really all you need to know about BNF to read and understand it and even express the syntax of your own language using it. Believe it or not, it's that simple. And yet it can be used to describe the syntax of many programming languages and other kinds of coding languages.

The thing that makes it possible to break down complex syntax programming languages easily is the ability to define non-terminal symbols recursively. 

As a simple example let's see how you express one or more digits in BNF:

```bnf
<digits> ::= <digit> | <digit> <digits>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

```

If you want to see a simple real-world example of BNF grammar checkout: [Semver notation](https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions).

## What is EBNF?

BNF is fine, but sometimes it can become verbose and hard to interpret. EBNF (which stands for **E**xtended **B**ackus–**N**aur **F**orm) may help you in those cases. For example, the previous example can be written in EBNF like below:

```ebnf
digits = digit { digit }
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

```

The braces above mean that its inner part may be repeated 0 or more times. It frees your mind from getting lost in recursion.

One interesting fact is that everything you can express in EBNF can also be expressed in BNF.

EBNF usually uses a slightly different notation than BNF. For example:

* `::=` becomes just `=`.
* There are no angle brackets around non-terminals.

```ad-info
For concatenation, instead of juxtaposition, some prefer `,` to be more explicit. However, I will not use it here.

```

Don't assume that these styles to be universal. There are several variants of them and they are usually clear from the context. The more important thing to focus on is the new operations it offers like the braces we've seen above.

EBNF extends BNF by adding the following 3 operations:

* Option
* Repetition
* Grouping

### Option

Option uses square brackets to make the inner content optional. Example:

```ebnf
thing = "water" [ "melon" ]

```

So the above `thing` is either `water` or `watermelon`.

### Repetition

Curly braces indicate the inner content may be repeated 0 or more times. You have already seen a good example of it above. Below is a very simple one just to make the idea solid in your mind:

```ebnf
long_google = "Goo" { "o" } "gle"

```

So `"Google"`, `"Gooogle"`, `"Gooooooogle"` are all valid `long_google` non-terminal.

### Grouping

Parentheses can be used to indicate grouping. It means everything they wrap can be replaced with any of the valid strings that the contents of the group represent according to the rules of EBNF. For example:

```ebnf
fly = ("fire" | "fruit") "fly"

```

Here  `fly` is either `"firefly"` or `"fruitfly"`.

With BNF we could not do that in one line. It would look like the following in BNF:

```ebnf
<fly> ::= <type> "fly"
<type> ::= "fire" | "fruit"

```

## The BNF Playground

There is a very nice online playground for BNF and EBNF: [<BNF> Playground](https://bnfplayground.pauliankline.com/).

I recommend you check it out and play with it. It uses a slightly different notation so read the "Grammar Help" section beforehand.

It can test if a string is valid according to the grammar you entered. It can also generate random strings based on your grammar!

For fun this is the syntax of a poem-like text (credit goes to chatGPT):

```ebnf
<poem> ::= <line> | <line> "\n" <poem>
<line> ::= <noun_phrase> " " <verb_phrase> " " <adjective>
<noun_phrase> ::= "the " <adjective> " " <noun> | <noun>
<verb_phrase> ::= <verb> | <verb> " " <adverb>
<adjective> ::= "red" | "blue" | "green" | "yellow"
<noun> ::= "sky" | "sun" | "grass" | "flower"
<verb> ::= "shines" | "glows" | "grows" | "blooms"
<adverb> ::= "brightly" | "slowly" | "vividly" | "peacefully"

```

Go ahead and copy-paste it into the playground and press the "Generate Random" button to get some mostly meaningless lines of a grammatically correct poem.

## Conclusion

BNF and EBNF are simple and powerful notations to write what computer scientists call _context-free grammar_. 

In simple terms it means the expansion of a non-terminal is not dependent on the context (surrounding symbols), that is it's context-free. It is the most widely used grammar form to formalize the syntax of coding languages.

Here are some resources you might find interesting:

- [EBNF: How to Describe the Grammar of a Language](https://tomassetti.me/ebnf/)
- [The language of languages](https://matt.might.net/articles/grammars-bnf-ebnf/)
- Parser generators:
  - [ANTLR](https://www.antlr.org/), a very powerful parser generator capable of writing parsers in many languages.
  - If you are a JavaScript person like me and want to get started with a parser generator, take a look at [nearly.js](https://nearley.js.org/) for a gentle start.

Below are some real-world grammars written using BNF/EBNF or similar notations that you might find interesting:

* [Lisp](https://iamwilhelm.github.io/bnf-examples/lisp)
* [Lua](https://www.lua.org/manual/5.4/manual.html#9)
* [Semver](https://semver.org/#backusnaur-form-grammar-for-valid-semver-versions)
* [JavaScript](https://tc39.es/ecma262/multipage/grammar-summary.html#sec-grammar-summary)
* [JSX](https://facebook.github.io/jsx/)
* [Python](https://docs.python.org/3/reference/grammar.html)
* [Value Definition Syntax in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Value_definition_syntax)

Thanks for reading. Let me know on [Twitter](https://twitter.com/ashutoshbw) if you have any questions or found this article helpful. Happy learning!

Photo by [Ryan Wallace](https://unsplash.com/@accrualbowtie?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/azA1hLbjBBo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

