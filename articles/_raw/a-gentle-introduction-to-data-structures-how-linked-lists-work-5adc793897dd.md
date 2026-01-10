---
title: 'A Gentle Introduction to Data Structures: How Linked Lists Work'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-15T20:13:35.000Z'
originalURL: https://freecodecamp.org/news/a-gentle-introduction-to-data-structures-how-linked-lists-work-5adc793897dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a75WWf1cQX8wcKN0nEYMJQ.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Michael Olorunnisola

  Have you ever built a Rube Goldberg Machine? If not, maybe you’ve built an elaborate
  line of dominoes?

  Okay, maybe you weren’t as nerdy of a kid as I was. So be it. For those of you who
  have had the pleasure to do any of the a...'
---

By Michael Olorunnisola

Have you ever built a Rube Goldberg Machine? If not, maybe you’ve built an elaborate line of dominoes?

Okay, maybe you weren’t as nerdy of a kid as I was. So be it. For those of you who have had the pleasure to do any of the above, you’ve already grasped the essence of today’s data structure: linked lists!

![Image](https://cdn-media-1.freecodecamp.org/images/1*RDUZJbkbiibhVmnl5OOOMw.gif)

### **How linked lists work**

The simplest form of linked lists — a _singly linked list —_ is a series of nodes where each individual node contains both a value and a pointer to the next node in the list.

Additions (**Add**) grow the list by adding items to the end of the list.

Removals (**Remove)** will always remove from a given position in the list.

Search (**Contains**) will search the list for a value.

**Example use cases:**

* Storing values in a hash table to prevent collisions (more on this in a few posts)
* Remaking the amazing race!

![Image](https://cdn-media-1.freecodecamp.org/images/0*nYchAJ8wQnhjtMZZ.png)

Let’s keep this article nice and light by working on a tool that the CBS network can use to plan out their next amazing race TV show.

As you go through this, I want you to keep asking yourself: “How are linked lists any different from arrays? How are they similar?”

Let’s get started.

First, you need to create the representation of our linked list:

```
class LinkedList{  constructor(){    this._head = null;    this._tail = null;    this._length = 0;  }
```

```
  size(){    return this._length;  }}
```

To keep track of the starting point and end point of the race, you create the head and tail properties.

Then, to make sure you don’t make the race too long or too short for the season, you create a length property and size method. This way, you can always keep track of exactly how long the race is.

Now that you have a way to store the race list, you should create a way to add to this list. The question is, what are you adding specifically?

Remember, a linked list is a series of nodes where each node has a value and a pointer to the next node in the list. Knowing this, you realize a node is just an object with a value and next property.

Since you’re going to be creating a new node every time you add to the list, you decide to create a constructor that makes it easier to create a new node for every value that’s added to your list.

```
class Node{  constructor(value){    this.value = value;    this.next = null;  }}
```

Having this constructor available lets you create your add method.

```
class Node {  constructor(value) {    this.value = value;    this.next = null;  }}
```

```
class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);         //we create our node    if(!this._head && !this._tail){     //If it's the first node      this._head = node;                //1st node is head & tail      this._tail = node;    }else{    this._tail.next = node;             //add node to the back    this._tail = this._tail.next;       //reset tail to last node    }    this._length++;  }    size() {    return this._length;  }}
```

```
const AmazingRace = new LinkedList();AmazingRace.add("Colombo, Sri Lanka");AmazingRace.add("Lagos, Nigeria");AmazingRace.add("Surat, India");AmazingRace.add("Suzhou, China");
```

Now that you’ve added this method, you will be able to add a bunch of locations to your Amazing Race list. This is how it’ll look. Note that I’ve added some extra white space to make it easier to understand.

```
{ _head:    { value: 'Colombo, Sri Lanka',     next: { value: 'Lagos, Nigeria',              next: { value: 'Surat, India',                     next: { value: 'Suzhou, China',                             next: null                            }                   }           }    },  _tail: { value: 'Suzhou, China', next: null },  _length: 4 }
```

Okay, so now that you’ve created this list and a way to add, you realize that you want some help adding locations to this list because you have Decidophobia (yep, it’s a [thing](https://en.wikipedia.org/wiki/Decidophobia)).

You decide to share it with your co-worker, Kent, asking him to add a few more places. The only problem is, when you give it to him, you don’t tell him which places you’ve already added. Unfortunately, you’ve forgotten, too, after suffering amnesia brought on from decision anxiety.

Of course he could just run _console.log(AmazingRace)_ and read through what the console outputs. But Kent’s a lazy programmer and needs a way to check whether something exists so he can prevent duplicates. With that in mind, you build out a **contains** method to check for existing values.

```
class Node {  constructor(value) {    this.value = value;    this.next = null;  }}class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);             if(!this._head && !this._tail){           this._head = node;                      this._tail = this._head;    }else{    this._tail.next = node;                 this._tail = this._tail.next;           }    this._length++;  }    contains(value){    let node = this._head;    while(node){      if(node.value === value){        return true;      }      node = node.next;    }    return false;  }    size() {    return this._length;  }  }
```

```
const AmazingRace = new LinkedList();AmazingRace.add("Colombo, Sri Lanka");AmazingRace.add("Lagos, Nigeria");AmazingRace.add("Surat, India");AmazingRace.add("Suzhou, China");
```

```
//Kent's check
```

```
AmazingRace.contains('Suzhou, China'); //trueAmazingRace.contains('Hanoi, Vietnam'); //falseAmazingRace.add('Hanoi, Vietnam');AmazingRace.contains('Seattle, Washington'); //falseAmazingRace.add('Seattle, Washington');AmazingRace.contains('North Pole'); // falseAmazingRace.add('North Pole');
```

Awesome, now Kent has a way to check values before adding them, to avoid duplicates.

As an aside, you might be wondering why you didn’t just use the contains method in the add method to prevent duplicate additions? When you’re implementing a linked list — or any data structure, for that matter — you could theoretically add whatever additional functionality you want.

You can even go in and change native methods on existing structures. Try the below out in a REPL:

```
Array.prototype.push = () => { return 'cat';}
```

```
let arr = [];arr.push('eggs'); // returns 'cat';
```

The reason why we don’t do either of these things is because of [agreed-upon standards](http://www.ecma-international.org/ecma-262/7.0/index.html#sec-array.prototype.push). Essentially, developers have an expectation of how certain methods should work.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vEGGi4mAQz9c9H6dkoOmLw.gif)

Since our linked list class isn’t native to JavaScript, we have more freedom in implementing it, but there are still basic expectations of how data structures such as these should function. Linked lists don’t inherently store unique values. But they do have methods like **contains** that allow us to pre-check and maintain uniqueness in our list.

Kent gets back to you with his list of destinations, but some of them are questionable. For example, the North Pole might not be the best Amazing Race destination.

So you decide to build out a method to be able to remove a node. It’s important to remember that once you remove the node, you unlink the list, and will have to re-link what came before and after the removed node.

```
class Node {  constructor(value) {    this.value = value;    this.next = null;  }}class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);             if(!this._head && !this._tail){           this._head = node;                      this._tail = this._head;    }else{    this._tail.next = node;                 this._tail = this._tail.next;           }    this._length++;  }    remove(value) {    if(this.contains(value)){          // see if our value exists      let current = this._head;           // begin at start of list      let previous = this._head;        while(current){                   // check each node          if(current.value === value){            if(this._head === current){   // if it's the head              this._head = this._head.next;  // reset the head              this._length--;              // update the length              return;                      // break out of the loop            }            if(this._tail === current){   // if it's the tail node              this._tail = previous;       // make sure to reset it            }            previous.next = current.next;  // unlink (see img below)            this._length--;            // update the length            return;                    // break out of           }          previous = current;          // look at the next node          current = current.next;      // ^^        }     }    }      contains(value){    let node = this._head;    while(node){      if(node.value === value){        return true;      }      node = node.next;    }    return false;  }    size() {    return this._length;  }  }
```

```
const AmazingRace = new LinkedList();AmazingRace.add("Colombo, Sri Lanka");AmazingRace.add("Lagos, Nigeria");AmazingRace.add("Surat, India");AmazingRace.add("Suzhou, China");AmazingRace.add('Hanoi, Vietnam');AmazingRace.add('Seattle, Washington');AmazingRace.add('North Pole');
```

```
//Kent's check
```

```
AmazingRace.remove('North Pole');
```

There’s a lot of code in that **remove** function up there. Essentially it boils down to the following:

1. if the value exists in the list…
2. iterate over the linked list, keeping track of the previous and current node
3. then, if there’s a match →

4A . if it’s the head

* reset the head to the next node in the list
* update the length
* break out of the loop

4B. if it’s the tail

* reset the tail to the previous node in the list
* unlink the node by resetting the pointers as seen below

![Image](https://cdn-media-1.freecodecamp.org/images/0*pMf-_vYuiuI1u3j5.png)
_[Wikipedia](https://www.google.com/url?sa=i&amp;rct=j&amp;q=&amp;esrc=s&amp;source=images&amp;cd=&amp;cad=rja&amp;uact=8&amp;ved=0ahUKEwjauKOv46rQAhULfiYKHdgFDWYQjhwIBQ&amp;url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FLinked_list&amp;psig=AFQjCNHXY1FhqqxQeG8hKywNnnpfCnVNpw&amp;ust=1479299805807482" rel="noopener" target="_blank" title=")_

4C. If it’s not a match → _continue iterating_

* make the next node current
* make the current node previous

One last thing to note: you may have realized that you didn’t actually delete the node. You just removed the references to it. Well, that’s OK because once all references to an object are removed, the garbage collector helps us remove it from memory. You can read up on the garbage collection [here](http://docstore.mik.ua/orelly/webprog/jscript/ch11_03.htm).

With the remove method now implemented, you can run this little piece of code below to make sure contestants don’t freeze to death, or accidentally bother Santa as he’s prepping for this year’s festivities.

```
AmazingRace.remove('North Pole');
```

You’ve done it! You’ve created a simple implementation of a linked list. And you can grow the list by adding items, and shrink it by removing items — all based on the item’s value.

See if you can add you can expand the linked list to allow you to insert values at the beginning, end, or any point in between.

You have all you need to implement those methods. The names and arguments for these methods should look a little like this:

```
addHead(value) {
```

```
}
```

```
insertAfter(target, value){
```

```
}
```

Feel free to share your implementations in the comments below ?

### **A time complexity analysis on the queue methods**

![Image](https://cdn-media-1.freecodecamp.org/images/1*MIdvIvbjZVo_Tv4tKYsxUw.gif)

Here’s the code again:

```
class LinkedList {   constructor() {    this._head = null;    this._tail = null;    this._length = 0;  }    add(value) {    let node = new Node(value);             if(!this._head && !this._tail){           this._head = node;                      this._tail = this._head;    }else{    this._tail.next = node;                 this._tail = this._tail.next;           }    this._length++;  }    remove(value) {    if(this.contains(value)){                let current = this._head;              let previous = this._head;        while(current){                   if(current.value === value){            if(this._head === current){               this._head = this._head.next;              this._length--;                            return;                                  }            if(this._tail === current){               this._tail = previous;                }            previous.next = current.next;            this._length--;                        return;                              }          previous = current;                    current = current.next;              }     }    }     contains(value){    let node = this._head;    while(node){      if(node.value === value){        return true;      }      node = node.next;    }    return false;  }    size() {    return this._length;  }
```

```
// To Be Implemented
```

```
addHead(value) {
```

```
}
```

```
insertAfter(target, value){
```

```
}
```

**Add** is **O(1):** Since you always know the last item in the list thanks to tail property, you don’t have to iterate over the list.

**Remove** is **O(n):** In the worst case scenario you’re going to have to iterate over the entire list to find the value to be removed. Great part though is the actual removal of the node is O(1) because you’re just resetting pointers.

**Contains** is **O(n):** You have to iterate over the entire list to check if the value exists in your list.

**addHead** is **O(1):** Similar to our add method above, we always know the position of the head, so no iteration necessary.

**insertAfter** is **O(n)**: Similar to our Remove method above, you’ll have to iterate over the entire list to find the target node that your value should be inserted after. Likewise, the actual insertion is O(1) because you’re just resetting pointers.

### Linked List vs Array?

Why would you use a linked list instead of an arrays? Arrays technically allow you to do all of the things linked lists do, such as additions, insertions, and removals. Also, all these methods are already readily available to us in JavaScript.

Well, the biggest difference comes in the insertions and removals. Since arrays are indexed, when you perform an insertion or removal in the middle of the array, you have to reset the position of all following values to their new indices.

Imagine inserting into the start or middle of an array 100,000 values long! Insertions and removals like this are extremely expensive. Because of this, linked lists are often preferred for large data sets that are often shifted around.

On the other hand, arrays are great when it comes to finding items (random access) since they are indexed. If you know the position of an item, you can access it in O(1) time via _array[position]_.

Linked lists always require you to iterate over the linked lists sequentially. Given this, arrays are usually preferred for either smaller data sets, or data sets that aren’t shifted around as often.

### Time for a quick recap

Linked Lists:

1. have a tail and head property to track the ends of the list
2. have an add, addHead, insertAfter, and remove method to manage the contents of your list
3. have a length property to track how long your linked list is

### Further Reading

There are also the doubly-linked list and circular-linked list data structures. You can read about them [on Wikipedia](https://en.wikipedia.org/wiki/Linked_list#Linked_lists_vs._dynamic_arrays).

Also, here’s a solid, quick [overview](http://www.codingeek.com/data-structure/linked-list-types-explanation/) by Vivek Kumar.

Finally, Ian Elliot wrote a [walk-through](http://www.i-programmer.info/programming/javascript/5328-javascript-data-structures-the-linked-list.html?start=1) that helps you implementing all of the methods. But see if you can implement **addHead()** and **insertAfter()** for your linked list before peeking at this ?

