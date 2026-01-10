---
title: Comment les entreprises obtiennent vos données – et ce qu'elles peuvent en
  faire
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2020-10-05T14:03:48.000Z'
originalURL: https://freecodecamp.org/news/how-companies-get-your-data
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/company-data.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: data
  slug: data
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Comment les entreprises obtiennent vos données – et ce qu'elles peuvent
  en faire
seo_desc: 'Curious about what kinds of personal and even private data you may be exposing
  through the course of a normal day on the internet? How about using “all kinds”
  as a starting point?

  Here, adapted from my new book, Keeping Up: Backgrounders to all the b...'
---

Curieux de savoir quels types de données personnelles et même privées vous pourriez exposer au cours d'une journée normale sur Internet ? Et si nous utilisions « tous types » comme point de départ ?

Voici, adapté de mon nouveau livre, _[Keeping Up: Backgrounders to all the big technology trends you can't afford to ignore](https://www.amazon.com/Keeping-Up-backgrounders-technology-trends/dp/B08HGLPZMP)_, une manière de décomposer l'ampleur et la nature du problème par plateforme.

## Transactions financières

Prenez un moment pour visualiser ce qui est impliqué dans un simple achat en ligne par carte de crédit. Vous avez probablement signé sur le site du marchand en utilisant votre adresse e-mail comme identifiant de compte et un mot de passe (espérons-le) unique. Après avoir parcouru quelques pages, vous ajouterez un ou plusieurs articles au panier d'achat virtuel du site.

Lorsque vous avez tout ce dont vous avez besoin, vous commencez le processus de paiement, en entrant les informations de livraison, y compris une adresse postale et votre numéro de téléphone. Vous pourriez également entrer le numéro de compte de la carte de fidélité que le marchand vous a envoyée et un code de coupon que vous avez reçu dans un message marketing par e-mail.

Bien sûr, l'étape clé implique d'entrer vos informations de paiement. Pour une carte de crédit, cela inclura probablement le nom et l'adresse du titulaire de la carte, ainsi que le numéro de la carte, la date d'expiration et un code de sécurité.

En supposant que l'infrastructure du marchand soit conforme aux protocoles Payment Card Industry Data Security Standard (PCI-DSS) pour la gestion des informations financières, il est relativement peu probable que ces informations soient volées et vendues par des criminels. Mais dans tous les cas, elles existeront toujours dans la base de données du marchand.

Pour approfondir un peu, comprenez que l'utilisation de votre compte de carte de fidélité et d'un code de coupon peut communiquer beaucoup d'informations sur vos préférences d'achat et de mode de vie. Sans parler des enregistrements de certaines de vos activités précédentes. Et votre compte sur le site vient avec des informations de contact et votre localisation.

Toutes ces informations peuvent, au moins en théorie, être assemblées pour créer un profil robuste de vous en tant que consommateur et citoyen.

C'est pour ces raisons que je préfère personnellement utiliser des systèmes de paiement e-commerce tiers comme PayPal, car de telles transactions ne laissent aucune trace de ma méthode de paiement spécifique dans les bases de données du marchand.

## Appareils

Les systèmes d'exploitation modernes sont conçus dès le départ pour se connecter à Internet de multiples façons. Ils interrogent souvent automatiquement les dépôts de logiciels en ligne pour les correctifs et mises à jour et « demandent » de l'aide à distance lorsque quelque chose ne va pas.

Certaines données de diagnostic de performance sont envoyées et stockées en ligne, où elles peuvent contribuer à l'analyse statistique ou au diagnostic et à la correction de bugs. Les logiciels individuels peuvent se connecter à des serveurs distants indépendamment du système d'exploitation pour accomplir leurs propres tâches.

Tout cela est bien. Sauf que vous pourriez avoir du mal à être sûr que toutes les données circulant entre votre appareil et Internet sont des choses que vous êtes d'accord pour partager.

Pouvez-vous savoir que des fichiers privés et des informations personnelles ne sont pas balayés avec toutes les autres données ? Et êtes-vous sûr qu'aucune de vos données ne se retrouvera jamais accidentellement dans une application inattendue échappant à votre contrôle ?

Pour illustrer le problème, je vous renvoie aux appareils alimentés par des assistants numériques comme Alexa d'Amazon et l'Assistant Google (« OK Google »). Puisque, par définition, les microphones utilisés par les assistants numériques écoutent constamment leur mot clé (« Alexa… »), tout ce que dit quiconque à portée de l'appareil est enregistré.

Au moins certaines de ces conversations sont également enregistrées et stockées en ligne et, comme il s'avère, certaines d'entre elles ont finalement été entendues par des êtres humains travaillant pour le vendeur. Dans au moins un cas, une conversation enregistrée par inadvertance a été utilisée pour condamner un suspect de meurtre (ce qui ne signifie pas que nous sommes opposés à la condamnation des meurtriers).

Amazon, Google et d'autres acteurs de ce domaine sont conscients du problème et tentent de le résoudre. Mais il est peu probable qu'ils le résolvent jamais complètement. Rappelez-vous, la commodité, la sécurité et la confidentialité ne fonctionnent pas bien ensemble.

Maintenant, si vous pensez que les informations des ordinateurs et des tablettes qui peuvent être suivies et enregistrées sont effrayantes, attendez de entendre parler des thermostats et des ampoules.

À mesure que de plus en plus d'appareils électroménagers et d'outils sont adoptés dans le cadre des systèmes de « maison intelligente », de plus en plus de flux de données de performance seront générés avec eux.

Et, comme cela a déjà été démontré dans de multiples applications réelles, toutes ces données peuvent être interprétées de manière programmatique pour révéler des informations significatives sur ce qui se passe dans une maison et qui le fait.

## Appareils mobiles

Vous êtes-vous déjà arrêté au milieu d'un trajet, sorti votre smartphone et vérifié une carte numérique pour des directions ? Bien sûr que oui.

Eh bien, l'application de carte utilise vos informations de localisation actuelles et vous envoie des informations précieuses, mais en même temps, vous envoyez certaines informations tout aussi précieuses en retour. Quel type d'informations cela pourrait-il être ?

J'ai déjà lu l'histoire d'un individu facétieux en Allemagne qui a emprunté quelques dizaines de smartphones, les a chargés sur une remorque pour enfants et a lentement tiré la remorque au milieu d'une rue de ville vide. Il n'a pas fallu longtemps avant que Google Maps ne signale un sérieux embouteillage là où il n'y en avait pas.

Comment l'application Google Maps en sait-elle plus sur les conditions de circulation locales que vous ? Une classe importante de données qui alimente leur système est obtenue par la surveillance constante de la localisation, de la vitesse et de la direction de mouvement de chaque téléphone Android actif qu'ils peuvent atteindre - y compris votre téléphone Android.

Pour ma part, j'apprécie ce service et cela ne me dérange pas trop la façon dont mes données sont utilisées. Mais je suis également conscient que, un jour, ces données pourraient être utilisées de manière à entrer en conflit avec mes intérêts. Appelez cela un risque calculé.

Bien sûr, ce ne sont pas seulement les informations de mouvement basées sur le GPS que Google et Apple - les créateurs des deux systèmes d'exploitation mobiles les plus populaires - obtiennent. Ils, ainsi que quelques autres acteurs de l'industrie, gèrent également les enregistrements de toutes nos activités sur les moteurs de recherche et les données retournées par les applications de surveillance de l'exercice et de la santé.

En d'autres termes, s'ils décident de le faire, de nombreuses entreprises technologiques pourraient compiler sans effort des profils décrivant nos mouvements précis, nos plans et notre état de santé. Et à partir de là, il n'y a pas un grand pas à faire pour imaginer les propriétaires de telles données prédire ce que nous sommes susceptibles de faire dans les semaines et les mois à venir.

## Navigateurs web

La plupart d'entre nous utilisent des navigateurs web pour nos interactions quotidiennes avec Internet. Et, tout bien considéré, les navigateurs web sont des créations assez miraculeuses. Ils agissent souvent comme un concierge incroyablement puissant, nous apportant toutes les richesses de l'humanité sans même transpirer.

Mais, comme je suis sûr que vous pouvez déjà l'anticiper, toute cette puissance s'accompagne d'un compromis.

Pour avoir un aperçu des informations que votre navigateur partage librement sur vous, jetez un coup d'œil à la page Google Analytics illustrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-116.png)

Ce tableau de bord affiche un résumé visuel décrivant toutes les visites sur mon propre [site bootstrap-it.com](https://bootstrap-it.com/) au cours des sept derniers jours. À partir des données collectées, je peux voir :

* D'où dans le monde viennent mes visiteurs
* À quel moment de la journée ils ont tendance à visiter
* Combien de temps ils ont passé sur mon site
* Quelles pages ils visitent
* Quel site ils ont quitté avant de venir sur mon site
* Combien de visiteurs font des visites répétées
* Quels systèmes d'exploitation ils utilisent
* Quel facteur de forme d'appareil ils utilisent (c'est-à-dire, ordinateur de bureau, smartphone ou tablette)
* Les cohortes démographiques auxquelles ils appartiennent (genres, groupes d'âge, groupes de revenus)

En plus de tout cela, les journaux propres d'un serveur web peuvent rapporter des informations détaillées, en particulier l'adresse IP spécifique et l'heure précise associée à chaque visiteur.

Ce que cela signifie, c'est que, chaque fois que votre navigateur se connecte à mon site web (ou à tout autre site web), il donne à mon serveur web une quantité énorme d'informations. Google les collecte simplement et me les présente dans un format élégant et facile à digérer.

À propos, je suis pleinement conscient qu'en laissant Google collecter toutes ces informations sur les utilisateurs de mon site web, je fais partie du problème. Et, pour la record, je me sens un peu coupable à ce sujet.

De plus, les serveurs web sont capables de « surveiller » ce que vous faites en temps réel et de « se souvenir » de ce que vous avez fait lors de votre dernière visite.

Pour expliquer, avez-vous déjà remarqué comment, sur certains sites, juste avant de cliquer pour quitter la page, un message « Attendez ! Avant de partir ! » s'affiche ? Les serveurs peuvent suivre vos mouvements de souris et, lorsqu'ils se rapprochent « trop » de la fermeture de l'onglet ou du passage à un autre onglet, ils affichent cette fenêtre contextuelle.

De même, de nombreux sites enregistrent de petits paquets de données sur votre ordinateur appelés « cookies ». Un tel cookie pourrait contenir des informations de session qui pourraient inclure le contenu précédent d'un panier d'achat ou même votre statut d'authentification. Le but est de fournir une expérience pratique et cohérente sur plusieurs visites. Mais de tels outils peuvent être mal utilisés.

Enfin, comme les systèmes d'exploitation, les navigateurs communiqueront également silencieusement avec le fournisseur qui les fournit. Obtenir des commentaires sur l'utilisation peut aider les fournisseurs à rester à jour sur les problèmes de sécurité et de performance. Mais des tests indépendants ont montré que, dans de nombreux cas, beaucoup plus de données sont renvoyées « à la maison » que ce qui semblerait approprié.

## Interaction avec les sites web

Bien que je traite de cela plus en profondeur dans [mon livre "Keeping Up"](https://www.amazon.com/Keeping-Up-backgrounders-technology-trends/dp/B08HGLPZMP), je devrais souligner au moins quelques problèmes particulièrement pertinents ici. Comme, par exemple, le fait que les sites web adorent vous faire signer pour des services à valeur ajoutée.

Les newsletters et les mises à jour de produits qu'ils vous enverront pourraient être parfaitement légitimes et, en effet, fournir une grande valeur. Mais elles arrivent toujours en échange de certaines de vos informations de contact privées. Tant que vous en êtes conscient, j'ai fait mon travail.

Un exemple parfait est les données que vous contribuez aux plateformes de médias sociaux comme Twitter, Facebook et LinkedIn. Vous pourriez penser que vous ne communiquez qu'avec vos connexions et followers, mais cela va en réalité beaucoup plus loin.

Prenez un logiciel merveilleux - et effrayant - appelé Recon-ng qui est utilisé par les professionnels de la sécurité réseau pour tester la vulnérabilité numérique d'une organisation. Une fois que vous l'avez configuré avec quelques bases sur votre organisation, Recon-ng se rendra sur Internet et recherchera toute information publique disponible qui pourrait être utilisée pour pénétrer vos défenses ou vous causer du tort.

Par exemple, êtes-vous sûr que des étrangers ne peuvent pas savoir assez sur l'environnement logiciel avec lequel vos développeurs travaillent pour vous causer des dommages ? Eh bien, peut-être devriez-vous jeter un coup d'œil à la section « qualifications souhaitées » de certaines de ces annonces d'emploi que vous avez publiées sur LinkedIn. Ou que dire des questions (ou réponses) que vos développeurs pourraient avoir publiées sur le site Stack Overflow ?

Chaque publication raconte une histoire, et il ne manque pas de personnes intelligentes qui adorent lire des histoires.

Des logiciels comme Recon-ng peuvent vous aider à identifier les menaces potentielles. Mais cela souligne uniquement votre responsabilité d'éviter de laisser vos données en public en premier lieu.

Le message final ? Souriez. Vous êtes observé.

_Il y a beaucoup plus de bonnes informations technologiques rapides, amusantes et accessibles disponibles dans mon livre [Keeping Up](https://www.amazon.com/Keeping-Up-backgrounders-technology-trends/dp/B08HGLPZMP). Jetez un coup d'œil._