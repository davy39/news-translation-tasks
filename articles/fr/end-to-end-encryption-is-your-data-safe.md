---
title: Chiffrement de bout en bout – Vos données sont-elles en sécurité face aux géants
  de la technologie ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-14T00:28:41.000Z'
originalURL: https://freecodecamp.org/news/end-to-end-encryption-is-your-data-safe
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/cyber-security-3400657__340.jpg
tags:
- name: encryption
  slug: encryption
- name: privacy
  slug: privacy
seo_title: Chiffrement de bout en bout – Vos données sont-elles en sécurité face aux
  géants de la technologie ?
seo_desc: "By Yehuda Clinton\nEvery now and then we hear buzzing in the news about\
  \ some egregious Big Tech privacy infringement. We are also frequently notified\
  \ about all the new steps our apps are taking to further protect our privacy. \n\
  Most of us then weigh th..."
---

Par Yehuda Clinton

De temps en temps, nous entendons parler dans les nouvelles de quelque violation flagrante de la vie privée par les géants de la technologie. Nous sommes également fréquemment informés de toutes les nouvelles mesures que nos applications prennent pour mieux protéger notre vie privée. 

La plupart d'entre nous pèsent alors les préoccupations et se soumettent au statu quo sans vraiment comprendre le problème. Tant que personne d'autre que nous ne peut voir ce message :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/e2ee.jpeg)

Récemment, WhatsApp a annoncé que les utilisateurs doivent consentir à partager leurs données, y compris les numéros de téléphone et les localisations avec Facebook. 

Commençons par la question de base :

## Quelles informations les applications, sites web et systèmes d'exploitation peuvent-ils accéder ?

Essayons de nous pencher sur WhatsApp, qui a récemment été sous le feu des critiques.

Chaque utilisateur de WhatsApp rencontre une déclaration comme "ce message personnel est chiffré de bout en bout". Ce qui signifie que WhatsApp ou toute autre personne ne devrait pas être en mesure de déchiffrer ce message une fois qu'il quitte votre téléphone. 

Nous devrions pouvoir faire confiance à ce que Facebook ne peut pas lire nos messages WhatsApp sur son serveur, même s'ils les stockent jusqu'à ce que le destinataire soit connecté. Vous pouvez lire la [politique de confidentialité de WhatsApp ici](https://www.whatsapp.com/legal/privacy-policy).

**Jusqu'à présent, pas d'arnaque.**

Ce qu'ils ne mentionnent pas dans leur politique de confidentialité, cependant, ce sont les permissions dans l'application concernant les médias et les capteurs. Je fais référence aux dialogues de permission qui apparaissent à la première utilisation.

Je fais également référence aux données que votre système d'exploitation partage avec Facebook en dehors de l'écosystème de l'application.

%[https://android.stackexchange.com/questions/71802/help-understanding-whatsapps-permissions]

Lors de l'installation d'un nouveau téléphone, vous pourriez lire cette liste de permissions accessibles par l'application, y compris : Stockage, localisation, Caméra, Microphone, Comptes, Profil, Contacts et vue des applications en cours d'exécution. 

L'article _StackExchange_ ci-dessus a plus de cinq ans et la liste a changé depuis. Cependant, vous voyez un schéma de changements fréquents des permissions et à quel point il peut être difficile de déterminer quand et comment l'application accède aux médias ou aux capteurs de l'appareil.

### Comment les géants de la technologie utilisent-ils vos données ?

Passons en revue certaines des permissions listées pour WhatsApp :

* **votre profil de réseau social** - détails comme le 'numéro de téléphone' et 'à propos'
* **localisation et heure** - quand vous étiez à un endroit donné
* **Photos/Médias/Fichiers** - espérons qu'ils ne les utilisent que pour ce qu'ils disent
* **contacts** - ils pourraient partager cela dans leurs algorithmes publicitaires 
* **caméra** - espérons qu'elle n'est utilisée que lors d'un appel vidéo chiffré
* **microphone** - espérons... mais voir [ceci](https://www.quora.com/Can-Whatsapp-use-microphone-access-to-listen-to-converstations-even-when-not-being-used-for-audio-video-call-And-can-Facebook-use-that-data-to-shows-ads?share=1) et [ceci](https://www.quora.com/Is-Facebook-listening-to-me-through-my-phones-microphone). Cela semble peu clair
* **gyroscope/accéléromètre** - détermine quand vous marchez, êtes assis ou conduisez
* **capteur de lumière** - aide à déterminer si votre téléphone est dans votre poche ou contre votre tête, etc.

### Utilisent-ils donc directement ou indirectement ces capteurs quand vous ne vous y attendez pas ?

Facebook n'a peut-être pas à admettre la réponse à cela, car google-play-services collecte une grande partie de ces informations et les partage avec eux de différentes manières. Notre meilleure réponse est que nous ne pouvons pas vraiment le prouver d'une manière ou d'une autre. 

Cela convient à la plupart des gens si les géants de la technologie utilisent simplement nos données pour nous proposer des publicités pertinentes, mais comment pouvons-nous le savoir ? De plus, s'ils ne le font pas aujourd'hui, rien ne les empêche de le faire un jour.

### Comment s'en sortent-ils

Nous pouvons voir, à partir d'autres cas, que les grandes entreprises technologiques se soutiennent généralement mutuellement sur ces questions. Les géants de la technologie ont une manière établie et centrée sur les données de alimenter le monde en ligne. Ils ne semblent pas aimer la concurrence. 

Remarquez comment l'application Parler a été expulsée d'AWS et en même temps, elle a été bannie des différentes boutiques d'applications. Il y a beaucoup d'autres incitations qui se produisent sur les applications hébergées par AWS ou Google. Même s'il y avait une pression continue pour se débarrasser de Parler, le fait d'être une application de réseau social en croissance a probablement scellé leur sort. 

## Quelles sont donc les alternatives ?

### [Telegram](https://telegram.org) & Signal

**Telegram** est une plateforme de messagerie instantanée axée sur la confidentialité avec quelque 500 millions d'utilisateurs. Bien que l'application ressemble à un réseau social de premier plan, son PDG [n'a pas l'intention de monétiser en utilisant les données des utilisateurs](https://techcrunch.com/2020/12/23/telegram-to-launch-an-ad-platform-as-it-approaches-500-million-users/). 

Ses applications mobiles sont open source, donc nous pouvons savoir exactement comment elles utilisent les données de votre téléphone. Cela nous permet également d'évaluer la robustesse du chiffrement de bout en bout.

**Signal** est un service de messagerie et d'appels complètement open source. Sa nature à but non lucratif vous assure qu'il n'y a pas de publicités ni de frais, mais il est un peu plus compliqué à utiliser et offre un service de moindre qualité.

### Comment garder votre Telegram privé et sécurisé

Utilisez les paramètres pour contrôler qui peut voir votre photo, vos groupes/canaux ou votre numéro de téléphone. Vous pouvez faire de votre nom de compte un alias et avoir votre vrai nom dans votre profil, qui ne peut être vu que par vos amis.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/telegram.png)

## Que sacrifiez-vous pour la confidentialité ?

Lorsque vous utilisez WhatsApp et des réseaux sociaux similaires, vous êtes obligé d'adhérer aux normes politiques et morales de la Silicon Valley. Même si cela peut vous déplaire, ils font assez bien pour vous protéger contre les arnaques, le harcèlement et autres activités criminelles. 

Si vous décidez d'utiliser une alternative, comme Telegram, vous devez être prêt à être votre propre filtre. Les applications Telegram ou Signal peuvent ne pas être sûres pour les enfants sans une surveillance attentive. Il existe [des versions de l'application disponibles](https://www.mspy.com/telegram.html) qui permettent aux parents de surveiller les messages et les contacts de leurs enfants. 

Si vous souhaitez en savoir plus sur les technologies sous-jacentes que nous rencontrons quotidiennement, lisez [ce livre de David Clinton](https://bootstrap-it.com/davidclinton/keeping-up/).

Si vous cherchez à chiffrer vos appareils, envisagez de suivre mon [cours VPN de Manning Publications](https://www.manning.com/liveproject/secure-business-infrastructure-with-a-custom-vpn?a_aid=bootstrap-it&a_bid=b9d7d398&chan=VPN).