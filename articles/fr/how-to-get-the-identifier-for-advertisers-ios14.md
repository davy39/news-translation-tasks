---
title: Comment obtenir l'identifiant pour les annonceurs (IDFA) dans iOS14
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2020-09-22T17:44:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-identifier-for-advertisers-ios14
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/0_oIyg9OzrsA2PiXHW.jpg
tags:
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment obtenir l'identifiant pour les annonceurs (IDFA) dans iOS14
seo_desc: "If the title of this article means something to you, then you are probably\
  \ aware of the earthquake caused by iOS14. \nWith the release of iOS14, there have\
  \ been major changes in the way applications can gather information about a user.\
  \ One of them dea..."
---

Si le titre de cet article vous dit quelque chose, alors vous êtes probablement conscient du séisme causé par iOS14. 

Avec la sortie d'iOS14, il y a eu des changements majeurs dans la façon dont les applications peuvent recueillir des informations sur un utilisateur. L'un d'eux concerne l'Identifiant pour les Annonceurs (ou IDFA) et la manière dont les applications peuvent y accéder. 

Mais pour ceux qui ne savent pas, expliquons d'abord ce qu'est l'IDFA et pourquoi il est important.

## Qu'est-ce qu'un IDFA?

Chaque propriétaire d'un appareil iOS peut décider s'il souhaite être suivi par des entreprises publicitaires. Cela permet à ces entreprises de fournir à l'utilisateur du contenu qui est adapté à ses besoins (en fonction de ses habitudes de navigation en ligne).

Les entreprises peuvent faire cela avec ce qu'on appelle un IDFA (Identifiant pour les Annonceurs). Il s'agit d'une chaîne [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#:~:text=A%20universally%20unique%20identifier%20(UUID,%2C%20for%20practical%20purposes%2C%20unique.) qui permet aux annonceurs d'associer l'utilisateur à son comportement.

Voici un exemple de chaîne UUID : 123e4567-e89b-12d3-a456-426614174000.

### Alors, quels sont ces changements dont nous avons parlé plus tôt?

En bref, les applications devront désormais afficher une boîte de dialogue à l'utilisateur, lui demandant s'il souhaite autoriser l'application à le suivre ou non.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screen-Shot-2020-09-17-at-22.35.25.png)
_La boîte de dialogue d'autorisation de suivi_

Cela semble assez menaçant, n'est-ce pas?

Cela contraste avec la façon dont les choses fonctionnaient avant iOS14, où vous deviez simplement vérifier si le suivi publicitaire était activé ou désactivé sur l'appareil.

La dernière version du système d'exploitation d'Apple (iOS14) est déjà disponible (depuis le 16 septembre). Les développeurs qui utilisent l'IDFA doivent apporter des modifications à leurs applications pour être compatibles avec iOS14. 

Le 3 septembre, Apple a fait une [mise à jour](https://developer.apple.com/news/?id=hx9s63c5%27) et a repoussé la date limite pour compléter ces mises à jour au début de l'année prochaine:

> "Pour donner aux développeurs le temps d'apporter les modifications nécessaires, les applications devront obtenir l'autorisation de suivre les utilisateurs à partir du début de l'année prochaine"

Maintenant que nous avons un peu de temps pour retrouver notre calme et respirer à nouveau, commençons à nous préparer pour ce qui sera la nouvelle norme en 2021. 

Dans cet article, nous présenterons quelques informations sur l'IDFA et verrons comment nous pouvons obtenir sa valeur à partir d'iOS14 et au-delà.

## Comment l'IDFA est-il utilisé par les annonceurs?

Prenons un scénario (avant le COVID-19) où vous naviguez sur le web avec votre iPhone et cherchez un hôtel pour vos prochaines vacances. 

Chaque publicité que vous voyez enverra un pixel avec votre IDFA attaché. Un annonceur peut voir que vous regardez beaucoup de publicités promouvant des hôtels en associant votre IDFA et en conclure que vous cherchez à réserver une chambre d'hôtel. 

À partir de là, il ne faudra pas longtemps avant que vous ne voyiez beaucoup de publicités pour des chambres d'hôtel.

Cette technologie simple mais profonde est entrée dans nos vies en 2012 avec iOS6. Depuis, beaucoup de choses ont changé, et iOS14 bouleverse à nouveau l'industrie.

📝 Note : _Pour utiliser ces nouvelles API, vous devez avoir mis à niveau/téléchargé XCode 12_.

## Suivi publicitaire et obtention de l'IDFA

Avant iOS14, obtenir l'IDFA était assez simple.

Vous deviez vérifier si le [Suivi Publicitaire](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-isadvertisingtrackingenabled) était activé ou non, en faisant ceci:

```[[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled]```

Et s'il était désactivé, cela signifiait que vous pouviez acquérir l'IDFA via la classe [ASIdentifierManager](https://developer.apple.com/documentation/adsupport/asidentifiermanager), comme ceci:

```[[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];```

Assez simple, n'est-ce pas?

⚠️ À partir d'iOS10, si l'utilisateur désactivait le suivi publicitaire, la méthode ci-dessus retournait une chaîne UUID remplie de zéros.

L'un des changements dans iOS14 est la dépréciation de la méthode qui vérifie si le suivi des annonceurs est activé ou non. Alors, comment les applications peuvent-elles obtenir le précieux IDFA à partir d'iOS14 et au-delà?

Elles devront utiliser une nouvelle API qui présente une boîte de dialogue à l'utilisateur. Quelques mots de sagesse concernant cette boîte de dialogue:

* Elle ne peut être présentée à l'utilisateur qu'une seule fois
* La seule chose qui peut être modifiée dans l'interface utilisateur de la boîte de dialogue sont les deux lignes au-dessus de l'option Autoriser le suivi ("Souhaitez-vous être suivi?")

Cela signifie que les développeurs devront réfléchir longuement et sérieusement à la manière et au moment où ils présenteront le message à l'utilisateur.

## Statut d'autorisation

Avec iOS14, un nouveau framework a été créé appelé [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency?language=objc). Ce framework contient une classe appelée [ATTrackingManager](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager?language=objc), qui fournit une API pour:

1. Présenter une boîte de dialogue à l'utilisateur demandant l'autorisation de le suivre
2. Interroger le statut d'autorisation (que la boîte de dialogue soit affichée ou non)

Nous allons d'abord apprendre comment obtenir le statut d'autorisation. Pour ce faire, vous devez appeler la méthode **trackingAuthorizationStatus**.

```ATTrackingManagerAuthorizationStatus status = [ATTrackingManager trackingAuthorizationStatus];```

Elle retournera un NSUInteger avec l'une des valeurs suivantes:

* ATTrackingManagerAuthorizationStatusNotDetermined = 0
* ATTrackingManagerAuthorizationStatusRestricted = 1
* ATTrackingManagerAuthorizationStatusAuthorized = 3
* ATTrackingManagerAuthorizationStatusDenied = 2

Les trois premiers résultats sont assez explicites, donc nous allons nous concentrer un instant sur le dernier.

Vous pouvez obtenir un statut d'autorisation restreint lorsque l'écran pour activer/désactiver le suivi publicitaire est verrouillé et que cette option est définie sur activé.

Apple a reconnu cela sur les appareils identifiés comme appartenant à des enfants (par exemple).

## Demander l'autorisation de suivre

Avant de regarder le code nécessaire pour présenter la boîte de dialogue, vous devez d'abord inclure la clé **NSUserTrackingUsageDescription** dans votre fichier info.plist. 

Ce que vous ajoutez comme valeur pour cette clé apparaîtra comme les deux lignes mentionnées précédemment, dans la boîte de dialogue.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screen-Shot-2020-09-17-at-22.29.31.png)
_**NSUserTrackingUsageDescription dans le fichier info.plist**_

Pour présenter la boîte de dialogue, nous devons appeler [requestTrackingAuthorizationWithCompletionHandler](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/3547037-requesttrackingauthorizationwith?language=objc):

```
[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:^(ATTrackingManagerAuthorizationStatus status) {
        if (status == ATTrackingManagerAuthorizationStatusDenied) {
            //Logique lorsque le statut d'autorisation est refusé
        } else if (status == ATTrackingManagerAuthorizationStatusAuthorized) {
            //Logique lorsque le statut d'autorisation est autorisé
        } else if (status == ATTrackingManagerAuthorizationStatusNotDetermined) {
            //Logique lorsque le statut d'autorisation est inconnu
        }  else if (status == ATTrackingManagerAuthorizationStatusRestricted) {
            //Logique lorsque le statut d'autorisation est restreint
        }
    }];
```

Dans la première image de cet article (où vous voyez la boîte de dialogue), vous pouvez voir que les lignes que nous avons écrites dans le fichier info.plist apparaissent comme les deux lignes dans la boîte de dialogue.

## Conclusion

En conclusion, il est important de se rappeler que ces changements, bien qu'intimidants, ne se produisent pas immédiatement. 

Vous devez également vous assurer de suivre toutes les étapes détaillées dans cet article afin de ne pas rencontrer de plantages/erreurs dans vos applications.