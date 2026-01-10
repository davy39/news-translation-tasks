---
title: All you need to know about Go version 1.11
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T09:48:15.000Z'
originalURL: https://freecodecamp.org/news/all-you-need-to-know-about-go-1-11-webassembly-modules-and-major-changes-df6a02108373
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZhP-Sh-b9W-Y4IeI84prkw.png
tags:
- name: Go Language
  slug: go
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: WebAssembly
  slug: webassembly
seo_title: null
seo_desc: 'By Ridham Tarpara

  Go 1.11 hit the ground on 24 August 2018. It introduces a few really needed tools
  and components such as versioned modules, WebAssembly support, and debugging improvements.
  It also brings some changes to core packages and performanc...'
---

By Ridham Tarpara

Go 1.11 hit the ground on 24 August 2018. It introduces a few really needed tools and components such as versioned modules, WebAssembly support, and debugging improvements. It also brings some changes to core packages and performance/run-time.

As always, the release maintains the Go 1 [promise of compatibility](https://golang.org/doc/go1compat.html). So almost all Go programs continue to compile and run as before with this update. There are no changes to the language specification.

Let’s take a look at what’s new.

### **Modules**

Go 1.11 includes experimental support for Go modules, including a new module-aware `go get` command.

The quickest way to take advantage of the new module support is to check out your repository into a directory **outside,** create a go.mod file and run Go commands from within that file tree.

Let’s demo this. I am using the [testify-powerful and standard Go testing libraries](https://github.com/stretchr/testify).

Let’s clone the testify repo in my favorite folder `~/proj/github` .

```
$ git clone https://github.com/stretchr/testify ~/proj/github/testify$ cd ~/proj/github/testify
```

Now, to use Go commands from here, you need to initialize this repo as a module with the following command:

```
go mod init github.com/stretchr/testify
```

Where `github.com/stretchr/testify` is the location you would generally put this repo, under the Go src folder.

This command will create a go.mod file in the root of the folder. In a project already using an existing dependency management tool like godep, glide, or dep, `go mod init` will also add require statements matching the existing configuration.

Now if you open the `go.mod` file, you can see the list of dependencies with the module name.

```
$ vi go.mod
```

```
module github.com/stretchr/testify
```

```
require (    github.com/davecgh/go-spew v1.1.0    github.com/pmezard/go-difflib v1.0.0    github.com/stretchr/objx v0.1.0)
```

As you’ll notice, these three are the dependencies of the testify. This is testify’s `Gopkg.toml` file:

```
[prune] unused-packages = true non-go = true go-tests = true
```

```
[[constraint]] name = “github.com/davecgh/go-spew” version = “~1.1.0”
```

```
[[constraint]] name = “github.com/pmezard/go-difflib” version = “~1.0.0”
```

```
[[constraint]] name = “github.com/stretchr/objx” version = “~0.1.0”
```

Now that the module has been initialized, you can use any Go command from this folder.

```
╭─ ~/proj/github/testify  ‹master*› ╰─$ go build                               go: finding github.com/davecgh/go-spew v1.1.0go: finding github.com/pmezard/go-difflib v1.0.0go: finding github.com/stretchr/objx v0.1.0go: downloading github.com/davecgh/go-spew v1.1.0go: downloading github.com/pmezard/go-difflib v1.0.0go: downloading github.com/stretchr/objx v0.1.0
```

```
╭─ ~/proj/github/testify  ‹master*› ╰─$ go test PASSok   github.com/stretchr/testify 0.001s
```

So with Go 1.11 and modules, you can write your Go modules _anywhere you like and you don’t need to maintain a copy_ in a specific sub directory of your `$GOPATH`.

### WebAssembly

Go 1.11 adds an experimental port to WebAssembly.

> WebAssembly (abbreviated _Wasm_) is a binary instruction format for a stack-based virtual machine. Wasm is designed as a portable target for compilation of high-level languages like C/C++/Rust, enabling deployment on the web for client and server applications.

Now we can run Go in the browser, and vice versa — we can run JavaScript in Go easily. Although this feature is in the experimental state, it’s still pretty useful.

This small example calls Go from the Web:

**wasm-exec.html**

```
<!doctype html><!--Copyright 2018 The Go Authors. All rights reserved.Use of this source code is governed by a BSD-stylelicense that can be found in the LICENSE file.--><html>
```

```
<head>    <meta charset="utf-8">    <title>Go wasm</title></head>
```

```
<body>    <script src="wasm_exec.js"></script>    <script>        if (!WebAssembly.instantiateStreaming) { // polyfill            WebAssembly.instantiateStreaming = async (resp, importObject) => {                const source = await (await resp).arrayBuffer();                return await WebAssembly.instantiate(source, importObject);            };        }        const go = new Go();        let mod, inst;        WebAssembly.instantiateStreaming(fetch("test.wasm"), go.importObject).then((result) => {            mod = result.module;            inst = result.instance;            document.getElementById("runButton").disabled = false;        });        let printMessage // Our reference to the Go callback        let printMessageReceived // Our promise        let resolvePrintMessageReceived // Our promise resolver        function setPrintMessage(callback) {          printMessage = callback          resolvePrintMessageReceived()        }        async function run() {          console.clear()          // Create the Promise and store its resolve function          printMessageReceived = new Promise(resolve => {            resolvePrintMessageReceived = resolve          })          const run = go.run(inst) // Start the wasm binary          await printMessageReceived // Wait for the callback reception          printMessage('Hello Wasm!') // Invoke the callback          await run // Wait for the binary to terminate          inst = await WebAssembly.instantiate(mod, go.importObject) // reset instance        }    </script>
```

```
<button onClick="run();" id="runButton" disabled>Run</button></body>
```

```
</html>
```

**go-call.go**

```
package main
```

```
import (  "fmt"  "syscall/js")
```

```
var done = make(chan struct{})
```

```
func main() {  callback := js.NewCallback(printMessage)  defer callback.Release() // To defer the callback releasing is a good practice  setPrintMessage := js.Global().Get("setPrintMessage")  setPrintMessage.Invoke(callback)  <-done}
```

```
func printMessage(args []js.Value) {  message := args[0].String()  fmt.Println(message)  done <- struct{}{} // Notify printMessage has been called}
```

You can find more examples [here](https://github.com/nlepage/golang-wasm/blob/master/examples). And here is a video on [building a calculator with WebAssembly](https://www.youtube.com/watch?v=4kBvvk2Bzis&feature=youtu.be).

### **Other changes to consider**

* Because Go module support assigns special meaning to the `@` symbol in command line operations, the `go`command now disallows the use of import paths containing `@` symbols.
* With the new `runtime/trace` package's [user annotation API](https://golang.org/pkg/runtime/trace/#hdr-User_annotation), users can record application-level information in execution traces and create groups of related goroutines. The `go` `tool` `trace` command visualizes this information in the trace view and the new user task/region analysis page.
* The runtime now uses a sparse heap layout so there is no longer a limit to the size of the Go heap (previously, the limit was 512GiB). This also fixes rare “address space conflict” failures in mixed Go/C binaries or binaries compiled with `-race`.
* [time](https://golang.org/pkg/time/): Parsing of timezones denoted by sign and offset is now supported. In previous versions, numeric timezone names (such as `+03`) were not considered valid, and only three-letter abbreviations (such as `MST`) were accepted when expecting a timezone name.
* [text/scanner](https://golang.org/pkg/text/scanner/): The `[Scanner.Scan](https://golang.org/pkg/text/scanner/#Scanner.Scan)` method now returns the `[RawString](https://golang.org/pkg/text/scanner/#RawString)` token instead of `[String](https://golang.org/pkg/text/scanner/#String)` for raw string literals.
* There are changes in [crypto](https://golang.org/pkg/crypto/), [encoding](https://golang.org/pkg/encoding/), [net/http](https://golang.org/pkg/net/http/), [os](https://golang.org/pkg/os/), [runtime](https://golang.org/pkg/runtime/), [sync](https://golang.org/pkg/sync/), [mime](https://golang.org/pkg/mime/) and few others which you can read about [here](https://golang.org/doc/go1.11#library).

If you enjoyed this article, spare me some claps — it means the world to the writer. Follow me if you want to read more articles about Go, JavaScript, Technology, and Startups.

