---
title: strcmp in C – How to Compare Strings in C
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-04-27T20:32:00.000Z'
originalURL: https://freecodecamp.org/news/strcmp-in-c-how-to-compare-strings-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/max-duzij-qAjJk-un3BI-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
- name: functions
  slug: functions
seo_title: null
seo_desc: "Comparing strings is a common task in most programming languages. In C,\
  \ you can use the strcmp function to handle string comparisons. \nIn this article,\
  \ I will show you practical examples of the strcmp function, and offer insights\
  \ into how it compares..."
---

Comparing strings is a common task in most programming languages. In C, you can use the `strcmp` function to handle string comparisons. 

In this article, I will show you practical examples of the `strcmp` function, and offer insights into how it compares strings, what its return values mean, and how to use it effectively. 

You'll also see some best practices to help optimize your code.

## What are Strings in C?

Before we discuss the `strcmp` function, it is important to understand the basics of strings in C. 

A string is an array of characters terminated by a null character ('\0').   
Strings are usually represented either using character pointers ( `char *` ) or character arrays ( `char []` ).

## What is t**he `strcmp()` function of C, and how does it work?** 

The `strcmp()` function is part of the standard C library ( `string.h` ). Its primary purpose is to compare the characters of the two strings in sequence until it finds a mismatch or until the end of the strings is reached (that is, the null character '\0'). In our programming world, we call it [lexicographic order](https://en.wikipedia.org/wiki/Lexicographic_order)-based searching.

The function prototype for `strcmp` is as follows:

```c
int strcmp(const char *s1, const char *s2);
```

Here's what the parameters above mean:

* **s1** denotes the first string to be compared.
* **s2** denotes the second string to be compared.

`strcmp()` is like a game that compares two words. It helps us to identify whether a word comes before or after another word in the dictionary.

* If the first word (**s1**) comes before the second word (**s2**) in the dictionary, `strcmp()` gives a negative number.
* If the first word (**s1**) comes after the second (**s2**) word in the dictionary, `strcmp()` gives a positive number.
* If both words are the same, `strcmp()` gives the number 0.

`strcmp()` compares the corresponding characters from both strings based on their ASCII values, which are numeric codes that represent each character.

Therefore, if the ASCII value of the first differing character in the first string is less than the ASCII value of the corresponding character in the second string, `strcmp()` returns a negative number. This indicates that the first string comes before the second string in the dictionary. 

If the ASCII value of the first differing character in the first string is greater than the ASCII value of the corresponding character in the second string, `strcmp()` returns a positive number. This indicates that the first string comes after the second string in the dictionary.

If the two strings are equal up to the end of the shorter string, `strcmp()` returns a negative, zero, or positive value depending on whether the longer string has a character with a smaller, equal, or greater ASCII value than the null character.

Actually, the C compiler implements this logic of comparing the ASCII values of characters in two strings and returning the result accordingly.

## `strcmp()` Function Example #1 – Basic String Comparison

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "apple";
    char str2[] = "banana";

    int result = strcmp(str1, str2);

    if (result == 0) {
        printf("The strings are equal.\n");
    } else if (result < 0) {
        printf("String 1 is less than string 2.\n");
    } else {
        printf("String 1 is greater than string 2.\n");
    }

    return 0;
}
```

Output:

```
String 1 is less than string 2.
```

Let me now explain each of the lines from the code given above.

Here, I have taken two different strings as two different character arrays, as we do not have access to direct strings in the **C** programming language. 

In the first character string ( `str1[]` ), I have stored the string `apple`. In the second character string ( `str2[]` ), I have stored the string `banana`. As the function `strcmp()` gives a boolean output (true/false, or 0/1), I have taken another int variable named `result` to store the boolean value ( `1` for `true` and `0` for `false`).

The `strcmp()` function compares the two strings, and finds out that the first string `apple` comes before the second string `banana`. Therefore, the function `strcmp()` returns a negative value indicating that the first string is less than the second string. 

Based on the value in `result`, it prints `String 1 is less than string 2.`.

If you are confused about "the string comes before or after another string" then let me explain to you a bit more.

When we say that the first string comes before the second string, we mean that if the two strings were listed in a dictionary or a sorted list of words, the first string would appear before the second string.

In the case of the program above, the first string is `"apple"`, and the second string is `"banana"`. If we were to look up these two words in a dictionary, we would find that `"apple"` appears before `"banana"`, which means that the first string comes before the second string.

The `strcmp()` function compares the two strings character by character and determines which string comes first in the dictionary based on the ASCII values of the characters. 

In this case, the first character of `"apple"` (which is `'a'`) has a lower ASCII value (ASCII value for a = 97) than the first character of `"banana"` (which is `'b'` and the ASCII value for b = 98), so `strcmp()` returns a negative value, indicating that the first string comes before the second string.

I hope this clears up any confusion regarding what the phrase "one string comes after/before another string" means.

## `strcmp()` Function Example #2 – Case-insensitive String Comparison

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Apple";
    char str2[] = "apple";

    // Convert both strings to lowercase
    for (int i = 0; str1[i]; i++) {
        str1[i] = tolower(str1[i]);
    }
    for (int i = 0; str2[i]; i++) {
        str2[i] = tolower(str2[i]);
    }

    int result = strcmp(str1, str2);

    if (result == 0) {
        printf("The strings are equal.\n");
    } else if (result < 0) {
        printf("String 1 is less than string 2.\n");
    } else {
        printf("String 1 is greater than string 2.\n");
    }

    return 0;
}
```

Output:

```
The strings are equal.
```

Here I converted both strings into lowercase. I used a for loop to change all the characters in the string to lowercase using the function `tolower()`. The `for` loops convert both strings to lowercase by iterating over each character of the strings using an index variable `i`, and calling the `tolower()` function on each character to convert it to lowercase.

After converting both strings into lowercase, I called the function `strcmp()` to check whether both strings are equal or not, like earlier. I stored the output of the `strcmp()` function in a new variable named `result`, like earlier.

The `if` statement checks the value of `result` and prints out the corresponding message depending on whether the strings are equal, or which string is less or greater. Here, the two strings become equal after converting them to lowercase. Thus, the first `if` statement executes and provides the output.

Keep in mind that, after converting both strings to lowercase, the value of `str1` is `"apple"`, which is the same as the value of `str2` in the ASCII.

Therefore, when the `strcmp()` function is called, it returns `0`, which indicates that the strings are equal. This can be useful when we want to compare strings that may differ in case but should be considered equal.

## `strcmp()` Best Practices

Here are some best practices to follow when using the `strcmp()` function:

* Always include the `string.h` header when using `strcmp()`.
* To compare case-insensitive strings, use a custom function like `strcasecmp()` or a standard library function like `stricmp()`.
* Be cautious when comparing strings that may contain non-ASCII characters, as `strcmp()` uses the difference in ASCII values for comparisons, which might not work as expected for non-ASCII characters. In such cases, consider using a Unicode-aware comparison function or library. 

If you want to learn more about ASCII characters, check out [this article](https://www.freecodecamp.org/news/ascii-table-hex-to-ascii-value-character-code-chart-2/).

## Alternative String Comparison Functions

Apart from `strcmp()`, there are other string comparison functions available in the C standard library:

* `strncmp()`: Compares up to a specified number of characters of two strings. It is useful when you want to compare only a portion of the strings.
* `strcoll()`: This is quite interesting. Let me explain more about this.

The `strcoll()` function is like a game that helps us compare two words or strings, just like `strcmp()`. But `strcoll()` is designed to handle strings that contain non-ASCII characters or require language-specific comparisons, such as words from different languages.

`strcoll()` uses the rules for comparing words that are specific to the language or region, based on the current locale setting of the computer. In other words, it compares words according to the language-specific collation rules of the locale, which may be different from the standard ASCII ordering used by `strcmp()`.

For example, in the Spanish language, the word "cañón" (which means "canyon" in English) is sorted after "casa" (which means "house" in English), because the letter "ñ" is considered a separate letter in the Spanish alphabet, and comes after "n".

So, `strcoll()` can be useful for comparing words from different languages or regions that have specific collation rules, and we use this function for this kind of specific need.

## Conclusion

In this article, we've explored the `strcmp()` function in C, how it compares strings, and its return values. We've also looked at examples and best practices for using `strcmp` effectively. 

With this knowledge, you can easily compare strings in C like a pro. Remember to consider alternative comparison functions like `strncmp()` and `strcoll()` when working with specific use cases, such as partial or locale-specific string comparisons.

If this article helps you in any way, then let me know via [Twitter](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/). You can also follow me on [GitHub](https://github.com/FahimFBA) and check my [YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1), and [my website](https://fahimbinamin.com/). You can also [buy me a coffee](https://www.buymeacoffee.com/fahimbinamin) if you want to support me.

Cover: Photo by [Max Duzij](https://unsplash.com/@max_duz?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/programming?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

