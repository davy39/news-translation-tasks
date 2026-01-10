---
title: How to Create an npm Library
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2025-02-07T15:33:19.302Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-npm-library
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738941301640/7189d889-387d-4bd2-bf5c-2cbcbd17faad.png
tags:
- name: npm
  slug: npm
- name: Yarn
  slug: yarn
- name: software development
  slug: software-development
seo_title: null
seo_desc: In the world of JavaScript development, npm (Node Package Manager) has become
  an essential tool for managing dependencies and sharing reusable code. Whether you're
  building a simple website or a complex web application, npm libraries help streamline
  ...
---

In the world of JavaScript development, **npm** (Node Package Manager) has become an essential tool for managing dependencies and sharing reusable code. Whether you're building a simple website or a complex web application, npm libraries help streamline development by providing pre-built solutions to common problems.

Another popular package manager is **Yarn**, which offers faster and more reliable dependency management while maintaining compatibility with the npm ecosystem.

In this article, we'll explore what npm libraries are, their benefits, and how they enhance the JavaScript and React ecosystem. We'll also go through a practical step-by-step guide on creating, publishing, and using your own npm library in a React project. We’ll also compare npm and Yarn, showing how you can use either of them effectively in your workflow.

By the end of this tutorial, you'll have a clear understanding of how to package and distribute your own code, making it reusable across multiple projects and even available to the wider developer community.

## **Table of Contents**

1. [What is npm?](#heading-what-is-npm)
    
    * [How npm works](#heading-how-npm-works)
        
    * [The role of the `package.json` file](#heading-the-role-of-packagejson)
        
    * [Key npm Commands](#heading-key-npm-commands)
        
2. [Why Use npm Libraries?](#heading-why-use-npm-libraries)
    
    * [Code reuse and modularization](#heading-code-reuse-and-modularization)
        
    * [Simplified dependency management](#heading-simplified-dependency-management)
        
    * [Community-driven ecosystem](#heading-community-driven-ecosystem)
        
3. [Introducing Yarn: An Alternative to npm](#heading-introducing-yarn-an-alternative-to-npm)
    
    * [What is Yarn?](#heading-what-is-yarn)
        
    * [Differences between npm and Yarn](#heading-differences-between-npm-and-yarn)
        
    * [When to use Yarn instead of npm](#heading-when-to-use-yarn-instead-of-npm)
        
4. [How to Create Your Own npm Library](#heading-how-to-create-your-own-npm-library)
    
    * [Setting up a new package](#heading-setting-up-a-new-package)
        
    * [Writing modular and reusable code](#heading-writing-modular-and-reusable-code)
        
    * [Adding dependencies and peer dependencies](#heading-adding-dependencies-and-peer-dependencies)
        
5. [How to Publish Your Library to npm](#heading-how-to-publish-your-library-to-npm)
    
    * [Creating an npm account](#heading-creating-an-npm-account)
        
    * [Configuring package.json for Publishing](#heading-configuring-packagejson-for-publishing)
        
    * [Publishing the package](#heading-publishing-the-package)
        
6. [How to Use Your npm Library in a React Project](#heading-how-to-use-your-npm-library-in-a-react-project)
    
    * [Installing your package](#heading-installing-your-package)
        
    * [Importing and using the package in a React component](#heading-importing-and-using-the-library-in-a-react-component)
        
    * [Handling package updates and versioning](#heading-handling-package-updates-and-versioning)
        
7. [Best Practices for npm and Yarn Libraries](#heading-best-practices-for-npm-and-yarn-libraries)
    
    * [Write Meaningful Documentation](#heading-write-meaningful-documentation)
        
    * [Follow Semantic Versioning (SemVer)](#heading-follow-semantic-versioning-semver)
        
    * [Keep Dependencies Up to Date](#heading-keep-dependencies-up-to-date)
        
    * [Write Unit Tests for Your Library](#heading-write-unit-tests-for-your-library)
        
    * [Ensure Cross-Platform Compatibility](#heading-ensure-cross-platform-compatibility)
        
8. [Conclusion & Next Steps](#heading-conclusion)
    
    * [Recap of key points](#heading-recap-of-key-points)
        
    * [Additional resources for npm and Yarn library development](#heading-additional-resources)
        
    * [Encouragement to contribute to open-source](#heading-encouragement-to-contribute-to-open-source)
        

## **What is npm?**

npm (Node Package Manager) is the default package manager for JavaScript and Node.js. It allows developers to install, share, and manage libraries or dependencies that make building applications easier and more efficient.

npm provides access to a vast ecosystem of open-source packages hosted on the **npm registry**, making it one of the largest software repositories in the world.

npm comes bundled with **Node.js**, meaning that once you install Node.js, you automatically have access to npm. You can check if npm is installed by running the following command in your terminal:

```python
npm -v
```

This command should return the version of npm installed on your system.

### **How npm Works**

npm operates through three key components:

1. **The npm Registry** – A public repository that hosts open-source JavaScript packages.
    
2. **The npm CLI (Command Line Interface)** – A tool that allows developers to install, update, and manage packages from the command line.
    
3. **The package.json File** – A metadata file that keeps track of dependencies, scripts, and project configurations.
    

When you install a package using npm, it pulls the package from the registry and saves it in the `node_modules` folder within your project.

For example, to install **Lodash**, a popular utility library, you would run:

```python
npm install lodash
```

This will:

* Download the latest version of `lodash` from the npm registry
    
* Add it to your `node_modules` folder
    
* Update the `package.json` and `package-lock.json` files to reflect the new dependency
    

### **The Role of** `package.json`

The `package.json` file is the heart of any npm project. It serves as a blueprint, containing information about the project, including:

* **Project metadata** (name, version, description)
    
* **Dependencies** (external packages required for the project)
    
* **Scripts** (commands to automate tasks like starting a server or running tests)
    
* **Versioning information** (ensuring compatibility between different versions of dependencies)
    

A typical `package.json` file looks like this:

```json
{
  "name": "my-awesome-project",
  "version": "1.0.0",
  "description": "A sample project demonstrating npm usage",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"No tests specified\" && exit 0"
  },
  "dependencies": {
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "eslint": "^8.0.0"
  },
  "author": "Your Name",
  "license": "MIT"
}
```

* `dependencies` – Lists essential packages required for the application to function.
    
* `devDependencies` – Includes development-only dependencies (for example, testing and linting tools).
    
* `scripts` – Defines CLI commands for automating tasks.
    

To install all dependencies listed in `package.json`, simply run:

```python
npm install
```

This ensures all required packages are downloaded and ready for use.

### **Key npm Commands**

Here are some essential npm commands you’ll use frequently:

| Command | Description |
| --- | --- |
| `npm init -y` | Creates a default `package.json` file |
| `npm install <package-name>` | Installs a package and adds it to `dependencies` |
| `npm install <package-name> --save-dev` | Installs a package and adds it to `devDependencies` |
| `npm uninstall <package-name>` | Removes a package from the project |
| `npm update` | Updates all installed dependencies |
| `npm outdated` | Checks for outdated dependencies |
| `npm run <script-name>` | Runs a script defined in `package.json` |

## **Why Use npm Libraries?**

As modern web development grows in complexity, using npm libraries has become essential for building scalable and maintainable applications. Instead of writing everything from scratch, you can leverage pre-built, tested, and optimized libraries to speed up development and ensure reliability.

In this section, we’ll explore the key advantages of using npm libraries and why they are crucial in JavaScript and React development.

### **Code Reuse and Modularization**

One of the biggest benefits of npm libraries is **code reuse**. Instead of repeatedly writing the same functions or utilities in different projects, developers can:

* ✅ Use existing open-source packages for common functionalities (for example, date formatting, HTTP requests, UI components).
    
* ✅ Create and publish their own reusable libraries to share across multiple projects.
    

For example, instead of manually implementing a function to format dates, you can install a well-maintained package like date-fns:

```python
npm install date-fns
```

Then, you can use it in your project:

```javascript
import { format } from "date-fns";

const formattedDate = format(new Date(), "yyyy-MM-dd");
console.log(formattedDate); // Outputs: 2024-02-04 (or the current date)
```

This modular approach saves time and ensures consistency across projects.

### **Simplified Dependency Management**

npm makes it easy to manage dependencies in a project. Instead of manually downloading and maintaining different versions of external libraries, npm automates this process through the package.json and package-lock.json files.

Some key features include:

🔹 **Automatic installation** – Run `npm install`, and all dependencies are set up.  
🔹 **Version control** – Specify package versions to avoid breaking changes.  
🔹 **Peer dependencies** – Ensure compatibility between different libraries.

For example, here’s how npm helps manage dependency versions in `package.json`:

```json
"dependencies": {
  "react": "^18.0.0",
  "axios": "^1.5.0"
}
```

* `^18.0.0` – Allows minor updates but prevents major breaking changes.
    
* `axios` – Ensures HTTP requests are handled consistently across different projects.
    

To update all dependencies safely, run:

```python
npm update
```

This ensures your project is always running on the latest stable versions.

### **Community-Driven Ecosystem**

npm has an active and growing community, meaning developers around the world contribute and maintain thousands of useful libraries. This results in:

🌎 **Faster development** – No need to reinvent the wheel.  
🛠️ **Well-tested solutions** – Many libraries are battle-tested in production environments.  
📚 **Rich documentation** – Most npm packages come with clear usage instructions and examples.

Popular npm libraries include:

| Library | Purpose |
| --- | --- |
| **React** (`react`) | UI library for building web applications |
| **Axios** (`axios`) | HTTP client for making API requests |
| **Lodash** (`lodash`) | Utility functions for working with arrays, objects, and strings |
| **Express** (`express`) | Web framework for building backend services |
| **Jest** (`jest`) | JavaScript testing framework |

For example, using **Axios** to make an API request:

```javascript
import axios from "axios";

axios.get("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```

This replaces the need for writing complex `fetch` requests with error handling manually.

## **Introducing Yarn: An Alternative to npm**

While **npm** is the default package manager for Node.js, another powerful alternative exists: **Yarn**. Developed by Facebook in 2016, Yarn was created to improve speed, security, and reliability in dependency management.

In this section, we’ll explore what Yarn is, how it differs from npm, and when you might prefer using Yarn over npm.

### **What is Yarn?**

Yarn (**Yet Another Resource Negotiator**) is a package manager that works similarly to npm but with a focus on performance, security, and consistency. It offers:

🚀 **Faster dependency installation** thanks to parallel downloads  
🔐 **More secure package management** using checksum verification  
📦 **Reliable dependency resolution** with an offline cache

To check if you have Yarn installed, run:

```python
yarn -v
```

If you don’t have it yet, you can install it globally using npm:

```python
npm install --global yarn
```

Once installed, you can use it just like npm to manage dependencies.

### **Differences Between npm and Yarn**

Although npm and Yarn serve the same purpose, they have some key differences:

| Feature | npm | Yarn |
| --- | --- | --- |
| **Speed** | Installs packages one at a time | Installs multiple packages in parallel (faster) |
| **Lock File** | `package-lock.json` | `yarn.lock` |
| **Offline Cache** | Not available (by default) | Can install packages from local cache |
| **Security** | Verifies package integrity but lacks checksum enforcement | Uses checksum verification for security |
| **Monorepo Support** | Supports workspaces but not optimized | Built-in support for monorepos with `workspaces` |

#### **Performance Comparison**

When installing dependencies, Yarn is often faster because it downloads packages in parallel, while npm installs them sequentially.

For example, to install all dependencies in a project:

```python
# With npm
npm install

# With Yarn
yarn install
```

Yarn can also install packages from a local cache, meaning it doesn't always need to fetch dependencies from the internet.

#### **Common Yarn Commands vs. npm**

Many npm commands have an equivalent in Yarn:

| Action | npm Command | Yarn Command |
| --- | --- | --- |
| Initialize a new project | `npm init` | `yarn init` |
| Install all dependencies | `npm install` | `yarn install` |
| Install a package | `npm install package-name` | `yarn add package-name` |
| Install a dev dependency | `npm install package-name --save-dev` | `yarn add package-name --dev` |
| Remove a package | `npm uninstall package-name` | `yarn remove package-name` |
| Update all packages | `npm update` | `yarn upgrade` |
| Run a script | `npm run script-name` | `yarn script-name` |

For example, installing `axios` using Yarn:

```python
yarn add axios
```

### **When to Use Yarn Instead of npm**

Yarn is a great choice when:

* **You want faster installations** – Yarn installs multiple packages in parallel, making it faster than npm.
    
* **You need better dependency consistency** – The `yarn.lock` file ensures that all developers use the same dependency versions.
    
* **You're working with monorepos** – Yarn’s built-in **workspaces** make it easier to manage multiple projects within the same repository.
    
* **You want improved security** – Yarn’s checksum verification prevents corrupted packages from being installed.
    

Still, npm has improved significantly in recent years, especially with npm v7+, making it a viable choice for most projects.

#### **Switching Between npm and Yarn**

If your project was originally set up using npm but you want to switch to Yarn, you can:

1️⃣ **Delete** `node_modules` and `package-lock.json`

```python
rm -rf node_modules package-lock.json
```

2️⃣ **Run Yarn to install dependencies**

```python
yarn install
```

This will generate a yarn.lock file, ensuring all dependencies are managed by Yarn moving forward.

Both npm and Yarn are powerful tools for package management. Choosing between them depends on your project’s needs:

✔️ Use **npm** if you want the default, widely used package manager that works well with most projects.  
✔️ Use **Yarn** if you need faster installs, better security, and monorepo support.

Ultimately, both tools allow you to **install, manage, and publish** JavaScript packages efficiently.

## **How to Create Your Own npm Library**

Creating your own npm library is a great way to **share reusable code**, contribute to the open-source community, or even streamline development across multiple projects. In this section, we’ll walk through the step-by-step process of setting up, coding, and preparing a library for publishing on npm.

### **Setting Up a New Package**

Before writing code, you need to set up an npm package. Follow these steps:

#### **Step 1: Create a New Project Folder**

```python
mkdir my-awesome-library
cd my-awesome-library
```

#### **Step 2: Initialize npm**

Run the following command to create a `package.json` file:

```python
npm init
```

You will be prompted to enter details such as:

* Package name
    
* Version
    
* Description
    
* Entry point (default: `index.js`)
    
* Author
    
* License
    

💡 To skip the prompts and create a default `package.json`, use:

```python
npm init -y
```

### **Writing Modular and Reusable Code**

Now, let’s create a simple utility library that provides a function to format dates.

#### **Step 3: Create an** `index.js` File

Inside the project folder, create a file named `index.js` and add the following code:

```javascript
function formatDate(date) {
  if (!(date instanceof Date)) {
    throw new Error("Invalid date");
  }
  return date.toISOString().split("T")[0];
}

module.exports = { formatDate };
```

### **Adding Dependencies and Peer Dependencies**

Your library might depend on external packages. For example, let’s use date-fns for better date formatting.

To install it as a dependency, run:

```python
npm install date-fns
```

Then, modify `index.js` to use `date-fns`:

```javascript
const { format } = require("date-fns");

function formatDate(date) {
  if (!(date instanceof Date)) {
    throw new Error("Invalid date");
  }
  return format(date, "yyyy-MM-dd");
}

module.exports = { formatDate };
```

If you're creating a React-specific library, you should add React as a peer dependency:

```python
npm install react --save-peer
```

This ensures users of your library install React separately, preventing version conflicts.

Before publishing, you should test how your package works when installed as a dependency.

#### **Step 4: Link the Package Locally**

Run the following command in your package folder:

```python
npm link
```

Then, in another project where you want to use your package, navigate to that project and run:

```python
npm link my-awesome-library
```

Now, you can import and use your function:

```javascript
const { formatDate } = require("my-awesome-library");

console.log(formatDate(new Date())); // Output: 2025-02-04 (or the current date)
```

Once you're happy with your package, it's time to **publish it on npm**.

## **How to Publish Your Library to npm**

Now that we’ve created our npm package, the next step is **publishing it to the npm registry** so others can install and use it. In this section, we’ll cover how to publish the package step by step.

### **Creating an npm Account**

Before publishing, you need an npm account.

#### **Step 1: Sign Up for npm**

1. Go to [https://www.npmjs.com/signup](https://www.npmjs.com/signup) and create an account.
    
2. Verify your email address.
    

#### **Step 2: Log in to npm from the Terminal**

Run the following command in your terminal:

```python
npm login
```

You will be prompted to enter:

* Your npm username
    
* Your password
    
* Your email (associated with your npm account)
    

If the login is successful, you’ll see a message:

```python
Logged in as your-username on https://registry.npmjs.org/
```

### **Configuring package.json for Publishing**

#### **Step 3: Ensure Your Package Name is Unique**

Every npm package needs a unique name. Run the following command to check if your desired name is available:

```python
npm search my-awesome-library
```

If the name is already taken, you’ll need to modify `package.json` and change the `"name"` field.

#### **Step 4: Add Metadata and Keywords**

Open `package.json` and ensure it includes useful metadata:

```json
{
  "name": "my-awesome-library",
  "version": "1.0.0",
  "description": "A simple npm package for formatting dates",
  "main": "index.js",
  "repository": {
    "type": "git",
    "url": "https://github.com/yourusername/my-awesome-library.git"
  },
  "keywords": ["date", "formatter", "utility", "npm package"],
  "author": "Your Name <your-email@example.com>",
  "license": "MIT"
}
```

🔹 **repository** – Useful if you plan to host the project on GitHub.  
🔹 **keywords** – Helps people discover your package on npm.  
🔹 **license** – Specifies how others can use your package (for example, MIT, GPL, and so on).

### **Publishing the Package**

#### **Step 5: Publish Your Package to npm**

Run the following command inside your project folder:

```python
npm publish
```

If successful, you’ll see output similar to:

```python
+ my-awesome-library@1.0.0
```

Your package is now available at:

📌 [**https://www.npmjs.com/package/my-awesome-library**](https://www.npmjs.com/package/my-awesome-library)

#### **Step 6: Making Changes and Updating the Package**

If you want to release a new version, update the `version` field in `package.json`. npm follows Semantic Versioning (SemVer):

* **Patch:** Bug fixes (1.0.0 → 1.0.1)
    
* **Minor:** New features, backward-compatible (1.0.0 → 1.1.0)
    
* **Major:** Breaking changes (1.0.0 → 2.0.0)
    

Instead of manually updating `package.json`, use:

```python
npm version patch   # 1.0.0 → 1.0.1
npm version minor   # 1.0.0 → 1.1.0
npm version major   # 1.0.0 → 2.0.0
```

Then, publish the new version:

```python
npm publish
```

If you accidentally publish a package and need to remove it:

```python
npm unpublish my-awesome-library --force
```

⚠️ **Note:** You can only unpublish packages **within 72 hours** of publishing.

🎯 **You’ve successfully published your own npm library!** Now, other developers can install it using:

```python
npm install my-awesome-library
```

By following Semantic Versioning, writing clear documentation, and maintaining your package, you contribute to the open-source ecosystem and make your code reusable.

## **How to Use Your npm Library in a React Project**

Now that we’ve published our npm package, let’s see how to install, import, and use it inside a React project created with **Vite**. This section will guide you through the process using both npm and Yarn.

### **Installing Your Package**

#### **Step 1: Create a New React Project with Vite (if needed)**

If you don’t have an existing React project, create one using Vite:

#### **Using npm**

```python
npm create vite@latest my-react-app --template react
cd my-react-app
npm install
```

#### **Using Yarn**

```python
yarn create vite@latest my-react-app --template react
cd my-react-app
yarn install
```

Once the installation is complete, you can start the development server:

```python
npm run dev
```

or

```python
yarn dev
```

#### **Step 2: Install Your npm Package**

Now, install the npm library we created earlier (`my-awesome-library`).

#### **Using npm**

```python
npm install my-awesome-library
```

#### **Using Yarn**

```python
yarn add my-awesome-library
```

### **Importing and Using the Library in a React Component**

Once installed, you can use the library inside a React component.

Open `src/App.jsx` and modify it as follows:

```javascript
import React from "react";
import { formatDate } from "my-awesome-library";

function App() {
  const today = new Date();
  return (
    <div>
      <h1>Formatted Date</h1>
      <p>{formatDate(today)}</p>
    </div>
  );
}

export default App;
```

Now, run your Vite React app:

```python
npm run dev
```

Or with Yarn:

```python
yarn dev
```

This will display a formatted date on the webpage, confirming that our library is working!

### **Handling Package Updates and Versioning**

To update your npm package in your project:

#### **Using npm**

```python
npm update my-awesome-library
```

#### **Using Yarn**

```python
yarn upgrade my-awesome-library
```

If you want to check outdated dependencies:

```python
npm outdated
```

or

```python
yarn outdated
```

### **Using a Local Version of Your Package in Development**

If you’re still making changes to your npm package and want to test it in your React project **before publishing**, you can use `npm link` or `yarn link`.

#### **Step 1: Link Your Package Locally**

Go to your package’s project folder:

```python
cd ~/path-to-my-awesome-library
npm link
```

or

```python
yarn link
```

#### **Step 2: Use It in Your React Project**

Navigate to your React app and link the package:

```python
cd ~/path-to-my-react-app
npm link my-awesome-library
```

or

```python
yarn link my-awesome-library
```

Now, when you import and use `my-awesome-library`, it will use the local version instead of the published one.

### **Publishing an Update to Your Package**

If you’ve made changes to your package and want to publish a new version:

1️⃣ **Update the version number** in `package.json` (use `npm version patch` for small updates).  
2️⃣ **Run** `npm publish` to upload the new version.  
3️⃣ **Run** `npm update my-awesome-library` in your React project to get the latest version.

### **Final Thoughts on Using npm Libraries in React (Vite Edition)**

By now, you should have a fully functional npm package and know how to install, use, and update it in a React project using Vite.

✔️ Vite is faster than Create React App and provides better performance for development.  
✔️ npm and Yarn make dependency management easy.  
✔️ `npm link` allows local testing before publishing.  
✔️ Keeping dependencies updated ensures stability.

This workflow is essential for developers looking to create, maintain, and distribute reusable React components or JavaScript utilities.

## **Best Practices for npm and Yarn Libraries**

Now that you've created, published, and used your own npm package, it's essential to follow best practices to ensure your package is reliable, maintainable, and easy to use. This section will cover key principles and techniques to make your npm library as professional as possible.

### **Write Meaningful Documentation**

A well-documented library helps other developers understand how to use it effectively.

#### **What to Include in Your Documentation**

📌 Installation instructions  
📌 Usage examples  
📌 API reference (functions, parameters, return values)  
📌 Versioning and update history  
📌 Contributions guide (if open-source)

For example, a simple [`README.md`](http://README.md) file for my-awesome-library:

````python
# my-awesome-library

A simple npm package for formatting dates.

## Installation

### Using npm
```sh
npm install my-awesome-library
````

#### Using Yarn

```python
yarn add my-awesome-library
```

#### Usage

```javascript
import { formatDate } from "my-awesome-library";

console.log(formatDate(new Date())); // Outputs: 2025-02-04
```

### **Follow Semantic Versioning (SemVer)**

Versioning helps maintain compatibility and informs users of changes. npm follows Semantic Versioning (SemVer):

MAJOR.MINOR.PATCH

| Change Type | Example | Meaning |
| --- | --- | --- |
| **Patch** | `1.0.0 → 1.0.1` | Bug fixes, no breaking changes |
| **Minor** | `1.0.0 → 1.1.0` | New features, no breaking changes |
| **Major** | `1.0.0 → 2.0.0` | Breaking changes |

💡 To bump versions automatically, use:

````javascript
```sh
npm version patch   # Small bug fix
npm version minor   # New feature added
npm version major   # Breaking changes
````

Then, publish the new version:

```javascript
npm publish
```

👉 Use proper versioning to prevent breaking projects that depend on your library.

### **Keep Dependencies Up to Date**

Regularly updating dependencies improves security, performance, and compatibility.

#### **Check for outdated dependencies:**

```javascript
npm outdated
```

or

```javascript
yarn outdated
```

#### **Update dependencies:**

```javascript
npm update
```

or

```javascript
yarn upgrade
```

### **Write Unit Tests for Your Library**

Testing ensures your package works correctly before publishing updates.

#### **Install a Testing Framework (Jest)**

```javascript
npm install --save-dev jest
```

#### **Create a Test File (**`index.test.js`)

```javascript
const { formatDate } = require("./index");

test("formats a date correctly", () => {
  expect(formatDate(new Date("2025-02-04"))).toBe("2025-02-04");
});

test("throws an error if input is not a date", () => {
  expect(() => formatDate("not a date")).toThrow("Invalid date");
});
```

#### **Run Tests**

```javascript
shCopyEditnpm test
```

👉 You can use CI/CD (for example, GitHub Actions) to run tests automatically on every push.

### **Using CI/CD for Automated Publishing**

#### **Automate Publishing with GitHub Actions**

Create a `.github/workflows/publish.yml` file:

```javascript
ymlCopyEditname: Publish to npm
on:
  push:
    branches:
      - main

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
          registry-url: "https://registry.npmjs.org/"
      - run: npm install
      - run: npm test
      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

1️⃣ **Create an npm token**:  
Run:

```javascript
shCopyEditnpm token create
```

Copy the token and add it to GitHub Secrets (`NPM_TOKEN`).

2️⃣ **Push code to GitHub** → Auto-publish on npm!

👉 Automating publishing prevents human errors and ensures quality control.

### **Ensure Cross-Platform Compatibility**

* Use **ES modules (**`import/export`) for modern compatibility.
    
* Include **CommonJS (**`require/module.exports`) support for older environments.
    
* Test with different **Node.js versions** using CI/CD.
    

Example `package.json` for dual compatibility:

```javascript
jsonCopyEdit"type": "module",
"main": "index.cjs",
"exports": {
  "import": "./index.mjs",
  "require": "./index.cjs"
}
```

👉 This ensures your package works everywhere (Node.js, React, Next.js, and so on).

## **Conclusion**

Congratulations! 🎉 You’ve successfully learned how to create, publish, and use your own npm package, while also understanding the benefits of both **npm** and **Yarn** for package management.

Throughout this guide, we covered:

✔️ What npm is and why it’s important  
✔️ How to use npm and Yarn to manage dependencies  
✔️ How to create a reusable npm package  
✔️ How to publish and update your package on npm  
✔️ How to integrate your package into a React project with Vite  
✔️ Best practices for writing, testing, and maintaining your library

By following these steps, you've taken an important step toward open-source development and modular programming, making your code reusable for both yourself and the developer community.
