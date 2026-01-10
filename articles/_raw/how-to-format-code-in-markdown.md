---
title: How to Format Code in Markdown
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-code-in-markdown
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d0f740569d1a4ca35a8.jpg
tags:
- name: markdown
  slug: markdown
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'There are two ways to format code in Markdown. You can either use inline
  code, by putting backticks (`) around parts of a line, or you can use a code block,
  which some renderers will apply syntax highlighting to.

  Inline Code

  You can use inline code f...'
---

There are two ways to format code in Markdown. You can either use inline code, by putting backticks (`) around parts of a line, or you can use a code block, which some renderers will apply syntax highlighting to.

## **Inline Code**

You can use inline code formatting to emphasize a small command or piece of syntax within a line you’re writing.

For example, you may wish to mention JavaScript’s `Array.protoype.map()` method. By using inline code formatting, it is clear that this is a piece of code. You might also use it to illustrate a terminal command, like `yarn install`.

To use inline code formatting, simply wrap the code you wish to format in backticks. On a standard US layout QWERTY keyboard, this can be found to the left of ‘1’, and above the Tab key. More information on the location of the backtick on international keyboards is provided below.

For instance, writing `Array.prototype.map()` in markdown will render as `Array.prototype.map()`.

## **Code Blocks**

To write longer or more detailed snippets of code, it is often better to place them inside a code block. Code blocks allow you to use multiple lines, and markdown will render it inside its own box and with code type font.

To achieve this, start your block with a line of three backticks. This signals to markdown that you are creating a code block. You will need to finish with another line of three backticks. For example:

```  
var add2 = function(number) {  
   return number + 2;  
}  
```

will render in markdown as:

```text
var add2 = function(number) {
  return number + 2;
}
```

### Syntax highlighting

While not supported natively by markdown, many markdown engines, including the one used by GitHub, will support syntax highlighting. This means that by telling markdown what language you're using inside the code block, it will add colors like an IDE would.

You can do this by adding the name of the language on the same line as your opening three back ticks. In the example above, if instead of the first line being ``` you could write ```js, then JavaScript highlighting will be applied to the block.

```js
var add2 = function(number) {
	return number + 2;
}
```

Syntax highlighting can be applied to more than just JavaScript, though. You can use ```html:

```html
<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <h1>Hello World</h1>
  </div>
</div>
```

```ruby:

```ruby
"Hello World".split('').each do |letter|
  puts letter
end
```

or ```python:

```python
a, b = 0, 1
while b < 10:
    print(b)
    a, b = a, a + b
```

Just remember, not all markdown engines will apply syntax highlighting.

## Backticks on international keyboards

The location of the backtick key can be different on different keyboards, and if you’re not using a US layout QWERTY keyboard, it may be tricky to find. [This](http://superuser.com/a/254077/122424) helpful guide lists some of the ways to find your backtick key, which we’ve collected here below:

### QWERTY and QWERTZ:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/a7daf1d707e12e207d47f0eb70ba01d97ffd1924_1_690x327.png)

### AZERTY:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/8f65c339ce4eefd9d79841f3dc54f4c37cab2e77.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/de291f0895b0fed992726a62d654f4e1f0e421f3.png)


