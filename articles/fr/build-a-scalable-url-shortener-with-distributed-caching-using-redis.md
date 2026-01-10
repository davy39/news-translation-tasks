---
title: Comment construire un raccourcisseur d'URL scalable avec mise en cache distribuée
  en utilisant Redis
subtitle: ''
author: Birkaran Sachdev
co_authors: []
series: null
date: '2024-11-19T15:14:58.005Z'
originalURL: https://freecodecamp.org/news/build-a-scalable-url-shortener-with-distributed-caching-using-redis
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/b9-odQi5oDo/upload/934c8b697ce5ce612a217d47ddf5430d.jpeg
tags:
- name: Redis
  slug: redis
- name: Node.js
  slug: nodejs
- name: caching
  slug: caching
- name: consistent hashing
  slug: consistent-hashing
- name: Cache Invalidation
  slug: cache-invalidation
- name: sharding
  slug: sharding
- name: Url Shortener
  slug: url-shortener
seo_title: Comment construire un raccourcisseur d'URL scalable avec mise en cache
  distribuée en utilisant Redis
seo_desc: In this tutorial, we'll build a scalable URL shortening service using Node.js
  and Redis. This service will leverage distributed caching to handle high traffic
  efficiently, reduce latency, and scale seamlessly. We'll explore key concepts such
  as consi...
---

Dans ce tutoriel, nous allons construire un service de raccourcissement d'URL scalable en utilisant Node.js et Redis. Ce service exploatera la mise en cache distribuée pour gérer efficacement un trafic élevé, réduire la latence et s'adapter de manière transparente. Nous explorerons des concepts clés tels que le hachage cohérent, les stratégies d'invalidation de cache et le sharding pour garantir que le système reste rapide et fiable.

À la fin de ce guide, vous aurez un service de raccourcissement d'URL entièrement fonctionnel qui utilise la mise en cache distribuée pour optimiser les performances. Nous créerons également une démonstration interactive où les utilisateurs pourront saisir des URL et voir des métriques en temps réel comme les hits et les misses du cache.

### Ce que vous allez apprendre

* Comment construire un service de raccourcissement d'URL en utilisant **Node.js** et **Redis**.

* Comment implémenter la **mise en cache distribuée** pour optimiser les performances.

* Comprendre le **hachage cohérent** et les **stratégies d'invalidation de cache**.

* Utiliser **Docker** pour simuler plusieurs instances Redis pour le sharding et la mise à l'échelle.

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

* Node.js (v14 ou supérieur)

* Redis

* Docker

* Connaissances de base en JavaScript, Node.js et Redis.

## Table des matières

* [Aperçu du projet](#heading-aperçu-du-projet)

* [Étape 1 : Configuration du projet](#heading-etape-1-configuration-du-projet)

* [Étape 2 : Configuration des instances Redis](#heading-etape-2-configuration-des-instances-redis)

* [Étape 3 : Implémentation du service de raccourcissement d'URL](#heading-etape-3-implémentation-du-service-de-raccourcissement-durl)

* [Étape 4 : Implémentation de l'invalidation du cache](#heading-etape-4-implémentation-de-linvalidation-du-cache)

* [Étape 5 : Surveillance des métriques du cache](#heading-etape-5-surveillance-des-métriques-du-cache)

* [Étape 6 : Test de l'application](#heading-etape-6-test-de-lapplication)

* [Conclusion : Ce que vous avez appris](#heading-conclusion-ce-que-vous-avez-appris)

## Aperçu du projet

Nous allons construire un service de raccourcissement d'URL où :

1. Les utilisateurs peuvent raccourcir des URL longues et récupérer les URL originales.

2. Le service utilise la **mise en cache Redis** pour stocker les mappages entre les URL raccourcies et les URL originales.

3. Le cache est distribué sur plusieurs instances Redis pour gérer un trafic élevé.

4. Le système démontrera les **hits** et **misses** du cache en temps réel.

### Architecture du système

Pour garantir la scalabilité et les performances, nous diviserons notre service en les composants suivants :

1. **Serveur API** : Gère les requêtes de raccourcissement et de récupération des URL.

2. **Couche de cache Redis** : Utilise plusieurs instances Redis pour la mise en cache distribuée.

3. **Docker** : Simule un environnement distribué avec plusieurs conteneurs Redis.

## Étape 1 : Configuration du projet

Configurons notre projet en initialisant une application Node.js :

```javascript
mkdir scalable-url-shortener
cd scalable-url-shortener
npm init -y
```

Maintenant, installez les dépendances nécessaires :

```javascript
npm install express redis shortid dotenv
```

* `express` : Un framework de serveur web léger.

* `redis` : Pour gérer la mise en cache.

* `shortid` : Pour générer des identifiants courts et uniques.

* `dotenv` : Pour gérer les variables d'environnement.

Créez un fichier **.env** à la racine de votre projet :

```javascript
PORT=3000
REDIS_HOST_1=localhost
REDIS_PORT_1=6379
REDIS_HOST_2=localhost
REDIS_PORT_2=6380
REDIS_HOST_3=localhost
REDIS_PORT_3=6381
```

Ces variables définissent les hôtes et ports Redis que nous utiliserons.

## Étape 2 : Configuration des instances Redis

Nous utiliserons Docker pour simuler un environnement distribué avec plusieurs instances Redis.

Exécutez les commandes suivantes pour démarrer trois conteneurs Redis :

```javascript
docker run -p 6379:6379 --name redis1 -d redis
docker run -p 6380:6379 --name redis2 -d redis
docker run -p 6381:6379 --name redis3 -d redis
```

Cela configurera trois instances Redis fonctionnant sur différents ports. Nous utiliserons ces instances pour implémenter le **hachage cohérent** et le sharding.

## Étape 3 : Implémentation du service de raccourcissement d'URL

Créons notre fichier d'application principal, **index.js** :

```javascript
require('dotenv').config();
const express = require('express');
const redis = require('redis');
const shortid = require('shortid');

const app = express();
app.use(express.json());

const redisClients = [
  redis.createClient({ host: process.env.REDIS_HOST_1, port: process.env.REDIS_PORT_1 }),
  redis.createClient({ host: process.env.REDIS_HOST_2, port: process.env.REDIS_PORT_2 }),
  redis.createClient({ host: process.env.REDIS_HOST_3, port: process.env.REDIS_PORT_3 })
];

// Fonction de hachage pour distribuer les clés parmi les clients Redis
function getRedisClient(key) {
  const hash = key.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0);
  return redisClients[hash % redisClients.length];
}

// Endpoint pour raccourcir une URL
app.post('/shorten', async (req, res) => {
  const { url } = req.body;
  if (!url) return res.status(400).send('URL is required');

  const shortId = shortid.generate();
  const redisClient = getRedisClient(shortId);
  
  await redisClient.set(shortId, url);
  res.json({ shortUrl: `http://localhost:${process.env.PORT}/${shortId}` });
});

// Endpoint pour récupérer l'URL originale
app.get('/:shortId', async (req, res) => {
  const { shortId } = req.params;
  const redisClient = getRedisClient(shortId);
  
  redisClient.get(shortId, (err, url) => {
    if (err || !url) {
      return res.status(404).send('URL not found');
    }
    res.redirect(url);
  });
});

app.listen(process.env.PORT, () => {
  console.log(`Server running on port ${process.env.PORT}`);
});
```

Comme vous pouvez le voir dans ce code, nous avons :

1. **Hachage cohérent** :

   * Nous distribuons les clés (URL raccourcies) sur plusieurs clients Redis en utilisant une fonction de hachage simple.

   * La fonction de hachage garantit que les URL sont distribuées uniformément sur les instances Redis.

2. **Raccourcissement d'URL** :

   * L'endpoint **/shorten** accepte une URL longue et génère un identifiant court en utilisant la bibliothèque **shortid**.

   * L'URL raccourcie est stockée dans l'une des instances Redis en utilisant notre fonction de hachage.

3. **Redirection d'URL** :

   * L'endpoint **/:shortId** récupère l'URL originale depuis le cache et redirige l'utilisateur.

   * Si l'URL n'est pas trouvée dans le cache, une réponse **404** est retournée.

## Étape 4 : Implémentation de l'invalidation du cache

Dans une application réelle, les URL peuvent expirer ou changer avec le temps. Pour gérer cela, nous devons implémenter l'**invalidation du cache**.

### Ajout d'une expiration aux URL mises en cache

Modifions notre fichier **index.js** pour définir un temps d'expiration pour chaque entrée mise en cache :

```javascript
// Endpoint pour raccourcir une URL avec expiration
app.post('/shorten', async (req, res) => {
  const { url, ttl } = req.body; // ttl (time-to-live) est optionnel
  if (!url) return res.status(400).send('URL is required');

  const shortId = shortid.generate();
  const redisClient = getRedisClient(shortId);
  
  await redisClient.set(shortId, url, 'EX', ttl || 3600); // TTL par défaut de 1 heure
  res.json({ shortUrl: `http://localhost:${process.env.PORT}/${shortId}` });
});
```

* **TTL (Time-To-Live)** : Nous définissons un temps d'expiration par défaut de **1 heure** pour chaque URL raccourcie. Vous pouvez personnaliser le TTL pour chaque URL si nécessaire.

* **Invalidation du cache** : Lorsque le TTL expire, l'entrée est automatiquement supprimée du cache.

## Étape 5 : Surveillance des métriques du cache

Pour surveiller les **hits** et **misses** du cache, nous ajouterons quelques logs à nos endpoints dans **index.js** :

```javascript
app.get('/:shortId', async (req, res) => {
  const { shortId } = req.params;
  const redisClient = getRedisClient(shortId);
  
  redisClient.get(shortId, (err, url) => {
    if (err || !url) {
      console.log(`Cache miss for key: ${shortId}`);
      return res.status(404).send('URL not found');
    }
    console.log(`Cache hit for key: ${shortId}`);
    res.redirect(url);
  });
});
```

Voici ce qui se passe dans ce code :

* **Hits du cache** : Si une URL est trouvée dans le cache, c'est un hit du cache.

* **Misses du cache** : Si une URL n'est pas trouvée, c'est un miss du cache.

* Ce logging vous aidera à surveiller les performances de votre cache distribué.

## Étape 6 : Test de l'application

1. **Démarrez vos instances Redis** :

```javascript
docker start redis1 redis2 redis3
```

2. **Exécutez le serveur Node.js** :

```javascript
node index.js
```

3. **Testez les endpoints** en utilisant `curl` ou Postman :

   * Raccourcir une URL :

     ```javascript
     POST http://localhost:3000/shorten
     Body: { "url": "https://example.com" }
     ```

   * Accéder à l'URL raccourcie :

     ```javascript
     GET http://localhost:3000/{shortId}
     ```

## Conclusion : Ce que vous avez appris

Félicitations ! Vous avez réussi à construire un service de **raccourcissement d'URL scalable** avec **mise en cache distribuée** en utilisant Node.js et Redis. Tout au long de ce tutoriel, vous avez appris à :

1. Implémenter le **hachage cohérent** pour distribuer les entrées de cache sur plusieurs instances Redis.

2. Optimiser votre application avec des **stratégies d'invalidation de cache** pour maintenir les données à jour.

3. Utiliser **Docker** pour simuler un environnement distribué avec plusieurs nœuds Redis.

4. Surveiller les **hits et misses du cache** pour optimiser les performances.

### Prochaines étapes :

* **Ajouter une base de données** : Stockez les URL dans une base de données pour une persistance au-delà du cache.

* **Implémenter des analyses** : Suivez les comptes de clics et les analyses pour les URL raccourcies.

* **Déployer dans le cloud** : Déployez votre application en utilisant Kubernetes pour l'auto-scaling et la résilience.

Bon codage !