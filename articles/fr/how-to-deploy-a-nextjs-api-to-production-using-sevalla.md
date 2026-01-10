---
title: Comment déployer une API Next.js en production avec Sevalla
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-08-01T23:14:57.805Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-nextjs-api-to-production-using-sevalla
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754090039728/75b0f680-94b4-4310-9c52-109000acde22.png
tags:
- name: Next.js
  slug: nextjs
- name: Web Development
  slug: web-development
- name: JavaScript
  slug: javascript
- name: deployment
  slug: deployment
seo_title: Comment déployer une API Next.js en production avec Sevalla
seo_desc: 'When people hear about Next.js, they often think of server-side rendering,
  React-powered frontends, or SEO-optimised static websites. But there''s more to
  this powerful framework than just front-end development.

  Next.js also allows developers to build...'
---

Lorsque les gens entendent parler de Next.js, ils pensent souvent au rendu côté serveur, aux frontends alimentés par React ou aux sites statiques optimisés pour le SEO. Mais ce framework puissant offre bien plus que le simple développement frontend.

Next.js permet également aux développeurs de créer des API backend robustes et évolutives directement dans la même base de code. Cela est particulièrement précieux pour les applications de petite à moyenne taille où un frontend et un backend étroitement couplés accélèrent le développement et le déploiement.

Dans cet article, vous apprendrez à créer une API avec Next.js et à la déployer en production avec Sevalla. Il est relativement facile d'apprendre à construire quelque chose en suivant un tutoriel, mais le vrai défi est de le mettre entre les mains des utilisateurs. Cela transforme votre projet d'un prototype local en quelque chose de réel et d'utilisable.

## Table des matières

* [Qu'est-ce que Next.js ?](#heading-qu-est-ce-que-nextjs)

* [Installation et configuration](#heading-installation-et-configuration)

* [Comment créer une API REST](#heading-comment-creer-une-api-rest)

* [Comment tester l'API](#heading-comment-tester-l-api)

* [Comment déployer sur Sevalla](#heading-comment-deployer-sur-sevalla)

* [Conclusion](#heading-conclusion)

## **Qu'est-ce que Next.js ?**

[Next.js](https://nextjs.org/) est un framework React open-source développé par Vercel. Il permet aux développeurs de créer des applications web avec rendu côté serveur et génération statique.

Il abstrait essentiellement la configuration et le code boilerplate nécessaires pour exécuter une application React full-stack, facilitant ainsi la tâche des développeurs pour se concentrer sur la création de fonctionnalités plutôt que sur la configuration de l'infrastructure.

Bien qu'il ait commencé comme une solution pour les défis frontend de React, il a évolué vers un framework full-stack qui permet de gérer la logique backend, d'interagir avec des bases de données et de créer des API. Cette base de code unifiée est ce qui rend Next.js particulièrement attrayant pour le développement web moderne.

## Installation et configuration

Installons Next.js. Assurez-vous d'avoir [Node.js](https://nodejs.org/en) et NPM installés sur votre système, et qu'ils sont à jour.

```plaintext
$ node --version
v22.16.0

$ npm --version
10.9.2
```

Maintenant, créons un projet Next.js. La commande à utiliser est :

```plaintext
$ npx create-next-app@latest
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

Mais pour ce tutoriel, nous ne sommes pas intéressés par une application full-stack, juste par une API. Donc, recréons l'application en utilisant le flag `--api`.

```plaintext
$ npx create-next-app@latest --api
```

Il vous posera encore quelques questions. Utilisez les paramètres par défaut et terminez la création de l'application.

![Configuration de l'API Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1753245601007/61b34b8f-0426-4bf1-80ed-315f97e18d8a.png align="center")

Une fois la configuration terminée, vous pouvez voir le dossier avec le nom de votre application. Entrons dans le dossier et exécutons l'application.

```plaintext
$ npm run dev
```

Votre modèle d'API devrait s'exécuter sur le port 3000. Allez sur [http://localhost:3000](http://localhost:3000/) et vous devriez voir le message suivant :

```plaintext
{
"message": "Hello world!"
}
```

## Comment créer une API REST

Maintenant que nous avons configuré notre modèle d'API, écrivons une API REST basique. Une API REST basique est simplement composée de quatre endpoints : Create, Read, Update, Delete (également appelés CRUD).

Habituellement, nous utiliserions une base de données, mais pour simplifier, nous utiliserons un fichier JSON dans notre API. Notre objectif est de créer une API REST qui peut lire et écrire dans ce fichier JSON.

Le code de l'API résidera sous /app dans le répertoire du projet. Next.js utilise un routage basé sur les fichiers pour construire les chemins d'URL.

Par exemple, si vous voulez un chemin d'URL /users, vous devez avoir un répertoire appelé "users" avec un fichier route.ts pour gérer toutes les opérations CRUD pour /users. Pour /users/:id, vous devez avoir un répertoire appelé \[id\] sous le répertoire "users" avec un fichier route.ts. Les crochets sont là pour indiquer à Next.js que vous attendez des valeurs dynamiques pour la route /users/:id.

Vous devez également avoir le fichier users.json à l'intérieur du répertoire /app/users pour que vos routes puissent lire et écrire des données.

Voici une capture d'écran de la configuration. Supprimez le répertoire \[slug\] qui vient avec le projet car il ne sera pas pertinent pour nous :

![Structure des routes](https://cdn.hashnode.com/res/hashnode/image/upload/v1753419862976/1ac6e871-6837-44e9-a02e-4e8d37ac4c76.png align="center")

* Le fichier route.ts en bas gère les opérations CRUD pour /

* Le fichier route.ts sous /users gère les opérations CRUD pour /users

* Le fichier route.ts sous /users/\[id\]/ gère les opérations CRUD sous /users/:id où l'"id" sera une valeur dynamique.

* Le fichier users.json sous /users sera notre stockage de données.

Bien que cette configuration puisse sembler compliquée pour un projet simple, elle fournit une structure claire pour les applications web à grande échelle. Si vous souhaitez approfondir la création d'API complexes avec Next.js, [voici un tutoriel](https://nextjs.org/blog/building-apis-with-nextjs) que vous pouvez suivre.

Le code sous /app/route.ts est le fichier par défaut pour notre API. Vous pouvez voir qu'il sert la requête GET et répond avec "Hello World!" :

```plaintext
import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({ message: "Hello world!" });
}
```

Maintenant, nous avons besoin de cinq routes :

* GET /users → Lister tous les utilisateurs

* GET /users/:id → Lister un seul utilisateur

* POST /users → Créer un nouvel utilisateur

* PUT /users/:id → Mettre à jour un utilisateur existant

* DELETE /users/:id → Supprimer un utilisateur existant

Voici le code pour le fichier route.ts sous /app/users :

```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { promises as fs } from "fs"; // Importation des méthodes de système de fichiers basées sur les promesses
import path from "path"; // Pour gérer les chemins de fichiers

// Définir la structure d'un objet User
interface User {
  id: string;
  name: string;
  email: string;
  age: number;
}

// Définir le chemin vers le fichier users.json
const usersFile = path.join(process.cwd(), "app/users/users.json");

// Lire les utilisateurs depuis le fichier JSON et les retourner sous forme de tableau
async function readUsers(): Promise<User[]> {
  try {
    const data = await fs.readFile(usersFile, "utf-8");
    return JSON.parse(data) as User[];
  } catch {
    // Si le fichier n'existe pas ou ne peut pas être lu, retourner un tableau vide
    return [];
  }
}

// Écrire le tableau des utilisateurs mis à jour dans le fichier JSON
async function writeUsers(users: User[]) {
  await fs.writeFile(usersFile, JSON.stringify(users, null, 2), "utf-8");
}

// Gérer la requête GET : retourner la liste des utilisateurs
export async function GET() {
  const users = await readUsers();
  return NextResponse.json(users);
}

// Gérer la requête POST : ajouter un nouvel utilisateur
export async function POST(request: NextRequest) {
  const body = await request.json();

  // Déstructurer et valider les champs d'entrée
  const { name, email, age } = body as {
    name?: string;
    email?: string;
    age?: number;
  };

  // Retourner 400 si un champ requis est manquant
  if (!name || !email || age === undefined) {
    return NextResponse.json(
      { error: "Missing name, email, or age" },
      { status: 400 }
    );
  }

  // Lire les utilisateurs existants
  const users = await readUsers();

  // Créer un nouvel objet utilisateur avec un ID unique basé sur le timestamp
  const newUser: User = {
    id: Date.now().toString(),
    name,
    email,
    age,
  };

  // Ajouter le nouvel utilisateur à la liste et sauvegarder dans le fichier
  users.push(newUser);
  await writeUsers(users);

  // Retourner l'utilisateur nouvellement créé avec le statut 201 Created
  return NextResponse.json(newUser, { status: 201 });
}
```

Maintenant, le code pour le fichier /app/users/\[id\]/route.ts :

```typescript
import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { promises as fs } from "fs";
import path from "path";

// Définir l'interface User
interface User {
  id: string;
  name: string;
  email: string;
  age: number;
}

// Chemin vers le fichier users.json
const usersFile = path.join(process.cwd(), "app/users/users.json");

// Fonction pour lire les utilisateurs depuis le fichier JSON
async function readUsers(): Promise<User[]> {
  try {
    const data = await fs.readFile(usersFile, "utf-8");
    return JSON.parse(data) as User[];
  } catch {
    // Si le fichier n'existe pas ou est illisible, retourner un tableau vide
    return [];
  }
}

// Fonction pour écrire les utilisateurs mis à jour dans le fichier JSON
async function writeUsers(users: User[]) {
  await fs.writeFile(usersFile, JSON.stringify(users, null, 2), "utf-8");
}

// GET /users/:id - Récupérer un utilisateur par ID
export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> },
) {
  const id = (await params).id;
  const users = await readUsers();

  // Trouver l'utilisateur par ID
  const user = users.find((u) => u.id === id);

  // Retourner 404 si l'utilisateur n'est pas trouvé
  if (!user) {
    return NextResponse.json({ error: "User not found" }, { status: 404 });
  }

  // Retourner l'utilisateur trouvé
  return NextResponse.json(user);
}

// PUT /users/:id - Mettre à jour un utilisateur par ID
export async function PUT(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> },
) {
  const id = (await params).id;
  const body = await request.json();

  // Extraire les champs optionnels du corps de la requête
  const { name, email, age } = body as {
    name?: string;
    email?: string;
    age?: number;
  };

  const users = await readUsers();

  // Trouver l'index de l'utilisateur à mettre à jour
  const index = users.findIndex((u) => u.id === id);

  // Retourner 404 si l'utilisateur n'est pas trouvé
  if (index === -1) {
    return NextResponse.json({ error: "User not found" }, { status: 404 });
  }

  // Mettre à jour l'utilisateur uniquement avec les champs fournis
  users[index] = {
    ...users[index],
    ...(name !== undefined ? { name } : {}),
    ...(email !== undefined ? { email } : {}),
    ...(age !== undefined ? { age } : {}),
  };

  await writeUsers(users);

  // Retourner l'utilisateur mis à jour
  return NextResponse.json(users[index]);
}

// DELETE /users/:id - Supprimer un utilisateur par ID
export async function DELETE(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> },
) {
  const id = (await params).id;
  const users = await readUsers();

  // Trouver l'index de l'utilisateur à supprimer
  const index = users.findIndex((u) => u.id === id);

  // Retourner 404 si l'utilisateur n'est pas trouvé
  if (index === -1) {
    return NextResponse.json({ error: "User not found" }, { status: 404 });
  }

  // Supprimer l'utilisateur du tableau et sauvegarder la liste mise à jour
  const [deleted] = users.splice(index, 1);
  await writeUsers(users);

  // Retourner l'utilisateur supprimé
  return NextResponse.json(deleted);
}
```

Nous aurons un tableau vide dans le fichier /app/users.json. Vous pouvez trouver tout le code ici [dans ce dépôt](https://github.com/manishmshiva/nextjs-api).

## Comment tester l'API

Maintenant, testons les endpoints de l'API.

Tout d'abord, exécutons l'API :

```typescript
$ npm run dev
```

Vous pouvez aller sur [http://localhost:3000/users](http://localhost:3000/users) et voir un tableau vide puisque nous n'avons pas encore ajouté d'informations d'utilisateur.

D'après le code, nous pouvons voir qu'un objet utilisateur a besoin de name, email et age puisque l'id est généré automatiquement dans l'endpoint POST.

![Création d'un nouvel utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1753336220369/11fceed9-6b2e-45f7-a5f9-2159d85e3cfb.png align="center")

Nous utiliserons [Postman](https://www.postman.com/downloads/) pour simuler des requêtes vers l'API et nous assurer que l'API se comporte comme prévu.

1. GET /users : il sera vide lors de notre première tentative puisque nous n'avons pas encore ajouté de données.

![GET /users](https://cdn.hashnode.com/res/hashnode/image/upload/v1753340954122/794e41d4-2660-49de-8bff-dbd979979049.png align="center")

2. POST /users : créer un nouvel utilisateur. Sous "body", choisissez "raw" et sélectionnez "JSON". Ce sont les données que nous allons envoyer à l'API. Le corps JSON serait :

```typescript
{"name":"Manish","age":30, "email":"manish@example.com"}
```

![POST /users](https://cdn.hashnode.com/res/hashnode/image/upload/v1753341103739/96f42da7-127c-4e99-9cd2-054d8bb74633.png align="center")

Je vais créer un autre enregistrement nommé "Larry". Voici le JSON :

```typescript
{"name":"Larry","age":25, "email":"larrry@example.com"}
```

Maintenant, regardons les utilisateurs. Vous devriez voir deux entrées pour notre requête GET à /users :

![GET /users](https://cdn.hashnode.com/res/hashnode/image/upload/v1753341200059/e4237349-9fc6-4424-965a-f4dc2d2cda3f.png align="center")

Maintenant, regardons un seul utilisateur en utilisant /users/:id.

![GET /users/:id](https://cdn.hashnode.com/res/hashnode/image/upload/v1753341556154/8dda05a1-7a83-40a2-b212-cd5ccb54f0a3.png align="center")

Maintenant, mettons à jour l'âge de Larry à 35. Nous allons passer uniquement l'âge dans le corps de la requête en utilisant la requête PUT à /users/:id.

![PUT /users/:id](https://cdn.hashnode.com/res/hashnode/image/upload/v1753341614641/a5a7ffbd-a371-42f9-9a32-285aeec39066.png align="center")

Maintenant, supprimons l'enregistrement de Larry.

![DELETE /users/:id](https://cdn.hashnode.com/res/hashnode/image/upload/v1753341668605/9456cf8d-e694-4d1d-968e-3ab9a9c6c30e.png align="center")

Si vous vérifiez /users, vous devriez voir un seul enregistrement :

![GET /users](https://cdn.hashnode.com/res/hashnode/image/upload/v1753341735968/d0b6ecf9-34e4-49a2-b6e1-da0ab859a8b3.png align="center")

Nous avons donc construit et testé notre API. Maintenant, mettons-la en ligne.

## Comment déployer sur Sevalla

[Sevalla](https://sevalla.com/) est un fournisseur moderne de Plateforme-en-tant-que-Service (PaaS) basé sur l'utilisation, et une alternative aux sites comme Heroku ou à votre configuration auto-gérée sur AWS. Il combine des fonctionnalités puissantes avec une expérience développeur fluide.

Sevalla offre l'hébergement d'applications, la base de données, le stockage d'objets et l'hébergement de sites statiques pour vos projets. Il vient avec un niveau gratuit généreux, alors voyons comment déployer notre API dans le cloud en utilisant Sevalla.

Assurez-vous d'avoir le code validé sur GitHub ou [forker mon dépôt](https://github.com/manishmshiva/nextjs-api) pour ce projet. Si vous êtes nouveau sur Sevalla, vous pouvez vous inscrire en utilisant votre compte GitHub pour activer les déploiements directs depuis votre compte GitHub. Chaque fois que vous poussez du code vers votre projet, Sevalla le récupérera automatiquement et déployera votre application dans le cloud.

Une fois que vous êtes [connecté](https://app.sevalla.com/login) à Sevalla, cliquez sur "Applications". Maintenant, créons une application.

![Interface de l'application Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1753420176622/a96c398e-18bc-42c2-917a-ba6a4f9ed585.png align="center")

Si vous vous êtes authentifié avec GitHub, l'interface de création d'application affichera une liste de dépôts. Choisissez celui dans lequel vous avez poussé votre code ou le projet nextjs-api si vous l'avez forké depuis mon dépôt.

![Connecter le dépôt](https://cdn.hashnode.com/res/hashnode/image/upload/v1753420351315/cc8b072b-fda8-43d5-a56b-9e3dd623523d.png align="center")

Cochez la case "auto deploy on commit". Cela garantira que votre dernier code est automatiquement déployé sur Sevalla. Maintenant, choisissons l'instance sur laquelle nous pouvons déployer l'application. Chacune a son propre prix, basé sur la capacité du serveur.

Choisissons le serveur hobby qui coûte 5 $/mois. Sevalla nous offre un niveau gratuit de 50 $, donc nous n'avons rien à payer à moins de dépasser ce niveau d'utilisation.

![Niveau d'utilisation de Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1753420434828/71cb0e8e-832a-4077-b493-6928c874eb4b.png align="center")

Maintenant, cliquez sur "Create and Deploy". Cela devrait récupérer notre code depuis notre dépôt, exécuter le processus de construction, configurer un conteneur Docker et ensuite déployer l'application. Habituellement le travail d'un administrateur système, entièrement automatisé par Sevalla.

Attendez quelques minutes pour que tout cela se produise. Vous pouvez suivre les logs dans l'interface "Deployments".

![Déploiement de l'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1753424002440/8dc98179-15f2-4178-b285-23f0f475bc66.png align="center")

Maintenant, cliquez sur "Visit App" et vous obtiendrez l'URL live (se terminant par sevalla.app) de votre API. Vous pouvez remplacer "http://localhost:3000" par la nouvelle URL et exécuter les mêmes tests en utilisant Postman.

Félicitations, votre application est maintenant en ligne. Vous pouvez faire plus avec votre application en utilisant l'interface d'administration, comme :

* Surveiller les performances de votre application

* Voir les logs en temps réel

* Ajouter des domaines personnalisés

* Mettre à jour les paramètres réseau (ouvrir/fermer des ports pour la sécurité, etc.)

* Ajouter plus de stockage

Sevalla propose également des ressources comme le stockage d'objets, la base de données, le cache, etc., qui sont hors du cadre de ce tutoriel. Mais il vous permet de surveiller, gérer et mettre à l'échelle votre application sans avoir besoin d'un administrateur système. C'est la beauté des systèmes PaaS. Voici une comparaison détaillée des [VPS vs systèmes PaaS](https://www.freecodecamp.org/news/vps-vs-paas-how-to-choose-a-hosting-solution/) pour l'hébergement d'applications.

## **Conclusion**

Dans cet article, nous avons dépassé le cas d'utilisation typique du frontend de Next.js et exploré ses capacités en tant que framework full-stack. Nous avons construit une API REST complète en utilisant l'App Router et le routage basé sur les fichiers, avec des données stockées dans un fichier JSON. Ensuite, nous avons franchi une étape supplémentaire en déployant l'API en production avec Sevalla, un PaaS moderne qui automatise le déploiement, la mise à l'échelle et la surveillance.

Cette configuration démontre comment les développeurs peuvent construire et livrer des applications full-stack comme le frontend, le backend et le déploiement, le tout dans un seul projet Next.js. Que vous prototypiez ou construisiez pour l'échelle, ce flux de travail vous équipe de tout ce dont vous avez besoin pour mettre vos applications entre les mains des utilisateurs rapidement et efficacement.

J'espère que vous avez apprécié cet article. Je vous retrouverai bientôt avec un autre. [Connectez-vous avec moi sur LinkedIn](https://manishshivanandhan.com/) ou [visitez mon site web](https://linkedin.com/in/manishmshiva).