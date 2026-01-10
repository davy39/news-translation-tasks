---
title: Qu'est-ce que la vie privée numérique ? Un guide pour débutants pour protéger
  vos données
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-10T17:45:33.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-digital-privacy
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-kevin-paster-1901388.jpg
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
seo_title: Qu'est-ce que la vie privée numérique ? Un guide pour débutants pour protéger
  vos données
seo_desc: "For all the many benefits we enjoy from technology – and particularly the\
  \ technologies that make up the public internet – there are plenty of costs, too.\
  \ \nFiguring out how you want to balance the benefits against the costs can take\
  \ some careful think..."
---

Pour tous les nombreux avantages que nous tirons de la technologie – et particulièrement des technologies qui composent l'internet public – il y a aussi beaucoup de coûts.

Déterminer comment vous souhaitez équilibrer les avantages par rapport aux coûts peut nécessiter une réflexion minutieuse. Voici une manière concise et efficace de décrire l'équation (dont la source, hélas, m'a échappé) :

> "Choisissez deux des trois éléments suivants : vie privée, sécurité et commodité. Mais vous ne pouvez pas avoir les trois."

En d'autres termes, si la sécurité est une valeur critique pour vous, alors vous devrez renoncer à un accès instantané 24h/24 et 7j/7 à votre argent, à votre crédit et à vos comptes personnels. Cela est dû au fait que ce type d'accès nécessite d'exposer vos comptes sur des réseaux publics à un niveau qui ne permettra pas autant de protection des données que vous pourriez souhaiter.

De même, que se passe-t-il si vous ne pouvez tout simplement pas vivre sans la commodité de recevoir des mises à jour d'actualités et une connectivité sociale via des sites appartenant à des entreprises tierces qui collectent et utilisent vos informations personnelles ? Eh bien, vous devrez "payer pour cela" en renonçant à une partie de votre vie privée.

Ce tutoriel a été tiré de mon livre, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). Si vous préférez regarder ce chapitre sous forme de vidéo, n'hésitez pas à suivre ici :

%[https://www.youtube.com/watch?v=p7PmzNLzUws]

Bien sûr, la plupart d'entre nous choisiront un mélange de ces trois éléments basé sur un compromis pratique entre des valeurs et des besoins concurrents. Mais prendre une décision raisonnable sur ce mélange nécessitera des informations solides. C'est ce que vous trouverez dans le reste de cet article.

# Comment les entreprises obtiennent vos données

Vous vous demandez quels types de données personnelles et même privées vous pourriez exposer au cours d'une journée normale sur internet ?

Et si nous commençons par "tous les types" ? Peut-être que la meilleure façon de comprendre l'ampleur et la nature du problème est de le décomposer par plateforme.

## Données issues des transactions financières

Prenez un moment pour visualiser ce qui est impliqué dans une simple transaction par carte de crédit en ligne. Vous avez probablement signé sur le site web du marchand en utilisant votre adresse e-mail comme identifiant de compte et un mot de passe (espérons-le) unique.

Après avoir parcouru quelques pages, vous ajouterez un ou plusieurs articles au panier d'achat virtuel du site. Lorsque vous avez tout ce dont vous avez besoin, vous commencez le processus de paiement, en entrant les informations de livraison, y compris une adresse postale et votre numéro de téléphone. Vous pourriez également entrer le numéro de compte de la carte de fidélité que le marchand vous a envoyée et un code de coupon que vous avez reçu dans un message marketing par e-mail.

Bien sûr, l'étape clé consiste à entrer vos informations de paiement qui, pour une carte de crédit, incluront probablement le nom et l'adresse du titulaire de la carte, ainsi que le numéro de la carte, la date d'expiration et un code de sécurité.

En supposant que l'infrastructure du marchand soit conforme aux protocoles Payment Card Industry Data Security Standard (PCI-DSS) pour la gestion des informations financières, il est relativement peu probable que ces informations soient volées et vendues par des criminels. Mais dans tous les cas, elles existeront toujours dans la base de données du marchand.

Pour approfondir un peu, comprenez que l'utilisation de votre compte de carte de fidélité et d'un code de coupon peut communiquer beaucoup d'informations sur vos préférences d'achat et de mode de vie, ainsi que des enregistrements de certaines de vos activités précédentes.

Votre compte sur le site contient des informations de contact et votre localisation. Toutes ces informations peuvent, au moins en théorie, être assemblées pour créer un profil robuste de vous en tant que consommateur et citoyen.

C'est pour ces raisons que je préfère personnellement utiliser des systèmes de paiement e-commerce tiers comme PayPal, car de telles transactions ne laissent aucune trace de ma méthode de paiement spécifique dans les bases de données du marchand.

## Données issues des appareils

Les systèmes d'exploitation modernes sont conçus dès le départ pour se connecter à internet de multiples façons. Ils interrogent souvent automatiquement les dépôts de logiciels en ligne pour les correctifs et les mises à jour et "demandent" de l'aide à distance lorsque quelque chose ne va pas.

Certaines données de diagnostic de performance sont envoyées et stockées en ligne, où elles peuvent contribuer à l'analyse statistique ou au diagnostic et à la correction de bugs. Les logiciels individuels peuvent se connecter à des serveurs distants indépendamment du système d'exploitation pour accomplir leurs propres tâches.

Tout cela est bien. Sauf que vous pourriez avoir du mal à être sûr que _toutes_ les données circulant entre votre appareil et internet sont des choses que vous êtes d'accord pour partager.

Pouvez-vous savoir que des fichiers privés et des informations personnelles ne sont pas balayés avec toutes les autres données ? Et êtes-vous sûr qu'aucune de vos données ne se retrouvera jamais accidentellement dans une application inattendue échappant à votre contrôle ?

Pour illustrer le problème, je vous renvoie aux appareils alimentés par des assistants numériques comme Alexa d'Amazon et l'Assistant Google ("Ok Google"). Puisque, par définition, les microphones utilisés par les assistants numériques écoutent constamment leur mot clé ("Alexa..."), tout ce que dit quiconque à portée de l'appareil est enregistré.

Au moins certaines de ces conversations sont également enregistrées et stockées en ligne et, comme il s'est avéré, certaines d'entre _elles_ ont finalement été entendues par des êtres humains travaillant pour le vendeur. Dans au moins un cas, une conversation enregistrée par inadvertance a été utilisée pour condamner un suspect de meurtre.

Amazon, Google et d'autres acteurs de ce domaine sont conscients du problème et tentent de le résoudre. Mais il est peu probable qu'ils le résolvent jamais complètement. Rappelez-vous, commodité, sécurité et vie privée ne fonctionnent pas bien ensemble.

Maintenant, si vous pensez que les informations des ordinateurs et des tablettes qui peuvent être suivies et enregistrées sont effrayantes, attendez de entendre parler des thermostats et des ampoules.

À mesure que de plus en plus d'appareils ménagers et d'outils sont adoptés dans le cadre des systèmes "maison intelligente", de plus en plus de flux de données de performance seront générés avec eux.

Et, comme cela a déjà été démontré dans de multiples applications réelles, toutes ces données peuvent être interprétées de manière programmatique pour révéler des informations significatives sur ce qui se passe dans une maison et qui le fait.

## Données issues des appareils mobiles

Vous êtes-vous déjà arrêté en plein voyage, sorti votre smartphone et vérifié une carte numérique pour des directions ? Bien sûr que oui.

Eh bien, l'application de carte utilise vos informations de localisation actuelles et vous envoie des informations précieuses, mais en même temps, vous envoyez des informations tout aussi précieuses en retour. Quel type d'informations cela pourrait-il être ?

J'ai déjà lu l'histoire d'un individu facétieux en Allemagne qui a emprunté quelques dizaines de smartphones, les a chargés sur une remorque pour enfants et a lentement tiré la remorque au milieu d'une rue de ville vide. Il n'a pas fallu longtemps avant que Google Maps ne signale un sérieux embouteillage là où il n'y en avait pas.

Comment l'application Google Maps en sait-elle plus sur les conditions de circulation locales que vous ? Une classe importante de données qui alimente leur système est obtenue par la surveillance constante de la localisation, de la vitesse et de la direction de mouvement de chaque téléphone Android actif qu'ils peuvent atteindre - y compris votre téléphone Android.

Pour ma part, j'apprécie ce service et je ne me soucie pas trop de la manière dont mes données sont utilisées. Mais je suis également conscient que, un jour, ces données pourraient être utilisées de manière à entrer en conflit avec mes intérêts. Appelez cela un risque calculé.

Bien sûr, ce ne sont pas seulement les informations de mouvement basées sur le GPS que Google et Apple – les créateurs des deux systèmes d'exploitation mobiles les plus populaires – obtiennent. Ils, ainsi que quelques autres acteurs de l'industrie, gèrent également les enregistrements de toutes nos activités sur les moteurs de recherche et les données retournées par les applications de surveillance de l'exercice et de la santé.

En d'autres termes, s'ils décident de le faire, de nombreuses entreprises technologiques pourraient compiler sans effort des profils décrivant nos mouvements précis, nos plans et notre état de santé. Et à partir de là, il n'est pas difficile d'imaginer les propriétaires de telles données prédisant ce que nous sommes susceptibles de faire dans les semaines et les mois à venir.

## Données issues des navigateurs web

La plupart d'entre nous utilisent des navigateurs web pour la plupart de nos interactions quotidiennes avec internet. Et, tout bien considéré, les navigateurs web sont des créations assez miraculeuses, agissant souvent comme un concierge incroyablement puissant, nous apportant toutes les richesses de l'humanité sans même transpirer. Mais, comme je suis sûr que vous pouvez déjà l'anticiper, tout ce pouvoir s'accompagne d'un compromis.

Pour avoir un aperçu des informations que votre navigateur partage librement sur vous, jetez un coup d'œil à la page Google Analytics illustrée dans l'image ci-dessous. Ce tableau de bord affiche un résumé visuel décrivant toutes les visites sur mon propre site bootstrap-it.com au cours des sept derniers jours. Je peux voir :

* D'où dans le monde viennent mes visiteurs
* À quel moment de la journée ils ont tendance à visiter
* Combien de temps ils ont passé sur mon site
* Quelles pages ils visitent
* Quel site ils ont quitté avant de venir sur mon site
* Combien de visiteurs font des visites répétées
* Quels systèmes d'exploitation ils utilisent
* Quel facteur de forme d'appareil ils utilisent (c'est-à-dire, bureau, smartphone ou tablette)
* Les cohortes démographiques auxquelles ils appartiennent (genres, groupes d'âge, groupes de revenus)

![Image](https://www.freecodecamp.org/news/content/images/2022/12/figure2-2.png)
_Le tableau de bord d'accueil d'une page Google Analytics affichant des visualisations des visiteurs d'un site web._

En plus de tout cela, les propres journaux d'un serveur web peuvent rapporter des informations détaillées, en particulier l'adresse IP spécifique et l'heure précise associée à chaque visiteur.

Cela signifie que, chaque fois que votre navigateur se connecte à mon site web (ou à tout autre site web), il donne à mon serveur web une quantité énorme d'informations. Google les collecte simplement et me les présente dans un format élégant et facile à digérer.

À propos, je suis pleinement conscient qu'en laissant Google collecter toutes ces informations sur les utilisateurs de mon site web, je fais partie du problème. Et, pour la record, je me sens un peu coupable à ce sujet.

De plus, les serveurs web sont capables de "surveiller" ce que vous faites en temps réel et de "se souvenir" de ce que vous avez fait lors de votre dernière visite.

Pour expliquer, avez-vous déjà remarqué comment, sur certains sites, juste avant de cliquer pour quitter la page, un message "Attendez ! Avant de partir !" apparaît ? Les serveurs peuvent suivre les mouvements de votre souris et, lorsqu'ils se rapprochent "trop" de la fermeture de l'onglet ou du passage à un autre onglet, ils afficheront cette fenêtre contextuelle.

De même, de nombreux sites enregistrent de petits paquets de données sur votre ordinateur appelés "cookies". Un tel cookie pourrait contenir des informations de session qui pourraient inclure le contenu précédent d'un panier d'achat ou même votre statut d'authentification. Le but est de fournir une expérience pratique et cohérente sur plusieurs visites. Mais de tels outils peuvent être mal utilisés.

Enfin, comme les systèmes d'exploitation, les navigateurs communiqueront également en silence avec le fournisseur qui les fournit. Obtenir des commentaires sur l'utilisation peut aider les fournisseurs à rester à jour sur les problèmes de sécurité et de performance. Mais des tests indépendants ont montré que, dans de nombreux cas, beaucoup plus de données sont envoyées "à la maison" que ce qui semblerait approprié.

## Données issues des interactions avec les sites web

Bien que certains de ces points puissent être couverts par les sections précédentes de cet article, je devrais souligner au moins quelques problèmes particulièrement pertinents.

Par exemple, le fait que les sites web adorent vous faire signer pour des services à valeur ajoutée. Les newsletters et les mises à jour de produits qu'ils vous enverront peuvent être parfaitement légitimes et, en effet, fournir une grande valeur – mais elles sont toujours échangées contre certaines de vos informations de contact privées. Tant que vous en êtes conscient, j'ai fait mon travail.

Un exemple parfait est les données que vous contribuez aux plateformes de médias sociaux comme Twitter, Facebook et LinkedIn. Vous pouvez penser que vous communiquez simplement avec vos connexions et vos abonnés, mais cela va en réalité beaucoup plus loin.

Prenez un logiciel merveilleux – et effrayant – appelé Recon-ng, utilisé par les professionnels de la sécurité réseau pour tester la vulnérabilité numérique d'une organisation. Une fois que vous l'avez configuré avec quelques bases sur votre organisation, Recon-ng se rendra sur internet et recherchera toute information publique disponible qui pourrait être utilisée pour pénétrer vos défenses ou vous causer du tort.

Par exemple, êtes-vous sûr que des étrangers ne peuvent pas savoir suffisamment sur l'environnement logiciel avec lequel vos développeurs travaillent pour vous causer des dommages ? Eh bien, peut-être devriez-vous jeter un coup d'œil à la section "qualifications" de certaines de ces annonces d'emploi que vous avez publiées sur LinkedIn.

Ou que dire des questions (ou réponses) que vos développeurs pourraient avoir publiées sur Stack Overflow ? Chaque publication raconte une histoire, et il ne manque pas de personnes intelligentes qui adorent lire des histoires.

Des logiciels comme Recon-ng peuvent vous aider à identifier les menaces potentielles, mais cela souligne simplement votre responsabilité d'éviter de laisser vos données accessibles au public en premier lieu.

Le message final ? Souriez. Vous êtes surveillé.

# Pourquoi les entreprises veulent vos données

Les données, c'est de l'argent. Certaines des plus grandes et des plus réussies entreprises technologiques de la dernière décennie ou deux ont fait leurs milliards grâce aux données. Généralement, ce serait grâce à vos données.

Bien sûr, la valeur ne va pas toutes dans une seule direction. Les grandes entreprises technologiques fournissent, en règle générale, des services utiles.

Les applications de suivi de la santé suivent et rapportent effectivement votre santé. Les entreprises de médias sociaux fournissent (à de rares occasions) des interactions sociales saines. Et les données de performance historiques aident parfois à améliorer le service client et technique.

Mais les entreprises existent pour générer des revenus et, en règle générale, plus elles possèdent de données, plus ces données peuvent générer de revenus. Plus il y a de clients potentiels qui fournissent leur e-mail et les coordonnées de leurs comptes de médias sociaux, plus il sera facile de se connecter à eux avec de nouvelles offres. Et plus il sera facile pour d'autres entreprises travaillant dans des industries similaires de se connecter aux clients d'une entreprise également.

L'incitation à vendre votre liste de contacts à un tiers intéressé est claire.

Naturellement, les restrictions légales et les accords d'utilisation peuvent parfois empêcher de telles ventes de jeux de données. Mais tous les cas d'utilisation ne sont pas nécessairement couverts par de telles lois, et toutes les entreprises ne sont pas nécessairement liées par un fort désir de suivre la loi.

Un cas délicieux en est la liste "Ne pas appeler" du Canada, qui remonte à 2004. La loi empêchait les télémarketeurs de contacter toute personne qui s'était ajoutée à la liste nationale. La loi exigeait que tous les télémarketeurs retirent toutes les entrées de la liste de leurs propres listes d'appels.

Le problème était que les spammeurs téléchargeaient joyeusement les listes "Ne pas appeler" et, convaincus qu'elles représentaient des comptes actifs confirmés, appelaient spécifiquement ceux-ci. La seule loi qui a été efficace dans ce cas était la _loi des conséquences imprévues_.

Vos données peuvent également être utiles pour personnaliser les résultats que vous obtenez des requêtes des moteurs de recherche. Bien sûr, vous pourriez parfois apprécier de voir des résultats liés à votre comportement de navigation précédent, mais ne perdez pas de vue le fait que votre comportement est utilisé dans le cadre d'une campagne pour vous vendre des choses.

Ce ne sont pas seulement les moteurs de recherche : les historiques de navigation sur smartphone sont parfois utilisés par les entreprises à proximité pour pousser des publicités personnalisées dans votre direction – parfois même via des affichages numériques automatisés sur des panneaux d'affichage physiques et autres signalétiques.

Peut-être que la plus grande valeur que vos données peuvent offrir est lorsqu'elles sont agrégées avec des données générées par des milliers ou des millions d'autres utilisateurs.

Les scientifiques des données peuvent diffuser et analyser d'énormes ensembles de données dynamiques pour extraire des informations significatives sur des tendances subtiles mais significatives. Dans de nombreux cas, ces données sont nettoyées pour supprimer toute information personnellement identifiable (PII).

Nous pouvons résumer le modèle économique des applications web du 21e siècle avec cette expression populaire – et exacte :

> "Si vous ne payez pas pour le produit, vous êtes le produit."

# Comment protéger vos données

Tout cela semble assez sombre. Après tout, 1984 de George Orwell était censé être un avertissement, pas un guide pratique. Que pouvez-vous faire pour résister ?

### Soyez conscient de votre environnement.

Remarquez-vous encore ces déclarations de conditions d'utilisation que vous "cliquez pour signer" avant qu'ils ne vous laissent utiliser un service ou un outil ? Certaines de ces déclarations sont aussi longues que cet article – et, si je puis me permettre, bien moins amusantes.

Mais le fait est qu'elles contiennent des informations qui peuvent avoir un impact profond sur vous et vos données.

De nombreux accords décrivent les données qu'ils sont susceptibles de collecter et ce qu'ils prévoient de faire avec elles. Ils offrent souvent des assurances qu'ils ne vendront jamais vos données à des tiers – une assurance qu'ils pourraient parfois même honorer à la fois dans la lettre et l'esprit de la loi (bien qu'il y ait eu des cas célèbres d'entreprises qui n'ont fait ni l'un ni l'autre).

Je n'ai jamais rencontré quelqu'un qui ait le temps et l'énergie de lire ces déclarations interminables du début à la fin. Mais si une organisation paie un groupe d'avocats pour écrire quelque chose, vous pouvez parier que c'est une affaire sérieuse.

### Soyez conscient de vos droits.

Au-delà de votre accord spécifique avec un fournisseur de services technologiques, l'utilisation de vos données peut être réglementée par la législation gouvernementale.

Un exemple est le Règlement Général sur la Protection des Données (GDPR) de l'Union Européenne, qui contrôle la manière dont les organisations doivent traiter les données personnelles qu'elles rencontrent dans le cadre de leurs opérations.

Un autre exemple est la loi américaine Health Insurance Portability and Accountability Act (HIPAA), qui réglemente la gestion des informations privées dans les industries de l'assurance maladie et des soins de santé.

### Soyez conscient de vos alternatives.

Envisagez d'adopter des outils axés sur la vie privée plutôt que les services plus commerciaux que vous utilisez actuellement. Par exemple, le moteur de recherche DuckDuckGo.com, dont la page d'accueil est illustrée ci-dessous, ne suit pas votre comportement de recherche et retournera les mêmes résultats pour une requête particulière pour vous que pour n'importe qui d'autre.

Ils sont une entreprise à but lucratif, mais ils gagnent une grande partie de leurs revenus grâce à des liens d'affiliation qui leur paient une commission pour les ventes générées via les liens de recherche – aucun de ces liens n'a d'impact sur votre vie privée.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/duckduck.png)
_La page d'accueil du navigateur DuckDuckGo_

Le navigateur Brave, comme autre exemple, a été montré pour envoyer beaucoup moins de données non documentées sur internet que tout autre navigateur majeur.

Pour être précis, au début de 2020, Douglas Leith de l'École d'Informatique et de Statistiques, Trinity College Dublin, a testé six navigateurs pour leurs risques de révéler des informations d'identification uniques sur leurs ordinateurs hôtes (scss.tcd.ie/Doug.Leith/pubs/browser_privacy.pdf). Il a constaté que Brave offrait clairement la plus grande protection de la vie privée.

Brave bloque également les publicités des pages web par défaut, ce qui soulève une question. Puisque de nombreuses pages web gagnent des revenus exclusivement via les publicités display, Brave s'attend-il à ce que les fournisseurs de contenu offrent leurs services gratuitement ?

Le fournisseur du navigateur a en réalité un modèle économique qui inclut les fournisseurs de contenu : les utilisateurs du navigateur Brave peuvent choisir de voir des publicités simples et extrêmement discrètes de la part d'annonceurs soigneusement sélectionnés en échange de micro-paiements en crypto-monnaie. Les utilisateurs peuvent ensuite choisir de faire des micro-paiements aux fournisseurs de contenu de sites web en utilisant ces fonds comme moyen de payer pour leur contenu via le programme Brave Rewards (illustré ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2022/12/figure2-4.png)
_Capture d'écran du programme de récompenses Brave_

Opter pour des applications open source peut également être une stratégie de confidentialité efficace. OpenStreetMap (openstreetmap.org) est une alternative à Google Maps. Il n'a peut-être pas toutes les clochettes et sifflets et la connectivité intégrée auxquels vous êtes habitué, mais c'est justement cette connectivité qui alimente nos réserves, n'est-ce pas ?

Si vous n'êtes pas à l'aise avec les grands acteurs des systèmes d'exploitation mobiles (Android et iOS), vous pourriez, à la place, acheter un téléphone et installer l'une des nombreuses variations expérimentales de Linux mobile.

Emprunter cette voie sera probablement semé d'embûches. Attendez-vous à rencontrer des défis de configuration et de compatibilité inattendus, et ne vous attendez pas à trouver toutes les applications pratiques que vous avez appris à connaître et à aimer en utilisant les grands magasins d'applications.

Voyez-vous un trou qui a besoin d'être comblé ? Pourquoi ne pas contribuer à votre propre innovation en participant à des projets open source existants ou en ajoutant vos propres solutions à la communauté ?

## Merci d'avoir lu !

J'espère que cet article vous a donné les outils pour prendre soin de votre vie privée numérique.

_Les vidéos YouTube des dix chapitres de ce livre [sont disponibles ici](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Beaucoup plus de bonnes choses technologiques - sous forme de livres, de cours et d'articles - [peuvent être trouvées ici](https://bootstrap-it.com). Et envisagez de suivre mes [cours sur AWS, la sécurité et la technologie des conteneurs ici](https://www.udemy.com/user/david-clinton-12/).