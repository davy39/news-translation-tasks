---
title: Comment construire un réseau blockchain en utilisant Hyperledger Fabric et
  Composer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-24T22:54:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-blockchain-network-using-hyperledger-fabric-and-composer-e06644ff801d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iGuxOX8a2_jCdQEd
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment construire un réseau blockchain en utilisant Hyperledger Fabric
  et Composer
seo_desc: 'By Haardik

  A tutorial for new blockchain developers


  _Photo by [Unsplash](https://unsplash.com/@alexacea?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Alexandru Acea on <a href="https://unsplash.com?utm_source=medium&...'
---

Par Haardik

#### Un tutoriel pour les nouveaux développeurs blockchain

![Image](https://cdn-media-1.freecodecamp.org/images/0*iGuxOX8a2_jCdQEd)
_Photo par [Unsplash](https://unsplash.com/@alexacea?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Alexandru Acea</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Avant de commencer, Hyperledger Fabric **ne fonctionne que** sur les systèmes d'exploitation basés sur Unix. Par conséquent, il ne pourra pas fonctionner sur Windows et vous aurez des restrictions sur ce que vous pouvez faire. Je suggère de configurer une machine virtuelle si vous utilisez Windows avant de continuer.

Cet article suppose une certaine connaissance de Javascript. Ce n'est pas un tutoriel destiné aux programmeurs débutants, mais plutôt aux programmeurs qui sont débutants dans le domaine de la blockchain.

### Que construisons-nous ?

Alors, vous voulez construire une application blockchain mais vous ne savez pas par où commencer ? Ne vous inquiétez pas. À travers ce tutoriel, nous allons configurer un réseau de cartes à échanger. Différents `Trader`s qui possèdent des `TradingCard`s de joueurs de Baseball, Football et Cricket pourront échanger des cartes entre eux.

Nous allons également configurer un serveur REST API pour permettre aux logiciels côté client d'interagir avec notre réseau d'entreprise. Enfin, nous allons également générer une application Angular 4 qui utilise l'API REST pour interfacer avec notre réseau.

Vous pouvez trouver le code final complet de ce que nous allons construire sur ce [dépôt Github](https://github.com/haardikk21/cards-trading-network)

Êtes-vous prêt à commencer ?

### Table des matières

* Introduction à Hyperledger Fabric et aux applications connexes
* Installation des prérequis, des outils et d'un runtime Fabric
* Création et déploiement de notre réseau d'entreprise
* Test de notre réseau d'entreprise
* Génération d'un serveur REST API
* Génération d'une application Angular qui utilise l'API REST

### Introduction à Hyperledger Fabric et aux applications connexes

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ma2ZQgFeXiAUYGeb)
_Aperçu de l'environnement de développement pour Hyperledger_

**Hyperledger Fabric** est un framework open source pour créer des réseaux d'entreprise blockchain privés (avec autorisation), où les identités et les rôles des membres sont connus des autres membres. Le réseau construit sur Fabric sert de backend, avec une application frontend côté client. Des SDK sont disponibles pour Nodejs et Java pour construire des applications client, avec un support pour Python et Golang à venir.

**Hyperledger Composer** est un ensemble d'outils et de scripts basés sur Javascript qui simplifient la création de réseaux Hyperledger Fabric. En utilisant ces outils, nous pouvons générer une **archive de réseau d'entreprise (BNA)** pour notre réseau. Composer couvre principalement ces composants :

* Archive de réseau d'entreprise (BNA)
* Composer Playground
* Serveur REST Composer

**Archive de réseau d'entreprise** — Composer nous permet d'emballer différents fichiers et de générer une archive qui peut ensuite être déployée sur un réseau Fabric. Pour générer cette archive, nous avons besoin de :

* **Modèle de réseau** — Une définition des ressources présentes dans le réseau. Ces ressources incluent les Actifs, les Participants et les Transactions. Nous reviendrons sur ces éléments plus tard.
* **Logique métier** — Logique pour les fonctions de transaction
* **Limitations de contrôle d'accès** — Contient diverses règles qui définissent les droits des différents participants dans le réseau. Cela inclut, sans s'y limiter, la définition des Actifs que les Participants peuvent contrôler.
* **Fichier de requête (optionnel)** — Un ensemble de requêtes qui peuvent être exécutées sur le réseau. Celles-ci peuvent être considérées comme similaires aux requêtes SQL. Vous pouvez en lire plus sur les requêtes [ici](https://hyperledger.github.io/composer/latest/reference/query-language).

**Composer Playground** est une interface utilisateur basée sur le web que nous pouvons utiliser pour modéliser et tester notre réseau d'entreprise. Playground est bon pour modéliser des preuves de concept simples, car il utilise le stockage local du navigateur pour simuler le réseau blockchain. Cependant, si nous exécutons un runtime Fabric local et avons déployé un réseau dessus, nous pouvons également y accéder en utilisant Playground. Dans ce cas, Playground ne simule pas le réseau, il communique directement avec le runtime Fabric local.

**Composer REST Server** est un outil qui nous permet de générer un serveur REST API basé sur notre définition de réseau d'entreprise. Cette API peut être utilisée par des applications client et nous permet d'intégrer des applications non-blockchain dans le réseau.

### Installation des prérequis, des outils et d'un runtime Fabric

#### **1. Installation des prérequis**

Maintenant que nous avons une compréhension de haut niveau de ce qui est nécessaire pour construire ces réseaux, nous pouvons commencer à développer. Avant de faire cela, nous devons nous assurer que nous avons les prérequis installés sur notre système. Une liste mise à jour peut être trouvée [ici](https://hyperledger.github.io/composer/latest/installing/installing-prereqs.html).

* Moteur Docker et Docker Compose
* Nodejs et NPM
* Git
* Python 2.7.x

Pour les utilisateurs d'Ubuntu, Hyperledger dispose d'un script bash disponible pour rendre ce processus extrêmement facile. Exécutez les commandes suivantes dans votre terminal :

Malheureusement, les utilisateurs de Mac doivent installer manuellement les outils mentionnés ci-dessus et s'assurer qu'ils ont tous les prérequis sur leur système. [Cette page](https://hyperledger.github.io/composer/latest/installing/installing-prereqs.html) est maintenue à jour avec les instructions d'installation.

#### 2. **Installation des outils pour faciliter le développement**

Exécutez les commandes suivantes dans votre Terminal, et assurez-vous de **NE PAS** utiliser sudo lors de l'exécution des commandes npm.

**composer-cli** est le seul package essentiel. Les autres ne sont pas des composants principaux mais s'avéreront extrêmement utiles avec le temps. Nous en apprendrons plus sur ce que chacun de ces outils fait au fur et à mesure que nous les rencontrerons.

#### 3. **Installation d'un runtime local Hyperledger Fabric**

Passons en revue les commandes et voyons ce qu'elles signifient. Tout d'abord, nous créons et entrons dans un nouveau répertoire. Ensuite, nous téléchargeons et extrayons les outils nécessaires pour installer Hyperledger Fabric.

Nous spécifions ensuite la version de Fabric que nous voulons, au moment de l'écriture, nous avons besoin de la version 1.2, d'où **hlfv12**. Ensuite, nous téléchargeons le runtime fabric et le démarrons.

Enfin, nous générons une carte `PeerAdmin`. Les participants à un réseau Fabric peuvent avoir des cartes de réseau d'entreprise, analogues aux cartes de visite réelles. Comme nous l'avons mentionné précédemment, Fabric est une couche de base sur laquelle les blockchains privées peuvent construire. Le détenteur de la carte d'entreprise PeerAdmin a l'autorité de déployer, supprimer et gérer les réseaux d'entreprise sur ce runtime Fabric (c'est-à-dire VOUS !)

Si tout s'est bien passé, vous devriez voir une sortie comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*xUjx4TYAN4gnsyWa)

De plus, si vous tapez `ls`, vous verrez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*uF_L4sB42hB8TqnH)

En gros, ce que nous avons fait ici, c'est simplement télécharger et démarrer un réseau Fabric local. Nous pouvons l'arrêter en utilisant `./stopFabric.sh` si nous le souhaitons. À la fin de notre session de développement, nous devrions exécuter `./teardownFabric.sh`

**NOTE :** Ce runtime local est **destiné à être fréquemment démarré, arrêté et détruit** pour un usage de développement. Pour un runtime avec un état plus persistant, vous voudrez déployer le réseau en dehors de l'environnement de développement. Vous pouvez le faire en exécutant le réseau sur Kubernetes ou sur des plateformes gérées comme IBM Blockchain. Néanmoins, vous devriez d'abord suivre ce tutoriel pour avoir une idée.

### Création et déploiement de notre réseau d'entreprise

Vous vous souvenez des packages `yo` et `generator-hyperledger-composer` que nous avons installés plus tôt ?

`yo` nous fournit un écosystème de générateurs où les générateurs sont des plugins qui peuvent être exécutés avec la commande yo. Cela est utilisé pour configurer des applications d'exemple de base pour divers projets. `generator-hyperledger-composer` est le générateur Yo que nous allons utiliser car il contient des spécifications pour générer des réseaux d'entreprise de base entre autres choses.

#### **1. Génération d'un réseau d'entreprise**

Ouvrez le terminal dans un répertoire de votre choix et tapez `yo hyperledger-composer`

![Image](https://cdn-media-1.freecodecamp.org/images/0*l7HZjX-AphNyrorr)

Vous serez accueilli avec quelque chose de similaire à ce qui est montré ci-dessus. Sélectionnez `Business Network` et nommez-le `cards-trading-network` comme indiqué ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0*4RUkLM9_We2YorAa)

#### 2. **Modélisation de notre réseau d'entreprise**

La première et la plus importante étape pour créer un réseau d'entreprise est d'identifier les ressources présentes. Nous avons quatre types de ressources dans le langage de modélisation :

* Actifs
* Participants
* Transactions
* Événements

Pour notre `cards-trading-network`, nous allons définir un type d'actif `TradingCard`, un type de participant `Trader`, une transaction `TradeCard` et un événement `TradeNotification`.

Allez-y et ouvrez les fichiers générés dans un éditeur de code de votre choix. Ouvrez `org.example.biznet.cto` qui est le fichier de modélisation. Supprimez tout le code présent dans celui-ci car nous allons le réécrire (sauf la déclaration de namespace).

Cela contient la spécification pour notre actif `TradingCard`. Tous les actifs et participants doivent avoir un identifiant unique que nous spécifions dans le code, et dans notre cas, c'est `cardId`

De plus, notre actif a une propriété `GameType cardType` qui est basée sur l'énumérateur défini ci-dessous. Les énumérations sont utilisées pour spécifier un type qui peut avoir jusqu'à N valeurs possibles, mais rien d'autre. Dans notre exemple, aucun `TradingCard` ne peut avoir un `cardType` autre que `Baseball`, `Football` ou `Cricket`

Maintenant, pour spécifier notre type de ressource participant `Trader`, ajoutez le code suivant dans le fichier de modélisation

Cela est relativement plus simple et assez facile à comprendre. Nous avons un type de participant `Trader` et ils sont identifiés de manière unique par leurs `traderId`s.

Maintenant, nous devons ajouter une référence à nos `TradingCard`s pour avoir une référence pointant vers leur propriétaire afin que nous sachions à qui appartient la carte. Pour ce faire, ajoutez la ligne suivante à l'intérieur de votre actif `TradingCard` :

`--> Trader owner`

de sorte que le code ressemble à ceci :

C'est la première fois que nous utilisons `--&`gt; et vous devez vous demander ce que cela signifie. Il s'agit d'un pointeur de relation. `o` et `-->` sont les moyens par lesquels nous différencions les propriétés propres d'une ressource par rapport à une relation avec un autre type de ressource. Puisque le propriétaire `est un` Trader qui est un participant dans le réseau, nous voulons une référence à `ce` Trader directement, et c'est exactement ce que fait `-->`.

Enfin, allez-y et ajoutez ce code dans le fichier de modélisation qui spécifie quels paramètres seront nécessaires pour effectuer une transaction et émettre un événement.

#### 3. **Ajout de logique pour nos transactions**

Pour ajouter de la logique derrière la fonction `TradeCard`, nous avons besoin d'un fichier de logique Javascript. Créez un nouveau répertoire nommé `lib` dans le dossier de votre projet et créez un nouveau fichier nommé `logic.js` avec le code suivant :

**NOTE :** Le décorateur dans les commentaires au-dessus de la fonction est très important. Sans le `@param {org.example.biznet.TradingCard} trade`, la fonction ne sait pas à quelle `Transaction` le code fait référence depuis le langage de modélisation. Assurez-vous également que le nom du paramètre passé (c'est-à-dire `trade`) est celui que vous passez dans la définition de la fonction juste après.

Ce code vérifie essentiellement si la carte spécifiée a `forTrade == true` et met à jour le propriétaire de la carte dans ce cas. Ensuite, il déclenche l'événement `TradeNotification` pour cette carte.

#### 4. **Définition des permissions et des règles d'accès**

Ajoutez une nouvelle règle dans `permissions.acl` pour donner aux participants l'accès à leurs ressources. En production, vous voudrez être plus strict avec ces règles d'accès. Vous pouvez en lire plus à leur sujet [ici](https://hyperledger.github.io/composer/latest/reference/acl_language).

#### 5. **Génération d'une archive de réseau d'entreprise (BNA)**

Maintenant que tout le codage est terminé, il est temps de créer un fichier d'archive pour notre réseau d'entreprise afin que nous puissions le déployer sur notre runtime Fabric local. Pour ce faire, ouvrez le Terminal dans votre répertoire de projet et tapez ceci :

`composer archive create --sourceType dir --sourceName .`

Cette commande indique à Hyperledger Composer que nous voulons construire une BNA à partir d'un répertoire qui est notre dossier racine actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MiI9-KZeQWmuhf1V)

**NOTE :** Le nom et la version de la BNA proviennent du fichier `package.json`. Lorsque vous ajoutez plus de code, vous devez changer le numéro de version là pour déployer des archives uniques capables de mettre à niveau les réseaux d'entreprise existants.

#### 6. **Installation et déploiement du fichier BNA**

Nous pouvons installer et déployer le réseau sur notre runtime Fabric local en utilisant l'utilisateur `PeerAdmin`. Pour installer le réseau d'entreprise, tapez

`composer network install --archiveFile cards-trading-network@0.0.1.bna --card PeerAdmin@hlfv1`

![Image](https://cdn-media-1.freecodecamp.org/images/0*nOI-6kbYiD76HuzM)

Pour déployer le réseau d'entreprise, tapez

`composer network start --networkName cards-trading-network --networkVersion 0.0.1 --networkAdmin admin --networkAdminEnrollSecret adminpw --card PeerAdmin@hlfv1 --file cards-trading-admin.card`

![Image](https://cdn-media-1.freecodecamp.org/images/0*o5dJtBPYS0YsqaH-)

Le `networkName` et `networkVersion` doivent être les mêmes que ceux spécifiés dans votre `package.json`, sinon cela ne fonctionnera pas.

`--file` prend le nom du fichier à créer pour la carte d'entreprise de CE réseau. Cette carte doit ensuite être importée pour être utilisable en tapant

`composer card import --file cards-trading-admin.card`

![Image](https://cdn-media-1.freecodecamp.org/images/0*7ONVFnE8dQGxMFG6)

Incroyable. Nous pouvons maintenant confirmer que notre réseau est opérationnel en tapant

`composer network ping --card admin@cards-trading-network`

`--card` cette fois prend la carte admin du réseau que nous voulons ping.

Si tout s'est bien passé, vous devriez voir quelque chose de similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5EE453FFFQp4O0LO3PIg5Q.png)
_**Votre version de réseau sera 0.0.1 ou celle spécifiée dans votre package.json —** J'ai en fait oublié de prendre cette capture d'écran et je l'ai téléchargée après avoir terminé la rédaction du tutoriel et les modifications_

### Test de notre réseau d'entreprise

Maintenant que notre réseau est opérationnel sur Fabric, nous pouvons démarrer Composer Playground pour interagir avec lui. Pour ce faire, tapez `composer-playground` dans le Terminal et ouvrez `[http://localhost:8080/](http://localhost:8080/)` dans votre navigateur et vous devriez voir quelque chose de similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*QX21rhAmdnKKwEZJ)

Appuyez sur Connect Now pour `admin@cards-trading-network` et vous serez accueilli avec cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/0*3VAwop80uPvM8sYb)

La page **Define** est l'endroit où nous pouvons apporter des modifications à notre code, déployer ces modifications pour mettre à niveau notre réseau et exporter des archives de réseau d'entreprise.

Rendez-vous sur la page **Test** dans le menu supérieur, et vous verrez ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ba4OQmMecPDEsaQU)

Sélectionnez `Trader` dans Participants, cliquez sur **Create New Participant** près du coin supérieur droit, et créez un nouveau `Trader` similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*UjUZmOLt9tOfpDOB)

Allez-y et créez quelques autres `Trader`s. Voici à quoi ressemblent mes trois traders avec les noms Haardik, John et Tyrone.

![Image](https://cdn-media-1.freecodecamp.org/images/0*HPPva_cp92xBKtxy)

Maintenant, créons quelques Actifs. Cliquez sur `TradingCard` dans le menu de gauche et appuyez sur **Create New Asset**. Remarquez comment le champ `owner` est particulièrement intéressant ici, ressemblant à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Q_ZmrJorW6RcUxUe)

Ceci est une relation. C'est ce que signifie `--&`gt;. Nous spécifions le type de ressource exact suivi de leur identifiant unique et voilà, nous avons un pointeur de relation.

Allez-y et terminez la création d'une `TradingCard` similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*A7wT8ywp1aO63Eo4)

Remarquez comment le champ `owner` pointe vers `Trader#1` alias `Haardik` pour moi. Allez-y et créez quelques autres cartes, et activez quelques-unes pour avoir `forTrade` défini sur true.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wMA5-OcEJnbyEAPg)

Remarquez comment ma `Card#2` a `forTrade == true` ?

Maintenant, pour les choses amusantes, essayons d'échanger des cartes :D

Cliquez sur **Submit Transaction** à gauche et faites pointer `card` vers `TradingCard#2` et `newOwner` vers `Trader#3` comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*GAb88nhGlD2xPRm9)

Appuyez sur **Submit** et jetez un coup d'œil à vos `TradingCard`s, vous verrez que `Card#2` a maintenant le propriétaire `Trader#3` :D

### Génération d'un serveur REST API

Faire des transactions avec Playground est bien, mais pas optimal. Nous devons créer un logiciel côté client pour offrir aux utilisateurs une expérience transparente, ils n'ont même pas besoin de connaître la technologie blockchain sous-jacente. Pour ce faire, nous avons besoin d'une meilleure façon d'interagir avec notre réseau d'entreprise. Heureusement, nous avons le module `composer-rest-server` pour nous aider.

Tapez `composer-rest-server` dans votre terminal, spécifiez `admin@cards-trading-network`, sélectionnez **never use namespaces**, et continuez avec les options par défaut pour le reste comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/0*VukFOTRBvtOMeGRG)

Ouvrez `[http://localhost:3000/explorer/](http://localhost:3000/explorer/)` et vous serez accueilli avec une version documentée d'une API REST générée automatiquement :D

### Génération d'une application Angular qui utilise l'API REST

Vous vous souvenez du générateur `yo hyperledger-composer` ? Il peut faire plus que générer un réseau d'entreprise. Il peut également créer une application Angular 4 qui s'exécute contre l'API REST que nous avons créée ci-dessus.

Pour créer l'application web Angular, tapez `yo hyperledger-composer` dans votre Terminal, sélectionnez Angular, choisissez de vous connecter à un réseau d'entreprise existant avec la carte `admin@cards-trading-network`, et connectez-vous également à une API REST existante. (**Modification :** Les nouvelles versions du logiciel peuvent demander le fichier de carte au lieu du seul nom de la carte)

![Image](https://cdn-media-1.freecodecamp.org/images/0*WkNRiy0grt6DD_M5)

Cela va exécuter `npm install`, donnez-lui une minute, et une fois que tout est terminé, vous pourrez charger `[http://localhost:4200/](http://localhost:4200/)` et être accueilli avec une page similaire à ceci :  
**Modification :** Les nouvelles versions du logiciel peuvent vous obliger à exécuter `npm install` vous-même, puis à exécuter `npm start`

![Image](https://cdn-media-1.freecodecamp.org/images/0*1GrawK-jGkN9cvqO)

Vous pouvez maintenant jouer avec votre réseau à partir de cette application directement, qui communique avec le réseau via le serveur REST s'exécutant sur le port 3000.

Félicitations ! Vous venez de configurer votre premier réseau d'entreprise blockchain en utilisant Hyperledger Fabric et Hyperledger Composer :D

Vous pouvez ajouter plus de fonctionnalités au réseau de trading de cartes, en fixant des prix sur les cartes et en donnant un solde à tous les `Trader`. Vous pouvez également avoir plus de transactions qui permettent aux `Trader`s de basculer la valeur de `forTrade`. Vous pouvez intégrer cela avec des applications non blockchain et permettre aux utilisateurs d'acheter de nouvelles cartes qui sont ajoutées à leur compte, qu'ils peuvent ensuite échanger davantage sur le réseau.

Les possibilités sont infinies, que ferez-vous avec elles ? Faites-le moi savoir dans les commentaires :D

### BUG CONNU : Votre application web Angular ne gère-t-elle pas correctement les transactions ?

Au moment de l'écriture, le générateur angular a un problème où le bouton purple Invoke sur la page des Transactions ne fait rien. Pour corriger cela, nous devons apporter quelques modifications à l'application angular générée.

![Image](https://cdn-media-1.freecodecamp.org/images/0*owNwB2hjvpxTSvxE)

#### **1. Obtenir une modale qui s'ouvre lorsque vous appuyez sur le bouton**

Le premier changement que nous devons apporter est de faire en sorte que le bouton ouvre la fenêtre modale. Le code contient déjà la fenêtre modale requise, il manque simplement les attributs `(click)` et `data-target` au bouton.

Pour résoudre cela, ouvrez `/cards-trading-angular-app/src/app/TradeCard/TradeCard.component.html`

Le nom du fichier peut varier en fonction de votre nom de `transaction`. Si vous avez plusieurs `transaction`s dans votre réseau d'entreprise, vous devrez apporter ce changement dans tous les fichiers HTML des types de ressources de transaction.

Faites défiler jusqu'à la toute fin et vous verrez une balise `<butt`on>. Allez-y et ajoutez ces deux attributs à cette balise :

`(click)="resetForm();" data-target="#addTransactionModal"`

de sorte que la ligne ressemble à ceci :

`<button type="button" class="btn btn-primary invokeTransactionBtn" data-toggle="modal" (click)="resetForm();" data-target="#addTransactionModal">Invoke</button>`

L'attribut `(click)` appelle `resetForm();` qui définit tous les champs d'entrée à vide, et `data-target` spécifie la fenêtre modale à ouvrir lors du clic.

Enregistrez le fichier, ouvrez votre navigateur et essayez d'appuyer sur le bouton invoke. Il devrait ouvrir cette modale :

![Image](https://cdn-media-1.freecodecamp.org/images/0*9Q6opS0G8rrwk4YA)

#### 2. **Suppression des champs inutiles**

Faire en sorte que la modale s'ouvre n'est pas suffisant. Nous pouvons voir qu'elle nous demande `transactionId` et `timestamp` alors que nous n'avons pas ajouté ces champs dans notre fichier de modélisation. Notre réseau stocke ces valeurs qui sont intrinsèques à toutes les transactions. Il devrait donc être capable de déterminer ces valeurs par lui-même. Et il s'avère qu'il le fait effectivement. Ce sont des champs superflus et nous pouvons simplement les commenter, l'API REST s'occupera du reste pour nous.

Dans le même fichier, faites défiler vers le haut pour trouver les champs d'entrée et commentez les divs responsables de ces champs d'entrée à l'intérieur de `addTransactionModal`

![Image](https://cdn-media-1.freecodecamp.org/images/1*EogUHWeTnXKV-EkmjXP7Pw.png)

Enregistrez votre fichier, ouvrez votre navigateur et appuyez sur Invoke. Vous devriez voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*W2O1PD-7qW0a-f2v)

Vous pouvez maintenant créer des transactions ici en passant des données dans ces champs. Puisque `card` et `newOwner` sont des relations avec d'autres ressources, nous pouvons faire une transaction comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*lRrhv1lZIgFSggbY)

Appuyez sur **Confirm**, retournez à la page **Assets**, et vous verrez que `TradingCard#2` appartient maintenant à `Trader#1` :

![Image](https://cdn-media-1.freecodecamp.org/images/0*teBdk1zFVR2hj2Tx)

Félicitations ! Vous avez réussi à construire et à déployer un réseau d'entreprise blockchain sur Hyperledger Fabric. Vous avez également généré un serveur REST API pour ce réseau et appris comment créer des applications web qui interagissent avec cette API.

Si vous avez des questions ou des doutes, laissez-les dans les commentaires et je vous répondrai.  
Email : hhaardik@uwaterloo.ca  
LinkedIn : [https://www.linkedin.com/in/haardikkk](https://www.linkedin.com/in/haardikkk)