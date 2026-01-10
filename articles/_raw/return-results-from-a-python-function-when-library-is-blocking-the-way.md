---
title: How to Return Results from a Python Function to Your Program When a Library
  is Blocking the Way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-14T10:46:14.000Z'
originalURL: https://freecodecamp.org/news/return-results-from-a-python-function-when-library-is-blocking-the-way
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/master-gmd-gmd370-g3701-g3701s-cw0011000.jpg
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "By David A. Kra\nUsually a Python function passes its results back using\
  \ a return statement.\nThe problem is that sometimes it can't, so you need to figure\
  \ out a different way to return those results. \nThis happens, most often, when\
  \ someone else's libr..."
---

By David A. Kra

Usually a Python function passes its results back using a `return` statement.

The problem is that sometimes it can't, so you need to figure out a different way to return those results. 

This happens, most often, when someone else's library's interface is in the way, and you can't change it. 

What you need to accomplish might be called passing results out-of-band, in a side-stream, circumventing, bypassing, or doing an end-run. 

This tutorial describes this problem at several levels of difficulty, then provides several solutions to handle those levels, including one not to use, and why. 

There is advice on how use as few as possible different solutions to cover the problem in your project. 

This is a long article, because it walks you through a progression of problem severities and their solutions. 

However, you might only need the beginning, one or two of the solutions described, and the guidance near the end.

<p>Contents of this tutorial:</p>
<ul>
    <li><a href="#when-does-this-problem-happen">When Does this Problem Happen?</a>
    </li><li><a href="#how-to-find-a-solution-depending-on-the-problem-s-severity">How to Find a Solution, Depending on the Problem's Severity</a>
	</li><li><a href="#several-possible-solutions">Several Possible Solutions</a>
</li><li><a href="#example-of-a-python-library-that-gets-in-the-way-of-passing-useful-results">Example of a Python Library that Gets in the Way of Passing Useful Results</a>
    </li><li>Solutions with examples and discussion</li>
		<ul>	<li><a href="#solution-1-using-a-function-attribute">Solution #1: Function attribute</a>
			</li><li><a href="#solution-2-using-a-global-variable">Solution #2: Global variable (Deprecated Anti-pattern)</a>
			</li><li><a href="#solution-3-using-a-queue">Solution #3: Queue</a>
			</li><li><a href="#solution-4-multiple-queues">Solution #4: Queues</a>
				<ul><li><a href="#what-if-your-high-level-program-only-needs-the-last-of-all-the-extended-results">Variation: Last In First Out (LIFO) queue</a>
				</li><li><a href="#design-possibility-combine-both-viable-solutions">Variation: Both attribute and queue</a>
				</ul>
			</li><li><a href="#solution-5-simple-python-wrapper">Solution #5: Simple python wrapper</a>
			</li><li><a href="#solution-6-python-decorator-wrapper">Solution #6: Python decorator wrapper</a>
	</ul>
</li><li><a href="#advice-on-selecting-which-solution-to-use">Advice Selecting Which Solution to Use</a>
</li><li><a href="#summary">Summary</a>
</ul>

## When Does this Problem Happen?

You have the problem if a library is in the way, but you need to use it.

Imagine your high level function program, **_p,_** calls a third-party library function, **_L,_** which then calls your low level target function,  **_f_**. 

A good example of such a library function is `timeit`. 

The top level program must invoke the library function and get returned results in accordance with that library's documented Application Programming Interface (API) specifications. 

Similarly, function **_f_** accepts parameters and must return results that again conform with that library function's API specifications. 

Library function **_L_** is an interposing intermediary. 

The problem happens when the intermediary library and its API are not under your control and don't meet your need for acquiring the target function's results.

Often the API for returning results from a lower level function to the intermediary library and the API from the library to your higher level function, in combination, will not pass the lower level function's complete results.

Typically, the library comes from pip, Git, Anaconda, or Python itself. 

Even if these libraries are open source, still you, your peers, your employer, and your clients do not want anyone tinkering with the library's internals and externals.

Also, if  the library is like `timeit.repeat` or `scipy.optimize.minimize`, then the low level target function will usually be called many times. 

## How to Find a Solution Depending on the Problem's Severity

How can a Python program circumvent an intermediary library blockade?

The concepts you have to learn and use to handle the problem depend on the extent of the needs: 

1. **Most recent result:** Your top level function needs access only to the most recent result from the low level function, even if it has been called many times. This solution uses the idea of [memoization](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/) by storing the last result in [an attribute of the lower level function](https://sethdandridge.com/blog/assigning-attributes-to-python-functions). By using a naming convention, the name of the attribute is always the same. That is safe, no matter how many different functions, even aliases, use that same attribute name.  Instead of using an attribute, an alternative solution uses the concept of a [global variable](https://www.freecodecamp.org/news/python-global-variables-examples/#keyword). Using a global variable is not a good thing to do. The provided example demonstrates how it is an unsafe bad practice. 
2. **Need every result:** Your top level function needs the result of each of many calls which the library makes to the low level function. The solution uses the concept of a [queue](https://www.guru99.com/python-queue-example.html), as implemented by [Python's standard queue library](https://docs.python.org/3/library/queue.html). 
3. **Need every result, but going to different places:** Multiple places in high level functions call the low level function through one or more intermediaries. Each needs its own set of results. The solution uses multiple queues, with which-queue-to-use being passed as a parameter to the low level function.
4. **Can't enhance the low level function:** The low level function comes from a library or elsewhere so you can not or must not change it. The solution uses the concept of a [wrapper](https://en.wikipedia.org/wiki/Wrapper_function). The wrapper sets up the queue and attributes, calls the low level function, and does what is necessary with the result. The solution uses the generic concept of a wrapper, but does not use the advanced python concept of "decorator wrappers."
5. **Can't enhance the low level function. Need every result, but going to different places:** This combines the most advanced needs. The solution exploits the advanced Python concept of [decorator wrappers](https://forum.freecodecamp.org/t/python-decorators-explained-with-examples/19198). This eliminates the need to pass queue objects as parameters.

Example code is provided for each of these.

My case that initially drove this effort was at the level of "need every result". 

The intermediary was a nested loop involving two library functions. 

My high level program invoked the  `timeit.repeat` function which then invoked `scipy.optimize.minimize` several times. 

Each invocation of `scipy.optimize.minimize` invoked my low level function many times. 

For each execution of my low level function, I wanted it to pass results to the main program, all the way up and around both libraries.

The design and development effort kept some good practices in mind:

* **Avoid naming conflicts or interference:** This is especially important when there are several target functions that need to return their own side-stream results. It is also important when the target function might be called from several places in the high level code or through multiple intermediaries.
* **Avoid coupling:** Minimize explicit coupling between the high level and the low level functions.
* **Provide optionalityL** Avoid inflicting additional coding requirements on the top level caller if it does not need the additional results.

### Several Possible Solutions

The first two solution alternatives in this tutorial are applicable when only a single result is needed, and that result comes from the final execution of the target function.

The third solution alternative is applicable when a result is needed from each execution of the target function or each completed execution of an interior loop of calls to the target function.

1. Function Attribute – Good for one result. Each setting of a result overwrites the previous one.
2. Global Variable – Good for one result. Each setting also overwrites the previous one. This alternative is a deprecated anti-pattern for Pythonic philosophical and technical reasons, which will be explained below.
3. Queue – Good for one or more results. There are choices regarding the ordering of results. 
4. Queues – Good for multiple results, but where they don't all go to the same place.  
5. Simple Wrapper – Good when you cannot change the lower level function. This solution is not really fundamentally different placing results into an attribute or queue. However, it externalizes the code that would go inside the target function. The result is a function that wraps the target function, which might be unchangeable, in some library, in a way that does not require advanced Python expertise.
6. Python Decorator Wrapper – Uses the advanced Python function wrapping "decorator" mechanism. It allows multiple queues and attributes without altering the underlying low level function. It may be challenging to understand, but is easy to use in your code.

All the alternatives work with multithreading. 

The queue and wrapper alternatives also work with multiprocessing.

## Example of a Python Library that Gets in the Way of Passing Useful Results

Let's first cause the problem, and then we'll go through each possible solution.

```python
# LibraryL.py
# usage:  from LibraryL import L
# The purpose of this library and its sole function is to demonstrate an intermediary that prevents an invoked function from returning useful results to the high level caller.
# Imagine it is in an external library not under the application programmer's control.
#

def L(f,fparms=[],Lparms=[]): # intermediary function
# f: target function; 
# fparms: parameter object to be passed to f. Defaults to []
# Lparms: object to be used by L itself (unused in this example).  Defaults to [].

    rf=f(fparms) # pass fparms to f, call f, collect its return value
    return rf.__class__.__name__
    
# L does not return to its caller any of what function f returned to L, only the returned object's class's name, such as 'list'. This is a good example of a bad example.
```

This function, L, will be used as the intermediary function in the solution examples below.

### Solution #1: Using a function attribute

The low level function stores its useful result in a Python attribute, in accordance with a naming convention.

```python
def f(fparms):  # Low level function to be called through an intermediate
# Attribute naming convention: <function_name>.mrrv 
#     where mrrv stands for  Most Recent Result Value
    # Create the attribute, so it exists even in case an exception is thrown before the result is set.
    
    if not hasattr(f, "mrrv"): f.mrrv=None  
    # f.mrrv=None # uncomment to clear it out on each call.
    # do work …
    
    ultimate_result=["this", "that", 42, "and the other thing"]
    f.mrrv=ultimate_result
    result_to_return=42
    return result_to_return

def p(): # High level function calling f through the intermediary L
    from LibraryL import L
    fparms=[]
    Lparms=[]
    r=L(f, fparms, Lparms) # invoke f through L
    resultfromf=f.mrrv
    print(resultfromf)
    # do work …
p()
quit()
```

Output: 

`['this', 'that', 42, 'and the other thing']`

In this solution, the invoked function places its side-stream result into an attribute within the function object, in accordance with a simple naming convention. 

Each function has its own local attribute in which to deposit results. 

The attribute's name, `mrrv`,  for most recent result value is the same in all functions that use this technique, so it works even when the called function is called through an alias, as in the following example:

```python
# Demonstration of how the attribute solution works correctly,
#   even if the target function has been aliased.  

def get_target_function():
   return f

def p():
    g=get_target_function() # g.__name__ would provide the string name of the underlying aliased function. So what? We don't need it. 
    # Do other things.
    from LibraryL import L
    gparms=[]
    Lparms=[]
    r=L(g, gparms, Lparms) # invoke g through L
    # L invokes g, which is really f
    # f sets f.mrrv 
    # Don't care that g is not the function's real name.
    resultfromg=g.mrrv # No problem. 
    print(resultfromg)

p()
quit()
```

Output: 

`['this', 'that', 42, 'and the other thing']`

The attribute has a single value in each function, although that single value could be a list or other complex object. 

Even if the function is called from many places in the code, even if from many threads, the attribute will still have only the value set most recently by any call in the process.

In the initial housekeeping at the top of the low level function, if the attribute does not already exist, the attribute's value is set to `None`. 

This way, even if the function returns without setting the attribute to a useful value, references to the attribute will not throw an exception. 

Optionally, the attribute could be set to `None` at the beginning of every call, in order to clear out any previous result. 

Doing that may be undesirable in a multithreading environment.

### Solution #2: Using a global variable

**Warning:** This solution alternative is a deprecated [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) for Pythonic philosophical and technical reasons, which I'll explain below. 

I've provided it only as a straw man for educational purposes to illustrate poor programming practices:

```python
def f(fparms): # DEPRECATED Low level function to be called through an intermediate
    # Global object naming convention:    <invoked_function_name>_mrrv
    # where mrrv represents Most Recent Result Value
    
    global f_mrrv
    f_mrrv=None # clears the global, in case an exception is thrown before the result is set.
    # do work, then
    
    ultimate_result=["this", "that", 42, "and the other thing"]
    f_mrrv=ultimate_result
    result_to_return=42
    return result_to_return

def p(): # top level calling program
    from LibraryL import L
    # Global object naming convention:     <invoked_function_name>_mrrv
    global f_mrrv # unnecessary to use this global statement if L is called from __main__ , but doesn't hurt
    fparms=[]
    Lparms=[]
    r=L(f, fparms, Lparms) # invoke f through L
    resultfromf=f_mrrv
    print(resultfromf)
# do work.

p()
quit()
```

Output:

`['this', 'that', 42, 'and the other thing']`

This solution gives each function its own global place to deposit results. 

The variable name is based on the name of the invoked function. 

The invoked function places its side-stream result into its global variable. 

Function `framus` would place its result in the global variable `framus_mrrv`.

In the initial housekeeping at the top of the invoked function, the code sets the value of the global variable to `None`. 

This way, even if the function returns without setting the variable to a useful value, references to the variable will not throw an exception. 

Also, any result from a previous call is cleared out. 

The global variable is a single value, although that single value could be a list or other complex object. 

Even if the function is called from many places in the code, the global variable will have only the most recent value set by any call to that function within the process.

#### Why is this solution deprecated?

This global variable alternative is deprecated for both Pythonic philosophical and technical reasons.

**Philosophical**: This solution inflicts itself onto the code of the higher level function and injects an object into the global namespace. The attribute solution does not do that. The low level function might be used in many programs. Some might not need the extended result. With the attribute solution, if the high level invoker does not need the extended result, it does not need to be concerned about it or do anything extra.

**Technical**: In a technical way, the global variable solution is not robust. Python treats functions as first class objects. The same function object can be assigned to multiple variable names. Each name can then be used as an alias for the function. The upcoming broken demonstration code does that. 

In the example, the target function creates a global variable with one name.

Afterwards, the higher level function looks for the result somewhere else, assuming it has a different name.

The attribute solution avoids this problem. 

With the attribute solution, the target function sets an attribute, `mrrv` , inside the function itself, not in some other object. 

The high level function references that same attribute name in this same object, even if referencing the object through an alias. 

It can do that because the attribute name is tied to the object it is part of, not the name used to access the object.

Let's see how the global variable solution is broken:

```python
# Demonstration of how the global variable solution is broken.
def get_target_function():
   return f

def p(): # BROKEN!  Demonstration why NOT to use the global variable solution.
# Forget or ignore that g is not the function's real name.
    g=get_target_function() # p() does not and cannot know the name of g's targetfunction
    # Do other things.
    
    from LibraryL import L
    # Global object naming convention: <invoked_function_name>_mrrv
    # Create and then use g_mrrv, which the function will not set.
    
    global g_mrrv # NOT GOOD: This is not the name of the global that will be set by the code inside the function.
    gparms=[]
    Lparms=[]
    r=L(g, gparms, Lparms) # invoke g through L
    
    # L invokes g, which is f
    # f sets f_mrrv not g_mrrv
    
    resultfromg=g_mrrv # Has not been set. g (alias for f) did set f_mrrv
    print(resultfromg)
# Fail to do work.
```

### Solution #3: Using a queue

In this solution, the low level function puts its extended results onto a Python queue. A high level function retrieves the results. 

Usually, in Python, we think of using queues in multithreaded or multiprocessing applications. 

Here the queue is used for information transfer between functions even in the same thread. 

There are variations of the queue solution. 

They vary in which function creates the queue and how the other function accesses the queue object. 

In this solution, the queue object is stored in a function attribute in the low level function. The attribute is named in accordance with a naming convention. 

This is conceptually similar to the attribute solution, except that the attribute holds a queue object, rather than the results themselves. The results are put onto the queue. 

If the calling program is interested in the extended results, it can read from the queue once the invoked function has completed.  

**Warning:** If the low level function runs thousands or millions of times without the high level function draining the queue, there could be an out-of-memory process crash.

```python
# Solution #3: Queue object in a function attribute

# low level function
def f(fparms): # ultimate result is put to a queueID which is stored in a function attribute. 
    ultimate_result=None
    # Queue object naming convention: <invoked_function_name>.sidestreamoutq
    
    if not hasattr(f, "sidestreamoutq"): f.sidestreamoutq=queue.Queue() # only create the queue once. 
    # do useful things
    
    ultimate_result=["what comes in is what is returned",fparms]
    f.sidestreamoutq.put(ultimate_result)
    result_to_return=42
    return result_to_return

def get_target_function():
   return f

# high level function
def p():
    fparms4=[4, "queueID in a function attribute", 84]
    fparms5=[5, "queueID in an aliased function's attribute", 84]
    Lparms=[]
    r4=L(f, fparms4, Lparms)
    while not f.sidestreamoutq.empty():
         f_result=f.sidestreamoutq.get()
         print(f_result) 
         
    # now do the same with an alias to the low level function
    
    g=get_target_function() # p() does not and cannot know the name of g's targetfunction
    r5=L(g, fparms5, Lparms)
    while not g.sidestreamoutq.empty(): # Note that g.sidestreamoutq === f.sidestreamoutq. Reading from one is the same as reading from the other.
         g_result=g.sidestreamoutq.get()
         print(g_result)

#  __main__ 
import queue 
from LibraryL import L
p()
quit()
```

In this solution variation, the low level function creates a queue object and then sets a function attribute in itself to refer to it. 

According to a naming convention, the attribute's name is `sidestreamoutq`. 

But because it exists within a function object, it is referred to as `whateverfunctionname.sidestreamoutq`. 

The invoked function puts its side-stream result onto that queue. 

As demonstrated in the example code, this solution works even if the calling program aliases the name of the low level function, such as with `someotherfunctionname=lowlevelfunctionname`, and then invokes `L(`someotherfunctionname`, fparms, Lparms)`.  

The reason is that all the references in `someotherfunctionname` are references to the exact same object instances as in `lowlevelfunctionname`.

In the initial housekeeping at the top of the invoked function, the function (a) sets the value of the extended result to `None` and (b) creates the result queue, but only if it does not already exist. 

Doing that does not automagically force results to be placed onto the queue if the function fails or terminates without an explicit put.

But if the function does not change the value to something else, then if  the function does the put, then the item put onto the queue would have the defined value `None`.

#### Solution #4: Multiple queues

In this solution the upper level functions specify the queues which will get the results. 

No naming convention is required for the queue object. 

The high level function creates a queue object then includes it among the parameters passed through the intermediary to the target. 

The low level function extracts the queue object's value and uses it.  

This is significantly different from the previous solutions. 

The previous solutions have all relied on a naming convention for the object to be shared between the high level invoking function and the target function. 

This is explicit name coupling between the functions. 

In Computer Science, this coupling is generally considered to be undesirable. 

Even in the case of an intermediary, this coupling is usually avoidable, at the expense of an increase in code complexity. 

The "usually avoidable" is whenever the invoker of the intermediary can specify an additional parameter value that will be passed to the target. 

In this case, the extra value is the queue object. 

This solution is not a viable option if the intermediary does not allow the invoker to pass the queue object to the target function. 

Here it is feasible, and the code does it:

```python

# Solution 4. Allow for multiple queues.
def fqp(fparms): # fparms is a list containing values to be passed to f,  including a queue object to be sent the ultimate result 
    ultimate_result=None
    # Extra complexity: Extract the result queue object from the incoming parameter list
    
    sidestreamoutq=None
    for p in fparms: # find and use the first element of parameter list which is a Queue or LifoQueue
        if p.__class__.__name__ in ["Queue", "LifoQueue"] : 
            sidestreamoutq=p
            break
    # do useful things
    
    ultimate_result=["this", "that", 42, "and the other thing", fparms]
    # put the result object to the result queue, if there is one
    
    if not (sidestreamoutq is None): sidestreamoutq.put(ultimate_result)  
    result_to_return=42
    return result_to_return
    
# usage: 
def p():
    potusqueue=queue.Queue() # could use queue.LifoQueue(), and a single get, if you only want the last item
    flotusqueue=queue.LifoQueue() 
    fparms1a=[11, "George", potusqueue, 1788] # bparms is a list containing values to be passed to b
    fparms1b=[12, "George", potusqueue, 1792] # bparms is a list containing values to be passed to b
    fparms2=[3, "no queueID in the parameters", 1789] # by not including the queue object among the parameters, the function will not put results to the queue.
    fparms3=[4, flotusqueue, "Martha", 1788, 1792]
    Lparms=[]
    r1a=L(fqp, fparms1a, Lparms) # invoke fqp through L
    r1b=L(fqp, fparms1b, Lparms) # invoke fqp through L
    r2=L(fqp, fparms2, Lparms) # fparms2 is missing a queueID.
    r3=L(fqp, fparms3, Lparms)
    #print("drain potusqueue and flotusqueue")
    while not potusqueue.empty():
         f_result=potusqueue.get()
         print(f_result)
         # use the f_result
    if not flotusqueue.empty(): # only interested in last result on the LIFO queue
         f_result=flotusqueue.get()
         print(f_result)
         # use the f_result     
     
#  __main__ 
import queue 
from LibraryL import L
p()
quit()
    


In this solution, the invoking function creates one or more LIFO or FIFO queue objects. 

The invoking function includes that queue object among the parameters passed to the library for the library to pass to the target function. 

That invoked function looks for and, if present, extracts the queue object from its incoming parameters.

In the initial housekeeping at the top of the invoked function, it sets the value of the result to `None`. 

Doing that does not cause `None` to be placed on the queue if the function fails or terminates without an explicit put. 

But if the function does not change the value to something else, when the function does the put, then the item on the queue will have the defined value `None`. 

The function only puts results onto the queue if it received a queue object among its parameters.

#### What if your high level program only needs the last of all the extended results?

Sometimes only the last result is interesting to the high level program. 

If that is true, and a queue is being used, there is an alternative to draining the entire queue and keeping only the last result. 

Instead, create the queue as a Last-In-First-out queue with `anyqueue=queue.LifoQueue()` instead of `anyqueue=queue.Queue()`. 

Then the first (and probably only) `anyqueue.get()` will get the final entry put onto the queue.

The example solution code above create two queues, one FIFO and one LIFO. 

It passes the FIFO queue as a parameter on two calls and the LIFO queue on one.

It drains however many results there are on the FIFO queue, but gets only one entry from the LIFO queue. 

That is because the intent is to use the LIFO queue when the most recently put item is the one of initial interest or the only one of interest. 

## Design Possibility – Combine Both Viable Solutions

These two options, (a) target function attribute and (b) invoking function queue object parameter, can be combined. 

The combination lets the high level function optionally specify a queue to receive the extended results. 

If not specified by the high level function, the low level function puts them to the queue object it created and stored in a function attribute. 

The following code does that. 

Note that it does not change the attribute containing the default queue when the function is used with a caller-specified queue. 

This lets callers in multiple places in the calling code use different queues, or use the default queue, as specified in the function's attribute:

```python
def fqap(fparms): # ultimate result is put to a queue object whose value is in a function parameter or, if not specified, in an attribute. 
    ultimate_result=None
    # Queue object attribute naming convention: <invoked_function_name>.sidestreamoutq
    
    if not hasattr(fqap, "sidestreamoutq"): fqap.sidestreamoutq = queue.Queue() # only create the default queue attribute once. It might never be used.
    q2use = fqap.sidestreamoutq
    for p in fparms: # find and use the first parameter that is a Queue or LifoQueue, if there is one.
        if p.__class__.__name__ in ["Queue", "LifoQueue"] : 
            q2use=p
            break
    # do useful things
    
    ultimate_result=["this", "that", 42, "and the other thing", fparms]
    fqap.mrrv=ultimate_result
    q2use.put(ultimate_result)
    result_to_return=42
    return result_to_return
```

Some things to keep in mind when using queue based solutions:

**Memory**: Queue entries exist in virtual memory. If the extended results are placed onto a queue, but never retrieved, then after thousands or millions of calls, eventually the process or system will run out of memory and crash (unless the process ends first). Whether by orderly termination or due to crash, at that point any queue elements that have not been retrieved are discarded.

**Multiple aliases for the same queue:** The attribute-based variation has one queue object no matter how many aliases the function has. When a high level function drains an attribute-based queue, the loop will get all results on that queue, even if they were placed there by a call to the function under some other alias.  

In the Solution #3 example above, `f.sidestreamoutq.get()`is reading from the same queue as `g.sidestreamoutq.get()` . 

The implication is that if there are calls to `L(f,...)`, followed by calls to `L(g,...)`, followed by a loop-until-empty of `f.sidestreamoutq.get()`, then that `get` loop will get all results placed there by all the calls whether  to `f` or to `g`. 

### Solution #5: Simple Python wrapper

What do you do if the low level function comes from a library or elsewhere so you can not or must not change it? 

This solution uses the concept of a wrapper. 

The wrapper sets up the queue and attributes, calls the low level function, does what is necessary with the result, and provides the return that the library requires. 

The solution uses the generic concept of a wrapper, but does not use the advanced Python concept of "decorator wrappers."

This solution is not really fundamentally different from placing results into an attribute or queue. 

However, it externalizes the code that would go inside the target function if you could change it. 

The result is a new function that simply wraps the target function: 

```python
#Solution #5: Simple python wrapper
import queue 
from LibraryL import L

# The function we cannot change
def f(fparms=[]):
    return ["f returns",fparms]

# This wrapper is specific to function f.
def wrapped_f(fparms): # wraps f. Useful when f's source code cannot be edited.
    # This function invokes function f and then 
    #  deposits the returned results into both an attribute and a queue.
    #   Queue object attribute naming convention: 
    #         <wrappingfunction_name>.sidestreamoutq
    #   Result object attribute naming convention: 
    #         <wrappingfunction_name>.mrrv
    #
    # For higher performance if fwrap will be called millions of times, 
    #    move the following statementinto a higher level function,
    #    so that the tests are only done once each.
    
    if not hasattr(wrapped_f, "sidestreamoutq"): wrapped_f.sidestreamoutq=queue.Queue()    
    # 
    # Just call f
    ultimate_result=f(fparms)
    # Both leave the result in the attributes of this function and put it to the queue
    
    wrapped_f.mrrv=ultimate_result 
    wrapped_f.sidestreamoutq.put(ultimate_result)
    if False: # The following statements would create and set attributes in the target function.
              # This injection is not considered a good programming practice if not necessary, and here it is not.
        if not hasattr(f, "sidestreamoutq"): f.sidestreamoutq=wrapped_f.sidestreamoutq # Same Queue. Only set it if it does not exist 
        f.mrrv=ultimate_result 
        # endif if False
    result_to_return=42
    return result_to_return
    
def test_wrapped_f():
    print(["object f: ", f ])
    print(["use f directly:", f("use f directly:")])
    # sidestream f
    print(["wrapped f object: ", wrapped_f])
    print(["use wrapped_f directly:", wrapped_f("use sidestreamed_f directly:")])
    print(["wrapped f Attribute:", wrapped_f.mrrv])
    print(["wrapped f Q entry:", wrapped_f.sidestreamoutq.get()])
    # print(["direct f Attribute:", f.mrrv])
    # print(["direct f Q entry:", f.sidestreamoutq.get()])
    print(["wrapped_f through L returns:", lwfr:=L(wrapped_f,["use L(sidestreamed_f):"])])
    print(["wrapped f Attribute:", wrapped_f.mrrv])
    print(["wrapped f Q entry:", wrapped_f.sidestreamoutq.get()])
    return 
    
test_wrapped_f()
quit()
""" Expected Output, but with different addresses:
['object f: ', <function f at 0x7fbf5f57fd90>]
['use f directly:', ['f returns', 'use f directly:']]
['wrapped f object: ', <function wrapped_f at 0x7fbf5ea36cb0>]
['use wrapped_f directly:', 42]
['wrapped f Attribute:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped f Q entry:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped_f through L returns:', 'int']
['wrapped f Attribute:', ['f returns', ['use L(sidestreamed_f):']]]
['wrapped f Q entry:', ['f returns', ['use L(sidestreamed_f):']]]
"""
```

This solution is similar to Solution #3 Queue, in that there is exactly one queue for the wrapper. 

In order to have usages for one target function yet have results that go to different queues and attributes, you could define additional wrapper functions, such as  `wrapped_f2()`, `wrapped_f3()`, and so on. 

Each would be almost identical to `wrapped_f()`, except for changing all instances of "wrapped_f" to "wrapped_f2", "wrapped_f3", and so on.

### Solution #6: Python decorator wrapper

What do you do if there are very many low level functions, so changing them all would be a tedious maintenance nightmare? 

What do you do if the many low level functions come from libraries or elsewhere so you can not or must not change them? 

What do you do if there need to be several result attributes for some functions? For example, a function is called from multiple places in the code or from multiple threads.

This solution also uses the concept of a wrapper, but differently from above.

Solution #5 has the problem of code proliferation. It requires writing an additional function for each independent usage of each low level function.  

At scale, this also becomes an error-prone maintenance nightmare. It could be categorized as, "Easy to learn, but not easy to use at scale."

Instead, this solution generates the wrappers on demand, at run time, from one set of generic wrapper-generator code. It allows multiple queues and attributes without altering the underlying low level function. 

Each use of the generator to create another wrapper takes only one simple line of code, such as `sidestreamed_f2=create_sidestream_wrapper_func(f)`.

The technique used here is called a Python "decorator". I categorize decorators as advanced Python. 

Decorators are explained in two freeCodeCamp articles, one by [Roy Chng](https://www.freecodecamp.org/news/python-decorators-explained/), and one by [Brandon Wallace](https://www.freecodecamp.org/news/python-decorators-explained-with-examples/). Please study the topic through those articles. 

Here we will just use the technique.  It can be categorized as, "Easy to use at scale, but not easy to learn."

Here, the wrapper generator, including the code defining our specific wrapper and creating its queue, is only 8 lines of executable code in `create_sidestream_wrapper_func`, not counting the `print` statements, which you will remove during testing:

```python
#!/bin/python3
#Solution #6: Python decorator wrapper generator

import queue 
from LibraryL import L

# function we cannot change
def f(fparms=[]):
    return ["f returns",fparms]
    
def create_sidestream_wrapper_func(myfunc):
# Usage
# Create the function: sidestreamed_f=create_sidestream_wrapper_func(f)
# fparm=["This", "that", "and the other thing"]
# Use the created function: 
#    direct:  x=sidestreamed_f(fparm)
#  indirect:  x=L(sidestreamed_f,fparm,lparms)

# Every time this is called, it creates a new instance of the wrapped function
    def sidestream_wrapped_func(parms):
        print("I am going to execute: ", myfunc.__name__)
        ultimate_result=myfunc(parms)
        # The queue was created when the wrapper function is created
        sidestream_wrapped_func.sidestreamoutq.put(ultimate_result)
        sidestream_wrapped_func.mrrv=ultimate_result
        return 42  
    sidestream_wrapped_func.sidestreamoutq=queue.Queue()
    print(["sidestream_wrapper_func = ",sidestream_wrapped_func, " ; with queue at = ",id(sidestream_wrapped_func.sidestreamoutq)])
    return sidestream_wrapped_func
    
def test_create_and_use_sidestream_wrapper_func():
    print(["use f directly:", f("use f directly:")])
    # sidestream f
    sidestreamed_f=create_sidestream_wrapper_func(f) #suitable for use whether f is in some library or inline here, either way.
    sidestreamed_f2=create_sidestream_wrapper_func(f) # creates another sidestreamed function with its own result attribute and queue
    print(["defined the sidestreamed f", sidestreamed_f])
    print(["defined the sidestreamed f2", sidestreamed_f2])
    print(["use sidestreamed_f directly:", sidestreamed_f("use sidestreamed_f directly:")])
    print(["use sidestreamed_f2 directly:", sidestreamed_f2("use sidestreamed_f2 directly:")])
    print(["wrapped f Attribute:", sidestreamed_f.mrrv])
    print(["wrapped f2 Attribute:", sidestreamed_f2.mrrv])
    print(["wrapped f Q entry:", sidestreamed_f.sidestreamoutq.get()])
    print(["wrapped f2 Q entry:", sidestreamed_f2.sidestreamoutq.get()])
    
    
test_create_and_use_sidestream_wrapper_func()
quit()

""" output should be something this, except that addresses will be different.
['use f directly:', ['f returns', 'use f directly:']]
['sidestream_wrapper_func = ', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3edd0>, ' ; with queue at = ', 139637920186032]
['sidestream_wrapper_func = ', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3ee60>, ' ; with queue at = ', 139637920175280]
['defined the sidestreamed f', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3edd0>]
['defined the sidestreamed f2', <function create_sidestream_wrapper_func.<locals>.sidestream_wrapped_func at 0x7efffca3ee60>]
I am going to execute:  f
['use sidestreamed_f directly:', 42]
I am going to execute:  f
['use sidestreamed_f2 directly:', 42]
['wrapped f Attribute:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped f2 Attribute:', ['f returns', 'use sidestreamed_f2 directly:']]
['wrapped f Q entry:', ['f returns', 'use sidestreamed_f directly:']]
['wrapped f2 Q entry:', ['f returns', 'use sidestreamed_f2 directly:']]

"""
```

The generator function and the generated functions have a few print statements that you will want to comment out after using and testing the code. 

It is important to notice in the sample output that the addresses of the functions `sidestreamed_f`  and `sidestreamed_f2` and their queue objects are different.

Similarly, the `mrrv` attributes are also at different addresses:

`sidestreamed_f ... at 0x7efffca3edd0>, ' ; with queue at = ', 139637920186032]`

`sidestreamed_f2 ... at 0x7efffca3ee60>, ' ; with queue at = ', 139637920175280]`

This reinforces how these two wrappers are completely separate objects.

### Advice on Selecting Which Solution to Use

This tutorial has shown you several solutions and variations. 

Which one or ones should you use? 

What are the considerations, selection criteria, and implications? 

This section provides a mix of general software engineering principles and the specifics for this article's topic. 

First eliminate the solutions not to use at all. 

Do not use the global variable solution. It is deprecated. 

Until you understand Solution #6: Python decorator wrapper, do not use it. 

If you cannot enhance the code in the low level function, then use a wrapper. 

The wrapper could be based on either Solution #5: Simple python wrapper for each specific function, or Solution #6: Python decorator wrapper to generate the wrapper.

Use the attribute solution everywhere possible. The attribute solution provides a very good general coding practice, called [memoization](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/). 

I suggest adding function-result memoization to your group's Python coding standards for all functions everywhere. 

Maybe use a different attribute naming convention. I use `.mrrv` , which stands for "most recent result value." 

For example, a function `m`  would be something like:

```python
def m():
  result=[1,2,3]
  m.mrrv=result
  return m.mrrv.copy()
```

Then in your code elsewhere use and reuse the memoized result, such as with `print([sum(m())," = sum(",m.mrrv,")"])` which outputs `[6, ' = sum(', [1, 2, 3], ')']`. 

However, be aware of Python's [order of evaluation](https://docs.python.org/3/reference/expressions.html#evaluation-order) and [short circuiting](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) of logic expressions, to make sure that the function is called before trying to use its `mrrv`.

In other words, always set a function attribute to the value being returned, and then return a copy of it, even if you do not have this tutorial's library-bypass problem.

Does one call to a library function invoke the low level function many times and does the high level program needs the result from each one? 

If so, then use a queue based solution rather than or in addition to the attribute solution.

Does your library-bypass problem apply to many lower level functions which need to pass multiple results via one or more queues for each function? 

If you understand Solution #6: Python decorator wrapper, use it. Otherwise, use Solution #4: Queues.

Is it better to use the simplest solution for each need within the project, or as few of these different solutions as possible in the entire project? 

I recommend the as-few-as-possible way. For me, that means using Solution #1: Function attribute and Solution #6: Python decorator wrapper.

### How good are these solutions?

So you might be wondering – do these recommended solutions conform to the guiding principles at the top of this tutorial?

Here are some things to consider:

* Conflicts: we avoided naming conflicts and interference by using a naming convention.
* Optionality: The two recommended solution alternatives, attribute and queue, do not require additional code in the high level function if it does not need the extended results from the lower level function. The queue solutions could crash if the extended results accumulate forever without being drained.
* Coupling: Several solutions eliminated explicit source code coupling with hard coded names and a naming convention. In one solution, the high level caller first defined one or more result destination queues. Then the caller passed an object reference to a queue in the parameters passed through the intermediary to the lower level function.   

## Summary

As you've learned in this tutorial, it is feasible to pass results from a low level function to be picked up by a higher level function or main program. 

This lets you circumvent any intermediaries by using an out-of-band sidestream. 

There are several solutions presented here. Use as few as possible in your project or projects. 

All these solutions used procedural Python. They are also applicable to object oriented Python with classes. 

Use an attribute in the low level function or use a queue. 

Do not use a global variable.

Illustration credits: [Scott's Great Snake Blockading the Confederacy](https://www.loc.gov/resource/g3701s.cw0011000?r=0.019,0.021,0.937,0.585,0). (c) 1861  

