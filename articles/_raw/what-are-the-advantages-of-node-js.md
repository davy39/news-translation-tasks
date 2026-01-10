---
title: Node.js is a great runtime environment - and here's why you should use it
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2019-10-15T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-the-advantages-of-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/node-js-development-company.png
tags:
- name: node
  slug: node
- name: Node.js
  slug: nodejs
seo_title: null
seo_desc: 'An introduction to the scalable, extensible, easily available, self-sufficient,
  and highly effective runtime environment

  Node.js is a cross-platform runtime environment for JavaScript, which is free and
  open-sourced. It is full-stack, so it can be us...'
---

### An introduction to the scalable, extensible, easily available, self-sufficient, and highly effective runtime environment

Node.js is a cross-platform runtime environment for JavaScript, which is free and open-sourced. It is full-stack, so it can be used to develop both the client-side and the server-side of an application.

Who uses Node.js? Node.js is a popular tech stack choice for the companies developing online games, instant messengers, social media platforms, or video conferencing tools. It is perfectly suitable for real-time applications, which need the app data to be constantly updated.

Before I start listing the advantages of Node.js, I need to explain something. There is some terminology to clarify for all of us to be on the same page. If you are aware of these concepts, feel free to scroll them past down.

**Google’s V8 engine** is the engine that Node.js is implemented with. Initially, it was developed by Google and for Google. V8 was written in C++ and aimed to compile JS functions into machine code. The same engine is used by Google Chrome. It is known for impressively high speeds and constantly improved performance.

**Event-based model** stands for the process of detecting events as soon as they take place and dealing with them respectively. You can use Promises, Async/Await and callbacks for handling events. For example, this snippet presents handling the writing of csv files using the Promise event model.

```js
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const path = ‘logs.csv”;
const header = [ 
	{
		id: 'id',
		 title: 'id’
	}, 
	{
		id: 'message', 
		title: 'message'
	}, 
	{
		id: 'timestamp',
		title: 'timestamp'
	}
 ];
const data = [
	{ 'id': 0, 'message': 'message1', 'timestamp': 'localtime1' },
	 { 'id': 1, 'message': 'message2', 'timestamp': 'localtime2'  }, 
	{ 'id': 2, 'message': 'message3', 'timestamp': 'localtime3'  }
];
const csvWriter = createCsvWriter({ path, header }); 
csvWriter .writeRecords(data) .then(
	()=> console.log('The CSV file was written successfully!')
) .catch(
	err => console.error("Error: ", err)
);
```

**Non-blocking Input/Output request handling** is the way Node.js processes requests. Usually, code is executed sequentially. A request cannot be processed until the previous one is finished. In the non-blocking model, requests do not have to wait in a line. This way, the single threading in Node.js is the most effective, the request processing is concurring, and the response time is short.

[<ins>**npm**</ins>](https://www.npmjs.com/) is a Node.js package manager and an open marketplace for various JS tools. It is the largest software registry in the world. Currently, it features over 836,000 libraries.

So, why Node.js development? Let’s see what the benefits of Node.js are.

![2-min](https://images.ctfassets.net/6xhdtf1foerq/7pkyYu6RpM9XROSa83gdU4/edcef661f034d2094b987da2d0f50a79/2-min.png?fm=png&q=85&w=1000)

## JavaScript

**Node.js is JavaScript-based. JavaScript is one of the most popular and simplest coding languages in the IT world.** It is easy to learn for beginning developers. Even people without the knowledge of JavaScript but with some basic technical background can read and understand the code. 

More than that, the pool of JavaScript talents is large, so as a business owner, you have full freedom to choose the team to work with.

## Scalability

**Node.js applications are easily scalable both horizontally and vertically.** Horizontally, new nodes are easily added to the existing system. Vertically, additional resources can be easily added to the existing nodes. 

When developing an application with Node.js, you do not have to create a large monolithic core. Instead, you can develop a set of modules and microservices, each running in its own process. All these small services communicate with lightweight mechanisms and comprise your application. Adding an extra microservice is as simple as it can get. This way, the development process becomes much more flexible.

## Extensibility

**Among other advantages of Node.js, there is the opportunity to integrate it with a variety of useful tools.** Node.js can be easily customized and extended. 

It can be extended with built-in APIs for the development of HTTP or DNS servers. To facilitate front-end development with old versions of Node or browser, Node.js can be integrated with a JS compiler [<ins>Babel</ins>](https://babeljs.io/). 

For unit-testing, it works perfectly with, for example, Jasmine. For deployment monitoring and troubleshooting purposes, it works well with [<ins>Log.io</ins>](http://logio.org/). 

Such tools as [<ins>Migrat</ins>](https://github.com/naturalatlas/migrat), [<ins>PM2</ins>](http://pm2.keymetrics.io/), and [<ins>Webpack</ins>](https://webpack.github.io/) can be used for data migration, process management, and module bundling respectively. In addition, Node.js is expanded with such frameworks as [<ins>Express</ins>](https://keenethics.com/tech-back-end-express), Hapi, Meteor, Koa, Fastify, Nest, Restify and plenty of others.

## Availability

**Node.js is open-source. The creator has granted everyone a right to learn, develop, and distribute the technology for any purpose.** The Node.js environment is one hundred percent free. Ready-made modules, libs, and code samples are open-sourced, so you can configure your application easily and for free. The ability to learn to work with Node.js as also available to everyone willing to acquire this technology.

## Self-Sufficiency

**There are a lot of convenient repositories with various ready-made modules.** The default package manager npm also offers a variety of additional libraries and tools. These significantly facilitate the development process. 

Also, Node.js technology can be used to develop both front-end and back-end with the same language. You can work with the same team until the final product is implemented. It simplifies communication and spares you plenty of organizational tasks.

You can even use Node.js as a platform for Machine Learning and Artificial Intelligence training.

```js
const tf = require('@tensorflow/tfjs-node');
const trainData = [ 
	{ input: [-120, -100, -60, -40, -60, -80, -80, -60, -40, -60, -80, -100].map(value => Math.abs(value)), output: [1]},
	 { input: [-82, -63, -45, -55, -77, -98, -122, -90, -55, -44, -61, -78].map(value => Math.abs(value)), output: [0]}, 
.
.
.
	{ input: [-80, -60, -40, -60, -80, -100, -120, -100, -60, -40, -60, -80].map(value => Math.abs(value)), output: [0]}, 
];
const model = tf.sequential(); 
model.add(tf.layers.dense({inputShape: [12], units: 12, activation: 'sigmoid'})); model.add(tf.layers.dense({units: 1, activation: 'sigmoid'}));
const preparedData =  tf.tidy(() => { 
	tf.util.shuffle(arr); 
	const inputs = arr.map(d => d.input) 
	const outputs = arr.map(d => d.output); 
	const inputTensor = tf.tensor2d(inputs, [arr.length, arr[0].input.length]); 
	const labelTensor = tf.tensor2d(outputs, [arr.length, 1]); 
	const inputMax = inputTensor.max(); 
	const inputMin = inputTensor.min(); 
	const labelMax = labelTensor.max(); 
	const labelMin = labelTensor.min();
	 const normalizedInputs = inputTensor.sub(inputMin).div(inputMax.sub(inputMin)); 
const normalizedOutputs = labelTensor
return { 
	inputs: normalizedInputs, 
	outputs: normalizedOutputs, 
	inputMax, 
	inputMin, 
	labelMax, 
	labelMin, } 
});
model.compile({ 
	optimizer: tf.train.adam(), 
	loss: tf.losses.meanSquaredError, 
	metrics: ['mse'], 
});
 const batchSize = 32; 
const epochs = 50; 
const trainedModel = model.fit(inputs, outputs, { batchSize, epochs, shuffle: true, });
```

## Universality

**Node.js is cross-platform.** For instance, a Node.js developer can create a cross-platform desktop application for Windows, Linux, and Mac. What is more, Node.js is not only for mobile, desktop, and web development. The advantages of Node.js are actively applied in the development of cloud or IoT solutions.

## Simplicity

**Node.js has a low entry threshold.** It is quite simple to acquire for the people with knowledge of JavaScript. It is also necessary to point out that the low entry threshold directly translates in an overly large number of low-quality specialists.

## Automation

**Node.js grants the opportunity to automate repetitive operations, schedule actions, or share modification records.** Node.js automatically groups functions and keeps your code in order. Furthermore, there is an extensive built-in library of UI templates or ready-to-go functionality.

## High Performance, Speed, and Resource-Efficiency

**In Node.js, the JavaScript code is interpreted with the help of Google’s V8 JS engine.** Google invests heavily in its engine, so the performance is constantly improved. 

Node.js executes code outside a web browser, which greatly improves the performance and resource-efficiency of an application. Also, it allows using features that are not available for the browser, such as a direct file system API, TCP sockets etc. 

The code execution is speedy and several requests can be processed simultaneously since Node.js runtime environment supports the non-blocking event-driven input/output operations. Node.js also offers the feature of single module caching, which allows the application to load faster and be more responsive.

## Community Support

**Among the advantages of using Node.js, developers mention the global developer community.** There is an immense number of active developers who contribute to open-source, develop and support the framework, and share their learning insights or coding experience with others. 

Node.js is well-supported on GitHub, and it is more popular there than, for example, React. Moreover, such companies as IBM, PayPal, eBay, Microsoft, Netflix, Yahoo!, LinkedIn, or NASA support and actively use Node.js.

## However…

It would not be fair to list only the benefits of Node.js without mentioning the drawbacks of Node.js. Presenting a one-sided point of view is not a healthy practice. I want you to understand that no solution is perfect, and Node.js is no exception.

> _Repositories are extended, but sometimes, they resemble a landfill. There are a lot of unnecessary, overly complicated, or incomprehensible modules. The language has some confusing features, which are difficult to understand. Some modern libs and frameworks are overloaded. My takeaway is as follows: measure is a treasure. If you know well what you are working with and how to do it best, Node,js is the tool you need. Why do we use Node js? Because there are a lot of useful features, the code is easy to understand, and the solutions can be effective. Otherwise – oh well._

![Anton Trofimov](https://images.ctfassets.net/6xhdtf1foerq/7Jz1VOMAF9kEvEE2EJ8TP/b0c5375f900114f3fd91e53f77d8e63e/0?fm=jpg&fl=progressive&q=95&h=130&w=130&fit=crop&fit=thumb)
_Anton Trofimov, Full Stack Software Developer_

## Do you have an idea for a Node.js project?

My company KeenEthics is an experienced [Node.js development company](https://keenethics.com/services-web-development-node). In case you need a free estimate of a similar project, feel free to [get in touch](https://keenethics.com/contacts?activeForm=estimate)_._

If you have enjoyed the article, you should continue with [Node.js Inject: How to Conduct](https://keenethics.com/blog/1559196000000-node-js-inject) and [Why to Use or Express.js Security Tips](https://www.freecodecamp.org/news/express-js-security-tips/).

## P.S.

A huge shout-out to [Volodia Andrushchak](https://www.linkedin.com/in/andrushchak-volodia-167430125/) and [Anton Trofimov](https://www.linkedin.com/in/anton-trofimov-590974108/), full stack software developers @ KeenEthics for helping me with the article. 

The original article posted on KeenEthics blog can be found here: [What Are the Advantages of Node.JS?](https://keenethics.com/blog/what-are-the-advantages-of-node-js)

