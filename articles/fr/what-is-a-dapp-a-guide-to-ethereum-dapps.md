---
title: Qu'est-ce qu'une Dapp ? Un guide des Dapps Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T19:08:55.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-dapp-a-guide-to-ethereum-dapps
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/clifford-photography-hiFghSs4keM-unsplash.jpg
tags:
- name: dapps
  slug: dapps
- name: Ethereum
  slug: ethereum
- name: Smart Contracts
  slug: smart-contracts
seo_title: Qu'est-ce qu'une Dapp ? Un guide des Dapps Ethereum
seo_desc: 'By Grant Bartel

  In the cryptoverse, a lot of attention is laid on Bitcoin. But don''t let that overshadow
  the growing interest in Ethereum, which is revolutionizing the way we think of applications.

  So, what is a Dapp? A Dapp, or decentralized applica...'
---

Par Grant Bartel

Dans le cryptoverse, beaucoup d'attention est portée sur Bitcoin. Mais ne laissez pas cela éclipser l'intérêt croissant pour Ethereum, qui révolutionne la façon dont nous concevons les applications.

Alors, qu'est-ce qu'une Dapp ? **Une Dapp, ou application décentralisée, est une application logicielle qui fonctionne sur un réseau distribué. Elle n'est pas hébergée sur un serveur centralisé, mais plutôt sur un réseau décentralisé pair-à-pair.**

D'accord, c'est la version courte, mais il y a beaucoup plus à déballer. Plongeons dans le monde des Dapps, plus spécifiquement celles construites sur le protocole Ethereum.

## Qu'est-ce qu'Ethereum ?

Pour comprendre ce qu'est une Dapp, vous devez d'abord comprendre ce qu'est Ethereum. Maintenant, il existe d'autres protocoles utilisés pour construire des Dapps, comme EOS, NEO, Stellar, Tron et Cardano, mais le grand favori est Ethereum.

Ethereum est un protocole de réseau qui permet aux utilisateurs de créer et d'exécuter des **contrats intelligents** sur un réseau décentralisé. Un contrat intelligent contient du code qui exécute des opérations spécifiques et interagit avec d'autres contrats intelligents, qui doit être écrit par un développeur. Contrairement à Bitcoin qui stocke un nombre, Ethereum stocke du code exécutable.

Alors, pourquoi devriez-vous vous en soucier ?

Parce qu'Ethereum élimine le besoin d'un tiers pour gérer les transactions entre pairs. Puisque l'intermédiaire est remplacé par du code, tous les types de coûts sont réduits, y compris le temps et l'argent.

**Tout comme Bitcoin élimine le besoin de quelqu'un pour détenir votre argent, Ethereum élimine le besoin de quelqu'un pour négocier un accord.**

Maintenant, vous vous demandez peut-être, où sont tous ces contrats intelligents ? Eh bien, ils sont essentiellement hébergés sur plusieurs nœuds informatiques à travers le monde.

Ces nœuds contiennent toutes les informations de tous les contrats intelligents du monde, y compris le code, les transactions, etc. Ils travaillent constamment pour maintenir ces informations à jour afin qu'ils aient tous la même copie exacte. C'est ce qui rend les contrats intelligents, et les cryptomonnaies en général, décentralisés.

Et puisque tous les nœuds ont les mêmes informations et sont répartis dans le monde, la suppression d'un nœud n'interrompra pas l'exécution d'un contrat intelligent. La redondance assure la disponibilité.

## Qu'est-ce qu'une Dapp ?

Maintenant que nous avons une bonne idée de ce qu'est Ethereum et les contrats intelligents, nous pouvons commencer à plonger dans les détails de ce qu'est une Dapp.

Pour être clair, une Dapp est tout comme n'importe quelle autre application logicielle que vous utilisez. Cela pourrait être un site web ou une application sur votre téléphone. Ce qui rend une Dapp différente d'une application traditionnelle, c'est qu'elle est construite sur un réseau décentralisé, comme Ethereum.

Lorsque vous créez vos propres contrats intelligents Ethereum, vous écrivez en fait une partie du code backend pour votre Dapp. Et bien que votre Dapp aura une interface utilisateur comme une application traditionnelle, tout ou partie du backend est construit sur Ethereum.

**Dapp = frontend + backend de contrat intelligent**

Ce code backend est écrit dans un langage spécifique à Ethereum, y compris Solidity (le plus populaire), Serpent et Vyper. Ci-dessous un exemple d'un contrat simple "Hello World" écrit en Solidity.

```
pragma solidity ^0.4.22;

contract helloWorld {
 function printHelloWorld () public pure returns (string) {
   return 'Hello World!';
 }
}
```

Si le contrat intelligent est déployé sur le mainnet d'Ethereum (c'est-à-dire, production) ou même un testnet local, votre Dapp peut exécuter le code dans le contrat intelligent en appelant la fonction **printHelloWorld()**.

Mais qu'en est-il du frontend ? Y a-t-il un langage spécifique que vous devez utiliser pour votre Dapp ?

Non ! Vous pouvez utiliser n'importe quel langage/framework frontend que vous voulez. Mais il est possible d'héberger votre code frontend sur des nœuds de stockage décentralisés pour rendre à la fois votre frontend et votre backend décentralisés.

Jetez un coup d'œil à des technologies comme [Swarm](https://ethereum.stackexchange.com/questions/375/what-is-swarm-and-what-is-it-used-for?noredirect=1&lq=1) et [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System) pour en savoir plus sur le stockage décentralisé.

D'accord, donc les Dapps sont simplement des applications qui ont une partie ou la totalité de leur backend décentralisé et peuvent même avoir un frontend décentralisé. Pourquoi devriez-vous vous en soucier ?

Le développement des Dapps est une autre étape vers un avenir de l'Internet qui est communément appelé Web 3.0.

## Ethereum Dapps : L'épine dorsale du Web 3.0

Depuis la création de l'Internet, la quantité d'informations et d'interactions humaines a explosé. Nous sommes capables de produire et de consommer des informations à des niveaux presque infinis.

Malheureusement, la capacité à contrôler cette information est devenue fortement centralisée au fil du temps. Cela inclut les informations sur votre vie sociale, votre santé, vos finances, et bien plus encore. Ceux qui contrôlent cette information en sont les propriétaires ultimes et peuvent l'utiliser comme ils l'entendent.

Ce sont essentiellement des intermédiaires qui détiennent vos informations sur leurs serveurs centralisés afin de pouvoir vous fournir des services, comme détenir votre argent, héberger votre site web, vous connecter avec votre famille et vos amis, etc. Et d'un simple clic, ils peuvent vous empêcher complètement d'accéder à cette information (votre ?) et à tous les services associés.

C'est un monopole sur les informations que vous produisez et consommez ainsi que sur les services que vous utilisez. Heureusement, le Web 3.0 change tout cela et les Dapps Ethereum jouent un rôle central.

Le Web 3.0 est beaucoup de choses, mais à sa base, c'est une technologie basée sur la décentralisation. En décentralisant l'information et les services, les grandes corporations et les gouvernements ne pourront pas contrôler les utilisateurs de l'Internet par des tactiques monopolistiques et autoritaires.

Les Dapps Ethereum, avec leur capacité à décentraliser l'information et les services, donnent au Web 3.0 une plateforme pour offrir un Internet complètement libre (comme dans liberté) et accessible à tous. Il n'y aura plus de point central de contrôle car il n'y aura plus d'intermédiaires pour faciliter le flux d'informations et de services.

Certains des jetons et Dapps Ethereum les plus prometteurs posent les bases de l'avenir de l'Internet, y compris :

* [Basic Attention Token](https://basicattentiontoken.org/) (BAT) : utilisé pour améliorer la confidentialité et le transfert de valeur entre les utilisateurs, les éditeurs et les annonceurs. Utilisé dans le navigateur [Brave](https://brave.com/).
* [Golem](https://golem.network/) (GNT) : utilisé pour exécuter du code sur un ou plusieurs nœuds de calcul distribués.
* [Minds](https://www.minds.com/) : une plateforme de médias sociaux qui améliore le transfert de valeur entre les créateurs de contenu et les consommateurs.
* [TokenSets](https://www.tokensets.com/) : utilisé pour gérer les actifs cryptographiques via des stratégies de gestion d'actifs automatisées tokenisées.
* [Aave](https://aave.com/) : utilisé pour gagner des intérêts sur les dépôts de cryptomonnaies et emprunter des actifs cryptographiques.
* [IDEX](https://idex.market/) : une bourse de cryptomonnaies décentralisée.

## Réflexions finales

Depuis la création de Bitcoin, la première cryptomonnaie, il y a eu une croissance massive dans le cryptoverse.

Pouvoir stocker des données de manière décentralisée était une étape nécessaire vers la décentralisation de l'exécution du code. Avec Ethereum, il est maintenant possible de déployer des contrats intelligents à travers le monde pour alimenter le backend des Dapps existantes et futures.

Et à mesure que de plus en plus de Dapps sont lancées, nous nous rapprocherons de plus en plus d'un Internet plus libre, plus équitable et plus accessible.

_Je suis Grant et je suis un professionnel indépendant du SEO et du contenu. Si vous cherchez à développer le trafic de recherche organique de votre marque, je peux vous aider avec votre [SEO fintech](https://www.writefintech.com/). Santé !_