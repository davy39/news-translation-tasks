---
title: La CIA vient de perdre le contrôle de son arsenal de piratage. Voici ce que
  vous devez savoir.
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-03-07T20:40:20.000Z'
originalURL: https://freecodecamp.org/news/the-cia-just-lost-control-of-its-hacking-arsenal-heres-what-you-need-to-know-ea69fc1ce38c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A2BGjM6cXjokKASrK8oLMA.jpeg
tags:
- name: News
  slug: news-tag
- name: politics
  slug: politics
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La CIA vient de perdre le contrôle de son arsenal de piratage. Voici ce
  que vous devez savoir.
seo_desc: WikiLeaks just released internal documentation of the CIA’s massive arsenal
  of hacking tools and techniques. These 8,761 documents — called “Vault 7” — show
  how their operatives can remotely monitor and control devices, such as phones, TVs,
  and cars....
---

WikiLeaks vient de publier des documents internes de la CIA révélant son immense arsenal d'outils et de techniques de piratage. Ces 8 761 documents — appelés « Vault 7 » — montrent comment leurs agents peuvent surveiller et contrôler à distance des appareils, tels que les téléphones, les téléviseurs et les voitures.

Et ce qui est pire, cet archive de techniques semble être accessible au public, où tous types de pirates peuvent l'utiliser pour nous attaquer.

> « La CIA a perdu le contrôle de la majorité de son arsenal de piratage, y compris des logiciels malveillants, des virus, des chevaux de Troie, des exploits "zero day" armés, des systèmes de contrôle à distance de logiciels malveillants et la documentation associée. Cette collection extraordinaire, qui représente plus de plusieurs centaines de millions de lignes de code, donne à son possesseur la capacité de piratage complète de la CIA. » — WikiLeaks

WikiLeaks a choisi de ne pas publier le code malveillant lui-même « jusqu'à ce qu'un consensus émerge sur... comment de telles 'armes' devraient être analysées, désarmées et publiées. »

Mais cela a révélé à quel point de nombreuses personnes sont au courant de ces techniques de piratage dévastatrices.

> « Cet archive semble avoir été diffusé parmi d'anciens pirates et entrepreneurs du gouvernement américain de manière non autorisée, dont l'un a fourni à WikiLeaks des parties de l'archive. » — WikiLeaks

De manière troublante, ces piratages ont été achetés ou volés à d'autres agences de renseignement de pays étrangers, et au lieu de fermer ces vulnérabilités, le gouvernement a mis tout le monde en danger en les laissant intentionnellement ouvertes.

> « [Ces décisions politiques] doivent être débattues en public de toute urgence, y compris si les capacités de piratage de la CIA dépassent ses pouvoirs mandataires et le problème de la surveillance publique de l'agence. » — l'agent qui a divulgué les données

Tout d'abord, je vais décomposer trois points clés de la publication Vault 7 d'aujourd'hui dont chaque citoyen américain devrait être conscient. Ensuite, je vous donnerai des conseils pratiques sur la manière dont vous pouvez vous protéger contre cette atteinte illégale du gouvernement américain — et contre les pirates malveillants que le gouvernement a renforcés par sa propre imprudence.

### Point clé #1 : Si vous conduisez une voiture connectée à Internet, les pirates peuvent la faire s'écraser contre un mur en béton et tuer vous et votre famille.

Je sais, cela semble fou, mais c'est réel.

> « En octobre 2014, la CIA envisageait également d'infecter les systèmes de contrôle des véhicules utilisés par les voitures et camions modernes. Le but d'un tel contrôle n'est pas spécifié, mais il permettrait à la CIA de mener des assassinats presque indétectables. » — WikiLeaks

Nous savons depuis un certain temps que les voitures connectées à Internet pouvaient être piratées. Mais nous n'avions aucune idée de l'ampleur de cela jusqu'à aujourd'hui.

Comme d'autres entreprises de logiciels, les fabricants de voitures corrigent constamment les vulnérabilités au fur et à mesure qu'ils les découvrent. Donc, si vous avez une voiture connectée à Internet, **mettez toujours à jour vers la dernière version de son logiciel**.

À mesure que Wikileaks rendra publiques davantage de ces vulnérabilités, les entreprises automobiles devraient pouvoir les corriger rapidement et publier des mises à jour de sécurité.

### Point clé #2 : Peu importe à quel point une application est sécurisée — si le système d'exploitation sur lequel elle fonctionne est piraté, l'application n'est plus sécurisée.

Puisque la CIA (et probablement beaucoup d'autres organisations, maintenant) sait comment compromettre vos appareils iOS et Android, elles peuvent intercepter des données avant même qu'elles n'atteignent l'application. Cela signifie qu'elles peuvent capturer vos entrées non chiffrées (microphone, frappes) avant que Signal ou WhatsApp ne puissent les chiffrer.

Une manière importante de réduire l'impact de ces exploits est d'**open sourcer autant de ce logiciel que possible**.

> « Les logiciels propriétaires tendent à avoir des fonctionnalités malveillantes. Le point est qu'avec un programme propriétaire, lorsque les utilisateurs n'ont pas le code source, nous ne pouvons jamais le savoir. Vous devez donc considérer chaque programme propriétaire comme un logiciel malveillant potentiel. » — Richard Stallman, fondateur du projet GNU

Vous pourriez penser — Android n'est-il pas open source ? Son noyau est open source, mais Google et les fabricants de téléphones comme Samsung ajoutent de plus en plus de code fermé par-dessus. En faisant cela, ils s'ouvrent à davantage de façons de se faire pirater. Lorsque le code est fermé, la communauté des développeurs ne peut pas faire grand-chose pour les aider.

> « Il existe deux types d'entreprises : celles qui ont été piratées, et celles qui ne savent pas encore qu'elles ont été piratées. » — John Chambers, ancien PDG de Cisco

En open sourçant davantage de code, la communauté des développeurs sera en mesure de découvrir et de corriger ces vulnérabilités beaucoup plus rapidement.

### Point clé #3 : Juste parce qu'un appareil semble éteint ne signifie pas qu'il est vraiment éteint.

L'un des exploits les plus troublants consiste à faire croire que les Smart TV sont éteintes, mais en laissant en réalité leurs microphones allumés. Les gens du monde entier buggent littéralement leurs propres maisons avec ces téléviseurs.

Le mode « faux éteint » fait partie de l'exploit « Weeping Angel » :

> « L'attaque contre les Smart TV Samsung a été développée en coopération avec le MI5/BTSS du Royaume-Uni. Après l'infestation, Weeping Angel place la TV cible en mode 'Faux Éteint', de sorte que le propriétaire croit à tort que la TV est éteinte alors qu'elle est allumée. En mode 'Faux Éteint', la TV fonctionne comme un micro, enregistrant les conversations dans la pièce et les envoyant via Internet à un serveur secret de la CIA. » — Documents Vault 7

La documentation divulguée de la CIA montre comment les pirates peuvent éteindre les LEDs pour faire croire qu'un appareil est éteint.

Vous savez, cette lumière qui s'allume chaque fois que votre webcam enregistre ? Elle peut aussi être éteinte. Même le directeur du FBI — le même officiel qui a récemment payé des pirates un million de dollars pour déverrouiller l'iPhone d'un tireur — encourage tout le monde à couvrir leurs webcams.

Tout comme vous devez toujours traiter une arme comme si elle était chargée, vous devez toujours traiter un microphone comme s'il enregistrait.

### Que pouvez-vous faire à ce sujet ?

Il n'est pas clair à quel point tous ces appareils sont compromis. Espérons qu'Apple, Google et d'autres entreprises corrigeront rapidement ces vulnérabilités à mesure qu'elles seront rendues publiques.

Il y aura toujours de nouvelles vulnérabilités. Aucune application logicielle ne sera jamais complètement sécurisée. Nous devons continuer à être vigilants.

Voici ce que vous devriez faire :

1. Ne désespérez pas. Vous devez tout de même faire tout ce que vous pouvez pour vous protéger, vous et votre famille.
2. Éduquez-vous sur la cybersécurité et la cyber guerre. [Voici le meilleur livre sur le sujet](http://amzn.to/2mjheuO).
3. Prenez un moment pour lire mon guide sur [comment chiffrer toute votre vie en moins d'une heure](https://medium.freecodecamp.com/tor-signal-and-beyond-a-law-abiding-citizens-guide-to-privacy-1a593f2104c3#.1sx4ibwny).

Merci d'avoir lu. Et un merci spécial à [Steve Phillips](https://twitter.com/elimisteve/) pour avoir aidé à réviser et vérifier les faits de cet article.