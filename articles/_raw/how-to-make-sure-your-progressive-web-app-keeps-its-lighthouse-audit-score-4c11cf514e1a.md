---
title: How to make sure your Progressive Web App keeps its Lighthouse audit score
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T21:01:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-sure-your-progressive-web-app-keeps-its-lighthouse-audit-score-4c11cf514e1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S5Da5dbVbwPIkDi6nS9uxg.png
tags:
- name: audit
  slug: audit
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ondrej Chrastina

  I bet most of you have implemented a web application before. Some of you may even
  have created a Progressive Web App (PWA) that can act as a native app installed
  in a device. You’ve maybe followed my tips to make your app fully co...'
---

By Ondrej Chrastina

I bet most of you have implemented a web application before. Some of you may even have created a [Progressive Web App](http://bit.ly/create-pwa-with-angular-from-lighthouse) (PWA) that can act as a native app installed in a device. You’ve maybe followed [my tips](http://bit.ly/tune-pwa-score-from-lighthouse-ci) to make your app fully compliant with prescribed PWA rules and conventions via the Lighthouse audit tool.

Now, wouldn’t it be nice to run the audit every time some of your colleagues updates the code-base? Accidents happen, and even if you and your colleagues strive for a 100% compliant PWA, it is always great to get early warnings, immediately after each build.

In the following article, I’ll describe how to check the compliance automatically by embedding the [Lighthouse](https://github.com/GoogleChrome/lighthouse) PWA audit into your continuous integration pipeline.

I’ll start exactly where I left off in [my previous article](http://bit.ly/tune-pwa-score-from-lighthouse-ci) (that is, working with the sample travel application that lists interesting places to visit). The app stores its data in the [Kentico Cloud headless CMS](http://bit.ly/kc-home-lighthouse) and it meets all the [PWA requirements](https://developers.google.com/web/progressive-web-apps/checklist). Following each implementation step, I will provide a GitHub link to the code state to allow you to try the changes step by step, without the need to write the code on your own.

![Image](https://cdn-media-1.freecodecamp.org/images/ChXsB7q9dIfEsqL0lsbUZndv6QTX7ylGCvC5)
_[Initial state](https://github.com/Kentico/cloud-sample-angular-pwa-app/tree/8521c612e273fc91670a408488dc981ad7023895" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/KflsZQz0gDj0VvhSaG-WANi-Ywt7mldUigo1)
_Sample Application_

I will use the [Lighthouse npm package](https://www.npmjs.com/package/lighthouse). Although Lighthouse could be used directly from the command line, its programmatic form is better as it properly reports success, failure, and the audit score.

I’ll do basically two things. First, I’ll show how to use the package the from command line to emit a JSON string with the audit results into my console window. Then I will show how to use the npm package in a continuous integration pipeline.

### How to use the Lighthouse package from the command line

Let’s start by installing Lighthouse as a development dependency to the project.

```
npm install --save-dev lighthouse
```

For deployment, I am using [Surge](https://surge.sh/) service. You just have to register on its site and install the CLI tools (in the following example globally). Then, you’re able to deploy the folder into a *.surge.sh sub-domain.

```
npm install -g surge
```

* `surge /dist your-own-subdomain.surge.sh` for example deploy the “dist” folder to the specified URL. This requires you to either log in or [set the surge environment variables](https://docs.travis-ci.com/user/deployment/surge#Environment-variables) with the login and token.

In your `package.json` file, define a public URL where your app will be deployed, like so:

```
{..."config": {   "deployUrl": "https://your-own-subdomain.surge.sh"},...}
```

Lighthouse will be configured to perform the audit against this URL. But, in order to do that, it needs to wait a few seconds before the app (or a new version of it) becomes publicly accessible.

Surge sometimes takes its time when publishing your app. Therefore, you should use the [npm-delay](https://www.npmjs.com/package/npm-delay) package (or something similar) to wait for two seconds before performing the audit. Let’s get through it. Install the package to the development dependencies.

```
npm install --save-dev npm-delay
```

Once you’re done with installing, define the script command for deployment using Surge to your URL. Then, define the “lighthouse” script command that will build the app in production mode into the `dist` folder, use the “deploy” command, wait for two seconds (to make sure that last version of app is publicly accessible), and then run the PWA audit against the application’s URL.

```
{..."scripts": {    ...    "deploy": "surge dist %npm_package_config_deployUrl%",    "lighthouse": "npm run build && npm run deploy && npm-delay 2000 && lighthouse --chrome-flags=\"--headless\" --quiet --output=json %npm_package_config_deployUrl%",    ...  }...}
```

**Alright, let’s run the command:**

```
npm run lighthouse
```

In the console, you’ll see a huge JSON string with the audit result. What you want to inspect is the `reportingCategories` property, its inner part (report) named “Progressive Web App” with its property called `score`.

```
{  ...  "reportCategories": [    ....    {      "name": "Progressive Web App",      ...      "id": "pwa",      "score": 100    }  ...  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/Nm21thuCToMlkcU0XKWVq7S910-BZhMQNvfU)
_[Lighthouse check](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/16da5916da8c14cbe090ce38cef73a93c0d90b31" rel="noopener" target="_blank" title=")_

### Add the Lighthouse check to the Continuous Integration pipeline

To plug the PWA audit into the CI pipeline, we can use the [programmatic approach](https://github.com/GoogleChrome/lighthouse/blob/master/docs/readme.md#using-programmatically) of using Lighthouse. First of all, you’ll want to define the JavaScript script that will check the score of you PWA.

The script uses the URL defined in the `package.json` file. In that script, there is a function used to run the [Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome) and perform the Lighthouse audit on it. After the audit is finished, the script will wait for two seconds to be sure that your application is deployed and accessible. Finally, the script selects the value from the audit result JSON string and checks whether it meets the defined score level — 100 in this case. Otherwise it returns the exit code 1, which will in turn cause the [Travis CI](http://travis-ci.org) build to fail.

```
const lighthouse = require('lighthouse');const chromeLauncher = require('chrome-launcher');const appConfig = require('./package');
```

```
const opts = {    chromeFlags: ['--headless']};
```

```
function launchChromeAndRunLighthouse(url, opts, config = null) {    return chromeLauncher.launch({ chromeFlags: opts.chromeFlags }).then(chrome => {        opts.port = chrome.port;        return lighthouse(url, opts, config).then(results => {            delete results.artifacts;            return chrome.kill().then(() => results);        });    });}
```

```
launchChromeAndRunLighthouse(appConfig.config.deployUrl, opts).then(results => {    setTimeout(() => {      if (results.reportCategories.filter((item) => item.id === "pwa").length) {        const score = results.reportCategories.filter((item) => item.id === "pwa")[0].score        if (score >= 100) {            console.info(`PWA score is 100.`);            process.exit(0);        }        console.error(`Score is lower than 100. It is ${score}`);        process.exit(1);    }    console.error(`No PWA score provided by lighthouse.`);    process.exit(1);    }, 2000);    });
```

Let’s define the new script in the `package.json` file.

```
{...    "scripts": {    ...    "check-pwa-score": "node checkLighthouse.js"    ...    }...}
```

Finally trigger Travis build and **publish out a 100% compliant PWA**!

I am using a yaml file for Travis configuration. Basically, you just sign in to [this service](https://travis-ci.org/) by your GitHub account, turn on the CI to repository in the Travis UI, and then you just commit the file `.travis.yml` to the root of your repository.

```
sudo: requireddist: trustylanguage: node_jsnode_js:- "stable"before_script:- npm installbefore_deploy:- npm run builddeploy:  provider: surge  project: ./dist/  domain: https://kentico-cloud-sample-angular-pwa-app.surge.sh   skip_cleanup: trueafter_deploy:- npm run check-pwa-score
```

As you can see at the bottom, there is an after-deploy action that checks the PWA audit score.

![Image](https://cdn-media-1.freecodecamp.org/images/OBVHa6yT8a1O7xzmQOllT9wfW2c9xTUWI8VU)
_[Add PWA audit to the CI pipeline](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/5e5a6999cb499345808ea5833f40a293c0b4632c" rel="noopener" target="_blank" title=")_

**Voila! Your build pipeline now automatically checks the PWA audit score.**

![Image](https://cdn-media-1.freecodecamp.org/images/RfocjMvvihEm9D-0xbCLr7uURJVZ1aGknXNT)

From now on, should any of your colleagues hurt the compliance of your PWA app, they will immediately be warned by Travis.

### Final words

Good job! If you’ve followed the steps, you’ve successfully added the Lighthouse npm package to get the JSON string with the results to the console.

You’ve also set things up to automatically publish your app, wait two seconds, and use the Lighthouse functionality in the Headless Chrome to check for your score in a Travis CI pipeline.

Now, you no longer have to lose sleep over your precious app!

