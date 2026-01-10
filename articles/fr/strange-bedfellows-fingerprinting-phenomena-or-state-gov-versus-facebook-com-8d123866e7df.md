---
title: 'Étranges compagnons de lit : Phénomènes d''empreintes digitales… ou state.gov
  versus facebook.com'
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
seo_title: 'Étranges compagnons de lit : Phénomènes d''empreintes digitales… ou state.gov
  versus facebook.com'
seo_desc: 'By Nathan Reitinger

  When browsing the Internet, who do you trust more: facebook.com or state.gov?

  A knee-jerk reaction might be to pick state.gov — given Zuckerberg’s consistency
  in drumming up uncannily accurate advertisements and state.gov’s seemin...'
---

Par Nathan Reitinger

Lors de la navigation sur Internet, à qui faites-vous le plus **confiance** : [_facebook.com_](https://www.facebook.com) ou [_state.gov_](https://www.state.gov) ?

Une réaction spontanée pourrait être de choisir [state.gov](https://www.state.gov) — étant donné la constance de Zuckerberg à créer des [publicités](https://www.parliament.uk/business/committees/committees-a-z/commons-select/digital-culture-media-and-sport-committee/news/fake-news-report-published-17-19/) d'une précision déconcertante et le but apparemment inoffensif de state.gov. Ou peut-être pensez-vous que c'est simplement un « choix entre deux maux » et, acculé, vous seriez forcé de choisir le site web exploité par le gouvernement. Après tout, c'est quelque chose pour lequel vous avez, d'une manière ou d'une autre, voté, non ?

D'autres encore pourraient vouloir savoir quel devrait être le critère de confiance. Est-ce un test pour savoir qui protège le mieux mes secrets ([haveibeenpwned](https://haveibeenpwned.com)) ou qui est le plus susceptible de me voir comme un chiffre ([et attendez, combien](https://www.cnbc.com/2019/02/11/reddit-users-are-the-least-valuable-of-any-social-network.html?__source=facebook%7Cmain) vaut ce chiffre) ? Et d'autres encore pourraient essayer de creuser plus profond et définir la « confiance » d'un point de vue colloquial : **que fait ce site web sans me le dire ?**

Et ici, assez surprenant, nous trouvons une similitude.

Mais d'abord, un peu de contexte...

### Suivi

Parmi les nombreuses façons de « suivre » les visites sur les sites web — pourquoi est-ce que je vois des publicités pour des téléviseurs après les avoir recherchés sur Amazon, *oh attendez, c'est en fait une très bonne affaire* *[[clic clic clic](https://medium.freecodecamp.org/what-you-should-know-about-web-tracking-and-how-it-affects-your-online-privacy-42935355525)]* — les meilleures sont celles pour lesquelles vous n'avez pas besoin d'obtenir le consentement des utilisateurs. Parce que soyons honnêtes, si quelqu'un vous demande d'« accepter » un cookie ou des conditions de service, vous le ferez. Faites-moi confiance, j'ai dit « non » une fois et j'ai été renvoyé vers Google.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uy84g3WWZi_gsOfsO61fRQ.jpeg)
_[J❤️les cookies](https://www.juniqe.com/i-accept-cookies-framed-poster-2459619.html" rel="noopener" target="_blank" title=")_

Mais le point clé ici, au moins en termes de confiance, est la connaissance. Vous êtes maintenant, d'une manière ou d'une autre, *conscient* de succomber à ce que vous venez d'accepter. Espérons que vous n'aurez pas à [renoncer à votre enfant aîné](https://www.theguardian.com/technology/2014/sep/29/londoners-wi-fi-security-herod-clause) comme vous l'avez fait la dernière fois, mais pour la plupart, vous venez d'accepter que peu importe ce qui se passe sur le site web que vous visitez, rien de tout cela n'était de 'leur' faute.

> ...vous avez été pris en train de tromper votre femme à cause d'une faille de sécurité sur un site web — [ce n'est pas leur faute](https://www.forbes.com/sites/beltway/2015/10/22/ashley-madisons-online-terms-and-conditions-may-leave-it-legally-undressed/#2106932e6b40)

> ...vous êtes harcelé encore et encore parce que votre harceleur continue d'utiliser un faux profil de vous pour envoyer des hordes d'inconnus à votre lieu de travail — [ce n'est pas leur faute](https://www.buzzfeednews.com/article/tylerkingkade/grindr-herrick-lawsuit-230-online-stalking)

### Empreintes digitales

Pour éviter ce problème de connaissance potentiellement délicat, les développeurs de sites web peuvent préférer utiliser des techniques plus secrètes comme les empreintes digitales pour *identifier* les utilisateurs, de manière similaire à la façon dont les cookies identifient les utilisateurs.

D'accord, un autre rappel — qu'est-ce qu'un cookie ? Un cookie est comme un mot de passe secret que vous donnez aux membres de votre club secret. Personne ne passe la porte sans le mot de passe secret, mais au lieu d'utiliser un seul mot de passe, vous donnez à chaque membre son propre mot de passe spécial. Donc vous savez que le mot de passe de Bob est « periwinkle » et vous savez aussi que « periwinkle » a été utilisé soixante-dix fois le mois dernier ; woah, Bob, tu devrais probablement faire une pause du club.

![Image](https://cdn-media-1.freecodecamp.org/images/1*M-VvTkqsnN_UYG-Hiq-S-g.gif)
_Secret numéro 2 par Jerzy Wierzy_

De manière similaire, les empreintes digitales sont comme recueillir des détails sur Bob sans avoir besoin d'utiliser son compteur de mot de passe spécial. Essayez ceci :

> Il est un peu... corpulent. Pas du côté mince, mais plutôt du côté large. Il est aussi un peu orange, avec des cercles blancâtres autour des yeux. Ses cheveux sont d'un blond jaunâtre. Ses [cheveux](https://www.quora.com/How-would-people-describe-Donald-Trumps-physical-appearance-to-a-blind-person) ne semblent pas très réels. Ensuite, son visage, ridé.

Vous avez peut-être deviné que c'est Trump, mais une « supposition » ne serait pas assez bonne pour un propriétaire de site web. Au lieu de cela, vous avez besoin de beaucoup de détails uniques pour pouvoir dire définitivement « Je sais que c'est Trump, [ce ne pourrait être personne d'autre](https://panopticlick.eff.org). »

### La preuve est dans le pudding

Alors, quel est le rapport avec state.gov, facebook.com et le tweet du professeur Narayanan ? Eh bien, les trois sites web utilisent actuellement* des techniques d'empreintes digitales pour vous examiner.

Flatté que vous puissiez être, il est un peu étrange qu'une entreprise qui vous évalue à [7,37 $](https://www.cnbc.com/2019/02/11/reddit-users-are-the-least-valuable-of-any-social-network.html?__source=facebook%7Cmain) et un site web représentant notre Département d'État, #diplomacyinaction, utilisent les mêmes moyens sournois d'identification. Mais je m'égare, comment ai-je découvert cela ?

J'ai créé une extension Google Chrome à la recherche d'une technique très particulière utilisée dans les empreintes digitales (c'est-à-dire, l'empreinte digitale de canvas). J'ai exécuté l'extension dans un web-scraping Selenium et j'ai récupéré des données sur environ un demi-million de sites web, créant une base de données des tentatives d'empreintes digitales. Mon extension Chrome est essentiellement du même type que l'extension Chrome que le chercheur Gunes Acar a utilisée pour identifier les empreintes digitales sur ftc.gov (il a utilisé [CanvasFingerprintBlock](https://chrome.google.com/webstore/detail/canvasfingerprintblock/ipmjngkmngdcdpmgmiebdmfbkcecdndc?hl=en-US)).

Voici une requête SQL relative affichant l'utilisation par facebook de l'empreinte digitale de canvas :

![Image](https://cdn-media-1.freecodecamp.org/images/1*9SlnL76VNQcpcDP5-PiGZQ.png)
_image de canvas de facebook.com (extraite de la troncature par ellipsis)_

La chaîne dans la colonne de gauche est encodée en base64, mais je l'ai reconvertie en image pour voir à quoi elle ressemble, comme indiqué par la flèche.

En voici une autre pour state.gov :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYaj5q08J7mfGxXzwr6FdQ.png)
_image de canvas de state.gov (la même que celle de ftc.gov)_

Il s'avère que l'utilisation par Facebook d'un emoji révèle beaucoup de détails uniques sur l'utilisateur — comme avoir quelqu'un qui _gare la voiture dans la cour de Harvard [Yard](https://www.npr.org/2015/08/25/434668684/testing-boston-authenticity-with-park-the-car-on-harvard-yard)_. Il en va de même pour les mots imprimés par [ForeSee](https://www.foresee.com), une société d'analyse, bien que _M. Jock, TV quiz Ph-D, bags few lynx !_ aurait été mieux car c'est un pangramme presque parfait [parfait](https://english.stackexchange.com/questions/167709/a-perfect-honest-pangram-that-is-understandable-for-a-regular-native-user).

![Image](https://cdn-media-1.freecodecamp.org/images/1*1voDM5LY41y8toDea3fZag.png)
_image de canvas de lenscrafters.com_

Dans les deux cas, l'emoji et le texte ForeSee étrangement ombré ont été demandés à être dessinés par votre ordinateur — sans vous en informer — et tous deux fournissent beaucoup de détails uniques sur qui vous êtes. Une forme sournoise d'empreintes digitales.

### Et state.gov n'est pas seul !

Il y a en fait 304 sites web dans ma base de données qui utilisent la même image 'ForeSee' pour extraire l'unicité des utilisateurs. De plus, beaucoup d'entre eux utilisent le domaine de premier niveau .gov — il semble donc que ForeSee ait une bonne 'entrée' avec les sites web gouvernementaux.

### Donc ce que vous dites, c'est...

Peut-être que nous ne devrions faire confiance à aucun des deux sites web lorsqu'il s'agit de notre vie privée.

En conclusion, voici la liste complète des sites web utilisant cette image de canvas particulière — mais notez que le scraping a eu lieu pendant l'été 2018, donc certains des sites web peuvent avoir été mis à jour depuis. Si vous voulez reproduire ces résultats vous-même, utilisez Chrome avec l'extension [CanvasFingerprintBlock](https://chrome.google.com/webstore/detail/canvasfingerprintblock/ipmjngkmngdcdpmgmiebdmfbkcecdndc?hl=en-US)** et rendez-vous sur les URL listées.

```
https://www.dignityhealth.org/https://www.stagingclub.com/https://www.nemours.org/https://www.thankyou.com/cms/thankyouhttps://www.upmc.com/http://www.proflowers.com/https://www.coach.com/https://ucrdatatool.gov/https://www.aarp.org/aarp-foundation/https://www.bcbsm.com/https://www.barclays.co.uk/https://www.smithsonianmag.com/https://www.menswearhouse.com/https://www.jcpenney.com/https://www.sce.com/wps/portal/home/!ut/p/b1/04_Sj9CPykssy0xPLMnMz0vMAfGjzOIt3Q1cPbz8DTzdQwKNDTyNAw38gh0djQ0MzIAKIoEKDHAARwNC-sP1o8BK8JhQkBthkO6oqAgAStf4Iw!!/dl4/d5/L2dBISEvZ0FBIS9nQSEh/https://www.sodimac.cl/sodimac-cl/blackfridayhttps://www.unicare.com/health-insurance/home/overviewhttps://nij.gov/Pages/welcome.aspxhttps://kidshealth.org/https://www.autonation.com/https://www.fbfs.com/find-an-agenthttps://www.mass.gov/orgs/office-of-jury-commissionerhttps://www.argos.co.uk/https://www.billygoat.com/na/en_us/home.htmlhttps://www.hertz.ca/rentacar/reservation/https://www.josbank.com/https://www.pizzahut.com/https://www.npower.com/https://www.carhartt.com/https://www.briggsandstratton.com/na/en_us/home.htmlhttps://pioneervalley.aaa.com/https://www.basspro.com/shop/enhttps://www.ftc.gov/https://www.stanleyblackanddecker.com/https://www.hickoryfarms.com/http://www.clubmonaco.ca/home/index.jsp?geos=2https://www.avid.com/sibelius-ultimatehttps://www.amd.com/enhttp://www.abbott.com/https://myamerigroup.com/Pages/welcome.aspxhttps://www.spectrumbusiness.net/loginhttps://nortonhealthcare.com/https://valottery.com/https://www.comed.com/Pages/default.aspxhttps://www.rue21.com/store/https://www.bls.gov/https://www.allenedmonds.com/https://www.myprime.com/https://www.mass.gov/orgs/massachusetts-registry-of-motor-vehicleshttps://www.ferrismowers.com/na/en_us/home.htmlhttp://www.three.co.uk/https://glucerna.com/https://www.us.elsevierhealth.com/https://www.tui.co.uk/https://www.labcorp.com/https://nationalzoo.si.edu/?fonzref=index.htmlhttp://www.emdmillipore.com/US/en?RedirectedFrom=http%3A%2F%2Fmerckmillipore.com%2F&bd=1https://thebenefitsguide.com/https://www.childrensmn.org/https://www.verabradley.com/us/Homehttps://www.asu.edu/https://www.irs.gov/https://www.mass.gov/https://www.carecreditpay.com/pmyp/showSearchhttp://www.doingbusiness.org/http://www.kraftcanada.com/https://www.redfcu.org/https://www.marks.com/https://www.snapper.com/na/en_us/home.htmlhttp://www.emdmillipore.com/?RedirectedFrom=http://emdmillipore.com/https://www.humana.com/dental-insurancehttps://www.bge.com/Pages/default.aspxhttps://www.usps.com/https://myaccountrwd.allstate.com/anon/account/login?campaign=145https://www.dfs.co.uk/https://snb.com/https://www.royalcanin.com/https://www.epa.gov/https://www.dremel.com/en_US/https://www.snapfish.co.nz/store/homehttps://www.slu.edu/medicine/clinics-community/hrc/https://www.mazdausa.com/http://www.enviroflash.info/https://www.truevalue.com/https://ftccomplaintassistant.gov/#nbhttps://www.nationalcar.com/en/home.htmlhttps://www.mdanderson.org/https://www.ups.com/us/en/global.pagehttp://www.eatonpowersource.com/https://www.gatorade.com/https://www.uscis.gov/https://www.harlequin.com/shop/index.htmlhttps://myavista.com/https://www.bcbsga.com/https://montgomerycountymd.gov/https://www.spectrum.net/https://www.tricare-west.com/https://www.aarp.org/https://www.progressive.com/agent/https://www.bea.gov/https://www.makinghomeaffordable.gov/pages/default.aspxhttps://hnfs.com/https://www.simplicitymfg.com/na/en_us/home.htmlhttps://www.chop.edu/https://www.stouffers.com/enhttps://bjs.gov/https://www.e-verify.gov/https://www.hottopic.com/https://www.mynavyexchange.com/https://www.mcdonalds.com/us/en-us.htmlhttps://www.magazineluiza.com.br/http://www.cooperindustries.com/content/public/en.htmlhttp://www.slu.edu/https://www.smilemakers.com/https://usitc.gov/https://www.humana.com/http://choa.org/https://www.colehaan.com/https://www.snapfish.co.uk/homehttp://girlshealth.gov/https://www.homecenter.com.co/homecenter-co/https://thunderbird.asu.edu/https://www.northernnewengland.aaa.com/?zip=03766&stateprov=nh&city=lebanon&devicecd=PChttps://www.ugi.com/https://www.verizonwireless.com/tablets/asus-zenpad-z8s/#sku=sku2600003?cmp=cse-Shopping-ASUS-P00J&cmp=CSE-C-HQ-NON-R-AC-NONE-NONE-2C0PX0-PX-EBAY-ASUS-P00J&cvosrc=cse.EBAY.ASUS-P00J&cvo_crid={campaign}http://www.coldwatercreek.com/https://www.usajobs.gov/https://www.lg.com/us/mobile-phones/warrantyhttps://www.usbank.com/index.htmlhttps://www.stanfordchildrens.org/https://www.buffalowildwings.com/https://www.fanatics.com/https://ensure.com/https://www.realtor.ca/mlshttps://ttb.gov/https://www.nationalcar.com/en/home.html?action=emcIndexhttps://www.abercrombie.com/shop/ushttps://lifefitness.co.uk/https://www.lg.com/ushttps://www.thenorthface.com/https://www.constellation.com/https://www.purepoint.com/https://www.sba.gov/https://www.beaumont.edu/http://www.boden.co.uk/https://www.acehardware.com/https://www.uvmhealth.org/Pages/home.aspxhttps://www.falabella.com.co/falabella-co/https://mobiloil.com/enhttps://www.verizonwireless.com/?intcmp=vzwdomhttps://www.ftd.com/https://www.va.gov/https://www.francescas.com/https://nortonchildrens.com/https://teenshealth.org/en/teens/https://www.bloomingdales.com/http://www.cooperindustries.com/content/public/en/bussmann/electrical.htmlhttps://www.oakley.com/en-ushttps://www.avid.com/https://starbuckscollegeachievement.info/welcomehttps://www.serve.com/https://ieeeusa.org/https://www.la-z-boy.com/https://www.myhealthybluela.com/la/louisiana-home.htmlhttps://lifefitness.com/http://www.worldbank.org/https://www.smithsonianstore.com/https://www.lennox.com/https://www.qualcomm.cn/https://www.pbgc.gov/https://www.metroairport.com/https://www.vagisil.com/http://www.nationalrail.co.uk/https://www.coachoutlet.com/https://www.gmfleet.com/https://www.sec.gov/https://providentcu.org/index.asp?i=homehttps://www.hayward-pool.com/shop/en/poolshttp://www.cspire.com/https://www.famousfootwear.com/https://www.enfamil.com/https://www.steinmart.com/https://www.kcpl.com/https://www.progressivecommercial.com/https://www.boots.com/webapp/wcs/stores/servlet/TopCategoriesDisplay?catalogId=28501&langId=-1&storeId=11352&webrewrite=Y&geoOpts=Yhttps://www.sony.com/https://www.silverscript.com/https://www.falabella.com.pe/falabella-pe/https://www.marriottvacationclub.com/https://www.flagstar.com//https://www.hertz.com/rentacar/reservation/https://www.nordstromrack.com/http://www.morethantired.com/https://www.homedepot.ca/en/home.htmlhttps://carecredit.com/https://www.cspire.com/business/https://www.patelco.org/https://www.ralphlauren.com/https://www.berries.com/https://www.gci.com/https://www.beaumont.org/https://www.barneyswarehouse.com/https://www.verizonwireless.com/smartphones/google-pixel-2/#sku=sku2690617?cmp=cse-Shopping-GA00141-US&cmp=CSE-C-HQ-NON-R-AC-NONE-NONE-2C0PX0-PX-EBAY-GA00141-US&cvosrc=cse.EBAY.GA00141-US&cvo_crid={campaign}https://www.state.gov/http://www.naturemade.com/#vtrlbl4lQ6UOFkCi.97https://www.avmed.org/https://www.anthem.com/https://www.caringbridge.org/https://www.mydreampool.com/https://www.snapfish.com/photo-gift/homehttps://www.progressive.com/https://www.airspacemag.com/https://www.sony.es/https://voegol.com.br/pthttps://www.personalcreations.com/https://www.ssfcu.org/https://www.subaru.com/https://www.virginatlantic.com/us/enhttps://www.qualcomm.com/https://www.nhtsa.gov/https://www.barneys.com/https://www.autotrader.com/https://www.nflshop.com/https://www.si.edu/https://www.smithsonianjourneys.org/https://stanfordhealthcare.org/https://www.sony.co.uk/https://www.findlaw.com/https://www.allrecipes.com/https://www.falabella.com/falabella-cl/http://www.naturemade.com/supplements/folic-acid?&utm_content=addotnet_11165150-AIjWvqOWintQjLiqLHeEtQ#H1kJKcPEe0zLLUck.97https://www.theglobeandmail.com/https://www.k12.com/http://www.calgary.ca/SitePages/cocis/default.aspxhttps://www.moderncoinmart.com/https://www.citipricerewind.com/https://www.uspto.gov/https://login.usajobs.gov/Access/Transitionhttps://www.bluebird.com/https://www.peco.com/Pages/default.aspxhttps://treasurydirect.gov/https://www.enterprisecarsales.com/https://www.horizonblue.com/https://unicor.gov/index.aspxhttp://www.ladyfanatics.com/https://www.oakleysi.com/en-ushttps://shop.nordstrom.com/https://www.proplants.com/https://www.allinahealth.org/https://www.blinds.com/https://www.asuprepdigital.org/http://www.bathandbodyworks.com/https://pediasure.com/https://www.fbfs.com/https://www.wrangler.com/https://www.usmint.gov/https://www.messa.org/https://www.empireblue.com/http://www.bodenusa.com/https://www.walgreens.com/https://www.cdse.edu/https://www.naturalizer.com/https://www.ieee.org/https://thebenefitsguide.com/why-are-gen-xers-falling-behind-on-health-care/http://www.epymtservice.com/index.htmlhttps://www.imf.org/external/index.htmhttps://www.allrecipes.com/recipes/17235/everyday-cooking/allrecipes-magazine-recipes/https://www.vanguardengines.com/na/en_us/home.htmlhttp://www.brittany-ferries.co.uk/https://www.verybestbaking.com/https://www.youngliving.com/vo/#/login/culture/en-UShttps://www.torrid.com/homepagehttp://www.uscourts.gov/https://www.maybelline.com/https://www.keurig.ca/http://trieagleenergy.com/https://www.bareminerals.com/https://www.caremark.com/wps/portalhttps://www.alliancerxwp.com/http://www.thecompanystore.com/https://www.boschtools.com/us/en/https://www.fedshirevets.gov/https://pedialyte.com/https://www.womenshealth.gov/https://www.realtor.ca/https://www.justformen.com/https://www.burlington.com/https://www.ovc.gov/https://uvahealth.com/https://www.sodimac.com.pe/sodimac-pe/https://www.timberland.com/https://www.hopkinsmedicine.org/https://www.hautelook.com/http://www.clubmonaco.com/home/index.jsphttps://catalog.usmint.gov/bureau-of-engraving.htmlhttps://www.keurig.com/https://www.pepboys.com/https://www.interflora.co.uk/https://www.goya.com/en/https://www.bankatunion.com/https://www.bobcat.com/https://home.bluecrossma.com/https://www.talbots.com/online/https://www.cvsspecialty.com/wps/portal/specialty
```

* Au 15 février 2019, il semble que la version du code de ForeSee sur ftc.gov ne déclenche plus d'action d'empreinte digitale de canvas. Cependant, cela n'efface pas le fait que ForeSee continue d'utiliser cette technique sur d'autres sites gouvernementaux comme state.gov et uscourts.gov, et le fait que ftc.gov ait utilisé cette pratique par le passé.

** Ma version maison de l'extension Chrome varie légèrement de CanvasFingerprintBlock, donc vos résultats peuvent varier. Si vous voulez vraiment partir à la pêche, ouvrez l'inspecteur dans Chrome et recherchez `toDataUrl()` ; vous serez confronté à un barrage de javascript, mais c'est l'une des principales fonctions permettant d'utiliser le canvas comme outil d'empreinte digitale.