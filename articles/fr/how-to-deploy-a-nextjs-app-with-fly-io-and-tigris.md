---
title: Comment déployer une application Next.js en utilisant Fly.io et Tigris
subtitle: ''
author: Andrew Baisden
co_authors: []
series: null
date: '2024-04-17T21:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-nextjs-app-with-fly-io-and-tigris
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/fly-tigris-banner.png
tags:
- name: AWS
  slug: aws
- name: deployment
  slug: deployment
- name: Next.js
  slug: nextjs
seo_title: Comment déployer une application Next.js en utilisant Fly.io et Tigris
seo_desc: "In this tutorial, you're going to learn about the app deployment platform\
  \ Fly.io and the globally distributed S3-compatible object storage service Tigris.\
  \ \nBoth platforms are deeply connected, which makes them a great choice for your\
  \ projects. You ge..."
---

Dans ce tutoriel, vous allez apprendre à connaître la plateforme de déploiement d'applications Fly.io et le service de stockage d'objets compatible S3 et distribué mondialement Tigris. 

Les deux plateformes sont profondément connectées, ce qui en fait un excellent choix pour vos projets. Vous bénéficiez de l'expérience de déploiement d'applications de Fly.io et des fonctionnalités de stockage d'objets de Tigris. 

Le déploiement d'applications est assez explicite, alors commençons par une rapide introduction au stockage par bucket, utilisé par Tigris.

## Prérequis

* Un IDE/éditeur de code installé comme [Visual Studio Code](https://code.visualstudio.com/)
* [Node.js et npm](https://nodejs.org/en) installés
* [Next.js](https://nextjs.org/) installé ou configuré
* Un compte gratuit sur [Fly.io](https://fly.io/)
* Un compte gratuit sur [Tigris](https://www.tigrisdata.com/)

## Table des matières

1. [Qu'est-ce que le stockage par bucket ?](#heading-quest-ce-que-le-stockage-par-bucket)
2. [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
3. [Comment créer un compte sur Fly.io et Tigris](#heading-comment-creer-un-compte-sur-flyio-et-tigris)
4. [Comment configurer le projet de base de données utilisateur](#heading-comment-configurer-le-projet-de-base-de-donnees-utilisateur)
5. [Comment construire l'application de base de données utilisateur](#heading-comment-construire-lapplication-de-base-de-donnees-utilisateur)
6. [Comment créer l'interface utilisateur de la base de données utilisateur](#heading-comment-creer-linterface-utilisateur-de-la-base-de-donnees-utilisateur)
7. [Comment déployer votre application sur Fly.io](#how-to-deploy-our-app-to-fly-io)
8. [Conclusion](#heading-conclusion)

## Qu'est-ce que le stockage par bucket ?

Un bucket Amazon S3 est une ressource de stockage cloud public accessible via la plateforme Simple Storage Service (S3) d'Amazon Web Services (AWS). 

Le stockage à faible latence est une fonctionnalité utilisée par le service de stockage d'objets compatible S3 et distribué mondialement, Tigris. Cela signifie que vous pouvez accéder aux buckets S3 d'Amazon sur Tigris pour vos besoins de stockage. 

Tigris a également été entièrement intégré directement avec Fly.io et est également complètement intégré avec flyctl qui fonctionne sur le matériel de Fly.io. L'interface de ligne de commande de Fly.io, flyctl, vous permet de gérer la plateforme, de la création de compte au déploiement d'applications.

## Ce que nous allons construire

Pour apprendre les bases de ces plateformes, nous allons construire une application de base de données utilisateur. C'est assez simple : essentiellement, nous pouvons effectuer des requêtes CRUD complètes, ce qui signifie pouvoir lire, ajouter, mettre à jour et supprimer nos données utilisateur. 

Next.js sera notre framework principal car il nous permet de construire des applications full-stack sans avoir à créer un serveur séparé.

![Application de base de données utilisateur](https://res.cloudinary.com/d74fh3kw/image/upload/v1710878134/user-database_h2gfd8.png)
_Ecran d'accueil de l'application de base de données utilisateur_

Vous pouvez en apprendre plus sur [Fly.io](https://fly.io/) et [Tigris](https://www.tigrisdata.com/) à partir de leur documentation. Nous devrons créer un compte sur les deux plateformes pour ce projet, ce que je vais vous expliquer dans un instant. 

Alors maintenant, la théorie étant terminée, commençons.

Pour ce projet, vous pouvez trouver le code source [sur mon GitHub ici](https://github.com/andrewbaisden/fly-tigris-user-database).

## Comment créer un compte sur Fly.io et Tigris

Suivez simplement ces étapes pour démarrer sur les deux plateformes :

1. Tout d'abord, vous devez créer un compte sur [Fly.io](https://fly.io/), car pour utiliser Tigris, vous aurez besoin d'un compte Fly.io.
2. Ensuite, installez l'outil de ligne de commande [flyctl](https://fly.io/docs/hands-on/install-flyctl/) sur votre ordinateur, ce qui est essentiel pour configurer votre compte afin de déployer vos applications.

D'accord, passons à l'étape suivante où nous allons configurer notre projet ainsi que notre stockage par bucket Tigris.

## Comment configurer le projet de base de données utilisateur

Commencez par naviguer vers un répertoire sur votre ordinateur où vous prévoyez de créer le projet. Ensuite, créez un dossier appelé `fly-tigris-user-database` et `cd` dedans. Maintenant, exécutez la commande pour configurer un projet Next.js à l'intérieur de ce dossier :

```shell
npx create-next-app .

```

Tout ce que nous faisons est de configurer notre projet Next.js et il est important que pour la configuration, vous sélectionniez oui pour Tailwind CSS et le routeur d'applications car nous en aurons besoin dans ce projet.

Maintenant, exécutez cette commande pour installer le SDK AWS :

```shell
npm install @aws-sdk/client-s3

```

Nous n'avons qu'un seul package à installer (`@aws-sdk/client-s3`) dont nous avons besoin pour nous connecter à notre bucket.  
  
D'accord, bien  maintenant il est temps de créer un bucket pour le projet que nous venons de créer. Vous pouvez vous référer à leur [documentation officielle ici](https://www.tigrisdata.com/docs/get-started/).

Exécutez simplement cette commande pour créer un bucket :

```shell
fly storage create

```

Maintenant, sur l'écran de configuration, choisissez un nom pour votre bucket. Le nom doit être unique, donc vous ne pouvez pas utiliser un nom que quelqu'un d'autre a choisi. 

D'accord, maintenant pour l'étape la plus importante : vous devriez avoir vos secrets AWS et bucket comme dans l'exemple ici :

```shell
AWS_ACCESS_KEY_ID: votreclé
AWS_ENDPOINT_URL_S3: https://fly.storage.tigris.dev
AWS_REGION: auto
AWS_SECRET_ACCESS_KEY: votre secret access
BUCKET_NAME: votre nom de bucket

```

Créez un fichier `.env.local` à la racine de votre projet Next.js et copiez et collez toutes ces variables d'environnement secrètes. 

Pour que ces variables d'environnement fonctionnent correctement à l'intérieur de notre application Next.js, nous devons ajuster leurs noms en les rendant publiques. Voir l'exemple ci-dessous et apportez la modification à votre fichier `.env.local`. 

```shell
NEXT_PUBLIC_SECRET_AWS_ACCESS_KEY_ID: votreclé
NEXT_PUBLIC_SECRET_AWS_ENDPOINT_URL_S3: https://fly.storage.tigris.dev
NEXT_PUBLIC_SECRET_AWS_REGION: auto
NEXT_PUBLIC_SECRET_AWS_SECRET_ACCESS_KEY: votre secret access
NEXT_PUBLIC_SECRET_BUCKET_NAME: votre nom de bucket
```

Maintenant, sur la page de documentation de Tigris, si vous cliquez sur le bouton du tableau de bord et vous connectez à votre compte, vous devriez voir votre bucket nouvellement créé comme dans mon exemple montré ici :

![Buckets Tigris](https://res.cloudinary.com/d74fh3kw/image/upload/v1710881025/tigris_w3n8zm.jpg)
_Page de gestion des buckets du site web Tigris_

Super ! C'est la première phase terminée. Nous avons maintenant un bucket pour stocker les données de notre application en ligne, donc nous pouvons commencer à créer notre application dans la section suivante.

## Comment construire l'application de base de données utilisateur

Je vais diviser cette partie en deux sections. Tout d'abord, nous allons construire et exécuter notre serveur afin de pouvoir tester les endpoints CRUD. Ensuite, nous terminerons en construisant notre front-end.

### Comment créer le serveur de base de données utilisateur

Pour commencer, créons notre architecture backend. Nous allons créer quatre endpoints, donc un pour chaque requête CRUD. Nous avons également besoin d'un fichier helper qui contiendra quelques fonctions pour obtenir les utilisateurs de notre stockage d'objets. 

Si vous ne l'avez pas déjà fait, `cd` à la racine du projet et exécutez les commandes ci-dessous. Elles vont configurer tous nos fichiers et dossiers rapidement :

```shell
cd src/app
mkdir api
mkdir api/deleteuser api/getusers api/postuser api/updateuser
touch api/deleteuser/route.js
touch api/getusers/route.js
touch api/postuser/route.js
touch api/updateuser/route.js
mkdir helpers
touch helpers/getUsers.js

```

Bien, c'était rapide. Maintenant, nous devons simplement ajouter le code à nos cinq fichiers et notre API backend sera prête à être testée.

Commençons par le fichier helper. Le code dans ce fichier nous permet de collecter et d'accéder aux données utilisateur stockées dans notre bucket S3 sur Tigris.   
  
Placez le code ci-dessous dans `helpers/getUsers.js` :

```javascript
import {
  S3Client,
  ListObjectsV2Command,
  GetObjectCommand,
} from '@aws-sdk/client-s3';

const streamToString = (stream) =>
  new Promise((resolve, reject) => {
    const chunks = [];
    stream.on('data', (chunk) => chunks.push(chunk));
    stream.on('error', reject);
    stream.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
  });

export async function fetchAllUsersFromS3() {
  try {
    const s3 = new S3Client({
      region: process.env.NEXT_PUBLIC_SECRET_AWS_REGION,
      endpoint: process.env.NEXT_PUBLIC_SECRET_AWS_ENDPOINT_URL_S3,
      credentials: {
        accessKeyId: process.env.NEXT_PUBLIC_SECRET_AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.NEXT_PUBLIC_SECRET_AWS_SECRET_ACCESS_KEY,
      },
    });

    const commandDetails = new ListObjectsV2Command({
      Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
      MaxKeys: 10,
    });
    const { Contents } = await s3.send(commandDetails);
    console.log('List Result', Contents);
    if (!Contents) {
      console.log('no users');
    } else {
      const users = await Promise.all(
        Contents.map(async (item) => {
          const getObject = new GetObjectCommand({
            Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
            Key: item.Key,
          });

          const { Body } = await s3.send(getObject);
          const data = await streamToString(Body);
          const userObject = JSON.parse(data);
          console.log('Data', data);
          return userObject;
        })
      );
      return users;
    }
  } catch (e) {
    console.error(e);
    throw e;
  }
}

export async function getUserById(users, userId) {
  if (!users) {
    console.log('no users');
  } else {
    return users.find((user) => user.id === userId);
  }
}

export async function getUserByIdEmail(users, email) {
  if (!users) {
    console.log('no users');
  } else {
    return users.find(
      (user) => user.email.toLowerCase() === email.toLowerCase()
    );
  }
}

```

La fonction principale est `fetchAllUsersFromS3()`, qui crée essentiellement le client S3 avec les informations d'identification et la configuration dont nous avons besoin. Elle utilise la commande `GetObjectCommand` pour obtenir le contenu des objets qui sont ensuite convertis d'un flux en une chaîne à l'aide de la fonction `streamToString`. Les données JSON sont ensuite analysées avec les objets utilisateur retournés.

Les deux autres appels de fonction, `getUserById(users, userId)` et `getUserByIdEmail(users, email)`, sont des fonctions helpers qui nous permettent de rechercher des personnes dans notre bucket S3 en fonction de leur ID ou de leur adresse e-mail. Le code stocke les paramètres de configuration AWS essentiels dans des variables d'environnement, y compris la région, l'URL de l'endpoint, la clé d'accès et la clé d'accès secrète, ainsi que le nom du bucket S3.  
  
D'accord, il ne reste plus que les routes.  
  
Commencez par mettre ce code dans `getusers/route.js` :

```javascript
import {
S3Client,
ListObjectsV2Command,
GetObjectCommand,
} from '@aws-sdk/client-s3';

export async function GET() {
const streamToString = (stream) =>
new Promise((resolve, reject) => {
const chunks = [];
stream.on('data', (chunk) => chunks.push(chunk));
stream.on('error', reject);
stream.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
});
  
try {
const s3 = new S3Client({
region: process.env.NEXT_PUBLIC_SECRET_AWS_REGION,
endpoint: process.env.NEXT_PUBLIC_SECRET_AWS_ENDPOINT_URL_S3,
credentials: {
accessKeyId: process.env.NEXT_PUBLIC_SECRET_AWS_ACCESS_KEY_ID,
secretAccessKey: process.env.NEXT_PUBLIC_SECRET_AWS_SECRET_ACCESS_KEY,
},
});

const listParams = {
Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
MaxKeys: 10,
};

const list = new ListObjectsV2Command(listParams);
const { Contents } = await s3.send(list);

console.log('List Result', Contents);

if (!Contents || Contents.length === 0) {
console.log('No users found');
return new Response(JSON.stringify({ error: 'No users found' }), {
status: 404,
});
}

const users = await Promise.all(
Contents.map(async (item) => {
const getObjectParams = {
Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
Key: item.Key,
};

const getObject = new GetObjectCommand(getObjectParams);
const { Body } = await s3.send(getObject);
const data = await streamToString(Body);
console.log('Backend API GET Data:', data);
return JSON.parse(data);
})
);

return new Response(JSON.stringify(users), { status: 200 });
} catch (e) {
console.error('Error:', e);
return new Response(
JSON.stringify({ error: e.message || 'Unknown error' }),
{ status: 500 }
);
}
}

```

Dans le code de ce fichier, nous récupérons les données utilisateur de notre bucket S3 Tigris et les renvoyons en tant que réponse JSON via la fonction de gestionnaire de route de l'API Next.js.

La fonction importe également les clients SDK AWS nécessaires pour communiquer avec notre bucket S3 sur Tigris. Lorsque la route de l'API est demandée, le point d'entrée principal, la fonction `GET`, est appelée. En utilisant des variables d'environnement, la méthode `GET` établit d'abord un client S3 avec la configuration requise pour la région, l'endpoint et les informations d'identification. 

Après cela, une commande `ListObjectsV2Command` est créée pour récupérer la liste des éléments de données utilisateur du bucket S3 désigné. La méthode parcourt ensuite la liste des objets, récupérant les données de chaque objet avec la commande `GetObjectCommand`. 

La méthode `streamToString` est utilisée pour convertir le contenu de chaque objet d'un flux en une chaîne. 

Après l'analyse des données JSON, les objets utilisateur sont envoyés en tant que réponse JSON. Une réponse d'erreur 404 est renvoyée si aucun utilisateur n'est détecté, et la fonction fournit une réponse d'erreur 500 avec le message d'erreur s'il y a des problèmes pendant le processus.  
  
Ensuite, c'est la route POST, donc mettez ce code dans `postuser/route.js` :

```javascript
import { fetchAllUsersFromS3, getUserByIdEmail } from '../../helpers/getUsers';

import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';

export async function POST(req) {
  try {
    const { firstname, lastname, email, password } = await req.json();
    const id = crypto.randomUUID();
    const data = { firstname, lastname, email, password, id };
    console.log('Request body data', data);
    const allUsers = await fetchAllUsersFromS3();
    console.log('all users', allUsers);
    const existingUser = await getUserByIdEmail(allUsers, email);
    console.log(existingUser, email);
    if (existingUser) {
      return Response.json({
        error: 'Email address already in use',
      });
    }

    const s3 = new S3Client({
      region: process.env.NEXT_PUBLIC_SECRET_AWS_REGION,
      endpoint: process.env.NEXT_PUBLIC_SECRET_AWS_ENDPOINT_URL_S3,
      credentials: {
        accessKeyId: process.env.NEXT_PUBLIC_SECRET_AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.NEXT_PUBLIC_SECRET_AWS_SECRET_ACCESS_KEY,
      },
    });

    const commandDetails = new PutObjectCommand({
      Body: JSON.stringify(data),
      Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
      Key: email,
    });

    await s3.send(commandDetails);

    return Response.json({ message: 'User added' });
  } catch (e) {
    console.error(e);
    return Response.json({ error: 'Failed to create user' });
  }
}

```

Ce code gère l'inscription des utilisateurs et sauvegarde les informations des utilisateurs dans notre bucket S3 Tigris. Les deux fonctions helpers nécessaires pour communiquer avec le bucket S3 et collecter les données utilisateur sont importées par la fonction `fetchAllUsersFromS3` et `getUserByIdEmail`. Le point d'entrée initial, qui est déclenché lorsqu'une requête `POST` est faite pour accéder à la route de l'API, est la fonction `POST`. 

Les informations de l'utilisateur (prénom, nom, adresse e-mail et mot de passe) sont initialement prises à partir du corps de la requête via la fonction `POST`. Elle utilise ensuite `crypto.randomUUID()` pour créer un identifiant utilisateur unique. Pour obtenir toutes les données utilisateur actuelles du bucket S3, la méthode appelle ensuite la fonction helper `fetchAllUsersFromS3`.  
  
Le code utilise la fonction helper `getUserByIdEmail` pour déterminer si l'adresse e-mail fournie dans la requête existe déjà dans les données utilisateur. Si l'adresse e-mail existe déjà, la méthode fournit une réponse JSON contenant un message d'erreur. Si l'adresse e-mail est unique, la méthode utilise des variables d'environnement pour générer un client S3 avec la configuration requise pour la région, l'endpoint et les informations d'identification. 

Elle génère ensuite une commande `PutObjectCommand` qui télécharge les nouvelles données utilisateur (en tant que chaîne JSON) vers le bucket S3, avec l'adresse e-mail comme clé. Enfin, la méthode génère une réponse JSON confirmant que l'utilisateur a été ajouté avec succès. Si une erreur se produit pendant le processus, la fonction fournit une réponse JSON contenant un message d'erreur.  
  
Suivez cela avec notre route UPDATE et voici le code qui va dans `updateuser/route.js` :

```javascript
import { getUserById, fetchAllUsersFromS3 } from '../../helpers/getUsers';

import {
  S3Client,
  DeleteObjectCommand,
  PutObjectCommand,
} from '@aws-sdk/client-s3';

export async function PUT(req) {
  try {
    const { firstname, lastname, email, originalEmail, id } = await req.json();
    console.log('request data', firstname, lastname, email, originalEmail, id);
    const allUsers = await fetchAllUsersFromS3();
    console.log('all users', allUsers);
    const userToUpdate = await getUserById(allUsers, id);
    console.log('user to update', userToUpdate);
    const user = allUsers.find((user) => user.id === id);
    const userEmail = user ? user.email : null;
    console.log('User Email', userEmail);
    if (!userToUpdate) {
      return Response.json({ error: 'User not found' });
    }

    if (!originalEmail || !email) {
      return Response.json({
        error: 'Both originalEmail and email are required for update',
      });
    }

    const data = { firstname, lastname, email, id };

    console.log('Updated data', data);

    const s3 = new S3Client({
      region: process.env.NEXT_PUBLIC_SECRET_AWS_REGION,
      endpoint: process.env.NEXT_PUBLIC_SECRET_AWS_ENDPOINT_URL_S3,
      credentials: {
        accessKeyId: process.env.NEXT_PUBLIC_SECRET_AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.NEXT_PUBLIC_SECRET_AWS_SECRET_ACCESS_KEY,
      },
    });

    console.log('Original email', originalEmail);
    console.log('New email', email);

    if (userEmail === originalEmail) {
      console.log('The emails are the same so its a match');
      const deleteCommand = new DeleteObjectCommand({
        Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
        Key: originalEmail,
      });

      await s3.send(deleteCommand);
      const putCommand = new PutObjectCommand({
        Body: JSON.stringify(data),
        Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
        Key: email,
      });

      await s3.send(putCommand);

      return Response.json({ message: 'User updated successfully' });
    } else {
      console.log('Error: The emails do not match');
      return Response.json({ error: 'Failed to update user' });
    }
  } catch (e) {
    console.error(e);
  }
}

```

Le code inclut les mêmes fonctions helpers que précédemment, `getUserById` et `fetchAllUsersFromS3`, qui sont utilisées pour se connecter au bucket S3 et obtenir les données utilisateur. Le point d'entrée principal est la fonction `PUT`, qui est appelée chaque fois qu'une requête `PUT` est faite à la route de l'API. La fonction `PUT` extrait d'abord les données utilisateur (prénom, nom, email, originalEmail et id) du corps de la requête. 

Elle appelle ensuite la fonction helper `fetchAllUsersFromS3`, qui récupère toutes les données utilisateur existantes du bucket S3. Le code localise ensuite l'utilisateur à mettre à jour en appelant la fonction helper `getUserById` avec l'ID utilisateur spécifié. Si l'utilisateur ne peut pas être trouvé, la méthode fournit une réponse JSON avec un message d'erreur.  
  
Si l'originalEmail ou l'email est absent, la fonction fournit une réponse JSON incluant un message d'erreur. La méthode construit ensuite un objet de données utilisateur mis à jour basé sur les informations fournies. De plus, le code peut utiliser des variables d'environnement pour générer un client S3 avec les paramètres requis (région, endpoint et informations d'identification).   
  
En supposant que l'adresse email initiale correspond à celle de l'utilisateur actuel, la fonction met à jour les informations de l'utilisateur, mais si l'email original et l'adresse email actuelle de l'utilisateur ne correspondent pas, la méthode fournit une réponse JSON incluant un message d'erreur. Comme avant, si une erreur est détectée pendant le processus, alors la fonction créera un journal sans envoyer de réponse.  
  
Il ne reste plus que notre route DELETE. Ajoutez ce code à `deleteuser/route.js` :

```javascript
import { S3Client, DeleteObjectCommand } from '@aws-sdk/client-s3';

import { fetchAllUsersFromS3, getUserById } from '../../helpers/getUsers';

export async function DELETE(req) {
  try {
    const id = await req.json();
    console.log('Id', id.id);
    const allUsers = await fetchAllUsersFromS3();
    console.log('all users', allUsers);
    const userToDelete = await getUserById(allUsers, id.id);
    console.log('user to delete', userToDelete);

    if (!userToDelete) {
      return Response.json({ error: 'User not found' });
    }

    const userEmail = userToDelete.email;
    const s3 = new S3Client({
      region: process.env.NEXT_PUBLIC_SECRET_AWS_REGION,
      endpoint: process.env.NEXT_PUBLIC_SECRET_AWS_ENDPOINT_URL_S3,
      credentials: {
        accessKeyId: process.env.NEXT_PUBLIC_SECRET_AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.NEXT_PUBLIC_SECRET_AWS_SECRET_ACCESS_KEY,
      },
    });

    const deleteCommand = new DeleteObjectCommand({
      Bucket: process.env.NEXT_PUBLIC_SECRET_BUCKET_NAME,
      Key: userEmail,
    });

    await s3.send(deleteCommand);
    return Response.json({ message: 'User deleted successfully' });
  } catch (e) {
    console.error(e);
    return Response.json({ error: 'Failed to delete user' });
  }
}

```

Ceci est utilisé pour supprimer des données de notre bucket. Le code inclut les mêmes clients SDK AWS nécessaires pour communiquer avec S3, ainsi que les deux fonctions helpers `fetchAllUsersFromS3` et `getUserById` (qui sont utilisées pour obtenir les données utilisateur du bucket S3). Le point d'entrée principal est la fonction `DELETE`, qui est appelée lorsqu'une requête `DELETE` est faite à la route de l'API. 

Dans la fonction `DELETE`, l'ID de l'utilisateur est initialement extrait du corps de la requête. Elle appelle ensuite la méthode helper `fetchAllUsersFromS3`, qui récupère toutes les données utilisateur existantes du bucket S3. Le code localise ensuite l'utilisateur à supprimer en appelant la fonction helper `getUserById` avec l'ID utilisateur spécifié. Si le client ne peut pas être trouvé, la méthode fournit une réponse JSON avec un message d'erreur.  

Elle génère ensuite une commande `DeleteObjectCommand` qui supprime l'élément du bucket S3, avec l'adresse e-mail de l'utilisateur comme clé. Enfin, la méthode produit une réponse JSON confirmant que l'utilisateur a été supprimé avec succès. Une fois de plus, les erreurs sont enregistrées dans la console.  
  
D'accord, bien, c'est tout  nous avons terminé avec le backend. Démarrez le serveur avec le code d'exécution habituel et testez ces routes pour vous assurer que vous pouvez vous connecter à votre bucket et utiliser toutes les requêtes CRUD :

```
npm run dev

```

Pour tester le backend, vous pouvez utiliser un outil de test d'API comme Postman. Jetez un coup d'œil aux captures d'écran d'exemple pour référence :

##### Faire des requêtes GET

![Requêtes GET](https://res.cloudinary.com/d74fh3kw/image/upload/v1710885503/get-user-dashboard_od5nyy.png)
_Utilisation de l'application API Postman pour faire des requêtes GET pour notre bucket Tigris_

Les requêtes GET sont assez simples. Allez simplement sur [http://localhost:3000/api/getusers](http://localhost:3000/api/getusers).

##### Faire des requêtes POST

![Requêtes POST](https://res.cloudinary.com/d74fh3kw/image/upload/v1710885503/post-user-dashboard_n01a4q.png)
_Utilisation de l'application API Postman pour faire des requêtes POST pour notre bucket Tigris_

Les requêtes POST peuvent être faites ici : [http://localhost:3000/api/postuser](http://localhost:3000/api/postuser).

##### Faire des requêtes PUT

![Requêtes PUT](https://res.cloudinary.com/d74fh3kw/image/upload/v1710885503/put-user-dashboard_n2evps.png)
_Utilisation de l'application API Postman pour faire des requêtes PUT pour notre bucket Tigris_

Pour les requêtes PUT, allez à cette route : [http://localhost:3000/api/updateuser](http://localhost:3000/api/updateuser). Il est important de noter que vous DEVEZ mettre l'adresse e-mail originale pour cet ID, sinon cela ne fonctionnera pas. Et souvenez-vous de cela pour le front-end également, car nous n'avons implémenté qu'une gestion d'erreur basique.

##### Faire des requêtes DELETE

![Requêtes DELETE](https://res.cloudinary.com/d74fh3kw/image/upload/v1710885503/delete-user-dashboard_ebniqk.png)
_Utilisation de l'application API Postman pour faire des requêtes DELETE pour notre bucket Tigris_

Les requêtes DELETE peuvent être faites ici : [http://localhost:3000/api/deleteuser](http://localhost:3000/api/deleteuser).

Super, notre backend devrait être entièrement fonctionnel. Maintenant, il ne nous reste plus que le front-end. Ensuite, nous pouvons déployer notre application en ligne sur fly.io.

## Comment créer l'interface utilisateur de la base de données utilisateur

Maintenant pour le front-end, nous devons créer quatre composants et quatre hooks personnalisés pour les intégrer, et chacun est explicite. Les fichiers de composants contiennent notre formulaire et les données de tableau tandis que les fichiers de hooks effectuent nos requêtes CRUD et c'est tout.

Autre que cela, nous devons modifier quelques fichiers pour que nos styles Tailwind CSS fonctionnent  puis nous pouvons terminer avec la construction de nos composants front-end.

Avant de commencer, exécutez ce script à partir du dossier racine du projet afin que nous puissions définir la structure du dossier du projet pour nos composants et hooks personnalisés :

```shell
cd src/app
mkdir -p components/AddUserForm
touch components/AddUserForm/AddUserForm.js
mkdir -p components/DeleteUserForm
touch components/DeleteUserForm/DeleteUserForm.js
mkdir -p components/UpdateUserForm
touch components/UpdateUserForm/UpdateUserForm.js
mkdir -p components/UserDatabaseTable
touch components/UserDatabaseTable/UserDatabaseTable.js
mkdir -p hooks
touch hooks/useDelete.js
touch hooks/useFetch.js
touch hooks/usePost.js
touch hooks/useUpdate.js
```

Maintenant que les dossiers sont terminés, faisons rapidement une configuration pour Tailwind CSS et le style avant de compléter notre base de code.

Remplacez tout le code dans le fichier `globals.css` par ce code qui définit simplement une couleur de fond pour notre application :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  background: #eeeff1;
  font-size: 16px;
  color: #0e0e0e;
}

```

Maintenant, faites de même pour `layout.js`  nous ajoutons simplement la police Arsenal à notre projet :

```javascript
import { Arsenal } from 'next/font/google';
import './globals.css';

const arsenal = Arsenal({
  weight: '400',
  subsets: ['latin'],
});

export const metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={arsenal.className}>{children}</body>
    </html>
  );
}

```

D'accord, passons à autre chose, terminons ces hooks. 

Tout d'abord, `useFetch.js` que nous utilisons pour obtenir des données de notre bucket S3. Donnez au fichier `useFetch.js` ce code :

```javascript
import { useState, useEffect } from 'react';

export function useFetch(url) {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const json = await fetch(url).then((r) => r.json());
        setIsLoading(false);
        setData(json);
      } catch (error) {
        setError(error);
        setIsLoading(false);
      }
    };

    fetchData();

    const pollInterval = setInterval(() => {
      fetchData();
    }, 5000);

    return () => {
      clearInterval(pollInterval);
    };
  }, [url]);

  return { data, error, isLoading };
}

```

Examinons ce fichier et voyons comment il fonctionne. 

Nous avons trois variables d'état : une pour nos données récupérées, une autre pour gérer les erreurs pendant le processus de récupération, et notre état de chargement qui indique si nos données sont en cours de récupération ou non. La méthode `fetchData` est asynchrone et utilise l'API fetch pour récupérer les données de l'URL spécifiée. Elle ajuste ensuite les variables d'état en conséquence.  
  
Si la récupération est réussie, `isLoading` est modifié en `false`, et l'état des données est mis à jour avec les données JSON récupérées. Si une erreur se produit, elle attribue l'erreur à l'objet d'erreur et définit `isLoading` sur `false`.  
  
Il y a également une fonction de sondage configurée à la fin qui est définie sur 5 secondes. Essentiellement, tout ce qu'elle fait est d'exécuter la fonction de récupération toutes les 5 secondes, donc si de nouvelles données sont présentes dans l'API, la page sera automatiquement mise à jour. 

Vous pouvez personnaliser cela pour qu'il le fasse plus fréquemment, moins fréquemment, ou pas du tout. Si vous désactivez ce code, vous devez alors actualiser manuellement votre page pour voir les nouvelles modifications de l'API.  
  
Enfin, la fonction `useFetch` retourne un objet avec les variables d'état `data`, `error` et `isLoading`, que nous pouvons utiliser dans le composant qui appelle ce hook personnalisé. 

Maintenant pour le fichier `usePost.js`, ajoutez ce code au fichier `usePost.js` :

```javascript
import { useState } from 'react';

export function usePost() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [response, setResponse] = useState(null);

  const postRequest = async (url, formData) => {
    setIsLoading(true);
    setError(null);
    setResponse(null);

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },

        body: JSON.stringify(formData),
      });

      const responseData = await response.json();

      if (response.ok) {
        setResponse(responseData);
      } else {
        setError(responseData);
      }
    } catch (error) {
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  return { isLoading, error, response, postRequest };
}

```

Passons en revue le code pour voir comment fonctionne ce hook personnalisé. Comme notre fichier précédent, ce fichier a des variables d'état configurées pour vérifier les états de chargement et d'erreur. Mais cette fois, nous avons également un état `response` utilisé pour sauvegarder les données de retour de la requête POST réussie.  
  
La méthode `postRequest` est asynchrone et accepte une URL et `formData` en tant qu'entrées. Cette fonction est responsable de l'exécution de la requête POST et de la modification des variables d'état. Elle collecte les données du formulaire à partir du front-end qui serait une nouvelle entrée pour notre API dans le bucket S3 sur Tigris. Cela est envoyé en tant que JSON et sauvegardé dans notre bucket S3.  
  
Ensuite, c'est `useUpdate.js`, alors maintenant vous pouvez ajouter ce code au fichier `useUpdate.js` :

```javascript
import { useState } from 'react';

export function useUpdate() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [response, setResponse] = useState(null);
  const updateRequest = async (url, formData) => {
    setIsLoading(true);
    setError(null);
    setResponse(null);

    try {
      const response = await fetch(url, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },

        body: JSON.stringify(formData),
      });

      const responseData = await response.json();

      if (response.ok) {
        setResponse(responseData);
      } else {
        setError(responseData);
      }
    } catch (error) {
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  return { isLoading, error, response, updateRequest };
}

```

Tout comme nos hooks personnalisés précédents, ce fichier peut suivre nos états de chargement et d'erreur. Il est assez similaire à notre hook personnalisé `POST`, mais il effectue maintenant une requête `PUT` et met à jour les données existantes dans notre bucket S3 au lieu de créer de nouvelles entrées.  
  
Et enfin, c'est le moment du fichier `useDelete.js`. Ajoutez ce code à notre fichier `useDelete.js` :

```javascript
import { useState } from 'react';

export function useDelete() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [response, setResponse] = useState(null);
  const deleteRequest = async (url, formData) => {
    setIsLoading(true);
    setError(null);
    setResponse(null);

    try {
      const response = await fetch(url, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },

        body: JSON.stringify(formData),
      });

      const responseData = await response.json();

      if (response.ok) {
        setResponse(responseData);
      } else {
        setError(responseData);
      }
    } catch (error) {
      setError(error);
    } finally {
      setIsLoading(false);
    }
  };

  return { isLoading, error, response, deleteRequest };
}

```

Tout d'abord, nous allons avoir un aperçu de comment fonctionne ce hook personnalisé. Nous utilisons ce fichier pour faire des requêtes de suppression, donc essentiellement supprimer des données de notre bucket S3. 

Comme nos autres hooks personnalisés, il contient le même état pour vérifier le chargement et les erreurs. L'état de réponse nous donne les données d'une requête `DELETE` réussie ou mauvaise.  
  
Le fichier utilise l'API fetch pour envoyer une requête `DELETE` à l'URL spécifiée. Le corps de la requête contient l'objet formData avec sa réponse.  
  
Nos fichiers de hooks sont terminés, donc nous devons simplement terminer avec notre composant et fichier de page et notre application est prête à être utilisée !

D'accord, nos fichiers de composants ont le même nom que leur dossier, ce qui les rend faciles à trouver.   
  
Tout d'abord, notre fichier `AddUserForm.js`, et voici le code pour notre fichier :

```javascript
import { useState } from 'react';
import { usePost } from '../../hooks/usePost';

export default function AddUserForm() {
  const API = 'http://localhost:3000/';

  // POST form input state
  const [firstname, setFirstname] = useState('');
  const [lastname, setlastname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handlePostForm = async (e) => {
    e.preventDefault();

    if (
      firstname === '' ||
      lastname === '' ||
      email === '' ||
      password === ''
    ) {
      console.log('The form needs all fields to be filled in');
    } else {
      try {
        const user = {
          firstname: firstname,
          lastname: lastname,
          email: email,
          password: password,
        };
        // POST Route
        postRequest(`${API}/api/postuser`, user);
        console.log(`User ${user}`);
        setFirstname('');
        setlastname('');
        setEmail('');
        setPassword('');

        setAddUserMessage();
      } catch (error) {
        console.log(error);
      }
    }
  };

  // CRUD message box state
  const useToggleMessage = (initialState = 'hidden') => {
    const [message, setMessage] = useState(initialState);

    const toggleMessage = () => {
      setMessage('');

      setTimeout(() => {
        setMessage('hidden');
      }, 3000);
    };

    return [message, toggleMessage];
  };

  const [addUserMessage, setAddUserMessage] = useToggleMessage();
  const { postRequest } = usePost();

  return (
    <div className="bg-white p-4 rounded drop-shadow-md">
      <h1 className="text-2xl mb-4">ADD User</h1>
      <form onSubmit={(e) => handlePostForm(e)}>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Firstname</label>
          <input
            type="text"
            value={firstname}
            onChange={(e) => setFirstname(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>

        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Lastname</label>
          <input
            type="text"
            value={lastname}
            onChange={(e) => setlastname(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div>
          <button
            type="submit"
            className="bg-slate-600 hover:bg-slate-400 p-2 text-white cursor-pointer font-bold rounded-lg"
          >
            Add User
          </button>
        </div>
        <div>
          <p className={`bg-amber-100 p-2 mt-4 rounded ${addUserMessage}`}>
            User added
          </p>
        </div>
      </form>
    </div>
  );
}

```

Ce composant a un formulaire qui envoie une requête POST à notre serveur. Nous ajoutons de nouveaux utilisateurs en envoyant les données du corps de la requête pour les variables d'état (Prénom, Nom, Email et Mot de passe) à notre serveur backend qui les sauvegarde ensuite dans notre bucket S3 sur Tigris. Le formulaire utilise le hook `usePost` que nous avons créé pour envoyer la requête `POST` à notre serveur.  
  
D'accord, ensuite, c'est le fichier `DeleteUserForm.js`. Voici le code nécessaire pour le fichier :

```javascript
import { useState } from 'react';
import { useDelete } from '../../hooks/useDelete';

export default function DeleteUserForm() {
  const API = 'http://localhost:3000/';

  // DELETE form input state
  const [deleteId, setDeleteId] = useState('');
  const { deleteRequest } = useDelete();

  // CRUD message box state
  const useToggleMessage = (initialState = 'hidden') => {
    const [message, setMessage] = useState(initialState);

    const toggleMessage = () => {
      setMessage('');

      setTimeout(() => {
        setMessage('hidden');
      }, 3000);
    };

    return [message, toggleMessage];
  };

  const [deleteUserMessage, setDeleteUserMessage] = useToggleMessage();

  const handleDeleteForm = async (e) => {
    e.preventDefault();
    if (deleteId === '') {
      console.log('Form needs an id to be submitted');
    } else {
      try {
        const userId = {
          id: deleteId,
        };

        console.log('User ID', userId);
        // DELETE Route
        deleteRequest(`${API}/api/deleteuser`, userId);
        console.log(`User ${deleteId} deleted`);
        console.log(`UserId ${userId}`);
        setDeleteId('');

        setDeleteUserMessage();
      } catch (error) {
        console.log(error);
      }
    }
  };

  return (
    <div className="bg-white p-4 rounded drop-shadow-md mb-4 mt-4">
      <h1 className="text-2xl mb-4">DELETE User</h1>
      <form onSubmit={(e) => handleDeleteForm(e)}>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">ID</label>
          <input
            type="text"
            value={deleteId}
            onChange={(e) => setDeleteId(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div>
          <button
            type="submit"
            className="bg-slate-600 hover:bg-slate-400 p-2 text-white cursor-pointer font-bold rounded-lg"
          >
            Delete User
          </button>
        </div>
        <div>
          <p className={`bg-amber-100 p-2 mt-4 rounded ${deleteUserMessage}`}>
            User deleted
          </p>
        </div>
      </form>
    </div>
  );
}

```

Celui-ci est assez simple : il a juste un formulaire pour supprimer des utilisateurs de la base de données. Essentiellement, la logique recherche un utilisateur par son ID dans la base de données. Si elle trouve une correspondance, alors elle envoie une requête `DELETE` au serveur qui supprime cette entrée de notre bucket S3. Comme notre composant précédent, celui-ci utilise un hook `useDelete` pour effectuer l'action.  
  
D'accord, passons maintenant au fichier `UpdateUserForm.js`. Voici le code pour notre formulaire, alors ajoutez-le :

```javascript
import { useState } from 'react';
import { useUpdate } from '../../hooks/useUpdate';

export default function UpdateUserForm() {
  const API = 'http://localhost:3000/';

  // UPDATE/PUT form input state
  const [updateId, setUpdateId] = useState('');
  const [updateFirstname, setUpdateFirstname] = useState('');
  const [updateLastname, setUpdateLastname] = useState('');
  const [updateEmail, setUpdateEmail] = useState('');
  const [originalemail, setOriginalemail] = useState('');
  const [updatePassword, setUpdatePassword] = useState('');

  // CRUD message box state
  const useToggleMessage = (initialState = 'hidden') => {
    const [message, setMessage] = useState(initialState);

    const toggleMessage = () => {
      setMessage('');

      setTimeout(() => {
        setMessage('hidden');
      }, 3000);
    };

    return [message, toggleMessage];
  };

  const [updateUserMessage, setUpdateUserMessage] = useToggleMessage();
  const { updateRequest } = useUpdate();

  const handleUpdateForm = async (e) => {
    e.preventDefault();

    if (
      updateId === '' ||
      updateFirstname === '' ||
      updateLastname === '' ||
      originalemail === '' ||
      updateEmail === '' ||
      updatePassword === ''
    ) {
      console.log('The form needs all fields to be filled in');
    } else {
      try {
        const user = {
          id: updateId,
          firstname: updateFirstname,
          lastname: updateLastname,
          originalEmail: originalemail,
          email: updateEmail,
          password: updatePassword,
        };

        console.log(`User: ${user}`);
        // UPDATE Route
        updateRequest(`${API}/api/updateuser`, user);

        setUpdateId('');
        setUpdateFirstname('');
        setUpdateLastname('');
        setOriginalemail('');
        setUpdateEmail('');
        setUpdatePassword('');

        setUpdateUserMessage();
      } catch (error) {
        console.log(error);
      }
    }
  };

  return (
    <div className="bg-white p-4 rounded drop-shadow-md mb-4 mt-4">
      <h1 className="text-2xl mb-4">UPDATE User</h1>
      <form onSubmit={(e) => handleUpdateForm(e)}>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">ID</label>
          <input
            type="text"
            value={updateId}
            onChange={(e) => setUpdateId(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Firstname</label>
          <input
            type="text"
            value={updateFirstname}
            onChange={(e) => setUpdateFirstname(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>

        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Lastname</label>
          <input
            type="text"
            value={updateLastname}
            onChange={(e) => setUpdateLastname(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">
            Original Email
          </label>
          <input
            type="email"
            value={originalemail}
            onChange={(e) => setOriginalemail(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Email</label>
          <input
            type="email"
            value={updateEmail}
            onChange={(e) => setUpdateEmail(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div className="flex flex-wrap items-center mb-2">
          <label className="p-2 w-36 border-solid border-2">Password</label>
          <input
            type="password"
            value={updatePassword}
            onChange={(e) => setUpdatePassword(e.target.value)}
            className="grow p-2 border border-2"
            required
          />
        </div>
        <div>
          <button
            type="submit"
            className="bg-slate-600 hover:bg-slate-400 p-2 text-white cursor-pointer font-bold rounded-lg"
          >
            Update User
          </button>
        </div>
        <div>
          <p className={`bg-amber-100 p-2 mt-4 rounded ${updateUserMessage}`}>
            User updated
          </p>
        </div>
      </form>
    </div>
  );
}

```

Le formulaire de ce composant utilise le hook `useUpdate` pour envoyer une requête `PUT` à notre serveur backend. Le formulaire prend des variables d'état pour ID, Prénom, Nom, Email original, Email et Mot de passe. 

La plupart des champs sont faciles à interpréter  notons le champ de formulaire Email original. Vous devez entrer l'adresse e-mail actuelle de l'utilisateur, sinon vous ne pourrez pas mettre à jour l'utilisateur car cela échouera à la vérification. L'ID doit également correspondre, sinon le formulaire ne fonctionnera pas.

Bien, maintenant il ne nous reste plus que deux fichiers  commençant par le fichier `UserDatabaseTable.js` qui nécessite ce code :

```javascript
import { useEffect } from 'react';
import { useFetch } from '../../hooks/useFetch';

export default function UserDatabaseTable() {
  const API = 'http://localhost:3000/';

  const { data, error, isLoading } = useFetch(`${API}/api/getusers`);
  if (error) return <div>An error has occurred.</div>;
  if (isLoading) return <div>Loading...</div>;

  useEffect(() => {
    console.log('Client API GET Data:', data);
  }, [data]);

  return (
    <div>
      <h1 className="text-4xl mb-2 text-center uppercase">User Database</h1>
      <div className="bg-gray-900 text-white p-4 rounded flex justify-center">
        <table className="table-auto border border-slate-500">
          <thead>
            <tr>
              <th className="border border-slate-600 p-2 text-2xl">ID</th>
              <th className="border border-slate-600 p-2 text-2xl">
                Firstname
              </th>
              <th className="border border-slate-600 p-2 text-2xl">Lastname</th>
              <th className="border border-slate-600 p-2 text-2xl">Email</th>
            </tr>
          </thead>

          {data === 0 ? (
            <tbody></tbody>
          ) : (
            <tbody>
              {data.map((user) => (
                <tr key={user.id}>
                  <td className="border border-slate-600 p-2 bg-gray-800 hover:bg-gray-600">
                    {user.id}
                  </td>
                  <td className="border border-slate-600 p-2 bg-gray-800 hover:bg-gray-600">
                    {user.firstname}
                  </td>
                  <td className="border border-slate-600 p-2 bg-gray-800 hover:bg-gray-600">
                    {user.lastname}
                  </td>
                  <td className="border border-slate-600 p-2 bg-gray-800 hover:bg-gray-600">
                    {user.email}
                  </td>
                </tr>
              ))}
            </tbody>
          )}
        </table>
      </div>
    </div>
  );
}

```

Dans ce fichier, nous utilisons le hook `useFetch` pour faire une requête `GET` à notre bucket S3. C'est ainsi que nous récupérons les données qui s'y trouvent. Ensuite, tout ce que nous faisons est `data.map` pour parcourir le tableau de données et les afficher dans un tableau à l'écran.  
  
Presque terminé  il nous reste un fichier : notre fichier `page.js` dans le dossier racine. Ajoutez simplement ce code et terminons-le :

```javascript
'use client';
import UserDatabaseTable from './components/UserDatabaseTable/UserDatabaseTable';
import AddUserForm from './components/AddUserForm/AddUserForm';
import UpdateUserForm from './components/UpdateUserForm/UpdateUserForm';
import DeleteUserForm from './components/DeleteUserForm/DeleteUserForm';

export default function Home() {
  return (
    <div className="container mx-auto mt-4">
      <UserDatabaseTable />
      <div className="bg-slate-100 rounded p-10 drop-shadow-lg">
        <AddUserForm />
        <UpdateUserForm />
        <DeleteUserForm />
      </div>
    </div>
  );
}

```

Tout ce que fait ce fichier est de servir de point d'entrée principal pour tous les composants que nous avons créés afin qu'ils s'affichent à l'écran et complètent le front-end.  
  
Et nous avons terminé ! Maintenant, vous pouvez exécuter l'application avec `npm run dev` (si elle ne fonctionne pas déjà) et l'essayer.

Juste un petit rappel : lors de l'utilisation du formulaire de mise à jour de l'utilisateur, vous devez vous assurer que vous utilisez l'email original, sinon cela ne mettra pas à jour. 

De plus, faites attention aux espaces blancs lors de la copie de l'ID car cela empêchera également les mises à jour de se faire. N'hésitez pas à implémenter une meilleure gestion des erreurs et des vérifications si vous le souhaitez ;)

Notre application devrait être entièrement fonctionnelle maintenant. Il ne nous reste plus qu'à la déployer en ligne dans la section finale.

## Comment déployer votre application sur Fly.io

Le déploiement est la dernière partie de ce processus, et il ne faut que quelques étapes simples pour déployer votre application en ligne. 

Tout d'abord, vous devriez être à la racine du dossier de projet `fly-tigris-user-database`. Exécutez la commande suivante à partir du répertoire source de votre projet pour démarrer une nouvelle application Fly.io :

```shell
fly launch

```

Cette commande créera un fichier `fly.toml` et configurera notre projet en définissant le nom de notre projet, la région de déploiement et d'autres paramètres.  
  
Maintenant, exécutez la commande ci-dessous pour déployer votre application sur Fly.io :

```shell
fly deploy
```

La commande `fly deploy` de flyctl crée votre application Fly et la lance sur une ou plusieurs machines Fly, en utilisant les paramètres fournis dans le fichier local `fly.toml`.  
  
Maintenant, lorsque vous allez sur le tableau de bord de votre compte Fly.io, vous verrez votre application comme dans la capture d'écran ici :

![Écran du tableau de bord des applications du site web fly.io](https://res.cloudinary.com/d74fh3kw/image/upload/v1712949553/fly-io-dashboard_m1egpx.jpg)
_Écran du tableau de bord des applications du site web Fly.io_

Notre application est maintenant en ligne mais elle ne fonctionnera pas tant que nous n'aurons pas ajouté nos variables d'environnement du fichier `.env.local` à la page Secrets pour notre application sur Fly.io. Nous devrons également mettre à jour notre variable de route API ensuite afin qu'elle utilise notre route Fly.io et non localhost.   
  
Tout d'abord, faisons les secrets, utilisez donc cette page de secrets d'exemple comme référence pour votre propre application :

![Écran des secrets du site web fly.io](https://res.cloudinary.com/d74fh3kw/image/upload/v1712950078/fly-io-secrets_s6ysyz.jpg)
_Écran des secrets du site web Fly.io_

Les secrets sont planifiés pour la prochaine version. Pour déclencher un déploiement, exécutez [`fly deploy`](https://fly.io/docs/flyctl/deploy/) à partir d'un terminal. N'oubliez pas que votre application ne fonctionnera pas en ligne tant que vous n'aurez pas mis à jour la variable API pour les composants à l'intérieur du dossier des composants. Localement, nous utilisons [http://localhost:3000](http://localhost:3000/) et en ligne, nous utiliserons l'URL qui est automatiquement générée par fly.io.

La variable API se trouve près du haut dans ces fichiers que vous devrez mettre à jour :

* components/AddUserForm/AddUserForm.js
* components/DeleteUserForm/DeleteUserForm.js
* components/UpdateUserForm/UpdateUserForm.js
* components/UserDatabaseTable/UserDatabaseTable.js

Voir le code d'exemple ici pour la variable API :

```javascript
const API = 'https://votre-url-en-ligne.fly.dev/';
```

Lorsque votre application est déployée en ligne, vous obtiendrez une URL. Remplacez simplement la valeur de la variable `API` par votre URL en ligne Fly.io. Les routes dans notre application proviennent maintenant de notre application sur Fly.io et non de notre application localhost dans l'environnement de test de développement.

N'oubliez pas d'exécuter à nouveau la commande `fly deploy` (et chaque fois que vous apportez une modification à votre base de code locale ou aux secrets) afin que votre application sur Fly.io obtienne les dernières modifications.  
  
Vous pouvez [lire la documentation ici](https://fly.io/docs/apps/launch/) pour plus d'informations sur la façon dont le déploiement est effectué.

C'est tout ! Le déploiement devrait également être terminé, et nous pouvons accéder à notre application en ligne.

## Conclusion

Aujourd'hui, nous avons appris à construire une application full-stack en utilisant Next.js et à la déployer en ligne sur la plateforme d'hébergement d'applications Fly.io. Nous avons également utilisé Tigris pour stocker nos données utilisateur dans un bucket AWS en ligne. 

La combinaison des deux plateformes en fait un outil très utile et puissant pour mettre nos applications en ligne. Les deux plateformes offrent de nombreuses fonctionnalités différentes, il est donc intéressant de jouer avec elles et de voir comment elles peuvent être bénéfiques pour vos projets.