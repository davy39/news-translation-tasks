---
title: Comment déployer une application React + Node sur Heroku en 3 minutes sans
  la ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-07T21:04:32.000Z'
originalURL: https://freecodecamp.org/news/deploy-a-react-node-app-to
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/david-watkis-qtyGhwZOAbU-unsplash.jpg
tags:
- name: Heroku
  slug: heroku
- name: node
  slug: node
seo_title: Comment déployer une application React + Node sur Heroku en 3 minutes sans
  la ligne de commande
seo_desc: "By Mohammad Iqbal\nIn this tutorial we will be doing a basic React + Node\
  \ app deploy to Heroku. \nThere are a lot of tutorials that do this only using the\
  \ command line, so to change things up a bit, I will do it completely without the\
  \ command line. \nFo..."
---

Par Mohammad Iqbal

Dans ce tutoriel, nous allons effectuer un déploiement de base d'une application React + Node sur Heroku. 

Il existe de nombreux tutoriels qui le font uniquement en utilisant la ligne de commande, alors pour changer un peu les choses, je vais le faire complètement sans la ligne de commande. 

Pour des choses comme la génération d'applications React et Express, nous n'avons pas le choix et devons utiliser la ligne de commande. Pour tout le reste, nous utiliserons une interface graphique.

Je suppose également que vous avez un compte Github et Heroku. Ils sont tous les deux gratuits, donc pas de soucis pour s'inscrire.

Projet exemple : 
[https://github.com/iqbal125/react-express-](https://github.com/iqbal125/react-express-heroku)sample

## Installation de React et Express

Tout d'abord, commençons par créer deux répertoires nommés **Server** et **Client.** 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-80.png)

Le répertoire Client contiendra le contenu de la commande `create-react-app`, et Server contiendra le contenu de la commande `express`. Cette bibliothèque crée simplement une application Express pour nous automatiquement, similaire à `create-react-app`. Elle doit être installée globalement, ce que vous pouvez faire avec la commande :

`npm install -g express-generator`

Après cela, exécutez simplement ces commandes dans chacun des répertoires respectifs pour installer les projets de démarrage :

`npx create-react-app app1` dans le répertoire **Client**

`express` dans le répertoire **Server** 



Changez pour le répertoire **app1** généré par `create-react-app` et exécutez :

`npm run build`

Cela générera une version de build de production du projet qui est optimisée pour un déploiement de production, avec des éléments comme le code de gestion des erreurs et les espaces blancs supprimés.  

_Note :_ Dans une build de développement, vous utiliseriez un proxy vers **http://localhost:5000** pour communiquer de votre application React à votre serveur Express, mais ici l'application React et le serveur Express ne font qu'un seul projet. Le serveur Express sert les fichiers React.

Ensuite, coupez et collez l'intégralité du répertoire **build** dans le répertoire **Server**. La structure de votre projet devrait ressembler à ceci : 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-81.png)



Nous pouvons maintenant ajouter du code pour indiquer à notre serveur Express de servir notre projet React :

```javascript
....

app.use(express.static(path.join(__dirname, 'build')));


app.get('/*', (req, res) => {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

....

```

La première ligne de code sert tous nos fichiers statiques depuis le répertoire **build**. 

Le deuxième morceau de code est pour garder notre routage côté client fonctionnel. Ce code sert essentiellement le fichier `index.html` sur n'importe quelle route inconnue. Sinon, nous devrions réécrire tout notre routage pour qu'il fonctionne avec cette configuration de serveur Express. 

Pour tester votre application, exécutez simplement `npm start` dans le répertoire **Server** et allez sur **http://localhost:3000** dans le navigateur. Ensuite, vous devriez voir votre application React en cours d'exécution. 

Maintenant, nous sommes prêts à télécharger ce projet sur GitHub.

## GitHub 

Au lieu d'utiliser la ligne de commande pour télécharger sur GitHub, nous allons le faire avec l'interface graphique. Tout d'abord, allez sur la page d'accueil de GitHub et créez un nouveau dépôt. Nommez-le comme vous voulez, mais assurez-vous que l'option **Initialize this Repository with a README** est cochée :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-82.png)

Ensuite, téléchargez tous les fichiers du projet sans le répertoire **node_modules**. 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-83.png)

Cliquez sur commit et nous avons terminé. Vos fichiers de projet téléchargés apparaîtront sur GitHub comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-84.png)

Maintenant, nous pouvons passer à la configuration de Heroku.

## Heroku

Allez sur le tableau de bord Heroku, créez une nouvelle application et nommez-la comme vous le souhaitez. 

Ensuite, allez dans l'onglet Deploy et sélectionnez GitHub sous Deployment method :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-85.png)

Si vous n'avez pas encore connecté votre compte GitHub à votre compte Heroku, vous serez invité à le faire via le flux d'authentification GitHub. 

Après cela, recherchez votre projet sur GitHub et connectez-vous à celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-86.png)

Enfin, nous pouvons simplement déployer notre application en cliquant sur le bouton Deploy Branch : 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-87.png)

Heroku installera automatiquement tous les modules Node pour vous. Vous pouvez consulter votre projet en cliquant sur le bouton View. 

Et c'est tout, nous avons terminé ! Merci d'avoir lu. 



> Connectez-vous avec moi sur Twitter pour plus de mises à jour sur les futurs tutoriels : [https://twitter.com/iqbal125sf](https://twitter.com/iqbal125sf)