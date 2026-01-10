---
title: 'Another big problem with token models: “Medium of Exchange” tokens and the
  velocity problem'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-22T14:07:33.000Z'
originalURL: https://freecodecamp.org/news/single-biggest-problem-with-token-models-part-2-52c0eca2115c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dOLz3DK9K1LUHuFK.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Investment
  slug: investment
- name: 'tech '
  slug: tech
- name: token economy
  slug: token-economy
seo_title: null
seo_desc: 'By Jose Maria Macedo

  As an analyst at Amazix, I spend a large portion of my time reading through hundreds
  of projects’ whitepapers and analyzing their token economic models to discern whether
  or not they’re adequately capturing the value created by t...'
---

By Jose Maria Macedo

As an analyst at [Amazix](https://www.amazix.com/), I spend a large portion of my time reading through hundreds of projects’ whitepapers and analyzing their token economic models to discern whether or not they’re adequately capturing the value created by the project.

This is extremely important because the value captured by a token is essentially its utility or intrinsic value which is also what ensures that the token’s price grows alongside adoption/success of the underlying project. A token lacking utility will see its price supported only by speculation and is very likely to fail in the long-run.

For more on this, see my [earlier blog](https://medium.com/@zemacedo/token-valuation-the-misunderstood-importance-of-token-economics-or-why-xrp-is-worthless-6b1b9ce5605f), in which I discussed the importance of token economic models in ensuring a token’s long-term value.

In [part 1 of this series](https://medium.freecodecamp.org/the-single-biggest-problem-with-token-models-part-i-8f9bcb3bab50), I covered the problem of misaligned incentives caused by projects which have both equity and tokens, suggesting there’s an inverse relationship between the value of a project’s equity and the value of its token in that they are effectively competing to capture the value created by the project. I also suggested some potential solutions to this issue.

In this blog, I’ll discuss the second most common problem we see with token economic models: the velocity problem facing “Medium of Exchange” tokens. I’ll begin by giving a brief background of what token economics is before describing what the velocity problem is, why it matters and some of the solutions we recommend to our clients.

![Image](https://cdn-media-1.freecodecamp.org/images/AaXmsMRKJbeixIkkpXWJtu1QQMyDyfTlVVBr)

### What is a token economic model and why does it matter?

If you’re a seasoned crypto investor or understand what a token economic model is, feel free to skip this part.

Before we start talking about token economic models, it may be wise to start at the very beginning with what is a token and what makes up its value.

A token is a crypto-economic unit of account that represents or interacts with an underlying value-generating asset. A token’s value is made up of its intrinsic value, the percentage of the token’s value that derives from demand for the underlying asset, and its speculative value, the percentage of the value of the tokens that derives from demand due to an expectation of future price increases. While speculation is nice, it is hard to control/predict and puts projects at the mercy of short-term-oriented investors, like our friend below:

![Image](https://cdn-media-1.freecodecamp.org/images/3y3eqaNZaPfZ67xy-gMHyX-xdx8tCn3HCUK6)

Rather than focus on speculative value, we recommend investors focus on intrinsic value. A token’s intrinsic value is dependent on two factors: the value created by the underlying asset _and_ the percentage of this value which is captured by the token.

The token economic model is what determines the latter — how much of the value created by the platform is captured by the token. As such, it’s one of the primary determinants of a project’s utility value and long-term success.

### Medium of Exchange tokens and the velocity problem

A pure Medium of Exchange token is a token whose sole or at least primary use is as payment for some utility on the project’s platform or protocol. There are various incarnations of this, from marketplaces such as [Signals Network](https://signals.network/) where the token is the sole currency used to buy services on the platform, to SaaS type projects like [BitStation](http://bitstation.co/) where customers can only access the platform’s utility by paying the company a fee in the native token.

The general problem with MoE tokens is that they suffer from extremely high velocity. This has been well documented by many, including [Vitalik](https://vitalik.ca/general/2017/10/17/moe.html), [James Kilroe](https://medium.com/newtown-partners/velocity-of-tokens-26b313303b77) and [Kyle Samani](https://www.coindesk.com/blockchain-token-velocity-problem/).

Basically, given the MoE token’s only use is payment for a service on the platform, there’s no incentive actually to hold tokens and incur price risk vs FIAT.

Buyers of the platform’s utility will simply acquire tokens for the purposes of a specific transaction (holding it for as little time as possible). On the other hand, sellers of the platform’s utility (whether this be users on a marketplace as in the case of Signals or the company behind the project in the case of Bitstation) will instantly sell the tokens they receive for FIAT rather than incur price risk vs FIAT.

This will result in high velocity for the token, as the increase in demand driven by buyers acquiring tokens will always be quickly matched by a corresponding increase in supply from sellers converting these tokens to FIAT.

Effectively, high velocity acts as an increase in circulating supply and is thus inversely proportional to the value of the token (although a certain base level velocity is necessary for the token to have any value, [as pointed out by James Kilroe](https://medium.com/newtown-partners/velocity-of-tokens-26b313303b77)). We can see how this works using the [Equation of Exchange](https://www.investopedia.com/terms/e/equation_of_exchange.asp), which has famously been adapted to crypto by both Chris Burniske and Vitalik.

To use Burniske’s definition:

MV=PQ

Where:   
_M_= size of the asset base   
_V_= velocity of the asset (the number of times that an average coin changes hands every day)   
_P_= price of the digital resource being provisioned. This is not the price of the cryptocurrency but rather of the resource being provisioned by the network (i.e. price in $ per GB of storage in the case of Filecoin)  
_Q_= quantity of the digital resource being provisioned (GBs of storage provided)

As Burniske tells us, in order to value the coin, we solve for M, where:

M = PQ/V.

M is the size of the monetary base necessary to support a cryptoeconomy of size PQ, at velocity V. In order to find the token price, we simply divide M by the total token supply. As we can see, the higher the velocity the lower the coin’s value.

Or, if we prefer to use Vitalik’s definition:

Vitalik takes MV=PT and in order to simplify the analysis of cryptocurrencies recasts it as MC=TH, where:

_M_= total money supply (or total number of coins)   
_C_= price of the cryptocurrency (or _1/P_, with _P_ being price level)   
_T_= transaction volume (the economic value of transactions per time)   
_H= 1/V_ (the average time that a user holds a coin before using it to make a transaction)

Therefore, the left part of the equation (MC) is simply the market cap (total supply*price) whereas the right side is the economic value transacted per time period (T) multiplied by the average time a user holds a coin (H).

To solve for the token price, one must therefore solve for C:

_C=TH/M_

Once again, we can see that the higher the velocity (or the lower the holding time H), the lower the token price.

![Image](https://cdn-media-1.freecodecamp.org/images/pdcCegPgrx4ceZkSDwRkENIKHTs956dP9L2B)
_Vitalik impress_

In both Burniske and Vitalik’s definitions, it is apparent that the velocity of the coin is inversely proportional to the value of the token, That is, the longer people hold the token, the higher the price of each token. As James Kilroy tells us:

> _“This is intuitive, because if the transactional activity of an economy is $100 billion (for the year) and coins circulate 10 times each over the course of the year, then the collective value of the coins is $10 billion. If they circulate 100 times, then the collective coins are worth $1 billion. Thus, understanding and calculating the velocity in any token economy is extremely important.”_

To see the drastic effects that velocity can have on a token’s value capture and market cap, see the following analysis [of the effects of velocity on Ethereum’s market cap by John Pfeffer:](https://medium.com/@john_pfeffer/hi-johnny-8411ec5d266)

> _“In a protocol-land where protocol usage is managed by capital-efficiency optimising intelligent bots (which seems likely), let’s assume for simplicity the absolute floor on 1/V is the block time of the chain in question. Let’s then take ETH with a 2.5 minute block time as an example (highly theoretical, just to make a simple maths point). This implies each token could be used (assuming fixed block times, which in fact will likely shorten) 210,240 times a year. Buterin, Choi, etc. talk about, say, 10% of ETH being staked (let’s assume staked tokens never move at all). That would bring V down to 189,216 per year. Assume 50%, then V=105,120. Multiply this last number by $50b of network value (i.e., ETH just maintains its current value, and you’d need $5.25 quadrillion of economic activity denominated in ETH (i.e., excluding any ERC20/ ERC721-denominated economic activity), that is to say, 65x the current global GDP of $80 trillion. These numbers are all just varying shades of silly. That’s the point. As long as some of your tokens are circulating at a high V, your overall V is high.”_

### **Solutions to the velocity problem**

The most commonly used solutions to this problem all involve designing token economic models that provide incentives for people to hold the token — basically turning it into an asset (or “Store of Value”) rather than a currency. This can be done in several ways:

#### (1) Ensure token model has a “sink” in it

This one was initially suggested by Vitalik and has been widely adopted since. Basically, it involves designing token models with “buy-and-burn” mechanisms in which the project charges transaction fees and then uses some or all of the cash flows generated by its platform to purchase its own tokens and destroy them. The decrease in supply raises the value of all remaining tokens by the percentage of total supply destroyed. Effectively, the project is distributing its cash flows to its token-holders, very similar to how equity distributes cashflows to its stockholders through a dividend.

An example of this is Iconomi, a digital asset management platform which [burns preset percentages of all fees collected](https://iconomi.zendesk.com/hc/en-us/articles/360001428854-Repayment-Programme-Buybacks-Token-Burn) and also produces quarterly reports outlining the number of tokens burned (crypto quarterly earnings reports).

Since, as we previously mentioned, velocity acts as an increase in circulating supply which reduces the value captured by the token, a buy-and-burn mechanism has the opposite effect of ensuring each additional transaction (i.e. increase in velocity) on the platform reduces the total supply of tokens, thus counteracting the increase in velocity with a deflationary force.

This should also reduce velocity by giving people a reason to hold the token, namely the expectation that it will be more valuable in the future due to the deflationary force created by the token burn.

![Image](https://cdn-media-1.freecodecamp.org/images/4xvIyYR8SJlQ7BkY8LMyp81y935fNtYHlvK-)
_The Joker reducing $ velocity_

#### (2) Implement a “profit-share”

This one was initially [suggested by Kyle Samani of Multicoin](https://multicoin.capital/2017/12/08/understanding-token-velocity/). It is very similar in spirit to the “buy-and-burn” in that it is providing the token with a yield and turning it into an asset that generates cash flows.

An example of this is Augur which pays REP holders for performing work for the network. REP tokens are like taxi medallions: you must pay for the right to work for the network. Specifically, REP holders must report event outcomes to resolve prediction markets. Other examples of “profit-share” tokens include [FOAM](https://foam.space/) , [Sharpe Capital](https://sharpe.capital/) and also Ethereum once it has switched to Proof of Stake.

Once again, a profit-share reduces token velocity by forcing people to hold the token in order to have the right to generate cash flows by providing work to the network.

![Image](https://cdn-media-1.freecodecamp.org/images/vrdFC-TozgbVmvYVmqlkK3yPMTW2A3YrMJHo)

#### (3) Encourage users to lock up tokens

This can be done through mechanisms such as [Proof-of-Stake](https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQ) which encourage users to lock up a certain amount of tokens, verify transactions and receive a yield in return (this also has the added benefit of acting as a profit-share). DASH, NEO and Navcoin are all examples of coins that have implemented proof of stake models.

Users can also be encouraged to lock up tokens through clever gamification — providing users with rewards (financial or otherwise) for locking up tokens. For instance, Alluma, a crypto exchange targeting Asian markets, offers different membership levels and fee discounts based on users staking different amounts of tokens:

* Gold memberships offer 35% discounts in exchange for staking 2500 LUMA for 30 days, and
* Platinum memberships offer 50% discounts in exchange for staking 10,000 LUMA for 90 days ([source: page 28 of Alluma whitepaper](https://cdn2.hubspot.net/hubfs/4077694/whitepaper%20languages/Alluma%20Whitepaper.pdf?__hssc=147911272.3.1531961915300&__hstc=147911272.bf36623eb62b5916dee4146a67129a0e.1531961915299.1531961915299.1531961915299.1&__hsfp=2747456470&hsCtaTracking=8aed7630-08c6-4c61-8bd1-6db116fa6876%7C50cad1a6-1dbf-4b3e-9f82-a8dd851584c5)).

For another example, we can look at YouNow, a live streaming app which allows users to tip content creators in its native token PROPS.

While content creators could immediately convert PROPS to FIAT, they are incentivized to hold onto it as their content is ranked higher by YouNow’s algorithm based on how many tokens they hold. Since discoverability leads directly to more tips, YouNow is effectively turning PROPS into an asset by ensuring users who hold it are able to generate cash flows.

![Image](https://cdn-media-1.freecodecamp.org/images/HHs-7B9WUn3SVSULp62cIeO8FbpXYO8kvSFk)
_Donald Duck’s masternode_

### Conclusion

Token economic model design is an extremely important and underrated area for both investors and founders of cryptocurrency projects to think about. A project with a weak token economic model may see its token price fail, even as the project itself succeeds, simply because the token is not capturing any of the value created by the project.

Velocity is one of the biggest problems with current token economic models and many established projects such as [Civic](https://www.newtownpartners.com/how-civics-updated-token-model-decentralizes-trust/), [Storj](https://www.coindesk.com/300-million-lockup-storj-clarifies-token-economics-surprise-reveal/,) and Po.et have recently revamped their token models to address this issue. If you believe your project may also suffer from high velocity and are interested in having your token economics audited or discussing this further, feel free to get in touch with me through here or on [Twitter.](https://twitter.com/zemariamacedo)

