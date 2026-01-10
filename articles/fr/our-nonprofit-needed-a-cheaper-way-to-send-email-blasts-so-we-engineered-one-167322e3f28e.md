---
title: Notre organisation à but non lucratif avait besoin d'une solution moins chère
  pour envoyer des emails en masse. Nous en avons donc conçu une.
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-09-15T14:56:46.000Z'
originalURL: https://freecodecamp.org/news/our-nonprofit-needed-a-cheaper-way-to-send-email-blasts-so-we-engineered-one-167322e3f28e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*th13skTPFs53EtCuupOYQA.jpeg
tags: []
seo_title: Notre organisation à but non lucratif avait besoin d'une solution moins
  chère pour envoyer des emails en masse. Nous en avons donc conçu une.
seo_desc: 'Every week, I send an email blast to a million people who’ve signed up
  for freeCodeCamp.org.

  These are high-deliverability emails — sent through Amazon Web Services — and they
  only cost our nonprofit $0.0001 each.

  This means I’m able to send out all ...'
---

Chaque semaine, j'envoie un email en masse à un million de personnes qui se sont inscrites sur freeCodeCamp.org.

Ces emails ont un taux de livraison élevé — envoyés via Amazon Web Services — et ne coûtent que 0,0001 $ chacun à notre organisation à but non lucratif.

Cela signifie que je peux envoyer les 1 000 000 emails — tout en évitant la plupart des filtres anti-spam — pour un total de seulement 100 $.

Et depuis un an, j'utilise un nouvel outil pour envoyer ces emails. Il me offre une interface navigateur pratique avec de nombreuses fonctionnalités avancées pour les campagnes email :

* Modèles HTML
* Tableaux de bord analytiques
* Suivi des ouvertures d'emails (pixels de suivi)
* Suivi des clics (liens de suivi)
* Widgets d'inscription intégrés
* Fonctionnalité de désabonnement
* Importation et exportation de listes
* Permissions d'accès aux données basées sur les rôles

Nous avons développé cet outil en interne.

Il est complètement gratuit.

Il est complètement open source.

Il s'appelle **Mail for Good**.

Et aujourd'hui, nous le rendons public. Il passe en bêta ouverte. Les organisations à but non lucratif du monde entier peuvent commencer à l'utiliser immédiatement.

![Image](https://cdn-media-1.freecodecamp.org/images/gRZE6urv7xUmwt0xFx3v4c6wX9f0DR2Sjkgi)
_Une capture d'écran de l'interface basée sur navigateur de Mail for Good_

### Mail for Good est un outil de marketing par email ultra-économique et à haute livraison pour les organisations à but non lucratif.

D'accord — si vous êtes déjà convaincu et prêt à l'utiliser, [voici le dépôt GitHub](https://github.com/freeCodeCamp/mail-for-good). Allez-y et faites du monde un endroit meilleur.

Mais si vous vous demandez encore si quelque chose comme Mail for Good est adapté à votre organisation, laissez-moi vous donner plus de détails.

### Mail for Good est le moyen le moins cher d'envoyer des emails avec un taux de livraison élevé.

Il est gratuit et open source. Vous avez juste besoin d'un serveur pour le faire fonctionner. Nous l'exécutons sur un serveur cloud à 10 $ par mois. Vous pourriez faire de même. Ou vous pourriez simplement l'exécuter sur l'un de vos serveurs existants gratuitement.

Ensuite, vous payez Amazon 1 $ pour 10 000 emails envoyés via leur service Simple Email Service.

Si vous avez un million d'emails dans votre liste de diffusion, et que vous envoyez une campagne par mois, cela signifie que vous dépenseriez 100 $ par mois.

Disons que vous envoyez une campagne par semaine. Alors vous dépenseriez 400 $ par mois.

Disons que vous envoyez trois campagnes par semaine. Alors vous dépenseriez 1 200 $ par mois.

Pour référence, voici combien cela coûte pour héberger une liste de diffusion d'un million d'abonnés sur MailChimp — indépendamment du fait que vous leur envoyiez des emails : **4 399 $ par mois**.

![Image](https://cdn-media-1.freecodecamp.org/images/kPP0SMSZf58aBgf-OMKE4Zfwht0YzX0S3pjp)
_MailChimp coûte 4 200 $ + 199 $ chaque mois pour une liste de diffusion de 1 000 000 abonnés._

Et les autres outils de campagne email ne sont pas beaucoup moins chers. La plupart d'entre eux ne vous diront même pas leurs tarifs à moins que vous les appeliez.

![Image](https://cdn-media-1.freecodecamp.org/images/LGG6N6yFGicgJ7NB0Z0APgZf5s2YJy6MT)

### Avec Mail for Good, _vos_ données de liste d'emails restent sur votre serveur.

Vous n'avez pas à vous soucier qu'un service d'email tiers soit piraté et que les adresses email de vos abonnés soient compromises. Vous contrôlez toutes les données de votre organisation.

Si vous souhaitez qu'un membre de votre équipe — ou même un bénévole — puisse concevoir des modèles d'emails ou consulter les analyses, vous pouvez lui donner la permission de le faire — sans lui donner accès à vos données.

Vous pouvez également facilement importer et exporter vos données. Et vous pouvez maintenir autant de listes de diffusion que vous le souhaitez.

### Mail for Good reçoit de nouvelles fonctionnalités tout le temps.

Puisque Mail for Good est open source (avec la licence permissive BSD-3), toute organisation qui l'utilise peut facilement contribuer ses améliorations.

Et la communauté freeCodeCamp contribue activement et maintient Mail for Good. Il devrait donc continuer à s'améliorer régulièrement avec le temps.

Les futures versions incluront des fonctionnalités comme les tests A/B, et des intégrations avec d'autres outils populaires utilisés par les organisations à but non lucratif.

Tout est coordonné ouvertement sur GitHub. Toute personne peut demander une fonctionnalité spécifique dont elle a besoin pour son organisation, ou signaler un bug qu'elle a découvert, [en ouvrant une issue GitHub](https://github.com/freeCodeCamp/mail-for-good/issues).

### Questions Fréquemment Posées

#### Dois-je faire partie d'une organisation à but non lucratif pour utiliser Mail for Good ?

Tout le monde peut utiliser Mail for Good. Nous sommes une organisation à but non lucratif, et nous avons construit cet outil en pensant aux organisations à but non lucratif. Mais les entrepreneurs, les entreprises, et même les gouvernements pourraient utiliser Mail for Good et économiser une somme considérable d'argent dans le processus.

#### Comment puis-je installer Mail for Good ?

Sauf si vous avez déjà vos propres serveurs, nous recommandons de configurer un serveur cloud sur Amazon Web Services. Amazon est économique, sécurisé, et de nombreuses organisations l'utilisent — y compris Netflix. [Voici des instructions détaillées pour configurer Mail for Good sur Amazon](https://github.com/freeCodeCamp/mail-for-good/blob/master/docs/aws_deploy.md).

#### Qui a construit Mail for Good ?

Mail for Good a déjà nécessité des milliers d'heures de travail de développement jusqu'à présent. Le maintenir et étendre ses fonctionnalités nécessitera des milliers d'heures supplémentaires.

Jusqu'à présent, tout cela a été fait par des contributeurs bénévoles, sur une période d'environ un an.

Voici quelques-unes des personnes qui ont été instrumentales dans son développement jusqu'à présent :

* [Andrew Walsh](https://github.com/AndrewGHC)
* [Ian Hawes](https://github.com/4iar)
* [Valentin Dupas](https://github.com/zhakkarn)
* [Carl Kashnier](https://github.com/CarlJKashnier)
* [Michael D. Johnson](https://github.com/CodeNonprofit)
* [Joel Bentley](https://github.com/joel-bentley)

#### Comment puis-je aider ce projet ?

La manière la plus immédiate d'aider est de l'utiliser pour les campagnes email de votre organisation. Nous ne collectons aucune de vos données d'utilisation, donc la seule façon pour nous de savoir ce que vous en pensez est que vous nous le disiez. Vous pouvez également signaler les bugs que vous rencontrez.

Si vous souhaitez contribuer au code du projet, rejoignez [le salon de discussion Gitter de Mail for Good](https://gitter.im/FreeCodeCamp/mail-for-good) et présentez-vous.

Mail for Good n'est qu'un des nombreux outils que la communauté freeCodeCamp développe pour aider les organisations à but non lucratif à accomplir plus avec moins. Si vous souhaitez soutenir les efforts de notre organisation à but non lucratif, vous pouvez [configurer un don mensuel que vous pouvez vous permettre](https://www.freecodecamp.org/donate).

Merci d'avoir lu. Bon envoi d'emails !