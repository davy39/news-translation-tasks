---
title: Comment construire un système de chaîne d'approvisionnement pour la fabrication
  automobile en utilisant Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-15T17:16:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-car-manufacturing-supply-chain-system-using-ethereum-cbb87144cde5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t0Z20-NTO_EcRzDpgl3FZg.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: supply chain
  slug: supply-chain
- name: 'tech '
  slug: tech
seo_title: Comment construire un système de chaîne d'approvisionnement pour la fabrication
  automobile en utilisant Ethereum
seo_desc: 'By Marcelo Russi Mergulhão

  Here at Daitan we are always looking for new technologies that can help our clients
  solve their problems more efficiently. Lately one that has captured a lot of our
  and our clients’ attention is Blockchain.

  In this article,...'
---

Par Marcelo Russi Mergulhão

Ici chez [Daitan](http://www.daitan.com/), nous sommes toujours à la recherche de nouvelles technologies qui peuvent aider nos clients à résoudre leurs problèmes de manière plus efficace. Récemment, l'une d'entre elles a attiré beaucoup notre attention ainsi que celle de nos clients : la Blockchain.

Dans cet article, notre objectif est de présenter une manière pratique de mettre en œuvre votre propre application de chaîne d'approvisionnement basée sur une plateforme blockchain !

Le système est utilisé pour l'un des problèmes où je pense que l'application de la blockchain apporte la plus grande valeur : une chaîne d'approvisionnement.

Cette application a été beaucoup explorée récemment dans les PoCs et de grandes entreprises expérimentent déjà [cette solution pour leurs opérations](https://www.maersk.com/en/news/2018/06/29/maersk-and-ibm-introduce-tradelens-blockchain-shipping-solution).

Utiliser la blockchain pour résoudre ce type de problème est une bonne alternative car nous pouvons bénéficier de la transparence et du suivi efficace de la provenance inhérents à la technologie.

Étant donné que cet article vise à être simple et non un projet complet, nous allons simplifier beaucoup le problème.

À la fin, nous avons toujours un système de bout en bout qui peut démontrer l'applicabilité de la technologie à cet ensemble particulier de problèmes.

### Choix d'une plateforme

Actuellement, il existe de nombreuses plateformes qui vous permettent de créer votre propre blockchain ou d'utiliser une blockchain publique pour vos propres projets, nous allons donc en utiliser une au lieu de construire à partir de zéro.

Ces projets bénéficient d'un grand soutien de la part des entreprises et de la communauté open source, nous croyons donc que l'utilisation de l'une d'entre elles est le chemin le plus pratique pour la majorité des problèmes, nous permettant de nous concentrer sur la logique métier plutôt que sur l'infrastructure.

Pour notre démonstration, nous avons choisi le [projet Ethereum](https://www.ethereum.org/). C'est une plateforme populaire et tous les outils de développement disponibles rendent la mise en œuvre de solutions sur celle-ci facile à accomplir.

### **L'histoire de la fabrication**

Nous avons établi le domaine, mais que voulons-nous faire spécifiquement ?  
Décrivons un problème simple de fabrication automobile et les acteurs impliqués dans le processus.

Tout d'abord, nous avons l'usine de pièces, responsable de la production de roues, de pièces de carrosserie, de moteurs et de transmissions. L'usine informe chaque production de pièces en utilisant le contrat intelligent "ProductManagement", qui conservera les détails de chaque pièce et produit.

De plus, l'usine déclare qu'elle est le propriétaire d'une pièce spécifique en appelant une méthode du contrat intelligent "ChangeOwnership", qui conservera l'historique des propriétaires de chaque pièce et produit.

En allant plus loin dans la chaîne, nous avons une usine de voitures qui achète des pièces à l'usine de pièces pour fabriquer des voitures. Le contrat "ChangeOwnership" est l'endroit où nous conservons ce type d'opération, nous avons donc une autre méthode pour permettre à l'usine de pièces de transférer la propriété des pièces à l'usine de voitures.

Avec suffisamment de pièces, l'usine de voitures peut enfin commencer à fabriquer des voitures. Similaire à ce que l'usine de pièces a fait pour informer de son travail, l'usine de voitures utilise maintenant le contrat intelligent "ProductManagement" pour déclarer un assemblage spécifique de voiture. Chaque voiture a un ensemble de propriétés, comme un numéro de série, et a également une liste de pièces, qui lie les voitures à des pièces spécifiques.

La propriété est contrôlée par le contrat "ChangeOwnership" et ainsi l'usine de voitures définit la propriété de la voiture à elle-même.

Enfin, nous ajoutons des concessionnaires au scénario et ils peuvent acheter des voitures à une usine et cette dernière peut transférer la propriété de la voiture en utilisant "ChangeOwnership". La blockchain stocke chaque transaction qui a impliqué cette voiture ou l'une des pièces qui la composent, donc le concessionnaire (ou toute autre partie) peut suivre tout ce qu'un article spécifique a traversé. Dans notre cas, ce suivi sera effectué en surveillant les événements générés par les transactions. Cela deviendra clair lorsque nous analyserons le code.

Le flux complet des produits peut être vu dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UoHJ5vPAkJXnu-cMPYRB_A.jpeg)
_Chaîne d'approvisionnement pour la fabrication automobile_

Nous savons ce que nous devons faire, mais nous devons encore nous équiper de quelques outils pour permettre le développement.

### **Environnement et outils**

Tout d'abord, nous devons faire une distinction claire entre les réseaux de l'écosystème Ethereum. Le réseau principal (appelé Mainnet) est l'endroit où résident les vraies applications et où chaque unité d'ether a une valeur réelle.

Cela signifie que tout ce que vous enregistrez là est destiné à exister tant qu'Ethereum lui-même existe. De plus, l'ether ne peut être obtenu que par minage ou en l'achetant avec de l'argent réel.

Utiliser ce réseau pour développer des démonstrations semble être une mauvaise idée, il existe donc d'autres réseaux qui sont meilleurs pour supporter le développement. Ces réseaux peuvent être des réseaux publics, comme celui appelé Rinkeby, ou vous pouvez même créer votre propre réseau Ethereum !

Bien qu'utiliser un Test Net public comme Rinkeby nous offre une meilleure façon de valider notre DApp (Application Décentralisée), nous allons créer notre propre réseau pour réduire le temps d'acceptation des transactions et simplifier au maximum le développement.

L'outil que nous allons utiliser pour créer notre réseau s'appelle [Ganache](https://truffleframework.com/ganache).

Ganache est un outil simple qui crée un réseau Ethereum local et vous pouvez vous y connecter comme vous le feriez avec le réseau principal. Il vous fournit également 10 comptes avec 100 ethers chaque fois que vous l'exécutez.

J'aime vivre dans le terminal, donc au lieu d'utiliser l'interface utilisateur de Ganache, j'utiliserai [ganache-cli](https://github.com/trufflesuite/ganache-cli), la version en ligne de commande de Ganache qui est un outil basé sur NodeJS et peut être installé avec npm :

`npm install -g ganache-cli`

Pour l'exécuter, il suffit d'exécuter `ganache-cli` et vous êtes prêt à partir ! Lorsque vous exécutez la CLI, elle générera une phrase mnémonique pour vos portefeuilles. La phrase mnémonique est une phrase de 12 mots qui est la racine pour générer les clés privées des comptes et par conséquent les portefeuilles.

La sortie est comme l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wnlj5Sl_5e-NTos9HPwc3A.png)

Enregistrez la phrase mnémonique pour l'utiliser plus tard. Chaque fois que vous devez exécuter Ganache à nouveau, vous pouvez préserver les mêmes comptes en fournissant la phrase mnémonique avec le paramètre -m :

`ganache-cli -m "now frame tenant chronic oven cube minute immune leaf clock demand volume"`

**Remarque : les phrases mnémoniques créées par Ganache ne sont pas sécurisées et ne doivent pas être utilisées pour des portefeuilles sur le réseau Ethereum**

Maintenant que nous avons notre réseau, nous devons pouvoir tester et déployer nos contrats sur celui-ci. Cela est accompli par un autre outil appelé [Truffle](https://truffleframework.com/truffle), faisant partie de la même suite de développement que Ganache. Truffle peut également être installé avec npm, il suffit donc d'exécuter :

`npm install -g truffle`

Nous allons utiliser Truffle pour préparer la structure de notre projet, donc exécutez `truffle init` et vérifiez la structure de dossiers qui est créée :

```
ethereum-supply-chain
|-contracts
|  Migrations.sol
|-migrations
|  1_initial_migration.js
|-test
truffle-config.js
```

* Contrats : contient le code pour nos contrats intelligents
* Migrations : contient les instructions de déploiement pour nos contrats
* Test : contient les tests pour les contrats
* Truffle-config.js (ou truffle.js selon votre système d'exploitation) : fichier de configuration principal, pointe vers les réseaux Ethereum sur lesquels nous pouvons déployer

Le fichier de configuration contient beaucoup de contenu, mais la plupart est commenté. Pour ajouter notre réseau local aux options de déploiement, il suffit de décommenter la partie suivante (lignes 49-53) :

Enfin, nous devons fournir une interface à nos utilisateurs pour leur permettre d'interagir avec les réseaux Ethereum.

L'une des options pour cela est d'installer [Metamask](https://metamask.io/), un plugin de navigateur qui gère les portefeuilles et permet également aux systèmes web de communiquer avec les réseaux Ethereum.

Une fois installé, Metamask fournit une interface pour vérifier les fonds des portefeuilles sur différents réseaux. Chaque fois qu'un système web nécessite une opération impliquant un paiement, Metamask demande l'approbation de l'utilisateur.

Pour l'installer, il suffit d'aller sur leur [site web](https://metamask.io/) et de choisir l'extension pour votre navigateur.

Après l'installation, Metamask doit créer ou importer un portefeuille, choisissez donc "importer avec une phrase de départ" et collez la phrase mnémonique que vous avez obtenue de ganache-cli.

**Remarque : Metamask est actuellement en version bêta, gardez cela à l'esprit lorsque vous l'utilisez et suivez les instructions données après la configuration**

Et c'est tout ce dont nous avons besoin pour l'instant, plongeons dans le code !

### **Contrats intelligents en pratique**

La première chose que nous devons faire est de mettre en œuvre la logique derrière chacun des contrats intelligents, nous commençons donc par "ProductManagement".

Ce contrat doit avoir une méthode pour enregistrer les pièces et une autre pour enregistrer les produits, même si les exigences pour chaque opération sont très similaires.  
Nous faisons cela parce que nous voulons vérifier que toutes les pièces existent lorsque nous essayons de construire un nouveau produit. Nous pouvons donc avoir les méthodes suivantes :

* Enregistrement des pièces : créer un mappage donné les détails de la pièce elle-même (type, numéro de série et date de fabrication), l'usine qui l'a fabriquée (ID de l'usine) et le propriétaire actuel (ID du propriétaire).
* Enregistrement des produits : créer un mappage donné les mêmes informations que l'enregistrement des pièces plus l'ID de chacune des pièces présentes sur le produit.
* Getters pour les mappages afin que nous puissions vérifier l'existence des pièces et des produits et obtenir leurs détails.

Le code du contrat que nous devons implémenter est le suivant :

Nous définissons des structs pour les pièces et les produits qui mappent toutes les informations requises pour "construire" nos pièces et produits, et après cela, nous ajoutons les mappages qui conserveront tous les éléments enregistrés.

La méthode `buildPart` est simple : elle utilise une fonction helper pour concaténer l'adresse de l'expéditeur et les informations de la pièce dans un tableau d'octets et calculer un hash. Ce hash est la clé utilisée lors de l'enregistrement et de l'interrogation ultérieure des données, nous le retournons donc pour faciliter le développement.

Étant donné que les transactions Ethereum ne sont pas validées et s'exécutent lorsque vous appelez le contrat intelligent, nous recevons un hash de transaction et ne pouvons pas l'utiliser pour notre application web, mais nous pouvons émettre un appel au lieu d'une transaction pour vérifier les résultats facilement.

Dans un système réel, nous nous attendrions à ce que le fabricant fournisse le hash de la pièce avec la pièce physique, mais nous ne penserons pas à ce mécanisme ici. Nous connaissons les informations utilisées pour générer le hash, nous pouvons donc le calculer lorsque nous en avons besoin, et c'est exactement ce que nous faisons dans le code de test et également dans l'application web.

Nous ne couvrirons pas le code de test afin de ne pas étendre l'article, mais consultez-le dans notre [dépôt](https://github.com/daitan-innovation/ethereum-supply-chain) !

La méthode buildProduct est simplement une extension de la méthode buildPart, ajoutant une vérification simple pour garantir que toutes les pièces ont été enregistrées avant de tenter de créer le produit.

Deux choses valent vraiment la peine d'être notées à propos du code :

* Solidity génère automatiquement des getters pour les mappages publics, nous n'avons donc pas à nous en soucier !
* Mais nous devons nous en soucier lorsque nous retournons des valeurs de tableau, exactement le cas pour nos pièces de produit. Nous avons créé une fonction "getParts" pour répondre à ce besoin.

En continuant notre développement, nous allons coder le contrat "ChangeOwnership". Il a un but simple : gérer le transfert de pièces et de produits entre les parties intéressées.

Étant donné que nous utiliserons des identifiants pour l'opération de transfert de propriété, nous pouvons avoir une méthode pour que les fabricants enregistrent leur "propriété initiale" et une autre méthode pour changer la propriété à d'autres parties.

Nous devons simplement recevoir un paramètre pour nous indiquer si nous voulons enregistrer des pièces ou des produits afin de savoir quel mappage vérifier dans le contrat "ProductManagement" et également où stocker le propriétaire de l'élément actuel. Le code est le suivant :

Nous utilisons une instance de "ProductManagement" pour interroger les pièces et les produits chaque fois que nous essayons d'interagir avec eux. Cela met en évidence un aspect important des contrats intelligents : vous pouvez les utiliser pour appeler d'autres contrats intelligents ! Une option pour faire cela est de déclarer l'ABI du contrat au début du fichier de contrat, mais seulement les parties requises par votre contrat. Dans notre cas, cela signifie :

Pour pointer vers le contrat correct, nous devons simplement passer l'adresse du contrat lors de son instanciation, comme ceci :

`pm = ProductManagement(prod_contract_add);`

En procédant à la révision du code "ChangeOwnership", nous pouvons également voir que nous définissons deux événements, TransferPartOwnership et TransferProductOwnership. Les événements peuvent être enregistrés avec des transactions, ce qui sera le cœur de notre fonctionnalité de "suivi".

Chaque fois qu'une pièce ou un produit est transféré avec succès à un autre compte, nous émettons un événement.

Prenons la fonction addOwnership comme exemple : nous vérifions que l'élément existe, vérifions s'il est toujours non enregistré et que le fabricant est celui qui demande la propriété. Si nous vérifions tout cela, nous stockons alors le fabricant comme propriétaire de la pièce et enregistrons cela sur Ethereum comme un événement. Plus tard, nous pouvons interroger les événements concernant cette pièce à partir de son hash et voir tous les transferts.

Le seul autre point à noter à propos de ce code est dans la fonction "changeOwnership" : chaque fois qu'une voiture change de propriétaire, nous changeons également la propriété des pièces qui la composent. Mais assez parlé de la révision du code, vérifions comment le déployer.

### Déploiement des contrats

Pour migrer nos contrats vers Ethereum, nous devons créer un simple fichier de déploiement dans le dossier "deployments". Nous pouvons nous baser sur le fichier "1_initial_migration.js" créé par Truffle, notre code devient donc :

Nous pouvons enfin déployer notre code sur notre réseau Ethereum local en exécutant :

`truffle migrate -network development`

Lorsque vous exécutez cela, vous remarquerez probablement que le terminal ganache-cli génère beaucoup de messages, y compris certains comme :

```
Transaction: 0x9fe6d2ece9cdca2f12b574ead7abb7bea7feab316f5cd6ebbd5b713e76850a1d
Contract created: 0xb6a3c3cf9d1e27e43e5fb12e505d79764748edbe
```

Celles-ci représentent les adresses de nos contrats, alors enregistrez-les pour pouvoir communiquer plus tard. Nous aurons besoin de cette adresse sur notre interface web !

### **Interface web en pratique**

Notre système dispose désormais des deux contrats intelligents prêts et tout ce dont nous avons besoin est l'interface pour les utiliser.

Nous avons créé une page pour chaque rôle dans notre scénario, nous avons donc une "Vue de l'usine de pièces", une "Vue de l'usine de voitures" et une "Vue du concessionnaire". Nous n'entrerons pas dans les détails des méthodes implémentées pour les interactions, mais donnons un aperçu pour vous inciter à vérifier le code !

Les interactions de l'usine de pièces, comme l'enregistrement des pièces, l'ajout de propriété et le transfert de propriété, peuvent être effectuées sur l'interface montrée ci-dessous. Il est intéressant de noter que Metamask demande une permission pour chaque transaction que nous effectuons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qPeuFBBB1rSmtRSfZGBDbQ.png)
_Interface de fabrication de pièces_

En regardant les choses du point de vue d'un fabricant de voitures, nous avons la liste des pièces remplie à partir des enregistrements sur la blockchain, puis la sélection des pièces pour assembler la voiture, la construction de la voiture, et enfin nous transférons la propriété à un concessionnaire. Tout comme une usine de pièces, l'usine de voitures a également sa propre interface, montrée ci-dessous. Toutes les interactions avec Ethereum utilisent le hash de la pièce/voiture créé à partir de leurs propriétés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y_O0U_FEUYFeE0F57i-qLQ.png)
_Interface de fabrication de voitures_

La vue finale est celle des concessionnaires, et pour notre exemple, c'est la plus simple : nous pouvons simplement vérifier les voitures et les pièces pour l'historique des propriétaires. Voir l'image ci-dessous pour plus de détails :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vOylTWq1GMo6wWt3a9iYjw.png)
_Vue du concessionnaire avec l'historique des propriétaires pour les voitures et les pièces_

Sous le capot, nous utilisons la bibliothèque web3 pour appeler les méthodes de nos contrats intelligents. La bibliothèque nous fournit des objets représentant nos contrats et méthodes, et pour cela, nous devons simplement définir :

* Emplacement du réseau
* ABI du contrat (définition du contrat intelligent)
* Adresse du contrat
* Portefeuille à utiliser pour les opérations

Par défaut, ganache-cli exécute le réseau sur le port 8545 et l'ABI est généré chaque fois que vous compilez et déployez vos contrats (mais seulement lorsque nous mettons à jour le code, nous n'avons donc pas besoin de changer cela).

Si vous en avez besoin, obtenez la valeur stockée dans le dossier "build" de la configuration.  
L'adresse du contrat que nous devons spécifier avec les valeurs enregistrées précédemment, modifiez donc les lignes suivantes avec vos valeurs :

Maintenant que notre page est prête à interagir avec nos contrats intelligents, nous devons simplement préparer les fonctions qui utilisent les objets fournis par web3 et notre système est complet !

Les fonctions obtiennent essentiellement les données des champs d'entrée sur la page et appellent ensuite les fonctions avec celles-ci comme paramètres. Le code complet est trop grand pour cet article, mais vérifions simplement deux parties qui expliquent la plupart des interactions avec la blockchain. La première est :

L'objet "window.co" est notre contrat "ChangeOwnership", et currentPartOwner et addOwnership sont des méthodes fournies par celui-ci.  
La différence ici est dans la fonction utilisée pour les appeler : call vs send.  
Web3 1.0 vous oblige à spécifier le type d'interaction que vous souhaitez faire avec la blockchain : lectures ou transactions.

Ainsi, chaque fois que vous utilisez une méthode avec "call", vous lisez simplement des données depuis la blockchain, cela ne vous coûte pas d'ether et ne modifie pas l'état de la chaîne.

D'un autre côté, si vous utilisez "send", vous devez envoyer du gaz pour effectuer l'opération et cela crée une transaction. Comme nous l'avons dit auparavant, les transactions ne sont pas minées immédiatement, alors tenez-en compte lorsque vous développez des Dapps pour le monde réel.

Enfin, la deuxième partie à mettre en évidence est :

Vous souvenez-vous lorsque nous avons dit que les événements seraient le cœur de notre chaîne d'approvisionnement ? Cette ligne est utilisée pour obtenir tous les événements d'un type spécifique, en filtrant les résultats par le hash de la pièce.

Cela signifie que nous pouvons obtenir tout ce qui s'est passé avec une seule pièce, et si nous le voulons, nous pouvons également obtenir les détails de la pièce en utilisant le même hash et en appelant "parts" depuis "ProductManagement".

Plutôt cool, n'est-ce pas ?

### **Conclusion**

Et nous avons terminé !

Chaque fois qu'un fabricant de pièces souhaite notifier une nouvelle production de pièces, qu'un fabricant de voitures souhaite assembler cela dans une voiture, ou que nous souhaitons déplacer les pièces et les voitures d'un propriétaire à un autre, nous pouvons simplement utiliser l'interface web pour le faire.

Nous avons un enregistrement transparent qui permet aux fabricants, aux concessionnaires et aux acheteurs d'avoir les mêmes informations sur les produits.

Si un problème est trouvé concernant une certaine plage de numéros de série dans les usines, l'usine peut vérifier où s'attaquer et résoudre le problème.

La même chose est vraie dans le sens inverse : les concessionnaires et les acheteurs peuvent retracer les pièces de leurs produits jusqu'aux usines en cas de problème ou de besoin de remplacement.

La mise en œuvre du système basé sur une blockchain fournit également un enregistrement distribué et cohérent que aucun des participants ne peut altérer sans laisser de traces, nous évitons ainsi les comportements malhonnêtes.

Nous avons beaucoup simplifié le scénario de la chaîne d'approvisionnement, mais nous espérons que cette démonstration a montré la puissance de l'utilisation de la blockchain dans ce contexte. Vous pouvez maintenant commencer la planification de votre solution et la considérer comme une alternative de mise en œuvre.

J'espère que vous avez apprécié !