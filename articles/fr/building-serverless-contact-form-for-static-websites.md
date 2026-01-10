---
title: Création d'un formulaire de contact Serverless pour les sites web statiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T18:55:10.000Z'
originalURL: https://freecodecamp.org/news/building-serverless-contact-form-for-static-websites
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_lYvXrG9rcgLg42weUyOfyg.jpeg
tags:
- name: Python
  slug: python
- name: serverless
  slug: serverless
- name: serverless framework
  slug: serverless-framework
seo_title: Création d'un formulaire de contact Serverless pour les sites web statiques
seo_desc: 'By Faizan Bashir


  Photo by Unsplash

  Introduction

  A few years ago AWS launched static hosting service S3, which was a paradigm shift
  for hosting static websites. The tech was crystal clear, all the static assets (HTML,
  CSS, and JS) would reside in an ...'
---

Par Faizan Bashir

![Image](https://cdn-media-1.freecodecamp.org/images/1*lYvXrG9rcgLg42weUyOfyg.jpeg align="left")

*Photo par* [*Unsplash*](https://unsplash.com/photos/AtvuPUenaeI?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

### Introduction

Il y a quelques années, AWS a lancé le service d'hébergement statique S3, qui a marqué un changement de paradigme pour l'hébergement de sites web statiques. La technologie était claire : tous les actifs statiques (HTML, CSS et JS) résideraient dans un bucket S3 pour héberger votre site web impressionnant. Une idée plutôt cool que j'ai personnellement appréciée, vraiment. Sans ce formulaire de contact super important, l'hébergement sur S3 aurait été cool, mais votre formulaire de contact serait une blague à moins d'avoir un autre serveur en place pour traiter les requêtes AJAX de ce formulaire. Le moment où vous aviez ce service prêt, la solution S3 n'aurait plus l'air si attractive.

À l'ère de la technologie de pointe, il y a toujours des innovations à couper le souffle au coin de la rue. L'une des innovations technologiques impressionnantes est le serverless. Ce n'est pas qu'il n'y a pas de serveurs impliqués, mais vous pouvez vous en soucier moins maintenant. Le serverless peut être une solution appropriée et viable à de nombreux problèmes, c'est la solution la plus parfaite pour votre formulaire de contact hébergé de manière statique. Continuez à lire, à la fin de cet article, vous serez en mesure de gérer les formulaires de votre site web de la manière la plus économique et la plus simple possible.

---

### Le Framework Serverless

![Image](https://cdn-media-1.freecodecamp.org/images/1*oDBqXrshDx-kEVUg1e6Rhw.png align="left")

*Source :* [*https://serverless.com/*](https://serverless.com/)

> *Serverless est votre boîte à outils pour déployer et exploiter des architectures serverless. Concentrez-vous sur votre application, pas sur votre infrastructure.*  
>   
> ** [*Serverless.com*](https://serverless.com/)

Le couteau suisse des technologies Serverless. Le Serverless Framework est un framework web gratuit et open-source écrit en Node.js. Serverless a été le premier framework développé pour construire des applications exclusivement sur AWS Lambda, la plateforme de calcul serverless fournie par Amazon Web Services. Actuellement, les applications développées avec le Serverless Framework peuvent être déployées sur d'autres fournisseurs de services FaaS. Voici la liste des services cloud Serverless pris en charge par le Serverless Framework :

* [**AWS Lambda**](https://aws.amazon.com/lambda/)
    
* [**Google Cloud Functions**](https://cloud.google.com/functions/)
    
* [**Azure Functions**](https://azure.microsoft.com/en-us/services/functions/)
    
* [**IBM OpenWhisk**](https://www.ibm.com/cloud-computing/bluemix/openwhisk)
    
* [**Auth0 Webtask**](https://webtask.io/)
    
* [**Oracle Fn Project**](https://fnproject.io/)
    
* [**Spotinst**](https://spotinst.com/)
    
* [**Kubeless**](https://kubeless.io/)
    

---

### Getting started with Serverless Framework

Évidemment, vous êtes très excité à l'idée de commencer avec le Serverless Framework, passons directement à l'installation de Serverless.

La configuration de Serverless est simple. Vous devez l'installer via npm et le lier à votre compte AWS.

#### 1\. Installation de Serverless Globalement

Il est temps de se mettre à Serverless.

```bash
$ npm install serverless -g
```

Cette commande installe Serverless globalement sur votre machine locale. Les commandes Serverless sont maintenant disponibles pour vous depuis votre terminal.

**Note :** Sous Linux, vous pouvez vouloir exécuter la commande ci-dessus en tant que sudo.

#### 2\. Créer un utilisateur IAM dans la Console AWS

Allez dans votre [Console AWS](https://console.aws.amazon.com/), vous trouverez le service [IAM](https://console.aws.amazon.com/iam/home) listé sous le groupe "Sécurité, Identité & Conformité". Dans le tableau de bord IAM, cliquez sur l'onglet Utilisateurs et cliquez sur le bouton "Ajouter un utilisateur".

![Image](https://cdn-media-1.freecodecamp.org/images/1*VtA7fGzE2a_h6yMTl69lBw.png align="left")

*Onglet Utilisateurs du Tableau de bord IAM AWS*

Créez un nouvel utilisateur et autorisez l'accès **programmatique** en cliquant sur la case à cocher Accès programmatique. Ensuite, dans la section des permissions, vous devez ajouter un ensemble de permissions à l'utilisateur. Dans la liste des options disponibles sous "Attacher des politiques existantes directement", cochez **AdministratorAccess**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_6PWCnAeK25k7P7CaL1uA.png align="left")

Après la création de l'utilisateur, vous aurez accès à l'**ID de la clé d'accès** et à la **Clé d'accès secrète** de l'utilisateur. Vous devrez utiliser ces clés dans l'étape suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7FqyvVFoRxZClqC16SevXw.png align="left")

**Avertissement :** Ce sont le genre de credentials que vous ne voulez pas perdre, même par erreur, rappelez-vous que vous avez fourni un **AdministratorAccess** à cet utilisateur. L'utilisateur avec **AdministratorAccess** peut faire presque tout avec votre compte AWS.

#### 3\. Configuration de Serverless pour utiliser les identifiants IAM

Super ! Avec les clés, vous pouvez configurer le Serverless Framework pour accéder à votre compte AWS. Passez à votre terminal et utilisez cette commande pour configurer Serverless :

```bash
$ sls config credentials --provider aws --key xxxxxxxxxxxxxx --secret xxxxxxxxxxxxxx --profile <username>
```

Maintenant, votre installation Serverless sait quel compte AWS connecter.

**Note :** `sls` est un alias pour la commande `serverless`. Vous pouvez utiliser les deux avec le même effet. Mais `sls` est plutôt cool.

#### 4\. Création d'un service

Avec le Serverless Framework connecté à votre compte AWS, vous pouvez configurer un projet Serverless en un clin d'œil. Lancez le terminal et exécutez la commande suivante :

```bash
$ sls create --template aws-python --path <your-folder-path>
```

Le drapeau `--template` est utilisé pour spécifier un modèle prédéfini avec les paramètres donnés. Dans la commande ci-dessus, le modèle `aws-python` configurera le projet pour utiliser AWS comme fournisseur et Python comme runtime. La commande générera automatiquement `serverless.yml`, `handler.py` et le fichier `.gitignore` avec des valeurs prédéfinies.

La configuration est définie dans le fichier `serverless.yml`. Ce fichier est le fichier le plus important dans le Serverless Framework. Il est presque magique, étant donné comment il peut créer l'infrastructure que vous avez définie. Le contenu du fichier `serverless.yml` généré automatiquement ressemblera à ceci :

```bash
service: <your-service-name>
  
provider:  
  name: aws  
  runtime: python2.7
    
functions:  
  hello:    
    handler: handler.hello
```

La section `provider` définit tout ce qui est lié au fournisseur de services, il y a beaucoup plus de propriétés pour le configurer davantage, vous pouvez les consulter [ici](https://serverless.com/framework/docs/providers/aws/guide/serverless.yml/). Dans le fichier `serverless.yml` généré automatiquement, vous devez ajouter deux balises importantes sous la section `provider`, qui sont les suivantes :

```bash
region: <your-aws-region>
profile: <aws-username-with-programmatic-access>
```

La propriété `functions` est utilisée pour déclarer les fonctions serverless, vous pouvez déclarer plusieurs fonctions sous cette propriété. L'exemple ci-dessus déclare une fonction appelée `hello` présente dans le fichier `handler.py`. Parcourez le fichier `handler.py` et vous trouverez quelque chose comme ceci :

```bash
import json
def hello(event, context):    
	body = {
    	"message": "Go Serverless v1.0! Your function executed      successfully!",        
        "input": event    
    }
    response = {
    	"statusCode": 200,        
        "body": json.dumps(body)    
    }
    return response
```

---

### L'application Serverless

Notre solution Serverless utilise l'infrastructure AWS, elle se compose de API Gateway, Lambda Functions, DynamoDB et Simple Email Service (SES). Pour atteindre ce résultat final, nous utiliserons le Serverless Framework précédemment introduit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Be-VuMqQEg6Ifh60bFtDcQ.png align="left")

*Architecture de l'application Serverless*

* **Site Web Statique
**
Amazon S3 fournit un serveur web robuste et simple. Tous les fichiers HTML, CSS et JS statiques de votre application peuvent être servis depuis S3. Le formulaire de contact sur notre site web statique est soumis en utilisant AJAX.
    
* **API Gateway
**
L'API Gateway est la source d'événements pour l'application, elle agit comme un pont entre notre formulaire de contact et la fonction lambda serverless. Elle achemine la requête du formulaire de contact vers la fonction lambda. L'API Gateway effectue également des tâches telles que le contrôle d'accès, la surveillance, le contrôle de version de l'API et la gestion du trafic.
    
* **AWS Lambda
**
AWS Lambda est l'endroit où l'action se déroule. Les fonctions Lambda s'exécutent dans des conteneurs de calcul sans état qui sont déclenchés par des événements, gérés et éphémères. Dans notre exemple, nous utilisons une fonction lambda pour envoyer un email en utilisant SES et stocker le contenu de la requête dans la base de données NoSQL DynamoDB.
    
* **Simple Email Service (SES)
**
Le service d'envoi d'emails basé sur le cloud d'Amazon. Service d'email évolutif, vous pouvez envoyer des emails marketing et transactionnels en utilisant SES. Dans notre exemple, nous utilisons SES pour envoyer des emails en utilisant une adresse email vérifiée.
    
* **DynamoDB
**
DynamoDB fournit une base de données évolutive, cohérente, entièrement gérée et non relationnelle d'Amazon. Dans notre exemple, nous utilisons DynamoDB pour stocker et récupérer les messages reçus du formulaire de contact statique.
    

Vous pouvez trouver le code source de l'application de démonstration ici. Allez-y et clonez-le !

[**faizanbashir/python-ses-dynamodb-contactform**](https://github.com/faizanbashir/python-ses-dynamodb-contactform)  
[\_python-ses-dynamodb-contactform - Serverless Framework SES et DynamoDB Contact Form\_github.com](https://github.com/faizanbashir/python-ses-dynamodb-contactform)

---

### Présentation de l'application

Faisons un tour de l'application de démonstration avant de la déployer sur AWS.

#### 1\. Démystification du fichier serverless.yml

Le fichier `serverless.yml` définit les services que l'application doit utiliser et avec lesquels interagir. Les ressources et les actions que les fonctions Serverless peuvent effectuer sont listées sous la propriété `**iamRoleStatements**`. Il liste les actions et les ressources.

```bash
iamRoleStatements:
  - Effect: "Allow"
    Action:
      - ses:SendEmail      
      - ses:SendRawEmail    
    Resource: "*"  
  - Effect: "Allow"    
    Action:      
      - dynamodb:Scan      
      - dynamodb:PutItem    
    Resource: "arn:aws:dynamodb:${opt:region, self:provider.region}:*:table/${self:provider.environment.DYNAMODB_TABLE}"
```

Dans le `serverless.yml`, nous permettons aux fonctions Serverless d'utiliser les actions `ses:SendEmail` et `dynamoDB:PutItem` parmi beaucoup d'autres définies ci-dessus.

Puisque Lambda exécute des fonctions serverless dans le cloud, nous devons définir les fonctions quelque part. Les fonctions sont définies en utilisant la propriété `**functions**`. Dans notre application d'exemple, nous avons défini des événements qui leur sont attachés.

```bash
functions:  
  sendMail:    
    handler: handler.sendMail
    description: Send Email using AWS SES Service
    events:
      - http:          
        path: sendMail          
        method: post          
        integration: lambda          
        cors: true          
        response:            
          headers:              
            "Access-Control-Allow_Origin": "'*'"  
            
  list:    
    handler: handler.list    
    description: List all the contact form submissions    
    events:      
      - http:          
        path: list          
        method: get          
        integration: lambda          
        cors: true          
        response:            
          headers:              
            "Access-Control-Allow_Origin": "'*'"
```

Une autre grande fonctionnalité du Serverless Framework est qu'il créera une API dans l'API Gateway AWS et la liera avec la fonction Lambda pertinente. Cela est fait en utilisant la propriété `http` définie dans la propriété `events`.

#### 2\. Création de ressources

Avec le Serverless Framework, vous créez des ressources comme une table DynamoDB comme nous l'avons fait ici. Ce snippet de code est responsable de la création d'une table DynamoDB avec la configuration donnée.

```bash
resources:  
  Resources:    
    ContactFormDynamoDbTable:      
      Type: 'AWS::DynamoDB::Table'      
      DeletionPolicy: Retain      
      Properties:        
        AttributeDefinitions:          
          -            
            AttributeName: id            
            AttributeType: S        
        KeySchema:          
          -            
            AttributeName: id            
            KeyType: HASH        
        ProvisionedThroughput:          
          ReadCapacityUnits: 1          
          WriteCapacityUnits: 1        
        TableName: ${self:provider.environment.DYNAMODB_TABLE}
```

#### 3\. Jeter un coup d'œil aux fonctions Serverless

L'application de démonstration est écrite en **python**, elle utilise le SDK AWS [**boto3**](https://github.com/boto/boto3) pour envoyer des emails en utilisant SES et pour effectuer des opérations de lecture/écriture sur DynamoDB.

La fonction `sendMail` est déclenchée lorsqu'une requête `POST` est reçue du formulaire de contact sur le chemin `/sendMail`. La fonction `list` est déclenchée par une requête `GET` vers le chemin `/list` défini dans le fichier `serverless.yml`.

---

### Construction de l'application

Maintenant que vous avez configuré et installé le Serverless Framework sur votre machine, il est temps de faire avancer les choses.

#### 1\. Cloner l'application

Commençons par cloner l'application depuis Github.

```bash
$ git clone https://github.com/faizanbashir/python-ses-dynamodb-contactform
$ cd python-ses-dynamodb-contactform
```

#### 2\. Vérifier l'adresse e-mail avec SES

Passez à la vérification de l'email que vous avez l'intention d'envoyer depuis SES. Tout ce que vous avez à faire est d'ajouter une adresse email, AWS vous enverra une vérification avec un lien pour vérifier l'adresse email.

![Image](https://cdn-media-1.freecodecamp.org/images/1*f_Y1mmdgKjtvxjBZL8zdIw.png align="left")

Après avoir vérifié l'adresse email, le "Statut de vérification" pour l'email apparaîtra comme "vérifié".

![Image](https://cdn-media-1.freecodecamp.org/images/1*IqxxKMYybvn0PlSPWgWgew.png align="left")

#### 3\. Configuration de l'application

Vous devez configurer le fichier `serverless.yml` avec les détails spécifiques à votre compte pour le faire fonctionner. Remplacez les propriétés `region`, `profile` et `SENDER_EMAIL` dans `serverless.yml` comme suit :

```bash
provider:  
  name: aws  
  runtime: python2.7  
  region: <aws-region>  
  profile: <aws-user>  
  ...
environment:  
  SENDER_EMAIL: <verified-email-address>
```

Super ! Avec la configuration terminée, vous pouvez vous concentrer sur le déploiement de l'application.

#### 4\. Déploiement sur AWS

Tout est en place maintenant, vous pouvez déployer l'application avec une seule commande, ce n'est pas super cool ?

```bash
$ sls deploy -v
```

Il faudra une minute ou deux pour s'exécuter si vous avez suivi ce tutoriel à la lettre, à la fin, il vous fournira une liste de points de terminaison à utiliser pour appeler nos fonctions. Cela ressemblera à ceci :

```bash
endpoints:
POST - https://xxx.execute-api.xx.amazonaws.com/development/sendMail
GET - https://xxxx.execute-api.xx.amazonaws.com/development/list
```

#### 5\. Test des points de terminaison

Maintenant que nous avons les points de terminaison, testons l'application pour voir si elle fonctionne ou non. Le point de terminaison `/sendMail` attend une entrée au format JSON.

```bash
$ curl --header "Content-Type: application/json" \--request POST \--data '{"firstname": "John", "lastname": "Doe", "email": "john@doe.com", "message": "Hi there"}'\https://xxx.execute-api.xx.amazonaws.com/development/sendMail
```

Si l'email est envoyé et l'entrée écrite dans DynamoDB, la requête se terminera avec une réponse comme celle-ci.

```bash
> "Email Sent!"
```

Maintenant, testons le point de terminaison `/list` de la même manière avec le point de terminaison `GET` que vous avez obtenu après avoir déployé l'application.

```bash
$ curl https://xxxx.execute-api.xx.amazonaws.com/development/list
```

La réponse du point de terminaison `/list` ressemblera à ceci :

```bash
> {"body": [{"firstname": "John", "lastname": "Doe", "email": "john@doe.com", "updatedAt": 1529425349731, "message": "Hi there", "id": "f651c404-73dc-11e8-bf3e-be54be0b5d22", "createdAt": 1529425349731}], "statusCode": 200}
```

#### 6\. Le formulaire de contact

Avec les fonctions Serverless fonctionnant correctement, nous pouvons aller de l'avant et les intégrer dans notre formulaire de contact statique. Le code du formulaire statique se trouve dans le dossier `public`.

Ouvrez le fichier `index.html` dans votre IDE préféré et mettez à jour la variable `URL` avec le point de terminaison `/sendMail` et vous êtes prêt à partir.

```bash
//Insert your lambda function URL here
var URL = "https://xxx.execute-api.xx.amazonaws.com/development/sendMail";
```

Accédez à la page en utilisant `file:///<path>/<to>/<folder>/index.html` dans le navigateur ou téléchargez-la dans un bucket S3 et activez l'hébergement statique.

```bash
$ aws s3 sync public s3://your-bucket-name
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*G6Q3XRI6tADC38nbcJohkQ.png align="left")

*Formulaire de contact Serverless*

Offrez-vous un Cappuccino, un Latte ou autre. Vous venez de mettre en place une manière cool de garder votre site web sur un hébergement statique tout en gérant vos formulaires, grâce à Serverless.

---

### Réflexions finales

Serverless est définitivement la voie à suivre, pas seulement pour les formulaires de contact statiques du monde. Serverless a ouvert un univers d'opportunités pour vous, le formulaire de contact n'était qu'un début. Et si vous utilisiez Serverless pour vos analyses de site web, un compteur de visiteurs ou peut-être le suivi des clics ?

Des opportunités sans fin vous attendent. Lancez-vous pour votre prochain projet en Serverless, ce sera un voyage incroyable.

---

*Publié à l'origine sur* [*www.serverlessops.io*](https://www.serverlessops.io/blog/serverless-contact-form-for-static-websites)*.*