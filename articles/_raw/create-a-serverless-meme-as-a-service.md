---
title: How to Create a Serverless Meme-as-a-Service
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2021-02-25T15:54:07.000Z'
originalURL: https://freecodecamp.org/news/create-a-serverless-meme-as-a-service
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/meme1.png
tags: []
seo_title: null
seo_desc: 'The “meme economy” is apparently the next big thing. It is a natural extension
  of the Internet’s “attention economy”. Among many others, even Elon Musk is doing
  it. By some estimate, the meme economy is already worth $250 million USD.


  The meme econo...'
---

The “meme economy” is apparently the next big thing. It is a natural extension of the Internet’s “attention economy”. Among [many others](https://www.bloomberg.com/press-releases/2021-02-23/sino-global-shipping-partners-up-with-cybermiles-blockchain-to-explore-non-fungible-token-business), even [Elon Musk is doing it](https://www.axios.com/meme-economy-tesla-elon-musk-c1e9c225-d8e2-4953-a591-0a29dacf2d4a.html). By some estimate, the meme economy is already worth [$250 million USD](https://news.bitcoin.com/blockchain-backed-nft-market-value-grew-299-in-2020/).

> The meme economy is where FOMO meets YOLO. — Felix Salmon from AXIOS

However, it takes time to create a meme. How about a web app that allows anyone to customize a meme and generate a new one? [That is a meme-as-a-service (MaaS)!](https://sls-website-ap-hongkong-hmtn9c-1302315972.cos-website.ap-hongkong.myqcloud.com/)

## Why Serverless?

As a developer, it is probably not difficult to create a web application that adds text captions to images. However, a meme-as-a-service has some additional requirements.

* The imaging processing task is often computationally intensive and requires high performance.
    
* The meme service can see very little use or it could explode in popularity. In other words, it needs to be scalable and the developer only pays for actual use.
    

There are solutions to the above issues. First, we will use a modern high-performance programming language to write the image and text manipulation function. We'll use Rust for this purpose, which delivers native performance but with memory safety.

Next, we can best address the scalability requirement with a serverless function in a public cloud. A serverless function is free when it is not used and can quickly scale to millions of users.

While it is possible to run a native program compiled from Rust as a serverless function, a better way is to run the Rust program in a WebAssembly VM as a serverless function.

The WebAssembly VM acts as a compatibility layer and the security sandbox between the native application and the serverless host environment. It allows the Rust program to be more portable as the WebAssembly VM is pre-configured to run in a variety of operating systems and container images required by public cloud serverless runtimes.

In addition, WebAssembly makes it easy for Rust programs to securely access software libraries written in C/C++. An example is to [access Tensorflow libraries in legacy operating systems from Rust](https://www.secondstate.io/articles/wasi-tensorflow/).

## Quick start

In this tutorial, we will use [a template project on GitHub](https://github.com/second-state/tencent-meme-scf) to deploy our Rust meme-as-a-service on Tencent Cloud. The template is based on the open source Serverless Framework.

The Rust program compiles to and runs on the Second State VM (SSVM), which is a WebAssembly VM optimized to run in cloud-based host environments.

> While we use Tencent Cloud in this example, the Serverless Framework is agnostic to all leading public clouds. You can easily deploy to AWS or Azure with minor changes.

First, you will need to [install the Serverless Framework](https://www.serverless.com/framework/docs/getting-started/) and create a free account on [Tencent Cloud](https://cloud.tencent.com/). Next, fork or clone the [template GitHub repo](https://github.com/second-state/tencent-meme-scf) and then cd into its directory.

```bash
$ git clone https://github.com/second-state/tencent-meme-scf
$ cd tencent-meme-scf
```

You can now use the Serverless Framework to deploy the cloud function, an API gateway for the function service, and a static HTML page that uses the function service. It is configured to deploy to Tencent Cloud in the `.env` file.

Just follow the on screen instructions to log into Tencent Cloud and deploy.

```bash
$ sls deploy
... ...
  website:       https://sls-website-ap-hongkong-kfdilz-1302315972.cos-website.ap-hongkong.myqcloud.com
  vendorMessage: null

63s › tencent-meme-scf › "deploy" ran for 3 apps successfully.
```

Load the `website` URL in a browser to see your deployed [meme-as-a-service in action](https://sls-website-ap-hongkong-hmtn9c-1302315972.cos-website.ap-hongkong.myqcloud.com/)! It allows you to customize the text, position, and size for each piece of caption / watermark on the meme picture.

## How the application works

The overall architecture of the application is a typical JAMStack app. The backend logic for image processing is deployed as a serverless function, and is available via an API.

The front end UI is a static HTML and JavaScript web page. The front end interacts with the backend API through JavaScript Ajax calls.

The backend serverless function for adding captions (or watermarks) to the meme background image is written in Rust in the [main.rs](https://github.com/second-state/tencent-meme-scf/blob/main/src/main.rs) file. It first reads the font file for the watermark text and the background image file.

It then reads the input from the user application that specifies the text, position, and size of each watermark. The input is in the form of JSON text, and it is parsed into an array of Rust structs using the `serde_json` library.

The `_watermark()` function adds each watermark to the image. The function outputs the final image and base64 encodes it. The serverless runtime’s API gateway returns the base64 encoded image to the calling JavaScript to be displayed on the web page.

```rust
const FONT_FILE : &[u8] = include_bytes!("PingFang-Bold.ttf") as &[u8];
const TEMPLATE_BUF : &[u8] = include_bytes!("bg.png") as &[u8];

fn main() {
  let mut buffer = String::new();
  io::stdin().read_to_string(&mut buffer).expect("Error reading from STDIN");
  let obj: FaasInput = serde_json::from_str(&buffer).unwrap();

  let mut img = image::load_from_memory(TEMPLATE_BUF).unwrap();

  let memes: Vec<Watermark> = serde_json::from_str(&(obj.body)).unwrap();
  for m in memes {
    _watermark(m, &mut img);
  }

  let mut buf = vec![];
  img.write_to(&mut buf, image::ImageOutputFormat::Png).unwrap();
  println!("{}", base64::encode_config(buf, base64::STANDARD));
}
```

The `_watermark()` function adds a piece of watermark text to the image. It utilizes the standard Rust image processing libraries (known as crates) to manipulate the meme image.

```rust
fn _watermark(w: Watermark, img: &mut image::DynamicImage) {
  let font_size = w.font_size;

  let font = Vec::from(FONT_FILE);
  let font = Font::try_from_vec(font).unwrap();

  let scale = Scale {
    x: font_size,
    y: font_size,
  };
  drawing::draw_text_mut(img, image::Rgba([0u8, 0u8, 0u8, 255u8]), w.left, w.top, scale, &font, &w.text);
}
```

The frontend JavaScript takes the user input text, position, and font size from the HTML form, submits the input data in JSON to the cloud function, and then displays the returned base64 image.

```javascript
var memes = [];
memes[0] = {};
memes[0].text = $('#top-says').val();
memes[0].left = parseInt($('#top-left').val());
memes[0].top = parseInt($('#top-top').val());
memes[0].font_size = parseInt($('#top-font').val());
... ...

$.ajax({
  url: window.env.API_URL,
  type: "post",
  data : JSON.stringify(memes),
  dataType: "text",
  success: function (data) {
    const img_url = "data:image/png;base64," + data;
    $('#wm_img').prop('src', img_url);
  },
  error: function(jqXHR, exception){
    console.log("Error Status: " + jqXHR.statusText);
  }
});
```

## Build your own meme-as-a-service

With the source code template, you can create your own meme-as-a-service. You can change the meme background image, and change the UI for adding text watermarks.

To do that, first make sure that you have installed the [Rust](https://www.rust-lang.org/tools/install) compiler and [ssvmup](https://www.secondstate.io/articles/ssvmup/) build tools.

Make changes to the Rust code and the HTML document. Compile the Rust function to WebAssembly, and copy the result to the `scf/` folder.

```bash
$ ssvmup build --enable-aot
$ cp pkg/scf.so scf/
```

Run the serverless framework command to deploy the application.

```bash
$ sls deploy
... ...
  website:       https://sls-website-ap-hongkong-kfdilz-1302315972.cos-website.ap-hongkong.myqcloud.com
  vendorMessage: null

63s › tencent-meme-scf › "deploy" ran for 3 apps successfully.
```

## What’s next

Now that you have created and published your own meme-as-a-service, congratulations!

There is much more you can do with the JAMStack application and serverless functions. For example, you can create serverless functions for Tensorflow inference to incorporate advanced image recognition and processing to your application.
