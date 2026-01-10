---
title: Why You Should Refactor Your Code
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2020-04-03T20:00:25.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-refactor-your-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/refactor-your-react-code.png
tags:
- name: clean code
  slug: clean-code
- name: refactoring
  slug: refactoring
seo_title: null
seo_desc: 'Raise your hand if any of the following sounds familiar: Think about code
  formatting. Get rid of unnecessary <div>''s and <span>''s. Use functional React
  components. Try to avoid arrow function in render. And do not repeat yourself!

  Before I go straigh...'
---

Raise your hand if any of the following sounds familiar: Think about code formatting. Get rid of unnecessary `<div>`'s and `<span>`'s. Use functional React components. Try to avoid arrow function in render. And do not repeat yourself!

Before I go straight to refactoring, I need you to answer one simple question: What does it mean to develop an application? Usually, this means producing a piece of software that meets requirements by implementing certain features. 

And how do we do that? We collect customer requirements, estimate them, and develop features one by one, right? Almost.

## **Do Not Forget About Bugs**

Yes, errors do occur. Depending on the development process, software complexity, technical stack, and many other parameters, the number of bugs may vary. 

A business cannot afford critical issues in production. To minimize problems, you should pay particular attention to the [<ins>QA process</ins>](https://keenethics.com/blog/qa-documentation). But QA theory claims that it is usually impossible to run 100% test coverage of your apps and prepare for all possible scenarios. 

Still, to achieve optimal results, teams spend a lot of time testing software and fixing issues. This is a necessary part of the process that each customer should understand and prioritize.

## **Mind the Technical Debt**

Yet, this coin has a flip side. The longer the development and testing process takes, the more technical debt you incur. 

So, what does "technical debt" mean? Technical debt refers to all the quality-related issues you have in your code. Issues which will require spending additional resources in the future. 

You incur technical debt for a variety of reasons, such as:

1. The business pushes to release new features faster.
2. Testing is insufficient.
3. The requirements are changing rapidly.
4. The developers are inexperienced.

Technical debt should be documented. If you do not leave to-do's in the code, you will most likely forget about the issue. And even if you have time for it in the future, you will not remember to fix it.

## **Understand the Importance of Refactoring**

Usually, you need to spend some time refactoring the existing code in order to solve code quality issues and thus lower technical debt. 

But what is refactoring? It is the process of restructuring the existing code without changing its external behavior. And that is actually something that might be difficult to understand for business people managing the project.

> – Will we get any new features?   
>   
> – No.   
>   
> – Will we at least fix some bugs?   
>   
> – Also no.    
>   
> – What will we get then?   
>   
> – …

Working with technical debt helps to avoid bugs. And to add fixes or changes to the project, we always need to read the old code. 

Therefore, refactoring and maintaining good code quality will help us keep development at a good pace. 

Sometimes a business might not need it. For instance, if you're working on a prototype or [<ins>Proof of Concept</ins>](https://keenethics.com/services-proof), or if there are business priorities that cannot be adjusted, you can do without refactoring. 

But in most cases, cutting out refactoring is not a wise thing to do. You might spend a huge amount of time on refactoring if your developers are perfectionists, but this makes no sense either. 

Therefore, you need to strike a balance. You should not spend more time refactoring than you will save in the future.

## **How to Start Refactoring Your React Code**

### **Think about code formatting**

Some people add trailing commas, and some don't. Some use single quotes, while others use double quotes for a string. 

If you work in a team, maintaining the common code style can be really difficult. And inconsistency in code style can make your code look dirty and hard to read. 

So if you haven’t thought about using code formatting tools before, it’s high time to do so. One of the most popular and easy-to-use React refactoring tools is [<ins>Prettier</ins>](https://prettier.io/). You can just add it to the project and it will take care of formatting for you. 

Prettier has some default style settings, but you can change them according to your preferences by adding a `.prettierrc` file with your formatting rules. 

A good setup of `.prettierrc` may look like this:

```js
{ "printWidth": 120,  "singleQuote": true, “trailingComma”: “none” }
```

You can also automatically reformat the code before committing with [<ins>pre-commit hooks</ins>](https://prettier.io/docs/en/precommit.html).

### **Get rid of unnecessary <div>’s and <span>’s**

When React 16.2 was released in November 2017, a lot of React developers sighed in relief. Prior to that, for a component to return a list of children, it was necessary to wrap the children in an extra element, such as `<div>` or `<span>`. 

But with React 16.2 we received improved support for returning components’ children. Now developers can use so-called fragments. They look like empty JSX tags (`<> … </>`). With the help of fragments, you can pass a list of children to the component without adding extra nodes to the DOM.

### **Think about names**

Don’t be lazy when you're thinking about names for components and variables. Every name should be self-explanatory.

Have you ever seen code snippets like this?

```js
const modifyData = data.map(x => [x.a, x.b]))
```

What does it do? If you cannot understand the purpose of a variable from its name, it is time to rename it! 

This will help you and your team understand the logic more easily. It will also eliminate the time spent making changes to existing components in the future.

### **Don’t Repeat Yourself**

The DRY principle was first formulated in the book _The Pragmatic Programmer_. It states that "every piece of knowledge must have a single, unambiguous, authoritative representation within a system". In other words, you need to put repetitive code blocks into separate reusable components. 

Making your code DRY has a lot of benefits. It can save you a lot of time. If you need to change this code in the future, you will only do that in one place. Also, you will never have to worry that you forgot to make changes in some places. Furthermore, you will keep the components cleaner and increase the readability of code. 

To keep your components DRY and small, you can follow two simple rules:

1. If you use a code block more than two times, it’s time to extract it.
2. If you exceed a predefined number of lines in a component (e.g. 100 lines), there is probably logic that can be extracted. Divide it into smaller components by functionality.

### **Use functional over class components**

With the introduction of Hooks in React 16.8, we received access to React class features in functional components. Hooks solve a bunch of problems frequently encountered by developers over the past few years. 

For example, the `useEffect` hook, as the React docs suggest, allows us to group the component logic into small functions based on what pieces are related (instead of grouping the logic based on life-cycle methods). This helps us to better restructure our logic. 

All in all, refactoring React components with the help of hooks makes the code cleaner and reduces the amount of code you need to write. 

Here is a very basic example: fetching the data after the component has mounted and re-fetching it based on the updated props. 

In a class component, we would write something like this:

```js
class BookList extends React.Component {
  componentDidMount() {
    this.props.fetchBooks(this.props.bookGenre);
  }
  componentDidUpdate(prevProps) {
    if (prevProps.bookGenre !== this.props.booksGenre) {
      this.props.fetchBooks(this.props.bookGenre);
    }
  } 
// ... }
```

With React hooks it will look like this:

```js
const BookList = ({ bookGenre, fetchBooks }) => {
  useEffect(() => {
    fetchBooks(bookGenre);
  }, [bookGenre]);
// ... }
```

The books fetching logic is now gathered in one place. The `useEffect` hook will run after mount each time the props `[bookGenre]` in square brackets change. Much cleaner, isn’t it? 

Also, you can extract similar stateful logic and reuse it in different components by creating your custom hooks. You can read more about custom hooks in the official <ins>[React documentation](https://reactjs.org/docs/hooks-custom.html)</ins>.

### **Try to avoid arrow functions in render**

Have you ever seen code like this?:

```js
render() {    
  return (
    <div>
      <button onClick={() => this.setState({ flag: true })} />
      ...      
    </div>    
  );  
}
```

Sure you have. What is the problem with it? Every time a component is rendered, a new instance of such a function is created. 

It is not a big deal if the component is rendered one or two times. But in other cases, it can really affect performance. So, if you care about performance, declare the function before using it in render:

```js
changeFlag = () => this.setState({ flag: true })
render() {    
  return (      
    <div> 
      <button onClick={this.changeFlag} />        
      ...      
    </div>    
  );  
}
```

### **Make the bundle smaller**

If you are using a third-party library, you should not load the entire thing if it isn't necessary. Sometimes you can stumble upon an import which uses only one method from the library, such as:

```js
import lodash form 'lodash'  
...  
const certainProps = lodash.pick(userObject, ['name', 'email']);  ...
```

Instead, it is better to use the following:

```js
import pick from 'lodash/pick' 
... 
const certainProps = pick(userObject, ['name', 'email']); ...
```

Now you do not load the whole library, just the method you need.

## **To Wrap Up**

Let's review the steps you should take to refactor your React code:

* Think about code formatting
* Get rid of unnecessary `<div>`'s and `<span>`'s
* Think about names
* Don’t Repeat Yourself
* Use functional over class components
* Try to avoid arrow functions in render
* Make the bundle smaller

Yet, ideal refactoring is refactoring that does not occur. As a developer and especially as a tech lead, you should think many steps ahead and try to produce high-quality code. You should also carry out regular code reviews, not only within one team but also between teams.

## Do you have an idea for a React project?

My company KeenEthics is an experienced React [development company](https://keenethics.com/services-web-development). If you are ready to change the game with your software project, feel free to [request an estimate](https://keenethics.com/services-web-development).

You can read more similar articles on my Keen Blog. Allow me to suggest [The Value of User Testing](https://keenethics.com/blog/the-value-of-user-testing) or [Angular vs React: What to Choose for Your App?](https://keenethics.com/blog/angular-vs-react-what-to-choose-for-your-app)

Most importantly, I would like to say "thank you" to Yaryna Korduba and Max Fedas, both outstanding React developers, for coauthoring this article as well as the readers for making it to the end!

