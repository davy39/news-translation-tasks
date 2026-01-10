---
title: Quel moteur de jeu 2D utiliser pour votre prochain jeu
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-04T20:47:36.000Z'
originalURL: https://freecodecamp.org/news/what-2d-game-engine-to-use-for-your-next-game
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f9f740569d1a4ca4397.jpg
tags:
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
- name: phaser 3
  slug: phaser-3
- name: React
  slug: react
- name: unity
  slug: unity
seo_title: Quel moteur de jeu 2D utiliser pour votre prochain jeu
seo_desc: 'By M. S. Farzan

  A few weeks ago, I posted about my experience attempting to make a prototype in
  a bunch of different 2D game engines/frameworks to learn what makes them tick.

  If you''re shopping around for an engine for your next 2D game, this article...'
---

Par M. S. Farzan

Il y a quelques semaines, j'ai [publié mon expérience](https://www.freecodecamp.org/news/how-i-made-a-2d-prototype-in-different-game-engines/) en tentant de créer un prototype dans plusieurs moteurs et frameworks de jeux 2D différents pour comprendre ce qui les fait fonctionner.

Si vous cherchez un moteur pour votre prochain jeu 2D, cet article vous fournira quelques éléments à considérer pour vous aider dans votre processus de discernement.

Notez que je ne cherche pas à couvrir tous les moteurs de jeux 2D existants, ni à positionner un moteur ou un framework au-dessus d'un autre. Ces recommandations sont basées sur mon expérience personnelle en utilisant différents moteurs et frameworks pour le prototypage.

Et si vous préférez regarder plutôt que lire, j'ai créé une version vidéo de cet article (26 minutes) :

%[https://www.youtube.com/watch?v=gtKEkuhsWOs]

## React

À première vue, vous pourriez penser : "[React](https://reactjs.org/) est un framework front-end pour créer des sites web interactifs. Ce n'est pas un moteur de jeu !" Et vous auriez raison.

React ne fournit pas de support natif pour les bases du développement de jeux, comme par exemple la physique 2D, mais il gère extrêmement bien l'état. Si vous êtes déjà un développeur JavaScript et prêt à associer React avec quelque chose comme [boardgame.io](https://boardgame.io/) pour créer un jeu 2D simple, vous pourriez potentiellement avoir un prototype opérationnel assez rapidement.

Pour tous les autres types de jeux 2D, vous voudrez regarder ailleurs.

## Unity

[Unity](https://unity.com/) s'est imposé comme un acteur incontournable dans les domaines du développement de jeux 2D et 3D. Je le positionnerais comme un excellent moteur de jeu 3D et un moteur 2D fonctionnel.

L'éditeur Unity est assez complexe, avec de nombreux menus imbriqués qui prennent un certain temps à maîtriser (consultez [cet article](https://www.freecodecamp.org/news/take-a-tour-of-unity-2d/) pour une visite de ses fonctionnalités 2D). Si vous n'avez pas déjà une expérience en C#, que Unity utilise pour le scripting, vous voudrez vous familiariser avec ce langage avant d'apprendre Unity, car cela facilitera votre courbe d'apprentissage globale.

Unity fait également beaucoup de choses de manière "compliquée" en ce qui concerne le développement de jeux 2D, ce qui ne semble pas natif par rapport à d'autres moteurs de jeu. Créer un monde de jeu 2D dans Unity, par exemple, donne l'impression que vous forcez un plan 2D dans un grand espace 3D, et des éléments comme l'animation et la perfection des pixels sont plus maladroits que dans d'autres moteurs spécifiques à la 2D.

Vous pouvez créer n'importe quel type de jeu 2D avec Unity si vous êtes prêt à lutter avec l'éditeur et les idiosyncrasies sous-jacentes de la 3D. Il bénéficie d'un soutien communautaire étendu, et vous trouverez que travailler avec C# est un plaisir. De plus, l'Asset Store de Unity propose toutes sortes d'arts et de modèles à télécharger et à acheter, mais attention : vous pourriez passer autant de temps à réécrire le code de quelqu'un d'autre pour l'adapter à votre projet qu'à commencer à partir de zéro.

Unity est, en général, gratuit à utiliser, mais les tarifs deviennent plus complexes si vous souhaitez utiliser _tout_ ce qu'il a à offrir (voir [cette page](https://store.unity.com/compare-plans) pour plus de détails).

## Godot

[Godot](https://godotengine.org/) est un moteur de jeu 2D et 3D gratuit et open source qui supporte GDScript, C#, et même C++ et Python si vous êtes prêt à faire beaucoup de travail pour les faire fonctionner. Il supporte un flux de travail de type nœud et est super léger.

Si vous êtes a) prêt à investir dans l'apprentissage de GDScript ou b) déjà très bon en C#, C++ ou Python, vous vous en sortirez probablement bien avec Godot, surtout si vous aimez travailler avec des logiciels open source. Sinon, vous pourriez vous frustrer facilement, car il n'y a pas presque autant de support pour C# ou d'autres langages que pour GDScript. Néanmoins, Godot est un moteur agréable avec lequel travailler, et bien qu'il n'ait peut-être pas le même pedigree et soutien communautaire que quelque chose comme Unity, si vous êtes un autodidacte, vous pourriez vous y sentir bien chez vous.

## Construct 3

Si vous voulez simplement créer des jeux 2D et que vous ne vous souciez pas du langage de programmation ou des frais d'abonnement, vous trouverez que [Construct 3](https://www.construct.net/en) a tout ce dont vous avez besoin pour mettre en place une démo rapidement. Tout votre travail sera effectué dans un navigateur, en utilisant des outils de glisser-déposer (et un support JavaScript personnalisé si nécessaire).

Ne vous attendez pas à avoir une expérience productivement significative avec Construct 3 gratuitement, cependant. Il y a une simple démo que vous pouvez essayer, mais le développement de jeux impactant avec Construct 3 est verrouillé derrière un paywall, et un abonnement en plus.

## Game Maker Studio 2

[Game Maker Studio 2](https://www.yoyogames.com/gamemaker) dispose d'un éditeur convivial qui supporte un langage propriétaire appelé, de manière appropriée, Game Maker Language (GML), ainsi que la programmation visuelle. Il dispose également de nombreux tutoriels, d'un excellent soutien communautaire et d'une boutique d'assets (qui vient avec les mêmes mises en garde que celle d'Unity, ci-dessus).

Le flux de travail général de Game Maker Studio 2 et des choses comme l'animation de sprites, la configuration de votre monde de jeu, etc., sont simples et intuitifs. GML pourrait ne pas être votre tasse de thé si vous venez d'un autre langage de programmation plus largement utilisé, et je ne le recommanderais _pas_ comme votre première introduction à l'apprentissage de la programmation. Il emploie certains des concepts de base de la programmation, mais pas des détails importants tels que les meilleures pratiques de codage ou comment écrire un code propre.

De plus, vous pouvez essayer Game Maker Studio 2 avec un essai gratuit de 30 jours, mais vous devrez payer pour continuer à l'utiliser après cette période.

## Phaser 3

Si vous voulez coder _tout_ et en apprendre beaucoup sur l'écosystème JavaScript en le faisant, consultez [Phaser 3](http://phaser.io/) (ou attendez Phaser 4, qui est [en route](https://madmimi.com/p/4f5f0f)).

Phaser est un framework JavaScript léger et puissant pour créer des jeux 2D. Alors que Phaser 2 était extrêmement bien documenté et bénéficiait d'un excellent soutien communautaire, Phaser 3 est tout le contraire. Il y a une bonne documentation officielle et une série d'exemples (sans beaucoup de contexte autour d'eux, il faut le dire), et une quantité désespérément faible de tutoriels.

Attendez-vous à tout construire vous-même, mais si vous cherchez un support ES6 ou TypeScript, ou si vous voulez _vraiment_ perfectionner vos compétences en tant que développeur JavaScript, vous pourrez aller loin avec Phaser 3.

Dans un souci d'équité, je devrais mentionner deux autres moteurs de jeux 2D qui m'ont été recommandés depuis que j'ai commencé à écrire sur le sujet : [LÖVE 2D](https://love2d.org/), qui utilise Lua, et [MonoGame](http://www.monogame.net/), qui supporte C#. Je n'ai utilisé aucun d'eux (ni d'autres, comme [PyGame](https://www.pygame.org/)), et je ne peux pas parler de leur utilité, mais ils pourraient valoir le coup d'œil.

Faites-moi savoir quel moteur de jeu 2D vous finissez par utiliser, et pourquoi !

Si vous avez aimé cet article, envisagez de [découvrir mes jeux et livres](https://www.nightpathpub.com/), de [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou de [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** a écrit et travaillé pour des entreprises de jeux vidéo de haut profil et des sites éditoriaux tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer Principal de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](http://www.twitter.com/sominator).