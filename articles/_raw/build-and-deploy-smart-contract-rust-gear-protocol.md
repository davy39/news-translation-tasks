---
title: How to Build and Deploy a Smart Contract With Rust and the Gear Protocol
subtitle: ''
author: Rocky Essel
co_authors: []
series: null
date: '2024-06-04T10:36:01.000Z'
originalURL: https://freecodecamp.org/news/build-and-deploy-smart-contract-rust-gear-protocol
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/How-to-Build-and-Deploy-a-Smart-Contract-With-Rust-and-the-Gear-Protocol-Cover.png
tags:
- name: handbook
  slug: handbook
- name: Rust
  slug: rust
- name: Web3
  slug: web3
seo_title: null
seo_desc: "Smart contracts are like digital agreements that run on blockchain technology,\
  \ making transactions automatic and secure. While many people use Ethereum and Solidity\
  \ to create these contracts, there are other options that can be just as powerful.\
  \ \nOne..."
---

Smart contracts are like digital agreements that run on blockchain technology, making transactions automatic and secure. While many people use Ethereum and Solidity to create these contracts, there are other options that can be just as powerful. 

One great combination is using Rust with the Gear Protocol. In this guide, I'll show you how to build and deploy a smart contract using Rust and the Gear Protocol. Whether you're new to this or have some experience, this article will help you get started with clear and easy-to-follow steps.

## Prerequisites

1. Have basic Rust knowledge.
2. Having a basic understanding of decentralization. 

## Table of Contents

1. [Introduction to Vara Network & Gear Protocol.](#heading-introduction-to-vara-network-amp-gear-protocol)
2. [Why Use the Web2 Analogy](#heading-why-use-the-web2-analogy)? 
3. [Message-based Communication](#heading-message-based-communication).
4. [Illustration](#heading-illustration)
5. [Vara Network's Role](#heading-vara-networks-role).
6. [First Project – Reading a Joke](#heading-first-project-reading-a-joke)
7. [Next Project – `input-msg`](#heading-next-project-input-msg)
8. [Metadata & State](#heading-metadata-amp-state)
9. [Third Project – Building Messages](#heading-third-project-building-messages)
10. [Final Project – Battle Showdown](#heading-final-project)
11. [Conclusion.](#conclusion-1)

## Introduction to Vara Network & Gear Protocol.

### Vara Network

Think of Vara as the sturdy foundation of blockchain technology. It's a layer-1 blockchain, meaning that it's at the core of transactions, ensuring that they are secure and decentralized. Vara uses Nominated Proof-of-Stake (NPoS) for agreement, making it reliable and efficient.

Furthermore, Vara Network distinguishes itself through its novel Actor Model, an architecture characterized by isolation and asynchronous messaging. This paradigm shift in smart contract execution imbues Vara Network with unparalleled security and scalability, setting it apart from conventional blockchain platforms.

### Gear Protocol

Gear Protocol is like a toolbox for developers. It's a smart contract engine that makes building decentralized apps (dApps) faster, safer, and cheaper. By using substrate technology and WebAssembly (Wasm), Gear makes it easy for developers to create dApps that run smoothly and securely.

Gear's utilization of the Wasm virtual machine serves as a cornerstone of its efficiency. By harnessing the power of Wasm, developers can transcend language barriers, seamlessly integrating existing codebases and accelerating the development lifecycle. This fusion of familiarity and performance paves the way for a new era of dApp creation, where speed, security, and scalability converge harmoniously.

In simpler terms, Vara Network and Gear Protocol work together to make blockchain technology more user-friendly and secure for building and using decentralized apps.

## Why Use the Web2 Analogy?

Understanding message-based communication, particularly within the context of Gear Protocol, can be quite challenging. To gain a clearer understanding, I delved into the documentation and conducted additional research. Eventually, I stumbled upon an analogy that made it all click: the analogy of web HTTP requests, specifically the POST method.

Let's dissect this analogy step by step. Consider the familiar scenario of a user visiting a website like google.com and interacting with the search bar. When the user enters a search query and hits enter, what's happening behind the scenes is akin to a POST HTTP request being sent.

### Here's how it unfolds:

1. **User Interaction:** The user initiates the action by typing a search query into the search bar and hitting enter. This action triggers a request for information.
2. **Client Acknowledgment:** Google's website, acting as the client-side user interface (UI), acknowledges the user's input and prepares to send a request to the server for processing.
3. **Request Sent:** Just like when you hit enter after typing a query, Google's website sends a POST request to its server, conveying the user's search query.
4. **Server Processing:** Upon receiving the POST request, Google's server processes the query, searching its vast index for relevant information.
5. **Response Generation:** After processing the query, Google's server generates a response containing the search results.
6. **Response Sent:** Finally, Google's server sends the response back to the client (the user's web browser), completing the communication cycle.

In this analogy, the user represents the initiator of the communication, the client (UI) serves as the intermediary between the user and the server, and the server acts as the responder, processing requests and generating responses.

By drawing parallels between message-based communication in Gear Protocol and the familiar concept of web HTTP requests, we can better grasp the dynamics at play. Just as understanding how web requests facilitate communication between users and servers is essential for navigating the internet, comprehending message-based communication in Gear Protocol is crucial for building and interacting with decentralized applications effectively.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-114.png)
_how the POST method works_



## Message-based Communication

Similarly, the Gear Protocol operates based on user or program interactions.  
**Note**: Programs on Gear can also interact with each other.   
So here is a detailed explanation to the whole communication flow in Gear.

### User Interaction and @gear-js/api

When a user (actor) interacts with the dApp's UI elements (like buttons or forms), `_@gear-js/api_` (which is integrated into the UI) captures these interactions. Based on the interactions, it extracts information and potentially pre-defined message formats, and then contracts a message object containing the user's intent or request.

### How to Send Messages

The constructed message object encapsulates the user's input and becomes the data `@gear-js/api` transmits across the Vara Network to the Gear crate within the program.

### How the Program Receives and Processes Messages

Gear (`crate`) delivers the message object to the appropriate program deployed on the Vara Network based on the location the user initiated the action. The Gear crate within the program utilizes functions like `msg::load()` and access the delivered message object, which the program extracts information (such as `payload`, `source`, `messsageId`) from, and process it according to how it's designed by the developer.

### How to Generate a Reply

Based on the processed input, the program creates a new message object containing a reply (`response` in `web2`) to the user's action or interaction (called `reply`) to or for the user. 

Note, the program typically doesn't send the original message object back, it generates a new one based message received, which a reply is sent back to be received by `@gear-js/api` using the `gstd` crate from the program utilizing functions like the `msg::reply` or `msg::reply_bytes`.

### UI Update

`@gear-js/api`, within the dApp, receives the reply message object delivered by the `gstd` crate from the program across the Vara Network and extracts the response data from the reply object, and finally updates the UI reflecting the program's response to the user's interaction.  
  
And that's pretty much the communication between the Users, Client(dApp), Gear Protocol(`gstd`), and finally Vara Network.

## Illustration

Let's discuss more about the diagrams below, and how they each interact with each other.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-1.png)
_UI Update_

This illustration above is just a bird's eye view of how communication flows from the user to the program**.** I'll provide a complete illustration for more clarity. But before that, let's break the overview illustration into three stages.

### Initial Interaction Stage

As said earlier, this is when the user interacts with the program, both `@gear-js/api` and `gstd`.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-124.png)
_Initial Interaction Stage_

### Business/Program Logic

This section depicts the communication between the program and Gear within Vara Network. The `gstd` is used by the program to access the transmitted message (`msg::load()`) from the initial stage to perform business logic.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-126.png)
_Business/Program Logic_

### Reply (Response)

This final stage shows how user feedback is delivered to the user or program. `@gear-js/api` translates it if necessary, and then updates the dApp's UI with the results. This allows the user to see the outcome of their action within the dApp.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-127.png)
_Reply(Response)_

That's great, right? This should help you understand how messages are passed from the client to the program. But what does Vara Network role mean here? Earlier I said that, the message object get transmitted across the Vara Network, but I didn't say how. Let's explain that.

## Vara Network's Role 

In Vara, all participants, including user interfaces (through `@gear-js/api`) and smart contracts (programs & `gstd`), are considered as actors. Another point to know is that, actors don't directly call functions within other actors (as in, programs interacting with other programs or even users). 

Instead, they send messages containing data or instructions. So in our explanation of the message-based communication, Vara serves as the underlying decentralized network infrastructure for communication of our system (dApps). It provides a secure and reliable platform for message transmission across distributed network of nodes. And since Vara utilize a consensus mechanism NPoS (Nominated Proof-of-Stake), it ensures network security and transaction validation.

## Getting Our Hands Dirty

In order to build upon the above information I provided, you and I need to get our hands dirty by building and deploying programs with additional explanation for a clearer understanding. 

Let's get started.

### First Project - Reading a Joke

In this project, you're going to interact with and deploy your smart contract on Vara Network, and receive a reply message back.

This is just a simple project, and nothing too complex. I chose this example project because it aligns with the analogy I gave earlier.

Currently, this project should be fine when running it on your Windows system. In case you get an error, scroll to the part of this article with a guide for setting up a Windows Subsystem for Linux (WSL), since it would allow you to run a Linux environment, including command-line tools and applications, directly on Windows, without the overhead of a traditional virtual machine or dual boot setup.

To get started, create a directory named `freecodecamp-gear-protocol`. Since you'll be building about fours projects, and I think it is important on how you can setup your projects for Gear Protocol.

So in your `freecodecamp-gear-protocol` directory, create a `Cargo.toml` file with the following code:

```toml
[workspace]
resolver = "2"
members = []


[workspace.package]
name = "freecodecamp-gear-protocol"
version = "0.1.0"
edition = "2021"
authors = ["Rocky Essel"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal Crates
# External Crates
```

For someone new to Rust or used to creating single projects, I'll guide you through understanding and setting up a workspace in Rust, making it easy to grasp.

### Understanding Your Workspace

A workspace in Rust is a set of packages (crates) that are managed together. Let's break down the key sections: `[workspace]`, `members`, `[workspace.package]`, and `[workspace.dependencies]`. So think of this like a cabin for your shoes, where each pair of shoes is a crate (package) that you want to keep organized.

#### `[workspace]` Section

The `[workspace]` section defines the overall workspace. It typically contains multiple members.

**`resolver = "2"`**: Specifies the version of Cargo's feature resolver to use, improving how dependencies are managed across the workspace.

**`members`**: Lists the crates that are part of the workspace. When you add a project with `cargo new --lib sneakers` or `boots`, the `members` section of the `Cargo.toml` is populated with the name of the project you created.

> If not added automatically, you can add them yourself.

  For example:

```toml
members = ["sneakers", "boots"]

```

#### `[workspace.package]` Section

This section provides metadata for the entire workspace as if it were a single package.

* **`name`**: The name of the workspace package.
* **`version`**: The version of the workspace package.
* **`edition`**: The Rust edition being used (e.g., "2021").
* **`authors`**: List of authors.
* **`license`**: The license for the workspace package.
* **`publish`**: Indicates whether the workspace package should be published to crates.io.

Example:

```toml
[workspace.package]
name = "my-shoe-collection"
version = "0.1.0"
edition = "2021"
authors = ["Your Name"]
license = "MIT"
publish = false
```

#### `[workspace.dependencies]` Section

Lists dependencies that apply to the entire workspace. Meaning that every crate whether external or internal added to the `[workspace.dependencies]` is accessible to every project you create under project workspace. So below is how both external and internal crate are made accessible to other project.

**Note**: For internal crate, you need to add them yourself.

**`Internal Crates`**: Add internal crates like this:

```toml
sneakers = { path = "sneakers" }
boots = { path = "boots" }
```

**`External Crates`**: Add external crates like this:

```toml
polish = "1.0"
```

### Example `Cargo.toml`

Here's an example combining these sections:

```toml
[workspace]
resolver = "2"
members = ["sneakers", "boots"]

[workspace.package]
name = "my-shoe-collection"
version = "0.1.0"
edition = "2021"
authors = ["Your Name"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal crate
sneakers = { path = "sneakers" } 
boots = { path = "boots" } 

# External crate
polish = "1.0"
```

So, here's how you set up a workspace for your project to manage multiple crates (sub-projects) and share dependencies and configuration settings across them. I spent quite some time understanding this, so I thought I'd share it with you all to make it easier.

To build your first smart contract, run the command below in your parent directory (`freecodecamp-gear-protocol`) on your terminal.

```bash
cargo new --lib receive-joke
```

```bash
.freecodecamp-gear-protocol
├── Cargo.toml
└── receive-joke
    ├── Cargo.toml
    └── src
        └── lib.rs

2 directories, 3 files
```

Head over to your `freecodecamp-gear-protocol/receive-joke/Cargo.toml`, and this is how you access crates, and configuration from the workspace directory(main) using `.workspace=true`, like below;

```toml
[package]
name ="receive-joke"
version.workspace = true
edition.workspace = true
authors.workspace = true
license.workspace = true
publish.workspace = true

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

Next, create a `build` file in your `receive-joke` directory with path like`receive-joke/build.rs`, and paste the code below. Now, the `build.rs` helps you to build your project into `.wasm` file, that is used to deploy your smart contract.

**build.rs:**

```rust
fn main() {
    gear_wasm_builder::build();
}
```

Currently, you have't install the nesscessary crate to help create your smart contract. Therefore, add the following crate to your workspace dependency.

**Cargo.toml:**

```toml
[workspace]
resolver = "2"
members = ["receive-joke"]


[workspace.package]
name = "freecodecamp-gear-protocol"
version = "0.1.0"
edition = "2021"
authors = ["Rocky Essel"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal Crates

# External Crates
gstd = "1.4.1"
gmeta = "1.4.1"
gtest  = "1.4.1"
gear-wasm-builder = "1.4.1"
parity-scale-codec = { version = "3.6.12", default-features = false }
scale-info = { version = "2.11.3", default-features = false }
```

For your first project, only `gstd` would be used, so like add that external crate to your `receive-joke`'s `Cargo.toml`. Like below:

```toml
[dependencies]
gstd.workspace = true


[build-dependencies]
gear-wasm-builder.workspace = true
```

If you reached here without any errors, well done my friend. Next, is to clear any code in `freecodecamp-gear-protocol/receive-joke/src/lib.rs`. Let's move on to the next step.

In Gear Protocol, there are entry points. An entry point serves as a gateway or door to your code. Gear has a few entry points, namely:

```rust
state(),
handle(),
handle_reply(),
init(),
handle_signal(),
```

Each entry point plays a significant role. For example, `init()` is called when the smart contract(`.wasm`) is deployed, allowing you to set certain conditions or variables or even other functions  that need to be executed for smooth sailing of your smart contract or program.

However, it's optional, meaning that you can choose to include or exclude it depending on your project, but it still gets executed, and it is the first message you'll see once you deploy your smart contract.

The `handle()` method is crucial as it contains most of the business logic. It's mandatory to include your program. More light will be shared on the entry points as you move forward.

Now, paste the following code into your `receive-joke/src/lib.rs`:

```rust
#![no_std]

use gstd::msg;

#[no_mangle]
extern "C" fn handle() {
    // Send a reply(in HTTP GET Request, you'd use "response").
    msg::reply_bytes(
        "What did the dirt say to the rain? If you keep this up, my name will be mud!",
        0,
    )
    .expect("Unable to reply");
}
```

The code above defines a function `handle` that, when called, sends a message you've defined as a response using the `gstd::msg` functionality. This `gstd` is a crate provided by Gear Protocol**,** to send and receive messages, and this is crucial for programs running on Vara Network to communicate with each other and external systems. And the `reply_bytes` send a new message as a reply to the message that is currently being processed.

Time to deploy and send your first message and recieve your joke reply. In your terminal, run the following command to build your program into **`.wasm`**.

Usually, I use `cargo check` for check for errors first, before using the `build` command below, either way is fine.

```bash
cargo build --release
```

After the build is completed, follow the structure below to locate your **`.wasm`** file in the path below:

```bash
.freecodecamp-gear-protocol
├── Cargo.lock
├── Cargo.toml
├── receive-joke
│   └── ...
└── target
    ├── ...
    └── wasm32-unknown-unknown
        ├── ...
        └── release
            ├── receive_joke.opt.wasm <--- Optimized for deployment.
            └── receive_joke.wasm
```

### How to Deploy Your Smart Contract

Just like in other blockchain tools, that help you deploy your smart contract from the terminal, IDEA is where you deploy your smart contract and interact with it. We'll be exploring the interface in a bit. So finally, head over to [IDEA](https://idea.gear-tech.io/) so start familiarizing yourself with your deployment environment. 

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-135927.png)
_Smart Contract Deplyment Web App- IDEA_

1. Step one, click on **Upload program**, then select or drag your **`.opt.wasm`** inside the modal. This takes you to the upload page, where you can change names, enter values for the payload, or change the payload type. For now, let's leave everything as it is, and click on the **Calculate,** which will enter a `0.00015` gas fee value for uploading your program.

**Note**: You can either set the gas limit yourself, or click on **Calculate** to allow the program to generate one for you.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-144729.png)
_Upload Page Details_

At this point, click on the **Upload Program**, and click on the **Submit** button.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-144825.png)
_Transaction Details- PopUp_

When you submit, you'll be prompted you sign into a your wallet, and approve.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-128.png)
_Wallet - SubWallet_

After the approval, a toast message should be displayed at the right-hand corner your computer/laptop screen for you to see the status of your program, whether it failed or succeeded.

Assuming it's a success, click on the **Programs** on the sidebar, then BOOM!, there's your program. Click on it, and let's explore.

Upon deploying, the first thing you see is the program ID, but after a few seconds, the name of your program would be shown.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-150230.png)
_Smart Contract Block - Page_

Earlier, I said that when you deploy a program, the `init()` function is executed regardless of whether you defined it in your project or not, and that's what you see in the **Messages** section. Below is a simple illustration for you to familiarize and understand the information about your program.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-129.png)
_Page Illustration_

Now, it's time to send a message to your program and receive a reply back, which is our joke. Remember, you're not inputting any values, you're just performing a simple action to receive a reply from the program. So click on **Calculate** and press the **Send Message** (that's the action or interaction) button.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-152529.png)
_Performing an action - Initial Stage_

After the message has been sent, a `success` toast will popup. Then head back to your program by clicking on the **Cancel** button, and you'll see two additional messages. 

Remember, the blue color with the arrow represent the message you sent, and the green represents the reply you've received. So click on the replied message to see the joke, which says: `What did the dirt say to the rain? If you keep this up, my name will be mud!`.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-130.png)
_Receiving Reply &amp; More Illustration_

Now, you're finally done with this project. In the next project, you'll be sending data or information to your program, and having it return a reply with your entered value attached to it. [Here is the program deployed on the **Vara Network**](https://idea.gear-tech.io/programs/0x79e6c86aa1ab2026ef3bbc0ccbe801ce085ca2614b36f9e5be04d2354ad56396).

### Important Information

Though I've provided some context to the picture above, I want to expand on it. Both the `Source` and `Destination` takes an address that can be either a user (actor) and a program (actor), or even a message object.

## Next Project – `input-msg`

Just like the illustration earlier, you're going to interact with your program by sending an input value to your smart contract deployed on **`[IDEA](https://idea.gear-tech.io/programs?node=wss%3A%2F%2Ftestnet.vara.network)`**. [**IDEA** ](https://idea.gear-tech.io/programs?node=wss%3A%2F%2Ftestnet.vara.network) is your deployment environment where you deploy your smart contract on the Vara Network.  
 The point here is for you to load input values from your user, and process it by concatenating a string to the user's input value: "We've received your query. {user's-input}".

This is the reply you'll send back to the user that sends a message (input value).

So in your `freecodecamp-gear-protocol` directory, run the command below to add another member to your `freecodecamp-gear-protocol/Cargo.toml`.

```bash
cargo new --lib input-msg
```

After adding another member or project in the `freecodecamp-gear-protocol`, your path should be `freecodecamp-gear-protocol/input-msg`.

Earlier, I made mention of how to access input values into the smart contract or program by using `gstd`, which has a function or method called `load()`. For the next step, clear your `freecodecamp-gear-protocol/input-msg/src/lib.rs`, and paste the following code and run `cargo check`.

```bash
#![no_std]

use gstd::{msg, prelude::*};

#[no_mangle]
extern "C" fn handle() {
    let new_msg = msg::load().expect("Unable to create string");
    let reply_msg = format!("We've received your query {}", new_msg);
    msg::reply_bytes(reply_msg, 0).expect("Unable to reply.");
}

```

The check fails, but why? Well, the `load()` function has a type of `unknown`. And since Rust is a strongly typed language, it has to always know the type before hand, which wasn't the case, so it failed to build the project.

This should tell you that the `load()` doesn't have a type, and it is up to you to set the right data type, and failure to do so would result in some frustrating errors like below.

### Debugging

Now if you were to use a single project and not a workspace, then debugging the error might have easy like below.

```bash
     
  error[E0282]: type annotations needed
   --> C:\Users\user\Desktop\2024\web3\re-gear\input-msg\src\lib.rs:7:9
    |
  7 |     let new_msg = msg::load().expect("Unable to create string");
    |         ^^^^^^^
    |
  help: consider giving `new_msg` an explicit type
    |
  7 |     let new_msg: /* Type */ = msg::load().expect("Unable to create string");
    |                ++++++++++++

```

But since you and I are using a workspace, it makes debugging a little difficult. This is my error message i got, when dubgging this error.

```bash
  error[E0275]: overflow evaluating the requirement `gstd::parity_scale_codec::Compact<_>: gstd::Decode`
    |
    = help: consider increasing the recursion limit by adding a `#![recursion_limit = "256"]` attribute to your crate (`input_msg`)
    = note: required for `gstd::parity_scale_codec::Compact<_>` to implement `gstd::Decode`
    = note: 125 redundant requirements hidden
    = note: required for `gstd::parity_scale_codec::Compact<<_ as CompactAs>::As>` to implement `gstd::Decode`

  For more information about this error, try `rustc --explain E0275`.
  error: could not compile `input-msg` (lib) due to 1 previous error
  warning: build failed, waiting for other jobs to finish...
  error: cargo command run failed: exit status: 101
warning: build failed, waiting for other jobs to finish...
```

And  if you look closely, you can tell that the `input-msg` is what creating the error. In this case, run `rustc --explain E0275`, which output an suggestion like this

```bash
An evaluation of a trait requirement overflowed.

Erroneous code example:

trait Foo {}

struct Bar<T>(T);

impl<T> Foo for T where Bar<T>: Foo {}

This error occurs when there was a recursive trait requirement that overflowed before it could be
evaluated. This often means that there is an unbounded recursion in resolving some type bounds.

To determine if a T is Foo, we need to check if Bar<T> is Foo. However, to do this check, we need to
determine that Bar<Bar<T>> is Foo. To determine this, we check if Bar<Bar<Bar<T>>> is Foo, and so on. This
is clearly a recursive requirement that can't be resolved directly.

Consider changing your trait bounds so that they're less self-referential.
```

Now, though, compared to the first error message, this message doesn't provide a direct solution, it does tells you that, there's a type error in your code. And the reason is that, the `load()` can load any data type, so you should always defined a type for it.

```rust
#![no_std]

use gstd::{msg, prelude::*};

#[no_mangle]
extern "C" fn handle() {
    let new_msg: String = msg::load().expect("Unable to create string");
    let reply_msg = format!("We've received your query {}", new_msg);
    msg::reply_bytes(reply_msg, 0).expect("Unable to reply.");
}

```

In the above code, you've added a type `String` to the `new_msg` because that's the `type` you're expecting. Now run the build command, and deploy the file **`.opt.wasm`** to `IDEA`. 

```bash
.freecodecamp-gear-protocol
├── receive-joke
├── Cargo.toml
├── input-msg
│   └── ...
└── target
    ├── ...
    └── wasm32-unknown-unknown
        ├── ...
        └── release
            ├── input_msg.opt.wasm <--- Optimized for deployment.         
            ├── input_msg.wasm
            ├── receive_joke.opt.wasm
            └── receive_joke.wasm
```

When you're done, go to your program and click on the **Send Messages**. Type any value into the `payload` field, and it should be a `type` of `String`. 

Submit and approve and head back to your program, then select your `reply_message` box and you should see your `reply message`.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-06-080437.png)
_Smart Contract - Reply Message_

[You can find the program here on the Vara Network](https://idea.gear-tech.io/programs/0x25629eaa3c7a51ec407f89bbaae7ccb4f58c6026283758d0fccb50e3bb042bdd).

## Metadata & State

Metadata and state goes hand in hand with each other. In order for your client application to allow users to interact or request data(state) from your smart contract, you need to define both the metadata and state, and even if the state is defined, and the metadata was not provided, you cannot access the any data.

So let's take each step by step.

### Metadata

In the Gear Protocol world, metadata is like a blueprint for defining how different parts of a decentralized app (dApp) talk to each other. It's similar to how interfaces or types work in TypeScript. These blueprints describe how things like initial data type to expect, handling messages, and swapping data happen in the dApp, whether `In`, `Out`, and `InOut`.

When we make clear blueprints, it helps developers make sure that all the different parts of the dApp understand each other's data formats. This makes it easy for the smart contract (program-actor) and the client side app to share data smoothly.

To create these blueprints for your program, we use the `gmeta` tool. It helps us define these blueprints by outlining how different interactions work and what kinds of data they involve.

So, think of metadata in your program as similar to how interfaces/types work in TypeScript. They help organize how the different parts of your dApp communicate and understand each other's data.

### Example Of A Metadata

```bash
use gmeta::{InOut, Metadata, Out};

pub struct ProgramMetadata;

// Be sure to describe all the types.
// But if any of the endpoints is missing in your program, you can use ();
// as indicated in the case of `type Signal`.

impl Metadata for ProgramMetadata {
    type Init = InOut<MessageInitIn, MessageInitOut>;
    type Handle = InOut<MessageIn, MessageOut>;
    type Others = InOut<MessageAsyncIn, Option<u8>>;
    type Reply = String;
    type Signal = ();
    type State = Out<Vec<Wallet>>;
}
```

The above is an example of how it is defined. Don't worry if you don't understand it now, I'll cover more into details later. Now let's talk about the state.

### State

In Gear Protocol, the `state` function serves as a dedicated storage space within a program. This storage allows us to store and retrieve data as needed. Since this data is stored in persistent memory, it remains accessible even after the contract stops running. What's fascinating is that anyone with access to the blockchain can view this stored data. The `state` function doesn't alter or modify the blockchain itself. Instead, it simply provides a way to access stored data within the program.

Here is an example of a `state` function:

```bash
// Describe state structure
#[derive(TypeInfo, Decode, Encode, Clone)]
pub struct Messages {
    pub id: ActorId,
    pub content: String,
}

// Declare and initialize the state
static mut MESSAGES: Vec<Messages> = Vec::new();

#[no_mangle]
extern "C" fn state() {
    msg::reply(unsafe { MESSAGES.clone() }, 0).expect("Failed to share state");
}
```

When the `state` function is called, it returns a list of `wallets` data stored within the program. This means that once a program is deployed on the blockchain, anyone can read its state.

Additionally, developers have the flexibility to create custom programs that can read the state. This empowers you and I to tailor our data access methods according to the specific needs for our dApp, even if the primary program undergoes changes.

The key takeaway is that, the `state` function facilitates access to data stored in smart contracts. It's worth noting that both users and other programs can access the state of a program, providing a versatile means of interacting with stored data.

## Third Project - Building Messages

In our last project `input-msg`, we didn't keep track of the messages that got sent. So in this project, we'll cover the metadata and state.

Run the command below to create your project in **/freecodecamp-gear-protocol/**:

```bash
cargo new --lib messages
```

Next, add your **build.rs** file, and make the workspace dependencies available to the `/freecodecamp-gear-protocol/messages`.

### Adding Metadata to Messages

To setup a metadata for your project, you need to create an additional crate to manage that, so `cd` into **messages**, and run the command below.

```bash
cargo new --lib io
```

In your **freecodecamp-gear-protocol/messages/io/Cargo.toml**, copy and paste the following code:

```toml
[package]
name = "messages-io"
version.workspace = true
edition.workspace = true


[dependencies]
gstd.workspace = true
gmeta.workspace = true
```

Here, I changed the name from `io` to `messages-io`, and the reason is for me to identify, and separate it for other `io`'s in the workspace. And add the dependencies.

In order to use the `io` in your workspace, you need to go the **freecodecamp-gear-protocol/Cargo.toml**, and add a path from your `io` to your workspace, which you can then use in any of the projects that need `struct`, `enum`, and `method`.

In **freecodecamp-gear-protocol/Cargo.toml**:

```bash
[workspace]
resolver = "2"
members = ["receive-joke","input-msg"]


[workspace.package]
name = "freecodecamp-gear-protocol"
version = "0.1.0"
edition = "2021"
authors = ["Rocky Essel"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal Crates
messages-io={path = "messages/io"} < ---- Here

# External Crates
gstd = "1.4.1"
gmeta = "1.4.1"
gtest  = "1.4.1"
gear-wasm-builder = "1.4.1"
parity-scale-codec = { version = "3.6.12", default-features = false }
scale-info = { version = "2.11.3", default-features = false }
```

And that's the `Internal Crate` I talked about earlier. Next, you need to include the `messages-io` in your `messages` project, like below:

```toml
[package]
name="messages"
version.workspace = true
edition.workspace = true
authors.workspace = true
license.workspace = true
publish.workspace = true


[dependencies]
gstd.workspace = true
messages-io.workspace = true <---

[build-dependencies]
gear-wasm-builder.workspace = true
messages-io.workspace = true < ---

```

The reason for adding `messages-io.workspace` to both the `[dependencies]` and `[build-dependencies]` is to make the `struct`, `enums`, `pub variables` and `methods` accessible to `messages/src/lib.rs`, and `messages/build.rs` using `messages-io.workspace`.

### Metadata in `io/src/lib.rs`

```rust
#![no_std]

use gmeta::{InOut, Metadata, Out};
use gstd::{prelude::*, ActorId, Vec};

pub struct MessageMetadata;

pub static mut MESSAGES: Vec<User> = Vec::new();

pub struct Message {
    pub id: ActorId,
    pub content: String,
}

impl Metadata for MessageMetadata {
    type Init = InOut<Message, String>;
    type Handle = InOut<Message, String>;
    type State = Out<Vec<Message>>;
    type Reply = ();
    type Others = ();
    type Signal = ();
}

```

To implement the logic of the message-handling system for your program or smart contract, understanding how to set the metadata of your program is crucial.  
Therefore, much attention is needed here.

The `MessageMetadata` struct you've defined implements the `Metadata` trait, which then structures the message metadata for the program. Also, a mutable static variable `MESSAGES` is declared to store all the messages you and your users send to the program. And since it’s a mutable static variable, unsafe code will be required to modify it due to Rust's safety guarantees around mutable static variables.

The `Message` struct is defined with two fields: `id` (sender's identifier) and `content` (the message text).

The `Metadata` trait is implemented for `MessageMetadata`, defining several associated types. The `Init` type is set to `InOut<MessageInit, String>`, specifying the input-output types for the initialization phase. \

This means that when the contract is initialized, it will accept a `MessageInit` type and return a `String`. The `Handle` type is set to `InOut<Message, String>`, specifying the input-output types for handling messages. It accepts a `Message` type as input and returns a `String`. 

The `State` type is set to `Out<Vec<Message>>`, defining the state output type, meaning that the state of the contract will be a vector of `Message` objects, and it doesn’t accept any input to retrieve this state. The `Reply`, `Others`, and `Signal` types are all set to `()`, indicating no additional reply, other types, or signals are used in this case.

### Further Context of its usage.

In this system, the metadata definition specifies how the smart contract should handle initialization and message handling. During the initialization phase (`Init`), when the contract is deployed on the Vara Network, it uses the `Init` type to set up the initial state. The input is expected to be of type `MessageInit`, and the output will be a `String`. During deployment, you provide your ID and message content, which the contract processes using the `init()` method.

After deployment, the contract can handle new messages using the `Handle` type, which expects a `Message` type as input and returns a `String` as a response. This functionality is useful for adding new messages to the `MESSAGES` vector. For state management (`State`), the contract’s state is a list of messages (`Vec<Message>`), and it doesn’t accept any input to retrieve the state but outputs the current state when queried.

So to summarize, the code in **freecodecamp-gear-protocol/messages/io/src/lib.rs** defines the structure and behavior of a message-handling smart contract, specifying how it initializes, handles messages, and manages state.

### Building the Metadata

In order to build your project with the metadata, you need to modify the **build.rs**, which initially looks like below:

```rust
fn main() {
    gear_wasm_builder::build();
}

```

There's nothing wrong with using the above code, but if you plan to build your program and deploy on the blockchain to use it on the client or anywhere else, it would be impossible to interact with your smart contract if the metadata is not defined. Think of it like `ABI` in other blockchain environment.

So replace the code with:

```rust
use messages_io::MessageMetadata;

fn main() {
    gear_wasm_builder::build_with_metadata::<MessageMetadata>();
}
```

Finally, you would be handling the logic for your smart contract in the `messages/src/lib.rs` using the `handle()` function.

Here is the code for the `lib.rs`:

```rust
#![no_std]

use gstd::{exec, msg, prelude::*, ActorId};

use messages_io::*;

#[no_mangle]
extern "C" fn init() {
    let init: Message = msg::load().expect("Unable to decode Message");
    let init_message = Message {
        id: init.id,
        content: init.content,
    };

    unsafe { MESSAGES.push(init_message) };    
    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}


#[no_mangle]
extern "C" fn handle() {
    
    let message_handler: Message = msg::load().expect("Unable to decode Message");
    let message = Message {
        id: message_handler.id,
        content: message_handler.content,
    };
    unsafe { MESSAGES.push(message) };
    msg::reply_bytes("Message sent successfully.", 0).expect("Failed to send  reply message.");
}


#[no_mangle]
extern "C" fn state() {
    msg::reply(unsafe { MESSAGES.clone() }, 0).expect("Failed to share state");
}
```

### Initialization Function (`init`)

```rust
#[no_mangle]
extern "C" fn init() {
    let init: Message = msg::load().expect("Unable to decode Message");
    let init_message = Message {
        id: init.id,
        content: init.content,
    };

    unsafe { MESSAGES.push(init_message) };
    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}

```

The `init` function is the entry point for initializing the smart contract. It is marked with `#[no_mangle]` to prevent Rust from applying name mangling, making the function accessible from the smart contract runtime. 

The function begins by loading the initial message from the input payload using `msg::load()`. This message is expected to be of type `Message`, and if decoding fails, the function will panic with an error message. Next, a new `Message` instance is created from the loaded data. This new message is then added to the global `MESSAGES` vector, which is a mutable static variable marked as unsafe due to potential data races. Finally, the function sends a reply indicating successful initialization using `msg::reply_bytes`. If this reply fails, the function will panic.

### Message Handling Function (`handle`)

```rust
#[no_mangle]
extern "C" fn handle() {
    let message_handler: Message = msg::load().expect("Unable to decode Message");
    let message = Message {
        id: message_handler.id,
        content: message_handler.content,
    };
    unsafe { MESSAGES.push(message) };
    msg::reply_bytes("Message sent successfully.", 0).expect("Failed to send  reply message.");
}

```

The `handle` function is designed to handle incoming messages after the contract is deployed. Like the `init` function, it is marked with `#[no_mangle]` to ensure it can be called from the smart contract runtime. The function begins by loading the incoming message from the input payload. This message is decoded into a `Message` struct, and if decoding fails, the function will panic. 

A new `Message` instance is then created from the decoded data and added to the global `MESSAGES` vector using an unsafe block. The function then sends a reply indicating that the message was sent successfully. If the reply fails, the function will panic.

### State Query Function (`state`)

```rust
#[no_mangle]
extern "C" fn state() {
    msg::reply(unsafe { MESSAGES.clone() }, 0).expect("Failed to share state");
}

```

The `state` function allows querying the current state of the smart contract. It is also marked with `#[no_mangle]` for the same reasons as the previous functions. The function replies with a cloned version of the global `MESSAGES` vector, containing all the messages that have been added so far. This is done within an unsafe block due to the mutable static variable. If the function fails to send the state, it will panic.

So this code simply defines a smart contract with three main functions: `init` for initialization, `handle` for processing incoming messages, and `state` for querying the current state of the contract. Where each function carefully manages the global `MESSAGES` vector.

### Deployment on the Vara Network

%[https://www.loom.com/share/e967ebf211f54f2c9c85fedc593e427e?sid=3ef6709a-8b5a-412b-b80c-93f721ba135b]

Now you're done with this project, and hope you learned and have understood most of what I've written. In our next project, you'll be building something a bit more complex than this. So let's begin.

[Here is the program deployed on Vara Network](https://idea.gear-tech.io/programs/0x58acd467aa011554b0dc167f741e745b336a03943df6f1eba635e9c28ca9824e), and this is the [entire repository for the 3 projects](https://github.com/rockyessel/freecodecamp-gear-protocol) we've built so far. The next project is going to be stand-alone project so you won't use the workspace.

## Final Project

In this final project, you'll build a very simple game: where you (`player`) fights with the `boss`. So here is a simple layman's explanation of the game mechanics.

### Game Description

This game is a one-on-one battle between a player and a boss. To begin, the player selects their character from three options: Warrior, Mage, or Archer. Once the player's character data is stored in the program, the game begins.

In the game, the player immediately faces the boss, who starts with 10 lives (represented as an integer), while the player begins with 10 lives by default. The objective is to defeat the boss using a specific rule: the boss has weaknesses represented by letters (X, Y, Z), each associated with a random number.

During gameplay, if the player enters one of these letters, for example, 'Y' with a value of 4, and the boss starts with 0 lives, the program subtracts 4 lives from the boss, leaving 6. Similarly, when the player makes a move with a letter, the boss also makes a move with the a random letter with an associated value added to it.

The player progresses to the next level upon defeating the boss, continuing the battle with new challenges. I call this game Battle Showdown **🤣😁😂.**

### **Battle Showdown** Mechanics Summary

#### Player and Boss Lives

* Player starts with 10 lives.
* Boss starts with 10 lives.

#### Weaknesses and Values

* Boss and the player has weaknesses represented by letters ( `X`, `Y`, `Z`), each associated with a random number.

#### Gameplay

* Player inputs a letter (for example, `'Y'`) and the associated value (for example, `4`) is subtracted from the boss's lives.
* Boss retaliates with a letter and the same value is subtracted from the player's lives.
* The objective is for the player to reduce the boss's lives to 0 to progress to the next level.

### Match Equation

Let's define the key variables:

* (`Lp`) = Player's current lives.
* (`Lb`) = Boss's current lives.
* (`V`) = Value associated with the letter representing the attack.

**Initial conditions:**

* ( `Lp` = 10 )
* ( `Lb` = 10 )

**Player's turn:**

* Player selects a letter with an associated value (`V`).
* Boss's lives are reduced: (`Lb` = `Lb` - `V`).

**Boss's retaliation:**

* Boss selects a letter (same value (`V`)).
* Player's lives are reduced: (`Lp` = `Lp` - `V`).

This continues until either ( `Lb` ) (boss's lives) or ( `Lp` ) (player's lives) reaches 0.

### Equations

After the player's attack and the Boss's retaliation:  
[`Lb` = `Lb` - `V`]  
[`Lp` = `Lp` - `V`]

The game loop continues with the player and boss exchanging moves. Repeat until `Lb` `<= 0` or `Lp` `<= 0`

### Example

If the player inputs `'Y'` with a value of `4`:

* Initial: ( `Lp` = 10 ), ( `Lb` = 10 )
* Player's attack: ( `Lb` = 10 - 4 = 6 )
* Boss's retaliation: ( `Lp` = 10 - 4 = 6 )

Next move:

* If the player inputs another value, let's say: `'X'` with a value of `5`:
* Player's attack: ( `Lb` = 6 - 5 = 1 )
* Boss's retaliation: ( `Lp` = 6 - 5 = 1 )

The player wins as the Boss's lives ( `Lb` ) have reached 0.

The match equation for each round of the game can be summarized as:  
[`Lb` = `Lb` - `V`]  
[`Lp` = `Lp` - `V`]  
This process is repeated until either the player's lives (( `Lp` )) or the Boss's lives (( `Lb` )) reach 0, determining the winner of the battle.

### Windows Error

If you use Windows, you may encounter an error with the **link.exe**. Honestly, I cannot explain the reason behind the error, but in the Gear docs, it was made clear that Windows users might experience some problems when building their project.

But rest assured, there's a solution, and I'm going to guide you through it. So please follow these steps carefully so you don't have to deal with bugs along the way.

### Step 1 - Install WSL via Command Prompt

Open your CLI with administrative privileges, and run the command below:

```bash
wsl --install
```

After excutting the command, run the command below to list other Linux releases. 

```bash
wsl -l -o
```

This command shows a list of other Linux distros, and you can select anyone you've used before. If you're new to Linux distros, I recommend selecting the `Ubuntu-22.04`.

These are just lists and are read-only. In order to select your system, run the command below.

```bash
wsl --install -d {Distribtion Name here(Ubuntu-22.04)} 
```

After you're done with the installation, restart your PC. Wait a little while for the terminal to popup and prompt you for your details such as your username and password. If the terminal doesn't open, go to your start menu, and you will find something similar to this in your `Start` menu.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-6.png)
_Ubuntu in start menu_

After that, the next thing to do is to install Rust on your WSL. 

### How to Install Rust On Your WSL

To install Rust on your machine, I recommend that whenever you want to install any package, it is best practice to install updates and upgrades to the system before continuing with the installation.

```bash
sudo apt update && sudo apt upgrade -y
```

When you run `sudo apt update && sudo apt upgrade -y`, you first update the package lists to get the latest information about available software packages. Then, if the update is successful, it proceeds to upgrade the installed packages to their latest versions, automatically confirming the upgrades to avoid manual intervention. This is a common and recommended practice to keep your Linux system up-to-date and secure.

### Essential Dependencies.

The command below installs essential development tools (`build-essential`, `gcc`, and `make`) and the `curl` utility for making HTTP requests and downloading files. These packages are commonly required for software development, compilation, and system administration tasks.

```bash
 sudo apt install curl build-essential gcc make -y
```

After that, run the command in the terminal  

```bash
 curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh 

```

In the installation process, you'll be prompted a question: go with the `default` when it happens.

```bash
1. Proceed with installation (default) --> Enter
2. Customize installation
3. Cancel installation.


```

After this prompt, you have successfully installed Rust on the Ubuntu System. Now the next step is to restart your terminal, simply close the current terminal. Open a new one, and run the command below.

```bash
source "$HOME/.cargo/env" 

```

What this command source `"$HOME/.cargo/env"` does is to activate the Rust environment. The reason is that the Rust environment comprises essential variables and configurations required for effective Rust usage. Now, once run, there's no output, so you can verify the installation by running the command below.

```bash
 rustc -V

```

Expected output:

```bash
rockyessel@UBUNTU-ROCKY:~$ rustc -V rustc 1.73.0 (cc66ad468 2024-02-07)

```

When you're done, there're also additional dependencies we have to install. So here, install them.

```bash
// Install the following.

 --> rustup toolchain add nightly-2023-09-18
 --> rustup target add wasm32-unknown-unknown --toolchain nightly-2023-09-18
```

After successfully installing them, head to the next section, which is building a game project.

In your WSL terminal, create your project name `battle-showdown`, and adding all the necessary **toml** files, and dependences. After that, `cd` into your project `battle-showdown` and added another program called **io**, this is where you write your metadate and other complex or simple data-type for your dApp.

```bash
battle-showdown
.
├── Cargo.toml
├── io
│   ├── Cargo.toml
│   └── src
│       └── lib.rs
└── src
    └── lib.rs
```

So head-over to to your **./io/src/lib.rs** and paste the follow code:

```bash
#![no_std]

use gmeta::Metadata;

pub struct BattleShowdown;

impl Metadata for BattleShowdown {
    type Init = ();
    type Handle = ();
    type State = ();
    type Reply = ();
    type Others = ();
    type Signal = ();
}

```

Here, you have defined a new public struct named `BattleShowdown`. Structs are used to create custom data types by grouping fields of various types together. But in this case, you're providing an implementation for the required types of the `Metadata` trait for the `BattleShowdown` struct: `impl Metadata for BattleShowdown`.

`type Init = ()`, `type Handle = ()`, `type State = ()`, `type Reply = ()`, `type Others = ()`, and `type Signal = ()` specifies that the handlers or functions data type for `BattleShowdown` is of type `()`, which in Rust's unit type, equivalent to `void` in other language such as `TypeScript`.

So for now, we're saying that these handlers do not send or receive data as such. Hence, the code just specifies how `BattlwShowdown` interacts with the system. However, it is worth mentioning that, the `BattleShowdown` struct itself doesn't have any specific initialization data, state, handling behavior, replies, signals, or other associated types defined.

### Building Our Game

First off, let's make register the **io** in your parent directory **cargo.toml**. So head over to `./cargo.toml` and paste the code below:

```toml
workspace = { members = ["io"] }
[package]
name = "battle-showdown"
version = "0.1.0"
edition = "2021"

[dependencies]
gstd = "1.4.1"
battle-showdown-io={path = "io"}



[build-dependencies]
gear-wasm-builder = "1.4.1"
battle-showdown-io={path = "io"}
```

I've ensured that the "battle-showdown-io" path is included in both the dependencies and build-dependencies sections. This decision was intentional because when it's added solely to build-dependencies, only the structs, enums, and other data types or functions within the build.rs file gain access to them, not the dependencies in your **`./src/lib.rs`**. This is important because I'll be utilizing `battle-showdown-io` in both build-dependencies (`build.rs`) and dependencies (`./src/lib.rs`).

This step is crucial because overlooking it can lead to frustrating import errors.

Next, is the file **`./io/cargo.toml`**, paste the following code below.

```toml
[package]
name = "battle-showdown-io"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
gstd = "1.4.1"
gmeta = "1.4.1"
parity-scale-codec = { version = "3.6.12", default-features = false }
scale-info = { version = "2.11.3", default-features = false }
```

### Explaining Metadata For BattleShown

It's crucial to pay closer attention to this section, as I'll shed more light on explaining the metadata types for `BattleShown` and deploying it on the Vara Network.

```rust
#![no_std]

use gmeta::Metadata;

pub struct BattleShowdown;

impl Metadata for BattleShowdown {
    type Init = ();
    type Handle = ();
    type State = ();
    type Reply = ();
    type Others = ();
    type Signal = ();
}
```

### Defining Initialization – `Init`

To define the types for this purpose, consider whether your program or smart contract needs to store data or perform actions before the user can interact with it. In the case of this game, the answer is yes. 

The game assumes that only one person is playing and does not allow users to create their characters or players. This means that you need to store data before proceeding to use this program, and in this scenario, we need information about the person/developer/actor/user deploying the contract or program, which is you.

Here is the information you'll want to store:

* **playerId - Type: ActorId**  
The playerId is actually the address associated with your account, which has the type of `ActorId`.
* **playerName - Type: String**  
This has a type of string, pretty much straightforward.
* **playerCharacterType - Type: Enum**  
The `playerCharacterType` is an enum that gives the actor an option to select which type they want to be, with options including Mage, Warrior, and Archer.

```rust
#![no_std]

use gmeta::Metadata;

pub struct BattleShowdown;

impl Metadata for BattleShowdown {
    type Init = InOut<InitBattleShowdown, String>;
    type Handle = ();
    type State = ();
    type Reply = ();
    type Others = ();
    type Signal = ();
}

#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum CharacterType {
    Warrior,
    Mage,
    Archer,
}


#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct InitBattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub player_name: String,
}
```

Although I've previously discussed metadata, you might be curious about what `type Init = InOut<InitBattleShowdown, String>;` means. Well, it's nothing complex. Here, we're simply stating that the `init` handle will accept a data type of `InitBattleShowdown` and will respond with a data type of `String`.

Before you continue, one more step remains: implementing a `default trait` for the enum `CharacterType`. This ensures that if the `CharacterType` is not explicitly defined, it defaults to `Warrior`. Simply add the following code to the existing code above:

```rust
impl Default for CharacterType {
    fn default() -> Self {
        CharacterType::Warrior
    }
}
```

### Defining the `Handle`

Defining a type for the `handle` function mirrors the process for the `init` function, but the actual implementation is left to the developer, which in this case, is you. After reviewing code and experimenting with different approaches, I discovered a method used by Gear Protocol (which shares similarities with some of their projects) that made more sense.

### Action & Event

In their implementation, they utilized Actions and Events. Actions represent a set of operations that the program can perform, while Events are the outcomes of these Actions.

For example, in the context of this game, you could have an action named `Attack` with a corresponding Event named `Attacked`. These could potentially accept parameters and return results.

Therefore, to define the handle type, include the following code in your existing codebase:

```rust

#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownAction {
    Attack {
        character_hit_power_value: PlayerHitPowerValue,
    },
}
```

Previously, when describing the game mechanics, I introduced a mechanic involving a letter with a randomly assigned number to inject an element of randomness. In this context, these letters correspond to an `ENUM` state of `X`, `Z`, and `Y`.

Therefore, to implement this mechanic, add the following code:

```rust
...

#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum PlayerHitPowerValue {
    X,
    Y,
    Z,
}
```

When an actor or user decides to attack the boss, they can select from the options provided above, each with a random value. Consequently, each attack on the boss will yield different outcomes due to the variability in these values. Similar to how you implemented a default trait for the `CharacterType`, you should follow suit here.

```rust
impl Default for PlayerHitPowerValue {
    fn default() -> Self {
        PlayerHitPowerValue::X
    }
}
```

### Event

As mentioned earlier, events are the outcomes of actions. Unlike the `BattleShowdownAction`, which only had one action, the `BattleShowdownEvent` will encompass more than two actions. Why? Because the game's logic dictates that when the user attacks, the boss also counterattacks. This results in three possible outcomes: either the user loses, the boss is defeated, or the battle continues. 

However, the third outcome is contingent upon the first two outcomes.  
Therefore, for the `BattleShowdownEvent`, you will need to define:

```rust
#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownEvent {
    Attacked {
        id: ActorId,
        character_type: CharacterType,
        name: String,
        player_lives: u32,
        boss_livesL: u32,
    },

    PlayerLost {
        id: ActorId,
        character_type: CharacterType,
        boss_livesL: u32,
        player_lives: u32,
        message: String,
    },

    BossLost {
        character_type: CharacterType,
        player_lives: u32,
        boss_livesL: u32,
        message: String,
    },
}

```

You have one action, but there are three possible events, correct? When the user/actor attacks the boss and the boss counterattacks, if either of them is defeated, the "Attacked" event is returned. However, if the player successfully defeats the boss, the "BossLost" event is returned.  
Now that you have a solid understanding, let's incorporate both the input and output types for the Handle function: `type Handle = InOut<BattleShowdownAction, BattleShowdownEvent>;`.

### Defining `State`

As previously mentioned, the state stores information within your program. For `BattleShowdown`, the state you'd want to store includes information about the player, the boss, and the current level.

```rust
#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct BattleShowdownState {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
}
```

Therefore, whenever you call the state function, you should expect to see the result in this format. Now, add the `BattleShowdownState` to the state in the metadata, like so: `type State = Out<BattleShowdownState>;`.

With that, the setup is complete. Here is the entire code for the **./io/src/lib.rs** file.

```rust
#![no_std]

use gmeta::{In, InOut, Metadata, Out};
use gstd::{prelude::*, ActorId};

// Define the main struct for the BattleShowdown
pub struct BattleShowdown;

// Implementing Metadata for BattleShowdown
impl Metadata for BattleShowdown {
    // Define the type for initialization messages
    type Init = InOut<InitBattleShowdown, String>;
    // Define the type for handle messages
    type Handle = InOut<BattleShowdownAction, BattleShowdownEvent>;
    // Define the type for state messages
    type State = Out<BattleShowdownState>;
    type Reply = ();
    type Others = ();
    type Signal = ();
}

// Struct for initializing the BattleShowdown
#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct InitBattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub player_name: String,
}

// Struct representing the state of the BattleShowdown
#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct BattleShowdownState {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
}

// Enum representing different character types
#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum CharacterType {
    Warrior,
    Mage,
    Archer,
}

// Enum representing different values for player hit power
#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum PlayerHitPowerValue {
    X,
    Y,
    Z,
}

// Implementing Default for PlayerHitPowerValue
impl Default for PlayerHitPowerValue {
    fn default() -> Self {
        PlayerHitPowerValue::X
    }
}

// Implementing Default for CharacterType
impl Default for CharacterType {
    fn default() -> Self {
        CharacterType::Warrior
    }
}

// Enum representing different actions in the BattleShowdown
#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownAction {
    Attack {
        character_hit_power_value: PlayerHitPowerValue,
    },
}

// Enum representing different events in the BattleShowdown
#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownEvent {
    Attacked {
        id: ActorId,
        character_type: CharacterType,
        name: String,
        player_lives: u32,
        boss_lives: u32,
    },
    PlayerLost {
        id: ActorId,
        character_type: CharacterType,
        boss_lives: u32,
        player_lives: u32,
        message: String,
    },
    BossLost {
        character_type: CharacterType,
        player_lives: u32,
        boss_lives: u32,
        message: String,
    },
}

```

### `Build.rs`

Import `BattleShowdown` to the **build.rs** from your parent directory at **./src/build.rs**. If you encounter an import error, make sure that in your **./cargo.toml**, you're registering `battle-showdown-io={path = "io"}` there.

```rust
use battle_showdown_io::BattleShowdown;

fn main() {
    gear_wasm_builder::build_with_metadata::<BattleShowdown>();
}
```

That's it for the **build.rs**, and what it does is to build your project into `wasm` and then build the `metadata` for `BattleShown` for you.

### Game Logic Implementation - `./src/lib.rs`

For this section, I'll write the code below, then I'll explain this as we go. There's going to be a problem I'd want you to solve, which will be about the state.

```rust
#![no_std]

use gstd::{exec, msg, prelude::*, ActorId};

use battle_showdown_io::*;

// Function to generate random number between 1 and 3
fn get_random_u32() -> u32 {
    let salt = msg::id();
    let (hash, _num) = exec::random(salt.into()).expect("get_random_u32(): random call failed");
    (u32::from_le_bytes([hash[0], hash[1], hash[2], hash[3]]) % 3) + 1 // Generate random number between 1 and 3
}

#[derive(Debug, Default)]
pub struct BattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub character_hit_power_value: PlayerHitPowerValue,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
    pub game_state: String,
}

static mut BATTLESHOWNDOWN: Option<BattleShowdown> = None;

#[no_mangle]
unsafe extern "C" fn init() {
    let init: InitBattleShowdown = msg::load().expect("Unable to decode InitBattleShowdown");

    let battle_showdown = BattleShowdown {
        player_id: msg::source(),
        player_character_type: init.player_character_type,
        player_name: init.player_name,
        boss_lives: 10,
        player_lives: 10,
        ..Default::default()
    };

    BATTLESHOWNDOWN = Some(battle_showdown);

    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}

impl Encode for BattleShowdown {
    fn encode(&self) -> Vec<u8> {
        let mut encoded = Vec::new();

        // Encode each field of BattleShowdown struct
        encoded.extend_from_slice(&self.player_id.encode());
        encoded.extend_from_slice(&self.player_character_type.encode());
        encoded.extend_from_slice(&self.current_level.encode());
        encoded.extend_from_slice(&self.player_lives.encode());
        encoded.extend_from_slice(&self.player_name.encode());
        encoded.extend_from_slice(&self.boss_lives.encode());
        encoded.extend_from_slice(&self.character_hit_power_value.encode());
        encoded.extend_from_slice(&self.player_hit_power.encode());
        encoded.extend_from_slice(&self.boss_hit_power.encode());
        encoded.extend_from_slice(&self.game_state.encode());

        encoded
    }
}

impl BattleShowdown {
    // Placeholder for the `attack` method
    fn attack(&mut self, _character_hit_power_value: PlayerHitPowerValue) -> BattleShowdownEvent {
        // Implement this method according to your game logic
        // For now, just returning an empty event

        // Calculate total hit power for player based on character type and random values
        let character_hit_power = match &self.player_character_type {
            CharacterType::Warrior => 4,
            CharacterType::Mage => 3,
            CharacterType::Archer => 2,
        };

        let player_hit_power = match &self.character_hit_power_value {
            PlayerHitPowerValue::X => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Y => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Z => character_hit_power + get_random_u32(),
        };

        // Placeholder for boss attack logic
        // Update boss hit power to a random value for each attack
        self.boss_hit_power = get_random_u32();

        self.player_hit_power = player_hit_power;

        // Reduce boss's lives based on player's hit power
        self.boss_lives = self.boss_lives.saturating_sub(self.player_hit_power);
        // Reduce player's lives based on boss's hit power
        self.player_lives = self.player_lives.saturating_sub(self.boss_hit_power);

        // Check if player or boss has lost
        if self.player_lives == 0 {
            // Player lost
            self.game_state = "Player lost.".to_string();
            return BattleShowdownEvent::PlayerLost {
                id: self.player_id,
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                message: "".to_string(),
                player_lives: self.player_lives,
            };
        } else if self.boss_lives == 0 {
            // Boss lost
            self.game_state = "Boss lost.".to_string();
            return BattleShowdownEvent::BossLost {
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                player_lives: self.player_lives,
                message: "You've defeated the boos".to_string(),
            };
        }

        self.game_state = "The games continues.".to_string();
        BattleShowdownEvent::Attacked {
            boss_lives: self.boss_lives,
            character_type: self.player_character_type,
            id: self.player_id,
            name: self.player_name.clone(),
            player_lives: self.player_lives,
        }
    }
}

#[no_mangle]
extern "C" fn handle() {
    let battle_showdown_action: BattleShowdownAction =
        msg::load().expect("Could not load BattleShowdownAction");
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .as_mut()
            .expect("`BattleShowdown` is not initialized.")
    };
    let result: BattleShowdownEvent = match battle_showdown_action {
        BattleShowdownAction::Attack {
            character_hit_power_value,
        } => battle_showdown.attack(character_hit_power_value),
    };
    msg::reply_bytes(result.encode(), 0)
        .expect("Failed to encode or reply with `BattleShowdownEvent`.");
}

#[no_mangle]
extern "C" fn state() {
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .take()
            .expect("Unexpected error in taking state")
    };

    msg::reply(battle_showdown, 0).expect("Unable to share the state");
}

```

At first glance this might seem a lot, but it isn't, so don't get too intimidated. Before you start, make sure you understand the whole logic of the game description I gave earlier since you'll be implementing it here.

Above, we have some important functions, `struct`, and `impl`, and here is an overview of what they do.

1. With the `get_random_u32` function, we generated a random number between 1 and 3.
2. The `BattleShowdown` struct in the `/src/lib.rs` represents the main state of the game. It holds information such as player and boss stats, current game level, and game state. The `static mut BATTLESHOWNDOWN: Option<BattleShowdown> = None;` is a static mutable variable that holds the current state of the game. It's wrapped in an `Option` to indicate whether the game has been initialized yet or not, which you'll use later in your implementation.
3. `unsafe extern "C" fn init()` is responsible for initializing the game state when called after the contract has been uploaded. It loads an initialization message, constructs a `BattleShowdown` instance based on that message, and sets `BATTLESHOWNDOWN` to `Some` with the constructed instance.
4. `impl Encode for BattleShowdown`: this trait is implemented for `BattleShowdown`, enabling it to be encoded into a byte representation. This is useful for serialization and sending the game state over the network. And there's a way to also implement the trait without creating an `impl` for `BattleShowdown`.
5. `impl BattleShowdown`: this `impl` for `BattleShowdown` is where the entire logic happens, and for now, we've only added an `attack` method for it. It worth noting that we'll be adding more as we continue this project.
6. So what does the `attack` method do? Well, The `attack` method simulates a combat encounter between the player and the boss character in our game. It calculates the hit power for both entities based on character type and randomness, manages their health points accordingly, and generates game events to reflect the outcome of the encounter.
7. `extern "C" fn handle()`: In our case, the `handle` function is used to process incoming messages, specifically `BattleShowdownAction`. So depending on the action perform by the actor, it dispatches a result of the action to the appropriate methods of `BattleShowdown`, such as `attack`, and sends back the resulting game events to the actor. Like disccued in the illustration.
8. And lastly, `extern "C" fn state()` simply retrieves the current game state represented by `BattleShowdown` and sends it as a reply.

This is the overall explanation to the code in the file. But leaving with this isn't enough for even me. Let's disccus more below.

### Understanding the`init()`

```rust
#[derive(Debug, Default)]
pub struct BattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub character_hit_power_value: PlayerHitPowerValue,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
    pub game_state: String,
}

static mut BATTLESHOWNDOWN: Option<BattleShowdown> = None;

#[no_mangle]
unsafe extern "C" fn init() {
    // Load initialization data
    let init: InitBattleShowdown = msg::load().expect("Unable to decode InitBattleShowdown");

    // Create a BattleShowdown instance with initial values
    let battle_showdown = BattleShowdown {
        player_id: msg::source(),
        player_character_type: init.player_character_type,
        player_name: init.player_name,
        boss_lives: 10,
        player_lives: 10,
        ..Default::default()
    };

    // Store the BattleShowdown instance
    BATTLESHOWNDOWN = Some(battle_showdown);

    // Reply to signal successful initialization
    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}
```

The function loads data from an initialization message (`InitBattleShowdown`) sent by the developer or player. This data includes the player's chosen `character type` and `name`. Based on the initialization data, a `BattleShowdown` instance is created with initial values, which is stored in `battle_showdown`. 

This instance represents the state of the game, including player and boss stats, current level, and game state. The created `BattleShowdown` instance is stored in the `BATTLESHOWNDOWN` static variable, allowing the game logic to access and manipulate the game state throughout the gameplay. Finally, a reply message is sent back to the developer or player to indicate successful initialization of the game contract. 

This function sets up the initial state of the game, paving the way for further interactions and gameplay logic.

### Understanding the `handle()`

```rust
#[no_mangle]
extern "C" fn handle() {
    // Load the action from the message
    let battle_showdown_action: BattleShowdownAction =
        msg::load().expect("Could not load BattleShowdownAction");

    // Retrieve the current game state
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .as_mut()
            .expect("`BattleShowdown` is not initialized.")
    };

    // Execute the appropriate action on the game state and get the result
    let result: BattleShowdownEvent = match battle_showdown_action {
        BattleShowdownAction::Attack {
            character_hit_power_value,
        } => battle_showdown.attack(character_hit_power_value),
    };

    // Send back the result as a reply message
    msg::reply_bytes(result.encode(), 0)
        .expect("Failed to encode or reply with `BattleShowdownEvent`.");
}
```

The `handle()` function plays a crucial role in processing incoming messages and orchestrating the game's actions. It serves as the bridge between player interactions and the game's internal logic. When invoked, `handle()` begins by loading the `action` sent by the player from the message. 

This `action`, encapsulated as `BattleShowdownAction`, dictates the player's intended move, such as attacking the boss. Next, the function retrieves the current game state from the `BATTLESHOWNDOWN` variable. This state holds essential information about the player, the boss, and the overall game environment. 

With both the action and the game state at hand, `handle()` proceeds to execute the appropriate action. For instance, if the player's action is an `attack`, the function triggers the `attack()` method on the `battle_showdown` instance. This method calculates the outcome of the player's attack, considering factors like the player's hit power and the boss's remaining health points.

Crucially, the `attack()` method requires a parameter: `character_hit_power_value`. This parameter corresponds to the player's choice between three options: `X`, `Y`, and `Z`, each associated with different hit power values as disccused in earlier sections. 

Once the `action` is executed, `handle()` generates an event, encapsulated as `BattleShowdownEvent`, reflecting the outcome of the player's move. This event encapsulates important details, such as changes in player and boss health points. Finally, `handle()` responds to the player by replying with the result of the action as a byte-encoded message. This message contains the updated game state, allowing the player to understand their current situation, including their health status and that of the boss.

### Understanding the `impl BattleShowdown for attack`

```rust
impl BattleShowdown {
    fn attack(&mut self, _character_hit_power_value: PlayerHitPowerValue) -> BattleShowdownEvent {
        // Calculate total hit power for player based on character type and random values
        let character_hit_power = match &self.player_character_type {
            CharacterType::Warrior => 4,
            CharacterType::Mage => 3,
            CharacterType::Archer => 2,
        };

        let player_hit_power = match &self.character_hit_power_value {
            PlayerHitPowerValue::X => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Y => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Z => character_hit_power + get_random_u32(),
        };

        // Placeholder for boss attack logic
        // Update boss hit power to a random value for each attack
        self.boss_hit_power = get_random_u32();

        self.player_hit_power = player_hit_power;

        // Reduce boss's lives based on player's hit power
        self.boss_lives = self.boss_lives.saturating_sub(self.player_hit_power);
        // Reduce player's lives based on boss's hit power
        self.player_lives = self.player_lives.saturating_sub(self.boss_hit_power);

        // Check if player or boss has lost
        if self.player_lives == 0 {
            // Player lost
            self.game_state = "Player lost.".to_string();
            return BattleShowdownEvent::PlayerLost {
                id: self.player_id,
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                message: "".to_string(),
                player_lives: self.player_lives,
            };
        } else if self.boss_lives == 0 {
            // Boss lost
            self.game_state = "Boss lost.".to_string();
            return BattleShowdownEvent::BossLost {
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                player_lives: self.player_lives,
                message: "You've defeated the boss".to_string(),
            };
        }

        self.game_state = "The game continues.".to_string();
        // Return event indicating attack occurred
        BattleShowdownEvent::Attacked {
            boss_lives: self.boss_lives,
            character_type: self.player_character_type,
            id: self.player_id,
            name: self.player_name.clone(),
            player_lives: self.player_lives,
        }
    }
}
```

The `attack` method within the `BattleShowdown` implementation simulates a pivotal moment in the game: a combat encounter between the player and the boss character. 

Here's how it works:

Firstly, the method calculates the total hit power for the player based on their character type (`character_hit_power`) and randomness (`player_hit_power`). Different character types (`Warrior`, `Mage`, or `Archer`) have different base hit powers. 

Next, a random hit power value is added to the character's base hit power. This adds an element of unpredictability to each attack. The method then updates the boss's hit power (`self.boss_hit_power = get_random_u32();`) to a random value, representing the boss's retaliatory strike against the player.

After calculating the hit powers, the method reduces the boss's lives based on the player's hit power and vice versa, updating their respective health points accordingly.

```rust
        // Reduce boss's lives based on player's hit power
        self.boss_lives = self.boss_lives.saturating_sub(self.player_hit_power);
        // Reduce player's lives based on boss's hit power
        self.player_lives = self.player_lives.saturating_sub(self.boss_hit_power);
```

The game state is then checked to determine if either the player or the boss has lost the battle. If the player's health points reaches zero, the game state is updated to indicate that the player has lost. Conversely, if the boss's health points reach zero, the game state reflects the boss's defeat.

```rust
        // Check if player or boss has lost
        if self.player_lives == 0 {
            // Player lost
            self.game_state = "Player lost.".to_string();
            return BattleShowdownEvent::PlayerLost {
                id: self.player_id,
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                message: "".to_string(),
                player_lives: self.player_lives,
            };
        } else if self.boss_lives == 0 {
            // Boss lost
            self.game_state = "Boss lost.".to_string();
            return BattleShowdownEvent::BossLost {
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                player_lives: self.player_lives,
                message: "You've defeated the boss".to_string(),
            };
        }

        self.game_state = "The game continues.".to_string();
        // Return event indicating attack occurred
        BattleShowdownEvent::Attacked {
            boss_lives: self.boss_lives,
            character_type: self.player_character_type,
            id: self.player_id,
            name: self.player_name.clone(),
            player_lives: self.player_lives,
        }
```

Finally, if neither the player nor the boss has lost, the game state is updated to indicate that the battle continues.

### Understanding the `State()`

```rust
#[no_mangle]
extern "C" fn state() {
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .take()
            .expect("Unexpected error in taking state")
    };

    msg::reply(battle_showdown, 0).expect("Unable to share the state");
}
```

For this instance there's nothing more to share, it retrieves the current state of the game, represented by the `BattleShowdown` struct, from a static mutable variable `BATTLESHOWNDOWN`, and sends a reply message containing the game state back to the player. If there is an error sending the reply message, it will panic with an error message indicating the inability to share the state.

And that's that for this project. There are some exciting features you can consider if you want to extend this project. Imagine the possibility of resetting the game state, accommodating multiple players, or even resetting the game for a single player. And for the ambitious, you could even tackle the challenge of resetting the state for the entire game. These additions can offer new dimensions to the project and provide excellent opportunities for you to challenge yourself.

### Short Recording of what we've built - Demo

%[https://www.loom.com/share/590d685f311f46c386943c41816dbf83?sid=e99d4948-f0ab-486d-a5fa-98fbcdfe3fe3]

In the video you could see I added another method for resetting everything back to it inital state. Though I didn't guide you through the process of doing that, you should know it is easy to implement, and I've added [a GitHub repository](https://github.com/rockyessel/battle-showdown) for the entire code.

### Conclusion

As demonstrated, developing a smart contract with Gear Protocol becomes straightforward once you grasp the communication message concepts. By following the steps outlined, you can start building your own projects with confidence.

While this article didn't delve into handling transactions such as token transfers, minting, or NFTs, I will cover these topics in a future article.

For now, you can explore the repository of the project we built together: [Battle-Showdown](https://github.com/rockyessel/battle-showdown), and if you have any question to ask, feel free to reach @rockyessel on X.

