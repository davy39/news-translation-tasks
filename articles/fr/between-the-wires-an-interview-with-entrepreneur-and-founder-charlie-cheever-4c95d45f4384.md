---
title: 'Entre les fils : Une interview avec Charlie Cheever, cofondateur de Quora'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-31T03:53:58.000Z'
originalURL: https://freecodecamp.org/news/between-the-wires-an-interview-with-entrepreneur-and-founder-charlie-cheever-4c95d45f4384
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PA7ePsyQTz1f64RL9Xm47w.png
tags:
- name: Design
  slug: design
- name: Entrepreneurship
  slug: entrepreneurship
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: startup
  slug: startup
seo_title: 'Entre les fils : Une interview avec Charlie Cheever, cofondateur de Quora'
seo_desc: 'By Vivian Cromwell

  I interviewed Charlie Cheever, who is the founder of expo.io. Expo’s mission is
  to let web developers build truly native apps that work across both iOS and Android
  by writing them once in just JavaScript. It’s open source, free and...'
---

Par Vivian Cromwell

_J'ai interviewé Charlie Cheever, qui est le fondateur de [expo.io](https://expo.io/). La mission d'Expo est de permettre aux développeurs web de créer des applications véritablement natives qui fonctionnent à la fois sur iOS et Android en les écrivant une seule fois en JavaScript. C'est [open source](https://blog.expo.io/open-sourcing-the-exponent-client-9b37634c13d7), [gratuit](https://blog.expo.io/exponent-is-free-as-in-and-as-in-1d6d948a60dc) et utilise React Native._

_Auparavant, Charlie a cofondé [Quora](https://www.quora.com/), et a travaillé chez Facebook sur l'équipe plateforme._

#### **Parlez-nous un peu de votre enfance et de l'endroit où vous avez grandi.**

J'ai grandi à Pittsburgh, en Pennsylvanie. J'ai toujours aimé les jeux vidéo. Un jour, mon père m'a emmené à la bibliothèque lorsque j'étais en 3ème année, j'ai pris un livre intitulé _Comment créer vos propres jeux vidéo_. La première page disait qu'il fallait savoir programmer en BASIC, alors je suis retourné et j'ai pris un autre livre sur la programmation en BASIC. Je suis allé à l'école et j'ai tapé les programmes du livre sur Apple II, lentement j'ai commencé à leur apporter de petites modifications.

Lorsque j'étais au lycée, j'ai participé à ce programme d'été à Carnegie Mellon appelé [Andrew's Leap](http://www.cs.cmu.edu/~./leap/). C'est un programme d'été gratuit qui vous enseigne la théorie de la complexité de base et un peu de programmation. C'était vraiment amusant. J'aimais vraiment créer des choses avec des ordinateurs ou des calculatrices, et les partager avec les gens. C'était assez facile pour moi de savoir ce que je voulais faire de ma vie.

Finalement, je suis allé à Harvard et j'ai étudié l'informatique. Ensuite, je suis allé travailler chez Amazon, un jour j'ai reçu un email de recrutement de Facebook parce que j'avais été assistant d'enseignement pour un cours que les fondateurs avaient suivi. J'ai rencontré deux amis de l'école, David Fetterman et [Andrew Bosworth](https://twitter.com/boztank?lang=en), ils m'ont dit qu'ils quittaient Microsoft pour aller travailler chez Facebook. J'ai pensé que si ils le faisaient, peut-être que c'était une bonne idée. Alors, j'ai envoyé un email à leur recruteur, j'ai obtenu le poste et j'ai commencé à travailler en 2006 en tant qu'ingénieur logiciel. À l'époque, Facebook ne comptait qu'environ 10 à 12 ingénieurs. J'ai lancé la plateforme de développement Facebook, qui était une plateforme de jeu assez réussie à bien des égards.

J'ai fini par quitter Facebook pour commencer à travailler chez [Quora](https://www.quora.com/). Je voulais vraiment créer une entreprise. Même si Facebook était super amusant et un excellent endroit pour travailler, j'avais l'impression que le moment était venu pour moi de commencer quelque chose par moi-même.

Ensuite, j'ai lancé [Expo](https://expo.io/) il y a environ deux ans.

#### **Qu'est-ce qu'Expo ?**

![Image](https://cdn-media-1.freecodecamp.org/images/0*HPWSbNED3NuSi8QR.jpg)
_Logo d'Expo_

Expo est une plateforme [gratuite](https://blog.expo.io/exponent-is-free-as-in-and-as-in-1d6d948a60dc) [open source](https://blog.expo.io/open-sourcing-the-exponent-client-9b37634c13d7) qui permet aux développeurs web et mobiles de créer et d'itérer rapidement sur des applications natives de haute qualité qui fonctionnent à la fois sur iOS et Android. Le cœur d'Expo est construit autour de [React Native](https://facebook.github.io/react-native/), une technologie inventée chez Facebook et utilisée dans des parties de l'application principale Facebook, Instagram, et bien d'autres. React Native est également utilisé par d'autres grandes entreprises comme Airbnb, Walmart et Tesla.

Avec Expo, vous pouvez écrire du JavaScript pour des composants et des API disponibles sur iOS et Android avec des performances natives. [Expo SDK](https://docs.expo.io/versions/v17.0.0/sdk/index.html#expo-sdk) inclut le runtime, les API React Native et des composants supplémentaires tels que l'audio, la vidéo, l'authentification, les notifications et plus encore. Cela signifie que vous pouvez passer plus de temps à écrire uniquement du JavaScript grâce à un partage de code accru entre iOS et Android.

[XDE](https://expo.io/tools) (Expo Development Environment) gère les versions de React Native pour vous. Vous pouvez rester sur une ancienne version si vous le souhaitez, ou passer à une nouvelle sans vous soucier des changements cassants ou de la reconstruction de votre binaire d'application.

Vous pouvez partager une application que vous construisez avec une simple URL, qui peut être ouverte depuis l'application cliente Expo. Lorsque vous êtes prêt à déployer sur l'app store, compilez simplement votre application en binaires et déployez. Vous pouvez également mettre à jour votre application en quelques secondes "over the air" (oui, cela est autorisé par Apple !)

Expo fournit également un outil basé sur le navigateur appelé [Snack](http://snack.getexpo.io/), qui est similaire à JSFiddle mais pour les applications React Native. Vous pouvez aller sur [snack.expo.io](https://snack.expo.io/), et commencer à prototyper. Vous pouvez le prévisualiser dans votre navigateur ou l'ouvrir sur votre téléphone. Lorsque vous êtes prêt, partagez-le avec vos amis et collègues avec une simple URL.

Tout cela est possible grâce au client Expo car l'application construite avec Expo utilise le même runtime natif. La plupart du temps, vous n'aurez pas besoin d'installer Xcode ou Android Studio sur votre machine pour utiliser Expo. Mais, lorsque vous devez l'étendre avec vos propres bibliothèques natives, vous pouvez toujours [vous détacher vers ExpoKit](https://docs.expo.io/versions/v17.0.0/guides/detach.html) et ouvrir votre projet dans l'un ou l'autre IDE.

![Image](https://cdn-media-1.freecodecamp.org/images/0*q76U5WvgSo6-JQip.png)
_Cycle de vie d'un projet Expo._

Nous sommes passionnés par la simplification et l'accessibilité du développement mobile pour tous. Vous pouvez en savoir plus sur [expo.io](https://expo.io/).

#### **Qu'est-ce qui vous a motivé à créer Expo ?**

Notre mission, à un niveau élevé, est de réduire la distance entre la vision dans la tête de quelqu'un et son produit finalisé.

Lorsque je travaillais chez Quora sur des applications mobiles, il fallait neuf à dix mois pour compléter une application même lorsque nous avions d'excellents développeurs et designers qui travaillaient dessus. Nous devions utiliser webview pour tout rendre multiplateforme, mais elles semblaient toujours un peu décalées. Vous ne pouvez pas tout à fait obtenir la performance optimale, et vous ne pouvez pas tout à fait faire les animations sympas que les applications natives peuvent faire. Cela semblait fondamentalement rétrograde après avoir fait du développement web pendant presque toute ma vie. Quelqu'un devait régler cela. Alors, j'ai pris un peu de temps et j'ai commencé à travailler avec [James Ide](https://twitter.com/JI) pour explorer des moyens d'améliorer cela.

Nous avons commencé avec HTML5 et les technologies web, mais c'était intrinsèquement limité — nous ne pensions pas que c'était assez bon. Mais nous croyions profondément au paradigme du web, qui était un grand pas en avant en termes de productivité. Nous avons construit ce système entier appelé « Ion », qui était un nom stupide car il y avait déjà le [framework Ionic](https://ionicframework.com/).

Mais nous n'avons pas lancé Ion, nous l'avons juste utilisé pour créer quelques applications. Ensuite, React Native est sorti et c'était presque exactement la même chose sauf plus avancé et avec une équipe de 20 personnes derrière au lieu de deux. Nous avons essentiellement décidé d'arrêter de travailler sur Ion et avons commencé à travailler sur tout le reste que nous voulions construire sur React Native.

#### **Souvent, l'un des moments les plus gratifiants pour un fondateur de startup est lorsque votre produit est utilisé de manière inattendue ou innovante. Est-ce que cela arrive avec Expo ?**

Si vous allez dans l'application cliente Expo, il y a un nouvel onglet de projet et il vous montre les dix derniers éléments sur lesquels quelqu'un a appuyé sur le bouton « publier ». C'est vraiment cool, maintenant qu'il y a assez de gens qui l'utilisent, vous verrez généralement au moins 1-2 projets intéressants. C'est excitant de trouver des choses que je ne savais pas que les gens construisaient avec Expo, comme un magasin d'électronique en Thaïlande.

#### **Décrivez-nous une journée dans la vie de la construction d'expo.io en tant que fondateur.**

Si vous me comptez, nous sommes dix personnes maintenant. La plupart d'entre eux sont dans la région de la Baie sauf [Brent](https://twitter.com/notbrent) à Vancouver et [Ben](https://twitter.com/terribleben) à Seattle. Ils viennent nous rendre visite toutes les quelques semaines. Ils aiment où ils sont, et nous les aimons, alors nous faisons en sorte que cela fonctionne.

Slack est le centre de gravité pour notre équipe car nous sommes distribués. Nous travaillons également un peu plus étroitement avec des personnes qui sont développeurs sur notre plateforme, certains d'entre eux sont des contractuels sur des projets spécifiques. Par exemple, [Satyajit](https://twitter.com/satya164) qui vit à Bangalore, nous a aidés sur Sketch. Cela signifie que nous avons beaucoup de flexibilité. Tout le monde travaille à des heures différentes et prend beaucoup de décisions locales sans avoir à consulter un chef de produit.

#### **Pourquoi est-il difficile de gagner de l'argent avec les produits pour développeurs ? Comment Expo aborde-t-il cela ?**

Il y a plusieurs raisons pour lesquelles il est difficile de gagner de l'argent avec les produits pour développeurs. L'une d'elles est qu'il y a beaucoup de personnes motivées à améliorer les processus ou les outils de développement. C'est similaire au contenu, qui est également difficile à monétiser, car beaucoup de gens sont prêts à l'écrire pour d'autres raisons comme le branding ou la réputation.

Les outils de développement tombent souvent dans cette catégorie. Il y a beaucoup de gens qui aiment les créer ou les créer de manière open source, peut-être que certains d'entre eux veulent créer des outils open source pour rendre une plateforme plus populaire ou pour des raisons de recrutement.

Ce qui a du sens pour nous, c'est de ne pas gagner d'argent avec la plateforme elle-même. Il est vraiment important que les outils soient open source car les types de développeurs que nous voulons attirer, et les types d'outils que nous voulons utiliser, sont open source. Vous pouvez comprendre ce qui se passe dans ces outils et vous pouvez envoyer des correctifs s'il y a des problèmes. Vous pouvez faire un audit de sécurité si vous êtes inquiet. Il serait étrange de facturer pour l'un de ces outils.

Une partie de notre mission est d'ouvrir le développement de logiciels mobiles aux enfants. Parfois, je pense que si j'avais 13 ou 14 ans maintenant, et que mes amis et moi étions tous assis sur nos téléphones, je penserais à des moyens de créer des trucs sympas pour nous amuser. Mais si vous facturez de l'argent pour cela, vous excluez les enfants qui sont impatients d'apprendre. Ils n'ont pas de cartes de crédit, et leurs parents sont peu susceptibles de leur donner de l'argent pour quelque chose qu'ils ne comprennent peut-être pas.

De cette manière, cela a du sens pour moi, c'est un modèle économique similaire à Twitch et YouTube. YouTube ne facture pas les gens pour télécharger des vidéos, et Twitch ne facture pas les gens pour diffuser. Mais si ils vous aident à gagner de l'argent, ils peuvent prendre une partie de celui-ci.

Alors, j'espère que si nous pouvons aider les développeurs à monétiser, alors il y aura un moyen pour nous de prendre une petite partie. Mais pour la plupart, je veux que ce soit gratuit et open source pour toujours. Si nous pouvons aider les gens à construire des entreprises durables sur notre plateforme, alors il y aura beaucoup de moyens pour nous de nous soutenir.

#### **Pouvez-vous parler d'une ou deux périodes vraiment difficiles que vous avez dû traverser en construisant Expo ?**

J'ai l'impression qu'il y aura des moments vraiment difficiles à venir, mais nous sommes passionnés par notre mission, alors cela n'a pas encore semblé si difficile jusqu'à présent. Je savais que cela allait prendre beaucoup de temps et qu'il y aurait beaucoup de défis à venir, mais au cours des derniers mois, nous avons très bien exécuté et mis en place quelques bonnes pièces du puzzle qui ont rendu notre message plus clair.

Une partie de cela est due au fait qu'il y a beaucoup de façons dont les développeurs se retrouvent dans différents états, donc nous avons des réponses à beaucoup de ces questions, mais ensuite, il est difficile d'expliquer tout ce que nous faisons. Si vous avez commencé un projet avec React Native, vous obtenez ce dossier IOS et ce dossier Android avec toutes vos sources JavaScript, si vous n'avez écrit aucun code natif IOS ou Android, et que vous avez juste du JavaScript, nous avons un script de convergence. C'est un peu bancal car il y a tant de façons différentes de faire des changements à votre projet.

Notre grand objectif maintenant est d'aider les nouvelles personnes à venir à bord.

Nous avons une grande équipe et nous travaillons bien ensemble, donc cela a été amusant. Beaucoup de personnes dans notre équipe sont des contributeurs actifs au projet open source React Native, et travailler chez Expo est un moyen de pouvoir travailler complètement dans cet espace. Le genre de personnes qui travaillent dans le dépôt React Native sont celles qui se soucient de la façon dont les applications mobiles sont construites et du développement mobile. Cela résonne avec eux lorsque la vision d'Expo est de rendre la construction de logiciels mobiles plus facile, plus rapide et plus accessible. Ils sont souvent les plus réfléchis sur la façon dont ils font le développement.

#### **Qu'est-ce qui est prévu pour Expo ?**

Nous allons travailler très dur pour devenir la méthode la plus standard, la plus simple et la meilleure pour démarrer tout nouveau projet React Native. Nous voulons également ajouter plus de capacités de modules natifs.

J'ai publié [10 raisons d'utiliser Expo](https://www.facebook.com/groups/react.native.community/permalink/945445875590991/) dans le groupe communautaire React Native et l'une d'elles était qu'Expo est simplement React Native régulier, plus quelques autres trucs. Par exemple, l'un des plus grands défis pour les développeurs React Native est non seulement de faire les mises à jour régulières eux-mêmes, mais beaucoup des modules tiers ne sont pas mis à jour et restent sur une version plus ancienne, comme certains modules bluetooth ou de localisation en arrière-plan vraiment personnalisés. Parce que la bibliothèque React Native publie réellement de nouvelles versions toutes les quelques semaines, il a été difficile pour beaucoup de bibliothèques natives de suivre le rythme des changements.

Un autre objectif pour nous au cours de l'année prochaine est de donner aux gens les blocs de construction dont ils ont besoin pour le mobile. Une chose que je n'aime pas sur le web, peut-être parce que le web a commencé comme un moyen de créer des documents, est essentiellement du texte qui s'écoule, et peut-être quelques images dedans, plus des rectangles pour le disposer, et les formulaires. C'est super, mais c'était ce dont le monde avait besoin en 1994.

Si vous pensez à ce que les gens aiment faire sur leurs téléphones, c'est beaucoup d'images, de vidéos, de streaming, de balayage, de likes et de lecture de sons. C'est une expérience beaucoup plus tactile et multimédia. Nous essayons d'être les bons blocs de construction pour les personnes qui veulent créer des logiciels mobiles. Nous n'avons peut-être pas toutes les réponses aujourd'hui, mais c'est la direction que nous visons pour cette année à venir.

#### **Quels sont certains de vos hobbies ou intérêts en dehors de votre startup ?**

Littéralement, j'ai écouté beaucoup de [Ryan Adams](https://en.wikipedia.org/wiki/Ryan_Adams) sans arrêt depuis deux ans, et je pense que je me suis un peu plus impliqué politiquement que par le passé, simplement parce que cela semble important cette année d'une manière qui ne l'a pas été pour la plupart de ma vie.

J'ai grandi à Pittsburgh, donc je suis un fan des [Penguins](https://en.wikipedia.org/wiki/Pittsburgh_Penguins), des [Steelers](http://www.steelers.com/), des [Pirates](https://www.mlb.com/pirates). Les Penguins ont remporté la Coupe Stanley l'année dernière à San Jose et j'ai pu voir cela se produire, c'était cool.

![Image](https://cdn-media-1.freecodecamp.org/images/0*bfU6sACh7uVZN2Yu.png)
_Pittsburgh Penguins_

[Faites un don pour soutenir ce projet](https://opencollective.com/betweenthewires).

Ce projet est rendu possible grâce aux parrainages de [frontendmasters.com](https://frontendmasters.com/), [egghead.io](https://egghead.io/), [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge) et [Google Developers](https://developers.google.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*bMdgkbz1ZwgKR-Wp.png)
_Nos sponsors._

Pour suggérer un créateur que vous aimeriez entendre, veuillez remplir ce [formulaire](https://goo.gl/forms/XhR1IyLXJHNMljcp1).

Vous pouvez également envoyer des commentaires à [betweenthewires](https://twitter.com/betweenthewires) sur Twitter.