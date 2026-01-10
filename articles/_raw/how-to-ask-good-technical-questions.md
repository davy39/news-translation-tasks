---
title: How to Ask Good Technical Questions – the Ultimate Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-11T17:39:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-ask-good-technical-questions
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/raised-hand.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: communication
  slug: communication
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
seo_title: null
seo_desc: "By Nabil Tharwat\nKnowing how to ask effective technical questions is an\
  \ essential skill every software engineer should have. \nYou may be stuck with a\
  \ bug, unable to figure out why your program isn't working correctly, or you might\
  \ be having trouble l..."
---

By Nabil Tharwat

Knowing how to ask effective technical questions is an essential skill every software engineer should have. 

You may be stuck with a bug, unable to figure out why your program isn't working correctly, or you might be having trouble learning how to implement a certain algorithm.

In all of these situations (and more) you'll most likely go online and post a question on Stack Overflow, some community on Discord, a subreddit, a Facebook group, or even just send it to a friend. 

These tips will equip you with the knowledge to write questions that are easy to read and reason about, and that make it easier for someone to help you.

## Provide Context for Your Question

The first thing you should focus on is context. Context helps people understand your question better, because they'll know what situation you're dealing with and any parameters that might affect how they answer. 

Developers might not be able to guess what programming language you're using or what framework you're having trouble with. Or they might not understand your environment setup just by reading some code examples you've provided.

These contextual details make a difference if you want someone to answer your question, and many devs often overlook them despite their importance. 

For example, you may be using C++ 1999 and are trying to use a feature available only in C++ 2011. Provide this sort of context, otherwise people can end up looking at the wrong things when they're trying to help you.

## Sum Up Your Question

Sum up your question in a title. Just like Stack Overflow, each question should have a title that gets the basic point across. The title should be a relatively short summation of the question at hand. 

The title may not be enough to list all the details. But you should at least add enough details that just by reading the title, someone will be able to tell if they can help you with this issue or not.

This is important because people usually don't have enough time to actually go through the whole question (especially if your detailed question is several pages long). A punchy, helpful title is a time-aware summation that delivers just enough information to make an early decision.

For example, consider saying "Adding float and int using the + operator evaluates to int in C++11" instead of saying "C++ operators not working". By doing this, you provide enough context about the problem and introduce the problem itself.

## Create a Minimal Reproducible Example

Always include a minimal reproducible example if your question depends on code. This may be a complete GitHub repository, a gist, or even just a few lines of code.

You don't want to copy the whole project or the whole repository you're dealing with, but you need to add just the bits that someone would need to help you. 

If you're referring to a complete repository, make sure to let them know where to look. Then clearly state which specific files are affected, which functions in those files are broken, and so on. 

This example should be complete, meaning that it's sufficient to explain the problem and doesn't lack any imports, external modules, or functions. It has all the pieces that someone needs to be able to reason about the code. 

It should be minimal and have no irrelevant bits of code. Only show code that directly affects the example's completion and the issue at hand.

It should also be reproducible. I can't help you if I cannot reproduce the problem you're facing. This also takes context into account. Lacking enough context alongside examples makes it harder for people to answer your question.

## Include Any Restrictions and Constraints

Always mention restrictions and constraints. Not doing this sometimes leads to answers getting rejected because the answer goes beyond some constraint that you're not allowed to pass.

For example, you may be solving some assignment for school in which you're not allowed to use complex data structures. Someone may actually use those when providing an answer because you haven't listed those constraints. 

If you fail to mention this, you'll be wasting someone's time and yours as well. This is really frustrating and can cause people to ignore your question entirely. Always mention constraints and restrictions.

Sometimes you mistakenly set restrictions upon yourself, so it's useful to always elaborate on _why_ those restrictions exist in the first place. People might surprise you!

## Avoid Using Code Screenshots

If you're posting code screenshots alongside your question on social networks, chances are these images will be compressed. They'll become hard to read and may end up being completely unreadable because of how much code you've crammed into a single image and how much that image was compressed.

A poor quality image like that prevents developers from copying your code to try it themselves, forcing them to actually write down the code themselves just to start helping you. 

This is time-consuming and will likely push those developers away from answering your question – whereas they'd have probably been happy to help you if they were able to read the code in these screenshots in the first place.

Also, keep in mind that images aren't as accessible as text. You may be using a theme for your IDE that is hard to read for some people. Be aware of how accessible your question is to the community. 

If you must add code examples, then text is the best way to do it. Text will allow screen readers to actually read your question instead of saying something generic like "image". It'll also allow others to read the code in the comfort of their own browser theme (think Stack Overflow dark vs light themes).

There are many ways to share code. Many code hosting solutions exist such as Codepen, JSBin, GitHub Gist, Codesandbox, and Pastebin. 

You can also just embed the code into the question as text. This is natively supported with syntax highlighting on platforms like Stack Overflow and the freeCodeCamp forums. Some online communities require specific code hosting solutions, and you should follow those requirements.

## Share What You've Already Tried

List what you've actually tried already. You don't want to look lazy when asking a question. Your last attempt may be one tiny step away from fixing the problem. Without listing what you've tried, people will have to debug the problem from the very start.

Not listing what you tried often results in rejected answers as well because someone may end up suggesting something you already tried. It's frustrating and is not only a waste of time to you, but it's a waste of time to those who try to help you as well.

## Keep Your Sample Data Small

Often times we need sample data to test the code we're trying to run. This may be a JSON object response with hundreds of keys from some server or a SQL table with 10s or even hundreds of columns.

In this case, you should limit the amount of information you provide as sample data. Why include ten other columns if the problem is related to only one of them? Too much information will be hard to work with.

Try to limit the surface area of your code. Provide a simplified JSON object with a limited number of keys or a SQL table with only the columns related to the problem. This is easier to debug and easier to get started with.

## Format, Lint, and Document Your Code

No one wants to read code that is all on the same line with bad indentation, variable naming inconsistencies, or bad style in general. Follow popular conventions if possible. 

Variables and function names should convey what they're for. People want to be able to tell what a function does just by reading the signature. They don't want to decipher code before reading it.

If it's completely impossible to provide descriptive names, then make sure you have good documentation. Document what functions do, what variables are for, and how you intend to use them.

Try to use a linter as well. Linters are tools that go over your code, inspect it, and give feedback on possible logic improvements, style and convention violations, and overall help with code readability. 

In general, you don't want your code to look like this:

```
function someFunction ( p1,p2)
{
const b=p1+p2;
	console.log(b+p1*p2);
if( b > some_Const) throw 
			Error ( "something went wrong")
   else return 0;
}
```

but like this instead:

```javascript
function someFunction(p1, p2){
    const b = p1 + p2;
    
    console.log(b + p1 * p2);
    
    if(b > SOME_CONST) throw Error("Something went wrong");
    else return 0;
}
```

This kind of magic actually helps with reading the code and debugging the problem. It makes it easier to read and navigate. And you should always format your code anyway, regardless of whether you're posting it online or working on it alone. Trust me, it helps.

Many tools do this, but for web development, the most popular tools are Prettier and ESLint. They support a number of languages and work with several editors such as Atom, Vim, VSCode, Visual Studio, and others.

Almost all IDEs come with a built-in formatter and linter. Check the IDE you're using for those before reaching out to external tools. 

## Grammar-Check Your Question

Sometimes questions are hard to decipher because there are too many grammatical errors. This makes the question hard to read and limits the number of people that can help you. 

Platforms like Stack Overflow give editors the ability to improve questions, but you shouldn't depend on that. Other platforms don't have this kind of support, and thus it's generally best practice to grammar-check your questions before and after posting them.

Tools like Grammarly automatically scan your text and advise on improving the grammar or even correct complete grammatical errors. It has extensions for Firefox, Chrome, Safari, and Edge. Give it a shot.

## Keep Track of Your Question

One of the most frustrating things for people answering questions online is the lack of feedback. 

Once you ask a question and you get an answer, don't just desert the whole thing. Don't just ghost the people that are trying to help you. Provide feedback. Tell them what worked, what didn't work, and why.

Often times you may be left with a partial solution, but without feedback, you'll never get to the complete one.

Sometimes you will be asked for further information. You may have forgotten some of these tips, or you may not have provided enough information. Welcome feedback with a smile and give back.

And remember, people aren't paid for these services. They are paying with their time and effort to help you, so appreciate this and work with them to give them as much information as possible. It'll pay off eventually.

## Add a Summary

Generally, try to keep your questions short. Long questions take a lot of time and are often overlooked because of this. I'm not going to read 3 pages of a question with the possibility of getting deserted afterwards. 

In addition to summing up in the title, add a summary to the start of the question if it's too long. This will help readers by giving them a short version of your question instead of having to read the whole ting. 

It will also allow them to decide whether or not they want to continue reading the whole thing and whether they'll be able to help.

## We're All Human

You won't always get cheerful, welcoming, or happy responses. People have lives in which they could be facing problems. If you push people too much, they may start to ignore you or delete their responses altogether. Respect people's privacy, and give them space.

If you like this article don't forget to share it! You can find more of my content on my [blog](https://iamnabil.netlify.app/blog). Thanks for reading!

