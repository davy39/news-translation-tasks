---
title: 'Strange Bedfellows: Fingerprinting Phenomena…or state.gov versus facebook.com'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T18:20:03.000Z'
originalURL: https://freecodecamp.org/news/strange-bedfellows-fingerprinting-phenomena-or-state-gov-versus-facebook-com-8d123866e7df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5iNOhgzIAXQVduS-r_l9NQ.png
tags:
- name: government
  slug: government
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nathan Reitinger

  When browsing the Internet, who do you trust more: facebook.com or state.gov?

  A knee-jerk reaction might be to pick state.gov — given Zuckerberg’s consistency
  in drumming up uncannily accurate advertisements and state.gov’s seemin...'
---

By Nathan Reitinger

When browsing the Internet, who do you **trust** more: [_facebook.com_](https://www.facebook.com) or [_state.gov_](https://www.state.gov)?

A knee-jerk reaction might be to pick [state.gov](https://www.state.gov) — given Zuckerberg’s consistency in drumming up uncannily accurate [advertisements](https://www.parliament.uk/business/committees/committees-a-z/commons-select/digital-culture-media-and-sport-committee/news/fake-news-report-published-17-19/) and state.gov’s seemingly innocuous purpose. Or you may feel like this is simply a “choice of evils” and, when backed into a corner, you’d be forced pick the website operated by the government. Hey, at least it’s something you, in some unknown, tenuous way, cast a vote on, right?

Still others might want to know what _should_ the metric for trust be. Is this a test of who better safeguards my secrets ([haveibeenpwned](https://haveibeenpwned.com)) or who is more likely to view me as a dollar figure (and wait, [how high](https://www.cnbc.com/2019/02/11/reddit-users-are-the-least-valuable-of-any-social-network.html?__source=facebook%7Cmain) is that dollar figure)? And still others may try to dig deeper and define “trust” from a colloquial vantage: **what does this website do without telling me?**

And here, quite surprisingly, we find a likeness.

But first, a bit of background…

### Tracking

Out of the many ways to “track” visits to websites — why is it that I’m seeing advertisements for TVs after searching for them on Amazon, _oh wait_ _that’s actually a really good deal_ _[[click click click](https://medium.freecodecamp.org/what-you-should-know-about-web-tracking-and-how-it-affects-your-online-privacy-42935355525)]_ — the best are those that you don’t have to get users’ consent for. Because let’s face it, if someone asks you to “accept” a cookie or terms of service, you will. Trust me, I said “no” one time and got kicked back to google.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uy84g3WWZi_gsOfsO61fRQ.jpeg)
_[I♥cookies](https://www.juniqe.com/i-accept-cookies-framed-poster-2459619.html" rel="noopener" target="_blank" title=")_

But the key here, at least in terms of trust, is knowledge. You are now, in some way shape or form, _aware_ of succumbing to whatever you just agreed to. Hopefully you don’t have to [give up your eldest child](https://www.theguardian.com/technology/2014/sep/29/londoners-wi-fi-security-herod-clause) like you did last time, but for the most part you’ve just agreed that no matter what happens on the website you are visiting, none of it was ‘their’ fault.

> …got caught for cheating on your wife because of a website breach — [no fault](https://www.forbes.com/sites/beltway/2015/10/22/ashley-madisons-online-terms-and-conditions-may-leave-it-legally-undressed/#2106932e6b40)

> …being harassed over and over again because your stalker keeps using a fake profile of you to send hoards of randos to your place of work — [no fault](https://www.buzzfeednews.com/article/tylerkingkade/grindr-herrick-lawsuit-230-online-stalking)

### Fingerprinting

To avoid this possibly-sticky knowledge issue, website builders may prefer to use more secretive techniques like fingerprinting to _identify_ users, in a similar way that cookies identify users.

Okay another backup — what actually is a cookie? A cookie is like a secret password you give out to the members of your secret club. No one gets through the door without the secret password, but instead of using just one password, you give each member their own special password. So you know Bob’s password is “periwinkle” and you also know that “periwinkle” has been used seventy times in the last month; woah, Bob, you should probably take a break from the club.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M-VvTkqsnN_UYG-Hiq-S-g.gif)
_Top secret #2 by Jerzy Wierzy_

In a similar way, fingerprinting is like gathering details about Bob without needing to use his special password tally. Try this one:

> He’s a tad…heavyset. Not on the skinny side, but on the rather large side. Also he’s kind of Orange, with white-ish circles around his eyes. His hair is a yellowish blonde. His [hair](https://www.quora.com/How-would-people-describe-Donald-Trump’s-physical-appearance-to-a-blind-person) doesn’t look that real. Then his face, wrinkly.

You may have guessed this is Trump, but a “guess” wouldn’t be good enough for a website owner. Instead, you need lots and lots of unique details so you can definitively say “I know that’s Trump, [it couldn’t be anyone else](https://panopticlick.eff.org).”

### Proof’s in the Pudding

So what does this all have to do with state.gov, facebook.com, and professor Narayanan’s tweet? Well, all three websites currently* use fingerprinting techniques to check you out.

Flattered as you may be, it’s a bit strange that a company who values you at [$7.37](https://www.cnbc.com/2019/02/11/reddit-users-are-the-least-valuable-of-any-social-network.html?__source=facebook%7Cmain) and a website representing our Department of State, #diplomacyinaction, are using the same sneaky means of identification. But I digress, how did I figure this out?

I built a Google Chrome Extension hunting for a very particular technique used in fingerprinting (i.e., canvas fingerprinting). I ran the extension in a Selenium web-scrape and pulled in data on approximately half a million websites, creating a database of fingerprinting attempts. My Chrome extension is essentially the same type of Chrome extension the researcher Günes Acar used to identify the fingerprinting on ftc.gov, (he used [CanvasFingerprintBlock](https://chrome.google.com/webstore/detail/canvasfingerprintblock/ipmjngkmngdcdpmgmiebdmfbkcecdndc?hl=en-US)).

Here’s a relative SQL query displaying facebook’s use of canvas fingerprinting:

![Image](https://cdn-media-1.freecodecamp.org/images/1*9SlnL76VNQcpcDP5-PiGZQ.png)
_facebook.com’s canvas image (pulled from ellipsis truncation)_

The string in the left-hand column is base64 encoded, but I turned it back into an image to see what it looks like, shown with the arrow.

Here’s another for state.gov:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYaj5q08J7mfGxXzwr6FdQ.png)
_state.gov’s canvas image (same one from ftc.gov)_

As it turns out, Facebook’s use of an emoji reveal lots of unique details about the user — like having someone _pahk the cah in Hahvahd [Yahd](https://www.npr.org/2015/08/25/434668684/testing-boston-authenticity-with-park-the-car-on-harvard-yard)_. So too do the words printed by [ForeSee](https://www.foresee.com), an analytics company, though _Mr. Jock, TV quiz Ph-D, bags few lynx!_ would have been better because it is a not-quite-but-pretty-close [perfect pangram](https://english.stackexchange.com/questions/167709/a-perfect-honest-pangram-that-is-understandable-for-a-regular-native-user).

![Image](https://cdn-media-1.freecodecamp.org/images/1*1voDM5LY41y8toDea3fZag.png)
_lenscrafters.com’s canvas image_

Either way, both the emoji and oddly-shadowed ForeSee text were requested to be drawn by your computer — without telling you about it — and both provide a lot of unique detail about who you are. A sneaky form of fingerprinting.

### And state.gov is not Alone!

There are actually 304 websites in my database that use the same ‘ForSee’ image to extract uniqueness from users. Moreover, many of them use the .gov top level domain — so it looks like foresee has a good ‘in’ with government-based websites.

### So what you’re saying is…

Maybe we shouldn’t trust either website when talking about our privacy.

In conclusion, here’s the full list of websites using this one particular canvas image — but note, the scape occurred over the summer of 2018, so some of the websites may have updated since that time. If you want to reproduce these results yourself, use Chrome with the [CanvasFingerprintBlock](https://chrome.google.com/webstore/detail/canvasfingerprintblock/ipmjngkmngdcdpmgmiebdmfbkcecdndc?hl=en-US)** extension and head on over to the listed URLs.

```
https://www.dignityhealth.org/https://www.stagingclub.com/https://www.nemours.org/https://www.thankyou.com/cms/thankyouhttps://www.upmc.com/http://www.proflowers.com/https://www.coach.com/https://ucrdatatool.gov/https://www.aarp.org/aarp-foundation/https://www.bcbsm.com/https://www.barclays.co.uk/https://www.smithsonianmag.com/https://www.menswearhouse.com/https://www.jcpenney.com/https://www.sce.com/wps/portal/home/!ut/p/b1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOIt3Q1cPbz8DTzdQwKNDTyNAw38gh0djQ0MzIAKIoEKDHAARwNC-sP1o8BK8JhQkBthkO6oqAgAStf4Iw!!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/https://www.sodimac.cl/sodimac-cl/blackfridayhttps://www.unicare.com/health-insurance/home/overviewhttps://nij.gov/Pages/welcome.aspxhttps://kidshealth.org/https://www.autonation.com/https://www.fbfs.com/find-an-agenthttps://www.mass.gov/orgs/office-of-jury-commissionerhttps://www.argos.co.uk/https://www.billygoat.com/na/en_us/home.htmlhttps://www.hertz.ca/rentacar/reservation/https://www.josbank.com/https://www.pizzahut.com/https://www.npower.com/https://www.carhartt.com/https://www.briggsandstratton.com/na/en_us/home.htmlhttps://pioneervalley.aaa.com/https://www.basspro.com/shop/enhttps://www.ftc.gov/https://www.stanleyblackanddecker.com/https://www.hickoryfarms.com/http://www.clubmonaco.ca/home/index.jsp?geos=2https://www.avid.com/sibelius-ultimatehttps://www.amd.com/enhttp://www.abbott.com/https://myamerigroup.com/Pages/welcome.aspxhttps://www.spectrumbusiness.net/loginhttps://nortonhealthcare.com/https://valottery.com/https://www.comed.com/Pages/default.aspxhttps://www.rue21.com/store/https://www.bls.gov/https://www.allenedmonds.com/https://www.myprime.com/https://www.mass.gov/orgs/massachusetts-registry-of-motor-vehicleshttps://www.ferrismowers.com/na/en_us/home.htmlhttp://www.three.co.uk/https://glucerna.com/https://www.us.elsevierhealth.com/https://www.tui.co.uk/https://www.labcorp.com/https://nationalzoo.si.edu/?fonzref=index.htmlhttp://www.emdmillipore.com/US/en?RedirectedFrom=http%3A%2F%2Fmerckmillipore.com%2F&bd=1https://thebenefitsguide.com/https://www.childrensmn.org/https://www.verabradley.com/us/Homehttps://www.asu.edu/https://www.irs.gov/https://www.mass.gov/https://www.carecreditpay.com/pmyp/showSearchhttp://www.doingbusiness.org/http://www.kraftcanada.com/https://www.redfcu.org/https://www.marks.com/https://www.snapper.com/na/en_us/home.htmlhttp://www.emdmillipore.com/?RedirectedFrom=http://emdmillipore.com/https://www.humana.com/dental-insurancehttps://www.bge.com/Pages/default.aspxhttps://www.usps.com/https://myaccountrwd.allstate.com/anon/account/login?campaign=145https://www.dfs.co.uk/https://snb.com/https://www.royalcanin.com/https://www.epa.gov/https://www.dremel.com/en_US/https://www.snapfish.co.nz/store/homehttps://www.slu.edu/medicine/clinics-community/hrc/https://www.mazdausa.com/http://www.enviroflash.info/https://www.truevalue.com/https://ftccomplaintassistant.gov/#nbhttps://www.nationalcar.com/en/home.htmlhttps://www.mdanderson.org/https://www.ups.com/us/en/global.pagehttp://www.eatonpowersource.com/https://www.gatorade.com/https://www.uscis.gov/https://www.harlequin.com/shop/index.htmlhttps://myavista.com/https://www.bcbsga.com/https://montgomerycountymd.gov/https://www.spectrum.net/https://www.tricare-west.com/https://www.aarp.org/https://www.progressive.com/agent/https://www.bea.gov/https://www.makinghomeaffordable.gov/pages/default.aspxhttps://hnfs.com/https://www.simplicitymfg.com/na/en_us/home.htmlhttps://www.chop.edu/https://www.stouffers.com/enhttps://bjs.gov/https://www.e-verify.gov/https://www.hottopic.com/https://www.mynavyexchange.com/https://www.mcdonalds.com/us/en-us.htmlhttps://www.magazineluiza.com.br/http://www.cooperindustries.com/content/public/en.htmlhttp://www.slu.edu/https://www.smilemakers.com/https://usitc.gov/https://www.humana.com/http://choa.org/https://www.colehaan.com/https://www.snapfish.co.uk/homehttp://girlshealth.gov/https://www.homecenter.com.co/homecenter-co/https://thunderbird.asu.edu/https://www.northernnewengland.aaa.com/?zip=03766&stateprov=nh&city=lebanon&devicecd=PChttps://www.ugi.com/https://www.verizonwireless.com/tablets/asus-zenpad-z8s/#sku=sku2600003?cmp=cse-Shopping-ASUS-P00J&cmp=CSE-C-HQ-NON-R-AC-NONE-NONE-2C0PX0-PX-EBAY-ASUS-P00J&cvosrc=cse.EBAY.ASUS-P00J&cvo_crid={campaign}http://www.coldwatercreek.com/https://www.usajobs.gov/https://www.lg.com/us/mobile-phones/warrantyhttps://www.usbank.com/index.htmlhttps://www.stanfordchildrens.org/https://www.buffalowildwings.com/https://www.fanatics.com/https://ensure.com/https://www.realtor.ca/mlshttps://ttb.gov/https://www.nationalcar.com/en/home.html?action=emcIndexhttps://www.abercrombie.com/shop/ushttps://lifefitness.co.uk/https://www.lg.com/ushttps://www.thenorthface.com/https://www.constellation.com/https://www.purepoint.com/https://www.sba.gov/https://www.beaumont.edu/http://www.boden.co.uk/https://www.acehardware.com/https://www.uvmhealth.org/Pages/home.aspxhttps://www.falabella.com.co/falabella-co/https://mobiloil.com/enhttps://www.verizonwireless.com/?intcmp=vzwdomhttps://www.ftd.com/https://www.va.gov/https://www.francescas.com/https://nortonchildrens.com/https://teenshealth.org/en/teens/https://www.bloomingdales.com/http://www.cooperindustries.com/content/public/en/bussmann/electrical.htmlhttps://www.oakley.com/en-ushttps://www.avid.com/https://starbuckscollegeachievement.info/welcomehttps://www.serve.com/https://ieeeusa.org/https://www.la-z-boy.com/https://www.myhealthybluela.com/la/louisiana-home.htmlhttps://lifefitness.com/http://www.worldbank.org/https://www.smithsonianstore.com/https://www.lennox.com/https://www.qualcomm.cn/https://www.pbgc.gov/https://www.metroairport.com/https://www.vagisil.com/http://www.nationalrail.co.uk/https://www.coachoutlet.com/https://www.gmfleet.com/https://www.sec.gov/https://providentcu.org/index.asp?i=homehttps://www.hayward-pool.com/shop/en/poolshttp://www.cspire.com/https://www.famousfootwear.com/https://www.enfamil.com/https://www.steinmart.com/https://www.kcpl.com/https://www.progressivecommercial.com/https://www.boots.com/webapp/wcs/stores/servlet/TopCategoriesDisplay?catalogId=28501&langId=-1&storeId=11352&webrewrite=Y&geoOpts=Yhttps://www.sony.com/https://www.silverscript.com/https://www.falabella.com.pe/falabella-pe/https://www.marriottvacationclub.com/https://www.flagstar.com//https://www.hertz.com/rentacar/reservation/https://www.nordstromrack.com/http://www.morethantired.com/https://www.homedepot.ca/en/home.htmlhttps://carecredit.com/https://www.cspire.com/business/https://www.patelco.org/https://www.ralphlauren.com/https://www.berries.com/https://www.gci.com/https://www.beaumont.org/https://www.barneyswarehouse.com/https://www.verizonwireless.com/smartphones/google-pixel-2/#sku=sku2690617?cmp=cse-Shopping-GA00141-US&cmp=CSE-C-HQ-NON-R-AC-NONE-NONE-2C0PX0-PX-EBAY-GA00141-US&cvosrc=cse.EBAY.GA00141-US&cvo_crid={campaign}https://www.state.gov/http://www.naturemade.com/#vtrlbl4lQ6UOFkCi.97https://www.avmed.org/https://www.anthem.com/https://www.caringbridge.org/https://www.mydreampool.com/https://www.snapfish.com/photo-gift/homehttps://www.progressive.com/https://www.airspacemag.com/https://www.sony.es/https://voegol.com.br/pthttps://www.personalcreations.com/https://www.ssfcu.org/https://www.subaru.com/https://www.virginatlantic.com/us/enhttps://www.qualcomm.com/https://www.nhtsa.gov/https://www.barneys.com/https://www.autotrader.com/https://www.nflshop.com/https://www.si.edu/https://www.smithsonianjourneys.org/https://stanfordhealthcare.org/https://www.sony.co.uk/https://www.findlaw.com/https://www.allrecipes.com/https://www.falabella.com/falabella-cl/http://www.naturemade.com/supplements/folic-acid?&utm_content=addotnet_11165150-AIjWvqOWintQjLiqLHeEtQ#H1kJKcPEe0zLLUck.97https://www.theglobeandmail.com/https://www.k12.com/http://www.calgary.ca/SitePages/cocis/default.aspxhttps://www.moderncoinmart.com/https://www.citipricerewind.com/https://www.uspto.gov/https://login.usajobs.gov/Access/Transitionhttps://www.bluebird.com/https://www.peco.com/Pages/default.aspxhttps://treasurydirect.gov/https://www.enterprisecarsales.com/https://www.horizonblue.com/https://unicor.gov/index.aspxhttp://www.ladyfanatics.com/https://www.oakleysi.com/en-ushttps://shop.nordstrom.com/https://www.proplants.com/https://www.allinahealth.org/https://www.blinds.com/https://www.asuprepdigital.org/http://www.bathandbodyworks.com/https://pediasure.com/https://www.fbfs.com/https://www.wrangler.com/https://www.usmint.gov/https://www.messa.org/https://www.empireblue.com/http://www.bodenusa.com/https://www.walgreens.com/https://www.cdse.edu/https://www.naturalizer.com/https://www.ieee.org/https://thebenefitsguide.com/why-are-gen-xers-falling-behind-on-health-care/http://www.epymtservice.com/index.htmlhttps://www.imf.org/external/index.htmhttps://www.allrecipes.com/recipes/17235/everyday-cooking/allrecipes-magazine-recipes/https://www.vanguardengines.com/na/en_us/home.htmlhttp://www.brittany-ferries.co.uk/https://www.verybestbaking.com/https://www.youngliving.com/vo/#/login/culture/en-UShttps://www.torrid.com/homepagehttp://www.uscourts.gov/https://www.maybelline.com/https://www.keurig.ca/http://trieagleenergy.com/https://www.bareminerals.com/https://www.caremark.com/wps/portalhttps://www.alliancerxwp.com/http://www.thecompanystore.com/https://www.boschtools.com/us/en/https://www.fedshirevets.gov/https://pedialyte.com/https://www.womenshealth.gov/https://www.realtor.ca/https://www.justformen.com/https://www.burlington.com/https://www.ovc.gov/https://uvahealth.com/https://www.sodimac.com.pe/sodimac-pe/https://www.timberland.com/https://www.hopkinsmedicine.org/https://www.hautelook.com/http://www.clubmonaco.com/home/index.jsphttps://catalog.usmint.gov/bureau-of-engraving.htmlhttps://www.keurig.com/https://www.pepboys.com/https://www.interflora.co.uk/https://www.goya.com/en/https://www.bankatunion.com/https://www.bobcat.com/https://home.bluecrossma.com/https://www.talbots.com/online/https://www.cvsspecialty.com/wps/portal/specialty
```

* as of February 15, 2019, it looks like ftc.gov’s version of ForeSee’s codebase no longer triggers a canvas fingerprint action. However, this does not displace the fact that ForeSee continues to use the technique on other government websites like state.gov and uscourts.gov, and the fact that ftc.gov had used this practice in the past.

** my home-grown version of the Chrome extension varies slightly from CanvasFingerprintBlock so your mileage may vary. If you really want to go fishing, open up the inspector in Chrome and search for `toDataUrl()`; you’ll face a barrage of javascript, but this is one of the main functions allowing for canvas to be used as a fingerprinting tool.

