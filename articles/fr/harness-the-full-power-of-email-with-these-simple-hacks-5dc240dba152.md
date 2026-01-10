---
title: Exploitez tout le pouvoir de l'email avec ces astuces simples
subtitle: ''
author: Nikita Savchenko
co_authors: []
series: null
date: '2017-08-28T13:09:39.000Z'
originalURL: https://freecodecamp.org/news/harness-the-full-power-of-email-with-these-simple-hacks-5dc240dba152
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2czgFeeJ6ftdfDf90XO7dg.jpeg
tags:
- name: development
  slug: development
- name: email
  slug: email
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Exploitez tout le pouvoir de l'email avec ces astuces simples
seo_desc: 'Let’s talk about some email features that are surprisingly under-used,
  and that can really benefit you — if you know how to use them. This article is suitable
  for both users and developers who want to become email Jedi.

  Hack #1: Multiple email addres...'
---

Parlons de certaines fonctionnalités d'email qui sont étrangement sous-utilisées, et qui peuvent vraiment vous être bénéfiques — si vous savez comment les utiliser. Cet article est adapté aux utilisateurs ainsi qu'aux développeurs qui veulent devenir des Jedi de l'email.

### Astuce #1 : Plusieurs adresses email dans un seul compte

Avez-vous déjà voulu vous inscrire plusieurs fois sur un site web, tout en gardant la même boîte de réception pour tous les comptes ? Cette astuce simple fonctionne avec environ 95 % des sites web et services à travers le monde. Même sur Twitter et Instagram.

Certains fournisseurs d'email, comme gmail.com ou live.com, vous permettent de mettre un point supplémentaire entre les lettres de l'adresse email. Cela ne change rien sauf l'apparence de l'adresse.

Par exemple, disons que vous possédez **letgrandmaseat@gmail.com**. Vous possédez également **let.grandma.seat@gmail.com**, **let.grandmas.eat@gmail.com**, **l.e.t.g.r.a.n.d.m.a.s.e.a.t@gmail.com**, et ainsi de suite. Tous les emails envoyés à ces adresses apparaîtront dans la même boîte de réception. Vous pouvez également envoyer des emails en utilisant n'importe laquelle de ces adresses — il suffit de [quelques configurations](https://support.google.com/a/answer/22370).

Cela vous permet de changer l'apparence d'une adresse email et d'utiliser n'importe laquelle des itérations comme une adresse "nouvelle" valide. Par exemple :

* Vous pouvez vous inscrire plusieurs fois sur des sites web en utilisant le même compte email
* Vous pouvez partager différentes formes de votre adresse email avec différentes personnes. Ainsi, lorsque vous recevez des emails d'inconnus, vous pouvez découvrir comment les expéditeurs ont appris votre adresse email.

De plus, certains fournisseurs d'email vous permettent d'ajouter un signe plus à votre adresse suivi de n'importe quelle chaîne arbitraire :

* **let.grandmas.eat+your.soup@gmail.com**
* **let.grandma.seat+a.baby@gmail.com**

Cela augmente le nombre de variations possibles d'adresses email presque à l'infini.

Cela peut être extrêmement utile pour regrouper vos emails entrants. Vous pouvez [configurer une règle](https://support.google.com/inbox/answer/6067566) pour regrouper les emails différemment selon l'adresse dont ils proviennent. Par exemple, vous pouvez vous inscrire sur certains sites web mineurs en utilisant l'adresse **letgrandmaseat+trash@gmail.com**. Ensuite, vous pouvez configurer une règle de boîte de réception pour déplacer tous ces emails entrants vers la boîte "Faible Priorité".

De nombreux services offrant une version d'essai de leurs produits acceptent différentes formes du même compte email. Cela signifie que vous pouvez vous inscrire encore et encore, lorsque chaque essai se termine, pour obtenir un nouvel essai — tout avec le même compte email. Les développeurs ne peuvent pas faire grand-chose pour restreindre cela. Continuez à lire pour comprendre pourquoi.

### Astuce #2 : Plusieurs domaines peuvent faire référence au même compte

Si vous possédez une adresse **@gmail.com**, vous pouvez également utiliser n'importe quelle adresse **@googlemail.com** pour envoyer ou recevoir des emails. La plupart des sites web et services web traitent ces adresses email comme différentes. Cela vous permet de vous inscrire à plusieurs comptes en utilisant les deux formes d'une seule adresse email.

### Astuce #3 : Les adresses email peuvent être sensibles à la casse

Beaucoup de gens savent qu'il n'est généralement pas important d'écrire à **letgrandmaseat@gmail.com ou LetGrandmasEat@gmail.com**.

Mais il s'avère que la partie avant le @ peut être sensible à la casse. Cela est dû au fait qu'elle est entièrement sous le contrôle du système hôte. Selon la RFC 5321, section 2.3.11 :

> "La convention de nommage standard des boîtes aux lettres est définie comme étant 'partie-locale@domaine' ; l'usage contemporain permet un ensemble beaucoup plus large d'applications que de simples 'noms d'utilisateur'. Par conséquent, et en raison d'une longue histoire de problèmes lorsque les hôtes intermédiaires ont tenté d'optimiser le transport en les modifiant, la partie locale DOIT être interprétée et assignée sémantiquement uniquement par l'hôte spécifié dans la partie domaine de l'adresse."

Ainsi, si vous utilisez un domaine de luxe au lieu d'un domaine bien connu (comme gmail.com), il est préférable de garder l'adresse dans sa casse d'origine. Mais si vous avez fait une faute de frappe et que l'adresse résultante n'existe pas, vous recevrez probablement un email vous indiquant que votre message n'a pas été livré.

Ces conventions de nommage dépendent entièrement des systèmes hôtes. Techniquement, toute personne pouvant créer des serveurs email peut établir les règles de nommage qu'elle souhaite. Ils peuvent utiliser différents domaines qu'ils possèdent pour la même boîte aux lettres, autoriser ou refuser l'un des [caractères valides](https://en.wikipedia.org/wiki/Email_address#Local-part) dans les adresses email, et ainsi de suite.

### Astuce #4 : Services d'email "jetables"

Il existe quelques services qui vous permettent de créer une adresse email temporaire et [jetable](https://en.wikipedia.org/wiki/Disposable_email_address) gratuitement. Ceux-ci existent pour vous permettre d'accéder à des informations lorsque vous ne voulez pas vous inscrire en raison de préoccupations de confidentialité ou d'autres problèmes.

Et ces services sont utilisés par de nombreuses personnes. Vérifiez simplement la fréquence à laquelle [test@mailinator.com reçoit des emails](https://www.mailinator.com/v2/inbox.jsp?zone=public&query=test), et la quantité de courrier indésirable sans intérêt qu'il reçoit.

Pour empêcher l'utilisation de faux emails, certains services utilisent différentes [solutions de validation d'email](https://www.accuwebhosting.com/blog/top-10-bulk-email-list-verification-validation-services-compared/). Et oui, elles aident dans certains cas. Il devient plus difficile de créer un ensemble d'adresses email qui contourneront les vérifications de validité. De nombreux robots et programmes de spam seront bloqués ici, ce qui est la raison pour laquelle ces services existent.

Les services de validation d'email semblent-ils être la solution aux problèmes de fraude ou de spam ? Dans la plupart des cas — oui. Mais pas pour tous les problèmes possibles, comme vous le lirez ensuite.

### Astuce #5 : Vous pouvez créer presque n'importe quelle adresse email gratuitement

Lorsque vous possédez un domaine, vous pouvez configurer un service email pour celui-ci. Il existe [quelques services](https://www.google.com/search?q=free+email+for+domain) qui vous permettent de le faire gratuitement. Et il existe [quelques fournisseurs](https://www.google.com/search?q=free+domain) qui fournissent des noms de domaine gratuits pour tout le monde.

Si vous pouvez suivre les instructions pour configurer un domaine et un email sur celui-ci, vous pouvez créer une adresse email **_any.name@any.domain.XY_** gratuitement. Les instructions détaillées pour configurer un tel email dépassent le cadre de cet article. Mais en résumé, la procédure ressemble à ceci :

1. Enregistrez un domaine [gratuit](https://www.google.com/search?q=free+domain) ou payant en remplissant un formulaire d'enregistrement typique.
2. Sélectionnez l'un des fournisseurs "email pour domaine" (par exemple, [Zoho](https://www.zoho.com/mail/)), et suivez [les instructions](https://www.zoho.eu/mail/help/adminconsole/email-hosting-setup.html) pour créer un compte email pour votre domaine.

Oui, c'est aussi simple que cela.

### Implications pour les utilisateurs d'email

En ajoutant des symboles spéciaux comme des points ou des signes plus à votre adresse email (pour certains fournisseurs d'email), vous pouvez en tirer le meilleur parti. Vous pouvez gérer les emails de groupe entrants et vous inscrire plusieurs fois sur certains sites. Et cela vous permet de mettre différentes formes de votre adresse sur votre carte de visite pour savoir la source des emails entrants.

Les [emails jetables](https://www.google.com/search?q=Disposable+email), ainsi que les [services de numéro de téléphone temporaire](https://www.google.com/search?q=temporary+phone+number), peuvent protéger votre vie privée lorsque vous devez vous inscrire sur un site web indésirable pour une raison quelconque.

Et enfin, de nos jours, n'importe qui peut enregistrer un nom de domaine gratuit et configurer un email sur celui-ci. Cela vous donne une adresse email unique, personnalisée et valide.

### Implications pour les développeurs

En résumé, il n'y a aucun moyen d'être complètement sûr que nous pouvons faire confiance à un email donné. Mais voici quelques pratiques qui peuvent réduire l'utilisation anormale d'une adresse email :

**1.** Stockez-vous les emails comme identifiants principaux dans la base de données, mais souhaitez-vous empêcher les utilisateurs de s'inscrire plusieurs fois sur votre service ? Si oui, vous pouvez utiliser [une bibliothèque comme celle-ci](https://www.npmjs.com/package/normalize-email) pour normaliser les adresses email avant de les stocker comme identifiants. [Cette bibliothèque](https://www.npmjs.com/package/normalize-email) supprime les points et les suffixes avec un signe plus selon différents fournisseurs d'email bien connus, met l'adresse en minuscules et corrige les noms de domaine en une seule forme (googlemail.com → gmail.com).

**2.** Si vous utilisez des bibliothèques qui normalisent les adresses email, laissez les utilisateurs garder leur adresse email sous la forme dans laquelle elle a été initialement saisie. Par exemple, si un utilisateur s'inscrit sur votre service avec **username+bank@googlemail.com**, assurez-vous que tous les emails sont envoyés uniquement à cette adresse. N'envoyez pas à l'adresse "normalisée" **username@gmail.com**.

**3.** Pour détecter les adresses email jetables, vous pouvez utiliser des bibliothèques open-source comme [celle-ci](https://www.npmjs.com/package/disposable-email). Vous pouvez également vous appuyer sur les services qui fournissent des API pour valider les adresses email. Il y a [plus de 2 000 domaines](https://github.com/ivolo/disposable-email-domains/blob/master/index.json) dans la liste !

J'espère que vous avez appris quelque chose de nouveau en lisant cet article. Si vous l'aimez, faites-le circuler sur Medium en appuyant sur le bouton "clap" autant de fois que vous le souhaitez.

Merci pour votre lecture !