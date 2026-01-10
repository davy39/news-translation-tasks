---
title: 'Comment créer des applications web prêtes pour la production avec le Framework
  Hono : une exploration approfondie'
subtitle: ''
author: Mayur Vekariya
co_authors: []
series: null
date: '2025-09-08T20:37:52.863Z'
originalURL: https://freecodecamp.org/news/build-production-ready-web-apps-with-hono
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757363825321/562644c8-b2b3-4c1c-92c2-736bcade5aac.png
tags:
- name: JavaScript
  slug: javascript
- name: hono
  slug: hono
- name: javascript framework
  slug: javascript-framework
- name: Node.js
  slug: nodejs
seo_title: 'Comment créer des applications web prêtes pour la production avec le Framework
  Hono : une exploration approfondie'
seo_desc: As a dev, you’d probably like to write your application once and not have
  to worry so much about where it's going to run. This is what the open source framework
  Hono lets you do, and it’s a game-changer. Hono is a small, incredibly fast web
  framework...
---

En tant que développeur, vous aimeriez probablement écrire votre application une seule fois sans trop vous soucier de l'endroit où elle sera exécutée. C'est ce que le Framework open source Hono vous permet de faire, et c'est un véritable changement de paradigme. Hono est un petit Framework web incroyablement rapide qui adopte la philosophie « écrire une fois, exécuter n'importe où ».

L'écosystème JavaScript évolue rapidement. Un jour, nous construisons des serveurs Node.js monolithiques. Le lendemain, tout tourne autour des fonctions serverless et de l'exécution de code à l'Edge sur des plateformes comme Cloudflare ou Vercel. Se tenir à jour peut ressembler à un travail à plein temps.

[Hono](https://hono.dev/) est construit sur les Standards Web – les mêmes objets `Request` et `Response` que dans votre navigateur – ce qui signifie que votre code est naturellement portable sur presque tous les environnements d'exécution JavaScript.

Ce guide est une exploration approfondie de ce petit Framework puissant, conçu pour vous aider à créer de véritables applications prêtes pour la production. Nous passerons le traditionnel « Hello, World ! » pour plonger directement dans les modèles et les fonctionnalités que vous utiliserez réellement, avec de nombreux exemples de code détaillés tout au long du parcours.

## **Table des matières**

* [Ce que vous apprendrez dans ce guide](#heading-ce-que-vous-apprendrez-dans-ce-guide)
    
* [Prérequis pour suivre ce guide](#heading-prerequis-pour-suivre-ce-guide)
    
* [Comment configurer un projet Hono professionnel](#heading-comment-configurer-un-projet-hono-professionnel)
    
* [Comprendre l'API principale de Hono](#heading-comprendre-lapi-principale-de-hono)
    
* [L'objet Context en profondeur](#heading-lobjet-context-en-profondeur)
    
* [Comment utiliser les fonctionnalités avancées pour les applications de production](#heading-comment-utiliser-les-fonctionnalites-avancees-pour-les-applications-de-production)
    
* [Guide de déploiement pour Hono](#heading-guide-de-deploiement-pour-hono)
    

### Ce que vous apprendrez dans ce guide

À la fin de ce tutoriel, vous serez capable de :

* Structurer un projet Hono pour le développement et la production.
    
* Implémenter des modèles de routage avancés.
    
* Exploiter toute la puissance de l'objet **Context** pour gérer les requêtes et transmettre des données entre les middlewares.
    
* Écrire des middlewares personnalisés complexes pour l'authentification, la journalisation et la gestion des erreurs.
    
* Valider les données entrantes à l'aide du validateur officiel **Zod** pour des API robustes.
    
* Créer une petite application rendue côté serveur avec des composants **JSX**.
    
* Déployer une application Hono sur diverses plateformes d'hébergement modernes.
    

### Prérequis pour suivre ce guide

Ceci est un guide approfondi, mais il suppose que vous ayez quelques connaissances de base. Avant de commencer, vous devriez avoir :

* **Node.js installé :** La version 18 ou supérieure est recommandée.
    
* **Un éditeur de code :** Visual Studio Code est un excellent choix.
    
* **Une familiarité avec TypeScript :** Vous devez comprendre les types de base, les fonctions et `async`/`await`.
    
* **Connaissances de base en ligne de commande :** Vous devez être à l'aise avec l'exécution de commandes dans votre terminal.
    

## Comment configurer un projet Hono professionnel

Vous pouvez commencer avec Hono en utilisant une seule commande. Cela créera un nouveau répertoire de projet avec une structure et des fichiers de configuration recommandés. Lorsque vous y êtes invité, sélectionnez le template `nodejs` et choisissez d'installer les dépendances avec votre gestionnaire de paquets préféré (par exemple, npm).

```bash
npm create hono@latest hono-production-app
```

La commande vous guidera à travers la configuration :

```bash
> npx create-hono hono-production-app

create-hono version 0.19.2
✔ Using target directory … hono-production-app
✔ Which template do you want to use? nodejs
✔ Do you want to install project dependencies? Yes
✔ Which package manager do you want to use? npm
✔ Cloning the template
✔ Installing project dependencies
🎉 Copied project files
Get started with: cd hono-production-app
```

Maintenant, naviguez dans votre nouveau répertoire : `cd hono-production-app`. Examinons les fichiers qui ont été créés :

* `package.json` : Définit les dépendances et les scripts de votre projet.
    
* `tsconfig.json` : Le fichier de configuration TypeScript.
    
* `src/index.ts` : Le point d'entrée de votre application.
    

Maintenant, vous pouvez exécuter `npm run dev` pour démarrer votre serveur de développement. Naviguez vers [`http://localhost:3000`](http://localhost:3000), et vous verrez "Hello Hono!".

## Comprendre l'API principale de Hono

L'API de Hono est conçue pour être minimale, ce qui la rend facile à apprendre – tout en étant incroyablement puissante.

### Comment utiliser des techniques de routage avancées

Vous connaissez peut-être déjà `app.get()` et `app.post()` d'Express, mais le routeur de Hono peut faire bien plus.

#### 1\. Comment router avec des expressions régulières

Vous pouvez contraindre un paramètre d'URL à correspondre à une expression régulière spécifique. Par exemple, pour vous assurer qu'un paramètre `:id` n'accepte que des chiffres, vous pouvez faire ceci :

```typescript
// Ne correspond qu'aux routes comme /users/123, pas /users/abc
app.get('/users/:id{[0-9]+}', (c) => {
  const id = c.req.param('id')
  return c.text(`Fetching data for user ID: ${id}`)
})
```

#### 2\. Comment utiliser des routes optionnelles et des jokers (wildcards)

Vous pouvez définir des routes qui correspondent à plusieurs chemins à l'aide de jokers (`*`) ou gérer des paramètres optionnels.

```typescript
// Ceci correspondra à /files/image.png, /files/docs/report.pdf, et ainsi de suite.
app.get('/files/*', (c) => {
  // c.req.path contiendra le chemin complet correspondant
  return c.text(`You are accessing the file at: ${c.req.path}`)
})

// Le '?' rend la partie '/:format?' de l'URL optionnelle
// Ceci correspondra à la fois à /api/posts et /api/posts/json
app.get('/api/posts/:format?', (c) => {
  const format = c.req.param('format')
  if (format === 'json') {
    return c.json({ message: 'Here are the posts in JSON format.' })
  }
  return c.text('Here are the posts in plain text.')
})
```

#### 3\. Comment grouper les routes avec `app.route()`

Pour les applications plus importantes, vous devriez organiser vos routes en groupes logiques. La méthode `app.route()` est parfaite pour cela. Elle vous permet de créer des routeurs modulaires et de les monter sur un préfixe spécifique.

Créons une structure d'API plus complexe pour un blog.

`src/routes/posts.ts`

```typescript
import { Hono } from 'hono'

// Création d'une nouvelle instance de routeur spécifiquement pour les posts
const posts = new Hono()

posts.get('/', (c) => c.json({ posts: [] }))
posts.post('/', (c) => c.json({ message: 'Post created' }, 201))
posts.get('/:id', (c) => c.json({ post: { id: c.req.param('id') } }))

export default posts
```

`src/routes/authors.ts`

```typescript
import { Hono } from 'hono'

const authors = new Hono()

authors.get('/', (c) => c.json({ authors: [] }))
authors.get('/:id', (c) => c.json({ author: { id: c.req.param('id') } }))

export default authors
```

`src/index.ts`

```typescript
import { serve } from '@hono/node-server'
import { Hono } from 'hono'
import { appendTrailingSlash } from 'hono/trailing-slash';
import posts from './routes/posts.js'
import authors from './routes/authors.js'

const app = new Hono()

app.use(appendTrailingSlash());

app.route('/posts/', posts)
app.route('/authors/', authors)

app.get('/', (c) => {
  return c.text('Hello Hono!')
})

serve({
  fetch: app.fetch,
  port: 3000
}, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})
```

Ce modèle garde votre fichier `index.ts` principal propre et rend votre application beaucoup plus facile à naviguer et à maintenir.

## L'objet Context en profondeur

Le **Context** (`c`) est le cœur de Hono. C'est un objet qui est transmis à chaque middleware et gestionnaire de route, contenant toutes les informations relatives à la requête actuelle. C'est essentiellement un conteneur pour la requête (`c.req`), des méthodes pour créer une réponse (`c.json`, `c.html`, `c.text`), ainsi qu'une propriété spéciale pour transmettre des données entre les middlewares (`c.set` et `c.get`).

Bien que cela couvre ses propriétés les plus courantes et utiles, l'objet Context complet en contient davantage. Pour une liste exhaustive de toutes les propriétés et méthodes disponibles, vous pouvez vous référer à la [documentation officielle de Hono](https://hono.dev/docs/api/context).

Explorons comment vous pouvez utiliser l'objet Context pour transmettre des données entre les middlewares et les gestionnaires, une technique cruciale pour des choses comme l'authentification.

Les méthodes `c.set()` et `c.get()` vous permettent de stocker et de récupérer des données typées dans le contexte d'une seule requête.

Remplacez `src/index.ts` par cet exemple pour l'authentification :

```typescript
import { Hono } from 'hono'
import type { Context, Next } from 'hono'

// Définition d'un type pour les variables que nous stockerons dans le contexte
type AppVariables = {
  user: {
    id: string
    name: string
    roles: string[]
  }
}

// Utilisation d'un générique pour informer notre application Hono du type des variables
const app = new Hono<{ Variables: AppVariables }>()

// Middleware pour "authentifier" un utilisateur à partir d'un header
const authMiddleware = async (c: Context, next: Next) => {
  const userId = c.req.header('X-User-ID')
  if (!userId) {
    return c.json({ error: 'Missing X-User-ID header' }, 401)
  }

  // Dans une application réelle, vous récupéreriez ceci d'une base de données
  const user = {
    id: userId,
    name: 'Jane Doe',
    roles: ['admin', 'editor'],
  }

  // Utilisation de c.set() pour attacher les données utilisateur au contexte
  c.set('user', user)
  
  await next()
}

app.get('/admin/dashboard', authMiddleware, (c) => {
  // Utilisation de c.get() pour récupérer les données utilisateur typées
  const user = c.get('user')

  if (!user.roles.includes('admin')) {
    return c.json({ error: 'Forbidden' }, 403)
  }

  return c.json({
    message: `Welcome to the admin dashboard, ${user.name}!`,
    userId: user.id,
  })
})

export default app
```

Décomposons les parties importantes du code ci-dessus.

* **Variables de contexte typées** : Nous définissons un type TypeScript `AppVariables` et le passons en tant que générique à notre application Hono `new Hono<{ Variables: AppVariables }>()`. C'est une fonctionnalité puissante qui nous donne une sécurité de type complète pour nos variables de contexte, évitant les erreurs de frappe et garantissant que les données que nous stockons et récupérons correspondent exactement à ce que nous attendons.
    
* **Middleware personnalisé** : Le `authMiddleware` est une fonction personnalisée qui s'exécute avant notre gestionnaire de route. Elle inspecte les en-têtes de la requête entrante (`c.req.header('X-User-ID')`).
    
* **Stockage des données** : Si un en-tête valide est trouvé, le middleware utilise `c.set('user', user)` pour stocker l'objet utilisateur dans le contexte. Ces données sont désormais disponibles pour tout middleware ou gestionnaire de route ultérieur pour la même requête.
    
* **Récupération des données** : Le gestionnaire de route `app.get('/admin/dashboard', ...)` utilise ensuite `c.get('user')` pour récupérer l'objet utilisateur. Le système de types de Hono garantit que `c.get('user')` renvoie une variable de type `{ id: string; name: string; roles: string[]; }`.
    
* **Contrôle de flux** : Si l'utilisateur est manquant ou n'a pas le rôle "admin", le middleware ou le gestionnaire peut immédiatement envoyer une réponse d'erreur en utilisant `c.json()` et un code d'état, empêchant la requête de continuer plus loin.
    

Maintenant, exécutez `npm run dev`.

Vous pouvez tester avec `curl` (en ajoutant l'en-tête) :

```bash
curl -H "X-User-ID: 123" http://localhost:3000/admin/dashboard
```

Cela renverra un message de bienvenue.

Sans l'en-tête :

```bash
curl http://localhost:3000/admin/dashboard
```

Cela renverra une erreur `401`.

Ceci démontre comment transmettre des données typées de manière sécurisée et efficace entre les middlewares et les gestionnaires de route.

## Comment utiliser les fonctionnalités avancées pour les applications de production

Nous sommes maintenant prêts à aborder les fonctionnalités que vous utiliserez quotidiennement en production : middleware avancé, validation de données et création d'applications full-stack.

### Comment utiliser des modèles de middleware avancés

Hono dispose d'un ensemble puissant de middlewares intégrés, notamment pour JWT et la mise en cache. Ce ne sont pas des bibliothèques distinctes que vous devez installer, mais plutôt des fonctions fournies avec le package Hono lui-même.

**Étape 1 :** Remplacez `src/index.ts` par cet exemple pour JWT et la mise en cache :

```typescript
import { Hono } from 'hono'
import { serve } from '@hono/node-server'
import { jwt, sign } from 'hono/jwt'

const app = new Hono()
const SECRET = 'my-secret-key' // Utilisez une variable d'environnement en production !

// Création d'un simple stockage de cache en mémoire
const cacheStore = new Map();

// Middleware de mise en cache personnalisé pour Node.js
app.use('/api/public-data', async (c, next) => {
  const cacheKey = c.req.url;

  // Vérifie si la réponse est dans notre cache
  if (cacheStore.has(cacheKey)) {
    const cachedItem = cacheStore.get(cacheKey);
    console.log('Serving from custom in-memory cache.');
    return new Response(cachedItem.body, { headers: cachedItem.headers });
  }

  // Si pas dans le cache, passe au gestionnaire de route
  await next();

  // Après le retour du gestionnaire, clone et stocke la réponse
  if (c.res) {
    const newResponse = c.res.clone();
    const body = await newResponse.text();
    const headers = Object.fromEntries(newResponse.headers.entries());
    cacheStore.set(cacheKey, { body, headers });
    console.log('Storing response in custom in-memory cache.');
  }
});

// Connexion pour obtenir un JWT
app.post('/login', async (c) => {
  const { username } = await c.req.json()
  if (username === 'admin') {
    const payload = {
      sub: username,
      role: 'admin',
      exp: Math.floor(Date.now() / 1000) + 60 * 5, // Expiration 5 minutes
    }
    const token = await sign(payload, SECRET)
    return c.json({ token })
  }
  return c.json({ error: 'Invalid credentials' }, 401)
})

// Route protégée
app.get(
  '/api/protected',
  jwt({ secret: SECRET }),
  (c) => {
    const payload = c.get('jwtPayload')
    return c.json({ message: 'You have access!', payload })
  }
)

// Route avec cache
app.get(
  '/api/public-data',
  async (c) => {
    console.log('Executing handler with delay...');
    await new Promise(resolve => setTimeout(resolve, 1000)) // Simule un délai
    return c.json({ data: 'This is some public data that rarely changes.' })
  }
)

serve({ fetch: app.fetch, port: 3000 }, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})
```

Le code ci-dessus montre deux types différents de middlewares en action.

Tout d'abord, le **middleware JWT** (`jwt`) est un moyen puissant de sécuriser vos routes. Lorsque nous appelons `jwt({ secret: SECRET })`, nous demandons à Hono de vérifier la présence d'un JWT valide dans l'en-tête `Authorization` de la requête entrante. Si un jeton valide est trouvé, il décode le payload et l'attache au contexte, où nous pouvons le récupérer avec `c.get('jwtPayload')`. Si aucun jeton n'est trouvé ou s'il est invalide, le middleware arrête automatiquement la requête et renvoie une erreur `401 Unauthorized`.

Nous avons également un **Middleware de Cache Personnalisé** qui démontre la puissance du système de middleware de Hono pour la mise en cache en mémoire. Le middleware vérifie d'abord une `Map` en mémoire pour voir si une réponse pour l'URL actuelle existe déjà. Si c'est le cas, il renvoie immédiatement la réponse mise en cache, empêchant l'exécution du gestionnaire de route. Si la réponse n'est pas dans le cache, il laisse la requête continuer vers le gestionnaire. Une fois que le gestionnaire a répondu, le middleware intercepte la réponse et en stocke une copie dans le cache avant de la renvoyer au client. C'est un modèle robuste et fiable pour les environnements Node.js.

**Étape 2 :** Exécutez `npm run dev`.

**Étape 3 :** Testez le endpoint de connexion avec `curl` :

Tout d'abord, testons le endpoint de connexion pour obtenir un JWT. Ouvrez un nouveau terminal et exécutez la commande suivante. La commande envoie une requête `POST` au endpoint `/login` avec `username: "admin"` dans le corps de la requête.

```bash
curl -X POST http://localhost:3000/login -H "Content-Type: application/json" -d '{"username": "admin"}'
```

Cela renverra un objet JSON avec un JWT. Copiez ce jeton pour l'étape suivante.

Maintenant, testons la route protégée. Nous utiliserons le jeton que nous venons de recevoir dans l'en-tête `Authorization`. Remplacez `<votre_token_jwt>` par le jeton que vous avez copié.

```bash
curl http://localhost:3000/api/protected -H "Authorization: Bearer <votre_token_jwt>"
```

Vous devriez recevoir un message de succès avec le payload décodé.

Enfin, testons la route avec cache. Vous devrez exécuter un build de production et lancer le fichier avec `node` pour que cela fonctionne.

Tout d'abord, exécutez la commande suivante. Le délai de `1000` millisecondes dans le code fera durer cette requête environ une seconde.

```bash
curl -o /dev/null -s -w 'Total: %{time_total}s\n' http://localhost:3000/api/public-data
```

Exécutez immédiatement **exactement la même commande à nouveau**. Cette fois, la réponse sera presque instantanée car notre middleware de cache personnalisé a servi la réponse directement depuis son stockage en mémoire, contournant complètement le `setTimeout` dans le gestionnaire de route. Exécutez-le une troisième fois, et vous verrez une réponse quasi instantanée similaire.

Voici un exemple de ce à quoi devrait ressembler la sortie de votre terminal lors du test du cache. La première requête a pris environ 1 seconde, mais les requêtes suivantes n'ont pris que quelques millisecondes.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757125753352/180cc4a7-f361-4966-a26f-a5d8251f77a4.png align="center")

### Comment créer un gestionnaire d'erreurs global

Vous pouvez définir un seul gestionnaire d'erreurs global avec `app.onError()`. C'est utile pour gérer les erreurs inattendues de manière centralisée, comme les échecs de validation.

Ajoutez le code suivant à votre `src/index.ts` :

```typescript
app.get('/users/:id', (c) => {
  const id = c.req.param('id')
  if (isNaN(Number(id))) {
    throw new Error('User ID must be a number.')
  }
  return c.text(`User ID is ${id}`)
})

app.onError((err, c) => {
  console.error(`${err}`)
  return c.json({
    success: false,
    message: err.message,
  }, 500)
})
```

Désormais, si vous visitez [`http://localhost:3000/users/abc`](http://localhost:3000/users/abc), vous obtiendrez une réponse d'erreur JSON au lieu d'une exception non gérée.

### Comment gérer la validation avec Zod

Pour des API robustes, la validation des données est essentielle. Hono s'intègre parfaitement avec [Zod](https://zod.dev/), une bibliothèque de validation de schéma populaire pensée pour TypeScript.

**Étape 1 :** Installez les dépendances nécessaires :

```bash
npm install zod @hono/zod-validator
```

**Étape 2 :** Remplacez `src/index.ts` par l'exemple de validation :

```typescript
import { Hono } from 'hono'
import { serve } from '@hono/node-server'
import { z } from 'zod'
import { zValidator } from '@hono/zod-validator'

const app = new Hono()

// Définition d'un schéma Zod pour les données de création d'utilisateur
const createUserSchema = z.object({
  username: z.string().min(3).max(20),
  email: z.string().email(),
  age: z.number().int().positive(),
  tags: z.array(z.string()).optional(),
})

app.post(
  '/users',
  zValidator('json', createUserSchema), // Utilisation du middleware zValidator
  (c) => {
    // Les données validées sont disponibles sur c.req.valid()
    const user = c.req.valid('json')
    console.log(`Creating user: ${user.username} with email ${user.email}`)
    return c.json({
      success: true,
      message: 'User created successfully!',
      user: user,
    }, 201)
  }
)

serve({ fetch: app.fetch, port: 3000 }, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})
```

Voici comment fonctionne la validation Zod :

1. Nous définissons d'abord un schéma appelé `createUserSchema` en utilisant `z.object()`. Ce schéma est un plan de la structure de données attendue. Nous utilisons les méthodes intégrées de Zod comme `z.string().min(3)`, `z.string().email()`, et `z.number().int().positive()` pour spécifier les règles de validation pour chaque propriété.
    
2. Nous appliquons ensuite le middleware [`zValidator`](https://github.com/honojs/middleware/tree/main/packages/zod-validator) à notre gestionnaire de route. Le premier argument, `'json'`, indique au middleware de valider le corps JSON de la requête entrante. Le deuxième argument, `createUserSchema`, lui indique quel schéma utiliser pour la validation.
    
3. Le middleware `zValidator` fait automatiquement le gros du travail. Lorsqu'une requête arrive sur le endpoint `/users`, il analyse le corps JSON et tente de le valider par rapport à `createUserSchema`. Si les données sont invalides (par exemple, si l'email n'est pas au bon format), le middleware arrête immédiatement la requête et renvoie un statut `400 Bad Request` avec un message d'erreur détaillé.
    
4. Si les données sont valides, le middleware les rend disponibles sur l'objet `Context`, auquel nous pouvons accéder avec `c.req.valid('json')`. Le système de types de Hono garantit que ces données sont correctement typées selon le schéma Zod.
    

**Étape 3 :** Exécutez `npm run dev`.

**Étape 4 :** Testez avec `curl` (données valides) :

```bash
curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d '{"username": "testuser", "email": "test@example.com", "age": 25}'
```

Cela renverra un message de succès.

Testez avec des données invalides (par exemple, un mauvais email) :

```bash
curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d '{"username": "testuser", "email": "invalid-email", "age": 25}'
```

Cela renverra automatiquement un statut `400` avec un message d'erreur détaillé de Zod.

### Comment créer une application Full-Stack avec JSX

Hono prend en charge le rendu côté serveur avec JSX, vous permettant de créer des applications full-stack sans avoir besoin d'un Framework séparé.

**Étape 1 :** Créez `src/components/Layout.tsx` :

```typescript
import { html } from 'hono/html'

export const Layout = (props: { title: string; children?: any }) => html`
  <!DOCTYPE html>
  <html>
    <head>
      <title>${props.title}</title>
      <style>
        body { font-family: sans-serif; background: #f4f4f4; color: #333; }
        .container { max-width: 800px; margin: 2rem auto; padding: 1rem; background: white; border-radius: 8px; }
        header { border-bottom: 1px solid #ccc; padding-bottom: 1rem; }
        footer { margin-top: 2rem; text-align: center; font-size: 0.8rem; color: #777; }
      </style>
    </head>
    <body>
      <div class="container">
        <header>
          <h1>${props.title}</h1>
        </header>
        <main>
          ${props.children}
        </main>
        <footer>
          <p>Powered by Hono</p>
        </footer>
      </div>
    </body>
  </html>
`
```

**Étape 2 :** Créez `src/components/PostItem.tsx` :

```typescript
export const PostItem = (props: { post: { id: number; title: string; author: string } }) => (
  <article style="border-bottom: 1px solid #eee; padding: 1rem 0;">
    <h3><a href={`/posts/${props.post.id}`}>{props.post.title}</a></h3>
    <p><em>By {props.post.author}</em></p>
  </article>
)
```

**Étape 3 :** Mettez à jour `src/index.tsx` :

```typescript
import { Hono } from 'hono'
import { serve } from '@hono/node-server'
import { Layout } from './components/Layout'
import { PostItem } from './components/PostItem'

const app = new Hono()

// Données fictives
const posts = [
  { id: 1, title: 'Getting Started with Hono', author: 'Alice' },
  { id: 2, title: 'Advanced Middleware Patterns', author: 'Bob' },
  { id: 3, title: 'Deploying Hono to the Edge', author: 'Charlie' },
]

app.get('/', (c) => {
  return c.html(
    <Layout title="My Hono Blog">
      <h2>Recent Posts</h2>
      {posts.length > 0
        ? posts.map(post => <PostItem post={post} />)
        : <p>No posts yet!</p>
      }
    </Layout>
  )
})

serve({ fetch: app.fetch, port: 3000 }, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})
```

Assurez-vous de mettre à jour le script `dev` dans votre fichier `package.json` pour avoir `src/index.tsx` comme point de départ.

```json
"dev": "tsx watch src/index.tsx"
```

**Étape 4 :** Exécutez `npm run dev` et visitez [`http://localhost:3000`](http://localhost:3000). Vous verrez une page de blog entièrement rendue avec la liste des articles.

![Page de blog avec liste d'articles](https://cdn.hashnode.com/res/hashnode/image/upload/v1756952439130/27ee63cc-6d60-4372-9634-4d1eadf33f32.png align="center")

## Guide de déploiement pour Hono

Vous avez construit votre application, et il est maintenant temps de la partager avec le monde. Voici comment vous pouvez déployer votre application Hono sur certaines des plateformes les plus populaires.

### Comment déployer sur Node.js

Pour un environnement serveur traditionnel, vous pouvez utiliser l'adaptateur `@hono/node-server` et un gestionnaire de processus comme `pm2` pour la production.

`src/index.ts` :

```typescript
import { serve } from '@hono/node-server'
import app from './app' // En supposant que votre application Hono soit dans app.ts

serve({ fetch: app.fetch, port: 3000 })
```

Vous compilerez ensuite votre TypeScript en JavaScript et exécuterez `pm2 start dist/index.js` pour le lancer en arrière-plan.

### Comment déployer sur Cloudflare Workers

La véritable force de Hono réside dans sa portabilité. La commande `create hono` peut configurer un projet spécifiquement pour Cloudflare Workers.

Exécutez la commande suivante et sélectionnez le template `cloudflare-workers` :

```bash
npm create hono@latest my-app-hono-cloudflare-worker

create-hono version 0.19.2
✔ Using target directory … my-app-hono-cloudflare-worker
? Which template do you want to use?
  aws-lambda
  bun
❯ cloudflare-workers
  cloudflare-workers+vite
  deno
  fastly
  lambda-edge
```

Le processus de configuration est identique à l'exemple Node.js, mais la structure du projet est optimisée pour Cloudflare.

Une fois le projet configuré, il ne vous reste plus qu'à taper une commande pour déployer votre application sur Cloudflare :

```bash
wrangler deploy
```

Cette commande vous invitera à vous connecter à votre compte Cloudflare et gérera automatiquement l'ensemble du processus de déploiement.

## **Conclusion**

Vous y êtes arrivé ! Nous avons couvert beaucoup de choses dans ce guide. Vous avez commencé par la configuration d'un projet professionnel et avez progressé jusqu'au routage avancé, à la gestion du contexte, aux modèles de middleware complexes, à la validation robuste des données et aux composants JSX full-stack.

Vous possédez désormais les connaissances et les outils nécessaires pour créer des applications sérieuses et prêtes pour la production avec Hono. Son API simple ne limite pas sa puissance. Au contraire, elle l'améliore en s'effaçant pour vous laisser vous concentrer sur la création de fonctionnalités exceptionnelles. Et grâce à sa portabilité, vous pouvez être certain que l'application que vous construisez aujourd'hui pourra être déployée sur les plateformes de demain.

L'écosystème du développement web continuera d'évoluer, mais en s'appuyant sur les Standards Web, Hono est un Framework conçu pour durer.

Pour poursuivre votre voyage, je vous recommande vivement d'explorer la [documentation officielle de Hono](https://hono.dev/docs/), qui regorge de guides et d'exemples supplémentaires.