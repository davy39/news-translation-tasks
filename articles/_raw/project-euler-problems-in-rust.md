---
title: How to Solve Project Euler Problems in Rust
subtitle: ''
author: Shaun Hamilton
co_authors: []
series: null
date: '2022-03-03T17:09:14.000Z'
originalURL: https://freecodecamp.org/news/project-euler-problems-in-rust
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-9-1.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Rust
  slug: rust
seo_title: null
seo_desc: "You can now solve the classic Project Euler programming problems using\
  \ the Rust language. Each of these problems comes with a user-friendly test suite.\
  \ \nHere's the full Project Euler Rust GitHub repository.\nIf you do not know Rust,\
  \ and want to learn ..."
---

You can now solve the classic Project Euler programming problems using the Rust language. Each of these problems comes with a user-friendly test suite. 

Here's the full [Project Euler Rust GitHub repository](https://github.com/freeCodeCamp/euler-rust).

If you do not know Rust, and want to learn it, you can start with [freeCodeCamp's interactive Rust course](https://www.freecodecamp.org/news/rust-in-replit/).

All right. Let's see how to get started working through Project Euler in Rust.

## How to Run the Project Euler Problems Locally in VSCode

First, you'll need to download and install the [freeCodeCamp Courses VSCode extension](https://marketplace.visualstudio.com/items?itemName=freeCodeCamp.freecodecamp-courses).

Also, ensure you have the Microsoft [Dev Containers VSCode extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

Then, in an empty workspace, open the VSCode command palette with `Ctrl/Cmd + Shift + P`.

![euler-rust-local-ext-1](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-1.png)

Select the command `freeCodeCamp: Open Course`.

![euler-rust-local-ext-2](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-2.png)

Next, choose the `Project Euler: Rust` option.

![euler-rust-local-ext-3](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-3.png)

Once the course is cloned, open the command palette again and select `Dev Containers: Rebuild and Reopen in Container`.

![euler-rust-local-ext-4](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-4.png)

![euler-rust-local-ext-5](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-5.png)

![euler-rust-local-ext-6](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-local-ext-6.png)

![euler-rust-gitpod](https://www.freecodecamp.org/news/content/images/2024/02/euler-rust-gitpod.png)


## How to Run the Project Euler Problems Locally without the Extension

If you would prefer to run these without the VS Code extension, you'll need to fork the repository:

![euler-rust-fork](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-fork.png)

Then clone your fork to your local machine.

```bash
git clone https://github.com/<your_username>/euler-rust.git
cd euler-rust
```

Build and open the Docker container like this:

```bash
docker build -f Dockerfile -t euler-rust .
```

And then start the course:

```bash
npm i && npm run start
```

Optionally, you can also clone and build the container with Docker like this:

```bash
docker build github.com/<your_username>/euler-rust
```

## How to Run the Project Euler Problems Using Gitpod

GitPod is a popular tool for running a VM in your browser, and is yet another way you can solve these Project Euler problems. First, fork the repository:

![euler-rust-fork](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-fork.png)

Then open your fork in Gitpod: `https://gitpod.io/#https://github.com/<your_user_name>/euler-rust`

Optionally, if you have the Gitpod browser extension installed, you can click the `Gitpod` button it adds to GitHub:

![euler-rust-gitpod-button](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-gitpod-button.png)

![euler-rust-gitpod-setup](https://www.freecodecamp.org/news/content/images/2022/02/euler-rust-gitpod-setup.png)

![euler-rust-gitpod](https://www.freecodecamp.org/news/content/images/2024/02/euler-rust-gitpod.png)

## Useful Information

_NOTE:_ If you are using any of the above methods with Docker, you will need to have Docker installed on your machine, and have the Daemon running.

You should need to only edit the `src/lib.rs` file within each `project-euler-problems-...` directory, and you can follow the example code there to get started.

To compile your code, before running the tests, run:

```bash
wasm-pack build
```

If at any point you get stuck, I recommend that you check out more information about [Rust with WASM](https://www.rust-lang.org/what/wasm). Otherwise, feel free to open a new topic on the [freeCodeCamp forum](https://forum.freecodecamp.org/).

## How the Project Works

First, taking your Rust code in `src/lib.rs`:

```rust
use wasm_bindgen::prelude::*;

// Example format to write functions:
#[wasm_bindgen(js_name = camelCaseName)] // js_name must equal function name tested on client
pub fn snake_case_name(num: i32) -> i32 { // Function must be public
    // All numbers in JS are 32-bit
    num
}
```

The Rust is transpiled into JavaScript code using `wasm-pack`:

```javascript
import * as wasm from "./curriculum_bg.wasm";

/**
 * @param {number} n
 * @returns {number}
 */
export function camelCaseName(num) {
  var ret = wasm.camelCaseName(num);
  return ret;
}
```

## Frequently Asked Questions (FAQ)

> Will these Project Euler problems be made available in other programming languages?

We welcome any and all well-intended contributions to the freeCodeCamp community. So, if you are interested in developing on a fork of the repository, please do so!

> Can I save my progress on my freeCodeCamp.org account?

Not yet, but it is something that we can look into further.

> The Docker step takes such a long time. Is there a quicker way to get started?

Well, provided you have the tenacity to install all the necessary tooling on your local machine, you can simple run the following commands within the project:

```bash
npm ci
npm run start
```

```bash
cd project-euler-problems-1-to-100
wasm-pack build
```

Now, you should be able to open a browser and navigate to `http://localhost:8080/`, and begin.



