---
title: The Complete Guide to building an API with TypeScript and AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-27T15:57:26.000Z'
originalURL: https://freecodecamp.org/news/build-an-api-with-typescript-and-aws
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9900740569d1a4ca1d4b.jpg
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: serverless
  slug: serverless
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: "By Sam Williams\nIn this article we'll be looking at how we can quickly\
  \ and easily build an API with TypeScript and Serverless. \nWe'll then learn how\
  \ to use the aws-sdk to access other AWS services and create an automatic translation\
  \ API.\nIf you prefe..."
---

By Sam Williams

In this article we'll be looking at how we can quickly and easily build an API with TypeScript and Serverless. 

We'll then learn how to use the _aws-sdk_ to access other AWS services and create an automatic translation API.

If you prefer to watch and learn, you can check out the video below:

%[https://youtu.be/HhgXwKFUzT8]

## Getting started

To start this whole process we need to make sure that we have the Serverless Framework installed and have an AWS profile set up on our computer. If you haven't then you can [check out this video](https://youtu.be/D5_FHbdsjRc) on how to get that all set up.

If you want to follow along with this tutorial you can follow all the steps or [download the code here](https://www.subscribepage.com/awstypescriptapizip) and follow with the completed code.

Now we're onto creating our serverless project and API. We need to start in a terminal and run the command to create our new repo. All you need to do is to switch out the `{YOUR FOLDER NAME}` for the name of your folder.

```
serverless create --template aws-nodejs-typescript --path {YOUR FOLDER NAME}
```

This will create a very basic serverless project with TypeScript. If we open this new folder with VS Code then we can see what the template has given us.

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-21-at-06.54.45.png)

The main files we want to look at are the `serverless.ts` file and the `handler.ts` file.

The `serverless.ts` file is where the configuration for the deployment is held. This file tells the serverless framework the project name, the runtime language of the code, the list of functions and a few other configuration options. 

Whenever we want to change the architecture of our project this is the file we'll be working in.

The next file is the `handler.ts` file. Here we have the example code for a lambda given to us by the template. It is very basic and just returns an API Gateway response with a message and the input event. We'll be using this later as a starting block for our own API.

## Create Your Own Lambda

Now that we've seen what we get with the template, it's time to add our own Lambda and API endpoint.

To start, we're going to make a new folder to hold all of our lambda code and call it `lambdas`. This helps organise it, especially when you start getting a few different lambdas in one project.

In that new folder we're going to create our new lambda calling it `getCityInfo.ts`. If we open this file up we can start creating our code. We can begin by copying all of the `handler.ts` code as a starting point.

The first thing we're going to do is to change the name of the function to `handler`. This is a personal preference, but I like naming the function that handles the event handler.

On the first line in this function we need to add some code to get the city that the user is requesting. We can get this from the URL path using `pathParameters`.

```js
const city = event.pathparameter?.city;
```

One thing you may notice is the use of `?.` in that declaration. That is Optional Chaining and is a really cool feature. I

t means _if the path parameter is truthy then get the city parameter, else return undefined._ This means if `pathParameter` was not an object_,_ this wouldn't get the `cannot read property _city_` of undefined error that causes the Node runtime to error.

Now that we have the city we need to check that the city is valid and that we have data for that city. For this we need some data. We can use the code below and paste this at the bottom of the file.

```
interface CityData {
    name: string;
    state: string;
    description: string;
    mayor: string;
    population: number;
    zipCodes?: string;
}

const cityData: { [key: string]: CityData } = {
    newyork: {
        name: 'New York',
        state: 'New York',
        description:
            'New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean. At its core is Manhattan, a densely populated borough that’s among the world’s major commercial, financial and cultural centers. Its iconic sites include skyscrapers such as the Empire State Building and sprawling Central Park. Broadway theater is staged in neon-lit Times Square.',
        mayor: 'Bill de Blasio',
        population: 8399000,
        zipCodes: '100xx–104xx, 11004–05, 111xx–114xx, 116xx',
    },
    washington: {
        name: 'Washington',
        state: 'District of Columbia',
        description: `DescriptionWashington, DC, the U.S. capital, is a compact city on the Potomac River, bordering the states of Maryland and Virginia. It’s defined by imposing neoclassical monuments and buildings – including the iconic ones that house the federal government’s 3 branches: the Capitol, White House and Supreme Court. It's also home to iconic museums and performing-arts venues such as the Kennedy Center.`,
        mayor: 'Muriel Bowser',
        population: 705549,
    },
    seattle: {
        name: 'Seattle',
        state: 'Washington',
        description: `DescriptionSeattle, a city on Puget Sound in the Pacific Northwest, is surrounded by water, mountains and evergreen forests, and contains thousands of acres of parkland. Washington State’s largest city, it’s home to a large tech industry, with Microsoft and Amazon headquartered in its metropolitan area. The futuristic Space Needle, a 1962 World’s Fair legacy, is its most iconic landmark.`,
        mayor: 'Jenny Durkan',
        population: 744955,
    },
};
```

The difference between this and JavaScript is that we can create an _interface_ to tell the system what the structure of the data must be. This feels like extra work at the start but will help make everything easier later on.

Inside our interface we define the keys of the city object; some that are strings, one number, and then the `zipCodes` is an optional property. This means it could be there but doesn't have to be.

If we want to test our interface, we can try adding a new property to any of the cities in our city data. 

TypeScript should instantly tell you that your new property doesn't exist on the interface. If you delete one of the required properties TypeScript will also complain. This makes sure that you always have the correct data and objects always look exactly as expected.

Now that we have the data we can check if the user sent up the correct city request.

```js
if (!city || !cityData[city]) {
    
}
```

If this statement is true then the user has done something wrong, therefore we need to return a 400 response. 

We could just manually type the code here but we're going to create a new `apiResponses` object with methods for a few of the possible API response codes.

```js
const apiResponses = {
    _200: (body: { [key: string]: any }) => {
        return {
            statusCode: 200,
            body: JSON.stringify(body, null, 2),
        };
    },
    _400: (body: { [key: string]: any }) => {
        return {
            statusCode: 400,
            body: JSON.stringify(body, null, 2),
        };
    },
};
```

This just makes it much easier to reuse later in the file. You should also see that we have one property of `body: { [key: string]: any }`. This is stating that this function has one property of body which needs to be an object. That object can have keys that have a value of any type. 

Because we know that `body` is always going to be a string we can use `JSON.stringify` to make sure we return a string body.

If we add this function to our handler we get this:

```js
export const handler: APIGatewayProxyHandler = async (event, _context) => {
    const city = event.pathParameters?.city;

    if (!city || !cityData[city]) {
        return apiResponses._400({ message: 'missing city or no data for that city' });
    }

    return apiResponses._200(cityData[city]);
};
```

If the user didn't pass up a city or passed up one we have no data for, we return a 400 with an error message. If the data does exist then we return a 200 with a body of the data.

# Adding a New Translation API

In the previous section we set up our TypeScript API repo and created a lambda which just used hard coded data. 

This part is going to teach you how to use the _aws-sdk_ to interact directly with other AWS services to create a really powerful API.

%[https://youtu.be/xdWpbr1DZHQ]

To start, we need to add a new file for our translation API. Create a new file under the `lambdas` folder called `translate.ts`. We can start this file out with some basic boilerplate code. This is the starting code for a TypeScript API Lambda.

```js
import { APIGatewayProxyHandler } from 'aws-lambda';
import 'source-map-support/register';

export const handler: APIGatewayProxyHandler = async (event) => {
    
};
```

Now we need to get the text that the user wants translated and the language that they want to translate to. We can get these from the body of the request. 

One extra thing we have to do here is to parse the body. By default, API Gateway stringifies any JSON passed in the body. We can then destructure the text and language from the body.

```js
const body = JSON.parse(event.body);
const { text, language } = body;
```

We now need to check that the user has passed up text and language.

```js
if (!text) {
    // retrun 400
}
if (!language) {
    // return 400
}
```

In the last part we created the 400 response as a function in the file. As we're going to be using these API responses across multiple files, it is a good idea to pull them out to their own _common_ file.

Create a new folder under _lambdas_ called `common`. This is where we are going to store all common functions. 

In that folder create a new file called `apiResponses.ts`. This file is going to export the `apiResponses` object with the __200 and _400_ methods on it. If you have to return other response codes then you can add them to this object.

```js
const apiResponses = {
    _200: (body: { [key: string]: any }) => {
        return {
            statusCode: 200,
            body: JSON.stringify(body, null, 2),
        };
    },
    _400: (body: { [key: string]: any }) => {
        return {
            statusCode: 400,
            body: JSON.stringify(body, null, 2),
        };
    },
};

export default apiResponses;
```

We can now import that object into our code and use these common methods in our code. At the top of our _translate.ts_ file we can now add this line:

```js
import apiResponses from './common/apiResponses';
```

and update our text and language checks to call the __400_ method on that object:

```js
if (!text) {
    return apiResponses._400({ message: 'missing text fom the body' });
}
if (!language) {
    return apiResponses._400({ message: 'missing language from the body' });
}
```

With that completed we know that we have the text to translate and a language to translate into, so we can start the translation process. 

Using the aws-sdk is almost always an async task so we're going to wrap it in a _try/catch_ so that our error handling is easier.

```js
try {
    
} catch (error) {
    
}
```

The first thing we need to do is to import the aws-sdk and create a new instance of the translate service. 

To do that we need to install the aws-sdk and then import it. First run `npm install --save aws-sdk` and then add this code to the top of your translate file:

```js
import * as AWS from 'aws-sdk';

const translate = new AWS.Translate();
```

With this we can start to write our translation code. We're going to start with the line that does the translation first. Add this in the _try_ section.

```js
const translatedMessage = await translate.translateText(translateParams).promise();
```

One thing that some of you may have noticed is that we're passing in `translateParams` without having defined it yet. That is because we're not sure what type it is yet. 

To find this out we can use a tool in VS Code called `go to definition`. This allows us to jump to where the function if defined so we can find out what the type of the parameters is. You can either right click and select `go to definition` or hold _Ctrl_ and click on the function.

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-23-at-08.14.03.png)

As you can see the `translateText` function takes a param of `Translate.Types.TranslateTextRequest`. 

Another way to find this out is to use _intelisense_ by mousing over the `translateText` function. You should see this, where you can see that `params: AWS.Translate.TranslateTextRequest`:

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-23-at-08.15.30.png)

With this we can create our translate params above the translate request we made earlier. We can then populate it based on the type we are setting it as. This makes sure we're passing up the correct fields.

```js
const translateParams: AWS.Translate.Types.TranslateTextRequest = {
    Text: text,
    SourceLanguageCode: 'en',
    TargetLanguageCode: language,
};
```

Now that we have the parameters and are passing them into the `translate.translateText` function, we can start creating our response. This is just going to be a 200 response with the translated message.

```js
return apiResponses._200({ translatedMessage });
```

With that all done we can move onto the _catch_ section. In here we just want to log out the error and then return a 400 response from the common file.

```js
console.log('error in the translation', error);
return apiResponses._400({ message: 'unable to translate the message' });
```

With that completed we're done with our lambda code, so need to move into our `severless.ts` file to add this new API endpoint and give it the permissions it needs.

In the `serverless.ts` file we can scroll down to the `functions` section. In here we need to add a new function to the object.

```js
translate: {
    handler: 'lambdas/translate.handler',
    events: [
        {
            http: {
                path: 'translate',
                method: 'POST',
                cors: true,
            },
        },
    ],
},
```

The main difference between this and the previous endpoint is that the endpoint is now a _POST_ method. This means if you try and do a _GET_ request to this URL path, you'll get an error response.

The last thing to do is to give the lambdas permission to use the Translate service. With almost all of the AWS Services, you'll need to add extra permissions to be able to use the from within a lambda. 

To do this we add a new field onto the `provider` section called `iamRoleStatements`. This is an array of _allow_ or _deny_ statements for different services and resources.

```
iamRoleStatements: [
    {
        Effect: 'Allow',
        Action: ['translate:*'],
        Resource: '*',
    },
],
```

With this added in we have everything we need set up so we can run `sls deploy` to deploy our new API.

Once this has deployed, we can get the API URL and use a tool like postman or [postwoman.io](https://postwoman.io/) to make a request to that URL. We just need to pass up a body of:

```js
{
    "text": "This is a test message for translation",
    "language": "fr"
}
```

and then we should get a 200 response of:

```js
{
  "translatedMessage": {
    "TranslatedText": "Ceci est un message de test pour la traduction",
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "fr"
  }
}
```

# Summary

In this article we've learnt how to:

* Set up a new TypeScript repo with `severless create --template aws-nodejs-typescript`
* Add our own Lambda that returns a selection of hardcoded data
* Added that Lambda as an API endpoint
* Added another Lambda which will automatically translate any text passed to it
* Added an API endpoint and gave the Lambda the permissions it needed to work

If you enjoyed this article and want to learn more about Serverless and AWS, then I have a Youtube Channel with over 50 videos on all of this. I'd recommend watching the videos you find most interesting in my [Serverless and AWS playlist](https://www.youtube.com/playlist?list=PLmexTtcbIn_gP8bpsUsHfv-58KsKPsGEo).

