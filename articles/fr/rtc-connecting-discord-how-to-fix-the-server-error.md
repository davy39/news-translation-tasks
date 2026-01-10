---
title: RTC Connecting Discord – Comment corriger l'erreur du serveur
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-02T17:10:47.000Z'
originalURL: https://freecodecamp.org/news/rtc-connecting-discord-how-to-fix-the-server-error
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Discord.png
tags:
- name: Chat
  slug: chat
- name: discord
  slug: discord
- name: messaging
  slug: messaging
seo_title: RTC Connecting Discord – Comment corriger l'erreur du serveur
seo_desc: 'Discord is an instant messaging app that lets you communicate through voice,
  video, and texts. It is available in a web-based form, a desktop app, and a mobile
  app.

  But sometimes, when you''re trying to establish a voice call connection, you''ll
  get an...'
---

Discord est une application de messagerie instantanée qui vous permet de communiquer par voix, vidéo et textes. Elle est disponible sous forme web, en application de bureau et en application mobile.

Mais parfois, lorsque vous essayez d'établir une connexion d'appel vocal, vous obtenez une erreur qui dit « RTC Connecting Discord ». Ce message continue de s'afficher sans aucun progrès significatif.

Alors, que signifie cette erreur ?

Discord utilise le protocole Real-time Chat (RTC) pour exécuter des communications concurrentes. Donc, si vous rencontrez le problème « RTC Connecting Discord », il s'agit d'un problème réseau.

Dans cet article, je vais vous montrer 5 modifications que vous pouvez apporter à vos configurations réseau pour corriger le problème RTC Connecting Discord. 3 des correctifs concernent les paramètres réseau de votre ordinateur, tandis que les 2 restants se font directement dans votre application Discord.

## Comment corriger RTC Connecting Discord en mettant à jour votre pilote réseau

Si votre appareil dépend d'un pilote de carte réseau obsolète pour les connexions Internet, cela pourrait avoir un effet négatif sur votre expérience Internet – et pourrait également causer ce problème.

Ainsi, la mise à jour de votre pilote réseau peut corriger le problème.

**Les étapes ci-dessous vous guident pour mettre à jour votre pilote de carte réseau.**

**Étape 1** : Cliquez sur Démarrer (logo Windows) et recherchez « gestionnaire de périphériques ». Appuyez sur `ENTRÉE` pour ouvrir le premier résultat de recherche – qui est toujours le Gestionnaire de périphériques. Vous pouvez également cliquer sur le résultat de recherche « Gestionnaire de périphériques ».
![ss-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-1.jpg)

**Étape 2** : Développez « Cartes réseau ».

**Étape 3** : Recherchez l'adaptateur en cours d'utilisation, faites un clic droit dessus et sélectionnez « mettre à jour le pilote ».
![ss-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-2.jpg)

**Étape 4** : Sélectionnez « Rechercher automatiquement les pilotes ».
![ss-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-3.jpg)

Windows recherchera maintenant sur Internet un pilote mis à jour et l'installera pour vous.

## Comment corriger RTC Connecting Discord en changeant votre serveur de noms de domaine

Un serveur de noms de domaine (DNS) vous est attribué par votre FAI (Fournisseur d'Accès à Internet). Les serveurs de noms de domaine permettent d'atteindre des sites web en tapant des adresses (URL) dans le navigateur au lieu de nombres illisibles.

Changer ce DNS pour un DNS largement utilisé comme celui de Google ou Cloudflare peut vous aider à corriger le problème RTC Connecting Discord.

**Pour changer votre DNS pour celui de Google, suivez les étapes ci-dessous.**

**Étape 1** : Faites un clic droit sur Démarrer et choisissez « Exécuter » pour ouvrir la boîte de dialogue Exécuter.
![ss-4](https://www.freecodecamp.org/news/content/images/2021/12/ss-4.jpg)

**Étape 2** : Tapez « Control ncpa.cpl » (sans les guillemets) et appuyez sur `ENTRÉE`. Cela ouvrira vos périphériques de connexion réseau.
![ss-5-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-5-2.png)

**Étape 3** : Faites un clic droit sur votre réseau actuel et sélectionnez « Propriétés ».
![ss-6-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-1.jpg)

**Étape 4** : Recherchez le Protocole Internet Version 4 (TCP/IPv4) et double-cliquez dessus.
![ss-7](https://www.freecodecamp.org/news/content/images/2021/12/ss-7.jpg)

**Étape 5** : Cliquez sur le bouton radio « Utiliser l'adresse de serveur DNS suivante » et tapez les valeurs suivantes :
- 8.8.8.8 pour Serveur DNS préféré
- 8.8.4.4 pour Serveur DNS alternatif

![ss-8](https://www.freecodecamp.org/news/content/images/2021/12/ss-8.jpg)

**Étape 6** : Cliquez sur Ok.

Terminez la configuration avec le correctif suivant.

## Comment corriger RTC Connecting Discord en effaçant le cache réseau de votre ordinateur dans l'invite de commande

Si vous utilisez Discord en version web, ce correctif peut fonctionner pour vous.

Vous pouvez effacer le cache réseau de votre navigateur, mais une méthode plus efficace consiste à l'effacer directement sur votre ordinateur Windows 10 dans l'invite de commande.

Les étapes ci-dessous vous montrent comment faire.

**Étape 1** : Appuyez sur la touche `WIN` (logo Windows) de votre clavier et recherchez « cmd ».

Vous devez utiliser l'invite de commande en tant qu'administrateur, donc vous devez sélectionner « Exécuter en tant qu'administrateur » à droite au lieu de simplement appuyer sur `ENTRÉE` pour l'ouvrir.

**Étape 2** : Entrez et exécutez les commandes suivantes une après l'autre :

- `ipconfig /release`
- `ipconfig /flushdns`
- `ipconfig /renew`

**Étape 3** : Redémarrez votre ordinateur.
![ss-9](https://www.freecodecamp.org/news/content/images/2021/12/ss-9.png)

![ss-10](https://www.freecodecamp.org/news/content/images/2021/12/ss-10.png)

## Comment corriger RTC Connecting Discord en désactivant la QoS

La QoS (Qualité de Service) de Discord communique à votre routeur que les unités de données transmises sont de haute priorité. Cela pourrait faire dysfonctionner votre routeur et causer le problème RTC Connecting Discord.

Ainsi, la désactivation de la QoS pourrait le corriger pour vous au cas où elle serait activée.

**Suivez les étapes ci-dessous pour désactiver la QoS sur Discord.**

**Étape 1** : Lancez Discord, puis cliquez sur Paramètres dans le coin inférieur gauche.
![ss-11](https://www.freecodecamp.org/news/content/images/2021/12/ss-11.jpg)

**Étape 2** : Sélectionnez Voix et Vidéo dans le panneau de gauche.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/12/ss-12.jpg)

**Étape 3** : Faites défiler jusqu'à la section QoS et désactivez-la.
![ss-13](https://www.freecodecamp.org/news/content/images/2021/12/ss-13.jpg)

**Étape 4** : Redémarrez l'application Discord.

## Comment corriger RTC Connecting Discord en changeant le sous-système audio dans Discord

Dans Discord, le sous-système audio Legacy a toujours été suggéré comme le meilleur car il est de la plus haute qualité comparé aux sous-systèmes audio Standard et Expérimental.

Changer votre sous-système audio pour Legacy peut vous permettre d'établir un audio de qualité – ce qui peut finir par corriger le problème RTC Connecting Discord.

**Ces étapes vous guident pour changer votre sous-système audio pour Legacy.**

**Étape 1** : Ouvrez Discord et cliquez sur Paramètres dans le coin inférieur gauche.
![ss-11](https://www.freecodecamp.org/news/content/images/2021/12/ss-11.jpg)

**Étape 2** : Sélectionnez Voix et Vidéo.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/12/ss-12.jpg)

**Étape 3** : Faites défiler jusqu'au menu déroulant Sous-système audio et sélectionnez « Legacy ».
![ss-14](https://www.freecodecamp.org/news/content/images/2021/12/ss-14.jpg)

**Étape 4** : Redémarrez Discord.

## Conclusion

Cet article vous a montré comment corriger le problème RTC Connecting Discord que vous pourriez rencontrer lorsque vous essayez d'utiliser la fonction d'appel audio de Discord.

Outre les solutions expliquées dans cet article, vous pouvez essayer d'autres correctifs mineurs tels que :
- Redémarrer vos appareils – ordinateur et routeur
- Vérifier deux fois la connexion Internet
- Utiliser un VPN

Merci beaucoup d'avoir lu cet article. Si vous le trouvez utile, partagez-le avec vos amis et proches.