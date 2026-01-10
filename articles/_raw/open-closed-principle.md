---
title: Open-Closed Principle – The Software Development Concept Explained in Plain
  English
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2021-09-27T19:43:06.000Z'
originalURL: https://freecodecamp.org/news/open-closed-principle
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/IMG_8905.JPG
tags:
- name: software design
  slug: software-design
- name: software design patterns
  slug: software-design-patterns
- name: software development
  slug: software-development
seo_title: null
seo_desc: "There are many articles about the Open-Closed Principle, but I can never\
  \ find one that explains it in a way that really works for me. \nSo here, hopefully,\
  \ is a good one – with a non trivial and real life example, what changes to support,\
  \ and a descri..."
---

There are many articles about the Open-Closed Principle, but I can never find one that explains it in a way that really works for me. 

So here, hopefully, is a good one – with a non trivial and real life example, what changes to support, and a description of the trade offs.

The Open-Closed principle states that code should be "Open for extension" and "Closed for modification". 

There is [quite a lot of confusion about the term](https://codeblog.jonskeet.uk/2013/03/15/the-open-closed-principle-in-review/), but essentially it means that if you want to implement a _supported_ change, you should be able to do it without changing the code in a large number of places. Ideally, you can implement the new feature just by adding new code, and changing little or no old code, which makes the code easier to develop and maintain. 

Open is the 'O' in the [SOLID design principles](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/), which are probably the most famous guides for writing high quality code.

No useful code can ever be completely open to all possible changes, so we have to decide which changes we are going to _support_. When writing our code we can think about what the potential changes might be, decide which ones to _support_, and then make the code 'open' to these. 

We can create a list of these potential changes by:

* Analysing the code
* Looking at previous changes to the code
* Using our experience of commonly requested changes
* Using any knowledge of upcoming feature requests

Take a minute to look at the code below ([and on GitHub](https://github.com/ceddlyburge/open-closed-principle/blob/master/OpenClosedPrinciple/Original/GrossToNetCalculator.cs)) and think about what changes we might expect. You don't have access to the commit history, or any knowledge of upcoming feature requests, but you can still probably come up with some likely candidates.

```csharp=
public class GrossToNetCalculator
{
    public GrossToNetCalculator(
        IGrossEnergyYield grossYield,
        double grossEnergy,
        double hysteresisLoss,
        double curtailmentLossGrid,
        double turbineLossTurbulence,
        double electricalLoss,
        double turbineLossShear,
        double turbinePerformanceExperience,
        double operationalExperienceLoss)
    {
        double dependentLoss = 
            CombinePercentages(
                grossYield.TurbineAvailability,
                grossYield.BalanceAvailability,
                grossYield.AccessibilityAvailability,
                hysteresisLoss,
                electricalLoss,
                grossYield.EnvironmentalShutdownWeather,
                grossYield.EnvironmentalSiteAccess,
                grossYield.EnvironmentTreeGrowth);

        double independentLoss = 
            CombinePercentages(
                grossYield.GridAvailability,
                turbinePerformanceExperience,
                turbineLossTurbulence,
                grossYield.EnvironmentalPerformanceDegradationIcing,
                grossYield.CurtailmentPowerPurchase,
                grossYield.SubOptimalPerformance,
                turbineLossShear,
                operationalExperienceLoss);

        GrossToNet = 
        	1 - 
            (1 - (dependentLoss + curtailmentLossGrid))
            * (1 - independentLoss);
    }

    double CombinePercentages(params double[] percentages)
    {
        double combination = 1;
        foreach (var percentage in percentages)
            combination *= 1 - percentage;
        return 1 - combination;
    }

    public double GrossToNet { get; private set; }
}
```

This code is relatively simple, and when I look at it these are the potential changes that I see:

* Items could be added or removed from the `dependentLoss` and `independentLoss` calculations. Items could be also be moved between `dependentLoss` and `independentLoss`, but this is essentially the same thing
* The calculation of `GrossToNet` could change
* The `CombinePercentages` calculation could change

As with most things in computer programming, there is a tension when applying the Open-Closed Principle. 

On the one hand, making the code more easily extensible is good. On the other hand, doing this often breaks encapsulation, adds complication, and adds unnecessary levels of abstraction. 

So again, we need to make a decision about which of these changes we want to support and make the code 'open to'_._ We can then avoid adding unnecessary complication to the code for unsuitable changes. 

It is worth remembering that the work can always be done later, when it will be easier, as we will know exactly what is required.

To make a decision about what changes we should support and make the code 'open to',  we need to estimate how likely the change is to occur, think about design solutions, and then think about the trade offs.

## We Could Add or Remove Items from the dependentLoss and independentLoss Calculations

###   
Very likely to change

The calculation of `dependentLoss` and `independentLoss` (for example `double dependentLoss = CombinePercentages(...)`) each use 8 parameters (`electricalLoss`, `TurbineAvailability` and so on).

These 16 make up the majority of the 17 total inputs to the entire calculation. So, from a purely statistical point of view, a change to one of these has a 16/17 (94%) chance of affecting these calculations.

It's also easy to imagine that we might want to add another "Loss" or "Availability" or similar in the future, or that a current one is no longer relevant, or that different combinations will be required in different circumstances.

### Possible solution

Take a list of dependent and independent losses in the constructor, instead of taking each loss individually. So the existing constructor:

```csharp=
public GrossToNetCalculator(
	...
    double hysteresisLoss,
    double curtailmentLossGrid,
    ...)
```

is replaced with this:

```csharp=
public GrossToNetCalculator(
    IReadOnlyList<double> dependentLosses
    IReadOnlyList<double> independentLosses)
```

This means that if the change is requested, we can implement it without changing the class (and instead just changing the parameters we pass to the constructor). 

For example, if another 'dependentLoss' is requested, we can just add this to the `dependentLosses` list.

(You can see the [code on GitHub here](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/ListParameters))

### Trade offs

A small amount of encapsulation is lost, and the calling code would now be in charge of deciding which losses to pass in.

The code adheres much better to the Open-Closed Principle and becomes much more easily extendable and reusable. If you need to make a change, you won't need to modify the tests, which is useful as they are complicated. 

Tests for the calling code would have to modified, but only to verify that they pass the correct parameters, which is much simpler. 

It is possible that the constructor parameters are passed around in the code base, and now there are only two parameters, as opposed to the previous nine.

### Decision

We should implement this solution to support this change and make the code 'open' to it. 

## The GrossToNet Calculation Could Change

###   
Unlikely to change

The GrossToNet calculation is `GrossToNet = 1 - (1 - (dependentLoss + curtailmentLossGrid)) * (1 - independentLoss);`

Only the `curtailmentLossGrid` parameter is used, aside from the `dependentLoss` and `independentLoss` which are covered earlier.

This 1 parameter is a small minority of the 17 total inputs to the entire calculation. So, from a purely statistical point of view, a change to one of these has a 1/17 (6%) chance of affecting this calculation.

### Possible solutions

1. Take a lambda parameter in the constructor to calculate `GrossToNet` and pass it `dependentLoss` and `independentLoss`, so that the calculation becomes `GrossToNet = grossToNetCalculatorLambda(dependentLoss, independentLoss)`([code on GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/GrossToNetLambda))
2. Remove `curtailmentLossGrid` from the calculation, which then becomes completely generic and can be renamed to `PercentageCombiner`. Require that the calling code applies this adjustment (this adjustment is too complicated for useful example code)
3. Remove `curtailmentLossGrid` from the calculation as above, then recreate the original `GrossToNetCalculator`, using the `PercentageCombiner` and adding `curtailmentLossGrid` to the calculation   
([code on GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/PercentageCombiner))

### Trade Offs

A large amount of encapsulation is lost for options 1 and 2. Option 3 is a reasonable amount of work, and adds a layer of abstraction.

### Decision

This change isn't likely to happen, so it probably isn't worth the effort involved to support it and make the code 'open' to it. But if we had another use for the new `PercentageCombiner` then it would definitely be worthwhile.

## The CombinePercentages Calculation Could Change

###   
Very unlikely to change

```csharp=
CombinePercentages(params double[] percentages)
{
    double combination = 1;
    foreach (var percentage in percentages)
    combination *= 1 - percentage;
    return 1 - combination;
}
```

The CombinePercentages calculation implements some standard laws of math / statistics, which do not change.

### Possible solutions

1. Take a lambda parameter in the constructor to combine the percentages, and use this instead of the CombinePercentages function. So instead of having `double dependentLoss = CombinePercentages(...)`, you would have  `double dependentLoss = combinePercentagesLambda(...)`.   
([code on GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/CombinePercentagesLambda))
2. Create a `PercentageCombiner` abstraction, take this in the constructor to combine the percentages, and use this instead of the CombinePercentages function. So instead of having `double dependentLoss = CombinePercentages(...)`, you would have `double dependentLoss = percentageCombiner.CombinePercentages(...)`.  
([code on GitHub](https://github.com/ceddlyburge/open-closed-principle/tree/master/OpenClosedPrinciple/PercentageCombinerAbstraction))

### Trade offs

Combining percentages is at the heart of what this code does, so removing this logic makes the code mostly useless. 

Option 1 passes all the responsibility for this on to the caller, whereas option 2 at least allows for predefined implementations of the abstraction.

### Decision

This change is very unlikely, and the only reasonable solution (option 2) requires a lot of work and adds complexity and abstraction. 

This means that it would only make sense to do it when the change is actually required, and even then only if multiple algorithms are required. Note that if a change is required to the algorithm, it will make more sense to simply change the implementation of the CombinePercentages function.

## Conclusion

Deciding whether code adheres to the Open-Closed Principle is almost always a judgement call, and there are usually trade offs involved with encapsulation, complexity and abstraction. 

It is worth thinking about likely changes and extensions, and using these to guide your decisions.

