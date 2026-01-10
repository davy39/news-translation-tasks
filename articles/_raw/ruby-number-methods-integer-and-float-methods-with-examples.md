---
title: Ruby Number Methods and Number Operations (with Examples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-21T23:10:00.000Z'
originalURL: https://freecodecamp.org/news/ruby-number-methods-integer-and-float-methods-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c76740569d1a4ca3253.jpg
tags:
- name: Ruby
  slug: ruby
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Number methods in Ruby

  Ruby provides a variety of built-in methods you may use on numbers. The following
  is an incomplete list of integer and float methods.

  Even:

  Use .even? to check whether or not an integer is even. Returns a true or false boolean....'
---

## Number methods in Ruby

Ruby provides a variety of built-in methods you may use on numbers. The following is an incomplete list of [integer](https://ruby-doc.org/core-2.2.0/Integer.html) and [float](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil) methods.

### [Even](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-even-3F):

Use `.even?` to check whether or not an [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html) is even. Returns a `true` or `false` **boolean**.

```ruby
    15.even? #=> false
    4.even?  #=> true
```

### [Odd](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-odd-3F):

Use `.odd?` to check whether or not an [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html) is odd. Returns a `true` or `false` **boolean**.

```ruby
    15.odd? #=> true
    4.odd?  #=> false
```

### [Ceil](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil):

The `.ceil` method rounds [**floats**](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil) **up** to the nearest number. Returns an [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    8.3.ceil #=> 9
    6.7.ceil #=> 7
```

### [Floor](https://ruby-doc.org/core-2.2.0/Float.html#method-i-floor):

The `.floor` method rounds [**floats**](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil) **down** to the nearest number. Returns an [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    8.3.floor #=> 8
    6.7.floor #=> 6
```

### [Next](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-next):

Use `.next` to return the next consecutive [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    15.next #=> 16
    2.next  #=> 3
    -4.next #=> -3
```

### [Pred](https://ruby-doc.org/core-1.8.7/Integer.html#method-i-pred):

Use `.pred` to return the previous consecutive [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    15.pred #=> 14
    2.pred  #=> 1
    (-4).pred #=> -5
```

### [To String](https://ruby-doc.org/core-2.4.2/Object.html#method-i-to_s):

Using `.to_s` on a number ([**integer**](https://ruby-doc.org/core-2.2.0/Integer.html), [**floats**](https://ruby-doc.org/core-2.2.0/Float.html#method-i-ceil), etc.) returns a [string](https://ruby-doc.org/core-2.2.0/String.html) of that number.

```ruby
    15.to_s  #=> "15"
    3.4.to_s #=> "3.4"
```

### [Greatest Common Denominator](https://ruby-doc.org/core-2.2.0/Integer.html#method-i-gcd):

The `.gcd` method provides the greatest common divisor (always positive) of two numbers. Returns an [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html).

```ruby
    15.gcd(5) #=> 5
    3.gcd(-7) #=> 1
```

### [Round](http://ruby-doc.org/core-2.2.0/Integer.html#method-i-round):

Use `.round` to return a rounded [**integer**](https://ruby-doc.org/core-2.2.0/Integer.html) or [**float**](https://ruby-doc.org/core-2.2.0/Float.html).

```ruby
    1.round        #=> 1
    1.round(2)     #=> 1.0
    15.round(-1)   #=> 20
```

### [Times](http://ruby-doc.org/core-2.2.0/Integer.html#method-i-times):

Use `.times` to iterate the given block `int` times.

```ruby
    5.times do |i|
      print i, " "
    end
    #=> 0 1 2 3 4
```

## Math operations in Ruby

In Ruby you can perform all standard math operations on numbers, including: addition `+`, subtraction `-`, multiplication `*`, division `/`, find remainders `%`, and work with exponents `**`.

### Addition:

Numbers can be added together using the `+` operator.

```ruby
15 + 25 #=> 40
```

### Subtraction:

Numbers can be subtracted from one another using the `-` operator.

```ruby
25 - 15 #=> 10
```

### Multiplication:

Numbers can be multiplied together using the `*` operator.

```ruby
10 * 5 #=> 50
```

### Division:

Numbers can be divided by one another using the `/` operator.

```ruby
10 / 5 #=> 2
```

### Remainders:

Remainders can be found using the modulus `%` operator.

```ruby
10 % 3 #=> 1 # because the remainder of 10/3 is 1
```

### Exponents:

Exponents can be calculated using the `**` operator.

```ruby
2 ** 3 #=> 8 # because 2 to the third power, or 2 * 2 * 2 = 8
```

