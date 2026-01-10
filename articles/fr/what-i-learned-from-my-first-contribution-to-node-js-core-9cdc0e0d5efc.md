---
title: Ce que j'ai appris de ma première contribution au cœur de Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-26T18:44:36.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-my-first-contribution-to-node-js-core-9cdc0e0d5efc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TMcOrpatfD5sTKioEqsMKg.jpeg
tags:
- name: lessons learned
  slug: lessons-learned
- name: Node.js
  slug: nodejs
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Ce que j'ai appris de ma première contribution au cœur de Node.js
seo_desc: 'By Yael Hermon

  A couple of weeks ago my very first PR for Node.js core was merged! A few days later,
  I decided to tweet about it and share how positive this experience was, hoping to
  encourage others to contribute as well.

  Later, Uri Shaked suggested...'
---

Par Yael Hermon

Il y a quelques semaines, ma toute première PR pour le cœur de Node.js a été fusionnée ! Quelques jours plus tard, j'ai décidé d'en tweeter et de partager à quel point cette expérience était positive, espérant encourager les autres à contribuer également.

Plus tard, [Uri Shaked](https://www.freecodecamp.org/news/what-i-learned-from-my-first-contribution-to-node-js-core-9cdc0e0d5efc/undefined) a suggéré que je partage mon expérience dans un court article de blog. Uri a toujours de grandes idées. Merci, Uri !

#### Comment en suis-je arrivé à cette PR ?

Je suis contente que vous ayez posé la question. Laissez-moi commencer par un peu de contexte. J'adore Node.js, et contribuer à celui-ci était en fait sur ma liste de choses à faire depuis très longtemps. Je n'ai jamais eu l'occasion de le faire parce que je me disais toujours que je n'avais pas le temps pour cela, ou que je n'étais peut-être pas assez qualifiée, ou d'autres excuses bidon.

Le rebondissement s'est produit lorsque je travaillais sur une présentation pour une rencontre JavaScript-Israël sur le [V8 Garbage Collector](https://docs.google.com/presentation/d/14CVuylg19RUnNLz525ecSHTyN7upVdF196WNtzhqdoA/edit?usp=sharing). [Benjamin Gruenbaum](https://github.com/benjamingr), un collaborateur du cœur de Node.js, m'a demandé si je voulais qu'il me mette en contact avec des ingénieurs de V8 pour réviser mes diapositives. Euh... évidemment, je voulais.

Il l'a fait, ce qui s'est avéré plutôt génial. Benji m'a également demandé si j'étais intéressée à contribuer au cœur de Node.js. Encore une fois, j'ai dit oui. Plus d'excuses. Les choses sont devenues sérieuses.

#### Configuration de l'environnement

J'ai d'abord dû construire Node.js sur ma machine. C'était surprenamment facile, grâce à la [grande documentation](https://github.com/nodejs/node/blob/master/BUILDING.md) de Node.js. Ensuite, j'ai décidé de m'amuser et de commencer à le déboguer.

Je mentirais si je disais que tout s'est passé sans accroc dès le début. La dernière fois que j'ai travaillé avec C++ remonte à 2012. J'étais rouillée. De plus, à l'époque, j'avais un environnement complètement différent de celui que j'ai maintenant. J'avais un PC Windows avec Visual Studio, tandis que maintenant j'utilise VSCode sur un Mac.

J'adore VSCode, alors je voulais configurer VSCode pour ce projet aussi. J'ai rapidement trouvé une [extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) et j'ai configuré les choses pour qu'elles fonctionnent. Pour ma configuration de débogage, j'ai fini par configurer un débogueur de nœud et un débogueur lldb pour attacher au processus Node. Cela a très bien fonctionné.

#### Travailler sur un problème réel !

Donc, Benji m'a mise en contact avec [Anna](https://github.com/addaleax), qui est la collaboratrice du cœur de Node.js qui a implémenté les [worker_threads](https://nodejs.org/api/worker_threads.html). Benji m'a également dirigé vers ce [problème](https://github.com/nodejs/node/issues/24636). J'ai regardé le problème et j'ai essayé de le reproduire avec aussi peu de code que possible, juste pour éliminer le bruit.

J'ai eu du mal à créer un cas de test qui reproduisait le problème, car il était causé par une condition de course. Le code qui échouait lors de l'exécution à l'intérieur de Node.js ne échouait pas dans mon environnement de test. Finalement, j'ai trouvé quelque chose qui échouait à toutes mes exécutions. Bien que cela puisse ne pas échouer sur toutes les machines, ou à chaque fois, Anna a confirmé que c'était suffisamment bon. Ensuite, j'ai commencé à le déboguer pour voir ce qui se passait réellement.

Si vous n'avez jamais entendu parler des 'worker threads', c'est probablement parce qu'ils sont assez nouveaux et sont actuellement dans un état expérimental. Les workers vous permettent de créer plusieurs environnements s'exécutant sur des threads indépendants. Ils sont utiles pour effectuer des opérations JavaScript intensives en CPU, sans bloquer le thread principal.

Le thread principal et le thread worker peuvent communiquer entre eux via un canal de messages entre eux. En plus de ce canal de messages, il existe un autre canal de messages où les messages internes sont envoyés, tels que stdout du worker. Lorsque vous `console.log` à l'intérieur du worker, il arrive au thread principal via ce canal de messages interne et le thread principal le gère en le poussant vers son flux stdout.

Le problème était que nous appelions la fonction `kDispose` dans la classe JS worker avant d'attendre que tous les messages du stdio du worker soient traités par le thread principal via le port de messages interne. Donc, lorsque le thread worker se terminait, nous perdions les références pour les flux stdio côté parent, et un message au parent pouvait éventuellement arriver après cela.

Au début, j'ai essayé de nombreuses approches différentes pour résoudre ce problème, y compris la définition d'une promesse à résoudre lorsque le port de messages était terminé, l'attente avant la disposition, et le passage de rappels JS à la couche C++.

En discutant avec Anna à ce sujet, j'ai découvert qu'une méthode _drain_ existait pour le MessagePort et qu'elle émettait tous ses messages entrants de manière synchrone. Ainsi, à la fin, tous les messages de celui-ci seraient traités. En fait, _drain_ était déjà appelé pour le MessagePort externe. Comment n'avais-je pas vu cette fonction tout ce temps ? ? J'ai ajouté un appel à drain également sur le MessagePort interne. La correction était aussi simple que cela.

Une chose importante à retenir est — il est tout à fait acceptable d'essayer des approches étranges en cours de route. C'est comme cela qu'on apprend. Et après avoir débogué beaucoup de code worker_threads, je peux dire que je connais maintenant assez bien une partie de sa base de code :)

Benji et Anna ont été si accueillants dès le début. Ce fut une grande expérience. J'ai beaucoup appris d'Anna et du code, qui était très stimulant. Ce n'est définitivement pas quelque chose que je traite habituellement dans mon quotidien.

Je n'ai pas hâte de travailler sur mon prochain problème !