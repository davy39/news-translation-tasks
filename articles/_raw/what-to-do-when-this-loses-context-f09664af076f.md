---
title: What to do when “this” loses context
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-06T18:38:14.000Z'
originalURL: https://freecodecamp.org/news/what-to-do-when-this-loses-context-f09664af076f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IqZ-dx0QZDVvTBqQBNrOhg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  The best way to avoid this losing context is to not use this at all. However, this
  is not always an option. We may have i...'
---

By Cristian Salcescu

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

The best way to avoid `this` losing context is to not use `this` at all. However, this is not always an option. We may have inherited code that uses `this` or we might work with a library making use of `this`.

Object literals, constructor functions, and `class`es build objects over the prototype system. The `this` pseudo-parameter is used by the prototype system to give functions access to the other object properties.

Let’s take a look at some situations.

### Nested Functions

`this` loses context inside nested functions. [Consider the following code](https://jsfiddle.net/cristi_salcescu/n7zh5gvw/):

```
class Service {
  constructor(){
    this.numbers = [1,2,3];
    this.token = "token";
  }
  
  doSomething(){
    setTimeout(function doAnotherThing(){
      this.numbers.forEach(function log(number){
      //Cannot read property 'forEach' of undefined
          console.log(number);
          console.log(this.token);
      });
    }, 100);
  }
}

let service = new Service();
service.doSomething();
```

The `doSomething()` method has two nested functions: `doAnotherThing()` and `log()`. When `service.doSomething()` is called, `this` loses context in the nested functions.

#### bind()

One way to fix the problem is with `bind()`. [Look at the next code](https://jsfiddle.net/cristi_salcescu/2r4ncoum/):

```
doSomething(){
   setTimeout(function doAnotherThing(){
      this.numbers.forEach(function log(number){
         console.log(number);
         console.log(this.token);
      }.bind(this));
    }.bind(this), 100);
  }
```

`bind()` creates a new version of the function that, when called, has the `this` value already set. Note that we need to use `.bind(this)` for every nested function.

`function doAnotherThing(){ /*…*/}.bind(this)` creates a version of `doAnotherThing()` that takes the `this` value from `doSomething()`.

#### that/self

Another option is to declare and use a new variable `that/self` that stores the value of `this` from the `doSomething()` method.

[See the code below](https://jsfiddle.net/cristi_salcescu/6ajx1hbp/):

```
doSomething(){
   let that = this;
   setTimeout(function doAnotherThing(){
      that.numbers.forEach(function log(number){
         console.log(number);
         console.log(that.token);
      });
    }, 100);
  }
```

We need to declare `let that = this` in all methods using `this` in nested functions.

#### Arrow function

The arrow function offers another way to fix this issue. [Below is the code](https://jsfiddle.net/cristi_salcescu/ejdb19su/):

```
doSomething(){
   setTimeout(() => {
     this.numbers.forEach(number => {
         console.log(number);
         console.log(this.token);
      });
    }, 100);
  }
```

The arrow function does not have its own `this`. It takes the `this` value from its parent. The only problem with this fix is that we tend to lose the function name. The function name is important, as it improves readability by expressing the function intention.

[Below is the same code](https://jsfiddle.net/cristi_salcescu/by096fza/), with functions inferring the variable name:

```
doSomething(){    
   let log = number => {
     console.log(number);
     console.log(this.token);
   }
    
   let doAnotherThing = () => {
     this.numbers.forEach(log);
   }
    
   setTimeout(doAnotherThing, 100);
}
```

Method as callback

`this` loses context when the method is used as a callback.

[Consider the next class](https://jsfiddle.net/cristi_salcescu/f3t2vmex/):

```
class Service {
  constructor(){
    this.token = "token"; 
  }
  
  doSomething(){
    console.log(this.token);//undefined
  } 
}
let service = new Service();
```

Now, let’s look at some situations where the method `service.doSomething()` is used as a callback.

```
//callback on DOM event
$("#btn").click(service.doSomething);

//callback for timer
setTimeout(service.doSomething, 0);

//callback for custom function
run(service.doSomething);

function run(fn){
  fn();
}
```

In all previous situations `this` loses context.

#### bind()

We can use `bind()` to fix the problem. [Check out the next code snippet](https://jsfiddle.net/cristi_salcescu/1904jbh8/):

```
//callback on DOM event
$("#btn").click(service.doSomething.bind(service));

//callback for timer
setTimeout(service.doSomething.bind(service), 0);

//callback for custom function
run(service.doSomething.bind(service));
```

#### Arrow function

Another option is to create a new function that calls `service.doSomething()` .

```
//callback on DOM event
$("#btn").click(() => service.doSomething());

//callback for timer
setTimeout(() => service.doSomething(), 0);

//callback for custom function
run(() => service.doSomething());
```

### React Components

In React components, `this` loses context when methods are used as callbacks for UI events.

[Consider the following component](https://jsfiddle.net/cristi_salcescu/q59zjx1p/):

```
class TodoAddForm extends React.Component {
  constructor(){
      super();
      this.todos = [];
  }
  
  componentWillMount() {
    this.setState({desc: ""});
  }
  
  add(){
    let todo = {desc: this.state.desc}; 
    //Cannot read property 'state' of undefined
    this.todos.push(todo);
  }
  
  handleChange(event) {
     //Cannot read property 'setState' of undefined
     this.setState({desc: event.target.value});
  }
  
  render() {
    return <form>
      <input onChange={this.handleChange} value={this.state.desc} type="text"/>
      <button onClick={this.add} type="button">Save</button>
    </form>;
  }
}

ReactDOM.render(
  <TodoAddForm />,
  document.getElementById('root'));
```

A way to fix the problem is to create new functions in the constructor using `bind(this)`.

```
constructor(){
   super();
   this.todos = [];
   this.handleChange = this.handleChange.bind(this);
   this.add = this.add.bind(this);
}
```

### Not using “`this"`

No `this`, no problems with losing context. Objects can be created using factory functions. [Check out this code](https://jsfiddle.net/cristi_salcescu/xvsk6twc/):

```
function Service() {  
  let numbers = [1,2,3];
  let token = "token";
  
  function doSomething(){
   setTimeout(function doAnotherThing(){
     numbers.forEach(function log(number){
        console.log(number);
        console.log(token);
      });
    }, 100);
  }
  
  return Object.freeze({
    doSomething
  });
}
```

This time the context is not lost when the method is used as a callback.

```

let service = Service();
service.doSomething();

//callback on DOM event
$("#btn").click(service.doSomething);

//callback for timer
setTimeout(service.doSomething, 0);

//callback for custom function
run(service.doSomething);
```

### Conclusion

`this` can lose context in different situations.

`bind()`, the that/self pattern, and arrow functions are tools at our disposal for solving the context problems.

Factory functions give the option of creating objects without using `this` at all.

[**Discover Functional JavaScript**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) was named one of the [**best new Functional Programming books by BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**For more on applying functional programming techniques in React take a look at** [**Functional React**](https://read.amazon.com/kp/embed?asin=B07S1NLFTS&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_Pko5CbA30383Y)**.**

Learn **functional React**, in a project-based way, with [**Functional Architecture with React and Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[Follow on Twitter](https://twitter.com/cristi_salcescu)

