---
title: Comment construire une API avec Lambdas et API Gateway
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T20:39:01.000Z'
originalURL: https://freecodecamp.org/news/building-an-api-with-lambdas-and-api-gateway-11254e23b703
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VjGHQOLK4sJDqYvzTkx30g.png
tags:
- name: api
  slug: api
- name: aws lambda
  slug: aws-lambda
- name: Movies
  slug: movies
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment construire une API avec Lambdas et API Gateway
seo_desc: 'By Sam Williams

  Do you want to access your database, control your system, or execute some code from
  another website? An API can do all of this for you, and they’re surprisingly easy
  to set up.

  An API is a URL that you can perform GET, PUT, POST, and ...'
---

Par Sam Williams

Souhaitez-vous accéder à votre base de données, contrôler votre système ou exécuter du code depuis un autre site web ? Une API peut tout faire pour vous, et elles sont surprenamment faciles à configurer.

Une API est une URL sur laquelle vous pouvez effectuer des requêtes `GET`, `PUT`, `POST` et `DELETE` pour contrôler un autre service. Si vous en créez une vous-même, vous pouvez alors construire ces API pour faire ce que vous voulez en arrière-plan. Les utilisations courantes sont le contrôle de la base de données, l'exécution d'actions sur des API tierces (API-ception) ou le contrôle d'un autre service.

%[https://www.youtube.com/watch?v=4_WI8ZGIcXY]

### Pourquoi utiliser une API ?

Vous pouvez vous demander pourquoi nous avons besoin d'une API alors que nous pouvons accéder directement à la base de données ou exécuter le code sur le site web. Il y a quelques avantages majeurs à utiliser des API plutôt que d'exécuter le code dans votre site web.

#### Masquez vos clés d'accès et jetons

C'est peut-être la **raison la plus importante** d'utiliser une API. Si vous accédez à une base de données, vous aurez besoin des détails de la base de données ainsi que des données d'utilisateur et de jeton/clé d'accès.

Si vous accédez à la base de données depuis le site web, vous aurez tous ces détails dans le code source de votre site. C'est une **très mauvaise pratique**, car n'importe qui peut regarder dans le contrôle de source et voler vos détails. Cela ne semble pas trop grave, mais que se passe-t-il si ce sont vos identifiants AWS ou Google Cloud Compute ? Les personnes accédant à votre site pourraient alors les utiliser pour exécuter ce qu'ils veulent sur votre compte, vous laissant avec une énorme facture.

Exécuter ces processus derrière une API signifie que personne ne peut voir les détails privés — ils ne peuvent pas les voler pour les utiliser dans leurs propres projets. Si vous stockez le code de votre site web dans GitHub ou un autre contrôle de source public, cela signifie également qu'ils ne sont pas visibles là non plus.

#### Exécutez le code ailleurs

Et si vous n'utilisez aucun autre service et n'utilisez aucune clé secrète ? Si vous exécutez un grand ou complexe morceau de code, ou si vous ne voulez pas que quelqu'un d'autre lise votre code et découvre comment il fonctionne, vous pouvez toujours utiliser une API.

#### Contrôlez qui a accès

![Image](https://cdn-media-1.freecodecamp.org/images/mobDuXc3Fnbib2-rOnW7ZOY4n7HMm8iUqOhq)
_[Porte fermée verte verrouillée](https://www.pexels.com/photo/door-green-closed-lock-4291/" rel="noopener" target="_blank" title=")._

Fournir une API vous permet également de restreindre qui peut accéder à la base de données ou exécuter le code. Vous pouvez le faire en exigeant une clé API. Cette clé est utilisée pour identifier l'utilisateur faisant la requête, puis pour autoriser ou rejeter la requête.

Cela peut être utilisé pour permettre à seulement quelques personnes d'accéder au service, ou même pour créer un système à niveaux. C'est ainsi que fonctionnent de nombreuses API payantes. Tout le monde a un accès gratuit mais limité, puis vous autorisez le paiement pour accéder à des parties supérieures du service ou simplement à un taux de requêtes plus élevé.

### Construction de l'API

Maintenant que nous connaissons quelques raisons pour lesquelles nous pourrions vouloir créer une API, faisons exactement cela. Nous allons utiliser API Gateway et AWS Lambdas, car c'est plus simple que de faire fonctionner un serveur. Assurez-vous d'avoir un compte AWS et d'être connecté.

#### Configuration d'une API Gateway

Nous allons commencer par ouvrir le service API Gateway et cliquer sur "Commencer". Sur la page suivante, nous devons sélectionner l'option "Nouvelle API". Ensuite, nous donnerons un nom et une description à notre API, et cliquerons sur "Créer une API".

![Image](https://cdn-media-1.freecodecamp.org/images/V3XpqCcqXz7t2yywu6dOwQK8Lfhhdhl9TCdx)

Cliquer sur "Créer une API" nous amène à la page de configuration de l'API.

La première chose que nous devons faire est d'ajouter une ressource à l'API. L'utilisation de ressources nous permet de regrouper des appels API similaires en utilisant des barres obliques imbriquées. Nous allons créer une API que nous pouvons utiliser pour faire des recommandations sur ce qu'il faut regarder. Par conséquent, nous pouvons avoir `/emissions-tv` et `/films` comme deux méthodes de base.

Cliquez sur le menu déroulant "Actions" et sélectionnez "Créer une ressource". Nommez vos ressources, en veillant à ce qu'elles soient toutes les deux dans le chemin "/".

![Image](https://cdn-media-1.freecodecamp.org/images/pUpkZpJGX095a02J0Wx3GuSGO1khay6YVogm)

![Image](https://cdn-media-1.freecodecamp.org/images/RZpG3Q2QcVqjG4k8lUfemrEKEFR-3Aa5RHJw)

Nous voulons que les utilisateurs puissent aller à "/films/horreur" ou "/emissions-tv/comedie", et nous pouvons le faire en ajoutant des paramètres de chemin. Ce sont des variables auxquelles nous pouvons accéder à l'intérieur de l'API. Pour créer l'un de ceux-ci, nous devons définir la ressource sur `{nomRessource}` comme montré ci-dessous. Cela peut être fait pour "emissions-tv" et "films".

![Image](https://cdn-media-1.freecodecamp.org/images/Y09YGFKPy2bamMfzHjWqJCsLOchP3NyLBTKs)

Maintenant que nous avons la longueur et le genre, nous pouvons créer des méthodes pour obtenir et ajouter des données à une table. Sélectionnez l'une des ressources `{genre}`, cliquez sur "Actions", puis sur "Créer une méthode". Cela créera une petite boîte grise sous la ressource sur laquelle nous pouvons cliquer. Nous allons commencer par une requête `GET`, alors sélectionnez celle-ci et cliquez sur le bouton de validation.

C'est ici que nous décidons comment gérer la requête. Nous allons utiliser AWS Lambdas, mais nous devons les créer avant de pouvoir terminer la configuration des méthodes.

#### Création des Lambdas

Nous sommes en mesure de répondre à ces requêtes API en utilisant des Lambdas, ce qui est génial car elles ne s'exécutent que lorsque nous en avons besoin. Elles sont également très faciles à créer, c'est donc ce que nous allons faire maintenant.

Dans la console Lambda, cliquez sur "Créer une fonction". Ensuite, nous pouvons nommer notre première fonction API `movieAPI`, la configurer pour qu'elle s'exécute sur Node 8.10, et "Créer un nouveau rôle à partir de modèle(s)". Nous nommerons notre nouveau rôle "tableAPI" et ajouterons "Autorisations de microservice simple" comme seul modèle.

Tout le code peut être trouvé à [https://github.com/SamWSoftware/Projects/tree/master/movieAPI](https://github.com/SamWSoftware/Projects/tree/master/movieAPI)

Cliquer sur "Créer une fonction" nous enverra dans la fenêtre Lambda. Faites défiler vers le bas jusqu'à la section "Code de la fonction" et nous changerons le code. La première chose que nous allons faire est de vérifier quelle méthode de requête a été utilisée.

```js
exports.handler = async (event) => {
    console.log(event);
    if (event.httpMethod === 'PUT'){
        let response = putMovie(event)
        return done(response);
    } else if (event.httpMethod === 'GET'){
        let response = getMovie(event);
        return done(response);
    }
};
```

Nous allons commencer par écrire la fonction `getMovie`. Cette fonction commencera par obtenir le `genre` à partir des paramètres de chemin. C'est là que l'utilisation des paramètres de chemin peut rendre ce processus facile.

```js
const getMovie = event => {
    let genre = event.pathParameters.genre;
    return;
}
```

Avec le genre que l'utilisateur a demandé, nous allons obtenir un film recommandé pour lui. J'ai copié ceux-ci depuis [25 Top Films From Each Genre](https://www.imdb.com/list/ls000441429/) et je les ai ajoutés à un objet avec le genre comme clé. Nous pouvons ensuite obtenir le film en obtenant la valeur du genre demandé.

```js
const movies = {
    action: 'Desperado (1995)',
    fantasy: 'Inception (2010)',
    ...
    horror: 'Black Swan (2010)'
}

const getMovie = event => {
    let genre = event.pathParameters.genre;
    return movies[genre];
}
```

Cela signifie que le titre du film est transmis à la fonction `done`. Cette fonction est utilisée, car API Gateway attend que les données reviennent dans un format très spécifique. Cette fonction transforme une chaîne de caractères dans ce format requis.

```js
const done = response => {
    return {
        statusCode: '200',
        body: JSON.stringify(response),
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
        }
    }
}
```

Nous pouvons faire quelque chose de très similaire pour une fonction `tv-showsAPI`, en réutilisant la plupart du code. Il suffit de changer les noms de fonction et les suggestions de films en émissions de télévision.

#### Connexion des Lambdas à API Gateway

De retour dans API Gateway, nous pouvons ajouter nos nouveaux Lambdas aux méthodes que nous avons créées précédemment. Nous devons nous assurer que "Utiliser l'intégration Lambda Proxy" est sélectionné et que nous pointons vers le bon Lambda. Cliquer sur "Enregistrer" vous demandera des autorisations pour accéder à ce Lambda, auxquelles nous pouvons donner "OK".

![Image](https://cdn-media-1.freecodecamp.org/images/XBHJhtze5MscnYcFHruORyPAtD93M26anNO9)

Faites cela pour les méthodes `GET` sur les deux ressources et nous pouvons commencer à tester. La sélection des méthodes devrait maintenant montrer un diagramme d'exécution de la méthode. Cela semble compliqué, mais la seule partie dont nous avons besoin est la section "TEST".

Cliquer sur "TEST" ouvrira une nouvelle section où nous pouvons essayer l'API. Il y a beaucoup de choses que vous pouvez configurer ici, mais la seule qui nous intéresse est `Path {genre}`. Nous devons définir cela sur le genre que nous demandons. Entrer "western" comme genre et appuyer sur le bouton "Test" donne une réponse comme celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/i34jkqAn9b7XhoR6nAr2kpeuGCMX5gGbXbjA)

Nous avons fait fonctionner notre API ! Maintenant, nous devons nous assurer que d'autres personnes peuvent y accéder. Il y a deux étapes pour cela.

1. Nous activons CORS — Sélectionnez la ressource "{genre}" puis cliquez sur "Actions" et "Activer CORS". Laissez tout par défaut et, lorsque demandé, cliquez sur "Oui, remplacer les valeurs existantes".
2. Déployez notre API — Cliquez sur "Actions" et "Déployer l'API". Définissez l'étape de déploiement sur "[Nouvelle étape]" puis donnez un nom à votre étape comme "production" ou "public".

Une fois votre API déployée, vous devriez obtenir une URL comme celle-ci. C'est la base de votre API. Vous pouvez ajouter `/films/western` pour accéder à votre API.

```js
https://{uniqueCode}.execute-api.eu-west-1.amazonaws.com/production
```

Votre URL d'API pourrait ressembler à ceci :

```
https://fds1fe31fes476s.execute-api.eu-west-1.amazonaws.com/production/films/western
```

C'est tout pour cet article. Dans le suivant, nous connecterons cette API à des tables Dynamo et permettrons aux utilisateurs de voter pour leurs films préférés dans chaque genre. Vous pouvez lire cet article ci-dessous.

[**Construction d'une API avec Lambdas et API Gateway — Partie 2**](https://medium.com/@samwsoftware/building-an-api-with-lambdas-and-api-gateway-part-2-7c674a0eb121)  
[_Dans la première partie, nous avons créé une API qui transmettait les requêtes à un Lambda qui retournait la meilleure émission de télévision ou le meilleur film..._](https://medium.com/@samwsoftware/building-an-api-with-lambdas-and-api-gateway-part-2-7c674a0eb121)  
[medium.com](https://medium.com/@samwsoftware/building-an-api-with-lambdas-and-api-gateway-part-2-7c674a0eb121)