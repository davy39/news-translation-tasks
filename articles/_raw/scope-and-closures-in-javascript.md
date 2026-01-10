---
title: Scope and Closures in JavaScript – Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-01T23:52:27.000Z'
originalURL: https://freecodecamp.org/news/scope-and-closures-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/karine-avetisyan-ipuiM-36tAg-unsplash.jpg
tags:
- name: closure
  slug: closure
- name: JavaScript
  slug: javascript
- name: Scope
  slug: scope
seo_title: null
seo_desc: "By Zach Snoek\nYou may have come across or written code similar to this\
  \ when writing JavaScript:\nfunction sayWord(word) {\n    return () => console.log(word);\n\
  }\n\nconst sayHello = sayWord(\"hello\");\n\nsayHello(); // \"hello\"\n\nThis code\
  \ is interesting for a..."
---

By Zach Snoek

You may have come across or written code similar to this when writing JavaScript:

```javascript
function sayWord(word) {
	return () => console.log(word);
}

const sayHello = sayWord("hello");

sayHello(); // "hello"
```

This code is interesting for a couple of reasons. First, we can access `word` in the function returned from `sayWord`. Second, we have access to `word`’s value when we call `sayHello` – even though we call `sayHello` where we do not otherwise have access to `word`.

In this article, we’ll learn about scope and closures, which enable this behavior.

## Introducing Scope in JavaScript

Scope is the first piece that will help us understand the previous example. A variable’s scope is the part of a program where it is available for use. 

JavaScript variables are lexically scoped, meaning that we can determine a variable’s scope from where it is declared in the source code. (This is not entirely true: `var` variables are not lexically scoped, but we will discuss that shortly.)

Take the following example:

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"
}
```

The `if` statement introduces a block scope by using a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block). We say that `foo` is block-scoped to the `if` statement. This means it can only be accessed from within that block.

If we try to access `foo` outside of the block, we get a `ReferenceError` because it is out of scope:

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"
}

console.log(foo); // Uncaught ReferenceError: foo is not defined
```

Block statements in other forms, such as `for` and `while` loops, will also create a scope for block-scoped variables. For instance, `foo` is scoped within a function body below:

```javascript
function sayFoo() {
	const foo = "foo";
	console.log(foo);
}

sayFoo(); // "foo"

console.log(foo); // Uncaught ReferenceError: foo is not defined
```

## Nested Scopes and Functions

JavaScript allows nested blocks and therefore nested scopes. Nested scopes create a scope tree or scope chain. 

Consider the code below, which nests multiple block statements:

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"

	if (true) {
		const bar = "bar";
		console.log(foo); // "foo"

		if (true) {
			console.log(foo, bar); // "foo bar"
		}
	}
}
```

JavaScript also allows us to nest functions:

```javascript
function foo(bar) {
	function baz() {
		console.log(bar);
	}

	baz();
}

foo("bar"); // "bar"
```

As expected, we can access variables from their direct scope (the scope where they get declared). We can also access variables from their inner scopes (the scopes that nest within their direct scope). That is, we can access variables from the scope they get declared in and from every inner scope.

Before we go further, we should clarify the difference in this behavior between variable declaration types.

## Scope of let, const, and var in JavaScript

We can create variables with the `let`, `const`, and `var` declarations. For `let` and `const`, block scoping works as explained above. However, `var` behaves differently.

### let and const

`let` and `const` create block-scoped variables. When declared within a block, they are only accessible within that block. This behavior was demonstrated in our previous examples:

```javascript
if (true) {
	const foo = "foo";
	console.log(foo); // "foo"
}

console.log(foo); // Uncaught ReferenceError: foo is not defined
```

### var

Variables created with `var` are scoped to their nearest function or the global scope (which we will discuss shortly). They are not block scoped:

```javascript
function foo() {
	if (true) {
		var foo = "foo";
	}
	console.log(foo);
}

foo(); // "foo"
```

`var` can create confusing situations, and this information is only included for completeness. It is best to use `let` and `const` when possible. The rest of this article will pertain only to `let` and `const` variables.

If you’re interested in how `var` behaves in the example above, you should check out [my article on hoisting](https://www.freecodecamp.org/news/what-is-hoisting-in-javascript/).

## Global and Module Scope in JavaScript

In addition to block scopes, variables can be scoped to the global and module scope.

In a web browser, the global scope is at the top level of a script. It is the root of the scope tree that we described earlier, and it contains all other scopes. Thus, creating a variable in the global scope makes it accessible in every scope:

```html
<script>
	const foo = "foo";
</script>
<script>
	console.log(foo); // "foo"
		
	function bar() {
		if (true) {
			console.log(foo);
		}
	}

	bar(); // "foo"
</script>
```

Each module also has its own scope. Variables declared at the module level are only available within that module – they are not global:

```html
<script type="module">
	const foo = "foo";
</script>
<script>
	console.log(foo); // Uncaught ReferenceError: foo is not defined
</script>
```

## Closures in JavaScript

Now that we understand scope, let’s go back to the example that we saw in the introduction:

```javascript
function sayWord(word) {
	return () => console.log(word);
}

const sayHello = sayWord("hello");

sayHello(); // "hello"
```

Recall that there were two interesting points about this example:

1. The returned function from `sayWord` can access the `word` parameter
2. The returned function maintains the value of `word` when `sayHello` is called outside the scope of `word`

The first point can be explained by lexical scope: the returned function can access `word` because it exists in its outer scope.

The second point is because of closures: A closure is a function combined with references to the variables defined outside of it. Closures maintain the variable references, which allow functions to access variables outside of their scope. They “enclose” the function and the variables in its environment.

## Examples of Closures in JavaScript

You have probably encountered and used closures frequently without being aware of it. Let’s explore some more ways to use closures.

### Callbacks

It is common for a callback to reference a variable declared outside of itself. For example:

```javascript
function getCarsByMake(make) {
	return cars.filter(x => x.make === make);
}
```

`make` is available in the callback because of lexical scoping, and the value of `make` is persisted when the anonymous function is called by `filter` because of a closure.

### Storing state

We can use closures to return objects from functions that store state. Consider the following `makePerson` function which returns an object that can store and change a `name`:

```javascript
function makePerson(name) {
	let _name = name;

	return {
		setName: (newName) => (_name = newName),
		getName: () => _name,
	};
}

const me = makePerson("Zach");
console.log(me.getName()); // "Zach"

me.setName("Zach Snoek");
console.log(me.getName()); // "Zach Snoek"
```

This example illustrates how closures do not just freeze the values of variables from a function’s outer scope during creation. Instead, they maintain the references throughout the closure’s lifetime.

### Private methods

If you’re familiar with object-oriented programming, you might have noticed that our previous example closely resembles a class that stores private state and exposes public getter and setter methods. We can extend this object-oriented parallel further by using closures to implement private methods:

```javascript
function makePerson(name) {
	let _name = name;

	function privateSetName(newName) {
		_name = newName;
	}

	return {
		setName: (newName) => privateSetName(newName),
		getName: () => _name,
	};
}
```

`privateSetName` is not directly accessible to consumers and it can access the private state variable `_name` through a closure.

### React event handlers

Lastly, closures are common in React event handlers. The following `Counter` component is modified from the [React docs](https://reactjs.org/docs/hooks-reference.html#functional-updates):

```jsx
function Counter({ initialCount }) {
	const [count, setCount] = React.useState(initialCount);

	return (
		<>
			<button onClick={() => setCount(initialCount)}>Reset</button>
			<button onClick={() => setCount((prevCount) => prevCount - 1)}>
				-
			</button>
			<button onClick={() => setCount((prevCount) => prevCount + 1)}>
				+
			</button>
			<button onClick={() => alert(count)}>Show count</button>
		</>
	);
}

function App() {
	return <Counter initialCount={0} />;
}
```

Closures make it possible for:

* the reset, decrement, and increment button click handlers to access `setCount`
* the reset button to access `initialCount` from `Counter`'s props
* and the “Show count” button to display the `count` state.

Closures are important in other parts of React, such as props and hooks. Discussion about these topics is out of scope for this article. I recommend reading [this post](https://epicreact.dev/how-react-uses-closures-to-avoid-bugs/) from Kent C. Dodds or [this post](https://overreacted.io/making-setinterval-declarative-with-react-hooks/) from Dan Abramov to learn more about the role that closures play in React.

## Conclusion

Scope refers to the part of a program where we can access a variable. JavaScript allows us to nest scopes, and variables declared in outer scopes are accessible from all inner ones. Variables can be globally-, module-, or block-scoped.

A closure is a function enclosed with references to the variables in its outer scope. Closures allow functions to maintain connections with outer variables, even outside the scope of the variables. 

There are many uses of closures, from creating class-like structures that store state and implement private methods to passing callbacks to event handlers.

## Let's connect

If you’re interested in more articles like this, [subscribe to my newsletter](https://mailchi.mp/2df4b6d5458f/signup-page) and connect with me on [LinkedIn](https://www.linkedin.com/in/zach-snoek-5b327b179/) and [Twitter](https://twitter.com/zach_snoek)!

## Acknowledgements

Thanks to [Bryan Smith](https://github.com/bryanrsmith) for providing feedback on drafts of this post.

Cover photo by [Karine Avetisyan](https://unsplash.com/@kar111?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/chain?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

