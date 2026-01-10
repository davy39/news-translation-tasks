---
title: Concurrent Programming in Go – Goroutines, Channels, and More Explained with
  Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-21T19:02:59.000Z'
originalURL: https://freecodecamp.org/news/concurrent-programming-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/2-1.png
tags:
- name: concurrency
  slug: concurrency
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: null
seo_desc: "By Rwitesh Bera\nConcurrency refers to a programming language's ability\
  \ to deal with lots of things at once. \nA good way to understand concurrency is\
  \ by imagining multiple cars traveling on two lanes. Sometimes the cars overtake\
  \ each other, and someti..."
---

By Rwitesh Bera

**Concurrency** refers to a programming language's ability to deal with lots of things at once. 

A good way to understand concurrency is by imagining multiple cars traveling on two lanes. Sometimes the cars overtake each other, and sometimes they stop and let others pass by. 

Another good example is when your computer runs multiple background tasks like messaging, downloading movies, running the operating system, and so on – all at once. 


**Parallelism** means doing lots of things simultaneously and independently. It might sound similar to concurrency, but it’s actually quite different. 

Let's understand it better with the same traffic example. In this case, cars travel on their own road without intersecting each other. Each task is isolated from all other tasks. Concurrent tasks can be executed in any given order. 

This is a non-deterministic way to achieve multiple things at once. True parallel events require multiple CPUs.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/1-1.png)
_Illustration showing difference between parallelism and concurrency_

## What is a Goroutine?
A goroutine is an independent function that executes simultaneously in some separate lightweight threads managed by Go. GoLang provides it to support concurrency in Go.

Here's an example of what a goroutine looks like:

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	go helloworld()
	time.Sleep(1 * time.Second)
	goodbye()
}

func helloworld() {
	fmt.Println("Hello World!")
}

func goodbye() {
	fmt.Println("Good Bye!")
}
```

In this example, first, the `main` goroutine starts. Then it invokes the `helloworld()` function, and the `helloworld` goroutine starts. 

After the `helloworld ` goroutine finishes its operation, the `main` goroutine waits for 1 second and invokes the `goodbye()` function. 

If you omit the `time` function in main, then it will exit before the `helloworld()` finishes its execution. 

Let's understand the steps involved here:

1. `main` goroutine starts
2. Invokes `helloworld` and `helloworld` goroutine starts
3. If there is no pause using the sleep method, the `main` will then invoke `goodbye()` and exit before the `helloworld` goroutine finishes its execution.

Without time.Sleep():

```bash
$ go run HelloWorld.go 
Good Bye!
```

After adding time.Sleep(), the `helloworld` goroutine is able to finish its execution before main exits:

```bash
$ go run HelloWorld.go 
Hello World!
Good Bye!
```


### What are WaitGroups?
You can use WaitGroups to wait for multiple goroutines to finish. A WaitGroup blocks the execution of a function until its internal counter becomes 0. 

Let's see a simple code snippet:

```go
package main

import (
	"fmt"
)

func main() {
	go helloworld()
	go goodbye()
}

func helloworld() {
	fmt.Println("Hello World!")
}

func goodbye() {
	fmt.Println("Good Bye!")
}
``` 

Output
```bash
$ go run HelloWorld.go 

$
```

If we run the above program, it doesn't print anything. This is because the main function got terminated as soon as those two goroutines started executing. So, we can use `Sleep` which pauses the execution of the main function. It looks like this:

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	go helloworld()
	go goodbye()
	time.Sleep(2 * time.Second)
}

func helloworld() {
	fmt.Println("Hello World!")
}

func goodbye() {
	fmt.Println("Good Bye!")
}
```

Here's the output:

```bash
$ go run HelloWorld.go 
Good Bye!
Hello World!
```

Here, the `main` function was blocked for 2 seconds and all the goroutines were executed successfully. 

Blocking the method for 2 seconds might not create any problems. But at the production level, where each millisecond is vital, millions of concurrent requests can create a huge problem.

You can solve this problem using **sync.WaitGroup** like this:

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2)
	go helloworld(&wg)
	go goodbye(&wg)
	wg.Wait()
}

func helloworld(wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Println("Hello World!")
}

func goodbye(wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Println("Good Bye!")
}
```
Output
```bash
$ go run HelloWorld.go 
Good Bye!
Hello World!
```

The output is the same as the previous one, but it doesn't block the `main` for 2 seconds.

1. `wg.Add(int)`: This method indicates the number of goroutines to wait. In the above code, I have provided 2 for 2 different goroutines. Hence the internal counter wait becomes 2.
2. `wg.Wait()`: This method blocks the execution of code until the internal counter becomes 0.
3. `wg.Done()`: This will reduce the internal counter value by 1.

**NOTE**: If a WaitGroup is explicitly passed into functions, it should be added by a pointer.

### What are Channels?
In concurrent programming, Go provides channels that you can use for bidirectional communication between goroutines. 

Bidirectional communication means that one goroutine will send a message and the other will read it. Sends and receives are blocking. Code execution will be stopped until the write and read are done successfully. 

Channels are one of the more convenient ways to send and receive notifications.

There are a couple different types of channels:

**Unbuffered channel**: Unbuffered channels require both the sender and receiver to be present to be successful operations. It requires a goroutine to read the data, otherwise, it will lead to deadlock. By default, channels are unbuffered.

**Buffered channel**: Buffered channels have the capacity to store values for future processing. The sender is not blocked until it becomes full and it doesn't necessarily need a reader to complete the synchronization with every operation. 

If a space in the array is available, the sender can send its value to the channel and complete its send operation immediately. 

After its execution, if a receiver comes, the channel will start sending values to the receiver and it will start its operation once it receives the values. As the sender and receiver are operating at different times, this is called `asynchronous communication`. 

Here's an example:

```txt
Syntax to declare a channel
ch := make(chan Type)
```
```txt
Declaration of channels based on directions
1. Bidirectional channel : chan T
2. Send only channel: chan <- T
3. Receive only channel: <- chan T
```

#### How to write and read from a channel
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	msg := make(chan string)
	go greet(msg)
	time.Sleep(2 * time.Second)

	greeting := <-msg

	time.Sleep(2 * time.Second)
	fmt.Println("Greeting received")
	fmt.Println(greeting)
}

func greet(ch chan string) {
	fmt.Println("Greeter waiting to send greeting!")

	ch <- "Hello Rwitesh"

	fmt.Println("Greeter completed")
}
```

```bash
$ go run main.go 
Greeter waiting to send greeting!
Greeter completed
Greeting received
Hello Rwitesh
```

In the above code snippet, `msg := make(chan string)` is declaring a channel of type string. Then I passed the channel in goroutine greet. `ch <-"Hello Rwitesh"` allows us to write the message to `ch`.

The `ch <-"Hello Rwitesh"` blocks the execution of the goroutine, as no one reads its value written in a channel. So in the `main` goroutine `time.Sleep(2 * time.Second)` terminates the execution without waiting for `greet`. 

The second `time.Sleep(2* time.Second)` statement gives us the time to read from the channel. We read from the channel using `<-msg`.

**Closing the channel**: Closing the channel indicates that no more values should be sent on it. We want to show that the work has been completed and there is no need to keep a channel open.

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	msg := make(chan string)
	go greet(msg)

	time.Sleep(2 * time.Second)

	greeting := <-msg

	time.Sleep(2 * time.Second)
	fmt.Println("Greeting received")
	fmt.Println(greeting)

	_, ok := <-msg
	if ok {
		fmt.Println("Channel is open!")
	} else {
		fmt.Println("Channel is closed!")
	}
}

func greet(ch chan string) {
	fmt.Println("Greeter waiting to send greeting!")

	ch <- "Hello Rwitesh"
	close(ch)

	fmt.Println("Greeter completed")
}
```

We close a channel by using `close()` like `close(ch)` on the above code snippet.

```bash
$ go run main.go 
Greeter waiting to send greeting!
Greeter completed
Greeting received
Hello Rwitesh
Channel is closed!
```

## Conclusion

Let's recap what we've learned: concurrency in Go refers to the ability to perform multiple tasks simultaneously, using goroutines and tools like WaitGroups and channels to synchronize and communicate between them. 

Goroutines are lightweight threads of execution used in Go to support concurrency. WaitGroups are used to wait for multiple goroutines to finish. They block the execution of a function until their internal counter becomes 0. 

Channels are a way for goroutines to communicate and can be used to send and receive data between goroutines.

I hope you found this tutorial helpful and informative. If you enjoyed reading it, I encourage you to share it with your friends and followers on social media.

Don't forget to also follow me on [Twitter](https://twitter.com/RwiteshBera) for more updates on coding and tech. Thanks for reading!

