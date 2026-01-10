---
title: What is TOON? How Token-Oriented Object Notation Could Change How AI Sees Data
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2025-11-13T15:23:51.254Z'
originalURL: https://freecodecamp.org/news/what-is-toon-how-token-oriented-object-notation-could-change-how-ai-sees-data
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762978794293/e75f145b-a418-458e-8a41-12fe3add0107.png
tags:
- name: llm
  slug: llm
- name: AI
  slug: ai
- name: json
  slug: json
seo_title: null
seo_desc: 'JSON, or JavaScript Object Notation, was popularized by Douglas Crockford
  in early 2000. Since then, there’s been no looking back. JSON has become the standardized
  data exchange format between client and server technologies.

  JSON was built for humans...'
---

`JSON`, or JavaScript Object Notation, was popularized by Douglas Crockford in early 2000. Since then, there’s been no looking back. JSON has become the standardized data exchange format between client and server technologies.

JSON was built for humans. It’s readable, accessible, and universal for APIs to consume data or return responses. But in the modern era of AI, a downside of JSON has really come to light: it’s quite verbose.

Every brace, every quote, and every repeated key consumes tokens. If you spend time building apps that talk to large language models (LLMs), you’ll likely know that tokens are the currency of LLM interactions. The more tokens, the more costly your AI solution is going to be.

Now, there is a new kid in town called `TOON` (Token-Oriented Object Notation). It promises to enable LLMs to talk to structured data more efficiently, intelligently, and cost-effectively.

This article is the result of my curiosity in exploring TOON. I wanted to learn why it’s trending, how it works, and how you can use it today in your JavaScript/TypeScript and Python projects. I hope you find this equally exciting as I do.

You can find all the source code used in this article in [this GitHub Repository](https://github.com/tapascript/toon-and-json).

## **Table of Contents**

1. [What is Toon?](#heading-what-is-toon)
    
2. [Why is TOON Important Now?](#heading-why-is-toon-important-now)
    
3. [JSON vs TOON - Learn With Examples](#heading-json-vs-toon-learn-with-examples)
    
4. [How to Use TOON With JavaScript / TypeScript](#heading-how-to-use-toon-with-javascript-typescript)
    
5. [How to Use Toon With Python?](#heading-how-to-use-toon-with-python)
    
6. [Hold On, JSON Might Still Be Better(In Many Cases)](#heading-hold-on-json-might-still-be-betterin-many-cases)
    
7. [The Future of TOON](#heading-the-future-of-toon)
    
8. [Before We End…](#heading-before-we-end)
    

## What is Toon?

TOON is a new data serialization format designed with a code objective:

> Reduce the number of tokens when exchanging structured data with language models.

While JSON uses verbose syntax with braces, quotes, and commas, TOON relies on a token-efficient tabular style, which is much closer to how LLMs naturally understand structured data.

Let’s make a quick comparison between JSON and TOON:

Here is some JSON with a `users` array that contains information about two users (two objects):

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

If you wanted to represent the same data in TOON, it would look like this:

```json
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

Did you notice the differences?

* No quotes, braces, or colons in TOON.
    
* The `users[2]{id,name,role}:` declares an array of two objects with the fields id, name, and role.
    
* The lines below are simply the data rows.
    

You can see that TOON visibly reduced the token usage by 30-50%, depending on the data shape.

## Why is TOON Important Now?

LLMs like GPT, Gemini, and Claude are token-based systems. Each word, symbol, or chunk costs tokens for input and output. So, if you’re preparing an LLM with structured data input/output like this:

```json
{ "products": [ ... 300, "items" ... ] }
```

You might waste thousands of tokens in quotes, braces, colons, and repeated keys. TOON solves that by focusing on a compact yet structured representation.

Some of the key benefits of TOON are:

* 30-50% fewer tokens for uniform data sets.
    
* It has less syntactic clutter, which makes it easier for LLMs to reason about.
    
* It can be nested as we do with JSON.
    
* Works well with languages like Python, Go, Rust, and JavaScript.
    

TOON is a great augmentation to JSON, especially for AI projects, LLMs, and data-heavy prompts. It may not replace JSON entirely, but it’s suitable for use cases where JSON is considered heavyweight for data exchange.

## JSON vs TOON – Learn With Examples

Now that you have a basic idea of what TOON does and why it’s helpful, let’s look at some of the most used JSON structures and their equivalent representation in TOON.

### 1\. A Simple Object

Here’s how you’d represent an object with JSON:

```json
{ "name": "Alice", "age": 30, "city": "Bengaluru" }
```

And here’s how it works with TOON:

```json
name: Alice
age: 30
city: Bengaluru
```

### 2\. Array of Values

With JSON:

```json
{ "colors": ["red", "green", "blue"] }
```

With TOON:

```json
colors[3]: red,green,blue
```

### 3\. Array of Objects

With JSON:

```json
{
  "users": [
    { "id": 1, "name": "Alice" },
    { "id": 2, "name": "Bob" }
  ]
}
```

With TOON:

```json
users[2]{id,name}:
  1,Alice
  2,Bob
```

Here, `users[2]{id,name}` represents the schema, and the lines following it contain the actual data rows.

![TOON Schema](https://cdn.hashnode.com/res/hashnode/image/upload/v1762968459600/03584141-37ae-429d-a999-99ffb93acdcc.png align="center")

### 4\. Nested Objects

With JSON:

```json
{
  "user": {
    "id": 1,
    "name": "Alice",
    "profile": { "age": 30, "city": "Bengaluru" }
  }
}
```

With TOON:

```json
user:
  id: 1
  name: Alice
  profile:
    age: 30
    city: Bengaluru
```

Indentation represents nesting. It’s almost YAML-like, but it’s still structured.

### 5\. Array of Objects With Nested Fields

With JSON:

```json
{
  "teams": [
    {
      "name": "Team Alpha",
      "members": [
        { "id": 1, "name": "Alice" },
        { "id": 2, "name": "Bob" }
      ]
    }
  ]
}
```

With TOON:

```json
teams[1]:
  - name: Team Alpha
    members[2]{id,name}:
      1,Alice
      2,Bob
```

This is still perfectly understandable, and much smaller than the JSON format.

Now that you know a bit about TOON syntax, let’s see how to use it with different programming languages.

## How to Use TOON With JavaScript / TypeScript

In most cases, TOON is not meant to be handwritten. Most TOON data will be generated automatically by software, or you’ll need to encode existing data (say, JSON data) into the TOON format.

And there’s good news – [TOON](https://github.com/toon-format) already has an official NPM package that you can use in your JavaScript/TypeScript project to convert your JSON data to TOON and vice versa.

Install it using the following command:

```bash
npm install @toon-format/toon # Or yarn add, pnpm install, etc
```

The easiest way to create TOON code is by converting JSON to TOON. You can use the `encode()` method from the above-mentioned NPM package:

```javascript
import { encode } from "@toon-format/toon";

const data = {
  users: [
    { id: 1, name: "Alice", role: "admin" },
    { id: 2, name: "Bob", role: "user" },
  ],
};

const toonString = encode(data);
console.log(toonString);
```

Output:

```json
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

To do the reverse (TOON =&gt; JSON), you need to use the `decode()` method:

```javascript
import { decode } from "@toon-format/toon";

const toonString = `
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
`;

const jsonObject = decode(toonString);
console.log(jsonObject);
```

Output:

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

You can check out [this sandbox](https://codesandbox.io/p/sandbox/javascript-forked-n4zsww) and try out a few encoding and decoding examples.

## How to Use Toon With Python

Using TOON in Python projects is as straightforward as it was with JavaScript/TypeScript. There are Python packages that can encode JSON data to TOON and decode it back to JSON. The `python-toon` package is the most famous one in recent days.

First, open your terminal and install the `python-toon` package:

```bash
pip install python-toon
```

Note that if you’re in a virtual environment, you’ll need to activate it first:

```bash
python -m venv venv
source venv/bin/activate
pip install python-toon
```

That’s it! Now you’re all set to use the methods to encode and decode your data to and from TOON. First, let’s encode JSON data to TOON using Python:

```python
from toon import encode

# A channel object
channel = {"name": "tapaScript", "age": 2, "type": "education"}
toon_output = encode(channel)
print(toon_output)
```

Output:

```json
name: tapaScript
age: 2
type: education
```

Similarly, we can decode TOON back to JSON:

```python
from toon import decode

toon_string = """
name: tapaScript
age: 2
type: education
"""

python_struct = decode(toon_string)
print(python_struct)
```

Output:

```json
{"name": "tapaScript", "age": 2, "type": "education"}
```

## Hold On, JSON Might Still Be Better (In Many Cases)

Let’s make it clear that TOON is NOT a universal replacement for JSON. In fact, you should still prefer JSON in many cases, such as when:

* Your data is deeply nested.
    
* Your data is irregular (for example, varying object shapes).
    
* Your application needs strict schema validations or type enforcement.
    
* NON-AI use cases where JSON still stands out and does its job perfectly.
    

A hybrid approach may even work better. Keep JSON for your application’s data exchange format with APIs, but convert to TOON when it comes to sending data to LLMs.

## The Future of TOON

TOON, though in its infancy, is still getting a lot of attention from the developer community. Its early traction is making it unavoidable to talk about.

TOON has already been explored for:

* Less token overhead for structured training data to fine-tune LLMs.
    
* Compact data exchange in Agent frameworks.
    
* Faster data serialization and deserialization between the MCP and AI workflow engines.
    
* With Serverless AI APIs, where cost and speed matter a lot.
    

Just as JSON has been a standard for the Web’s data exchange, TOON may soon be standardized for AI data interchange. So next time you craft a prompt or pass structured data to an AI model, try it in the TOON format. You may notice the model gets faster and cheaper.

## Before We End…

That’s all! I hope you found this article insightful.

Let’s connect:

* Subscribe to my [YouTube Channel](https://www.youtube.com/tapasadhikary?sub_confirmation=1).
    
* Check out my FREE courses, [40 Days of JavaScript](https://www.tapascript.io/courses/40-days-javascript) and [15 Days of React Design Patterns](https://www.tapascript.io/courses/react-design-patterns).
    
* Follow on [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) if you don't want to miss the daily dose of up-skilling tips.
    
* Join my [Discord Server](https://discord.gg/zHHXx4vc2H), and let’s learn together.
    

See you soon with my next article. Until then, please take care of yourself and keep learning.
