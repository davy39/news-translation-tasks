---
title: Comment créer un raccourcisseur d'URL sans serveur en utilisant AWS Lambda
  et S3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-01T21:09:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-url-shortener-using-aws-lambda-and-s3-4fbdf70cbf5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9sb5DpSDIGpG1zhzvVAuXQ.png
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: Web Development
  slug: web-development
seo_title: Comment créer un raccourcisseur d'URL sans serveur en utilisant AWS Lambda
  et S3
seo_desc: 'By Daniel Ireson

  Throughout this post we’ll be building a serverless URL shortener using Amazon Web
  Services (AWS) Lambda and S3. Whilst you don’t require any previous experience with
  AWS, I’m assuming some familiarity with ES6 JavaScript and Node.js...'
---

Par Daniel Ireson

Tout au long de cet article, nous allons créer un raccourcisseur d'URL sans serveur en utilisant Amazon Web Services (AWS) Lambda et S3. Bien que vous n'ayez pas besoin d'expérience préalable avec AWS, j'assume une certaine familiarité avec ES6 JavaScript et Node.js.

Ironiquement, les URL générées par notre raccourcisseur d'URL seront souvent plus longues que les URL vers lesquelles elles redirigent - cela est dû au fait que nous utilisons l'adresse du site web par défaut du bucket S3. Vers la fin de l'article, je discuterai de la manière dont vous pouvez ajouter un domaine personnalisé pour contourner cette limitation.

#### [Voir la démonstration](http://serverless-url-shortener.s3-website-eu-west-1.amazonaws.com)

#### [Voir le code sur Github](https://github.com/danielireson/serverless-url-shortener)

![Image](https://cdn-media-1.freecodecamp.org/images/tEVMAYbvGlK1NVTUsULy984Ee322WWoMTtax)

Il est relativement facile de commencer avec AWS et pourtant il y a définitivement une complexité perçue. Le nombre de services disponibles peut être décourageant à choisir parmi eux, car beaucoup se chevauchent en termes de fonctionnalités. La console de gestion AWS lente et peu intuitive n'aide pas, ni la documentation en ligne très textuelle. Mais tout au long de cet article, j'espère démontrer que la meilleure façon d'adopter les services AWS est d'utiliser une approche incrémentale et que vous pouvez commencer en utilisant seulement une poignée de services.

Nous allons utiliser le [Framework Serverless](https://serverless.com) pour interagir avec AWS et donc il n'y aura pas besoin de se connecter à la console de gestion AWS. Le Framework Serverless fournit une abstraction sur AWS et aide à fournir une structure de projet et des configurations par défaut sensées. Si vous souhaitez en savoir plus avant de commencer, vous devriez lire leur [documentation](https://serverless.com/framework/docs/).

### Architecture

Avant de plonger dans le développement, examinons d'abord les services AWS que nous allons utiliser pour construire notre raccourcisseur d'URL.

Pour héberger notre site web, nous allons utiliser le service de stockage de fichiers Amazon S3. Nous allons configurer notre bucket S3, qui peut être considéré comme un dossier de premier niveau, pour servir un site web statique. Le site web sera composé de contenu statique et de scripts côté client. Il n'y a pas de capacité à exécuter du code côté serveur (comme PHP, Ruby ou Java par exemple), mais cela convient parfaitement à notre cas d'utilisation.

Nous allons également utiliser une [fonctionnalité peu connue](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html) de S3 qui vous permet de configurer la redirection pour les objets à l'intérieur des buckets S3 simplement en ajoutant une valeur `Website-Redirect-Location` aux métadonnées de l'objet. En définissant cela sur une URL, les navigateurs seront redirigés via une réponse HTTP 301 et l'en-tête `location`.

L'URL d'un objet S3 est composée de l'adresse du bucket S3 suivie du nom de l'objet.

```
http://[nom-du-bucket].s3-website-eu-west-1.amazonaws.com/[nom-de-l'objet]
```

Voici un exemple du format d'un objet de bucket S3 pour la région `eu-west-1`.

```
http://serverless-url-shortener.s3-website-eu-west-1.amazonaws.com/6GpLcdl
```

Ce nom d'objet « 6GpLcdl » à la fin de l'URL dans l'exemple ci-dessus devient le code court pour nos URL raccourcies. En utilisant cette fonctionnalité, nous obtenons une redirection d'URL native ainsi que des capacités de stockage. Nous n'avons pas besoin d'une base de données pour stocker les détails de quel code court pointe vers quelle URL, car cette information sera stockée avec l'objet lui-même.

Nous allons créer une fonction Lambda pour sauvegarder ces objets S3 avec les métadonnées appropriées dans notre bucket S3.

Vous pourriez alternativement utiliser le SDK AWS côté client dans le navigateur pour sauvegarder les objets. Mais il est préférable d'extraire cette fonctionnalité dans un service séparé. Cela offre l'avantage de ne pas avoir à se soucier de l'exposition des informations d'identification de sécurité et est plus extensible à l'avenir. Nous allons mapper la fonction Lambda à un point de terminaison sur API Gateway afin qu'elle soit accessible via un appel d'API.

### Getting started

Rendez-vous sur la [documentation du Framework Serverless](https://serverless.com/framework/docs/providers/aws/guide/quick-start/) et suivez leur guide de démarrage rapide. Dans le cadre du processus de configuration, vous devrez installer le [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) et configurer vos informations d'identification AWS.

Commencez par créer un fichier `package.json` à la racine du projet.

```
{  "name": "serverless-url-shortener",  "scripts": {},  "dependencies": {}}
```

Nous savons que nous aurons besoin d'utiliser le [SDK AWS](https://aws.amazon.com/sdk-for-node-js/), alors installez-le depuis NPM en entrant la commande suivante.

`npm install aws-sdk --save`

Créez maintenant un fichier `config.json` également à la racine du projet. Nous allons l'utiliser pour stocker les options utilisateur personnalisables au format JSON.

Ajoutez les clés suivantes avec des valeurs appropriées à votre configuration.

* **BUCKET** - le nom que vous souhaitez utiliser pour votre bucket S3. Cela deviendra une partie de l'URL courte si vous choisissez de ne pas ajouter un domaine personnalisé. Il doit être unique pour la région dans laquelle vous déployez, alors ne choisissez pas quelque chose de trop générique. Mais ne vous inquiétez pas, si le nom de bucket choisi est déjà utilisé, vous serez averti via le CLI Serverless au moment du déploiement.
* **REGION** - la [région AWS](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) dans laquelle vous souhaitez déployer. Il est préférable de choisir la région la plus proche de vos utilisateurs pour des raisons de performance. Si vous suivez simplement ce tutoriel, j'utiliserai `eu-west-1`.
* **STAGE** - l'étape à déployer. Typiquement, vous auriez un environnement de staging qui reproduit la même configuration que votre environnement de production. Cela vous permet de tester les versions logicielles de manière non destructive. Comme il s'agit d'un tutoriel, je vais déployer à l'étape `dev`.

Votre fichier `config.json` devrait ressembler à ce qui suit une fois complété.

```
{  "BUCKET": "votre-nom-de-bucket",  "REGION": "eu-west-1",  "STAGE": "dev",}
```

Ensuite, créez un autre fichier à la racine du projet, `serverless.yml`. Cela contiendra notre configuration du Framework Serverless formatée dans le langage de balisage YAML.

Dans ce fichier, nous allons commencer par définir notre environnement. Remarquez comment nous pouvons référencer les variables stockées précédemment dans `config.json`.

```
service: serverless-url-shortenerprovider:  name: aws  runtime: nodejs6.10  stage: ${file(config.json):STAGE}  region: ${file(config.json):REGION}  iamRoleStatements:    - Effect: Allow      Action:        - s3:PutObject      Resource: "arn:aws:s3:::${file(config.json):BUCKET}/*"
```

La section `iamRoleStatements` fait référence à [Identity and Access Management](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) qui est utilisé pour configurer les permissions Lambda. Ici, nous donnons à Lambda l'accès en écriture à notre bucket S3.

Pour sauvegarder des objets, nous avons besoin de la permission d'exécuter l'action `s3:PutObject`. D'autres permissions peuvent être ajoutées ici si elles sont requises par votre projet. Consultez la [documentation S3](http://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html#using-with-s3-actions-related-to-objects) pour d'autres actions disponibles.

La valeur `Resource` est définie sur le [Nom de Ressource Amazon](http://Amazon Resource Name) du bucket S3, qui est utilisé pour identifier de manière unique une ressource AWS particulière. Le format de cet identifiant dépend du service AWS auquel il est fait référence, mais généralement, ils ont le format suivant.

```
arn:partition:service:region:account-id:resource
```

Sous `provider`, ajoutez notre configuration `functions`.

```
functions:  store:    handler: api.handle    events:      - http:          path: /          method: post          cors: true
```

Ici, nous définissons la configuration de l'API et mappons notre Lambda à un événement HTTP POST à l'URL de base de l'API. Un `handler` avec la valeur `api.handle` fait référence à une fonction nommée `handle` qui est exportée depuis `api.js` (nous n'avons pas besoin de l'extension de fichier _js_ car plus tôt dans `serverless.yml` nous avons défini le runtime à `nodejs6.10`).

Lambda est basé sur des événements et donc les fonctions ne sont exécutées que sur la base de déclencheurs prédéfinis. Ici, nous avons défini un événement HTTP, mais cela aurait également pu être un événement déclenché par une table DynamoDB ou une file d'attente SQS.

Ensuite, dans `serverless.yml`, nous définissons les ressources AWS à instancier pour nous lors du déploiement en utilisant [CloudFormation](https://aws.amazon.com/cloudformation). Il est utile de mentionner que vous n'êtes pas nécessairement obligé de configurer les ressources de cette manière, vous pourriez également les créer en utilisant la console de gestion AWS. À condition que les permissions d'accès appropriées soient en place, peu importe comment les ressources sont créées. Mais en définissant les services requis dans `serverless.yml`, vous définissez votre 'infrastructure en tant que code' et obtenez un certain nombre d'avantages en le faisant.

> « L'infrastructure en tant que code est l'approche de la définition de l'infrastructure informatique et réseau par le biais de code source qui peut ensuite être traité comme n'importe quel système logiciel. Un tel code peut être conservé dans le contrôle de source pour permettre l'auditabilité et les ReproducibleBuilds, soumis à des pratiques de test, et à la discipline complète de la ContinuousDelivery. »

> - Martin Fowler

Allez-y et ajoutez la configuration `resources`.

```
resources:  Resources:    ServerlessRedirectS3Bucket:      Type: AWS::S3::Bucket      Properties:        BucketName: ${file(config.json):BUCKET}        AccessControl: PublicRead        WebsiteConfiguration:          IndexDocument: index.html    ServerlessRedirectS3BucketPolicy:      Type: AWS::S3::BucketPolicy      Properties:        Bucket: ${file(config.json):BUCKET}        PolicyDocument:          Statement:          - Action:            - s3:GetObject            Effect: Allow            Resource:            - arn:aws:s3:::${file(config.json):BUCKET}/*            Principal: "*"
```

Nous demandons une ressource de bucket S3 configurée pour utiliser l'hébergement de site statique avec `index.html` comme document racine. Les buckets S3 sont privés par défaut pour de bonnes raisons, nous devons donc créer une politique de bucket S3 qui permet l'accès public. Sans cette politique, les visiteurs du site web verraient un message d'erreur non authentifié.

### Building the API

Notre fonction Lambda est responsable de quatre tâches.

1. Récupérer l'URL à raccourcir à partir de la soumission du formulaire de l'utilisateur.
2. Générer un code court unique pour l'URL.
3. Sauvegarder l'objet de redirection approprié dans S3.
4. Retourner le chemin de l'objet au client.

#### Create the handler

Créez un nouveau fichier appelé `api.js` et exportez une fonction fléchée nommée `handle` qui prend trois arguments : `event`, `context` et `callback`. Ceux-ci seront fournis par AWS lorsque le handler est invoqué. Ce fichier est un script Node.js et pour exporter la fonction fléchée, vous devez l'ajouter à `module.exports`.

```
module.exports.handle = (event, context, callback) => {
```

```
}
```

Ce handler sera invoqué lorsqu'une requête HTTP POST est faite à notre endpoint. Pour retourner une réponse API, nous devons utiliser la fonction de rappel fournie en tant que troisième argument de la fonction fléchée. C'est un [callback error-first](http://fredkschott.com/post/2014/03/understanding-error-first-callbacks-in-node-js/) qui prend deux arguments. Si la requête s'est terminée avec succès, `null` doit être passé en tant que premier argument. L'objet de réponse passé en tant que deuxième argument détermine le type de réponse à retourner à l'utilisateur. Générer une réponse est aussi simple que de fournir un `statusCode` et un `body` comme le montre l'exemple ci-dessous.

```
const response = {  statusCode: 201,  body: JSON.stringify({ "shortUrl": "http://example.com" })}
```

```
callback(null, response)
```

L'objet `context` passé en tant que deuxième argument au handler contient des informations d'exécution que pour ce tutoriel nous n'avons pas besoin d'accéder. Nous devons cependant utiliser l'`event` passé en tant que premier argument car il contient la soumission du formulaire avec l'URL à raccourcir.

#### Parse the request

Voici un exemple d'un événement API Gateway qui sera passé à notre handler lorsqu'un utilisateur soumet un formulaire. Comme nous construisons notre raccourcisseur d'URL en tant qu'application monopage, nous allons soumettre le formulaire en utilisant JavaScript et donc le type de contenu sera `application/json` plutôt que `application/x-www-form-urlencoded`.

```
{     resource:'/',   path:'/',   httpMethod:'POST',   headers: {      Accept:'*/*',      'Accept-Encoding':'gzip, deflate',      'cache-control':'no-cache',      'CloudFront-Forwarded-Proto':'https',      'CloudFront-Is-Desktop-Viewer':'true',      'CloudFront-Is-Mobile-Viewer':'false',      'CloudFront-Is-SmartTV-Viewer':'false',      'CloudFront-Is-Tablet-Viewer':'false',      'CloudFront-Viewer-Country':'GB',      'content-type':'application/json',      Host:'',      'User-Agent':'',      'X-Amz-Cf-Id':'',      'X-Amzn-Trace-Id':'',      'X-Forwarded-For':'',      'X-Forwarded-Port':'443',      'X-Forwarded-Proto':'https'   },   queryStringParameters:null,   pathParameters:{},   stageVariables:null,   requestContext: {        path:'/dev',      accountId:'',      resourceId:'',      stage:'dev',      requestId:'',      identity:{           cognitoIdentityPoolId:null,         accountId:null,         cognitoIdentityId:null,         caller:null,         apiKey:'',         sourceIp:'',         accessKey:null,         cognitoAuthenticationType:null,         cognitoAuthenticationProvider:null,         userArn:null,         userAgent:'',         user:null      },      resourcePath:'/',      httpMethod:'POST',      apiId:''   },   body:'{"url":"http://example.com"}',   isBase64Encoded:false}
```

Nous avons seulement besoin de la soumission du formulaire de l'événement, que nous pouvons obtenir en regardant le `body` de la requête. Le corps de la requête est stocké sous forme d'objet JavaScript stringifié que nous pouvons récupérer à l'intérieur de notre handler en utilisant `JSON.parse()`. En tirant parti de [l'évaluation de court-circuit JavaScript](http://www.jstips.co/en/javascript/short-circuit-evaluation-in-js/), nous pouvons définir une valeur par défaut de chaîne vide pour les cas où une URL n'a pas été envoyée dans le cadre de la soumission du formulaire. Cela nous permet de traiter de la même manière les cas où l'URL est manquante et où l'URL est une chaîne vide.

```
module.exports.handle = (event, context, callback) => {  let longUrl = JSON.parse(event.body).url || ''}
```

#### Validate the URL

Ajoutons une validation de base pour vérifier que l'URL fournie semble légitime. Il existe plusieurs approches qui pourraient être adoptées pour y parvenir. Mais pour les besoins de ce tutoriel, nous allons garder cela simple et utiliser le module [Node.js URL](https://nodejs.org/api/url.html) intégré. Nous allons construire notre validation pour retourner une promesse résolue sur une URL valide et retourner une promesse rejetée sur une URL invalide. Les promesses en JavaScript peuvent être enchaînées séquentiellement de sorte que la résolution d'une promesse soit transmise au gestionnaire de succès de la suivante. Nous allons utiliser cet attribut des promesses pour structurer notre handler. Écrivons la fonction de validation en utilisant des promesses.

```
const url = require('url')
```

```
function validate (longUrl) {  if (longUrl === '') {    return Promise.reject({      statusCode: 400,      message: 'URL is required'    })  }
```

```
let parsedUrl = url.parse(longUrl)  if (parsedUrl.protocol === null || parsedUrl.host === null) {    return Promise.reject({      statusCode: 400,      message: 'URL is invalid'    })  }
```

```
return Promise.resolve(longUrl)}
```

Dans notre fonction `validate`, nous vérifions d'abord que l'URL n'est pas définie sur une chaîne vide. Si c'est le cas, nous retournons une promesse rejetée. Remarquez comment la valeur rejetée est un objet contenant un code de statut et un message. Nous allons utiliser cela plus tard pour construire une réponse API appropriée. Appeler `parse` sur le module `url` de Node.js retourne un objet URL avec des informations qui pourraient être extraites de l'URL qui a été passée en tant qu'argument de chaîne. Dans le cadre de notre validation d'URL de base, nous vérifions simplement si un protocole (par exemple, 'http') et un hôte (comme 'example.com') pourraient être extraits. Si l'une de ces valeurs est `null` sur l'objet URL retourné, nous supposons que l'URL est invalide. Si l'URL est valide, nous la retournons dans le cadre d'une promesse résolue.

#### Returning a response

Après avoir récupéré l'URL de la requête, nous appelons `validate` et pour chaque étape supplémentaire du handler qui est requise, nous retournerons une nouvelle promesse dans le gestionnaire de succès de la promesse précédente. Le dernier gestionnaire de succès est responsable du retour d'une réponse API via l'argument de rappel du handler. Il sera invoqué pour les réponses d'erreur de l'API générées à partir de promesses rejetées ainsi que pour les réponses d'API réussies.

```
module.exports.handle = (event, context, callback) => {  let longUrl = JSON.parse(event.body).url || ''  validate(longUrl)    .then(function(path) {      let response = buildResponse(200, 'success', path)      return Promise.resolve(response)    })    .catch(function(err) {      let response = buildResponse(err.statusCode, err.message)      return Promise.resolve(response)    })    .then(function(response) {      callback(null, response)    })}
```

```
function buildResponse (statusCode, message, path = false) {  let body = { message }  if (path) body['path'] = path    return {    headers: {      'Access-Control-Allow-Origin': '*'    },    statusCode: statusCode,    body: JSON.stringify(body)  }}
```

#### Generate a URL shortcode

L'API doit être capable de générer des codes courts d'URL uniques, qui sont représentés sous forme de noms de fichiers dans le bucket S3. Comme un code court est simplement un nom de fichier, il y a une grande flexibilité dans la manière dont il est composé. Pour notre code court, nous allons utiliser une chaîne alphanumérique de 7 caractères composée de caractères majuscules et minuscules, ce qui se traduit par 62 combinaisons possibles pour chaque caractère. Nous allons utiliser la récursivité pour construire le code court en sélectionnant un caractère à la fois jusqu'à ce que sept aient été sélectionnés.

```
function generatePath (path = '') {  let characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  let position = Math.floor(Math.random() * characters.length)  let character = characters.charAt(position)
```

```
if (path.length === 7) {  return path}
```

```
return generatePath(path + character)}
```

Bien que la probabilité de générer aléatoirement le même code court soit faible (il y a en fait une probabilité de 0,0000000000000000000000008063365516 que deux codes courts soient identiques), nous devons vérifier si le code court généré est déjà utilisé, ce que nous pouvons faire en utilisant le SDK AWS. Il existe une méthode `headObject` sur le service S3 qui charge les métadonnées d'un objet. Nous pouvons utiliser cela pour tester si un objet avec le même nom existe déjà, car lorsqu'un objet n'est pas trouvé, une promesse avec le code _NotFound_ est rejetée. Cette promesse rejetée indique que le code court est libre et peut être utilisé. Appeler `headObject` est plus performant que de tester si l'objet existe via `getObject`, qui charge l'objet entier.

```
const AWS = require('aws-sdk')const S3 = new AWS.S3()
```

```
function isPathFree (path) {  return S3.headObject(buildRedirect(path)).promise()    .then(() => Promise.resolve(false))    .catch(function (err) {      if (err.code == 'NotFound') {        return Promise.resolve(true)      } else {        return Promise.reject(err)      }    })}
```

```
function buildRedirect (path, longUrl = false) {  let redirect = {    'Bucket': config.BUCKET,    'Key': path  }
```

```
if (longUrl) {    redirect['WebsiteRedirectLocation'] = longUrl  }
```

```
return redirect}
```

Nous pouvons utiliser `isPathFree` pour trouver récursivement un chemin d'objet unique.

```
function getPath () {  return new Promise(function (resolve, reject) {    let path = generatePath()    isPathFree(path)      .then(function (isFree) {        return isFree ? resolve(path) : resolve(getPath())      })  })}
```

En tirant parti de la capacité à enchaîner les promesses, nous retournons une nouvelle invocation de `getPath` si `isPathFree` retourne false.

Pour sauvegarder un objet après qu'un code court unique a été trouvé, nous devons simplement appeler la méthode `putObject` sur le service S3 du SDK AWS. Enveloppons cela dans une fonction qui résout le code court si l'appel de la méthode `putObject` a réussi et retourne un objet d'erreur pour construire une réponse API s'il n'a pas réussi.

```
function saveRedirect (redirect) {  return S3.putObject(redirect).promise()    .then(() => Promise.resolve(redirect['Key']))    .catch(() => Promise.reject({      statusCode: 500,      message: 'Error saving redirect'  })}
```

En utilisant les fonctions ci-dessus, nous pouvons ajouter deux nouveaux gestionnaires de succès de promesse pour finaliser notre endpoint API. Nous devons retourner `getPath` à partir du premier gestionnaire de succès de promesse qui résoudra un code court d'URL unique. Retourner `saveRedirect` avec un objet de redirection construit en utilisant ce code court unique dans le deuxième gestionnaire de succès sauvegardera l'objet dans le bucket S3. Le chemin de cet objet peut ensuite être retourné au client dans le cadre d'une réponse API. Notre handler devrait maintenant être complet.

```
module.exports.handle = (event, context, callback) => {  let longUrl = JSON.parse(event.body).url || ''  validate(longUrl)    .then(function () {      return getPath()    })    .then(function (path) {      let redirect = buildRedirect(path, longUrl)      return saveRedirect(redirect)    })    .then(function (path) {      let response = buildResponse(200, 'success', path)      return Promise.resolve(response)    })    .catch(function (err) {      let response = buildResponse(err.statusCode, err.message)      return Promise.resolve(response)    })    .then(function (response) {      callback(null, response)    })}
```

#### Deploy the API

Exécutez `serverless deploy` dans votre terminal pour déployer l'API sur AWS. Cela configurera notre bucket S3 et retournera l'URL de l'endpoint. Gardez l'URL de l'endpoint à portée de main car nous en aurons besoin plus tard.

```
Serverless: Packaging service...Serverless: Excluding development dependencies...Serverless: Uploading CloudFormation file to S3...Serverless: Uploading artifacts...Serverless: Uploading service .zip file to S3 (5.44 MB)...Serverless: Validating template...Serverless: Updating Stack...Serverless: Checking Stack update progress.................Serverless: Stack update finished...Service Informationservice: serverless-url-shortenerstage: devregion: eu-west-1stack: serverless-url-shortener-devapi keys:  Noneendpoints:  POST - https://t2fgbcl26h.execute-api.eu-west-1.amazonaws.com/dev/functions:  store: serverless-url-shortener-dev-storeServerless: Removing old service versions...
```

### Creating the frontend

Pour aider à la conception du frontend, nous allons utiliser le [Framework PaperCSS](https://github.com/papercss/papercss). Nous allons également utiliser [jQuery](https://jquery.com/) pour simplifier le travail avec le DOM et les requêtes AJAX. Il est utile de noter que pour un environnement de production, vous voudriez probablement utiliser deux dépendances plus légères, mais comme il s'agit simplement d'un tutoriel, je pense que c'est acceptable.

Créez un dossier `static` pour que nous ayons un endroit où stocker notre code frontend.

#### Download the dependencies

Enregistrez une copie de [paper.min.css](https://github.com/papercss/papercss/releases/download/v1.3.1/paper.min.css) et [jquery-3.2.1.min.js](https://code.jquery.com/jquery-3.2.1.min.js) dans notre dossier `static` nouvellement créé, ce sont des versions minifiées du framework PaperCSS et de la bibliothèque jQuery respectivement.

#### Add the HTML

Créez un nouveau fichier appelé `index.html` à l'intérieur du dossier `static` et ajoutez le HTML requis. Nous avons besoin d'un formulaire avec une entrée d'URL et un bouton pour soumettre le formulaire. Nous avons également besoin d'un endroit où mettre le résultat de tout appel d'API, qui pour un appel d'API réussi serait l'URL raccourcie et pour un appel d'API infructueux, ce serait le message d'erreur.

```
<!DOCTYPE html><html lang="en"><head>  <meta charset="UTF-8">  <meta name=viewport content="width=device-width,initial-scale=1">  <title>Serverless url shortener</title>  <link href="paper.min.css" rel="stylesheet"></head><style>  * {    text-align: center;  }
```

```
  #message {    display: none;  }</style><body>  <div class="row flex-center">    <div class="col-8 col">      <h2>Serverless url shortener</h2>      <form action="">        <div class="form-group">          <label for="url">Enter URL to shorten</label>          <input             class="input-block"             name="url"             type="url"             id="url"              autocomplete="off"             required>        </div>        <div id="message" class="alert alert-primary"></div>        <input           class="paper-btn"           type="submit"           value="Shorten link">      </form>      <p class="padding-top">        <a href="https://git.io/vbS8I">          View this project on Github        </a>      </p>    </div>  </div></body></html>
```

Bien que non montré dans le bloc de code ci-dessus pour des raisons de brièveté, assurez-vous de définir l'action du formulaire sur l'endpoint de l'API qui a été affiché lorsque vous avez exécuté `serverless deploy`. Si vous n'avez plus accès à la sortie de votre terminal de ce déploiement, vous pouvez trouver l'URL de l'endpoint via la commande `serverless info`.

#### Make API requests

Avant d'écrire le JavaScript pour faire des requêtes à notre API, chargeons d'abord jQuery en ajoutant une balise de script juste avant `</body>` et en référençant le fichier minifié que nous avons téléchargé précédemment.

```
<script src="jquery-3.2.1.min.js"></script>
```

Ajoutez maintenant une autre paire de balises de script en dessous et à l'intérieur, créons une fonction qui peut être utilisée pour afficher un message à l'utilisateur en utilisant le `div` de message dans notre modèle qui est défini sur `display:none` par défaut au chargement de la page. Pour afficher un message, nous pouvons simplement définir le texte à l'intérieur de ce `div` en utilisant `text()` et basculer l'affichage en utilisant `show()`.

```
<script>  function addMessage (text) {    $('#message').text(text).show()  }</script>
```

Écrivons une autre fonction à placer dans le même ensemble de balises de script qui utilisera jQuery pour faire des requêtes à notre API.

```
function shortenLink (apiUrl, longUrl) {  $.ajax(apiUrl, {    type : 'POST',     data: JSON.stringify({url: longUrl})})    .done(function (responseJSON) {      var protocol = window.location.protocol + '//'      var host = window.location.host + '/'      var shortUrl = protocol + host + responseJSON.path      addMessage(shortUrl)    })    .fail(function (data) {      if (data.status === 400) {        addMessage(data.responseJSON.message)      } else {        addMessage('an unexpected error occurred')      }    })}
```

Cette fonction crée une requête POST et définit le corps de la requête sur un objet JSON contenant l'URL à raccourcir. Si la requête s'est terminée avec succès et qu'un code de statut HTTP 2XX a été retourné, elle récupère le code court de la clé `path` sur la réponse et construit une URL courte entièrement qualifiée à présenter à l'utilisateur en utilisant la fonction `addMessage` créée précédemment. Si la requête a échoué, un message d'erreur est affiché.

Enfin, nous pouvons relier cela à notre formulaire en ajoutant un gestionnaire de soumission. Nous obtenons l'URL de l'endpoint de l'API à partir de l'attribut d'action du formulaire et obtenons l'URL à raccourcir à partir de l'entrée de formulaire `url`.

```
$('form').submit(function (event) {  event.preventDefault()  addMessage('...')  shortenLink(event.target.action, event.target.url.value)})
```

#### Deploy the website

Pour le déploiement du site web, nous allons utiliser la commande `sync` de l'AWS CLI pour télécharger le contenu du dossier static vers notre bucket S3. Exécutez `aws s3 sync static s3://[bucket]` dans votre terminal, en remplaçant `[bucket]` par le nom de votre bucket choisi dans `config.json`. Après cela, vous devriez pouvoir vous rendre à l'adresse de votre bucket S3 dans un navigateur pour voir le raccourcisseur d'URL en action. Les URL publiques pour les buckets S3 prennent la forme suivante.

```
http://[bucket].s3-website-[region].amazonaws.com
```

Ainsi, après avoir ajouté le nom de votre bucket et votre région, l'adresse de votre raccourcisseur d'URL devrait ressembler à celle ci-dessous.

```
http://serverless-url-shortener.s3-website-eu-west-1.amazonaws.com
```

Pour ajouter un domaine personnalisé à votre bucket, vous devriez suivre l'une des instructions de [cet article de support AWS](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html). Pour l'option la plus facile, vous devriez définir le nom du bucket sur le sous-domaine `www` de votre domaine (par exemple www.example.com). Si vous ajoutez ensuite un enregistrement CNAME dans votre configuration DNS pour le sous-domaine `www` et le définissez sur l'adresse de votre bucket S3, le site web devrait être accessible via votre domaine. Assurez-vous également de supprimer tous les enregistrements `A` existants et gardez à l'esprit que cela ne configurera pas de redirection de votre domaine racine vers le sous-domaine `www`. Il existe quelques façons de résoudre ce problème qui sont décrites dans l'article AWS.

### Wrap up

J'espère que vous avez trouvé ce tutoriel utile. La réalité est qu'AWS est incroyablement flexible et dans cet article, nous avons passé en revue une seule façon de créer un raccourcisseur d'URL en utilisant Lambda et S3. Mais il existe une variété d'autres façons dont le même processus aurait également pu être accompli.

Si vous avez trouvé cela intéressant, vous pourriez apprécier [un de mes articles précédents](https://hackernoon.com/creating-a-form-forwarding-service-for-aws-lambda-aec07af9f951) où j'ai créé un service de transfert de formulaire en utilisant AWS Lambda.

[**Présentation de Formplug v1, un service de transfert de formulaire pour AWS Lambda**](https://hackernoon.com/introducing-formplug-v1-a-form-forwarding-service-for-aws-lambda-2c125dfe608e)  
[_Il est estimé qu'environ 269 milliards d'e-mails sont envoyés en une seule journée. Plus de 10 millions ont été envoyés pendant que vous lisiez..._hackernoon.com](https://hackernoon.com/introducing-formplug-v1-a-form-forwarding-service-for-aws-lambda-2c125dfe608e)