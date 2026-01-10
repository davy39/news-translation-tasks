---
title: Vous voulez rendre le processus de déploiement moins effrayant ? Construisez
  ChatOps dans Slack.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-12T05:06:44.000Z'
originalURL: https://freecodecamp.org/news/want-to-make-the-deployment-process-less-scary-build-chatops-in-slack-b2accc72e2a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C-h4AY4jHHPv9AEyND0JWQ.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Vous voulez rendre le processus de déploiement moins effrayant ? Construisez
  ChatOps dans Slack.
seo_desc: "By Rick Mak\nIn a company that makes mobile and web products, developers\
  \ shouldn’t be the only ones who can launch the latest version of an app. You need\
  \ proper testing beyond getting colleagues to give ad hoc feedback by clicking through\
  \ the app.  \nA..."
---

Par Rick Mak

Dans une entreprise qui crée des produits mobiles et web, les développeurs ne devraient pas être les seuls à pouvoir lancer la dernière version d'une application. Vous avez besoin de tests appropriés au-delà de la simple collecte de feedbacks ad hoc de la part de collègues en cliquant sur l'application. 
   
Chez [Oursky](http://www.oursky.com/), notre équipe QA a construit un [pipeline de tests automatiques](https://medium.freecodecamp.org/4-steps-to-build-an-automated-testing-pipeline-with-gitlab-ci-24ccab95535e). Mais les tests doivent être coordonnés et le rapport doit être envoyé aux personnes concernées. L'équipe QA doit savoir quand tester la dernière version de l'application. Le chef de projet doit vérifier les dernières avancées. Et le designer doit soutenir et affiner les détails. Bien que la création d'outils en ligne de commande soit la solution évidente pour les développeurs, nous voulions trouver un outil que tout le monde dans l'entreprise utilise.   
   
**Nous avons créé notre ChatOp de déploiement sur [Slack](https://slack.com/). Lisez la suite pour voir comment vous pouvez le faire avec votre service de chat. Vous pouvez automatiser votre déploiement, ce qui fait gagner du temps à tout le monde et réduit les erreurs de coordination** ([Campfire](https://campfirenow.com/), [Hipchat](https://www.hipchat.com/), et [Flowdock](https://www.flowdock.com/) sont également supportés). Nous utilisons ChatOps dans 15+ projets simultanés au sein de notre équipe.

![Image](https://cdn-media-1.freecodecamp.org/images/OSgHVDOKtykyuQ9JEme3X7NigY0umsV6Ggzw)
_Capture d'écran de nos bots Slack, Chima et Faseng (les noms de nos chats de bureau résidents)_

[ChatOps](https://speakerdeck.com/jnewland/chatops-at-github) est un excellent moyen de rendre la procédure de déploiement moins complexe, moins opaque et moins effrayante.   
   
J'ai adapté l'utilisation de ChatOps par GitHub pour notre déploiement avec Slack. Le chatbot open source de GitHub ([_Hubot_](https://github.com/hubotio/hubot)) permet d'automatiser le déploiement, la génération de graphiques, la surveillance, le provisionnement, les tweets et bien d'autres choses. GitHub a même créé des jobs de sauvegarde de bases de données MySQL afin de pouvoir effectuer des opérations importantes sans quitter la salle de chat avec un ensemble d'instructions.

![Image](https://cdn-media-1.freecodecamp.org/images/DybIY-xmClUaAGzIdQHdh26XoCdfM7VHYQ9k)

### La vue d'ensemble du déploiement ChatOps

ChatOps simplifie le déploiement avec l'automatisation : il élimine les erreurs de coordination manuelle et permet à tout le monde dans un projet de participer. Il encourage également la communication ouverte afin que les membres de l'équipe n'aient pas à s'interrompre mutuellement pour des mises à jour ou de la documentation. Ils peuvent accéder aux informations chaque fois qu'ils en ont besoin.

Alors, comment cela fonctionne-t-il et comment le configurer ?

Ce graphique montre comment les interactions de déploiement fonctionneraient via [Github](http://www.github.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/5lFj3dx1NEJbacfRzMJ7NLgESxydcB9QL47k)
_Référence : [https://developer.github.com/v3/repos/deployments/](https://developer.github.com/v3/repos/deployments/" rel="noopener" target="_blank" title=")_

Notre entreprise a mis en place une version similaire en utilisant des canaux ouverts [Slack](https://slack.com/) pour toutes nos opérations. Chaque projet a son propre canal. Nous avons introduit deux bots Slack, **Chima** et **Faseng**, pour assister le processus de déploiement. ([Chima et Faseng](https://www.facebook.com/chima.fasang/) sont les noms de nos chats de bureau résidents.)  
   
 **L'idée principale est résumée dans cette phrase :**

> `_Dites à **Chima**(CEO), de faire en sorte que **Faseng**(CTO) déploie._`

![Image](https://cdn-media-1.freecodecamp.org/images/OfZNDJeh2c1hs7k-0DqatAJziwt5jBFtHcVP)

### Rôles des bots : Création et exécution

Pour chaque projet, nous configurons des jobs de déploiement respectifs avec Faseng. Non seulement il est facile de déployer, mais les notifications de déploiement rendent le progrès et le statut du projet clairs.

![Image](https://cdn-media-1.freecodecamp.org/images/R3iYF373wiHko0066Nuj4j6CpWk-LkbPHDvn)
_Capture d'écran de Chima et Faseng (nos bots Slack)_

### Création du job de déploiement (bot de commande de chat)

Chima est un [github/hubot](https://github.com/github/hubot) qui aide à comprendre nos commandes depuis Slack. Par exemple, `chima deploy` est une commande de déploiement.  
   
 Nous devons configurer ces paramètres pour chaque projet :

* Spécifier un `provider` de déploiement tel que [Fabric](http://www.fabfile.org/), [Capistrano](http://capistranorb.com/), [Heroku](https://www.heroku.com/), ou toute tâche Ruby Rescue
* Si supporter `auto_merge` pour la branche cible de déploiement
* Le nom du `repository` du projet
* Les environnements disponibles pour le déploiement
* Seuls les membres du canal dans la liste `allowed_rooms` peuvent créer le déploiement

Nous mettons cette configuration dans le fichier **app.json**. Voici un exemple de configuration pour `project-x` :

```
{  "project-x": {    "provider": "fabric",    "auto_merge": false,    "repository": "oursky/project-x",    "environments": ["live", "edge"],    "allowed_rooms": ["deployment"]  }}
```

### Exécution du job de déploiement (bot de déploiement)

Faseng est un programme [atmos/heaven](https://github.com/atmos/heaven). Lorsqu'il reçoit des webhooks GitHub, il exécute des jobs de déploiement en tant que tâches en arrière-plan avec Resque. Il existe plusieurs façons supportées de créer des jobs de déploiement, telles que :

* [Fabric](http://www.fabfile.org/)
* [Capistrano](http://capistranorb.com/)
* [Heroku](https://www.heroku.com/)
* Toute tâche Ruby rescue
* [Lita](https://www.lita.io/) : Écrit en Ruby
* [Err](http://errbot.net/) : Écrit en Python

La création et l'achèvement des tâches de déploiement enverront des notifications dans les services de chat intégrés. [Campfire](https://campfirenow.com/), [Hipchat](https://www.hipchat.com/), [SlackHQ](https://slack.com/), et [Flowdock](https://www.flowdock.com/) peuvent recevoir des notifications d'événements de statut de déploiement.

### Cas d'utilisation dans notre entreprise

#### 1. Les développeurs l'utilisent pour déployer dans l'environnement de staging

![Image](https://cdn-media-1.freecodecamp.org/images/YapGwrkBWWBq5IoiBz5bEEVNrM9dyzjDGzEZ)

Bien que nous ayons prévu d'utiliser ChatOps pour faciliter les difficultés pour les non-développeurs, cela bénéficie également aux développeurs comme moi.   
   
Par exemple, lorsque je veux déployer `trellhub/edge` sur `pandawork`, je peux simplement taper `chima deploy trelhub/edge to pandawork` et ensuite boire un café en attendant.  
   
Pour déployer en utilisant une commande de chat, je dois configurer les paramètres d'environnement dans Chima. Pour m'assurer que le déploiement est autorisé, j'ai également donné à Faseng l'accès au serveur `pandawork`.

#### 2. La QA peut également déployer la dernière version sur l'edge

![Image](https://cdn-media-1.freecodecamp.org/images/ineCyjjOu42d8gr0PhywpxSVxPttFjflD5Kd)

Après chaque étape, l'équipe QA est responsable de la réalisation des tests fonctionnels, des tests d'utilisabilité et des tests de performance pour le logiciel pré-livrable.   
   
 Dans cet exemple, notre ingénieur QA, [Joyz](https://www.freecodecamp.org/news/want-to-make-the-deployment-process-less-scary-build-chatops-in-slack-b2accc72e2a9/undefined), veut s'assurer que la dernière version de `modmod-web` est prête sur l'environnement edge avant de lancer les tests. Elle peut déclencher le déploiement et recevoir des notifications également.

#### 3. Vérification des jobs en cours

![Image](https://cdn-media-1.freecodecamp.org/images/5p-KCMIxtualZDKOFv1GkIkwk8Y-SUaH9ZJ9)

Pour voir les jobs de construction en cours, **tout le monde** concerné par le projet peut parler à Chima et vérifier la progression de la construction Travis.  
   
Cette configuration initiale unique de ChatOps a aidé notre équipe à gérer nos projets de les manières suivantes :

* Permet aux membres moins techniques de l'équipe de contribuer au processus de développement.
* Les notifications sont poussées vers le canal de projet concerné, ce qui signifie que chaque membre de l'équipe concerné reçoit et peut accéder aux mises à jour de statut.

Nous travaillons à faire plus via ChatOps, comme la sauvegarde des serveurs et [l'exécution de tests automatiques](https://medium.freecodecamp.org/4-steps-to-build-an-automated-testing-pipeline-with-gitlab-ci-24ccab95535e). Restez à l'affût des futures mises à jour ou partagez vos conseils avec nous ! Nous serions ravis d'avoir de vos nouvelles.

### Lectures complémentaires

#### À propos de l'intégration continue

* [Issue 6: Build Tools · Issue Travis CI for iOS](http://www.objc.io/issue-6/travis-ci.html)

#### À propos du déploiement

* [Github Developer — Deployments](https://developer.github.com/v3/repos/deployments/)
* [Remote multi-server automation tool — Capistrano](https://github.com/capistrano/capistrano)
* [Python tool for streamlining deployment- Fabric](http://www.fabfile.org/)

Note de bas de page : Maintenant, nous sommes passés au déploiement déclenché par GitHub.

Vous construisez une application ? Nos [outils pour développeurs gratuits](https://oursky.com/products/) et notre [backend open source](http://skygear.io) faciliteront votre travail.

Vous avez aimé ce que vous avez lu ? Donnez-moi quelques applaudissements pour que plus de gens voient cet article ! Merci !