---
title: 'Présentation de Packem : un bundler expérimental ultra-rapide écrit en Rust'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T16:36:27.000Z'
originalURL: https://freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AP72bMDkd2rDgR4txJreIQ.png
tags:
- name: Bundler
  slug: bundler
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Rust
  slug: rust
- name: TypeScript
  slug: typescript
seo_title: 'Présentation de Packem : un bundler expérimental ultra-rapide écrit en
  Rust'
seo_desc: 'By Bukhari Muhammad

  Packem is an experimental precompiled JavaScript module bundler primarily implemented
  in Rust. It can also handle a variety of other file types like YAML/TOML, fragment
  shader files and a lot more. Checkout the website or the GitH...'
---

Par Bukhari Muhammad

Packem est un bundler expérimental de modules JavaScript précompilés, principalement implémenté en Rust. Il peut également gérer une variété d'autres types de fichiers comme YAML/TOML, des fichiers de shaders de fragments et bien plus encore. Consultez le [site web](https://packem.github.io/) ou la [page GitHub](https://github.com/packem/packem) pour commencer rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/qAPcGMSL2YG2dAXsQL0rzSN7vytigBv8HQd6)
_Le logo de Packem. Toujours apaisant._

Packem résout les dépendances d'un module et les réhydrate dans un graphe de modules, une liste plate contenant des interfaces de modules qui sont essentiellement des **références à des structures de données mutables basées sur le tas en mémoire** contenant des métadonnées spéciales d'un module dans le graphe de modules.

La plupart de la logique métier est abstraite en Rust en utilisant des liaisons FFI pour permettre des interactions de bas niveau entre les deux extrémités. Les binaires Rust sont disponibles sous forme d'addons Node C/C++ précompilés dans le [dépôt de Packem](https://github.com/packem/packem/tree/master/bin). Un CI basé sur le cloud est utilisé pour exécuter quelques scripts avec des installations pre-gyp, produisant des binaires spécifiques au système d'exploitation avec support pour les versions ultérieures de Node (8, 9, 10).

Cette couche du cœur de Packem est ce à quoi l'on fait référence comme le **Contexte Logique (LC)**. Toutes les autres opérations qui ne sont pas _explicitement prioritaires_ sont régressées dans l'environnement d'exécution général de Node, qui, en termes de Packem, est le **Contexte d'Exécution (RC)**. Lisez plus sur les contextes [ici](https://packem.github.io/docs/execution-contexts.html).

Théoriquement, le graphe de modules est maintenu plat pour éviter les pièges courants qui entraîneraient des traversées inutiles si un arbre était utilisé à la place. Cela permet au RC de suivre des cas tels que les dépendances circulaires profondes ou les imports dynamiques fortement imbriqués (division de code), parmi d'autres, de manière appropriée avec un minimum d'implications de performance ou d'effets secondaires.

![Image](https://cdn-media-1.freecodecamp.org/images/Ig7Fy4kGltI7JTU9IqMpMBH7Gvq-ctV2z44f)
_Un aperçu du cycle de bundling à partir des contextes._

> Plus de détails peuvent être trouvés dans le [README.md](https://github.com/packem/packem) de Packem.

J'avais cette idée en tête mais je n'avais jamais prévu de l'exécuter jusqu'à ce que je _m'associe_ avec [Saddam M](https://www.freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517/undefined). Il a vraiment été dans mon intérêt de voir le bundling de modules comme un concept sûr pour que chacun puisse apprendre, comprendre et implémenter. Voir des gens lutter avec des configurations, de la documentation et des plugins était extrêmement horrible et j'aimerais saisir l'opportunité de changer cela. Avec vous. Avec Packem.

### Histoire rapide

J'ai pris le temps d'épuiser la plupart des bundlers écrits dans un environnement non-JavaScript. J'ai découvert que la plupart d'entre eux _avaient oublié_ qu'ils étaient censés être un bundler et non une bibliothèque C/C++ des années 1990.

Ce que je voulais, c'était un bundler qui effectue la plupart des tâches lourdes dans un langage _proche du matériel_ pour l'utilisateur sans nécessiter d'interaction avec ses internes. Ensuite, j'ai trouvé Rust. Un langage système intelligent et concis qui présente des caractéristiques louables comme un modèle de concurrency sans crainte, la sécurité des types, et plus encore ! Je m'attendrais à autant en utilisant C/C++, mais je préférerais rester avec Rust puisque c'est assez simple en ce qui concerne la gestion de la mémoire.

### Pourquoi un autre bundler ?

Alors, quel est l'intérêt ici ? Pourquoi avons-nous besoin d'un autre outil de build alors que nous avons déjà des outils incroyables comme webpack, Parcel, Rollup, etc ? Je vais vous emmener avec quelques raisons pourquoi. Peut-être que vous pourriez avoir vos propres intérêts à voir vos temps de build de développement et de production fortement réduits.

#### C'est 2019, nous n'avons plus besoin d'outils lents

Bien que Packem soit plus rapide que webpack 4, **il est plus de deux fois plus rapide que Parcel (avec la compilation multicœur)**. Dans un test de benchmark, nous avons bundlé [Lodash v4.17.1](https://lodash.com/docs/4.17.11) avec Packem et Parcel et voici le résultat :

> Ne prenez jamais les benchmarks au pied de la lettre. Vous pouvez le tester vous-même [ici](https://github.com/bukharim96/packem-lodash-test).

La raison pour laquelle je ne me suis pas donné la peine de benchmarker Parcel contre webpack est que webpack 4 est profondément plus rapide que Parcel. J'ai prouvé ce fait en utilisant les propres benchmarks de [Sean T. Larkin](https://www.freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517/undefined) et un fil Twitter à ce sujet peut être trouvé [ici](https://twitter.com/bukharim96/status/1099049693290680321?s=20).

#### Parce que nous le pouvons. N'importe qui peut, non ?

Bien sûr, ce qui aura le plus de sens, c'est parce que _nous le pouvons_. Nous avions l'idée d'avoir des temps de bundling plus rapides avec une interface Rust soit avec FFI ou WASM (n'étions toujours pas sûrs à l'époque). FFI était plus raisonnable en termes de vitesse et d'expérience développeur, donc nous avons opté pour une implémentation de Packem en liaisons FFI Rust.

Nous avons rencontré quelques problèmes liés aux threads, donc nous n'avons pas beaucoup utilisé les ressources disponibles. En conséquence, nous avons utilisé plusieurs processus enfants Node (avec [_node-worker-farm_](https://github.com/rvagg/node-worker-farm)_), la même technique que Parcel utilise pour la compilation multicœur, mais pour des graphes de modules plus grands puisque cela ajoute un temps de démarrage significatif en plus du temps de fonctionnement de Node lorsqu'il est utilisé avec des graphes de modules plus petits.

### Style de configuration

C'était une partie délicate. Il y avait beaucoup de questions qui nécessitaient une bonne réponse pour choisir le bon style de configuration. Statique ou dynamique ? JSON/YAML/TOML ? Notre choix était entièrement basé sur le fait que nous **avions besoin** que Packem :

1. Ait un style de configuration plus propre, et
2. Soit agnostique des autres configurations personnalisées de l'utilisateur comme _.babelrc_ ou _package.json_.

En résumé, nous avons procédé avec un style de configuration statique puisque nous avons trouvé que c'était exactement ce dont nous avions besoin. Quelque chose qui pourrait _dire de manière déclarative à Packem comment gérer le cycle de bundling_. Toutes les limites d'avoir une configuration statique ont été clairement définies.

Un autre aspect d'intérêt était le type de fichier que nous devrions utiliser pour la configuration. JSON, plus courant pour une majorité écrasante de développeurs JavaScript, ou YAML/TOML/XML, moins courants mais ayant leurs propres avantages. Une suggestion a été faite pour le support JSON ([#5](https://github.com/packem/packem/issues/5)).

JSON n'a tout simplement pas fonctionné à cause de toutes les guillemets de chaîne inutiles, les accolades et les crochets, ce qui est logique puisque c'est un **format d'échange de données**. Une approche XML ne mérite aucun respect en ce qui concerne son utilisation comme format de configuration, car elle aggrave les choses par rapport à JSON en ce qui concerne les caractères inutiles. TOML a introduit beaucoup de nouvelles lignes, et le débogage des options imbriquées n'avait pas l'air attrayant, car nous savions que les plugins Packem pouvaient devenir très imbriqués.

Le grand gagnant était YAML ! Il a réussi à passer tous les aspects d'être un format de configuration approprié (pour Packem au moins). Il :

1. Rend la configuration indolore.
2. Utilise une approche élégante.
3. Est encore familier à l'œil JavaScript.
4. A été conçu spécifiquement pour ce cas d'utilisation (configurations).

Voici un exemple de configuration typique de Packem (_packem.config.yml_). Vérifiez par vous-même et pensez à écrire le même contenu dans un style JSON/TOML/XML.

Pour information, seules les deux premières options sont nécessaires ! ?

#### Étendre Packem

> Cette fonctionnalité n'est pas encore implémentée.

Parfois, nous pourrions avoir besoin d'utiliser une fonctionnalité qui **n'existe pas encore**, **n'est peut-être pas implémentée dans Packem** ou est **très spécifique à notre projet**. Pour ce cas, vous auriez deux façons de résoudre vos besoins :

1. [Créer un plugin Packem](https://packem.github.io/docs/plugin-system.html) pour votre cas d'utilisation (ce qui est l'option recommandée).
2. Construire un RC personnalisé sur les binaires de Packem.

L'utilisation de Rust nous donne la chance de reformer le LC en d'autres formats binaires, tels que WebAssembly, ce qui permettra à Packem d'exhiber plusieurs cibles de compilation :

1. Un addon C/C++ basé sur NAPI avec des binaires spécifiques à la plateforme requis par le RC par défaut de Packem.
2. Un binaire basé sur WebAssembly qui est multiplateforme et injecté dans le RC.
3. Le standalone par défaut de Packem qui utilise WebAssembly avec une implémentation compatible navigateur du RC.

> Les deux derniers ne sont pas encore à l'ordre du jour puisque des refactorisations internes sont encore en cours.

Le guide avancé devrait bientôt vous montrer comment **construire un outil de build personnalisé en utilisant les binaires de Packem** pour répondre à vos propres besoins au cas où vous auriez besoin d'utiliser Packem en dehors des environnements navigateur et Node. Ces binaires complètent l'ensemble de la génération de graphe, le filtrage des doublons et d'autres aspects liés au graphe. Cela signifie que vous pouvez utiliser votre propre sérialiseur, observateur de fichiers, système de plugins, etc. C'est un peu comme la façon dont vous pouvez construire votre propre moteur de rendu sur OpenGL.

1. Vous pouvez toujours adopter [le système de plugins de Packem](https://packem.github.io/docs/plugin-system.html) puisque cela vous permettra d'intégrer l'écosystème de plugins de Packem avec votre bundler personnalisé.
2. Si vous n'êtes pas sûr de devoir construire un bundler personnalisé, sachez que vous n'en aurez pas toujours besoin. Veuillez essayer de créer une issue en premier.
3. Il est garanti que ces binaires accéléreront votre flux de travail en fonction de vos cas d'utilisation spécifiques.

#### État actuel

* ✂ [Code Splitting](https://packem.github.io/docs/code-splitting.html) pour les modes développement et production.
* ? CLI améliorée (`—verbose`) pour de meilleures informations sur le cycle de bundling.
* ? [Interfaces de Module](https://packem.github.io/docs/advanced-plugin-apis.html#module-interfaces) pour permettre une manipulation facile du graphe de modules.
* ✔ Priorité appropriée. Les fonctionnalités natives s'intègrent parfaitement dans le LC. Cela signifie qu'il y a de plus grandes chances de builds rapides.
* ? Exporter `NativeUtils` pour une utilisation externe des fonctionnalités natives, y compris `generateModuleGraph` qui relance le processus de génération d'un graphe de modules. C'est lourd mais toujours utile dans les cas où vous auriez besoin d'un clone du graphe de modules actif actuel. L'utiliser signifie doubler le temps de build, alors utilisez-le avec précaution.

#### Qu'est-ce qui suit ?

Voici les fonctionnalités que nous espérons avoir bientôt dans les prochaines versions. Avec vos efforts, nous pourrions **faire du bundling de la bonne manière**. Lorsque Packem sera à la version _1.0_, nous espérons avoir un support complet pour toutes les fonctionnalités listées ci-dessous et les autres mentionnées dans la [feuille de route de Packem](https://packem.github.io/docs/roadmap.html).

* Un standalone compatible navigateur de Packem avec le LC en WebAssembly pour une intégration plus étroite avec le système sous-jacent. [Axel Rauschmayer](https://www.freecodecamp.org/news/introducing-packem-a-super-fast-experimental-bundler-written-in-rust-e981af875517/undefined) a déjà [fait une demande de fonctionnalité](https://github.com/packem/packem/issues/1) pour avoir une version compatible Node en WASM. Pour le record, nous travaillerons bientôt sur les deux.
* Treeshaking, mais avancé. Résoudre les imports nommés/non nommés et supprimer le code mort devrait être un jeu d'enfant. Cela signifie que vous pouvez utiliser des bibliothèques comme _lodash_ au lieu de _lodash-es_ sans vous soucier de savoir si votre code sera **élidé** ou non.
* Auto Config. Comme Zero Config, mais orienté par défaut pour une flexibilité supplémentaire.
* Options CLI avancées pour faire du développement avec Packem une seconde nature.
* Meilleure gestion des erreurs.
* Plus de cibles d'environnement. Packem ne peut bundler que pour le navigateur pour l'instant. Finalement, nous espérons supporter Node CJS et d'autres formats également.
* Plus de plugins. Nous avons besoin de plus de plugins ! Packem dispose d'un ensemble de plugins courants pour vous faire démarrer plus rapidement. Mais pour faire grandir une communauté, nous aurons besoin d'un grand écosystème de plugins. Consultez les [plugins courants](https://packem.github.io/docs/common-plugins.html) disponibles ou la [section plugins](https://packem.github.io/docs/plugin-system.html) sur le site pour commencer à développer un plugin tout de suite.
* Et bien plus encore...

#### Ressources

* [Packem sur GitHub](https://github.com/packem/packem/)
* [Feuille de route et demandes de fonctionnalités](https://packem.github.io/docs/roadmap.html)
* [Site officiel de Packem](https://packem.github.io/)
* [Création de plugins avec Packem](https://packem.github.io/docs/plugin-system.html)
* [Code Splitting avec Packem](https://packem.github.io/docs/code-splitting.html)
* [Le graphe de modules](https://packem.github.io/docs/the-module-graph.html)

**Packem n'a pas encore atteint la version _1.0_**. Si vous avez trouvé Packem intéressant, essayez de contribuer à Packem lui-même en créant des plugins, en mettant à jour la documentation, en nous soutenant financièrement, en représentant Packem lors de conférences ou par tout autre moyen. Nous apprécions vos efforts !

Bonne bundling ! 😊