---
title: 'Les sites web des compagnies aériennes ne se soucient pas de votre vie privée
  : suite - Emirates répond à mon article avec…'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-06T22:04:08.000Z'
originalURL: https://freecodecamp.org/news/privacy-leaks-round-trip-emirates-com-in-denial-7f99950bcdd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ETvXCCF1aTIj9Kial1iOhQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Les sites web des compagnies aériennes ne se soucient pas de votre vie
  privée : suite - Emirates répond à mon article avec…'
seo_desc: 'By Konark Modi

  Yesterday, The Register wrote about my exposé on the privacy failings of airline
  websites.

  When I published my original article last Friday, Emirates had failed to respond
  to my request for comments. But Emirates did respond to The Reg...'
---

Par Konark Modi

Hier, [The Register](https://www.theregister.co.uk/2018/03/05/emirates_dinged_for_slipshod_privacy_practices/) a écrit à propos de mon exposé sur [les manquements en matière de confidentialité des sites web des compagnies aériennes](https://medium.freecodecamp.org/how-airlines-dont-care-about-your-privacy-case-study-emirates-com-6271b3b8474b).

Lorsque j'ai publié mon article original vendredi dernier, Emirates n'avait pas répondu à ma demande de commentaires. Mais Emirates a répondu à The Register, avec la déclaration suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/xl6tmP46uZY7rYTwUAjVKdiGO1iUe1Fi56-6)
_Commentaire d'Emirates sur theregister.co.uk_

Leur déclaration n'est pas seulement vague — elle est factuellement incorrecte. Et je pense qu'il est de mon devoir professionnel de les dénoncer.

### **Une analyse de leur déclaration, et comment leur logique s'effondre lorsque l'on y réfléchit vraiment**

#### Problème #1

Emirates déclare d'abord : « Nous pouvons confirmer qu'aucune des vulnérabilités de sécurité mises en lumière ne permettra une violation (accès non autorisé) des données personnelles sur notre site web ou notre application mobile. »

Comment Emirates définit-il une violation ? Eh bien, le [Cambridge Dictionary](https://dictionary.cambridge.org/us/dictionary/english/data-breach) définit une violation de données comme suit :

> « Une occasion où des informations privées peuvent être vues par des personnes qui ne devraient pas pouvoir les voir. »

Dans sa [Politique de Confidentialité](https://www.emirates.com/english/sitetools/privacy_policy.aspx#), Emirates souligne l'importance de protéger les informations de référence de réservation :

![Image](https://cdn-media-1.freecodecamp.org/images/DRUrRwOdF8KCiBlvSk0qWoJ-GbrVRaDmIFF8)
_Politique de confidentialité mettant en évidence les risques de partage du numéro de référence de réservation._

**Mise à jour du 8 mars 2018 :** Un autre exemple montrant comment Emirates semble avoir oublié de suivre son propre conseil « gardez votre référence de réservation en sécurité » et envoie **toujours** celle-ci à Google Analytics depuis l'application mobile, via **key:cd8** (non masqué). J'ai masqué les champs sur l'image pour garantir la confidentialité.

![Image](https://cdn-media-1.freecodecamp.org/images/aCVUzJzm-yKZwhxuYTei-GlAfRKnfaD92Uhe)
_Envoi du PNR via le champ cd8 à Google Analytics._

Pour toute modification d'une réservation existante, un **numéro de référence de réservation** et un **nom de famille** suffisent. Il n'est pas nécessaire de vérifier qui a initialement effectué la réservation et si la personne apportant les modifications est autorisée à le faire ou non.

Emirates.com et la version mobile de l'application Emirates (6.1.0) permettent tous deux l'accès à leur section Gérer la réservation **uniquement** sur la base de ces deux points de données. Il s'agit d'une pratique standard dans les compagnies aériennes, et ce n'est pas le point de contention aux fins de cet article.

#### **Mais c'est là que cela devient préoccupant**

En date du 6 mars 2018, le numéro de référence de réservation et le nom de famille, parmi de nombreux autres points de données, sont toujours envoyés aux tiers implémentés. Crazy Egg, Boxever, Coremetrics ont-ils besoin du numéro de référence de réservation et du nom de famille pour afficher la carte thermique de la page ? Je ne le pense pas.

Voici le problème — transmettre les informations personnelles des utilisateurs à des tiers qui n'ont absolument pas besoin de ces informations pour rendre leurs services à Emirates « dans le but d'améliorer l'expérience de navigation en ligne ».

L'importance d'utiliser des liens HTTPS a été établie maintes et maintes fois par tous ceux qui comptent dans le domaine de la technologie. Les liens HTTP ne sont pas seulement vulnérables aux attaques de type Man-In-The-Middle, mais peuvent également souffrir de l'injection de données malveillantes.

Je ne suis pas sûr de la manière dont Emirates est suffisamment confiant pour « confirmer qu'aucune des vulnérabilités de sécurité mises en lumière dans l'article de M. Modi ne permettra une violation (accès non autorisé) des données personnelles sur notre site web ou notre application mobile » alors que track.emirates.email n'a toujours pas de SSL. Comment prévoient-ils d'éviter les attaques de type Man-in-The-Middle ?

#### Problème #2

Emirates déclare : « Bien que nous utilisions un certain nombre d'outils analytiques tiers sur nos sites dans le but d'améliorer l'expérience de navigation en ligne, nous examinons continuellement la manière dont ceux-ci sont implémentés. »

J'ai partagé dans l'article comment les informations de passeport et les détails de contact étaient auparavant non obfusqués à la fois sur le site web et l'application mobile. Bien que le site web ait été corrigé lorsque j'ai vérifié pour la dernière fois en février 2018, l'application mobile continue d'être problématique dans ce domaine. Cela ne peut se produire que lorsqu'il y a un manque de communication entre l'équipe de développement du site web et celle de l'application mobile, ou qu'ils n'ont pas « examiné continuellement l'implémentation » sur tous les produits.

Une autre question qui mérite d'être posée est de savoir quels sont les paramètres pour examiner l'implémentation des tiers. À moins que le mandat ne soit strictement de NE PAS divulguer de quelque type d'information utilisateur que ce soit, les examens pourraient porter sur n'importe quoi et n'auraient pas le moindre impact sur la sécurité et la vulnérabilité des informations utilisateur étant librement transmises aux tiers.

La dernière fois que ce problème a été signalé à Emirates, c'était en octobre 2017. Dans les 5 mois qui se sont écoulés depuis, ces problèmes n'ont pas été détectés par l'équipe d'examen. Peut-être ne sont-ils pas aussi « continus » qu'Emirates le prétend.

#### **Problème #3**

Emirates déclare : « Les clients peuvent en savoir plus sur la manière dont nous utilisons les données personnelles et sur la manière dont ils peuvent se désinscrire en lisant notre politique de confidentialité sur emirates.com. »

![Image](https://cdn-media-1.freecodecamp.org/images/EyIuQm2i40qJNliIU6mixG5QD3EBvjyD1f27)
_Tiers répertoriés sur la page de la politique de confidentialité._

![Image](https://cdn-media-1.freecodecamp.org/images/PANiBbCzm2U6CbxfznZjQwfuEteBTSYRcvrR)
_Tiers réellement présents._

Après un examen approfondi de la [Politique de Confidentialité et des Cookies d'Emirates](https://www.emirates.com/english/sitetools/privacy_policy.aspx), voici les points à noter :

1. Elle ne répertorie pas **TOUS** les tiers implémentés et les informations partagées avec eux. Des tiers comme Boxever, ads-twitter.com, Coremetrics, Imigix, bing et bien d'autres que j'avais agrégés depuis leur site web ne sont même pas mentionnés dans leur politique de confidentialité.

2. Les options de désinscription disponibles ne mentionnent que des moyens utilisant des cookies, YourOnlineChoices. Cela signifie que non seulement les informations fournies dans la politique de confidentialité sont incomplètes, mais qu'elles ne partagent également aucune option pour se désinscrire des services CrazyEgg, BoxEver, Coremetrics, etc. Le processus est fastidieux et laborieux.

3. L'option de désinscription est biaisée en fonction du pays de résidence des utilisateurs. Si vous êtes résident de l'UE, vous pouvez utiliser ce lien pour vous désinscrire. Si vous êtes résident des États-Unis, voici le lien pour vous désinscrire. Mais si vous êtes résident d'une autre région, je suis désolé de vous apprendre que vous avez été lésé.

![Image](https://cdn-media-1.freecodecamp.org/images/tDl-3ATYivfyZTuq-TXReJZ2lgtXVkefX2RI)

4. Se désinscrire des cookies n'aura aucun impact sur les fuites de données mises en lumière dans l'article, car le référent n'est pas nettoyé. Toute personne ayant des connaissances techniques de base peut confirmer cela.

### **En résumé**

Même si l'utilisateur parvient d'une manière ou d'une autre à se désinscrire de tous les trackers en utilisant les méthodes répertoriées et non répertoriées, Emirates continuera de divulguer la référence de réservation et le nom de famille, ce qui est suffisant pour accéder à toutes les autres informations sensibles, car l'implémentation de ces services tiers sur Emirates.com est défectueuse.

Emirates doit comprendre que, une fois les informations partagées avec des tiers, il y a très peu de choses qu'ils peuvent faire pour contrôler la manière dont elles sont utilisées ou pourraient être utilisées à l'avenir, comme ils l'ont eux-mêmes mentionné dans leur politique de confidentialité.

**Il est une chose pour Emirates de penser que ces problèmes ne sont pas suffisamment critiques pour qu'ils prennent les mesures nécessaires pour les corriger. C'en est une autre de dire que les informations partagées dans l'article sont « non vraies ».**

J'espère qu'ils corrigeront ces problèmes le plus tôt possible.

Bonne exploration !

[- Konark Modi](https://twitter.com/konarkmodi)

Merci d'avoir lu et partagé ! :)

Si vous avez aimé cette histoire, n'hésitez pas à ??? plusieurs fois (Jusqu'à 50 fois. Sérieusement).

_Crédits : Un merci spécial à [Remi](https://twitter.com/Pythux), [Pallavi](https://twitter.com/Pi_Modi) pour avoir également relu cet article :)_