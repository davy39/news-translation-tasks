---
title: 'AWS step functions: how to implement semaphores for state machines'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-21T20:06:11.000Z'
originalURL: https://freecodecamp.org/news/aws-step-functions-how-to-implement-semaphores-for-state-machines-8075650ceb86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sjet9qSO4O8fX2-FXvxflw.jpeg
tags:
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yan Cui

  Here at DAZN, we are migrat­ing from our lega­cy plat­form into the brave new world
  of microfron­tends and microser­vices. Along the way, we also dis­cov­ered the delights
  that AWS Step Func­tions have to offer. For exam­ple…


  flex­i­ble e...'
---

By Yan Cui

Here at [DAZN](https://engineering.dazn.com/), we are migrat­ing from our lega­cy plat­form into the brave new world of [microfron­tends](https://micro-frontends.org/) and microser­vices. Along the way, we also dis­cov­ered the delights that AWS Step Func­tions have to offer. For exam­ple…

* flex­i­ble error han­dling and retry
* the under­stat­ed abil­i­ty to wait between tasks
* the abil­i­ty to mix auto­mat­ed steps with [activ­i­ties](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html) that require human intervention

In some cas­es, we need to con­trol the num­ber of con­cur­rent state machine exe­cu­tions that can access a shared resource. This might be a busi­ness require­ment. Or it could be due to scal­a­bil­i­ty con­cerns for the shared resource. It might also be a result of the design of our state machine which makes it dif­fi­cult to par­al­lelise.

We came up with a few solu­tions that fall into two gen­er­al cat­e­gories:

1. Con­trol the num­ber of exe­cu­tions that you can start
2. Allow con­cur­rent exe­cu­tions to start, but block an exe­cu­tion from enter­ing the crit­i­cal path until it’s able to acquire a [sem­a­phore](https://en.wikipedia.org/wiki/Semaphore_%28programming%29) (that is, a sig­nal to proceed)

### Control the number of concurrent executions

You can con­trol the MAX num­ber of con­cur­rent exe­cu­tions by intro­duc­ing an SQS queue. A Cloud­Watch sched­ule will trig­ger a Lamb­da func­tion to:

1. check how many con­cur­rent exe­cu­tions there are
2. if there are N exe­cu­tions, then we can start MAX-N exe­cu­tions
3. poll SQS for MAX-N mes­sages, and start a new exe­cu­tion for each

![Image](https://cdn-media-1.freecodecamp.org/images/HEltXnpPctxNoQlmZPgqWmqFKAExcaRJMBst)

We’re not using the new [SQS trig­ger for Lamb­da](https://aws.amazon.com/blogs/aws/aws-lambda-adds-amazon-simple-queue-service-to-supported-event-sources/) here, because the pur­pose is to **slow down** the cre­ation of new exe­cu­tions. Where­as the SQS trig­ger would push tasks to our Lamb­da func­tion eager­ly.

Also, you should use a FIFO queue so that tasks are processed in the same order they’re added to the queue.

### Block execution using semaphores

You can use the [Lis­tEx­e­cu­tions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html) API to find out how many exe­cu­tions are in the RUNNING state. You can then sort them by [start­Date](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ExecutionListItem.html#StepFunctions-Type-ExecutionListItem-startDate) and only allow the oldest exe­cu­tions to tran­si­tion to states that access the shared resource.

![Image](https://cdn-media-1.freecodecamp.org/images/fJaX03lK7RvYFecLc9CeJn0hZ5dj3Kpt4BMc)

Take the fol­low­ing state machine for instance.

![Image](https://cdn-media-1.freecodecamp.org/images/35CfjuZqHsXqiEx5fXvkAeYBov9zvyDMA3ol)

The **Only­One­Shall­RunA­tOne­Time** state invokes the `one-shall-pass` Lambda func­tion and returns a `proceed` flag. The **Shall Pass?** state then branch­es the flow of this exe­cu­tion based on the `proceed` flag.

```
OnlyOneShallRunAtOneTime:  Type: Task  Resource: arn:aws:lambda:us-east-1:xxx:function:one-shall-pass  Next: Shall Pass?Shall Pass?:  Type: Choice  Choices:    - Variable: $.proceed  # check if this execution should proceed                      BooleanEquals: true      Next: SetWriteThroughputDeltaForScaleUp  Default: WaitToProceed   # otherwise wait and try again later          WaitToProceed:  Type: Wait  Seconds: 60  Next: OnlyOneShallRunAtOneTime
```

The tricky thing here is how to asso­ciate the Lamb­da invo­ca­tion with the corre­spond­ing Step Func­tion exe­cu­tion. Unfor­tu­nate­ly, Step Func­tions do not pass the exe­cu­tion ARN to the Lamb­da func­tion. Instead, we have to pass the exe­cu­tion name as part of the input when we start the exe­cu­tion.

```
const name = uuid().replace(/-/g, '_')const input = JSON.stringify({ name, bucketName, fileName, mode })   const req = { stateMachineArn, name, input }const resp = await SFN.startExecution(req).promise()
```

When the `one_shall_pass` func­tion runs, it can use the exe­cu­tion `name` from the input. It’s then able to match the invo­ca­tion against the exe­cu­tions returned by [Lis­tEx­e­cu­tions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html).

In this par­tic­u­lar case, only the oldest exe­cu­tion can pro­ceed. All oth­er executions would tran­si­tion to the **Wait­To­Pro­ceed** state.

```
module.exports.handler = async (input, context) => {  const executions = await listRunningExecutions()  Log.info(`found ${executions.length} RUNNING executions`)
```

```
const oldest = _.sortBy(executions, x =&gt; x.startDate.getTime())[0]       Log.info(`the oldest execution is [${oldest.name}]`)
```

```
if (oldest.name === input.name) {    return { ...input, proceed: true }  } else {    return { ...input, proceed: false }  }}
```

### Compare the approaches

Let’s com­pare the two approach­es against the fol­low­ing cri­te­ria:

* **Scal­a­bil­i­ty**. How well does the approach cope as the num­ber of con­cur­rent exe­cu­tions goes up?
* **Sim­plic­i­ty**. How many mov­ing parts does the approach add?
* **Cost**. How much extra cost does the approach add?

#### Scalability

Approach 2 (block­ing exe­cu­tions) has two prob­lems when you have a large num­ber of con­cur­rent exe­cu­tions.

First, you can hit the region­al throt­tling lim­it on the `ListExecutions` API call.

![Image](https://cdn-media-1.freecodecamp.org/images/WeuQ0JcWEx5FoUQlIkfuj1pYh3fcHkfXn9x2)

Sec­ond, if you have con­fig­ured time­out on your state machine (and you should!) then they can also time­out. This cre­ates back­pres­sure on the sys­tem.

![Image](https://cdn-media-1.freecodecamp.org/images/c69Jh5yX3TpcLhmDBfHfwzmUn8d8nMsx1k56)

Approach 1 (with SQS) is far more scal­able by com­par­i­son. Queued tasks are not start­ed until they are allowed to start, so no back­pres­sure. Only the cron Lamb­da func­tion needs to list exe­cu­tions, so you’re also unlike­ly to reach API lim­its.

#### Simplicity

Approach 1 intro­duces new pieces to the infra­struc­ture — SQS, Cloud­Watch sched­ule, and Lamb­da. Also, it forces the pro­duc­ers to change as well.

With approach 2, a new Lamb­da func­tion is need­ed for the addi­tion­al step, but it’s part of the state machine.

#### Cost

Approach 1 intro­duces min­i­mal base­line cost even when there are no executions. How­ev­er, we are talk­ing about cents here…

Approach 2 intro­duces addi­tion­al state tran­si­tions, which is around $25 per mil­lion. See the [Step Func­tions pric­ing](https://aws.amazon.com/step-functions/pricing/) page for more details. Since each execution will incur 3 tran­si­tions per minute while it’s blocked, the cost of these tran­si­tions can pile up quick­ly.

### Conclusions

Giv­en the two approach­es we con­sid­ered here, using SQS is by far the more scal­able. It is also more cost effec­tive as the num­ber of con­cur­rent exe­cu­tions goes up.

But, you need to man­age addi­tion­al infra­struc­ture and force upstream sys­tems to change. This can impact oth­er teams, and ulti­mate­ly affects your abil­i­ty to deliv­er on time.

If you do not expect a high num­ber of exe­cu­tions, then you might be bet­ter off going with the sec­ond approach.

