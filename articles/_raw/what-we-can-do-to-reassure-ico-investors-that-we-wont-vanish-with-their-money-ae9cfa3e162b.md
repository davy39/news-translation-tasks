---
title: What we can do to reassure ICO investors that we won’t vanish with their money
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-08T10:20:16.000Z'
originalURL: https://freecodecamp.org/news/what-we-can-do-to-reassure-ico-investors-that-we-wont-vanish-with-their-money-ae9cfa3e162b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yY21X2rr17WAE_zs35u3pg.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: ICO
  slug: ico
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pablo Ruiz

  What a great time to be in the tech industry! It’s never been easier to raise funds
  for a new startup. Well, maybe during the dot-com era, but most people of my generation
  — those born after 1985 — were too young at that time to build a...'
---

By Pablo Ruiz

What a great time to be in the tech industry! It’s never been easier to raise funds for a new startup. Well, maybe during the dot-com era, but most people of my generation — those born after 1985 — were too young at that time to build a company.

**For those of us Millennials, it’s never been easier to raise funds for a new startup!**

2017 has seen the rise of ICOs ([Initial Coin Offerings](https://hackernoon.com/twenty-years-and-three-months-to-create-an-overnight-sensation-cf7190df871b)). ICOs are a novel way for teams to raise funding in exchange for tokens that are (or will be) used to interact with the company’s product. Through the sale of tokens, startup teams can get the funding they need to further develop their products without having to give up control to investors. Instead, they get the funding by selling digital tokens that at some point should be useful within their platform, hopefully holding — or even increasing — their value.

The early days of ICOs were a success, and in most cases, they raised millions of dollars each in a matter of days or even hours. As these results started to make headlines, more people started jumping on the ICO bandwagon. It didn’t matter what the product was, or even if it made sense to build those products using Blockchain technology.

[Eric Risley](https://www.freecodecamp.org/news/what-we-can-do-to-reassure-ico-investors-that-we-wont-vanish-with-their-money-ae9cfa3e162b/undefined)’s article, [Tale of Two World](https://hackernoon.com/most-icos-fail-tale-of-two-worlds-d1ab7625ff66)s, shows that ICOs are failing to raise the funds they intended to raise as the months go by.

The chart he published goes from June to mid-September 2017, but given how exponentially this trend has evolved, I bet it has only gotten worse.

ICOs were bound to start missing their targets. There’s currently an over-saturation of ICOs, as can be evidenced by looking at the popular listing sites. Many of them spring out every day. And many of them are garbage or outright scams.

I’m not going to go over what makes an ICO potentially dangerous to invest in, as it is not the point of this article. But there are many telltale signs, such as ridiculous caps, non-existent MVPs, shady founders and unknown advisors. It is worrisome — but interesting to analyze — given how many of them still do manage to raise some money despite all the red flags.

Alongside these failed ICOs that miss their targets, there’s a new problem starting to manifest in this industry. Some ICOs successfully raise the funds, but either fail to fulfill their promise or directly vanish with the funds they raised.

![Image](https://cdn-media-1.freecodecamp.org/images/-Q-vxQplymMoEO5fmUh6PLXJzDSeDnMj3yy8)
_Photo by [Unsplash](https://unsplash.com/photos/ZbZ5KP7D9z8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Patrick Tomasso</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

[The most recent case is Confido.](https://www.cnbc.com/2017/11/21/confido-ico-exit-scam-founders-run-away-with-375k.html) In November 2017 they managed to raise almost $400,000 through an Initial Coin Offering and simply vanished with the money. They took down the site, deleted their profiles from social networks, and ran away with the funds they had collected. ? ? ?

**If the number of scams and failed ICOs keeps increasing, it’s going to take a toll on the Ethereum community and make it harder for honest founders to access this method of funding.**

So, what can we do, as honest founders, to reassure potential contributors/investors of our good intentions?

Currently, most ICOs have outrageous hard caps — typically 10 or more times the funds that any company would need to build a tech product. We are raising tens of millions of dollars to launch products that could be accomplished with a few hundred thousands.

I know, ICOs might soon be dead or the bar might be raised so high that it’s impossible for smaller teams to raise any funding at all. So, better to seize the moment and ask for as much as you can, right? It’s not like you are giving more control of your company by asking for 10 times the money you need.

Well, I firmly believe that at some point we won’t be able to raise funds as easily as we can now. **We will be asked for more accountability.** The market will accommodate, and we will need to up our game in order to be able to do successful ICOs. One of the first things I believe we will be asked to do is to restrict our access to the funds to prevent hit-and-run Confido-like outcomes.

You want to raise 100 million dollars? Perfect, go ahead. But you will only get $500k right after the ICO.

Need more? Show us some progress.

Haven’t shown some considerable progress for months? We’ll take what’s left of our money back.

### Building a Milestone-based Vault for ICOs

![Image](https://cdn-media-1.freecodecamp.org/images/o8-nUBaQEfC7gEtji41CXgZqRq9dtfO3K4dY)
_Photo by [Unsplash](https://unsplash.com/photos/FqaybX9ZiOU?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">James Sutton</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

[The complete, fully-commented, code can be found on my Github repository](https://github.com/pabloruiz55/MilestoneVault). Please refer to the README.md file for detailed usage instructions.

The MilestoneVault is a smart contract implementation of a vault that stores the crowdsale’s contributions and releases the funds as project milestones get completed.

Once the crowdsale has finished, the funds are stored in this vault. At any moment, the team can request a portion of those funds — as previously defined — and the original contributors can cast their vote against that request. If the majority rejects the request, the funds are not made available.   
If the founding team makes several requests and they keep getting rejected, the project gets cancelled and contributors can get a refund on the money that hasn’t yet been withdrawn on previous milestones.

As I started working on this project, I realized there was not just one right solution. There are many ways this can be achieved depending on how the founding team wants to handle it, **and what the community is willing to tolerate**. For example:

#### Initial contributors VS token holders

**My current implementation allows the ICO contributors, instead of the token holders, to vote.**

A person’s investment in a project is represented by the tokens they got in exchange for their contribution. But I don’t think that, after the ICO, the token holders should have a say on the future of the project. After the ICO, owning tokens don’t necessarily make someone an investor or a supporter of the project. I could have the tokens for mere speculation and not care about the project at all.

On the other hand, as an early contributor to the ICO, I might have already sold my tokens along the way and couldn’t care less about the current and future state of the project.

There could be a third option that takes into account only the votes from early backers that still have all, any, or some portion of the tokens. But I felt this would over-complicate the smart contract.

#### **One person, one vote VS weighted votes**

**My current implementation is based on weighted votes.**

This means that the size of the original investment is taken into account when voting. If I invested 3 ether, my vote will matter more than the vote of someone who invested only 1 ether.

#### Approval voting VS disapproval voting

**My current implementation is based on disapproval voting.**

When the team initiates a request for funds, a voting period is started. During that voting period, contributors to the ICO can vote against the request for withdrawal for the current milestone. If the majority votes against, then the request is rejected.

This could be changed so that the request is not approved by default, and the team has to get enough positive votes in order to unlock the next milestone.

Again, I don’t feel that this is a case where one-solution-fits-all applies, and I’m not claiming to know how these choices would affect the project in the long run. Depending on the nature of the project, the composition of its community and contributor base, and many other variables, the voting system could be modified to better represent all parties and prevent issues.

#### What about disputes?

![Image](https://cdn-media-1.freecodecamp.org/images/sgOSelI2BRXalzMr91P1NkkMHOS09lrxNK0A)
_Photo by [Unsplash](https://unsplash.com/photos/DCtwjzQ9uVE?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">CloudVisual</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

There’s one final topic I’d like to discuss. My inspiration for looking into this subject and thinking about ways to make ICOs a bit more transparent was [this post](https://medium.com/kleros/kleros-a-tool-against-abuse-in-token-distribution-924217746c16) by [Federico Ast](https://www.freecodecamp.org/news/what-we-can-do-to-reassure-ico-investors-that-we-wont-vanish-with-their-money-ae9cfa3e162b/undefined), one of the founders of [Kleros](https://kleros.io/).

In his article, Federico writes how he thinks ICOs should work:

> During the crowdsale, backers from all over the world send payments into a smart contract which will release payments to the team as some predefined milestones are met. For example: “Next payment will be done when the team releases a new version of the software with substantial improvements”.

> When the team claims a milestone is reached, token holders have some period of time to dispute it. If a sufficient amount of token holders reject the milestone completion claim, a dispute arises between the team and the token holders (Was the milestone met? Should the money be released?). Kleros is the dispute resolution mechanism.

As it stands today, the solution I propose could be subject to some abuse from the contributors. They have the final say in whether or not the project gets further funding, and there’s no way to refute their voting. They could even collude to cut off the project’s funds and get their money back if, for example, the tokens are worth much less than the money they put in.

As Federico writes, a dispute resolution mechanism could be put in place so that each time the contributors decide to withhold the funds (or right before deeming the project cancelled), the team can initiate a dispute, present their evidence, and get objective third parties to decide what to do.

I believe that ICOs are a great fundraising mechanism that will enable awesome companies to be born and thrive, but we must do our best effort to use this great tool consciously.

What other mechanisms do you think could be put in place to provide more security for ICO investors?

_I hope you enjoyed reading this article as much as I enjoyed writing it. I’m currently taking consultancy jobs related to smart contracts development. If you are planning on raising funds through an ICO or building a Blockchain-based product, feel free to get in touch with me._

