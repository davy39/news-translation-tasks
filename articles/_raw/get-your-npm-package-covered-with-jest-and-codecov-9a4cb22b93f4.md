---
title: Get your NPM-package covered with Jest and Codecov ☂️
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T17:54:02.000Z'
originalURL: https://freecodecamp.org/news/get-your-npm-package-covered-with-jest-and-codecov-9a4cb22b93f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HVSEe7dPPG_hCmRD_ENoxw.jpeg
tags: []
seo_title: null
seo_desc: 'By Carl-Johan Kihl

  Introduction

  Let’s talk about code coverage, and how you can do coverage reports in Jest and
  Codecov.

  What is Code Coverage?

  If you’re familiar with testing. You know its main purpose:


  Tests gives the developers freedom to make ch...'
---

By Carl-Johan Kihl

### Introduction

Let’s talk about code coverage, and how you can do coverage reports in [Jest](https://jestjs.io/) and [Codecov](https://codecov.io/).

### What is Code Coverage?

If you’re familiar with testing. You know its main purpose:

> _Tests gives the developers freedom to make changes and refactor code with the confidence that everything should work fine as long as all the automated tests will pass._

However, if the unit tests don’t cover all scenarios, there’s still a chance your changes can break something. That’s why we have Code coverage: the measure of **how much** of the code-base is covered by automated tests.

**Without Code coverage analysis, your tests have lost their main purpose.**

This is important when your project grows and many developers are involved.

✅ We can maintain quality of our test when new code is added.   
✅ We get a deeper understanding of existing tests.  
✅ Give developers confidence to refactor code without worrying about breaking things.   
✅ We can catch untested flows **before** they cause trouble.

Ok, now that we know what code coverage is, let’s implement it! ?

### Prerequisites

To keep this article short and concise, I will start here: [Step by Step Building and Publishing and NPM Typescript Package](http://bit.ly/2zAC2nK).

What’s been done so far:

✅ Setup a basic [NPM-package](https://github.com/caki0915/my-awesome-greeter/tree/basic-package)  
✅ Add testing with [Jest](https://jestjs.io/)  
✅ Write a basic test

If you have your project already setup with Jest you’re good to go. ? If not, I recommend that you clone or fork the repository for this article to start off from a b[asic NPM-package foundation:](https://github.com/caki0915/my-awesome-greeter)

```
git clone git@github.com:caki0915/my-awesome-greeter.git && cd my-awesome-greeter &&git checkout basic-package && npm install
```

If you’re interested how to build NPM packages, I recommend [my previous article here](http://bit.ly/2zAC2nK).

Alright, now when everything is set up, let’s go!

### Create Coverage reports in Jest

Creating coverage reports in Jest is easy. Just add this line in your jest config file:

```
"collectCoverage":true
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jvqy8Brvr_VLF0GOOv-odA.png)
_This is how my jest config file (jestconfig.json) looks like_

**collectCoverage:** Should be set to true if you want jest to collect coverage information while running your tests. _(Tests will run a little bit slower so it’s false by default.)_

Make sure your script command `test` in your **package.json** file will run Jest with your config file.

```
“test”: “jest --config jestconfig.json”
```

Alright! Run `npm test` in your terminal, and voilà! You will have a new folder with code coverage files generated for you.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8eP9WhWo1VrmS_kUg7LssA.png)
_Run npm test in the terminal_

![Image](https://cdn-media-1.freecodecamp.org/images/1*x4dsZDfiBpu_C_NjXR3NBg.png)
_Code coverage data generated for you!_

Don’t forget to add the coverage folder to `.gitignore`. We don’t want build-files in our repository. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*k9TVX54mc_hPWfmoRQj9kg.png)

### Make something useful of your reports

Ok, that’s cool, we generated a folder with some files, but what should we do with this information? ?

First of all, you can manually review the coverage-report on a generated HTML-page. Open `/coverage/lcov-report/index.html` in your browser:

![Image](https://cdn-media-1.freecodecamp.org/images/1*3siDGI3_o1etjgGgL93vEQ.png)
_coverage/lcov-report/index.html_

Ok, that’s nice, but do we REALLY need to manually review the reports on every build??

No, you shouldn’t. You should publish the reports online to make something useful of them. In this article, we’re going to use a coverage reporting tool called [codecov.io](http://codecov.io).

**Codecov** is free for open-source projects. It takes code coverage reports to the next level. With Codecov, we can also auto-generate badges and run it on continuous integration builds. _(More on it later.)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*LDkR3IU8CgySEN9eRUlxRg.png)
_A coverage badge with a link to a coverage report on **codecov.io in** a ****package README.md_

Sign up at [https://codecov.io/](https://codecov.io/) and follow the guide to connect to Github and your repository. After that, you should end up seeing a screen like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5LmuJfwbiEFLzM5Iv5wZgQ.png)

Nice! For now, this page will be empty since you haven’t uploaded any reports yet, so let’s fix that. In the terminal, run:

```
npm install --save-dev codecov
```

Normally you want to upload reports at the end of a continuous integration build, but for this article, we will upload the reports from our local machine. In the terminal run:   
_(Replace <Your token> with your repository-token found in codec_ov.io)

```
./node_modules/.bin/codecov --token="<Your token>"
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*npeviaPBYnSHbbiZ0-iCzQ.png)

Success! Now you can view your report online in codecov.io.? ?

```
https://codecov.io/gh/<Github Username>/<Repository Name>/
```

### Add a Badge to your README.md

Badges are important, especially for NPM packages. It gives the first impression of high quality when you see a beautiful code coverage badge in [npmjs](https://www.npmjs.com/) and [Github](https://github.com/).

In your **README.md** add the following line:  
_(Replace <Github Username>, <Repository Name> and <Branch Name> with_ your information)

```
[![Codecov Coverage](https://img.shields.io/codecov/c/github/<Github Username>/<Repository Name>/&lt;Branch Name>.svg?style=flat-square)](https://codecov.io/gh/<Github Username>/<Repository Name>/)
```

In my case, it will look like this:

```
[![Codecov Coverage](https://img.shields.io/codecov/c/github/caki0915/my-awesome-greeter/coverage.svg?style=flat-square)](https://codecov.io/gh/caki0915/my-awesome-greeter/)
```

Awesome! Now you can show the rest of the world that you are using unit-testing and code coverage reports! ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*pgmvJpcddTB5QGExR3kfag.png)
_A coverage badge with a link to your coverage analysis report._

### Summary

If you’re using tests, code coverage reporting is a must and it should run every-time you make a pull-request or make changes on your branches.

You can find my [NPM-starter package here on Github.](https://github.com/caki0915/my-awesome-greeter)  
It’s an educational base for best practices NPM-package development. Comments, Forks and PR’s are welcome. ?

### What’s next?

If you don’t use continuous integration (CI) yet, it’s time to set it up.   
In my next article, I’m going to cover continuous integration with code-coverage for NPM packages.

If you find this article useful, please give it some claps and follow me for more articles about development.

#### Good luck building your awesome package! ? ?

