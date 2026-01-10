---
title: 'Webtask Backend-as-a-Service : Tutoriel rapide sur le serverless'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-02T19:04:00.000Z'
originalURL: https://freecodecamp.org/news/webtask-backend-as-a-service-quick-serverless-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca977740569d1a4ca84d3.jpg
tags: []
seo_title: 'Webtask Backend-as-a-Service : Tutoriel rapide sur le serverless'
seo_desc: 'By Charles Ouellet

  The word serverless is buzzing through dozens of dev circles today.

  It has been for a while now.

  I’ve been meaning to exit my code editor and come talk about the trend here. Especially
  since I discovered Webtask, a few months ago.

  ...'
---

### Par Charles Ouellet

Le mot **serverless** fait le buzz dans des dizaines de cercles de développeurs aujourd'hui.

Cela fait un moment déjà.

J'avais l'intention de quitter mon éditeur de code et de venir parler de cette tendance ici. Surtout depuis que j'ai découvert [Webtask](https://webtask.io/), il y a quelques mois.

Alors, entre les corrections de bugs, le support et les nouvelles fonctionnalités, j'ai finalement pris le temps de m'asseoir et d'écrire un peu.

Dans cet article, je vais aborder un peu les architectures serverless et les outils Backend as a Service. Mais je vais surtout me concentrer sur l'offre d'un tutoriel simple mais significatif sur le e-commerce serverless. Et je vais utiliser notre propre plateforme de panier d'achat HTML/JS et Webtask pour ce faire.

## Qu'est-ce qu'une architecture serverless, et pourquoi devriez-vous vous en soucier ?

Comme [le "JAMstack"](https://snipcart.com/blog/jamstack-clients-static-site-cms), **l'architecture serverless** est une nouvelle tendance de développement web qui souscrit au paradigme de "l'essor du frontend" dans lequel nous nous trouvons. En termes simples, c'est une façon d'exécuter du code côté serveur dans le cloud sans se soucier des serveurs web, du routage, etc. Elle repose fortement sur des tiers **Backend as a Service (BaaS)** tels que Webtask, ou l'enfant chéri du moment : [AWS Lambda](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html). Avec ces services BaaS, vous écrivez simplement du code et les laissez gérer toute l'infrastructure sous-jacente. En termes de scalabilité, une telle approche est assez géniale : la couche d'abstraction que ces services offrent peut gérer les pics de trafic sur votre site de manière merveilleuse.

Comme vous le savez peut-être, nous sommes de grands fans de [JAMstack](http://jamstack.org/) (JavaScript, APIs & Markup) ici chez Snipcart. C'est une autre expression vibrante du paradigme de "l'essor du frontend" que j'ai mentionné. Nous avons écrit des tutoriels complets sur la façon de gérer le e-commerce avec des générateurs de sites statiques tels que [Jekyll](https://snipcart.com/blog/static-site-e-commerce-part-2-integrating-snipcart-with-jekyll) ou [Hugo](https://snipcart.com/blog/hugo-tutorial-static-site-ecommerce), et même avec des [CMS API-first comme Contentful](https://www.contentful.com/blog/2016/02/10/snipcart-middleman-contentful/). Du coût aux changements de stacks technologiques, je crois qu'une telle approche aura un impact profond sur la façon dont les entreprises gèrent le développement web dans les années à venir.

Cependant, je suis conscient que cela a ses limites : un site statique moderne est du **contenu brut**, ce qui signifie que l'utilisation de fonctionnalités dynamiques telles que les webhooks serait impossible sans _un peu_ de code côté serveur. C'est là que Webtask entre en jeu.

## Webtask : Backend-as-a-Service pour des tâches ciblées (ou FaaS)

Webtask est un service pratique conçu par [Auth0](https://auth0.com/), les bonnes personnes qui ont fait une sérieuse percée dans le monde de l'authentification en ligne. Agissant comme une Function as a Service, il élimine essentiellement le besoin de configurer un backend pour des applications mobiles simples ou des applications à page unique. Souvent [comparé à AWS Lambda](http://thenewstack.io/often-choose-webtask-lambda/), il permet aux développeurs d'écrire une logique côté serveur et des fonctions exécutées via des appels HTTP. C'est donc l'un des meilleurs outils Backend as a Service pour les développeurs qui préfèrent se concentrer sur le frontend plutôt que de configurer le backend.

Maintenant, voyons à quel point il est parfait pour le cas d'utilisation que nous allons explorer dans ce tutoriel serverless.

## Tutoriel sur le e-commerce serverless : webhooks et tarifs d'expédition personnalisés

Chez Snipcart, je crois que l'une de nos fonctionnalités les plus puissantes est [l'API de livraison par Webhooks](https://docs.snipcart.com/configuration/shipping-providers#webhooks-shipping-api). En termes simples, elle vous donne un contrôle total sur la façon dont votre site de e-commerce gère la livraison.

Cependant, l'utilisation de cette fonctionnalité nécessite l'exécution de code côté serveur. Donc, si vous vouliez utiliser une configuration JAMstack avec un générateur de site statique, vous seriez coincé. Grâce à Webtask, cependant, vous ne l'êtes pas ! Dans ce tutoriel serverless, nous allons l'utiliser pour héberger la fonction de livraison e-commerce dont nous avons besoin directement via leur plateforme.

## Notre cas d'utilisation simple de e-commerce serverless

Maintenant, imaginons que nous avons un site de e-commerce statique fonctionnant avec Snipcart.

Et disons que nous voulons offrir trois tarifs d'expédition spéciaux :

* Un pour les clients de notre ville natale du Québec
* Un pour les clients américains
* Un pour tous les autres clients internationaux

## 1. Comment créer la fonction Webtask

Tout d'abord, laissez-moi expliquer un peu comment fonctionne notre API de livraison. Snipcart envoie tous les détails de la commande à une URL que vous pouvez spécifier dans votre tableau de bord marchand. En utilisant ces données, vous pouvez ensuite écrire du code pour retourner les tarifs d'expédition disponibles à vos clients finaux.

**Commencez par créer un compte sur** [**https://webtask.io/.**](https://webtask.io/) **Une fois cela fait, suivez leurs étapes pour installer le CLI Webtask via** `**npm**`**.**

Nous allons maintenant créer un fichier nommé `shipping_task.js`. Il contiendra tout le code nécessaire pour analyser les détails de la commande reçus de Snipcart et retourner les tarifs d'expédition disponibles.

Commençons par exporter un module que Webtask comprendra.

```javascript
module.exports = function (context, cb) {
    cb(null, context.body);
}
```

Le premier paramètre, context, contient les données que Snipcart enverra à votre application. Webtask se charge d'analyser le JSON, et vous pouvez accéder à tous les détails de l'événement ainsi qu'à la commande via context.body.

Avec le code ci-dessus, notre tâche retournerait le corps de la requête qu'elle a reçue ; assez inutile. ;)

Maintenant, disons que nous voulons offrir la livraison gratuite pour les clients du Québec.

```javascript
module.exports = function (context, cb) {
    var orderDetails = context.body.content;
    var rates = [];
    
    var address = orderDetails.shippingAddress || order.billingAddress;
    
    if (address.country == "CA" && address.province == "QC") {
      rates.push({
        cost: 0,
        description: "Livraison gratuite pour les résidents du Québec !"
      });
    }
    
    cb(null, { rates: rates });
}
```

Ce n'est pas mal, n'est-ce pas ? Cependant, avec ce code, les clients en dehors du Québec n'auront aucune option d'expédition. Nous allons donc nous assurer de retourner un tarif d'expédition standard au cas où la commande ne correspondrait pas à nos conditions :

```javascript
if (rates.length === 0) {
  rates.push({
    cost: 20,
    description: "Livraison standard"
  });  
}
```

Vous pouvez voir ci-dessous le code complet avec quelques conditions supplémentaires :

```javascript
module.exports = function (context, cb) {
    console.log(context.body);

    var orderDetails = context.body.content;

    var rates = [];

    var address = orderDetails.shippingAddress || order.billingAddress;

    if (address.country == "CA" && address.province == "QC") {
      rates.push({
        cost: 0,
        description: "Livraison gratuite pour les résidents du Québec !"
      });
    }

    if (address.country == "CA" && address.province != "QC") {
      rates.push({
        cost: 10,
        description: "Livraison au Canada"
      });
    }

    if (address.country == "US") {
      rates.push({
        cost: 15,
        description: "Livraison aux États-Unis"
      });
    }

    if (rates.length === 0) {
      rates.push({
        cost: 20,
        description: "Livraison standard"
      });
    }

    cb(null, { rates: rates });
}
```

Webtask générera ensuite une URL ; vous devriez la voir dans votre terminal.

Il suffit d'utiliser cette URL lors de la configuration de l'API de livraison par Webhooks.

#### 2. Sécuriser le composant serverless

Avec notre configuration actuelle, n'importe qui pourrait envoyer des requêtes à cette API, n'est-ce pas ? Ce n'est pas quelque chose que nous voulons. Nous allons donc nous assurer que la fonction ne traite que les requêtes provenant de Snipcart. Nous allons utiliser notre API de validation de requête pour ce faire.

Tout d'abord, nous devons envoyer une clé secrète de l'API Snipcart à la tâche afin d'appeler l'API de validation de requête. Nous ne voulons pas l'exposer directement via le code, donc nous allons utiliser la fonctionnalité `secrets` que Webtask possède. Elle nous permet de passer des paramètres secrets à la tâche qui seront chiffrés et accessibles via l'objet `context`.

Lors de la création de la tâche, j'ai ajouté l'option `--secret` :

```javascript
wt create shipping_task.js --secret snipcartApiKey=MY_SECRET_API_KEY
```

Vous pourrez alors accéder à cette valeur en utilisant `context.secrets.snipcartApiKey`. Nous allons également utiliser le module `request`, donc nous devons l'inclure au début du fichier :

```javascript
var request = require('request');

```

Lorsque nous faisons des requêtes à vos Webhooks, nous incluons toujours un jeton de requête dans les en-têtes de la requête. L'en-tête est nommé `X-Snipcart-RequestToken`. Nous y accéderons à nouveau via notre objet `context` :

```javascript
var requestToken = context.headers['x-snipcart-requesttoken'];
```

_Veuillez noter que tous les en-têtes sont en minuscules avec Webtask._

Voici les options que nous allons utiliser pour envoyer la requête à notre API :

```javascript
var requestToken = context.headers['x-snipcart-requesttoken'];
var secretApiKey = context.secrets.snipcartApiKey;

var requestOptions = {
  url: 'https://app.snipcart.com/api/requestvalidation/' + requestToken,
  headers: {
    "Accept": "application/json"
  },
  auth: {
    user: secretApiKey
  }
};
```

Nous allons exécuter cette requête et n'exécuter le code dans le callback que si elle est réussie.

```javascript
request(requestOptions, function(error, response, body) {
  if (response.statusCode === 200) {
      // Retourner les tarifs
  } else {
    // Retourner une erreur lorsque la requête ne provient pas de Snipcart.    
    cb("Seul Snipcart peut appeler ce code !");
  }
});
```

Donc, ma fonction complète ressemble maintenant à ceci :

```javascript
var request = require('request');

module.exports = function (context, cb) {
  var requestToken = context.headers['x-snipcart-requesttoken'];
  var secretApiKey = context.secrets.snipcartApiKey;

  var requestOptions = {
    url: 'https://app.snipcart.com/api/requestvalidation/' + requestToken,
    headers: {
      "Accept": "application/json"
    },
    auth: {
      user: secretApiKey
    }
  };

  request(requestOptions, function(error, response, body) {
    if (response.statusCode === 200) {
      var orderDetails = context.body.content;
      var rates = [];

      var address = orderDetails.shippingAddress || order.billingAddress;

      if (address.country == "CA" && address.province == "QC") {
        rates.push({
          cost: 0,
          description: "Livraison gratuite pour les résidents du Québec !"
        });
      }

      if (address.country == "CA" && address.province != "QC") {
        rates.push({
          cost: 10,
          description: "Livraison au Canada"
        });
      }

      if (address.country == "US") {
        rates.push({
          cost: 15,
          description: "Livraison aux États-Unis"
        });
      }

      if (rates.length === 0) {
        rates.push({
          cost: 20,
          description: "Livraison standard"
        });
      }

      cb(null, { rates: rates });
    }
    else {
      cb("Seul Snipcart peut appeler ce code !");
    }
  });
}
```

#### Mots de la fin sur Webtask et l'approche serverless

La création de cette petite fonction Webtask pour un site statique utilisant Snipcart m'a pris moins de deux heures. Bien sûr, nous aurions pu nous concentrer sur d'autres fonctions de e-commerce : gérer les webhooks pour faire le pont entre Snipcart et des systèmes de comptabilité externes, automatiser la livraison de biens numériques, et plus encore.

Je crois vraiment qu'il existe des tonnes de cas d'utilisation serverless passionnants que les développeurs devraient essayer de gérer avec Webtask d'Auth0. Toute intégration avec une API, ou la délégation de travaux plus longs/consommant plus de CPU aurait beaucoup de sens !

L'approche serverless est sur le point d'avoir un impact assez important sur notre travail en tant que développeurs. Comme nous le voyons maintenant avec les APIs RESTful, de nombreux services commenceront à dépendre de fonctions développées ou hébergées par d'autres. Le futur proche apportera de plus en plus de microservices hébergés dans des environnements comme Webtask et AWS Lambda. Surtout couplé avec l'essor de [frameworks comme Vue](https://snipcart.com/blog/vue-js-seo-prerender-example) et le JAMstack.

J'espère donc sincèrement que cet article inspire les développeurs à tirer parti de la puissance FaaS de Webtask sur différents projets serverless, e-commerce ou non. Et bien sûr, je serais plus qu'intéressé à jeter un coup d'œil à [de telles configurations](https://snipcart.com/blog/sell-event-tickets-website). Vous pouvez nous envoyer un email à geeks@snipcart.com si vous avez quelque chose de similaire à partager, ou si vous avez des questions concernant cette approche !

Aimez l'article ? Prenez une seconde pour ? et [_le partager sur Twitter_](https://twitter.com/home?status=Using%20%40auth0%27s%20%40webtaskio%20FaaS%20on%20a%20%23serverless%20e-commerce%20tutorial%20http%3A//bit.ly/2e5vm8d%20%23webtask)_!_

_Originalement publié sur le_ [_blog de Snipcart_](https://snipcart.com/blog/webtask-baas-serverless-tutorial) _et dans_ [_notre newsletter_](https://us5.list-manage.com/subscribe?u=c019ca88eb8179b7ffc41b12c&id=3e16e05ea2)_._