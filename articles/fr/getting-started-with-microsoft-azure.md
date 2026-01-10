---
title: Comment commencer avec Microsoft Azure - Applications de fonction, déclencheurs
  HTTP et files d'attente d'événements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-30T00:57:47.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-microsoft-azure
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca036740569d1a4ca4743.jpg
tags:
- name: Azure
  slug: azure
seo_title: Comment commencer avec Microsoft Azure - Applications de fonction, déclencheurs
  HTTP et files d'attente d'événements
seo_desc: "By Amber Wilkie\n\"Serverless\" architecture is all the rage in tech land\
  \ at the moment, including heavy usage at my new workplace. \nMicrosoft jumped into\
  \ this space with Azure a while back. Their portal, where all the services are grouped\
  \ and \"organize..."
---

Par Amber Wilkie

L'architecture "Serverless" est très en vogue dans le monde de la technologie en ce moment, y compris une utilisation intensive dans mon nouveau lieu de travail. 

Microsoft s'est lancé dans cet espace avec [Azure](https://azure.microsoft.com) il y a quelque temps. Leur portail, où tous les services sont regroupés et "organisés", offre tellement de services qu'il semble presque impossible d'être un expert. 

Je vais couvrir les __applications de fonction, les déclencheurs, les liaisons et les files d'attente d'événements__, suffisamment pour qu'un développeur web puisse commencer quelque chose de grand dans le cloud.

![Champs de tulipes près d'Amsterdam](https://www.freecodecamp.org/news/content/images/2019/09/spring-2019-16.jpg)

Il y a deux mois, je n'avais jamais travaillé avec aucune de ces technologies, mais j'adore la propreté, la séparation claire et l'asynchronicité de ces outils. Les services Azure ont quelques défauts (vitesse du portail, problèmes d'UI, et à mesure que vous montez en échelle, difficulté à comprendre ce qui ralentit le système), mais dans l'ensemble, la technologie est facile à utiliser et très puissante.

# Applications de fonction
La première chose que vous ferez pour commencer est de créer une Application de fonction. Dans le monde d'Azure, il s'agit d'un regroupement de fonctionnalités liées. Vous créerez des *fonctions* discrètes à l'intérieur de l'*Application de fonction*. Chaque Application de fonction a accès à un conteneur de stockage.

![Création d'une application de fonction dans le portail web d'Azure](https://www.freecodecamp.org/news/content/images/2019/09/create-function-app.png)

![Paramètres de l'application de fonction](https://www.freecodecamp.org/news/content/images/2019/09/function-app-creation-settings.png)

À partir du portail (après la configuration du compte et le paiement), vous cliquerez sur "Créer une ressource" en haut, puis sélectionnerez Application de fonction. Donnez un nom à votre application, choisissez un langage pour écrire votre code (j'ai choisi Node pour JavaScript), et gardez le reste des paramètres tels quels. 

Il faut une minute pour déployer une nouvelle Application de fonction - vous pouvez cliquer sur la notification en haut à droite pour suivre la progression et obtenir un lien facile lorsqu'elle est prête.

## Ajout de fonctionnalités
Une fois l'Application de fonction prête, cliquez sur le plus à côté de Fonctions. Sélectionnez "Dans l'éditeur du portail" et "Webhook / API". Nous allons faire la configuration la plus basique possible. Les déploiements CI/CD et autres sont hors du cadre de ce tutoriel, mais bien sûr, vous pouvez contrôler les versions de votre travail à l'aide d'outils git et déployer via un pipeline.

![editing-azure-function-in-portal](https://www.freecodecamp.org/news/content/images/2019/09/editing-azure-function-in-portal.png)

![Journaux de l'application de fonction Azure après le déclencheur HTTP](https://www.freecodecamp.org/news/content/images/2019/09/http-trigger-in-azure.png)

# Liaisons
Après avoir créé votre fonction, vous obtiendrez un `index.js` et un `function.json`. Vous pouvez accéder à ces fichiers à droite de votre éditeur dans le portail sous "Voir les fichiers". 

Commençons par examiner `function.json` - c'est le fichier de configuration de votre fonction. Voici le fichier tel que le portail le générera :
```json
{
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "get",
        "post"
      ]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    }
  ],
  "disabled": false
}
```
Les [Liaisons](https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings) sont un moyen pratique d'Azure pour se connecter à divers services et ressources sans avoir besoin de faire beaucoup de configuration.

### httpTrigger
* Changez `authLevel` en `"anonymous"` et nous n'aurons pas besoin d'une clé pour appeler notre fonction.
* Le `type` est `httpTrigger` - cela signifie que nous allons générer un point de terminaison que nous pouvons utiliser pour appeler cette fonction (plus d'informations ci-dessous). 
* La `direction` peut être soit `in` soit `out` - indiquant une entrée ou une sortie vers/de notre fonction.
* Le déclencheur appellera la fonction avec les paramètres fournis. Nous pouvons appeler la liaison comme nous voulons, mais la convention dit que nous nommons l'entrée `req` pour requête et la sortie `res` pour réponse. 
* Les `Methods` sont les moyens par lesquels nous pouvons appeler cette fonction. Je vais supprimer `post`, car nous n'en aurons pas besoin.

La liaison suivante est également de type `http`, direction `out`, car c'est ainsi que nous enverrons une réponse. Si vous souhaitez désactiver la fonction, vous pouvez le faire ici dans le `function.json` ou dans l'UI du portail.

## Utilisation des liaisons dans le code de la fonction
Nous pouvons utiliser le code d'exemple fourni par Azure pour montrer comment fonctionnent les liaisons. J'ai simplifié le code d'Azure, mais vous devriez avoir quelque chose de très similaire dans votre `index.js` si vous suivez ce tutoriel :
```javascript
module.exports = async function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    if (req.query.name) {
        context.res = {
            // status: 200, /* Par défaut 200 */
            body: "Hello " + req.query.name
        };
    }
    else {
        context.res = {
            status: 400,
            body: "Veuillez passer un nom dans la chaîne de requête ou dans le corps de la requête"
        };
    }
};
```

![Envoi d'une requête via Postman à notre application de fonction Azure](https://www.freecodecamp.org/news/content/images/2019/09/postman-request-to-http-trigger.png)

Ici, vous pouvez voir que nous avons un webhook simple. Nous pouvons voir son fonctionnement rapidement en cliquant sur "Obtenir l'URL de la fonction" et en envoyant une requête avec cURL ou Postman. Alors, que se passe-t-il ?

![Journaux de l'application de fonction Azure recevant un déclencheur HTTP](https://www.freecodecamp.org/news/content/images/2019/09/trigger-demo-logs-executing.png)

Grâce à la magie d'Azure, notre fonction a été appelée avec `context` et la `req` que nous avons envoyée. Le `context` nous permet d'accéder aux liaisons que nous avons vues dans `function.json` et la `req` devient l'entrée de notre fonction. 

Plus de magie d'Azure gère la réponse. Nous définissons simplement le `status` selon nos besoins, et le `body` de manière appropriée. Azure gère le reste. (Notez que si vous envoyez des objets de réponse JSON ou autres non chaînés, vous devrez définir les en-têtes.)

Nous pouvons voir tout cela fonctionner dans les journaux. Vous les trouverez tout en bas de la page sous le code `index.js`. Notez que `console.log` ne vous aidera pas ici - vous devrez utiliser `context.log`.

Et c'est tout ! Nous avons un webhook qui s'exécute dans le "cloud".

## Variables d'environnement
Nous ne pourrons probablement pas aller loin sans avoir quelques secrets que nous utilisons pour nous connecter aux bases de données, aux API externes et à d'autres services. Vous pouvez garder ces variables sous "Configuration" lorsque vous cliquez sur le nom de votre Application de fonction (par opposition à Fonctions). Azure placera automatiquement un ensemble de variables pour gérer le stockage de votre Application de fonction et Application Insights (surveillance).

## Autres liaisons
Il existe des dizaines de liaisons qui peuvent être utilisées. Azure peut se connecter à plusieurs types de bases de données différents, et vous pouvez créer un déclencheur pour un nouveau document créé. De même, cette méthode pourrait recevoir une charge utile qui créerait un enregistrement avec une liaison de sortie. 

Une autre liaison intéressante est un `event`, que je vais couvrir ensuite.

# Files d'attente d'événements
Une requête et une réponse, c'est bien, mais que faire si nous voulons créer un événement asynchrone à partir d'une liaison HTTP ? 

Supposons que nous créons un utilisateur. Après la création de cet utilisateur, nous voulons envoyer un e-mail pour l'accueillir dans notre service. 

Mais si quelque chose ne va pas avec notre code d'envoi d'e-mail, nous ne voudrions jamais que cela empêche la création d'un utilisateur ou la réponse au client. Nous pouvons créer une messagerie asynchrone via une [file d'attente d'événements](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue).

Je ne vais pas entrer trop dans les détails sur le fonctionnement des files d'attente, mais l'idée est assez simple : une méthode place des messages dans une file, et une autre les retire et fait quelque chose avec eux (dernier entré, premier sorti). Lorsque la file est vide, tout ce qui l'écoute est silencieux. 

Azure dispose de fonctionnalités pour différents types de files d'attente, y compris le Service Bus plus complexe.

## Création de la file d'attente
La première chose que nous allons faire est de créer une file d'attente que nos fonctions peuvent utiliser pour envoyer et lire des messages. Si vous cliquez sur "Accueil" dans le fil d'Ariane, vous devriez voir le nom de votre Application de fonction dans les ressources récentes. 

Le lien ici est en fait vers le "Groupe de ressources" - une collection de tous les éléments que vous avez créés avec l'Application de fonction. Cliquez dessus, puis sélectionnez votre stockage (il ressemble à une table de base de données). 

Maintenant, trouvez l'onglet Files d'attente, cliquez sur "+File d'attente", puis créez une file d'attente pour votre application de fonction. Notez que vous pouvez avoir autant de files d'attente que vous le souhaitez. Vous pouvez également créer des éléments dans votre file d'attente manuellement pour tester vos fonctions indépendamment.

![Groupe de ressources de l'application de fonction Azure](https://www.freecodecamp.org/news/content/images/2019/09/function-app-resource-group.png)

## Liaisons de file d'attente

Ajoutez une nouvelle fonction (cliquez sur l'icône `+`) et sélectionnez "Déclencheur de stockage de file d'attente Azure". Cela vous invitera à installer une extension Event Hub, puis donnez un nom à votre fonction - vous pouvez ignorer les autres paramètres pour l'instant. Voici le code `function.json` pour nos nouvelles liaisons :
```json
{
  "bindings": [
    {
      "name": "myQueueItem",
      "type": "queueTrigger",
      "direction": "in",
      "queueName": "js-queue-items",
      "connection": "AzureWebJobsStorage"
    }
  ],
  "disabled": false
}
```
Nous utiliserons le stockage que nous avons créé pour cette application de fonction pour maintenir une file d'attente d'événements. Le `index.js` prend l'élément de la file et l'exécute. Nous n'avons pas besoin de faire grand-chose avec notre fonction, donc nous pouvons simplement garder le code de démonstration d'Azure :
```javascript
module.exports = async function (context, myQueueItem) {
    context.log('JavaScript queue trigger function processed work item', myQueueItem);
};
```

![Journaux de l'application de fonction Azure après le déclencheur de file d'attente](https://www.freecodecamp.org/news/content/images/2019/09/queue-trigger-executing.png)

## Ajout d'un élément à la file d'attente
Votre fonction de déclencheur de file d'attente est en cours d'exécution, mais elle ne fera rien tant que nous n'aurons pas ajouté un élément à notre file d'attente. Nous pouvons le faire en ajustant notre première fonction pour placer un élément dans la file lorsque le webhook est appelé.
```json
{ bindings: [...],
    {
      "name": "myQueueItem",
      "type": "queue",
      "direction": "out",
      "queueName": "js-queue-items",
      "connection": "AzureWebJobsStorage"
    }
}
```
Maintenant, nous pouvons mettre à jour notre code pour ajouter un élément à la file d'attente :
```javascript
[...]
    if (req.query.name) {
        context.bindings.myQueueItem = {
            name: req.query.name,
            ts: new Date()
        }
[...]
```
Si vous ouvrez vos fonctions dans des fenêtres séparées, vous pouvez voir tout cela se produire dans les journaux de chaque fonction. Envoyez votre requête, regardez-la être consommée dans le déclencheur HTTP, puis le déclencheur de file d'attente récupérera le message placé par la première fonction. Cool, n'est-ce pas ?

C'est une technologie puissante pour créer des travaux asynchrones de manière à empêcher vos fonctions de s'interférer les unes avec les autres. Dans un modèle "monolithique", si une fonction se comporte mal, elle peut empêcher les autres de s'exécuter. Dans ce modèle, si quelque chose ne va pas avec le déclencheur de file d'attente, cela n'empêchera pas le serveur de répondre de manière appropriée. Naturellement, cela ajoute une couche de complexité et de considération qui n'existe pas dans un monolithe - il y a toujours des compromis.

Mais si nous revenons à notre cas d'utilisation théorique où nous créons un nouvel utilisateur avec un déclencheur HTTP, imaginez avoir 10 files d'attente pour faire diverses choses. Notre déclencheur HTTP pourrait créer un document dans la base de données et retourner un succès dans la requête. 

Le même travail pourrait ajouter à une file d'attente pour envoyer un e-mail, déclencher un SMS de coupon à envoyer dans une heure, envoyer un message Slack à une équipe marketing, ou toute autre chose parmi un million de choses qui pourraient devoir se produire lorsqu'un nouvel utilisateur est créé. Si l'une d'entre elles échoue (Slack est en panne ?), les autres continuent joyeusement leur chemin.

Cet article n'a fait qu'effleurer la surface de ce qui est disponible. J'ai hâte d'explorer davantage ce qu'Azure peut faire. Faites-moi savoir si vous avez des conseils sur ce qu'il faut construire ensuite !


_Vous pouvez lire plus de mes articles sur mon blog à l'adresse [wilkie.tech](https://wilkie.tech)._