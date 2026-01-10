---
title: Building a community sign-up app with Serverless, StepFunctions, and StackStorm
  Exchange — Episode…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-03T02:03:56.000Z'
originalURL: https://freecodecamp.org/news/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jiZOQLvfX2257LHxe3n4cg.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: AWS Step Functions
  slug: aws-step-functions
- name: Devops
  slug: devops
- name: FaaS
  slug: faas
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Dmitri Zimine

  Build a real-world serverless application on AWS with Serverless framework and ready-to-use
  functions from StackStorm Exchange open-source catalog.

  Episode One | Episode Two | Episode Three | Episode Four

  It took us three exciting ep...'
---

By Dmitri Zimine

Build a real-world serverless application on AWS with [Serverless framework](https://serverless.com/framework/) and ready-to-use functions from [StackStorm Exchange](https://exchange.stackstorm.org) open-source catalog.

[Episode One](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) | [Episode Two](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6) | [Episode Three](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a) | Episode Four

It took us three exciting episodes to create a non-trivial serverless app. The back-end now works, but two things are still missing: a Web UI, and a final discussion to sum up the lessons. Let’s continue… after a quick recap of the previous episodes:

* In [Episode One](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419), I described the application we are building, walked you through setting up the development environment and creating a Serverless project, and showed how to build your first Lambda function from a [StackStorm Exchange](https://exchange.stackstorm.org) action with [Serverless Framework](https://serverless.com/framework).
* In [Episode Two](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6), we added more actions: one native Lambda to record user info to DynamoDB, and another one from StackStorm Exchange to make a call to ActiveCampaign CRM system. You learned more of `serverless.yml`syntax and practiced the development workflow with Lambda functions.
* In [Episode Three](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a), we wired the actions with StepFunctions, learned tricks on passing the data between the steps, struggled debugging StepFunction executions, and finally got the backend working end-to-end.

You can get the final code for this episode from [GitHub](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/3-add-stepfunction).

### Add Web UI

We need a web form that takes user names and emails, and posts to our StepFunction API Gateway endpoint. I just copied the one I used while [exploring Serverless with Python, StepFunctions, and Web Front-end Serverless](https://github.com/dzimine/slack-signup-serverless). Which, I confess, I grabbed from the old [Serverless Slack Invite](https://github.com/serverless-london/serverless-slack-invite) project.

Those of you who are Web developers can surely create something more elegant with ReactJS — PRs welcome! Whether you build your own or grab mine, do this: create a directory `web` and place the static content there.

I use `[http-server](https://www.npmjs.com/package/http-server)` for a quick look that at my static form:

```
cd webhttp-serverStarting up http-server, serving ./Available on:  http://127.0.0.1:8080
```

Open a browser, check the form at [http://127.0.0.1:8080](http://127.0.0.1:8080) , see that it comes out right, and let’s move on to the next step.

How is a serverless web front end deployed to AWS? Typically, you put the static content on S3, configure it to serve the web, make your web app call your backend endpoint, and remember to enable CORS on API Gateway endpoint.

Alternatively, you add a path to your API Gateway resource to serve your static web content from the S3 bucket.

**Pros:** 1) no mess with CORS, 2) no adjusting your web app to point to the correct backend endpoint. Extra bonus: easily done with [serverless-apig-s3](https://github.com/sdd/serverless-apig-s3) plugin.

**Cons:** 1) paying API Gateway charges for web requests 2) the plugin is a bit shaky: fine for examples and small apps, but I wouldn’t use it for anything resembling production.

**PRO TIP:** For serious web front-ends with high loads: deploy them to CloudFront. Or use something like Netlify — check out the recent post [“How to build a static Serverless site with Netlify”](https://serverless.com/blog/how-built-static-serverless-website-netlify/) from serverless.com.

I’ll use the API Gateway approach with [serverless-apig-s3](https://github.com/sdd/serverless-apig-s3) plugin here: we don’t expect massive load. And it is simple. Watch:

Install the plugin (been there, done that):

```
npm install --save-dev serverless-apig-s3
```

Change `serverless.yml`. Add the plugin (been there, done that). Add the [plugin’s configurations](https://github.com/sdd/serverless-apig-s3):

```
...custom:  private: ${file(env.yml):private}  stage: ${opt:stage, self:provider.stage}  region: ${opt:region, self:provider.region}  apigs3:    dist: web    topFiles: true
```

```
...
```

```
plugins:  - serverless-plugin-stackstorm  - serverless-step-functions  - serverless-apig-s3
```

We are telling the plugin to pick our `web` directory and put it to S3. The `topFiles` flag tells API Gateway to expose our `index.html` and `formsubmit.js` at our endpoint, under `/web/`

Now deploy the service, and, separately, the client side, with two commands:

```
sls deploy
```

```
sls client deploy
```

Deploying the service will update the API Gateway with the paths to access our web content. Deploying the client puts the web content up to an S3 bucket. Now you can reason that if you add or remove web files and client deploy is not enough, a full `sls deploy` is required. But if you only change the web files, quick `sls client deploy` will put them up on AWS.

That’s it!   
Go to `https://YOUR-ENDPOINT.amazonaws.com/dev/web/index.html.`The form is right there. The button is orange. You type in the user info and email, hit the orange button. The green message tells you everything is OK. Soon you receive an invitation from Slack. You check the StepFunction executions in AWS console and see everything is green.

![Image](https://cdn-media-1.freecodecamp.org/images/P7X4oec6ilXzVayCaauhg-KqdJAwkcRIMI1w)

**No?!** Most likely, you hit this [apig-s3 bug](https://github.com/sdd/serverless-apig-s3/issues/16), just like I did. And just like I did, you got to do a little final step manually.

Open AWS Console ->API Gateway->Resources->Actions-Deploy API.   
Or use AWS CLI:

```
# Find out your rest-api-id firstaws apigateway get-rest-apis
```

```
# Deploy the changes to the stage# Don't COPY-PASTE, it needs YOUR ID!aws apigateway create-deployment --rest-api-id  YOUR_API_ID  --stage-name dev
```

**Now it works for me.**

**PRO TIP:** The plugin works when everything is deployed from scratch. But if you’re tempted to `sls remove` and redeploy again, you hit at least one [other plugin bug](https://github.com/sdd/serverless-apig-s3/issues/11) on removing the stack. See Tips and Tricks at the end of the post on how to properly clean-up.

![Image](https://cdn-media-1.freecodecamp.org/images/AxHuvaj3Gp0QWiqDinSqS43JfK1RsrcQJsVw)

Congratulations! You made it. You might have followed along and built your own app. You might have dropped it at some point out of frustration or fatigue. You might have just skimmed the text and examples. But if you made it to the end, you learned enough of serverless to be dangerous.

### Reflection

After wrestling through all the 4 episodes, you likely sensed it: serverless is not simple. Many things can go wrong as you build a serverless app.

You can blame some on me: I surely made a few mistakes and omissions (BTW reports and comments much appreciated!)

But serverless complexity is not all my fault. We wire together many different services — AWS and 3rd party — with many different wires — frameworks and tools. The services are of different quality and [in]convenience (don’t get me started on AWS StepFunction CLI). The frameworks and tools are still maturing (which serverless plugin made you struggle the most?).

Why get into serverless? Because for some classes of apps, it is substantially cheaper. This community signup is a case in point: we used to run StackStorm’s with StackStorm. It was simple to build and solid like a rock, but it took a `m3.large` instance at $100/month, without even getting to multi-zone reliability. With serverless it runs at less than $1/month, thanks to the occasional load pattern. $100 would buy us ~5,000,000 sign-ups — that’s more that we’ll ever need!

On the other extreme, high volume apps with high reliability requirements might be better as serverless too, leveraging “infinite” elasticity which may be expensive to build and operate yourself. I carefully use “_might_” and “_would_”, as the equation varies greatly from case to case. Do your math upfront, watch your load patterns, explore your bill.

As for taming complexity, [Serverless framework](https://serverless.com/framework) helps. To fully appreciate it, try and redo the same app without it. Make it reliable, repeatable, reviewable infrastructure-as-code. While Serverless framework is not the only game in town, I specifically like it for it’s pluggable architecture and the plugin ecosystem.

Plugins help, picking up in areas not covered by the core Serverless framework. Using the plugins, we enjoyed the simplicity of building StepFuncions and adding simple web front-ends (and if you haven’t, try and redo it without the plugins). There are more: skim and bookmark the [list of official plugins](https://github.com/serverless/plugins) to keep them in mind when for your next project.

[StackStorm Exchange](https://exchange.stackstorm.org) — the recent addition to the serverless ecosystem — brings a catalog of reusable integrations. While it is not hard to scrape APIs for ActiveCampaign or find and use undocumented Slack API calls, it is low-value work that takes away from building the application logic.

Explore what is already there: while DevOps integrations dominate due to StackStorm roots in IT automation, I expect that variety will grow now that Serverless community is joining to contribute and co-pilot the catalog.

With that, **we are officially done.** Enjoy!

### A few more Tips and Tricks

* Removing everything will not remove the DynamoDB table. A reasonable default, but when you try and re-deploy the service, it’ll cry that the table can’t be created as it already exists. Delete it: `aws dynamodb delete-table --table-name signup-stormless-dev`
* Due to an apig-s3 bug, `sls remove` will fail complaining that the bucket is not empty. Remove the web s3 bucket manually when removing a stack. `aws s3 rb s3://bucketname --force`
* Removing the stack does not remove the DynamoDB table. If you really want to start from scratch, delete it manually (export the data first):  
 `aws dynamodb delete-table --table-name slack-signup-dev`
* Sometimes `sls delete` fails to clean up. Reasons might be various, but the place to look is the same. Did I tell you to master CloudFormation? Go there, find a stack that failed to delete, find the reason, fix, and delete the stack.

Hope this helped you learn something new, find something interesting, or provoked some good thoughts. Please share your thoughts in the comments here, or tweet me [@dzimine](https://twitter.com/dzimine).

