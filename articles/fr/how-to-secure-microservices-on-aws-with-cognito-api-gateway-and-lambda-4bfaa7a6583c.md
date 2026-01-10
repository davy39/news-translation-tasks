---
title: Comment sécuriser les Microservices sur AWS avec Cognito, API Gateway et Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T20:44:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-microservices-on-aws-with-cognito-api-gateway-and-lambda-4bfaa7a6583c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b46gRLzVry1kr8ikUOrXMg.jpeg
tags:
- name: AWS
  slug: aws
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Comment sécuriser les Microservices sur AWS avec Cognito, API Gateway et
  Lambda
seo_desc: 'By Christian Sepulveda


  _let me in! ([Giphy](https://media.giphy.com/media/3o6gb3kkXfLvdKEZs4/giphy.gif"
  rel="noopener" target="blank" title="))

  Handling auth is painful. But most applications need to authenticate users and control
  what resources the...'
---

Par Christian Sepulveda

![Image](https://cdn-media-1.freecodecamp.org/images/1*CKz6WCjkxktPPhGtpXGefA.gif)
_laissez-moi entrer ! ([Giphy](https://media.giphy.com/media/3o6gb3kkXfLvdKEZs4/giphy.gif" rel="noopener" target="_blank" title="))_

Gérer l'authentification est douloureux. Mais la plupart des applications doivent authentifier les utilisateurs et contrôler les ressourcesqu'ils peuvent accéder. [Microservices](https://martinfowler.com/articles/microservices.html), bien que de plus en plus populaires, peuvent ajouter de la complexité. Vous devez sécuriser _à la fois_ les actions de l'utilisateur et les interactions _entre_ les services.

[AWS](https://aws.amazon.com/) offre quelques excellents blocs de construction pour une architecture de microservices. Mais comme les meubles d'IKEA, vous devez assembler les pièces vous-même. De plus, les instructions ne sont pas très bonnes.

Nous allons construire une application simple et configurer AWS pour authentifier un utilisateur et sécuriser un microservice.

### TL;DR (pour les impatients)

**Démo fonctionnelle :** [https://auth-api-demo.firebaseapp.com/](https://auth-api-demo.firebaseapp.com/) (utilisateur : `demouser` mot de passe : `demoPASS123`)

**Dépôt GitHub :** [https://github.com/csepulv/auth-api-demo](https://github.com/csepulv/auth-api-demo)

**Cas d'utilisation/Assomption de base :** Il y a deux groupes de ressources — **a)** celles qui nécessitent un utilisateur _authentifié_ et **b)** celles qui n'en ont pas besoin.

Nous utiliserons

* AWS [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), et [Cognito](https://aws.amazon.com/cognito/dev-resources/)
* [Claudia.js](https://claudiajs.com/) (pour construire notre API)
* [React](https://reactjs.org/) (pour notre client web)

Pour ceux qui lisent jusqu'à la fin, il y a quelques bonus.

Maintenant, pour les détails.

### Modèle d'application conceptuel

L'application de démonstration implémente le modèle suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vq_EQibUjpiCK1C_rF1azg.jpeg)

* Un utilisateur se connecte à une application et obtient un jeton d'authentification
* AWS utilise ce jeton pour vérifier l'identité et autoriser les demandes d'utilisateurs pour les ressources protégées
* l'App Gateway crée un _fossé_ virtuel entre les utilisateurs et les ressources de l'application

### Services AWS

Si vous êtes nouveau sur AWS, il y a le portail officiel [AWS Getting Started](https://aws.amazon.com/getting-started/). De plus, Udemy propose un cours gratuit, [AWS Essentials](https://www.udemy.com/aws-essentials/).

Vous aurez besoin d'un accès à un compte AWS. Vous pouvez vous inscrire pour le niveau [gratuit d'AWS](https://aws.amazon.com/free/).

#### AWS Lambda

Bien que [EC2](https://aws.amazon.com/ec2/) soit l'une des options AWS les plus populaires, je pense que [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) est mieux adapté aux microservices. Les instances EC2 sont des machines virtuelles. Vous êtes responsable de tout, du système d'exploitation à tous les logiciels qu'il exécute. Lambda est un modèle [Function as a Service](https://martinfowler.com/articles/serverless.html). Il n'y a pas de provisionnement ou de déploiement de serveur ; vous écrivez votre logique de service.

Pour plus d'informations, consultez la [documentation AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

Mais il y a un problème avec les Lambdas. Ils ne peuvent pas être atteints directement par un utilisateur d'application. Les Lambdas ont besoin de déclencheurs qui invoquent la fonction Lambda. Cela peut être un message en file d'attente, ou dans notre cas, une demande de passerelle API.

#### AWS API Gateway

Une passerelle API fournit un fossé autour de vos services d'application. Elle peut journaliser l'activité des utilisateurs, authentifier les demandes et appliquer des politiques d'utilisation (comme la limitation de débit). (La [documentation AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) est une bonne référence.)

#### AWS Cognito

[AWS Cognito](https://aws.amazon.com/cognito/dev-resources/) est un service de gestion des utilisateurs, d'authentification et de contrôle d'accès. Malheureusement, toutes les fonctionnalités et la configuration peuvent être déroutantes à certains moments. (Comme si la sécurité et l'authentification étaient jamais faciles. ?) Nous allons nous concentrer sur les éléments principaux de Cognito pour sécuriser notre API.

### Configuration de l'application et de l'environnement

![Image](https://cdn-media-1.freecodecamp.org/images/1*b46gRLzVry1kr8ikUOrXMg.jpeg)
_Éléments de l'application_

La recette pour notre application de démonstration est :

1. Dans AWS Cognito, créez un User Pool (avec une application cliente) et un Federated Identity Pool.
2. Dans AWS API Gateway, créez un plan d'utilisation et une clé API
3. En utilisant Claudia JS, construisez et déployez une API simple basée sur AWS Lambda.
4. Mettez à jour le rôle AWS IAM pour accorder aux utilisateurs authentifiés l'accès aux méthodes API protégées
5. Créez une application monopage (SPA) en utilisant `create-react-app`. Elle utilisera AWS Cognito et effectuera des demandes d'API signées (et authentifiées)

La configuration détaillée d'AWS se trouve dans `[aws-setup.md](https://github.com/csepulv/auth-api-demo/blob/master/docs/aws-setup.md)`, dans le dépôt GitHub de démonstration. Nous mettrons en évidence certains aspects de la configuration et expliquerons comment les choses fonctionnent.

#### AWS Cognito

**User Pool, Application cliente et Nom de domaine**

Nous allons créer un User Pool avec les paramètres par défaut. Détails et captures d'écran :

* [User Pool](https://github.com/csepulv/auth-api-demo/blob/master/docs/aws-setup.md#user-pool)
* [Application cliente](https://github.com/csepulv/auth-api-demo/blob/master/docs/aws-setup.md#app-client-settings)
* [Nom de domaine](https://github.com/csepulv/auth-api-demo/blob/master/docs/aws-setup.md#domain-name)

**Federated Identity Pool**

Il peut être un peu déroutant que nous ayons besoin à la fois d'un User Pool et d'un Federated Identity Pool. [Ashan Fernando](https://www.freecodecamp.org/news/how-to-secure-microservices-on-aws-with-cognito-api-gateway-and-lambda-4bfaa7a6583c/undefined) a une assez bonne explication dans cet [article](https://codeburst.io/the-difference-between-aws-cognito-userpools-and-federated-identities-9b47571795d4). En résumé,

* Les _User Pools_ fournissent un accès pour un utilisateur à une application. C'est comme des services tels que [Auth0](https://auth0.io).
* Un _Federated Identity Pool_ fournit un accès aux ressources AWS.

En combinant les deux pools, notre application peut authentifier un utilisateur et AWS attribuera des [identifiants temporaires](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html). Ces identifiants permettent à l'utilisateur d'accéder aux ressources AWS. Le rôle IAM, configuré dans le Identity Pool, spécifie les privilèges pour les identifiants temporaires.

La configuration détaillée du Federated Identity Pool se trouve [ici](https://github.com/csepulv/auth-api-demo/blob/master/docs/aws-setup.md#federated-identity-pool).

#### AWS API Gateway

Je suggère de créer un plan d'utilisation pour notre API. Bien que ce ne soit pas une exigence, c'est une bonne pratique, car les coûts AWS peuvent "s'envoler" si vous n'êtes pas prudent. Nous allons créer un [**Usage Plan**](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html), nommé `api-auth-demo` et définir un débit et un taux de rafale, et un quota quotidien pour les appels API. Nous allons également créer une clé API, que l'application cliente web utilisera. (Les détails complets de la configuration sont [ici](https://github.com/csepulv/auth-api-demo/blob/master/docs/aws-setup.md#api-gateway).)

![Image](https://cdn-media-1.freecodecamp.org/images/1*hyVIHxcwGElJbWp3cEYebw.png)
_limites de débit et quota_

Nous avons terminé la majeure partie de notre configuration AWS. Nous allons maintenant écrire nos fonctions Lambda puis construire notre application web React.

### AWS Lambda et Claudia JS

Nous allons écrire nos fonctions Lambda en utilisant Node.js. [Claudia.js](https://claudiajs.com/) déployera nos Lambdas et configurera l'API Gateway. (À noter, le framework [Serverless](https://serverless.com/) offre une fonctionnalité similaire.)

Nous n'avons besoin que d'une API simple pour notre exemple. Nous allons créer deux méthodes API (c'est-à-dire des microservices très simples) : une pour les utilisateurs authentifiés et une pour les invités.

Nous allons utiliser le [Claudia API Builder](https://claudiajs.com/claudia-api-builder.html), qui permet à plusieurs routes de mapper vers un seul lambda. Le mécanisme de routage est similaire au routage dans des frameworks tels que [Express.js](https://expressjs.com/en/guide/routing.html).

```javascript

const ApiBuilder = require("claudia-api-builder");
const api = new ApiBuilder();

api.get("/no-auth",request => {
    return {message: "Open for All!"};
  },
  { apiKeyRequired: true }
);

api.get("/require-auth", request => {
    return {message: "You're past the velvet rope!"};
  },
  { apiKeyRequired: true, authorizationType: "AWS_IAM" }
);

module.exports = api;
view rawapi.js hosted with [31m[39m by GitHub
```

Nous allons utiliser la [ligne de commande](https://github.com/claudiajs/claudia/blob/master/docs/create.md) de Claudia.js pour déployer l'API sur AWS.

```
claudia create --region us-west-2  --api-module api --name auth-api-demo
```

NOTE : Toute modification de `api.js` devra être redéployée. Utilisez `claudia update...`

**Clés API et Auth**

Dans `api.js`, `{apiKeyRequired: true}` indique que les demandes API nécessitent une clé API. `{authorizationType: 'AWS_IAM'}` configure l'API Gateway pour autoriser en utilisant [AWS IAM](https://aws.amazon.com/iam/). Le mécanisme d'authentification sous-jacent n'est pas évident. La [documentation AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) décrit l'approche, mais un résumé est :

* lorsqu'un utilisateur se connecte, Cognito émettra des jetons pour des identifiants temporaires (obtenus via [STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)).
* pour les ressources protégées, l'application doit signer les demandes en utilisant ces identifiants
* AWS décode et vérifie la signature
* si la signature est valide, l'API Gateway envoie la demande

Il existe d'autres méthodes d'autorisation disponibles. La documentation de Claudia.js [docs](https://github.com/claudiajs/claudia-api-builder/blob/master/docs/authorization.md) décrit comment spécifier d'autres méthodes. (La documentation AWS correspondante est [ici](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html).)

#### Rôles AWS IAM pour les utilisateurs authentifiés

Nous devons modifier les privilèges des rôles IAM pour les utilisateurs authentifiés. Nous devons permettre l'invocation de la méthode API Gateway que nous avons créée.

Nous avons besoin de l'[ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) de l'API Gateway. Allez dans la console API Gateway et trouvez la ressource/méthode API Gateway.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EaRh0csoB_smLKrY42uIBA.jpeg)
_ARN (montré en surbrillance)_

* Copiez l'ARN
* Allez dans la console IAM et trouvez le _rôle authentifié_ créé lors de la configuration du Federated Identity Pool de Cognito
* ajoutez une _politique en ligne_ comme ci-dessous

![Image](https://cdn-media-1.freecodecamp.org/images/1*UZPI5CLzl3xdxg6A9IHwLg.jpeg)
_entrez l'ARN copié depuis la ressource API Gateway (dans la zone en surbrillance)_

* Spécifiez l'ARN copié pour la ressource API Gateway dans la politique.

Les utilisateurs authentifiés peuvent maintenant invoquer nos méthodes API protégées.

### Contrôle d'accès de service à service

La configuration de Cognito permettra à un utilisateur d'invoquer une méthode API. Mais cette invocation de méthode est un déclencheur pour une fonction Lambda. La fonction Lambda s'exécute dans le contexte d'un rôle IAM différent. Ce n'est plus une demande directe de l'utilisateur, mais une interaction de service AWS à service. Les rôles IAM fournissent un contrôle d'accès pour cette interaction.

Claudia.JS a créé le rôle IAM pour la fonction Lambda. (Vous pouvez également créer manuellement ce rôle et spécifier son identifiant à Claudia.JS via le paramètre `--role`. Les détails sont [ici](https://github.com/claudiajs/claudia/blob/master/docs/create.md).)

Si notre fonction Lambda a besoin d'accéder à d'autres ressources AWS, nous devrons mettre à jour le rôle IAM de la Lambda et fournir ces privilèges. Cela pourrait être une base de données [RDS](https://aws.amazon.com/rds/), par exemple.

AWS a toujours utilisé IAM pour configurer le contrôle d'accès de service à service. C'est un modèle bien développé et [bien documenté](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). Ce sera probablement votre mécanisme principal pour le contrôle d'accès entre les microservices (au sein d'AWS). Il peut y avoir des cas où vous devez l'augmenter ou le remplacer, mais je commencerais par IAM.

Nous pouvons maintenant construire l'application web pour nos utilisateurs.

### Application Web React

Je vais construire une application web monopage [React](https://reactjs.org/) (SPA). Une application [Vue.js](https://vuejs.org/) ou [Angular](https://angularjs.org/) fonctionnerait aussi. Pour l'application cliente, il y a deux composants significatifs : [AWS Amplify](https://aws-amplify.github.io/amplify-js/index.html) et le module `[aws4](https://www.npmjs.com/package/aws4)`.

AWS Amplify fournit une intégration facile avec AWS Cognito. `aws4` est une bibliothèque populaire pour signer les demandes AWS en utilisant [AWS Request Signatures Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). AWS utilise des demandes signées pour les ressources protégées (c'est-à-dire les demandes d'utilisateurs autorisées).

Revenons au client web, nous allons utiliser `[create-react-app](https://github.com/facebook/create-react-app)`. Je ne vais pas décrire les étapes, car elles sont bien documentées sur la page d'accueil de `create-react-app`, et il existe de nombreux tutoriels en ligne. (J'ai même écrit [quelques](https://medium.freecodecamp.org/how-to-build-animated-microinteractions-in-react-aab1cb9fe7c8). )

Pour l'authentification, nous devons faire de la gestion d'état. L'application d'exemple n'utilise aucun framework, mais dans une application réelle, je suggérerais [Mobx](https://mobx.js.org/) (ou [Redux](https://redux.js.org/).)

Dans l'application de démonstration, `auth-store.js` gère l'état d'authentification de l'utilisateur. Cela consiste en l'état d'authentification de l'utilisateur et ses identifiants. Ceux-ci sont utilisés pour

* rendre différents composants et styles pour les utilisateurs authentifiés et invités
* signer les demandes pour les méthodes API protégées

Bien qu'AWS Amplify gère une grande partie de l'intégration AWS Cognito, il y a encore du travail à faire pour nous.

**Détermination de l'état d'authentification à partir d'AWS Amplify**

La documentation d'AWS Amplify est bonne dans certains domaines et déficiente dans d'autres. Je suggère de lire la [section Authentication](https://aws-amplify.github.io/amplify-js/media/authentication_guide) de la documentation Amplify. Cela décrit le composant `Auth`, qui interagit avec Cognito.

Cependant, il y a encore certains aspects que la documentation n'aborde pas clairement. AWS Amplify ne facilite pas la connaissance de l'état d'authentification. (Une discussion sur cette complexité se trouve [ici](https://github.com/aws-amplify/amplify-js/issues/159#issuecomment-374028468).) Amplify se configure de manière asynchrone, sans rappel. Mais il y a une classe `aws-amplify` qui peut aider.

La classe `[Hub](https://github.com/aws-amplify/amplify-js/blob/master/docs/media/hub_guide.md)` dans le module `aws-amplify` se comporte comme un émetteur d'événements. Nous nous intéressons à deux événements : `configured` et `cognitoHostedUI`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4tvCgp1hgYXycSJleun6rw.jpeg)
_séquence de chargement/configuration de la page_

Après qu'AWS Amplify a configuré le composant `Auth`, il émet l'événement `configured`. Notre application peut alors interroger le statut d'authentification de l'utilisateur actuel. Cela est utile lorsque notre application est en cours de chargement, par exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vWN0pVQVoa0qY-jg3HottA.jpeg)
_séquence de changement d'état de connexion/authentification_

Lors de l'utilisation de l'application, nous devons savoir si l'état d'authentification change. Il y a un événement `sign-in`, mais ce n'est pas l'événement que nous voulons, car notre application de démonstration utilise [OAuth et l'interface utilisateur hébergée par Cognito](https://aws-amplify.github.io/amplify-js/media/authentication_guide#using-amazon-cognito-hosted-ui). L'événement `sign-in` est utilisé dans un écran de connexion/inscription personnalisé ou lors de l'utilisation de l'interface utilisateur React Amplify intégrée. Pour OAuth, Amplify envoie l'événement `cognitoHostedUI` après un flux de connexion OAuth terminé.

**Signature des demandes**

L'utilisateur actuel aura des identifiants émis par AWS Cognito. Ceux-ci contiennent un _identifiant d'accès_, une _clé secrète_ et une _clé de session_. Ceux-ci sont disponibles en appelant `Auth.currentCredentials()` dans `aws-amplify`. Pour les méthodes API autorisées par IAM, vous devez _signer_ la demande en utilisant [AWS V4 Request Signatures](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). Heureusement, le module `[aws4](https://www.npmjs.com/package/aws4)` gère les complexités de la génération de ces signatures.

Dans `[api-client.js](https://github.com/csepulv/auth-api-demo/blob/master/web-ui/src/api-client.js)`,

```javascript

import aws4 from "aws4";

const apiHost = process.env.REACT_APP_API_HOST;
const apiKey = process.env.REACT_APP_API_KEY;
const region = process.env.REACT_APP_REGION;

export async function authenticatedCall(authStore) {
  const opts = {
    method: "GET",
    service: "execute-api",
    region: region,
    path: "/latest/require-auth",
    host: apiHost,
    headers: { "x-api-key": apiKey },
    url: `https://${apiHost}/latest/require-auth`
  };
  const credentials = await authStore.getCredentials();
  const { accessKeyId, secretAccessKey, sessionToken } = credentials;
  const request = aws4.sign(opts, {
    accessKeyId,
    secretAccessKey,
    sessionToken
  });
  delete request.headers.Host;
  const response = await fetch(opts.url, {
    headers: request.headers
  });
  if (response.ok) {
    return await response.json();
  } else return { message: response.statusText };
}

export async function noAuthCall(authStore) {
  const response = await fetch(`https://${apiHost}/latest/no-auth`, {
    headers: { "x-api-key": apiKey }
  });
  return await response.json();
}
view rawapi-client.js hosted with [31m[39m by GitHub
```

#### Démo

Nous pouvons enfin exécuter `npm start` et lancer l'application ! Lorsque nous arrivons pour la première fois sur l'application, nous sommes un invité (utilisateur non authentifié). Vous pouvez également aller sur [https://auth-api-demo.firebaseapp.com/](https://auth-api-demo.firebaseapp.com/) pour l'essayer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5jsOZ6Qsn6xFn9eqZixKDA.png)

Nous pouvons accéder aux méthodes non protégées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fCm0PGScMXKBMtNzea7QOw.png)
_l'authentification n'est pas requise_

Mais si nous essayons d'accéder à une ressource protégée, cela échouera.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UEcp7iF8kWvrE8dnjpZ0WQ.png)
_non authentifié_

Mais si nous nous connectons, nous pouvons accéder aux ressources protégées.

Cliquez sur **Se connecter** et utilisez `demouser` avec le mot de passe `demoPASS123`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ot3j4-o8OaBiaagTy9hMfg.png)
_après la connexion — les boutons reflètent un état authentifié_

Nous pouvons maintenant cliquer sur le bouton `Req. Auth` pour accéder à une méthode API protégée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kANusN4eyPy0PBufRlD51A.png)

Ouf ! Nous avons dû configurer plusieurs services et digérer beaucoup d'informations. Mais nous avons maintenant une application qui est un modèle pour l'authentification des microservices sur AWS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uvDysqC-6VLSBHIEmjrmmw.gif)
_[Giphy](https://giphy.com/gifs/reese-witherspoon-y4OKEc5NuPDwY" rel="noopener" target="_blank" title=")_

### Et maintenant ?

L'approche de cet article est "tout-en-un" sur AWS. Ce fut un choix délibéré, pour montrer comment les différentes pièces d'AWS s'emboîtent pour résoudre un besoin commun, à savoir l'authentification. Il existe des alternatives aux méthodes de cet article, et j'en décris quelques-unes [ici](https://github.com/csepulv/auth-api-demo/blob/master/docs/auth-alternatives.md).

Et pour ceux qui sont restés avec moi jusqu'à la fin, j'ai quelques cadeaux de départ.

* Dans le [dépôt de démonstration](https://github.com/csepulv/auth-api-demo), il y a un [script](https://github.com/csepulv/auth-api-demo/blob/master/scripts/create-resources.js) pour automatiser la configuration AWS. Son [README](https://github.com/csepulv/auth-api-demo/blob/master/scripts/README.md) contient les détails pour l'exécuter.
* `[resources-cheatsheet.md](https://github.com/csepulv/auth-api-demo/blob/master/docs/resource-cheatsheet.md)` contient les liens spécifiques pour la documentation pertinente d'AWS, Claudia.js, etc.

Merci d'avoir lu !