---
title: Comment construire un Hackintosh pour coder
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-30T08:55:44.000Z'
originalURL: https://freecodecamp.org/news/build-a-hackintosh-for-coding-560bcdd3446d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FYqYWh0SOJVBpuZUKDBtAg.jpeg
tags:
- name: Apple
  slug: apple
- name: coding
  slug: coding
- name: hackintosh
  slug: hackintosh
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire un Hackintosh pour coder
seo_desc: 'By Simon Waters

  Let’s talk about Hackintosh-ing — the installation of Mac OS X on PC hardware.

  If you want a Mac-compatible computer, but don’t want to shell out thousands of
  dollars, a Hackintosh can help you code for iOS without buying a Mac.

  So wi...'
---

Par Simon Waters

Parlons de [Hackintosh-ing](https://en.wikipedia.org/wiki/OSx86) — l'installation de Mac OS X sur du matériel PC.

Si vous voulez un ordinateur compatible Mac, mais que vous ne voulez pas dépenser des milliers de dollars, un Hackintosh peut vous aider à coder pour iOS sans acheter un Mac.

Alors sans plus tarder, voici un aperçu rapide de la construction d'un Hackintosh, de ses avantages et des risques auxquels vous devez faire attention.

> _Le HP Elitebook 8470p [#hackintosh](https://twitter.com/hashtag/hackintosh?src=hash) est maintenant construit. Temps de continuer avec [@FreeCodeCamp](https://twitter.com/FreeCodeCamp) -ing, maintenant que je suis mobile [pic.twitter.com/w1psj9Gkud](https://t.co/w1psj9Gkud)_

> _— Simon Waters (@developersimon) [12 juin 2016](https://twitter.com/developersimon/status/742047965309734912)_

#### Qu'est-ce qu'un « Hackintosh » ?

Depuis plusieurs années, les Mac d'Apple sont équipés de processeurs Intel, les mêmes que ceux trouvés dans un PC. En fait, un grand nombre de composants matériels sont similaires sur PC et Mac, à part le boîtier en aluminium brillant.

Et certaines personnes intelligentes ont trouvé un moyen d'installer Mac OS X sur du matériel PC standard, le trompant ainsi pour qu'il pense être un vrai Mac.

Le principal avantage est, bien sûr, le prix. Construire votre propre Hackintosh à partir d'une liste de [composants pré-vérifiés connus pour être compatibles](http://www.tonymacx86.com/buyersguide/june/2016) vous coûtera considérablement moins cher qu'un vrai Mac.

L'inconvénient de tout cela est que construire un Hackintosh n'est pas pour les âmes sensibles — cela demande quelques recherches et quelques connaissances en assemblage de PC, ainsi qu'une part de tâtonnements pour obtenir un système entièrement fonctionnel.

Heureusement pour nous, il existe de nombreuses ressources en ligne pour aider à construire un Hackintosh.

Mon préféré est [www.tonymacx86.com](http://www.tonymacx86.com/), où vous trouverez des guides d'achat de matériel. Il présente également des outils d'installation pratiques tels que [Unibeast](http://www.tonymacx86.com/resources/unibeast-6-2-0.314/) et [Multibeast](http://www.tonymacx86.com/resources/multibeast-el-capitan-8-2-3.319/), qui créent pratiquement un Hackintosh pour vous si vous avez le bon matériel.

#### Comment commencer ?

Votre meilleur pari est de vous rendre sur [ce post pour débutants](http://www.tonymacx86.com/threads/im-new-to-everything-where-do-i-start.104542/) et de commencer à lire pour vous familiariser avec tout cela.

En résumé, vous commencez par vous procurer la dernière version de Mac OS X. [Ce guide vous aidera](http://www.tonymacx86.com/threads/simplest-mac-os-x-installation-guide.60255/).

Vous utilisez ensuite Unibeast pour créer un installateur USB de Mac OS X, qui démarrera sur un PC. Une fois que vous démarrez avec cette clé USB, vous pouvez installer Mac OS sur un disque dur de votre choix.

La dernière étape consiste à utiliser Multibeast, qui vous permet de personnaliser votre installation, en installant des pilotes Mac personnalisés (connus sous le nom de « kexts » — extensions de noyau). Ceux-ci communiquent avec tout votre matériel et s'assurent qu'il est tous reconnu comme des composants Mac « officiels ». Il vous permet également de démarrer dans Mac OS X sans avoir besoin de la clé USB créée précédemment, vous offrant un système Mac autonome.

#### Quels sont les avantages ?

Le principal avantage d'utiliser un Hackintosh est un bien meilleur rapport coût/performance par rapport à un vrai Mac. Vous pouvez économiser mille dollars ou plus.

Parce que vous pouvez utiliser du matériel standard, vous pouvez en théorie construire un ordinateur compatible Mac plus puissant que n'importe quel Mac vendu par Apple.

Vous avez également la chance d'utiliser Mac OS X, qui est bien sûr un système d'exploitation bien supérieur à Windows. (Cue la guerre des flammes).

Enfin, vous avez accès à XCode pour le développement. Vous pouvez créer un identifiant Apple comme d'habitude et l'utiliser pour publier vos applications sur l'App Store.

#### Quels sont les pièges ?

La mise à jour vers la prochaine version de Mac OS X comporte certains risques. Vous pouvez principalement atténuer ces risques en utilisant le chargeur de démarrage Clover, qui conserve tous vos fichiers Hackintosh personnalisés dans une zone séparée de votre disque dur, appelée partition EFI. Cette partition ne sera pas écrasée par une mise à jour du système d'exploitation.

Vous ne réussirez peut-être pas à tout faire fonctionner correctement du premier coup, vous devez donc passer un peu de temps à chercher des codes d'erreur sur Google pour découvrir ce qui ne va pas. Il existe cependant très peu de problèmes pour lesquels il n'existe pas de solution pré-découverte.

#### Puis-je transformer mon ordinateur portable en Hackintosh ?

Oui, vous pouvez ! C'est un peu plus délicat, car vous êtes beaucoup plus limité en options de personnalisation matérielle que vous ne le seriez avec un ordinateur de bureau.

Soit ça marche, soit ça ne marche pas. Votre meilleur pari est de simplement chercher sur Google « modèle d'ordinateur portable » + « Hackintosh » et de voir ce qui apparaît.

J'ai fait mes propres recherches et je peux vous dire que le HP Elitebook 8470p fonctionne parfaitement, une fois que vous avez remplacé la carte WiFi par une carte à 2 $ de Chine sur eBay. J'ai acheté le mien auprès d'une entreprise britannique de reconditionnement d'ordinateurs portables pour 120 GBP (environ 180–200 USD). C'est la version i5 2,6 Ghz, avec l'écran 14 pouces définition standard. Bien moins cher que de réparer mon Macbook Pro 2008 cassé !

![Image](https://cdn-media-1.freecodecamp.org/images/bUJkrbLH5ozFWTaDD8xQ9o8Lz8h1fBW5jOox)

Comme vous pouvez le voir, il est reconnu comme un Macbook Pro de mi-2012.

#### Quel est le meilleur matériel à utiliser pour un Hackintosh ?

Si vous cherchez à construire un nouvel ordinateur à partir de zéro, rendez-vous sur [www.tonymacx86.com](http://www.tonymacx86.com/) et consultez le dernier guide d'achat (mis à jour mensuellement). Tous les composants que vous choisissez dans cette liste fonctionneront, mais les plus importants sont la carte mère et le CPU. J'ai constaté que la RAM et le stockage font à peine une différence. Avec une carte mère entièrement compatible (celles de Gigabyte fonctionnent bien), vous n'aurez besoin d'aucune carte Ethernet ou WiFi externe, car tout fonctionnera « out-of-the-box ».

Voici la configuration Hackintosh actuelle que j'utilise pour mon ordinateur de bureau :

* Carte mère Gigabyte Z97-SLI
* CPU Intel 4770K @ 3,5 Ghz
* 16 Go de RAM Corsair (2 x 8 Go)
* Carte graphique Gigabyte 760 OC Windforce edition
* SSD de 128 Go pour le système d'exploitation
* Disques durs de 3 To et 1,5 To à 7200 tr/min pour le stockage

Le SSD fonctionne très bien. Je peux démarrer mon bureau en environ 10–15 secondes.

À l'époque où j'ai commencé à m'intéresser aux Hackintosh vers 2009–10, j'utilisais une ancienne Asus P5K avec un processeur Core 2 Quad Q6600 comme Mac Pro, pour compléter mon vrai Macbook Pro de début 2008.

#### Combien ça coûte ?

Cela dépend entièrement des composants que vous achetez, bien sûr, mais vous pouvez vous attendre à payer bien moins cher qu'un vrai Mac. Surtout si, comme moi, vous avez déjà une gamme de pièces PC qui traînent (moniteur, clavier, souris, boîtier, disques durs, etc.).

Vous n'avez pas vraiment besoin d'investir dans une carte graphique sophistiquée. L'Intel HD4000 intégré qui accompagne les CPU Core est compatible.

Ma configuration de bureau a été mise à niveau l'année dernière pour environ 100 £ (carte mère), 165 £ (CPU) et 90 £ (RAM). Je possédais déjà le reste des composants.

#### À quoi puis-je utiliser mon Hackintosh ?

À tout ce pour quoi vous utiliseriez un vrai Mac. J'ai tendance à utiliser le mien pour des tâches quotidiennes. Je l'utilise également pour coder mon jeu vidéo dans Unreal Engine, qui est inspiré du jeu vidéo des années 1980 Spindizzy. Le principal avantage est que je peux également exporter mon jeu vers iOS, car XCode est requis pour le développement iOS.

#### Et Windows ?

La beauté d'un Hackintosh de bureau est que vous pouvez (avec un peu de travail) démarrer en double boot Mac OS X et Windows à partir du même disque dur. Cependant, avant d'essayer cela, il est utile de noter que pour éviter tout futur mal de tête, vous devriez vraiment envisager d'utiliser un disque dur séparé pour chaque système d'exploitation. Cela est dû à certaines particularités techniques avec les chargeurs de démarrage qui sont écrasés une fois que vous installez Windows. Recherchez « Dual Boot Hackintoshes » sur Google pour plus d'informations.

#### Prochaines étapes

Rendez-vous sur [tonymacx86.com](http://www.tonymacx86.com/) et commencez vos recherches. Du point de vue de l'expérience utilisateur, une fois que vous êtes opérationnel, il n'y a aucune différence entre un Hackintosh et un vrai Mac, à part la boîte brillante dans laquelle il est livré. En termes de performance, vous en aurez beaucoup plus pour votre argent, et de nos jours, la stabilité est tout aussi bonne qu'un vrai Mac.

Bon Hackintoshing !

_Publié à l'origine sur [simonwaters.co.uk](https://simonwaters.co.uk/build-a-hackintosh-for-ios-coding/) le 30 juin 2016._