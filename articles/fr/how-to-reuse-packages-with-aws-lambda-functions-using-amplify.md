---
title: Comment réutiliser des packages Node.js avec des fonctions AWS Lambda en utilisant
  Amplify et Lambda Layers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T19:33:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-reuse-packages-with-aws-lambda-functions-using-amplify
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99a3740569d1a4ca20e2.jpg
tags:
- name: aws lambda
  slug: aws-lambda
- name: node js
  slug: node-js
- name: serverless
  slug: serverless
seo_title: Comment réutiliser des packages Node.js avec des fonctions AWS Lambda en
  utilisant Amplify et Lambda Layers
seo_desc: 'By Erick Wendel

  In this article, you''ll learn how to inject custom packages on AWS Lambda Functions''
  Runtime by using AWS Lambda Layers. You''ll also use Amplify to develop, deploy,
  and distribute your applications.

  Serverless applications are great f...'
---

Par Erick Wendel

Dans cet article, vous apprendrez comment injecter des packages personnalisés dans le runtime des fonctions AWS Lambda en utilisant AWS Lambda Layers. Vous utiliserez également Amplify pour développer, déployer et distribuer vos applications.

Les applications serverless sont idéales pour ceux qui ne veulent pas payer pour des machines inactives ou même gérer des infrastructures cloud. Cet article se concentrera sur une introduction douce au **Framework Amplify** en utilisant **Node.js**. Vous installerez un package Node.js personnalisé une fois et l'injecterez dans toutes vos fonctions en utilisant **AWS Lambda Layers**.

À la fin de cet article, vous aurez appris comment déployer des fonctions serverless sur AWS en :

* Créant une API Web Node.js utilisant Express.js comme fonction serverless en utilisant le **Framework Amplify**
* Injectant un package personnalisé dans le runtime des fonctions AWS Lambda en utilisant AWS Lambda Layers pour surveiller et étendre les requêtes HTTP.

## **Conditions préalables**

Dans les étapes suivantes, vous créerez une application réelle et la publierez sur l'infrastructure AWS. Avant de commencer à coder, assurez-vous d'avoir les conditions préalables suivantes configurées dans votre environnement :

* Un compte AWS actif
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
* [Node.js v14](https://nodejs.org/en/download/current/)

## **Introduction**

L'une de mes plateformes cloud préférées qui fournit une infrastructure serverless est Amazon Web Services. Ils développent et livrent depuis longtemps des plateformes qui permettent aux entreprises de publier des logiciels plus rapidement que si elles devaient configurer et gérer des configurations répétitives.

Si vous êtes familier avec les applications serverless, vous avez peut-être entendu parler du [Serverless Framework](https://www.serverless.com/). Il s'agit d'un framework multi-cloud pour gérer des architectures serverless en utilisant des fichiers de configuration, déployer et exécuter des applications en utilisant une seule commande.

Même ainsi, les développeurs doivent encore installer des plugins et gérer des fichiers de configuration par eux-mêmes, ce qui peut prendre un certain temps pour construire un workflow complexe.

Alors, quel type de CLI préférez-vous ? Une CLI qui vous demanderait ce que vous voulez, comme des connexions externes (Base de données, Stockage, File d'attente, etc.), un flux d'authentification, des permissions externes, et ainsi de suite ? Oui, mon ami, bienvenue dans **AWS Amplify**.

## AWS Amplify

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-18-at-00.06.42.png)
_Site web du Framework Amplify_

AWS Amplify est un écosystème qui aide les développeurs back-end, front-end et d'intégration. Si vous regardez sa [documentation officielle](https://aws.amazon.com/amplify/framework/), vous verrez la longue liste de bibliothèques et d'exemples possibles pour travailler à la fois sur les applications back-end et front-end.

Lorsque vous avez configuré votre AWS CLI et votre environnement, exécutez la commande suivante pour installer AWS Amplify globalement sur votre machine :

`npm install -g amplify-cli`

Ensuite, initialisons un répertoire de travail en créant un dossier :

`mkdir app && cd app`

Maintenant, vous allez initialiser un projet Amplify en exécutant la commande ci-dessous. Pour ce faire, vous devrez vérifier quelques options dans l'assistant CLI. Remarquez que lorsque vous y êtes invité, vous pouvez appuyer sur **Entrée** sur votre clavier pour choisir les valeurs par défaut.

`amplify init`

Choisissez les options selon le texte en **gras** ci-dessous :

* Entrez un nom pour le projet **app**
* Entrez un nom pour l'environnement **dev**
* Choisissez votre éditeur par défaut : **Visual Studio Code**
* Choisissez le type d'application que vous construisez **javascript**

Parlez-nous de votre projet

* Quel framework javascript utilisez-vous **none**
* Chemin du répertoire source : **src**
* Chemin du répertoire de distribution : **dist**
* Commande de construction : **npm run-script build**
* Commande de démarrage : **npm run-script start**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/01-init.gif)

## Initialisation du projet partagé

Au cours des étapes suivantes, vous créerez une fonction. Cette fonction sera utilisée pour stocker des dépendances qui seront injectées plus tard dans les fonctions autour de l'écosystème des fonctions AWS Lambda.

L'exécution de la commande ci-dessous vous guidera vers les étapes pour créer votre Lambda Layer :

`amplify function add`

Choisissez les options selon les options en texte **gras** ci-dessous. Remarquez que pour les runtimes compatibles, vous devrez appuyer sur la touche **espace** de votre clavier pour sélectionner le runtime.

* Sélectionnez la capacité que vous souhaitez ajouter : Lambda layer (code et ressource partagés utilisés dans les fonctions)
* Fournissez un nom pour votre Lambda layer : **apmAgentLayer**
* Sélectionnez jusqu'à 2 runtimes compatibles : **NodeJS**
* Le compte AWS actuel aura toujours accès à cette couche.
* Optionnellement, configurez qui d'autre peut accéder à cette couche. (Appuyez pour ignorer) **Public**

✅ Dossiers et fichiers de la couche Lambda créés : amplify/backend/function/apmAgentLayer

### Installation de modules personnalisés

En allant au chemin de la couche _amplify/backend/function/apmAgentLayer_, vous avez peut-être vu quelques dossiers créés par Amplify. Comme nous travaillons sur un projet Node.js, tous les modules Node doivent être installés sur _lib/nodejs_.

J'ai construit un exemple de moniteur de performance d'application pour montrer comment utiliser la fonctionnalité _performance hooks_ de Node.js pour mesurer la durée entre les requêtes et changer les lecteurs de réponse HTTP. Cela aidera à montrer d'autres possibilités pour implémenter du code partagé et étendre le comportement de Node.js.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-18-at-00.56.56.png)
_Package NPM pour mesurer la durée entre les requêtes_

La première étape ici est d'installer les dépendances partagées et de les télécharger sur AWS. Allez au chemin généré par la CLI _amplify/backend/function/apmAgentLayer/lib/nodejs_ puis installez le package en utilisant les commandes suivantes :

```sh
cd amplify/backend/function/apmAgentLayer/lib/nodejs
npm i @erickwendel/ew-agent
```

### Déploiement

Une fois que vous avez installé votre package, vous pouvez simplement le déployer et l'inspecter plus tard via la console AWS. Remarquez que nous n'avons pas encore ajouté de code. L'objectif à ce stade est simplement de préparer cette bibliothèque pour une utilisation ultérieure.

Exécutez la commande suivante pour télécharger votre Lambda Layer :

`amplify push`

![Image](https://www.freecodecamp.org/news/content/images/2020/07/02-amplify-push.gif)
_exécution de la commande amplify push et visualisation de la sortie_

## Création de la fonction API Web

À ce stade, vous avez déjà un projet d'infrastructure Amplify local prêt à ajouter des routes API, des routines, à le lier avec des services AWS, et ainsi de suite.

La commande ci-dessous sera utile pour générer un projet basé sur ExpressJS et une fonction AWS Lambda. Elle liera également la fonction sur votre couche AWS Lambda nouvellement créée et l'exposera sur l'AWS API Gateway.

`amplify api add`

Choisissez les options selon le texte en **gras** ci-dessous :

* Veuillez sélectionner l'un des services mentionnés ci-dessous : **REST**
* Fournissez un nom convivial pour votre ressource à utiliser comme étiquette pour cette catégorie dans le projet : **myApi**
* Fournissez un chemin (par exemple, /book/{isbn}) : **/hi**
* Choisissez une source Lambda **Créer une nouvelle fonction Lambda**
* Fournissez un nom convivial pour votre ressource à utiliser comme étiquette pour cette catégorie dans le projet : **myApi**
* Fournissez le nom de la fonction AWS Lambda : **myApi**
* Choisissez le runtime que vous souhaitez utiliser : **NodeJS**
* Choisissez le modèle de fonction que vous souhaitez utiliser : **Fonction Serverless ExpressJS (Intégration avec API Gateway)**
* Souhaitez-vous accéder à d'autres ressources dans ce projet à partir de votre fonction Lambda ? **Non**
* Souhaitez-vous invoquer cette fonction selon un calendrier récurrent ? **Non**
* Souhaitez-vous configurer des couches Lambda pour cette fonction ? **Oui**
* Fournissez des couches existantes ou sélectionnez des couches dans ce projet pour y accéder à partir de cette fonction (choisissez jusqu'à 5) : **apmAgentLayer**
* Sélectionnez une version pour apmAgentLayer : **1**
* Souhaitez-vous modifier la fonction lambda locale maintenant ? **Oui**

Comme j'utilise VSCode, la dernière réponse de l'assistant ouvrira le fichier `app.js` dans mon éditeur afin que je puisse le modifier. Maintenant, sans ajouter d'autres dépendances, importons le module partagé **Lambda Layer** sur la première ligne de ce fichier en utilisant le code ci-dessous :

```javascript
require('@erickwendel/ew-agent').start()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screen-Shot-2020-07-18-at-01.24.42.png)
_code ajouté en tête du fichier_

Après avoir modifié le fichier, allez dans le terminal et appuyez sur **Entrée** et choisissez les réponses affichées en **gras** ci-dessous :

* Restreindre l'accès à l'API **Non**
* Souhaitez-vous ajouter un autre chemin ? **Non**

Au moment de la rédaction, nous ne pouvons pas tester les Lambda Layers localement en utilisant AWS Amplify. Mais vous allez déployer votre projet sur AWS et le tester **en production** en exécutant à nouveau la commande `amplify push`.

Remarquez qu'il imprimera quelles ressources doivent être mises à jour et quelles ressources seront créées lors de ce déploiement. Cela prendra un certain temps pour effectuer toutes les opérations et votre sortie devrait ressembler à ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/03-deploy-fn-1.gif)
_déploiement de l'API_

Comme votre terminal peut l'avoir montré, votre API a maintenant une URL. Mon URL générée est [https://nlq7x7onj0.execute-api.us-east-1.amazonaws.com/dev](https://nlq7x7onj0.execute-api.us-east-1.amazonaws.com/dev/hi) et la route sera `hi`, que nous avons créée ensemble dans les étapes précédentes.

Déclenchons une requête en utilisant cURL (ou même votre navigateur) pour voir ce qui se passe :

```sh
curl -i https://nlq7x7onj0.execute-api.us-east-1.amazonaws.com/dev/hi
```

Après l'avoir exécuté, l'API devrait répondre avec une réponse JSON avec le contenu suivant `{"success":"get call succeed!","url":"/hi"}`. La couche Lambda a été injectée et elle devrait avoir changé vos en-têtes de réponse en ajoutant les clés `x-instrumented-by` et `x-request-id` comme ceci :

```sh
x-instrumented-by: ErickWendel
x-request-id: 5ddf1343-e42e-4e33-b1e1-936c303c14c8
```

Si vous êtes curieux de savoir ce qu'Amplify a géré pour vous pendant ce tutoriel, exécutez `amplify console` et naviguez sur le tableau de bord. Vous pouvez voir le mien ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/04-aws-console.gif)
_tableau de bord et visualisation des journaux de fonction sur AWS_

## Nettoyage

Pour supprimer toutes les ressources créées par Amplify, exécutez `amplify delete`.

## Conclusion

Il existe de nombreuses façons d'améliorer votre expérience avec les applications serverless. Le Framework Amplify peut vous aider à construire des applications de nouvelle génération et à éviter les tâches répétitives.

Consultez la documentation officielle pour voir d'autres possibilités de construire des API puissantes en utilisant des technologies de pointe telles que GraphQL et AWS AppSync. Je suis sûr que cela vous aidera beaucoup !

## **Merci d'avoir lu**

J'apprécie vraiment le temps que nous avons passé ensemble. J'espère que ce contenu sera plus que du simple texte. J'espère qu'il vous aura rendu meilleur penseur et aussi meilleur programmeur. Suivez-moi sur [Twitter](https://twitter.com/erickwendel_) et consultez mon [blog personnel](https://erickwendel.com/) où je partage tout mon contenu précieux.

À bientôt ! 😊