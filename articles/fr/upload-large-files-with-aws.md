---
title: Comment télécharger des fichiers volumineux efficacement avec le téléchargement
  multipartite AWS S3
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2024-07-08T12:02:56.000Z'
originalURL: https://freecodecamp.org/news/upload-large-files-with-aws
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/mr-cup-fabien-barral-o6GEPQXnqMY-unsplash.jpg
tags:
- name: AWS
  slug: aws
- name: S3
  slug: s3
seo_title: Comment télécharger des fichiers volumineux efficacement avec le téléchargement
  multipartite AWS S3
seo_desc: "Imagine running a media streaming platform where users upload large high-definition\
  \ videos. Uploading such large files can be slow and may fail if the network is\
  \ unreliable. \nUsing traditional single-part uploads can be cumbersome and inefficient\
  \ for..."
---

Imaginez gérer une plateforme de streaming média où les utilisateurs téléchargent de grandes vidéos haute définition. Le téléchargement de tels fichiers volumineux peut être lent et peut échouer si le réseau est peu fiable. 

L'utilisation de téléchargements traditionnels en une seule partie peut être fastidieuse et inefficace pour les gros fichiers, entraînant souvent des erreurs de délai d'attente ou la nécessité de redémarrer l'ensemble du processus de téléchargement si une partie échoue. C'est là que la fonctionnalité de téléchargement multipartite d'Amazon S3 entre en jeu, offrant une solution robuste à ces défis.

Dans cet article, vous explorerez comment gérer efficacement les gros fichiers avec le téléchargement multipartite Amazon S3. Nous discuterons des avantages de l'utilisation de cette fonctionnalité, passerons en revue le processus de téléchargement de fichiers en parties et fournirons des exemples de code utilisant le SDK AWS pour un projet full-stack Node et React. 

À la fin de cet article, vous devriez avoir une bonne compréhension de la manière de tirer parti du téléchargement multipartite Amazon S3 pour optimiser les téléchargements de fichiers dans vos applications.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

* Un compte AWS avec des identifiants d'utilisateur IAM.
* Node.js installé sur votre machine de développement.
* Des connaissances de base en JavaScript, React et Node.js.

## Table des matières :

* [Introduction](#)
* [Prérequis](#heading-prerequisites)
* [Table des matières](#table-of-contents)
* [Comment cela fonctionne](#heading-comment-cela-fonctionne)
* [Étape 1 : Comment configurer AWS S3](#heading-etape-1-comment-configurer-aws-s3)
* [Comment créer un bucket S3](#heading-comment-creer-un-bucket-s3)
* [Comment configurer la politique de bucket S3](#heading-comment-configurer-la-politique-de-bucket-s3)
* [Étape 2 : Comment configurer le backend AWS S3 avec Node.js](#heading-etape-2-comment-configurer-le-backend-aws-s3-avec-nodejs)
* [Comment initialiser un projet Node.js](#heading-initialiser-un-projet-nodejs)
* [Installer les packages requis](#heading-installer-les-packages-requis-1)
* [Créer le fichier serveur](#heading-creer-le-fichier-serveur)
* [Imports et configuration](#heading-imports-et-configuration)
* [Middleware et configuration AWS](#heading-middleware-et-configuration-aws)
* [Routes](#heading-routes)
* [Point de terminaison de démarrage/initialisation du téléchargement](https://www.freecodecamp.org/news/p/d96e9e12-b460-4784-b0cf-88855383af4d/start-initialize-upload-endpoint)
* [Point de terminaison de téléchargement de partie](#heading-point-de-terminaison-de-telechargement-de-partie)
* [Point de terminaison de finalisation du téléchargement](#heading-point-de-terminaison-de-finalisation-du-telechargement)
* [Démarrer le serveur](#heading-demarrer-le-serveur)
* [Variables d'environnement](#heading-variables-environnement)
* [Exécuter le serveur](#heading-executer-le-serveur)
* [Étape 3 : Comment configurer le frontend avec React](#heading-etape-3-comment-configurer-le-frontend-avec-react)
* [Comment initialiser un projet React](#heading-initialiser-un-projet-react)
* [Installer les packages requis](#heading-installer-les-packages-requis-1)
* [Créer des composants](#heading-creer-des-composants)
* [Composant App](#heading-composant-app)
* [Test](#heading-test)
* [Téléchargement de partie](#heading-telechargement-de-partie)
* [Finalisation du téléchargement de partie](#heading-finalisation-du-telechargement-de-partie)
* [Code complet sur GitHub](#heading-code-complet-sur-github)
* [Conclusion](#heading-conclusion)

## Comment cela fonctionne

Un téléchargement de fichier volumineux est divisé en parties/morceaux plus petits, chaque partie est téléchargée indépendamment vers Amazon S3. Une fois que toutes les parties ont été téléchargées, elles sont combinées pour créer l'objet final.

Exemple : Le téléchargement d'un fichier de 100 Mo en parties de 5 Mo entraînerait le téléchargement de 20 parties vers S3. Chaque partie est téléchargée avec un identifiant unique, et l'ordre est maintenu pour garantir que le fichier peut être réassemblé correctement.

Les nouvelles tentatives peuvent être configurées pour réessayer automatiquement les parties échouées, et le téléchargement peut être mis en pause et repris à tout moment. Cela rend le processus plus robuste et tolérant aux pannes, en particulier pour les gros fichiers.

![https://media.amazonwebservices.com/blog/s3_multipart_upload.png](https://media.amazonwebservices.com/blog/s3_multipart_upload.png)
_téléchargements multipartites AWS s3_

En savoir plus sur la [documentation du téléchargement multipartite Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html).

Commençons !

## Étape 1 : Comment configurer AWS S3

### Comment créer un bucket S3

Tout d'abord, connectez-vous à la console de gestion AWS

* Accédez au service S3.

![Comment créer un bucket s3](https://www.freecodecamp.org/news/content/images/2024/06/create-bucket.png)
_Comment créer un bucket s3_

Créez un nouveau bucket et notez le nom du bucket.

Décochez les paramètres d'accès public pour simplifier. Nous allons également configurer l'accès au bucket en utilisant les politiques IAM après avoir créé le bucket.

![Comment créer un bucket s3](https://www.freecodecamp.org/news/content/images/2024/06/create-bucket2.png)
_Comment créer un bucket s3_

* Laissez les autres paramètres par défaut et créez le bucket.

### Comment configurer la politique de bucket S3

Maintenant que vous avez créé le bucket, configurons la politique pour permettre aux utilisateurs de lire l'URL de vos objets (fichiers/vidéos).

* Cliquez sur le nom du bucket et accédez à l'onglet `Permissions`.

![Comment configurer la politique de bucket s3](https://www.freecodecamp.org/news/content/images/2024/06/permission.png)
_Comment configurer la politique de bucket s3_

Accédez à la section `Bucket Policy` et cliquez sur Edit.

Saisissez la politique suivante, et remplacez `your-bucket-name` par le nom réel de votre bucket :

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}

```

`Version` : Numéro de version de l'objet Amazon S3 pour le langage de politique de bucket.

`Statement` : Un tableau d'une ou plusieurs déclarations individuelles qui définissent la politique.

`Effect` : L'effet détermine si la déclaration permet ou refuse l'accès.

`Principal` : L'entité à laquelle la politique est appliquée. Dans ce cas, nous permettons à tous les principaux. En production, vous devez spécifier l'utilisateur ou le rôle IAM qui a besoin d'accès.

`Action` : L'action que la politique permet ou refuse. Dans ce cas, nous permettons l'action `s3:GetObject`, qui permet aux utilisateurs de récupérer des objets du bucket.

`Resource` : Le nom de ressource Amazon (ARN) du bucket et des objets auxquels la politique s'applique. Dans ce cas, nous permettons l'accès à tous les objets du bucket.

Cliquez sur Save changes pour appliquer la politique.

## Étape 2 : Comment configurer le backend AWS S3 avec Node.js

Ensuite, configurons le serveur backend avec le SDK AWS pour gérer le processus de téléchargement de fichiers.

### Comment initialiser un projet Node.js

Créez un nouveau répertoire pour votre projet et initialisez un nouveau projet Node.js :

```bash
mkdir s3-multipart-upload
cd s3-multipart-upload
npm init -y

```

### Installer les packages requis

Installez les packages suivants en utilisant npm :

```bash
 npm install express dotenv multer aws-sdk

```

### Créer le fichier serveur

Créez un nouveau fichier nommé `app.js` (Pour simplifier, nous allons utiliser ce fichier uniquement pour toute la logique de téléchargement) et ajoutez le code suivant :

#### Imports et configurations

```javascript
const cors = require("cors");
const express = require("express");
const AWS = require("aws-sdk");
const dotenv = require("dotenv");
const multer = require("multer");

const multerUpload = multer();
dotenv.config();

const app = express();
const port = 3001;

```

##### Imports

`cors` : Middleware pour activer le partage de ressources cross-origin (CORS). Cela est nécessaire pour permettre à votre application frontend d'interagir avec le backend hébergé sur un domaine ou un port différent.

`express` : Un framework d'application web Node.js minimal et flexible.

`AWS` : Le SDK AWS pour JavaScript, qui vous permet d'interagir avec les services AWS.

`dotenv` : Un module qui charge les variables d'environnement à partir d'un fichier **.env** dans **process.env**.

`multer` : Middleware pour gérer les données multipart/form-data, principalement utilisé pour télécharger des fichiers.

##### Configurations

`multerUpload` : Initialise `multer` pour gérer les téléchargements de fichiers.

`dotenv.config()` : Charge les variables d'environnement à partir d'un fichier .env.

`app` : Initialise une application Express.

`port` : Définit le port sur lequel l'application Express s'exécutera.

#### Middleware et configuration AWS

Ensuite, ajoutez le code suivant pour configurer le middleware et le SDK AWS :

```javascript
app.use(cors());

AWS.config.update({
  accessKeyId: process.env.AWS_ACCESS_KEY,
  secretAccessKey: process.env.AWS_SECRET_KEY,
  region: process.env.AWS_REGION,
});

const s3 = new AWS.S3();
app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ limit: "50mb", extended: true }));

```

`app.use(cors())` : Active CORS pour toutes les routes, permettant à votre frontend de communiquer avec le backend sans problèmes liés aux requêtes cross-origin.

`AWS.config.update({ ... })` : Configure le SDK AWS avec la clé d'accès, la clé secrète et la région à partir des variables d'environnement.  
const s3 = new AWS.S3() : Crée une instance du service S3.

`app.use(express.json({ limit: '50mb' }))` : Configure Express pour analyser les corps JSON avec une limite de taille de 50 Mo.

`app.use(express.urlencoded({ limit: '50mb', extended: true }))` : Configure Express pour analyser les corps encodés en URL avec une limite de taille de 50 Mo.

### Routes

Il est temps de commencer à créer nos routes. Les routes requises pour le processus de téléchargement multipartite sont les suivantes :

* Initialisation du processus de téléchargement.
* Téléchargement de parties du fichier.
* Finalisation du processus de téléchargement.

#### Point de terminaison de démarrage/initialisation du téléchargement

Cette route met en jeu le processus de téléchargement. Ajoutez le code suivant pour créer un point de terminaison pour initialiser le processus de téléchargement multipartite :

```javascript
app.post("/start-upload", async (req, res) => {
  const { fileName, fileType } = req.body;

  const params = {
    Bucket: process.env.S3_BUCKET,
    Key: fileName,
    ContentType: fileType,
  };

  try {
    const upload = await s3.createMultipartUpload(params).promise();
    // console.log({ upload });
    res.send({ uploadId: upload.UploadId });
  } catch (error) {
    res.send(error);
  }
});

```

La fonction ci-dessus crée un point de terminaison POST **/start-upload** qui attend un corps JSON avec les propriétés `fileName` et `fileType`. Elle utilise ensuite la méthode `createMultipartUpload` du service S3 pour initialiser le processus de téléchargement multipartite. Si elle réussit, elle retourne l'`uploadId` à l'utilisateur, qui sera utilisé pour télécharger les parties du fichier.

#### Point de terminaison de téléchargement de partie

C'est la route où les différentes parties plus petites du téléchargement de fichier volumineux sont reçues et étiquetées. Ajoutez le code suivant pour créer un point de terminaison pour télécharger les parties du fichier :

```javascript
app.post("/upload-part", multerUpload.single("fileChunk"), async (req, res) => {
  const { fileName, partNumber, uploadId, fileChunk } = req.body;

  const params = {
    Bucket: process.env.S3_BUCKET,
    Key: fileName,
    PartNumber: partNumber,
    UploadId: uploadId,
    Body: Buffer.from(fileChunk, "base64"),
  };

  try {
    const uploadParts = await s3.uploadPart(params).promise();
    console.log({ uploadParts });
    res.send({ ETag: uploadParts.ETag });
  } catch (error) {
    res.send(error);
  }
});

```

La fonction ci-dessus crée un point de terminaison POST à l'adresse **/upload-part** qui attend un corps de données de formulaire avec les propriétés `uploadId`, `partNumber` et `fileName`. Elle utilise la méthode `uploadPart` du service S3 pour télécharger la partie du fichier. Si elle réussit, elle retourne l'`ETag` de la partie téléchargée au client.

L'`ETag` est un identifiant unique pour la partie de téléchargement qui sera utilisé pour finaliser le téléchargement multipartite.

#### Point de terminaison de finalisation du téléchargement

Une fois que la partie a été téléchargée, l'étape finale consiste à combiner toutes les parties pour créer l'objet final.

Ajoutez le code suivant pour créer un point de terminaison pour finaliser le processus de téléchargement multipartite :

```js
app.post("/complete-upload", async (req, res) => {
  const { fileName, uploadId, parts } = req.body;

  const params = {
    Bucket: process.env.S3_BUCKET,
    Key: fileName,
    UploadId: uploadId,
    MultipartUpload: {
      Parts: parts,
    },
  };

  try {
    const complete = await s3.completeMultipartUpload(params).promise();
    console.log({ complete });
    res.send({ fileUrl: complete.Location });
  } catch (error) {
    res.send(error);
  }
});

```

La fonction ci-dessus crée un point de terminaison POST à l'adresse **/complete-upload** qui attend un corps JSON avec les propriétés `uploadId`, `fileName` et `parts`. Elle utilise la méthode `completeMultipartUpload` du service S3 pour combiner les parties téléchargées et créer l'objet final. Si elle réussit, elle retourne l'objet de données contenant `fileUrl` concernant le téléchargement terminé.

### Démarrer le serveur

Enfin, ajoutez le code suivant pour démarrer le serveur Express :

```javascript
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

```

Ce code démarre le serveur Express sur le port 3001 et journalise un message dans la console lorsque le serveur est en cours d'exécution.

### Variables d'environnement

Créez un nouveau fichier nommé .env dans le répertoire racine de votre projet et ajoutez les variables d'environnement suivantes :

```bash
AWS_ACCESS_KEY=your-access-key
AWS_SECRET_KEY=your-secret-key
AWS_REGION=your-region
S3_BUCKET=your-bucket-name

```

Remplacez `your-access-key`, `your-secret-key`, `your-region` et `your-bucket-name` par vos identifiants AWS réels et le nom de votre bucket.

### Exécuter le serveur

Pour exécuter le serveur, exécutez la commande suivante dans votre terminal :

```bash
node app.js

```

Cela démarrera le serveur sur le port 3001.

## Étape 3 : Comment configurer le frontend avec React

Maintenant que le backend est configuré, créons un frontend React pour interagir avec le serveur et télécharger des fichiers vers S3 en utilisant le processus de téléchargement multipartite.

Le frontend sera responsable de la division du fichier en parties, du téléchargement de chaque partie vers le serveur et de la finalisation du processus de téléchargement.

### Comment initialiser un projet React

Créez un nouveau projet React en utilisant Create React App :

```bash
npx create-react-app s3-multipart-upload-frontend
cd s3-multipart-upload-frontend

```

### Installer les packages requis

Installez les packages suivants en utilisant npm :

```bash
  npm install axios

```

### Créer des composants

Créez un nouveau fichier nommé **Upload.js** dans le répertoire src/components et ajoutez le code suivant :

```javascript
import React, { useState } from "react";
import axios from "axios";

const CHUNK_SIZE = 5 * 1024 * 1024; // 5MB

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [fileUrl, setFileUrl] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileUpload = async () => {
    const fileName = file.name;
    const fileType = file.type;
    let uploadId = "";
    let parts = [];

    try {
      // Démarrer le téléchargement multipartite
      const startUploadResponse = await axios.post(
        "http://localhost:3001/start-upload",
        {
          fileName,
          fileType,
        }
      );

      uploadId = startUploadResponse.data.uploadId;

      // Diviser le fichier en morceaux et télécharger chaque partie
      const totalParts = Math.ceil(file.size / CHUNK_SIZE);

      console.log(totalParts);

      for (let partNumber = 1; partNumber <= totalParts; partNumber++) {
        const start = (partNumber - 1) * CHUNK_SIZE;
        const end = Math.min(start + CHUNK_SIZE, file.size);
        const fileChunk = file.slice(start, end);

        const reader = new FileReader();
        reader.readAsArrayBuffer(fileChunk);

        const uploadPart = () => {
          return new Promise((resolve, reject) => {
            reader.onload = async () => {
              const fileChunkBase64 = btoa(
                new Uint8Array(reader.result).reduce(
                  (data, byte) => data + String.fromCharCode(byte),
                  ""
                )
              );

              const uploadPartResponse = await axios.post(
                "http://localhost:3001/upload-part",
                {
                  fileName,
                  partNumber,
                  uploadId,
                  fileChunk: fileChunkBase64,
                }
              );

              parts.push({
                ETag: uploadPartResponse.data.ETag,
                PartNumber: partNumber,
              });
              resolve();
            };
            reader.onerror = reject;
          });
        };

        await uploadPart();
      }

      // Finaliser le téléchargement multipartite
      const completeUploadResponse = await axios.post(
        "http://localhost:3001/complete-upload",
        {
          fileName,
          uploadId,
          parts,
        }
      );

      setFileUrl(completeUploadResponse.data.fileUrl);
      alert("Fichier téléchargé avec succès");
    } catch (error) {
      console.error("Erreur lors du téléchargement du fichier :", error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button disabled={!file} onClick={handleFileUpload}>
        Télécharger
      </button>
      <hr />
      <br />
      <br />
      {fileUrl && (
        <a href={fileUrl} target="_blank" rel="noopener noreferrer">
          Voir le fichier téléchargé
        </a>
      )}
    </div>
  );
};

export default FileUpload;

```

Le composant `FileUpload` ci-dessus gère le processus de téléchargement de fichiers en utilisant la méthode de téléchargement multipartite. Il divise le fichier en morceaux, télécharge chaque partie vers le serveur et finalise le processus de téléchargement.

Le composant se compose des parties clés suivantes :

`CHUNK_SIZE` : La taille de chaque partie en octets. Dans ce cas, nous utilisons des parties de 5 Mo.

`handleFileChange` : Une fonction qui définit le fichier sélectionné dans l'état.

`handleFileUpload` : Une fonction qui initie le processus de téléchargement multipartite en envoyant le fichier au serveur en parties.

* Elle démarre le processus de téléchargement en appelant le point de terminaison **/start-upload** et récupère l'uploadId.
* Elle divise le fichier en morceaux et télécharge chaque partie vers le serveur en utilisant le point de terminaison **/upload-part**.
* Elle finalise le processus de téléchargement en appelant le point de terminaison **/complete-upload** avec l'uploadId et le tableau de parties.

`fileUrl` : Une variable d'état qui stocke l'URL du fichier téléchargé.

Le composant rend un champ d'entrée pour sélectionner un fichier, un bouton pour télécharger le fichier et un lien pour afficher le fichier téléchargé.

### Composant App

Mettez à jour le fichier App.js dans le répertoire src avec le code suivant :

```javascript

import React from "react";

import FileUpload from "./components/FileUpload";

function App() {
  return (
    <div className="App">
      <h1>Téléchargement de gros fichiers avec le téléchargement multipartite S3</h1>
      <FileUpload />
    </div>
  );
}


export default App;

```

Le composant App rend le composant FileUpload, qui gère le processus de téléchargement de fichiers.

### Comment démarrer le frontend

Pour exécuter le frontend, exécutez la commande suivante dans votre terminal :

```bash
npm start

```

Cela démarrera le serveur de développement React sur le port 3000 et ouvrira l'application dans votre navigateur web par défaut.

## Test

Testons l'application en téléchargeant un gros fichier en utilisant le frontend. Vous devriez voir le fichier être téléchargé en parties puis combiné pour créer l'objet final sur le serveur en inspectant votre onglet réseau.

### Téléchargement de partie

Dans l'image ci-dessous, le point de terminaison `start-upload` est appelé pour initialiser et démarrer le processus de téléchargement. Le gros fichier téléchargé est divisé en morceaux et téléchargé avec le point de terminaison `upload-part`. Vous pouvez voir jusqu'à 10 ou plus (selon la taille de chaque morceau par rapport à la taille totale du fichier).

Chaque partie de téléchargement a un identifiant unique `Etag` utilisé pour le téléchargement complet.

![Image téléchargée en parties](https://www.freecodecamp.org/news/content/images/2024/06/uplaod-start-parts.png)
_Image téléchargée en parties_

### Finalisation du téléchargement de partie

La dernière et dernière étape du processus est le point de terminaison `complete-upload` où les parties de téléchargement sont combinées pour former un seul objet pour le fichier téléchargé.

![Image téléchargée en parties](https://www.freecodecamp.org/news/content/images/2024/06/upload-complete.png)
_Téléchargements d'images terminés_

Vous pouvez cliquer sur `View Uploaded File` pour accéder à votre fichier téléchargé.

## Code complet sur GitHub

Cliquez sur le lien ci-dessous pour accéder au code complet sur GitHub :

[Multipart file uploads with react and NodeJS](https://github.com/Caesarsage/aws-multipart-uploads-react-node.git)

## Conclusion

Dans cet article, nous avons exploré comment gérer efficacement les gros fichiers avec le téléchargement multipartite Amazon S3. Nous avons discuté des avantages de l'utilisation de cette fonctionnalité, passé en revue le processus de téléchargement de fichiers en parties et fourni des exemples de code utilisant Node.js et React. 

Il s'agit d'une implémentation de haut niveau du processus de téléchargement multipartite, vous pouvez l'améliorer davantage en ajoutant plus de fonctionnalités comme le suivi de la progression, la gestion des erreurs et les téléchargements reprenables.

En tirant parti du téléchargement multipartite Amazon S3, vous pouvez optimiser les téléchargements de fichiers dans vos applications en divisant les gros fichiers en parties plus petites, en les téléchargeant indépendamment et en les combinant pour créer l'objet final. Cette approche non seulement améliore les performances de téléchargement, mais ajoute également une tolérance aux pannes et une flexibilité pour mettre en pause et reprendre les téléchargements, ce qui la rend idéale pour gérer les gros fichiers sur des réseaux instables.