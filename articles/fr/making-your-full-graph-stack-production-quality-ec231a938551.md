---
title: Comment passer d'un MVP à un serveur de production en un jour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T08:29:58.000Z'
originalURL: https://freecodecamp.org/news/making-your-full-graph-stack-production-quality-ec231a938551
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IBwh1zdiKEN7OdkOoUJC8w.png
tags:
- name: GraphQL
  slug: graphql
- name: mvp
  slug: mvp
- name: General Programming
  slug: programming
- name: servers
  slug: servers
- name: 'tech '
  slug: tech
seo_title: Comment passer d'un MVP à un serveur de production en un jour
seo_desc: 'By Yisroel Yakovson

  This article follows two others about creating Full Graph Stacks. Check out How
  To Build A Cutting Edge Server Now for a conceptual introduction to the approach.
  Launch Your MVP Server In An Hour guides you through building a stac...'
---

Par Yisroel Yakovson

Cet article fait suite à deux autres sur la création de Full Graph Stacks. Consultez [Comment construire un serveur de pointe maintenant](https://medium.freecodecamp.org/meet-the-full-graph-stack-d32150308a87) pour une introduction conceptuelle à l'approche. [Lancez votre serveur MVP en une heure](https://medium.freecodecamp.org/building-a-full-graph-stack-f95590ade5af) vous guide à travers la construction d'une pile de qualité de développement. Cet article explique comment convertir cette pile en une application robuste et permanente.

![Image](https://cdn-media-1.freecodecamp.org/images/xMv8-fJ-bBLSQJDiVRVDBAkJPEB1UFdoMrLz)

### Qu'est-ce qui ne va pas avec la pile de développement ?

Les étapes du deuxième article reflétaient la [vidéo GRANDstack](https://github.com/grand-stack/grand-stack-starter) :

* La base de données est un [Neo4j Sandbox](https://neo4j.com/sandbox-v2/)
* Le serveur APIC s'exécute sur [Now](https://zeit.co/now).

Cela suffit pour un MVP ou pour le prototypage initial, mais vous devrez passer à autre chose rapidement. La plus grande limitation initiale est la base de données. Le bac à sable vivra au maximum dix jours.

Même après avoir lancé une base de données permanente, Now serait un foyer permanent difficile. En théorie, ce serait possible si vous ne modifiiez pas fréquemment votre serveur. Vous pourriez configurer votre API permanente avec un hôte séparé et l'aliaser à votre point de terminaison Now. Le problème est que le point de terminaison Now change chaque fois que vous téléchargez une révision. Cela signifie que vous devez continuer à mettre à jour votre alias.

La sécurité pose également un défi. Il est courant de créer une liste blanche d'IP autorisées à accéder à votre base de données et de limiter la liste à votre serveur API. Donc, si l'IP de ce serveur change fréquemment, vous devez mettre à jour la liste à chaque révision. Je ne vois pas de moyen viable de faire cela avec Now à l'heure actuelle. (Veuillez me contacter si vous en avez un !)

La question est donc de savoir quelle est la meilleure approche pour résoudre ces limitations.

### À la pointe de la technologie

La vérité est que cet article a été en attente pendant quelques semaines. Le problème était que [neo4j-graphql-js](https://github.com/neo4j-graphql/neo4j-graphql-js) n'était pas tout à fait prêt à supporter la production. Mais au cours des dernières semaines, tout cela a changé. L'équipe a résolu quelques problèmes fondamentaux :

* Le [Middleware](https://expressjs.com/en/guide/using-middleware.html) est devenu supportable il y a deux semaines. L'équipe a ajouté aux réducteurs générés le support pour le lancement d'erreurs de middleware. Cela permet à votre serveur d'exécuter des fonctionnalités générales d'authentification et d'autorisation en tant que middleware.
* La modification des [mutations](https://graphql.org/learn/queries/#mutations) est devenue possible il y a une semaine. Jusqu'alors, vous étiez coincé avec les mutations générées. Maintenant, vous pouvez ajouter la logique métier nécessaire ou des effets secondaires.
* Les clés autogénérées deviennent disponibles. L'équipe a signalé hier une nouvelle directive @autogenerate. Placer la directive après une clé entraînera la génération automatique d'un UUID. Auparavant, le front-end devait transmettre des valeurs pour les clés, ce qui est très inhabituel pour un serveur de production.

Cet article, écrit le 19 août 2018, intervient au milieu de nombreuses autres corrections attendues. Parmi les points d'intérêt particuliers, l'équipe prévoit de publier certaines directives pour simplifier l'authentification. De plus, j'espère que nous verrons bientôt des [mutations imbriquées](https://github.com/neo4j-graphql/neo4j-graphql-js/issues/89). Une grande partie de ce que j'écris ici deviendra bientôt obsolète. Mais j'ai décidé qu'il valait la peine de décrire ce package maintenant, car il est déjà utile. Veuillez publier des mises à jour ou des corrections ci-dessous en tant que commentaires.

### Options

Lorsque vous quittez le monde des bacs à sable, vous avez des choix. Je pense que la règle générale est que la plupart des options sont acceptables aujourd'hui. L'important est d'avancer.

Mais les trois étapes de base que je discute ci-dessous sont probablement des besoins universels. Elles peuvent être tout ce dont vous avez besoin pour votre back-end.

Deux observations introductives :

* Vous n'avez pas besoin de tout rendre parfait dès le premier jour. Il fut un temps où des décisions comme la taille de votre machine ou de votre hôte avaient une signification à long terme. Aujourd'hui, toute équipe sensée travaille dans le cloud. La plupart des décisions sont réversibles. L'authentification peut être une exception, mais même cela peut changer. Mettez quelque chose en ligne et commencez à pivoter !
* Si vous avez suivi les étapes de [Lancez votre serveur MVP en une heure](https://medium.freecodecamp.org/building-a-full-graph-stack-f95590ade5af), vous avez un back-end incroyablement petit. Vous aurez besoin de trois composants : votre petite application serveur, votre base de données et un service d'authentification. Vous n'avez même pas besoin de les stocker avec le même hôte.

### Contenu

1. [Configurer l'authentification](#heading-installation)
2. [Lancer votre base de données](#heading-lancement-base-de-donnees)
3. [Créer votre serveur](#heading-creation-serveur)

### Configurer l'authentification

Les besoins d'authentification de chaque projet sont différents, mais quelques bases ont émergé. Vous avez besoin de deux choses :

1. Un service d'authentification externe. Deux choix courants sont Cognito et Auth0.
2. La plupart des serveurs ont également besoin d'autorisation, ou de contrôle d'accès. Vous devez décider si un utilisateur particulier est autorisé à faire quelque chose.

#### Configuration de la capacité Middleware

La manière préférée de gérer l'authentification est [via middleware](https://graphql.org/graphql-js/authentication-and-express-middleware/) ou des directives. À l'heure actuelle, l'authentification n'est pas incluse dans le démarreur GRANDstack.

Le serveur utilisé dans `api/src/index.jx` dans le package de démarrage est actuellement `ApolloServer`. Mais vous pouvez le remplacer par `graphalExpress` de `apollo-server-express`.

Vous devrez modifier 2 fichiers :

* `api/src/index.js`
* `api/package.json`

Vous devriez également ajouter un fichier `auth.js`.

Voici une version de `index.js` qui fonctionne actuellement avec middleware :

```
import express from 'express';
import { graphqlExpress, graphiqlExpress } from 'apollo-server-express';
import cors from 'cors';
import { makeExecutableSchema } from 'graphql-tools'
import expressPlayground from 'graphql-playground-middleware-express';
import bodyParser from 'body-parser';
require('dotenv').config();
import { v1 as neo4j } from "neo4j-driver";
import { augmentSchema } from "neo4j-graphql-js";
import { typeDefs, resolvers } from "./graphql-schema";
import { authenticateUser, authorize } from './auth';
// augmentSchema ajoutera des mutations autogénérées basées sur les types dans le schéma
const schema = makeExecutableSchema({  typeDefs,  resolvers});
const augmentedSchema = augmentSchema(schema);
const driver = neo4j.driver(  process.env.NEO4J_URI,  neo4j.auth.basic(    process.env.NEO4J_USER,    process.env.NEO4J_PASSWORD  ));
const app = express();
app.use(bodyParser.json()); // support des corps encodés en json
app.use(cors());
app.use('/graphql i apollo-server-expressql', graphiqlExpress({  endpointURL: '/graphql'}));
app.get('/', expressPlayground({ endpoint: '/graphql' }));
// app.use('/', authenticateUser, authorize);
app.use('/graphql', bodyParser.json(), graphqlExpress(req => {  return {    context:  {      auth: req.auth,      driver    },    endpointURL: '/graphql',    schema: augmentedSchema  }}));
app.listen(process.env.GRAPHQL_LISTEN_PORT, '0.0.0.0');
console.log(`GraphQL Playground at ${process.env.GRAPHQL_LISTEN_PORT}`);
```

Notez que :

1. Nous utilisons apollo-server-express, qui supporte le middleware
2. Deux fonctions sont appelées en tant que middleware : authenticateUser et authorize. Les deux définitions apparaissent dans auth.js.
3. J'ai également ajouté cors, dont nous avions besoin pour résoudre certains problèmes CORS.

Le fichier project.json doit contenir les dépendances appropriées. À l'heure actuelle, voici les versions que j'utilise :

```
{  "name": "grand-stack-express",  "version": "0.0.1",  "description": "Application API pour GRANDstack avec express",  "main": "src/index.js",  "license": "MIT",  "dependencies": {    "apollo-server-express": "^1.3.6",    "babel-cli": "^6.26.0",    "babel-core": "^6.26.3",    "babel-polyfill": "^6.26.0",    "babel-preset-env": "^1.7.0",    "babel-preset-stage-0": "^6.24.1",    "babel-watch": "^2.0.7",    "body-parser": "^1.18.3",    "cors": "^2.8.4",    "dotenv": "^6.0.0",    "express": "^4.16.3",    "express-graphql": "^0.6.12",    "graphql-playground-middleware-express": "^1.7.1",    "graphql-tag": "^2.9.2",    "graphql-tools": "^3.0.4",    "neo4j-driver": "^1.6.3",    "neo4j-graphql-js": "^0.1.32",    "node-fetch": "^2.1.2",    "nodemon": "^1.17.5"  },  "resolutions": {    "neo4j-graphql-js/graphql": "v14.0.0-rc.2"  },  "scripts": {    "test": "echo \"Error: no test specified\" && exit 1",    "dev": "babel-watch --exec babel-node --presets env,stage-0 src/index.js",    "start": "nodemon --exec babel-node --presets env,stage-0 src/index.js"  },  "devDependencies": {    "nodemon": "^1.17.5"  }}
```

Voici un fichier auth.js de départ à ajouter à votre projet et à compléter :

```
import gql from 'graphql-tag'
import { v1 as neo4j } from 'neo4j-driver';
import { INSPECT_MAX_BYTES } from 'buffer';
require('dotenv').config();
const driver = neo4j.driver(  process.env.NEO4J_URI,  neo4j.auth.basic(    process.env.NEO4J_USER,    process.env.NEO4J_PASSWORD  ));
const resolveUser = () => {  // un placeholder  return 0;}
/* * les fonctions middleware suivent */
export const authenticateUser = async (req, res, next) => {  req.auth={};  try {    const response = await resolveUser();    req.auth.user=response  } catch(err) {    req.error=err.message  }  next();}
export const authorize = async (req, res, next) => {  if (req.error) {    console.log(req.error);    next();    return;  }  // placeholder, permet chaque requête authentifiée  next();}
```

1. commencez par commiter votre ancienne version sur git et probablement créer une nouvelle branche. `git add .` puis `git commit -m "fonctionne sans auth"` et ensuite `git checkout -b auth`. Vous verrez alors une réponse de   
`Passé à une nouvelle branche 'auth'`
2. remplacez vos fichiers `api/src/index.js` et `api/project.json` par les versions ci-dessus, et ajoutez le fichier `auth.js` à `api/src`.
3. déplacez vos node_modules actuels : `mv node_modules node_modules.old`
4. exécutez `npm install` à nouveau, puis `npm start`. Assurez-vous que cela fonctionne en exécutant une requête.

![Image](https://cdn-media-1.freecodecamp.org/images/ya3u8WaXGfR4VcOTOJXpA8SNJUrAOAoiUlEG)

#### Ajoutez votre service d'authentification

Vous pouvez remplir les détails en fonction du SDK pour le logiciel d'authentification que vous utilisez.

Vous devrez peut-être étudier [l'utilisation des fonctions async/await dans une application express](https://dev.to/geoff/writing-asyncawait-middleware-in-express-6i0), mais ce n'est pas trop difficile à apprendre.

1. Décommentez la ligne `app.use('/', authenticateUser, authorize);` dans `index.js`.
2. Installez le SDK Node.js approprié pour votre service d'authentification. Ajoutez ensuite le code nécessaire et réécrivez la fonction `authenticateUser` dans `auth.js` pour l'appeler. N'oubliez pas de définir `req.error` sur un message d'erreur approprié lorsque l'authentification échoue.
3. Pratiquez en ajoutant un jeton valide à l'en-tête HTTP. Notez que dans Playground, le panneau HTTP HEADERS rend cela assez simple.

#### Ajoutez l'autorisation

Le fichier `auth.js` inclut un pilote de base de données. Le pilote supporte l'interrogation pour déterminer les droits d'accès d'un utilisateur à des données spécifiques. Par exemple, votre base de données pourrait stocker des privilèges de lecture/écriture pour les données. Chaque fois qu'une requête échoue à votre test, vous pouvez spécifier ce qui a échoué en définissant `req.error`. La fonction de résolution `neo4jgraphql` retournera le message d'erreur.

Notez que vous pouvez ajouter plus de fonctions au middleware. Par exemple, vous pourriez ajouter une vérification pour savoir si l'utilisateur actuel est entièrement payé.

#### Amélioration de AugmentSchema

L'appel à `augmentSchema` dans le fichier `index.js` génère les mutations dans votre schéma. Comme indiqué ci-dessus, une amélioration récente vous permet d'ajouter des mutations. Vous pouvez également écraser celles générées.

Une manière simple est d'utiliser la directive @cypher dans votre déclaration de mutation :

```
type Mutation { UpdateFoo(id: ID, name: String): Foo @cypher(statement:"MATCH (f:Foo {id: $id}) SET f.name = $name")}
```

Ensuite, pour le résolveur, utilisez simplement `neo4jgraphql` :

```
Mutation: { UpdateFoo: neo4jgraphql}
```

### Hébergement de la base de données

Vous avez plusieurs options. Tout d'abord, il existe certains [services d'hébergement](https://neo4j.com/developer/neo4j-cloud-hosting-providers/). Je n'ai pas été très impressionné, car ce n'est pas si difficile de créer un serveur de base de données soi-même. Mais le coût est une goutte d'eau dans l'océan par rapport au temps de votre équipe. Si vous payez quelques centaines de dollars par mois pour obtenir quelque chose qui fonctionne et que vous n'avez aucun souci, vous pourriez faire bien pire.

#### Hébergement de base

J'ai décidé de lancer une instance AWS EC2 à la place. Je vais écrire ce que j'ai fait là-bas.

1. Décidez de votre région. Cela peut ne pas avoir beaucoup d'importance, mais si vous êtes centré quelque part, alors allez-y.
2. Faites fonctionner l'AWS CLI sur votre ordinateur.
3. Obtenez une AMI appropriée. Vous pouvez rechercher sur le magasin AWS ou voir ce qui est disponible.
4. Effectuez les étapes (jusqu'à la dernière) [ici](https://neo4j.com/developer/neo4j-cloud-aws-ec2-ami/). Assurez-vous de sauvegarder votre fichier de clé, car vous en aurez besoin pour configurer APOC.
5. Ensuite, vous devez vous rendre sur la page, vous connecter et changer le mot de passe. Mais le port auquel vous devez vous rendre et le mot de passe peuvent ne pas être les mêmes. Pour mon AMI, le mot de passe était "neo4j" (comme le nom d'utilisateur). J'ai dû me rendre sur [https://[IP]:7473/browser/](https://[IP]:7473/browser/) (pas http comme dans l'exemple donné sur la page, et pas 7434).
6. Changez votre code sur votre machine locale pour vous assurer que vous pouvez vous y connecter. Vérifiez-le sur votre localhost:4000.

#### Configuration d'APOC

Pour utiliser les directives `@cypher`, ou l'une des [fonctions APOC](https://neo4j-contrib.github.io/neo4j-apoc-procedures/), vous devrez installer le fichier jar APOC sur le serveur lui-même. Vous devrez vous connecter en ssh à votre serveur de base de données. Il y a deux mois, il n'était pas inclus dans les AMI.

1. Vous devrez utiliser la commande indiquée dans [Hébergement de Neo4j sur EC2 sur AWS](https://neo4j.com/developer/neo4j-cloud-aws-ec2-ami/) : `ssh -i $KEY_NAME.pem ubuntu@[PublicDnsName]`
2. Vous devrez ajouter le fichier jar au répertoire des plugins neo4j. [Suivez les instructions manuelles](https://github.com/neo4j-contrib/neo4j-apoc-procedures#manual-installation-download-latest-release) pour trouver la dernière version et déterminer où l'insérer.
3. Vous devez également trouver votre fichier neo4j.conf et y insérer la permission d'appeler les fonctions. Ce qui suit fonctionne : `dbms.security.procedures.unrestricted=apoc.*`
4. Ensuite, vous devrez redémarrer : `sudo systemctl restart neo4j.`

### Déploiement de l'API

Vous pouvez déployer sur n'importe quel système qui supporte une application NODE js. J'ai utilisé [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) :

1. Exécutez la commande `zip -r api.zip . -x node_modules/**\*` dans le répertoire `api`. Cela crée un zip sans le répertoire lui-même et sans les node_modules.
2. Allez sur [AWS Elastic Beanstalk](https://console.aws.amazon.com/elasticbeanstalk/home?region=us-east-1#/welcome) dans la console et assurez-vous d'être dans votre région de choix.
3. Si vous pouvez accéder à la page de bienvenue, je la trouve la plus facile. Vous cliquez sur **Commencer**, et suivez les instructions. Ils m'ont tout de suite configuré avec ce dont j'avais besoin. Vous téléchargez simplement le fichier que vous avez zippé ci-dessus.
4. Sous **Configuration pour l'environnement Elastic Beanstalk**, allez dans **Modifier le logiciel**. Entrez **Options de conteneur**, et définissez **Commande Node** sur `npm start`.
5. Après environ 10 minutes, c'est prêt. Vous pouvez cliquer sur l'**URL de point de terminaison** pour le voir.
6. Utilisez Route53 pour aliasser votre propre domaine api au point de terminaison Elastic Beanstalk, et vous êtes prêt.

### Conclusions

Si vous avez suivi jusqu'ici, félicitations. Vous en savez plus sur la construction d'une [pile graphique complète](https://medium.com/p/d32150308a87/edit) que de nombreux concepteurs back-end expérimentés.

Le processus décrit dans ces articles peut prendre une heure pour quelqu'un qui les a faits quelques fois. Pour les autres, ces articles minimisent, espérons-le, le temps supplémentaire de recherche. Le temps de développement devrait encore diminuer à mesure que ces outils s'améliorent.

Mais la simplicité et la facilité ne sont qu'un avantage. La pile graphique complète est également technologiquement solide.

* Le serveur créé ici est robuste.
* Une base de données graphique, en général, s'adapte brillamment.
* La pile utilise très peu de ressources.
* Vous pouvez porter le back-end vers différents hôtes ou services, réduisant ainsi le verrouillage et les frais.

Travaillons ensemble pour faire avancer cette technologie. Veuillez laisser des commentaires ou nous contacter avec d'autres améliorations. Bonne chance avec vos propres projets !