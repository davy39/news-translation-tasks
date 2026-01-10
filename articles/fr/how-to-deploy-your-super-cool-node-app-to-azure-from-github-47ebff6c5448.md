---
title: Comment déployer votre super application Node sur Azure depuis GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-25T14:36:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-super-cool-node-app-to-azure-from-github-47ebff6c5448
coverImage: https://cdn-media-1.freecodecamp.org/images/0*aZ3MaOUUJ11gKWAI
tags:
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment déployer votre super application Node sur Azure depuis GitHub
seo_desc: 'By Rohit Ramname

  Are you a Nodejs developer who loves developing wonderful apps as a hobby but needs
  some place to show it off?

  Are you a person fascinated by Azure and tempted to try it out?

  Are you also that person overwhelmed by the configurations...'
---

Par Rohit Ramname

Êtes-vous un développeur Node.js qui aime créer des applications merveilleuses en tant que hobby mais qui a besoin d'un endroit pour les montrer ?

Êtes-vous une personne fascinée par Azure et tentée de l'essayer ?

Êtes-vous aussi cette personne submergée par les configurations qu'offre Azure ?

Eh bien... aujourd'hui, je vais expliquer une méthode très simple pour mettre votre application en ligne et la faire fonctionner sur Azure en quelques clics.

> J'avais publié un [article](https://medium.freecodecamp.org/how-to-deploy-a-nodejs-app-to-heroku-from-github-without-installing-heroku-on-your-machine-433bec770efe) sur le déploiement d'une application Node "cool" sur Heroku depuis GitHub gratuitement. Mais maintenant que nous avons décidé de créer une application Node "super cool", nous allons utiliser un autre service cloud populaire sur le marché.

Assez de bavardages... passons maintenant aux choses sérieuses.

### **Étape 1 : Créer cette super application Node**

Créons d'abord cette super application Node.

Créez un dossier sur votre machine locale et donnez-lui un nom (au choix), par exemple MySuperCoolApp.

Ajoutez un fichier nommé package.json et collez le contenu ci-dessous. Ce fichier contient les informations de base de notre package. (Cela peut également être créé en tapant la commande npm init et en acceptant tous les paramètres par défaut.)

```
{"name": "supercoolnodeapp","version": "1.0.0","description": "super node app ","main": "app.js","scripts": {"start": "node app.js"},"repository": {"type": "git","url": ""},"author": "","license": "ISC","bugs": {"url": ""},"homepage": ""}
```

Un changement très important à noter est cette ligne :

```
"start": "node app.js"
```

**Après le déploiement, Azure exécutera cette commande pour démarrer votre application.**

Ajoutez un fichier, app.js, et collez le code ci-dessous. Ce sera le point de départ de notre application.

```
const http = require('http');
```

```
const port=process.env.PORT || 3000
```

```
const server = http.createServer((req, res) => {
```

```
res.statusCode = 200;
```

```
res.setHeader('Content-Type', 'text/html');
```

```
res.end('<h1>Hello World</h1>');
```

```
});
```

```
server.listen(port,() => {
```

```
console.log(`Server running at port `+port);
```

```
});
```

Ce code ouvre un port sur le serveur local et sert du HTML.

Veuillez noter le bloc de code **le plus important** ici :

```
const port=process.env.PORT || 3000
```

Cela est important lorsque vous souhaitez déployer votre application dans le cloud. Le serveur d'application est démarré sur un port aléatoire dans le cloud. Si vous codez en dur un numéro de port, comme dans tous les guides de démarrage, et que vous déployez dans le cloud, le numéro de port spécifique peut ne pas être disponible. L'application ne démarrera jamais. Il est donc préférable d'obtenir le numéro de port attribué par l'instance cloud et de démarrer le serveur HTTP.

Enregistrez le fichier et exécutez la commande suivante dans la fenêtre d'invite de commande (qui est ouverte dans le dossier) :

```
node app.js
```

Avec cela, Node démarrera le serveur et affichera le message suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/OaYZEqBsoUYIH9Rs5xcNtb1EVNrYkiZ0Miym)

Maintenant, si nous ouvrons [http://localhost:3000/](http://localhost:3000/) dans le navigateur, nous verrons ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/FGJ2ZtZHV08xBAiEHvt2AE-p7Gu0kk7PCXrT)

Cool ! Nous avons créé une application Node.js basique mais super cool.

### ÉTAPE 2 : Pousser vers GitHub

Maintenant, nous voulons télécharger notre code sur GitHub. De cette façon, nous pourrons modifier notre code de n'importe où et également déployer les modifications validées dans le cloud instantanément.

Créons un dépôt sur [GitHub](https://github.com/) en cliquant sur Nouveau dépôt.

Donnez-lui un nom, une description, et cliquez sur Créer un dépôt :

![Image](https://cdn-media-1.freecodecamp.org/images/Dflliq0Ssjp8H21RcQNJ7uDo17CFcQoJjK41)

GitHub créera un dépôt et vous donnera quelques commandes que vous pouvez exécuter localement afin de cloner votre dossier local avec votre dépôt GitHub.

Ouvrez l'invite de commande à l'intérieur de votre application où se trouve le fichier package.json. Dans l'invite de commande, exécutez les commandes suivantes dans cet ordre.

1. Initialisez le dépôt Git au niveau racine :

```
git init
```

2. Ajoutez tous les fichiers à votre Git local (staging). Remarquez le dernier point :

```
git add .
```

3. Validez vos modifications dans votre Git local :

```
git commit -m "first commit"
```

4. Liez à votre dépôt GitHub. (Veuillez changer l'URL pour pointer vers votre dépôt.)

```
git remote add origin https://github.com/rramname/MySuperCoolNodeApp.git
```

5. Et poussez votre changement :

```
git push --set-upstream origin master
```

Vous devriez voir des messages comme ci-dessous dans l'invite de commande.

![Image](https://cdn-media-1.freecodecamp.org/images/xlbyPaIeqLixxVDk2ruikLQJWBp5OCBn937H)

Maintenant, si vous ouvrez GitHub et actualisez le dépôt, vous devriez pouvoir voir le code.

### ÉTAPE 3 : Maintenant, mettons-le en ligne sur Azure

Cet exercice suppose que vous avez un abonnement Microsoft Azure configuré et prêt à l'emploi. Si vous n'en avez pas, vous pouvez en créer un gratuitement en allant sur le site [web](https://azure.microsoft.com/en-us/free/) de Microsoft Azure. Il vous demandera les informations de votre carte de crédit. Votre carte n'est jamais débité sauf si vous achetez des services payants (ce qui n'est pas nécessaire pour cette démonstration).

Ouvrez portal.azure.com et connectez-vous avec vos identifiants.

Cliquez sur Créer une nouvelle ressource en haut à gauche. Entrez "web app" dans la zone de recherche pour obtenir le type de ressource requis et appuyez sur Entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/IRuP2II13mElTOZKRDJP9tzRIsyz3yNoDtgz)

Sélectionnez Application Web dans les résultats de recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/xKvK6yiE7T4GjMuPbG2NUyhvWXI65mzo3aOx)

Et cliquez sur le bouton Créer.

Nous devrons fournir quelques informations de base pour cette application :

![Image](https://cdn-media-1.freecodecamp.org/images/R8n1urfiKFIyn3o7pdiwne5YYacxfk8n5KQa)

La première case est le nom de votre application. Ce qui est super facile puisque c'est SuperCoolNodeApp :)

La deuxième option est l'abonnement. Je me suis inscrit à l'abonnement "Pay As You Go" puisque j'ai déjà consommé mon essai gratuit. Vous pouvez sélectionner votre plan d'abonnement gratuit ici.

Ensuite, il y a le groupe de ressources. Il s'agit du regroupement logique de vos applications sur Azure. Vous pouvez en créer un nouveau pour cette application ou utiliser ceux existants. J'ai créé un nouveau pour cette application sous le nom SuperCoolNodeApp.

Enfin, vous devrez sélectionner le plan de service d'application. J'ai créé un plan gratuit avec le nom Test Plan. Vous pouvez créer un nouveau plan si vous n'en avez pas déjà un, mais assurez-vous de sélectionner une version gratuite. Lors de la sélection, Azure sélectionne automatiquement le niveau S1 qui n'est PAS GRATUIT. Assurez-vous de le changer en plan gratuit pour la démonstration (Bien sûr, si vous voulez des capacités supérieures, des puissances de traitement, etc., optez pour des plans payants.)

Cliquez sur **Créer.**

Azure mettra en file d'attente votre demande de création d'une application avec le plan de service que vous avez choisi et vous montrera une petite notification en haut. La création d'une application ne devrait pas prendre beaucoup plus de temps. Si vous actualisez votre page dans une minute ou deux, vous devriez pouvoir voir l'application et le plan de service qui ont été créés sous toutes les ressources.

![Image](https://cdn-media-1.freecodecamp.org/images/jvVtbEd9wkb65ZzXCDYbxWA7E6as235MIgYK)

Maintenant, cliquez dessus pour voir les détails de l'application que nous venons de créer.

![Image](https://cdn-media-1.freecodecamp.org/images/hwvCTMksJePPyGVPQZw6kHoD5WG40TqcmG98)

Il montre les détails comme l'abonnement sur lequel le plan est en cours d'exécution, le statut comme En cours d'exécution, l'ID d'abonnement, l'emplacement sur le serveur où l'application est hébergée "Centre des États-Unis" et quelques détails FTP. Mais la chose la plus importante ici est l'**URL**. C'est ce qui va être l'URL de notre application dans le cloud.

Maintenant, mettons-la là-bas...

> Un petit spoiler, :) Dans cette section, nous allons configurer la stratégie de déploiement pour notre application.

Faites défiler vers le bas et cliquez sur Options de déploiement.

![Image](https://cdn-media-1.freecodecamp.org/images/LvzIntREsWCJ4OC1KQLCg6sBKLsOPc2TrDzF)

Cliquez sur Configurer les paramètres requis et sélectionnez GitHub. Cela devrait vous montrer l'écran ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/bZWe8XsrmMX1603j3w9X1tieIuqXA1VHJk0I)

Cliquez sur Choisir un projet. Cela devrait vous montrer tous les dépôts de votre compte GitHub.

Si vous faites cela pour la première fois, vous devrez donner à Azure l'autorisation d'accéder à votre compte GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/UHTbvX9sAUnbe1nvRmXizZ5RCQecAIEZUhua)

Ici, vous sélectionnerez cette application MySuperCoolNodeApp que vous avez poussée vers GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/O-ESMvitVZTZscnqKDGbpBUiGljHYSK9fbsh)

Ensuite, nous pouvons sélectionner la branche que nous voulons déployer.

Pour l'instant, je n'ai que master, donc je laisse celle par défaut.

Et c'est tout. Cliquez sur OK.

Azure se chargera de déployer l'application. Il vous montrera même cette petite notification indiquant qu'Azure est en train de faire ce travail.

![Image](https://cdn-media-1.freecodecamp.org/images/-gDgrCkxjoXyWLE1h4Pt0GP-FPIYpMz6vdD0)

Lorsque c'est terminé (ce qui ne devrait vraiment pas prendre trop de temps), cliquez à nouveau sur les options de déploiement. Vous devriez pouvoir voir le dernier déploiement.

![Image](https://cdn-media-1.freecodecamp.org/images/DLvCpf8QopyXPYctNRFuKKZg5F-j0NFGfA-J)

Si vous cliquez sur l'enregistrement, Azure vous montrera même le journal de l'événement de déploiement.

![Image](https://cdn-media-1.freecodecamp.org/images/YaMWtBP1Dnhm1YTJRblCMkfQ771LFCtlEwSy)

Cool. Maintenant, si vous ouvrez votre application en allant à l'URL mentionnée dans la section vue d'ensemble [https://supercoolnodeapp.azurewebsites.net/](https://supercoolnodeapp.azurewebsites.net/), vous vous attendez à voir le message Hello World mais au lieu de cela, vous voyez l'erreur ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/5IC41g7t6GGlnWv4j2BcDVg8mjE1bAhULljB)

Huh... qu'est-ce qui ne va pas ? Les journaux montrent que l'application a été déployée, vous ne voyez aucune erreur, mais l'application ne fonctionne pas. C'est un mystère.

Il y a un petit paramètre que vous devez faire sur le portail Azure pour aider Azure à le traiter comme une application Node.js et à le démarrer en conséquence.

Ouvrez les paramètres de l'application et faites défiler jusqu'à la section des paramètres de l'application et ajoutez l'entrée ci-dessous.

```
Nom du paramètre de l'application : WEBSITE_NODE_DEFAULT_VERSION
```

```
Valeur : 8.9.0
```

![Image](https://cdn-media-1.freecodecamp.org/images/dfrlxCgAqbmC-DiTUnZIRxwdFZygW1iyfkMp)

Cela indique essentiellement à Azure d'utiliser cette version de Node et d'ouvrir le site web.

Cliquez sur Enregistrer en haut.

Maintenant, si vous allez à l'URL [https://supercoolnodeapp.azurewebsites.net/](https://supercoolnodeapp.azurewebsites.net/)

![Image](https://cdn-media-1.freecodecamp.org/images/s3uN-mKHfI8qyZpU8JR2IHpdZ2OmwL7cjPRJ)

WOOHOO!!! C'est fait. Nous venons de mettre notre super application Node en ligne et de la faire fonctionner sur Azure.

Félicitations!! Maintenant, chaque fois que vous apportez une modification à votre application et que vous la poussez vers GitHub, Azure les détectera et effectuera le déploiement continu.

P.S : Si vous construisez un jour une application plus cool que la mienne :), alors n'hésitez pas à la partager.

Si cet article vous a aidé, j'adore les applaudissements ici et les connexions sur Twitter :)

> Je n'écris que sur la programmation et la technologie sur [Twitter](https://twitter.com/@rramname).

Amusez-vous bien!!