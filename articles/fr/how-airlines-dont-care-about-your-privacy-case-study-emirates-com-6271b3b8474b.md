---
title: 'Mise à jour : Les sites web des compagnies aériennes ne se soucient pas de
  votre vie privée : une étude de cas sur Emirates.com'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-03T00:56:18.000Z'
originalURL: https://freecodecamp.org/news/how-airlines-dont-care-about-your-privacy-case-study-emirates-com-6271b3b8474b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*61m9JVlYvpvORj2IUlp-4w.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Data Science
  slug: data-science
- name: Facebook
  slug: facebook
- name: privacy
  slug: privacy
- name: 'tech '
  slug: tech
seo_title: 'Mise à jour : Les sites web des compagnies aériennes ne se soucient pas
  de votre vie privée : une étude de cas sur Emirates.com'
seo_desc: 'By Konark Modi

  I asked my wife if it is alright if her Date of Birth is known to a stranger. Only
  if they send me a birthday gift, she joked. What about your passport number? She
  lowered the book she was reading. I now had her attention.

  Now imagine ...'
---

Par Konark Modi

J'ai demandé à ma femme si cela la dérangeait qu'un inconnu connaisse sa date de naissance. Seulement s'ils m'envoient un cadeau d'anniversaire, a-t-elle plaisanté. Et ton numéro de passeport ? Elle a baissé le livre qu'elle lisait. J'avais maintenant son attention.

Maintenant, imaginez ceci, ai-je dit : « Vous essayez de faire votre enregistrement en ligne pour votre vol et vous voyez le message d'erreur — Cette réservation n'existe pas. Vous essayez à nouveau, cela doit sûrement être une erreur. Non, toujours le même message d'erreur. La personne du centre d'appels répète les mêmes mots. Cela doit être une erreur ! Vous vérifiez votre email, et le voilà — qui vous fixe — la confirmation par email de l'annulation. Mais vous êtes sûr de ne pas l'avoir fait. » Qui l'a fait ?

Ce n'est pas un scénario tirée d'un livre de science-fiction, [cela s'est vraiment produit](https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego).

Une organisation dont le produit numérique principal manque même des pratiques de base en matière de sécurité des données vit dans un monde utopique où les gens laissent leur coffre-fort ouvert et ne s'attendent jamais à ce qu'un cambrioleur entre.

Dans le cadre de la divulgation complète, il y a quelque temps, lors de la réservation de voyages pour ma famille, je suis tombé sur quelques pratiques de sécurité des données qui, en tant que défenseur de la sécurité des données, m'ont extrêmement inquiété. Lorsque j'ai exprimé mes préoccupations à l'équipe d'Emirates, cette conversation a eu lieu -

![Image](https://cdn-media-1.freecodecamp.org/images/J98i59bZQiaHOsLcEjwt8BwljNL7iZvwi2Vt)
_Conversation avec le support d'Emirates._

Pour un profane, lorsque vous réservez votre vol via Emirates, national ou international, il y a environ [300 points de données](https://pastebin.com/cAcXx2A4) liés à votre réservation.

Dès que vous cliquez sur gérer les préférences pour sélectionner un siège ou un repas pour votre voyage ou pour vous enregistrer à votre vol, votre identifiant de réservation et votre nom de famille sont transmis à environ 14 différents trackers tiers comme Crazy Egg, Boxever, Coremetrics, Google et Facebook, parmi d'autres.

### **Détails**

Après avoir terminé la réservation sur Emirates, j'ai reçu un email de confirmation intitulé : Confirmation de réservation — Numéro de réservation.

![Image](https://cdn-media-1.freecodecamp.org/images/8-8XXdTlMKTutKcdyriWK1-UD4YgeZlyVGJL)
_Email de confirmation de réservation._

Le corps de l'email contenait Gérer la réservation. J'ai procédé à la sélection des sièges et des repas en cliquant sur le bouton Gérer la réservation et j'ai atteint la page Gérer les préférences. Cela était assez simple.

![Image](https://cdn-media-1.freecodecamp.org/images/U2fdc81FxC3yRXi5ooiz2GLDMtJOS8Cks5nj)
_Lien Gérer la réservation dans l'email._

Alors qu'en tant qu'utilisateur, j'ai vu le comportement normal de cliquer sur un lien et d'atteindre la page de destination « Gérer les préférences », en arrière-plan, une chaîne de redirection a eu lieu.

![Image](https://cdn-media-1.freecodecamp.org/images/TJgXmvJ95h6sw3noBhTlGdU5OEVB7t9ZnKAQ)
_Chaîne de redirection avant d'atteindre la page de destination._

Alors que le lien Gérer la réservation était censé être exclusif à moi (l'utilisateur et le site web), ce lien a également été partagé avec de nombreux trackers tiers mis en œuvre par Emirates sur leurs pages web.

![Image](https://cdn-media-1.freecodecamp.org/images/UfY2o2W4fksf1pZbNRZLXMNFjBqL6oLzQ5kU)
_Page Gérer la réservation._

La cerise sur le gâteau était le lien HTTP qui mène à la page Gérer les préférences. L'insécurité de HTTP a été [discutée](https://medium.com/@pallavimodi/http-https-what-is-the-difference-3a97fe2f7fd8) maintes et maintes fois, surtout lorsqu'il s'agit de maintenir l'authenticité du contenu et la protection contre les intrus. Mais en bref, les liens HTTP sont un cauchemar pour la confidentialité des données. Ainsi, non seulement Emirates transmettait les informations des utilisateurs aux trackers tiers auto-implantés, mais permettait également aux adversaires du réseau d'avoir accès à la page supposément « privée ».

![Image](https://cdn-media-1.freecodecamp.org/images/GUDfElLiP1iynwZ8AL84GTAMC27HCh8HMZqB)
_[http://track.emirates.email/track/click/30705682/www.emirates.com?p=eMSwicCI6IntcInVcIjozM....(REDACTED)](http://track.emirates.email/track/click/30705682/www.emirates.com?p=eMSwicCI6IntcInVcIjozM....(REACTED)" rel="noopener" target="_blank" title=")_

### **Quelles informations les tiers peuvent-ils accéder ?**

Les liens mentionnés en (1) et (2) sont actuellement envoyés aux tiers.

![Image](https://cdn-media-1.freecodecamp.org/images/blQnYPaptvr2V9k8ruJXyJGRaAmdhhrrpIgp)

Les champs suivants prennent l'URL, ce qui donne accès aux détails de la réservation.

![Image](https://cdn-media-1.freecodecamp.org/images/S5Ah2kCOMZJznXUtFly-KRt1VltJgYrJl37d)
_Champs qui prennent l'URL privée._

![Image](https://cdn-media-1.freecodecamp.org/images/CcJhlcel0E2cjrlD7WtgacQvlv4FF-4YGvbt)
_Envoi de l'URL dans la clé `dr` utilisée par Google Analytics._

![Image](https://cdn-media-1.freecodecamp.org/images/DbuxeC1c16zWXNAguVpioFAOrfXXq0F9cdVE)

Toute personne ayant accès à ces liens peut non seulement lire mais aussi modifier les informations que je peux en tant qu'utilisateur.

Par exemple, ils peuvent maintenant -

1. Changer ou annuler le vol
2. Changer la préférence de siège ou de repas
3. Ajouter plus de produits à la réservation
4. Changer ou ajouter les informations de passeport
5. Changer ou ajouter les informations du programme de fidélité, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/MJWQLCMrz6SWu2nMTuq3fm7swGiAfxl3hOO0)

![Image](https://cdn-media-1.freecodecamp.org/images/-NJQfaC6PV7DtifczwFIsA0ZDRRksu-EfopD)

![Image](https://cdn-media-1.freecodecamp.org/images/vxvDjZC9XrDCMiaWBG-WWrs4hhWzRapLS2by)
_Modifier la réservation._

**Exemple d'informations personnelles modifiables sur cette page :**

**a. Nom complet :**

![Image](https://cdn-media-1.freecodecamp.org/images/B3TaqII7bAoKkofhVk21DY040GlpuBHQ-wQP)
_Nom._

**b. Numéro Skywards**

![Image](https://cdn-media-1.freecodecamp.org/images/Pw9KljVJmGJOZCbxPjC4R4XFYy2Id4EdJsjw)
_Numéro Skywards_

**c. Adresse e-mail / Numéro de téléphone :**

![Image](https://cdn-media-1.freecodecamp.org/images/IXHrwJuTbuoulITQC4tADyQKdE79YKYR62DV)
_Lire / Changer les informations personnelles_

**d. Montant payé, détail des frais.**

![Image](https://cdn-media-1.freecodecamp.org/images/F76wEiebLxzeqNvF1mrtmweKg9z4huZqJsby)
_Montant payé, forme de paiement, détail des frais._

**e. Détails du passeport, Nationalité, Date de naissance, Genre**

![Image](https://cdn-media-1.freecodecamp.org/images/0zHmM1qv8K4ZqfE6fbG4MRnAfGgKrwAEK1ms)
_Détails du passeport, Date de naissance, Expiration, Genre, Nationalité._

_Note :_ En octobre 2017, des champs tels que le numéro de passeport, l'adresse e-mail et le numéro de téléphone étaient masqués sur l'interface utilisateur mais n'étaient pas obfusqués dans le code source. L'application web a été révisée depuis et ces champs sont maintenant obfusqués.

![Image](https://cdn-media-1.freecodecamp.org/images/8EbqAkIVUoJKvI6RnBvGSlDOG1hll183ivzO)
_Champs masqués en texte brut. (Octobre 2017)_

J'ai décidé de jeter un coup d'œil à l'application mobile et de voir si le passé rattrape le présent, et le voilà dans toute sa gloire — Numéro de passeport, adresse e-mail et numéro de téléphone en texte brut. Ce qui était obfusqué sur l'application web était facile d'accès sur l'application mobile.

![Image](https://cdn-media-1.freecodecamp.org/images/FOZAgyc668QqoBD3zh17PB6fOdh0ir4oSCD8)
_Détails du passeport en texte brut sur l'API mobile._

**Maintenant, qu'est-ce qui ne va pas avec cela ?**

Ce problème n'est pas limité à Emirates, de nombreuses compagnies aériennes comme Lufthansa, KLM (vérifié en octobre 2017) souffrent des mêmes problèmes.

Chaque site web utilise des trackers tiers pour améliorer leur produit et offrir une meilleure expérience d'utilisation du web. Les fuites de données sont souvent considérées comme des dommages collatéraux et parfois même pas considérées du tout lors de la mise en œuvre de tels trackers.

La plupart de ces tiers sont présents sur de nombreux autres sites web et utilisent des identifiants à long terme comme les cookies pour suivre les utilisateurs à travers les domaines. Maintenant, parce qu'un des sites web, dans ce cas Emirates, fuit des informations privées, ces entreprises peuvent maintenant potentiellement non seulement lier l'activité de l'utilisateur à travers le web, mais aussi identifier qui est l'utilisateur.

Les questions qui nécessitent des réponses de la part d'Emirates (et d'autres) sont -

1. Pourquoi mes informations de réservation ont-elles été transmises à ces tiers sans mon consentement explicite.
2. Pourquoi ces tiers doivent-ils recevoir ces informations ?
3. Emirates est-il même conscient que des informations sensibles des utilisateurs sont divulguées à ces tiers ?
4. Qui sont ces tiers ?
5. Que font-ils avec les informations des utilisateurs ?

### **Signalement à Emirates**

Dans le cadre d'un comportement responsable, après avoir découvert ces graves failles de sécurité qui violent la confidentialité des données des utilisateurs, j'ai décidé de les signaler à Emirates via un message direct sur Twitter en octobre 2017. Veuillez noter que je n'ai pas pu trouver de canal dédié pour signaler les bugs de sécurité sur le site web d'Emirates.

L'équipe des médias sociaux a immédiatement répondu à mon message direct sur Twitter avec une réponse standard, mais je n'étais pas prêt à abandonner. J'ai également écrit un email au chef de produit en soulignant les failles de sécurité. J'ai été accueilli par un silence assourdissant.

À ce jour (2018-03-03), beaucoup de ces problèmes persistent.

Cela constitue une grave violation de la vie privée, il n'y a aucun moment pendant le processus de réservation où j'ai accepté de partager l'une de ces informations personnelles avec l'un de ces sites web.

La [politique de confidentialité](https://www.emirates.com/english/sitetools/privacy_policy.aspx) d'Emirates elle-même n'est pas très claire. Elle [mentionne certains de ces services](https://www.emirates.com/english/sitetools/cookie-policy.aspx), mais pas tous ou les données partagées avec eux.

#### **Puis-je ne pas me désinscrire ?**

Ce n'est pas une option. Malheureusement, je n'ai pas trouvé de moyen de me désinscrire de ce système fourni par Emirates. J'ai finalement dû recourir à l'utilisation d'extensions de navigateur préservant la vie privée.

#### **Emirates ne peut-il pas corriger cela ?**

En tant qu'ingénieur logiciel ayant travaillé pour certaines des plus grandes entreprises de commerce électronique, je comprends le besoin d'utiliser des services tiers pour optimiser et améliorer non seulement le produit numérique mais aussi la manière dont l'utilisateur interagit avec le produit.

Ce n'est pas l'utilisation de services tiers qui est préoccupante dans ce cas, mais la mise en œuvre de ces services. Emirates a le contrôle de son site web et de ce que le site web partage avec les services tiers. C'est ce contrôle qui doit être exercé pour limiter la fuite d'informations des utilisateurs.

Ce n'est pas une tâche colossale, c'est simplement une question d'engagement à préserver le droit fondamental à la vie privée.

Par exemple :

1. Les pages privées doivent avoir des [balises meta noindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta).
2. Limiter la présence de services tiers sur les pages privées.
3. [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) sur les pages avec des données sensibles.
4. Mettre en œuvre CSP et SRI. Même avec une grande empreinte de services tiers, [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), [SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) ne sont pas activés sur Emirates.com
5. L'utilisateur doit être informé lorsque des informations sensibles comme le passeport, les coordonnées, etc., sont mises à jour, modifiées ou supprimées.
6. Domaine pour l'envoi d'e-mails : track.emirates.email, doit avoir un certificat valide. [https://track.emirates.email/](https://track.emirates.email/)

![Image](https://cdn-media-1.freecodecamp.org/images/n04rAIAp6Z1zBmHuWz4symTvtvVt7W-nTKOP)

Si vous êtes intéressé à en savoir plus sur la présence de trackers sur vos sites web préférés, je vous recommande vivement de consulter [WhoTracksMe](https://whotracks.me/).

**_Mises à jour:_**

**_- 6 mars 2018:_**

_Emirates a répondu avec une déclaration standard._

_Extrait : « La représentation dans l'article de M. Modi quant aux données partagées, ou au choix du client de « se désinscrire » est inexacte. »_

_Voici ma réponse : [Fuites de confidentialité aller-retour : Emirates.com dans le déni](https://medium.com/@konarkmodi/privacy-leaks-round-trip-emirates-com-in-denial-7f99950bcdd)_

Bon piratage !

- [Konark Modi](https://twitter.com/konarkmodi)

Merci d'avoir lu et partagé ! :)

Si vous avez aimé cette histoire, n'hésitez pas à ??? quelques fois (Jusqu'à 50 fois. Sérieusement).

_Crédits : Un merci spécial à [Remi](https://twitter.com/Pythux), [Pallavi](https://twitter.com/Pi_Modi) pour avoir relu l'article._