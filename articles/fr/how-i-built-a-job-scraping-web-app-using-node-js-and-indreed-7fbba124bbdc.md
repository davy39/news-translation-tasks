---
title: Comment j'ai construit une application web de scraping d'emplois en utilisant
  Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-11T17:13:07.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-job-scraping-web-app-using-node-js-and-indreed-7fbba124bbdc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AFP5e1igLlHtks_byLj1uA.jpeg
tags:
- name: jobs
  slug: jobs
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai construit une application web de scraping d'emplois en utilisant
  Node.js
seo_desc: 'By Oyetoke Tobi Emmanuel

  Scraping jobs from the web has now become easier thanks to Indreed.

  About Indreed

  Indreed is a Rest API for scraping jobs from Indeed and around the web. It is powered
  by my personal web scraping project and layered on a rest...'
---

Par Oyetoke Tobi Emmanuel

Le scraping d'emplois sur le web est désormais plus facile grâce à Indreed.

### À propos d'Indreed

[Indreed](https://indreed.herokuapp.com) est une API Rest pour le scraping d'emplois depuis Indeed et autour du web. Elle est alimentée par mon projet personnel de web scraping et est structurée en une API Rest. C'est une vraie API Rest et peut être utilisée depuis n'importe quelle plateforme avec n'importe quel langage de programmation. Elle prend en charge les CORs, vous pouvez donc l'utiliser depuis des pages web externes. Indreed supporte une large gamme de filtres que vous pouvez utiliser pour affiner vos résultats de recherche d'emplois. Avec Indreed, vous pouvez obtenir presque toutes les informations dont vous avez besoin sur un emploi autour du web. La documentation peut être trouvée [ici](https://documenter.getpostman.com/view/4679966/indreed/RWEiLy2s).

### Construction de l'application web

Pour ce tutoriel, nous allons utiliser Node.js pour construire une application web de liste d'emplois. La pile technologique que nous allons utiliser inclut :

1. [Axios](https://github.com/axios/axios) pour effectuer des appels d'API Rest
2. [Express](https://expressjs.com/) pour le serveur
3. [Handlebars](http://handlebarsjs.com/) pour le langage de template.
4. Et oui, nous allons utiliser [MDL](http://getmdl.io) pour notre UI/UX.

Commençons...

Ouvrez votre terminal :

```
mkdir jobby && cd jobbynpm init -ynpm install --save express axios express-handlebarsnpm install --save-dev nodemon
```

Une fois que vous avez fait cela, ouvrez le fichier `package.json` créé dans votre éditeur de texte préféré et vous devriez voir quelque chose comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/vyWVz4qyXW82C7uUXolQBw4BD94zgOUH4AEJ)
_package.json_

J'ai déjà ajouté une description, pointé mon main vers `app.js`, et j'ai ajouté des mots-clés, mon nom et aussi nodemon pour le rechargement en direct.

Maintenant, configurons un serveur express de base et le moteur de template handlebars. Créez le fichier `app.js` dans votre répertoire de projet :

Assurez-vous d'avoir la même structure de dossiers comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/L1sXRZDJ3ES7ddMcGKYkirl-GfoL40yxtPZl)
_configuration des dossiers (ignorez le `data.json)`_

Maintenant, nous devons créer un fichier `index.hbs` dans le dossier views qui contiendra notre HTML :

Pour exécuter l'application, vous pouvez utiliser `node app.js`. Si vous voulez utiliser nodemon, vous pouvez faire `nodemon app.js`.

![Image](https://cdn-media-1.freecodecamp.org/images/sxYPGxFnnY5V720GFFx1dvTYW3s7eQ9CE1jW)

Vous pouvez maintenant ouvrir `[http://localhost:5000](http://localhost:5000)` dans votre navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/rGlzAry0qSrBYCR-nuwK-UqQvu6CmrC6vMPO)

Hourra !

Maintenant, essayons d'obtenir des emplois depuis l'API Indreed en utilisant axios, puis utilisons handlebars pour les formater.

Ouvrez le fichier `app.js` et mettez à jour le `app.get("/")` :

Puis remplacez `{{ body }}` par ce qui suit :

```
<div class="mdl-grid portfolio-max-width">{{# each jobs }}   <div class="mdl-cell mdl-card mdl-shadow--4dp portfolio-card">   <div class="mdl-card__media"></div>   <div class="mdl-card__title">   <h2 class="mdl-card__title-text">{{ this.title }}</h2>   </div>   <div class="mdl-card__supporting-text">   {{ this.summary }}   </div>   <div class="mdl-card__actions mdl-card--border">   <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-   ripple-effect mdl-button--accent" href="{{ this.url }}">Read   more</a>   </div>   </div>{{/each}}</div>
```

**Note** : Pour cela, nous affichons uniquement `title`, `summary` et `url`. Il y a d'autres informations que vous pouvez ajouter, alors vérifiez cela.

Actualisez et vous serez impressionné :

![Image](https://cdn-media-1.freecodecamp.org/images/CSlgoD2ACZxBQ7NyRBX3j3rBBdfvvbH1m3iV)

Félicitations, vous venez de construire une simple application web de liste d'emplois.

Décomposons ce que nous venons de construire :

* Nous avons envoyé une requête `_GET_` à l'API Indreed en utilisant `_axios_`
* cela a récupéré les listes d'emplois de développeur web
* et a retourné des données JSON que nous avons passées dans handlebars pour nous aider à les parcourir
* les résultats sont affichés.

Notre application montre uniquement les emplois de `développeur web`. Que faire si nous voulions voir d'autres types d'emplois ? Ce serait idiot d'aller les changer côté code. Donc, ce que nous allons faire ensuite, c'est créer un simple formulaire pour filtrer les résultats d'emplois.

Créons un endpoint `/search` :

Ensuite, créez `search.hbs` :

Ajoutons un peu de CSS :

Ensuite, mettez à jour votre template de page d'accueil avec ceci :

Maintenant que nous avons terminé avec les templates, nettoyons notre `app.js` :

C'est tout, nous avons terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/9HnWhWMAbacRj5yNJM2ExGMZezzGrINooqts)

![Image](https://cdn-media-1.freecodecamp.org/images/mPjZEjwoJcOZ-Ah5zwfsFzBEZEK72KAy2VVG)

### Quelques suggestions

1. **Localisation** : L'application détectant la localisation de l'utilisateur est quelque chose que vous pouvez ajouter pour rendre Indreed plus intelligent. Je suggère que vous utilisiez [Express-IP](https://www.npmjs.com/package/express-ip), un middleware express pour obtenir des informations sur l'IP. Vous pouvez l'utiliser comme suit :

`req.ipInfo` peut retourner null si vous êtes en localhost (c'est pourquoi l'instruction if est là).

2. **Résultats de recherche avancés** : Indreed dispose d'une variété de filtres que vous pouvez utiliser pour filtrer vos résultats d'emplois, et nous n'avons utilisé que `q` et `l`. Vous pouvez donc ajouter un formulaire qui utilise certains des filtres disponibles :

3. **Authentification** : Vous pouvez ajouter un système d'authentification pour personnaliser les résultats de recherche pour l'utilisateur. Avec cela, les utilisateurs peuvent sélectionner les catégories d'emplois qu'ils aimeraient voir, et vous continuerez à suggérer des emplois liés à cela lorsqu'ils se connectent.

4. **Cache** : Si vous voulez personnaliser les résultats de recherche pour un utilisateur sans passer par l'authentification, vous pouvez opter pour le **Cache**.

### Note courte

Je suis le créateur de l'API Indreed, et elle est actuellement en phase Alpha. Comme vous pouvez le voir, elle est hébergée sur Heroku et a encore besoin de nombreuses améliorations en termes de structuration, de performance, de vitesse et d'hébergement. Pour faire avancer cela, vous pouvez contribuer au développement en me contactant (oyetoketoby80[at]gmail.com) ou vous pouvez également aider via ma page patreon. [http://patreon.com/oyetoketoby](http://patreon.com/oyetoketoby)

C'est tout pour cet article. Vous pouvez obtenir le code depuis [ici](https://github.com/CITGuru/Jobby) et également voir la démonstration en direct : [http://jobbyio.herokuapp.com](http://jobbyio.herokuapp.com).

**Si vous avez aimé cet article, n'hésitez pas à applaudir et à le partager avec les autres.**