---
title: 'Beyond regular expressions: An introduction to parsing context-free grammars'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T19:12:10.000Z'
originalURL: https://freecodecamp.org/news/beyond-regular-expressions-an-introduction-to-parsing-context-free-grammars-ee77bdab5a92
coverImage: https://cdn-media-1.freecodecamp.org/images/0*yyZM9V_77Q-uAj0F
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Christopher Diggins

  An important and useful tool that is already a part of most programmers’ arsenals
  is the trusty regular expression. But beyond that lie context-free grammars. This
  is a simple concept with a fancy name.

  A regular expression is ...'
---

By Christopher Diggins

An important and useful tool that is already a part of most programmers’ arsenals is the trusty [**regular expression**](https://en.wikipedia.org/wiki/Regular_expression)**.** But beyond that lie context-free grammars. This is a simple concept with a fancy name.

A regular expression is a method of validating and finding patterns in text. The kinds of patterns (aka grammars) that can be described and detected using a regular expression are called [**regular languages**](https://en.wikipedia.org/wiki/Regular_language). Regular languages are the simplest of formal languages in the [**Chomsky hierarchy**](https://en.wikipedia.org/wiki/Chomsky_hierarchy).

Regular expressions are great for finding or validating many types of simple patterns, for example phone numbers, email addresses, and URLs. However, they fall short when applied to patterns that can have a recursive structure, such as:

* HTML / XML open/close tags
* open/close braces {/} in programming languages
* open/close parentheses in arithmetical expressions

To parse these types of patterns, we need something more powerful. We can move to the next level of formal grammars called [**context free grammars**](https://en.wikipedia.org/wiki/Context-free_grammar) (CFG).

### Parsing mathematical expressions

Parsing the set of all mathematical expressions is beyond the power of a true regular expression. The reason is that these can contain arbitrarily deep nested pairs of parentheses.

For example, consider the expression: `(2 + (3 * (7–4)))`

Notice that the structure of the arithmetical expression is effectively a tree:

```
  + / \ 2   *   / \  3   -     / \     7 4
```

The tree structure generated as the result of running a CFG parser is called a [**parse tree**](https://en.wikipedia.org/wiki/Parse_tree).

### Describing context-free grammars

There are two popular methods of expressing CFG grammars:

1. [Extended Bachus-Naur Form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) (EBNF) — describes a CFG in terms of **production rules**. These are rules that, when applied, can generate all possible legal phrases in the language.
2. [Parsing Expression Grammar](https://en.wikipedia.org/wiki/Parsing_expression_grammar) (PEG) — describes a CFG in terms of **recognition rules**. These are rules that can be used to match valid phrases in the language.

The PEG formalism has the advantage over EBNF that the mapping to a parser is unambiguous, and can be easily automated.

The following is a simple PEG [lifted from its Wikipedia](https://en.wikipedia.org/wiki/Parsing_expression_grammar) page describing mathematical formulas that apply the basic four operations to non-negative   
integers.

```
Expr ← SumSum ← Product ((‘+’ / ‘-’) Product)*Product ← Value ((‘*’ / ‘/’) Value)*Value ← [0–9]+ / ‘(‘ Expr ‘)’
```

In plain English, we can read this as:

* `Expr` is a `Sum`
* `Sum` is a `Product` followed by zero or more sub-patterns that consist of a “+” or “-” followed by a `Product`
* `Product` is a `Value` followed by zero or more sub-patterns that consist of a “*” or “/” followed by a `Value`
* `Value` is either one or more members of the character set {0,..9}, or it is an open parenthesis “(“ followed by a `Expr` and a closing parenthesis “)”.

### Parser generators versus parsing libraries

Assuming you aren’t the type of person who likes to reinvent the wheel (not that there is anything wrong with that), there are generally two options for creating a parser:

1. **Use a parser generator** — a tool that generates the source code for a parser from an abstract definition of the parser. Some popular examples in JavaScript include [Jison](http://jison.org/), [PEG.js](https://pegjs.org/), [nearley](http://nearley.js.org/), and [ANTLR](http://www.antlr.org/).

2. **Use a parsing library** — a library that allows the expression of the parse rules as an API. Some examples in JavaScript include [Myna](https://github.com/cdiggins/myna-parser), [Parsimmon](https://github.com/jneen/parsimmon), and [Chevrotain](https://github.com/SAP/chevrotain).

My preference is to use parsing libraries, because they are easier to understand, debug, maintain, and customize.

### Writing parsers in TypeScript / JavaScript using the [Myna Parsing Library](https://github.com/cdiggins/myna-parser)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YvovmmxWoIEpHKQ1Fu6cxw.png)
_Common Myna b[y Mahesh Iyer from Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Common_Myna.svg" rel="noopener" target="_blank" title=")_

Recently, a project I was working on ([the Heron language](https://github.com/cdiggins/heron-language/)) required a parsing library that could run in the browser. I found the complexity and overhead of existing libraries too great. Given I had previous experience in writing parsing libraries in C++ and C#, I decided to write a [parser library called **Myna** using TypeScript](https://github.com/cdiggins/myna-parser).

Myna uses [fluent syntax (method chaining)](https://en.wikipedia.org/wiki/Fluent_interface) to make it easy to define a parser as a set of rules (sub-parser) that resemble a PEG grammar.

The following example is [from the Myna GitHub repo](https://github.com/cdiggins/myna-parser/blob/master/grammars/grammar_arithmetic.js):

### From concrete syntax tree (CST) to abstract syntax tree (AST)

When a parser processes the input, each successfully matched rule (aka grammar production) can be mapped to a node in the parse tree. This literal mapping of production rules to nodes in a tree is a **concrete syntax tree** (CST).

In some cases, the CST is of limited use as it contains a lot of syntactic clutter, for example comments in the source code, or whether a string literal has double quotes or single quotes. It may contain results from rules that are created to make the grammar easier to use, but don’t represent the intended tree structure for analysis.

The simplest thing to do is to only create nodes in the output tree for specific rules and to skip other rules. This simplified version of the parse tree is called an [**abstract syntax tree**](https://en.wikipedia.org/wiki/Abstract_syntax_tree) **(AST)**. There may be multiple passes performed on an AST to transform it into alternative AST representations, to simplify later processing steps.

In Myna, an AST is generated by creating nodes from rules labeled with the `ast` property. Technically, this property returns a new rule that has an internal property set that tells the parser to generate a parse node in the parse tree.

### Using the generated Myna abstract syntax tree

Here is an example of using a Myna-defined parser in “Node.JS” to evaluate an arithmetical expression:

### Final words

If you are interested in learning more about creating and using parsers, whether or not the Myna library meets your specific needs, I encourage you to take a bit of time to read through the [source code of the Myna parsing library](https://github.com/cdiggins/myna-parser/blob/master/myna.ts).

Myna was written in TypeScript (which has a familiar syntax for most programmers), is contained in a single file with no dependencies, and is less than 1200 lines including detailed documentation.

If you are interested in seeing Myna applied to a more a complex scenario, take a look at the [Chickadee programming language](https://github.com/Clemex/chickadee). This is implemented entirely in TypeScript and depends only on the [Myna parsing library](https://github.com/cdiggins/myna-parser). Chickadee is a tiny programming language designed specifically to help people learn about techniques of implementing programming languages.

If you liked this article please let me know, and consider sharing it with your friends and colleagues.

