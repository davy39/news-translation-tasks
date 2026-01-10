---
title: J'ai tenté de créer le même prototype de jeu 2D dans React, Unity, Godot, Construct,
  Game Maker et Phaser. Voici ce que j'ai découvert.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-11T16:17:31.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-a-2d-prototype-in-different-game-engines
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/EntromancyHB_Logo_COLOR.jpg
tags:
- name: phaser 3
  slug: phaser-3
- name: C
  slug: c
- name: construct 3
  slug: construct-3
- name: Game Development
  slug: game-development
- name: game-maker-2
  slug: game-maker-2
- name: Godot
  slug: godot
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: unity
  slug: unity
seo_title: J'ai tenté de créer le même prototype de jeu 2D dans React, Unity, Godot,
  Construct, Game Maker et Phaser. Voici ce que j'ai découvert.
seo_desc: 'By M. S. Farzan

  I''m a tabletop game developer. In designing a new card game, I decided to build
  a digital prototype to help me run simulations and easily share a proof of concept
  with collaborators.

  I have some background in JavaScript and C#, and I ...'
---

Par M. S. Farzan

Je suis un développeur de jeux de société. En concevant un nouveau jeu de cartes, j'ai décidé de créer un prototype numérique pour m'aider à exécuter des simulations et à partager facilement une preuve de concept avec des collaborateurs.

J'ai quelques connaissances en JavaScript et C#, et je me suis lancé comme beaucoup le font : en passant un temps excessif dans des fils de discussion "quel framework devrais-je utiliser" et en lisant de la documentation sans vraiment créer quoi que ce soit.

Plusieurs mois plus tard, j'ai maintenant passé plus de temps à travailler (et à lutter) avec React, Unity, Godot, Construct 3, Game Maker Studio 2 et Phaser 3, dans le but de comprendre ce qui les fait fonctionner.

Je dois admettre que j'ai probablement passé _beaucoup plus_ de temps dans chacun d'eux que nécessaire pour créer mon petit jeu, et que j'aurais probablement pu simplement rester avec le premier et me débrouiller pour le prototype. J'espère que les informations ci-dessous seront utiles pour toute autre personne qui cherche un moteur ou un framework.

Plusieurs mises en garde : je n'essaie pas de vendre un moteur ou un framework plutôt qu'un autre, et je ne suggère pas non plus qu'un ou plusieurs de ces frameworks fonctionneront mieux pour votre jeu qu'un autre. Je ne compare pas non plus les prix, les fonctionnalités back-end ou le déploiement sur différentes plateformes. Ainsi, selon vos exigences, les informations ci-dessous peuvent avoir une valeur différente pour vous.

De plus, cette expérience est basée sur le développement d'un jeu de cartes 2D, donc je ne discuterai pas des moteurs 3D, de la physique, etc.

Vous pouvez également **passer directement à la conclusion pour le résumé**.

%[https://www.youtube.com/watch?v=gtKEkuhsWOs]

## Le Prototype

Mon jeu, _Entromancy: Hacker Battles_, est un jeu de cartes cyberpunk compétitif avec des mécaniques légères de TCG. Vous pouvez en lire plus sur notre [site web](https://www.entromancy.com) ou regarder comment il est censé être joué dans [cette vidéo](https://www.entromancy.com/single-post/2019/09/26/Get-a-Sneak-Peek-at-Entromancy-Hacker-Battles). Mais il suffit de dire que, en tant que jeu de cartes, il nécessite un framework numérique potentiel pour supporter des choses de base comme la gestion d'état, l'UI, l'UX de glisser-déposer et des hooks back-end pour implémenter le multijoueur.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/HackerBattles_Card-Mockup.png)

Étant donné ces exigences, j'ai exploré les frameworks et moteurs suivants pour voir lequel serait le plus adapté à la création de mon jeu... au lieu de réellement _créer_ le jeu (je suis heureux de dire que maintenant que j'ai choisi un framework, je fais beaucoup plus de progrès).

Vous pouvez accéder à une version jouable [ici](https://sominator.github.io/hacker-battles/), et bien que le jeu soit plus avancé que ce que la version live du prototype pourrait suggérer, cette version est assez stable (au moins dans Chrome).

## React

Ayant déjà construit un prototype de générateur de personnages dans [React](https://reactjs.org/) pour un [RPG de table que j'ai conçu](https://www.entromancy.com/rpg), j'ai pensé qu'une étape naturelle serait de donner une chance au framework pour le jeu de cartes. J'ai trouvé que la gestion d'état était une brise (c'est ce que React _fait_, après tout), tandis que l'implémentation d'une simple fonctionnalité de glisser-déposer pour les cartes s'est avérée être un cauchemar.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/React_Native_Logo.png)

Il existe quelques bibliothèques qui peuvent aider avec le glisser-déposer de base (par exemple, [React DnD](https://react-dnd.github.io/react-dnd/about)), mais j'ai trouvé que pour un jeu de cartes, j'avais besoin d'une solution plus élégante pour les zones de dépôt, car Hacker Battles est très spécifique quant aux cartes qui peuvent être jouées où et quand.

Cette expérience m'a conduit à découvrir [boardgame.io](https://boardgame.io/), qui peut fonctionner en tandem avec React. Mais cela a finalement nécessité d'apprendre un autre framework en plus d'un framework existant, ce qui était moins qu'idéal pour mes besoins.

## Unity

Par intérêt général, j'avais passé beaucoup de temps dans [Unity](https://unity.com) à faire des tutoriels et à apprendre à utiliser l'éditeur avant d'essayer de recréer le prototype de jeu de cartes avec celui-ci. L'asset store est une excellente ressource, et il y a tellement de documentation, officielle et non officielle, que j'étais confiant de pouvoir trouver une réponse à tout problème que je pourrais rencontrer.

Mon expérience avec Unity jusqu'à présent a été mitigée. J'aime vraiment travailler en C#, et tout ce qui est lié au code a été une expérience relativement sans douleur. Cependant, Unity est très spécifique quant à son implémentation et peut sembler contre-intuitif à certains moments.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1280px-Unity_Technologies_logo.svg.png)

L'éditeur, en revanche, est un vrai casse-tête à utiliser. Pour exploiter tout le potentiel de Unity, vous devez passer un bon moment à lutter avec l'UI pour comprendre où tout se trouve et comment l'utiliser. Il est également désespérément en retard en matière de développement de jeux 2D, essayant clairement d'aplatir un moteur principalement 3D en un plan 2D, avec des résultats mitigés.

Pour être juste, j'aime bien travailler dans l'éditeur Unity, aussi encombrant soit-il. Mais si vous cherchez un moteur de jeu 2D, votre qualité de vie sera bien meilleure ailleurs (regardez une vidéo sur le système d'animation de Unity ou sur la réalisation de la perfection pixel et vous verrez ce que je veux dire).

En fin de compte, la gestion de l'espace 2D par Unity est un peu plus complexe que ce dont j'ai besoin pour mon prototype, mais je reviendrai pour d'autres types de jeux.

De plus, une note en marge qui pourrait être utile à certains : j'étais initialement très excité par l'asset store, avec l'idée que je pourrais acheter un modèle de jeu de cartes qui rendrait le processus de développement beaucoup plus facile pour moi. Cela n'a pas fonctionné. La plupart d'entre eux étaient des clones de MTG/Hearthstone/etc. qui nécessiteraient autant de temps de développement de ma part pour les restructurer pour mon jeu de cartes que de simplement commencer à partir de zéro. <shrug>

## Godot

Ma première pensée en rencontrant [Godot](https://godotengine.org) a été : "un moteur de jeu open source qui supporte C# ? Inscrivez-moi !" Ensuite, je l'ai téléchargé, j'ai travaillé sur quelques tutoriels de base, et il a planté lors de la compilation. Hum.

Plusieurs recherches Google, réinstallations et cheveux arrachés plus tard, j'ai compris que cela avait quelque chose à voir avec ma version de VS Build (je pense ?), ce qui m'a conduit dans un terrier de lapin séparé. Je savais par expérience que d'autres moteurs - Unity en tête - pouvaient causer des problèmes de jeu complètement en dehors de votre propre code, mais c'était un obstacle ennuyeux qui a probablement coloré le reste de mon expérience avec Godot.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Godot_logo.svg)

En termes d'éditeur, j'ai beaucoup aimé l'implémentation basée sur les nœuds de Godot, que j'ai trouvée contre-intuitive en venant des préfabriqués de Unity, mais à laquelle je me suis finalement habitué. Je dirais même que sa fonctionnalité 2D est _meilleure_ que celle de Unity, mais il lui manque la communauté, l'asset store (voir la note en marge ci-dessus) et surtout, la documentation que possède Unity. Si vous prévoyez de travailler en C# avec Godot, par exemple, soyez prêt à chercher des réponses dans le GDScript personnalisé du moteur et à les traduire en C#.

J'ai cependant entendu parler de personnes ayant connu un grand succès avec Godot en utilisant GDScript, donc si vous êtes prêt à investir du temps pour l'apprendre, vous pourriez apprécier ce que Godot a à offrir.

## Construct 3

Dans les mises en garde que j'ai listées ci-dessus, j'ai mentionné que je n'inclus pas le prix comme point de discussion. Pourtant, je pense devoir en parler avec [Construct 3](https://construct.net/), car cela s'est avéré impactant dans mon expérience.

Contrairement aux autres moteurs de jeu listés ici, qui sont, pour la plupart, gratuits à utiliser (Game Maker Studio 2 a un essai gratuit de 30 jours), la grande majorité des fonctionnalités de Construct sont derrière un paywall, et un abonnement en plus. Ugh.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Construct_3_Logo.svg)

J'aime vraiment, _vraiment_ le style de Construct pour les jeux 2D simples. L'éditeur ressemble un peu à une mise à niveau de MS Paint, mais il gère très bien les sprites et les objets, et est tout simplement facile à utiliser. Je n'aime pas qu'il utilise un style de "scripting visuel", mais ils ont récemment ajouté la possibilité d'écrire du bon vieux JavaScript et cela semble fonctionner plus ou moins.

J'ai pu créer une architecture très rudimentaire pour le prototype en un court laps de temps avant de fermer la démo de Construct 3 (qui s'exécute dans un navigateur)... puis j'ai tout réessayé plus tard avec une nouvelle démo. Je pense que, au moins pour ce jeu de cartes, je pourrais faire beaucoup avec Construct 3, mais je ne suis tout simplement pas prêt à payer 99 $/an (ou plus, en tant qu'entreprise) pour un prototype.

## Game Maker Studio 2

YoYo Games a clairement fait beaucoup de travail pour rendre [Game Maker Studio 2](https://www.yoyogames.com/gamemaker) accessible et facilement navigable, et cela se voit. De tous les moteurs que j'ai utilisés pour ce projet, j'aime le plus l'éditeur GMS. Pour un petit projet, il est facile de s'y retrouver et de vaquer à ses occupations. Je suspecte, cependant, qu'un projet plus grand pourrait rapidement devenir ingérable.

Cela pourrait être influencé par le langage propriétaire de Game Maker Studio, GML (bien que GMS 2 supporte le scripting visuel, que je n'ai pas utilisé). Cela fonctionne, mais si vous venez d'un autre langage OOP (ou, vraiment, de tout autre langage largement utilisé), vous pourriez vous gratter la tête devant l'implémentation ou en essayant de comprendre comment faire certaines choses. Si vous êtes un débutant ou prêt à passer du temps à comprendre comment GMS _veut_ que vous utilisiez GML, vous serez probablement bien.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/download.png)

J'ai rencontré quelques bizarreries avec la fonctionnalité de glisser-déposer de Game Maker Studio - notamment, la détection du pointeur de la souris lors du glisser est un peu capricieuse et nécessite un peu d'échafaudage pour fonctionner correctement.

Je pense - et c'est totalement une préférence personnelle et de la paresse de ma part - que si GMS offrait la possibilité d'utiliser un autre langage de programmation non propriétaire, je passerais du temps à faire plus de dégâts ici. Je suis pour monter en niveau plusieurs compétences en travaillant, alors que passer du temps à devenir un expert dans l'éditeur GMS _et_ GML sans pouvoir appliquer facilement ces connaissances ailleurs ne semble pas valable.

Néanmoins, c'est un éditeur 2D assez fonctionnel, et bien que le support de la communauté ne soit peut-être pas à la hauteur de celui de Unity, il est toujours assez bon. Attention également, une fois votre essai gratuit terminé, vous devrez payer pour continuer à utiliser Game Maker Studio 2.

## Phaser 3

[Phaser](https://www.freecodecamp.org/news/how-i-made-a-2d-prototype-in-different-game-engines/phaser%20io) est un framework de jeu JavaScript léger et open-source. Il existe quelques IDE Phaser, mais si vous êtes du genre à vouloir travailler principalement en code, vous pourriez vous retrouver ici, en utilisant Atom, Sublime ou votre éditeur préféré.

Phaser 2 était et est largement utilisé et bien documenté avec une tonne de tutoriels à utiliser. Phaser 3 est l'inverse. Il a une courbe d'apprentissage relativement élevée pour les débutants, avec un tas d'exemples et peu de contexte autour d'eux.

Beaucoup des tutoriels disponibles supportent Phaser 2, et bien que l'apprentissage soit transférable, le code ne l'est pas. De plus, les développeurs [ont récemment annoncé qu'ils passeront à Phaser 4](https://madmimi.com/p/4f5f0f) (et TypeScript plutôt que ES6), ce qui n'est pas idéal si vous avez passé du temps à travailler dans Phaser 3.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Phaser_-game_framework-_logo.png)

Si vous n'êtes pas un programmeur professionnel (je ne le suis pas) et à jour avec les classes ES6 et les meilleures pratiques JavaScript (je ne l'étais pas), vous pourriez rapidement vous frustrer avec le manque de prise en main de Phaser et devoir configurer votre propre IDE et flux de travail (je l'étais).

Cependant, je l'ai trouvé être un framework puissant et léger qui fait beaucoup de choses de manière beaucoup plus rationalisée que d'autres moteurs de jeu. La fonctionnalité de glisser-déposer pour le jeu de cartes a été relativement facile, et la capacité de séparer les types de cartes en classes (un peu comme les préfabriqués de Unity) a compartimenté une partie de la charge cognitive que ce type de jeu nécessite.

Si vous êtes un développeur front-end, vous pourriez aimer ou être à l'aise avec le codage en dur des coordonnées de pixels pour tout, mais bon sang, ce travail est fastidieux. De plus, si vous n'êtes pas à jour sur tout ce qui concerne JavaScript, vous serez probablement à la recherche de réponses dans des cercles non-Phaser et à les appliquer à votre projet, ce qui a son propre avantage, je suppose.

Une autre note au cas où ce ne serait pas clair : Phaser 3 _a_ effectivement beaucoup de documentation officielle et d'exemples, mais il _n'a pas_ la communauté ou les réponses Stack Overflow que beaucoup d'autres moteurs de jeu ont. Si vous rencontrez un problème ou ne parvenez pas à comprendre quelque chose, vous devrez trouver votre propre solution ou poser votre question sur le serveur Discord de Phaser, ce qui a été utile dans mon expérience.

## Conclusion

Étant donné tout ce qui précède, le prototype auquel je me suis tenu et que je continue à itérer est celui que j'ai construit avec Phaser 3. Je réalise que cela peut être anticyclique, car Phaser n'est pas intrinsèquement "meilleur" que les autres frameworks et moteurs pour le développement de jeux 2D (sauf peut-être React, qui n'essaie pas d'être un concurrent dans l'espace des jeux numériques).

Phaser semble cependant gérer le glisser-déposer et la gestion de la boucle de jeu pour _Hacker Battles_ plus facilement, et pour mes besoins, c'est important. J'apprécie également que l'utilisation de Phaser me demande d'investir plus lourdement dans les écosystèmes et communautés JavaScript, mais je suis intéressé à le faire de toute façon, donc cela semble être un bonus.

Si vous êtes plus du type "que puis-je utiliser pour construire quelque chose rapidement et ne pas me soucier du contexte dans lequel le moteur est situé", YMMV.

## TL;DR

**React** : excellent pour le développement front-end. Ne l'utiliserais pas pour les jeux, en particulier le glisser-déposer.

**Unity** : vous pouvez créer n'importe quel type de jeu 2D si vous êtes prêt à lutter avec l'éditeur et les idiosyncrasies sous-jacentes 3D. Excellent support communautaire, et C# est génial. L'asset store existe, mais peut ne pas être utile pour vos besoins.

**Godot** : open source et supporte GDScript, C#, même C++ et Python si vous êtes prêt à faire beaucoup de travail. Bonnes implications 2D mais pas près d'avoir autant de support communautaire que quelque chose comme Unity. De plus, mon expérience a été buggée.

**Construct 3** : vraiment facile à utiliser, barrière d'entrée élevée en raison du paywall d'abonnement. Le scripting visuel peut vous énerver si vous cherchez à utiliser ou apprendre du code, bien qu'il y ait maintenant un certain support JavaScript.

**Game Maker Studio 2** : éditeur convivial avec un bon support communautaire. GML ou le scripting visuel peut ne pas être votre tasse de thé si vous venez d'un autre langage de programmation plus populaire, mais bon, quand à Rome. De plus, nécessite un paiement après un essai gratuit de 30 jours.

**Phaser 3** : attendez-vous à tout coder, et à faire beaucoup de recherches pour comprendre comment faire fonctionner les choses. Cela fonctionne pour moi pour ce jeu et ce prototype particuliers, mais Phaser 4 est en route, donc il y a cela.

J'espère que cet article sera utile dans votre propre recherche et processus de discernement. J'adorerais entendre parler de vos propres expériences avec l'un de ces frameworks/moteurs ou d'autres !

Si vous avez aimé cet article, envisagez de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** a écrit et travaillé pour des entreprises de jeux vidéo de haut profil et des sites éditoriaux tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer Principal de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](http://www.twitter.com/sominator).