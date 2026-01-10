---
title: What’s In a Name? DevOps Edition.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T22:00:43.000Z'
originalURL: https://freecodecamp.org/news/whats-in-a-name-devops-edition-c3f4e1f85dfb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g7vToxOAkz-rfjtpHwgApg.jpeg
tags:
- name: coding
  slug: coding
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jon Goodall

  I’ve been working in DevOps for a while now, and I’ve yet to come across a tool
  that didn’t have something odd about its name. It’s either got a backstory, a meaning,
  or it’s Greek. I don’t know why, but I’d postulate that it’s because...'
---

By Jon Goodall

I’ve been working in DevOps for a while now, and I’ve yet to come across a tool that didn’t have something odd about its name. It’s either got a backstory, a meaning, or it’s Greek. I don’t know why, but I’d postulate that it’s because the market is completely flooded with tools, and you **_need_** yours to stand out, so you can make money — either from the tool itself, or a support package.

With that in mind, I thought I’d translate them. In case you ever have the misfortune of having to explain to someone at C-Level (‘C’ as in CEO, not the swear word), why you’re trying to install an octopus.

I’ve listed them here, and linked to the explanation, so you don’t need to read the list. But please do, the stats are a great ego boost.

* [Docker](#048e)
* [Jenkins](#ee62)
* [Bamboo](#82c6)
* [Drone](#62ba)
* [GoCD](#b86d)
* [Octopus Deploy](#38b3)
* [Ansible](#d56a)
* [Chef](#d1be)
* [Puppet](#d90d)
* [TeamCity](#39cb)
* [UrbanCodeDeploy](#054b)
* [Consul](#356e)
* [Vagrant](#16aa)
* [Kafka](#4af7)
* [Kubernetes](#a7f7)
* [Terraform](#63f0)
* [Vault](#f8c4)
* [Sentinel](#d8c4)

**Docker**.

_The tool_: creates, operates and managers containers.

_The meaning_: Containers are in a dock at some point. A “docker” is an occasional shorthand for someone that works at a dock, with containers.

**Jenkins**.

_The tool_: General purpose CI tool. CD was retconned into it with plugins that let you write pipelines (which I happen to quite like).

_The meaning_: Stereotypical name for a butler. Butlers run households and “get stuff done” in a general purpose sort of way. Not to be confused with a valet (essentially a male equivalent of a lady’s maid). Also lots of creative definitions on UrbanDictionary, but I refuse to link to that (because no doubt someone will send me a bill for it).

**Bamboo**.

_The tool_: CI/CD tool from Atlassian. Works with other Atlassian tools (jira, bitbucket etc.) much better than other tools as a result.

_The meaning:_ Fast growing plant, not very nutritious, pandas eat a lot of it — this one doesn’t make sense to me.

**Drone**.

_The tool:_ Yet another CI/CD tool. This one runs in Docker, with pipelines written in a version of docker compose. I guess you could call it “container native”, if you like. They do.

_The meaning_: The proper name for most “worker” insects. And what every corporate employee feels like many times a day. Well, I do anyway.

**GoCD**.

_The tool:_ **ANOTHER CD TOOL.** The odd names are making more sense now… (This definition is a little unfair, because it’s actually a really good tool. Lots of built in functionality, runs on kubernetes really well.)

_The meaning:_ It’s written in GoLang. You could take it to mean “Go and do CD”.

**Octopus Deploy**.

_The tool:_ One of the few deployment specific tools (outside of a couple of DB deployment tools) that I’ve come across. The sales pitch is that it gets you away from writing massive scripts. This will do the “heavy lifting” for you. Not sure I buy that. Not sure they do either, as they have a method of writing pipelines as code.

_The meaning:_ Feels like someone thought they were being clever with this one — “an octopus has tentacles, we’ll call our remote agents tentacles”. Nice Octopus graphics though.

**Ansible**.

_The tool:_ Configuration management tool (there’s a few of these in the list, and in essence they all let you determine the state of a server in code). Uses YAML (Yet Another Markup Language) file to store its config. Steps are executed sequentially by default, so ordering is simple.

_The meaning:_ I think this one is quite clever, if you like science fiction.

> “The name of Ansible originally came from the book Rocannon’s World by Ursula Le Guin, published in 1966. She used the word as the name of an instantaneous communication device that would allow contact over vast interstellar distances”

> [— https://h2g2.com/edited_entry/A1165501](https://h2g2.com/edited_entry/A1165501)

I don’t know if that was the inspiration for the name, but I like to think it was.

**Chef**.

_The tool:_ Configuration management tool. Steps in “recipes”. Really nice interface.

_The meaning:_ Chefs read cookbooks or create recipes to achieve the same end result each time (well, nearly. Depends on the restaurant. Hopefully the same isn’t true here).

**Puppet**.

_The tool:_ Configuration management tool (again). The IDE is called “geppetto”, which is nice. (Geppetto made Pinocchio, in case you didn’t know. I didn’t until I looked it up).

_The meaning:_ You control a puppet on a set of strings from elsewhere. Puppet itself though is the other way around most of the time, as the deployment targets ask for the changes.

**TeamCity**.

_The tool:_ CI/CD tool from JetBrains (who make [Intellij](https://www.jetbrains.com/idea/) and a bunch of other tools).

_The meaning:_ Erm. Right. No logic or clever backstory here that I could find. Seems like it was made to sell to large corporations — which to be honest, I can understand.

**UrbanCodeDeploy**.

_The tool:_ IBMs’ take on a deployment tool. The only tool I’ve found that doesn’t have a free trial or download, so I couldn’t try it out.

_The meaning:_ I couldn’t find any reason behind this one, so I think it’s just a name.

**Consul**.

_The tool:_ Key/Value store from Hashicorp. Nice CLI and API’s. Also does service discovery, health-checking and DNS (via agents).

_The meaning:_ This one makes absolutely no sense to me. A consul is an official appointed by a state to live in a foreign city and protect the states’ interests there — e.g. they work at the consulate.

**Vagrant**.

_The tool:_ Allows you to make quick and cheap virtual PC’s on your existing physical PC. Saves you the pain of having to use VirtualBox/VMWare tools directly. Although you do still have to install them.

_The meaning:_ Colloquialism for a wandering beggar. If you do a little mental gymnastics you can see where they were going with this — person of no fixed address, virtual PC with no permanent home.

**Kafka.**

_The tool:_ Used for building realtime data streams.

_The meaning:_ Apparently it’s named after [Franz Kafka](https://en.wikipedia.org/wiki/Franz_Kafka).

**Kubernetes**:

_The tool:_ Kubernetes is a “container orchestration tool”. Which translates to it controls large amounts of containers

_The meaning:_ Loosely translated from Greek as a helmsman, or habour pilot. Essentially a controller. Yes the spelling is a bit different, but you can see the logic here.

**Terraform**.

_The tool:_ Infrastructure as code from HashiCorp. Lets you make anything in the major cloud providers, and manages their state. So that if someone changes something by hand, terraform can correct it.

_The meaning:_ SciFi staple. Changing the environment to suit you. We (as in the species) might do it to Mars (the planet, not the chocolate) one day.

**Vault**.

_The tool:_ Keeps data secure, only known people have the keys. Can seal/unseal/re-key. Various access policies

_The meaning:_ Another analogy. Not a Hollywood vault with a big room behind 1 massive door, but more a vault with lots of safety deposit boxes in it. For a film reference I’d go with “The Bank Job (2008)”.

**Sentinel**.

_The tool:_ Policies as code. Works with other HashiCorp tools (enterprise version, you’ve got to pay for this one) to ensure that they are only used in a pre-defined manner. Lots of good examples on their website, go check it out.

_The meaning:_ Sentinels guard or watch things to ensure that people don’t do things they aren’t meant to. Typically military personnel.

#### Wrapping up

Right, that’s it for now, because I’ve run out of brain. If you’ve made it to this point I’m impressed. If you’ve skimmed the list to see if there’s a witty final statement “hi, *waves*”. If you only wanted to see what Sentinel was and saw me waving, I don’t blame you.

I’ll try to post a follow up at some point as I find/try/use more tools — particularly ones with “odd” names. If there’s any you’ve come across and I’ve missed, or if you have a better reason/definition for any I do have drop me a comment.

Hopefully this (very dry, quite boring) list saves you a bit of a headache, or gives you one, who knows. I promise next time I’ll write about something interesting and maybe grind an axe for a bit.

