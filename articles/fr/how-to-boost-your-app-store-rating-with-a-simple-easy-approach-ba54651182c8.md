---
title: Comment améliorer la note de votre application sur l'App Store avec une approche
  simple et facile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-31T09:12:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-boost-your-app-store-rating-with-a-simple-easy-approach-ba54651182c8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9Ue8oEZUuEQoB0GNhf_n-Q@2x.jpeg
tags:
- name: Apple
  slug: apple
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment améliorer la note de votre application sur l'App Store avec une
  approche simple et facile
seo_desc: 'By Max Stein

  Users love to see high app ratings when deciding which apps to download. If two
  apps do the same thing, but one has a higher rating than the other, which one do
  you think most users would choose?

  Several of the most popular apps in the A...'
---

Par Max Stein

Les utilisateurs adorent voir des notes élevées pour les applications lorsqu'ils décident lesquelles télécharger. Si deux applications font la même chose, mais que l'une a une note plus élevée que l'autre, laquelle pensez-vous que la plupart des utilisateurs choisiraient ?

Plusieurs des applications les plus populaires de l'App Store ont vu leurs notes passer de la fourchette 3,5–4,5 à 4,8–5,0. En même temps, elles voient également leur nombre d'avis passer de 5 000–15 000 avis à 100 000–1 000 000 !

Par exemple, examinons Instagram :

![Image](https://cdn-media-1.freecodecamp.org/images/8Lr5yYEiB9lDCNekapz1ktftso1LG0YhPg3y)
_Instagram sur l'App Store iOS 11_

4,8 étoiles de la part de plus de 580 000 avis. Mais Instagram est une application énorme, il n'est donc pas difficile de comprendre pourquoi tant de personnes l'ont notée.

Examinons une application encore plus grande qu'Instagram — Facebook :

![Image](https://cdn-media-1.freecodecamp.org/images/ySiwYdiYVE7mGi5jwDCmTWjEFPNE1J577ciK)
_Facebook sur l'App Store iOS 11_

Facebook a une note de 3,0 étoiles de la part de seulement 14 500 utilisateurs. Comment Instagram a-t-il réussi à obtenir 40 fois plus d'utilisateurs pour noter son application alors que Facebook a [beaucoup plus d'utilisateurs](https://techcrunch.com/2017/06/27/facebook-2-billion-users/) qu'Instagram ?

### L'invite de notation d'Apple

La réponse réside dans le placement stratégique de [l'invite de notation native d'Apple](https://developer.apple.com/documentation/storekit/skstorereviewcontroller) :

![Image](https://cdn-media-1.freecodecamp.org/images/MhGynYb2eyuAuFQEVJYFSazGAFbS7TErndyt)

Avant l'existence de cette solution native, les développeurs devaient rediriger les utilisateurs vers l'App Store pour noter leurs applications. Maintenant, avec la solution d'Apple, les utilisateurs peuvent appuyer sur la note qu'ils souhaitent, appuyer sur soumettre, et c'est terminé !

Elle est disponible pour iOS 10.3 et versions ultérieures — vos utilisateurs iOS 10 ne seront donc pas laissés pour compte.

L'invite est très facile à ajouter et ne nécessite que quelques lignes de code :

```
// Ajoutez ceci près du haut de votre fichier
import StoreKit
```

```
// Placez ceci où vous souhaitez que l'invite d'avis apparaisse
SKStoreReviewController.requestReview()
```

#### Bien utiliser l'invite

Avant de vous lancer et de coller ceci n'importe où dans votre application, vous devez considérer votre base de clients. Où dans votre application pouvez-vous afficher cette invite pour permettre aux utilisateurs d'interagir avec elle de manière positive ?

Il n'y a pas de réponse unique à cette question, mais voici quelques idées :

* Pour les applications d'achat — après une ou plusieurs transactions réussies.
* Pour les applications de consommation de contenu — après une certaine période de temps. Ou, après X nombre de chansons/vidéos/livres terminés.
* Pour les applications de réseautage social — après qu'un utilisateur a créé du contenu. Ou, lorsqu'un utilisateur interagit avec le contenu de X autres personnes.

#### Points à garder à l'esprit

« Parce que cette méthode peut ou non présenter une alerte, il n'est pas approprié de l'appeler en réponse à un appui sur un bouton ou à une autre action de l'utilisateur. »
[https://developer.apple.com/documentation/storekit/skstorereviewcontroller/2851536-requestreview](https://developer.apple.com/documentation/storekit/skstorereviewcontroller/2851536-requestreview)

`requestReview()` retournera une invite basée sur la politique de l'App Store régie par Apple. Vous ne devez pas présenter une alerte au préalable demandant aux clients s'ils apprécient votre application. Si vous le faites, il est possible qu'ils ne voient pas d'invite de notation, ce qui entraînerait une mauvaise expérience utilisateur.

« Vous pouvez demander des notes jusqu'à trois fois en 365 jours. »
— [https://developer.apple.com/app-store/ratings-and-reviews/](https://developer.apple.com/app-store/ratings-and-reviews/)

L'invite de notation n'apparaîtra à un utilisateur que jusqu'à trois fois par an, même s'il met à jour votre application.

Cela ne pose pas autant de problèmes que dans les versions précédentes d'iOS. À partir d'iOS 11, Apple a modifié la manière dont les notes sont réinitialisées sur l'App Store.

Auparavant, chaque fois que vous soumettiez une nouvelle version à l'App Store, vos notes étaient réinitialisées. Maintenant, vous avez la possibilité de conserver votre historique de notes. Donc, si vous êtes satisfait de votre note, vous pouvez la garder !

Obtenir une note élevée sur l'App Store est l'un des moyens les plus efficaces d'augmenter vos téléchargements. Apple propose désormais une méthode facile, native et efficace pour améliorer la note de votre application. Profitez-en de manière intelligente et vous verrez certainement des résultats.

**Si vous avez aimé cette histoire, j'adorerais que vous cliquiez sur le bouton ? ci-dessous pour que plus de personnes puissent la découvrir. N'hésitez pas à partager dans les réponses également si vous avez utilisé cette invite dans votre application !**