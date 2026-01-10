---
title: Mise en cache d'une API Next.js avec Redis et Sevalla
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-08-27T16:00:42.744Z'
originalURL: https://freecodecamp.org/news/caching-a-nextjs-api-using-redis-and-sevalla
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756310410998/ee5f34fd-0efe-4efc-9e91-2baa826edff9.png
tags:
- name: Next.js
  slug: nextjs
- name: caching
  slug: caching
- name: Redis
  slug: redis
- name: APIs
  slug: apis
seo_title: Mise en cache d'une API Next.js avec Redis et Sevalla
seo_desc: 'When you hear about Next.js, your first thought may be static websites
  or React-driven frontends. But that’s just part of the story. Next.js can also power
  full-featured backend APIs that you can host and scale just like any other backend
  service.

  In...'
---

Quand on parle de Next.js, on pense d'abord aux sites statiques ou aux frontends basés sur React. Mais ce n'est qu'une partie de l'histoire. Next.js peut également propulser des API backend complètes que vous pouvez héberger et mettre à l'échelle comme n'importe quel autre service backend.

[Dans un article précédent](https://www.freecodecamp.org/news/how-to-deploy-a-nextjs-api-with-postgresql-and-sevalla/), j'ai expliqué comment construire une API Next.js et la déployer avec Sevalla. L'exemple stockait les données dans une base de données PostgreSQL et gérait les requêtes directement. Cela fonctionnait bien, mais à mesure que le trafic augmente, les API qui sollicitent la base de données à chaque requête peuvent ralentir.

C'est là qu'intervient la mise en cache. En ajoutant Redis comme couche de cache, nous pouvons rendre notre API Next.js beaucoup plus rapide et efficace. Dans cet article, nous verrons comment ajouter le cache Redis à notre API, la déployer avec [Sevalla](https://sevalla.com/) et montrer des améliorations mesurables.

Dans le dernier article, j'ai expliqué l'API en détail. Vous pouvez donc [utiliser ce dépôt](https://github.com/manishmshiva/nextjs-api-pgsql) comme base pour ce projet.

## Table des matières

* [Pourquoi la mise en cache est importante](#heading-pourquoi-la-mise-en-cache-est-importante)
    
* [Qu'est-ce que Redis](#heading-qu-est-ce-que-redis)?
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Provisionnement de Redis](#heading-provisionnement-de-redis)
    
* [Mise à jour du cache lors des lectures](#heading-mise-a-jour-du-cache-lors-des-lectures)
    
* [Mise à jour du cache lors des écritures](#heading-mise-a-jour-du-cache-lors-des-ecritures)
    
* [Déploiement sur Sevalla](#heading-deploiement-sur-sevalla)
    
* [Pourquoi Redis fonctionne bien avec les API Next.js](#heading-pourquoi-redis-fonctionne-bien-avec-les-api-nextjs)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi la mise en cache est importante

Chaque fois que votre API interroge la base de données, elle consomme du temps et des ressources. Les bases de données sont excellentes pour stocker et interroger des données structurées, mais elles ne sont pas optimisées pour la vitesse à grande échelle lorsque vous devez servir des milliers de requêtes de lecture par seconde.

La mise en cache résout ce problème en conservant les données fréquemment consultées en mémoire. Au lieu de solliciter la base de données à chaque fois, l'API peut renvoyer les données directement depuis le cache si elles sont disponibles. Redis est parfait pour cela car c'est un magasin clé-valeur en mémoire conçu pour la performance.

Par exemple, si vous récupérez la liste des utilisateurs de la base de données à chaque requête, l'exécution de la requête et le renvoi des résultats peuvent prendre 200 ms. Avec le cache Redis, la première requête stocke le résultat en mémoire, et les requêtes suivantes peuvent renvoyer les mêmes données en moins de 10 ms. C'est une amélioration d'un ordre de grandeur.

## Qu'est-ce que Redis ?

[Redis](https://www.freecodecamp.org/news/how-in-memory-caching-works-in-redis/) est un magasin de données en mémoire qui fonctionne comme une base de données ultra-rapide. Au lieu d'écrire et de lire sur le disque, il conserve les données en mémoire, ce qui le rend incroyablement rapide. C'est pourquoi il est souvent utilisé comme cache, là où la vitesse est plus importante que le stockage à long terme.

Il est conçu pour gérer des charges de travail à haut débit avec une latence très faible, ce qui signifie qu'il peut répondre en microsecondes. Cela en fait un choix parfait pour des cas d'utilisation tels que la mise en cache des réponses API, le stockage des données de session, ou même l'alimentation d'applications en temps réel comme les systèmes de chat et les classements.

Contrairement à une base de données traditionnelle, Redis se concentre sur la simplicité et la vitesse. Il stocke les données sous forme de paires clé-valeur, ce qui vous permet de récupérer ou de mettre à jour rapidement des valeurs sans écrire de requêtes complexes. Et parce qu'il prend en charge des types de données avancés tels que les listes, les ensembles et les hachages, il est beaucoup plus flexible qu'un simple magasin clé-valeur.

Combiné à une API comme celle que nous avons construite dans Next.js, Redis vous aide à réduire la charge sur la base de données principale et à fournir des réponses ultra-rapides aux clients.

## Configuration du projet

Clonons le dépôt :

```typescript
git clone git@github.com:manishmshiva/nextjs-api-pgsql.git next-api
```

Maintenant, entrons dans le répertoire et lançons un npm install pour installer les packages.

```typescript
cd next-api
npm i
```

Créez un fichier .env et ajoutez l'URL de la base de données de Sevalla dans une variable d'environnement.

```typescript
cat .env
```

Le fichier .env devrait ressembler à ceci :

```typescript
PGSQL_URL=postgres://<username>:<password>-@asia-east1-001.proxy.kinsta.app:30503/<db_name>
```

Maintenant, assurons-nous que l'application fonctionne comme prévu en démarrant l'application et en effectuant quelques requêtes API.

Démarrage de l'application :

```typescript
npm run dev
```

Assurons-nous que la base de données est connectée. Allez sur `localhost:3000` dans votre navigateur. Cela devrait renvoyer le JSON suivant :

![GET /](https://cdn.hashnode.com/res/hashnode/image/upload/v1755607650708/543df6fe-3bea-4eb2-b962-13df35b6fb2c.png align="center")

Créons un nouvel utilisateur. Pour créer une nouvelle entrée dans la DB en utilisant [Postman](https://www.postman.com/), envoyez une requête POST avec le JSON suivant :

```typescript
{"id":"d9553bb7-2c72-4d92-876b-9c3b40a8c62c","name":"Larry","email":"larry@example.com","age":"25"}
```

![Postman test](https://cdn.hashnode.com/res/hashnode/image/upload/v1755607596858/7c8c71b5-7868-47a1-ae8d-172474f6d75b.png align="center")

Assurons-nous que l'enregistrement est créé en allant sur `localhost:3000/users` dans le navigateur.

![Réponse Postman pour /users](https://cdn.hashnode.com/res/hashnode/image/upload/v1755607717319/d6743d2a-8373-4d81-afee-1f034e1954e1.png align="center")

Parfait. Maintenant, mettons en cache ces API en utilisant Redis.

## Provisionnement de Redis

Allez sur le tableau de bord de [Sevalla](https://app.sevalla.com/login) et cliquez sur « Databases ». Choisissez « Redis » dans la liste, et laissez le reste des options par défaut.

![Créer une base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1755415913475/0ba7badb-2c67-474a-a5b1-6d72b5bdc5f3.png align="center")

Une fois la base de données créée, activez l'option « external connection » et copiez l'URL accessible publiquement.

![Mettre à jour les paramètres réseau](https://cdn.hashnode.com/res/hashnode/image/upload/v1755611728877/6e139e09-8484-4a50-b007-32ecdb266afb.png align="center")

Voici à quoi cela devrait ressembler dans le fichier .env :

```typescript
REDIS_URL=redis://default:<password>@<host>:<port>
```

Maintenant, installez un client Redis pour Node.js :

```bash
npm install ioredis
```

Nous pouvons maintenant nous connecter à Redis et l'utiliser comme couche de cache pour notre API d'utilisateurs. Voyons comment implémenter la mise en cache.

## Mise à jour du cache lors des lectures

Voici le fichier `users/route.ts` mis à jour qui utilise Redis :

```ts
import { NextResponse } from "next/server";
import { Client } from "pg";
import Redis from "ioredis";

const redis = new Redis(process.env.REDIS_URL!);

async function readUsers() {
  const client = new Client({
    connectionString: process.env.PGSQL_URL,
  });
  await client.connect();

  try {
    const result = await client.query("SELECT id, name, email, age FROM users");
    return result.rows;
  } finally {
    await client.end();
  }
}

export async function GET() {
  try {
    // Vérifier d'abord le cache
    const cached = await redis.get("users");
    if (cached) {
      return NextResponse.json(JSON.parse(cached));
    }

    // Repli sur la base de données si non mis en cache
    const users = await readUsers();

    // Stocker le résultat dans le cache avec un TTL de 60s
    await redis.set("users", JSON.stringify(users), "EX", 60);

    return NextResponse.json(users);
  } catch (err) {
    return NextResponse.json({ error: "Échec de la récupération des utilisateurs" }, { status: 500 });
  }
}
```

Maintenant, quand vous accédez à `/users` :

1. L'API vérifie d'abord Redis.
    
2. Si les données existent, elle les renvoie instantanément.
    
3. Sinon, elle interroge PostgreSQL, enregistre le résultat dans Redis, puis le renvoie.
    

Cela rend les requêtes répétées extrêmement rapides. Vous pouvez ajuster l'expiration du cache (`EX 60`) en fonction de la fraîcheur requise pour vos données.

Sans mise en cache Redis, récupérer `/users` dix fois signifie dix requêtes à la base de données. Chacune peut prendre environ 150–200 ms selon la taille de la base de données et la latence du réseau.

Avec Redis, la première requête prend toujours ~200 ms car elle remplit le cache. Mais chaque requête suivante est presque instantanée, souvent moins de 10 ms. C'est une **amélioration de 20x**.

Ce gain de vitesse est crucial lorsque votre API fait face à des centaines ou des milliers de requêtes par seconde. La mise en cache réduit non seulement la latence mais allège également la charge de votre base de données.

## Mise à jour du cache lors des écritures

Actuellement, seules les requêtes GET utilisent le cache. Mais que se passe-t-il si nous ajoutons de nouveaux utilisateurs ? Le cache renverrait toujours les anciennes données.

La solution consiste à mettre à jour ou à vider le cache chaque fois qu'une écriture se produit. Mettons à jour le gestionnaire `POST` :

```ts
export async function POST(req: Request) {
  try {
    const body = await req.json();
    const client = new Client({
      connectionString: process.env.PGSQL_URL,
    });
    await client.connect();

    const query = `
      INSERT INTO users (id, name, email, age)
      VALUES ($1, $2, $3, $4)
      RETURNING *;
    `;

    const result = await client.query(query, [
      body.id,
      body.name,
      body.email,
      body.age,
    ]);

    await client.end();

    // Invalider le cache pour que le prochain GET récupère des données fraîches
    await redis.del("users");

    return NextResponse.json(result.rows[0]);
  } catch (err) {
    return NextResponse.json({ error: "Échec de l'ajout de l'utilisateur" }, { status: 500 });
  }
}
```

Maintenant, chaque fois qu'un nouvel utilisateur est créé, le cache pour `users` est vidé. La requête GET suivante interrogera la base de données, rafraîchira le cache, puis continuera à servir des données mises en cache.

## **Déploiement sur Sevalla**

Poussez votre code sur GitHub ou [forkez mon dépôt](https://github.com/manishmshiva/nextjs-api-redis). Maintenant, allons sur Sevalla et créons une nouvelle application.

![Création d'application Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1754545093624/9747a06d-0dcf-482a-89b9-732b9937b1dc.png align="left")

Choisissez votre dépôt dans le menu déroulant et cochez « Automatic deployment on commit ». Cela garantira que le déploiement est automatique à chaque fois que vous poussez du code. Choisissez « Hobby » dans la section des ressources.

![créer une nouvelle application](https://cdn.hashnode.com/res/hashnode/image/upload/v1755683871627/cc8bd555-caaa-43f2-a9a3-f3f0d1481108.png align="center")

Cliquez sur « Create » et non sur « Create and deploy ». Nous n'avons pas encore ajouté notre URL PostgreSQL et notre URL Redis en tant que variables d'environnement, donc l'application plantera si vous essayez de la déployer.

Allez dans la section « Environment variables » et ajoutez la clé « PGSQL\_URL » et l'URL dans le champ de valeur. Faites de même pour la clé « REDIS\_URL » et ajoutez l'URL Redis.

![Ajout de variables d'environnement](https://cdn.hashnode.com/res/hashnode/image/upload/v1755683943610/97932885-29aa-4cef-b999-689f0871809e.png align="center")

Revenez maintenant à la section « Overview » et cliquez sur « Deploy now ».

![Déploiement de l'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1755684196447/a1da5802-aa2c-47f6-8837-14f7e40198fd.png align="center")

Une fois le déploiement terminé, cliquez sur « Visit app » pour obtenir l'URL en direct de votre API. Vous pouvez remplacer [localhost:3000](http://localhost:3000) par la nouvelle URL dans Postman et tester votre API.

## Pourquoi Redis fonctionne bien avec les API Next.js

Redis est léger, ultra-rapide et parfait pour la mise en cache des réponses API. Dans le contexte de Next.js, il s'intègre naturellement parce que :

* Les routes API s'exécutent côté serveur où Redis peut être interrogé directement.
    
* La logique de mise en cache est simple à ajouter autour des appels de base de données.
    
* Redis peut être utilisé pour plus que la simple mise en cache – des choses comme la limitation de débit (rate limiting), le stockage de session et le pub/sub sont également des modèles courants.
    

En combinant Next.js, PostgreSQL et Redis sur Sevalla, vous obtenez une pile (stack) rapide, évolutive et facile à déployer.

## Conclusion

La mise en cache n'est pas seulement une optimisation – c'est une nécessité pour les API du monde réel. Next.js vous aide à construire des API backend robustes qui peuvent être déployées facilement. En ajoutant Redis au mélange, ces API peuvent gérer la montée en charge sans sourciller.

Sevalla unifie le tout en fournissant PostgreSQL géré, Redis et l'hébergement d'applications en un seul endroit. Avec quelques variables d'environnement et un dépôt GitHub, vous pouvez passer du développement local à une API en production mise en cache en quelques minutes.

*J'espère que vous avez apprécié cet article. Inscrivez-vous à ma newsletter gratuite sur l'IA* [***TuringTalks.ai***](https://www.turingtalks.ai/) *pour plus de tutoriels pratiques sur l'IA. Vous pouvez également me trouver sur* [***Linkedin***](https://www.linkedin.com/in/manishmshiva)***.***