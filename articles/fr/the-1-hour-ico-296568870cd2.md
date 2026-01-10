---
title: Comment créer et déployer une offre initiale de pièces (ICO) complète en une
  heure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-26T10:42:12.000Z'
originalURL: https://freecodecamp.org/news/the-1-hour-ico-296568870cd2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nCwrO-nVS4dJevh67knnRw.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: ICO
  slug: ico
- name: Solidity
  slug: solidity
- name: 'tech '
  slug: tech
seo_title: Comment créer et déployer une offre initiale de pièces (ICO) complète en
  une heure
seo_desc: 'By Gilad Haimov

  This article will show you how you can create and deploy a full-fledged ERC20 token
  in less than an hour.

  In the last couple of years the ERC20 token specification has practically become
  the standard for Ethereum tokens. In fact most ...'
---

Par Gilad Haimov

Cet article vous montrera comment créer et déployer un jeton ERC20 complet en moins d'une heure.

Au cours des dernières années, la spécification des jetons ERC20 est pratiquement devenue la norme pour les jetons Ethereum. En fait, la plupart des jetons Ethereum sont conformes à l'ERC20.

Plusieurs facteurs font le succès de l'ERC20 :

1. Il est simple. Vraiment simple. Comme nous allons bientôt le découvrir.
2. Il résout un problème réel : les places de marché blockchain et les portefeuilles cryptographiques ont besoin d'un ensemble unique de commandes pour communiquer avec tous les jetons qu'ils gèrent, y compris les règles d'interaction entre les jetons et les règles d'achat de jetons.
3. C'était la première (ou presque) spécification à offrir une standardisation des jetons Ethereum.

Comme tout autre jeton Ethereum, les jetons ERC-20 sont implémentés sous forme de contrats intelligents et sont exécutés sur la machine virtuelle Ethereum (EVM) de manière décentralisée.

Les contrats intelligents Ethereum sont écrits dans un langage appelé Solidity (il existe d'autres options, mais presque personne ne les utilise). Solidity est quelque peu similaire à JavaScript. En fait, si vous avez quelques connaissances en JavaScript, Java ou d'autres langages de type C, vous comprendrez probablement ce que fait un morceau de code Solidity même avant d'apprendre le langage.

Et maintenant, la partie amusante : créer un contrat ERC20 de base. C'est en fait une tâche plutôt simple. Suffisamment simple pour que nous puissions écrire et déployer votre premier jeton ERC20 en moins d'une heure.

Certes, le jeton que nous allons créer sera une implémentation basique, mais j'ai vu de nombreux jetons basiques qui se portent très bien.

### La Norme

![Image](https://cdn-media-1.freecodecamp.org/images/1*Pn9Fl-H1fuYdnXLsp5WJ6A.png)

#### **Qu'est-ce que ce ERC20 ?**

La norme ERC20 définit un ensemble court et basique de fonctions à implémenter par tous les jetons compatibles ERC20 afin de permettre l'intégration avec d'autres contrats, portefeuilles ou places de marché :

```
 function totalSupply() public view returns (uint256); function balanceOf(address tokenOwner) public view returns (uint); function allowance(address tokenOwner, address spender) public view returns (uint);
```

```
 function transfer(address to, uint tokens) public returns (bool); function approve(address spender, uint tokens)  public returns (bool); function transferFrom(address from, address to, uint tokens) public   returns (bool);
```

Ces fonctions permettront à un utilisateur externe, par exemple un portefeuille, de connaître le solde d'un utilisateur et d'effectuer des transferts de fonds sûrs et autorisés d'un utilisateur à un autre.

De plus, le contrat définit deux événements :

```
event Approval(address indexed tokenOwner, address indexed spender,   uint tokens);event Transfer(address indexed from, address indexed to,   uint tokens);
```

Ces événements seront invoqués ou _émis_ lorsqu'un autre utilisateur aura obtenu le droit de retirer des jetons d'un compte, et lorsque des jetons auront été effectivement transférés.

De nombreux jetons ajoutent également les champs suivants qui sont devenus de facto une partie de la norme :

```
 string public constant name; string public constant symbol; uint8 public constant decimals;
```

En ce qui concerne la nomenclature :

* Une fonction `public` peut être accessible en dehors du contrat lui-même
* `view` signifie essentiellement constant, c'est-à-dire que l'état interne du contrat ne sera pas modifié par la fonction
* Un `event` est la manière de Solidity de permettre aux clients, par exemple votre application frontend, d'être notifiés d'occurrences spécifiques au sein du contrat

Le reste des constructions du langage devrait être clair si vous avez déjà appris Java/JavaScript.

### Le Code

Jusqu'à présent, nous avons discuté de l'interface. Maintenant, écrivons réellement un peu de logique.

Pour cela, nous devrons définir deux objets de mappage, qui est la notion de Solidity pour un tableau associatif ou clé/valeur :

```
 mapping(address => uint256) balances; mapping(address => mapping (address => uint256)) allowed;
```

L'expression `mapping(address => uint256)` définit un tableau associatif dont les clés sont de type `address` — un nombre utilisé pour désigner les adresses de compte, et dont les valeurs sont de type `uint256` — un entier 256 bits typiquement utilisé pour stocker les soldes de jetons.

Le premier objet de mappage, `balances`, contiendra le solde de jetons de chaque compte propriétaire.

Le deuxième objet de mappage, `allowed`, inclura tous les comptes approuvés pour retirer d'un compte donné, ainsi que le montant de retrait autorisé pour chacun.

Comme vous pouvez le voir, le champ de valeur du mappage `allowed` est lui-même un mappage traçant l'adresse du compte à son montant de retrait approuvé.

Ces mappages, ainsi que tous les autres champs du contrat, seront stockés dans la blockchain et seront _minés_, ce qui entraînera la propagation des changements à tous les nœuds utilisateurs du réseau.

Le stockage de la blockchain est coûteux. Il coûte du gaz que les utilisateurs de votre contrat devront payer. Dans la mesure du possible, essayez toujours de minimiser à la fois la taille du stockage et les écritures dans la blockchain.

Maintenant que nous avons les structures de données requises, continuons et écrivons réellement la logique ERC20 dans les fonctions appropriées.

#### Obtenir le nombre total de jetons

Il existe plusieurs approches pour définir le nombre maximal de jetons d'une ICO, et en fait, cette question pourrait mériter une discussion en soi.

Pour nos besoins, nous utiliserons l'approche la plus simple, qui consiste à définir le montant total de jetons au moment de la création du contrat et à les attribuer initialement tous au compte du "propriétaire du contrat", c'est-à-dire le compte qui a déployé le contrat :

```
uint256 totalSupply_;   constructor(uint256 total) public {     totalSupply_ = total;    balances[msg.sender] = _totalSupply; }
```

Un constructeur est une fonction spéciale appelée automatiquement par Ethereum juste après le déploiement du contrat. Vous l'utiliseriez typiquement, comme nous le faisons ici, pour initialiser l'état du jeton en utilisant des paramètres passés par le déployeur du contrat.

`msg` est une variable globale déclarée et peuplée par Ethereum lui-même, et qui contient des données importantes pour l'exécution du devoir du contrat. Le champ que nous utilisons ici : `msg.sender` contient le compte Ethereum exécutant la fonction actuelle du contrat.

Puisque seul le compte de déploiement peut entrer dans le constructeur d'un contrat, ce que fait cette fonction est, au démarrage du contrat, d'allouer tous les jetons disponibles au compte du "propriétaire du contrat".

#### Obtenir l'offre totale de jetons

```
function totalSupply() public view returns (uint256) {   return totalSupply_;}
```

Cette fonction retournera le nombre de tous les jetons alloués par ce contrat, indépendamment de leur propriétaire.

#### Obtenir le solde de jetons du propriétaire

```
function balanceOf(address tokenOwner) public view returns (uint) {   return balances[tokenOwner];}
```

balanceOf retournera le solde actuel de jetons d'un compte, identifié par l'adresse de son propriétaire.

#### Transférer des jetons vers un autre compte

```
function transfer(address receiver,                   uint numTokens) public returns (bool) {   require(numTokens <= balances[msg.sender]);   balances[msg.sender] = balances[msg.sender] - numTokens;   balances[receiver] = balances[receiver] + numTokens;   emit Transfer(msg.sender, receiver, numTokens);   return true;}
```

La fonction `transfer` fait ce que son nom implique, c'est-à-dire déplacer un montant de `numTokens` de jetons du solde du propriétaire vers celui d'un autre utilisateur `receiver`. Notez que le propriétaire du transfert est `msg.sender`, c'est-à-dire celui qui exécute la fonction, ce qui implique que seul le propriétaire des jetons peut les transférer à d'autres.

`require` est la manière de Solidity d'affirmer un prédicat, dans ce cas que le compte de transfert a suffisamment de solde pour transférer. Si une instruction require échoue, la transaction est immédiatement annulée sans aucun changement écrit dans la blockchain.

Juste avant de quitter, la fonction déclenche l'événement ERC20 `Transfer`, permettant aux auditeurs enregistrés de réagir à son achèvement.

#### Autoriser un délégué à retirer des jetons de mon compte

```
function approve(address delegate,                  uint numTokens) public returns (bool) {   allowed[msg.sender][delegate] = numTokens;   emit Approval(msg.sender, delegate, numTokens);   return true;}
```

Cette fonction est typiquement utilisée dans un contexte de place de marché de jetons. Ce qu'elle fait est de permettre à un propriétaire, c'est-à-dire `msg.sender`, d'approuver un compte délégué — éventuellement la place de marché elle-même — à retirer des jetons de son compte et à les transférer à d'autres comptes.

Un cas d'utilisation typique pour ce scénario serait un propriétaire offrant des jetons à la vente sur une place de marché sans avoir besoin de son propre accord avant que la transaction réelle ne se produise. À la fin de son exécution, cette fonction déclenche un événement `Approval`.

#### Obtenir le nombre de jetons approuvés pour le retrait

```
function allowance(address owner,                    address delegate) public view returns (uint) {   return allowed[owner][delegate];}
```

Cette fonction retourne le nombre actuel de jetons approuvés par un propriétaire à un délégué spécifique, tel que défini dans la fonction `approve`.

Transférer des jetons par un délégué :

```
function transferFrom(address owner, address buyer,                       uint numTokens) public returns (bool) {   require(numTokens <= balances[owner]);    require(numTokens <= allowed[owner][msg.sender]);
```

```
   balances[owner] = balances[owner] - numTokens;   allowed[owner][msg.sender] =          allowed[from][msg.sender] - numTokens;   balances[buyer] = balances[buyer] + numTokens;   Transfer(owner, buyer, numTokens);   return true;}
```

`transferFrom` est le pair de la fonction `approve` que nous avons déjà vue. Il permet à un délégué approuvé pour le retrait de transférer effectivement les fonds du propriétaire à un compte tiers.

Les deux instructions `require` au début de la fonction sont destinées à vérifier que la transaction est légale, c'est-à-dire que le propriétaire a suffisamment de jetons à transférer et que le délégué a une autorisation pour au moins `numTokens` à retirer.

Outre le déplacement du montant de `numTokens` du propriétaire à l'acheteur, cette fonction soustrait également `numTokens` de l'autorisation du délégué. Cela permet à un délégué avec une autorisation donnée de la diviser en plusieurs retraits, ce qui est un comportement typique de la place de marché.

En fait, nous pourrions nous arrêter ici et avoir une implémentation ERC20 valide. Mais nous visons plus haut : nous voulons un jeton de qualité industrielle, bien que simple. Cela nous oblige à rendre notre code un peu plus sécurisé.

_SafeMath_ est une bibliothèque Solidity visant à traiter une manière dont les pirates ont été connus pour briser les contrats : l'attaque par débordement d'entier. Dans une telle attaque, le pirate force le contrat à utiliser des valeurs numériques incorrectes en passant des paramètres qui feront dépasser les entiers pertinents **au-delà** de leurs valeurs maximales.

_SafeMath_ protège contre cela en testant le débordement avant d'effectuer l'action arithmétique, éliminant ainsi le danger d'attaque par débordement. Il est également vraiment petit, de sorte que l'impact sur la taille du contrat est minimal, alors utilisons-le.

Tout d'abord, nous l'ajouterons à notre code :

```
library SafeMath { // Seules les fonctions pertinentes
```

```
function sub(uint256 a, uint256 b) internal pure returns (uint256) {   assert(b <= a);   return a - b;} function add(uint256 a, uint256 b) internal pure returns (uint256)   {   uint256 c = a + b;   assert(c >= a);   return c; }}
```

_SafeMath_ utilise des instructions `assert` pour vérifier l'exactitude des paramètres passés. Lorsque `assert` échoue, l'exécution de la fonction est immédiatement arrêtée et toutes les modifications de la blockchain sont annulées.

Ensuite, ajoutons l'instruction suivante pour introduire la bibliothèque au compilateur Solidity :

```
using SafeMath for uint256;
```

et enfin, nous remplacerons l'arithmétique naïve que nous avons utilisée au début par les fonctions SafeMath :

```
 balances[msg.sender] = balances[msg.sender].sub(numTokens); 
```

```
 balances[receiver] = balances[receiver].add(numTokens);   balances[buyer] = balances[buyer].add(numTokens);  balances[owner] = balances[owner].sub(numTokens);
```

#### Assemblons maintenant le tout

Dans Solidity, les fonctions et événements du contrat sont enveloppés dans une entité appelée _contrat_, que vous pouvez traduire silencieusement par une "classe blockchain". Ci-dessous se trouve le contrat compatible ERC20 que nous avons créé jusqu'à présent. Les champs de nom et de symbole peuvent être modifiés à volonté. La plupart des jetons conservent la valeur décimale à 18. Nous ferons de même ici :

### Déploiement du Contrat

Nous allons maintenant déployer notre contrat dans la blockchain. Une fois déployé, le contrat sera transféré à tous les nœuds participant au réseau et toutes les modifications apportées au contrat seront propagées à tous les nœuds participants.

Les professionnels d'Ethereum utilisent généralement des outils de déploiement tels que [Truffle](https://truffleframework.com/).
Pour nos besoins, un simple outil en ligne appelé [Remix](https://remix.ethereum.org/) suffira.

Vous devrez d'abord avoir un plugin [MetaMask](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=en) installé sur votre navigateur (que j'espère être Chrome..) et un compte Rinkeby (réseau de test Ethereum) avec au moins un peu d'Ether Rinkeby. Ces deux prérequis sont hors de notre portée actuelle et sont également assez simples à réaliser.

Si vous n'avez aucun d'entre eux, n'hésitez pas à visiter [MetaMask](https://metamask.io/) et [Rinkeby](https://www.rinkeby.io/#stats)
pour obtenir des instructions claires d'installation et d'utilisation.

En supposant que nous avons les prérequis, nous allons maintenant nous rendre sur [Remix](https://remix.ethereum.org/) et coller le code ci-dessus, y compris la ligne pragma et la bibliothèque SafeMath, dans l'éditeur en ligne.

Après cela, nous passerons au 2ème onglet 'Run' sur le panneau de droite et cliquerons sur 'Deploy'. Une fenêtre contextuelle MetaMask apparaîtra nous demandant de confirmer la transaction, ce que nous ferons bien sûr.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nCwrO-nVS4dJevh67knnRw.png)

* _Marqueur vert : Assurez-vous d'être sur le réseau Rinkeby_
* _Marqueur bleu : Définir l'offre totale de jetons_
* _Marqueur rouge : Déployer !_

**Félicitations !** Vous venez de déployer votre premier jeton ERC20. Il est simple mais entièrement fonctionnel, conforme aux normes, sécurisé et prêt à être acheté, payé et transféré sur l'ensemble du réseau Blockchain !

#### Est-ce tout ?

Pas du tout. Les contrats intelligents peuvent devenir bien plus complexes en fonction de votre logique métier, de votre modélisation de l'interaction utilisateur, de si vous autorisez ou non la création et la destruction de jetons, des changements de cycle de vie que vous introduisez dans le contrat, du besoin de capacités de niveau administrateur qui vient généralement avec un ensemble de fonctions autorisées par l'administrateur et... vous voyez le tableau.

Néanmoins, ce que vous avez accompli ici est une base solide pour avancer lorsque vous aurez besoin d'un contrat plus complexe.

Espérons que ce fut aussi un peu amusant.