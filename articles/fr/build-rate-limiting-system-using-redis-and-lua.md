---
title: Comment construire un système de limitation de débit distribué en utilisant
  Redis et des scripts Lua
subtitle: ''
author: Birkaran Sachdev
co_authors: []
series: null
date: '2024-11-19T14:39:25.408Z'
originalURL: https://freecodecamp.org/news/build-rate-limiting-system-using-redis-and-lua
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/CGWK6k2RduY/upload/a5ac857cec1d18720a060fc5e3462cf3.jpeg
tags:
- name: Lua
  slug: lua
- name: Redis
  slug: redis
- name: Docker
  slug: docker
seo_title: Comment construire un système de limitation de débit distribué en utilisant
  Redis et des scripts Lua
seo_desc: 'In this comprehensive guide, you’ll build a distributed rate limiter using
  Redis and Lua scripting to control user requests in a high-traffic environment.

  Rate limiting is crucial in any system to prevent abuse, manage traffic, and protect
  your resou...'
---

Dans ce guide complet, vous allez construire un limiteur de débit distribué en utilisant Redis et des scripts Lua pour contrôler les requêtes des utilisateurs dans un environnement à fort trafic.

La limitation de débit est cruciale dans tout système pour prévenir les abus, gérer le trafic et protéger vos ressources. En exploitant Redis et Lua, vous allez construire un système de limitation de débit efficace et scalable capable de gérer un grand nombre de requêtes tout en gardant vos services backend en sécurité.

Nous allons également inclure une démonstration interactive où les utilisateurs peuvent simuler du trafic, observer les limites de débit appliquées et visualiser les logs des requêtes bloquées.

## Ce que vous allez apprendre

* Comment construire un système de limitation de débit en utilisant Redis.
  
* Comment utiliser des scripts Lua avec Redis pour réaliser des opérations atomiques.
  
* Comprendre les structures de données Redis pour un suivi efficace des requêtes.
  
* Techniques pour gérer un trafic élevé dans un système distribué.
  
* Utiliser Docker pour simuler et scaler un limiteur de débit distribué.
  

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

* Node.js (v14 ou supérieur)
  
* Redis
  
* Docker (pour simuler un environnement distribué)
  
* Compréhension basique de Node.js, Redis et des scripts Lua.
  

## Table des matières

* [Ce que vous allez apprendre](#heading-ce-que-vous-allez-apprendre)
  
* [Prérequis](#heading-prerequis)
  
* [Aperçu du projet](#heading-aperçu-du-projet)
  
* [Étape 1 : Comment configurer le projet](#heading-etape-1-comment-configurer-le-projet)
  
* [Étape 2 : Comment configurer Redis](#heading-etape-2-comment-configurer-redis)
  
* [Étape 3 : Comment implémenter le limiteur de débit avec Redis et Lua](#heading-etape-3-comment-implementer-le-limiteur-de-debit-avec-redis-et-lua)
  
* [Étape 4 : Comment créer le serveur API Node.js](#heading-etape-4-comment-creer-le-serveur-api-nodejs)
  
* [Étape 5 : Comment tester le limiteur de débit](#heading-etape-5-comment-tester-le-limiteur-de-debit)
  
* [Étape 6 : Comment visualiser les métriques de limitation de débit](#heading-etape-6-comment-visualiser-les-metriques-de-limitation-de-debit)
  
* [Étape 7 : Comment déployer avec Docker](#heading-etape-7-comment-deployer-avec-docker)
  
* [Conclusion : Ce que vous avez appris](#heading-conclusion-ce-que-vous-avez-appris)
  

## Aperçu du projet

Dans ce tutoriel, vous allez :

1. Construire un limiteur de débit en utilisant Redis et Lua pour appliquer des quotas de requêtes.
  
2. Utiliser des scripts Lua pour garantir des opérations atomiques, évitant les conditions de course.
  
3. Implémenter un algorithme de token bucket pour la limitation de débit.
  
4. Créer une démonstration interactive pour simuler un trafic élevé et visualiser la limitation de débit en action.
  

### Architecture du système

Vous allez construire le système avec les composants suivants :

1. **Serveur API** : Gère les requêtes entrantes des utilisateurs.
  
2. **Redis** : Stocke les données des requêtes et applique les limites de débit.
  
3. **Scripts Lua** : Assure les mises à jour atomiques de Redis pour la limitation de débit.
  
4. **Docker** : Simule un environnement distribué avec plusieurs instances.
  

## Étape 1 : Comment configurer le projet

Commençons par configurer notre projet Node.js :

```javascript
mkdir distributed-rate-limiter
cd distributed-rate-limiter
npm init -y
```

Ensuite, installez les dépendances requises :

```javascript
npm install express redis dotenv
```

* **express** : Un framework de serveur web léger.
  
* **redis** : Pour interagir avec Redis.
  
* **dotenv** : Pour gérer les variables d'environnement.
  

Créez un fichier **.env** avec le contenu suivant :

```javascript
REDIS_HOST=localhost
REDIS_PORT=6379
PORT=3000
RATE_LIMIT=5
TIME_WINDOW=60
```

Ces variables définissent l'hôte Redis, le port, la limite de débit (nombre de requêtes autorisées) et la fenêtre de temps (en secondes).

## Étape 2 : Comment configurer Redis

Avant de plonger dans le code, assurez-vous que Redis est installé et en cours d'exécution sur votre système. Si vous n'avez pas Redis installé, vous pouvez utiliser Docker pour le configurer rapidement :

```javascript
docker run -p 6379:6379 --name redis-rate-limiter -d redis
```

## Étape 3 : Comment implémenter le limiteur de débit avec Redis et Lua

Pour gérer efficacement la limitation de débit, nous allons utiliser un algorithme de token bucket. Dans cet algorithme :

1. Chaque utilisateur a un "bucket" de tokens.
  
2. Chaque requête consomme un token.
  
3. Les tokens se rechargent périodiquement à un taux défini.
  

Pour garantir l'atomicité et éviter les conditions de course, nous allons utiliser des scripts Lua avec Redis. Les scripts Lua dans Redis s'exécutent de manière atomique, ce qui signifie qu'ils ne peuvent pas être interrompus par d'autres opérations pendant leur exécution.

### Comment créer un script Lua pour la limitation de débit

Créez un fichier appelé **rate_limiter.lua** :

```javascript
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local current = redis.call("get", key)

if current and tonumber(current) >= limit then
    return 0
else
    if current then
        redis.call("incr", key)
    else
        redis.call("set", key, 1, "EX", window)
    end
    return 1
end
```

1. **Entrées** :
  
  * **KEYS[1]** : La clé Redis représentant le compteur de requêtes de l'utilisateur.
      
  * **ARGV[1]** : La limite de débit (nombre maximum de requêtes autorisées).
      
  * **ARGV[2]** : La fenêtre de temps (en secondes) pour la limite de débit.
      
2. **Logique** :
  
  * Si l'utilisateur a atteint la limite de débit, retourner `0` (requête bloquée).
      
  * Si l'utilisateur est dans la limite, incrémenter son compteur de requêtes ou définir un nouveau compteur avec une expiration si c'est la première requête.
      
  * Retourner 1 (requête autorisée).
      

## Étape 4 : Comment créer le serveur API Node.js

Créez un fichier appelé **server.js** :

```javascript
require('dotenv').config();
const express = require('express');
const redis = require('redis');
const fs = require('fs');
const path = require('path');

const app = express();
const client = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT
});

const rateLimitScript = fs.readFileSync(path.join(__dirname, 'rate_limiter.lua'), 'utf8');

const RATE_LIMIT = parseInt(process.env.RATE_LIMIT);
const TIME_WINDOW = parseInt(process.env.TIME_WINDOW);

// Middleware pour la limitation de débit
async function rateLimiter(req, res, next) {
  const ip = req.ip;
  try {
    const allowed = await client.eval(rateLimitScript, 1, ip, RATE_LIMIT, TIME_WINDOW);
    if (allowed === 1) {
      next();
    } else {
      res.status(429).json({ message: 'Trop de requêtes. Veuillez réessayer plus tard.' });
    }
  } catch (err) {
    console.error('Erreur dans le limiteur de débit :', err);
    res.status(500).json({ message: 'Erreur interne du serveur' });
  }
}

app.use(rateLimiter);

app.get('/', (req, res) => {
  res.send('Bienvenue dans l\'API avec limitation de débit !');
});

const PORT = process.env.PORT;
app.listen(PORT, () => {
  console.log(`Serveur en cours d'exécution sur le port ${PORT}`);
});
```

1. **Middleware de limitation de débit** :
  
  * Récupère l'adresse IP du client et vérifie s'il est dans la limite de débit en utilisant le script Lua.
      
  * Si l'utilisateur dépasse la limite, une réponse `429` est envoyée.
      
2. **Point de terminaison de l'API** :
  
  * Le point de terminaison racine est limité en débit, donc les utilisateurs ne peuvent y accéder qu'un nombre limité de fois dans la fenêtre spécifiée.
      

## Étape 5 : Comment tester le limiteur de débit

1. **Démarrer Redis** :
  
  ```basic
  docker start redis-rate-limiter
  ```
  
2. **Exécuter le serveur Node.js** :
  
  ```bash
  node server.js
  ```
  
3. **Simuler des requêtes** :
  
  * Utilisez `curl` ou Postman pour tester le limiteur de débit :
      
      ```bash
      curl http://localhost:3000
      ```
      
  * Envoyez plusieurs requêtes rapidement pour voir la limitation de débit en action.
      

## Étape 6 : Comment visualiser les métriques de limitation de débit

Pour surveiller les métriques de limitation de débit comme les hits de cache et les requêtes bloquées, nous allons ajouter des logs au middleware dans **server.js** :

```javascript
async function rateLimiter(req, res, next) {
  const ip = req.ip;
  try {
    const allowed = await client.eval(rateLimitScript, 1, ip, RATE_LIMIT, TIME_WINDOW);
    if (allowed === 1) {
      console.log(`Requête autorisée de ${ip}`);
      next();
    } else {
      console.log(`Requête bloquée de ${ip}`);
      res.status(429).json({ message: 'Trop de requêtes. Veuillez réessayer plus tard.' });
    }
  } catch (err) {
    console.error('Erreur dans le limiteur de débit :', err);
    res.status(500).json({ message: 'Erreur interne du serveur' });
  }
}
```

## Étape 7 : Comment déployer avec Docker

Containerisons l'application pour l'exécuter dans un environnement distribué.

Créez un `Dockerfile` :

```dockerfile
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
EXPOSE 3000
CMD ["node", "server.js"]
```

Construisez et exécutez le conteneur Docker :

```bash
docker build -t rate-limiter .
docker run -p 3000:3000 rate-limiter
```

Vous pouvez maintenant scaler le limiteur de débit en exécutant plusieurs instances.

## Conclusion : Ce que vous avez appris

Félicitations ! Vous avez réussi à construire un limiteur de débit distribué en utilisant Redis et des scripts Lua. Tout au long de ce tutoriel, vous avez appris à :

1. Implémenter la limitation de débit pour contrôler les requêtes des utilisateurs dans un système distribué.
  
2. Utiliser des scripts Lua dans Redis pour effectuer des opérations atomiques.
  
3. Appliquer un algorithme de token bucket pour gérer les quotas de requêtes.
  
4. Surveiller les métriques de limitation de débit pour optimiser les performances.
  
5. Utiliser Docker pour simuler un environnement distribué scalable.
  

### Prochaines étapes :

1. **Ajouter la limitation de débit par ID utilisateur** : Étendre le système pour supporter des limites de débit par utilisateur.
  
2. **Intégrer avec Nginx** : Utiliser Nginx comme proxy inverse avec une limitation de débit basée sur Redis.
  
3. **Déployer avec Kubernetes** : Scaler votre limiteur de débit en utilisant Kubernetes pour une haute disponibilité.
  

Bonne programmation !