---
title: How to control your randomizer in R
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T20:10:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-control-your-randomizer-in-r-852ae7d8f80c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aI6mpoboOmJMKqvEU593xA.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: r language
  slug: r-language
- name: sampling
  slug: sampling
- name: statistics
  slug: statistics
seo_title: null
seo_desc: 'By Michelle Jones

  What happens when you need a particular type of randomization?


  200 random numbers using the normal distribution.

  Overview of random number generation in R

  R has at least 20 random number generator functions. Each uses a specific pr...'
---

By Michelle Jones

What happens when you need a particular type of randomization?

![Image](https://cdn-media-1.freecodecamp.org/images/KcZO-yHw1nNM1n8Mnq6gGWolKXhE1UNd3d2z)
_200 random numbers using the normal distribution._

### Overview of random number generation in R

[R](https://cran.r-project.org) has at least 20 random number generator functions. Each uses a specific probability distribution to create the numbers. All require you to specify the number of random numbers you want (the above image shows 200). All are available in base R — no packages required.

Common random number generator distributions are:

* [normal](http://www.statisticshowto.com/probability-and-statistics/normal-distributions/) (rnorm): default mean of 0 and standard deviation of 1
* [binomial](http://www.statisticshowto.com/probability-and-statistics/binomial-theorem/binomial-distribution-formula/) (rbinom): no defaults, specify the number of trials and the probability of success on each trial
* [uniform](https://www.investopedia.com/terms/u/uniform-distribution.asp) (runif): default minimum value of 0 and maximum value of 1

Of the three above, only the binomial random number generator creates integers.

### Why create random numbers?

Problems involving random numbers are very common — there are around [50,000 questions relating to random numbers](https://stackoverflow.com/search?q=random+numbers) on Stack Exchange.

But why use them?

Random numbers have many practical applications. They are used in [Monte Carlo simulations](http://reference.wolfram.com/language/howto/PerformAMonteCarloSimulation.html). They are used in [cryptography](https://crypto.stackexchange.com/questions/726/what-is-the-use-of-real-random-number-generators-in-cryptography). They have been used to produce [CAPTCHA content](https://support.google.com/a/answer/1217728?hl=en). They are used in [slot machines](http://www.casinonewsdaily.com/slots-guide/random-number-generator-hit-frequency-vs-payout-ratio/). They have also been used for more mundane tasks such as creating a random sort order for an array of ordered data.

### Problems with random numbers

Common questions include “are my random numbers actually random?” and “how can I generate non-repeated random numbers?”

**Note**: the latter decreases randomness, because the population of possible random numbers is decreased by one each time a random number is drawn. The method is appropriate in situations such as lotteries or bingo, where each ticket or ball can only be drawn once.

This problem brings in another problem! The randomly generated, sampling without replacement numbers must be integers. No one has ticket 5.6932 or bingo ball 0.18967.

### A practical example of random number problems

Let’s take the example that I have 20 female students of the same age. I have four teaching methods that I want to trial. I only want to trial one teaching method for each student. Easy math— I need five students in each group.

But how do I do this so that each student is randomly assigned?

And how do I make sure that I only have integers produced?

And how do I do all this while using randomly generated numbers without replacement? I don’t want, for example, six students in one group, and four students in another.

First, I need to create some dummy data, in R. Let’s create that list of mock female students.

```
FemaleStudents <- data.frame(Names=c("Alice", "Betty", "Carol", "Denise", "Erica", "Frances", "Gina", "Helen", "Iris", "Julie", "Katherine",                           "Lisa", "Michelle", "Ngaire", "Olivia", "Penelope", "Rachel", "Sarah", "Trudy", "Uma"))
```

Now we have a one-dimensional dataset of our 20 students.

We know that the `runif()` function doesn’t create integers. Why don’t we round the random numbers so that we only get integers and use this function? We can wrap the random number in a rounding function.

**Question 1:** why am I using the random uniform distribution and not another one, such as the random normal distribution?

There are five types of rounding functions in R. We will use `round()`.

So that we get the same results, I will set a seed for the random number generation. Each time we generate random numbers, we will use the same seed. I’ve decided on 5 as the seed. If you do not set a seed, or if you set a seed other than 5, your results will be different than mine.

```
set.seed(5)FemaleStudents$Group <- round(runif(20, 1, 5))
```

Well, that seemed to work. We have each student allocated to a group numbered between 1 and 5.

Let’s double check our allocation.

```
table(FemaleStudents$Group)
```

```
1 2 3 4 5 2 6 5 4 3
```

Darn. Only one of the five groups has the correct number of students (Group 4). Why did this happen?

We can check the numbers actually output by `runif()` without rounding, and letting the output print to the console. Here, the output prints because I have not assigned the function to an object (for example, to a data.frame variable).

```
set.seed(5)runif(20,1,5)
```

```
[1] 1.800858 3.740874 4.667503 2.137598 1.418601 3.804230 3.111840 4.231741 4.826001 1.441812 2.093140 2.962053 2.273616 3.236691 2.050373[16] 1.807501 2.550103 4.551479 3.219690 4.368718
```

As we can see, the rounding caused our problem. But if we hadn’t rounded, each student would have been assigned to a different group.

What do we do?

### sample()

`sample()` is now one of my favourite functions in R. Let’s see how it works.

#### Randomly allocate to equally sized groups (counts matter)

How can we use it to randomly assign our 20 students to four equally sized groups?

What happens if we try `sample()` normally?

```
set.seed(5)FemaleStudents$Sample <- sample(1:5, nrow(FemaleStudents), replace=TRUE)
```

**Question 2:** what output did you get when you used `table(FemaleStudents$Sample)`?

We can fix this problem by creating a vector of group numbers, and then using sampling without replacement from this vector. The `rep` command is used to create a range of repeated values. You can use it to repeat each number in the series, as I have used here. Number 1 is repeated four times, then number 2 is repeated four times, and so forth. You can also use it to repeat a sequence of numbers, if you use this code instead: `rep(1:5,4)`

```
OurGroups <- rep(1:5, each=4)set.seed(5)FemaleStudents$Sample <- sample(OurGroups, nrow(FemaleStudents), replace=FALSE)
```

We used our vector of numbers (`OurGroups`) to allocate our students to groups. We used sampling without replacement (`replace=FALSE`) from `OurGroups` because we need to use each value in that vector. We need to remove each value as we use it.

And we get the result we wanted!

```
table(FemaleStudents$Sample)
```

```
1 2 3 4 5 4 4 4 4 4
```

**Question 3**: why did I still set a seed?

Another advantage of `sample()` is that it doesn’t care about type. We can repeat the allocation using a vector of strings. This can be useful if you don’t want to keep referring back to what “1” means.

```
OurNamedGroups <- rep(c("Up", "Down", "Charmed", "Strange", "Top"), each=4)set.seed(5)FemaleStudents$Sample2 <- sample(OurNamedGroups, nrow(FemaleStudents), replace=FALSE)table(FemaleStudents$Sample2)
```

```
Charmed    Down Strange     Top      Up       4       4       4       4       4
```

Because we used the same seed, we can see that the same student allocation was performed, irrespective of whether we used numeric or character data for the assignment.

```
table(FemaleStudents$Sample,FemaleStudents$Sample2)       Charmed Down Strange Top Up  1       0    0       0   0  4  2       0    4       0   0  0  3       4    0       0   0  0  4       0    0       4   0  0  5       0    0       0   4  0
```

#### Randomly allocate when group size is not restricted

Sometimes we want to randomly allocate to groups, but we don’t have a vector of groups. We are still only allocating each unit (person, sheep, block of cheese) to a single group, and we use completely random allocation.

Let’s say that our school has a new, special library room. It’s been constructed to be soundproof to give students a better studying environment. The chief librarian would like to know about the experiences of students in that room. The only problem is that the room is limited in size. The chief librarian thinks that around four students is a large enough group to provide the initial feedback.

Again, we can use `sample()` to pick our student groups. In this case, we have “students who will test the room” and “students who won’t test the room”. I’m going to call them “Test” and “Not test”. These labels have been chosen for being 1. short and 2. easily distinguished.

Because we did sampling without replacement earlier, we didn’t specify probabilities of assignment to groups — we simply pulled out an assignment from a vector. Now we are going to use sampling with replacement. With replacement refers to the group, not to the students.

We need to sample with replacement as we only have two groups (“Test”, “Not test”) and 20 students. If we tried to sample without replacement, our code would error.

Our code is very similar:

```
set.seed(5)FemaleStudents$Library <- sample(c("Test", "Not test"), nrow(FemaleStudents), replace=TRUE, prob=c(4/20,16/20))table(FemaleStudents$Library)
```

```
Not test     Test       15        5
```

As you can see, we allocated five students to test the room, not four. This type of result is expected when dealing with small samples. However, our allocation of students is completely random. Each student had exactly the same probability of being assigned to test the room. Whether previous students were testers or not had no impact on the allocation of the next student.

Let’s walk through some of that code.

I’ve constructed a new variable in the `data.frame` to collect the allocation (`Library`).

Instead of dealing with numbers for group names, I’ve used the strings I mentioned earlier. Because I’ve used strings, the `c()` must wrap the group names (`“Test”, “Not test”`) and each group name is separated by a comma.

Replacement has been set to `TRUE`.

The probability of assignment to either group must be provided. This is the `prob=c(4/20,16/20)` part of the `sample()` function. Again, note how `c()` is used to contain the probabilities. Also of interest is that the probabilities can be expressed as fractions, rather than decimals.

### Hooray for sample()

I use `sample()` all the time for the work I am doing. The ability to use strings, as well as to restrict numeric output to integers (and define the desired integer range), provides me with more control than trying to use one of the random number functions.

### Answers

**Answer 1**: I used a random uniform distribution because I wanted each value to be equally probable.

**Answer 2**: I got this output:

```
1 2 3 4 5 2 7 4 2 5
```

**Answer 3:** If we don’t set a seed value, or we use a different one, the allocation of specific students will be different. For example, when the seed is 5, Alice is allocated to group 2. If the seed is 7, Alice is allocated to group 5. Replication is important when code needs to be re-run (for example, in testing).

