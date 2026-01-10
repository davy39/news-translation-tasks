---
title: Comment déployer une API Next.js avec PostgreSQL et Sevalla
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-08-18T13:54:12.097Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-nextjs-api-with-postgresql-and-sevalla
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755525213723/75759868-d5e9-4ea7-a6be-22bc33dde0d8.png
tags:
- name: Next.js
  slug: nextjs
- name: PostgreSQL
  slug: postgresql
- name: APIs
  slug: apis
seo_title: Comment déployer une API Next.js avec PostgreSQL et Sevalla
seo_desc: 'When developers think of Next.js, they often associate it with SEO-friendly
  static websites or React-based frontends. But what many miss is how Next.js can
  also be used to build full-featured backend APIs – all within the same project.

  I’ve recently ...'
---

Lorsque les développeurs pensent à Next.js, ils l'associent souvent à des sites Web statiques optimisés pour le SEO ou à des frontends basés sur React. Mais ce que beaucoup ignorent, c'est comment Next.js peut également être utilisé pour créer des API backend complètes – le tout au sein du même projet.

J'ai [récemment écrit un article](https://www.freecodecamp.org/news/how-to-deploy-a-nextjs-api-to-production-using-sevalla/) sur l'utilisation de l'API Next.js et son déploiement en production. Dans ce cas, j'aurais utilisé un fichier JSON comme mini-base de données.

Mais le format JSON ou tout autre type de stockage de fichiers n'est pas adapté à une application en production. En effet, le stockage basé sur des fichiers n'est pas conçu pour un accès concurrent ; ainsi, plusieurs utilisateurs écrivant des données en même temps peuvent provoquer une corruption ou une perte de données.

Il manque également de capacités d'indexation et de requête, ce qui le rend lent à mesure que les données augmentent. Les sauvegardes, la sécurité et l'évolutivité sont également plus difficiles à gérer par rapport à une véritable base de données.

En résumé, si les fichiers JSON fonctionnent pour des démos ou des prototypes, les systèmes de production ont besoin d'une base de données capable de gérer la concurrence, de grands ensembles de données, des requêtes complexes et une persistance fiable.

Dans cet article, nous allons donc voir comment construire une API REST avec Next.js, stocker des données dans une base de données gérée par Sevalla, et déployer l'intégralité du projet en production en utilisant l'[infrastructure PaaS](https://www.freecodecamp.org/news/vps-vs-paas-how-to-choose-a-hosting-solution/) de Sevalla.

## Table des matières

* [Qu'est-ce que Next.js ?](#heading-qu-est-ce-que-nextjs)
    
* [Installation et configuration](#heading-installation-et-configuration)
    
* [Comment construire une API Next.js](#heading-comment-construire-une-api-nextjs)
    
* [Provisionnement d'une base de données dans Sevalla](#heading-provisionnement-d-une-base-de-donnees-dans-sevalla)
    
* [Déploiement sur Sevalla](#heading-deploiement-sur-sevalla)
    
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce que Next.js ?**

[Next.js](https://nextjs.org/) est un Framework React open-source développé par Vercel. Il est connu pour le rendu côté serveur (server-side rendering), la génération statique et le routage fluide. Mais au-delà de ses super-pouvoirs frontend, il permet aux développeurs de construire une logique backend et des API via son système de routage basé sur les fichiers. Cela fait de Next.js un excellent choix pour construire des applications full-stack.

## **Installation et configuration**

Pour commencer, assurez-vous que Node.js et NPM sont installés.

```bash
$ node --version
v22.16.0

$ npm --version
10.9.2
```

Maintenant, créez un nouveau projet Next.js :

```bash
npx create-next-app@latest
```

Le résultat de la commande ci-dessus vous posera une série de questions pour configurer votre application :

```plaintext
What is your project named? my-app
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to use Turbopack for `next dev`?  No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```

Mais pour ce tutoriel, nous ne sommes pas intéressés par une application full-stack – juste une API. Recréons donc l'application en utilisant le flag `--api`.

```plaintext
$ npx create-next-app@latest --api
```

Il vous posera encore quelques questions. Utilisez les paramètres par défaut et terminez la création de l'application.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1754476744959/9f1d2763-7df5-491b-8cb3-05161b35fbd9.webp align="center")

Une fois la configuration terminée, vous pouvez voir le dossier portant le nom de votre application. Entrons dans le dossier et lançons l'application.

```plaintext
$ npm run dev
```

Votre modèle d'API devrait fonctionner sur le port 3000. Allez sur [http://localhost:3000](http://localhost:3000/) et vous devriez voir le message suivant :

```plaintext
{
"message": "Hello world!"
}
```

## **Comment construire une API Next.js**

Maintenant que nous avons configuré notre modèle d'API, écrivons une API REST de base avec deux points de terminaison (endpoints) : un pour créer des données et un pour consulter les données.

Le code de l'API résidera sous `/app` dans le répertoire du projet. Next.js utilise le routage basé sur les fichiers pour construire les chemins URL.

Par exemple, si vous voulez un chemin URL `/users`, vous devriez avoir un répertoire appelé "users" avec un fichier `route.ts` pour gérer toutes les opérations CRUD pour `/users`. Pour `/users/:id`, vous devriez avoir un répertoire appelé `[id]` sous le répertoire "users" avec un fichier `route.ts`. Les crochets servent à indiquer à Next.js que vous attendez des valeurs dynamiques pour la route `/users/:id`.

Voici une capture d'écran de la configuration. Supprimez le répertoire `[slug]` qui accompagne le projet car il ne sera pas pertinent pour nous.

![Configuration des dossiers](https://cdn.hashnode.com/res/hashnode/image/upload/v1754479396056/a80a0fd3-707d-4813-b402-041561354c94.png align="center")

* Le fichier `route.ts` à la base gère les opérations CRUD pour `/` (c'est de là que la réponse "hello world" a été générée).
    
* Le fichier `route.ts` sous `/users` gère les opérations CRUD pour `/users`.
    

Bien que cette configuration puisse sembler compliquée pour un projet simple, elle offre une structure claire pour les applications Web à grande échelle. Si vous voulez approfondir la création d'API complexes avec Next.js, [voici un tutoriel](https://nextjs.org/blog/building-apis-with-nextjs) que vous pouvez suivre.

Le code sous `/app/route.ts` est le fichier par défaut de notre API. Vous pouvez le voir servir la requête GET et répondre par "Hello World!" :

```plaintext
import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({ message: "Hello world!" });
}
```

Nous avons maintenant besoin de deux routes :

* GET `/users` qui liste tous les utilisateurs
    
* POST `/users` qui crée un nouvel utilisateur
    

Pour ce projet, nous utiliserons une base de données pour stocker nos enregistrements. Nous n'allons pas installer de base de données sur notre machine locale. Au lieu de cela, nous allons provisionner la base de données dans le cloud et l'utiliser avec notre API. Cette approche est courante dans les environnements de test / prod pour garantir la cohérence des données.

## Provisionnement d'une base de données dans Sevalla

[Sevalla](https://sevalla.com/) est un fournisseur de Platform-as-a-service moderne, basé sur l'utilisation, et une alternative à des sites comme Heroku ou à votre propre installation gérée sur AWS. Il combine des fonctionnalités puissantes avec une expérience développeur fluide.

Sevalla propose l'hébergement d'applications, de bases de données, de stockage d'objets et d'hébergement de sites statiques pour vos projets. Il dispose d'une offre gratuite généreuse, nous l'utiliserons donc pour nous connecter à une base de données ainsi que pour déployer notre application dans le cloud.

Si vous êtes nouveau sur Sevalla, vous pouvez vous [inscrire](https://sevalla.com/signup/) en utilisant votre compte GitHub pour activer les déploiements directs depuis votre GitHub. Chaque fois que vous pousserez du code vers votre projet, Sevalla récupérera automatiquement et déploiera votre application dans le cloud.

Une fois connecté à Sevalla, cliquez sur "Databases".

![Bases de données Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1754477578430/7b7fa655-0f35-4901-90be-07bd5abdf2c0.png align="center")

Maintenant, créons une base de données [PostgreSQL](https://www.freecodecamp.org/news/posgresql-course-for-beginners/).

![Créer une base de données Postgresql](https://cdn.hashnode.com/res/hashnode/image/upload/v1754477639118/d6ea82ae-45c9-40a7-bcf5-d144885db929.png align="center")

Utilisez les paramètres par défaut. Une fois la base de données créée, elle désactivera par défaut les connexions externes par sécurité pour s'assurer que personne en dehors de notre serveur ne puisse s'y connecter. Puisque nous voulons tester notre connexion depuis notre machine locale, activons une connexion externe.

![Paramètres de la base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1754479205197/58c01504-59c0-4df3-b9f9-cb14e1431135.png align="center")

La valeur dont nous avons besoin pour nous connecter à la base de données depuis notre point de terminaison local est l'"url" sous la connexion externe. Créez un fichier appelé `.env` dans le projet et collez l'URL au format suivant :

```typescript
PGSQL_URL=postgres://<username>:<password>-@asia-east1-001.proxy.kinsta.app:30503/<db_name>
```

La raison pour laquelle nous utilisons `.env` est de stocker des variables d'environnement spécifiques à l'environnement. En production, nous n'aurons pas besoin de ce fichier (ne poussez jamais les fichiers `.env` sur GitHub). Sevalla nous donnera l'option d'ajouter des variables d'environnement via l'interface graphique lors du déploiement de l'application.

Maintenant, testons la connexion à notre base de données. Installez le paquet `pg` pour Node afin d'interagir avec PostgreSQL. Installons également l'extension TypeScript pour `pg` pour prendre en charge les définitions TypeScript.

```typescript
$ npm i pg
$ npm install --save-dev @types/pg
```

Modifiez le fichier `route.ts` qui servait "hello world" par celui-ci :

```typescript
// app/api/your-endpoint/route.ts
import { NextResponse } from "next/server";
import { Client } from "pg";

export async function GET() {
  const client = new Client({
    connectionString: process.env.PGSQL_URL,
  });

  try {
    await client.connect();
    await client.end();
    return NextResponse.json({ message: "Connecté à la base de données" });
  } catch (error) {
    console.error("Erreur de connexion à la base de données :", error);
    return NextResponse.json({ message: "La connexion a échoué" }, { status: 500 });
  }
}
```

Maintenant, lorsque vous lancez votre application et allez sur `localhost:3000`, elle devrait afficher "connecté à la base de données".

![Connexion Postgresql réussie](https://cdn.hashnode.com/res/hashnode/image/upload/v1754485714515/c63f11fc-2310-462a-9b42-c0528e500637.png align="center")

Excellent. Maintenant, écrivons nos deux routes, une pour créer des données et l'autre pour consulter les données créées. Utilisez ce code sous `users/route.ts` :

```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { Client } from "pg";

// Définition de la structure d'un objet Utilisateur
interface User {
  id: string;
  name: string;
  email: string;
  age: number;
}

// Création d'un client PostgreSQL
function getClient() {
  return new Client({
    connectionString: process.env.PGSQL_URL,
  });
}

// Récupération de tous les utilisateurs de la base de données
async function readUsers(): Promise<User[]> {
  const client = getClient();
  await client.connect();

  try {
    const result = await client.query("SELECT id, name, email, age FROM users");
    return result.rows;
  } finally {
    await client.end();
  }
}

// Insertion ou mise à jour des utilisateurs dans la base de données
async function writeUsers(users: User[]) {
  const client = getClient();
  await client.connect();

  try {
    const insertQuery = `
      INSERT INTO users (id, name, email, age)
      VALUES ($1, $2, $3, $4)
      ON CONFLICT (id) DO UPDATE SET
        name = EXCLUDED.name,
        email = EXCLUDED.email,
        age = EXCLUDED.age;
    `;

    for (const user of users) {
      await client.query(insertQuery, [user.id, user.name, user.email, user.age]);
    }
  } finally {
    await client.end();
  }
}

// Gestion de la requête GET : retourne la liste des utilisateurs
export async function GET() {
  try {
    const users = await readUsers();
    return NextResponse.json(users);
  } catch (err) {
    console.error("Erreur lors de la lecture des utilisateurs depuis la BDD :", err);
    return NextResponse.json({ error: "Échec de la récupération des utilisateurs" }, { status: 500 });
  }
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const users: User[] = Array.isArray(body) ? body : [body];

    await writeUsers(users);

    return NextResponse.json({ success: true, count: users.length });
  } catch (err) {
    console.error("Erreur lors de l'écriture des utilisateurs dans la BDD :", err);
    return NextResponse.json({ error: "Échec de l'écriture des utilisateurs" }, { status: 500 });
  }
}
```

Maintenant, lorsque vous allez sur `localhost:3000/users`, cela vous donnera une erreur car la table `users` n'existe pas encore. Créons-en une.

Dans l'interface de la base de données, cliquez sur "Studio". Vous obtiendrez un éditeur visuel pour votre base de données où vous pourrez gérer vos données directement (plutôt cool, non ?).

![Studio de base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1754486852876/2437c76a-562a-4575-9cc0-a5f563aa6206.png align="center")

Appuyez sur l'icône "+" et choisissez "create table". Créez la table avec le schéma ci-dessous. Cliquez sur le lien "add column" pour créer de nouvelles colonnes.

![Schéma de la base de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1754487097219/9d01d9b7-e3c6-427b-9b42-c97065826af7.png align="center")

Cliquez sur "create table" et vous devriez voir la table créée comme ci-dessous :

![Table des utilisateurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1754487162119/c64e0577-d094-4549-85f4-ab8c8d15f48e.png align="center")

Ajoutons un enregistrement fictif en utilisant le bouton "add record" pour tester notre API. Le champ `id` doit être au format UUID (et vous pouvez [en générer un ici](https://www.uuidgenerator.net/)).

Maintenant, testons notre API.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1754487408705/3fd9784e-3a83-415d-870f-f3f5d23dec51.png align="center")

Vous devriez voir l'utilisateur que vous avez créé comme réponse à la requête `localhost:3000/users`. Maintenant, créons un nouvel utilisateur via notre API.

Nous utiliserons [Postman](https://www.postman.com/) pour cela car il est facile de créer des requêtes POST avec Postman. Nous enverrons des données d'exemple sous "body" → "raw" → "JSON".

![Requête Post](https://cdn.hashnode.com/res/hashnode/image/upload/v1754543941765/a77be1b8-05c3-4c61-a5c3-f7f0fbf48b4d.png align="center")

La réponse de Postman devrait être la suivante :

![Résultats Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1754544001954/5a52331c-a445-4b10-8c4b-9337ca873c13.png align="center")

Maintenant, en allant sur `localhost:3000/users`, vous devriez voir le nouvel enregistrement créé.

![Get /users](https://cdn.hashnode.com/res/hashnode/image/upload/v1754544086690/8c4533c6-4250-42e1-a850-b52c460775fc.png align="center")

Beau travail ! Maintenant, mettons cette application en ligne.

## Déploiement sur Sevalla

Poussez votre code sur GitHub ou [forkez mon dépôt](https://github.com/manishmshiva/nextjs-api-pgsql). Allez maintenant sur Sevalla et créez une nouvelle application.

![Sevalla créer une application](https://cdn.hashnode.com/res/hashnode/image/upload/v1754545093624/9747a06d-0dcf-482a-89b9-732b9937b1dc.png align="center")

Choisissez votre dépôt dans la liste déroulante et cochez "Automatic deployment on commit". Cela garantira que le déploiement est automatique chaque fois que vous poussez du code (Commit). Choisissez "Hobby" sous la section des ressources.

![Sevalla créer une nouvelle application](https://cdn.hashnode.com/res/hashnode/image/upload/v1754545136001/dde5fe4d-4691-401c-a3ef-959b8e53f62a.png align="center")

Cliquez sur "Create" et non sur "Create and deploy". Nous n'avons pas encore ajouté notre URL PostgreSQL en tant que variable d'environnement, l'application planterait donc si vous essayiez de la déployer.

Allez dans la section "Environment variables" et ajoutez la clé "PGSQL\_URL" et l'URL dans le champ de valeur.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1754545371348/7525c6cd-63af-40b2-80c5-6b49b6101f19.png align="center")

Maintenant, retournez dans la section "Overview" et cliquez sur "Deploy now".

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1754545664510/c3f12f86-0732-4518-bf51-4867ac86abdd.png align="center")

Une fois le déploiement terminé, cliquez sur "Visit app" pour obtenir l'URL en direct de votre API. Vous pouvez remplacer `localhost:3000` par la nouvelle URL dans Postman et tester votre API.

Félicitations – votre application est maintenant en ligne. Vous pouvez faire plus avec votre application en utilisant l'interface d'administration, comme :

* Surveiller les performances de votre application
    
* Consulter les logs en temps réel
    
* Ajouter des domaines personnalisés
    
* Mettre à jour les paramètres réseau (ouvrir/fermer des ports pour la sécurité, etc.)
    
* Ajouter plus de stockage
    

## **Conclusion**

Next.js n'est plus seulement un Framework frontend. C'est une plateforme full-stack puissante qui vous permet de construire et de déployer des API prêtes pour la production avec un minimum de friction. En l'associant à l'infrastructure conviviale de Sevalla, vous pouvez passer du développement local à une API hébergée dans le cloud en quelques minutes.

Dans ce tutoriel, vous avez appris à configurer un projet d'API Next.js, à le connecter à une base de données PostgreSQL hébergée sur le cloud de Sevalla et à tout déployer de manière fluide. Que vous construisiez un petit projet personnel ou une application à grande échelle, cette pile technologique vous offre la rapidité, la structure et l'évolutivité nécessaires pour avancer vite sans perdre en flexibilité.

J'espère que vous avez apprécié cet article. À bientôt pour un prochain tutoriel. Vous pouvez [me contacter ici](https://manishshivanandhan.com/) ou [visiter mon blog](https://blog.manishshivanandhan.com/).