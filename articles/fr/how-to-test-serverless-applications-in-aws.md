---
title: Comment tester les applications serverless dans AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-07T18:33:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-serverless-applications-in-aws
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/testing-serverless-apps.jpeg
tags:
- name: serverless
  slug: serverless
- name: Software Testing
  slug: software-testing
- name: Web Applications
  slug: web-applications
seo_title: Comment tester les applications serverless dans AWS
seo_desc: "By Ali Haydar\nOver the past few years, serverless architecture has become\
  \ very popular. This is largely because it has removed the burden of managing infrastructure,\
  \ such as servers, storage, databases, scalability, and so on. \nWhen people first\
  \ star..."
---

Par Ali Haydar

Au cours des dernières années, l'architecture serverless est devenue très populaire. Cela est principalement dû au fait qu'elle a supprimé le fardeau de la gestion de l'infrastructure, telle que les serveurs, le stockage, les bases de données, la scalabilité, et ainsi de suite. 

Lorsque les gens ont commencé à utiliser le terme "serverless", cela a créé une certaine confusion dans l'industrie. Certaines personnes se demandaient en plaisantant comment elles pouvaient exécuter des applications sans serveurs. 

Eh bien, les serveurs existent toujours, mais leur gestion et leur fonctionnement sont gérés en votre nom par le fournisseur de cloud.

L'utilisation de l'architecture serverless permet aux organisations et aux ingénieurs de se concentrer sur ce qui est important – construire des applications performantes, rentables et qui se démarquent sur le marché.

## Comment tester l'architecture serverless ?

Bien que le serverless ait introduit beaucoup de simplicité dans le processus de construction et de livraison de logiciels, certains défis peuvent intervenir autour des tests.

Tout d'abord, les tests locaux sont complexes car les applications serverless dépendent des services cloud. Cela est vrai pour les tests unitaires et d'intégration, où vous avez besoin de services de mocking et de stubbing pour vous assurer que l'application fonctionne correctement. 

Même si cela peut représenter un peu de travail supplémentaire, cela offre une meilleure façon de tester en isolation, et vos pipelines commenceront à échouer à cause de problèmes dans votre code, et non à cause des dépendances.

Deuxièmement, les tests d'intégration sont plus difficiles et importants car il y a plusieurs services/composants intégrés ensemble. Cela augmente le risque de créer des bugs de configuration/installation en plus des défauts de code potentiels existants.

Alors, que devons-nous tester ? Comment testons-nous notre application à la fois au niveau unitaire et au niveau de l'intégration ? 

Comment pouvons-nous nous assurer que notre application fonctionnera correctement dans un environnement en direct, étant donné que nous avons mocké d'autres services lors du développement en local ? 

Et comment pouvons-nous tester l'interaction avec les services cloud (les services AWS dans ce cas) sans avoir à tester le service lui-même ?

Cet article vise à répondre à ces questions pour vous aider à tester efficacement vos applications serverless. Alors, commençons.

## Que construisons-nous ?

AWS propose un ensemble de services serverless (services qui s'exécutent dans le cloud, sur du matériel et des systèmes que nous ne gérons pas). Cet article couvrira quelques-uns d'entre eux :

* Lambda (Fonction Cloud)
* API Gateway
* DynamoDB

Comme cet article se concentre principalement sur le test des applications serverless, nous utiliserons une application que j'ai précédemment développée comme exemple. Cette application retourne une liste de fausses entreprises cotées en bourse.

L'architecture ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/architecture.png)

N'hésitez pas à jeter un coup d'œil à l'[application de démonstration](https://companies-data-demo.s3.amazonaws.com/index.html) en cours d'exécution dans AWS (veuillez excuser la conception de l'interface utilisateur).

L'application dispose d'un front-end qui effectue des appels API REST au back-end. Ces appels passent par l'API Gateway vers Lambda, qui interroge DynamoDB pour les entreprises cotées en bourse et retourne le résultat.

Tout le code back-end se trouve dans le dossier `api`. Nous commencerons par examiner chaque composant en isolation, puis nous testerons l'intégration. Pour commencer, [clonez le dépôt ici](https://github.com/AHaydar/companies-data-demo).

Testons l'application.

## Tests unitaires de l'application

Comme je l'ai mentionné précédemment, nous avons trois composants sur notre back-end : DynamoDB, Lambda et API Gateway. Dans cette section, nous aborderons comment tester unitairement ces composants.

### Comment exécuter des tests unitaires sur DynamoDB

Le code d'infrastructure pour construire DynamoDB ressemble à ceci :

```

Resources:
  CompaniesTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: companies
      AttributeDefinitions:
        - AttributeName: CompanyId
          AttributeType: S
        - AttributeName: CompanyType
          AttributeType: S
      KeySchema:
        - AttributeName: CompanyId
          KeyType: HASH
        - AttributeName: CompanyType
          KeyType: RANGE
      ProvisionedThroughput:
        ReadCapacityUnits: 5
        WriteCapacityUnits: 5
      Tags:
        - Key: author
          Value: ali

  CompaniesTableReadOnlyAccessPolicy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      Description: Policy for Read only companies table
      ManagedPolicyName: companies-readonly-access
      Path: /
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Sid: CompaniesReadOnlyAccess
            Effect: Allow
            Action:
              - 'dynamodb:Scan'
              - 'dynamodb:GetItem'
              - 'dynamodb:Query'
            Resource:
              - !GetAtt CompaniesTable.Arn

```

En naviguant vers AWS CloudFormation et en téléchargeant le modèle, nous allons provisionner une table DynamoDB, principalement avec les champs "CompanyId" et "CompanyType" qui forment une clé primaire. Nous aurons également une politique IAM qui nous permet d'accéder à la table. 

Alors, y a-t-il quelque chose à tester ici ?

Le schéma DynamoDB est principalement défini en fonction des modèles d'accès. C'est ainsi que nous créons la clé primaire, décidons de la clé de hachage et de la clé de tri, et ainsi de suite. 

Par exemple, si un champ (ou une combinaison de champs) n'est pas une clé primaire, nous n'obtiendrons pas l'enregistrement à moins de définir un index secondaire sur ce champ. Nous devons donc prêter attention à nos cas d'utilisation métier lorsque nous testons la configuration de DynamoDB. 

Gardez à l'esprit que nous ne testons pas le fonctionnement de DynamoDB lui-même ici (AWS a fait un excellent travail là-bas). Plutôt, nous testons comment nous interagissons avec lui.

Il est possible de naviguer vers AWS, d'ajouter des éléments, puis de s'assurer qu'ils sont visibles et filtrables sur la console AWS. Est-ce suffisant ? Ce modèle d'accessibilité se produira de manière programmatique. Dans la vie réelle, la fonction Lambda (section suivante) essaiera d'accéder à la base de données.

J'écris généralement un petit script bash qui s'exécute après le provisionnement de la table et vérifie si les modèles d'accès fonctionnent correctement. Par exemple :

```
#!/bin/bash

# Insérer un enregistrement dans la table dynamoDB
aws dynamodb put-item \
 --table-name companies \
 --item '{
  "CompanyId": { "S": "COMPANY#4" },
  "CompanyType": { "S": "PRIVATE" },
  "Details": { "M": {
    "name": { "S": "Awesome Company" },
    "revenue": { "S": "1000000" }
    } }
  }' \
 --return-consumed-capacity TOTAL \
 --return-item-collection-metrics SIZE

 # Interroger l'enregistrement ajouté depuis la table
 RESULT=$(
 aws dynamodb get-item \
 --table-name companies \
 --key file://key.json \
 --return-consumed-capacity TOTAL
 )
 echo $RESULT
### OUTPUT ###
#  {
#   "Item": {
#     "Details": {
#       "M": { "name": { "S": "Kousa" }, "revenue": { "S": "1000000" } }
#     },
#     "CompanyType": { "S": "PRIVATE" },
#     "CompanyId": { "S": "COMPANY#4" }
#   },
#   "ConsumedCapacity": { "CapacityUnits": 0.5, "TableName": "companies" }
# }

# analyser le nom et vérifier qu'il est correct
NAME=$(jq -r '.Item.Details.M.name.S' <<< "$RESULT")
echo $NAME

if [ "$NAME" = "Awesome Company" ]; then
    echo 'The item was retrieved correctly.'
    exit 0
else
    echo 'Something went wrong. Double-check the schema or the query.'
    exit 1
fi


# Supprimer l'élément ajouté
aws dynamodb delete-item \
--table-name companies \
--key file://key.json

```

Il y a un peu de travail supplémentaire, cependant, en plus de l'écriture du script bash, y compris ce qui suit :

* Quand devons-nous exécuter le script ?
* Sera-t-il exécuté contre une base de données de test également ? Est-ce risqué ?
* Que se passe-t-il si la base de données est déjà utilisée (par exemple, nous avons ajouté un index à la table) ?
* L'exécution de ce script repose sur le fait d'avoir des identifiants AWS alimentés en tant que variables d'environnement – probablement qu'ils font déjà partie des pipelines CI/CD
* Cela a-t-il couvert le test de la politique IAM qui permet l'accès à la table ?

L'écriture de ce type de test est-elle précieuse ? C'est quelque chose à considérer au cas par cas. Principalement, nous devons peser les avantages de l'automatisation des tests de la configuration de l'infrastructure par rapport au temps que nous passons à développer et à maintenir ces tests. 

Par exemple, supposons que nous utilisions cette table à plusieurs fins dans plusieurs équipes. Dans ce cas, il pourrait être utile d'avoir le code d'infrastructure de la table et les tests vivre dans un dépôt séparé, où nous exécutons les tests avant toute modification de la table déployée en production. 

Nous ne voulons pas interrompre aucune fonctionnalité qui pourrait dépendre de cette table. Pour ne pas causer d'interruptions dans l'environnement de test ou endommager les données de la table à cause de nouvelles modifications, nous pouvons provisionner une table temporaire avec les modifications dans AWS, exécuter nos tests, et ne mettre à jour la base de données de test que si ces tests réussissent.

Pour résumer tout cela, notre pipeline CI/CD fait ce qui suit :

* Provisionner une nouvelle table temporaire sur l'environnement de test AWS (sans toucher la vraie base de données de test)
* Exécuter les tests bash sur la table temporaire
* En cas de succès, supprimer la table temporaire et mettre à jour la table de test réelle
* En cas d'échec, supprimer la table temporaire et arrêter les modifications ultérieures

### Comment exécuter des tests unitaires sur Lambda

En regardant le code original, il ne semble pas idéal car il inclut toute la logique dans le gestionnaire de la Lambda (c'est une grande fonction qui fait plusieurs choses) :

```
const { DynamoDB } = require('@aws-sdk/client-dynamodb'); // importing library from aws-sdk that allows the interaction with dynamodb
const { unmarshall } = require('@aws-sdk/util-dynamodb'); // importing unmarshall function, which converts a DynamoDB record into a JavaScript object

exports.lambdaHandler = async (event, context) => {
  try {
    console.log('here is the event received', event);
    const dynamodb = new DynamoDB({ region: 'us-east-1' }); // creating a new instance of DynamoDB
    const params = {
      TableName: 'companies',
    };

    // if no query parameter was passed to the function, then update the dynamodb params to query all companies
    if (!event.queryStringParameters) {
      params.ExpressionAttributeValues = {
        ':companyType': {
          S: 'PUBLIC',
        },
      };
      params.FilterExpression = 'CompanyType = :companyType';
    }
    // if the companyId query paramater was passed, then update the dynamodb params to filter according that company exactly
    else {
      params.ExpressionAttributeValues = {
        ':companyId': {
          S: `COMPANY#${event.queryStringParameters.companyId}`,
        },
      };
      params.FilterExpression = 'CompanyId = :companyId';
    }

    const results = await dynamodb.scan(params); // get the results from dynamodb according to the previously set params
    console.log('results', results);
    let unmarshalledResults = [];

    // unmarshall every record returned (convert it into a JS object)
    for (const item of results.Items) {
      const unmarshalledRecord = unmarshall(item);
      unmarshalledResults.push(unmarshalledRecord);
    }

    console.log('unmarshalled results', unmarshalledResults);

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify(unmarshalledResults),
    };
  } catch (e) {
    console.error('something went wrong', e);
    return {
      statusCode: 500,
      body: 'Something has gone wrong, please contact the support team',
    };
  }
};


```

Notez que l'utilisation de l'opération de scan sur DynamoDb nécessite une réflexion approfondie dans un environnement de production, car elle opère sur l'ensemble de la table. Cela pourrait causer des problèmes de performance ou consommer la capacité de lecture qui est réservée pour la table.

Alors, que fait ce code ?

Il serait bon de séparer les préoccupations pour une meilleure testabilité, donc nous allons créer une nouvelle fonction qui gère l'interaction avec DynamoDb et faire en sorte que le gestionnaire lambda l'appelle selon les besoins. 

Nous prenons donc la partie qui interroge DynamoDB et convertit les résultats en un objet JS. Le nouveau fichier et la nouvelle fonction ressemblent à ceci :

```
const { DynamoDB } = require('@aws-sdk/client-dynamodb');
const { unmarshall } = require('@aws-sdk/util-dynamodb');

const dynamodb = new DynamoDB({ region: 'us-east-1' });

const scanAndFilterData = async (params) => {
    const results = await dynamodb.scan(params);
    console.log('results', results);
    let unmarshalledResults = [];

    for (const item of results.Items) {
      const unmarshalledRecord = unmarshall(item);
      unmarshalledResults.push(unmarshalledRecord);
    }

    console.log('unmarshalled results', unmarshalledResults);
    return unmarshalledResults;
}

module.exports = { scanAndFilterData }

```

Le gestionnaire Lambda ne gérera que la réception de l'événement et le passera à la fonction qui interagit avec la base de données.

### Comment tester unitairement le code

Les tests unitaires de la fonction `scanAndFilterData` nécessitent de mocker les bibliothèques @aws-sdk que nous utilisons. Sinon, nous couvrirons également les bibliothèques elles-mêmes dans nos tests, et nous ne voulons pas cela. 

De plus, cela pourrait ajouter une certaine complexité autour de l'accès à la table DynamoDB, qui se fera automatiquement par la bibliothèque (par exemple, nous devrions gérer les identifiants dans le cadre des tests). Nous devons donc soit stubber DynamoDb, soit mocker les fonctions qui interagissent avec lui.

```
const { scanAndFilterData } = require('../dynamoDbData');

jest.mock('@aws-sdk/client-dynamodb', () => {
    return {
        DynamoDB: jest.fn().mockReturnValue({scan: jest.fn().mockReturnValue({Items: ['item1', 'item2']})})
    }
})

jest.mock('@aws-sdk/util-dynamodb', () => {
    return {
        unmarshall: jest.fn().mockReturnValue('test')
    }
})

describe('scanAndFilterData', () => {
    it('should scan the dynamoDB table and unmarchall the returned records', async () => {
        const mockedDynamoDBInstance = require('@aws-sdk/client-dynamodb').DynamoDB;
        const params = 'test'
        const result = await scanAndFilterData(params);
        expect(mockedDynamoDBInstance.mock.results[0].value.scan).toHaveBeenCalledWith(params);
        const mockedUnmarshall = require('@aws-sdk/util-dynamodb').unmarshall;
        expect(mockedUnmarshall).toHaveBeenNthCalledWith(1, 'item1');
        expect(mockedUnmarshall).toHaveBeenNthCalledWith(2, 'item2');

        expect(result).toEqual(['test','test']);

    })
})

```

Note de côté : remarquez que nous testons le code au lieu du comportement. Il m'a fallu un certain temps pour changer mon état d'esprit et voir les choses ainsi lorsque j'ai commencé à écrire des tests unitaires. 

Cela est différent des tests E2E, qui sont généralement plus axés sur le comportement. Basiquement, nous regardons chaque ligne de code et vérifions dans nos tests qu'elle est écrite correctement (par exemple, une fonction a été appelée). 

Mais nous pouvons encore mélanger les tests de code et de comportement. Nous pouvons décider du style de tests au cas par cas – j'ai souvent tendance à tester le code lorsqu'il a des dépendances et à tester le comportement lorsque la fonction est pure.

De manière similaire à la façon dont nous avons testé la fonction `scanAnFilterData`, nous devons tester la fonction du gestionnaire lambda. Les tests ressembleraient à ceci (notez que les tests ne sont pas complets mais suffisants pour donner l'idée) :

```
const { lambdaHandler } = require("../app");

jest.mock('../dynamoDbData', () => {
    return {
        scanAndFilterData: jest.fn()
    };
})

describe('lambda handler', () => {
    it('should only filter by compay type and return the result accordingly', async ()=> {
        const event = {}
        const result = await lambdaHandler(event);
        const mockedScanAndFilterData = require('../dynamoDbData').scanAndFilterData
        expect(mockedScanAndFilterData).toHaveBeenCalledWith({"ExpressionAttributeValues": {":companyType": {"S": "PUBLIC"}}, "FilterExpression": "CompanyType = :companyType", "TableName": "companies"});
    })
    it('should filter by passed company ID and return the result accordingly', async ()=> {
        const event = {queryStringParameters: {companyId: '1'}};
        const result = await lambdaHandler(event);
        const mockedScanAndFilterData = require('../dynamoDbData').scanAndFilterData
        expect(mockedScanAndFilterData).toHaveBeenCalledWith({"ExpressionAttributeValues": {":companyId": {"S": "COMPANY#1"}}, "FilterExpression": "CompanyId = :companyId", "TableName": "companies"});
    })
})


```

## Comment exécuter des tests d'intégration sur l'application

Nous avons sauté le test du composant API Gateway en isolation, car nous le couvrirons dans les tests d'intégration.

Nous diviserons les tests d'intégration en deux parties : les tests de flux complet et les tests d'intégration Lambda.

### Tests de flux complet

Les tests de flux complet sont des tests d'API qui couvrent l'API Gateway, la Lambda et la table DynamoDB.

Nous pouvons utiliser n'importe quel(s) outil(s) pour effectuer ces tests (comme Postman, une combinaison de Mocha/Chai/Cucumber, et ainsi de suite). Voici quelques scénarios :

* Obtenir toutes les entreprises publiques :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/get-all-companies.png)

* Obtenir les détails d'une seule entreprise publique :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/get-info-of-single-public-company.png)

* Obtenir les détails d'une seule entreprise privée :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/get-info-of-single-private-company.png)

Le dernier scénario montre un bug de sécurité, où l'utilisateur peut obtenir les informations d'une entreprise privée en sélectionnant un ID aléatoire dans le paramètre de chemin de la requête.

Opinion personnelle – Je préfère avoir les tests d'API construits dans le cadre du code plutôt que d'utiliser des outils externes tels que Postman. 

Postman offre une excellente utilité pour les tests d'API. Mais gérer les collections et les requêtes en dehors du même dépôt ou du contrôle de version n'est pas pratique pour la collaboration au sein d'une équipe et n'encouragerait pas les développeurs à écrire ce type de test.

Pour exécuter ces tests, nous devons avoir un environnement qui est correctement configuré et qui inclut les données nécessaires. Différentes équipes utiliseraient une variété d'approches pour créer les données :

* Avoir les données toujours disponibles dans l'environnement, en supposant que nous récupérons simplement des données.
* Avoir une API qui crée les données et une autre qui les supprime. Nous pourrions nous appuyer sur ces API pour préparer et nettoyer les données dans le cadre de nos tests. C'est mon approche préférée car elle supprime toute dépendance ou hypothèse sur les environnements et les données existants.

Je considère cet ensemble de tests comme des tests E2E, car ils couvrent la fonctionnalité et masquent toute intégration interne entre les trois composants de notre projet. 

Certaines personnes pourraient être en désaccord, car cela ne couvre pas le frontend de l'application que nous testons, ce qui est un bon point. 

Néanmoins, une autre approche consiste à ajouter quelques tests d'interface utilisateur en isolation, quelques tests de contrat, et à les combiner avec ces tests d'API pour couvrir la fonctionnalité de l'ensemble du système.

### Tests d'intégration Lambda

Cette section abordera le déploiement de Lambda et comment nous pouvons contrôler le trafic pour atteindre un déploiement plus sûr. Cela va de pair avec le test de l'intégration de Lambda avec d'autres services (DynamoDB dans ce cas).

Nous examinerons le basculement de trafic en utilisant le service "CodeDeploy", en nous appuyant sur les hooks "Before Traffic" et "After Traffic" de lambda. 

Ces hooks de trafic sont des fonctions lambda distinctes qui exécutent des vérifications de santé avant et après le basculement du trafic vers la nouvelle version de Lambda que nous avons implémentée. Cela aidera à éviter tout temps d'arrêt et toute interruption après le déploiement.

Les hooks nous permettent de décider si le déploiement doit réussir ou échouer. Les hooks pré-trafic nous permettent de tester la nouvelle Lambda déployée avant qu'elle ne soit utilisée (avant tout basculement de trafic). Un extrait de code ressemble à ceci :

```

exports.handler = (event, context, callback) => {

  const deploymentId = event.DeploymentId;
  const lifecycleEventHookExecutionId = event.LifecycleEventHookExecutionId;
  const functionToTest = process.env.NewVersion;

  // Create parameters to pass to the updated Lambda function that
  // include the newly added "time" option. If the function did not
  // update, then the "time" option is invalid and function returns
  // a statusCode of 400 indicating it failed.
  const lambdaParams = {
    FunctionName: functionToTest,
    InvocationType: "RequestResponse",
  };

  const lambdaResult = "Failed";
  lambda.invoke(lambdaParams, function (err, data) {
    if (err) {
      console.log(err, err.stack);
      lambdaResult = "Failed";
    } else {
      const result = JSON.parse(data.Payload);
      if (result.statusCode != "400") {
        console.log("Validation succeeded");
        lambdaResult = "Succeeded";
      } else {
        console.log("Validation failed");
      }

      var params = {
        deploymentId: deploymentId,
        lifecycleEventHookExecutionId: lifecycleEventHookExecutionId,
        status: lambdaResult, // status can be 'Succeeded' or 'Failed'
      };

      codedeploy.putLifecycleEventHookExecutionStatus(
        params,
        function (err, data) {
          if (err) {
            console.log("CodeDeploy Status update failed");
            console.log(err, err.stack);
            callback("CodeDeploy Status update failed");
          } else {
            console.log("CodeDeploy status updated successfully");
            callback(null, "CodeDeploy status updated successfully");
          }
        }
      );
    }
  });
};


```

Dans ce code, nous avons invoqué la fonction principale et mis à jour le statut à Failed si le code de statut est différent de 400. Ce n'est qu'un exemple – nous pourrions effectuer n'importe quelles vérifications dans ce cas, comme valider la réponse retournée par la base de données, et ainsi de suite. 

Une fois que nous obtenons la réponse dont nous avons besoin (ou non), nous informons CodeDeploy de mettre à jour le statut en utilisant `codedeploy.putLifecycleEventHookExecutionStatus`. Si le statut est un échec, alors "Code Deploy" arrête tout basculement de trafic futur et conserve la Lambda d'origine :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/code-deploy-traffic-shifting.png)

De même, dans le hook "After Traffic", nous pouvons effectuer les vérifications nécessaires après que le trafic a été redirigé vers la nouvelle version. J'utilise généralement les hooks After Traffic pour tester l'API en utilisant une bibliothèque telle que [axios](https://github.com/axios/axios), ce qui est très similaire à ce que nous avons testé dans Postman. Le code ressemble à ceci :

```
exports.handler = (event, context, callback) => {
  const deploymentId = event.DeploymentId;
  const lifecycleEventHookExecutionId = event.LifecycleEventHookExecutionId;
  let lambdaResult = "Failed";
  axios
    .get(
      "https://nfc079xjo3.execute-api.us-east-1.amazonaws.com/Prod/companies"
    )
    .then(function (response) {
      if (response.data.length == 2) {
        lambdaResult = "Succeeded";
      }
    })
    .catch(function (error) {
      console.log("An error occured", error);
    })
    .then(function () {
      const params = {
        deploymentId: deploymentId,
        lifecycleEventHookExecutionId: lifecycleEventHookExecutionId,
        status: lambdaResult, // status can be 'Succeeded' or 'Failed'
      };
      codedeploy.putLifecycleEventHookExecutionStatus(
        params,
        function (err, data) {
          if (err) {
            // Validation failed.
            console.log("AfterAllowTestTraffic validation tests failed");
            console.log(err, err.stack);
            callback("CodeDeploy Status update failed");
          } else {
            // Validation succeeded.
            console.log("AfterAllowTestTraffic validation tests succeeded");
            callback(null, "AfterAllowTestTraffic validation tests succeeded");
          }
        }
      );
    });
};

```

Cela sera-t-il suffisant pour remplacer les tests d'API ?

En cas d'échec dans le hook après, CodeDeploy reviendra à la version précédente de la Lambda.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/code-deploy-after-shifting-failure.png)

## Conclusion

Il est crucial de s'assurer que les applications que nous développons sont de haute qualité. Les tests sont l'un des moyens de confirmer cela. 

Selon la pyramide des tests, écrivez des tests autant que possible pour couvrir la base (tests unitaires), testez l'intégration, et enfin couvrez votre flux complet avec des tests E2E. 

Dans une application serverless, les tests restent les mêmes, avec quelques ajustements supplémentaires autour des tests d'intégration et du déploiement. Cette configuration permet le basculement de trafic et peut faire une différence significative pour garder vos clients satisfaits.

Vous pourriez encore vouloir tester votre application dans un environnement local. Il existe des outils tels que [localstack](https://github.com/localstack/localstack) qui aident à cela.

Comment testez-vous vos applications serverless ?

## Références

[https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/welcome.html](https://docs.aws.amazon.com/whitepapers/latest/serverless-architectures-lambda/welcome.html)

[https://www.serverless.com/framework/docs/providers/aws/guide/testing/](https://www.serverless.com/framework/docs/providers/aws/guide/testing/)

[https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html)

[https://blog.outwiththeold.info/posts/testable-lambda/](https://blog.outwiththeold.info/posts/testable-lambda/)