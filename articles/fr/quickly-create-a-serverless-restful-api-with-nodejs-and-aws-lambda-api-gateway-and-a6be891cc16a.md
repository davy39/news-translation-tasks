---
title: Comment créer rapidement une API RESTful sans serveur avec Node.js et AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-26T01:30:16.000Z'
originalURL: https://freecodecamp.org/news/quickly-create-a-serverless-restful-api-with-nodejs-and-aws-lambda-api-gateway-and-a6be891cc16a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YofxX8XmRkh_uB4XMyq34g.png
tags:
- name: AWS
  slug: aws
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment créer rapidement une API RESTful sans serveur avec Node.js et AWS
seo_desc: 'By Mark Hopson

  In this beginner’s guide, we’ll briefly describe the “Serverless” software architecture,
  and then create a RESTful API using AWS, Node.js, and Swagger in a few short minutes.

  So what’s Serverless?

  The term Serverless (a.k.a. Functions-...'
---

Par Mark Hopson

Dans ce guide pour débutants, nous allons brièvement décrire l'architecture logicielle "Serverless", puis créer une API RESTful en utilisant AWS, Node.js et Swagger en quelques minutes.

### Qu'est-ce que le Serverless ?

Le terme Serverless (également connu sous le nom de Functions-as-a-Service) décrit un type d'architecture qui permet de déployer et d'exécuter du code sur des conteneurs éphémères et sans état fournis par des tiers (comme Azure ou AWS).

#### Avantages du Serverless

* **Réduction de la gestion opérationnelle.** Les architectures Serverless permettent aux développeurs de se concentrer sur l'écriture de code, sans se soucier de la configuration et de la gestion de l'infrastructure sur laquelle leur code s'exécute.
* **Mise à l'échelle facile et flexible.** Puisque les fonctions Serverless (vos applications Serverless) sont sans état et toujours invoquées par un événement (comme une requête HTTP), vous pouvez exécuter autant, ou aussi peu, de fonctions que nécessaire. Plus d'invocations signifient plus de conteneurs. Selon l'échelle et la forme de votre trafic, cela peut être très rentable, car les fonctions Serverless sont généralement facturées par invocation.

#### Inconvénients du Serverless

* **Latence pour les premières requêtes (connue sous le nom de "cold starts").** Si la fonction Serverless est inactive (n'a pas été exécutée depuis un certain temps), alors le traitement de la première invocation peut nécessiter un temps supplémentaire pour se compléter car le conteneur devra s'initialiser (c'est-à-dire allouer l'hôte, charger le code, etc.).
* **Manque de contrôle du système.** Puisque votre code s'exécute dans un environnement géré par un fournisseur, vous ne pourrez pas contrôler les mises à jour du système, ou les dépendances en dehors de votre base de code.

### Et qu'est-ce que CloudFormation ?

CloudFormation est un service d'Amazon qui vous permet de construire des ressources AWS en utilisant des templates. Un template est un fichier de configuration (YML ou JSON) pour provisionner toutes vos ressources AWS telles que des instances EC2, des tables DynamoDB, des rôles et permissions IAM, ou autre chose.

### Commençons à coder !

Dans ce tutoriel, nous allons créer une API RESTful simple avec les deux endpoints suivants :

#### POST /users/${userId}/hello

Le corps de la requête sera sauvegardé dans une table DynamoDB. Dans ce tutoriel, le corps de la requête doit avoir cette structure : `{ "email": "any@email.com" }`

#### GET /users/${userId}/hello

La réponse contiendra la valeur pour `"email"` définie dans la requête POST.

![Image](https://cdn-media-1.freecodecamp.org/images/P04BLr7QnCkdrzhpX6KANzaOxxwfzzUTzUGx)
_Une architecture système simplifiée de ce que nous allons construire._

#### Étape 1 : Clonez le dépôt

Il y a deux fichiers dont vous avez besoin pour ce tutoriel : `index.js` (le code NodeJS pour notre fonction Lambda) et `stack.yml` (le template de stack CloudFormation). Pour obtenir ces fichiers, visitez [ce lien](https://github.com/markhopson/cloudformation-serverless-api) Github.

#### Étape 2 : Examinez le fichier stack.yml

Faites attention au fichier `stack.yml` dans le dépôt, car c'est le fichier de configuration qui sera utilisé par CloudFormation pour créer tout ce dont notre application aura besoin.

Ci-dessous se trouve un diagramme détaillé de toutes les ressources AWS que notre `stack.yml` devra créer. Les noms utilisés dans le YML sont dans les boîtes rouges.

![Image](https://cdn-media-1.freecodecamp.org/images/B5oGAguxI6ZzZESx99yV0XWDk4nrQ1fnd1Pj)
_Toutes les ressources AWS (boîtes grises) qui seront provisionnées par notre fichier CloudFormation `stack.yml`._

#### Étape 3 : Téléchargez votre template CloudFormation

Après avoir examiné le fichier YML, rendez-vous sur [ce lien](https://console.aws.amazon.com/cloudformation) et cliquez sur le bouton **Créer une stack**. Choisissez **Télécharger un template vers Amazon S3** et téléchargez le fichier `stack.yml`.

![Image](https://cdn-media-1.freecodecamp.org/images/vrSzSMhfzIEL6jbjhsoRqSlGLTTkZrqYNmAI)
_Créez votre stack CloudFormation en téléchargeant d'abord notre template `stack.yml`._

Sur l'écran suivant, vous serez invité à choisir un **Nom de stack** (peut être n'importe quoi). Après cela, cliquez sur Suivant et sélectionnez **Je reconnais qu'AWS CloudFormation pourrait créer des ressources IAM**, puis cliquez à nouveau sur Suivant.

À ce stade, votre stack est en cours de création. Attendez une minute sur la page des stacks jusqu'à ce que le statut de votre stack devienne **CREATE_COMPLETE**.

![Image](https://cdn-media-1.freecodecamp.org/images/C0drkb4xxGIHAJOwSzjYriMn4vDqn9-2xRCP)
_La page de liste des stacks CloudFormation avec le statut._

#### Étape 4 : Trouvez votre Lambda créée par CloudFormation

Une fois votre stack complète, allez trouver la nouvelle Lambda de votre stack [ici](https://console.aws.amazon.com/lambda). Le nom de la fonction de votre Lambda devrait ressembler à **${StackName}-HelloLambda-XXXX**.

![Image](https://cdn-media-1.freecodecamp.org/images/mjmf5CxbNznAvYisJXr2C7OAPevVVtyBMAYi)
_Page de liste des Lambda_

#### Étape 5 : Déployez (copiez et collez) votre code dans votre Lambda

Une fois que vous avez trouvé votre Lambda, cliquez dessus pour plus de détails. Ensuite, faites défiler jusqu'à la section **Code de la fonction**, changez le **Type d'entrée de code** en **Modifier le code en ligne**, puis ouvrez et copiez `index.js` (du dépôt) dans l'éditeur de code. Cliquez sur **Enregistrer**.

![Image](https://cdn-media-1.freecodecamp.org/images/Rm2WnYjfErwGdcI078HzvlMh8OSbFjwkuXJw)
_Ma page de détails de Lambda avec l'éditeur de code en ligne_

À ce stade, votre code a été "déployé" sur le Lambda, et il ne reste plus qu'à déployer notre API Gateway pour que nous puissions lui envoyer des requêtes HTTP.

#### Étape 6 : Trouvez votre API Gateway créée par CloudFormation

Trouvez votre API Gateway créée par votre template CloudFormation [ici](https://console.aws.amazon.com/apigateway). Le nom de votre API Gateway devrait ressembler à **${StackName}-MyApiGateway**.

![Image](https://cdn-media-1.freecodecamp.org/images/yfx9e9OPI6QdU577QQLufZ5TkBKHORDyTQik)
_La page de détails pour l'endpoint POST /hello_

#### Étape 7 : Testez si votre API Gateway est connectée à Lambda

Après avoir trouvé votre API Gateway, nous pouvons tester pour voir si tout est connecté en sélectionnant l'option **POST** sous **/users** puis en cliquant sur **TEST**.

![Image](https://cdn-media-1.freecodecamp.org/images/uzYspS9a9seVUYWaxzT8avKmIVKFxPhfTXNx)
_La page de test pour l'endpoint POST /hello après une requête de test réussie._

Sur la page de test, définissez **userId** à 123, et définissez le **Corps de la requête** comme suit et cliquez sur **Test**. Si tout a fonctionné, le **Statut** devrait être **200** sans données.

![Image](https://cdn-media-1.freecodecamp.org/images/N8VquMDYIYnp792ZjcuXeM4BBhtQ6zJw5shU)
_La page de test pour l'endpoint GET /hello après une requête de test réussie._

Après avoir testé l'endpoint POST, vous pouvez vérifier si vos données ont été sauvegardées en allant sur la page de test GET /hello et en essayant une requête (n'oubliez pas de définir **userId** à 123). Le corps de la réponse devrait contenir le corps de la requête du test POST (voir ci-dessus).

Maintenant que vous avez vérifié que votre API Gateway, Lambda et DynamoDB sont connectés, vous pouvez déployer votre API Gateway pour pouvoir y accéder depuis Internet.

#### Étape 8 : Déployez votre API Gateway

Pour déployer votre API, cliquez sur le menu Actions et sélectionnez Déployer l'API. Une fois la fenêtre de confirmation apparue, définissez **Étape de déploiement** sur **prod** puis cliquez sur **Déployer**.

![Image](https://cdn-media-1.freecodecamp.org/images/61EyYYsUGVS1d8FBv2hwQFDCm2lksXbIUOnT)
_L'option Déployer l'API dans le menu déroulant Actions._

Une fois que vous avez déployé votre API, vous serez redirigé vers la page **Étapes** pour **prod**. Ici, vous trouverez le domaine de votre API Gateway dans la zone surlignée en bleu à côté de **URL d'invocation**.

![Image](https://cdn-media-1.freecodecamp.org/images/quo2GSkRBopc1s-bWDVZVgP1PWPu7iod1d8y)
_Trouvez l'URL publique (URL d'invocation) pour votre API Gateway dans la grande boîte bleue._

En utilisant l'URL de la capture d'écran ci-dessus, je devrais pouvoir envoyer une requête **GET /users/123/hello** dans mon navigateur web comme ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1Z-JHxCJCE7QtuPvGVvYUtfO83EvqOMg9qap)
_Une requête réussie à mon API Serverless depuis le monde extérieur_

Et c'est tout ! Vous avez maintenant une API RESTful Serverless qui est scalable, fiable, ne nécessite pas de patching ou de provisionnement, et ne coûte pas d'argent lorsqu'elle est inactive. J'espère que vous avez apprécié ce tutoriel, et si vous avez des commentaires, n'hésitez pas à les laisser dans les commentaires ci-dessous. Merci !

### Autres notes et remarques

* La configuration des routes pour API Gateway est intégrée dans la configuration de l'API Gateway (MyApiGateway) dans `stack.yml`, ce qui rend le YML encore plus monstrueux qu'il ne l'est déjà.
* Les variables d'environnement dans la page de configuration de la Lambda HelloLambda contiennent les informations nécessaires pour se connecter à la table DynamoDB HelloTable.
* Le AWS-SDK est fourni avec chaque fonction Lambda, donc nous pouvons utiliser `require('aws-sdk')` sans avoir besoin d'un `package.json`. Très pratique !
* Au lieu de copier et coller le code NodeJS dans l'éditeur intégré de la page de détails de la Lambda, vous pouvez déployer votre code via l'AWS CLI. Nous copions et collons pour simplifier.
* Attention, le template de stack CloudFormation est naturellement très verbeux. Je vous promets que ce n'est pas juste moi et mon `stack.yml`.
* La clé de partition principale de la table DynamoDB HelloTable est **userId**
* De u/[**SalamiJack**](https://www.reddit.com/user/SalamiJack) : "Il vaut la peine de mentionner que les performances de l'API Gateway + Lambda, même pour une Lambda simple et préchauffée, sont assez mauvaises. Attendez-vous à des temps de réponse de l'ordre de 80 à 150 ms en tout temps."

_Publié à l'origine sur [medium.com](https://medium.com/@markhopson/how-to-create-a-serverless-restful-api-with-nodejs-and-aws-9aab63c636db) le 26 mars 2018._