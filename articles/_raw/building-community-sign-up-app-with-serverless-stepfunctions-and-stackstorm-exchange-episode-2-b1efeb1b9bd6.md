---
title: Building community sign-up app with Serverless, StepFunctions and StackStorm
  Exchange — Episode  2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-19T19:41:18.000Z'
originalURL: https://freecodecamp.org/news/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-0KcbVF9M6t_UvLpObeNYw.jpeg
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: lambda
  slug: lambda
- name: Python
  slug: python
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Dmitri Zimine

  Build a real-world serverless application on AWS with Serverless framework and ready-to-use
  functions from StackStorm Exchange open-source catalog.

  Episode One | Episode Two | Episode Three | Episode Four

  In this second episode, I’ll...'
---

By Dmitri Zimine

Build a real-world serverless application on AWS with [Serverless framework](https://serverless.com/framework/) and ready-to-use functions from [StackStorm Exchange](https://exchange.stackstorm.org) open-source catalog.

[Episode One](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) | Episode Two | [Episode Three](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a) | [Episode Four](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-7c5f0e93dd6)

In this second episode, I’ll add two more actions: create a contact in ActiveCampaign, and record a user in Dynamo DB. The full code for this episode is on Github at [2-add-more-actions branch](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/2-add-more-actions).

### Add more actions

To continue to the next step, you’ll need an [ActiveCampaign](https://www.activecampaign.com) account. Fear not: it takes 2 minutes — I just tried — they didn’t ask me for a credit card or anything stupid. Just email. Once in, go to “My Settings”, and select “Developer”.

Note the `URL` and `Key` fields in the "API access" section. Add them into `env.yml` like this:

```
# Copy to env.yml and replace with your values.# Don't commit to Github :)slack:  admin_token: "xoxs-111111111111-111111111111-..."  organization: "your-team"active_campaign:  url: "https://YOUR-COMPANY.api-us1.com"  api_key: "1234567a9012a12345z12aa2..."
```

**PRO TIP:** If you’re not in the mood for Active Campaign, or any sign-ups, just mock up the API endpoint with something like [Mocky](https://www.mocky.io/) or [mockable.io](https://www.mocky.io/)and adjust the examples accordingly. For bonus points, create another serverless function with API Gateway endpoint in your `serverless.yml` and use it to mock the ActiveCampaign API call.

Now I am ready to add an [Active Campaign](https://exchange.stackstorm.org/#activecampaign) lambda function. Same routine as in [Episode One](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419): start with finding a new action in a pack with `sls stackstorm info --pack activecampaign` (hint: the action you're looking is `contact_sync` which adds and updates a contact). Inspect the action with `sls stackstorm info --action activecampaign.contact_sync`:

Bunch of parameters, but besides the config, only `email` is required. I also want to use `first_name` and `last_name`. The function definition in `serverless.yml` will look like this:

```
RecordAC:    timeout: 10    memorySize: 128    stackstorm:      action: activecampaign.contact_add      input:        email: "{{ input.body.email }}"        first_name: "{{ input.body.first_name }}"        last_name: "{{ input.body.last_name }}"      config: ${file(env.yml):activecampaign}
```

I had to bump up the timeout as the ActiveCampaign API is taking longer than Lambda's default 6 seconds during Christmas season. But I can reclaim invocation cost by lowering memory use from default 512Mb. This time I don't bother to expose it to AWS API Gateway - we can conveniently test it with `sls`.

The function is ready to fly to AWS. We could do it at once with `sls deploy`but let's take it slow again and repeat the deployment steps just like in [episode 1](https://medium.com/@dzimine/tutorial-building-a-community-on-boarding-app-with-serverless-stepfunctions-and-stackstorm-b2f7cf2cc419) of this tutorial to engrave the workflow in your mind:

1. Build and package the bundle:

```
sls package
```

2. Test locally (note I’m using `--passthrough` to only test transformations, remove it to make an actual call):

```
sls  stackstorm docker run --function RecordAC \--passthrough \--verbose --data '{"body":{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}}'
```

3. Deploy to AWS:

```
sls deploy
```

4. Test on AWS with `sls invoke`:

```
sls invoke --function RecordAC --logs \ --data '{"body":{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}}'
```

5. Check the logs:

```
sls logs --function  RecordAC
```

and I checked, it works: Santa Claus appeared in ActiveCampaign’s contact list. How do I know it’s our Lambda? Because I no longer believe Santa is real enough to subscribe to community without our little Lambda function.

**PRO TIP:** If you hit a bug or want a feature in a pack you are using from [StackStorm Exchange](https://exchagne.stackstorm.org), you can fix it on the spot. Packs are cloned under `./~st2/packs`. Find your action there, modify the code, and use a local run to debug and validate.   
Big bonus for pushing fixes back to the Exchange: each pack is already a git clone that makes it naturally easy to contribute back to the community.

Let’s add the final action, RecordDB, that writes contact info into a DynamoDB table. I could have used the `aws.dynamodb_put_item` action from the [AWS pack on StackStorm Exchange](https://exchange.stackstorm.org/#aws) - the pack is heavily used and well maintained. But I decided to make it a native Lambda: it's just 30 lines of code, with no extra Python dependencies, since the Boto library is already in the AWS Lambda environment.

The function’s code goes into `./record_db/handler.py`:

The final `serverless.yml` with all three actions now looks like this:

Wow! The file doubled. The function itself is just 2 lines (35:36), but quite a few interesting additions took place. Let’s review them:

1. Line 9 — Table name generated to avoid collisions between regions and environments.
2. Lines 10:13 — IAM Role created to give the function access to the DynamoDB table.
3. Line 39:56 — AWS CloudFormation template defining the table.

The last point brings up an important observation: [Serverless framework](https://www.freecodecamp.org/news/building-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-2-b1efeb1b9bd6/(https://serverless.com/framework)) simplifies mainly the FaaS part of serverless. But because servereless is more than FaaS, you’ll find yourself writing quite a lot of CloudFormation to provision other services. Serverless framework leaves space for provider specific resources. To be seriously serverless on AWS, master CloudFormation. Looking for “provider-agnostic serverless”? Double-check your assumptions.

Also, I moved `memorySize` and `timeout` to apply to all functions (lines 6:7). And the API Gateway endpoint is gone from the InviteSlack function: it served the demonstration role in the first episode, but now we've learned to test Lambda functions directly. We'll return to API Gateway later to invoke the final StepFunction end-to-end workflow.

Let’s get the RecordDB function up to the sky and running.   
Deploy, invoke, logs. Rinse repeat.

```
# Deploysls deploy ...
```

```
# Invokesls invoke --function RecordDB --logs --data '{"body":{"email":"santa@mad.russian.xmas.com", "first_name":"Santa", "last_name": "Claus"}}'...
```

```
# Check logs.sls logs --function RecordDB.
```

Now all three actions are here, waiting to be wired together into a final workflow with a StepFunction. But I’m just reminded not to be Mr. Scrooge: it’s the holiday season, let’s take it easy and put it off to the next episode. Until then, keep the spirits high!

The complete code example for this episode is on Github at [2-add-more-actions](https://github.com/dzimine/slack-signup-serverless-stormless/tree/DZ/2-add-more-actions) branch.

[**Episode 3**](https://medium.com/@dzimine/building-a-community-sign-up-app-with-serverless-stepfunctions-and-stackstorm-exchange-episode-6efb9c102b0a)**: Wiring the actions with a StepFunction**

Hope this helped you learn something new, find something interesting, or provoked some good thoughts. Please share your thoughts in the comments here, or tweet me [@dzimine](https://twitter.com/dzimine).

