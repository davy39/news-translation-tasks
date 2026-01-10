---
title: What Can Money Heist Teach Us About Cybersecurity?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-07T14:49:47.000Z'
originalURL: https://freecodecamp.org/news/cybersecurity-lessons-from-money-heist-show
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/money-heist-image.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: '#infosec'
  slug: infosec
- name: threat modeling
  slug: threat-modeling
seo_title: null
seo_desc: 'By Periklis Gkolias

  I was watching the TV series, La Casa De Papel (Money Heist), on Netflix a few weeks
  ago. I realized that the story of the gang can reveal some best practices we should
  use while dealing with the security of the products we build....'
---

By Periklis Gkolias

I was watching the TV series, La Casa De Papel (Money Heist), on Netflix a few weeks ago. I realized that the story of the gang can reveal some best practices we should use while dealing with the security of the products we build.

Beware – this text contains spoilers. If you haven't watched the show until the end and you are planning to, please visit the article on a later day. Or proceed at your own risk :)

## Threat modeling can protect you against unexpected events

First of all, **what is threat modeling**?

Threat modeling, in layperson's terms, is an analytical process. In it, the engineers who build a product coordinate with the security team. They collaborate towards the security architecture of the product.

More specifically, it's the model – how someone can attack the product – and what is worth protecting (assets). They also model what they can be less concerned about. Less concerned not because they don't care. But because protecting it can be more costly than the asset itself.

Threat modeling can get you a long way and protect you from certain events, against the odds. 

What is threat modeling in our "Money Heist" case? It is Professor's (aka Sergio Marquina's) plan against all potential routes the plan will take. In having alternatives, even for the edgiest scenarios. The assets are clearly the stolen money or his comrades in the heist.

## A single point of failure can cause a chain of bad reactions

Threat modeling might help you recover from many security problems that will arise. You can recover from a cyber-attack, but things will never be the same. A crack in the security wall can have a domino effect.

Imagine a lake dam, with a few cracks around it going unnoticed and being exploited by nature. You can always fix it, but it might take time for the lake visitors to establish trust again. 

In the same way, small companies that experience a security issue might close in the next few months, according to a [survey](https://cybersecurityventures.com/60-percent-of-small-companies-close-within-6-months-of-being-hacked/). 

This is like the Professor, where he lost respect after the gold (temporarily) vanished. Even though his great problem-solving skills helped resolve the issue, things got hairy very fast.

![Chain reactions](https://i.imgur.com/3047AXD.jpg)

## Luck is not a strategy in the long term

In the show, there are some provocative cases of luck. For example:

* Raquel renegading the police organization
* Police and army failing plans to invade the bank
* Failing to shoot to the target many times. Especially by troops that are supposed to be professional shooters.

After all, in the [pragmatic programmer](https://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X) book, there is a whole chapter about how bad it is to program by coincidence. It likens luck-as-strategy with the soldier that moves without a plan in a field full of landmines.

Snitches and worse-than-expected defense might give you some extra time to move with your plan or escape. But you have to take advantage of it. To either move with your plan or escape. Always think your luck might go away, any time soon.

## Never drop the weapons

This is not specific to cybersecurity but to life in general.

Pain is temporary, quitting lasts forever. Accept your mistakes, remediate them and learn from them. As long as your heart is pumping blood, you are not dead yet.

* Architectural mistake? Patch it immediately and re-architect the product (yeah, I know...delivery and business constraints)
* Below expectations monitoring? Fix it now. Add more people and see how they can be more effective
* Serious defects in the code? Train your team in secure practices and code reviews focused on security. Buy a license to a package like Snyk or Nessus. Plan some percentage of your capacity to patch the most severe ones

![Budget constraints](https://i.imgur.com/BtMM0JS.jpg)

## Even in the worst of moments, keep your composure

Imagine a ransomware attack. It is there, it is happening. Screaming over people's heads will not solve the problem.

When you cannot win against an attack, you still have to do your best, to at least not lose. For sure, don't panic. As the Stoics say, you have to be your best self on the things you control. And let the rest just be. Accept them.

You cannot control the next stage of an attack. But you can do your best to prevent it, to not repeat the same mistakes, and to close the open doors that exist now.

That is true for non tech issues too. If a pipe broke at home what would you do? First, you stop the damage and maybe provide a sustainable fix (given the timeframe). Then you try to see how this will never happen again.

Don't lose your temper and clear mind, like Tamayo lost it, when he realized the gang was blackmailing him for various reasons.

He got angry, he got blackmailed, he was even ridiculed in the eyes of the European Central Bank. And what was the result? He lost, hands down, even though he lied to the media about winning.

## Conclusion

Top-notch cybersecurity is not a free lunch. And not everyone can do it, as the caveats are so many. But with some discipline, retrospection, and humility, you can do wonders. Also, the show is great, if you haven't seen it, please do.

