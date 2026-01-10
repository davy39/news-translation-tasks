---
title: How to Validate Pull Requests in AWS and Make Code Reviews Easier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-23T15:59:03.000Z'
originalURL: https://freecodecamp.org/news/validate-pull-requests-in-aws
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9893740569d1a4ca1ad3.jpg
tags:
- name: AWS
  slug: aws
- name: code review
  slug: code-review
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: "By Aagam Vadecha\nWhen a project grows, and developers are pushing code\
  \ frequently, there is always a chance that working pull requests might break somewhere.\
  \ \nIt could be because one PR was merged before another, or the destination branch\
  \ moved a few..."
---

By Aagam Vadecha

When a project grows, and developers are pushing code frequently, there is always a chance that working pull requests might break somewhere. 

It could be because one PR was merged before another, or the destination branch moved a few commits ahead, causing conflicts. 

Or maybe because a developer didn’t run tests before pushing and unknowingly introduced a bug in some other part of the product. And the list goes on.

But this shouldn't be a problem. Every organization has a workflow for Code Reviews, right? But it still takes up a lot of time. Especially for those PR's that break and are not even ready for review. 

We can manually build and test our code every time before a proper code review, no doubt. But after a certain point, it seems better to automate it. 

Imagine a medium size organization with 100–150 PR’s every week. The time spent repetitively validating those might give that firm a whole set of new features. Well then, let’s go get those features!

## Prerequisites

You should have some familiarity with AWS Services. 

I assume you know how to create and manage Lambda Functions, Codebuild Projects, Cloudwatch Events, IAM Roles, and that you’re using CodeCommit to version your codebase.

## Architecture

Let’s understand, at a high level, how we are going to tackle this project.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/ValidatePR-Architecture-Flowchart.png)
_Uh huh, What?_

Step by step, let’s understand our workflow better.

1. Let’s say a new PR is created / an existing PR is updated.
2. A Cloudwatch event that is watching our repository will be activated and will send relevant data to a lambda function.
3. This function will do two things  
 → Trigger CodeBuild Project to build our latest commit and run tests.   
 → Comment any custom message that we want on our PR.
4. After CodeBuild finishes running the build, another Cloudwatch event will send those build results to a lambda function.
5. This function will comment the build results on our PR.

Alright then, let’s get started!

## Setting up our App

For the sake of simplicity, I’ve created a simple Node.js application. It’s written in TypeScript and all the build phase does is compile the ‘app.ts’ to ‘app.js’.

[Here’s](https://github.com/aagam29/ValidatePR) the link to the repo – clone and use it if you want to follow along.   
All the relevant code used in this article can be found there.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/simple-express-app-screenshots.jpg)
_A simple Express app_

The `build` command here is a simple `tsc app.ts` , but you can change it to your project’s build command.

Also to keep it simple, I’ve not included test cases. You can link them to `test` in the script section of `package.json` and follow along.

## Codebuild Project

First, you'll want to set up a basic CodeBuild project for your repository. 

**To do this, do the following:**

* Set up source as your Codecommit repository
* Reference type should be branch
* Environment should be per the project's requirements
* You should use a buildspec file
* The rest should just be defaults.

Make sure you have a `buildspec.yml` file in your repo’s root folder.

Note: this might differ if you’re dealing with a MonoRepo. In that case, you might have separate buildspec.yml files for each App and will have to selectively pass the buildspec file path as an environment variable depending on the files changed inside the commit. 

We have a similar setup at our organization, and we're loving the results at present!

```yml
version: 0.2
phases:
  install:
    commands:
     - n 12.12
     - curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
     - echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
     - apt update
     - apt install yarn
     - yarn install
#   pre_build:
#     commands:
#     - yarn test
  build:
    commands:
     - yarn build
```

What does this buildspec.yml do? Well, it passes runtime commands for each build to our CodeBuild project.

And then does what? ?

* Installs node 12.12.0
* Installs yarn
* Installs our project’s dependencies.
* yarn test (It runs our test cases. There are none here, but you can uncomment that section if you need it.)
* yarn build (Builds our project.)

## Lambda Functions

Let’s set up two functions as discussed in the architecture section above.

The function **TriggerCodebuildStart** will receive a Cloudwatch Event (which we will set up in a bit) and it will trigger our CodeBuild project to start a fresh build.

It will also post a Build Started comment with the timestamp and a neat link to the build logs in our PR’s comment section.

The function **TriggerCodebuildResult** will receive a Cloudwatch Event from our CodeBuild project which will have the build results. 

It will also post the Codebuild Results comment with the timestamp and a neat link to the build logs in our PR’s comment section.

Here’s the code. That’s what you were waiting for, weren’t you! ? 

```js
const AWS = require('aws-sdk');
const codecommit = new AWS.CodeCommit();
const codebuild = new AWS.CodeBuild();

exports.handler = async (event) => {
    try {
        console.log('Received Event: ', event);
        const { destinationCommit } = event.detail;
        const { sourceCommit } = event.detail;
        const { pullRequestId } = event.detail;
        const pullRequestName = event.detail.title;
        const sourceBranch = event.detail.sourceReference.split('/').pop();
        const triggerCodeBuildParameters = {
            sourceBranch, sourceCommit, destinationCommit, pullRequestId, pullRequestName
        };
        const codeBuildResult = await triggerCodebuild(triggerCodeBuildParameters);
        
        const buildId = codeBuildResult.build.id;
        const postBuildStartedCommentOnPRParameters = {
            sourceCommit, destinationCommit, pullRequestId, buildId
        }
        
        await postBuildStartedCommentOnPR(postBuildStartedCommentOnPRParameters);
        
        return {
            statusCode: 200
        };
    }
    catch (error) {
        console.log('An Error Occured', error);
        return { 
            error
        };
    }
};

async function postBuildStartedCommentOnPR(postBuildStartedCommentOnPRParameters) {
    const { sourceCommit, destinationCommit, pullRequestId, buildId } = postBuildStartedCommentOnPRParameters;
    const logLink = `https://${process.env.REGION}.console.aws.amazon.com/codesuite/codebuild/projects/ValidatePullRequest/build/${buildId}`;
    const parameters = {
        afterCommitId: sourceCommit,
        beforeCommitId: destinationCommit,
        content: `Build For Validating The Pull Request has been started.   
        Timestamp: **${Date.now()}**   
        Check [CodeBuild Logs](${logLink})`,
        pullRequestId,
        repositoryName: process.env.REPOSITORY_NAME
    };

    const request = await codecommit.postCommentForPullRequest(parameters);
    const promise = request.promise();
    return promise.then(
        (data) => data,
        (error) => {
            console.log('Error In Commenting To Pull Request', error);
            throw new Error(error);
        }
    );
}

async function triggerCodebuild(triggerCodeBuildParameters) {
    const { sourceBranch, sourceCommit, destinationCommit, pullRequestId, pullRequestName } = triggerCodeBuildParameters;
    console.log(`Triggering Codebuild, Branch: ${sourceBranch}`);
    const parameters = {
        projectName: process.env.CODEBUILD_PROJECT,
        sourceVersion: `refs/heads/${sourceBranch}^{${sourceCommit}}`,
        environmentVariablesOverride: [
            {
                name: 'pullRequestId',
                value: pullRequestId,
                type: 'PLAINTEXT'
            },
            {
                name: 'sourceCommit',
                value: sourceCommit,
                type: 'PLAINTEXT'
            },
            {
                name: 'destinationCommit',
                value: destinationCommit,
                type: 'PLAINTEXT'
            },
            {
                name: 'pullRequestName',
                value: pullRequestName,
                type: 'PLAINTEXT'
            }
        ]
    };
    const request = await codebuild.startBuild(parameters);
    const promise = request.promise();
    return promise.then(
        (data) => data,
        (error) => {
            console.log('Error In Starting Codebuild', error);
            throw new Error(error);
        }
    );
}
```

```js
const AWS = require('aws-sdk');
const codecommit = new AWS.CodeCommit();
exports.handler = async (event) => {
    try {
        console.log('Event', event);
        const parameters = await getParameters(event);
        console.log('Parameters For Comment:', parameters);
        await commentCodeBuildResultOnPR(parameters);
        return { statusCode: 200 };
    }
    catch (error) {
        console.log('An Error Occured', error);
        return { error };
    }
};

async function getParameters(event) {
    try {
        const buildId = event.detail['build-id'].split('/')[1];
        const buildStatus = event.detail['build-status'];
        const environmentVariableList = event.detail['additional-information'].environment['environment-variables'];
        let afterCommitId, beforeCommitId, content, pullRequestId;
        for (element of environmentVariableList) {
            if (element.name === 'pullRequestId') pullRequestId = element.value;
            if (element.name === 'sourceCommit') afterCommitId = element.value;
            if (element.name === 'destinationCommit') beforeCommitId = element.value;
            if (element.name === 'pullRequestName') pullRequestName = element.value;
        }

        const logLink = `https://${process.env.REGION}.console.aws.amazon.com/codesuite/codebuild/projects/ValidatePullRequest/build/${buildId}`;
        content = `Build Result: **${buildStatus}**   
        Timestamp: **${Date.now()}**   
        Check [CodeBuild Logs](${logLink})`;

        return {
            afterCommitId,
            beforeCommitId,
            content,
            pullRequestId,
            repositoryName: process.env.REPOSITORY_NAME
        };
    } catch (error) {
        throw error;
    }
}

async function commentCodeBuildResultOnPR(parameters) {
    const request = await codecommit.postCommentForPullRequest(parameters);
    const promise = request.promise();
    return promise.then(
        (data) => data,
        (error) => {
            console.log('Error In Commenting To Pull Request', error);
            throw new Error(error);
        }
    );
}
```

You'll need to fill in the appropriate environment variables before using these functions. Read the code once and you’ll know what to do.

In case you need to refer to the docs, just go [here](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CodeBuild.html#startBuild-property) and [there](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CodeCommit.html#postCommentForPullRequest-property). ? 

## Configure Cloudwatch Events

Okay, now to hook it all up, let’s configure our Cloudwatch events.

We’ll create two events: One will receive new commit data from our repository, and the other will receive the Codebuild Results. The targets for these events will be our lambda functions.  
  
I'm attaching full-page screenshots here. This will make it easier for you to understand the references.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/CloudWatch-Events.png)
_Focus on the Green Ones_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Start--CloudWatch-Event-1.png)
_Replace with your CodeBuild project’s ARN._

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Result---Cloudwatch-Event.png)
_Almost there!_

I’ve chosen to trigger the lambda function on FAILED and SUCCEEDED events. But you can select All Events too and tailor it to your needs.

## And, Action!

Okay, you’re super cool if you made it to this point. ? After so much work, Let’s see what we’ve achieved. 

Let’s make two pull requests, one which is works well and the other which has an intentional build error.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/New-Working-PR.png)
_Error Free PR_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Successfull-build.png)
_Great!_

Now, let's create a PR with bugs. See here, instead of **app.get** there’s **ap.get.** It’s intentional and silly. But it will do the job for now.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Faulty-PR.png)
_Faulty PR_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Failed-build.png)
_Failed Build Message, Happy reviewers. Didn’t have to checkout the branch and test!_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Failed-Logs.png)
_Devs, as usual, we’ve got logs for you!_

## Wrapping up

To take this a step further, you could trigger an API call to your Slack webhook URL to immediately notify in a channel in case of build failures. Awesome, right?

Also, this is a very simple set up and real-world projects might be more complex.   
For example, MonoRepos might have multiple apps and builds, and tests for each of those apps are different. 

Triggering all those tests every time will be of no use, and it'll be costlier and create confusion. You might need to selectively trigger those builds depending on which files were committed and which apps were affected.

However, this article should build up a decent base for you. And you can definitely expand on it. After all, you’re awesome too. :)

**Thanks for reading!** If you need some help regarding this, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/aagamvadecha/). Looking forward to helping however I can.

