---
title: What are Github Actions and How Can You Automate Tests and Slack Notifications?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-03T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-are-github-actions-and-how-can-you-automate-tests-and-slack-notifications
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/github-actions.jpg
tags:
- name: automation
  slug: automation
- name: 'automation testing '
  slug: automation-testing
- name: CI/CD
  slug: cicd
- name: continuous delivery
  slug: continuous-delivery
- name: continuous deployment
  slug: continuous-deployment
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
- name: slack
  slug: slack
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: "Automation is a powerful tool. It both saves us time and can help reduce\
  \ human error. \nBut automation can be tough and can sometimes prove to be costly.\
  \ How can Github Actions help harden our code and give us more time to work on features\
  \ instead of ..."
---

Automation is a powerful tool. It both saves us time and can help reduce human error. 

But automation can be tough and can sometimes prove to be costly. How can Github Actions help harden our code and give us more time to work on features instead of bugs?

* [What are Github Actions?](#heading-what-are-github-actions)
* [What is CI/CD?](#heading-what-is-cicd)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Part 0: Setting up a project](#heading-part-0-setting-up-a-project)
* [Part 1: Automating tests](#heading-part-1-automating-tests)
* [Part 2: Post new pull requests to Slack](#heading-part-2-post-new-pull-requests-to-slack)

%[https://www.youtube.com/watch?v=1n-jHHNSoTw]

## What are Github Actions?

[Actions](https://github.com/features/actions) are a relatively new feature to [Github](https://github.com/) that allow you to set up CI/CD workflows using a configuration file right in your Github repo.

Previously, if you wanted to set up any kind of automation with tests, builds, or deployments, you would have to look to services like [Circle CI](https://circleci.com/) and [Travis](https://travis-ci.org/) or write your own scripts. But with Actions, you have first class support to powerful tooling to automate your workflow.

## What is CI/CD?

CD/CD stands for Continuous Integration and Continuous Deployment (or can be Continuous Delivery). They're both practices in software development that allow teams to build projects together quickly, efficiently, and ideally with less errors.

Continuous Integration is the idea that as different members of the team work on code on different git branches, the code is merged to a single working branch which is then built and tested with automated workflows. This helps to constantly make sure everyone's code is working properly together and is well-tested.

Continuous Deployment takes this a step further and takes this automation to the deployment level. Where with the CI process, you automate the testing and the building, Continuous Deployment will automate deploying the project to an environment. 

The idea is that the code, once through any building and testing processes, is in a deployable state, so it should be able to be deployed.

## What are we going to build?

We're going to tackle two different workflows.

The first will be to simply run some automated tests that will prevent a pull request from being merged if it is failing. We won't walk through building the tests, but we'll walk through running tests that already exist.

In the second part, we'll set up a workflow that sends a message to slack with a link to a pull request whenever a new one is created. This can be super helpful when working on open source projects with a team and you need a way to keep track of requests.

## Part 0: Setting up a project

For this guide, you can really work through any node-based project as long as it has tests you can run for Part 1.

If you'd like to follow along with a simpler example that I'll be using, I've set up a new project that you can clone with a single function that has two tests that are able to run and pass.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/function-with-test.jpg)
_A function with two tests_

If you'd like to check out this code to get started, you can run:

```shell
git clone --single-branch --branch start git@github.com:colbyfayock/my-github-actions.git

```

Once you have that cloned locally and have installed the dependencies, you should be able to run the tests and see them pass!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/passing-tests.jpg)
_Passing tests_

It should also be noted that you'll be required to have this project added as a new repository on Github in order to follow along.

[Follow along with the commit!](https://github.com/colbyfayock/my-github-actions/commit/6919b1b9beea4823fd28375f1864d233e23f2d26)

## Part 1: Automating tests

Tests are an important part of any project that allow us to make sure we're not breaking existing code while we work. While they're important, they're also easy to forget about.

We can remove the human nature out of the equation and automate running our tests to make sure we can't proceed without fixing what we broke.

### Step 1: Creating a new action

The good news, is Github actually makes it really easy to get this workflow started as it comes as one of their pre-baked options.

We'll start by navigating to the **Actions** tab on our repository page.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-actions-dashboard.jpg)
_Github Actions starting page_

Once there, we'll immediately see some starter workflows that Github provides for us to dive in with. Since we're using a node project, we can go ahead and click **Set up this workflow** under the **Node.js** workflow.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-new-nodejs-workflow.jpg)
_Setting up a Node.js Github Action workflow_

After the page loads, Github will land you on a new file editor that already has a bunch of configuration options added.

We're actually going to leave this "as is" for our first step. Optionally, you can change the name of the file to `tests.yml` or something you'll remember.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-create-new-workflow.jpg)
_Adding a new Github Action workflow file_

You can go ahead and click **Start commit** then either commit it directory to the `master` branch or add the change to a new branch. For this walkthrough, I'll be committing straight to `master`.

To see our new action run, we can again click on the **Actions** tab which will navigate us back to our new Actions dashboard.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-status.jpg)
_Viewing Github Action workflow events_

From there, you can click on **Node.js CI** and select the commit that you just made above and you'll land on our new action dashboard. You can then click one of the node versions in the sidebar via **build (#.x)**, click the **Run npm test** dropdown, and we'll be able to see the output of our tests being run (which if you're following along with me, should pass!).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-logs.jpg)
_Viewing logs of a Github Action workflow_

[Follow along with the commit!](https://github.com/colbyfayock/my-github-actions/commit/10e397966572ed9975cac40f6ab5f41c1255a947)

### Step 2: Configuring our new action

So what did we just do above? We'll walk through the configuration file and what we can customize.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-file.jpg)
_Github Action Node.js workflow file_

Starting from the top, we specify our name:

```yaml
name: Node.js CI

```

This can really be whatever you want. Whatever you pick should help you remember what it is. I'm going to customize this to "Tests" so I know exactly what's going on.

```yaml
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

```

The `on` key is how we specify what events trigger our action. This can be a variety of things like based on time with [cron](https://en.wikipedia.org/wiki/Cron). But here, we're saying that we want this action to run any time someone pushes commits to  `master` or someone creates a pull request targeting the `master` branch. We're not going to make a change here.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest

```

This next bit creates a new job called `build`. Here we're saying that we want to use the latest version of Ubuntu to run our tests on. [Ubuntu](https://ubuntu.com/) is common, so you'll only want to customize this if you want to run it on a specific environment.

```yaml
    strategy:
      matrix:
        node-version: [10.x, 12.x, 14.x]

```

Inside of our job we specify a [strategy](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#jobsjob_idstrategy) matrix. This allows us to run the same tests on a few different variations. 

In this instance, we're running the tests on 3 different versions of [node](https://nodejs.org/en/) to make sure it works on all of them. This is definitely helpful to make sure your code is flexible and future proof, but if you're building and running your code on a specific node version, you're safe to change this to only that version.

```yaml
    steps:
    - uses: actions/checkout@v2
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v1
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm ci
    - run: npm run build --if-present
    - run: npm test

```

Finally, we specify the steps we want our job to run. Breaking this down:

* `uses: actions/checkout@v2`: In order for us to run our code, we need to have it available. This checks out our code on our job environment so we can use it to run tests.
* `uses: actions/setup-node@v1`: Since we're using node with our project, we'll need it set up on our environment. We're using this action to do that setup  for us for each version we've specified in the matrix we configured above.
* `run: npm ci`: If you're not familiar with `npm ci`, it's similar to running `npm install` but uses the `package-lock.json` file without performing any patch upgrades. So essentially, this installs our dependencies.
* `run: npm run build --if-present`: `npm run build` runs the build script in our project. The `--if-present` flag performs what it sounds like and only runs this command if the build script is present. It doesn't hurt anything to leave this in as it won't run without the script, but feel free to remove this as we're not building the project here.
* `run: npm test`: Finally, we run `npm test` to run our tests. This uses the `test` npm script set up in our `package.json` file.

And with that, we've made a few tweaks, but our tests should run after we've committed those changes and pass like before!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-action-workflow-logs-npm-test.jpg)
_Logs of passing tests in Github Action workflow_

[Follow along with the commit!](https://github.com/colbyfayock/my-github-actions/commit/087cd8e8592d1f2b520b6e44b70b0a242a9d2d72)

### Step 3: Testing that our tests fail and prevent merges

Now that our tests are set up to automatically run, let's try to break it to see it work.

At this point, you can really do whatever you want to intentionally break the tests, but [here's what I did](https://github.com/colbyfayock/my-github-actions/pull/1):

![Image](https://www.freecodecamp.org/news/content/images/2020/05/bad-changes-code-diff.jpg)
_Code diff - https://github.com/colbyfayock/my-github-actions/pull/1_

I'm intentionally returning different expected output so that my tests will fail. And they do!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-failing-checks.jpg)
_Failing status checks on pull request_

In my new pull request, my new branch breaks the tests, so it tells me my checks have failed. If you noticed though, it's still green to merge, so how can we prevent merges?

We can prevent pull requests from being merged by setting up a Protected Branch in our project settings.

First, navigate to **Settings**, then **Branches**, and click **Add rule**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-add-protected-branch.jpg)
_Github branch protection rules_

We'll then want to set the branch name pattern to `*`, which means all branches, check the **Require status checks to pass before merging option**, then select all of our different status checks that we'd like to require to pass before merging.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-configure-protected-branch.jpg)
_Setting up a branch protection rule in Github_

Finally, hit **Create** at the bottom of the page.

And once you navigate back to the pull request, you'll notice that the messaging is a bit different and states that we need our statuses to pass before we can merge.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-failing-checks-cant-merge.jpg)
_Failing tests preventing merge in pull request_

_Note: as an administrator of a repository, you'll still be able to merge, so this technically only prevents non-administrators from merging. But will give you increased messaging if the tests fail._

And with that, we have a new Github Action that runs our tests and prevents pull requests from merging if they fail.

[Follow along with the pull request!](https://github.com/colbyfayock/my-github-actions/pull/1)

_Note: we won't be merging that pull request before continuing to Part 2._

## Part 2: Post new pull requests to Slack

Now that we're preventing merge requests if they're failing, we want to post a message to our [Slack](http://slack.com/) workspace whenever a new pull request is opened up. This will help us keep tabs on our repos right in Slack.

For this part of the guide, you'll need a Slack workspace that you have permissions to create a new developer app with and the ability to create a new channel for the bot user that will be associated with that app.

### Step 1: Setting up Slack

There are a few things we're going to walk through as we set up Slack for our workflow:

* Create a new app for our workspace
* Assign our bot permissions
* Install our bot to our workspace
* Invite our new bot to our channel

To get started, we'll create a new app. Head over to the [Slack API Apps dashboard](https://api.slack.com/apps). If you already haven't, log in to your Slack account with the Workspace you'd like to set this up with.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-create-new-app.jpg)
_Creating a new Slack app_

Now, click **Create New App** where you'll be prompted to put in a name and select a workspace you want this app to be created for. I'm going to call my app "Gitbot" as the name, but you can choose whatever makes sense for you. Then click **Create App**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-add-name-new-app.jpg)
_Configuring a new Slack app_

Once created, navigate to the **App Home** link in the left sidebar. In order to use our bot, we need to assign it [OAuth](https://oauth.net/) scopes so it has permissions to work in our channel, so select **Review Scopes to Add** on that page.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-review-scopes.jpg)
_Reviewing Slack app scopes_

Scroll own and you'll see a **Scopes** section and under that a **Bot Token** section. Here, click **Add an OAuth Scope**. For our bot, we don't need a ton of permissions, so add the `channels:join` and `chat:write` scopes and we should be good to go.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-add-scopes.jpg)
_Adding scopes for a Slack app Bot Token_

Now that we have our scopes, let's add our bot to our workspace. Scroll up on that same page to the top and you'll see a button that says **Install App to Workspace**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-install-app-to-workspace.jpg)
_Installing Slack app to a workspace_

Once you click this, you'll be redirected to an authorization page. Here, you can see the scopes we selected for our bot. Next, click **Allow**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-allow-workspace-permissions.jpg)
_Allowing permission for Slack app to be installed to workspace_

At this point, our Slack bot is ready to go. At the top of the **OAuth & Permissions** page, you'll see a **Bot User OAuth Access Token**. This is what we'll use when setting up our workflow, so either copy and save this token or remember this location so you know how to find it later.

_Note: this token is private - don't give this out, show it in a screencast, or let anyone see it!_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-oauth-token.jpg)
_Copying OAuth Access Token for Slack bot user_

Finally, we need to invite our Slack bot to our channel. If you open up your workspace, you can either use an existing channel or create a new channel for these notifications, but you'll want to enter the command `/invite @[botname]` which will invite our bot to our channel.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-invite-bot-to-channel.jpg)
_Inviting Slack bot user to channel_

And once added, we're done with setting up Slack!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-app-bot-joined-channel.jpg)
_Slack bot was added to channel_

### Create a Github Action to notify Slack

Our next step will be somewhat similar to when we created our first Github Action. We'll create a workflow file which we'll configure to send our notifications.

While we can use our code editors to do this by creating a file in the `.github` directory, I'm going to use the Github UI.

First, let's navigate back to our _Actions_ tab in our repository. Once there, select **New workflow**.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-new-workflow.jpg)
_Setting up a new Github Action workflow_

This time, we're going to start the workflow manually instead of using a pre-made Action. Select **set up a workflow yourself** at the top.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-set-up-new-workflow.jpg)
_Setting up a Github Action workflow manually_

Once the new page loads, you'll be dropped in to a new template where we can start working. Here's what our new workflow will look like:

```yaml
name: Slack Notifications

on:
  pull_request:
    branches: [ master ]

jobs:
  notifySlack:

    runs-on: ubuntu-latest

    steps:
    - name: Notify slack
      env:
        SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
      uses: abinoda/slack-action@master
      with:
        args: '{\"channel\":\"[Channel ID]\",\"blocks\":[{\"type\":\"section\",\"text\":{\"type\":\"mrkdwn\",\"text\":\"*Pull Request:* ${{ github.event.pull_request.title }}\"}},{\"type\":\"section\",\"text\":{\"type\":\"mrkdwn\",\"text\":\"*Who?:* ${{ github.event.pull_request.user.login }}\n*Request State:* ${{ github.event.pull_request.state }}\"}},{\"type\":\"section\",\"text\":{\"type\":\"mrkdwn\",\"text\":\"<${{ github.event.pull_request.html_url }}|View Pull Request>\"}}]}'

```

So what's happening in the above?

* `name`: we're setting a friendly name for our workflow
* `on`: we want our workflow to trigger when there's a pull request is created that targets our `master` branch
* `jobs`: we're creating a new job called `notifySlack`
* `jobs.notifySlack.runs-on`: we want our job to run on a basic setup of the latest Unbuntu
* `jobs.notifySlack.steps`: we really only have one step here - we're using a pre-existing Github Action called [Slack Action](https://github.com/marketplace/actions/post-slack-message) and we're configuring it to publish a notification to our Slack

There are two points here we'll need to pay attention to, the `env.SLACK_BOT_TOKEN` and the `with.args`.

In order for Github to communicate with Slack, we'll need a token. This is what we're setting in `env.SLACK_BOT_TOKEN`. We generated this token in the first step. Now that we'll be using this in our workflow configuration, we'll need to [add it as a Git Secret in our project](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets-for-a-repository).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-slack-token-secret.jpg)
_Github secrets including SLACK_BOT_TOKEN_

The  `with.args` property is what we use to configure the payload to the Slack API that includes the channel ID (`channel`) and our actual message (`blocks`).

The payload in the arguments is stringified and escaped. For example, when expanded it looks like this:

```json
{
  "channel": "[Channel ID]",
  "blocks": [{
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*Pull Request:* ${{ github.event.pull_request.title }}"
    }
  }, {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*Who?:*n${{ github.event.pull_request.user.login }}n*State:*n${{ github.event.pull_request.state }}"
    }
  }, {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "<${{ github.event.pull_request._links.html.href }}|View Pull Request>"
    }
  }]
}

```

_Note: this is just to show what the content looks like, we need to use the original file with the stringified and escaped argument._

Back to our configuration file, the first thing we set is our channel ID. To find our channel ID, you'll need to use the Slack web interface. Once you open Slack in your browser, you want to find your channel ID in the URL:

```
https://app.slack.com/client/[workspace ID]/[channel ID]

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-web-channel-id.jpg)
_Channel ID in Slack web app URL_

With that channel ID, you can modify our workflow configuration and replace `[Channel ID]` with that ID:

```yaml
with:
  args: '{\"channel\":\"C014RMKG6H2\",...

```

The rest of the arguments property is how we set up our message. It includes variables from the Github event that we use to customize our message. 

We won't go into tweaking that here, as what we already have will send a basic pull request message, but you can test out and build your own payload with Slack's [Block Kit Builder](https://app.slack.com/block-kit-builder/).

[Follow along with the commit!](https://github.com/colbyfayock/my-github-actions/commit/e228b9899ef3da218d1a100d06a72259d45ea19e)

### Test out our Slack workflow

So now we have our workflow configured with our Slack app, finally we're ready to use our bot!

For this part, all we need to do is create a new pull request with any change we want. To test this out, I simply [created a new branch](https://github.com/colbyfayock/my-github-actions/pull/2) where I added a sentence to the `README.md` file.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/github-test-pull-request.jpg)
_Code diff - [https://github.com/colbyfayock/my-github-actions/pull/2](https://github.com/colbyfayock/my-github-actions/pull/2)_

Once you [create that pull request](https://github.com/colbyfayock/my-github-actions/pull/2), similar to our tests workflow, Github will run our Slack workflow! You can see this running in the Actions tab just like before.

As long as you set everything up correctly, once the workflow runs, you should now have a new message in Slack from your new bot.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/slack-github-notification.jpg)
_Slack bot automated message about new pull request_

_Note: we won't be merging that pull request in._

## What else can we do?

### Customize your Slack notifications

The message I put together is simple. It tells us who created the pull request and gives us a link to it.

To customize the formatting and messaging, you can use the Github [Block Kit Builder](https://app.slack.com/block-kit-builder/) to create your own.

If you'd like to include additional details like the variables I used for the pull request, you can make use of Github's available [contexts](https://help.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#contexts). This lets you pull information about the environment and the job to customize your message.

I couldn't seem to find any sample payloads, so here's an example of a sample `github` context payload you would expect in the event.

[Sample github context](https://gist.github.com/colbyfayock/1710edb9f47ceda0569844f791403e7e)

### More Github actions

With our ability to create new custom workflows, that's not a lot we can't automate. Github even has a [marketplace](https://github.com/marketplace?type=actions) where you can browse around for one.

If you're feeling like taking it a step further, you can even create your own! This lets you set up scripts to configure a workflow to perform whatever tasks you need for your project.

## Join in the conversation!

%[https://twitter.com/colbyfayock/status/1268197100539514881]

## What do you use Github actions for?

Share with me on [Twitter](https://twitter.com/colbyfayock)!

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

