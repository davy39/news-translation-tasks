---
title: 'Devenir serverless avec React et AWS Amplify : Installation de l''environnement
  de développement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T16:31:05.000Z'
originalURL: https://freecodecamp.org/news/going-serverless-with-react-and-aws-amplify-development-environment-set-up-9b15c3363bd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*B6_zkUG4Or9zIWwU
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: 'Devenir serverless avec React et AWS Amplify : Installation de l''environnement
  de développement'
seo_desc: 'By Peter Mbanugo

  Serverless computing provides us with benefits such as reduced operation costs and
  development time. It allows us focus on our code to provide business value to the
  users without worrying about building and maintaining servers.

  AWS i...'
---

Par Peter Mbanugo

Le serverless computing nous offre des avantages tels que la réduction des coûts opérationnels et du temps de développement. Il nous permet de nous concentrer sur notre code pour fournir une valeur commerciale aux utilisateurs sans nous soucier de la construction et de la maintenance des serveurs.

AWS est l'un des nombreux fournisseurs de services de serverless computing. Dans cet article, je vais vous guider à travers la configuration de votre environnement de développement pour construire sur AWS. Ce sera une introduction pour les futurs articles de cette série.

Selon [Wikipedia](https://en.wikipedia.org/wiki/Serverless_computing), le serverless computing est un modèle d'exécution de cloud computing dans lequel le fournisseur de cloud agit comme serveur, gérant dynamiquement l'allocation des ressources machine. Cela signifie généralement que vous pouvez construire des applications prêtes pour la production en vous concentrant sur la codification de la logique métier, et laisser la tâche de provisionnement des serveurs, de mise à l'échelle ou de mise à niveau des serveurs, et d'autres fonctionnalités à des fournisseurs de cloud ou à des fournisseurs de services tiers. Vous pouvez utiliser cela pour construire presque tout type d'application ou de service backend, et tout ce qui est nécessaire pour exécuter et mettre à l'échelle votre application avec une haute disponibilité est géré pour vous.

Ce modèle d'exécution des applications nous offre des avantages tels que la réduction des coûts opérationnels, la réduction du temps de développement, et bien plus encore. Si vous souhaitez en savoir plus sur ce qu'est le serverless et ses avantages, consultez [cet article sur l'architecture serverless](https://martinfowler.com/articles/serverless.html).

### Que vais-je apprendre en lisant ceci ?

Cet article (et d'autres à venir dans un avenir proche) est destiné à vous apprendre à construire des applications React en utilisant l'architecture serverless et divers services [AWS](https://aws.amazon.com/). Nous aborderons des domaines tels que l'authentification, la création et la consommation d'API REST, l'analyse, et l'hébergement, tout en utilisant les services d'un seul fournisseur de cloud. Nous travaillerons avec [AWS Amplify](https://aws-amplify.github.io/), qui fournit des outils CLI et des composants UI pour faciliter la construction d'applications serverless sur AWS.

Dans cet article, je vais vous guider à travers la configuration de votre environnement de développement pour construire sur AWS.

### Commencer avec AWS Amplify

[AWS Amplify](https://aws-amplify.github.io/) est une bibliothèque qui vous fournit des outils pour construire des applications serverless. Avec elle, l'intégration de divers services AWS avec votre application peut être faite en quelques lignes de code. Vous obtenez également des composants UI pour accélérer le développement.

Pour utiliser les services AWS ou la bibliothèque Amplify, vous aurez besoin d'un compte AWS. Si vous n'en avez pas, vous pouvez [vous inscrire](https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation) maintenant. L'inscription vous donne un accès immédiat au niveau gratuit d'AWS et il n'y a pas de frais initiaux.

### Installer et configurer l'AWS Amplify CLI

L'AWS Amplify CLI est un outil qui vous permet de créer et de configurer des services AWS pour votre application. Son but est de simplifier le développement d'applications mobiles et web pour vous. Le CLI utilise [AWS CloudFormation](https://aws.amazon.com/cloudformation/) et des piles imbriquées, ce qui vous permet d'ajouter ou de modifier des configurations localement avant de les pousser pour exécution dans le cloud.

Vous avez besoin de Node.js (version 8.11 ou supérieure) et de npm (version 5 ou supérieure) installés pour utiliser le CLI. Si vous ne les avez pas installés, visitez la [page de téléchargement de Node.js](https://nodejs.org/en/download/). L'installation de Node.js vous donnera également npm, mais si vous avez seulement Node.js installé, vous pouvez également [télécharger npm](https://www.npmjs.com/get-npm) séparément.

Installez le CLI en exécutant `npm install -g @aws-amplify/cli` dans la ligne de commande. N'utilisez pas yarn pour installer le CLI car il a des problèmes connus. Une fois l'AWS Amplify CLI installé, vous devrez le configurer pour spécifier les informations d'identification AWS nécessaires et la région. Suivez les instructions ci-dessous pour configurer le CLI.

1. Ouvrez la ligne de commande et exécutez la commande `amplify configure`. Cela ouvrira la console AWS dans votre navigateur, et si vous n'êtes pas connecté, vous devrez vous connecter à votre compte.
2. Une fois connecté, retournez à la ligne de commande et appuyez sur Entrée.
3. Vous serez invité à sélectionner une région AWS. Sélectionnez-en une et appuyez sur Entrée.
4. Vous avez ensuite la possibilité de spécifier le nom d'utilisateur d'un nouvel utilisateur AWS IAM (Identity and Access Management) à utiliser avec le CLI. Entrez un nom d'utilisateur et appuyez sur Entrée. Lorsque vous appuyez sur Entrée, cela ouvre votre navigateur et vous emmène au tableau de bord IAM dans la console AWS.
5. Sur le tableau de bord IAM, on vous demande de créer un nouvel utilisateur. Le champ nom d'utilisateur est pré-rempli avec le nom d'utilisateur que vous avez entré dans la console, et le type d'accès `Programmatic Access` est sélectionné. Cliquez sur le bouton `Next: Permissions` pour passer à la page suivante.
6. Laissez la politique `Administrator Access` sélectionnée par défaut et cliquez sur le bouton `Next: Review`.
7. Cliquez sur le bouton `Create User` pour créer l'utilisateur. Lorsque l'utilisateur est créé, vous recevrez un **Access Key ID** et un **Secret Access Key**. Conservez ces informations car vous en aurez besoin pour configurer le CLI.
8. Retournez à la ligne de commande et appuyez sur Entrée.
9. Il vous demandera l'**Access Key ID**. Copiez et collez la valeur puis appuyez sur Entrée.
10. Une autre invite apparaît demandant le **Secret Access Key**. Copiez et collez la valeur puis appuyez sur Entrée.
11. Maintenant, on vous demandera si vous souhaitez créer ou mettre à jour le profil AWS sur votre machine locale. Nous utiliserons le profil par défaut. Appuyez sur Entrée pour sélectionner le profil par défaut et créer votre profil AWS.

![Image](https://cdn-media-1.freecodecamp.org/images/WQsdAH5XMIvZzw5gD2DfjVbP2EOQhtISKCe3)

### Créer l'application React

Maintenant que l'AWS Amplify CLI a été configuré, nous pouvons commencer à créer l'application React. Nous allons démarrer l'application React avec [Create React App](https://github.com/facebookincubator/create-react-app). Cela nous permet de nous concentrer sur l'écriture de code et de ne pas nous soucier de la configuration de Babel et Webpack car ils seront préconfigurés pour nous. Pour créer le projet React, exécutez la commande suivante :

```
$ npx create-react-app serverless-react
```

Cela crée un dossier `serverless-react` avec les fichiers nécessaires pour une application React. La prochaine chose à faire est d'initialiser un projet Amplify. Pour ce faire, suivez les instructions ci-dessous

1. Changez de répertoire pour le projet en exécutant `cd serverless-react` dans la ligne de commande
2. Exécutez la commande `amplify init`. Cela vous invitera à répondre à quelques questions.
3. Sélectionnez votre éditeur de code et appuyez sur Entrée.
4. La série suivante d'invites vous présente des questions pour déterminer le type d'application que vous construisez. Sélectionnez JavaScript, puis React, et appuyez sur Entrée pour les invites restantes pour utiliser les valeurs par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/-No7PaAGFPBfb4jGZDHL5zkU5aYRKs7FwmEn)

La commande `amplify init` configure les ressources de déploiement dans le cloud avec des piles CloudFormation, et prépare le projet pour Amplify. Elle extrait les détails de configuration des ressources dans le répertoire du projet. Ces informations de configuration seront utilisées pour ajouter des services AWS au projet et mettre à jour la configuration des services. À la racine du répertoire du projet, vous trouverez un fichier `.amplifyrc` et un dossier **amplify**. Ils contiennent les informations de configuration CloudFormation pour les ressources que nous utiliserons.

Le dernier élément dont nous avons besoin pour configurer le projet est d'ajouter la bibliothèque Amplify à notre projet. La bibliothèque nous fournit des modules et des composants UI qui facilitent l'intégration des services AWS en quelques lignes de code. Exécutez la commande suivante pour l'installer depuis npm.

```
$ npm install -S aws-amplify && npm install -S aws-amplify-react
```

### C'est tout pour aujourd'hui

Le serverless computing nous offre des avantages tels que la réduction des coûts opérationnels et du temps de développement. Il nous permet de nous concentrer sur notre code pour fournir une valeur commerciale aux utilisateurs sans nous soucier de la construction et de la maintenance des serveurs.

AWS est l'un des nombreux fournisseurs de services de serverless computing. Il faut quelques étapes pour configurer et intégrer ces services, et AWS Amplify a été construit pour faciliter la construction d'applications serverless sur AWS. Il fournit des outils pour créer et configurer des services avec quelques commandes, et des composants de bibliothèque pour interagir facilement avec ces services depuis notre code.

Ceci est le premier article d'une série pour vous introduire à la construction d'applications serverless avec AWS Amplify. Nous avons configuré l'AWS Amplify CLI et créé un projet Amplify.