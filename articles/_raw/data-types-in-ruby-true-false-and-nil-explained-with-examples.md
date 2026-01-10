---
title: Data Types in Ruby - True, False, and Nil Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/data-types-in-ruby-true-false-and-nil-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cf8740569d1a4ca352a.jpg
tags:
- name: Boolean
  slug: boolean
- name: Ruby
  slug: ruby
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "true, false, and nil are special built-in data types in Ruby. Each of these\
  \ keywords evaluates to an object that is the sole instance of its respective class.\n\
  true.class\n => TrueClass\nfalse.class\n => FalseClass\nnil.class\n => NilClass\n\
  \ntrue and false ..."
---

`true`, `false`, and `nil` are special built-in data types in Ruby. Each of these keywords evaluates to an object that is the sole instance of its respective class.

```ruby
true.class
 => TrueClass
false.class
 => FalseClass
nil.class
 => NilClass
```

`true` and `false` are Ruby’s native boolean values. A boolean value is a value that can only be one of two possible values: true or not true. The object `true` represents truth, while `false` represents the opposite. You can assign variables to `true` / `false`, pass them to methods, and generally use them as you would other objects (such as numbers, Strings, Arrays, Hashes).

`nil` is a special value that indicates the absence of a value – it is Ruby’s way of referring to “nothing”. An example of when you will encounter the `nil` object is when you ask for something that doesn’t exist or cannot be found:

```ruby
hats = ["beret", "sombrero", "beanie", "fez", "flatcap"]

hats[0]
 => "beret" # the hat at index 0
hats[2]
 => "beanie" # the hat at index 2
hats[4]
 => "flatcap" # the hat at index 4
hats[5]
 => nil # there is no hat at index 5, index 5 holds nothing (nil)
```

Zero is not nothing (it’s a number, which is something). Likewise, empty strings, arrays, and hashes are not nothing (they are objects, which happen to be empty). You can call the method `nil?` to check whether an object is nil.

```ruby
0.nil?
 => false
"".nil?
 => false
[].nil?
 => false
{}.nil?
 => false
nil.nil?
 => true
 # from the example above
hats[5].nil?
 => true
```

Every object in Ruby has a boolean value, meaning it is considered either true or false in a boolean context. Those considered true in this context are “truthy” and those considered false are “falsey.” In Ruby, _only_ `false` and `nil` are “falsey,” everything else is “truthy.”

## More Information:

* [Learning Ruby: From Zero to Hero](https://www.freecodecamp.org/news/learning-ruby-from-zero-to-hero-90ad4eecc82d/)
* [Idiomatic Ruby: writing beautiful code](https://www.freecodecamp.org/news/idiomatic-ruby-writing-beautiful-code-6845c830c664/)
* [How to Export a Database Table to CSV Using a Simple Ruby Script](https://www.freecodecamp.org/news/export-a-database-table-to-csv-using-a-simple-ruby-script-2/)

