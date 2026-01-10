---
title: Comment déployer votre application Node.js gratuitement avec Render
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2022-09-01T16:08:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-nodejs-application-with-render
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-pixabay-163235--1-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
- name: React
  slug: react
seo_title: Comment déployer votre application Node.js gratuitement avec Render
seo_desc: "For years, Heroku has been an excellent platform to host your Full Stack\
  \ applications. freeCodeCamp made heavy use of Heroku early on – as have countless\
  \ open source projects. \nBut that may change, as Heroku is bringing its generous\
  \ free tier to an e..."
---

Pendant des années, Heroku a été une excellente plateforme pour héberger vos applications Full Stack. freeCodeCamp a largement utilisé Heroku dès le début – tout comme d'innombrables projets open source. 

Mais cela pourrait changer, car Heroku met fin à son généreux niveau gratuit.

Vous avez peut-être reçu un email de Heroku vous informant que, à partir du 28 novembre 2022, vous ne pourrez plus héberger d'application gratuitement sur la plateforme, et que vous devrez maintenant acheter un plan payant.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/no_free_heroku.png)

Si vous souhaitez héberger des sites web statiques ou des webapps gratuitement, vous pouvez utiliser [Netlify](https://www.netlify.com/) comme je l'ai expliqué dans [cet article](https://www.freecodecamp.org/news/how-to-deploy-react-router-based-app-to-netlify/) mais pour les applications backend. Cela dit, il n'y a pas beaucoup de plateformes gratuites qui offrent la même sensation et la même facilité de déploiement que Heroku.

Donc dans cet article, nous allons apprendre à déployer votre application Node.js avec un serveur Express sur [Render](https://render.com/). C'est une alternative gratuite à Heroku avec un processus de déploiement similaire et facile.

Alors, commençons.

## Que faire avant de déployer votre application

Comme vous le savez peut-être de votre expérience avec Heroku, chaque application déployée s'exécute sur un port spécifique que Heroku attribue aléatoirement. Vous pouvez y accéder en utilisant la variable `process.env.PORT`.

Il en va de même avec la plateforme Render.

Vous devez donc vous assurer que, au lieu de fournir une valeur de port codée en dur pour démarrer votre serveur Express, vous utilisez la variable `process.env.PORT` comme ceci :

```js
const express = require("express");
const app = express();
const PORT = process.env.PORT || 3030;

// votre code

app.listen(PORT, () => {
  console.log(`serveur démarré sur le port ${PORT}`);
});

```

## **Comment déployer une application sur Render à partir d'un dépôt GitHub**

Maintenant, une fois que vous avez effectué la modification liée au port, il est temps de déployer votre application.

J'ai déjà [ce dépôt GitHub](https://github.com/myogeshchavan97/github-repos-nodejs-api) que je vais déployer sur Render. Le code de ce dépôt GitHub affiche simplement la liste des principaux dépôts et le nombre d'étoiles pour chaque dépôt au format JSON.

Alors, commençons.

[Render](https://render.com/) propose diverses façons de s'inscrire comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/sign_up_render.png)

Une fois inscrit et connecté à votre compte, vous verrez un tableau de bord comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/dashboard.png)

Pour déployer une application Node.js, cliquez sur le bouton `New Web Service` sous l'option `Web Services`.

Vous pouvez également cliquer sur le bouton `New +` affiché dans l'en-tête juste avant votre photo de profil et sélectionner l'option `Web Service`.

Une fois cliqué, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/new_web_service.png)

Cliquez sur le bouton `Connect account` affiché sur le côté droit sous le menu GitHub. Une fois cliqué, vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/install_render.png)

Cliquez sur le lien `Configure` et vous pouvez donner la permission de sélectionner tous vos dépôts GitHub ou seulement des dépôts sélectionnés.

Je préfère donner accès uniquement aux dépôts sélectionnés que je souhaite déployer actuellement. J'ai donc sélectionné l'option `Only select repositories`. 

Ensuite, cliquez sur le bouton `Select repositories` affiché sous l'option et sélectionnez le dépôt GitHub que vous souhaitez déployer.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/connect_github.png)

Une fois sélectionné, vous verrez l'écran suivant affichant le dépôt sélectionné.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/selected_repository.png)

Cliquez sur le bouton vert `Install` pour donner accès au dépôt sélectionné au site Render.

Une fois cliqué, vous serez redirigé vers votre tableau de bord où vous verrez votre dépôt sélectionné comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/connected_repository.png)

Maintenant, cliquez sur le bouton `Connect` et vous verrez l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/deploy_details.png)

Ici, pour le champ `Name`, entrez un nom court et simple pour identifier votre site web.

**Note :** gardez la valeur `Name` simple car elle deviendra l'URL de votre application une fois l'application déployée. Donc si j'entre `github-repos` comme valeur pour `Name`, l'URL de mon application deviendra [`https://github-repos.onrender.com`](https://github-repos.onrender.com). 

Assurez-vous donc d'entrer une valeur courte et significative pour `Name`.

Entrez les détails comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/details.png)

Pour `Build Command`, entrez `yarn` comme valeur, ce qui est équivalent à la commande `yarn install`. Yarn est un gestionnaire de paquets similaire à npm mais plus rapide que npm.

Et pour `Start Command`, entrez `node index.js` comme valeur, si votre fichier d'entrée est `index.js`.

Après avoir entré tous les détails, faites défiler vers le bas et vous verrez la section `Plans` où votre plan gratuit sera automatiquement sélectionné. Si ce n'est pas le cas, vous devez le sélectionner car nous déployons l'application gratuitement.

Si vous faites défiler un peu plus bas, vous verrez un bouton `Advanced`.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/advanced_options.png)

Si votre application utilise des variables d'environnement, vous pouvez les entrer dans les paramètres `Advanced` comme montré ci-dessous. Vous pouvez également ajouter vos fichiers `.env` pour ne pas avoir à les entrer manuellement un par un.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/env_vars-1.png)

Notez que le champ `Auto-Deploy` a une valeur par défaut de `Yes` – donc une fois que vous poussez vos modifications de code vers le dépôt GitHub, elles seront automatiquement déployées sur Render.

Si vous ne souhaitez pas déployer automatiquement vos modifications à chaque changement de code poussé vers votre dépôt GitHub, vous pouvez sélectionner la valeur `No` dans le menu déroulant `Auto-Deploy`.

Maintenant, vous pouvez cliquer sur le bouton `Create Web Service` pour démarrer le processus de déploiement.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/10-1.png)

Attendez un moment jusqu'à ce que le déploiement soit en cours. Parfois, vous devrez peut-être actualiser la page si vous voyez le message "en cours" pendant longtemps.

Une fois le déploiement terminé, vous verrez que votre application est déployée `Live` comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/11.png)

Vous pouvez cliquer sur l'URL de l'application déployée qui est affichée en haut comme montré dans la capture d'écran ci-dessus. Dans mon cas, l'URL de l'application est [https://github-repos.onrender.com/](https://github-repos.onrender.com/).

Lorsque vous déployez l'application pour la première fois, vous pourriez voir une erreur `Page is not working` lorsque vous essayez d'accéder à votre site déployé.

Attendez un peu et continuez à actualiser la page en utilisant `Ctrl + R` ou `Cmd + R (Mac)`. Parfois, la plateforme Render prend un certain temps pour démarrer l'application car nous utilisons un service gratuit avec du matériel limité.

Une fois déployée, vous verrez votre application déployée comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/deployed_live.png)

**Astuce :** Pour voir le JSON tel qu'il est formaté ci-dessus, vous pouvez installer l'extension Chrome [JSON Formatter](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en).

Comme vous le savez peut-être, lorsque vous utilisez Heroku avec un compte gratuit, votre application passe en mode veille après 30 minutes si aucune requête n'est reçue pour l'application. Cela signifie qu'il faut un certain temps pour charger l'application lorsque la prochaine requête arrive.  
  
De même, dans le cas de Render, votre application passera en mode veille après 15 minutes s'il n'y a pas de requêtes pour l'application.

### **Merci d'avoir lu !**

Vous pouvez trouver le code source complet de l'application déployée sur GitHub dans [ce dépôt](https://github.com/myogeshchavan97/github-repos-nodejs-api).

**Vous pouvez voir la démonstration en direct de l'application déployée [ici](https://github-repos.onrender.com/).**

Si vous souhaitez apprendre Redux en détail à partir de zéro et construire 3 applications ainsi que l'application [complete food ordering app](https://www.youtube.com/watch?v=2zaPDfCKAvM), consultez mon cours [Mastering Redux](https://master-redux.yogeshchavan.dev/).

Dans le cours, vous apprendrez :

* Redux de base et avancé
* Comment gérer l'état complexe des tableaux et des objets
* Comment utiliser plusieurs réducteurs pour gérer l'état complexe de Redux
* Comment déboguer une application Redux
* Comment utiliser Redux dans React en utilisant la bibliothèque react-redux pour rendre votre application réactive.
* Comment utiliser la bibliothèque redux-thunk pour gérer les appels API asynchrones
* Construire 3 applications différentes en utilisant Redux

et bien plus encore.

Enfin, nous construirons une application complète de [commande de nourriture](https://www.youtube.com/watch?v=2zaPDfCKAvM) à partir de zéro avec l'intégration de Stripe pour accepter les paiements et la déployer en production.

**Vous souhaitez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**