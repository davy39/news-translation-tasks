---
title: What is Computer Programming? Defining Software Development.
subtitle: ''
author: Phoebe Voong-Fadel
co_authors: []
series: null
date: '2020-04-16T15:38:38.000Z'
originalURL: https://freecodecamp.org/news/what-is-computer-programming-defining-software-development
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/illustration_cover.png
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'My five year old son, Ramy, approached me one day while I was working from
  home and asked, “What are you doing Mama?”

  “I’m working,” I replied.

  He looked at my laptop screen and inquired again: “But what are you doing?”

  I paused and started to think ...'
---

My five year old son, Ramy, approached me one day while I was working from home and asked, “What are you doing Mama?”

“I’m working,” I replied.

He looked at my laptop screen and inquired again: “But what *are you doing*?”

I paused and started to think about this. I’m a web developer and I’m programming in JavaScript. How do I explain this to a five year old?

“I write instructions for the computer and the computer does what I tell it to do. This is called programming,” I explained. Ramy looked puzzled.

I continued, “For example, I can give the computer instructions to add two numbers and it will give me the answer.” I wrote a function which added 2 + 2 and showed him the answer on my screen. His eyes lit up.

From that point, I started to think *what is programming*? What actually happens under the hood? When I first started to learn to code in 2017 on [freeCodeCamp](https://www.freecodecamp.org/), I used the inbuilt code editor on the website and would see the results. However, I didn’t really understand the magic that was going on behind the scenes.

I started doing some research and these were some of the terms I searched for: “What is computer programming? What is software?” There are over 600 million search results on Google for “What is Computer Programming?” It's a bit like going down a rabbit hole – it can be complicated and overwhelming.

I wanted to put together a comprehensive introduction to what computer programming and software development is for beginners. I will start with computer programming and then cover computer programming languages. Then I’ll talk about software and software development. Finally, I’ll move onto the current trends and the future of computer programming.

If you’re thinking about transitioning into the world of programming or are just interested in learning to code, then this will provide you with a general overview, without (too much!) technical jargon.

Just one thing to note: you can use the words “Developer” and “Programmer” to mean someone who writes code.

## What is Computer Programming?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_input_output.png align="left")

On Wikipedia, the definition of “Computer Programming” is:

> *“Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result.”*

But what does that mean?

A computer itself isn’t smart. Yes they’re powerful and have the potential to carry out tasks much faster than a human. But computers need a human to write instructions and tell them what to do.

Therefore, programming is the process of writing those instructions. We use a programming language to do this. These instructions are translated to a readable format which a computer can understand. The instructions are then carried out by the computer.

## Programming how to make a cup of tea

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_programming_tea.png align="left")

Let’s take making a cup of tea as an example. If you were to give instructions on how to make a cup of tea, it would look like the following:

1. Boil some water
    
2. Pour hot water in a cup with a teabag
    
3. Let the tea brew
    
4. Remove the teabag
    
5. Add milk and/or sugar (if desired)
    

Simple, right?

What we take for granted is that communication with a human being is different than communicating with a computer. A human has prior knowledge and life experience – they may know where to find the tea. We assume they know that milk is stored in a fridge.

Humans also have intuition. If you can't find a cup you might then search the cupboards instead. There’s also reading people’s non verbal cues like body language.

When it comes to programming, you have to be **very** specific. Continuing with how to make a cup of tea, you might write instructions in [pseudo-code](https://en.wikipedia.org/wiki/Pseudocode) like this:

1. Go to the kitchen
    
2. Locate the kettle
    
3. Open the lid of the kettle
    
4. Fill the kettle with water
    
5. Turn the kettle on
    
6. Wait for it to boil to 100 degrees Celsius
    
7. Find a cup
    

And so forth.

What if instructions like the ones above are not enough? You may need to add some *logic* to account for all scenarios. For example: 2) Locate the kettle. Well, is it an electric kettle or is it a kettle you put on a hob? You’ll need to add a condition that **if** it is an electric kettle, then do xyz. **Otherwise**, do xyz for a kettle that you put on a hob.

Even when you think that you’ve accounted for every possible condition and given very specific instructions, there are things that you may not foresee. You start making your cup of tea and something goes wrong. Oh no! Your kettle stops working after you start boiling it.

What happened? There’s a bug in your code! A bug is an error or flaw in your code which might lead to unexpected results. In order to fix your code, you go through a process of “[debugging](https://en.wikipedia.org/wiki/Debugging)”, which is where you find the problems in your code and resolve the issues.

In this case, your instructions didn’t include filling up your kettle to 0.8 litres to cover the heating element. So the kettle switches off as a safety measure.

To prevent errors from happening after you run your program, developers carry out testing and [unit-testing](https://en.wikipedia.org/wiki/Unit_testing) on their programs. Unit-testing is where you write tests for parts of your code. The tests either fail or pass.

For example, you write a function which adds two numbers: 1 + 1. You then write a unit test where the expected output is 2. All answers will fail unless it's 2.

You go through your code until everything runs without any unexpected problems. Programming is therefore a detailed oriented and iterative process where you are continuously improving what you have previously written.

## How does your computer understand your code?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_low_high_languages.png align="left")

What most programmers write as “code” is a [high level programming language](https://en.wikipedia.org/wiki/High-level_programming_language). It is [abstract](https://levelup.gitconnected.com/what-is-abstraction-in-programming-2f35c8c72e15) by design. Abstraction in this context means that we are moving further away from machine code and programming languages are closer to spoken languages.

But a computer can’t understand text based code. It needs to be compiled (translated) into [machine code](https://en.wikipedia.org/wiki/Machine_code). Machine code is a set of instructions which can be understood by a computer’s [central processing unit](https://en.wikipedia.org/wiki/Central_processing_unit) (CPU). Think of the CPU as the brain of a computer. Machine code is made up of ones and zeros. This is called binary.

For example, this is how you would write “Hello World” in binary:

`01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100`

As you can see, binary is not easily readable for humans, so we tend to avoid programming in machine code!

## What exactly is a programming language?

Programming languages fall both within the spectrum of low-level languages, such as assembly, and high level programming languages, such as JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_spoken_programming_lang.png align="left")

But what is a programming language exactly? The best analogy I can think of are the spoken languages we use today. All languages express the same idea, but in different ways to another person:

English: Hello

French: Bonjour

Spanish: Hola

Programming languages are different ways of expressing the same idea, but to a computer instead. The following will print out “Hello” in three different programming languages:

JavaScript: `alert(“Hello”);`

Python: `print(“Hello”)`

Perl: `print "Hello";`

Each programming language has its own [syntax](https://en.wikipedia.org/wiki/Syntax_\(programming_languages\)). In English, we have grammar. The same applies to programming languages – they each have their own set of rules.

## How do you know if a programming language is a programming language?

This might seem like an odd question to ask. Is all code written in a programming language? Technically, no. For example, there is a misconception that [HTML](https://en.wikipedia.org/wiki/HTML) (HyperText Markup Language) is a programming language. It is in fact a “[declarative](https://en.wikipedia.org/wiki/Declarative_programming)” language, which according to Wikipedia is:

> *“...a style of building the structure and elements of computer programs - that expresses the logic of computation without describing its control flow.”*

In other words, HTML provides the structure of a web page, but doesn’t control how the website behaves or functions.

You can determine if a language is a programming language by whether it’s “Turing complete”. The [Turing Machine](https://en.wikipedia.org/wiki/Turing_machine) is a hypothetical machine described by Alan Turing in 1936. For a programming language to be [Turing complete](https://en.wikipedia.org/wiki/Turing_completeness) it needs:

1. Conditional branching (which I explore below).
    
2. The ability to read and write to an infinite paper tape. This essentially means being able to store data in memory.
    

I’m not going to explore this topic deeply, but if you are interested this [video](https://www.youtube.com/watch?v=RPQD7-AOjMI) is a helpful introduction.

## What are the fundamentals of a programming language?

There are some basic elements which are commonly featured. This includes variables, loops, conditional statements, data structures and algorithms. These are the building blocks of most programming languages.

### What is a 'for loop'?

For loops are useful if you have to execute a set of instructions repeatedly. For example, you have afternoon tea and have to make five cups of tea for your guests. In order to make one cup of tea, you have to follow a set of instructions, like my earlier example.

Instead of writing the instructions five times, you can tell the computer to loop through the same instructions five times. This enables you to scale.

Below is an example of a basic `for` loop:

```js
for (let i = 0; i < 5; i++) {
  console.log("Make Tea!");
}

//expected output: 
"Make Tea!"
"Make Tea!"
"Make Tea!"
"Make Tea!"
"Make Tea!"
```

### What is a conditional statement?

In JavaScript we have `if...else` conditional statements. These are used when you want to execute different actions based on a condition.

Going back to my earlier example, you ask the user **if** they want milk in their tea. **If** they do want milk, then add milk to tea, **else** do nothing.

Here is an example of an `if...else` statement in JavaScript:

```js
if(milk == true) {
  // add milk
  } else {
  // don't add milk
}
```

### What are data structures?

> *“A data structure is a way of organizing data so that it can be used effectively...They are essential ingredients in creating fast and powerful algorithms.”*

([Data Structures Easy to Advanced Course, William Fiset](https://www.youtube.com/watch?v=RBSGKlAvoiM))

Common [data structures](https://en.wikipedia.org/wiki/Data_structure) that you can find across many programming languages are arrays, objects, tuples, and unions. I’ll take arrays as an example.

In JavaScript, an array can store a range of data such as numbers and strings (text). I love biscuits with my tea so I’m going to store them in my array:

```js
biscuits = [“shortbread”, “digestive”, “ginger nut”];
```

These biscuits are stored in the computer’s memory and you, as a developer, can access a specific biscuit by referencing its [index](https://simple.wikipedia.org/wiki/Array_data_structure). You start counting the index from 0. The index is like the biscuit’s position in a biscuit tin. You reference it by using the square bracket notation.

```js
biscuits[0]; // “shortbread”
biscuits[1]; // “digestive”
biscuits[2]; // “ginger nut”
```

If you want to get a digestive biscuit, you can access its index position: `biscuits[1]`. I can easily find it because I know where it’s stored.

Remember that the first item of the array is index 0. So when you refer to index 1, it’s actually the second item of the array.

Therefore, data structures are a way to manage data. This includes storing and retrieving data. It’s more efficient to execute algorithms if data is organised in a data structure.

### What is an algorithm?

An [algorithm](https://simple.wikipedia.org/wiki/Algorithm) is a specific set of instructions that solves a problem. It’s an abstract concept. Here’s a link to a short video from TED on "[What is an Algorithm?](https://youtu.be/6hfOvs8pY1k)".

Remember when we were writing instructions on how to make a cup of tea earlier? That is essentially an algorithm: a set of sequential instructions.

When I wrote my first function in JavaScript, I actually created my first algorithm without knowing it was an algorithm! A function is an implementation of an algorithm.

Just like in real life, there are often multiple solutions for a coding problem. For example, say you’re planning on going to a cafe that you’ve never been to before. There are several ways of getting to your destination. Some routes take longer than others, but ultimately, they all get you to the same place. Ideally you want to pick the quickest, most efficient, and easiest route.

The same principle can be applied to programming. There are usually a few ways to solve a coding problem, and programmers strive to find the most elegant and efficient solution.

Developers often don’t get it right on the first try! Just as I would write a first draft for an article, it’s the same for coding. I would redraft an article several times, where I may change the structure, edit, rewrite sections, and cut out unnecessary sentences. In programming we go through a similar process, and we call this [refactoring](https://en.wikipedia.org/wiki/Code_refactoring) our code.

## What are the main programming languages used today? How many are there?

There seems to be some debate on the total number of programming languages on the internet. Some websites such as [Wikipedia](https://en.wikipedia.org/wiki/List_of_programming_languages) list approximately 700 of “all notable” current and historical programming languages. Other sites such as [Tiobe](https://www.tiobe.com/tiobe-index/programming-languages-definition/#instances) track and monitor 250 of the “most popular” languages.

On [Github](https://github.com/), the most popular programming language of 2019 was JavaScript:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/github-most-popular-languages.png align="left")

*Source:* [*https://octoverse.github.com/#top-languages*](https://octoverse.github.com/#top-languages)

### Why are there so many programming languages? How have programming languages evolved?

Different programming languages are developed to satisfy different needs. This is demonstrated throughout the history of programming languages. Please refer to this diagram by O’Reilly which maps out the [history of programming languages from the 1950s to 2004](https://www.cs.toronto.edu/~gpenn/csc324/PLhistory.pdf).

In the mid 1950s, FORTRAN (Formula Translation) was created to work out complex mathematical, statistical, and scientific problems. COBOL (“Common Business Oriented Language”) was created in 1959 to make it easier for businesses to use code. There are some languages which are more suited for doing statistical analysis such as R (1976).

There was the rise of general purpose programming languages from the 1970s onwards, such as C, C++, C# and Java. As you can see in the chart above, general purpose languages dominate the top 10 most popular languages.

JavaScript, created in 1995, is a popular language for the web. It gives websites their interactivity and life.

More recently, we’ve seen the birth of new languages such as Go from Google, which was intended to maintain large software systems more efficiently. We'll probably see even more programming languages created in the future.

## Compiled vs. interpreted programming languages

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_compiled_interpreted.png align="left")

As you start to become more familiar with programming languages, you will come across compiled and interpreted programming languages. What is the difference?

### What is a compiled language?

Programming languages such as C, C++, and Java have a “build” process where your code is compiled down to a more readable format (machine language) for the computer.

It might be easier to think of two people who don’t speak the same language, but they have to work together. John speaks English and Chloe speaks French. Chloe writes a set of instructions on how to make a chocolate soufflé in French, but John can’t understand it. They need a translator that can speak both English and French. It’s easier if the translator can translate Chloe’s instructions in advance before they start cooking together.

Instead, developers “speak” a programming language like Java or Python. They need their code to be compiled (translated) to machine language before a program can run so the computer can understand it.

Programs made from a compiled language are easier for a computer to understand, and therefore run very quickly.

### What is an interpreted language?

JavaScript, PHP, and Python are examples of interpreted programming languages. There’s no build process and the code doesn’t need to be compiled. Your code is being interpreted or read line by line as you run the program.

Back to my analogy of Chloe and John. John writes down a set of instructions on how to make a shepherds pie. The translator doesn’t translate John’s instructions in advance, but instead joins them for their cooking session. The translator translates each line of John’s instructions from English to French as Chloe cooks. Because of this, it takes longer for Chloe to prepare and cook the meal.

Therefore, interpreted languages are slower than compiled languages. They have to be translated on the fly so the computer can understand.

But with [just-in-time](https://blog.sessionstack.com/how-javascript-works-inside-the-v8-engine-5-tips-on-how-to-write-optimized-code-ac089e62b12e) (JIT) compilers, interpreted languages are becoming faster and more efficient.

## Which programming language(s) should I choose to learn?

Programming languages pretty much do the same thing, but they are just different ways of expressing the same instructions to a computer. Once you've grasped the concepts and fundamentals of one programming language, the learning curve for learning another language won't be as steep.

The programming language you should choose to learn first depends on a number of factors. For example, I wanted to be a web developer, so I chose JavaScript as my primary programming language. Other languages for the web you can learn are PHP and Ruby on Rails.

If you want to become a data scientist, then Python might be an option. Python is considered one of the best data science tools to analyze [big data](https://en.wikipedia.org/wiki/Big_data). I mentioned R earlier, which is another language used widely amongst data scientists and statisticians.

Python is a general purpose programming language, and is also useful to learn if you want to get into the field of Machine Learning and Artificial Intelligence.

If you want to become a Software Engineer then Java could be an option. Java is one of the most popular and in demand languages in the world. It's a versatile language which can be used for developing small to large enterprise software.

So think about what role in tech you would like and what kind of companies you want to work for.

Choosing a programming language also depends on what software you’re trying to build. This leads us nicely to our next section.

## What is software?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_software_everywhere.png align="left")

How many times do you interact with software on a given day?

Software is everywhere. It’s integrated as [embedded systems](https://en.wikipedia.org/wiki/Embedded_system) into everyday devices such as your microwave, washing machines, cars, TVs, children’s toys, and remote controls. Then there’s more obvious computer related devices which have [application](https://en.wikipedia.org/wiki/Application_software) and/or [system](https://en.wikipedia.org/wiki/System_software) software such as tablets, smart phones, laptops, desktop computers, and home assistants like Alexa.

The average person probably interacts with software a few dozen times a day, if not more. It is part of our daily life.

All software is programmed by a developer. Software is agile by nature and can constantly iterate. Software and hardware are intertwined. Imagine your phone without its apps and operating system. The phone would essentially be an expensive brick! Therefore, software gives hardware life and hardware is how we interact with software.

The majority of software that’s created by programmers is written in a high level programming language.

### What is software development?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_software_development.png align="left")

[Software development](https://en.wikipedia.org/wiki/Software_development) is everything from the conception of an idea to development and deployment. This process, from conceiving an idea to deploying software, is also known as the software life cycle.

There are several stages of the software life cycle: discovery, design, programming/creation, testing, and deployment/execution. It also includes everything else in the software development ecosystem such as maintenance, documentation, and bug fixes.

I won't go into detail here, as the subject of software development warrants its own article.

## Current trends in Software Development and Computer Programming

### Artificial Intelligence and Machine Learning

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_machine_learning.png align="left")

In recent years you’ve probably heard of terms like artificial intelligence and machine learning. Sometimes they’re used interchangeably, but are they the same?

No, they’re not quite the same thing. Machine learning is where a machine learns through experience. Whereas artificial intelligence is a broader idea that machines can execute tasks intelligently. Machine learning is a subset of Artificial Intelligence.

### What is Artificial intelligence?

I’ve covered how programming languages work – the programmer writes a set of instructions for the computer to execute. Artificial Intelligence (AI) is a broader concept where computers can mimic the way a brain functions. It’s training a machine to “think” like a human.

The big question is: can you replicate human intelligence in a machine? Can you mimic the way a human learns, reasons, and perceives? Alan Turing asked this question in his article in 1950:

> *“Can machines think?”*

([Computing Machinery and Intelligence](https://phil415.pbworks.com/f/TuringComputing.pdf), 1950 by Alan Turing)

In Turing’s article he proposed the “Turing test” in which a machine would be classed as “intelligent” if a person could not tell the difference between the responses of a human and the artificially intelligent machine.

After 70 years, AI developers, academics, scientists and researchers are still trying to answer this question and create an artificially intelligent machine. I don’t think we’re there yet. Have you tried having a conversation with Siri or Alexa? Conversations with these two devices are still basic. However, I’m sure it’s just a matter of time before the technology improves.

Companies like [DeepMind](https://deepmind.com/) are researching this concept and whether machines are capable of intelligence. DeepMind’s [AlphaGo](https://deepmind.com/research/case-studies/alphago-the-story-so-far) program made the headlines when it beat a professional player at Go. This was a huge milestone for AI.

### What is Machine Learning?

[Machine learning](https://en.wikipedia.org/wiki/Machine_learning) (ML) is a subset of artificial intelligence. ML is a different way of programming. It is the idea that the computer has the ability to learn without being explicitly programmed. Arthur Samuel first came up with the idea of machine learning in his [paper](https://www.semanticscholar.org/paper/Some-Studies-in-Machine-Learning-Using-the-Game-of-Samuel/e9e6bb5f2a04ae30d8ecc9287f8b702eedd7b772) in 1959:

> *“Programming computers to learn from experience should eventually eliminate the need for much of this detailed programming effort.”*

When I was teaching my son how to recognize a cat, I would show him pictures of cats. I did this repeatedly until he was able to recognize a cat without me prompting him.

Machine learning is similar to this. You give your computer a hundred images (input) of cats. It then learns the patterns in the data and builds a classification system through repetition. If you give your computer more images of cats and other animals, it should be able to identify whether the animal in the picture is a cat or not a cat. It has essentially learned what a cat should look like.

ML is giving your computer data and examples, and in turn, it’s able to learn for itself like babies and young children do. Instead of developers giving the instructions to a computer, the computer creates its own set of instructions to follow – machine learning algorithms. Machine learning algorithms is a subset of ML, a concept known as [“Deep learning”](https://en.wikipedia.org/wiki/Deep_learning).

> “AI is one of the most profound things we’re working on as humanity. It’s more profound than fire or electricity...”

(Sundar Pichai, [World Economic Forum](https://www.youtube.com/watch?v=sqd516M0Y5A), January 2020)

The quote from Sundar Pichai, the CEO of Alphabet Inc, summaries the importance of AI and ML.

## What is the future of computer programming?

This final section will be my predictions on the future of computer programming.

Developers will continue to create new programming languages. Programming languages will become more abstract and, therefore, accessible to individuals learning to code.

I believe there will be greater importance placed on coding and programming education in primary and secondary school curricula. The demand for developers and programmers will only increase as technology and software becomes ever more integrated in our daily lives. Programming will become ubiquitous.

We will see the continual rise and popularity of ML and AI to assist developers in the software development process. This includes automating testing, along with detecting and preventing vulnerabilities and bugs.

AI will revolutionize all aspects of our society, not just in programming and software development. For example, we’ve seen great strides in the area of AI and self driving cars.

One of the world’s leading companies developing self driving cars is [Tesla](https://www.tesla.com/), founded by Elon Musk. With the supervision of a human driver, a Tesla car can now automatically change lanes, navigate autonomously on limited access freeways, and the owner can summon the car to and from a garage or parking spot. Tesla's goal is to create a fully automated, self driving car without any human supervision.

As machines become more intelligent, we may come to a point where machines surpass the intelligence of human beings. This is referred to as [singularity](https://en.wikipedia.org/wiki/Technological_singularity). It may seem like complete science fiction at the moment! But notable figures such as [Ray Kurzweil](https://en.wikipedia.org/wiki/Ray_Kurzweil) predict that machines with human level intelligence will be available within the next 20 years. Kurzweil is known for his accurate predictions of how technologies will progress. He wrote a book on this: [The Age of Spiritual Machines](https://en.wikipedia.org/wiki/The_Age_of_Spiritual_Machines).

How will our society change as a result of super intelligent machines?

## Final words

![Image](https://www.freecodecamp.org/news/content/images/2020/03/illustration_ending_illustration.png align="left")

Technology influences and code touches almost every part of our lives. From our choice of entertainment (online games, streaming) and how we shop, to choosing what we eat and even how we date! Code is important and more jobs will shift and require people to have at least some basic understanding of programming.

Yet there are only approximately 23.9 million developers in the world according to the [Global Developer Population and Demographic study 2019](https://evansdata.com/reports/viewRelease.php?reportID=9). To put this in perspective, only **0.3%** of the world’s population knows how to program. As I discussed earlier, our dependency on software and technology is increasing. According to the [US Bureau of Labor statistics](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm#tab-6), the demand for software engineers is expected to grow by 21% from 2018 to 2028. Therefore, we need to increase the number of developers.

If you’re thinking about becoming a developer, start today. It is an incredibly exciting time to do so! There are many learn-to-code resources online. There are self-paced platforms like [freeCodeCamp](https://www.freecodecamp.org/). There's also a great [post by Laurence Bradford](https://learntocodewith.me/posts/code-for-free/) which compiles all the best resources to learn to code for free. Do some research and find out which resource suits your learning style.

If you have any questions or just want to say hello, find me on Twitter [@PhoebeVF](https://twitter.com/PhoebeVF).

*A special thanks to Katerina Limpitsouni from* [*Undraw*](https://undraw.co/) *for creating the illustrations for this article.*
