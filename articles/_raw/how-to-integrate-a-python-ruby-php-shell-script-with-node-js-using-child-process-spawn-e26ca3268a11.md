---
title: How to integrate a Python/Ruby/PHP shell script with Node.js using child_process.spawn
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-a-python-ruby-php-shell-script-with-node-js-using-child-process-spawn-e26ca3268a11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mtP3Ak9ndB1jJo0mauPu5w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Hugo Di Francesco

  There are occasions when running a Python/Ruby/PHP shell script from Node.js is
  necessary. This post looks at best practices around leveraging child_process.spawn
  to encapsulate this call in Node.js/JavaScript.

  The goal here is t...'
---

By Hugo Di Francesco

There are occasions when running a Python/Ruby/PHP shell script from Node.js is necessary. This post looks at best practices around leveraging child_process.spawn to encapsulate this call in Node.js/JavaScript.

The goal here is to have an interoperability layer between Node.js and an outside shell. This is a quick workaround if some other part of your system isn’t developed in JavaScript.

We’ll use `spawn` over `exec` because we’re talking about passing data and potentially large amounts of it. To understand the difference between `child_process.spawn` and `child_process.exec` see “[Difference between spawn and exec of Node.js child_process](https://www.hacksparrow.com/difference-between-spawn-and-exec-of-node-js-child_process.html)”.

The long and short of it is use `exec` for small amounts of data (under 200k) using a Buffer interface and `spawn` for larger amounts using a stream interface.

`spawn` has a more verbose syntax for some of the use-cases we’ll look at. It’s more serviceable for integrating with Ruby/Python/PHP since we might get more data than a couple of lines of text.

Full examples [github.com/HugoDF/node-run-python](https://github.com/HugoDF/node-run-python).

The following examples contain 2 sections:

* The part that actually runs the shell command, usually a function called `run`, and
* an IIFE (“immediately invoked function expression”) that actually calls it, `(async () => { await run() }`)(). This IIFE is a nice pattern enabled by async/await (s[ee Async JS: history, patterns and gotc](https://codewithhugo.com/async-js/#async-await)has) but it’s just there for illustration purposes since it represents the call to the wrapp`ed sp`awn call from another part of your application.

### Call a shell command and log it

Using `spawn` is overkill in this situation since echo is only going to return what’s passed to it.

The example is pretty self-explanatory and shows how to use `child_process.spawn` to “shell out” and read that data back.

`spawn` takes the executable to call as the first parameter and optionally an array of options/parameters for the executable as the second parameter.

```js
const { spawn } = require('child_process');
function run() {
  const process = spawn('echo', ['foo']);
  process.stdout.on(
    'data',
    (data) => console.log(data.toString())
  );
}
(() => {
  try {
    run()
    // process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

### Call Python for its version

We’ll move quite quickly to showcase how we would do something similar to the above with Python. Note again how `--version` is passed inside of an array.

We also create a nice logger to differentiate between stdout and stderr and bind to them. Since spawn returns an instance which has `stdout` and `stderr` event emitters, we can bind our `logOutput` function to `'data'` event using `.on('data', () => { /* our callback function */` }).

Another interesting tidbit is that `python` `--version` outputs the version to `stderr`. The inconsistencies around whether *NIX executables use exit codes, stderr and stdout on success/error are a quirk that we’ll have to bear in mind while integrating Python/Ruby/other with Node.js.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data.toString()}`)
function run() {
  const process = spawn('python', ['--version']);
process.stdout.on(
    'data',
    logOutput('stdout')
  );
process.stderr.on(
    'data',
    logOutput('stderr')
  );
}
(() => {
  try {
    run()
    process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Output:

```
$ node run.js
```

```
[stderr] Python 2.7.13
```

### Call a Python script from Node

We’ll now run a fully-fledged Python script (although it could just as well be Ruby, PHP, shell etc.) from Node.js.

This is `script.py`, it just logs out `argv` (the “argument vector”, ie. `['path/to/executable', /* command line arguments ]`)

```py
import sys
print(sys.argv)
```

Like in the previous example, we’ll just call spawn with `python` with the path to the Python script (`./script.py`) in the second parameter.

Here comes another gotcha of integrating scripts in this fashion. In this example, the path to the script is based on the working directory from which `node` is called.

There is a workaround, of course, using the `path` module and `__dirname`, which for example could resolve a `other-script.py` co-located with the JavaScript file/Node module calling `spawn` using: `require('path').resolve(__dirname, './other-script.py')`.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data.toString()}`)
function run() {
  const process = spawn('python', ['./script.py']);
process.stdout.on(
    'data',
    logOutput('stdout')
  );
process.stderr.on(
    'data',
    logOutput('stderr')
  );
}
(() => {
  try {
    run()
    // process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Output:

```bash
node run.js
\[stdout\] ['./script.py']
```

### Pass arguments to a Python script from Node.js using child_process.spawn

The next step of integration is to be able to pass data from the Node/JavaScript code to the Python script.

In order to do this, we’ll just pass more shell arguments using the arguments array (the second parameter to `spawn`).

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data.toString()}`)
function run() {
  const process = spawn('python', ['./script.py', 'my', 'args']);
  process.stdout.on(
    'data',
    logOutput('stdout')
  );
  process.stderr.on(
    'data',
    logOutput('stderr')
  );
}
(() => {
  try {
    run()
    // process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Our `script.py` will also just log out the `argv` except for the first element (which is the path to the script).

```py
import sys
print(sys.argv)[1:]
```

Here’s the output:

```bash
node run.js
\[stdout\] ['my', 'args']
```

### Read child_process.spawn output from Node.js

It’s nice to be able to pass data down to the Python script. We’re still not able to get the data from the Python script back in a format that we’re able to leverage in our Node.js/JavaScript application.

The solution to this is to wrap the whole `spawn` -calling function into a Promise. This allows us to decide when we want to `resolve` or `reject`.

To keep track of the Python script’s output stream(s), we manually buffer the output using arrays (one for `stdout` and another for `stderr`).

We also add a listener for `'exit'` using `spawn().on('exit', (code, signal) => { /* probably call resolve() */` }). This is where we will tend `to reso`l`ve/rej`ect the Promise’s value(s) from the Python/Ruby/other script.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data}`)
function run() {
  return new Promise((resolve, reject) => {
    const process = spawn('python', ['./script.py', 'my', 'args']);
    const out = []
    process.stdout.on(
      'data',
      (data) => {
        out.push(data.toString());
        logOutput('stdout')(data);
      }
    );
    const err = []
    process.stderr.on(
      'data',
      (data) => {
        err.push(data.toString());
        logOutput('stderr')(data);
      }
    );
    process.on('exit', (code, signal) => {
      logOutput('exit')(`${code} (${signal})`)
      resolve(out);
    });
  });
}
(async () => {
  try {
    const output = await run()
    logOutput('main')(output)
    process.exit(0)
  } catch (e) {
    console.error(e.stack);
    process.exit(1);
  }
})();
```

Output:

```bash
node run.js
\[stdout\] ['my', 'args']
\[main\] ['my', 'args']
```

### Handle errors from child_process.spawn

Next up we need to handle errors from the Python/Ruby/shell script at the Node.js/JavaScript level.

The main way that a *NIX executable signals that it errored are by using a `1` exit code. That’s why the `.on('exit'` handler now does a check against `code === 0` before deciding whether to resolve or reject with value(s).

```js
const { spawn } = require('child_process')
const logOutput = (name) => (data) => console.log(`[${name}] ${data}`)
function run() {
  return new Promise((resolve, reject) => {
    const process = spawn('python', ['./script.py', 'my', 'args']);
const out = []
    process.stdout.on(
      'data',
      (data) => {
        out.push(data.toString());
        logOutput('stdout')(data);
      }
    );
const err = []
    process.stderr.on(
      'data',
      (data) => {
        err.push(data.toString());
        logOutput('stderr')(data);
      }
    );
process.on('exit', (code, signal) => {
      logOutput('exit')(`${code} (${signal})`)
      if (code === 0) {
        resolve(out);
      } else {
        reject(new Error(err.join('\n')))
      }
    });
  });
}
(async () => {
  try {
    const output = await run()
    logOutput('main')(output)
    process.exit(0)
  } catch (e) {
    console.error('Error during script execution ', e.stack);
    process.exit(1);
  }
})();
```

Output:

```bash
node run.js
[stderr] Traceback (most recent call last):
    File "./script.py", line 3, in <module>
    print(sy.argv)[1:]
NameError: name 'sy' is not defined
Error during script execution Error: Traceback (most recent call last):
    File "./script.py", line 3, in <module>
    print(sy.argv)[1:]
NameError: name 'sy' is not defined
at ChildProcess.process.on (/app/run.js:33:16)
    at ChildProcess.emit (events.js:182:13)
    at Process.ChildProcess._handle.onexit (internal/child_process.js:240:12)
```

### Pass structured data from Python/Ruby to Node.js/JavaScript

The final step to full integration between Ruby/Python/PHP/shell scripts and our Node.js/JavaScript application layer is to be able to pass structured data back from the script up to Node.js/JavaScript.

The simplest structured data format that tends to be available in both Python/Ruby/PHP and Node.js/JavaScript is JSON.

In the Python script, we print the `json.dumps()` output of a dictionary, see `script.py`:

```py
import sys
import json
send_message_back = {
  'arguments': sys.argv[1:],
  'message': """Hello,
This is my message.
To the world"""
}
print(json.dumps(send_message_back))
```

In Node, we add some JSON-parsing logic (using `JSON.parse`) in the `'exit'` handler.

A gotcha at this point is if, for example `JSON.parse()` fails due to badly-formed JSON, we need to propagate that error up. Hence the try/catch where the `catch` clause `reject`-s the potential error: `try { resolve(JSON.parse(out[0])) } catch(e) { reject(e) }`.

```js
const { spawn } = require('child_process')
const logOutput = (name) => (message) => console.log(`[${name}] ${message}`)
function run() {
  return new Promise((resolve, reject) => {
    const process = spawn('python', ['./script.py', 'my', 'args']);
    const out = []
    process.stdout.on(
      'data',
      (data) => {
        out.push(data.toString());
        logOutput('stdout')(data);
      }
    );
    const err = []
    process.stderr.on(
      'data',
      (data) => {
        err.push(data.toString());
        logOutput('stderr')(data);
      }
    );
   process.on('exit', (code, signal) => {
      logOutput('exit')(`${code} (${signal})`)
      if (code !== 0) {
        reject(new Error(err.join('\n')))
        return
      }
      try {
        resolve(JSON.parse(out[0]));
      } catch(e) {
        reject(e);
      }
    });
  });
}
(async () => {
  try {
    const output = await run()
    logOutput('main')(output.message)
    process.exit(0)
  } catch (e) {
    console.error('Error during script execution ', e.stack);
    process.exit(1);
  }
})();
```

Output:

```bash
node run.js
[stdout] {"message": "Hello,\nThis is my message.\n\nTo the world", "arguments": ["my", "args"]}
[main] Hello,
This is my message.
To the world
```

That’s it! Thanks for reading :)

I’ve got mentoring spots open at [https://mentorcruise.com/mentor/HugoDiFrancesco/](https://mentorcruise.com/mentor/HugoDiFrancesco/). Do that if you want Node.js/JavaScript/career mentoring or feel free to tweet at me [@hugo__df](https://twitter.com/hugo__df)

And read more of my articles on [codewithhugo.com](https://www.codewithhugo.com)

