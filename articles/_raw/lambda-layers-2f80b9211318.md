---
title: How to build and use a Layer for your AWS Lambdas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-16T09:23:47.000Z'
originalURL: https://freecodecamp.org/news/lambda-layers-2f80b9211318
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kQDtO4sMgdnizh7DLdBE2g.png
tags:
- name: AWS
  slug: aws
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sam Williams

  AWS Lambdas are brilliant! They simplify deploying serverless applications. They
  allow us to really quickly build prototypes and automatically scale. One of the
  issues with having every function as a separate entity is that you need t...'
---

By Sam Williams

AWS Lambdas are brilliant! They simplify deploying serverless applications. They allow us to really quickly build prototypes and automatically scale. One of the issues with having every function as a separate entity is that you need to include common code into every single Lambda.

> If you have to do the same thing the same way three times, its time to automate it — Automation Rule of Three

%[https://www.youtube.com/watch?v=5a2LS7gNECk]

### Layers

Lambda Layers have been created to solve this _repeated code_ issue. The way they work is that you deploy your common code into a layer. This can be your common code or NPM packages that you always use. When you connect this layer to one of your Lambdas, you can access all the common code from inside your Lambda.

This means that you don’t have to copy the same file into every Lambda folder or create your own ‘common’ repo that you require.

### Setting up a Layer

Since a layer is just a collection of code, we can start by creating a new folder for this layer. I like to have all my layers in a folder next to my Lambdas folder. We can create a new layer folder called _DemoLayer_ which needs to have a folder for the runtime that it is going to use. For this example, we are going to use _nodejs,_ so we create that folder.

```bash
mkdir -p lambdaLayers/DemoLayer/nodejs
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*PIfYqz7wFGNQxnF97h99Lw.png)

Using our terminal, we can navigate to the _DemoLayer_ folder and initialize NPM.

```bash
cd lambdaLayers/DemoLayer/nodejs
npm init
```

Accept all the default values in the NPM setup, and you’ll have the _package.json_ file generated in your folder.

For our first layer, we are going to import the _moment_ library. This is the same process as you would use to add any NPM package to the layer.

```bash
npm install --save moment
```

#### Deploying our Layer

Now that we have the common code in our folder we need to deploy it. To do this, we need to zip up the whole folder and then upload it as a Lambda Layer. To zip up the folder content you can navigate into the _DemoLayer_ folder and run a _zip_ command on the content of the folder.

```bash
cd ../
zip -r demoLayer.zip ./*
```

You should now see a `demoLayer.zip` file inside your folder. We can now go the AWS Console create our layer.

In the AWS console, navigate to AWS Lambda, and on the left-hand side, we should have options including _Layers._

![Image](https://cdn-media-1.freecodecamp.org/images/1*J04fWaAc04iOFUBFSIPkgg.png)

Inside the layers menu, we have the option to create a new layer. Clicking this opens up the setup options where we can give the layer a name, a description, upload the zip file we just created and select the runtimes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lA4CyPZr32jHLu7w-76mkQ.png)

### Testing the Layer

With the layer created we can test that it all works. To do this, we can create a new Lambda called _DemoWithLayer_ that runs on node 8.10. Inside this Lambda we can add this code:

```js
const moment = require('moment');

exports.handler = async (event) => {
    let momentNow = moment.now();
    
    const response = {
        statusCode: 200,
        body: JSON.stringify({momentNow}),
    };
    return response;
};
```

We can test what happens when we run this without the layer by creating a test event. In the top right of the Lambda console, click _select a test event_ and then _configure test events._ This opens a config window where we create the JSON blob that is sent to the handler. As we don’t use the event object, we can pass the default values, give this test a name and create it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KhQ2qNZY0uIJkSUeBeQEpw.png)

We can now click the _Test_ button to run our Lambda. Doing this results in this message:

![Image](https://cdn-media-1.freecodecamp.org/images/1*t81K9fcj9ZZHyA6IJ9tvVA.png)

This is because our Lambda doesn’t have the _moment_ module installed. We can now add our new layer to the Lambda and rerun the test.

To add a layer, click the _Layers_ button underneath the _DemoWithLayer_ button. Scroll to the bottom of the page to the _Referenced layers_ section and click the _add a layer_ button. In the popup, we can select our _DemoLayer_ from the dropdown and selecting the highest version.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sB0HC6rsFrYOzaTMLOvrVg.png)

Add this to the Lambda and make sure to save the Lambda changes. When we rerun the test, we get a success response. You can use this process to remove a lot of the common packages from your Lambdas.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Xc59dAEq2aYdk4WlrdYFXg.png)

