---
title: How to Build a CRUD Command Line Application With Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-06T15:59:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-command-line-application-with-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-hitesh-choudhary-1261427.jpg
tags:
- name: command line
  slug: command-line
- name: crud
  slug: crud
- name: node js
  slug: node-js
seo_title: null
seo_desc: "By Njoku Samson Ebere\nIf you're looking for a tutorial to teach you the\
  \ basics of Nodejs and the command line, you're in the right place.  \nYou can use\
  \ JavaScript to build almost any software (web, mobile, bots, and so on). The reason\
  \ is that compute..."
---

By Njoku Samson Ebere

If you're looking for a tutorial to teach you the basics of [Nodejs](https://nodejs.org/en/) and the command line, you're in the right place.  
  
You can use JavaScript to build almost any software (web, mobile, bots, and so on). The reason is that computers no longer depend on browsers only to understand JavaScript code. Check out this article to see [How Computers Understand JavaScript Code](https://dev.to/ebereplenty/how-computers-understand-javascript-code-k1n). 

Node.js is used to run backend applications that are written in JavaScript.   
  
I will teach you how to build a command line application that can read, write, edit, and delete data using Node.js. It will not require connecting to external databases like MySQL, MongoDB, Postgresql, and so on. See the project [here](https://github.com/EBEREGIT/Nodejs_CLI_app).  
  
By the end of the article, you should be able to set up a basic Node project, manipulate files, use modules, navigate promises, collect input, and so on.

I also added videos to enhance your learning.

## Prerequisites

You do not need any prior programming knowledge to understand this tutorial.

%[https://www.youtube.com/watch?v=RQ4b0Ui1-3o&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=2&t=6s]

## How the Finished Project Will Function

The application that we are going to build will be able to do the following:

* Check if a database exists
* Retrieve data from the database
* Add new data to the database
* Update database with new data
* Remove data from the database

## How to Install Node and NPM

Please go to the [Nodejs website](https://nodejs.org/en/) and download the one recommended for all users. Install it after the download is complete.

Use the command below to check if the installation was successful:

* For Node

```
node -v
```

* For npm

```
npm -v
```

The installation is successful if each command returns a version number.

## How to Setup a  Node.js Project

%[https://www.youtube.com/watch?v=8dlICKn-tQw&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=2]

The steps below will help you set up your project:  
  
Open your terminal or CMD and create the project directory:

```
mkdir node_CLI_app
```

Navigate into the directory:

```
cd node_CLI_app
```

Initialize the project:

```
npm init	
```

It will bring up some questions. Press the Enter button for every prompt.   
  
A new file (`package.json`) should have been added to your project directory. We will use the file to add external code (module) to the project.  
  
Add the following line before the closing curly brace (`}`) to enable ES6 import:

```
"type": "module"
```

That completes the project setup!

## How to Install Dependencies

You will recall that the `package.json` file is for adding external code to the project. This external code is also called Dependencies, Modules, or Packages. It's written by other programmers (usually free of charge) to help others build applications faster. You will find a lot of these on the [npm website](https://www.npmjs.com/).  
  
We need two (2) packages for this project: [inquirer](https://www.npmjs.com/package/inquirer) and [uuid](https://www.npmjs.com/package/uuid). I will show you how to install them in this section.  
  
Installing of packages follows this pattern:

```
npm install <package_name>
```

We can install more than one package at a time by separating the package names with a space:

```
npm install <package_name_1> <package_name_2> <package_name_3>
```

The `install` command can be replaced with `i` for convenience.  
  
So run the following command to install the packages:

```
npm i inquirer uuid
```

Your package.json file should have the following lines of code added to it when the installation is complete:

```javascript

  "dependencies": {
    "inquirer": "^9.1.4",
    "uuid": "^9.0.0"
  }
```

The version numbers may differ, but that’s fine.

You will also notice that a file (`package.lock.json`) and a folder (`node_modules`) have been added. You do not have to worry about them. Just know that they help to manage the external code we just added.

That completes the installation of dependencies!

## How to Create a New File from the Terminal

You can create a file from the terminal using the following command:

* On Mac:

```
touch <file_name>
```

* On Windows:

```
echo.><file_name>
```

You can also create more than one file at a time by separating the files with a space. That is how we will generate the files for this project:

```
touch addData.js removeData.js retrieveData.js updateData.js queryDB.js dbFileCheck.js
```

Each of those files will play a unique role in the application.

* `addData.js` adds data to the database. It also fabricates the database file if it doesn’t exist.
* `removeData.js` removes selected data.
* `retrieveData.js` fetches all data.
* `updateData.js` edits data.
* `queryDB.js` checks if a database exists and executes a function passed to it.
* `dbFileCheck.js` confirms if the database file has been created.

There is one more file that we did not create: the database file (`db.json`). We will auto-generate it using our code.

## How to Check if a File Exists

%[https://www.youtube.com/watch?v=V9dmEXCnY-8&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=3]

Node.js provides a built-in module for manipulating files – [file system](https://nodejs.org/api/fs.html) (fs). One of the methods that the module contains is the `existsSync` method. It returns `true` or `false` depending on if the file has been created. I will use that to check if the `db.json` file is in the project. See the code below:

```javascript
  import fs from "fs";
  import { exit } from "process";  
  
  if (fs.existsSync("db.json")) {
    console.log("File exists!");
    exit(1);
  }
```

The `exit` method terminates a process.

That is what we want to do in the `dbFileCheck.js` file. However, we want to invert the result by adding a `!` before the `fs.existsSync` method like this:

```javascript
  import fs from "fs";
  import { exit } from "process";  
  
  if (!fs.existsSync("db.json")) {
    console.log("File does not exist!");
    exit(1);
  }
```

This will be necessary when building other functionalities like updating and deleting data. 

So how will those files gain access to this code? It is through a modular structure. That entails bundling this code and making it accessible through other files in the project. The export command makes this possible:

```
import fs from "fs";
import { exit } from "process";

export default function dbFileCheck() {
  if (!fs.existsSync("db.json")) {
    console.log("Database is Empty. Create some data!");
    exit(1);
  }
}
```

The code above puts the code in a function (`dbFileCheck`) and exports it using the `export` command. This function can now be imported and used in other files within this project.

Note that the `default` keyword is necessary for the first export from a file.

## How to Query the Database

Another method the `file system` has is the `readFile` method. It returns the content of any file passed to it. 

%[https://www.youtube.com/watch?v=ZmckWr9sH-w&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=4]

The `readFile` method takes in two parameters: the file to be read and a callback function that returns the result of the operation.  
  
We will use the following code to retrieve data from our database:

```javascript
import fs from "fs";

fs.readFile("db.json", function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data.toString());
});
```

The code above imports the file system module and tries to read the database file. If there is an error, it will return the error. If there are no errors, it will return the data it got. 

The `.toString()` method attached to the data returned (`data.toString()`) is because the data retrieved is of the type `buffer` by default, which is not readable.

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675074450995_Screenshot+2023-01-30+at+11.25.25.png)
_buffer output_

Open your project in a code editor and paste that code into the `queryDB.js` file.  
  
Run the command below to see if it is working:

```
node queryDB
```

The command above will execute every code in the `queryDB.js`. The `.js` extension is optional. It will run either way.

The result of that operation will be an error because we do not have the file.

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675074558543_Screenshot+2023-01-30+at+11.28.47.png)

You can create the `db.json` file, add some content, and check the output.  
  
But we do not want our app to try to read the database file if it has not been generated. So use the `existsSync` method to check if the file has been created. See how I use it in the code below:

```javascript
    import fs from "fs";

    if (fs.existsSync("db.json")) {
      fs.readFile("db.json", function (err, data) {
        if (err) {
          console.log(err);
        }
        console.log(data.toString());
      });
    } else {
      console.log("No data available!");
    }
```

The code above checks if the file exists by passing the file name (`db.json`) to the `fs.existsSync` method. If it is true, then it reads the file. If it is false, it returns a string.

Now that we have that clean code, we want to make it even more robust.

Since we are building a CRUD application, we must have access to and keep track of the data returned. I have introduced a new variable in the code below to make that happen:

```javascript
    import fs from "fs";

    let info = [];
    if (fs.existsSync("db.json")) {
      fs.readFile("db.json", function (err, data) {
        if (err) {
          console.log(err);
        }
        info = JSON.parse(data.toString());
        console.log(info);
      });
    } else {
      console.log("No data available!");
    }


```

The code above now has a variable, `info`. It keeps track of the data returned. I passed the data through the `JSON.parse` method to convert the data from string to array. 

We can now manipulate the `info` as we deem fit. We have to export the code and accept a function to make this possible. That function will take the `info` variable as input and then use it as required.

```javascript
import fs from "fs";

export default async function queryDB(externalFunction) {
  try {
    let info = [];

    if (fs.existsSync("db.json")) {
      await fs.readFile("db.json", function (err, data) {
        info = JSON.parse(data.toString());
        console.log(info);

        if (err) {
          console.log(err);
          return;
        }

        if (externalFunction && !err) {
          externalFunction(info);
          return;
        }
      });
    } else {
      if (externalFunction) {
        externalFunction(info);
        return;
      }
    }
  } catch (error) {
    console.error(`Something Happened: ${error.message}`);
  }
}
```

This code takes in a function and executes it only if there are no errors. However, there will be one exception – when adding data. In that case, the database will be created.

The [`try…catch…`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) block helps pick out errors, and the [`async`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) keywords are used when executing code that will take a long time to run.

The `queryDB.js` will no longer return any output when we execute the `node queryDB` command. But that is fine. We will trigger it from other files.

## How to Add Data to a File

In this section, I will teach you how to add data to the store. The file for this section is the `addData.js` file.

%[https://www.youtube.com/watch?v=vi0unBmidkE&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=5]

We will start by importing all necessary modules:

```javascript
import inquirer from "inquirer";
import fs from "fs";
import { v4 as uuidv4 } from "uuid";
import queryDB from "./queryDB.js";
```

Next, create the boilerplate for the function:

```
export default async function addData(info) {
  try {
    
  } catch (error) {
    console.log("Something went wrong!", error);
  }
}

```

This is similar to what we have done before now. All the code we would write next will go into the `try…` block. The `info` array passed into the function is coming from the `queryDB` file.  
  
The first thing to do in the `try…` block is to collect the data to be stored. We will use [`inquirer`](https://www.npmjs.com/package/inquirer) to do that with the code below:

```javascript
const answers = await inquirer.prompt([
      {
        type: "input",
        name: "name",
        message: "What's your name?",
      },
      {
        type: "number",
        name: "phone",
        message: "What's your phone?",
      },
      {
        type: "list",
        name: "age",
        message: "Are you an adult?",
        choices: [
          { name: "Y", value: "Adult" },
          { name: "N", value: "Minor" },
        ],
      },
    ]);
```

The `inquirer` package helps in building interactive command line interfaces. It contains a method called `prompt` used to ask for inputs. It takes an array of questions in object format. Each object must have the `name`, `type`, and `message` keys. 

The `choices` key is optional. It is used when there is a list of options.

So the code above collects three (3) inputs (name, phone, and age) and stores them in a variable called `answers`.

Next, we assign this set of input a unique ID by calling the `uuidv4()` function and push everything into the `info` array:

```javascript
    const data = {
      id: uuidv4(),
      name: answers.name,
      phone: answers.phone,
      age: answers.age,
    };
    info.push(data);
```

Finally, we check if the database file exists. We will update the database with the new data if the file has been created or create it and add the new data if it is false.

```javascript
    if (fs.existsSync("db.json")) {
      createDetails(info);
    } else {
      fs.appendFile("db.json", "[]", (err) => {
        if (err) {
          console.log("Could not create db.json", err);
          return;
        }
        createDetails(info);
      });
    }
```

The `createDetails` function will be used to overwrite the database data. I will create that in a bit.  
  
In the `else` (if the file doesn’t exist) block, I created the file using the file system’s `appendFile` method. This method is used to create a file if it is not there already and add or append data to the bottom of the file. 

I am appending `[]` to the file. So the newly created file will have just `[]` in it. I called the `createDetails` function next to add the data collected from the CLI.  
  
Please type the following code for the createDetails function below the addData function. 

```javascript
async function createDetails(info) {
  await fs.writeFile("db.json", JSON.stringify(info), function (err) {
    if (err) {
      console.log(err);
    }
    console.log("saved!");
  });
}
```

This function uses the file system’s `writeFile` method to overwrite the database with current data. I am using `JSON.stringify` to convert the `info` variable to a string because that is the acceptable format when writing to a file. That also explains why I used `JSON.parse` to convert it to the original type when I retrieved it in the previous section.  
  
`writeFile` is different from `appendFile` because `writeFile` overwrites a file while `appendFile` adds to the existing content. They are similar in that both methods will create the file if it has not been created.

The last thing to do in this file is invoke or call the function. The way to do that is by typing its name followed by opening and closing braces like this:

```javascript
addData();
```

This might work fine, but it wouldn’t do what we want. We need to pass the function as an argument into the `queryDB` like this:

```javascript
queryDB(addData);
```

Now, the `addData` will be able to communicate with the `queryDB` function.

## How to Test the `addData` File

Run the command below to test if the `addData` file works as expected:

```
node addData
```

It will prompt you for answers. Fill in the answers. After that, your screen should look like mine:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675241012883_Screenshot+2023-02-01+at+09.42.57.png)
_addData output_

It should also have auto-generated a `db.json` file with the data you just added.

And that is it for the `addData` file!

## How to Retrieve Data

This section shows how to get the content of the database. All you need to achieve this functionality is the code below:

```javascript
import queryDB from "./queryDB.js";

queryDB();
```

What the code does is import the `queryDB` function and invoke it. Paste the code in the `retrieveData.js` file and execute the file with:

```
node retrieveData
```

It will return an output similar to this:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675319554801_Screenshot+2023-02-02+at+07.29.43.png)
_retrieveData.js output_

You might wonder: why did I not call this function in the `queryDB` file? The reason is that the file performs more than just retrieving data. Calling the `queryDB` function in its file will alter the result of other files.

## How to Edit Data

This section will now focus on how to update data. The pattern to follow here is:

* Collect the user’s ID.
* Search for the user.
* Return the user’s data if the user exists, and set it as the default option.
* Ask for updated info. The initial value will be kept if the user presses the `Enter` key.
* Finally, overwrite the database with the updated information.

%[https://www.youtube.com/watch?v=UmshAmmU-44&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=6]

Let’s get to it…  
  
Navigate into the `updateData.js` file and paste the following code:

```
import inquirer from "inquirer";
import fs from "fs";
import queryDB from "./queryDB.js";
import dbFileCheck from "./dbFileCheck.js";

export default async function updateData(info) {
  dbFileCheck();

  try {
    
  } catch (error) {
    console.log("Something went wrong!", error);
  }
}
```

This is the boilerplate for the `updateData` function. The new thing here is the `dbFileCheck` function (made it a while ago) to terminate an operation if the database has not been created.   
  
The rest of the code will be inside the `try…` block.

The first thing is to collect the user ID with this code:

```
    const answers = await inquirer.prompt([
      {
        type: "input",
        name: "recordID",
        message: "Enter Record ID",
      },
    ]);
```

The second is to search for the user:

```
    let current;

    info.forEach((element) => {
      if (element.id === answers.recordID) {
        current = element;

        updateDetails(current, info);
      }
    });
```

The code above searches through the users (`info`) and sets the user found to the `current` variable. Finally, the `updateDetails` is called to collect the updated information and overwrite the database with the new data.

### How to build the `updateDetails` function

This part will show how to keep track of a user’s initial data while collecting new data. It will update the database with the new data afterward.  
  
The following code is the boilerplate for the function:

```
async function updateDetails(current, info) {
  try {
    
  } catch (error) {
    console.log("Something went wrong!", error);
  }
}
```

This code goes under the `updateData` operation.  
  
The code below goes into the `try…` block. It is for collecting updated information from the user.

```
  const feedbacks = await inquirer.prompt([
      {
        type: "input",
        default: current.name,
        name: "name",
        message: "What's your name?",
      },
      {
        type: "number",
        default: current.phone,
        name: "phone",
        message: "What's your phone?",
      },
      {
        type: "list",
        default: current.age,
        name: "age",
        message: "Are an adult?",
        choices: [
          { name: "Y", value: "Adult" },
          { name: "N", value: "Minor" },
        ],
      },
    ]);
```

The `default` key is new. It holds input that will be used if the user doesn’t provide one. It keeps track of the user’s current data for this code. So the user can hit the `Enter` button instead of entering the former value again.  
  
The user’s details should be updated accordingly using this code:

```
    current.name = feedbacks.name;
    current.phone = feedbacks.phone;
    current.age = feedbacks.age;
```

Finally, overwrite the database with the new value:

```
await fs.writeFile("db.json", JSON.stringify(info), function (err) {
      if (err) {
        console.log(err);
      }
      console.log("updated");
    });
```

Call the `updateData` function to bring everything together:

```
queryDB(updateData)
```

### How to test the `updateData` file

Run the command below to see how the `updateData` function performs:

```
node updateData
```

It will prompt you for an ID. Enter the ID of any record in the database.  
  
It will then prompt for updated information about the user. Fill in the information and press `Enter` for any detail that does not need an update. The terminal should look like this at the end:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675324018105_Screenshot+2023-02-02+at+08.45.07.png)
_updateData Output_

That wraps it up for the `updateData` file. Records can now be updated.

## How to Delete Data

A CRUD application cannot be completed without the DELETE part. That will be the focus here. It will borrow a bit from the previous sections. So it will not be too much to grasp.

%[https://www.youtube.com/watch?v=JptWEtAtOeA&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=7]

You'll begin by typing the following code in the `removeData.js` file:

```
import inquirer from "inquirer";
import fs from "fs";
import queryDB from "./queryDB.js";
import dbFileCheck from "./dbFileCheck.js";

export default async function removeData(info) {
  dbFileCheck();

  try {
    const answers = await inquirer.prompt([
      {
        type: "input",
        name: "recordID",
        message: "Enter Record ID",
      },
    ]);

    let remnantData = [];
    info.forEach((element) => {
      if (element.id !== answers.recordID) {
        remnantData.push(element);
      }
    });

    fs.writeFile("db.json", JSON.stringify(remnantData), function (err) {
      if (err) {
        console.log(err);
      }
      console.log("Deleted!");
    });
  } catch (error) {
    console.log("Something went wrong!", error);
  }
}

```

First, the code above collects an ID.  
  
Next, it uses the ID to search the database data and keeps only data with a different ID in the `remnantData` array.  
  
Finally, it overwrites the database with the updated data.  
  
Call the removeData function at the bottom to put everything together like this:

```
queryDB(removeData)
```

Now try to test the file using this command:

```
node removeData
```

The is my output:

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675329363353_Screenshot+2023-02-02+at+10.15.12.png)
_removeData Ouput_

## Conclusion

The best way to learn to program is by building. And some of the best projects to build are CRUD applications because they cover the basics of what a professional project requires. That is what I have done in this tutorial.  
  
I have taught you the basics of Nodejs by building an application that creates, reads, updates, and deletes records. I covered concepts such as reading files, writing to files, loops, conditional statements, modules, and CLI operations.  
  
All the files for this tutorial are on [GitHub](https://github.com/EBEREGIT/Nodejs_CLI_app).  
  
You now have all the basics needed to start building applications using Nodejs. Something I will like you to try is to update or delete more than one record at a time.

I have some other tutorials on Nodejs, and I suggest that you follow them in this order to grow your skill:

* [How to Build a Secure Server with Node.js and Express and Upload Images with Cloudinary](https://www.freecodecamp.org/news/build-a-secure-server-with-node-and-express/)
* [How to Build and Deploy a Backend App with Express, Postgres, Github, and Heroku](https://www.freecodecamp.org/news/how-to-build-a-backend-application/)
* [How to Build a Full-Stack Authentication App With React, Express, MongoDB, Heroku, and Netlify](https://www.freecodecamp.org/news/how-to-build-a-fullstack-authentication-system-with-react-express-mongodb-heroku-and-netlify/)

Happy Building!


