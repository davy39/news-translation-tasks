---
title: How I automate all of the boring parts of my job with Create React App DevOps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-07T03:16:18.000Z'
originalURL: https://freecodecamp.org/news/lets-write-create-react-app-devops-together-dc19512c6fbb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LjmVlUg4vIy-MA6BCwkLPw.jpeg
tags:
- name: Devops
  slug: devops
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By James Y Rauhut

  When you have responsibilities as one of the only designers — and possibly developer
  s— on your team, automation becomes your best friend.

  At work, I have both responsibilities as a designer and sometimes as a lone developer.
  This m...'
---

By James Y Rauhut

When you have responsibilities as one of the only designers — and possibly developer s— on your team, automation becomes your best friend.

At work, I have both responsibilities as a designer and sometimes as a lone developer. This means that there is not much time to configure the dev environment I am working on. Time is also wasted when I have to manually update the apps to their online environment.

Thankfully, there are free tools that help us prototype and release in no time: Create React App, Bluemix, GitHub, and Travis CI. I’m going to share with you how I use all of these to automate all of the boring parts of my job with [Create React App DevOps](https://github.com/seejamescode/create-react-app-devops).

> Update March 3rd, 2017: Thanks to a heads up from a commenter, I was warned not to use Babel-Node in production (on Bluemix). [Create React App DevOps](https://github.com/seejamescode/create-react-app-devops) now reflects that with v1.1.0!

There are three ways you can adapt this process yourself:

* Follow along with this post as we write the project together
* Inspect the comparison between the initial Create React App use and the final commit: [Github Comparison Between First and Last Commit](https://github.com/seejamescode/create-react-app-devops/compare/0dbaf64a02f0eeedba2e5a134d472a58b3fc55a5...master)
* Fork the repo and follow the instructions below: [Fork Create React App DevOps](https://github.com/seejamescode/create-react-app-devops#fork-destination-box)

Check out the app live at: https[://create-react-app-devops.mybluemix.net/](http://create-react-app-devops.mybluemix.net/)

If you want to know the guts of the project, then continue reading to make it with me! There will be six sections:

1. Use Create React App to Get the UI Up
2. Setup Your Server with Node, Express, and Babel
3. Run the App on the Web with Bluemix
4. Automagically Deploy from Github with Travis CI
5. Fetch API Data While Keeping Keys Secure
6. Create a Staging App for Experimentation

### [Use Create React App to Get the UI Up](https://github.com/seejamescode/create-react-app-devops/commit/0dbaf64a02f0eeedba2e5a134d472a58b3fc55a5)

When I first started using React for front-end projects, I wasted a lot of time. A lot of that time was configuring Webpack and various plug-ins. Thankfully, Create React App was created to keep your projects configured properly. There is an option to “eject” your Create React App projects, but I avoid ejecting. That is so that I can continue receiving Facebook’s updates to the project.

1. [Install Node](https://docs.npmjs.com/getting-started/installing-node) to manage the packages we use and server.
2. [Install Yarn](https://yarnpkg.com/lang/en/docs/install/#mac-tab) (optional) to speed up the installation of packages. If you choose not to, just keep in mind that terminal commands like `yarn run ---` are usually `npm run ---`.
3. It is time to open up your terminal. Install Create React App globally: `yarn global add create-react-app`
4. Now let Create React App make your project or you and navigate into it: `create-react-app <app-na`me>`; and cd <`app-name>

**Side Note**: Anytime you see “<app-name>” in this write-up, you can replace it with a unique name for your project like “super-cool-app”.

#### ?????

You can now work on all of the client-side (user interface) code! Run `yarn start` and Create React App will open a tab in your browser to show you the UI. Anytime you edit the client-side code in the `<app-name>`;/src/, the browser will refresh with the changes!  
?????

### [Setup Your Server with Node, Express, and Babel](https://github.com/seejamescode/create-react-app-devops/commit/aafd7e34b43906814b7bb49e0a3d33e211e81281)

Now let’s get a server running so that you can host the app online. Controlling your own Node server will also be important later to fetch data with an API from services like Github.

1. Let’s add all of the packages for a Node server. The Babel related packages will allow you to use the latest Javascript functionality: `yarn add babel-cli babel-preset-es2015 babel-preset-stage-2 compression express`
2. Now make an `index.js` file in the root of the project folder to represent our Node server:

```
import compression from 'compression';import express from 'express'; const app = express();const port = process.env.PORT || 8080;app.use(compression()); app.use(express.static('./build')); app.listen(port, (err) => { if (err) {   console.log(err);   return; }
```

```
 console.log(`Server is live at http://localhost:${port}`);});
```

3. You can now see all of the dependencies we installed in `package.json`. Let’s add a script called “bluemix” to run the server and section called “babel” to configure Babel:

```
"scripts": {  "bluemix": "babel-node index.js",  "start": "react-scripts start",  "build": "react-scripts build",  "test": "react-scripts test --env=jsdom",  "eject": "react-scripts eject",},"babel": {  "presets": [    "es2015",    "stage-2"  ]}
```

4. `yarn build && yarn bluemix` will build the app and run the server. However, we want to add a dev mode to the server similar to our client-side code. This way we see changes from just saving `index.js` when we are coding. Let’s add some dependencies that will let us do this: `yarn add babel-watch concurrently --dev`

5. Now update the “start” script in package.json so that we run Create React App’s dev mode and our server. We will also add a “proxy” line. This line tells Create React App that a server can take requests that are not found in the client-side code:

```
"proxy": "http://localhost:8081","scripts": {  "bluemix": "babel-node index.js",  "start": "concurrently \"PORT=8080 react-scripts start\" \"PORT=8081 babel-watch index.js\"",  "build": "react-scripts build",  "test": "react-scripts test --env=jsdom",  "eject": "react-scripts eject",},
```

#### ?????

You can now work on the server-side code in `index.js`! Run `yarn start` and both the Create React App dev mode and our server will respond to changes saved!  
?????

### [Run the App on the Web with Bluemix](https://github.com/seejamescode/create-react-app-devops/commit/3d61ec57acdbd0988c4aadf402415d290cf9c064)

Since I work at IBM, Bluemix is our go-to hosting platform. Not only do we host our final products on Bluemix, but we also host any prototypes to share with peers and user test. I also use Bluemix for personal projects like this one because it has a solid free tier.

1. Create a free account on [Bluemix](https://www.bluemix.net).
2. Install the [Cloud Foundry CLI](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html). Since Bluemix is built on top of an open-source project called Cloud Foundry, you will see “cf” in a lot of our commands.
3. Similar to `.gitignore` files, we should make a file to prevent unnecessary files from being uploaded to Bluemix. Make `.cfignore` in the project’s root folder to do this:

```
/node_modules .DS_Store npm-debug.log* yarn-debug.log* yarn-error.log*
```

4. Now we can tell Bluemix all of our app’s settings for the deploy with a `manifest.yml` file in the root of the project:

```
---applications:- name: <app-name>  buildpack: https://github.com/cloudfoundry/nodejs-buildpack  command: npm run bluemix  disk_quota: 256MB  memory: 128MB
```

5. Finally, login into Bluemix from your terminal with `cf login -a https://api.ng.bluemix.net`, build your app with `yarn build`, and then push your app into the world with `cf push`.

#### ?????

After about five minutes, your terminal should say the app is live at <app-name>.mybluemix.net! Now the world can see it. A common error is that your app name has already been taken on Bluemix. Simply choose a more unique name and it should work!  
?????

### [Automagically Deploy from Github with Travis CI](http://Automagically Deploy from Github with Travis CI)

One of the most tedious parts of managing an app is deploying it every time you have changes ready. I would even get lazy and batch my deploys whenever I finally felt like doing it. Thanks to Travis CI (Continuous Integration), deploying can become as simple as [managing your Github repo](https://guides.github.com/activities/hello-world/).

1. First, you need to make a [Github account](https://github.com/join) and set up the [Git on your computer](https://help.github.com/articles/set-up-git/).
2. Next, create a new repo on [Github.com](https://github.com/new) and then follow the terminal instructions provided to push your project to Github:

```
git initgit add .git commit -m 'Initial commit'git remote add origin https://github.com/<github-username/<app-name>.gitgit push -u origin master
```

3. Now head over to [Travis CI](https://travis-ci.org/) to login with your Github credentials. Hit the “+” icon to activate your new repo. If you do not see the repo you just created, click “Sync account” and then it should show up.

4. Then click on the project’s settings in Travis to choose the following options:

Build only if .travis.yml is present = On  
Build pushes = On  
Limit concurrent jobs = Off  
Build pull requests = On (This will allow Github to still run any automated tests you add in the future for opened PRs.)  
Environment Variables: `BLUEMIX_PASSWORD = <Your-bluemix-passwo`rd>

5. The biggest step here is adding the blueprint for Travis as a `.travis.yml` file in the project’s root:

```
sudo: truelanguage: node_jsnode_js:- '5.7'cache:  yarn: true  directories:    - node_modulesenv:  global:  - CF_API=https://api.ng.bluemix.net/  - CF_USERNAME=<Your-bluemix-email>  - CF_ORG=<Your-bluemix-email>  - CF_SPACE=devbefore_deploy:  - wget https://s3.amazonaws.com/go-cli/releases/v6.12.4/cf-cli_amd64.deb -qO temp.deb && sudo dpkg -i temp.deb  - rm temp.deb  - cf login -a ${CF_API} -u ${CF_USERNAME} -p ${BLUEMIX_PASSWORD} -o ${CF_ORG} -s ${CF_SPACE}  - cf install-plugin autopilot -r CF-Community  - yarn builddeploy:  - edge: true    provider: script    script: if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then cf zero-downtime-push <My-app> -f ./manifest.yml; else echo "PR skip deploy"; fi    skip_cleanup: true    on:      branch: master
```

**Important:** Notice that there two places where you insert your Bluemix email and one place where you insert the name of the app on Bluemix!

There is a lot going on here. So I will try to summarize it: In the `before_deploy` section, Travis is building the app, logging into Bluemix as you, and then downloading a Cloud Foundry plugin called Autopilot. Then in the deploy section, Travis decides if the deploy is an open pull request or an actual commit to the Github master branch. If it is an actual commit, run Autopilot to deploy the app.

Autopilot practices Blue-Green Deployment. This means that the new version of your app will be given the name `<my-app>-ven`erable on Bluemix. If the new version builds and runs successfully, the old version of the app is deleted and the new version renames itself to the original name. If the deploy f`ails, <my-app&g`t;-venerable stays up so that you can debug the logs and the old version of the app keeps running so your users see zero downtime!

#### ?????

Dope DevOps, Batman! Navigate to `https://travis-ci.org/<github-username>/<app-nam`e>/builds and you should see a Travis build about to happen. If you click into it, you can watch it start and follow it deploying for you!  
?????

### [Fetch API Data While Keeping Keys Secure](https://github.com/seejamescode/create-react-app-devops/commit/2a4fe33006f46b4f036f1846874ef869243d5743)

Most apps use data from different sources to put together their offerring. For an app to get external data, they use an API to fetch the data. For the API to make sure the right app is fetching data, the app is given a key to identify itself. We need to keep this key secret from our Github repo though!

1. First, let’s ask the [Github API for a key](https://github.com/settings/tokens/new). Under “Select scopes”, we will check `public_repo` to get your repo information. Click “Generate token” and then you will get a key next to a green checkmark!
2. It is time to add the key to our project locally as `keys.json` in the root of our project:

```
{  "github": "<your-github-key>"}
```

However, we do not want your precious key to be uploaded to your Github repo. So, add this file to your `.gitignore` file:

```
# misc.DS_Store.envnpm-debug.log*yarn-debug.log*yarn-error.log*keys.json
```

3. Now that we have your key, we can add a server request. Install Request to your project with `yarn add request` and then edit your server’s `index.js`:

```
import compression from 'compression';import express from 'express';import fs from 'fs';import request from 'request';
```

```
const app = express();const port = process.env.PORT || 8080;app.use(compression());
```

```
let keys;if (fs.existsSync('./keys.json')) {  keys = require('./keys.json');} else {  keys = JSON.parse(process.env.VCAP_SERVICES)['user-provided'][0].credentials;}
```

```
app.get('/github', (req, res) => {  request({    url: `https://api.github.com/user/repos?affiliation=owner,collaborator&access_token=${keys.github}`,    headers: {      'user-agent': 'node.js',    },  }, (err, response, body) => {    if (!err && response.statusCode === 200) {      res.send(body);    }  });});
```

```
app.use(express.static('./build'));
```

```
app.listen(port, (err) => {  if (err) {    console.log(err);    return;  }  console.log(`Server is live at http://localhost:${port}`);});
```

You will first notice an if statement checking if we have the local `keys.json` file. The “else” in that statement will cover when the app is on Bluemix later. We then have an endpoint where pinging `[http://localhost:8080/github](http://localhost:8080/github)` will return your profile’s repos!

4. Open up `src/App.js` to fetch that data to your UI from your server. After these additions, `yarn start` should show all of your project’s repos listed :

```
import React, { Component } from 'react';import logo from './logo.svg';import './App.css';
```

```
class App extends Component {
```

```
  state = {    repos: [],  }
```

```
  componentDidMount() {    fetch('/github')    .then(response => response.json())    .then((data) => {      const repos = data.map((repo) =>        <p key={repo.id}>{repo.name}</p>      );
```

```
      this.setState({ repos })    });  }
```

```
render() {    return (      <div className="App">        <div className="App-header">          <img src={logo} className="App-logo" alt="logo" />          <h2>Welcome to React</h2>        </div>        <p className="App-intro">          To get started, edit <code>src/App.js&lt;/code> and save to reload.        </p>        <h3>App Creator's Repos:</h3>        {this.state.repos}      </div>    );  }}
```

```
export default App;
```

5. Now that we can use the Github API securely in dev mode, let’s make sure your Bluemix app can also get the API key. We are going to create a user-provided service on Bluemix in the terminal: `cf cups keys -p keys.json`. Then tell the `manifest.json` that the app should always bind itself to that service:

```
---applications:- name: <app-name>  buildpack: https://github.com/cloudfoundry/nodejs-buildpack  command: npm run bluemix  disk_quota: 256MB  memory: 128MB  services:     - keys
```

Side Note: If you ever need to update the keys on Bluemix, you can run `cf uups keys -p keys.json`!

#### ?????

After Travis updates your Bluemix app, you should see the UI fetching all of your repos live on the web! We did go through a lot of trouble keeping the keys off of github.com. This is because other devs can abuse your API keys if they get a lot of them.  
?????

### [Create a Staging App for Experimentation](https://github.com/seejamescode/create-react-app-devops/commit/e792b417e6a6b843516fd485668587bc9f513c04)

Now that our production version of the app has DevOps set up, let’s build a staging app. This will help us share works-in-progress for user testing and peer review!

1. We need to make a manifest file for Bluemix that specifies our new staging app now. In the root of your project, make a `manifest-staging.yml` file:

```
---applications:- name: <my-app>-staging  buildpack: https://github.com/cloudfoundry/nodejs-buildpack  command: npm run bluemix  disk_quota: 256MB  memory: 128MB  services:     - keys
```

2. Go ahead and deploy this staging app directly to Bluemix with the new manifest file: `cf push -f manifest-staging.yml`

3. Then we are going to edit the deploy scripts in `.travis.yml`. We need to change the original deploy script for when we commit to master to update the new staging app. We also need to add a new deploy script for the original production app:

```
deploy:  - edge: true    provider: script    script: if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then cf zero-downtime-push <my-app>-staging -f ./manifest-staging.yml; else echo "PR skip deploy"; fi    skip_cleanup: true    on:      branch: master  - edge: true    provider: script    script: if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then cf zero-downtime-push <my-app> -f ./manifest.yml; else echo "PR skip deploy"; fi    skip_cleanup: true    on:      tags: true
```

So now that we update the staging app by committing to the Github master branch, how do we update the production app? You will use [Github’s Releases functionality](https://help.github.com/articles/creating-releases/) as if your app is a real offerring. ?

4. Go ahead and push your latest changes to Github! Then navigate to “Releases” on the Github repo and create a new release.

#### ?????

Based on the last step, you should see two builds in queue on Travis CI. One will be the staging app updating because of the latest commit. The other will be your production app updating because of the new release!  
?????

### The Final, Most Important Value of DevOps

I want to end this write-up by stressing the most important part of DevOps: **automated testing**. Whenever Travis runs, including in opened pull requests, it will check that the command `yarn test` passes before taking action. Create React App already has `yarn test` configured with [Jest](https://facebook.github.io/jest/). However, you can add accessibility, linting, and any other testing framework you are familiar with!

To recap what we have done: First, we quickly got our React project configured thanks to Create React App. Then we built a simple server. We pushed the app into the world. Next, we got Travis deploying the app (with zero downtime) for any of our changes. Then we used the Github API while keeping our key away from public eyes. Lastly, we also set up a staging app so that we could test pre-release.

I hope this project has helped make your workflow easier as you make epic web apps! A big ? goes to the contributors of B[abel,](https://github.com/babel/babel/graphs/contributors) C[reate React App,](https://github.com/facebookincubator/create-react-app/graphs/contributors) E[xpress,](https://github.com/expressjs/express/graphs/contributors) N[ode,](https://github.com/nodejs/node/graphs/contributors) and all other packages used. Also, all the ❤️️ goes to Bluemix, Github, and Travis CI for their free tiers.

Please share in the comments or [tweet me](https://twitter.com/seejamescode) if this helped you! I also would love to hear of different workflows!

You can also contact me by leaving a comment, [emailing me](mailto:james@seejamescode.com), or tweeting to [@seejamescode](https://twitter.com/seejamescode). I work in ATX for IBM Design, and always love conversations with the web design community.

You may also like…

[**How to crank your progressive web app’s Google Lighthouse score up to 100**](https://medium.freecodecamp.com/how-to-crank-your-progressive-web-apps-google-lighthouse-score-up-to-100-cfc053eb7661)  
[_If there’s one message the Chrome Dev Team wants to drive home to developers, it’s this: performance matters._medium.freecodecamp.com](https://medium.freecodecamp.com/how-to-crank-your-progressive-web-apps-google-lighthouse-score-up-to-100-cfc053eb7661)

#### Check out [Create React App DevOps on Github](https://github.com/seejamescode/create-react-app-devops)

