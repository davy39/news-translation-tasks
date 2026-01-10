---
title: Just how expensive is the full AWS SDK?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-23T15:07:36.000Z'
originalURL: https://freecodecamp.org/news/just-how-expensive-is-the-full-aws-sdk-3713fed4fe70
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xFEOPesnxHTgZFBGzwQ6Kg.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud
  slug: cloud
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Yan Cui

  If you’re not familiar with how cold start works within the context of AWS Lambda,
  then read this post first.

  When a Node.js Lambda function cold starts, a number of things happen:


  the Lambda service has to find a server with enough capac...'
---

By Yan Cui

_If you’re not familiar with how cold start works within the context of AWS Lambda, then read [this post](https://theburningmonk.com/2018/01/im-afraid-youre-thinking-about-aws-lambda-cold-starts-all-wrong/) first._

When a Node.js Lambda function cold starts, a number of things happen:

* the Lambda service has to find a server with enough capacity to host the new container
* the new container is initialized
* the Node.js runtime is initialized
* your handler module is initialized, which includes initializing any global variables and functions you declare outside the handler function

If you enable active tracing for a Lambda function, you will be able to see how much time is spent on these steps in X-Ray. Unfortunately, the time it takes to initialize the container and the Node.js runtime are not recorded as segments. But you can work out from the difference in duration.

Here, `Initialization` refers to the time it takes to initialize the handler module.

![Image](https://cdn-media-1.freecodecamp.org/images/oJHJ0JDLY-CfzclwpKjswAorw17pnVNoP26N)

The above trace is for the function below, which requires the AWS SDK and nothing else. As you can see, this simple `require` added 147ms to the cold start.

```
const AWS = require('aws-sdk')module.exports.handler = async () => {}
```

Consider this the cost of doing business when your function needs to interact with AWS resources. But, if you only need to interact with one service (e.g. DynamoDB), you can save some initialization time with this one-liner.

```
const DynamoDB = require('aws-sdk/clients/dynamodb') const documentClient = new DynamoDB.DocumentClient()
```

It requires the DynamoDB client directly without initializing the whole AWS SDK. I ran an experiment to see how much cold start time you can save with this simple change.

_Credit goes to my colleague [**Justin Caldicott**](https://www.linkedin.com/in/justin-caldicott-96b36a9/) for piquing my interest and doing a lot of the initial analysis._

In addition to the AWS SDK, we often require the XRay SDK too and use it to auto-instrument the AWS SDK. Unfortunately, the `aws-xray-sdk` package also has some additional baggage that we don’t need. By default, it supports Express.js apps, MySQL and Postgres. If you are only interested in instrumenting the AWS SDK and `http`/`https` modules then you only need the `aws-xray-sdk-core`.

![Image](https://cdn-media-1.freecodecamp.org/images/oA2OPpll77iNxdSt70GgZsvjww92JXt44144)

### Methodology

I tested a number of configurations:

* [no AWS SDK](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/no-aws-sdk.js)
* [requiring only the DynamoDB client](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/dynamodb-only.js)
* [requiring the full AWS SDK](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-sdk.js)
* [requiring the XRay SDK only (no AWS SDK)](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-xray-sdk-require-only.js)
* [requiring the XRay SDK and instrumenting the AWS SDK](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-xray-sdk.js)
* [requiring the XRay SDK Core and instrumenting the AWS SDK](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/aws-xray-sdk-core.js)
* [requiring the XRay SDK Core and instrumenting only the DynamoDB client](https://github.com/theburningmonk/aws-sdk-coldstart-overhead/blob/master/functions/trace-dynamodb-only.js)

Each of these functions is traced by X-Ray. Sample rate set to 100%, so we don’t miss anything. We are only interested in the duration of the **Initialization** segment as it corresponds to the time for initializing these dependencies.

![Image](https://cdn-media-1.freecodecamp.org/images/vti9c-ncmZmjEhZ1EAsigD4Izw5ytDib-vIx)

The `no AWS SDK` case is our control group. We can see how much time each additional dependency adds to our `Initialization` duration.

To collect a statistically significant sample set of data, I decided to automate the process using Step Functions.

![Image](https://cdn-media-1.freecodecamp.org/images/WLmC8wSjkh5BzqCqZ8Lt1h6PjX3-XXPCQVO2)

* The state machine takes an input `{ functionName, count }`.
* The `SetStartTime` step adds the current UTC timestamp to the execution state. This is necessary as we need the start time of the experiment to fetch the relevant traces from X-Ray.
* The `Loop` step triggers the desired number of cold starts for the specified function. To trigger cold starts, I programmatically update an environment variable before invoking the function. That way, I ensure that every invocation is a cold start.

![Image](https://cdn-media-1.freecodecamp.org/images/n53oR25NejQ5zkTR3Ac1Lu4qstHCrm9dOI1E)

* The `Wait30Seconds` step makes sure that all the traces are published to XRay before we attempt to analyze them.
* The `Analyze` step fetches all the relevant traces in XRay and outputs several statistics around the `Initialization` duration.

Each configuration is tested over 1000 cold starts. Occasionally the XRay traces are incomplete (see below). These incomplete traces are excluded in the `Analyze` step.

![Image](https://cdn-media-1.freecodecamp.org/images/njYdfDGCkx4x0o4zurYChzt7jsDVUqwpgU2F)
_where is the AWS::Lambda:Function segment?_

Each configuration is also tested with WebPack as well (using the [serverless-webpack](https://github.com/serverless-heaven/serverless-webpack) plugin). _Thanks to [Erez Rokah](https://www.freecodecamp.org/news/just-how-expensive-is-the-full-aws-sdk-3713fed4fe70/undefined) for the suggestion._

### The Results

These are the `Initialization` times for all the test cases.

![Image](https://cdn-media-1.freecodecamp.org/images/cAjSzzz77ppKqsM1osUtqn6-OlhkUpN-LA0g)

![Image](https://cdn-media-1.freecodecamp.org/images/XehPjBmG-NAXGOMkt5CMl0FrqmUfGXYFGN7S)

Key observations:

* WebPack improves the `Initialization` time across the board.
* Without any dependencies, `Initialization` time averages only 1.72ms without WebPack and 0.97ms with WebPack.
* Adding AWS SDK as the only dependency adds an average of 245ms without WebPack. This is fairly significant. Adding WebPack doesn’t improve things significantly either.
* Requiring only the DynamoDB client (the one-liner change discussed earlier) saves up to 176ms! In 90% of the cases, the saving was over 130ms. With WebPack, the saving is even more dramatic.
* The cost of requiring the XRay SDK is about the same as AWS SDK.
* There’s no statistically significant difference between using the full XRay SDK and XRay SDK Core. With or without WebPack.

_Originally published at [theburningmonk.com](https://theburningmonk.com/2019/03/just-how-expensive-is-the-full-aws-sdk/) on March 23, 2019._

