---
title: L'introduction la plus facile au monde à WebAssembly ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-28T15:28:38.000Z'
originalURL: https://freecodecamp.org/news/webassembly-with-golang-is-fun-b243c0e34f02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XLrgliUgUebeFCVrZ--o2g.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: golang
  slug: golang
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: L'introduction la plus facile au monde à WebAssembly ?
seo_desc: 'By Martin Olsansky (olso)

  WASM in Golang for JavaScript developers.


  An interactive <canvas> laser game for cats ? on your phone ?written completely
  in Golang. Being inspected by Matsu ?


  Do you think that WebAssembly (WASM) is only used for image ma...'
---

Par Martin Olsansky (olso)

#### WASM en Golang pour les développeurs JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XLrgliUgUebeFCVrZ--o2g.jpeg)
_Un jeu laser interactif sur &lt;canvas&gt; pour chats ? sur votre téléphone ? écrit entièrement en Golang. Inspecté par Matsu ?_

* Pensez-vous que WebAssembly (WASM) n'est utilisé que pour la manipulation d'images, les mathématiques complexes ou d'autres cas d'utilisation de niche sur le web ?
* Confondez-vous toujours WASM avec `Web Workers` et `Service Workers` ?
* Pas intéressé parce que vous pensez que les applications web JavaScript développées aujourd'hui devront encore être maintenues pendant les 10 prochaines années ?
* Voulez-vous faire du développement web frontend dans des langages autres que JS ?

_Pour ceux qui parcourent rapidement, voici les liens vers la [**démo**](https://olso.space/go-wasm-cat-game-on-canvas/index.html) ou **/[src](https://github.com/olso/go-wasm-cat-game-on-canvas-with-docker)** ?. "[Lire/écrire est une transaction](http://www.perell.com/blog/coolest-things-2018#block-yui_3_17_2_1_1546345205921_226865)", je vais essayer de ne pas perdre votre temps. Il y a des g`ists` avec des commentaires explicatifs dans le code._

### Scénario ?

Notre objectif est de créer un simple jeu pour chats ?: déplacer un laser rouge sur mobile avec quelques ? effets audio et vibrations. Nous allons tout implémenter en Go[lang (](https://golang.org)Go), y compris la manipulation du DOM, la logique et l'état.

_Aaaaaand puisque les chats ne peuvent pas utiliser une souris, nous aurons besoin d'une interaction tactile pour ces pattes de chat ?._

#### Introduction expliquée !

Pensez à WASM comme la [Machine Virtuelle Universelle](https://webassembly.org/docs/use-cases/) (sandbox), où vous écrivez UN SEUL code, et il s'exécute partout.

WASM est une cible de compilation, pas un langage. Comme si vous deviez compiler pour Windows, Mac OS et Linux en même temps !

Je ne pense pas que WASM soit là pour détrôner JS, il s'agit d'avoir des alternatives sans aucun sacrifice.

Imaginez toutes les personnes qui développent en _Go, Swift, Rust, Ruby, C++, OCaml ou autres_. Maintenant, ils peuvent utiliser leur langage préféré pour créer des sites web et des applications web interactifs, en réseau, rapides et capables de fonctionner hors ligne.

Avez-vous déjà participé à une discussion sur le fait que votre projet sera un mono-dépôt ou un multi-dépôt ?

**Vous allez maintenant aussi avoir une discussion sur le fait que votre projet est mono-langage ou multi-langage.**

Lorsque les gens peuvent travailler avec la même pile technologique, tout devient plus facile. Surtout la communication entre les équipes.

Vous pouvez toujours utiliser React, Vue mais maintenant vous n'êtes plus obligé d'utiliser JS.

#### Comment WASM est-il différent des Service et Web Workers ?

`Service & Web Workers` vous permettent d'exécuter des processus en arrière-plan, hors ligne et de mise en cache. Ils imitent le threading, n'ont pas accès au DOM et ne peuvent pas partager les données (uniquement via messagerie) et s'exécutent dans un contexte séparé. En fait, vous pourriez même exécuter WASM au lieu de JS dans ceux-ci. Pour moi, ils ne fournissent qu'une couche d'abstraction avec des privilèges spéciaux, personne n'a dit que ces couches devaient exécuter JS.

> `_Service & Web Workers_` sont une fonctionnalité du navigateur, ils ne sont pas une fonctionnalité exclusive de JS.

### Configurer l'environnement de développement ?

Nous allons utiliser WASM, Go, JS et (optionnellement) Docker ?.

Si vous ne connaissez pas Go mais connaissez JS, [apprenez Go](https://nemethgergely.com/learning-go-as-a-nodejs-developer/) puis revenez ici. Commençons par aller sur le [wiki Go WASM](https://github.com/golang/go/wiki/WebAssembly).

Utilisez votre `go` local, j'utilise l'image Docker `golang:1.12-rc`. Il suffit de définir deux indicateurs WASM pour le compilateur `go` ici. Créez un simple [hello world](https://gobyexample.com/hello-world) dans `main.go` pour le tester.

```
$ GOOS=js GOARCH=wasm go build -o game.wasm main.go
```

Maintenant, récupérez le `[wasm_exec.js](https://github.com/golang/go/blob/master/misc/wasm/wasm_exec.js)` fourni par l'équipe Go. Ce `Go` global abstrait l'initiation WASM. Nous n'avons pas à créer une abstraction DOM à partir de zéro ?. Enfin, f`etch` le fichier .`wasm` et exécutez notre jeu.

En résumé, cela devrait ressembler à ceci :

### Montrez-moi le code Go déjà !

Pour rendre notre simple jeu, `<canv`as> devrait suffire. Nous pouvons créer la structure et les éléments DOM directement à partir du code Go ! `[That sysc](https://github.com/golang/go/tree/master/src/syscall/js)`all/js (inclus en tant que package Go standard) gère l'interaction DOM pour nous.

#### main()

Je parie que vous n'avez pas vu `main()` depuis longtemps ?.

Cela ressemble beaucoup à JS, n'est-ce pas ?

Oui, c'est tout ce dont vous avez besoin pour interagir avec le `DOM` ! Juste quelques fonctions `Get` et `Call` pour l'instant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QBGaRFL9RDLQ-y2BnY5iDg.png)
_Oh mama ? Il est là !_

À ce stade, je me demandais. J'écris encore une sorte de JS d'une certaine manière... comment est-ce une amélioration ? Parce que nous n'avons pas encore d'accès direct au DOM, nous devons recourir à l'appel du DOM (via JS) afin de faire quoi que ce soit. Imaginez comment vous pourriez abstraire cela avec, par exemple, JSX/React. _En fait, vous pouvez déjà le faire, mais laissons cela pour mon prochain article_ ?.__

#### "Rendu" et la gestion des événements

L'utilisation directe de la bibliothèque `syscall/js` révèle certains callbacks de type ES5. Nous sommes capables d'écouter les événements DOM. Cela semble très propre avec ces types statiques !

#### Journalisation, Audio et "async"

En Go, il y a une convention pour écrire toutes les `func` de manière synchrone. C'est à l'appelant de décider si `func` est asynchrone. Rendre une `func` asynchrone est vraiment facile. Il suffit de la préfixer avec `go` et voilà ! Cela crée un thread avec son propre contexte. Vous pouvez toujours lier le contexte parent à celui-ci, ne vous inquiétez pas.

#### Exécuter notre jeu pour toujours ! F6E0

Ce code crée un canal non tamponné et tente de recevoir à partir de celui-ci. Et puisque personne n'envoie jamais rien dessus, c'est essentiellement une opération de blocage pour toujours, nous permettant d'exécuter notre programme pour toujours.

#### Mettre à jour l'état du jeu et déplacer le laser rouge

Aucune gestion d'état à voir ici, juste une `struct` typée simple, qui ne vous permet pas de passer des valeurs incorrectes à l'intérieur.

### Conclusion

Le fait que WASM soit encore considéré comme un [MVP](https://hacks.mozilla.org/2018/10/webassemblys-post-mvp-future/) (MAP) et que vous puissiez créer un jeu comme celui-ci, sans écrire une seule ligne de JS, est incroyable ! [CanIUse](https://caniuse.com/#feat=wasm) est déjà entièrement vert, il n'y a rien qui vous empêche de construire des sites web et des applications alimentés par WASM.

Regardez, vous pouvez combiner tous les langages que vous voulez, même JS -> WASM. À la fin, ils seront tous compilés en bytecode WASM. Si vous devez partager quelque chose entre eux, vous pouvez, car ils peuvent partager une mémoire brute.

Ce qui me fait peur, c'est que dans les nouvelles récentes, nous avons appris que [Microsoft construit un navigateur Chromium](https://news.ycombinator.com/item?id=18595069) et que [la part de marché de Firefox est inférieure à 9 %](https://news.ycombinator.com/item?id=18595025). Cela donne à Google un pouvoir de kill switch sur WASM. S'ils ne suivent pas, les masses ne le sauront peut-être jamais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UGmDc4xve13Yws3WEe8Hrg.gif)
_Gameplay ?_

#### Qui utilise déjà WASM ?

D'accord, mon exemple ne fait que dessiner un `canvas` en pleine page. Voici des exemples plus avancés qui se concentrent sur le web sémantique [awesome-wasm#web-frameworks-libraries](https://github.com/mbasso/awesome-wasm#web-frameworks-libraries).

Plusieurs projets ont déjà sauté dans le train WASM. Certains des plus intéressants pour moi sont Spotify, Twitch, [Figma](https://www.figma.com/blog/webassembly-cut-figmas-load-time-by-3x/) et [EWASM](https://github.com/ewasm).

#### WASM à l'ère du Web3

De nos jours, si vous voulez utiliser un portefeuille Ethereum sur le web mobile, vous devez télécharger un portefeuille mobile comme Status.im à partir d'un App Store centralisé et faire confiance à toutes les parties.

Et si une Progressive Web App exécutait `geth` (client Ethereum Go) avec une synchronisation légère sur WebRTC ? Elle pourrait utiliser `Service Worker` pour mettre à jour son code WASM et l'exécuter en arrière-plan, pourrait être hébergée sur IPFS/Dat.

### Articles, ressources et goodies WASM utiles ?

* [WebAssembly est plus que le web](https://words.steveklabnik.com/webassembly-is-more-than-just-the-web)
* [WebAssembly et Go : Un regard vers l'avenir](https://www.brianketelsen.com/web-assembly-and-go-a-look-to-the-future/) et les [commentaires HN](https://news.ycombinator.com/item?id=17381816)
* articles de [Mozilla Hacks](https://hacks.mozilla.org/category/webassembly) et [Hacker News](https://hn.algolia.com/?query=wasm&sort=byDate&prefix&page=0&dateRange=all&type=story)
* [Architecture WebAssembly pour Go](https://docs.google.com/document/d/131vjr4DH6JFnb-blm_uRdaC0_Nv3OUwjEY5qVCxCup4/edit)

[**awesome-wasm**](https://github.com/mbasso/awesome-wasm), [awesome-wasm-langs](https://github.com/appcypher/awesome-wasm-langs), [gowasm-experiments](https://github.com/stdiopt/gowasm-experiments), [**WasmWeekly**](https://twitter.com/wasmweekly), [WasmRocks](http://www.wasmrocks.com/), [SPA avec C++](https://github.com/mbasso/asm-dom#examples), [meilleures liaisons DOM pour Go](https://github.com/dennwc/dom)

Merci à [https://github.com/twifkak](https://github.com/twifkak) pour l'optimisation de Go sur Chrome pour Android !

### Prochain article ? F4DDF3FB

Nous allons examiner l'interopérabilité avec les modules JS et React. Restez à l'écoute !

_Si vous avez aimé et que vous souhaitez voir plus de contenu, n'oubliez pas de suivre et de continuer à appuyer sur ce bouton d'applaudissements_ ?.

### À propos de moi F6A1F3FB

Salut, je suis **Martin Olsansky** _(olso)_. Si vous avez des questions/suggestions, n'hésitez pas à me contacter à [**https://olso.space**](https://olso.space) ou @[olso_uznebolo](https://twitter.com/olso_uznebolo)

Je m'intéresse également à [DIYBio](http://sphere.diybio.org), [Écosystèmes/plantes augmentés par la technologie](https://terra0.org/), [Données des patients ouvertes et santé numérique](https://events.ccc.de/congress/2018/wiki/index.php/Session:Digital_Health_and_Patient_Data), Cryptomonnaies, Web3, P2P.