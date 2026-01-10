---
title: Ressources que j'ai utilisées pour m'autoformer au développement blockchain
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-09T14:46:04.000Z'
originalURL: https://freecodecamp.org/news/the-resources-i-used-to-teach-myself-blockchain-development-1fccada9b92b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6bOXOdSXtre9t7aMgTr-4A.png
tags:
- name: Blockchain
  slug: blockchain
- name: dapps
  slug: dapps
- name: Ethereum
  slug: ethereum
- name: Solidity
  slug: solidity
- name: technology
  slug: technology
seo_title: Ressources que j'ai utilisées pour m'autoformer au développement blockchain
seo_desc: 'By Gwendolyn Faraday

  I started investing in cryptocurrencies last year, and just kept going down the
  blockchain rabbit hole from there. Where I live especially, much of the blockchain
  community is focused on things like trading and investing in crypt...'
---

Par Gwendolyn Faraday

J'ai commencé à investir dans les cryptomonnaies l'année dernière, et depuis, je n'ai cessé de descendre dans le terrier du lapin de la blockchain. Là où je vis, une grande partie de la communauté blockchain se concentre sur des choses comme le trading et l'investissement dans les cryptomonnaies. Bien que ce soit amusant d'investir au début, cela ne m'intéressait pas tant. J'ai donc créé mon propre groupe de rencontre local pour me concentrer sur le développement blockchain.

Le groupe de rencontre m'a permis de me connecter et d'apprendre aux côtés des membres de la communauté, et j'ai utilisé cela pour compiler une liste de ressources que moi, et les autres membres, avons trouvées utiles. Ces ressources sont organisées des explications les plus basiques de la blockchain aux systèmes sous-jacents ainsi qu'à la construction d'applications sur la blockchain.

Il y a beaucoup de bruit là-bas. J'espère que cela vous aidera à y voir plus clair si vous êtes intéressé à devenir un professionnel de la blockchain.

### **Table des matières :**

1. Apprendre les bases
2. Développement de Dapp avec Ethereum
3. Théorie des jeux
4. Cryptographie
5. Matériaux audio/supplementaires
6. Autres types de développement blockchain
7. Recherche

### **Les bases — Comment fonctionnent les technologies blockchain**

Il peut falloir un moment pour comprendre les complexités des technologies blockchain. Cette technologie englobe tant de domaines différents : l'informatique, la théorie des jeux, la cryptographie, et l'économie pour n'en nommer que quelques-uns. Il est donc difficile d'apprendre initialement les tenants et aboutissants de son fonctionnement.

Voici quelques ressources que je pense donner un bon aperçu clair de comment la blockchain fonctionne vraiment.

1. **Commencez par cette vidéo expliquant comment cela fonctionne :**

**2. Regardez les deux vidéos ici (il y a un certain chevauchement avec la ressource précédente, mais cela ancrera les concepts dans votre esprit) et jouez avec la démonstration sur le site :**

[**Démonstration de la Blockchain**](https://anders.com/blockchain/)  
[_Une démonstration en direct de la blockchain dans un navigateur._anders.com](https://anders.com/blockchain/)

3. **Lisez le chapitre « [Qu'est-ce qu'Ethereum](https://github.com/ethereumbook/ethereumbook/blob/develop/what-is.asciidoc) » du livre GitHub, « [Maîtriser Ethereum](https://github.com/ethereumbook/ethereumbook) »**

### **Développement de Dapp avec Ethereum**

Il existe de nombreuses blockchains différentes qui permettent désormais de créer des applications et des contrats intelligents. Ethereum est de loin l'option la plus populaire, avec Solidity comme langage de programmation dominant. Je suggère d'essayer de construire des dapps avec ces technologies en premier.

De loin **la meilleure façon d'apprendre à coder avec Solidity** est [Cryptozombies](http://cryptozombies.io/). C'est un environnement de codage interactif qui vous apprend à programmer Solidity étape par étape tout en construisant un jeu de zombies ! Il est également maintenu à jour avec les nouvelles versions de Solidity, ce qui est difficile à trouver dans l'espace blockchain en constante évolution.

**Si vous voulez quelque chose en plus de Cryptozombies, voici deux autres recommandations que j'ai pour apprendre Solidity :**

1. [Série de vidéos YouTube pour le développement de dapp](https://www.youtube.com/playlist?list=PL16WqdAj66SCOdL6XIFbke-XQg2GW_Avg) — Cette chaîne explique très bien les choses, mais la syntaxe n'est pas totalement à jour, donc vous devrez peut-être chercher certaines choses sur Google si vous obtenez des erreurs. L'éditeur Remix qu'il utilise vous donnera des indices sur ce que vous devez changer, donc vous devriez être bien.
2. [Stephen Grider sur Udemy](https://www.udemy.com/ethereum-and-solidity-the-complete-developers-guide) — il s'agit d'un cours payant, mais vous pouvez obtenir une offre pour ~9,99 USD et il contient de bons exemples et du contenu.

Après avoir terminé Cryptozombies, il est bon d'apprendre à utiliser l'[IDE Remix](http://remix.solidity.com) pour créer, déboguer et déployer des contrats. [La documentation contient un guide de démarrage rapide et de nombreuses instructions étape par étape avec des captures d'écran](https://media.readthedocs.org/pdf/remix/latest/remix.pdf) pour vous aider à démarrer.

Vous devriez également en apprendre davantage sur les [clients](https://github.com/ethereumbook/ethereumbook/blob/3812a5dfa5b851a1aaa52b14c5aea6c74629e5a0/clients.asciidoc) et les [portefeuilles](https://github.com/ethereumbook/ethereumbook/blob/3812a5dfa5b851a1aaa52b14c5aea6c74629e5a0/wallets.asciidoc) Ethereum. Ces liens expliqueront tout ce que vous devez savoir. Metamask est un plugin de navigateur et une excellente façon de commencer (il est pour Chrome ou Firefox, mais celui pour Chrome semble fonctionner beaucoup mieux).

Ensuite, apprenez le développement avancé de contrats intelligents. Commencez par lire la [documentation Solidity](https://solidity.readthedocs.io/en/v0.4.24/solidity-by-example.html). Elle aborde des concepts plus avancés et contient également quelques bonnes exemples de dapps. Ethereum.org propose également quelques bons exemples de dapps à consulter comme [celui-ci](https://www.ethereum.org/dao). Vous pouvez copier les exemples directement dans l'IDE Remix et les tester vous-même.

Une fois que vous avez une bonne maîtrise de Solidity et des contrats intelligents, commencez à parcourir quelques exemples open source. Le choix par défaut semble être [Crypto Kitties](https://etherscan.io/address/0x06012c8cf97bead5deae237070f9587f8e7a266d#code) (vous pouvez voir le code du contrat à n'importe quelle adresse Ethereum sur [etherscan.io](https://etherscan.io)), mais il en existe beaucoup d'autres qui peuvent être de grands outils d'apprentissage. Vous pouvez rechercher sur GitHub et Etherscan pour en trouver plus.

Il y a beaucoup de développement en cours dans l'espace Ethereum autour des outils de développement et de la sécurité. Voici quelques bibliothèques et outils géniaux que vous pouvez consulter :

* [Open Zeppelin](https://github.com/OpenZeppelin/openzeppelin-solidity)
* [Truffle Development Framework](https://www.truffleframework.com/)
* [ConsenSys — Bonnes pratiques pour les contrats intelligents](https://github.com/ConsenSys/smart-contract-best-practices)

### Théorie des jeux

Certains des problèmes que la blockchain vise à résoudre proviennent de la théorie des jeux, notamment le problème des généraux byzantins. Ce problème traite du consensus entre de nombreuses parties différentes sans avoir à faire confiance à ce qu'un individu n'est pas malveillant.

[The Great Courses Plus propose une excellente série de conférences sur divers sujets de la théorie des jeux](https://www.thegreatcoursesplus.com/game-theory-in-life-business-and-beyond). Ils ont un modèle d'abonnement mensuel avec un essai gratuit de deux semaines. Les 24 conférences de 30 minutes couvrent un large éventail de sujets en théorie des jeux, et je pense que c'est excellent pour une compréhension globale du sujet.

### Cryptographie

Je ne suis définitivement pas une experte dans ce domaine, mais j'apprends continuellement comment fonctionne la cryptographie et comment elle peut être appliquée à la blockchain. Ce domaine plonge vraiment dans les mathématiques, car Ethereum et de nombreuses autres blockchains utilisent la cryptographie à courbe elliptique.

En tant que débutante dans ce domaine, voici quelques ressources que j'ai trouvées utiles :

* [Coursera Cryptographie I](https://www.coursera.org/learn/crypto) — Gratuit pour auditer le cours ; payant si vous voulez un certificat.
* [Chapitre sur la cryptographie dans le livre Maîtrise d'Ethereum](https://github.com/ethereumbook/ethereumbook/blob/3812a5dfa5b851a1aaa52b14c5aea6c74629e5a0/keys-addresses.asciidoc)

### Matériel audio supplémentaire

* [**Podcast :** Software Engineering Daily, Blockchain](https://itunes.apple.com/us/podcast/blockchain-software-engineering-daily/id1230807219) — C'est mon podcast blockchain préféré. Ils font un très bon travail en expliquant des sujets complexes et ont une variété de leaders de l'industrie dans l'émission.
* [**Podcast :** CryptoDisrupted](https://cryptodisrupted.com/) — L'animateur invite de nombreux invités de projets intéressants dans l'espace blockchain. J'ai apprécié la plupart de ce que j'ai écouté avec ce podcast.

### Autres types de développement blockchain

La communauté Ethereum compte, de loin, le plus de développeurs et de ressources d'apprentissage, c'est donc un bon endroit pour commencer avec le développement blockchain. Je pense que vous auriez tort de ne pas explorer d'autres innovations dans le domaine, cependant. Voici quelques projets intéressants.

[**Lisk**](https://lisk.io/) — Rend le développement blockchain plus accessible, car tout est construit en JavaScript.

[**EOS**](https://www.eos.io/) — Le créateur, Dan Larimer, avait construit plusieurs autres solutions blockchain réussies avant de commencer ce projet. EOS est censé résoudre certains des problèmes d'Ethereum, comme la scalabilité et la sécurité. Il est parfois appelé « Le tueur d'Ethereum ».

**Protocoles interchaînes** — Ce sont quelques solutions qui aident à faciliter les transactions entre différentes blockchains et qui ont également des solutions intéressantes pour aider la blockchain à évoluer :

1. [Cosmos](https://cosmos.network/)
2. [Polkadot](https://polkadot.network/)
3. [Interledger](https://interledger.org/)

[**Hyperledger**](https://www.hyperledger.org/) — Un effort collaboratif open source créé pour faire avancer les technologies blockchain interindustrielles. Il est hébergé par la Linux Foundation.

[**Holo**](https://holo.host/) — Une technologie post-blockchain qui tente de résoudre les problèmes de scalabilité et de centralisation dans les technologies blockchain d'aujourd'hui.

### Recherche et développement actuel

Une fois que vous avez appris les bases, il est si important de lire des articles de recherche pour atteindre la maîtrise dans l'espace blockchain. Voici quelques endroits où j'ai eu du succès :

* [The Morning Paper — Articles sur la Blockchain](https://blog.acolyer.org/?s=blockchain)
* [Collection de livres blancs d'ICO](http://whitepaperdatabase.com/)
* [http://blockchain.mit.edu/](http://blockchain.mit.edu/)
* [https://www.blockchainresearchinstitute.org/](https://www.blockchainresearchinstitute.org/)

### Conclusion

Je vais continuer à étudier le développement blockchain et à essayer de trouver de nouvelles solutions intéressantes. Veuillez laisser un commentaire ou m'envoyer un message si je manque quelque chose ici.

En ce moment, je prévois d'autres articles sur les entreprises, les projets et les personnes d'intérêt dans l'espace blockchain. Suivez-moi si vous êtes intéressé par l'une de ces choses.