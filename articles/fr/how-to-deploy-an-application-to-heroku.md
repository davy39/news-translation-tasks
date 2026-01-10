---
title: Déploiement sur Heroku – Comment publier une application ou un site web en
  production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-05T18:41:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-an-application-to-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/preview.jpeg
tags:
- name: Heroku
  slug: heroku
- name: Node.js
  slug: nodejs
seo_title: Déploiement sur Heroku – Comment publier une application ou un site web
  en production
seo_desc: 'By Stan Georgian

  When it comes to deploying an application, there are usually two options: a VPS
  or a PaaS (platform as a service). This article will show you a recipe for deploying
  an application to production on a PaaS like Heroku.

  Step 1 - Create ...'
---

Par Stan Georgian

Lorsqu'il s'agit de déployer une application, il existe généralement deux options : un [VPS](https://en.wikipedia.org/wiki/Virtual_private_server) ou une [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) (plateforme en tant que service). Cet article vous montrera une méthode pour déployer une application en production sur une PaaS comme [Heroku](https://www.heroku.com/).

## Étape 1 - Créer le projet

La première étape consiste à créer une structure simple pour notre projet avec quelques fichiers de base. Pour cet article, je vais créer un serveur de démonstration avec NodeJS.

Dans un nouveau dossier, j'ouvrirai un terminal et exécuterai la commande `npm init -y` afin de créer un nouveau projet. Le serveur fictif sera écrit en [Express](https://expressjs.com/), nous devons donc exécuter la commande `npm install express` pour installer ce module.

Une fois cette bibliothèque installée, nous pouvons créer un nouveau fichier pour notre projet, nommé `app.js`. À l'intérieur, nous écrivons le code pour notre serveur simple :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/server.png)
_[RAW](https://carbon.now.sh/?bg=rgba(171%2C%20184%2C%20195%2C%201)&amp;t=seti&amp;wt=none&amp;l=javascript&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=const%2520app%2520%253D%2520require(%2522express%2522)()%253B%250A%250Aconst%2520PORT%2520%253D%2520process.env.PORT%2520%257C%257C%25203000%253B%250A%250Aapp.get(%2522%2522%252C%2520(req%252C%2520res)%2520%253D%253E%2520%257B%250A%2520%2520res.send(%2522Hello%2520world%2522)%253B%250A%257D)%253B%250A%250Aapp.listen(PORT%252C%2520()%2520%253D%253E%2520%257B%250A%2520%2520console.log(%2560App%2520up%2520at%2520port%2520%2524%257BPORT%257D%2560)%253B%250A%257D)%253B)_

Nous pouvons démarrer l'application en exécutant `node app.js`. Ensuite, nous pouvons l'essayer à l'URL suivante `http://localhost:3000`. À ce stade, vous devriez voir le message `Hello World` dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/output.PNG)

## Étape 2 - Système de contrôle de version

L'étape suivante consiste à choisir un système de contrôle de version et à placer notre code sur une plateforme de développement dans un dépôt.

Le système de contrôle de version le plus populaire est [Git](https://git-scm.com/) avec [Github](https://github.com/) comme plateforme de développement, c'est donc ce que nous utiliserons ici.

Sur GitHub, allez-y et créez un nouveau dépôt pour votre application, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1.PNG)

Pour téléverser votre code local dans un dépôt, vous devez exécuter les commandes qui sont listées sur Github après avoir cliqué sur le bouton `Create repository` :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/git.PNG)
_Commandes pour téléverser notre code vers le dépôt Github_

**!** Avant de faire cela, nous devons ignorer certains fichiers. Nous voulons téléverser dans le dépôt uniquement le code que nous écrivons, sans les dépendances (les modules installés).

Pour cela, nous devons créer un nouveau fichier `.gitignore` et y écrire le fichier que nous voulons ignorer.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ignore.PNG)
_Structure du dossier et fichier .gitignore_

Maintenant, nous pouvons écrire les commandes listées dans l'image ci-dessus (celle de GitHub).

Si vous avez exécuté les commandes correctement, elles seront sur la page de votre dépôt. Si vous l'actualisez, vous devriez voir vos fichiers, à l'exception de celui que vous avez explicitement ignoré, à savoir `node_modules`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/git-master.PNG)

## Étape 3 - Lier le dépôt avec Heroku

À cette étape, nous pouvons lier le dépôt de Github à notre application Heroku.

Tout d'abord, créez une nouvelle application sur Heroku et suivez les étapes listées sur la plateforme.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/heroku-new.PNG)

Une fois l'application créée, une fenêtre similaire à celle-ci devrait apparaître :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/heroku-shoud-see.PNG)
_Tableau de bord de l'application_

Maintenant, si vous regardez la navigation en haut, vous verrez `Overview`, `Resources`, `Deploy`, `Metrics` et ainsi de suite. Assurez-vous que `Deploy` est sélectionné. Ensuite, sur la deuxième ligne, cliquez sur l'icône GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/search-and-cionnect.PNG)
_Cliquez sur connecter_

Recherchez l'application souhaitée, qui est `demo-deploy-app-09` dans notre cas. Ensuite, cliquez sur `Connect`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/deploy.PNG)
_Déployer la branche_

Une fois l'application connectée avec succès à votre compte Heroku, vous pouvez cliquer sur `Deploy Branch` pour déployer votre application.

Si vous le souhaitez, vous pouvez également sélectionner l'option `Enable Automatic Deploys` qui tirera automatiquement le code de votre dépôt Github chaque fois que vous ferez un push vers ce dépôt.

Une fois l'application déployée, vous pouvez cliquer sur View pour ouvrir votre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/final.PNG)

## Étape 4 - Configurer Heroku pour exécuter correctement l'application

Si vous ouvrez l'application à ce stade, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/errr.PNG)

C'est exact, une erreur. C'est parce que Heroku ne sait pas comment démarrer notre application.

Si vous vous souvenez, nous avons exécuté la commande `node app.js` pour démarrer l'application localement. Heroku n'a aucun moyen de savoir quelles commandes il doit exécuter pour démarrer l'application, et c'est pourquoi il a généré une erreur.

Pour résoudre ce problème, nous devons créer un nouveau fichier nommé `Procfile` avec le contenu suivant : `web: node ./app.js`.

Pour mettre à jour notre application, tout ce que nous devons faire est de pousser un nouveau commit vers GitHub. Si nous avons activé l'option `Automatic Deploys`, alors le code sera automatiquement tiré vers Heroku. Sinon, nous devons cliquer à nouveau sur `Deploy Branch`.

Une fois l'application reconstruite, nous devrions la voir fonctionner comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/deployed.PNG)

## Étape 5 - Comment ajouter un add-on

L'un des principaux avantages que Heroku offre est le fait que vous pouvez facilement ajouter des ressources sous forme d'`add-ons` à votre projet. Ces ressources externes se présentent sous la forme de bases de données, d'outils de journalisation et de surveillance, d'outils CI et CD, ou d'outils de test.

Voyons maintenant comment ajouter une nouvelle ressource à votre projet. Tout d'abord, nous irons dans Resources, et de là, nous ajouterons un nouvel outil de test.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/add-addon.PNG)

Allez-y et cliquez sur `Find more add-ons` puis recherchez `Loadmill`.

[Loadmill](https://elements.heroku.com/addons/loadmill) est un outil de test qui est vraiment excellent pour les tests de régression et les tests de charge.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/install-loadmill.PNG)

Allez-y et cliquez sur `Install…`. Ensuite, choisissez l'application que vous souhaitez lier.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/provision-add-on.PNG)

À cette étape, Heroku créera automatiquement un nouveau compte pour vous sur la plateforme provisionnée.

Dans l'onglet des ressources, vous pouvez voir la nouvelle ressource ajoutée :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/ff.PNG)

Si vous allez de l'avant et accédez à cet add-on, vous devriez voir son tableau de bord avec un tutoriel d'introduction et un test de démonstration créé pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/fff2.PNG)
_Tableau de bord Loadmill_

# Conclusion

Heroku permet aux développeurs de déployer rapidement et presque sans douleur une application sur un serveur web.

Il fournit également de nombreux plugins que vous pouvez intégrer à votre application.

Une solution PaaS vous permettra toujours de vous déplacer plus rapidement que la solution avec un VPS où vous devez tout configurer à partir de zéro.