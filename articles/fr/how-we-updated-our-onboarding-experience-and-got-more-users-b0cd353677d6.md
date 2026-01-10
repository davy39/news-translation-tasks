---
title: Comment nous avons mis à jour notre expérience d'onboarding et obtenu plus
  d'utilisateurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T19:05:18.000Z'
originalURL: https://freecodecamp.org/news/how-we-updated-our-onboarding-experience-and-got-more-users-b0cd353677d6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Kp5Z_lcq-cbmwAnI.png
tags:
- name: Design
  slug: design
- name: onboarding
  slug: onboarding
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: Comment nous avons mis à jour notre expérience d'onboarding et obtenu plus
  d'utilisateurs
seo_desc: 'By William Woodhead

  Methods we used to increase conversion by 60%


  Pilcro Artboard — User Onboarding

  As a product designer and developer, I have spent a lot of time thinking about the
  elements of a successful User Onboarding experience. It’s a diffic...'
---

Par William Woodhead

#### Méthodes que nous avons utilisées pour augmenter la conversion de 60%

![Image](https://cdn-media-1.freecodecamp.org/images/RngZsRjwpWrpromZzWL0nr472IPxxVrpidIC)
_Pilcro Artboard  User Onboarding_

En tant que designer produit et développeur, j'ai passé beaucoup de temps à réfléchir aux éléments d'une expérience d'onboarding réussie. C'est un processus difficile qui est crucial pour une bonne conversion, et il est souvent négligé.

Dans cet article, je vais décrire le processus que nous avons suivi (en travaillant sur notre [logiciel de gestion de marque](https://www.pilcro.com)), afin que vous puissiez appliquer les leçons que nous avons apprises pour votre propre flux d'onboarding utilisateur.

Pourquoi m'écouter ? Eh bien, nous avons récemment augmenté notre taux de conversion global de 60 % après avoir lancé notre flux d'onboarding utilisateur dans le cadre de notre [lancement de produit](https://www.pilcro.com/blog/pilcro-is-on-product-hunt) sur Product Hunt. Voici ce que [Jonathan Price](https://www.linkedin.com/in/jvprice) en a dit le jour du lancement :

> _"La page de destination thématique Product Hunt était vraiment exceptionnelle  peut-être le lancement Product Hunt le plus abouti que j'aie vu. Excellent travail."_

### Qu'est-ce que l'onboarding utilisateur ?

Voici une définition de [trychameleon](https://www.trychameleon.com/blog/what-is-user-onboarding) :

> _"L'onboarding utilisateur est le système qui guide activement les utilisateurs à découvrir de nouvelles valeurs dans votre produit."_

Il s'agit donc de communiquer les fonctionnalités précieuses à vos utilisateurs.

Mais qui sont ces utilisateurs ? Sont-ils des utilisateurs pour la première fois ? Sont-ils des utilisateurs (plus ou moins) nouveaux qui reviennent à votre produit ?

Et que signifie "valeur" ? Des fonctionnalités que les utilisateurs pourraient apprécier ? Des comportements d'utilisateurs que vous pourriez valoriser ? Par exemple, des connexions ou des abonnements ?

Il est immédiatement clair que l'onboarding utilisateur n'est pas une tâche UX simple.

Nous avons plusieurs types d'utilisateurs et plusieurs fonctionnalités que nous pensons que les utilisateurs trouveraient précieuses. Comment donner un sens à tout cela ? Comment communiquer la valeur du produit de manière efficace ? Et ensuite, que cherchons-nous réellement à accomplir en montrant des fonctionnalités aux utilisateurs ?

### Première étape  Auditer les parcours utilisateurs

Cela peut sembler évident, mais la première étape consiste à comprendre comment les nouveaux et les utilisateurs existants naviguent dans votre application. Y a-t-il un parcours unique que tout le monde suit, ou existe-t-il plusieurs chemins différents ?

Nous avons réalisé cette étape avec l'aide des étudiants en UX de [General Assembly](https://generalassemb.ly/?ref=pilcro) qui ont utilisé des tests utilisateurs pour comprendre comment les nouveaux utilisateurs expérimentaient notre application pour la première fois. Ce processus nous a également aidés à catégoriser nos utilisateurs en trois types différents :

* Premières 20 secondes
* Première session
* Premier mois

À la fin de ce processus, nous avions une bien meilleure compréhension de la manière dont les utilisateurs naviguent dans notre application. Mais nous ne savions toujours pas quelle valeur nous voulions leur communiquer ou quel était l'objectif final.

### Introduction au Moment Magique

Dans le cadre de notre confusion concernant l'onboarding utilisateur, nous sommes tombés sur [cette vidéo](https://youtu.be/n_yHZ_vKjno). Elle explique comment Facebook a conçu ses parcours utilisateurs pour amener les utilisateurs à un "Moment Magique".

Le Moment Magique est celui où un utilisateur comprend soudainement quelle est la valeur centrale de votre produit. C'est le moment où un utilisateur "comprend". Pour Facebook, c'était lorsqu'un utilisateur voyait une photo d'un de ses amis.

Pour nous, chez Pilcro, nous avons réalisé que notre Moment Magique est lorsque l'utilisateur copie un actif de marque pour la première fois. C'est à ce moment-là qu'ils comprennent vraiment pourquoi ils devraient utiliser Pilcro.

Avec le Moment Magique en tête, nous avons conçu ce tableau pour aider à ordonner nos pensées.

![Image](https://cdn-media-1.freecodecamp.org/images/KrklNMfoiB4RKCtZC0F4tCUwlAN3ikg04LL8)

Ensuite, nous avons essayé de faire correspondre ces mêmes objectifs à des stratégies possibles pour les atteindre.

![Image](https://cdn-media-1.freecodecamp.org/images/N7E0JpUjOAxo1rx5T1PQ7oN7gVvq8Z-6ax0U)

À ce stade, nous avions quelques stratégies pour atteindre les objectifs. Il était temps de voir quels composants visuels d'onboarding étaient disponibles pour nous  quels outils et astuces pouvions-nous tirer de l'onboarding utilisateur pour donner vie à tout cela.

### Options d'onboarding utilisateur

Après toutes les analyses, l'onboarding utilisateur se résume toujours à écrire quelques composants d'interface utilisateur qui communiquent la valeur aux utilisateurs. Quels sont donc ces composants d'interface utilisateur ? Quelles options sont disponibles pour les développeurs d'applications et les designers UX ?

Il existe bien sûr une infinité d'options pour les composants d'onboarding utilisateur, mais voici une liste concise de nos préférés avec des exemples d'images d'onboarding utilisateur provenant d'autres applications.

#### Modales

Prenez le contrôle de tout l'écran, forçant l'utilisateur à s'arrêter pour lui montrer quelque chose d'utile.

![Image](https://cdn-media-1.freecodecamp.org/images/dtKqT-MpF0wNnfH7ZrXGRuopT-NS8bg97UTm)
_Modale de bienvenue de Google Photos_

#### Popups contextuels

Informations lorsque et où l'utilisateur en a besoin. Les infobulles sont l'exemple le plus courant :

![Image](https://cdn-media-1.freecodecamp.org/images/2KcBvN8IseHl96Y1gLUbwa3TRhSsVgZ80lWD)
_Infobulle Asana_

#### Espace vide

Utilisez les listes et les grilles vides dans l'interface utilisateur de l'application pour afficher des conseils utiles et des appels à l'action.

![Image](https://cdn-media-1.freecodecamp.org/images/pRb5g2c-cLSD7sCeRLbik4KJl9BaBruLFMNV)
_Application Bear  espace vide intelligent_

#### Indicateur de progression

Affichez un indicateur de la performance de l'utilisateur. Cela peut durer toute la durée de vie de l'utilisateur sur votre produit et peut être gamifié.

![Image](https://cdn-media-1.freecodecamp.org/images/yjmoV2tY0eAJ83lluysEoJkz9NGSbrbRIO2P)
_Indicateur de progression de la configuration Sentry_

Avec ces options en tête, nous avons tracé ce tableau pour déterminer quelles options d'onboarding utilisateur convenaient le mieux à quels types d'utilisateurs et pourquoi. Les carrés verts sont les meilleures correspondances tandis que les carrés rouges sont de mauvaises correspondances.

![Image](https://cdn-media-1.freecodecamp.org/images/e6OqaHHtsOX8W0RjqxDY8xLo8TvHoKT1oiWP)

À ce stade, nous avions toutes les pièces du puzzle prêtes.

1. Nous avions identifié les différents types d'utilisateurs.
2. Nous avions identifié les stratégies à utiliser pour nos types d'utilisateurs.
3. Nous avions identifié les composants d'interface utilisateur pour réaliser ces stratégies.

Il était temps de tout assembler.

### Que avons-nous réellement fait ?

#### Modale des avantages utilisateur

* Uniquement lors de la première visite
* Communiquer certains avantages principaux de l'application pour l'utilisateur.
* **Objectif**  inciter les utilisateurs à rester.

![Image](https://cdn-media-1.freecodecamp.org/images/98SKqUvFhyQTvi9qdra5aJRJGBLPuTiLhYfm)
_Diaporama des avantages utilisateur_

#### Popups contextuels

* Familiariser rapidement les utilisateurs avec l'interface
* Leur montrer les fonctionnalités et boutons les plus importants.
* Thème Product Hunt pour donner aux visiteurs de Product Hunt une certaine cohérence visuelle.
* **Objectif**  amener les utilisateurs au Moment Magique

![Image](https://cdn-media-1.freecodecamp.org/images/Jk9DUH218hBG6YU6A-FKEP36BUZEWtHZjZmP)
_Popups contextuels  le swoosh_

#### Utilisation intelligente de l'espace vide

* Afficher des appels à l'action là où il n'y a pas de contenu
* **Objectif**  ne jamais laisser un utilisateur en dehors d'un flux

![Image](https://cdn-media-1.freecodecamp.org/images/vRQSiXUVaaXOZAGN6swVvqqqOazIGPd4dw53)
_Appels à l'action dans l'espace vide de Pilcro_

#### Indicateur de progression

* Montrer aux utilisateurs une barre de pourcentage indiquant à quel point ils sont des "power-users".
* **Objectif**  inciter les utilisateurs à se comporter comme nous le souhaitons.

![Image](https://cdn-media-1.freecodecamp.org/images/1DY8iN-0EfG-jBm2t0AUwl2zEN4Wl1mjAMmT)
_Indicateur de progression en %_

### Et les chiffres ne mentent pas

Comment savions-nous que la conception de l'onboarding utilisateur fonctionnait ? Voici les statistiques.

Nous avons plus que doublé nos conversions vers le produit depuis le site web dans la semaine suivant le déploiement du nouvel onboarding utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/3zrVR3uzFrpt2DdBtit4xpsSiWCQJ7IjJzLz)
_Conversions vers le produit_

Nous avons augmenté notre taux de conversion global de 60 %.

![Image](https://cdn-media-1.freecodecamp.org/images/Z6cMZDXS25TpmnU4LQgYGijKT2C4D8KbL3DY)

Admettons-le, le lancement a aidé ces statistiques car il y avait plus de buzz autour de notre produit. Mais le nouvel onboarding utilisateur a sans aucun doute joué un rôle crucial dans le succès du lancement.

### Réflexion  Pourquoi l'onboarding utilisateur est-il si difficile ?

* Les propriétaires de produits sont trop proches du produit. Comment un propriétaire de produit peut-il savoir ce que cela fait d'expérimenter son produit pour la première fois ?
* Différents utilisateurs trouvent de la valeur dans différentes parties du produit. Les guider pour trouver de la valeur n'est donc pas un parcours linéaire que tous les utilisateurs partagent. Différents utilisateurs peuvent avoir différents Moments Magiques.
* Différents utilisateurs se comportent différemment et naviguent différemment dans votre produit. Certains utilisateurs aiment être guidés lors de l'onboarding dans un nouveau produit, d'autres préfèrent plonger directement et explorer. Comment concevoir une expérience UX qui répond aux besoins d'onboarding de tous les différents utilisateurs ?
* Différents utilisateurs ont des connaissances différentes de votre produit. Comment savoir donc combien d'informations donner à quelqu'un ?
* La technologie derrière la conception d'une bonne expérience d'onboarding utilisateur est souvent très complexe car elle nécessite l'ajout d'une toute nouvelle couche visuelle à votre application.

L'onboarding utilisateur est un défi complexe car vous devez gérer une matrice de différents utilisateurs, fonctionnalités, objectifs et comportements. Cependant, si vous l'abordez de la bonne manière, vous pouvez faire briller votre application pour vos nouveaux utilisateurs. Bonne chance !

### Expérimentez-le par vous-même

Découvrez notre onboarding utilisateur par vous-même à [ce lien](https://artboard.pilcro.com/). Faites-nous savoir ce que vous en pensez !

_Pilcro offre un logiciel gratuit de gestion de marque pour G-Suite._