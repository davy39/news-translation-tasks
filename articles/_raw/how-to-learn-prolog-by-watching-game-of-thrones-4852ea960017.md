---
title: How to learn Prolog by watching Game of Thrones
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T15:41:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-prolog-by-watching-game-of-thrones-4852ea960017
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fVNJJSasfcKnyv1JSM2B_g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: coding
  slug: coding
- name: game of thrones
  slug: game-of-thrones
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Rachel Wiles

  Are they dead? Are they alive? Is she his aunt? Instead of casting your mind back
  to 2011, save the exhaustion and build your own expert using Prolog.


  Image via HBO

  Obligatory Game of Thrones SPOILER WARNING! Events included are up t...'
---

By Rachel Wiles

#### Are they dead? Are they alive? Is she his aunt? Instead of casting your mind back to 2011, save the exhaustion and build your own expert using Prolog.

![Image](https://cdn-media-1.freecodecamp.org/images/0mPIMd4VO0fFg9AA3aOkINfRK4VhuinAGXSZ)
_Image via HBO_

#### Obligatory Game of Thrones **SPOILER WARNING!** Events included are up to Season 7, disregarding anything that occurs only in the books. If you aren’t up to speed, proceed with caution. But, the Prolog remains the same since 1972, with no plot twists and an easy to follow structure that this tutorial will help you ace.

### Establish the facts

Prolog is a logic programming language, which forms rules and relationships from facts. To use Prolog, queries are passed through a structured database of facts. Game of Thrones is renowned for its complex (and often incestuous) family trees, so breaking things down into simple facts starts a great basis for a Prolog database.

![Image](https://cdn-media-1.freecodecamp.org/images/7Z4tEvxRINNe9qpbuQJF07WjtPlnAYgFEyoC)
_Ain’t nobody got time for that. Image via usefulcharts_

Simplify things by starting the database with one set of facts, which can be applied to all characters. For family trees, a good place to start is linking characters through their parents. Take the case of Arya Stark:

```
parent(eddard_stark, arya_stark).parent(catelyn_stark, arya_stark).
```

Here, two separate facts have been defined, saying that Eddard and Catelyn are the parents of Arya. You can then extrapolate these queries across the entire Game of Thrones universe, for all the houses, to create a complete database (or, poach the whole dataset from my [GitHub](https://github.com/rachelwiles/GoT-Check)). These facts alone are enough to start making queries. The most basic query checks whether a fact is present within the database.

```
?-parent(eddard_stark, arya_stark).true
```

If you input relationships that aren’t within the database, it returns **false**. You can also query with variables in Prolog by using uppercase. To find who the parents of Arya are, ask:

```
?-parent(Parent, arya_stark).Parent = eddard_stark ;Parent = catelyn_stark.
```

Eddard returns first in this example, for this is the first **true** fact listed in the database. Hit semicolon conducts searches for further true answers (catelyn_stark), until there are none remaining. A period terminates the search all together. Use underscores as anonymous variables to filter out information that doesn’t matter. For instance, if you wanted to see that Arya has parents, but don’t care who they are, query the following:

```
?-parent(_, arya_stark).true
```

![Image](https://cdn-media-1.freecodecamp.org/images/3tkjbtN5ezXYqcSN2xqBVuQy6MQ7p5ZnAUXt)
_Season 1 Episode 1: The last time anyone smiled in GoT. Image via Fanpop_

### Create rules

Now that there are facts in the database, begin creating rules. Rules are dependent on facts. Tying facts together creates rules. From our last example, make a simple rule from the parent fact, to determine a child relationship; X is the child of Y **if** (written as **:-** in Prolog) Y is the parent of X.

```
child(X, Y) :-    parent(Y, X).
```

This essentially reverses the parent rule, and allows searches up and down the family tree. In another instance, suppose you want to make a rule determined by the _absence_ of a fact…

```
status(X, dead) :-    not(status(X, alive)).
```

Here, I’ve expanded the database to include a set of rules for every character that is still alive. The query searches the database for all instances where person X is alive. The **not** indicates that, if X is not found to be alive, then X is dead. This rule is efficient for Game of Thrones, as it only requires a handful of facts, for the few who are still alive.

![Image](https://cdn-media-1.freecodecamp.org/images/FFOu992hmDDjc7itq9Bd8o1DGBuJ7wgMRJhM)
_dies(X) :- played_by(X, sean_bean). Image via [nova969](http://www.nova969.com.au" rel="noopener" target="_blank" title=")_

More interesting and specific rules are created by combining facts. For example, to create a mother/father relationship, more facts on every character’s gender in Game of Thrones is needed. Once done, a rule to identify mothers is created by the following:

```
mother(X, Y) :-    parent(X, Y),    female(X).
```

In the above, we’ve stated that a mother (X) is a parent of someone **and** (written as a comma in Prolog) is female.

So far, we’ve covered traveling up and down the family tree, but haven’t touched left to right. By creating a sibling rule, queries can be made every which way across the Game of Thrones family tree:

```
sibling(X, Y) :-    parent(Z, X),    parent(Z, Y),    dif(X, Y).
```

In layman’s terms, this states that two people (X and Y) are siblings if they both share the same parent (Z). The **dif** function here is important to stop the program from returning _themselves_ as their own sibling. HOWEVER, there are limitations to this approach. Querying this will evaluate both parents of X _and_ both parents of Y (often, but not always, the same people), consequently the full search will return duplicates. This can be fixed by introducing lists.

![Image](https://cdn-media-1.freecodecamp.org/images/KLLHVm1FdhMM-WM7LHEuOrswL37-0V1WUNF7)
_A whole different breed of sibling problems. Image via wordpress_

### Making lists

Revisiting the sibling problem, adding lists will achieve better implementation, and have many applications in Prolog. The code used previously can still be used, however the results need to be collected into a list using the following:

```
list_siblings(X, Siblings) :-    setof(Y, sibling(X, Y), Siblings);    Siblings = none. 
```

**setof** pulls together all possible outcomes for the `sibling(X, Y)`query, and stores them in a list called Siblings. In the case where there are no siblings, the **or** component (represented by a semicolon in Prolog) returns none. **setof** also removes any duplicates, keeping only unique values, hence improves the prior query. Now that a list of siblings can be generated for any character, a separate query can determine whether 2 characters are siblings:

```
siblings(X, Y) :-    list_siblings(X, Siblings),    member(Y, Siblings).
```

When queried, this builds the list Siblings for X and uses **member** to determine whether Y is within the list Siblings.

Now that there’s sibling relationships, parent relationships and gender within the database, you don’t need to visit the Grand Library in the Citadel to work out who Jon Snow’s aunt is.

![Image](https://cdn-media-1.freecodecamp.org/images/3dI6nBbgaPmvcpXKa7fozwtE9bGKF3poObzv)
_Should’ve just used Prolog. Image via usatoday_

### Recursion

The family trees in Game of Thrones span much further than just immediate family. It is possible to venture further out, and generate links between more distant relationships. Using the parent predicate, Prolog can recursively evaluate the database to find ancestry. Setup recursion through including the following 3 sections in a database:

1. Terminating section — This section must occur before the looping section, to stop the program from looping infinitely:

```
ancestor(X, Y) :-    parent(X, Y).
```

2. Looping section — This section calls upon itself repeatedly, until the terminating condition above is met:

```
ancestor(X, Y) :-    parent(X, Z),    ancestor(Z, Y).
```

3. Calling section — query ?-ancestors(X, Ancestor_of) to begin storing a list of ancestors through each recursion as defined above:

```
ancestors(X, Ancestor_of) :-    findall(A, ancestor(X, A), Ancestors_of).
```

The **findall** function here works similarly to **setof**, however does not exclude duplicates, and returns a list of who X is the ancestor of.

### Printing and formatting

If you’re looking for a one stop shop where you can get all information on one character, you’ll need formatting to organise it. To return a bunch of information in one go, call on previously defined rules within a rule:

```
tell_me_about(X) :-    alive_or_dead(X),    parents(X, Parents),    format("Parents: ~w", [Parents]), nl,     children(X, Children),    format("Children: ~w", [Children]), nl,    list_siblings(X, Siblings),    format("Siblings: ~w", [Siblings]), nl,    !.
```

**format** returns whatever output from the square parenthesis in place of the ~w, and prints everything enclosed in quotations. **nl** represents a new line. The cut function (**!**) in Prolog prevents backtracking, so forces the program to stop finding additional solutions after the first has been found. In the above, this ensures that everything prints once. Querying this with Stannis Baratheon gives the following:

![Image](https://cdn-media-1.freecodecamp.org/images/2XYV4yOyu5NiJAx-bdRpne-66sOfDOrMCnvO)

The function **print** can also be used in place of format, when there are no variables to be outputted.

![Image](https://cdn-media-1.freecodecamp.org/images/VlEjB6izTlNvedDdXOz2bcbvCcApzIXpOeqo)
_The code is long and full of errors. Image via HBO_

### Using arithmetic

Arithmetic operations can be used in Prolog to interpret and analyse data. Suppose Arya now wants to be super organised, and use Prolog instead of committing her list to memory. She could use the following to keep track:

```
aryas_list :-    print("ARYAS TOP SECRET LIST. KEEP OUT."), nl,    findall(X, on_list(X), MainList),    ticked_off(List),    format("Done: ~w", [List]), nl,    not_dead_yet(AnotherList),    format("Still to go: ~w", [AnotherList]), nl,    length(AnotherList, LCompletedList),         length(MainList, LMainList),    Percent is ((LMainList - LCompletedList) / LMainList) * 100,    Percentage is round(Percent),             format("Percentage complete: ~w%", [Percentage]), nl.
```

In aryas_list, I have used the following operators:

* * Multiply
* - Subtract
* / Divide
* length(). Generate list length
* round(). Round to nearest integer

The result looks as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/yqf4CUXcnSht0c9z8W-3hagkkwoccwCO2yut)

![Image](https://cdn-media-1.freecodecamp.org/images/4S0ZSFXJQYC51AGKvHdKdUceVF7P0EA-EZjj)
_is_arya :- girl(X), no_name(X). Image via inverse_

With all the tools covered, there’s plenty more interesting ways to explore the Game of Thrones universe in Prolog. Or, scrap watching the show entirely, after working out who should sit on the Iron Throne through inarguable logic programming.

```
rightful_heir(X) :-    parent(robert_baratheon, X),    status(X, alive).
```

The results speak for themselves…

![Image](https://cdn-media-1.freecodecamp.org/images/CNwejVS4LLM8yTdS4EwTjc9QGlUUPgMPEUQQ)
_My inbox is open for debate._

If you want to expand the existing database, or play around creating your own relationships, the code is on my [GitHub](https://github.com/rachelwiles/GoT-Check).

Follow my [LinkedIn](https://www.linkedin.com/in/rachelwiles/) for future projects.

