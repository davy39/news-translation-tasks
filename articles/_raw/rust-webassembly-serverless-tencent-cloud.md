---
title: How to use Rust + WebAssembly to Perform Serverless Machine Learning and Data
  Visualization in the Cloud
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T16:26:16.000Z'
originalURL: https://freecodecamp.org/news/rust-webassembly-serverless-tencent-cloud
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/origin_img_6f483a12-6885-4499-b35b-2e23c949ef8g.PNG
tags:
- name: Machine Learning
  slug: machine-learning
- name: Rust
  slug: rust
- name: WebAssembly
  slug: webassembly
seo_title: null
seo_desc: 'The Tencent Serverless Cloud Function Custom Runtime allows developers
  to write serverless functions in any programming language.

  In this article, we make the case for serverless functions in Rust and WebAssembly,
  and demonstrate their use in machine...'
---

The Tencent Serverless Cloud Function Custom Runtime allows developers to write serverless functions in any programming language.

In this article, we make the case for serverless functions in Rust and WebAssembly, and demonstrate their use in machine learning and visualization.

You will learn how to create a simple function for machine learning and deploy a serverless web site around it, for free (unless a million people use it!).

## First, what is Tencent?

Tencent is the biggest Internet company outside of the USA with over a billion active daily users. Its cloud computing arm, [Tencent Cloud](https://cloud.tencent.com/?lang=en), is ranked among the top 5 cloud providers in the world by market share.

If you want to reach the world-wide market with your cloud services, Tencent Cloud should be near the top of your list.

Tencent Cloud is also a leading innovator in serverless computing with strong offerings ranging from Function as a Service (FaaS) runtimes, triggers, connectors, and developer tools.

The [Tencent Serverless Cloud Functions (SCF)](https://intl.cloud.tencent.com/document/product/583) already support 10+ programming languages and runtime frameworks. But the recently released SCF Custom Runtime took another step forward. The SCF can now support functions written in any programming language.

In this article, I will cover how to run WebAssembly functions, written in Rust, in the SCF.

### What we'll cover in this article

We will first go over the basic concepts. Then, we will review a complete but simple hello world example to deploy your first WebAssembly serverless function.

Finally, we will do something useful with a machine earning as a service (MLaaS) example that takes data and returns the fitted model and visualization in the SVG format.

[Here is the final application](https://www.secondstate.io/demo/2020-tencentcloud.html) you will create by the end of this tutorial. It is completely “serverless” and incurs cost when people use it.

The HTML and JavaScript UI can be hosted on any computer including your laptop, and the [backend function](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca) to perform machine learning and SVG drawing is on Tencent Cloud Serverless.

## Why WebAssembly and Rust

Traditional serverless functions are based on heavy-weight frameworks. Developers must write functions in specific application frameworks, such as JavaScript in Node.js or Python Boto and so on.

The Tencent Cloud SCF Custom Runtime breaks this mold, and allows developers to write serverless functions in any language.

To demonstrate this point, it provides examples for a [Bash script-based function](https://github.com/tencentyun/scf-demo-repo/tree/master/CustomRuntime-shellDemo), a [Deno-based TypeScript function](https://github.com/tencentyun/scf-demo-repo/tree/master/CustomRuntime-denoDemo), and a [Rust-based native binary function](https://github.com/tencentyun/scf-demo-repo/tree/master/CustomRuntime-rustDemo). That allows us to create and deploy WebAssembly-based serverless functions on Tencent Cloud.

Why do we want to do that? Here are [some reasons](https://www.secondstate.io/articles/why-webassembly-server/).

* WebAssembly is designed for performance. [WebAssembly functions could be 10x faster](https://www.secondstate.io/articles/performance-rust-wasm/) than comparable programs written in JavaScript or Python.
    
* WebAssembly functions are portable. While it is possible to run native binaries on SCF Custom Runtime, those binaries must be compiled to the exact operating system environment for Custom Runtime. It is currently CentOS 7.6 on X86 CPUs, and could change later. WebAssembly functions are portable and very easy to deploy and manage as we will see.
    
* WebAssembly functions are safe. It is known that even with Docker, native binary applications could breach the container. Since your application probably depends on many 3rd-party libraries, the risk for rogue code in your dependencies is real. WebAssembly, with its [capability-based security model](https://www.secondstate.io/articles/wasi-access-system-resources/), provides better runtime protection for your code.
    
* While WebAssembly is agnostic to programming languages, Rust, AssemblyScript (a subset of TypeScript), C/C++, and Go are among the best languages to write WebAssembly functions. In particular, Rust is a popular and fast rising programming language with a passionate community. It allows us to write highly efficient, yet memory safe, functions.
    

Finally, programming and deploy WebAssembly functions on Tencent Cloud is actually quite easy. You can do in it an hour. Let’s get started.

## Prerequisites

First, sign up for a [Tencent Cloud account](https://cloud.tencent.com/?lang=en). For most development and personal projects, you can probably staying within its [free tier](https://intl.cloud.tencent.com/document/product/583/12282) of service.

Then, on your local development computer or Docker container, make sure that you have Rust and [ssvmup](https://www.secondstate.io/articles/ssvmup/) toolchain installed. The ssvmup toolchain compiles and optimizes Rust programs into WebAssembly bytecode.

Just use the following simple commands to install both. Or you can refer to [this guide](https://www.secondstate.io/articles/ssvmup/).

```bash
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
$ source $HOME/.cargo/env
... ...
$ curl https://raw.githubusercontent.com/second-state/ssvmup/master/installer/init.sh -sSf | sh
```

The WebAssembly function is executed in the [Second State VM](https://www.secondstate.io/ssvm/) — a [high-performance WebAssembly VM](https://www.secondstate.io/articles/ssvm-performance/) optimized for server-side use cases and applications.

## Hello, world

To get started with your first Rust and WebAssembly function on Tencent Cloud, we encourage your to clone or [fork this template repository](https://github.com/second-state/ssvm-tencent-starter) on Github and use it as the basis for your own application.

The Rust function in [main.rs](https://github.com/second-state/ssvm-tencent-starter/blob/master/src/main.rs) is the serverless function we will deploy to SCF. As you can see from its source code, it reads the function’s input from `STDIN`, and then use the `println!` macro to send results to the `STDOUT`.

```rust
use std::io::{self, Read};
use serde::Deserialize;

fn main() {    
    let mut buffer = String::new();    
    io::stdin().read_to_string(&mut buffer).expect("Error reading from STDIN");    
    let obj: FaasInput = serde_json::from_str(&buffer).unwrap();    
    let key1 = &(obj.key1);    
    let key2 = &(obj.key2);    
    println!("Hello! {}, {}", key1, key2);
}

#[derive(Deserialize, Debug)]
struct FaasInput {    
    key1: String,    
    key2: String
}
```

The Rust `main()` function uses the `serde` library to parse a JSON string from `STDIN`.

The JSON looks like the following. The reason we write the function this way is because this is the built-in hello world JSON template SCF uses to test deployed functions.

```json
{  
    "key1": "test value 1",  
    "key2": "test value 2"
}
```

The function extracts the `key1` and `key2` values and outputs the following hello message to `STDOUT`.

```text
Hello! test value 1, test value 2
```

But, how does a web request to this function get translated into `STDIN`? And how does the function response in `STDOUT` get translated into a the HTTP response?

That is done by the SCF Custom Runtime infrastructure and the [bootstrap](https://github.com/second-state/ssvm-tencent-starter/blob/master/cloud/bootstrap) program in our template.

As you can see, the [bootstrap](https://github.com/second-state/ssvm-tencent-starter/blob/master/cloud/bootstrap) program is simply a bash shell program that continuously polls the SCF for incoming requests. It translates the incoming request to `STDIN` and calls the WebAssembly function through the SSVM. It then takes the `STDOUT` output and sends it back into SCF as the function’s response.

You do not need to modify the bootstrap program if you use our template.

Now, you can build the Rust function into WebAssembly bytecode with ssvmup, and then package a zip file for deployment on the Tencent Cloud SCF Custom Runtime.

```bash
$ ssvmup build
```

[Follow the instructions and screenshots](https://github.com/second-state/ssvm-tencent-starter/blob/master/README.md) to deploy and test the `hello.zip` file from above. Now you have successfully deployed a WebAssembly serverless function!

Next, let's create a useful web service from a Rust function.

## Machine Learning as a Service

For this example, we chose a computationally intensive machine learning task to demonstrate the performance of a Rust WebAssembly function.

The serverless function takes an input string of comma delimited numbers that represent a set of points on a 2-D plane. The input data format is `x1,y1,x2,y2,...`.

The function analyzes the data and computes two Eigenvectors that indicate the directions of the most variance in the data.

The Eigenvectors give data scientists hints on the underlying factors that drives the variance in the data. This is called Principal Component Analysis (PCA).

Our function creates a SVG graph with the input data points as well as the Eigenvectors plotted on it. It outputs the SVG graph in XML text.

To get started with this example, you should [clone or fork this repository](https://github.com/second-state/wasm-learning). The project is in the [tencentcloud/ssvm/pca](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca) folder. You can also copy the content of the [Cargo.toml](https://github.com/second-state/wasm-learning/blob/master/tencentcloud/ssvm/pca/Cargo.toml) and [src/](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca/src)[\*](http://main.rs)to your hello world template.

If you do the latter, make sure that you modify the [Cargo.toml](https://github.com/second-state/wasm-learning/blob/master/tencentcloud/ssvm/pca/Cargo.toml) to point to the correct source code folder for our Rust machine learning library.

I will not go into the details of the Rust source code for PCA or SVG generation in this tutorial as they involve a fair amount of computational code. If you are interested, you can check out more resources at the end of this article.

You can [follow the same process](https://github.com/second-state/ssvm-tencent-starter/blob/master/README.md) as in the hello world example. Use the ssvmup to build a `pca.zip` package and deploy it on Tencent Cloud SCF Custom Runtime.

Next, we want to associate the deployed function with a web API Gateway so that it can be invoked from a web HTTP or HTTPS request. Do that from the Trigger Management tab in the web console for SCF. [See the instructions and screenshots here](https://github.com/second-state/wasm-learning/tree/master/tencentcloud/ssvm/pca#create-a-web-service).

The API console turns an HTTP request into a JSON input to the serverless function. For example, here is an HTTP POST request to the API gateway URL. We put the comma delimited data points from the `iris.csv` file in the POST body.

```bash
$ curl -d @iris.csv -X POST https://service-m9pxktbc-1302315972.hk.apigw.tencentcs.com/release/PCASVG
```

The API Gateway passes the following JSON to the Rust function’s STDIN. The POST body is now the body attribute in the JSON.

```json
{
  "body": "3.5,0.2,3,0.2,...",
  "headerParameters": {},
  "headers": {
    "accept": "/",
    "content-length": "11",
    "content-type": "application/x-www-form-urlencoded",
    "host": "service-aj0plx8u-1302315972.hk.apigw.tencentcs.com",
    "user-agent": "curl/7.54.0",
    "x-anonymous-consumer": "true",
    "x-api-requestid": "e3123014742e7dd79f0652968bf1f62e",
    "x-b3-traceid": "e3123014742e7dd79f0652968bf1f62e",
    "x-qualifier": "$DEFAULT"
  },
  "httpMethod": "POST",
  "path": "/my_hk",
  "pathParameters": {},
  "queryString": {},
  "queryStringParameters": {},
  "requestContext": {
    "httpMethod": "ANY",
    "identity": {},
    "path": "/my_hk",
    "serviceId": "service-aj0plx8u",
    "sourceIp": "136.49.211.114",
    "stage": "release"
  }
}
```

The Rust function parses the data in the body, performs PCA, and generates the SVG graph. It prints the SVG content to STDOUT, which is picked up by the API Gateway and sent back as the HTTP response.

> To use this API Gateway URL in AJAX requests, you must also configure the Tencent Cloud gateway to accept CORS web requests. [Check out this guide](https://www.secondstate.io/articles/tencentcloud-api-gateway-cors/) on how to do it.

The HTML JavaScript example below shows how to use this serverless function in a web page.

It takes the CSV data from the `textarea` field with ID `csv_data`, makes an AJAX HTTP POST request to the serverless function, and then puts the return value, which is a SVG graph, in an HTML element with ID `svg_img`. [See the live demo here](https://www.secondstate.io/demo/2020-tencentcloud.html).

```javascript
$.ajax({
  method: "POST",
  url: "https://service-m9pxktbc-1302315972.hk.apigw.tencentcs.com/release/PCASVG",
  data: $('#csv_data').val(),
  dataType: "text"
}).done(function(data) {
  $('#svg_img').html(data);
})
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/tencentcloud_pca_webapp.png align="left")

*The serverless web application in action.*

## Next steps

The Tencent SCF Custom Runtime is a very powerful serverless environment. It provides a generic Linux environment for any application function you want to write, as well as standard web interfaces to interact with the function input and output. It is definitely worth trying out.

As discussed in the article, we believe that Rust and WebAssembly provides a [high performance, safe, portable, and future-proof stack](https://www.secondstate.io/articles/why-webassembly-server/) for serverless functions. Rust and WebAssembly with SCF Custom Runtime is the future!

## Resources

* Learn more about [why use WebAssembly on the server side](https://www.secondstate.io/articles/why-webassembly-server/)
    
* Learn more about [Tencent Serverless Cloud Functions](https://intl.cloud.tencent.com/document/product/583)
    
* [Learn more about machine learning algorithms](https://www.freecodecamp.org/news/a-no-code-intro-to-the-9-most-important-machine-learning-algorithms-today/)
    
* [Getting started with Rust](https://www.rust-lang.org/learn/get-started)
    
* [Machine learning algorithms in Rust and WebAssembly](https://github.com/second-state/wasm-learning/tree/master/nodejs/algos)
    
* [Getting started with Rust functions in Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/)
    
* Learn more about the [Second State WebAssembly VM](https://www.secondstate.io/ssvm/)
    

[Subscribe to our newsletter](https://webassemblytoday.substack.com/) and stay in touch. Happy coding!
