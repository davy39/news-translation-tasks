---
title: All you need to know on by reference vs by value
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-18T10:59:23.000Z'
originalURL: https://freecodecamp.org/news/understanding-by-reference-vs-by-value-d49139beb1c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KWzeGf9HU8eLhbDiikaobg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Szilard Magyar

  When it comes to software engineering there are quite a few misunderstood concepts
  and misused terms. By reference vs by value is definitely one of them.

  I remember back in the day when I read up on the topic and every source I went...'
---

By Szilard Magyar

When it comes to software engineering there are quite a few misunderstood concepts and misused terms. By reference vs by value is definitely one of them.

I remember back in the day when I read up on the topic and every source I went through seemed to contradict the previous one. It took some time to get a solid grasp of it. I had no choice as it is a fundamental subject if you are a software engineer.

I ran into a nasty bug a few weeks back and decided to write an article so other people may have easier time figuring this whole thing out.

I code in Ruby on a daily basis. I also use JavaScript pretty often, so I have chosen these two languages for this presentation.

To understand all the concepts though we will use some Go and Perl examples as well.

To grasp the whole topic you have to understand 3 different things:

* How the underlying data structures are implemented in the language (objects, primitive types, mutability,).
* How variable assignment/copying/reassignment/comparison work
* How variables are passed to functions

### Underlying data types

In Ruby there are no primitive types and everything is an object including integers and booleans.

And yes there is a `TrueClass` in Ruby.

```
true.is_a?(TrueClass) => true3.is_a?(Integer) => truetrue.is_a?(Object) => true3.is_a?(Object) => trueTrueClass.is_a?(Object) => trueInteger.is_a?(Object) => true
```

These objects can be either mutable or immutable.

Immutable means there is no way you can change the object once it is created. There is just one instance for a given value with one `object_id` and it stays the same no matter what you do.

By default in Ruby the immutable object types are: `Boolean`, `Numeric`, `nil`, and `Symbol`.

> _In MRI the_ `object_id` _of an object is the same as the_ `VALUE` _that represents the object on the C level. For most kinds of objects this_ `VALUE` _is a pointer to a location in memory where the actual object data is stored._

From now on we will use `object_id` and `memory address` interchangeably.

Let’s run some Ruby code in MRI for an immutable Symbol and a mutable String:

```
:symbol.object_id => 808668:symbol.object_id => 808668'string'.object_id => 70137215233780'string'.object_id => 70137215215120
```

As you see while the symbol version keeps the same object_id for the same value, the string values belong to different memory addresses.

Unlike Ruby, JavaScript has primitive types.

They are — `Boolean`, `null`, `undefined`, `String`, and `Number`.

The rest of the data types go under the umbrella of Objects (`Array`, `Function`, and `Object)`. There is nothing fancy here it is way more straightforward than Ruby.

```
[] instanceof Array => true[] instanceof Object => true3 instanceof Object => false
```

### **Variable assignment , copying , reassignment and comparison**

In Ruby every variable is just a reference to an object (since everything is an object).

```
a = 'string'b = a
```

```
# If you reassign a with the same value
```

```
a = 'string'puts b => 'string'puts a == b => true # values are the sameputs a.object_id == b.object_id => false # memory adr-s. differ
```

```
# If you reassign a with another value
```

```
a = 'new string'puts a => 'new string'puts b => 'string'puts a == b => false # values are differentputs a.object_id == b.object_id => false # memory adr-s. differ too
```

When you assign a variable, it is a reference to an object not the object itself. When you copy an object `b = a` both variables will point to the same address.

This behavior is called **copy by reference value**.

**Strictly speaking in Ruby and JavaScript everything is copied by value.**

**When it comes to objects though, the values happen to be the memory addresses of those objects. Thanks to this we can modify values that sit in those memory addresses. Again, this is called copy by reference value but most people refer to this as copy by reference.**

It would be copy by reference if after reassigning `a` to ‘new string’, `b` would also point to the same address and have the same ‘new string’ value.

![Image](https://cdn-media-1.freecodecamp.org/images/EDUJJ3qKxslYQaQU4HGqSfr4CJH5gwgu2e10)
_When you declare **b = a**, **a** and **b** are pointing to the same memory address_

![Image](https://cdn-media-1.freecodecamp.org/images/zmQes155ly7g3T0bqcdTDYvL6EQKvlfOADQV)
_After reassigning **a (a = ‘string’)**, **a** and **b** are pointing to different memory addresses_

The same with an immutable type like Integer:

```
a = 1b = a
```

```
a = 1puts b => 1puts a == b => true # comparison by valueputs a.object_id == b.object_id => true # comparison by memory adr.
```

When you reassign **a** to the same integer, the memory address stays the same since a given integer always has the same object_id.

As you see when you compare any object to another one it is compared by value. If you wanna check out if they are the same object you have to use `object_id.`

Let’s see the JavaScript version:

```
var a = 'string';var b = a;a = 'string'; # a is reassigned to the same value
```

```
console.log(a); => 'string'console.log(b); => 'string'console.log(a === b); => true // comparison by value
```

```
var a = [];var b = a;
```

```
console.log(a === b); => true
```

```
a = [];
```

```
console.log(a); => []console.log(b); => []console.log(a === b); => false // comparison by memory address
```

Except the comparison — JavaScript uses by value for primitive types and by reference for objects. The behavior looks to be the same just like in Ruby.

Well, not quite.

Primitive values in JavaScript will not be shared between multiple variables . Even if you set the variables equal to each other. Every variable representing a primitive value is guaranteed to belong to a unique memory location.

This means none of the variables will ever point to the same memory address. It is also important that the value itself is stored in a physical memory location.

In our example when we declare `b = a`, `b` will point to a different memory address with the same ‘string’ value right away. So you don’t need to reassign `a` to point to a different memory address.

**This is called copied by value** since you have no access to the memory address only to the value.

![Image](https://cdn-media-1.freecodecamp.org/images/-KYjFr8QIDdsGNMvjrsUac-V5KI6soar-ex3)
_When you declare **a = b** it is assigned by value so **a** and **b** point to different memory addresses_

Let’s see a better example where all this matters.

In Ruby if we modify the value that sits in the memory address then all the references that point to the address will have the same updated value:

```
a = 'x'b = a
```

```
a.concat('y')puts a => 'xy'puts b => 'xy'
```

```
b.concat('z')puts a => 'xyz'puts b => 'xyz'
```

```
a = 'z'puts a => 'z'puts b => 'xyz'
```

```
a[0] = 'y'puts a => 'y'puts b => 'xyz'
```

You might think in JavaScript only the value of `a` would change but no. You can’t even change the original value as you don’t have direct access to the memory address.

You could say you assigned ‘x’ to `a` but it was assigned by value so `a`’s memory address holds the value ‘x’, but you can’t change it as you have no reference to it.

```
var a = 'x';var b = a;
```

```
a.concat('y');console.log(a); => 'x'console.log(b); => 'x'
```

```
a[0] = 'z';console.log(a); => 'x';
```

The behavior of JavaScript objects and implementation are the same like Ruby’s mutable objects. Both copy be reference value.

JavaScript primitive types are copied by value. The behavior is the same like Ruby’s immutable objects which are copied by reference value .

Huh?

Again, when you copy something by value it means you can’t change (mutate) the original value since there is no reference to the memory address. From the perspective of the writing code this is the same thing like having immutable entities that you can’t mutate.

If you compare Ruby and JavaScript the only data type that ‘behaves’ differently by default is String (that’s why we used String in the examples above).

In Ruby it is a mutable object and it is copied/passed by reference value while in JavaScript it is a primitive type and copied/passed by value.

When you wanna clone (not copy) an object you have to do it explicitly in both languages so you can make sure the original object won’t be modified:

```
a = { 'name': 'Kate' }b = a.cloneb['name'] = 'Anna'puts a => {:name=>"Kate"}
```

```
var a = { 'name': 'Kate' };var b = {...a}; // with the new ES6 syntaxb['name'] = 'Anna';console.log(a); => {name: "Kate"}
```

It is crucial to remember this otherwise you will run into some nasty bugs when you invoke your code more than once. A good example would be a recursive function where you use the object as argument.

Another one is React (JavaScript front-end framework) where you always have to pass a new object for updating [state](https://facebook.github.io/react/docs/state-and-lifecycle.html) as the comparison works based on object id.

This is faster because you don’t have to go through the object line by line to see if it has been changed.

### How variables are passed to functions

Passing variables to functions is working the same way like copying for the same data types in most of the languages.

In JavaScript primitive types are copied and passed by value and objects are copied and passed by reference value.

I think this is the reason why people only talk about pass by value or pass by reference and never seem to mention copying. I guess they assume copying works the same way.

```
a = 'b'
```

```
def output(string) # passed by reference value  string = 'c' # reassigned so no reference to the original  puts stringend
```

```
output(a) => 'c'puts a => 'b'
```

```
def output2(string) # passed by reference value  string.concat('c') # we change the value that sits in the address  puts stringend
```

```
output(a) => 'bc'puts a => 'bc'
```

Now in JavaScript:

```
var a = 'b';
```

```
function output (string) { // passed by value  string = 'c'; // reassigned to another value  console.log(string);}
```

```
output(a); => 'c'console.log(a); => 'b'
```

```
function output2 (string) { // passed by value  string.concat('c'); // we can't modify it without reference  console.log(string);}
```

```
output2(a); => 'b'console.log(a); => 'b'
```

If you pass an object (not a primitive type like we did) in JavaScript to the function it works the same way like the Ruby example.

### **Other languages**

We have already seen how copy/pass by value and copy/pass by reference value work. Now we will see what pass by reference is about and we also discover how we can change objects if we pass by value.

As I looked for pass by reference languages I couldn’t find too many and I ended up choosing Perl. Let’s see how copying works in Perl:

```
my $x = 'string';my $y = $x;$x = 'new string';
```

```
print "$x"; => 'new string'print "$y"; => 'string'
```

```
my $a = {data => "string"};my $b = $a;$a->{data} = "new string";
```

```
print "$a->{data}\n"; => 'new string'print "$b->{data}\n"; => 'new string'
```

Well this seems to be the same just like in Ruby. I haven’t found any proof but I would say Perl is copied by reference value for String.

Now let’s check what pass by reference means:

```
my $x = 'string';print "$x"; => 'string'
```

```
sub foo {  $_[0] = 'new string';  print "$_[0]"; => 'new string'}
```

```
foo($x);
```

```
print "$x"; => 'new string'
```

Since Perl is **passed by reference if you do a reassignment within the function it will change the original value of the memory address as well.**

For pass by value language I have chosen Go as I intend to deepen my Go knowledge in the foreseeable future:

```
package mainimport "fmt"
```

```
func changeAddress(a *int) {  fmt.Println(a)  *a = 0         // setting the value of the memory address to 0}
```

```
func changeValue(a int) {  fmt.Println(a)  a = 0          // we change the value within the function  fmt.Println(a)}
```

```
func main() {  a := 5  fmt.Println(a)  fmt.Println(&a)  changeValue(a) // a is passed by value  fmt.Println(a)  changeAddress(&a) // memory address of a is passed by value  fmt.Println(a)}
```

```
When you compile and run the code you will get the following:
```

```
0xc42000e32855050xc42000e3280
```

If you wanna change the value of a memory address you have to use pointers and pass around memory addresses by value. A pointer holds the memory address of a value.

The `&` operator generates a pointer to its operand and the `*` operator denotes the pointer’s underlying value. This basically means that you pass the memory address of a value with `&` and you set the value of a memory address with `*`.

### **Conclusion**

How to evaluate a language:

1. Understand the underlying data types in the language. Read some specifications and play around with them. It usually boils down to primitive types and objects. Then check if those objects are mutable or immutable. Some languages use different copying/passing tactics for different data types.
2. Next step is the variable assignment, copying, reassignment and comparison. This is the most crucial part I think. Once you get this you will be able to figure out what’s going on. It helps a lot if you check the memory addresses when playing around.
3. Passing variables to functions usually is not special. It usually works the same way like copying in most languages. Once you you know how the variables are copied and reassigned you already know how they are passed to functions.

The languages we used here:

* **Go**: Copied and passed by value
* **JavaScript**: Primitive types are copied/passed by value, objects are copied/passed by reference value
* **Ruby**: Copied and passed by reference value + mutable/immutable objects
* **Perl**: Copied by reference value and passed by reference

When people say passed by reference they usually mean passed by reference value. **Passing by reference value means that variables are passed around by value but those values are references to the objects**.

As you saw Ruby only uses pass by reference value while JavaScript uses a mixed strategy. Still, the behavior is the same for almost all the data types due to the different implementation of the data structures.

Most of the mainstream languages are either copied and passed by value or copied and passed by reference value. For the last time: Pass by reference value is usually called pass by reference.

In general pass by value is safer as you won’t run into issues since you can’t accidentally change the original value. It is also slower to write because you have to use pointers if you want to change the objects.

It’s the same idea like with static typing vs dynamic typing — development speed at the cost of safety. As you guessed pass by value is usually a feature of lower level languages like C, Java or Go.

Pass by reference or reference value are usually used by higher level languages like JavaScript, Ruby and Python.

When you discover a new language go through the process like we did here and you will understand how it works.

This is not an easy topic and I am not sure everything is correct what I wrote here. If you think I have made some mistakes in this article, please let me know in the comments.

