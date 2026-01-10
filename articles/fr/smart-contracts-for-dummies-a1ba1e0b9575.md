---
title: Les Smart Contracts pour les Nuls
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-26T12:01:00.000Z'
originalURL: https://freecodecamp.org/news/smart-contracts-for-dummies-a1ba1e0b9575
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lsZWlQRE0lWRLzx-BpxR8A.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: ICO
  slug: ico
- name: technology
  slug: technology
seo_title: Les Smart Contracts pour les Nuls
seo_desc: 'By Nik Custodio

  If you still don’t get what the heck a Smart Contract is…


  Ok, you know a bit about Bitcoin (see: Explain Bitcoin Like I’m Five). You’ve been
  seeing the blockchain on the news.

  But what’s this new Ethereum thing? Apparently it’s this ...'
---

Par Nik Custodio

#### **Si vous ne comprenez toujours pas ce qu'est un Smart Contract...**

![Image](https://cdn-media-1.freecodecamp.org/images/1*lsZWlQRE0lWRLzx-BpxR8A.jpeg)

D'accord, vous connaissez un peu le Bitcoin (voir : [Explain Bitcoin Like I’m Five](https://medium.com/@nik5ter/explain-bitcoin-like-im-five-73b4257ac833)). Vous avez vu la blockchain dans les nouvelles.

Mais qu'est-ce que ce nouveau truc [**Ethereum**](https://www.nytimes.com/2017/02/27/business/dealbook/ethereum-alliance-business-banking-security.html) ? Apparemment, c'est une crypto-monnaie que vous pouvez utiliser pour construire des "smart contracts". Ça a l'air impressionnant. Alors, eh... qu'est-ce que c'est encore ? _(Spoiler : Ils ne sont pas si intelligents. Et ce ne sont pas vraiment des contrats !)_

Au lieu d'une définition en une ligne, essayons de comprendre intuitivement. D'abord, nous allons revisiter la _blockchain_ et le mot "confiance". Ensuite, nous parlerons du mot "contrat". Comprendre ces deux mots est la clé.

### Partie I : Ce que nous entendons par "Confiance(sans)"

La plupart du temps, lorsque nous pensons au Bitcoin (ou à Ethereum), nous avons une image mentale de, eh bien..._pièces_.

Ne sont-ce pas des _crypto-monnaies_ après tout ? N'est-ce pas le but ? Dans notre esprit, nous voyons des objets — de l'or numérique, ou de l'argent (ou des tulipes pour les sceptiques).

Parce que ces images sont faciles à comprendre, nous oublions un peu cette _chose_ qui est sous-jacente. Alors, je dis que nous devrions commencer à penser à cela différemment.

### **_Pierre Numérique_**

![Image](https://cdn-media-1.freecodecamp.org/images/1*iU2aL8uUyDD5Sqg66Bo9Tw.jpeg)

Beurk, vraiment ? Des rochers numériques ? En fait, les rochers sont assez utiles.

Nous avons cette expression en anglais qui dit quelque chose comme ceci : "graver dans la **pierre**".

> "J'ai révisé le contrat Bob. Ça a l'air bien. Gravons cela dans la pierre !"

> "Ne t'emballe pas trop Alice, rien n'est encore gravé dans la pierre."

> "C'est Dieu. J'ai écrit mes 10 commandements sur ces deux tablettes de pierre. Vous savez. Juste au cas où vous auriez des idées drôles."

Cette métaphore continue d'avoir du sens dans un monde moderne parce que dans le monde physique (ancien), la pierre avait certaines propriétés intéressantes :

1. Lorsque vous gravez quelque chose sur la pierre, il y a une **_finalité et permanence_** physique. Vous ne pouvez pas faire des changements comme ça.
2. Si vous essayez d'"effacer" quelque chose plus tard, ce sera évident. Tout changement que vous apportez est assez **_transparent et inviolable (prouvable)_**.
3. Ces règles s'appliquent à tous de la même manière. La pierre est **_neutre_**. Elle obéit aux lois de la physique, pas aux hommes. Elle ne se soucie pas de savoir si vous êtes un roi puissant ou un paysan — elle se comporte exactement de la même manière pour tout le monde.

À cause de toutes ces propriétés, nous avons un niveau de **_confiance assez élevé_** dans la pierre.

Je veux dire — il y a une raison pour laquelle nous ne disons jamais "gravons cet accord dans le **_sable_**". La pierre est le genre de chose à laquelle je peux me référer dans le futur comme preuve. La pierre égale preuve solide — pas n'importe quel matériau ne fera l'affaire !

![Image](https://cdn-media-1.freecodecamp.org/images/1*8sfxhyikasLgeiUpNBa1iw.jpeg)
_[The Economist](http://www.economist.com/news/leaders/21677198-technology-behind-bitcoin-could-transform-how-economy-works-trust-machine" rel="noopener" target="_blank" title=") est d'accord !_

En fin de compte, une blockchain est vraiment juste ce qui précède : _un type de matériau qui, grâce à un mélange spécial de cryptographie et de décentralisation, a les propriétés de permanence, de transparence et de neutralité — quoi que vous y mettiez._

Que ce soit une liste du nombre de pommes que vous avez envoyées à Joe. Ou les mots "J'aime Jenny." Peu importe. Lorsque vous le mettez sur une blockchain — c'est _fait_.

> **Mettre quelque chose sur une blockchain, c'est comme le graver dans la pierre. Cela facilite la confiance.**

Sauf que maintenant nous pouvons le faire _numériquement_. Et c'est assez spécial.

Penser à une blockchain comme à un morceau de pierre sur lequel vous pouvez écrire des choses (au lieu d'une pièce de monnaie) nous aide également à comprendre son potentiel large. Ce qui nous amène aux... contrats !

### Partie II : Ce que nous entendons par "Contrats"

Le mot "contrat" a beaucoup de connotations. Nous commençons à penser : documents juridiques et avocats.

La description courante utilisée dans les nouvelles est un peu meilleure : des choses qui s'"exécutent automatiquement" ou s'"auto-exécutent". Cela semble vaguement familier. Après tout, il n'y a vraiment rien de nouveau dans l'"automatisation" ou l'"exécution".

#### Le grand-père des smart contracts

Prenez votre bon vieux distributeur automatique de bureau, par exemple. C'est une machine "stupide" qui fait ce qu'on lui dit et exécute les choses automatiquement. Elle existe depuis des décennies !

![Image](https://cdn-media-1.freecodecamp.org/images/1*U73m4z7Tl3fQVtAThldjGg.png)
_Voici, la machine magique qui crache des aliments riches en fructose._

Faisons semblant qu'un après-midi, vous vous retrouvez devant cette machine. Elle dit : **"Si vous me donnez 2,50 $ et que vous appuyez sur ce bouton, vous obtiendrez un Coca Light."**

Elle ne dit peut-être pas réellement ces mots quelque part. Mais c'est la promesse de cette petite interaction. On pourrait même appeler cela une sorte d'"accord" simple. (Vous pouvez deviner où cela nous mène.)

Vous insérez l'argent. Vous appuyez sur le bouton. Presto ! Bouteille en main, vous oubliez cet événement sans importance dans votre vie 2 secondes plus tard et vous recommencez à vous inquiéter de ces rapports TPS que vous avez oubliés.

Eh bien, vous ne l'avez pas remarqué, mais toute cette affaire était en fait un petit programme ("contrat") codé ("écrit") dans la machine à l'avance qui s'est exécuté lorsque vous avez appuyé sur le bouton ("signé"). Quelque chose comme :

```
> si argent reçu == 2,50 $ 
>     && le bouton pressé est "Coca Light"
> alors libérer Coca_Light
```

Le code informatique, comme vous le voyez, est _un peu_ comme un **_contrat_**.

Il fait des déclarations. Il y a des termes (si vous faites cela... alors...). Et tout comme quelqu'un en qui vous avez confiance — il remplit même sa part du marché !

Voilà. Les contrats sont juste du code. Mais contrairement à un "contrat" en anglais, c'est quelque chose que les humains _et_ les machines peuvent lire. Extra amusant !

#### D'accord, mais...

Maintenant, vous êtes encore plus confus à propos de ces smart contracts. Comme nous l'avons dit, ce n'est rien de spécial. En fait, comme le démontre le distributeur automatique, ce type de code _est_ déjà partout dans notre vie quotidienne. Si un smart contract est juste du code "si... alors" (ou _n'importe quel_ code d'ailleurs), alors quel est le battage ? Qu'est-ce qui est réellement _nouveau_ ?

### Distributeurs Automatiques 2.0

![Image](https://cdn-media-1.freecodecamp.org/images/1*fhtPA_xZNCEwq1SMzYS2rw.jpeg)

Un jour ensoleillé, vous repérez un distributeur automatique au coin de la rue. Vous n'avez jamais vu celui-ci auparavant !

Vous vous approchez et regardez. Cette machine dit : **"Si vous mettez 1 000 $ dans cette machine, elle vous donnera 5 000 $."**

Waouh ! Celui qui a assemblé cette machine doit être très riche et généreux. (Ou insensément stupide...). Dans tous les cas. 1k pour 5k ? Pas besoin de réfléchir — c'est une affaire que vous accepterez n'importe quel jour ! N'est-ce pas ?

C'est exactement comme notre bon vieux distributeur de Coca Light. Même logique. Même processus si-alors.

Sauf que maintenant les enjeux sont différents. Vous atteignez votre poche mais soudain, vous vous sentez hésitant. Qui diantre a assemblé cette machine de toute façon ? Et si elle avale votre argent ? 1 000 $ n'est pas une petite somme — vous économisiez cela depuis des mois. Vous n'avez pas hésité pour ce Coca Light. Mais maintenant ? Maintenant vous réalisez que peut-être les distributeurs automatiques ne sont pas si simples.

Vous commencez à penser à la **confiance**.

> **_Comment savons-nous qu'elle a assez de fonds pour cracher les 5 000 $ promis ?_**

> **_Comment savons-nous que le code va s'exécuter ?_**

> **_Y a-t-il un moyen de vérifier publiquement et de manière transparente ce code ?_**

### Conclusion

Le distributeur automatique de 5 000 $ est un exemple extrême et théorique, mais il suggère le problème de l'"échelle" de la confiance. Dans un monde numérique en expansion où les gens peuvent se connecter anonymement — la confiance devient une chose délicate. Nous comptons généralement sur des tiers et d'autres intermédiaires pour cette raison. Nous devons le faire. Surtout si nous déplaçons des choses bien plus précieuses que des Coca Lights. Vous savez, comme des trucs financiers nouveaux. Ou [l'idée même de "valeur" et de "propriété"](http://nikcustodio.tumblr.com/post/150500263430/why-blockchains-an-eli21) elle-même.

Hmmm. Si seulement vous pouviez marier l'automatisation de la programmation traditionnelle **_et_** les propriétés dignes de confiance de la _pierre numérique_...

Eh bien, c'est exactement ce qu'est un smart contract ! Ce n'est que du code — avec un soutien très spécial.

> Gardez à l'esprit, nous avons eu à la fois le calcul et l'exécution auparavant. _Mais jamais un qui était finalisé de manière neutre, prouvable et fiable sur de la (pierre) numérique._

#### **Et dans le monde réel ? Quelques idées.**

**Jeux en Ligne :** Lutter contre [la fraude sur les sites de jeu](http://money.cnn.com/2012/07/31/technology/online-poker-settlement/). Les chances de ce lancer de dé que vous venez de faire sont-elles _réellement_ de 1 sur 6 ? Comment savons-nous qu'ils vont payer ? Eh bien, pourquoi ne pas "graver le code dans la pierre" et le prouver ? Un exemple [en direct](https://etheroll.com/#tab7).

**Chaînes d'Approvisionnement :** Peut-être [suivre et vérifier où et comment les choses sont fabriquées ?](https://www.provenance.org/whitepaper)

**Vote :** Peut-être un processus de [vote](http://www.govtech.com/blogs/lohrmann-on-cybersecurity/can-blockchain-technology-secure-your-vote.html) inviolable ?

**Entreprises Décentralisées et Autonomes :** Temps de science-fiction.

Tout au long de l'histoire, l'automatisation a toujours été appliquée au _bas_ des entreprises. La chaîne de montage. L'ouvrier d'usine. Mais si les règles d'une entreprise sont juste une sorte de logique _opérationnelle_ — alors n'est-il pas possible d'inverser la pyramide et d'automatiser plutôt le _haut_ ?

Ce ne sont que quelques exemples de ce que vous pourriez coder sur une blockchain en utilisant le langage de programmation [Turing complet](https://www.wikiwand.com/simple/Turing_complete) d'Ethereum. Nous ne sommes qu'au début. Si vous le rêvez, vous pourriez être capable de le coder.

Et à bien des égards, c'est ce qui rend tout cela excitant. Nous avons quelques idées, mais honnêtement — nous n'avons aucune idée de ce qui sera construit dans les années et décennies à venir.

Tout ce que nous savons, c'est que les blocs de construction sont là. Et c'est ouvert à tous. Le reste dépend de vous.

#### **Prêt à plonger dans le terrier du lapin ?**

* [Un Guide du Débutant sur Ethereum](https://blog.coinbase.com/a-beginners-guide-to-ethereum-46dd486ceecf)
* [Crypto-Tokens : Une Avancée dans la Conception de Réseaux Ouverts _(Chris Dixon)_](https://medium.com/@cdixon/crypto-tokens-a-breakthrough-in-open-network-design-e600975be2ef)
* [L'Idée des Smart Contracts _(Nick Szabo, 1997)_](https://perma.cc/V6AZ-7V8W)
* [L'Autre Face de la Pièce : Une perspective différente sur les cryptomonnaies](https://medium.com/@nik5ter/the-other-side-of-the-coin-f293b65b1eda?source=linkShare-2d6f142ff3cc-1513820863)