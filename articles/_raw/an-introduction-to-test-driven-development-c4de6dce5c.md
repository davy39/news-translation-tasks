---
title: An Introduction to Test-Driven Development
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-02-04T16:44:44.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-test-driven-development-c4de6dce5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UILpgckM9QDwSXuy6l1WTg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: TDD (Test-driven development)
  slug: tdd
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: I’ve been programming for five years and, honestly, I have avoided test-driven
  development. I haven’t avoided it because I didn’t think it was important. In fact,
  it seemed very important–but rather because I was too comfortable not doing it.
  That’s ...
---

I’ve been programming for five years and, honestly, I have avoided test-driven development. I haven’t avoided it because I didn’t think it was important. In fact, it seemed very important–but rather because I was too comfortable not doing it. That’s changed.

### What is Testing?

Testing is the process of ensuring a program receives the correct input and generates the correct output and intended side-effects. We define these correct inputs, outputs, and side-effects with *specifications*. You may have seen testing files with the naming convention `filename.spec.js`. The `spec` stands for specification. It is the file where we specify or *assert* what our code should do and then test it to verify it does it.

You have two choices when it comes to testing: manual testing and automated testing.

#### Manual Testing

Manual testing is the process of checking your application or code from the user’s perspective. Opening up the browser or program and navigating around in an attempt to test functionality and find bugs.

#### Automated Testing

Automated testing, on the other hand, is writing code that checks to see if other code works. Contrary to manual testing, the specifications remain constant from test to test. The biggest advantage is being able to test *many* things much faster.

It’s the combination of these two testing techniques that will flush out as many bugs and unintended side-effects as possible, and ensure your program does what you say it will. The focus of this article is on automated testing, and in particular, unit testing.

> There are two main types of automated tests: Unit and End-to-End (E2E). E2E tests test an application as a whole. Unit tests test the smallest pieces of code, or units. What is a unit? Well, we define what a unit is, but in general, it’s a relatively small piece of application functionality.

#### Recap:

1. Testing is verifying our application does what it should.
    
2. There are two types of tests: manual and automated
    
3. Tests *assert* that your program will behave a certain way. Then the test itself proves or disproves that assertion.
    

### Test-Driven Development

Test-driven development is the act of first deciding what you want your program to do (the specifications), formulating a failing test, *then* writing the code to make that test pass. It is most often associated with automated testing. Although you could apply the principals to manual testing as well.

Let’s look at a simple example: Building a wooden table. Traditionally, we would make a table, then once the table is made, test it to make sure it does, well, what a table should do. TDD, on the other hand, would have us first define what the table should do. Then when it isn’t doing those things, add the minimum amount of “table” to make each unit work.

Here an example of TDD for building a wooden table:

```python
I expect the table to be four feet in diameter.

The test fails because I have no table.

I cut a circular piece of wood four feet in diameter.

The test passes.

__________

I expect the table to be three feet high.

The test fails because it is sitting on the ground.

I add one leg in the middle of the table.

The test passes.

__________

I expect the table to hold a 20-pound object.

The test fails because when I place the object on the edge, it makes the table fall over since there is only one leg in the middle.

I move the one leg to the outer edge of the table and add two more legs to create a tripod structure.

The test passes.
```

This would continue on and on until the table is complete.

#### Recap

1. With TDD, test logic precedes application logic.
    

### A Practical Example

Imagine we have a program that manages users and their blog posts. We need a way to keep track of the posts a user writes in our database with more precision. Right now, the user is an object with a name and email property:

```js
user = { 
   name: 'John Smith', 
   email: 'js@somePretendEmail.com' 
}
```

We will track the posts a user creates in the same user object.

```js
user = { 
   name: 'John Smith', 
   email: 'js@someFakeEmailServer.com'
   posts: [Array Of Posts] // <-----
}
```

Each post has a title and content. Instead of storing the entire post with each user, we’d like to store something unique that could be used to reference the post. We first thought we would store the title. But, if the user ever changes the title, or if–although somewhat unlikely–two titles are exactly the same, we’d have some issues referencing that blog post. Instead, we will create a unique ID for each blog post that we will store in the `user`Object.

```js
user = { 
   name: 'John Smith', 
   email: 'js@someFakeEmailServer.com'
   posts: [Array Of Post IDs]
}
```

#### Set up our testing environment

For this example, we will be using Jest. Jest is a testing suite. Often, you’ll need a testing library and a separate assertion library, but Jest is an all-in-one solution.

> An assertion library allows us to make assertions about our code. So in our wooden table example, our assertion is: “I expect the table to hold a 20-pound object.” In other words, I am asserting something about what the table should do.

#### Project setup

1. Create an NPM project: `npm init`.
    
2. Create `id.js` and add it to the project’s root.
    
3. Install Jest: `npm install jest --D`
    
4. Update the package.json `test` script
    

```json
// package.json

{
   ...other package.json stuff
   "scripts": {   
     "test": "jest" // this will run jest with "npm run test"
   }
}
```

That’s it for the project setup! We aren’t going to have any HTML or any styling. We are approaching this purely from a unit-testing standpoint. And, believe it or not, we have enough to run Jest right now.

In the command line, run our test script: `npm run test`.

You should have received an error:

```bash
No tests found
In /****/
  3 files checked.
  testMatch: **/__tests__/**/*.js?(x),**/?(*.)+(spec|test).js?(x) - 0 matches
  testPathIgnorePatterns: /node_modules/ - 3 matches
```

Jest is looking for a file name with some specific characteristics such as a `.spec` or `.test` contained within the file name.

Let’s update `id.js` to be `id.spec.js`.

Run the test again

You should receive another error:

```bash
FAIL  ./id.spec.js
  ● Test suite failed to run
  
Your test suite must contain at least one test.
```

A little bit better, it found the file, but not a test. That makes sense; it’s an empty file.

#### How Do We Write a Test?

Tests are just functions that receive a couple of arguments. We can call our test with either `it()` or `test()`.

> `it()`is an alias of `test()`.

Let’s write a very basic test just to make sure Jest is working.

```js
// id.spec.js

test('Jest is working', () => {
   expect(1).toBe(1);
});
```

Run the test again.

```bash
PASS  ./id.spec.js
  ✓ Jest is working (3ms)
  
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        1.254s
Ran all test suites.
```

We passed our first test! Let’s analyze the test and results output.

We pass a title or description as the first argument.

`test('Jest is Working')`

The second argument we pass is a function where we actually assert something about our code. Although, in this case, we aren’t asserting something about our code, but rather something truthy in general that will pass, a sort of sanity check.

`...() => { expect(1).toBe(1)` });

This assertion is mathematically true, so it’s a simple test to ensure we’ve wired up Jest correctly.

The results tell us whether the test passes or fails. It also tells us the number of tests and test suites.

#### A side note about organizing our tests

There is another way we could organize our code. We could wrap each test in a `describe` function.

```js
describe('First group of tests', () => {
   test('Jest is working', () => {
      expect(1).toBe(1);
   });
});

describe('Another group of tests', () => {
   // ...more tests here
});
```

`describe()` allows us to divide up our tests into sections:

```bash
PASS  ./id.spec.js
  First group of tests
    ✓ Jest is working(4ms)
    ✓ Some other test (1ms)
  Another group of tests
    ✓ And another test
    ✓ One more test (12ms)
    ✓ And yes, one more test
```

We won’t use `describe`, but *it is* more common than not to see a `describe` function that wraps tests. Or even a couple of `describes`–maybe one for each file we are testing. For our purposes, we will just focus on `test` and keep the files fairly simple.

#### Testing Based on Specifications

As tempting as it is to just sit down and start typing application logic, a well-formulated plan will make development easier. We need to define what our program will do. We define these goals with specifications.

Our high-level specification for this project is to create a unique ID, although we should break that down into smaller units that we will test. For our small project we will use the following specifications:

1. Create a random number
    
2. The number is an integer.
    
3. The number created is within a specified range.
    
4. The number is unique.
    

#### Recap

1. Jest is a testing suite and has a built-in assertion library.
    
2. A test is just a function whose arguments define the test.
    
3. Specifications define what our code should do and are ultimately what we test.
    

### Specification 1: Create a Random Number

JavaScript has a built-in function to create random numbers–`Math.random()`. Our first unit test will look to see that a random number was created and returned. What we want to do is use `math.random()` to create a number and then ensure that is the number that gets returned.

So you might think we would do something like the following:

`expect(our-functions-output).toBe(some-expected-value)`. The problem with our return value being random, is we have no way to know what to expect. We need to re-assign the `Math.random()` function to some constant value. This way, when our function runs, Jest replaces `Math.random()`with something constant. This process is called *mocking.* So, what we are really testing for is that `Math.random()`gets called and returns some expected value that we can plan for.

Now, Jest also provides a way to prove a function is called. However, in our example, that assertion alone only assures us `Math.random()`was called somewhere in our code. It won’t tell us that the result of `Math.random()`was also the return value.

> Why would you want to mock a function? Isn’t the point to test the real code? Yes and no. Many functions contain things we cannot control, for example an HTTP request. We aren’t trying to test this code. We assume those dependencies will do what they are supposed or make pretend functions that simulate their behavior. And, in the event those are dependencies we’ve written, we will likely write separate tests for them.

Add the following test to `id.spec.js`

```js
test('returns a random number', () => {
   const mockMath = Object.create(global.Math);
   mockMath.random = jest.fn(() => 0.75);
   global.Math = mockMath;
   const id = getNewId();
   expect(id).toBe(0.75);
});
```

#### Breaking the above test down

First, we copy the global Math object. Then we change the `random` method to return a constant value, something we can *expect*. Finally, we replace the global `Math` object with our mocked `Math` object.

We should get an ID back from a function (that we haven't created yet–remember this TDD). Then, we expect that ID to equal 0.75–our mocked return value.

> Notice I’ve chosen to use a built-in method that Jest provides for mocking functions: `jest.fn()`. We could have also passed in a anonymous function instead. However, I wanted to show you this method, since there will be times that a Jest-mocked function will be required for other functionality in our tests to work .

Run the test: `npm run test`

```bash
FAIL  ./id.spec.js
✕ returns a random number (4ms)
● returns a random number
   ReferenceError: getNewId is not defined
```

Notice we get a reference error just like we should. Our test can’t find our `getNewId()`.

Add the following code above the test.

```js
function getNewId() {
   Math.random()
}
```

> I am keeping the code and testing in the same file for simplicity. Normally, the test would be written in a separate file, with any dependencies imported as they are needed.

```bash
FAIL  ./id.spec.js
   ✕ returns a random number (4ms)
   ● returns a random number
   
   expect(received).toBe(expected) // Object.is equality
   Expected: 0.75
   Received: undefined
```

We failed again with what is called an *assertion error*. Our first error was a reference error. This second error tells us it received `undefined`. But we called `Math.random()`so what happened? Remember, functions that don’t explicitly return something will implicitly return `undefined`. This error is a good hint that something wasn’t defined such as a variable, or, like in our case, our function isn’t returning anything.

Update the code to the following:

```js
function getNewId() {
   return Math.random()
}
```

Run the test

```bash
PASS  ./id.spec.js
✓ returns a random number (1ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

Congratulations! We passed our first test.

> Ideally, we want to get to our assertion errors as quickly as possible. Assertion errors–specifically *value assertion errors* like this one, although we will touch on *boolean assertions errors* in a bit–give us hints to what is wrong.

### Specification 2: The number we return is an integer.

`Math.random()` generates a number between 0 and 1 (not inclusive). The code we have will never generate such an integer. That’s ok though, this is TDD. We will check for an integer and then write the logic to transform our number to an integer.

So, how do we check if a number is an integer? We have a few options. Recall, we mocked `Math.random()` above, and we are returning a constant value. In fact, we are creating a real value as well since we are returning a number between 0 and 1 (not inclusive). If we were returning a string, for example, we couldn’t get this test to pass. Or if on the other hand, we were returning an integer for our mocked value, the test would always (falsely) pass.

So a key takeaway is if you going to use mocked return values, they should be realistic so our tests return meaningful information with those values.

Another option would be to use the `Number.isInteger()`, passing our ID as the argument and seeing if that returns true.

Finally, without using the mocked values, we could compare the ID we get back with its integer version.

Let’s look at option 2 and 3.

**Option 2: Using Number.isInteger()**

```js
test('returns an integer', () => {
   const id = getRandomId();
   expect(Number.isInteger(id)).toBe(true);
});
```

The test fails as it should.

```bash
FAIL  ./id.spec.js
✓ returns a random number (1ms)
✕ returns an integer (3ms)

● returns an integer
expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false
```

The test fails with a *boolean assertion error*. Recall, there are multiple ways a test might fail. We want them to fail with assertion errors. In other words, our assertion isn’t what we say it is. But even more so, we want our test to fail with *value assertion errors*.

Boolean assertion errors (true/false errors) don’t give us very much information, but a value assertion error does.

Let’s return to our wooden table example. Now bear with me, the following two statements might seem awkward and difficult to read, but they’re here to highlight a point:

First, you might assert that **the table is blue \[to be\] true**. In another assertion, you might assert **the table color \[to be\] blue**. I know, these are awkward to say and might even look like identical assertions but they're not. Take a look at this:

`expect(table.isBlue).toBe(true)`

vs

`expect(table.color).toBe(blue)`

Assuming the table isn’t blue, the first examples error will tell us it expected true but received false. You have no idea what color the table is. We very well may have forgotten to paint it altogether. The second examples error, however, might tell us it expected blue but received red. The second example is much more informative. It points to the root of the problem much quicker.

Let’s rewrite the test, using option 2, to receive a value assertion error instead.

```js
test('returns an integer', () => {
   const id = getRandomId();
   expect(id).toBe(Math.floor(id));
});
```

We are saying we expect the ID we get from our function to be equal to the floor of that ID. In other words, if we are getting an integer back, then the floor of that integer is equal to the integer itself.

```bash
FAIL  ./id.spec.js
✓ returns a random number (1ms)
✕ returns an integer (4ms)
● returns an integer
expect(received).toBe(expected) // Object.is equality

Expected: 0
Received: 0.75
```

Wow, what are the chances this function just happened to return the mocked value! Well, they are 100% actually. Even though our mocked value seems to be scoped to only the first test, we are actually reassigning the global value. So no matter how nested that re-assignment takes place, we are changing the global `Math` object.

If we want to change something before each test, there is a better place to put it. Jest offers us a `beforeEach()` method. We pass in a function that runs any code we want to run before each of our tests. For example:

```js
beforeEach(() => {
   someVariable = someNewValue;
});

test(...)
```

For our purposes, we won’t use this. But let's change our code a bit so that we reset the global `Math` object back to the default. Go back into the first test and update the code as follows:

```js
test('returns a random number', () => {
   const originalMath = Object.create(global.Math);
   const mockMath = Object.create(global.Math);
   mockMath.random = () => 0.75;
   global.Math = mockMath;
   const id = getNewId();
   expect(id).toBe(0.75);
   global.Math = originalMath;
});
```

What we do here is save the default `Math` object before we overwrite any of it, then reassign it after our test is complete.

Let’s run our tests again, specifically focusing back on our second test.

```bash
✓ returns a random number (1ms)
✕ returns an integer (3ms)
● returns an integer
expect(received).toBe(expected) // Object.is equality

Expected: 0
Received: 0.9080890805713182
```

Since we’ve updated our first test to go back to the default `Math` object, we are truly getting a random number now. And just like the test before, we are expecting to receive an integer, or in other words, the floor of the number generated.

Update our application logic.

```js
function getRandomId() {
   return Math.floor(Math.random()); // convert to integer
}

FAIL  ./id.spec.js
✕ returns a random number (5ms)
✓ returns an integer
● returns a random number
expect(received).toBe(expected) // Object.is equality
Expected: 0.75
Received: 0
```

Uh oh, our first test failed. So what happened?

Well, because we are mocking our return value. Our first test returns 0.75, no matter what. We expect, however, to get 0 (the floor of 0.75). Maybe it would be better to check if `Math.random()` gets called. Although, that is somewhat meaningless, because we could call `Math.random()`anywhere in our code, never use it, and the test still passes. Maybe, we should test whether our function returns a number. After all, our ID must be a number. Yet again, we are already testing if we are receiving an integer. And all integers are numbers; that test would be redundant. But there is one more test we could try.

When it is all said and done, we expect to get an integer back. We know we will use `Math.floor()` to do so. So maybe we can check if `Math.floor()` gets called with `Math.random()` as an argument.

```js
test('returns a random number', () => {
   jest.spyOn(Math, 'floor'); // <--------------------changed
   const mockMath = Object.create(global.Math); 
   const globalMath = Object.create(global.Math);
   mockMath.random = () => 0.75;
   global.Math = mockMath;
   const id = getNewId();
   getNewId(); //<------------------------------------changed
   expect(Math.floor).toHaveBeenCalledWith(0.75); //<-changed
   global.Math = globalMath;
});
```

I’ve commented the lines we changed. First, move your attention towards the end of the snippet. We are asserting that a function was called. Now, go back to the first change: `jest.spyOn()`. In order to watch if a function has been called, jest requires us to either mock that function, or spy on it. We’ve already seen how to mock a function, so here we spy on `Math.floor()`. Finally, the other change we’ve made was to simply call `getNewId()` without assigning its return value to a variable. We are not using the ID, we are simply asserting it calls some function with some argument.

Run our tests

```bash
PASS  ./id.spec.js
✓ returns a random number (1ms)
✓ returns an integer

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
```

Congratulations on a second successful test.

### Specification 3: The number is within a specified range.

We know `Math.random()` returns a random number between 0 and 1 (not inclusive). If the developer wants to return a number between 3 and 10, what could she do?

Here is the answer:

`Math.floor(Math.random() * (max — min + 1))) + min;`

The above code will produce a random number in a range. Let’s look at two examples to show how it works. I’ll simulate two random numbers being created and then apply the remainder of the formula.

**Example:** A number between 3 and 10. Our random numbers will be .001 and .999. I’ve chosen the extreme values as the random numbers so you could see the final result stays within the range.

`0.001 * (10-3+1) + 3 = 3.008` the floor of that is `3`

`0.999 * (10-3+1) + 3 = 10.992` the floor of that is `10`

Let’s write a test

```js
test('generates a number within a specified range', () => {
   const id = getRandomId(10, 100);
   expect(id).toBeLessThanOrEqual(100);
   expect(id).toBeGreaterThanOrEqual(10);
});

FAIL  ./id.spec.js
✓ returns a random number (1ms)
✓ returns an integer (1ms)
✕ generates a number within a specified range (19ms)

● generates a number within a specified range
expect(received).toBeGreaterThanOrEqual(expected)

Expected: 10
Received: 0
```

The floor of `Math.random()` will always be 0 until we update our code. Update the code.

```js
function getRandomId(min, max) {
   return Math.floor(Math.random() * (max - min + 1) + min);
}

FAIL  ./id.spec.js
✕ returns a random number (5ms)
✓ returns an integer (1ms)
✓ generates a number within a specified range (1ms)

● returns a random number

expect(jest.fn()).toHaveBeenCalledWith(expected)

Expected mock function to have been called with:

0.75 as argument 1, but it was called with NaN.
```

Oh no, our first test failed again! What happened?

Simple, our test is asserting that we are calling `Math.floor()` with `0.75`. However, we actually call it with 0.75 plus and minus a max and min value that isn’t yet defined. Here we will re-write the first test to include some of our new knowledge.

```js
test('returns a random number', () => {
   jest.spyOn(Math, 'floor');
   const mockMath = Object.create(global.Math);
   const originalMath = Object.create(global.Math);
   mockMath.random = () => 0.75;
   global.Math = mockMath;
   const id = getNewId(10, 100);
   expect(id).toBe(78);
   global.Math = originalMath;
});

PASS  ./id.spec.js
✓ returns a random number (1ms)
✓ returns an integer
✓ generates a number within a specified range (1ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
```

We’ve made some pretty big changes. We’ve passed some sample numbers into our function (10, and 100 as minimum and maximum values), and we’ve changed our assertion once again to check for a certain return value. We can do this because we know if `Math.random()` gets called, the value is set to 0.75. And, when we apply our min and max calculations to `0.75` we will get the same number each time, which in our case is 78.

Now we have to start wondering if this is even a good test. We’ve had to go back in and mold our test to fit our code. That goes against the spirit of TDD a bit. TDD says to change your code to make the test pass, not to change the test to make the test pass. If you find yourself trying to fix tests so they pass, that may be a sign of a bad test. Yet, I’d like to leave the test in here, as there are a couple of good concepts. However, I urge you to consider the efficacy of a test such as this, as well as a better way to write it, or if it’s even critical to include at all.

Let’s return to our third test which was generating a number within a range.

We see it has passed, but we have a problem. Can you think of it?

The question I am wondering is whether we just get lucky? We only generated a single random number. What are the chances that number just happened to be in the range and pass the test?

Fortunately here, we can mathematically prove our code works. However, for fun (if you can call it fun), we will wrap our code in a `for loop` that runs 100 times.

```js
test('generates a number within a defined range', () => {
   for (let i = 0; i < 100; i ++) {
      const id = getRandomId(10, 100);    
   
      expect(id).toBeLessThanOrEqual(100);
      expect(id).toBeGreaterThanOrEqual(10);
      expect(id).not.toBeLessThan(10);
      expect(id).not.toBeGreaterThan(100);
   }
});
```

I added a few new assertions. I use the `.not` only to demonstrate other Jest API’s available.

```bash
PASS  ./id.spec.js
  ✓ is working (2ms)
  ✓ Math.random() is called within the function (3ms)
  ✓ receives an integer from our function (1ms)
  ✓ generates a number within a defined range (24ms)
  
Test Suites: 1 passed, 1 total
Tests:       4 passed, 4 total
Snapshots:   0 total
Time:        1.806s
```

With 100 iterations, we can feel fairly confident our code keeps our ID within the specified range. You could also purposely try to fail the test for added confirmation. For example, you could change one of the assertions to *not* expect a value greater than 50 but still pass in 100 as the maximum argument.

#### Is it ok to use multiple assertions in one test?

Yes. That isn’t to say you shouldn’t attempt to reduce those multiple assertions to a single assertion that is more robust. For example, we could rewrite our test to be more robust and reduce our assertions to just one.

```js
test('generates a number within a defined range', () => {
   const min = 10;
   const max = 100;
   const range = [];
   for (let i = min; i < max+1; i ++) {
     range.push(i);
   }
   for (let i = 0; i < 100; i ++) {
      const id = getRandomId(min, max);
      expect(range).toContain(id);
   }
});
```

Here, we created an array that contains all the numbers in our range. We then check to see if the ID is in the array.

### Specification 4: The number is unique

How can we check if a number is unique? First, we need to define what unique to us means. Most likely, somewhere in our application, we would have access to all ID’s being used already. Our test should assert that the number that is generated is not in the list of current IDs. There are a few different ways to solve this. We could use the `.not.toContain()` we saw earlier, or we could use something with `index`.

#### **indexOf()**

```js
test('generates a unique number', () => {
   const id = getRandomId();
   const index = currentIds.indexOf(id);
   expect(index).toBe(-1);
});
```

`array.indexOf()` returns the position in the array of the element you pass in. It returns `-1` if the array doesn’t contain the element.

```bash
FAIL  ./id.spec.js
✓ returns a random number (1ms)
✓ returns an integer
✓ generates a number within a defined range (25ms)
✕ generates a unique number (10ms)

● generates a unique number

ReferenceError: currentIds is not defined
```

The test fails with a reference error. `currentIds` is not defined. Let's add an array to simulate some ID’s that might already exist.

```js
const currentIds = [1, 3, 2, 4];
```

Re-run the test.

```bash
PASS  ./id.spec.js
✓ returns a random number (1ms)
✓ returns an integer
✓ generates a number within a defined range (27ms)
✓ generates a unique number

Test Suites: 1 passed, 1 total

Tests:       4 passed, 4 total
```

While the test passes, this should once again raise a red flag. We have absolutely *nothing* that ensures the number is unique. So, what happened?

Again, we are getting lucky. In fact, *your* test may have failed. Although if you ran it over and over, you’d likely get a mix of both with far more passes than failures due to the size of `currentIds`.

One thing we could try is to wrap this in a `for loop`. A large enough `for loop` would likely cause us to fail, although it would be possible they all pass. What we could do is check to see that our `getNewId()` function could somehow be self-aware when a number is or is not unique.

For example. we could set `currentIds = [1, 2, 3, 4, 5]`. Then call `getRandomId(1, 5)` . Our function should realize there is no value it can generate due to the constraints and pass back some sort of error message. We could test for that error message.

```js
test('generates a unique number', () => {
   mockIds = [1, 2, 3, 4, 5];
   let id = getRandomId(1, 5, mockIds);
   expect(id).toBe('failed');
    
   id = getRandomId(1, 6, mockIds);
   expect(id).toBe(6);
});
```

There are a few things to notice. There are two assertions. In the first assertion, we expect our function to fail since we constrain it in a way that it shouldn’t return any number. In the second example, we constrain it in a way where it should only be able to return `6`.

```bash
FAIL  ./id.spec.js
✓ returns a random number (1ms)
✓ returns an integer (1ms)
✓ generates a number within a defined range (24ms)
✕ generates a unique number (6ms)

● generates a unique number

expect(received).toBe(expected) // Object.is equality

Expected: "failed"
Received: 1
```

Our test fails. Since our code isn’t checking for anything or returning `failed`, this is expected. Although, it is possible your code received a 2 through 6.

How can we check if our function *can’t* find a unique number?

First, we need to do some sort of loop that will continue creating numbers until it finds one that’s valid. At some point though, if there are no valid numbers, we need to exit the loop so we avoid an infinite loop situation.

What we will do is keep track of each number we’ve created, and when we’ve created every number we can, and none of those numbers pass our unique check, we will break out of the loop and provide some feedback.

```js
function getNewId(min = 0, max = 100, ids =[]) {
   let id;
   do {
      id = Math.floor(Math.random() * (max - min + 1)) + min;
   } while (ids.indexOf(id) > -1);
   return id;
}
```

First, we refactored `getNewId()` to include a parameter that is a list of current ID’s. In addition, we updated our parameters to provide default values in the event they aren’t specified.

Second, we use a `do-while` loop since we don’t know how many times it will take to create a random number that is unique. For example, we could specify a number from 1 to 1000 with the *only* number unavailable being 7. In other words, our current ID’s only has a single 7 in it. Although our function has 999 other numbers to choose from, it could theoretically produce the number 7 over and over again. While this is very unlikely, we use a `do-while` loop since we are not sure how many times it will run.

Additionally, notice we break out of the loop when our ID *is* unique. We determine this with `indexOf()`.

We still have a problem, with the code currently how it is, if there are no numbers available, the loop will continue to run and we will be in an infinite loop. We need to keep track of all the numbers we create, so we know when we’ve run out of numbers.

```js
function getRandomId(min = 0, max = 0, ids =[]) {
   let id;
   let a = [];
   do {
      id = Math.floor(Math.random() * (max - min + 1)) + min;
      if (a.indexOf(id) === -1) {
         a.push(id);
      }
      if (a.length === max - min + 1) {
         if (ids.indexOf(id) > -1) {
            return 'failed';
         }
      }
   } while (ids.indexOf(id) > -1);
   return id;
}
```

Here is what we did. We solve this problem by creating an array. And every time we create a number, add it to the array (unless it already in there). We know we’ve tried every number at least once when the length of that array is equal to the range we’ve chosen plus one. If we get to that point, we’ve created the last number. However, we still want to make sure the last number we created doesn’t pass the unique test. Because if it does, although we want the loop to be over, we still want to return that number. If not, we return “failed”.

```bash
PASS  ./id.spec.js
✓ returns a random number (1ms)
✓ returns an integer (1ms)
✓ generates a number within a defined range (24ms)
✓ generates a unique number (1ms)

Test Suites: 1 passed, 1 total

Tests:       4 passed, 4 total
```

Congratulations, we can ship our ID generator and make our millions!

### Conclusion

Some of what we did was for demonstration purposes. Testing whether our number was within a specified range is fun, but that formula can be mathematically proven. So a better test might be to make sure the formula is called.

Also, you could get more creative with the random ID generator. For example, if it can’t find a unique number, the function could automatically increase the range by one.

One other thing we saw was how our tests and even specifications might crystalize a bit as we test and refactor. In other words, it would be silly to think nothing will change throughout the process.

Ultimately, test-driven development provides us with a framework to think about our code at a more granular level. It is up to you, the developer, to determine how granular you should define your tests and assertions. Keep in mind, the more tests you have, and the more narrowly focused your tests are, the more tightly coupled they become with your code. This might cause a reluctance to refactor because now you must also update your tests. There is certainly a balance in the number and granularity of your tests. The balance is up to you, the developer, to figure out.

Thanks for reading!

woz
