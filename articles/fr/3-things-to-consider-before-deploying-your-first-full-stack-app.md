---
title: Trois choses à considérer avant de déployer votre première application Full
  Stack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-17T21:12:22.000Z'
originalURL: https://freecodecamp.org/news/3-things-to-consider-before-deploying-your-first-full-stack-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c1d740569d1a4ca3007.jpg
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: Azure
  slug: azure
- name: containers
  slug: containers
- name: deployment
  slug: deployment
- name: Docker
  slug: docker
- name: Express
  slug: express
- name: full stack
  slug: full-stack
- name: Heroku
  slug: heroku
- name: Kubernetes
  slug: kubernetes
- name: mongoose
  slug: mongoose
- name: node
  slug: node
- name: REST
  slug: rest
- name: vue
  slug: vue
seo_title: Trois choses à considérer avant de déployer votre première application
  Full Stack
seo_desc: 'By M. S. Farzan

  Building a full stack app is no small endeavor, and deploying it comes with its
  own host of things to consider.

  I''m a tabletop game developer, and recently deployed a simple roleplaying game
  tracker that uses the M-E-V-N stack (you ca...'
---

Par M. S. Farzan

Construire une application full stack n'est pas une mince affaire, et son déploiement comporte son propre ensemble de choses à considérer.

Je suis un développeur de [jeux de table](https://www.nightpathpub.com/entromancy), et j'ai récemment déployé un simple [suiveur de jeu de rôle](https://mevn-rpg-app.herokuapp.com/) qui utilise la pile [M](https://www.mongodb.com/)-[E](https://expressjs.com/)-[V](https://vuejs.org/)-[N](https://nodejs.org/en/) (vous pouvez suivre mon tutoriel pour créer votre propre application [ici](https://www.freecodecamp.org/news/build-a-full-stack-mevn-app/)).

En déployant l'application, je suis tombé sur trois points clés qui peuvent être utiles lorsque vous commencez à considérer la meilleure façon d'amener vos projets de développement à production.

Vous pouvez consulter le code de mon application sur [GitHub](https://github.com/sominator/mevn-rpg-app), et je devrais mentionner qu'il inclut le [très cool CSS statblock](https://codepen.io/retractedhack/pen/gPLpWe) de Chad Carteret pour embellir ce qui serait autrement du HTML très basique.

Si vous pensez suivre le même chemin de déploiement que moi, assurez-vous de consulter la documentation officielle sur [Heroku](https://devcenter.heroku.com/articles/deploying-nodejs), le [Vue CLI](https://cli.vuejs.org/guide/deployment.html), et [ce tutoriel](https://medium.com/netscape/deploying-a-vue-js-2-x-app-to-heroku-in-5-steps-tutorial-a69845ace489) par Nick Manning.

Vous voudrez également jeter un coup d'œil à l'article de Will Abramson sur [un sujet similaire](https://www.freecodecamp.org/news/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286/).

Passons au déploiement !

## Votre front end et back end peuvent être déployés ensemble ou séparément, selon la complexité de votre application.

Un obstacle qui semble apparaître immédiatement lorsque l'on considère la production est la question structurelle de savoir comment déployer les parties front end et back end de votre application.

Le client (ou les fichiers statiques) doit-il vivre au même endroit que le serveur et la base de données ? Ou doivent-ils être séparés, avec le front end faisant des requêtes HTTP depuis ailleurs vers le back end en utilisant [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) ?

La réponse est oui ! Ou non. Peut-être ??

Pour le meilleur ou pour le pire, il n'existe pas de solution universelle à cette question, car elle dépendra probablement de l'architecture et de la complexité de votre application. Dans le suiveur de jeu de rôle que j'ai lié ci-dessus, j'ai toute la pile qui tourne sur un seul [dyno](https://www.heroku.com/dynos) Heroku, avec la structure de dossiers suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Folder-Structure.PNG)

Tous les fichiers front end et back end vivent au même endroit, avec le client Vue construit pour la production dans un dossier situé à /client/dist.

Dans server.js, avec un tas de code de base de données et de routage, il y a une petite ligne qui dit :

```javascript
server.use(serveStatic(__dirname + "/client/dist"));
```

Dans Express, cela indique à l'application de servir mes fichiers client statiques à partir d'un dossier particulier, et me permet de faire tourner les parties front end et back end dans le même environnement. Si vous déployez une application tout aussi simple, ce type de solution pourrait également fonctionner pour vous.

Inversement, et selon la complexité de votre projet, vous devrez peut-être séparer les parties front end et back end et les traiter comme des applications distinctes, ce qui n'est pas un gros problème. Dans l'application ci-dessus, mon client fait des appels à des points de terminaison API statiques qui sont gérés par le serveur, comme ceci :

```javascript
getQuests: function () {
    axios
        .get('https://mevn-rpg-app.herokuapp.com/quests')
        .then(response => (this.questData = response.data))
}
```

Techniquement, mon client pourrait faire ces requêtes depuis n'importe où - même un site statique GitHub Pages. Ce type de solution peut aider à séparer votre application en deux entités distinctes à traiter, ce qui est parfois mieux que d'essayer d'entasser tout le projet dans un seul endroit.

Une note : si vous allez faire des requêtes HTTP cross-origin - c'est-à-dire des requêtes depuis un client qui vit sur un domaine séparé de l'API ou du serveur - vous devrez vous familiariser avec [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing). Vous pouvez en lire plus à ce sujet dans [cet article](https://www.freecodecamp.org/news/i-built-a-web-api-with-express-flask-aspnet/).

## Votre code devra changer pour supporter un environnement de production.

Lorsque vous êtes en plein dans le processus de développement, il est facile de perdre de vue combien de votre code dépend de fichiers locaux ou d'autres données.

Considérez ce qui suit dans un server.js en cours d'exécution localement :

```javascript
server.listen(3000, () => console.log("Server started!"));
```

Sur une machine locale, le code demande simplement au serveur d'écouter sur le port 3000 et de journaliser dans la console que nous sommes prêts pour le décollage.

Dans un environnement de production, le serveur n'a aucune notion de l'endroit où le "localhost" devrait être, ou sur quel port 3000 il devrait écouter. Avec cet exemple, vous devriez changer votre code en quelque chose comme :

```javascript
const port = process.env.PORT || 3000;

server.listen(port, () => console.log("Server started!"));
```

Ce qui précède indique au serveur d'écouter plutôt sur le port 3000 du _processus_ qui est actuellement en cours d'exécution, où qu'il soit (consultez [cet article](https://codeburst.io/process-env-what-it-is-and-why-when-how-to-use-it-effectively-505d0b2831e7) pour plus de lectures sur ce sujet).

De même, dans mon application, j'ai plusieurs modules qui doivent être importés les uns par les autres pour fonctionner :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Folder-Structure-Expanded.PNG)

Dans /routes/Quests.js, par exemple, j'ai un routeur qui indique au serveur quoi faire lors de la réception de requêtes API pour interagir avec des éléments liés aux quêtes dans la base de données. Le routeur doit importer un [schéma Mongoose](https://mongoosejs.com/docs/guide.html) depuis /models/quest.js pour fonctionner correctement. Si l'application était en cours d'exécution localement, nous pourrions simplement dire :

```javascript
const Quest = require('../models/quest');
```

Assez simple ! Pourtant, malheureusement, notre serveur ne saura pas où trouver le répertoire racine de notre projet une fois déployé. Dans Express, nous changerions notre code en quelque chose comme :

```javascript
const path = require('path');
const Quest = require(path.join(__dirname, '../models/quest'));
```

Votre cas particulier peut être différent, selon votre langage et votre ou vos frameworks, mais vous devrez être spécifique quant à l'apparence de votre code dans un environnement de production plutôt que dans votre environnement de développement local.

De plus, vous êtes probablement déjà familiarisé avec le bundler que vous utilisez pour votre front end (par exemple, [webpack](https://webpack.js.org/)), et vous voudrez construire votre client pour la production afin de l'optimiser pour le déploiement.

## Vous avez une multitude de plateformes de déploiement parmi lesquelles choisir.

Si vous avez déployé un site web front end ou une autre type d'application statique, vous êtes peut-être familiarisé avec le fait de simplement pousser vos fichiers vers un dépôt distant et d'en rester là.

Déployer une application full stack (ou même juste un back end) est éminemment plus complexe. Vous aurez besoin d'un serveur dédié, ou de quelque chose qui en émule un, pour répondre aux requêtes HTTP qu'il recevra et travailler avec une base de données en ligne.

Il existe un certain nombre de services qui feront exactement cela pour vous, et le spectre varie en fonction du prix, de la scalabilité, de la complexité et d'autres facteurs.

Il y a un tas d'articles qui comparent les options [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) pour le déploiement, mais voici quelques réflexions lorsque vous considérez les plateformes pour votre premier projet :

<ul>
    <li><strong>Heroku</strong> : Si vous avez un petit projet comme le mien ou si vous voulez simplement en apprendre davantage sur le déploiement, une bonne première étape pourrait être <a href="https://www.heroku.com/">Heroku</a>.</li>
    <li><strong>AWS, Docker et Kubernetes</strong> : Si vous cherchez une carrière dans le développement web full stack ou DevOps, c'est le bon moment pour vous familiariser avec <a href="https://aws.amazon.com/">Amazon Web Services</a> et/ou les plateformes de conteneurs comme <a href="https://www.docker.com/">Docker</a> et <a href="https://kubernetes.io/">Kubernetes</a>.</li>
    <li><strong>Azure</strong> : Si vous êtes un développeur C# ou .NET, <a href="https://azure.microsoft.com/en-us/">Azure</a> semble être un moyen transparent de déployer vos applications sans avoir à quitter la sécurité de l'écosystème Microsoft.</li>
</ul>

Il existe, bien sûr, plusieurs autres options, et votre scénario d'utilisation particulier peut dépendre des prix ou des ensembles de fonctionnalités spécifiques qui sont proposés.

De plus, vous voudrez considérer les addons qui seront nécessaires pour reproduire la fonctionnalité de votre application dans un environnement de production. Mon suiveur de jeu de rôle, par exemple, utilise MongoDB, mais la version de production ne peut certainement pas utiliser la petite base de données sur ma machine locale ! À la place, j'ai utilisé l'addon Heroku [mLab](https://elements.heroku.com/addons/mongolab) pour mettre le site en ligne avec la même fonctionnalité que dans mon environnement de développement.

Le succès de votre application, ainsi que vos propres progrès en tant que développeur web full stack, dépendent de votre capacité à considérer les options de déploiement et à créer un pipeline réussi pour la production. Avec un peu de recherche, je suis certain que vous pouvez trouver la meilleure solution qui répond à tous les besoins de votre application.

Bon codage !

Si vous avez aimé cet article, veuillez considérer [découvrir mes jeux et livres](https://www.nightpathpub.com/), [vous abonner à ma chaîne YouTube](https://www.youtube.com/msfarzan?sub_confirmation=1), ou [rejoindre le Discord _Entromancy_](https://discord.gg/RF6k3nB).

M. S. Farzan, Ph.D. a écrit et travaillé pour des entreprises de jeux vidéo de haut profil et des sites éditoriaux tels qu'Electronic Arts, Perfect World Entertainment, Modus Games et MMORPG.com, et a servi en tant que Community Manager pour des jeux comme _Dungeons & Dragons Neverwinter_ et _Mass Effect: Andromeda_. Il est le Directeur Créatif et le Game Designer en Chef de _[Entromancy: A Cyberpunk Fantasy RPG](https://www.nightpathpub.com/rpg)_ et l'auteur de _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Retrouvez M. S. Farzan sur Twitter [@sominator](https://twitter.com/sominator).