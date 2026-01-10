---
title: Le guide complet pour construire une API avec TypeScript et AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-27T15:57:26.000Z'
originalURL: https://freecodecamp.org/news/build-an-api-with-typescript-and-aws
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9900740569d1a4ca1d4b.jpg
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: serverless
  slug: serverless
- name: TypeScript
  slug: typescript
seo_title: Le guide complet pour construire une API avec TypeScript et AWS
seo_desc: "By Sam Williams\nIn this article we'll be looking at how we can quickly\
  \ and easily build an API with TypeScript and Serverless. \nWe'll then learn how\
  \ to use the aws-sdk to access other AWS services and create an automatic translation\
  \ API.\nIf you prefe..."
---

Par Sam Williams

Dans cet article, nous allons voir comment construire rapidement et facilement une API avec TypeScript et Serverless. 

Nous apprendrons ensuite comment utiliser le _aws-sdk_ pour accéder à d'autres services AWS et créer une API de traduction automatique.

Si vous préférez regarder et apprendre, vous pouvez consulter la vidéo ci-dessous :

%[https://youtu.be/HhgXwKFUzT8]

## Installation

Pour commencer ce processus, nous devons nous assurer que nous avons le Framework Serverless installé et qu'un profil AWS est configuré sur notre ordinateur. Si ce n'est pas le cas, vous pouvez [regarder cette vidéo](https://youtu.be/D5_FHbdsjRc) pour savoir comment tout configurer.

Si vous souhaitez suivre ce tutoriel, vous pouvez suivre toutes les étapes ou [télécharger le code ici](https://www.subscribepage.com/awstypescriptapizip) et suivre avec le code terminé.

Maintenant, nous passons à la création de notre projet serverless et de notre API. Nous devons commencer dans un terminal et exécuter la commande pour créer notre nouveau dépôt. Tout ce que vous avez à faire est de remplacer `{YOUR FOLDER NAME}` par le nom de votre dossier.

```
serverless create --template aws-nodejs-typescript --path {YOUR FOLDER NAME}
```

Cela créera un projet serverless très basique avec TypeScript. Si nous ouvrons ce nouveau dossier avec VS Code, nous pouvons voir ce que le modèle nous a donné.

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-21-at-06.54.45.png)

Les principaux fichiers que nous voulons examiner sont le fichier `serverless.ts` et le fichier `handler.ts`.

Le fichier `serverless.ts` est où la configuration pour le déploiement est stockée. Ce fichier indique au framework serverless le nom du projet, le langage d'exécution du code, la liste des fonctions et quelques autres options de configuration. 

Chaque fois que nous voulons changer l'architecture de notre projet, c'est le fichier avec lequel nous travaillerons.

Le fichier suivant est le fichier `handler.ts`. Ici, nous avons le code d'exemple pour une lambda donné par le modèle. Il est très basique et retourne simplement une réponse API Gateway avec un message et l'événement d'entrée. Nous utiliserons cela plus tard comme bloc de départ pour notre propre API.

## Créer votre propre Lambda

Maintenant que nous avons vu ce que nous obtenons avec le modèle, il est temps d'ajouter notre propre Lambda et notre point de terminaison API.

Pour commencer, nous allons créer un nouveau dossier pour contenir tout notre code lambda et l'appeler `lambdas`. Cela aide à l'organiser, surtout lorsque vous commencez à avoir quelques lambdas différentes dans un projet.

Dans ce nouveau dossier, nous allons créer notre nouvelle lambda en l'appelant `getCityInfo.ts`. Si nous ouvrons ce fichier, nous pouvons commencer à créer notre code. Nous pouvons commencer par copier tout le code de `handler.ts` comme point de départ.

La première chose que nous allons faire est de changer le nom de la fonction en `handler`. C'est une préférence personnelle, mais j'aime nommer la fonction qui gère l'événement handler.

Sur la première ligne de cette fonction, nous devons ajouter du code pour obtenir la ville que l'utilisateur demande. Nous pouvons l'obtenir à partir du chemin de l'URL en utilisant `pathParameters`.

```js
const city = event.pathParameters?.city;
```

Une chose que vous avez peut-être remarquée est l'utilisation de `?.` dans cette déclaration. C'est l'enchaînement optionnel et c'est une fonctionnalité vraiment cool. 

Cela signifie _si le paramètre de chemin est vrai alors obtenir le paramètre de ville, sinon retourner indéfini._ Cela signifie que si `pathParameter` n'était pas un objet, cela ne donnerait pas l'erreur `cannot read property city of undefined` qui fait planter le runtime Node.

Maintenant que nous avons la ville, nous devons vérifier que la ville est valide et que nous avons des données pour cette ville. Pour cela, nous avons besoin de données. Nous pouvons utiliser le code ci-dessous et le coller en bas du fichier.

```
interface CityData {
    name: string;
    state: string;
    description: string;
    mayor: string;
    population: number;
    zipCodes?: string;
}

const cityData: { [key: string]: CityData } = {
    newyork: {
        name: 'New York',
        state: 'New York',
        description:
            'New York City comprend 5 arrondissements situés où la rivière Hudson rencontre l'océan Atlantique. Au cœur de celle-ci se trouve Manhattan, un arrondissement densément peuplé qui est l'un des principaux centres commerciaux, financiers et culturels du monde. Ses sites emblématiques incluent des gratte-ciels tels que l'Empire State Building et le vaste Central Park. Le théâtre de Broadway est présenté dans Times Square illuminé de néons.',
        mayor: 'Bill de Blasio',
        population: 8399000,
        zipCodes: '100xx104xx, 1100405, 111xx114xx, 116xx',
    },
    washington: {
        name: 'Washington',
        state: 'District of Columbia',
        description: `DescriptionWashington, DC, la capitale des États-Unis, est une ville compacte sur la rivière Potomac, bordant les États du Maryland et de la Virginie. Elle est définie par des monuments et des bâtiments néoclassiques imposants, y compris les icônes qui abritent les 3 branches du gouvernement fédéral : le Capitole, la Maison Blanche et la Cour suprême. C'est également le foyer de musées emblématiques et de lieux de spectacle tels que le Kennedy Center.`,
        mayor: 'Muriel Bowser',
        population: 705549,
    },
    seattle: {
        name: 'Seattle',
        state: 'Washington',
        description: `DescriptionSeattle, une ville sur le Puget Sound dans le Nord-Ouest Pacifique, est entourée d'eau, de montagnes et de forêts de conifères, et contient des milliers d'acres de parcs. La plus grande ville de l'État de Washington, elle abrite une grande industrie technologique, avec Microsoft et Amazon ayant leur siège dans sa région métropolitaine. La futuriste Space Needle, un héritage de la Foire mondiale de 1962, est son monument le plus emblématique.`,
        mayor: 'Jenny Durkan',
        population: 744955,
    },
};
```

La différence entre cela et JavaScript est que nous pouvons créer une _interface_ pour dire au système quelle doit être la structure des données. Cela semble être un travail supplémentaire au début, mais cela aidera à rendre tout plus facile plus tard.

Dans notre interface, nous définissons les clés de l'objet ville ; certaines sont des chaînes, une est un nombre, et ensuite `zipCodes` est une propriété optionnelle. Cela signifie qu'elle pourrait être là mais n'a pas à l'être.

Si nous voulons tester notre interface, nous pouvons essayer d'ajouter une nouvelle propriété à l'une des villes dans nos données de ville. 

TypeScript devrait vous dire instantanément que votre nouvelle propriété n'existe pas sur l'interface. Si vous supprimez l'une des propriétés requises, TypeScript se plaindra également. Cela garantit que vous avez toujours les données correctes et que les objets ont toujours l'apparence attendue.

Maintenant que nous avons les données, nous pouvons vérifier si l'utilisateur a envoyé la demande de ville correcte.

```js
if (!city || !cityData[city]) {
    
}
```

Si cette déclaration est vraie, alors l'utilisateur a fait quelque chose de mal, donc nous devons retourner une réponse 400. 

Nous pourrions simplement taper le code ici, mais nous allons créer un nouvel objet `apiResponses` avec des méthodes pour quelques-uns des codes de réponse possibles de l'API.

```js
const apiResponses = {
    _200: (body: { [key: string]: any }) => {
        return {
            statusCode: 200,
            body: JSON.stringify(body, null, 2),
        };
    },
    _400: (body: { [key: string]: any }) => {
        return {
            statusCode: 400,
            body: JSON.stringify(body, null, 2),
        };
    },
};
```

Cela rend simplement beaucoup plus facile de réutiliser plus tard dans le fichier. Vous devriez également voir que nous avons une propriété de `body: { [key: string]: any }`. Cela indique que cette fonction a une propriété de body qui doit être un objet. Cet objet peut avoir des clés qui ont une valeur de n'importe quel type. 

Parce que nous savons que `body` sera toujours une chaîne, nous pouvons utiliser `JSON.stringify` pour nous assurer que nous retournons un body de chaîne.

Si nous ajoutons cette fonction à notre handler, nous obtenons ceci :

```js
export const handler: APIGatewayProxyHandler = async (event, _context) => {
    const city = event.pathParameters?.city;

    if (!city || !cityData[city]) {
        return apiResponses._400({ message: 'ville manquante ou aucune donnée pour cette ville' });
    }

    return apiResponses._200(cityData[city]);
};
```

Si l'utilisateur n'a pas passé une ville ou a passé une ville pour laquelle nous n'avons pas de données, nous retournons une erreur 400 avec un message d'erreur. Si les données existent, nous retournons une réponse 200 avec un body des données.

# Ajout d'une nouvelle API de traduction

Dans la section précédente, nous avons configuré notre dépôt d'API TypeScript et créé une lambda qui utilisait simplement des données codées en dur. 

Cette partie va vous apprendre comment utiliser le _aws-sdk_ pour interagir directement avec d'autres services AWS afin de créer une API vraiment puissante.

%[https://youtu.be/xdWpbr1DZHQ]

Pour commencer, nous devons ajouter un nouveau fichier pour notre API de traduction. Créez un nouveau fichier sous le dossier `lambdas` appelé `translate.ts`. Nous pouvons commencer ce fichier avec un peu de code de base. C'est le code de départ pour une Lambda API TypeScript.

```js
import { APIGatewayProxyHandler } from 'aws-lambda';
import 'source-map-support/register';

export const handler: APIGatewayProxyHandler = async (event) => {
    
};
```

Maintenant, nous devons obtenir le texte que l'utilisateur veut traduire et la langue dans laquelle il veut le traduire. Nous pouvons obtenir ces informations à partir du corps de la requête. 

Une chose supplémentaire que nous devons faire ici est de parser le corps. Par défaut, API Gateway stringifie tout JSON passé dans le corps. Nous pouvons ensuite déstructurer le texte et la langue à partir du corps.

```js
const body = JSON.parse(event.body);
const { text, language } = body;
```

Nous devons maintenant vérifier que l'utilisateur a passé le texte et la langue.

```js
if (!text) {
    // retourner 400
}
if (!language) {
    // retourner 400
}
```

Dans la dernière partie, nous avons créé la réponse 400 en tant que fonction dans le fichier. Comme nous allons utiliser ces réponses API dans plusieurs fichiers, il est bon de les extraire dans leur propre fichier _commun_.

Créez un nouveau dossier sous _lambdas_ appelé `common`. C'est là que nous allons stocker toutes les fonctions communes. 

Dans ce dossier, créez un nouveau fichier appelé `apiResponses.ts`. Ce fichier va exporter l'objet `apiResponses` avec les méthodes __200 et _400_. Si vous devez retourner d'autres codes de réponse, vous pouvez les ajouter à cet objet.

```js
const apiResponses = {
    _200: (body: { [key: string]: any }) => {
        return {
            statusCode: 200,
            body: JSON.stringify(body, null, 2),
        };
    },
    _400: (body: { [key: string]: any }) => {
        return {
            statusCode: 400,
            body: JSON.stringify(body, null, 2),
        };
    },
};

export default apiResponses;
```

Nous pouvons maintenant importer cet objet dans notre code et utiliser ces méthodes communes dans notre code. En haut de notre fichier _translate.ts_, nous pouvons maintenant ajouter cette ligne :

```js
import apiResponses from './common/apiResponses';
```

et mettre à jour nos vérifications de texte et de langue pour appeler la méthode __400_ sur cet objet :

```js
if (!text) {
    return apiResponses._400({ message: 'texte manquant dans le corps' });
}
if (!language) {
    return apiResponses._400({ message: 'langue manquante dans le corps' });
}
```

Avec cela terminé, nous savons que nous avons le texte à traduire et une langue dans laquelle le traduire, donc nous pouvons commencer le processus de traduction. 

L'utilisation du aws-sdk est presque toujours une tâche asynchrone, donc nous allons l'envelopper dans un _try/catch_ pour que notre gestion des erreurs soit plus facile.

```js
try {
    
} catch (error) {
    
}
```

La première chose que nous devons faire est d'importer le aws-sdk et de créer une nouvelle instance du service de traduction. 

Pour cela, nous devons installer le aws-sdk puis l'importer. D'abord, exécutez `npm install --save aws-sdk` puis ajoutez ce code en haut de votre fichier translate :

```js
import * as AWS from 'aws-sdk';

const translate = new AWS.Translate();
```

Avec cela, nous pouvons commencer à écrire notre code de traduction. Nous allons commencer par la ligne qui fait la traduction en premier. Ajoutez ceci dans la section _try_.

```js
const translatedMessage = await translate.translateText(translateParams).promise();
```

Une chose que certains d'entre vous ont peut-être remarquée est que nous passons `translateParams` sans l'avoir défini. C'est parce que nous ne sommes pas encore sûrs de son type. 

Pour le découvrir, nous pouvons utiliser un outil dans VS Code appelé `go to definition`. Cela nous permet de sauter à l'endroit où la fonction est définie afin que nous puissions découvrir quel est le type des paramètres. Vous pouvez soit faire un clic droit et sélectionner `go to definition`, soit maintenir la touche _Ctrl_ et cliquer sur la fonction.

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-23-at-08.14.03.png)

Comme vous pouvez le voir, la fonction `translateText` prend un paramètre de `Translate.Types.TranslateTextRequest`. 

Une autre façon de le découvrir est d'utiliser _intelisense_ en survolant la fonction `translateText`. Vous devriez voir ceci, où vous pouvez voir que `params: AWS.Translate.TranslateTextRequest` :

![Image](https://completecoding.io/content/images/2020/08/Screenshot-2020-08-23-at-08.15.30.png)

Avec cela, nous pouvons créer nos paramètres de traduction au-dessus de la requête de traduction que nous avons faite précédemment. Nous pouvons ensuite le remplir en fonction du type que nous définissons. Cela garantit que nous passons les champs corrects.

```js
const translateParams: AWS.Translate.Types.TranslateTextRequest = {
    Text: text,
    SourceLanguageCode: 'en',
    TargetLanguageCode: language,
};
```

Maintenant que nous avons les paramètres et que nous les passons dans la fonction `translate.translateText`, nous pouvons commencer à créer notre réponse. Il s'agit simplement d'une réponse 200 avec le message traduit.

```js
return apiResponses._200({ translatedMessage });
```

Avec cela terminé, nous pouvons passer à la section _catch_. Ici, nous voulons simplement logger l'erreur et ensuite retourner une réponse 400 à partir du fichier commun.

```js
console.log('erreur dans la traduction', error);
return apiResponses._400({ message: 'impossible de traduire le message' });
```

Avec cela terminé, nous avons terminé avec notre code lambda, donc nous devons passer à notre fichier `severless.ts` pour ajouter ce nouveau point de terminaison API et lui donner les permissions dont il a besoin.

Dans le fichier `serverless.ts`, nous pouvons faire défiler jusqu'à la section `functions`. Ici, nous devons ajouter une nouvelle fonction à l'objet.

```js
translate: {
    handler: 'lambdas/translate.handler',
    events: [
        {
            http: {
                path: 'translate',
                method: 'POST',
                cors: true,
            },
        },
    ],
},
```

La principale différence entre cela et le point de terminaison précédent est que le point de terminaison est maintenant une méthode _POST_. Cela signifie que si vous essayez de faire une requête _GET_ à cette URL, vous obtiendrez une réponse d'erreur.

La dernière chose à faire est de donner aux lambdas la permission d'utiliser le service de traduction. Avec presque tous les services AWS, vous devrez ajouter des permissions supplémentaires pour pouvoir les utiliser depuis une lambda. 

Pour cela, nous ajoutons un nouveau champ à la section `provider` appelé `iamRoleStatements`. Il s'agit d'un tableau de déclarations _allow_ ou _deny_ pour différents services et ressources.

```
iamRoleStatements: [
    {
        Effect: 'Allow',
        Action: ['translate:*'],
        Resource: '*',
    },
],
```

Avec cela ajouté, nous avons tout ce dont nous avons besoin pour exécuter `sls deploy` et déployer notre nouvelle API.

Une fois cela déployé, nous pouvons obtenir l'URL de l'API et utiliser un outil comme postman ou [postwoman.io](https://postwoman.io/) pour faire une requête à cette URL. Nous devons simplement passer un corps de :

```js
{
    "text": "This is a test message for translation",
    "language": "fr"
}
```

et ensuite nous devrions obtenir une réponse 200 de :

```js
{
  "translatedMessage": {
    "TranslatedText": "Ceci est un message de test pour la traduction",
    "SourceLanguageCode": "en",
    "TargetLanguageCode": "fr"
  }
}
```

# Résumé

Dans cet article, nous avons appris comment :

* Configurer un nouveau dépôt TypeScript avec `severless create --template aws-nodejs-typescript`
* Ajouter notre propre Lambda qui retourne une sélection de données codées en dur
* Ajouter cette Lambda en tant que point de terminaison API
* Ajouter une autre Lambda qui traduira automatiquement tout texte qui lui est passé
* Ajouter un point de terminaison API et donner à la Lambda les permissions dont elle a besoin pour fonctionner

Si vous avez aimé cet article et que vous souhaitez en apprendre davantage sur Serverless et AWS, alors j'ai une chaîne YouTube avec plus de 50 vidéos sur tout cela. Je vous recommande de regarder les vidéos qui vous intéressent le plus dans ma [playlist Serverless et AWS](https://www.youtube.com/playlist?list=PLmexTtcbIn_gP8bpsUsHfv-58KsKPsGEo).