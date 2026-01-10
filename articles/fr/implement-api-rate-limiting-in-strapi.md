---
title: Comment implémenter la limitation de débit d'API dans Strapi CMS
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-09-10T14:18:17.105Z'
originalURL: https://freecodecamp.org/news/implement-api-rate-limiting-in-strapi
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725233479497/7c12e6e4-a6d7-433a-b23b-f25c33037ffa.jpeg
tags:
- name: api
  slug: api
seo_title: Comment implémenter la limitation de débit d'API dans Strapi CMS
seo_desc: 'Implementing rate limiting in web applications is a necessary web development
  best practice. In an article published earlier, I delved deep into the benefits
  and real life use cases of API rate limiting.

  Some of the benefits include its use by develo...'
---

L'implémentation de la limitation de débit (rate limiting) dans les applications web est une meilleure pratique nécessaire du développement web. Dans un [article](https://www.freecodecamp.org/news/what-is-rate-limiting-web-apis/) publié précédemment, j'ai approfondi les avantages et les cas d'utilisation réels de la limitation de débit d'API.

Certains des avantages incluent son utilisation par les développeurs pour restreindre l'accès malveillant aux sites web, prévenir les attaques DDoS, conserver les ressources du site web et assurer une performance optimale du serveur web.

Cet article couvre les aspects pratiques de l'implémentation des limites de débit dans une application Strapi en utilisant plusieurs packages et techniques.

Commençons.

## Table des matières

* [Projet de démonstration](#heading-projet-de-demonstration)
    
* [Koa Rate Limiter](#heading-koa2-rate-limit)
    
* [Limiteur de débit d'API Strapi personnalisé](#heading-limiteur-de-debit-dapi-strapi-personnalise)
    
* [Implémentation de Express-rate-limiter](#heading-implementation-de-express-rate-limiter)
    
* [Conclusion](#heading-conclusion)
    

## Projet de démonstration

Nous allons construire un site e-commerce en utilisant [Strapi](https://strapi.io/) comme Framework backend. Nous configurerons ensuite un limiteur de débit dans notre application Strapi pour aider à garantir la sécurité de notre backend. Postman servira d'outil pour tester les points de terminaison (endpoints) de l'API. Créons maintenant une application Strapi par défaut.

Pour créer une application Strapi, saisissez `npx create-strapi-app@latest {nom du projet}` dans la ligne de commande et suivez les instructions fournies. Pour rendre l'installation plus simple, choisissez la méthode d'installation *quick start* et votre application devrait être prête.

Cette modalité d'installation configure automatiquement une base de données SQLite facile à utiliser. Cependant, vous pouvez choisir d'utiliser n'importe quelle autre base de données SQL supportée par Strapi.

Alternativement, vous pouvez télécharger le dépôt de démarrage pour le projet [ici](https://github.com/oluwatobi2001/Strapi-default) et installer les dépendances nécessaires via `npm install`. Par la suite, vous pouvez exécuter l'application Strapi en naviguant vers le dossier du code de l'application Strapi dans la ligne de commande et lancer `npm run develop`.

![Configuration Strapi](https://hackmd.io/_uploads/BkRn2PqrR.png align="left")

Une fois l'exécution réussie, vous recevrez le lien vers l'adresse localhost pour personnaliser l'application.

![Lancement Strapi](https://hackmd.io/_uploads/SkkSavcS0.png align="left")

La navigation vers le lien vous demandera de créer un e-mail et un mot de passe d'administrateur. La réussite de cette étape vous donnera accès au tableau de bord (dashboard) backend.

![Interface de connexion Strapi](https://hackmd.io/_uploads/S1Vqxd5B0.png align="left")

You pouvez utiliser l'interface utilisateur du tableau de bord Strapi pour créer des API, ou vous pouvez générer une API en utilisant `npm generate`. Les API créées seront utilisées pour terminer la configuration de la fonctionnalité de limitation de débit. Nous allons créer un magasin de produits pour notre site e-commerce. Pour configurer facilement les produits, veuillez naviguer vers l'onglet Content-Type builder dans la barre latérale.

![Tableau de bord Strapi](https://hackmd.io/_uploads/r1RzbO5BC.png align="left")

Le gestionnaire Content-Type builder vous permet de créer diverses collections qui seront utiles lors de la configuration de vos API. Dans ce cas, les collections produit (product) et catégorie (category) seront créées pour vous permettre de configurer vos catalogues de produits.

![Création d'un endpoint de catégorie](https://hackmd.io/_uploads/B16rbu5rA.png align="left")

![Création d'une entrée de produit](https://hackmd.io/_uploads/SJhdb_qSR.png align="left")

Après avoir terminé la création des types de collection, vous pouvez facilement ajouter vos produits de manière transparente dans la base de données backend. Dans mon cas, j'ai créé des produits de marques de téléphones à vendre.

![Démo de création de produit](https://hackmd.io/_uploads/HyR9JT6fR.jpg align="left")

Il est également important de noter que les collections que nous avons créées dans le tableau de bord Strapi créent automatiquement un dossier API pour nous au sein de notre base de code. Nous travaillerons ensuite sur la base de code du projet.

La prochaine étape de ce tutoriel consiste à configurer un limiteur de débit efficace pour nos API Strapi créées dans le dépôt en utilisant les outils présentés ci-dessus.

## koa2-rate-limit

Dans cette section, nous utiliserons le package koa2-rate-limit pour construire le limiteur de débit de notre projet. Pour installer le package, naviguez vers le dossier de votre projet dans la ligne de commande et exécutez `npm i koa2-rate-limit`. Une fois l'installation réussie, naviguez vers le sous-dossier middleware à l'intérieur du dossier API et créez un fichier de code. Pour faciliter l'intégration, nommez-le **rateLimit.js**.

Après cela, dans le fichier de limitation de débit, importez et initialisez le package koa2-rate-limit.

```javascript
const RateLimit = require("koa2-ratelimit").RateLimit;
```

Ensuite, nous pouvons configurer le limiteur de débit Koa sur un intervalle de temps spécifié et le nombre total de requêtes.

```javascript
module.exports = (config, { strapi }) => {
  // Configuration du middleware du limiteur de débit
  const limiter = RateLimit.middleware({
    interval: { min: 1 }, // Fenêtre de temps en minutes
    max: 3, // Nombre maximum de requêtes par intervalle
 });
```

Dans le code ci-dessus, le middleware du limiteur de débit a été invoqué et l'intervalle de temps dans lequel la limite de débit s'applique a été fixé à 1 minute. Le nombre maximum de requêtes (max) a été fixé à 3 pour ce tutoriel. Vous pouvez ajuster cela selon vos préférences.

```javascript
  return async (ctx, next) => {
    

    try {
      // Appliquer le limiteur de débit à la requête actuelle
      await limiter(ctx, next);
 } catch (err) {
      if (err.status === 429) {
        // Gérer l'erreur de dépassement de limite de débit
        strapi.log.warn('Rate limit exceeded.');
        ctx.status = 429;
        ctx.body = {
          statusCode: 429,
          error: 'Too Many Requests',
          message: 'You have exceeded the maximum number of requests. Please try again later.',
 };
 } else {
        // Relancer les autres erreurs pour qu'elles soient gérées par le middleware de gestion d'erreurs de Strapi
        throw err;
 }
 }
```

Le code ci-dessus définit un middleware qui s'exécute chaque fois qu'une fonction est appelée sur n'importe quelle API. Si les requêtes dépassent le maximum imparti, un code d'erreur est affiché. Voici le code complet.

```javascript

'use strict';

/**
 * Middleware `RateLimit`
 */
const RateLimit = require("koa2-ratelimit").RateLimit;

module.exports = (config, { strapi }) => {
  // Configuration du middleware du limiteur de débit
  const limiter = RateLimit.middleware({
    interval: { min: 1 }, // Fenêtre de temps en minutes
    max: 3, // Nombre maximum de requêtes par intervalle
 });

  return async (ctx, next) => {

    try {
      // Appliquer le limiteur de débit à la requête actuelle
      await limiter(ctx, next);
 } catch (err) {
      if (err.status === 429) {
        // Gérer l'erreur de dépassement de limite de débit
        strapi.log.warn('Rate limit exceeded.');
        ctx.status = 429;
        ctx.body = {
          statusCode: 429,
          error: 'Too Many Requests',
          message: 'You have exceeded the maximum number of requests. Please try again later.',
 };
 } else {
        // Relancer les autres erreurs pour qu'elles soient gérées par le middleware de gestion d'erreurs de Strapi
        throw err;
 }
 }

 };
};
```

Pour assurer son intégration transparente à toutes les API du projet Strapi, les middlewares d'administration doivent également être configurés.

```javascript
const rateLimit = require('../middlewares/rateLimit');

module.exports = [
 'strapi::logger',
 'strapi::errors',
 'strapi::security',
 'strapi::cors',
 'strapi::poweredBy',
 'strapi::query',
 'strapi::body',
 'strapi::session',
 'strapi::favicon',
 'strapi::public',
 
 {
   name: 'global::rateLimit',
   config: {},
 },
];
```

Avec cela, nous avons configuré avec succès le limiteur de débit propulsé par koa2-ratelimiter. Voici des images de son exécution.

![Postman testant le point de terminaison des catégories](https://hackmd.io/_uploads/Bybbd-hj0.png align="left")

![affichage de la réponse d'erreur de limitation de débit](https://hackmd.io/_uploads/r1Zb_-3jC.png align="left")

## Limiteur de débit d'API Strapi personnalisé

Dans le fichier **rateLimit** du dossier **API/middlewares**, créez un limiteur de débit personnalisé en initialisant un stockage en mémoire.

```javascript
const requestCounts = new Map();
```

Ensuite, définissez votre fonction de limitation de débit puis configurez le limiteur de débit.

```javascript
module.exports = (config, { strapi }) => {
  
  const rateLimitConfig = strapi.config.get('admin.rateLimit', {
    interval: 60 * 1000,  
    max: 3,  
 });
```

L'intervalle de temps ci-dessus est de 1 minute tandis que le nombre maximum de requêtes pouvant être effectuées dans l'intervalle de temps spécifié est de 3. Vous pouvez l'ajuster selon vos préférences.

```javascript
return async (ctx, next) => {

    const ip = ctx.ip; 
    const currentTime = Date.now();

    if (!requestCounts.has(ip)) {
      
      requestCounts.set(ip, { count: 1, startTime: currentTime });
 } else {
      const requestInfo = requestCounts.get(ip);

      
      if (currentTime - requestInfo.startTime > rateLimitConfig.interval) {
        requestInfo.count = 1;
        requestInfo.startTime = currentTime;
 } else {
        
 }

      
      if (requestInfo.count > rateLimitConfig.max) {
        strapi.log.warn(`Rate limit exceeded for IP: ${ip}`);

        ctx.status = 429;
        ctx.body = {
          statusCode: 429,
          error: 'Too Many Requests',
          message: 'You have exceeded the maximum number of requests. Please try again later.',
 };
        return;
 }
 }

    await next();
 };
};
```

Ensuite, un middleware est défini qui obtient l'adresse IP de l'utilisateur et la stocke dans le stockage en mémoire. L'intervalle de temps est également défini à partir de l'heure actuelle à laquelle la requête est faite et le compteur de requêtes est mis à jour à chaque nouvelle requête.

Si les requêtes effectuées dépassent le maximum attendu dans l'intervalle de temps d'une minute dans notre cas, une erreur est déclenchée. Voici le code complet ci-dessous.

```javascript
'use strict';
const requestCounts = new Map();

module.exports = (config, { strapi }) => {
  
  const rateLimitConfig = strapi.config.get('admin.rateLimit', {
    interval: 60 * 1000,  
    max: 3,  
 });

  return async (ctx, next) => {

    const ip = ctx.ip; 
    const currentTime = Date.now();

    if (!requestCounts.has(ip)) {
      
      requestCounts.set(ip, { count: 1, startTime: currentTime });
 } else {
      const requestInfo = requestCounts.get(ip);

      
      if (currentTime - requestInfo.startTime > rateLimitConfig.interval) {
        requestInfo.count = 1;
        requestInfo.startTime = currentTime;
 } else {
        
        requestInfo.count += 1;
 }

    
      if (requestInfo.count > rateLimitConfig.max) {
        

        ctx.status = 429;
        ctx.body = {
          statusCode: 429,
          error: 'Too Many Requests',
          message: 'You have exceeded the maximum number of requests. Please try again later.',
 };
        return;
 }
 }

    await next();
 };
};
```

Voici une démonstration du projet.

![récupération des catégories sur Postman](https://hackmd.io/_uploads/BkIyHZ2j0.png align="left")

![erreur de limitation de débit sur Postman](https://hackmd.io/_uploads/HyxgHW2i0.png align="left")

### Implémentation de Express-rate-limiter

Express rate limiter est également un autre package important qui peut être utilisé pour implémenter la limitation de débit dans notre projet. À présent, ce package sera utilisé pour implémenter une limitation de débit d'API spécifique à une route.

La prochaine étape de ce tutoriel consiste à configurer un limiteur de débit efficace pour nos API Strapi créées dans le dépôt.

Pour configurer des limiteurs de débit sur nos applications Strapi, nous travaillerons principalement sur le fichier **routes**. On y accède en entrant dans le dossier **src** au sein du répertoire racine du projet. Dans le dossier **src**, naviguez vers le dossier **API** qui contient tous les fichiers API pour les collections créées dans le tableau de bord Strapi.

![le répertoire de la route produit](https://hackmd.io/_uploads/S1ERbxndR.png align="left")

Le limiteur de débit sera appliqué dans la section des routes de chaque API. Pour ce tutoriel, j'utiliserai l'API des produits comme API de démonstration dans cet article.

```javascript
'use strict';


/**
 * routeur de produit
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::product.product');
```

Ceci est la configuration initiale du code dans le fichier **routes.js** de notre dossier d'API produit. L'outil de limitation de débit choisi pour ce tutoriel est express-rate-limit car il offre beaucoup de simplicité et de convivialité couplées à son efficacité. Voici un lien vers sa [documentation](https://www.npmjs.com/package/express-rate-limit). Pour l'installer, naviguez vers la ligne de commande du répertoire du projet et lancez

```bash
npm install express-rate-limit
```

Une fois l'installation terminée, nous l'initialiserons dans le fichier **products** déjà créé dans le dossier **routes** comme suit.

```javascript
const { rateLimit } = require("express-rate-limit");
```

Continuez et configurez le limiteur de débit selon vos spécifications souhaitées.

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 3 * 60 * 1000, // 3 minutes
  max: 2, // limite chaque IP à 2 requêtes par windowMs
  handler: async (req, res, next) => {
    const ctx = strapi.requestContext.get();
    ctx.status = 429;
    ctx.body = {
      message: "Too many requests",
      policy: "rate limit"
    };
    // S'assurer que la réponse est terminée après avoir défini le corps et le statut de la réponse
    ctx.res.end();
  }
});

module.exports = limiter;
```

Le code ci-dessus sert à configurer les paramètres de limitation de débit que nous avons l'intention d'utiliser pour le fichier.

`windowMs` représente l'intervalle de temps en millisecondes pour le nombre de requêtes. Dans notre cas, nous avons spécifié un temps de 3 minutes. De plus, nous avons spécifié le nombre maximum de requêtes pouvant être effectuées dans ce même laps de temps. Dans notre cas, nous avons utilisé 2 à des fins de démonstration.

Cependant, le paramètre `limit` sert également d'alternative au paramètre `max`. Est également incluse la fonction handler qui s'exécute chaque fois que les requêtes dépassent le nombre fixé. Elle renvoie une **Erreur 429** avec un corps d'erreur contenant "Too many requests".

```javascript

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::product.product', {
  config: {
    find: {
      middlewares: [
        async (ctx, next) => {
          await new Promise((resolve, reject) => {
            limiter(ctx.req, ctx.res, (error) => {
              if (error) {
                ctx.status = 429;
                ctx.body = { error: error.message };
                reject(error);
              } else {
                resolve();
              }
            });
          });
          await next();
        }
      ]
    }
  }
});
```

Le code ci-dessus illustre l'utilisation du middleware d'API Strapi qui sert à garantir que la limite de débit est respectée avant la poursuite de l'exécution des requêtes API. Il garantit également que la requête est interrompue lorsque la limite de débit est dépassée. Voici le code final du projet.

```javascript
'use strict';

/**
 * routeur de produit
 */

const { createCoreRouter } = require('@strapi/strapi').factories;
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 3 * 60 * 1000, // 3 minutes
  max: 2, // limite chaque IP à 2 requêtes par windowMs
  handler: async (req, res, next) => {
    const ctx = strapi.requestContext.get();
    ctx.status = 429;
    ctx.body = {
      message: 'Too many requests',
      policy: 'rate limit'
    };
    // S'assurer que la réponse est terminée après avoir défini le corps et le statut de la réponse
    ctx.res.end();
  }
});

module.exports = createCoreRouter('api::product.product', {
  config: {
    find: {
      middlewares: [
        async (ctx, next) => {
          await new Promise((resolve, reject) => {
            limiter(ctx.req, ctx.res, (error) => {

              if (error) {
                ctx.status = 429;
                ctx.body = { error: error.message };
                reject(error);
              } else {
                resolve();
              }
            });
          });
          if (ctx.status !== 429) {
            await next();
          }
        }
      ]
    }
  }
});
```

Voici une image montrant la fonctionnalité de limitation de débit.

![test de l'endpoint produit dans Postman](https://hackmd.io/_uploads/S116Wu9BR.png align="left")

![ratelimit exécuté avec succès](https://hackmd.io/_uploads/S1zMGO5B0.png align="left")

Vous pouvez également télécharger le code final du projet [ici](https://github.com/oluwatobi2001/Strapi-project). Une fois cela fait, vous pouvez tester la fonctionnalité de limitation de débit de votre API. L'application Strapi peut être lancée en exécutant `npm run develop` dans la ligne de commande.

## Conclusion

Avec cela, nous sommes arrivés à la fin du tutoriel. Nous espérons que vous avez appris l'essentiel sur la limitation de débit, ses utilisations, les outils et les meilleures pratiques.

Vous pouvez également concevoir plusieurs limiteurs de débit dans le code et les implémenter dans n'importe quel point de terminaison de votre choix pour faire des tests.

N'hésitez pas à poser des questions ou à laisser des commentaires. Bon codage !