---
title: De Zéro à Héros Interplanétaire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T18:53:56.000Z'
originalURL: https://freecodecamp.org/news/from-zero-to-interplanetary-hero-7e62f7d4427
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GGQAuJS_S0gonQc3goq0Vw.png
tags:
- name: Blockchain
  slug: blockchain
- name: dapps
  slug: dapps
- name: ipfs
  slug: ipfs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: De Zéro à Héros Interplanétaire
seo_desc: "By Carson Farmer\nA fun guide to getting started with browser-based ĐApps\
  \ on IPFS\n\n_[â€œIf you can read this, congratulationsâ€”the archive youâ€™re using\
  \ still knows about the mouseover textâ€\x9D!](https://xkcd.com/1683/\" rel=\"noopener\"\
  \ target=\"blank\" ..."
---

Par Carson Farmer

#### Un guide amusant pour commencer avec les ÐApps basées sur navigateur sur IPFS

![Image](https://cdn-media-1.freecodecamp.org/images/1*GGQAuJS_S0gonQc3goq0Vw.png)
_[Si vous pouvez lire ceci, félicitations l'archive que vous utilisez connaît encore le texte au survol de la souris!](https://xkcd.com/1683/" rel="noopener" target="_blank" title=")_

Les [ÐApps](https://en.wikipedia.org/wiki/DAPP), ou applications décentralisées, sont très populaires en ce moment, particulièrement sur la [blockchain Ethereum](https://www.ethereum.org/). Mais saviez-vous que les ÐApps peuvent également fonctionner sur le [Système de Fichiers Interplanétaire (IPFS)](https://ipfs.io/)? Oui, et c'est beaucoup plus facile que vous ne le pensez pour en lancer une rapidement.

Dans cet article, nous allons passer en revue les étapes nécessaires pour lancer rapidement et facilement une ÐApp basée sur IPFS. Nous allons profiter de certains nouveaux outils navigateurs IPFS cool, et de ma bande dessinée en ligne préférée. En faisant cela, nous allons aider à archiver une ressource précieuse ([xkcd](https://xkcd.com/)!) pour les visiteurs futurs. Donc cet article a tout : intrigue, excitation, et un engagement pour l'avenir du web!

### Archiver les pépites du web

L'objectif de ce tutoriel est de créer un clone web distribué du [site web xkcd](https://xkcd.com/). Nous allons utiliser IPFS pour récupérer des images à partir d'une archive de bandes dessinées xkcd, et les afficher sous une forme familière aux fans de xkcd.

Il y a plusieurs raisons pour lesquelles nous pourrions vouloir faire quelque chose comme cela. Premièrement, j'aime les bandes dessinées xkcd, et je cherche toujours une excuse pour jouer avec elles. Deuxièmement, xkcd, ainsi que plusieurs autres ressources archivées, sont disponibles via [les archives IPFS](https://archives.ipfs.io/), ce qui en fait un exemple pratique. Troisièmement, et c'est important, la construction de ÐApps basées sur le contenu sur IPFS peut aider à archiver le web!

Que veux-je dire par là? Eh bien, les tendances changent, les intérêts s'estompent, et Internet est un endroit capricieux. Couplez cela avec les coûts croissants de maintien des serveurs, de mise à jour des infrastructures, et de suivi des dernières tendances, et vous avez une recette pour des liens morts. IPFS et le web distribué sont un excellent moyen de aider à combattre [la pourriture des liens](https://en.wikipedia.org/wiki/Link_rot).

Prenons notre ÐApp xkcd par exemple. Dans un instant, nous allons écrire un JavaScript très simple qui chargera une bande dessinée xkcd aléatoire chaque fois que notre ÐApp est accessible. Et ainsi, chaque fois que quelqu'un visite la ÐApp, le pair fonctionnant dans son navigateur récupère cette bande dessinée, et la met temporairement en cache, ce qui permet aux autres de la récupérer également. En fait, plus nous utilisons la ÐApp, mieux elle est capable de distribuer et d'archiver xkcd.

> Plus nous accédons et utilisons des choses sur le web distribué via IPFS, plus elles sont susceptibles de rester longtemps  [tweetez-le](https://twitter.com/home?status=The%20more%20we%20access%20and%20use%20things%20on%20the%20distributed%20web%20via%20IPFS,%20the%20more%20likely%20they%20are%20to%20stick%20around%20long-term%20-%20%40carsonfarmer%20https%3A//medium.com/%40carsonfarmer/from-zero-to-interplanetary-hero-7e62f7d4427)

C'est une idée vraiment puissante : plus nous accédons et utilisons des choses sur le web distribué via IPFS, plus elles sont susceptibles de rester longtemps. Et qu'en est-il des choses qui sont importantes mais moins _populaires_ (comme les documents historiques)? C'est là que des choses comme [Filecoin](https://filecoin.io/) aideront à combler le manque. Dans le [monde de Filecoin](https://coincentral.com/filecoin-beginners-guide-largest-ever-ico/), plutôt que de compter sur la popularité pour préserver les documents et les fichiers, vous pouvez payer le réseau pour stocker ces choses pour vous. C'est une idée très cool.

### Commencer

Pour ceux d'entre vous qui ne peuvent pas attendre, la ÐApp complète est disponible sur le [dépôt GitHub Textile](https://github.com/textileio/xkcd-dapp-demo). N'hésitez pas à la cloner et à suivre le code pour faciliter le démarrage. Et puisque vous venez de vous économiser du temps, pourquoi ne pas [regarder cette excellente vidéo](https://www.youtube.com/watch?v=HUVmypx9HGI) sur la vision IPFS de Juan Benet avant de continuer. Vous pouvez également consulter une [version live ici](https://ipfs.carsonfarmer.com/ipfs/QmYDEzjNKm6ZMCmQVVRAJqPnGL2H7c4EK81LBTK3GC4kCh/).

Pour ceux d'entre vous qui veulent une approche étape par étape, voici quelques étapes d'installation pour vous aider à démarrer.

Tout d'abord, clonez notre modèle IPFS vanilla [Dapp Template](https://github.com/textileio/dapp-template), et changez dans le nouveau répertoire:

```
git clone https://github.com/textileio/dapp-template.git xkcd-dappcd xkcd-dapp
```

Ce modèle est assez simple et a des [dépendances](https://github.com/textileio/dapp-template/blob/carson/xkcd-demo/package.json) assez minimales. La plupart des dépendances de développement sont juste pour transpiler JavaScript afin que nous puissions exécuter notre ÐApp dans le navigateur. Pour plus de détails sur tous ces packages, consultez leurs dépôts GitHub respectifs, ou [contactez-nous](https://www.textile.io/) pour poser une ou deux questions.

Donc, première chose à faire, consultez le fichier `README.md` du dépôt. Vous remarquerez qu'il dit que cette application fonctionne mieux avec `window.ipfs`, et que vous pouvez installer l'extension web [IPFS Companion](https://github.com/ipfs-shipyard/ipfs-companion) en cliquant sur l'un des liens.

L'extension IPFS Companion est une extension de navigateur qui simplifie l'accès aux ressources IPFS en exécutant un [pair IPFS JavaScript](https://github.com/ipfs/js-ipfs) dans votre navigateur. Encore mieux, elle peut exposer un nœud IPFS intégré en tant que `window.ipfs` sur chaque page web! Cela permet à notre ÐApp de détecter si `window.ipfs` existe et d'opter pour l'utiliser au lieu de créer notre propre nœud `js-ipfs` ponctuel. Ce n'est pas _requis_ pour exécuter les ÐApps, mais cela les fait mieux fonctionner (plus rapidement), et je recommande vivement de l'installer.

Cependant, nous ne pouvons pas nous attendre à ce que les utilisateurs de notre ÐApp installent une extension de navigateur avant de pouvoir utiliser notre ÐApp. Il existe donc un module JavaScript appelé `[window.ipfs-fallback](https://github.com/tableflip/window.ipfs-fallback)`, qui détectera la présence de `window.ipfs` et basculera automatiquement vers le téléchargement de la [dernière version d'IPFS](https://unpkg.com/ipfs/dist/index.min.js) depuis le CDN si elle n'est pas disponible. Donc, lors de la création d'une ÐApp, il est toujours bon de l'inclure  et vous obtenez `window.ipfs` gratuitement si disponible. Super!

D'accord, alors pour s'assurer que tout fonctionne bien, installons nos dépendances requises, et construisons et exécutons notre ÐApp localement. Entrez ce qui suit dans votre terminal:

```
yarn installyarn buildyarn start
```

Vous devriez voir une ÐApp assez minimale (page blanche) avec un pied de page et pas grand-chose d'autre. Maintenant, ouvrez votre console de développement JavaScript (Chrome:Ctl+Shift+J(Command+Option+Jon Mac), Firefox: Ctrl+Shift+K(Command+Option+Kon Mac), Safari: Command+Option+I). Vous devriez voir quelque chose comme `running js-ipfs/0.29.2 with ID Qm{hash}` où `Qm{hash}` est un long hash alphanumérique qui représente votre identifiant de pair.

Félicitations, vous exécutez avec succès une ÐApp sur le web décentralisé! Maintenant, faisons-en quelque chose d'intéressant...

### Récupération de données sur le web distribué

D'accord, ajoutons quelques fonctionnalités à notre ÐApp. Nous allons commencer par simplement récupérer une bande dessinée xkcd aléatoire et l'afficher sur une page blanche. Assez simple, non? Tout d'abord, plutôt que de `yarn start` notre application, `yarn watch` la afin que toute modification que nous apportons au JavaScript soit automatiquement reflétée lorsque nous actualisons notre fenêtre de navigateur.

Maintenant, vous pouvez modifier la fonction `setup` dans `src/main.js` avec le code suivant:

Il y a beaucoup à analyser là, mais en gros ce qui se passe est:

* Les lignes 3 & 5 définissent _quelle_ bande dessinée aléatoire récupérer ([à partir de notre archive](https://ipfs.io/ipfs/QmWEAXcqwq5zY2u8Z1mii5m3MXricctd7efFep7sSEWZQz))
* Les lignes 8 & 10 initialisent un nœud pair IPFS, et se connectent à un pair connu pour épingler l'archive xkcd (cette deuxième étape n'est pas toujours requise, mais je l'ai ajoutée ici pour aider à démarrer la ÐApp)
* La ligne 14 est vraiment la magie IPFS... elle récupère les fichiers à l'identifiant CID donné et retourne une promesse, que nous attendons et avec laquelle nous faisons un peu de travail dans les lignes 15 à 27...
* Les lignes 15 & 16 parcourent simplement les objets binaires retournés par l'étape précédente, et recherchent l'image png réelle
* Les lignes 18 & 20 convertissent les données d'image binaires en une chaîne encodée en base64
* Et enfin, les lignes 22 à 27 créent un élément image et l'ajoutent à la div main pour l'affichage.

Terminé!

### Nettoyer les choses

À partir de là, toute modification supplémentaire est simplement pour faire en sorte que la ÐApp ressemble et se sente plus comme la page web originale de la bande dessinée xkcd.

Je ne vais pas entrer dans les détails dans cet article, mais vous pouvez jeter un coup d'œil dans le dépôt [xkcd-dapp-demo](https://github.com/textileio/xkcd-dapp-demo) pour l'exemple de code complet. Là, j'ai ajouté les boutons de navigation et le style du site web xkcd, ainsi que des liens vers [l'attribution appropriée](https://ipfs.io/ipfs/QmWEAXcqwq5zY2u8Z1mii5m3MXricctd7efFep7sSEWZQz/about.html), [les informations de licence](https://ipfs.io/ipfs/QmWEAXcqwq5zY2u8Z1mii5m3MXricctd7efFep7sSEWZQz/license.html), et d'autres goodies. Nous avons même les commentaires amusants au survol! C'est presque tout du JavaScript ES6 vanilla, et je tire bon parti des [modèles async/await](https://davidwalsh.name/async-await) pour rendre le code agréable et lisible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2DSOGJ4sBp5Njb7hN3RF_Q.png)

Donc, comme vous pouvez le voir, il est relativement facile de commencer à créer des ÐApps sur IPFS. Notre ÐApp xkcd fonctionne mieux lorsqu'elle est exécutée a) localement (via `yarn start` par exemple), et b) avec l'extension de navigateur IPFS Companion activée. Si vous le souhaitez, vous pouvez en fait lancer un démon IPFS local, et exécuter `ipfs add -r dist/`, pour ajouter toute la ÐApp à IPFS. Maintenant, vous pouvez la tester via votre passerelle IPFS locale: `http://localhost:5001/ipfs/Qm{hash}/` (si votre code n'est pas identique au mien, votre hash CID peut différer, utilisez celui sorti de la commande `ipfs add` ci-dessus).

### Conclusion

Nous espérons que [notre modèle](https://github.com/textileio/dapp-template) fournira un moyen rapide et facile de démarrer des ÐApps supplémentaires, et que la communauté des ÐApps basées sur IPFS continuera de croître. Chez [Textile](https://www.textile.io/), nous aimerions vraiment soutenir une communauté de ÐApps autour d'IPFS, donc si vous décidez d'utiliser notre modèle, faites-le nous savoir, et nous serions ravis d'ajouter un lien à [notre dépôt de modèles](https://github.com/textileio/dapp-template/blob/master/README.md). Nous garderons également un œil sur les forks et essayerons de les promouvoir autant que possible.

Nous espérons que vous avez apprécié notre rapide introduction aux ÐApps sur IPFS. Si vous avez aimé cela, venez [nous rendre visite](https://www.textile.photos/) et en savoir plus sur ce que nous faisons. Pendant que vous y êtes, inscrivez-vous sur la [liste d'attente de Textile Photos](https://www.producthunt.com/upcoming/textile-photos) pour demander un accès anticipé à une toute nouvelle façon de contrôler vos photos, qui fonctionne également sur IPFS et le web permanent.