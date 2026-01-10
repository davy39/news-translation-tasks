---
title: Un hacker a volé 31 millions de dollars d'Ether — comment c'est arrivé, et
  ce que cela signifie pour Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-20T23:59:31.000Z'
originalURL: https://freecodecamp.org/news/a-hacker-stole-31m-of-ether-how-it-happened-and-what-it-means-for-ethereum-9e5dc29e33ce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8yCGP72sL36SzFYmZfPkaA.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: Security
  slug: security
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Un hacker a volé 31 millions de dollars d'Ether — comment c'est arrivé,
  et ce que cela signifie pour Ethereum
seo_desc: 'By Haseeb Qureshi

  Yesterday, a hacker pulled off the second biggest heist in the history of digital
  currencies.

  Around 12:00 PST, an unknown attacker exploited a critical flaw in the Parity multi-signature
  wallet on the Ethereum network, draining thr...'
---

Par Haseeb Qureshi

Hier, un hacker a réalisé le deuxième plus gros vol de l'histoire des monnaies numériques.

Vers 12h00 PST, un attaquant inconnu a exploité une faille critique dans le portefeuille multi-signatures Parity sur le réseau Ethereum, vidant trois portefeuilles massifs de plus de 31 000 000 $ d'Ether en quelques minutes. Avec quelques heures de plus, le hacker aurait pu s'enfuir avec plus de 180 000 000 $ de portefeuilles vulnérables.

Mais quelqu'un les a arrêtés.

Ayant sonné l'alarme, un groupe de hackers bienveillants (white-hat) de la communauté Ethereum s'est rapidement organisé. Ils ont analysé l'attaque et réalisé qu'il n'y avait aucun moyen d'inverser les vols, mais que de nombreux autres portefeuilles étaient vulnérables. Le temps était essentiel, donc ils n'ont vu qu'une seule option disponible : **pirater les portefeuilles restants avant que l'attaquant ne le fasse.**

En exploitant la même vulnérabilité, les white-hats ont [piraté tous les portefeuilles restants à risque](https://etherscan.io/address/0x1dba1131000664b884a1ba238464159892252d3a) et vidé leurs comptes, empêchant ainsi efficacement l'attaquant d'accéder aux 150 000 000 $ restants.

_Oui, vous avez bien lu._

Pour empêcher le hacker de voler d'autres banques, les white-hats ont écrit un logiciel pour voler toutes les banques restantes dans le monde. Une fois l'argent volé en toute sécurité, ils ont commencé le processus de restitution des fonds à leurs détenteurs respectifs. Les personnes dont l'argent a été sauvé par cet exploit héroïque sont maintenant en train de récupérer leurs fonds.

C'est une histoire extraordinaire, et elle a des implications significatives pour le monde des cryptomonnaies.

**Il est important de comprendre que cette faille n'était pas une vulnérabilité dans Ethereum ou dans Parity lui-même.** Il s'agissait plutôt d'une vulnérabilité dans le code de contrat intelligent par défaut que le client Parity donne à l'utilisateur pour déployer des portefeuilles multi-signatures.

C'est assez compliqué, donc pour clarifier les détails pour tout le monde, cet article est divisé en trois parties :

1. **Que s'est-il passé exactement ?** Une explication d'Ethereum, des contrats intelligents et des portefeuilles multi-signatures.
2. **Comment ont-ils fait ?** Une explication technique de l'attaque (spécifiquement pour les programmeurs).
3. **Et maintenant ?** Les implications de l'attaque sur l'avenir et la sécurité des contrats intelligents.

Si vous êtes familier avec Ethereum et le monde des cryptomonnaies, vous pouvez passer à la deuxième section.

### 1. Que s'est-il passé exactement ?

Il y a trois éléments clés à cette histoire : **Ethereum**, **les contrats intelligents** et **les portefeuilles numériques**.

![Image](https://cdn-media-1.freecodecamp.org/images/XeGxrCaAhPoDnakHA9Q7zmccXovYiRbwHyCY)

[Ethereum](https://www.ethereum.org/) est une monnaie numérique inventée en 2013 — soit 4 ans après la sortie de Bitcoin. Elle est depuis devenue la deuxième plus grande monnaie numérique au monde en termes de capitalisation boursière — 20 milliards de dollars, contre 40 milliards pour Bitcoin.

Comme toutes les cryptomonnaies, Ethereum est un descendant du protocole Bitcoin et améliore la conception de Bitcoin. Mais ne vous y trompez pas : bien qu'il s'agisse d'une monnaie numérique comme Bitcoin, Ethereum est bien plus puissant.

Alors que Bitcoin utilise sa blockchain pour implémenter un registre de transactions monétaires, Ethereum utilise sa blockchain pour enregistrer les transitions d'état dans un ordinateur distribué géant. La monnaie numérique correspondante d'Ethereum, l'ether, est essentiellement un effet secondaire de l'alimentation de cet ordinateur massif.

En d'autres termes, _Ethereum est littéralement un ordinateur qui s'étend à travers le monde entier_. Toute personne qui exécute le logiciel Ethereum sur son ordinateur participe aux opérations de cet ordinateur mondial, la Machine Virtuelle Ethereum (EVM). Parce que l'EVM a été conçue pour être [Turing-complète](https://en.wikipedia.org/wiki/Turing_completeness) (en ignorant les limites de gaz), elle peut faire presque tout ce qui peut être exprimé dans un programme informatique.

Permettez-moi d'être emphatique : _c'est du lourd_. Le monde des cryptomonnaies est enthousiaste quant au potentiel d'Ethereum, dont la valeur a grimpé en flèche au cours des six derniers mois.

![Image](https://cdn-media-1.freecodecamp.org/images/UD5RQRBlzIToGL-PRW4P6cVwVSDMiQrjytca)

La communauté des développeurs s'est ralliée derrière lui, et il y a beaucoup d'excitation quant à ce qui peut être construit sur l'EVM — et cela nous amène aux contrats intelligents.

**Les contrats intelligents** sont simplement des programmes informatiques qui s'exécutent sur l'EVM. À bien des égards, ils ressemblent à des contrats normaux, sauf qu'ils n'ont pas besoin d'avocats ou de juges pour les interpréter. Au lieu de cela, ils sont compilés en bytecode et interprétés de manière unambiguë par l'EVM. Avec ces programmes, vous pouvez (entre autres) transférer de manière programmatique des monnaies numériques basées uniquement sur les règles du code du contrat.

Bien sûr, il y a des choses que les contrats normaux font et que les contrats intelligents ne peuvent pas — les contrats intelligents ne peuvent pas facilement interagir avec des choses qui ne sont pas sur la blockchain. Mais les contrats intelligents peuvent aussi faire des choses que les contrats normaux ne peuvent pas, comme appliquer un ensemble de règles entièrement par une cryptographie infaillible.

Cela nous amène à la notion de **portefeuilles**. Dans le monde des monnaies numériques, les portefeuilles sont la manière dont vous stockez vos actifs. Vous accédez à votre portefeuille en utilisant essentiellement un mot de passe secret, également connu sous le nom de clé privée ([simplifié un peu](http://searchsecurity.techtarget.com/definition/asymmetric-cryptography)).

Il existe de nombreux types de portefeuilles différents qui confèrent différentes propriétés de sécurité, comme des limites de retrait. L'un des types les plus populaires est le portefeuille multi-signatures.

Dans un portefeuille multi-signatures, il y a plusieurs clés privées qui peuvent déverrouiller le portefeuille, mais une seule clé ne suffit pas pour le déverrouiller. Si votre portefeuille multi-signatures a 3 clés, par exemple, vous pouvez spécifier qu'au moins 2 des 3 clés doivent être fournies pour le déverrouiller avec succès.

Cela signifie que si vous, votre père et votre mère êtes chacun signataires de ce portefeuille, même si un criminel piratait votre mère et volait sa clé privée, il ne pourrait toujours pas accéder à vos fonds. Cela conduit à des garanties de sécurité beaucoup plus fortes, donc les multi-sigs sont un standard en matière de sécurité des portefeuilles.

C'est le type de portefeuille que le hacker a attaqué.

Alors, qu'est-ce qui a mal tourné ? Ont-ils cassé les clés privées ? Ont-ils utilisé un ordinateur quantique, ou un algorithme de factorisation de pointe ?

Non, toute la cryptographie était solide. L'exploit était presque ridicule de simplicité : ils ont trouvé un bug introduit par le programmeur dans le code qui leur permettait de réinitialiser le portefeuille, presque comme le restaurer aux paramètres d'usine. Une fois qu'ils ont fait cela, ils étaient libres de se définir comme les nouveaux propriétaires, puis de partir avec tout.

### 2. Comment cela s'est-il produit ?

Ce qui suit est une explication technique de ce qui s'est passé exactement. Si vous n'êtes pas développeur, n'hésitez pas à passer à la section suivante, car cela va être très technique.

Ethereum a un modèle de programmation assez unique. Sur Ethereum, vous écrivez du code en publiant des contrats (que vous pouvez considérer comme des objets), et les transactions sont exécutées en appelant des méthodes sur ces objets pour muter leur état.

Pour exécuter du code sur Ethereum, vous devez d'abord déployer le contrat (le déploiement est lui-même une transaction), ce qui coûte une petite quantité d'Ether. Vous devez ensuite appeler des méthodes sur le contrat pour interagir avec lui, ce qui coûte plus d'Ether. Comme vous pouvez l'imaginer, cela incite un programmeur à optimiser son code, à la fois pour minimiser les transactions et minimiser les coûts de calcul.

Une façon de réduire les coûts est d'utiliser des bibliothèques. En faisant en sorte que votre contrat appelle une bibliothèque partagée qui a été déployée à un moment précédent, vous n'avez pas à redéployer de code partagé. Dans Ethereum, garder votre code DRY vous fera directement économiser de l'argent.

Le portefeuille multi-sig par défaut dans Parity a fait exactement cela. Il contenait une référence à une bibliothèque externe partagée qui contenait la logique d'initialisation du portefeuille. Cette bibliothèque partagée est référencée par la clé publique du contrat de la bibliothèque.

```
// CHAMPS
address constant _walletLibrary = 0xa657491c1e7f16adb39b9b60e87bbb8d93988bc3;
```

La bibliothèque est appelée à plusieurs endroits, via une instruction EVM appelée `DELEGATECALL`, qui fait ce qui suit : pour toute méthode qui appelle `DELEGATECALL`, elle appellera la même méthode sur le contrat auquel vous déléguez, mais en utilisant le contexte du contrat actuel. C'est essentiellement comme un appel `super`, sauf sans la partie héritage. (L'équivalent en JavaScript serait `OtherClass.functionName.apply(this, args)`.)

Voici un exemple de cela dans leur portefeuille multi-sig : la méthode `isOwner` délègue simplement à la méthode `isOwner` de la bibliothèque de portefeuille partagée, en utilisant l'état du contrat actuel :

```
function isOwner(address _addr) constant returns (bool) {
    return _walletLibrary.delegatecall(msg.data);
}
```

C'est tout à fait innocent. Le portefeuille multi-sig lui-même contenait toutes les vérifications de permissions appropriées, et ils se sont assurés de faire respecter rigoureusement l'autorisation sur toutes les actions sensibles liées à l'état du portefeuille.

Mais ils ont fait une erreur critique.

Solidity permet de définir une "méthode de repli". Il s'agit de la méthode qui est appelée lorsqu'il n'y a pas de méthode correspondant à un nom de méthode donné. Vous la définissez en ne lui donnant pas de nom :

```
function() {
    // faire des choses ici pour toutes les méthodes inconnues
}
```

L'équipe Parity a décidé de laisser toute méthode inconnue envoyant de l'Ether au contrat simplement déposer l'Ether envoyé par défaut.

```
function() payable {
    // payable est juste un mot-clé qui signifie que cette méthode peut recevoir/payer de l'Ether
```

```
if (msg.value > 0) {
    // juste en train de recevoir de l'argent ?
    Deposit(msg.sender, msg.value);
    } else {
    throw;  }
```
```
}
```

Mais ils sont allés plus loin, et voici leur erreur critique. Voici le _code réel qui a été attaqué_.

```
function() payable {
    // juste en train de recevoir de l'argent ?
  if (msg.value > 0)
    Deposit(msg.sender, msg.value);
  else if (msg.data.length > 0)
    _walletLibrary.delegatecall(msg.data);
}
```

En gros :

* Si le nom de la méthode n'est pas défini sur ce contrat...
* Et qu'il n'y a pas d'ether envoyé dans la transaction...
* Et qu'il y a des données dans la charge utile du message...

Alors il appellera la méthode exacte si elle est définie dans `_walletLibrary`, mais dans le contexte de ce contrat.

En utilisant cela, l'attaquant a appelé une méthode appelée `initWallet()`, qui n'était pas définie sur le contrat multisig _mais qui était_ définie dans la bibliothèque de portefeuille partagée :

```
function initWallet(address[] _owners, uint _required, uint _daylimit) {
    initDaylimit(_daylimit);
  initMultiowned(_owners, _required);
}
```

Qui appelle la méthode `initMultiowned`...

```
function initMultiowned(address[] _owners, uint _required) {
    m_numOwners = _owners.length + 1;
  m_owners[1] = uint(msg.sender);
  m_ownerIndex[uint(msg.sender)] = 1;
  for (uint i = 0; i < _owners.length; ++i)
  {
    m_owners[2 + i] = uint(_owners[i]);
    m_ownerIndex[uint(_owners[i])] = 2 + i;
  }
  m_required = _required;
}
```

Voyez-vous ce qui vient de se passer ? L'attaquant a essentiellement **réinitialisé le contrat** en déléguant via la méthode de la bibliothèque, écrasant les propriétaires du contrat original. Lui et tout tableau de propriétaires qu'il fournit comme arguments seront les nouveaux propriétaires.

Étant donné qu'ils contrôlent désormais l'ensemble du portefeuille, ils peuvent extraire trivialement le reste du solde. Et c'est précisément ce qu'ils ont fait.

L'initWallet : [https://etherscan.io/tx/0x707aabc2f24d756480330b75fb4890ef6b8a26ce0554ec80e3d8ab105e63db07](https://etherscan.io/tx/0x707aabc2f24d756480330b75fb4890ef6b8a26ce0554ec80e3d8ab105e63db07)

Le transfert :   
[https://etherscan.io/tx/0x9654a93939e98ce84f09038b9855b099da38863b3c2e0e04fd59a540de1cb1e5](https://etherscan.io/tx/0x9654a93939e98ce84f09038b9855b099da38863b3c2e0e04fd59a540de1cb1e5)

Alors, quelle était finalement la vulnérabilité ? On pourrait dire qu'il y en avait deux. Premièrement, `initWallet` et `initMultiowned` dans la bibliothèque de portefeuille n'étaient pas marqués comme `internal` (ce qui est comme une méthode `private`, qui aurait empêché cet appel délégué), et ces méthodes ne vérifiaient pas que le portefeuille n'était pas déjà initialisé. L'une ou l'autre de ces vérifications aurait rendu ce piratage impossible.

La deuxième vulnérabilité était le `delegateCall` brut. Vous pouvez penser à cela comme équivalent à une instruction `eval` brute, s'exécutant sur une chaîne fournie par l'utilisateur. Dans une tentative d'être concis, ce contrat a utilisé la métaprogrammation pour proxy des appels de méthodes potentiels à une bibliothèque sous-jacente. L'approche plus sûre ici aurait été de lister les méthodes spécifiques que l'utilisateur est autorisé à appeler.

Le problème, bien sûr, est que cela est plus coûteux en termes de coûts de gaz (puisqu'il doit évaluer plus de conditionnelles). Mais lorsqu'il s'agit de sécurité, nous devons probablement surmonter cette préoccupation lors de l'écriture de contrats intelligents qui déplacent des sommes d'argent massives.

_C'était donc l'attaque._

C'était une découverte astucieuse, mais une fois que vous la pointez, elle semble presque élémentaire. L'attaquant a ensuite sauté sur cette vulnérabilité pour trois des plus grands portefeuilles qu'il pouvait trouver — mais à en juger par les temps de transaction, il faisait cela entièrement manuellement.

Le groupe de white-hats le faisait à grande échelle en utilisant des scripts, et c'est pourquoi ils ont pu battre l'attaquant de vitesse. Étant donné cela, il est peu probable que l'attaquant était très sophistiqué dans la manière dont il a planifié son attaque.

Vous pourriez vous poser la question cependant — pourquoi ne pas simplement annuler ce piratage, comme ils l'ont fait avec le [piratage de la DAO](https://www.cryptocompare.com/coins/guides/the-dao-the-hack-the-soft-fork-and-the-hard-fork/) ?

Malheureusement, ce n'est pas vraiment possible. Le piratage de la DAO était unique en ce sens que lorsque l'attaquant a vidé la DAO dans une DAO enfant, les fonds étaient gelés pendant de nombreux jours à l'intérieur d'un contrat intelligent avant de pouvoir être libérés à l'attaquant.

Cela a empêché les fonds volés d'entrer en circulation, donc l'Ether volé était effectivement mis en silo. Cela a donné à la communauté Ethereum beaucoup de temps pour conduire un quorum public sur la manière de traiter l'attaque.

Dans cette attaque, l'attaquant a immédiatement volé les fonds et pouvait commencer à les dépenser. Un hard fork serait impraticable — que faites-vous de toutes les transactions qui se produisent en aval ? Et les personnes qui ont échangé des actifs de manière innocente avec l'attaquant ? Une fois que l'ether qu'ils ont volé est blanchi et entre en circulation générale, c'est comme des billets contrefaits circulant dans l'économie — il est facile de s'arrêter lorsqu'ils sont tous dans une mallette, mais une fois que tout le monde détient potentiellement un billet contrefait, vous ne pouvez plus vraiment revenir en arrière.

Donc la transaction ne sera pas inversée. La perte de 31 millions de dollars reste. C'est une leçon coûteuse, mais nécessaire.

Alors, que devons-nous retenir de cela ?

### 3. Que signifie cette attaque pour Ethereum ?

Il y a plusieurs enseignements importants ici.

**Tout d'abord, rappelez-vous, ce n'était pas une faille dans Ethereum ou dans les contrats intelligents en général. Il s'agissait plutôt d'une erreur de développeur dans un contrat particulier.**

Alors, qui étaient les développeurs farfelus qui ont écrit cela ? Ils auraient dû savoir mieux, non ?

[Les développeurs ici](https://blog.parity.io/the-multi-sig-hack-a-postmortem/) étaient une collaboration croisée entre la fondation Ethereum (littéralement les créateurs d'Ethereum), l'équipe principale de Parity, et des membres de la communauté open-source. Il a subi un examen approfondi par les pairs. C'est essentiellement le standard de programmation le plus élevé qui existe dans l'écosystème Ethereum.

Ces développeurs étaient humains. Ils ont fait une erreur. Et il en va de même pour les réviseurs qui ont audité ce code.

J'ai lu certains commentaires sur Reddit et HackerNews du genre : « Quelle erreur évidente ! Comment était-il même possible qu'ils l'aient manquée ? » (En ignorant que la vulnérabilité « évidente » a été introduite en janvier et n'a été découverte que maintenant.)

Lorsque je vois des réponses comme celle-ci, je sais que les personnes qui commentent ne sont pas des développeurs professionnels. Pour un développeur sérieux, la réaction est plutôt : _putain, c'était une erreur stupide. Je suis content de ne pas être celui qui l'a faite._

Des erreurs de ce genre sont **routinièrement** commises en programmation. Tous les programmes comportent le risque d'erreur du développeur. Nous devons nous débarrasser de l'état d'esprit « si ils avaient été plus prudents, cela ne serait pas arrivé ». À une certaine échelle, la prudence ne suffit pas.

À mesure que les programmes atteignent une complexité non triviale, vous devez commencer à considérer comme _acquis_ que les programmes ne sont probablement pas corrects. Aucune quantité de diligence humaine ou de tests n'est suffisante pour prévenir tous les bugs possibles. Même des organisations comme Google ou la NASA commettent des erreurs de programmation, malgré la rigueur extrême qu'elles appliquent à leur code le plus critique.

Nous ferions bien de prendre une page des pratiques de fiabilité des sites chez des entreprises comme Google et Airbnb. Chaque fois qu'il y a un bug de production ou une panne, ils font une analyse post-mortem et la distribuent au sein de l'entreprise. Dans ces post-mortems, il y a toujours un principe de _ne jamais blâmer les individus_.

Blamer les erreurs sur les individus est inutile, car tous les programmeurs, peu importe leur expérience, ont une probabilité non nulle de faire une erreur. Au lieu de cela, le but d'un post-mortem est d'identifier ce qui, dans le processus, a permis à cette erreur d'être déployée.

Le problème n'était pas que le développeur a oublié d'ajouter `internal` à la bibliothèque de portefeuille, ou qu'il a fait un `delegateCall` brut sans vérifier quelle méthode était appelée.

**Le problème est que leur chaîne d'outils de programmation leur a permis de faire ces erreurs.**

À mesure que l'écosystème des contrats intelligents évolue, il doit évoluer dans le sens de rendre ces erreurs plus difficiles, et cela signifie rendre les contrats sécurisés par défaut.

Cela m'amène à mon prochain point.

**La force est une faiblesse** lorsqu'il s'agit de langages de programmation. Plus un langage de programmation est fort et expressif, plus son code devient complexe. Solidity est un langage très complexe, modélisé pour ressembler à Java.

_La complexité est l'ennemi de la sécurité_. Les programmes complexes sont plus difficiles à raisonner et plus difficiles à identifier les cas limites. Je pense que des langages comme [Viper](https://github.com/ethereum/viper) (maintenu par Vitalik Buterin) sont une étape prometteuse dans cette direction. Viper inclut par défaut des mécanismes de sécurité de base, tels que des constructions de boucle bornées, pas de débordements d'entiers, et empêche d'autres bugs de base que les développeurs ne devraient pas avoir à raisonner.

Moins le langage vous permet de faire, plus il est facile d'analyser et de prouver les propriétés d'un contrat. La sécurité est difficile car la seule façon de prouver une affirmation positive comme « ce contrat est sécurisé » est de réfuter chaque vecteur d'attaque possible : « ce contrat ne peut pas être réinitialisé », « ses fonds ne peuvent pas être accessibles sauf par les propriétaires », etc. Moins vous avez de vecteurs d'attaque possibles à considérer, plus il est facile de développer un contrat sécurisé.

Un modèle de programmation plus simple permet également des choses comme la [vérification formelle](https://en.wikipedia.org/wiki/Formal_verification) et la génération automatique de tests. Ce sont des domaines en recherche active, mais tout comme les contrats intelligents ont incorporé la cryptographie de pointe, ils devraient également commencer à incorporer l'avant-garde de la conception des langages de programmation.

Il y a une leçon plus grande ici aussi.

La plupart des programmeurs qui entrent dans cet espace, moi y compris, viennent d'un milieu de développement web, et la chaîne d'outils blockchain est conçue pour être familière pour les développeurs web. Solidity a atteint une adoption énorme dans la communauté des développeurs grâce à sa familiarité avec d'autres formes de programmation. D'une certaine manière, cela pourrait finir par être sa perte.

Le problème est que **la programmation blockchain est fondamentalement différente du développement web**.

Permettez-moi d'expliquer.

Avant l'ère du modèle web client-serveur, la plupart de la programmation était faite pour des logiciels consommateurs emballés ou sur des systèmes embarqués. C'était avant l'ère des mises à jour logicielles automatiques. Dans ces programmes, un produit expédié était final — vous publiiez une forme de votre logiciel tous les 6 mois, et s'il y avait un bug, ce bug devrait rester jusqu'à la prochaine version. En raison de ce cycle de développement plus long, toutes les versions de logiciels étaient rigoureusement testées dans toutes les circonstances concevables.

Le développement web est beaucoup plus indulgent. Lorsque vous poussez du mauvais code sur un serveur web, ce n'est pas grave s'il y a une erreur critique — vous pouvez simplement revenir en arrière avec le code, ou avancer avec une correction, et tout va bien parce que vous contrôlez le serveur. Ou si le pire se produit et qu'il y a une brèche active ou une fuite de données, vous pouvez toujours arrêter l'hémorragie en éteignant vos serveurs et en vous déconnectant du réseau.

_Ces deux modèles de développement sont fondamentalement différents._ C'est seulement à partir de quelque chose comme le développement web que vous pouvez obtenir la devise « avancer vite et casser des choses ».

La plupart des programmeurs aujourd'hui sont formés au modèle de développement web. Malheureusement, le modèle de sécurité de la blockchain est plus proche de l'ancien modèle.

Dans la blockchain, le code est intrinsèquement irréversible. Une fois que vous déployez un mauvais contrat intelligent, n'importe qui est libre de l'attaquer aussi longtemps et aussi fort qu'il le peut, et il n'y a aucun moyen de le reprendre s'ils y parviennent en premier. À moins que vous ne construisiez des mécanismes de sécurité intelligents dans vos contrats, s'il y a un bug ou une attaque réussie, il n'y a aucun moyen d'éteindre vos serveurs et de corriger l'erreur. Être sur Ethereum signifie par définition que _tout le monde_ possède votre serveur.

Un dicton courant en cybersécurité est « l'attaque est toujours plus facile que la défense ». La blockchain multiplie fortement ce déséquilibre. Il est beaucoup plus facile d'attaquer car vous avez accès au code de chaque contrat, savez combien d'argent il contient, et pouvez prendre tout le temps que vous voulez pour essayer de l'attaquer. Et une fois que votre attaque est réussie, vous pouvez potentiellement voler _tout l'argent_ du contrat.

Imaginez que vous déployiez un logiciel pour des distributeurs automatiques. Mais au lieu qu'un bug ne vous permette que de voler des bonbons d'une seule machine, le bug vous permettait de voler simultanément des bonbons de toutes les machines du monde qui utilisaient ce logiciel. Oui, c'est ainsi que fonctionne la blockchain.

En cas d'attaque réussie, la défense est extrêmement difficile. Les white-hats du piratage de Parity ont démontré à quel point leurs options de défense étaient limitées — il n'y avait aucun moyen de sécuriser ou de démanteler les contrats, ou même de pirater l'argent volé ; tout ce qu'ils pouvaient faire était de pirater les contrats vulnérables restants avant que l'attaquant ne le fasse.

Cela pourrait sembler annoncer un avenir sombre.

_Mais je ne pense pas que ce soit un glas pour la programmation blockchain._ Cela confirme plutôt ce que tout le monde sait déjà : cet écosystème est jeune et immature. Il faudra beaucoup de travail pour développer la formation et la discipline nécessaires pour traiter les contrats intelligents de la même manière que les banques traitent leur logiciel de guichet automatique. Mais nous allons devoir y parvenir pour que la blockchain soit couronnée de succès à long terme.

Cela signifie non seulement que les programmeurs doivent mûrir et recevoir plus de formation. Cela signifie également développer des outils et des langages qui rendent tout cela plus facile, et nous donnent des garanties rigoureuses sur notre code.

C'est encore tôt. Ethereum est un travail en cours, et il change rapidement. Vous ne devriez pas traiter Ethereum comme une banque ou comme un remplacement pour l'infrastructure financière. Et certainement, vous ne devriez pas stocker d'argent dans un [portefeuille chaud](https://en.bitcoin.it/wiki/Hot_wallet) que vous n'êtes pas à l'aise de perdre.

Mais malgré tout cela, je pense toujours qu'Ethereum va gagner à long terme. Et voici pourquoi : **la communauté des développeurs dans Ethereum est ce qui le rend si puissant**.

Ethereum ne vivra ou ne mourra pas à cause de l'argent qu'il contient. Il vivra ou mourra en fonction des développeurs qui se battent pour lui.

La ligue de white-hats qui s'est réunie et a défendu les portefeuilles vulnérables ne l'a pas fait pour l'argent. Ils l'ont fait parce qu'ils croient en cet écosystème. Ils veulent qu'Ethereum prospère. Ils veulent voir leur vision de l'avenir se réaliser. Et après toute la spéculation et le profit, ce sont finalement ces personnes qui vont guider la communauté vers son avenir. Ils sont fondamentalement la raison pour laquelle Ethereum gagnera à long terme — ou si ils abandonnent Ethereum, leur abandon sera la raison pour laquelle il perdra.

Cette attaque est importante. Elle va secouer les gens. Elle va forcer la communauté à examiner de près les meilleures pratiques de sécurité. Elle va forcer les développeurs à traiter la programmation des contrats intelligents avec beaucoup plus de rigueur qu'ils ne le font actuellement.

Mais cette attaque n'a pas ébranlé la force des constructeurs qui travaillent sur ce sujet. En ce sens, c'est un revers temporaire.

En fin de compte, des attaques comme celle-ci sont bonnes pour la communauté pour grandir. Elles vous appellent à vos sens et vous forcent à garder les yeux ouverts. Cela fait mal, et la presse va probablement en faire un gâchis. Mais chaque blessure rend la communauté plus forte, et nous rapproche de la compréhension profonde de la technologie de la blockchain — à la fois ses dangers, et son potentiel incroyable.

P.S. Si vous êtes un développeur et que vous voulez en savoir plus sur la sécurité des contrats intelligents, [voici une très bonne ressource.](https://github.com/ConsenSys/smart-contract-best-practices#known-attacks)

_Errata : Cet article disait à l'origine que Gavin Wood était le développeur du contrat, ce qui est incorrect. Gavin est le fondateur de Parity et a poussé la correction du contrat, mais n'était pas le développeur original. Il affirmait également à l'origine que 77 millions de dollars supplémentaires étaient vulnérables, mais cela ne compte pas tous les jetons ERC20 (ICO) qui étaient vulnérables. [Le montant total est en fait de 150 000 000 $ si vous incluez tous les jetons ERC20.](https://etherscan.io/address/0x1dba1131000664b884a1ba238464159892252d3a) Au moment de la rédaction de cet article (21 juillet 16h00 EST), la valeur totale des actifs sauvés par les white-hats était de 179 704 659 $.