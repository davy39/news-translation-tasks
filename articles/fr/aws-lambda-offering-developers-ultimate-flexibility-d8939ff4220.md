---
title: Voici trois façons courantes de créer vos fonctions Lambda avec AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-15T09:04:40.000Z'
originalURL: https://freecodecamp.org/news/aws-lambda-offering-developers-ultimate-flexibility-d8939ff4220
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JuAJNrCky6mkF4upt0emCg.png
tags:
- name: automation
  slug: automation
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Voici trois façons courantes de créer vos fonctions Lambda avec AWS
seo_desc: 'By Sam Williams

  AWS Lambda functions are incredible! They’re functions that are hosted on Amazon
  Web Services that can be triggered in many different ways.

  One of the best parts is that you only pay for the time the Lambda function is running.
  Got so...'
---

Par Sam Williams

Les fonctions AWS Lambda sont incroyables ! Ce sont des fonctions hébergées sur Amazon Web Services qui peuvent être déclenchées de nombreuses manières différentes.

L'un des meilleurs aspects est que vous ne payez que pour le temps pendant lequel la fonction Lambda est en cours d'exécution. Vous avez quelque chose qui ne s'exécute qu'une fois par heure et ne prend que 2 secondes ? Vous ne serez facturé que pour 48 secondes par jour ! C'est incroyable comparé à l'exécution d'une instance AWS EC2 24/7 ou de votre propre serveur privé.

Aujourd'hui, nous allons créer une fonction Lambda et examiner les trois meilleures façons de travailler avec le code.

### Création d'une fonction Lambda

Une fois votre compte AWS configuré, il existe plusieurs façons de créer une nouvelle fonction Lambda. Nous allons utiliser la console AWS.

#### Console AWS

Dans la console AWS, vous pouvez trouver AWS Lambda sous Services, ce qui vous mène à la console Lambda.

![Image](https://cdn-media-1.freecodecamp.org/images/1*23UBDu9eiNn9CasvX9dUqg.png)

Voici ce que vous verrez si c'est votre première Lambda. Cliquez sur ce bouton **Créer une fonction** pour commencer à configurer votre première fonction.

Vous arriverez sur la page de configuration où vous configurez certains aspects de la fonction (nom, runtime, rôle). Vous pouvez créer une Lambda à partir de Blueprints ou de Serverless Application Repos, mais dans cet exemple, nous allons l'écrire à partir de zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmKCKMsIPuMLhgsMxNMBog.png)

Entrez le nom de votre fonction (celui-ci doit être unique pour votre utilisateur ou sous-compte), choisissez votre Runtime (nous utiliserons Node.js 8.10), et sélectionnez un rôle.

Vous devrez créer un nouveau rôle si vous n'en avez pas déjà un. Créez-en un à partir d'un modèle et vous pouvez laisser **Policy templates** vide.

### Écriture du code de votre fonction Lambda

L'un des grands avantages des Lambdas est que vous pouvez choisir comment vous les écrivez et les éditez. Il existe trois principales façons de le faire :

* Console Lambda
* Cloud9
* Sur votre machine locale

Je vais couvrir les trois et discuter des avantages et des inconvénients pour chacune d'entre elles.

### Méthode 1 : Console Lambda

Voici l'écran auquel vous avez été redirigé lorsque vous avez créé la fonction. Vous verrez qu'il y a beaucoup de choses qui se passent. La partie qui nous intéresse pour l'instant est la section **Code de la fonction**, à peu près à mi-chemin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VxeSaa8uQgP92Wl4zCPMUg.png)

Ici, nous avons un éditeur de base. Je crois qu'il est basé sur l'IDE Cloud 9 et fonctionne plutôt bien pour les fonctions Lambda simples. Vous pouvez voir ci-dessous que le handler est une fonction asynchrone parce que j'ai choisi d'utiliser Node 8.10. Si vous préférez les callbacks, alors Node 6.10 est le runtime qu'il vous faut.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ukr1dY8xL4mT2IIEw0DVZg.png)

#### **Les avantages**

* C'est un éditeur décent.
* Vous pouvez y accéder depuis n'importe quel ordinateur via votre console AWS.

#### **Les inconvénients**

* Il ne semble pas être stable à 100 %. Parfois, il ne vous permet pas de sauvegarder, donc vous devez copier tout votre travail dans un fichier local, recharger la page et recopier votre travail. J'espère que cela sera bientôt corrigé !
* Il n'a pas de terminal. Cela signifie que vous ne pouvez pas installer de packages en utilisant NPM avec cette méthode seule.

### Méthode 2 : Éditeur Cloud9

Amazon a récemment acquis Cloud9, une plateforme de développement en ligne. Il semble exécuter une version très basique d'Ubuntu qui est intégrée au reste de la plateforme AWS.

Recherchez **Cloud9** dans la console AWS, allez sur la page et sélectionnez **Créer un environnement**. À partir de là, donnez un nom à votre environnement et passez à l'étape suivante.

Ici, vous pouvez choisir ce sur quoi vous voulez exécuter cet environnement. Le point positif est que t2.micro est éligible pour le niveau gratuit, donc vous pouvez utiliser cette méthode sans être facturé si vous êtes sur le niveau gratuit. Je n'ai jamais eu besoin de quelque chose de plus puissant qu'un t2.micro.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mIMSy6hKCQuer20ZOTjVSQ.png)

Continuez à partir de là et vous arriverez dans votre nouvel environnement Cloud9 !

![Image](https://cdn-media-1.freecodecamp.org/images/1*uaTpBEey0EHYd-_aWa165g.png)

Le point intéressant ici est que vous avez accès à toutes vos fonctions Lambda depuis votre environnement Cloud9. Cliquez sur **Ressources AWS** et sous **Fonctions distantes**, vous trouverez toutes vos fonctions. Cliquez sur la fonction Lambda que vous souhaitez modifier, puis cliquez sur l'icône de téléchargement ci-dessus pour l'importer dans votre environnement.

Une fois cela fait, ce sera comme si vous travailliez localement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P2Y6g3Juw5T7lltbooxhbg.png)

Une fois que vous avez terminé, sélectionnez simplement la fonction sur laquelle vous avez travaillé dans la liste locale et cliquez sur le bouton de téléchargement. En quelques secondes, elle sera en ligne avec toutes vos modifications.

#### **Les avantages**

* Encore une fois, tout cela est à distance, donc vous n'avez pas à vous soucier d'oublier de valider votre travail ou de l'enregistrer sur une clé USB si vous travaillez sur plusieurs machines.
* Obtenir vos fonctions et les télécharger est super facile. C'est de loin le meilleur aspect de cette méthode.
* Vous avez maintenant un terminal intégré, ce qui vous permet d'installer des packages npm et de faire tout ce que vous voulez faire en utilisant le terminal.

#### **Les inconvénients**

* Il présente toujours les mêmes problèmes de stabilité que l'éditeur Lambda. J'ai eu plusieurs occasions où j'ai essayé d'enregistrer la fonction mais je n'ai pas pu, devant copier en local, rafraîchir et recopier dans Cloud 9. Après quelques fois, j'ai abandonné et je suis passé à l'édition locale.

### Méthode 3 : Édition locale

Je vais faire celle-ci un peu différemment, je vais lister les avantages et les inconvénients puis vous montrer comment la rendre bien meilleure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XMS7swq0ptF24er7L0fgmg.png)

#### **Les avantages**

* L'édition locale est la façon dont la plupart des développeurs travaillent. Nous pouvons utiliser notre IDE préféré, nos extensions et nos schémas de couleurs.
* C'est stable (tant que votre ordinateur l'est).

#### **Les inconvénients**

* Il n'y a pas de bouton fantaisiste pour obtenir et télécharger votre travail sur AWS.
* Votre travail est local, donc avoir plusieurs utilisateurs ou simplement travailler sur plusieurs appareils est plus complexe.

#### Astuces d'édition locale

Parce que les avantages de cette méthode sont si attrayants (ou les inconvénients des autres méthodes sont si affreux), nous allons utiliser quelques solutions de contournement de base. Cela devrait prendre environ 15 minutes pour configurer tout ce dont nous avons besoin !

#### AWS CLI

Pour télécharger notre travail sur AWS, nous pouvons utiliser l'AWS CLI. Cela nous permet de télécharger un fichier zip sur notre compte AWS qui remplit une Lambda donnée.

Pour ce faire, nous devons d'abord configurer AWS CLI. Vous pouvez l'installer en utilisant [ce tutoriel](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) ou en tapant `npm install -g aws-cli` dans votre terminal. Maintenant, nous devons configurer un utilisateur pour que notre CLI se connecte.

Dans la gestion IAM, cliquez sur **Ajouter un utilisateur**, donnez un nom à l'utilisateur et sélectionnez **Accès programmatique**. Cela nous permettra d'agir en tant qu'utilisateur à distance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LkB76XZZwPt6soPHPtWlCQ.png)

Dans l'écran des permissions, choisissez **Attacher des politiques existantes directement** et sélectionnez **AdministratorAccess**. Cela vous permettra de faire tout ce que vous voulez via votre CLI. Vous pouvez définir des politiques plus strictes pour cet utilisateur si vous le souhaitez, ou si cela est pour une autre personne à accéder.

Il y a un autre écran avant que vous ne voyiez vos clés d'accès. Copiez vos clés d'accès et ouvrez un terminal. Exécutez la commande `aws configure` qui vous demandera 4 choses.

```
AWS Access Key ID [None]: "Votre ID de clé d'accès"AWS Secret Access Key [None]: "Votre clé d'accès secrète"Default region name [eu-west-1]:Default output format [json]:
```

Les deux premiers se trouvent sur la dernière page de la création de l'utilisateur et les deux suivants peuvent être laissés par défaut ou changés en ce que vous voulez.

#### Utilisation de l'AWS CLI

Maintenant que nous avons configuré le CLI, nous pouvons l'utiliser pour rendre notre vie beaucoup plus facile. Si vous avez un dossier avec une fonction Lambda stockée dedans, nous pouvons exécuter quelques commandes simples pour la télécharger sur AWS.

```
cd MyLambdaFunctionrm index.zipzip –X –r ./index.zip *aws lambda update-function-code     --function-name MyLambdaFunction     --zip-file fileb://index.zipcd ..
```

#### Script de construction AWS CLI

C'est bien, mais taper tout cela à chaque fois que vous voulez télécharger une nouvelle version de Lambda deviendrait fastidieux. Nous allons donc utiliser un script de construction.

Pour que ce script exact fonctionne, vous devez avoir une structure de dossiers comme celle-ci. Chaque lambda a un dossier avec les fichiers pertinents et un fichier region.txt.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XEed7aP1zbg6CyB3B8maWA.png)

Ce script non seulement exécute les commandes de base de l'AWS CLI, mais il effectue également des vérifications supplémentaires, exécute `npm install`, et affiche les détails sur la progression.

Cela peut sembler un script complexe, mais il peut être facilement décomposé. Les 32 premières lignes se déplacent dans le dossier de la fonction Lambda, exécutent `npm install` et vérifient que AWS CLI est installé. La ligne 38 zippe le dossier, à l'exception de certains fichiers, et la ligne 42 télécharge le fichier zip.

Maintenant, tout ce que vous avez à faire est de naviguer jusqu'au dossier principal où se trouve la fonction Lambda et d'exécuter

```
./build.sh example-lambda
```

Ce script pourrait être modifié et étendu pour inclure le téléchargement spécifique à une région, le téléchargement par lots de plusieurs fonctions Lambda ou l'intégration Git.

#### Git

La plupart des personnes qui lisent ceci utilisent Git au quotidien. Il y a une raison à cela : cela simplifie la vie.

Avoir un dépôt Git pour toutes vos fonctions Lambda est un excellent moyen de travailler avec des équipes de développeurs ou par vous-même sur plusieurs machines.

### Résumé

Il existe trois façons courantes d'éditer les fonctions Lambda : dans la console Lambda, Cloud 9 et localement.

Chacune des trois méthodes présente des avantages et des inconvénients, mais personnellement, je pense que le meilleur choix est d'écrire la fonction localement et de la déployer à l'aide d'un script de déploiement.

Si vous avez trouvé cet article utile, donnez-lui quelques applaudissements et suivez-moi pour plus de tutoriels AWS et d'articles pour développeurs !

SUIVANT ▶ [Dites bonjour à votre propre chatbot Amazon Lex](https://tutorials.botsfloor.com/say-hello-to-your-own-amazon-lex-chat-bot-9f22e7a0f9b0)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-leQk1ik68WjLB__Vc9IXw.gif)