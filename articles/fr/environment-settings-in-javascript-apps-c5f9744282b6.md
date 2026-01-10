---
title: Comment gérer les paramètres spécifiques à l'environnement dans vos applications
  JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T23:56:52.000Z'
originalURL: https://freecodecamp.org/news/environment-settings-in-javascript-apps-c5f9744282b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sS6KcsjhHDEI1T0ka164Wg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment gérer les paramètres spécifiques à l'environnement dans vos applications
  JavaScript
seo_desc: 'By Cory House

  Today many web apps are built using React, Angular, Vue, Ember, and others. These
  modern client-side rendered apps often call web APIs that are hosted on separate
  servers. This creates a problem: how do you configure your app to call th...'
---

Par Cory House

Aujourd'hui, de nombreuses applications web sont construites en utilisant React, Angular, Vue, Ember, et d'autres. Ces applications modernes rendues côté client appellent souvent des API web hébergées sur des serveurs séparés. Cela crée un problème : comment configurer votre application pour appeler la bonne URL d'API dans chaque environnement ?

Par exemple, pendant le développement, vous pouvez héberger l'API localement à localhost:3000. En production, l'API peut être hébergée sur un autre serveur à api.monentreprise.com. Vous avez donc besoin que votre application appelle localhost:3000 en développement et api.monentreprise.com en production. Mais comment ?

Et l'URL de base n'est qu'un exemple de paramètres qui peuvent changer par environnement. Vous pouvez choisir d'ajuster d'autres paramètres par environnement pour des raisons de performance, de sécurité ou de journalisation. Certaines des approches ci-dessous sont applicables pour ces configurations spécifiques à l'environnement en général. Mais pour simplifier, cet article se concentre sur les techniques de configuration des URL de base par environnement.

J'ai posté un sondage sur Twitter avec quelques options :

%[https://twitter.com/housecor/status/973881714710908928?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fhousecor%2Fstatus%2F973881714710908928%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F650743198348808192%25252FLT6SeOJr_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

Il s'avère qu'il existe de nombreuses façons de gérer cela. J'ai reçu de nombreuses réponses perspicaces dans le fil de discussion du tweet. J'ai résumé huit options ci-dessous. J'ai classé ces options (de manière approximative) dans l'ordre dans lequel elles devraient être considérées. Donc, si vous êtes pressé, les options à considérer en premier sont en haut. ?

### Option 1 : Héberger l'API avec l'application

Simple. Il suffit d'héberger l'application et l'API sur le même serveur web, de sorte que les URL relatives fonctionnent partout. Cela évite à la fois le problème de l'URL de base ainsi que les problèmes de cross-origin.

#### **Quand l'envisager** :

* Votre API est consommée par une seule application.
* Vous n'avez pas besoin de mettre à l'échelle votre API et votre application séparément, donc l'hébergement sur le même serveur est pratique.

### Option 2 : Build spécifique à l'environnement

Cette approche respecte le principe de compilation :

> « Ne faites jamais à l'exécution ce que vous pouvez gérer à la compilation. »

Avec cette approche, vous utilisez généralement un serveur d'intégration continue (CI) pour générer et déployer des builds personnalisés pour chaque environnement. C'est une approche puissante, sécurisée et polyvalente, mais elle nécessite que chaque développeur crée et maintienne un fichier .env sur sa machine. [Voici un excellent article avec quelques astuces pour rendre cela assez indolore](https://medium.com/@rafaelvidaurre/managing-environment-variables-in-node-js-2cb45a55195f).

#### **Quand l'envisager** :

* Vous êtes à l'aise pour configurer un serveur CI afin d'automatiser le processus de build et de déploiement pour assurer la fiabilité.
* Vous souhaitez modifier significativement le code déployé en production, comme supprimer du code qui n'est utilisé que dans les environnements non-production pour des raisons de performance ou de sécurité.
* Vous êtes à l'aise avec le risque qui accompagne le déploiement de code différent en production par rapport au code que vous avez exécuté pendant le développement et les tests.

### Option 3 : Configuration à l'exécution

Avec cette approche, vous configurez votre application pour chaque environnement en référençant les données de configuration pertinentes au démarrage (par opposition à la construction comme discuté ci-dessus). Ainsi, **contrairement à l'approche ci-dessus, avec cette approche, le même code est déployé dans tous les environnements**. Les données de configuration que vous passez au démarrage personnalisent le comportement de l'application.

Il existe quelques moyens potentiels de passer les données de configuration de l'environnement :

1. **Config en ligne de commande** — Passez la config lors du démarrage de l'application.
2. **Fichier de config d'environnement** — Remplissez un fichier .env dans chaque environnement et lisez-le au démarrage. [Voici un exemple de la documentation de create-react-app](https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/template/README.md#adding-custom-environment-variables), mais l'approche s'applique à toute application JavaScript.

Mais comment votre application obtient-elle ces informations ? Il existe également quelques moyens de le faire :

1. **Fichier de config** — Écrivez les données de config dans un fichier JavaScript séparé au démarrage de l'application. Votre application peut importer et lire ce fichier au démarrage.
2. **Global dans index.html** — Écrivez les données de config dans un global dans index.html en utilisant votre outil de build. Encore une fois, [voici un exemple de la documentation de create-react-app](https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/template/README.md#injecting-data-from-the-server-into-the-page), mais l'approche s'applique à toute application JavaScript.

Admettons que ces approches modifient légèrement votre code au démarrage en fonction de la configuration d'exécution fournie. Mais elles sont différentes de l'option #2 ci-dessus, car le même code est déployé dans tous les environnements.

#### **Quand l'envisager** :

* Vous préférez déployer le même code dans tous les environnements.

### Option 4 : Proxy inverse

Avec cette approche, vous appelez la même URL relative dans tous les environnements. Comment cela fonctionne-t-il ? Eh bien, c'est la responsabilité du serveur web front-end de transférer les appels à l'API pertinente pour chaque environnement. Il y a plusieurs avantages à cette approche :

1. Vos URL dans tous vos appels d'API sont des URL relatives propres. Par exemple /user.
2. Vous pouvez configurer votre serveur web front-end comme une couche de cache pour des performances accrues.
3. Cette approche prend en charge le basculement des systèmes back-end en reconfigurant simplement le proxy.

%[https://twitter.com/_ericelliott/status/973970277670436864?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2F_ericelliott%2Fstatus%2F973970277670436864%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F464310668984725504%25252Fym-M-SNv_400x400.jpeg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

#### **Quand l'envisager** :

* Vous avez la capacité de configurer le serveur web dans tous les environnements
* Vous êtes intéressé par la mise en place d'une couche de cache entre votre UI et votre API.
* Votre serveur web front-end peut transférer les appels à votre serveur API de manière fiable et rapide. Il y a un coût de performance à cette approche, puisque votre serveur web doit transmettre les requêtes à un autre serveur.

#### **Note de côté** :

Pendant que nous parlons de proxies, une autre approche de proxy qui mérite d'être mentionnée est le proxy middleware (il s'agit d'une approche totalement différente du proxy inverse discuté ci-dessus).

Avec le proxy middleware en cours d'exécution sur votre machine locale, les requêtes sont transférées à une URL spécifiée pendant le développement. Par exemple, si vous êtes un développeur React, [create-react-app a un support de proxy intégré](https://github.com/facebook/create-react-app/blob/master/packages/react-scripts/template/README.md#proxying-api-requests-in-development). Il utilise le proxy middleware de Webpack.

Voici un [bon aperçu de l'approche proxy](https://medium.freecodecamp.org/how-to-make-create-react-app-work-with-a-node-backend-api-7c5c48acb1b0) utilisant React et Express.

**Cependant** : Le proxy middleware ne résout le problème de l'URL de base qu'en développement. Utilisez donc l'une des autres techniques de cet article pour gérer d'autres environnements tels que la QA et la production.

### Option 5 : Docker

Avec Docker, vous pouvez déployer l'UI et l'API en tant que conteneurs séparés, mais créer un « LAN » qui permet aux conteneurs de communiquer comme s'ils étaient sur le même réseau. De cette façon, les URL de base ne changent pas dans chaque environnement. Les conteneurs s'exécutent de manière identique dans tous les environnements. Et vous pouvez passer des variables d'environnement pertinentes dans les conteneurs dans chaque environnement. Regardez Kubernetes ou Docker Swarm pour cette approche.

#### **Quand l'envisager** :

* Vous êtes déjà investi dans l'écosystème Docker.

### Option 6 : Détection d'environnement

Avec cette approche, vous utilisez du code pour « détecter » ?? l'environnement actuel, généralement en regardant l'URL. Par exemple, si l'URL est http://localhost, vous savez que vous êtes en développement.

L'avantage de cette approche est la simplicité. Les développeurs n'ont pas besoin de configurer quoi que ce soit sur leur machine et vous n'avez pas besoin de manipuler les configurations du serveur CI ou du serveur web non plus.

#### **Quand l'envisager** :

* Vous avez une application simple qui appelle un petit nombre d'API.
* Vous n'avez pas de serveur CI.
* Les politiques de votre entreprise rendent douloureux ou peu pratique la mise en œuvre des autres options ci-dessus.
* Vous n'êtes pas préoccupé par le fait que des personnes puissent trouver les URL de votre environnement non-production. (Pour des raisons de sécurité, votre environnement non-production ne devrait pas être accessible en dehors de votre LAN/VPN d'entreprise de toute façon).

### Option 7 : En-tête HTTP personnalisé

Configurez le serveur web front-end pour fournir un en-tête HTTP personnalisé qui contient l'URL cliente pertinente pour l'environnement. L'inconvénient de cette approche est que votre application doit faire un appel HTTP à cette API d'abord pour déterminer quelles sont les URL de base pertinentes pour tous les environnements.

#### **Quand l'envisager** :

* Je ne recommande pas cette approche, car elle nécessite que votre application fasse un appel HTTP aller-retour avant de pouvoir commencer à récupérer des données. Je préfère l'une des autres approches ci-dessus.

### Option 8 : Point de terminaison de configuration de l'application

Avec cette approche, votre application appelle la même API de « configuration de l'application » à la même URL, pour tous les environnements. Votre application appelle cette API en premier. L'appel d'API retourne l'URL de base pertinente dans chaque environnement (ainsi que potentiellement d'autres paramètres spécifiques à l'environnement). Avec cette approche, vous pouvez potentiellement transmettre d'autres données de configuration spécifiques à l'environnement.

#### **Quand l'envisager** :

* Je ne recommande pas non plus cette approche. Elle impacte le temps de chargement, car l'appel HTTP initial pour récupérer les données de configuration doit être terminé avant que l'application ne puisse commencer à récupérer les données souhaitées. Considérez l'une des autres options ci-dessus à la place.

### Résumé

Créez un build par environnement via un serveur CI si vous avez besoin d'une personnalisation réelle par environnement (#2 ci-dessus). Si vous préférez déployer le même code dans chaque environnement, envisagez la configuration à l'exécution (#3 ci-dessus) ou un proxy inverse (#4 ci-dessus).

Bon codage ! ⌨️

Avez-vous d'autres façons de gérer cela ? N'hésitez pas à commenter.

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), un architecte logiciel, MVP Microsoft, et forme des développeurs logiciels à l'international sur les pratiques de développement front-end. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).