---
title: 'Qu''est-ce que la NFC ? Communication en champ proche : utilisations, puces,
  tags et lecteurs expliqués'
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-03T18:00:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-nfc-near-field-communication-uses-chips-tags-and-readers-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9581740569d1a4ca0d5c.jpg
tags:
- name: finance
  slug: finance
- name: fintech
  slug: fintech
- name: payments
  slug: payments
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Qu''est-ce que la NFC ? Communication en champ proche : utilisations,
  puces, tags et lecteurs expliqués'
seo_desc: 'NFC is everywhere these days. You''ve probably seen it in your phone settings,
  or heard about it online.

  While the use of NFC for things like contactless payments was growing steadily,
  it exploded early this year due to the Coronavirus pandemic.

  In th...'
---

La NFC est partout de nos jours. Vous l'avez probablement vue dans les paramètres de votre téléphone, ou en avez entendu parler en ligne.

Bien que l'utilisation de la NFC pour des choses comme les paiements sans contact était en croissance régulière, elle a explosé plus tôt cette année en raison de la pandémie de Coronavirus.

Dans cet article, nous allons passer en revue ce qu'est la NFC, à quoi elle sert, quelques façons créatives d'utiliser la NFC, et plus encore.

## Qu'est-ce que la NFC et comment fonctionne-t-elle ?

NFC signifie communication en champ proche. C'est une norme pour que les appareils communiquent entre eux sans fil à une très courte distance.

La NFC est un sous-ensemble d'une autre technologie appelée RFID, alors creusons un peu cela avant de revenir à la NFC.

### Qu'est-ce que la RFID ?

L'identification par radiofréquence, ou RFID, est un terme générique pour les technologies qui utilisent des ondes radio d'un lecteur pour suivre des tags spécifiques. Ces tags incluent tous une antenne et une minuscule puce, et peuvent venir dans de nombreuses formes et tailles. 

Les dispositifs de paiement des péages autoroutiers et ces choses en plastique sur les vêtements et autres articles coûteux dans les magasins sont quelques exemples courants de tags RFID.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-123.png)
_Un diagramme d'un tag RFID. Les tags NFC ressemblent beaucoup à cela – [Source](https://www.analogictips.com/rfid-tag-and-reader-antennas/)_

Si vous avez déjà vu ces grands dispositifs de chaque côté d'une entrée de magasin, ce sont simplement de grands lecteurs RFID. Ils transmettent constamment des ondes radio et écoutent une réponse.

Alors, que se passe-t-il si vous essayez de quitter un magasin et qu'il y a encore un tag sur l'article que vous avez acheté ? 

La plupart des tags RFID ne sont pas alimentés, donc lorsque l'antenne dans le tag capte les ondes radio du lecteur, elle génère une petite quantité d'électricité. Cette électricité active la puce à l'intérieur du tag, et elle envoie un signal avec les informations stockées sur la puce vers le lecteur. 

Dans ce cas, lorsque le lecteur reçoit un signal du tag sur votre article, il déclenche une alarme.

### Comment la RFID et la NFC sont-elles liées ?

La NFC est une version plus récente et à haute fréquence de la RFID, et implique également des tags et des lecteurs. 

La fréquence plus élevée de la NFC signifie que, bien qu'elle puisse transférer des données beaucoup plus rapidement que la RFID, elle ne fonctionne qu'à une distance d'environ 4 cm/1,6 pouce ou moins. Pendant ce temps, la RFID fonctionne à une distance allant jusqu'à 12 m/40 pieds.

## À quoi sert la NFC ?

Il y a beaucoup de cas d'utilisation pour la NFC, mais voici quelques-uns des plus courants que vous verrez.

### Paiements sans contact

De nos jours, la chose la plus courante pour laquelle la NFC est utilisée est le paiement sans contact. De nombreuses cartes de crédit et de débit plus récentes incluent un tag NFC, donc vous pouvez simplement tenir votre carte juste au-dessus d'un terminal de paiement plutôt que de la faire glisser ou de l'insérer.

Les cartes de crédit et de débit avec paiement sans contact activé ont un symbole sur elles similaire à ceux-ci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-124.png)
_La plupart des cartes de paiement sans contact auront un symbole similaire sur l'avant ou l'arrière – [Source](https://www.emvco.com/emv_insights_post/contactless-payments-how-emvco-supports-seamless-and-secure-acceptance/)_

La plupart des téléphones modernes incluent une puce NFC, qui peut agir à la fois comme un lecteur/écrivain NFC et un tag. 

Cette puce, associée à une application de paiement mobile comme Google Pay, Apple Pay et Samsung Pay, signifie que vous n'aurez peut-être même plus besoin de sortir votre portefeuille. 

Au lieu de cela, votre téléphone peut agir comme un tag NFC virtuel pour votre carte de crédit ou de débit, même si ladite carte n'a pas de tag NFC réel à l'intérieur.

Que vous utilisiez votre carte sans contact ou une application de paiement mobile, chaque paiement que vous effectuez implique une tokenisation pour une sécurité supplémentaire.

La tokenisation est lorsque les informations de votre carte sont utilisées pour générer un jeton temporaire aléatoire pour chaque transaction. Ensuite, votre carte ou votre application de paiement mobile peut envoyer ce jeton temporaire en toute sécurité, plutôt que de transmettre votre numéro de carte réel, votre nom et d'autres informations sensibles.

Cependant vous choisissez de payer, utiliser une carte de paiement sans contact, une application de paiement mobile ou insérer la puce de votre carte sont toutes [beaucoup plus sûres que l'ancienne méthode de glissement](https://www.engadget.com/2019-08-29-how-to-make-online-payments-safely-and-securely.html).

### Interagir avec des produits

Traditionnellement, la RFID est utilisée pour suivre les stocks dans les entrepôts et les magasins. Mais une fois qu'un produit quitte le magasin, son tag RFID est désactivé.

Beaucoup de produits incluent maintenant des tags NFC pour une interaction supplémentaire après avoir quitté le magasin. Les figurines Amiibo de Nintendo sont probablement l'exemple le plus courant et récent de cela :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-96.png)
_Si ce n'est pas le tag NFC le plus mignon, je ne sais pas ce que c'est – [Source](https://www.nintendo.com/amiibo/detail/detective-pikachu-amiibo/)_

Lorsque vous scannez une figurine Amiibo avec votre console Nintendo, vous pouvez obtenir des personnages spéciaux, des objets ou d'autres contenus supplémentaires, selon le jeu et la figurine que vous utilisez.

Votre console Nintendo peut également écrire des informations sur le tag NFC de votre figurine, encore une fois, selon le jeu et la figurine.

D'autres entreprises comme Nike ont inclus des tags NFC dans des choses comme des maillots de sport et des baskets. Cela vous permet d'obtenir du contenu personnalisé basé sur le produit que vous scannez (scores récents pour une équipe, statistiques pour un joueur spécifique, etc.), ou même de vérifier qu'un produit est authentique.

### Transfert de données

Contrairement à la RFID, qui est typiquement une communication unidirectionnelle entre un lecteur et un tag, la NFC permet une communication bidirectionnelle.

Certains téléphones sont capables d'utiliser la NFC pour transférer des données comme des contacts ou des photos entre deux appareils si vous les touchez ensemble.

## Utilisations créatives de la NFC

L'une des choses les plus cool que vous pouvez faire avec la NFC est d'acheter un pack de tags en ligne et de les programmer pour faire différentes choses avec votre téléphone.

Par exemple, si vous êtes fatigué de toujours donner votre mot de passe WiFi aux invités, vous pourriez programmer un tag NFC pour qu'il se connecte automatiquement à votre réseau. Ensuite, tous vos invités doivent faire est de s'assurer que la NFC est activée et de tenir leurs téléphones près du tag.

Vous pourriez également programmer des tags NFC pour contrôler différents appareils intelligents autour de votre maison. Vous pourriez avoir un tag qui active ou désactive une lampe intelligente, ou un qui règle le thermostat. 

Les commandes déclenchées par les tags NFC peuvent également être personnalisées pour des appareils spécifiques. Par exemple, si vous aimez que la pièce soit un peu plus fraîche que votre partenaire, lorsque vous scannez le tag du thermostat, il peut baisser la température. Mais lorsque votre partenaire le scanne, il pourrait augmenter la température à son réglage préféré.

Il y a beaucoup d'autres façons intéressantes d'utiliser les tags NFC pour rendre votre vie un peu plus facile. Consultez cette vidéo pour plus d'idées et pour voir comment programmer vos propres tags NFC sur iOS et Android :

%[https://www.youtube.com/watch?v=o9WHrX9cvXA&t=87s]

## En résumé

Bien que vous n'ayez peut-être pas beaucoup entendu parler de la NFC jusqu'à plus tôt cette année (je n'en avais certainement pas entendu parler), elle deviendra probablement la norme pour payer les choses. 

Et considérant toutes les choses cool que vous pouvez faire avec un téléphone et un pack de tags NFC, il est surprenant que la NFC ne soit pas plus largement adoptée.

Si vous finissez par programmer vos propres tags NFC, faites-moi savoir ce que vous avez fait et comment vous l'avez fait sur [Twitter](https://twitter.com/kriskoishigawa).