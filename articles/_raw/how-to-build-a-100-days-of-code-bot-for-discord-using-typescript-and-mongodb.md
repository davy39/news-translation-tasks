---
title: How to Use TypeScript and MongoDB to Build a 100 Days of Code Discord Bot
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2021-06-22T16:20:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-100-days-of-code-bot-for-discord-using-typescript-and-mongodb
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/news-header.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: '#chatbots'
  slug: chatbots
- name: discord
  slug: discord
- name: freeCodeCamp.org
  slug: freecodecamp
seo_title: null
seo_desc: "The 100 Days of Code challenge is very popular among new coders and developers\
  \ looking to level up their skills. It's so popular that our Discord server has\
  \ an entire channel dedicated to it. \nBy popular demand, we recently built a Discord\
  \ bot that h..."
---

The [100 Days of Code challenge](https://www.freecodecamp.org/news/the-crazy-history-of-the-100daysofcode-challenge-and-why-you-should-try-it-for-2018-6c89a76e298d/) is very popular among new coders and developers looking to level up their skills. It's so popular that our [Discord server](https://www.freecodecamp.org/news/freecodecamp-discord-chat-room-server/) has an entire channel dedicated to it. 

By popular demand, we recently built a Discord bot that helps people track their progress in the challenge.

Today I am going to show you how to build your own 100 Days of Code bot.

## How to Create a Discord Bot Application

Your first step is to set up a Discord bot application. Head over to the [Discord Developer Portal](https://discord.com/developers), sign in if needed, and select "Applications" from the sidebar.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-158.png)
_Screenshot of the Developer Portal. If this is your first bot, you will not have any applications here._

Click the "New Application" button. Give it a name, and set it as a "Personal" application. You will now be taken to the application's settings. Here you can change the name, or give it an avatar.

Select "Bot" from the side bar, then click the "Add Bot" button. This will create a Discord Bot account for your application.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-99.png)
_Screenshot of the Bot settings page. If you did not set an avatar, you will see a default based on your bot's name._

This is the screen where you will get the bot token. It is _very_ important to keep this token secret, as the token allows your code to connect to your bot. Keep it safe and do not share it with anyone.

Now you need to add the bot to a server to interact with it. Click the "OAuth2" option on the side bar. You should see a form under the "OAuth2 URL Generator" section. Leave the "Select Redirect URL" dropdown blank, and check the box for the "bot" scope.

An option to select permissions will appear. Check the boxes for the following permissions:

* Send Messages
* Manage Messages
* Embed Links
* Read Message History
* View Channels

Above that section, you should see a URL generated. Click the "Copy" button to copy it, then paste it into your browser and go. 

This will take you through Discord's process to add your new bot to a server. Note that you must have the Manage Server permission in the server you want to add the bot to. If you do not have this permission in any servers, you can create a server to test your bot in.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-156.png)
_Screenshot of the OAuth screen with the correct settings marked._

Now you are ready to write some code!

## How to Set Up Your Project

You need to set up the infrastructure and tooling for your project.

### Prepare the `package.json`

Create a directory, or folder, for your project. Open your terminal pointing to that new folder. Run the command `npm init` to set up your `package.json` file. For this tutorial, the default values are sufficient, but feel free to edit them as you wish.

You should end up with a `package.json` similar to this:

```json
{
  "name": "tutorial",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

Now you need to make a couple of changes to get ready for the TypeScript implementation.

First, replace the `main` value of `index.js` with `./prod/index.js` – you will be setting your TypeScript to compile to a `prod` directory.

Then, remove the `test` script and add the following two scripts:

```json
"build": "tsc",
"start": "node -r dotenv/config ./prod/index.js"
```

The `build` script will compile your TypeScript into JavaScript so `node` can run it, and the `start` script will run the `index.js` entrypoint file.

Adding the `-r dotenv/config` here will dynamically import and run the `config` method in the `dotenv` package, which loads your environment variables from the `.env` file.

Speaking of packages, your next step is to install dependencies. Using `npm install`, install these dependencies:

* `discord.js` – this is the library that will handle connecting to the gateway and managing the Discord API calls.
* `dotenv` – a package that loads `.env` values into the node process.
* `mongoose` – A wrapper for the MongoDB connection which offers tools for structuring your data.

Finally, install the development dependencies with `npm install --save-dev`. Development dependencies are packages that are required for working on your project in a development environment, but not required for running the codebase in production.

* `typescript` – This is the package for the TypeScript language, which includes everything needed to write code in TypeScript and compile it into JavaScript.
* `@types/node` – TypeScript relies on type definitions to help understand the code you write. This package defines the types for the Node.js runtime environment, such as the `process.env` object.

With these packages installed, you should now have a `package.json` similar to this:

```json
{
  "name": "tutorial",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "build": "tsc",
    "start": "node -r dotenv/config ./prod/index.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "discord.js": "^12.5.3",
    "dotenv": "^10.0.0",
    "mongoose": "^5.12.14"
  },
  "devDependencies": {
    "@types/node": "^15.12.2",
    "typescript": "^4.3.4"
  }
}
```

### Prepare TypeScript

TypeScript's compiler offers a number of different settings to maximize your control over the resulting JavaScript. 

You can typically modify compiler settings through a `tsconfig.json` file at the root of your project. You can generate the default boilerplate for this file with `npx tsc --init`, use an existing one if you set one up in another project, or even write one from scratch.

Because the compiler settings can significantly change the behaviour of TypeScript, it is best to use the same settings when following this tutorial. Here are settings you should use:

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "CommonJS",
    "rootDir": "./src",
    "outDir": "./prod",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  }
}
```

The most important settings here are the `rootDir` and `outDir` settings. These tell the compiler that all of your code will be in the `src` directory, and the resulting JavaScript should go in the `prod` directory.

If you would like to test your settings, create a `src` directory and place an `index.ts` file inside. Write some code (such as a `console.log` statement) and run `npm run build` in your terminal. You should see a `prod` directory get created, with an `index.js` containing your compiled code.

### Additional Setup Notes

If you are using `git` as a version control, you want to avoid pushing secrets and unnecessary code to your repository. Create a `.gitignore` file in your root project directory, and add the following content:

```txt
/node_modules/
/prod/
.env
```

The `.gitignore` file tells `git` not to track files/folders that match the patterns you enter. Ignoring the node modules folder keeps your repository from becoming bloated. 

Pushing the compiled JavaScript is also unnecessary, as your project is typically compiled in production before runtime. `.env` files typically contain your secret values, such as API keys and tokens, so they should not be committed to a repository.

If you are using a UNIX based environment (such as Linux, or Git Bash on Windows), you can also add a `prebuild` script to your `package.json`. The `prebuild` script will automatically run before the `build` script when you use `npm run build`. I set mine to clean up the existing `prod` directory with `rm -r ./prod`.

## How to Create the Discord Bot

Your next step is to prepare the initial bot connection. If you did not do so earlier, create a `src` directory and an `index.ts` file within.

Start with an anonymous immediately-invoked function expression (IIFE) to allow for top-level `await` use:

```ts
(async () => {

})();
```

Within this function you are going to instantiate your Discord bot. At the top of the file, import the `Client` class with `import { Client } from "discord.js;"`. The `Client` class represents your Discord bot's session.

Inside your function, construct a new `Client` instance and assign it to a `BOT` variable with `const BOT = new Client();`. Now the `BOT` variable will represent your bot.

To connect your bot to Discord's gateway and begin receiving events, you will need to use the `.login()` method on your bot instance. The `.login()` method takes a single argument, which is the token for the bot application you created earlier. 

Many of the methods in `discord.js` are asynchronous, so you will need to use `await` here. Add the line `await BOT.login(process.env.BOT_TOKEN);` to your IIFE.

The `process.env` object will contain the environment variables for your Node.js runtime environment. With the `dotenv` package, this will also include any variables you set in your `.env` secrets file. 

Create that `.env` file in the root of your project, and add `BOT_TOKEN=""` as the first line. Between the quotes, paste the bot token from the bot page on the Discord Developer Portal.

Your `index.ts` file should now look like this:

```ts
import { Client } from "discord.js";

(async () => {
  const BOT = new Client();

  await BOT.login(process.env.BOT_TOKEN);
})();

```

Assuming you added your new bot to a server, if you run `npm run build` and `npm start` you should see your bot come online in the server. However, the bot will not respond to anything yet, because we have not started listening to events.

## Gateway Events in Discord

Gateway "events" are generated when an action happens on Discord, and are typically sent to clients (including your bot) as JSON payloads. You can listen to those events with the `.on()` method, allowing you to write logic for your bot to follow when specific events occur.

The first event to listen to is the "ready" event. This event fires when your bot has connected to the gateway and is _ready_ to process events. Above your `.login()` call, add `BOT.on("ready", () => console.log("Connected to Discord!"));`. 

For your changes to take effect, use `npm run build` again to compile the new code. Now if you try `npm run start`, you should see "Connected to Discord!" print in your terminal.

## How to Connect to the Database

You'll be using the `mongoose` package to connect to a MongoDB instance. If you prefer, you can run MongoDB locally, or you can use the MongoDB Atlas free tier for a cloud-based solution. 

If you do not have a MongoDB Atlas account, freeCodeCamp has a [great tutorial on setting one up](https://www.freecodecamp.org/news/get-started-with-mongodb-atlas/).

Grab your connection string for your database and add it to your `.env` file as `MONGO_URI=""`, with the connection string going between the quotes. For the database name, use `oneHundredDays`.

Create a directory called `database` to hold the files that contain your database logic. Within that directory, create a file called `connectDatabase.ts`. You will be writing your logic to initiate the database connection here.

Start with an exported function declaration:

```ts
export const connectDatabase = async () => {

}
```

`mongoose` offers a `connect` method for connecting to the database. Import it with `import { connect } from "mongoose";` at the top of your file.

Then use the method inside your function with `await connect(process.env.MONGO_URI);`. Add a `console.log` statement after that so you can identify that your bot has connected to the database. 

Your `connectDatabase.ts` file should now look something like this:

```ts
import { connect } from "mongoose";

export const connectDatabase = async () => {
    await connect(process.env.MONGO_URI);
    console.log("Database Connected!")
}
```

Now, within your `index.ts` file, import this function with `import { connectDatabase } from "./database/connectDatabase"` and add `await connectDatabase()` to your IIFE, just before the `.login()` method. Go ahead and run `npm run build` again.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-157.png)
_A compiler error, indicating that: Argument of type string or undefined is not assignable to parameter of type string._

Oh no – an error!

## Environment Variable Validation

The problem with environment variables is that they can all be `undefined`. This often happens if you make a typo in your environment variable name, or mix the name up with another name (a mistake I made when writing this tutorial, using `TOKEN` instead of `BOT_TOKEN` in some places).

TypeScript is warning you that the `connect` method takes a string, and that an `undefined` value will break things. You can fix this, but first you will want to write a function to handle validating your environment variables.

Within your `src` directory, create a `utils` directory to contain your utility functions. Add a `validateEnv.ts` file there.

Create a function in the file called `validateEnv`. This function will be synchronous and does not need the `async` keyword. Within that function, add conditions to check for your two environment variables. If either one is missing, return `false`. Otherwise, return `true`.

Your code might look something like this:

```ts
export const validateEnv = () => {
  if (!process.env.BOT_TOKEN) {
    console.warn("Missing Discord bot token.");
    return false;
  }

  if (!process.env.MONGO_URI) {
    console.warn("Missing MongoDB connection.");
    return false;
  }
  return true;
};


```

Head back to your `index.ts` file and import this validation function with `import { validateEnv } from "./utils/validateEnv"`. Then at the beginning of your IIFE, use an if statement to return early if the function returns false. Your `index.ts` should look like:

```ts
import { Client } from "discord.js";
import { connectDatabase } from "./database/connectDatabase";
import { validateEnv } from "./utils/validateEnv";

(async () => {
  if (!validateEnv()) return;

  const BOT = new Client();

  BOT.on("ready", () => console.log("Connected to Discord!"));

  await connectDatabase();

  await BOT.login(process.env.BOT_TOKEN);
})();

```

If you try `npm run build` again, you will see the same error message as before. This is because while we know the environment variable exists, TypeScript still cannot infer it. The validation function is set up to exit the process if the environment variable is missing, so we are going to tell TypeScript that it is definitely a string.

Back in your `connectDatabase.ts` file, within the `connect` function use `process.env.MONGO_URI as string` to coerce the type into `string`. The error should go away, and you can now run `npm run build` and `npm start`. 

You should see the messages you wrote for both the Discord and MongoDB connections print in your terminal.

## The "message" Event

While you are making great progress on your bot, it still does not _do_ anything. In order for the bot to respond to messages, you will need another event handler. 

The logic in this one will be a bit more complicated, so you should create a separate module for it. Create an `events` folder in the `src` directory.

Within your `events` folder, create an `onMessage.ts` file. At the top, import the `Message` class from discord.js with `import { Message } from "discord.js";`. This class will serve as your type definition.

Then create an exported function called `onMessage`. The function should be asynchronous and take a `message` parameter with the `Message` type. Your function will look like this:

```ts
import { Message } from "discord.js";

export const onMessage = async (message: Message) => {

};

```

Before diving in to the logic for this function, you should attach it to the event listener. Back in your `index.ts` file, import your new function with `import { onMessage } from "./events/onMessage";`.

Next to your existing `.on("ready")` listener, add a `BOT.on("message")` listener. For the "message" event, the callback takes a `message` argument which you can pass to your new `onMessage` function:

```ts
BOT.on("message", async (message) => await onMessage(message));
```

We should test that this works. Head back to your `onMessage.ts` file. Inside your `onMessage` function, add `console.log(message.content)`. The `.content` property on the `Message` class contains the text content sent in the message.

Use `npm run build` and `npm start` to get your bot running again, and then send "Hello" in a Discord channel the bot can see. You should see "Hello" print to your terminal.

## How to Prepare for Commands

I maintain a few Discord bots, and one thing I've discovered that helps keep code maintainable and readable is making the components modular.

### Define an Interface

You will first need to define a common structure for your commands. Create an `interfaces` folder in `src`. Then inside `interfaces` create a file `CommandInt.ts`.

Now you are going to create an interface. In TypeScript, an interface is often used to define the structure of an object, and is one of many tools available for declaring a variable's type.

In your `CommandInt.ts` file, import the Message class from Discord, then declare an interface called `CommandInt` with this syntax:

```ts
import { Message } from "discord.js";

export interface CommandInt {

}
```

Inside this interface, you are going to add three properties:

* `name: string;` – the `name` value will be your command's name. You will use this to trigger the command in the Discord server.
* `description: string;` – the `description` value explains what the command does. You will used this in one of the commands.
* `run: (message: Message) => Promise<void>` – this is the property that will hold the command's logic.

The `run` type definition is a bit tricky, so let's break it down. You have typed it as a function which takes one argument, `message`. That argument should be the `Message` type. You then set the function's `return` type to `Promise<void>`. This means your function will be asynchronous (this is important later) and does not return a value.

### Create a Command List

Next you need a place to store all of your commands. Create a folder called `commands` in the `src` directory, and add a file called `_CommandList.ts`. The underscore here will keep this file at the top of the list.

The `_CommandList.ts` file will need two lines. First, import your `CommandInt` interface, then declare a `CommandList` array. The array will be empty for now, but give it a `CommandInt[]` type so TypeScript knows it will eventually hold your command objects. The file should look like:

```ts
import { CommandInt } from "../interfaces/CommandInt";

export const CommandList: CommandInt[] = [];
```

The purpose of this file is to create an array of your bot's commands which you will iterate over in the message event listener. [There are ways to automate this](https://github.com/BeccaLyria/discord-bot/blob/main/src/utils/readDirectory.ts), but they tend to be unnecessarily complex for smaller bots.

### Check for Commands

Back in your `onMessage.ts` file, you should start working on the logic to check messages for commands.

The first step is to ensure that your bot ignores its own messages, as well as the messages of other bots. This helps prevent endless cycles where the bot is responding to itself. 

The `message` object has an `author` property, which represents the Discord user that sent the message. The `author` property has a `bot` property, which is a Boolean that indicates the author is a bot account. Add a step to check if this property is true:

```ts
if (message.author.bot) {
  return;
}
```

You also want to prevent people from accidentally calling your bot's commands. For example, if you have a `help` command, you would not want the bot to respond when someone says "help me please".

This can be avoided by setting a prefix for the bot to detect. Most bots use `!`, but you are welcome to choose whichever prefix you would like. 

Declare a variable `prefix` and assign it your chosen prefix, such as `const prefix = "!";`. Then add a condition to check if the `message.content` does not start with that prefix, and if so `return`.

```ts
const prefix = "!";

if (!message.content.startsWith(prefix)) {
  return;
}

```

Now that you have verified that the message came from a user and is intentionally triggering your bot, you can check to see if the command is valid. 

Using the (currently empty) `CommandList` array will facilitate this process, so import it at the top of your file with `import { CommandList } from "../commands/_CommandList";`.

There are a few ways to iterate through an array – for the live bot, I used a `for..of` loop. Regardless of the loop approach, you will want to check each command in the array against the message content. Here is a loop example:

```ts
  for (const Command of CommandList) {
    if (message.content.startsWith(prefix + Command.name)) {
      await Command.run(message);
      break;
    }
  }
```

This loop iterates through the list of commands, and if the message content starts with the prefix and command name, the bot will call the command's `run` method. 

Remember that you declared the `run` property to be an async function that took the message as an argument. Then, to save on compute time, the loop breaks when it finds a matching command.

## Database Model

There's one more step before you are ready to start writing commands. This bot will track your community members' 100 Days of Code progress. And you need to store that progress in the database.

`mongoose` helps structure your MongoDB records to prevent you from passing malformed or incomplete data into your database.

Start by creating a `models` folder in your `database` directory. In that `models` folder, create a `CamperModel.ts` file. This will be your structure for the user objects.

You first need to import the necessary values from the `mongoose` library. Add `import { Document, model, Schema } from "mongoose";` at the top of the file.

Because you are using TypeScript, you need to create a type definition for your database objects. Create another interface, like you did for your commands, named `CamperInt`.

```ts
export interface CamperInt {

}
```

Your database model will have four properties. Add these to your interface:

* `discordId: string;` – Every user object in Discord has a unique identifier, called a Snowflake, which is used to distinguish them from other users. Unlike a username or discriminator (the four digit number after the username), the `id` value cannot be changed. This makes it the ideal value for linking your stored data to a Discord user.
* `round: number;` – This will represent the "round" the user is on in the challenge. When someone completes 100 days of the challenge, they may choose to undertake the challenge again. When they do, they often refer to it as "round 2", for example. 
* `day: number;` – This represents the day the user is on in the challenge.
* `timestamp: number;` – You will use this value to track when the user last submitted a 100 Days of Code post.

Great! Now you need to define the Schema for your database entries. `mongoose` uses a Schema object to define the shape of the documents that go in to your database collection. The `Schema` import has a constructor, which you will assign to a variable.

```ts
export const Camper = new Schema();
```

This constructor takes an object as its argument, and that object defines the database keys and types. Go ahead and pass in an object similar to what your interface looks like.

```ts
export const Camper = new Schema({
    discordId: String,
    round: Number,
    day: Number,
    timestamp: Number,
})
```

Next you need to create the `model`. In `mongoose`, the `model` object serves to create, read, and update your documents in the MongoDB database. Add `export default model();` at the bottom of your file.

The `model` function takes a few parameters. The first is a string, and is the name to use for the documents in your database. For this collection, use `"camper"`. The second argument is the schema to use for the data – use your `Camper` schema there.

By default, `mongoose` will use the plural version of your `model` name for the collection. In our case, that would be "campers". If you want to change that, you can pass in a third argument of `{ collection: "name" }` to set the collection to `name`.

If you were using JavaScript, this would be enough to get your database model set up. However, because you are using TypeScript, you should take advantage of the type safety. `model()` by default returns a `Document` type of `any`. 

To resolve this, you can pass a generic type into the `model` function. Generic types serve as variables for type definitions, in a sense. You need to set the generic type for your `model` to use your interface. Add the generic type by changing `model` to `model<CamperInt>`.

Just one more step here. Your `CamperInt` interface only defines the properties you set in the MongoDB document, but doesn't include the standard properties. 

Change your `export interface CamperInt` to `export interface CamperInt extends Document`. This tells TypeScript that your type definition is an extension of the existing `Document` type definition – you are essentially adding properties to that structure.

Your final file should look like this:

```ts
import { Document, model, Schema } from "mongoose";

export interface CamperInt {
  discordId: string;
  round: number;
  day: number;
  timestamp: number;
}

export const Camper = new Schema({
  discordId: String,
  round: Number,
  day: Number,
  timestamp: Number,
});

export default model<CamperInt>("camper", Camper);

```

As a safety check, use `npm run build` again. You should not see any errors in the terminal.

## How to Write Bot Commands

You are finally ready to start writing some commands! As this is a 100 Days of Code bot, you should start with the command for creating a 100 Days of Code update.

### 100 command

Within your `commands` folder, create a `oneHundred.ts` file. This will hold your 100 Days of Code command. Import your command interface with `import { CommandInt } from "../interfaces/CommandInt";`.

Now declare an exported variable `oneHundred` and give it the `CommandInt` type:

```ts
import { CommandInt } from "../interfaces/CommandInt";

export const oneHundred: CommandInt = {
    
}
```

Set the `name` property to `"100"`, give it a `description` property similar to `"Creates a 100 Days of Code update"`, and set up the `run` function as `async (message) => {}`.

Now for the logic within the function. Your logic will need a few properties from the `message` object to work, so go ahead and destructure those out: `const{ author, channel, content } = message;`.

When a user calls this command, it should look something like this:

> !100 Here is my 100 Days of Code update.

You will want to extract that text without the `!100` part. There are a few was to do this – we are going to slice it out with `const text = content.split(" ").slice(1).join(" ")`.  Using the previous example, `text` would now hold the string `"Here is my 100 Days of Code update."`.

Time for some database work. Import your `CamperModel` with `import CamperModel from "../database/models/CamperModel"`. Note that you are importing the default export, instead of a module.

Now you need to see if the user has a record in your database. Use `let targetCamperData = await CamperModel.findOne()` to prepare for this. 

The `.findOne()` method is used to query the collection for a single record, and takes an object to filter the query. These queries support MongoDB's syntax for advanced searching, but in this case you only need to find the record by the user's `discordId`. Add `{discordId: author.id}` as the parameter for the `findOne()`.

What happens if the user's record does not exist yet? If this is their first time using the command, they will not have a document in the database. Add an `if` condition to check if `targetCamperData` does not exist:

```ts
if (!targetCamperData) {

}
```

In this block, you are going to reassign `targetCamperData` to a new document with `targetCamperData = await CamperModel.create()`. You use the `.create()` method to generate and save a new document. The method takes an object as the first argument – that object is the document to create. Pass the following object to the method:

```ts
targetCamperData = await CamperModel.create({
  discordId: author.id,
  round: 1,
  day: 0,
  timestamp: Date.now()
});
```

Whether the record exists already or has just been created, your next step is to update it. After your `if` block, add a line to increment the `day` value: `targetCamperData.day++`.

What happens if the user is on day 100? They should not be able to go to day 101, as the challenge is only a hundred days long. You will need to add logic for that. If the user is above day 100, you want to set their day to 1 and increase their round:

```ts
targetCamperData.day++;
if (targetCamperData > 100) {
  targetCamperData.day = 1;
  targetCamperData.round++;
}

```

Now update the timestamp with `targetCamperData.timestamp = Date.now();`. This may seem redundant, since you did this step in the `create` method, but this ensures that the timestamp is updated if the data already existed.

You need to save the changes you made to the document. Add `await targetCamperData.save();` to do this – `mongoose` will then save your changes to the document in MongoDB.

Now you will construct the message the bot should send. To do this, you are going to use a message embed. Message embeds are special message formats that are available to Discord bots, which offer additional formatting options and styling.

Start by adding the `MessageEmbed` class to your imports with `import { MessageEmbed } from "discord.js";`. Then, after your database logic, create a new message embed with `const oneHundredEmbed = new MessageEmbed();`. Time to start setting the values of the embed.

The embed title appears as large text at the top of the embed. Set the title to "100 Days of Code" with `oneHundredEmbed.setTitle("100 Days of Code");`.

The embed description appears as standard text below the title. Set this to the user-provided text with `oneHundredEmbed.setDescription(text);`.

The embed author appears above the title, and is used to indicate who generated the embed. You will set this with `oneHundredEmbed.setAuthor()`. 

This method takes a few arguments, and you will use the first two. The first argument is the author's name. Set this to `author.username + "#" + author.discriminator`.  This will display in the same way that you see a user in Discord: `nhcarrigan#0001`.  

Set the second argument to `author.displayAvatarUrl()`. This is a method provided by discord.js to fetch the URL for the author's avatar image.

Embed fields are additional title-description pairs that can be nested within the embed, and optionally inlined. These can be created with the `.addField()` method, which takes up to three arguments. The first argument is the field title, the second argument is the field description, and the third argument is an optional Boolean to set the field as inline. 

Add two fields to your embed. The first is `oneHundredEmbed.addField("Round", targetCamperData.round, true);`, and the second is `oneHundredEmbed.addField("Day", targetCamperData.day, true);`.

You can add a footer to an embed and appears at the bottom in small text. Set the footer to the data's timestamp with `oneHundredEmbed.setFooter("Day completed: " + new Date(targetCamperData.timestamp).toLocaleDateString();`.  The `toLocaleDateString()` method will take a `Date` object and convert it to a locale-specific string based on the location of your bot's server.

Now you need to send that message embed. The `channel` property you extracted from the `message` value earlier represents the Discord channel in which the message was sent. This object has a `.send()` method, which you can use to have the bot send a message back to that channel. Use `await channel.send(oneHundredEmbed)` to send your new embed to that channel.

To keep the channel clean, add an `await message.delete()` to have the bot delete the message that triggered the command. Your final code should look like this:

```ts
import { CommandInt } from "../interfaces/CommandInt";
import CamperModel from "../database/models/CamperModel";
import { MessageEmbed } from "discord.js";

export const oneHundred: CommandInt = {
  name: "100",
  description: "Creates a 100 Days of Code update",
  run: async (message) => {
    const { author, channel, content } = message;
    const text = content.split(" ").slice(1).join(" ");

    let targetCamperData = await CamperModel.findOne({ discordId: author.id });

    if (!targetCamperData) {
      targetCamperData = await CamperModel.create({
        discordId: author.id,
        round: 1,
        day: 0,
        timestamp: Date.now(),
      });
    }

    targetCamperData.day++;
    if (targetCamperData.day > 100) {
      targetCamperData.day = 1;
      targetCamperData.round++;
    }
    targetCamperData.timestamp = Date.now();
    await targetCamperData.save();

    const oneHundredEmbed = new MessageEmbed();
    oneHundredEmbed.setTitle("100 Days of Code");
    oneHundredEmbed.setDescription(text);
    oneHundredEmbed.setAuthor(
      author.username + "#" + author.discriminator,
      author.displayAvatarURL()
    );
    oneHundredEmbed.addField("Round", targetCamperData.round, true);
    oneHundredEmbed.addField("Day", targetCamperData.day, true);
    oneHundredEmbed.setFooter(
      "Day completed: " +
        new Date(targetCamperData.timestamp).toLocaleDateString()
    );

    await channel.send(oneHundredEmbed);
    await message.delete();
  },
};

```

If you remember, you created a list to hold all of your commands. You need to add your new command to that list. Head back to your `_CommandList.ts` file. Import your new command with `import { oneHundred } from "./oneHundred";`, then add `oneHundred` to your empty `CommandList` array:

```ts
import { CommandInt } from "../interfaces/CommandInt";
import { oneHundred } from "./oneHundred";

export const CommandList: CommandInt[] = [oneHundred];

```

Now you can test it out! Use `npm run build` and `npm start` to get the bot started. Try sending `!100 This is my first post!` in the channel. The bot should respond with an embed and delete your message.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-160.png)
_You can see the embed, with the author, title, description, fields, and footer._

### View command

What happens if a user forgets if they submitted or not, or wants to see what day they are on? You should add a command to view current 100 Days of Code progress.

In your `commands` directory, create a `view.ts` file. Like before, import your command interface and CamperModel, and create a new command called `view`. Set the `name` to `"view"`, the `description` to something like "View your current 100 Days of Code progress", and the `run` command to `async (message) => {}`.

You won't need the message content for this command, so extract the `author` and `channel` values from the `message` like you did before: `const { author, channel } = message;`.

Just like the 100 command, you need to fetch the user's data from the database. This time, however, if the data does not exist you will not be creating it – so you can use `const` here instead of `let`: `const targetCamperData = await CamperModel.findOne({ discordId: author.id });` 

Now, if the user doesn't have a data record yet, they haven't started the challenge with the bot. You should send a message to let them know how to do this. 

```ts
if (!targetCamperData) {
  await channel.send("You have not started the challenge yet.");
  return;
}

```

Construct an embed, similar to the one you built for the 100 command. Don't forget to import the `MessageEmbed` class!

```ts
    const camperEmbed = new MessageEmbed();
    camperEmbed.setTitle("My 100DoC Progress");
    camperEmbed.setDescription(
      `Here is my 100 Days of Code progress. I last reported an update on ${new Date(
        targetCamperData.timestamp
      ).toLocaleDateString()}.`
    );
    camperEmbed.addField("Round", targetCamperData.round, true);
    camperEmbed.addField("Day", targetCamperData.day, true);
    camperEmbed.setAuthor(
      author.username + "#" + author.discriminator,
      author.displayAvatarURL()
    );
```

A couple of key differences here. Instead of taking a text input from the user, you are using a fixed description value to indicate this is a `view` embed instead of a `100` embed. Since you use the timestamp in the description, you do not need to add a footer.

Just like before, send the embed to the message channel and delete the original message. Your final file should be:

```ts
import { CommandInt } from "../interfaces/CommandInt";
import CamperModel from "../database/models/CamperModel";
import { MessageEmbed } from "discord.js";

export const view: CommandInt = {
  name: "view",
  description: "Views your 100 Days of Code progress.",
  run: async (message) => {
    const { author, channel } = message;

    const targetCamperData = await CamperModel.findOne({
      discordId: author.id,
    });

    if (!targetCamperData) {
      await channel.send("You have not started the challenge yet.");
      return;
    }

    const camperEmbed = new MessageEmbed();
    camperEmbed.setTitle("My 100DoC Progress");
    camperEmbed.setDescription(
      `Here is my 100 Days of Code progress. I last reported an update on ${new Date(
        targetCamperData.timestamp
      ).toLocaleDateString()}.`
    );
    camperEmbed.addField("Round", targetCamperData.round, true);
    camperEmbed.addField("Day", targetCamperData.day, true);
    camperEmbed.setAuthor(
      author.username + "#" + author.discriminator,
      author.displayAvatarURL()
    );

    await channel.send(camperEmbed)
    await message.delete();
  },
};

```

Add your new `view` command to your `_CommandList.ts` file with an import, and put the command in the `CommandList` array. Then use `npm run build` and `npm start` to test your new changes. Send "!view" in your channel and you should see the bot respond:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-161.png)

### Edit command

Unfortunately, if a user makes a typo in their 100 Days of Code post, they can't edit the message because the bot sent it. But you can add a command that will allow them to do this.

Create an `edit.ts` file in your `commands` directory. Import your command interface and declare a new command called `edit`. Set the `name` to `"edit"`, the `description` to something like "Edits a previous 100 Days of Code post", and prepare the `run` function as you have before.

Within the function, extract the `author`, `channel`, and `content` properties from the `message` object.

The `edit` command will take a Discord message id, followed by the updated text to use. You can destructure those from the message content with `const [, targetId, ...text] = content.split(" ");`. 

The first element in the array would be the `!edit` command call, which is not needed for this command so you do not need to assign it to a value. The `targetId` element would be the id of the message to edit. `...text` that uses the spread operator to assign the remaining message content to the `text` variable, as an array.

Now you need to use the `targetId` to get the actual message from Discord. The `channel` value has a `messages` property which represents all of the messages sent in that channel. You can use the `fetch` method on that `messages` property to get a specific message (or multiple messages). Set this up as `const targetMessage = await channel.messages.fetch()`. 

The `.fetch()` method can take an object containing the options for the fetch request, or it can take a string as the `id` of the message to fetch. Because you have the `id`, and are only fetching one message, you can pass `targetId` to the `.fetch()` method as the only parameter.

It is possible that the `targetMessage` does not exist. For example, if the user provided an invalid id string (or no id string at all). You'll need to add logic to check if the `targetMessage` is not found:

```ts
    if (!targetMessage) {
        await channel.send("That does not appear to be a valid message ID.");
        return;
    }
```

Now that you have asserted that the message exists, you can start working with the properties. Because your bot sends the message as an embed, the `content` property you are used to working with will be empty. Instead, you can find the embed within the `embeds` property.

The `embeds` property is an array of `MessageEmbed` objects. Since you wrote the bot's code to only send one embed, you can access that embed with `const targetEmbed = targetMessage.embeds[0];`.

Now that you have the embed, you need to confirm that the embed is from one of that user's 100 Days of Code posts. Thankfully, you set the user as the author of the embed. You can check if the embed's author information does not match the message author's information:

```ts
    if (
      targetEmbed.author?.name !==
      author.username + "#" + author.discriminator
    ) {
      await channel.send(
        "This does not appear to be your 100 Days of Code post. You cannot edit it."
      );
      return;
    }
```

You have accounted for the message belonging to a different user (or not having the correct embed entirely), so now you can edit the embed. 

Like you did before, set the description of the embed with the `.setDescription()` method. You'll need to use `.join(" ")` on the `text` variable this time, since it is currently an array. `targetEmbed.setDescription(text.join(" "));`

Rather than sending a new message, you need to edit the existing message. You have the existing message stored in `targetMessage`, so you can use the `.edit()` method to change that message directly. 

`await targetMessage.edit(targetEmbed);` will change the message's embed to your modified version. Then delete the message that triggered this command with `await message.delete();`. Your command should look like this:

```ts
import { CommandInt } from "../interfaces/CommandInt";

export const edit: CommandInt = {
  name: "edit",
  description: "Edits a previous 100 Days of Code post.",
  run: async (message) => {
    const { author, channel, content } = message;
    const [, targetId, ...text] = content.split(" ");

    const targetMessage = await channel.messages.fetch(targetId);

    if (!targetMessage) {
      await channel.send("That does not appear to be a valid message ID.");
      return;
    }

    const targetEmbed = targetMessage.embeds[0];

    if (
      targetEmbed.author?.name !==
      author.username + "#" + author.discriminator
    ) {
      await channel.send(
        "This does not appear to be your 100 Days of Code post. You cannot edit it."
      );
      return;
    }

    targetEmbed.setDescription(text.join(" "));

    await targetMessage.edit(targetEmbed);
    await message.delete();
  },
};

```

Add the command to your `_CommandList.ts` file, importing it and adding the variable to the array. Then use `npm run build` and `npm start` to run the bot again.

To grab a message ID, you should have Developer Mode enabled in your Discord client. If you have not done so, visit your settings and select the "Advanced" section. Toggle "Developer Mode" on:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-162.png)

Then head back to your channel and right click on your original 100 Days of Code message. You should see an option in the context menu to copy the message ID:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-164.png)

Select that option and you will get an ID (mine was `855559921666621441`). Then in the same channel, use `!edit 855559921666621441 This is an edited post!`, replacing my value with the one you got from the "Copy ID" option. The bot should edit the existing embed with your new content.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-165.png)

### Help command

You are almost there! One more command to go. Many bots have a `help` command, which returns a list of available commands. You should add one to your bot as well.

One last time, create a `help` file in your `commands` directory. Import your `CommandInt` interface and set up your command as `help`. Set the `name` to `"help"`, and the `description` to something like `"Returns information on the bot's available commands."`. Set up your `run` function. 

This time you only need the message's `channel` property, so no need to destructure anything here. Instead, import the `MessageEmbed` class from `discord.js`, and go ahead and import your command list too: `import { CommandList } from "./_CommandList";`.

Construct a new `MessageEmbed` and assign it to a `helpEmbed` variable. Set the `title` to `"Available Commands:"` and the description to something similar to `"These are the available commands for this bot."`.

Now you need to add a field to the embed and dynamically generate the list of commands. Start by adding the field with `helpEmbed.addField()`. Use the first parameter to set the field name to `"Commands:"`. For the description (the second parameter), you will use the `CommandList` array to generate a readable list of commands.

```ts
    helpEmbed.addField(
      "Commands:",
      CommandList.map((el) => `\`!${el.name}\`: ${el.description}`).join("\n")
    );
```

The process here is two-part. First, using the built-in array method `.map`, you are creating a new array from your array of `CommandInt` objects. This array contains strings formatted using Markdown so the command name and description are readable. The string for your help command would look like:

> `!help`: Returns information on the bot's available commands.

You are then joining that array of strings with a new-line separator, which will create a vertical list of commands in a single string (embed fields require strings for the description).

Send the embed to the channel. Because you did not destructure the `channel` property out of the `message` object, you will need to use `message.channel.send(helpEmbed);` directly. 

This time, do not delete the original message – you did not add an author to the help embed, so preserving the original message helps moderators see who used the command. Your help command should look like:

```ts
import { CommandInt } from "../interfaces/CommandInt";
import { MessageEmbed } from "discord.js";
import { CommandList } from "./_CommandList";

export const help: CommandInt = {
  name: "help",
  description: "Returns information on the bot's available commands.",
  run: async (message) => {
    const helpEmbed = new MessageEmbed();
    helpEmbed.setTitle("Available Commands!");
    helpEmbed.setDescription(
      "These are the available commands for this bot."
    );
    helpEmbed.addField(
      "Commands:",
      CommandList.map((el) => `\`!${el.name}\`: ${el.description}`).join("\n")
    );

    await message.channel.send(helpEmbed);
  },
};

```

Import your `help` command into your `_CommandList.ts` file and add the command to your array. With this final command, your `_CommandList.ts` file should be:

```ts
import { CommandInt } from "../interfaces/CommandInt";
import { oneHundred } from "./oneHundred";
import { view } from "./view";
import { edit } from "./edit";
import { help } from "./help";

export const CommandList: CommandInt[] = [oneHundred, view, edit, help];

```

Use `npm run build` and `npm start` one last time to test this feature. Send `!help` in your channel and the bot should respond:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-167.png)

## Conclusion

Congratulations! You have successfully built a Discord bot for the 100 Days of Code challenge.

If you are interested in exploring further, you can view [the source code](https://github.com/nhcarrigan/100-days-of-code-bot) for the live bot that inspired this tutorial, which includes custom error logging, external error reporting, and a documentation site.

