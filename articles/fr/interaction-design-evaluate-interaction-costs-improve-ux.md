---
title: Conception d'Interaction – Comment Évaluer les Coûts d'Interaction et Améliorer
  l'Expérience Utilisateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-08T21:16:00.000Z'
originalURL: https://freecodecamp.org/news/interaction-design-evaluate-interaction-costs-improve-ux
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/1_WzkvMd3sZRb6BCwKEsoHjA.png
tags:
- name: Design
  slug: design
- name: user experience
  slug: user-experience
- name: ux design
  slug: ux-design
seo_title: Conception d'Interaction – Comment Évaluer les Coûts d'Interaction et Améliorer
  l'Expérience Utilisateur
seo_desc: 'By Richard Yang

  There are three core skills that every modern product designer must master: product
  thinking, visual design, and interaction design.


  The “table-stakes” for all modern product designers.

  In general, you should be good at all three, bu...'
---

Par Richard Yang

Il existe trois compétences principales que tout designer de produits moderne doit maîtriser : la réflexion sur le produit, le design visuel et le design d'interaction.

![Diagramme montrant les trois compétences principales en design de produits : la réflexion sur le produit, le design visuel (UI) et le design d'interaction (IxD).](https://www.freecodecamp.org/news/content/images/2021/02/image-146.png)
_Les "enjeux de base" pour tous les designers de produits modernes._

En général, vous devriez être bon dans les trois domaines, mais vous devriez exceller dans deux d'entre eux. La plupart des designers peuvent s'autoformer en design visuel et en réflexion sur le produit grâce à des ressources en ligne, à la pratique et à la livraison de produits réels.

En tant que responsable de la conception de produits dans une entreprise FAANG, ayant mentoré des centaines de designers aspirants, je constate que le design d'interaction tend à être la compétence principale la plus difficile à auto-apprendre pour les designers.

Dans cet article, je fournis une base et un cadre pour apprendre et améliorer vos compétences en design d'interaction.

![Diagramme montrant le chevauchement et la différence entre UX et IxD. IxD est un sous-domaine de l'UX.](https://www.freecodecamp.org/news/content/images/2021/02/image-148.png)
_La différence entre UX (expérience utilisateur) et IxD (design d'interaction)._

## Qu'est-ce que le Coût d'Interaction ?

Le concept fondamental derrière le design d'interaction est le "coût d'interaction", souvent utilisé pour mesurer l'utilisabilité d'un produit. Nielsen Norman définit les "coûts d'interaction" comme la [somme des efforts mentaux et physiques](https://www.nngroup.com/articles/interaction-cost-definition/) que les utilisateurs doivent fournir pour atteindre leurs objectifs.

En général, nous voulons garder les coûts d'interaction aussi bas que possible. Cependant, cela est difficile, car plus votre produit couvre de cas d'utilisation, plus cela devient difficile.

Prendre en charge plus de cas d'utilisation et de fonctionnalités ajoute de la complexité à l'architecture de l'information (IA) et à la navigation de votre produit. Un cas d'utilisation est une séquence d'étapes, commençant par un objectif de l'utilisateur et se terminant par le résultat lorsque cet objectif est atteint.

Une IA plus complexe augmentera intrinsèquement le nombre de clics nécessaires pour accomplir un objectif de l'utilisateur. Par exemple, une application d'horloge iOS a les objectifs de cas d'utilisation d'alarme suivants : activer l'alarme, créer une nouvelle alarme et modifier l'alarme.

![Un diagramme d'architecture de l'information (IA).](https://www.freecodecamp.org/news/content/images/2021/02/image-149.png)
_Plus l'IA est complexe, plus l'utilisateur doit cliquer pour accéder à l'écran souhaité. [Crédits : Topta](https://dribbble.com/shots/4406909-The-Comprehensive-Guide-to-Information-Architecture" rel="noopener nofollow)l_

La règle générale consiste à réduire les coûts d'interaction pour les cas d'utilisation principaux de votre utilisateur cible. Chaque fois qu'un produit accommode trop de cas d'utilisation (par exemple, des produits d'entreprise avec un million de menus déroulants et de fonctionnalités), il devient plus difficile à utiliser.

Pour éviter cette surcomplication, choisissez un utilisateur et un cas d'utilisation spécifiques sur lesquels vous concentrer lors de la création d'un tout nouveau produit.

### Coûts d'Interaction Physiques et Mentaux

De nombreux designers juniors ont l'idée fausse que le coût d'interaction est égal au nombre de clics nécessaires pour qu'un utilisateur accomplisse une tâche.

![Un diagramme montrant les PIC et MIC.](https://www.freecodecamp.org/news/content/images/2021/02/image-150.png)

Cependant, cela va bien plus loin. Le coût d'interaction peut être classé en coûts d'interaction mentaux (MIC) et coûts d'interaction physiques (PIC), que je vais expliquer ci-dessous.

## Comment Évaluer le Coût d'Interaction – Trouver les Flux Utilisateurs Critiques en Premier

Une bonne pratique consiste à identifier les cas d'utilisation principaux (c'est-à-dire les routes rouges) et à réduire leurs coûts d'interaction au détriment des cas d'utilisation secondaires et tertiaires si nécessaire.

Vous pouvez utiliser une [Analyse des Routes Rouges (RRA)](https://medium.muz.li/red-routes-critical-design-paths-that-make-or-break-your-app-a642ebe0940a) pour évaluer quels flux d'interaction de cas d'utilisation sont les plus importants pour vos utilisateurs principaux.

Les routes rouges tendent à être critiques, à englober des tâches de bout en bout avec plusieurs étapes, à être souvent utilisées, à être construites pour une utilisation à haut volume, à fournir le plus de valeur, à avoir des critères de succès clairs et à être liées aux métriques du produit.

![Un exemple de RRA.](https://www.freecodecamp.org/news/content/images/2021/02/image-151.png)
_Vous pouvez créer une RRA à partir d'entretiens avec les utilisateurs ou avec des données si le produit est en ligne._

Par exemple, dans l'application Uber, la route rouge du passager serait de demander une course, tandis que leur route normale serait d'ajouter une méthode de paiement.

## Comment la Loi de Tesler Aide à Réduire les Coûts d'Interaction

Selon la [Loi de Tesler](https://lawsofux.com/laws/teslers-law/) de Conservation de la Complexité, tous les systèmes ont une complexité inhérente qui ne peut être supprimée ou cachée.

Un bon design garantit que la charge de complexité repose autant que possible sur le système plutôt que sur l'utilisateur.

![Un diagramme illustrant la loi de Tesler, où la charge de complexité est répartie entre l'utilisateur et le produit.](https://www.freecodecamp.org/news/content/images/2021/02/image-152.png)

Vous devriez commencer par réduire les coûts d'interaction au sein des cas d'utilisation principaux et déplacer la charge de complexité vers les cas d'utilisation les moins importants.

Tesler a soutenu qu'un designer et un ingénieur devraient passer une semaine supplémentaire à réduire la complexité d'une application plutôt que de faire perdre une minute supplémentaire à des millions d'utilisateurs.

Faites attention à ne pas simplifier les interfaces au point de les rendre abstraites. Un piège courant consiste à réduire le PIC au détriment du MIC (je vous regarde, Apple).

Lorsque le système a géré autant que possible la complexité inhérente, vous devriez déplacer le reste de la complexité des cas d'utilisation principaux vers les cas d'utilisation secondaires et tertiaires.

La plupart des produits numériques ont des paramètres compliqués pour cette raison. Dans la plupart des cas, les paramètres sont généralement un cas d'utilisation tertiaire et sont très rarement utilisés.

Imaginez si vous voyiez toujours l'écran des paramètres au lieu de l'écran d'accueil et que vous deviez cliquer plusieurs fois pour accéder à l'écran dont vous avez besoin. Vous seriez probablement frustré par les coûts d'interaction déraisonnables.

## Coûts d'Interaction Mentaux (MIC)

Les [coûts d'interaction mentaux (MIC)](https://www.researchgate.net/publication/23456170_A_Framework_of_Interaction_Costs_in_Information_Visualization) sont souvent négligés par les nouveaux designers qui ne prêtent attention qu'aux coûts d'interaction physiques (PIC).

Les MIC courants que vous avez peut-être remarqués dans les produits à faible utilisabilité incluent une navigation complexe, des instructions denses, des modèles mentaux et des schémas d'interaction non conventionnels, et ainsi de suite.

### Attention et Mémoire

Les deux composantes les plus importantes des MIC sont l'attention et la mémoire.

Lorsque une tâche nécessite une attention ou une mémoire excessive pour être accomplie, elle aura un MIC proportionnellement élevé, diminuant ainsi l'utilisabilité.

Certains éléments courants qui augmentent les coûts d'attention ou détournent l'attention incluent les bannières pop-up, les modèles, les visuels accrocheurs et les mouvements non liés à la tâche actuelle de l'utilisateur.

Les utilisateurs sont facilement distraits. Assurez-vous de ne pas détourner leur attention ailleurs lorsqu'ils essaient d'accomplir une tâche.

### Évaluer l'Attention

Si vous souhaitez évaluer combien d'attention MIC votre interface a, envisagez de faire une [étude de suivi du regard (ETS)](https://uxplanet.org/uxers-quick-guide-to-eye-tracking-edf70bffd03d). Vous pouvez utiliser une ETS pour déduire non seulement où les utilisateurs regardent, mais aussi ce à quoi ils pensent.

![Un exemple d'ETS.](https://www.freecodecamp.org/news/content/images/2021/02/image-153.png)
_Un exemple d'ETS._

L'ETS examine deux mouvements oculaires pertinents en particulier : la "fixation" et le "saccade".

La fixation se produit lorsque les pupilles d'un utilisateur s'attardent sur un élément d'interface suffisamment longtemps pour le traiter. Un saccade se produit lorsque l'œil est en mouvement, passant rapidement entre diverses zones de votre interface.

Si votre ETS révèle de nombreux mouvements saccadiques non pertinents pour la tâche, cela est probablement dû à une interface distractive. Les résultats de votre ETS peuvent vous aider à comprendre si les utilisateurs manquent des éléments critiques de l'interface, ce qui est distractif et ce qui est inutile.

### Mémoire de travail

Il existe une classification extensive pour tous les différents types de mémoire.

Pour nos besoins en tant que designers, la mémoire de travail (partie de la mémoire à court terme) est la plus pertinente. Le type de mémoire le plus court est connu sous le nom de mémoire de travail, qui dure généralement seulement quelques secondes pendant une tâche.

En d'autres termes, notre mémoire de travail est responsable des informations que nous pouvons garder en tête pendant que nous interagissons avec d'autres processus cognitifs.

La [Loi de Miller](https://lawsofux.com/laws/millers-law/) stipule que la personne moyenne ne peut garder que 5 à 11 éléments dans sa mémoire de travail à la fois. La mémoire de travail requise pour accomplir une tâche dans votre produit est proportionnelle à la charge MIC que vous imposez à vos utilisateurs.

![Une illustration de la Loi de Miller.](https://www.freecodecamp.org/news/content/images/2021/02/image-154.png)

Inversement, à aucun moment votre tâche ne devrait nécessiter que l'utilisateur garde plus de sept éléments dans sa mémoire de travail à un moment donné.

Dans de rares scénarios où vous exigez que l'utilisateur garde plus de 11 éléments dans sa mémoire, utilisez le "chunking" pour réduire sa charge mentale. Le chunking consiste à décomposer des morceaux individuels d'un ensemble d'informations, puis à les regrouper en un tout significatif.

Par exemple, nous mémorisons les numéros de téléphone sous la forme XXX-XXXX plutôt que XXXXXXX. Il est plus facile de se souvenir du numéro en deux parties plutôt qu'en une série de sept unités individuelles.

Un autre facteur à considérer lié à l'attention et à la mémoire est la ["Loi de Hick"](https://lawsofux.com/laws/hicks-law/). La loi stipule que "le temps nécessaire pour prendre une décision augmente avec le nombre et la complexité des choix".

![Un graphique de la Loi de Hick avec le temps x le nombre d'options.](https://www.freecodecamp.org/news/content/images/2021/02/image-155.png)
_Plus il y a de choix, plus il faut de temps à l'utilisateur pour prendre une décision._

Évitez de submerger les utilisateurs avec des choix excessifs, mettez en avant la meilleure option pour eux chaque fois que possible. Divisez les tâches complexes en étapes plus petites, c'est-à-dire en utilisant une divulgation progressive lorsque cela est approprié.

## Coûts d'Interaction Physiques (PIC)

Je ne vais pas entrer dans trop de détails sur les PIC car la plupart des designers les comprennent bien.

Les facteurs courants de PIC incluent la distance de portée et la largeur de la cible ([Loi de Fitts](https://lawsofux.com/laws/fittss-law/)), le nombre d'entrées et d'actions de l'utilisateur nécessaires pour accomplir une tâche, et ainsi de suite.

La [Loi de Fitts](https://lawsofux.com/laws/fittss-law/) stipule que le temps nécessaire pour atteindre une cible (c'est-à-dire cliquer sur un bouton) est une fonction de la distance entre votre dispositif d'entrée et la largeur de la zone de clic de la cible.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-156.png)
_Un diagramme pour la Loi de Fitts._

Par exemple, cliquer sur un bouton sur le bureau prendrait beaucoup plus de temps si votre curseur de souris était loin et que le bouton était minuscule.

Une excellente méthode pour évaluer les PIC est l'["analyse des tâches"](https://www.nngroup.com/articles/task-analysis/) et l'examen des [métriques d'utilisabilité](https://usabilitygeek.com/usability-metrics-a-guide-to-quantify-system-usability/) telles que le "temps de tâche (TT)".

La base de l'AT consiste à examiner le nombre de tâches nécessaires pour atteindre l'objectif de l'utilisateur, la fréquence de ces tâches, les exigences physiques et le temps de tâche.

L'AT et les métriques d'utilisabilité sont des sujets avancés qui méritent une note entièrement séparée, je les garderai donc pour la prochaine fois.

## Pièges Courants à Éviter

Selon le Nielsen Norman Group, certains des aspects les plus courants d'un produit qui entraînent une augmentation des coûts d'interaction incluent les suivants :

* Lecture et défilement excessifs
* Recherche d'informations pertinentes pour l'utilisateur
* Compréhension des informations présentées à l'utilisateur
* Entrées physiques de l'utilisateur
* Temps de chargement des pages et temps d'attente
* Changements d'attention
* Charge de mémoire

### Coûts d'Interaction Situationnels

Les pièges mentionnés ci-dessus peuvent être plus ou moins critiques en fonction de l'utilisateur. Par exemple, les utilisateurs dyslexiques trouvent la lecture plus difficile que l'utilisateur moyen (astuce : utilisez une police adaptée aux dyslexiques comme ["Dyslexie"](https://www.dyslexiefont.com/en/typeface/)).

![Une animation 3D de la police Dyslexie.](https://www.freecodecamp.org/news/content/images/2021/02/image-157.png)
_[Source](https://www.dyslexiefont.com/" rel="noopener nofollow)_

Les utilisateurs ayant des troubles moteurs peuvent trouver le clic beaucoup plus difficile que la lecture. Même le dispositif de l'utilisateur peut jouer un rôle important. Par exemple, le chargement d'une page sur un appareil mobile peut prendre une éternité si la couverture cellulaire est lente.

![Un indicateur de chargement standard.](https://www.freecodecamp.org/news/content/images/2021/02/image-158.png)

### Chemins d'Interaction et Motivation

Dans certaines situations, il existe plusieurs chemins possibles qu'un utilisateur peut emprunter pour accomplir son objectif. Les utilisateurs décident du chemin à prendre en fonction du concept d'"utilité attendue", définie comme utilité attendue = bénéfices attendus - coûts d'interaction attendus.

En d'autres termes, les utilisateurs pèsent les bénéfices et les coûts de chaque action et choisissent le chemin qui offre le meilleur équilibre entre bénéfices et coûts.

Les utilisateurs seront attirés par le chemin qui a le coût d'interaction estimé le plus bas. Même s'il existe un chemin à moindre coût, si ce chemin est peu intuitif ou peu familier, ils finiront par choisir le chemin qui leur est le plus familier en raison d'un MIC plus bas.

Les utilisateurs ayant une forte motivation (par exemple, grâce à vos efforts de marketing ou de branding) sont plus susceptibles de supporter des coûts d'interaction élevés pour atteindre leur objectif. Par exemple, si le site web d'Apple avait des coûts d'interaction élevés, les utilisateurs pourraient encore être suffisamment motivés pour accomplir leur tâche.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-159.png)
_Apple est la marque la plus précieuse au monde pour une raison._

Cependant, si les utilisateurs voulaient acheter un produit générique et que le processus de paiement avait un coût d'interaction élevé, ils l'achèteraient chez un concurrent à la place.

Pour plus de détails, consultez l'exemple du Nielsen Norman Group sur [comment évaluer le coût d'interaction d'un cas d'utilisation](https://www.nngroup.com/articles/interaction-cost-definition/), "découvrir d'où vient le mot 'cérémonie'".

## Conclusion

Comprendre le coût d'interaction est une compétence vitale pour tout designer de produits moderne. Je vous encourage à aller au-delà des considérations superficielles de design d'interaction et à approfondir les nombreux facteurs PIC et MIC.

Bien sûr, nous devrions nous efforcer de réduire autant que possible les coûts d'interaction. Mais lorsque les choses se compliquent, nous devrions faire des compromis pour garantir que les cas d'utilisation principaux aient le moins de friction.

Une excellente première étape consiste à créer un modèle mental de lois, de cadres et de tests pour évaluer les coûts d'interaction de votre design.

Si vous avez aimé cet article, [**rejoignez ma newsletter gratuite**](https://theambitiousdesigner.substack.com/) "The Ambitious Designer" pour plus d'informations sur la carrière et le design.

Je dirige également un [groupe de mentorat privé](https://www.facebook.com/groups/richarduxmentorship) sur Facebook et un compte [Instagram](https://www.instagram.com/richard.ux/) sur le design.