---
title: Comment créer et déployer un service d'hébergement d'images sur Sevalla
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-09-26T13:15:09.317Z'
originalURL: https://freecodecamp.org/news/build-and-deploy-an-image-hosting-service-on-sevalla
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758890260515/c4b83d17-c783-425c-ab11-50961e44ea58.png
tags:
- name: JavaScript
  slug: javascript
- name: image processing
  slug: image-processing
- name: image
  slug: image
seo_title: Comment créer et déployer un service d'hébergement d'images sur Sevalla
seo_desc: 'When most people think of image hosting, they imagine uploading photos
  to a cloud service and getting back a simple link.

  It feels seamless, but behind that experience sits a powerful set of technologies.
  At the core is something called object storag...'
---

Quand la plupart des gens pensent à l'hébergement d'images, ils imaginent télécharger des photos sur un service cloud et recevoir en retour un simple lien.

Cela semble fluide, mais derrière cette expérience se cache un ensemble de technologies puissantes. Au cœur se trouve ce qu'on appelle l'Object Storage, qui est une manière différente de gérer les fichiers par rapport aux bases de données ou aux systèmes de fichiers traditionnels.

Dans cet article, nous allons construire un service d'hébergement d'images complet en utilisant [Node.js](https://nodejs.org/en) et Express, le connecter à un Object Storage, et enfin, déployer l'ensemble du projet sur [Sevalla](https://sevalla.com/).

À la fin, vous disposerez d'une application fonctionnelle qui permet aux utilisateurs de télécharger des images et de les récupérer via des URL hébergées, le tout fonctionnant en direct sur le cloud.

## **Table des matières**

* [Qu'est-ce que l'Object Storage ?](#heading-quest-ce-que-lobject-storage)
    
* [Ce que nous allons construire](#heading-ce-que-nous-allons-construire)
    
* [Comment configurer le projet](#heading-comment-configurer-le-projet)
    
* [Comment créer votre Object Storage](#heading-comment-creer-votre-object-storage)
    
* [Comment déployer votre projet sur Sevalla](#heading-comment-deployer-votre-projet-sur-sevalla)
    
* [Pourquoi ce projet est important](#heading-pourquoi-ce-projet-est-important)
    
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce que l'Object Storage ?**

Pour comprendre pourquoi notre projet est conçu de cette manière, nous devons d'abord comprendre l'Object Storage.

Les systèmes de stockage de fichiers traditionnels enregistrent les fichiers dans une hiérarchie de dossiers, comme l'explorateur de fichiers de votre ordinateur. Les systèmes de stockage par blocs, souvent utilisés dans les bases de données, divisent les données en morceaux et les gèrent pour la rapidité et la fiabilité.

L'Object Storage est différent. Il traite chaque fichier, qu'il s'agisse d'une image, d'une vidéo ou d'un document, comme un objet unique. Chaque objet est stocké avec ses métadonnées et un identifiant unique à l'intérieur d'une structure plate, généralement appelée un bucket.

Cette architecture plate rend l'Object Storage évolutif presque sans limite. Au lieu de vous soucier des chemins de fichiers ou des répertoires, vous placez simplement un objet dans un bucket et recevez un identifiant en retour.

[Amazon S3](https://aws.amazon.com/s3/) est la norme de l'industrie pour l'Object Storage, offrant une échelle massive, une réplication mondiale et des fonctionnalités avancées, mais il s'accompagne d'une complexité accrue et de coûts souvent imprévisibles. L'Object Storage de Sevalla, en revanche, est conçu pour les développeurs qui souhaitent la même durabilité et évolutivité sans la courbe d'apprentissage abrupte.

Il offre une configuration plus simple et est compatible avec S3, donc interagir avec lui est identique à l'utilisation d'un bucket S3 sans la configuration et la complexité supplémentaires. Alors que S3 est idéal pour les entreprises gérant des pétaoctets de données, la solution de Sevalla est parfaite pour des projets comme l'hébergement d'images, des blogs ou des applications mobiles où la facilité d'utilisation et la rapidité comptent le plus.

## **Ce que nous allons construire**

Nous allons créer un service d'hébergement d'images simple mais pratique. À la base, le service permet à un utilisateur d'envoyer une image via une requête HTTP. Le serveur acceptera cette image, la traitera et la stockera dans l'Object Storage.

L'utilité d'un tel projet va bien au-delà d'un simple exercice de codage. Si vous construisez un blog, vous pourriez utiliser ce service pour stocker les images de vos articles sans vous soucier de la gestion des fichiers sur votre serveur web.

Si vous développez une application mobile qui nécessite des photos de profil ou le partage d'images, ce backend peut servir de base. Même si vous voulez simplement comprendre comment les applications cloud-native gèrent les téléchargements de fichiers, ce projet vous offre une expérience pratique et claire.

À la fin, vous n'aurez pas seulement du code tournant localement. Nous déploierons l'application sur Sevalla, ce qui signifie que votre service d'hébergement d'images sera en ligne, évolutif et accessible à toute personne disposant d'un lien.

## **Comment configurer le projet**

Commençons par configurer un projet Node.js. Vous pouvez [cloner ce dépôt](https://github.com/manishmshiva/image-host) si vous ne voulez pas configurer le projet de zéro.

Créez un nouveau répertoire de projet, initialisez-le avec npm et installez les dépendances requises.

```plaintext
npm init -y
npm i express multer dotenv @aws-sdk/client-s3 @aws-sdk/s3-request-presigner
```

Nous utiliserons [Express](https://expressjs.com/) pour notre serveur web, [Multer](https://www.npmjs.com/package/multer) pour gérer les téléchargements de fichiers, et l'[AWS SDK](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/welcome.html) pour nous connecter à l'Object Storage. Multer agit comme un middleware, nous donnant un accès facile aux fichiers téléchargés. L'AWS SDK nous donne un accès programmatique à l'Object Storage, nous permettant de télécharger des fichiers et de générer des liens.

Écrivons un fichier `index.html` rapide et plaçons-le dans le répertoire `public/` pour servir d'interface utilisateur pour le téléchargement de fichiers.

```xml
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" /> <!-- Set character encoding -->
  <meta name="viewport" content="width=device-width,initial-scale=1" /> <!-- Mobile-friendly -->
  <title>Pic Host</title>

  <!-- Simple CSS styling for layout and form -->
  <style>
    :root { color-scheme: light dark; } /* Support dark/light themes */
    body { 
      font-family: system-ui, sans-serif; 
      max-width: 560px; 
      margin: 4rem auto; 
      padding: 0 1rem; 
    }
    h1 { font-size: 1.25rem; margin-bottom: 1rem; }
    form, .card { 
      border: 1px solid #9993; 
      padding: 1rem; 
      border-radius: 12px; 
    }
    input[type="file"] { margin: .5rem 0 1rem; }
    button { 
      padding: .6rem 1rem; 
      border-radius: 10px; 
      border: 1px solid #9995; 
      background: #0000FF; 
      cursor: pointer; 
    }
    #result { margin-top: 1rem; display: none; }
    #result a { word-break: break-all; } /* Break long URLs nicely */
  </style>
</head>
<body>
  <!-- Page heading -->
  <h1>Simple Image Host</h1>

  <!-- Upload form -->
  <form id="uploadForm" class="card">
    <label for="file">Choose image</label><br/>
    <input id="file" name="file" type="file" accept="image/*" required />
    <br/>
    <button type="submit">Upload</button>
    <!-- Status text (uploading, success, error) -->
    <div id="status" aria-live="polite" style="margin-top:.75rem;"></div>
  </form>

  <!-- Result card: hidden until an image is uploaded -->
  <div id="result" class="card">
    <div>
      <strong>Share this page:</strong> 
      <a id="pageUrl" href="#" target="_blank" rel="noopener"></a>
    </div>
  </div>

  <!-- Client-side JavaScript -->
  <script>
    const form = document.getElementById('uploadForm');   // Form element
    const statusEl = document.getElementById('status');   // Upload status
    const result = document.getElementById('result');     // Result box
    const pageUrlEl = document.getElementById('pageUrl'); // Share link
    const directUrlEl = document.getElementById('directUrl'); // (unused here)

    // Event listener for form submission
    form.addEventListener('submit', async (e) => {
      e.preventDefault(); // Prevent full-page reload
      statusEl.textContent = 'Uploading...'; 
      result.style.display = 'none';

      const fd = new FormData(); // FormData object for sending file
      const file = document.getElementById('file').files[0];
      if (!file) {
        statusEl.textContent = 'Pick a file first.';
        return;
      }
      fd.append('file', file); // Attach file to request

      try {
        // Send file to backend /upload route
        const res = await fetch('/upload', { method: 'POST', body: fd });
        if (!res.ok) throw new Error('Upload failed');
        const data = await res.json();

        // Show returned page URL
        pageUrlEl.textContent = data.pageUrl;
        pageUrlEl.href = data.pageUrl;

        // Display result card and reset form
        result.style.display = 'block';
        statusEl.textContent = 'Done!';
        form.reset();
      } catch (err) {
        // Handle error
        statusEl.textContent = 'Error: ' + err.message;
      }
    });
  </script>
</body>
</html>
```

Lorsqu'un utilisateur visite la page, il voit un formulaire de téléchargement simple avec un sélecteur de fichier. Il peut sélectionner une image sur son ordinateur et cliquer sur Upload. Ensuite, le JavaScript intercepte la soumission du formulaire à l'aide de `addEventListener('submit')`, empêche le navigateur d'effectuer un rafraîchissement complet de la page et, à la place, regroupe le fichier sélectionné dans un objet `FormData`.

Ce fichier est ensuite envoyé au serveur avec un appel `fetch` vers la route `/upload`. Si le serveur répond avec succès, le JSON renvoyé contient une `pageUrl`. Cette URL est affichée à l'intérieur de la carte de résultat, qui était initialement masquée. L'utilisateur peut maintenant copier ce lien et le partager avec d'autres.

Si quelque chose ne va pas, comme l'absence de fichier sélectionné, une erreur du serveur ou l'échec du téléchargement, le script met à jour le message d'état pour informer l'utilisateur.

Voici à quoi cela ressemble pour l'utilisateur.

![Index.html](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306506845/aed05c76-954e-4bae-a995-8efc2da89f10.jpeg align="center")

Maintenant, créons le backend en utilisant le fichier `server.js`.

```javascript
import path from "path"; // For working with file paths
import express from "express"; // Web framework to handle HTTP routes
import multer from "multer"; // Middleware for handling file uploads
import crypto from "crypto"; // Used to generate random unique IDs
import dotenv from "dotenv"; // Loads environment variables from .env file
import { fileURLToPath } from "url"; // For handling ES module file paths
import {
  S3Client,
  PutObjectCommand,
  HeadObjectCommand,
  GetObjectCommand,
} from "@aws-sdk/client-s3"; // AWS SDK commands for S3 operations
import { getSignedUrl } from "@aws-sdk/s3-request-presigner"; // To generate temporary signed URLs

dotenv.config(); // Load environment variables

// Setup paths for __dirname and __filename in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Bucket name from environment
const S3_BUCKET = process.env.S3_BUCKET;

// Create an S3 client (works with Sevalla-compatible storage as well)
const s3 = new S3Client({
  region: "auto", // Auto-region for Sevalla
  endpoint: process.env.ENDPOINT, // Custom endpoint for object storage
  credentials: {
    accessKeyId: process.env.AWS_ACCESS_KEY_ID, // From .env
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY, // From .env
  },
});

// Initialize Express app
const app = express();

// Serve static files (like index.html, CSS, JS) from "public" folder
app.use(express.static(path.join(__dirname, "public")));

// Multer setup: store uploaded files in memory (not on disk)
// Limit file size to 10MB
const upload = multer({
  storage: multer.memoryStorage(),
  limits: { fileSize: 10 * 1024 * 1024 },
});

// ---------- ROUTE 1: GET / ----------
// Serves the main HTML file (upload form)
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// ---------- ROUTE 2: POST /upload ----------
// Handles image uploads and stores them in object storage
app.post("/upload", upload.single("file"), async (req, res) => {
  try {
    // Check if file exists
    if (!req.file) return res.status(400).json({ error: "file is required" });

    // Generate a random ID for the file
    const id = crypto.randomUUID().replace(/-/g, "");
    const key = id;

    // Create a PutObjectCommand to upload file to S3/Sevalla
    const put = new PutObjectCommand({
      Bucket: S3_BUCKET,
      Key: key,
      Body: req.file.buffer,
      ContentType: req.file.mimetype,
      Metadata: {
        originalname: req.file.originalname || "",
      },
    });

    // Upload the file
    await s3.send(put);

    // Build a page URL for retrieving the image later
    const baseUrl = `${req.protocol}://${req.get("host")}`;
    const pageUrl = `${baseUrl}/i/${id}`;

    // Respond with the page URL
    res.json({ id, pageUrl });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "upload_failed" });
  }
});

// ---------- ROUTE 3: GET /i/:id ----------
// Redirects to a signed URL for secure access to the uploaded file
app.get("/i/:id", async (req, res) => {
  const { id } = req.params;
  const key = id;

  try {
    // Ensure the object exists in storage
    await s3.send(new HeadObjectCommand({ Bucket: S3_BUCKET, Key: key }));

    // Create a signed URL valid for 1 hour
    const command = new GetObjectCommand({ Bucket: S3_BUCKET, Key: key });
    const signedUrl = await getSignedUrl(s3, command, { expiresIn: 3600 });

    // Redirect user to the signed URL
    return res.redirect(302, signedUrl);
  } catch (err) {
    console.error(err);
    return res.status(404).send("Not found");
  }
});

// ---------- Boot the Server ----------
app.listen(process.env.PORT || 3000, () => {
  console.log(`Image host server listening for requests...`);
});
```

### Route 1 : `GET /`

C'est le point d'entrée de l'application. Lorsque vous ouvrez le navigateur et accédez à l'URL racine, il sert le fichier `index.html` du dossier `public`. Ce fichier contient le formulaire de téléchargement où l'utilisateur peut sélectionner une image et la soumettre.

### Route 2 : `POST /upload`

C'est là que la magie opère. Lorsqu'un utilisateur sélectionne une image et clique sur « Upload », le fichier est envoyé à cet endpoint. Multer gère le téléchargement du fichier en mémoire, puis le fichier est poussé vers l'Object Storage à l'aide de `PutObjectCommand`. Un identifiant unique aléatoire est généré comme clé pour le fichier. Une fois téléchargé, le serveur répond avec une `pageUrl` qui peut être utilisée pour visualiser l'image téléchargée plus tard.

### Route 3 : `GET /i/:id`

Cette route récupère une image téléchargée. Au lieu de servir le fichier directement, elle génère une URL signée valide pendant une heure à l'aide de `getSignedUrl`. Cette URL signée donne un accès temporaire au fichier stocké dans l'Object Storage. Le serveur redirige ensuite l'utilisateur vers cette URL signée. Si le fichier n'existe pas, il renvoie une erreur 404.

Avant d'exécuter ce code, nous avons besoin d'accéder à l'Object Storage et d'ajouter les valeurs dans un fichier d'environnement. Le code que vous voyez avec `process.env` récupère ces valeurs et nous aide à nous authentifier auprès de l'Object Storage pour lire et écrire des fichiers.

## **Comment créer votre Object Storage**

[Connectez-vous](https://app.sevalla.com/login) à Sevalla et cliquez sur « Object Storage ». Cliquez sur « Create Object Storage » et donnez-lui un nom.

![Object Storage Creation](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306560384/3e88b143-2fa9-465d-b3d6-e0e54c90a6a3.jpeg align="center")

Une fois créé, cliquez sur « Settings » et vous verrez la clé d'accès et la clé secrète. Nous avons besoin de ces quatre valeurs :

* Nom du bucket (Bucket name)
    
* URL de l'endpoint (Endpoint URL)
    
* Clé d'accès (Access Key)
    
* Clé secrète (Secret Key)
    

![Object Storage Access Keys](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306618051/90970694-3d7c-486f-b32a-54c83ca88c7f.jpeg align="center")

Copiez-les dans un fichier nommé `.env` au sein de votre projet.

```plaintext
AWS_ACCESS_KEY_ID=VOTRE_ID_DE_CLE_D_ACCES_ICI
AWS_SECRET_ACCESS_KEY=VOTRE_CLE_D_ACCES_SECRETE_ICI
S3_BUCKET=VOTRE_NOM_DE_BUCKET_ICI
ENDPOINT=VOTRE_URL_D_ENDPOINT_ICI
```

De plus, activez l'accès public dans les paramètres afin de pouvoir pousser des fichiers depuis votre environnement local.

![public access enabled](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306660300/7abe369e-f820-4770-82d7-27da03c9b7a9.jpeg align="center")

### **Tester l'application localement**

Vérifions que notre code fonctionne localement.

```bash
node server.js
```

Allez sur [http://localhost:3000/](http://localhost:3000/) et essayez de télécharger un fichier. Il devrait vous donner l'URL pour visualiser le fichier après un téléchargement réussi.

![File upload success](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306699833/b95b69ed-17f6-4fe9-b0a8-22e15876655d.jpeg align="center")

Vous pouvez visiter l'URL pour voir votre fichier téléchargé. Vous pouvez également vérifier s'il a bien été téléchargé en utilisant l'interface utilisateur de l'Object Storage.

![Object Storage UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306733665/35944857-71bb-4d1a-9e11-85c35c875465.jpeg align="center")

Super. Nous avons construit un service simple d'hébergement et de partage d'images. Maintenant, mettons cela dans le cloud.

## **Comment déployer votre projet sur Sevalla**

Tout d'abord, poussez votre projet sur GitHub ou [faites un fork de mon dépôt](https://github.com/manishmshiva/image-host). Ensuite, connectez-vous à votre tableau de bord Sevalla et créez une nouvelle application.

![Create application](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306768439/3be4f9ac-abd4-4b98-95e3-22b97a3eea1a.jpeg align="center")

Connectez votre compte GitHub, choisissez le dépôt qui contient votre service d'hébergement d'images et sélectionnez la branche que vous souhaitez déployer. Sevalla détectera automatiquement qu'il s'agit d'un projet Node.js et installera les dépendances. Il exécutera également l'application sur le port spécifié.

Pour configurer les identifiants AWS et les informations du bucket, allez dans la section des variables d'environnement de votre application et ajoutez vos `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION` et `S3_BUCKET_NAME`. Ces valeurs seront injectées dans votre application au moment de l'exécution, garantissant que les données sensibles ne sont pas codées en dur dans votre code source.

![Adding environment variables](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306811113/b5e1782d-2bce-4b9e-a654-a131e58a44cd.jpeg align="center")

Une fois les variables d'environnement ajoutées, allez dans « Overview » et cliquez sur « Deploy ».

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306855343/fbcfcd74-d74e-43ad-9b99-7f02421cf5df.jpeg align="center")

Attendez quelques minutes. Une fois le déploiement terminé, Sevalla vous donnera une URL en direct. Cliquez sur « Visit APP » pour accéder à la page de votre application.

![Live url](https://cdn.hashnode.com/res/hashnode/image/upload/v1757306886378/97705a1f-c625-4282-9ef0-042c8c01b431.jpeg align="center")

Félicitations ! Votre application est maintenant en ligne. Vous pouvez partager l'URL avec d'autres ou même ajouter un domaine personnalisé à votre application pour avoir votre propre solution d'hébergement d'images.

## **Pourquoi ce projet est important**

Ce projet est plus qu'un simple exercice de codage. Il vous apprend comment les applications modernes gèrent les fichiers à grande échelle, vous initie à l'Object Storage et montre comment intégrer des services cloud dans vos propres projets.

Avec Sevalla, vous avez également appris à déployer des applications prêtes pour la production, vous offrant le cycle complet, du prototype local au service cloud en direct.

Pour les développeurs qui créent des blogs, des applications mobiles ou même des outils internes, la capacité d'héberger des images de manière fiable et à grande échelle est inestimable. Avec l'Object Storage et un service Node.js simple, vous pouvez éviter de réinventer la roue et vous appuyer sur une infrastructure cloud éprouvée.

## **Conclusion**

Nous avons commencé par explorer l'Object Storage et pourquoi il est idéal pour gérer des fichiers comme des images. Nous avons ensuite construit une application Node.js qui accepte les téléchargements, les stocke dans l'Object Storage de Sevalla et renvoie des URL accessibles. Enfin, nous avons déployé l'application sur Sevalla, transformant un projet local en un service d'hébergement d'images en direct. En chemin, vous avez acquis non seulement du code fonctionnel, mais aussi une compréhension plus approfondie de la manière de construire des services cloud-native.

En terminant ce projet, vous disposez désormais d'un service d'hébergement d'images fonctionnel que vous pouvez étendre et adapter. Vous pourriez ajouter des fonctionnalités telles que l'authentification, le redimensionnement d'images ou même une meilleure interface front-end avec un UI en glisser-déposer. Plus important encore, vous avez expérimenté comment le développement et le déploiement s'articulent dans le logiciel moderne.