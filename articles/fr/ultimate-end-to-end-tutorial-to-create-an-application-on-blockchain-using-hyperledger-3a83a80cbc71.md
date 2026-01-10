---
title: Comment créer une application sur blockchain en utilisant Hyperledger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T06:03:20.000Z'
originalURL: https://freecodecamp.org/news/ultimate-end-to-end-tutorial-to-create-an-application-on-blockchain-using-hyperledger-3a83a80cbc71
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9B5O5E7KzF2AFHiL4-dtIg.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une application sur blockchain en utilisant Hyperledger
seo_desc: 'By Niharika Singh

  We are going to build a digital bank using Hyperledger Composer. It will have customers
  and accounts. At the end of it, you’ll be able to transfer funds and record all
  transactions on blockchain. We’ll expose a RESTful API for the s...'
---

Par Niharika Singh

Nous allons construire une banque numérique en utilisant Hyperledger Composer. Elle aura des clients et des comptes. À la fin, vous pourrez transférer des fonds et enregistrer toutes les transactions sur la blockchain. Nous exposerons une API RESTful pour la même chose, afin qu'une personne qui n'a aucune idée de ce qu'est la blockchain puisse créer une belle interface utilisateur (UI) autour. Nous créerons également l'interface utilisateur de cette application en Angular.

Je suis super excitée de partager ce guide étape par étape avec vous. Alors commençons tout de suite !

![Image](https://cdn-media-1.freecodecamp.org/images/IMGn4dzREfDI32HrLkU-JSGA1b-NQVlOC3QG)
_Source : [https://giphy.com/explore/excited](https://giphy.com/explore/excited" rel="noopener" target="_blank" title=")_

Lorsque j'ai commencé à coder cela, j'ai rencontré des erreurs. Beaucoup. Mais je pense que c'est bien, car cela m'a permis d'apprendre beaucoup de choses. **Les erreurs sont essentielles.** Je suis arrivée à un point où je pensais que l'allumer et l'éteindre améliorerait les choses. Cela a failli me faire perdre la tête, mais c'est une partie intégrante de la vie de chaque hacker.

Avant de commencer, vous devez vous assurer que la machine que vous utilisez est équipée des configurations requises. Vous devrez peut-être télécharger certaines prérequis et configurer un environnement de développement de base. Voici les liens pour le faire. Suivez ces étapes avant de commencer à développer une application, sinon vous rencontrerez définitivement des erreurs stupides.

Tout d'abord, installez [Hyperledger Composer](https://hyperledger.github.io/composer/installing/installing-prereqs.html). Ensuite, installez [l'environnement de développement](https://hyperledger.github.io/composer/installing/development-tools.html).

Il n'est pas nécessaire de démarrer Playground pendant que vous installez l'environnement.

Assurez-vous que Docker est en cours d'exécution, et lorsque vous exécutez **./startFabric.sh**, cela prendra quelques minutes. Soyez patient.

Maintenant que votre machine est prête, nous pouvons commencer à coder !

![Image](https://cdn-media-1.freecodecamp.org/images/ISfnV6NFxgNcFao2U2fWY-gH3ND8qjxpp4lY)
_Source : [http://www.forthebrokenhearted.net/170254395/4208888/posting/](http://www.forthebrokenhearted.net/170254395/4208888/posting/" rel="noopener" target="_blank" title=")_

#### Étape 1 : Définir votre réseau d'entreprise

Notre définition de réseau d'entreprise (BND) se compose du modèle de données, de la logique de transaction et des règles de contrôle d'accès. Le modèle de données et les règles de contrôle d'accès sont codés dans un langage spécifique au domaine (qui est très simple à assimiler). La logique de transaction sera codée en JavaScript.

Pour créer une BND, nous devons créer une structure de projet appropriée sur le disque. Nous allons créer une structure de réseau d'entreprise squelette en utilisant **Yeoman**. Pour créer une structure de projet, ouvrez votre terminal et exécutez la commande suivante :

```
$ yo hyperledger-composer
```

Cela lancera une série de questions comme suit. Vous devrez utiliser les touches fléchées pour naviguer dans les réponses.

![Image](https://cdn-media-1.freecodecamp.org/images/CF0D-XmKKlo4bmAyumr3l91W90T1o1SIHTko)

Ouvrez ce projet dans votre éditeur de texte préféré. J'utilise Visual Code. Voici à quoi ressemble la structure des fichiers :

![Image](https://cdn-media-1.freecodecamp.org/images/6xQNYHOyB8gCc0qNY7dJTjNEZToXeAdLQlsa)

**Supprimez le contenu de test/logic.js. Nous ne l'utiliserons pas pour le moment.**

#### Étape 2.1 : Coder notre réseau d'entreprise (models/test.cto)

Tout d'abord, nous définirons **models/test.cto**. Il contient les définitions de classe pour tous les actifs, participants et transactions du réseau d'entreprise. Ce fichier est écrit en [langage de modélisation Hyperledger Composer](https://hyperledger.github.io/composer/reference/cto_language.html).

```
namespace test
```

```
asset Account identified by accountId {o String accountId--> Customer ownero Double balance}
```

```
participant Customer identified by customerId {o String customerIdo String firstNameo String lastName}
```

```
transaction AccountTransfer {--> Account from--> Account too Double amount}
```

**Account** est un actif qui est identifié de manière unique par **accountId.** Chaque compte est lié à un **Customer** qui est le **propriétaire** du compte. **Account** a une propriété de **balance** qui indique combien d'argent le compte détient à tout moment.

**Customer** est un participant qui est identifié de manière unique par **customerId.** Chaque **Customer** a un **firstName** et un **lastName**.

**AccountTransfer** est une transaction qui peut se produire **to** et **from** un **Account**. Et combien d'argent doit être transféré est stocké dans **amount.**

#### **Étape 2.2 : Coder le réseau d'entreprise (lib/logic.js)**

Dans ce fichier, nous ajouterons la logique de transaction en JavaScript.

```
/*** Sample transaction* @param {test.AccountTransfer} accountTransfer* @transaction*/
```

```
function accountTransfer(accountTransfer) {if (accountTransfer.from.balance < accountTransfer.to.balance) {throw new Error ("Fonds insuffisants");}
```

```
accountTransfer.from.balance -= accountTransfer.amount;accountTransfer.to.balance += accountTransfer.amount;
```

```
return getAssetRegistry('test.Account').then (function (assetRegistry) {return assetRegistry.update(accountTransfer.from);}).then (function () {return getAssetRegistry('test.Account');}).then(function (assetRegistry) {return assetRegistry.update(accountTransfer.to);});
```

```
}
```

**@param {test.AccountTransfer} accountTransfer** est le décorateur que nous plaçons en haut du fichier pour lier la transaction avec notre fonction JavaScript. Ensuite, nous validons si le compte où se trouvent les fonds a suffisamment d'argent. Sinon, une erreur sera levée. Ensuite, nous effectuons des additions et des soustractions de base sur le solde du compte.

À ce stade, l'étape la plus importante est de mettre à jour cela sur la blockchain. Pour ce faire, nous appelons l'API **getAssetRegistry** de nos actifs qui est Account. Ensuite, nous mettons à jour le **assetRegistry** récupéré pour le compte qui distribue les fonds et le compte qui reçoit les fonds.

#### Étape 3 : Générer l'archive du réseau d'entreprise (BNA)

Maintenant que le réseau d'entreprise a été défini, il doit être packagé dans un fichier d'archive de réseau d'entreprise déployable (`.bna`).

Étape 3.1 : Naviguez dans l'application test-bank dans votre terminal.

Étape 3.2 : Exécutez la commande suivante :

```
$ composer archive create -t dir -n .
```

Cela crée un fichier .bna dans le dossier **test-bank**.

![Image](https://cdn-media-1.freecodecamp.org/images/B3DUtkud4azEoCEoiIKV4PupBCxIPY4XOjLn)

#### Étape 4 : Déployer le fichier d'archive du réseau d'entreprise sur le Fabric

**Étape 4.1 : Installer le runtime composer**

```
$ composer runtime install --card PeerAdmin@hlfv1 --businessNetworkName test-bank
```

![Image](https://cdn-media-1.freecodecamp.org/images/HezXfxt3FVVtnHDfFkPVd6aghaKngGxrQBrF)

**Étape 4.2 : Déployer le réseau d'entreprise**

```
$ composer network start --card PeerAdmin@hlfv1 --networkAdmin admin --networkAdminEnrollSecret adminpw --archiveFile test-bank@0.0.1.bna --file networkadmin.card
```

(Assurez-vous d'être dans le dossier test-bank).

![Image](https://cdn-media-1.freecodecamp.org/images/LSkNP7nxN4tUcY3Dy01M22S6CivgkYLUJL4T)

**Étape 4.3 : Importer l'identité de l'administrateur réseau en tant que carte de réseau d'entreprise utilisable**

```
$ composer card import --file networkadmin.card
```

![Image](https://cdn-media-1.freecodecamp.org/images/keh-Fx-k7zKaN11RaG6LPsedpFTmpfyAF6cC)

**Étape 4.4 :** Pour vérifier que le réseau d'entreprise a été déployé avec succès, **exécutez la commande suivante pour pinguer le réseau :**

```
$ composer network ping --card admin@test-bank
```

![Image](https://cdn-media-1.freecodecamp.org/images/VnU45AuKe6eCuQ82kr9AqTIJqNaeDMZJ-OKM)

#### ÉTAPE 5 : Exposer une API RESTful

Pour créer une API RESTful à partir de votre ligne de commande, exécutez la commande suivante :

```
$ composer-rest-server
```

Cela posera beaucoup de questions.

![Image](https://cdn-media-1.freecodecamp.org/images/0hTic2-uVL1dhxlNfTYlfo9lBdW3lbDr4HEJ)

Maintenant, pointez votre navigateur vers [http://localhost:3000/explorer.](http://localhost:3000/explorer.)

Vous verrez votre belle API blockchain.

![Image](https://cdn-media-1.freecodecamp.org/images/rUfk5ZJuROhQ5ipcqDPXAQ-5LLtIRxYQvyQk)

Maintenant, ajoutons deux clients.

Tout d'abord, ajoutons un client nommé Niharika Singh :

![Image](https://cdn-media-1.freecodecamp.org/images/r9u1KOBTHhA1x5LOelLkurSaFwFaKYS0rVO0)

Nous obtenons un code de réponse 200.

Maintenant, nous ajouterons un client nommé Tvesha Singh de manière similaire.

Pour vérifier si vous les avez ajoutés correctement, obtenez-les.

![Image](https://cdn-media-1.freecodecamp.org/images/v97WNZggvnZFaiYxpWW-pODw2v2D0g7qiWuJ)

Vous verrez deux clients dans le corps de la réponse.

Maintenant, ajoutons 2 comptes liés à ces deux clients.

![Image](https://cdn-media-1.freecodecamp.org/images/GeZJHVxzha7X3ao72H43wwSgQeSsbcxP2m8w)

Ajoutez des comptes de cette manière. Maintenant, obtenez-les pour vérifier si vous les avez ajoutés correctement.

![Image](https://cdn-media-1.freecodecamp.org/images/ByunFMXCKUkDkrZw6QuulazjTZgzRzEry3WD)

Maintenant, transférons 75 de Niharika à Tvesha.

![Image](https://cdn-media-1.freecodecamp.org/images/F99wtlbUc8DVEvRgLOt8XWzMebf5wlbERYNo)

Vérifions si le solde est mis à jour en obtenant les informations du compte.

![Image](https://cdn-media-1.freecodecamp.org/images/EWgbqrF7UtcVQfIRfOPatTdv40TgIYqVHyYg)

Viola ! Cela fonctionne. Niharika a maintenant 25, et Tvesha a 125.

#### Étape 6 : Front End Angular

Pour créer automatiquement l'échafaudage Angular, exécutez la commande suivante dans le dossier test-bank :

```
$ yo
```

Cela posera plusieurs questions.

![Image](https://cdn-media-1.freecodecamp.org/images/vyKb0G94DpcK4yExEBWdhTTJMb6Qav1g3hqW)

Et cela prendra quelques minutes.

Naviguez dans **bank-app.**

```
$ npm start
```

Cela démarre le serveur Angular.

![Image](https://cdn-media-1.freecodecamp.org/images/vCj4O1jxyOR3dEhonZekK-5l1PEVlcRmTMts)

La structure des fichiers Angular est créée comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/65mXKzp9zqtW-lXFUb3jC7ne9jV7QtIfwPQg)

Pointez votre navigateur vers [http://localhost:4200.](http://localhost:4200.) C'est là que la magie opère ! Vous verrez cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/hwqSianiBbujtAhMPwTirT0Le9Sb6wMJ9M1s)

Maintenant, allez dans **Assets** dans le coin supérieur droit et cliquez sur **Account**.

![Image](https://cdn-media-1.freecodecamp.org/images/PuPBiymiOk9Bbyxx90z8WWUPHS9twirN3luf)

Ce sont exactement les comptes que nous avons créés.

Alors maintenant, vous pouvez jouer avec cela.

Vous avez votre front end et votre back end prêts !

Toutes les transactions qui se produisent sur localhost:3000 sont reflétées sur localhost:4200 et vice versa. Et tout cela est sur la blockchain.

![Image](https://cdn-media-1.freecodecamp.org/images/8JLTo8tOyOiLLXdTsxO6KjAD7Vl7befHeWZo)
_Source : [https://giphy.com/explore/thats-how-its-done](https://giphy.com/explore/thats-how-its-done" rel="noopener" target="_blank" title=")_

Récemment, j'ai écrit un article sur les cas d'utilisation de la blockchain. J'ai listé et expliqué 20 idées. Elles peuvent être trouvées ici :

[**Comment l'Inde peut-elle être blockchained ?**](https://medium.com/quillhash/how-can-india-get-blockchained-7f1c7ada98e8)  
[_L'époque de la blockchain vient de commencer et comme toute autre technologie, la blockchain rencontrera également quelques obstacles
2026_medium.com](https://medium.com/quillhash/how-can-india-get-blockchained-7f1c7ada98e8)

> **_Si vous avez une idée d'entreprise et que vous souhaitez la concrétiser avec des détails technologiques et architecturaux, n'hésitez pas à me contacter à niharika.3297@gmail.com_**