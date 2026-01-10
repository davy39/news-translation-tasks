---
title: How to Make Calculation Tests Simpler and More Expressive with These New Refactorings
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2021-02-03T17:32:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-complicated-calculations-new-refactoring
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/unit-testing-calculations.JPG
tags:
- name: refactoring
  slug: refactoring
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'It is a good idea to make tests as descriptive as possible – to achieve
  Tests as Documentation. Including the calculations in the test is a big part of
  this, and avoids the Hard Coded Test Data smell.

  For example, if a test looks like this, it is har...'
---

It is a good idea to make tests as descriptive as possible – to achieve [Tests as Documentation](http://xunitpatterns.com/Goals%20of%20Test%20Automation.html#Tests%20as%20Documentation). Including the calculations in the test is a big part of this, and avoids the [Hard Coded Test Data](http://xunitpatterns.com/Obscure%20Test.html#Hard-Coded%20Test%20Data) smell.

For example, if a test looks like this, it is hard to know what the problem is when it fails, as the test data is all hard coded. The test tells you very little about how the system under test (SUT) should behave, and so doesn’t act as documentation.

```python
assert sut.wake_erosion_rate(0.03) == 0.8

```

However, if you remove this code smell, and include the calculation in the test, it becomes obvious what the problem is when there is a failure, and the test does now act as documentation. 

You might also want to replace the `2.5` and `0.05` with the names of the constants they represent.

```python
ambient_turbuluence = 0.03

assert 
    sut.wake_erosion_rate(ambient_turbuluence) 
    == 2.5 * ambient_turbuluence + 0.05

```

This article references the excellent [XUnit Test Patterns book](https://www.goodreads.com/review/show/2179089513), which defines the most widely accepted lexicon on unit test patterns and practices.

## Example Calculation

The rest of this article will discuss the [example ConstructionMarginCalculator class](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator.py#L31), and will describe refactorings that simplify the tests and allow them to feasibly include the calculations. 

The calculation is around 30 lines long, and is worth a quick glance now if you have the time. But if not, don’t worry, the rest of this post will still make sense.

There are a few if statements and a loop, and in total these lead to 2^9, or 512, paths through the code! Eek! It is clearly not feasible (or useful) to test all these, hence the need to find ways to make it easier.

This example code has an [initial naive test](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator.py#L17), which is around 30 lines long. It doesn’t include the calculations, and introducing them would make the test even longer and more complicated, so would be hard to justify.

Each of the following sections describes a refactoring, and includes links to the refactored example code. These build on the existing [test refactorings](http://xunitpatterns.com/Test%20Refactorings.html) from [XUnit Test Patterns](https://www.goodreads.com/review/show/2179089513).

The refactorings reduce the number of paths through the code and simplify the test. This means that fewer tests are needed, and that the tests become small and simple enough to include the calculations.

## Extract Calculation From Loop

The code initially calculates values for a _list of_ `steps`, which means that any test for it must take on this complication. 

The setup of the test is harder, as we have to create a list as opposed to a single value. The assertions are harder as we have to assert on a list as opposed to a single value. Finally, we should have multiple tests (probably for 0, 1, and multiple items in the list).

The easy fix is simply to refactor the code so that it only calculates a single `step`. This displaces the iteration code to some other place, which might want testing. However, this can be tested using a Mock, so only the iteration needs to be tested (as opposed to the iteration _and_ the calculation), which is simple, and potentially so simple that you don’t need to test it.

This refactoring means that instead of requiring 3 tests (for 0, 1, and multiple items in the list), there is now just one. This reduces the number of paths through the code from 2^9 to 2^7, or 128. This is already a lot better, but still too many to test!

* [Refactored Calculation](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_without_loop.py#L31)
* [Refactored Test](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_remove_loop.py#L11)

## Introduce Mockable Abstractions

The details of the inflation calculation aren’t shown in the example, but they are reasonably complicated.

To avoid this we can change the code to accept an `InflationCalculator`. The inflation calculation always uses the same `date_of_financial_close`, `inflation_rate` and `inflation_mode`, which means that it can take these in the constructor. This in turn means that the main calculation no longer requires the `inflation_rate` and `inflation_mode`.

Then in the tests we can create a mock `InflationCalculator`. This could for example always return a value of `2`, which makes the overall calculation a lot simpler.

It is also easy to imagine that inflation calculations will happen in other parts of the code, so the abstraction will be widely useful.

This step means that instead of 4 conditional branches in the inflation calculation, there is now just one. This reduces the number of paths through the code from 2^7 to 2^3, or just 8. It is also necessary to test the `InflationCalculator`, and this has 4 branches, so needs 4 tests, but this still only makes 12 tests in total. Yay for loosely coupled code!

We now have a feasible number of tests to write, but including the calculation in the test is still going to be very cumbersome. Luckily we still have some refactorings left up our sleeve.

* [Refactored Calculation](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Refactored Test](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_mockable_abstraction.py#L11)

## Test Conditional Branches in Isolation

The code branches based on certain conditionals. We can simply make some of these conditionals `False`, and then test each branch of the code in isolation. This way, each test only has to include the calculation for the branch that it is concerned with.

For example, we can set `in_selling_mode` to be `False` and `step.start_of_step` to be different to `date_of_financial_close`. This makes the test simple enough that it is feasible for it to perform the same calculation that the code does. 

This in turn means that the test clearly communicates that the `turbine_cost_including_margin` should be the `turbine_costs * fraction_of_spend * inflation`. This helps readers understand the calculator, and achieves the goal of [Tests as Documentation](http://xunitpatterns.com/Goals%20of%20Test%20Automation.html#Tests%20as%20Documentation)

At the moment the test is still quite long. However, because we are only testing a small part of the calculation, a lot of this information is now irrelevant (the `any_double` variable). This means we can now create a [Test Data Builder](http://natpryce.com/articles/000714.html), or use helper functions to make things more concise. We will see an example of this in the next refactoring.

* [No Change to Calculation](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Refactored Test](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_isolate_branches.py#L16)

## Test Values in Isolation

“Test Conditional Branches in Isolation” is a useful technique, but it can still leave us with some complications if a value is calculated / updated in multiple branches. 

A good example of this is `balance_of_plant_cost_including_margin`, which is set initially, and then updated in the `if (in_selling_mode)` branch.

Testing `balance_of_plant_cost_including_margin` in isolation allows the test to concentrate just on this one value / calculation, which means that a lot less setup is required. The [Test Data Builder](http://natpryce.com/articles/000714.html) pattern hides [Irrelevant Information](http://xunitpatterns.com/Obscure%20Test.html#Irrelevant%20Information), and the test becomes more concise and expressive.

Including the calculation continues to make the test clearly communicate its intent and act as documentation. Interestingly the test calculation code is no longer an exact copy of the SUT calculation code, as it already knows that it is `in_selling_mode`, so doesn’t need a conditional statement. This means that the test is simpler than the code, which helps avoid the [Obscure Test](http://xunitpatterns.com/Obscure%20Test.html) smell.

* [No Change to Calculation](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Refactored Test](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_isolate_values.py#L18)

## Test Partial Values in Isolation

Sometimes the calculation of individual values is very complex, and can’t be split up by conditional branches. This can make it challenging to include the calculation in the test. `construction_profit` is a reasonable example of this, which is calculated as follows:

```python
step.turbine_cost_including_margin = 
 turbine_costs * inflation * fraction_of_spend;

step.balance_of_plant_cost_including_margin = 
 balance_of_plant_costs_at_financial_close * inflation * fraction_of_spend;

step.construction_profit = 
 -1 * 
 (step.turbine_cost_including_margin + step.balance_of_plant_cost_including_margin) *
 epc_margin

```

`inflation`, `fraction_of_spend` and `epc_margin` have a multiplicative effect, so if we set them to `1`, they won’t have any effect and we can easily write a test for the rest of the logic.

`step.turbine_cost_including_margin` and `step.balance_of_plant_cost_including_margin` have an additive effect, so if we set them to `0`, again they won’t have any effect and we can easily write a test for the rest of the logic.

Testing just a portion of `construction_profit` in isolation allows the test to concentrate just on this part of the calculation, which, as before, makes the test shorter and simpler, and avoids the [Obscure Test](https://hackmd.io/4xuiUbrAQimsWCknJiqXNw?both) smell.

* [No Change to Calculation](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_mockable_abstraction.py#L29)
* [Refactored Test](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_isolate_partial_values.py#L14)

## Introduce the Blackboard Pattern

The Blackboard pattern is a more involved technique, and is often badly understood. But essentially it involves using a “blackboard” to break the dependencies within complicated calculations.

In this example the `construction_profit` depends on `turbine_cost_including_margin` and `balance_of_plant_cost_including_margin`, which are themselves calculated from the inputs. This makes testing harder. 

In order to test the `construction_profit` you essentially also have to test `turbine_cost_including_margin` and `balance_of_plant_cost_including_margin`.

When we introduce the blackboard pattern, one calculator writes the `turbine_cost_including_margin` and `balance_of_plant_cost_including_margin` to the blackboard, and when calculating the `construction_profit` we read these values from the blackboard.

This breaks the connection between the two things, so when testing we can just add values for `turbine_cost_including_margin` and `balance_of_plant_cost_including_margin` to the blackboard.

* [Refactored Calculation](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/cash_flow_calculator/construction_margin_calculator_blackboard_pattern.py#L15)
* [Refactored Test](https://github.com/ceddlyburge/unit-testing-calculations/blob/main/tests/test_construction_margin_calculator_blackboard_pattern.py#L12)

## Conclusion

When testing calculations, it is important to include the calculation in the tests. This avoids the [Hard Coded Test Data](http://xunitpatterns.com/Obscure%20Test.html#Hard-Coded%20Test%20Data) smell, allows the tests to clearly express their intent and achieve [Tests as Documentation](http://xunitpatterns.com/Goals%20of%20Test%20Automation.html#Tests%20as%20Documentation).

The refactorings described in this article allow you to do this while also making sure that the tests are concise and understandable.

