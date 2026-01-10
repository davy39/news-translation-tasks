---
title: How to Structure JSON Responses in ChatGPT with Function Calling
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-25T18:09:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-json-back-from-chatgpt-with-function-calling
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/chatgpt-ui-circled-1.png
tags:
- name: chatgpt
  slug: chatgpt
- name: json
  slug: json
seo_title: null
seo_desc: 'By James Charlesworth

  ChatGPT''s Problem With JSON

  Open up the ChatGPT UI and ask it for some JSON. Chances are you will get a response
  like you can see in the cover photo above: a JSON object presented to you in markdown
  format, with some text to eit...'
---

By James Charlesworth

## ChatGPT's Problem With JSON

Open up the [ChatGPT UI](https://chat.openai.com/) and ask it for some JSON. Chances are you will get a response like you can see in the cover photo above: a JSON object presented to you in markdown format, with some text to either side explaining what the JSON shows.  

If you try this same prompt in the [OpenAI Playground](https://platform.openai.com/playground), you can see the JSON is enclosed in three backticks (markdown syntax).

![Open AI Playground interface showing a user prompt asking for some JSON](https://www.freecodecamp.org/news/content/images/2023/10/openai-playground-1-1.png)
_https://platform.openai.com/playground_

Now this is great. ChatGPT has gone above and beyond by explaining the response in easy to understand terms – easy to understand, that is...for a human. Not for a machine. Machines need data in a format that sticks to a reliable, consistent, and predictable schema.

Ideally, you'd like to parse the response from ChatGPT in your code and do something useful with it, like this:

```ts
// Use the openai package from npm to call ChatGPT
import OpenAI from "openai";

// Create a new instance of the openai client with our API key
const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });

// Call ChatGPT's completions endpoint and ask for some JSON
const gptResponse = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    temperature: 1,
    messages: [
        {
            role: "user",
            content: "Give me the JSON for an object that represents a cat."
        }
    ],
});

// Attempt to read the response as JSON,
// Will most likely fail with a SyntaxError...
const json = JSON.parse(gptResponse.choices[0].message.content);
```

But this will only work if `gptResponse.choices[0].message.content` is valid JSON every time.  

It would also be nice to have JSON returned that reliably sticks to a schema:

```ts
type Cat = {
    name: string,
    colour: "brown" | "grey" | "black",
    age: number
}

// Read the response JSON and type it to our Cat object schema
const json = <Cat>JSON.parse(gptResponse.choices[0].message.content);
```

Not being able to rely on ChatGPT to return valid JSON in a predictable format can introduce bugs into your application, particularly when consistency is key. This becomes a real problem when you're writing code that relies on real-time responses from ChatGPT to trigger specific actions or updates so we need to find a solution. There are a couple of ways we can approach this...

## How Prompt Engineering Can Help

One approach to solving this problem is through prompt engineering.

![Open AI Playground image showing a system prompt controlling the response format](https://www.freecodecamp.org/news/content/images/2023/10/asking-specifically-2.png)
_https://platform.openai.com/playground_

Here, we have added some instructions to both the user prompt and the [system message](https://platform.openai.com/docs/guides/gpt/chat-completions-api). The instructions attempt to force the model to return only the JSON we want, with the format we want.  

And for many use cases this works acceptably. You can see from the screenshot above that the "Assistant" response is nothing but JSON, and the JSON does adhere to the schema we described for it.

But this doesn't work 100% of the time.

Here is the _exact same_ pair of prompts with the temperature of the model set above 1. Notice how the `colour` field in the returned JSON does not now stick to one of the allowed values we specified in the User prompt:

![Open AI Playground interface showing the Temperature parameter causing invalid responses at higher values](https://www.freecodecamp.org/news/content/images/2023/10/higher-temperature-1.png)

## Function Calling to the Rescue

[Function calling](https://platform.openai.com/docs/guides/gpt/function-calling) is a new way to use the ChatGPT API. Instead of getting a message back from the language model, you get a request to call a function.  

If you've ever used plugins in the ChatGPT UI, _Function Calling_ is the feature behind the scenes that allow plugins to be integrated with the LLM's responses.

Plugins define the functions that are available to the model and allow it to call those functions in response to user prompts.  

When using the API in your own code, you can also take advantage of function calling to better control the data you get back from the model, including forcing it to return JSON data in a predictable format.

Here is a basic request that uses Function Calling to return a `message.function_call` object in the response instead of a `message.content` string.  

Here, we are simply asking ChatGPT to call a function ("getName") and a description of the function inside the `functions: []` array. We are also instructing ChatGPT that we expect it to call this function in the response by setting the value of `function_call` to the name of our function.

```ts
const gptResponse = await openai.chat.completions.create({
    model: "gpt-3.5-turbo-0613",
    messages: [
        {
            role: "user",
            content: "Call the function 'getName' and tell me the result."
        }
    ],
    functions: [
        {
            name: "getName",
            parameters: {
                type: "object",
                properties: {}
            }
        }
    ],
    function_call: { name: "getName" }
});

// Will print "getName"...
console.log(gptResponse.choices[0].message.function_call.name);
```

It's important to note here that the `getName()` function does not need to actually exist anywhere in our codebase. All we are doing is telling ChatGPT it exists, and that is it available to be called.

### How to add function arguments

Function calling is great because it makes the response from ChatGPT predictable and structured.  

In the example above we will get an object back in `gptResponse.choices[0].message.function_call` that will contain details of how ChatGPT wants to execute our (imaginary) function. 

This object looks like the below, with the name of the function and a [stringified](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) version of any function arguments it should be called with:

```json
{
  name: "functionName",
  arguments: "{ \"arg1\": \"value\" }",
}
```

We can take advantage of this second `arguments` value by describing the shape of the function arguments, and having ChatGPT fill this value in with some JSON that conforms to our shape.

Here is the original example as a function call. Note how we have described the schema of the `Cat` object to ChatGPT inside the definition of a `createCatObject` function:

```ts
    type Cat = {
        name: string,
        colour: "brown" | "grey" | "black",
        age: number
    }

    const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });

    const gptResponse = await openai.chat.completions.create({
        model: "gpt-3.5-turbo-0613",
        messages: [
            {
                role: "user",
                content: "Create a new Cat object."
            }
        ],
        functions: [
            {
                name: "createCatObject",
                parameters: {
                    type: "object",
                    properties: {
                        name: {
                            type: "string"
                        },
                        colour: {
                            type: "string",
                            enum: ["brown", "grey", "black"]
                        },
                        age: {
                            type: "integer"
                        }
                    },
                    required: ["name", "colour", "age"]
                }
            }
        ],
        function_call: { name: "createCatObject" }
    });

    const functionCall = gptResponse.choices[0].message.function_call;
    const json = <Cat>JSON.parse(functionCall.arguments);
```

This completions request will instruct ChatGPT to create a new cat object and send it to the `createCatObject()` function in a specific format. The last line:

```ts
const json = <Cat>JSON.parse(functionCall.arguments);
```

parses the arguments from ChatGPT into our `Cat` type, which mirrors the description we gave the model of our the shape of our expected object.

## Conclusion

Function calling with ChatGPT not only brings clarity and predictability to the results but also introduces a paradigm shift in how you can interface with machine learning models. 

This structured approach ensures that the responses from ChatGPT are scalable, allowing for easier integration into various applications, whether they be simple web apps or more complex machine learning pipelines.

