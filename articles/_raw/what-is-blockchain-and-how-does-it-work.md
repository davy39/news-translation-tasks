---
title: What is Blockchain and how does it work?
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2020-02-10T23:48:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-blockchain-and-how-does-it-work
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ca4740569d1a4ca335e.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Developer
  slug: developer
seo_title: null
seo_desc: 'If you''re interested in technology, there''s a good chance you’ve probably
  heard the terms Bitcoin, Crypto, Ethereum, or even "distributed, decentralized ledgers."

  You’ve probably heard people talk about cryptocurrency and encryption algorithms,
  about...'
---

If you're interested in technology, there's a good chance you’ve probably heard the terms Bitcoin, Crypto, Ethereum, or even "distributed, decentralized ledgers."

You’ve probably heard people talk about cryptocurrency and encryption algorithms, about the end of "intermediaries" and so on.

It's easy to assume that cryptocurrency (eg: Bitcoin, Ripple, Ethereum, Litecoin, etc.) are the same as blockchain. They're not.

[Cryptocurrencies](https://en.wikipedia.org/wiki/Cryptocurrency) are a clever application of a much cleverer technology – [the Blockchain](http://en.wikipedia.org/wiki/Blockchain_(database)).

In this post, I will cover some of the basic concepts of the blockchain so you understand what it is, how it must be conceptualized, and what can be built on top of it.

But as with all things, they make more sense if you understand *why* they were invented, before you get into what they do. That context will help you grasp what problem the blockchain was designed to solve.

## Why use blockchain?

Great question. So glad you asked. Let's sit back and do a small thought experiment.

What happens if you and your best friend *independently* and separately conduct the same petition campaign? Let’s say it’s for the “Free the Hamsters” cause.

Let's say you conduct it in an identical sequence across the same suburb, but come up with different sets of signatures on the petition. Which version of the signed petition is the “source of truth”?

You would need to trace back your separate trails, one signature at a time, to locate the *last* discrepancy. And then you'd have to work further back to identify the first result that diverged between your signature sheets. Prior to that root divergence, all other signatures on the two lists should match up.

You then know that prior to that divergence. Both lists are in accord, so those signatures represent the minimum number of people who signed to support freeing the hamsters.

While that may work well for hamsters and small suburban surveys, it doesn’t work so well in the digital world. Or voting, banking, financial transactions, transferring land title, discharging contractual obligations etc. You need independent and “trusted third parties” to verify a chain of events, and solemnly reassure you that the "chain of custody" was unbroken.

A "chain of custody" can sometimes also be called the "provenance" – they both mean the same thing: the sequence of historical events concerning the data in question.

That’s why you have governments having the final say on your identity, and votes need to be physically counted and recounted by hundreds of volunteers, and clerks in dingy offices maintain ledgers and certificates to confirm whether or not you own your farm/white picket-fenced bungalow.

That is why you need financial intermediaries to ensure that when you buy your collector's item Darth Vader doll, using a credit card, the money (value) is “removed” from your account and “put into” to the seller’s account.

This is technically called the “[double spending problem](https://en.wikipedia.org/wiki/Double-spending)” – how do you ensure that you’re not spending the same money twice? Without someone to do this, you could spend money and at the same time continue to hold on to that money.

So it’s a big problem really – modern life requires that we rely on, trust in and pay for “trusted” third party intermediaries to ensure that value (money) does actually digitally “change hands”. That is why Visa and MasterCard exist, and why PayPal and others link with your bank accounts.

> At the heart of the blockchain's why is this problem: how do you know a sequence of events has not been tampered with to alter the current state?

This is where the blockchain fits in. Clear, so far?

## How Blockchain works

For the sake of communicating a concept with simplicity, I may take liberties with some of the technical, under-the-hood aspects of this technology. My aim is to get you to understand what it is and have a mental model of how it works. For that, I may need to be a little loose with precision in order to improve the odds of comprehension, especially for non-native English speakers.

It is essential to remember that the blockchain is a technology – mathematically complex software code to be specific. And Bitcoin (or Ethereum or any of the other cryptos on offer) are just applications of that technology.

So the key principles are:

* Blockchains are ‘mined” (produced through the expenditure of effort, like in gold mining) by powerful and resource-hungry computers – called nodes, that are on the same network.
    
* Chains of digitally encrypted and timestamped records of transactions are lumped into “blocks”, which are maintained on a “ledger” by each node. As transactions are added to a block, and blocks are linked together linearly and chronologically as "chains". Then the entire record/ledger gets synchronised across the network of nodes such that all the block "chains" on the nodes should tell an identical story of the history of any given transaction. Thus we get "block + chain = blockchain". It's a long, complicated linked list.
    
* Each block in a chain has its own id - a cryptographic hash that is unique and specific to each block. That hash is also stored in the *next* block in the chain, causing a link. A block can store thousands of transactions and the tiniest change in that block's data would result in a new hash. So if a hash changes but the next block has a different hash, then we know some data in the previous block was tampered with.
    
* As hundreds become thousands of nodes (and more are added all the time), each node has to “agree” on the history of the blocks/ledger – this is called "critical consensus". One of the ways in which consensus is achieved is through the cryptographic hash we talked about earlier.
    
* Where there are discrepancies in the ledger (for example the hash of a block doesn't match with the next block's reference to the previous block's hash), the ledger with the longest chain of valid transactions embedded will be the “correct” one – the source of truth. Any nodes working on other (shorter versions) of the chain switch to the longer one. This maintains the critical consensus (this bit is hugely oversimplified, but sufficient for now).
    
* Any naughty interception or change to one ledger (again, for example, where a block's hash doesn't tally) would immediately create a discrepancy with all the other versions. It would also have a shorter block “history” to corroborate it, which makes that tampered version a suspicious character in the blockchain network where length matters (ahem).
    
* Replicating that discrepancy across *all* the versions of the ledger – the entire blockchain network – is such a huge task that it is computationally impractical, and would only happen if the bad guys suddenly had control over the *majority* of the nodes mining blockchain and changed them all rather rapidly. This sort of coordinated attack on the majority of the nodes on the network is often called the [51% attack](https://en.bitcoin.it/wiki/Majority_attack).
    

Interestingly, Satoshi Nakamoto says in the [original Bitcoin white paper](http://bitcoin.org/bitcoin.pdf),

> “*As such, the verification is reliable as long as honest nodes control the network, but is more vulnerable if the network is overpowered by an attacker.*”

However, elsewhere [he/she/the organisation](http://en.wikipedia.org/wiki/Satoshi_Nakamoto) (we don't know who "Satoshi" is) calmly points out that to modify past transactions in blocks, across the entire network of nodes, would require the attacker to re-do the chain of custody in those blocks, and all the blocks added after that. Then they'd have to run like mad to catch up with, and surpass, the work of nodes that aren’t under the bad guy’s control (so that they can re-write the ledger, so-to-speak).

And because of this, the “*probability of a slower attacker catching up diminishes exponentially as subsequent blocks are added*”.

The sheer programmatic complexity, pace and volume of nodal activities make it hard for counterfeiters/attackers to catch up with, let alone outrun, the new blocks mined constantly.

That does make sense. It’s like the lie you tell one family member about why you couldn’t attend their kid’s flute recital. And then you have to madly chase everyone else in the family and ensure you’ve told them all the same lie so that when the original person you’ve lied to brings it up, everyone is aware of this lie and plays along. Sounds exhausting.

To wrap up, the defining characteristic of a blockchain is that it is a distributed ledger across many, many nodes and it is extremely computationally intensive (expensive) to add nodes to that network.

Thus each ledger must be "aware" of all the transactions, and must have an agreed version (which will have the longest “chain of custody” behind it) across the entire network to which the next transaction will be added.

> *As* [*Satoshi Nakamoto declares*](http://bitcoin.org/bitcoin.pdf) *in the original Bitcoin white paper, “ The only way to confirm the absence of a transaction is to be aware of all transactions.”*

Importantly, the blockchain "[dis-intermediates](https://en.wikipedia.org/wiki/Disintermediation)" trust – so we don’t need to pay “trusted third parties” transaction fees for being trustworthy and keeping us, and the counter-parties we deal with, honest. The blockchain programmatically ensures truth (provenance) of the history of transaction in it.

### So why should we care?

Well, by getting rid of the need for “trusted intermediaries” any intermediary that charges a modest fee for giving us the gift of certainty needs to find a new job. And that impact banks who traditionally offer such assurance services.

It also means that we can program “[smart contracts](https://en.wikipedia.org/wiki/Smart_contract)” between promisor and promisee that automatically recognise (digitally) whether that promise has been delivered or not.

This has enabled a truly tech savvy artist like [Imogen Heap to sell her music directly](http://fortune.com/2016/09/22/blockchain-music-disruption/) to her listening public, and collect her dues directly from them rather than losing the bulk of earnings to record labels, managers and other “trusted intermediaries”.

It will likely change the way Intellectual Property is protected, accessed, shared, distributed, and developed on the internet.

It could even mean that Uber’s fleet of drivers transact directly with people who want a ride rather than rely on Uber to coordinate and control the flow of information and money.

It may mean that I could directly send you small amounts of money for virtually no fees (micro-transactions). It could mean that the millions of unbanked people in the world who have smartphones can start to transact well beyond their traditional physical-world boundaries.

Wonderfully enough, governments are looking beyond just cryptocurrency when it comes to deploying this technology – to [record land ownership](http://www.redherring.com/startups/georgia-pilots-sweden-ponders-blockchain-future-europes-land-registries/), [for example](http://dci.mit.edu/assets/papers/spielman_thesis.pdf).

In effect, we could create a world of true peer-to-peer digital transactions for the transfer of value that is distributed, horizontal, removes the need to rely on trust, and above all requires extraordinary computational power to tamper with. These transactions could be between people, machines and devices.

It could therefore offer a new security paradigm for the protection of data collected by and transferred through the “internet of things”.

I personally believe that the complexity of the modern world is obscured behind intuitive touchscreens. Blockchain technology will quickly become embedded in our technological universe without us being fully aware of it – just like we have been using yeast recombinant DNA for synthetic insulin production since the 1970s.

The changes and cost savings will be sweepingly referred to as technological changes, like that "interweby thing” or some other vague, all-inclusive phrase.

One catch: it'll work as long as we can trust that a "trust-less system" that is coded and engineered by humans (whom we trust?) will further the cause of trust-less-ness in an untrusting and untrustworthy world. You may need to read that sentence several times.

## Wrapping up

OK – you should now be reasonably aware of the basics of blockchain. But there is a lot more to learn if you're interested.

You can debate whether blockchain is useful or over-hyped, revolutionary or boring. But it's hard to ignore that it is pretty cool as a concept.

Here is a really fantastic video by Anders Brownworth that explains the whole thing with a mockup blockchain. I strongly recommend you watch it.

%[https://youtu.be/_160oMzblY8] 

And as a learning exercise, you can build your own blockchain right in your browser or your command line. Here's a quick [tutorial for how to build your own blockchain](https://www.freecodecamp.org/news/how-does-blockchain-really-work-i-built-an-app-to-show-you-6b70cd4caf7d/).

If you have any comments about this article or think I could have explained parts of this better, Tweet at me at [@ZubinPratap](https://twitter.com/zubinpratap)

If you would like to learn more about my journey into code, check out [episode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) of the [freeCodeCamp podcast](http://podcast.freecodecamp.org/), where Quincy (founder of freeCodeCamp) and I share our experiences as career changers that may help you on your journey. You can also access the podcast on [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true), and [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

I will also hold a few AMAs and webinars in the coming months. If this is of interest to you please let me know by going [here](http://www.matchfitmastery.com/). And of course, you can also Tweet me at [@ZubinPratap](https://twitter.com/zubinpratap).
