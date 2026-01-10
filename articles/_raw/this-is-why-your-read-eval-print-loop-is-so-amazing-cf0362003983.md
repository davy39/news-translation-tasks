---
title: This is why your read-eval-print-loop is so amazing
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-16T17:49:27.000Z'
originalURL: https://freecodecamp.org/news/this-is-why-your-read-eval-print-loop-is-so-amazing-cf0362003983
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wOeV-wURvl_DeuBPreGGcg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: psychology
  slug: psychology
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By IObert

  One of the things that makes the tech community so special is that we are always
  looking for ways to work more efficiently. Everyone has their favorite set of tools
  which makes them run better. As a professional UI dev, the Chrome DevTools ...'
---

By IObert

One of the things that makes the tech community so special is that we are always looking for ways to work more efficiently. Everyone has their favorite set of tools which makes them run better. As a professional UI dev, the Chrome DevTools and the Node.js read-eval-print-loop (REPL) became my favorite tools early on. I noticed that they enabled me to work more efficiently and allowed me to learn new things more quickly.

![Image](https://cdn-media-1.freecodecamp.org/images/QyirbrnboR992KJY6hdvrkmnqTwS4FGnVuja)
_The three phases of the REPL process_

This actually made me curious to investigate why this tool is so useful. I could easily find plenty of blog posts which explained **what** REPLs are and **how** to use them, for example [here](https://clojure.org/guides/repl/introduction) or [here](http://blogish.nomistech.com/repl-based-development/). But this post here is dedicated to the **why** (as in why are REPLs such a great tool for developers).

> “The number one reason that schools move away from Java as a teaching language is the high bars to Hello-world programs.”

> — Stuart Halloway

### What is a REPL?

REPL stands for _read-evaluate-print-loop_ and this is basically all there is to it.

Your application runtime is in a specific state and the REPL helps you to interact with it. The REPL will _read_ and _evaluate_ the commands and _print_ the result and then go back to the start to read your next input. The _evaluate_ step might change your runtime. This process can be seen as an interview with your application to query its current state.

In other words, the REPL makes your **runtime more tangible** and allows you to **test hypotheses** about it.

[According to Stuart Halloway,](https://vimeo.com/223309989) the absence of a REPL in Java is the most significant reason why schools started to move to other languages to teach programming. Some people even use the REPL to [write better unit tests](https://danlebrero.com/2018/11/26/repl-driven-development-immediate-feedback-for-you-backend/).

### Do I already use a REPL (-like tool) today?

This basic explanation might have reminded you of some tools which you use every day. If you know and use one of the following tools, the answer is “yes”:

* The dev tools of your browser (like [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/))
* Your terminal/shell
* Jupyter Notebooks
* The REPL process in Clojure
* Repl.it, jsfiddle.net, or jsbin.com
* Online regex validators

### Why is the REPL so helpful?

This question kept me up at night because I didn’t understand what makes us inefficient in the first place. I started to research some common psychological effects and tried to link them to my daily interactions with the REPL. Here are my top three hypotheses:

#### Being in the flow

> Flow is the mental state of operation in which a person performing an activity is fully immersed in a feeling of energized focus, full involvement, and enjoyment in the process of the activity. ([source](https://en.wikipedia.org/wiki/Flow_(psychology)))

I think all of us are familiar with this state, it makes us extremely productive and [time flies](https://www.verywellmind.com/what-is-flow-2794768) basically. Unfortunately, it’s fairly easy to “lose” the flow, for example when you get interrupted or when you have to wait for some period. I learned this can happen very fast: [Researchers found out](https://psychology.stackexchange.com/questions/1664/what-is-the-threshold-where-actions-are-perceived-as-instant) that one second is about the limit for the user’s flow of thought to stay uninterrupted.

The REPL doesn’t need to compile or deploy your code. This leads to a very short response time (<100ms). Thus, you are able to test your hypotheses without losing the flow.

![Image](https://cdn-media-1.freecodecamp.org/images/89s3maIoDGdbPFnt8JKJSGA0foZrdSklK-PT)
_This is what we want to avoid (source: [XKCD](https://xkcd.com/303/" rel="noopener" target="_blank" title="))_

#### Positive Reinforcement

> Positive reinforcement involves the addition of a reinforcing stimulus following a behavior that makes it more likely that the behavior will occur again. ([source](https://www.verywellmind.com/what-is-positive-reinforcement-2795412))

This is the effect that appeals the most to me. Your brain learns to favor certain actions when they were rewarded in the past. This reward could be a bonus from your boss after an outstanding month or a simple “Great job!” from your skiing instructor.

Every time your REPL experiment succeeds and you solved a puzzle/problem, your brain feels rewarded as well! This also takes place when you code in a common IDE. But the REPL responds way faster and allows you to iterate more often. So, more experiments lead to more reinforcement. This effect makes you use the REPL more often and keeps your eye on the ball (instead of distracting yourself by checking for emails).

#### Digital Amnesia

> The tendency to forget information that can be found readily online by using Internet search engines. ([source](https://en.wikipedia.org/wiki/Google_effect))

I have to admit, I often mix Java, Python and JavaScript syntax, because that information can be found all over the internet. I would ask myself “Do I need to use _add()_, _append()_ or _push()_ to add a new element to an array in JavaScript?”. Thus for me, an example of this effect is recalling method names of API and language references.

In the REPL, I can see the available functions immediately with autocomplete:

![Image](https://cdn-media-1.freecodecamp.org/images/zjpzMLtOwLZHgDHMmBRremTlLJ-Hv4VDHJON)
_The code-completion feature of the Node.js REPL_

The great thing is, this works beyond the standard objects of programming languages. This works **for all frameworks and modules**, which makes the REPL more mighty than your IDE! There’s no need to compare the version numbers of modules and API references anymore:

> “Truth can only be found in one place: the code.”

> – Robert C. Martin, Clean Code

![Image](https://cdn-media-1.freecodecamp.org/images/QAfs4XNxxCuoF6IEEHVxi2Nqs6td8SY42BJ2)
_source: [arungupta.me](http://blog.arungupta.me/jdk9-repl-getting-started/" rel="noopener" target="_blank" title=")_

I hope this article helped you to understand how your brain works and how the REPL can help you to be more productive.

I’m curious to see if you agree with my hypotheses or if you know more tools to be a more efficient developer.

Update 2/13/2019:

I’ve also written [a blog post](https://blogs.sap.com/2019/02/04/cloudfoundryfun-upgrade-cloud-foundry-with-a-new-repl-feature/) about the usage of REPLs in Cloud Foundry Environments.

Check out [this video](https://www.twitch.tv/videos/379997882) by [DJ Adams](https://people.sap.com/dj.adams.sap) if you’d like to see the REPL in action :)

