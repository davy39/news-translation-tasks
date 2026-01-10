---
title: Nous approchons de la sortie de Babel 7.0. Voici tout ce que nous avons fait
  de cool.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T11:06:33.000Z'
originalURL: https://freecodecamp.org/news/were-nearing-the-7-0-babel-release-here-s-all-the-cool-stuff-we-ve-been-doing-8c1ade684039
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vLtFVPTHJGDfw3XOl4C1Sw.jpeg
tags:
- name: Babel
  slug: babel
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Nous approchons de la sortie de Babel 7.0. Voici tout ce que nous avons
  fait de cool.
seo_desc: 'By Henry Zhu


  6 months later, the actual release https://twitter.com/left_pad/status/1034204330352500736!


  Hey there ?! I’m Henry, one of the maintainers on Babel.


  EDIT: I’ve left Behance and have made a Patreon to try to pursue working on open
  sour...'
---

Par Henry Zhu

> 6 mois plus tard, la sortie officielle [https://twitter.com/left_pad/status/1034204330352500736](https://twitter.com/left_pad/status/1034204330352500736) !

Hey là-bas ?! Je suis [Henry](http://twitter.com/left_pad), l'un des mainteneurs de [Babel](http://babeljs.io/).

> EDIT : J'ai [quitté Behance](https://www.henryzoo.com/blog/2018/02/15/leaving-behance.html) et j'ai créé un [Patreon](https://www.patreon.com/henryzhu) pour essayer de poursuivre [le travail à temps plein sur l'open source](https://www.henryzoo.com/blog/2018/03/02/in-pursuit-of-open-source-part-1.html), veuillez envisager de faire un don (demandez à votre entreprise).

#### Une rapide introduction à Babel

Certaines personnes aiment penser à Babel comme un outil qui permet d'écrire du code ES6. Plus spécifiquement, un compilateur JavaScript qui convertira ES6 en code ES5. Cela était assez approprié lorsque son nom était 6to5, mais je pense que Babel est devenu bien plus que cela.

Maintenant, faisons un peu marche arrière. La raison pour laquelle cela est même nécessaire en premier lieu est que, contrairement à la plupart des langages sur le serveur (même Node.js), la version de JavaScript que vous pouvez exécuter dépend de votre version spécifique de navigateur. Donc, peu importe si vous utilisez les derniers navigateurs si vos utilisateurs (que vous souhaitez garder) sont encore sur IE. Si vous voulez écrire `class A {}`, par exemple, alors vous êtes malchanceux — un certain nombre de vos utilisateurs obtiendront une `SyntaxError` et une page blanche.

C'est pourquoi Babel a été créé. Il permet d'écrire la version de JavaScript souhaitée, en sachant qu'elle s'exécutera correctement sur tous les (anciens) navigateurs que vous supportez.

Mais cela ne s'arrête pas à « ES6 » (certaines personnes aiment dire ES2015). Babel a certainement élargi son objectif initial de ne compiler que le code ES6, et compile maintenant n'importe quelle version ES20xx souhaitée (la dernière version de JavaScript) en ES5.

#### Le processus en cours

L'une des choses intéressantes à propos du projet est que, tant que de nouvelles syntaxes JavaScript sont ajoutées, Babel devra implémenter une transformation pour les convertir.

Mais vous pourriez vous demander, pourquoi devrions-nous même envoyer une version compilée (taille de code plus grande) aux navigateurs qui supportent cette syntaxe ? Comment savons-nous même quelles syntaxes chaque navigateur supporte ?

Eh bien, nous avons créé `[babel-preset-env](https://babeljs.io/docs/en/babel-preset-env)` pour aider avec ce problème en créant un outil qui permet de spécifier quels navigateurs vous supportez. Il transformera automatiquement uniquement les choses que ces navigateurs ne supportent pas nativement.

Au-delà de cela, Babel (en raison de son utilisation dans la communauté) a une place dans l'influence de l'avenir du langage JavaScript lui-même ! Étant donné que c'est un outil pour transformer le code JS, il peut également être utilisé pour implémenter n'importe laquelle des propositions soumises à [TC39](http://2ality.com/2015/11/tc39-process.html) (Comité Technique 39 d'Ecma, le groupe qui fait avancer JavaScript en tant que standard).

Il y a tout un processus qu'une « proposition » traverse, de l'Étape 0 à l'Étape 4 lorsqu'elle est intégrée dans le langage. Babel, en tant qu'outil, est au bon endroit pour tester de nouvelles idées et permettre aux développeurs de l'utiliser dans leurs applications afin qu'ils puissent donner leur avis au comité.

Cela est vraiment important pour plusieurs raisons : le comité veut être sûr que les changements qu'il apporte sont ce que la communauté veut (cohérent, intuitif, efficace). Implémenter une idée non spécifiée dans le navigateur est lent (C++ dans le navigateur vs. JavaScript dans Babel), coûteux, et nécessite que les utilisateurs utilisent un flag dans le navigateur au lieu de changer leur fichier de configuration Babel.

Étant donné que Babel est si omniprésent, il y a de bonnes chances que son utilisation réelle se produise. Cela rendra la proposition bien meilleure que si elle était simplement implémentée sans aucun examen de la communauté des développeurs dans son ensemble.

Et ce n'est pas seulement utile en production. Notre [REPL](https://babeljs.io/repl) en ligne est utile pour les personnes apprenant JavaScript lui-même, et leur permet de tester des choses.

Je pense que Babel est dans une excellente position pour être un outil éducatif pour les programmeurs afin qu'ils puissent continuer à apprendre comment JavaScript fonctionne. En contribuant au projet lui-même, ils apprendront de nombreux autres concepts tels que les AST, les compilateurs, la spécification du langage, et plus encore.

Je suis vraiment excité par l'avenir du projet et j'ai hâte de voir où l'équipe peut aller. Veuillez nous rejoindre et nous aider !

#### Mon histoire

Ce sont quelques-unes des raisons pour lesquelles je suis excité de travailler sur ce projet chaque jour, surtout en tant que mainteneur. La plupart des mainteneurs actuels, y compris moi-même, n'ont pas créé le projet mais ont rejoint un an après — et c'est toujours [époustouflant](https://medium.com/@left_pad/ossthanks-some-thoughts-d0267706c2c6) de penser à mes débuts.

Quant à moi, j'ai reconnu un besoin et un projet intéressant. Je me suis lentement et régulièrement impliqué davantage, et maintenant j'ai pu faire en sorte que mon employeur, [Behance](https://www.behance.net/), sponsorise la moitié de mon temps sur Babel.

Parfois, « maintenir » signifie simplement corriger des bugs, répondre à des questions sur notre Slack ou [Twitter](https://twitter.com/babeljs/), ou écrire un journal des changements (c'est vraiment à chacun de nous de décider). Mais récemment, j'ai réduit mon attention sur les corrections de bugs et les fonctionnalités. Au lieu de cela, j'ai consacré du temps à réfléchir à des problèmes de plus haut niveau comme : quel est l'avenir de ce projet ? Comment pouvons-nous faire croître notre communauté en termes de nombre de mainteneurs par rapport au nombre d'utilisateurs ? Comment pouvons-nous soutenir le projet en termes de financement ? Où nous situons-nous dans l'écosystème JavaScript dans son ensemble (éducation, [TC39](https://github.com/tc39/proposals), outils) ? Et y a-t-il un rôle pour nous à jouer dans l'aide aux nouvelles personnes à rejoindre l'open source ([RGSoC](https://twitter.com/left_pad/status/959439119960215552) et [GSoC](https://summerofcode.withgoogle.com/)) ?

En raison de ces questions, ce qui m'excite le plus avec cette sortie n'est pas nécessairement les particularités de l'ensemble des fonctionnalités (qui sont nombreuses : implémentations initiales de nouvelles propositions comme l'[Opérateur Pipeline (a |> b)](https://github.com/babel/babel/tree/master/packages/babel-plugin-proposal-pipeline-operator), un [nouveau preset TypeScript](https://github.com/babel/babel/tree/master/packages/babel-preset-typescript) avec l'aide de l'équipe TS, et les fichiers .babelrc.js).

Plutôt, je suis excité par ce que toutes ces fonctionnalités représentent : une année de travail acharné pour essayer de ne rien casser, en équilibrant les attentes des utilisateurs (pourquoi la construction est si lente/la sortie du code est si grande, pourquoi le code n'est pas suffisamment conforme aux spécifications, pourquoi cela ne fonctionne-t-il pas sans configuration, pourquoi n'y a-t-il pas d'option pour x), et en soutenant une équipe solide composée principalement de bénévoles.

Et je sais que notre industrie a une énorme concentration sur les « sorties majeures », les fonctionnalités hypées et les étoiles, mais ce n'est qu'un jour qui s'estompe. J'aimerais suggérer que nous continuions à réfléchir à ce qu'il faut pour être cohérent dans la poussée de l'écosystème vers l'avant de manière saine.

Cela pourrait simplement signifier réfléchir au fardeau mental et émotionnel de la maintenance. Cela pourrait signifier réfléchir à la manière de fournir du mentorat, de la gestion des attentes, des conseils sur l'équilibre travail/vie privée et d'autres ressources aux personnes souhaitant s'impliquer, au lieu d'encourager les développeurs à s'attendre à une aide immédiate et gratuite.

#### Plongeons dans le journal des changements

Eh bien, j'espère que vous apprécierez le long journal des changements ?. Si vous êtes intéressé à nous aider, veuillez nous le faire savoir et nous serons ravis d'en parler davantage.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zvhm_vD3VWFaWA1c.png)

Nous avons commencé une nouvelle [page vidéos](https://babeljs.io/docs/community/videos/), puisque les gens voulaient en savoir plus sur le fonctionnement de Babel et contribuer en retour. Cette page contient des vidéos de conférences sur Babel et des concepts connexes de la part des membres de l'équipe et des personnes de la communauté.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8q5nV1APkAFKydrZ.png)

Nous avons également créé une nouvelle [page d'équipe](https://babeljs.io/team) ! Nous mettrons à jour cette page à l'avenir avec plus d'informations sur ce que les gens font et pourquoi ils sont impliqués. Pour un projet aussi important, il existe de nombreuses façons de s'impliquer et d'aider.

Voici quelques points forts et faits rapides :

* Babel a eu 3 ans le [28 septembre 2017](https://babeljs.io/blog/2017/10/05/babel-turns-three) !
* Daniel a [déplacé](https://twitter.com/left_pad/status/926096965565370369) `babel/babylon` et `babel/babel-preset-env` dans le monorepo principal de Babel, [babel/babel](https://github.com/babel/babel). Cela inclut tout l'historique Git, les labels et les problèmes.
* Nous avons reçu un [don de 1k/mois](https://twitter.com/left_pad/status/923696620935421953) de Facebook Open Source !
* C'est le don mensuel le plus élevé que nous ayons reçu depuis le début (le suivant est de 100$/mois).
* En attendant, nous utiliserons nos fonds pour nous rencontrer en personne et envoyer des personnes aux réunions TC39. Ces réunions ont lieu tous les 2 mois dans le monde.
* Si une entreprise souhaite sponsoriser spécifiquement quelque chose, nous pouvons créer des problèmes séparés pour le suivre. Cela était difficile auparavant, car nous devions payer de notre poche ou trouver une conférence à laquelle parler la même semaine pour aider à couvrir les dépenses.

#### Comment vous pouvez aider

Si votre entreprise souhaite **redonner** en soutenant une partie fondamentale du développement JavaScript et de son avenir, envisagez de faire un don à notre [Open Collective](https://opencollective.com/babel). Vous pouvez également faire don de temps de développement pour aider à maintenir le projet.

#### #1 : Aider à maintenir le projet (temps de développement au travail)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Ingénieur : Il y a un truc dans SQL Server Enterprise qui nous bloque<br>Entreprise : Organisons un appel la semaine prochaine avec eux et une discussion en cours pour le résoudre le trimestre prochain<br><br>Ingénieur : Il y a un truc dont nous avons besoin dans babel, puis-je passer 2 jours avec une PR pour cela<br>Entreprise : lol non c'est leur travail <a href="https://t.co/icgaoJ0dTe">https://t.co/icgaoJ0dTe</a></p>&mdash; Shiya (@ShiyaLuo) <a href="https://twitter.com/ShiyaLuo/status/931230821976907776?ref_src=twsrc%5Etfw">16 novembre 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

La meilleure chose pour Babel est de trouver des personnes qui sont engagées à aider avec le projet, étant donné la quantité massive de travail et de responsabilité qu'il nécessite. Encore une fois, [je ne me suis jamais senti prêt](https://dev.to/hzoo/im-the-maintainer-of-babel-ask-me-anything-282/comments/1k6d) à être un mainteneur, mais je suis somehow tombé dessus. Mais je ne suis qu'une seule personne, et notre équipe n'est que quelques personnes.

#### #2 : Aider à financer le développement

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Entreprise : "Nous aimerions utiliser SQL Server Enterprise"<br>MS : "Cela coûtera un quart de million de dollars + 20K$/mois"<br>Entreprise : "Ok !"<br>...<br>Entreprise : "Nous aimerions utiliser Babel"<br>Babel : "Ok ! npm i babel --save"<br>Entreprise : "Cool"<br>Babel : "Souhaitez-vous aider à contribuer financièrement ?"<br>Entreprise : "lol non"</p>&mdash; Adam Rackis (@AdamRackis) <a href="https://twitter.com/AdamRackis/status/931195056479965185?ref_src=twsrc%5Etfw">16 novembre 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Nous voulons définitivement pouvoir financer les personnes de l'équipe afin qu'elles puissent travailler à temps plein. Logan, en particulier, a quitté son travail il y a un moment et utilise nos fonds actuels pour travailler sur Babel à temps partiel.

#### #3 Contribuer d'autres manières ?

Par exemple, [Angus](https://twitter.com/angustweets) nous a fait une [chanson officielle](https://medium.com/@angustweets/hallelujah-in-praise-of-babel-977020010fad) !

#### Mise à niveau

Nous travaillerons également sur un outil de mise à niveau qui aidera à [réécrire vos fichiers package.json/.babelrc](https://github.com/babel/notes/issues/44) et plus encore. Idéalement, cela signifie qu'il modifiera tout changement de numéro de version nécessaire, renommage de package et changements de configuration.

Veuillez nous contacter pour obtenir de l'aide et pour poster des problèmes lors de la tentative de mise à jour. C'est une excellente opportunité de s'impliquer et d'aider l'écosystème à se mettre à jour !

#### Résumé du [post précédent](https://babeljs.io/blog/2017/09/12/planning-for-7.0)

* Abandon du support de Node 0.10/0.12/5.
* Mise à jour des [propositions TC39](https://github.com/babel/proposals/issues)
* Séparateur numérique : `1_000`
* Opérateur de chaînage optionnel : `a?.b`
* `import.meta` (analysable)
* Liaison de capture optionnelle : `try { a } catch {}`
* BigInt (analysable) : `2n`
* Division des extensions d'exportation en `export-default-from` et `export-ns-form`
* Support de `.babelrc.js` (une configuration utilisant JavaScript au lieu de JSON)
* Ajout d'un nouveau preset Typescript et séparation des presets React/Flow
* Ajout de la [prise en charge des fragments JSX](https://reactjs.org/blog/2017/11/28/react-v16.2.0-fragment-support.html) et diverses mises à jour de Flow
* Suppression de la dépendance interne `babel-runtime` pour une taille plus petite

#### Nouvelles propositions TC39 mises à jour

* Opérateur Pipeline : `a |> b`
* Expressions de lancement : `() => throw 'hi'`
* Opérateur de coalescence nulle : `a ?? b`

#### Presets annuels obsolètes (par exemple, babel-preset-es20xx)

TL;DR : utilisez `babel-preset-env`.

Qu'y a-t-il de mieux que de devoir décider quel preset Babel utiliser ? Que cela soit fait pour vous, automatiquement !

Même si la quantité de travail nécessaire pour maintenir les listes de données est énorme — encore une fois, pourquoi nous avons besoin d'aide — cela résout plusieurs problèmes. Cela garantit que les utilisateurs sont à jour avec la spécification. Cela signifie moins de confusion de configuration/package. Cela signifie un chemin de mise à niveau plus facile. Et cela signifie moins de problèmes concernant ce qui est quoi.

`babel-preset-env` est en fait un preset assez _ancien_ qui remplace tous les autres presets de syntaxe dont vous aurez besoin (es2015, es2016, es2017, es20xx, latest, et ainsi de suite).

![Image](https://cdn-media-1.freecodecamp.org/images/0*wgAjmRI1MVcI_Veg.png)

Il compile la dernière version annuelle de JavaScript (ce qui est en Stage 4) qui remplace tous les anciens presets. Mais il a également la capacité de compiler selon les environnements cibles que vous spécifiez : il peut gérer le mode développement, comme la dernière version d'un navigateur, ou plusieurs builds, comme une version pour IE. Il a même une autre version pour les navigateurs evergreen.

#### Ne pas supprimer les presets de Stage (babel-preset-stage-x)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Niveau de frustration si nous supprimons les presets de Stage dans Babel ? (en faveur de l'exigence explicite des plugins de proposition puisqu'ils ne sont pas encore JavaScript)</p>&mdash; Henry Zhu (@left_pad) <a href="https://twitter.com/left_pad/status/873242704364306433?ref_src=twsrc%5Etfw">9 juin 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


Nous pouvons toujours le maintenir à jour, et peut-être devons-nous simplement déterminer un meilleur système que celui des presets actuels.

Actuellement, les presets de stage sont simplement une liste de plugins que nous mettons à jour manuellement après chaque réunion TC39. Pour rendre cela gérable, nous devons permettre des augmentations majeures de version pour ces packages « instables ». Cela est en partie parce que la communauté recréera ces packages de toute façon. Donc, nous pourrions aussi bien le faire à partir d'un package officiel, puis avoir la capacité de fournir une meilleure messagerie et ainsi de suite.

#### Renommages : Packages avec portée (`@babel/x`)

Voici un sondage que j'ai publié il y a presque un an :

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Avis sur <a href="https://twitter.com/babeljs?ref_src=twsrc%5Etfw">@babeljs</a> utilisant des packages npm avec portée pour 7.0 ?</p>&mdash; Henry Zhu (@left_pad) <a href="https://twitter.com/left_pad/status/821551189166878722?ref_src=twsrc%5Etfw">18 janvier 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


À l'époque, peu de projets utilisaient des packages avec portée, donc la plupart des gens ne savaient même pas qu'ils existaient. Vous auriez peut-être dû payer pour un compte d'organisation npm à l'époque, alors que maintenant c'est gratuit (et supporte également les packages non portés).

Les problèmes de recherche de packages avec portée sont résolus, et les comptes de téléchargement fonctionnent. Le seul obstacle restant est que certains registres tiers ne supportent toujours pas les packages avec portée. Mais je pense que nous sommes à un point où il semble assez déraisonnable d'attendre cela.

Voici pourquoi nous préférons les packages avec portée :

* Le nommage est difficile : nous n'aurons pas à vérifier si quelqu'un d'autre a décidé d'utiliser notre convention de nommage pour son propre plugin
* Nous avons des problèmes similaires avec le squattage de packages
* Parfois, les gens créent `babel-preset-20xx` ou un autre package parce que c'est drôle. Nous devons créer un problème et envoyer un email pour le récupérer.
* Les gens ont un package légitime, mais il se trouve qu'il porte le même nom que ce que nous voulions l'appeler.
* Les gens voient qu'une nouvelle proposition est en cours de fusion (comme l'opérateur de chaînage optionnel ou l'opérateur de pipeline) et décident de forker et de publier une version sous le même nom. Ensuite, lorsque nous publions, il nous dit que le package a déjà été publié ?. Je dois donc trouver leur email et envoyer un email à la fois à eux et au support npm pour récupérer le package et le republier.
* Qu'est-ce qu'un package « officiel » et qu'est-ce qu'un package utilisateur/communauté avec le même nom ? Nous recevons des rapports de problèmes de personnes utilisant des packages mal nommés ou non officiels parce qu'elles pensaient qu'il faisait partie de Babel. Un exemple de cela était un rapport selon lequel `babel-env` réécrivait leur fichier `.babelrc`. Il leur a fallu un certain temps pour réaliser qu'il ne s'agissait pas de `babel-preset-env`.

Donc, il semble assez clair que nous devrions utiliser des packages avec portée, et, si quoi que ce soit, nous aurions dû le faire beaucoup plus tôt ?!

Exemples de changement de nom avec portée :

* `babel-cli` -> `@babel/cli`
* `babel-core` -> `@babel/core`
* `babel-preset-env` -> `@babel/preset-env`

#### Renommages : `-proposal-`

Toutes les propositions seront désormais nommées avec `-proposal-` pour signifier qu'elles ne font pas encore officiellement partie de JavaScript.

Ainsi, `@babel/plugin-transform-class-properties` devient `@babel/plugin-proposal-class-properties`, et nous le renommerons une fois qu'il atteindra le Stage 4.

#### Renommages : Suppression de l'année du nom du plugin

Les plugins précédents avaient l'année dans le nom, mais cela ne semble plus nécessaire maintenant.

Ainsi, `@babel/plugin-transform-es2015-classes` devient `@babel/plugin-transform-classes`.

Puisque les années n'étaient utilisées que pour es3/es2015, nous n'avons rien changé pour es2016 ou es2017. Cependant, nous déprécions ces presets en faveur de preset-env, et pour la révision des littéraux de gabarit, nous l'avons simplement ajouté à la transformation des littéraux de gabarit pour simplifier.

#### Dépendances et intégrations

Nous introduisons une dépendance sur `@babel/core` pour tous les plugins (`@babel/plugin-class-properties`), les presets (`@babel/preset-env`), et les packages de haut niveau (`@babel/cli`, `babel-loader`).

> Les peerDependencies sont des dépendances censées être utilisées par votre code, par opposition aux dépendances utilisées uniquement comme détail d'implémentation. — [Stijn de Witt via StackOverflow](https://stackoverflow.com/a/34645112).

`babel-loader` avait déjà une `peerDependency` sur `babel-core`, donc cela change simplement pour `@babel/core`. Ce changement empêche les gens d'essayer d'installer ces packages sur la mauvaise version de Babel.

Pour les outils qui ont déjà une `peerDependency` sur `babel-core` et ne sont pas prêts pour une mise à jour majeure (puisque changer la dépendance est une rupture de changement), nous avons publié une nouvelle version de `babel-core` pour combler les changements avec la nouvelle version [babel-core@7.0.0-bridge.0](https://github.com/babel/babel-bridge). Pour plus d'informations, consultez [cet issue](https://github.com/facebook/jest/pull/4557#issuecomment-344048628).

De même, des packages comme `gulp-babel`, `rollup-plugin-babel`, et ainsi de suite utilisaient tous `babel-core` comme dépendance. Maintenant, ceux-ci auront simplement une `peerDependency` sur `@babel/core`. Grâce à cela, ces packages n'ont pas à augmenter les versions majeures lorsque l'API `@babel/core` n'a pas changé.

#### [#5224](https://github.com/babel/babel/pull/5224) : publication indépendante des packages expérimentaux

Je mentionne cela dans [The State of Babel](http://babeljs.io/blog/2016/12/07/the-state-of-babel) dans la section `Versioning`. Voici le [Github Issue](https://github.com/babel/babylon/issues/275).

Vous vous souvenez peut-être qu'après Babel 6, Babel est devenu un ensemble de packages npm avec son propre écosystème de presets et plugins personnalisés.

Depuis lors, cependant, nous avons toujours utilisé un système de versionnage « fixe/synchronisé » (de sorte qu'aucun package ne soit en v7.0 ou au-dessus). Lorsque nous faisons une nouvelle sortie, comme `v6.23.0`, seuls les packages qui ont mis à jour le code dans la source sont publiés avec la nouvelle version. Le reste des packages est laissé tel quel. Cela fonctionne principalement en pratique parce que nous utilisons `^` dans nos packages.

Malheureusement, ce type de système nécessite qu'une version majeure soit publiée pour tous les packages une fois qu'un seul package en a besoin. Cela signifie soit que nous faisons beaucoup de petits changements de rupture (inutiles), soit que nous regroupons beaucoup de changements de rupture en une seule sortie. Au lieu de cela, nous voulons différencier les packages expérimentaux (Stage 0, et ainsi de suite) et tout le reste (es2015).

En raison de cela, nous avons l'intention de faire des augmentations majeures de version pour tous les plugins de proposition expérimentaux lorsque la spécification change, plutôt que d'attendre de mettre à jour tout Babel. Donc, tout ce qui est < Stage 4 serait ouvert aux changements de rupture sous la forme d'augmentations majeures de version. La même chose s'applique aux presets de Stage eux-mêmes (si nous ne les abandonnons pas entièrement).

Cela s'inscrit dans notre décision d'exiger que les plugins de proposition TC39 utilisent le nom `-proposal-`. Si la spécification change, nous ferons une augmentation majeure de version du plugin et du preset auquel il appartient (plutôt que de simplement faire une version de correctif qui peut casser pour les gens). Ensuite, nous devrons déprécier les anciennes versions et mettre en place une infrastructure qui mettra automatiquement à jour les gens afin qu'ils soient à jour sur ce que la spécification deviendra (et qu'ils ne restent pas bloqués sur quelque chose. Nous n'avons pas eu autant de chance avec les décorateurs.).

#### L'option `env` dans `.babelrc` n'est pas dépréciée !

Contrairement au [dernier post](https://babeljs.io/blog/2017/09/12/planning-for-7.0#deprecate-the-env-option-in-babelrc), nous avons simplement corrigé le comportement de fusion pour être [plus cohérent](https://twitter.com/left_pad/status/936687774098444288).

La configuration dans `env` est donnée une priorité plus élevée que les éléments de configuration racine. Et au lieu de l'approche étrange consistant à utiliser les deux, les plugins et les presets fusionnent désormais en fonction de leur identité, donc vous pouvez faire ceci :

```
{
  presets: [
    ['env', { modules: false}],
  ],
  env: {
    test: {
      presets: [
         'env'
      ],
    }
  },
}
```

avec `BABEL_ENV=test`. Il remplacerait la configuration env racine par celle de test, qui n'a pas d'options.

#### Support de `[class A extends Array](https://twitter.com/left_pad/status/940723982638157829)` (la plus ancienne mise en garde)

Babel enveloppera automatiquement tous les éléments natifs intégrés comme `Array`, `Error`, et `HTMLElement` afin que cela fonctionne simplement lors de la compilation des classes.

#### Vitesse

* De nombreuses [corrections](https://twitter.com/rauchg/status/924349334346276864) de [bmeurer](https://twitter.com/bmeurer) de l'équipe v8 !
* 60 % plus rapide via le [web-tooling-benchmark](https://github.com/v8/web-tooling-benchmark) [https://twitter.com/left_pad/status/927554660508028929](https://twitter.com/left_pad/status/927554660508028929)

#### preset-env : `"useBuiltins": "usage"`

`babel-preset-env` a introduit l'idée de compiler la syntaxe pour différentes cibles. Il a également introduit, via l'option `useBuiltIns`, la capacité d'ajouter uniquement les polyfills que les cibles ne supportent pas.

Ainsi, avec cette option, quelque chose comme :

```js
import "babel-polyfill";
```

peut se transformer en

```js
import "core-js/modules/es7.string.pad-start";
import "core-js/modules/es7.string.pad-end";
// ...
```

si l'environnement cible se trouve à supporter des polyfills autres que `padStart` ou `padEnd`.

Mais pour rendre cela encore meilleur, nous devrions uniquement importer des polyfills qui sont « utilisés » dans la base de code elle-même. Pourquoi importer `padStart` s'il n'est même pas utilisé dans le code ?

`"useBuiltins": "usage"` est notre première tentative pour aborder cette idée. Il effectue une importation en haut de chaque fichier, mais n'ajoute l'importation que s'il la trouve utilisée dans le code. Cette approche signifie que nous pouvons importer le nombre minimum de polyfills nécessaires pour l'application (et seulement si l'environnement cible ne le supporte pas).

Ainsi, si vous utilisez `Promise` dans votre code, il l'importera en haut du fichier (si votre cible ne le supporte pas). Les bundlers dédupliqueront le fichier s'il est le même, donc cette approche ne provoquera pas l'importation de plusieurs polyfills.

```js
import "core-js/modules/es6.promise";
var a = new Promise();

import "core-js/modules/es7.array.includes";
[].includes
a.includes
```

Avec l'inférence de type, nous pouvons savoir si une méthode d'instance comme `.includes` est pour un tableau ou non. Avoir un faux positif est acceptable jusqu'à ce que cette logique soit meilleure, puisque c'est toujours mieux que d'importer tout le polyfill comme avant.

#### Mises à jour diverses

* `[babel-template](https://github.com/babel/babel/blob/master/packages/babel-template)` est plus rapide et plus facile à utiliser
* [regenerator](https://github.com/facebook/regenerator) a été publié sous la [licence MIT](https://twitter.com/left_pad/status/938825429955125248) — c'est la dépendance utilisée pour compiler les générateurs/async
* Option « lazy » pour le plugin `modules-commonjs` via [#6952](https://github.com/babel/babel/pull/6952)
* Vous pouvez maintenant utiliser `envName: "something"` dans .babelrc ou passer via cli `babel --envName=something` au lieu d'avoir à utiliser `process.env.BABEL_ENV` ou `process.env.NODE_ENV`
* `["transform-for-of", { "assumeArray": true }]` pour faire en sorte que toutes les boucles for-of sortent sous forme de tableaux réguliers
* Exclure `transform-typeof-symbol` en mode loose pour preset-env [#6831](https://github.com/babel/babel/pull/6831)
* [PR atterri pour de meilleurs messages d'erreur avec les erreurs de syntaxe](https://twitter.com/left_pad/status/942859244759666691)

#### À faire avant la sortie

* [Gérer](https://github.com/babel/babel/issues/6766) la [recherche](https://github.com/babel/babel/issues/6766) de `[.babelrc](https://github.com/babel/babel/issues/6766)` (vouloir que cela soit fait avant la première sortie RC)
* [Support des "overrides"](https://github.com/babel/babel/pull/7091) : configuration différente basée sur le motif glob
* Logique de mise en cache et d'invalidation dans babel-core.
* Meilleure histoire autour des helpers externes.
* Soit implémenter ou avoir un plan en place pour le versionnage et la gestion des polyfills indépendamment des helpers, afin que nous ne soyons pas explicitement liés à core-js 2 ou 3. Les gens peuvent avoir des choses qui dépendent de l'un ou de l'autre, et ne voudront pas charger les deux la plupart du temps.
* Soit une [implémentation de décorateur fonctionnelle](https://github.com/babel/babel/pull/6107), ou une implémentation héritée fonctionnelle, avec un chemin clair pour atterrir le comportement actuel de la spécification pendant la durée de vie de 7.x.

#### Remerciements

Un grand merci à notre équipe de bénévoles :

[Logan](https://twitter.com/loganfsmyth) a vraiment travaillé dur pour corriger beaucoup de nos problèmes principaux concernant les configurations et plus encore. C'est lui qui fait tout ce travail acharné.

[Brian](https://twitter.com/existentialism) a repris la maintenance de beaucoup de travail sur preset-env et tout ce que je faisais avant ?

[Daniel](https://twitter.com/TschinderDaniel) a toujours été là quand nous avions besoin d'aide, que ce soit pour maintenir babel-loader ou aider à déplacer les dépôts babylon/babel-preset-env. Et pareil pour [Nicolo](https://twitter.com/NicoloRibaudo), [Sven](https://twitter.com/svensauleau), [Artem](https://twitter.com/yavorsky_), et [Diogo](https://twitter.com/kovnsk) qui se sont impliqués au cours de la dernière année pour aider.

Je suis vraiment impatient pour une sortie (je suis fatigué aussi — cela fait presque un an ?). Mais je ne veux pas non plus précipiter quoi que ce soit juste parce que. Il y a eu beaucoup de hauts et de bas tout au long de cette sortie, mais j'ai certainement appris beaucoup et je suis sûr que le reste de l'équipe aussi.

Et si j'ai appris quoi que ce soit cette année, je devrais vraiment suivre ce conseil plutôt que de juste en parler.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">"Avant de maintenir autre chose, maintenez d'abord votre propre corps" - Maman ?</p>&mdash; Henry Zhu (@left_pad) <a href="https://twitter.com/left_pad/status/944313617243099136?ref_src=twsrc%5Etfw">22 décembre 2017</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


> Merci aussi à [Mariko](https://twitter.com/kosamari) pour la [petite poussée](https://twitter.com/kosamari/status/944272286055530496) pour enfin terminer ce post (2 mois en préparation)