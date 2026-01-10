---
title: Comment inspecter Node.js avec Grunt-SWATCH (!watch) et Fiveo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-10T13:59:00.000Z'
originalURL: https://freecodecamp.org/news/watch-sockets-with-this-grunt-plugin
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/DSC_0698-Custom-1--1-.jpg
tags:
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: Comment inspecter Node.js avec Grunt-SWATCH (!watch) et Fiveo
seo_desc: 'By Will

  I know, I know... the socket in the cover picture isn''t really the type of socket
  we''re talking about in this post, but I''ve been preoccupied lately with the idea
  of building a new workstation and the ThreadRipper is a monster! I mean it migh...'
---

Par Will

Je sais, je sais... la prise dans l'image de couverture n'est pas vraiment le type de socket dont nous parlons dans cet article, mais j'ai été préoccupé récemment par l'idée de construire une nouvelle station de travail et le [ThreadRipper](https://www.amd.com/en/products/ryzen-threadripper) est un monstre ! Je veux dire qu'il pourrait bien être la solution pour ne jamais avoir l'impression que mon ordinateur n'est jamais assez rapide, peu importe ce que je mets à niveau (en ce moment, c'est un processeur Intel I7 8ème génération).

Chaque bureau/station de travail que j'ai utilisée au fil des ans (il y en avait un) a toujours laissé beaucoup à désirer. Attendre que votre ordinateur CALCULE, c'est nul ! Les bugs d'écran, les indicateurs de progression sans fin, le temps de latence et autres choses du genre nuisent vraiment à la productivité et au flux de travail.

Bref, passons au sujet et éloignons-nous de...

![Tangent](https://res.cloudinary.com/june07/image/upload/c_scale,w_300/v1566505264/june07/1280px-Tangent_to_a_curve.svg.png)

## Piratage de NodeBB (Forum Node.js)

Comme je l'ai écrit récemment, mon temps de piratage ces derniers temps a été consacré au logiciel de forum NodeBB. Le processus de construction mis en place par les développeurs de NodeBB repose sur l'exécuteur de tâches Grunt, qui lui-même est également construit avec Node.js. C'est génial quand on peut travailler dans un écosystème construit principalement sur les frameworks que l'on préfère le plus (par exemple Node.js ❤️).

Cependant, lorsqu'il s'agit de débogage, et que vos outils de construction et d'autres couches de logiciels sont tous construits avec Node.js, les choses deviennent parfois un peu délicates. Par exemple, lorsque vous voulez passer le flag `--inspect` à l'exécutable node pour démarrer une session de débogage, avec l'intention de déboguer votre code de plugin, et non les couches au-dessus (Grunt, NodeBB).

Je ne connais aucune option de ligne de commande spécifique à l'interface de ligne de commande Grunt qui puisse être utilisée pour transmettre votre intention de démarrer une session de débogage Node au niveau de la tâche. J'ai essayé plusieurs choses sans succès, mais il restait encore quelques options pour y parvenir :

1. Démarrer Grunt en appelant Node directement, ala `node --inspect /path/to/grunt`
2. Démarrer l'inspecteur Node de manière programmatique en utilisant l'API Inspector encore expérimentale [Inspector API](https://nodejs.org/api/inspector.html)
3. Démarrer l'inspecteur Node après coup en utilisant les signaux Linux, `SIGUSR1` pour être exact.

## Compromis

Bien sûr, chacune de ces solutions présentait ses propres obstacles, et comme pour la plupart des choses, elles incluaient à la fois des aspects positifs et négatifs !

Dans cet article, je vais parler de chacune de ces solutions, en détaillant les problèmes auxquels j'ai été confronté en utilisant chacune d'elles. Nous verrons comment l'utilisation de l'API Inspector a rendu possible le [module NPM fiveo](https://www.npmjs.com/package/fiveo), et comment cet outil rend l'utilisation des signaux Linux avec Node.js encore plus puissante. Et enfin, je montrerai comment, dans le scénario présenté ici, l'option #3 s'est avérée être la meilleure solution. Et comment le choix de l'option #3 a servi de catalyseur pour écrire le plugin grunt-swatch, ce que ce plugin fait actuellement, et ce qu'il pourrait faire avec un peu plus de travail.

# 1. Le flag Inspect `--inspect`

Cette commande fonctionne parfaitement bien pour démarrer le débogueur :

`node --inspect /home/batman/.nvm/versions/node/v10.16.0/bin/grunt`

et grunt continuera à faire son travail, qui est d'effectuer une série d'étapes de construction avant de démarrer réellement le serveur NodeBB. Pourtant, notez le fait important que le démarrage de ce processus Node initial en appelant node avec `--inspect` va présenter ses propres défis lorsque Grunt lancera des processus entièrement nouveaux.

Heureusement, lorsque des processus enfants node sont démarrés et que le processus parent a été appelé avec le flag inspect défini, les enfants hériteront de ce paramètre. Mais c'est pour cette même raison que si vous appelez node avec `--inspect` comme nous l'avons fait, vous êtes confronté à ces jolis messages ? qui vous fixent dans la console :

`failed: address already in use`

![Image](https://res.cloudinary.com/june07/image/upload/v1566264160/june07/Capture-gruntInspectListening.png)

Ces messages `failed: address already in use` se produisent parce que l'inspecteur, qui est un serveur de socket, a déjà été démarré sur le processus parent qui, dans notre cas, est Grunt. Ainsi, lorsque les enfants démarrent avec le flag `--inspect` hérité, dont les arguments par défaut sont définis sur `localhost:9229`, Node essaie de démarrer le serveur de socket de l'inspecteur (nous l'appellerons le "_processus d'inspection_" à partir de maintenant) en utilisant le port par défaut 9229.

Une solution de contournement pour cela serait de changer notre commande initiale en :
`node --inspect=0 /home/batman/.nvm/versions/node/v10.16.0/bin/grunt`

Le **"=0"** fait en sorte que le processus d'inspection choisisse un port aléatoire, comme vous pouvez le voir, les ports 39380 et 46704 ont été choisis.

![Ports aléatoires de l'inspecteur](https://res.cloudinary.com/june07/image/upload/v1566264160/june07/Capture-gruntInspectListening2.png)

Ce qui est génial, car maintenant nous avons deux processus d'inspection en cours d'exécution ! La partie qui n'est pas si géniale est que nous ne nous soucions pas de l'un ou de l'autre... pour l'instant.

## Configuration de la construction de NodeBB

Je ne peux pas expliquer complètement le **POURQUOI** du [flux Grunt](https://github.com/NodeBB/NodeBB/blob/master/Gruntfile.js#L208-L216) qui constitue le Gruntfile de NodeBB :

![Extrait de NodeBB Gruntfile.js](https://res.cloudinary.com/june07/image/upload/v1566266263/june07/Capture-GruntfileNodeBB.png)

Mais je peux dire que **CE QU'**il fait est essentiellement de bifurquer une séquence d'initialisation qui prend en charge la construction du css, des fichiers de langue, des modèles, la construction/le regroupement de JavaScript, etc... et ensuite un deuxième processus est bifurqué pour démarrer réellement le serveur NodeBB avec les actifs prêts et bons à aller.

En allant plus loin, chaque fois qu'un changement est détecté grâce au processus de surveillance ([grunt-contrib-watch](https://www.npmjs.com/package/grunt-contrib-watch)), le processus NodeBB actuel est tué et un nouveau est démarré. Et avec ce nouveau processus vient... exactement, un nouveau port de débogage aléatoire va être généré à chaque cycle.

Ce qui complique à nouveau nos efforts de débogage et soulève quelques questions.

* Comment garder une trace de tous ces ports d'inspecteur aléatoires ?
* De plus, comme nous travaillons sur un serveur distant, comment gérer le transfert de port ?
* Nous soucions-nous vraiment des sessions d'inspecteur intermédiaires ?

Pendant que nous réfléchissons ? à ces questions, bifurquons-nous pour...

# 2. Utiliser l'API Inspector de Node

Cela nécessite une approche plus "invasive" lorsqu'il s'agit de notre désir initial de déboguer NOTRE propre code. Cette option nécessite l'inclusion du module inspector, ce qui en soi n'est pas un gros problème. Nous nécessitons du code tout le temps et le module inspector est un module principal de Node.js, et non un morceau de code tiers.

Mais, pour que ce module soit vraiment utile, du code supplémentaire doit être écrit et ajouté à notre base de code.

```node.js
const inspector = require('inspector')
```

Pour être tout à fait...

*éloigné pour pirater un autre code...*

## La nuit dernière !

Alors, hier soir, pendant que j'écrivais ceci, j'ai commencé à écrire que, pour être tout à fait honnête, je n'avais pas donné au module inspector beaucoup de regard avant. Et en le faisant dans l'effort d'écrire cet article de la manière la plus informée possible, j'ai été envoyé dans un peu de terrier de lapin.

L'un d'eux, dont je suis sorti après avoir écrit une petite bibliothèque qui ajoute un peu de sucre sur le module inspector principal, qui, comme il s'avère, est assez cool. Maintenant, après avoir écrit ladite petite bibliothèque, je recommanderais que, au lieu de nécessiter le module inspector, on serait mieux de utiliser [fiveo](https://www.npmjs.com/package/fiveo) qui, à son tour, fait cela pour vous, tout en ajoutant quelques fonctionnalités sympas comme utiliser un port autre que 9229 un peu comme [ce problème GitHub](https://github.com/nodejs/node/issues/16872) en parle.

![Démonstration de Fiveo](https://i.imgur.com/Lad67se.gif)

Néanmoins, vous n'aimerez peut-être pas ma petite bibliothèque ?, et vous n'êtes peut-être pas intéressé à écrire la vôtre. Le fait que l'utilisation de l'API inspector nécessite l'ajout de code supplémentaire à votre propre code existe toujours. Et cela pourrait être un facteur qui rend cette deuxième option un mauvais choix pour votre projet. Ce qui nous amène à la troisième et dernière option...

# 3. `SIGUSR1`... Attendez, je veux dire `SIGUSR2` !

Donc, finalement, la meilleure solution que j'ai trouvée a été d'utiliser les signaux UNIX/Linux [signaux](https://manpages.ubuntu.com/manpages/bionic/en/man7/signal.7.html). C'est un lien vers la page de manuel qui vous donne un aperçu de ce que sont exactement les signaux. En bref, les signaux peuvent changer le comportement des processus qui les reçoivent. *Notez que les signaux ne sont pas pris en charge sur Windows.* Et d'après la documentation officielle de Node :

Node.js commencera également à écouter les messages de débogage s'il reçoit un signal SIGUSR1. (SIGUSR1 n'est pas disponible sur Windows.)

## Le Plan

L'idée générale est que nous pouvons livrer le signal SIGUSR1 au processus Node spécifique à notre code au moment où nous en avons besoin, et pas avant, éliminant ainsi tout le bruit dont nous ne nous soucions pas. Du bruit comme ce que NodeBB fait pendant la phase d'init (rappelez-vous qu'il bifurque un tas de choses), ou ce que le code Grunt fait, etc.

Le point où nous sommes prêts à démarrer le débogueur est le point après que Grunt ait effectué ses tâches d'init, démarre le serveur NodeBB, et que le forum puisse être atteint via le port sur lequel il est configuré pour fonctionner `tcp/45670`. À ce moment-là, nous devons déterminer l'identifiant du processus sur lequel NodeBB écoute, car nous avons besoin d'un identifiant de processus afin de livrer notre signal à l'endroit approprié. Upon receiving the `SIGUSR1`, Node will start the inspector process and we can begin debugging!

What we just described in the preceeding paragraph is exactly what our Grunt plugin **grunt-swatch** does. It's similar to _grunt-contrib-watch_ in that it continuously watches for changes in your environment, the difference is in that **grunt-swatch** doesn't watch the filesystem but rather the network, thus the name, derived from _socket watch_.

grunt-contrib-watch

Run predefined tasks whenever watched file patterns are added, changed or deleted

One should be able to write other "actions" for the plugin, however I've only written the nim (aptly named but also a callback to [NiM](https://june07.com/nim)) action [nim.js](https://github.com/june07/grunt-swatch/blob/master/nim.js):

![Code for nim action showing SIGUSR1](https://res.cloudinary.com/june07/image/upload/v1566414249/june07/Capture-nimAction.png)

You can see that it's rather simple in what it does, but exactly what we need.  It uses the Linux `kill` command (also [an entertaining Sci-Fi](https://en.wikipedia.org/wiki/Kill_Command) by the way!) to send the `SIGUSR1` signal to our _swatched_ process. As you can see the `close()` function currently doesn't do anything and that's because prior to writing [fiveo](https://www.npmjs.com/package/fiveo), there was no way to close the Node inspector via the signal method. However with fiveo included, we have access to `SIGUSR2` which can close the inspector process... leaving things a bit more tidy ?.

![Code for nim action showing SIGUSR2](https://res.cloudinary.com/june07/image/upload/v1566497159/june07/Capture-nimActionSIGUSR2.png)

And here is the output where you can see from the `swatch:nim` log output, that the nim action is actually closing the Node inspector socket that was previously opened. In the screenshot below you can see the complete open/close cycle of this websocket: `ws://localhost:9230/b26fc131-af5e-4943-b911-a25b4261e43c`

![Log for nim action showing SIGUSR2](https://res.cloudinary.com/june07/image/upload/v1566497343/june07/Capture-nimActionSIGUSR2-output.png)

Grunt with my grunt-swatch task loaded and configured appropriately will ensure that during my development process, the inspector will intelligently be stopped and started when I need it to.

```node.js
grunt.loadNpmTasks('grunt-swatch')

```

Further [NiM](https://june07.com/nim) will ensure that DevTools is always right where I need it, opened to the correct inspector websocket and ready to go.

![NiM Popup Screenshot](https://res.cloudinary.com/june07/image/upload/c_scale,w_300/v1566567468/june07/CaptureNiM.png)

And there we have it. By using grunt-swatch, fiveo, along with [NiM](https://june07.com/nim) the [Chromium Extension](http://june07.com/nim-browser-compatability), our NodeBB plugin development workflow is greatly improved! I certainly don't miss the manual process of running this command over, and over, ? and over again:

```bash
pid=`netstat -lnp|grep 45670|awk 'BEGIN {FS=" "}{print $7}'|cut -f1 -d"/"'`
kill -SIGUSR1 $pid

```

Some next steps could be to devise a method of communicating to the debugee process in order to change the debugger port dynamically. To be able to set the debug port from the Grunt config and in essence force the Node application to open a debugger on a preconfigured (in development, post runtime) port would be ideal!

# Conclusion

I hope you found this post helpful. Here are the relevant links to stuff:

* fiveo - NPM [https://www.npmjs.com/package/fiveo](https://www.npmjs.com/package/fiveo), GitHub [https://github.com/june07/fiveo](https://github.com/june07/fiveo)
* grunt-swatch - NPM [https://www.npmjs.com/package/grunt-swatch](https://www.npmjs.com/package/grunt-swatch), GitHub [https://github.com/june07/grunt-swatch](https://github.com/june07/grunt-swatch)
* NiM - Web Store [https://june07.com/nim](https://june07.com/nim), GitHub [https://github.com/june07/NiM](https://github.com/june07/NiM)