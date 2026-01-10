---
title: Comment déployer des API de manière sécurisée sur Amazon Lambda – Un guide
  pratique
subtitle: ''
author: Agnes Olorundare
co_authors: []
series: null
date: '2025-10-09T23:13:17.628Z'
originalURL: https://freecodecamp.org/news/how-to-securely-deploy-apis-to-amazon-lambda-a-practical-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760051580641/75d09121-6167-4e06-94d7-53cf23a6f6a1.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: Security
  slug: security
- name: APIs
  slug: apis
- name: API Gateway
  slug: api-gateway
- name: serverless
  slug: serverless
- name: secrets management
  slug: secrets-management
seo_title: Comment déployer des API de manière sécurisée sur Amazon Lambda – Un guide
  pratique
seo_desc: Cyber attacks against APIs (Application Programming Interfaces) are on the
  increase. These attacks arise from issues with proper authentication, authorization,
  unnecessary data exposure, lack of request limits, resource consumption, and use
  of vulner...
---

Les cyberattaques contre les API (Application Programming Interfaces) sont en augmentation. Ces attaques proviennent de problèmes liés à l'authentification, à l'autorisation, à l'exposition inutile de données, au manque de limites de requêtes, à la consommation de ressources et à l'utilisation d'API tierces vulnérables.

Des failles dans les API peuvent survenir avant que les requêtes n'atteignent les API, au sein du code hébergeant les API, et même le long du chemin de communication des API avec les services en aval, les dépendances ou d'autres microservices.

Les attaquants exploitent les failles des API pour accéder à des données confidentielles, collecter ou manipuler des données, ou même rendre votre service indisponible via des attaques par déni de service distribué (DDoS).

Dans cet article, vous apprendrez à déployer vos API dans Lambda et à appliquer certaines mesures de sécurité avant la fonction, au sein de la fonction et après la fonction.

## **Table des matières**

* [Qu'est-ce qu'une API ?](#heading-qu-est-ce-qu-une-api)
    
* [Prérequis](#heading-prerequis)
    
* [Objectif du projet](#heading-objectif-du-projet)
    
* [Architecture globale du projet](#heading-architecture-globale-du-projet)
    
    * [Configuration AWS](#heading-configuration-aws)
        
    * [Cloner le projet](#heading-cloner-le-projet)
        
    * [Configurer Simple Notification Service](#heading-configurer-simple-notification-service)
        
    * [Configurer Secrets Manager](#heading-configurer-secrets-manager)
        
    * [Configurer la Lambda interne](#heading-configurer-la-lambda-interne)
        
    * [Configurer la Lambda externe](#heading-configurer-la-lambda-externe)
        
    * [Configurer Web Application Firewall](#heading-configurer-web-application-firewall)
        
    * [Configurer les pools d'utilisateurs Cognito](#heading-configurer-les-pools-d-utilisateurs-cognito)
        
    * [Configurer API Gateway](#heading-configurer-api-gateway)
        
    * [Tester la configuration de bout en bout](#heading-tester-la-configuration-de-bout-en-bout)
        
    * [Nettoyage](#heading-nettoyage)
        
* [Améliorations](#heading-ameliorations)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'une API ?

L'accent de cet article est mis sur la sécurité des interfaces de programmation d'applications (API). Une API est une interface qui connecte deux programmes ou applications, leur permettant d'échanger des données et de communiquer.

Une API peut être interne à une organisation ou appartenir à un tiers qui permet à d'autres utilisateurs de consommer leurs données via l'API.

## Prérequis

Bien que ce tutoriel soit accessible aux débutants, vous aurez besoin des prérequis suivants pour le suivre sans encombre :

* Une connaissance de base du Cloud AWS.
    
* Un compte AWS avec un accès administrateur.
    
* AWS CLI. Vous pouvez trouver le guide d'installation [ici](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Suivez les instructions pour votre système d'exploitation.
    
* Python. Vous pouvez visiter le [site](https://www.python.org/downloads/) de documentation officielle de Python pour savoir comment télécharger et installer Python pour votre système d'exploitation spécifique.
    
* Pipenv ou tout outil de création d'environnement virtuel Python. Vous pouvez trouver le guide d'installation de Pipenv [ici](https://pypi.org/project/pipenv/).
    
* Une connaissance de base de Git.
    
* Un client API, comme Postman ou Thunderclient.
    

## Objectif du projet

À la fin de ce projet, vous devriez être capable de déployer des API dans Lambda de manière sécurisée, en tirant parti des services de sécurité natifs du cloud AWS.

## Architecture globale du projet

Voici l'architecture du flux de travail du projet :

![Diagramme architectural du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1758829544078/b76347ee-bbd3-41f4-88c8-2b3a89ad9087.png align="center")

Comme le montre le diagramme architectural, lorsqu'un utilisateur envoie une requête (un objet JSON composé du nom de l'utilisateur) à une API hébergée dans Lambda, l'utilisateur est d'abord authentifié par un service d'authentification appelé Amazon Cognito.

La requête passe par un Web Application Firewall, puis par une API Gateway. API Gateway effectuera une vérification pour voir si l'utilisateur est autorisé à accéder à l'API en utilisant le jeton (token) que l'utilisateur envoie avec la requête après l'authentification. API Gateway laisse ensuite passer le trafic vers l'API si l'utilisateur est autorisé.

La requête de l'utilisateur arrivera d'abord à une fonction Lambda externe, qui enregistrera ensuite le nom de l'utilisateur sous forme de message dans un sujet (topic) Simple Notification Service (SNS). Cela invoquera ensuite une Lambda interne pour s'exécuter et enregistrer la sortie dans les journaux Amazon CloudWatch. Le sujet SNS sera accédé par la Lambda externe à l'aide de l'identifiant unique du SNS stocké dans Amazon Secrets Manager.

### Configuration AWS

Vous devrez configurer un environnement AWS pour commencer. Cela nécessite la création d'un compte si vous n'en avez pas déjà un.

Après la création du compte, un utilisateur racine (root user) est automatiquement créé, avec tous les privilèges attachés. La meilleure pratique de sécurité consiste à créer un autre utilisateur avec des privilèges d'administrateur et à utiliser cet utilisateur pour les tâches suivantes.

Ensuite, créez une clé d'accès pour cet utilisateur, qui se compose généralement de deux parties (ID de clé d'accès et Clé d'accès secrète) en naviguant vers :

IAM —→ Users —→ Create Access key

Suivez les instructions et choisissez l'option `Command Line Interface`. Cochez la case `Confirmation` et procédez à la création de la clé. Téléchargez le fichier CSV fourni, ou copiez manuellement l' `Access Key ID` et la `Secret Access Key`. Enregistrez-les en toute sécurité.

![Tableau de bord IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1758890397608/a88ec1c6-511c-4a66-aa7a-d0dd3f41f665.png align="center")

![Page utilisateur IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1758890497481/faab2cb7-b7ba-4e5c-b67e-a00d8fb27a10.png align="center")

![Page de création de clé d'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1758890928429/1a4b3163-6340-47d2-be3e-0e61c275ba8f.png align="center")

![Page d'option d'utilisation de la clé d'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1758890991928/5bb150b6-b014-4398-b839-ee5d6e49c425.png align="center")

![Page de définition de tag de clé d'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1758891021874/a2e4eb61-eaca-4732-9377-b499fa7eab5d.png align="center")

![Téléchargement de la clé d'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1758891049362/372f3a63-8e64-478d-9b06-61f7aa88f73a.png align="center")

Ouvrez votre terminal et exécutez les commandes suivantes à l'aide de l'AWS CLI :

```bash
aws configure
```

La commande ci-dessus affichera des invites pour fournir les composants de la `Access Key` créée précédemment et votre région par défaut (la région AWS hébergeant le service avec lequel vous avez l'intention d'interagir).

### Cloner le projet

Dans l'étape suivante, vous clonerez le dépôt GitHub contenant les actifs et les ressources utilisés dans la mise en œuvre du projet.

Visitez l' [URL](https://github.com/Agnes4Him/secure-lambda) du projet et clonez le dépôt localement.

```bash
git clone <repository_clone_url>
```

### Configurer Simple Notification Service

Amazon Simple Notification Service (SNS) connecte les composants du système, permettant une communication et une messagerie asynchrones entre eux.

Recherchez `SNS` sur la console, cliquez dessus et créez un sujet (topic) auquel vos API enverront des messages. Après avoir créé avec succès un sujet, naviguez vers celui-ci, et dans les détails du sujet, vous trouverez l' `ARN` du sujet. Un ARN est un Amazon Resource Name, et c'est une chaîne unique attachée à une ressource que vous avez créée sur AWS pour aider à identifier la ressource. Copiez l' `ARN` du sujet.

![Tableau de bord SNS](https://cdn.hashnode.com/res/hashnode/image/upload/v1758983690093/a2820581-46fb-41d1-aed9-9471a0c2db02.png align="center")

![Créer un sujet SNS](https://cdn.hashnode.com/res/hashnode/image/upload/v1758982964553/3eb717c7-8ce3-497b-96fb-c16483cff43e.png align="center")

![Détails du sujet](https://cdn.hashnode.com/res/hashnode/image/upload/v1758983004729/854335ec-3d53-42e4-8bef-0e8a7d3fb2e6.png align="center")

![Politique d'accès au sujet SNS](https://cdn.hashnode.com/res/hashnode/image/upload/v1758983094356/320ebaf9-9f2d-4241-b747-fd3fd0f0b62b.png align="center")

![Sujet créé](https://cdn.hashnode.com/res/hashnode/image/upload/v1758983451385/7886c2c4-a52f-4538-8e9d-0d33738f7632.png align="center")

### Configurer Secrets Manager

Amazon Secrets Manager est utilisé pour stocker, gérer et récupérer des informations sensibles telles que des clés, des identifiants, des jetons, etc. Vous y stockerez l' `Topic ARN` créé précédemment. Avec cette approche, vous démontrerez comment votre API peut accéder en toute sécurité aux données et informations dont elle a besoin pour fonctionner.

Allez dans `Secrets Manager` sur la console AWS et créez un secret. Fournissez les détails du secret et ajoutez un nouveau secret nommé `TOPIC_ARN` comme clé et l'ARN réel du sujet SNS comme valeur.

![Console Secrets Manager](https://cdn.hashnode.com/res/hashnode/image/upload/v1758984342157/38c7855c-2221-4406-9078-496cbb480e47.png align="center")

![Créer un secret](https://cdn.hashnode.com/res/hashnode/image/upload/v1758984379959/3c4ebdf7-26c8-4b74-a175-0ea2eefd258d.png align="center")

![Choisir d'autres types de secret](https://cdn.hashnode.com/res/hashnode/image/upload/v1758984459477/cfdd8fce-4a33-45c3-8f12-d6a4a04bf799.png align="center")

![Détails du secret](https://cdn.hashnode.com/res/hashnode/image/upload/v1758984512368/7a76618e-18f6-4b3d-bc03-5941c89909ef.png align="center")

![Stockage final du secret](https://cdn.hashnode.com/res/hashnode/image/upload/v1758984575543/91ca9360-6320-442a-a121-37f9f35b175b.png align="center")

Ensuite, vous créerez des fonctions Lambda pour servir vos API et consommer la sortie des API. Il y a trois fonctions Lambda à configurer. Deux des fonctions hébergeront des API, chacune ne pouvant être accédée que par des utilisateurs spécifiques. Celles-ci seront appelées `ExternalLambda`. La troisième Lambda consommera la sortie des fonctions Lambda externes via SNS.

### Configurer la Lambda interne

AWS Lambda est un service serverless sur AWS que les utilisateurs peuvent exploiter pour exécuter des fonctions d'application ou du code en cas de besoin. Vous êtes facturé pour votre fonction Lambda en fonction du nombre d'invocations de la fonction, de la durée de chaque invocation et de la quantité de mémoire allouée à la fonction. Lambda peut être provisionné pour utiliser n'importe quel runtime, tel que Python ou NodeJS. Dans cette démonstration, nous nous concentrerons sur le runtime NodeJS.

Maintenant que vous savez ce qu'est Lambda et ce qu'il fait, vous pouvez en créer une. Appelons la première fonction Lambda InternalLambda. Sur la console AWS, recherchez `Lambda`, et sur le tableau de bord `Lambda`, cliquez sur `Create a function` et fournissez les détails. Nous utiliserons `Node.js` – JavaScript côté serveur comme runtime de choix.

![AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759140048151/60d5c813-a190-456e-9bad-50b429bdc6f7.png align="center")

![Détails Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759140165012/d519f8e9-cb98-4f75-b94e-d4d343e3003c.png align="center")

Pour les détails des `Permissions`, laissez Lambda créer un `IAM Role` par défaut. Ce rôle par défaut est nommé en fonction de votre fonction, et les permissions attachées au rôle permettent à votre fonction Lambda d'envoyer des journaux à CloudWatch, un autre service AWS utilisé pour la surveillance et l'observabilité.

![Permissions Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759140368576/3f922a46-7b3c-4034-b20b-c2b9ab5dde94.png align="center")

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1759146593382/39d50020-d0bf-4cfe-950f-eec8a2ff8989.png align="center")

Comme vous pouvez le voir dans la dernière image ci-dessus, la fonction Lambda que vous avez créée a besoin d'un déclencheur (`trigger`) et parfois d'une destination. Pour votre `InternalLambda`, le déclencheur est le sujet SNS que nous avons configuré précédemment. Cette Lambda lira les messages qui lui ont été publiés, puis vous pourrez accéder au message depuis votre client ou même les journaux CloudWatch.

Pour y parvenir, cliquez sur le bouton `Add trigger` et fournissez les détails.

![Ajouter SNS à Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759140925997/2534535f-5ad3-4e13-99f1-d8bf48c9cec1.png align="center")

![ARN SNS](https://cdn.hashnode.com/res/hashnode/image/upload/v1759146639798/1f3d75c9-ef5d-4538-9f3a-aaf2e8c0ddbb.png align="center")

![Aperçu InternalLambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759146670136/367f7ca9-0b41-41ed-8749-ff70e1770ebb.png align="center")

Ensuite, vous fournirez le `code` que vous souhaitez invoquer via Lambda. Trouvez le code dans le dépôt GitHub que vous avez cloné précédemment. Collez le code dans l'espace de code de la fonction Lambda et cliquez sur `Deploy` pour déployer la fonction.

`secure-lambda/InternalLambda/index.js`

```javascript
export const handler = async (event) => {
    try {
        console.log('Request successfully received from SNS');                            

        let name = event['Records'][0]['Sns']['Message'];
        let response = {
            statusCode: 200,
            body: JSON.stringify(`Hello ${name}. Greetings from InternalLambda!`),
        };       
        console.log('Response: ', response);                                                
        return response;
    } catch (err) {
        let response = {
            statusCode: 500,
            body: JSON.stringify('An error occurred while processing your request.'),
        };

        console.error('Error processing event', err);
        return response;
    }   
};
```

La fonction définie dans le fichier index.js ci-dessus prend simplement l'objet `event` qui lui est envoyé par SNS et en extrait l'attribut `Message`. Nous utilisons `console.log` ici pour visualiser les sorties de la fonction et nous assurer qu'elle se comporte comme prévu. Ne l'utilisez simplement pas dans une application prête pour la production.

![Code InternalLambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759142277747/f4437ff2-4495-485d-b891-d9dda3fc939c.png align="center")

### Configurer la Lambda externe

Vous allez créer deux fonctions Lambda externes : 1 et 2. Ces deux fonctions recevront les requêtes des utilisateurs, les traiteront et publieront des messages sur votre sujet SNS.

Sur la console Lambda, créez une autre fonction et nommez-la `ExternalLambda1`. Laissez Lambda créer un rôle IAM par défaut, comme précédemment.

![Créer ExternalLambda1](https://cdn.hashnode.com/res/hashnode/image/upload/v1759144966306/ee8a2ed1-5a2e-48df-8556-5dedd7ecdde1.png align="center")

![Aperçu ExternalLambda1](https://cdn.hashnode.com/res/hashnode/image/upload/v1759146732803/82a46fd1-e3e5-4d72-a9fe-b41496ba076b.png align="center")

Collez l'extrait de code ci-dessous dans l'espace de code `ExternalLambda1` :

`secure-lambda/ExternalLambda1/insex.js`

```javascript
import {
  GetSecretValueCommand,
  SecretsManagerClient,
} from "@aws-sdk/client-secrets-manager";

import { SNSClient, 
    PublishCommand 
} from "@aws-sdk/client-sns";

const secretsManagerClient = new SecretsManagerClient();

const snsClient = new SNSClient({});

// Fetch topicArn from AWS Secrets Manager
async function getSecretValue(secretName) {
    try {
        const data = await secretsManagerClient.send(
                            new GetSecretValueCommand({
                            SecretId: secretName,
                            }),
                        );
        if (data.SecretString) {
            return JSON.parse(data.SecretString);
        }   else {
            let buff = Buffer.from(data.SecretBinary, 'base64');
            return JSON.parse(buff.toString("utf-8"));
        }
    } catch (err) {
        console.error('Error retrieving secret', err);                             // added for debugging
        throw err;
    }
}                                        

export const handler = async (event) => {

    let name = event['name'];
    console.log(`Request successfully received from ${name}`);    
    
    // Retrieve SNS Topic ARN from Secrets Manager
    let topicArn;
    let response;
    try {
        const secret = await getSecretValue('LambdaSNSTopicARN');
        topicArn = secret.TOPIC_ARN;
    } catch (err) {
        response = {
            statusCode: 500,
            body: JSON.stringify('An error occured, try again later.'),
        };
        console.error('Failed to load SNS Topic ARN from Secrets Manager', err);
        return response;        
    }

    // Publish to SNS topic
   try {
        const snsResponse = await snsClient.send(
        new PublishCommand({
            Message: name,
            TopicArn: topicArn,
        })
        );
        console.log("Message published successfully:", snsResponse.MessageId);
        response = {
            statusCode: 200,
            body: JSON.stringify(`Hello ${name}. Greetings from ExternalLambda1! Message forwarded to InternalLambda.`),
        };
        return response;
  } catch (err) {
        response = {
            statusCode: 500,
            body: JSON.stringify(`Sorry ${name}.An error occurred while processing your request.`),
        };
        console.error("Failed to publish message:", err);
        return response;
  }  
};
```

Le code ci-dessus utilise le SDK AWS pour récupérer l'ARN du sujet SNS créé précédemment à partir de Secrets Manager. Il publie ensuite un message sur le sujet.

Le SDK est déjà installé dans la fonction Lambda. En dehors de Lambda, le SDK doit être explicitement installé. La fonction reçoit son `event` du client via API Gateway, que nous configurerons plus tard.

Le sujet SNS que vous avez créé précédemment sera la destination de cette fonction. Pour que Lambda puisse publier un sujet sur SNS, il a besoin de la permission nécessaire attachée à son rôle IAM. AWS peut s'en charger automatiquement lors de votre configuration, comme indiqué ci-dessous.

Pour le déclencheur, vous utiliserez un autre service connu sous le nom d' `API Gateway`. Plus d'informations à ce sujet plus tard.

![ExternalLambda1 Ajouter une destination](https://cdn.hashnode.com/res/hashnode/image/upload/v1759146816330/3c542eff-984e-4d02-85b3-c1da142f94d7.png align="center")

![ExternalLambda1 Permissions de destination](https://cdn.hashnode.com/res/hashnode/image/upload/v1759146778567/9b3650f1-90fd-47ce-99c3-627654f2d41f.png align="center")

Suivez les mêmes étapes pour provisionner une autre Lambda connue sous le nom d' `ExternalLambda2`.

![ExternalLambda2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759145915181/631aa639-493a-4f12-af1e-45f425ca2c16.png align="center")

Le résultat de la configuration de la Lambda externe est présenté ci-dessous :

![Aperçu ExternalLambda2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759146919917/93aaf281-387f-44c3-bf6d-995b076150e9.png align="center")

Collez le code ci-dessous dans `ExternalLambda2`. Il remplit la même fonction qu' `ExternalLambda1`, mais leur sortie diffère. Chacune des deux fonctions Lambda recevra du trafic pour un utilisateur spécifique autorisé à accéder à la fonction.

`secure-lambda/ExternalLambda2/index.js`

```javascript
import {
  GetSecretValueCommand,
  SecretsManagerClient,
} from "@aws-sdk/client-secrets-manager";

import { SNSClient, 
    PublishCommand 
} from "@aws-sdk/client-sns";

const secretsManagerClient = new SecretsManagerClient();

const snsClient = new SNSClient({});

// Fetch topicArn from AWS Secrets Manager
async function getSecretValue(secretName) {
    try {
        const data = await secretsManagerClient.send(
                            new GetSecretValueCommand({
                            SecretId: secretName,
                            }),
                        );
        if (data.SecretString) {
            return JSON.parse(data.SecretString);
        }   else {
            let buff = Buffer.from(data.SecretBinary, 'base64');
            return JSON.parse(buff.toString("utf-8"));
        }
    } catch (err) {
        console.error('Error retrieving secret', err);  
        throw err;
    }
}                                        

export const handler = async (event) => {

    let name = event['name'];
    console.log(`Request successfully received from ${name}`);    
    
    // Retrieve SNS Topic ARN from Secrets Manager
    let topicArn;
    let response;
    try {
        const secret = await getSecretValue('LambdaSNSTopicARN');
        topicArn = secret.TOPIC_ARN;
    } catch (err) {
        response = {
            statusCode: 500,
            body: JSON.stringify('An error occured, try again later.'),
        };
        console.error('Failed to load SNS Topic ARN from Secrets Manager', err);
        return response;        
    }

    // Publish to SNS topic
   try {
        const snsResponse = await snsClient.send(
        new PublishCommand({
            Message: name,
            TopicArn: topicArn,
        })
        );
        console.log("Message published successfully:", snsResponse.MessageId);
        response = {
            statusCode: 200,
            body: JSON.stringify(`Hello ${name}. Greetings from ExternalLambda2! Message forwarded to InternalLambda.`),
        };
        return response;
  } catch (err) {
        response = {
            statusCode: 500,
            body: JSON.stringify(`Sorry ${name}.An error occurred while processing your request.`),
        };
        console.error("Failed to publish message:", err);
        return response;
  }              
};
```

Avant de continuer, vous devez modifier les rôles IAM de la Lambda externe. Actuellement, les rôles IAM n'ont que les permissions d'écrire dans CloudWatch et SNS (ajoutées automatiquement). La Lambda externe a également besoin de la permission de récupérer l'ARN du sujet SNS créé précédemment.

L'idée ici est de montrer comment exploiter un gestionnaire de secrets, tel qu'AWS Secrets Manager, pour stocker des informations ou des données sensibles, tout en y accédant de manière sécurisée. Cette approche est plus sûre que de stocker l'ARN en tant que variable d'environnement au sein de Lambda.

Naviguez vers IAM et cliquez sur l'onglet `Policies` à gauche. Cela vous amène à une liste de politiques. Ensuite, cliquez sur `Create policy`.

![Politiques IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1759320098124/71bde9ad-c6d9-4c0d-8472-d56107708be2.png align="center")

Recherchez `secrets manager` dans l'éditeur de politique.

![Éditeur de politique](https://cdn.hashnode.com/res/hashnode/image/upload/v1759320163875/a040af9a-1e92-4aea-8c2e-5c029f60f54e.png align="center")

![Éditeur de politique 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759320923537/c3e8bb54-e78d-498c-9fec-7c7a5225b116.png align="center")

Sélectionnez les permissions dont Lambda a besoin pour accéder à Secrets Manager. Dans ce cas, ce serait `Read —> GetSecretValue`.

![Éditeur de politique - Spécifier les permissions](https://cdn.hashnode.com/res/hashnode/image/upload/v1759321060458/963c1876-dbcc-4d7d-a6fe-9f65281c1a26.png align="center")

Sélectionnez `Specific` pour les ressources, et cliquez sur `Add ARNs`. Sur l'onglet suivant, ajoutez les détails du secret Secrets Manager créé précédemment.

![Éditeur de politique - Sélectionner l'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1759321219657/f50fc354-a238-499c-9009-958bbc624299.png align="center")

L'ARN du secret sera renseigné ici.

![Éditeur de politique - Ajouter l'ARN Secrets Manager](https://cdn.hashnode.com/res/hashnode/image/upload/v1759321662642/356fb6bd-adc7-4663-a337-3cfaedb74b2d.png align="center")

Ensuite, donnez un nom à la politique et créez-la.

![Éditeur de politique - Créer la politique](https://cdn.hashnode.com/res/hashnode/image/upload/v1759321510186/fa5da448-293f-4d95-a3b5-651292a91a7f.png align="center")

![Politique nouvellement ajoutée](https://cdn.hashnode.com/res/hashnode/image/upload/v1759321721882/27807dda-8ea3-4489-bcab-d03efc201655.png align="center")

Ensuite, naviguez vers `Roles` et recherchez les rôles IAM attribués aux fonctions Lambda externes. Ceux-ci sont nommés en fonction de la Lambda.

![Rôles IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1759321748368/dfc73acb-622c-44f9-9cf8-be51b31e3fe9.png align="center")

![Rôles IAM Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759321856410/f1d4a13c-a568-4c9c-b14f-bb3d24b870f8.png align="center")

Cliquez sur `Add permissions` pour ajouter une nouvelle permission au rôle IAM sélectionné.

![Rôle ExternalLambda1](https://cdn.hashnode.com/res/hashnode/image/upload/v1759322020293/689715ef-7e8c-45cb-9473-010f5aa105fa.png align="center")

![Rôle ExternalLambda1 - Politique ajoutée](https://cdn.hashnode.com/res/hashnode/image/upload/v1759322453532/83996cca-7a05-48fb-8e31-d3fc679df7bc.png align="center")

![Rôle ExternalLambda2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759322498243/29a8fff5-af9a-4d4c-b3ff-3790b82b6339.png align="center")

![Rôle ExternalLambda2 - Politique ajoutée](https://cdn.hashnode.com/res/hashnode/image/upload/v1759322570298/ab28750d-eb99-40f3-bf48-936b63bba1f0.png align="center")

### Configurer Web Application Firewall

Un pare-feu est un système placé devant une application, une charge de travail, des API, etc., pour inspecter le trafic, le filtrer et soit autoriser, soit bloquer le trafic en fonction de certaines règles préconfigurées.

Pour ce projet, vous utiliserez le service AWS Web Application Firewall (WAF) pour inspecter les requêtes des utilisateurs avant d'acheminer le trafic vers vos API s'exécutant dans Lambda.

Rendez-vous sur la console AWS et recherchez WAF.

![AWS Web Application Firewall](https://cdn.hashnode.com/res/hashnode/image/upload/v1759310730367/bbcbdf00-2759-4dd7-9b7b-63ee9c252542.png align="center")

Cliquez sur l'onglet `IP sets` à gauche. Cela vous permettra de créer une liste d'adresses IP que vous souhaitez autoriser (comme dans ce cas) ou refuser.

![Page IP Sets](https://cdn.hashnode.com/res/hashnode/image/upload/v1759311298551/4537577d-a574-417e-8352-3f72b3732926.png align="center")

![Configuration IP Set](https://cdn.hashnode.com/res/hashnode/image/upload/v1759311354043/edd29c9c-63e7-4bf6-a503-23ef0af5ac20.png align="center")

Les adresses IP doivent inclure un bloc CIDR. Par exemple, si vous ajoutez une seule adresse IP, elle doit être `X.X.X.X/32`. Il en va de même pour les plages d'adresses IP telles que `X.X.X.X/24`.

![Aperçu IP Set](https://cdn.hashnode.com/res/hashnode/image/upload/v1759311560565/0ad16e51-b70b-4a80-98f4-821659fa61b8.png align="center")

Ensuite, cliquez sur l'onglet `Web ACLs`, puis sur `Create web ACL`.

![Page Web ACL](https://cdn.hashnode.com/res/hashnode/image/upload/v1759311623780/9742ab87-3303-4046-84df-f9f770ed7c41.png align="center")

Choisissez `Regional resources` comme type de ressource, et entrez votre région. Il est préférable de conserver toutes les ressources que vous créez dans ce projet dans la même région. Donnez un nom à votre Web ACL, puis cliquez sur suivant.

![Description Web ACL](https://cdn.hashnode.com/res/hashnode/image/upload/v1759311736091/b4201885-2dc0-4ed8-aa38-5e25824c363b.png align="center")

Ajoutez des règles à la Web ACL.

![Règle WAF](https://cdn.hashnode.com/res/hashnode/image/upload/v1759311892739/5efad662-6c20-4678-b490-54fa33bc3a7b.png align="center")

![Ajouter une règle](https://cdn.hashnode.com/res/hashnode/image/upload/v1759311985197/9e7157c8-bfb4-47a9-a850-67ce8bb302b2.png align="center")

Choisissez un type de règle. Dans ce cas, vous utiliserez `IP set`, et donnerez un nom à la règle. Choisissez l'IP set créé précédemment.

Sélectionnez `Source IP address`, et `Count` comme action. Pour ce projet, vous vous concentrerez sur le comptage des requêtes envoyées à vos API. Mais comme le montre l'image ci-dessous, vous pouvez effectuer d'autres actions, telles qu'autoriser, bloquer, etc.

![Configuration de règle WAF](https://cdn.hashnode.com/res/hashnode/image/upload/v1759312925911/ea491527-970c-4b5f-b658-4345ce3d08e4.png align="center")

Votre configuration de règle finale apparaîtra de cette façon.

![Aperçu de règle WAF](https://cdn.hashnode.com/res/hashnode/image/upload/v1759313133810/8e1be6d3-f6bf-42d9-881d-87216862b3bd.png align="center")

Faites défiler vers le bas, puis cliquez sur `Create web ACL`.

![Créer une règle](https://cdn.hashnode.com/res/hashnode/image/upload/v1759313210947/d625c4f3-a5a3-47c9-961f-ca67f652c992.png align="center")

![Tableau de bord Web ACL](https://cdn.hashnode.com/res/hashnode/image/upload/v1759313261493/3bd16ec5-3376-4607-86cc-fd1716ad68aa.png align="center")

### Configurer les pools d'utilisateurs Cognito

Amazon Cognito est un service de gestion d'identité utilisé pour créer et gérer des utilisateurs. Vous pouvez l'exploiter pour authentifier et autoriser les utilisateurs à accéder à des applications, des API ou d'autres charges de travail.

Vous créerez des `User Pools` (pools d'utilisateurs) au sein de Cognito et ajouterez un utilisateur à chaque pool. Vous configurerez la manière dont ces utilisateurs peuvent être authentifiés et autorisés à accéder aux fonctions Lambda externes déjà créées.

Recherchez `Cognito` sur AWS.

![Amazon Cognito](https://cdn.hashnode.com/res/hashnode/image/upload/v1759315681568/c2e7df4e-0e51-4c03-bf59-41ca895df74d.png align="center")

Cliquez sur `Get started for free`, puis sur `Create user pool`.

![Créer un pool d'utilisateurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1759315735324/1c09e934-186f-49db-811f-dd84d7400285.png align="center")

Sélectionnez Single-page application (SPA), donnez au pool d'utilisateurs le nom `MyUserPool1`, et sélectionnez `Email` comme option de connexion. Cela signifie que l'attribut principal que les utilisateurs fourniront lors de l'inscription et de la connexion sera leur adresse e-mail. Laissez tout le reste par défaut. Nous garderons les choses aussi simples que possible.

![Configuration du pool d'utilisateurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1759315828576/73cb66a3-cbde-4443-8dfd-34338091aabc.png align="center")

![Configuration du pool d'utilisateurs 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759315901551/9fdc173d-f92b-4080-98d4-513b404a9aeb.png align="center")

![Configuration du pool d'utilisateurs 3](https://cdn.hashnode.com/res/hashnode/image/upload/v1759315994247/3fb17ade-90aa-4d47-b2f9-258f6b547a1f.png align="center")

Après avoir créé le pool d'utilisateurs, vous trouverez la page ci-dessous. Vous pouvez afficher la page de connexion et d'inscription pour le pool que vous venez de créer en cliquant sur le bouton `View login page`.

![URL de connexion du client d'application Cognito](https://cdn.hashnode.com/res/hashnode/image/upload/v1759316208497/4db5f370-deb2-449e-8017-505dc1e13079.png align="center")

Vous pouvez ajouter des `App clients` à votre pool d'utilisateurs. Par défaut, un client nommé `MyUserPool1` sera ajouté au pool. Naviguez vers votre pool d'utilisateurs et cliquez sur `App clients` pour voir les détails de ce client. Notez le `Client ID`. Vous apporterez également quelques modifications au client d'application en cliquant sur le bouton `Edit`.

![Aperçu du client d'application du pool d'utilisateurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1759316443170/58081c40-cdcb-4af9-a60b-79156f6d2d68.png align="center")

Vous modifierez le champ `Authentication flows` en cochant les cases `Sign in with username and password…` et `Sign in with server-side administrative credentials…`. Ces modifications vous permettront d'authentifier l'utilisateur qui sera ajouté à ce client par programmation, plutôt que via une interface utilisateur. Avec cette approche, nous pouvons récupérer le jeton attribué à l'utilisateur par Cognito et utiliser ce jeton pour autoriser l'accès à Lambda.

![Modifier le client d'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1759317429341/f8db3816-c603-49fe-b661-696bfff98639.png align="center")

Maintenant, ajoutez un utilisateur à ce pool. L'utilisateur a besoin d'une adresse e-mail valide. Vous aurez besoin de l'URL de la page de connexion pour créer l'utilisateur.

![Cognito Créer un nouvel utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1759318555729/d9a8ac0c-72d4-4fca-8a94-ff71a5a20caf.png align="center")

Vous devez avoir accès à l'e-mail utilisé pour créer l'utilisateur. Récupérez le code envoyé à l'adresse e-mail et soumettez-le pour confirmer le compte.

![Cognito Confirmer l'e-mail](https://cdn.hashnode.com/res/hashnode/image/upload/v1759318672240/42d4418d-a4e1-4af9-b8b5-deaf5fb63118.png align="center")

![Inscription réussie Cognito](https://cdn.hashnode.com/res/hashnode/image/upload/v1759318710760/4505260f-13c9-4b3b-af99-1cb9e7436147.png align="center")

![Utilisateurs du pool d'utilisateurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1759318734000/1b3789d9-917a-4341-84ef-b8e498628557.png align="center")

Suivez les mêmes étapes et créez un autre pool d'utilisateurs nommé `MyUserPool2`. Ajoutez un utilisateur avec un e-mail différent à ce pool.

### Configurer API Gateway

API Gateway est un service utilisé pour gérer l'accès et acheminer le trafic vers les services backend d'API tels que les API. Il sert de proxy inverse et fournit une couche de sécurité supplémentaire pour les services backend.

Vous configurerez API Gateway pour diriger le trafic vers vos fonctions Lambda.

Naviguez vers `API Gateway` et cliquez sur `Create an API`.

![API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759336384538/0e2e4120-ade3-43c3-8a3e-9ec4d0e2b343.png align="center")

Sélectionnez l'option `REST API` —→ `Build`.

![Sélectionner le type d'API](https://cdn.hashnode.com/res/hashnode/image/upload/v1759336533762/56d96fcb-ff27-4f96-b739-fc9658dca50e.png align="center")

Sélectionnez `New API`, fournissez un nom et choisissez `Regional` comme type de point de terminaison (endpoint) d'API. Le type d'adresse IP peut être IPv4 ou Dualstack. Nous sélectionnerons IPv4 ici. Puis créez.

![Configuration API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759336585590/ff2b11c2-cb32-4657-913e-6dfc9922531f.png align="center")

Une partie importante de la configuration d'API Gateway pour ce projet est l'Authorizer. API Gateway utilise l'Authorizer pour autoriser le trafic des clients vers les services backend.

Vous créerez deux Authorizers. Chacun sera connecté à l'un des pools d'utilisateurs que vous avez configurés précédemment. Sur le côté gauche de l'API Gateway que vous avez configurée, cliquez sur `Authorizers` —→ `Create authorizer`.

![Authorizer API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759336744757/bb00a260-3897-4867-96d3-5370e40eae59.png align="center")

Fournissez le nom `AGAuthorizer1`, et sélectionnez `Cognito` comme type d'Authorizer. Ajoutez le pool d'utilisateurs pour MyUserPool1 créé précédemment. Pour la source du jeton (Token source), utilisez `Authorization`. Lorsque vous envoyez une requête depuis votre client API, un jeton sera ajouté à l'en-tête de la requête pour l'autorisation. La clé du jeton sera nommée `Authorization`, tandis que la valeur sera le jeton lui-même.

![Configuration Authorizer1](https://cdn.hashnode.com/res/hashnode/image/upload/v1759337066816/1ef4b11c-3508-49a5-ae7b-561b4c7f4259.png align="center")

Créez une autre autorisation pour MyUserPool2 de la même manière.

![Configuration Authorizer2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759337472200/aacad54f-8927-4c3e-9a60-f207bbf45577.png align="center")

Les deux Authorizers apparaîtront de cette façon.

![Aperçu des Authorizers](https://cdn.hashnode.com/res/hashnode/image/upload/v1759337540381/56362d9c-7f84-4021-b077-59992abd979b.png align="center")

Ensuite, vous créerez des ressources et des points de terminaison au sein de l'API Gateway que vous avez définie.

Une `resource` dans API Gateway est utilisée pour regrouper certains points de terminaison dans un chemin spécifique. Vous définirez deux ressources au sein de l'API Gateway que vous avez créée. Cela créera deux chemins différents, <BASE_URL>/<RESOURCE1> et <BASE_URL/RESOURCE2>.

Sur le tableau de bord API Gateway, naviguez vers votre Gateway, cliquez sur `Create resource`, définissez votre chemin racine ('/' dans votre cas), et fournissez le nom de la ressource (`lambda1`).

![Ressource lambda1 API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759420480646/c6e7c1c9-9eee-4dbf-af5b-8c335e14927c.png align="center")

Créez une autre ressource nommée `lambda2`.

![Aperçu des ressources API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759420822042/74d1790e-c752-490c-883f-b42bd00d91eb.png align="center")

Maintenant, cliquez sur `/lambda1`, puis sur `Create method` pour définir un point de terminaison au sein de cette ressource. Vous utiliserez la méthode `POST` pour envoyer des requêtes au service backend via ce point de terminaison.

![Configuration de méthode API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759420769955/bd861a6a-884d-4873-aaeb-dc958a0915b1.png align="center")

Pour le service backend ou le type d'intégration, sélectionnez Lambda function, et fournissez l'ARN d'ExternalLambda1.

![Configuration de méthode API Gateway 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759421208532/8d84c272-58ad-4ca4-ae56-682151495b76.png align="center")

Pour l'autorisation, sélectionnez `AWS IAM —→ Cognito user pool authorizers —→ AGAuthorizer1`. Laissez les autres configurations, puis créez le point de terminaison.

![Configuration de méthode API Gateway 3](https://cdn.hashnode.com/res/hashnode/image/upload/v1759421234684/1e76c46e-ba07-4178-94b3-e579ed752278.png align="center")

Répétez la même étape pour créer une méthode `POST` pour la ressource `/lambda2`. La `method` doit être attachée à `ExternalLambda2` et `AGAuthorizer2`.

![Déploiement API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759421691530/563c85e5-52ff-43fa-8216-41fc269989e0.png align="center")

L'API Gateway que vous avez créée doit être déployée pour devenir accessible. Le déploiement se fait généralement vers une étape (Stage).

Cliquez sur `Deploy API`, sélectionnez New stage et nommez l'étape development. Puis, déployez.

![Étape API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759421954217/f0ca31c8-78d9-4b1b-a47c-424f6ef32093.png align="center")

Après le déploiement vers une étape, une URL d'invocation sera fournie. Elle servira d'URL de base pour les points de terminaison que vous avez définis.

![Aperçu de l'étape API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759422031311/c7cac4e7-52e9-43dd-a565-46aa062aa364.png align="center")

L'étape que vous avez créée nécessite quelques modifications pour une sécurité accrue. Premièrement, vous devez attacher le `WAF` que vous avez créé précédemment. Deuxièmement, la limite de débit (rate limit) par défaut pour l'API déployée sur cette étape est de 10000. La limite de débit restreint la consommation excessive de ressources et protège votre API contre les abus. Pour ce projet, vous pouvez réduire la limite à 50.

![Modifier l'étape API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759422132101/b0f67d30-30ec-4d1f-9eee-735dc3b26500.png align="center")

![Étape API Gateway - Ajouter une limite de débit et WAF](https://cdn.hashnode.com/res/hashnode/image/upload/v1759423441047/95dc8f74-c71d-449a-b15a-46caa53c7595.png align="center")

Pour tester la configuration d'API Gateway, cliquez sur le point de terminaison que vous souhaitez tester, puis sur le bouton `Test`. Ce test initial ne nécessite aucune autorisation, car le test est effectué directement au sein de la Gateway.

![Test de point de terminaison API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759435394293/8933349c-3e2a-4795-adb4-bb9eeb990e81.png align="center")

Ajoutez des données JSON comme corps de la requête (Request body). La clé sera `name`, et la valeur sera n'importe quelle chaîne de caractères.

![Test API Gateway 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759435424778/a613816e-8b89-4978-9b3e-6734e48119eb.png align="center")

La réponse renvoyée par ExternalLambda1 affiche un code d'état 200 et un corps de réponse contenant exactement le message attendu de la fonction Lambda.

![Réponse de test API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1759435744694/516bab58-99de-4b41-8926-e9928b8c42e4.png align="center")

Si vous vous rendez dans les groupes de journaux CloudWatch (Log groups), vous devriez également trouver les groupes de journaux qui ont été automatiquement créés pour les fonctions Lambda. Cliquez sur le groupe de journaux pour ExternalLambda1 et naviguez vers le flux de journaux (Log stream) le plus récent. Vous devriez trouver les journaux de la requête que vous venez de faire depuis API Gateway.

![Journaux CloudWatch pour le test](https://cdn.hashnode.com/res/hashnode/image/upload/v1759435884121/05741f0c-82dd-43f1-855c-157df5c112fc.png align="center")

![Journaux CloudWatch pour le test 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759436073425/d4a0a2c7-8d86-44ce-adb7-4c67c3cdf40b.png align="center")

![Journaux CloudWatch - Sortie d'InternalLambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1759436150374/5fae1a11-c80d-41df-8ea9-39303287144b.png align="center")

### Tester la configuration de bout en bout

Pour tester correctement notre configuration, et depuis Internet, envoyez la même requête depuis votre client API sans aucune information supplémentaire dans l'en-tête de la requête. Cela devrait renvoyer une erreur `401` – Unauthorized. C'est le comportement attendu.

![Requête sans jeton](https://cdn.hashnode.com/res/hashnode/image/upload/v1759436452961/342e7659-5a58-45a2-af26-a657b622a83a.png align="center")

API Gateway attend un jeton d'autorisation pour chaque requête qu'elle reçoit avant d'acheminer le trafic vers le service backend approprié. Elle valide ce jeton via Cognito.

Vous allez simuler une connexion utilisateur pour chaque utilisateur ajouté aux pools d'utilisateurs Cognito afin d'obtenir un jeton pour l'utilisateur. Pour y parvenir, vous utiliserez les deux scripts Python que j'ai fournis ci-dessous :

`secure-lambda/auth-scripts/user1.py`

```python
import boto3

client = boto3.client("cognito-idp")

response = client.initiate_auth(
    AuthFlow="USER_PASSWORD_AUTH",  # or ADMIN_USER_PASSWORD_AUTH if using admin creds
    AuthParameters={
        "USERNAME": "",             # user1 email
        "PASSWORD": ""              # user1 password
    },
    ClientId=""                     # Cognito App Client ID
)

id_token = response["AuthenticationResult"]["IdToken"]
access_token = response["AuthenticationResult"]["AccessToken"]
refresh_token = response["AuthenticationResult"]["RefreshToken"]

print("ID Token:", id_token)
```

En utilisant la bibliothèque Python boto3, vous initierez une requête d'authentification auprès de Cognito. Fournissez l'adresse e-mail et le mot de passe de l'utilisateur dans MyUserPool1. Ajoutez également l'ID client du client d'application.

Pour exécuter le script, créez un environnement isolé à l'aide de Pipenv, uv ou d'une bibliothèque similaire. Installez la dépendance utilisée dans le projet comme défini dans le Pipfile, et exécutez le script avec le shell Pipenv.

```bash
pipenv install
pipenv shell
Python secure-lambda/auth-scripts/user1.py
```

La commande Python renverra un jeton attribué à l'utilisateur. Ensuite, vous utilisez ce jeton pour autoriser un utilisateur à accéder à ExternalLambda1.

![Ajouter un jeton à l'en-tête de la requête](https://cdn.hashnode.com/res/hashnode/image/upload/v1759437804885/f03ab150-74f9-4ecf-9c7c-0ee07e8662a2.png align="center")

Assurez-vous que l'URL de la requête POST est au format : <BASE_URL/lambda1>. Vous devriez recevoir une réponse d'API Gateway indiquant le succès.

Maintenant, essayez d'accéder à ExternalLambda2 en utilisant le jeton de User1. Vous devriez recevoir un message `Unauthorized`. Notez que user1 recevra toujours un message non autorisé lorsqu'il tente d'accéder à ExternalLambda1 sans jeton d'autorisation dans l'en-tête, avec un mauvais jeton, ou lorsqu'il tente d'accéder à ExternalLambda2, pour lequel il n'est pas autorisé.

![User1 accède à ExternalLambda2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438020972/39e2650a-6a99-466a-ad40-6bcf72c491c4.png align="center")

Répétez le processus avec User2 en utilisant le jeton généré pour l'utilisateur dans MyUserPool2. Tout d'abord, testez l'accès à ExternalLambda2 sans jeton dans l'en-tête de la requête.

![Requête User2 sans jeton](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438058029/37dbffcb-7f58-4ce0-abfa-abf0e6d1d3a4.png align="center")

Puis testez l'accès avec le jeton.

![Requête User2 avec jeton](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438118097/a408bfe0-6e94-46a1-b98e-c959f31673f8.png align="center")

Ensuite, essayez d'accéder à ExternalLambda1 en utilisant User2.

![User2 accède à ExternalLambda1](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438144636/06ba905d-ff7b-48d6-8e5b-e35b959221ba.png align="center")

Vous pouvez également visualiser le résultat de certaines des requêtes effectuées par votre client sur les journaux CloudWatch.

![Sortie des journaux CloudWatch](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438188476/2e5aaa35-b52c-4fd3-88f4-00bc704cd809.png align="center")

![Sortie des journaux CloudWatch 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438223720/630bd443-41d2-40b7-b28f-ff937fbf13f9.png align="center")

De plus, puisque WAF a été configuré précédemment pour compter les requêtes (bien que, dans un scénario réel, vous souhaitiez accomplir bien plus avec WAF, comme autoriser ou bloquer certains trafics), vous pouvez visualiser les activités capturées par WAF en naviguant vers le service sur AWS, puis en recherchant le WAF que vous avez configuré, et en naviguant vers Traffic overview.

![WAF - Détails du trafic](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438469300/df718ef7-7eaa-49ad-8780-c43878d2d388.png align="center")

![WAF - Détails du trafic 2](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438498828/b1619abf-db45-4946-85e2-53e5a769cdb8.png align="center")

Vous pouvez trouver d'autres détails, tels que les types d'appareils clients et l'origine des requêtes.

![WAF - Détails du trafic 3](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438552359/477c4f39-04e4-4427-a2d2-74a6066622dd.png align="center")

![WAF - Détails du trafic 4](https://cdn.hashnode.com/res/hashnode/image/upload/v1759438590513/31acecd0-7f45-4fb9-b352-5dc5fcf49e75.png align="center")

### Nettoyage

Il est important de nettoyer les ressources créées jusqu'à présent après l'exercice pratique. En raison des dépendances entre les ressources, essayer de supprimer une ressource dont dépend une autre ressource peut entraîner une erreur. Vous devez donc les supprimer dans cet ordre :

* Secrets Manager
    
* Cognito – Utilisateurs, Client d'application, puis Pool d'utilisateurs
    
* API Gateway – Points de terminaison/ Méthodes, Ressources, API, Étape
    
* Web Application Firewall – IP Set, Web ACL
    
* Toutes les fonctions Lambda
    
* Rôles IAM Lambda et les politiques qui leur sont attachées
    
* Groupe de journaux CloudWatch pour toutes les fonctions Lambda
    
* Sujet SNS
    

De plus, vous pouvez désactiver ou supprimer les identifiants créés pour votre utilisateur IAM Admin s'ils ne sont pas utilisés.

## Améliorations

Considérez les domaines suivants pour améliorer, appliquer les meilleures pratiques et renforcer davantage la posture de sécurité de vos systèmes.

1. Utilisation de clés d'API
    
2. Consommation d'API tierces
    
3. Gestion de l'inventaire des API / documentation
    
4. Provisionnement des ressources à l'aide de l'Infrastructure as Code
    

## Conclusion

La sécurité à chaque couche d'un système informatique n'est pas négociable. Dans ce projet, nous avons démontré comment exploiter des solutions natives du cloud pour sécuriser des API hébergées dans un service serverless, en n'autorisant l'accès aux API qu'aux utilisateurs autorisés.

Je suis Agnes Olorundare, et vous pouvez en savoir plus sur moi sur [**LinkedIn**](https://www.linkedin.com/in/agnes-olorundare-446055b8/).