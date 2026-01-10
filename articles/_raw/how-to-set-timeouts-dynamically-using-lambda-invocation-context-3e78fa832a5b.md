---
title: How to set timeouts dynamically using Lambda invocation context
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-08T08:30:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-timeouts-dynamically-using-lambda-invocation-context-3e78fa832a5b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XKE_zsrkxUG3yf5qkbGPzA.png
tags:
- name: aws lambda
  slug: aws-lambda
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Yan Cui

  With API Gate­way and Lamb­da, you’re forced to use short time­outs on the serv­er-side:


  API Gate­way has a 29s max time­out on all inte­gra­tion points

  The Server­less frame­work uses a default of 6s for AWS Lamb­da func­tions


  How­ev­er...'
---

By Yan Cui

With API Gate­way and Lamb­da, you’re forced to use short time­outs on the serv­er-side:

* **API Gate­way has a 29s max time­out** on all inte­gra­tion points
* The [Server­less](https://serverless.com/framework/) frame­work uses a default of **6s** for AWS Lamb­da func­tions

How­ev­er, you have lim­it­ed _influ­ence_ over a Lamb­da function’s cold start time. And you have no con­trol over how much over­head API Gate­way adds. So the actu­al laten­cy you’d expe­ri­ence from a call­ing func­tion is far less pre­dictable than you might think.

![Image](https://cdn-media-1.freecodecamp.org/images/WhmOKbUJElluVZAAQUgnFi6N2vUIiQcXZgwo)

![Image](https://cdn-media-1.freecodecamp.org/images/WR1ntsEd4TwiicN1wDWWAuUAEokbPNZFeuIu)
_[https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/api-gateway-metrics-dimensions.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/api-gateway-metrics-dimensions.html" rel="noopener" target="_blank" title=")_

We don’t want a slow HTTP respons­e to cause the call­ing func­tion to time­out. This has a negative impact on the user experience. Instead, we should stop wait­ing for a response before the call­ing func­tion times out.

> “The goal of the time­out strat­e­gy is to give HTTP requests the **best chance to suc­ceed**, pro­vid­ed that doing so does not cause the call­ing func­tion itself to err.”

> - Me

Most of the time, I see folks use fixed time­out val­ues — but it’s often tricky to decide:

* Too short, and you won’t give the request the _best chance to suc­ceed._ For example, there’s 5s left in the invo­ca­tion, but the time­out is set to 3s.
* Too long, and you run the risk of let­ting the request time­out the call­ing func­tion. For example, there’s 5s left in the invo­ca­tion but the time­out is set to 6s.

Things are fur­ther com­pli­cat­ed by the fact that we often per­form more than one HTTP request dur­ing a func­tion invo­ca­tion. For example,

1. _read from DynamoDB_
2. perform business logic on the data
3. _save the update to DynamoDB_
4. _publish an event to Kinesis_

Let’s look at two com­mon approach­es for pick­ing time­out val­ues, and where they fall short.

![Image](https://cdn-media-1.freecodecamp.org/images/h2OAW3TBhEJGGYIwdZUhXZMIinuP8kLhvtzA)
_requests are not giv­en the best chance to suc­ceed_

![Image](https://cdn-media-1.freecodecamp.org/images/gOowm9GXISJ1H-jb-wutX6ocGILgytVHD0xl)
_requests are allowed too much time to exe­cute and caused the func­tion to time­out._

Instead of following these approaches, I propose we should **set the request time­out based on the amount of invo­ca­tion time left**. We should also reserve some time to per­form **recovery steps** in the event of failures.

You can find out how much time is left in the cur­rent invo­ca­tion through the `context` object.

![Image](https://cdn-media-1.freecodecamp.org/images/D7EMF5dKAZdN8yTbch2tm0nBKSFjB9SCSrfg)
_[https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html" rel="noopener" target="_blank" title=")_

For exam­ple, if a function’s `timeout` is 6s, and we’re 1s into the invocation. If we reserve 500ms for recov­ery, then that leaves us with 4.5s to wait for a HTTP response.

With this approach, we get the best of both worlds:

* Allow requests the best chance to suc­ceed based on the actu­al amount of invo­ca­tion time we have left

![Image](https://cdn-media-1.freecodecamp.org/images/e7OC4y4Hoe7MhYCARqwejIPGpU4Y5upJXOll)
_requests are giv­en the best chance to suc­ceed, with­out being restrict­ed by an arbi­trar­i­ly deter­mined time­out._

* Pre­vent slow respons­es from tim­ing out the func­tion, which gives us a window of oppor­tu­ni­ty to per­form recov­ery actions.

![Image](https://cdn-media-1.freecodecamp.org/images/FmnGFJFXltV07ajBvuXihhZ42zaOGW44G-Mo)
_slow respons­es are timed out before they cause the call­ing func­tion to time out_

But what are you going to do _after_ you time out these requests? Aren’t you still going to have to respond with a HTTP error, since you couldn’t fin­ish what­ev­er oper­a­tions you need­ed to per­form?

At the min­i­mum, the recov­ery actions should include:

* Log the timeout incident with as much context as possible. For example, request target, timeout value, [correlation IDs](https://theburningmonk.com/2017/09/capture-and-forward-correlation-ids-through-different-lambda-event-sources/), and the request object.
* Track cus­tom met­rics for `serviceX.timedout` so it can be mon­i­tored and the team can be alert­ed if the sit­u­a­tion esca­lates
* Return an appli­ca­tion error code and the original request ID in the response body. The client app can then dis­play a user-friend­ly mes­sage like `_“Oops, looks like this fea­ture is cur­rent­ly unavail­able, please try again lat­er. If this is urgent, please con­tact us at xxx@domain.com and quote the request ID f19a7dca. Thank you for your coop­er­a­tion :-)”_`

```
{   "errorCode": 10021,   "requestId": "f19a7dca",   "message": "service X timed out" }
```

In _some_ _cas­es_, you can also recov­er even more grace­ful­ly using fall­backs.

Netflix’s [Hys­trix](https://github.com/Netflix/Hystrix) library sup­ports sev­er­al flavors of fall­backs via the _Com­mand_ pat­tern it employs heav­i­ly. I recommend reading its [wiki page](https://github.com/Netflix/Hystrix/wiki/How-To-Use), as there is tons of use­ful infor­ma­tion and ideas there.

![Image](https://cdn-media-1.freecodecamp.org/images/d7dnsp1JyZBHfqvZaPzRgaRSM-Xz2lKIPUMN)

Every _Hystrix_ com­mand lets you spec­i­fy a fall­back action.

![Image](https://cdn-media-1.freecodecamp.org/images/zYiuzrRGym4ZIHPv9Nu6idnxTlHRY8FIF2cR)

You can also chain the fall­back togeth­er by chain­ing com­mands via their respec­tive `getFallback` meth­ods.

![Image](https://cdn-media-1.freecodecamp.org/images/lSERDe6Z69uzepFiE3jkQvCS8z2K-JgTrZzs)

For exam­ple,

1. exe­cute a DynamoDB read inside `CommandA`
2. In the `getFallback` method, exe­cute `CommandB` which would return a pre­vi­ous­ly cached response if avail­able
3. If there is no cached response, then `CommandB` would fail and trig­ger its own `getFallback` method
4. Exe­cute `CommandC`, which returns a stubbed response

You should check out _Hys­trix_ if you haven’t already. Most of the pat­terns that are baked into _Hys­trix_ can be eas­i­ly adopt­ed in our server­less appli­ca­tions to help make them more resilient to fail­ures.

