---
title: J'ai trouvé un moyen de pirater n'importe quel compte parmi les 2 milliards
  de comptes Facebook, et ils m'ont payé une prime de 15 000 $…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-09T11:41:36.000Z'
originalURL: https://freecodecamp.org/news/responsible-disclosure-how-i-could-have-hacked-all-facebook-accounts-f47c0252ae4d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YxD3C1C9qLsIGG4pqLv7ig.jpeg
tags:
- name: Facebook
  slug: facebook
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: J'ai trouvé un moyen de pirater n'importe quel compte parmi les 2 milliards
  de comptes Facebook, et ils m'ont payé une prime de 15 000 $…
seo_desc: 'By AppSecure

  I am publishing this with the permission of Facebook under the responsible disclosure
  policy. They have fixed this vulnerability.

  This post is about a simple vulnerability I discovered on Facebook which I could
  have used to hack into oth...'
---

Par AppSecure

Je publie ceci avec la permission de Facebook dans le cadre de la politique de divulgation responsable. Ils ont corrigé cette vulnérabilité.

Cet article parle d'une vulnérabilité simple que j'ai découverte sur Facebook, que j'aurais pu utiliser pour pirater facilement les comptes Facebook d'autres utilisateurs et sans aucune interaction de leur part.

Cela m'a donné un accès complet aux comptes d'autres utilisateurs en définissant un nouveau mot de passe. J'ai pu consulter les messages, leurs cartes de crédit/débit stockées dans leur section de paiement, les photos personnelles et d'autres informations privées.

Facebook a reconnu le problème rapidement, l'a corrigé et m'a récompensé avec une prime de 15 000 $ US en fonction de la gravité et de l'impact de cette vulnérabilité.

### Comment le piratage a fonctionné

Lorsqu'un utilisateur oublie son mot de passe sur Facebook, il a la possibilité de le réinitialiser en entrant son numéro de téléphone et son adresse e-mail sur [https://www.facebook.com/login/identify?ctx=recover&lwv=110](https://www.facebook.com/login/identify?ctx=recover&lwv=110&__mref=message).

Facebook envoie ensuite un code à 6 chiffres à ce numéro de téléphone ou à cette adresse e-mail, que l'utilisateur doit entrer pour définir un nouveau mot de passe.

J'ai essayé de forcer brutalement le code à 6 chiffres sur [www.facebook.com](http://www.facebook.com/?__mref=message) et j'ai été bloqué après 10 à 12 tentatives invalides.

J'ai ensuite cherché le même problème sur beta.facebook.com et mbasic.beta.facebook.com. Intéressamment, la limitation de taux était absente de l'endpoint de mot de passe oublié.

J'ai essayé de prendre le contrôle de mon propre compte (selon la politique de Facebook, vous ne devez pas causer de tort aux comptes d'autres utilisateurs) et j'ai réussi à définir un nouveau mot de passe pour mon compte. J'ai ensuite pu utiliser ce même mot de passe pour me connecter à mon propre compte piraté.

### Une vidéo de preuve de concept du piratage

Comme vous pouvez le voir dans la vidéo, j'ai pu définir un nouveau mot de passe pour l'utilisateur en forçant brutalement le code qui avait été envoyé à leur adresse e-mail et à leur numéro de téléphone.

### **Requête vulnérable**

`POST /recover/as/code/ HTTP/1.1`

`Host: beta.facebook.com`

`lsd=AVoywo13&n=XXXXX`

Le forçage brutal du « n » m'a permis de définir un nouveau mot de passe pour n'importe quel utilisateur Facebook.

### **Chronologie de la divulgation**

22 février 2016 : Rapport envoyé à l'équipe Facebook.

23 février 2016 : Vérification de la correction de mon côté.

2 mars 2016 : Prime de 15 000 $ attribuée par Facebook