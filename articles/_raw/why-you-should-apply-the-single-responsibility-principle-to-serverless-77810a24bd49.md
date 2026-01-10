---
title: Why you should apply the single responsibility principle to serverless
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-29T08:30:07.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-apply-the-single-responsibility-principle-to-serverless-77810a24bd49
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lIL-txZJ5iBrg9DDf6-nww.png
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yan Cui

  A fun­ny moment (at 38:50) hap­pened dur­ing Tim Bray’s ses­sion (SRV306) at re:invent
  2017. Tim asked the audi­ence if we should have many single-purposed func­tions,
  or few­er mono­lith­ic func­tions, and there was an equal split in opin...'
---

By Yan Cui

A fun­ny moment (at 38:50) hap­pened dur­ing Tim Bray’s ses­sion ([SRV306](https://www.youtube.com/watch?v=sMaqd5J69Ns)) at re:invent 2017. Tim asked the audi­ence if we should have many single-purposed func­tions, or few­er mono­lith­ic func­tions, and there was an equal split in opinions.

This was a moment that chal­lenged my belief, as I’ve been brought up on the SOLID principles.

* Single Responsibility Principle
* Open/Closed Principle
* Liskov Substitution Principle
* Interface Segregation Principle
* Dependency Inversion Principle

I have, for a long time, believed that following the **Single Responsibility Principle** (SRP) is a no-brainer.

That prompt­ed this clos­er exam­i­na­tion of the argu­ments from both sides.

Full dis­clo­sure: **I am biased in this debate.** If you find flaws in my think­ing, or disagree with my views, please point them out in the com­ments.

By “mono­lith­ic func­tions,” I mean func­tions that have inter­nal branch­ing log­ic. These functions can do one of sev­er­al things based on the invocation event.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lIL-txZJ5iBrg9DDf6-nww.png)

For exam­ple, you can have one func­tion han­dle all the endpoints for an API. The function would per­form a dif­fer­ent action based on the `path` and `method` parameters.

```
module.exports.handler = (event, context, cb) => {   const path = event.path;   const method = event.httpMethod; 
```

```
  if (path === '/user' && method === 'GET') {     .. // get user   } else if (path === '/user' && method === 'DELETE') {     .. // delete user   } else if (path === '/user' && method === 'POST') {     .. // create user   } else if {    .. // other endpoints & methods   }}
```

You can’t ratio­nal­ly rea­son about and com­pare solu­tions with­out first under­stand­ing the prob­lem and what qual­i­ties are most desirable in a solu­tion.

And when I hear com­plaints such as that “hav­ing so many func­tions is hard to man­age,” I won­der what does **man­age** entail?

* Is it to find spe­cif­ic func­tions you’re look­ing for?
* Is it to dis­cov­er what func­tions you have?
* Does this become a prob­lem when you have 10 func­tions or 100 func­tions?
* Does it become a prob­lem only when you have more devel­op­ers work­ing on them than you’re able to keep track of?

Draw­ing from my own expe­ri­ences, the prob­lem has less to do with what func­tions we have. Rather, it’s about discovering what fea­tures and capabilities we pos­sess through these func­tions.

After all, a Lamb­da func­tion, like a Dock­er con­tain­er, is a con­duit to deliv­er some busi­ness fea­ture or capa­bil­i­ty.

You wouldn’t ask _“Do we have a `get-user-by-facebook-id` func­tion?”_ since you would need to know what the func­tion was called with­out even know­ing if the capa­bil­i­ty exists and if it’s cap­tured by a Lamb­da func­tion. Instead, you would prob­a­bly ask, _“Do we have a Lamb­da func­tion that can find a user based on his/her face­book ID?”_

So the real prob­lem is that, giv­en that we have a com­plex sys­tem that con­sists of many fea­tures and capa­bil­i­ties, that is main­tained by many teams of devel­op­ers, **how do we orga­nize these fea­tures and capa­bil­i­ties into Lamb­da func­tions so that it’s opti­mized towards:**

* **dis­cov­er­abil­i­ty**: how do I find out what fea­tures and capa­bil­i­ties exist in our sys­tem?
* **debug­ging**: how do I quick­ly iden­ti­fy and locate the code I need to look at to debug a prob­lem? For example, there are errors in sys­tem X’s logs, where do I find the rel­e­vant code to start debug­ging the sys­tem?
* **scal­ing the team**: how do I min­imize fric­tion and grow the engi­neer­ing team while maintaining the code?

Below are the qual­i­ties that are most impor­tant to me. With this knowl­edge, I can com­pare different approach­es and see which is **best suit­ed** **for me**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OG159w6MLTOQnLL6ei18lw.png)

You might care about dif­fer­ent qual­i­ties. For exam­ple, you might not care about scal­ing the team, but cost is an important consideration for you. Whatever they might be, it’s help­ful to make those design goals explic­it. You should also make sure they’re shared with and under­stood by your team.

### Discoverability

The lack of dis­cov­er­abil­i­ty is not a new prob­lem. Accord­ing to Simon Ward­ley, it’s rather ram­pant in both gov­ern­ment as well as the pri­vate sec­tor. Most organ­i­za­tions lack­ a sys­tem­at­ic way for teams to share and dis­cov­er each other’s work.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xqxvFs3jRv_gc9eePzWf2g.png)
_courtesy of Simon Wardley’s posts on Twitter_

As stated ear­li­er, discovery is about finding out what capa­bil­i­ties are avail­able through your func­tions. Knowing what functions you have is not enough.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6FC_6slSGi3GyQP_5zMLLw.png)
_Ask not what functions you have, ask rather what your functions can do._

An argu­ment I often hear for mono­lith­ic func­tions is that it reduces the number of func­tions, which makes them eas­i­er to man­age.

On the sur­face, this seems to make sense. But the more I think about it, the more the argument appears flawed. The number of func­tions would only be an imped­i­ment IF we try to man­age them by hand rather than using the tools avail­able to us already.

After all, we are able to locate books by their con­tent in a huge phys­i­cal space with tens of thou­sands of books. Using the library analogy, with the tools available to us, we can catalogue our functions and make them easy to search.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P9R8YbGTO_zVQH3Owjbrig.png)

For example, the [Serverless](https://serverless.com/framework/) frame­work enforces a simple naming convention of `{service}-{stage}-{function}`. This simple convention makes it easy to find relat­ed func­tions by pre­fix. If I want to find all the func­tions that are part of a `user` API, I can do that by search­ing for `user-api`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xNLVK6_Jq7MVZd69Yn3NDg.png)

With tags, we can cat­a­logue func­tions across mul­ti­ple dimen­sions. For example, we can catalogue using envi­ron­ment, fea­ture name, event source, author, and so on.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ck-QETFR0AMVV0OgHP2usQ.png)
_By default, the Serverless framework adds the STAGE tag to all of your functions. You can also add your own tags as well, see [documentation](https://serverless.com/framework/docs/providers/aws/guide/functions/#tags" rel="noopener" target="_blank" title=") on how to add tags._

![Image](https://cdn-media-1.freecodecamp.org/images/1*jAtLpmlp2yjQ4cT3JwUKWQ.png)
_The Lambda management console also gives you a handy dropdown list of the available values when you try to search by a tag._

If you have a rough idea of what you’re look­ing for, then the number of func­tions is not an imped­i­ment to your abil­i­ty to dis­cov­er what’s there.

With single-purposed functions, the capa­bil­i­ties of the `user-api` is immediately obvi­ous. I can see from the rel­e­vant func­tions that I have the basic CRUD capa­bil­i­ties, because there are cor­re­spond­ing func­tions for each.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C22Wu2wC8uROThTfwyn7iQ.png)
_I can see what capabilities I have as part of the suite of functions that make up the user-api feature._

With a mono­lith­ic func­tion, how­ev­er, it’s not so straightforward. There is only one function, but what can this function do? I’ll have to either look at the code myself, or con­sult with the author of the func­tion. For me, this makes for poor dis­cov­er­abil­i­ty.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o9wXc2rndRZm2hO0ggevtA.png)

Because of this, I mark the mono­lith­ic approach down on dis­cov­er­abil­i­ty.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bXYf0mExyAPrzHuA3wMz2A.png)

But, having more func­tions means there are more pages for you to scroll through. This can be laborious if you just want to browse and see what functions are there.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Xjwc62Up78CfUs3qwYECg.png)

Although, in my expe­ri­ence, this has never been a problem per se. Thanks to the _Serverless_ framework’s naming convention, all related functions are close together. It’s actually quite nice to see what each group of functions can do, rather than having to guess what goes on inside a monolithic function.

But, it can be a pain to scroll through every­thing when you have **thousands** of func­tions. So, I’m going to penalize sin­gle-purposed func­tions for that.

At that lev­el of com­plex­i­ty, though, packing more capabilities into each function would only make the system more difficult to understand. Say you have a thousand functions, and you know what each does at a glance. Wouldn’t it be simpler if you replace them with a hundred functions, but you can’t tell what each does?

![Image](https://cdn-media-1.freecodecamp.org/images/1*xGGFxDFUXcRHNDjopc23eA.png)

### Debugging

For debug­ging, the rel­e­vant ques­tion is whether having few­er func­tions makes it easier to iden­ti­fy and locate the bug.

In my experience, the path from an error to the relevant function and repo is the same, regard­less of whether the func­tion does one thing or many things.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qV9A5t6nXBmulssjGXzfRw.png)

The difference is how to find the rel­e­vant code inside the repo for the prob­lems you’re inves­ti­gat­ing.

A mono­lith­ic func­tion has more branch­ing logic. So it would take more cog­ni­tive effort to fol­low through to the code that is rel­e­vant to the prob­lem at hand.

For that, I’ll mark mono­lith­ic func­tions down slight­ly. Of course, we’re talking about a minimal difference here, which is why the penalty is also minimal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7BfnhHIlQx0KEqnFIxQa4A.png)

### Scaling

In the early days of microservices, one of the argu­ments for microservices was that it makes scal­ing eas­i­er.

But that’s not the case!

If you know how to scale a sys­tem, then you can scale a mono­lith as eas­i­ly as you can scale a microser­vice.

I say that as some­one who has built mono­lith­ic back­end sys­tems for games that had a mil­lion Dai­ly Active Users (DAU). **Super­cell**, the cre­ator of top gross­ing games like **Clash of Clans** and **Clash Royale**, have well over 100 million DAU. The backend systems for these games are all monoliths, and **Supercell** has no problems scaling these systems.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uXFIo5_szcKnh0kd6m3Vxg.png)

Instead, tech giants such as Ama­zon and Google taught us that microservices make it eas­i­er to scale in a dif­fer­ent dimen­sion — our engi­neer­ing team.

This style of archi­tec­ture allows us to cre­ate bound­aries with­in our sys­tem, around fea­tures and capa­bil­i­ties. It allows our engi­neer­ing teams to scale the com­plex­i­ty of what they build, because they can more easily build on top of the work that oth­ers have cre­at­ed before them.

Take Google’s [Cloud Data­s­tore](https://cloud.google.com/datastore/docs/concepts/overview) as an exam­ple. The engi­neers in that team were able to pro­duce a sophis­ti­cat­ed ser­vice by [build­ing on top of many lay­ers of ser­vices](http://bit.ly/2CQx3C4). Each layer pro­vides a pow­erful abstrac­tions the next layer can leverage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cyUwWcGZkfpw4tzlrS8muQ.png)
_[http://bit.ly/2CQx3C4](http://bit.ly/2CQx3C4" rel="noopener" target="_blank" title=")_

These bound­aries give us a greater divi­sion of labour. Which allows more engi­neers to work on the sys­tem by giv­ing them areas where they can work in rel­a­tive iso­la­tion. This way, they don’t trip over each oth­er with merge con­flicts, inte­gra­tion prob­lems, and so on.

Michael Nygard also wrote a [nice arti­cle](https://bit.ly/coherence-penalty) that explains this ben­e­fit from another angle: that these bound­aries and iso­la­tion helps us reduce the over­head of shar­ing men­tal mod­els.

> “If you have a high coher­ence penal­ty and too many peo­ple, then the team as a whole moves slow­er… It’s about **reduc­ing** **the over­head of shar­ing men­tal mod­els**.”

> - Michael Nygard

Hav­ing lots of sin­gle-pur­posed func­tions is per­haps the pin­na­cle of that divi­sion of tasks. You lose that division a little when you move to mono­lith­ic func­tions. Although in prac­tice, you prob­a­bly won’t have so many devel­op­ers work­ing on the same project that you feel the pain.

Restrict­ing a func­tion to doing one thing also helps lim­it how complex a func­tion can become. To make some­thing more complex, you would com­pose these sim­ple func­tions togeth­er via oth­er means, such as with AWS **Step Functions.**

I’ll mark mono­lith­ic func­tions down for los­ing some divi­sion of labour, and for rais­ing the com­plex­i­ty ceil­ing of a func­tion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GNu9RlaxpUhdyTRwyLzozQ.png)

### Conclusion

**Based on the** **cri­te­ria that are** **impor­tant to me**, hav­ing many sin­gle-pur­posed func­tions is the bet­ter way to go. But I do not see this as a hard and fast rule.

Like every­one else, I come pre­loaded with a set of pre­dis­po­si­tions and bias­es formed from my expe­ri­ences, which like­ly do not exactly reflect yours. I’m not ask­ing you to agree with me. Though I do hope you appre­ci­ate the process of working out what’s important to you so you can go about find­ing the right approach for you.

But what about **cold starts**? Wouldn’t monolithic functions help you reduce the number of cold starts?

The short answer is no, they don’t help you with cold starts in any meaningful way. It’s also the wrong place to optimize for cold starts. If you’re interested in the longer version of this answer, then please read my other post [here](https://theburningmonk.com/2018/02/aws-lambda-monolithic-functions-wont-help-you-with-cold-starts/).

And lastly, having smaller surface areas with single-purposed functions reduces the attack surface. You can give each function the exact permission it needs and nothing more. This is an important, but often underappreciated advantage of single-purposed functions.

