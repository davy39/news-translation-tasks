---
title: Que contient un en-tête d'email et pourquoi devriez-vous vous en soucier ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-29T04:06:00.000Z'
originalURL: https://freecodecamp.org/news/reading-email-headers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ab8740569d1a4ca274f.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: email
  slug: email
- name: email marketing
  slug: email-marketing
- name: information security
  slug: information-security
seo_title: Que contient un en-tête d'email et pourquoi devriez-vous vous en soucier
  ?
seo_desc: 'By Megan Kaczanowski

  Ever gotten a spam or phishing message from an email address you didn''t recognize?
  Maybe someone offered you a free trip, asked you to send them bitcoin in exchange
  for personal photos, or just sent you an unwanted marketing emai...'
---

Par Megan Kaczanowski

Avez-vous déjà reçu un spam ou un message de phishing d'une adresse email que vous ne reconnaissiez pas ? Peut-être que quelqu'un vous a offert un voyage gratuit, vous a demandé d'envoyer des bitcoins en échange de photos personnelles, ou vous a simplement envoyé un email marketing non sollicité ? 

Vous êtes-vous déjà demandé d'où venaient ces emails ? Avez-vous vu un spammer usurper votre adresse email et vous êtes-vous demandé comment ils avaient fait ? 

L'usurpation d'email, ou le fait de faire apparaître un email comme s'il venait d'une adresse différente de celle d'où il provient (par exemple, un email qui semble venir de whitehouse.gov, mais qui provient en réalité d'un escroc), est remarquablement facile. 

Les protocoles de base des emails n'ont aucune méthode d'authentification, ce qui signifie que l'adresse 'de' est essentiellement juste un champ à remplir.

Habituellement, lorsque vous recevez un email, il ressemble à ceci :

```
De : Nom <name@gmail.com>
Date : Mardi 16 juillet 2019 à 10h02
À : Moi <Me@freecodecamp.com>
```

En dessous se trouvent le sujet et le message.

Mais comment savez-vous d'où vient vraiment cet email ? N'y a-t-il pas de données supplémentaires qui peuvent être analysées ? 

Ce que nous cherchons, ce sont les en-têtes complets de l'email — ce que vous voyez ci-dessus n'est qu'un en-tête partiel. Ces données nous donneront des informations supplémentaires sur l'origine de l'email et sur la manière dont il a atteint votre boîte de réception. 

Si vous souhaitez examiner vos propres en-têtes d'email, voici comment y accéder sur [Outlook](https://support.office.com/en-us/article/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c) et [Gmail](https://support.google.com/mail/answer/29436?hl=en). La plupart des programmes de messagerie fonctionnent de manière similaire, et une simple recherche Google vous indiquera comment afficher les en-têtes sur d'autres services de messagerie. 

Dans cet article, nous examinerons un ensemble d'en-têtes réels (bien qu'ils soient fortement édités — j'ai modifié les noms d'hôtes, les horodatages et les adresses IP).

Nous lirons les en-têtes de haut en bas, mais sachez que chaque nouveau serveur ajoute son en-tête en haut du corps de l'email. Cela signifie que nous lirons chaque en-tête à partir du dernier Agent de Transfert de Message (MTA) et travaillerons jusqu'au premier MTA à accepter le message.

## Transferts internes

```
Reçu : de REDACTED.outlook.com (adresse IPv6) par REDACTED.outlook.com avec HTTPS via REDACTED.OUTLOOK.COM ; Ven 25 oct 2019 20:16:39 +0000
```

Ce premier saut montre une ligne HTTPS, ce qui signifie que le serveur n'a pas reçu le message via SMTP standard et a plutôt créé le message à partir d'une entrée reçue sur une application web.

```
Reçu : de REDACTED.outlook.com (IPv6Address) par REDACTED.outlook.com (IPv6Address) avec Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.1.1358.20 ; Ven 25 oct 2019 20:16:38 +0000

Reçu : de REDACTED.outlook.com (IPv6Address) par REDACTED.outlook.office365.com (IPv6Address) avec Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384) id 15.20.2385.20 via Frontend Transport ; Ven 25 oct 2019 20:16:37 +0000 Authentication-Results: spf=softfail (IP de l'expéditeur est REDACTEDIP)smtp.mailfrom=gmail.com ; privatedomain.com ; dkim=pass (la signature a été vérifiée)header.d=gmail.com ;privatedomain.com ; dmarc=pass action=noneheader.from=gmail.com ;compauth=pass reason=100Received-SPF: SoftFail (REDACTED.outlook.com: domaine de transition gmail.com décourage l'utilisation de l'adresse IP en tant qu'expéditeur autorisé)
```

Ce sont les deux premiers blocs d'en-tête qui sont des transferts de courrier internes. Vous pouvez voir que ceux-ci ont été reçus par des serveurs Office365 (outlook.com), et acheminés en interne au bon destinataire. 

Vous pouvez également voir que le message est envoyé via SMTP chiffré. Vous le savez parce que l'en-tête indique "avec Microsoft SMTP Server" puis spécifie la version TLS utilisée, ainsi que le chiffrement spécifique. 

Le troisième bloc d'en-tête marque la transition d'un serveur de messagerie local à un service de filtrage de messagerie. Vous le savez parce qu'il est passé "via Frontend Transport" qui est un protocole spécifique à Microsoft Exchange (et donc ce n'était pas strictement SMTP). 

Ce bloc inclut également certaines vérifications d'email. L'en-tête d'Outlook.com détaille ici leurs résultats SPF/DKIM/DMARC. Un SoftFail SPF signifie que cette adresse IP n'est pas autorisée à envoyer des emails au nom de gmail.com. 

"dkim=pass" signifie que l'email provient de son expéditeur prétendu et n'a (probablement) pas été altéré en transit.  

DMARC est un ensemble de règles indiquant au serveur de messagerie comment interpréter les résultats SPF et DKIM. Pass signifie probablement que l'email continue vers sa destination.

Pour plus d'informations sur SPF, DKIM et DMARC, consultez [cet article](https://www.freecodecamp.org/news/p/1fb5b1b8-7bd9-40fc-8a76-d64c979df748/www.freecodecamp.org/news/how-does-email-work/).

## Transition interne/externe

```
Reçu : de Redacted.localdomain.com (adresse IP) par redacted.outlook.com (adresse IP) avec Microsoft SMTPServer (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384) id15.20.2305.15 via Frontend Transport ; Ven 25 oct 2019 20:16:37 +0000

Received-SPF: None (Redacted.localdomain.com: aucune information d'authenticité de l'expéditeur disponible depuis le domaine de l'expéditeur@gmail.com) identity=xxx ; client-ip=IPaddress ;receiver=Redacted.localdomain.com ;envelope-from="sender@gmail.com" ;x-sender="sender@gmail.com" ; x-conformance=sidf_compatible


Received-SPF: Pass (Redacted.localdomain.com: domaine de l'expéditeur@gmail.com désigne l'IP d'envoi comme expéditeur autorisé) identity=mailfrom ; client-ip=IPaddress2 ;receiver=Redacted.localdomain.com ;envelope-from="sender@gmail.com" ;x-sender="sender@gmail.com" ; x-conformance=sidf_compatible ;x-record-type="v=spf1" ; x-record-text="v=spf1ip4:35.190.247.0/24 ip4:64.233.160.0/19 ip4:66.102.0.0/20ip4:66.249.80.0/20 ip4:72.14.192.0/18 ip4:74.125.0.0/16ip4:108.177.8.0/21 ip4:173.194.0.0/16 ip4:209.85.128.0/17ip4:216.58.192.0/19 ip4:216.239.32.0/19 ~all"
```

Ceci est l'enregistrement SPF de Google - indiquant au serveur récepteur que l'email qui prétend venir de gmail.com provient d'un serveur approuvé par Google.

```
Received-SPF: None (redacted.localdomain.com: aucune information d'authenticité de l'expéditeur disponible depuis le domaine de postmaster@redatedgoogle.com) identity=helo ;client-ip=IPaddress ; receiver=Redacted.localdomain.com ;envelope-from="sender@gmail.com" ;x-sender="postmaster@.google.com" ;x-conformance=sidf_compatibleAuthentication-Results-Original: Redacted@localdomain.com ; spf=None smtp.pra=sender@gmail.com ; spf=Pass smtp.mailfrom=sender@gmail.com ;spf=None smtp.helo=postmaster@redacted.google.com ; dkim=pass (signature vérifiée) header.i=@gmail.com ; dmarc=pass (p=none dis=none) d=gmail.comIronPort-SDR: IronPort-PHdr: =X-IronPort-Anti-Spam-Filtered: trueX-IronPort-Anti-Spam-Result: =X-IronPort-AV: ;d="scan"X-Amp-Result: SKIPPED(aucune pièce jointe dans le message)X-Amp-File-Uploaded: False
```

Cela montre certaines vérifications supplémentaires SPF/DKIM/DMARC, ainsi que les résultats d'un scan IronPort. 

Ironport est un filtre d'email populaire utilisé par de nombreuses entreprises pour rechercher des spams, des virus et d'autres emails malveillants. Il scanne les liens et les pièces jointes dans l'email et détermine si l'email est malveillant (et doit être supprimé), s'il est probablement légitime et doit être livré, ou s'il est suspect, auquel cas il peut attacher un en-tête au corps qui indique aux utilisateurs de se méfier de l'email.

```
Reçu : de redacted.google.com ([IPAddress]) par Redacted.localdomain.com avec ESMTP/TLS/ECDHE-RSA-AES128-GCM-SHA256 ; Ven 25 oct 2019 16:16:36 -0400

Reçu : par redacted.google.com avec SMTP id pour recipient@localdomain.com ; Ven 25 oct 2019 13:16:35 -0700 (PDT)

X-Received: par IPv6:: avec SMTP id ; Ven 25 oct 2019 13:16:35 -0700 (PDT) Return-Path: sender@gmail.com

Reçu : de senderssmacbook.fios-router.home (pool-.nycmny.fios.verizon.net. [adresse IP masquée]) par smtp.gmail.com avec ESMTPSA id IP masquée (version=TLS1 cipher=ECDHE-RSA-AES128-SHA bits=128/128) ; Ven 25 oct 2019 13:16:34 -0700 (PDT)

Reçu : de senderssmacbook.fios-router.home (pool-.nycmny.fios.verizon.net. [adresse IP masquée]) par smtp.gmail.com avec ESMTPSA id IP masquée (version=TLS1 cipher=ECDHE-RSA-AES128-SHA bits=128/128) ; Ven 25 oct 2019 13:16:34 -0700 (PDT)
```

Cette section montre les sauts internes que l'email a effectués depuis le périphérique initial de l'expéditeur jusqu'au système de routage de Gmail et à l'environnement Outlook du destinataire. De cela, nous pouvons voir que l'expéditeur initial était un Macbook, utilisant un routeur domestique, avec Verizon Fios à NYC. 

Ceci est la fin des sauts montrant le chemin que l'email a pris de l'expéditeur au destinataire. Passé cela, vous verrez le corps de l'email (et les en-têtes que vous voyez typiquement comme "de :", "à :", etc.), peut-être avec un certain formatage basé sur le type de média et le client de messagerie (par exemple la version MIME, le type de contenu, la frontière, etc.). Il peut également contenir certaines informations sur l'agent utilisateur, qui sont des détails sur le type de périphérique qui a envoyé le message. 

Dans ce cas, nous savons déjà que le périphérique d'envoi était un Macbook grâce à la convention de nommage d'Apple, mais il peut également contenir des détails sur le type de CPU, la version, même le navigateur et la version qui étaient installés sur le périphérique. 

Dans certains cas, mais pas tous, il peut également contenir l'adresse IP du périphérique d'envoi (bien que de nombreux fournisseurs masqueront cette information sans une assignation à comparaître).

## Que peuvent vous dire les en-têtes d'email ?

Les en-têtes d'email peuvent aider à identifier lorsque les emails ne sont pas envoyés par leurs expéditeurs prétendus. Ils peuvent fournir certaines informations sur l'expéditeur — bien que cela ne soit généralement pas suffisant pour identifier le véritable expéditeur. 

Les forces de l'ordre peuvent souvent utiliser ces données pour obtenir une assignation à comparaître auprès du bon FAI, mais le reste d'entre nous peut surtout l'utiliser pour aider à informer les enquêtes, généralement sur le phishing. 

Ce processus est rendu plus difficile par le fait que les en-têtes peuvent être falsifiés par des serveurs malveillants ou des pirates. Sans contacter le propriétaire de chaque serveur et vérifier individuellement que les en-têtes dans votre email correspondent à leurs journaux SMTP, ce qui est fastidieux et chronophage, vous ne serez pas certain que les en-têtes sont exacts (à l'exception des en-têtes attachés par vos propres serveurs de messagerie). 

Sans contacter le propriétaire de chaque serveur et vérifier individuellement que les en-têtes dans votre email correspondent à leurs journaux SMTP, ce qui est fastidieux et chronophage, vous ne serez pas certain que tous les en-têtes sont exacts. 

DKIM, DMARC et SPF peuvent tous aider dans ce processus, mais ne sont pas parfaits, et sans eux, il n'y a aucune vérification du tout.

Vous ne voulez pas analyser vos propres en-têtes ? [Ce site](https://mailheader.org/) le fera pour vous.