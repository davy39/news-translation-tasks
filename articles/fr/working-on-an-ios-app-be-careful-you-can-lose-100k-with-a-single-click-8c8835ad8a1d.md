---
title: Vous travaillez sur une application iOS ? Faites attention à ceci.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-29T19:06:33.000Z'
originalURL: https://freecodecamp.org/news/working-on-an-ios-app-be-careful-you-can-lose-100k-with-a-single-click-8c8835ad8a1d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Yr4cMTyueBsyThzsN31J-g.jpeg
tags:
- name: Apple
  slug: apple
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Vous travaillez sur une application iOS ? Faites attention à ceci.
seo_desc: 'By Kevin Natanzon

  Integrating certain SDKs can have irreversible consequences


  At Beta Labs, we’ve been building apps for a long time. Throughout our journey,
  we created many apps that reached the Top 10 charts and that were used by millions
  of users...'
---

Par Kevin Natanzon

#### Intégrer certains SDK peut avoir des conséquences irréversibles

![Image](https://cdn-media-1.freecodecamp.org/images/6ocmURQGtecBZ9tJ2DaiJUkBCgv2Cy4jggdo)

Chez [Beta Labs](http://beta.uy), nous développons des applications depuis longtemps. Au cours de notre parcours, nous avons créé de nombreuses applications qui ont atteint le Top 10 des charts et qui ont été utilisées par des millions d'utilisateurs. Cependant, comme toute autre startup, nous avons également connu de nombreux échecs et revers.

Nous avons publié nos découvertes, nos insights et nos apprentissages autant que possible. Principalement parce que cela nous rend très heureux de savoir que nos histoires aident les autres à construire de meilleures choses en ligne. Beaucoup de créateurs, de fondateurs, de marketeurs et de développeurs nous ont contactés pour nous dire à quel point cela les avait aidés, et c'est génial ! Voici notre dernier article sur [Top Nine](http://Topnine.co) :

[**Top Nine devient viral !**](https://blog.beta.uy/top-nine-is-going-viral-1cef13033635)  
[_Annonce de la version Android_blog.beta.uy](https://blog.beta.uy/top-nine-is-going-viral-1cef13033635)

Aujourd'hui, nous voulons partager avec vous l'un de nos revers, avec pour objectif d'éviter à d'autres créateurs d'applications de ne pas prêter attention à quelque chose qui pourrait devenir un très gros problème à l'avenir.

### Le problème : Vous pouvez perdre plus de 100 000 $ avec un clic

Peut-être que ce titre était un peu accrocheur, mais imaginez que votre application vaut autant, et que quelqu'un veut l'acheter. Mais vous ne pouvez pas la vendre.

Il est vraiment important pour toute personne impliquée dans le développement d'une application iOS (marketeur, développeur, CEO, PM, etc.) d'être consciente de ce problème important :

> Si vous utilisez un jour l'autorisation Passbook dans votre application, vous ne pourrez jamais la transférer.

Voici ce que disent les documents d'Apple :

![Image](https://cdn-media-1.freecodecamp.org/images/1KC9nGJY1GJyA3oVJzdCZFigA9QjjnVRHkXc)
_[source](https://developer.apple.com/library/content/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/TransferringAndDeletingApps.html" rel="noopener" target="_blank" title=")_

Bien qu'il soit clair que toute version d'une application peut contenir Passbook pour être transférée, il n'y a aucun avertissement lorsque le développeur ajoute le framework au projet.

### Pourquoi le transfert d'une application serait-il si important ?

Pour de nombreuses raisons, mais en voici quelques-unes :

* Vous pouvez vouloir **vendre votre application** à une autre entreprise, tout en conservant votre compte développeur avec d'autres actifs.
* Vous pouvez avoir **commencé avec un compte développeur personnel** et continué avec un compte entreprise, où vous devez transférer les applications.
* Vous pouvez avoir **publié l'application sous le compte de quelqu'un d'autre** (comme votre société de développement), pour des raisons de simplicité.

### Nous l'avons appris à nos dépens

Il y a deux ans, à l'époque où nous ne savions pas grand-chose sur la manière de monétiser les applications, nous avons décidé d'intégrer la médiation Twitter MoPub. Nous pensions que le CPM serait élevé car le potentiel du SDK était vraiment grand, permettant les mêmes choses que ce que fait actuellement le [Facebook Audience Network](https://developers.facebook.com/products/audience-network/overview/).

Dans le cadre de l'intégration, nous avons suivi [ce tutoriel](https://www.mopub.com/resources/docs/ios-sdk-integration/ios-getting-started/) écrit par MoPub.

De plus, les réseaux tiers nécessitent :

* AudioToolbox.framework
* AVFoundation.framework
* Ad.framework
* MessageUI.framework
* MobileCoreServices.framework
* PassKit.framework
* Social.framework

En tant que développeur, tout ce que vous avez à faire est d'ajouter la bibliothèque au projet Xcode. Quel effet négatif cela pourrait-il avoir ?

![Image](https://cdn-media-1.freecodecamp.org/images/YZhEFYzg1-ugHoKty2vOWdvQXrtxm75XjjqM)

Quelques mois plus tard, nous avons réussi à positionner [cette application](https://blog.beta.uy/we-are-2-9a7318391630) à la première place pour les mots-clés "Vérité ou Défi", générant plus de 15 000 $ par mois grâce aux installations organiques — principalement des fêtards cherchant une application amusante.

Nous étions vraiment heureux de trouver un acheteur tôt, alors nous avons décidé de vendre "pas cher" pour un très bon montant. Après tout, un actif générant 15 000 $/mois vaut au moins six chiffres.

Le transfert de l'application était censé être très simple, car Apple fournit déjà un processus pour cela. Mais après avoir conclu un accord avec l'acheteur, nous nous sommes rendu compte que nous avions ajouté l'autorisation Passbook à un moment donné.

![Image](https://cdn-media-1.freecodecamp.org/images/OzizXcATKuzgAfElgkWXB4ryuzu3kuSKwR3X)

(Nous avons récemment intégré Passbook à [Top Nine](http://topnine.co) également, mais cette fois-ci, nous l'avons fait en connaissance de cause car c'est nécessaire pour intégrer Apple Pay)

Compléter un processus de paiement e-commerce en deux clics vaut la peine de ne pas pouvoir transférer l'application jusqu'à ce qu'il y ait un acquéreur qui décide d'acheter toute l'entreprise. Mais encore une fois, c'est un compromis que les développeurs devraient réfléchir soigneusement, et non réaliser qu'ils ont choisi par hasard de rendre leur application non transférable une fois qu'il est trop tard.

### Comment Apple pourrait résoudre ce problème

La meilleure (mais la moins probable) façon de résoudre ce problème serait de lever cette restriction complètement. C'est-à-dire, permettre aux applications d'être transférées même si elles ont intégré l'autorisation Passbook à un moment donné dans le passé. Nous avons essayé de pousser Apple à faire cela, mais après des années, nous n'avons pas eu de chance.

![Image](https://cdn-media-1.freecodecamp.org/images/dheKP1-VCmtrzB4CKVHqFYTt8osJ8fpxtgwt)

Si soutenir cela est difficile à réaliser pour une raison quelconque, tout ce que je demanderais est un avertissement clair des implications commerciales de l'ajout de cette bibliothèque au moment du développement. Intégrer le SDK Passbook est une décision qui ne doit pas être prise à la légère, donc si le développeur doit ajouter cette bibliothèque, je m'attendrais à ce que l'action nécessite des permissions élevées, ainsi qu'un petit avertissement :

![Image](https://cdn-media-1.freecodecamp.org/images/SvWh1ZE1ZpDG2x2ShF3-hjsQmj3WgOlhmoDF)

### Comment vous pouvez aider

Si vous lisez ceci, cela signifie que vous êtes impliqué dans le développement d'applications. Si c'est le cas, vous pouvez soit aider un ami dans le domaine, soit nous aider à faire en sorte qu'Apple résolve ce problème.

Si vous êtes un développeur iOS et que vous souhaitez aider, nous avons juste besoin que vous partagiez cet article sur Twitter avec le tweet suivant :

> Cher @Apple, pouvez-vous s'il vous plaît résoudre ce problème ? — [Tweetez ceci.](https://twitter.com/intent/tweet?ref_src=twsrc%5Etfw&text=Dear%20%40Apple%2C%20can%20you%20please%20fix%20this%3F&tw_p=tweetbutton&url=https%3A%2F%2Fmedium.com%2F%40kevntz%2Fworking-on-an-ios-app-be-careful-with-this-8c8835ad8a1d)

### Merci !