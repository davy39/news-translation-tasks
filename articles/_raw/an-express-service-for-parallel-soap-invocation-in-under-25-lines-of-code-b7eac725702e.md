---
title: An Express service for parallel SOAP invocation in under 25 lines of code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-09T19:31:11.000Z'
originalURL: https://freecodecamp.org/news/an-express-service-for-parallel-soap-invocation-in-under-25-lines-of-code-b7eac725702e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gnvtnZJe9Ejl8x0oEE_Ufw.jpeg
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Felipe Ignacio Lazo Gallardo

  Overview

  Let’s suppose there is a service that has the following features:


  It exposes a REST endpoint receiving a list of requests.

  It in parallel invokes a SOAP service, once per element in the requests list.

  It retu...'
---

By Felipe Ignacio Lazo Gallardo

### Overview

Let’s suppose there is a service that has the following features:

1. It exposes a REST endpoint receiving a list of requests.
2. It in parallel invokes a SOAP service, once per element in the requests list.
3. It returns the converted result from XML to JSON.

That service’s source code could look something like this using Node.js, Express, and the [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript#airbnb-javascript-style-guide-):

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', (req, res) => (clientPromise.then(client => ({ client, requests: req.body }))
        .then(invokeOperations)
        .then(results => res.status(200).send(results))
        .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('Waiting for incoming requests.'));

const invokeOperations = ({ client, requests }) => (Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
))));
```

Sample request:

```
POST /parallel-soap-invoke
[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]
```

Sample response:

```
HTTP/1.1 200
[
  {
    "AddResult": 3
  },
  {
    "AddResult": 7
  },
  {
    "AddResult": 11
  }
]
```

Tests show that a single direct request to the SOAP service using SOAPUI takes ~430 ms (from where I’m located, in Chile). Sending three requests (as shown above) takes ~400 ms for calls to the Express service (other than the first one, which gets the WSDL and builds the client).

Why do more requests take less time? Mostly because the XML is not heavily validated as it is in regular SOAP, so if this soft validation doesn’t match your expectations, you should consider additional features or solutions.

Wondering how would it look using `async/await`? Here you go (results are the same):

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', async (req, res) => {
        try {
            res.status(200).send(await invokeOperations(await clientPromise, req.body));
        } catch ({message: error}) {
            res.status(500).send({ error });
        }
    })
    .listen(3000, () => console.log('Waiting for incoming requests.'));

const invokeOperations = (client, requests) => (Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
))));
```

The following image provides a concept of how the code works:

![Image](https://cdn-media-1.freecodecamp.org/images/1*WFN937ih5z83fc_gNqWVqw.png)

This article aims to show the simplicity of using JavaScript for tasks in enterprise World, such as invoking SOAP services. If you’re familiar with JavaScript, this is basically just a `Promise.all` on top of a couple of promisified callbacks under an Express endpoint. You can go directly to section 4 (**Bonus track**) if you think that could be useful for you.

If you’re outside the JavaScript world, I think that 24 lines of code for the three features I mentioned at the beginning are a very good deal. I’ll now go into the details.

### 1. The Express section

Let’s start with the code related to Express, a minimal and flexible Node.js web application framework. It’s quite simple and you can find it anywhere, so I’ll give a summarized description.

```js
'use strict';

 // Express framework.
const express = require('express');
// Creates an Express application.
const app = express();

/**
 * Creates a GET (which is defined by the method invoked on 'app') endpoint,
 * having 'parallel-soap-invoke' as entry point.
 * Each time a GET request arrives at '/parallel-soap-invoke', the function passed
 * as the second parameter from app.get will be invoked.
 * The signature is fixed: the request and response objects.
 */
app.get('/parallel-soap-invoke', (_, res) => {
    // HTTP status of the response is set first and then the result to be sent.
    res.status(200).send('Hello!');
});

// Starts 'app' and sends a message when it's ready.
app.listen(3000, () => console.log('Waiting for incoming requests.'));
```

Result:

```
GET /parallel-soap-invoke
HTTP/1.1 200
Hello!
```

Now we’ll need to handle an object sent through POST. Express `body-parser` allows easy access to the body of the request:

```js

'use strict';

const expressApp = require('express')(); // Compressing two lines into one.
const bodyParser = require('body-parser'); // Several parsers for HTTP requests.

expressApp.use(bodyParser.json()) // States that 'expressApp' will use JSON parser.
    // Since each Express method returns the updated object, methods can be chained.
    .post('/parallel-soap-invoke', (req, res) => { 
        /**
         * As an example, the same request body will be sent as response with
         * a different HTTP status code.
         */
        res.status(202).send(req.body); // req.body will have the parsed object 
    })
    .listen(3000, () => console.log('Waiting for incoming requests.'));
```

```
POST /parallel-soap-invoke
content-type: application/json

[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]

HTTP/1.1 202

[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]

```

So, long story short: setup the Express app, and as soon as you have the result, send it via `res` and voilà.

### 2. The SOAP section

This will have some more steps than the previous section. The main idea is that, for making SOAP invocations in parallel, I’ll use `Promise.all`. In able to use `Promise.all`, the invocation to the SOAP services needs to be handled within a Promise, which is not the case for `strong-soap`. This section will show how to convert the regular callbacks from `strong-soap` into Promises and then putting a `Promise.all` on top of that.

The following code will use the most basic example from `strong-soap`’s [documentation](https://github.com/strongloop/strong-soap#client). I’ll just simplify it a bit and use the same WSDL we’ve been seeing (I didn’t use the same WSDL stated in `strong-soap`’s documentation, since that WSDL is not working anymore):

```js
'use strict';

// The SOAP client library.
var { soap } = require('strong-soap');
// WSDL we'll be using through the article.
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

// Hardcoded request
var requestArgs = {
    "intA": 1,
    "intB": 2,
};

// Creates the client which is returned in the callback.
soap.createClient(url, {}, (_, client) => (
    // Callback delivers the result of the SOAP invokation.
    client.Add(requestArgs, (_, result) => (
        console.log(`Result: ${"\n" + JSON.stringify(result)}`)
    ))
));
```

```
$ node index.js
Result:
{"AddResult":3}
```

I’ll convert this into Promises and I’ll go through all callbacks, one by one, for the sake of the example. That way the translation process will be crystal clear for you:

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

/**
 * A function that will return a Promise which will return the SOAP client.
 * The Promise receives as parameter a function having two functions as parameters:
 * resolve & reject.
 * So, as soon as you got a result, call resolve with the result,
 * or call reject with some error otherwise.
 */
const createClient = () => (new Promise((resolve, reject) => (
    // Same call as before, but I'm naming the error parameter since I'll use it.
    soap.createClient(url, {}, (err, client) => (
        /**
         * Did any error happen? Let's call reject and send the error.
         * No? OK, let's call resolve sending the result. 
         */
        err ? reject(err) : resolve(client)
    ))))
);

/**
 * The above function is invoked.
 * The Promise could have been inlined here, but it's more understandable this way.
 */
createClient().then(
    /**
     * If at runtime resolve is invoked, the value sent through resolve
     * will be passed as parameter for this function.
     */
    client => (client.Add(requestArgs, (_, result) => (
        console.log(`Result: ${"\n" + JSON.stringify(result)}`)
    ))),
    // Same as above, but in this case reject was called at runtime.
    err => console.log(err),
);
```

Calling `node index.js`gets the same result as before. Next callback:

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

const createClient = () => (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => (
        err ? reject(err) : resolve(client)
    ))))
);

/**
 * Same as before: do everything you need to do; once you have a result,
 * resolve it, or reject some error otherwise.
 * invokeOperation will replace the first function of .then from the former example,
 * so the signatures must match.
 */
const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

/**
 * .then also returns a Promise, having as result the value resolved or rejected
 * by the functions that were passed as parameters to it. In this case, the second .then
 * will receive the value resolved/rejected by invokeOperation.
 */
createClient().then(
    invokeOperation,
    err => console.log(err),
).then(
    result => console.log(`Result: ${"\n" + JSON.stringify(result)}`),
    err => console.log(err),
);
```

`node index.js`? Still the same. Let’s wrap those Promises in a function, in order to prepare the code for calling it inside the Express endpoint. It also simplifies the error handling a bit:

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

const createClient = () => (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => (
        err ? reject(err) : resolve(client)
    ))))
);

const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

const processRequest = () => createClient().then(invokeOperation);

/**
 * .catch() will handle any reject not handled by a .then. In this case,
 * it will handle any reject called by createClient or invokeOperation.
 */
processRequest().then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

I bet you can guess the result of `node index.js`.

What happens if several subsequent calls are made? We’ll find out with the following code:

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

const createClient = () => (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => {
        if (err) {
            reject(err);
        } else {
            // A message is displayed each time a client is created.
            console.log('A new client is being created.');
            resolve(client);
        }
    })))
);

const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

const processRequest = () => createClient().then(invokeOperation)

processRequest().then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
processRequest().then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
processRequest().then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

```
$ node index.js
A new client is being created.
A new client is being created.
Result:
{"AddResult":3}
A new client is being created.
Result:
{"AddResult":3}
Result:
{"AddResult":3}
```

Not good, as several clients are being created. Ideally, the client should be cached and reused. There are two main ways to achieve this:

1. You can create a variable outside the Promise and cache the client as soon as you have it (just before resolving it). Let’s call this `cachedClient`. But, in that case, you’d have to manually deal with calls to `createClient()` made between the first time it is called and before the first client is resolved. You’d have to inspect if `cachedClient` is the expected value, or you’d have to check if the Promise is resolved or not, or you’d have to put some kind of event emitter to know when the `cachedClient` is ready. The first time I wrote code for this, I used this approach and I ended up living with the fact that every single call made before the first `createClient().resolve` overwrote `cachedClient`. If the problem is not that clear, let me know and I’ll write the code and the examples.
2. Promises have a very cool feature ([see MDN documentation, “Return value” section](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)): if you call `.then()` on a resolved/rejected Promise, it will return the very same value that was resolved/rejected, without processing again. In fact, very technically, it will be the very same object reference.

The second approach is much simpler to implement, so the related code is the following:

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

var requestArgs = {
    "intA": 1,
    "intB": 2,
};

// createClient function is removed.
const clientPromise = (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => {
        if (err) {
            reject(err);
        } else {
            console.log('A new client is being created.');
            resolve(client);
        }
    })))
);

const invokeOperation = client => (new Promise((resolve, reject) => (
    client.Add(requestArgs, (err, result) => (
        err ? reject(err) : resolve(result)
    ))
)));

// clientPromise is called instead getClient().
clientPromise.then(invokeOperation)
    .then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
clientPromise.then(invokeOperation)
    .then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
clientPromise.then(invokeOperation)
    .then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

```
$ node index.js
A new client is being created.
Result:
{"AddResult":3}
Result:
{"AddResult":3}
Result:
{"AddResult":3}
```

Finally for this section, let’s make the code handle several parallel calls. This will be easy:

1. For handling several parallel calls, we’ll need `Promise.all`.
2. `Promise.all` has a single parameter: an array of Promises. So we’ll be converting the list of requests into a list of Promises. The code currently converts a single request into a single Promise (`invokeOperation`), so the code just needs a `.map` to achieve this.

```js
'use strict';

var { soap } = require('strong-soap');
var url = 'http://www.dneonline.com/calculator.asmx?WSDL';

// Hardcoded list of requests.
var requestsArgs = [
    {
        "intA": 1,
        "intB": 2,
    },
    {
        "intA": 3,
        "intB": 4,
    },
    {
        "intA": 5,
        "intB": 6,
    },
];

const clientPromise = (new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(error) : resolve(client))
)));

// Promise.all on top of everything.
const invokeOperation = client => (Promise.all(
    // For each request, a Promise is returned.
    requestsArgs.map(requestArgs => new Promise((resolve, reject) => (
        // Everything remains the same here.
        client.Add(requestArgs, (err, result) => (
            err ? reject(err) : resolve(result)
        ))
    )))
));

clientPromise.then(invokeOperation)
    .then(result => console.log(`Result: ${"\n" + JSON.stringify(result)}`))
    .catch(({ message }) => console.log(message));
```

```
$ node index.js
Result:
[{"AddResult":3},{"AddResult":7},{"AddResult":11}]
```

### 3. Putting it all together

This is fairly easy — it’s just assembling the last code from each previous section:

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', (req, res) => (clientPromise.then(invokeOperations)
        .then(results => res.status(200).send(results))
        .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('Waiting for incoming requests.'));

// Adding req.body instead of hardcoded requests.
const invokeOperations = client => Promise.all(req.body.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
)));
```

```
POST /parallel-soap-invoke

[
  {
    "intA": 1,
    "intB": 2
  },
  {
    "intA": 3,
    "intB": 4
  },
  {
    "intA": 5,
    "intB": 6
  }
]
 
HTTP/1.1 500

{
  "error": "req is not defined"
}
```

Hmmm… Not a good result, since I did not expect an error at all. The problem is that `invokeOperations` doesn’t have `req` in its scope. The first thought could be “Just add it to the signature.” But that’s not possible, as that signature matches the result from the previous Promise, and that promise doesn’t return `req`, it only returns `client`. But, what if we add an intermediate Promise whose only purpose is injecting this value?

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const url = 'http://www.dneonline.com/calculator.asmx?WSDL';
const clientPromise = new Promise((resolve, reject) => (
    soap.createClient(url, {}, (err, client) => err ? reject(err) : resolve(client))
));

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', (req, res) => (
        /**
         * After clientPromise.then, where client is received, a new Promise is
         * created, and that Promise will resolve an object having two properties:
         * client and requests.
         */
        clientPromise.then(client => ({ client, requests: req.body }))
            .then(invokeOperations)
            .then(results => res.status(200).send(results))
            .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('Waiting for incoming requests.'));

/**
 * Since the shape of the object passed to invokeOperations changed, the signature has
 * to change to reflect the shape of the new object.
 */
const invokeOperations = ({ client, requests }) => Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client.Add(request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
)));
```

The results are exactly the same as the ones at the summary.

### 4. Bonus track

A generic SOAP to JSON converter for parallel SOAP invoking. The code is familiar, based on what you saw in the former sections. How about that?

```js
'use strict';

const { soap } = require('strong-soap');
const expressApp = require('express')();
const bodyParser = require('body-parser');

const clientPromises = new Map();

expressApp.use(bodyParser.json())
    .post('/parallel-soap-invoke', ({ body: { wsdlUrl, operation, requests } }, res) => (
        getClient(wsdlUrl).then(client => ({ client, operation, requests }))
            .then(invokeOperations)
            .then(results => res.status(200).send(results))
            .catch(({ message: error }) => res.status(500).send({ error }))
    ))
    .listen(3000, () => console.log('Waiting for incoming requests.'));

const getClient = wsdlUrl => clientPromises.get(wsdlUrl)
    || (clientPromises.set(wsdlUrl, new Promise((resolve, reject) => (
        soap.createClient(wsdlUrl, {}, (err, client) => err ? reject(err) : resolve(client))
    ))).get(wsdlUrl));

const invokeOperations = ({ client, operation, requests }) => (Promise.all(requests.map(request => (
    new Promise((resolve, reject) => client[operation](request, (err, result) => (
        err ? reject(err) : resolve(result))
    ))
))));
```

First use example:

```
POST /parallel-soap-invoke
content-type: application/json

{
  "wsdlUrl": "http://www.dneonline.com/calculator.asmx?WSDL",
  "operation": "Add",
  "requests": [
    {
      "intA": 1,
      "intB": 2
    },
    {
      "intA": 3,
      "intB": 4
    },
    {
      "intA": 5,
      "intB": 6
    }
  ]
}

HTTP/1.1 200

[
  {
    "AddResult": 3
  },
  {
    "AddResult": 7
  },
  {
    "AddResult": 11
  }
]

```

Second use example:

```
POST /parallel-soap-invoke
content-type: application/json

{
  "wsdlUrl": "http://ws.cdyne.com/ip2geo/ip2geo.asmx?wsdl",
  "operation": "ResolveIP",
  "requests": [
    {
      "ipAddress": "8.8.8.8",
      "licenseKey": ""
    },
    {
    	"ipAddress": "8.8.4.4",
    	"licenseKey": ""
    }
  ]
}

HTTP/1.1 200

[
  {
    "ResolveIPResult": {
      "Country": "United States",
      "Latitude": 37.75101,
      "Longitude": -97.822,
      "AreaCode": "0",
      "HasDaylightSavings": false,
      "Certainty": 90,
      "CountryCode": "US"
    }
  },
  {
    "ResolveIPResult": {
      "Country": "United States",
      "Latitude": 37.75101,
      "Longitude": -97.822,
      "AreaCode": "0",
      "HasDaylightSavings": false,
      "Certainty": 90,
      "CountryCode": "US"
    }
  }
]
```

Are you going through [Digital Decoupling](https://www.accenture.com/t00010101T000000__w__/nz-en/_acnmedia/Accenture/Conversion-Assets/DotCom/Documents/Global/PDF/Digital_2/Accenture-Digital-Decoupling.pdf)? In a JavaScript full-stack architecture on top of the old services, this artifact could help you encapsulate all SOAP services, extend them, and expose only JSON. You could even modify this code a bit to call several different SOAP services at the same time (that should be just an additional `.map` and `.reduce`, as I see it right now). Or you could encapsulate your enterprise’s WSDLs in a database and invoke them based on a code or some identifier. That would be just one or two additional promises to the chain.

