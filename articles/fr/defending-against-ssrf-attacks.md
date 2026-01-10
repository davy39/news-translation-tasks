---
title: Comment se défendre contre la falsification de requêtes côté serveur
subtitle: ''
author: Hamdaan Ali
co_authors: []
series: null
date: '2024-01-05T17:21:50.000Z'
originalURL: https://freecodecamp.org/news/defending-against-ssrf-attacks
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730833444910/4e483988-c1f3-4637-af6c-fcf2fbedbbb6.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Comment se défendre contre la falsification de requêtes côté serveur
seo_desc: 'Server-Side Request Forgery (SSRF) has been a consistent issue in application
  security and is among the OWASP Top 10 vulnerabilities.

  In this walkthrough, you''ll first learn what Server-Side Request Forgery is and
  how it differs from Client-Side Requ...'
---

La falsification de requêtes côté serveur (SSRF) est un problème récurrent en matière de sécurité des applications et figure parmi les 10 vulnérabilités les plus critiques selon l'OWASP.

Dans ce guide, vous apprendrez d'abord ce qu'est la falsification de requêtes côté serveur et en quoi elle diffère de la falsification de requêtes côté client. Nous créerons une application exemple pour mieux comprendre le fonctionnement des attaques par falsification de requêtes côté serveur, et explorerons diverses méthodes pour protéger notre application contre les vulnérabilités SSRF.

## Table des matières :

* [Prérequis](#heading-prerequisites)
    
* [Qu'est-ce que la falsification de requêtes côté serveur ?](#heading-quest-ce-que-la-falsification-de-requetes-cote-serveur)
    
* [En quoi le SSRF diffère-t-il du CSRF ?](#heading-en-quoi-le-ssrf-differe-t-il-du-csrf)
    
* [Identifier les mauvaises pratiques de code](#heading-identifier-les-mauvaises-pratiques-de-code)
    
* [Comprendre les points sensibles](#heading-comprendre-les-points-sensibles)
    
* [Installation du projet](#heading-installation-du-projet)
    
* [Comment exploiter la vulnérabilité](#heading-comment-exploiter-la-vulnerabilite)
    
* [Comment se défendre contre les attaques SSRF](#heading-comment-se-defendre-contre-les-attaques-ssrf)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

1. **Node et Express :** Nous créerons une application exemple en JavaScript utilisant le framework Express. Une compréhension basique du framework serait utile. Vous aurez besoin de l'[environnement d'exécution Node](https://nodejs.org/en/download/) pour exécuter les scripts.
    
2. **Client Postman :** Pour faire une requête API et exploiter la vulnérabilité, vous aurez besoin d'un outil pour faire des requêtes HTTP. Vous pouvez utiliser la fonction "Edit and Send" de votre navigateur web sous l'onglet Networks, mais comme tous les navigateurs ne permettent pas cela, il est préférable d'utiliser un outil comme [Postman](https://www.postman.com/downloads/) qui offre une meilleure interface pour observer les réponses.
    

## Qu'est-ce que la falsification de requêtes côté serveur ?

La falsification de requêtes côté serveur, ou SSRF, est une vulnérabilité de sécurité qui permet à des acteurs malveillants de manipuler le serveur pour qu'il effectue des requêtes non intentionnelles en son nom.

Le SSRF offre une opportunité à ces acteurs malveillants de faire des requêtes "depuis" le serveur alors qu'ils devraient faire des requêtes "vers" le serveur.

Pour comprendre ce que cela signifie, examinons l'exécution normale d'une requête à l'aide des diagrammes de séquence ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-104.png align="left")

*Diagramme de séquence UML pour l'exécution normale d'une requête*

Dans un scénario typique, un serveur traite les requêtes entrantes des clients. Les utilisateurs ou les systèmes externes initient ces requêtes, et le serveur répond en conséquence. Il s'agit d'une interaction client-serveur standard où le serveur agit en fonction des requêtes qu'il reçoit.

Voyons maintenant à quoi ressemble le SSRF :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-7.png align="left")

*Diagramme de séquence UML pour les attaques SSRF*

Dans les applications vulnérables au SSRF, les attaquants exploitent la capacité du serveur à faire des requêtes HTTP vers des ressources qui ne devraient pas être directement accessibles depuis l'internet public. Ces ressources peuvent inclure des ressources internes protégées, des API, des sites web ou des bases de données qui ne peuvent être accessibles que depuis le serveur.

Les attaquants y parviennent en trompant le serveur pour qu'il effectue des requêtes non intentionnelles vers diverses destinations, y compris des API internes, des pages HTML internes et des bases de données internes.

## En quoi le SSRF diffère-t-il du CSRF ?

Le SSRF est une attaque où un attaquant peut faire en sorte que le serveur effectue des requêtes en son nom. Cela implique de manipuler le serveur pour qu'il fasse des requêtes vers des ressources internes, ce qui peut entraîner des actions non autorisées ou la divulgation d'informations.

En revanche, dans le CSRF, ou falsification de requêtes côté client, l'attaquant trompe le navigateur d'un utilisateur pour qu'il effectue des requêtes non intentionnelles vers une application web spécifique pour laquelle l'utilisateur est déjà authentifié. Cela signifie que des actions sont effectuées au nom de l'utilisateur sans son consentement.

Les développeurs backend doivent être conscients du SSRF pour créer des applications sécurisées. En revanche, les développeurs frontend doivent être attentifs et mettre en œuvre des mesures de sécurité côté client pour prévenir les attaques CSRF.

## Identifier les mauvaises pratiques de code

Les attaques SSRF se produisent souvent lorsque les applications web gèrent incorrectement les entrées contrôlées par l'utilisateur, ce qui conduit à des requêtes réseau basées sur des entrées utilisateur insuffisamment assainies. Le traitement d'URL non assainies dans les requêtes API est un point d'entrée courant pour les attaques SSRF.

Un autre indice courant pour identifier les vulnérabilités SSRF dans vos applications est de vérifier les instances où l'analyse XML se produit sans validation adéquate des entités externes. Les applications qui ne valident pas et ne sécurisent pas correctement leurs analyseurs XML peuvent s'exposer involontairement à des risques SSRF.

Dans ce guide, vous allez créer un serveur qui prend une URL et l'utilise pour faire des requêtes réseau sans validation et assainissement appropriés. Vous verrez ensuite des moyens d'atténuer ce problème.

## Comprendre les points sensibles

Pour mieux comprendre le problème des attaques SSRF, créons une application exemple en utilisant Express et JavaScript. Ci-dessous se trouve un diagramme de séquence Mermaid où nous expliquons ce que fait la base de code :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-169.png align="left")

*Diagramme de séquence UML pour l'application exemple*

Nous allons créer une application Express avec deux endpoints — `/fetch`, une requête `GET` conçue pour récupérer le contenu d'une URL spécifiée, et `/admin`, une autre requête `GET`, qui est une API interne à l'organisation qui accède à une ressource protégée en interne.

Nous allons découvrir une vulnérabilité de sécurité associée à la falsification de requêtes côté serveur (SSRF) dans la mise en œuvre de la première requête `GET`.

Nous allons également créer une autre fonction d'assistance à l'endpoint `/uploads` pour permettre à nos clients de récupérer et de visualiser leur contenu récemment téléchargé.

## Installation du projet

Pour commencer, mettons rapidement en place notre dépôt et installons tous les packages nécessaires. À la racine de votre espace de travail, installez Express et Axios en utilisant la commande suivante :

```bash
npm init -y | npm i axios express
```

L'exécution de cette commande créera un fichier `package.json` avec les paramètres par défaut et installera les packages spécifiés.

Pour simuler la ressource protégée en interne, créons un fichier `data.json` à la racine de votre espace de travail :

```json
{   
    "name": "Hamdaan Ali Quatil",
    "password": "violinblackeye"
}
```

Maintenant, créez un fichier appelé `app.js` à la racine de votre dépôt. Ici, nous définirons tous nos endpoints. Importez tous les packages nécessaires comme ceci :

```javascript
const express = require('express');
const axios = require('axios');
const fs = require('fs').promises;
```

Nous utilisons le module `fs` (File System) pour interagir avec le système de fichiers local. Dans l'application Express, nous utilisons `fs.promises` pour lire le contenu d'un fichier. La fonction `fetchPrivateResource` lit de manière asynchrone le contenu du fichier `data.json`, qui est une ressource interne.

Créons une instance de l'application Express pour gérer les requêtes HTTP et définissons la méthode `fetchPrivateResource`. Dans l'application exemple, seul l'administrateur devrait pouvoir récupérer cette ressource interne, mais vous observerez comment un acteur malveillant peut y accéder en utilisant une attaque SSRF.

```js
const app = express();
const port = 3000;

// Fonction pour récupérer la ressource privée
const fetchPrivateResource = async () => {
  try {
    const content = await fs.readFile('data.json', 'utf-8');
    return content;
  } catch (error) {
    console.error('Erreur de lecture de la ressource privée :', error.message);
    throw error;
  }
};
```

### L'Endpoint Fetch

Maintenant, définissons notre premier endpoint, `/fetch` qui attend un paramètre de requête `url` contenant l'URL cible. À la réception d'une requête, le serveur utilise la bibliothèque Axios pour faire une requête GET à l'URL spécifiée.

```js
app.get("/fetch", async (req, res) => {
  const url = req.query.url;

  try {
    const response = await axios.get(url);
    const responseData = JSON.stringify(response.data);

    const filename = path.basename(url);
    const textFilePath = path.join(__dirname, "uploads", "upload-data.txt");

    await fs.writeFile(textFilePath, responseData, "utf-8");

    res.send("Téléchargement réussi");
  } catch (error) {
    console.error("Erreur :", error.message);
    res.status(500).send("Erreur interne du serveur");
  }
});
```

La méthode `axios.get` est utilisée pour effectuer la requête HTTP GET, et les données de réponse sont ensuite converties en une chaîne JSON. La chaîne résultante est écrite dans un fichier texte nommé `upload-data.txt` dans le dossier `uploads` du serveur. Enfin, un message de succès ou un message d'erreur est envoyé au client, selon le résultat de l'opération.

### L'Endpoint Uploads

Cela fait, créons un endpoint pour permettre aux utilisateurs d'accéder et de vérifier leurs fichiers téléchargés. Le serveur vérifiera si le fichier demandé existe, et si c'est le cas, il l'envoie au client. Lorsqu'un fichier ne peut pas être trouvé, le serveur retourne une erreur 404.

```js
app.get("/uploads/:filename", async (req, res) => {
  const filename = req.params.filename;
  const filePath = path.join(__dirname, "uploads", filename);
  console.log(filePath);

  try {
    // Vérifier si le fichier existe
    await fs.access(filePath);

    // Si le fichier existe, l'envoyer au client
    res.sendFile(filePath);
    
  } catch (error) {
    res.status(404).send("Fichier non trouvé : " + error);
  }
});
```

### L'Endpoint Admin

Maintenant, nous devons créer une API interne — la route `/admin` — qui est intentionnellement protégée de l'accès public. L'objectif est de s'assurer que cette API n'est accessible que depuis localhost ou la machine locale (127.0.0.1).

Nous pouvons faire cela en implémentant un middleware qui agit comme une barrière de protection, permettant aux requêtes de se poursuivre vers la route `/admin` uniquement si elles proviennent de l'hôte local.

Le middleware vérifie si la propriété `req.hostname`, qui représente le nom d'hôte spécifié dans la requête HTTP, correspond à `localhost` ou `127.0.0.1`. Si la requête provient d'un autre hôte, le middleware répond avec un statut `403` Forbidden, restreignant ainsi l'accès.

```js
// middleware pour protéger l'API admin
app.use('/admin', async (req, res, next) => {
  const isLocalhost = req.hostname === 'localhost' || req.hostname === '127.0.0.1';
  
  if (isLocalhost) {
    next();
  } else {
    res.status(403).send('Accès interdit');
  }
});

// Route pour accéder à l'API admin
app.get('/admin', async (req, res) => {
  try {
    const content = await fetchPrivateResource();
    res.send(content);
  } catch (error) {
    res.status(500).send('Erreur interne du serveur');
  }
});
```

Une fois toutes les routes configurées, nous démarrons le serveur en utilisant la méthode `app.listen`, et il commence à écouter sur le port 3000 pour les requêtes entrantes.

```js
app.listen(port, () => {
  console.log(`Le serveur est en cours d'exécution sur http://localhost:${port}`);
});
```

Avec notre `app.js` maintenant configuré pour traiter les requêtes entrantes, exécutons l'application exemple en utilisant `nodemon` :

```bash
npm i -D nodemon | nodemon app.js
```

Le serveur a démarré sur le port `3000`. Maintenant, nous sommes prêts à tester notre application exemple et à rechercher les mauvaises pratiques de code qui peuvent conduire à des attaques SSRF. Vous pouvez trouver le code complet ici — [GitHub Gist | HamdaanAliQuatil](https://gist.github.com/HamdaanAliQuatil/c7db6f3dd0666bd9396a7f4e6ebe6665).

## Comment exploiter la vulnérabilité

Essayons de faire une requête `GET` à l'API fetch. Nous simulons le processus de téléchargement d'un fichier texte en utilisant l'URL du fichier. Dans cette démonstration, nous allons récupérer le contenu d'un fichier exemple et le sauvegarder sur nos serveurs. Voici le [lien vers le fichier texte](https://example-files.online-convert.com/document/txt/example.txt).

Ouvrez votre client Postman et exécutez une requête `GET` avec l'URL `http://localhost:3000/fetch?url=https://example-files.online-convert.com/document/txt/example.txt`. Nous ajoutons le lien vers le fichier en tant que paramètre de requête dans l'endpoint `/fetch`. Lorsque vous envoyez la requête, vous verrez une réponse `"Téléchargement réussi"`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-3.png align="left")

*Client Postman : Endpoint Fetch*

Vous verrez que votre dépôt contient maintenant un nouveau fichier créé dans le répertoire `uploads`. Les clients peuvent maintenant accéder à leurs informations téléchargées en utilisant l'endpoint API `/uploads` pour visualiser leurs fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-4.png align="left")

*Client Postman : Endpoint Uploads*

Maintenant, envoyons une requête malveillante en changeant notre paramètre de requête en `http://120.0.07/admin` dans la même requête à l'endpoint `/fetch`. L'URL mise à jour ressemblera maintenant à ceci : `http://localhost:3000/fetch?url=http://127.0.0.1:3000/admin`.

Dans le paramètre de requête, `127.0.0.1` est une adresse de loopback. Une adresse de loopback est une adresse IP réservée utilisée pour établir des connexions réseau avec le même hôte (la machine locale) pour des tests et des communications au sein de l'appareil.

Ce que l'acteur malveillant tente de faire est d'effectuer une requête vers la route `/admin` du serveur depuis le serveur lui-même en utilisant l'adresse de loopback. Cela simule un scénario d'accès à une ressource interne.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-5.png align="left")

*Client Postman : Endpoint Admin*

Vous remarquerez qu'un message `"Téléchargement réussi"` apparaît en réponse à cette requête. Essayez maintenant d'accéder à nouveau à votre fichier téléchargé en utilisant la requête `GET` à l'endpoint `/upload`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-6.png align="left")

*Client Postman : Endpoint Uploads*

Vous verrez que le contenu du fichier téléchargé a été altéré. Cette altération met en évidence une attaque SSRF (Server-Side Request Forgery) réussie, où un acteur malveillant a profité de la capacité du serveur à initier des requêtes internes.

Le fichier, qui contenait initialement des données spécifiques, a maintenant été falsifié. Cela montre le potentiel d'accès non autorisé et de manipulation d'informations sensibles par le biais d'exploits SSRF.

## Comment se défendre contre les attaques SSRF

Maintenant, voyons les moyens de corriger la vulnérabilité de notre application au SSRF. La solution la plus intuitive qui vous vient à l'esprit pourrait être de ne jamais permettre à un client d'entrer une URL. C'est certainement la défense la plus puissante. Le serveur devrait créer une URL dont il a besoin.

Mais souvent, permettre des URL dans votre logique métier devient une nécessité absolue. Dans de tels cas, notre objectif est de prévenir l'attaque ou au moins de réduire le risque si une attaque se produit.

Si vous devez vraiment permettre une URL telle quelle, voici quelques étapes de précaution que vous pouvez prendre :

### Assainissement et validation

Comme pour la plupart des vulnérabilités, un point sensible dans les attaques SSRF est l'utilisation de données non fiables. Traitez toujours les données provenant du côté client comme non fiables.

L'assainissement et la validation des données fournies par le client devraient contribuer grandement à la défense contre les attaques SSRF. Une validation très intuitive consiste à restreindre toute URL contenant localhost ou l'adresse de loopback.

Créons une fonction d'assistance `isValidUrl` et appelons-la dans la fonction pour l'endpoint `/fetch`.

```js
function isValidUrl(url) {
  // Restreindre les URL à HTTP uniquement. Cela bloque FTP et autres protocoles
  const validUrlRegex = /^http:\/\/\S+$/;

  if (!validUrlRegex.test(url)) {
    return false;
  }

  try {
    const parsedUrl = new URL(url);

    // Vérifier si l'hôte est localhost ou une adresse IP de loopback
    const isLocalhost = parsedUrl.hostname === 'localhost';
    const isLocalIP = /^127\.\d+\.\d+\.\d+$/g.test(parsedUrl.hostname);

    return !(isLocalhost || isLocalIP);
  } catch (error) {
    return false;
  }
}
```

Votre fonction mise à jour pour l'endpoint `/fetch` devrait ressembler à ceci :

```js
app.get("/fetch", async (req, res) => {
  const url = req.query.url;

  if (!isValidUrl(url)) {
    res.status(400).send("Les URL de loopback ne sont pas autorisées");
    return;
  }

  try {
    ...
    res.send("Téléchargement réussi");
  } catch (error) {
	...
  }
});
```

Maintenant, retournez dans le client Postman et renvoyez la requête malveillante. Vous observerez que le fichier précédemment téléchargé n'a pas été altéré et vous recevez `"Les URL de loopback ne sont pas autorisées"` dans la réponse.

### Liste blanche via une liste d'autorisation

Vous pouvez créer une liste d'autorisation positive pour n'autoriser que certaines adresses IP de confiance, schémas d'URL et ports. Implémentons une liste d'autorisation et améliorons notre fonction `isValidUrl` :

```js
const whitelist = ["boost.com", "boost.in", "trustedDomain3.com"];
const allowedPorts = ['80', '443'];
```

Utilisez maintenant votre `whitelist` déclarée dans la fonction `isValidUrl` :

```js
function isValidUrl(url) {
  try {
    const parsedUrl = new URL(url);

    if (!whitelist.includes(parsedUrl.hostname)) {
      return false;
    }

    if (!allowedPorts.includes(parsedUrl.port)) {
      return false;
    }

    return true;
  } catch (error) {
    return false;
  }
}
```

Remarquez comment nous avons supprimé le besoin de regex. Cela nous amène à une autre technique d'atténuation que vous devez éviter :

### Ne pas utiliser une liste de refus

Vous ne devez jamais atténuer les vulnérabilités SSRF en utilisant une liste de refus ou des regex. Restreindre l'utilisation des adresses IP n'est pas simple. Pour comprendre pourquoi nous devons éviter une liste de refus, regardez l'exemple suivant.

Une adresse de loopback est généralement représentée par `127.0.0.1`. Il est assez facile de repérer cette adresse et de la rejeter. Mais un problème survient lorsqu'une requête malveillante est envoyée en utilisant d'autres formes de cette adresse de loopback qui pointent également vers la machine locale. Par exemple, `127.1`, `::1`, `localhost`, `::ffff:7f00:1` pointent tous vers la machine locale.

Une expression régulière pour repérer toutes ces variations est beaucoup plus complexe. Les acteurs malveillants peuvent facilement contourner une liste de refus en passant une représentation octale de l'encodage décimal de l'adresse IP.

### Imposer un schéma d'URL

En l'absence de cette mesure, un client pourrait envoyer des requêtes utilisant d'autres protocoles que ceux prévus. Pour remplacer notre `validUrlRegex`, nous utiliserons une liste `allowedSchemes`. Nous restreindrons notre application à ne traiter que les requêtes lorsque les protocoles sont soit `https:` soit `http`. Ne pas autoriser les requêtes avec les protocoles `file:` et `ftp:` protégera notre application exemple.

```js
const allowedSchemes = ['http:', 'https:'];
```

La fonction `isValidUrl` mise à jour ressemblera à ceci :

```js
function isValidUrl(url) {
  try {
    const parsedUrl = new URL(url);

    if (!whitelist.includes(parsedUrl.hostname)) {
      return false;
    }

    if (!allowedPorts.includes(parsedUrl.port)) {
      return false;
    }

    if (!allowedSchemes.includes(parsedUrl.protocol)) {
      return false;
    }

    return true;
  } catch (error) {
    return false;
  }
}
```

### Désactiver les redirections

Les redirections sont un mécanisme utilisé par les applications web pour rediriger le navigateur d'un utilisateur d'une URL à une autre. Si un serveur suit automatiquement les redirections, un attaquant pourrait exploiter ce comportement pour faire en sorte que le serveur accède involontairement à des ressources internes, entraînant une exposition de données ou des actions non autorisées.

Pour restreindre les redirections dans Axios, passez un objet de configuration Axios dans le deuxième paramètre :

```js
const response = await axios.get(url, { maxRedirects: 0 });
```

Pour en savoir plus sur la configuration Axios, consultez ce guide : [Axios | Request Config](https://axios-http.com/docs/req_config).

### Envoyer des données filtrées au client

Évitez d'envoyer des corps de réponse bruts directement de votre serveur au client. Assurez-vous que les réponses atteignant le client sont soigneusement sélectionnées et conformes aux formats attendus.

En mettant en œuvre cette pratique, vous protégez votre application contre les vulnérabilités de sécurité potentielles associées à l'exposition d'informations non filtrées ou sensibles. Validez, filtrez et formatez toujours les réponses pour qu'elles correspondent aux structures de données attendues par votre application.

## Conclusion

Et voilà : en mettant en œuvre quelques méthodologies et bonnes pratiques bien établies, vous pouvez détecter et atténuer efficacement les attaques SSRF dans vos applications et créer des API sécurisées en tant que développeur.

Trouvez les extraits de code complets ici — [GitHub Gist | HamdaanAliQuatil](https://gist.github.com/HamdaanAliQuatil/c7db6f3dd0666bd9396a7f4e6ebe6665).  
Vous pouvez me trouver sur X (anciennement Twitter) - [Hamdaan Ali Quatil](https://twitter.com/violinblackeye).