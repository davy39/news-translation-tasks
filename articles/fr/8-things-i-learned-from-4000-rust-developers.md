---
title: Les 8 choses principales que j'ai apprises de 4000 développeurs Rust
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2020-05-24T17:57:05.000Z'
originalURL: https://freecodecamp.org/news/8-things-i-learned-from-4000-rust-developers
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/learn-rust-20-seconds-1.gif
tags:
- name: codespaces
  slug: codespaces
- name: programming languages
  slug: programming-languages
- name: Rust
  slug: rust
- name: Visual Studio Code
  slug: vscode
- name: Web Applications
  slug: web-applications
- name: WebAssembly
  slug: webassembly
seo_title: Les 8 choses principales que j'ai apprises de 4000 développeurs Rust
seo_desc: 'Do you know that most Rust programmers are working on web applications?
  ? Rust is challenging, but also rewarding and great fun! Learn Rust by example,
  or ?open this GitHub repo to get started in VSCode.

  Rust is one of the hottest ? programming langu...'
---

Saviez-vous que la plupart des programmeurs Rust travaillent sur des applications web ? ? Rust est exigeant, mais aussi gratifiant et très amusant ! Apprenez [Rust par l'exemple](https://rust-by-example-ext.com/), ou ? ouvrez [ce dépôt GitHub](https://github.com/second-state/learn-rust-with-github-actions) pour commencer dans VSCode.

Rust est l'un des langages de programmation ? les plus en vogue aujourd'hui. Il est le [langage de programmation le plus apprécié](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/) de StackOverflow depuis les quatre dernières années. Pourtant, il a toujours la réputation d'être le langage de programmation des geeks alpha.

Selon [certaines estimations](https://s3-eu-west-1.amazonaws.com/vm-blog/uploads/2020/04/DE18-SoN-Digital-.pdf), il y a 600 000 développeurs Rust dans le monde, ce qui est un nombre significatif. Mais il est encore éclipsé par les dizaines de millions de développeurs JavaScript, Java et Python.

Qui sont ces développeurs Rust ? À quoi utilisent-ils Rust ? Pourquoi aiment-ils tant Rust ? Et surtout, comment rejoindre leurs rangs et voir par vous-même pourquoi Rust est tant apprécié ? Ne restez pas à la traîne.

Pour répondre à ces questions, la communauté Rust a mené des enquêtes annuelles auprès des développeurs depuis 2016 sur rust-lang.org. Le site a récemment publié les [résultats de l'enquête 2019](https://blog.rust-lang.org/2020/04/17/Rust-survey-2019.html) basés sur les réponses de près de 4000 développeurs Rust. Voici les 8 choses principales que j'ai apprises de cette enquête.

## ??? Rust est pour les programmeurs professionnels

Le langage de programmation Rust n'est pas conçu pour être "[facile à prendre en main](https://www.secondstate.io/articles/a-rusty-hello-world/)". Il est plutôt conçu pour être puissant et sûr en même temps. Il vise à être le langage de productivité des développeurs pour les programmeurs professionnels. Il est exigeant, amusant et gratifiant. Cela se voit dans l'enquête.

Très peu de répondants se considèrent comme des experts en Rust. La plupart des gens évaluent leur expertise en Rust à 7/10 ou moins, malgré le fait que plus de 68 % d'entre eux écrivent du code Rust sur une base hebdomadaire. C'est clairement un langage qui prend du temps à maîtriser et à exceller.

> Environ 37 % des utilisateurs de Rust se sont sentis productifs en Rust en moins d'un mois d'utilisation - ce qui n'est pas très différent du pourcentage de l'année dernière (40 %). Plus de 70 % se sont sentis productifs dans leur première année. Malheureusement, comme l'année dernière, il y a encore une lutte parmi les utilisateurs - 21 % ont indiqué qu'ils ne se sentaient pas encore productifs.

En même temps, lorsqu'on leur demande pourquoi ne pas utiliser Rust sur certains projets, la courbe d'apprentissage est citée comme la deuxième raison la plus courante. La première raison, bien sûr, est la décision de l'entreprise d'utiliser ou non un langage de programmation particulier dans un projet.

## ? La documentation est cruciale pour l'adoption

Comment les développeurs surmontent-ils la courbe d'apprentissage de Rust et tombent-ils amoureux de ce langage ? Eh bien, sans surprise, la plupart des développeurs citent une "meilleure documentation" comme moteur de l'adoption.

Mais fidèle aux "programmeurs professionnels", la documentation Rust la plus recherchée est le contenu de niveau intermédiaire qui aide les développeurs à améliorer leurs compétences et leur productivité en Rust.

Bien que l'enquête soit biaisée envers les développeurs qui connaissaient déjà les bases de Rust, il semble qu'il y ait une soif de connaissances et d'amélioration personnelle dans cette communauté.

## ? Les développeurs ne veulent pas de tomes de texte

La documentation logicielle traditionnelle consiste généralement en des livres et des sites web entiers. Les nouvelles générations de développeurs veulent plus et une meilleure documentation. En tant que langage "nouveau", Rust est déjà à la pointe de l'innovation en matière de documentation des langages de programmation.

Par exemple, le compilateur Rust est un outil auto-documenté. L'une des caractéristiques les plus uniques et appréciées de Rust est son compilateur agressif qui vous aide à garantir la correction et la sécurité avant même que le programme ne s'exécute. Par conséquent, les développeurs Rust peuvent écrire des programmes très performants et sûrs.

Lorsque vous rencontrez une erreur de compilation en Rust, le compilateur vous donne une explication immédiate de l'erreur, ainsi que des suggestions sur la façon de corriger l'erreur en fonction du contexte de votre programme.

[Ce projet de démarrage](https://github.com/second-state/learn-rust-with-github-actions) sur GitHub vous permet de commencer avec le compilateur Rust et le système Cargo sans avoir à installer de chaîne d'outils logiciels. Vous pouvez utiliser l'IDE en ligne VSCode directement avec ce projet.

Les sites web de documentation Rust comme [docs.rs](http://docs.rs) et [Rust par l'exemple](https://doc.rust-lang.org/rust-by-example/) (et son [Édition Étendue](https://rust-by-example-ext.com/)) utilisent le [Rust Playground](https://play.rust-lang.org/) pour exécuter directement du code exemple Rust depuis le navigateur. Ces livres interactifs sont bien meilleurs que du simple texte.

Cependant, comme le révèle l'enquête, les développeurs veulent plus. Les développeurs ont soif de plus de contenu vidéo, par exemple. Nous pouvons nous attendre à plus de vidéos de codage et de diffusions en direct de la communauté bientôt.

## ?? La plupart des gens utilisent Rust pour les applications web, sérieusement !

En tant que langage de niveau système destiné à remplacer C et C++, la plupart des gens supposent que Rust serait utilisé dans la programmation d'infrastructure, telle que les systèmes d'exploitation, les bibliothèques natives et les plateformes d'exécution.

Pourtant, l'enquête montre clairement que, de manière significative, la plupart des développeurs Rust aujourd'hui travaillent sur des backends d'applications web. Pas étonnant que des crates comme [hyper](https://docs.rs/hyper/0.13.5/hyper/), [actix-web](https://github.com/actix/actix-web), et [Rocket](https://rocket.rs/) soient parmi les plus populaires auprès des développeurs Rust.

Pour être sûr, la plupart des développeurs logiciels travaillent sur des applications web. Il n'est pas surprenant que, à mesure que Rust gagne en adoption grand public, les projets Rust reflètent l'industrie logicielle plus large.

Cependant, cela présente des opportunités pour des projets et des outils qui intègrent Rust dans des environnements d'exécution d'applications web populaires. Par exemple, l'approche [application hybride Rust + JavaScript](https://www.secondstate.io/articles/getting-started-with-rust-function/) gagne en popularité.

## ? La blockchain est un vivier de Rust

En ce qui concerne les logiciels d'infrastructure, Rust se distingue vraiment comme un langage de programmation pour les systèmes de blockchain.

Pour tous les secteurs de l'industrie logicielle, l'enquête montre que la blockchain ne se classe qu'au 35e rang pour tous les développeurs logiciels, mais au 11e rang pour les développeurs Rust. Cela est en grande partie dû à l'adoption agressive de Rust par de grands projets de blockchain tels que [Polkadot / Substrate](https://www.parity.io/), [Oasis](https://www.oasislabs.com/), [Solana](https://solana.com/), et [Second State](https://www.secondstate.io/) etc.

À bien des égards, les blockchains sont parfaitement adaptées à Rust. Les blockchains représentent l'effort communautaire pour reconstruire l'infrastructure internet de manière décentralisée. Elles nécessitent des logiciels haute performance qui sont également très sûrs. Si vous êtes intéressé par une carrière d'ingénieur blockchain, Rust est une compétence indispensable aujourd'hui.

## Rust 764e0f WebAssembly

L'enquête révèle que WebAssembly est un environnement d'exécution populaire pour les programmes Rust. Rust et WebAssembly ont tous deux été inventés chez Mozilla.

Rust se concentre sur la performance et la sécurité de la mémoire, tandis que WebAssembly se concentre sur la performance et la sécurité d'exécution. En tant que conteneur d'exécution, WebAssembly rend également les programmes Rust multiplateformes et plus faciles à gérer. Il y a en effet beaucoup de synergie entre les deux technologies.

WebAssembly a été initialement inventé comme une machine virtuelle côté client pour exécuter des applications dans le navigateur. Mais comme Java et JavaScript avant lui, WebAssembly effectue maintenant la migration du côté client [vers le côté serveur](https://www.secondstate.io/articles/why-webassembly-server/).

Rust-dans-WebAssembly est prometteur avec la tendance de l'accélération de l'adoption de Rust dans les applications web backend. Vous pouvez commencer le développement d'applications Rust et WebAssembly à partir d'un projet de démarrage dans [ce dépôt GitHub](https://github.com/second-state/ssvm-nodejs-starter).

## ? La programmation asynchrone décolle

Ces dernières années, deux nouveaux langages de programmation ont gagné une traction significative parmi les développeurs. L'un est Rust, et l'autre est Go. Une grande partie de leur succès réside dans leur soutien supérieur aux modèles de programmation concurrente.

En fait, un ancien slogan de Rust est "la concurrence sans crainte". Il promet une productivité des développeurs dans l'écriture de programmes multithreads asynchrones optimisés pour les architectures CPU multicœurs d'aujourd'hui. Comme Node.js l'a démontré, une programmation asynchrone facile est cruciale pour le succès d'un langage ou d'un framework côté serveur.

L'enquête montre que 4 des 10 crates Rust les plus importants (c'est-à-dire les bibliothèques tierces), [tokio](https://tokio.rs/), [async](https://docs.rs/crate/async-std/1.4.0), [futures](https://docs.rs/futures/0.3.4/futures/), et [hyper](https://hyper.rs/), sont des frameworks pour des applications multithreads asynchrones.

## ? R, Python et JavaScript

À mesure que l'adoption de Rust grandit, les développeurs ont de plus en plus besoin d'intégrer des programmes Rust avec des programmes écrits dans d'autres langages. Par le passé, C et C++ étaient les langages les plus courants pour "parler" à Rust, car ils sont tous utilisés dans des projets de logiciels d'infrastructure.

À mesure que Rust se développe dans des projets de logiciels d'application, plus d'interfaces et de ponts au niveau du langage sont nécessaires maintenant. Un bon exemple est le [pont Rust JavaScript](https://www.secondstate.io/articles/rust-functions-in-nodejs/) qui supporte les [fonctions Rust dans les applications Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/).

L'enquête a révélé que, outre C/C++ et JavaScript, les développeurs Rust sont intéressés par l'intégration avec R et Python. Cela indique un intérêt des développeurs pour les applications de machine learning, de big data et d'intelligence artificielle (IA). En fait, de nombreux packages Python et R de machine learning et de statistiques sont implémentés dans des modules binaires natifs.

Rust est l'un des meilleurs langages de programmation pour écrire des modules natifs. [Cet exemple](https://github.com/second-state/rust-wasm-ai-demo) montre comment utiliser [Rust pour exécuter des modèles Tensorflow dans une application Node.js](https://www.secondstate.io/articles/artificial-intelligence/). À l'avenir, nous envisageons que de tels modules Rust s'exécutent dans des conteneurs gérés haute performance comme WebAssembly.

## Conclusion

2019 a été une année de croissance et d'améliorations incrémentielles pour Rust. À mesure que Rust devient un langage de programmation grand public, nous attendons avec impatience plus de documentation, plus d'outils, plus de support d'écosystème, plus d'interopérabilité avec d'autres langages, et une courbe d'apprentissage plus douce.

Et surtout, nous sommes impatients de nous faire plus d'amis et de nous amuser avec le langage de programmation le plus apprécié au monde !

## À propos de l'auteur

Le Dr. Michael Yuan est l'[auteur de 5 livres](http://www.michaelyuan.com/) sur l'ingénierie logicielle. Son dernier livre [Building Blockchain Apps](https://www.buildingblockchainapps.com/) a été publié par Addison-Wesley en décembre 2019. Le Dr. Yuan est le co-fondateur de [Second State](https://www.secondstate.io/), une startup financée par des capitaux-risqueurs qui apporte les technologies WebAssembly et Rust aux applications [cloud](https://www.secondstate.io/articles/why-webassembly-server/), [blockchain](https://docs.secondstate.io/), et [IA](https://github.com/second-state/rust-wasm-ai-demo/blob/master/README.md). Elle permet aux développeurs de déployer des [fonctions Rust rapides, sûres, portables et serverless sur Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/).

<iframe src="https://webassemblytoday.substack.com/embed" width="480" height="320" style="border:1px solid #EEE;background:white"></iframe>

Avant Second State, le Dr. Yuan était un contributeur de longue date à l'open source chez Red Hat, JBoss et Mozilla. En dehors du logiciel, le Dr. Yuan est un chercheur principal aux National Institutes of Health, avec plusieurs prix de recherche sur le cancer et la santé publique. Il est titulaire d'un doctorat en astrophysique de l'Université du Texas à Austin.