---
title: Comment créer un générateur de sous-titres vidéo avec l'API Gemini
date: '2024-12-11T15:28:11.973Z'
author: Sanjay
authorURL: https://www.freecodecamp.org/news/author/sanjayxr/
originalURL: https://freecodecamp.org/news/build-a-video-subtitle-generator-using-the-gemini-api
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733638398422/2f468b16-5801-4f8c-bf40-c24d07e219b7.jpeg
tags:
- name: gemini
  slug: gemini
- name: React
  slug: reactjs
- name: Express
  slug: express
seo_desc: 'In this tutorial, you''ll build an AI-powered subtitle generator using
  Google''s Gemini API. We''ll create a project called “AI-Subtitle-Generator” using
  React for the front end and Express for the back end. Get ready for a fun and practical
  project.

  Ta...'
---


Dans ce tutoriel, vous allez créer un générateur de sous-titres alimenté par l'IA en utilisant l'API Gemini de Google. Nous allons créer un projet appelé « AI-Subtitle-Generator » en utilisant React pour le front end et Express pour le back end. Préparez-vous pour un projet pratique et amusant.

<!-- more -->

## Table des matières

-   [Comment obtenir votre clé API][1]
    
-   [Configuration du projet][2]
    
-   [Configuration du Front End][3]
    
-   [Configuration du serveur][4]
    
-   [Mise à jour du Front End][5]
    
-   [Résumé][6]
    
-   [Conclusion][7]
    

### Prérequis

Pour réaliser ce projet, vous devez connaître les bases de React et d'Express.

## Comment obtenir votre clé API

Une clé API agit comme un identifiant unique et authentifie vos requêtes auprès du service. Elle est essentielle pour accéder et utiliser les capacités de l'IA Gemini. Cette clé permettra à notre application de communiquer avec Gemini et nous aidera à construire notre projet.

Allez sur [Google AI Studio][8], puis cliquez sur « Get API Key » :

![Capture d'écran de Google AI Studio montrant le bouton 'Get API Key'](https://cdn.hashnode.com/res/hashnode/image/upload/v1733571839232/f5636fd0-c3cd-4c1b-bf7f-5200bce41444.png)

Après avoir été redirigé vers la page API KEY, cliquez sur « Create API Key » :

![Capture d'écran montrant comment créer une clé API dans Google AI Studio.](https://cdn.hashnode.com/res/hashnode/image/upload/v1733572045638/c950f7a2-613c-4976-905a-ce5c9dceb901.png)

Une nouvelle API KEY sera créée. Assurez-vous de copier la clé.

Ceci est votre clé API. Elle est utilisée pour authentifier les requêtes de votre application auprès de l'API Gemini. Chaque fois que votre application envoie une requête à Gemini, cette clé doit être incluse. Gemini utilise cette clé pour vérifier que la requête provient d'une source autorisée. Sans cette clé API, vos requêtes seront rejetées et vous ne pourrez pas accéder aux services de Gemini.

## Configuration du projet

Commencez par créer un nouveau dossier pour votre projet. Appelons-le `ai-subtitle-generator`.

À l'intérieur du dossier `ai-subtitle-generator`, créez deux sous-dossiers : `client` et `server`. Le dossier `client` contiendra le frontend React, et le dossier `server` contiendra le backend Express.

## Configuration du Front End

Tout d'abord, nous allons nous concentrer sur le front end et mettre en place une application React de base.

Naviguez vers le dossier `client` :

```
cd client
```

Ensuite, créez un nouveau projet React en utilisant Vite. Pour ce faire, exécutez la commande suivante :

```
npm create vite@latest .
```

Lorsque vous y êtes invité, choisissez « React ». Sélectionnez « React + TS » ou « React + JS ». Dans ce tutoriel, j'utiliserai React + TS. Vous pouvez également suivre avec JS.

Ensuite, installez les dépendances avec cette commande :

```
npm install
```

Puis démarrez le serveur de développement :

```
npm run dev
```

#### Comment gérer l'upload de fichiers dans le frontend

Maintenant, dans `client/src/App.tsx`, ajoutez le code suivant :

```
//  client/src/App.tsx

const App = () => {
    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>): Promise<void> => {
    e.preventDefault();
    try {
      const formData = new FormData(e.currentTarget);
      console.log(formData)
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="video/*,.mkv" name="video" />
        <input type="submit" />
      </form>
    </div>
  );
};

export default App;
```

Dans le code ci-dessus, nous avons utilisé une balise input qui acceptera la vidéo et la nommera `video`. Ce nom sera ajouté à l'objet `FormData`.

Lors de l'envoi de la vidéo au serveur, nous devons l'envoyer sous forme de paire clé-valeur, où la clé est `video` et la valeur est les données du fichier.

Pourquoi des paires clé-valeur ? Parce que lorsque le serveur reçoit la requête, il doit parser les morceaux (chunks) entrants. Après le parsing, les données vidéo seront disponibles dans `req.files[key]`, où `key` est le nom que nous avons attribué dans le frontend (`video` dans ce cas).

C'est pourquoi nous utilisons l'objet `FormData`. Lorsque nous créons une nouvelle instance de `FormData` et que nous lui passons `e.target`, tous les champs du formulaire et leurs noms seront automatiquement disponibles sous forme de paires clé-valeur.

## Configuration du serveur

Maintenant que nous avons notre clé API, configurons le serveur backend. Ce serveur gérera les uploads de vidéos depuis le frontend et communiquera avec l'API Gemini pour la génération de sous-titres.

Naviguez vers le dossier `server` :

```
cd server
```

Et initialisez le projet :

```
npm init -y
```

Ensuite, installez les paquets nécessaires :

```
npm install express dotenv cors @google/generative-ai express-fileupload nodemon
```

Voici les dépendances back-end que nous utilisons dans ce projet :

-   `express` **:** Le framework web pour créer l'API backend.
    
-   `dotenv` **:** Charge les variables d'environnement depuis un fichier `.env`.
    
-   `cors` **:** Active le Cross-Origin Resource Sharing, permettant à votre frontend de communiquer avec votre backend.
    
-   `@google/generative-ai` **:** La bibliothèque Google AI pour interagir avec l'API Gemini.
    
-   `express-fileupload` **:** Gère les uploads de fichiers, facilitant l'accès aux fichiers téléchargés sur le serveur.
    
-   `nodemon` **:** Redémarre automatiquement le serveur lorsque vous modifiez votre code.
    

### Configurer les variables d'environnement

Maintenant, créez un fichier nommé `.env`. C'est ici que vous gérerez vos clés API.

```
//.env
API_KEY = VOTRE_CLE_API
PORT = 3000
```

### Mettre à jour le `package.json`

Pour ce projet, nous utilisons les modules ES6 au lieu de CommonJS. Pour activer cela, mettez à jour votre fichier `package.json` avec le code suivant :

```
{
  "name": "server",
  "version": "1.0.0",
  "main": "index.js",
  "type": "module",       //Ajoutez "type": "module" pour activer les modules ES6
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"    //configurer nodemon
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": "",
  "dependencies": {
    "@google/generative-ai": "^0.21.0",
    "cors": "^2.8.5",
    "dotenv": "^16.4.7",
    "express": "^4.21.1",
    "express-fileupload": "^1.5.1",
    "nodemon": "^3.1.7"
  }
}
```

### Configuration de base d'Express

Créez un fichier `server.js`. Maintenant, configurons une application Express de base.

```
//  server/server.js

import express from "express";
import { configDotenv } from "dotenv";
import fileUpload from "express-fileupload";
import cors from "cors"

const app = express();

configDotenv();           //configurer le env
app.use(fileUpload());    //cela parsera les données multipart
app.use(express.json());  // Activer le parsing JSON pour les corps de requête
app.use(cors())           //configurer cors

app.use("/api/subs",subRoutes);  // Utiliser les routes pour l'endpoint "/api/subs"

app.listen(process.env.PORT, () => {   //accéder au PORT depuis le .env
  console.log("server started");         
});
```

Dans ce code, nous créons une instance d'application Express puis chargeons nos variables d'environnement. C'est là que nous gardons en sécurité les données sensibles comme les clés API. Ensuite, nous appliquons des fonctions middleware : `fileUpload` prépare le serveur à recevoir les vidéos uploadées, `express.json` nous permet de recevoir des données JSON, et `cors` active la communication entre notre frontend et notre backend.

Nous définissons une route `(/api/subs)` qui gérera toutes les requêtes liées à la génération de sous-titres. La logique spécifique pour ces routes sera définie dans `subs.routes.js`. Enfin, nous démarrons le serveur, en lui demandant d'écouter les requêtes sur le port spécifié dans notre fichier `.env`.

Nous devons maintenant créer quelques dossiers pour organiser le code. Vous pourriez gérer tout le code dans un seul fichier, mais le structurer en dossiers séparés sera plus facile à gérer.

Voici la structure finale des dossiers pour le serveur :

```
server/
├── server.js
├── controller/
│   └── subs.controller.js
├── gemini/
│   ├── gemini.config.js
├── routes/
│   └── subs.routes.js
├── uploads/
├── utils/
│   ├── fileUpload.js
│   └── genContent.js
└── .env
```

**Note :** Ne vous inquiétez pas de créer cette structure de dossiers maintenant. C'est juste pour référence. Suivez-moi étape par étape, et nous construirons cette structure ensemble.

### Créer les routes

Maintenant, créez un dossier `routes` puis créez `subs.routes.js` :

```
// server/routes/sub.routes.js

import express from "express"
import { uploadFile } from "../controller/subs.controller.js"    // importer la fonction uploadFile depuis le dossier controller

const router = express.Router()

router.post("/",uploadFile)    // définir une route POST qui appelle la fonction uploadFile

export default router     // exporter le routeur pour l'utiliser dans le fichier server.js principal
```

Ce code définit les routes pour notre serveur, plus précisément la route qui gère les uploads de vidéos et la génération de sous-titres.

Nous créons une nouvelle instance de routeur en utilisant `express.Router()`. Cela nous permet de définir des routes séparément de notre fichier serveur principal, améliorant ainsi l'organisation du code. Nous définissons une route POST sur le chemin racine `("/")` de notre endpoint API. Lorsqu'une requête POST est faite sur cette route (ce qui arrivera lorsqu'un utilisateur soumettra le formulaire d'upload de vidéo sur le frontend), la fonction `uploadFile` est appelée. Cette fonction gérera l'upload réel et la génération de sous-titres.

Enfin, nous exportons le routeur afin qu'il puisse être utilisé dans notre fichier serveur principal `(server.js)` pour connecter cette route à l'application principale.

### Configurer Gemini

Maintenant, configurons la manière dont notre application interagira avec Gemini.

Créez un dossier `gemini` puis créez un nouveau fichier nommé `gemini.config.js` :

```
//  server/gemini/gemini.config.js

import {
  GoogleGenerativeAI,
  HarmBlockThreshold,
  HarmCategory,
} from "@google/generative-ai";
import { configDotenv } from "dotenv";
configDotenv();

const genAI = new GoogleGenerativeAI(process.env.API_KEY);  // Initialiser Google Generative AI avec la clé API

const safetySettings = [
  {
    category: HarmCategory.HARM_CATEGORY_HARASSMENT,
    threshold: HarmBlockThreshold.BLOCK_NONE,
  },
  {
    category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
    threshold: HarmBlockThreshold.BLOCK_NONE,
  },
  {
    category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
    threshold: HarmBlockThreshold.BLOCK_NONE,
  },
  {
    category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    threshold: HarmBlockThreshold.BLOCK_NONE,
  },
];

const model = genAI.getGenerativeModel({
  model: "gemini-1.5-flash-001",    //choisir le modèle
  safetySettings: safetySettings,   //paramètres de sécurité optionnels
});

export default model;    //exporter le modèle
```

Dans le code ci-dessus, les `safetySettings` sont facultatifs. Ces paramètres vous permettent de définir des seuils pour les contenus potentiellement dangereux (comme les discours de haine, la violence ou le matériel explicite) dans la sortie de Gemini.

Vous pouvez en savoir plus sur les paramètres de sécurité de Gemini [ici][9].

### Créer un contrôleur pour gérer la logique des endpoints

Maintenant, créez un dossier `controller`, et à l'intérieur, créez un fichier nommé `subs.controller.js`. Dans ce fichier, vous gérerez la logique de l'endpoint pour interagir avec le modèle Gemini.

Dans `server/controller/subs.controller.js`, ajoutez ce code :

```
// server/controller/subs.controller.js

import { fileURLToPath } from "url";
import path from "path";
import fs from "fs";

const __filename = fileURLToPath(import.meta.url);  //convertit l'URL du module en chemin de fichier
const __dirname = path.dirname(__filename);   //récupère le répertoire du fichier actuel

export const uploadFile = async (req, res) => {
  try {
    if (!req.files || !req.files.video) {   //si aucun fichier n'est disponible, retourner une erreur au client
      return res.status(400).json({ error: "No video uploaded" });
    }

    const videoFile = req.files.video;   //accéder à la vidéo
    const uploadDir = path.join(__dirname, "..", "uploads");   //chemin pour uploader la vidéo temporairement

    if (!fs.existsSync(uploadDir)) {   //vérifier si le répertoire existe
      fs.mkdirSync(uploadDir);      //sinon, en créer un nouveau
    }

    const uploadPath = path.join(uploadDir, videoFile.name);  

    await videoFile.mv(uploadPath);  //déplace la vidéo du buffer vers le dossier "uploads"

    return res.status(200).json({ message:"file uploaded sucessfully" });
  } catch (error) {
    return res
      .status(500)
      .json({ error: "Internal server error: " + error.message });
  }
};
```

Puisque nous utilisons un module ES6, `__dirname` n'est pas disponible par défaut. Le mécanisme de gestion des fichiers est différent par rapport à CommonJS. Pour cette raison, nous utiliserons `fileURLToPath` pour gérer les chemins de fichiers.

Nous avons déplacé le fichier de l'emplacement temporaire par défaut (le buffer) vers le dossier `uploads`.

Mais le processus d'upload n'est pas encore terminé. Nous devons encore envoyer le fichier au Google AI File Manager, et après l'upload, il retournera un URI. Cet URI sera ensuite passé au modèle pour l'analyse vidéo.

### Comment uploader un fichier sur le Google AI File Manager

Créez un dossier `utils` et créez un fichier `fileUpload.js`. Vous pouvez vous référer à la structure de dossiers fournie plus haut.

```
//  server/utils/fileUpload.js

import { GoogleAIFileManager, FileState } from "@google/generative-ai/server";
import { configDotenv } from "dotenv";
configDotenv();

export const fileManager = new GoogleAIFileManager(process.env.API_KEY);  //créer une nouvelle instance de GoogleAIFileManager

export async function fileUpload(path, videoData) {  
  try {
    const uploadResponse = await fileManager.uploadFile(path, {   //donner le chemin comme argument
      mimeType: videoData.mimetype,  
      displayName: videoData.name,
    });
    const name = uploadResponse.file.name;
    let file = await fileManager.getFile(name);    
    while (file.state === FileState.PROCESSING) {     //vérifier l'état du fichier
      process.stdout.write(".");
      await new Promise((res) => setTimeout(res, 10000));   //vérifier toutes les 10 secondes
      file = await fileManager.getFile(name);
    }
    if (file.state === FileState.FAILED) {   
      throw new Error("Video processing failed");
    }
    return file;   // retourner l'objet file, contenant les informations du fichier uploadé et l'uri
  } catch (error) {
    throw error;
  }
}
```

Dans le code ci-dessus, nous avons créé une fonction appelée `fileUpload` qui prend deux arguments. Ces arguments seront passés depuis la fonction du contrôleur, que nous configurerons plus tard.

La fonction `fileUpload` utilise la méthode `fileManager.uploadFile` pour envoyer la vidéo aux serveurs de Google. Cette méthode nécessite deux arguments : le chemin du fichier et un objet contenant les métadonnées du fichier (son type MIME et son nom d'affichage).

Parce que le traitement vidéo sur les serveurs de Google prend du temps, nous devons vérifier l'état du fichier. Nous le faisons en utilisant une boucle qui vérifie l'état du fichier toutes les 10 secondes via `fileManager.getFile()`. La boucle continue tant que l'état du fichier est `PROCESSING`. Une fois que l'état passe à `SUCCESS` ou `FAILED`, la boucle s'arrête.

La fonction vérifie ensuite si le traitement a réussi. Si c'est le cas, elle renvoie l'objet file, qui contient des informations sur la vidéo téléchargée et traitée, y compris son URI. Sinon, si l'état est `FAILED`, la fonction lève une erreur.

### Passer l'URI au modèle Gemini

Maintenant, dans le dossier `utils`, créez un fichier appelé `genContent.js` :

```
// server/utils/genContent.js

import model from "../gemini/gemini.config.js";
import { configDotenv } from "dotenv";
configDotenv();

export async function getContent(file) {
  try {
    const result = await model.generateContent([
      {
        fileData: {
          mimeType: file.mimeType,
          fileUri: file.uri,
        },
      },
      {
        text: "You need to write a subtitle for this full video, write the subtitle in the SRT format, don't write anything else other than a subtitle in the response, create accurate subtitle.",
      },
    ]);
    return result.response.text();
  } catch (error) {
    throw error;
  }
}
```

Importez le modèle que nous avons configuré précédemment. Créez une fonction appelée `getContent`. La fonction `getContent` prend l'objet file (renvoyé par la fonction `fileUpload`).

Passez l'URI du fichier et le `mimeType` au modèle. Ensuite, nous fournirons un prompt demandant au modèle de générer des sous-titres pour l'intégralité de la vidéo au format SRT. Vous pouvez également ajouter votre propre prompt si vous le souhaitez. Enfin, retournez la réponse.

### Mettre à jour le fichier `subs.controller.js`

Enfin, nous devons mettre à jour le fichier du contrôleur. Nous avons créé les fonctions `fileUpload` et `getContent`, et nous allons maintenant les utiliser dans le contrôleur en fournissant les arguments requis.

Dans `server/controller/subs.controller.js` :

```
//  server/controller/subs.controller.js

import { fileURLToPath } from "url";
import path from "path";
import fs from "fs";
import { fileUpload } from "../utils/fileUpload.js";
import { getContent } from "../utils/genContent.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const uploadFile = async (req, res) => {
  try {
    if (!req.files || !req.files.video) {
      return res.status(400).json({ error: "No video uploaded" });
    }

    const videoFile = req.files.video;
    const uploadDir = path.join(__dirname, "..", "uploads");

    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir);
    }

    const uploadPath = path.join(uploadDir, videoFile.name);

    await videoFile.mv(uploadPath);

    const response = await fileUpload(uploadPath, req.files.video);  //nous passons 'uploadPath' et les données du fichier vidéo à 'fileUpload'
    const genContent = await getContent(response);   //la 'response' (contenant l'URI du fichier) est passée à 'getContent'

    return res.status(200).json({ subs: genContent });   //// retourner les sous-titres générés au client
  } catch (error) {
    console.error("Error uploading video:", error);
    return res
      .status(500)
      .json({ error: "Internal server error: " + error.message });
  }
};
```

Avec cela, l'API backend est terminée. Maintenant, nous allons passer à la mise à jour du front end.

## Mise à jour du Front End

Notre frontend permet actuellement uniquement aux utilisateurs de sélectionner une vidéo. Dans cette section, nous allons le mettre à jour pour envoyer les données vidéo à notre backend pour traitement. Le frontend recevra ensuite les sous-titres générés par le backend et lancera le téléchargement du fichier `.srt`.

Naviguez vers le dossier `client` :

```
cd client
```

Installez `axios`. Nous l'utiliserons pour gérer les requêtes HTTP.

```
npm install axios
```

Dans `client/src/App.tsx` :

```
//   client/src/App.tsx

import axios from "axios";

const App = () => {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>): Promise<void> => {
    e.preventDefault();
    try {
      const formData = new FormData(e.currentTarget);
      // envoi d'une requête POST avec les données du formulaire
      const response = await axios.post(
        "http://localhost:3000/api/subs/",   
        formData
      );
// création d'un Blob à partir de la réponse du serveur et déclenchement du téléchargement du fichier
      const blob = new Blob([response.data.subs], { type: "text/plain" }); 
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = "subtitle.srt";
      link.click();
      link.remove();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="video/*,.mkv" name="video" />
        <input type="submit" />
      </form>
    </div>
  );
};

export default App;
```

`axios` effectue la requête POST vers l'endpoint de votre API backend `(/api/subs)`. Le serveur traitera la vidéo, ce qui peut prendre un certain temps.

Une fois que le serveur envoie les sous-titres générés, le frontend les reçoit en réponse. Pour gérer cette réponse et permettre aux utilisateurs de télécharger les sous-titres, nous utiliserons un Blob. Un Blob (Binary Large Object) est un objet de l'API web qui représente des données binaires brutes, agissant essentiellement comme un fichier. Dans notre cas, les sous-titres renvoyés par le serveur seront convertis en Blob, ce qui nous permettra ensuite de déclencher un téléchargement dans le navigateur de l'utilisateur.

## Résumé

Dans ce tutoriel, vous avez appris à créer un générateur de sous-titres alimenté par l'IA en utilisant l'API Gemini de Google, React et Express. Vous pouvez uploader des vidéos, les envoyer à l'API Gemini pour la génération de sous-titres, et proposer les sous-titres générés au téléchargement.

## Conclusion

C'est tout ! Vous avez réussi à créer un générateur de sous-titres alimenté par l'IA en utilisant l'API Gemini. Pour des tests plus rapides, commencez par de courts clips vidéo (3 à 5 minutes). Les vidéos plus longues peuvent prendre plus de temps à être traitées.

Vous voulez créer une application de prompting vidéo personnalisable ? Ajoutez simplement un champ de saisie pour permettre aux utilisateurs d'entrer leurs propres prompts, envoyez ce prompt au serveur et utilisez-le à la place du prompt codé en dur. C'est tout ce qu'il faut.

Pour plus d'informations sur l'API Gemini, consultez la [documentation officielle de l'API Gemini][10].

Vous pouvez trouver le code complet ici : [AI-Subtitle-Generator][11]

S'il y a des erreurs ou si vous avez des questions, contactez-moi sur [LinkedIn][12] ou [Instagram][13].

Merci de m'avoir lu !

[1]: #heading-comment-obtenir-votre-cle-api
[2]: #heading-configuration-du-projet
[3]: #heading-configuration-du-front-end
[4]: #heading-configuration-du-serveur
[5]: #heading-mise-a-jour-du-front-end
[6]: #heading-resume
[7]: #heading-conclusion
[8]: https://aistudio.google.com/prompts/new_chat
[9]: https://ai.google.dev/gemini-api/docs/safety-settings
[10]: https://ai.google.dev/gemini-api/docs#node.js
[11]: https://github.com/sanjayr-12/ai-subtitle-generator
[12]: https://www.linkedin.com/in/sanjay-r-ab6064294/
[13]: https://www.instagram.com/heheheh_pet/profilecard/?igsh=eXh3MWw4ZzZ3NTRq