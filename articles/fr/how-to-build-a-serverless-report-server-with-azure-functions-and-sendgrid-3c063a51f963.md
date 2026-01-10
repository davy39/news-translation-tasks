---
title: Comment construire un serveur de rapports sans serveur avec Azure Functions
  et SendGrid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T17:40:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-report-server-with-azure-functions-and-sendgrid-3c063a51f963
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vQPIjM0f0bLivXDceow66w.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
seo_title: Comment construire un serveur de rapports sans serveur avec Azure Functions
  et SendGrid
seo_desc: 'By Burke Holland

  It’s 2018 and I just wrote a title that contains the words “Serverless server”.
  Life has no meaning.

  Despite that utterly contradictory headline, in this article we’re going to explore
  a pretty nifty way to exploit SendGrid’s templat...'
---

Par Burke Holland

Nous sommes en 2018 et je viens d'écrire un titre qui contient les mots « serveur sans serveur ». La vie n'a aucun sens.

Malgré ce titre totalement contradictoire, dans cet article, nous allons explorer une méthode assez ingénieuse pour exploiter la fonctionnalité de modèles de SendGrid en utilisant des déclencheurs de minuterie dans [Azure Functions](https://azure.microsoft.com/en-us/services/functions/?WT.mc_id=serverlessreport-medium-buhollan) afin d'envoyer des rapports tabulaires planifiés. Nous faisons cela parce que c'est ce que tout le monde veut dans sa boîte de réception. Un rapport. Avec des chiffres. Et de préférence quelques acronymes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vD5Qf5yUplqO3gDw8dcDlg.png)

#### Le rapport de stock SKU

Tout d'abord, définissons ce projet avec une application fictive qui semble suffisamment ennuyeuse pour justifier un rapport. J'ai juste ce qu'il faut. Un site où nous pouvons ajuster les niveaux de stock. Le mot « stock » ne demande qu'à être rapporté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xisRfTO8WdoNqLWLL5q4ZQ.png)

Cette application vous permet d'ajuster la quantité de stock (dernière colonne). Disons qu'un cadre quelque part a demandé que nous lui envoyions un rapport chaque nuit contenant une liste de chaque SKU modifié au cours des dernières 24 heures. Parce que bien sûr, ils demanderaient cela. En fait, je pourrais jurer avoir construit ce rapport dans la vraie vie dans un ancien emploi. Ou il y a un bug dans la matrice. Dans les deux cas, nous le faisons.

Voici ce que nous allons construire...

![Image](https://cdn-media-1.freecodecamp.org/images/1*DjphgVS92Dtc_5r4_id9Zg.png)

Normalement, la façon dont vous construiriez cela serait avec une sorte de serveur de rapports. Quelque chose comme SQL Server Reporting Services ou Business Objects ou tout autre serveur de rapports qui existe. Honnêtement, je ne veux pas le savoir. Mais si vous n'avez pas de serveur de rapports, cela devient assez fastidieux.

Passons en revue ce que vous devez faire pour que cela se produise...

1. Exécuter un travail sur une sorte de minuterie (tâche cron)
2. Interroger une base de données
3. Itérer sur les enregistrements et les formater pour la sortie à l'écran
4. Envoyer ledit rapport par e-mail
5. Mettre à jour votre CV et contacter des recruteurs

C'est le genre de chose que personne ne veut faire. Mais **je pense** que ce projet peut être très amusant, et nous pouvons utiliser une technologie intéressante pour le réaliser. En commençant par Serverless.

#### Fonctions de minuterie sans serveur

Serverless est un cas d'utilisation vraiment bon pour des requêtes ponctuelles comme celle-ci. Dans ce cas, nous pouvons utiliser Azure Functions pour créer une fonction de déclencheur de minuterie.

Pour cela, je vais utiliser l'extension Azure Functions pour VS Code. En fait, je vais l'utiliser pour tout. Pourquoi ? Parce que je ne vous connais pas, mais je sais qu'il est très probable que vous utilisiez VS Code. VS Code est génial parce que c'est comme un film que tous les développeurs peuvent universellement s'accorder à dire qu'il est complètement génial. Un peu l'opposé de « Children of Men ». Ce film était terrible et vous le savez.

Assurez-vous d'installer l'extension Azure Functions.

[**Azure Functions - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions&WT.mc_id=serverlessreport-medium-buhollan)
[_Extension pour Visual Studio Code - Une extension Azure Functions pour Visual Studio Code._marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions&WT.mc_id=serverlessreport-medium-buhollan)

Maintenant, créez une nouvelle application de fonction depuis VS Code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W1QGqj0bSh4X_CJk0JQukQ.gif)

Ensuite, créez une nouvelle fonction de déclencheur de minuterie. Les fonctions de déclencheur de minuterie sont planifiées à l'aide d'expressions Cron standard. Vous n'avez probablement jamais vu cela avant parce que je n'en avais jamais vu jusqu'il y a quelques mois. Et je suis dans cette industrie depuis LONGTEMPS. Je suis vieux, père William.

Les expressions Cron ont l'air un peu effrayantes parce qu'elles contiennent des astérisques. Dans le cas ci-dessous, je dis que lorsque les minutes sont à 0 et les secondes à 0 et les heures sont divisibles par 24, déclenchez la fonction. Ce serait minuit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l7L3hD2vVF_imKfrwODdhg.gif)

Maintenant, nous pouvons l'exécuter localement (F5). Nous verrons dans le terminal intégré le calendrier selon lequel notre fonction sera appelée ; les 5 prochaines occurrences.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4w9tkPYAfylKylDNxmWwKA.png)

Cela fait du bien, mon ami.

D'accord, maintenant nous devons obtenir des données. Je ne vais pas vous entraîner dans les spécificités de ma requête SQL Server à partir de cette fonction parce que ce n'est pas le sujet de cet article, mais voici le code quand même.

```js
const { Connection, Request } = require('tedious');

const options = {
  weekday: 'long',
  year: 'numeric',
  month: 'long',
  day: 'numeric'
};

const config = {
  userName: process.env.SQL_USERNAME,
  password: process.env.SQL_PASSWORD,
  server: process.env.SQL_SERVER,
  options: {
    encrypt: true,
    database: process.env.SQL_DATABASE
  }
};

module.exports = function(context, myTimer) {
  getChangedSkus()
    .then(data => {
      if (data.length > 0) {
        sendEmail(context, data);
      } else {
        context.done();
      }
    })
    .catch(err => {
      context.log(`ERROR: ${err}`);
    });
};

/**
 * Exécute une requête sur la base de données pour les SKU modifiés au cours des dernières 24 heures
 * @returns {Promise} L'objet Promise contient le résultat de la requête
 */
function getChangedSkus() {
  return new Promise((resolve, reject) => {
    const connection = new Connection(config);
    const query = `SELECT Sku, Quantity, CONVERT(varchar, Modified, 0) as Modified
                   FROM Inventory
                   WHERE Modified >= dateadd(day, -1, getdate())`;

    connection.on('connect', err => {
      if (err) reject(err);

      let request = new Request(query, err => {
        if (err) {
          reject(err);
        }
      });

      const results = [];
      request.on('row', columns => {
        let result = {};
        columns.forEach(column => {
          result[column.metadata.colName] = column.value;
        });

        results.push(result);
      });

      request.on('doneProc', (rowCount, more) => {
        resolve(results);
      });

      connection.execSql(request);
    });
  });
}
```

Je me connecte à la base de données, je fais une simple requête et... attendez une minute... n'ai-je pas dit que je **ne** m'attarderais pas sur les spécificités ? Vous m'aviez là pendant une minute, mais je suis sur votre jeu !

Cela récupère les données et nous les obtenons dans un objet JavaScript que nous pouvons passer en JSON. Si nous devions faire un `JSON.stringify` de cela, nous verrions l'ensemble de données que nous devons envoyer dans le rapport.

```js
[
  { "Sku": "1", "Quantity": 65, "Modified": "Nov  6 2018 10:14PM" },
  { "Sku": "10", "Quantity": 89, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "11", "Quantity": 39, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "12", "Quantity": 2, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "13", "Quantity": 75, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "14", "Quantity": 85, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "15", "Quantity": 58, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "16", "Quantity": 2, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "17", "Quantity": 48, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "18", "Quantity": 68, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "19", "Quantity": 67, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "2", "Quantity": 5, "Modified": "Nov  6 2018 11:18PM" },
  { "Sku": "20", "Quantity": 37, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "21", "Quantity": 54, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "22", "Quantity": 21, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "23", "Quantity": 46, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "24", "Quantity": 55, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "25", "Quantity": 21, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "26", "Quantity": 42, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "27", "Quantity": 65, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "28", "Quantity": 74, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "29", "Quantity": 33, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "3", "Quantity": 51, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "4", "Quantity": 96, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "5", "Quantity": 27, "Modified": "Nov  6 2018 11:18PM" },
  { "Sku": "6", "Quantity": 13, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "7", "Quantity": 54, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "8", "Quantity": 89, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "9", "Quantity": 56, "Modified": "Nov  2 2018  8:18PM" }
]
```

D'accord ! Nous avons les données, maintenant nous devons les rendre jolies et les envoyer par e-mail à quelqu'un que nous n'aimons pas. Comment allons-nous faire cela ? Avec SendGrid !

#### Configuration de SendGrid

SendGrid est un service ingénieux avec un tableau de bord vraiment agréable. Vous allez l'aimer. Ou non. Dans les deux cas, vous devez l'utiliser pour passer à travers cet article de blog.

Vous pouvez créer un compte gratuit si vous n'en avez pas déjà un. Cela suffit amplement pour ce que nous faisons aujourd'hui.

Une fois que vous avez créé un rapport, SendGrid va vous déposer dans votre « tableau de bord ». À partir de ce tableau de bord, vous devez créer une nouvelle application API et obtenir la clé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4YEtLhScWTudhZZT0-O8lA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CyjzWnmxyTsrX9qr1z5rMw.png)

Assurez-vous de copier votre clé API lorsqu'elle vous est donnée. Vous ne pouvez plus jamais y revenir et vous devrez tout recommencer. Admettons-le : c'était un peu ennuyeux la première fois.

Copiez cette clé dans votre projet Azure Functions. Mettez-la dans le fichier `local.settings.json` afin de pouvoir y accéder en tant que variable d'environnement Node.js plus tard.

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "DefaultEndpointsProtocol=https;AccountName=reporttimerstorage;AccountKey=OJVYCHI0GhtIm5XZdsDzGZFraJD/v/rfPwMSu4B72Kf5/O7oCrOQKNAFkQ==",
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "SENDGRID_API_KEY": "SG.rlpDOy3EQNOTChnzpa1COPYg.G4MYlEYhwHk0RyvuGcY_xKEYbhQoFTtPB9A9-5ZaYQ"
  }
}
```

Maintenant, nous allons créer un modèle dans SendGrid. C'est ce que nous allons utiliser pour concevoir notre rapport. SendGrid a quelque chose appelé « Modèles transactionnels ». Je ne sais pas pourquoi ils sont appelés ainsi, mais nous allons en avoir besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s53lLNCrkJBZatWFVff0pA.png)

Une fois que vous en avez créé un nouveau, vous devez créer une nouvelle « version ». J'ai eu un mal fou à comprendre cela. Mais après tout, mon cerveau est un peu du côté petit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SteEZljYYaKdqArZ4PzWlQ.png)

Choisissez de concevoir votre modèle avec l'éditeur de code. Vous n'avez pas besoin de l'éditeur de conception !

![Image](https://cdn-media-1.freecodecamp.org/images/1*wyh-9yjmGsJYGg5gu3Vkvw.png)

SendGrid prend en charge handlebars, qui est une syntaxe de modèle si facile que même moi je peux le faire. Dans l'éditeur de code, vous pouvez coller les données JSON dans l'onglet « Test Data »...

![Image](https://cdn-media-1.freecodecamp.org/images/1*KOj15MbsQnxKsdLsDYkoPQ.png)

Maintenant, itérez sur les données en utilisant leur nom de clé à partir du JSON...

![Image](https://cdn-media-1.freecodecamp.org/images/1*oAx66f58qZbtieLt0wghFA.png)

C'est BEAU ! Je pleure. Envoyez-le.

D'accord. Bien. Nous allons le rendre un peu plus agréable pour les vieux yeux. Voici un style que j'ai honteusement volé au magnifique [framework CSS Bulma](https://bulma.io/).

```html
<style>
  table {
    border-collapse: collapse;
    border-spacing: 0;
    background-color: white;
    color: #363636;
  }
  .table td,
  .table th {
    border: 1px solid #dbdbdb;
    border-width: 0 0 1px;
    padding: 0.5em 0.75em;
    vertical-align: top;
  }
  .table th {
    color: #363636;
    text-align: left;
  }
  .table thead td,
  .table thead th {
    border-width: 0 0 2px;
    color: #363636;
  }
  .table tbody tr:last-child td,
  .table tbody tr:last-child th {
    border-bottom-width: 0;
  }
  .table.is-bordered td,
  .table.is-bordered th {
    border-width: 1px;
  }
  .table.is-bordered tr:last-child td,
  .table.is-bordered tr:last-child th {
    border-bottom-width: 1px;
  }
  .table.is-fullwidth {
    width: 100%;
  }
  .container {
    margin: 0 auto;
    position: relative;
    max-width: 960px;
    padding-top: 20px;
    font-family: helvetica, sans-serif;
  }
</style>

<div class="container">
  <h1>SKUs modifiés</h1>
  <p>Les SKUs suivants ont été modifiés au cours des dernières 24 heures</p>

  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Sku</th>
        <th>Quantité</th>
        <th>Dernière modification</th>
      </tr>
    </thead>
    <tbody>
      {{#each Skus}}
      <tr>
        <td>{{Sku}}</td>
        <td>{{Quantity}}</td>
        <td>{{Modified}}</td>
      </tr>
      {{/each}}
    </tbody>
  </table>
</div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*TML-eMV1jv6d5NQppwtV5g.png)

À ce stade, il est acceptable que vous soyez audiblement impressionné.

Maintenant, vous avez peut-être remarqué que le sujet de l'e-mail est manquant. Comment allons-nous le remplir ? Eh bien, après une autre période embarrassante d'échec suivie d'introspection, j'ai compris qu'il se cache derrière l'icône « Paramètres » à gauche. Vous devez simplement passer une valeur dans votre JSON pour « Subject ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*siB4hsbwPrTkydVpVT66Fg.png)

Maintenant, nous devons obtenir l'ID du modèle et l'ajouter à notre projet Azure Functions. Enregistrez ce modèle et sélectionnez l'ID à partir de l'écran principal du modèle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S6zR6HQbhBWc1pgwpA9gnw.png)

Déposez-le dans le fichier `local.settings.json` juste en dessous de votre clé API SendGrid.

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "DefaultEndpointsProtocol=https;AccountName=reporttimerstorage;AccountKey=OJVYCHI0GhtIm5XZdsDzGZFraJD/v/rfPwMSu4B72Kf5/O7oCrOQKNAFkQ==",
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "SENDGRID_API_KEY": "SG.rlpDOy3EQNOTChnzpa1COPYg.G4MYlEYhwHk0RyvuGcY_xKEYbhQoFTtPB9A9-5ZaYQ"
    "SENDGRID_TEMPLATE_ID": "d-3e33c1453cf7457fb06e6d30519bd422"
  }
}
```

Maintenant, nous sommes prêts à passer nos données de notre fonction Azure à SendGrid et à envoyer ce travail incroyable d'art commercial.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3RlCKtdQS1oXYBc0.jpg)

#### Liaisons SendGrid pour Azure Functions

Azure Functions fournit une liaison pour SendGrid. Si vous créez une fonction via le portail Azure, elle créera cette liaison pour vous lorsque vous sélectionnerez le modèle « SendGrid ». Si vous le faites localement comme moi, vous devez l'ajouter vous-même.

Tout d'abord, vous devez ouvrir le fichier `function.json` pour la fonction `CreateReport` et ajouter la liaison SendGrid.

```
{
   "type": "sendGrid",
   "name": "message",
   "apiKey": "SENDGRID_API_KEY",
   "to": "youremail@company.com",
   "from": "hahabusiness@businesstime.com",
   "direction": "out"
}
```

La liaison SendGrid vient sous forme d'extension pour Azure Functions. Exécutez la commande suivante dans le terminal pour l'installer.

```
Microsoft.Azure.WebJobs.Extensions.SendGrid -Version 3.0.0
```

Lorsque vous exécutez cette commande, VS Code vous demandera de restaurer certaines dépendances. Vous pouvez cliquer sur restaurer. Rien de mal ne se passera... OU PAS ?!

Une autre chose que vous devez faire est de modifier votre fichier `extensions.csproj` pour référencer la dernière bibliothèque SendGrid. Cela est nécessaire pour utiliser des modèles dynamiques.

```
<PackageReference Include="Sendgrid" Version="9.10.0" />
```

Lorsque vous ajoutez cela, VS Code vous demandera de restaurer à nouveau et oui, vous devez absolument le faire cette fois-ci. VS Code doit construire ces binaires et la restauration fait cela.

D'accord ! Maintenant, nous sommes prêts à envoyer un e-mail via notre modèle SendGrid. Voici le code pour le faire. C'est d'une simplicité déprimante. Je sais qu'après tout cela, vous espériez assez de code pour étouffer un chat (quoi ? vous n'avez jamais entendu cette métaphore auparavant ?), mais c'est tout ce qu'il faut.

```js
function sendEmail(context, data) {
  context.done(null, {
    message: {
      /* vous pouvez remplacer les paramètres to/from de function.json ici si vous le souhaitez
        to: 'someone@someplace.com',
        from: 'someone@anotherplace.com'
        */
      personalizations: [
        {
          dynamic_template_data: {
            Subject: `Rapport SKU Tailwind pour ${new Date().toLocaleDateString(
              'en-US',
              options
            )}`,
            Skus: data
          }
        }
      ],
      template_id: process.env.SENDGRID_TEMPLATE_ID
    }
  });
}
```

Les éléments à noter sont que je passe un Subject dans le JSON. Ainsi que le fait que vous pouvez remplacer les adresses to/from spécifiées dans le fichier `function.json` ici.

Maintenant, vous pouvez exécuter votre fonction et attendre 24 heures pour la tester !

Non, mais sérieusement — comment tester manuellement un déclencheur de minuterie sans modifier constamment le Cron Job ?

Je vais vous montrer comment je le fais et ensuite vous pourrez trouver une meilleure façon.

#### Tester les déclencheurs de minuterie avec des déclencheurs HTTP

Je crée un déclencheur HTTP dans le même projet et je l'appelle « RunCreateReport ». Dans cette fonction, j'importe et j'appelle simplement la fonction de minuterie.

```js
const index = require('../CreateReport/index');

module.exports = function(context, req) {
  // Ceci est une fonction de test qui exécute manuellement la fonction de minuterie CreateReport
  index(context);
};
```

Le seul inconvénient de cela est que vous devez répéter vos paramètres de liaison SendGrid de `function.json` dans « CreateReport » dans le `function.json` de « RunCreateReport ». Mais à part cela, cela fonctionne très bien. Maintenant, vous pouvez exécuter cette chose, lancer un navigateur et accéder à l'URL qui appellera la fonction de minuterie immédiatement. Vous pouvez tester sans avoir à toucher cette vieille expression Cron.

#### HAHA business

Maintenant, allez vérifier votre e-mail et baignez-vous dans la gloire du rapport. Notez que vous n'avez pas besoin de posséder une adresse e-mail pour envoyer depuis SendGrid. Vous pouvez littéralement envoyer depuis n'importe quelle adresse. Sérieusement. Allez-y et essayez. PENSEZ JUSTE À CE QUE VOUS POUVEZ FAIRE AVEC CE POUVOIR.

Voici à quoi ressemble ma boîte de réception. Attention, cela va dans les spams. Probablement parce que je ne possède pas l'adresse e-mail de l'expéditeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BOXOst-_FtJ-RHaHO11jyA.png)

QUOI ? Il y a une « Conférence sur la résilience des entreprises » ? Oh mon Dieu, tellement d'affaires. Je parie que ces gens reçoivent BEAUCOUP de rapports.

Vous pouvez obtenir ce projet depuis GitHub.

[**burkeholland/serverless-sendgrid-report**](https://github.com/burkeholland/serverless-sendgrid-report)
[_Contribuez au développement de burkeholland/serverless-sendgrid-report en créant un compte sur GitHub._github.com](https://github.com/burkeholland/serverless-sendgrid-report)

Voici quelques autres ressources Azure Functions pour vous occuper.

* [Déployer sur Azure en utilisant Azure Functions](https://code.visualstudio.com/tutorials/functions-extension/getting-started?WT.mc_id=serverlessreport-medium-buhollan)
* [Guide du développeur JavaScript pour Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-node?WT.mc_id=serverlessreport-medium-buhollan)
* [Migration d'une API Mongo DB vers Azure Functions](https://www.youtube.com/watch?v=89WXgaY-NqY)