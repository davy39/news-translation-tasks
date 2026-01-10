---
title: How to analyze the security of your application with threat modeling
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-30T11:09:14.000Z'
originalURL: https://freecodecamp.org/news/threat-modeling-goran-aviani
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/image-44-1.png
tags:
- name: Application Security
  slug: application-security
- name: Stride
  slug: stride
- name: threat modeling
  slug: threat-modeling
seo_title: null
seo_desc: 'By Goran Aviani

  Digital attacks are more and more frequent, and the first step in securing your
  app is understanding the threats and how to counter them.

  Threat modeling is an approach that analyses the security of an application. It
  is a structured ...'
---

By Goran Aviani

Digital attacks are more and more frequent, and the first step in securing your app is understanding the threats and how to counter them.

Threat modeling is an approach that analyses the security of an application. It is a structured way to identify, quantify and mitigate the security risks in an application.

You are about to read a short briefing I wrote for myself some time ago, made up from information I’ve collected by dissecting several other articles. The idea behind this article is for it to act as a reminder and to be as short as possible but still hold relevant information.

---

So with that being said, let’s write the most common definition of threat modeling:

> Threat modeling is a security process with goals to identify objectives  and vulnerabilities and then define countermeasures to prevent or lessen  the effects of threats to the system.

I’ve also read that threat modeling gives answers to these four questions:

* _What are we working on?_
* _What can go wrong?_
* _What are we going to do about it?_
* _Did we do a good job?_

And I couldn’t agree more. That’s why threat modeling is composed of four parts, where each part answers one question:

* _Decomposing the application._
* _Determining the threats._
* _Determine counter measures and mitigations (reducing the danger)._
* _Rank threats._

# Decomposing the application

The goal of this step is to understand the application by decomposing it into parts and seeing how those parts interact with external entities. The way to do this is to gather information and documentation by mapping the application’s entry points, elements/assets and dependencies.

* Decompose the application by drawing a diagram of various components in the  application. You can do this with Data Flow Diagrams.
* Identifying  entry points — Software entry points may serve as entry points of an  attacker( login pages, search fields, HTTP requests etc.). It is essential that all entry points are identified and documented.
* Identifying  the elements/assets — that have a value, and therefore a risk of being  attacked. An asset can be in a form of data like a list of customer  information, it can also be in different forms: overall application  availability, organizations reputation.
* Dependencies  are parts of the app that lay outside of the application’s code. As  these items are outside of your control they may pose a threat if they are not properly maintained so identifying these dependencies will minimize the application’s overall risk.

# Determining threats

Determining threats can be done by threat categorization STRIDE. STRIDE is an  approach from the attackers perspective, and it is used to determine  threats. While there are other approaches such as ASF (Application  security framework — an approach from the defenders perspective to  determine countermeasures), in this article I will be focusing on  STRIDE.

> STRIDE categorization outlines six most common types of threats and their countermeasures.

## STRIDE

1. **S**poofing identity — Impersonating someone or something else.
2. **T**empering with data — Modifying some data on disk, network, memory.
3. **R**eputation — Denial of proof of some action.
4. **I**nformation disclosure — Exposing information to someone not authorized to see it.
5. **D**enial of service — Deny or degrade service to users.
6. **E**levation of privileges — Unauthorized gaining of more rights than originally intended.

# Determining countermeasures

Every threat from STRIDE has a countermeasure.

1. Authentication (for Spoofing) — Establishing a verifiable identity.
2. Data protection (for Tempering with data) — Maintaining data and ensuring consistency of data and methods that work on data.
3. Confirmation (for Reputation) — Every action against the application must be logged.
4. Confidentiality ( for Information disclosure) — Restricting access to system and data.
5. Availability(for Dos) — Leverage levels of redundancies.
6. Authorization (for Elevation of privileges) — Limiting access to data, actions and services.

# Rank Threats

To  tackle the problem of ranking threats Microsoft devised a risk  assessment model called DREAD, a model which provides five rating  categories for each threat. In the beginning they used the rating from 1  to 10, ex. for every threat in each category a rating from 1 do 10  would be given.

However,  as different people selected very different numbers, there was a shift  away from DREAD ratings within high number ranges towards some simpler  classification with 4 different levels of risk:

* 1: low
* 2: medium
* 3: high
* 4: critical

Sum of all ratings for a given threat is used to prioritize it among other threats.

The categories to rank for every threat are:

* **D**amage — how bad would an attack be?
* **R**eproducibility — how easy is it to reproduce the attack?
* **E**xploitability — how much work is it to launch the attack?
* **A**ffected users — how many people will be impacted?
* **D**iscoverability — how easy is it to discover the threat?

For  every threat in each category a rating from 1 do 4 is given and the sum  of all ratings for a given threat is used to prioritize it among other  threats.

---

Up until now we decomposed the application, analysed functionalities,  determined possible risks and identified weak points that could be  exploited. Then we determined the countermeasures and used DREAD to rank  the risks. The only thing left is to act accordingly in solving those  risks.

---

Thank you for reading! Check out more articles like this on my freeCodeCamp profile: [https://www.freecodecamp.org/news/author/goran/](https://www.freecodecamp.org/news/author/goran/) and other fun stuff I build on my GitHub page: [https://github.com/GoranAviani](https://github.com/GoranAviani)

