---
title: Comment lancer votre serveur MVP en une heure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T08:29:44.000Z'
originalURL: https://freecodecamp.org/news/building-a-full-graph-stack-f95590ade5af
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IBwh1zdiKEN7OdkOoUJC8w.png
tags:
- name: database
  slug: database
- name: GraphQL
  slug: graphql
- name: mvp
  slug: mvp
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment lancer votre serveur MVP en une heure
seo_desc: 'By Yisroel Yakovson

  Building A Full Stack Server

  This article guides you through creating a live, development quality API and back
  end. It should take you about an hour. And, by the way, it will be free!

  This is the second of a series of 3 articles a...'
---

Par Yisroel Yakovson

### Construire un serveur Full Stack

Cet article vous guide à travers la création d'une API et d'un back-end de qualité développement, en direct. Cela devrait vous prendre environ une heure. Et, au fait, ce sera gratuit !

Il s'agit du deuxième d'une série de 3 articles sur les stacks graphiques complètes. Consultez [Comment construire un serveur de pointe maintenant](https://medium.freecodecamp.org/meet-the-full-graph-stack-d32150308a87) pour une introduction.

Je suppose que vous savez coder, mais pas que vous êtes avancé. Il s'agit d'un projet full stack. Il aborde de nombreux nouveaux outils, vous n'avez donc pas besoin de vous sentir intimidé si vous ne comprenez pas tout. Vous aurez quelques courbes d'apprentissage devant vous, mais pas trop raides.

L'idée, comme expliqué dans le [premier article](https://medium.freecodecamp.org/meet-the-full-graph-stack-d32150308a87), est de se concentrer sur la spécification du graphe des types de données de votre application. Ensuite, utiliser de nouveaux outils qui génèrent une application à partir de celui-ci.

Comme je l'ai écrit dans le premier article, j'ai choisi le projet [GRANDstack](http://grandstack.io/). Je ne prétends pas que c'est la seule approche viable, mais je vous recommande au moins de le vérifier. Mon équipe a décidé par nous-mêmes que nous voulions utiliser React, GraphQL, Apollo et une base de données graphique. Le GRANDstack se compose exactement de ces éléments, donc la découverte m'a excité.

Mais la vraie excitation commence avec le package [neo4j-graphql-js](https://github.com/neo4j-graphql/neo4j-graphql-js). Il génère (style Prisma) un ensemble de mutations et de résolveurs à partir de TypeDefs. Si vous ne savez pas ce que cela signifie, continuez à lire.

Sur la page [GRANDstack Kickstarter](http://grandstack.io/docs/getting-started-grand-stack-starter.html), une vidéo montre comment créer une stack complète de A à Z. C'est là que j'ai commencé.

Un problème avec la rédaction de ces articles est que les packages présentés sont en développement. De nombreuses choses que vous devez encore faire aujourd'hui pourraient être automatiques dans quelques semaines. Je veux résumer les étapes et expliquer comment faire certaines des choses dont vous avez encore besoin. Mais l'équipe de Neo4j travaille dessus. Si vous voyez que ces informations sont obsolètes à un moment donné, veuillez poster une mise à jour ci-dessous.

### Approches alternatives

Avant de commencer, laissez-moi répéter que je n'appelle pas GRANDstack la seule ou même la meilleure approche pour une Full Graph Stack.

De nombreuses alternatives utilisent Prisma pour convertir un schéma GraphQL en une base de données sous-jacente. Assurez-vous de consulter [GraphCool](https://www.graph.cool/). À l'heure où nous écrivons ces lignes, ces systèmes sont plus développés et laissent moins de travail au développeur. Un bon exemple est l'authentification.

L'approche Prisma a également moins de verrouillage sur une base de données particulière. En pratique, changer la base de données ne serait pas si difficile avec GRANDstack. Mais les requêtes de chiffrement et les directives sont uniques à Neo4j.

Cela dit, le projet GRANDstack est explicitement axé sur l'idée d'une Full Graph Stack. Je les recommande parce qu'ils sont réactifs et dévoués à la vision. C'est aussi très simple.

### Installation

#### Créer un projet

1. Téléchargez le starter. Cliquez sur `DOWNLOAD STARTER` depuis [GRANDstack](http://grandstack.io/), ou téléchargez-le depuis leur page [GitHub](https://github.com/grand-stack/grand-stack-starter). J'ai utilisé la page GitHub pour être sûr d'avoir la dernière version (ce devrait être le cas de toute façon).
2. Décompressez dans un dossier et nommez-le pour votre projet d'application
3. Il est judicieux de déplacer le nouveau dossier d'application dans un dossier général **projet**.

#### Configurer Git

Je vous recommande de ne rien faire tant que vous n'utilisez pas Git pour gérer le contrôle de version.

1. [Installez Git](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/) si vous ne l'avez pas.
2. Dans un éditeur de texte, modifiez `.gitignore` dans le répertoire racine du projet pour inclure sous `#dependencies` une ligne pour `api/node_modules` et une ligne pour `ui/node_modules`. À l'heure où nous écrivons ces lignes, `.gitignore` ne contenait que `node_modules`.
3. Déplacez-vous dans le répertoire racine du projet dans un terminal, et créez un nouveau projet git :

```
git init git add .   # ajoute les fichiers pertinentsgit status  # optionnel pour voir les fichiers si vous êtes intérességit commit -m "Fichiers d'application initiaux" #ou le nom que vous souhaitez
```

Vous pouvez effectuer `git add .` et `git commit -m "une description"` aussi souvent que vous le souhaitez. Voir la documentation sans fin sur Git en ligne. Vous pouvez apprendre sur les branches, les commits, la réversion et tout sur le contrôle de version.

### Créer le back-end d'exemple

Notez que votre code de projet a deux répertoires : `api` et `ui`. Ces articles se concentrent uniquement sur le répertoire `api`, pour créer un serveur API et un back-end. Pour plus d'informations sur `ui`, consultez la vidéo [GRANDstack Kickstarter](http://grandstack.io/docs/getting-started-grand-stack-starter.html). Vous pouvez également consulter les tutoriels sur GRANDstack.

#### Construire le back-end

Vous devez construire le code. Vous pouvez utiliser npm pour cela. Dans le terminal, déplacez-vous dans `api`, et effectuez ces étapes :

```
npm install # récupère tous les modules node nécessaires pour l'apinpm start # commence l'application
```

Cela devrait initier l'application. Vous devriez voir quelque chose comme ceci dans votre terminal :

```
$ npm start
```

```
> grand-stack-starter-api@0.0.1 start /home/israel/projects/events2/api> nodemon --exec babel-node src/index.js
```

```
[nodemon] 1.18.3[nodemon] pour redémarrer à tout moment, entrez `rs`[nodemon] surveillance : *.*[nodemon] démarrage de `babel-node src/index.js`GraphQL API prêt à http://0.0.0.0:4000/
```

Ouvrez ce lien, et vous devriez voir une page GraphQL Playground.

![Image](https://cdn-media-1.freecodecamp.org/images/p287pjNAiabrD4eyZBNr-GdewMT88YQSWyTq)

Vous pouvez cliquer sur l'onglet vert SCHEMA à droite, et vous verrez un schéma pour une base de données d'exemple. La seule chose qui vous manque est la base de données elle-même.

### Configurer une base de données d'exemple

Vous devrez vous inscrire sur [Neo4j](https://neo4j.com/lp/try-neo4j-sandbox/) pour utiliser leur bac à sable dans les étapes données ci-dessous. Je recommande de rejoindre leur [chaîne Slack](https://neo4j-users.slack.com/) dès le début. En particulier, si vous suivez les étapes ci-dessous, je rejoindrais le canal **#grand-stack** afin que vous puissiez poser des questions. Le projet évolue rapidement, il est donc important de rester connecté. Ils sont assez réceptifs aux idées et réactifs aux problèmes. Au cours des dernières semaines, ils ont mis en œuvre plusieurs idées que j'ai proposées avec d'autres.

#### Lancer une base de données vide

1. Connectez-vous à [Neo4j Sandbox](https://neo4j.com/sandbox-v2/). (Comme indiqué au début, vous devez créer un compte si vous n'en avez pas.)
2. Trouvez "Blank Database" et cliquez dessus. Elle devrait se générer et apparaître après une minute sous **Vos bacs à sable actuels**.
3. Cliquez sur l'onglet **Détails**, et vous verrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/g2WzC42HBX1fuPW6kr-3i9Z9HfE83F3yIkpf)

Vous avez maintenant généré une base de données en direct. Vous pouvez la visiter dans le navigateur via le lien en haut.

#### Connecter votre projet à la base de données

Ouvrez le fichier `api/.env`, qui contient certaines variables globales utilisées dans l'API :

```
NEO4J_URI=bolt://localhost:7687NEO4J_USER=neo4jNEO4J_PASSWORD=letmeinGRAPHQL_LISTEN_PORT=4000GRAPHQL_URI=http://localhost:4000
```

Vous devez définir certaines de ces variables à partir de l'onglet Détails de votre bac à sable

1. Copiez l'adresse IP (par exemple, dans l'exemple montré ci-dessus, il s'agit de `174.129.54.148`), puis le port bolt, par exemple `33199`. Utilisez-les ensemble pour créer une nouvelle valeur pour `NEO4J_URI` dans le fichier `api/.env`, en remplaçant `bolt://localhost:7687`. Notez qu'un deux-points les sépare. Par exemple, la première ligne dans ce cas serait `NEO4J_URI=bolt://174.129.54.148:33199`.
2. Copiez également depuis Détails le mot de passe de la base de données sandbox (par exemple, dans ce cas `adhesives-casualties-loads`) et remplacez le mot de passe par défaut `letmein`.
3. Bien sûr, assurez-vous d'avoir enregistré vos modifications. Puis retournez à votre terminal, appuyez sur `ctrl-c`, entrez à nouveau `npm start`, et retournez à [http://0.0.0.0:4000/](http://0.0.0.0:4000/) et rechargez.
4. Maintenant, entrez la mutation suivante dans le panneau de gauche :

```
# Essayez d'écrire votre requête ici
mutation {  CreateUser (id: "borris", name: "borris the spider") {    id  }}
```

Cliquez sur le bouton flèche au milieu pour exécuter, et vous devriez voir les résultats de la mutation dans le bouton de droite :

![Image](https://cdn-media-1.freecodecamp.org/images/19KFekShbwlleukGojgH-4FQ59ZHswV3jrtg)

Si c'est le cas, félicitations ! Vous avez déjà un serveur API fonctionnel en cours d'exécution localement.

N'oubliez pas de valider vos modifications dans Git. Dans le répertoire racine de votre application (pas dans API), entrez :

```
git add .git commit -m "Working Sandbox Db"
```

### Inspecter les données directement

Maintenant, cliquez sur le lien vers `Neo4j Browser` en haut des Détails dans votre Neo4j Sandbox. (Dans le cas montré ci-dessus, il s'agit de `[https://10-0-1-68-33200.neo4jsandbox.com/](https://10-0-1-68-33200.neo4jsandbox.com/.))`[.)](https://10-0-1-68-33200.neo4jsandbox.com/.))

![Image](https://cdn-media-1.freecodecamp.org/images/2IMvSnlT0Bwd5Q7dOwHYMk06rmkTJTBLcGst)

Vous pouvez lire comment l'utiliser sur Neo4j. Mais pour nos besoins, entrez la requête suivante à l'invite : `MATCH (n) RETURN n`. Cette requête retourne tous les nœuds de la base de données. Cliquez sur le bouton flèche à droite pour exécuter, et vous devriez voir le nouveau nœud que vous avez créé :

![Image](https://cdn-media-1.freecodecamp.org/images/iY4PdL88TEOKKOkNlJ3LDZXwkxk5io-ibdal)

Vous pouvez revenir à un terminal dans votre répertoire `api` et entrer `npm seedDb` si vous le souhaitez. Après une minute ou deux, vous verrez les données de départ qui accompagnent le package de démarrage pour leur base de données d'exemple. Vous pouvez ensuite jouer avec Playground en faisant des requêtes comme celle-ci :

```
{  users(name: "Will") {    id    name  }}
```

Ou, vous pouvez simplement passer à l'étape suivante.

### Ajouter votre propre schéma GraphQL

Cliquez sur le bouton vert SCHEMA dans l'interface Playground. Vous verrez un schéma qui accompagnait la base de données d'exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/oYUqCcTIe7TNBPn7lXpnUMPm8BhIqR6XfnLw)

Maintenant, il est temps de remplacer cela par votre propre schéma.

1. Ouvrez le schéma d'exemple actuel `api/src/graphql-schema.js`, et voyez la source de ces données. Elle se trouve dans la déclaration `typeDefs`.
2. Apprenez au minimum ce que vous devez savoir sur les [schémas de types GraphQL](https://graphql.org/learn/schema/). Vous devez être capable de mettre en œuvre vos propres types nécessaires et certaines requêtes. C'est simple.
3. Commencez par un ou deux types et expérimentez, en le construisant progressivement. Pour créer une requête, vous devrez modifier à la fois `typeDefs` et `resolvers` (sous `typeDefs` dans le même fichier). Heureusement, vos résolveurs seront simples. Appelez simplement `neo4jgraphql` depuis le package [neo4j-graphql-js](https://github.com/neo4j-graphql/neo4j-graphql-js), comme dans la base de données d'exemple.
4. Enregistrez les modifications du fichier et confirmez que npm est en cours de mise à jour. Ensuite, actualisez l'onglet Playground et confirmez que le nouveau schéma s'affiche.

L'[article d'introduction](https://medium.freecodecamp.org/meet-the-full-graph-stack-d32150308a87) sur les stacks graphiques complètes mentionnait une application d'exemple pour les événements. Voici son graphe de types de données d'application d'exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/-DvKBsPHFILwdawQmLAXeBgrGNfdYHvk1K-O)

C'est beaucoup à ajouter d'un coup, mais ce n'est pas difficile à commencer. Nous travaillons de haut en bas, et GraphQL est extrêmement indulgent.

#### Comprendre neo4j-graphql-js

Il serait utile de comprendre un peu comment le serveur utilise `neo4j-graphql-js`.

L'appel à `augmentSchema` dans `index.js` est ce qui crée toutes les mutations. Cela inclut les fonctions CRUD (Create, Update et Delete) pour chacun des types créés. Ainsi que les fonctions Add et Remove pour créer des relations.

Les relations entre les types génèrent des fonctions de relation. Lorsqu'un type X retourne le type Y comme champ, cela indique une relation. Les fonctions Add et Remove sont générées lorsque la relation précise est définie en utilisant :

1. une directive `@cypher` ou
2. une directive `@relation` avec une direction "OUT".

L'autre fonction importante est `neo4jgraphql`, qui implémente un résolveur. La [documentation du package](https://grandstack.io/docs/neo4j-graphql-js.html) explique les détails.

La documentation a été mise à jour la semaine dernière sur la [page de documentation GRANDstack](https://grandstack.io/docs/neo4j-graphql-js.html). (Cette rédaction date du 19 août 2018). La documentation est encore un peu minimale. Par exemple, la fonction critique `augmentSchema` n'est pas discutée dans la documentation. Ils discutent des mutations et montrent un exemple en utilisant celle-ci. Mais la documentation est utile. Les exemples contenus dans le package de démarrage et dans les exemples apportés là-bas le sont également.

Vous pourriez également consulter la documentation pour `[neo4j-graphql](https://github.com/neo4j-graphql/neo4j-graphql)`[.](https://github.com/neo4j-graphql/neo4j-graphql) mais certaines choses là-bas n'ont peut-être pas encore été intégrées dans la version `ps`.

#### Modifications initiales

Vous pouvez supprimer tous les types de l'exemple, mais notez que vous ne devez pas supprimer entièrement le type Query. Vous en aurez besoin pour vos requêtes, comme vous pouvez le voir dans la documentation GraphQL.

Voici un exemple du début le plus simple possible pour le schéma de l'application d'événements :

```
export const typeDefs = `type Event {  id: ID!  name: String}type Query {    events(id: ID, name: String): [Event]}`;export const resolvers = {  Query: {    events: neo4jgraphql,  }};
```

Après avoir enregistré, vérifiez un message rassurant dans le terminal où `npm start` est en cours d'exécution. Quelque chose comme ceci :

```
[nodemon] redémarrage en raison des changements[nodemon] démarrage de `babel-node src/index.js`GraphQL API prêt à http://0.0.0.0:4000/
```

Actualisez Playground dans le navigateur et cliquez sur les boutons SCHEMA. Vous devriez voir le nouveau schéma :

![Image](https://cdn-media-1.freecodecamp.org/images/I5Htv0-2MxJQ2B5i8HJfJKUQTmq061wCM01J)

Vous pouvez ensuite commencer à ajouter plus de types.

#### Ajouter vos propres données

1. À l'invite de votre Sandbox, entrez `MATCH (n) DETACH DELETE n`. Cela supprimera toutes les données que vous avez ajoutées pour le schéma d'exemple qui accompagnait le projet.
2. Utilisez les mutations générées dans votre nouveau schéma pour créer des données. Par exemple :

```
mutation {  CreateEvent(id: "my event", name: "The Big Event") {    id    name  }}
```

### Passer en direct

La seule chose restante est de déplacer votre serveur vers un site en direct afin que votre front-end puisse l'appeler. (Oh, et vous devrez créer le front-end — allez dans le répertoire `ui` de votre dossier d'application pour vous en occuper). La vidéo sur la page [GRANDstack Kickstart](http://grandstack.io/docs/getting-started-grand-stack-starter.html) recommande d'utiliser [Now](https://zeit.co/now).

Allez sur [Now Desktop](https://zeit.co/download) et cliquez sur télécharger. **Mais** : l'application de bureau ne fonctionne actuellement pas pour Linux. Je suis sur Ubuntu, donc j'ai simplement utilisé leur [interface de ligne de commande](https://zeit.co/download#now-cli). C'est ce que j'utilise dans ces instructions.

1. Une fois que vous avez installé sur votre machine, connectez-vous. Vous devriez pouvoir retourner sur le [site Now](https://zeit.co/now) et voir votre nom ou votre photo en haut à droite.
2. Allez dans le répertoire `api` et tapez `now`. Vous serez invité plusieurs fois à entrer des choses. Si tout se passe bien, vous obtiendrez une longue série de sorties dans le terminal se terminant par un message de succès :

```
$ now> Lisez plus sur la façon de mettre à jour ici : https://zeit.co/update-cli> Déploiement de ~/projects/events2/api sous xxxxxxxxxx@gmail.com> Le code et les journaux de votre déploiement seront accessibles publiquement car vous êtes abonné au plan OSS.> NOTE : Vous pouvez utiliser `now --public` ou mettre à niveau votre plan (https://zeit.co/account/plan) pour ignorer cette invite> Téléchargement [=============-------] 66% 0.1s (192.48KB) [4 fichiers]> Utilisation de Node.js 8.11.3 (par défaut)> https://grand-stack-starter-api-qibrvosvuh.now.sh [dans le presse-papiers] (bru1) [7s]> Synchronisé 4 fichiers (192.48KB) [7s]> Construction>  npm install>  Utilisation de "package-lock.json">  Installation de 13 dépendances principales> Construction de "nodemon@1.18.1" à distance> Construction de "nodemon@1.18.1" à distance> Construction de "nodemon@1.18.1" à distance> Construction de "nodemon@1.18.1" à distance> Erreur : Erreur d'analyse de `package.json` pour nodemon-1.18.1.tar>     à extract (/snapshot/ace/lib/extract.js:36:11)>     à process._tickCallback (internal/process/next_tick.js:188:7)>     à <anonymous>>  npm install> > protobufjs@6.8.6 postinstall /home/nowuser/src/node_modules/protobufjs> node scripts/postinstall> > > nodemon@1.18.1 postinstall /home/nowuser/src/node_modules/nodemon> node bin/postinstall || exit 0> > Love nodemon ? Vous pouvez maintenant soutenir le projet via l'open collective :>  > https://opencollective.com/nodemon/donate> > npm WARN grand-stack-starter-api@0.0.1 No repository field.> npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.4 (node_modules/fsevents):> npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.4: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})> > added 564 packages in 9.426s>  Instantané de déploiement>  Sauvegarde de l'image de déploiement (9.0M)> Construction terminée> Vérification de l'instanciation dans bru1> [0] > [0] grand-stack-starter-api@0.0.1 start /home/nowuser/src> [0] nodemon --exec babel-node src/index.js> [0] > [0] [nodemon] 1.18.1> [0] [nodemon] pour redémarrer à tout moment, entrez `rs`> [0] [nodemon] surveillance : *.*> [0] [nodemon] démarrage de `babel-node src/index.js`>  Mis à l'échelle 1 instance dans bru1 [13s]Ouvrez cette URL, et vous devriez voir votre playground. Essayez-le pour être sûr qu'il fonctionne :
```

La chose la plus importante est une ligne indiquant votre endpoint en direct :

```
https://grand-stack-starter-api-qibrvosvuh.now.sh [dans le presse-papiers]
```

Ouvrez cette URL, et vous devriez voir votre playground. Essayez-le pour être sûr qu'il fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/D2UG0F8A2zauoEePjiO-9qkNzyJ48cp88KKL)

### Ce que vous avez accompli

C'est tout — un serveur de développement en direct, avec très peu de temps et sans argent ! Vous avez une stack complète. Mais contrairement à une stack LAMP, cette stack inclut l'API elle-même. Notez que tout ce que vous avez eu à modifier était `typeDefs` et `resolvers`.

Comprenez que cela n'est pas encore de qualité production :

* Votre temps est très limité pour utiliser cela sans configurer une base de données permanente. Vous pouvez maintenant jouer avec cela sur votre front-end jusqu'à ce que votre Neo4j Sandbox expire. Cela sera dans 3 jours, mais vous pouvez demander une semaine supplémentaire. Et bien sûr, vous pouvez toujours créer un nouveau Sandbox. Si vous le souhaitez, vous pouvez également stocker un ensemble de mutations dans `api/src/seed/seed-mutations.js`. Vous pouvez l'exécuter avec la commande `npm seedDb` chaque fois que vous changez pour un nouveau sandbox.
* Chaque fois que vous voulez changer votre version sur now, l'URL changera. Vous pouvez [configurer un alias](https://zeit.co/docs/features/aliases) pour permettre à votre code de gérer cela, mais ce n'est pas idéal à long terme.

Mais pour un MVP, et pour le développement initial, c'est suffisant et gratuit. Si vous avez un domaine, vous pouvez utiliser n'importe quel service d'hébergement pour configurer un [enregistrement CNAME](https://www.linode.com/docs/networking/dns/dns-records-an-introduction/#cname) pour exécuter votre page Now à partir de celui-ci.

Consultez [Rendre votre Full Graph Stack de qualité production](https://medium.com/@yisroelyakovson/making-your-single-graph-stack-production-quality-ec231a938551) pour apprendre comment déployer pour la publication.