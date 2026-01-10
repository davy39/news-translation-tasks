---
title: 'Regular Expressions Demystified: RegEx isn’t as hard as it looks'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-23T21:35:28.000Z'
originalURL: https://freecodecamp.org/news/regular-expressions-demystified-regex-isnt-as-hard-as-it-looks-617b55cf787
coverImage: https://cdn-media-1.freecodecamp.org/images/0*kKGQn6RZmO--M8ix.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Vijayabharathi Balasubramanian

  Are you one of those people who stays away from regular expressions because it looks
  like a foreign language? I was one. Not anymore.

  Think of all those sounds, traffic signs and smells that you can recognize. Regula...'
---

By Vijayabharathi Balasubramanian

Are you one of those people who stays away from regular expressions because it looks like a foreign language? I was one. Not anymore.

Think of all those sounds, traffic signs and smells that you can recognize. Regular expressions are no different. It’s like a sign language to analyze strings.

We are going to get our head around regular expressions today. At least, **regularly** used expressions.

Much like any programming language, a regular expression is a succinct language in its own right.

We will know how to put regular expressions to good use by the end of this article. We will solve simple problems and learn loads in the process.

Are you willing to invest 30 minutes and come out enlightened in RegEx? Settle down then.

#### Why regular expressions?

We each have our own ‘why’, don’t we? One may be to test if the string is a valid hex color code. You may be writing a processor library such as [Sass](https://github.com/search?l=&q=regexp+repo%3Asass%2Fsass&ref=advsearch&type=Code&utf8=%E2%9C%93) that leverages RegEx.

I’ll let the universe throw the **why** at you and help you cover the **how**.

### 0. Get Your Playground Ready

#### References

Most of the time, I find this page adequate to get going: [Regular Expressions from MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions). In fact, that page is all you need. You can stop reading this post. Right now. Close this tab. ?

Still with me? Thanks. You need a sandbox to play around in. Luckily, one is available on your browser. Just use the DevTools in your browser’s console.

#### Familiarize yourself with the syntax

To start with, we are going to use the `/expression/.test('string')` syntax.

An `expression` is any regular expression that we build. A `string` is the string under test. The `test` method returns `true` or `false` depending on the match.

Slashes mark the start and end of the expression. Treat them like the double quotes (“) and single quotes (‘) that you use to the mark start and end of a plain string.

The expression between `/` is a literal. **They are treated as literal characters.** Variable names wouldn’t be resolved down to their contents.

To make it dynamic, we’ll have to go via the constructor route, using `new RegEx(variable_name)` syntax. This will come to rescue towards the end of the post.

**Do it right now.** Just type this into your browser console.

```js
/a/.test("a"); //true
/a/.test("b"); //false
```

If that works, you are ready. Don’t worry about what it is. That’s what we are going to breakdown into pieces in the following lines.

Let’s dive in…

### 1. Start Small With Letters

Let’s start small. We need to find if a string has a particular character. Look for the character `a` in a string.

Here is the expression in all its glory:

```js
/a/.test("abc"); //true 
/a/.test("bcd"); //false 
/a/.test("cba"); //true
```

The expression does what we asked for, “Look for `a` in the string under test”. In our case, `abc` and `bca` do have the character `a`. But `bcd` does not have it.

#### Breakdown

Now, that’s a lot of slashes and backslashes. Let’s break them down.

We’ve seen that `/expression/` is how we build regular expressions. So no question about slash there. In fact, we can even **assign it to a variable** and make it look better.

**The same code:**

```js
let e=/a/; 
e.test("abc"); //true 
e.test("bcd"); //false 
e.test("cba"); //true
```

The expression between slashes is just a single character `a` in our case. We are looking only for that one character.

#### Reach Multi-Characters

Let’s scale the solution.

What if you want to find more than one character?

Put them in sequence. Treat them as a substring.

Here is an example:

```js
/ab/.test("abacus"); //true 
/bac/.test("abacus"); //true  
/abc/.test("abacus"); //false 
/abas/.test("abacus"); //false
```

The string under test should contain the exact expression within slashes. We get a match if that condition is met.

`bac` is within `abacus`but `abas` is not in `abacus` as it is. Even though we have those characters scrambled, we do not get an exact match.

#### Review Ground Covered

Symbol `/.../` . Slash (/) marks the start and end of the regular expression. Ignore the dots, that’s where we place the pattern. The `/a/` character between slashes is a pattern matched on string under test. The `/abc/` characters between slashes are looked up as a sub-string during the pattern matching test on string under test.

### 2. Patterns in Numbers

Let’s spice it up a bit. Let’s say you want to find out if a string is full of numeric characters.

Here it is:

```js
let e=/0|1|2|3|4|5|6|7|8|9/;
e.test("42"); //true 
e.test("The answer is 42"); //true
```

First of all, the pattern looks pretty long. But the same long streak of characters **can be expressed in just two characters**. I reserved it towards end of this section for a dramatic closure.

The second case shouldn’t be true. We’ll deal with it a bit later.

For now, the pipe symbol (`|`) means **or**. Outside of regular expressions, we’ve used it as a bitwise **or** and conditional **or** with double pipes (||). That’s the same guy.

I could call that easy and call it a day. But you would scream for something better, right? We are developers. We spend the best part of our day thinking about better Bash and Git aliases to save few keystrokes.

Should I type in nine pipe symbols? Nah.

Here we go again:

```js
e=/[0123456789]/; 
e.test("42"); //true 
e.test("The answer is 42"); //still true
```

This is better. 9 pipes were replaced with 2 square brackets. 7 characters were saved. That’s 77.7% less keystrokes.

By the way, anything within square brackets is considered as `Either this` or `that`. It is a character set. In our case, the string should contain either `0`, or `1`, or `2`, or…bear with me, I promised myself to write 1000 words a day, or `3` or `4` or `5`. All right, let’s stop. You get it.

What are you saying? It still looks quite lengthy? Not satisfied?

Okay, here we go once again:

```js
e=/[0-9]/; 
e.test(42); //true 
e.test("42"); //true 
e.test("The answer is 42"); //true!
```

How about that? Looks much cleaner, doesn’t it? Anything within square brackets `[]` means **or**. `0-9` marks a range, meaning zero to nine.

So the test looks for characters from zero to nine in the test string.

As you can see, the test takes numbers too.

#### The prefix and suffix patterns

Let’s now address that failing second case. `The answer is 42` matches our test because our pattern looks for numeric characters somewhere **within** the string. **Not start to end**.

Let’s bring in `^` and `$` to help us.

* `^` means the **start** of the string. He is a double agent and he’ll trip us off. His second avatar is unmasked only in the last section.
* `$` means the **end** of the string.

Let’s get the prefix pattern sorted out:

```js
/^a/.test("abc"); //true 
/^a/.test("bca"); //false 
/^http/.test("https://pineboat.in"); //true /^http/.test("ftp://pineboat.in"); //false
```

Any pattern that follows `^` should be at the start of the string under test.

The second string starts with `b` while our pattern looks for `a`. The fourth one looks for `http` while the string starts with `ftp.` This is the reason they fail.

#### The suffix patterns

The suffix pattern follows. `$` at the end of the pattern directs the test to look for end of string.

```js
/js$/.test("regex.js"); //true 
/js$/.test("regex.sj"); //false
```

That should sound in your head like, “Look for `js` and then the end of the string”. Better yet, “Look for a string that ends in `js`”.

#### Pattern match End to End

That paves the road to pattern match start to end, you might as well call it end to end.

```js
let e=/^[0-9]$/ 
e.test("42"); //false - NO! 
e.test("The answer is 42"); //false 
e.test("7"); //true
```

Surprisingly, the first one failed when we added `^` and `$`.

`/^[0-9]$/` reads like, “Go to the start of the string. Look for a **single numeral** from the character set. Check if the string ends right there.” That’s the reason the last entry returned `true`. It is just a single number, start to end.

That’s not what we wanted. We wanted to test if the string had one or more numerals.

We are very close. One last thing we need to learn is how to instruct the pattern to look for more than one character in the set.

#### Tale of Three Musketeers

A question mark (`?`), a plus (`+`) and an asterisk (`*`) met at a battle ground. Each is differently sighted.

The humble question mark (`?`)says, “I can see none or just one.”

Plus (`+`) says, “I need to see at least one or more.”

Asterisk (`*`) says, “I get you both. I can see none, one, or more.”

**One of them is cleverly hiding what he is capable of.**

The question mark gets on stage first:

```js
/a?/.test(""); //true 
/a?/.test("a"); //true 
/a?/.test("b"); //true! 
/a?/.test("aa"); //true 
/^a?$/.test("aa"); //false
```

* Matches empty string `""`   
as `?` stands for 0 or 1
* Matches `a`   
one match
* Matches `b`  
 matches 0 occurrence
* Matches `aa`   
one match and the second `a` is not part of the pattern
* `/^a?$/` does not match `aa`  
It looks for zero or one `a`, start to end, nothing more, nothing less

The plus (`+`) looks at question mark and remarks, “I’m impressed, but your focus is so binary!”. And takes the stage to show off:

```js
/a+/.test("a"); //true 
/a+/.test("aa"); //true 
/a+/.test("ba"); //true! 
/^a+$/.test("aa"); //true  
/a+/.test(""); //false 
/a+/.test("b"); //false 
/^a+$/.test("ab"); //false
```

Remember what plus (`+`) said? It can match one or more occurrences of preceding pattern.

All those returning `true` have one or more `a`. We even managed to get a whole string comprised only of `a` in the last one that returned true with `/^a+$/`.

`false` should make sense now, but a word on the last one that returned false. `/^a+$/` looks for `a` start to end, no other characters allowed. This is why `ab` failed the test.

Finally, star (`*`) of the show gets on stage. He boasts that, “I can duel alone or duel you both at once” and says, “I can match zero, one or more”.

```js
/a*/.test("a"); //true 
/a*/.test("aa"); //true 
/a*/.test("ba"); //true 
/a*/.test(""); //true 
/a*/.test("b"); //true 
/^a*$/.test("aa"); //true 
/^a*$/.test(""); //true  
/^a*$/.test("ab"); //false
```

Except the last one, * was able to handle all else. `/^a*$/` reads like, 0 or more `a` start to end. Which is why empty string `""` passed the test and `"ab"` failed.

#### Back to the Universal Answer

Remember where were we before we met the three musketeers? Yes, “The answer is 42”.

Now if we need to look for only numerals, one or more, start to end, what do we do?

```js
//Let's throw in a plus 
let e=/^[0-9]+$/ 
e.test("4"); //true 
e.test("42"); //true 
e.test("The answer 42"); //false - Hurray
```

The plus sign (`+`) in `[0-9]+` comes to our rescue. Plus means more than one occurrence of the character or pattern in front of it. In our case, more than one numerals.

It also fails the match for our last case `The answer is 42` because, there are no numerals at the start of the string.

#### Practice Patterns

* Can you try to write a pattern for hexadecimal numbers (consisting of numerals 0–9 and letters a-f, with an optional # in front)?
* How about a binary number? Can you test if a string is full of just 0 and 1?

#### That Dramatic End

Oh, I almost forgot. `[0-9]` stands for any of the numeric character set and also has a shorthand version `\d`.

```js
let e=/^\d+$/; e.test("4"); //true e.test("42"); //true e.test("The answer 42"); //false - Hurray
```

Just two characters denoting numerals. And No, it doesn’t get any shorter than that.

There are a whole bunch of such special patterns to specify clusters such as numbers (`\d`), alpha numeric characters (`\w`), white spaces (`\s`).

#### Review

* `[123]`  
The expression within square brackets are a character set  
Any one of the characters match will pass the test. Just ONE character.
* `[0-9]`   
Looks for a single numeric digit between 0 to 9
* `[0-5]`   
Looks for a single numeric digit between 0 to 5
* `[a-z]`   
Looks for a single letter between a to z
* `[A-F]`   
Looks for a single letter between A to F
* `[123]+`   
Plus (`+`) looks for one or more occurrence of the characters within the set This one matches a “23132” sub-string that consists of 1, 2 and 3 within a larger string “abc23132”.
* `|`   
Pipe symbol stands for **or**
* `\d`   
A shorthand for numerals  
Matches a single numeric digit.
* `\D`   
A shorthand for non-numeric characters  
Anything other than numerals that’ll be matched by `\d`

### 3. Recurrence Match to Find Duplicates

This is the actual problem I was trying to solve. I dove deep into regular expressions, which eventually led to this post.

You’ve been given a string. Find out if it has been infused with duplicate characters before sunset.

Here is the solution for duplicate characters appearing immediately after an occurrence:

```js
let e=/(\w)\1/; 
e.test("abc"); //false 
e.test("abb"); //true
```

The expression does not match any part of the string `abc` as there are no duplicate characters in sequence. So it returns false.

But it matches `bb` part of the string `abb` and returns true.

Go ahead, type that on your DevTool console. Look at this!

Let’s break it down to understandable pieces.

#### Backslash \ Unleashed

I’ve been a little quiet about the backslash that was introduced in the last section. To those who have **been there** and **done that**, it may not have been a surprise. They might have **escaped** the confusion. But if you are new to programming world, you need to know more about backslash.

In the regular expression language, backslash is special. The backslash alters the meaning of the characters that follow them. Ring a bell?

What do you call `\n` when you encounter it in a string? Yes, a new line. We’ve got something similar here.

In fact, `\n` is what you use as a pattern if you want to look for a new line. That’s called `escaping` the usual meaning of `n` and giving it a whole new attire called `new line`.

* `\d`  
A shorthand for numerals  
Matches a single numeric digit
* `\D`   
A shorthand for non-numeric characters  
Anything other than numerals that’ll be matched by `\d`
* `\s`   
Shorthand for single white space character such as space, new line or tab.
* `\S` Antonym of `\s`  
anything other than white space
* `\w`   
Shorthand for alpha-numeric character  
Matches a-z, A-Z, 0–9 and underscore _.
* `\W`   
Antonym of `\w`

#### Recallable Matches

We started this section with the solution for finding duplicate characters. `/(\w)\1/` matched `"abb"`. That shows use of memory and recall within regular expressions.

Consider the use of brackets in this format `(expression)`. The resulting string that matches the expression within a bracket is remembered for later use.

`\1` remembers and uses the match from first expression that is within brackets. Likewise, `\2` from second set of brackets. And so on.

Let’s translate our expression `(\w)\1` to plain English:

Match any alpha-numeric character on a given string. Remember it as `\1`. Check if that character appears right next to the first occurrence.

#### Extension 1 — Reverse Pairs

Let’s say we want to find two characters appearing in reverse order right next to each other. That is like `abba`. `ab` is reversed as `ba` and is right next to each other.

Here is the expression:

```js
let e=/(\w)(\w)\2\1/; 
e.test("aabb"); //false 
e.test("abba"); //true 
e.test("abab"); //false
```

The first `(\w)` matches `a` and remembers it as `\1`. The second `(\w)` matches `b` and remembers it as `\2`. Then the expression expects `\2` to occur first followed by `\1`. Hence, `abba` is the only string that matches the expression.

#### Extension 2 — No duplicates

This time, we are going to look at sequence of characters with no duplicates. No character should be followed by the same character. Plain and simple.

Here, take a look at the solution:

```js
let e=/^(\w)(?!\1)$/; 
e.test("a"); //true 
e.test("ab"); //false 
e.test("aa"); //false
```

Not the one we wanted, but close. The middle one shouldn’t be false. But we threw in a few more symbols that need explaining. That means confronting the most powerful musketeer once again.

#### Return of the Question Mark

Remember the three musketeers we met earlier. The humble **question mark is actually the most powerful manipulator** that can get other symbols to do his bidding. That is, if you take the backslash for granted.

A combination of brackets, question mark and exclamation mark `(?!)`, is called a **look ahead**. A negative look ahead to be precise. `a(?!b)` matches `a` only if it is **not** followed by `b`.

Across JavaScript ecosystem, the exclamation mark means **not**. But its cousin CSS takes a u-turn and `!important` means it is actually very important and should not be overridden. I almost scrolled past [Chen’s tweet](https://twitter.com/vijayabharathib/status/910772769964548096) thinking it is marked not important. I digress.

On the other hand, `(?=)` is a positive **look ahead**. `a(?=b)` matches `a` only if it is followed by `b`.

We had a solution. `(\w)(?!\1)` looks for a character without recurrence. **But only for one character.** We need to group it and look for 1 or more occurrences of characters with the use of plus (`+`). That’s all.

```js
let e=/^((\w)(?!\1))+$/; 
e.test("madam"); //false 
e.test("maam"); //false
```

But it doesn’t seem to be working. If we group the pattern within plain brackets like `((\w)(?!\1))`, the `\1` does not represent`(\w)`, it represents higher level bracket pair that groups the pattern. So it fails.

What we need is a **forgetful** grouping option. That’s where the question mark, `?`, strikes back. It pairs with a colon, `(?:)` and wipes out any function of memory that the brackets can bring in.

One last time:

```js
let e=/^(?:(\w)(?!\1))+$/; 
e.test("madam"); //true 
e.test("maam"); //false
```

This time, the first level of brackets are not remembered, thanks to `?:`, hence, `\1` remembers the match returned by `\w`.

It helps us use the plus `+` against the overall grouping to find similar pairs of characters start to end, which works like magic.

In English, “Look for a character. Look ahead to ensure it is not followed by the same character. Do this from start to end for all characters.”

#### Review

* `\w` represents all the alpha-numeric characters  
If you capitalize ‘w’ and use `\W'`, that would mean all characters **other than** alpha-numeric
* `( )`   
The expression within a bracket is remembered for later use
* `\1` remembers and uses the match from first expression that is within brackets  
 `\2` from second set of brackets. And so on.
* `a(?!b)`   
A combination of brackets, question mark and exclamation mark (`?!`), is called a **look ahead**  
This matches `a` only if it is **not** followed by `b`
* `a(?=b)`  
The other side of the coin  
Match `a` only if it is followed by `b`. `(?:a)`   
**Forgetful grouping**  
Look for `a` but don’t remember it  
You can’t use `\1` pattern to reuse this match

### 4. Alternating Sequence

The usecase is simple. Match a string that uses only two characters. Those two characters should alternate throughout the length of the string. Two sample tests for “abab” and “xyxyx” will do.

It wasn’t easy. I got it wrong on several attempts. This [answer](https://stackoverflow.com/questions/45504400/regex-match-pattern-of-alternating-characters) directed me down the right street.

Here is the solution:

```js
let e=/^(\S)(?!\1)(\S)(\1\2)*$/; 
e.test("abab"); //true 
e.test("$#$#"); //true 
e.test("#$%"); //false 
e.test("$ $ "); //false 
e.test("xyxyx"); //false
```

This is where you say, “I’ve had enough!” and throw in the towel.

But wait for the Aha moment! You are 3 feet away from the gold ore, not the right time to stop digging.

Let’s first make sense out of results before we arrive at ‘**how?**’ `abab` matches. `$#$#` matches, this is no different from `abab`.

`#$%` fails as there is a third character. `$ $` fails though they are pairs, because space is excluded in our pattern.

All is well except, `xyxyx` fails, because our pattern doesn’t know how to handle that last x. We’ll get there.

Let’s take a look at the tools added to our belt. It’ll start to make sense soon.

#### One piece at a time

You already know most of the pieces. `\S` is the opposite of `\s`. `\S` looks for non white space characters.

Now comes the plain English version of `/^(\S)(?!\1)(\S)(\1\2)*$/`.

* Start from the start `/^`
* Look for a non-white space character `(\S)`
* Remember it as `\1`
* Look ahead and see if the first character is not followed by the same character `(?!\1)`.   
Remember this is a **negative look ahead**.
* If we are good so far, look for another character `(\S)`
* Remember it as `\2`
* Then look for **0 or more pairs of first two matches** `(\1\2)*`
* Look for such pattern until end of the string `$/`

Apply that to our test cases. `"abab"` and `"$#$#"` match.

#### Tail End

After looking at the solution you may think this does not demand a separate section. But the simplicity of it is elegant. Let’s fix that one failing case `xyxyx`. As we’ve seen, the last trailing x is the problem. We have a solution for `xyxy`. All we need is a pattern to say “Look for an optional occurrence of first character”.

As usual, let’s start with the solution.

```js
let e=/^(\S)(?!\1)(\S)(\1\2)*\1?$/; e.test("xyxyx"); //true e.test("$#$#$"); //true
```

The question mark strikes again. There is no escaping him. It’s better we make him our ally than our enemy. A question mark `?` after a character or pattern means 0 or 1 match for the preceding pattern. It is non-greedy in gobbling up characters.

In our case, `\1?` means, 0 or 1 match of the first character remembered through first set of brackets.

Easy. Relax.

#### Review

* `\S`   
Represents all characters excluding white space such as a space and new lines  
Note that it is capital S
* `a*`   
The asterisk or star, looks for 0 or more occurrences of the preceding character. In this case, it is 0 or more `a`  
Remember plus (`+`) which looks for 1 or more? Yeah, these guys are cousins.
* `a(?!b)`   
This combination of brackets, question mark and exclamation mark (`?!`) is called a **look ahead**.   
This matches `a` only if it is not followed by `b`.   
For example, it matches `a` in `aa`, `ax`, `a$` but does not match `ab`  
Though it uses bracket, it does not remember the matching character after `a`.
* `\s`   
Small caps `s` matches a single white space character such as a space or new line.
* `a(?=b)`   
This matches `a` that is followed by `b`.
* `^ab*$`   
You may think this translates to 0 or more occurrences of `ab`, but it matches `a` followed by 0 or more `b`  
For example: This matches `abbb`, `a`and `ab`, but does not match `abab`
* `^(ab)*$`   
This matches 0 or more pairs of `ab`  
 That means it will match empty string `""`, `ab`and `abab`, but not `abb`
* `a?`   
`?` matches 0 or 1 occurrence of preceding character or pattern  
 `\1?` matches 0 or 1 recurrence of first remembered match

### 5. Match an email address

#### Warning for Production

Regular expressions alone may not help validate emails. Some would even argue that regular expressions should not be used as it can never match 100% of the emails.

Think about all the fancy domain names popping up. Also consider inclusion of symbols within email addresses, such as dot (.) and plus (+).

You need to validate email twice. Once on the client side to help users avoid misspelled addresses. Start with a semantic input tag type `<input type='emai`l'>. Some of the browsers automatically validate it without any extra scripting on the front end.

Validate it once again on the server by actually sending a confirmation email.

Haven’t you seen one such lately? Just try to subscribe to this [pineboat](https://www.pineboat.in/). You’ll get an actual email asking you to confirm that it is yours. That confirmation is a solid proof that your email is valid.

That was smooth sailing, wasn’t it?

#### RegEx for Email

Now that we added the disclaimer, you’d actually want to see a pattern right? No, search for regular expression for an email address. One such result from [perl module](http://www.ex-parrot.com/~pdw/Mail-RFC822-Address.html) goes for more than a page.

So, I am not even going to attempt it. Such long regular expressions are generated by computers through pattern builders. Not for mere mortals like us.

### 6. Match a Strong Password

If you are a coffee person, this is the right time to get a strong one. Because we are at last section of this post, but the longest one so far.

It introduces very few new operators and patterns. But it reuses many patterns. As usual, we reserve the shortest optimized one for last.

The ASCII range is the best part of this post. Because, I learned it while researching for this post.

Now, the problem. Remember that registration form that took several attempts before you could meet their strong password requirements? Weak, good, strong, and very strong? Yeah, we are going to build that validation.

The password should:

* have a minimum of 4 characters
* contain lowercase
* contain uppercase
* contain a number
* contain a symbol

This is a tricky one. Once you start consuming letters, you can’t come back to check if they meet any other condition. There in lies our clue. **We can’t look back, but we can look ahead!**

#### Length of the string

Let’s first test if the string password is 4 characters long. Pretty simple. Use `.length` on the password string. Done, right? No, who needs a simple solution? Let’s spice it up.

```js
//expression with just lookahead
//wouldn't consume any character
e1=/^(?=.{4,})$/; 
e1.test("abc") //false
e1.test("abcd") //false  

//after lookahead, 
//pattern to consume character is needed.
e2=/^(?=.{4,}).*$/; 
e2.test("abc") //false 
e2.test("abcd") //true
```

* You may remember `(?=)` from our previous work on [“no duplicates”](https://www.pineboat.in/post/regular-expressions-your-ally/#extension-2-no-duplicates) That’s a look ahead use  
It does not consume any character
* The dot (`.`) is an interesting character  
It means, **any character**.
* `{4,}`   
Stands for at least 4 preceding characters with no maximum limit
* `\d{4}`   
Would look for exactly 4 numerals
* `\w{4,20}`   
Would look for 4 to 20 alpha-numeric characters

Let’s translate `/^(?=.{4,})$/`. “Start from the beginning of the string. Look ahead for at least 4 characters. Don’t remember the match. Come back to the beginning and check if the string ends there.”

Doesn’t sound right. Does it? At least the last bit.

Which is why we brought in the variation `/^(?=.{4,}).*$/`. An extra dot and a star. It reads like this, “Start from the beginning. Look ahead for 4 characters. Don’t remember the match. Come back to the beginning. Consume all the characters using `.*` and see if you reach the end of the string.”

This makes sense now. Doesn’t it?

Which is why `abc` fails and `abcd` passes the pattern.

#### At least One Number

This is going to be easy.

```js
e=/^(?=.*\d+).*$/ 
e.test(""); //false 
e.test("a"); //false 
e.test("8"); //true 
e.test("a8b"); //true 
e.test("ab890"); //true
```

Start from the beginning of the string `/^`. Look ahead for 0 or more characters `?=.*`. Check if 1 or more numbers follow `\d+`. Once it matches, come back to the beginning (because we were in look ahead). Consume all the characters in the string until end of the string `.*$/`.

#### At Least One Lowercase Letter

This one follows the same patter as above.

```js
e=/^(?=.*[a-z]+).*$/; 
e.test(""); //false 
e.test("A"); //false 
e.test("a"); //true
```

Translation? Sure. “Start from the… okay.” Instead of `\d+`, we have `[a-z]+` which is a character set of letters from `a` to `z`.

#### At least One Uppercase Letter

Let’s not overkill. `[A-Z]` instead of `[a-z]` from the previous section will do.

#### At least One Symbol

This is going to be challenging. One way to match symbols is to place a list of symbols in a character set. `/^(?=.*[-+=_)(\*&\^%\$#@!~”’:;|\}]{[/?.>,<]+).*$/.test`(“$”) That’s all the symbols in a character set. Properly escaped where necessary. It’ll take months for me to write it in plain English.

So to save all of us from eternal pain, here is a simple one:

```js
//considers space as symbol 
let e1; 
e1=/^(?=.*[^a-zA-Z0-9])[ -~]+$/ 
e1.test("_"); //true 
e1.test(" "); //true  

//does not take space 
let e2; 
e2=/^(?=.*[^a-zA-Z0-9])[!-~]+$/ 
e2.test(" "); //false 
e2.test("_"); //true  

//the underscore exception 
let e3; 
e3=/^(?=.*[\W])[!-~]+$/ 
e3.test("_"); //false
```

Wait, what’s that `^` coming again from the middle of no where? If you have reached this far, this is where you realize that unassuming innocent `^` that marks start of a string is a double agent. Which means, the end is not too far. He has been exposed.

Within a character set, `^` negates the character set. That is, `[^a-z]` means, any character other than `a` to `z`.

`[^a-zA-Z0-9]` then stands for any character other than lower case alphabets, upper case alphabets, and numerals.

We could have used `\W` instead of the long character set. But `\W` stands for all alpha-numeric characters **including underscore _.** As you can see in the third set of examples above, that will not accept underscore as a valid symbol.

#### CharSet Range

The curious case of `[!-~]`. They stand next to each other in the keyboard, but their ASCII values are diagonally opposite.

Remember a-z? A-Z? 0–9? These are not constants. They are actually based on the ASCII range of their values.

The [ASCII table](http://www.asciitable.com/) has 125 characters. zero (0) to 31 are not relevant to us. Space starts from 32 going all the way up to 126 which is tilda(~). The exclamation mark is 33.

So `[!-~]` covers all the symbols, letters and numbers we need. The seed for this idea came from [another solution](https://stackoverflow.com/questions/8359566/regex-to-match-symbols) to the symbol problem.

#### Assemble the Troops

Bringing it all together, we get this nice looking piece of regular expression `/^(?=.{5,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)(?=.*[^\w])[ -~]+$/`.

That’s starting to haunt and intimidate us. Though we’ve been studying them individually.

This is where the syntax for dynamically building expression object comes in handy. We are going to build each piece separately and assemble them later.

```js
//start with prefix 
let p = "^"; 

//look ahead  
// min 4 chars 
p += "(?=.{4,})"; 
// lower case 
p += "(?=.*[a-z]+)"; 
// upper case 
p += "(?=.*[A-Z]+)"; 
// numbers 
p += "(?=.*\\d+)"; 
// symbols 
p += "(?=.*[^ a-zA-Z0-9]+)"; 
//end of lookaheads  

//final consumption 
p += "[ -~]+";  
//suffix 
p += "$"; 

//Construct RegEx 
let e = new RegEx(p); 
// tests 
e.test("aB0#"); //true  
e.test(""); //false 
e.test("aB0"); //false 
e.test("ab0#"); //false 
e.test("AB0#"); //false 
e.test("aB00"); //false 
e.test("aB!!"); //false  

// space is in our control 
e.test("aB 0"); //false 
e.test("aB 0!"); //true
```

If your eyes are not tired yet, you’d have noticed two strange syntax in the above code.

* One, we didn’t use `/^`, instead we used just `^`. We didn’t use `$/` to end the expression either, instead just `$`.  
The reason is that the `RegEx` constructor automatically adds starting and trailing slashes for us.
* Two, to match numbers we used `\\d` instead of the usual `\d`. This is because the variable `p` is just a normal string within double quotes. To insert a backslash, you need to escape the backslash itself.   
`\\d` resolves to `\d` within the `RegEx` constructor

Apparently, there should be server side validations for passwords too. Think about SQL injection vulnerabilities if your framework or language doesn’t handle it already.

### 7. Conclusion

That brings us to the end of the story. But this is the beginning of a journey.

We just scratched the pattern matching portion of RegEx with `test` method. `exec` method builds on this foundation to return matched sub-strings based on pattern.

String object has methods such as `match`, `search`, `replace`, and `split` that widely uses regular expressions.

Hope this sets you off to explore those capabilities further with a solid understanding on composing patterns for RegEx.

### 8. Call To Action

No, after all this difficulty we’ve been through, I am not going to ask you to subscribe.

Just make good software.

If any code blocks presented here do not work, leave a comment on this [github issue](https://github.com/pineboat/pineboat.github.io/issues/3) I created specially for this post.

Hope it was useful! Share it if others would benefit.

You’ve been wonderful. Appreciate your time. This content is far long by recent standards. Thanks for reading.

Originally published at [www.pineboat.in](https://www.pineboat.in/post/regular-expressions-your-ally/).

