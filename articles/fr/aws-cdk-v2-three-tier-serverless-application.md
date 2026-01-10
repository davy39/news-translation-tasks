---
title: Tutoriel AWS CDK v2 – Comment créer une application serverless à trois niveaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-25T21:32:22.000Z'
originalURL: https://freecodecamp.org/news/aws-cdk-v2-three-tier-serverless-application
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/three-tier-1.jpeg
tags:
- name: AWS
  slug: aws
- name: serverless
  slug: serverless
seo_title: Tutoriel AWS CDK v2 – Comment créer une application serverless à trois
  niveaux
seo_desc: "By Matt Morgan\nA three-tier web application has a presentation layer,\
  \ an application layer, and a database layer. \nThis familiar pattern is fertile\
  \ ground for learning new technologies like the AWS Cloud Development Kit (CDK).\
  \ \nIn this tutorial, we w..."
---

Par Matt Morgan

Une application web à trois niveaux possède une couche de présentation, une couche applicative et une couche de base de données. 

Ce modèle familier est un terrain fertile pour apprendre de nouvelles technologies comme l'AWS Cloud Development Kit (CDK). 

Dans ce tutoriel, nous allons créer une application simple de prise de notes en utilisant une table DynamoDB, des points de terminaison d'API HTTP, des gestionnaires Lambda et une application frontend React avec le réseau de diffusion de contenu (CDN) CloudFront. 

Tout cela peut être déployé sur un compte AWS en utilisant une seule commande. Et tout cela sera écrit en TypeScript. 

Le code source de ce tutoriel est disponible sur [GitHub](https://github.com/elthrasher/cdk-three-tier-serverless).


### Comment obtenir les identifiants de compte AWS

Pour commencer, nous aurons besoin d'un compte AWS et d'identifiants disponibles dans notre ligne de commande. Toutes les ressources déployées dans ce tutoriel devraient rester dans le niveau gratuit d'utilisation, cependant une carte de crédit est toujours requise pour s'inscrire à un compte AWS. 

Si vous n'avez pas encore de compte AWS, [ici](https://acloudguru.com/videos/acg-fundamentals/how-to-create-an-aws-account) se trouve une bonne ressource pour le faire en toute sécurité et en gardant à l'esprit les meilleures pratiques. 

Les nouveaux venus sur AWS peuvent également consulter l'[Atelier CDK](https://cdkworkshop.com/), en particulier la partie sur la création d'un [compte et utilisateur AWS](https://cdkworkshop.com/15-prerequisites/200-account.html).


### Autres prérequis

Lorsqu'on travaille avec AWS, il est judicieux d'installer l'[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Vous aurez également besoin d'avoir une version récente de [Node.js](https://nodejs.org/en/) installée.


## Comment initialiser l'application

Pour commencer, nous pouvons utiliser l'utilitaire de ligne de commande cdk pour échafauder une application.

1. `mkdir cdk-three-tier-serverless && cd cdk-three-tier-serverless`
2. `npx cdk init app --language=typescript`

Cela créera quelques fichiers pour nous aider à démarrer et téléchargera les dépendances nécessaires.


### CDK v1 vs v2 – Quelle est la différence ?

AWS CDK v2 a été rendu [généralement disponible](https://aws.amazon.com/about-aws/whats-new/2021/12/aws-cloud-development-kit-cdk-generally-available/) en décembre 2021. AWS a annoncé que v1 entrera dans une phase de maintenance et mettra fin au support de v1 en juin 2023. La principale différence entre v1 et v2 est que v2 fait un meilleur travail de gestion des dépendances. Les constructs publiés construits pour v1 devront être mis à jour avant de pouvoir fonctionner dans les applications v2.


### Qu'est-ce que Projen ? (Optionnel)

[Projen](https://github.com/projen/projen) est populaire dans la communauté CDK comme alternative à `cdk init`. Pour éviter d'introduire trop de concepts, ce tutoriel n'utilise pas projen mais vous pourriez créer une application très similaire en commençant par `npx projen new awscdk-app-ts`.


## Comment démarrer votre compte AWS

Afin d'utiliser notre compte AWS avec AWS CDK, nous devons d'abord démarrer le compte en déployant une pile simple pour gérer nos actifs dans le compte. 

Vous pouvez faire cela en entrant `npx cdk bootstrap` à la ligne de commande. Il est préférable de le faire _après_ avoir initialisé un projet ou le bootstrap demandera des informations supplémentaires. Si le bootstrap est réussi, nous sommes prêts à continuer à construire notre application, sinon, nous devrions nous référer à la [documentation officielle](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) pour des conseils de dépannage.


### Comment démarrer les rôles AWS (optionnel)

Le bootstrap créera plusieurs rôles qui peuvent être utilisés pour déployer, gérer des actifs et rechercher des noms de ressources Amazon (ARN). Bien que vous puissiez compléter ce tutoriel avec un utilisateur ayant la politique AdministratorAccess, ce n'est pas une meilleure pratique. 

Si nous recherchons les ARN des rôles créés par le bootstrap, nous pouvons construire une politique fine et l'appliquer à un nouvel utilisateur.

La politique que nous créons pourrait ressembler à ceci. Voir les [docs officiels](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) sur la création d'utilisateurs IAM.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "assumecdkroles",
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole",
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::1234567890:role/cdk-abc123-deploy-role-1234567890-us-east-1",
                "arn:aws:iam::1234567890:role/cdk-abc123-file-publishing-role-1234567890-us-east-1",
                "arn:aws:iam::1234567890:role/cdk-abc123-image-publishing-role-1234567890-us-east-1",
                "arn:aws:iam::1234567890:role/cdk-abc123-lookup-role-1234567890-us-east-1"
            ]
        }
    ]
}
```

Une politique comme celle-ci dans un compte qui a également la MFA et l'accès root verrouillé devrait fournir un degré raisonnable de sécurité pour les apprenants. Les utilisateurs d'entreprise voudront penser à configurer [AWS SSO](https://aws.amazon.com/single-sign-on/) et une [Organisation AWS](https://github.com/aws-samples/aws-bootstrap-kit-examples/blob/main/source/1-SDLC-organization/README.md). 

## Comment construire la couche de données

Nous allons commencer par construire la couche de données. Nous pourrons déployer notre application à chaque étape et vérifier notre progression dans la console AWS.


### Comment créer une table DynamoDB

L'opération init aura créé un fichier appelé cdk-three-tier-serverless-stack.ts. Nous pouvons commencer par là pour construire notre application. D'abord, supprimons le code commenté et ajoutons une déclaration de Table. Notez que, contrairement aux applications CDK v1, il n'est pas nécessaire d'installer des packages supplémentaires pour commencer à utiliser DynamoDB.


```TypeScript
import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { AttributeType, BillingMode, Table } from 'aws-cdk-lib/aws-dynamodb';
import { Construct } from 'constructs';

export class CdkThreeTierServerlessStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const table = new Table(this, 'NotesTable', {
      billingMode: BillingMode.PAY_PER_REQUEST,
      partitionKey: { name: 'pk', type: AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY,
      sortKey: { name: 'sk', type: AttributeType.STRING },
      tableName: 'NotesTable',
    });
  }
}
```

Nous pouvons immédiatement déployer cette table en utilisant `npx cdk deploy` puis l'inspecter dans la console.

![NotesTable](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-23-at-2.30.20-PM.png)

### Comment modéliser les données en utilisant AWS DynamoDB OneTable

[OneTable](https://github.com/sensedeep/dynamodb-onetable) est un outil pour gérer les requêtes DynamoDB. Le concept derrière lui est que plusieurs entités différentes peuvent être modélisées dans la même table DynamoDB, une pratique approuvée par de nombreux experts dans le domaine. 

Dans notre application simple, nous n'aurons que l'entité unique notes, mais nous utiliserons OneTable pour gérer notre schéma. Puisque DynamoDB est une base de données NoSQL, le schéma n'est pas défini lors de la création de la table et nous allons plutôt le définir dans le code de l'application.

Pour commencer, nous devons installer les dépendances.

```bash
npm i @aws-sdk/client-dynamodb dynamodb-onetable
```

Nous allons créer deux fonctions Lambda dans un instant et nous voudrons partager un modèle entre elles. Nous pouvons organiser le code de la manière que nous voulons. Créons un dossier "fns" sous lib et créons des fichiers appelés notesTable.ts, readFunction.ts et writeFunction.ts.

![disposition du projet](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-12-at-11.00.58-AM-2.png)

Nous pouvons définir un schéma dans notesTable.ts.

```TypeScript
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { Entity, Table } from 'dynamodb-onetable';
import Dynamo from 'dynamodb-onetable/Dynamo';

const client = new Dynamo({ client: new DynamoDBClient({}) });

const schema = {
  indexes: {
    primary: {
      hash: 'pk',
      sort: 'sk',
    },
  },
  models: {
    note: {
      type: {
        required: true,
        type: 'string',
        value: 'note',
      },
      pk: {
        type: 'string',
        value: 'note',
      },
      sk: {
        type: 'string',
        value: '${date}',
      },
      note: {
        required: true,
        type: 'string',
      },
      date: {
        required: true,
        type: 'string',
      },
      subject: {
        required: true,
        type: 'string',
      },
    },
  },
  version: '0.1.0',
  params: {
    typeField: 'type',
  },
  format: 'onetable:1.0.0',
} as const;

export type NoteType = Entity<typeof schema.models.note>;

const table = new Table({
  client,
  name: 'NotesTable',
  schema,
  timestamps: true,
});

export const Notes = table.getModel<NoteType>('note');
```

Nous définissons les propriétés de "type", "subject", "note" et "date" pour le modèle. Tous ceux-ci auront le type string. Nous allons également indiquer que la clé de partition sera toujours définie sur "note". Cela convient pour une petite application d'exemple, mais pour quelque chose de plus grand, il serait logique d'utiliser une valeur comme un identifiant d'utilisateur ou un identifiant de compte basé sur les types de requêtes ou les modèles d'accès que l'application nécessite. 

La clé de tri et le champ de date auront exactement les mêmes données. Cette duplication de données est une meilleure pratique car elle nous permettra d'avoir différents types d'entités dans notre table et certaines d'entre elles ne seront peut-être pas triées par date.

## La couche applicative

Notre couche applicative sera composée de quelques fonctions Lambda et d'une API Gateway pour les connecter à Internet.

### Gestionnaires Lambda

Nous allons maintenant remplir nos gestionnaires Lambda. Nous pouvons ajouter des typages supplémentaires pour faciliter le travail dans un environnement TypeScript.


```bash
npm i -D @types/aws-lambda
```


Grâce à OneTable qui extrait une grande partie de la complexité de la gestion de DynamoDB, nos gestionnaires Lambda sont assez simples. Notre fonction de lecture exécute une opération de recherche et retourne le résultat.


```TypeScript
import type { APIGatewayProxyResultV2 } from 'aws-lambda';

import { Notes } from './notesTable';

export const handler = async (): Promise<APIGatewayProxyResultV2> => {
  const notes = await Notes.find({ pk: 'note' }, { limit: 10, reverse: true });
  return { body: JSON.stringify(notes), statusCode: 200 };
};
```


L'ajout des paramètres limit et reverse signifie que la requête retournera les dix notes les plus récentes, automatiquement triées par la clé de tri.

Notre fonction d'écriture est également assez simple.


```TypeScript
import type {
  APIGatewayProxyEventV2,
  APIGatewayProxyResultV2,
} from 'aws-lambda';

import { Notes } from './notesTable';

export const handler = async (
  event: APIGatewayProxyEventV2
): Promise<APIGatewayProxyResultV2> => {
  const body = event.body;
  if (body) {
    const notes = await Notes.create(JSON.parse(body));
    return { body: JSON.stringify(notes), statusCode: 200 };
  }
  return { body: 'Error, invalid input!', statusCode: 400 };
};
```



### Le construct NodejsFunction

En revenant à notre pile, nous devons maintenant créer les constructs de fonction. Nos fonctions Lambda seront écrites en TypeScript et nécessiteront donc une étape de transpilation avant de pouvoir s'exécuter dans le runtime Lambda. 

Heureusement, le CDK fournit un construct NodejsFunction qui s'occupera de cela pour nous. NodejsFunction utilise [esbuild](https://esbuild.github.io/), un transpileur très rapide. esbuild n'est pas une dépendance directe de CDK, nous devons donc l'installer pour éviter le fallback plus lent, qui construit dans Docker.

npm i -D esbuild

Nous pouvons maintenant ajouter les constructs à notre pile.

```TypeScript
import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { AttributeType, BillingMode, Table } from 'aws-cdk-lib/aws-dynamodb';
import { Architecture } from 'aws-cdk-lib/aws-lambda';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { RetentionDays } from 'aws-cdk-lib/aws-logs';
import { Construct } from 'constructs';

export class CdkThreeTierServerlessStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const table = new Table(this, 'NotesTable', {
      billingMode: BillingMode.PAY_PER_REQUEST,
      partitionKey: { name: 'pk', type: AttributeType.STRING },
      removalPolicy: RemovalPolicy.DESTROY,
      sortKey: { name: 'sk', type: AttributeType.STRING },
      tableName: 'NotesTable',
    });

    const readFunction = new NodejsFunction(this, 'ReadNotesFn', {
      architecture: Architecture.ARM_64,
      entry: `${__dirname}/fns/readFunction.ts`,
      logRetention: RetentionDays.ONE_WEEK,
    });

    const writeFunction = new NodejsFunction(this, 'WriteNoteFn', {
      architecture: Architecture.ARM_64,
      entry: `${__dirname}/fns/writeFunction.ts`,
      logRetention: RetentionDays.ONE_WEEK,
    });
  }
}
```


Notre liste d'imports s'allonge, mais tous ont été installés avec aws-cdk-lib, donc pas de souci de versionnage. Une autre chose dont nous aurons besoin est d'accorder des permissions à nos fonctions pour accéder à la table.


```TypeScript
    table.grantReadData(readFunction);

    table.grantWriteData(writeFunction);
```


Tout cela peut être déployé à ce stade. Bien que nos fonctions ne seront pas accessibles sur Internet, elles pourraient être exécutées depuis la console AWS.

Les fonctions Lambda doivent être testées unitairement ! L'écriture de tests dépassera le cadre de ce tutoriel, mais vous pouvez voir quelques tests dans le [dépôt source](https://github.com/elthrasher/cdk-three-tier-serverless/tree/main/lib/fns).

### API HTTP

Nous allons construire notre API orientée utilisateur en utilisant l'API HTTP d'AWS API Gateway. L'API HTTP est une alternative à moindre coût à l'API REST. Le construct CDK pour l'API HTTP est encore expérimental, nous devons donc installer des modules supplémentaires pour l'utiliser.


```bash
npm i @aws-cdk/aws-apigatewayv2-alpha @aws-cdk/aws-apigatewayv2-integrations-alpha
```


Ensuite, nous pouvons importer les classes nécessaires dans notre pile.


```TypeScript
import {
  CorsHttpMethod,
  HttpApi,
  HttpMethod,
} from '@aws-cdk/aws-apigatewayv2-alpha';
import { HttpLambdaIntegration } from '@aws-cdk/aws-apigatewayv2-integrations-alpha';
```


Pour créer l'API HTTP, nous aurons besoin du construct de base avec une configuration CORS, puisque notre vue sera servie depuis un domaine CloudFront. Ensuite, nous créons des constructs d'intégration et enfin nous ajoutons les routes.

```TypeScript
    const api = new HttpApi(this, 'NotesApi', {
      corsPreflight: {
        allowHeaders: ['Content-Type'],
        allowMethods: [CorsHttpMethod.GET, CorsHttpMethod.POST],
        allowOrigins: ['*'],
      },
    });

    const readIntegration = new HttpLambdaIntegration(
      'ReadIntegration',
      readFunction
    );

    const writeIntegration = new HttpLambdaIntegration(
      'WriteIntegration',
      writeFunction
    );

    api.addRoutes({
      integration: readIntegration,
      methods: [HttpMethod.GET],
      path: '/notes',
    });

    api.addRoutes({
      integration: writeIntegration,
      methods: [HttpMethod.POST],
      path: '/notes',
    });
```


API Gateway générera automatiquement une URL pour notre point de terminaison. Nous pourrions appliquer un domaine personnalisé, mais cela coûterait quelque chose, donc nous utiliserons l'URL générée pour l'instant. Il est souhaitable de sortir cela de notre pile afin de ne pas avoir à la rechercher sur la console. Nous pouvons ajouter CfnOutput à nos imports aws-cdk-lib et une ligne supplémentaire à notre pile.


```TypeScript
new CfnOutput(this, 'HttpApiUrl', { value: api.apiEndpoint });
```


Maintenant, déployons-le à nouveau avec `npx cdk deploy`. Nous serons récompensés par une sortie qui ressemble à ceci.

Sorties :

CdkThreeTierServerlessStack.HttpApiUrl = https://g50qzchav1.execute-api.us-east-1.amazonaws.com

Nous pouvons immédiatement ouvrir [https://g50qzchav1.execute-api.us-east-1.amazonaws.com/notes](https://g50qzchav1.execute-api.us-east-1.amazonaws.com/notes) dans un navigateur web et voir l'API fonctionnelle. Comme il n'y a encore rien dans la base de données, nous obtiendrons simplement un tableau vide. Nous pourrions utiliser un client REST et commencer à poster des données, mais au lieu de cela, construisons notre interface utilisateur.

### Capturer l'URL de l'API

Afin d'avoir une meilleure expérience de développement, nous pouvons en fait stocker cette URL dans un fichier de configuration local pour l'utiliser dans notre projet. Cela peut être fait en ajoutant l'argument --outputs-file à notre commande de déploiement. Nous pouvons ajouter cela à nos scripts npm pour générer un config.json.

![scripts npm](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-12-at-12.20.35-PM.png)

Il est probablement judicieux d'ajouter ce fichier config.json à notre .gitignore. Nous n'en aurons pas besoin dans le contrôle de source et nous gérerons notre application web déployée d'une autre manière.

## La couche de présentation

Enfin, construisons la couche de présentation. Nous utiliserons React dans ce tutoriel. La couche de présentation sera servie via une distribution CloudFront, mais elle peut être construite et déployée dans le cadre de notre application CDK.

### Application React

Une chose cool à propos des applications full-stack TypeScript est que nous pouvons gérer toutes nos dépendances en un seul endroit. Nous allons construire une application React en TypeScript. Nous allons la bundler avec esbuild et utiliser [vitejs](https://vitejs.dev/), un outil sympa qui ajoute le rechargement en direct et quelques autres capacités de qualité de vie à esbuild. Ajoutons nos dépendances et devDependencies. Notez que la distinction ici est plus par convention et que cette application fonctionnera probablement de la même manière que ces dépendances soient dans dependencies ou devDependencies.

```bash
npm i react react-dom
npm i -D @types/react @types/react-dom @vitejs/plugin-react-refresh vite
```

Par convention, vitejs veut un index.html à la racine du projet, alors ajoutons cela.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta
      name="description"
      content="Sample Three-tier Serverless Web Application"
    />
    <meta
      http-equiv="Cache-Control"
      content="no-cache, no-store, must-revalidate"
    />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Three-tier Serverless Web App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/lib/web/main.tsx"></script>
  </body>
</html>
```

Le fichier index.html fait directement référence à un fichier main.tsx. Créons un nouveau répertoire sous lib appelé web et ajoutons App.tsx, index.css, main.tsx et utils.ts dans ce sous-répertoire.

Puisque nous ajoutons React au projet, nous devons modifier notre fichier tsconfig.json en ajoutant les clés et valeurs suivantes :

```json
    "jsx": "react",
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true
```


Nous devrons également ajouter une autre valeur à la clé "lib" dans tsconfig.json.

```json
    "lib": ["DOM", "es2018"],
```

Maintenant, écrivons ce fichier main.tsx. C'est le point d'entrée de l'application React et il ne doit invoquer qu'un autre composant.


```TypeScript
import './index.css';

import React from 'react';
import ReactDOM from 'react-dom';

import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
```


Nous pouvons mettre ensemble un peu de CSS dans index.css pour démarrer l'application.


```css
body {
  background-color: darkslategray;
  color: antiquewhite;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande',
    'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  font-size: 16pt;
}

button {
  background-color: forestgreen;
  color: white;
}

input,
textarea {
  width: 200px;
}

table {
  border: 1px solid;
  margin: 20px;
}

td {
  font-size: 12pt;
  padding: 10px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```


App.tsx commence à devenir un peu long et pourrait être mieux divisé en composants individuels, mais la gestion de l'état React est bien au-delà du cadre de ce tutoriel, alors gardons cela simple.


```TypeScript
import React, { useEffect, useState } from 'react';

import { NoteType } from '../fns/notesTable';
import { getNotes, saveNote } from './utils';

const App = () => {
  const [body, setBody] = useState('');
  const [notes, setNotes] = useState([]);
  const [subject, setSubject] = useState('');
  useEffect(() => {
    getNotes().then((n) => setNotes(n));
  }, []);
  const clickHandler = async () => {
    if (body && subject) {
      setBody('');
      setSubject('');
      await saveNote({
        date: new Date().toISOString(),
        note: body,
        subject,
        type: 'note',
      });
      const n = await getNotes();
      setNotes(n);
    }
  };
  return (
    <div>
      <div>
        <div>
          <input
            onChange={(e) => setSubject(e.target.value)}
            placeholder="Note Subject"
            type="text"
            value={subject}
          />
        </div>
        <div>
          <textarea
            onChange={(e) => setBody(e.target.value)}
            placeholder="Note Body"
            value={body}
          ></textarea>
        </div>
        <div>
          <button onClick={clickHandler}>save</button>
        </div>
      </div>
      <div>
        <table>
          <thead>
            <tr>
              <th>Subject</th>
              <th>Note</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            {notes.map((note: NoteType) => (
              <tr key={note.date}>
                <td>{note.subject}</td>
                <td>{note.note}</td>
                <td>{new Date(note.date).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default App;
```


Nous devons construire notre client HTTP dans utils.ts. Ici, nous avons une étape supplémentaire où nous allons récupérer cette URL de l'API HTTP à partir du fichier config.json que nous avons créé précédemment. De cette façon, nous pouvons avoir un environnement de développement local sans avoir besoin de copier-coller des URL.


```TypeScript
import { NoteType } from '../fns/notesTable';

let url = '';

const getUrl = async () => {
  if (url) {
    return url;
  }
  const response = await fetch('./config.json');
  url = `${(await response.json()).CdkThreeTierServerlessStack.HttpApiUrl}/notes`;
  return url;
};

export const getNotes = async () => {
  const result = await fetch(await getUrl());

  return await result.json();
};

export const saveNote = async (note: NoteType) => {
  await fetch(await getUrl(), {
    body: JSON.stringify(note),
    headers: { 'Content-Type': 'application/json' },
    method: 'POST',
    mode: 'cors',
  });
};
```

Pour activer le plugin react-refresh, nous pouvons optionnellement ajouter un fichier vite.config.ts à la racine de notre projet avec le code suivant.

```TypeScript
import { defineConfig } from 'vite';
import reactRefresh from '@vitejs/plugin-react-refresh';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [reactRefresh()],
});
```

Tout cela fait, nous pouvons démarrer notre serveur de développement en utilisant `npx vite`, puis visualiser l'application web sur http://localhost:3000. Le serveur détectera les changements et rechargera si nous apportons des modifications. Nous pouvons essayer d'enregistrer quelques notes et voir comment cela fonctionne.

![Note App](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-12-at-1.11.48-PM.png)

Pourrait peut-être utiliser une aide de style, mais sinon, cela fonctionne assez bien.

### Distribution CloudFront

Dans cette section, nous allons ajouter plusieurs autres constructs à cdk-three-tier-serverless-stack.ts. Nous n'aurons besoin que d'une dépendance supplémentaire. Notre pile commence à devenir assez grande à ce stade, mais pour les besoins de ce tutoriel, nous allons tout garder dans un seul module. Il est généralement bon de commencer à réfléchir à la manière de décomposer les grands modules ou piles, mais ce sujet approfondi serait mieux couvert dans un autre tutoriel ou article de blog.

Notre application web consistera en un bucket S3 pour le stockage, une distribution CloudFront et une étape de construction pour l'application React, ainsi qu'une ressource personnalisée qui fournira notre URL d'API à l'application web.

Créer un bucket S3 dans CDK est facile. Notez que bien que les sites web S3 soient possibles, ceci **ne** sera **pas** un site web S3 car nous voulons utiliser CloudFront pour le CDN global et https. Si nous avions un domaine personnalisé, nous voudrions également l'attacher à notre distribution CloudFront.

```TypeScript
import { BlockPublicAccess, Bucket } from 'aws-cdk-lib/aws-s3';

    const websiteBucket = new Bucket(this, 'WebsiteBucket', {
      autoDeleteObjects: true,
      blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
      removalPolicy: RemovalPolicy.DESTROY,
    });
```

Nous utilisons `autoDeleteObjects` et `RemovalPolicy.DESTROY` ici simplement parce que c'est un tutoriel. Si vous construisez une application de production, vous pouvez vouloir être plus protecteur de vos actifs.

Ce bucket S3 n'a pas d'accès public. Au lieu de cela, nous allons donner accès via la distribution CloudFront. Pour ce faire, nous allons utiliser le construct OriginAccessIdentity pour accorder l'accès en lecture dont CloudFront aura besoin.

```TypeScript
import {
  Distribution,
  OriginAccessIdentity,
  ViewerProtocolPolicy,
} from 'aws-cdk-lib/aws-cloudfront';

    const originAccessIdentity = new OriginAccessIdentity(
      this,
      'OriginAccessIdentity'
    );
    websiteBucket.grantRead(originAccessIdentity);
```

Ensuite, nous créons la distribution réelle.

```TypeScript
import {
  Distribution,
  OriginAccessIdentity,
  ViewerProtocolPolicy,
} from 'aws-cdk-lib/aws-cloudfront';
import { S3Origin } from 'aws-cdk-lib/aws-cloudfront-origins';

    const distribution = new Distribution(this, 'Distribution', {
      defaultBehavior: {
        origin: new S3Origin(websiteBucket, { originAccessIdentity }),
        viewerProtocolPolicy: ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
      },
      defaultRootObject: 'index.html',
      errorResponses: [
        {
          httpStatus: 404,
          responseHttpStatus: 200,
          responsePagePath: '/index.html',
        },
      ],
    });
```

Cette distribution est conçue pour une application à page unique comme React et mettra à niveau tout le trafic vers https.

Pour la partie suivante, nous allons ajouter une nouvelle bibliothèque d'assistance, fs-extra. Cela facilitera la copie de nos fichiers de construction dans l'application.

```bash
npm i -D @types/fs-extra fs-extra
```

Nous allons utiliser les capacités de bundling d'actifs CDK pour construire notre application React avec vitejs et esbuild dans le cadre de notre processus de synthèse de pile. Par défaut, le bundling d'actifs CDK veut utiliser Docker. Puisque nous sommes déjà dans un runtime NodeJS, nous préférerons contourner la construction Docker plus lente et utiliser plutôt le bundling local.

```TypeScript
import {
  CfnOutput,
  DockerImage,
  RemovalPolicy,
  Stack,
  StackProps,
} from 'aws-cdk-lib';
import { execSync, ExecSyncOptions } from 'child_process';
import { join } from 'path';
import { copySync } from 'fs-extra';

    const execOptions: ExecSyncOptions = {
      stdio: ['ignore', process.stderr, 'inherit'],
    };

    const bundle = Source.asset(join(__dirname, 'web'), {
      bundling: {
        command: [
          'sh',
          '-c',
          'echo "Docker build not supported. Please install esbuild."',
        ],
        image: DockerImage.fromRegistry('alpine'),
        local: {
          tryBundle(outputDir: string) {
            try {
              execSync('esbuild --version', execOptions);
            } catch {
              return false;
            }
            execSync('npx vite build', execOptions);
            copySync(join(__dirname, '../dist'), outputDir, {
              ...execOptions,
              recursive: true,
            });
            return true;
          },
        },
      },
    });
```

Le bundler exécutera vite build qui place notre application web transpilée sous `/dist`, puis il copiera ces fichiers dans le répertoire de staging CDK (généralement cdk.out).

Nous allons finaliser tout cela avec un BucketDeployment qui gère réellement l'envoi de nos modifications au Bucket S3 cible.

```TypeScript
import { BucketDeployment, Source } from 'aws-cdk-lib/aws-s3-deployment';

    new BucketDeployment(this, 'DeployWebsite', {
      destinationBucket: websiteBucket,
      distribution,
      logRetention: RetentionDays.ONE_DAY,
      prune: false,
      sources: [bundle],
    });
```

### AwsCustomResource

Tout cela est assez bien, mais il nous manquera toujours un fichier config.json qui aidera l'application React à connaître notre URL d'API HTTP. Nous pourrions déployer la pile une fois, générer le fichier, puis le bundler et l'envoyer, mais cela signifie que nous devrions déployer deux fois pour mettre en place notre application. Il serait préférable de générer ce fichier à la volée la première fois que nous déployons. Nous pouvons faire cela avec AwsCustomResource. La ressource personnalisée créera implicitement une fonction Lambda qui peut recevoir l'URL générée, puis effectuer un appel AWS SDK pour la stocker dans S3 où notre application web peut la trouver. Tout cela peut être fait avec seulement quelques lignes de code !

```TypeScript
import { AwsCustomResource, AwsCustomResourcePolicy, PhysicalResourceId } from 'aws-cdk-lib/custom-resources';
import { PolicyStatement } from 'aws-cdk-lib/aws-iam';

    new AwsCustomResource(this, 'ApiUrlResource', {
      logRetention: RetentionDays.ONE_DAY,
      onUpdate: {
        action: 'putObject',
        parameters: {
          Body: Stack.of(this).toJsonString({
            [this.stackName]: { HttpApiUrl: api.apiEndpoint },
          }),
          Bucket: websiteBucket.bucketName,
          CacheControl: 'max-age=0, no-cache, no-store, must-revalidate',
          ContentType: 'application/json',
          Key: 'config.json',
        },
        physicalResourceId: PhysicalResourceId.of('config'),
        service: 'S3',
      },
      policy: AwsCustomResourcePolicy.fromStatements([
        new PolicyStatement({
          actions: ['s3:PutObject'],
          resources: [websiteBucket.arnForObjects('config.json')],
        }),
      ]),
    });
```

Une dernière chose avant de déployer à nouveau. Maintenant que nous avons une distribution CloudFront pour héberger notre application React, ajoutons un autre CfnOutput pour que nous puissions facilement obtenir l'URL de cette distribution.

```TypeScript
    new CfnOutput(this, 'DistributionDomain', {
      value: distribution.distributionDomainName,
    });
```

Maintenant, nous pouvons visiter l'URL de la distribution et voir notre application fonctionnelle ! Nous verrons nos notes existantes et pourrons en ajouter de nouvelles également !

![Note App](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-12-at-1.51.05-PM.png)

## Conclusion et prochaines étapes

Si vous êtes arrivé jusqu'ici et que votre application fonctionne, félicitations ! Vous pouvez souhaiter ajouter des fonctionnalités supplémentaires telles que la pagination, l'autorisation, ou permettre aux utilisateurs de mettre à jour ou de supprimer des notes. Lorsque vous avez terminé vos expériences, il est bon de suivre le conseil donné ci-dessus et d'exécuter `npx cdk delete` pour supprimer la pile et les ressources afin d'éviter des factures.

Nous avons couvert toutes les étapes nécessaires pour créer une application web à trois niveaux en utilisant AWS CDK. Vous voulez en savoir plus sur le CDK ? Rejoignez la communauté et le canal Slack sur [https://cdk.dev/](https://cdk.dev/) et consultez [https://thecdkbook.com/](https://thecdkbook.com/), écrit par des membres de la communauté CDK.

Vous aimez le TypeScript full-stack mais vous voulez affûter vos compétences ? Alors consultez mon livre [The TypeScript Workshop](https://www.amazon.com/gp/product/B093Y29GW3). Des questions ou des commentaires sur ce tutoriel, sur le CDK, ou sur TypeScript ? Trouvez-moi sur Twitter [https://twitter.com/NullishCoalesce](https://twitter.com/NullishCoalesce) ou sur [https://mattmorgan.cloud](https://mattmorgan.cloud).