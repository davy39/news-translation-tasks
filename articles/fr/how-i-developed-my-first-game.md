---
title: Comment j'ai développé mon premier jeu d'aventure
subtitle: ''
author: Andrea Koutifaris
co_authors: []
series: null
date: '2022-03-09T20:05:24.000Z'
originalURL: https://freecodecamp.org/news/how-i-developed-my-first-game
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/presentazione-new.min.jpg
tags:
- name: Art
  slug: art
- name: C
  slug: c
- name: '#Game Design'
  slug: game-design
- name: Game Development
  slug: game-development
- name: lessons learned
  slug: lessons-learned
- name: technology
  slug: technology
- name: unity
  slug: unity
seo_title: Comment j'ai développé mon premier jeu d'aventure
seo_desc: 'It''s hard to tell exactly when my journey creating Occulto, a point and
  click adventure game, started. But I have a significant date in mind:

  3 May 2018.

  Here''s one thing that got the ball rolling:


  Luigi: Hello Andrea. Sorry to bother you. I would l...'
---

Il est difficile de dire exactement quand mon voyage pour créer Occulto, un jeu d'aventure de type point and click, a commencé. Mais j'ai une date significative en tête :

3 mai 2018.

Voici une chose qui a lancé le projet :

> Luigi : Bonjour Andrea. Désolé de te déranger. J'aimerais apprendre à développer une application. Suis-je fou ?

> Moi (Andrea) : Hmm... Je n'ai pas ton numéro... qui es-tu ?

Lire ces deux messages WhatsApp maintenant me fait sourire. Mais il y a aussi deux autres informations intéressantes :

Premièrement, c'était en mai 2018. Maintenant nous sommes en 2022... 3 ans et quelques mois plus tard, nous avons publié notre toute première démo de jeu. Donc oui, il nous a fallu 3 ans pour sortir une démo.

Mais nous produisons maintenant à un rythme régulier, et dans les premiers mois de 2023, nous sortirons le jeu complet.

Cela dit, si vous prévoyez de développer un jeu vous-même, cela ne vous prendra pas nécessairement 4 ans... et j'ai quelques conseils qui, je l'espère, vous aideront !

Deuxièmement, une application – tout le monde veut créer une application. Avons-nous vraiment besoin d'une autre application ? Et si c'était un jeu à la place ? Ce que je veux dire, c'est qu'un jeu d'aventure est comme un livre, vous l'installez, vous y jouez, vous en profitez et éventuellement vous le désinstallez. Ce n'est pas une autre application qui pollue la mémoire de votre téléphone.

Avant de commencer, permettez-moi de faire un pas en arrière et d'expliquer de quoi parle cet article.

## Ce dont nous parlerons dans cet article

Cet article parle de la façon dont moi (Andrea) et Luigi avons développé *Occulto*, notre premier jeu d'aventure.

Il abordera certains aspects techniques du projet, ainsi que la manière dont nous avons géré sa création et son développement. Je discuterai à la fois des parties psychologiques et pratiques du voyage.

Je fournirai également une comparaison superficielle entre l'utilisation des technologies web (comme WebGL) pour le développement et Unity 2D.

Cet article se compose de :

* Une brève histoire de ma passion pour les jeux d'aventure P&C, et comment j'en suis venu à développer mon propre jeu.

* Une section sur *Occulto*, le jeu que je développe

* Une section technique avec une comparaison entre les technologies web et Unity 2D

* Une section sur ce que j'ai appris tout au long du processus, ainsi que quelques conseils si vous créez votre propre jeu.

## Comment je me suis lancé dans les jeux d'aventure

Il y a de nombreuses années, un bon ami m'a fait découvrir [Machinarium](https://amanita-design.net/games/machinarium.html). Machinarium est l'un des meilleurs jeux d'aventure auxquels j'ai jamais joué.

Après l'avoir terminé, j'ai ressenti le besoin de créer mon propre jeu d'aventure. Ce sentiment n'était pas immédiat, mais il s'est renforcé avec le temps. Finalement, il m'a conduit à trouver Luigi et à être réellement capable de créer mon propre jeu indépendant.

### Première tentative de jeu d'aventure

![Image](https://www.freecodecamp.org/news/content/images/2021/10/newton-scene.jpeg align="left")

Lors de ma première tentative de création d'un jeu, j'ai contacté quelques amis et créé un petit groupe de personnes enthousiastes à l'idée de créer un jeu artistique P&C.

Nous avons réussi à créer un brouillon de la première scène (voir l'illustration ci-dessus). L'idée était de faire tomber une pomme sur la tête de Newton, qui se repose sous l'arbre.

J'ai utilisé le [framework Playn Java](https://github.com/playn/playn) pour écrire en Java et exporter vers Android, iOS et le web. À l'époque, j'étais développeur Java. Playn est toujours un projet actif, il peut valoir la peine de le considérer si vous cherchez un framework de jeu 2D en Java.

Cette première tentative n'a pas duré longtemps. Nous avons dîné tous ensemble, et demandé à deux amis de nous présenter un brouillon de l'histoire du jeu. Et puis je n'ai plus eu de retour des autres et le projet a disparu dans le néant.

### Deuxième tentative

![Image](https://www.freecodecamp.org/news/content/images/2021/10/cover-red-moony.min.jpg align="left")

Lors de ma deuxième tentative, j'ai réussi à créer quatre scènes et un peu de gameplay entre elles. Mais le projet a échoué parce que je n'étais pas prêt à diriger le projet. Vous en lirez plus à ce sujet bientôt.

Ci-dessous, vous pouvez voir une image de l'une des scènes du jeu. Il était prévu d'être une réinterprétation moderne du Petit Chaperon Rouge où les loups n'étaient pas méchants :).

![Image](https://www.freecodecamp.org/news/content/images/2021/10/room.min.jpeg align="left")

## Troisième et dernière tentative de jeu d'aventure : Occulto

Développer *Occulto* est ma troisième tentative de création d'un jeu d'aventure – et j'espère que celle-ci sera couronnée de succès !

![Image](https://www.freecodecamp.org/news/content/images/2021/10/village-editor.min.jpg align="left")

*Éditeur Unity : 1er Village*

### Introduction au jeu

C'est un beau matin, et Eliot, un jeune apprenti mage, se rend au studio de son maître pour une leçon sur les potions magiques. Dès le premier moment, quelque chose ne va pas : pourquoi le maître n'ouvre-t-il pas la porte ?

À l'intérieur du studio, tout est en désordre, et un mot dit à Eliot d'aller à l'église du village. Que se passe-t-il ? Où est le maître ?

![Image](https://www.freecodecamp.org/news/content/images/2021/10/studio.jpg align="left")

*2ème Studio du Maître*

Allez-vous aider Eliot dans son voyage pour trouver son maître et récupérer le puissant livre interdit intitulé "Le livre jamais écrit" qu'une figure maléfique tente de voler ?

La démo se compose de quatre scènes :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/monastery.jpg align="left")

*3ème Monastère*

et un passage secret entre le monastère et le studio privé d'un moine.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/secret-passage.jpg align="left")

*4ème Passage secret*

Ci-dessous, vous pouvez voir la dernière scène de la démo.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/hunckback-studio.jpg align="left")

*5ème Studio privé du moine*

## Technologie utilisée pour construire mon jeu d'aventure

![Image](https://www.freecodecamp.org/news/content/images/2022/03/unity-vs-pixijs.png align="left")

Nous avons développé *Occulto* au début en utilisant [Pixi.JS](https://pixijs.com/) et HTML. Ensuite, plus tard, je suis passé à Unity en utilisant les fonctionnalités 2D qui sont maintenant incluses par défaut dans l'éditeur.

Comme cet article est assez long, je n'entrerai pas dans les détails du code. Mais je fournirai une description des technologies que nous avons utilisées et du processus de création du jeu.

Je prévois d'écrire un deuxième article pour la partie technique.

Nous sommes un groupe de 3 personnes :

* Moi-même, Andrea, le développeur et gestionnaire de projet/technique. Je contribue également à l'histoire et à la conception des énigmes du jeu. Je suis ingénieur logiciel.

* Luigi, le merveilleux designer artistique qui conçoit et dessine les scènes. Il est également responsable de l'histoire du jeu et du gameplay. Si vous aimez les illustrations ci-dessus, alors vous aimez le travail de Luigi :). Il est diplômé en mathématiques.

* Antonio est le designer des musiques et des sons. Il est ingénieur logiciel.

Luigi dessine les scènes en utilisant [Photoshop](https://www.adobe.com/products/photoshop.html) et fait les animations en utilisant [After Effects](https://www.adobe.com/products/aftereffects.html). Ensuite, il exporte tout en images (jpg et png) que j'utilise plus tard pour assembler les scènes.

En outre, Antonio me fournit les sons et la musique pour les scènes. Nous utilisons des fichiers mp3 pour le moment, mais nous prévoyons de passer à [FMOD](https://www.fmod.com/) à l'avenir.

Le jeu utilise des images FHD (1920x1080), et fonctionne également sur des appareils mobiles bas de gamme. Si vous souhaitez exécuter le jeu sur un appareil avec 1 Go de RAM, vous devez réduire le nombre d'images FHD. Si vous chargez en mémoire plus de 50/60 images FHD, le jeu peut planter sur les appareils avec une mémoire insuffisante.

Dans la gestion normale de la mémoire Unity, toute la scène est chargée en mémoire, donc vous devez faire attention à ce que vous ajoutez à la scène.

Une solution simple et classique pour réduire l'empreinte mémoire est d'utiliser des feuilles de sprites pour les animations. La plupart du temps, une animation tiendra dans un sprite de 2048x2048. J'utilise [Texture Packer](https://www.codeandweb.com/texturepacker) pour créer et importer des feuilles de sprites d'animation dans Unity.

En outre, j'utilise [ImageMagick](https://imagemagick.org/index.php) [CLI](https://en.wikipedia.org/wiki/Command-line_interface) pour rogner les images avec un objet à l'intérieur. Mon entrée est un PNG transparent FHD avec un objet à l'intérieur placé dans la bonne position. Ensuite, j'utilise :

```bash
magick mogrify -trim -verbose *.png > trim.txt
```

pour rogner l'image et obtenir la position précise de l'objet.

Enfin, j'ajoute l'image rognée à la scène et la place en utilisant un script que j'ai fait qui mappe les coordonnées à l'intérieur du fichier *trim.txt* aux valeurs x,y de la scène Unity.

En rognant et en utilisant des feuilles de sprites, j'ai résolu tous les problèmes de mémoire. De plus, des images plus petites signifient un temps de chargement plus court lors du chargement d'une scène. Sur les appareils mobiles bon marché, le chargement d'une scène peut prendre environ 5 ou 6 secondes (alors que sur les appareils plus puissants, cela prend moins d'une seconde).

En ce qui concerne les fps et les performances, Unity est bon – donc essentiellement vous n'avez pas à faire quoi que ce soit de spécial. Vous devez simplement éviter les mauvaises conceptions. Et faire attention à la [complexité temporelle](https://en.wikipedia.org/wiki/Time_complexity). Par exemple, évitez de rechercher un élément à chaque tick de la boucle de jeu.

Comme je l'ai mentionné précédemment, je prévois d'écrire un article technique sur la façon dont j'ai développé le jeu en utilisant Unity 2D. Si vous êtes intéressé, suivez-moi ou suivez-nous sur l'un de nos comptes de réseaux sociaux.

### Unity vs WebGL

Même si j'ai utilisé les deux technologies, je ne suis pas un expert (c'est mon premier jeu). Donc ci-dessous je vais simplement lister quelques avantages et inconvénients des deux technologies.

#### Avantages de WebGL

* Facile à porter partout avec [Capacitor](https://capacitorjs.com/) ou [Electron](https://www.electronjs.org/).

* Convivial pour les programmeurs : [PixiJS](https://pixijs.com/) le rend très facile.

* Presque la seule solution fonctionnelle si vous avez besoin d'une version web responsive.

* L'intégration et la livraison continues sur le web sont très faciles, puisque la sortie est un ensemble de fichiers.

* Le développement web est mature, et vous avez accès à des tonnes de bibliothèques, d'utilitaires ainsi qu'à des outils de packaging web, comme [Webpack](https://webpack.js.org/).

* La collaboration est très facile et mature avec Git. Il y a quelque chose à propos de la collaboration dans Unity, que je n'ai pas exploré. Je ne sais pas ce qui se passe si deux personnes travaillent sur la même scène.

#### Inconvénients de WebGL

* Performances légèrement inférieures par rapport aux frameworks plus natifs.

* Soumis aux bugs des WebViews (que vous ne pouvez pas résoudre).

* Peut être difficile pour les programmeurs qui ne connaissent pas le développement web.

* Les WebViews ne semblent pas être prêtes à supporter parfaitement WebGL. Le jeu ne fonctionnait pas bien sur mon Neffos, et qui sait sur quels appareils il avait des problèmes. Peut-être que les WebViews ne sont pas encore prêtes pour le gaming, mais elles sont définitivement prêtes pour le HTML et les applications hybrides.

#### Avantages de Unity

* Éditeur graphique : il est plus facile de visualiser/mettre à jour la scène et d'affiner les réglages.

* Facile et complet : il a presque tout ce dont vous avez besoin.

* Bonne performance : 60 fps même sur les appareils bas de gamme à une résolution de 1920 x 1080.

* Multiplateforme, mais la version WebGL ne fonctionne pas bien sur les téléphones mobiles.

* Beaucoup de jeux indépendants sont faits en utilisant Unity. Si l'équipe Unity introduit un bug, il sera trouvé très rapidement.

#### Inconvénients de Unity

* Éditeur graphique : vous avez besoin d'un éditeur Unity mis à jour et fonctionnel sur chacun des ordinateurs que vous allez utiliser. Avec Linux, ce n'est pas si simple.

* [Licence fermée](https://store.unity.com/compare-plans) mais elle a un niveau gratuit si vous avez gagné jusqu'à 100 000 $ au cours des 12 derniers mois.

* À l'heure actuelle, la version web mobile n'est pas officiellement supportée.

* L'éditeur Unity pour Linux est en version alpha (et j'ai réussi à le faire fonctionner après plusieurs tentatives).

* Pas beaucoup d'informations utiles à ce sujet : la plupart des posts que j'ai lus pour trouver de l'aide sur un sujet particulier étaient de mauvaise qualité ou étaient des vidéos. C'est loin de la qualité de stack overflow. Mais la documentation est bien faite.

Gardez à l'esprit que cette section n'est pas destinée à être une comparaison exhaustive entre Unity 3D et les frameworks WebGl. Selon votre cible, une technologie peut être meilleure que l'autre.

Cela dit, même si je suis un développeur web, je dois admettre que Unity est génial pour développer des jeux 2D (et je suppose aussi des jeux 3D).

## Ce que j'ai appris en construisant Occulto

![Image](https://www.freecodecamp.org/news/content/images/2022/03/1_zGuG4nFo8O4e0WMoNWVbMA.jpeg align="left")

### Quelqu'un doit diriger le projet

C'est ma première prise de conscience : si c'est vous qui proposez un projet à d'autres (un jeu, une application ou autre), ils supposeront que vous dirigerez le projet.

À l'époque, je pensais que j'étais juste un programmeur, et je n'agissais pas comme un leader de projet. Cela ne fonctionnera pas si quelqu'un ne suit pas activement chaque personne dans le projet.

### Avoir la bonne attitude

Il est important d'avoir la bonne attitude envers les personnes qui participent au projet. Vous devez également comprendre si elles peuvent être productives.

Dans ce contexte, "productif" n'a pas la même signification que celle qu'il a au travail. Productif signifie "réellement capable de produire". Au travail, cela signifie combien vous produisez et à quel point votre production est bonne.

Avant de continuer, permettez-moi de vous raconter une histoire :

Avant de me lancer dans le développement du jeu *Occulto*, j'ai décidé d'aider un gars à développer l'interface pour son jeu de société. Je l'ai fait parce que je pensais que le jeu qu'il avait inventé était un bon jeu qui avait quelques parties brillantes.

Dans ce cas, j'étais le développeur, et il dirigeait le projet (être l'inventeur d'un jeu n'implique malheureusement pas que vous soyez également bon en tant que leader de projet).

Au début, tout allait bien, et j'ai apprécié développer le jeu. En outre, j'apprenais React, que j'ai utilisé comme framework pour construire l'application du jeu. (C'est un jeu de société, pas un jeu classique, donc React était un bon choix, et il avait aussi beaucoup de pages, pas seulement la page de jeu).

Ensuite, les choses ont commencé à devenir étranges : il a commencé à demander des délais, à se plaindre des retards dans le développement, et à demander des fonctionnalités que je pensais n'être pas vraiment utiles dans la première version du jeu.

À la fin, cela n'a pas fonctionné et je n'ai pas pu bien travailler avec lui, alors j'ai bloqué toute communication. Rappelez-vous que j'ai travaillé sur son jeu gratuitement, et j'ai même résolu un bug désagréable qui faisait que le côté back-end du jeu cessait de fonctionner.

Alors, pourquoi cette histoire ? Pour vous dire que faire un jeu avec un groupe d'amis est un travail très différent de ce que vous faites au travail. Quelques conseils :

* **Ne poussez pas trop les gens** : si vous faites un jeu pour le plaisir, cela doit être amusant. Motivez les gens et aidez-les. Ils travaillent (comme vous) gratuitement sur un projet auquel ils croient.

* **Ne vous comportez pas comme un patron** : même si vous dirigez et suivez chaque étape du jeu, les gens devraient vous considérer davantage comme un gestionnaire de projet/responsable d'équipe que comme un patron.

### Travaillez pendant votre temps libre

Être capable d'être "productif" s'applique également à vous. Êtes-vous capable de travailler pendant votre temps libre sur le jeu ? Pouvez-vous fournir une production régulière, sans longues périodes éloignées du projet ?

C'est le premier obstacle que j'ai rencontré lors de mes tentatives précédentes. Je n'étais pas capable de fournir une production constante et ponctuelle, et les gens pensaient que le projet s'effondrait.

Dans ce cas, en tant que programmeur, il est important d'intégrer la production des autres membres de votre équipe (images, animations et sons) dès que possible. Les gens seront plus engagés s'ils voient leur travail rapidement intégré dans le jeu. De plus, plus vous intégrez rapidement le travail des autres, plus vous trouverez et résoudrez rapidement les problèmes.

### Éliminez autant d'obstacles que possible

Pour travailler pendant votre temps libre, vous devez réduire ou éliminer tous les obstacles. Ceux-ci peuvent être physiques (ordinateur lent, écran trop petit, ...) ou psychologiques. Ces derniers sont les plus subtils. Je vais essayer d'en lister quelques-uns :

**Se sentir coupable de ne pas travailler** : c'est difficile, et je pense que c'est l'une des principales raisons pour abandonner. Vous devez aimer travailler sur votre projet. Donc les délais, pousser les autres à produire plus, menacer (comme "Si vous ne travaillez pas assez, vous êtes dehors") ne fonctionnent PAS.

Il est préférable de motiver les gens et de les aider à comprendre ce qui les bloque (ou vous bloque) pour produire quelque chose.

**Obstacles qui retardent le moment où vous pouvez réellement travailler** : vous pouvez penser quelque chose comme "J'aimerais finir cette chose que j'ai commencée, je pense que je peux la compléter en 10 minutes." Ensuite, vous pensez : "Mais l'ordinateur est lent et il mettra une éternité à démarrer... peut-être demain, maintenant je vais juste surfer sur Instagram".

Il est important que lorsque vous pensez pouvoir travailler un peu sur le jeu, vous puissiez le faire sans aucun retard ou obstacle.

**Trop fatigué pour travailler sur le jeu** : en effet, vous ne devez pas en faire trop. Il est important de trouver un équilibre entre le temps de travail et le temps de repos. Mais il est également important d'éviter les longues périodes sans travailler sur le jeu.

J'ai remarqué que de petites actions peuvent aider : par exemple, pour moi, il suffit de démarrer l'éditeur Unity pour augmenter les chances que je travaille réellement sur le jeu.

**Partagez vos résultats avec les autres** : même si les personnes non techniques ne comprendront peut-être pas pleinement ce que vous faites (et vice-versa), il est satisfaisant d'expliquer que vous avez résolu un problème de performance, ou que vous avez réduit la taille du bundle, par exemple.

En fait, dans les méthodologies agiles, dire ce que vous avez fait et ce que vous allez faire est l'un des points principaux.

**Persévérez**. Tout ne sera pas facile. Vous devrez persévérer. Même si vous faites probablement un jeu par passion, cela nécessite tout de même beaucoup de travail et parfois vous devez persévérer et surmonter les problèmes/blocages. Vous le faites probablement tout le temps au travail, vous pouvez le faire aussi pour votre jeu.

**Chaque moment n'est pas un moment de plaisir**. Imaginez quand j'ai découvert que la démo, presque prête à être publiée, ne fonctionnait pas sur certains appareils mobiles et que je devais tout réécrire dans Unity. J'ai vraiment passé un mauvais week-end.

Mais ensuite, j'ai réussi à changer mon attitude, à commencer avec Unity, et à retrouver du plaisir à travailler sur le jeu.

Heureusement, Luigi, mon partenaire dans le jeu, l'a compris et a accepté que nous devions reporter la date de sortie de la démo du jeu. Bien qu'il ait fallu beaucoup de temps pour écrire la démo (2 ans, si vous comptez à partir du premier commit), il m'a fallu 3 mois pour la réécrire.

### Concentrez-vous sur le développement du jeu

Il est extrêmement important de se concentrer sur la création du jeu, et non sur le framework pour le jeu.

En tant que programmeur, vous voudrez probablement écrire plus de code que nécessaire et utiliser votre langage préféré. Choisissez un framework en fonction de vos besoins (multiplateforme ? 2D ou 3D ? ...) et essayez de développer un niveau simple pour comprendre si vous avez fait les bons choix.

Lorsque vous commencez, vous n'aurez pas nécessairement une vue claire des frameworks/technologies possibles disponibles pour construire un jeu – et il y en a beaucoup. De plus, vous serez biaisé envers certains langages/fonctionnalités.

À ce sujet, je peux vous raconter 2 erreurs que j'ai commises :

J'ai d'abord utilisé PixiJS et les technologies HTML. Contrairement à ce que vous pourriez penser, j'ai pu atteindre 60 fps avec une résolution FHD (1920x1080) même sur des appareils mobiles de performance moyenne.

C'est parce que la plupart du travail est fait par WebGL. Mais à un certain moment, le jeu a commencé à scintiller sur mon ancien téléphone mobile (Neffos X1 Max) lorsqu'il était porté sur une application mobile en utilisant Capacitor (webview). Mais il fonctionnait bien sur le navigateur et sur les autres téléphones que j'avais. Même sur mon Motorola Moto G de première génération (appareil bas de gamme de 2013).

J'aurais dû tester plus tôt sur mobile (pas seulement avec le navigateur). De plus, le jeu n'était pas fluide sur mon appareil bas de gamme Moto G (il tournait tout de même près de 30 fps).

J'ai décidé que je voulais que mon jeu fonctionne de manière fluide même sur les appareils bas de gamme, alors je suis passé à Unity 2D. Unity est utilisé par beaucoup de développeurs de jeux indépendants, et C# est assez facile. Je n'ai pas essayé Unreal Engine, parce que je suis trop rouillé en C++. Maintenant, il fonctionne de manière fluide également sur mon Moto G (60 FPS).

La deuxième chose qui était presque une erreur est que j'ai développé une bibliothèque pour trouver le chemin le plus court sur des zones polygonales avec des trous polygonaux. [Ici](https://github.com/Kouty/shortest-path-polygon-area) vous pouvez trouver le code JS (je l'ai porté en C#, mais je ne l'ai pas encore publié sur GitHub).

Il m'a fallu 3 tentatives pour le faire fonctionner correctement, et beaucoup de temps. Heureusement, au moment où j'ai commencé à développer *Occulto*, la bibliothèque était prête et fonctionnelle. Maintenant, je peux simplement dessiner la zone praticable et faire bouger le personnage principal à l'intérieur, en évitant les obstacles (trous polygonaux).

Le fait est que disposer d'un algorithme pour déplacer des objets dans une zone praticable n'est pas strictement nécessaire, et il est préférable de se concentrer sur la création réelle du jeu. D'autres jeux P&C n'utilisent pas cette fonctionnalité, ils déplacent simplement les personnages le long de chemins prédéfinis.

Donc, avant de vous lancer dans quelque chose qui n'est pas strictement nécessaire pour le jeu, voyez si vous pouvez trouver quelque chose déjà implémenté ou si cela en vaut vraiment la peine.

### Publiez une version à une scène du jeu

Après avoir choisi le bon framework, prenez une scène, et développez le jeu entier qui consistera en une scène plus un menu et tous les composants UI qui sont inter-scènes. Il est important d'apprendre tout ce dont vous avez besoin et de trouver les problèmes dès que possible.

De plus, soumettez le jeu pour des tests internes (non publics) aux magasins que vous allez utiliser. Oui, faites tout ce qui est nécessaire, du développement à la publication (en privé) du jeu.

Lorsque j'ai publié la démo du jeu sur iOS, une animation ne fonctionnait pas. Elle fonctionnait sur Android, Desktop, et même sur iPhone avec la version de développement. Donc oui, vous devez tester tout dès que possible, même le processus de publication.

J'ai fait l'erreur de d'abord développer toute la démo (quatre scènes, plus menu et quelques autres écrans) pour découvrir que la technologie WebGL n'était pas le bon choix pour mon jeu.

## Notes finales

J'espère que vous avez apprécié la lecture de cet article et que vous y avez trouvé quelques conseils intéressants. Peut-être que j'écrirai un autre article lorsque j'aurai publié le jeu complet, en partageant d'autres informations.

Si vous êtes curieux au sujet du jeu [*Occulto*](https://www.sirioartgames.com/), suivez-nous sur :

* Twitter : [https://twitter.com/SirioArtGames](https://twitter.com/SirioArtGames)

* Instagram : [https://www.instagram.com/sirioartgames](https://www.instagram.com/sirioartgames/)

* Notre site web : [https://www.sirioartgames.com](https://www.sirioartgames.com/)

ou [essayez la démo](http://onelink.to/mxsak4) : [http://onelink.to/occulto](http://onelink.to/occulto) !