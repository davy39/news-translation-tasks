---
title: Comment corriger les erreurs Cross-Origin — L'erreur CORS expliquée
subtitle: ''
author: Sumit Saha
co_authors: []
series: null
date: '2025-10-01T13:57:58.744Z'
originalURL: https://freecodecamp.org/news/how-to-fix-cross-origin-errors
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759324719020/8c59e405-107b-4e45-acab-c61cbf353d0b.png
tags:
- name: Web Development
  slug: web-development
- name: CORS
  slug: cors
seo_title: Comment corriger les erreurs Cross-Origin — L'erreur CORS expliquée
seo_desc: 'In this article, you’ll learn about an important concept: Cross-Origin
  Resource Sharing (CORS) policy. As a developer, you might encounter a situation
  where a client request to the server fails, and the browser displays a red error
  like "CORS policy ...'
---

Dans cet article, vous découvrirez un concept important : la politique de partage de ressources entre origines multiples (CORS). En tant que développeur, vous pouvez être confronté à une situation où une requête client vers le serveur échoue, et le navigateur affiche une erreur rouge telle que \"CORS policy failed\". Même lorsque la requête est correctement implémentée, cette erreur peut toujours survenir.

Certains débutants effectuent des recherches en ligne ou copient des correctifs temporaires, ce qui peut résoudre le problème sans apporter de réelle compréhension. Ici, nous allons décomposer le CORS de manière claire afin que vous puissiez comprendre pourquoi cela se produit et comment le corriger.

![Erreur CORS](https://cdn.hashnode.com/res/hashnode/image/upload/v1758399944364/ea17ff8c-3791-45df-bcc6-276eeeab0af1.png align=\"center\")

## Voici ce que nous allons aborder

* [Prérequis](#heading-prerequis)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Démonstration : Interaction Client-Serveur](#heading-demonstration-interaction-client-serveur)
    
* [Qu'est-ce qu'une origine ?](#heading-quest-ce-quune-origine)
    
* [Que signifie la politique CORS pour le navigateur ?](#heading-que-signifie-la-politique-cors-pour-le-navigateur)
    
* [Comment corriger les erreurs de politique CORS](#heading-comment-corriger-les-erreurs-de-politique-cors)
    
* [Notes supplémentaires sur le CORS](#heading-notes-supplementaires-sur-le-cors)
    
* [Résumé](#heading-resume)
    
* [Mot de la fin](#heading-mot-de-la-fin)
    

## Prérequis

Pour suivre ce guide et en tirer le meilleur parti, vous devriez avoir :

1. Des connaissances de base en JavaScript — Vous devez être familier avec la syntaxe JavaScript, les fonctions et l'API fetch pour effectuer des requêtes HTTP côté client.
    
2. Node.js et `npm` installés — Vous utiliserez Node.js pour la configuration côté serveur et `npm` pour gérer les packages. Vous pouvez télécharger Node.js [ici](https://nodejs.org).
    
3. Un éditeur de code (comme VS Code) — Vous aurez besoin d'un éditeur de code comme [VS Code](https://code.visualstudio.com/) pour écrire et exécuter vos fichiers client et serveur.
    
4. Des connaissances de base sur les méthodes HTTP — La connaissance des requêtes GET, POST, PUT, DELETE vous aidera à comprendre comment le navigateur et le serveur communiquent.
    
5. Un navigateur avec les Outils de développement — Chrome, Firefox ou Edge avec les Developer Tools.
    
6. Facultatif mais utile : l'extension VS Code Live Server — Elle permet d'exécuter vos fichiers HTML localement pour tester les requêtes client-serveur.
    

J'ai également créé une vidéo pour accompagner cet article. Si vous préférez apprendre par la vidéo autant que par le texte, vous pouvez la consulter ici :

%[https://www.youtube.com/watch?v=rYVGbOMV8Ng] 

## Configuration du projet

Avant d'explorer le CORS, configurons un client et un serveur de base.

### Initialiser le serveur

Tout d'abord, créez un dossier de projet nommé `cors-tutorial`, et à l'intérieur de ce dossier, créez un autre dossier appelé `server`. Ensuite, naviguez dans le dossier `server` et initialisez un projet Node. Exécutez les commandes ci-dessous une par une :

```powershell
mkdir cors-tutorial
cd cors-tutorial
mkdir server
cd server
npm init -y
```

### Installer les packages requis

Pour la configuration de base du serveur, vous utiliserez un Framework Node.js populaire, [Express.js](https://expressjs.com/). Installez-le avec la commande suivante :

```powershell
npm install express
```

### Créer le fichier serveur

Créez un fichier `server/app.js`. À l'intérieur du fichier, importez le package Express installé et initialisez l'application à l'aide de la fonction `express()`. Ensuite, créez une route `/data` qui renvoie un objet JSON simple.

```javascript
// server/app.js
const express = require("express");
const app = express();

app.get("/data", (req, res) => {
    res.json({
        name: "Bangladesh",
        description: "Land of emotions",
    });
});

app.listen(3000, () => {
    console.log("Server is running on http://localhost:3000");
});
```

### Exécuter le serveur

Maintenant, démarrez le serveur avec la commande suivante :

```javascript
node app.js
```

### Configuration du client

Il est temps de configurer le client. Créez un fichier `index.html` et un fichier `script.js` à l'intérieur du dossier `cors-tutorial`.

```xml
<!-- index.html -->
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Qu'est-ce que le CORS</title>
  </head>
  <body>
    <div>
      <button onclick="fetchData()">Récupérer les données</button>
    </div>

    <script src="./script.js"></script>
  </body>
</html>
```

```javascript
// script.js
async function fetchData() {
  const response = await fetch("http://localhost:3000/data", {
    method: "GET",
  });

  const data = await response.json();
  console.log(data);
}
```

## Démonstration : Interaction Client-Serveur

### Côté Client

* `index.html` possède un seul bouton intitulé `Récupérer les données`.
    
* Le client s'exécute sur `127.0.0.1:5500` via VS Code Live Server.
    
* La console du navigateur est ouverte pour visualiser les logs.
    

### Côté Serveur

* Un serveur Express minimal se trouve dans le dossier `server`.
    
* `app.js` contient la route `/data` qui renvoie :
    
    ```json
    {
      "name": "Bangladesh",
      "description": "Land of emotions"
    }
    ```
    
* Le serveur s'exécute sur `localhost:3000`.
    

### Comment ça fonctionne

* Cliquer sur le bouton **Récupérer les données** appelle `fetchData()` depuis `script.js`.
    
* `fetchData()` envoie une requête GET au serveur et enregistre la réponse JSON.
    
* Visiter directement `localhost:3000/data` affiche également la sortie JSON.
    
* Comme les ports du client et du serveur diffèrent, vous pourriez voir un message d'erreur lié au CORS dans la console.
    

![Erreur CORS Access-Control-Allow-Origin](https://cdn.hashnode.com/res/hashnode/image/upload/v1758400085132/e5dbc478-b6c4-429a-b113-3e0b24db7f55.png align=\"center\")

### Notes

* Python, PHP ou d'autres langages backend peuvent être utilisés de manière similaire pour créer une API.
    
* Cette démonstration montre comment le client interagit avec le serveur avant de gérer les problèmes de CORS.
    

## Qu'est-ce qu'une origine ?

L'origine désigne la source d'où provient la requête. J'ai effectué la requête depuis `127.0.0.1:5500` et j'essaie d'accéder aux données sur `localhost:3000`. Les deux sont des URL, mais elles sont différentes, n'est-ce pas ? Quand nous parlons d'URL, nous entendons la partie domaine, pas le chemin complet. `localhost` et `127.0.0.1` semblent identiques, mais ils sont différents en ce qui concerne l'origine. Les ports sont également différents. Pour cette raison, l'URL ou l'origine est considérée comme différente.

Ainsi, la source et le serveur sont différents, et c'est pourquoi il est indiqué \"has been blocked by CORS policy\" et \"No 'Access-Control-Allow-Origin' header is present on the requested resource.\" Lorsqu'un débutant voit cela, il peut ne pas comprendre tout le processus : pourquoi cela arrive et comment cela arrive. Nous allons apprendre cela maintenant et comment le résoudre.

## Que signifie la politique CORS pour le navigateur ?

Imaginez que votre site Web soit `xyz.com` et que ce soit notre frontend. Et votre serveur est `www.abc.com`, un domaine différent. Ces deux sont des domaines différents. Nous attendons de `xyz.com` qu'il fasse une requête à `abc.com` et que `abc.com` envoie une réponse — c'est simple.

![Visualisation Requête - Réponse](https://cdn.hashnode.com/res/hashnode/image/upload/v1758400245846/8e04ca91-073a-4da5-a19b-355a9178be85.jpeg align=\"center\")

Le code que nous avons écrit devrait fonctionner, mais parfois ce n'est pas le cas, ce qui peut être déroutant. Pourquoi cela arrive-t-il ? La raison est simple : la politique CORS bloque la requête. La politique CORS est une politique du navigateur. Sa forme complète est Cross-Origin Resource Sharing (CORS).

![Cross-Origin Resource Sharing (CORS)](https://cdn.hashnode.com/res/hashnode/image/upload/v1758400326775/22ebc6fd-9479-4fe9-aad7-0a752dadef8c.jpeg align=\"center\")

En termes simples, si le domaine du demandeur est différent du domaine du destinataire, alors par défaut, le navigateur rejettera la requête. Bien qu'elle puisse atteindre le serveur, le navigateur refusera de livrer la réponse au client. C'est pourquoi nous observons ce comportement.

## Comment corriger les erreurs de politique CORS

Cette tâche doit être gérée côté serveur. Tout d'abord, ouvrez l'onglet Network du navigateur. Lorsque vous effectuez la requête, rechargez et effacez tout, puis cliquez sur `fetchData`. Notez les détails de la requête. Chaque requête comporte deux parties : les Request Headers (en-têtes de requête) et les Response Headers (en-têtes de réponse).

Les en-têtes de requête sont envoyés par le navigateur et incluent des métadonnées et des informations relatives au navigateur. Les en-têtes de réponse sont générés par le serveur et contiennent également des métadonnées, tandis que les en-têtes de requête sont créés par le client (le navigateur).

Si vous inspectez le côté réponse, l'erreur indique : \"No 'Access-Control-Allow-Origin' header is present on the requested resource\". Vous devez donc rechercher cet en-tête dans la réponse. Dans l'onglet Network, si vous vérifiez les en-têtes de réponse, vous verrez qu'il n'y a pas de `Access-Control-Allow-Origin`. Si la réponse contenait cet en-tête, le navigateur autoriserait l'accès. Vous devez donc ajouter l'en-tête approprié à la réponse.

![En-tête Access-Control-Allow-Header manquant](https://cdn.hashnode.com/res/hashnode/image/upload/v1758400366863/51da88e4-b44d-4d99-b50c-9dd0064b9236.png align=\"center\")

Alors, que devons-nous faire ? Si vous souhaitez corriger cela dans une configuration Node.js/Express, allez dans le fichier `app.js` du dossier `server`. Arrêtez le serveur et installez le package `cors` :

```powershell
npm install cors
```

Après avoir installé le package, redémarrez le serveur. Ensuite, importez le package et dites à l'application de l'utiliser. La fonction `cors()` peut accepter une option `origin`. Si nous définissons `origin` sur `localhost:5500`, qui est l'URL de notre client, le serveur n'autorisera que cette origine. Si vous souhaitez autoriser plusieurs origines, vous pouvez passer un tableau d'URL. Ici, je définis une seule URL car le client s'exécute sur le port 5500. Cela signifie que les requêtes provenant d'autres adresses ne seront pas autorisées.

Vous pouvez maintenant recharger, effacer la console et cliquer à nouveau sur `fetchData`, mais vous aurez toujours un problème. Pourquoi ? Parce que l'URL du client utilisait `127.0.0.1` au lieu de `localhost`. C'est une variation, et l'origine doit correspondre exactement. Vous pouvez donc la changer en `127.0.0.1:5500` dans la configuration du serveur.

Maintenant, vous pouvez recharger, effacer et cliquer sur `fetchData`. Tout devrait fonctionner comme prévu : il n'y a pas d'erreur, la réponse a été envoyée et les données ont été affichées dans la console.

Si vous inspectez les en-têtes de réponse réseau pour la requête de données, vous devriez voir `Access-Control-Allow-Origin: http://127.0.0.1:5500`. Cela signifie que le serveur a répondu avec l'en-tête CORS et a autorisé cette origine. Comme l'origine correspondait, la requête a réussi. Ce qu'il faut retenir : le serveur doit inclure un en-tête `Access-Control-Allow-Origin` spécifiant le domaine autorisé. Si vous souhaitez autoriser toutes les origines (pour une API publique), vous pouvez utiliser `*`. Dans Express, vous pouvez également simplement appeler `app.use(cors())` pour autoriser toutes les origines. Cela fera en sorte que le serveur accepte les requêtes de n'importe quelle origine.

```javascript
// server/app.js
const express = require("express");
const cors = require("cors");
const app = express();

// Activer le CORS pour l'origine du client
app.use(cors({ origin: "http://127.0.0.1:5500" }));

app.put("/data", (req, res) => {
    res.json({
        name: "Bangladesh",
        description: "Land of emotions",
    });
});

app.listen(3000, () => {
    console.log("Server is running on http://localhost:3000");
});
```

Cela garantit que le serveur autorise explicitement l'origine du client, résolvant ainsi les erreurs de politique CORS.

## Notes supplémentaires sur le CORS

Une chose de plus à noter. La requête que nous envoyions depuis le client était une requête GET. Pour GET, POST, DELETE, le processus est simple. Mais pour des méthodes comme PUT, qui modifient les données sur le serveur, le CORS se comporte légèrement différemment. Si vous modifiez le client pour envoyer une requête PUT et que le serveur définit une route `app.put`, vous remarquerez deux requêtes dans le panneau réseau. Le navigateur envoie d'abord une requête de pré-vérification (preflight). C'est la façon dont le navigateur vérifie s'il est autorisé à envoyer la requête réelle. Cette requête preflight est une requête `OPTIONS` envoyée automatiquement par le navigateur avant la requête PUT réelle.

```javascript
// server/app.js
const express = require("express");
const cors = require("cors");

const app = express();
app.use(
    cors({
        origin: "http://127.0.0.1:5500",
        methods: ["GET", "POST"],
    })
);

app.put("/data", (req, res) => {
    res.json({
        name: "Bangladesh",
        description: "Land of emotions",
    });
});

app.listen(3000);
```

```javascript
// script.js
async function fetchData() {
    const response = await fetch("http://localhost:3000/data", {
        method: "PUT",
    });

    const data = await response.json();

    console.log(data);
}
```

Lorsque vous regardez la requête preflight dans l'onglet Network, vous verrez des en-têtes de réponse qui incluent `Access-Control-Allow-Methods` et d'autres en-têtes CORS. Le package `cors` par défaut autorise toutes les méthodes comme `GET`, `POST`, `PUT`, `HEAD`, `PATCH`, etc. Si vous souhaitez une sécurité plus stricte, vous pouvez spécifier les méthodes autorisées dans la configuration CORS. Par exemple, définissez l'option `methods` sur `['GET', 'POST']` pour autoriser uniquement GET et POST et refuser PUT et DELETE. Même si l'origine correspond, si la méthode n'est pas autorisée, le preflight échouera et la requête réelle sera bloquée.

![Exemple de requête Preflight](https://cdn.hashnode.com/res/hashnode/image/upload/v1758400423187/0186a5b6-b3fb-4ead-8ee8-aac847d28852.png align=\"center\")

Si vous effectuez la même requête avec des méthodes non autorisées, elle échouera. La console affichera le message d'erreur CORS exact. Maintenant que vous comprenez le flux, vous pourrez expliquer lors d'un entretien :  
\"L'accès à fetch à [URL-1] depuis l'origine [URL-2] a été bloqué par la politique CORS : La méthode PUT n'est pas autorisée par Access-Control-Allow-Methods dans la réponse preflight.\" La vérification preflight a vu `Access-Control-Allow-Methods: GET, POST` et a donc bloqué la requête PUT.

Vous pouvez donc contrôler le comportement du CORS à l'aide de deux éléments principaux : `Access-Control-Allow-Origin` et `Access-Control-Allow-Methods`. Si vous les comprenez et les configurez sur le serveur, vous pouvez contrôler quelles origines et quelles méthodes sont autorisées. C'est finalement ce qu'est la politique CORS : une mesure de sécurité appliquée par le navigateur. Les navigateurs implémentent ce modèle standard afin que si le serveur n'envoie pas les en-têtes appropriés, le navigateur n'autorise pas le client à accéder à la réponse.

## Résumé

* Le CORS (Cross-Origin Resource Sharing) est un mécanisme de sécurité appliqué par le navigateur qui bloque les requêtes provenant d'origines différentes, sauf autorisation explicite du serveur.
    
* L'origine est déterminée par le protocole, le domaine et le port. Même de petites différences comme `localhost` par rapport à `127.0.0.1` ou des ports différents rendent l'origine différente.
    
* Les navigateurs bloquent les réponses si le serveur n'inclut pas l'en-tête `Access-Control-Allow-Origin` pour l'origine demanderesse.
    
* Le package Node.js `cors` peut aider à gérer facilement le CORS. L'utilisation de `app.use(cors({ origin: "`[`http://127.0.0.1:5500`](http://127.0.0.1:5500)`" }))` autorise uniquement l'origine client spécifiée.
    
* Pour les méthodes comme PUT, DELETE et PATCH, les navigateurs envoient d'abord une requête preflight `OPTIONS` pour vérifier si la méthode et l'origine sont autorisées.
    
* L'en-tête `Access-Control-Allow-Methods` définit les méthodes HTTP que le serveur autorise. Si une méthode est refusée, le preflight échoue et la requête est bloquée.
    
* Une configuration appropriée de `Access-Control-Allow-Origin` et `Access-Control-Allow-Methods` garantit une communication client-serveur sûre et fonctionnelle.
    
* Faites toujours correspondre l'origine du client exactement et n'autorisez que les méthodes nécessaires pour la sécurité. Les API publiques peuvent utiliser `*` pour autoriser toutes les origines.
    

## Mot de la fin

Vous pouvez trouver tout le code source de ce tutoriel dans [ce dépôt GitHub](https://github.com/logicbaselabs/cors-tutorial). S'il vous a aidé d'une manière ou d'une autre, n'hésitez pas à lui donner une étoile pour montrer votre soutien !

De plus, si vous avez trouvé les informations ici précieuses, n'hésitez pas à les partager avec d'autres personnes qui pourraient en bénéficier. J'apprécierais vraiment vos retours – mentionnez-moi sur X [@sumit\_analyzen](https://x.com/sumit_analyzen) ou sur Facebook [@sumit.analyzen](https://facebook.com/sumit.analyzen), [regardez mes tutoriels de programmation](https://youtube.com/@logicBaseLabs), ou [connectez-vous simplement avec moi sur LinkedIn](https://www.linkedin.com/in/sumitanalyzen/).