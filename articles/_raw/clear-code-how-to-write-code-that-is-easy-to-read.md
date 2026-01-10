---
title: Clear Code – How to Write Code That Is Easy to Read
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2022-11-28T12:26:28.000Z'
originalURL: https://freecodecamp.org/news/clear-code-how-to-write-code-that-is-easy-to-read
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/cafe-gc5d844b68_1280.jpg
tags: []
seo_title: null
seo_desc: 'This article is a follow up to a tweet I made on how I deal with my poor
  ability to remember code. It may seem funny to you, but I do actually tend to forget
  what I write shortly after writing it.

  https://twitter.com/wiseAss301/status/159118167805122...'
---

This article is a follow up to a tweet I made on how I deal with my poor ability to remember code. It may seem funny to you, but I do actually tend to forget what I write shortly after writing it.

%[https://twitter.com/wiseAss301/status/1591181678051229696?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1591181678051229696%7Ctwgr%5E0c73a629a6c4b95546c3202d41070cd1ff69b172%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext2Fhtmlkey%3Da19fcc184b9711e1b4764040d3dc5c07schema%3Dtwitterurl%3Dhttps3A%2F%2Ftwitter.com%2Fwiseass301%2Fstatus%2F1591181678051229696image%3Dhttps3A%2F%2Fi.embed.ly%2F1%2Fimage3Furl3Dhttps253A252F252Fabs.twimg.com252Ferrors252Flogo46x38.png26key3Da19fcc184b9711e1b4764040d3dc5c07] 

First, we will discuss why you may want to write more legible code as opposed to short, concise code. Afterwards, we will look at the following strategies on how to do that with:

* Variable, value, reference, class, object, and function naming
    
* Helper functions
    
* Code comments
    
* Enums/dictionaries/sealed classes/etc.
    
* Package organization and naming
    

Basic code literacy is recommended to get the most out of this article. However, I have tried to make it accessible to beginners where possible.

![Image](https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDE1Mnx8cmVhZGluZ3xlbnwwfHx8fDE2Njg4MTYyMjQ&ixlib=rb-4.0.3&q=80&w=2000 align="left")

*Photo by \[Unsplash\](https://unsplash.com/@jamie452?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit"&gt;Jamie Street / &lt;a href="https://unsplash.com/?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit)*

## Does Efficiency Come From Fewer Keystrokes?

I recall as a junior developer, thinking that short or abbreviated names for identifiers – basically any code construct us developers are allowed to name – were more efficient.

My logic was simple: If it takes me less time to write it, then I can get the job done faster.

This logic would make sense if the following things were true:

* I, or someone else, would never have to read or fix what I wrote in the past
    
* I did not often forget what a variable, or several variables were, as I was reading through a function
    
* I did not occasionally have to write some code which was truly complex and obscure
    
* I could rename ridiculous or obscure external library functions, classes, or properties to something more sensible
    

The point is that, for me, **I find few situations where being concise actually saves time**. Further, modern IDEs have this useful feature called code completion which saves most of the keystrokes anyways.

You may not feel the same way, and that is perfectly okay! Take whatever works for you in this article and throw away the rest.

## How To Name Classes, Variables, and Functions

I will now share what I do to make my code easier for myself and others to read. The code examples I use will be in Kotlin, but the points I make should be applicable to most platforms and languages.

There are two important things to know when learning about how to name software entities. Before getting to that, this term software entities refers to any of the following:

* Classes, structs, objects
    
* Variables, values, references, pointers
    
* Functions, methods, algorithms, commands
    
* Interfaces, protocols, abstractions
    

Essentially, anything which a programmer has to name when writing a program.

### How Descriptive Names Should Be

My goal for naming software entities is this: The name should **reduce any confusion about what a software entity does, or is.**

The details of how it does something are not usually necessary.

The context, or everything around, of a software entity is important when deciding on a name. Something may require more or less details depending on its context.

Let us consider three examples:

1. `getFormattedDate(date: String) : String`
    
2. `getYYYYMMDDFormattedDate(date: String) : String`
    
3. `getYYYYMMDDFormattedDateFromIso8601Format(date: String) : String`
    

The production application I am currently working on frequently requires transforming dates to and from different formats.

In that context, I absolutely use names like example 3, which is much clearer than example 1.

Another option might be to change the parameter name in example 2 to something like `iso8601Date`.

While I do suggest you be consistent in your approach in a given codebase, feel free to experiment with what works for you. The point is to add as much information as is necessary to clear up any ambiguity.

If I was writing a one-off program that only ever converts one format to another, then example 1 is fine. **Adding more information than necessary is not what I am advocating here.**

### The More Something Does, the Harder It Is to Name

If you find yourself having trouble naming something, it is most often (though not always) because it does too many things that are not conceptually related.

The degree to which software entities are conceptually related is known as [cohesion](https://en.wikipedia.org/wiki/Cohesion_\(computer_science\)).

**By looking at what parts of a program are cohesive or not**,\*\* you can begin to understand what should be separated or grouped together.\*\*

This process can be done from various perspectives, which I will try to explain by example.

Suppose you have four software entities:

1. `StoreUserInCloud`
    
2. `StoreUserOnDisk`
    
3. `StoreMessage`
    
4. `EditUserUI`
    

The first perspective we can consider is the real-world information which these entities are concerned with. From that perspective, we can see that `StoreUserInCloud`,`StoreUserOnDisk`, and `EditUserUI`use the same model of information: A User.

However, there is another perspective that we must keep in mind, particularly when designing graphical user interface (GUI) programs.

Every GUI program can be broken down into three principal layers:

* User Interface (commonly called “View”)
    
* Logic (commonly refers to things like Controllers and Presenters)
    
* Model (data storage and access, or the state itself depending on your definition)
    

This does not mean that you should only ever look at a program as having these three layers! The three layer approach is a generalization which is **frequently insufficient**.

In any case, from that perspective, `StoreMessage` has more in common with the other storage entities than does `EditUserUI`.

Being able to look at your programs from multiple perspectives is something that will come as you build more complex programs.

The key takeaway is that separating your codebase into cohesive, related parts will generally make software entities easier to name.

## How to Use Helper Functions

Helper functions, particularly when combined with good function naming practices, can greatly improve the readability of your code.

Helper functions are also an opportunity to apply a core principle of software architecture: Separation of concerns.

### How to Create Sudoku Puzzles with Helper Functions

We will now look at a practical example to demonstrate extensive usage of helper functions. Please try to imagine how much harder this code would be to follow if everything was just in a single, giant function!

In the past, I worked on a large but cohesive part of a program: A [Sudoku](https://en.wikipedia.org/wiki/Sudoku) builder which uses graph data structures and algorithms. Even if you are not familiar with Sudoku or graph DSA, I believe you will still be able to follow the main point.

You can find the full [source code here](https://github.com/BracketCove/GraphSudokuOpen/tree/master/app/src/main/java/com/bracketcove/graphsudoku/computationlogic).

We can break the process of generating a playable Sudoku puzzle into five steps:

* Creating the nodes of the puzzle (representing the tiles)
    
* Creating the edges of the puzzle (edges in this case is another word for relationships/references between the tiles: Either row, column, or subgrid)
    
* Seeding (adding) some values to the data structure to make solving it faster
    
* Solving the puzzle
    
* Unsolving a certain number of tiles so that the game is actually playable by a user
    

I used something similar to the builder pattern to represent these steps in the function I call to create the puzzle:

```kotlin
internal fun buildNewSudoku(
    boundary: Int,
    difficulty: Difficulty
): SudokuPuzzle = buildNodes(boundary, difficulty)
        .buildEdges()
        .seedColors()
        .solve()
        .unsolve()
```

Although the idea of “nodes” and “edges” are technical definitions within [graph theory](https://en.wikipedia.org/wiki/Graph_theory), this code clearly reflects the five steps I had decided on.

We will not look at the entire codebase, but I want to highlight how the helper functions continue to break down the logic and promote readability:

```kotlin
internal fun SudokuPuzzle.buildEdges(): SudokuPuzzle {
    this.graph.forEach {
        val x = it.value.first.x
        val y = it.value.first.y

        it.value.mergeWithoutRepeats(
                getNodesByColumn(this.graph, x)
        )

        it.value.mergeWithoutRepeats(
                getNodesByRow(this.graph, y)
        )

        it.value.mergeWithoutRepeats(
                getNodesBySubgrid(this.graph, x, y, boundary)
        )

    }
    return this
}

internal fun LinkedList<SudokuNode>.mergeWithoutRepeats(new: List<SudokuNode>) {
    val hashes: MutableList<Int> = this.map { it.hashCode() }.toMutableList()
    new.forEach {
        if (!hashes.contains(it.hashCode())) {
            this.add(it)
            hashes.add(it.hashCode())
        }
    }
}

internal fun getNodesByColumn(graph: LinkedHashMap<Int,
        LinkedList<SudokuNode>>, x: Int): List<SudokuNode> {
    val edgeList = mutableListOf<SudokuNode>()
    graph.values.filter {
        it.first.x == x
    }.forEach {
        edgeList.add(it.first)
    }
    return edgeList
}
//...
```

To summarize this process, the helper functions provide two benefits:

* They are a stand in for a blob of code which does something
    
* That blob of code can be given a descriptive name
    

Both of those benefits can lead to greater legibility as the code becomes less cluttered and more descriptive.

If you are wondering what should and should not be a helper function, I suggest you practice different approaches to see what works for you.

## How to Use Code Comments

My personal preference on code comments is that they have two primary usages: First, comments help describe complex functions in detail.

Second, to clear up any confusion about a line or block of code.

### How To Use Comments to Design New Functions

When I come across functions which I expect to be difficult to write, I will describe what the function does using either plain language or pseudocode.

How I do this has changed over the years, so I encourage you to try different approaches.

In the examples from the previous section, I had omitted the code comments:

```kotlin
/**
 * 1. Generate a Map which contains n*n nodes.
 * 2. for each adjacent node (as per rules of Sudoku), add an Edge to the hashset
 *  - By column
 *  - By row
 *  - By n sized subgrid
 *
 *  LinkedHashMap: I chose to use a LinkedHashMap because it preserves the ordering of
 *  the elements placed within the Map, but also allows lookups by hash code, which are
 *  generated by x and y values.
 *
 *  As for the LinkedList in each bucket (element) of the map, assume that the first element
 *  is the node at hashCode(x, y), and subsequent elements are edges of that element.
 *  Apart from the ordering the first element as the Head of the LinkedList, the rest of
 *  the elements need not be ordering in any particular fashion.
 *
 *
 *  */
internal fun buildNodes(n: Int, difficulty: Difficulty): SudokuPuzzle {
    val newMap = LinkedHashMap<Int, LinkedList<SudokuNode>>()

    (1..n).forEach { xIndex ->
        (1..n).forEach { yIndex ->
            val newNode = SudokuNode(
                    xIndex,
                    yIndex,
                    0
            )

            val newList = LinkedList<SudokuNode>()
            newList.add(newNode)
            newMap.put(
                    newNode.hashCode(),
                    newList
            )
        }
    }
    return SudokuPuzzle(n, difficulty, newMap)
}
```

The amount of detail I add to these comments depends on the context. If I am working in a team, I will usually try to keep this much shorter than what you see above, and only include information that I feel is necessary.

The example above was a personal learning project that I expected to share with others. This is why I even included my decision making process on the types used to represent a Sudoku puzzle.

For fans of test driven development, you might try writing out the pseudocode steps of an algorithm before writing the test:

```kotlin
/**
     * On bind process, called by view in onCreate. Check current user state, write that result to
     * vModel, show loading graphic, perform some initialization
     *
     * a. User is Anonymous
     * b. User is Registered
     *
     * a:
     * 1. Display Loading View
     * 2. Check for a logged in user from auth: null
     * 3. write null to vModel user state
     * 4. call On start process
     */
    @Test
    fun `On bind User anonymous`() = runBlocking {

        //...
    }
```

This allows you to design the unit at a **higher level of abstraction** before writing the implementation. The time you spend designing at higher levels of abstraction can save you time in the long run.

### How to Use Inline Code Comments Effectively

There are two primary situations where I will write an inline code comment:

* When I feel that the purpose of a line or block of code will not be clear to myself or anyone else reading it later
    
* When I have to call some poorly named library function which has a confusing or misleading name
    

By far, the most complex Sudoku algorithm in my program is the [solver algorithm](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/computationlogic/SolveSudoku.kt). In fact, it's so long that I will only post a snippet of it here:

```kotlin
internal fun SudokuPuzzle.solve()
        : SudokuPuzzle {
    //nodes that have been assigned (not including nodes seeded from seedColors()
    val assignments = LinkedList<SudokuNode>()

    //keep track of failed assignment attempts to watch for infinite loops
    var assignmentAttempts = 0
    //Two stages of backtracking, partial is half the dataset, full is a complete restart
    var partialBacktrack = false

    var fullbacktrackCounter = 0

    //from 0 - boundary, represents how "picky" the algorithm is about assigning new values
    var niceValue: Int = (boundary / 2)

    //to avoid being too nice too soon
    var niceCounter = 0

    //work with a copy
    var newGraph = LinkedHashMap(this.graph)
    //all nodes which are of 0 value (uncolored)
    val uncoloredNodes = LinkedList<SudokuNode>()
    newGraph.values.filter { it.first.color == 0 }.forEach { uncoloredNodes.add(it.first) }

    while (uncoloredNodes.size > 0) {
    //...
    }
//...
}
```

In this case, inline comments were necessary as I would frequently forget what some of these variables were while reading through this giant algorithm.

Another case where I will add an inline comment is when I have to explain or remind myself about code which I do not have control over.

For example, the infamous [Java Calendar API](https://docs.oracle.com/javase/7/docs/api/java/util/Calendar.html#MONTH) uses zero-based indexing for months. This is arguably really stupid, as I am not aware of any standard that represents January with 0, nor do I care if one exists!

I cannot share the code with you as it is proprietary, but suffice it to say that I have comments in my current team’s codebase that explains random `- 1` statements to conform to the Calendar API.

## How To Use Enums and Dictionaries

There are other names for these kinds of code constructs, but these are the two I am familiar with. Suppose you have a restricted, or limited, set of values which you use to represent something.

For example, I needed a way to limit the number of tiles that are included in a new Sudoku puzzle, based on:

* The size of the puzzle (4, 9, or 16 tiles per column/row/subgrid)
    
* The difficulty of the puzzle (easy, medium, or hard)
    

Through extensive testing, I arrived at the following values as modifiers:

```kotlin
enum class Difficulty(val modifier:Double) {
    EASY(0.50),
    MEDIUM(0.44),
    HARD(0.38)
}

data class SudokuPuzzle(
        val boundary: Int,
        val difficulty: Difficulty,
        val graph: LinkedHashMap<Int, LinkedList<SudokuNode>>
        = buildNewSudoku(boundary, difficulty).graph,
        var elapsedTime: Long = 0L
)//...
```

These values are used in various places where the logic must change based on the difficulty.

Sometimes, you do not even need to have values associated with human-readable names. I used a different enum to represent different solving strategies to ensure a puzzle is playable relative to the selected difficulty:

```kotlin
enum class SolvingStrategy {
    BASIC,
    ADVANCED,
    UNSOLVABLE
}

internal fun determineDifficulty(
    puzzle: SudokuPuzzle
): SolvingStrategy {
    val basicSolve = isBasic(
        puzzle
    )
    val advancedSolve = isAdvanced(
        puzzle
    )

    //if puzzle is no longer solvable, we return the current strategy
    if (basicSolve) return SolvingStrategy.BASIC
    else if (advancedSolve) return SolvingStrategy.ADVANCED
    else {
        puzzle.print()
        return SolvingStrategy.UNSOLVABLE
    }
}
```

A good principle in designing any system is this: **Fewer moving parts generally have fewer things that can go wrong**.

Placing restrictions on values and types, and giving them good names, not only makes your code easier to read, **it can protect it from errors as well**.

## How to Organize and Name Packages, Folders, and Directories

No guide on code legibility would be complete without some discussion on packages. If the platform and language of your preference does not use this term, assume I mean folder or directory instead.

This is something which I have changed my opinions on several times, and that is reflected in my older projects.

Two common approaches to package organization are:

* Package by architectural layer
    
* Package by feature
    

### How to Do Package By Layer

Package by layer is the first and worst system I have ever used. The idea is usually to build your package structure around some architectural pattern like MVC, MVP, MVVM, and so on.

To take MVC as an example, your top level package structure would look like this:

* model
    
* view
    
* controller
    

The first problem with this approach is that it assumes that every class or function fits comfortably in one of these layers. This is rarely the case in practice.

I also find this approach to be the least legible, as the top level tells you only the most general details about what to expect inside each package.

This approach can usually be improved upon by adding more “layers” to be more specific:

* ui
    
* model
    
* api
    
* buildlogic/di
    
* repository
    
* domain
    
* common
    

This can work reasonably well in smaller codebases where all developers are familiar with the general pattern and style used.

### How To Do Package By Feature

Package by feature has its own flaws, but is generally easier to read and navigate. This is assuming that you give the packages good names.

The term feature is tough to describe, but I would generally define it as this: A screen/page, or set of screens/pages that define a **primary piece of functionality** for users or customers.

For a social media app, we might see a structure such as:

* timeline
    
* friends
    
* userprofile
    
* messages
    
* messagedetail
    

The core problem with package by feature is the opposite of package by layer: There will almost always be software entities which are used in multiple features.

There are two solutions to this problem. The first would be to have duplicate code in each feature.

Believe it or not, duplicating software entities **can be incredibly useful in enterprise settings** in specific situations.

However, it is not something I would recommend as a general rule.

### How to Do a Hybrid Package Structure

The solution I generally recommend to developers is what I like to call the hybrid approach. It is very simple, flexible, and should cover most of your requirements:

* timeline
    
* friends
    
* messages
    

* allmessages
    
* conversation
    
* messagedetail
    

* api
    

* timeline
    
* user
    
* message
    

* uicomponents
    

Please do not take this example too seriously; I am trying to convey the general idea: Anything which is feature specific goes into that feature package. Anything which is shared across features goes into a separate package nested at the same level or a higher level.

Again, what defines a layer was a vague concept to begin with, so do not just follow a convention blindly. **Think critically about what is clear, particularly to someone who is not familiar with the project**.

## Closing Thoughts

Most of my preferences on code legibility and style have come from a great deal of trying different approaches. Sometimes these were approaches I saw others use and some of them came about naturally.

If you are able to put yourself in the position of someone less familiar with the code or program you are looking at, you will have an easier time making your code read like a book.

### Before you go...

If you liked this article and want more information on these principles and code constructs, check out my free, full length [programming fundamentals course](https://youtu.be/FL2SMZxNQlc). It includes professionally written English, Burmese, and Arabic subtitles.
