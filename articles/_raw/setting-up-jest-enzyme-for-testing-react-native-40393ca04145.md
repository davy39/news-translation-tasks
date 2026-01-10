---
title: How to set up Jest and Enzyme to test React Native apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T07:55:33.000Z'
originalURL: https://freecodecamp.org/news/setting-up-jest-enzyme-for-testing-react-native-40393ca04145
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ro5rChbmw1G4Cf5i2GAZJg.jpeg
tags:
- name: Jest
  slug: jest
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: null
seo_desc: 'By Sam Ollason

  This short article shares my experiences setting up my testing environment to unit
  test React Native components with Jest and Enzyme.


  _Photo by [Unsplash](https://unsplash.com/photos/6wdRuK7bVTE?utm_source=unsplash&utm_medium=referral...'
---

By Sam Ollason

This short article shares my experiences setting up my testing environment to unit test React Native components with Jest and Enzyme.

![Image](https://cdn-media-1.freecodecamp.org/images/nks4F4Jhip65XWA3f1i0GDn6a2TvXE0qhwfh)
_Photo by [Unsplash](https://unsplash.com/photos/6wdRuK7bVTE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Neil Soni</a> on <a href="https://unsplash.com/search/photos/mobile-app?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Testing tools and environment

The first thing I learnt was the approach and infrastructure for writing unit tests for a React Native app are very similar to writing unit tests for a React app…perhaps unsurprisingly.

However, while the tooling and the use of the test suites are very similar, the **testing environment and infrastructure have to be set up in a slightly different way**. This is essentially because React apps are designed to work with the DOM inside a browser whereas mobile apps don’t target this data structure for rendering (they target actual ‘native’ modules that are on the mobile system instead).

#### Using Jest

[Jest](https://jestjs.io/) is a library used for testing JavaScript apps.

I wanted to use Jest for several reasons:

Firstly, it was created and is actively maintained by Facebook for their own React Native apps.

Secondly, it comes pre-packaged with the version of React Native I was working with (created using [react-native](https://github.com/facebook/react-native)).

Thirdly, **Jest is a ‘comprehensive’ testing framework** and contains the whole suite of testing tools I needed. For example, Jest comes with a library to check assertions, a test runner to actually run tests and tools to check code coverage. With other solutions, one has to choose and assemble individual components of a testing suite.

#### Using Jest + Enzyme

I wanted to combine Jest and Enzyme. There are lots of slightly confusing comments on the web that compare ‘Jest versus Enzyme’. This is a bit misleading. While Jest is a testing framework you can think of Enzyme as a library that makes it easier to select and query elements inside of an emulated DOM. So **it is often used alongside Jest** to make writing the logic of tests cleaner and easier to read.

Still confused? It’s similar to how jQuery introduced a concise and clear syntax for querying and selecting elements in the DOM, whereas the syntax using vanilla JavaScript was (at least back when jQuery was first introduced) not as clear and easy to use. And people don’t often compare ‘jQuery versus JavaScript’, unless they are comparing a particular way that the two approaches use to query and modify elements of the DOM.

_Note:_ you can use Jest without Enzyme (I believe Facebook does this) but Enzyme makes your tests a bit easier to create and read. From my perspective, combining Enzyme with Jest is about convenience.

### Setting up Jest + Enzyme

I had to jump through some hoops to successfully setup Jest and Enzyme in my React Native environment.

Jest now comes included with React Native apps created using the ‘react-native’ tool. So I could use Jest out of the box. Wonderful!

But I ran into some problems trying to combine Enzyme with React Native using their [documentation](https://airbnb.io/enzyme/docs/guides/react-native.html). I never quite got to the bottom of what was the underlying problem, but I kept getting ‘modules not found’ errors like this one [here](https://github.com/facebook/react-native/issues/23943).

#### A solution

In the end I used a solution that essentially abstracts away some of the setup into a pre-packaged environment using the [jest-enzyme](https://github.com/FormidableLabs/enzyme-matchers/tree/master/packages/jest-enzyme#readme) library and then made sure the jest ‘presets’ was set to ‘react-native’ in my package.json.

I followed the instructions to install these libraries:

```
npm install jest-environment-enzyme jest-enzyme enzyme-adapter-react-16 --save-dev
```

Errors when I tried to run my tests also directed me to explicitly install these myself too:

```
npm install --save-dev react-dom enzyme
```

Here is what I had to manually add to package.json:

```
// package.json before with react-native init

{
...
   "jest": {
       "presets": ["react-native"],
     }
...
}

// package.json after my manual changes:
{
...

"jest": {
       "presets": ["react-native"], // not clear in documentation!
       "setupTestFrameworkScriptFile": "jest-enzyme",
       "testEnvironment": "enzyme",
       "testEnvironmentOptions": {
           "enzymeAdapter": "react16"
       }  
   }
...
}
```

You can see the repo [here](https://github.com/SamOllason/jest-enzyme-config-for-react-native/blob/master/README.md).

Using the jest-enzyme library in this way worked easily for me and it also meant that I had a slightly cleaner setup. This is because the other approach (that I couldn’t get to work, following the Enzyme documentation) would have meant I also had to set up and maintain a separate ‘jest config’ script.

### Summary

Writing business logic inside of Jest+Enzyme tests for React Native seems to be exactly the same as writing tests for React using Jest+Enzyme. This means the examples and documentation online for React unit testing are easily transferrable, which is really useful. This is a great step towards the vision of web developers being able to easily transfer their skills to create cross-platform mobile apps.

However, for the ease-of-use in the ‘test writing’ phase, I paid the price when setting up the infrastructure and environment so that the various tools were compatible with my React Native ecosystem.

In addition, from coming across Github issues in this area, it seems like there are lots of small instabilities between React Native versions that makes it really hard to find out what is the underlying cause of an infrastructure problem like the ones I described above. But I suppose we can’t have flexibility in such a fast-moving space as this without some challenges.

[Here](https://github.com/SamOllason/jest-enzyme-config-for-react-native/blob/master/README.md) is the repo with my jest-enzyme setup with a few example tests.

I hope you found this interesting and useful! Please feel free to add any questions or comments below.

