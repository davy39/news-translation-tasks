---
title: How to Add TypeScript to a JavaScript Project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-27T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-typescript-to-a-javascript-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/1_9XMpTyccrky0eW5Wz6DoWQ.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: "By dor sever\nI love writing code. And I want to be really good at it.\
  \ But somehow, writing JavaScript has never been my strong suit. \nNo matter how\
  \ much I practiced, the same mistakes kept appearing in production: cannot read\
  \ property <> of undefined..."
---

By dor sever

I love writing code. And I want to be really good at it. But somehow, writing JavaScript has never been my strong suit. 

No matter how much I practiced, the same mistakes kept appearing in production: `cannot read property <> of undefined` exceptions, the famous `[Object object]` string, and even function calls with an invalid number of parameters.  


What's more, most of the codebases I was working on were really large JavaScript ones. So here is a nice diagram of how it felt to be me:

![Image](https://www.freecodecamp.org/news/content/images/2020/07/typescript-vs-javascript--1-.png)
_We can do much better!_

In this post, I’ll avoid explaining why TypeScript is awesome (and it is), and focus on the tasks you need to complete if you want to migrate your vanilla JavaScript project to a mixed TypeScript project.

By the end of the post, you will be a happier person and will be able to answer the following questions:

* How can I add types to my JavaScript project?
* What is TypeScript?
* How can I use TypeScript in a JavaScript project?
* What are the steps to convert a JavaScript application to support TypeScript?
* How can I take care of build & packaging?
* How can I take care of linting?
* How can I “sell” TypeScript to my organization and developers?

## How can I add types to my JavaScript project?

Vanilla JavaScript does not support types at the moment, so we need some sort of abstraction on top of JavaScript in order to do so. 

Some common abstractions are using Facebook’s static type-checker called `[flow](https://github.com/facebook/flow)` and Microsoft's language called :`[typescript](https://github.com/microsoft/TypeScript)` .

This blog post will examine the usage and addition of TypeScript to your JavaScript project.

## What is Typescript?

TypeScript is a typed superset of JavaScript that compiles to plain JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/superset.png)
_If you know javascript, you are more than half way there._

TypeScript consists of a few parts. The first is the TypeScript language — this is a new language which contains all JavaScript features . Check out the [specs](https://github.com/Microsoft/TypeScript/blob/master/doc/spec.md) for more information.

The second is the TypeScript compiler, `tsc` (the type system engine) which is a compilation engine that builds ts files and yields js files.

## Hello world in TypeScript

As an example, these are the steps you need to take to write your first TypeScript application:

1. install TypeScript with `npm i typescript`
2. create a folder called `example` and cd into it (in your terminal)
3. create a file called `hello.world.ts`
4. write the following code in it:

```typescript
const firstWords:string = "hello world"
console.info(firstWords);

```

and then save it.

5.  run the `tsc` command to run the TypeScript compiler on the current folder

6.  notice that you got a `hello.js` file that you can now run :) 

7.  run `node ./hello.js`

## How can I use TypeScript in a JavaScript project?

There are couple of strategies for doing this "migration" (company-wise and code-wise). I've listed them below by their "cost" and by how much value they provide. 

I would suggest starting with "application TS support" and moving forward after you have proved the value to your development team.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/typescript-migration-steps.png)
_The typescript migration process, iterate through the process only if you prove value._

### The "small step for man" approach - Adding TS support for existing applications

![Image](https://www.freecodecamp.org/news/content/images/2020/07/small-step.jpeg)
_One small step for a developer. types are wonderful :)_

My first suggestion is to create a mixture of the two languages in a single project, and then write all “future” code in TypeScript.

The combination of two languages in a single project sounds pretty awful at first, but it works quite well since TS was built for gradual usage. At first it can be used just as JS with .ts files and weird import lines.

In this strategy, we will be compiling the migrated TypeScript files and just copying the JavaScript files to an output folder.

The huge benefit of this approach is that it allows a gradual learning curve for the development team (and for you) with language and it’s features. It also gives you hands-on experience and insight into its pros and cons.

I highly recommend starting from this step and then iterating on it with your team before moving forward. For a quick “how to do this”, scroll down to `The steps to convert a javascript application to support typescript` part.

### The open for business approach - Adding TS support for existing libraries.

After you have some hands on experience with TS and your development team agrees it's worth moving forward, I suggest converting your in-house libraries and modules to support TS. 

This can be done in two ways:

**The first way** involves using [declaration files](https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html). A simple addition of `d.ts` files helps the TS compiler type-check existing JavaScript code and gives you auto-completion support in your IDE. 

This is the "cheapest" option, as it doesn't require any code changes to the library at all. It also gives you maximum power and types support in your future code.

**The second way** is to perform a full re-write of TypeScript, which might be time-consuming and error-prone. I would advise against it, unless it proves ROI worthy to your team.

### The skeleton - a step towards the future

![Image](https://www.freecodecamp.org/news/content/images/2020/07/future.jpeg)
_Typescript skeleton is the way to ensure a bright future!_

I assume most developers are "lazy" and usually start their application by copying from a skeleton (which usually contains logging, metrics, configuration, and so on).

This step helps you navigate your way into a bright future, by creating an "official" skeleton for your company. It will be 100% TS, and deprecates the old JS skeleton if one exists.

This [typescript-node-starter](https://github.com/microsoft/TypeScript-Node-Starter#getting-started) is a really good first project to start with.

### **The all in approach - Converting a full codebase from JS into TS**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/allin.jpeg)
_I'm all in! Let's make all things typed!_

This option requires a total rewrite from JavaScript code to TypeScript.   
  
I would recommend doing this as a final step in the TS migration process since it requires a total application re-write and deep knowledge of TypeScript and it's features.

You can do such a rewrite (it's a long process) in the following manner:

1. Define clear types for your application business logic, API, & HTTP's
2. Use `@types` packages for all the libraries in your `package.json`. Most of the libraries out there support TS, and in this process I suggest migrating them one by one (by just adding `@types/<package_name>` in your `package.json` file).
3. Convert your application logical components in order of their importance. The more unique the business logic, the better.
4. Convert the IO parts of your application, database layers, queues and so on.
5. Convert your tests.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/champagne.jpeg)
_Types are a cause for a celebration :)_

Keep in mind that there are automated tools designed to ease this process, for example [ts-migrate](https://github.com/airbnb/ts-migrate) from the Airbnb team. 

It tackles this problem from a different perspective, and converts all files to TypeScript. It also allows gradual improvements (like mentioned in the steps above) while the entire codebase is TypeScript from day one.

## How to convert a JavaScript application to support TypeScript.

### Install typescript 

by running : `npm install typescript`.

### Typescript config file

Add a typescript config file, which can be created using the `tsc --init` command in you CLI.

Here is an example of how our initial config looked:

```json
{
 "compilerOptions": {
   "target": "esnext",
   "module": "commonjs",
   "allowJs": true,
   "checkJs": false,
   "outDir": "dist",
   "rootDir": ".",
   "strict": false,
   "esModuleInterop": true /* Enables emit interoperability between CommonJS and ES Modules via creation of namespace objects for all imports. Implies 'allowSyntheticDefaultImports'. */,
   "forceConsistentCasingInFileNames": true, /* Disallow inconsistently-cased references to the same file. */
   "declaration": true, /* Generates corresponding '.d.ts' file. */
   "strictNullChecks": true,
   "resolveJsonModule": true,
   "sourceMap": true,
   "baseUrl": ".",
   "paths": {
    "*": [
      "*",
      "src/*",
      "src/setup/*",
      "src/logic/*",
      "src/models/*",
      "config/*"
    ]
  },
 },
  "exclude": ["node_modules", "dist"],
  "include": [
    "./src",
    "./test",
    "./*",
    "./config" 
  ]
}
```

A few things to notice above:

* We read all the files in the `src` or `test` or `config` directory (using the `include` flag).
* We accept JavaScript files as inputs (using the `allowJs` flag).
* We emit all of the output files in `build` (using the `outDirflag`).

### Create your first .TS file in your project 

I recommend starting by adding a simple TypeScript file (or changing a really simple JS file to a TS one) and deploying. Take this migration one step at a time.

### Take care of your package.json file

Here is how our `package.json` looks before and after:

```json
{
  "scripts": {
    "start": "node ./application.js",
    "mocha": "mocha --recursive --reporter spec -r test/bootstrap.js",
    "test": "npm run mocha -- test/ -r test/integration/bootstrap.js", 
  }
}
```

```json
{
  "scripts": {
    "start": "node ./dist/application.js",
    "build-dist": "./node_modules/typescript/bin/tsc",
    "mocha": "mocha --recursive --reporter spec -r ./dist/test/bootstrap.js",
    "test": "npm run mocha -- ./dist/test/ -r ./dist/test/integration/bootstrap.js"
  }
}
```

As you can see, most of the changes were about adding the prefix `dist` to most of our build commands. We also added a `build-dist` script that compiles our codebase and moves all files to a dedicated folder called `dist`.

### Add source-map-support

One of the big issues when adding TypeScript to your project is that you are adding a layer of indirection between the code you write and the code that actually runs in production (since `.ts` is transpiled  to `.js`  in run time).

For example, imagine the following TypeScript program:

```typescript
const errorMessage: string = "this is bad"

throw new Error(a)
```

When we run it, it will throw the following stack-trace:

```typescript
Error: this is bad
    at Object.<anonymous> (/Users/dorsev/work/git/example/hello.js:3:7)
```

This is problematic since our code-base contains only `.ts` files. And since most production code contains hundreds of lines, it will be really time-consuming translating these numbers and files properly. 

Luckily for us, there is a solution for this called [source-map-support](https://www.npmjs.com/package/source-map-support)!

This allows us to ensure that stack-traces will have proper `.ts` file names and line numbers like we are used to :) 

This can be done by running `npm install source-map-support` and then adding the following line in the first lines of your application:

`require('source-map-support').install();`

The code now looks like this:

```typescript
require('source-map-support').install();
const a:string = "this is bad"
throw new Error(a)
```

And when we compile it we run `tsc --sourcemap hello.ts`. Now we get the following stack-trace which is awesome :) 

```victory
Error: this is bad
    at Object.<anonymous> (/Users/dorsev/work/git/example/hello.ts:3:7)
```

In recent versions of `nodejs`, this is supported natively by using the `--enable-source-maps` [flag](https://github.com/nodejs/node/pull/29564).

## How to take care of your build (Travis) & packaging

Let's just examine the before and after changes on our build configuration file.

This is how our `.travis` file looked before (simplified edition):

```yaml
jobs:
  include:
  - &build-and-publish
    before_script:
    - npm install --no-optional --production
    - npm prune --production
    before_deploy:
     - XZ_OPT=-0 tar --exclude=.git --exclude=reports.xml --exclude=${ARTIFACTS_MAIN_DIR}
       --exclude=.travis.yml --exclude=test -cJf "${ARTIFACTS_PATH}/${REPO_NAME}".tar.xz * .??*
  
  - &test
    before_script:
     - npm install --no-optional
    script:
     - echo "Running tests"
     - npm run lint && npm test
```

And this is how it looked after:

```yaml
jobs:
  include:
  - &build-and-publish
    before_script:
    - npm install --no-optional --production
    - npm run build-dist  # Build dist folder
    - npm prune --production
    before_deploy:
     - cp -rf config/env-templates ./dist/config/
     - cp -rf node_modules ./dist/
     - cd dist
     - XZ_OPT=-0 tar --exclude=.git --exclude=reports.xml --exclude=${ARTIFACTS_MAIN_DIR} --exclude=.travis.yml --exclude=test -cJf "${REPO_NAME}.tar.xz" *
     - mv ${REPO_NAME}.tar.xz "../${ARTIFACTS_PATH}"
     - cd ..

  - &test
    before_script:
     - npm install --no-optional
     - npm run build-dist
    script:
     - echo "Running tests"
     - npm run lint && npm test
```

Notice most changes concern "packaging" to the `tar.xz` file and running the `build-dist` command before accessing the `dist` folder.

## How can I take care of linting?

There are a couple of linting solutions available.

The first solution we used was [tsfmt](https://github.com/vvakame/typescript-formatter)  –  but then we decided against it later on because it requires you to maintain two separate configurations for your project (one for TypeScript using `tsfmt` and a separate one for JavaScript using `eslint`). The project also looks deprecated.

We then found [TSLint](https://palantir.github.io/tslint/)  which redirected us to the [eslint plugin for TypeScript](https://github.com/typescript-eslint/typescript-eslint). We then configured it as follows:

This was our `eslintrc.js`:

```javascript
module.exports = {
    rules: {
        indent: [2, 2, {
            SwitchCase: 1
        }],
        'no-multi-spaces': 2,
        'no-trailing-spaces': 2,
        'space-before-blocks': 2,
    },
    overrides: [{
        files: ['**/*.ts'],
        parser: '@typescript-eslint/parser',
        plugins: ['@typescript-eslint'],
        extends: ['plugin:@typescript-eslint/eslint-recommended', 'plugin:@typescript-eslint/recommended']
    }]
}
```

Which we configured to run using a `lint-fix` command in our `package.json` which looks as follows:

```json
{
    "scripts": {
        "lint-fix": "node_modules/.bin/eslint . --fix"
    },
    "pre-commit": ["lint-fix"]
}
```

## How to "sell" typescript to your development team 

I believe one of the most critical aspects of introducing TypeScript to your organization is the "pitch" and how you present it to your development team.

Here is the [presentation](https://github.com/dorsev/typescript-talk/blob/master/typescript_meetup.md  ) we presented internally which revolved around the following topics:

1. Explain why we think TypeScript is awesome
2. What is TypeScript
3. Some basic code examples. The main point in this part is not to "teach" 100% TypeScript, since people will do that on their own. Instead, give people the feeling  that they can read and write TypeScript, and that the learning curve is not so hard.
4. Advanced code examples, like Union types and Algebraic data-types which provide enormous values to a JS developer. This are a real treats, on top of typed-language and the compiler that will attract your developers to it. 
5. How to start using it. Encourage people to download the `vs-code` IDE and to add an annotation ([//@ts-check](https://code.visualstudio.com/docs/nodejs/working-with-javascript#_type-checking-javascript)) so they can start seeing the magic!  In our company, we prepared in advances some really cool mistakes that `ts-check` catches, and we did a live demo (2-3 minutes) to show how fast the TypeScript compiler can help them  using JS docs with type annotations or `ts-check`).
6. Deep dive into some features. Explain `ts.d` files and `@types packages` which are some of the things you will encounter really early in your TypeScript codebases.
7. Live PR's from your work. We showed the PR we created early on, and encouraged people to review it and try it out for themselves. 
8. Share some cool resources. There is a lot of content online, and it's hard to figure out good from bad. Do your teammates a solid and dig deeper and try to find quality content about the tools you use and need. Scroll down to the conclusion for my resources.
9. Create a public pull request .  I recommend trying to get as much support as possible for its approval.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-5780-10-20-at-10.09.59-AM.png)
_Adding typescript to a project! hurray!_

10.  Create a positive buzz in your organization about the change!

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-5780-10-20-at-10.13.33-AM.png)

I highly recommend tweaking this list according to your team, standards, and time-constraints.

## Conclusion

**Typescript is super awesome**! If you are writing production grade software and the business requirements and availability are high, I strongly encourage you to give typescript a try. 

**Just remember to take it one step at a time.** New languages and frameworks are hard, so take the time to learn and to educate yourself and your team before pushing this process forward. 

**Create a short feedback loop and value proposition**. It's hard to "sell" a new language to your team and management as it takes time and resources. 

So design your migration process with short feedback loops, and try to define clear KPI's (fewer bugs in production, easier refactoring times, and so on) and make sure the value proposition for your use-case is constantly justified until it becomes the de-facto standard.   

**Make learning resources readily available**. I really enjoyed [this](https://youtu.be/vxvQPHFJDRo) talk about TypeScript first steps and this [blog post](https://dylanvann.com/incrementally-migrating-to-typescript/) about incremental migration to TypeScript. 

Also, don't miss out on the `[deno](https://github.com/denoland/deno)` project and the `[ts-node](https://github.com/TypeStrong/ts-node)` project. I'm super excited and looking forward to using them soon.

