---
title: Rust Programming Language Tutorial – How to Build a To-Do List App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-04T19:16:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-to-do-app-with-rust
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/rust-mascot.png
tags:
- name: app development
  slug: app-development
- name: Rust
  slug: rust
seo_title: null
seo_desc: 'By Claudio Restifo

  Since its first open-source release in 2015, the Rust programming language has gained
  a lot of attention from the community. It''s also been voted the most loved programming
  language on StackOverflow''s developer survey each year sin...'
---

By Claudio Restifo

Since its first open-source release in 2015, the Rust programming language has gained a lot of attention from the community. It's also been voted the most loved programming language on [StackOverflow](https://insights.stackoverflow.com/survey/2020#technology-most-loved-dreaded-and-wanted-languages)'s developer survey each year since 2016.

Rust was designed by Mozilla and is considered a system programming language (like C or C++). It has no garbage collector, which makes its performance really good. But its design often makes it look and feel very “high-level”.

The learning curve for Rust is considered to be somewhat steep. I am not a master of the language myself, but with this tutorial I'll try to give you a practical approach to some concepts to help you dig in deeper.

## What we will build in this hands-on tutorial

I have decided to follow the long tradition of JavaScript apps and make a to-do app as our first project. We will work with the command line so some familiarity with it is necessary. You'll also need some knowledge of general programming concepts.

This app will run in the terminal. We will store values as a collection of items and a boolean value representing its active state.

## What we will cover here

- Error handling in Rust.
- Options and Null types.
- Structs and impl.
- Terminal I/O.
- File system handling.
- Ownership and borrow in Rust.
- Match patters.
- Iterators and closures.
- Using external crates.

## Before we begin

Some advice before we get started, from someone coming from a JavaScript background:

- Rust is a strongly typed language. This means that we will have to take care of variable types when the compiler isn't able to infer types for us.
- Also as opposed to JavaScript, there's no [AFI](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Automatic_semicolon_insertion). This means that we have to type semicolons (";") ourselves unless it is the last statement of a function. In that case you can omit `;` to have it as a return.

Without farther ado, let's get started.

## How to Get Started with Rust

To get started, download Rust onto your computer. To do so please follow the instructions you find on the [getting started](https://www.rust-lang.org/learn/get-started) page of the official Rust website.

There, you will also find instructions to integrate the language with your favorite editor for a better experience.

Along with the Rust compiler itself, Rust comes with a tool called [Cargo](https://doc.rust-lang.org/cargo/index.html). Cargo is the Rust package manager, and to JavaScript developers it'll feel like npm or yarn.

To start a new project, navigate to where you want your project to be created then simply run `cargo new <project-name>`. In my case I have decided to name my project "todo-cli" so I can run:

```console
$ cargo new todo-cli
```

Now navigate to the newly created directory and list its content. You should see two files in there:

```console
$ tree .
.
├── Cargo.toml
└── src
 └── main.rs
```

We will work on the `src/main.rs` file for the rest of this tutorial, so go ahead and open it.

Like many other languages, Rust has a main function that will be run first. `fn` is how to declare functions while the `!` in `println!` is a [macro](https://doc.rust-lang.org/book/ch19-06-macros.html). As you may guess, this program is the Rust version of "_hello world!_".

To build and run it, simply execute `cargo run`.

```console
$ cargo run
Hello world!
```

## How to Read the Arguments

Our goal is to have our CLI accept two arguments: the first one which will be the action, and the second one which will be the item.

We will start by reading the arguments the user inputs and printing them out.

**Replace** the content of main with the following:

```rust
let action = std::env::args().nth(1).expect("Please specify an action");
let item = std::env::args().nth(2).expect("Please specify an item");

println!("{:?}, {:?}", action, item);
```

Let’s start by digesting all this information.

- `let` [[doc]](https://doc.rust-lang.org/std/keyword.let.html) binds a value to a variable.
- `std::env::args()` [[doc]](https://doc.rust-lang.org/std/env/fn.args.html) is a function brought in from the _env_ module of the standard libray that returns the arguments that the program was started with. Since it's an iterator we can access the value stored at each position with the `nth()` function. The Argument at position 0 is the program itself, which is why we start reading from the 1st element.
- `expect()` [[doc]](https://doc.rust-lang.org/std/option/enum.Option.html#method.expect) is a method defined for the `Option` enum that will either return the value, or if not present will terminate the program immediatly (Panic in Rust terms), returning the provided message.

Because the program can be run without arguments, Rust requires us to check whether a value is actually provided by giving us an Option type: either the value is there, or not.

As the programmer we have the responsibility of ensuring that we take the appropriate action in each case.

For the time being, if the argument is not provided we will exit the program immediately.

Let's run the program and pass two arguments. To do so, append them after `--`. For example:

```console
$ cargo run -- hello world!
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/todo_cli hello 'world'\!''`
"hello", "world!"
```

## How to Insert and Save Data with a Custom Type

Let's think for a moment about our goal for the program. We want to read the argument given by the user, update our todo list, and store it somehwere for usage.

To do so, we will implement our own type where we can define our methods to meets the business needs.

We will use Rust's [struct](https://doc.rust-lang.org/std/keyword.struct.html), which let us do both in a clean way. It avoids having to write all the code inside the main function.

### How to define our struct

Since we will type HashMap a lot in the following steps, we can bring it into scope and save ourselves some typing.

At the top of our file add this line:

```rust
use std::collections::HashMap
```

This will let us use `HashMap` directly without the need to type the full path each time.

Below the main function, let's add the following code:

```rust
struct Todo {
    // use rust built in HashMap to store key - val pairs
    map: HashMap<String, bool>,
}
```

This will define our custom Todo type: a struct with a single field called "map".

This field is a [HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html). You can think of it as a *kind* of JavaScript object, where Rust requires us to declare the types of the key and value.

- `HashMap<String, bool>` means we have keys composed by Strings, and a boolean value: the active state.

### How to add methods to our struct

Methods are like regular functions – they are delcared with the `fn` keyword, they accept parameters, and they have a return value. 

However they differ from regular function in that are defined within the context of a struct and their first parameters is _always_ `self`.

We are gonna define an _impl_ (implementation) block below the newly added struct.

```rust
impl Todo {
    fn insert(&mut self, key: String) {
        // insert a new item into our map.
        // we pass true as value
        self.map.insert(key, true);
    }
}
```

This function is pretty straightforward: it's simply taking a *reference* to the struct and a key, and insterting it into our map using HashMap's built in [insert](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.insert) method.

Two very important piece of information:

- **mut** [[doc]](https://doc.rust-lang.org/std/keyword.mut.html) makes a variable mutable.
In Rust every variable is _immutable_ by default. If you want to update a value, you need to opt-in mutability using the `mut` keyword. Since with our function we are effectively changing our map by adding a new value, we need it to be declared as mutable.

- **&** [[doc]](https://doc.rust-lang.org/std/primitive.reference.html) indicates a _reference_.
You can imagine the varaible as a pointer to the memory location where the value is stored, rather the being the "value" itself.<br/>
In Rust terms this is referred to as a **borrow**, meaning that the function doesn't actually own this value, but it's merely pointing to the location where it's stored.

## A Brief Overview of Rust's Ownership System

With the previous hint about borrow and reference, it's now a good time to briefly talk about ownership.

Ownership is Rust's most unique feature. It enables Rust programmers to write programs without needing to manually allocate memory (like in C/C++) while still being able to run without a Garbage Collector (like in JavaScript or Python) that constantly looks at the program's memory to free resources not in use.

The ownership system has three rules:
* Each value in Rust has a variable: its owner.
* There can only be one owner at a time for each value.
* When the owner goes out of scope, the value will be dropped.

Rust checks this rules at compile time, which means that you have to be explicit if and when you want a value to be freed in memory.
Think of this example:

```rust
fn main() {
 // the owner of the String is x
 let x = String::from("Hello");

 // we move the value inside this function.
 // now doSomething is the owner of x.
 // Rust will free the memory associated with x 
 // as soon as it goes out of "doSomething" scope.
 doSomething(x);

 // The compiler will throw an error since we tried to use the value x
 // but since we moved it inside "doSomething"
 // we cannot use it as we don't have ownership
 // and the value may have been dropped.
 println!("{}", x);
}
```

This concept is widely regarded as the hardest to grasp when learning Rust, as it's a concept that may be new to many programmers. 

You can read a more in-depth explanation about [Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html) from Rust's official docs.

We will not dig too deep into the ins and outs of the ownership system. For now just keep in mind the rules I mentioned above. Try to think, in each step, if we need to "own" the values and then drop them, or if we need a reference of it so it can be kept.

For example in the above insert method, we don't want to own `map`, as we still need it to store its data somewhere. Only then we can finally free the allocated memory.

### How to save the map to disk

Since this is a demo app, we will adopt the simplest possible solution for long term storage: writing the map into a file to disk.

Let's create a new method in our `impl` block.

```rust
impl Todo {
    // [rest of the code]
    fn save(self) -> Result<(), std::io::Error> {
        let mut content = String::new();
        for (k, v) in self.map {
            let record = format!("{}\t{}\n", k, v);
            content.push_str(&record)
        }
        std::fs::write("db.txt", content)
    }
}
```

* `->` annotates the returned type from the function. We are returning a `Result`.
* We iterate over the map, and format each string, separating key and value with a tab character and each line with a new line.
* We push the formatted string into a content variable.
* We write `content` inside a file called `db.txt`.

It's important to notice that `save` *take ownership* of self.
This is an arbitrary decision so that the compiler would stop us if we were to accidentally try to update the map after we called save (as the memory of self would be freed).

This is a personal decision to "enforce" save as the last method to be used. And it's a perfect example to show how you can use Rust's memory management to create stricter code that won't compile (which helps prevent human error during development).

### How to use struct in main

Now that we have these two methods, we can put them to use. We left off main from the point where we read the arguments supplied. Now if the action supplied is "add" we will insert that item into the file and store it for later use.

Add these lines below the two argument bindings:

```rust
fn main() {
    // ...[arguments bindig code]

    let mut todo = Todo {
        map: HashMap::new(),
    };
    if action == "add" {
        todo.insert(item);
        match todo.save() {
            Ok(_) => println!("todo saved"),
            Err(why) => println!("An error occurred: {}", why),
        }
    } 
}
```

Let's see what we are doing here:

* `let mut todo = Todo` let us instantiate a struct, binding it as mutable.
* we call the `TODO insert` method using the `.` notation.
* we [match](https://doc.rust-lang.org/std/keyword.match.html) the Result returned from the save function and print a message on screen for both cases.

Let's test it. Navigate to your terminal and type:

```console
$ cargo run -- add "code rust"
todo saved
```

Let's inspect the saved item:

```console
$ cat db.txt
code rust true
```

You can find a full snippet of the code so far in this [gist](https://gist.github.com/Marmiz/b67e98c2fc7be3561d124294cf3cb6ac).

## How to Read From File

Right now our program has a fundamental flaw: each time we "add" we are overwriting the map instead of updating it. This is because we create a new empty map every time we run the program. Let's fix that.

### Add a new function in TODO

We are gonna implement a new function for our Todo struct. Once called, it will read the content of our file and give us back our Todo populated with the value previously stored. Note that this is not a method as it's not taking `self` as the first argument.

We will call it `new`, which is just a Rust convention (see HashMap::new() as used before).

Let's add the following code inside our impl block:

```rust
impl Todo {
    fn new() -> Result<Todo, std::io::Error> {
        let mut f = std::fs::OpenOptions::new()
            .write(true)
            .create(true)
            .read(true)
            .open("db.txt")?;
        let mut content = String::new();
        f.read_to_string(&mut content)?;
        let map: HashMap<String, bool> = content
            .lines()
            .map(|line| line.splitn(2, '\t').collect::<Vec<&str>>())
            .map(|v| (v[0], v[1]))
            .map(|(k, v)| (String::from(k), bool::from_str(v).unwrap()))
            .collect();
        Ok(Todo { map })
    }

// ...rest of the methods
}
```

No worries if this feels a bit overwhelming. We're using a more functional programming style for this one, mainly to showcase and introduce the fact that Rust supports many paradigms found in other languages such as iterators, closure, and lambda functions.

Let's see what is happening here:

* We are defining a `new` function that will return a Result that is either a `Todo` struct or an `io:Error`.
* We configure how to open the "db.txt" file by defining various [OpenOptions](https://doc.rust-lang.org/std/fs/struct.OpenOptions.html). Most notably is the `create(true)` flag that will create the file if it's not already present.
* `f.read_to_string(&mut content)?` reads all the bytes in the file and appends them into the `content` String.
*note:* remember to add `use std::io::Read;` at the top of the file along with the other use statements in order to use the `read_to_string` method.
* We need to convert from the String type of the file to a HashMap. We do so by binding a map variable with this line: `let map: HashMap<String, bool>`.
This is one of the occasions where the compiler has trouble infering the type for us, so we declare it ourself.
* lines [[doc]](https://doc.rust-lang.org/std/primitive.str.html#method.lines) creates an Iterator over each line of a string, meaning that now we will iterate on each entry of our file, since we formatted it with a `/n` at the end of each entry.
* map [[doc]](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map) takes a closure and calls it on each element of the iterator.
* `line.splitn(2, '\t')` [[doc]](https://doc.rust-lang.org/std/primitive.str.html#method.splitn) will split our lines on the tab character.
* `collect::<Vec<&str>>()`[[doc]](https://doc.rust-lang.org/core/iter/trait.Iterator.html#method.collect) as described in the documentation is one of the most powerful methods in the standard library: it transforms an iterator into a relevant collection.
Here we are telling the map function to transform our Split string into a Vector of borrowed string slices by appending `::Vec<&str>` to the method. This tells the compiler which collection we want at the end of the operation.
* Then we transform it into a tuple for convenience using `.map(|v| (v[0], v[1]))`.
* Then we convert the two elements of the tuple into a String and a boolean using `.map(|(k, v)| (String::from(k), bool::from_str(v).unwrap()))`.
*note:* remember to add `use std::str::FromStr;` at the top of the file along with the other use statement in order to be able to use the `from_str` method.
* We finally collect them into our HashMap. This time we don't need to declare the type as Rust infers it from the binding declaration.
* Lastly if we never encountered any errors we return our struct to the caller with `Ok(Todo { map })`. 
Note here that, much like in JavaScript, we can use a shorter notation if the key and the variable have the same name inside a struct.

*phew!*

![dancing ferris.](https://www.freecodecamp.org/news/content/images/2021/01/dancing-ferris.gif)
_You are doing great! Image credits: https://rustacean.net/_

### An alternative approach
Although map is generally considered more idiomatic, the above could have also been implemented with a `for` loop instead. Feel free to use the one you like the most.

```rust
fn new() -> Result<Todo, std::io::Error> {
    // open the db file
    let mut f = std::fs::OpenOptions::new()
        .write(true)
        .create(true)
        .read(true)
        .open("db.txt")?;
    // read its content into a new string   
    let mut content = String::new();
    f.read_to_string(&mut content)?;
    
    // allocate an empty HashMap
    let mut map = HashMap::new();
    
    // loop over each lines of the file
    for entries in content.lines() {
        // split and bind values
        let mut values = entries.split('\t');
        let key = values.next().expect("No Key");
        let val = values.next().expect("No Value");
        // insert them into HashMap
        map.insert(String::from(key), bool::from_str(val).unwrap());
    }
    // Return Ok
    Ok(Todo { map })
}
```

The code above is functionally equivalent to the more "functional" approach used before.

### How to use the new function

Inside main, simply update the binging to our todo variable with:

```rust
let mut todo = Todo::new().expect("Initialisation of db failed");
```

Now if we go back to the terminal and run a bunch of "add" commands we should see our database correctly updating:

```console
$ cargo run -- add "make coffee"
todo saved
$ cargo run -- add "make pancakes"
todo saved
$ cat db.txt
make coffee     true
make pancakes   true
```

You can find the full code written so far here in this [gist](https://gist.github.com/Marmiz/b659c7835054d25513106e3804c4539f).

## How to Update a Value in the Collection

As in all TODO apps out there, we want to be able to not only add items, but to toggle them as well and mark them as completed.

### How to add the complete method

To do so let's add a new method to our struct called "complete". In it, we take a reference to a key, and update the value, or return `None` if the key is not present.

```rust
impl Todo {
// [Rest of the TODO methods]

  fn complete(&mut self, key: &String) -> Option<()> {
      match self.map.get_mut(key) {
          Some(v) => Some(*v = false),
          None => None,
      }
  }
}
```

Let's see what is happening here:

* We are declaring our function return type: an empty `Option`.
* The whole method returns the result of the Match expression which will be either an empty `Some()` or `None`.
* `self.map.get_mut` [[doc]](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.get_mut) will give us a mutable reference to the value of key, or `None` if the value is not present in the collection.
* We are using the `*` [[doc]](https://doc.rust-lang.org/book/appendix-02-operators.html) operator to de-reference the value and set it to false.

### How to use the complete method

We can use the "complete" method in a similar fashion as we used insert before.

In `main` let's check that the action passed as an argument is "complete" by using an `else if` statement:

```rust
// in the main function

if action == "add" {
    // add action snippet
} else if action == "complete" {
    match todo.complete(&item) {
        None => println!("'{}' is not present in the list", item),
        Some(_) => match todo.save() {
            Ok(_) => println!("todo saved"),
            Err(why) => println!("An error occurred: {}", why),
        },
    }
}
```

Time to analyze what we are doing here:

* We match the Option returned by the `todo.complete(&item)` method.
* If the case is `None` we print a warning to the user for a better experience.
We passed item as a reference with `&item` to the "todo.complete" method so that the value is still owned by this function. This means we can use it for our `println!` macro in the following line.
If we were not to do that, the value would have been owned by "complete" and dropped there.
* If we detect that `Some` value has returned, we call `todo.save` to store the change permanently into our file.

As before, you can find a snapshot of the code written so far in this [gist](https://gist.github.com/Marmiz/1480b31e8e0890e8745e7b6b44a803b8).

## Try Running the Program

It's time to try out the app we've developed locally in our terminal. Let's start by removing our db file to start fresh.

```console
$ rm db.txt
```

Then add and modify some of the todos:
```console
$ cargo run -- add "make coffee"
$ cargo run -- add "code rust"
$ cargo run -- complete "make coffee"
$ cat db.txt
make coffee     false
code rust       true
```
Meaning that at the end of these commands we have one completed action ("make coffee") and a pending one: "code rust".

Let's say we want to make coffee again:

```console
$ cargo run -- add "make coffee
$ cat db.txt
make coffee     true
code rust       true
```

## Bonus: How to Store it as JSON with Serde

The program, even if minimal, is running. But let's give it a bit of a twist. Coming from the JavaScript world I have decided that instead of a plain text file, I want to store my values as a JSON file.

We are gonna take this opportunity to see how to install and use a package from the Rust open source community called [crates.io](https://crates.io/).

### How to install serde

To install a new package into our project, open the `cargo.toml` file. At the bottom you should see a `[dependencies]` field: simply add the following to the file:

```toml
[dependencies]
serde_json = "1.0.60"
```

And that's it. The next time, cargo will compile our program and will also download and include the new package along with our code.

### How to update Todo::New

The first place where we want to use Serde is when we read the db file. Now instead of reading a ".txt", we want to read a JSON file.

Inside the `impl` block let's update the `new` function:

```rust
// inside Todo impl block

fn new() -> Result<Todo, std::io::Error> {
    // open db.json
    let f = std::fs::OpenOptions::new()
        .write(true)
        .create(true)
        .read(true)
        .open("db.json")?;
    // serialize json as HashMap
    match serde_json::from_reader(f) {
        Ok(map) => Ok(Todo { map }),
        Err(e) if e.is_eof() => Ok(Todo {
            map: HashMap::new(),
        }),
        Err(e) => panic!("An error occurred: {}", e),
    }
}
```

The notable changes are:

* No more `mut f` binding for the file option, as we don't need to manually allocate the content into a String as before. Serde will take care of it for us.
* We updated our file extension as `db.json`.
* `serde_json::from_reader` [[doc]](https://docs.serde.rs/serde_json/fn.from_reader.html) will deserialize the file for us. It interferes with the return type of map and will attempt to convert our JSON into a compatible HashMap. If all goes well we return our `Todo` struct as before.
* `Err(e) if e.is_eof()` is a [Match guard](https://doc.rust-lang.org/reference/expressions/match-expr.html#match-guards) that lets us refine the behavior of the Match statement.
If Serde returns as an error a premature EOF (end of file), this means that the file is totally empty (for example on the very first run, or if we deleted the file). In that case we recover from the error and return an empty HashMap.
* For all the other errors, exit the program immediately.

### How to update Todo.save

The other place where we want to use Serde is when we save our map as JSON. To do so, update the `save` method in the impl block to be:

```rust
// inside Todo impl block
fn save(self) -> Result<(), Box<dyn std::error::Error>> {
    // open db.json
    let f = std::fs::OpenOptions::new()
        .write(true)
        .create(true)
        .open("db.json")?;
    // write to file with serde
    serde_json::to_writer_pretty(f, &self.map)?;
    Ok(())
}
```

As before, let's see what we are changing here:

* `Box<dyn std::error::Error>`. This time we return a [Box](https://doc.rust-lang.org/std/boxed/index.html) containing a Rust generic error implementation.
To put it simply, a box is a pointer to an allocation in memory.
Since we may return either a file system error when opening the file, or a Serde error when converting it, we don't really know which of the two our function may return. 
Therefore we return a pointer to the possible error, instead of the error itself so that the caller will handle them.
* We of course have updated the file name to `db.json` to match.
* Finally we let Serde do the heavy lifting and write our HashMap as a JSON file (pretty printed).
* Remember to remove both `use std::io::Read;` and `use std::str::FromStr;` from the top of the file as we do not need them anymore.

And that's it.
Now you can run your program and inspect the output saved to file. If all went well, you now should see your todos saved as JSON.

You can find the full code written so for in this [gist](https://gist.github.com/Marmiz/541c3ccea832a27bfb60d4882450a4a8).

## Closing Thoughts, Tips and Additional Resources

This was quite a long journey, and I am honored you have taken it with me.
I hope you learned something and had your curiosity sparked with this introduction. Don't forget that we worked with a very "low-level" language, yet reviewing the code probably felt very familiar to most.

And that is what personally attracts me to Rust – the fact that it empowers me to write code that is both blazing fast and memory efficient without the fear that comes with such responsability: I know that the compiler will be there for me, stopping my code before it is even possible to run it.

Before finishing up, I would like to share with you some additional tips and resources to help you move forward in your Rust journey:

* [Rust fmt](https://github.com/rust-lang/rustfmt) Is a very handy tool you can run to format your code following a consistent pattern. No more wasting time configuring your favourite linter plugins.
* `cargo check` [[doc]](https://doc.rust-lang.org/cargo/commands/cargo-check.html) will attempt to compile your code without running: this is a very useful command when developing, where you just want to check the correctness of the code without actually running it.
* Rust comes with both an integrated test suite and a tool to generate documentation: [cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) and [cargo doc](https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html). We didn't touch on them this time, as the tutorial seems rather dense as it is. Perhaps in the future.

To learn more about the language, in my opinion the best resources are:

* The official [Rust website](https://www.rust-lang.org/), where all the information is gathered.
* If you like interacting via chat, Rust's [Discord](https://discord.gg/rust-lang) server has a very active and helpful community.
* If you like learning by reading books, "[The Rust programming language](https://doc.rust-lang.org/book/title-page.html)" book is the right choice for you.
* If you are more a video type, Ryan Levick's [introduction to Rust](https://youtu.be/WnWGO-tLtLA) video series is an amazing resource.


You can find the source code of this article hosted on [GitHub](https://github.com/Marmiz/todo-cli).

The cover image comes from [https://rustacean.net/](https://rustacean.net/).

Thanks for reading and Happy Coding!

