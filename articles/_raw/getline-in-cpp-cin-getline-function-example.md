---
title: Getline in C++ – cin getline() Function Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-04T20:06:07.000Z'
originalURL: https://freecodecamp.org/news/getline-in-cpp-cin-getline-function-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/getline.png
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: 'In this article, we''ll talk about the getline() function in C++. This
  is an inbuilt function that accepts single and multiple character inputs.

  When working with user input in C++, the cin object allows us to get input information
  from the user. But ...'
---

In this article, we'll talk about the `getline()` function in C++. This is an inbuilt function that accepts single and multiple character inputs.

When working with user input in C++, the `cin` object allows us to get input information from the user. But when we try to log out the user's input that has multiple values, it only returns the first character.

This happens because the C++ compiler assumes that any white space terminates the program when getting the input. That is, "My name is Ihechikara" would only return "My" when logged out. 

Here is a better example:

```c++
#include <iostream>
using namespace std;

int main() {

    string bio;
    
    
    // Information logged to the console
    cout << "Tell us about yourself: ";
    
    
    /* This prompts the user to input a string and I typed in this: 				"JavaScript is my favorite language"
    */
    cin >> bio;
    
    
    /* When logging out the bio inputed above, only "JavaScript" was logged 		out
    */
    cout << "Your bio says: " << bio;
    // Your bio says: JavaScript 

    
}
```

In the code above, the user is asked to input their bio. They went on to input "JavaScript is my favorite language". But when the bio was logged to the console, only "JavaScript" was logged out.

Next, we'll see how to use the `getline()` function to get the rest of the characters in the string.

## C++ getline() Function Example

In this section, we'll see a practical example of using the `getline()` function.

```c++
#include <iostream>
using namespace std;

int main() {

    string bio;
    
    cout << "Tell us about yourself: ";
    
    getline(cin, bio);
    
    cout << "Your bio says: " << bio;
}
```

In the example above, we passed in two parameters in the `getline()` function: `getline(cin, bio);`. The first parameter is the `cin` object while the second is the `bio` string variable. 

When you run the code, you'll be prompted to input some text. After you've done that, hit enter and see the output that has all the text from your input instead of just the first character.

In my case, I typed in a string with multiple characters and got it logged out to the console. Go on and try it to see how it works.

With this, you can work effectively with user inputs in your programs.

## Conclusion

In this article, we talked about the `getline()` function which enables us get multiple characters from a user's input. 

We first saw what happens when we get a string with multiple characters from a user – only the first character is returned.

We then saw how to get all the characters from the string using the `getline()` function which takes two parameters – the `cin` object and the string variable.

Happy coding!

