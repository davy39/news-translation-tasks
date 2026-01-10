---
title: How to Create Documentation from Your Python Tests
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2020-09-15T19:12:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-documentation-from-your-python-tests
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/docs-from_tests_example_graph.png
tags:
- name: automation
  slug: automation
- name: documentation
  slug: documentation
- name: Python
  slug: python
- name: Testing
  slug: testing
seo_title: null
seo_desc: "What if I told you that you could automatically create documentation from\
  \ your existing tests that would always be up to date? \nAnd what if it could be\
  \ in markdown format, so it would be committed along with the rest of your code,\
  \ and be shown on Git..."
---

What if I told you that you could automatically create documentation from your existing tests that would always be up to date? 

And what if it could be in markdown format, so it would be committed along with the rest of your code, and be shown on GitLab / GitHub?

Sounds pretty cool, right? Let's see how it's done.

### Context

People like [Simon Brown](https://c4model.com/) do a great job of convincing me that I don't have enough documentation for my projects. And that the documentation should be up to date, and show concise information at a variety of levels of abstraction. 

I would love to work on a code base with documentation like that.

## The Problem with Documentation

I have read a good number of [books](https://www.goodreads.com/book/show/44144493-fundamentals-of-software-architecture) and articles about software architecture and related things. But I have never been able to summon up enough energy, or enough political capital, to be able to create documentation to this standard. Let alone keep it up to date.

So, for my situation at least, I need a way of creating and updating documentation automatically. 

I would also like to store the diagrams "as code", so that they can be checked in to the repository. This way, changes to them can be easily seen and discussed in pull requests and other code reviews.

There are many [tools](https://structurizr.com/help/code) that can generate build time dependency diagrams from code, and I have used quite a few of them. 

But the problem seems to be that these diagrams always look like spaghetti, even when the code is good. And they are complex to set up. 

It seems to be very hard to get the level of detail right. There is no way to show related code in logical groups for high level diagrams. There is also no way to pick out code relationships that are specific to a particular context for low level diagrams. 

They also give you no information about the run time relationships of the code, which is usually a bigger issue than the design time relationships.

## A solution

To capture run time relationships, generating diagrams from running code is the only option. And we already have plenty of code that is executed regularly, in the form of tests.

Repositories should already have a good suite of tests (unit, integration and end to end, for example), and each test should be relatively short and simple. 

These tests should already embody logical groupings of code, and sensible levels of abstraction. So they are an excellent candidate for generating documentation.

The solution involves instrumenting the code imported by a test. This instrumented code then keeps a record of the run time call hierarchy, and is able to write the results as a [Mermaid markdown diagram](https://mermaid-js.github.io/mermaid/#/) (tecnhically a [sequence diagram](http://agilemodeling.com/artifacts/sequenceDiagram.htm)).

The code below ([a test from the python package](https://github.com/resgroup/docs-from-tests/blob/master/tests/test_hello_world.py)) shows how it works. 

For each existing test you create a "wrapper" test, which is responsible for initialising the call hierarchy and saving the diagram. If you have a lot of tests you might want to introduce a [decorator](https://realpython.com/primer-on-python-decorators/) to save repetition.

```python
from docs_from_tests.instrument_call_hierarchy import instrument_and_import_package, instrument_and_import_module, initialise_call_hierarchy, finalise_call_hierarchy
from samples.hello_world_combiner import HelloWorldCombiner

# you can instrument entire packages / folders at once like this
instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'samples'), 'samples')
# You can instrument individual modules like this
# instrument_and_import_module('tests.blah')

# this is a wrapper around the test that also outputs the documentation / sequence diagram
def test_hello_world():
    # the initialises the recording of the call hierarchy
    initialise_call_hierarchy('start')

    # This runs the actual test
    _test_hello_world()
    
    # this finalises the call hierarchy and returns the root
    root_call = finalise_call_hierarchy()

    # this returns a sequence diagram of the call hierarchy
    sequence_diagram = root_call.sequence_diagram(
        show_private_functions=False,
        excluded_functions=[
            'HelloWorldCombiner.__init__',
        ]
    )

    # this writes out the markdown to disk    
    sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'top-level-sequence-diagram.md')
    Path(sequence_diagram_filename).write_text(sequence_diagram)

# this is the original / source test
def _test_hello_world():
    assert HelloWorldCombiner().combine() == 'Hello world'

```

Running `pytest` on this code will result in the test being run, and the [markdown "diagram as code"](https://github.com/resgroup/docs-from-tests/blob/master/doc/top-level-sequence-diagram.md) (below) being created in the doc directory:

```
sequenceDiagram
  start->>HelloWorldCombiner.combine: calls x1
  HelloWorldCombiner.combine->>hello: calls x1
  hello-->>HelloWorldCombiner.combine: returns str
  HelloWorldCombiner.combine->>world: calls x1
  world-->>HelloWorldCombiner.combine: returns str
  HelloWorldCombiner.combine-->>start: returns str

```

This renders as the following diagram:

![Example docs-from-tests diagram](https://www.freecodecamp.org/news/content/images/2020/09/docs-from_tests_example_graph-2.png)

Changes to the diagram will show up in Git and be committed along with the code that caused the change. This means that the change to the code and the change to the diagram are linked and can be seen together.

Private methods would usually be excluded (although it is optional), and you can exclude other functions so that the graph looks as desired. 

Because the call hierarchy is stored in a tree structure, excluding a function also excludes all the functions beneath it.

## Code quality

Hopefully you already have tests at appropriate levels of abstraction (classically you would have unit, integration and end to end). This makes it easy to create diagrams at these levels. 

If not, then the desire to create good diagrams should guide you towards also creating good tests.

Sometimes the diagrams will look a bit crazy, and you may end up ignoring a lot of functions. This is a clue that the code could probably be made simpler. And in this case the desire to create good diagrams should guide you towards simplifying the code.

## Conclusion

Hopefully this will inspire you to create and maintain the documentation that your teammates and your future self will thank you for! It's all quite easy to do.  

All the functionality is in a Python package ([docs-from-tests)](https://pypi.org/project/docs-from-tests/), and there is an [example repo that demonstrates how to use it](https://github.com/ceddlyburge/docs-from-tests-example).

