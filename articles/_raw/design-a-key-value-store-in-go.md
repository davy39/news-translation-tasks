---
title: How to Design a Transactional Key-value Store in Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-09T15:29:12.000Z'
originalURL: https://freecodecamp.org/news/design-a-key-value-store-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/key-value-blog-header--5-.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: null
seo_desc: 'By Bhupesh Varshney

  If you want to design an interactive shell that allows access to a transactional
  in-memory key/value store, then you''re in the right place.

  Let''s Go together and design one now.

  Backstory

  System design questions have always intere...'
---

By Bhupesh Varshney

If you want to design an interactive shell that allows access to a transactional in-memory key/value store, then you're in the right place.

Let's Go together and design one now.

## Backstory

System design questions have always interested me because they let you be creative. 

Recently I read [Uduak's](https://meekg33k.dev/) [blog](https://triplebyte.com/blog/the-best-worst-and-most-interesting-moments-from-my-marathon-month-of-technical-interviews/?ref=linews_blog) where he shared his experience doing a 30-day interview marathon, which was pretty exciting. I highly recommend reading it.

Anyway, I got to know about this interesting [system design](https://en.wikipedia.org/wiki/Systems_design) question he was asked during the interview.

## The Challenge

The question is as follows:

_Build an interactive shell that allows access to a "transactional in-memory key/value store"._

**Note**: The question is re-phrased for better understanding. It was given as a "take home" project during the above mentioned author's interview.

The shell should accept the following commands:

<table>
<thead>
<tr>
<th align="center">Command</th>
<th align="center">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><code>SET</code></td>
<td align="left">Sets the given key to the specified value. A key can also be updated.</td>
</tr>
<tr>
<td align="center"><code>GET</code></td>
<td align="left">Prints out the current value of the specified key.</td>
</tr>
<tr>
<td align="center"><code>DELETE</code></td>
<td align="left">Deletes the given key. If the key has not been set, ignore.</td>
</tr>
<tr>
<td align="center"><code>COUNT</code></td>
<td align="left">Returns the number of keys that have been set to the specified value. If no keys have been set to that value, prints 0.</td>
</tr>
<tr>
<td align="center"><code>BEGIN</code></td>
<td align="left">Starts a transaction. These transactions allow you to modify the state of the system and commit or rollback your changes.</td>
</tr>
<tr>
<td align="center"><code>END</code></td>
<td align="left">Ends a transaction. Everything done within the "active" transaction is lost.</td>
</tr>
<tr>
<td align="center"><code>ROLLBACK</code></td>
<td align="left">Throws away changes made within the context of the active transaction. If no transaction is active, prints "No Active Transaction".</td>
</tr>
<tr>
<td align="center"><code>COMMIT</code></td>
<td align="left">Commits the changes made within the context of the active transaction and ends the active transaction.</td>
</tr>
</tbody>
</table>

## We are in the arena ?

Before we begin, we can ask some additional questions like:

**Q1.** _Does the data persist after the interactive shell session ends?_

**Q2.** _Do operations on the data reflect to the global shell?_

**Q3.** _Does COMMITing changes in a nested transaction reflect to grandparents as well?_

Your questions may differ, which is perfect. The more questions you ask the better you understand the problem.

Solving the problem will largely depend on the questions asked, so let's define what we are going to assume while building our key-value store:

1. Data is non-persistent (that is, as soon as the shell session ends, data is lost).
2. Key-values can only be strings (we can implement interfaces for custom data-types, but that is out of scope for this tutorial).

Now let's try to understand the tricky part of our problem.

### Understanding a "Transaction"

A transaction is created with the `BEGIN` command and creates a context for the other operations to happen. For example:

```go
> BEGIN // Creates a new transaction
> SET X 200
> SET Y 14
> GET Y
14

```

This is the current active transaction and all the operations only work inside it.

Until the active transaction is committed using the `COMMIT` command, those operations do not persist. And, the `ROLLBACK` command throws away any changes made by those operations in the context of the active transaction. To be more precise, it deletes all key-value pairs from the map.

For example:

```go
> BEGIN //Creates a new transaction which is currently active
> SET Y 2020
> GET Y
2020
> ROLLBACK //Throws away any changes made
> GET Y
Y not set // Changes made by SET Y have been discarded

```

A transaction can also be nested, that is, have child transactions as well:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/parent-child.png)
_Parent-Child hierarchy in transactions_

The newly spawned transaction inherits the variables from its parent transaction and changes made in the context of a child transaction will reflect in the parent transaction as well.  


For example:

```go
> BEGIN //Creates a new active transaction
> SET X 5
> SET Y 19
> BEGIN //Spawns a new transaction in the context of the previous transaction and now this is currently active
> GET Y
Y = 19 //The new transaction inherits the context of its parent transaction**
> SET Y 23
> COMMIT //Y's new value has been persisted to the key-value store**
> GET Y
Y = 23 // Changes made by SET Y 19 have been discarded**

```

I gave it a shot just after I read the blog. Let's see how we can solve this.

## Let's design

We discussed that transactions may also have child transactions as well, we can use the [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) data-structure to generalize this:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/kv1.png)
_Visualizing our Transaction Stack_

* Every stack element is a **transaction**.
* Top of the stack stores our current "Active" transaction.
* Each transaction element has its own [map](https://en.wikipedia.org/wiki/Hash_table). We will call it "local store" which acts like a local cache – every time we `SET` a variable inside a transaction this store is updated.
* Once the changes are COMMITed inside a transaction the values in this "local" store are written to our global map object.

We will be using a [Linked-list](https://en.wikipedia.org/wiki/Linked_list) implementation of stack. We can also achieve this using dynamic arrays as well, but that's homework for the reader:

```go
package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
)

/*GlobalStore holds the (global) variables*/
var GlobalStore = make(map[string]string)

/*Transaction points to a key:value store*/
type Transaction struct {
	store map[string]string // every transaction has its own local store
	next  *Transaction
}

/*TransactionStack maintains a list of active/suspended transactions */
type TransactionStack struct {
	top  *Transaction
	size int 			// more meta data can be saved like Stack limit etc.
}

```

* Our stack is represented by a structure, `TransactionStack` which only stores a pointer to the `top` of the stack.`size` is a struct variable which can be used to determine the size of our stack i.e to find number of suspended & active transactions (completely optional – you can omit declaring this).
* The `Transaction` struct has a store which we defined earlier as a map and a pointer to the next transaction in memory.
* `GlobalStore` is a map which is shared by all the transactions in the stack. This is how we achieve a parent-child relationship, but more on this later.

Now let's write the push and pop methods for our `TransactionStack`.

```go

/*PushTransaction creates a new active transaction*/
func (ts *TransactionStack) PushTransaction() {
	// Push a new Transaction, this is the current active transaction
	temp := Transaction{store : make(map[string]string)}
	temp.next = ts.top
	ts.top = &temp
	ts.size++
}

/*PopTransaction deletes a transaction from stack*/
func (ts *TransactionStack) PopTransaction() {
	// Pop the Transaction from stack, no longer active
	if ts.top == nil {
		// basically stack underflow
		fmt.Printf("ERROR: No Active Transactions\n")
	} else {
		node := &Transaction{}
		ts.top = ts.top.next
		node.next = nil
		ts.size--
	}
}


```

* With every `BEGIN` operation, a new stack element is pushed into the `TransactionStack` and updates `top` to this value.
* For every `COMMIT` or `END` operation, the active transaction is _popped_ from the stack and the next element of the stack is assigned to `top`. Hence the parent transaction is now our current active transaction.

If you are new to Go, note that `PushTransaction()` and `PopTransaction()` are [methods](https://gobyexample.com/methods) and not functions of receiver type (`*TransactionStack`).

In languages like JavaScript and Python, the receiver method invocation is achieved by the keywords `this` and `self`, respectively. 

However in Go this is not the case. You can name it anything you want. To make it easier to understand we choose `ts` to refer to the transaction stack.

Now we create a `Peek` method to return us the `top` element from the stack:

```go
/*Peek returns the active transaction*/
func (ts *TransactionStack) Peek() *Transaction {
	return ts.top
}

```

Note that we are returning a pointer variable of type `Transaction`.

COMMITing a transaction will involve "copying" all the new and/or updated values from the transaction local store to our `GlobalStore`:

```go
/*Commit write(SET) changes to the store with TranscationStack scope
Also write changes to disk/file, if data needs to persist after the shell closes
*/
func (ts *TransactionStack) Commit() {
	ActiveTransaction := ts.Peek()
	if ActiveTransaction != nil {
		for key, value := range ActiveTransaction.store {
			GlobalStore[key] = value
			if ActiveTransaction.next != nil {
				// update the parent transaction
				ActiveTransaction.next.store[key] = value
			}
		}
	} else {
		fmt.Printf("INFO: Nothing to commit\n")
	}
	// write data to file to make it persist to disk
	// Tip: serialize map data to JSON
}

```

Rolling back a transaction is pretty easy. Just delete all the keys from the map (the local map of a transaction):

```go
/*RollBackTransaction clears all keys SET within a transaction*/
func (ts *TransactionStack) RollBackTransaction() {
	if ts.top == nil {
		fmt.Printf("ERROR: No Active Transaction\n")
	} else {
		for key := range ts.top.store {
			delete(ts.top.store, key)
		}
	}
}

```

And finally, here are the `GET` and `SET` functions:

```go
/*Get value of key from Store*/
func Get(key string, T *TransactionStack) {
	ActiveTransaction := T.Peek()
	if ActiveTransaction == nil {
		if val, ok := GlobalStore[key]; ok {
		    fmt.Printf("%s\n", val)
		} else {
			fmt.Printf("%s not set\n", key)
		}
	} else {
		if val, ok := ActiveTransaction.store[key]; ok {
		    fmt.Printf("%s\n", val)
		} else {
			fmt.Printf("%s not set\n", key)
		}
	}
}

```

While SETing a variable, we also have to consider the case when the user might not run any transactions at all. This means that our stack will be empty, that is, the user is SETing variables in the global shell itself.

```go
> SET F 55
> GET F
55

```

In this case we can directly update our `GlobalStore`:

```go
/*Set key to value */
func Set(key string, value string, T *TransactionStack) {
	// Get key:value store from active transaction
	ActiveTransaction := T.Peek()
	if ActiveTransaction == nil {
		GlobalStore[key] = value
	} else {
		ActiveTransaction.store[key] = value
	}
}

```

Are you still with me? Don't go!

![we are in the endgame now](https://i.imgflip.com/2pep5c.jpg?a444295)

We are pretty much done with our key-value store, so let's write the driver code:

```go

func main(){
	reader := bufio.NewReader(os.Stdin)
	items := &TransactionStack{}
	for {
		fmt.Printf("> ")
		text, _ := reader.ReadString('\n')
		// split the text into operation strings
		operation := strings.Fields(text)
		switch operation[0] {
		case "BEGIN": 		items.PushTransaction()
		case "ROLLBACK": 	items.RollBackTransaction()
		case "COMMIT": 		items.Commit(); items.PopTransaction()
		case "END": 		items.PopTransaction()
		case "SET": 		Set(operation[1], operation[2], items)
		case "GET": 		Get(operation[1], items)
        case "DELETE": 		Delete(operation[1], items)
		case "COUNT": 		Count(operation[1], items)
		case "STOP": 		os.Exit(0)
		default:
			fmt.Printf("ERROR: Unrecognised Operation %s\n", operation[0])
		}
	}
}


```

The `COUNT` and `DELETE` operations are fairly easy to implement if you stuck with me until now. 

I encourage you to do this as homework, but I have provided my implementation below if you get stuck somewhere.

Time for testing ⚔.

![zoe-demo](https://user-images.githubusercontent.com/34342551/92362469-aa2a7700-f10d-11ea-8426-1e8462b66d18.gif)

And let me leave you with [my source code](https://github.com/Bhupesh-V/zoe) - you can give the repo a star if you want to support my work.

If you liked this tutorial, you can read more of my stuff at [my blog](https://bhupesh-v.github.io).

Any doubts, something's wrong, or you have feedback? Connect with me on [Twitter](https://twitter.com/bhupeshimself) or [e-mail](mailto:varshneybhupesh@gmail.com) them to me directly.

Gophers by [MariaLetta/free-gophers-pack](https://github.com/MariaLetta/free-gophers-pack)

Happy Learning ?

