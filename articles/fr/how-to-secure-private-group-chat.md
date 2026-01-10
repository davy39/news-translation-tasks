---
title: Comment configurer un chat de groupe privé extrêmement sécurisé
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-01-15T20:20:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-private-group-chat
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/WinonaSavingsBankVault.JPG
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
- name: Security
  slug: security
seo_title: Comment configurer un chat de groupe privé extrêmement sécurisé
seo_desc: 'Chat room tools like Discord and Slack are more popular than ever. But
  they were never intended as a place for sensitive discussions or secure file sharing.

  Discord was built primarily for voice chat during online games. And Slack''s roots
  are in corp...'
---

Les outils de chat comme Discord et Slack sont plus populaires que jamais. Mais ils n'ont jamais été conçus pour des discussions sensibles ou le partage sécurisé de fichiers.

Discord a été principalement construit pour le chat vocal pendant les jeux en ligne. Et les racines de Slack se trouvent dans la communication d'entreprise.

Aucun de ces outils de chat n'a été conçu avec la confidentialité comme priorité.

Un autre outil de chat de facto que beaucoup de gens utilisent - Twitter - a été conçu pour des mises à jour de statut rapides et publiques. Ils ont ajouté les Messages Directs, mais ceux-ci ne sont pas particulièrement privés non plus.

Selon [PrivacySpy](https://privacyspy.org/directory/) – un site web qui analyse les politiques de confidentialité des grandes entreprises technologiques – aucune de ces trois options ne peut être suffisamment privée pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Directory___PrivacySpy.jpg)

Selon leurs politiques de confidentialité, Discord, Slack et Twitter peuvent tous être prêts à transmettre vos données à quelqu'un d'autre sans même nécessiter une assignation à comparaître ou une ordonnance du tribunal.

Il pourrait y avoir des situations où le gouvernement – ou même une entreprise privée – pourrait accéder à vos messages. Ils pourraient même les rendre publics.

Si cette possibilité vous dérange, ne craignez rien. Si vous voulez vraiment pouvoir parler avec des amis sans risque que votre groupe soit compromis ou que vos secrets soient divulgués, il existe de nombreuses options à votre disposition.

Cet article vous montrera plusieurs façons de créer des chats de groupe où aucune entreprise n'a le pouvoir de transmettre vos conversations à qui que ce soit.

# Comment discuter en toute sécurité en utilisant des applications de messagerie

Tout d'abord, il existe des outils de messagerie conçus par des experts en sécurité.

Vous pouvez entendre Mark Zuckerberg parler de la façon dont WhatsApp et Facebook Messenger utilisent le chiffrement. Ou Tim Cook parler de la façon dont iMessage utilise le chiffrement.

Ces trois outils de messagerie sont closed-source, il est donc difficile de savoir à quel point ils chiffrent vos messages de manière sécurisée, et qui à l'intérieur (et à l'extérieur) de l'entreprise peut y accéder.

Cela signifie que ces outils ne sont pas suffisamment privés pour des conversations sensibles.

Il existe cependant des outils de messagerie vraiment privés qui sont open source, ce qui leur donne une responsabilité supplémentaire.

# Utiliser Signal Private Messenger pour discuter en toute sécurité

![Image](https://www.freecodecamp.org/news/content/images/2020/01/signal.jpg)
_Signal Private Messenger dans le Google Play Store_

[Signal Private Messenger](https://signal.org/download/) offre un chiffrement de bout en bout et utilise des numéros de vérification.

Signal propose également des messages éphémères, des appels téléphoniques chiffrés et toute une série d'autres fonctionnalités de communication sécurisée. Et pour en venir au sujet, Signal offre un chat de groupe.

Signal est gratuit et fonctionne sur iOS, Android et sur votre bureau. Je l'utilise depuis plusieurs années.

Le principal inconvénient de Signal est que vous devez télécharger une application et associer votre compte à votre numéro de téléphone. Ce n'est pas un outil de communication anonyme. Si vous étiez - par exemple - un journaliste rencontrant des sources, vous devrez peut-être trouver une option plus sécurisée.

# Utiliser Keybase pour discuter en toute sécurité

![Image](https://www.freecodecamp.org/news/content/images/2020/01/The_App_-_Install_Macos___Keybase_Docs.jpg)
_Une capture d'écran de Keybase_

Un autre outil de messagerie est [Keybase](https://keybase.io/download). Il s'agit d'un outil de partage de fichiers qui dispose également d'un chat sécurisé intégré.

Contrairement à Signal, Keybase stocke vos messages chiffrés sur leur serveur, donc en théorie, il est moins sécurisé. Mais il est open source, et le chiffrement qu'ils utilisent coûterait en théorie des milliards de dollars de temps de supercalculateur pour être craqué avec la technologie d'aujourd'hui.

Keybase nécessite également l'installation d'un logiciel et la vérification de votre identité - le plus souvent en publiant des messages publics depuis vos comptes de réseaux sociaux.

# Mais si vous voulez vraiment, vraiment que votre chat de groupe soit privé sans installer d'applications...

Je vais vous présenter les outils que j'utiliserais si je voulais former un groupe autour d'un sujet sensible, ou depuis un pays avec un régime autoritaire.

Et un mot d'avertissement - nous allons aborder des choses dignes d'un roman d'espionnage ici. Rien d'aussi élaboré que [communiquer à travers des mots croisés dans des journaux quotidiens](https://en.wikipedia.org/wiki/D-Day_Daily_Telegraph_crossword_security_alarm), mais tout aussi ésotérique.

# Comment créer votre salle de chat privée

Si vous voulez simplement pouvoir discuter en toute sécurité sans passer beaucoup de temps à configurer, voici l'outil de chat le plus sécurisé que je connaisse : [LeapChat](https://www.leapchat.org).

Ce chat minimaliste utilise un chiffrement de bout en bout. Il chiffre les messages à la fois en transit et au repos. Et il déchiffre les messages lorsqu'ils atteignent votre navigateur.

Il n'est pas nécessaire de vous connecter avec une adresse e-mail ou un numéro de téléphone - ou même de vous souvenir d'un mot de passe. Si vous connaissez l'URL de la salle, vous pouvez simplement choisir un nom d'utilisateur et commencer à discuter.

Mais la seule façon de connaître l'URL d'une salle LeapChat est de l'obtenir de quelqu'un d'autre. Vous ne allez pas la deviner. Parce que les URLs sont longues de 25 mots en anglais, et chacun de ces mots provient de la liste EFF de 7 776 mots. Cela signifie que le nombre de combinaisons possibles est d'environ 1 googol (10 à la puissance 100 - plus de combinaisons possibles qu'il n'y a d'atomes dans l'univers connu).

Mais un avantage que l'URL soit une longue liste de mots anglais est que vous pouvez la mémoriser en utilisant un outil mnémotechnique si vous devez, et vous pouvez facilement la lire à haute voix à quelqu'un.

# Comment partager en toute sécurité l'URL de votre salle de chat

Vous vous demandez peut-être - quelle est la manière la plus sécurisée de partager une URL vers ma nouvelle salle LeapChat ?

Dans ce cas, vous devriez utiliser une sorte d'URL de redirection autodestructrice. Ainsi, même si quelqu'un découvre l'URL dans l'un de vos messages après que vous l'ayez déjà utilisée, ils ne sauront pas où le lien mène finalement.

Vous pouvez utiliser un service open source comme [One Time Secret](https://onetimesecret.com) pour partager votre URL.

Et qu'en est-il du partage de fichiers ? Vous pourriez simplement partager en toute sécurité un fichier texte contenant le lien vers votre salle de chat sécurisée en utilisant Keybase ou Signal si vous voulez les configurer.

Mais il existe une méthode encore plus simple. Mozilla offre [un service de partage de fichiers anonymes et chiffrés de bout en bout pour des fichiers jusqu'à 1 gigaoctet](https://send.firefox.com). Vous pouvez même définir les liens de téléchargement pour qu'ils expirent après utilisation.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Firefox_Send.jpg)

# Comment empêcher les taupes d'entrer dans votre salle de chat

Maintenant, vous avez tous les outils nécessaires pour créer un chat de groupe vraiment privé et vraiment sécurisé avec vos amis. Mais comment identifier si vos amis sont bien ceux qu'ils prétendent être ?

Toute organisation aura un problème potentiel de "taupe".

Si un intrus parvient à s'infiltrer dans votre groupe, peu importe à quel point vous pratiquez sérieusement la sécurité. Ils peuvent simplement faire toutes les contre-mesures de confidentialité que vous leur dites de faire et continuer à avoir accès.

Ainsi, avant de transférer votre groupe vers un emplacement plus sécurisé, vous devez établir que les personnes dans votre groupe sont bien celles qu'elles prétendent être.

En supposant que les personnes du groupe sont censées se connaître (et qu'il ne s'agit pas d'une réunion de personnes anonymes), j'ai une méthode assez infaillible pour y parvenir. Elle est similaire à l'approche de Keybase de confirmation de votre identité en utilisant des publications publiques sur les réseaux sociaux. Mais ma méthode est encore plus discrète.

Tout ce que vous avez à faire est de leur demander de mettre à jour leur profil LinkedIn pour inclure un mot aléatoire, comme "pizzicato". Ensuite, vous pouvez vérifier leur profil LinkedIn pour confirmer qu'ils en ont le contrôle.

LinkedIn est un excellent réseau social à utiliser pour cela car presque tous les professionnels en ont un. Il est fastidieux de créer un nouveau compte et d'accumuler des connexions et des recommandations du monde réel. Ils n'ont pas besoin de créer une publication - ils peuvent simplement mettre à jour leur profil le temps que vous vérifiiez qu'ils sont bien ceux qu'ils prétendent être, puis revenir en arrière sur leur modification de profil.

Ainsi, une fois qu'un membre de votre chat actuel a passé votre vérification d'identité dans le monde réel, vous pouvez lui donner une URL autodestructrice qui mène à votre salle LeapChat, ou échanger des clés de chiffrement Signal ou Keybase, puis discuter là-bas.

# Comment supprimer votre communauté Discord / Slack / Twitter DM existante

La mauvaise nouvelle est que la plupart de ces services continueront à stocker vos données longtemps après que vous ayez supprimé votre compte.

Même si vous leur demandez explicitement de supprimer toutes vos données, il n'y a tout simplement aucun moyen de savoir avec certitude que vos données ont été supprimées. Il est impossible de prouver que vos données n'existent plus dans une sauvegarde quelque part.

Ce qui est fait est fait. Ce qui est dit est dit.

Mais vous avez le contrôle sur ce que les entreprises peuvent stocker à votre sujet à l'avenir.

Si vous avez un accès administrateur à votre ancien Discord ou Slack, vous pouvez le supprimer. Et même si cela ne supprime pas réellement toutes les données de leurs serveurs, cela empêchera de nouvelles personnes de pouvoir rejoindre le groupe et de fouiller dans votre historique de chat. Cela réduira la probabilité que l'un de vos secrets soit divulgué à l'avenir.

Vous pouvez également supprimer vos propres comptes sur les Slacks et Discords dont vous faites partie. Cela devrait supprimer vos anciens messages.

# Encore une fois, voici comment migrer votre Slack, Discord, ou autre chat de groupe vers un environnement plus sécurisé - le tout en un seul organigramme.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/An_untitled_mindmap.jpg)

# Quelques outils bonus si vous voulez vraiment, vraiment être sécurisé

## Naviguer avec Tor

Tor signifie "The Onion Router" qui fait référence à son utilisation de nombreuses couches semblables à des oignons pour masquer l'activité du réseau. Il est gratuit, open source et raisonnablement facile à utiliser.

Tor ressemble à n'importe quel autre navigateur et a un ensemble de fonctionnalités similaire. C'est un fork de Firefox. Il est juste un peu plus lent à cause de toutes les redirections de paquets supplémentaires.

Mais si vous voulez vraiment naviguer sur le web en toute tranquillité d'esprit, utilisez Tor et il sera virtuellement impossible pour quiconque de vous tracer.

[Téléchargez le navigateur Tor ici](https://www.torproject.org/download/).

Une fois que vous avez installé Tor, vous pouvez visiter [check.torproject.org](https://check.torproject.org/) pour vérifier que tout fonctionne correctement.

## Utiliser un compte Protonmail pour les e-mails

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Secure_email__ProtonMail_is_free_encrypted_email_.jpg)

[Protonmail](https://protonmail.com/) est un outil d'e-mail axé sur la confidentialité. Vous savez qu'il est sécurisé parce qu'il est suisse. 😉

Vous devrez donner à Protonmail une vraie adresse e-mail afin de créer votre compte, mais cette adresse e-mail sera stockée sous forme chiffrée.

Vous voudrez probablement plus d'une adresse Protonmail pour chaque usage.

N'oubliez pas non plus que les e-mails sont également stockés sur les serveurs du service de messagerie de votre destinataire. Donc si vous envoyez un e-mail à quelqu'un qui a une adresse Gmail, votre e-mail sera également stocké sur les serveurs de Google.

## C'est tout. Restez vigilants, amis.