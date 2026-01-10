---
title: Comment déployer une application NodeJS sur Heroku depuis GitHub (sans installer
  Heroku sur votre machine)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-29T18:56:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-nodejs-app-to-heroku-from-github-without-installing-heroku-on-your-machine-433bec770efe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6YaRlBgzJa17RRM9
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment déployer une application NodeJS sur Heroku depuis GitHub (sans
  installer Heroku sur votre machine)
seo_desc: 'By Rohit Ramname

  As a web developer, nothing is more satisfying that being able to show (and show
  off) your work to the word. Not only through the images or videos on Twitter, but
  letting them actually interact with it — especially if you are working...'
---

Par Rohit Ramname

En tant que développeur web, rien n'est plus satisfaisant que de pouvoir montrer (et montrer) votre travail au monde. Non seulement à travers les images ou vidéos sur Twitter, mais en laissant les autres interagir avec lui — surtout si vous travaillez sur des projets secondaires sympas ou si vous postulez pour un poste.

Et heureusement, maintenant avec tous les fournisseurs de cloud, partager votre travail est une nécessité et une étape de base dans votre parcours.

Dans ce tutoriel, nous allons voir comment déployer votre application NodeJS sympa sur Heroku. À la fin de ce tutoriel, nous aurons une application basique Hello World en cours d'exécution sur un domaine public accessible par tous.

Pour ce tutoriel, je suppose que vous avez Node installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger depuis le site [Nodejs.org](https://nodejs.org/en/). Les étapes sont simples et peuvent être trouvées [en ligne](https://www.wikihow.com/Install-Node.Js-on-Windows) facilement.

Vous aurez également besoin d'un compte GitHub pour héberger notre code en ligne. Si vous n'avez pas de compte, vous pouvez en créer un gratuitement sur [Github.com](https://github.com/). Avec un compte gratuit, vous pouvez créer des dépôts publics illimités. Nous utiliserons le système de contrôle de version Git pour pousser nos modifications vers GitHub.

### **ÉTAPE 1 : Créer cette application sympa**

Maintenant, créons cette application Node sympa à laquelle vous avez pensé.

Créez un dossier sur votre machine locale et donnez-lui un nom (de votre choix), par exemple MyCoolApp.

Ajoutez un fichier nommé package.json et collez le contenu ci-dessous. Ce fichier contient les informations de base de notre package. (Cela peut également être créé en tapant la commande npm init et en acceptant tous les paramètres par défaut.)

```json
{
  "name": "coolnodeapp",
  "version": "1.0.0",
  "description": "application node",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "repository": {
    "type": "git",
    "url": ""
  },
  "author": "",
  "license": "ISC",
  "bugs": {
    "url": ""
  },
  "homepage": ""
}
```

Un changement très important à noter est cette ligne :

```bash
"start": "node app.js"
```

**Après le déploiement, Heroku exécutera cette commande pour démarrer votre application.**

Ajoutez un fichier, app.js, et collez le code ci-dessous. Ce sera le point de départ de notre application.

```js
const http = require('http');
const port = process.env.PORT || 3000

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end('<h1>Hello World</h1>');
});

server.listen(port,() => {
  console.log(`Serveur en cours d'exécution sur le port `+port);
});
```

Ce code ouvre essentiellement un port sur le serveur local et sert du HTML.

Veuillez noter le bloc de code **le plus important** ici :

```js
const port = process.env.PORT || 3000
```

Cela est extrêmement important lorsque vous souhaitez déployer votre application dans le cloud. Le serveur d'application est démarré sur un port aléatoire dans le cloud. Si vous codez en dur un numéro de port, comme dans tous les guides de démarrage, et que vous déployez dans le cloud, le numéro de port spécifique peut ne pas être disponible. L'application ne démarrera jamais. Il est donc préférable d'obtenir le numéro de port attribué par l'instance cloud et de démarrer le serveur HTTP.

Enregistrez le fichier et exécutez la commande suivante dans la fenêtre d'invite de commande (qui est ouverte à l'intérieur du dossier) :

```bash
node app.js
```

Avec cela, Node démarrera le serveur et affichera le message suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/e8L6vy5EQXp5av7XM0dnQ1UJ1ujUNKWg9x80)

Maintenant, si nous ouvrons [http://localhost:3000/](http://localhost:3000/) dans le navigateur, nous verrons ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/tboqj1yfKFq8Plt2iMGQtI8ELMz2wmokZ4N9)

Super ! Nous venons de créer une application NodeJs basique.

### **ÉTAPE 2 : Pousser vers GitHub**

Maintenant, nous voulons télécharger notre code sur GitHub. De cette façon, nous pourrons éditer notre code de n'importe où et également déployer les modifications validées dans le cloud instantanément.

Créons un dépôt sur [GitHub](https://github.com/) en cliquant sur Nouveau dépôt.

Donnez-lui un nom, une description et cliquez sur Créer un dépôt :

![Image](https://cdn-media-1.freecodecamp.org/images/ErZ9uAGixHBqPU8Ycm35oP4MefF10W4-rot4)

GitHub créera un dépôt et vous donnera quelques commandes que vous pouvez exécuter localement afin de cloner votre dossier local avec votre dépôt GitHub.

![Image](https://cdn-media-1.freecodecamp.org/images/0Iev7eGUvXGm7aTOo9Qb8jiUMYN7tc44uUdE)

Dans l'invite de commande, exécutez les commandes suivantes dans cet ordre.

1. Initialisez le dépôt Git au niveau racine :

```bash
git init
```

2. Ajoutez tous les fichiers à votre Git local (staging). Remarquez le dernier point :

```bash
git add . 
```

3. Validez vos modifications dans votre Git local :

```bash
git commit -m "premier commit"
```

4. Liez à votre dépôt GitHub. (Veuillez changer l'URL pour pointer vers votre dépôt.)

```bash
git remote add origin https://github.com/rramname/MyCoolNodeApp.git
```

5. Et poussez votre modification :

```bash
git push --set-upstream origin master
```

Vous devriez voir des messages comme ci-dessous à l'invite de commande.

![Image](https://cdn-media-1.freecodecamp.org/images/KYLZUjqsIYpGDn45YmePQG1l1r771AypiRfb)

Maintenant, si vous ouvrez GitHub et actualisez le dépôt, vous devriez pouvoir voir le code.

![Image](https://cdn-media-1.freecodecamp.org/images/1A8PaQtHzEJDMvJm2oCbplcpvOR30AIYyaSP)

### **ÉTAPE 3 : Déployer sur Heroku**

Maintenant vient le moment amusant, la raison pour laquelle vous avez survécu à tout cela : le déploiement.

Si vous n'avez pas de compte avec Heroku, vous pouvez en ouvrir un gratuitement en remplissant ce [formulaire simple](https://signup.heroku.com/login). (Et ici, vous n'avez pas besoin de fournir d'informations sur la carte de crédit :) )

![Image](https://cdn-media-1.freecodecamp.org/images/375W2miDv-0ou4ZkP5Y3cyrrfapKcLksdBeY)

Une fois que votre compte est prêt, connectez-vous avec vos identifiants.

Cliquez sur Nouveau dans le coin supérieur droit et sélectionnez « Créer une nouvelle application ».

Donnez un nom à votre application (celui-ci sera inclus dans l'URL publique de votre application) et cliquez sur Créer une application.

Cette étape vous amènera au tableau de bord de votre application. Ouvrez l'onglet Déployer et faites défiler jusqu'à la section « Méthode de déploiement ».

Sélectionnez GitHub comme méthode.

Il affichera une option « Se connecter à GitHub » où nous pouvons fournir notre dépôt GitHub. Si vous le faites pour la première fois, Heroku demandera la permission d'accéder à votre compte GitHub.

Ici, vous pouvez rechercher votre dépôt GitHub et cliquer sur connecter :

![Image](https://cdn-media-1.freecodecamp.org/images/ylaZsAuah1udMDvouTIQLmzLDKJX9FrC23yB)

Si Heroku est en mesure de trouver et de se connecter au dépôt GitHub, la section Déploiement s'affichera où vous pourrez sélectionner si vous souhaitez un déploiement automatique (dès que les modifications sont poussées vers GitHub, Heroku les récupérera et les déployera) ou un déploiement manuel.

![Image](https://cdn-media-1.freecodecamp.org/images/PPD75YeIqpQs-R2pFcjyRmfvZwNQWvrAH6CM)

Cliquez sur Activer les déploiements automatiques (parce que c'est moins de travail pour les applications de démonstration :) ). Vous pouvez également sélectionner la branche GitHub si nécessaire, mais pour cette démonstration, nous déployerons depuis la branche master.

Maintenant, nous devons dire à Heroku que notre application est une application NodeJs. Pour cela, nous aurons besoin du buildpack NodeJs.

Ouvrez l'onglet Paramètres et localisez les Buildpacks et cliquez sur **"Ajouter un buildpack".**

![Image](https://cdn-media-1.freecodecamp.org/images/C-eFABZoiiKs2MJMPfWNSFaALNH2mLeIlmlN)

Sélectionnez **nodejs** parmi les options et cliquez sur Enregistrer les modifications.

Maintenant, retournez à l'onglet Déployer et cliquez sur **Déployer la branche** en bas.

Heroku prendra le code et l'hébergera. Ouvrez l'onglet Activité et vous pourrez voir la progression :

![Image](https://cdn-media-1.freecodecamp.org/images/P8kVjkwamaoyks8E0LalLAFspxTir0FtJOwX)

![Image](https://cdn-media-1.freecodecamp.org/images/0zV4RWDevunNPKRv6cgLD0Xk7swy4YJAFJ2Q)

Et c'est tout !

Ouvrez l'onglet **paramètres** et faites défiler jusqu'à la section **Domaines et certificats**. Ici, vous pouvez voir l'URL de votre application qui vient d'être déployée. Copiez et collez cette URL dans le navigateur et... Hourra !

![Image](https://cdn-media-1.freecodecamp.org/images/UMOjVBMZNmFpIhOz4uuqwOqIntxBUlSpEGVt)

Nous venons de créer notre propre application web accessible via Internet.

Super !

N'hésitez pas à la partager avec les autres !

Bon hébergement :)