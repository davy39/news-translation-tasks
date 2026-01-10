---
title: How to Build an AI-Powered ChatBot with OpenAI, ChatGPT, Node.js, and React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-05T22:08:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chatbot-with-openai-chatgpt-nodejs-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-sanket-mishra-16629368.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: chatgpt
  slug: chatgpt
- name: node js
  slug: node-js
- name: openai
  slug: openai
- name: React
  slug: react
seo_title: null
seo_desc: "By Njoku Samson Ebere\nArtificial Intelligence (AI) has been making waves\
  \ lately, with ChatGPT revolutionizing the internet with the chat completion functionality.\
  \ \nYou can do a lot with it: drafting an email or other piece of writing, answering\
  \ quest..."
---

By Njoku Samson Ebere

Artificial Intelligence (AI) has been making waves lately, with [ChatGPT](https://platform.openai.com/) revolutionizing the internet with the [chat completion](https://platform.openai.com/docs/guides/chat) functionality. 

You can do a lot with it: drafting an email or other piece of writing, answering questions about a set of documents, creating conversational agents, giving your software a natural language interface, tutoring in various subjects, translating languages, and so on.  
  
This article will teach the basics of building a chat application using the [chat completion](https://platform.openai.com/docs/guides/chat) functionality to make it easy for every programmer to get on board. It is not as tough as it looks. You will see this as you follow this tutorial. 

You will learn the following:

* How to create a CLI chat app with Node.js only.
* How to build a chat application using just React.
* How to combine React and Node.js to create better chat AI software.

This tutorial will be based on the [`gpt-3.5-turbo`](https://platform.openai.com/docs/models/gpt-3-5) model.

%[https://youtu.be/T-9-_1w82Jg]

## Prerequisites

This tutorial requires basic knowledge of JavaScript, CSS, React, and Node.js.  
  
You also need an account on the OpenAI platform where chatGPT is hosted. It is free, so you can create one [here](https://platform.openai.com/overview).

## How to Create a CLI Chat AI App With Node.js

This section will focus on creating a chat application that will run only on the terminal using [Node.js](https://nodejs.org/).

%[https://youtu.be/4uTO3xZx5r4]

Begin by creating a directory for the project:

```cmd
mkdir nodejs-chatgpt-tutorial
```

Navigate into the folder:

```cmd
cd nodejs-chatgpt-tutorial
```

Initialize the project:

```
npm init -y
```

This will create a `package.json` file to keep track of the project details

Add the following line of code to the file:

```javascript
"type": "module"
```

This will enable you to use the ES6 module import statement.  
  
Install [OpenAI](https://openai.com/) with the command below:

```cmd
npm i openai

```

Create a file where all the code will live. Name it `index.js`:

```cmd
touch index.js
```

Import `Configuration` and `OpenAIApi` from the [OpenAI](https://openai.com/) module and `readline` from the [readline](https://nodejs.org/api/readline.html) module:

```javascript
import { Configuration, OpenAIApi } from "openai";
import readline from "readline";
```

Build the OpenAI configuration like this:

```javascript
const configuration = new Configuration({
  organization: "org-0nmrFWw6wSm6xIJXSbx4FpTw",
  apiKey: "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",
});
```

This code creates a new instance of the `Configuration` object. Inside it, you'll enter values for your `organization` and `apiKey`. You can find details of your organization in [settings](https://platform.openai.com/account/org-settings) and your apiKey info in [API](https://platform.openai.com/account/api-keys) [keys](https://platform.openai.com/account/api-keys). If you do not have an existing API Key, you can create it.  
  
Enter the following code after the configuration to create a new instance of the OpenAI API:

```javascript
const openai = new OpenAIApi(configuration);
```

You'll use this throughout the project.

Type the code below to test the `createChatCompletion` function:

```javascript
openai
  .createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: "Hello" }],
  })
  .then((res) => {
    console.log(res.data.choices[0].message.content);
  })
  .catch((e) => {
    console.log(e);
  });
```

This code calls the `createChatCompletion` function that triggers an endpoint (`https://api.openai.com/v1/chat/completions`). The function accepts an object of arguments (the `model` of chatGPT in use and an array of `messages` between the user and the AI. We will look at how to use the `messages` array to keep a history of the chat and improve the app in the next section).  
  
Each message is an object containing the `role` (that is, who sent the message. The value can be `assistant` if it is from the AI or `user` when the message originates from a human) and the `content` (the information sent).  
  
Finally, the code prints the response (`res.data.choices[0].message.content`) from the AI. Run the file in the terminal with this command:

```cmd
node index
```

This will return a response from the AI after some seconds.  
  
And that is all it takes to create the chatbot!   
  
But it will be helpful to make the application more interactive by requesting input from the user instead of hardcoding the message content into the code. The [readline](https://nodejs.org/api/readline.html) module will help us out in this regard.  
  
To make it interactive, remove the last code you typed and add the following:

```javascript
const userInterface = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
```

This code creates a UI in the terminal that allows users to type in their questions.

Next, prompt the user to enter a message using the code below:

```javascript
userInterface.prompt();

```

Finally, enter the following code:

```javascript
userInterface.on("line", async (input) => {
  await openai
    .createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: input }],
    })
    .then((res) => {
      console.log(res.data.choices[0].message.content);
      userInterface.prompt();
    })
    .catch((e) => {
      console.log(e);
    });
});
```

In the code above,

* When a user types something and hits `Enter`, the code above triggers a callback function.
* It passes whatever was typed by the user as `input`.
* The `input` is now used as the `content`.
* After the response of the AI is displayed, the user is prompted for another message in the `then` block.

See all the code on [GitHub](https://github.com/EBEREGIT/nodejs-chatgpt-tutorial).  
  
Run the file and have a conversation with the AI. It will look like the image below:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682935202577_Screenshot+2023-05-01+at+10.58.02.png)
_CLI chat with AI_

Great! That is an interactive CLI chat.  
  
This is useful to a few people (like engineers), but it has good security because it is on the server side.   
  
But how about others who might not understand how to use a CLI application? They will need something easier to use with a better user interface (UI) and user experience (UX). The following section will focus on building that kind of application using [React](https://react.dev/).

## How to Create a Chat Application Using React

This section is aimed at helping frontend developers get up to speed with the ChatGPT API for creating a chat app and building a better user interface to give users better experiences. You can apply the knowledge that you gain here to other frontend frameworks or libraries.

%[https://youtu.be/JrfaQ5dYbWg]

The first thing to do is to set up a basic React boilerplate. I will use [Vite](https://vitejs.dev/guide/#scaffolding-your-first-vite-project) for this purpose. You can use Vite to scaffold any modern JavaScript frontend project. Use the command below:

```javascript
npm create vite@latest
```

This command will prompt you to create a name and folder for your project and choose a framework or library (this tutorial uses React). After that, you will navigate into the folder and run the following command:

```javascript
npm install
npm run dev
```

These commands will install the necessary dependencies and start the local server on port `5173`  
  
Next, install [OpenAI](https://openai.com/) with the command below:

```javascript
npm i openai
```

This module gives access to all we need to create the chat app.  
  
Now we are set to start writing the code!  
  
Navigate into the `src/App.jsx` file and delete all of its content. Then add the following import statements:

```javascript
import { useState } from "react";
import { Configuration, OpenAIApi } from "openai";
```

The code above imports the `Configuration` for setting up config values and `OpenAIApi` to give us access to the chat completion functionalities.  
  
After that, build the configuration like this:

```javascript
const configuration = new Configuration({
  organization: "org-0nmrFWw6wSm6xIJXSbx4FpTw",
  apiKey: "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",
});
```

This code creates a new instance of the `Configuration` object. Inside it, you enter values for your `organization` and `apiKey`. You can find details of your organization in [settings](https://platform.openai.com/account/org-settings) and your apiKey info in [API](https://platform.openai.com/account/api-keys) [keys](https://platform.openai.com/account/api-keys). If you do not have an existing API Key, you can create it.  
  
Enter the following code after the configuration to create a new instance of the OpenAI API:

```javascript
const openai = new OpenAIApi(configuration);
```

We'll use this throughout the project.  
  
Create and export a default function:

```javascript
function App() {

  return (
    <main>
      <h1>Chat AI Tutorial</h1>
    <main/>
  );
}
export default App;
```

This function will house the rest of the code.  
  
Set up the following states before the `return` statement:

```javascript
  const [message, setMessage] = useState("");
  const [chats, setChats] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
```

* The `message` will hold the information sent from the app to the AI.
* The `chats` array will keep track of all the messages sent by both parties (user and AI).
* The `isTyping` variable will notify the user whether the bot is typing or not.

Type the following lines of code under the h1 tag

```javascript
      <div className={isTyping ? "" : "hide"}>
        <p>
          <i>{isTyping ? "Typing" : ""}</i>
        </p>
      </div>
```

The code above will display `Typing` whenever the user is waiting for a response from the AI.  
  
Create a form in which a user can type in a message by adding the code below into the `main` element:

```javascript
      <form action="" onSubmit={(e) => chat(e, message)}>
        <input
          type="text"
          name="message"
          value={message}
          placeholder="Type a message here and hit Enter..."
          onChange={(e) => setMessage(e.target.value)}
        />
      </form>
```

This code creates a form with one input. Whenever the form is submitted by hitting the `Enter` key, it triggers the `chat` function.  
  
The chat function will take two (2) arguments (`e` and `message`) like this:

```javascript
const chat = async (e, message) => {

}

```

Enter the following lines in the function:

```javascript
    e.preventDefault();
    
    if (!message) return;
    setIsTyping(true);
```

The code above prevents the `form` from reloading the web page, checks if a message was typed before submission, and sets `isTyping` to `true` to indicate that the app has started working on the input provided.   
  
ChatGPT has a format in which messages should be. It takes the following pattern:

```
{role: user | assistant, content: message to be sent
```

Every message (`content`) must show who sent it. The role is `assistant` when the chat is from the AI but `user` if it is from a human. So, before sending the message, be sure to format it properly and add it to the array (`chats`) like this:

```javascript
    let msgs = chats;
    msgs.push({ role: "user", content: message });
    setChats(msgs);

    setMessage("");
```

The last line above clears the input for a user to type another note.  
  
Now we will call the `createChatCompletion` endpoint by triggering the `createChatCompletion` function using the code below:

```javascript
  await openai
      .createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [
          {
            role: "system",
            content:
              "You are a EbereGPT. You can help with graphic design tasks",
          },
          ...chats,
        ],
      })
```

The `createChatCompletion` function takes at least two (2) arguments (`model` and `messages`):

* The model specifies the version of chatGPT in use.
* The messages is a list of all the messages between a user and the AI so far and a system message that gives the AI an idea of what sort of assistance it can provide.

```javascript
          {
            role: "system",
            content:
              "You are a EbereGPT. You can help with graphic design tasks",
          }
```

You can change the content to whatever suits you.  
  
The `messages` don’t have to contain more than one object in the array. It can be just one message. But when it is an array, it provides a message history that the AI can rely on to give better replies in the future, and it makes the user type less since there might be no need to be overly descriptive all the time.  
  
The `createChatCompletion` function returns a promise. So use a `then…catch…` block to get the response.

```javascript
      .then((res) => {
        msgs.push(res.data.choices[0].message);
        setChats(msgs);
        setIsTyping(false);
      })
      .catch((error) => {
        console.log(error);
      });
```

This code adds the message returned from the AI into the `chats` array and sets `isTyping` to false, indicating that the AI is done replying.   
  
You should now receive feedback (`Typing`) each time you send a message:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682702095176_Screenshot+2023-04-28+at+18.14.08.png)
_Chat application giving feedback when the AI is about to respond_

It is time to display the chat history for the user to see.  
  
Type the following code just below the `h1` tag:

```javascript
      <section>
        {chats && chats.length
          ? chats.map((chat, index) => (
              <p key={index} className={chat.role === "user" ? "user_msg" : ""}>
                <span>
                  <b>{chat.role.toUpperCase()}</b>
                </span>
                <span>:</span>
                <span>{chat.content}</span>
              </p>
            ))
          : ""}
      </section>
```

The code above loops through the `chats` and displays them one after another to the user. It outputs the `role` in upper case and the `content` of the message side by side.  
  
Here is what the output should look like:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682702531307_Screenshot+2023-04-28+at+18.21.23.png)
_ChatBot Working As Expected without CSS_

That looks cool!   
  
But adding some styling will give it an engaging look like [WhatsApp](https://www.whatsapp.com/) or [Messenger](https://www.messenger.com/).   
  
Replace the content of the `src/index.css` file with the following:

```css
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;
  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}
h1 {
  font-size: 3.2em;
  line-height: 1.1;
  text-align: center;
  position: sticky;
  top: 0;
  background-color: #242424;
}
main{
  max-width: 500px;
  margin: auto;
}
p{
  background-color: darkslategray;
  max-width: 70%;
  padding: 15px;
  border-radius: 50px;
}
p span{
  margin: 5px;
}
p span:first-child{
  margin-right: 0;
}
.user_msg{
  text-align: right;
  margin-left: 30%;
  display: flex;
  flex-direction: row-reverse;
}
.hide {
  visibility: hidden;
  display: none;
}
form{
  text-align: center;
  position: sticky;
  bottom: 0;
}
input{
  width: 100%;
  height: 40px;
  border: none;
  padding: 10px;
  font-size: 1.2rem;
}
input:focus{
  outline: none;
}
```

And remove all the styles from the `src/App.css` file.

You can find the [complete code on GitHub](https://github.com/EBEREGIT/react-chatgpt-tutorial).  
  
The application should now have a new look:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682704193641_Screenshot+2023-04-28+at+18.48.44.png)
_ChatBot Working As Expected with CSS_

That wraps it up for creating a chatbot with React and ChatGPT. It isn’t as tough as it sounds.  
  
But frontend applications like this one are best for demonstration, not production. The problem with creating the application this way is that the frontend exposes the API Key to cyber attacks. 

To fix this problem, it may be wise to save the API Key and Organisation Id somewhere safe in the cloud and reference it or build a backend for your application with better security.  
  
The following section will work on the problem.

## How to Combine React and Node.js to Make a Fullstack Chat AI Software

This section will now join the powers of the previous sections to build a more secure application while exhibiting better UI and UX. 

We will improve the Node section by using a server to expose an endpoint for the frontend’s consumption and simplify the frontend to interact with the backend instead of contacting [OpenAI](https://openai.com/) directly.

%[https://youtu.be/OJ7AgZVH118]

### How to Setup the Project

This part will create the folders and files necessary for the project.  
  
Create the project directory:

```cmd
mkdir react-node-chatgpt-tutorial
```

Navigate into the folder:

```cmd
cd react-node-chatgpt-tutorial
```

Install React using Vite and name the folder `frontend`. Use this command:

```cmd
npm create vite@latest
```

After that, you will navigate into the folder and run the following command:

```cmd
npm install
npm run dev
```

These commands will install the necessary dependencies and start the local server on port `5173`.  
  
Create the backend folder:

```cmd
mkdir backend
```

Now navigate into the backend folder and initialize the project with this command:

```cmd
npm init -y
```

This will create a `package.json` file to keep track of the project details.  
  
Add the following line of code to the file:

```javascript
"type": "module"
```

This will enable the use of the ES6 module import statement.  
  
Install [OpenAI](https://openai.com/) and other dependencies with the command below:

```cmd
npm i openai body-parser cors express
```

Create a file where all the code will live. Name it `index.js`:

```
touch index.js
```

That completes the project setup. There are now two folders (`frontend` and `backend`).

### How to Build a Server 

This part will focus on creating a local server to listen on port `8000`.

The first thing to do is to import the necessary modules like this:

```javascript
import { Configuration, OpenAIApi } from "openai";
import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
```

Next, set up `express`, a `port` to listen to, the `body-parser` for receiving input, and `cors` to allow free communications between the frontend and backend. Use the code below:

```javascript
const app = express();
const port = 8000;
app.use(bodyParser.json());
app.use(cors());
```

Finally, type the following code:

```javascript
app.listen(port, () => {
  console.log(`listening on port ${port}`);
});
```

This completes the server setup.  
  
When you run the `index.js`, you should get the following output:

```
listening on port 8000
```

### How to Create an Endpoint

In this part, we will build an endpoint that will receive messages from the frontend using the request body and return a response to the caller.  
  
Begin by establishing the configuration parameters as we did in previous sections:

```javascript
const configuration = new Configuration({
  organization: "org-0nmrFWw6wSm6xIJXSbx4FpTw",
  apiKey: "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",
});
const openai = new OpenAIApi(configuration);
```

Next, create an asynchronous POST route using the code below:

```javascript
app.post("/", async (request, response) => {
  
});
```

This endpoint will be called using `http://localhost:8000/`  
  
In the callback function, enter the code below to receive the `chats` input from the request body (`request.body`):

```javascript
const { chats } = request.body;
```

Now call the `createChatCompletion` endpoint as we did in the React section:

```javascript
  const result = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: "You are a EbereGPT. You can help with graphic design tasks",
      },
      ...chats,
    ],
  });
```

The difference here is that instead of using the `then…catch…` block, we assigned it to a variable (`result`) and returned the response using `response.json()` as in the following code:

```javascript
  response.json({
    output: result.data.choices[0].message,
  });
```

Find the code for this part on [GitHub here](https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial/tree/master/backend).  
  
Here is the output when tested on Postman:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682943795836_Screenshot+2023-05-01+at+13.22.17.png)
_Output From Postman_

That concludes the backend portion of the code. The next part will connect the frontend to the backend using the endpoint ( `http://localhost:8000/`) just created.

### How to Connect to the Backend from the Frontend.

This part takes us to the frontend, where we will create a form. The form will send a message to the backend via the API endpoint and receive a response through the same medium.  
  
Navigate to the `frontend/src/App.jsx` file and type the following code:

```javascript
import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [chats, setChats] = useState([]);
  const [isTyping, setIsTyping] = useState(false);

  const chat = async (e, message) => {
    e.preventDefault();

    if (!message) return;
    setIsTyping(true);

    let msgs = chats;
    msgs.push({ role: "user", content: message });
    setChats(msgs);

    setMessage("");

    alert(message);
  };

  return (
    <main>
      <h1>FullStack Chat AI Tutorial</h1>

      <section>
        {chats && chats.length
          ? chats.map((chat, index) => (
              <p key={index} className={chat.role === "user" ? "user_msg" : ""}>
                <span>
                  <b>{chat.role.toUpperCase()}</b>
                </span>
                <span>:</span>
                <span>{chat.content}</span>
              </p>
            ))
          : ""}
      </section>

      <div className={isTyping ? "" : "hide"}>
        <p>
          <i>{isTyping ? "Typing" : ""}</i>
        </p>
      </div>

      <form action="" onSubmit={(e) => chat(e, message)}>
        <input
          type="text"
          name="message"
          value={message}
          placeholder="Type a message here and hit Enter..."
          onChange={(e) => setMessage(e.target.value)}
        />
      </form>
    </main>
  );
}
export default App;
```

This code is similar to the code from the previous section. But we have removed the OpenAI configurations as we will no longer need them in this section. 

At this point, an alert pops up whenever the form is submitted. This will change in a moment.  
  
In the chat function, get rid of the `alert` message and type the following:

```javascript
fetch("http://localhost:8000/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        chats,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        msgs.push(data.output);
        setChats(msgs);
        setIsTyping(false);
      })
      .catch((error) => {
        console.log(error);
      });
```

The code above calls the endpoint we created and passes in the `chats` array for it to process. It then returns a response that is added to the `chats` and displayed in the UI.  
  
The following is how the UI looks at the moment:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682945738011_Screenshot+2023-05-01+at+13.55.10.png)
_Fullstack Chat UI before Styling_

The UI can look better if you add the following styles to the `frontend/src/index.css` file:

```css

:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;
}

html, body{
  scroll-behavior: smooth;
}

h1 {
  font-size: 3.2em;
  line-height: 1.1;
  text-align: center;
  position: sticky;
  top: 0;
  background-color: #242424;
}

main{
  max-width: 800px;
  margin: auto;
}

p{
  background-color: darkslategray;
  max-width: 70%;
  padding: 15px;
  border-radius: 50px;
}

p span{
  margin: 5px;
}

p span:first-child{
  margin-right: 0;
}

.user_msg{
  text-align: right;
  margin-left: 30%;
  display: flex;
  flex-direction: row-reverse;
}

.hide {
  visibility: hidden;
  display: none;
}

form{
  text-align: center;
  position: sticky;
  bottom: 0;
}

input{
  width: 100%;
  height: 40px;
  border: none;
  padding: 10px;
  font-size: 1.2rem;
  background-color: rgb(28, 23, 23);
}

input:focus{
  outline: none;
}
```

And remove all the styles from the `frontend/src/App.css` file.

The code for this part is on [GitHub](https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial/tree/master/frontend).  
  
Now here is the final output:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1682946018213_Screenshot+2023-05-01+at+13.59.37.png)
_FullStack ChatBot Working As Expected with CSS_

Congratulations on finishing this project!  
  
The full stack chatbot was more work, but it helped us separate concerns, build a more secure and attractive application, and offer a better experience to users. So it was worth the effort.  
  
You can find the [code for this section on GitHub](https://github.com/EBEREGIT/react-nodejs-chatgpt-tutorial).

## Conclusion

This tutorial hopefully showed you that anyone with basic programming knowledge can build AI-powered software. You learned how to build a chatbot using React and Nodejs, and we discussed the pros and cons of each technology. Finally, we built a solution that was both functional, secure, and visually appealing.  
  
After reading this tutorial, you can now explore AI’s functionalities like image manipulation and audio interaction. Take your time to go through the [documentation](https://platform.openai.com/docs/introduction) and see how you can expand on what we covered here.  

