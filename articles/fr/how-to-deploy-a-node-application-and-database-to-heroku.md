---
title: Comment déployer une application Node et une base de données sur Heroku
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-09-28T05:02:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-node-application-and-database-to-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/banner.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: deployment
  slug: deployment
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Heroku
  slug: heroku
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: terminal
  slug: terminal
seo_title: Comment déployer une application Node et une base de données sur Heroku
seo_desc: Heroku is a cloud-based, fully-managed platform as a service (PaaS) for
  building, running, and managing apps. The platform is flexible and designed with
  DX support for you and your team’s preferred development style and to help you stay
  focused and p...
---

Heroku est une plateforme cloud entièrement gérée en tant que service (PaaS) pour construire, exécuter et gérer des applications. La plateforme est flexible et conçue avec un support DX pour vous et le style de développement préféré de votre équipe, afin de vous aider à rester concentré et productif.

Les développeurs, les équipes et les entreprises de toutes tailles utilisent Heroku pour déployer, gérer et mettre à l'échelle des applications. Que vous construisiez un simple prototype ou un produit critique pour l'entreprise, la plateforme entièrement gérée de Heroku vous offre le chemin le plus simple pour livrer des applications rapidement.

Avec des fonctionnalités comme Heroku Runtime, Heroku Postgres (SQL), Heroku Redis, Add-ons, Data Clips, App metrics, Smart containers, Support de niveau entreprise, Intégration GitHub et bien plus encore, Heroku donne aux développeurs la liberté de se concentrer sur leur produit principal sans la distraction de la maintenance des serveurs, du matériel ou de l'infrastructure.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku.png align="left")

---

L'une des fonctionnalités principales de Heroku est le déploiement, la gestion et la mise à l'échelle d'applications avec vos langages préférés \[Node, Ruby, Python, Java, PHP, Go, et plus\].  
Dans cet article, je vais vous montrer comment prendre une application Node.js existante et la déployer sur Heroku – tout, depuis la création de votre compte Heroku jusqu'à l'ajout d'une base de données à votre application déployée.

## Prérequis

Dans mon article précédent, j'ai écrit sur "[Building a SlackBot with Node.js and SlackBots.js](https://bolajiayodeji.com/building-a-slackbot-with-nodejs-and-slackbotsjs-cjz8gh7zg000exfs1tq2z5zzu)" et j'ai promis d'écrire un article de suivi pour montrer comment héberger le SlackBot sur Heroku, Zeit ou Netlify et le publier sur le magasin d'applications Slack. Eh bien, voici l'article de suivi, mais sans la partie "Publier sur Slack Apps". Nous couvrirons cela dans un autre article.

Je suppose que vous avez/déjà connaissez les éléments suivants :

* Lire mon [article précédent](https://bolajiayodeji.hashnode.dev/building-a-slackbot-with-nodejs-and-slackbotsjs-cjz8gh7zg000exfs1tq2z5zzu)
    
* Construit le [inspireNuggets SlackBot](https://github.com/BolajiAyodeji/inspireNuggetsSlackBot)
    
* Git, Node et npm installés
    
* Un compte [Heroku gratuit](https://signup.heroku.com/)
    
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installé
    

## Bonus

Si vous n'avez pas npm, Node et Heroku CLI installés ou un compte Heroku déjà, voici un petit bonus \[ Oui, vous êtes les bienvenus :) \].

### Installation de npm et Node

* [Node.js](https://nodejs.org) est un environnement d'exécution JavaScript basé sur le [moteur JavaScript V8 de Chrome](https://v8.dev/).
    
* [npm](https://www.npmjs.com/) est le gestionnaire de paquets pour Node.js. Un projet open-source créé pour aider les développeurs JavaScript à partager facilement des modules de code empaquetés.
    

Vous pouvez simplement télécharger Node.js [ici](https://nodejs.org/en/). Ne vous inquiétez pas, npm vient avec Node.js, donc cela installe les deux ✨

### Création d'un compte Heroku gratuit

Veuillez vous rendre [ici](https://signup.heroku.com/) et remplir le formulaire d'inscription. C'est assez simple.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-signup.png align="left")

### Installation de Heroku CLI

L'interface de ligne de commande (CLI) de Heroku facilite la création et la gestion de vos applications Heroku directement depuis le terminal. C'est une partie essentielle de l'utilisation de Heroku. \[ Eh bien, vous pouvez décider d'utiliser la fonction d'intégration GitHub et le tableau de bord Heroku, mais oui, vous devriez apprendre à utiliser la CLI \]  
Heroku CLI nécessite Git, le système de contrôle de version populaire. Si vous n'avez pas déjà Git installé, j'ai écrit [cet article](https://www.bolajiayodeji.com/setting-up-git-first-time/) pour vous aider.

#### Heroku CLI pour Mac OS

```python
brew tap heroku/brew && brew install heroku
```

ou [téléchargez l'installateur](https://devcenter.heroku.com/articles/heroku-cli).

#### Heroku CLI pour Ubuntu

```python
sudo snap install --classic heroku
```

#### Heroku CLI pour Windows

Téléchargez l'installateur pour [64-Bit](https://cli-assets.heroku.com/heroku-x64.exe) ou [32-Bit](https://cli-assets.heroku.com/heroku-x86.exe).

#### Autres méthodes d'installation

Veuillez lire [ceci](https://devcenter.heroku.com/articles/heroku-cli#other-installation-methods).

#### Démarrage avec Heroku CLI

* Vérifiez votre installation
    

```python
heroku --version
```

heroku/7.30.1 linux-x64 node-v11.14.0

* Connectez-vous à votre compte Heroku
    

Il y a deux façons de faire cela :

* **Authentification basée sur le web**
    

```python
heroku login
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-web-auth.png align="left")

Suivez les instructions et connectez-vous via votre navigateur web, puis retournez à votre terminal.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-web-auth2.png align="left")

* **Authentification CLI**
    

C'est une option plus sûre car elle sauvegarde votre adresse e-mail et un jeton API dans `~/.netrc` pour une utilisation future.

```python
heroku login -i
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-cli-auth-1.png align="left")

---

### Déploiement de votre application Node.js

Je suppose que vous avez déjà construit le SlackBot. Si ce n'est pas le cas, veuillez cloner le [projet terminé](https://github.com/BolajiAyodeji/inspireNuggetsSlackBot).

Le projet est un simple Slackbot qui affiche des citations et des blagues technologiques inspirantes aléatoires pour les développeurs/designers.

```bash
git clone https://github.com/BolajiAyodeji/inspireNuggetsSlackBot.git && cd inspireNuggetsSlackBot
```

Maintenant, déployons notre application sur Heroku 🚀. Je vais vous montrer deux façons de faire cela :

#### Déploiement via Heroku Git

Cela se fait via la CLI Heroku.

##### **✅ Checklist**

* Spécifiez la version de Node.js qui sera utilisée pour exécuter votre application sur Heroku dans votre fichier `package.json`.
    

```python
"engines": {
    "node": "10.16.0"
  },
```

* Spécifiez votre script de démarrage.  
    Créez simplement un `Procfile` (sans aucune extension de fichier) et ajoutez
    

```python
web: node index.js
```

Heroku cherche d'abord ce Procfile. Si aucun n'est trouvé, Heroku tentera de démarrer un processus web par défaut via le script de démarrage dans votre `package.json`.

* Démarrez votre application localement en utilisant la commande heroku local pour être sûr que tout fonctionne bien
    

```python
heroku local web
```

Votre application devrait maintenant s'exécuter sur [http://localhost:5000](http://localhost:5000).

* N'oubliez pas le `.gitignore`
    

```python
/node_modules
.DS_Store
/*.env
```

##### **🚀 Déployons**

Voici comment cela fonctionne : vous avez le projet qui fonctionne localement et vous l'avez déjà poussé sur GitHub.

* Exécutez `heroku create`
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-create.png align="left")

En gros, cette commande crée une nouvelle application Heroku pour vous avec un domaine généré aléatoirement et ajoute Heroku à votre dépôt Git local.

* Maintenant, exécutez `git push heroku master`
    

C'est la commande magique, elle pousse votre application vers Heroku, l'installe là-bas et la lance sur votre domaine alloué.

Dans l'exemple ci-dessus, c'est [https://lit-cove-58897.herokuapp.com/](https://lit-cove-58897.herokuapp.com/)

Vous pouvez toujours modifier les paramètres de votre application et les domaines dans votre [Tableau de bord Heroku](https://dashboard.heroku.com/)

* Maintenant, visitez votre application dans votre navigateur
    

```python
heroku open
```

* Vous pouvez également afficher des informations sur votre application en cours d'exécution en utilisant l'une des commandes de journalisation. Cela est très utile pour le débogage des erreurs.
    

```python
heroku logs --tail
```

#### Déploiement via l'intégration GitHub

Vous pouvez configurer l'intégration GitHub dans l'onglet Déploiement des applications dans le [Tableau de bord Heroku](https://dashboard.heroku.com).

##### **✅ Checklist**

* Toutes les checklists précédentes s'appliquent ici – assurez-vous d'avoir déjà déployé l'application sur GitHub
    

##### **🚀 Déployons**

Voici comment cette méthode fonctionne : vous poussez votre projet entier sur GitHub et l'intégrez à Heroku. Chaque fois que vous poussez, il déploie de GitHub à Heroku. Plutôt cool, non ?

* Connectez-vous à votre tableau de bord Heroku et créez une nouvelle application
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/create-app.png align="left")

* Sélectionnez le nom de votre application et la région
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/new-app.png align="left")

Maintenant, votre application a été créée avec succès

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-dash.png align="left")

* Cliquez sur l'onglet de déploiement et faites défiler jusqu'à la section **Méthode de déploiement**
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-deploy.png align="left")

* Cliquez sur le bouton **Se connecter à GitHub**
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-github.png align="left")

* Maintenant, vous avez la section **Se connecter à GitHub**, recherchez le dépôt et déployez.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-search.png align="left")

* Maintenant, votre application a été déployée avec succès
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-200.png align="left")

#### Déploiements automatiques

Maintenant, votre application est déployée, mais vous devrez continuer à déployer manuellement. Vous devez activer les déploiements automatiques pour une branche GitHub, afin que Heroku construise et déploie toutes les poussées vers cette branche.

* Faites défiler jusqu'à la section **Déploiements automatiques**
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-auto.png align="left")

Sélectionnez la branche que vous souhaitez déployer. Idéalement, cela devrait être la branche `master`, mais changez cela selon votre préférence.

Maintenant, chaque poussée vers `master` (ou la branche que vous avez choisie) déployera une nouvelle version de cette application.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-auto-200.png align="left")

#### Buildpack Node.js

Dans Heroku, les Buildpacks sont des scripts qui sont exécutés lorsque votre application est déployée. Ils sont utilisés pour installer les dépendances de votre application et configurer votre environnement.

Après avoir déployé votre application, assurez-vous d'ajouter un buildpack Node.js à votre projet.

* Allez dans **Paramètres** et faites défiler jusqu'à la section **Buildpack**
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-buildpack.png align="left")

* Cliquez sur le bouton **Ajouter un Buildpack** et sélectionnez Node.js dans la fenêtre modale.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-add-build.png align="left")

* Maintenant, la nouvelle configuration du buildpack sera utilisée lors du prochain déploiement de cette application. Apportez quelques modifications à votre application et poussez vers GitHub – elle se déployera automatiquement.
    

### Ajout d'une base de données à votre application déployée

Le marché des add-ons Heroku dispose d'un grand nombre de magasins de données, allant des fournisseurs Redis et MongoDB à Postgres et MySQL.

Heroku fournit trois services de données gérés à tous les clients sous forme d'add-ons :

* [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
    
* [Heroku Redis](https://elements.heroku.com/addons/heroku-redis)
    
* [Apache Kafka sur Heroku](https://elements.heroku.com/addons/cloudkarafka)
    

Écrire sur ces trois services rendrait cet article trop long. C'est assez simple et j'ajouterai quelques liens vers la documentation Heroku.

* [Documentation Heroku Postgresql](https://devcenter.heroku.com/categories/postgres-basics)
    
* [Documentation Heroku Redis](https://devcenter.heroku.com/articles/heroku-redis)
    
* [Documentation Apache Kafka sur Heroku](https://devcenter.heroku.com/articles/kafka-on-heroku)
    

---

## Conclusion

Chaque compte Heroku se voit attribuer un pool d'heures de dyno gratuites. Les dynos Heroku (gratuits) sont excellents pour héberger des applications et des projets personnels. L'inconvénient, cependant, est que votre application s'endormira si elle ne reçoit aucun trafic web pendant 30 minutes :(.

Vous pouvez utiliser des outils externes pour pinguer votre serveur périodiquement afin qu'il ne s'endorme jamais.

En voici quelques-uns à considérer :

* [Pingmydyno](https://www.npmjs.com/package/pingmydyno)
    
* [Heroku self ping](https://www.npmjs.com/package/heroku-self-ping)
    
* [Wakemydyno](http://wakemydyno.com/)
    
* [Kaffeine](https://kaffeine.herokuapp.com/)
    

---

> Heroku est méticuleusement conçu pour aider les développeurs à être aussi productifs que possible. La plateforme élimine les obstacles frustrants et les tâches fastidieuses, afin que vous puissiez rester libre de distraction dans votre flux de développement. Où que vous soyez sur le chemin de l'apprentissage, Heroku vous aide à aimer encore plus le développement d'applications. - Heroku

L'expérience Heroku fournit des services, des outils, des flux de travail et un support polyglotte – tous conçus pour améliorer la productivité des développeurs. Il y a plus à utiliser Heroku et j'espère que vous explorerez davantage et construirez des choses incroyables avec Heroku.

Si vous êtes étudiant, veuillez vous inscrire au [GitHub Student Developer Pack](https://education.github.com/pack) pour obtenir un [Hobby Dyno](https://www.heroku.com/pricing) gratuit pendant jusqu'à deux ans.

Le pack offre aux étudiants un accès gratuit aux meilleurs outils de développement en un seul endroit afin que vous puissiez apprendre en faisant.