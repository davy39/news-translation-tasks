---
title: Apprenez les bases de Unity 2D et des jeux de plateforme avec cet aperçu
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-17T21:33:36.000Z'
originalURL: https://freecodecamp.org/news/take-a-tour-of-unity-2d
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f41740569d1a4ca419d.jpg
tags:
- name: C
  slug: c
- name: Game Development
  slug: game-development
- name: learn to code
  slug: learn-to-code
- name: unity
  slug: unity
seo_title: Apprenez les bases de Unity 2D et des jeux de plateforme avec cet aperçu
seo_desc: 'By M. S. Farzan

  If you''re shopping around for a 2D game engine, you''ve undoubtedly come across
  Unity. Dipping your toe into Unity''s editor can be overwhelming if you haven''t
  had a good overview of where all of the tools live, particularly if it''s als...'
---

Par M. S. Farzan

Si vous cherchez un moteur de jeu 2D, vous avez sans doute rencontré [Unity](https://unity.com/). Plonger dans l'éditeur de Unity peut être écrasant si vous n'avez pas eu un bon aperçu de l'emplacement de tous les outils, en particulier si c'est aussi votre première fois à utiliser C# pour écrire des scripts.

Dans cet article, je vais vous donner un tour des fonctionnalités 2D de Unity avec un aperçu des outils dont vous aurez besoin pour créer un jeu de plateforme - ou tout autre type de jeu 2D - et où les trouver dans l'éditeur !

Si vous envisagez Unity parmi d'autres moteurs de jeu 2D, consultez [cet article](https://www.freecodecamp.org/news/what-2d-game-engine-to-use-for-your-next-game/) pour quelques options.

Et si vous préférez une visite visuelle de Unity, regardez plutôt cette vidéo (28 minutes) :

%[https://youtu.be/w2hxVVnbEFA]

Dans cet aperçu, nous utiliserons le [Warped City Unity Assets Pack](https://assetstore.unity.com/packages/2d/environments/warped-city-assets-pack-138128) par [Ansimuz](https://assetstore.unity.com/publishers/18720).

## Aperçu

À première vue, l'éditeur de Unity semblera familier si vous avez utilisé un autre moteur de jeu "tout-en-un", mais si c'est votre première entrée dans le développement de jeux, cela peut être écrasant. De plus, si vous n'avez pas déjà une certaine expérience de travail en C#, je vous recommande fortement de faire quelques tutoriels en utilisant [Microsoft's .NET](https://dotnet.microsoft.com/learn) ou similaire. Unity a une courbe d'apprentissage relativement raide, et si vous pouvez venir avec une certaine maîtrise de base de C#, vous aurez une expérience d'intégration plus facile.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-1.png)

Vous passerez beaucoup de temps dans la hiérarchie (1), qui vous permet de garder une trace de tous vos objets de jeu dans une "scène" donnée, qui est une partie spécifique de votre jeu (comme votre menu "Start" ou un monde de jeu particulier dans votre jeu de plateforme). Avec elle, vous pouvez imbriquer des objets sous d'autres, gérer vos caméras et canevass, et naviguer à travers tous les objets de jeu que vous avez créés.

Vous voudrez rester organisé dans votre onglet de projet (2), qui agit comme un système de fichiers que vous pouvez structurer comme vous le souhaitez. Une bonne pratique, par exemple, est de collecter tous vos actifs dans un dossier, les animations dans un autre, les scripts dans un autre, et ainsi de suite. Vous pouvez également cliquer sur l'onglet de la console si vous avez demandé à Unity de journaliser des choses dans des circonstances que vous dictez.

En cliquant sur un objet de jeu, soit dans la hiérarchie ou l'onglet de projet, vous serez accueilli avec plus de détails dans l'inspecteur (3). Ces détails dépendront du type d'objet sur lequel vous avez cliqué, et de ce que vous avez attaché à cet objet de jeu. Si vous avez créé un objet de jeu vide, par exemple, il n'y aura pas grand-chose là. Mais si vous avez fait un personnage joueur qui a un sprite attaché, ainsi qu'un contrôleur d'animation, un rigidbody2d pour gérer la physique, un collider2d pour gérer les collisions, et un script pour gérer les entrées utilisateur et l'interactivité, tous ceux-ci apparaîtront dans l'inspecteur pour que vous puissiez les ajuster.

Le reste de l'espace dans l'éditeur est occupé par la scène elle-même (4), où vous construirez votre monde de jeu, déposerez des objets et des déclencheurs, et vous occuperez de la conception de votre jeu. Vous pouvez cliquer sur l'onglet de jeu pour voir à quoi ressemble réellement votre jeu lorsqu'il est joué (et le jouer en appuyant sur le bouton "play"), ou consulter l'Asset Store depuis la sécurité de votre client Unity.

## Où trouver des choses comme l'Animateur

Si vous avez lu [un de mes écrits sur les moteurs de jeu](https://www.freecodecamp.org/news/what-2d-game-engine-to-use-for-your-next-game/), vous m'avez entendu me plaindre du support 2D de Unity étant inséré de force dans un environnement 3D, et de la difficulté à localiser les outils dont vous avez besoin pour accomplir votre travail.

Disons simplement que certaines choses sont difficiles à accomplir dans Unity par rapport à d'autres moteurs de jeu 2D, mais elles sont toutes encore possibles. Si vous essayez d'accéder à l'animateur, par exemple, vous devrez sélectionner Window > Animation > Animator, ce qui est différent de l'emplacement des animations que vous créerez minutieusement et enregistrerez dans votre onglet de projet.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-2.png)

De même, si vous souhaitez accéder aux paramètres de Physics 2D, cliquez sur Edit > Project Settings, qui sont différents de vos préférences personnelles, situées sous Edit > Preferences. Et si vous cherchez à ajuster les builds, vous voudrez aller à File > Build Settings.

De même, si vous voulez simplement créer un objet de jeu ordinaire, allez à GameObject > Create Empty (ou 2D Object si vous savez ce que vous cherchez). Si, au contraire, vous essayez d'ajouter un rigidbody à un objet de jeu existant, vous devrez aller à Component > Physics 2D > Rigidbody 2D (ou cliquer sur "Add Component" dans l'inspecteur lorsque vous avez l'objet de jeu sélectionné dans la hiérarchie).

Je pense qu'il est clair à ce stade que trouver les choses dont vous aurez besoin pour accomplir votre travail peut être compliqué, imbriquées qu'elles sont dans différents menus. Cela n'aide pas que certains des outils eux-mêmes, comme l'animateur, soient maladroits par rapport à leurs homologues dans d'autres moteurs de jeu 2D, mais une fois que vous aurez compris comment ils fonctionnent, vous les trouverez parfaitement utilisables.

## Visual Studio et le scripting C#

Unity supporte C# pour écrire des scripts, et vous pouvez l'associer à Visual Studio pour un environnement de développement intégré relativement indolore.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-3.png)

Les scripts sont facilement accessibles via l'éditeur, et vous devrez les attacher à vos objets de jeu pour faire faire à votre jeu à peu près n'importe quoi. Une fonctionnalité amusante est de déclarer une variable publique dans un script - disons, un entier appelé "jumpSpeed" - puis d'attacher ce script à un objet de jeu dans l'inspecteur. Vous verrez cette variable exposée dans l'éditeur Unity, et pourrez la changer à la volée pendant que votre jeu est en cours d'exécution pour voir comment vos changements fonctionnent en action.

## Prefabs

Enfin, Unity utilise ce qu'ils appellent des "prefabs" pour rationaliser votre flux de travail. En essence, un prefab est un type d'objet réutilisable que vous avez créé afin de pouvoir le déposer dans votre monde de jeu encore et encore sans avoir besoin de personnalisation répétée.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-4.png)

Supposons que vous créiez un monstre dans votre jeu d'aventure 2D en vue de dessus en tant qu'objet de jeu vide, puis attachez un sprite, un rigidbody2d, un collider2d, des animations et un script de contrôleur. Vous pouvez glisser ce monstre dans votre onglet de projet pour en faire un prefab, ce qui vous permet de l'utiliser encore et encore dans votre monde de jeu sans avoir à répéter tout le processus à chaque fois.

Unity possède plusieurs autres fonctionnalités qui supportent le développement de jeux 2D, dont certaines sont couvertes dans la vidéo ci-dessus, et il serait utile de regarder quelques tutoriels sur des aspects spécifiques de l'éditeur si vous envisagez de l'utiliser pour votre prochain jeu. Je vous recommande particulièrement de vous rafraîchir la mémoire sur C# avant de vous attaquer à l'éditeur lui-même, car cela vous offrira une courbe d'apprentissage plus douce.

J'espère que cet aperçu sera utile pour votre prochain jeu !

Si vous avez aimé cet article, envisagez de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** a écrit et travaillé pour des entreprises de jeux vidéo et des sites éditoriaux de haut profil tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer Principal de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](http://www.twitter.com/sominator).