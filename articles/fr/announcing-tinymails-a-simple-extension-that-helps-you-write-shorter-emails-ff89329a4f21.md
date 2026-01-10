---
title: 'Comment j''ai construit TinyMails : une extension Chrome qui vous aide à écrire
  des emails plus courts'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-07T14:49:13.000Z'
originalURL: https://freecodecamp.org/news/announcing-tinymails-a-simple-extension-that-helps-you-write-shorter-emails-ff89329a4f21
coverImage: https://cdn-media-1.freecodecamp.org/images/1*th13skTPFs53EtCuupOYQA.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Comment j''ai construit TinyMails : une extension Chrome qui vous aide
  à écrire des emails plus courts'
seo_desc: 'By Florent Crivello

  I’ve been complaining about the death of brevity for a while now. Personal correspondence
  — especially emails — are as verbose as ever.

  Some of this is because it’s now much easier to generate a lot of content (computers
  are faste...'
---

Par Florent Crivello

Je me plains de la mort de la brièveté depuis un certain temps. Les correspondances personnelles — surtout les emails — sont aussi verbeuses que jamais.

Une partie de cela est due au fait qu'il est désormais beaucoup plus facile de générer du contenu (les ordinateurs sont plus rapides que les machines à écrire, qui sont plus rapides que l'écriture manuscrite).

Lorsque vous rédigez un email, vos clients de messagerie vous accueillent avec un Grand Champ de Texte qui semble dire : « C'est le moment d'écrire ce roman dont vous rêvez ! » Comparez cela au champ de texte ridiculement petit des applications de messagerie instantanée (en bleu) :

![Image](https://cdn-media-1.freecodecamp.org/images/SZ5aWUYN3GAm2iAzkihLnSFonAHBOVBeT32g)

Certes, les emails sont plus riches en contenu que les messages instantanés, mais je pense aussi que les gens seraient incités à écrire des emails beaucoup plus courts si cette boîte était plus petite (et s'agrandissait automatiquement au fur et à mesure que vous tapez, comme dans Facebook Messenger).

Ainsi, dans l'esprit de « ne vous plaignez pas de X, construisez Y à la place », j'ai construit [TinyMails](https://www.producthunt.com/posts/tinymails), ma première extension Chrome. Lorsque vous rédigez un email, TinyMails vous indique combien de mots vous avez écrits, ainsi qu'une estimation du temps qu'il faudra pour le lire. Il rend également progressivement le texte de l'estimation de plus en plus rouge à mesure que l'email devient de plus en plus long.

![Image](https://cdn-media-1.freecodecamp.org/images/BDk7vqUQjOvbVKPLtCOAK-B1zpfWwNyVzgsT)

Vous pouvez le télécharger ici sur le [Chrome WebStore](https://chrome.google.com/webstore/detail/tinymails/flpmjncnhickgfkjgmeloenfjgpgcpni), voter pour lui [sur ProductHunt](https://www.producthunt.com/posts/tinymails), et l'envoyer de manière passive-agressive à toutes les personnes que vous connaissez qui ont tendance à être verbeuses dans leurs emails (pour ma part, j'ai ajouté un lien à ma signature).

### Les détails techniques

Pour les curieux, j'ai mis [la source de l'extension ici sur GitHub](https://github.com/Altimor/TinyMails). J'ai utilisé l'incroyable [InboxSDK](https://www.inboxsdk.com), qui offre une API de haut niveau pour gérer Gmail / Inbox, me permettant de me concentrer sur la logique réelle de mon extension, et de la construire en 2 ou 3 heures.

Alors que je codais et en faisais le profilage, j'ai remarqué qu'il était beaucoup plus gourmand en calculs que je ne l'avais pensé. Une partie de cela est simplement JavaScript qui est JavaScript. Mais je fais aussi cette chose où — à chaque fois qu'une touche est pressée — je clone l'ensemble du DOM du champ de texte de composition afin de pouvoir supprimer la signature du compte de mots. Il s'avère que cela n'est pas trivial, alors j'ai fait en sorte que cela se fasse au maximum 5 fois par seconde. C'est suffisamment fréquent pour sembler en temps réel, mais plus économe en énergie que le comportement précédent.

N'hésitez pas à me contacter sur Twitter ([@Altimor](https://twitter.com/Altimor)) pour des commentaires/suggestions, et laissez un avis si vous l'aimez :)