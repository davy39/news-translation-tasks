---
title: Learn Regular Expressions with this free course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-21T16:46:07.000Z'
originalURL: https://freecodecamp.org/news/learn-regular-expressions-with-this-free-course-37511963d278
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sg2Vdih6v1wDWRPtgnX0DA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: software
  slug: software
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Beau Carnes


  “Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’
  Now they have two problems.” -Jamie Zawinski


  For some people, using regular expressions can be a problem. But it doesn’t have
  to be a problem...'
---

By Beau Carnes

> “Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’ Now they have two problems.” _-Jamie Zawinski_

For some people, using regular expressions can be a problem. But it doesn’t have to be a problem for you. This article is a full course on Regular Expressions.

### 1. Introduction

Regular Expressions, or just RegEx, are used in almost all programming languages to define a search pattern that can be used to search for things in a string.

I’ve developed a [free, full video course](https://scrimba.com/g/gregularexpressions) on Scrimba.com to teach the basics of regular expressions.

This article contains the course in written form. But if you would prefer to watch the video version with interactive lessons, you can check it out on [Scrimba](https://scrimba.com/g/gregularexpressions). The sections in this article correspond to the sections in the Scimba course.

This course follows along with the [RegEx](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/regular-expressions) curriculum at freeCodeCamp.org. You can check that out for coding challenges and to earn a certificate.

These lessons focus on using RegEx in JavaScript, but the principles apply in many other programming languages you might choose to use. If you don’t already know basic JavaScript, it could be helpful if you cover it a bit first. I also have a basic JavaScript course that you can access on [Scrimba](https://scrimba.com/p/pPgdYTV/cEv4Lh6) and on the [freeCodeCamp.org YouTube channel](https://www.youtube.com/watch?v=PkZNo7MFNFg).

So let’s get started! You’ll be saving the day in no time. ?

![Image](https://cdn-media-1.freecodecamp.org/images/mR0hvYGgyvAY9jIH9iiSUNj1gz-dI39-34RS)
_From [https://xkcd.com/208/](https://xkcd.com/208/" rel="noopener" target="_blank" title=")_

### 2. Using the Test Method

To match parts of strings using RegEx, we need to create patterns that help you to do that matching. We can indicate that something is a RegEx pattern by putting the pattern between slashes `/`, like so `/pattern-we-want-to-match/`.

Let’s look at an example:

```
// We want to check the following sentencelet sentence = "The dog chased the cat."
```

```
// and this is the pattern we want to match.let regex = /the/
```

Notice how we use `/the/` to indicate that we are looking for “the” in our `sentence`.

We can use RegEx `test()` method to tell if a pattern is present in a string or not.

```
// String we want to testlet myString = "Hello, World!";
```

```
// Pattern we want to findlet myRegex = /Hello/;
```

```
// result is now truelet result = myRegex.test(myString);
```

### 3. Match Literal Strings

Let’s now find Waldo.

```
let waldoIsHiding = "Somewhere Waldo is hiding in this text.";let waldoRegex = /Waldo/;
```

```
// test() returns true, so result is now also truelet result = waldoRegex.test(waldoIsHiding);
```

Note that in this example `waldoRegex` is case sensitive, so if we were to write `/waldo/` with a lowercase ‘w’, then our `result` would be false.

### 4. Match a Literal String with Different Possibilities

RegEx also has `OR` operator which is `|` character.

```
let petString = "James has a pet cat.";
```

```
// We can now try to find if either of the words are in the sentencelet petRegex = /dog|cat|bird|fish/;
```

```
let result = petRegex.test(petString);
```

### 5. Ignore Case While Matching

So far, we have looked at patterns when the case of the letters mattered. How can we make our RegEx patterns to be case insensitive?

To ignore case we can do it by adding the `i` flag at the end of a pattern, like so `/some-pattern/i`.

```
let myString = "freeCodeCamp";
```

```
// We ignore case by using 'i' flaglet fccRegex = /freecodecamp/i;
```

```
// result is truelet result = fccRegex.test(myString);
```

### 6. Extract Matches

When we want to extract the matched value we can use `match()` method.

```
let extractStr = "Extract the word 'coding' from this string.";
```

```
let codingRegex = /coding/;
```

```
let result = extractStr.match(codingRegex);
```

```
console.log(result);
```

```
// Terminal will show: // > ["coding"]
```

### 7. Find More Than the First Match

Now when we know how to extract one value and it’s also possible to extract multiple values using the`g` flag

```
let testStr = "Repeat, Repeat, Repeat";
```

```
let ourRegex = /Repeat/g;
```

```
testStr.match(ourRegex); // returns ["Repeat", "Repeat", "Repeat"]
```

We can also combine the`g` flag with the`i` flag, to extract multiple matches and ignore casing.

```
let twinkleStar = "Twinkle, twinkle, little star";
```

```
let starRegex = /twinkle/ig;// writing /twinkle/gi would have the same result.
```

```
let result = twinkleStar.match(starRegex);
```

```
console.log(result);
```

```
// Terminal will show: // &gt; ["Twinkle", "twinkle"]
```

### 8. Match Anything with Wildcard Period

In RegEx `.` is a wildcard character that would match anything.

```
let humStr = "I'll hum a song";
```

```
let hugStr = "Bear hug";
```

```
// Looks for anything with 3 characters beginning with 'hu'let huRegex = /hu./;
```

```
humStr.match(huRegex); // Returns ["hum"]
```

```
hugStr.match(huRegex); // Returns ["hug"]
```

### 9. Match Single Character with Multiple Possibilities

Matching any character is nice, but what if we want to restrict the matching to a predefined set of characters? We can do by using `[]` inside our RegEx.

If we have `/b[aiu]g/`, it means that we can match ‘bag’, ‘big’ and ‘bug’.

If we want to extract all the vowels from a sentence, this is how we can do it using RegEx.

```
let quoteSample = "Beware of bugs in the above code; I have only proved it correct, not tried it.";
```

```
let vowelRegex = /[aeiou]/ig;
```

```
let result = quoteSample.match(vowelRegex);
```

### 10. Match Letters of the Alphabet

But what if we want to match a range of letters? Sure, let’s do that.

```
let quoteSample = "The quick brown fox jumps over the lazy dog.";
```

```
// We can match all the letters from 'a' to 'z', ignoring casing. let alphabetRegex = /[a-z]/ig;
```

```
let result = quoteSample.match(alphabetRegex);
```

### 11. Match Numbers and Letters of the Alphabet

Letters are good, but what if we also want numbers?

```
let quoteSample = "Blueberry 3.141592653s are delicious.";
```

```
// match numbers between 2 and 6 (both inclusive), // and letters between 'h' and 's'. let myRegex = /[2-6h-s]/ig;
```

```
let result = quoteSample.match(myRegex);
```

### 12. Match Single Characters Not Specified

Sometimes it’s easier to specify characters that you don’t want to watch. These are called ‘Negated Characters’ and in RegEx you can do it by using `^`.

```
let quoteSample = "3 blind mice.";
```

```
// Match everything that is not a number or a vowel. let myRegex = /[^0-9aeiou]/ig;
```

```
let result = quoteSample.match(myRegex);// Returns [" ", "b", "l", "n", "d", " ", "m", "c", "."]
```

### 13. Match Characters that Occur One or More Times

If you want to match a characters that occurs one or more times, you can use `+`.

```
let difficultSpelling = "Mississippi";
```

```
let myRegex = /s+/g;
```

```
let result = difficultSpelling.match(myRegex);// Returns ["ss", "ss"]
```

### 14. Match Characters that Occur Zero or More Times

There is also a `*` RegEx quantifier. This one matches even 0 occurrences of a character. Why might this be useful? Most of the time it’s usually in combination with other characters. Let’s look at an example.

```
let soccerWord = "gooooooooal!";
```

```
let gPhrase = "gut feeling";
```

```
let oPhrase = "over the moon";
```

```
// We are trying to match 'g', 'go', 'goo', 'gooo' and so on. let goRegex = /go*/;
```

```
soccerWord.match(goRegex); // Returns ["goooooooo"]
```

```
gPhrase.match(goRegex); // Returns ["g"]
```

```
oPhrase.match(goRegex); // Returns null
```

### 15. Find Characters with Lazy Matching

Sometimes your pattern matches can have more than one outcome. For example, let’s say I’m looking for a pattern in a word `titanic` and my matched values must begin with a ‘t’ and end with an ‘i’. My possible results are ‘titani’ and ‘ti’.

This is why RegEx has a concepts of ‘Greedy Match’ and ‘Lazy Match’.

Greedy match finds _the_ _longest possible match_ of the string that fits the RegEx pattern, this is a default RegEx match:

```
let string = "titanic";
```

```
let regex = /t[a-z]*i/;
```

```
string.match(regex);// Returns ["titani"]
```

Lazy match finds _the_ _shortest possible match_ of the string that fits the RegEx pattern and to use it we need to use `?`:

```
let string = "titanic";
```

```
let regex = /t[a-z]*?i/;
```

```
string.match(regex);// Returns ["ti"]
```

### 16. Find One or More Criminals in a Hunt

Now let’s have a look at a RegEx challenge. We need to find all the criminals (‘C’) in a crowd. We know that they always stay together and you need to need to write a RegEx that would find them.

```
let crowd = 'P1P2P3P4P5P6CCCP7P8P9';
```

```
let reCriminals = /./; // Change this line
```

```
let matchedCriminals = crowd.match(reCriminals);
```

You can find me walking through [the solution in this Scrimba cast](https://scrimba.com/p/peyvVAN/c3nEpta).

### 17. Match Beginning String Patterns

RegEx also allows you to match patterns that are only at the beginning of a string. We’ve already talked about `^` creating a negating set. We can use the same symbol to find a match _only_ at the beginning of a string.

```
let calAndRicky = "Cal and Ricky both like racing.";
```

```
// Match 'Cal' only if it's at the beginning of a string. let calRegex = /^Cal/;
```

```
let result = calRegex.test(calAndRicky); // Returns true
```

```
let rickyAndCal = "Ricky and Cal both like racing.";
```

```
let result = calRegex.test(rickyAndCal); // Returns false
```

### 18. Match Ending String Patterns

What about matching a pattern at the end of a string? We can use `$` for that.

```
let caboose = "The last car on a train is the caboose";
```

```
// Match 'caboose' if it's at the end of a string.let lastRegex = /caboose$/;
```

```
let result = lastRegex.test(caboose); // Returns true
```

### 19. Match All Letters and Numbers

Earlier in parts 10 and 11 I showed you how we can match ranges of letters and numbers. If I asked you to write a RegEx that matches all the letters and numbers and ignore their cases you probably would have written something like `/[a-z0-9]/gi` and that’s exactly right. But it’s a bit too long.

RegEx has something called _‘Shorthand Character Classes’_, which is basically a shorthand for common RegEx expression. For matching all letters and numbers we can use `\w` and we also get underscore `_` matched as a bonus.

```
let quoteSample = "The five boxing wizards jump quickly.";
```

```
// Same as /[a-z0-9_]/gi to match a-z (ignore case), 0-9 and _let alphabetRegexV2 = /\w/g;
```

```
// The length of all the characters in a string// excluding spaces and the period. let result = quoteSample.match(alphabetRegexV2).length;
```

```
// Returns 31
```

### 20. Match Everything But Letters and Numbers

If we want to do the opposite and match everything that is not a letter or a number (also exclude underscore `_`), we can use `\W`

```
let quoteSample = "The five boxing wizards jump quickly.";
```

```
// Match spaces and the periodlet nonAlphabetRegex = /\W/g;
```

```
let result = quoteSample.match(nonAlphabetRegex).length;
```

```
// Returns 6
```

### 21. Match All Numbers

Ok, what about if you want only numbers? Is there a shorthand character class for that? Sure, it’s `\d`.

```
let numString = "Your sandwich will be $5.00";
```

```
// Match all the numberslet numRegex = /\d/g;
```

```
let result = numString.match(numRegex).length; // Returns 3
```

### 22. Match All Non-Numbers

Would you like the opposite and match all the non-numbers? Use `\D`

```
let numString = "Your sandwich will be $5.00";
```

```
// Match everything that is not a numberlet noNumRegex = /\D/g;
```

```
let result = numString.match(noNumRegex).length; // Returns 24
```

### 23. Restrict Possible Usernames

So far so good! Well done for making it this far. RegEx can be tricky as it’s not the most easily readable way to code. Let’s now look at a very real-life example and make a username validator. In this case you have 3 requirements:

* If there are numbers, they must be at the end.
* Letters can be lowercase and uppercase.
* At least two characters long. Two-letter names can’t have numbers.

Try to solve this on your own and if you find it difficult or just want to check the answer, [check out my solution.](https://scrimba.com/p/peyvVAN/cmb6nf9)

### 24. Match Whitespace

Can we match all the whitespaces? Of course, we can use a shorthand for that too and it’s `\s`

```
let sample = "Whitespace is important in separating words";
```

```
// Match all the whitespaceslet countWhiteSpace = /\s/g;
```

```
let result = sample.match(countWhiteSpace);
```

```
// Returns [" ", " ", " ", " ", " "]
```

### 25. Match Non-Whitespace Characters

Can you guess how to match all non-whitespace characters? Well done, it’s `\S`!

```
let sample = "Whitespace is important in separating words";
```

```
// Match all non-whitespace characterslet countWhiteSpace = /\S/g;
```

```
let result = sample.match(countWhiteSpace);
```

### 26. Specify Upper and Lower Number of Matches

You can specify the lower and upper number of pattern matches with _‘Quantity Specifiers’._ They can be used with `{}` syntax, for example `{3,6}`, where `3` is the lower bound and `6` is the upper bound to be matched.

```
let ohStr = "Ohhh no";
```

```
// We want to match 'Oh's that have 3-6 'h' characters in it. let ohRegex = /Oh{3,6} no/;
```

```
let result = ohRegex.test(ohStr); // Returns true
```

### 27. Specify Only the Lower Number of Matches

When we want to specify only the lower bound, we can do it by omitting the upper bound, for example to match at least three characters we can write `{3,}`. Notice that we still need a comma, even when we don’t specify the upper limit.

```
let haStr = "Hazzzzah";
```

```
// Match a pattern that contains at least for 'z' characterslet haRegex = /z{4,}/;
```

```
let result = haRegex.test(haStr); // Returns true
```

### 28. Specify Exact Number of Matches

In the previous section I mentioned that we need a comma in `{3,}` when we specify only the lower bound. The reason is when you write `{3}` without a comma, it means that you are looking to match exactly 3 characters.

```
let timStr = "Timmmmber";
```

```
// let timRegex = /Tim{4}ber/;
```

```
let result = timRegex.test(timStr); // Returns true
```

### 29. Check for All or None

There are times when you might want to specify a possible existence of a character in your pattern. When a letter or a number is optional and we would use `?` for that.

```
// We want to match both British and American English spellings // of the word 'favourite'
```

```
let favWord_US = "favorite";let favWord_GB = "favourite";
```

```
// We match both 'favorite' and 'favourite' // by specifying that 'u' character is optionallet favRegex = /favou?rite/; // Change this line
```

```
let result1 = favRegex.test(favWord_US); // Returns truelet result2 = favRegex.test(favWord_GB); // Returns true
```

### 30. Positive and Negative Lookahead

‘_Lookaheads_’ are patterns that tell your JS to lookahead to check for patterns further along. They are useful when you’re trying to search for multiple patterns in the same strings. There 2 types of lookaheads — positive and negative.

Positive lookahead uses `?=` syntax

```
let quit = "qu";
```

```
// We match 'q' only if it has 'u' after it. let quRegex= /q(?=u)/;
```

```
quit.match(quRegex); // Returns ["q"]
```

Negative lookahead uses `?!` syntax

```
let noquit = "qt";
```

```
// We match 'q' only if there is no 'u' after it. let qRegex = /q(?!u)/;
```

```
noquit.match(qRegex); // Returns ["q"]
```

### 31. Reuse Patterns Using Capture Groups

Let’s imagine we need to capture a repeating pattern.

```
let repeatStr = "regex regex";
```

```
// We want to match letters followed by space and then letterslet repeatRegex = /(\w+)\s(\w+)/;
```

```
repeatRegex.test(repeatStr); // Returns true
```

Instead of repeating `(\w+)` at the end we can tell RegEx to repeat the pattern, by using `\1`. So the same as above can be written again as:

```
let repeatStr = "regex regex";
```

```
let repeatRegex = /(\w+)\s\1)/;
```

```
repeatRegex.test(repeatStr); // Returns true
```

### 32. Use Capture Groups to Search and Replace

When we find a match, it’s sometimes handy to replaced it with something else. We can use `replace()` method for that.

```
let wrongText = "The sky is silver.";
```

```
let silverRegex = /silver/;
```

```
wrongText.replace(silverRegex, "blue");
```

```
// Returns "The sky is blue."
```

### 33. Remove Whitespace from Start and End

Here’s a little challenge for you. Write a RegEx that would remove any whitespace around the string.

```
let hello = "   Hello, World!  ";
```

```
let wsRegex = /change/; // Change this line
```

```
let result = hello; // Change this line
```

If you get stuck or just want to check my solution, feel free to have a look at [the Scrimba cast where I solve this challenge](https://scrimba.com/p/peyvVAN/cZVvkH7).

### 34. Conclusion

Congratulations! You have finished this course! If you’d like to keep learning more, feel free to checkout [this YouTube playlist](https://www.youtube.com/playlist?list=PLWKjhJtqVAbleDe3_ZA8h3AO2rXar-q2V), that has a lot of JavaScript projects you can create.

Keep learning and thanks for reading!

You are now ready to play regex golf. ?

![Image](https://cdn-media-1.freecodecamp.org/images/sRhyrBTA9B-XwaBVwi00yiBYdaIX2rHopdBJ)
_From [https://xkcd.com/1313/](https://xkcd.com/1313/" rel="noopener" target="_blank" title=")_

