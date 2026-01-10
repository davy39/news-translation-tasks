---
title: Comment créer un générateur de codes QR pour les URL avec Node.js, Next.js
  et Azure Blob Storage
subtitle: ''
author: Ayomide Wilfred
co_authors: []
series: null
date: '2024-05-10T15:41:39.000Z'
originalURL: https://freecodecamp.org/news/build-a-qr-code-generator-using-nodejs-nextjs-azure-blob-storage
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/qr-code-image-real.jpeg
tags:
- name: Next.js
  slug: nextjs
- name: node js
  slug: node-js
- name: qr code
  slug: qr-code
- name: Web Development
  slug: web-development
seo_title: Comment créer un générateur de codes QR pour les URL avec Node.js, Next.js
  et Azure Blob Storage
seo_desc: 'A while ago, a client asked me to help them create a special app for generating
  QR codes so users could receive payments.

  What set this app apart was that instead of users entering a URL to generate a QR
  code, they would initiate a request through th...'
---

Il y a quelque temps, un client m'a demandé de l'aider à créer une application spéciale pour générer des codes QR afin que les utilisateurs puissent recevoir des paiements.

Ce qui distinguait cette application, c'est que, au lieu que les utilisateurs entrent une URL pour générer un code QR, ils initiaient une demande via l'application. Ensuite, un code QR unique était généré, associé à leurs détails de compte. Le code QR était alors affiché sur leur écran tandis que le payeur scannait le code QR à l'aide de l'appareil photo de son appareil mobile.

Dans ce tutoriel, vous apprendrez à développer un générateur de codes QR personnalisé pour les URL en utilisant Node.js et Next.js. Je vous guiderai à travers le processus étape par étape, y compris la configuration d'Azure Blob Storage pour stocker les URL générées. Ces URL seront ensuite affichées sous forme de codes QR dans votre application frontend Next.js.

Nous construirons le backend de l'application en utilisant `Node.js` et le framework `Express`, et le frontend (qui interagit avec le backend) avec `Next.js`.

Je fournirai également des explications sur les codes QR, le concept de `buffers` pour gérer les données binaires dans Node.js, et comment il est utilisé pour diffuser les données d'image du code QR vers Azure Blob Storage.

Alors, plongeons-nous dans le sujet.

### **Prérequis**

Avant de commencer, vous aurez besoin d'un compte et d'un abonnement actifs [Azure](https://azure.microsoft.com/en-us/get-started/azure-portal) pour créer un stockage blob Azure.

## **Table des matières**

1. [Qu'est-ce qu'un code QR](#heading-quest-ce-quun-code-qr)?
    
2. [Comment configurer Azure Blob Storage](#heading-comment-configurer-azure-blob-storage)
    
3. [Code QR avec Node.js](#heading-code-qr-avec-nodejs)
    
4. [Aperçu du code](#code-overwiew)
    
5. [Comment connecter l'application frontend](#heading-comment-connecter-lapplication-frontend)
    
6. [Visite guidée du code Next.js](#heading-visite-guidee-du-code-nextjs)
    
7. [Comment démarrer l'application localement](#heading-comment-demarrer-lapplication-localement)
    
8. [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'un code QR ?

Selon [Investopedia](https://www.investopedia.com/terms/q/quick-response-qr-code.asp), un code QR (Quick Response) fonctionne comme un code-barres spécialisé, scannable par des appareils numériques, qui stocke des données dans une grille de pixels carrés.

Les codes QR sont largement utilisés dans les paiements numériques, les cryptomonnaies et la transmission d'adresses web vers des appareils mobiles. Ils peuvent encoder des URL, facilitant l'accès aux pages web.

Maintenant, plongeons dans le processus de génération programmatique de codes QR. Aujourd'hui, je vais vous montrer cela étape par étape. Pour commencer, vous allez configurer une instance `Azure Blob Storage` dans votre `Azure Portal`.

## Comment configurer Azure Blob Storage

[Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview) est un service de stockage basé sur le cloud fourni par Microsoft Azure. Il fait partie de la suite Azure Storage, qui comprend également des services tels que Azure Files, Azure Queues et Azure Tables.

Azure Blob Storage est conçu pour stocker de grandes quantités de données non structurées, telles que du texte ou des données binaires, sous forme d'objets appelés blobs. Si vous êtes familier avec AWS, Azure Blob Storage est similaire à un bucket S3. Les comptes de stockage sont principalement accessibles via une API REST.

### Étape 1 : Créer un compte de stockage

Vous pouvez créer votre compte de stockage en recherchant simplement "Storage account" dans la barre de recherche en haut du portail Azure.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-16.08.23.png align="left")

*Créer des comptes de stockage dans le portail Azure*

Vous pouvez ensuite suivre les étapes pour créer votre compte de stockage. Notez simplement que ce nom doit être unique et qu'il doit également être en minuscules – pas d'espaces mais il peut inclure des chiffres.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-16.16.46.jpeg align="left")

*Créer un nouveau groupe de ressources*

### Étape 2 : Créer un conteneur

Après avoir créé votre compte de stockage, vous pouvez maintenant créer un `conteneur`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-16.44.16.jpeg align="left")

*Créer un nouveau conteneur*

Lors de l'accès au stockage blob avec les `codes QR` stockés dans Azure Storage, l'URL suit généralement une structure comme `https://<nom_du_compte_de_stockage>.blob.core.windows.net/<nom_du_conteneur>/<nom_du_blob>`.

Avoir un conteneur nous permet de structurer les URL de manière significative et organisée, ce qui facilite la gestion et le partage des codes QR générés.

### Étape 3 : Obtenir la chaîne de connexion Azure Storage

Dans la section `Sécurité + réseau`, sélectionnez "Clés d'accès".

Assurez-vous de copier la chaîne de connexion et de la sauvegarder quelque part, car elle est nécessaire pour établir une connexion sécurisée entre le compte de stockage Azure et l'application `Node.js`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-16.54.39.jpeg align="left")

*Obtenir la clé d'accès pour le conteneur*

Cela conclut la discussion sur Microsoft Azure Storage. Je dois dire que j'ai vraiment apprécié explorer et résoudre ces défis.

Ensuite, vous allez plonger dans le codage, spécifiquement autour de `Node.js`, puis passer au développement frontend, où vous utiliserez `Next.js`.

## Code QR avec Node.js

Tout d'abord, vous devez installer `Node.js` et `npm` sur votre ordinateur. Allez sur le site [Node.js](https://nodejs.org/) et téléchargez la version pour votre ordinateur si vous ne l'avez pas déjà.

Une fois que vous les avez installés, vérifiez si Node.js et npm sont installés correctement en tapant ces commandes dans votre terminal :

```bash
node -v
npm -v
```

Ensuite, allez sur ce lien GitHub [lien](https://github.com/ayowilfred95/azure-qr-code-generator.git) pour fork le projet, puis clonez-le dans le répertoire de votre choix sur votre ordinateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-17.26.39--2-.jpeg align="left")

*Projet de dépôt GitHub*

Une fois que vous avez cloné le dépôt du projet, ouvrez le projet avec votre éditeur de code. J'utilise [VS Code](https://code.visualstudio.com/download). Vous remarquerez que le projet contient deux dossiers : `server` et `frontend`. Vous allez commencer par naviguer vers le dossier `server` en tapant `cd server` dans votre terminal, puis appuyez sur `Entrée`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-17.48.03.jpeg align="left")

*Changer le répertoire courant pour un répertoire nommé "server".*

Maintenant, vous pouvez installer toutes les dépendances nécessaires en exécutant `npm install`. Cette commande téléchargera et installera tous les packages requis pour l'application côté serveur.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-17.55.01.jpeg align="left")

*Installation des dépendances*

Si tout s'est bien passé, vous devriez voir quelque chose comme ceci après `npm install` :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-17.51.59.png align="left")

*Installation réussie*

Ensuite, vous devez créer un fichier `.env` dans le répertoire `server` pour stocker vos variables d'environnement. Il n'est pas conseillé de coder en dur les informations d'identification sensibles. Vous pouvez le faire facilement en exécutant `touch .env` dans votre terminal.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-17.59.38.jpeg align="left")

*Créer un nouveau fichier nommé ".env"*

Dans le fichier `.env` nouvellement créé, vous définirez trois variables dont votre application dépend : `CONTAINER_NAME`, `AZURE_STORAGE_CONNECTION_STRING` et `PORT`.

Attribuez 'qrcode' comme valeur pour `CONTAINER_NAME`. C'était le nom du conteneur que vous avez créé dans le compte de stockage Azure. De plus, définissez le `PORT` sur `8000`, qui est le port sur lequel votre application backend écoutera.

Maintenant, pour `AZURE_STORAGE_CONNECTION_STRING`, vous devrez obtenir la clé secrète à partir de la clé d'accès que vous avez obtenue précédemment. Copiez la chaîne de connexion et collez-la comme valeur pour `AZURE_STORAGE_CONNECTION_STRING` dans le fichier `.env`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-18.18.00.png align="left")

*Stocker les variables secrètes*

Une fois que vous avez ajouté ces variables d'environnement au fichier `.env`, enregistrez-le et vous êtes prêt à exécuter le côté serveur de l'application !

Avant d'exécuter l'application, laissez-moi expliquer rapidement le code. Cliquez sur le fichier `index.js`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-18.18.28.png align="left")

*Voir le fichier Index.js*

### Aperçu du code :

Voici l'extrait de code contenant la logique nécessaire pour générer des codes QR et établir une connexion avec le compte de stockage Azure que vous avez créé précédemment.

```bash
const express = require('express');
const { BlobServiceClient, generateBlobSASQueryParameters, BlobSASPermissions } = require('@azure/storage-blob');
const qrcode = require('qrcode');
const { v4: uuidv4 } = require('uuid');
const { Readable } = require('stream');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
const port = process.env.PORT || 5000;

// Autoriser CORS pour les tests locaux
const origins = [
    "http://localhost:3000"
];

app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', origins.join(','));
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});


const containerName = process.env.CONTAINER_NAME;

const blobServiceClient = BlobServiceClient.fromConnectionString(process.env.AZURE_STORAGE_CONNECTION_STRING);

app.use(express.json());

app.post('/generate-qr', async (req, res) => {
    const { url } = req.body;

    // Générer le code QR
    console.log('URL reçue :', url);
    const qrCode = await qrcode.toBuffer(url);

    const bufferStream = new Readable();
    bufferStream.push(qrCode);
    bufferStream.push(null);

    // Générer un nom de fichier unique pour Azure Blob Storage
    const fileName = `qr_codes/${uuidv4()}.png`;

    try {
        const containerClient = blobServiceClient.getContainerClient(containerName);
        const blockBlobClient = containerClient.getBlockBlobClient(fileName);

        await blockBlobClient.uploadStream(bufferStream, 4 * 1024 * 1024, 20, {
            blobHTTPHeaders: {
                blobContentType: 'image/png'
            }
        });

        // Générer un jeton SAS pour le blob
        const sasToken = generateSasToken(blockBlobClient);

        // Générer l'URL du blob avec le jeton SAS
        const blobUrlWithSasToken = `${blockBlobClient.url}?${sasToken}`;

        // Envoyer la réponse avec l'URL du blob contenant le jeton SAS
        res.json({ qr_code_url: blobUrlWithSasToken });
    } catch (error) {
        console.error('Erreur lors de la génération du code QR :', error);
        res.status(500).json({ error: 'Erreur interne du serveur' });
    }
});

// Fonction pour générer un jeton SAS pour le blob
function generateSasToken(blobClient) {
    const blobSAS = generateBlobSASQueryParameters({
        containerName: blobClient.containerName,
        blobName: blobClient.blobName,
        permissions: BlobSASPermissions.parse("r"), // Permission de lecture
        startsOn: new Date(),
        expiresOn: new Date(new Date().valueOf() + 86400) // Le jeton expire dans 24 heures
    }, blobClient.credential);

    return blobSAS.toString();
}

app.listen(port, () => {
    console.log(`Le serveur est en cours d'exécution sur le port ${port}`);
});
```

Maintenant, je vais donner une explication détaillée de la structure du code, des fonctionnalités et des composants clés de l'application.

#### Importation des modules requis :

* `const express = require('express')` : Cette ligne importe le framework Express.js, qui est un framework d'application web Node.js pour construire des applications web et des API. Il vous permet de définir des routes, de gérer les requêtes HTTP, et plus encore.
    
* `const { BlobServiceClient, generateBlobSASQueryParameters, BlobSASPermissions } = require('@azure/storage-blob')` : Cette ligne importe des modules spécifiques du package `@azure/storage-blob`, qui est le SDK Azure Blob Storage pour JavaScript. Il vous permet d'interagir avec Azure Blob Storage à partir de notre application Node.js.
    
* `const qrcode = require('qrcode')` : Cette ligne importe le module `qrcode`, qui est une bibliothèque Node.js populaire pour générer des codes QR.
    
* `const{ v4: uuidv4 } = require('uuid')` : Cette ligne importe le module `uuid` et extrait spécifiquement la fonction `v4` en tant que `uuidv4`. Le module `uuid` est utilisé pour générer des identifiants uniques universels (UUID) dans Node.js.
    
* `const{ Readable } = require('stream')` : Cette ligne importe la classe `Readable` du module `stream` intégré de Node.js. La classe `Readable` est utilisée pour créer des flux lisibles, qui sont utiles pour gérer les données qui peuvent être lues séquentiellement.
    

#### Configuration des variables d'environnement :

* `dotenv.config();` : Cette ligne charge les variables d'environnement à partir d'un fichier `.env` dans `process.env`. Le fichier `.env` contient généralement `CONTAINER_NAME` et `AZURE_STORAGE_CONNECTION_STRING` que vous spécifiez dans votre fichier `.env`.
    

#### Initialisation de l'application Express :

* `const app = express();` : Cette ligne initialise une instance d'application Express, que vous utiliserez pour définir des routes, des middlewares et d'autres configurations pour votre application web.
    

#### Définition de la configuration du port :

* `const port = process.env.PORT || 5000` : Cette ligne définit le numéro de port pour l'application Express. Elle récupère le numéro de port à partir de la variable d'environnement `process.env.PORT`, si elle existe. Sinon, elle utilise par défaut le port `5000`. Cela permet une flexibilité pour déployer l'application dans différents environnements où le port peut être spécifié externement.
    

#### Autorisation de CORS pour les tests locaux :

* CORS (Cross-Origin Resource Sharing) est une fonctionnalité de sécurité implémentée par les navigateurs web pour restreindre les ressources d'être demandées depuis un autre domaine ou une autre application.
    
* Dans cette section, CORS est configuré pour permettre les requêtes depuis une origine spécifique (`http://localhost:3000`), qui est typiquement utilisée pendant le développement local.
    
* La fonction `app.use()` est utilisée pour ajouter un middleware à l'application Express. Ici, une fonction middleware est définie qui définit les en-têtes CORS nécessaires sur chaque réponse HTTP.
    
* `res.header('Access-Control-Allow-Origin', origins.join(','))` : Définit la valeur de l'en-tête `Access-Control-Allow-Origin` pour permettre les requêtes depuis les origines spécifiées (dans ce cas, `http://localhost:3000`).
    
* `res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')` : Définit les en-têtes autorisés pour la requête CORS.
    
* `next()` : Appelle la fonction middleware suivante dans la pile.
    

#### Configuration d'Azure Blob Storage :

* `containerName` et `blobServiceClient` sont initialisés en utilisant les variables d'environnement (`process.env.CONTAINER_NAME` et `process.env.AZURE_STORAGE_CONNECTION_STRING`) configurées précédemment.
    
* `blobServiceClient` est initialisé en utilisant la méthode `fromConnectionString()` de la classe `BlobServiceClient` fournie par le package `@azure/storage-blob`. Cela permet à l'application d'interagir avec Azure Blob Storage en utilisant la chaîne de connexion fournie.
    

#### Configuration de l'application Express :

* `app.use(express.json())` : Ajoute un middleware pour analyser les corps JSON des requêtes entrantes. Cela permet à l'application de gérer les données JSON dans les requêtes.
    

#### Point de terminaison pour générer des codes QR :

* Définit un point de terminaison POST à `/generate-qr` pour gérer les requêtes de génération de codes QR.
    
* Lors de la réception d'une requête, le point de terminaison extrait l'URL du corps de la requête et génère une image de code QR en utilisant la fonction `qrcode.toBuffer()`.
    
* L'image du code QR générée est ensuite téléchargée vers Azure Blob Storage en tant que blob avec un nom de fichier unique.
    
* Après avoir téléchargé avec succès l'image, un jeton de signature d'accès partagé (SAS) est généré pour le blob, qui fournit un accès temporaire au blob avec des permissions spécifiées (dans ce cas, lecture seule).
    
* Enfin, le point de terminaison répond avec un objet JSON contenant l'URL de l'image du code QR générée ainsi que le jeton SAS.
    

#### Fonction pour générer un jeton SAS pour le blob :

* Définit une fonction `generateSasToken()` pour générer un jeton SAS pour un client de blob donné (client de blob de bloc dans ce cas). Le jeton SAS est généré avec des permissions de lecture et une heure d'expiration définie à 24 heures.
    

#### Écoute sur le port :

* L'application Express écoute sur le port configuré (`port`) pour les requêtes HTTP entrantes. Lorsque le serveur démarre, il imprime un message indiquant le port sur lequel il écoute.
    

Maintenant, vous pouvez démarrer l'application localement.

Pour démarrer l'application, exécutez simplement `npm start` comme indiqué ci-dessous. Si tout se passe bien, vous devriez observer le message `Le serveur est en cours d'exécution sur le port 8000` imprimé sur votre console.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-18.36.50.png align="left")

*Démarrer l'application localement*

## Comment connecter l'application frontend

Maintenant, il est temps de connecter l'application frontend avec l'application backend qui écoute sur le port 8000.

Une application full-stack typique se compose généralement d'au moins deux composants principaux : un frontend (côté client) et un backend (côté serveur).

**Composant Frontend** : C'est la partie de l'application avec laquelle les utilisateurs interagissent directement. Il est généralement construit en utilisant des technologies comme HTML, CSS et des frameworks JavaScript comme React, Angular ou Next.js.

**Composant Backend** : C'est la partie de l'application qui gère le stockage des données, la récupération et la connectivité côté serveur. Il est généralement construit en utilisant des langages de programmation côté serveur comme Node.js (avec des frameworks comme Express.js ou Nest.js), Python (avec des frameworks comme Django ou Flask), Java (avec des frameworks comme Spring) ou Ruby (avec des frameworks comme Ruby on Rails).

Le backend communique avec le frontend, traite les requêtes des utilisateurs, interagit avec les bases de données et génère des réponses.

Pour naviguer vers le dossier frontend, ouvrez un nouveau terminal en cliquant sur le `+`, puis utilisez `cd frontend` pour entrer dans le dossier frontend.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-18.57.14.jpeg align="left")

*Naviguer vers le répertoire Frontend*

Maintenant, vous pouvez installer toutes les dépendances nécessaires en exécutant `npm install`. Cette commande téléchargera et installera tous les packages requis pour l'application côté client Next.js.

Si tout s'est bien passé, vous devriez voir quelque chose comme ceci après `npm install`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-17.51.59-1.png align="left")

*Installation réussie des dépendances*

Avant d'exécuter l'application, laissez-moi expliquer rapidement le code. Naviguez vers le dossier frontend, puis dans le répertoire `src/app`, cliquez sur le fichier page.js.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-18.50.17.jpeg align="left")

*Voir le fichier page.js*

### Visite guidée du code Next.js

Ce code représente un composant React servant de frontend pour l'application backend de générateur de codes QR que vous avez récemment construite. Ce composant permet aux utilisateurs de saisir une URL, de la soumettre et de recevoir l'image du code QR correspondant pour l'affichage.

```bash
'use client'

import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [url, setUrl] = useState('');
  const [qrCodeUrl, setQrCodeUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/generate-qr', { url });
      setQrCodeUrl(response.data.qr_code_url);
    } catch (error) {
      console.error('Erreur lors de la génération du code QR :', error);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Générateur de code QR</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Entrez une URL comme https://www.google.com"
          style={styles.input}
        />
        <button type="submit" style={styles.button}>Générer le code QR</button>
      </form>
      {qrCodeUrl && <img src={qrCodeUrl} alt="Code QR" style={styles.qrCode} width="200" height="200" />}
    </div>
  );
}

// Styles
const styles = {
  container: {
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#121212',
    color: 'white',
  },
  title: {
    margin: '0',
    lineHeight: '1.15',
    fontSize: '4rem',
    textAlign: 'center',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  input: {
    padding: '10px',
    borderRadius: '5px',
    border: 'none',
    marginTop: '20px',
    width: '300px',
    color: '#121212'

  },
  button: {
    padding: '10px 20px',
    marginTop: '20px',
    border: 'none',
    borderRadius: '5px',
    backgroundColor: '#0070f3',
    color: 'white',
    cursor: 'pointer',
  },
  qrCode: {
    marginTop: '20px',
  },
};
```

Maintenant, je vais donner une explication détaillée de la structure du code de l'application frontend, des fonctionnalités et des composants clés.

#### Gestion d'état :

* `import { useState } from 'react'` importe le hook `useState` de React pour gérer l'état au sein du composant.
    
* `const [url, setUrl] = useState('')` et `const [qrCodeUrl, setQrCodeUrl] = useState('')` : Ces variables d'état, `url` et `qrCodeUrl`, sont initialisées en utilisant le hook `useState`. Ces variables contiennent l'URL d'entrée et l'URL du code QR généré, respectivement.
    

#### Soumission du formulaire :

* Lorsque le formulaire est soumis, la fonction `handleSubmit` est déclenchée.
    
* Cette fonction empêche le comportement par défaut de soumission du formulaire en utilisant `e.preventDefault()`.
    
* Elle envoie une requête POST au serveur (`http://localhost:8000/generate-qr`) avec l'URL d'entrée en utilisant la bibliothèque [Axios](https://axios-http.com/docs/intro).
    
* Lors d'une réponse réussie, l'URL du code QR généré est stockée dans la variable d'état `qrCodeUrl`.
    

#### Rendu :

* Le composant rend un titre, un formulaire avec un champ de saisie pour entrer l'URL et un bouton pour générer le code QR.
    
* Lorsque l'URL du code QR est disponible (`qrCodeUrl` n'est pas vide), un élément image est rendu pour afficher le code QR généré.
    

#### Styling :

* Le composant inclut des styles en ligne définis à l'aide d'objets JavaScript.
    
* Les styles sont appliqués au conteneur, au titre, au formulaire, au champ de saisie, au bouton et à l'image du code QR.
    

## Comment démarrer l'application localement

Maintenant, vous pouvez démarrer l'application localement.

Pour démarrer l'application, exécutez simplement `npm run dev` comme indiqué ci-dessous. Si tout se passe bien, vous devriez observer le message [`http://localhost:3000`](http://localhost:3000) imprimé dans votre console.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-08-at-15.18.18.png align="left")

*Application prête à démarrer*

Ouvrez votre navigateur et collez l'URL [`http://localhost:3000`](http://localhost:3000). Le navigateur devrait rendre l'application et elle devrait ressembler exactement à ce qui est montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-09-at-11.32.04.png align="left")

*Application en cours d'exécution dans le navigateur*

Collez l'URL d'un site web – soit votre site web portfolio ou tout autre site web pour lequel vous souhaitez générer un code QR. J'ai collé l'URL de mon site web portfolio, [`https://wilfred-portfolio.vercel.app/`](https://wilfred-portfolio.vercel.app/), dans la boîte d'URL. Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-07-at-20.32.40.png align="left")

*Code QR généré avec succès*

## Conclusion

Lorsqu'il s'agit de choisir les bons outils, les choix technologiques sont importants. Next.js est excellent pour créer le frontend d'un site web, tandis que Node.js fonctionne bien pour gérer les tâches côté serveur. De plus, Azure Blob Storage est idéal pour stocker des données non structurées telles que des données binaires comme les codes QR.

Mais n'oubliez pas, ce voyage ne consiste pas seulement à écrire du code. Il s'agit également d'apprendre différentes technologies et de choisir les meilleures pour ce que vous devez faire.

Alors que je termine ce tutoriel, j'aimerais continuer à demander des retours pour m'assurer que ce tutoriel reste utile. N'hésitez pas à partager vos pensées ou commentaires avec moi.

Merci d'avoir lu !

Bon codage ! 🚀

### **Contactez-moi :**

* [Twitter](https://twitter.com/ayomidewilfred9)
    
* [LinkedIn](https://www.linkedin.com/in/ayomide-wilfred-95083a104/)
    
* [GitHub](https://github.com/Ayowilfred95)