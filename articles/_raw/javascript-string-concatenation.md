---
title: How JavaScript String Concatenation Works – the "+" Operator vs the "+=" Operator
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-09-07T18:50:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-concatenation
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/pexels-francesco-ungaro-96081--1-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'String concatenation is a common task that we do often. String concatenation
  is the operation of joining character strings end-to-end. For example, the concatenation
  of "snow" and "ball" is "snowball".

  In this article, I will be showing two methods b...'
---

String concatenation is a common task that we do often. String concatenation is the operation of joining character strings end-to-end. For example, the concatenation of "snow" and "ball" is "snowball".

In this article, I will be showing two methods by which you can concatenate strings in JavaScript. I will also make sure to clarify when you should use each method. 

Also, I will provide you with a good exercise from freeCodeCamp to practice this concept. If you are interested in watching a step-by-step video explanation, then you are also in the right place!

I recently tweeted about this, and and as I promised, I have created a video and now I am writing this article for you. Check out the Twitter thread also:

%[https://twitter.com/Fahim_FBA/status/1699144812602220569?s=20]

Make sure to follow me on [Twitter/X](https://twitter.com/Fahim_FBA) to get the latest updates about my new videos or articles.

## Video Walkthrough:

Now is the moment you may have been waiting for: yes, it is a video, and I have specially prepared it just for you.

%[https://youtu.be/9eZMdTvvbJk]

Let me know if you like the video presentation in the video's comment section. Also, make sure to [subscribe to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1).

## Working with Strings

Before talking about string concatenation, let us talk about some basic stuff.

Let's say, I want to print my full name but I do not want to input my full name all at once. Check the example below:

```javascript
myName = "Md. Fahim ";
myName2 = "Bin Amin";
console.log(myName); // Md. Fahim 
console.log(myName2); // Bin Amin
```

My full name is "Md. Fahim Bin Amin". I have broken it down into two parts or you can say in two halves. Therefore, `myName` contains my first name, `"Md. Fahim "` with a space at the end so that I can have a leading space before printing my last name. But you can add this space as a leading space in the second string also.

`myName2` contains my last name, `"Bin Amin"`. Then I printed two variables' values. Therefore, I got two separate lines containing my full name. But it does not look good to print a person's name in two different lines, right?

Let's solve this issue now. There are many ways to do that, but we are going to use **String Concatenation** methods. We are going to learn two different approaches to using string concatenation along with the suitable usage for each of them.

## String Concatenation Method 1 – Using the `+` Operator

This is the simplest method: it uses the `+` operator. Let me give you an example first, and I promise that it will be crystal clear for you once we go through it.

Let's say I am creating a new variable named `fullName` for storing my full name. But as earlier, instead of using my full name in the double quotations, I will use separate strings.

```javascript
fullName = "Md. Fahim " + "Bin Amin";
console.log(fullName); // Md. Fahim Bin Amin
```

Here, I have provided two separate strings in a single string variable, but I used the plus ( `+` ) operator to append the second string at the end of the first string. Here `"Md. Fahim "` is the first string, and `"Bin Amin"` is the second string.

Since I want a space between the two separate strings, I have added a trailing space in the first string. But you can also add a leading space in the second string instead of adding a trailing space in the first string, as I mentioned above. 

It is important to note that the order of the strings always matters in String Concatenation.

For example, if I change the order (give the second string before the first string) in the `fullName` variable, then the whole string also gets a different orientation and I will not get the result I want (it prints my name wrong!).

```javascript
fullName =  "Bin Amin" + "Md. Fahim ";
console.log(fullName); // Bin AminMd. Fahim 
```

It always considers the string that appears first as the first string and appends the next string at the end of that first string. It keeps going on each time like this – it doesn't matter how many individual strings you want to append in a single string variable.

```javascript
fullName =  "Bin Amin " + "Md. Fahim" + " My name is";
console.log(fullName); // Bin Amin Md. Fahim My name is
```

Ah! It looks awful. Let me correct the orientation now:

```javascript
fullName = "My name is " + "Md. Fahim " + "Bin Amin";
console.log(fullName); // My name is Md. Fahim Bin Amin
```

Now it is better.

## String Concatenation Method 2 – Using the `+=` Operator

This method is very handy. When using it, we append separate strings in separate lines. Let me give you an example again.

I will use a variable named `fullName` like earlier, but instead of using the `+` operator to concatenate strings like earlier, I will use `+=`:

```javascript
fullName = "Md. Fahim ";
fullName += "Bin Amin";
console.log(fullName); // Md. Fahim Bin Amin
```

In the first line, I have stored my first name in the `fullName` variable. In the second line, I have stored my last name in that same variable but using the `+=` operator (which is actually the combination for `fullName = fullName + "Bin Amin"`). It appends the second string at the end of the first string like earlier.

This lets me print my full name on a single line.

 `+=` is a combination, so direct usage of the generic way also works the same as below:

```javascript
fullName = "Md. Fahim ";
fullName = fullName + "Bin Amin";
console.log(fullName); // Md. Fahim Bin Amin
```

But you can pretty much assume that using `+=` will be the easier and more compact way. So I recommend you to use the `+=` operator directly.

### What's the Difference?

I know you may be getting confused and thinking that if these methods give the exact same result, why you should learn both of them? What are the specific use cases for each one?

Hold your horses! I am going to answer your question right now.

Follow the code below where I am using the 1st method:

```javascript
fullParagraph = "This is the first line of the paragraph. " + "This is the second line of the paragraph. " + "This is the third line of the paragraph. ";
console.log(fullParagraph); // This is the first line of the paragraph. This is the second line of the paragraph. This is the third line of the paragraph.
```

Here I have taken a variable named `fullParagraph` and I have stored three individual strings/sentences in it. The output is accurate, but you see that based on the number of adding new strings/sentences, the one line for storing the data in that specific variable is getting longer. 

The more strings or different sentences you add for string concatenation using the first method, the longer a single statement becomes. As such, it becomes very boring and hard to inspect later on.

Here comes the second method to the rescue! 😉

Follow the code below where I am using the 2nd method:

```javascript
fullParagraph = "This is the first line of the paragraph. ";
fullParagraph += "This is the second line of the paragraph. ";
fullParagraph += "This is the third line of the paragraph. ";
console.log(fullParagraph); // This is the first line of the paragraph. This is the second line of the paragraph. This is the third line of the paragraph.
```

Here I have taken a variable named `fullParagraph` and stored individual strings in individual lines. As usual, I can easily append newer strings in new lines using the `+=` operator. 

Since I'm taking a new line for appending new strings each time, it doesn't create any hassle for me. Also, each individual statement is short and it is very easy to read or inspect later on. The code also looks pretty clean.

Keep in mind that the order of strings of course matters in each method. That means they always follow the orientation of the order of the strings during appending (String Concatenation).

### When to Use Each Method

I guess you already know this answer. But, still, for the sake of this article, let me clarify it again.

If you are using any string concatenation where the individual strings are comparatively smaller or you know they'll remain small in size, then you can directly go for the first method.

But if you know that you might need to append longer strings later on, then you should use the second method.

That's it!

## Practice String Concatenation

You can practice this concept [using this freeCodeCamp exercise](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/concatenating-strings-with-the-plus-equals-operator).

## Conclusion

I hope you have enjoyed this short article. It takes a lot of time and effort to write an in-depth article and create videos for you. So let me know whether these are helping you or not.

Let's connect on [LinkedIn](https://www.linkedin.com/in/fahimfba/). Please make sure to endorse me on the relevant skillset. Also getting recommendations from you always makes me happy! 😊

If you have any questions then please let me know by reaching out on [Twitter](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can also follow me on:  
🎁GitHub: [FahimFBA](https://github.com/FahimFBA)  
🎁YouTube: [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

If you are interested then you can also check my website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

Cheers! 🍻

