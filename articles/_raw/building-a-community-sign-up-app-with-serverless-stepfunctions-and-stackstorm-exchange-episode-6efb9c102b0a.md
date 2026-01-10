---
title: Building a community sign-up app with Serverless, StepFunctions, and StackStorm
  Exchange — Episode…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T07:06:59.000Z'
originalURL: https://freecodecamp.org/news/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0xq8ywxkBv-oIe6b-6H9ug.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: AWS Step Functions
  slug: aws-step-functions
- name: FaaS
  slug: faas
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Dmitri Zimine

  Build a real-world serverless application on AWS with Serverless framework and ready-to-use
  functions from StackStorm Exchange open-source catalog.

  Episode One | Episode Two | Episode Three | Episode Four

  We are at Episode Three. Qui...'
---

By Dmitri Zimine

Build a real-world serverless application on AWS with [Serverless framework](https://serverless.com/framework/) and ready-to-use functions from [StackStorm Exchange](https://exchange.stackstorm.org) open-source catalog.

[Episode One](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) | [Episode Two](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6) | Episode Three | [Episode Four](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6)

We are at Episode Three. Quick recap:

* In [Episode One](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419), I described the application we are building, walked you through setting up the development environment and creating a Serverless project, and showed how to build your first Lambda function from a [StackStorm Exchange](https://exchange.stackstorm.org) action with [Serverless Framework](https://serverless.com/framework).
* In [Episode Two](https://medium.com/@dzimine/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6), we added more actions: one native Lambda to record user info to DynamoDB, and another one from StackStorm Exchange to make a call to ActiveCampaign CRM system. You learned more of `serverless.yml` syntax and practiced the development workflow with Lambda functions.

In this third episode, I’ll show how to use AWS StepFunction to wire the actions into a workflow.

You can get the final code for this episode from [GitHub](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/3-add-stepfunction).

### Wiring functions together with StepFunction

Now that our building blocks — Lambda functions — are all lined up, it’s time to string them together. An [AWS StepFunction](https://aws.amazon.com/step-functions/) will define the sequence of calls, maintain the state of the sign-up workflow, and carry the data between the steps. I’ll use the`[serverless-step-functions](https://github.com/horike37/serverless-step-functions)` plugin from Serverless Champion @horike37, give him a heart:

Let’s get busy. Install the plugin:

```
npm install --save-dev serverless-step-functions
```

Add the plugin to the `serverless.yml` file:

```
plugins:  - serverless-plugin-stackstorm  - serverless-step-functions
```

The Step Function definition will require my `accountID`. As it is something I want to keep to myself, I add it to `env.yml`, which now looks like this:

```
# ./env.yml# Don't commit to Github :)
```

```
slack:  admin_token: "xoxs-111111111111-..."  organization: "your-team"active_campaign:  url: "https://YOUR-COMPANY.api-us1.com"  api_key: "1234567a9012a12345z12aa2aaa..."private:  accountId: "000000000000"
```

Go back to `serverless.yml` and add the following two blocks:

```
# ./serverless.yml......custom:  private: ${file(env.yml):private}  stage: ${opt:stage, self:provider.stage}  region: ${opt:region, self:provider.region}
```

```
stepFunctions:  stateMachines:    signup:      events:        - http:            path: signup            method: POST            cors: true      definition: ${file(stepfunction.yml)}
```

In the `custom` block, I assigned the `private` object from the `private` key in `env.yml`. I also defined variables for `stage` and `region` so that the values are picked from CLI options, if provided, or default to the current AWS settings.

The `stepFunctions` block is here to define - you have already guessed - StepFunctions. Mine is called "`signup`".

The `events` section here is doing exactly what `events` sections do in function definitions: it configures an API Gateway endpoint for invoking StepFunction from outside of AWS. We'll use it later to call the back-end from a Web form.

The `definition` can be written as YAML right here in `serverless.yml`, but I prefer to include it from a separate file, keeping the logic separate from the configuration. Here it is:

StepFunction definitions are written in [Amazon States Language](https://states-language.net/spec.html). The spec is short, well written and worth a read. Using YAML instead of JSON is a nice perk from the plugin — it reads better and allows comments. But if you want JSON — no problem, help yourself.

* `Resource` refers to Lambda functions by ARN. I used the variables we defined earlier to construct the ARNs matching account ID, region, and stage with the function name: `arn:aws:lambda:${self:custom.region}:${self:custom.private.accountId}:function:${self:service}-${self:custom.stage}-RecordDB`
* `ResultPath` is used to pass data between steps. By default, StepFunctions work on a "need-to-know" basis: the step downstream receives only the output from the step directly upstream. If you think it logical, think again: if only RecordDB receives the workflow input, how will RecordAC and InviteSlack get it? RecordDB may just return "200 OK", not `email`. Changing the code of functions to return their input would make them [inappropriately intimate](https://refactoring.guru/smells/inappropriate-intimacy). The trick is to use `ResultPath` to write the function output under a function-specific key, like `ResultPath: $results.RecordDB`. This preserves initial workflow input in the step output for downstream Lambda steps, while appending the output of each Lambda. Like this:

```
{  "body": {    "name": "Vasili Terkin",    "email": "dmitri.zimine+terkin@gmail.com",    "first_name": "Vasili",    "last_name": "Terkin"  },  "results": {    "RecordDB": {      "statusCode": 200    },    "RecordAC": ...    ...  }}
```

To fully grasp it, read the [“Input and Output” section](https://states-language.net/spec.html#filters) in the spec. Ansd entertain youself with a video from “[AWS Step Functions Tutorial](https://foobar123.com/aws-step-functions-tutorial-76b9f5a7b9c8)” by [Marcia Villalba](https://www.freecodecamp.org/news/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a/undefined).

**PRO TIP:** I made the workflow sequential to demonstrate the data passing trick. It is more proper to run all three steps in parallel: it is faster and more resilient: the failure of one step will not prevent the other function invocations. Go ahead change the StepFunctions to parallel.

That is it. Time to try. Deploy, invoke, check the logs.

You CURL fans know what to do with the new API Gateway endpoint for our StepFunction. If you forgot the endpoint, `sls info` to the rescue. I’ll show off again with [httpie](https://httpie.org):

```
# DON'T COPY! Use YOUR ENDPOINT!
```

```
http POST https://YOUR.ENDPOINT.amazonaws.com/dev/signup \body:='{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}'
```

Ok, `http` or `curl`, either way it returns the StepFunction execution ARN so that we can check on it to see how our StepFunction is being executed. How do we check on it? I’m afraid you gotta open a browser and login to your AWS Console. If you want to use AWS CLI first, fine, don’t say I didn’t show you how:

```
aws stepfunctions describe-execution --execution-arn arn:aws:states:us-east-1:00000000000:execution:SignupStepFunctionsStateMac-seo9CrijATLU:cbeda709-e530-11e7-86d3-49cbe4261318 --output json{    "status": "FAILED",     "startDate": 1513738340.18,     "name": "cbeda709-e530-11e7-86d3-49cbe4261318",     "executionArn": "arn:aws:states:us-east-1:00000000000:execution:SignupStepFunctionsStateMac-seo9CrijATLU:cbeda709-e530-11e7-86d3-49cbe4261318",     "stateMachineArn": "arn:aws:states:us-east-1:00000000000:stateMachine:SignupStepFunctionsStateMac-seo9CrijATLU",     "stopDate": 1513738370.481,     "input": "{\"body\":{\"email\":\"santa@mad.russian.xmas.com\",\"first_name\":\"Santa\",\"last_name\":\"Claus\"}}"}
```

This is the output for an execution that failed because the RecordAC function timed out. Can you infer this from the output? The only valuable info here is `FAILED`. No kidding! I must say AWS don't give StepFunction the love it deserves. Not in CLI. If you think I missed something, check [the CLI docs](http://docs.aws.amazon.com/cli/latest/reference/stepfunctions/index.html), find it and tell me.

The most irritating part is that the CLI doesn’t tell me which step failed. They make me call the logs on every Lambda, one by one. Luckily I only have 3 functions, what if there were more?

Or, open a browser and hop on AWS Console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0xq8ywxkBv-oIe6b-6H9ug.png)

Even there, debugging some Lambda failures, like timeouts, is tricky. StepFunction execution “Exception” report says `"The cause could not be determined because Lambda did not return an error type."`Go to the lambda logs to see what happened there.

There I find the line which I wish I saw in the StepFunction exception:

```
2017-12-20T04:21:44.298Z 4230a73b-e53d-11e7-be6b-bff82b9b3572 Task timed out after 6.00 seconds
```

**PRO TIP:** For debugging, invoke the StepFunction with `sls invoke stepf`: it creates the execution, waits for completion, and prints the output to the terminal. Three AWS CLI commands in one.

```
sls invoke stepf --name signup \--data  '{"body": {"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Clause"}}'
```

Your StepFunction executions may work just fine — we already adjusted the timeouts. I took you on this debugging detour for a taste of StepFunction troubleshooting, admittedly a bit bitter. On the sweet side, once debugged, StepFunctions run reliably like Toyota cars.

As a back-end developer, I am tempted to call it done here. But to make it a   
“complete example” we need one more thing. **The Web front-end.**

Let’s call it a day and save the web part and conclusions for the next and final episode.

[**Episode 4**](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6)**: Adding Web Front-end, Reflection and Summary**

Hope this helped you learn something new, find something interesting, or provoked some good thoughts. Please share your thoughts in the comments here, or tweet me [@dzimine](https://twitter.com/dzimine).

